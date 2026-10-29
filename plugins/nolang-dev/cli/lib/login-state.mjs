// ログインの待ち受けと別プロセスの auth complete が、同じ認可を一度だけ交換する。
import { randomBytes } from "node:crypto";
import { mkdir, open, readFile, rename, rm, stat, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { setTimeout as sleep } from "node:timers/promises";
import { CliError, EXIT } from "./errors.mjs";

export async function writePrivate(path, value) {
  const temp = `${path}.${process.pid}.${randomBytes(8).toString("hex")}.tmp`;
  try {
    await writeFile(temp, JSON.stringify(value, null, 2) + "\n", { mode: 0o600, flag: "wx" });
    await rename(temp, path);
  } finally {
    await rm(temp, { force: true });
  }
}

// lockFile を排他作成できた 1 プロセスだけが action を実行する (持ち主の消えた lock は回収する)。
export async function withLock(lockFile, action, busyMessage) {
  await mkdir(dirname(lockFile), { recursive: true, mode: 0o700 });
  for (let attempt = 0; attempt < 700; attempt++) {
    let handle;
    try { handle = await open(lockFile, "wx", 0o600); }
    catch (error) {
      if (error.code !== "EEXIST") throw error;
      // 回収同士も直列化して、別プロセスが取得し直した lock を消さない。
      let recovery;
      try { recovery = await open(`${lockFile}.recovery`, "wx", 0o600); }
      catch (cause) { if (cause.code !== "EEXIST") throw cause; }
      if (recovery) {
        try {
          const pid = Number(await readFile(lockFile, "utf8"));
          if (pid > 0) {
            try { process.kill(pid, 0); }
            catch (cause) { if (cause.code === "ESRCH") await rm(lockFile, { force: true }); }
          } else if (Date.now() - (await stat(lockFile)).mtimeMs > 30000) {
            await rm(lockFile, { force: true });
          }
        } catch (cause) { if (cause.code !== "ENOENT") throw cause; }
        finally { await recovery.close(); await rm(`${lockFile}.recovery`, { force: true }); }
      }
      await sleep(50);
      continue;
    }
    try {
      await handle.writeFile(String(process.pid));
      return await action();
    } finally {
      await handle.close();
      await rm(lockFile, { force: true });
    }
  }
  throw new CliError(busyMessage, { exit: EXIT.AUTH });
}

export class LoginState {
  constructor(dir) {
    this.dir = dir;
    this.statusFile = join(dir, "login-status.json");
    this.pendingFile = join(dir, "pending-login.json");
    this.lockFile = join(dir, "login.lock");
  }

  async read(path) {
    try { return JSON.parse(await readFile(path, "utf8")); }
    catch (error) { if (error.code === "ENOENT") return null; throw error; }
  }

  status() { return this.read(this.statusFile); }
  pending() { return this.read(this.pendingFile); }

  locked(action) {
    return withLock(this.lockFile, action, "別のログイン処理が実行中です。少し待ってやり直してください");
  }

  async current(id) {
    const status = await this.status();
    if (status?.login_id !== id) throw new CliError("別のログインが開始されました。新しい案内を使ってください", { exit: EXIT.AUTH });
    return status;
  }

  start(id, api, method, expiresAt) {
    return this.locked(async () => {
      await rm(this.pendingFile, { force: true });
      await writePrivate(this.statusFile, {
        login_id: id, api, method, state: "starting", expires_at: expiresAt,
        started_at: new Date().toISOString(), pid: process.pid,
      });
    });
  }

  publish(pending, publicFields) {
    return this.locked(async () => {
      const status = await this.current(pending.login_id);
      if (status.state !== "starting") throw new CliError("このログインは終了しています。auth login からやり直してください", { exit: EXIT.AUTH });
      await writePrivate(this.pendingFile, pending);
      await writePrivate(this.statusFile, { ...status, ...publicFields, state: "waiting", pid: process.pid });
    });
  }

  complete(id, exchange) {
    return this.locked(async () => {
      const status = await this.current(id);
      if (status.state === "done") return status;
      if (status.state === "failed") throw new CliError(status.error, { exit: EXIT.AUTH });
      const pending = await this.pending();
      if (pending?.login_id !== id || Date.now() >= pending.expires_at) {
        throw new CliError("ログインの期限が切れました。auth login からやり直してください", { exit: EXIT.AUTH });
      }
      const profile = await exchange(pending);
      const done = {
        login_id: id, state: "done", api: pending.api, method: pending.method,
        access_expires_at: new Date(profile.expires_at).toISOString(),
      };
      await writePrivate(this.statusFile, done);
      await rm(this.pendingFile, { force: true });
      return done;
    });
  }

  fail(id, error) {
    return this.locked(async () => {
      const status = await this.status();
      if (status?.login_id !== id || status.state === "done") return;
      await writePrivate(this.statusFile, { login_id: id, api: status.api, method: status.method, state: "failed", error: error.message });
      await rm(this.pendingFile, { force: true });
    });
  }

  async wait(id, signal) {
    for (;;) {
      const status = await this.current(id);
      if (status.state === "done") return status;
      if (status.state === "failed") throw new CliError(status.error, { exit: EXIT.AUTH });
      if (Date.now() >= status.expires_at) throw new CliError("ログインの待ち時間を過ぎました。auth login からやり直してください", { exit: EXIT.AUTH });
      await sleep(200, undefined, { signal });
    }
  }
}

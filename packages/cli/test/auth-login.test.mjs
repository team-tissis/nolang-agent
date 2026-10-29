import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createHash } from "node:crypto";
import { mkdtemp, readFile, rm, stat, writeFile, chmod } from "node:fs/promises";
import { createServer } from "node:http";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { test } from "node:test";
import { LoginState } from "../lib/login-state.mjs";
import { DEVICE_CLIENT_ID, DEVICE_GRANT } from "../lib/device-auth.mjs";

const cli = fileURLToPath(new URL("../nolang.mjs", import.meta.url));
// 手元 (リモート・コンテナでない・画面がある) と SSH の環境を固定する — テストを走らせる端末の SSH や画面の有無に依らない
const LOCAL = { SSH_CONNECTION: "", SSH_TTY: "", REMOTE_CONTAINERS: "", CODESPACES: "", WSL_DISTRO_NAME: "", DISPLAY: ":0" };
const REMOTE = { ...LOCAL, SSH_CONNECTION: "203.0.113.1 50000 192.0.2.1 22" };

async function fixture(t, { device = false, tokenErrors = [], registerFails = false } = {}) {
  const dir = await mkdtemp(join(tmpdir(), "nolang-auth-test-"));
  const state = new LoginState(dir);
  const jobs = [];
  const opened = join(dir, "opened");
  for (const name of ["open", "xdg-open"]) {
    await writeFile(join(dir, name), `#!/bin/sh\nprintf '%s' "$1" > '${opened}'\n`);
    await chmod(join(dir, name), 0o700);
  }
  let trades = 0, approved = false, denied = false, registrations = 0;
  const server = createServer(async (req, res) => {
    let raw = "";
    for await (const chunk of req) raw += chunk;
    const form = new URLSearchParams(raw);
    const send = (body, status = 200) => res.writeHead(status, { "content-type": "application/json" }).end(JSON.stringify(body));
    if (req.url === "/.well-known/oauth-protected-resource") return send({ resource: api, authorization_servers: [api] });
    if (req.url === "/.well-known/oauth-authorization-server") return send({
      issuer: api, authorization_endpoint: `${api}/authorize`, token_endpoint: `${api}/token`, registration_endpoint: `${api}/register`,
      ...(device ? { device_authorization_endpoint: `${api}/device` } : {}), scopes_supported: ["nolang"],
    });
    if (req.url === "/register") {
      if (registerFails) return send({ error: "invalid_redirect_uri" }, 400);
      registrations++;
      return send({ client_id: "browser-client" });
    }
    if (req.url === "/device") {
      assert.equal(form.get("client_id"), DEVICE_CLIENT_ID);
      return send({ device_code: "private-device-code", user_code: "BCDF-GHJK", verification_uri: `${api}/verify`, expires_in: 10, interval: 0.05 });
    }
    if (req.url === "/token") {
      if (form.get("grant_type") === DEVICE_GRANT) {
        assert.equal(form.get("device_code"), "private-device-code");
        assert.equal(form.get("client_id"), DEVICE_CLIENT_ID);
        if (tokenErrors.length) return send({ error: "temporarily_unavailable" }, tokenErrors.shift());
        if (denied) return send({ error: "access_denied" }, 400);
        if (!approved) return send({ error: "authorization_pending" }, 400);
      } else {
        const status = await state.status();
        const url = new URL(status.authorize_url);
        assert.equal(createHash("sha256").update(form.get("code_verifier")).digest("base64url"), url.searchParams.get("code_challenge"));
        assert.equal(form.get("redirect_uri"), url.searchParams.get("redirect_uri"));
        assert.equal(form.get("code"), "test-code");
        await new Promise((r) => setTimeout(r, 100));
      }
      trades++;
      return send({ access_token: "private-access-token", refresh_token: "private-refresh-token", expires_in: 3600 });
    }
    return send({}, 401);
  });
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  const api = `http://127.0.0.1:${server.address().port}`;
  t.after(async () => {
    for (const pid of jobs) { try { process.kill(pid, "SIGTERM"); } catch {} }
    server.closeAllConnections();
    await new Promise((r) => server.close(r));
    await rm(dir, { recursive: true, force: true });
  });
  async function run(args, env = LOCAL) {
    return new Promise((resolve, reject) => {
      const child = spawn(process.execPath, [cli, ...args, "--api", api], {
        env: { ...process.env, ...env, NOLANG_TOKEN: "", NOLANG_CONFIG_DIR: dir, PATH: `${dir}:${process.env.PATH}` },
        stdio: ["ignore", "pipe", "pipe"],
      });
      let stdout = "", stderr = "";
      child.stdout.on("data", (d) => stdout += d);
      child.stderr.on("data", (d) => stderr += d);
      child.once("error", reject);
      child.once("close", (code) => resolve({ code, stdout, stderr }));
    });
  }
  async function start(args = ["--browser", "--background"], env = LOCAL) {
    const result = await run(["auth", "login", ...args], env);
    assert.equal(result.code, 0, result.stderr);
    const status = await state.status();
    if (!args.includes("--no-browser")) jobs.push(status.pid);
    return JSON.parse(result.stdout);
  }
  const callback = async (params = "code=test-code") => {
    const url = new URL((await state.status()).authorize_url);
    return `${url.searchParams.get("redirect_uri")}?${params}&state=${url.searchParams.get("state")}`;
  };
  return { dir, opened, state, run, start, callback, trades: () => trades, registrations: () => registrations, approve: () => approved = true, deny: () => denied = true };
}

test("background を auth complete で救済し、ブラウザとの競合でも PKCE 交換は一度だけ", { timeout: 20000 }, async (t) => {
  const f = await fixture(t);
  await f.start();
  assert.equal((await stat(f.state.pendingFile)).mode & 0o777, 0o600);
  const cb = await f.callback();
  const wrong = await f.run(["auth", "complete", cb.replace("state=", "state=wrong")]);
  assert.equal(wrong.code, 3);
  assert.equal(f.trades(), 0);
  const [completed, response] = await Promise.all([f.run(["auth", "complete", cb]), fetch(cb)]);
  assert.equal(completed.code, 0, completed.stderr);
  assert.equal(response.status, 200);
  assert.equal(f.trades(), 1);
  assert.equal((await f.state.status()).state, "done");
  assert.equal(await f.state.pending(), null);
  assert.equal((await f.run(["auth", "wait", "--timeout", "1"])).code, 0);
});

test("--no-browser の貼り戻しと、有効な state の拒否に対応する", { timeout: 20000 }, async (t) => {
  const f = await fixture(t);
  await f.start(["--no-browser"]);
  assert.equal((await f.run(["auth", "complete", await f.callback()])).code, 0);
  await f.start();
  assert.equal((await f.run(["auth", "complete", await f.callback("error=access_denied")])).code, 3);
  assert.equal((await f.state.status()).state, "failed");
  assert.equal(await f.state.pending(), null);
});

test("手元のエージェントの --background はブラウザを開き、コード入力なしで完了する", { timeout: 20000 }, async (t) => {
  const f = await fixture(t, { device: true });
  const shown = await f.start(["--background"]);
  assert.equal(shown.method, "browser");
  assert.equal(shown.user_code, undefined);
  assert.match(shown.tell_user, /ログイン画面を開きました/);
  assert.match(shown.next, /--device/);
  const cb = await f.callback();
  for (let i = 0; i < 50; i++) {  // 子がブラウザを開く (偽の open が URL を書く)
    try { if ((await readFile(f.opened, "utf8")).includes("/authorize")) break; } catch {}
    await new Promise((r) => setTimeout(r, 100));
  }
  assert.match(await readFile(f.opened, "utf8"), /\/authorize/);
  assert.equal((await fetch(cb)).status, 200);  // ブラウザが戻り先 (127.0.0.1) に届く
  assert.equal((await f.run(["auth", "wait", "--timeout", "5"])).code, 0);
  assert.equal(f.trades(), 1);
});

test("ブラウザ認可を始められなければ (client の登録を断られた)、デバイス認可に落ちる", { timeout: 20000 }, async (t) => {
  const f = await fixture(t, { device: true, registerFails: true });
  const shown = await f.start(["--background"]);
  assert.equal(shown.method, "device");
  assert.equal(shown.user_code, "BCDF-GHJK");
  const strict = await fixture(t, { device: true, registerFails: true });
  assert.equal((await strict.run(["auth", "login", "--browser"])).code === 0, false);  // 明示 --browser は落とさない
});

test("リモート (SSH) のエージェントは device を選び、確認前は pending・許可後に token を保存する", { timeout: 20000 }, async (t) => {
  const f = await fixture(t, { device: true });
  const shown = await f.start(["--background"], REMOTE);
  assert.equal(shown.method, "device");
  assert.equal(shown.user_code, "BCDF-GHJK");
  assert.ok(!JSON.stringify(shown).includes("private-device-code"));
  assert.equal(f.registrations(), 0);
  assert.equal(f.trades(), 0);
  assert.equal((await f.run(["auth", "wait", "--timeout", "0"])).code, 3);
  f.approve();
  assert.equal((await f.run(["auth", "wait", "--timeout", "5"])).code, 0);
  assert.equal(f.trades(), 1);
  assert.equal(await f.state.pending(), null);
  assert.ok((await readFile(join(f.dir, "credentials.json"), "utf8")).includes("private-access-token"));
  assert.ok(!(await readFile(f.state.statusFile, "utf8")).includes("private-access-token"));
});

test("device の拒否は待機終了、明示 --device は非対応サーバーで失敗する", { timeout: 20000 }, async (t) => {
  const f = await fixture(t, { device: true });
  await f.start(["--device", "--background"]);
  f.deny();
  assert.equal((await f.run(["auth", "wait", "--timeout", "5"])).code, 3);
  assert.equal((await f.state.status()).state, "failed");
  const old = await fixture(t);
  assert.equal((await old.run(["auth", "login", "--device"])).code, 3);
  const fallback = await old.start(["--background"], REMOTE);
  assert.equal(fallback.method, "browser");
  assert.match(fallback.notice, /未対応/);
});

test("古い試行や終了済みの試行が、新しいログイン状態を書き換えない", async (t) => {
  const f = await fixture(t);
  await f.state.start("old", "api", "browser", Date.now() + 10000);
  await f.state.start("new", "api", "browser", Date.now() + 10000);
  await assert.rejects(f.state.complete("old", () => assert.fail("交換してはいけない")), /別のログイン/);
  await f.state.fail("old", new Error("old error"));
  assert.equal((await f.state.status()).state, "starting");
  await f.state.fail("new", new Error("timeout"));
  await assert.rejects(f.state.publish({ login_id: "new" }, {}), /終了/);
});


test("device の poll 中の 502・503・429 は待ち時間を増やして復旧を待つ", { timeout: 20000 }, async (t) => {
  const tokenErrors = [502, 503, 429];
  const f = await fixture(t, { device: true, tokenErrors });
  await f.start(["--device", "--background"]);
  f.approve();
  const result = await f.run(["auth", "wait", "--timeout", "5"]);
  assert.equal(result.code, 0, result.stderr);
  assert.deepEqual(tokenErrors, []);
  assert.equal(f.trades(), 1);
  assert.equal((await f.state.status()).state, "done");
});

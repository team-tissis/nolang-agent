#!/usr/bin/env node
// nolang — NoLang の動画を AI エージェント (Claude Code / Codex など) から作る CLI。
// 依存なし (Node 20+)。結果は stdout に JSON、途中経過は stderr に出す。
// 裏は NoLang API (`v1/unstable/drafts/…`) と OAuth (MCP と同じ認可サーバー・同じアカウント)。

import { execFileSync, spawn } from "node:child_process";
import { createHash, randomBytes } from "node:crypto";
import { readFileSync, statSync } from "node:fs";
import { chmod, mkdir, open, readFile, rm, stat, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { homedir } from "node:os";
import { basename, dirname, join, resolve } from "node:path";
import { createInterface } from "node:readline";
import { parseArgs } from "node:util";

import { ASSET_KINDS, mimeOf, uploadKind } from "./lib/assets.mjs";
import { codeFromCallback } from "./lib/callback.mjs";
import { FALLBACK_API, TARGETS, apiUrl, chooseApi, targetName } from "./lib/config.mjs";
import { CliError, EXIT } from "./lib/errors.mjs";
import { aspectOf, pendingCuts, splitCuts } from "./lib/src.mjs";

const VERSION = JSON.parse(readFileSync(new URL("./package.json", import.meta.url), "utf8")).version;
// プラグインに入った CLI には、ビルドがそのプラグインの接続先を defaults.json (`{"api": "…"}`) として横に置く
const PACKAGED_API = (() => {
  try {
    return JSON.parse(readFileSync(new URL("./defaults.json", import.meta.url), "utf8")).api;
  } catch {
    return undefined;
  }
})();
const CONFIG_DIR = process.env.NOLANG_CONFIG_DIR || join(homedir(), ".config", "nolang");
const CRED_FILE = join(CONFIG_DIR, "credentials.json");
const PENDING_FILE = join(CONFIG_DIR, "pending-login.json");
// --background のログイン: 待ち受けは切り離した子が持ち、状態 (waiting / done / failed) をここに書く
const LOGIN_STATUS_FILE = join(CONFIG_DIR, "login-status.json");
const LOGIN_LOG_FILE = join(CONFIG_DIR, "login.log");
const LOGIN_TIMEOUT_MS = 5 * 60 * 1000;
// --background は裏で待つだけなので長めに (エージェントが原稿を書く間も切れないように)
const BACKGROUND_LOGIN_TIMEOUT_MS = 15 * 60 * 1000;
// 未ログインの時の案内。エージェントがユーザーにコマンドを打たせず、自分でログインを始めるように書く
const LOGIN_HINT = (api, what) =>
  `${what} (${api})。エージェントは \`nolang auth login --background\` で許可の URL をユーザーに渡し、許可されたら \`nolang auth wait\`。人が打つなら \`nolang auth login\``;

const log = (...args) => console.error(...args);
// tell_user と next を先頭に出す (エージェントが他の値より先に読む)
const out = ({ tell_user, next, ...rest }) =>
  process.stdout.write(JSON.stringify({ ...(tell_user ? { tell_user } : {}), ...(next ? { next } : {}), ...rest }, null, 2) + "\n");
// tell_user を返す時の next の頭 (リンクの指示を、ターンを終える指示から分けて先に置く)
const TELL_FIRST = "最優先: 次のツールを呼ぶ前に、tell_user (案内の文 + URL の行) をそのままユーザーへのメッセージに書く (省かない・要約しない・試しや計測でも同じ)";

// ---- 設定と資格情報 (~/.config/nolang/credentials.json・0600・接続先ごと) ----

async function loadStore() {
  try {
    return JSON.parse(await readFile(CRED_FILE, "utf8"));
  } catch {
    return { selected_api: null, profiles: {} };
  }
}

async function writePrivate(path, obj) {
  await mkdir(CONFIG_DIR, { recursive: true, mode: 0o700 });
  await writeFile(path, JSON.stringify(obj, null, 2) + "\n", { mode: 0o600 });
  await chmod(path, 0o600);
}

const saveStore = (store) => writePrivate(CRED_FILE, store);

async function chosenApi(flags) {
  return chooseApi({ flag: flags.api, env: process.env.NOLANG_API_URL, selected: (await loadStore()).selected_api, packaged: PACKAGED_API });
}

async function resolveApi(flags) {
  return (await chosenApi(flags)).api;
}

// ---- HTTP ----

async function request(url, init = {}) {
  try {
    return await fetch(url, init);
  } catch (error) {
    const cause = error.cause?.code || error.cause?.message || error.message;
    throw new CliError(`${url} に接続できない (${cause})。\`nolang doctor\` で接続先を確かめてください`, {
      exit: EXIT.NETWORK,
    });
  }
}

async function readBody(res) {
  const text = await res.text();
  try {
    return JSON.parse(text);
  } catch {
    return { raw: text.slice(0, 500) };
  }
}

async function getJson(url) {
  const res = await request(url, { headers: { accept: "application/json" } });
  const body = await readBody(res);
  if (!res.ok) throw new CliError(`GET ${url} → ${res.status}`, { exit: EXIT.NETWORK, data: body });
  return body;
}

async function postForm(url, form) {
  const res = await request(url, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded", accept: "application/json" },
    body: new URLSearchParams(Object.entries(form).filter(([, v]) => v != null && v !== "")).toString(),
  });
  const body = await readBody(res);
  if (!res.ok) throw new CliError(`POST ${url} → ${res.status}: ${body.error_description || body.error || ""}`, { exit: EXIT.AUTH, data: body });
  return body;
}

// ---- OAuth (RFC 9728 → 8414 → DCR 7591 → PKCE 7636・loopback 8252) ----

const b64url = (buf) => buf.toString("base64url");

async function discover(api) {
  let prmUrl = `${api}/.well-known/oauth-protected-resource`;
  // 401 の WWW-Authenticate が resource metadata の場所を教える (無ければ root の well-known)
  const probe = await request(`${api}/v1/unstable/drafts/templates/`);
  const hinted = (probe.headers.get("www-authenticate") || "").match(/resource_metadata="([^"]+)"/);
  if (hinted) prmUrl = hinted[1];
  const prm = await getJson(prmUrl);
  const issuer = (prm.authorization_servers || [])[0];
  if (!issuer) throw new CliError(`${prmUrl} に authorization_servers が無い`, { exit: EXIT.NETWORK });
  const as = await getJson(`${issuer.replace(/\/+$/, "")}/.well-known/oauth-authorization-server`);
  return { resource: prm.resource, as };
}

async function registerClient(as, redirectUri) {
  const res = await request(as.registration_endpoint, {
    method: "POST",
    headers: { "content-type": "application/json", accept: "application/json" },
    body: JSON.stringify({
      client_name: "NoLang CLI",
      redirect_uris: [redirectUri],
      grant_types: ["authorization_code", "refresh_token"],
      response_types: ["code"],
      token_endpoint_auth_method: "none",
    }),
  });
  const body = await readBody(res);
  if (!res.ok || !body.client_id) throw new CliError(`client の登録に失敗 (${res.status})`, { exit: EXIT.AUTH, data: body });
  return body.client_id;
}

function authorizeUrl(as, { clientId, redirectUri, challenge, state, resource }) {
  const url = new URL(as.authorization_endpoint);
  const params = {
    response_type: "code",
    client_id: clientId,
    redirect_uri: redirectUri,
    code_challenge: challenge,
    code_challenge_method: "S256",
    state,
    scope: (as.scopes_supported || []).join(" "),
    resource,
  };
  for (const [key, value] of Object.entries(params)) if (value) url.searchParams.set(key, value);
  return url.toString();
}

function startCallbackServer(expectedState) {
  return new Promise((resolveStart, rejectStart) => {
    let settle;
    const code = new Promise((resolveCode, rejectCode) => (settle = { resolveCode, rejectCode }));
    const server = createServer((req, res) => {
      const url = new URL(req.url, "http://127.0.0.1");
      if (url.pathname !== "/callback") {
        res.writeHead(404).end();
        return;
      }
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
      try {
        const got = codeFromCallback(url.toString(), expectedState);
        res.end("<p>NoLang にログインしました。このタブを閉じてターミナルに戻ってください。</p>");
        settle.resolveCode(got);
      } catch (error) {
        res.end("<p>ログインできませんでした。ターミナルの表示を確かめてください。</p>");
        settle.rejectCode(error);
      }
    });
    server.on("error", rejectStart);
    server.listen(0, "127.0.0.1", () => resolveStart({ server, port: server.address().port, code }));
  });
}

// ターミナルから使う人向け: ブラウザの戻り先がこの機械に届かない時 (リモート・コンテナ)、アドレスバーの URL を貼れば続く
function pastedCallback() {
  if (!process.stdin.isTTY) return new Promise(() => {});
  const rl = createInterface({ input: process.stdin });
  return new Promise((resolveLine) => rl.on("line", (line) => line.includes("code=") && (rl.close(), resolveLine(line))));
}

function openBrowser(url) {
  const [cmd, args] =
    process.platform === "darwin" ? ["open", [url]] : process.platform === "win32" ? ["cmd", ["/c", "start", "", url]] : ["xdg-open", [url]];
  try {
    spawn(cmd, args, { stdio: "ignore", detached: true }).on("error", () => {}).unref();
  } catch {
    // 開けなくても URL は表示済み
  }
}

async function saveTokens(api, base, tokens) {
  const store = await loadStore();
  store.profiles[api] = {
    ...base,
    access_token: tokens.access_token,
    refresh_token: tokens.refresh_token || base.refresh_token,
    expires_at: Date.now() + (tokens.expires_in || 3600) * 1000,
    scope: tokens.scope || base.scope,
    updated_at: new Date().toISOString(),
  };
  await saveStore(store);
  return store.profiles[api];
}

async function exchangeCode(api, pending, code) {
  const tokens = await postForm(pending.token_endpoint, {
    grant_type: "authorization_code",
    code,
    redirect_uri: pending.redirect_uri,
    client_id: pending.client_id,
    code_verifier: pending.verifier,
    resource: pending.resource,
  });
  return saveTokens(api, { client_id: pending.client_id, token_endpoint: pending.token_endpoint, resource: pending.resource }, tokens);
}

async function refreshTokens(api, profile) {
  if (!profile.refresh_token) throw new CliError(LOGIN_HINT(api, "ログインが切れた"), { exit: EXIT.AUTH });
  try {
    const tokens = await postForm(profile.token_endpoint, {
      grant_type: "refresh_token",
      refresh_token: profile.refresh_token,
      client_id: profile.client_id,
    });
    return await saveTokens(api, profile, tokens);
  } catch (error) {
    if (error.exit === EXIT.NETWORK) throw error;
    throw new CliError(LOGIN_HINT(api, "ログインが切れた"), { exit: EXIT.AUTH });
  }
}

// minValidMs = 返すトークンに残す有効時間 (他のスクリプトに渡して長く使う時)。更新すると前のトークンは無効になるので、
// 足りている間は更新しない (同じ人が並行して作る動画のトークンを切らない)
async function accessToken(api, { forceRefresh = false, minValidMs = 60_000 } = {}) {
  if (process.env.NOLANG_TOKEN) return process.env.NOLANG_TOKEN; // API key (nlg-c-…) か access token — CI 向け
  const profile = (await loadStore()).profiles[api];
  if (!profile) throw new CliError(LOGIN_HINT(api, "未ログイン"), { exit: EXIT.AUTH });
  if (forceRefresh || Date.now() > profile.expires_at - minValidMs) return (await refreshTokens(api, profile)).access_token;
  return profile.access_token;
}

// NoLang API を呼ぶ。body が FormData なら multipart (境界は fetch が付ける)。401 は 1 回だけ refresh して掛け直す
async function callApi(api, method, path, body) {
  const form = body instanceof FormData;
  const send = async (token) =>
    request(`${api}${path}`, {
      method,
      headers: {
        authorization: `Bearer ${token}`,
        accept: "application/json",
        ...(body && !form ? { "content-type": "application/json" } : {}),
      },
      body: body ? (form ? body : JSON.stringify(body)) : undefined,
    });
  let res = await send(await accessToken(api));
  if (res.status === 401 && !process.env.NOLANG_TOKEN) res = await send(await accessToken(api, { forceRefresh: true }));
  const data = await readBody(res);
  if (!res.ok) {
    const exit = res.status === 401 || res.status === 403 ? EXIT.AUTH : res.status >= 500 ? EXIT.NETWORK : EXIT.FAIL;
    throw new CliError(`${method} ${path} → ${res.status}`, { exit, data: { status: res.status, ...data } });
  }
  return data;
}

// ---- 原稿 (design.txt / timeline.txt) ----

async function readSrc(dir) {
  const root = resolve(dir || ".");
  const read = async (name) => {
    try {
      return await readFile(join(root, name), "utf8");
    } catch {
      throw new CliError(`${join(root, name)} が無い (directory に design.txt と timeline.txt を置く)`, { exit: EXIT.USAGE });
    }
  };
  return { root, design: await read("design.txt"), timeline: await read("timeline.txt") };
}

function printDefects(defects = [], findings = []) {
  for (const d of defects) log(typeof d === "string" ? d : d.text || `DEFECT:${d.code} ${d.file}:${d.line} ${d.cause}${d.fix ? `。直し方: ${d.fix}` : ""}`);
  for (const f of findings) log(`${f.severity} ${f.rule} [${f.cut}] ${f.message}${f.hint ? ` → ${f.hint}` : ""}`);
}

// ---- 状態 ----

async function waitStatus(api, videoId, until, timeoutS) {
  const deadline = Date.now() + timeoutS * 1000;
  let last = null;
  for (;;) {
    const st = await callApi(api, "GET", `/v1/videos/${videoId}/`);
    if (st.status !== last?.status || st.playable !== last?.playable) log(`status: ${st.status}${st.playable ? " (再生できる)" : ""}`);
    last = st;
    if (st.status === "failed" || st.status === "expired") return st;
    if (st.status === "completed" || (until === "playable" && st.playable)) return st;
    if (Date.now() > deadline) return { ...st, timed_out: true };
    await new Promise((r) => setTimeout(r, 5000));
  }
}

// ---- commands ----

async function readLoginStatus() {
  try {
    return JSON.parse(await readFile(LOGIN_STATUS_FILE, "utf8"));
  } catch {
    return null;
  }
}

// エージェント向け: 待ち受けを切り離した子に任せ、許可の URL が出たらすぐ戻る (長く待つコマンドを打ち切るエージェントでも使える)。
// 完了は `nolang auth wait` で確かめる
async function startBackgroundLogin(api) {
  await mkdir(CONFIG_DIR, { recursive: true, mode: 0o700 });
  await rm(LOGIN_STATUS_FILE, { force: true });
  const logFile = await open(LOGIN_LOG_FILE, "w", 0o600);
  const child = spawn(process.execPath, [process.argv[1], "auth", "login", "--detached-child", "--api", api], {
    detached: true,
    stdio: ["ignore", logFile.fd, logFile.fd],
  });
  child.unref();
  await logFile.close();
  for (let i = 0; i < 150; i++) {
    const status = await readLoginStatus();
    if (status?.state === "failed") throw new CliError(`ログインを始められなかった: ${status.error}`, { exit: EXIT.AUTH, data: status });
    if (status?.authorize_url) {
      log("ブラウザで NoLang にログインして許可してください (同じ機械ならブラウザが開いています)。許可したら `nolang auth wait`。");
      out({
        ok: true,
        api,
        waiting: true,
        authorize_url: status.authorize_url,
        // エージェントがそのままユーザーに伝える文 (コマンドの出力はユーザーに見えないことがあるので、URL ごと本文に書く)
        tell_user: `NoLang へのログインが必要です。次の URL をブラウザで開き、ログインして「許可」を押してください (15 分有効):\n${status.authorize_url}`,
        next: `${TELL_FIRST}。許可されたら nolang auth wait`,
      });
      return;
    }
    await new Promise((r) => setTimeout(r, 200));
  }
  throw new CliError(`ログインを始められなかった (30 秒で URL が出ない)。様子は ${LOGIN_LOG_FILE}`, { exit: EXIT.NETWORK });
}

async function cmdAuthLogin(flags) {
  const api = await resolveApi(flags);
  if (flags.background) return startBackgroundLogin(api);
  if (!flags["detached-child"]) return loginInBrowser(api, flags);
  // 切り離した子: 結果を状態 file に残す (前の CLI はもう居ないので、stdout ではなく file で伝える)
  try {
    await loginInBrowser(api, flags, {
      timeoutMs: BACKGROUND_LOGIN_TIMEOUT_MS,
      onUrl: (url) => writePrivate(LOGIN_STATUS_FILE, { state: "waiting", api, authorize_url: url, pid: process.pid, started_at: new Date().toISOString() }),
      onDone: (profile) => writePrivate(LOGIN_STATUS_FILE, { state: "done", api, access_expires_at: new Date(profile.expires_at).toISOString() }),
    });
  } catch (error) {
    await writePrivate(LOGIN_STATUS_FILE, { state: "failed", api, error: error.message });
    throw error;
  }
}

async function loginInBrowser(api, flags, hooks = {}) {
  const { resource, as } = await discover(api);
  const verifier = b64url(randomBytes(32));
  const challenge = b64url(createHash("sha256").update(verifier).digest());
  const state = b64url(randomBytes(16));

  if (flags["no-browser"]) {
    // 2 段: URL を出して終わる → 許可後のアドレスバーの URL を `nolang auth complete` に渡す (待ち受けない)
    const port = 20000 + Math.floor(Math.random() * 40000);
    const redirectUri = `http://127.0.0.1:${port}/callback`;
    const clientId = await registerClient(as, redirectUri);
    const url = authorizeUrl(as, { clientId, redirectUri, challenge, state, resource });
    await writePrivate(PENDING_FILE, {
      api,
      client_id: clientId,
      redirect_uri: redirectUri,
      token_endpoint: as.token_endpoint,
      resource,
      verifier,
      state,
      expires_at: Date.now() + 10 * 60 * 1000,
    });
    log("この URL をブラウザで開き、NoLang にログインして許可してください。");
    log("許可後のページは接続エラーになります。そのアドレスバーの URL を `nolang auth complete '<URL>'` に渡してください。");
    out({ ok: true, api, authorize_url: url, next: "nolang auth complete '<許可後のアドレスバーの URL>'" });
    return;
  }

  const { server, port, code } = await startCallbackServer(state);
  const redirectUri = `http://127.0.0.1:${port}/callback`;
  try {
    const clientId = await registerClient(as, redirectUri);
    const url = authorizeUrl(as, { clientId, redirectUri, challenge, state, resource });
    log("ブラウザで NoLang にログインして許可してください。開かなければこの URL を開いてください:");
    log(url);
    await hooks.onUrl?.(url);
    if (process.stdin.isTTY) log("(ブラウザが別の機械なら、許可後のアドレスバーの URL をここに貼って Enter)");
    openBrowser(url);
    const waitMs = hooks.timeoutMs ?? LOGIN_TIMEOUT_MS;
    const timeout = new Promise((_, reject) =>
      setTimeout(() => reject(new CliError(`ログインの待ち時間 (${waitMs / 60000} 分) を過ぎた`, { exit: EXIT.AUTH })), waitMs).unref(),
    );
    const got = await Promise.race([code, pastedCallback().then((line) => codeFromCallback(line, state)), timeout]);
    const profile = await exchangeCode(api, { client_id: clientId, redirect_uri: redirectUri, token_endpoint: as.token_endpoint, resource, verifier }, got);
    await hooks.onDone?.(profile);
    out({ ok: true, api, logged_in: true, expires_at: new Date(profile.expires_at).toISOString() });
  } finally {
    server.close();
  }
  process.exit(EXIT.OK); // 貼り付け待ちの stdin を閉じる
}

// --background で始めたログインの結果を待つ (既定 120 秒・エージェントの 1 回のコマンドに収まる長さ)
async function cmdAuthWait(flags) {
  const deadline = Date.now() + Number(flags.timeout || 120) * 1000;
  for (;;) {
    const status = await readLoginStatus();
    if (status?.state === "done") return out({ ok: true, api: status.api, logged_in: true, access_expires_at: status.access_expires_at });
    if (status?.state === "failed") throw new CliError(`ログインできなかった: ${status.error}`, { exit: EXIT.AUTH, data: status });
    if (!status) {
      const api = await resolveApi(flags);
      if ((await loadStore()).profiles[api]) return out({ ok: true, api, logged_in: true });
      throw new CliError("始めたログインが無い。先に `nolang auth login --background`", { exit: EXIT.AUTH });
    }
    if (Date.now() > deadline) {
      out({
        ok: false,
        waiting: true,
        api: status.api,
        authorize_url: status.authorize_url,
        tell_user: `まだログインの許可が確認できていません。次の URL をブラウザで開き、ログインして「許可」を押してから教えてください:\n${status.authorize_url}`,
        next: `${TELL_FIRST}。そこで止まる → 許可されたら、もう一度 nolang auth wait (待ち受けは開始から 15 分)`,
      });
      process.exitCode = EXIT.AUTH;
      return;
    }
    await new Promise((r) => setTimeout(r, 1000));
  }
}

async function cmdAuthComplete(positionals) {
  const callback = positionals[0];
  if (!callback) throw new CliError("使い方: nolang auth complete '<許可後のアドレスバーの URL>'", { exit: EXIT.USAGE });
  let pending;
  try {
    pending = JSON.parse(await readFile(PENDING_FILE, "utf8"));
  } catch {
    throw new CliError("始めたログインが無い。先に `nolang auth login --no-browser`", { exit: EXIT.USAGE });
  }
  if (Date.now() > pending.expires_at) throw new CliError("ログインの期限 (10 分) が切れた。`nolang auth login --no-browser` からやり直し", { exit: EXIT.AUTH });
  const profile = await exchangeCode(pending.api, pending, codeFromCallback(callback, pending.state));
  await rm(PENDING_FILE, { force: true });
  out({ ok: true, api: pending.api, logged_in: true, expires_at: new Date(profile.expires_at).toISOString() });
}

async function cmdAuthStatus(flags) {
  const api = await resolveApi(flags);
  if (process.env.NOLANG_TOKEN) return out({ api, logged_in: true, source: "NOLANG_TOKEN" });
  const profile = (await loadStore()).profiles[api];
  if (!profile) {
    out({ api, logged_in: false, next: "nolang auth login --background (エージェント) / nolang auth login (人)" });
    process.exitCode = EXIT.AUTH;
    return;
  }
  // 実際に API を 1 回叩いて確かめる (期限切れなら refresh も試す)
  await callApi(api, "GET", "/v1/unstable/drafts/templates/");
  const fresh = (await loadStore()).profiles[api];
  out({ api, logged_in: true, source: CRED_FILE, access_expires_at: new Date(fresh.expires_at).toISOString() });
}

// 他のスクリプト (studio の stream_make.sh --remote) に接続先とトークンを渡す: eval "$(nolang auth env)"。トークンは画面に出さない
async function cmdAuthEnv(flags) {
  const api = await resolveApi(flags);
  const token = await accessToken(api, { minValidMs: 20 * 60_000 });
  const q = (s) => `'${String(s).replace(/'/g, "'\\''")}'`;
  process.stdout.write(`export NOLANG_API_URL=${q(api)}\nexport NOLANG_TOKEN=${q(token)}\n`);
}

async function cmdAuthLogout(flags) {
  const api = await resolveApi(flags);
  const store = await loadStore();
  const had = Boolean(store.profiles[api]);
  delete store.profiles[api];
  await saveStore(store);
  out({ ok: true, api, removed: had });
}

// 接続先を選ぶ (名前か URL・`default` で選びを外してプラグインの接続先に戻す)。引数なしは今の接続先を見せる。ログインは接続先ごと
async function cmdUse(positionals, flags) {
  const [target] = positionals;
  const store = await loadStore();
  if (target) {
    store.selected_api = target === "default" ? null : apiUrl(target);
    await saveStore(store);
  }
  const { api, source } = await chosenApi(flags);
  const loggedIn = Boolean(process.env.NOLANG_TOKEN || store.profiles[api]);
  out({
    ok: true,
    api,
    target: targetName(api),
    source,
    logged_in: loggedIn,
    ...(loggedIn ? {} : { next: "この接続先は未ログイン — nolang auth login --background (エージェント) / nolang auth login (人)" }),
    targets: TARGETS,
  });
}

async function cmdDoctor(flags) {
  const api = await resolveApi(flags);
  const checks = [];
  const add = (name, ok, detail) => {
    checks.push({ name, ok, detail });
    log(`${ok ? "OK  " : "NG  "} ${name}${detail ? ` — ${detail}` : ""}`);
  };
  try {
    const { as } = await discover(api);
    add("API に届く・ログイン情報の案内", true, api);
    add("ログイン (OAuth) に届く", true, as.issuer);
  } catch (error) {
    add("API とログインに届く", false, `${error.message} — localhost なら SSH の LocalForward (18000 / 8000) を確かめる`);
  }
  if (checks.every((c) => c.ok)) {
    try {
      await callApi(api, "GET", "/v1/unstable/drafts/templates/");
      add("ログイン済み", true, process.env.NOLANG_TOKEN ? "NOLANG_TOKEN" : CRED_FILE);
    } catch (error) {
      add("ログイン済み", false, error.exit === EXIT.AUTH ? "未ログイン → nolang auth login" : error.message);
    }
  }
  const ok = checks.every((c) => c.ok);
  out({ ok, api, checks });
  if (!ok) process.exitCode = EXIT.FAIL;
}

async function check(api, design, timeline) {
  return callApi(api, "POST", "/v1/unstable/drafts/check/", { design, timeline, open_ended: false });
}

async function cmdCheck(positionals, flags) {
  const api = await resolveApi(flags);
  const { root, design, timeline } = await readSrc(positionals[0]);
  const result = await check(api, design, timeline);
  printDefects(result.defects, result.findings);
  const ok = !(result.defects || []).length;
  log(ok ? `check OK (${root})` : `DEFECT ${result.defects.length} 件 — 直して check し直す`);
  out({ ok, dir: root, defects: result.defects || [], findings: result.findings || [], cuts: splitCuts(design, timeline).map((c) => c.name) });
  if (!ok) process.exitCode = EXIT.FAIL;
}

async function cmdCreate(positionals, flags) {
  const { root, design, timeline } = await readSrc(positionals[0]);
  const cuts = splitCuts(design, timeline);
  const params = {
    title: flags.title || basename(root),
    aspect_ratio: flags.aspect || aspectOf(design),
    language: flags.language || "ja",
    ...(flags.seconds ? { duration_s: Number(flags.seconds) } : {}),
  };
  if (flags["dry-run"]) {
    // サーバーに触れず、開始の引数と cut ごとの投入 text だけを見せる
    out({ ok: true, dry_run: true, params, cuts });
    return;
  }

  const api = await resolveApi(flags);
  const checked = await check(api, design, timeline);
  if ((checked.defects || []).length) {
    printDefects(checked.defects, checked.findings);
    out({ ok: false, stage: "check", defects: checked.defects, findings: checked.findings || [] });
    process.exitCode = EXIT.FAIL;
    return;
  }

  const started = await callApi(api, "POST", "/v1/unstable/drafts/", params);
  const videoId = started.video_id;
  log(`開始: ${started.watch_url} (生成中から再生できる)`);
  // 投入は 1 つずつ順に (呼んだ順が動画の順)。間を 180 秒空けるとサーバーが失敗にするので、待たずに続けて流す
  for (const [index, cut] of cuts.entries()) {
    const end = index === cuts.length - 1;
    try {
      await callApi(api, "POST", `/v1/unstable/drafts/${videoId}/cuts/`, { text: cut.text, end });
    } catch (error) {
      await callApi(api, "DELETE", `/v1/unstable/drafts/${videoId}/`).catch(() => {}); // worker を空ける
      const defects = error.data?.defects || [];
      printDefects(defects);
      out({ ok: false, stage: "submit", video_id: videoId, cut: cut.name, error: error.message, defects, detail: error.data });
      process.exitCode = error.exit;
      return;
    }
    log(`cut ${index + 1}/${cuts.length} ${cut.name} 投入${end ? " (最後)" : ""}`);
  }

  // 再生できるようになるまで待って返す (エージェントはここでユーザーに知らせる)。--wait = 完成まで
  const until = flags.wait ? "completed" : "playable";
  const result = { ok: true, video_id: videoId, watch_url: started.watch_url, title: params.title, aspect_ratio: params.aspect_ratio, cuts: cuts.map((c) => c.name) };
  let st = null;
  if (until) {
    st = await waitStatus(api, videoId, until, Number(flags.timeout || (until === "completed" ? 900 : 420)));
    Object.assign(result, { status: st.status, playable: Boolean(st.playable), download_url: st.download_url || "", timed_out: Boolean(st.timed_out) });
    if (st.status === "failed" || st.status === "expired") {
      result.ok = false;
      process.exitCode = EXIT.FAIL;
    }
  }
  const url = started.watch_url;
  result.tell_user =
    st?.status === "failed" || st?.status === "expired"
      ? `動画の生成がサーバー側で失敗しました (原稿の check は通過)。video_id: ${videoId}`
      : st?.status === "completed"
        ? `動画ができました:\n${url}`
        : st?.playable
          ? `動画が再生できるようになりました (生成は続いていて、そのまま最後まで見られます):\n${url}`
          : `動画の生成を始めました。生成中から再生できます (最初の場面が描けるまで 1〜2 分):\n${url}`;
  // エージェント向け: 次のコマンドの前に tell_user をユーザーへのメッセージの本文に書く (コマンドの出力はユーザーに見えない)
  result.next = TELL_FIRST;
  out(result);
}

// ---- studio で作る (NoLang の studio と同じ段取り: 著者が cut を書いた端から、担当の書き直し → check / 直し → 投入) ----
// 再生できるかを聞く間隔 — 気づくのが遅れた分だけユーザーにリンクが届くのが遅れる (1 回の GET は軽い)
const MAKE_POLL_MS = 1000;
// studio の一式 (backend の .agents/skills/nolang-draft-studio の写し) を --remote で動かす。著者と担当は `claude -p`。
const STUDIO_TYPES = ["concept", "data", "compare", "story", "cinematic"];
const MAKE_LOG = "make.log";
// 再生できるまで待つ上限 (秒)。持ち込み音声は文字起こしを待つ分だけ長い
const MAKE_TIMEOUT_S = 420;
const MAKE_SPEECH_TIMEOUT_S = 1500;
const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

function studioDir() {
  const here = dirname(new URL(import.meta.url).pathname);
  const candidates = [process.env.NOLANG_STUDIO_DIR, join(here, "..", "studio"), join(here, "..", "..", "studio")].filter(Boolean);
  const found = candidates.find((dir) => {
    try {
      return statSync(join(dir, "scripts", "stream_make.sh")).isFile();
    } catch {
      return false;
    }
  });
  if (!found) throw new CliError("studio の一式 (studio/scripts/stream_make.sh) が見つからない — プラグインを入れ直す", { exit: EXIT.FAIL });
  return found;
}

function hasCommand(name) {
  return (process.env.PATH || "").split(":").some((dir) => {
    try {
      return statSync(join(dir, name)).isFile();
    } catch {
      return false;
    }
  });
}

async function cmdMake(positionals, flags) {
  const dir = positionals[0];
  if (!dir || !STUDIO_TYPES.includes(flags.type) || !(flags["request-text"] || flags.request)) {
    throw new CliError(`使い方: nolang make <dir> --type <${STUDIO_TYPES.join("|")}> --request-text "<依頼文>" [--aspect 16:9|9:16] [--seconds 60] [--staff medium|low (既定 medium) | --no-staff] [--editable] [--effort low] [--engine claude|codex] [--speech <音声の file か id> [--speakers N]]`, { exit: EXIT.USAGE });
  }
  const engine = flags.engine || "claude";
  if (!["claude", "codex"].includes(engine)) throw new CliError("--engine は claude / codex", { exit: EXIT.USAGE });
  for (const name of ["python3", engine]) {
    if (!hasCommand(name)) throw new CliError(`${name} が無い — studio では作れない (skill の write-yourself.md の手順で、自分で書いて流す)`, { exit: EXIT.FAIL });
  }
  if (engine === "codex") {
    const authFile = join(process.env.CODEX_HOME || join(homedir(), ".codex"), "auth.json");
    if (!await stat(authFile).then((s) => s.isFile(), () => false)) {
      throw new CliError("Codex の auth.json がありません。codex login で file 保存の認証を用意してください", { exit: EXIT.AUTH });
    }
    try {
      execFileSync("codex", ["login", "status"], { stdio: "ignore", timeout: 15000 });
    } catch {
      throw new CliError("Codex の認証を確認できません。codex login を実行してください", { exit: EXIT.AUTH });
    }
  }
  const root = resolve(dir);
  if (await stat(join(root, "stream")).then(() => true, () => false)) throw new CliError(`${root}/stream が既にある (別の dir で作る)`, { exit: EXIT.USAGE });
  const studio = studioDir();
  const api = await resolveApi(flags);
  const token = await accessToken(api, { minValidMs: 20 * 60_000 });
  await mkdir(root, { recursive: true });
  // 持ち込み音声: file なら upload して id に (id ならそのまま)。文字起こしは stream_make.sh が server に頼んで待ち、長さは音声から決まる
  let speechId = null;
  if (flags.speech) {
    if (UUID_RE.test(flags.speech)) speechId = flags.speech;
    else {
      log(`${basename(flags.speech)} を持ち込み音声として送る…`);
      speechId = await uploadSpeech(api, resolve(flags.speech), { speakers: flags.speakers, language: flags.language });
    }
  }
  const seconds = String(flags.seconds || (speechId ? "auto" : 60));
  const args = [join(studio, "scripts", "stream_make.sh"), root, "--type", flags.type, "--aspect", flags.aspect || "16:9", "--seconds", seconds];
  if (flags.engine) args.push("--engine", engine);
  if (flags.request) args.push("--request", resolve(flags.request));
  else args.push("--request-text", flags["request-text"]);
  if (flags.effort) args.push("--effort", flags.effort);
  // 既定は担当 medium (担当は絵と台詞を変えず、素材は著者の版から担当と並列に作る・直し役は DEFECT の時だけ) — 速さ優先なら --no-staff
  const staff = flags["no-staff"] ? null : flags.staff || "medium";
  if (staff) args.push("--staff", staff);
  else args.push("--no-staff");
  if (flags.editable) args.push("--editable");
  if (flags.samples) args.push("--samples", flags.samples);
  if (speechId) args.push("--speech", speechId);
  args.push("--remote", api, "--token", token);
  // macOS の bash は UTF-8 の locale で `$VAR・` の全角文字を変数名に含めて読む — bash は C・python は UTF-8 で動かす
  const logFile = await open(join(root, MAKE_LOG), "a");
  const child = spawn("bash", args, { detached: true, stdio: ["ignore", logFile.fd, logFile.fd], env: { ...process.env, LC_ALL: "C", PYTHONUTF8: "1" } });
  child.unref();
  await logFile.close();
  let exited = null;
  child.on("exit", (code) => (exited = code));
  log(`studio で作り始めた ${engine === "codex" ? "[Codex] " : ""}(${flags.type}・担当 ${staff || "なし"}・著者 ${flags.effort || "low"}${flags.editable ? "・編集可能モード" : ""}${speechId ? `・持ち込み音声 ${speechId}` : ""}) — 再生できるまで待つ (${speechId ? "文字起こしを含めて数分" : "1〜3 分"})`);
  const startedAt = Date.now();
  const deadline = startedAt + Number(flags.timeout || (speechId ? MAKE_SPEECH_TIMEOUT_S : MAKE_TIMEOUT_S)) * 1000;
  let watch = null;
  let serverPlayable = false;
  let serverFailed = null;
  let polledAt = 0;
  for (;;) {
    const runOut = await readFile(join(root, "stream", "run.out"), "utf8").catch(() => "");
    const engineFailure = engine === "codex" ? await readFile(join(root, "stream", "engine.failed"), "utf8").catch(() => "") : "";
    watch = runOut.match(/^WATCH (\S+)/m)?.[1] || watch;
    const playableLine = runOut.match(/^PLAYABLE (\S+)/m)?.[1];
    const videoId = (playableLine || watch || "").match(/[0-9a-f-]{36}/)?.[0] || null;
    // 再生できるかはサーバーに直接聞く — studio は全 cut を投入し終えてから見に行くので、PLAYABLE の行を待つと最後の cut まで遅れる
    if (videoId && !playableLine && Date.now() - polledAt >= MAKE_POLL_MS) {
      polledAt = Date.now();
      const st = await callApi(api, "GET", `/v1/videos/${videoId}/`).catch(() => null);
      serverPlayable = Boolean(st?.playable);
      if (st?.status === "failed" || st?.status === "expired") serverFailed = st.status;
    }
    const playable = playableLine || (serverPlayable ? watch : null);
    if (playable && !engineFailure) {
      log(`再生できる (${Math.round((Date.now() - startedAt) / 1000)} 秒)`);
      out({
        ok: true,
        video_id: videoId,
        watch_url: playable,
        playable: true,
        tell_user: `動画が再生できるようになりました (続きは生成しながら伸びていきます):\n${playable}`,
        next: `${TELL_FIRST}。他に頼まれていなければ、そのあとターンを終える (生成は裏で最後まで続く)`,
        log: join(root, MAKE_LOG),
      });
      return;
    }
    if (engineFailure || exited !== null || serverFailed || Date.now() > deadline) {
      const tail = (await readFile(join(root, MAKE_LOG), "utf8").catch(() => "")).split("\n").slice(-12).join("\n");
      const author = (await readFile(join(root, "stream", "author.out"), "utf8").catch(() => "")).split("\n").slice(-4).join("\n");
      const timedOut = exited === null && !serverFailed && !engineFailure;
      out({
        ok: false,
        video_id: videoId,
        watch_url: watch,
        playable: false,
        ...(watch ? { tell_user: `動画の生成を始めましたが、まだ再生できません。このページで続きを確かめてください:\n${watch}`, next: `${TELL_FIRST}。error もユーザーに伝える` } : {}),
        error: engineFailure ? `Codex の生成に失敗: ${engineFailure.trim()}` : serverFailed
          ? `サーバーで動画の生成が失敗した (status ${serverFailed})`
          : timedOut
            ? "再生できるまでの待ち時間を超えた (生成は裏で続いている事がある)"
            : `studio が終わった (exit ${exited}) — 再生まで届かなかった`,
        log_tail: tail,
        author_tail: author,
      });
      process.exitCode = EXIT.FAIL;
      return;
    }
    await new Promise((r) => setTimeout(r, MAKE_POLL_MS));
  }
}

// ---- cut ごとに流す (書いた端から投入する): start → submit → submit … → submit --end ----
// 投入の状態は原稿の dir の stream.json (video_id・投入済みの cut の名と text・最後に投入した時刻)
const STREAM_FILE = "stream.json";
const IDLE_LIMIT_S = 180; // サーバーは投入の間がこれだけ空くと生成を失敗にする

async function readStream(root) {
  try {
    return JSON.parse(await readFile(join(root, STREAM_FILE), "utf8"));
  } catch {
    throw new CliError(`${join(root, STREAM_FILE)} が無い (先に nolang start ${root})`, { exit: EXIT.USAGE });
  }
}

// server が受理済みの cut 名 (真実) と手元の台帳 (stream.json) を照合する。応答を失った投入 (server は受理したのに
// 台帳に無い) は原稿の cut を台帳へ回収する。server の名が原稿と食い違えば止める。status が読めない (古い server・
// 一時的な失敗) ときは手元の台帳のまま続ける。
async function resyncSubmitted(api, state, cuts) {
  let server = null;
  try {
    server = (await callApi(api, "GET", `/v1/unstable/drafts/${state.video_id}/`)).submitted_cuts;
  } catch {
    return;
  }
  if (!Array.isArray(server) || server.length <= state.submitted.length) return;
  for (const [index, name] of server.entries()) {
    const cut = index < state.submitted.length ? state.submitted[index] : cuts[index];
    if (!cut || cut.name !== name) {
      throw new CliError(`server の投入済み cut (${server.join(" → ")}) と手元 (台帳 + 原稿) が食い違う — 投入した cut の順と名は変えられない`, { exit: EXIT.FAIL });
    }
    if (index >= state.submitted.length) {
      state.submitted.push({ name: cut.name, text: cut.text });
      log(`cut ${cut.name} は server が受理済み (応答を失った投入) — 台帳へ回収`);
    }
  }
}

async function cmdStart(positionals, flags) {
  const { root, design } = await readSrc(positionals[0]);
  if (await stat(join(root, STREAM_FILE)).then(() => true, () => false)) {
    throw new CliError(`${join(root, STREAM_FILE)} がある (この原稿はもう開始した — 作り直すなら stream.json を消す)`, { exit: EXIT.USAGE });
  }
  const params = {
    title: flags.title || basename(root),
    aspect_ratio: flags.aspect || aspectOf(design),
    language: flags.language || "ja",
    ...(flags.seconds ? { duration_s: Number(flags.seconds) } : {}),
  };
  const api = await resolveApi(flags);
  const started = await callApi(api, "POST", "/v1/unstable/drafts/", params);
  // 接続先も残す — 途中で nolang use を切り替えても、この動画の続きは開始したサーバーへ投入する
  const state = { api, video_id: started.video_id, watch_url: started.watch_url, title: params.title, started_at: Date.now(), last_submit_at: Date.now(), submitted: [] };
  await writeFile(join(root, STREAM_FILE), JSON.stringify(state, null, 2) + "\n");
  log(`開始: ${started.video_id} — ${IDLE_LIMIT_S} 秒以内に最初の cut を nolang submit ${root}`);
  out({ ok: true, video_id: started.video_id, watch_url: started.watch_url, next: `${IDLE_LIMIT_S} 秒以内に nolang submit で最初の cut (根 + cut 1) を投入する` });
}

async function cmdSubmit(positionals, flags) {
  const { root, design, timeline } = await readSrc(positionals[0]);
  const state = await readStream(root);
  const api = flags.api ? apiUrl(flags.api) : state.api || (await resolveApi(flags));
  const cuts = splitCuts(design, timeline);
  await resyncSubmitted(api, state, cuts);
  const { pending, changed } = pendingCuts(cuts, state.submitted);
  for (const name of changed) log(`注意: 投入済みの cut ${name} が手元で変わった — サーバーには送り直せない (出した物のまま続く)`);
  if (!pending.length && !flags.end) throw new CliError("まだ投入していない cut が無い (design.txt と timeline.txt に次の cut を書き足す)", { exit: EXIT.USAGE });
  const idle = Math.round((Date.now() - state.last_submit_at) / 1000);
  if (idle > IDLE_LIMIT_S) log(`注意: 前の投入から ${idle} 秒 — ${IDLE_LIMIT_S} 秒を超えるとサーバーが生成を失敗にしている事がある`);
  const wasFirst = state.submitted.length === 0;
  const sent = [];
  const save = () => writeFile(join(root, STREAM_FILE), JSON.stringify(state, null, 2) + "\n");
  const send = async (cut, end) => {
    try {
      await callApi(api, "POST", `/v1/unstable/drafts/${state.video_id}/cuts/`, { text: cut ? cut.text : "", end });
    } catch (error) {
      // 409 = 投入の交錯 (検査した prefix が投入の前に動いた)。server が次の位置にちょうどこの cut を受理済みなら、
      // 応答を失った投入の再送 — 台帳へ回収して続ける。それ以外は server の真実を見せて止める (再実行が照合して直す)
      if (error.data?.status === 409) {
        const server = error.data.submitted_cuts;
        if (cut && Array.isArray(server) && server[state.submitted.length] === cut.name) {
          state.submitted.push({ name: cut.name, text: cut.text });
          state.last_submit_at = Date.now();
          log(`cut ${cut.name} は server が受理済み (応答を失った投入) — 台帳へ回収して続ける`);
          return true;
        }
        await save();
        out({ ok: false, video_id: state.video_id, cut: cut?.name, error: error.data?.error || error.message, submitted: state.submitted.map((c) => c.name), server_cuts: server || [], fix: "もう一度 nolang submit (server の受理状態と照合して続きから投入する)" });
        process.exitCode = EXIT.FAIL;
        return false;
      }
      await save();
      const defects = error.data?.defects || [];
      printDefects(defects);
      if (error.message.includes("No Video matches")) log("この動画はもう失敗している (投入の間が空きすぎた等) — stream.json を消して start からやり直す");
      out({ ok: false, video_id: state.video_id, cut: cut?.name, error: error.message, defects, submitted: state.submitted.map((c) => c.name), fix: "この cut だけを直して、もう一度 nolang submit (投入済みの cut は変えない)" });
      process.exitCode = error.exit;
      return false;
    }
    if (cut) {
      state.submitted.push({ name: cut.name, text: cut.text });
      sent.push(cut.name);
    }
    state.last_submit_at = Date.now();
    return true;
  };
  for (const [index, cut] of pending.entries()) {
    if (!(await send(cut, Boolean(flags.end) && index === pending.length - 1))) return;
    log(`cut ${state.submitted.length} ${cut.name} 投入${flags.end && index === pending.length - 1 ? " (最後)" : ""}`);
  }
  if (flags.end && !pending.length && !(await send(null, true))) return;
  if (flags.end) state.ended = true;
  await save();
  const url = state.watch_url;
  const result = { ok: true, video_id: state.video_id, watch_url: url, submitted: sent, total: state.submitted.length, ended: Boolean(flags.end) };
  if (wasFirst) {
    result.tell_user = `動画の生成が始まりました。最初の場面が描けると (数十秒) 再生が始まり、続きは書いた端から伸びていきます:\n${url}`;
    result.next = `${TELL_FIRST}。続けて次の cut を書き、${IDLE_LIMIT_S} 秒以内に nolang submit`;
  } else if (flags.end) {
    result.tell_user = `最後の場面まで投入しました。1〜2 分で完成します (今も最後まで再生できます):\n${url}`;
    result.next = `${TELL_FIRST}。他に頼まれていなければ、そのあとターンを終える`;
  } else {
    result.next = `次の cut を書き足して ${IDLE_LIMIT_S} 秒以内に nolang submit (最後の cut は --end)`;
  }
  out(result);
}

async function cmdStatus(positionals, flags) {
  const videoId = positionals[0];
  if (!videoId) throw new CliError("使い方: nolang status <video_id> [--wait]", { exit: EXIT.USAGE });
  const api = await resolveApi(flags);
  const st = flags.wait
    ? await waitStatus(api, videoId, flags.until || "completed", Number(flags.timeout || 900))
    : await callApi(api, "GET", `/v1/videos/${videoId}/`);
  out(st);
  if (st.status === "failed" || st.status === "expired") process.exitCode = EXIT.FAIL;
}

async function cmdAbort(positionals, flags) {
  const videoId = positionals[0];
  if (!videoId) throw new CliError("使い方: nolang abort <video_id>", { exit: EXIT.USAGE });
  out(await callApi(await resolveApi(flags), "DELETE", `/v1/unstable/drafts/${videoId}/`));
}

// ---- 素材 (検索と upload)。見つけた / 送った素材は `ref` (`id=<uuid>` など) を原稿の usage の位置に書けば使われる ----

async function cmdAssetsSearch(positionals, flags) {
  const [kind, ...words] = positionals;
  if (!ASSET_KINDS.includes(kind)) {
    throw new CliError(`使い方: nolang assets search <${ASSET_KINDS.join("|")}> "<探す物の説明か名前>" [--mine]`, { exit: EXIT.USAGE });
  }
  const query = words.join(" ");
  if (!query && !flags.mine) throw new CliError("探す物の説明か名前が要る (自分の upload の一覧なら --mine)", { exit: EXIT.USAGE });
  const params = new URLSearchParams({ kind, scope: flags.mine ? "mine" : "catalog", language: flags.language || "ja" });
  if (query) params.set("q", query);
  if (flags.limit) params.set("limit", flags.limit);
  const result = await callApi(await resolveApi(flags), "GET", `/v1/unstable/assets/search/?${params}`);
  for (const row of result.results || []) {
    const extra = [row.duration_ms ? `${(row.duration_ms / 1000).toFixed(1)}s` : "", row.width ? `${row.width}x${row.height}` : ""].filter(Boolean).join(" ");
    log(`${row.ref}  ${row.name || ""}${extra ? `  (${extra})` : ""}`);
  }
  log(`${(result.results || []).length} 件${result.degraded ? " (意味の検索が使えず表示名だけで探した)" : ""} — 書き方: ${result.usage}`);
  out(result);
}

async function uploadImage(api, path, name) {
  const form = new FormData();
  form.append("image_file", new Blob([await readFile(path)], { type: mimeOf(path) }), basename(path));
  if (name) form.append("names_by_languages", JSON.stringify({ default: name }));
  const row = await callApi(api, "POST", "/v1/unstable/assets/images/", form);
  return String(row.image_id);
}

// 動画素材・持ち込み音声: 分割 upload を始める → 各 part を S3 の presigned URL へ PUT → 確定 → 仕上げの job (尺・codec の検査と
// 変換) を待つ。route = `footages` / `speeches`・extra = 確定に足す項目・idKey = 確定の応答の素材の id の欄
async function uploadMultipart(api, path, { route, extra, idKey }) {
  const { size } = await stat(path);
  const started = await callApi(api, "POST", `/v1/unstable/assets/${route}/uploads/`, { filename: basename(path), total_size: size });
  const chunk = Number(started.chunk_size);
  const partUrls = [...started.part_urls].sort((a, b) => a.part_number - b.part_number);
  const parts = [];
  const file = await open(path, "r");
  try {
    for (const part of partUrls) {
      const offset = (part.part_number - 1) * chunk;
      const buffer = Buffer.alloc(Math.min(chunk, size - offset));
      await file.read(buffer, 0, buffer.length, offset);
      const res = await request(part.url, { method: "PUT", body: buffer });
      if (!res.ok) throw new CliError(`${basename(path)}: part ${part.part_number} の送信に失敗 (${res.status})`, { exit: EXIT.NETWORK });
      parts.push({ part_number: part.part_number, etag: res.headers.get("etag") });
      if (partUrls.length > 1) log(`  ${basename(path)}: part ${part.part_number}/${partUrls.length}`);
    }
  } finally {
    await file.close();
  }
  const done = await callApi(api, "PATCH", `/v1/unstable/assets/${route}/uploads/${started.upload_id}/`, {
    upload_id: started.upload_id,
    object_key: started.object_key,
    filename: basename(path),
    parts,
    ...extra,
  });
  const deadline = Date.now() + 600_000;
  for (;;) {
    const job = await callApi(api, "GET", `/v1/unstable/jobs/${done.job_id}/`);
    if (job.status === "succeeded") return String(done[idKey]);
    if (job.status === "failed" || job.status === "canceled") {
      throw new CliError(`${basename(path)}: 仕上げの job が ${job.status} (${job.error_code || ""})`, { exit: EXIT.FAIL, data: job });
    }
    if (Date.now() > deadline) throw new CliError(`${basename(path)}: 仕上げの job が 600 秒で終わらない (job ${done.job_id})`, { exit: EXIT.NETWORK });
    await new Promise((r) => setTimeout(r, 3000));
  }
}

function uploadFootage(api, path, name) {
  return uploadMultipart(api, path, { route: "footages", extra: name ? { name } : {}, idKey: "footage_id" });
}

// 持ち込み音声 (音声だけのファイル): speakers = 話者の人数のヒント (無ければ自動)。文字起こしは `nolang make --speech` の時に server が行う
function uploadSpeech(api, path, { speakers, language } = {}) {
  const extra = { ...(speakers ? { speaker_num: Number(speakers) } : {}), ...(language ? { language } : {}) };
  return uploadMultipart(api, path, { route: "speeches", extra, idKey: "file_id" });
}

async function cmdAssetsUpload(positionals, flags) {
  if (!positionals.length) throw new CliError("使い方: nolang assets upload <file>… [--name 表示名] [--speakers N (音声の話者の人数)]", { exit: EXIT.USAGE });
  const api = await resolveApi(flags);
  const uploaded = [];
  for (const file of positionals) {
    const path = resolve(file);
    try {
      if (!(await stat(path)).isFile()) throw new Error();
    } catch {
      throw new CliError(`${file}: file が無い`, { exit: EXIT.USAGE });
    }
    const kind = uploadKind(path);
    log(`${basename(path)} を${{ footage: "動画素材", speech: "持ち込み音声", image: "画像" }[kind]}として送る…`);
    const id =
      kind === "footage"
        ? await uploadFootage(api, path, flags.name)
        : kind === "speech"
          ? await uploadSpeech(api, path, { speakers: flags.speakers, language: flags.language })
          : await uploadImage(api, path, flags.name);
    log(`REF ${file} id=${id}`);
    uploaded.push({ file, kind, id, ref: `id=${id}` });
  }
  out({
    ok: true,
    uploaded,
    usage:
      "画像も動画素材も根に `image 名 = <ref>` を書き、置く所に `content: @名` (動画素材は `play: loop` も)。持ち込み音声は `nolang make --speech <id>` で使う",
  });
}

const HELP = `nolang ${VERSION} — NoLang の動画を AI エージェントから作る

使い方:
  nolang auth login [--no-browser]      ブラウザで NoLang にログイン (--no-browser は URL を出して終わる 2 段)
  nolang auth login --background        エージェント向け: 待ち受けを裏に回し (15 分)、許可の URL を出してすぐ戻る
  nolang auth wait [--timeout 120]      --background のログインが許可されるのを待つ (終了コード 0 でログイン済み)
  nolang auth complete '<URL>'          --no-browser の続き: 許可後のアドレスバーの URL を渡す
  nolang auth status | logout
  nolang auth env                       他のスクリプトへ接続先とトークンを渡す (eval "$(nolang auth env)" で使う・画面に出さない)
  nolang use [local|dev|stg|prod|<URL>|default]
                                        接続先を選ぶ (default = プラグインの接続先に戻す・引数なしは今の接続先)。ログインは接続先ごと
  nolang doctor                         接続先とログインを確かめる
  nolang check [dir]                    dir の design.txt / timeline.txt を検査 (DEFECT があれば終了コード 1)
  nolang create [dir] --title "…"       check → 開始 → cut を順に投入 → 再生できるまで待つ → watch_url
        [--aspect 16:9|9:16] [--seconds N] [--language ja] [--wait (完成まで)]
        [--dry-run]  サーバーに触れず、cut ごとの投入 text だけを出す
  nolang make <dir> --type <concept|data|compare|story|cinematic> --request-text "<依頼文>"
        [--aspect 16:9|9:16] [--seconds 60] [--staff medium|low (既定 medium) | --no-staff] [--editable] [--effort low] [--engine claude|codex]
                                        NoLang の studio と同じ段取りで作る (既定 Claude / codex は全役割 Codex)。再生できたら URL を返す
                                        --editable = 生成後に編集画面で調整しやすい文法サブセットに収める
        [--speech <音声の file か id> [--speakers N]]
                                        持ち込み音声 (mp3・m4a・wav など) を文字起こしし、その音声を切って使う動画にする
                                        (切り抜き・要約など。長さは音声から決まる — --seconds で目安を渡せる)
  nolang start [dir] --title "…" [--seconds N]
                                        cut ごとに流す: 開始だけ (dir に stream.json を作る)
  nolang submit [dir] [--end]           書き足した cut を投入 (最後は --end)。投入の間は 180 秒以内に
  nolang status <video_id> [--wait] [--until playable|completed] [--timeout 秒]
  nolang abort <video_id>
  nolang assets search <kind> "<説明か名前>" [--mine] [--limit N]
                                        NoLang の素材を探す (kind: image|footage|bgm|soundeffect|speaker|avatar|font)
  nolang assets upload <file>… [--name 表示名] [--speakers N]
                                        手元の画像 / 動画 (mp4・webm・mov) / 音声 (mp3・m4a・wav…) を自分の素材に送る → ref (id=<uuid>)

共通: --api <名前か URL> (無ければ NOLANG_API_URL → nolang use の接続先 → このプラグインの接続先${PACKAGED_API ? ` (${PACKAGED_API})` : ""} → ${FALLBACK_API})
接続先の名前: ${Object.entries(TARGETS).map(([name, url]) => `${name} = ${url}`).join("・")}
環境変数: NOLANG_TOKEN (API key か access token。CI 向け)・NOLANG_API_URL・NOLANG_CONFIG_DIR
出力: 結果は stdout に JSON・途中経過は stderr。終了コード 0 成功 / 1 欠陥・失敗 / 2 使い方 / 3 未ログイン / 4 接続`;

const OPTIONS = {
  api: { type: "string" },
  "no-browser": { type: "boolean" },
  background: { type: "boolean" },
  "detached-child": { type: "boolean" },
  aspect: { type: "string" },
  title: { type: "string" },
  seconds: { type: "string" },
  language: { type: "string" },
  wait: { type: "boolean" },
  until: { type: "string" },
  timeout: { type: "string" },
  "dry-run": { type: "boolean" },
  end: { type: "boolean" },
  type: { type: "string" },
  "request-text": { type: "string" },
  request: { type: "string" },
  engine: { type: "string" },
  effort: { type: "string" },
  staff: { type: "string" },
  "no-staff": { type: "boolean" },
  editable: { type: "boolean" },
  samples: { type: "string" },
  mine: { type: "boolean" },
  limit: { type: "string" },
  name: { type: "string" },
  speech: { type: "string" },
  speakers: { type: "string" },
  help: { type: "boolean", short: "h" },
  version: { type: "boolean", short: "v" },
};

async function main() {
  let parsed;
  try {
    parsed = parseArgs({ args: process.argv.slice(2), options: OPTIONS, allowPositionals: true });
  } catch (error) {
    throw new CliError(`${error.message}\n\n${HELP}`, { exit: EXIT.USAGE });
  }
  const { values: flags, positionals } = parsed;
  const [command, ...rest] = positionals;
  if (flags.version) return out({ version: VERSION });
  if (!command || flags.help) return log(HELP);
  switch (command) {
    case "auth": {
      const [sub, ...args] = rest;
      if (sub === "login") return cmdAuthLogin(flags);
      if (sub === "wait") return cmdAuthWait(flags);
      if (sub === "complete") return cmdAuthComplete(args);
      if (sub === "status") return cmdAuthStatus(flags);
      if (sub === "logout") return cmdAuthLogout(flags);
      if (sub === "env") return cmdAuthEnv(flags);
      throw new CliError(`auth の後は login | wait | complete | status | logout | env\n\n${HELP}`, { exit: EXIT.USAGE });
    }
    case "use":
      return cmdUse(rest, flags);
    case "doctor":
      return cmdDoctor(flags);
    case "check":
      return cmdCheck(rest, flags);
    case "create":
      return cmdCreate(rest, flags);
    case "status":
      return cmdStatus(rest, flags);
    case "make":
      return cmdMake(rest, flags);
    case "start":
      return cmdStart(rest, flags);
    case "submit":
      return cmdSubmit(rest, flags);
    case "abort":
      return cmdAbort(rest, flags);
    case "assets": {
      const [sub, ...args] = rest;
      if (sub === "search") return cmdAssetsSearch(args, flags);
      if (sub === "upload") return cmdAssetsUpload(args, flags);
      throw new CliError(`assets の後は search | upload\n\n${HELP}`, { exit: EXIT.USAGE });
    }
    default:
      throw new CliError(`知らないコマンド: ${command}\n\n${HELP}`, { exit: EXIT.USAGE });
  }
}

main().catch((error) => {
  if (error instanceof CliError) {
    log(`error: ${error.message}`);
    out({ ok: false, error: error.message, ...(error.data ? { detail: error.data } : {}) });
    process.exit(error.exit);
  }
  log(error.stack || String(error));
  process.exit(EXIT.NETWORK);
});

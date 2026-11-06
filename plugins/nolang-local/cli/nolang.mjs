#!/usr/bin/env node
// nolang — NoLang の動画を AI エージェント (Claude Code / Codex など) から作る CLI。
// 依存なし (Node 20+)。結果は stdout に JSON、途中経過は stderr に出す。
// 裏は NoLang の Agent API (`agent/v1/…`) と OAuth (MCP と同じ認可サーバー・同じアカウント)。

import { execFileSync, spawn } from "node:child_process";
import { createHash, randomBytes } from "node:crypto";
import { readFileSync, statSync } from "node:fs";
import { mkdir, open, readFile, rm, stat, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { homedir } from "node:os";
import { basename, dirname, join, resolve } from "node:path";
import { createInterface } from "node:readline";
import { parseArgs } from "node:util";

import { ASSET_KINDS, mimeOf, uploadKind } from "./lib/assets.mjs";
import { codeFromCallback } from "./lib/callback.mjs";
import { DEVICE_CLIENT_ID, loginMethod, pollDeviceAuthorization, validateDeviceAuthorization } from "./lib/device-auth.mjs";
import { LoginState, withLock, writePrivate as writePrivateAtomic } from "./lib/login-state.mjs";
import { FALLBACK_API, TARGETS, apiUrl, chooseApi, targetName } from "./lib/config.mjs";
import { CliError, EXIT } from "./lib/errors.mjs";
import { changedDocs, docHashes, installBundle, readContract, referenceHash } from "./lib/reference.mjs";
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
// credentials.json の読み直し → 書き込みを直列にする (並行する nolang の更新を失わない・同じ refresh token を 2 回使わない)
const CRED_LOCK_FILE = join(CONFIG_DIR, "credentials.lock");
// --background のログイン: 待ち受けは切り離した子が持ち、状態 (waiting / done / failed) をここに書く
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
  await writePrivateAtomic(path, obj);
}

const saveStore = (store) => writePrivate(CRED_FILE, store);

// lock の中で読み直した store を update に渡し、書き戻す。update の戻り値を返す (例外なら書かない)
const updateStore = (update) =>
  withLock(CRED_LOCK_FILE, async () => {
    const store = await loadStore();
    const result = await update(store);
    await saveStore(store);
    return result;
  }, "別の nolang が資格情報を更新中です。少し待ってやり直してください");

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
  const res = await request(url, { headers: { accept: "application/json" }, signal: AbortSignal.timeout(30000) });
  const body = await readBody(res);
  if (!res.ok) throw new CliError(`GET ${url} → ${res.status}`, { exit: EXIT.NETWORK, data: body });
  return body;
}

async function postForm(url, form, { signal } = {}) {
  const res = await request(url, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded", accept: "application/json" },
    body: new URLSearchParams(Object.entries(form).filter(([, v]) => v != null && v !== "")).toString(),
    signal: signal ? AbortSignal.any([signal, AbortSignal.timeout(30000)]) : AbortSignal.timeout(30000),
  });
  const body = await readBody(res);
  if (!res.ok) throw new CliError(`POST ${url} → ${res.status}: ${body.error_description || body.error || ""}`, {
    exit: res.status >= 500 || res.status === 429 ? EXIT.NETWORK : EXIT.AUTH, data: body,
  });
  return body;
}

// ---- OAuth (RFC 9728 → 8414 → DCR 7591 → PKCE 7636・loopback 8252) ----

const b64url = (buf) => buf.toString("base64url");

async function discover(api) {
  let prmUrl = `${api}/.well-known/oauth-protected-resource`;
  // 401 の WWW-Authenticate が resource metadata の場所を教える (無ければ root の well-known)
  const probe = await request(`${api}/agent/v1/templates/`, { signal: AbortSignal.timeout(30000) });
  const hinted = (probe.headers.get("www-authenticate") || "").match(/resource_metadata="([^"]+)"/);
  if (hinted) prmUrl = hinted[1];
  const prm = await getJson(prmUrl);
  const issuer = (prm.authorization_servers || [])[0];
  if (!issuer) throw new CliError(`${prmUrl} に authorization_servers が無い`, { exit: EXIT.NETWORK });
  const as = await getJson(`${issuer.replace(/\/+$/, "")}/.well-known/oauth-authorization-server`);
  // 名乗る issuer が取りに行った場所と違う metadata は使わない (別の認可サーバーの窓口へ誘導する mix-up の入口)。
  // issuer は末尾の / も含めて完全一致で比べる (RFC 8414 — 末尾だけ違う issuer は別の認可サーバー)
  if (as.issuer !== issuer) {
    throw new CliError(`${issuer} の認可サーバーの metadata が別の issuer (${as.issuer}) を名乗っています`, { exit: EXIT.AUTH });
  }
  return { resource: prm.resource, as };
}

async function registerClient(as, redirectUri) {
  const res = await request(as.registration_endpoint, {
    method: "POST",
    headers: { "content-type": "application/json", accept: "application/json" },
    signal: AbortSignal.timeout(30000),
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

function openBrowser(url) {
  const [cmd, args] =
    process.platform === "darwin" ? ["open", [url]] : process.platform === "win32" ? ["cmd", ["/c", "start", "", url]] : ["xdg-open", [url]];
  try {
    spawn(cmd, args, { stdio: "ignore", detached: true }).on("error", () => {}).unref();
  } catch {
    // 開けなくても URL は表示済み
  }
}

function tokenProfile(base, tokens) {
  if (typeof tokens.access_token !== "string" || !tokens.access_token) {
    throw new CliError("token 応答に access_token がありません", { exit: EXIT.AUTH });
  }
  return {
    ...base,
    access_token: tokens.access_token,
    refresh_token: tokens.refresh_token || base.refresh_token,
    expires_at: Date.now() + (tokens.expires_in || 3600) * 1000,
    scope: tokens.scope || base.scope,
    updated_at: new Date().toISOString(),
  };
}

const saveTokens = (api, base, tokens) => updateStore((store) => (store.profiles[api] = tokenProfile(base, tokens)));

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

// refresh token は 1 回しか使えない。lock の中で読み直し、手元の access token が staleAccess (期限が近い・401 を受けた
// token) から変わっていれば、別の nolang が更新済みなのでその token を使う
async function refreshTokens(api, staleAccess) {
  return updateStore(async (store) => {
    const profile = store.profiles[api];
    if (!profile?.refresh_token) throw new CliError(LOGIN_HINT(api, "ログインが切れた"), { exit: EXIT.AUTH });
    if (profile.access_token !== staleAccess) return profile;
    let tokens;
    try {
      tokens = await postForm(profile.token_endpoint, {
        grant_type: "refresh_token",
        refresh_token: profile.refresh_token,
        client_id: profile.client_id,
      });
    } catch (error) {
      if (error.exit === EXIT.NETWORK) throw error;
      throw new CliError(LOGIN_HINT(api, "ログインが切れた"), { exit: EXIT.AUTH });
    }
    return (store.profiles[api] = tokenProfile(profile, tokens));
  });
}

// minValidMs = 返すトークンに残す有効時間 (他のスクリプトに渡して長く使う時)。足りている間は更新しない
// (更新しても前のトークンは期限まで使えるが、渡した先は自分で更新できないので期限より長くは使えない)。
// rejected = 401 を受けた token。それを基準に更新する (同じ token の 401 が重なっても更新は 1 回)
async function accessToken(api, { rejected, minValidMs = 60_000 } = {}) {
  if (process.env.NOLANG_TOKEN) return process.env.NOLANG_TOKEN; // OAuth の access token (nolang auth env が出す) — CI 向け。API key は受けない (403)
  const profile = (await loadStore()).profiles[api];
  if (!profile) throw new CliError(LOGIN_HINT(api, "未ログイン"), { exit: EXIT.AUTH });
  if (rejected || Date.now() > profile.expires_at - minValidMs) return (await refreshTokens(api, rejected ?? profile.access_token)).access_token;
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
  const token = await accessToken(api);
  let res = await send(token);
  if (res.status === 401 && !process.env.NOLANG_TOKEN) res = await send(await accessToken(api, { rejected: token }));
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
    const st = await callApi(api, "GET", `/agent/v1/videos/${videoId}/`);
    if (st.status !== last?.status || st.playable !== last?.playable) log(`status: ${st.status}${st.playable ? " (再生できる)" : ""}`);
    // patch の直した区間 (range_render) は全尺より先に描かれる — 見られるようになった時と出来上がった時を知らせる
    const range = st.range_render ?? null;
    if (range && (range.status !== last?.range_render?.status || Boolean(range.manifest_url) !== Boolean(last?.range_render?.manifest_url))) {
      log(`range: ${range.status}${range.manifest_url ? ` (直した区間を再生できる: ${range.watch_url})` : ""}${range.mp4_url ? ` mp4 ${range.mp4_url}` : ""}`);
    }
    last = st;
    if (st.status === "failed" || st.status === "expired") return st;
    if (st.status === "completed" || (until === "playable" && st.playable)) return st;
    // range = 直した区間を再生できる所 (manifest が出た時) まで。区間が無い動画は全尺が再生できる所まで
    if (until === "range" && (range?.manifest_url || range?.status === "ready" || range?.status === "failed" || (!range && st.playable))) return st;
    if (Date.now() > deadline) return { ...st, timed_out: true };
    await new Promise((r) => setTimeout(r, 5000));
  }
}

// ---- commands ----

const loginState = new LoginState(CONFIG_DIR);
const readLoginStatus = () => loginState.status();

function loginInstructions(status) {
  const minutes = Math.max(1, Math.ceil((status.expires_at - Date.now()) / 60000));
  if (status.method === "device") {
    return {
      authorize_url: status.verification_uri,
      verification_uri: status.verification_uri,
      user_code: status.user_code,
      tell_user: `NoLang へのログインが必要です。次の URL を開き、コード ${status.user_code} を入力して許可してください (${minutes} 分以内)。いま自分で開始したログインのコードか確認してください:\n${status.verification_uri}`,
      next: `${TELL_FIRST}。許可されたら nolang auth wait`,
    };
  }
  if (status.opened) {
    return {
      authorize_url: status.authorize_url,
      ...(status.notice ? { notice: status.notice } : {}),
      tell_user: `NoLang へのログインが必要です。ブラウザで NoLang のログイン画面を開きました。ログインして「許可」を押してください (${minutes} 分以内・コードの入力はありません)。ブラウザが開かなければ、次の URL を開いてください:\n${status.authorize_url}`,
      next: `${TELL_FIRST}。許可されたら nolang auth wait。ブラウザで進めない (別の機械のブラウザしか無い・許可後に接続エラー) と言われたら nolang auth login --background --device (コードを入力する方式) でやり直す`,
    };
  }
  return {
    authorize_url: status.authorize_url,
    ...(status.notice ? { notice: status.notice } : {}),
    tell_user: `NoLang へのログインが必要です。次の URL をブラウザで開き、ログインして「許可」を押してください (${minutes} 分以内):\n${status.authorize_url}\n許可後に接続エラーになったら、そのページのアドレスバーの URL を貼ってください。ログインをやり直す必要はありません。`,
    next: `${TELL_FIRST}。許可されたら nolang auth wait。戻り先に届かなければ nolang auth complete '<許可後の URL>'`,
  };
}

const loginDone = (status) => ({ ok: true, api: status.api, logged_in: true, access_expires_at: status.access_expires_at });

async function startBackgroundLogin(api, flags, id, method) {
  const logFile = await open(LOGIN_LOG_FILE, "w", 0o600);
  const args = [process.argv[1], "auth", "login", "--detached-child", "--login-id", id, "--api", api];
  // 自動選択か明示指定かを子にも伝える (非対応サーバーへの扱いが異なる)。
  if (flags.device) args.push("--device");
  else if (flags.browser) args.push("--browser");
  else args.push("--login-method", method);
  try {
    const child = spawn(process.execPath, args, { detached: true, stdio: ["ignore", logFile.fd, logFile.fd] });
    await new Promise((resolve, reject) => { child.once("spawn", resolve); child.once("error", reject); });
    child.unref();
  } finally { await logFile.close(); }
  for (let i = 0; i < 300; i++) {
    const status = await loginState.current(id);
    if (status.state === "failed") throw new CliError(status.error, { exit: EXIT.AUTH });
    if (status.state === "done") return out(loginDone(status));
    if (status.state === "waiting") return out({ ...loginInstructions(status), ok: true, api, waiting: true, method: status.method, expires_at: status.expires_at });
    await new Promise((resolve) => setTimeout(resolve, 200));
  }
  throw new CliError(`ログインを始められませんでした。様子は ${LOGIN_LOG_FILE}`, { exit: EXIT.NETWORK });
}

async function cmdAuthLogin(flags) {
  const api = await resolveApi(flags);
  const method = loginMethod(flags);
  const id = flags["detached-child"] ? flags["login-id"] : b64url(randomBytes(16));
  if (!id) throw new CliError("ログインの識別子がありません", { exit: EXIT.USAGE });
  if (!flags["detached-child"]) {
    await loginState.start(id, api, method, Date.now() + (flags.background || flags["no-browser"] ? BACKGROUND_LOGIN_TIMEOUT_MS : LOGIN_TIMEOUT_MS));
  }
  try {
    if (flags.background) return await startBackgroundLogin(api, flags, id, method);
    await loginState.current(id);
    await runLogin(api, flags, id, flags["login-method"] || method);
  } catch (error) {
    await loginState.fail(id, error);
    throw error;
  }
}

async function runLogin(api, flags, id, method) {
  const { resource, as } = await discover(api);
  let notice;
  if (method === "device" && !as.device_authorization_endpoint) {
    if (flags.device) throw new CliError("接続先はデバイス認可に未対応です。サーバーを更新するか、auth login --browser --background で開始し、許可後の URL を auth complete に渡してください", { exit: EXIT.AUTH });
    notice = "接続先はデバイス認可に未対応のため、ブラウザ認可と URL の貼り戻しを使います";
    log(notice);
    method = "browser";
  }
  if (method === "device") return loginOnDevice(api, as, resource, id);
  const auto = !flags.browser && !flags["no-browser"];
  try {
    return await loginInBrowser(api, flags, as, resource, id, notice);
  } catch (error) {
    // 自動選択のブラウザ認可が始められない (戻り先を開けない・client の登録を断られた) — デバイス認可へ落とす
    if (!(error instanceof BrowserSetupError)) throw error;
    if (!auto || !as.device_authorization_endpoint) throw error.cause ?? error;
    log(`ブラウザ認可を始められないため、コードを入力するデバイス認可に切り替えます (${error.cause?.message ?? error.message})`);
    return loginOnDevice(api, as, resource, id);
  }
}

// ブラウザ認可の準備 (戻り先の待ち受け・client の登録) の失敗 — 自動選択ならデバイス認可へ落とす印
class BrowserSetupError extends Error {}

async function loginOnDevice(api, as, resource, id) {
  const body = validateDeviceAuthorization(await postForm(as.device_authorization_endpoint, {
    client_id: DEVICE_CLIENT_ID, scope: "nolang", resource,
  }));
  const pending = {
    login_id: id, method: "device", api, client_id: DEVICE_CLIENT_ID,
    device_code: body.device_code, token_endpoint: as.token_endpoint, resource,
    interval: body.interval, expires_at: Date.now() + body.expires_in * 1000,
  };
  await loginState.publish(pending, { method: "device", verification_uri: body.verification_uri, user_code: body.user_code, expires_at: pending.expires_at });
  const status = await loginState.current(id);
  log(loginInstructions(status).tell_user);
  // コードの確認を省かせない。verification_uri_complete は使わない。
  const tokens = await pollDeviceAuthorization(pending, postForm, { check: () => loginState.current(id) });
  const done = await loginState.complete(id, () => saveTokens(api, {
    client_id: pending.client_id, token_endpoint: pending.token_endpoint, resource,
  }, tokens));
  out(loginDone(done));
}

async function completeBrowserLogin(id, callback) {
  try {
    return await loginState.complete(id, (pending) => {
      if (pending.method !== "browser") throw new CliError("このログインはデバイス認可です。表示されたコードを認可ページに入力し、auth wait を実行してください", { exit: EXIT.USAGE });
      const code = codeFromCallback(callback, pending.state, pending.redirect_uri, { issuer: pending.issuer, issRequired: pending.iss_required });
      return exchangeCode(pending.api, pending, code);
    });
  } catch (error) {
    // state と戻り先を検証済みの拒否は、貼り戻しでも待ち受けでも同じ終了状態にする。
    if (error.data?.error === "access_denied") await loginState.fail(id, error);
    throw error;
  }
}

async function loginInBrowser(api, flags, as, resource, id, notice) {
  const verifier = b64url(randomBytes(32));
  const challenge = b64url(createHash("sha256").update(verifier).digest());
  const state = b64url(randomBytes(16));
  const controller = new AbortController();
  let server;
  let readline;
  let port = 20000 + Math.floor(Math.random() * 40000);
  if (!flags["no-browser"]) {
    server = createServer(async (req, res) => {
      const callback = new URL(req.url, `http://127.0.0.1:${server.address().port}`);
      if (callback.pathname !== "/callback") { res.writeHead(404).end(); return; }
      if (callback.searchParams.get("state") !== state) { res.writeHead(400).end("Invalid state"); return; }
      try {
        await completeBrowserLogin(id, callback.toString());
        res.writeHead(200, { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" }).end("<p>NoLang にログインしました。このタブを閉じてください。</p>");
      } catch (error) {
        res.writeHead(400, { "content-type": "text/html; charset=utf-8", "cache-control": "no-store" }).end("<p>ログインできませんでした。ターミナルの表示を確認してください。</p>");
      }
    });
    try {
      await new Promise((resolve, reject) => { server.once("error", reject); server.listen(0, "127.0.0.1", resolve); });
    } catch (error) {
      throw new BrowserSetupError("戻り先を開けない", { cause: error });
    }
    port = server.address().port;
  }
  try {
    const redirectUri = `http://127.0.0.1:${port}/callback`;
    let clientId;
    try {
      clientId = await registerClient(as, redirectUri);
    } catch (error) {
      throw new BrowserSetupError("client を登録できない", { cause: error });
    }
    const url = authorizeUrl(as, { clientId, redirectUri, challenge, state, resource });
    const status = await loginState.current(id);
    const pending = {
      login_id: id, method: "browser", api, client_id: clientId, redirect_uri: redirectUri,
      token_endpoint: as.token_endpoint, resource, verifier, state, expires_at: status.expires_at,
      issuer: as.issuer, iss_required: as.authorization_response_iss_parameter_supported === true,
    };
    await loginState.publish(pending, { method: "browser", authorize_url: url, ...(flags["no-browser"] ? {} : { opened: true }), ...(notice ? { notice } : {}) });
    const instructions = loginInstructions(await loginState.current(id));
    if (flags["no-browser"]) return out({ ...instructions, ok: true, api, waiting: true, method: "browser" });
    log(instructions.tell_user);
    if (process.stdin.isTTY) {
      log("許可後の URL をこのターミナルに貼って Enter でも完了できます。");
      readline = createInterface({ input: process.stdin });
      readline.on("line", (line) => {
        if (!line.includes("code=") && !line.includes("error=")) return;
        completeBrowserLogin(id, line).catch((error) => log(error.message));
      });
    }
    openBrowser(url);
    out(loginDone(await loginState.wait(id, controller.signal)));
  } finally {
    controller.abort();
    readline?.close();
    process.stdin.pause();
    server?.close();
  }
}

async function cmdAuthWait(flags) {
  const timeout = Number(flags.timeout ?? 120);
  if (!Number.isFinite(timeout) || timeout < 0) throw new CliError("--timeout は 0 以上の秒数です", { exit: EXIT.USAGE });
  const deadline = Date.now() + timeout * 1000;
  for (;;) {
    const status = await readLoginStatus();
    if (status?.state === "done") return out(loginDone(status));
    if (status?.state === "failed") throw new CliError(`ログインできませんでした: ${status.error}`, { exit: EXIT.AUTH });
    if (!status) throw new CliError("始めたログインがありません。先に auth login --background を実行してください", { exit: EXIT.AUTH });
    if (Date.now() >= status.expires_at) throw new CliError("ログインの期限が切れました。auth login からやり直してください", { exit: EXIT.AUTH });
    if (Date.now() >= deadline) {
      out({ ...(status.state === "waiting" ? loginInstructions(status) : {}), ok: false, waiting: true, api: status.api, method: status.method });
      process.exitCode = EXIT.AUTH;
      return;
    }
    await new Promise((resolve) => setTimeout(resolve, 200));
  }
}

async function cmdAuthComplete(positionals) {
  const callback = positionals[0];
  if (!callback) throw new CliError("使い方: nolang auth complete '<許可後のアドレスバーの URL>'", { exit: EXIT.USAGE });
  const pending = await loginState.pending();
  if (!pending) throw new CliError("待機中のログインがありません。先に auth login を実行してください", { exit: EXIT.USAGE });
  // callback の任意の URL へアクセスしない。保存済み endpoint に PKCE 付きで交換する。
  out(loginDone(await completeBrowserLogin(pending.login_id, callback)));
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
  await callApi(api, "GET", "/agent/v1/templates/");
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

// サーバーでも失効させる (RFC 7009・同じ認可から出た token をまとめて)。失敗の理由を返す (成功は null)
async function revokeOnServer(as, profile) {
  if (!as.revocation_endpoint) return "接続先がトークンの取り消しに未対応です";
  try {
    await postForm(as.revocation_endpoint, { token: profile.refresh_token || profile.access_token, client_id: profile.client_id });
    return null;
  } catch (error) {
    return error.message;
  }
}

async function cmdAuthLogout(flags) {
  const api = await resolveApi(flags);
  if (!(await loadStore()).profiles[api]) return out({ ok: true, api, removed: false, revoked: false });
  // 窓口を探す通信は lock の外 (lock を握るのは取り消しの 1 回だけにして、並行する nolang を長く待たせない)
  let as;
  let failure = null;
  try { ({ as } = await discover(api)); } catch (error) { failure = error.message; }
  // 取り消しと削除は lock の中: 待つ間に別の nolang が更新していても、その最新の token で取り消す。届かなくても手元からは消す
  const removed = await updateStore(async (store) => {
    const profile = store.profiles[api];
    if (profile && !failure) failure = await revokeOnServer(as, profile);
    delete store.profiles[api];
    return Boolean(profile);
  });
  out({
    ok: true, api, removed, revoked: removed && !failure,
    ...(removed && failure ? { note: `手元のトークンは消しましたが、サーバー側の取り消しに失敗しました: ${failure}` } : {}),
  });
}

// 接続先を選ぶ (名前か URL・`default` で選びを外してプラグインの接続先に戻す)。引数なしは今の接続先を見せる。ログインは接続先ごと
async function cmdUse(positionals, flags) {
  const [target] = positionals;
  const store = target
    ? await updateStore((saved) => { saved.selected_api = target === "default" ? null : apiUrl(target); return saved; })
    : await loadStore();
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
      await callApi(api, "GET", "/agent/v1/templates/");
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
  return callApi(api, "POST", "/agent/v1/drafts/check/", { design, timeline, open_ended: false });
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

// --seconds は秒数か auto (= 指定なし・台本の分量と内容に合わせる)。数字でも auto でもなければ使い方エラー
function parseSeconds(value) {
  if (value === undefined || value === "auto") return null;
  if (!/^[1-9]\d*$/.test(value)) throw new CliError(`--seconds は秒数か auto: ${value}`, { exit: EXIT.USAGE });
  return Number(value);
}

async function cmdCreate(positionals, flags) {
  const { root, design, timeline } = await readSrc(positionals[0]);
  const cuts = splitCuts(design, timeline);
  const durationS = parseSeconds(flags.seconds);
  const params = {
    title: flags.title || basename(root),
    aspect_ratio: flags.aspect || aspectOf(design),
    language: flags.language || "ja",
    ...(durationS ? { duration_s: durationS } : {}),
    ...clientContract(),
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

  const started = await callApi(api, "POST", "/agent/v1/drafts/", params);
  const videoId = started.video_id;
  log(`開始: ${started.watch_url} (生成中から再生できる)`);
  // 投入は 1 つずつ順に (呼んだ順が動画の順)。間を 180 秒空けるとサーバーが失敗にするので、待たずに続けて流す
  for (const [index, cut] of cuts.entries()) {
    const end = index === cuts.length - 1;
    try {
      await callApi(api, "POST", `/agent/v1/drafts/${videoId}/cuts/`, { text: cut.text, end });
    } catch (error) {
      await callApi(api, "DELETE", `/agent/v1/drafts/${videoId}/`).catch(() => {}); // worker を空ける
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
// studio の出力 (stream/run.out) を見直す間隔 — 手元の file を読むだけなので短くてよい
const MAKE_POLL_MS = 1000;
// サーバーに再生できるかを聞く間隔。気づくのが遅れた分だけリンクが遅れるが、本番の回数制限と無駄な負荷を考えて 3 秒にする
const MAKE_SERVER_POLL_MS = 3000;
// studio の一式 (backend の .agents/skills/nolang-draft-studio の写し) を --remote で動かす。著者と担当は `claude -p`。
const STUDIO_TYPES = ["concept", "data", "compare", "story", "cinematic"];
const MAKE_LOG = "make.log";
// 再生できるまで待つ上限 (秒)。持ち込み音声は文字起こしを待つ分だけ長い。super は著者 high とレビューの分だけ再生開始が遅い
// (6〜10 分) が、エージェントの Bash の上限 (10 分) より短くする — 超えても生成中なら still_generating でリンクを返す
const MAKE_TIMEOUT_S = 420;
const MAKE_SUPER_TIMEOUT_S = 570;
const MAKE_SPEECH_TIMEOUT_S = 1500;
// 開始時に出す「再生できるまで」の目安 (mode ごと)
const MAKE_PLAYBACK_ESTIMATE = { light: "1〜3 分", standard: "1〜3 分", plus: "2〜4 分", super: "6〜10 分" };
const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

// 焼き込みの文書一式の段取りの版 (studio/reference/contract.json の contract)。drafts/ の開始に添え、server の受ける範囲の外なら
// server が課金の前に DRAFT_CLIENT_CONTRACT_UNSUPPORTED で止める (版の整合 — backend の reference_sync.md)。studio が無ければ送らない
function clientContract() {
  try {
    const contract = JSON.parse(readFileSync(join(studioDir(), "reference", "contract.json"), "utf8")).contract;
    return Number.isInteger(contract) ? { client_contract: contract } : {};
  } catch {
    return {};
  }
}

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

// 直し役 (--fix) の flag — 検証して studio へそのまま渡す (make / edit 共通)。値は直す指摘の段 (effort は low 固定)。
// 旧 `--fix low` (warn の直し + レビュー) のレビューは 10-30 に外した — warn まで直すなら `--fix warn`
function fixArgs(flags) {
  const fix = flags.fix || "severe";
  if (!["defect", "severe", "warn", "none"].includes(fix)) {
    throw new CliError(
      ["low", "medium", "high", "xhigh"].includes(fix)
        ? "--fix は直す指摘の段 (defect / severe / warn / none)。warn まで直すなら --fix warn"
        : "--fix は defect / severe / warn / none",
      { exit: EXIT.USAGE },
    );
  }
  const review = flags.review || "none";
  if (!["low", "medium", "none"].includes(review)) throw new CliError("--review は low / medium / none", { exit: EXIT.USAGE });
  if (review !== "none" && fix === "none") throw new CliError("--review は直し役の機構で直す — --fix none とは併用できない", { exit: EXIT.USAGE });
  return [...(flags.fix ? ["--fix", flags.fix] : []), ...(flags.review ? ["--review", flags.review] : [])];
}

async function cmdMake(positionals, flags) {
  const dir = positionals[0];
  if (!dir || !STUDIO_TYPES.includes(flags.type) || !(flags["request-text"] || flags.request)) {
    throw new CliError(`使い方: nolang make <dir> --type <${STUDIO_TYPES.join("|")}> --request-text "<依頼文>" [--aspect 16:9|9:16] [--seconds 秒|auto (既定 auto)] [--author low|medium|high|xhigh (著者の effort)] [--author-brief] [--staff balanced|low|medium|high|xhigh|none (既定 balanced)] [--staff-warn] [--editable] [--engine claude|codex] [--mode light|standard|plus|super] [--review low|medium|none] [--fix defect|severe|warn|none] [--staff-assets] [--speech <音声の file か id> [--speakers N]]`, { exit: EXIT.USAGE });
  }
  const engine = flags.engine || "claude";
  if (!["claude", "codex"].includes(engine)) throw new CliError("--engine は claude / codex", { exit: EXIT.USAGE });
  parseSeconds(flags.seconds); // 形だけ検査 (studio へは文字列のまま渡す)
  const seconds = String(flags.seconds || "auto"); // 既定 auto = 台本の分量と内容に合わせる
  // --mode = 役の flag の組 (engine の stream_make.sh が展開する・明示の役の flag が上書き)
  const mode = flags.mode || null;
  if (mode && !["light", "standard", "plus", "super"].includes(mode)) throw new CliError("--mode は light / standard / plus / super", { exit: EXIT.USAGE });
  const staff = flags.staff || null; // 書かなければ engine の既定 (balanced・--mode があればその組)
  if (staff && !["balanced", "low", "medium", "high", "xhigh", "none"].includes(staff)) throw new CliError("--staff は balanced / low / medium / high / xhigh / none", { exit: EXIT.USAGE });
  // 著者 brief: 著者は台本 (台詞) と cut ごとの絵コンテだけを書き、絵は cut ごとの担当がゼロから設計する。
  // effort (--author) とは直交 — brief の著者の深さも --author で選ぶ。
  // 担当が素材も変える形に固定 (engine が --staff-edits-assets を含意) なので、担当なしとは両立しない
  const brief = Boolean(flags["author-brief"]);
  if (flags.author && !["low", "medium", "high", "xhigh"].includes(flags.author)) {
    throw new CliError(
      flags.author === "brief"
        ? "--author brief は --author-brief になった (--author は著者の effort: low / medium / high / xhigh)"
        : "--author は low / medium / high / xhigh",
      { exit: EXIT.USAGE },
    );
  }
  if (brief && staff === "none") throw new CliError("--author-brief は担当が各 cut を仕上げる前提 — --staff none とは併用できない", { exit: EXIT.USAGE });
  const roleArgs = fixArgs(flags);
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
  const args = [join(studio, "scripts", "stream_make.sh"), root, "--type", flags.type, "--aspect", flags.aspect || "16:9", "--seconds", seconds];
  if (flags.engine) args.push("--engine", engine);
  if (flags.request) args.push("--request", resolve(flags.request));
  else args.push("--request-text", flags["request-text"]);
  if (mode) args.push("--mode", mode);
  if (brief) args.push("--author-brief");
  if (flags.author) args.push("--author", flags.author);
  // 既定は担当 balanced (cut 1・2 は low・cut 3 以降は medium が再生に間に合う見込みの時だけ medium。担当は絵と台詞を変えず、素材は著者の版から担当と並列に作る・直し役は DEFECT の時だけ) — 質を優先するなら --staff medium / high / xhigh か --mode plus / super・速さ最優先なら --staff none (= --mode light)
  if (staff) args.push("--staff", staff);
  if (flags["staff-warn"]) args.push("--staff-warn");
  if (flags.editable) args.push("--editable");
  if (flags.samples) args.push("--samples", flags.samples);
  // 直し役 (fixArgs で検証済み)・担当が絵と台詞も変える
  args.push(...roleArgs);
  if (flags["staff-assets"]) args.push("--staff-assets");
  if (speechId) args.push("--speech", speechId);
  args.push("--remote", api, "--token", token);
  log(`studio で作り始めた ${engine === "codex" ? "[Codex] " : ""}(${flags.type}・${seconds === "auto" ? "長さ auto" : `${seconds} 秒`}${mode ? `・mode ${mode}` : ""}${staff ? `・担当 ${staff === "none" ? "なし" : staff}` : ""}${flags.author ? `・著者 ${flags.author}` : ""}${brief ? " (brief = 台詞と絵コンテだけ)" : ""}${flags.editable ? "・編集可能モード" : ""}${speechId ? `・持ち込み音声 ${speechId}` : ""}) — 再生できるまで待つ (${speechId ? "文字起こしを含めて数分" : MAKE_PLAYBACK_ESTIMATE[mode || "standard"]})`);
  await runStudioAndWait(root, args, api, {
    engine,
    // 待ち時間の優先: --timeout の指定 → 持ち込み音声 (文字起こしを待つ・runStudioAndWait の既定) → super → 既定
    timeout: flags.timeout || (!speechId && mode === "super" ? MAKE_SUPER_TIMEOUT_S : null),
    speech: Boolean(speechId),
  });
}

// stream_make.sh を裏で起こし、再生できるまで待って out() する (make / edit 共通の待ち方)
async function runStudioAndWait(root, args, api, { engine = "claude", timeout, speech = false } = {}) {
  // macOS の bash は UTF-8 の locale で `$VAR・` の全角文字を変数名に含めて読む — bash は C・python は UTF-8 で動かす
  const logFile = await open(join(root, MAKE_LOG), "a");
  const child = spawn("bash", args, { detached: true, stdio: ["ignore", logFile.fd, logFile.fd], env: { ...process.env, LC_ALL: "C", PYTHONUTF8: "1" } });
  child.unref();
  await logFile.close();
  let exited = null;
  child.on("exit", (code) => (exited = code));
  const startedAt = Date.now();
  const deadline = startedAt + Number(timeout || (speech ? MAKE_SPEECH_TIMEOUT_S : MAKE_TIMEOUT_S)) * 1000;
  let watch = null;
  let serverPlayable = false;
  let serverFailed = null;
  let polledAt = 0;
  let waiting = null;
  for (;;) {
    const runOut = await readFile(join(root, "stream", "run.out"), "utf8").catch(() => "");
    const engineFailure = engine === "codex" ? await readFile(join(root, "stream", "engine.failed"), "utf8").catch(() => "") : "";
    // 開始が本人の同時生成の上限で断られ、studio が枠の空きを待っている (送り直すごとに 1 行・経過秒つき) — 行が変わった時だけ出す
    const waitingLine = runOut.match(/^WAITING .+$/gm)?.at(-1) || null;
    if (waitingLine && waitingLine !== waiting) log(waitingLine);
    waiting = waitingLine;
    watch = runOut.match(/^WATCH (\S+)/m)?.[1] || watch;
    const playableLine = runOut.match(/^PLAYABLE (\S+)/m)?.[1];
    const videoId = (playableLine || watch || "").match(/[0-9a-f-]{36}/)?.[0] || null;
    // 再生できるかはサーバーに直接聞く — studio は全 cut を投入し終えてから見に行くので、PLAYABLE の行を待つと最後の cut まで遅れる
    if (videoId && !playableLine && Date.now() - polledAt >= MAKE_SERVER_POLL_MS) {
      polledAt = Date.now();
      const st = await callApi(api, "GET", `/agent/v1/videos/${videoId}/`).catch(() => null);
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
      const makeLog = await readFile(join(root, MAKE_LOG), "utf8").catch(() => "");
      // edit の「変更なし」(exit 0): patch の対象が無かっただけで失敗ではない — 項目ごとの判定を返す
      if (exited === 0 && !watch && /^edit: 変更なし/m.test(makeLog)) {
        let verdict = null;
        try {
          verdict = JSON.parse(await readFile(join(root, "edit", "verdict.json"), "utf8"));
        } catch { /* 判定 file が無い・壊れている時は verdict なしで返す */ }
        out({
          ok: true,
          no_change: true,
          verdict,
          tell_user: "依頼のうち、この動画の変更になる項目はありませんでした (動画はそのまま)。",
          next: `${TELL_FIRST}。verdict の各項目 (rebuild / asset / impossible と why) を平易に伝える`,
          log: join(root, MAKE_LOG),
        });
        return;
      }
      const tail = makeLog.split("\n").slice(-12).join("\n");
      const author = (await readFile(join(root, "stream", "author.out"), "utf8").catch(() => "")).split("\n").slice(-4).join("\n");
      const timedOut = exited === null && !serverFailed && !engineFailure;
      // 待ち時間を超えても、動画が始まっていてサーバーが失敗にしていなければ生成は裏で続いている — 失敗として返さない
      if (timedOut && watch) {
        log(`待ち時間を超えたが生成中 (${Math.round((Date.now() - startedAt) / 1000)} 秒)`);
        out({
          ok: true,
          video_id: videoId,
          watch_url: watch,
          playable: false,
          still_generating: true,
          tell_user: `動画を生成中です。再生できるまでもう少しかかります。このページで続きを確かめてください:\n${watch}`,
          next: `${TELL_FIRST}。他に頼まれていなければ、そのあとターンを終える (生成は裏で最後まで続く)`,
          log: join(root, MAKE_LOG),
        });
        return;
      }
      // engine の失敗 (サーバーが開始を断った理由・traceback) は make.log ではなく run.out に出る
      const runTail = runOut.split("\n").slice(-12).join("\n");
      const startRefused = runOut.match(/^開始できない: (.+)$/m)?.[1];
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
            : startRefused
              ? `サーバーが生成の開始を断った: ${startRefused}`
              : `studio が終わった (exit ${exited}) — 再生まで届かなかった`,
        log_tail: tail,
        run_tail: runTail,
        author_tail: author,
      });
      process.exitCode = EXIT.FAIL;
      return;
    }
    await new Promise((r) => setTimeout(r, MAKE_POLL_MS));
  }
}

// ---- 完成した動画を直す (stored src を種に、著者を飛ばして編集役が依頼のぶんだけ patch) ----
// patch にならない依頼 (作り直し級・編集役の失敗) は stream_make.sh がそのまま参照つきの著者経路に倒す
async function cmdEdit(positionals, flags) {
  const dir = positionals[0];
  const videoId = (positionals[1] || "").match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/i)?.[0];
  if (!dir || !videoId || !(flags["request-text"] || flags.request)) {
    throw new CliError(`使い方: nolang edit <dir> <video_id か動画の URL> --request-text "<直す点>" [--fix defect|severe|warn|none] [--editable] [--engine claude|codex]`, { exit: EXIT.USAGE });
  }
  const engine = flags.engine || "claude";
  if (!["claude", "codex"].includes(engine)) throw new CliError("--engine は claude / codex", { exit: EXIT.USAGE });
  const roleArgs = fixArgs(flags);
  for (const name of ["python3", engine]) {
    if (!hasCommand(name)) throw new CliError(`${name} が無い — studio では直せない`, { exit: EXIT.FAIL });
  }
  const root = resolve(dir);
  if (await stat(join(root, "stream")).then(() => true, () => false)) throw new CliError(`${root}/stream が既にある (別の dir で)`, { exit: EXIT.USAGE });
  const studio = studioDir();
  const api = await resolveApi(flags);
  const token = await accessToken(api, { minValidMs: 20 * 60_000 });
  await mkdir(root, { recursive: true });
  const args = [join(studio, "scripts", "stream_make.sh"), root, "--edit", videoId];
  if (flags.engine) args.push("--engine", engine);
  if (flags.request) args.push("--request", resolve(flags.request));
  else args.push("--request-text", flags["request-text"]);
  args.push(...roleArgs);
  if (flags.editable) args.push("--editable");
  args.push("--remote", api, "--token", token);
  log(`編集を始めた ${engine === "codex" ? "[Codex] " : ""}(対象 ${videoId}) — patch にならない依頼は参照つきの作り直しに倒れる。再生できるまで待つ (1〜3 分)`);
  await runStudioAndWait(root, args, api, { engine, timeout: flags.timeout });
}

// ---- 完成した動画への最小の直し (patch — server の patch gate を直接叩く) ----
// 決定論の op (台詞の言い換え・見た目の宣言・素材の差し替え…) が当たる依頼だけ成立し、音声・不変 cut は再利用される。
// 成立しない依頼は stage (rebuild / clarify / unsupported / …) が返るだけで何も作らない — その時は nolang edit へ
async function cmdPatch(positionals, flags) {
  const videoId = (positionals[0] || "").match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/i)?.[0];
  if (!videoId || !flags["request-text"]) {
    throw new CliError(`使い方: nolang patch <video_id か動画の URL> --request-text "<直す点>" [--language ja] [--answered (質問に答えた再送)] [--confirmed (対応不能な節を無視して進める再送)]`, { exit: EXIT.USAGE });
  }
  const api = await resolveApi(flags);
  const body = { text: flags["request-text"] };
  if (flags.language) body.language = flags.language;
  if (flags.confirmed) body.confirmed = true;
  if (flags.answered) body.answered = true;
  log(`patch を頼んだ (対象 ${videoId}) — 決定論の編集が当たる依頼だけ成立する (判定に数秒〜30 秒)`);
  const res = await callApi(api, "POST", `/agent/v1/videos/${videoId}/patch/`, body);
  if (res.stage === "applied") {
    // 直した区間 (range_render) は全尺より先に描かれる: 既定は区間を再生できる所 (無ければ全尺が再生できる所) まで待ち、
    // 区間の視聴ページ (range_render.watch_url) を tell_user で知らせる (plugin の hook が通知にする)。
    // --until playable で従来どおり全尺が再生できるまで
    const st = await waitStatus(api, res.video_id, flags.until === "playable" ? "playable" : "range", Number(flags.timeout || 300));
    const ok = st.status !== "failed" && st.status !== "expired" && !st.timed_out;
    const range = st.range_render ?? null;
    const rangeWatchUrl = range?.manifest_url && range.watch_url ? range.watch_url : null;
    out({
      ok,
      stage: "applied",
      video_id: res.video_id,
      watch_url: res.watch_url,
      status: st.status,
      playable: Boolean(st.playable),
      range_render: range,
      ...(ok
        ? {
            tell_user: rangeWatchUrl
              ? `直した区間を今すぐ再生できます (全体の描画は続いています):\n${rangeWatchUrl}\n直しを当てた動画全体 (元の動画はそのまま・生成中から追いかけ再生):\n${res.watch_url}`
              : `直しを当てた動画ができました (元の動画はそのまま):\n${res.watch_url}`,
            next: rangeWatchUrl
              ? `${TELL_FIRST}。全体が再生できる所までは nolang status ${res.video_id} --wait --until playable (区間の mp4 は出来たら range_render.mp4_url)`
              : TELL_FIRST,
          }
        : { error: st.timed_out ? "再生できるまでの待ち時間を超えた" : `描画が ${st.status} になった` }),
    });
    if (!ok) process.exitCode = EXIT.FAIL;
    return;
  }
  if (res.stage === "clarify") {
    out({ ok: false, stage: "clarify", questions: res.questions, next: "質問の答えを指示文に足し、--answered で出し直す (質問はもう返らない)。答えが分からなければユーザーに聞く" });
    return;
  }
  if (res.stage === "unsupported") {
    out({ ok: false, stage: "unsupported", blockers: res.blockers, next: "対応不能な節を外して出し直すか、そのまま進めるなら --confirmed で再送 (節は無視される)" });
    return;
  }
  out({ ok: false, stage: res.stage, reason: res.reason ?? null, next: "patch にならない依頼 — nolang edit (保存された原稿への編集) で直す" });
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
    server = (await callApi(api, "GET", `/agent/v1/drafts/${state.video_id}/`)).submitted_cuts;
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
  const durationS = parseSeconds(flags.seconds);
  const params = {
    title: flags.title || basename(root),
    aspect_ratio: flags.aspect || aspectOf(design),
    language: flags.language || "ja",
    ...(durationS ? { duration_s: durationS } : {}),
    ...clientContract(),
  };
  const api = await resolveApi(flags);
  const started = await callApi(api, "POST", "/agent/v1/drafts/", params);
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
      await callApi(api, "POST", `/agent/v1/drafts/${state.video_id}/cuts/`, { text: cut ? cut.text : "", end });
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

// 依頼文から 1 本 (NoLang が台本と画面を書く — web の home と同じ入口)。studio を使わないので速いが細かくは作れない
async function cmdGenerate(positionals, flags) {
  const text = flags["request-text"] || positionals.join(" ");
  if (!text) {
    throw new CliError(`使い方: nolang generate --request-text "<依頼文>" [--aspect 16:9|9:16] [--seconds 秒] [--language ja] [--video-language ja] [--confirmed] [--wait]`, { exit: EXIT.USAGE });
  }
  const api = await resolveApi(flags);
  // 同じ鍵の再送は server が 1 本にする (応答を失った時の呼び直しで動画を重ねない)
  const body = { text, idempotency_key: randomBytes(16).toString("hex") };
  if (flags.aspect) body.aspect_ratio = flags.aspect;
  const durationS = parseSeconds(flags.seconds);
  if (durationS) body.duration_s = durationS;
  if (flags.language) body.language = flags.language;
  if (flags["video-language"]) body.video_language = flags["video-language"];
  if (flags.confirmed) body.confirmed = true;
  log("NoLang が台本と画面を書く (受付の判定に数秒〜30 秒)");
  const res = await callApi(api, "POST", "/agent/v1/videos/", body);
  if (res.stage !== "accepted") {
    const next =
      res.stage === "unsupported"
        ? "blockers (できない節と代案) をユーザーに見せ、そのまま作るなら --confirmed で同じ依頼を再送する"
        : res.stage === "clarify"
          ? "questions の答えを依頼文に足して出し直す (分からなければユーザーに聞く)"
          : "作れない依頼 — 依頼文を変える";
    out({ ok: false, stage: res.stage, blockers: res.blockers, questions: res.questions, next });
    if (res.stage !== "unsupported" && res.stage !== "clarify") process.exitCode = EXIT.FAIL;
    return;
  }
  const videoId = res.video_id;
  log(`開始: ${res.watch_url} (生成中から再生できる)`);
  const until = flags.wait ? "completed" : "playable";
  const st = await waitStatus(api, videoId, until, Number(flags.timeout || (until === "completed" ? 900 : 420)));
  const failed = st.status === "failed" || st.status === "expired";
  out({
    ok: !failed,
    video_id: videoId,
    watch_url: res.watch_url,
    status: st.status,
    playable: Boolean(st.playable),
    download_url: st.download_url || "",
    timed_out: Boolean(st.timed_out),
    tell_user: failed
      ? `動画の生成がサーバー側で失敗しました。video_id: ${videoId}`
      : st.status === "completed"
        ? `動画ができました:\n${res.watch_url}`
        : st.playable
          ? `動画が再生できるようになりました (生成は続いていて、そのまま最後まで見られます):\n${res.watch_url}`
          : `動画の生成を始めました。生成中から再生できます (最初の場面が描けるまで 1〜2 分):\n${res.watch_url}`,
    next: TELL_FIRST,
  });
  if (failed) process.exitCode = EXIT.FAIL;
}

async function cmdStatus(positionals, flags) {
  const videoId = positionals[0];
  if (!videoId) throw new CliError("使い方: nolang status <video_id> [--wait]", { exit: EXIT.USAGE });
  const api = await resolveApi(flags);
  const st = flags.wait
    ? await waitStatus(api, videoId, flags.until || "completed", Number(flags.timeout || 900))
    : await callApi(api, "GET", `/agent/v1/videos/${videoId}/`);
  out(st);
  if (st.status === "failed" || st.status === "expired") process.exitCode = EXIT.FAIL;
}

// 焼き込みの文書一式 (studio/reference/) を server の版と照合する — 自分で書く経路 (write-yourself.md §1 の 0) が書く前に 1 回。
// 一致なら焼き込みの dir、ずれていれば server の束を cache (NOLANG_CONFIG_DIR/reference/<指紋>/ — `nolang make` の取り直しと共有)
// に置いてその dir を返す。changed = 文書ごとの指紋が違う文書 (server が文書ごとの指紋を返さなければ null)
async function cmdReference(flags) {
  const api = await resolveApi(flags);
  const baked = join(studioDir(), "reference");
  const { contract } = await readContract(baked);
  const { sync } = await callApi(api, "GET", "/agent/v1/rules/");
  if (!sync) {
    log("接続先の server は文書の版を返さない (古い server) — 焼き込みの文書で書く");
    return out({ status: "unknown", dir: baked, changed: null });
  }
  if (contract < sync.min_supported || contract > sync.contract) {
    throw new CliError(
      contract < sync.min_supported
        ? `このプラグインの段取り (contract ${contract}) は server が受ける範囲 (${sync.min_supported} 以上) より古い — プラグインを更新する`
        : `このプラグインの段取り (contract ${contract}) は server (${sync.contract}) より新しい — server の更新を待つか、接続先を確かめる`,
      { exit: EXIT.FAIL, data: { contract, sync } },
    );
  }
  if ((await referenceHash(baked)) === sync.reference_hash) return out({ status: "match", dir: baked, changed: [] });
  const changed = sync.docs ? changedDocs(await docHashes(baked), sync.docs) : null;
  const dest = join(CONFIG_DIR, "reference", sync.reference_hash);
  let status = "cached";
  if (!(await stat(join(dest, "contract.json")).catch(() => null))) {
    const path = "/agent/v1/reference/";
    const res = await request(`${api}${path}`, { headers: { authorization: `Bearer ${await accessToken(api)}` } });
    // 取れない (束を配らない server・一時の失敗) → 焼き込みで続ける。終了コード 1 は contract の止まれだけに使う (手順が書かずに止まる)
    if (!res.ok) {
      log(`server の文書を取れなかった (GET ${path} → ${res.status}) — 焼き込みの文書で書く (文書と check が食い違う所は check に従う)`);
      return out({ status: "unknown", dir: baked, changed });
    }
    await mkdir(dirname(dest), { recursive: true });
    await installBundle(Buffer.from(await res.arrayBuffer()), sync.reference_hash, dest);
    status = "fetched";
  }
  log(`プラグインの文書は server より古い — server の現行の文書を ${dest} に置いた${changed ? ` (変わった文書: ${changed.join(" ") || "なし"})` : ""}`);
  out({ status, dir: dest, changed });
}

async function cmdAbort(positionals, flags) {
  const videoId = positionals[0];
  if (!videoId) throw new CliError("使い方: nolang abort <video_id>", { exit: EXIT.USAGE });
  out(await callApi(await resolveApi(flags), "DELETE", `/agent/v1/drafts/${videoId}/`));
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
  const result = await callApi(await resolveApi(flags), "GET", `/agent/v1/assets/search/?${params}`);
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
  const row = await callApi(api, "POST", "/agent/v1/assets/images/", form);
  return String(row.image_id);
}

// 動画素材・持ち込み音声: 分割 upload を始める → 各 part を S3 の presigned URL へ PUT → 確定 → 仕上げの job (尺・codec の検査と
// 変換) を待つ。route = `footages` / `speeches`・extra = 確定に足す項目・idKey = 確定の応答の素材の id の欄
async function uploadMultipart(api, path, { route, extra, idKey }) {
  const { size } = await stat(path);
  const started = await callApi(api, "POST", `/agent/v1/assets/${route}/uploads/`, { filename: basename(path), total_size: size });
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
  const done = await callApi(api, "PATCH", `/agent/v1/assets/${route}/uploads/${started.upload_id}/`, {
    upload_id: started.upload_id,
    object_key: started.object_key,
    filename: basename(path),
    parts,
    ...extra,
  });
  const deadline = Date.now() + 600_000;
  for (;;) {
    const job = await callApi(api, "GET", `/agent/v1/jobs/${done.job_id}/`);
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
  nolang auth login [--device | --browser | --no-browser]
                                        手元はブラウザ認可 (ブラウザが開く・コード入力なし)、SSH・コンテナ・画面の無い環境はデバイス認可 (コード入力)
  nolang auth login --background        認可待ちを裏に回し、案内 (デバイス認可ではコードも) を出してすぐ戻る
  nolang auth wait [--timeout 120]      --background のログインが許可されるのを待つ (終了コード 0 でログイン済み)
  nolang auth complete '<URL>'          ブラウザ認可の続き (--background / 対話ログイン / --no-browser 共通)
  nolang auth status | logout           logout はサーバー側でもトークンを取り消す
  nolang auth env                       他のスクリプトへ接続先とトークンを渡す (eval "$(nolang auth env)" で使う・画面に出さない)
  nolang use [local|dev|stg|prod|<URL>|default]
                                        接続先を選ぶ (default = プラグインの接続先に戻す・引数なしは今の接続先)。ログインは接続先ごと
  nolang doctor                         接続先とログインを確かめる
  nolang check [dir]                    dir の design.txt / timeline.txt を検査 (DEFECT があれば終了コード 1)
  nolang create [dir] --title "…"       check → 開始 → cut を順に投入 → 再生できるまで待つ → watch_url
        [--aspect 16:9|9:16] [--seconds 秒|auto (既定)] [--language ja] [--wait (完成まで)]
        [--dry-run]  サーバーに触れず、cut ごとの投入 text だけを出す
  nolang generate --request-text "<依頼文>" [--aspect 16:9|9:16] [--seconds 秒] [--language ja] [--video-language ja] [--confirmed] [--wait]
                                        NoLang が台本と画面を書く (web の home と同じ・studio を使わないので速いが細かくは作れない)。
                                        再生できたら URL を返す。stage=unsupported なら blockers を見せ、そのまま作るなら --confirmed で再送
  nolang make <dir> --type <concept|data|compare|story|cinematic> --request-text "<依頼文>"
        [--aspect 16:9|9:16] [--seconds 秒|auto (既定 auto = 内容に合わせる)] [--engine claude|codex]
        [--author low|medium|high|xhigh (著者の effort・既定 low)] [--author-brief (著者は台詞と絵コンテだけ書き、担当が絵をゼロから設計 — 台詞は著者の版で固定・--staff-assets を含意・--staff none とは併用不可。--author は brief の著者にも効く)] [--staff balanced|low|medium|high|xhigh|none (担当・既定 balanced = cut 1・2 は low・以降は再生に間に合う見込みの時だけ medium)] [--staff-warn (担当に warn の指摘も渡す)] [--editable]
                                        NoLang の studio と同じ段取りで作る (既定 Claude / codex は全役割 Codex)。再生できたら URL を返す
                                        --editable = 生成後に編集画面で調整しやすい文法サブセットに収める
        [--mode light|standard|plus|super]
                                        役の flag の組。light = 著者 low・担当なし・直し severe (速さ最優先) / standard = 既定 (著者 low・担当 balanced・
                                        直し severe) / plus = 著者 brief (low)・担当 balanced (素材も)・直し warn (長い説明系向け) / super = 著者 high
                                        (brief なし)・担当 high (素材も)・レビュー medium・直し warn (再生開始 6〜10 分・費用は plus の 2 倍)。
                                        後ろに書いた役の flag が組の値を上書きする
        [--review low|medium|none (既定 none)] [--fix defect|severe|warn|none (既定 severe)] [--staff-assets]
                                        役は 4 つ (著者・担当・レビュー・直し役)。--review = 担当の後に 1 回、cut の静止画と check の指摘全部を見て
                                        弱い所・崩れも探して直す監督 (--fix none とは併用不可)。--fix = 直し役が直す指摘の段 (severe = DEFECT と severe
                                        だけ・warn = warn も・defect = DEFECT と隠れる文字だけ・none = 直し役なし)。--staff-assets で担当が絵と台詞も変える
        [--speech <音声の file か id> [--speakers N]]
                                        持ち込み音声 (mp3・m4a・wav など) を文字起こしし、その音声を切って使う動画にする
                                        (切り抜き・要約など。長さは音声から決まる — --seconds で目安を渡せる)
  nolang patch <video_id か URL> --request-text "<直す点>" [--language ja] [--answered] [--confirmed] [--until playable]
                                        完成した動画への最小の直し (server の決定論 patch)。台詞の言い換え・見た目・素材の
                                        差し替えなどが数十秒で当たり、音声と触らない cut は再利用される。成立しない依頼は
                                        stage が返るだけで何も作らない — その時は nolang edit へ
  nolang edit <dir> <video_id か URL> --request-text "<直す点>"
        [--fix defect|severe|warn|none] [--editable] [--engine claude|codex]
                                        studio で作った完成済みの動画を直す: 保存された原稿を種に、編集役が依頼のぶんだけ書き換えて
                                        新しい動画にする (元の動画はそのまま)。patch にならない依頼 (尺・縦横・全体の作り直し級) は
                                        元の動画を参照にした作り直しに自動で倒れる。再生できたら URL を返す
  nolang reference                      手元の文書 (プラグインに焼き込み) を server の版と照合する。古ければ server の現行の文書を
                                        cache に置き、その dir (と変わった文書) を返す — 自分で書く時は以後そこを読む
  nolang start [dir] --title "…" [--seconds 秒|auto (既定)]
                                        cut ごとに流す: 開始だけ (dir に stream.json を作る)
  nolang submit [dir] [--end]           書き足した cut を投入 (最後は --end)。投入の間は 180 秒以内に
  nolang status <video_id> [--wait] [--until playable|completed|range] [--timeout 秒]
  nolang abort <video_id>
  nolang assets search <kind> "<説明か名前>" [--mine] [--limit N]
                                        NoLang の素材を探す (kind: image|footage|bgm|soundeffect|speaker|avatar|font)
  nolang assets upload <file>… [--name 表示名] [--speakers N]
                                        手元の画像 / 動画 (mp4・webm・mov) / 音声 (mp3・m4a・wav…) を自分の素材に送る → ref (id=<uuid>)

共通: --api <名前か URL> (無ければ NOLANG_API_URL → nolang use の接続先 → このプラグインの接続先${PACKAGED_API ? ` (${PACKAGED_API})` : ""} → ${FALLBACK_API})
接続先の名前: ${Object.entries(TARGETS).map(([name, url]) => `${name} = ${url}`).join("・")}
環境変数: NOLANG_TOKEN (OAuth の access token・nolang auth env が出す。CI 向け)・NOLANG_API_URL・NOLANG_CONFIG_DIR
出力: 結果は stdout に JSON・途中経過は stderr。終了コード 0 成功 / 1 欠陥・失敗 / 2 使い方 / 3 未ログイン / 4 接続`;

const OPTIONS = {
  api: { type: "string" },
  "no-browser": { type: "boolean" },
  device: { type: "boolean" },
  browser: { type: "boolean" },
  "login-id": { type: "string" },
  "login-method": { type: "string" },
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
  "video-language": { type: "string" },
  request: { type: "string" },
  engine: { type: "string" },
  author: { type: "string" },
  "author-brief": { type: "boolean" },
  mode: { type: "string" },
  staff: { type: "string" },
  "staff-warn": { type: "boolean" },
  "staff-assets": { type: "boolean" },
  editable: { type: "boolean" },
  samples: { type: "string" },
  review: { type: "string" },
  fix: { type: "string" },
  answered: { type: "boolean" },
  confirmed: { type: "boolean" },
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
    case "generate":
      return cmdGenerate(rest, flags);
    case "status":
      return cmdStatus(rest, flags);
    case "make":
      return cmdMake(rest, flags);
    case "edit":
      return cmdEdit(rest, flags);
    case "patch":
      return cmdPatch(rest, flags);
    case "reference":
      return cmdReference(flags);
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

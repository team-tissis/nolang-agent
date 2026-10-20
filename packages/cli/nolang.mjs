#!/usr/bin/env node
// nolang — NoLang の動画を AI エージェント (Claude Code / Codex など) から作る CLI。
// 依存なし (Node 20+)。結果は stdout に JSON、途中経過は stderr に出す。
// 裏は NoLang API (`v1/unstable/drafts/…`) と OAuth (MCP と同じ認可サーバー・同じアカウント)。

import { spawn } from "node:child_process";
import { createHash, randomBytes } from "node:crypto";
import { readFileSync } from "node:fs";
import { chmod, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { homedir } from "node:os";
import { basename, join, resolve } from "node:path";
import { createInterface } from "node:readline";
import { parseArgs } from "node:util";

import { codeFromCallback } from "./lib/callback.mjs";
import { CliError, EXIT } from "./lib/errors.mjs";
import { aspectOf, splitCuts } from "./lib/src.mjs";

const VERSION = JSON.parse(readFileSync(new URL("./package.json", import.meta.url), "utf8")).version;
const DEFAULT_API = "http://localhost:18000";
const CONFIG_DIR = process.env.NOLANG_CONFIG_DIR || join(homedir(), ".config", "nolang");
const CRED_FILE = join(CONFIG_DIR, "credentials.json");
const PENDING_FILE = join(CONFIG_DIR, "pending-login.json");
const LOGIN_TIMEOUT_MS = 5 * 60 * 1000;

const log = (...args) => console.error(...args);
const out = (obj) => process.stdout.write(JSON.stringify(obj, null, 2) + "\n");

// ---- 設定と資格情報 (~/.config/nolang/credentials.json・0600・接続先ごと) ----

async function loadStore() {
  try {
    return JSON.parse(await readFile(CRED_FILE, "utf8"));
  } catch {
    return { default_api: null, profiles: {} };
  }
}

async function writePrivate(path, obj) {
  await mkdir(CONFIG_DIR, { recursive: true, mode: 0o700 });
  await writeFile(path, JSON.stringify(obj, null, 2) + "\n", { mode: 0o600 });
  await chmod(path, 0o600);
}

const saveStore = (store) => writePrivate(CRED_FILE, store);

async function resolveApi(flags) {
  const raw = flags.api || process.env.NOLANG_API_URL || (await loadStore()).default_api || DEFAULT_API;
  return raw.replace(/\/+$/, "");
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
  store.default_api = api;
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
  if (!profile.refresh_token) throw new CliError(`ログインが切れた (${api})。\`nolang auth login\` をやり直してください`, { exit: EXIT.AUTH });
  try {
    const tokens = await postForm(profile.token_endpoint, {
      grant_type: "refresh_token",
      refresh_token: profile.refresh_token,
      client_id: profile.client_id,
    });
    return await saveTokens(api, profile, tokens);
  } catch (error) {
    if (error.exit === EXIT.NETWORK) throw error;
    throw new CliError(`ログインが切れた (${api})。\`nolang auth login\` をやり直してください`, { exit: EXIT.AUTH });
  }
}

async function accessToken(api, { forceRefresh = false } = {}) {
  if (process.env.NOLANG_TOKEN) return process.env.NOLANG_TOKEN; // API key (nlg-c-…) か access token — CI 向け
  const profile = (await loadStore()).profiles[api];
  if (!profile) throw new CliError(`未ログイン (${api})。\`nolang auth login\` を実行してください`, { exit: EXIT.AUTH });
  if (forceRefresh || Date.now() > profile.expires_at - 60_000) return (await refreshTokens(api, profile)).access_token;
  return profile.access_token;
}

// NoLang API を呼ぶ。401 は 1 回だけ refresh して掛け直す
async function callApi(api, method, path, body) {
  const send = async (token) =>
    request(`${api}${path}`, {
      method,
      headers: {
        authorization: `Bearer ${token}`,
        accept: "application/json",
        ...(body ? { "content-type": "application/json" } : {}),
      },
      body: body ? JSON.stringify(body) : undefined,
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

async function cmdAuthLogin(flags) {
  const api = await resolveApi(flags);
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
    if (process.stdin.isTTY) log("(ブラウザが別の機械なら、許可後のアドレスバーの URL をここに貼って Enter)");
    openBrowser(url);
    const timeout = new Promise((_, reject) =>
      setTimeout(() => reject(new CliError("ログインの待ち時間 (5 分) を過ぎた", { exit: EXIT.AUTH })), LOGIN_TIMEOUT_MS).unref(),
    );
    const got = await Promise.race([code, pastedCallback().then((line) => codeFromCallback(line, state)), timeout]);
    const profile = await exchangeCode(api, { client_id: clientId, redirect_uri: redirectUri, token_endpoint: as.token_endpoint, resource, verifier }, got);
    out({ ok: true, api, logged_in: true, expires_at: new Date(profile.expires_at).toISOString() });
  } finally {
    server.close();
  }
  process.exit(EXIT.OK); // 貼り付け待ちの stdin を閉じる
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
    out({ api, logged_in: false, next: "nolang auth login" });
    process.exitCode = EXIT.AUTH;
    return;
  }
  // 実際に API を 1 回叩いて確かめる (期限切れなら refresh も試す)
  await callApi(api, "GET", "/v1/unstable/drafts/templates/");
  const fresh = (await loadStore()).profiles[api];
  out({ api, logged_in: true, source: CRED_FILE, access_expires_at: new Date(fresh.expires_at).toISOString() });
}

async function cmdAuthLogout(flags) {
  const api = await resolveApi(flags);
  const store = await loadStore();
  const had = Boolean(store.profiles[api]);
  delete store.profiles[api];
  if (store.default_api === api) store.default_api = Object.keys(store.profiles)[0] || null;
  await saveStore(store);
  out({ ok: true, api, removed: had });
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

async function cmdTemplates(flags) {
  const api = await resolveApi(flags);
  const query = flags.aspect ? `?aspect=${encodeURIComponent(flags.aspect)}` : "";
  out(await callApi(api, "GET", `/v1/unstable/drafts/templates/${query}`));
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
    ...(flags.template ? { template_video_id: flags.template } : {}),
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

  const result = { ok: true, video_id: videoId, watch_url: started.watch_url, title: params.title, aspect_ratio: params.aspect_ratio, cuts: cuts.map((c) => c.name) };
  if (flags.wait) {
    const st = await waitStatus(api, videoId, "completed", Number(flags.timeout || 900));
    Object.assign(result, { status: st.status, playable: st.playable, download_url: st.download_url || "", timed_out: Boolean(st.timed_out) });
    if (st.status === "failed" || st.status === "expired") {
      result.ok = false;
      process.exitCode = EXIT.FAIL;
    }
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

const HELP = `nolang ${VERSION} — NoLang の動画を AI エージェントから作る

使い方:
  nolang auth login [--no-browser]      ブラウザで NoLang にログイン (--no-browser は URL を出して終わる 2 段)
  nolang auth complete '<URL>'          --no-browser の続き: 許可後のアドレスバーの URL を渡す
  nolang auth status | logout
  nolang doctor                         接続先とログインを確かめる
  nolang templates [--aspect 16:9]      素材の台帳に使えるテンプレ
  nolang check [dir]                    dir の design.txt / timeline.txt を検査 (DEFECT があれば終了コード 1)
  nolang create [dir] --title "…"       check → 開始 → cut を順に投入 → watch_url
        [--aspect 16:9|9:16] [--seconds N] [--language ja] [--template ID] [--wait]
        [--dry-run]  サーバーに触れず、cut ごとの投入 text だけを出す
  nolang status <video_id> [--wait] [--until playable|completed] [--timeout 秒]
  nolang abort <video_id>

共通: --api <URL> (既定: 前回ログインした接続先 → NOLANG_API_URL → ${DEFAULT_API})
環境変数: NOLANG_TOKEN (API key か access token。CI 向け)・NOLANG_API_URL・NOLANG_CONFIG_DIR
出力: 結果は stdout に JSON・途中経過は stderr。終了コード 0 成功 / 1 欠陥・失敗 / 2 使い方 / 3 未ログイン / 4 接続`;

const OPTIONS = {
  api: { type: "string" },
  "no-browser": { type: "boolean" },
  aspect: { type: "string" },
  title: { type: "string" },
  seconds: { type: "string" },
  language: { type: "string" },
  template: { type: "string" },
  wait: { type: "boolean" },
  until: { type: "string" },
  timeout: { type: "string" },
  "dry-run": { type: "boolean" },
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
      if (sub === "complete") return cmdAuthComplete(args);
      if (sub === "status") return cmdAuthStatus(flags);
      if (sub === "logout") return cmdAuthLogout(flags);
      throw new CliError(`auth の後は login | complete | status | logout\n\n${HELP}`, { exit: EXIT.USAGE });
    }
    case "doctor":
      return cmdDoctor(flags);
    case "templates":
      return cmdTemplates(flags);
    case "check":
      return cmdCheck(rest, flags);
    case "create":
      return cmdCreate(rest, flags);
    case "status":
      return cmdStatus(rest, flags);
    case "abort":
      return cmdAbort(rest, flags);
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

#!/usr/bin/env node
// nolang — 起動係 (bootstrap)。CLI の本体は NoLang の server が配る束 (`GET <api>/agent/client/` の tar.gz: cli/ = CLI 本体・
// scripts/ = studio・reference/ = 文書一式) で、server と一緒に変わる。ここは起動のたびに束を ETag で照合し (304 なら手元の束・
// 変わっていれば取り直して展開)、束の cli/nolang.mjs を同じ process で動かす。版番号は無い: 束の指紋 = tar.gz の sha256 = ETag。
// 束の置き場は NOLANG_CONFIG_DIR/client/<指紋>/ (既定 ~/.config/nolang)。依存なし (Node 20+)。
// 接続先の決め方は束の CLI と同じ順 (--api → NOLANG_API_URL → プラグインの defaults.json → 本番)。URL だけを受ける。
// 束 (= 実行する code) を取るのは NoLang の API host (https) と手元のスタック (localhost) からだけで、束は server の build が付けた
// Ed25519 の署名を公開鍵で検証してから動かす (localhost だけは署名の無い束も受ける — source から動く開発の stack)。
// 開発: NOLANG_CLIENT_DIR=<nolang-backend の agent_client> で、server から取らずにその checkout の CLI を動かす。
import { createHash, createPublicKey, verify } from "node:crypto";
import { existsSync, readFileSync } from "node:fs";
import { mkdir, readFile, readdir, rename, rm, stat, writeFile } from "node:fs/promises";
import { homedir } from "node:os";
import { dirname, isAbsolute, join, normalize } from "node:path";
import { pathToFileURL } from "node:url";
import { gunzipSync } from "node:zlib";

const BOOTSTRAP = JSON.parse(readFileSync(new URL("./package.json", import.meta.url), "utf8")).version;
const CONFIG_DIR = process.env.NOLANG_CONFIG_DIR || join(homedir(), ".config", "nolang");
const CLIENT_DIR = join(CONFIG_DIR, "client");
const CURRENT_FILE = join(CLIENT_DIR, "current.json"); // 接続先 → 最後に使った束の指紋
const PROD_API = "https://api.no-lang.com";
// 束 (code) を取ってよい接続先。`--api` / NOLANG_API_URL に書かれた任意の host から code を取って動かすと、エージェントに許可された
// `nolang` が任意 code の入口になるので、NoLang の API host と手元のスタック (localhost) に限る。許可の外で CLI を動かす時は
// NOLANG_CLIENT_DIR (手元の checkout・取得なし)
const BUNDLE_ORIGINS = new Set([PROD_API, "https://api-dev.no-lang.com", "https://api-stg.no-lang.com"]);
const isLocalhost = (api) => /^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(api);
// 束の署名 (Ed25519) の公開鍵 (生の 32 byte・hex) — nolang-backend の libs/ai/llm_prompts/draft_author/client_bundle.py の
// BUNDLE_PUBLIC_KEY と同じ値。鍵を替える時は新しい鍵をここに足した bootstrap を先に配り、build の秘密鍵を替えてから古い鍵を外す
const BUNDLE_PUBLIC_KEYS = ["2cb56de2d1adb85a6ec5ad2ba44b1c1d56f323c7cd923a727d041dc72ba120a7"];
const ED25519_SPKI_PREFIX = Buffer.from("302a300506032b6570032100", "hex");
// プラグインに入った bootstrap には、ビルドがそのプラグインの接続先を defaults.json (`{"api": "…"}`) として横に置く
const PACKAGED_API = (() => {
  try {
    return JSON.parse(readFileSync(new URL("./defaults.json", import.meta.url), "utf8")).api;
  } catch {
    return undefined;
  }
})();
// 手元に束がある時の照合の待ち (header が来るまで — 超えたら手元の束で動く・起動を遅らせない) と、束の本体を取る待ち
const CHECK_TIMEOUT_MS = 1500;
const FETCH_TIMEOUT_MS = 60_000;
const KEEP = 2; // 残す束の数 (新しい順。各接続先の今の束は残す)
const EXIT = { USAGE: 2, NETWORK: 4 }; // 束の CLI の EXIT と同じ値

const log = (...args) => console.error(...args);

class BootstrapError extends Error {
  constructor(message, exit) {
    super(message);
    this.exit = exit;
  }
}

// 接続先 (束を取る先)。束の CLI の pickApi と同じ順・URL だけ
function apiOf(argv) {
  const i = argv.findIndex((arg) => arg === "--api" || arg.startsWith("--api="));
  const flag = i < 0 ? undefined : argv[i].includes("=") ? argv[i].slice("--api=".length) : argv[i + 1];
  const raw = flag || process.env.NOLANG_API_URL || PACKAGED_API || PROD_API;
  if (!/^https?:\/\/[^/\s]+/.test(raw)) throw new BootstrapError(`接続先は http(s):// の URL: ${raw}`, EXIT.USAGE);
  return raw.replace(/\/+$/, "");
}

// 束の署名 (base64) を公開鍵のどれかで検証する
function signedByNoLang(bytes, signature) {
  const sig = Buffer.from(signature, "base64");
  return BUNDLE_PUBLIC_KEYS.some((hex) => {
    const key = createPublicKey({ key: Buffer.concat([ED25519_SPKI_PREFIX, Buffer.from(hex, "hex")]), format: "der", type: "spki" });
    return verify(null, bytes, key, sig);
  });
}

// tar (ustar / pax) の file だけを [path, bytes] で返す。束は server の tarfile が書く素直な物 (dir の entry 無し・file だけ)
function untar(buffer) {
  const out = [];
  let paxPath = null;
  for (let offset = 0; offset + 512 <= buffer.length; ) {
    const header = buffer.subarray(offset, offset + 512);
    if (header.every((b) => b === 0)) break;
    const field = (start, len) => header.subarray(start, start + len).toString("utf8").replace(/\0.*$/s, "");
    const size = parseInt(field(124, 12).trim() || "0", 8);
    const type = field(156, 1) || "0";
    const prefix = field(345, 155);
    const body = buffer.subarray(offset + 512, offset + 512 + size);
    offset += 512 + Math.ceil(size / 512) * 512;
    if (type === "x") {
      paxPath = body.toString("utf8").match(/^\d+ path=(.*)$/m)?.[1] ?? null;
      continue;
    }
    if (type === "g") continue;
    const path = paxPath ?? (prefix ? `${prefix}/${field(0, 100)}` : field(0, 100));
    paxPath = null;
    if (type !== "0") throw new Error(`束に受けない entry: ${path} (type ${type})`);
    out.push([path, Buffer.from(body)]);
  }
  return out;
}

async function currentMap() {
  try {
    return JSON.parse(await readFile(CURRENT_FILE, "utf8"));
  } catch {
    return {};
  }
}

const installed = (hash) => existsSync(join(CLIENT_DIR, hash, "cli", "nolang.mjs"));

// 束を取る (`If-None-Match` 付き): 304 → null・200 → { hash, bytes }。届かない・断られた・署名が合わないは例外
async function fetchBundle(api, known, timeoutMs) {
  const controller = new AbortController();
  let timer = setTimeout(() => controller.abort(), timeoutMs);
  let res;
  try {
    res = await fetch(`${api}/agent/client/`, {
      headers: { accept: "application/gzip", ...(known ? { "if-none-match": `"${known}"` } : {}) },
      redirect: "error", // 束は接続先そのものから取る (他所へ飛ばされた物は受けない)
      signal: controller.signal,
    });
  } finally {
    clearTimeout(timer);
  }
  if (res.status === 304) return null;
  if (!res.ok) throw new Error(`GET ${api}/agent/client/ → ${res.status}`);
  timer = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS); // header は来た — 本体の取り寄せは長めに
  let bytes;
  try {
    bytes = Buffer.from(await res.arrayBuffer());
  } finally {
    clearTimeout(timer);
  }
  const hash = createHash("sha256").update(bytes).digest("hex");
  const etag = (res.headers.get("etag") || "").replace(/"/g, "");
  if (etag && etag !== hash) throw new Error(`束の指紋が ETag と違う (${hash.slice(0, 12)} ≠ ${etag.slice(0, 12)}) — 途中で中身が変わった`);
  const signature = res.headers.get("x-nolang-bundle-signature");
  if (signature) {
    if (!signedByNoLang(bytes, signature)) throw new BootstrapError(`${api} の client の束の署名が NoLang の鍵と合わない (${hash.slice(0, 12)}) — この束は動かさない`, EXIT.NETWORK);
  } else if (!isLocalhost(api)) {
    throw new BootstrapError(`${api} の client の束に署名が無い (${hash.slice(0, 12)}) — server の image が束に署名していない。署名の無い束を動かすのは localhost だけ`, EXIT.NETWORK);
  }
  return { hash, bytes };
}

// 束を NOLANG_CONFIG_DIR/client/<指紋>/ に置く。tmp に展開してから rename するので、並行する nolang・途中の失敗で半端な dir は残らない
async function install(hash, bytes) {
  const dest = join(CLIENT_DIR, hash);
  if (installed(hash)) return dest;
  const tmp = join(CLIENT_DIR, `.${hash}.${process.pid}.tmp`);
  await rm(tmp, { recursive: true, force: true });
  try {
    for (const [path, data] of untar(gunzipSync(bytes))) {
      if (isAbsolute(path) || normalize(path).split("/").includes("..")) throw new Error(`束に受けない path: ${path}`);
      await mkdir(dirname(join(tmp, path)), { recursive: true });
      await writeFile(join(tmp, path), data);
    }
    if (!existsSync(join(tmp, "cli", "nolang.mjs"))) throw new Error("束に cli/nolang.mjs が無い");
    try {
      await rename(tmp, dest);
    } catch (error) {
      if (!installed(hash)) throw error; // 並行する nolang が先に置いた (同じ指紋 = 同じ中身) のでなければ失敗
    }
  } finally {
    await rm(tmp, { recursive: true, force: true });
  }
  return dest;
}

// 古い束を消す (新しい KEEP 個と、各接続先の今の束は残す)
async function prune(current) {
  const keep = new Set(Object.values(current));
  const dirs = [];
  for (const entry of await readdir(CLIENT_DIR, { withFileTypes: true })) {
    if (entry.isDirectory() && !entry.name.startsWith(".")) dirs.push([entry.name, (await stat(join(CLIENT_DIR, entry.name))).mtimeMs]);
  }
  dirs.sort((a, b) => b[1] - a[1]);
  for (const [name] of dirs.slice(KEEP)) if (!keep.has(name)) await rm(join(CLIENT_DIR, name), { recursive: true, force: true });
}

// 今回動かす束 → { dir, hash }。手元に束があれば照合は CHECK_TIMEOUT_MS まで (届かなければ手元の束で動く)。無ければ取れるまで待つ
async function ensureBundle(api) {
  if (process.env.NOLANG_CLIENT_DIR) return { dir: process.env.NOLANG_CLIENT_DIR, hash: "dev" };
  if (!BUNDLE_ORIGINS.has(api) && !isLocalhost(api)) {
    throw new BootstrapError(
      `${api} からは NoLang の client を取らない (取るのは ${[...BUNDLE_ORIGINS].join(" / ")} と localhost だけ)。他の server で動かすなら NOLANG_CLIENT_DIR=<nolang-backend の agent_client>`,
      EXIT.USAGE,
    );
  }
  const current = await currentMap();
  const cached = current[api] && installed(current[api]) ? current[api] : null;
  let got;
  try {
    got = await fetchBundle(api, cached, cached ? CHECK_TIMEOUT_MS : FETCH_TIMEOUT_MS);
  } catch (error) {
    const why = error.cause?.code || error.cause?.message || error.message;
    if (cached) {
      log(`注意: ${api} から client を取れない (${why}) — 手元の client で動く`);
      return { dir: join(CLIENT_DIR, cached), hash: cached };
    }
    if (error instanceof BootstrapError) throw error;
    throw new BootstrapError(`NoLang の client を ${api} から取れない (${why}) — 接続先 (NOLANG_API_URL) と網を確かめる`, EXIT.NETWORK);
  }
  if (!got) return { dir: join(CLIENT_DIR, cached), hash: cached };
  const dir = await install(got.hash, got.bytes);
  current[api] = got.hash;
  await writeFile(CURRENT_FILE, JSON.stringify(current, null, 2) + "\n");
  await prune(current);
  return { dir, hash: got.hash };
}

const argv = process.argv.slice(2);
let api;
let bundle;
try {
  api = apiOf(argv);
  bundle = await ensureBundle(api);
} catch (error) {
  log(`error: ${error.message}`);
  process.stdout.write(JSON.stringify({ ok: false, error: error.message }, null, 2) + "\n");
  process.exit(error.exit ?? EXIT.NETWORK);
}
process.env.NOLANG_CLIENT_BUNDLE = bundle.hash; // 束の CLI と studio の script が X-NoLang-Client に載せる
const { run } = await import(pathToFileURL(join(bundle.dir, "cli", "nolang.mjs")).href);
await run(argv, { packagedApi: PACKAGED_API, bootstrap: BOOTSTRAP });
// 失敗した時だけ: この間に server が更新されていれば、やり直しで直る事を 1 行で知らせる (束の照合は起動時の 1 回だけ)
if (process.exitCode && bundle.hash !== "dev") {
  try {
    if (await fetchBundle(api, bundle.hash, CHECK_TIMEOUT_MS)) log("注意: NoLang の server がこの間に更新された — 同じコマンドをもう一度実行すると新しい client で動く");
  } catch {
    // 知らせは最善努力
  }
}

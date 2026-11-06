#!/usr/bin/env node
// nolang — 起動係 (bootstrap)。CLI の本体は NoLang の server が配る束 (`GET <api>/agent/client/` の tar.gz: cli/ = CLI 本体・
// scripts/ = studio・reference/ = 文書一式) で、server と一緒に変わる。ここは起動のたびに束を ETag で照合し (304 なら手元の束・
// 変わっていれば取り直して展開)、束の cli/nolang.mjs を同じ process で動かす。版番号は無い: 束の指紋 = tar.gz の sha256 = ETag。
// 束の置き場は NOLANG_CONFIG_DIR/client/<指紋>/ (既定 ~/.config/nolang)。依存なし (Node 20+)。
// 接続先の決め方は束の CLI と同じ順 (--api → NOLANG_API_URL → `nolang use` の接続先 → プラグインの defaults.json → 本番)。
// 開発: NOLANG_CLIENT_DIR=<nolang-backend の agent_client> で、server から取らずにその checkout の CLI を動かす。
import { createHash } from "node:crypto";
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
// 接続先の名前 (束の lib/config.mjs と同じ表 — 束を取る前に接続先が要るのでここにも持つ)
const TARGETS = {
  local: "http://localhost:18000",
  dev: "https://api-dev.no-lang.com",
  stg: "https://api-stg.no-lang.com",
  prod: "https://api.no-lang.com",
};
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

const log = (...args) => console.error(...args);

// 接続先 (束を取る先)。束の CLI の chooseApi と同じ順
function apiOf(argv) {
  const i = argv.findIndex((arg) => arg === "--api" || arg.startsWith("--api="));
  const flag = i < 0 ? undefined : argv[i].includes("=") ? argv[i].slice("--api=".length) : argv[i + 1];
  let selected;
  try {
    selected = JSON.parse(readFileSync(join(CONFIG_DIR, "credentials.json"), "utf8")).selected_api;
  } catch {
    selected = undefined;
  }
  const raw = flag || process.env.NOLANG_API_URL || selected || PACKAGED_API || TARGETS.prod;
  return (TARGETS[raw] || raw).replace(/\/+$/, "");
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

// 束を取る (`If-None-Match` 付き): 304 → null・200 → { hash, bytes }。届かない・断られたは例外
async function fetchBundle(api, known, timeoutMs) {
  const controller = new AbortController();
  let timer = setTimeout(() => controller.abort(), timeoutMs);
  let res;
  try {
    res = await fetch(`${api}/agent/client/`, {
      headers: { accept: "application/gzip", ...(known ? { "if-none-match": `"${known}"` } : {}) },
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
  const current = await currentMap();
  const cached = current[api] && installed(current[api]) ? current[api] : null;
  let got;
  try {
    got = await fetchBundle(api, cached, cached ? CHECK_TIMEOUT_MS : FETCH_TIMEOUT_MS);
  } catch (error) {
    const why = error.cause?.code || error.cause?.message || error.message;
    if (!cached) throw new Error(`NoLang の client を ${api} から取れない (${why}) — 接続先 (nolang use) と網を確かめる`);
    log(`注意: ${api} に届かない (${why}) — 手元の client で動く`);
    return { dir: join(CLIENT_DIR, cached), hash: cached };
  }
  if (!got) return { dir: join(CLIENT_DIR, cached), hash: cached };
  const dir = await install(got.hash, got.bytes);
  current[api] = got.hash;
  await writeFile(CURRENT_FILE, JSON.stringify(current, null, 2) + "\n");
  await prune(current);
  return { dir, hash: got.hash };
}

const argv = process.argv.slice(2);
const api = apiOf(argv);
let bundle;
try {
  bundle = await ensureBundle(api);
} catch (error) {
  log(`error: ${error.message}`);
  process.stdout.write(JSON.stringify({ ok: false, error: error.message }, null, 2) + "\n");
  process.exit(4); // 接続 (束の CLI の EXIT.NETWORK と同じ)
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

// 文書一式 (studio/reference/ — 正本は backend の libs/ai/llm_prompts/draft_author/reference/) の版: 内容の指紋・文書ごとの指紋・
// server の束 (`GET drafts/reference/` の tar.gz) の取り直し。sync (scripts/sync-reference.mjs) と `nolang reference` が使う。
// 算法は backend の author_core.reference_hash_of / doc_hashes_of と同じ (server の `drafts/rules/` の sync 欄と比べる値):
//   全体 = sha256( Σ_{path の昇順} "{path}\0{sha256(内容)}\n" ) の hex
//   文書ごと = manifest の行ごとの hex 先頭 12 文字 (file の行は内容の sha256・dir の行は中の file で全体と同じ算法)
// 範囲は contract.json の `reference` の列 (`/` で終わる行は dir の中の全 file・`.` で始まる物と `__pycache__` は除く)。
// path は ASCII だけ (並びが言語の文字列比較で揺れない)。算法を変える時は backend の test vector
// (libs/tests/ai/llm_core/test_draft_reference_bundle.py) と test/reference.test.mjs を揃える。
import { createHash } from "node:crypto";
import { mkdir, readdir, readFile, rename, rm, stat, writeFile } from "node:fs/promises";
import { dirname, isAbsolute, join, normalize } from "node:path";
import { gunzipSync } from "node:zlib";

async function walk(root, rel) {
  const out = [];
  for (const entry of await readdir(join(root, rel), { withFileTypes: true })) {
    if (entry.name.startsWith(".") || entry.name === "__pycache__") continue;
    const child = `${rel}/${entry.name}`;
    if (entry.isDirectory()) out.push(...(await walk(root, child)));
    else if (entry.isFile()) out.push(child);
  }
  return out;
}

export async function readContract(dir) {
  return JSON.parse(await readFile(join(dir, "contract.json"), "utf8"));
}

async function manifest(dir) {
  const { reference } = await readContract(dir);
  if (!Array.isArray(reference)) throw new Error("contract.json: reference が列でない");
  return reference;
}

export async function referenceFiles(dir) {
  const paths = new Set();
  for (const row of await manifest(dir)) {
    const target = row.replace(/\/$/, "");
    if (row.endsWith("/")) {
      if (!(await stat(join(dir, target)).catch(() => null))?.isDirectory()) throw new Error(`contract.json の reference の dir が無い: ${row}`);
      for (const path of await walk(dir, target)) paths.add(path);
    } else {
      if (!(await stat(join(dir, target)).catch(() => null))?.isFile()) throw new Error(`contract.json の reference の file が無い: ${row}`);
      paths.add(target);
    }
  }
  const sorted = [...paths].sort();
  const nonAscii = sorted.filter((p) => !/^[\x00-\x7f]*$/.test(p));
  if (nonAscii.length) throw new Error(`reference の path は ASCII だけ: ${nonAscii.join(", ")}`);
  return sorted;
}

const sha256 = (data) => createHash("sha256").update(data).digest("hex");

async function digestOf(dir, paths) {
  const digest = createHash("sha256");
  for (const rel of paths) digest.update(`${rel}\0${sha256(await readFile(join(dir, rel)))}\n`);
  return digest.digest("hex");
}

export async function referenceHash(dir) {
  return digestOf(dir, await referenceFiles(dir));
}

export async function docHashes(dir) {
  const files = await referenceFiles(dir);
  const out = {};
  for (const row of await manifest(dir)) {
    out[row] = row.endsWith("/")
      ? (await digestOf(dir, files.filter((rel) => rel.startsWith(row)))).slice(0, 12)
      : sha256(await readFile(join(dir, row))).slice(0, 12);
  }
  return out;
}

// 文書ごとの指紋の差 (server にあって値が違う / 手元に無い行)
export function changedDocs(local, server) {
  return Object.keys(server || {}).filter((row) => local[row] !== server[row]);
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

// 束 (tar.gz の bytes) を dest (指紋の名の dir) に置く。tmp に展開して指紋を確かめてから rename するので、並行する run・途中の失敗で
// 半端な dir は残らない。path は束の範囲の相対 path だけを受ける (絶対 path・`..` は弾く)。新しい物から keep 版だけ残す
// (backend の agent_client/scripts/stream_run.py の fetch_reference_bundle と同じ置き場・同じ手順 — cache を共有する)
export async function installBundle(tgz, expectedHash, dest, { keep = 2 } = {}) {
  const tmp = join(dirname(dest), `.${dest.split("/").pop()}.${process.pid}.tmp`);
  await rm(tmp, { recursive: true, force: true });
  try {
    for (const [path, data] of untar(gunzipSync(tgz))) {
      if (isAbsolute(path) || normalize(path).split("/").includes("..")) throw new Error(`束に受けない path: ${path}`);
      await mkdir(dirname(join(tmp, path)), { recursive: true });
      await writeFile(join(tmp, path), data);
    }
    const got = await referenceHash(tmp);
    if (got !== expectedHash) throw new Error(`束の指紋が違う: ${got.slice(0, 16)} ≠ ${expectedHash.slice(0, 16)}`);
    try {
      await rename(tmp, dest);
    } catch (error) {
      // 並行する run が先に置いた (同じ指紋 = 同じ中身) のでなければ失敗
      if (!(await stat(join(dest, "contract.json")).catch(() => null))) throw error;
    }
  } finally {
    await rm(tmp, { recursive: true, force: true });
  }
  const dirs = [];
  for (const entry of await readdir(dirname(dest), { withFileTypes: true })) {
    if (entry.isDirectory() && !entry.name.startsWith(".")) dirs.push([entry.name, (await stat(join(dirname(dest), entry.name))).mtimeMs]);
  }
  dirs.sort((a, b) => a[1] - b[1]);
  for (const [name] of dirs.slice(0, -keep)) if (join(dirname(dest), name) !== dest) await rm(join(dirname(dest), name), { recursive: true, force: true });
}

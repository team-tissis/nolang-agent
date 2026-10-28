// 文書一式 (studio/reference/ — 正本は backend の libs/ai/llm_prompts/draft_author/reference/) の内容の指紋。
// 算法は backend の author_core.reference_hash_of と同じ (server の `drafts/rules/` の sync.reference_hash と比べる値):
//   sha256( Σ_{path の昇順} "{path}\0{sha256(内容)}\n" ) の hex
// 範囲は contract.json の `reference` の列 (`/` で終わる行は dir の中の全 file・`.` で始まる物と `__pycache__` は除く)。
// path は ASCII だけ (並びが言語の文字列比較で揺れない)。算法を変える時は backend の test vector
// (libs/tests/ai/llm_core/test_draft_reference_bundle.py) と reference-hash.test.mjs を揃える。
import { createHash } from "node:crypto";
import { readdir, readFile, stat } from "node:fs/promises";
import { join } from "node:path";

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

export async function referenceFiles(dir) {
  const { reference } = await readContract(dir);
  if (!Array.isArray(reference)) throw new Error("contract.json: reference が列でない");
  const paths = new Set();
  for (const row of reference) {
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

export async function referenceHash(dir) {
  const digest = createHash("sha256");
  for (const rel of await referenceFiles(dir)) {
    const content = createHash("sha256").update(await readFile(join(dir, rel))).digest("hex");
    digest.update(`${rel}\0${content}\n`);
  }
  return digest.digest("hex");
}

#!/usr/bin/env node
// 見本 2 本を選ぶ — nolang-backend の studio (`.agents/skills/nolang-draft-studio/scripts/stream_author.py` の pick_samples) と同じ規則:
// NoLang の src (`<型>_NN.md`) 1 本 + hf の写し (`hf_<型>_*.md`) 1 本。両側とも、70 KB 以下の自分の型の見本から (後ろに近い型の見本を足す)・
// 依頼と同じ題材の物を外し・依頼と同じ向きの物を先に・その中は file 名順。片側に 1 本も無ければもう片側の 2 本目を取る。
//
//   node scripts/pick_samples.mjs --type concept --aspect 16:9 --request "<依頼文>"
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

const SAMPLES_DIR = fileURLToPath(new URL("../reference/samples/", import.meta.url));
const NEAR_TYPE = { cinematic: "story", compare: "concept", data: "compare", story: "cinematic", concept: "compare" };
const SAMPLE_MAX_BYTES = 70_000;
// 題の語: 漢字・片仮名の続き 2 字以上・英字で始まる英数 3 字以上 (平仮名だけの語・1 字の漢字は数えない)
const TOPIC_WORD = /[一-鿿々゠-ヿー]{2,}|[A-Za-z][A-Za-z0-9]{2,}/g;

const head = (name) => readFileSync(join(SAMPLES_DIR, name), "utf8").split("\n", 1)[0];

function portrait(name) {
  const m = head(name).match(/— canvas (\d+)x(\d+)/);
  return Boolean(m) && Number(m[1]) < Number(m[2]);
}

// 1 行目 `# type · 題 (注記) — canvas …` の題の語 (英字の slug を除き、注記の `— ` の後の和文の題を足す)
function topicWords(name) {
  const text = head(name).split(" · ").slice(1).join(" · ").split(" — canvas")[0];
  const m = text.match(/^(.*?)\s*\((.*)\)\s*$/s);
  const [title, note] = m ? [m[1], m[2]] : [text, ""];
  const parts = [...title.split(" — "), ...note.split(" — ").slice(1)]
    .filter((p) => !/^[a-z0-9-]+$/.test(p))
    .map((p) => p.split("・")[0]);
  return [...new Set(parts.flatMap((p) => p.normalize("NFKC").match(TOPIC_WORD) ?? []))].sort();
}

// 依頼と同じ題材か: 題の語の半分以上が依頼にあり、それが 2 語以上か 3 字以上の語を含む
function sameTopic(name, request) {
  const words = topicWords(name);
  const req = request.normalize("NFKC").toLowerCase();
  const hit = words.filter((w) => req.includes(w.toLowerCase()));
  return words.length > 0 && 2 * hit.length >= words.length && (hit.length >= 2 || hit.some((w) => w.length >= 3));
}

// 子を持つ `.sticky` (cut を跨ぐ群) — 外部の著者の経路では cut ごとに置き直す (write-yourself.md §1 の 4)
function stickyParents(name) {
  const text = readFileSync(join(SAMPLES_DIR, name), "utf8");
  const design = text.match(/^```design\.txt\n([\s\S]*?)^```/m)?.[1] ?? "";
  const lines = design.split("\n");
  const indent = (s) => s.length - s.trimStart().length;
  return lines
    .filter((line, i) => /^[^(]*\.sticky\b/.test(line) && !line.startsWith("section#") && (lines[i + 1] ?? "").trim() && indent(lines[i + 1]) > indent(line))
    .map((line) => line.trim().split("(")[0]);
}

export function pickSamples(type, aspect, request) {
  if (!NEAR_TYPE[type]) throw new Error(`型は ${Object.keys(NEAR_TYPE).join(" / ")} のどれか: ${type}`);
  const wantPortrait = aspect === "9:16";
  const skipped = [];
  const ranked = (pattern) =>
    [type, NEAR_TYPE[type]].flatMap((t) => {
      const names = readdirSync(SAMPLES_DIR)
        .filter((n) => pattern(t).test(n) && statSync(join(SAMPLES_DIR, n)).size <= SAMPLE_MAX_BYTES)
        .sort();
      const same = names.filter((n) => sameTopic(n, request));
      skipped.push(...same);
      return names.filter((n) => !same.includes(n)).sort((a, b) => Number(portrait(a) !== wantPortrait) - Number(portrait(b) !== wantPortrait));
    });
  const nolang = ranked((t) => new RegExp(`^${t}_\\d+\\.md$`));
  const hf = ranked((t) => new RegExp(`^hf_${t}_.+\\.md$`));
  const picked = [...nolang.slice(0, 1), ...hf.slice(0, 1)];
  picked.push(...[...nolang.slice(1), ...hf.slice(1)].slice(0, 2 - picked.length));
  if (picked.length < 2) throw new Error(`${type} (${NEAR_TYPE[type]}) の見本が 2 本無い: ${picked.join(", ")}`);
  return { samples: picked, skipped };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const { values } = parseArgs({ options: { type: { type: "string" }, aspect: { type: "string" }, request: { type: "string" } } });
  if (!values.type) {
    console.error('使い方: node scripts/pick_samples.mjs --type <concept|data|compare|story|cinematic> --aspect <16:9|9:16> --request "<依頼文>"');
    process.exit(2);
  }
  const { samples, skipped } = pickSamples(values.type, values.aspect || "16:9", values.request || "");
  const rows = samples.map((name) => ({ path: `reference/samples/${name}`, sticky_parents: stickyParents(name) }));
  for (const row of rows) {
    console.error(`見本: ${row.path}${row.sticky_parents.length ? ` (子を持つ .sticky: ${row.sticky_parents.join(" ")} — 写す時に cut ごとに置き直す)` : ""}`);
  }
  console.log(JSON.stringify({ samples: rows, skipped }, null, 2));
}

#!/usr/bin/env node
// nolang-backend から、このスキルの辞書 (skills/make-video/reference/) と、studio の一式 (studio/ —
// `nolang make` が --remote で動かす著者・担当・投入の段取り) を写す。
// 正本は backend (文法とサーバーは一緒に変わる)。ここには写しと、写した元の commit (reference/SOURCE.json) だけを置く。
// backend 31e748d48f で置き場が分かれた: script は agent_client/・文書と author_core.py は libs/ai/llm_prompts/draft_author/ が正本。
//
//   node scripts/sync-reference.mjs <nolang-backend の repo root> [--commit <sha>] [--ref <branch>]
//
// backend の checkout が手元に無い時 (例: 開発機にだけある) は、commit 済みの物を git archive で取り出して渡す:
//   mkdir -p /tmp/nbe && ssh <host> 'git -C <backend> archive HEAD .agents/skills/nolang-draft-studio agent_client libs/ai/llm_prompts/draft_author' | tar x -C /tmp/nbe
//   node scripts/sync-reference.mjs /tmp/nbe --commit "$(ssh <host> git -C <backend> rev-parse HEAD)"
import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import { cp, readFile, rm, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { readContract, referenceHash } from "./reference-hash.mjs";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const DEST = join(ROOT, "skills/make-video/reference");
const DOCS = ["spec.md", "authoring.md", "capabilities.md", "looks.md", "sounds.md"];
const DIRS = ["scaffolds", "samples"];
const STUDIO_DEST = join(ROOT, "studio");
const STUDIO_SKIP = new Set(["__pycache__", ".DS_Store"]);
// backend の中の置き場 (31e748d48f 以降)
const SKILL_MD = ".agents/skills/nolang-draft-studio/SKILL.md";
const REFERENCE = "libs/ai/llm_prompts/draft_author/reference";
const AUTHOR_CORE = "libs/ai/llm_prompts/draft_author/author_core.py";
const SCRIPTS = "agent_client/scripts";
const TESTS = "agent_client/tests";
// `nolang make` (stream_make.sh --remote) が読む物だけ — 著者の文書一式 (reference/ は contract.json の manifest どおり丸ごと) と
// remote の段取りの script。check / 素材 / 描画はサーバーがするので、backend の repo の中でだけ動く script (studio.py・studio_lint.py …) は要らない。
// [studio/ の中の写し先, backend repo root からの写し元]
const STUDIO_FILES = [
  ["SKILL.md", SKILL_MD],
  ["reference", REFERENCE],
  // author_core.py の正本は libs — bundle では scripts の隣に同梱する (stream_author は repo 内なら libs を読む)
  ["scripts/author_core.py", AUTHOR_CORE],
  ["scripts/README.md", `${SCRIPTS}/README.md`],
  ["tests/__init__.py", `${TESTS}/__init__.py`],
  ["tests/test_stream_engine.py", `${TESTS}/test_stream_engine.py`],
  // studio_rules.py は backend 1874c9ecd5 で server 側 (`GET drafts/rules/`) へ移った — stream_run は台帳を API から受ける
  ...["stream_make.sh", "stream_pipeline.sh", "stream_author.py", "stream_codex.py", "stream_codex_pipeline.py", "stream_run.py", "studio_new.py"].map(
    (name) => [`scripts/${name}`, `${SCRIPTS}/${name}`],
  ),
];

const args = process.argv.slice(2);
const src = args.find((a, i) => !a.startsWith("--") && !["--commit", "--ref"].includes(args[i - 1]));
const flag = (name) => (args.indexOf(name) >= 0 ? args[args.indexOf(name) + 1] : undefined);
if (!src) {
  console.error("使い方: node scripts/sync-reference.mjs <nolang-draft-studio の directory> [--commit <sha>] [--ref <branch>]");
  process.exit(2);
}
const from = resolve(src);

function gitCommit(dir) {
  try {
    const sha = execFileSync("git", ["-C", dir, "rev-parse", "HEAD"], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
    const dirty = execFileSync("git", ["-C", dir, "status", "--porcelain", "--", "."], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim() !== "";
    return { sha, dirty };
  } catch {
    return null;
  }
}

// 規則の台帳 (SKILL.md の「Rule names and fixes」の 1 段落) を 1 規則 1 行に
// 先頭の版の行は MCP (shell の無い host) の照合に使う — skill の手順の最初に `nolang_draft_sync` を呼び、この値と比べる
function rulesMarkdown(skillMd, version) {
  const line = skillMd.split("\n").find((l) => l.startsWith("Rule names and fixes"));
  if (!line) throw new Error('SKILL.md に「Rule names and fixes」の段落が無い');
  const body = line.slice(line.indexOf("): ") + 3);
  const items = body.split("・`").map((item, i) => (i === 0 ? item : "`" + item));
  return [
    "# Rule names and fixes for check findings",
    "",
    `Version of these documents: contract: ${version.contract} · reference_hash: ${version.reference_hash} · synced_at: ${version.synced_at}`,
    "",
    "The per-rule fixes for `findings[].rule` returned by `nolang check` / `nolang_draft_check` (and the render-time lint). Silence a rule that does not fit the piece with `lint off=<rule>,…` in the root.",
    "",
    ...items.map((item) => `- ${item}`),
    "",
  ].join("\n");
}

for (const name of DOCS) await cp(join(from, REFERENCE, name), join(DEST, name));
for (const name of DIRS) {
  await rm(join(DEST, name), { recursive: true, force: true });
  await cp(join(from, REFERENCE, name), join(DEST, name), { recursive: true });
}
await rm(STUDIO_DEST, { recursive: true, force: true });
for (const [rel, srcRel] of STUDIO_FILES) {
  await cp(join(from, srcRel), join(STUDIO_DEST, rel), { recursive: true, filter: (src) => !STUDIO_SKIP.has(src.split("/").pop()) });
}
// import できない写しを出荷しない (10-23 の craft.md の欠けと同じ型の事故を塞ぐ)
const streamAuthor = await readFile(join(STUDIO_DEST, "scripts/stream_author.py"), "utf8");
if (streamAuthor.includes("author_core") && !existsSync(join(STUDIO_DEST, "scripts/author_core.py")))
  throw new Error("stream_author.py が author_core を import するのに、写した元に scripts/author_core.py が無い");

// 文書一式の版: 写した studio/reference/ の指紋 (JS) を、backend の正本の実装 (author_core.reference_hash_of — server と client が
// 使う python) の値と突き合わせる。食い違えば言語間の算法がずれている — 出荷すると全 run が「古い plugin」と判定されて毎回取り直す
const referenceDir = join(STUDIO_DEST, "reference");
const contract = (await readContract(referenceDir)).contract;
const reference_hash = await referenceHash(referenceDir);
const pyHash = execFileSync(
  process.env.PYTHON || "python3",
  [
    "-c",
    "import importlib.util, sys, pathlib; s = importlib.util.spec_from_file_location('author_core', sys.argv[1]); m = importlib.util.module_from_spec(s); sys.modules['author_core'] = m; s.loader.exec_module(m); print(m.reference_hash_of(pathlib.Path(sys.argv[2])))",
    join(from, AUTHOR_CORE),
    join(from, REFERENCE),
  ],
  { encoding: "utf8" },
).trim();
if (pyHash !== reference_hash) throw new Error(`文書一式の指紋が JS (${reference_hash.slice(0, 16)}) と python (${pyHash.slice(0, 16)}) で違う`);
const synced_at = new Date().toISOString();
await writeFile(join(DEST, "rules.md"), rulesMarkdown(await readFile(join(from, SKILL_MD), "utf8"), { contract, reference_hash, synced_at }));

const git = gitCommit(from);
const source = {
  from: "nolang-backend (agent_client/ + libs/ai/llm_prompts/draft_author/ + .agents/skills/nolang-draft-studio/SKILL.md)",
  ref: flag("--ref") || null,
  commit: flag("--commit") || git?.sha || null,
  dirty: git?.dirty ?? null,
  synced_at,
  contract,
  reference_hash,
  files: [...DOCS, ...DIRS.map((d) => d + "/"), "rules.md (SKILL.md から生成)", "../../../studio/ (skill 一式)"],
};
await writeFile(join(DEST, "SOURCE.json"), JSON.stringify(source, null, 2) + "\n");
console.error(`reference/ を写した (commit ${source.commit || "不明"})。npm run build でプラグインにも反映する`);

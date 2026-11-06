#!/usr/bin/env node
// nolang-backend から studio の一式 (packages/cli/studio/ — `nolang make` が --remote で動かす著者・担当・投入の段取りと、
// 著者の読む文書一式 reference/) を写す。
// 正本は backend (文法とサーバーは一緒に変わる)。ここには写しと、写した元の commit (studio/SOURCE.json) だけを置く。
// skill (skills/make-video/) は文書の写しを持たない — 自分で書く経路は `nolang reference` / `nolang_draft_reference` で server の現行を読む。
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
import { docHashes, readContract, referenceHash } from "../packages/cli/lib/reference.mjs";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const STUDIO_DEST = join(ROOT, "packages/cli/studio");
const STUDIO_SKIP = new Set(["__pycache__", ".DS_Store"]);
// backend の中の置き場 (31e748d48f 以降)
const SKILL_MD = ".agents/skills/nolang-draft-studio/SKILL.md";
const REFERENCE = "libs/ai/llm_prompts/draft_author/reference";
const AUTHOR_CORE = "libs/ai/llm_prompts/draft_author/author_core.py";
const CUT_STAGES = "libs/ai/llm_prompts/draft_author/cut_stages.py";
const SCRIPTS = "agent_client/scripts";
const TESTS = "agent_client/tests";
// `nolang make` (stream_make.sh --remote) が読む物だけ — 著者の文書一式 (reference/ は contract.json の manifest どおり丸ごと) と
// remote の段取りの script。check / 素材 / 描画はサーバーがするので、backend の repo の中でだけ動く script (studio.py・studio_lint.py …) は要らない。
// [studio/ の中の写し先, backend repo root からの写し元]
const STUDIO_FILES = [
  ["SKILL.md", SKILL_MD],
  ["reference", REFERENCE],
  // author_core.py・cut_stages.py の正本は libs — bundle では scripts の隣に同梱する (stream_author._shipped は repo 内なら libs を読む)
  ["scripts/author_core.py", AUTHOR_CORE],
  ["scripts/cut_stages.py", CUT_STAGES],
  ["scripts/README.md", `${SCRIPTS}/README.md`],
  ["tests/__init__.py", `${TESTS}/__init__.py`],
  ["tests/test_stream_engine.py", `${TESTS}/test_stream_engine.py`],
  // studio_rules.py は backend 1874c9ecd5 で server 側 (`GET drafts/rules/`) へ移った — stream_run は台帳を API から受ける
  ...[
    "stream_make.sh",
    "stream_api.py",
    "stream_author.py",
    "stream_codex.py",
    "stream_pipeline.py",
    "stream_run.py",
    "stream_stages.py",
    "studio_new.py",
    "upload_asset.py",
  ].map(
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

await rm(STUDIO_DEST, { recursive: true, force: true });
for (const [rel, srcRel] of STUDIO_FILES) {
  await cp(join(from, srcRel), join(STUDIO_DEST, rel), { recursive: true, filter: (src) => !STUDIO_SKIP.has(src.split("/").pop()) });
}
// import できない写しを出荷しない (10-23 の craft.md の欠けと同じ型の事故を塞ぐ)
const streamAuthor = await readFile(join(STUDIO_DEST, "scripts/stream_author.py"), "utf8");
for (const name of ["author_core", "cut_stages"])
  if (streamAuthor.includes(`_shipped("${name}")`) && !existsSync(join(STUDIO_DEST, `scripts/${name}.py`)))
    throw new Error(`stream_author.py が ${name} を import するのに、写した元に scripts/${name}.py が無い`);

// 文書一式の版: 写した studio/reference/ の指紋 (JS) を、backend の正本の実装 (author_core.reference_hash_of — server と client が
// 使う python) の値と突き合わせる。食い違えば言語間の算法がずれている — 出荷すると `nolang reference` が毎回 server から取り直す
const referenceDir = join(STUDIO_DEST, "reference");
const contract = (await readContract(referenceDir)).contract;
const reference_hash = await referenceHash(referenceDir);
const docs = await docHashes(referenceDir);
const py = JSON.parse(
  execFileSync(
    process.env.PYTHON || "python3",
    [
      "-c",
      "import importlib.util, json, sys, pathlib; s = importlib.util.spec_from_file_location('author_core', sys.argv[1]); m = importlib.util.module_from_spec(s); sys.modules['author_core'] = m; s.loader.exec_module(m); d = pathlib.Path(sys.argv[2]); print(json.dumps({'hash': m.reference_hash_of(d), 'docs': m.doc_hashes_of(d)}))",
      join(from, AUTHOR_CORE),
      join(from, REFERENCE),
    ],
    { encoding: "utf8" },
  ),
);
if (py.hash !== reference_hash) throw new Error(`文書一式の指紋が JS (${reference_hash.slice(0, 16)}) と python (${py.hash.slice(0, 16)}) で違う`);
if (JSON.stringify(py.docs) !== JSON.stringify(docs)) throw new Error(`文書ごとの指紋が JS と python で違う: ${JSON.stringify(docs)} ≠ ${JSON.stringify(py.docs)}`);
const synced_at = new Date().toISOString();

const git = gitCommit(from);
const source = {
  from: "nolang-backend (agent_client/ + libs/ai/llm_prompts/draft_author/ + .agents/skills/nolang-draft-studio/SKILL.md)",
  ref: flag("--ref") || null,
  commit: flag("--commit") || git?.sha || null,
  dirty: git?.dirty ?? null,
  synced_at,
  contract,
  reference_hash,
  docs,
  files: STUDIO_FILES.map(([rel]) => rel),
};
await writeFile(join(STUDIO_DEST, "SOURCE.json"), JSON.stringify(source, null, 2) + "\n");
console.error(`packages/cli/studio/ を写した (commit ${source.commit || "不明"})。npm run build でプラグインにも反映する`);

#!/usr/bin/env node
// nolang-backend のスキル `nolang-draft-studio` から、このスキルの辞書 (skills/make-video/reference/) と、studio の一式 (studio/ —
// `nolang make` が --remote で動かす著者・担当・投入の段取り) を写す。
// 正本は backend (文法とサーバーは一緒に変わる)。ここには写しと、写した元の commit (reference/SOURCE.json) だけを置く。
//
//   node scripts/sync-reference.mjs <nolang-draft-studio の directory> [--commit <sha>] [--ref <branch>]
//
// backend の checkout が手元に無い時 (例: 開発機にだけある) は、commit 済みの物を git archive で取り出して渡す:
//   mkdir -p /tmp/nds && ssh <host> 'git -C <backend> archive HEAD .agents/skills/nolang-draft-studio' | tar x -C /tmp/nds
//   node scripts/sync-reference.mjs /tmp/nds/.agents/skills/nolang-draft-studio --commit "$(ssh <host> git -C <backend> rev-parse HEAD)"
import { execFileSync } from "node:child_process";
import { cp, readFile, rm, writeFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const DEST = join(ROOT, "skills/make-video/reference");
const DOCS = ["authoring.md", "capabilities.md", "looks.md", "sounds.md"];
const DIRS = ["scaffolds", "samples"];
const STUDIO_DEST = join(ROOT, "studio");
const STUDIO_SKIP = new Set(["__pycache__", ".DS_Store"]);
// `nolang make` (stream_make.sh --remote) が読む物だけ — 著者の system prompt の文書 (SKILL.md と reference の 4 つ)・見本・骨組みと、
// remote の段取りの script。check / 素材 / 描画はサーバーがするので、backend の repo の中でだけ動く script (studio.py・studio_lint.py …) は要らない
const STUDIO_FILES = [
  "SKILL.md",
  "scripts/README.md",
  "tests/test_stream_engine.py",
  "tests/__init__.py",
  ...["authoring.md", "capabilities.md", "looks.md", "sounds.md", "samples", "scaffolds"].map((name) => `reference/${name}`),
  // studio_rules.py は backend 1874c9ecd5 で server 側 (`GET drafts/rules/`) へ移った — stream_run は台帳を API から受ける
  ...["stream_make.sh", "stream_pipeline.sh", "stream_author.py", "stream_codex.py", "stream_codex_pipeline.py", "stream_run.py", "studio_new.py"].map((name) => `scripts/${name}`),
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

// 規則の台帳 (SKILL.md の「規則の名と直し方」の 1 段落) を 1 規則 1 行に
function rulesMarkdown(skillMd) {
  const line = skillMd.split("\n").find((l) => l.startsWith("規則の名と直し方"));
  if (!line) throw new Error("SKILL.md に「規則の名と直し方」の段落が無い");
  const body = line.slice(line.indexOf("): ") + 3);
  const items = body.split("・`").map((item, i) => (i === 0 ? item : "`" + item));
  return [
    "# check の findings の規則名と直し方",
    "",
    "`nolang check` / `nolang_draft_check` が返す `findings[].rule` (と描画時の lint) の名前ごとの直し方。型に合わない規則は根の `lint off=規則,…` で切れる。",
    "",
    ...items.map((item) => `- ${item}`),
    "",
  ].join("\n");
}

for (const name of DOCS) await cp(join(from, "reference", name), join(DEST, name));
for (const name of DIRS) {
  await rm(join(DEST, name), { recursive: true, force: true });
  await cp(join(from, "reference", name), join(DEST, name), { recursive: true });
}
await writeFile(join(DEST, "rules.md"), rulesMarkdown(await readFile(join(from, "SKILL.md"), "utf8")));
await rm(STUDIO_DEST, { recursive: true, force: true });
for (const rel of STUDIO_FILES) {
  await cp(join(from, rel), join(STUDIO_DEST, rel), { recursive: true, filter: (src) => !STUDIO_SKIP.has(src.split("/").pop()) });
}

const git = gitCommit(from);
const source = {
  from: "nolang-backend/.agents/skills/nolang-draft-studio",
  ref: flag("--ref") || null,
  commit: flag("--commit") || git?.sha || null,
  dirty: git?.dirty ?? null,
  synced_at: new Date().toISOString(),
  files: [...DOCS, ...DIRS.map((d) => d + "/"), "rules.md (SKILL.md から生成)", "../../../studio/ (skill 一式)"],
};
await writeFile(join(DEST, "SOURCE.json"), JSON.stringify(source, null, 2) + "\n");
console.error(`reference/ を写した (commit ${source.commit || "不明"})。npm run build でプラグインにも反映する`);

#!/usr/bin/env node
// 正本 (packages/cli・skills/) からプラグインの中身 (plugins/<名>/cli・skills) を作り、manifest の version を CLI に揃える。
// プラグインごとに違うのは接続先だけ: CLI の既定の接続先 (cli/defaults.json) と、スキルの中の MCP の名前・つながらない時の手当て。
// Codex はプラグインの directory だけを cache に写すので、CLI とスキルの実体をプラグインの中に置く (symlink は使わない)。
// `--check` は書かずに、今のプラグインの中身が正本どおりかだけを見る (CI 用・ずれていれば終了コード 1)。
import { cp, mkdtemp, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const CLI_FILES = ["nolang.mjs", "lib", "package.json", "README.md"];
const LOCAL_TROUBLESHOOT =
  "- つながらない (connection refused・timeout) → `bash scripts/doctor.sh` を実行して結果をユーザーに伝える。ユーザーの `localhost:18000` (API) と `localhost:8000` (ログイン) が NoLang のスタックに届いている必要がある (SSH の LocalForward など・README.md)。";
const PLUGINS = {
  // 手元のデモスタック (開発者向け・SSH の LocalForward で localhost に届ける)
  "nolang-local": { api: "http://localhost:18000", replace: [] },
  // 社内の dev (dev.no-lang.com)
  "nolang-dev": {
    api: "https://api-dev.no-lang.com",
    replace: [
      ["デモ用の NoLang で動画を 1 本作る。", "社内 dev の NoLang (dev.no-lang.com) で動画を 1 本作る。"],
      ["MCP (nolang-local) で投入すると", "MCP (nolang-dev) で投入すると"],
      ["# NoLang の動画を作る (nolang-local)", "# NoLang の動画を作る (nolang-dev)"],
      ["`codex mcp login nolang-local`", "`codex mcp login nolang-dev`"],
      [
        LOCAL_TROUBLESHOOT,
        "- つながらない・ログインできない → (シェルがあれば `nolang doctor` の結果を添えて) ユーザーに伝える。接続先は `https://api-dev.no-lang.com` (API) と `https://dev.no-lang.com` (ログイン)。dev.no-lang.com に会社のネットワークから入れるか、dev のアカウントがあるかを確かめてもらう。",
      ],
    ],
  },
};
const MANIFESTS = [".claude-plugin/plugin.json", ".codex-plugin/plugin.json"];
const IGNORED = new Set([".DS_Store"]);
const SKILL_DOCS = ["SKILL.md", "write-yourself.md"];

async function buildInto(pluginDir, plugin) {
  const version = JSON.parse(await readFile(join(ROOT, "packages/cli/package.json"), "utf8")).version;
  await rm(join(pluginDir, "cli"), { recursive: true, force: true });
  for (const name of CLI_FILES) await cp(join(ROOT, "packages/cli", name), join(pluginDir, "cli", name), { recursive: true });
  await writeFile(join(pluginDir, "cli/defaults.json"), JSON.stringify({ api: plugin.api }, null, 2) + "\n");
  // studio の一式 (nolang make が動かす)。skills/ の外に置く — 中の SKILL.md を別の skill として拾わせない
  await rm(join(pluginDir, "studio"), { recursive: true, force: true });
  await cp(join(ROOT, "studio"), join(pluginDir, "studio"), { recursive: true, filter: (src) => !IGNORED.has(src.split("/").pop()) });
  // Claude Code の hook (tell_user を通知で出す)。plugin の hooks/hooks.json は有効にした時に読まれる
  await rm(join(pluginDir, "hooks"), { recursive: true, force: true });
  await cp(join(ROOT, "hooks"), join(pluginDir, "hooks"), { recursive: true, filter: (src) => !IGNORED.has(src.split("/").pop()) });
  await rm(join(pluginDir, "skills"), { recursive: true, force: true });
  await cp(join(ROOT, "skills"), join(pluginDir, "skills"), { recursive: true, filter: (src) => !IGNORED.has(src.split("/").pop()) });
  for (const skill of await readdir(join(pluginDir, "skills"))) {
    // 置き換えは skill の手順の文書 (SKILL.md と、自分で書く経路の write-yourself.md) に掛ける
    const paths = SKILL_DOCS.map((name) => join(pluginDir, "skills", skill, name));
    const texts = await Promise.all(paths.map((path) => readFile(path, "utf8").catch(() => null)));
    for (const [from, to] of plugin.replace) {
      // 正本の文言が変わって置き換えが空振りしたら止める (dev 用のスキルに localhost の手当てが残らないように)
      if (!texts.some((text) => text?.includes(from))) throw new Error(`skills/${skill}: 置き換える文言が見つからない: ${from.slice(0, 60)}…`);
      texts.forEach((text, i) => (texts[i] = text?.replaceAll(from, to) ?? null));
    }
    await Promise.all(paths.map((path, i) => texts[i] !== null && writeFile(path, texts[i])));
  }
  for (const manifest of MANIFESTS) {
    const path = join(pluginDir, manifest);
    const json = JSON.parse(await readFile(path, "utf8"));
    json.version = version;
    await writeFile(path, JSON.stringify(json, null, 2) + "\n");
  }
}

async function listFiles(dir, prefix = "") {
  const found = new Map();
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    if (IGNORED.has(entry.name)) continue;
    const rel = prefix + entry.name;
    if (entry.isDirectory()) for (const [k, v] of await listFiles(join(dir, entry.name), rel + "/")) found.set(k, v);
    else found.set(rel, await readFile(join(dir, entry.name)));
  }
  return found;
}

async function check(name, plugin) {
  const real = join(ROOT, "plugins", name);
  const tmp = await mkdtemp(join(tmpdir(), "nolang-build-"));
  try {
    const expected = join(tmp, name);
    await cp(real, expected, { recursive: true });
    await buildInto(expected, plugin);
    const [have, want] = await Promise.all([listFiles(real), listFiles(expected)]);
    const drift = [];
    for (const [path, body] of want) if (!have.has(path) || !have.get(path).equals(body)) drift.push(`${have.has(path) ? "changed" : "missing"} ${path}`);
    for (const path of have.keys()) if (!want.has(path)) drift.push(`extra ${path}`);
    return drift;
  } finally {
    await rm(tmp, { recursive: true, force: true });
  }
}

if (process.argv.includes("--check")) {
  let failed = false;
  for (const [name, plugin] of Object.entries(PLUGINS)) {
    const drift = await check(name, plugin);
    if (drift.length) {
      failed = true;
      console.error(`plugins/${name} が正本とずれている (npm run build で直す):\n  ${drift.slice(0, 20).join("\n  ")}${drift.length > 20 ? `\n  …ほか ${drift.length - 20} 件` : ""}`);
    } else console.error(`plugins/${name}: 正本どおり`);
  }
  process.exit(failed ? 1 : 0);
}
for (const [name, plugin] of Object.entries(PLUGINS)) {
  await buildInto(join(ROOT, "plugins", name), plugin);
  console.error(`plugins/${name} を作った`);
}

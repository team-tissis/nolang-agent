#!/usr/bin/env node
// 正本 (packages/cli・skills/・hooks/) からプラグインの箱 (plugins/nolang) の中身を作り、manifest の version を CLI (起動係) に揃える。
// CLI の本体 (studio・文書一式を含む) は箱に入れない — NoLang の server が `agent/client/` で配り、起動係が起動のたびに取る。
// 箱は 1 つ = 本番の NoLang (社内の dev / stg は shell の NOLANG_API_URL で向ける)。MCP の接続は箱に入れない (シェルの無い client が connector でつなぐ)。
// Codex はプラグインの directory だけを cache に写すので、CLI (起動係) とスキルの実体を箱の中に置く (symlink は使わない)。
// hooks/ は Claude Code だけが読む (Codex の manifest には書かない)。
// `--check` は書かずに、今の箱の中身が正本どおりかだけを見る (CI 用・ずれていれば終了コード 1)。
import { cp, mkdtemp, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const PLUGIN = { name: "nolang", api: "https://api.no-lang.com" };
const CLI_FILES = ["nolang.mjs", "package.json", "README.md"];
const MANIFESTS = [".claude-plugin/plugin.json", ".codex-plugin/plugin.json"];
// 箱に入れない物
const IGNORED = new Set([".DS_Store", "__pycache__", "test", "tests"]);
const keep = (src) => !IGNORED.has(src.split("/").pop());

async function buildInto(pluginDir) {
  const version = JSON.parse(await readFile(join(ROOT, "packages/cli/package.json"), "utf8")).version;
  await rm(join(pluginDir, "cli"), { recursive: true, force: true });
  for (const name of CLI_FILES) await cp(join(ROOT, "packages/cli", name), join(pluginDir, "cli", name), { recursive: true, filter: keep });
  await writeFile(join(pluginDir, "cli/defaults.json"), JSON.stringify({ api: PLUGIN.api }, null, 2) + "\n");
  // Claude Code の hook (tell_user を通知で出す)。plugin の hooks/hooks.json は有効にした時に読まれる
  await rm(join(pluginDir, "hooks"), { recursive: true, force: true });
  await cp(join(ROOT, "hooks"), join(pluginDir, "hooks"), { recursive: true, filter: keep });
  await rm(join(pluginDir, "skills"), { recursive: true, force: true });
  await cp(join(ROOT, "skills"), join(pluginDir, "skills"), { recursive: true, filter: keep });
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

async function check() {
  const real = join(ROOT, "plugins", PLUGIN.name);
  const tmp = await mkdtemp(join(tmpdir(), "nolang-build-"));
  try {
    const expected = join(tmp, PLUGIN.name);
    await cp(real, expected, { recursive: true });
    await buildInto(expected);
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
  const drift = await check();
  if (drift.length) {
    console.error(`plugins/${PLUGIN.name} が正本とずれている (npm run build で直す):\n  ${drift.slice(0, 20).join("\n  ")}${drift.length > 20 ? `\n  …ほか ${drift.length - 20} 件` : ""}`);
    process.exit(1);
  }
  console.error(`plugins/${PLUGIN.name}: 正本どおり`);
  process.exit(0);
}
await buildInto(join(ROOT, "plugins", PLUGIN.name));
console.error(`plugins/${PLUGIN.name} を作った`);

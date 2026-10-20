#!/usr/bin/env node
// 正本 (packages/cli・skills/) からプラグインの中身 (plugins/<名>/cli・skills) を作り、manifest の version を CLI に揃える。
// Codex はプラグインの directory だけを cache に写すので、CLI とスキルの実体をプラグインの中に置く (symlink は使わない)。
// `--check` は書かずに、今のプラグインの中身が正本どおりかだけを見る (CI 用・ずれていれば終了コード 1)。
import { cp, mkdtemp, readdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = fileURLToPath(new URL("..", import.meta.url));
const CLI_FILES = ["nolang.mjs", "lib", "package.json", "README.md"];
const PLUGINS = ["nolang-local"];
const MANIFESTS = [".claude-plugin/plugin.json", ".codex-plugin/plugin.json"];
const IGNORED = new Set([".DS_Store"]);

async function buildInto(pluginDir) {
  const version = JSON.parse(await readFile(join(ROOT, "packages/cli/package.json"), "utf8")).version;
  await rm(join(pluginDir, "cli"), { recursive: true, force: true });
  for (const name of CLI_FILES) await cp(join(ROOT, "packages/cli", name), join(pluginDir, "cli", name), { recursive: true });
  await rm(join(pluginDir, "skills"), { recursive: true, force: true });
  await cp(join(ROOT, "skills"), join(pluginDir, "skills"), { recursive: true, filter: (src) => !IGNORED.has(src.split("/").pop()) });
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

async function check(name) {
  const real = join(ROOT, "plugins", name);
  const tmp = await mkdtemp(join(tmpdir(), "nolang-build-"));
  try {
    const expected = join(tmp, name);
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
  let failed = false;
  for (const name of PLUGINS) {
    const drift = await check(name);
    if (drift.length) {
      failed = true;
      console.error(`plugins/${name} が正本とずれている (npm run build で直す):\n  ${drift.slice(0, 20).join("\n  ")}${drift.length > 20 ? `\n  …ほか ${drift.length - 20} 件` : ""}`);
    } else console.error(`plugins/${name}: 正本どおり`);
  }
  process.exit(failed ? 1 : 0);
}
for (const name of PLUGINS) {
  await buildInto(join(ROOT, "plugins", name));
  console.error(`plugins/${name} を作った`);
}

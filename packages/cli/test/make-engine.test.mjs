import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { mkdtemp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { promisify } from "node:util";
import { test } from "node:test";

const execute = promisify(execFile);
const cli = new URL("../nolang.mjs", import.meta.url).pathname;

async function fixture(t, { claude = false, codex = false, loggedIn = true, authFile = true, engineFailure = "" } = {}) {
  const root = await mkdtemp(join(tmpdir(), "nolang-engine-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  const codexHome = join(root, "codex");
  await mkdir(codexHome);
  if (authFile) await writeFile(join(codexHome, "auth.json"), "{}");
  const bin = join(root, "bin");
  const studio = join(root, "studio");
  await mkdir(bin);
  await mkdir(join(studio, "scripts"), { recursive: true });
  await writeFile(join(studio, "scripts", "stream_make.sh"), "");
  for (const name of ["python3", ...(claude ? ["claude"] : []), ...(codex ? ["codex"] : [])]) {
    await writeFile(join(bin, name), `#!${process.execPath}\nprocess.exit(${loggedIn ? 0 : 1});\n`, { mode: 0o755 });
  }
  await writeFile(join(bin, "bash"), `#!${process.execPath}
const fs = require("node:fs");
const path = require("node:path");
const root = process.argv[3];
fs.mkdirSync(path.join(root, "stream"), { recursive: true });
fs.writeFileSync(path.join(root, "args.json"), JSON.stringify(process.argv.slice(2)));
if (${JSON.stringify(engineFailure)}) fs.writeFileSync(path.join(root, "stream", "engine.failed"), ${JSON.stringify(engineFailure)});
fs.writeFileSync(path.join(root, "stream", "run.out"), "PLAYABLE http://localhost:3000/video/11111111-1111-4111-8111-111111111111\\n");
`, { mode: 0o755 });
  return {
    project: join(root, "project"),
    env: { ...process.env, PATH: bin, CODEX_HOME: codexHome, NOLANG_API_URL: "https://api-dev.no-lang.com", NOLANG_TOKEN: "test", NOLANG_CONFIG_DIR: join(root, "config"), NOLANG_STUDIO_DIR: studio },
  };
}

test("Codex は Claude なしで起動し、engine を studio に明示する", async (t) => {
  // Arrange
  const { project, env } = await fixture(t, { codex: true });
  // Act
  const { stdout } = await execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "短い説明", "--engine", "codex"], { env });
  // Assert
  assert.equal(JSON.parse(stdout).playable, true);
  const args = JSON.parse(await readFile(join(project, "args.json"), "utf8"));
  assert.equal(args[args.indexOf("--engine") + 1], "codex");
});

test("既定は担当 balanced・長さ auto で、effort の既定を維持する", async (t) => {
  const { project, env } = await fixture(t, { claude: true, codex: true });
  await execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "短い説明"], { env });
  const args = JSON.parse(await readFile(join(project, "args.json"), "utf8"));
  assert.deepEqual(args.slice(2), ["--type", "concept", "--aspect", "16:9", "--seconds", "auto", "--request-text", "短い説明", "--remote", "https://api-dev.no-lang.com", "--token", "test"]);
});

test("--staff は担当を opt-in し、--editable を studio へ渡す", async (t) => {
  const { project, env } = await fixture(t, { claude: true, codex: true });
  await execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "短い説明", "--staff", "medium", "--editable"], { env });
  const args = JSON.parse(await readFile(join(project, "args.json"), "utf8"));
  assert.deepEqual(args.slice(2), ["--type", "concept", "--aspect", "16:9", "--seconds", "auto", "--request-text", "短い説明", "--staff", "medium", "--editable", "--remote", "https://api-dev.no-lang.com", "--token", "test"]);
});

test("役割の flag (--author / --staff none / --review / --fix / --staff-assets) は同じ名で studio へ渡る", async (t) => {
  const { project, env } = await fixture(t, { claude: true, codex: true });
  await execute(
    process.execPath,
    [cli, "make", project, "--type", "concept", "--request-text", "短い説明", "--seconds", "90", "--author", "medium", "--staff", "none", "--review", "medium", "--no-stills", "--fix", "warn", "--staff-assets"],
    { env },
  );
  const args = JSON.parse(await readFile(join(project, "args.json"), "utf8"));
  assert.deepEqual(args.slice(2), ["--type", "concept", "--aspect", "16:9", "--seconds", "90", "--request-text", "短い説明", "--author", "medium", "--staff", "none", "--review", "medium", "--no-stills", "--fix", "warn", "--staff-assets", "--remote", "https://api-dev.no-lang.com", "--token", "test"]);
});

test("--mode は役の flag の組として studio へ渡り、書かない役の flag は押し付けない", async (t) => {
  const { project, env } = await fixture(t, { claude: true, codex: true });
  await execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "短い説明", "--mode", "super", "--fix", "severe"], { env });
  const args = JSON.parse(await readFile(join(project, "args.json"), "utf8"));
  assert.deepEqual(args.slice(2), ["--type", "concept", "--aspect", "16:9", "--seconds", "auto", "--request-text", "短い説明", "--mode", "super", "--fix", "severe", "--remote", "https://api-dev.no-lang.com", "--token", "test"]);
  await assert.rejects(execute(process.execPath, [cli, "make", project + "2", "--type", "concept", "--request-text", "説明", "--mode", "turbo"], { env }), (error) => {
    assert.equal(error.code, 2);
    assert.match(error.stderr, /--mode は light \/ standard \/ plus \/ super/);
    return true;
  });
});

test("--fix low は直し役の段でない (warn の直しとレビューに分かれた) — 案内して止める", async (t) => {
  const { project, env } = await fixture(t, { claude: true });
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--fix", "low"], { env }), (error) => {
    assert.equal(error.code, 2);
    assert.match(error.stderr, /--fix warn/);
    assert.match(error.stderr, /--review low/);
    return true;
  });
});

test("--seconds は秒数か auto だけを受ける", async (t) => {
  const { project, env } = await fixture(t, { claude: true });
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--seconds", "60s"], { env }), (error) => {
    assert.equal(error.code, 2);
    return true;
  });
});

test("--staff は balanced / low / medium / high / xhigh / none 以外を拒否する", async (t) => {
  const { project, env } = await fixture(t, { claude: true });
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--staff", "fast"], { env }), (error) => {
    assert.equal(error.code, 2);
    return true;
  });
  await execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--staff", "xhigh"], { env });
  const args = JSON.parse(await readFile(join(project, "args.json"), "utf8"));
  assert.equal(args[args.indexOf("--staff") + 1], "xhigh");
});

test("Codex があっても engine 未指定なら Claude の不足を報告する", async (t) => {
  const { project, env } = await fixture(t, { codex: true });
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明"], { env }), (error) => {
    assert.equal(error.code, 1);
    assert.match(error.stderr, /claude が無い/);
    return true;
  });
});

test("Codex 未認証は生成開始前に終了コード3で返す", async (t) => {
  const { project, env } = await fixture(t, { codex: true, loggedIn: false });
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--engine", "codex"], { env }), (error) => {
    assert.equal(error.code, 3);
    assert.match(error.stderr, /codex login/);
    return true;
  });
});

test("不明な engine は依存確認や生成の前に拒否する", async (t) => {
  const { project, env } = await fixture(t);
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--engine", "other"], { env }), (error) => {
    assert.equal(error.code, 2);
    return true;
  });
});


test("keyring のみの認証は生成開始前に案内する", async (t) => {
  const { project, env } = await fixture(t, { codex: true, authFile: false });
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--engine", "codex"], { env }), (error) => {
    assert.equal(error.code, 3);
    assert.match(error.stderr, /auth.json/);
    return true;
  });
});


test("再生通知があっても検知済みの Codex 失敗を返す", async (t) => {
  const { project, env } = await fixture(t, { codex: true, engineFailure: "staff_one: quota" });
  await assert.rejects(execute(process.execPath, [cli, "make", project, "--type", "concept", "--request-text", "説明", "--engine", "codex"], { env }), (error) => {
    assert.equal(error.code, 1);
    assert.equal(JSON.parse(error.stdout).ok, false);
    assert.match(JSON.parse(error.stdout).error, /staff_one: quota/);
    return true;
  });
});

// 起動係の束の取得: 手元に束が無い時 (初めての起動) は一時の失敗を取り直す・断られた時は取り直さない・手元に束があれば手元で動く
import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { createHash } from "node:crypto";
import { mkdtemp, rm } from "node:fs/promises";
import { createServer } from "node:http";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, test } from "node:test";
import { fileURLToPath } from "node:url";
import { gzipSync } from "node:zlib";

const LAUNCHER = fileURLToPath(new URL("../nolang.mjs", import.meta.url));

// file 1 つだけの tar.gz (起動係の untar が読む ustar の header・dir の entry は無し)
function bundleOf(path, text) {
  const body = Buffer.from(text);
  const header = Buffer.alloc(512);
  header.write(path, 0);
  header.write(body.length.toString(8).padStart(11, "0"), 124);
  header.write("0", 156);
  const padded = Buffer.alloc(Math.ceil(body.length / 512) * 512);
  body.copy(padded);
  return gzipSync(Buffer.concat([header, padded, Buffer.alloc(1024)]));
}

const BUNDLE = bundleOf("cli/nolang.mjs", 'export async function run(argv) { console.log("BUNDLE RAN " + argv.join(" ")); }\n');
const ETAG = `"${createHash("sha256").update(BUNDLE).digest("hex")}"`;

// statuses の順に応える server (尽きたら最後の status を繰り返す)。200 は束・304 は ETag が一致した時
async function serverOf(statuses) {
  const seen = [];
  const server = createServer((req, res) => {
    const status = statuses[Math.min(seen.length, statuses.length - 1)];
    seen.push(req.headers["if-none-match"] ?? null);
    if (status !== 200) return res.writeHead(status).end();
    res.writeHead(200, { "content-type": "application/gzip", etag: ETAG }).end(BUNDLE);
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  return { origin: `http://127.0.0.1:${server.address().port}`, seen, close: () => new Promise((resolve) => server.close(resolve)) };
}

function launch(origin, configDir) {
  const { NOLANG_API_URL, NOLANG_CLIENT_DIR, NOLANG_TOKEN, ...env } = process.env;
  return new Promise((resolve) => {
    execFile(
      process.execPath,
      [LAUNCHER, "--api", origin, "hello"],
      { env: { ...env, NOLANG_CONFIG_DIR: configDir, NOLANG_CLIENT_TRUSTED_ORIGIN: origin } },
      (error, stdout, stderr) => resolve({ code: error ? error.code : 0, stdout, stderr }),
    );
  });
}

async function withServer(statuses, body) {
  const server = await serverOf(statuses);
  const configDir = await mkdtemp(join(tmpdir(), "nolang-bootstrap-"));
  try {
    await body(server, configDir);
  } finally {
    await server.close();
    await rm(configDir, { recursive: true, force: true });
  }
}

describe("起動係の束の取得", { concurrency: true }, () => {
  test("初めての起動: 502 の後に取り直して動く", async () => {
    await withServer([502, 200], async (server, configDir) => {
      const result = await launch(server.origin, configDir);

      assert.equal(result.code, 0, result.stderr);
      assert.match(result.stdout, /BUNDLE RAN --api .* hello/);
      assert.equal(server.seen.length, 2);
      assert.match(result.stderr, /取り直す \(2\/3 回目\)/);
    });
  });

  test("初めての起動: 取り直しても届かなければ 3 回で止まる", async () => {
    await withServer([503], async (server, configDir) => {
      const result = await launch(server.origin, configDir);

      assert.equal(result.code, 4);
      assert.equal(server.seen.length, 3);
      assert.equal(JSON.parse(result.stdout).ok, false);
      assert.match(result.stderr, /取れない \(GET .* → 503\)/);
    });
  });

  test("初めての起動: 断られた (404) は取り直さない", async () => {
    await withServer([404], async (server, configDir) => {
      const result = await launch(server.origin, configDir);

      assert.equal(result.code, 4);
      assert.equal(server.seen.length, 1);
      assert.doesNotMatch(result.stderr, /取り直す/);
    });
  });

  test("手元に束があれば、届かなくても取り直さず手元で動く", async () => {
    await withServer([200, 503], async (server, configDir) => {
      const first = await launch(server.origin, configDir);
      const second = await launch(server.origin, configDir);

      assert.equal(first.code, 0, first.stderr);
      assert.equal(second.code, 0, second.stderr);
      assert.match(second.stdout, /BUNDLE RAN/);
      assert.deepEqual(server.seen, [null, ETAG]);
      assert.match(second.stderr, /手元の client で動く/);
      assert.doesNotMatch(second.stderr, /取り直す/);
    });
  });
});

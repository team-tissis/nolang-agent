// 指紋の算法の test vector — backend の libs/tests/ai/llm_core/test_draft_reference_bundle.py と同じ入力・同じ値。
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { mkdir, mkdtemp, readFile, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { changedDocs, docHashes, installBundle, referenceHash } from "../lib/reference.mjs";

const VECTOR_FILES = {
  "contract.json": '{"contract": 1, "min_supported": 1, "reference": ["contract.json", "a.md", "d/"], "compose": []}\n',
  "a.md": "alpha\n",
  "d/b.md": "beta\n",
  "d/.hidden": "not in the bundle\n",
  "stray.md": "not in the manifest\n",
};
const VECTOR_HASH = "8de50bdd95086e30596e515ea4855f878ce2f9fa2af485aac17417a3be1b9351";
const VECTOR_DOCS = { "contract.json": "21a8bafd3f14", "a.md": "b6a98d9ce9a2", "d/": "3adb453ff5ef" };

async function vectorDir() {
  const dir = await mkdtemp(join(tmpdir(), "reference-hash-"));
  for (const [rel, text] of Object.entries(VECTOR_FILES)) {
    await mkdir(dirname(join(dir, rel)), { recursive: true });
    await writeFile(join(dir, rel), text);
  }
  return dir;
}

test("the hash algorithm matches the shared vector", async () => {
  // Arrange
  const dir = await vectorDir();

  // Act
  const got = await referenceHash(dir);
  const docs = await docHashes(dir);

  // Assert
  assert.equal(got, VECTOR_HASH);
  assert.deepEqual(docs, VECTOR_DOCS);
  assert.deepEqual(changedDocs(docs, { ...VECTOR_DOCS, "a.md": "000000000000", "new.md": "111111111111" }), ["a.md", "new.md"]);
});

test("installBundle unpacks a server-shaped tar.gz, checks the hash and keeps the newest versions", async () => {
  // Arrange — server と同じ形の束 (python の tarfile・PAX・mtime 0)。python が無い環境では飛ばす
  const src = await vectorDir();
  const tgz = join(await mkdtemp(join(tmpdir(), "reference-tgz-")), "bundle.tar.gz");
  const script = [
    "import gzip, io, sys, tarfile, pathlib",
    "src = pathlib.Path(sys.argv[1]); raw = io.BytesIO()",
    "with tarfile.open(fileobj=raw, mode='w', format=tarfile.PAX_FORMAT) as tar:",
    "    for rel in ['a.md', 'contract.json', 'd/b.md']:",
    "        data = (src / rel).read_bytes(); info = tarfile.TarInfo(rel); info.size = len(data); tar.addfile(info, io.BytesIO(data))",
    "pathlib.Path(sys.argv[2]).write_bytes(gzip.compress(raw.getvalue(), mtime=0))",
  ].join("\n");
  try {
    execFileSync(process.env.PYTHON || "python3", ["-c", script, src, tgz]);
  } catch {
    return;
  }
  const cache = await mkdtemp(join(tmpdir(), "reference-cache-"));
  const dest = join(cache, VECTOR_HASH);

  // Act
  await installBundle(await readFile(tgz), VECTOR_HASH, dest);

  // Assert
  assert.equal(await referenceHash(dest), VECTOR_HASH);
  await assert.rejects(installBundle(await readFile(tgz), "0".repeat(64), join(cache, "0".repeat(64))), /指紋が違う/);
});

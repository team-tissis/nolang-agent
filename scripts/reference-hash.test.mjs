// 指紋の算法の test vector — backend の libs/tests/ai/llm_core/test_draft_reference_bundle.py と同じ入力・同じ値。
import assert from "node:assert/strict";
import { mkdir, mkdtemp, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { referenceHash } from "./reference-hash.mjs";

const VECTOR_FILES = {
  "contract.json": '{"contract": 1, "min_supported": 1, "reference": ["contract.json", "a.md", "d/"], "compose": []}\n',
  "a.md": "alpha\n",
  "d/b.md": "beta\n",
  "d/.hidden": "not in the bundle\n",
  "stray.md": "not in the manifest\n",
};
const VECTOR_HASH = "8de50bdd95086e30596e515ea4855f878ce2f9fa2af485aac17417a3be1b9351";

test("the hash algorithm matches the shared vector", async () => {
  // Arrange
  const dir = await mkdtemp(join(tmpdir(), "reference-hash-"));
  for (const [rel, text] of Object.entries(VECTOR_FILES)) {
    await mkdir(dirname(join(dir, rel)), { recursive: true });
    await writeFile(join(dir, rel), text);
  }

  // Act
  const got = await referenceHash(dir);

  // Assert
  assert.equal(got, VECTOR_HASH);
});

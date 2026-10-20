import assert from "node:assert/strict";
import { test } from "node:test";

import { FALLBACK_API, pickApi } from "../lib/config.mjs";

test("--api → NOLANG_API_URL → プラグインの既定 → 前回ログイン → localhost の順", () => {
  const all = { flag: "https://a", env: "https://b", packaged: "https://c", stored: "https://d" };
  assert.equal(pickApi(all), "https://a");
  assert.equal(pickApi({ ...all, flag: undefined }), "https://b");
  assert.equal(pickApi({ ...all, flag: undefined, env: undefined }), "https://c");
  assert.equal(pickApi({ stored: "https://d" }), "https://d");
  assert.equal(pickApi({}), FALLBACK_API);
});

test("末尾の / は落とす", () => {
  assert.equal(pickApi({ flag: "https://api-dev.no-lang.com///" }), "https://api-dev.no-lang.com");
});

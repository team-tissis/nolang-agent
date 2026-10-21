import assert from "node:assert/strict";
import { test } from "node:test";

import { FALLBACK_API, TARGETS, apiUrl, chooseApi, pickApi, targetName } from "../lib/config.mjs";

test("--api → NOLANG_API_URL → nolang use → プラグインの既定 → localhost の順", () => {
  const all = { flag: "https://a", env: "https://b", selected: "https://c", packaged: "https://d" };
  assert.equal(pickApi(all), "https://a");
  assert.equal(pickApi({ ...all, flag: undefined }), "https://b");
  assert.equal(pickApi({ ...all, flag: undefined, env: undefined }), "https://c");
  assert.equal(pickApi({ packaged: "https://d" }), "https://d");
  assert.equal(pickApi({}), FALLBACK_API);
  assert.equal(chooseApi({ selected: "stg", packaged: "https://d" }).source, "use");
});

test("名前は URL に・末尾の / は落とす・名前でも URL でもない物は使い方の誤り", () => {
  assert.equal(pickApi({ flag: "prod" }), TARGETS.prod);
  assert.equal(apiUrl("https://api-dev.no-lang.com///"), "https://api-dev.no-lang.com");
  assert.equal(targetName(TARGETS.stg), "stg");
  assert.throws(() => apiUrl("staging"), /接続先は/);
});

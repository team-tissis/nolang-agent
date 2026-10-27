import assert from "node:assert/strict";
import { test } from "node:test";

import { codeFromCallback } from "../lib/callback.mjs";
import { EXIT } from "../lib/errors.mjs";

test("state が合えば code を返す (前後の空白も許す)", () => {
  assert.equal(codeFromCallback("  http://127.0.0.1:5555/callback?code=abc&state=s1 \n", "s1"), "abc");
});

test("state が違えば未認可", () => {
  assert.throws(() => codeFromCallback("http://127.0.0.1:5555/callback?code=abc&state=other", "s1"), (e) => e.exit === EXIT.AUTH);
});

test("拒否 (error=access_denied) は未認可", () => {
  assert.throws(() => codeFromCallback("http://127.0.0.1:5555/callback?error=access_denied&state=s1", "s1"), /access_denied/);
});

test("code が無ければ未認可", () => {
  assert.throws(() => codeFromCallback("http://127.0.0.1:5555/callback?state=s1", "s1"), (e) => e.exit === EXIT.AUTH);
});

test("URL として読めなければ使い方の誤り", () => {
  assert.throws(() => codeFromCallback("not a url", "s1"), (e) => e.exit === EXIT.USAGE);
});


test("state が一致しても戻り先の host・port・path が違えば受け取らない", () => {
  const expected = "http://127.0.0.1:5555/callback";
  for (const base of ["http://evil.example/callback", "http://127.0.0.1:5556/callback", "http://127.0.0.1:5555/elsewhere"]) {
    assert.throws(() => codeFromCallback(`${base}?code=abc&state=s1`, "s1", expected), /戻り先/);
  }
});

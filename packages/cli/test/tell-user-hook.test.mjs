import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { test } from "node:test";

import { tellUserOf } from "../../../hooks/tell-user.mjs";

const HOOK = fileURLToPath(new URL("../../../hooks/tell-user.mjs", import.meta.url));
const MAKE_OUT = `studio で作り始めた
{
  "tell_user": "動画が再生できるようになりました (続きは生成しながら伸びていきます):\\nhttps://dev.no-lang.com/video/abc",
  "next": "…",
  "ok": true
}
exit 0`;

test("tell_user は出力の JSON から改行ごと取り出す・無ければ null", () => {
  assert.equal(tellUserOf(MAKE_OUT), "動画が再生できるようになりました (続きは生成しながら伸びていきます):\nhttps://dev.no-lang.com/video/abc");
  assert.equal(tellUserOf('{"tell_user": "a \\"b\\""}\n{"tell_user": "後の方"}'), "後の方");
  assert.equal(tellUserOf("check OK"), null);
  assert.equal(tellUserOf(undefined), null);
});

test("hook は tell_user がある時だけ systemMessage を出す", () => {
  const run = (stdout) => execFileSync("node", [HOOK], { input: JSON.stringify({ tool_name: "Bash", tool_response: { stdout } }), encoding: "utf8" });
  assert.deepEqual(JSON.parse(run(MAKE_OUT)), { systemMessage: "動画が再生できるようになりました (続きは生成しながら伸びていきます):\nhttps://dev.no-lang.com/video/abc" });
  assert.equal(run("ls"), "");
  assert.equal(execFileSync("node", [HOOK], { input: "壊れた入力", encoding: "utf8" }), "");
});

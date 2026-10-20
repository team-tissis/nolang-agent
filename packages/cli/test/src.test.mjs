import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";

import { EXIT } from "../lib/errors.mjs";
import { aspectOf, splitCuts } from "../lib/src.mjs";

const DESIGN = `#v2
canvas 1280x720 bg=#0B1220
# 注記は投入しない
def h1(t) = p(font-size: 72px; content: {t})

section#a
h1#a_h(left: 80px; top: 96px) 見出し A
#a_h.on(color: $a)

section#orphan
p#o(left: 0px; top: 0px) timeline に無い cut

section#b
h1#b_h(left: 80px; top: 96px) 見出し B
`;

const TIMELINE = `#v2
cast n = "落ち着いたナレーター"

*** a
[>#subtitle]
@n: [>#a_h]A の台詞。
# TODO 消し忘れの注記

*** b
@n: [>#b_h]B の台詞。
`;

test("1 つ目の cut は根の design + 根の timeline (#v2 を除く) + timeline に無い block + cut の 2 block", () => {
  const [first] = splitCuts(DESIGN, TIMELINE);
  assert.equal(first.name, "a");
  assert.equal(
    first.text,
    [
      "#v2",
      "canvas 1280x720 bg=#0B1220",
      "def h1(t) = p(font-size: 72px; content: {t})",
      'cast n = "落ち着いたナレーター"',
      "section#orphan",
      "p#o(left: 0px; top: 0px) timeline に無い cut",
      "section#a",
      "h1#a_h(left: 80px; top: 96px) 見出し A",
      "#a_h.on(color: $a)",
      "*** a",
      "[>#subtitle]",
      "@n: [>#a_h]A の台詞。",
      "",
    ].join("\n"),
  );
});

test("2 つ目以降は cut の design block + timeline block だけ", () => {
  const [, second] = splitCuts(DESIGN, TIMELINE);
  assert.equal(second.name, "b");
  assert.equal(second.text, ["section#b", "h1#b_h(left: 80px; top: 96px) 見出し B", "*** b", "@n: [>#b_h]B の台詞。", ""].join("\n"));
});

test("cut の順は design ではなく timeline の順", () => {
  const timeline = TIMELINE.replace("*** a", "*** tmp").replace("*** b", "*** a").replace("*** tmp", "*** b");
  assert.deepEqual(
    splitCuts(DESIGN, timeline).map((c) => c.name),
    ["b", "a"],
  );
});

test("CRLF の原稿も同じに分かれる", () => {
  const crlf = splitCuts(DESIGN.replace(/\n/g, "\r\n"), TIMELINE.replace(/\n/g, "\r\n"));
  assert.deepEqual(crlf, splitCuts(DESIGN, TIMELINE));
});

test("timeline に cut が無ければ使い方の誤り", () => {
  assert.throws(() => splitCuts(DESIGN, "#v2\ncast n = \"声\"\n"), (error) => error.exit === EXIT.USAGE);
});

test("作例はサーバーが受理した行数と同じに分かれる (7 cut)", () => {
  const dir = new URL("../../../skills/make-video/examples/explainer_16x9/", import.meta.url);
  const cuts = splitCuts(readFileSync(new URL("design.txt", dir), "utf8"), readFileSync(new URL("timeline.txt", dir), "utf8"));
  assert.deepEqual(
    cuts.map((c) => c.name),
    ["title", "skill", "mcp", "diff", "plugin", "market", "close"],
  );
  // 2026-10-20 に MCP で 1 つずつ投入して受理された行数 (応答の lines から確定の合図の 1 行を引いた数)
  assert.deepEqual(
    cuts.map((c) => c.text.split("\n").length - 1),
    [37, 12, 13, 10, 9, 12, 7],
  );
  assert.equal(cuts[0].text.split("\n").filter((line) => line === "#v2").length, 1);
});

test("縦横は canvas から", () => {
  assert.equal(aspectOf("#v2\ncanvas 1280x720 bg=#000\n"), "16:9");
  assert.equal(aspectOf("#v2\ncanvas 720x1280 bg=#000\n"), "9:16");
  assert.equal(aspectOf("#v2\n"), "16:9");
});

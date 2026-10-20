import assert from "node:assert/strict";
import { test } from "node:test";

import { mimeOf, uploadKind } from "../lib/assets.mjs";

test("mp4 / webm / mov は動画素材、それ以外は画像として送る (大文字の拡張子も)", () => {
  assert.equal(uploadKind("clip.mp4"), "footage");
  assert.equal(uploadKind("/tmp/a/CLIP.MOV"), "footage");
  assert.equal(uploadKind("b.webm"), "footage");
  assert.equal(uploadKind("photo.JPG"), "image");
  assert.equal(uploadKind("noext"), "image");
});

test("画像の MIME は拡張子から、知らない物は octet-stream", () => {
  assert.equal(mimeOf("a.png"), "image/png");
  assert.equal(mimeOf("a.JPEG"), "image/jpeg");
  assert.equal(mimeOf("a.bmp"), "application/octet-stream");
});

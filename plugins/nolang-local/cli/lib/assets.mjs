// 手元の file を NoLang の素材として送る時の振り分け。動画素材として送る拡張子は web の動画の upload が受ける物
// (backend の `VIDEO_ALLOWED_EXTENSIONS`)。ほかは画像として送り、形式の検査はサーバーに任せる。
import { extname } from "node:path";

const FOOTAGE_EXTENSIONS = new Set([".mp4", ".webm", ".mov"]);
const MIME = {
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".gif": "image/gif",
  ".heic": "image/heic",
  ".avif": "image/avif",
  ".svg": "image/svg+xml",
};

export const ASSET_KINDS = ["image", "footage", "bgm", "soundeffect", "speaker", "avatar", "font"];

export function uploadKind(path) {
  return FOOTAGE_EXTENSIONS.has(extname(path).toLowerCase()) ? "footage" : "image";
}

export function mimeOf(path) {
  return MIME[extname(path).toLowerCase()] || "application/octet-stream";
}

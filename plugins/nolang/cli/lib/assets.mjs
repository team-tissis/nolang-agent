// 手元の file を NoLang の素材として送る時の振り分け。動画素材 / 持ち込み音声として送る拡張子は web の upload が受ける物
// (backend の `VIDEO_ALLOWED_EXTENSIONS` / `AUDIO_ALLOWED_EXTENSIONS`)。ほかは画像として送り、形式の検査はサーバーに任せる。
import { extname } from "node:path";

const FOOTAGE_EXTENSIONS = new Set([".mp4", ".webm", ".mov"]);
const SPEECH_EXTENSIONS = new Set([".mp3", ".wav", ".m4a", ".aac", ".opus", ".flac"]);
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
  const ext = extname(path).toLowerCase();
  if (SPEECH_EXTENSIONS.has(ext)) return "speech";
  return FOOTAGE_EXTENSIONS.has(ext) ? "footage" : "image";
}

export function mimeOf(path) {
  return MIME[extname(path).toLowerCase()] || "application/octet-stream";
}

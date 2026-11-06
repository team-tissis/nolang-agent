#!/usr/bin/env node
// Claude Code の PostToolUse hook: nolang の出力に tell_user (動画・ログインの URL を含む案内) があれば、モデルを通さずに通知として
// ユーザーの画面に出す。モデルがリンクを書き忘れても、続けて長いコマンドを打っても、リンクはコマンドが返った時点で見える
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

// 出力の中の最後の `"tell_user": "…"` (JSON の文字列) の中身。無ければ null
export function tellUserOf(stdout) {
  const found = [...String(stdout ?? "").matchAll(/"tell_user":\s*("(?:[^"\\]|\\.)*")/g)];
  if (!found.length) return null;
  try {
    return JSON.parse(found.at(-1)[1]);
  } catch {
    return null;
  }
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  try {
    const text = tellUserOf(JSON.parse(readFileSync(0, "utf8")).tool_response?.stdout);
    if (text) process.stdout.write(JSON.stringify({ systemMessage: text }) + "\n");
  } catch {
    // 通知は補助 — hook の失敗で作業を止めない
  }
}

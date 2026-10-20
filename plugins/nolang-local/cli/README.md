# @no-lang/cli

NoLang の動画を AI エージェント (Claude Code / Codex など) から作る CLI です。コマンド名は `nolang`。

> 注意: npm の `nolang` (スコープ無し) は NoLang と無関係の別パッケージです。必ず `@no-lang/cli` を使ってください。

## 入れ方

```
npm install -g @no-lang/cli     # 以後 `nolang …`
npx @no-lang/cli <command>      # 入れずに使う
```

Node.js 20 以上が要ります。依存パッケージはありません。

## 使い方

```
nolang auth login                     ブラウザで NoLang にログイン (1 回だけ)
nolang doctor                         接続先とログインを確かめる
nolang check <dir>                    dir の design.txt / timeline.txt を検査
nolang create <dir> --title "…"       検査 → 生成開始 → 視聴 URL (生成中から再生できる)
nolang status <video_id> --wait       完成を待って mp4 の URL を得る
```

`nolang --help` で全部のコマンドが出ます。結果は stdout に JSON、途中経過は stderr。終了コードは 0 成功 / 1 原稿の欠陥・生成の失敗 / 2 使い方 / 3 未ログイン / 4 接続。

## 接続先

`--api` → 環境変数 `NOLANG_API_URL` → 前回ログインした接続先 → `http://localhost:18000` の順で決まります。
CI など対話できない環境では `NOLANG_TOKEN` に API key を入れます。

ログイン情報は `~/.config/nolang/credentials.json` (権限 0600) に保存され、期限が切れても自動で更新されます。
ブラウザが別の機械にある時 (リモート・コンテナ) は `nolang auth login --no-browser` → `nolang auth complete '<許可後の URL>'`。

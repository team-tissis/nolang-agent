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
nolang auth login                     NoLang にログイン (ローカルはブラウザ、リモートはコード入力)
nolang doctor                         接続先とログインを確かめる
nolang use [local|dev|stg|prod|<URL>|default]   接続先を選ぶ (引数なしは今の接続先・default でプラグインの接続先に戻す)
nolang make <dir> --type concept --request-text "…" [--engine claude|codex]   NoLang の studio と同じ段取りで作る (再生できたら視聴 URL)
nolang check <dir>                    dir の design.txt / timeline.txt を検査
nolang start <dir> --title "…"        書いた cut から流す: 開始 (dir に stream.json を作る)
nolang submit <dir> [--end]           書き足した cut を投入 (最後は --end)
nolang create <dir> --title "…"       全 cut を一度に: 検査 → 生成開始 → 再生できたら視聴 URL
nolang status <video_id> --wait       完成を待って mp4 の URL を得る
```

`nolang --help` で全部のコマンドが出ます。結果は stdout に JSON、途中経過は stderr。終了コードは 0 成功 / 1 原稿の欠陥・生成の失敗 / 2 使い方 / 3 未ログイン / 4 接続。

## 接続先

`--api` → 環境変数 `NOLANG_API_URL` → `nolang use` で選んだ接続先 → (プラグインに入った CLI なら) プラグインの接続先 → `dev` (`https://api-dev.no-lang.com`) の順で決まります。手元のスタックで試す時は `nolang use local` に切り替えます。
どれも名前か URL で書けます: `local` = `http://localhost:18000`・`dev` = `https://api-dev.no-lang.com`・`stg` = `https://api-stg.no-lang.com`・`prod` = `https://api.no-lang.com`。
`nolang use stg` で切り替え、`nolang use` で今の接続先、`nolang use default` で選びを外します。ログインは接続先ごとに保存され、切り替えても前のログインは残ります。
CI など対話できない環境では、ログイン済みの機械の `eval "$(nolang auth env)"` が出す access token を `NOLANG_TOKEN` に入れます。この token は CLI が更新しないので、期限 (1 時間) が切れたら入れ直します。API key (`nlg-c-…`) は CLI と MCP では使えません (403)。API key は NoLang API 用です。

ログイン情報は `~/.config/nolang/credentials.json` (権限 0600) に保存され、期限が切れても自動で更新されます。
手元の機械では、エージェントの `--background` や対話できない端末でもブラウザ認可を選びます。ブラウザでログイン画面が開き、「許可」を押すと端末の戻り先 (`127.0.0.1`) が受けてログインが完了します (コード入力なし)。ブラウザ認可を始められない時 (戻り先を開けない・client の登録を断られた) は、自動でデバイス認可に切り替えます。
SSH・リモートコンテナ・Codespaces・Docker・WSL・画面の無い Linux はデバイス認可を選びます。表示された URL を手元のブラウザで開き、`user_code` を入力して許可するとログインが完了します。ブラウザから端末へのポート接続は不要です。エージェントは `nolang auth login --background` の案内 (デバイス認可ならコードも) をユーザーに渡し、`nolang auth wait` で完了を確かめます。
`--device` / `--browser` で方式を指定できます。サーバーがデバイス認可に未対応なら自動選択はブラウザ認可へ戻り、明示 `--device` はエラーになります。明示 `--browser` はデバイス認可に切り替えません。

ブラウザ認可の戻り先に接続できない場合は、許可後のアドレスバーの URL を `nolang auth complete '<URL>'` に渡してください。通常の待ち受け・`--background`・`--no-browser` のどれでも同じ開始済みログインを完了できます。`--no-browser` はブラウザを開かず、URL を表示して終了する従来の手動方式です。
一度に待機できるログインは設定ディレクトリごとに 1 件です。新しいログインを始めると古い待機は終了します。

`make` の既定は Claude のままです。`--engine codex` では著者・担当・修正役をすべて Codex が自動実行します (codex-cli 0.162.0 で検証)。Codex の `auth.json` によるログインと NoLang のログインは別々に必要です。Codex のユーザー設定は読み込まず、CLI の既定モデルを使用します。MCP サーバーは利用者のローカル Codex を起動しません。

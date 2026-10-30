# nolang-agent

NoLang を AI エージェント (Claude Code / Codex など) から使うための配布物です。CLI・スキル・プラグインをまとめています (非公開)。

| プラグイン | 接続先 | 誰向け |
|---|---|---|
| **`nolang-dev`** | 社内の dev (`dev.no-lang.com`) | 社内の人 (下の「社内の人へ」) |
| `nolang-local` | 手元のデモスタック (localhost) | 開発者 (下の「開発者向け」) |

入口は 2 つで、裏は同じ NoLang API・同じアカウントです (HyperFrames / Higgsfield と同じ形)。スキルは CLI を優先し、使えない時は MCP で作ります。

| 入口 | 向いている所 |
|---|---|
| **CLI `nolang`** (推奨) | Claude Code・Codex などシェルを持つエージェント。原稿を file のまま渡し、check → 開始 → cut の分割 → 順番の投入を 1 コマンドで |
| **MCP** (`nolang-dev` / `nolang-local`) | シェルの無い client。ツールを 1 つずつ呼ぶ |

## 社内の人へ: nolang-dev で動画を作る (デモ)

Claude Code に「〇〇の動画を作って」と頼むと、NoLang が台本・画面・声・BGM まで作り、**1〜2 分で再生できるリンク**が返ります (続きは見ている間に伸びていき、数分で完成)。
社内の dev 環境 (`dev.no-lang.com`) で動くデモです。

### 前提

- `dev.no-lang.com` にログインできるアカウント。
- 会社のネットワーク。在宅などで dev のログイン画面に `ACCESS DENIED` と出る人は、同じブラウザで https://dev.no-lang.com/cdn-cgi/trace を開き、`ip=` の値を管理者に伝えて許可リストに足してもらう。
- GitHub の `team-tissis` の repo を読めること (プラグインはこの repo から入る)。
- **Claude Code** (ログイン済み)・**Node.js 20 以上**・**python3** (macOS 標準の 3.9 で動く)。
  台本は手元の Claude Code (`claude -p`・Opus) が書くので、Claude の利用量を使います (1 本で API 換算 約 1〜3 ドル)。
- Codex では `nolang make ... --engine codex` で著者・担当・修正役 を Codex が自動実行します (codex-cli 0.162.0 で検証)。Claude のインストールは不要です。Codex のローカル認証 (`auth.json`) と NoLang のログインが必要です。リンクはエージェントが返し、Claude Code の hook 通知は使いません。

### 1. 入れる (1 回だけ・端末で)

```
claude plugin marketplace add team-tissis/nolang-agent
claude plugin install nolang-dev@nolang
```

入れたら Claude Code を起動し直す (Claude Code の中なら `/plugin marketplace add …` と `/plugin install …` でも同じ)。

Codex:

```
codex plugin marketplace add team-tissis/nolang-agent
codex plugin add nolang-dev@nolang
```

### 2. ログインする (1 回だけ)

Claude Code に **「NoLang にログインして」** と頼む (頼まなくても、初めて動画を頼んだ時に聞かれます)。許可の URL が出る (同じ機械ならブラウザも開く) ので、dev にログインして「許可」を押し、「許可した」と返す。
ログインは 30 日使わなければ切れる。切れたらまた同じように頼めばよい。

### 3. 頼む

```
ハンドドリップでおいしいコーヒーを淹れるコツを 60 秒で解説する動画を作って
この写真 (~/Desktop/product.png) を背景にして、新商品の紹介動画を縦長で作って
落ち着いた女性の声とピアノの BGM で、在宅勤務のコツを解説する動画を作って
```

- 1〜2 分で視聴 URL (`https://dev.no-lang.com/video/…`) が出る。Claude Code では、エージェントの返事より先に `PostToolUse:Bash says:` で始まる通知にもリンクが出る。生成中から再生でき、続きは見ている間に伸びる。
- 縦長・長さ・型 (解説 / 数字 / 比較 / 物語 / 映像寄り) は言えばその通りに、言わなければ 16:9 で、長さは内容に合わせて決まる (auto)。
- 手元の写真・動画は自分の素材として送られて動画に入る。声・BGM・効果音・書体は説明文から選ばれる (決めたい時は「〇〇な声の候補を探して」)。
- 完成した mp4 が欲しい時は「完成したら mp4 のリンクをちょうだい」。

### デモの注意

- dev 環境なので、止まっていたり、作った動画やデータが消えたりすることがあります。
- 送った写真・動画は dev のサーバーに保存されます。社外秘・個人情報を含む素材は使わないでください。
- 同時にたくさん作ると、描画の順番待ちで遅くなります。

### 更新する

デモの間は版 (0.1.0) を上げずに中身だけを更新するので、`update` では新しくなりません。入れ直します (端末で):

```
claude plugin marketplace update nolang
claude plugin uninstall nolang-dev@nolang
rm -rf ~/.claude/plugins/cache/nolang/nolang-dev
claude plugin install nolang-dev@nolang
```

入れ直したら Claude Code を起動し直す。ログインは残ります。
Codex: `codex plugin marketplace upgrade nolang` → `codex plugin remove nolang-dev@nolang` → `codex plugin add nolang-dev@nolang` → 起動し直す。

### 困った時

| 症状 | どうする |
|---|---|
| ブラウザに `ACCESS DENIED` | 接続元の IP が許可されていない。https://dev.no-lang.com/cdn-cgi/trace の `ip=` を管理者へ |
| ログインの URL を開くのが遅れた | 待ち受けは 15 分。過ぎたらもう一度「NoLang にログインして」 |
| 「python3 / claude が無い」と言われる | 入れれば標準の作り方 (速い) になる。無いままでもエージェントが台本を書いて作る (遅い) |
| つながらない・様子がおかしい | 「nolang doctor を実行して」と頼み、結果を管理者へ |
| 生成が `failed` になる・声が出ない | 原稿ではなくサーバー側のことが多い。視聴 URL (video_id) を添えて管理者へ |

MCP だけで使う時 (シェルが無い client など): Claude Code は「nolang-dev を認証して」、Codex は `codex mcp login nolang-dev` で同じ dev にログインする (CLI のログインとは別に保存される)。

## 構成

```
nolang-agent/
  packages/cli/                        # CLI @no-lang/cli の正本 (Node 20+・依存なし・テスト付き)
  skills/make-video/                   # スキルの正本 (CLI 優先・無ければ MCP)
    reference/                         # 辞書・規則・雛形・見本 (nolang-backend からの写し・SOURCE.json に元の commit)
  studio/                              # nolang make が動かす studio (nolang-backend の nolang-draft-studio の写し・remote で使う物だけ)
  hooks/                               # Claude Code の hook: nolang の出力の tell_user (動画・ログインの URL) を通知で画面に出す
  plugins/nolang-dev/                  # 箱 (plugin)。cli/・skills/・studio/・hooks/ は npm run build が正本から作る — 直接直さない
  plugins/nolang-local/                #   同上 (接続先だけが違う)
    .claude-plugin/plugin.json         #   Claude Code 用 (MCP の接続設定も中に書く)
    .codex-plugin/plugin.json          #   Codex 用
    .codex-plugin/mcp.json             #   Codex 用の MCP の接続設定
  .claude-plugin/marketplace.json      # Claude Code 用の棚 (marketplace nolang)
  .agents/plugins/marketplace.json     # Codex 用の棚
  scripts/build-plugins.mjs            # 正本 → plugins/ (--check はずれの検査)
  scripts/sync-reference.mjs           # nolang-backend → skills/make-video/reference/ と studio/
  .github/workflows/ci.yml             # npm run check と npm pack --dry-run
```

## 開発者向け: 手元のデモスタック (nolang-local)

手元 (や ubik) で動かしている NoLang のスタックにつなぐ。

```
/plugin marketplace add <この repo のパス か team-tissis/nolang-agent>
/plugin install nolang-local@nolang
```

(Codex は `codex plugin marketplace add …` → `codex plugin add nolang-local@nolang`。プラグインを直しながら試す時は、この repo のパスで棚を登録する)

Claude Code / Codex が動いている機械の localhost で、次の 3 つが NoLang のスタックに届いている必要があります。

| port | 役割 |
|---|---|
| 18000 | API (CLI・MCP) |
| 8000 | ログイン (OAuth) |
| 3000 | 視聴ページ |

例: デモのスタックが ubik の `127.10.0.14` にあるなら、手元の `~/.ssh/config` に

```
Host ubik-nolang
    HostName <ubik のアドレス>
    User <ユーザー>
    LocalForward 18000 127.10.0.14:18000
    LocalForward 8000 127.10.0.14:8000
    LocalForward 3000 127.10.0.14:3000
```

を書いて `ssh -fN ubik-nolang` (VS Code の Remote-SSH で ubik-nolang につないでいる間も同じ転送が効きます)。

確かめ方: `nolang doctor` (node が無ければ `bash skills/make-video/scripts/doctor.sh`)。

注意:
- 転送は「Claude Code / Codex が動いている機械」に要ります。手元の PC の LocalForward は、ubik の上で動く Claude Code には効きません。
- NoLang のスタックにログインできるアカウントが要ります。
- `claude mcp add … nolang-local …` で手で登録していた人は、プラグインを入れたら `claude mcp remove nolang-local -s user` で外す (同じ接続が 2 つ並ぶ)。

## CLI

```
nolang auth login [--device | --browser] [--background] | login --no-browser | wait | complete '<URL>' | status | logout
nolang doctor                         接続先とログインを確かめる
nolang use [local|dev|stg|prod|<URL>|default]   接続先を選ぶ (引数なしは今の接続先・default でプラグインの接続先に戻す)
nolang make <dir> --type <型> --request-text "<依頼文>" [--aspect 16:9|9:16] [--seconds 秒|auto (既定 auto)] [--author low|medium|high|xhigh] [--author-brief] [--staff balanced|low|medium|high|xhigh|none (既定 balanced)] [--review low|medium|none] [--no-stills] [--fix defect|severe|warn|none] [--staff-assets] [--editable] [--engine claude|codex]
                                      NoLang の studio と同じ段取りで作る (engine 未指定は従来どおり Claude、codex は全役割を Codex)。再生できたら URL を返す (スキルの標準)
                                      --editable = 生成後に編集画面で調整しやすい文法サブセットに収める
nolang check [dir]                    dir の design.txt / timeline.txt を検査
nolang start [dir] --title "…" [--seconds 秒|auto]   cut ごとに流す: 開始だけ (dir に stream.json)
nolang submit [dir] [--end]           書き足した cut を投入 (最後は --end・投入の間は 180 秒以内)
nolang create [dir] --title "…" [--seconds 秒|auto] [--aspect 16:9|9:16] [--wait] [--dry-run]   全 cut を一度に (人が手で使う時)
nolang status <video_id> [--wait] [--until playable|completed]
nolang abort <video_id>
nolang assets search <kind> "<説明か名前>" [--mine]   NoLang の素材を探す → ref (id=<uuid> など)
nolang assets upload <file>… [--name 表示名]       手元の画像 / 動画を自分の素材に送る → ref
```

- 結果は stdout に JSON・途中経過は stderr。終了コード 0 成功 / 1 原稿の欠陥・生成の失敗 / 2 使い方 / 3 未ログイン / 4 接続。
- リンクの通知: プラグインの hook (`hooks/`) が、コマンドの出力に `tell_user` (動画・ログインの URL を含む案内) があれば、モデルを通さずに Claude Code の画面に通知として出す (モデルがリンクを書き忘れても届く)。
- 接続先: `--api` → `NOLANG_API_URL` → `nolang use` で選んだ接続先 → プラグインの接続先 (`cli/defaults.json`) → `dev` (`https://api-dev.no-lang.com`)。手元のスタックで試す時は `nolang use local`。どれも名前 (`local` = `http://localhost:18000`・`dev` = `https://api-dev.no-lang.com`・`stg` = `https://api-stg.no-lang.com`・`prod` = `https://api.no-lang.com`) か URL で書ける。ログインは接続先ごとに持ち、ログインしても接続先は変わらない。MCP の接続先はプラグインごとに固定 (切り替えられるのは CLI だけ)。
- ログイン: 手元の機械はエージェントの `--background` も含めてブラウザ認可 (ブラウザが開き、許可するだけ・コード入力なし。始められなければデバイス認可へ自動で切り替え)。SSH・リモートコンテナ・Docker・WSL・画面の無い Linux はデバイス認可を選び、URL とコードをブラウザで入力して許可する (ポート転送不要)。エージェントは `--background` で案内 (デバイス認可ならコードも) を受け取り、`nolang auth wait` で完了を確かめる。`--device` / `--browser` で明示選択できる。未対応サーバーでは自動選択はブラウザ認可へ戻る。ブラウザ認可の戻り先が接続エラーになっても、開始済みのログインに `auth complete '<許可後の URL>'` で貼り戻せる (`--background` も対応)。トークンは `~/.config/nolang/credentials.json` (0600)・期限が切れても自動で更新 (30 日使わなければ再ログイン)。
- CI など非対話: `NOLANG_TOKEN` に API key (`nlg-c-…`) か access token を入れる。
- ログインは MCP と同じ認可サーバー (OAuth 2.1・PKCE・`127.0.0.1` で受ける)。client はログインごとに自動登録 (DCR)。

### studio の実行エンジン

`nolang make ... --engine codex` は、手元の `codex app-server` を著者・担当・修正役 の各呼出しで起動し、本文を受け取ったカットから検査・投入します。既定の Claude のモデル・effort・プロンプト・キャッシュ予熱は変わりません。

Codex は元の `CODEX_HOME` (既定 `~/.codex`) の `auth.json` のみを共有し、ユーザーの設定・hook・plugin・MCP・会話履歴を読み込まない一時環境で動きます。モデルはその Codex CLI の既定を使い、使用モデルと effort を `stream/author.jsonl` に記録します。API key の環境変数だけの認証や keyring だけの認証は現在対象外です。Codex の本文・usage イベントは `stream/codex_*.jsonl`、エラーは `.err` に残ります。途中失敗は投入側へ伝えて中断し、Claude に自動で切り替えません。

CLI / MCP の原稿検査・素材・描画は共通の NoLang サーバーを使います。自動の著者・担当・修正は手元の studio の機能なので、シェルのないリモート MCP クライアントは従来の原稿投入手順を使います。

## 開発

直すのは正本 (`packages/cli/`・`skills/`) だけ。直したら:

```
npm run build       # 正本 → plugins/nolang-local/ (cli/ と skills/ を作り直し、manifest の version を CLI に揃える)
npm run check       # plugins/ が正本どおりか + CLI の単体テスト (CI と同じ)
npm run validate    # claude plugin validate --strict (Claude Code が要る)
```

- 版番号は `packages/cli/package.json` の 1 か所。build が 2 つの `plugin.json` に写し、CLI は実行時に `package.json` から読む。
- 反映: Claude Code はこの repo を直接読むので、次のセッション開始か `/reload-plugins`。Codex は入れた時に `~/.codex/plugins/cache/` へ写すので、入れ直す (`codex plugin remove nolang-local@nolang` → `codex plugin add nolang-local@nolang`)。

置き方の決まり (Claude Code と Codex の両方で動かすため):
- 箱は棚の下の sub directory に置く。棚と同じ directory (`./`) に箱を置くと、Claude Code は読むが Codex は棚ごと無視する。
- `.mcp.json` を棚や箱の root に置かない。この repo で作業した時に Claude Code が project の MCP としても読んで二重になる。Claude Code 用は `plugin.json` の `mcpServers` に直接、Codex 用は `.codex-plugin/mcp.json` に書く。
- CLI とスキルの実体は箱の中に置く (symlink にしない)。Codex は箱ごと cache に写すので、スキルからの相対パス (`../../cli/nolang.mjs`) がどちらでも同じになる。

### 辞書の同期 (nolang-backend → reference/)

正本は nolang-backend: 文書一式 (文法・見本・骨組み・`contract.json`) と `author_core.py` は `libs/ai/llm_prompts/draft_author/`、
配布 script は `agent_client/scripts/`、studio で作る手順は `.agents/skills/nolang-draft-studio/SKILL.md`。ここには写しだけを置き、
元の commit と文書の版 (`contract`・内容の指紋 `reference_hash`・文書ごとの指紋 `docs`) を `skills/make-video/reference/SOURCE.json` に、
版の行と `Docs:` の行を `reference/rules.md` の先頭に残す (MCP の手順が `nolang_draft_sync` と比べ、ずれた文書だけを
`nolang_draft_reference` で server から読む)。シェルのある経路は `nolang reference` が同じ照合をして server の現行の文書を
cache に置く。指紋の算法は `packages/cli/lib/reference.mjs` 1 か所 (sync と CLI が共有)。sync は指紋を JS と backend の python の
両方で計算して食い違えば止まる (算法の正本と test vector は backend の `author_core.py` / `test_draft_reference_bundle.py`)。
版の整合の設計は backend の `app_main/docs/feature/video_generate/reference_sync.md`。

自動: backend の `agent-sync-dispatch` が push を知らせ、この repo の `sync-from-backend` が写して plugin の版を上げて push する
(secret: backend 側 `NOLANG_AGENT_DISPATCH_TOKEN`・この repo 側 `BACKEND_READ_TOKEN`)。`contract` が上がる sync は止まる —
server を先に deploy してから workflow_dispatch に `server_deployed=true` を付けて流す。

手で写す時は commit 済みの物だけを写す (作業中の変更を持ち込まない):

```
mkdir -p /tmp/nbe && ssh <host> 'git -C <backend> archive HEAD .agents/skills/nolang-draft-studio agent_client libs/ai/llm_prompts/draft_author' | tar x -C /tmp/nbe
npm run sync-reference -- /tmp/nbe \
  --commit "$(ssh <host> git -C <backend> rev-parse HEAD)" --ref "$(ssh <host> git -C <backend> rev-parse --abbrev-ref HEAD)"
npm run build
```

デモのスタックに合わせる時はスタックが動いている branch から、本番向けは backend の `main` から写す。
`SKILL.md` (studio で作る標準の手順・ログイン・素材) と `write-yourself.md` (自分で書く経路) はこの repo で書いた物。文法は写した
`reference/spec.md` を読ませる (手順の文書に文法の要約を手で写さない — 版の照合の外で古びる)。

## 公開 (まだしていない)

- **npm**: `@no-lang/cli` (コマンド名は `nolang`)。npm の `nolang` (スコープ無し) は NoLang と無関係の別パッケージなので使わない。公開は `cd packages/cli && npm publish`。公開したら SKILL.md の CLI の呼び方に `npx -y @no-lang/cli` を足す。
- **GitHub**: `team-tissis/nolang-agent` として作る想定 (まず非公開)。公開すれば `npx skills add <org>/nolang-agent` と `/plugin marketplace add <org>/nolang-agent` で入るようになる。
- 一般ユーザー向けには、本番の API (`api.no-lang.com`) に drafts・OAuth が出ている必要がある (今は 404)。CLI の既定の接続先もその時に本番へ変える。

## 今後

- サーバーに 1 回で作る口 (`drafts/create`) を足し、CLI と MCP の `nolang_draft_create` を同じ関数で裏打ちする (今は CLI が手元で cut に分けて順に投入している)。
- CLI 専用の固定の client ID (DCR は MCP の仕様で非推奨になった・後継は CIMD)・device flow のログイン。
- 素材の検索・upload は backend の `claude-draft-src` の API (`v1/unstable/assets/…`) に合わせて CLI に入れた (MCP は検索だけ・upload は CLI)。dev / 本番に出たら実機で確かめる。
- 辞書をサーバーから配り、写し (`reference/`) を無くす。

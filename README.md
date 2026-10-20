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

## 社内の人へ: nolang-dev で動画を作る

### 前提

- `dev.no-lang.com` にログインできるアカウント。
- 会社のネットワーク。在宅などで dev のログイン画面に `ACCESS DENIED` と出る人は、同じブラウザで https://dev.no-lang.com/cdn-cgi/trace を開き、`ip=` の値を管理者に伝えて許可リストに足してもらう。
- Node.js 20 以上 (CLI を使うため)。GitHub の `team-tissis` の repo を clone できること (プラグインはこの repo から入る)。

### 1. 入れる (1 回だけ)

Claude Code:

```
/plugin marketplace add team-tissis/nolang-agent
/plugin install nolang-dev@nolang
```

Codex:

```
codex plugin marketplace add team-tissis/nolang-agent
codex plugin add nolang-dev@nolang
```

入れたら Claude Code / Codex を起動し直す。

### 2. ログインする (1 回だけ)

Claude Code / Codex に **「NoLang にログインして」** と頼む。許可の URL が出る (同じ機械ならブラウザも開く) ので、dev にログインして「許可」を押し、「許可した」と返す。
ログインは 30 日使わなければ切れる。切れたらまた同じように頼めばよい。

### 3. 頼む

```
NoLang の使い方を 60 秒で紹介する動画を作って
この写真 (~/Desktop/product.png) を背景にして、新商品の紹介動画を縦長で作って
落ち着いた女性の声とピアノの BGM で、在宅勤務のコツを解説する動画を作って
```

視聴 URL (`https://dev.no-lang.com/video/…`) が返り、生成中から再生できる。手元の写真・動画は自分の素材として送られ、NoLang の声・BGM・効果音・書体は説明文から選ばれる (決めたい時は「〇〇な声の候補を探して」と頼めば候補が出る)。

### 更新する

- Claude Code: `/plugin marketplace update nolang` → 起動し直す。
- Codex: `codex plugin marketplace upgrade nolang` → `codex plugin remove nolang-dev@nolang` → `codex plugin add nolang-dev@nolang` → 起動し直す。

### 困った時

| 症状 | どうする |
|---|---|
| ブラウザに `ACCESS DENIED` | 接続元の IP が許可されていない。https://dev.no-lang.com/cdn-cgi/trace の `ip=` を管理者へ |
| ログインの URL を開くのが遅れた | 待ち受けは 5 分。もう一度「NoLang にログインして」 |
| つながらない・様子がおかしい | 「nolang doctor を実行して」と頼み、結果を管理者へ |
| 生成が `failed` になる | 原稿ではなくサーバー側のことが多い。視聴 URL (video_id) を添えて管理者へ |

MCP だけで使う時 (シェルが無い client など): Claude Code は「nolang-dev を認証して」、Codex は `codex mcp login nolang-dev` で同じ dev にログインする (CLI のログインとは別に保存される)。

## 構成

```
nolang-agent/
  packages/cli/                        # CLI @no-lang/cli の正本 (Node 20+・依存なし・テスト付き)
  skills/make-video/                   # スキルの正本 (CLI 優先・無ければ MCP)
    reference/                         # 辞書・規則・雛形・見本 (nolang-backend からの写し・SOURCE.json に元の commit)
  plugins/nolang-dev/                  # 箱 (plugin)。cli/ と skills/ は npm run build が正本から作る — 直接直さない
  plugins/nolang-local/                #   同上 (接続先だけが違う)
    .claude-plugin/plugin.json         #   Claude Code 用 (MCP の接続設定も中に書く)
    .codex-plugin/plugin.json          #   Codex 用
    .codex-plugin/mcp.json             #   Codex 用の MCP の接続設定
  .claude-plugin/marketplace.json      # Claude Code 用の棚 (marketplace nolang)
  .agents/plugins/marketplace.json     # Codex 用の棚
  scripts/build-plugins.mjs            # 正本 → plugins/ (--check はずれの検査)
  scripts/sync-reference.mjs           # nolang-backend → skills/make-video/reference/
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
nolang auth login [--background | --no-browser] | wait | complete '<URL>' | status | logout
nolang doctor                         接続先とログインを確かめる
nolang templates [--aspect 16:9]
nolang check [dir]                    dir の design.txt / timeline.txt を検査
nolang create [dir] --title "…" [--seconds N] [--aspect 16:9|9:16] [--wait] [--dry-run]
nolang status <video_id> [--wait] [--until playable|completed]
nolang abort <video_id>
nolang assets search <kind> "<説明か名前>" [--mine]   NoLang の素材を探す → ref (id=<uuid> など)
nolang assets upload <file>… [--name 表示名]       手元の画像 / 動画を自分の素材に送る → ref
```

- 結果は stdout に JSON・途中経過は stderr。終了コード 0 成功 / 1 原稿の欠陥・生成の失敗 / 2 使い方 / 3 未ログイン / 4 接続。
- 接続先: `--api` → `NOLANG_API_URL` → プラグインの接続先 (`cli/defaults.json`) → 前回ログインした接続先 → `http://localhost:18000`。
- ログイン: 人が打つなら `nolang auth login` (ブラウザで許可するまで待つ)。エージェントは `--background` で URL を受け取ってすぐ戻り、`nolang auth wait` で完了を確かめる。ブラウザが別の機械なら `--no-browser` → `complete`。トークンは `~/.config/nolang/credentials.json` (0600)・期限が切れても自動で更新 (30 日使わなければ再ログイン)。
- CI など非対話: `NOLANG_TOKEN` に API key (`nlg-c-…`) か access token を入れる。
- ログインは MCP と同じ認可サーバー (OAuth 2.1・PKCE・`127.0.0.1` で受ける)。client はログインごとに自動登録 (DCR)。

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

文法・規則・雛形・辞書の正本は nolang-backend の `.agents/skills/nolang-draft-studio/` (文法とサーバーは一緒に変わる)。ここには写しだけを置き、元の commit を `skills/make-video/reference/SOURCE.json` に残す。
commit 済みの物だけを写す (作業中の変更を持ち込まない):

```
mkdir -p /tmp/nds && ssh <host> 'git -C <backend> archive HEAD .agents/skills/nolang-draft-studio' | tar x -C /tmp/nds
npm run sync-reference -- /tmp/nds/.agents/skills/nolang-draft-studio \
  --commit "$(ssh <host> git -C <backend> rev-parse HEAD)" --ref "$(ssh <host> git -C <backend> rev-parse --abbrev-ref HEAD)"
npm run build
```

デモのスタックに合わせる時はスタックが動いている branch から、本番向けは backend の `main` から写す。
`SKILL.md` の「0・1・A・B」(作る手順) はこの repo で書いた物、「2」(書き方の要点) は backend の SKILL.md からの抜き出し。

## 公開 (まだしていない)

- **npm**: `@no-lang/cli` (コマンド名は `nolang`)。npm の `nolang` (スコープ無し) は NoLang と無関係の別パッケージなので使わない。公開は `cd packages/cli && npm publish`。公開したら SKILL.md の CLI の呼び方に `npx -y @no-lang/cli` を足す。
- **GitHub**: `team-tissis/nolang-agent` として作る想定 (まず非公開)。公開すれば `npx skills add <org>/nolang-agent` と `/plugin marketplace add <org>/nolang-agent` で入るようになる。
- 一般ユーザー向けには、本番の API (`api.no-lang.com`) に drafts・OAuth が出ている必要がある (今は 404)。CLI の既定の接続先もその時に本番へ変える。

## 今後

- サーバーに 1 回で作る口 (`drafts/create`) を足し、CLI と MCP の `nolang_draft_create` を同じ関数で裏打ちする (今は CLI が手元で cut に分けて順に投入している)。
- CLI 専用の固定の client ID (DCR は MCP の仕様で非推奨になった・後継は CIMD)・device flow のログイン。
- 素材の検索・upload は backend の `claude-draft-src` の API (`v1/unstable/assets/…`) に合わせて CLI に入れた (MCP は検索だけ・upload は CLI)。dev / 本番に出たら実機で確かめる。
- 辞書をサーバーから配り、写し (`reference/`) を無くす。

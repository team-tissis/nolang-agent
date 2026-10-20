# nolang-agent

NoLang を AI エージェント (Claude Code / Codex など) から使うための配布物です。CLI・スキル・プラグインをまとめています。
今は社内デモ用のプラグイン `nolang-local` だけで、公開はしていません。

入口は 2 つで、裏は同じ NoLang API・同じアカウントです (HyperFrames / Higgsfield と同じ形)。

| 入口 | 向いている所 |
|---|---|
| **CLI `nolang`** (推奨) | Claude Code・Codex などシェルを持つエージェント。原稿を file のまま渡し、check → 開始 → cut の分割 → 順番の投入を 1 コマンドで |
| **MCP `nolang-local`** | シェルの無い client。ツールを 1 つずつ呼ぶ |

## 構成

```
nolang-agent/
  packages/cli/                        # CLI @no-lang/cli の正本 (Node 20+・依存なし・テスト付き)
  skills/make-video/                   # スキルの正本 (CLI 優先・無ければ MCP)
    reference/                         # 辞書・規則・雛形・見本 (nolang-backend からの写し・SOURCE.json に元の commit)
  plugins/nolang-local/                # 箱 (plugin)。cli/ と skills/ は npm run build が正本から作る — 直接直さない
    .claude-plugin/plugin.json         #   Claude Code 用 (MCP の接続設定も中に書く)
    .codex-plugin/plugin.json          #   Codex 用
    .codex-plugin/mcp.json             #   Codex 用の MCP の接続設定
  .claude-plugin/marketplace.json      # Claude Code 用の棚 (marketplace nolang)
  .agents/plugins/marketplace.json     # Codex 用の棚
  scripts/build-plugins.mjs            # 正本 → plugins/ (--check はずれの検査)
  scripts/sync-reference.mjs           # nolang-backend → skills/make-video/reference/
  .github/workflows/ci.yml             # npm run check と npm pack --dry-run
```

## 試す人の手順

まず **つなぐ先の準備** (下) を済ませる。

### 1. プラグインを入れる

Claude Code:

```
/plugin marketplace add <この repo のパス>
/plugin install nolang-local@nolang
```

Codex:

```
codex plugin marketplace add <この repo のパス>
codex plugin add nolang-local@nolang
```

入れたら起動し直す。

### 2. CLI でログインする (1 回だけ)

```
npx <この repo のパス>/packages/cli auth login
```

ブラウザが開くので NoLang にログインして許可する。トークンは `~/.config/nolang/credentials.json` (0600) に保存され、期限が切れても自動で更新される (30 日使わなければ再ログイン)。
`nolang` を PATH に置きたければ `npm install -g <この repo のパス>/packages/cli`。

ブラウザが別の機械 (ubik の上・コンテナの中) なら:

```
nolang auth login --no-browser          # 出た authorize_url を手元のブラウザで開いて許可
nolang auth complete '<許可後のアドレスバーの URL>'   # 許可後のページは接続エラーになる。その URL を渡す
```

### 3. 頼む

Claude Code / Codex で「〇〇の動画を作って」。スキルが CLI で `check` → `create` を回し、視聴 URL (`http://localhost:3000/video/…`) が返る。生成中から再生できる。

### MCP で使う時 (シェルが無い client など)

- Claude Code: 「nolang-local を認証して」と頼み、出た URL でログインする。
- Codex: `codex mcp login nolang-local` (`codex mcp list` の Auth 欄は `Unsupported` と出るが login は通る)。

MCP の認証と CLI の認証は別々に保存される (同じアカウントでよい)。

## CLI

```
nolang auth login [--no-browser] | complete '<URL>' | status | logout
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
- 接続先: `--api` → `NOLANG_API_URL` → 前回ログインした接続先 → `http://localhost:18000`。
- CI など非対話: `NOLANG_TOKEN` に API key (`nlg-c-…`) か access token を入れる。
- ログインは MCP と同じ認可サーバー (OAuth 2.1・PKCE・`127.0.0.1` で受ける)。client はログインごとに自動登録 (DCR)。

## つなぐ先の準備

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
- NoLang のスタックにログインできるアカウントが要ります (デモの管理者に発行してもらう)。
- `claude mcp add … nolang-local …` で手で登録していた人は、プラグインを入れたら `claude mcp remove nolang-local -s user` で外す (同じ接続が 2 つ並ぶ)。

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

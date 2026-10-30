---
name: make-video
description: 社内 dev の NoLang (dev.no-lang.com) で動画を 1 本作る。「〇〇の動画を作って」「動画にして解説して」など、NoLang で動画を作る依頼の時に使う (手元の写真・動画や、決まった曲・声を使う依頼も)。「NoLang にログインして」・NoLang の素材を探す / 送る依頼にも使う。台本と画面 (draft src) を CLI (nolang) の studio が書くか、自分で書いて MCP (nolang-dev) で投入すると、NoLang のサーバーが声・素材・描画を担当する。
---

# NoLang の動画を作る (nolang-dev)

依頼を `nolang make` に渡すと、NoLang の studio と同じ段取り (著者が cut を書いた端から check と直し → 投入) で台本と画面 (draft src) が書かれ、NoLang のサーバーが声・絵・BGM・描画を担当する。手元に GPU も NoLang の repo も要らない。
この file のパスはすべてこの skill の directory からの相対。

## 最重要: 動画のリンクを、すぐ・省かずに渡す

コマンドとツールの出力はユーザーに見えない。ユーザーが動画を開けるかどうかは、あなたのメッセージに書いたリンクだけで決まる。

- 出力に `tell_user` があれば、**次のツールを呼ぶ前に**、その文 (案内の文 + URL の行) を**そのまま**ユーザーへのメッセージに書く。省かない・要約しない・秒数や状態だけを伝えて済ませない・「上のリンク」と書かない。
- 試しに作る・速さを測る・何本か続けて作る・完成まで待つ時も同じ。作業を続ける時も、先にリンクを書いてから続ける。
- 最後のメッセージ (完成・失敗の報告・まとめ) にも、その動画の URL をもう一度書く。
- **書き方**: URL (視聴 `watch_url`・ログインの `authorize_url`・mp4 の `download_url`) は前後で改行し、**1 行にその URL だけ**を書く。前後に文字・括弧・句読点・markdown の装飾 (`**` や `[]()`) を付けず、表のセルにも入れない (そのまま押して開けるように)。`tell_user` の文はこの形になっているので、改行も含めてそのまま書く。

## 0. どの作り方か

- **標準は studio** (§S): シェル・`node` (20 以上)・`python3` と実行エンジンがあれば `nolang make` を 1 回。原稿はあなたが書かない。
- **Claude Code では従来どおり**: `claude` があれば `nolang make` (engine 未指定)。著者・担当・修正役は Claude。再生開始の目安は 1 分半ほど。
- **Codex では**: `codex` があれば必ず `nolang make ... --engine codex`。著者・担当・修正役 をすべて Codex で自動実行する。`claude` が同居していても呼ばない。Codex のログインは NoLang と別で、手元の `auth.json` を使う認証が必要 (codex-cli 0.162.0 で検証)。未認証ならその旨を知らせ、Claude に切り替えない。
- `python3` か選択したエンジンが無い・`nolang make` が使えないと言う時は、`write-yourself.md` の「A」(原稿を自分で書いて CLI で流す)。
- **シェルが無い (Web 版など)・CLI が動かない時は** `write-yourself.md` の「B」(MCP で作る)。
- **ログインはこちらから頼む** (ユーザーはログインを知らなくてよい): 依頼を受けたら、作る前に 1 回 `nolang auth status` (MCP なら `nolang_draft_templates` などを 1 回呼ぶ)。未ログインなら §L (MCP は `write-yourself.md` の B) でログインを済ませてから進める。途中のどのコマンドでも終了コード 3 (未ログイン) が出たら、同じくログインしてからやり直す。
- **接続先を変える** (「stg で作って」「本番につないで」「localhost で」と頼まれた時だけ): `nolang use <local|dev|stg|prod>` (URL も可・`nolang use` で今の接続先・`default` で戻す)。ログインは接続先ごとなので、切り替えた先が未ログインなら上と同じくログインする。MCP の接続先はプラグインごとに固定で、切り替えられるのは CLI だけ。

## S. studio で作る (標準)

1. **ログイン**: §L。
2. **依頼から決める**: 型 (`concept` 解説 / `data` 数字 / `compare` 比べる / `story` 物語 / `cinematic` 映像寄り)・縦横 (`16:9` / `9:16`)・長さ (依頼に明示があればその秒数・無ければ auto = 内容に合わせる)。聞き返さず既定で進め、決めた値は最後に伝える。決まった素材 (この写真・この曲・この声) がある時だけ §M で `ref` を得る。
3. **作る**: `nolang make ./nolang-videos/<英小文字の名> --type <型> --aspect <縦横> --request-text "<依頼文>"` (長さの明示がある時だけ `--seconds <秒>` を足す・Bash の timeout は 600000)。
   - Codex ではコマンドに `--engine codex` を追加する。Claude Code では追加しない。
   - 依頼文 = ユーザーの依頼をそのまま + 決めた値 + 素材の `ref` (`id=<uuid>` と使い所) + 台本やテロップの文言があればそのまま。題材の事実が要る時は先に調べて依頼文に書く (著者は調べない)。
   - **役の組は `--mode` で選ぶ** (後ろに書いた役の flag が組の値を上書きする): `light` = 著者 low・担当なし・直し severe (最速・質は落ちる) / `standard` = 著者 low・担当 balanced・直し severe (今までの既定) / `plus` = 著者 brief (low)・担当 balanced (絵も設計)・直し warn (構図の密度と主役の立て方が上がる・開始は +40〜70 s・費用 +40%) / `super` = 著者 high (brief なし)・担当 high (絵と台詞も)・レビュー medium (cut の静止画と指摘全部を見る監督)・直し warn (質は最上・再生開始まで 6〜10 分・費用は plus の 2 倍)。
     ユーザーの指定が無ければ **`standard` か `plus` を基本に、依頼の長さと型で選ぶ** (10-30 の 5 題材 bench): 60 s 以下と story / cinematic は `standard`・90 s 以上の解説 / 比較 / 数字物は `plus`。「急いで」「とにかく早く」は `light`、「質を優先して」「時間と費用が掛かってよい」は `super`。選んだ mode と理由は最後に 1 行で伝える。
   - 既定は著者 `--author low`・担当 `--staff balanced` (cut 1・2 は担当 low、cut 3 以降は medium の見込み完了が再生に間に合う時だけ medium — 間に合わない見込みなら low に落とし、再生開始後に止まらない事を優先する。担当は絵と台詞を変えず、絵と声は著者の版から担当と並列に作る)・直し役 `--fix severe` = DEFECT と severe の指摘の時だけ直す・レビュー `--review none`。質を優先する時は `--staff medium` (全 cut medium・再生が担当の尻尾に追いつき途中で止まり得る)・`high` / `xhigh` はさらに強く遅い。急ぐ時だけ `--staff none` (担当なし・質は落ちる)。見本は型から自動 (`--samples a.md,b.md` で替えられる)。
   - 役を個別に動かすなら: **直し役の段** `--fix defect|severe|warn|none` (warn まで直すと担当の後に直し役の call が cut ごとに乗る)・**レビュー** `--review low|medium|none` (担当の後に 1 回、静止画を見る監督。cut ごとに 25〜45 s 直列に乗る・`--fix none` とは併用不可)・担当に絵と台詞も直させる `--staff-assets`。
   - 構図の質を優先する別の形: `--author-brief` = 著者は台本 (台詞)・cut ごとの絵コンテ・transition と root だけを書き、絵は cut ごとの担当がゼロから設計する (`--staff-assets` を含意・台詞は著者の版で固定・`--staff none` とは併用不可)。担当が著者の構図に縛られない分、絵の密度と主役の立て方が上がりやすい。完成はやや遅く、生成の費用も増える。著者の effort (`--author low|medium|…`) とは別の軸で、組み合わせられる (`--author-brief --author medium` = brief の著者を medium で)。
   - 生成後にユーザーが NoLang の編集画面で自分で調整したい動画は `--editable` — 編集画面で扱える文法サブセット (要素数・動きの preset など) に収めて書く (表現の密度は下がる)。
   - 話している音声 (トーク・インタビュー・講演の録音) から作る動画 (切り抜き・要点の紹介・ショート) は `--speech <音声の file か id>` (話者の人数が分かれば `--speakers N`)。サーバーが文字起こしし、その音声を切って使う (声は録音のまま)。長さは音声から決まる (目安があれば `--seconds`)。文字起こしを待つので、再生までは数分かかる。依頼文には「どこを使うか・何を切るか (フィラー・言い直し)」を書く。
   - サーバーが再生できる状態になった時点で返る (Claude の目安は既定 (balanced) で 1 分強・`--staff medium` で 1 分半ほど・`--staff none` で 1 分ほど。Codex の速度はモデルと依頼による)。生成はその後も裏で最後まで続く。待ち時間 (super は 9 分半・ほかは 7 分) を超えても生成が続いていれば、`still_generating: true` と視聴 URL を返す (失敗ではない。`tell_user` を書いて終える)。
   - **同時に生成中にできる動画は 2 本まで** (法人プランはテナント全体で 2 本)。`nolang make` は再生できた時点で返るが、動画は完成まで生成中に数える。何本か続けて作る時に、上限のエラー (`CONCURRENT_GENERATION_LIMIT`・「同時に作れる動画の数の上限」) が出たら、`nolang status <前の video_id> --wait` で前の動画の完成を待ってから次を始める。
4. **知らせる** (最優先・冒頭の「最重要」): 出力の `tell_user` (案内の文 + 次の行に URL) を、次のツールを呼ぶ前に**そのままユーザーへのメッセージの本文に書く**。他に頼まれていなければ、そこでターンを終える。完成の確認は頼まれた時だけ (`nolang status <video_id> --wait` → `completed` で URL と mp4 の `download_url`)。
5. **失敗した時** (`ok: false`): `error` と、あれば `watch_url` をユーザーに伝える。原因は `error` と `run_tail` (engine の出力の末尾) で分かる。サーバーが開始を断った時は、`error` が「サーバーが生成の開始を断った: …」になる — クレジット不足 (`INSUFFICIENT_CREDIT`) は待っても直らないので、ユーザーに伝えて止める。同時生成の上限は上の手順で待つ。`python3` / 選択したエンジンが無い時は `write-yourself.md` の A で作る。同じ依頼の作り直しは別の dir で 1 回まで。原因を探すために試しの動画を作らない。

## R. 完成した動画を直す (「この動画のここを直して」と頼まれた時)

元の動画はどちらの手でもそのまま残り、直った動画が新しい URL でできる。対象は `video_id` (視聴 URL の UUID)。

1. まず `nolang patch <video_id> --request-text "<直す点>"` — server の決定論の直し。台詞の言い換え・見た目 (色・大きさ・BGM 音量)・素材の差し替えなどが数十秒で当たり、声と触らない cut は再利用される。`stage: "applied"` なら出力の `tell_user` を伝えて終わり。`clarify` は質問に答えて (分からなければユーザーに聞いて) `--answered` で出し直す。
2. `applied` にならなかった時 (`stage: rebuild / clarify_suppressed / unsupported / …`) は `nolang edit <dir> <video_id> --request-text "<直す点>"` — 保存された原稿を種に編集役が依頼のぶんだけ書き換え、触らない cut はそのまま通る (1〜3 分)。作り直し級の依頼 (長さ・縦横・全体のスタイル変換) は、ここから自動で元の動画を参照にした作り直しに倒れる。
3. どちらも新しい動画を作らずに終わった時だけ、依頼文に `[video:<video_id>]` を書いて `nolang make` (参照つきの作り直し)。

## L. ログイン (「NoLang にログインして」と頼まれた時も、作る前も)

`nolang auth status`。終了コード 0 ならログイン済み。3 (未ログイン) なら、自分で始める:

- `nolang auth login --background` (すぐ戻る)。**次のメッセージで真っ先に**出力の `tell_user` (URL・有効時間・デバイス認可ならコードを含む案内文) を**自分のメッセージの本文に**そのまま書く。手元の機械ならブラウザでログイン画面が開き、ユーザーは「許可」を押すだけ (コード入力なし)。SSH・コンテナなどのデバイス認可では、ユーザーが URL を開き、`user_code` を入力して自分で始めたログインであることを確認し、許可する。コードを省かない。伝えたら、待つ間に依頼の中身を決めてよい。
- ブラウザ認可で進めない (ブラウザが別の機械にしか無い・許可後に接続エラーで URL も貼れない) と言われたら、`nolang auth login --background --device` (コードを入力する方式) でやり直す。
- 作るコマンドや素材のコマンドの前に `nolang auth wait` (最大 120 秒・終了コード 0 で完了)。まだ (終了コード 3・`"waiting": true`) ならもう一度。まだ許可されていない・切れていた (`failed` なら `--background` をやり直す) 時は、そこで止まって (ターンを終えて) ユーザーの「許可した」を待つ — 止まる時のメッセージにも `authorize_url` と、デバイス認可なら `user_code` をもう一度本文に書く (「上の URL」と書かない)。
- ブラウザに `ACCESS DENIED` (403) と出る → 接続元の IP が NoLang の許可リストに無い。同じブラウザで `https://<ログイン画面のホスト>/cdn-cgi/trace` を開き、`ip=` の値を管理者に伝えてもらう。
- SSH・コンテナでは同じ `--background` が自動でデバイス認可を使う。ポート転送は不要。未対応のサーバーではブラウザ認可へ戻る。その戻り先が接続エラーになったら、**ログインをやり直さず**許可後のアドレスバーの URL を貼ってもらい、`nolang auth complete '<URL>'` で待機中のログインを完了する。`--browser --background` でブラウザ認可を指定でき、`--no-browser` で始めた従来の手動方式も同じ `complete` を使う。
- 終了コード 4 (つながらない) → `nolang doctor` の結果をユーザーに伝える (README.md の「つなぐ先の準備」)。

## M. 決まった素材を使う (依頼に「この写真・この動画」「この曲」「この声」がある・手元の file を渡された時だけ)

- 手元の file → `nolang assets upload <file>…` で自分の素材に送り、`ref` (`id=<uuid>`) を得る (動画は仕上げを待つので数十秒)。MCP は file の中身を運べないので、upload は CLI で。音声 (mp3・m4a・wav…) は持ち込み音声として送られ、`nolang make --speech <id>` で使う (§S)。
- NoLang の素材から選ぶ → `nolang assets search <kind> "<説明か名前>"` (MCP なら `nolang_assets_search(kind, q)`)。自分が送った物は `--mine` (`scope="mine"`)。kind = `image` `footage` `bgm` `soundeffect` `speaker` `avatar` `font`。`preview_url` で中身を確かめられる。
- studio で作る時は、`ref` と使い所を依頼文に書く。自分で書く時は、`ref` を応答の `usage` の位置に書く: 画像・動画素材 = 根に `image 名 = id=…`、置く所に `content: @名` (動画素材は `play: loop` も)・BGM = `bgm#名 id=…`・効果音 = `sound 名 = id=…` か台詞に `[♪id=…]`・話者 = `cast 名 = id=…`・立ち絵 = `cast 名 = "声の説明" avatar="名"`・書体 = `font "名 太さ"`。
- id は全桁の `id=<uuid>` だけ (8 桁の id と `file=名` はこの経路では使えない)。読めない id は check が `DEFECT:ASSET_UNREADABLE` で止める。
- 決まった素材が無い所は説明文で書く (絵は生成、声・BGM・効果音・書体は説明文でカタログから選ばれる)。

## CLI の呼び方

`nolang` が PATH にあればそれ、無ければ `node ../../cli/nolang.mjs` (この skill の directory から。以下 `nolang` と書く)。
結果は stdout に JSON・途中経過は stderr。終了コード 0 成功 / 1 原稿の欠陥・生成の失敗 / 2 使い方 / 3 未ログイン / 4 接続。

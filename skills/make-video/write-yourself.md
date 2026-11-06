# 原稿を自分で書いて流す (studio が使えない時)

`SKILL.md` の §S (`nolang make`) が使えない時だけ読む。リンクの渡し方は `SKILL.md` 冒頭の「最重要」に従う。ログインは `SKILL.md` の §L、決まった素材は §M。
あなたが台本と画面 (draft src = `design.txt` と `timeline.txt`) を書き、NoLang のサーバーが声・絵・BGM・描画を担当する。
この file のパスはすべてこの skill の directory からの相対。

## 1. 原稿を書く (§A と §B 共通・この順で・寄り道しない)

0. **文書を server から取る** (書き始める前に 1 回): 文法の文書 (spec.md・辞書・見本) は plugin に入っていない — server の現行の物を読む。
   - シェルがある時: `nolang reference` → 出力の `dir` が文書一式の directory。以後この file で `<dir>/<名>` と書いてある所はそれを読む。終了コード 1 で contract の案内が出たら、書かずに止まって案内をユーザーに伝える。
   - シェルが無い時 (MCP): `nolang_draft_sync()` → `contract` (開始の `client_contract` に渡す)・`min_supported`・`docs` (文書の一覧)。文書は `nolang_draft_reference(path="<名>")` で読む (大きい文書は節の一覧が返るので `section` に見出しを渡して節ごとに・見本は `path="samples/"` の一覧から §1 の 2 と同じ規則で選び、1 本ずつ読む)。
1. **依頼から決める**: 伝えること 1 文・縦横 (`16:9` / `9:16`)・長さの目安 (依頼に明示があればその秒数・無ければ指定しない = 内容に合わせる)・型 (`concept` 解説 / `data` 数字 / `compare` 比べる / `story` 物語 / `cinematic` 映像寄り)。聞き返さず既定で進め、決めた値は最後にユーザーへ伝える。
2. **文法と見本 2 本を読む**: 文法は §2 (`<dir>/spec.md` の全文)。見本は NoLang の studio と同じ選び方で: `node scripts/pick_samples.mjs --type <型> --aspect <縦横> --request "<依頼文>" --reference <dir>` が `<dir>/samples/` から 2 本を選ぶ: NoLang の src (`<型>_NN.md`・字幕と cut の組み方の手本) 1 本と、hf の写し (`hf_<型>_*.md`・絵と動きの作り込みの手本) 1 本 (同じ題材の見本を外し、同じ向きを先に。同じ向きの NoLang の src が無い型は hf の写しを 2 本)。出た 2 本を全文読む (1 行目の題・`見せる作り:` の要約・design.txt と timeline.txt の全量)。シェルが無い時は同じ規則で自分で選ぶ。骨組み `<dir>/scaffolds/` は文法の形を確かめる時だけ見る。
3. **決まった素材を使う時だけ**: `SKILL.md` の §M で `ref` を得て、応答の `usage` の位置に書く。
4. **書く** (design system が先・書いた cut から流す):
   - **書く前に構成を決める**: cut の名と中身 (1 cut 1 行) を先に決める。cut は書いた端から投入し、投入した cut は直せないので、書きながら前の cut に戻らない。
   - **根に design system を 1 回決める**: `<dir>/looks.md` の「style の組」から依頼の気分で 1 つ選び、根に `palette` `font` `fonts` `motion` `transition` と、見出し・本文・札・箱の `def` (= class) を書く。値は題材に合わせる。見本は作り方の手本 (場面の組み方・部品の `def`・動き・語の印の打ち方) — 見本の色・書体をそのまま写さない。
   - 根の中の題材の物: `image 名 = "…"` (基準画像の説明)・`bgm` の説明・`cast` (声の説明を依頼の言語と調子に)・`art` (画風)。`lint off=…` と `# ` の注記は書かない。
   - **cut** は依頼の構成で組み直す: 依頼の流れを cut に分け (60 秒で 5〜8 cut・1 cut に台詞 1〜3 文が目安)、各 cut に見本の場面の型から合う物を当てて組み、文字・台詞・絵の説明を題材で書く。見本の cut の数と順には合わせない。使わない場面と `def` は消す。
   - **子を持つ要素を `.sticky` にしない**: cut を跨ぐ `.sticky` は子の無い要素 (1 枚の札・線・`veil`) だけに付ける。常設の帯・章の札・進行の点灯のように子を持つ物は `def` にして、各 cut に置き直す (今の章の点灯や済みの印は、cut ごとの引数か変種で)。子を持つ `.sticky` は、cut を順に投入する所で止まる (check の `DEFECT:prefix_broken`) か、check を通っても生成の最後で失敗する (`同じ lane の group は floor が同じであること` — engine の不具合で check では拾えない)。見本の多くがこの作りを含むので、写す時に直す (`pick_samples.mjs` が見本ごとに知らせる)。
   - 文字は枠に収まる長さに (見本の文字の長さが目安・長いと check の `shrink_estimate`)。要素の `#名` は cut ごとに付け替え、cut を跨いで同じ名を使わない (根の `.sticky` の物を除く)。
   - 1 cut = design の `section#名` の block + timeline の `*** 名` の block (名は一致させる)。CLI なら作業用の directory (例 `./nolang-videos/<英小文字の名>/`) に `design.txt` と `timeline.txt` として保存する。
   - **書く順**: 根 + 1 つ目の cut を書いたら流し始め (§A の 2・§B)、以後は 1 cut 書き足すごとに投入する。全部を書き終えてから投入しない (再生が始まるまで何分も待たせる)。

## A. CLI で流す

1. **ログイン**: `SKILL.md` の §L。
2. **流し始める** (根と 1 つ目の cut を書いたら): `nolang start <dir> --title "<題>" [--seconds <秒> (目安がある時だけ)]` (縦横は design の `canvas` から) → すぐ `nolang submit <dir>`。DEFECT が返ったら、その cut だけを直して `nolang submit <dir>` し直す (DEFECT は stderr に `DEFECT:コード file:行 原因。直し方: …`・投入済みの cut は直せないので変えない)。通信が切れて投入の結果が分からなくても、そのままもう一度 `nolang submit <dir>` でよい (server の受理状態と照合して続きから投入する)。
3. **知らせる** (必ず・2 つ目の cut を書く前に): 1 つ目の submit が成功したら、出力の `tell_user` (案内の文 + 次の行に URL) を**そのままユーザーへのメッセージの本文に書く**。数十秒で再生が始まり、続きは投入した端から伸びる。
4. **続きを流す**: 次の cut を design.txt と timeline.txt に書き足して `nolang submit <dir>`。これを cut の数だけ繰り返す。**投入の間は 180 秒以内** (空くとサーバーが生成を失敗にする) — 1 cut を書いたらすぐ submit する。最後の cut は `nolang submit <dir> --end`。
5. **終える**: `--end` の submit が返ったら、出力の `tell_user` (案内の文 + 次の行に URL) を書いて、ターンを終える。完成の確認は頼まれた時だけ (`nolang status <video_id> --wait` → `completed` で「完成しました」と URL・mp4 は `download_url`)。
6. **失敗した時** (submit が `No Video matches`・status が `failed`): その動画は終わり。原稿を見直して (§1 の 4 の規則を破っていないか)、`<dir>/stream.json` を消して start から作り直すのは 1 回まで。それでも `failed` なら止めて、ユーザーに video_id と「check は通ったが生成で失敗した」ことを伝える (サーバー側の問題のことが多い・管理者に伝えてもらう)。**原因を探すために試しの動画を作らない** (cut を減らした版を何本も create するなど — 1 本ごとに GPU と費用を使い、何十分もかかる)。

## B. MCP で作る (シェルが無い時)

### つながっているか

- `nolang_draft_check` などの `nolang_draft_*` ツールが見えれば準備完了 (実際の名前には client ごとの接頭辞が付く)。
- 認証がまだの時:
  - Claude Code: `authenticate` しか見えない → それを呼び、返った URL をユーザーに開いてもらう (NoLang にログインして許可)。ブラウザが `http://localhost:<port>/callback?code=…` で接続エラーになったら、アドレスバーの URL を貼ってもらい `complete_authentication` に渡す。
  - Codex: ユーザーに端末で `codex mcp login nolang` を実行してもらい (ブラウザでログインして許可)、Codex を起動し直してもらう。
- つながらない・ログインできない → (シェルがあれば `nolang doctor` の結果を添えて) ユーザーに伝える。接続先は `https://api.no-lang.com` (API) と `https://no-lang.com` (ログイン)。

### 手順 (§1 の原稿を、書いた cut から)

文書は §1 の 0 で server から取っておく (`nolang_draft_sync` → `nolang_draft_reference`)。

1. **開始** (根と 1 つ目の cut を書いたら): `nolang_draft_start(title, aspect_ratio, language="ja", duration_s, client_contract=<nolang_draft_sync の contract>)` → `video_id` と `watch_url`。`client_contract` は必ず渡す (版が合わない plugin を server が開始前に止める — `DRAFT_CLIENT_CONTRACT_UNSUPPORTED` が返ったら、その `error` の案内をユーザーに伝えて止まる)。`template_video_id` は省略する (空のテンプレ)。生成後にユーザーが編集画面で調整したい動画は `editable=true` — 編集画面で扱える文法サブセットに収めて書く (破った投入は `DEFECT:editable_*` で 400。規則と閾値は `GET drafts/rules/` の `profile` 列と `profiles.editable`・投入前の検査は `nolang_draft_check(profile="editable")`)。
2. **1 つ目を投入**: `nolang_draft_submit_cut(video_id, text)` — text = 根の design + 根の timeline (先頭の `#v2` 行は除く) + 1 つ目の cut の `section#` block + `*** ` block。`defects` が返ったらその cut を直して投入し直す。
3. **知らせる** (必ず・2 つ目の cut を書く前に): 1 つ目が受理されたら、案内の文の次の行に `watch_url` だけを書いてユーザーに渡す (数十秒で再生が始まり、続きは投入した端から伸びる)。
4. **続きを流す**: 次の cut を書いたら `nolang_draft_submit_cut(video_id, text)` — text = その cut の `section#` block + `*** ` block だけ。最後の cut は `end=true`。投入の間は 180 秒以内。
5. **終える**: 最後の cut が受理されたら、もう一度 `watch_url` を単独の行で書いてターンを終える。完成の確認は頼まれた時だけ (`nolang_video_status` の `completed`)。

1 つ目の text の形 (例):

```
#v2
canvas 1920x1080 bg=#0B1220
…根の design の残り…
cast narrator = "…"
transition = dissolve,300,overlap=300
section#title
img#t_bg(inset: 0; content: @bg)
h1#t_h(left: 120px; top: 294px; width: 1680px; height: 216px) 見出し
*** title
[>#subtitle]
bgm music
@narrator: [>#t_h]最初の台詞。
```

### 守ること (守らないと失敗する)

- `submit_cut` を並列に呼ばない。呼んだ順が動画の順になる。
- start の後、投入の間が 180 秒空くとサーバーが生成を失敗にする → 構成を先に決めておき、1 cut を書いたらすぐ投入する。
- `defects` が返った cut は流れていない。直して同じ cut を投入し直す (次の cut に進まない)。
- `No Video matches the given query.` = その動画はもう失敗している。`nolang_video_status` で `failed` を確かめ、start からやり直す。start 直後の失敗が続くならサーバー側の問題なので、スタックの管理者に伝える (原稿の問題ではない)。

## 2. 文法 (書く前に全文読む)

`<dir>/spec.md` (MCP は `nolang_draft_reference(path="spec.md")`) を全文読む (draft src の書き方の全量・約 17 KB — 4 つの圧縮の規則と例・CSS / GSAP との違い・書き方の対応・書けない物)。この file に要約を置かないのは、手写しの要約は文法が変わると古びるため (spec.md は §1 の 0 で server から取る)。
spec.md の中の `bash` の block (`studio.py` の `new` / `check` / `render` …) と「render で 1 回描く」は NoLang の repo の中の studio の手順 — ここでは check と描画は server がする (§A / §B の手順に従う)。素材は名や id で指定しない (例外は依頼に決まった素材がある時だけ — `SKILL.md` の §M)。

## 3. 辞書 (詰まった時だけ引く)

`<dir>` は §1 の 0 の directory (MCP は `nolang_draft_reference(path="<名>")`)。

- `<dir>/authoring.md` 文法の辞書。大きいので節ごとに読む: `grep -n '^##' <dir>/authoring.md` で見出しの行番号を出し、Read の `offset` / `limit` で読む。節は HTML 形 · 字句 · design.txt (型・位置・動き・×N と def と根の雛形・字幕と cut) · timeline.txt (印・時刻の規則・cue と切替) · 欠陥 · HTML の動画を写すとき。key の名は v2 の綴り (`size` `fill` `radius` `shadow` …) で載っているが、CSS の名 (`font-size` `background` `border-radius` `box-shadow` …) でそのまま書ける。
- `<dir>/rules.md` check の `findings` の規則名と直し方。
- `<dir>/looks.md` 見た目の作り方 / `<dir>/sounds.md` 音 / `<dir>/capabilities.md` できる表現と代用。
- `<dir>/samples/` 型ごとの見本 (`<型>_NN.md` は NoLang の src・`hf_*` は絵と動きの作り込みの見本・§1 の 2 で 1 本ずつ選ぶ)。

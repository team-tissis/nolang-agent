# 原稿を自分で書いて流す (studio が使えない時)

`SKILL.md` の §S (`nolang make`) が使えない時だけ読む。リンクの渡し方は `SKILL.md` 冒頭の「最重要」に従う。ログインは `SKILL.md` の §L、決まった素材は §M。
あなたが台本と画面 (draft src = `design.txt` と `timeline.txt`) を書き、NoLang のサーバーが声・絵・BGM・描画を担当する。
この file のパスはすべてこの skill の directory からの相対。

## 1. 原稿を書く (§A と §B 共通・この順で・寄り道しない)

0. **文書は server の現行を読む** (書き始める前に): 文法の文書 (spec.md・辞書・見本) は plugin に入っていない。
   - シェルがある時: `nolang reference` → 出力の `dir` が文書一式の directory (nolang が起動のたびに server と揃える束の中)。以後この file で `<dir>/<名>` と書いてある所はそれを読む。
   - シェルが無い時 (MCP): `nolang_draft_reference(path="<名>")` で読む (大きい文書は節の一覧が返るので `section` に見出しを渡して節ごとに・見本は `path="samples/"` の一覧から §1 の 2 と同じ規則で選び、1 本ずつ読む)。
1. **依頼から決める**: 伝えること 1 文・縦横 (`16:9` / `9:16`)・長さの目安 (依頼に明示があればその秒数・無ければ指定しない = 内容に合わせる)・型 (`concept` 解説 / `data` 数字 / `compare` 比べる / `story` 物語 / `cinematic` 映像寄り)・言語 (台詞を書く言語 = 依頼に明示があればそれ・無ければ依頼文の言語)。聞き返さず既定で進め、決めた値は最後にユーザーへ伝える。
2. **文法と見本 2 本を読む**: 文法は §2 (`<dir>/spec.md` の全文)。見本は NoLang の studio と同じ選び方で: `node scripts/pick_samples.mjs --type <型> --aspect <縦横> --request "<依頼文>" --reference <dir>` が `<dir>/samples/` から 2 本を選ぶ: NoLang の src (`<型>_NN.md`・字幕と cut の組み方の手本) 1 本と、hf の写し (`hf_<型>_*.md`・絵と動きの作り込みの手本) 1 本 (同じ題材の見本を外し、同じ向きを先に。同じ向きの NoLang の src が無い型は hf の写しを 2 本)。出た 2 本を全文読む (1 行目の題・`見せる作り:` の要約・design.txt と timeline.txt の全量)。シェルが無い時は同じ規則で自分で選ぶ。骨組み `<dir>/scaffolds/` は文法の形を確かめる時だけ見る。
3. **決まった素材を使う時だけ**: `SKILL.md` の §M で `ref` を得て、応答の `usage` の位置に書く。
4. **書く** (design system が先・書いた cut から流す):
   - **書く前に構成を決める**: cut の名と中身 (1 cut 1 行) を先に決める。cut は書いた端から投入し、投入した cut は直せないので、書きながら前の cut に戻らない。
   - **根に design system を 1 回決める**: `<dir>/looks.md` の「Style kits」から依頼の気分で 1 つ選び、根に `palette` `font` `fonts` `motion` `transition` と、見出し・本文・札・箱の `def` (= class) を書く。値は題材に合わせる。見本は作り方の手本 (場面の組み方・部品の `def`・動き・語の印の打ち方) — 見本の色・書体をそのまま写さない。
   - 根の中の題材の物: `image 名 = "…"` (基準画像の説明)・`bgm` の説明・`cast` (声の説明を依頼の言語と調子に)・`art` (画風)。`lint off=…` と `# ` の注記は書かない。
   - **cut** は依頼の構成で組み直す: 依頼の流れを cut に分け (60 秒で 5〜8 cut・1 cut に台詞 1〜3 文が目安)、各 cut に見本の場面の型から合う物を当てて組み、文字・台詞・絵の説明を題材で書く。見本の cut の数と順には合わせない。使わない場面と `def` は消す。
   - **子を持つ要素を `.sticky` にしない**: cut を跨ぐ `.sticky` は子の無い要素 (1 枚の札・線・`veil`) だけに付ける。常設の帯・章の札・進行の点灯のように子を持つ物は `def` にして、各 cut に置き直す (今の章の点灯や済みの印は、cut ごとの引数か変種で)。子を持つ `.sticky` は、cut を順に投入する所で止まる (check の `DEFECT:prefix_broken`) か、check を通っても生成の最後で失敗する (`同じ lane の group は floor が同じであること` — engine の不具合で check では拾えない)。見本の多くがこの作りを含むので、写す時に直す (`pick_samples.mjs` が見本ごとに知らせる)。
   - 文字は枠に収まる長さに (見本の文字の長さが目安・長いと check の `shrink_estimate`)。要素の `#名` は cut ごとに付け替え、cut を跨いで同じ名を使わない (根の `.sticky` の物を除く)。
   - 1 cut = design の `section#名` の block + timeline の `*** 名` の block (名は一致させる)。CLI なら作業用の directory (例 `./nolang-videos/<英小文字の名>/`) に `design.txt` と `timeline.txt` として保存する。
   - **書く順**: CLI (§A) は、根 + 1 つ目の cut を書いたら流し始め (§A の 2)、以後は 1 cut 書き足すごとに投入する。全部を書き終えてから投入しない (再生が始まるまで何分も待たせる)。MCP (§B) は、最後の cut まで書いてから 1 回で渡す。

## A. CLI で流す

1. **ログイン**: `SKILL.md` の §L。
2. **流し始める** (根と 1 つ目の cut を書いたら): `nolang start <dir> --title "<題>" --language <台詞の言語: ja / en / …> [--seconds <秒> (目安がある時だけ)] [--pin <video_id> (下の「前の動画の素材を継ぐ」)]` (`--language` は必須・縦横は design の `canvas` から) → すぐ `nolang submit <dir>`。DEFECT が返ったら、その cut だけを直して `nolang submit <dir>` し直す (DEFECT は stderr に `DEFECT:コード file:行 原因。直し方: …`・投入済みの cut は直せないので変えない)。通信が切れて投入の結果が分からなくても、そのままもう一度 `nolang submit <dir>` でよい (server の受理状態と照合して続きから投入する)。
3. **知らせる** (必ず・2 つ目の cut を書く前に): 1 つ目の submit が成功したら、出力の `tell_user` (案内の文 + 次の行に URL) を**そのままユーザーへのメッセージの本文に書く**。数十秒で再生が始まり、続きは投入した端から伸びる。
4. **続きを流す**: 次の cut を design.txt と timeline.txt に書き足して `nolang submit <dir>`。これを cut の数だけ繰り返す。**投入の間は 600 秒以内** (空くとサーバーが生成を失敗にする) — 1 cut を書いたらすぐ submit する。最後の cut は `nolang submit <dir> --end`。
5. **終える**: `--end` の submit が返ったら、出力の `tell_user` (案内の文 + 次の行に URL) を書いて、ターンを終える。完成の確認は頼まれた時だけ (`nolang status <video_id> --wait` → `completed` で「完成しました」と URL・mp4 は `download_url`・クレジット表記 `copyright` も伝える — 公開する時に載せる)。
6. **失敗した時** (submit が `404 NOT_FOUND` (`Video not found.`)・status が `failed`): その動画は終わり。原稿を見直して (§1 の 4 の規則を破っていないか)、`<dir>/stream.json` を消して start から作り直すのは 1 回まで (start に `--pin <失敗した video_id>` を付ける — その回が作った絵と選んだ声を継ぎ、作り直さない)。それでも `failed` なら止めて、ユーザーに video_id と「check は通ったが生成で失敗した」ことを伝える (サーバー側の問題のことが多い・管理者に伝えてもらう)。**原因を探すために試しの動画を作らない** (cut を減らした版を何本も create するなど — 1 本ごとに GPU と費用を使い、何十分もかかる)。
   - submit が `503 DRAFT_WORKER_UNAVAILABLE` の時は、その cut は投入されていない。そのままもう一度 `nolang submit <dir>`。2 回続けて同じなら server の側で生成が落ちている (status は `running` のまま残る) — 待たずに `<dir>/stream.json` を消して、同じ原稿で `nolang start … --pin <その video_id>` からやり直す (その回が作った絵と選んだ声を継ぐ)。出力の `fix` に同じ手順が出る。

### 前の動画の素材を継ぐ (`nolang pull` と `--pin`)

- `nolang pull <dir> <video_id か URL>`: テンプレか自分の動画の保存済みの原稿を `<dir>/reference/` に書く (`design.txt`・`timeline.txt`・`brief.md` = 形の要約)。
- `--pin <video_id>` (`nolang check`・`nolang create`・`nolang start`): その動画の素材の台帳を継ぐ。原稿の素材のうち、その動画の原稿と**文面が同じ物**が同じ素材に決まる — 自分の動画なら絵・声・文字の style、テンプレなら文字の style・書体・`id=` の素材。文面を変えた素材は選び直し・作り直しになる。
- **自分の動画を直して描き直す**: `pull` → `reference/` の `design.txt` と `timeline.txt` を `<dir>` 直下に写す → 直す所だけ書き換える (残したい絵・声の行は 1 字も変えない・変えたい絵は説明を書き換える) → `nolang check <dir> --language <言語> --pin <video_id>` → `nolang create <dir> --title "<題>" --language <言語> --pin <video_id>`。根の画風の行 (`art` など) を変えると、絵は全部作り直しになる。
- **テンプレの形で新しく書く**: `pull` → `brief.md` と原稿を読んで新しく書き、同じ `--pin <テンプレの video_id>` を付ける (テンプレの文字の style と書体がそのまま使われる)。
- `nolang check` の `--language` と `--pin` は、`create` / `start` に渡すのと同じ値にする (投入の検査と同じ答えになる)。`start` 済みの dir では付けない (その動画の設定で見る・書き途中の検査 — 最後の cut まで書いたら `--end`)。

### 持ち込み音声を切って使う・文字起こしだけ取る (`nolang transcribe` と `--speech`)

- `nolang transcribe <音声か動画の file か id>… [--speakers N] [--language <言語>]`: 音声 (mp3・m4a・wav など) か話している動画 (mp4・webm・mov) を文字起こしして (4 本まで)、発話の台帳 (`brief` = 発話ごとの id・時刻・原文と `@clip` の書き方) を返す。**クレジットを消費する** (音声の長さに比例・1 分あたり約 3・同じ音声は 1 度だけ)。動画は同じ id の動画素材にもなり、原稿で声と同じ時計の映像を置ける (`brief` の `content: @clip`)。
- その音声を原稿で切って使う (本人の語りのまま字幕や図を重ねる) 時は、`brief` の書き方で `@clip` を書き、返った id を `nolang check`・`nolang create`・`nolang start` に `--speech <id>[,<id>]` で渡す (3 つとも同じ値)。
- 参考の動画の台詞と時刻を読むだけなら `--speech` は付けない (声は NoLang が合成する)。

### 動く映像を入れる (AI クリップ・`--clip-seconds`)

- `nolang create` / `nolang start` に `--clip-seconds <秒>` を付けると、原稿の `media: footage` の絵 (`img#名(media: footage) 説明`) が動画生成で作られる。書き方は `nolang reference` の dir の `ai_clips.md` を読む。
- 秒数は新しく作るクリップの合計の上限。その秒数ぶんを先行消費し (1 秒あたり約 8 クレジット)、作った分へ精算する。上限を超えた分は生成画像になる。
- **standard 以上のプランだけ** (無料プランは断られる — `nolang account` で plan を確かめる)。付けなければ `media: footage` は生成画像になる。
- 実写の映像が主体の動画 (料理・Vlog など) や、ユーザーが動く映像を求めた場面だけに使う。作り終えたクリップは、描く前に中断しても請求される。

### 投入の前に絵を確かめる (`nolang stills`)

- `nolang start` の後、`nolang stills <dir> [cut]` が、まだ投入していない cut (既定 = 次の cut) を本物の絵の静止画にして `<dir>/stills/<cut>/` に置く (数十秒〜・最大 4 枚)。画像を見て、よければ `nolang submit`、直すなら cut を書き換えて `nolang check <dir>` → もう一度 `nolang stills`。
- ここで作った絵と声は、同じ文面の cut を投入すればそのまま使われる。**作った時点で請求の対象** (投入しなくても精算に入る) なので、見るだけの試し描きを重ねない。
- `unwarmed` に名が返った絵は、間に合わず仮の絵で描いた物 (中身で判断しない)。
- 静止画・`nolang check` (start 済みの dir) は投入の間の 600 秒を数え直す。

## B. MCP で作る (シェルが無い時)

原稿を全部書いてから、1 回で渡す。検査と直しは NoLang の server がする (cut を順に流す・合図を送る手順は要らない)。
NoLang に台本を書かせる `nolang_create_video` より、クレジットが安く済む (台本と画面を書く LLM の分が掛からない)。

### つながっているか

- `nolang_draft_submit` が見えれば準備完了 (実際の名前には client ごとの接頭辞が付く)。
- 認証がまだの時:
  - Claude Code: `authenticate` しか見えない → それを呼び、返った URL をユーザーに開いてもらう (NoLang にログインして許可)。ブラウザが `http://localhost:<port>/callback?code=…` で接続エラーになったら、アドレスバーの URL を貼ってもらい `complete_authentication` に渡す。
  - Codex: ユーザーに端末で `codex mcp login nolang` を実行してもらい (ブラウザでログインして許可)、Codex を起動し直してもらう。
- つながらない・ログインできない → (シェルがあれば `nolang doctor` の結果を添えて) ユーザーに伝える。接続先は `https://api.no-lang.com` (API) と `https://no-lang.com` (ログイン)。

### 手順

文書は §1 の 0 のとおり `nolang_draft_reference` で server の現行を読む。

1. **書く**: §1 の原稿を最後の cut まで書く (design = 根 + 全 cut の `section#名` の block・timeline = 根 + 全 cut の `*** 名` の block)。
2. **確かめる** (任意): `nolang_draft_check(design, timeline, language, aspect_ratio)` — `defects` が返ったら直す。残しても server の直し役が直すが、0 にしてから出すと意図どおりに仕上がる。何も消費しない。
3. **渡す**: `nolang_draft_submit(title, aspect_ratio, language, design, timeline)` → `stage: accepted` と `watch_url`。`language` は書いた台詞の言語 (必須)。`aspect_ratio` は根の `canvas` と同じ比 (16:9 = `canvas 1920x1080`・9:16 = `canvas 1080x1920`)。生成後にユーザーが編集画面で調整したい動画は `editable=true` (編集画面で扱える文法サブセットに収めて書く・投入前の検査は `nolang_draft_check(profile="editable")`)。
4. **知らせる** (必ず・次の tool を呼ぶ前に): 案内の文の次の行に `watch_url` だけを書いてユーザーに渡す (生成中から再生でき、完成まで数分)。他に頼まれていなければターンを終える。完成の確認は頼まれた時だけ (`nolang_video_status` の `completed` — `download_url` とクレジット表記 `copyright` も伝える)。

### 守ること

- `stage: in_progress` = 同じ原稿を受付の途中 — 少し置いて同じ原稿で呼び直す。同じ原稿の再送は同じ動画を返す (応答を失った時の呼び直しで動画が重ならない)。
- 形の誤り (`design` に cut が無い・design と timeline の cut が揃わない・根の `canvas` が `aspect_ratio` と違う) は error で返る。直して出し直す。
- `nolang_video_status` が `failed` = 直しきれない cut があった (クレジットは戻る)。`nolang_draft_check` の `defects` を直して出し直す。
- 持ち込み音声・参照の動画の素材の引き継ぎ・AI クリップは、この入口では使えない (シェルのある環境で §A)。NoLang の素材は `nolang_assets_search` の `ref` を原稿に書けば使える。

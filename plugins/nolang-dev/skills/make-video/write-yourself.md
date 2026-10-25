# 原稿を自分で書いて流す (studio が使えない時)

`SKILL.md` の §S (`nolang make`) が使えない時だけ読む。リンクの渡し方は `SKILL.md` 冒頭の「最重要」に従う。ログインは `SKILL.md` の §L、決まった素材は §M。
あなたが台本と画面 (draft src = `design.txt` と `timeline.txt`) を書き、NoLang のサーバーが声・絵・BGM・描画を担当する。
この file のパスはすべてこの skill の directory からの相対。

## 1. 原稿を書く (§A と §B 共通・この順で・寄り道しない)

1. **依頼から決める**: 伝えること 1 文・縦横 (`16:9` / `9:16`)・長さの目安 (既定 60 秒)・型 (`concept` 解説 / `data` 数字 / `compare` 比べる / `story` 物語 / `cinematic` 映像寄り)。聞き返さず既定で進め、決めた値は最後にユーザーへ伝える。
2. **見本 2 本を読む** (NoLang の studio と同じ選び方): `node scripts/pick_samples.mjs --type <型> --aspect <縦横> --request "<依頼文>"` が `reference/samples/` から 2 本を選ぶ: NoLang の src (`<型>_NN.md`・字幕と cut の組み方の手本) 1 本と、hf の写し (`hf_<型>_*.md`・絵と動きの作り込みの手本) 1 本 (同じ題材の見本を外し、同じ向きを先に。同じ向きの NoLang の src が無い型は hf の写しを 2 本)。出た 2 本を全文読む (1 行目の題・`見せる作り:` の要約・design.txt と timeline.txt の全量)。シェルが無い時は同じ規則で自分で選ぶ。骨組み `reference/scaffolds/` は文法の形を確かめる時だけ見る。
3. **決まった素材を使う時だけ**: `SKILL.md` の §M で `ref` を得て、応答の `usage` の位置に書く。
4. **書く** (design system が先・書いた cut から流す):
   - **書く前に構成を決める**: cut の名と中身 (1 cut 1 行) を先に決める。cut は書いた端から投入し、投入した cut は直せないので、書きながら前の cut に戻らない。
   - **根に design system を 1 回決める**: `reference/looks.md` の「style の組」から依頼の気分で 1 つ選び、根に `palette` `font` `fonts` `motion` `transition` と、見出し・本文・札・箱の `def` (= class) を書く。値は題材に合わせる。見本は作り方の手本 (場面の組み方・部品の `def`・動き・語の印の打ち方) — 見本の色・書体をそのまま写さない。
   - 根の中の題材の物: `image 名 = "…"` (基準画像の説明)・`bgm` の説明・`cast` (声の説明を依頼の言語と調子に)・`art` (画風)。`lint off=…` と `# ` の注記は書かない。
   - **cut** は依頼の構成で組み直す: 依頼の流れを cut に分け (60 秒で 5〜8 cut・1 cut に台詞 1〜3 文が目安)、各 cut に見本の場面の型から合う物を当てて組み、文字・台詞・絵の説明を題材で書く。見本の cut の数と順には合わせない。使わない場面と `def` は消す。
   - **子を持つ要素を `.sticky` にしない**: cut を跨ぐ `.sticky` は子の無い要素 (1 枚の札・線・`veil`) だけに付ける。常設の帯・章の札・進行の点灯のように子を持つ物は `def` にして、各 cut に置き直す (今の章の点灯や済みの印は、cut ごとの引数か変種で)。子を持つ `.sticky` は、cut を順に投入する所で止まる (check の `DEFECT:prefix_broken`) か、check を通っても生成の最後で失敗する (`同じ lane の group は floor が同じであること` — engine の不具合で check では拾えない)。見本の多くがこの作りを含むので、写す時に直す (`pick_samples.mjs` が見本ごとに知らせる)。
   - 文字は枠に収まる長さに (見本の文字の長さが目安・長いと check の `shrink_estimate`)。要素の `#名` は cut ごとに付け替え、cut を跨いで同じ名を使わない (根の `.sticky` の物を除く)。
   - 1 cut = design の `section#名` の block + timeline の `*** 名` の block (名は一致させる)。CLI なら作業用の directory (例 `./nolang-videos/<英小文字の名>/`) に `design.txt` と `timeline.txt` として保存する。
   - **書く順**: 根 + 1 つ目の cut を書いたら流し始め (§A の 2・§B)、以後は 1 cut 書き足すごとに投入する。全部を書き終えてから投入しない (再生が始まるまで何分も待たせる)。

## A. CLI で流す

1. **ログイン**: `SKILL.md` の §L。
2. **流し始める** (根と 1 つ目の cut を書いたら): `nolang start <dir> --title "<題>" [--seconds 60]` (縦横は design の `canvas` から) → すぐ `nolang submit <dir>`。DEFECT が返ったら、その cut だけを直して `nolang submit <dir>` し直す (DEFECT は stderr に `DEFECT:コード file:行 原因。直し方: …`・投入済みの cut は直せないので変えない)。
3. **知らせる** (必ず・2 つ目の cut を書く前に): 1 つ目の submit が成功したら、出力の `tell_user` (案内の文 + 次の行に URL) を**そのままユーザーへのメッセージの本文に書く**。数十秒で再生が始まり、続きは投入した端から伸びる。
4. **続きを流す**: 次の cut を design.txt と timeline.txt に書き足して `nolang submit <dir>`。これを cut の数だけ繰り返す。**投入の間は 180 秒以内** (空くとサーバーが生成を失敗にする) — 1 cut を書いたらすぐ submit する。最後の cut は `nolang submit <dir> --end`。
5. **終える**: `--end` の submit が返ったら、出力の `tell_user` (案内の文 + 次の行に URL) を書いて、ターンを終える。完成の確認は頼まれた時だけ (`nolang status <video_id> --wait` → `completed` で「完成しました」と URL・mp4 は `download_url`)。
6. **失敗した時** (submit が `No Video matches`・status が `failed`): その動画は終わり。原稿を見直して (§1 の 4 の規則を破っていないか)、`<dir>/stream.json` を消して start から作り直すのは 1 回まで。それでも `failed` なら止めて、ユーザーに video_id と「check は通ったが生成で失敗した」ことを伝える (サーバー側の問題のことが多い・管理者に伝えてもらう)。**原因を探すために試しの動画を作らない** (cut を減らした版を何本も create するなど — 1 本ごとに GPU と費用を使い、何十分もかかる)。

## B. MCP で作る (シェルが無い時)

### つながっているか

- `nolang_draft_check` などの `nolang_draft_*` ツールが見えれば準備完了 (実際の名前には client ごとの接頭辞が付く)。
- 認証がまだの時:
  - Claude Code: `authenticate` しか見えない → それを呼び、返った URL をユーザーに開いてもらう (NoLang にログインして許可)。ブラウザが `http://localhost:<port>/callback?code=…` で接続エラーになったら、アドレスバーの URL を貼ってもらい `complete_authentication` に渡す。
  - Codex: ユーザーに端末で `codex mcp login nolang-dev` を実行してもらい (ブラウザでログインして許可)、Codex を起動し直してもらう。
- つながらない・ログインできない → (シェルがあれば `nolang doctor` の結果を添えて) ユーザーに伝える。接続先は `https://api-dev.no-lang.com` (API) と `https://dev.no-lang.com` (ログイン)。dev.no-lang.com に会社のネットワークから入れるか、dev のアカウントがあるかを確かめてもらう。

### 手順 (§1 の原稿を、書いた cut から)

1. **開始** (根と 1 つ目の cut を書いたら): `nolang_draft_start(title, aspect_ratio, language="ja", duration_s)` → `video_id` と `watch_url`。`template_video_id` は省略する (空のテンプレ)。生成後にユーザーが編集画面で調整したい動画は `editable=true` — 編集画面で扱える文法サブセットに収めて書く (破った投入は `DEFECT:editable_*` で 400。規則と閾値は `GET drafts/rules/` の `profile` 列と `profiles.editable`・投入前の検査は `nolang_draft_check(profile="editable")`)。
2. **1 つ目を投入**: `nolang_draft_submit_cut(video_id, text)` — text = 根の design + 根の timeline (先頭の `#v2` 行は除く) + 1 つ目の cut の `section#` block + `*** ` block。`defects` が返ったらその cut を直して投入し直す。
3. **知らせる** (必ず・2 つ目の cut を書く前に): 1 つ目が受理されたら、案内の文の次の行に `watch_url` だけを書いてユーザーに渡す (数十秒で再生が始まり、続きは投入した端から伸びる)。
4. **続きを流す**: 次の cut を書いたら `nolang_draft_submit_cut(video_id, text)` — text = その cut の `section#` block + `*** ` block だけ。最後の cut は `end=true`。投入の間は 180 秒以内。
5. **終える**: 最後の cut が受理されたら、もう一度 `watch_url` を単独の行で書いてターンを終える。完成の確認は頼まれた時だけ (`nolang_video_status` の `completed`)。

1 つ目の text の形 (例):

```
#v2
canvas 1280x720 bg=#0B1220
…根の design の残り…
cast narrator = "…"
transition = dissolve,300,overlap=300
section#title
img#t_bg(inset: 0; content: @bg)
h1#t_h(left: 80px; top: 196px; width: 1120px; height: 144px) 見出し
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

## 2. 書き方の要点

あなたは HTML + CSS + GSAP で動画を作る制作者です (scene の DOM を書き、class で見た目を揃え、GSAP の timeline で要素ごとの入場・状態変化・退場を打つ、いつもの作り方)。
draft src はその動画の圧縮形で、書く物は同じです。圧縮の規則は 4 つだけ:

1. **閉じタグは字下げ**。1 行 1 要素 `tag#id.class(css 宣言) 内容`。字下げ 2 空白 = 子。
2. **style は要素の行**。`(…)` の中に CSS の宣言をそのまま (`left:48px; top:120px; font-size:32px; color:#fff; border:3px solid $a; box-shadow:0 0 24px $a`)。共通の見た目は `def` (= class) に 1 回・型ごとの既定は `tag { 宣言 }` (= CSS の要素の rule)。
3. **gsap.from / to は object のまま**。入場 `in:{y:30, opacity:0, duration:.5, ease:'power3.out'}`、退場 `out:{…}`、状態の変化 `to,{scale:1.1, duration:.4}`。秒は GSAP の秒。
4. **時刻は秒ではなく台詞の語**。timeline.txt は台本で、tween はその語の前に置く: `[>#id]` 出す・`[!#id to,{…}]` 変える・`[<#id]` 消す。`tl.to(el, {…}, 2.3)` の 2.3 を書く場所は無く、声の実尺が時刻を決める。

```
#v2
canvas 1280x720 bg=#0A0614
palette a=#FF2D55 mute=#9A93B5
section#hook
div#c1(left:48px; top:420px; width:300px; padding:16px; border-radius:16px; background:#0a0614e6; border:3px solid $a; box-shadow:0 0 24px $a; in:{y:60, scale:.7, opacity:0, duration:.5, ease:'back.out(1.7)'})
  p#l(font-size:22px; color:$mute; letter-spacing:.2em) STAGE A
  p#t(font-size:72px; color:#fff; text-shadow:0 0 24px $a) 18:30
img#venue(inset: 0; main: kb {scale: [1, 1.06]}) 夜の野外フェス会場、遠くに二つのステージ、青と赤のネオン、人物なし
```

```
#v2
cast n = "落ち着いた30代女性のナレーター"
*** hook
[>#subtitle]
@n: 推しと推しが、[>#c1]同じ[!#c1 to,{scale:1.08, duration:.25} +300][!#c1 to,{scale:1, duration:.4, ease:'back.out'} >]時間。[<#c1 +600]
```


tag は HTML の別名 (`div p h1〜h4 span img svg`) か NoLang の型 (`icon shape veil group link backdrop progress …`) か自分の `def` の名。札の行・横棒・流れ図などの組み込みの部品は無く、`def` + `×N` で書く (authoring.md「根の雛形」)。
`#id` が名 (字下げの子は相対名・印では `#親.子`)、`.class` は flag (`.hug` 中身の幅・`.sticky` cut を跨ぐ) か変種の tag (全面は宣言 `inset: 0`)、文字の内容は行の残り。
CSS にあって engine に無い宣言 (`clip-path` `backdrop-filter` `transition` `transform:translate` … 表 `surface_table` の model の行) は落として check が warn で知らせる (止まらない)。表に無い名の宣言は DEFECT:KEY。`canvas 1920x1080` など短辺 720 以外の canvas は px ごと 720 に写す。根の `run` に無い `{class}` は素の文字 (note で知らせる)・def の渡さない引数は空。

素材は説明文で書く: 話者 `cast n = "落ち着いた30代女性のナレーター" speed=110%`・BGM `bgm#m 静かなピアノと弦`・絵 `img#p(inset: 0) 夜の屋台の湯気、文字なし` (`alt` と同じ)・書体 `font "太い明朝体"`・効果音 `[♪"グラスに注ぐ音" -6dB]`。名や id で指定しない (例外は依頼に決まった素材がある時だけ — `SKILL.md` の §M)。
依頼がキャラ (ずんだもん等) を名指ししたら、声は `cast z = character="ずんだもん"` (例外的に名で書く) で、画面にも立ち絵を出す: 最初の cut に `avatar#lay.sticky(left:900px; top:200px; width:360px; height:520px; cast:z; object-fit:contain)` (`.sticky` で cut を跨いで出続ける)・文字や図は立ち絵の場所を空けて置く・表情は台詞に `[!#lay expression,happy]`。
読みは src の責務でない (後段の読み検査が差し替える)。全出現を強制する語だけ根に `read 3日 = みっか`、その場だけ `{3日|みっか}`。

### 違い (CSS / GSAP に無い物・5 つ)

1. **時刻は語**: 印 `[動詞 #名 やり方 拍]` を台詞の語の直前に。動詞は `>` 出す・`!` 変える・`<` 消す・`=` 戻す。拍は `+300` / `-300` (語から ms)・`>` (直前の印の終わり)・`cut-400` (cut 末の 400 ms 前・`<` だけ)。cut 末の印だけの行 `[<#名]` は cut 末の拍。同じ語の印は同時。印の無い要素: 絵・箱・図形は cut 頭、文字と ×N は `cut { stagger: sentence }` (雛形にある) で 1 つ目が頭・2 つ目から文ごと。
2. **scene = cut**: 退場は cut 境界で終わる (退場を次の cut の入りに重ねるのは混ぜない切替 `transition none,370` = 次の cut は退場が終わる 370 ms 前に始まる・旧場面ごと残すのは `overlap=`・最後の cut は退場せず最後の frame まで残る — `fade out` は頼まれた時だけ)。cut の切替は timeline の前の cut の最後の行に `transition dissolve,400` (`wipe,700,dir=left` `slide,260` `dip,400`・境目の音は `,se="…"`)。cut を跨ぐ要素は `.sticky`。
3. **尺は TTS**: 依頼の長さは目安。合わせるために話速・無音・台詞を変えない。`@n: 文[印]文…` (2 行目から `@: …`)・`[silence:0.6s]`・`{表記|読み}`・`[br]`。話し方は cast の `manner=` が基本 (台詞ごとの `[manner:…]` は Fish Audio の声だけに効き、他の声では無視されて cast の `manner=` で読む)。
4. **素材は説明文**: 絵は `img#名 説明` (根の `image 名 = "…"` を `[ref:@名]説明` で基準画像に — 同じ料理・場所・物・人物を 2 枚以上の絵に描くなら、中身を具体に書いた基準画像を 1 枚置いて各絵を派生させるとよい。別々に注文すると絵ごとに別物になる: 和風パスタが途中でクリームに・碓氷峠に富士山)、声は `cast`、BGM は `bgm#名 説明` (音量は engine の既定 = hf の大きさ・`volume:` は書かない)、効果音は語に `[♪"説明" -6dB]`・cut 頭の場の音 `se "…" -8dB to=尺 fade=300,1500`、書体は `font "説明"` / `fonts m="説明"` (`font-family: m`)。根の `art` は画風 (筆致・質感・色調) だけ — 時間帯・天気・光は絵ごとの説明に (art の「夜」と絵の「真昼」がぶつかると上下 2 枚の絵になる)。palette の強調色 `a` は絵の主な色と変える (同じ系統だと絵の上の `a` の字が沈む)。
5. **出す前に触れない**: 出ていない要素への `!` `<` `=` は DEFECT:NOT_OPEN。`>` は要素ごとに 1 回。出した語と同じ拍の `to` は出た 1 frame 後から移る (出た見た目を変えるなら `[>#名 .tag]`)。

### 書き方の対応 (迷った時だけ)

- 位置: 絶対 `left top width height` (中心 `cx cy`・全面 `inset: 0`)、子は親の内側から。`x y` は GSAP の移動量 (`in: {x: -40}`・`to,{y: 20}`) だけ。flex は `display:flex; gap:24px` (`flex-direction:column` で縦)、`display:grid` で 2×2。重なりは書いた順 (後が上)・`z-index:front`・意図の重なり `overlap:相手`。
- 繰り返し: `div#c(…) ×3` + 子 `  p#t(…) a;b;c` (`;` で instance ごと) → `#c[1]` `#c[1].t` `#c[*]`・出る間隔は入場の tween の中 `div#c(in: {y:20, opacity:0, stagger: {each: .12, from: 'end'}}) ×3` か印 `[>#c[*] {stagger:{each:0.04, from:'center'}}]` (stagger は tween の object の中だけ — 1 つの文字なら 1 字ずつ)。一括の変化は `[!#c[*] to,{…, stagger:.08}]`・主役の切替は `[!#c[2] focus]` (`stagger: dim` で薄く先出し)。
- 変種: `#名.tag(宣言)` (静止の別の姿) → `[!#名 .tag]` (補間して移る。`points=` / `path=` の shape の変種は形ごと補間 = morph。書体 / style・画像・fit の種類・形の種類・blend・mask が違う変種は補間せず、その語で開き直す — 変種の `in=` が入場・無ければ切替)。部品: `def 名(引数) = tag(宣言) {引数}` → `名#x(…) 文字` (同じ形の 2 つ目も def に上げて実体を並べる)。
- 文字の一部: `{t}語{/}` + `[!#名{t} recolor,$a]` / `highlight` / `marker` / `strike` (`[=#名{t}]` で戻す)。
- 糖衣: 入場の名 `in: rise` (`fade rise drop slide zoom pop wipe` — 量と向きは config: `slide {x: -30}` = 左から・`wipe {dir: 'right'}` + studio の `spring settle bounce flash mask_rise swing_in travel punch typewriter fade_stagger blur pixelate circle_wipe iris_wipe clock_wipe spin_zoom zoom_reverse draw drift ping`)・役 `title big div row note` (雛形の根の `motion 名 { in: …; out: … }` 5 行)。property・ease・ms が固定なので、同じ名を繰り返すと動きが揃って見える — 急ぐ時と役の既定にだけ。
- 常時 `main: float|breathe|sway|pulse`・`spin {period: 9}`・`kb {scale: [1.1, 1], focus: '40% 60%'}` (寄りながら動くなら `focus: ['40% 60%', '60% 50%']`)。2 本以上の tween は `,` で並べる (`in: fade {duration: .8}, typewriter {level: 3}`)。同じ tween を関数に `cue 名(x) = [!#x punch][!#x check >]` → 台詞に `[名 #対象]`。
- 字幕: 印だけの行 `[>#subtitle]` で以後の台詞が自動の字幕 (cut を跨いで続く・閉じるのは `[<#subtitle]` — cut 末の印だけの行ならその cut の終わり)。`subtitle(font-size:32px; …)`・テロップの間だけ消す `.hide_subtitle`。話者札は `cast a = "…" label="部下" label_fill=$a`。

### 書けない物 (runtime に無い・GSAP と違う例外)

- 文字・図形への `filter` (彩度・色行列)・`to` の motion blur・画像の radial mask・chroma key・音のピッチ変更は無い。`mix-blend-mode` は `multiply screen add overlay soft-light` だけ。
- 文字の一部 (run) の拡大を保つ・run への glow・layer 単位の glow / tint・子ごと傾く要素 (子を持つ要素の skew・3D・filter・blend・glow は DEFECT — 入退場の blur は子ごと掛かる)・語を囲む手描きの丸 (rough-notation) は無い (代用は `reference/capabilities.md` 末尾)。
- `yoyo` の `repeat` は奇数 (偶数は頂点で終わり跳ねる)。1 層に `in` は 1 つ。強調中の文字の一部に別の強調は重ねない。係数つきの ease は `back.out(1.7)` だけで、効くのは `in` / `out` / `main` (`to` では係数を落として warn)。`elastic` / `bounce` / `circ` に係数は無い (`elastic.out(1,0.5)` は DEFECT — `elastic.out`)。
- 繰り返す tween (`repeat`) に書けるのは `x y scale rotation opacity`。

## 3. 辞書 (詰まった時だけ引く)

- `reference/authoring.md` 文法の辞書。大きいので節ごとに読む: `grep -n '^##' reference/authoring.md` で見出しの行番号を出し、Read の `offset` / `limit` で読む。節は HTML 形 · 字句 · design.txt (型・位置・動き・×N と def と根の雛形・字幕と cut) · timeline.txt (印・時刻の規則・cue と切替) · 欠陥 · HTML の動画を写すとき。key の名は v2 の綴り (`size` `fill` `radius` `shadow` …) で載っているが、CSS の名 (`font-size` `background` `border-radius` `box-shadow` …) でそのまま書ける。
- `reference/rules.md` check の `findings` の規則名と直し方。
- `reference/looks.md` 見た目の作り方 / `reference/sounds.md` 音 / `reference/capabilities.md` できる表現と代用。
- `reference/samples/` 型ごとの見本 (`<型>_NN.md` は NoLang の src・`hf_*` は絵と動きの作り込みの見本・§1 の 2 で 1 本ずつ選ぶ)。

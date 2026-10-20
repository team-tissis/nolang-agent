---
name: make-video
description: 社内 dev の NoLang (dev.no-lang.com) で動画を 1 本作る。「〇〇の動画を作って」「動画にして解説して」など、NoLang で動画を作る依頼の時に使う (手元の写真・動画や、決まった曲・声を使う依頼も)。「NoLang にログインして」・NoLang の素材を探す / 送る依頼にも使う。台本と画面 (draft src) を書き、CLI (nolang) か MCP (nolang-dev) で投入すると、NoLang のサーバーが声・素材・描画を担当する。
---

# NoLang の動画を作る (nolang-dev)

あなたが台本と画面 (draft src = `design.txt` と `timeline.txt`) を書き、NoLang のサーバーが声・絵・BGM・描画を担当する。手元に GPU も NoLang の repo も要らない。
この file のパスはすべてこの skill の directory からの相対。

## 0. CLI か MCP か

- **シェルが使え、`node` (20 以上) があれば CLI** (§A)。原稿を file のまま渡せ、check → 開始 → cut の分割 → 順番の投入を `nolang create` が 1 回でやる (並列の投入・待ち時間切れの失敗が起きない)。
- **シェルが無い (Web 版など)・CLI が動かない時は MCP** (§B)。
- 原稿の書き方 (§1・§2) はどちらも同じ。

CLI の呼び方: `nolang` が PATH にあればそれ、無ければ `node ../../cli/nolang.mjs` (この skill の directory から。以下 `nolang` と書く)。
結果は stdout に JSON・途中経過は stderr。終了コード 0 成功 / 1 原稿の欠陥・生成の失敗 / 2 使い方 / 3 未ログイン / 4 接続。

## 1. 原稿を書く (CLI・MCP 共通・この順で・寄り道しない)

1. **依頼から決める**: 伝えること 1 文・縦横 (`16:9` / `9:16`)・長さの目安 (既定 60 秒)・型 (`concept` 解説 / `data` 数字 / `compare` 比べる / `story` 物語 / `cinematic` 映像寄り)。聞き返さず既定で進め、決めた値は最後にユーザーへ伝える。
2. **骨組みを読む**: `reference/scaffolds/<型>_<16x9|9x16>/design.txt` と `timeline.txt`。動く完成例は `examples/explainer_16x9/` (7 cut・check 通過・描画済み)。最初の 1 本はこの 2 つで足りる。
3. **決まった素材を使う時だけ** (依頼に「この写真・この動画」「この曲」「この声」がある・手元の file を渡された):
   - 手元の file → `nolang assets upload <file>…` で自分の素材に送り、`ref` (`id=<uuid>`) を得る (動画は仕上げを待つので数十秒)。MCP は file の中身を運べないので、upload は CLI で。
   - NoLang の素材から選ぶ → `nolang assets search <kind> "<説明か名前>"` (MCP なら `nolang_assets_search(kind, q)`)。自分が送った物は `--mine` (`scope="mine"`)。kind = `image` `footage` `bgm` `soundeffect` `speaker` `avatar` `font`。`preview_url` で中身を確かめられる。
   - `ref` は応答の `usage` の位置に書く: 画像・動画素材 = 根に `image 名 = id=…`、置く所に `content: @名` (動画素材は `play: loop` も)・BGM = `bgm#名 id=…`・効果音 = `sound 名 = id=…` か台詞に `[♪id=…]`・話者 = `cast 名 = id=…`・立ち絵 = `cast 名 = "声の説明" avatar="名"`・書体 = `font "名 太さ"`。
   - id は全桁の `id=<uuid>` だけ (8 桁の id と `file=名` はこの経路では使えない)。読めない id は check が `DEFECT:ASSET_UNREADABLE` で止める。
   - 決まった素材が無い所は説明文で書く (絵は生成、声・BGM・効果音・書体は説明文でカタログから選ばれる)。
4. **書く**: 骨組みの根 (先頭から最初の `section#` の前まで) は配色と書体を題材に合わせる程度でほぼそのまま使い、cut を題材で書き直す。1 cut = design の `section#名` の block + timeline の `*** 名` の block (名は一致させる)。cut は 5〜8 個、1 cut に台詞 1〜3 文。`# TODO` の注記行は消す。CLI なら作業用の directory (例 `./nolang-videos/<英小文字の名>/`) に `design.txt` と `timeline.txt` として保存する。

## A. CLI で作る (シェルがある時・推奨)

1. **ログイン** (「NoLang にログインして」と頼まれた時も、作る前も): `nolang auth status`。終了コード 0 ならログイン済み。3 (未ログイン) なら、自分で始める:
   - `nolang auth login --background` → 出力の `authorize_url` をユーザーに渡し、「ブラウザで NoLang にログインして『許可』を押してください」と伝える (同じ機械ならブラウザも開く)。コマンドはすぐ戻り、待ち受けは裏で続く。
   - ユーザーが許可したら `nolang auth wait` (最大 120 秒・終了コード 0 で完了)。まだ (終了コード 3・`"waiting": true`) ならもう一度 `nolang auth wait`。待ち受けは 5 分で切れるので、切れたら `--background` からやり直す。
   - ブラウザに `ACCESS DENIED` (403) と出る → 接続元の IP が NoLang の許可リストに無い。同じブラウザで `https://<ログイン画面のホスト>/cdn-cgi/trace` を開き、`ip=` の値を管理者に伝えてもらう。
   - ブラウザが別の機械 (リモート・コンテナ) なら: `nolang auth login --no-browser` → 出た `authorize_url` をユーザーに開いてもらう → 許可後のページは接続エラーになるので、そのアドレスバーの URL を貼ってもらう → `nolang auth complete '<URL>'`。
   - 終了コード 4 (つながらない) → `nolang doctor` の結果をユーザーに伝える (README.md の「つなぐ先の準備」)。
2. **check**: `nolang check <dir>` を DEFECT 0 まで。DEFECT は stderr に `DEFECT:コード file:行 原因。直し方: …`。`findings` は `reference/rules.md` を見て直せる物は直す。
3. **作る**: `nolang create <dir> --title "<題>" [--seconds 60]` (縦横は design の `canvas` から自動)。stdout の JSON の `watch_url` をすぐユーザーに渡す (生成中から再生できる)。投入される text を先に見るなら `--dry-run`。
4. **完成を待つ** (頼まれた時・動画の file が要る時): `nolang status <video_id> --wait` → `completed` で `download_url` (mp4)。`failed` なら原稿ではなくサーバー側の問題のことが多いので、管理者に伝える。

## B. MCP で作る (シェルが無い時)

### つながっているか

- `nolang_draft_check` などの `nolang_draft_*` ツールが見えれば準備完了 (実際の名前には client ごとの接頭辞が付く)。
- 認証がまだの時:
  - Claude Code: `authenticate` しか見えない → それを呼び、返った URL をユーザーに開いてもらう (NoLang にログインして許可)。ブラウザが `http://localhost:<port>/callback?code=…` で接続エラーになったら、アドレスバーの URL を貼ってもらい `complete_authentication` に渡す。
  - Codex: ユーザーに端末で `codex mcp login nolang-dev` を実行してもらい (ブラウザでログインして許可)、Codex を起動し直してもらう。
- つながらない・ログインできない → (シェルがあれば `nolang doctor` の結果を添えて) ユーザーに伝える。接続先は `https://api-dev.no-lang.com` (API) と `https://dev.no-lang.com` (ログイン)。dev.no-lang.com に会社のネットワークから入れるか、dev のアカウントがあるかを確かめてもらう。

### 手順 (§1 で書いた原稿を)

1. **check**: `nolang_draft_check(design, timeline)` を `defects` が空になるまで (数秒で返る)。`findings` は `reference/rules.md` を見て直せる物は直す。
2. **開始**: `nolang_draft_start(title, aspect_ratio, language="ja", duration_s)` → `video_id` と `watch_url`。`template_video_id` は省略してよい (空のテンプレ)。
3. **cut を 1 つずつ順番に投入**: `nolang_draft_submit_cut(video_id, text)`
   - 1 つ目の text = 根の design + 根の timeline (先頭の `#v2` 行は除く) + 1 つ目の cut の `section#` block + `*** ` block
   - 2 つ目以降の text = その cut の `section#` block + `*** ` block だけ
   - 最後の cut は `end=true`
4. **渡す**: 1 つ目が受理されたら `watch_url` をユーザーに渡す (生成中から追いかけ再生できる)。`nolang_video_status` の `playable` が true なら再生でき、`completed` で完成。

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
- start の後、投入の間が 180 秒空くとサーバーが生成を失敗にする → 全 cut を書いて check を通してから start する。
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

素材は説明文で書く: 話者 `cast n = "落ち着いた30代女性のナレーター" speed=110%`・BGM `bgm#m 静かなピアノと弦`・絵 `img#p(inset: 0) 夜の屋台の湯気、文字なし` (`alt` と同じ)・書体 `font "太い明朝体"`・効果音 `[♪"グラスに注ぐ音" -6dB]`。名や id で指定しない (例外は依頼に決まった素材がある時だけ — §1 の 3)。
依頼がキャラ (ずんだもん等) を名指ししたら、声は `cast z = character="ずんだもん"` (例外的に名で書く) で、画面にも立ち絵を出す: 最初の cut に `avatar#lay.sticky(left:900px; top:200px; width:360px; height:520px; cast:z; fit:contain)` (`.sticky` で cut を跨いで出続ける)・文字や図は立ち絵の場所を空けて置く・表情は台詞に `[!#lay expression,happy]`。
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
- 糖衣: 入場の名 `in: rise` (`fade rise drop slide zoom pop wipe` — 量と向きは config: `slide {x: -30}` = 左から・`wipe {dir: 'right'}` + studio の `spring settle bounce flash mask_rise swing_in travel punch typewriter fade_stagger blur pixelate circle_wipe iris_wipe clock_wipe spin_zoom zoom_reverse draw drift ping`)・役 `title big div row note` (雛形の根の `motion 名 = …` 5 行)。property・ease・ms が固定なので、同じ名を繰り返すと動きが揃って見える — 急ぐ時と役の既定にだけ。
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
- `reference/samples/` 型ごとの見本 (評価の高かった src)。`hf_*` は作りの質が高い見本。

---
name: nolang-draft-studio
description: NoLang の動画を draft src (HTML / CSS / GSAP の圧縮形) で 0 から書き、check と render で仕上げる。
---

# NoLang Draft Studio

あなたは HTML + CSS + GSAP で動画を作る制作者です (scene の DOM を書き、class で見た目を揃え、GSAP の timeline で要素ごとの入場・状態変化・退場を打つ、いつもの作り方)。
draft src はその動画の圧縮形で、書く物は同じです。圧縮の規則は 4 つだけ:

1. **閉じタグは字下げ**。1 行 1 要素 `tag#id.class(css 宣言) 内容`。字下げ 2 空白 = 子。
2. **style は要素の行**。`(…)` の中に CSS の宣言をそのまま (`left:72px; top:180px; font-size:48px; color:#fff; border:4px solid $a; box-shadow:0 0 36px $a`)。共通の見た目は `def` (= class) に 1 回・型ごとの既定は `tag { 宣言 }` (= CSS の要素の rule)。`#id { }` `.c { }` `::after` の rule は書かない (要素の行・def・字下げの子)。
   font-size も CSS と同じ (書かない文字は親の値を継ぎ、根は 16px・`em` は親の比・`h1` は 2em)。箱 (div / group) の `font-family` `color` `letter-spacing` `white-space` も子の文字が継ぐ。hf と同じく字の要素に必ず書く — 目安 (1080): 字幕 40〜48 (縦 50〜60)・本文 34〜44・札 24〜30 (下限 26)・見出し 52〜84・hero / 数 100〜180・縦は ×1.3。
3. **gsap.from / to は object のまま**。入場 `in:{y:45, opacity:0, duration:.5, ease:'power3.out'}`、退場 `out:{…}`、状態の変化 `to,{scale:1.1, duration:.4}`。秒は GSAP の秒。duration を書かない object は GSAP と同じ 0.5 秒・語だけの preset (`in: fade`) は語ごとの既定。
4. **時刻は秒ではなく台詞の語**。timeline.txt は台本で、tween はその語の前に置く: `[>#id]` 出す・`[!#id to,{…}]` 変える・`[<#id]` 消す。`tl.to(el, {…}, 2.3)` の 2.3 を書く場所は無く、声の実尺が時刻を決める。

```
#v2
canvas 1920x1080 bg=#0A0614
palette a=#FF2D55 mute=#9A93B5
section#hook
div#c1(left:72px; top:630px; width:450px; padding:24px; border-radius:24px; background:#0a0614e6; border:4px solid $a; box-shadow:0 0 36px $a; in:{y:90, scale:.7, opacity:0, duration:.5, ease:'back.out(1.7)'})
  p#l(font-size:33px; color:$mute; letter-spacing:.2em) STAGE A
  p#t(font-size:108px; color:#fff; text-shadow:0 0 36px $a) 18:30
img#venue(inset: 0; main: kb {scale: [1, 1.06]}) 夜の野外フェス会場、遠くに二つのステージ、青と赤のネオン、人物なし
```

```
#v2
cast n = "落ち着いた30代女性のナレーター"
*** hook
[>#subtitle]
@n: 推しと推しが、[>#c1]同じ[!#c1 to,{scale:1.08, duration:.25} +300][!#c1 to,{scale:1, duration:.4, ease:'back.out'} >]時間。[<#c1 +600]
```

台本 (timeline.txt) と画面 (design.txt) を書き、check で欠陥と尺と配置を検査し、render で 1 回だけ描く。
tag は HTML の別名 (`div p h1〜h4 span img svg`) か NoLang の型 (`icon shape veil group link backdrop progress …`) か自分の `def` の名。札の行・横棒・流れ図などの組み込みの部品は無く、`def` + `×N` で書く (authoring.md「根の雛形」)。`svg` は 1 枚の絵に焼く — 本文の中の `id` は印の的にならない (動かす部品は字下げの svg の子・線を描くなら `shape` の `in: draw`)。`div` は CSS と同じ素の箱 (地・縁・角丸・影・余白は書いた物だけ) — 板は宣言で書く: `div#c(…; background: $panel; border: 2px solid $line; border-radius: 24px; box-shadow: 0 6px 18px #0003; padding: 36px)` (繰り返すなら `def card = div(…)`)。`border-radius: 50%` 以上は楕円 (CSS どおり)・pill は `999px`。
`#id` が名 (字下げの子は相対名・印では `#親.子`)、`.class` は flag (`.hug` 中身の幅・`.sticky` cut を跨ぐ) か変種の tag (全面は宣言 `inset: 0`)、文字の内容は行の残り。
CSS にあって engine に無い宣言 (`clip-path` `backdrop-filter` `transition` `display:none` … 表 `surface_table` の model の行) は落として check が warn で知らせる (止まらない)。`transform` は書いた関数の順に合成し、layout の位置と寸法を保ったまま描画時に適用する。`translate()` の `%` は自身の箱の寸法を基準にする (寸法の決まらない文字・% の箱は `left` / `top` に続く先頭の `translate(-50%, -50%)` だけを中央寄せとして読み、他は DEFECT)。`border` の線種は `solid` `dashed` `dotted` (破線 / 点線は Chromium と同じ模様・`double` などは DEFECT:CSS)。表に無い名の宣言は DEFECT:KEY。canvas の短辺は 1080 (`canvas 1920x1080` / `1080x1920` / `1080x1080`・px はそのまま layout の px) — 他の短辺は DEFECT:ARG。根の `run` に無い `{class}` は素の文字 (note で知らせる)・def の渡さない引数は空。

```bash
S=.agents/skills/nolang-draft-studio/scripts/studio.py; P="env PYTHONPATH=$PWD /opt/venv/bin/python"   # repo root から
$P .agents/skills/nolang-draft-studio/scripts/studio_server.py start   # 常駐 server (stop / status)・`export STUDIO_SERVER_SOCK=$PWD/tmp/studio/.server/sock`
$P $S new    tmp/studio/<name> --type data|concept|compare|story|cinematic [--aspect 9:16] [--seconds 90]   # 雛形 (根 + cut の TODO・target_s は目安)
$P $S check  tmp/studio/<name>            # 5〜10 秒: DEFECT (file:行・原因・直し方)・尺・配置・出る時刻・lint。通ると裏で素材と TTS を作る
$P $S render tmp/studio/<name>            # 1〜2 分: out/video.mp4 + render_frames/ + render_report.md (実時刻の frame 一覧・音量)
$P $S icons  lock shield                  # icon の名を探す (Phosphor 1,512 種)
$P $S speech tmp/studio/<name> 録音.mp3 [--speakers 2] [--language ja]   # 入力音声の intake (登録 + 転写 + clip 台帳 clips.json + pin)
```

project = `timeline.txt` / `design.txt` / `src.json` (`new` が書く・素材の pin は check が書く) / `out/`。両 file の 1 行目は `#v2`。
素材は説明文で書く: 話者 `cast n = "落ち着いた30代女性のナレーター" speed=110%`・BGM `bgm#m 静かなピアノと弦`・絵 `img#p(inset: 0) 夜の屋台の湯気、文字なし` (`alt` と同じ)・書体 `font "太い明朝体"`・効果音 `[♪"グラスに注ぐ音" -6dB]`。名や id で指定しない。
依頼がキャラ (ずんだもん等) を名指ししたら、声は `cast z = character="ずんだもん"` (例外的に名で書く) で、画面にも立ち絵を出す: 最初の cut に `avatar#lay.sticky(left:1350px; top:300px; width:540px; height:780px; cast:z; object-fit:contain)` (`.sticky` で cut を跨いで出続ける)・文字や図は立ち絵の場所を空けて置く・表情は台詞に `[!#lay expression,happy]`。
入力音声 (持ち込みの録音) は `speech` の後、`cast 名 = @clip clip-s0` と `@clip clip-s0-0001 原文` (原文は台帳の文をそのまま続ける — 角括弧で囲まない・省略も可) で台詞にする (台帳は clips.json の `ledger`・原文の無い行 `(発話なし 6.9s)` と行末の `(語の後 3.0s 発話なし)` 等は転写に出ない音 = イントロ・間奏・待ち時間・笑いの区間 — 原文の無い行は `@clip id` で残すか書かずに落とす)。文中の不要部分は `[trim:飛ばす原文]` で声ごと切る (フィラー・言い直し。中は台帳の原文をそのまま写す — 外れは DEFECT (`trim_miss`・check と投入の門が止める)。間を置くなら隣に `[silence:200ms]`)。clip と clip の間は行頭 / 行末の `[silence:N]` か根の `silence head= tail=` (端の無音の長さ・書かなければ素材の間を詰めて繋ぐ)。
読みは src の責務でない (後段の読み検査が差し替える)。全出現を強制する語だけ根に `read 3日 = みっか`、その場だけ `{3日|みっか}`。

## 前提 (環境)

- 製品を local で動かす dev container と同じ物: `/opt/venv` の python・Django と LOCAL DB (`.env`)・資材カタログ (書体・話者・BGM・効果音・立ち絵) を `manage.py seed` で入れた状態。
- resource-service (svg / html の描画・別 repo `nolang-resource-service`・`PORT=9500 npx tsx bin/server.ts`・到達先は `RESOURCE_SERVICE_URL` か localhost:9500)。落ちていると render が 1 行の案内で止まる。
- gpulibs の native build (`docker_setup/build_gpulibs.sh`)。render の encoder と HLS は CUDA を使うので GPU が要る (check は GPU なし)。
- worktree で回すなら `.env`・`static/credentials`・`build_gpulibs` を main checkout から symlink。skill を Claude Code に見せるのは `make link-skills` (clone / worktree ごと)。
- 常駐 server (`studio_server.py start`) は任意。無ければ各 command が自分で Django を起動する (1 回 7 秒ほど遅い)。
- stream (下) は著者と担当を `claude -p` で呼ぶので、その機械で claude CLI に login している事 (subscription の枠で動く・1 本 $0.7〜2.7 相当)。環境の `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` は login より優先されるので著者は外して呼ぶ (外さないと 0 token の応答で `author exit 1`・`cut 0`・理由は `stream/claude_author.err`)。

## 工程 (project の状態から入る)

- `brief.md` が無い → 依頼文を読んで brief を書く (書式は `reference/formats.md` §brief)。依頼に台本があれば brief に写し、以後そのまま使う。
- `storyboard.md` が無い → brief から storyboard を書く (§storyboard)。frame = cut。frame ごとに「画面のいちばん見える瞬間」「台詞」「語に結ぶ変化」「尺」を決める。この段では文法を書かない。
- `studio/` が無い → `reference/samples/` の自分の type の見本 2 本 (NoLang の勝ち src 1 本 + hf の作りを写した `hf_*` 1 本) を読む → `new` で骨組みを作る → **design system を根に 1 回** (`palette` `font` `fonts` `motion` `art` と、見出し・本文・札・箱 (札の行・横棒・流れ図の札) の `def` = class) → storyboard の frame を 1 つずつ `section#名` と `*** 名` に写す (§build)。
- `out/video.mp4` が無い → `check` を DEFECT 0・severe 0 まで (warn は読んで直せる物は直す) → `render` 1 回。
- 全部ある → 報告 (§report)。render の後に frame を見て直す往復はしない。

## 工程の規則

- **brief が正**: message 1 文・audience・arc・format・look の語 3 つ・voice・must / avoid。以後の判断は brief に戻って決める。
- **storyboard は構造の設計で、見た目の設計ではない**: 各 frame に「この frame で分かること」が 1 つ。frame の尺は台詞の長さから出る (4〜25 秒)。
- **design system が先**: hf と同じく、色・書体・文字の段・札と箱の class を根に決めてから frame を書く。frame の要素は class を当てて差分だけ書く。
- **build は frame 単位**: 1 frame = `section#名` の design + `*** 名` の台詞。frame の「いちばん見える瞬間」を design に書き (要素は全部出た時の位置と大きさ・絶対配置でよい)、入場はそこへ来る道・語の印はその瞬間の変化。
- **review は check の出力で**: 「出る時刻」の表で frame ごとに、見出し → 本文 → 変化 の順が台詞と合っているかを読む (変化 = 書いた印の全部・既定 = engine が足した動き)。render 後の frame は報告にだけ使う。

## 違い (CSS / GSAP に無い物・5 つ)

1. **時刻は語**: 印 `[動詞 #名 やり方 拍]` を台詞の語の直前に (的は `#a,#b,#c` と並べられる = 的ごとの同じ印)。動詞は `>` 出す・`!` 変える・`<` 消す・`=` 戻す。拍は `+300` / `-300` (語から ms)・`>` (直前の印の終わり)・`cut-400` (cut 末の 400 ms 前・`<` だけ)。cut 末の印だけの行 `[<#名]` は cut 末の拍。同じ語の印は同時。印の無い要素: 絵・箱・図形は cut 頭、文字と ×N は `cut { stagger: sentence }` (雛形にある) で 1 つ目が頭・2 つ目から文ごと (印の無い題 `h1` / `chap` は前の kick・番号の札と一緒に頭 — 題を後の文に出すなら印を書く)。
2. **scene = cut**: 退場は cut 境界で終わる (退場を次の cut の入りに重ねるのは混ぜない切替 `transition none,370` = 次の cut は退場が終わる 370 ms 前に始まる・旧場面ごと残すのは `overlap=`・最後の cut は退場せず最後の frame まで残る — `fade out` は頼まれた時だけ・全面の不透明な板 (`transition flash` / `dip` の板・不透明な全面の単色板) の下で閉じる層の out は engine が外す (見えない退場は描かない))。cut の切替は timeline の前の cut の最後の行に `transition dissolve,400` (`wipe,700,dir=left` `slide,260` `dip,400`・境目の音は `,se="…"`)。cut を跨ぐ要素は `.sticky`。
3. **尺は TTS**: 依頼の長さは目安。合わせるために話速・無音・台詞を変えない。`@n: 文[印]文…` (2 行目から `@: …`)・`[silence:0.6s]`・`{表記|読み}`・`[br]`。話し方は cast の `manner=` が基本 (台詞ごとの `[manner:…]` は Fish Audio の声だけに効き、他の声では無視されて cast の `manner=` で読む)。
4. **素材は説明文**: 絵は `img#名 説明` (根の `image 名 = "…"` を `[ref:@名]説明` で基準画像に — `content: @名` は基準画像をそのまま出す宣言で、説明と両方は書かない — 同じ料理・場所・物・部品・人物を 2 枚以上の絵に描くなら、中身を具体に書いた基準画像を根に 1 枚置き、各絵は `[ref:@名]` で派生させる。別々に注文すると絵ごとに別物になる: 和風パスタが途中でクリームに・碓氷峠に富士山・CAD の点群とメッシュで同じ部品の形が違う)、声は `cast`、BGM は `bgm#名 説明` (音量は engine の既定 = hf の大きさ・`volume:` は書かない)、効果音は語に `[♪"説明" -6dB]`・cut 頭の場の音 `se "…" -8dB to=尺 fade=300,1500` (timeline の `*** 名` の下の行)、書体は `font "説明"` / `fonts m="説明"` (`font-family: m`)。根の `art` は画風 (筆致・質感・色調) だけ — 時間帯・天気・光は絵ごとの説明に (art の「夜」と絵の「真昼」がぶつかると上下 2 枚の絵になる)。palette の強調色 `a` は絵の主な色と変える (同じ系統だと絵の上の `a` の字が沈む)。
5. **出す前に触れない**: 出ていない要素への `!` `<` `=` は DEFECT:NOT_OPEN。`>` は要素ごとに 1 回。出した語と同じ拍の `to` は出た 1 frame 後から移る (出た見た目を変えるなら `[>#名 .tag]`)。

## 書き方の対応 (迷った時だけ)

- 位置: 絶対 `left top width height` (中心 `cx cy`・全面 `inset: 0`)、子は親の内側から。`x y` は GSAP の移動量 (`in: {x: -60}`・`to,{y: 30}`) だけ。flex は `display:flex; gap:36px` (`flex-direction:column` で縦)、表は容器の `display:grid; grid-template-columns:repeat(3,1fr); gap:24px` + 字下げに位置を書かない子 (通常の子も ×N の複製も同じ item・cell いっぱい・gap 既定 0)。×N は要素と子の複製で、行自身の display / gap は各 instance の子に効く。重なりは書いた順 (後が上)・`z-index: 2` (CSS どおりの順)・全面の絵は書いた順によらず地・`z-index:front` は既定の段の全部より上・意図の重なり `overlap:相手`。
- 繰り返し: `div#c(…) ×3` + 子 `  p#t(…) a;b;c` (`;` で instance ごと) → `#c[1]` `#c[1].t` `#c[*]`・出る間隔は入場の tween の中 `div#c(in: {y:30, opacity:0, stagger: {each: .12, from: 'end'}}) ×3` か印 `[>#c[*] {stagger:{each:0.04, from:'center'}}]` (stagger は tween の object の中だけ — 1 つの文字なら 1 字ずつ)・消える間隔は `out: {opacity:0, stagger: .08}` (`[<#c[*]]` でも cut 末の自動 close でも)。一括の変化は `[!#c[*] to,{…, stagger:.08}]`・主役の切替は `[!#c[2] focus]` (`stagger: dim` で薄く先出し)。
- 変種: `#名.tag(宣言)` (静止の別の姿) → `[!#名 .tag]` (補間して移る。`points=` / `path=` の shape の変種は形ごと補間 = morph。書体 / style・画像・fit の種類・形の種類・blend・mask が違う変種は補間せず、その語で開き直す — 変種の `in=` が入場・無ければ切替)。部品: `def 名(引数) = tag(宣言) {引数}` → `名#x(…) 文字` (行の末尾の文字は最初の引数・2 つ目からは宣言 `名#x(v: "1,600 円") 紙の本` — `;` は ×N の instance の区切り) (同じ形の 2 つ目も def に上げて実体を並べる)。
- 文字の一部: `{t}語{/}` + `[!#名{t} recolor,$a]` / `highlight` / `marker` / `strike` (`[=#名{t}]` で戻す)。
- 糖衣: 入場の名 `in: rise` (`fade rise drop slide zoom pop wipe` — 量と向きは config: `slide {x: -45}` = 左から・`wipe {dir: 'right'}` + studio の `spring settle bounce flash mask_rise swing_in travel punch typewriter fade_stagger blur pixelate circle_wipe iris_wipe clock_wipe spin_zoom zoom_reverse draw drift ping`。名は型を問わず同じ動き — 文字も層ごと。1 字ずつは stagger を足す `in: rise {stagger: .03}`)・役 `title big div row note` (雛形の根の `motion 名 { in: …; out: … }` 5 行)。property・ease・ms が固定なので、同じ名を繰り返すと動きが揃って見える — 急ぐ時と役の既定にだけ。
- 常時 `main: float|breathe|sway|pulse`・`spin {period: 9}`・`kb {scale: [1.1, 1], focus: '40% 60%'}` (寄りながら動くなら `focus: ['40% 60%', '60% 50%']`)。一度きりの流れ / 寄りは `ramp {x: 120}` か語の無い object `main: {scale: [1.04, 1.12], ease: 'none'}` (GSAP の絶対値・層が出ている間いっぱい)・語から終わりまでは印 `to,{…, duration: END}`。2 本以上の tween は `,` で並べる (`in: fade {duration: .8}, typewriter {level: 3, duration: 0}` — 1 字ずつの語も object では 1 字が 0.5 秒・即座に切り替えるなら `duration: 0`)。同じ tween を関数に `cue 名(x) = [!#x punch][!#x check >]` → 台詞に `[名 #対象]`。
- 字幕: 印だけの行 `[>#subtitle]` で以後の台詞が自動の字幕 (cut を跨いで続く・閉じるのは `[<#subtitle]` — cut 末の印だけの行ならその cut の終わり・hold の字幕札が cut 境界を跨ぐ時は engine が次の cut の lane と 1 枚に繋ぐ (帯は cut で入り直さない))。`subtitle(font-size:48px; …)`・テロップの間だけ消す `.hide_subtitle`。話者札は `cast a = "…" label="部下" label_fill=$a`。

## 書けない物 (runtime に無い・GSAP と違う例外)

- 文字・図形への `filter` (彩度・色行列)・`to` の motion blur・絵 (img / video) の `mask-image` (DEFECT:CSS — 地の色のグラデの幕か画像の alpha `mask:`。板の `mask-image` は svg に焼く・子を持つ div は板だけ)・chroma key・音のピッチ変更は無い。`mix-blend-mode` は `multiply screen add overlay soft-light` だけ。
- 文字の一部 (run) の拡大を保つ・run への glow・layer 単位の glow / tint・子を持つ要素の blend / glow (DEFECT — 傾き skew・3D (`rotationX: 30; depth: 0.8`)・`filter:` の blur / 色調・`to,` の傾き / blur / filter は子ごと 1 枚に掛かる)・語を囲む手描きの丸 (rough-notation) は無い (代用は `reference/capabilities.md` 末尾)。
- `yoyo` の `repeat` は奇数 (偶数は頂点で終わり跳ねる)。1 層に `in` は 1 つ。強調中の文字の一部に別の強調は重ねない。係数つきの ease は `back.out(N)` (N = 行き過ぎ・`back.out(2.4)` も効く) だけで、効くのは `in` / `out` / `main` (`to` では係数を落として warn)。`back.in(N)` / `back.inOut(N)` と `elastic` / `bounce` / `circ` に係数は無い (`elastic.out(1,0.5)` は DEFECT — `elastic.out`)。
- 繰り返す tween (`repeat`) に書けるのは `x y scale rotation opacity`。

## ループ (render 1 回)

1. 工程 (上) の順に書く → `check` を DEFECT 0 まで。
2. check の読み方: DEFECT = 文法の誤り (file:行と直し方つき・描けない)・severe = 描けるが崩れる (直す)・warn = 直す・info = 参考。`出る時刻` の表 = 要素が語に結べているか (変化の列は書いた `[!#名]` `[=#名]` を全部・既定の列は engine が足した動き)。`展開表` = def の実体と ×N の子の名・箱・字の size (印と位置の式 `名.right+8` の宛先はこの名)。`css` の warn = 落とした宣言 (無い物として描く)。
3. `render` 1 回。見た目の指摘を報告に書くときは、その frame (`out/render_frames/`) を Read して秒数と一緒に書く。
4. 通しの批評が要るときは `tmp/critic/make_sheets.sh out/video.mp4 <dir>` の一覧を subagent `video-compare-opus-medium` に (reference/compare.md)。
5. 音は `listen` (render の後・`--apply` で描き直しまで): cut ごとの音を Gemini 3.8 Flash に 2 回聴かせ、場面に合わない音 (2 回一致の drop) と同じ音の連打 (repeat) を `listen.json` に記録し、次の render がそれを外す。音量は聴かせない (床と anchor は engine が測る)。詳細 reference/sounds.md。

規則の名と直し方 (2 つの台帳 製品の check の `draft_check/rules.py` と `quality_rules.py` から生成・型に合わない規則は根の `lint off=規則,…`): `empty_cut` 絵か札を置く・`shrunk` 幅か文字の大きさを変える (枠を広げる / `width:` を外して文字幅にする / 文言を短く)・`offcanvas` (severe) 位置を内側に・`duplicate_text` 字幕と同文の札 → 画面は要点の短い語に。台詞そのものを見せる札 (リリックビデオの歌詞・吹き出し) は札に `.hide_subtitle` (見えている間は字幕を描かない・`lint off` では 2 つ並んだまま)・`spoiler` 見出しが台詞の語を先に見せる → 語の印で出す・`still_stretch` 6 秒以上動かない (絵の kb は動きに数えない) → 語に印を足す・`long_still` (info) 台詞が 3 秒以上続く間に画面が変わらない → その間の語に印・`cut_head_gap` cut 頭が 1.2 秒以上空く → 頭の要素は印なしで置く・`entrance_in_fadeout` 切替や fade out の 0.8 秒前より後に出す → 語を前へ・`entrance_in_transition` 語の印の入場が前の切替の窓の中で済む → 最初の台詞の頭に `[silence:+0.4s]` を足して語を窓の後へ (要る秒は check が言う)・`no_closer` 最後の cut に大きな締めの一言が無い・`same_picture` 同じ絵が 15 秒以上 → cut の中で語に合わせて別の絵・図・札へ替える (cut は分けない)・`blank_band` cut の頭で画面の 1/3 が地のまま → 絵を全面に敷くか帯に札を・`dip_black_frame` dip は黒 frame → dissolve か wipe・`double_exit` 切替で終わる cut に cut 全体の out も掛かり、場面が fade してから切替が走る (二度消える) → 切替が場面を運ぶので section の out を外す (fade で消えたいなら切替を `transition cut` に)・`persistent_chrome` 常設の層 (progress / 章番号 / 累計) は 3 分以上の動画だけ — 短い動画では画面の端を 1 本占有する損の方が大きいので外す・`sparse_cut` 4 秒以上で要素が少ない → 絵か札を足す・`palette_drift` palette 外の色が多い・`low_contrast` 文字と地の差が小さい (沈めた `dim` / focus の兄弟・`recolor` の後も) → 沈める濃さを上げる・`overlap` 同じ族の文字どうしが重なる (`overlap:` を宣言しても warn・別の族の文字を隠すのは severe の occluded) → 判子・札を相手の文字から外す・`title_on_close` 最初の cut の題が閉じられず最後の frame に残る → `[<#名]` (締めで名を言い直すなら締めの cut に新しい層)・`leaks_into_next_cut` (info) 切替の前に他が out で消え、out の無い層だけが次の cut の頭に残る (既定は全員が生きたまま切替に乗る — 残すか消すかを割るのは著者の out だけ) → 揃えるなら他の層にも out を書くか、その out を外す・`orphan_line` 折り返しの最後の行が 1〜2 字 (「本気だっ / た。」) → 文言を詰める・字を小さく・`[br]` で切る・`overridden` engine が書いた値を変えた (cause つき) — subject_clear: 文字を絵の主体の外に置く / icon_square と late_admission: engine の揃え (直さなくてよい)・`transition_over_speech` 切替が台詞に掛かる・`se_dense` 効果音が密 (`sfx off`)・`running_total` 累計の札の値が cut を跨いで減る → plan に書いた累計を写す・`month_reading` 月日に読み `{9月5日|くがついつか}`・`font_not_pinned` 書体を本番の解決で引けず既定 font で測った (DB のある所で check を回す・書体の説明を catalog の書体に寄せる)・`synthetic_bold` family に太い face が無い (browser の合成 bold は無い) → 太さのある family を `font-family:` で選ぶか font-weight を外す・`ghost_dissolve` 400 ms 以上の dissolve で前の cut の大きな文字・絵が次の cut に透ける (out の無い層か、境界より前から溶ける切替) → `overlap=` を尺と同じに (out のある文字は境界までに消え終わる)・out の無い絵や札は cut 末の `[<#名 fade]`・`photo_hidden` 全面の写真の 9 割以上に濃さ 0.7 以上の幕が 3 秒以上掛かる (写真が白く飛ぶ / 暗く沈む) → 写真を片側の枠へ (文字は地の側) か、幕を 0.6 までにして文字の下にだけ帯 / 板。

## stream で作る (製品と同じ段取り・依頼文から 1 本)

```bash
bash .agents/skills/nolang-draft-studio/scripts/stream_make.sh tmp/studio/<name> --type concept --aspect 9:16 --seconds 60 --request <依頼文の file>
```

著者 (Opus・low・1 call) が cut 順に src を流し、cut ごとに担当 (Opus・medium) がプロの解説動画の密度と階層に仕上げ、check → 直し (2 回まで) → 素材 (絵・声) → 確定 → 投入、と
cut 単位で進む。描画は製品の DraftStreamRun (`studio.py stream`・この機械の 1 process) が seal ごとに HLS を伸ばす。最初の cut が seal された時点 (静かな機械で 90〜110 s) から
HLS の segment (`static/video_generate/<process>/`) が増え、全 cut で `studio/out/video.mp4`。名のある定義 (def・motion・run・svg・sound・image・cue) は初めて使う cut の block に書き、
その cut だけが直す。根 (設定・cast・字幕と BGM の開き・常設の層) の持ち主は最初の cut で、その cut が受理された時に凍る。
時刻は `stream/run.jsonl` (`first_segment` / `manifest_published` / `final_ready`・cut ごとの `staff` `check` `fix` `warm` `submitted` `sealed_ack`)、担当の前の著者の版は
`solo/author_cut_<名>.txt`、各 cut の doc と check は `weave/<cut>/`。`--no-staff` は担当なし (速いが質は落ちる)・`--staff balanced` は cut 1・2 だけ担当 low (止まらない開始 中央 約 130 → 90 s・質は小さく落ちる)・`--staff low` も可。effort は著者 `--effort`・担当 `--staff`・見直し `--review` (既定 low・`medium` も可・全 cut の 1 回目の直し役が厳しい監督として弱い所・崩れも探す・`none` で無し)・直し役 `--fix` (既定 `severe` = DEFECT と severe の指摘 (隠れる文字・画面の外 …) だけ直し役 low・見直しなし・warn は直さない・`defect` = DEFECT と隠れる文字だけ・`none` で直し役も無し・`low` で見直しと指摘の直し)。担当は既定で絵と台詞を変えず、絵と声は著者の版から担当と並列に作る (`--staff-edits-assets` で担当が絵と台詞も直す・`reference/stream.md`)。`--look` で見直しに cut の静止画も見せて 2 回 (local だけ・cut あたり +30〜50 s・`reference/stream.md`)。3 役の prompt は規則の束でなくプロへの依頼 + 文法 + 制作の作法 (`reference/craft.md`) (10-23・`reference/stream.md`)。見本は既定で `reference/samples/` の自分の type の `hf_*` 2 本 (依頼と同じ題材の物を除き、依頼と同じ向きの物を先に・file 名順の先頭)。
変えるなら `--samples a.md,b.md` (前の run の `stream/samples.txt` もそのまま渡せる)。質の根拠は `docs/draft_src_v2/stream-evidence-261013.md` と `reference/stream.md` の「3 役の prompt」。
描画を NoLang の server に任せるなら `--remote http://<api> [--token nlg-c-…]` (素材・描画・配信は製品の draft stream renderer、この機械は著者・担当・直しだけ)。token は API key か、Claude Code が `/mcp` で NoLang に接続 (OAuth・`mcp.json`) した時の token (省略時に自動で使う)。 repo の外 (plugin で入れた skill) では `--remote` だけが動き、check / 改名 / 規則の台帳は API から受ける (骨組みは `reference/scaffolds/`・python は `python3` で足りる)。plan が出た時点で `WATCH <url>` (video page・追いかけ再生) が出る。見る人が再生を始められる時点 (status の `playable`) で `PLAYABLE <url>`。手元の run (`--remote` なし) も同じ受け口 (投入・warm・check) を手元で呼ぶので、段も check の指摘も同じ。契約は `app_main/docs/feature/video_generate/external_author.md`。 依頼に決まった素材 (この写真・この曲・この声) があれば、MCP の `nolang_assets_search` (scope=mine は自分の upload) で探し、手元の file は `python3 .agents/skills/nolang-draft-studio/scripts/upload_asset.py <file>… --remote <api>` (plugin なら skill の dir の `scripts/`) で upload する (`REF <file> id=<uuid>` が出る・動画は仕上げを待つので数十秒)。その `ref` (`id=<uuid>` など) を依頼文に書けば、著者は `image 名 = id=…` / `bgm#名 id=…` / `cast 名 = id=…` にそのまま写す。

## 辞書と待ち方

`reference/authoring.md` は節を行番号で読む (Read の `offset` / `limit`): L7 HTML 形 · L16 字句 · L33 design.txt · L62 型 · L77 位置 · L95 動き · L106 ×N・群・def と根の雛形 · L164 字幕・cut · L168 timeline.txt · L198 印 · L217 時刻の規則 · L226 cue と切替 · L232 欠陥。key の名は v2 の綴り (`size` `fill` `radius` `shadow` …) で載っているが、CSS の名 (`font-size` `background` `border-radius` `box-shadow` …) でそのまま書ける。
render は前景で `timeout 900 $P $S …`。GPU を分け合うなら `STUDIO_RENDER_LOCK=<file>` を前置。resource-service が落ちていれば起こす (前提 (環境))。
2 本を比べるときは `reference/compare.md`。
この skill の形 (圧縮の規則 4 つ + 違い 5 つ + 工程 + 見本) の根拠は `docs/draft_src_v2/studio-skill-evidence.md`。

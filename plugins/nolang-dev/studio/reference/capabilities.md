# runtime の能力表 — VC の型と描画の field を v2 の property・印でどう書くか

HTML + GSAP の表現を書くとき「書けない」と思ったら、まずここで runtime (`domain/entities/video_component*.py`) の field を引く。
書き方の列: 要素の行の CSS 宣言 (`tag#id(…)`) / 印 · **✕** = 書けない (理由)。文法の形は authoring.md、型ごとの全 key は `docs/draft_src_v2/grammar-spec-types.md`。最後の「runtime に無い物」は runtime を足す判断待ち。

## 層の共通 (VisualLayerBase)

| field | 書き方 | 備考 |
|---|---|---|
| frame_layout x y w h | 根 `left top width height` / `inset: 0` / `inset: 上 右 下 左` · 子 `left top right bottom width height` (親の内側から) · 表 = 容器の `display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px` + 字下げの ×N 1 つ (CSS の grid: 各 instance が cell いっぱい・gap 既定 0・×N の行の `display: grid,3` と同じ) | 語で動かす = `[!#名 to,x+=dx,y+=dy]` `[!#名 to,x= y= left= top= scale= w= h=]` |
| frame_layout rot | `transform: rotate(-8deg)` · `[!#名 to,rotation=-15,pivot=100%,0%]` · `[!#名 to,rotation=720]` (上限なし = 2 周) | `transform-origin` (印では `pivot=`) は回転・倍率の原点 (中心は原点のまわりの弧を辿る・静止の rotate も原点のまわり — 中心の移動に畳む・原点つきの一周 (360° の倍数) は rotation だけの印なら engine が 180° ずつの key に割る (ease は半周ごと・他の変化と同じ印に書いた一周は DEFECT)・箱を書いた群の `transform-origin` と静止の `scale()` は書いた箱に対して解く (CSS どおり — engine の原点は member の合併なので写す・原点が合併の外の群に倍率 / 回転の入退場は DEFECT)) |
| frame_layout rx ry perspective (静止の 3D の傾き) | `transform: rotateX(30deg); depth: 0.8` · `[!#名 to,rotationX=0,duration=1200]` (補間) | 中心まわり — 下辺を軸にするなら `main: constant {rotationX: 30, depth: 0.8, pivot: 'bottom'}`・透視の中心は pivot (CSS の `perspective()`・depth = 短辺 ÷ 視点距離 px で、VC の perspective = 短辺 / depth px — 透視の床 = 群に `main: constant {rotationX: 70, depth: 4, pivot: 'top'}`)・子は一緒に傾かない。眼の後ろに出る角は描けない (native の上限): 上辺を軸に 70° 倒す床は `depth·sin(rx) ≤ 0.8` で飽和するので、床は眼より手前の高さだけにする (CSS の perspective 780px → 高さ 660px・`depth: 0.85` = 440/520) |
| frame_layout skx sky (静止の skew) | `transform: skewX(-12deg)` · `[!#名 to,skewX=12]` (補間) | CSS の skewX と同じ向き・±80°・素材も塗りも文字も枠ごと傾く (子を持つ要素には書けない — 子ごと 1 枚の群は平面) |
| media_layout (cover の切り抜き) | `object-fit: cover; object-position: 60% 0%; zoom: 130%` · `main: kb {scale: [1.1, 1], focus: '40% 60%'}` · `[!#名 zoom_media,1.3,duration=900,focus=40%,60%]` · `[!#名 to,w=640]` (切り抜きごと補間) | zoom_media は枠が動かず素材だけ寄る (cover の絵だけ — 箱の中の絵は `[!#箱.子 zoom_media]`) |
| media_layout x_flip y_flip | `img#名(flip: x\|y)` (写真・生成画像・svg の鏡像) · `icon#名(flip: x\|y)` (svg を焼き直す) · `avatar#名(flip: x)` | |
| visual_filter opacity contrast brightness saturation | `filter: saturate(.3) brightness(1.2) contrast(1.1)` · 語で `[!#名 to,{filter: 'saturate(0)', duration: .6}]` (filter 全体を置き換える) | 絵・写真・svg は素材に掛かる・文字と図形 (div の塗り・縁・影も — svg に焼いた板は本体に掛かり地 / 縁 / 影を焼く) は engine が描かないので書いた色に焼く (同じ式・色を書いていない文字は DEFECT)・子を持つ div には書けない (中の絵に)・子を持つ絵は絵の素材だけ |
| visual_filter blur (静止のぼかし px) | `filter: blur(6px)` · `[!#名 to,blur=8,duration=600]` (補間) | 層の raster 全体 (文字・板・絵) — 群と子を持つ要素には書けない |
| visual_filter color_matrix | `filter: sepia(1)` / `invert(1)` / `hue-rotate(90deg)` (`grayscale(a)` は彩度 = `saturate(1 − a)`) · CSS に無い look は `look: cool\|warm\|faded\|polaroid\|kodachrome\|technicolor\|browni\|vintage` · 単色化 `look: #暗/#明` (duotone) · `look: #色` (絵の形 (alpha) だけ残して 1 色で塗る = CSS の `mask-image` + 単色) | **✕** 生の行列 |
| (画面全体の色調) | `veil#名(filter: saturate(0))` (= `filter: grayscale(1)`・か `look: #000000/#3366FF`) を `[>#名]` … `[<#名]` | 開いている間、下の層 (後から出る物も) を色調の変種へ — 文字と図形は look の行列と彩度を掛けた色の変種で写す |
| alpha | `opacity: .5` · `[!#名 dim,0.3,duration=900]` · `[!#名 to,opacity=0.5]` | 子孫にも掛かる |
| (画面全体の閃光・暗転・揺れ) | 全面の `veil#fl(color: #FFFFFF; opacity: .55; z-index: curtain; in: none)` を `[>#fl][!#fl to,{opacity:0, duration:.4}]` (閃光) / `[>#名]` … `[<#名]` (暗転)・揺れは出ている要素ごとの `[!#名 shake,6,duration=2200]` を同じ語に | 幕は veil・揺れは層ごとの一回きりの shake (画面全体を指す印は無い — CameraLayer は viewport だけで揺れの channel が無い) |
| (写真の暗幕) | `img#名(scrim: right,0.45)` (`vignette,0.6` / 一様 `0.4`) | 絵の子の veil が絵の直上で一緒に出入り |
| pattern (svg に焼く板) | `pattern: dots,間隔,色,径` (CSS の `background-image: radial-gradient(色 2px, transparent 2px); background-size: 48px` も同じ) · `pattern: grid,間隔,色,幅` (CSS の方眼 `background-image: linear-gradient(色 1px, transparent 1px), linear-gradient(90deg, 色 1px, transparent 1px); background-size: 60px 60px` も同じ — 縦横 1 枚ずつ・同じ色と幅) · `mask-image: radial-gradient(…)` で放射に薄める | 板の svg (FE は同じ画像) |
| border w c radius | `border: 幅 solid #色` · `border: 幅 dashed #色` / `dotted` (箱・形・文字の札・楕円) · `border-radius:` (角ごと `border-radius: 0 33px 33px 0` は svg に焼く・全隅が同じ `50%` 以上は楕円 (CSS どおり・幅と高さの変化に追随)・pill は `999px`) | 50% 未満の %・角ごとの %・`a / b` (CSS の楕円の角) は短辺 × N% の円の角で描く (warn)・破線 / 点線は Chromium と同じ模様 (dashed: 幅 3 以上は線 2W・間 W・細い線は 3W / 2W、dotted: 幅 3 より太いと直径 W の丸い点を中心間 2W)・周に整数回で収まるよう間を詰める・線種は変種で切り替えられない・`double` / `groove` / `ridge` / `inset` / `outset` は DEFECT:CSS・辺の線 (`border-left:`) と吹き出しの形・字幕の帯は実線だけ |
| border shape (形 70 種) path dash cap | `shape#名(path: arrow_r)` (形の名前 48 種) / 楕円は `border-radius: 50%` / `points:` / `path: "M…"` · `dash: 6,6` · `stroke-linecap: butt` (`border:` の線は既定 round・SVG の綴り `stroke: 色; stroke-width: 6` の線は既定 butt) · `fill: 色` · `path: "M … A …"` (SVG の全文法・A は C に直す) · `filter: drop-shadow(0 8px 16px 色)` (= box-shadow) · 文字の板・絵の mask 形は `p#名(shape: star)` / `img#名(shape: star)` | 形の変形 (morph): `points:` / `path:` の shape (単色の塗り) の変種 `#名.tag(path: …)` へ `[!#名 .tag]` で頂点を補間 (状態 key の `border_path`)。形の種類の違う変種は開き直し (切替) |
| start_offset end_offset | `delay: 320` · 印の `+N` / `cut-N` (印の `+N` が `delay:` に勝つ) | |
| motion_in / motion_out / motion_main | `in:` `out:` `main:` (下の「Motion」) | 1 位相 3 本まで (後の語の一回きりの効果と `window=` を書いた `[!#名 main,…]` は同じ層の anchor 窓の main で別枠)・1 本の keyframe (`keys(at=…)`) は 24 個まで (at=1 は数えない) |
| keys = 状態 key (同じ層の状態の補間) | 印の変種 (`to` `move` `scale` `fill` `dim` `glow` `filter` `zoom_media` `.tag`) · 変種の `move: 600,sine.inOut` | `to,x= y= scale= scaleX= scaleY=` は frame の transform (tx ty sx sy・箱は変えない)・path = `to,…,arc=0.3` / `via=(x,y)`・`to,skewX= rotationX= rotationY= depth=` (姿勢)・`to,glow=1.5` (発光の強さ)・1 語の中で拍を書き分けて続ける (`[!#a to,rotation=-30 -50][!#a to,rotation=-22 +750]`・前の移りが途中なら途中の値から) |
| bg_color | `background: #色` (div の地は書いた時だけ — 既定は透明) · `[!#名 fill,$色]` / `to,fill=` (400 ms で補間 — glass・角ごとの角丸・尻尾・点列の板も単色の地は層の塗り) | グラデの地は svg に焼く (印の fill は DEFECT:ARG) |
| blend | `mix-blend-mode: screen\|multiply\|add\|overlay\|soft-light` | 印の変種なし |
| mask_media_id | `mask: "[transparent]筆で払った線、文字なし"` / `mask: @名` (+ `background: $色` で筆の形の単色塗り) | 画像の alpha を素材と塗り地に掛ける (文字は対象外・縁を書くと枠の中が縁の色になる) |
| shadow color dx dy blur spread | `box-shadow: 1..5` / `box-shadow: dx dy blur [spread] #色` (`0 0 0 21px #E8743B` = 外側の太い縁) · `glow: $色[,blur[,spread]]` · `[!#名 glow,blur=18,spread=10,$色]` | |

## 文字 (TextLayer・TextStyle・ParagraphStyle)

| field | 書き方 | 備考 |
|---|---|---|
| font_id | `font-family: "family 太さ"` / 根の `font` `fonts` の短い名 `font-family: m` / `style: "書体の説明"` (意味検索) | `font-weight: 900` (1〜1000・normal / bold) は family の中の face を CSS の照合で選ぶ (名や説明文の太さより優先・箱から継ぐ・`h1〜h4` は UA の 700)。1 face の family は変わらない (合成 bold は無い・warn) |
| font_size | `font-size: 72px` (`hero h1 h2 body label note` も・CSS と同じく書かない文字は親の値を継ぎ根は 16px・`em` は親の比・箱の font-size は子が継ぐ — `font-family` `color` `letter-spacing` `white-space` も同じ継承) | 語で `[!#名 to,scale=0.5]` (transform の sx / sy・箱は変えない)・`~` で size の違う変種へ移ると文字は frame の中心で拡縮 (折り返さない・枠線も太る) |
| color | `color:` (svg は本文の currentColor に焼く) · `[!#名 fill,$色]` (補間) · `[!#名 recolor,$色]` / `to,{color}` (文字・図形・icon・1 色の svg は補間 — svg は色行列) | |
| color_gradient | `color: linear(#FFE58A,#F5A623@60%,#C2410C,180)` / `radial(#…,#…,30%,60%[,72%,62%])` | 角度は CSS と同じ・`@N%` は止まり位置・radial の後ろは中心 (と楕円の半径) の箱の比 |
| stroke_color stroke_width | `stroke: #色,幅` (文字の px) | |
| 影 kind=drop | `text-shadow: dx dy blur #色` / `text-shadow: 1..5` | |
| 影 kind=glow | `[!#名 glow,$色]` (字形の光彩・text-shadow 0 0) | **✕** neon / echo / glitch の影 (`style:` の意味検索だけ) |
| highlight underline strikethrough | `[!#名{t} highlight,$色]` (run) · `underline: $色` (題の下の帯) · `[!#名 strike]` (取り消し線の図形) | 進行の style は `in: marker` / `in: underline_draw` / `in: strikethrough` (文字の preset) |
| italic | `font-style: italic` | |
| runs (文字の一部の style) | 根の `run hl { color: …; font-size: …; stroke: …; font-family: …; marker: …; background: …; border: …; border-radius: …; padding: … }` + content の `{hl}…{/}` (地の枠と下帯の形 = ParagraphStyle.highlight_box・文字で 1 つ) | 語で `[!#名{t} recolor / highlight / marker]` (`recolor,$o,250,400` = 250 ms で移り 400 ms で戻る)・一回きりの `[!#名{t} punch,1.12,duration=440]`・`[=#名{t} +600]` (span の切替を語から ms ずらす) |
| counter | content の `[count:9.4 start=0 roll ms=1400]` · `[count:400 roll ms=1150,1000,850]` (桁の帯ごとの所要 = CounterSpec.digit_ms・0 = 回らない帯) · `[count:… laps=0,0,0,3]` (帯ごとの周回数 = CounterSpec.digit_laps・0 = まっすぐ・既定 1) · `[count:… ease=power1.inOut delay=320]` · `[!#名 count]` | |
| spans (文言の切り替わり) | `[!#名 text,"文"]` (`[=#名]` で元の文) · 著者の変種の `content: "…"` を `[!#名 .tag]` で · 後の語の `[!#名 count]` | 同じ層の文言の切替 (箱は全部の文の最大)。地を持ち寸法を書かない文字と跨ぐ文字は写しの層に入れ替える |
| paragraph horizontal / vertical align | `text-align:` `vertical-align:` | |
| paragraph line_height letter_spacing writing_mode | `line-height:` · `letter-spacing: .1em` · `writing-mode: vertical-rl` | |
| padding | `padding:` (1 / 2 / 3 / 4 値) | |
| 塗りつき札の地のグラデ | `p#名(background: linear-gradient(90deg, #a, #b 42%, #c))` (札の下に焼いた板) | |
| chroma_key | **✕** | draft の語彙に無い (editor の keying) |

## Motion (EdgeMotion・MainMotion・MotionChannels)

| channel | 書き方 | 備考 |
|---|---|---|
| dx dy rot sx sy alpha blur | `in: {x: -45, opacity: 0, duration: .6}` / `in: keys(at=0 … \| at=0.6 …),duration=900` (時間は ms) / `main: sine {y: 18}` | 動きの `x y` は px (層の寸法で換算しない)・`scale scaleX scaleY` は倍率・`rotation` は deg |
| skx sky | 同じ (`in: {skewX: -20, opacity: 0, duration: .5}`) | 静止の傾きは層の `transform: skewX(-12deg)` (上の frame_layout) |
| rx ry perspective (+ `depth`) | 同じ (`main: constant {rotationX: 35, depth: 0.8, pivot: 'bottom'}`) | layer の単位だけ |
| color (描画色) | `in: {color: '#FF0000', …}` | 文字の単位だけ (書けば unit=paragraph) |
| glow gradient_shift stroke_width | `in: {glow: 3, …}` · `main: sawtooth {gradient_shift: 1, period: 1.8}` (`color: linear(…)` の文字) | 文字の単位だけ (unit=paragraph が付く)・箱 / 絵に書くと欠陥 |
| tracking | `in: {letterSpacing: '0.6em', opacity: 0, duration: .9}` (字間が詰まって入る・px と素の数は同じ行の `font-size:` で em に割る・印の `to` は em だけ) | 文字だけ・unit=grapheme が付く・字 i を i × 値 em 右へ (左揃えの伸び) |
| scramble | `in: {scramble: '01ABCDEF', duration: .6}` / `in: decode` | 文字だけ |
| elevation | **✕** (v2 の channel に無い) | 影 (`box-shadow:` / `glow:`) を持つ層だけの影の倍率 |
| reveal (+ reveal_shape) | `in: wipe {dir: 'right', angle: -20}` · `in: circle_wipe` / `iris_wipe` (円の中心 `pivot: 'top'` 等の 9 名・曲線 `ease`) / `clock_wipe {dir: 'left', splits: 3}` | `out:` も同じ・`in: wipe {dir: 'center'}` は横の倍率 |
| pixelate | `in: pixelate` | |
| number | `[count:…]` | |
| draw dash_offset | `in: draw {duration: .6}` · `main: sawtooth {dash_offset: 1}` | 枠線のある path の図形 |
| clip | `in: {…, clip: true}` · `in: mask_rise` | |
| style (進行済みの文字の上書き) | `in: karaoke {color: '#…', duration: 0}` (object の 1 字は 0.5 秒 — 即座に切り替えるなら `duration: 0`) / `in: marker` / `in: color_sweep` | 文字の preset |

| 軸 | 書き方 | 備考 |
|---|---|---|
| unit | `in: rise {y: 30, duration: .4, stagger: .04}` (1 字ずつの間隔 — stagger の無い `in: rise` は文字も層ごと) · range (`[!#名{t} punch]` が作る) | 文字だけ |
| order seed | `in: fade_stagger {from: 'random', seed: 3}` · ×N の入場 `in: {stagger: {each: .06, from: 'center'}}` / 退場 `out: {opacity: 0, stagger: {each: .06, from: 'end'}}` (`[<#名[*]]` と cut 末の自動 close で同じ) · 項目 `[>#名[*] from=center]` `[<#名[*] from=random +110]` | reverse / center_out / random |
| step duration delay | 入場の tween の `stagger: .04` (= step) · `in: pop {duration: .5}` · `delay: 320` / 印の `+N` | duration を書かない object は GSAP と同じ 0.5 秒・語だけの preset (`in: fade`) は語ごとの既定 |
| easing (bezier spring steps) | `ease: 'back.out(1.7)'` / `back(2.2)` / `bezier(.2/.8/.2/1)` / `spring(10/240)` / `steps(4)` · 名は GSAP の綴り (lowering が EffectEasing に写す: power1 = ease_* · power2 = cubic_* · power3 / circ = quart_* · power4 / expo = strong_ease_*) · keys の区間ごと `at=… ease=bezier(.33/1/.68/1)` (main の keys も・at=1 は静止へ戻る最後の区間) | 係数つきは preset の入場と keys の key だけ |
| pivot_point | `transform-origin: left` / `transform-origin: 40% 60%` / tween の `pivot: 'left'` · `[!#名 punch,1.05,duration=600,pivot=left]` · `[!#名 to,rotation=,pivot=]` | |
| target=media | `main: kb {…}` · `main: ramp {target: 'media', scaleX: 1.3, scaleY: 1.3}` · `[!#名 zoom_media]` | x y scaleX scaleY rotation だけ |
| path orient | `in: travel {start: '名', arc: 0.3}` / `via: '(x,y)(x,y)…'` (経由点をなめらかに通る・2 点で S 字) · 変種の `move: 600,sine.inOut,path="M…"` | path は quote |
| main の waveform period (freq_ms) phase_step phase_offset window reverse | `main: sine\|triangle\|square\|noise\|sawtooth\|ramp\|constant {…, period: .9, phase_offset: 0.25, window: '0,2200', reverse: true}` | |
| main start_ratio end_ratio | `main: kb {scale: [1, 1.06], start_ratio: 0.3}` / `main: ramp {…, start_ratio: 0.3}` · 進行バー `progress#名(until: cut\|end)` (ramp が層の実効の窓 = 尺を書かない) | |
| settle · driver · blend_ms | **✕** | 正準の語彙外 (名前つき演出の畳み込み専用・avatar の話者状態) |
| 一回きりの効果 | `[!#名 shake / punch / blink / pop / spring / swing]` (`punch,1.1,duration=450,rotation=8,pivot=left`) | `in: pop {then: 'shake'}` |

## 切替・場面 (SceneTransition・Scene)

| field | 書き方 | 備考 |
|---|---|---|
| transition kind duration overlap zoom bars sweep drift dim easing backdrop | timeline `transition none,370` (混ぜない — 退場が次の cut の入りに重なる) / `transition wipe,700,dir=left,overlap=350,bars=#色,18,drift=140` / `bars=linear(色,…),幅` (グラデの帯・`linear(色,…,180)` = 帯の縦のグラデ) / `dissolve,850,dir=right,bars=…` (溶けの上を帯が払う) / `slide,850,dir=left,drift=240,dim=0.38` (旧頁がずれて暗む) / `dissolve,600,overlap=300` (境界中心) / `dissolve,320,overlap=320` (旧場面の上に 0 → 1) / `dissolve,320,color=#色` (黒の上から) / `dip,400,color=,level=` / `flash,300` | dissolve の既定の easing は linear |
| enable_pre_fade post_fade | `fade in,1800` / `fade out,700` | |
| head_pause tail_pause | 台詞の `[silence:600]` / 根の `silence head= tail=` | |
| speedup_percent | `cast 名 = … speed=110%` · 台詞の `[speed:120%]` | |
| override_speaker / indicator | `cast` / `manner=` / `[manner:…]` (台詞ごとは Fish Audio の声だけ) · キャラの声色 `@名.style:` | |
| override_display_texts | `subtitle "…"` | |
| yomi_edits | 根の `read 表記 = 読み` (全出現) / 台詞の `{表記\|読み}` (1 か所) | |
| audio_filter volume_db (声) | `voice#名(volume: +3dB; filter: echo\|radio[,scale=,freq_ms=])` · 変種 `voice#名.tag(…)` を `@名 .tag:` で | |

## 字幕 (ScriptLayer・ScriptLayout・SpeechWindow)

| field | 書き方 |
|---|---|
| frame / fill / border / radius / padding / shadow / alpha | `subtitle(left: …; top: …; bottom: …; width: …; height: …; background: …; border: …; border-radius: …; padding: …; font-size: …; font-family: …; style: …)` |
| hug | `subtitle.hug(…)` |
| card_motion_in / out | `subtitle(in: pop; out: fade)` (札ごと・custom / keys も) |
| speech_window | `lead: 100; tail: 300; hold: next,800` / `hold: same` / `hold: off` (ms) |
| speaker_label | `cast 名 = … label="部下" label_fill=$a label_color=#…` + `subtitle(label: edge\|above\|top_left\|inside; label_in: pop)` |
| 札の変種 | `subtitle.em(…)` + `subtitle .em "…"` / 札の頭の `[card:em]` / `cast 名 = … subtitle=.em` (札の声の窓 `lead: tail: hold:` も = ScriptCardStyle.speech_window) |

## 群・camera (GroupLayer・CameraLayer)

| field | 書き方 |
|---|---|
| origin / pose (zoom rotate) | `group#g(…)` + `[!#g to,x=,scale=,rotation=]` / `[!#g to,scale=0.8]` / 変種 `#g.small(left: …; top: …; scale: .8; rotate: -6deg)` を `[!#g .small]` |
| alpha | `[!#g dim]` / `to,opacity=` |
| 子を持つ要素 (div・絵・文字 … 型を問わず) | 子ごと 1 枚 (CSS の stacking context): `opacity:` `transform: rotate()`・入退場・`[!#名 to,x= scale= rotation=]` / `move` / `scale` / `dim`・一回きりの効果は群 (子ごと・原点は描いた箱の中心)・塗り / 縁 / 影 / 印の glow / tint / frame・絵の Ken Burns / 色調 / 素材の寄り・文字の 1 字ずつの入場は要素自身 (子には掛からない) |
| clip (角丸の窓) | `group#g(clip: 24,g.bg)` / `clip: true` (窓は箱の枠線の外周まで・def の中 / 箱の子の群にも) · 要素の `clip-path: inset(8% 0 78% 0)` (要素を群 + 本体にして箱の内側の矩形で切る — 動きは切り口ごと) · 子を持つ要素の `overflow: hidden` (子だけを切る群 `名._clip` — 窓は縁の内側の角丸・板の縁と影は切らない)・窓は角丸の矩形だけで楕円の窓は無い (群の `border-radius: 50%` は warn で落とす・楕円の箱の中の `clip: true` も矩形で切る) |
| motion_in / out / main | 群に `in:` `out: fade {duration: .4}` `main: spin {period: 9, pivot: 'g.sun'}` — 群に掛かるのは移動・拡縮・回転・傾き・3D・不透明度・ぼかし (`out: {y: -14, blur: 8, opacity: 0, duration: .32}`) と経路・透視だけ (wipe 等は DEFECT:ARG — 板か子に) |
| camera viewport | `[!#名 zoom,1.4,duration=700]` / `[=#名]` · `camera#cam(left: 0px; top: 0px; zoom: 1)` + `#cam.tight(left: 300px; top: 150px; zoom: 1.4; move: 700)` + `[>#cam]` `[!#cam .tight]` |

## 音 (BgmLayer・SoundEffectFire・MasterLoudness)

| field | 書き方 |
|---|---|
| BGM volume_db / fade / crop_start | `bgm#名(volume: -3dB; fade: 1500,2500)` (volume の既定 +7dB = 声の 9 LU 下 — 書かない) · timeline `bgm 名 start=13.7s +1500` |
| BGM keys (volume_db・語の anchor) | `[!#名 to,{volume:-13dB, duration:.6, ease:'power2.out'}]` (曲の既定の大きさからの dB)・design の変種 `#名.low(volume: -6dB)` を `[!#名 .low]`・`[=#名]` で戻る |
| ducking | 既定で掛かる (−4 / 200 / 500 / 600 / 200)。`bgm#名(duck: -6; duck_attack: …; duck_release: …; duck_merge: …; duck_lead: …)`・`duck: off` |
| keys の volume_db (音量の点列) align_end lowpass_hz | `keys: "0:+3\|15s:0\|end-3s:+2"; align: end; lowpass: 650` (`align: end` = 曲の末尾を層の末尾に・文字の寄せでないので `text-align` ではない) · 区間だけ `lowpass_keys: "20s:650\|28s:off"` |
| keys の volume_db (変種の音量へ移る)・飛び (jump) | 変種 `#名.tag(volume: -6dB)` を `[!#名 .tag]` · `jump: 91.6s>166.8s; xfade: 1300` / `jump: at_cut:名>166.8s` |
| BGM audio_filter | `bgm#名(filter: echo\|radio,scale=,freq_ms=)` |
| SE volume offset crop fade | `se "…" -4.5dB -200 start=0.2s to=1.2s fade=100,800` (台詞の `[♪… -4.5dB peak=4.02s to=1.2s]` — start = 素材の頭出し・peak = 素材の山を語に) |
| master lufs true_peak | 根の `master lufs=-15 tp=-1` |
| 素材の再生 (mute loop fit_duration crop) | `img#名(play: loop\|stretch,start=500,to=1500,speed=150%,mute)` (img の footage・`stretch` = fit_duration・`start` = crop_start。bgm は常に loop — 書かない) |

## runtime に無い物 (判断待ち — v2 でも足さなかった)

- **文字・図形への filter** (彩度・色行列・contrast・明るさ): VisualFilter は素材だけ。文字と図形の filter と色調の幕は書いた色 (文字色・縁取り・塗り・縁・影・発光・地・文字のグラデ・filter は run の色も) に絵と同じ式で焼く (svg に焼いた箱は素材なので filter が効く・既定の文字色は焼けない — `color:` を書く)。
- **mix-blend-mode の saturation / color / hue / luminosity**: BlendMode は normal / multiply / screen / add / overlay / soft-light (画面全体の彩度落ちは色調の幕)。
- **拡大したまま保つ文字の一部 (run の scale)**: run の印は一回きり (punch / settle / shake / pop) と色・下帯だけ — 保つ拡大は別の文字に分けて `[!#t2 scale]`。
- **子ごと傾く要素**: 子を持つ要素 (型を問わず) は子ごと 1 枚 (CSS の stacking context) で平面 — `rotateX` / `skewX` / `depth`・`filter:` / `mix-blend-mode:` / `glow:`・`to,skewX= blur=`・入退場の wipe は DEFECT。傾けるのは子の無い要素 (兄弟に重ねた板) か子の各要素 (回転 `transform: rotate()` と拡縮・移動・不透明度・入退場の `blur` は子ごと)。
- **layer 単位の glow / tint**: 字形の channel は文字だけ (箱・絵の発光は `glow:` の影)。
- **語を囲む手描きの丸・括弧** (rough-notation の Circle / Bracket / Box): 語の印は `highlight underline strike marker` (文字) と `frame` (要素の縁) だけ — 囲むなら文字の上に `shape#o(left: …; top: …; width: …; height: …; path: circle_hand; border: 6px solid $a; background: none; in: draw {duration: .5})` (`bracket` `brace` `corners` も) を重ねて `[>#o]`。
- **motion blur** (移動の残像): 入退場の `blur` channel で代用 (`in: {x: -360, blur: 18, opacity: 0, duration: .45, ease: 'power3.out'}`)。印の `to,blur=` は静止のぼかしへ移る (移動の残像ではない)。
- **音のピッチ変更** (Remotion の toneFrequency): BGM / SE / 声とも無い — 別の素材を探す (`se` の説明文で高さを書く)。
- **svg の中の動き** (SVG の animate・svg の中の id への GSAP): svg は 1 枚の静止画で、中の id は印の的にならない。動かす物は部品 (shape / path / group・切り抜いた svg) に分けて層にし、語の印 (`to,{rotation}`・`in: draw`・変種の morph・`recolor`・`in: wipe`) で動かす — hf 14 本の svg animate 85 回を全部この形で書けた (10-23 実測・scratchpad m1)。svg + GSAP を透過動画に焼いて 1 層にする経路は採らない (同期が声の実尺の後の焼き直し必須・VC の外の黒箱が黙って古くなる・費用 4〜5 倍)。再検討は、製品の著者が部品に分けて書けない svg animate を実際に出した時だけ。
- **絵 (img / video) の mask-image** は DEFECT:CSS (絵の mask は画像の alpha `mask:` だけ — 透過の絵か svg で。地が単色なら絵の上に地の色のグラデの幕 `div#f(inset: 0; background: linear(#地色00,#地色,180))`)。板 (div / shape) の `mask-image: linear-gradient(…)` / `radial-gradient(…)` は svg に焼く — 子を持つ div は板だけが溶けて子の絵には効かない (warn `board_mask`)・**chroma key** (draft の語彙に無い)。

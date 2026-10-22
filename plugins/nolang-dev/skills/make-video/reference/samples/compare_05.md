# compare · 通常 CAD とリバース (横・比較 + 流れ図) — canvas 1920x1080・170.2s・視聴者 91.0 (Gemini・vs hf)

見せる文法: 流れ図の札 (def node ×N + 位置の式で置く矢印)・比べる 2 列 (div の段 ×N)・count・×N・stack・manner・se・sticky・def・run・bgm 切替

```design.txt
#v2
# 計画: 端正な格子を少し柔らかく — 地は graphite + grid・通常の CAD = 橙 (a)・リバース = 青緑 (b)
# 全編の主役は同じ 1 つの L 字ブラケット (基準画像 part) — ワイヤーフレーム / 実物 / 点群 / メッシュ と姿を変えて「向き」の違いを見せる
# 書体 太い角ゴシック (見出し) + 太い等幅 (数字・英字の小見出し) + 細い角ゴシック (注記)・文字の段 26 / 56 / 30 / 32 / 24 / 寸法 44
canvas 1920x1080 bg=#12161C
theme dark
palette a=#F28C28 b=#2EC4B6 bg=#12161C ink=#EEF1F4 mute=#9AA4B1 line=#2A313B panel=#1A1F27E8 ok=#2EC4B6 bad=#E5484D a_t=#F28C2829 b_t=#2EC4B629
font "太い角ゴシック体、すっきりした現代的な印象"
fonts e="太い等幅のモノスペース体、数字がそろう" m="細い角ゴシック体、本文向き"
photo_style "製品の3DCGレンダー、マットな質感、柔らかいスタジオ照明、暗いグラファイトの背景、浅い被写界深度"
prompt_tail "文字なし、ロゴなし、人物なし"
motion title { in: {y:-60, scale:0.94, opacity:0, duration:0.55, ease:'back.out(1.6)'}; out: {y:-24, opacity:0, duration:0.24} }
motion big { in: {scale:0.6, opacity:0, duration:0.45, ease:'back.out(2.2)'}; out: fade {duration:0.22} }
motion div { in: {y:36, opacity:0, duration:0.45, ease:'power3.out'}; out: fade {duration:0.22} }
motion row { in: {x:-90, opacity:0, duration:0.4, ease:'power2.out'}; out: fade {duration:0.2} }
motion note { in: {y:21, opacity:0, duration:0.35, ease:'power2.out'}; out: fade {duration:0.2} }
div { in: div; border-radius: 21px; border: 2px solid $line; background: $panel }
cut { stagger: sentence }
run a { color: $a }
run b { color: $b }
def h1(t) = p(font-size: 84px; line-height: 1.15; color: $ink; in: title; content: {t})
def num(t) = p(font-size: 36px; font-family: e; color: $a; letter-spacing: 0.2em; in: note; content: {t})
def sub(t) = p(font-size: 45px; font-family: m; color: $mute; in: note; content: {t})
def body(t) = p(font-size: 48px; color: $ink; in: row; content: {t})
def note(t) = p(font-size: 36px; font-family: m; color: $mute; in: note; content: {t})
def pill(t) = p(font-size: 39px; font-family: e; color: #12161C; background: $a; border-radius: 12px; padding: 9px 24px; in: pop; content: {t})
def dimrow(k,v,c=$a) = div(width: 780px; height: 126px)
  p#k(left: 42px; cy: 50%; font-size: 42px; font-family: m; color: $mute; content: {k})
  p#v(right: 42px; cy: 50%; font-size: 66px; font-family: e; color: {c}; content: {v})
# 流れ図の札 (×N で並べる・間の矢印は shape を位置の式 `札[k].right+N` で置く)
def node(t, i, c=$a) = div(width: 330px; height: 330px)
  icon#i(cx: 50%; top: 54px; font-size: 114px; name: {i}; color: {c})
  p#t(left: 0px; top: 210px; width: 100%; font-size: 42px; color: $ink; text-align: center; content: {t})
image part = "[photo]アルミ削り出しの L 字ブラケット部品、丸い穴が 2 つ、斜め上からの眺め、グラファイトの背景"
backdrop#bd(look: grid; spacing: 40; vignette: 0.25; drift: none)
subtitle.hug(font-size: 42px; bottom: 33px; background: #0B0D11E8; color: $ink; border-radius: 9px; padding: 12px 36px; border: 2px solid $line)
bgm#music 軽やかで前向きなミニマルエレクトロニカ、柔らかいシンセとクリーンなビート、ビジネス向けの解説動画
bgm#music2(volume: 1dB) 同じ系統で少し明るく推進力のあるエレクトロニカ、ビートを足して前向きに高揚する、まとめ向け

section#open
img#op_bg(inset: 0; scrim: 0.55; main: kb {scale: [1, 1.06], focus: ['60% 50%', '62% 50%']}) [photo][ref:@part]同じ部品、右半分は橙に光る線のワイヤーフレーム、左半分は青緑の細かい光の点の集まりに分かれていく、グラファイトの背景
num#op_n(left: 120px; top: 210px) CAD MODELING / REVERSE MODELING
h1#op_h(left: 120px; top: 276px; font-size: 96px) {a}CADモデリング{/}と[br]{b}リバースモデリング{/}
shape#op_r(left: 120px; top: 534px; width: 240px; height: 4px; path: line_h; background: $a; border: 4px solid $a; in: wipe {dir: 'right', duration: 0.7})
pill#op_f(left: 120px; top: 588px) アイデア → 3Dデータ
pill#op_g(left: 120px; top: 684px; background: $b; in: slide {dir: 'left'}) 実物 → 3Dデータ
sub#op_s(left: 120px; top: 810px) ちがいは、進む{k}向き{/}

section#goal
img#gl_bg(inset: 0; scrim: 0.6; main: kb {scale: [1, 1.05], focus: ['50% 50%', '']}) [photo][ref:@part]同じ部品の3Dモデルが大きなモニターに表示された作業机、暗い部屋、モニターの光
num#gl_n(left: 120px; top: 165px) COMMON
h1#gl_h(left: 120px; top: 225px) ゴールは同じ
div#gl_c(left: 120px; top: 390px; width: 840px; height: 225px; in: rise {y: 36, duration: 0.5})
  shape#bg(left: 42px; cy: 50%; width: 132px; height: 132px; path: rect,r=0.5; background: $a_t)
  icon#i(left: 69px; cy: 50%; font-size: 78px; name: cube; color: $a)
  p#t(left: 210px; cy: 50%; font-size: 51px; color: $ink; line-height: 1.3) パソコンの中の[br]部品の3Dデータ
body#gl_q(left: 120px; top: 690px) ちがうのは {k}出発点{/}
shape#gl_o(left: 1230px; top: 180px; width: 570px; height: 570px; border-radius: 50%; background: none; border: 3px solid $b; opacity: 0.25; main: breathe)

section#f_intro
img#fi_bg(inset: 0; scrim: 0.5; main: kb {scale: [1, 1.06], focus: ['65% 50%', '68% 48%']}) [photo]方眼紙に描いた鉛筆のスケッチから、橙に光る線の L 字ブラケットの3Dモデルが立ち上がる様子、グラファイトの机
num#fi_n(left: 120px; top: 225px) 01  FORWARD
h1#fi_h(left: 120px; top: 285px; font-size: 96px) 通常の[br]{a}CADモデリング{/}
shape#fi_r(left: 120px; top: 555px; width: 240px; height: 4px; path: line_h; background: $a; border: 4px solid $a; in: wipe {dir: 'right', duration: 0.7})
sub#fi_s(left: 120px; top: 600px) アイデアから、{k}ゼロで{/}形を組み立てる
pill#fi_p(left: 120px; top: 705px) アイデア → 3Dデータ

section#f_flow
img#ff_bg(inset: 0; scrim: 0.6) [photo][ref:@part]同じ部品が工場の CNC 加工機で削り出される様子、金属の切り粉、暗い工場
num#ff_n(left: 120px; top: 135px) FORWARD  FLOW
h1#ff_h(left: 120px; top: 192px; font-size: 72px) 描いて、決めて、{a}形にする{/}
node#ff_f(left: 120px; top: 420px; width: 1680px; height: 330px; display: flex; gap: 120px; t: "スケッチ;寸法を決める;立体にする;製品をつくる"; i: "pencil-simple;ruler;cube;factory") ×4
shape#ff_a(left: "ff_f[1].right+18;ff_f[2].right+18;ff_f[3].right+18"; cy: ff_f[1].cy; width: 84px; height: 54px; path: arrow_r; background: $a; border: 6px solid $a; in: wipe {dir: 'right', duration: 0.3}) ×3

section#f_dim
img#fd_bg(inset: 0; scrim: 0.6; main: kb {scale: [1.04, 1], focus: '70% 50%'}) [photo][ref:@part]同じ部品の橙の線のワイヤーフレーム、設計図のような寸法線が添えられている、グラファイト
num#fd_n(left: 120px; top: 150px) POINT
h1#fd_h(left: 120px; top: 210px) 寸法は {a}狙った値{/}
dimrow#fd_v1(left: 120px; top: 375px; k: "穴の直径"; v: "10.00 mm")
dimrow#fd_v2(left: 120px; top: 525px; k: "幅"; v: "50.00 mm")
p#fd_st(left: 120px; top: 705px; font-size: 45px; color: $ink; background: $a_t; border: 3px solid $a; border-radius: 15px; padding: 15px 33px; in: pop) 設計者が決めた数字 = データ

section#f_use
img#fu_bg(inset: 0; scrim: 0.55; main: kb {scale: [1, 1.05], focus: ['50% 50%', '']}) [photo]新しい製品の試作品がいくつか並ぶ開発室の机、3D プリンタ、暖かい光
note#fu_n(left: 120px; top: 225px) 通常の CAD が向いているのは
div#fu_c(left: 120px; top: 300px; width: 960px; height: 225px; in: rise {y: 36, duration: 0.5})
  shape#bg(left: 42px; cy: 50%; width: 132px; height: 132px; path: rect,r=0.5; background: $a_t)
  icon#i(left: 69px; cy: 50%; font-size: 78px; name: lightbulb; color: $a)
  p#t(left: 210px; cy: 50%; font-size: 54px; color: $ink; line-height: 1.3) 新しい製品を[br]一から設計する
pill#fu_p(left: 120px; top: 585px; transform: rotate(-4deg)) NEW DESIGN

section#r_intro
img#ri_bg(inset: 0; scrim: 0.5; main: kb {scale: [1, 1.06], focus: ['65% 50%', '66% 52%']}) [photo][ref:@part]同じ部品の使い込まれた実物、表面に細かな傷と摩耗、作業台の上に置かれている、横からの柔らかい光
num#ri_n(left: 120px; top: 225px; color: $b) 02  REVERSE
h1#ri_h(left: 120px; top: 285px; font-size: 96px) {b}リバース[br]モデリング{/}
shape#ri_r(left: 120px; top: 555px; width: 240px; height: 4px; path: line_h; background: $b; border: 4px solid $b; in: wipe {dir: 'left', duration: 0.7})
sub#ri_s(left: 120px; top: 600px) {k}今ある実物{/}から出発する
pill#ri_p(left: 120px; top: 705px; background: $b) 実物 → 3Dデータ

section#r_scan
img#rs_bg(inset: 0; scrim: 0.45; main: kb {scale: [1, 1.08], focus: ['60% 50%', '62% 48%']}) [photo][ref:@part]同じ部品に青緑の縞模様の光を当てる据え置き型の3Dスキャナー、暗い作業室
pill#rs_t(left: 120px; top: 165px; background: $b) STEP 1  測る
h1#rs_h(left: 120px; top: 255px; font-size: 72px) 3Dスキャナーで{b}測る{/}
div#rs_c(left: 120px; top: 420px; width: 720px; height: 300px; in: rise {y: 36, duration: 0.5})
  p#v(left: 42px; top: 39px; font-size: 108px; font-family: e; color: $b) [count:300,000]
  p#k(left: 45px; top: 186px; font-size: 39px; font-family: m; color: $mute) 点の位置を一気に読み取る (例)

section#r_mesh
img#rm_bg(inset: 0; scrim: 0.4; main: kb {scale: [1, 1.05], focus: ['30% 50%', '30% 50%']}) [photo][ref:@part]同じ部品の形をした青緑の細かい光の点の集まり、点群、暗い空間に浮かぶ
pill#rm_t(left: 120px; top: 135px; background: $b) STEP 2  つなぐ
h1#rm_h(left: 120px; top: 219px; font-size: 72px) 点 → {b}三角形の面{/}
pill#rm_l1(left: 120px; top: 780px; background: #12161C; color: $b; border: 3px solid $b) 点群
shape#rm_a(left: 840px; top: 495px; width: 210px; height: 90px; path: arrow_r; background: $b; border: none; in: wipe {dir: 'right', duration: 0.5})
div#rm_m(left: 1110px; top: 225px; width: 690px; height: 540px; in: zoom)
  img#img(left: 0px; top: 0px; width: 690px; height: 540px) [photo][ref:@part]同じ部品の形をした細かい三角形のポリゴンメッシュ、青緑の線、暗い空間
pill#rm_l2(left: 1140px; top: 795px; background: $b) メッシュ

section#r_cad
img#rc_bg(inset: 0; scrim: 0.6; main: kb {scale: [1, 1.05], focus: ['50% 50%', '']}) [photo][ref:@part]同じ部品、左半分は青緑の三角形メッシュ、右半分はなめらかな面のきれいな3Dモデル、境目がはっきり
pill#rc_t(left: 120px; top: 135px; background: $b) STEP 3  当てはめる
h1#rc_h(left: 120px; top: 219px; font-size: 72px) メッシュに{b}形の意味{/}を与える
note#rc_w(left: 120px; top: 339px) メッシュ = {x}表面の形だけ{/}
div#rc_c(left: 120px; top: 435px; width: 1140px; height: 165px; gap: 24; display: flex) ×2
  icon#i(left: 36px; cy: 50%; font-size: 66px; name: "square;cylinder"; color: $b)
  p#t(left: 126px; cy: 50%; font-size: 45px; color: $ink) 平らな所 → 平面;丸い所 → 円筒
p#rc_st(left: 120px; top: 675px; font-size: 48px; color: $ink; background: $b_t; border: 3px solid $b; border-radius: 15px; padding: 15px 33px; in: pop) 編集できる CAD データへ

section#r_dim
img#rd_bg(inset: 0; scrim: 0.6; main: kb {scale: [1.04, 1], focus: '70% 50%'}) [photo][ref:@part]同じ部品の実物の穴のアップ、わずかな摩耗とバリ、金属のノギスが当てられている
num#rd_n(left: 120px; top: 150px; color: $b) POINT
h1#rd_h(left: 120px; top: 210px) 寸法は {b}測った値{/}
dimrow#rd_v1(left: 120px; top: 375px; k: "穴の直径"; v: "10.03 mm"; c: $b)
dimrow#rd_v2(left: 120px; top: 525px; k: "幅"; v: "49.80 mm"; c: $b)
p#rd_m(left: 120px; top: 705px; font-size: 45px; color: $ink) 実物の{w}ズレや摩耗{/}も、そのまま入る

section#r_use
img#ru_bg(inset: 0; scrim: 0.6; main: kb {scale: [1, 1.05], focus: ['50% 50%', '']}) [photo]棚に並んだ古い機械部品と、手で削った木の試作品、柔らかい光の作業場
note#ru_n(left: 120px; top: 144px) リバースが活きる場面
div#ru_c(left: 120px; top: 225px; width: 1050px; height: 600px; gap: 20; display: flex; flex-direction: column) ×3
  shape#bg(left: 30px; cy: 50%; width: 96px; height: 96px; path: rect,r=0.5; background: $b_t)
  icon#i(left: 51px; cy: 50%; font-size: 54px; name: "clock-counter-clockwise;hand;puzzle-piece"; color: $b)
  p#t(left: 162px; cy: 50%; font-size: 48px; color: $ink) 図面のない古い部品;手作りの試作品;実物どうしの合わせ

section#cmp
img#cm_bg(inset: 0; scrim: 0.6) [photo][ref:@part]同じ部品が 2 つ向かい合う、左は橙に光る線のワイヤーフレーム、右は青緑の光の点群
num#cm_n(left: 120px; top: 90px; color: $ink) 03  COMPARE
div#cm_l(left: 120px; top: 165px; width: 810px; height: 705px; border: 3px solid $a)
  p#t(left: 48px; top: 42px; font-size: 60px; color: $a) 通常の CAD
  div#r(left: 36px; top: 156px; width: 738px; height: 510px; border: none; background: $a_t; display: flex; flex-direction: column; gap: 21px) ×3
    p#k(left: 36px; cy: 50%; font-size: 36px; font-family: m; color: $mute) 出発点;寸法;得意
    p#v(left: 192px; cy: 50%; font-size: 51px; color: $ink) アイデア・図面;狙った値;新しくつくる
div#cm_r(left: 990px; top: 165px; width: 810px; height: 705px; border: 3px solid $b)
  p#t(left: 48px; top: 42px; font-size: 60px; color: $b) リバース
  div#r(left: 36px; top: 156px; width: 738px; height: 510px; border: none; background: $b_t; display: flex; flex-direction: column; gap: 21px) ×3
    p#k(left: 36px; cy: 50%; font-size: 36px; font-family: m; color: $mute) 出発点;寸法;得意
    p#v(left: 192px; cy: 50%; font-size: 51px; color: $ink) 実物;測った値;今あるものを写す

section#combo
img#cb_bg(inset: 0; scrim: 0.6; main: kb {scale: [1, 1.05], focus: ['50% 50%', '']}) [photo][ref:@part]同じ部品の実物の隣で、改良された新しい形の部品の3Dモデルがモニターに映る、作業机
num#cb_n(left: 120px; top: 135px) IN PRACTICE
h1#cb_h(left: 120px; top: 192px; font-size: 72px) {b}写して{/}、{a}描き足す{/}
node#cb_f(left: 120px; top: 420px; width: 1680px; height: 330px; display: flex; gap: 120px; t: "実物;スキャン;CAD で改良;新しい製品"; i: "package;scan;pencil-simple;rocket-launch"; c: "$b;$b;$a;$a") ×4
shape#cb_a(left: "cb_f[1].right+18;cb_f[2].right+18;cb_f[3].right+18"; cy: cb_f[1].cy; width: 84px; height: 54px; path: arrow_r; background: "$b;$a;$a"; border: 6px solid $a; in: wipe {dir: 'right', duration: 0.3}) ×3

section#close
img#cl_bg(inset: 0; scrim: 0.6; main: kb {scale: [1, 1.06], focus: ['50% 50%', '']}) [photo][ref:@part]同じ部品が、橙の線のワイヤーフレームと青緑の点群から一つの完成品に重なっていく、明るく澄んだ光
div#cl_a(left: 120px; top: 165px; width: 810px; height: 375px; border: 3px solid $a; in: slide {dir: 'left'})
  p#k(left: 54px; top: 54px; font-size: 39px; font-family: e; color: $a; letter-spacing: 0.15em) 通常の CAD
  p#v(left: 54px; top: 150px; font-size: 78px; color: $ink) アイデア → 形
div#cl_b(left: 990px; top: 165px; width: 810px; height: 375px; border: 3px solid $b; in: slide {dir: 'right'})
  p#k(left: 54px; top: 54px; font-size: 39px; font-family: e; color: $b; letter-spacing: 0.15em) リバース
  p#v(left: 54px; top: 150px; font-size: 78px; color: $ink) 形 → データ
p#cl_t(left: 120px; top: 630px; width: 1680px; font-size: 66px; color: $ink; text-align: center; in: rise) {k}向き{/}のちがいで、使い分ける
```

```timeline.txt
#v2
cast narrator = "落ち着いた30代女性のナレーター、明るく親しみやすい解説口調、はっきりした発音" speed=108% manner="語りかけるように、やわらかく"
transition = dissolve,300,overlap=300,zoom=1.04,ease=power2.out

*** open
[>#subtitle]
bgm music
@narrator: [silence:+0.3s]CADモデリングと、リバースモデリング。何がちがうのでしょう。
@: [>#op_f]どちらも3Dデータを作る方法ですが、[>#op_g][>#op_s]進む向きが、[!#op_g punch][!#op_s{k} recolor,$a]正反対なんです。

*** goal
@narrator: [silence:+0.3s]まずは共通点から。どちらも最後は、パソコンの中に、[>#gl_c]部品の3Dデータを[!#gl_c check]作ります。
@: [>#gl_q]ちがうのは、[!#gl_q{k} recolor,$a]どこから出発するか、です。[silence:+0.6s]
transition wipe,600,dir=left

*** f_intro
@narrator: [silence:+0.3s]一つ目は、通常のCADモデリング。
@: 頭の中のイメージや図面をもとに、[>#fi_s]ゼロから[!#fi_s{k} recolor,$a +300]形を組み立てる方法です。[>#fi_p]

*** f_flow
@narrator: [silence:+0.3s]流れはシンプルです。[>#ff_f[1]]スケッチを描き、[>#ff_a[1]][>#ff_f[2]]寸法を決めて、[>#ff_a[2]][>#ff_f[3]]押し出しや穴あけで立体にします。
@: [>#ff_a[3]][>#ff_f[4]]そのデータをもとに、[!#ff_f[4] tint,$a]製品を作ります。

*** f_dim
@narrator: [silence:+0.3s]ポイントは、寸法がすべて「狙った値」だということ。
@: [>#fd_v1]穴の直径は10ミリ、[>#fd_v2]幅は50ミリ。[!#fd_v1 frame,$a]
@: 設計者が決めた数字が、[>#fd_st]そのまま[!#fd_st punch +500]データになります。

*** f_use
@narrator: [silence:+0.3s]だから、[>#fu_c]新しい製品を[>#fu_p +600]一から設計するときに、[!#fu_c tint,$a]ぴったりです。[silence:+0.6s]
transition wipe,600,dir=left

*** r_intro
@narrator: [silence:+0.3s]二つ目は、リバースモデリング。こちらは、向きが逆です。
@: [>#ri_s]すでにある[!#ri_s{k} recolor,$b +300]実物から出発して、[>#ri_p]3Dデータを作り直します。

*** r_scan
se "静かな作業室の空調の音、低い機械のうなり" -8dB to=10s fade=300,1500
@narrator: [silence:+0.3s][>#rs_h]まずは、3Dスキャナーで実物を[>#rs_t]測ります。
@: [♪"スキャナーが光を走らせる短い電子音" -6dB][!#rs_bg zoom_media,1.1]表面に光を当てて、[>#rs_c]何十万もの点の位置を、[!#rs_c pulse]一気に読み取ります。

*** r_mesh
@narrator: [silence:+0.3s]読み取った点の集まりを、[>#rm_l1]{点群|てんぐん}と呼びます。
@: [>#rm_a][>#rm_t][>#rm_h]点と点をつなぐと、[>#rm_m]細かい三角形で覆われた、[>#rm_l2][!#rm_m frame,$b]メッシュになります。

*** r_cad
@narrator: [silence:+0.3s]ただし、[>#rc_w]メッシュは、あくまで[!#rc_w{x} recolor,$b]表面の形だけ。
@: そこで、[>#rc_c[1]]平らな所には平面、[>#rc_c[2]]丸い所には円筒を[>#rc_t]当てはめて、[>#rc_st]編集できるCADデータに作り直します。
@: [!#rc_st punch]ここが、リバースモデリングの中心です。

*** r_dim
@narrator: [silence:+0.3s]そして、ここでの寸法は「測った値」です。
@: [>#rd_v1]穴は10.03ミリ、[>#rd_v2]幅は49.8ミリ。[!#rd_v1 frame,$b]
@: [>#rd_m]実物のわずかな[!#rd_m{w} marker,$b]ズレや摩耗も、データに入ってきます。

*** r_use
@narrator: [silence:+0.3s][>#ru_n]リバースモデリングが役立つのは、[>#ru_c[1] check]図面が残っていない、古い部品の復元。
@: [>#ru_c[2] check]手で作った試作品のデータ化。[>#ru_c[3] check]そして、実物どうしの合わせの確認です。[silence:+0.6s]
transition wipe,600,dir=left

*** cmp
@narrator: [silence:+0.3s]二つを並べてみましょう。
@: 出発点は、[>#cm_l.r[1]]アイデアと、[>#cm_r.r[1]]実物。
@: 寸法は、[>#cm_l.r[2]]狙った値と、[>#cm_r.r[2]]測った値。
@: 得意なのは、[>#cm_l.r[3]]新しくつくることと、[>#cm_r.r[3]]今あるものを写し取ることです。
[<#music]

*** combo
bgm music2 -1500
@narrator: [silence:+0.3s]実際の現場では、二つを組み合わせることも多いです。
@: [>#cb_f[1]]実物を[>#cb_a[1]][>#cb_f[2]]スキャンして形を取り込み、[>#cb_a[2]][>#cb_f[3]]そこに新しい設計を足していく。
@: [>#cb_a[3]][>#cb_f[4]][!#cb_f[4] tint,$a]良いところ取りの使い方です。

*** close
@narrator: [silence:+0.3s]まとめると、[>#cl_a]通常のCADは、アイデアから形へ。
@: [>#cl_b]リバースモデリングは、形からデータへ。
@: [>#cl_t]向きのちがいを押さえれば、[!#cl_t{k} recolor,$a]どちらを使うかが、見えてきます。[silence:3.0s]
```

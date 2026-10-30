# concept · オイラー積と素数の無限性 (横・式と札だけ・数式の書体の役 f・上付きは Unicode) — canvas 1920x1080・46.5s・check warn 0 (未審査・手書き)

見せる文法: 数式の書体の役 (`fonts f=` に式を全部) ・上付きの Unicode 文字 (2⁻ˢ・p⁻²ˢ・ζ(s))・def (eq / term)・位置の式 (`z_b.right+24`)・run・`lint off`

```design.txt
#v2
# 計画: 暗い紺の地 + 細い方眼・主色は青緑 (式の記号)・差し色は琥珀 (結論の強調)
# 書体 太い角ゴシック (見出し) + 数式向けの欧文セリフ体 (式は全部この役 f) + 細い角ゴシック (本文・注記)・絵なし・式と札だけ
canvas 1920x1080 bg=#0E1626
theme dark
palette a=#5EE7D5 b=#F2B84B ink=#F3F6FA paper=#0E1626 mute=#8FA0B8 line=#2A3850 card=#16213A
font "太い角ゴシック体、すっきりした現代的な印象"
fonts f="数式向けの欧文セリフ体 (Times 系)、変数はイタリック、ギリシャ文字と数学記号が揃う" m="細い角ゴシック体、本文向き"
motion title { in: {y:-36, opacity:0, duration:0.7, ease:'power3.out'}; out: fade {duration:0.3} }
motion big { in: {scale:0.94, opacity:0, duration:0.6, ease:'power3.out'}; out: fade {duration:0.3} }
motion div { in: {y:27, opacity:0, duration:0.6, ease:'power3.out'}; out: fade {duration:0.26} }
motion row { in: {x:-45, opacity:0, duration:0.5, ease:'power3.out'}; out: fade {duration:0.24} }
motion note { in: {opacity:0, duration:0.45, ease:'power2.out'}; out: fade {duration:0.24} }
div { in: div; border-radius: 18px; background: $card; border: 2px solid $line }
cut { stagger: sentence }
lint off=text_only_cut,sparse_cut,cut_head_gap   # 式と札だけの動画: 絵の無い cut・余白・頭の小さな面積は意図した物
run a { color: $a }
run b { color: $b }
def kick(t) = p(font-size: 30px; font-family: m; color: $a; letter-spacing: 0.2em; in: note; content: {t})
def h1(t) = p(font-size: 90px; line-height: 1.2; color: $ink; in: title; content: {t})
# 式は全部この役 (書体 f)。上付きは Unicode の上付き文字 (2ˢ・p⁻ˢ・x²)・^ は使わない
def eq(t) = p(font-size: 96px; line-height: 1.25; font-family: f; color: $ink; in: big; content: {t})
def body(t) = p(font-size: 48px; font-family: m; color: $ink; in: row; content: {t})
def note(t) = p(font-size: 36px; font-family: m; color: $mute; in: note; content: {t})
def chip(t) = p(font-size: 48px; color: $ink; background: $card; border: 2px solid $line; border-radius: 120px; padding: 18px 48px; text-align: center; in: pop; content: {t})
# 級数の項の札: 式の書体の 1 項 (札は横に並べ、印は 1 枚ずつ)
def term(t, c=$ink) = div(width: 250px; height: 130px)
  p#t(left: 0px; cy: 50%; width: 250px; font-size: 64px; font-family: f; color: {c}; text-align: center; content: {t})
bgm#music 静かな電子音のパッドとピアノの単音、ゆっくりした知的な解説向け、控えめ
subtitle.hug(font-size: 42px; font-family: m; bottom: 36px; background: #0E1626E6; color: $ink; border-radius: 9px; padding: 12px 36px)

section#hook
div#h_grid(inset: 0; pattern: grid,60,#5EE7D51A; background: none; border: none; border-radius: 0px; in: none)
kick#h_k(left: 120px; top: 150px) EULER PRODUCT
h1#h_h(left: 120px; top: 220px; width: 1680px) 素数は、[br]どこまで続くのか
eq#h_eq(left: 120px; top: 600px; width: 1680px; font-size: 88px) ζ(s) = 1 + 1/2ˢ + 1/3ˢ + 1/4ˢ + 1/5ˢ + ⋯
note#h_n(left: 120px; top: 780px) 18 世紀、レオンハルト・オイラーの一本の式

section#zeta
div#z_grid(inset: 0; pattern: grid,60,#5EE7D51A; background: none; border: none; border-radius: 0px; in: none)
kick#z_k(left: 120px; top: 150px) ZETA FUNCTION
h1#z_h(left: 120px; top: 220px) ゼータ関数 {a}ζ(s){/}
eq#z_eq(left: 120px; top: 390px) ζ(s) = Σ n⁻ˢ　(n = 1, 2, 3, …)
term#z_t1(left: 120px; top: 620px) 1
term#z_t2(left: 400px; top: 620px) 2⁻ˢ
term#z_t3(left: 680px; top: 620px) 3⁻ˢ
term#z_t4(left: 960px; top: 620px) 4⁻ˢ
term#z_t5(left: 1240px; top: 620px) 5⁻ˢ
term#z_t6(left: 1520px; top: 620px) 6⁻ˢ
body#z_b(left: 120px; top: 820px) すべての自然数の {a}s 乗の逆数{/} を、
body#z_b2(left: z_b.right+24; top: 820px) ぜんぶ足した和

section#factor
div#f_grid(inset: 0; pattern: grid,60,#5EE7D51A; background: none; border: none; border-radius: 0px; in: none)
kick#f_k(left: 120px; top: 150px) UNIQUE FACTORIZATION
h1#f_h(left: 120px; top: 220px) 自然数は、素数の積
eq#f_e1(left: 120px; top: 390px; font-size: 80px) 6⁻ˢ = 2⁻ˢ · 3⁻ˢ
eq#f_e2(left: 120px; top: 510px; font-size: 80px) 12⁻ˢ = 2⁻²ˢ · 3⁻ˢ
body#f_b(left: 120px; top: 660px) 素因数分解は {a}ただ一通り{/}
term#f_p2(left: 120px; top: 760px; c: $a) 2⁻ˢ
term#f_p3(left: 400px; top: 760px; c: $a) 3⁻ˢ
term#f_p5(left: 680px; top: 760px; c: $a) 5⁻ˢ
term#f_p7(left: 960px; top: 760px; c: $a) 7⁻ˢ
note#f_n(left: 1240px; top: 800px) 素数の項だけで、すべての自然数が作れる

section#product
div#p_grid(inset: 0; pattern: grid,60,#5EE7D51A; background: none; border: none; border-radius: 0px; in: none)
kick#p_k(left: 120px; top: 150px) EULER PRODUCT
h1#p_h(left: 120px; top: 220px) オイラー積
eq#p_eq(left: 120px; top: 390px) ζ(s) = {a}Π{/} 1 / (1 − p⁻ˢ)　(p は素数)
eq#p_geo(left: 120px; top: 530px; font-size: 64px; color: $mute) 1 / (1 − p⁻ˢ) = 1 + p⁻ˢ + p⁻²ˢ + p⁻³ˢ + ⋯
body#p_b(left: 120px; top: 660px) 素数ごとの等比級数を掛け合わせると、自然数が {a}一度ずつ{/} 現れる
chip#p_l(left: 120px; top: 780px; width: 520px) 自然数の和
shape#p_ar(left: 700px; top: 815px; width: 160px; height: 60px; path: arrow_r,head=line; background: none; border: 4px solid $a; in: wipe {dir: 'right', duration: 0.5})
chip#p_r(left: 920px; top: 780px; width: 520px) 素数の積

section#close
div#c_grid(inset: 0; pattern: grid,60,#5EE7D51A; background: none; border: none; border-radius: 0px; in: none)
kick#c_k(left: 120px; top: 150px) CONCLUSION
h1#c_h(left: 120px; top: 220px) だから、素数は {b}無限{/} にある
eq#c_eq(left: 120px; top: 390px) ζ(1) = 1 + 1/2 + 1/3 + 1/4 + ⋯ = ∞
body#c_b1(left: 120px; top: 560px) s = 1 なら、左辺は {a}発散{/} する
body#c_b2(left: 120px; top: 650px) 素数が有限なら、右辺は有限の積のまま
chip#c_x(left: 120px; top: 760px; color: $b; border: 2px solid $b) 矛盾
note#c_n(left: 400px; top: 790px) オイラー、1737 年
```

```timeline.txt
#v2
cast narrator = "落ち着いた30代男性のナレーター、低めで明瞭、知的で静かな語り口" speed=100%
transition = dissolve,300,overlap=300

*** hook
[>#subtitle]
bgm music
@narrator: [silence:+0.3s]素数は、どこまで続くのでしょうか。[silence:0.3s]
@: [>#h_n]この一本の式が、答えを教えてくれます。[silence:0.5s]

*** zeta
@narrator: [silence:+0.3s]ゼータ関数は、[>#z_b]自然数のエス乗の逆数を、[>#z_t1][>#z_t2 +150][>#z_t3 +300][>#z_t4 +450][>#z_t5 +600][>#z_t6 +750]ぜんぶ[>#z_b2]足した和です。[silence:+1.0s]

*** factor
@narrator: [silence:+0.3s]どんな自然数も、素数の積に[>#f_e2]ただ一通りに分解できます。[silence:0.3s]
@: [>#f_b]だから各項は、[>#f_p2][>#f_p3 +150][>#f_p5 +300][>#f_p7 +450][>#f_n +900]素数の項の掛け算にほどけます。[silence:+0.8s]

*** product
@narrator: [silence:+0.3s]オイラー積。[>#p_geo]素数ごとの等比級数をぜんぶ掛け合わせると、自然数の和に戻ります。[silence:0.3s]
@: [>#p_b][>#p_l]左の和と[>#p_ar][>#p_r]右の積が、同じものになる。[!#p_eq{a} recolor,$b]これが、オイラー積です。[silence:+0.8s]
transition dissolve,400,overlap=400

*** close
@narrator: [silence:+0.3s]エスを1にすると、左辺は[>#c_b1]無限大に発散します。[silence:0.3s]
@: [>#c_b2]もし素数が有限なら、右辺は有限の積のまま。[>#c_x]矛盾です。[silence:0.3s]
@: だから素数は、[>#c_n]無限にある。[silence:2.5s]
```

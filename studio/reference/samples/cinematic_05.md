# cinematic · 奥多摩の渓流の朝 (横・実写調・台詞 5 文の観光 PR) — canvas 1920x1080・33.0s

見せる文法: 常設の質感 (根の veil の周辺減光と grain)・絵の置き場 (subject / room)・同じ cut で絵を重ねて替える (2 枚目を fade で)・count・recolor・filter・hide_subtitle・read・場の音 (se to= fade=)・bgm

```design.txt
#v2
# 計画: 静かな高級の組 — 黒に近い深い緑の地・白の明朝・差し色は朝の光の淡い金 1 色。台詞は 5 文、映像と場の音で見せる
# 文字は少なく、細い明朝を余白の中に。全編に周辺減光と grain の常設の質感・上下の細い黒帯
canvas 1920x1080 bg=#060A08
theme dark
palette a=#E8C987 ink=#F4F1EA mute=#A9B3AC deep=#060A08
font "細めで端正な明朝体、上品な映画のタイトル向け"
fonts n="細めのクラシックな欧文セリフ体、数字がはっきりした上品な字形"
art "実写の映画のワンシーン、35mm フィルム、浅い被写界深度、深い緑と青灰色の落ち着いた色調、柔らかい粒子、文字なし"
prompt_tail "文字なし、ロゴなし"
motion title { in: {y:24, opacity:0, duration:1.2, ease:'power2.out'}; out: fade {duration:0.5} }
motion big { in: {scale:0.97, opacity:0, duration:1.4, ease:'power2.out'}; out: fade {duration:0.5} }
motion div { in: {y:18, opacity:0, duration:0.9, ease:'power2.out'}; out: fade {duration:0.4} }
motion row { in: {x:-30, opacity:0, duration:0.8, ease:'power2.out'}; out: fade {duration:0.4} }
motion note { in: {opacity:0, duration:1.0, ease:'power2.out'}; out: fade {duration:0.4} }
img { out: none }
cut { stagger: sentence }
subtitle.hug(bottom: 51px; font-size: 39px; letter-spacing: 0.1em; color: $ink; background: none; text-shadow: 0px 0px 12px #000000E6; unit: sentence)
bgm#music 静かで透明なアンビエント、柔らかいピアノの単音と遠いパッド、朝の自然の映像向け、ゆっくり
sfx off
veil#vignette(background: radial(#00000000@50%,#00000080@100%,50%,50%); z-index: front; in: none)
veil#grain(grain: 0.05; color: #00000000; mix-blend-mode: overlay; z-index: front; in: none; main: noise {x: 4, y: 4, period: 0.083})

section#dawn
img#dawn_p(inset: 0; subject: right 45%; room: left 50%; main: kb {scale: [1.02, 1.1], focus: ['62% 55%', '58% 45%']}) 夜明け前の暗い奥多摩の渓流、画面の右側に青黒い岩と白く流れる沢、左側はほとんど光の無い深い森の影で静か、木々の隙間にかすかな青い空、人物なし
veil#dawn_v(background: linear(#060A08D9,#060A0899@40%,#060A0800@70%,90); in: none)
div#dawn_glow(inset: 0; background: radial(#E8C98738,#E8C98700@100%,82%,8%); mix-blend-mode: screen; in: {opacity:0, duration:2.4, ease:'power1.inOut'})
p#dawn_l(left: 150px; top: 294px; font-size: 36px; color: $a; letter-spacing: 0.4em; in: note) 奥多摩　沢の朝
p#dawn_t(left: 138px; top: 339px; font-size: 234px; font-family: n; color: $ink; letter-spacing: 0.05em; line-height: 1; text-shadow: 0px 0px 27px #000000B3; in: big) 4:00
shape#dawn_r(left: 150px; top: 627px; width: 210px; height: 3px; path: line_h; background: $a; border: 3px solid $a; in: wipe {dir: 'right', duration: 0.9})
p#dawn_s.hide_subtitle(left: 144px; top: 669px; width: 1080px; font-size: 96px; color: $ink; letter-spacing: 0.06em; text-shadow: 0px 0px 21px #000000CC; in: title) 沢は、まだ{m}眠っている{/}

section#mist
img#mist_a(inset: 0; main: kb {scale: [1.04, 1.1], focus: ['50% 40%', '55% 45%']}) 夜明け直後の奥多摩の渓谷、白く濃い朝靄が谷いっぱいに満ち、杉の森の輪郭が青灰色にかすむ、まだ日の差さない薄明、静まり返った沢
img#mist_b(inset: 0; subject: right 55%; room: left 45%; in: {opacity:0, duration:2.2, ease:'sine.inOut'}; main: kb {scale: [1.06, 1.12], focus: '60% 40%'}) 靄が薄くほどけていく奥多摩の渓谷、右奥の山の稜線から最初の朝日が差し込み淡い金色の光の筋が谷へ落ちる、澄んだ深い緑の杉林と光る沢、左側は靄の残る静かな影
div#mist_sun(inset: 0; background: radial(#E8C98770,#E8C98700@100%,74%,20%); mix-blend-mode: screen; in: {opacity:0, duration:2.6, ease:'sine.inOut'})
veil#mist_v(background: linear(#060A08C0,#060A0866@38%,#060A0800@62%,90); in: none)
p#mist_c(left: 150px; top: 180px; font-size: 66px; font-family: n; color: $a; letter-spacing: 0.08em; in: note) [count:4:40 start=4:00]
p#mist_h(left: 144px; top: 420px; font-size: 126px; color: $ink; letter-spacing: 0.12em; text-shadow: 0px 0px 27px #000000B3; in: big) 山が、目を覚ます。
shape#mist_r(left: 150px; top: 600px; width: 630px; height: 3px; path: line_h; background: $a; border: 3px solid $a; in: wipe {dir: 'right', duration: 1.2})

section#cast
img#cast_p(inset: 0; main: kb {scale: [1.1, 1.03], focus: ['40% 50%', '50% 45%']}) 夜明け直後の奥多摩の渓流、腰まで水に入った釣り人の後ろ姿の引き、竿を大きく振り上げた瞬間、画面右側は暗い杉の森の陰、川面に淡い朝の光、静かな青灰色
veil#cast_v(background: linear(#060A0800@35%,#060A08B8,90); in: fade {duration: .8})
p#cast_t(right: 144px; top: 225px; font-size: 114px; color: $a; letter-spacing: 0.24em; text-shadow: 0px 0px 24px #000000CC; in: title) 一投目
img#cast_q(inset: 0; in: {opacity:0, scale:1.04, duration:0.9, ease:'power2.out'}; main: kb {scale: [1.02, 1.1], focus: ['60% 40%', '45% 50%']}) 逆光の朝日を受けて金色に光る細い釣り糸の寄り、暗い森を背に宙に長い弧を描き、先の小さな仕掛けが水面に落ちて小さな水しぶきと波紋、浅い被写界深度、光の玉のボケ

section#light
img#light_a(inset: 0; main: kb {scale: [1.03, 1.1], focus: '60% 55%'}) 朝日にきらめく渓流の水面を低い位置から、画面の右半分に無数の光の粒が集まり、左側は木陰で暗く静かな水面、澄んだ浅瀬
img#light_b(inset: 0; in: {opacity:0, duration:1.4, ease:'sine.inOut'}; main: kb {scale: [1.05, 1.13], focus: ['60% 55%', '66% 52%']}) 澄んだ渓流の水中、画面の右寄りの岩陰をすっと泳ぐ一匹のヤマメの魚影、水面から斜めに差し込む光の筋、左側は青緑の深い水で暗く静か
veil#light_v(background: linear(#000000B3,#00000066@38%,#00000000@62%,90); in: none)
p#light_k(left: 144px; top: 210px; font-size: 225px; color: $a; line-height: 1.1; text-shadow: 0px 0px 42px #E8C98799; in: big) 光
p#light_s(left: 144px; top: 495px; font-size: 225px; color: $ink; line-height: 1.1; text-shadow: 0px 0px 27px #000000CC; in: {opacity:0, blur:18, duration:1.4, ease:'power2.out'}) 影
shape#light_ln(left: 150px; top: 795px; width: 270px; height: 6px; path: line_h; background: $a; border: 3px solid $a; in: wipe {dir: 'right', duration: 0.9})

section#close
img#close_p(inset: 0; subject: bottom 40%; room: top 60%; main: kb {scale: [1.02, 1.08], focus: ['50% 70%', '50% 55%']}) 朝の光に満ちた奥多摩の渓谷を高い尾根から見下ろす遠景、画面の下半分に静かな沢と重なる緑の山並み、上半分は淡い金色に明けていく空と薄く残る靄、穏やかで広い余白
veil#close_v(background: radial(#060A08B3,#060A0866@55%,#060A0800@100%,50%,42%,62%,48%); in: fade {duration: 1.2})
p#close_k.hide_subtitle(cx: 960px; top: 180px; font-size: 108px; color: $a; letter-spacing: 0.4em; text-shadow: 0px 0px 27px #000000CC; in: title) 奥多摩
p#close_c1.hide_subtitle(cx: 960px; top: 402px; font-size: 54px; color: $mute; letter-spacing: 0.2em; text-shadow: 0px 0px 18px #000000CC; in: note) 東京から2時間、
p#close_c2.hide_subtitle(cx: 960px; top: 504px; font-size: 144px; color: $ink; letter-spacing: 0.1em; text-shadow: 0px 0px 30px #000000D9; in: big) 音のない{m}朝{/}。
shape#close_r(left: 780px; top: 729px; width: 360px; height: 3px; path: line_h; background: $a; border: 2px solid $a; in: wipe {dir: 'center', duration: 1.2})
```

```timeline.txt
#v2
cast n = "低く落ち着いた40代男性のナレーター、深く柔らかい声" speed=90% manner="ゆっくり、間を大きく取って静かに語る"
transition = dissolve {duration: .3, overlap: .3, ease: 'power2.inOut'}
read 奥多摩 = おくたま

*** dawn
[>#subtitle]
fade in,1200ms
bgm music
se "夜明け前の渓流のせせらぎ、静かな水の音" -8dB to=8s fade=800ms,1500ms
[>#dawn_l +600ms]
@n: [silence:1.5s][>#dawn_t]朝、[>#dawn_r]四時。[>#dawn_s][!#dawn_t dim {opacity: .55, duration: .9}]沢は、まだ眠っている。[silence:0.3s][>#dawn_glow][!#dawn_s{m} recolor,$a {duration: 1.2}][silence:0.9s]

*** mist
se "朝の森の鳥のさえずり、遠くの沢の音" -8dB to=9s fade=600ms,1500ms
@n: [silence:0.8s]靄が、[>#mist_b][>#mist_sun +300ms][♪"朝の森で鳥が一羽鳴き出す澄んだ声" -6dB +400ms]ほどけていく。[silence:0.6s][>#mist_h][>#mist_r][silence:2.4s]

*** cast
se "渓流の水音と森の鳥の声" -8dB to=8s fade=400ms,1500ms
@n: [silence:0.6s][♪"釣り竿を振るヒュッという風切り音" -4dB][>#cast_t]一投目。[>#cast_q][<#cast_t][<#cast_v][♪"小さな仕掛けが水面に落ちるポチャンという音" -6dB +600ms]糸が、[!#cast_q to,{filter:'brightness(1.2)', duration:.9}]光をひいた。[silence:1.5s]

*** light
se "浅瀬を流れる澄んだ水の音、ときどき鳥の声" -8dB to=10s fade=400ms,1500ms
@n: [silence:1.0s]水面に、[>#light_k]光。[silence:0.8s][>#light_b]その下を、[>#light_s][!#light_k recolor,$mute {duration: .9}][♪"水中を魚がすっと横切る小さな水の揺らぎの音" -8dB]影がよぎる。[silence:1.0s][>#light_ln][silence:1.0s]

*** close
se "静かな渓流の水音と朝の鳥のさえずり" -8dB to=11s fade=600ms,2500ms
@n: [silence:0.8s][>#close_k]奥多摩。[silence:0.6s][>#close_c1]東京から2時間、[>#close_c2]音のない朝。[silence:1.0s][>#close_r][!#close_c2{m} recolor,$a {duration: 1.2}][silence:2.0s]
```

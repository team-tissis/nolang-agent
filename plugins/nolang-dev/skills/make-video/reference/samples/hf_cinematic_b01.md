# cinematic · sake-brand (hf 全力版の全量の写し — 架空の日本酒ブランド「田恵」のブランドPR動画・田から杯までの全面写真 16 枚を語と無音の拍で切るシネマティックCM) — canvas 1080x1920

見せる作り: 黒から明ける頭と全編の周辺減光・動く grain・場面の中で語と無音の拍に硬く切る全面写真 (写真ごとに向きの違う kb)・右上の縦組みの明朝 2 列 (1 字ずつぼけから滲む・暗い楕円の陰)・朝日の光の玉と前景のぼけた稲穂・流れる朝霧・立ちのぼる湯気の透過 2 枚・着水の金の波紋 3 重・黒い幕の暗転から明ける瓶と流れる光の帯・同じ絵の寄り・締めの縦組みの社名 (1 字ずつ・落款・伸びる罫・欧文) と暗転・音の層 (場の音 4 + 語に結んだ foley 9 + 太鼓の一打)

```design.txt
#v2
# 学ぶ作り: 声の無い間も絵が語るシネマティック — 1 つの場面 (cut) の中で全面写真を語と無音の拍で硬く切り替え、写真ごとに違う向きの kb (寄り・引き・横と縦の pan) を付ける
# 字幕の代わりに右上の縦組みの明朝 2 列 (台詞と同じ文・1 字ずつぼけから滲み、まとめて消える・後ろに暗い楕円の陰) を def に 1 回
# 絵に重ねる薄い層: 朝日の光の玉と前景のぼけた稲穂 (screen と blur)・流れる朝霧・立ちのぼる湯気・しずくの波紋 3 重・瓶を流れる光の帯・黒い幕の暗転と明け
# 締めは霧の田に縦組みの社名が 1 字ずつ浮かび、落款・罫・欧文・「日本酒」が順に出て黒へ溶ける。全編に周辺減光と動く grain
# hf b01 sake-brand (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#000000
theme dark
palette paper=#F8F2E7 ink=#211A14 seal=#B8322A
font "上品で端正な明朝体、標準の太さ"
fonts mb="上品で端正な明朝体の太字"
sfx off
# hf の作り: 田 → 水は不透明な旧場面の上に新しい場面を 0.6 s で溶かす (前景の稲穂が水の絵に透ける)
lint off=ghost_dissolve
prompt_tail "Photorealistic cinematic film still from a luxury Japanese sake commercial, vertical 9:16 frame, shot on a digital cinema camera with a fast prime lens, shallow depth of field, natural light, soft highlight roll-off, unified refined color grade: warm amber highlights, deep charcoal shadows, gently desaturated greens, subtle film grain. Quiet, modern, premium mood. No text, letters or logos other than those described, no watermark."
p { color: $paper; out: none }
div { border: none; out: none }
img { out: none }
shape { out: none }
# 同じ瓶を 2 つの構図で引くので根に 1 枚・湯気の透過は 2 枚の層で使う
image bottle = "[photo]Luxury product shot of a modern minimalist Japanese sake bottle: tall slender bottle of deep matte black glass with a refined off-white washi paper label. On the label, two large kanji 田恵 are written vertically in elegant bold black brush calligraphy, with a small vermilion square seal below them. The bottle stands on a dark slate stone surface; soft directional morning light from the left draws a long highlight along the glass; a few golden rice ears lie softly out of focus beside it; dark charcoal background with a faint warm haze. Bottle centered, occupying the middle 60% of the frame height." aspect=9:16
image steam = "[transparent]Soft white wisps of rising steam: a delicate translucent swirling vapor plume rising from the bottom of the frame and fading out toward the top, realistic photographic steam. Isolated subject, nothing else in the frame." aspect=9:16
# 音は絵に結ぶ: 場の音 (風・鳥・渓流) と foley (注ぐ・しずく・ほぐす・泡・瓶を置く) と締めの太鼓だけ (飾りの pop は無し)
sound wind = "早朝の田んぼを渡るやわらかな風の音"
sound sparrow = "遠くで鳴くスズメのさえずり、朝の田園"
sound stream = "山の渓流の澄んだせせらぎ"
sound tub = "木桶に水がとくとくと注がれる音"
sound drop = "澄んだ水滴がぽちゃんと水面に落ちる音"
sound drip = "しずくがぽたりと落ちる小さく澄んだ音"
sound rice = "米粒を手でさらさらとほぐす音"
sound bubbles = "発酵するもろみの泡がぷつぷつとはじける音"
sound glass = "ガラスの瓶を石の台にそっと置くコトッという音"
sound pour = "日本酒をグラスにとくとくと注ぐ音"
sound taiko = "和太鼓の深く響くドンという一打"
bgm#music(fade: 1200,900) 静かで上品な和のシネマティックな曲、ピアノと高弦・低弦、ゆっくり始まり終盤で厚みを増して終止和音で余韻を残す、高級日本酒のCM向け
# 縦組みのコピー: 右の列 a → 1.55 字下げた左の列 b (b は a の字数 × 55 ms 遅れて滲み始める)。後ろの暗い楕円の陰は正方形の radial (端で透明) を main の constant で縦に 2.1 倍。閉じると 0.55 s で薄れ、字はぼける
def copy(a, b, d) = div(left: 600px; top: 86px; width: 480px; height: 1080px; in: none; out: {opacity:0, duration:0.55, ease:'sine.in'})
  div#shade(left: 34px; top: 266px; width: 483px; height: 483px; background: radial(#0C080475,#0C080438@35%,#0C080400@71%); main: constant {scaleY: 2.1})
  p#a(left: 303px; top: 150px; width: 69px; font-size: 64px; writing-mode: vertical-rl; letter-spacing: 0.2em; line-height: 1; text-shadow: 0px 3px 15px #000000A6; in: {y:16, opacity:0, blur:8, duration:0.9, ease:'power2.out', stagger:{each:0.055}}; out: {blur:6, duration:0.55, ease:'sine.in'}; content: {a})
  p#b(left: 202px; top: 249px; width: 69px; font-size: 64px; writing-mode: vertical-rl; letter-spacing: 0.2em; line-height: 1; text-shadow: 0px 3px 15px #000000A6; delay: {d}; in: {y:16, opacity:0, blur:8, duration:0.9, ease:'power2.out', stagger:{each:0.055}}; out: {blur:6, duration:0.55, ease:'sine.in'}; content: {b})
# 朝霧 (淡い暖色の楕円の光を screen で重ね、印の to で横へ流す)。正方形の radial (端で透明) を main の constant で横に伸ばして楕円にする — 縁は柔らかいまま
def mist() = shape(border-radius: 50%; background: radial(#FFF4E48C,#FFF0DC2E@45%,#FFF0DC00@70%); mix-blend-mode: screen; in: none)
# 全編の質感: 周辺減光 (中央 55% は素通し) + 動く grain (最前面)
veil#vignette(background: radial(#00000000@55%,#0000006B@100%,50%,46%); z-index: front; in: none)
veil#grain(grain: 0.11; color: #00000000; z-index: front; in: none; main: noise {x: 6, y: 6, period: 0.033, ease: 'steps(1)'})

# 田: 黒から明ける朝の田 (低い位置から寄る)・朝日の光の玉が膨らみ、前景のぼけた稲穂が揺れて迫り、霧が左右に流れる・右上に「酒は、田から生まれる。」
section#field
img#field_photo(inset: 0; main: kb {scale: [1.06, 1.15], focus: ['55% 46%', '64% 68%']}) [photo]Extreme low-angle shot from inside a Japanese rice field at sunrise: ripe golden rice ears in sharp focus in the foreground, heavy with grain and glowing with warm backlight; behind them a flooded paddy reflects the soft sunrise sky; thin morning mist lies over the fields; distant hills fade into haze; creamy bokeh; pale sky in the upper third.
div#sunglow(left: 482px; top: 222px; width: 495px; height: 495px; border-radius: 1498px; background: radial(#FFD6968C,#FFBE7838@35%,#FFAA5A00@70%); mix-blend-mode: screen; opacity: 0.55; in: none)
img#rice_fg.bleed(left: -200px; top: 1120px; width: 760px; height: 1352px; opacity: 0.95; filter: blur(10px) brightness(0.85); transform: rotate(-1.6deg); transform-origin: 40% 100%; main: none; in: none) [transparent]Close-up of five or six ripe golden Japanese rice stalks heavy with grain, the ears drooping gracefully, rising from the bottom edge of the frame and occupying the lower 60% of the frame, backlit by warm low morning sunlight with glowing golden rim light on the grains and fine awns, tiny dew drops. Sharp focus, photorealistic macro detail. Isolated subject, nothing else in the frame.
mist#mist1.bleed(left: 80px; top: 980px; width: 420px; height: 420px; opacity: 0.55; main: constant {scaleX: 3.1})
mist#mist2.bleed(left: 800px; top: 1120px; width: 360px; height: 360px; opacity: 0.45; main: constant {scaleX: 3.33})
copy#copy1(a: "酒は、"; b: "田から生まれる。"; d: 165ms)

# 水: 渓流 → 「育ち」で木桶に注ぐ水 → 言い終わりで柄杓のしずく (3 枚を語で硬く切る)
section#water
img#stream_photo(inset: 0; main: kb {scale: [1.07, 1.13], focus: ['50% 85%', '50% 56%']}) [photo]Crystal-clear spring water flowing over smooth mossy stones in a shaded mountain stream near a sake brewery, early morning light filtering through tall cedar trees, gentle silver highlights on the moving water surface, slight motion blur in the water, very close low angle.
img#pour_photo(inset: 0; main: kb {scale: [1.05, 1.11], focus: ['36% 55%', '70% 58%']}) [photo]Inside an old wooden Japanese sake brewery: pure clear water pours in a smooth glassy stream from a bamboo spout into a large round wooden tub (kioke) bound with bamboo hoops, the water surface rippling, splashes catching soft side light from a small latticed window; aged dark cedar walls and thick beams in the background; quiet early morning.
img#ladle_photo(inset: 0; main: kb {scale: [1.06, 1.15], focus: ['54% 35%', '54% 33%']}) [photo]Macro photograph of a single crystal-clear water droplet hanging from the edge of a wooden ladle (hishaku), about to fall; the droplet acts like a lens refracting the warm window light; background is the dim interior corner of an old wooden sake brewery with aged beams and wooden tanks, beautifully blurred.
copy#copy2(a: "米が育ち、"; b: "水が育てる。"; d: 275ms)

# 醸す: 甑の湯気 (透過の湯気 2 枚が下から立ちのぼる) → 蒸米を広げる手 → 麹をほぐす手 → もろみの泡 → 櫂を入れる蔵人の後ろ姿
section#brew
img#steam_photo(inset: 0; main: kb {scale: [1.04, 1.1], focus: ['50% 42%', '50% 59%']}) [photo]A large traditional wooden rice steamer (koshiki) in a sake brewery at dawn, thick white steam billowing upward from freshly steamed rice, backlit by soft beams of morning light through a high window, dark wooden interior, atmospheric haze, no people.
img#steam_a.bleed(left: 160px; top: -350px; width: 760px; height: 1352px; content: @steam; opacity: 0.75; mix-blend-mode: screen; main: none; in: {y:380, opacity:0, scaleY:0.82, duration:1.54, ease:'none'})
img#steam_b.bleed(left: 190px; top: -249px; width: 760px; height: 1352px; content: @steam; flip: x; opacity: 0.45; mix-blend-mode: screen; main: none; in: {x:30, y:350, opacity:0, duration:1.54, ease:'none'})
img#hands_photo(inset: 0; main: kb {scale: [1.09, 1.09], focus: ['32% 55%', '78% 57%']}) [photo]Close-up of a sake brewer's hands and forearms in white work-clothes sleeves spreading freshly steamed white rice on a linen cloth over a wooden table, thin steam rising from the rice, warm side light, each grain glistening. Faces are never visible; only hands, back or a partial side view.
img#koji_photo(inset: 0; main: kb {scale: [1.05, 1.12], focus: ['58% 60%', '64% 64%']}) [photo]In a cedar-paneled koji room (koji-muro) of a sake brewery, a brewer's hands gently breaking apart and crumbling koji rice dusted with fine white mold on a shallow wooden tray, warm low tungsten light, fine detail of the rice grains, intimate and quiet. Faces are never visible; only hands, back or a partial side view.
img#moromi_photo(inset: 0; main: kb {scale: [1.08, 1.14], focus: ['50% 55%', '50% 59%']}) [photo]Close-up looking down into a large fermentation tank of sake mash (moromi): a creamy pale surface covered with countless small bubbles and soft foam, a few bubbles bursting, soft light from above, dark rim of the wooden tank.
img#brewer_photo(inset: 0; main: kb {scale: [1.04, 1.1], focus: ['32% 42%', '25% 45%']}) [photo]A sake brewer seen from behind, wearing white work clothes and a white head towel, quietly stirring a large wooden fermentation vat with a long wooden paddle, inside a dim old brewery with tall wooden tanks, a shaft of soft light falling through drifting steam. Faces are never visible; only hands, back or a partial side view.
copy#copy3(a: "そして、"; b: "人の手が醸していく。"; d: 220ms)

# 一滴: 袋から垂れるしずく (縦に pan) → 「季節」で漆の器に落ちる一滴の寄り・着水に合わせて金の波紋が 3 重に広がる → 黒い幕で暗転
section#drip
img#shizuku_photo(inset: 0; main: kb {scale: [1.12, 1.12], focus: ['50% 20%', '50% 76%']}) [photo]In a dim sake brewery, clear freshly pressed sake drips slowly from the bottom tips of hanging canvas sake bags (shizuku-shibori) into a vessel below; warm golden backlight makes each falling drop shine; dark background.
img#drop_photo(inset: 0; main: kb {scale: [1.03, 1.12], focus: ['50% 56%', '50% 59%']}) [photo]Macro shot of a single drop of clear sake falling into a still pool of sake in a dark lacquered vessel, gentle concentric ripples spreading, golden rim light on the drop, dark background.
# 波紋: 着水点で潰れた楕円の輪 (screen) が小さな輪から広がり、出て 0.35 s 後から薄れる
shape#ripple1(left: 270px; top: 1492px; width: 540px; height: 120px; border-radius: 50%; background: none; border: 3px solid #FFE2AA8C; box-shadow: 0px 0px 10px #FFDCA059; mix-blend-mode: screen; opacity: 0.6; overlap: drop_photo; in: {scaleX:0.13, scaleY:0.16, duration:2.2, ease:'power1.out'})
shape#ripple2(left: 270px; top: 1492px; width: 540px; height: 120px; border-radius: 50%; background: none; border: 3px solid #FFE2AA8C; box-shadow: 0px 0px 10px #FFDCA059; mix-blend-mode: screen; opacity: 0.6; overlap: drop_photo, ripple1; in: {scaleX:0.13, scaleY:0.16, duration:2.2, ease:'power1.out'})
shape#ripple3(left: 270px; top: 1492px; width: 540px; height: 120px; border-radius: 50%; background: none; border: 3px solid #FFE2AA8C; box-shadow: 0px 0px 10px #FFDCA059; mix-blend-mode: screen; opacity: 0.6; overlap: drop_photo, ripple1, ripple2; in: {scaleX:0.13, scaleY:0.16, duration:2.2, ease:'power1.out'})
copy#copy4(a: "一滴に、"; b: "季節をとじこめて。"; d: 220ms)
veil#blackout(color: #000000; opacity: 1; z-index: curtain; in: {opacity:0, duration:0.5, ease:'sine.in'})

# 瓶: 黒から明ける石の台の瓶 (0.3 s 後に光の帯が画面の左の外から右の外へ流れる — 静止の位置は画面の内側に置き、main の keys で外から外へ) → 同じ絵の寄り (ラベルの「田恵」)
section#bottle
img#bottle_photo(inset: 0; content: @bottle; main: kb {scale: [1.02, 1.07], focus: ['50% 29%', '50% 59%']})
shape#sweep(left: 0px; top: 0px; width: 700px; height: 1920px; path: rect; border: none; background: linear(#FFE6BE00,#FFE2B429@50%,#FFE6BE00,100); mix-blend-mode: screen; in: none; main: keys(at=0 x=-467 | at=1 x=720 ease=power1.inOut),window=0,2600,forwards)
img#label_photo(inset: 0; content: @bottle; main: kb {scale: [1.34, 1.4], focus: ['50% 99%', '50% 99%']})

# 杯: 黒い瓶から脚つきのグラスへ注ぐ手元 → 言い終わりで朝の田にグラスを掲げる後ろ姿
section#pour
img#glass_photo(inset: 0; main: kb {scale: [1.03, 1.09], focus: ['66% 50%', '72% 55%']}) [photo]Close-up of a hand pouring clear sake from a slender matte black bottle into a thin delicate stemmed glass on a dark wooden counter; the stream of sake catches warm golden backlight with glints and reflections; dark refined background. Faces are never visible; only hands, back or a partial side view.
img#toast_photo(inset: 0; main: kb {scale: [1.03, 1.09], focus: ['60% 7%', '60% 58%']}) [photo]Over-the-shoulder shot from behind a person standing at the edge of a golden Japanese rice field at dawn, holding up a delicate stemmed glass of clear sake toward the misty sunrise; the glass glows with warm light; only the hand, the glass and part of the shoulder are visible; the rice field and mist are softly out of focus. Faces are never visible; only hands, back or a partial side view.
copy#copy5(a: "田の恵みを、"; b: "あなたの杯に。"; d: 330ms)

# 社名: 霧の田 (引いていく) に 3 枚の霧が流れ、太鼓の一打で縦組みの「田恵」が 1 字ずつぼけから浮かぶ → 落款 → 中央の罫が下へ伸びる → DENEI → 日本酒
section#brand
img#end_photo(inset: 0; main: kb {scale: [1.14, 1.02], focus: ['50% 45%', '50% 60%']}) [photo]Vast quiet Japanese rice field at dawn wrapped in soft mist, seen from a low angle: golden rice fills only the lowest quarter of the frame, the rest is pale misty sky with soft warm haze and a faint glow of the rising sun; minimal, calm, lots of empty negative space; no people.
mist#mist3.bleed(left: -10px; top: 1180px; width: 520px; height: 520px; opacity: 0.5; main: constant {scaleX: 2.88})
mist#mist4.bleed(left: 789px; top: 1330px; width: 460px; height: 460px; opacity: 0.42; main: constant {scaleX: 3.04})
mist#mist5.bleed(left: 351px; top: 760px; width: 520px; height: 520px; opacity: 0.22; main: constant {scaleX: 2.88})
div#seal(left: 598px; top: 918px; width: 32px; height: 32px; border-radius: 2px; background: $seal; opacity: 0.95; in: {scale:0.6, opacity:0, duration:0.6, ease:'power2.out'})
p#logo(cx: 540px; top: 454px; font-size: 214px; font-family: mb; writing-mode: vertical-rl; letter-spacing: 0.08em; line-height: 1; color: $ink; text-shadow: 0px 0px 36px #FFF6E68C; in: {y:26, opacity:0, blur:14, duration:1.6, ease:'power2.out', stagger:{each:0.28}}) 田恵
div#rule(left: 538px; top: 1000px; width: 3px; height: 64px; background: #211A14BF; transform-origin: top; in: {scaleY:0, duration:0.9, ease:'power2.inOut'})
p#latin(cx: 540px; top: 1092px; font-size: 48px; letter-spacing: 0.6em; color: #231C16; text-shadow: 0px 0px 20px #FFF6E699; in: {y:14, opacity:0, duration:1.4, ease:'power2.out'}) DENEI
p#sub(cx: 540px; top: 1172px; font-size: 32px; letter-spacing: 0.55em; color: #231C16E0; text-shadow: 0px 0px 16px #FFF6E699; in: {opacity:0, duration:1, ease:'sine.out'}) 日本酒
```

```timeline.txt
#v2
cast n = "落ち着いた低く深い響きの大人の男性ナレーター、息を含んだ滑らかな声で、静かに上品に間を取って語る"
silence head=0ms tail=0ms

*** field
fade in,1000ms
bgm music
se wind -8dB to=5.4s fade=1200ms,1200ms
se sparrow -14dB +300ms to=4.5s fade=800ms,1000ms
@n: [!#sunglow to,{opacity:0.9, scale:1.14, duration:4.8, ease:'sine.inOut'}][!#rice_fg to,{x:70, y:-40, rotation:1.2, scale:1.18, duration:4.8, ease:'none'}][!#mist1 to,{x:200, duration:4.8, ease:'none'}][!#mist2 to,{x:-200, duration:4.8, ease:'none'}][>#copy1 +900ms][<#copy1 +3400ms][silence:4.2s]
transition dissolve {duration: .6, overlap: .6}

*** water
se stream -6dB to=4.5s fade=400ms,700ms
@n: [silence:0.8s][>#copy2 -50ms]米が[>#pour_photo +430ms][<#stream_photo +530ms][♪tub -4dB +390ms to=1.7s fade=100ms,450ms]育ち、水が育て[<#copy2 +120ms][>#ladle_photo +220ms][<#pour_photo +320ms][♪drop +970ms]る。[silence:1.34s]

*** brew
@n: [silence:1.92s][>#hands_photo -380ms][<#steam_photo -280ms][<#steam_a -280ms][<#steam_b -280ms][>#copy3 -50ms]そして、[>#koji_photo +140ms][<#hands_photo +240ms][♪rice -6dB +190ms to=1.5s fade=100ms,400ms]人の手が醸してい[<#copy3 +270ms][>#moromi_photo +310ms][<#koji_photo +410ms][♪bubbles -8dB +270ms to=1.8s fade=200ms,500ms][>#brewer_photo +1820ms][<#moromi_photo +1920ms]く。[silence:3.41s]
transition dissolve {duration: .6, overlap: .6}

*** drip
@n: [silence:1.95s][♪drip -4dB -1300ms][♪drip -6dB -450ms][>#copy4 -50ms]一滴[♪drip -5dB +90ms]に、[>#drop_photo +150ms][<#shizuku_photo +250ms][♪drop +500ms][>#ripple1 +520ms][!#ripple1 to,{opacity:0, duration:1.8, ease:'sine.in'} +870ms][>#ripple2 +850ms][!#ripple2 to,{opacity:0, duration:1.8, ease:'sine.in'} +1200ms][>#ripple3 +1250ms][!#ripple3 to,{opacity:0, duration:1.8, ease:'sine.in'} +1600ms]季節をとじこめ[<#copy4 +610ms]て。[silence:1.86s][>#blackout][silence:0.5s]

*** bottle
fade in,1100ms
@n: [♪glass -6dB +20ms][>#sweep +320ms][>#label_photo +3000ms][<#bottle_photo +3100ms][silence:5.99s]

*** pour
se pour -4dB to=3.3s fade=150ms,600ms
@n: [silence:0.53s][>#copy5 -50ms]田の恵みを、あなたの杯[>#toast_photo +170ms][<#glass_photo +270ms][<#copy5 +330ms]に。[silence:3.48s]
transition dissolve {duration: .8, overlap: .8}

*** brand
@n: [!#mist3 to,{x:240, duration:8.3, ease:'none'}][!#mist4 to,{x:-260, duration:8.3, ease:'none'}][!#mist5 to,{x:-120, duration:8.3, ease:'none'}][silence:1.8s][>#logo -1400ms][♪taiko -2dB -1420ms fade=0ms,300ms][>#seal -300ms][>#rule -200ms][>#latin +100ms][>#sub +700ms]日本酒、田恵。[silence:4.42s]
fade out,1000ms
```

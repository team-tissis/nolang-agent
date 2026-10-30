# concept · black-tire (hf 全力版の全量の写し — タイヤが黒い理由・9 場面の全面写真の豆知識) — canvas 1080x1920

見せる作り: 常設の上下の暗幕と上端の進行線・場面ごとの全面写真 (動く cam・黒から溶ける切替・文の途中の絵替え)・場面の頭に置く左上の小札・語で下から出る大見出しと弾む黄の札 (判子の音)・問いの組 (？ が揺れる)・式の丸札・場面を跨ぐ効果の行 (前の行を薄める)・理由の札・赤の打ち消し線・締めの題と 3 つの札・音の層 (語に結んだ効果音 20 + 切替の音)

```design.txt
#v2
# 学ぶ作り: 全編に敷く常設の枠 (上下の暗幕 + 上端の進行線) の上で、場面ごとに全面写真を黒から溶かして替える (文の途中の絵替えも 1 回)
# 文字は 3 段の class で組む: 場面の頭に置く左上の黄の小札 → 語で下から mask で出る大見出し → 語と同時に弾む黄の札 (主役・判子の音)
# 説明の図は 1 場面に 1 つ: 式の丸札・場面を跨ぐ効果の行・理由の札・赤の打ち消し線・締めの題と 3 つの札
# hf 07 black-tire (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#000000
theme dark
palette y=#FFD21F k=#0B0B0C red=#FF3B30 ink=#111111 milk=#F3EAD3 latex_hi=#FFFAF0 latex_mid=#EFE3C4 latex_lo=#D9C79C carbon_hi=#3A3A3A
font "Noto Sans JP Bold"
sfx off
master lufs=-13.7
# hf の作り: 小札は場面の題を台詞より先に見せる (spoiler)・「つまり」の小札は台詞の接続詞をそのまま札にする (duplicate_text)
lint off=spoiler,duplicate_text
prompt_tail "Photorealistic, cinematic color grading with deep blacks and warm highlights. Absolutely no text, no letters, no logos, no brand names, no watermark."
run y { color: $y }
p { color: #FFFFFF; out: none }
div { border: none; out: none }
group { out: none }
shape { out: none }
svg { out: none }
motion mask_up { in: mask_rise {duration:0.32, ease:'power3.out'} }
sound whoosh = "カメラの動きのような乾いたシュッという風切り音"
sound impact = "重く響く低音のドンという衝撃音"
sound question = "コミカルなはてなの電子音、短く跳ねて上がる"
sound pop = "かわいく軽いポンという電子音"
sound shine = "ピーンと高く鳴るひらめきの金属音"
sound chime = "明るく高い正解のチャイム"
sound pinpon = "クイズのピンポンという速い正解音"
sound swish = "アニメのスピード線のような鋭いシュッという音"
sound stamp = "ドンと叩く判子の衝撃音"
svg tire = """<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="47" fill="#111"/><circle cx="50" cy="50" r="47" fill="none" stroke="#2c2c2e" stroke-width="6" stroke-dasharray="7 5"/><circle cx="50" cy="50" r="27" fill="#3a3a3c"/><circle cx="50" cy="50" r="20" fill="#c9c9cc"/><circle cx="50" cy="50" r="6" fill="#3a3a3c"/></svg>"""
svg shield = """<svg viewBox="0 0 24 24"><path d="M12 2.2 20 5.3v6.1c0 5-3.4 9.1-8 10.4-4.6-1.3-8-5.4-8-10.4V5.3z" fill="#0B0B0C"/><path d="m8 12.2 2.8 2.8L16.4 9" fill="none" stroke="#FFD21F" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg tread = """<svg viewBox="0 0 24 24"><rect x="5" y="2.5" width="14" height="19" rx="3" fill="#0B0B0C"/><path d="M8 6.5l4 2.5 4-2.5M8 11l4 2.5 4-2.5M8 15.5l4 2.5 4-2.5" fill="none" stroke="#FFD21F" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg sun = """<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4.6" fill="#0B0B0C"/><g stroke="#0B0B0C" stroke-width="2.2" stroke-linecap="round"><path d="M12 1.8v2.6M12 19.6v2.6M1.8 12h2.6M19.6 12h2.6M4.8 4.8l1.8 1.8M17.4 17.4l1.8 1.8M4.8 19.2l1.8-1.8M17.4 6.6l1.8-1.8"/></g></svg>"""
svg check = """<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#0B0B0C"/><path d="m6.8 12.4 3.4 3.4 7-7.4" fill="none" stroke="#FFD21F" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
bgm#music(keys: "0:+4.5|550ms:0|end-1.7s:0|end-1.3s:+4"; fade: 0,850) 明るく爽やかで軽快なアコースティックギターとドラムのポップ、四拍子、豆知識のショート動画向け
# 字幕: 白文字 + 黒の太い縁 + 落ち影・句末の約物は外す・語の色は台詞の {y}
subtitle.hug(left: 50px; bottom: 412px; width: 980px; padding: 0px; font-size: 72px; line-height: 1.3; letter-spacing: 0.01em; color: #FFFFFF; stroke: #000000,6; text-shadow: 0px 6px 10px #00000073; background: none; unit: sentence; strip: 、。; lead: 0; in: {y:18, scale:0.96, opacity:0, duration:0.16, ease:'back.out(2)'})
# 左上の小札 (黄の縦棒 + 黄文字)・場面の頭に印なしで置き、絵と一緒に出る
def kicker(t) = div(left: 72px; top: 200px; width: 936px; height: 72px; in: {x:-24, opacity:0, duration:0.25, ease:'power1.out'})
  div#bar(left: 0px; cy: 50%; width: 12px; height: 50px; background: $y; border-radius: 3px)
  p#text(left: 28px; cy: 50%; font-size: 50px; color: $y; letter-spacing: 0.04em; text-shadow: 0px 4px 16px #00000099; content: {t})
# 大見出し (下から mask で出る) と黄の札
def headline(t) = p(left: 72px; font-size: 118px; line-height: 1.16; letter-spacing: -0.01em; text-shadow: 0px 8px 28px #00000099; in: mask_up; content: {t})
def yellow_tag(t, s=79) = p(font-size: {s}; line-height: 1.16; color: $k; background: $y; border-radius: 14px; padding: 0px 20px; content: {t})
# 効果の行 (暗い板 + 黄の丸の icon + 文)
def effect_row(t) = div(left: 60px; width: 960px; height: 152px; background: #0A0A0CC7; border: 2px solid #FFD21F8C; border-radius: 26px; box-shadow: 0px 12px 30px #00000059; in: {x:-80, opacity:0, duration:0.32, ease:'back.out(1.6)'})
  shape#dot(left: 32px; cy: 50%; width: 104px; height: 104px; border-radius: 50%; background: $y)
  svg#icon(left: 52px; cy: 50%; width: 64px; height: 64px)
  p#text(left: 162px; cy: 50%; font-size: 60px; line-height: 1.2; content: {t})
# 理由の札 (黄の丸札 + 黒丸の ✓・札ごと弾んで出る)
def reason_chip(t, w) = group(width: {w}; height: 144px; in: {scale:0.3, opacity:0, duration:0.26, ease:'back.out(2.2)'})
  p#text(z-index: front; left: 0px; cy: 50%; font-size: 100px; line-height: 1.1; color: $k; background: $y; border-radius: 148px; padding: 16px 46px 18px 110px; box-shadow: 0px 16px 36px #00000073; content: {t})
  svg#icon(left: 26px; cy: 50%; width: 62px; height: 62px; part: check)
# 上下の暗幕 (上 78% → 40〜54% は素通し → 下 82%)
def shade() = div(inset: 0; background: linear(#000000C7,#00000080@18%,#00000000@40%,#00000000@54%,#00000080@70%,#000000D1,180); border-radius: 24px; in: none)
# 全編の層: 暗幕と上端の進行線 (地 18% の白 + 黄の棒)
shade#shade
div#progress_track(left: 0px; top: 0px; width: 1080px; height: 10px; background: #FFFFFF2E; z-index: front; border-radius: 24px; in: none)
progress#progress_bar(left: 0px; top: 0px; width: 1080px; height: 10px; background: $y; until: end; z-index: front; overlap: progress_track)

# 問い: 黒いタイヤの写真に「Q. なぜタイヤは 黒い ？」を語ごとに組み、？ を揺らす
section#hook
# 黒い？ が着地する語まで 1.07 倍で待ち、そこから 1 に締まる
img#tire_photo(inset: 0; in: keys(at=0 scale=1.07 | at=0.4 scale=1.07 | at=1 ease=power3.out),duration=750; main: kb {scale: [1, 1.12], focus: ['50% 63%', '50% 63%']}) [photo]Vertical 9:16 photograph. Dramatic close-up of a brand-new glossy black car tire standing upright, the deep tread pattern facing the camera at a slight three-quarter angle, in a dark studio. Strong rim light from behind traces the tread grooves, a soft warm key light from the side. The tire fills the lower two-thirds of the frame; the upper third is dark, clean empty space. High-end product photography, shallow depth of field.
group#quiz(left: 0px; top: 230px; width: 1080px; height: 519px; out: {y:-40, opacity:0, duration:0.22, ease:'power2.in'})
  p#q(cx: 540px; cy: 46px; font-size: 64px; color: $y; letter-spacing: 0.06em; in: {x:-30, opacity:0, duration:0.3, ease:'power2.out'}) Q.
  p#line(cx: 540px; cy: 176px; font-size: 132px; line-height: 1.15; letter-spacing: -0.02em; text-shadow: 0px 8px 30px #00000099; in: mask_up) なぜタイヤは
  yellow_tag#black(cx: 420px; cy: 394px; s: 147; line-height: 1.12; padding: 0px 27px 4px 27px; border-radius: 22px; box-shadow: 0px 16px 40px #00000073; overlap: quiz.line; transform: rotate(-3deg); in: {scale:2.2, opacity:0, rotation:-5, duration:0.26, ease:'back.out(1.6)'}) 黒い
  p#mark(cx: 792px; cy: 394px; font-size: 230px; line-height: 1; text-shadow: 0px 10px 34px #00000099; transform: rotate(8deg); in: {scale:0, rotation:-98, opacity:0, duration:0.42, ease:'back.out(2.4)'}) ？

# 前提を崩す: 白い樹液の写真に「ゴムは本来 / 黒くない」と根拠の札
section#latex
img#latex_photo(inset: 0; main: kb {scale: [1.12, 1.12], focus: ['50% 28%', '50% 72%']}) [photo]Vertical 9:16 photograph. Close-up of milky white natural rubber latex flowing from a fresh diagonal tapping cut in the bark of a rubber tree and dripping into a small cup, in a tropical rubber plantation in soft morning light, green bokeh background. The pure white color of the latex is clearly visible. Documentary style, shallow depth of field.
kicker#kick_truth 実は…
headline#latex_head(cy: 356px) ゴムは本来
yellow_tag#not_black(left: 72px; cy: 506px; in: mask_rise {duration: 0.34, ease: 'back.out(1.4)'}) 黒くない
p#sap_fact(left: 72px; top: 820px; font-size: 42px; color: $ink; background: #FFFFFFF0; border-radius: 148px; padding: 14px 26px 14px 62px; box-shadow: 0px 10px 30px #00000059; in: {y:20, opacity:0, duration:0.3, ease:'power2.out'}) 天然ゴムの原料（樹液）は白い
  div#dot(left: 26px; cy: 50%; width: 22px; height: 22px; border-radius: 148px; background: $milk; border: 4px solid $ink)

# 正体: 黒い粉の写真に光の走る札「カーボンブラック」→ 文の途中で混ぜる工程の写真へ替え、式の丸札を組む
section#carbon
img#powder_photo(inset: 0; main: kb {scale: [1, 1.12], focus: ['50% 63%', '50% 63%']}) [photo]Vertical 9:16 macro photograph. A mound of ultra-fine matte jet-black powder (carbon black) on a dark laboratory bench, a stainless steel spatula lifting some powder, a faint cloud of fine black particles floating in the air, side lighting revealing the velvety texture. Dark moody background. Scientific macro photography.
kicker#kick_cause 黒さの正体
# カーボンブラックの札 (黒の地 + 黄の縁 + 光が左から右へ走る)
group#carbon_badge(left: 72px; top: 292px; width: 844px; height: 140px; sheen: carbon_badge.plate,900,#FFFFFF47,soft,power1.inOut; in: {scale:1.6, opacity:0, duration:0.34, ease:'back.out(1.5)'})
  div#plate(left: 0px; top: 0px; width: 844px; height: 140px; background: $k; border: 4px solid $y; border-radius: 16px; box-shadow: 0px 14px 40px #00000080)
  p#text(cx: 50%; cy: 50%; font-size: 100px; line-height: 1.2; color: $y; white-space: nowrap) カーボンブラック
p#carbon_meaning(left: 72px; cy: 489px; font-size: 54px; text-shadow: 0px 4px 18px #000000B3; in: {y:16, opacity:0, duration:0.28, ease:'power1.out'}) ＝ 炭素のとても細かい粒
# 文の中の絵替え: 黒が先に覆い、混ぜる工程の写真が 1.08 → 1 で溶けて出る (語で出す絵は全編の暗幕より上に乗るので暗幕を重ね直す)
div#mill_black(inset: 0; background: #000000; border-radius: 24px; in: none)
img#mill_photo(inset: 0; main: kb {scale: [1.12, 1.12], focus: ['15% 50%', '85% 50%']}; in: {opacity:0, scale:1.08, duration:0.32, ease:'power2.out'}) [photo]Vertical 9:16 photograph inside a tire factory. On a two-roll rubber mill, a sheet of pale beige raw rubber is being kneaded together with black powder; the sheet turns from beige to deep black where the powder is mixed in. Heavy steel rollers, industrial lighting, warm tones. Industrial documentary, no human faces.
shade#mill_shade
kicker#kick_mix ゴムに混ぜると…
# ゴム ＋ カーボンブラック ＝ 黒いタイヤ (丸の札 + 名札が組で弾んで出る)
group#eq_rubber(left: 66px; top: 330px; width: 232px; height: 310px; in: {scale:0, opacity:0, duration:0.3, ease:'back.out(2)'})
  div#disc(cx: 50%; top: 0px; width: 190px; height: 190px; border-radius: 148px; background: radial($latex_hi,$latex_mid@55%,$latex_lo,35%,30%); border: 6px solid #FFFFFFE6; box-shadow: 0px 14px 34px #00000080)
  p#label(cx: 50%; top: 208px; font-size: 44px; line-height: 1.15; text-align: center; text-shadow: 0px 4px 14px #000000BF) ゴム
p#eq_plus(cx: 362px; cy: 424px; font-size: 90px; text-shadow: 0px 6px 20px #00000099; in: {scale:0, opacity:0, duration:0.2, ease:'power1.out'}) ＋
group#eq_carbon(left: 424px; top: 330px; width: 232px; height: 310px; in: {scale:0, opacity:0, duration:0.3, ease:'back.out(2)'})
  div#disc(cx: 50%; top: 0px; width: 190px; height: 190px; border-radius: 148px; background: radial($carbon_hi,$k@60%,35%,30%); border: 6px solid #FFFFFFE6; box-shadow: 0px 14px 34px #00000080)
  shape#grain(left: "52;102;71"; top: "52;89;107"; width: 4px; height: 4px; border-radius: 50%; background: "#FFFFFF2E;#FFFFFF24;#FFFFFF1F") ×3
  p#label(cx: 50%; top: 208px; font-size: 44px; line-height: 1.15; text-align: center; text-shadow: 0px 4px 14px #000000BF) カーボン[br]ブラック
p#eq_equals(cx: 718px; cy: 424px; font-size: 90px; text-shadow: 0px 6px 20px #00000099; in: {scale:0, opacity:0, duration:0.2, ease:'power1.out'}) ＝
group#eq_tire(left: 782px; top: 330px; width: 232px; height: 310px; in: {scale:0, opacity:0, rotation:-120, duration:0.45, ease:'back.out(1.7)'})
  div#disc(cx: 50%; top: 0px; width: 190px; height: 190px; border-radius: 148px; background: $ink; border: 6px solid $y; box-shadow: 0px 14px 34px #00000080)
  svg#tire(left: 27px; top: 6px; width: 178px; height: 178px; part: tire)
  p#label(cx: 50%; top: 208px; font-size: 44px; line-height: 1.15; text-align: center; color: $y; text-shadow: 0px 4px 14px #000000BF) 黒いタイヤ

# 効果 1・2: 路面を噛むタイヤの写真に効果の行を語ごとに 2 本 (小札と行は次の場面へ跨ぐ)
section#tread
img#road_photo(inset: 0; main: kb {scale: [1.14, 1.02], focus: ['50% 57%', '50% 50%']}) [photo]Vertical 9:16 photograph. Ground-level low-angle shot of a car tire rolling on asphalt, the black tread firmly gripping the road, motion blur on the road surface and background, dynamic perspective, late afternoon sunlight. Automotive commercial style.
kicker#kick_effect.sticky カーボンブラックの効果
effect_row#row_tough.sticky(top: 320px) タイヤが{y}丈夫{/}になる
  svg#icon(part: shield)
effect_row#row_wear.sticky(top: 494px) {y}摩耗{/}しにくくなる
  svg#icon(part: tread)

# 効果 3: 太陽の写真で 3 本目を足し、前の 2 本を薄める
section#uv
img#sun_photo(inset: 0; main: kb {scale: [1.12, 1.12], focus: ['50% 72%', '50% 28%']}) [photo]Vertical 9:16 photograph. A car's black tire in the foreground at the bottom of the frame, shot from the ground. Directly behind it, intense midday sunlight shines from the center of the frame with a radiant starburst and lens flare, suggesting strong ultraviolet rays. The upper third of the frame is plain bright blue sky.
effect_row#row_uv(top: 668px) {y}紫外線{/}による劣化を抑える
  svg#icon(part: sun; in: keys(at=0 x=-53 rotation=-60 opacity=0 | at=0.533 x=0 rotation=-13 opacity=1 ease=back(1.6) | at=1 ease=power2.out),duration=600)

# 言い換え: 「黒いのは 単なるデザイン」に赤の打ち消し線を引き、黄の札「ではない！」を判子で
section#design
img#showroom_photo(inset: 0; main: kb {scale: [1.12, 1.12], focus: ['85% 50%', '15% 50%']}) [photo]Vertical 9:16 photograph. A tire shop showroom wall with many new black tires neatly displayed in rows like products in a boutique, clean spotlights from above, glossy floor reflections, stylish interior. Commercial interior photography.
kicker#kick_so つまり
headline#design_head(cy: 356px) 黒いのは
p#design_word(left: 72px; cy: 506px; font-size: 118px; line-height: 1.16; letter-spacing: -0.01em; text-shadow: 0px 8px 28px #00000099; in: {y:30, opacity:0, duration:0.3, ease:'power3.out'}) 単なるデザイン
div#design_strike(left: 62px; top: 508px; width: 838px; height: 18px; background: $red; border-radius: 9px; box-shadow: 0px 4px 14px #00000066; overlap: design_word; in: {scaleX:0, pivot:'left', duration:0.28, ease:'power2.inOut'})
yellow_tag#design_not(left: 72px; cy: 657px; in: mask_rise {duration: 0.32, ease: 'back.out(1.6)'}) ではない！

# 結論: 海沿いを走る車の写真に理由の札 3 枚が語ごとに弾み、「使うための工夫」で締める
section#drive
img#coast_photo(inset: 0; main: kb {scale: [1, 1.12], focus: ['50% 63%', '50% 63%']}) [photo]Vertical 9:16 photograph. A compact family car driving calmly along a scenic coastal road at golden hour, seen from a slightly elevated angle, warm sunlight, calm sea, a feeling of safety and long journeys. Automotive commercial style, license plate blank.
kicker#kick_reason 黒い理由は
reason_chip#chip_long(left: 362px; top: 330px; w: 237) 長く
reason_chip#chip_tough(left: 312px; top: 498px; w: 304) 丈夫に
reason_chip#chip_safe(left: 312px; top: 666px; w: 304) 安全に
p#craft_line(cx: 540px; cy: 908px; font-size: 76px; background: #00000094; border-radius: 20px; padding: 6px 30px 10px 30px; text-shadow: 0px 6px 24px #000000B3; in: {y:24, opacity:0, duration:0.3, ease:'power2.out'}) 使うための{y}工夫{/}

# 締めの 1 枚: 身近な街のタイヤの写真に「タイヤの 秘密」と効果の 3 つの札を並べ、最後の frame まで残す
section#end
img#street_photo(inset: 0; main: kb {scale: [1.14, 1.02], focus: ['50% 57%', '50% 50%']}) [photo]Vertical 9:16 photograph. A car parked on a quiet Japanese residential street in soft warm evening light, its front tire prominently in the foreground from a low angle, a familiar everyday atmosphere, houses softly out of focus. License plate blank.
p#end_lead(cx: 540px; cy: 340px; font-size: 56px; text-shadow: 0px 4px 18px #000000B3; in: {y:20, opacity:0, duration:0.3, ease:'power1.out'}) 身近だけど意外と知らない
group#end_main(in: {scale:1.3, opacity:0, duration:0.4, ease:'back.out(1.5)'})
  p#text(left: 63px; cy: 490px; font-size: 150px; line-height: 1.15; text-shadow: 0px 8px 30px #00000099) タイヤの
  yellow_tag#secret(left: 675px; cy: 490px; s: 100; line-height: 1.15; padding: 0px 21px 3px 21px) 秘密
p#end_tags(cx: "153;307;513"; cy: 660px; font-size: 40px; color: $y; background: #00000099; border: 3px solid $y; border-radius: 148px; padding: 10px 24px; in: {y:16, opacity:0, duration:0.25, ease:'power1.out', stagger: {each: 0.12}}) ×3 丈夫;摩耗しにくい;紫外線に強い
```

```timeline.txt
#v2
cast n = "爽やかな若い男性のナレーター、明るくはっきりした声でテンポよく語る" speed=110%
silence head=0 tail=0
transition = dissolve,320,overlap=320,color=#000000,zoom=1.08,ease=power2.out

*** hook
[>#subtitle]
bgm music
@n: [silence:300][>#quiz.q -300][♪whoosh -3.4dB -300][>#quiz.line -250][>#quiz.black][♪impact +2.1dB -10][>#quiz.mark +320][♪question +2.6dB +320][!#quiz to,{scale:1.04, duration:3.591, ease:'none'} +600]突然ですが、[|]なぜ車のタイヤって[|][!#quiz.mark to,{rotation:-10, scale:1.15, duration:0.18, ease:'power2.out', repeat:1, yoyo:true}][♪question -0.9dB]{y}黒い{/}[<#quiz cut-0]と思いますか？[silence:220]

*** latex
@: [silence:120]実は、[>#latex_head -50][♪pop -0.9dB -50]ゴムそのものは[|]本来、[>#not_black -50][♪stamp +0.4dB -20][>#sap_fact]{y}黒くありません{/}。[silence:120]

*** carbon
@: [silence:120]タイヤには[|][>#carbon_badge -60][♪shine +2.1dB -40][>#carbon_meaning +200]『{y}カーボンブラック{/}』という[|][<#kick_cause][<#carbon_badge][<#carbon_meaning][>#mill_black -50][>#mill_photo -50][>#mill_shade -50][♪whoosh -1.7dB -150][<#powder_photo +270][>#kick_mix +100][>#eq_rubber +200][♪pop +0.4dB +200][>#eq_plus +400][>#eq_carbon +520][♪pop +0.4dB +520][>#eq_equals +760]黒い素材が[|][>#eq_tire +170][♪pinpon +1dB +170]加えられています。[silence:100]

*** tread
@: [silence:120]この素材には、[|]タイヤを[>#row_tough -50][♪pop +1.6dB -50]{y}丈夫に{/}して、[|][>#row_wear -50][♪pop +1.6dB -50]{y}摩耗しにくく{/}する[|]効果があります。[silence:120]

*** uv
@: [silence:120]さらに、[|][>#row_uv -50][!#row_tough to,{opacity:0.55, duration:0.3} -50][!#row_wear to,{opacity:0.55, duration:0.3} -50][♪shine +0.4dB -50]{y}紫外線{/}による[|]ゴムの{y}劣化を抑える{/}[|]効果もあります。[silence:180]
[<#kick_effect none][<#row_tough none][<#row_wear none]

*** design
@: [silence:120]つまり、[|][>#design_head -50]タイヤが黒いのは[|][>#design_word -50]{y}単なるデザイン{/}[>#design_strike -50][♪swish +2.6dB -80]では[|][>#design_not -50][♪stamp +2.6dB -40]ありません。[silence:380]

*** drive
@: [silence:120][>#chip_long -40][♪pop +1.6dB -40]{y}長く{/}[>#chip_tough -35][♪pop +1.6dB -35]{y}丈夫に{/}、[|][>#chip_safe -40][♪pop +1.6dB -40]{y}安全に{/}[>#craft_line]使うための[|]工夫だったんです。[silence:220]

*** end
@: [silence:120][>#end_lead +150]身近だけど[|]意外と知らない、[|][>#end_main -50][♪chime +2.1dB -50][>#end_tags[*] +700]{y}タイヤの秘密{/}でした！[silence:1.7s]
```

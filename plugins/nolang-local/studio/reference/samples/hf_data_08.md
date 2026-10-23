# data · cityhall-hours (hf の作りを draft src に写した物 — 市役所の窓口開庁時間の変更のお知らせ) — canvas 1920x1080

見せる作り: 常設の帯 (紺の丸札・sticky)・濃紺の札の字幕・題の札と mask から上がる 2 行と下線・時計つきの板 2 枚の前 → 後の入れ替え (針が回る・矢印・判子で板が沈む)・紙の地の比較の図 (目盛り・棒 2 本・差の枠の斜線と ×・吹き出し・注意の帯・図ごと寄る)・紙の板 + 写真の枠 (橙の縁) の段組で場面ごとの絵替えと左右の入れ替え・締めの白い板・右から左の wipe (紺 / 橙の帯) と前の場面の札を左へ流す退場・音の層 (チャイムで開いて閉じる・語に結んだ効果音・切替の音)

```design.txt
#v2
# この見本から学ぶ作り: design system を根に 1 回 (palette・書体 1・run・丸い札の def chip・段組の半分 2 種の def) → 場面は差分だけ
# 常設の帯 (sticky・締めで end)・題の札と mask から上がる 2 行・時計つきの板 2 枚を前 → 後に入れ替えて判子・紙の地の比較の図 (棒・差の斜線と ×・吹き出し・注意の帯)
# 紙の板 + 写真の枠の段組で場面ごとに絵を替え左右も入れ替える・時刻 / 棒 / × / チェックは台詞の語と同時に出す・締めは白い板 1 枚
# 座標は hf (1920x1080) の 2/3。切替は右から左の wipe + 紺 / 橙の帯 (timeline の根)・前の場面の札は左へ流して抜く (section と要素の out)
canvas 1920x1080 bg=#F6F1E6
theme light
palette navy=#1F3A5F navy_deep=#142A47 slate=#7B8CA3 orange=#E8743B o2=#CF5B22 cream=#F6F1E6 paper=#FBF8F2 ink=#1D2733 gray=#5F6B7B line=#DDD5C6 red=#D2463A red_t=#F9DED9 sky=#BCD6F0
font "BIZ UDPゴシック Bold"
sfx off
master lufs=-16
# hf の作り: 題・帯・場面の札と見出しは場面の頭に出し台詞が後から読む (図の棒の時刻と目盛りは前の場面で言った値)
lint off=spoiler
# hf の作り: お願いと注記の札は字幕と同じ文を同時に見せる (案内の念押し)
lint off=duplicate_text
# hf の作り: 比較の図の場面は写真を敷かず紙の地 (点の模様) だけ
lint off=text_only_cut
art "flat vector illustration in a clean, modern Japanese public-information style. Soft rounded shapes, subtle paper grain, gentle gradients, consistent limited palette: deep navy #1F3A5F, soft sky blue #BFD9EE, warm cream #F6F1E6, fresh leaf green #6FA772, with small warm orange #E8743B accents. Friendly, trustworthy, calm mood, even daylight. No text, no letters, no numbers, no logos, no signage writing"
image hall_morning = "A wide establishing view of a fictional modern Japanese city hall: a clean five-storey municipal office building with a glass entrance canopy, a small paved plaza with trees, flower beds and benches, and a few citizens (an elderly man with a cane, a mother holding a child's hand, an office worker) walking toward the entrance in bright morning sun. Clear blue sky with soft clouds. The building sits in the right two-thirds of the frame; keep the upper-left area as calm open sky" aspect=16:9
image counter = "Interior of a bright Japanese city hall service counter area: a long clean counter with low partitions, friendly staff members in office attire politely helping citizens (an elderly woman being assisted, a young father with documents), a queue-ticket machine and rows of waiting chairs, potted plants, large windows with soft daylight. Calm, orderly, welcoming. Eye-level wide shot" aspect=16:9
# 市役所の glyph: 破風 + 梁 + 柱 4 本 + 基壇。白 (札の中) と灰 (締めの板の足)
svg hall_white = """<svg viewBox="0 0 24 24" fill="#FFFFFF"><path d="M12 1.8 L22.5 7.2 H1.5 Z"/><rect x="2.5" y="8.4" width="19" height="1.8" rx="0.4"/><rect x="4.2" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="8.4" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="13.2" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="17.4" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="1.5" y="19.4" width="21" height="2.6" rx="0.5"/></svg>"""
svg hall_gray = """<svg viewBox="0 0 24 24" fill="#5F6B7B"><path d="M12 1.8 L22.5 7.2 H1.5 Z"/><rect x="2.5" y="8.4" width="19" height="1.8" rx="0.4"/><rect x="4.2" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="8.4" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="13.2" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="17.4" y="11.2" width="2.4" height="7.2" rx="0.4"/><rect x="1.5" y="19.4" width="21" height="2.6" rx="0.5"/></svg>"""
sound chime_in = "柔らかい低めの4点チャイム、アナウンスの前の合図 (ピンポンパンポーン)"
sound chime_out = "柔らかい4点チャイムの締め、公共施設のアナウンス (ピンポンパンポーン)"
sound fuwan = "テロップがふわりと出る柔らかい短い電子音 (ふわん)"
sound swish_soft = "空気感のある短い高音のノイズの掃き、残響つき (スッ)"
sound swish = "鋭く空気感のある短いデジタルの風切り音、残響つき (シュッ)"
sound pop = "短く明るい電子音のポン (ピコン)"
sound sparkle = "柔らかく高いシンセのベルの和音 (キラーン)"
sound stamp = "判子を紙に押す乾いた短い音"
sound down = "明るい電子音が下がる短い合図 (ピロン)"
sound up = "明るい電子音が上がる短い合図 (ピロリン)"
sound ting = "高く明るい金属のベルの単音 (ティン)"
run o { color: $orange }
run tilde_o { color: $orange; font-size: 0.66em }
run tilde { color: $slate; font-size: 0.7em }
run r { color: $red }
run num { color: $navy; font-size: 56px }
run num_o { color: $orange; font-size: 56px }
p { out: none }
div { background: #FFFFFF; out: none }
img { main: none; out: none }
shape { out: none }
icon { out: none }
svg { out: none }
subtitle.hug(font-size: 46px; bottom: 54px; background: #111F34CC; color: #FFFFFF; border-radius: 16px; padding: 14px 36px; letter-spacing: 0.03em; line-height: 1.25; unit: sentence; strip: all; lead: 120; tail: 350; hold: off; in: fade {duration: 0.12}; out: fade {duration: 0.1})
bgm#music(volume: 6dB; duck: -8; fade: 1200,3400; keys: "0:0") 明るく穏やかで爽やかな日常のポップ、ピアノとアコースティックギターと高い弦、軽い打楽器、希望のある普通の速さ
# 丸い札 (地と字の色を渡す)・段組の半分 (紙の板 573 px / 写真の枠 707 px・全高)
def chip(t, fill_color=$navy, text_color=#FFFFFF) = p(content: {t}; font-size: 36px; line-height: 1; background: {fill_color}; color: {text_color}; border-radius: 148px; padding: 14px 28px; letter-spacing: 0.04em)
def half_photo(src, focus_x=50%) = img(top: 0px; width: 1060px; height: 1080px; content: {src}; object-fit: cover; object-position: {focus_x} 50%; in: none)
def half_paper = div(top: 0px; width: 860px; height: 1080px; background: $paper; pattern: dots,23,#1F3A5F12; in: none)
# 時計の文字盤 (円の板 + 目盛り 4 + 針 2 本): 針は上半分だけ塗った細い板を中心で回した物 — 印 `[!#盤.mh to,{rotation:…}]` で針が回る
def dial(c) = div(width: 116px; height: 116px; border-radius: 58px; border: 8px solid {c})
  shape#tk(left: 0px; top: 0px; width: 100%; height: 100%; path: ticks,n=4,len=0.18; background: {c}; border: 3px solid {c})
  div#hh(cx: 50%; cy: 50%; width: 8px; height: 51px; border-radius: 4px; background: linear($navy,$navy@50%,#1F3A5F00@50%,180); transform: rotate(248deg))
  div#mh(cx: 50%; cy: 50%; width: 6px; height: 75px; border-radius: 3px; background: linear($navy,$navy@50%,#1F3A5F00@50%,180); transform: rotate(90deg))

# title — 題の札: 朝の市役所に左から cream の幕 → 札 → 2 行が mask から上がる → 下線
section#title(stagger: {each:0}; out: {x:-140, duration:0.7, ease:'power3.inOut'})
img#title_photo(inset: 0; content: @hall_morning; main: kb {scale: [1.03, 1.12], focus: ['70% 60%', '70% 60%']})
div#title_veil(inset: 0; background: linear(#F6F1E6F2@0%,#F6F1E6E0@42%,#F6F1E680@56%,#F6F1E600@72%,90); delay: 50; in: {opacity:0, duration:0.8, ease:'power2.out'})
chip#title_chip(left: 130px; top: 230px; padding: 14px 28px 14px 76px; delay: 300; in: {x:-30, scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.7)'}; out: {x:-140, duration:0.7, ease:'power3.inOut'}) 市役所からのお知らせ
svg#title_glyph(left: 159px; top: 243px; width: 36px; height: 36px; part: hall_white; delay: 300; in: {x:-30, scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.7)'}; out: {x:-140, duration:0.7, ease:'power3.inOut'}; overlap: title_chip)
p#title_l1(left: 130px; top: 339px; font-size: 104px; color: $navy; line-height: 1.15; letter-spacing: 0.02em; delay: 620; in: {y:148, duration:0.7, ease:'power3.out', clip:true}; out: {x:-140, duration:0.7, ease:'power3.inOut'}) 窓口開庁時間が
p#title_l2(left: 130px; top: 459px; font-size: 172px; color: $o2; line-height: 1.12; letter-spacing: 0.02em; text-shadow: 0px 0px 28px #FFFFFFB3; delay: 950; in: {y:242, duration:0.75, ease:'power3.out', clip:true}; out: {x:-140, duration:0.7, ease:'power3.inOut'}) 変わります
shape#title_rule(left: 130px; top: 660px; width: 820px; height: 12px; path: rect,r=0.5; background: $navy; delay: 1550; in: {scaleX:0, duration:0.7, ease:'power2.inOut', pivot:'left'}; out: {x:-140, duration:0.7, ease:'power3.inOut'})

# change — 前 → 後: ぼかした窓口の写真に「これまで」の板 → 左へ寄せて「変更後」の板と矢印 → 針が回って時刻が出て判子
section#change(stagger: {each:0}; out: {x:-140, duration:0.7, ease:'power3.inOut'})
img#change_photo(inset: 0; content: @counter; filter: blur(8px) saturate(0.9); main: kb {scale: [1.08, 1.16]})
div#change_veil(inset: 0; background: #F6F1E6DB; in: none)
# 常設の帯: 紺の丸札に glyph + 題 + 縦線 + 副題 (sticky で closing の頭まで残る)
div#banner.sticky(left: 56px; top: 40px; width: 710px; height: 60px; border-radius: 148px; background: $navy; box-shadow: 0px 8px 22px #142A472E; delay: 500; in: {y:-24, opacity:0, duration:0.5, ease:'power3.out'}; out: {y:-24, opacity:0, duration:0.4, ease:'power2.in'})
  svg#glyph(left: 24px; cy: 50%; width: 34px; height: 34px; part: hall_white)
  p#t(left: 76px; cy: 50%; font-size: 30px; line-height: 1; nowrap: true; color: #FFFFFF) 市役所からのお知らせ
  shape#vline(left: 392px; cy: 50%; width: 3px; height: 28px; path: rect; background: #FFFFFF59)
  p#sub(left: 411px; cy: 50%; font-size: 30px; line-height: 1; nowrap: true; color: $sky) 窓口開庁時間の変更
div#before(left: 580px; top: 236px; width: 760px; height: 500px; border-radius: 34px; box-shadow: 0px 24px 60px #142A4729; delay: 350; in: {y:60, opacity:0, duration:0.7, ease:'power3.out'}; out: {x:-140, duration:0.7, ease:'power3.inOut'})
  chip#pill(left: 50px; top: 46px; fill_color: $slate) これまで
  dial#dial(right: 46px; top: 34px; c: $slate)
  p#cap(left: 50px; top: 140px; font-size: 36px; color: $gray) 窓口開庁時間
  p#t(left: 50px; top: 192px; font-size: 92px; color: $navy; line-height: 1.1; letter-spacing: 0.01em; nowrap: true; delay: 600; in: {y:20, opacity:0, duration:0.55, ease:'power3.out'}) {open}8:15{/}{tilde}〜{/}{close}17:15{/}
  shape#rule(left: 50px; bottom: 120px; width: 662px; height: 3px; path: line_h; border: 3px solid $line; dash: 6,6)
  p#foot(left: 50px; bottom: 40px; font-size: 36px; color: $gray) 1日の受付{num}9{/}時間
# 矢印: 軸を描いてから頭が左から来る
shape#arrow_line(path: "M 579 325 L 657 325"; background: none; border: 14px solid $orange; in: draw {duration: 0.4, ease: 'power2.out'}; out: {x:-140, duration:0.7, ease:'power3.inOut'})
shape#arrow_head(path: "M 639 301 L 667 325 L 639 348"; background: none; border: 14px solid $orange; in: {x:-20, opacity:0, duration:0.3, ease:'power3.out'}; out: {x:-140, duration:0.7, ease:'power3.inOut'}; overlap: arrow_line)
div#after(left: 1060px; top: 236px; width: 760px; height: 500px; border-radius: 34px; border: 4px solid $orange; overlap: before; box-shadow: 0px 24px 60px #142A4729; in: {x:80, opacity:0, duration:0.7, ease:'power3.out'}; out: {x:-140, duration:0.7, ease:'power3.inOut'})
  chip#pill(left: 54px; top: 51px; fill_color: $orange) 変更後
  dial#dial(right: 51px; top: 39px; c: $orange)
  p#cap(left: 54px; top: 144px; font-size: 36px; color: $gray) 窓口開庁時間
  p#open(left: 54px; top: 196px; font-size: 92px; color: $orange; line-height: 1.1; in: {y:40, opacity:0, duration:0.45, ease:'back.out(1.6)'}) 9:00
  p#sep(left: 285px; top: 213px; font-size: 64px; color: $orange; in: fade {duration: 0.3}) 〜
  p#close(left: 381px; top: 196px; font-size: 92px; color: $orange; line-height: 1.1; in: {y:40, opacity:0, duration:0.45, ease:'back.out(1.6)'}) 16:00
  shape#rule(left: 54px; bottom: 120px; width: 662px; height: 3px; path: line_h; border: 3px solid $line; dash: 6,6)
  p#foot(left: 54px; bottom: 40px; font-size: 36px; color: $gray) 1日の受付{num_o}7{/}時間
# 判子: 赤の二重丸が -14° に傾いて上から叩きつけ、板ごと沈む (timeline)
group#hanko(left: 1692px; top: 615px; width: 178px; height: 178px; transform: rotate(-14deg); in: keys(at=0 scale=2.3 rotation=-18 opacity=0 | at=1 ease=power4.in),duration=220; out: {x:-140, duration:0.7, ease:'power3.inOut'})
  shape#outer(left: 0px; top: 0px; width: 178px; height: 178px; border-radius: 50%; background: #FFFFFFDB; border: 9px solid $red)
  shape#inner(left: 18px; top: 18px; width: 142px; height: 142px; border-radius: 50%; background: none; border: 3px solid $red)
  p#t(cx: 50%; cy: 50%; font-size: 58px; color: $red; letter-spacing: 0.04em) 変更

# gaps — 差を図にする: 紙の地に目盛りと棒 2 本 → 差の枠と吹き出し → 斜線と × → 注意の帯 (図ごとゆっくり寄る)
section#gaps(stagger: {each:0}; out: {x:-140, duration:0.7, ease:'power3.inOut'})
div#bg_gaps(inset: 0; background: $paper; in: none; out: none; z-index: back)
div#gaps_paper(inset: 0; background: $paper; pattern: dots,23,#1F3A5F12; in: none)
group#chart(main: ramp {scale: 1.035, window: '700,20830', pivot: '50%,45%'})
shape#chart.head_bar(left: 130px; top: 136px; width: 12px; height: 60px; path: rect; background: $orange; delay: 350; in: {y:20, opacity:0, duration:0.55, ease:'power3.out'})
p#chart.head(left: 171px; top: 134px; font-size: 54px; color: $navy; line-height: 1.1; delay: 350; in: {y:20, opacity:0, duration:0.55, ease:'power3.out'}) 窓口で受付できる時間帯
shape#chart.grid(left: 264px; top: 330px; width: 1452px; height: 330px; gap: 0; path: line_v; border: 3px solid #1F3A5F29; dash: 4,4; in: fade {duration: 0.4, stagger: 0.03}; delay: 700; display: flex) ×11
p#chart.label_before(left: 70px; top: 382px; width: 230px; font-size: 40px; color: $navy; text-align: right; in: {y:16, opacity:0, duration:0.4, ease:'power3.out'}; delay: 700) これまで
p#chart.label_after(left: 70px; top: 554px; width: 230px; font-size: 40px; color: $navy; text-align: right; in: {y:16, opacity:0, duration:0.4, ease:'power3.out'}) 変更後
div#chart.bar_before(left: 363px; top: 360px; width: 1188px; height: 100px; border-radius: 14px; background: $slate; box-shadow: 0px 10px 24px #142A4724; in: {scaleX:0, duration:0.8, ease:'power3.inOut', pivot:'left'}; delay: 800)
  p#t(cx: 50%; cy: 50%; font-size: 42px; color: #FFFFFF; letter-spacing: 0.03em; in: {y:10, opacity:0, duration:0.4, ease:'power3.out'}; delay: 1400) 8:15〜17:15
div#chart.bar_after(left: 462px; top: 530px; width: 924px; height: 100px; border-radius: 14px; background: $orange; box-shadow: 0px 10px 24px #142A4724; in: {scaleX:0, duration:0.8, ease:'power3.inOut', pivot:'left'})
  p#t(cx: 50%; cy: 50%; font-size: 42px; color: #FFFFFF; letter-spacing: 0.03em; in: {y:10, opacity:0, duration:0.4, ease:'power3.out'}) 9:00〜16:00
div#chart.gap_am(left: 363px; top: 330px; width: 99px; height: 330px; border-radius: 10px; background: #D2463A14; border: 3px solid $red; in: fade {duration: 0.35})
  div#hatch(left: 0px; top: 0px; width: 100%; height: 100%; border-radius: 8px; background: #FFFFFF80; pattern: hatch,45,#D2463A57,13,7; in: fade {duration: 0.4})
  div#xmark(cx: 50%; cy: 50%; width: 74px; height: 74px; border-radius: 38px; background: $red; box-shadow: 0px 6px 16px #D2463A59; in: {scale:0.85, opacity:0, duration:0.4, ease:'back.out(1.7)'})
    icon#cross(cx: 50%; cy: 50%; font-size: 39px; name: x; weight: bold; color: #FFFFFF)
div#chart.gap_pm(left: 1386px; top: 330px; width: 165px; height: 330px; border-radius: 10px; background: #D2463A14; border: 3px solid $red; in: fade {duration: 0.35})
  div#hatch(left: 0px; top: 0px; width: 100%; height: 100%; border-radius: 8px; background: #FFFFFF80; pattern: hatch,45,#D2463A57,13,7; in: fade {duration: 0.4})
  div#xmark(cx: 50%; cy: 50%; width: 74px; height: 74px; border-radius: 38px; background: $red; box-shadow: 0px 6px 16px #D2463A59; in: {scale:0.85, opacity:0, duration:0.4, ease:'back.out(1.7)'})
    icon#cross(cx: 50%; cy: 50%; font-size: 39px; name: x; weight: bold; color: #FFFFFF)
p#chart.balloon_am(cx: 412px; top: 246px; font-size: 38px; line-height: 1; color: $red; background: #FFFFFF; border: 3px solid $red; border-radius: 14px; padding: 10px 20px 9px 20px; pointer: below; in: {y:16, scale:0.85, opacity:0, duration:0.45, ease:'back.out(1.7)'}) 45分 遅く
p#chart.balloon_pm(cx: 1468px; top: 246px; font-size: 38px; line-height: 1; color: $red; background: #FFFFFF; border: 3px solid $red; border-radius: 14px; padding: 10px 20px 9px 20px; pointer: below; in: {y:16, scale:0.85, opacity:0, duration:0.45, ease:'back.out(1.7)'}) 1時間15分 早く
shape#chart.axis(left: 330px; top: 680px; width: 1320px; height: 4px; path: rect,r=0.5; background: $navy; in: {scaleX:0, duration:0.7, ease:'power2.inOut', pivot:'left'}; delay: 450)
p#chart.tick(left: 264px; top: 696px; width: 1452px; gap: 0; font-size: 30px; text-align: center; color: "$gray;$navy;$gray;$gray;$gray;$gray;$gray;$gray;$navy;$gray;$gray"; in: {y:10, opacity:0, duration:0.3, ease:'power3.out', stagger: {each: 0.04}}; delay: 600; display: flex) ×11 8時;9時;10時;11時;12時;13時;14時;15時;16時;17時;18時
div#chart.caution(left: 258px; top: 789px; width: 1404px; height: 112px; border-radius: 22px; background: $red_t; border: 4px solid $red; in: {y:40, opacity:0, duration:0.55, ease:'power3.out'})
  icon#sign(left: 30px; cy: 50%; font-size: 64px; name: warning; weight: fill; color: $red)
  p#t(left: 120px; cy: 50%; font-size: 44px; color: $ink; nowrap: true) {r}8:15〜9:00{/} と {r}16:00〜17:15{/} は、窓口で手続きできません

# reason — 理由: 左に紙の板 (札・3 行の見出し・お願いの札)・右に窓口の写真 (左端に橙の縁)
section#reason(stagger: {each:0})
half_paper#reason_paper(left: 0px)
half_photo#reason_photo(left: 860px; src: @counter; focus_x: 46%; main: kb {scale: [1.12, 1.02], focus: '33% 50%'}; edge: left,9,$orange)
chip#reason_chip(left: 100px; top: 196px; fill_color: none; text_color: $navy; border: 3px solid $navy; padding: 10px 26px; delay: 350; in: {y:14, opacity:0, duration:0.45, ease:'power3.out'}) 窓口サービスの見直し
p#reason_l1(left: 100px; top: 300px; font-size: 66px; color: $navy; line-height: 1.3; letter-spacing: 0.02em; in: {y:108, duration:0.6, ease:'power3.out', clip:true}) より丁寧で
p#reason_l2(left: 100px; top: 392px; font-size: 66px; color: $navy; line-height: 1.3; letter-spacing: 0.02em; in: {y:108, duration:0.6, ease:'power3.out', clip:true}) 正確な
p#reason_l3(left: 100px; top: 482px; font-size: 66px; color: $navy; line-height: 1.3; letter-spacing: 0.02em; in: {y:108, duration:0.6, ease:'power3.out', clip:true}) {o}窓口サービス{/}のために
div#reason_ask(left: 100px; top: 640px; width: 680px; height: 184px; border-radius: 0,15,15,0; edge: left,9,$orange; box-shadow: 0px 16px 40px #142A471F; in: {x:-40, opacity:0, duration:0.6, ease:'power3.out'})
  p#t(left: 48px; cy: 50%; font-size: 46px; color: $navy; line-height: 1.35) ご理解とご協力を[br]お願いいたします

# confirm — 確かめ方: 同じ段組で絵を替える (玄関でスマホを見る人)・見出しのチェックと 2 枚の札
section#confirm(stagger: {each:0})
half_paper#confirm_paper(left: 0px)
half_photo#confirm_photo(left: 860px; focus_x: 100%; main: kb {scale: [1.02, 1.1]}; edge: left,9,$orange) A cozy Japanese home entryway (genkan) in the morning: a woman in her forties holding a smartphone and checking the screen before going out (the screen shows only a simple clock symbol), her tote bag and shoes ready by the door, warm sunlight through a small window, a wall calendar with blank squares. She looks attentive and calm. Place her on the right side of the frame; the left side is a simple plain wall
chip#confirm_chip(left: 100px; top: 176px; delay: 350; in: {y:14, opacity:0, duration:0.45, ease:'power3.out'}) ご来庁の前に
p#confirm_l1(left: 100px; top: 282px; font-size: 92px; color: $navy; line-height: 1.18; letter-spacing: 0.02em; in: {y:135, duration:0.6, ease:'power3.out', clip:true}) 開庁時間を
p#confirm_l2(left: 100px; top: 398px; font-size: 92px; color: $orange; line-height: 1.18; letter-spacing: 0.02em; in: {y:135, duration:0.6, ease:'power3.out', clip:true}) チェック
shape#confirm_dot(left: confirm_l2.right+11; top: 405px; width: 84px; height: 84px; border-radius: 50%; background: $orange; in: {scale:0, duration:0.4, ease:'back.out(2)'})
icon#confirm_tick(left: confirm_l2.right+19; top: 417px; font-size: 60px; name: check; weight: bold; color: #FFFFFF; in: draw {duration: 0.35, ease: 'power2.out'}; overlap: confirm_dot)
div#via_web(left: 100px; top: 590px; width: 320px; height: 290px; border-radius: 26px; box-shadow: 0px 16px 40px #142A4721; in: {y:40, scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.7)'})
  img#pic(cx: 50%; top: 32px; width: 170px; height: 170px; object-fit: contain) [transparent]a single flat vector icon, soft rounded shapes, deep navy outlines and fills with warm orange and white highlights, subtle soft shadow: a smartphone showing a simple web page layout with an analog clock symbol on its screen, centered with generous padding, transparent background, no text
  p#t(cx: 50%; top: 213px; font-size: 34px; color: $navy) 市のホームページ
div#via_paper(left: 450px; top: 590px; width: 320px; height: 290px; border-radius: 26px; box-shadow: 0px 16px 40px #142A4721; in: {y:40, scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.7)'})
  img#pic(cx: 50%; top: 32px; width: 170px; height: 170px; object-fit: contain) [transparent]a single flat vector icon, soft rounded shapes, deep navy outlines and fills with warm orange and white highlights, subtle soft shadow: a folded community newsletter paper (a municipal bulletin) with abstract grey lines instead of text and a small analog clock symbol printed on it, centered with generous padding, transparent background, no text
  p#t(cx: 50%; top: 213px; font-size: 34px; color: $navy) 広報紙

# tips — 余裕をもって: 段組の左右を入れ替える (左に歩く人)・右に見出し・注記・受付の帯 (終了間際に斜線と札)
section#tips(stagger: {each:0})
half_photo#tips_photo(left: 0px; focus_x: 0%; main: kb {scale: [1.1, 1], focus: ['20% 40%', '20% 40%']}; edge: right,9,$orange) A relaxed man in his sixties with a shoulder bag walking along a tree-lined path toward the entrance of a modern city hall in the early afternoon, glancing at his wristwatch with a calm smile because he has plenty of time. Sunny weather, soft tree shadows on the pavement. Place him on the left third of the frame; keep the right side open and simple (sky and building facade)
half_paper#tips_paper(left: 1060px)
chip#tips_chip(left: 1161px; top: 176px; delay: 350; in: {y:14, opacity:0, duration:0.45, ease:'power3.out'}) ご来庁のポイント
p#tips_l1(left: 1161px; top: 282px; font-size: 74px; color: $navy; line-height: 1.22; letter-spacing: 0.02em; delay: 450; in: {y:112, duration:0.6, ease:'power3.out', clip:true}) 時間に
p#tips_l2(left: 1161px; top: 378px; font-size: 74px; color: $navy; line-height: 1.22; letter-spacing: 0.02em; delay: 650; in: {y:112, duration:0.6, ease:'power3.out', clip:true}) {o}余裕{/}をもって
p#tips_note(left: 1161px; top: 506px; font-size: 38px; color: $gray; line-height: 1.45; in: {y:18, opacity:0, duration:0.5, ease:'power3.out'}) 手続きによっては[br]時間がかかる場合があります
shape#mini_bar(left: 1161px; top: 774px; width: 660px; height: 64px; path: rect,r=0.19; background: $orange; in: {scaleX:0, duration:0.7, ease:'power3.inOut', pivot:'left'})
div#mini_end(left: 1737px; top: 774px; width: 84px; height: 64px; border-radius: 0,8,8,0; background: #FFFFFFB8; pattern: hatch,45,#D2463A8C,11,5; border: 3px solid $red; in: fade {duration: 0.3})
p#mini_label(right: 99px; top: 690px; font-size: 32px; color: $red; pointer: below; in: {y:12, scale:0.85, opacity:0, duration:0.45, ease:'back.out(1.7)'}) 終了間際は避けて
p#mini_tick(left: "774;994"; top: 848px; width: 330px; font-size: 30px; color: $navy; text-align: "left;right"; in: fade {duration: 0.3, stagger: 0.1}) ×2 9:00;16:00 受付終了

# closing — 締めの 1 枚: 夕方の市役所 + 左から cream の幕・白い板 (札・新しい時刻・罫・お願い・足)・帯を閉じる
section#closing(stagger: {each:0})
img#closing_photo(inset: 0; aspect: 16:9; main: kb {scale: [1.14, 1.02], focus: ['70% 55%', '70% 55%'], ease:'power1.out'}) A modern Japanese city hall building seen across its small plaza in the late afternoon: warm golden light, long soft shadows, sky gradient from light blue to soft peach, trees glowing in the sun, a couple of people walking away calmly. Peaceful closing mood. Keep the left half of the image simple (open sky and plaza)
div#closing_veil(inset: 0; background: linear(#F6F1E68C@0%,#F6F1E640@50%,#F6F1E600@70%,90); in: none)
div#endcard(left: 110px; top: 196px; width: 1000px; height: 610px; border-radius: 36px; background: #FFFFFFED; box-shadow: 0px 30px 70px #142A4738; delay: 400; in: {y:50, opacity:0, duration:0.8, ease:'power3.out'})
  chip#pill(left: 64px; top: 58px; delay: 750; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'}) 新しい窓口開庁時間
  p#hours(left: 64px; top: 156px; font-size: 124px; color: $navy; line-height: 1.05; letter-spacing: 0.01em; nowrap: true; delay: 950; in: {y:164, duration:0.7, ease:'power3.out', clip:true}) 9:00{tilde_o}〜{/}16:00
  shape#rule(left: 64px; top: 321px; width: 872px; height: 4px; path: rect,r=0.5; background: $line; delay: 1500; in: {scaleX:0, duration:0.6, ease:'power2.inOut', pivot:'left'})
  p#msg(left: 64px; top: 354px; font-size: 44px; color: $navy; line-height: 1.4; delay: 1900; in: {y:18, opacity:0, duration:0.55, ease:'power3.out'}) ご来庁の前に、{o}開庁時間のご確認{/}を[br]お願いします
  svg#glyph(left: 64px; bottom: 45px; width: 34px; height: 34px; part: hall_gray; in: {y:12, opacity:0, duration:0.5, ease:'power3.out'})
  p#foot(left: 111px; bottom: 44px; font-size: 34px; color: $gray; in: {y:12, opacity:0, duration:0.5, ease:'power3.out'}) 市役所
```

```timeline.txt
#v2
cast n = "澄んだ明るい高めの声の30〜40代の女性ナレーター、公共施設の案内アナウンスのように明瞭で落ち着いた丁寧な口調"
silence head=0 tail=0
transition = wipe,700,dir=left,overlap=700,ease=power3.inOut,bars=#1F3A5F,5;#E8743B,12,se=swish_soft -3dB

# title — チャイムで開き、題は頭に組み上げて「変わります」で弾ませる
*** title
[>#subtitle]
bgm music
fade in,500
se chime_in +3dB +100
se fuwan -4dB +950
@n: [silence:1450]市役所からのお知らせです。
@: [silence:350]窓口の開庁時間が、[!#title_l2 to,{scale:1.05, duration:0.25, ease:'power2.out', pivot:'left'} -50][!#title_l2 to,{scale:1, duration:0.35, ease:'power2.inOut', pivot:'left'} +200]変わります。[silence:550]

# change — 「8時15分」「17時15分」で前の時刻が光る・「変更後は」の前に板を入れ替え「9時」「16時」で新しい時刻・判子
*** change
@n: [silence:450]これまで{ |、}窓口は、[|][!#before.t{open} recolor,$orange,duration=250 -50][!#before.t{open} punch,1.08,duration=1000 -50][=#before.t{open} duration=400 +600][♪pop -5dB -50]8時15分から、[!#before.t{close} recolor,$orange,duration=250 -50][!#before.t{close} punch,1.08,duration=1000 -50][=#before.t{close} duration=400 +600]17時15分まで、開いていました。
subtitle "変更後は 9時から16時までとなります"
@: [silence:850][!#before to,{x:-470, scale:0.92, duration:0.75, ease:'power3.inOut'} -450][♪swish -4dB -470][>#after -150][>#arrow_line][>#arrow_head +250][!#before to,{x:-470, scale:0.92, opacity:0.72, duration:0.4} +50]変更後は、[!#after.dial.mh to,{rotation:360, duration:0.9, ease:'power2.inOut'} -500][!#after.dial.hh to,{rotation:270, duration:0.9, ease:'power2.inOut'} -500][>#after.open -120][♪sparkle -3dB -80][>#after.sep +200]9時から、[>#after.close -120][>#hanko +450][♪stamp +2dB +650][!#after to,{y:8, duration:0.06, ease:'power1.out'} +670][!#hanko to,{y:8, duration:0.06, ease:'power1.out'} +670][!#after to,{y:0, duration:0.25, ease:'power2.out'} +730][!#hanko to,{y:0, duration:0.25, ease:'power2.out'} +730]16時までとなります。[silence:700]

# gaps — 「朝の」で 2 本目の棒・「45分遅く」「1時間15分早く」で差の枠と吹き出し・時間帯を言う所で斜線と ×・「窓口での」で注意の帯
*** gaps
@n: [silence:450][>#chart.label_after +300][>#chart.bar_after +400][>#chart.bar_after.t +1000]朝の受付開始は{ |、}これまでより、[>#chart.gap_am -150][>#chart.balloon_am -100][♪pop -5dB -100]45分遅く、
subtitle "夕方の受付終了は 1時間15分早くなります"
@| 夕方の受付終了は、[>#chart.gap_pm -150][>#chart.balloon_pm -100][♪pop -5dB -100]1時間15分早くなります。
@: [silence:600][>#chart.gap_am.hatch][>#chart.gap_am.xmark +50][!#chart.gap_am to,{scale:1.06, duration:0.18, yoyo:true, repeat:1, ease:'power1.inOut'} +60][♪down -4dB -50]8時15分から、9時まで。[>#chart.gap_pm.hatch +300][>#chart.gap_pm.xmark +350][!#chart.gap_pm to,{scale:1.04, duration:0.18, yoyo:true, repeat:1, ease:'power1.inOut'} +360][♪down -4dB +250]そして、16時から、17時15分までは、[|][>#chart.caution -200]窓口での手続きができなくなりますので、[|][!#chart.caution to,{scale:1.04, duration:0.2, yoyo:true, repeat:1, ease:'power1.inOut'}][♪ting -6dB -50]ご注意ください。[silence:600]

# reason — 文頭で見出し 3 行が順に上がり「ご理解」でお願いの札
*** reason
@n: [silence:450][>#reason_l1][>#reason_l2 +180][>#reason_l3 +360]より丁寧で正確な窓口サービスを続けていくための、見直しです。[>#reason_ask -150][♪fuwan -5dB -100]ご理解とご協力をお願いいたします。[silence:550]

# confirm — 「ホームページ」「広報紙」で札を 1 枚ずつ・「開庁時間を」でチェック
*** confirm
@n: [silence:450][>#confirm_l1 +200][>#confirm_l2 +400]ご来庁の前には、[|]市の[>#via_web -100][♪pop -5dB -50]ホームページや[>#via_paper -100][♪pop -5dB -50]広報紙などで、[>#confirm_dot +50][>#confirm_tick +250][♪up -5dB +100]開庁時間をご確認ください。[silence:500]

# tips — 「時間がかかる」で注記と受付の帯・「終了間際」で斜線と札・「時間に余裕」で語が弾む
*** tips
@n: [silence:450]手続きによっては、[>#tips_note -600][>#mini_bar +200][>#mini_tick[*] +600]時間がかかる場合があります。
subtitle "終了間際を避けて 時間に余裕をもってお越しください"
@| [>#mini_end -100][>#mini_label]終了間際を避けて、[!#tips_l2{o} punch,1.12,duration=440][♪up -5dB]時間に余裕をもってお越しください。[silence:600]
[<#banner]

# closing — 「9時から」で時刻が弾み「市役所から」で足・チャイムの後も札を最後の frame まで残す
*** closing
subtitle "新しい窓口の開庁時間は 9時から16時まで"
@n: [silence:450]新しい窓口の開庁時間は、[!#endcard.hours to,{scale:1.05, duration:0.25, ease:'power2.out', pivot:'left'} -80][!#endcard.hours to,{scale:1, duration:0.4, ease:'power2.inOut', pivot:'left'} +250][♪sparkle -3dB -80]9時から、16時まで。[>#endcard.foot -100][>#endcard.glyph -100]市役所からのお知らせでした。[silence:350][♪chime_out +3dB][silence:3200]
```

# data · ec-cart-abandon (hf 全力版の全量の写し — カゴ落ち、どこで起きている？・雑貨 EC のカゴ落ちを 9 章の暗い data 図解で) — canvas 1920x1080

見せる作り: 全編の常設の暗い地 (放射の地・点の格子・漂う 2 色の光)・題の写真と左の題札・場面を跨ぐ左上の店の札 (sticky)・場面の頭の 3 点 (英字の小札・見出し・右上の 9 本の進行)・半透明の板の design system (KPI の数え上げ・100 マス・ファネルの横棒と離脱の斜線・内訳の帯・折れ線と帯・2 本ずつの横棒・縦棒と送料の境の破線・A/B の流れ図・理由の横棒・手順の 3 枚・結論の 3 行)・語ごとに伸びる棒と数字 (cue で行の 5 印を 1 語に)・下端の黒い字幕札・音の層 (場面頭の風切り + 語ごとの電子音)

```design.txt
#v2
# 学ぶ作り: 暗い data の design system を根に 1 回 (palette・書体 4 つ・数字と単位の run・板 panel の def・場面の頭の 3 点 (英字の小札 kicker・見出し stitle・右上の進行 prog) の def) → 場面は板の中身だけ
# 全編の地は根に 1 回 (紺の放射の地 + 点の格子 + 周辺の減光 + 全編で漂う青緑と琥珀の光)・場面は 1 つの cut に 1 主題で、旧場面は section の out で上へ抜けて消え、新しい場面は境目から delay で組み上がる (切替は書かない)
# 板の中の図 (KPI の数え上げ・100 マス・ファネルの横棒と離脱の斜線・折れ線と帯・2 本ずつの横棒・縦棒と送料の境の破線・A/B の流れ図・理由の横棒・手順の 3 枚・結論の 3 行) は台詞の数字の語で伸ばし、cue で行ごとの 5 つの印を 1 語に畳む
# hf d01 ec-cart-abandon (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#0A0E14
theme dark
palette amber2=#E0892A lvt=#FFD0CA seg_ink=#1B0D0B white=#FFFFFF mock=#0F141B hot=#FFE1B0 tag_ink=#1A1206 no_ink=#0B1015 pay_ink=#C9F6EE ink=#EEF2F7 ink2=#B6C0CD ink3=#8B97A8 teal=#35D0BA coral=#FF6B5B amber=#FFB547 orange=#FF8F5A blue=#6EA8FF slate=#8592A6 slate2=#5B6B80 amber_l=#FFD28C teal_l=#9FF0E2 orange_l=#FFC2A3 coral_l=#FFB3AA a=#FFB547 b=#35D0BA
font "端正で癖のない現代的な日本語の角ゴシック体の太字 (Bold)、技術資料や UI 向け"
fonts m="標準の太さの角ゴシック体、字幕向けで読みやすい"
fonts n="極太の幾何学的な欧文サンセリフ体、ウェブやUIで定番のモダンな書体"
fonts c="等幅のプログラミング用の英数字の書体、すっきりした形"
sfx off
# hf の作り: 板の中の題・軸・凡例・注記は 1080 で 17〜24 px の小さな字 (small_text)・場面の頭の見出しと結論の行は台詞より先に出る (spoiler)・図だけの場面 (text_only_cut)
# hf の作り: 題の札は 3.6 秒の場面で順に出る・最後の注記は場面の末尾 2〜3 秒だけ (flash_text)・結論の行は台詞と同文・A/B の流れ図は同じ段名が 2 列 (duplicate_text)・離脱の斜線は件数より先に出る (empty_board)
lint off=small_text,spoiler,text_only_cut,flash_text,duplicate_text,empty_board
run sm { font-family: c; font-size: 16px; color: $ink3 }
run nb { font-family: n; color: $ink }
run n16 { font-family: n; font-size: 24px; color: $ink }
run n23 { font-family: n; font-size: 34px; color: $ink }
run pc { font-size: 0.49em }
run yen { font-size: 0.47em }
run u { font-size: 0.46em; color: $ink2; font-family: m }
run s12 { font-size: 18px; color: $ink3; font-family: m }
run s13 { font-size: 20px; color: $ink3; font-family: m }
run g27 { font-size: 40px; color: $ink }
run g33 { font-size: 50px; color: $ink3 }
run k17 { font-size: 26px }
run vs { font-size: 40px; color: $ink3 }
run am { color: $amber }
run co { color: $coral }
run cn { color: $coral; font-family: n }
run te { color: $teal }
run or { color: $orange }
run bl { color: $blue }
run sl { color: $slate }
run i2 { color: $ink2 }
run k { color: $ink }
sound whoosh = "短いノイズのスイープ、シュッと流れる場面転換の音"
sound swoosh = "柔らかく流れて締まる短いブリッジの効果音、最後の場面への転換"
sound title = "低めの落ち着いたビジネス系の電子音の一打、題が出る瞬間"
sound pop = "短く軽いシステムの電子音のポッ、札が出る"
sound tick = "ごく短く乾いたシステムのクリック音"
sound accent = "低めのビジネス系の短い強調の電子音、要の数字"
sound rise = "低めのビジネス系の上昇する電子音、増えたことを示す"
sound chime = "中低音のビジネス系の短いチャイム、手順の札"
sound end = "低めのビジネス系の締めの電子音、題の再掲"
# 行ごとの 5 つの印を 1 語に畳む (ファネルの段・端末別の段・A/B の段)
cue frow(r) = [>#r -200][>#r.nm -200][>#r.ct -200][>#r.rt -50][>#r.bar -100][>#r.lost +350]
cue drow(r) = [>#r][>#r.nm][>#r.sp +50][>#r.pc +170][>#r.vs +450][>#r.vp +450]
cue abrow(r) = [>#r][>#r.nm][>#r.a +50][>#r.b +200][>#r.va +450][>#r.vb +450]
image parcel = "[transparent]A small closed cardboard shipping box with a blank paper price tag tied with twine, minimal clean 3D render, warm soft key light from the upper left, gentle shadow underneath, the box fills the frame centered, isolated object on a transparent background. The tag is blank. No text, no letters, no numbers, no logos."
image phone = "[transparent]A modern smartphone seen from the front, slightly tilted, its screen showing a dark-mode online shop checkout page with a long stack of eleven empty rounded input fields (plain blank rectangles, no readable text) and a small amber button at the bottom. Clean minimal 3D product render, soft cool rim light, crisp edges, the phone fills the frame vertically and is centered, isolated object on a transparent background. No text, no letters, no logos, no hands."
p { color: $ink }
div { border: none }
# 字幕: 下端中央の半透明の黒い札 (細い白の縁)・声と同時に出て声の 0.1 秒後に消える・句末の読点と句点は外す・動きなし
subtitle.hug(bottom: 40px; font-size: 32px; font-family: m; line-height: 1.35; letter-spacing: 0.02em; color: #F3F6FA; background: #06090DC7; border: 2px solid #FFFFFF0F; border-radius: 12px; padding: 10px 26px 12px 26px; unit: sentence; strip: 、。; lead: 0; tail: 100; hold: off; in: none; out: none)
bgm#music(fade: 1600,3200) ジャズ寄りのエレクトロニカ、エレクトリックピアノとアップライトベースとシンセ、115 BPM 前後、淡々とクールで知的な企業紹介やデータ解説向け、主旋律は控えめ

# 板: ほぼ透明の白の地 + 細い縁 + 角丸 13 (影なし)・下から 16 px 上がって出る
def panel = div(background: #FFFFFF09; border: 2px solid #FFFFFF16; border-radius: 20px; in: {y:24, opacity:0, duration:0.6, ease:'power3.out'})
# 場面の頭の 3 点: 琥珀の等幅の英字の小札 → 31 px の見出し → 右上の進行 (番号 + 9 本の目盛り・済みは薄い琥珀・今は琥珀)
def kicker(t) = p(left: 96px; top: 104px; font-size: 18px; font-family: c; letter-spacing: 0.16em; color: $amber; delay: 220; in: {x:-20, opacity:0, duration:0.5, ease:'power3.out'}; content: {t})
def stitle(t) = p(left: 96px; top: 132px; font-size: 46px; line-height: 1.2; letter-spacing: 0.01em; delay: 300; in: {x:-28, opacity:0, duration:0.6, ease:'power3.out'}; content: {t})
def prog(t, c) = div(left: 1454px; top: 60px; width: 370px; height: 18px; delay: 320; in: {opacity:0, duration:0.4, ease:'power1.out'})
  p#t(left: 0px; cy: 50%; font-size: 16px; font-family: c; letter-spacing: 0.08em; color: $ink3; content: {t})
  div#i(left: "62;83;104;125;146;167;188;209;230"; cy: 50%; width: 26px; height: 4px; border-radius: 3px; background: {c}) ×9
# KPI の札 (上端の色の短い線 + 題 + 欧文の数字 (数え上げ) + 単位 + 等幅の注記)
def kpi(l, v, u, f, c) = div(top: 228px; width: 408px; height: 164px; background: #FFFFFF09; border: 2px solid #FFFFFF16; border-radius: 20px; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 28px; top: 0px; width: 64px; height: 4px; border-radius: 3px; background: {c})
  p#l(left: 28px; top: 18px; font-size: 22px; font-family: m; color: $ink2; content: {l})
  p#v(left: 26px; top: 58px; font-size: 62px; line-height: 1; font-family: n; content: {v})
  p#u(left: .v.right+10; top: 90px; font-size: 22px; font-family: m; color: $ink2; content: {u})
  p#f(left: 28px; top: 134px; font-size: 16px; font-family: c; color: $ink3; content: {f})
# 流れ図の札 (薄い地 + 細い縁)
def node(t) = p(font-size: 26px; font-family: m; color: $ink2; background: #FFFFFF0D; border: 2px solid #FFFFFF24; border-radius: 14px; padding: 16px 26px; content: {t})
# 丸い札 (琥珀 / 橙の薄い地 + 縁)
def pill(t) = p(font-size: 22px; font-family: m; color: $amber_l; background: #FFB54724; border: 2px solid #FFB5478C; border-radius: 148px; padding: 8px 18px; in: {scale:0.8, opacity:0, duration:0.5, ease:'back.out(1.6)'}; content: {t})
# 手順の板 (番号 + 等幅の STEP + 2 行の題)
def act(no, st, hd) = div(top: 236px; width: 544px; height: 664px; background: #FFFFFF09; border: 2px solid #FFFFFF16; border-radius: 20px; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  p#no(left: 32px; top: 22px; font-size: 92px; line-height: 1; font-family: n; color: $ink3; content: {no})
  p#st(left: 130px; top: 34px; font-size: 18px; font-family: c; letter-spacing: 0.12em; color: $ink3; content: {st})
  p#hd(left: 130px; top: 62px; width: 402px; font-size: 30px; line-height: 1.35; content: {hd})
# 小さな札 (手順の板の下端)
def chip(t) = p(font-size: 20px; font-family: m; color: $ink2; background: #FFFFFF0F; border: 2px solid #FFFFFF24; border-radius: 10px; padding: 8px 14px; in: {opacity:0, duration:0.4, ease:'power1.out'}; content: {t})
# 結論の行 (色の丸の番号 + 28 px の主文 + 注記・右端の数字は実体の子)
def crow(no, c, m, s) = div(left: 96px; width: 1728px; height: 196px; background: #FFFFFF09; border: 2px solid #FFFFFF16; border-radius: 20px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
  div#no(left: 32px; top: 50px; width: 64px; height: 64px; border-radius: 148px; background: {c})
    p#t(cx: 50%; cy: 50%; font-size: 32px; font-family: n; color: #0B1015; content: {no})
  p#m(left: 128px; top: 36px; font-size: 42px; line-height: 1.25; content: {m})
  p#s(left: 130px; top: 108px; width: 1180px; font-size: 26px; line-height: 1.45; font-family: m; color: $ink2; content: {s})

# 全編の地 (根・z back): 紺の放射の地 + 点の格子 (中央だけ見える) + 青緑の光 (左上) と琥珀の光 (右下) が全編でゆっくり逆へ漂う
# 光は hf の blur(135px) の円を放射の濃淡で写す: 円の芯 (36〜38%) まで満ち・円の縁で半分・箱の内接円 (70.7%) の手前の 70% で透明 (縁が出ない)・漂いは動画の全長 128 s
div#bg_base(inset: 0; background: radial(#111823,#0A0E14@60%,#080B10,30%,20%); z-index: back; in: none; out: none)
div#dots(inset: 0; pattern: dots,21,#FFFFFF0E; z-index: back; in: none; out: none)
div#dots_fade(inset: 0; background: radial(#0A0E1400@35%,#0A0E14@80%,50%,45%); z-index: back; in: none; out: none)
shape#glow1(left: -250px; top: -350px; width: 940px; height: 940px; border-radius: 50%; background: radial(#35D0BA13,#35D0BA13@36%,#35D0BA0A@57%,#35D0BA00@70%,50%,50%); z-index: back; in: none; out: none; main: keys(at=0 x=0 y=0 | at=1 x=280 y=107 ease=sine.inOut),window=0,128000,forwards)
shape#glow2(left: 1269px; top: 530px; width: 1000px; height: 1000px; border-radius: 50%; background: radial(#FFB5470D,#FFB5470D@38%,#FFB54707@58%,#FFB54700@70%,50%,50%); z-index: back; in: none; out: none; main: keys(at=0 x=0 y=0 | at=1 x=-253 y=-93 ease=sine.inOut),window=0,128000,forwards)

# title — 題: 夜の雑貨店の写真が 1.12 → 1.02 に引きながら明け、左の暗い空きに英字の小札 → 2 行の題 → 琥珀の短い線 → 副題 → 3 つの札
section#title(stagger: {each:0}; out: {opacity:0, duration:0.35, ease:'power2.in'})
img#hero(inset: 0; subject: right 40%; room: left 55%; main: kb {scale: [1.12, 1.02], ease:'power1.out'}; in: fade {duration: 0.9}) [photo]Cinematic low-key photograph of a cozy Japanese zakka (household goods) shop interior at night. Wooden shelves with handmade ceramic mugs, folded linen, small potted plants and glass jars, lit by a few warm pendant lamps. On a wooden counter in the right third of the frame sits a small woven wicker shopping basket with two items inside, left behind. Deep shadows, moody atmosphere, subtle teal and amber color grade, shallow depth of field, soft bokeh. The left half of the frame is very dark and uncluttered, leaving negative space for the title. No text, no letters, no logos, no people.
# 写真の暗幕: 左から右へ薄れる幕 + 下から上へ薄れる幕 (題の側を沈める)
div#shade_l(inset: 0; background: linear(#0A0E14F7,#0A0E14E6@34%,#0A0E1473@62%,#0A0E1433,90); in: none)
div#shade_b(inset: 0; background: linear(#0A0E14D9,#0A0E1400@34%,0); in: none)
p#kick(left: 120px; top: 262px; font-size: 22px; font-family: c; letter-spacing: 0.18em; color: $amber; delay: 250; in: {x:-24, opacity:0, duration:0.6, ease:'power3.out'}) EC FUNNEL REVIEW ｜ 直近4週間
p#h1a(left: 116px; top: 310px; font-size: 112px; line-height: 1.14; letter-spacing: 0.005em; delay: 400; in: {y:40, opacity:0, duration:0.8, ease:'power3.out'}) カゴ落ち、
p#h1b(left: 116px; top: 438px; font-size: 112px; line-height: 1.14; letter-spacing: 0.005em; delay: 560; in: {y:40, opacity:0, duration:0.8, ease:'power3.out'}) どこで起きている？
div#rule(left: 120px; top: 578px; width: 96px; height: 4px; border-radius: 3px; background: $amber; delay: 950; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
p#sub(left: 120px; top: 600px; font-size: 32px; font-family: m; color: $ink2; delay: 1050; in: {y:18, opacity:0, duration:0.6, ease:'power3.out'}) こもれび雑貨店 ｜ 購入ファネルの分析と、直す順番の提案
p#chip(left: "80;364;504"; top: 676px; font-size: 22px; font-family: m; color: $ink2; background: #0A0E148C; border: 2px solid #FFFFFF33; border-radius: 148px; padding: 10px 20px; delay: 1350; in: {y:14, opacity:0, duration:0.5, ease:'power3.out', stagger:{each:0.1}}) ×3 対象：こもれび雑貨店（架空の雑貨 EC）;期間：直近4週間;共有先：プロダクトチーム

# overview — 01 全体像: KPI の札 4 枚を語ごとに数え上げ・「67%」で大きな数字の板と 100 マス (67 マスが珊瑚・33 マスが青緑) が組み上がる・2 文目で送料の板 (箱の絵 + 550 円 + 流れ図) と「初めて」の札
section#overview(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#ov_k 01 — OVERVIEW
stitle#ov_t 全体像：直近4週間の購入データ
prog#ov_p(t: "01 / 09"; c: "$amber;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29")
# 左上の店の札 (琥珀の角丸の印 + 店名 + 細い縦線 + 題)・overview の頭で出て締めの直前まで cut を跨ぐ (.sticky)
div#brand.sticky(left: 96px; top: 46px; width: 360px; height: 30px; display: flex; gap: 14px; align-items: center; delay: 100; in: {opacity:0, duration:0.5, ease:'power1.out'}; out: {opacity:0, duration:0.4})
  div#mark(width: 26px; height: 26px; border-radius: 8px; background: linear($amber,$amber2,135))
    p#t(cx: 50%; cy: 50%; font-size: 16px; color: $tag_ink) こ
  p#b(font-size: 20px; white-space: nowrap) こもれび雑貨店
  div#i(width: 2px; height: 18px; background: #FFFFFF40)
  p#s(font-size: 20px; font-family: m; color: $ink3; white-space: nowrap) カゴ落ち分析
kpi#k1(left: 96px; l: 商品ページ閲覧; v: "[count:48,000 start=0 ms=1200 delay=50]"; u: セッション; f: 4週合計; c: $slate; delay: 450)
kpi#k2(left: 536px; l: カート投入; v: "[count:7,200 start=0 ms=1000 delay=50]"; u: 件; f: 閲覧の 15.0%; c: $teal)
kpi#k3(left: 976px; l: 購入完了; v: "[count:2,376 start=0 ms=1000 delay=50]"; u: 件; f: カートから 33.0%; c: $teal)
kpi#k4(left: 1416px; l: カゴ落ち（買わずに去った）; v: "[count:4,824 start=0 ms=1000 delay=50]"; u: 件; f: カート投入の 67%; c: $coral)
panel#ov_stat(left: 96px; top: 414px; width: 1080px; height: 306px)
  p#l(left: 40px; top: 30px; font-size: 26px; font-family: m; color: $ink2) カートに入れた人のうち
  p#big(left: 32px; top: 92px; font-size: 180px; line-height: 1; font-family: n; color: $coral) [count:67 start=0 ms=900 delay=100]{pc}%{/}
  p#side(left: 560px; top: 84px; font-size: 44px; line-height: 1.3; in: {y:16, opacity:0, duration:0.5, ease:'power3.out'}) {cn}4,824{/} 件が[br]買わずに去っている
  p#note(left: 560px; top: 214px; font-size: 20px; font-family: c; color: $ink3; in: {y:16, opacity:0, duration:0.5, ease:'power3.out'}) カート投入 7,200 件 = 100%
# 100 マス (10 × 10 の格子・1 マス ≒ 72 件・先頭から 12 ms ずつ弾んで出る)
panel#ov_waf(left: 1208px; top: 414px; width: 616px; height: 306px)
  div#sq(left: "24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186;24;42;60;78;96;114;132;150;168;186"; top: "13;13;13;13;13;13;13;13;13;13;31;31;31;31;31;31;31;31;31;31;49;49;49;49;49;49;49;49;49;49;67;67;67;67;67;67;67;67;67;67;85;85;85;85;85;85;85;85;85;85;103;103;103;103;103;103;103;103;103;103;121;121;121;121;121;121;121;121;121;121;139;139;139;139;139;139;139;139;139;139;157;157;157;157;157;157;157;157;157;157;175;175;175;175;175;175;175;175;175;175"; width: 22px; height: 22px; border-radius: 4px; background: "$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$coral;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal;$teal"; in: {scale:0.3, opacity:0, duration:0.35, ease:'back.out(1.6)', stagger:{each:0.012}}) ×100
  p#lg1(left: 340px; top: 30px; font-size: 20px; font-family: m; color: $ink2) {co}■{/} 買わずに去った
  p#lv1(left: 340px; top: 60px; font-size: 30px; font-family: n) 4,824 件
  p#lg2(left: 340px; top: 122px; font-size: 20px; font-family: m; color: $ink2) {te}■{/} 購入完了
  p#lv2(left: 340px; top: 152px; font-size: 30px; font-family: n) 2,376 件
  p#wn(left: 340px; top: 236px; font-size: 16px; line-height: 1.45; font-family: c; color: $ink3) 1マス ≒ 72件[br]（7,200件 = 100マス）
# 送料の板: 箱の絵 (板の上へはみ出す) + 送料 550 円 + カート → 配送先入力 → 支払い → 完了 の流れ図 + 「初めて」の札と細い茎
panel#ov_fee(left: 96px; top: 752px; width: 1728px; height: 168px; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  # hf の作り: 箱の絵は板の上へはみ出す (child_overflow)
  img#parcel(left: 8px; top: -30px; width: 220px; height: 220px; content: @parcel; object-fit: contain; main: none; in: {scale:0.7, opacity:0, duration:0.6, ease:'back.out(1.6)'})
  div#fl(left: 232px; top: 26px; width: 270px; height: 123px; in: {scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.6)'})
    p#t(left: 0px; top: 0px; font-size: 22px; font-family: m; color: $ink2) 送料
    p#v(left: 0px; top: 28px; font-size: 64px; line-height: 1.05; font-family: n; color: $amber) 550{yen}円{/}
    p#n(left: 0px; top: 96px; font-size: 21px; font-family: m; color: $ink2) 5,000円以上で無料
  shape#ar(left: "439;615;757"; top: 108px; width: 64px; height: 15px; path: arrow_r; background: #FFFFFF4D; border: 3px solid #FFFFFF4D; in: {x:-16, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.14}}) ×3
  node#nd(left: "347;489;665;807"; top: 84px; in: {x:-16, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.14}}; t: "カート;配送先入力;支払い;完了") ×4
  pill#first(left: 690px; top: 20px) ここで初めて送料が表示される
  div#stem(left: 864px; top: 62px; width: 2px; height: 22px; background: #FFB547B3; in: {opacity:0, duration:0.3})

# funnel — 02 ファネル: 板の頭に閲覧 → カートの行・カートの棒が伸び、「55%」「75%」「80%」で段ごとに棒と離脱の斜線・「33%」で購入率・2 文目で内訳の帯が 3 色に割れ、「最大の穴」で枠と札
section#funnel(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#fn_k 02 — FUNNEL
stitle#fn_t 購入ファネル：どの段で離れているか
prog#fn_p(t: "02 / 09"; c: "#FFB54773;$amber;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29")
panel#fn(left: 96px; top: 230px; width: 1728px; height: 452px; delay: 200)
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) 購入ファネル（4週合計）{sm}　前の段からの通過率{/}
  p#lg(right: 32px; top: 24px; font-size: 20px; font-family: m; color: $ink2) {te}■{/} 通過　{co}■{/} その段で離脱
  p#tp1(left: 32px; top: 76px; font-size: 21px; font-family: m; color: $ink2; delay: 450; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 商品ページ閲覧 {nb}48,000{/}
  div#ar1(left: 276px; top: 92px; width: 40px; height: 2px; background: #FFFFFF4D; delay: 530; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'})
  p#rate(left: 333px; top: 75px; font-size: 22px; font-family: n; color: $teal; background: #35D0BA1A; border-radius: 8px; padding: 2px 12px; delay: 610; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 15.0%
  div#ar2(left: 441px; top: 92px; width: 40px; height: 2px; background: #FFFFFF4D; delay: 690; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'})
  p#tp2(left: 498px; top: 76px; font-size: 21px; font-family: m; color: $ink2; delay: 770; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) カート {nb}7,200{/}
  p#f1n(left: 32px; top: 140px; font-size: 26px; font-family: m; delay: 750; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) カート
  p#f1c(left: 196px; top: 140px; width: 112px; text-align: right; font-size: 28px; font-family: n; delay: 750; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 7,200
  div#f1b(left: 470px; top: 134px; width: 1000px; height: 50px; border-radius: 0px 6px 6px 0px; background: $teal; delay: 800; in: {scaleX:0, duration:0.9, ease:'power3.out', pivot:'left'})
  # 段の行 ×3 (段名・件数・通過率の札・通過の棒 (幅 = 7,200 を 667 px)・離脱の斜線・離脱の件数)
  div#fr(left: 0px; top: "141;195;248"; width: 1728px; height: 54px) ×3
    p#nm(left: 32px; top: 8px; font-size: 26px; font-family: m; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 配送先入力;支払い;完了
    p#ct(left: 196px; top: 8px; width: 112px; text-align: right; font-size: 28px; font-family: n; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 3,960;2,970;2,376
    p#rt(left: 330px; top: 9px; width: 116px; text-align: center; font-size: 22px; font-family: n; color: $teal_l; background: #35D0BA1A; border: 2px solid #35D0BA59; border-radius: 10px; padding: 3px 0px; in: {scale:0.8, opacity:0, duration:0.4, ease:'back.out(1.6)'}) 55.0%;75.0%;80.0%
    div#bar(left: 470px; top: 2px; width: "367;275;220"; height: 50px; border-radius: 0px 6px 6px 0px; background: $teal; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
    div#lost(left: "680;588;533"; top: 2px; width: "300;92;55"; height: 50px; border-radius: 0px 6px 6px 0px; background: #FF6B5B33; pattern: hatch,45,#FF6B5B9E,7,3; border: 2px solid #FF6B5BBF; in: {opacity:0, duration:0.5, ease:'power1.out'})
    p#lv(left: "797;605;538"; top: 10px; font-size: "16;16;14"; font-family: n; color: #FFD0CA; text-shadow: 0px 2px 6px #00000099; in: {opacity:0, duration:0.4, ease:'power1.out'}) −3,240;−990;−594
  p#cvt(left: 1504px; top: 300px; font-size: 20px; line-height: 1.35; font-family: m; color: $ink2; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}) カートからの[br]購入率
  p#cvv(left: 1504px; top: 356px; font-size: 64px; line-height: 1.05; font-family: n; color: $teal; white-space: nowrap; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}) 33.0%
  div#hole(left: 1012px; top: 206px; width: 466px; height: 66px; border: 3px solid $amber; border-radius: 10px; box-shadow: 0px 0px 0px 6px #FFB5471F; overlap: fn.fr; in: {scale:1.08, opacity:0, duration:0.45, ease:'power3.out'})
  pill#holetag(left: 1168px; top: 296px) ▲ 最大の穴：カートの直後
# 内訳の帯 (3 色に割れて左から伸びる・下に段ごとの件数)
panel#brk(left: 96px; top: 706px; width: 1728px; height: 214px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) カゴ落ち {nb}4,824{/} 件の内訳{sm}　どの段で去ったか{/}
  div#seg(left: "21;765;992"; top: 70px; width: "743;226;137"; height: 56px; background: "$coral;#FF6B5B9E;#FF6B5B61"; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left', stagger:{each:0.18}}) ×3
    p#v(left: 18px; top: 12px; font-size: 26px; font-family: n; color: "#1B0D0B;#FFFFFF;#FFFFFF") 67%;21%;12%
  p#sl1(left: 32px; top: 140px; font-size: 21px; font-family: m; color: $ink2; in: {opacity:0, duration:0.5, ease:'power1.out'}) カートで去る {k}3,240件{/}
  p#sl2(left: 1148px; top: 140px; font-size: 21px; font-family: m; color: $ink2; in: {opacity:0, duration:0.5, ease:'power1.out'}) 配送先入力で {k}990件{/}
  p#sl3(right: 32px; top: 140px; font-size: 21px; font-family: m; color: $ink2; in: {opacity:0, duration:0.5, ease:'power1.out'}) 支払いで {k}594件{/}

# weekly — 03 週次: 0〜50% の軸の板に、語で折れ線を左から描き、点と値が 0.42 秒おきに弾み、32〜34% の帯が開く・右に 3 枚の札 (最後は琥珀の「読み取り」)
section#weekly(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#wk_k 03 — WEEKLY
stitle#wk_t 週ごとの推移：カートからの購入率
prog#wk_p(t: "03 / 09"; c: "#FFB54773;#FFB54773;$amber;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29")
panel#wk(left: 96px; top: 230px; width: 1150px; height: 690px; delay: 200)
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) カート投入 → 購入完了の割合{sm}　週ごと・縦軸 0〜50%{/}
  div#gl(left: 110px; top: "336;272;208;144;80"; width: 980px; height: 2px; background: #FFFFFF12; delay: 400; in: {opacity:0, duration:0.5}) ×5
  div#base(left: 110px; top: 600px; width: 980px; height: 2px; background: #FFFFFF47; delay: 400; in: {opacity:0, duration:0.5})
  p#ax(left: 30px; top: "392;328;264;200;136;72"; width: 66px; text-align: right; font-size: 16px; font-family: c; color: $ink3; delay: 400; in: {opacity:0, duration:0.5}) ×6 0%;10%;20%;30%;40%;50%
  p#xl(cx: "147;320;493;667"; top: 627px; font-size: 22px; font-family: m; color: $ink2; delay: 400; in: {opacity:0, duration:0.5}) ×4 第1週;第2週;第3週;第4週
  div#band(left: 110px; top: 273px; width: 980px; height: 20px; background: #35D0BA29; in: {scaleY:0, opacity:0, duration:0.6, ease:'power3.out'})
  p#bandl(right: 64px; top: 243px; font-size: 20px; font-family: c; color: $teal_l; in: {opacity:0, duration:0.4}) 32〜34% の帯
# 折れ線・点・値は板の外 (canvas の座標の path は枠を持てない) に板の上へ重ねる
shape#wk_line(path: "M211 335 L384 348 L557 335 L731 349"; background: none; border: 3px solid $teal; in: draw {duration: 1.4})
shape#wk_dot(left: "206;379;552;726"; top: "330;343;330;344"; width: 16px; height: 16px; border-radius: 50%; background: #0F141B; border: 3px solid $teal; in: {scale:0.2, opacity:0, duration:0.35, ease:'back.out(1.6)', stagger:{each:0.42}}) ×4
p#wk_pl(cx: "211;384;557;731"; top: "303;367;303;368"; font-size: 28px; font-family: n; in: {y:8, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.42}}) ×4 34.0%;32.0%;34.0%;31.9%
panel#wc1(left: 1278px; top: 230px; width: 546px; height: 196px; delay: 600; in: {x:24, opacity:0, duration:0.6, ease:'power3.out'})
  p#t(left: 30px; top: 26px; font-size: 21px; font-family: m; color: $ink2) カート投入（1週あたり）
  p#v(left: 30px; top: 64px; font-size: 52px; line-height: 1.05; font-family: n) 1,750〜1,850{u} 件{/}
  p#n(left: 30px; top: 134px; font-size: 20px; font-family: m; color: $ink3) 母数は毎週ほぼ同じ規模
panel#wc2(left: 1278px; top: 450px; width: 546px; height: 196px; in: {x:24, opacity:0, duration:0.6, ease:'power3.out'})
  p#t(left: 30px; top: 26px; font-size: 21px; font-family: m; color: $ink2) カートからの購入率
  p#v(left: 30px; top: 64px; font-size: 52px; line-height: 1.05; font-family: n; color: $teal) 32〜34%{u} で横ばい{/}
  p#n(left: 30px; top: 134px; font-size: 20px; font-family: m; color: $ink3) 4週とも同じ帯に収まる
panel#wc3(left: 1278px; top: 670px; width: 546px; height: 250px; background: #FFB54712; border: 2px solid #FFB5478C; in: {x:24, opacity:0, duration:0.6, ease:'power3.out'})
  p#t(left: 30px; top: 26px; font-size: 21px; font-family: m; color: $amber_l) 読み取り
  p#q(left: 30px; top: 69px; font-size: 34px; line-height: 1.4) 特定の週の事故ではなく、[br]{am}構造的な離脱{/}

# device — 04 端末別: 左の板で「70%」を数えスマホ / PC の割合の帯と端末の絵・右の板で段ごとに 2 本ずつの横棒 (橙 = スマホ・青 = PC) が順に伸び、「全段」で札・「30%対40%」で購入率・「入力の重さ」で 2 段目の題が琥珀に
section#device(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#dv_k 04 — DEVICE
stitle#dv_t デバイス別：スマホと PC
prog#dv_p(t: "04 / 09"; c: "#FFB54773;#FFB54773;#FFB54773;$amber;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29")
panel#dl(left: 96px; top: 230px; width: 520px; height: 690px; delay: 200)
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) カート投入 7,200 件の内訳
  p#big(left: 32px; top: 76px; font-size: 128px; line-height: 1; font-family: n; color: $orange; in: none) [count:70 start=0 ms=800]{pc}%{/}
  p#bt(left: 300px; top: 124px; font-size: 32px; in: {opacity:0, duration:0.4}) がスマホ
  div#sp(left: 32px; top: 214px; width: 318px; height: 40px; border-radius: 6px 0px 0px 6px; background: $orange; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#pc(left: 351px; top: 214px; width: 136px; height: 40px; border-radius: 0px 6px 6px 0px; background: $blue; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  p#sl1(left: 32px; top: 268px; font-size: 20px; font-family: m; color: $ink2; in: {opacity:0, duration:0.4}) スマホ {n16}5,040{/}
  p#sl2(left: 300px; top: 268px; font-size: 20px; font-family: m; color: $ink2; in: {opacity:0, duration:0.4}) PC {n16}2,160{/}
  img#phone(left: 40px; top: 300px; width: 440px; height: 380px; content: @phone; object-fit: contain; main: none; in: {y:30, opacity:0, duration:0.8, ease:'power3.out'})
panel#dr(left: 648px; top: 230px; width: 1176px; height: 690px; delay: 350)
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) 段ごとの通過率{sm}　前の段から{/}
  p#lg(right: 32px; top: 24px; font-size: 20px; font-family: m; color: $ink2) {or}■{/} スマホ　{bl}■{/} PC
  pill#all(left: 32px; top: 70px; color: $orange_l; background: #FF8F5A21; border: 2px solid #FF8F5A8C) すべての段で スマホ ＜ PC
  div#row(left: 0px; top: "93;172;251"; width: 1176px; height: 110px) ×3
    p#nm(left: 32px; top: 4px; font-size: 24px; font-family: m; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) カート → 配送先入力;配送先入力 → 支払い;支払い → 完了
    div#sp(left: 380px; top: 0px; width: "245;341;365"; height: 34px; border-radius: 0px 4px 4px 0px; background: $orange; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    div#pc(left: 380px; top: 42px; width: "284;369;388"; height: 34px; border-radius: 0px 4px 4px 0px; background: $blue; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#vs(left: "508;603;628"; top: 0px; font-size: 26px; line-height: 1.35; font-family: n; in: {opacity:0, duration:0.35}) 52.5%{s12} 2,646件{/};73.0%{s12} 1,932件{/};78.3%{s12} 1,512件{/}
    p#vp(left: "547;631;651"; top: 42px; font-size: 26px; line-height: 1.35; font-family: n; in: {opacity:0, duration:0.35}) 60.8%{s12} 1,314件{/};79.0%{s12} 1,038件{/};83.2%{s12} 864件{/}
  p#note(left: 32px; top: 302px; font-size: 18px; line-height: 1.45; font-family: m; color: $amber_l; in: {x:-10, opacity:0, duration:0.45, ease:'power3.out'}) 住所・電話番号など[br]11 項目の手入力
  div#cvl(left: 32px; top: 500px; width: 1110px; height: 2px; background: #FFFFFF16)
  p#cvt(left: 32px; top: 522px; font-size: 22px; font-family: m; color: $ink2) カートからの購入率
  div#cs(left: 32px; top: 558px; width: 510px; height: 75px; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'})
    p#d(left: 0px; top: 33px; font-size: 24px; font-family: m) {or}●{/} スマホ
    p#v(left: .d.right+14; top: 0px; font-size: 72px; line-height: 1; font-family: n; color: $orange) 30.0%
    p#c(left: .v.right+14; top: 45px; font-size: 18px; font-family: c; color: $ink3) 1,512 / 5,040
  div#cp(left: 591px; top: 558px; width: 510px; height: 75px; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'})
    p#d(left: 0px; top: 33px; font-size: 24px; font-family: m) {bl}●{/} PC
    p#v(left: .d.right+14; top: 0px; font-size: 72px; line-height: 1; font-family: n; color: $blue) 40.0%
    p#c(left: .v.right+14; top: 45px; font-size: 18px; font-family: c; color: $ink3) 864 / 2,160

# value — 05 金額帯: 0〜60% の軸の板に灰の縦棒 3 本が下から伸び、「3割前後」で括りと札・「5000円以上」で送料の境の破線と琥珀の 4 本目・「50.3%」で値が弾む・右の板に箱の絵と 3 行の読み
section#value(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#vl_k 05 — CART VALUE
stitle#vl_t カート金額帯別の購入率
prog#vl_p(t: "05 / 09"; c: "#FFB54773;#FFB54773;#FFB54773;#FFB54773;$amber;#FFFFFF29;#FFFFFF29;#FFFFFF29;#FFFFFF29")
panel#vc(left: 96px; top: 230px; width: 1200px; height: 690px; delay: 200)
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) カート投入 → 購入完了の割合{sm}　金額帯別・縦軸 0〜60%{/}
  div#gl(left: 90px; top: "280;187;93"; width: 1060px; height: 2px; background: #FFFFFF12) ×3
  div#base(left: 90px; top: 560px; width: 1060px; height: 2px; background: #FFFFFF47)
  p#ax(left: 10px; top: "365;272;179;85"; width: 66px; text-align: right; font-size: 16px; font-family: c; color: $ink3) ×4 0%;20%;40%;60%
  div#col(left: "83;237;390"; top: "243;238;247"; width: 150px; height: "131;135;126"; border-radius: 6px 6px 0px 0px; background: $slate2; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom', stagger:{each:0.12}}) ×3
  div#c4(left: 885px; top: 208px; width: 150px; height: 352px; border-radius: 6px 6px 0px 0px; background: $amber; in: {scaleY:0, duration:0.9, ease:'power3.out', pivot:'bottom'})
  p#cv(cx: "133;287;440"; top: "208;203;213"; font-size: 40px; font-family: n; in: {opacity:0, duration:0.4}) ×3 28.0%;29.0%;27.0%
  p#cv4(cx: 960px; top: 156px; font-size: 40px; font-family: n; color: $amber; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(1.6)'}) 50.3%
  p#cl(cx: "133;287;440;640"; top: 578px; font-size: 22px; font-family: m; color: "$ink;$ink;$ink;$amber_l"; delay: 500; in: {opacity:0, duration:0.5}) ×4 3,000円未満;3,000〜3,999円;4,000〜4,999円;5,000円以上
  p#cs(cx: "133;287;440;640"; top: 616px; font-size: 18px; font-family: c; color: $ink3; delay: 500; in: {opacity:0, duration:0.5}) ×4 カート投入の 34%;カート投入の 26%;カート投入の 18%;カート投入の 22%
  shape#dv(left: 798px; top: 120px; width: 3px; height: 456px; path: line_v; background: #FFB547B3; border: 3px solid #FFB547B3; dash: 6,5; in: {scaleY:0, duration:0.6, ease:'power3.out', pivot:'top'})
  p#dvl(left: 812px; top: 96px; font-size: 20px; font-family: m; color: $amber_l; in: {opacity:0, duration:0.4}) ← 送料あり ｜ 送料無料 →
  # 送料がかかる 3 本を括る線 (上辺 + 両端の短い縦線)
  div#bk(left: 116px; top: 286px; width: 640px; height: 18px; in: {scaleX:0.6, opacity:0, duration:0.45, ease:'power3.out'})
    div#t(left: 0px; top: 0px; width: 640px; height: 3px; background: #B6C0CDB3)
    div#l(left: 0px; top: 0px; width: 3px; height: 18px; background: #B6C0CDB3)
    div#r(left: 638px; top: 0px; width: 3px; height: 18px; background: #B6C0CDB3)
  p#bkl(cx: 436px; top: 236px; font-size: 24px; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) 送料がかかる帯：{i2}どこも{/} 3割前後
panel#vr(left: 1328px; top: 230px; width: 496px; height: 690px; delay: 350)
  img#parcel(left: 150px; top: 24px; width: 230px; height: 230px; content: @parcel; object-fit: contain; main: none; delay: 250; in: {scale:0.7, opacity:0, duration:0.6, ease:'back.out(1.6)'})
  p#l1(left: 32px; top: 290px; font-size: 26px; line-height: 1.45; delay: 450; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) 送料 550円[br]{s13}5,000円以上で無料{/}
  p#l2(left: 32px; top: 410px; font-size: 26px; line-height: 1.45; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) 送料がかかる帯は[br]どこも 3割前後
  p#l3(left: 32px; top: 540px; font-size: 26px; line-height: 1.45; color: $amber_l; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) 無料になる帯だけ[br]購入率が倍近い

# abtest — 06 A/B: 「送料をカートで」で A と B の流れ図の板 (送料の札が出る段だけ琥珀)・「半分ずつ」で段の板と結果の板・2 文目で段ごとに灰と青緑の棒・「30.8%」「33.3%」で購入率・3 文目で「+2.5 ポイント」と「約 180 件」
section#abtest(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#ab_k 06 — A/B TEST
stitle#ab_t 送料の表示位置を比べた（2週間）
prog#ab_p(t: "06 / 09"; c: "#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;$amber;#FFFFFF29;#FFFFFF29;#FFFFFF29")
panel#aba(left: 96px; top: 230px; width: 852px; height: 172px; in: {y:22, opacity:0, duration:0.6, ease:'power3.out'})
  p#bd(left: 28px; top: 24px; font-size: 22px; font-family: n; color: #0B1015; background: $slate; border-radius: 8px; padding: 4px 14px) A
  p#tt(left: 112px; top: 22px; font-size: 26px) 現行：配送先入力で送料を表示
  p#ppl(right: 30px; top: 18px; font-size: 22px; color: $ink2) {n23}1,500{/}人
  shape#ar(left: "90;217;316"; top: 104px; width: 34px; height: 15px; path: arrow_r; background: #FFFFFF4D; border: 3px solid #FFFFFF4D) ×3
  node#nd(left: "19;118;245;344"; top: 84px; font-size: 21px; padding: 14px 18px; color: "$ink2;#FFE1B0;$ink2;$ink2"; background: "#FFFFFF0D;#FFB5471F;#FFFFFF0D;#FFFFFF0D"; border: "2px solid #FFFFFF24;2px solid #FFB547D9;2px solid #FFFFFF24;2px solid #FFFFFF24"; t: "カート;配送先入力;支払い;完了") ×4
  p#tag(left: 276px; top: 68px; font-size: 16px; color: #1A1206; background: $amber; border-radius: 148px; padding: 2px 10px; overlap: aba.nd[2]; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(1.6)'}) 送料
panel#abb(left: 972px; top: 230px; width: 852px; height: 172px; in: {y:22, opacity:0, duration:0.6, ease:'power3.out'})
  p#bd(left: 28px; top: 24px; font-size: 22px; font-family: n; color: #0B1015; background: $teal; border-radius: 8px; padding: 4px 14px) B
  p#tt(left: 112px; top: 22px; font-size: 26px) カートで送料を表示
  p#ppl(right: 30px; top: 18px; font-size: 22px; color: $ink2) {n23}1,500{/}人
  shape#ar(left: "90;217;316"; top: 104px; width: 34px; height: 15px; path: arrow_r; background: #FFFFFF4D; border: 3px solid #FFFFFF4D) ×3
  node#nd(left: "19;118;245;344"; top: 84px; font-size: 21px; padding: 14px 18px; color: "#FFE1B0;$ink2;$ink2;$ink2"; background: "#FFB5471F;#FFFFFF0D;#FFFFFF0D;#FFFFFF0D"; border: "2px solid #FFB547D9;2px solid #FFFFFF24;2px solid #FFFFFF24;2px solid #FFFFFF24"; t: "カート;配送先入力;支払い;完了") ×4
  p#tag(left: 86px; top: 68px; font-size: 16px; color: #1A1206; background: $amber; border-radius: 148px; padding: 2px 10px; overlap: abb.nd[1]; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(1.6)'}) 送料
p#ab_note(cx: 960px; top: 412px; font-size: 20px; font-family: m; color: $ink3; in: {opacity:0, duration:0.5}) 4週の後の2週間 ｜ カートに入れた人を半分ずつ A・B に分けて比較
panel#abr(left: 96px; top: 452px; width: 1170px; height: 468px)
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) 段ごとの通過率{sm}　前の段から（人数）{/}
  p#lg(right: 32px; top: 24px; font-size: 20px; font-family: m; color: $ink2) {sl}■{/} A 現行　{te}■{/} B カートで表示
  div#row(left: 0px; top: "56;140;224"; width: 1170px; height: 110px) ×3
    p#nm(left: 32px; top: 2px; font-size: 24px; font-family: m; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) カート → 配送先入力;配送先入力 → 支払い;支払い → 完了
    div#a(left: 330px; top: 0px; width: "235;299;341"; height: 32px; border-radius: 0px 4px 4px 0px; background: $slate; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    div#b(left: 330px; top: 40px; width: "222;341;341"; height: 32px; border-radius: 0px 4px 4px 0px; background: $teal; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#va(left: "463;527;569"; top: 0px; font-size: 22px; line-height: 1.4; font-family: n; in: {opacity:0, duration:0.35}) 55.0%{s12} 825人{/};70.1%{s12} 578人{/};79.9%{s12} 462人{/}
    p#vb(left: "450;569;569"; top: 40px; font-size: 22px; line-height: 1.4; font-family: n; in: {opacity:0, duration:0.35}) 52.0%{s12} 780人{/};80.0%{s12} 624人{/};80.0%{s12} 499人{/}
  p#n1(left: 32px; top: 126px; font-size: 20px; color: $ink3; in: {x:-10, opacity:0, duration:0.4, ease:'power3.out'}) B はカートで少し早く去る
  p#n2(left: 32px; top: 252px; font-size: 20px; color: $teal_l; in: {x:-10, opacity:0, duration:0.4, ease:'power3.out'}) B は離脱が大きく減る
panel#abs(left: 1290px; top: 452px; width: 534px; height: 468px)
  p#t(left: 32px; top: 24px; font-size: 22px; font-family: m; color: $ink2) 購入率（カート投入 → 完了）
  div#ra(left: 32px; top: 70px; width: 183px; height: 108px; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'})
    p#k(left: 0px; top: 0px; font-size: 20px; color: $ink2) A 現行
    p#v(left: 0px; top: 44px; font-size: 51px; line-height: 1.05; font-family: n; color: $slate; white-space: nowrap) 30.8%
  div#arr(left: 214px; top: 140px; width: 34px; height: 2px; background: #FFFFFF59; in: {opacity:0, duration:0.3})
  div#rb(left: 262px; top: 70px; width: 255px; height: 114px; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'})
    p#k(left: 0px; top: 0px; font-size: 20px; color: $teal_l) B カートで表示
    p#v(left: 0px; top: 34px; font-size: 72px; line-height: 1.05; font-family: n; color: $teal; white-space: nowrap) 33.3%
  p#plus(left: 32px; top: 210px; font-size: 92px; line-height: 1; font-family: n; color: $amber; in: {scale:0.7, opacity:0, duration:0.6, ease:'back.out(1.6)'}) +2.5{pc}ポイント{/}
  p#gain(left: 32px; top: 326px; width: 470px; font-size: 21px; line-height: 1.45; font-family: m; color: $ink2; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) 4週のカート投入 7,200件に当てはめると[br]{g27}約 180 件の購入増{/}

# survey — 07 アンケート: 左の板にクリップボードの絵が傾きから起き上がり対象と回答数・右の板の 6 行の横棒が 0.16 秒おきに伸び、語で 1 行目と 3 行目の題が色づき値が弾む・「スマホ」で札
section#survey(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#sv_k 07 — SURVEY
stitle#sv_t 離脱した人に聞いた理由
prog#sv_p(t: "07 / 09"; c: "#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;$amber;#FFFFFF29;#FFFFFF29")
panel#svl(left: 96px; top: 230px; width: 500px; height: 690px; delay: 200)
  img#clip(left: 70px; top: 30px; width: 360px; height: 360px; object-fit: contain; main: none; delay: 300; in: {rotation:-4, y:20, opacity:0, duration:0.8, ease:'power3.out'}) [transparent]A clipboard holding a short questionnaire sheet with six rows of blank checkbox options (plain lines instead of words, no readable text), one checkbox ticked in amber, and a pen resting diagonally on it. Minimal clean 3D render, soft lighting, the clipboard fills the frame centered, isolated object on a transparent background. No text, no letters, no logos.
  # 対象と回答 (小さな題 + 23 px の値・題と値は別の文字にして行の高さを分ける)
  p#m1l(left: 36px; top: 420px; font-size: 22px; color: $ink2; delay: 600; in: {opacity:0, duration:0.5}) 対象
  p#m1v(left: 36px; top: 452px; width: 458px; font-size: 34px; line-height: 1.45; delay: 600; in: {opacity:0, duration:0.5}) カートに入れて買わなかった[br]会員
  p#m2l(left: 36px; top: 568px; font-size: 22px; color: $ink2; delay: 600; in: {opacity:0, duration:0.5}) 回答
  p#m2v(left: 36px; top: 600px; font-size: 34px; line-height: 1.45; delay: 600; in: {opacity:0, duration:0.5}) 400 人・1つ選択
panel#svr(left: 628px; top: 230px; width: 1196px; height: 690px; delay: 350)
  p#pt(left: 32px; top: 22px; font-size: 22px; font-family: m; color: $ink2) 買わなかった理由{sm}　回答 400 人・%（人数）{/}
  div#q(left: 0px; top: "61;123;184;245;307;368"; width: 1196px; height: 84px) ×6
    p#nm(left: 32px; top: 6px; width: 420px; font-size: 24px; font-family: m; delay: "500;660;820;980;1140;1300"; in: {opacity:0, duration:0.35}) 送料が思ったより高い;ほかの店と比較・検討中だった;入力が面倒;使いたい支払い方法がない;届く日が遅い;その他
    div#b(left: 470px; top: 2px; width: "354;251;194;137;114;91"; height: 40px; border-radius: 0px 6px 6px 0px; background: "$amber;$slate2;$orange;$slate2;$slate2;$slate2"; delay: "550;710;870;1030;1190;1350"; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
    p#v(left: "677;574;517;460;437;414"; top: 2px; font-size: 28px; line-height: 1.4; font-family: n; delay: "900;1060;1220;1380;1540;1700"; in: {opacity:0, duration:0.3}) 31%{s13} 124人{/};22%{s13} 88人{/};17%{s13} 68人{/};12%{s13} 48人{/};10%{s13} 40人{/};8%{s13} 32人{/}
  pill#sp(left: 924px; top: 274px; color: $orange_l; background: #FF8F5A21; border: 2px solid #FF8F5A8C) 大半はスマホから

# actions — 08 直す順番: 「まず」で 1 枚目 (琥珀の縁・カートの見本の板の送料無料までの目盛りが伸び「あと ◯◯円」の札)・「次に」で 2 枚目 (端末の絵 + 11 → 6 項目・6 が青緑に)・「そして」で 3 枚目 (支払い方法の 3 行)・板の間に ›
section#actions(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
kicker#ac_k 08 — NEXT ACTIONS
stitle#ac_t 直す順番の提案
prog#ac_p(t: "08 / 09"; c: "#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;$amber;#FFFFFF29")
act#a1(left: 96px; no: 1; st: "STEP 1 ｜ まず"; hd: "送料をカートで表示し、[br]あといくらで無料かを出す"; background: #FFB5470D; border: 2px solid #FFB54799)
  p#no(color: $amber)
  div#mock(left: 32px; top: 222px; width: 480px; height: 250px; border-radius: 16px; background: #0F141B; border: 2px solid #FFFFFF1F; in: {y:14, opacity:0, duration:0.5, ease:'power3.out'})
    p#fl(left: 24px; top: 30px; font-size: 21px; font-family: m; color: $ink2) 送料
    p#fv(right: 24px; top: 30px; font-size: 21px; color: $amber) 550円
    p#ll(left: 24px; top: 84px; font-size: 18px; font-family: m; color: $ink3) 送料無料ライン
    p#lv(right: 24px; top: 84px; font-size: 18px; font-family: m; color: $ink3) 5,000円
    div#mt(left: 24px; top: 132px; width: 432px; height: 10px; border-radius: 6px; background: #FFFFFF1A)
    div#mf(left: 24px; top: 132px; width: 310px; height: 10px; border-radius: 6px; background: linear(#D98B2B,#FFB547,90); in: {scaleX:0, duration:0.9, ease:'power3.out', pivot:'left'})
    p#msg(left: 24px; top: 164px; width: 432px; font-size: 21px; color: #FFE1B0; background: #FFB5471F; border: 2px solid #FFB54773; border-radius: 10px; padding: 12px 16px; in: {scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.6)'}) あと ◯◯円で送料無料
  chip#ch(left: "21;176;21"; top: "363;363;397"; color: "$amber_l;$amber_l;$ink2"; background: "#FFB54721;#FFB54721;#FFFFFF0F"; border: "2px solid #FFB5478C;2px solid #FFB5478C;2px solid #FFFFFF24"; t: "比較で効果を確認済み;実装が軽い;+2.5pt ／ 4週で約180件") ×3
act#a2(left: 688px; no: 2; st: "STEP 2 ｜ 次に"; hd: "スマホの配送先入力を[br]短くする")
  img#phone(left: 20px; top: 190px; width: 260px; height: 300px; content: @phone; object-fit: contain; main: none; in: {y:24, opacity:0, duration:0.7, ease:'power3.out'})
  p#k(left: 270px; top: 230px; font-size: 20px; line-height: 1.4; font-family: m; color: $ink2; in: {opacity:0, duration:0.4}) 郵便番号から[br]住所を自動入力
  p#big(left: 270px; top: 302px; font-size: 64px; line-height: 1; font-family: n; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'}) {g33}11{/} → {six}6{/}{k17}項目{/}
  chip#ch(left: 32px; top: 596px) 「入力が面倒」17%・大半はスマホ
act#a3(left: 1280px; no: 3; st: "STEP 3 ｜ そして"; hd: 後払い・コンビニ払いを足す)
  p#pay(left: 32px; top: "153;205;257"; width: 480px; font-size: 24px; font-family: m; color: "$ink2;#C9F6EE;#C9F6EE"; background: "#FFFFFF0A;#35D0BA14;#35D0BA14"; border: "2px solid #FFFFFF1F;2px solid #35D0BA99;2px solid #35D0BA99"; border-radius: 14px; padding: 16px 22px; in: {x:-14, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.15}}) ×3 いまの支払い方法;{te}＋{/} 後払い;{te}＋{/} コンビニ払い
  chip#ch(left: "21;175"; top: 596px; t: "支払いでの離脱 594件;「支払い方法がない」12%") ×2
shape#chev(left: "436;831"; top: 543px; width: 14px; height: 30px; path: chevron; background: none; border: 3px solid #FFFFFF59; in: {opacity:0, duration:0.4}) ×2

# conclusion — 09 結論: 文ごとに結論の行が下から 1 本ずつ (番号の丸の色 = 珊瑚・橙・琥珀)・右端に要の数字・3 行目の「送料をカートで」が語で琥珀に
section#conclusion(stagger: {each:0}; out: {y:-10, opacity:0, duration:0.35, ease:'power2.in'})
kicker#cc_k 09 — CONCLUSION
stitle#cc_t 結論
prog#cc_p(t: "09 / 09"; c: "#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;#FFB54773;$amber")
crow#e1(top: 236px; no: 1; c: $coral; m: "カゴ落ちの {am}3分の2{/} は、カートの直後"; s: "送料を知る前ではなく、「知った瞬間」の驚きが効いている")
  p#s(in: {opacity:0, duration:0.5})
  p#kv(right: 40px; top: 36px; font-size: 60px; line-height: 1.15; font-family: n; color: $coral) 3,240件
  p#kl(right: 40px; top: 111px; font-size: 20px; font-family: m; color: $ink3) カゴ落ち 4,824件のうち
crow#e2(top: 456px; no: 2; c: $orange; m: "スマホは全段で PC より低い"; s: "差は入力の重さ ── 住所・電話番号など 11 項目の手入力")
  p#kv(right: 40px; top: 40px; font-size: 60px; line-height: 1; font-family: n) {or}30.0%{/} {vs}vs{/} {bl}40.0%{/}
  p#kl(right: 40px; top: 111px; font-size: 20px; font-family: m; color: $ink3) 購入率 スマホ / PC
crow#e3(top: 676px; no: 3; c: $amber; m: "まず{em}送料をカートで{/}見せ、次にスマホの入力を短く"; s: "比較で +2.5 ポイント ── 4週のカート投入に当てはめて約 180 件の購入増")
  p#kv(right: 40px; top: 36px; font-size: 60px; line-height: 1.15; font-family: n; color: $amber) +2.5pt
  p#kl(right: 40px; top: 111px; font-size: 20px; font-family: m; color: $ink3) 送料の表示位置の比較

# endcard — 締め: 暗い幕が溶けて籠の絵が 0.85 → 1 に・題の再掲と副題と琥珀の短い線
section#endcard(stagger: {each:0})
div#endbg(inset: 0; background: #080B10F0; delay: 150; in: {opacity:0, duration:0.7, ease:'power2.out'})
img#basket(left: 820px; top: 230px; width: 280px; height: 280px; object-fit: contain; main: none; in: {scale:0.85, y:16, opacity:0, duration:1.0, ease:'power3.out'}) [transparent]A small woven shopping basket holding a ceramic mug, a rolled linen towel and a tiny potted plant, minimal clean 3D render with soft warm lighting and gentle shadow, three-quarter view, the basket fills the frame centered, isolated object on a transparent background. No text, no letters, no logos.
p#end_t(cx: 960px; top: 548px; font-size: 56px; delay: 150; in: {y:14, opacity:0, duration:0.8, ease:'power3.out'}) カゴ落ち、どこで起きている？
p#end_s(cx: 960px; top: 632px; font-size: 24px; font-family: m; color: $ink2; delay: 270; in: {y:14, opacity:0, duration:0.8, ease:'power3.out'}) こもれび雑貨店 ｜ 購入ファネル分析（直近4週間）
div#end_r(left: 912px; top: 694px; width: 96px; height: 4px; border-radius: 3px; background: $amber; delay: 150; in: {opacity:0, duration:0.7})
```

```timeline.txt
#v2
cast n = "低く落ち着いた30〜40代の男性のナレーター、滑らかで信頼感のある声、社内向けの分析報告を淡々と明瞭に読む" speed=107%
silence head=0 tail=0
# 切替は書かない (旧場面は section の out で上へ抜けて消え、新しい場面は境目から組み上がる・地は常設)。場面の頭に風切り・声は境目の 0.35 秒後から

*** title
[>#subtitle]
bgm music
se title -2dB +120
@n: [silence:0.8s]カゴ落ち、どこで起きている？[silence:0.4s]

*** overview
se whoosh -5dB +20
@n: [silence:0.35s][♪pop -6dB +230]直近4週間で、カートに入った[>#k2 -150][>#k3 +700][♪pop -6dB][♪pop -6dB +715]{7,200|7200}件のうち、[|][>#ov_stat -350][>#ov_waf -200][>#ov_waf.sq[*] +100][♪accent -3dB]67%、[>#k4 -150][>#ov_stat.side -50][>#ov_stat.note -50][♪pop -6dB]{4,824|4824}件が買わずに去っています。[silence:0.35s]
@: [>#ov_fee -100]送料は[>#ov_fee.parcel -200][>#ov_fee.fl -100][>#ov_fee.nd[*] +600][>#ov_fee.ar[*] +670][♪pop -6dB]550円。いまは[!#ov_fee.nd[2] tint,$amber][♪tick -7dB]配送先入力の画面で、[>#ov_fee.first -100][>#ov_fee.stem -100][♪accent -3dB]初めて表示されます。[silence:0.2s]

*** funnel
se whoosh -5dB +20
@n: [silence:0.35s]カートから先の通過率は[frow fn.fr[1]][♪tick -7dB]55%、[frow fn.fr[2]][♪tick -7dB]75%、[frow fn.fr[3]][♪tick -7dB]80%。購入率は[>#fn.cvt -400][>#fn.cvv -400][♪accent -3dB]33%です。[silence:0.35s]
@: [>#brk -100]カゴ落ちの[>#brk.seg[*] -50][>#brk.sl1 +300][>#brk.sl2 +300][>#brk.sl3 +300][♪pop -6dB]3分の2、[|][>#fn.fr[1].lv -200][>#fn.fr[2].lv -200][>#fn.fr[3].lv -200][!#brk.sl1{k} recolor,$coral_l,duration=300]{3,240|3240}件はカートで去っています。[>#fn.hole -150][>#fn.holetag][♪accent -3dB]最大の穴は、カートの直後です。[silence:0.2s]

*** weekly
se whoosh -5dB +20
@n: [silence:0.35s]週ごとでも[>#wk_line -300][>#wk_dot[*] -200][>#wk_pl[*] -100][>#wk.band +1300][>#wk.bandl +1500][>#wc2 +1200][♪tick -7dB]32から34%で横ばい。[>#wc3 -100]特定の週の事故ではなく、[♪accent -3dB]構造的な離脱です。[silence:0.2s]

*** device
se whoosh -5dB +20
@n: [silence:0.35s]カート投入の[>#dl.big -300][>#dl.bt][>#dl.sp -100][>#dl.pc +350][>#dl.sl1 +400][>#dl.sl2 +400][>#dl.phone +600][drow dr.row[1] +900][drow dr.row[2] +1350][drow dr.row[3] +1800][♪pop -6dB]70%はスマホ。スマホは[>#dr.all -50][♪tick -7dB]全段でPCより低く、購入率は[>#dr.cs -200][>#dr.cp +450][♪accent -3dB]30%対40%。差は[>#dr.note -100][!#dr.row[2].nm recolor,$amber_l,duration=300][♪pop -6dB]入力の重さです。[silence:0.2s]

*** value
se whoosh -5dB +20
@n: [silence:0.35s]金額帯別では、[>#vc.col[*] -200][>#vc.cv[*] +350]送料がかかる帯はどれも[>#vc.bk -150][>#vc.bkl -50][>#vr.l2][♪pop -6dB]3割前後。無料になる[>#vc.dv -200][>#vc.dvl][>#vc.c4 +300][♪tick -7dB]{5,000円|5000円}以上だけが、[|][>#vc.cv4 -100][>#vr.l3 +200][♪accent -3dB]50.3%と倍近くです。[silence:0.2s]

*** abtest
se whoosh -5dB +20
@n: [silence:0.35s]そこで、[>#aba -300][>#abb +100][>#aba.tag +450][>#abb.tag +700][♪pop -6dB]送料をカートで見せる案を、[>#ab_note -100]2週間、[|][>#abr -300][>#abs -150][♪tick -7dB]半分ずつに分けて試しました。[silence:0.35s]
@: [abrow abr.row[1] +100][>#abr.n1 +900][♪tick -7dB]カートで去る人は少し増えるものの、[|][abrow abr.row[2] -100][>#abr.n2 +800][abrow abr.row[3] +1600][♪pop -6dB]配送先入力での離脱が大きく減り、[|]購入率は[>#abs.ra -150][♪tick -7dB]30.8%から[>#abs.arr -300][>#abs.rb -150][♪pop -6dB]33.3%へ。[silence:0.35s]
@: [>#abs.plus][♪rise -3dB]プラス2.5ポイント、[|]4週分なら[>#abs.gain -200][♪accent -3dB]約180件の購入増です。[silence:0.2s]

*** survey
se whoosh -5dB +20
@n: [silence:0.35s]アンケートでも、[|]最多は[!#svr.q[1].nm recolor,$amber_l,duration=300][♪accent -3dB]「送料が思ったより高い」の[!#svr.q[1].v punch,1.12,duration=500,pivot=left]31%。[!#svr.q[3].nm recolor,$orange_l,duration=300][♪pop -6dB]「入力が面倒」の[!#svr.q[3].v punch,1.12,duration=500,pivot=left]17%は、大半が[>#svr.sp -100][♪pop -6dB]スマホからでした。[silence:0.2s]

*** actions
se whoosh -5dB +20
@n: [silence:0.35s]直す順番は3つ。[>#a1 -300][>#a1.mock +200][♪chime -4dB]まず、送料をカートで見せ、[>#a1.mock.mf -300][>#a1.mock.msg][>#a1.ch[*] +600]あといくらで無料かを出す。[silence:0.35s]
@: [>#chev[*] -400][>#a2 -200][>#a2.phone +300][>#a2.k +600][♪chime -4dB]次に、スマホの配送先入力を[>#a2.big -100]11項目から[!#a2.big{six} recolor,$teal,duration=300][>#a2.ch +400][♪pop -6dB]6項目へ。[>#a3 -200][♪chime -4dB]そして、[>#a3.pay[*] -100][>#a3.ch[*] +500]後払いとコンビニ払いを足します。[silence:0.25s]

*** conclusion
se swoosh -5dB +20
@n: [silence:0.35s]カゴ落ちの[>#e1 -300][♪pop -6dB]3分の2はカートの直後。効いているのは送料を[>#e1.s -200]知った瞬間の[>#e2 -200][♪pop -6dB +200]驚きです。[>#e3 -200][!#e3.m{em} recolor,$amber,duration=300 +200][♪accent -3dB]まず送料をカートで見せ、[|]次にスマホの入力を短くしましょう。[<#brand -200][silence:0.25s]

*** endcard
se end -2dB
@n: [silence:2.15s]
```

# data · side-job-survey (hf 全力版の全量の写し — 会社員の副業、1,000 人調査・夜の部屋の題の絵から 7 枚の図の板を横に送る縦型の調査速報 (1,000 点の単位図・折れ線・アイコンつき横棒・縦棒・帯グラフ・ドーナツ)) — canvas 720x1280

見せる作り: 全編の紺の地と漂う琥珀 / 空色の光と薄い方眼・上端の進行線・開幕の全面の絵に字ごとに上がる 2 行の題と結論の札 (人の形 4 つ)・2 場面目から常設の題の札と出典・場面ごとに上がる章の番号・同じ骨組みの板 (def board) を右から入れて左へ抜き、縁が板の隙間を走る wipe で cut を継ぐ・語で伸びる図 (区画ごとに塗る 1,000 点の単位図と数え上げの札・折れ線と差の括弧・アイコンつき横棒の 1 位の点灯・縦棒の 6 割の括弧と中央値の破線・4 色の帯を沈めて 1 本を弾ませる・琥珀の枠の数え上げとメーター・時間別の 2 本の棒・ドーナツの弧)・まとめの 3 枚と絵つきの締めの枠・音の層 (BGM + 語に結んだ効果音 + 切替のスイープ)

```design.txt
#v2
# 学ぶ作り: 全編の地は根に 1 回 (紺の地 + 全編でゆっくり漂う琥珀と空色の光 + 薄い方眼)・上端の進行線・2 場面目から常設の枠 (左上の題の札・下の出典) を sticky で、右上の章の番号は場面ごとに上がる
# 場面は同じ骨組みの板 (def board = 番号の札 + 見出し + 母数 + 罫) を板ごとの in / out で右から入れて左へ抜く。cut の境目は縁が 2 枚の板の隙間を走る wipe で継ぐ (地と常設の枠は動かない)
# 板の中の図 (1,000 点の単位図・折れ線・アイコンつき横棒・縦棒・帯グラフ・ドーナツ) は台詞の数字の語で伸ばす。単位図は「点の模様の svg を区画ごとに 1 枚」を wipe で左から塗る (1,000 個の要素を置かない)
# hf d15 side-job-survey (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 720x1280 bg=#0B1322
theme dark
palette bg=#0B1322 board=#101B30 bline=#22314F ink=#F3F5F9 ink2=#C3CCDD muted=#8B99B3 amber=#FFB21A sand=#F3D699 sky=#4FC3F7 slate=#3C4A66 bar=#4A5B7D coral=#FF6B6B teal=#2FC4B2 gray6=#6B7A96 seg1=#2B4570 seg2=#3A5F96 seg3=#5684C0 cta=#0E1830
font "字面が大きく字間の詰まった現代的な日本語の角ゴシック体の極太 (Extra Bold)、画面の見出しや資料の UI 向けの読みやすい書体"
fonts x="字面が大きく字間の詰まった現代的な日本語の角ゴシック体の極太 (Extra Bold)、画面の見出しや資料の UI 向けの読みやすい書体" r="字面が大きく字間の詰まった現代的な日本語の角ゴシック体の標準の太さ (Regular)、癖がなく読みやすい本文用" n="縦長で幅の狭いコンデンスドの欧文サンセリフの太字、数字が細長く力強い"
art "フラットなベクターのエディトリアル・イラスト、幾何学的な形、柔らかいグラデーション、うっすら紙の粒子。色は深い紺 #0B1322・ミッドナイトブルー #16233D・暖かい琥珀 #FFB21A・柔らかい白 #F3F5F9・少しの空色 #4FC3F7 に限る"
prompt_tail "文字・数字・ロゴ・透かしは入れない"
sfx off
# hf の作り: 板の見出し・母数・凡例・注記は場面の頭に出し台詞が後から読む (spoiler)・注記と母数は 15〜17 px (hf の 22〜26 px の 2/3)
lint off=spoiler,small_text
# hf の作り: 場面 2〜8 は紺の地に図の板だけ (text_only_cut)・「分かれ目は、時間。」の大見出しは台詞と同じ語 (duplicate_text)・最後の空色 / 灰の点と 47% の値は板が押し出される直前に出る (entrance_in_fadeout)・推移の右の「14.1% → 23.4%」は場面の終わり際に出る (flash_text)
lint off=text_only_cut,duplicate_text,entrance_in_fadeout,flash_text
# hf の作り: 板の入れ替えは前の声の最後の 0.3 秒に掛かって始まる (transition_over_speech)
lint off=transition_over_speech
run a = color=$amber
run s = color=$sky
run c = color=$coral
run w = color=$ink
run nb = size=19 color=$ink2 font=n
run sm = size=15 color=$muted font=r
run pc = size=40
run pp = size=23 color=$muted font=n
run ps = size=16 color=$muted font=r
run num = size=100 color=$amber font=n
run na = size=29 color=$amber font=n
run big = size=43 color=$coral font=n
run dt = size=11 color=$ink2
run nw = size=27 color=$ink font=n
run na2 = size=27 color=$amber font=n
run h = color=$sky
p { color: $ink; out: none }
div { padding: 0px; border: none; box-shadow: none; border-radius: 0px; background: none; out: none }
shape { out: none }
svg { out: none }
img { out: none }
sound telop = "ニュース番組のテロップが出る明るい電子音のジングル"
sound whoosh = "短いノイズのスイープのシュッという場面転換の音"
sound whoosh_big = "カメラが大きく動くような重めのシュッという風切り音"
sound pop = "短く軽いサイバーなポップの電子音"
sound count = "数字が回るサイバーな電子のカウント音"
sound hit = "短く締まった単発のアクセントの打音"
sound tick = "短く軽いアクセントのティックという電子音"
# 人の形 (琥珀 1 + 灰 3)・単位図の点の模様 (1 区画 = 1 枚・18 px おきに直径 14 の点・列優先で左から 234 / 92 / 385 / 289)
# 写さなかった動き: hf は 1,000 個の点が 1〜3 ms おきに 0.2 → 1 倍で弾んで出る — ここは区画の wipe で左から塗るだけ (点ごとの弾みは無い)
svg pa = """<svg viewBox="0 0 56 92"><circle cx="28" cy="16" r="14" fill="#ffb21a"/><path d="M4 92 V54 a24 24 0 0 1 48 0 V92 Z" fill="#ffb21a"/></svg>"""
svg pg = """<svg viewBox="0 0 56 92"><circle cx="28" cy="16" r="14" fill="#56647f"/><path d="M4 92 V54 a24 24 0 0 1 48 0 V92 Z" fill="#56647f"/></svg>"""
svg waf_base = """<svg viewBox="0 0 716 446"><defs><pattern id="p" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="6" fill="#22304b"/></pattern></defs><rect x="0" y="0" width="716" height="446" fill="url(#p)"/></svg>"""
svg waf_c1 = """<svg viewBox="0 0 716 446"><defs><pattern id="p" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="7" fill="#ffb21a"/></pattern></defs><g fill="url(#p)"><rect x="0" y="0" width="162" height="446"/><rect x="162" y="0" width="18" height="162"/></g></svg>"""
svg waf_c2 = """<svg viewBox="0 0 716 446"><defs><pattern id="p" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="7" fill="#f3d699"/></pattern></defs><g fill="url(#p)"><rect x="162" y="162" width="18" height="284"/><rect x="180" y="0" width="54" height="446"/><rect x="234" y="0" width="18" height="18"/></g></svg>"""
svg waf_c3 = """<svg viewBox="0 0 716 446"><defs><pattern id="p" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="7" fill="#4fc3f7"/></pattern></defs><g fill="url(#p)"><rect x="234" y="18" width="18" height="428"/><rect x="252" y="0" width="252" height="446"/><rect x="504" y="0" width="18" height="198"/></g></svg>"""
svg waf_c4 = """<svg viewBox="0 0 716 446"><defs><pattern id="p" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="7" fill="#3c4a66"/></pattern></defs><g fill="url(#p)"><rect x="504" y="198" width="18" height="248"/><rect x="522" y="0" width="194" height="446"/></g></svg>"""
# 折れ線 (面のグラデ + 線)・差の括弧・6 割の括弧・中央値の破線
svg trend = """<svg viewBox="0 0 880 680"><defs><linearGradient id="ag" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb21a" stop-opacity="0.32"/><stop offset="1" stop-color="#ffb21a" stop-opacity="0"/></linearGradient></defs><polygon points="160,600 160,346.2 330,279.6 500,229.2 670,178.8 670,600" fill="url(#ag)"/><polyline points="160,346.2 330,279.6 500,229.2 670,178.8" fill="none" stroke="#ffb21a" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/></svg>"""
svg brk = """<svg viewBox="0 0 20 112"><path d="M0 1.35 H12 Q18.65 1.35 18.65 8 V104 Q18.65 110.65 12 110.65 H0" fill="none" stroke="#ffb21a" stroke-width="2.7"/></svg>"""
svg brk5 = """<svg viewBox="0 0 177 17"><path d="M1.35 17 V7 Q1.35 1.35 7 1.35 H170 Q175.65 1.35 175.65 7 V17" fill="none" stroke="#ffb21a" stroke-width="2.7"/></svg>"""
svg vdash = """<svg viewBox="0 0 4 249"><line x1="2" y1="0" x2="2" y2="249" stroke="#f3f5f9" stroke-width="2.7" stroke-dasharray="8 8"/></svg>"""
# 全編の地 (根・z back): 左上の琥珀の光と右下の空色の光が全編 (47.7 秒) で一定の速さで漂い、40 px おき (hf の 60 px) の薄い方眼が下へ流れる・上端の進行線は動画の終わりまで伸びる
div#glow1.bleed(left: -347px; top: -373px; width: 933px; height: 933px; border-radius: 467px; background: radial(#FFB21A29,#FFB21A00@62%,50%,50%); z-index: back; in: none; main: keys(at=0 x=-40 y=-20 | at=1 x=53 y=40 ease=none),window=0,47700,forwards)
div#glow2.bleed(left: 147px; top: 560px; width: 1000px; height: 1000px; border-radius: 500px; background: radial(#4FC3F721,#4FC3F700@62%,50%,50%); z-index: back; in: none; main: keys(at=0 x=40 y=27 | at=1 x=-60 y=-33 ease=none),window=0,47700,forwards)
div#grid.bleed(left: -40px; top: -40px; width: 800px; height: 1360px; pattern: grid,40,#FFFFFF04; z-index: back; in: none; main: keys(at=0 y=0 | at=1 y=40 ease=none),window=0,47700,forwards)
progress#prog(left: 0px; top: 0px; width: 720px; height: 5px; background: $amber; until: end; z-index: front)
bgm#music(fade: 150,1400) 明るく軽快なピアノのリズム、124 BPM、前向きでポップな情報番組の調査速報向けの曲
# 字幕: 暗い札の太字・数字は台詞の {a} で琥珀・句末の。は外す・場面 1 は下に寄せた変種
subtitle.hug(left: 27px; top: 875px; width: 667px; height: 113px; font-size: 32px; line-height: 1.32; letter-spacing: .01em; color: #FFFFFF; background: #040912C7; border-radius: 12px; padding: 9px 20px 11px 20px; text-align: center; unit: sentence; strip: 。; wrap: comma,24; lead: 60; in: {y:12, opacity:0, duration:.16, ease:'power2.out'})
subtitle.low(top: 1042px)

# 板の骨組み: 番号の札 + 見出し + 右の母数 + 罫・板は右から入り左へ抜ける (hf の boardIn / boardOut・x 1100 px の 2/3)
def board(k, t, n) = div(left: 37px; top: 124px; width: 645px; height: 733px; background: $board; border: 1.3px solid $bline; border-radius: 20px; box-shadow: 0px 27px 60px #00000059; in: {x:733, duration:.5, ease:'power3.inOut'}; out: {x:-733, duration:.5, ease:'power3.inOut'})
  p#k(left: 29px; cy: 43px; font-size: 17px; font-family: n; color: $bg; background: $ink; border-radius: 5px; padding: 4px 8px 3px 8px; line-height: 1; content: {k})
  p#t(left: 73px; cy: 43px; font-size: 29px; white-space: nowrap; content: {t})
  p#n(right: 29px; cy: 43px; font-size: 16px; font-family: r; color: $muted; white-space: nowrap; content: {n})
  div#rule(left: 29px; top: 77px; width: 587px; height: 1.3px; background: $bline)
# 右上の章の番号 (場面ごとに下から上がる・前の場面の番号は cut の終わりで消える)
def chap(no) = p(right: 37px; top: 33px; font-size: 23px; font-family: n; color: $muted; letter-spacing: .06em; in: {y:16, opacity:0, duration:.3, ease:'power3.out'}; content: "{w}{no}{/} / 07")
# 主役の数字の札: 色の角 + 題 + 大きな % (数える) + 人数
def stat(l, v, c) = div(width: 284px; height: 132px; background: #FFFFFF08; border: 1.3px solid $bline; border-radius: 13px; in: {y:20, opacity:0, duration:.35, ease:'power3.out'})
  div#sq(left: 17px; cy: 22px; width: 15px; height: 15px; border-radius: 4px; background: {c})
  p#l(left: 40px; cy: 22px; font-size: 19px; color: $ink2; white-space: nowrap; content: {l})
  p#v(left: 17px; top: 40px; font-size: 79px; font-family: n; color: {c}; line-height: 1.05; white-space: nowrap; content: {v})
# 凡例の行: 色の角 + 札 + 点線の引き出し + % + 人数 (右揃え)
def lg(t, v, p, c, ll, lw) = div(width: 587px; height: 34px; in: {x:-13, opacity:0, duration:.3, ease:'power2.out'})
  div#sq(left: 0px; cy: 50%; width: 17px; height: 17px; border-radius: 5px; background: {c})
  p#t(left: 26px; cy: 50%; font-size: 19px; color: $ink2; white-space: nowrap; content: {t})
  shape#ld(left: {ll}; cy: 50%; width: {lw}; height: 2px; path: line_h; border: 1.3px solid #33456A; dash: 2,3)
  p#v(right: 66px; cy: 50%; font-size: 23px; font-family: n; white-space: nowrap; content: {v})
  p#p(right: 0px; cy: 50%; width: 57px; font-size: 15px; font-family: r; color: $muted; text-align: right; content: {p})

# hook — 開幕: 夜の部屋で副業する人の全面の絵が引き、左上に「調査速報」と 2 行の題が字ごとに上がる →「4人に1人」で結論の札と人の形 4 つ
section#hook(stagger: {each:0}; out: {x:-733, duration:.5, ease:'power3.inOut'})
img#hero(inset: 0; subject: bottom 45%; room: top 50%; main: kb {scale: [1.12, 1], focus: ['50% 70%', '50% 70%']}) 夜遅く、東京の小さなアパートの机で、ネクタイを緩めた白いシャツの30代前半の日本人の会社員がノートパソコンで副業をしている。暖かい琥珀色のデスクライトが顔と手を照らし、机にはマグカップとスマートフォン。背後の大きな窓には深い青の夜の街の高層ビルの灯り。落ち着いた集中した雰囲気。縦長の構図: 人物と机は画面の下 45% に収め、上半分は柔らかなグラデーションの暗い夜空だけの広い余白 (題を置く場所) にする
div#shade(inset: 0; background: linear(#0B1322EB,#0B13228C@34%,#0B132200@52%,#0B132200@72%,#0B1322BF,180); in: none)
p#stamp_chip(left: 48px; cy: 113px; font-size: 23px; color: $bg; background: $amber; border-radius: 5px; padding: 8px 13px 7px 13px; letter-spacing: .04em; line-height: 1; in: {x:-40, opacity:0, duration:.35, ease:'power3.out'}) 調査速報
p#stamp_d(left: 181px; cy: 113px; font-size: 23px; font-family: n; color: $ink2; letter-spacing: .08em; in: {x:-40, opacity:0, duration:.35, ease:'power3.out'}) 2026.09
p#t1(left: 44px; top: 157px; font-size: 69px; line-height: 1.15; letter-spacing: .01em; white-space: nowrap; delay: 40; in: {y:40, opacity:0, duration:.34, ease:'back.out(1.6)', stagger:.03}) 会社員の副業、
p#t2(left: 44px; top: 240px; font-size: 69px; line-height: 1.15; white-space: nowrap; delay: 260; in: {y:47, opacity:0, duration:.38, ease:'back.out(1.6)', stagger:.05}) {num}1,000{/}人調査
div#bar(left: 48px; top: 365px; width: 200px; height: 7px; border-radius: 3px; background: $amber; delay: 550; in: {scaleX:0, duration:.5, ease:'power3.out', pivot:'left'})
p#src(left: 48px; top: 388px; font-size: 20px; font-family: r; color: $ink2; letter-spacing: .02em; delay: 650; in: {y:9, opacity:0, duration:.35}) ミナトリサーチ｜20〜59歳の正社員・ネット調査
# 結論の札 (暗い板 + 琥珀の縁)・人の形は 1 つ目だけ琥珀で弾む
div#head(left: 44px; top: 460px; width: 632px; height: 160px; background: #080E1BD1; border: 1.3px solid #FFB21A8C; border-radius: 17px; in: {y:47, scale:.94, opacity:0, duration:.45, ease:'back.out(1.5)'})
  p#lbl(left: 24px; top: 22px; font-size: 20px; color: $ink2) 副業をしている会社員は
  p#big(left: 24px; top: 64px; font-size: 49px; white-space: nowrap) {a}4人に1人{/}に近づく
  svg#ppl(left: "455;492;529;566"; top: 66px; width: 32px; height: 53px; part: "pa;pg;pg;pg"; in: {y:27, opacity:0, duration:.3, ease:'back.out(2)', stagger: {each: .07}}) ×4

# status — 01 副業の状況: 常設の枠が入り、1,000 点の地が左から敷かれ「23.4%」で琥珀の点と札が数え、続く語で淡い砂色、「38.5%」で空色、最後に灰
section#status(stagger: {each:0})
# 常設の枠 (sticky): 左上の題の札・下の出典
div#hdr.sticky(left: 37px; top: 33px; width: 560px; height: 73px; delay: 310; in: {y:-20, opacity:0, duration:.4, ease:'power3.out'})
  p#chip(left: 0px; cy: 19px; font-size: 17px; color: $bg; background: $amber; border-radius: 5px; padding: 7px 11px 6px 11px; letter-spacing: .04em; line-height: 1) 調査速報
  p#ttl(left: 105px; cy: 19px; font-size: 23px; white-space: nowrap) 会社員の副業、{na}1,000{/}人調査
  p#sub(left: 0px; top: 52px; font-size: 15px; font-family: r; color: $muted; letter-spacing: .02em; white-space: nowrap) 20〜59歳の正社員（会社員）1,000人・ネット調査｜2026年9月
chap#c1(no: "01"; delay: 60)
p#ftr.sticky(cx: 360px; top: 1004px; font-size: 15px; font-family: r; color: $muted; letter-spacing: .02em; delay: 410; in: {opacity:0, duration:.4}) 出典：ミナトリサーチ（架空の調査会社）「会社員の副業調査」2026年9月
board#b2(k: "01"; t: "副業の状況"; n: "回答者 {nb}1,000{/}人")
  stat#st1(left: 29px; top: 96px; l: "いま副業をしている"; v: "[count:23.4 start=0 ms=750 delay=200]{pc}%{/}{pp} 234{/}{ps}人{/}"; c: $amber)
  stat#st2(left: 332px; top: 96px; l: "始めたいが、していない"; v: "[count:38.5 start=0 ms=750 delay=200]{pc}%{/}{pp} 385{/}{ps}人{/}"; c: $sky)
  p#waf_unit(right: 28px; cy: 256px; font-size: 15px; font-family: r; color: $muted; delay: 860; in: {opacity:0, duration:.3}) {dt}●{/} 1つ＝1人
  svg#waf_base(left: 84px; top: 267px; width: 477px; height: 297px; part: waf_base; delay: 410; in: wipe {dir: 'right', duration: 0.9, ease: 'power2.inOut'})
  svg#waf_c1(left: 84px; top: 267px; width: 477px; height: 297px; part: waf_c1; in: wipe {dir: 'right', duration: 0.64})
  svg#waf_c2(left: 84px; top: 267px; width: 477px; height: 297px; part: waf_c2; in: wipe {dir: 'right', duration: 0.5})
  svg#waf_c3(left: 84px; top: 267px; width: 477px; height: 297px; part: waf_c3; in: wipe {dir: 'right', duration: 0.68})
  svg#waf_c4(left: 84px; top: 267px; width: 477px; height: 297px; part: waf_c4; in: wipe {dir: 'right', duration: 0.52})
  lg#lg(left: 29px; top: "571;609;647;685"; t: "いま副業をしている;過去にしていた;始めたいが、していない;関心なし"; v: "23.4%;9.2%;38.5%;28.9%"; p: "234人;92人;385人;289人"; c: "$amber;$sand;$sky;$slate"; ll: "206;168;244;111"; lw: "256;304;218;351") ×4

# trend — 02 推移: 目盛りと「4人に1人 (25%)」の破線が出て、折れ線が左から引かれ点が順に弾む →「14.1%」で最初の点 →「9.3ポイント」で差の破線・括弧・札と上の大きな数字
section#trend(stagger: {each:0})
chap#c2(no: "02"; delay: 60)
board#b3(k: "02"; t: "副業をしている割合の推移"; n: "各年 {nb}1,000{/}人")
  p#hr3_pre(left: 29px; top: 162px; font-size: 27px; color: $ink2; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) 3年で
  p#hr3_big(left: 109px; top: 112px; font-size: 100px; font-family: n; color: $amber; line-height: 1; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) +9.3
  p#hr3_post(left: 305px; top: 158px; font-size: 29px; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) ポイント
  p#hr3_side(right: 28px; top: 138px; font-size: 17px; font-family: r; color: $muted; line-height: 1.45; text-align: right; in: {x:20, opacity:0, duration:.4}) {nw}14.1%{/} → {na2}23.4%{/}[br]2023年 → 2026年
  # 目盛り (横線 4 本 + 左の %)・年の札 (頭に 20 ms ずつ)
  div#gl(left: 90px; top: "631;511;391;271"; width: 513px; height: 1.3px; background: $bline; delay: 260; in: {opacity:0, duration:.35, stagger: {each: .02}}) ×4
  p#gy(left: 29px; top: "620;500;380;260"; width: 51px; font-size: 17px; font-family: n; color: $muted; text-align: right; delay: 260; in: {opacity:0, duration:.35, stagger: {each: .02}}) ×4 0%;10%;20%;30%
  p#xl(cx: "136;249;362;476"; top: 648px; font-size: 21px; font-family: n; color: $ink2; delay: 260; in: {opacity:0, duration:.35, stagger: {each: .02}}) ×4 2023;2024;2025;2026
  shape#ref(left: 90px; top: 331px; width: 513px; height: 2px; path: line_h; border: 2px solid #4FC3F7D9; dash: 6,5; delay: 410; in: {x:-20, opacity:0, duration:.4})
  p#reflbl(left: 96px; top: 304px; font-size: 16px; color: $sky; background: $board; padding: 0px 8px 0px 0px; delay: 410; in: {x:-20, opacity:0, duration:.4}) 4人に1人（25%）
  # 折れ線は 1 枚の svg を 1.5 秒で左から (hf の linebox の幅 92 → 880・ease none)・点と値は線が着く時刻に (目盛りの文字の下に敷く)
  svg#line(left: 29px; top: 231px; width: 587px; height: 453px; part: trend; delay: 510; in: wipe {dir: 'right', duration: 1.5, ease: 'none'})
  div#pt(z-index: front; left: "126;239;352;466"; top: "452;407;374;340"; width: 20px; height: 20px; border-radius: 99px; background: $amber; border: 4px solid $board; box-shadow: 0px 0px 0px 1.3px $amber; delay: "590;913;1237;1560"; in: {scale:0, duration:.25, ease:'back.out(2.5)'}) ×4
  p#pv(cx: "136;249;362;476"; top: "411;367;333;285"; font-size: "29;29;29;40"; font-family: n; delay: "640;963;1287;1610"; in: {y:11, opacity:0, duration:.25}) ×4 14.1%;17.8%;20.6%;23.4%
  shape#g141(z-index: front; left: 136px; top: 462px; width: 380px; height: 2px; path: line_h; border: 2px solid #C3CCDD73; dash: 5,4; in: {scaleX:0, duration:.4, ease:'power2.out', pivot:'left'})
  svg#brk(left: 510px; top: 350px; width: 20px; height: 112px; part: brk; in: {scaleY:0, duration:.35, ease:'power3.out', pivot:'bottom'})
  p#brkl(left: 538px; top: 391px; font-size: 17px; color: $bg; background: $amber; border-radius: 5px; padding: 4px 8px 3px 8px; white-space: nowrap; in: {x:-13, opacity:0, duration:.3}) +9.3pt

# kinds — 03 副業の種類: アイコンつきの 6 行が 90 ms ずつ入り棒が伸びる →「ウェブライター」で 1 行目の地が琥珀に灯り「1位」の札と値が弾む
section#kinds(stagger: {each:0})
chap#c3(no: "03"; delay: 60)
board#b4(k: "03"; t: "副業の種類"; n: "している {nb}234{/}人・複数回答")
  div#k4(left: 29px; top: "100;193;287;380;473;567"; width: 587px; height: 79px; border-radius: 12px; delay: 310; in: {x:-27, opacity:0, duration:.35, ease:'power3.out', stagger: {each: .09}}) ×6
    div#ic(left: 4px; cy: 50%; width: 59px; height: 59px; border-radius: 15px; background: #FFFFFF0D)
      img#img(cx: 50%; cy: 50%; width: 47px; height: 47px; fit: contain; main: none) [transparent]フラットな app icon 風の 1 つのアイコン、丸みのある幾何学の形、琥珀と白の塗りに紺の輪郭、中央に余白: 開いたノートパソコンと大きな万年筆のペン先と文書のページ;[transparent]フラットな app icon 風の 1 つのアイコン、丸みのある幾何学の形、琥珀と白の塗りに紺の輪郭、中央に余白: 値札の下がった段ボールの配送箱;[transparent]フラットな app icon 風の 1 つのアイコン、丸みのある幾何学の形、琥珀と白の塗りに紺の輪郭、中央に余白: 再生ボタンとタイムラインの帯とペンツールのある動画編集の窓;[transparent]フラットな app icon 風の 1 つのアイコン、丸みのある幾何学の形、琥珀と白の塗りに紺の輪郭、中央に余白: 四角い保温の配達バッグを積んだ配達の自転車;[transparent]フラットな app icon 風の 1 つのアイコン、丸みのある幾何学の形、琥珀と白の塗りに紺の輪郭、中央に余白: 人物のビデオ通話と吹き出しが映るノートパソコン;[transparent]フラットな app icon 風の 1 つのアイコン、丸みのある幾何学の形、琥珀と白の塗りに紺の輪郭、中央に余白: 山括弧とスラッシュの記号が並ぶコードエディタの窓
    p#lb(left: 79px; cy: 50%; font-size: 21px; line-height: 1.25) Webライター・[br]ブログ;せどり・物販;デザイン・[br]動画編集;配達・軽作業;オンライン[br]講師・相談;プログラミング
    div#b(left: 288px; cy: 50%; width: "168;135;116;97;77;64"; height: 31px; border-radius: 0,7,7,0; background: "$amber;$bar;$bar;$bar;$bar;$bar"; delay: 100; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(left: .b.right+11; cy: 50%; font-size: 31px; font-family: n; white-space: nowrap; delay: 450; in: {opacity:0, duration:.3}) 26%{sm}61人{/};21%{sm}49人{/};18%{sm}42人{/};15%{sm}35人{/};12%{sm}28人{/};10%{sm}23人{/}
  p#badge4(left: 25px; top: 92px; font-size: 16px; color: $bg; background: $amber; border-radius: 99px; padding: 4px 9px 3px 9px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2.5)'}) 1位
  p#note4(left: 29px; top: 691px; font-size: 15px; font-family: r; color: $muted; delay: 1060; in: {opacity:0, duration:.3}) ※複数回答のため、合計は100%になりません

# income — 04 月の副業収入: 地の線と 6 本の縦棒が 80 ms ずつ伸びる →「6割」で左 2 本が琥珀に灯り括弧と札 →「中央値」で破線と札・上の大きな「約 2 万円」
section#income(stagger: {each:0})
chap#c4(no: "04"; delay: 60)
board#b5(k: "04"; t: "月の副業収入"; n: "している {nb}234{/}人")
  p#hr5_pre(left: 29px; top: 162px; font-size: 27px; color: $ink2; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) 中央値は
  p#hr5_yaku(left: 151px; top: 158px; font-size: 29px; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) 約
  p#hr5_big(left: 192px; top: 112px; font-size: 100px; font-family: n; color: $amber; line-height: 1; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) 2
  p#hr5_man(left: 253px; top: 158px; font-size: 29px; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) 万円
  div#base5(left: 29px; top: 568px; width: 587px; height: 2px; background: #C3CCDD99; delay: 260; in: {scaleX:0, duration:.4, ease:'power2.out'})
  div#col(left: "29;131;234;336;439;541"; top: "301;319;422;456;499;551"; width: 75px; height: "267;249;146;112;69;17"; border-radius: 7,7,0,0; background: $bar; delay: 360; in: {scaleY:0, duration:.55, ease:'power3.out', pivot:'bottom', stagger: {each: .08}}) ×6
  p#cv(cx: "66;168;271;373;476;578"; top: "248;266;369;403;446;498"; font-size: 29px; font-family: n; line-height: 1; delay: 710; in: {y:9, opacity:0, duration:.3, stagger: {each: .08}}) ×6 31%;29%;17%;13%;8%;2%
  p#cp(cx: "66;168;271;373;476;578"; top: "281;299;402;436;479;531"; font-size: 15px; font-family: r; color: $muted; line-height: 1; delay: 710; in: {y:9, opacity:0, duration:.3, stagger: {each: .08}}) ×6 73人;68人;40人;30人;19人;4人
  p#cx(cx: "66;168;271;373;476;578"; top: 577px; font-size: 17px; color: $ink2; line-height: 1.2; text-align: center; delay: 360; in: {opacity:0, duration:.3, stagger: {each: .08}}) ×6 1万円[br]未満;1〜3[br]万円;3〜5[br]万円;5〜10[br]万円;10〜30[br]万円;30万円[br]以上
  svg#brk5(left: 29px; top: 218px; width: 177px; height: 17px; part: brk5; in: {scaleX:0, duration:.35, ease:'power3.out'})
  p#brk5l(left: 222px; top: 210px; font-size: 19px; color: $bg; background: $amber; border-radius: 7px; padding: 5px 11px 5px 11px; white-space: nowrap; in: {y:11, opacity:0, duration:.3, ease:'back.out(2)'}) 月3万円未満 6割（141人）
  svg#med(left: 166px; top: 318px; width: 4px; height: 249px; part: vdash; in: {scaleY:0, duration:.35, ease:'power2.out', pivot:'bottom'})
  p#medl(left: 149px; top: 629px; font-size: 17px; background: $bline; border-radius: 7px; padding: 5px 9px 4px 9px; white-space: nowrap; in: {y:9, opacity:0, duration:.3}) ▲ 中央値 約2万円
  p#note5(left: 29px; top: 691px; font-size: 15px; font-family: r; color: $muted; delay: 1060; in: {opacity:0, duration:.3}) ※割合は「している」234人に占める比率
  # 「6割」で左 2 本が琥珀に灯る: 角の丸い棒は絵として描かれ fill の状態を受けないので、琥珀の棒の写しを上に重ねて 0.3 秒で出す (hf の背景色の 0.3 秒の tween)
  div#colhi(left: "29;131"; top: "301;319"; width: 75px; height: "267;249"; border-radius: 7,7,0,0; background: $amber; overlap: b5.col; in: {opacity:0, duration:.3, ease:'none'}) ×2

# hours — 05 かける時間: 「分かれ目は、時間。」→ 4 色の帯が左から塗られ札が続く →「週20時間」で他の帯を沈めて 8% が弾む →「63%」で琥珀の枠・数え上げ・メーター
section#hours(stagger: {each:0})
chap#c5(no: "05"; delay: 60)
board#b6(k: "05"; t: "副業にかける時間（週）"; n: "している {nb}234{/}人")
  p#kick6(left: 29px; top: 105px; font-size: 43px; line-height: 1.2; delay: 260; in: {y:20, opacity:0, duration:.4, ease:'power3.out'}) 分かれ目は、{a}時間{/}。
  # 帯 (hf の clip-path の 0.8 秒の塗りを、帯ごとの wipe の遅れに割った)
  div#sg(left: "29;252;445;570"; top: 184px; width: "220;191;122;46"; height: 64px; border-radius: "9,0,0,9;0;0;0,9,9,0"; background: "$seg1;$seg2;$seg3;$amber"; delay: "560;860;1130;1300"; in: "wipe,right,300,ease=none;wipe,right,270,ease=none;wipe,right,170,ease=none;wipe,right,60,ease=none") ×4
  p#sgt(left: "29;252;445;570"; cy: 216px; width: "220;191;122;46"; font-size: 25px; font-family: n; color: "$ink;$ink;$bg;$bg"; text-align: center; overlap: b6.sg; delay: "560;860;1130;1300"; in: "wipe,right,300,ease=none;wipe,right,270,ease=none;wipe,right,170,ease=none;wipe,right,60,ease=none") ×4 38%;33%;21%;8%
  p#sl(left: "29;252;445;446"; top: 256px; width: "200;180;120;170"; font-size: 15px; color: $ink2; line-height: 1.35; text-align: "left;left;left;right"; delay: 860; in: {y:8, opacity:0, duration:.3, stagger: {each: .12}}) ×4 5時間未満[br]{sm}89人{/};5〜10時間[br]{sm}77人{/};10〜20時間[br]{sm}49人{/};20時間以上[br]{sm}19人{/}
  # 琥珀の枠: 題 → 数える 63 + % + 2 行の文 → メーター (63%) → 人数
  div#call(left: 29px; top: 345px; width: 587px; height: 244px; background: #FFB21A14; border: 1.3px solid #FFB21A99; border-radius: 16px; in: {y:33, opacity:0, duration:.4, ease:'power3.out'})
    p#l(left: 21px; top: 17px; font-size: 20px; color: $ink2) 週20時間以上の人（19人）のうち
    p#big(left: 21px; top: 48px; font-size: 113px; font-family: n; color: $amber; line-height: 1) [count:63 start=0 ms=850]
    p#pc(left: 144px; top: 104px; font-size: 48px; font-family: n; color: $amber; line-height: 1) %
    p#t(left: 184px; top: 69px; font-size: 31px; line-height: 1.25) が月5万円以上[br]を得ている
    div#meter(left: 21px; top: 178px; width: 545px; height: 15px; border-radius: 7px; background: #FFFFFF14)
    div#fill(left: 21px; top: 178px; width: 343px; height: 15px; border-radius: 7px; background: $amber; in: {scaleX:0, duration:.85, ease:'power2.out', pivot:'left'})
    p#foot(left: 21px; top: 205px; font-size: 16px; font-family: r; color: $muted) 12人 ／ 19人

# impact — 06 本業への影響: 3 色の帯と凡例 → 睡眠不足の札 (絵つき) →「11%」「47%」で時間別の 2 本の棒が伸びる
section#impact(stagger: {each:0})
chap#c6(no: "06"; delay: 60)
board#b7(k: "06"; t: "本業への影響（自己評価）"; n: "している {nb}234{/}人")
  div#sb(left: "29;230;495"; top: 101px; width: "198;262;122"; height: 64px; border-radius: "9,0,0,9;0;0,9,9,0"; background: "$teal;$gray6;$coral"; delay: "410;710;1100"; in: "wipe,right,300,ease=none;wipe,right,390,ease=none;wipe,right,180,ease=none") ×3
  p#sbt(left: "29;230;495"; cy: 133px; width: "198;262;122"; font-size: 25px; font-family: n; color: "$bg;$ink;$bg"; text-align: center; overlap: b7.sb; delay: "410;710;1100"; in: "wipe,right,300,ease=none;wipe,right,390,ease=none;wipe,right,180,ease=none") ×3 34%;45%;21%
  div#il(left: "29;187;349"; top: 178px; width: 150px; height: 26px; delay: 610; in: {y:7, opacity:0, duration:.3, stagger: {each: .1}}) ×3
    div#sq(left: 0px; cy: 50%; width: 17px; height: 17px; border-radius: 5px; background: "$teal;$gray6;$coral")
    p#t(left: 26px; cy: 50%; font-size: 17px; color: $ink2; white-space: nowrap) 良い影響 {sm}80人{/};影響なし {sm}105人{/};悪い影響 {sm}49人{/}
  div#sleep(left: 29px; top: 226px; width: 587px; height: 147px; background: #FF6B6B14; border: 1.3px solid #FF6B6B73; border-radius: 15px; delay: 1160; in: {y:27, opacity:0, duration:.45, ease:'power3.out'})
    img#img(left: 15px; cy: 50%; width: 100px; height: 100px; border-radius: 12px; main: none) 夜中の2時、暗い部屋で机に突っ伏しそうな疲れた日本人の会社員、半分閉じた目で頬杖をつき、光るノートパソコン、背後の壁に丸い時計、空のコーヒーカップ。正方形の構図で人物を中央に大きく
    p#a(left: 132px; top: 16px; font-size: 17px; color: $ink2) 「悪い影響」49人の中身
    p#b(left: 132px; top: 50px; font-size: 31px; white-space: nowrap) 最多は睡眠不足{big}57%{/}
    p#c(left: 132px; top: 112px; font-size: 15px; font-family: r; color: $muted) 28人 ／ 49人
  p#cmp_h(left: 29px; top: 402px; font-size: 20px; color: $ink2; in: {opacity:0, duration:.3}) かける時間別：{c}悪い影響{/}と答えた割合
  # 時間別の 2 本 (地の溝 + 珊瑚の棒 + 値)
  div#cr1(left: 29px; top: 451px; width: 587px; height: 61px; in: {x:-20, opacity:0, duration:.3})
    p#k(left: 0px; cy: 50%; font-size: 20px; line-height: 1.2) 週5時間未満[br]{sm}89人{/}
    div#tk(left: 140px; top: 0px; width: 447px; height: 61px; border-radius: 8px; background: #FFFFFF0D)
    div#f(left: 140px; top: 0px; width: 49px; height: 61px; border-radius: 8px; background: $coral; in: {scaleX:0, duration:.45, ease:'power3.out', pivot:'left'})
    p#v(left: 201px; cy: 50%; font-size: 43px; font-family: n; white-space: nowrap; in: {opacity:0, duration:.25}) 11%{sm}10人{/}
  div#cr2(left: 29px; top: 528px; width: 587px; height: 61px; in: {x:-20, opacity:0, duration:.3})
    p#k(left: 0px; cy: 50%; font-size: 20px; line-height: 1.2) 週20時間以上[br]{sm}19人{/}
    div#tk(left: 140px; top: 0px; width: 447px; height: 61px; border-radius: 8px; background: #FFFFFF0D)
    div#f(left: 140px; top: 0px; width: 210px; height: 61px; border-radius: 8px; background: $coral; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(left: 362px; cy: 50%; font-size: 56px; font-family: n; color: $coral; white-space: nowrap; in: {scale:.6, opacity:0, duration:.35, ease:'back.out(2)'}) 47%{sm}9人{/}

# reasons — 07 始めない理由: 5 行が入り棒が伸びる →「時間がない」で 1 行目が琥珀に灯り「1位」→「規則が」で 3 行目が空色に →「61%」でドーナツの弧と数え上げ
section#reasons(stagger: {each:0})
chap#c7(no: "07"; delay: 60)
board#b8(k: "07"; t: "始めたいが、していない理由"; n: "{nb}385{/}人・複数回答")
  div#r7(left: 29px; top: "94;178;262;346;430"; width: 587px; height: 79px; border-radius: 11px; delay: 310; in: {x:-27, opacity:0, duration:.35, ease:'power3.out', stagger: {each: .09}}) ×5
    p#rk(left: 11px; top: 9px; width: 20px; font-size: 17px; font-family: n; color: $muted) 1;2;3;4;5
    p#lb(left: 39px; top: 7px; font-size: 20px; white-space: nowrap) 時間がない;何をすればいいか分からない;会社の規則で禁止・よく分からない;確定申告が面倒;会社に知られたくない
    div#b(left: 11px; top: 47px; width: "347;273;220;160;127"; height: 23px; border-radius: 0,6,6,0; background: $bar; delay: 100; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(left: .b.right+11; cy: 58px; font-size: 27px; font-family: n; white-space: nowrap; delay: 450; in: {opacity:0, duration:.3}) 52%{sm}200人{/};41%{sm}158人{/};33%{sm}127人{/};24%{sm}92人{/};19%{sm}73人{/}
  p#badge7(left: 173px; top: 101px; font-size: 16px; color: $bg; background: $amber; border-radius: 99px; padding: 4px 9px 3px 9px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2.5)'}) 1位
  # 空色の枠: 地の輪 + 61% の弧 (draw) + 中央の数え上げ + 右の文
  div#dn(left: 29px; top: 526px; width: 587px; height: 171px; background: #4FC3F714; border: 1.3px solid #4FC3F78C; border-radius: 15px; in: {y:33, opacity:0, duration:.4, ease:'power3.out'})
    shape#ring.ellipse(left: 22px; top: 18px; width: 134px; height: 134px; background: none; border: 20px solid #FFFFFF1A)
    shape#arc(path: "M 89 28.2 C 114.3 28.2 136.6 44.7 143.9 68.9 C 151.2 93.1 141.8 119.2 120.7 133.2 C 99.7 147.2 71.9 145.8 52.5 129.7"; background: none; border: 20px solid $sky; in: draw {duration: 0.9, ease: 'power2.out'})
    p#num(cx: 89px; top: 58px; font-size: 44px; font-family: n; line-height: 1) [count:61 start=0 ms=900]%
    p#den(cx: 89px; top: 108px; font-size: 13px; font-family: r; color: $muted) 77／127人
    p#a(left: 179px; top: 16px; font-size: 18px; color: $ink2; white-space: nowrap) 「会社の規則」を理由に挙げた127人のうち
    p#b(left: 179px; top: 46px; font-size: 29px; line-height: 1.3) {h}61%{/}は就業規則を[br]読んだことがない
    p#c2(left: 179px; top: 130px; font-size: 15px; font-family: r; color: $muted; white-space: nowrap) ※規則で「禁止」または「よく分からない」と回答
  # 「時間がない」で 1 行目の棒が琥珀・「規則が」で 3 行目の棒が空色に灯る: 角の丸い棒は絵として描かれ fill の状態を受けないので、色の棒の写しを上に重ねて 0.3 秒で出す
  div#hot(left: 40px; top: 141px; width: 347px; height: 23px; border-radius: 0,6,6,0; background: $amber; overlap: b8.r7; in: {opacity:0, duration:.3, ease:'none'})
  div#rul(left: 40px; top: 309px; width: 220px; height: 23px; border-radius: 0,6,6,0; background: $sky; overlap: b8.r7; in: {opacity:0, duration:.3, ease:'none'})

# summary — まとめ: 右上は「まとめ」の札・題の札と番号つきの 3 枚を載せた見えない容器が板と同じく右から入る (中は 3 枚が 200 ms ずつ・番号が弾む) →「就業規則」で規則の本の絵の枠 (絵が引き、文が 100 ms ずつ)
section#summary(stagger: {each:0})
p#c8(right: 37px; top: 37px; font-size: 20px; color: $amber; delay: 60; in: {y:16, opacity:0, duration:.3, ease:'power3.out'}) まとめ
div#s8(left: 37px; top: 124px; width: 645px; height: 740px; in: {x:733, duration:.5, ease:'power3.inOut'})
  p#chip(left: 0px; cy: 24px; font-size: 20px; color: $bg; background: $amber; border-radius: 5px; padding: 7px 11px 6px 11px; line-height: 1; delay: 110; in: {y:20, opacity:0, duration:.4, ease:'power3.out'}) まとめ
  p#t(left: 93px; cy: 24px; font-size: 32px; white-space: nowrap; delay: 110; in: {y:20, opacity:0, duration:.4, ease:'power3.out'}) 数字で見る、会社員の副業
  div#tk(left: 0px; top: "63;176;289"; width: 645px; height: 100px; background: $board; border: 1.3px solid $bline; border-radius: 15px; delay: 260; in: {x:53, opacity:0, duration:.42, ease:'power3.out', stagger: {each: .2}}) ×3
    div#no(left: 20px; cy: 50%; width: 51px; height: 51px; border-radius: 99px; background: $amber; delay: 100; in: {scale:0, duration:.35, ease:'back.out(2.5)'})
      p#t(cx: 50%; cy: 50%; font-size: 29px; font-family: n; color: $bg; line-height: 1) 1;2;3
    p#a(left: 88px; top: 20px; font-size: 25px; white-space: nowrap) 3年で {na}14.1%{/} → {na}23.4%{/};稼ぎは小さく、{na}6{/}割が月3万円未満;分かれ目は「時間」
    p#b(left: 88px; top: 62px; font-size: 17px; font-family: r; color: $ink2; white-space: nowrap) 副業をする会社員は、4人に1人に近づく;月の副業収入の中央値は約2万円;週20時間以上では47%が本業に悪影響
  div#cta(left: 0px; top: 410px; width: 645px; height: 280px; background: $cta; border: 1.3px solid #FFB21A99; border-radius: 17px; in: {y:40, scale:.96, opacity:0, duration:.5, ease:'power3.out'})
    img#img(left: 0px; top: 0px; width: 280px; height: 280px; main: kb {scale: [1.15, 1], ease:'power1.out'}) 机の上で両手が分厚い会社の就業規則のバインダーを開いている。色つきのインデックスのタブ、開いたページに置かれた虫眼鏡、暖かい琥珀色のデスクライトの光、暗い紺の背景。正方形の構図でバインダーを中央に大きく
    div#fade(left: 167px; top: 0px; width: 113px; height: 280px; z-index: front; background: linear(#0E183000,$cta,90))
    p#a(left: 287px; top: 50px; font-size: 21px; color: $ink2; in: {x:20, opacity:0, duration:.35}) 始めるなら、まずは
    p#b(left: 287px; top: 84px; font-size: 51px; color: $amber; line-height: 1.18; white-space: nowrap; in: {x:20, opacity:0, duration:.35}) 就業規則を
    p#c(left: 287px; top: 145px; font-size: 39px; line-height: 1.18; white-space: nowrap; in: {x:20, opacity:0, duration:.35}) 読むところから
    p#d(left: 287px; top: 201px; font-size: 15px; font-family: r; color: $muted; line-height: 1.4; in: {x:20, opacity:0, duration:.35}) 規則を理由に挙げた人の61%は[br]就業規則を読んだことがない
```

```timeline.txt
#v2
cast n = "明瞭で端正な30〜40代の男性のナレーター、やや高めのピッチと歯切れの良い発音で、淀みのない一定のテンポで調査の数字を伝える" speed=117%
silence head=0 tail=0
read 23.4% = にじゅうさんてんよんパーセント
read 38.5% = さんじゅうはってんごパーセント
# 切替: 旧い板が左へ抜け新しい板が右から入る (板ごとの in / out・0.5 秒)。縁が 2 枚の板の隙間を同じ速さで走る wipe で継ぐので、地と常設の枠は動かない
# 窓は境界の前の 0.5 秒 (overlap なし = 旧い板の out と新しい板の in が同じ 0.5 秒に重なる)・前の声の末尾の 0.2 秒 + 次の頭の 0.06 秒 (字幕は声の 60 ms 前に出る) が声と声の間
transition = wipe,500,dir=left,ease=power3.inOut,se=whoosh -1dB

# hook — 頭に題が組み上がり、「4人に1人」で結論の札と人の形 (1 つ目が弾む)・字幕は下に寄せた札
*** hook
[>#subtitle]
bgm music
se telop -5dB to=4.4s
@n: [silence:0.5s][card:low]副業をする会社員が、[|][card:low][>#head -120][♪pop -5dB -100][>#head.ppl[*] +100][!#head.ppl[1] punch,1.18,duration=320 +550]{a}4人に1人{/}に近づいています。[silence:0.2s]

# status — 頭で 1,000 点の地 →「23.4%」で琥珀の点・札・数え上げ →「始めたいけど」で砂色 →「38.5%」で空色・灰 (字幕は hf の札の文言で上書き)
*** status
subtitle "いま副業をしている人は{a}23.4%{/}"
@n: [silence:60][♪count -1dB +410 to=2s]いま副業をしている人は、[>#b2.waf_c1 -150][>#b2.st1 -300][♪hit -2dB -120][>#b2.lg[1] +200][!#b2.st1 punch,1.03,duration=320 +550]{a}23.4%{/}。
subtitle "始めたいけど、していない人も{a}38.5%{/}"
@| [>#b2.waf_c2 -500][>#b2.lg[2] -350]始めたいけど、していない人も、[>#b2.waf_c3 -200][>#b2.st2 -300][♪pop -6dB -150][>#b2.lg[3] +200][!#b2.st2 punch,1.03,duration=320 +550][>#b2.waf_c4 +700][>#b2.lg[4] +900]{a}38.5%{/}います。[silence:0.2s]

# trend — 頭で目盛り・25% の破線・折れ線と点 →「14.1%」で最初の点が弾む →「9.3ポイント」で差の破線・括弧・札・上の数字
*** trend
@n: [silence:60]3年前の[!#b3.pt[1] punch,1.5,duration=320][!#b3.pv[1] punch,1.2,duration=320]{a}14.1%{/}から、[|][>#b3.g141 -450][>#b3.brk -250][>#b3.brkl -50][>#b3.hr3_pre -150][>#b3.hr3_big -90][>#b3.hr3_post -30][>#b3.hr3_side +100][♪hit -2dB -180]{a}9.3ポイント{/}の増加です。[silence:0.2s]

# kinds — 頭で 6 行と棒 →「ウェブライター」で 1 行目の地が灯り「1位」・値が弾む
*** kinds
@n: [silence:60]中身の1位は、[|][!#b4.k4[1] fill,#FFB21A1A,duration=300 -100][>#b4.badge4][♪hit -3dB -20][!#b4.k4[1].v punch,1.15,duration=320 +200]{Webライター|ウェブライター}・ブログで{a}26%{/}。[silence:0.2s]

# income — 頭で 6 本の縦棒 →「6割」で左 2 本が琥珀・括弧と札 →「中央値」で破線・札・上の「約 2 万円」
*** income
@n: [silence:60]ただ、[>#b5.colhi[1] -100][>#b5.colhi[2] -100][>#b5.brk5][>#b5.brk5l +150][♪pop -6dB -20]{a}6割{/}はひと月{a}3万円未満{/}。[|][>#b5.med -100][>#b5.medl +100][>#b5.hr5_pre][>#b5.hr5_yaku +50][>#b5.hr5_big +100][>#b5.hr5_man +150][♪hit -3dB -20]中央値は{a}約2万円{/}です。[silence:0.2s]

# hours — 頭で題と帯 →「週20時間」で他の帯と札を沈め 8% が弾む →「63%」で琥珀の枠・数え上げ・メーター (hf の 1 文を「一方、」で 2 つの cut に割る)
*** hours
@n: [silence:60]分かれ目は時間。[|][!#b6.sg[1] to,{opacity:.5, duration:.3} -50][!#b6.sg[2] to,{opacity:.5, duration:.3} -50][!#b6.sg[3] to,{opacity:.5, duration:.3} -50][!#b6.sl[1] to,{opacity:.6, duration:.3} -50][!#b6.sl[2] to,{opacity:.6, duration:.3} -50][!#b6.sl[3] to,{opacity:.6, duration:.3} -50][!#b6.sg[4] punch,1.12,duration=320][♪tick -2dB -20]週20時間以上だと、[>#b6.call -500][>#b6.call.fill -450][♪hit -2dB -120]{a}63%{/}が[br]ひと月{a}5万円以上{/}を稼ぐ一方、[silence:0.2s]

# impact — 頭で 3 色の帯・凡例・睡眠不足の札 →「11%」「47%」で時間別の棒
*** impact
@n: [silence:60]本業への悪い影響も、[br]週5時間未満の[>#b7.cmp_h -600][>#b7.cr1 -350][>#b7.cr1.f -150][>#b7.cr1.v +100][♪tick -3dB -120]{a}11%{/}に対し、[|][>#b7.cr2 -450][>#b7.cr2.f -200][>#b7.cr2.v +150][♪hit -1dB -120]{a}47%{/}です。[silence:0.2s]

# reasons — 頭で 5 行 →「時間がない」で 1 行目が琥珀・「1位」→「規則が」で 3 行目が空色 →「61%」でドーナツ →「就業規則」で 61% が弾む
*** reasons
@n: [silence:60]始めない理由の1位も「[!#b8.r7[1] fill,#FFB21A1A,duration=300 -100][>#b8.hot -100][>#b8.badge7][♪hit -3dB -50]時間がない」。[!#b8.r7[3] fill,#4FC3F71F,duration=300 -100][>#b8.rul -100][♪pop -6dB -20]規則が理由の人の[>#b8.dn -550][>#b8.dn.arc -500][♪hit -3dB -150]{a}61%{/}は、[|][!#b8.dn.b{h} punch,1.12,duration=320]就業規則を読んだことがありません。[silence:0.2s]
transition wipe,500,dir=left,ease=power3.inOut,se=whoosh_big -3dB

# summary — 頭で題と 3 枚の札 (ティック 3 回) →「就業規則」で絵の枠と文 → 2 秒止めて終わる
*** summary
se tick -5dB +260
se tick -5dB +460
se tick -5dB +660
@n: [silence:60]まずは、[>#s8.cta -320][>#s8.cta.a -150][>#s8.cta.b -50][>#s8.cta.c +50][>#s8.cta.d +150][♪telop -6dB -300 to=3.8s][!#s8.cta.b punch,1.06,duration=320 +900]就業規則を読むところから。[silence:2.0s]
```

# data · churn-report (hf 全力版の全量の写し — 動画生成サービスの解約、この3か月で分かったこと・暗い紺の地に板と図を場面ごとに組む 10 場面のデータ図解) — canvas 1920x1080

見せる作り: 全編の地 (紺の写真 + 周辺減光 + grain) と 2 場面目から常設の上端の帯 (題・期間・場面の境の目盛り・全編で伸びる進行・場面ごとに入れ替わる章札)・場面 = 見出しの帯 + 板 1〜2 枚 (板の def)・数字の語で伸びる図 (人数の棒・薄く置いて語で点ける流れ図と流れ続ける点・2 段に割れる縦棒・左から描く折れ線と面・期間別の横棒とかぎ・25% → 53% の帯と台形・上位 3 つを塗り替える横棒・100 マスが 3 群に分かれる)・話し終えた板を 0.8 に沈める・まとめの 3 枚の札を文の頭で点ける・題の絵で始まり題の絵で締めて暗転・字幕は黒い半透明の札で数字だけ黄の欧文・音の層 (場面の境の風切り + 語に結んだ効果音 59)

```design.txt
#v2
# 学ぶ作り: 暗い data の design system を根に 1 回 (palette・書体 3・数字の run・見出しの帯・板 panel の def・章札 chap の def) → 場面は板の中身だけ
# 常設の層: 全編の地 (紺の写真 + 周辺減光 + grain)・2 場面目から sticky の上端の帯 (題・期間・目盛り 8 本の線と全編で伸びる進行) と場面ごとに入れ替わる章札
# 場面 = 見出しの帯 + 板 1〜2 枚。板の中の図 (縦棒・折れ線・横棒・帯・流れ図・100 マス) は数字の語と同時に伸び、話し終えた板は 0.8 に沈めて次の板へ目を移す
# hf churn churn-report (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の退場は section の out (上へ抜けて消える)・切替は書かない (地は常設なので素の切替)
canvas 1920x1080 bg=#05080F
theme dark
palette ink=#EEF2FA ink2=#AAB5C9 ink3=#8793AB note=#AEB8CC line=#AABEE621 line2=#AABEE642 coral=#FF6B6B amber=#F4B942 teal=#35D3B5 blue=#5B9DFF slate=#34405C slate2=#4E5B78 cap=#FFD27A
font "太い角ゴシック体、すっきりした現代的な印象"
fonts n="極太の幾何学的な欧文サンセリフ体、ウェブやUIで定番のモダンな書体"
fonts m="標準の太さの角ゴシック体、すっきりした現代的な印象"
fonts h="極太の角ゴシック体、すっきりした現代的な印象"
sfx off
# hf の作り: 場面の見出しは台詞より先に結論を出す (見出し → 図 → 台詞が数字を読む)
lint off=spoiler
# hf の作り: 見出しの帯は数字ごと場面の頭に全文を出す (月次の解約率は 13.2% から 10.8% へ)
lint off=all_at_once
# hf の作り: 板の中の目盛り・凡例・注記・補足は 13〜16 px (1080 の 20〜24 px)
lint off=small_text
# hf の作り: 図の色 (グラデの端・半透明の地・薄い線) は場面ごとに直書き
lint off=palette_drift
# hf の作り: 地は全編 1 枚の紺の写真 (場面は板と図で替える)
lint off=same_picture
# hf の作り: まとめの 2・3 枚目の札は 0.36 の薄い枠で先に置き、文の頭で点ける
lint off=empty_board
# hf の作り: 締めの注記は暗転の 2 秒前に出る
lint off=flash_text
run a { color: $amber }
run b { color: $cap; font-family: n }
run nn { font-family: n }
run an { color: $amber; font-family: n }
run lb { color: $ink3 }
run u { color: $ink3; font-size: 0.45em }
run un { color: $ink3; font-size: 0.41em }
run cr { color: $coral }
run ar { color: $coral; font-size: 0.76em }
run dai { font-size: 0.37em }
sound air = "空気が長く流れる柔らかい風切りの音、2 秒ほどで消える"
sound swoosh = "中低域の丸みのある短い電子のスウィッシュ、場面の切り替わり"
sound sub = "低域が響く 1 秒ほどの重いシネマティックなサブベースの一打"
sound deep = "滑らかで深みのあるシネマティックな一打のスウッシュ、重みのある強調"
sound pop = "木を軽く叩いたような乾いた丸い短いポップ音"
sound chime = "丸みと透明感のあるクリーンなシンセのベル、1 秒ほど"
sound tick = "中高音のごく短い、丸くウッディな上品な UI の音"
sound blip = "中高音のごく短い、丸みのあるクリアなシンセの UI 音"
sound click = "中低域のごく短く乾いたクリック音"
image plate = "[photo]ほぼ黒に近い深い紺の無地の背景。左上から青い光がやわらかくにじみ、右下に青緑のぼけた光の玉がいくつか浮かぶ。全面にごく細かい点の格子がうっすら見える。中央は暗く空いている。抽象的なデータ解説の背景、文字なし" aspect=16:9
image title_img = "[photo]暗い紺の空間に、青と青緑の光の粒子が画面右半分を横切る帯のように流れ集まり、右上の端で珊瑚色の粒子が火花のように散る抽象的なデータの風景。左半分は暗く空けて文字の場所にする。被写界深度の浅いぼけ、文字なし" aspect=16:9
# 機能への不満の icon (吹き出し + 声の波形)・初回の不満の icon (魔法の杖)・音声の icon (締めの札用の小さい版)
svg voice_ico = """<svg viewBox="0 0 84 84"><rect x="1" y="1" width="82" height="82" rx="20" fill="#F4B942" fill-opacity="0.12" stroke="#F4B942" stroke-opacity="0.6" stroke-width="2"/><path d="M16 22 H68 A6 6 0 0 1 74 28 V52 A6 6 0 0 1 68 58 H36 L26 67 V58 H16 A6 6 0 0 1 10 52 V28 A6 6 0 0 1 16 22 Z" fill="none" stroke="#F4B942" stroke-width="3.5" stroke-linejoin="round"/><path d="M26 40 V40 M33 34 V46 M40 30 V50 M47 35 V45 M54 32 V48 M61 38 V42" stroke="#F4B942" stroke-width="3.5" stroke-linecap="round"/></svg>"""
svg wand_ico = """<svg viewBox="0 0 60 60"><rect x="1" y="1" width="58" height="58" rx="14" fill="#5B9DFF" fill-opacity="0.14" stroke="#5B9DFF" stroke-opacity="0.6" stroke-width="2"/><path d="M17 41 L35 23 M31 19 L41 29 M22 18 L24 22 M18 26 L22 24 M40 38 L43 42" fill="none" stroke="#86B8FF" stroke-width="4" stroke-linecap="round"/></svg>"""
svg bubble_ico = """<svg viewBox="0 0 60 60"><rect x="1" y="1" width="58" height="58" rx="14" fill="#F4B942" fill-opacity="0.14" stroke="#F4B942" stroke-opacity="0.6" stroke-width="2"/><path d="M13 16 H47 A4 4 0 0 1 51 20 V36 A4 4 0 0 1 47 40 H26 L19 46 V40 H13 A4 4 0 0 1 9 36 V20 A4 4 0 0 1 13 16 Z" fill="none" stroke="#F4B942" stroke-width="3" stroke-linejoin="round"/><path d="M19 28 V28 M24 24 V32 M29 21 V35 M34 25 V31 M39 23 V33 M44 27 V29" stroke="#F4B942" stroke-width="3" stroke-linecap="round"/></svg>"""
p { color: $ink }
div { border: none }
# 字幕: 下端中央の半透明の黒い札・数字は黄の欧文 (台詞の {b})・札の中の読点は空白に・cut を割らない (札 = 文、[|] で句に切る)
subtitle.hug(bottom: 50px; font-size: 38px; line-height: 1.24; letter-spacing: 0.03em; color: #F4F7FC; background: #04070F94; border-radius: 12px; padding: 8px 26px 10px 26px; box-shadow: 0px 6px 24px #00000040; unit: sentence; strip: 、。>space; lead: 50ms; tail: 0ms; hold: off; in: {y:8, opacity:0, duration:0.16, ease:'power2.out'}; out: {opacity:0, duration:0.14, ease:'power2.in'})
# 曲: 頭の 1 秒と締めの題だけ前に出し、台詞の間は 6 dB 下げる
bgm#music(keys: "0:+6|800ms:+6|1300ms:0|end-3s:0|end-2.2s:+6"; fade: 600,1550) ミニマルで知的なディープテック寄りのアンビエント・エレクトロニカ、120 BPM 前後、シンセのアルペジオと柔らかいパッド、控えめなキックとハイハットとサブベース、主旋律なし、データ分析の解説向け

# 見出しの帯 (青緑 → 青の縦棒 + 50 px の題・語の強調は黄の run a)
def headline(t) = div(left: 112px; top: 128px; width: 1696px; height: 72px; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 8px; height: 50px; border-radius: 4px; background: linear($teal,$blue,180))
  p#t(left: 30px; cy: 50%; font-size: 50px; line-height: 1.1; letter-spacing: 0.01em; white-space: nowrap; content: {t})
# 板: 紺の縦グラデ + 細い縁 + 深い影・頭の行 (色の小さな縦棒 + 題 + 補足) と下の罫
def panel(t, s="", tk=$blue) = div(border-radius: 20px; background: linear(#161F38E6,#0D1325E6,180); border: 2px solid #AABEE624; box-shadow: 0px 28px 60px #00000061; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
  div#tick(left: 30px; top: 22px; width: 6px; height: 24px; border-radius: 3px; background: {tk})
  p#pt(left: 50px; cy: 34px; font-size: 27px; letter-spacing: 0.02em; white-space: nowrap; content: {t})
  p#ps(left: .pt.right+14; cy: 34px; font-size: 20px; color: $ink3; font-family: m; white-space: nowrap; content: {s})
  div#rule(left: 0px; top: 68px; width: 100%; height: 2px; background: $line)
# 上端の帯の章札 (番号は青緑の欧文 + 題)・場面の頭に下から入り、場面の終わりに上へ抜ける
def chap(n, t) = div(left: 402px; top: 38px; width: 540px; height: 44px; z-index: front; delay: 50ms; in: {y:14, opacity:0, duration:0.45, ease:'power3.out'}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
  p#n(left: 0px; cy: 50%; font-size: 20px; font-family: n; letter-spacing: 0.04em; color: $teal; content: {n})
  p#t(left: .n.right+12; cy: 50%; font-size: 22px; white-space: nowrap; content: {t})
# 丸い札 (既定は黄の地に黒文字・色は実体で上書き)
def badge(t) = p(font-size: 24px; line-height: 1.2; color: #1A1204; background: $amber; border-radius: 148px; padding: 8px 18px; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.45, ease:'back.out(2)'}; content: {t})
# 主役の人数 (月末の題 + 大きな数字 + 人 + 人数に比例した棒)
def kpi(l, v, w, c, vc=$ink) = div(width: 640px; height: 220px; in: {y:16, opacity:0, duration:0.5, ease:'power3.out'})
  p#l(left: 0px; top: 0px; font-size: 26px; letter-spacing: 0.06em; color: $ink3; content: {l})
  p#n(left: 0px; top: 46px; font-size: 112px; line-height: 1.08; font-family: n; letter-spacing: -0.02em; color: {vc}; in: {y:26, opacity:0, duration:0.55, ease:'power3.out'}; content: {v})
  p#u(left: .n.right+9; top: 111px; font-size: 38px; color: $ink2) 人
  div#bar(left: 0px; top: 184px; width: {w}; height: 14px; border-radius: 8px; background: {c}; in: {scaleX:0, duration:1, ease:'power3.out', pivot:'left'})
# 理由の行 (題 + 右端の % + 0〜40% の地の上の棒)
def reason(l, v, w, c="linear(#4C8DF0,#8CBBFF,90)", vc=$ink) = div(width: 420px; height: 140px)
  p#lb(left: 0px; top: 0px; font-size: 28px; white-space: nowrap; in: {x:-10, opacity:0, duration:0.4, ease:'power3.out'}; content: {l})
  div#tr(left: 0px; top: 58px; width: 420px; height: 30px; border-radius: 6px; background: #AABEE614)
  div#bar(left: 0px; top: 58px; width: {w}; height: 30px; border-radius: 6px; background: {c}; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  p#vv(right: 0px; top: -12px; font-size: 54px; line-height: 1.11; font-family: n; color: {vc}; in: {y:8, opacity:0, duration:0.4, ease:'power3.out'}; content: {v})
# まとめの札 (上端の色の線 + 番号の丸 + 題 2 行 + 補足 + 中身 + 出典)
# hf の作り: 番号は色の丸の上の暗い字 (check は全編の grain の幕と比べて low_contrast を出す)・hf の上端の線は札の角丸で切れる全幅の線 (ここは角を避けて内側に)
def card(n, t, s, cap, c, g) = div(top: 236px; width: 536px; height: 620px; border-radius: 22px; background: linear(#18223EF0,#0D1325F0,180); border: 2px solid #AABEE629; box-shadow: 0px 30px 70px #00000066; in: {y:40, scale:0.97, opacity:0, duration:0.7, ease:'power3.out'})
  div#top(left: 14px; top: 0px; width: 508px; height: 6px; border-radius: 3px; background: {g})
  div#no(left: 32px; top: 34px; width: 60px; height: 60px; border-radius: 148px; background: {c})
    p#t(cx: 50%; cy: 50%; font-size: 30px; font-family: n; color: #06122A; content: {n})
  p#t(left: 32px; top: 118px; width: 480px; font-size: 38px; line-height: 1.32; font-family: h; in: {y:14, opacity:0, duration:0.5, ease:'power3.out'}; content: {t})
  p#s(z-index: front; left: 32px; top: 232px; font-size: 26px; line-height: 1.36; color: $ink2; white-space: nowrap; in: {y:10, opacity:0, duration:0.5, ease:'power3.out'}; content: {s})
  p#cap(left: 32px; top: 560px; font-size: 20px; color: $ink3; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}; content: {cap})

# 全編の地 (根): 紺の写真が 119 秒かけて 1.08 → 1.16 に寄る + 周辺減光 + grain
img#plate(inset: 0; content: @plate; opacity: 0.95; z-index: back; main: kb {scale: [1.08, 1.16], focus: ['45% 50%', '55% 50%']}; in: none)
veil#vig(background: radial(#05080F00@55%,#03050A8C@100%,50%,45%); z-index: back; in: none)
veil#grain(grain: 0.05; color: #00000000; z-index: back; in: none)

# s01 題: 粒子の光の絵が寄りながら明け、左の空きに小札 → mask から上がる 2 行 → 下線 → 3 つの注記。題の組ごとゆっくり寄って上へ抜ける
section#s01(stagger: {each:0})
img#title_bg(inset: 0; content: @title_img; main: none; in: keys(at=0 scale=1.12 opacity=0 | at=0.374 scale=1.03 opacity=1 ease=power2.out | at=1 scale=1 ease=none),duration=4280; out: {opacity:0, duration:0.6, ease:'power2.inOut'})
group#title(left: 150px; top: 330px; width: 1100px; height: 460px; main: keys(at=0 scale=1 | at=1 scale=1.025),window=0,4900,forwards; transform-origin: 0% 50%; out: {y:-18, opacity:0, duration:0.4, ease:'power2.in'})
  div#kicker(left: 0px; top: 0px; width: 900px; height: 38px; delay: 300ms; in: {x:-24, opacity:0, duration:0.6, ease:'power3.out'})
    div#ln(left: 0px; cy: 50%; width: 44px; height: 3px; background: $teal)
    p#t(left: 60px; cy: 50%; font-size: 26px; letter-spacing: 0.14em; color: $teal; white-space: nowrap) 社内共有 ｜ 解約分析レポート
  p#l1(left: 0px; top: 52px; font-size: 92px; font-family: h; line-height: 1.3; letter-spacing: 0.01em; white-space: nowrap; delay: 500ms; in: {y:124, duration:0.8, ease:'power4.out', clip:true}) 動画生成サービスの解約、
  p#l2(left: 0px; top: 170px; font-size: 92px; font-family: h; line-height: 1.3; letter-spacing: 0.01em; white-space: nowrap; delay: 660ms; in: {y:124, duration:0.8, ease:'power4.out', clip:true}) この{a}3か月{/}で分かったこと
  div#bar(left: 0px; top: 318px; width: 620px; height: 6px; border-radius: 3px; background: linear($teal,$blue,90); delay: 1050ms; in: {scaleX:0, duration:0.9, ease:'power3.inOut', pivot:'left'})
  p#meta(left: "0;230;413"; top: "356;356;356"; font-size: 26px; color: $ink2; font-family: m; white-space: nowrap; delay: 1350ms; in: {y:14, opacity:0, duration:0.5, ease:'power3.out', stagger:{each:0.12}}) ×3 {lb}対象{/} 有料契約者;{lb}期間{/} 7〜9月;{lb}データ{/} 解約・申請・アンケート

# s02 現状: 上端の帯が降りて進行が伸び始める・左の板で 1,776 → 1,682 人を棒で比べ、右の板の流れ図 (新規 → 契約者 → 解約) を薄く置いて語で点ける・点が矢印を流れ続け「純増ゼロ」が光る
section#s02(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
# 上端の帯 (sticky・締めの題で抜く): 左の題・右の期間・細い線に場面の境の目盛り 8 本
div#hdr.sticky(left: 112px; top: 38px; width: 1696px; height: 60px; z-index: front; delay: 100ms; in: {y:-12, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-10, opacity:0, duration:0.6, ease:'power2.in'})
  div#dot(left: 0px; top: 16px; width: 10px; height: 10px; border-radius: 2px; background: linear($teal,$blue,135))
  p#l(left: 24px; cy: 22px; font-size: 21px; letter-spacing: 0.12em; color: #8E9AB2; white-space: nowrap) 解約分析レポート
  p#r(right: 0px; cy: 22px; font-size: 20px; letter-spacing: 0.06em; color: $ink3; font-family: m; white-space: nowrap) 7〜9月 ｜ 社内共有
  div#track(left: 0px; top: 56px; width: 1696px; height: 3px; background: #AABEE624)
  div#tk(left: "164;360;549;704;896;1005;1263;1424"; top: 52px; width: 3px; height: 8px; background: #AABEE659) ×8
# 進行 (線の上を全編の残りで左から伸びる)
progress#prog.sticky(left: 112px; top: 93px; width: 1696px; height: 3px; background: linear($teal,$blue,90); until: end; z-index: front; overlap: hdr)
chap#ch2(n: "01"; t: "現状")
headline#hl2 新規課金があっても、契約者数は{a}増えていない{/}
panel#p2a(left: 112px; top: 232px; width: 720px; height: 648px; t: "有料契約者数"; s: "各月末時点"; delay: 80ms)
  kpi#k1(left: 44px; top: 104px; l: "6月末"; v: "1,776"; w: 600px; c: $slate2; vc: $ink2)
  div#arrow(left: 44px; top: 318px; width: 600px; height: 50px; in: {y:-10, opacity:0, duration:0.45, ease:'power3.out'})
    icon#i(left: 0px; cy: 50%; font-size: 36px; name: arrow-down; color: #6E7A92)
    p#t(left: 40px; cy: 50%; font-size: 22px; color: $ink3; font-family: m) 3か月後
  kpi#k2(left: 44px; top: 386px; l: "9月末"; v: "1,682"; w: 568px; c: "linear(#4C8DF0,#86B8FF,90)")
  p#na(left: 44px; top: 598px; font-size: 22px; color: $note; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) バーの長さ ＝ 人数（0 起点）
# 流れ図: 3 つの枠を 0.32 で先に置き、語で 1 に点ける (点は矢印の上を 0.9 秒で流れ続ける)
panel#p2b(left: 872px; top: 232px; width: 936px; height: 648px; t: "毎月の出入り"; s: "7〜9月"; tk: $amber; delay: 220ms)
  shape#a1(left: 312px; top: 260px; width: 48px; height: 21px; path: arrow_r; background: $teal; border: 4px solid $teal; in: draw {duration: 0.5})
  shape#a2(left: 572px; top: 260px; width: 66px; height: 21px; path: arrow_r; background: $coral; border: 4px solid $coral; in: draw {duration: 0.5})
  shape#fi(left: "309;311;312"; top: "266;266;266"; width: 9px; height: 9px; border-radius: 50%; background: #BFF5EA; in: {opacity:0, duration:0.3}) ×3
  shape#fo(left: "570;572;573"; top: "266;266;266"; width: 9px; height: 9px; border-radius: 50%; background: #FFD0D0; in: {opacity:0, duration:0.3}) ×3
  div#node_in(left: 30px; top: 170px; width: 276px; height: 200px; border-radius: 18px; background: #35D3B512; border: 3px solid #35D3B58C; opacity: 0.32; delay: 450ms; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'})
    p#t(left: 0px; top: 22px; width: 276px; text-align: center; font-size: 26px; color: $teal) 新規課金
    p#v(left: 0px; top: 72px; width: 276px; text-align: center; font-size: 46px; line-height: 1.39; font-family: n; in: {y:8, opacity:0, duration:0.45, ease:'power3.out'}) 170〜178
    p#u(left: 0px; top: 140px; width: 276px; text-align: center; font-size: 22px; color: $ink3; font-family: m; in: {y:8, opacity:0, duration:0.45, ease:'power3.out'}) 人／月
  div#core(left: 368px; top: 170px; width: 200px; height: 200px; border-radius: 148px; background: radial(#5B9DFF38,#5B9DFF0A@70%,50%,40%); border: 3px solid #AABEE659; opacity: 0.32; delay: 550ms; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'})
    p#t(cx: 50%; cy: 50%; font-size: 26px; white-space: nowrap) 有料契約者
  div#node_out(left: 646px; top: 118px; width: 250px; height: 304px; border-radius: 18px; background: #FF6B6B12; border: 3px solid #FF6B6B8C; opacity: 0.32; delay: 650ms; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'})
    p#t(left: 0px; top: 22px; width: 250px; text-align: center; font-size: 26px; color: $coral) 解約成立
    div#r(left: "30;30;30"; top: "78;146;215"; width: 190px; height: 64px; in: {x:16, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.12}}) ×3
      p#m(left: 0px; cy: 50%; font-size: 24px; color: $ink3) 7月;8月;9月
      p#v(right: 0px; cy: 50%; font-size: 44px; font-family: n; white-space: nowrap) 234{u}人{/};193{u}人{/};181{u}人{/}
  div#res(left: 292px; top: 458px; width: 350px; height: 84px; border-radius: 42px; background: #F4B9421A; border: 3px solid $amber; box-shadow: 0px 0px 40px #F4B9422E; in: {scale:0.7, opacity:0, duration:0.55, ease:'back.out(2)'})
    p#t(cx: 50%; cy: 50%; font-size: 42px; color: $amber; white-space: nowrap) 純増ゼロ
  p#res_sub(left: 0px; top: 560px; width: 936px; text-align: center; font-size: 22px; color: $ink2; font-family: m; in: {y:8, opacity:0, duration:0.5, ease:'power3.out'}) 新規課金を、解約が相殺している

# s03 月次の解約率: 縦棒 3 本が月の語で下から伸び、9 月の棒の頭が黄に割れて「決済失敗」・前の 2 本を沈める・右の板は 10.8% と内訳の割合の帯 + 2 行
section#s03(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch3(n: "02"; t: "月次の解約率")
headline#hl3 月次の解約率は {nn}13.2%{/} から {nn}10.8%{/} へ
panel#p3a(left: 112px; top: 232px; width: 1100px; height: 648px; t: "月次の解約率"; s: "月内の解約成立 ÷ 月初の有料契約"; tk: $coral; delay: 100ms)
  div#grid(left: "110;110;110"; top: "120;260;401"; width: 960px; height: 2px; background: $line) ×3
  p#gl(left: "20;20;20;20"; top: "107;248;387;527"; width: 72px; text-align: right; font-size: 20px; color: $ink3; font-family: n) ×4 15%;10%;5%;0%
  div#c1(left: 154px; top: 171px; width: 150px; height: 369px; border-radius: 6px 6px 0px 0px; background: linear(#E26A72,#B9505B,180); in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom'})
  div#c2(left: 386px; top: 224px; width: 150px; height: 316px; border-radius: 6px 6px 0px 0px; background: linear(#E26A72,#B9505B,180); in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom'})
  # 9 月の棒は 2 段 (下 = 自発的な解約・上 = 決済失敗 — 内訳の語で上の段が黄に変わり 3 px 浮く)
  div#c3(left: 615px; top: 237px; width: 150px; height: 303px; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom'})
    div#a(left: 0px; top: 64px; width: 150px; height: 238px; background: linear(#FF7A7A,#E0525C,180))
    div#b(left: 0px; top: 0px; width: 150px; height: 64px; border-radius: 6px 6px 0px 0px; background: #FF7676)
  div#base(left: 110px; top: 540px; width: 960px; height: 3px; background: $line2)
  p#v(left: "110;341;570"; top: "104;158;173"; width: 240px; text-align: center; font-size: 50px; line-height: 1.12; font-family: n; letter-spacing: -0.02em; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) ×3 13.2%;11.3%;10.8%
  div#x(left: "101;330;560"; top: "557;557;557"; width: 260px; height: 69px; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) ×3
    p#mo(left: 0px; top: 0px; width: 260px; text-align: center; font-size: 28px; line-height: 1.2) 7月;8月;9月
    p#fr(left: 0px; top: 39px; width: 260px; text-align: center; font-size: 22px; color: #A3AEC4; font-family: n) 234 / 1,771;193 / 1,705;181 / 1,682
  div#lab_b(left: 786px; top: 246px; width: 285px; height: 36px; in: {x:-10, opacity:0, duration:0.4, ease:'power3.out'})
    div#ln(left: 0px; cy: 50%; width: 18px; height: 3px; background: $amber)
    p#t(left: 28px; cy: 50%; font-size: 26px; color: $amber; white-space: nowrap) 決済失敗 {nn}2.3%{/}
  div#lab_a(left: 786px; top: 396px; width: 285px; height: 36px; in: {x:-10, opacity:0, duration:0.4, ease:'power3.out'})
    div#ln(left: 0px; cy: 50%; width: 18px; height: 3px; background: $coral)
    p#t(left: 28px; cy: 50%; font-size: 26px; color: $coral; white-space: nowrap) 自発的な解約 {nn}8.5%{/}
  div#leg(left: 796px; top: 96px; width: 270px; height: 30px; in: {y:-8, opacity:0, duration:0.45, ease:'power3.out'})
    div#c1(left: 0px; cy: 50%; width: 14px; height: 14px; border-radius: 4px; background: $coral)
    p#t1(left: 24px; cy: 50%; font-size: 20px; color: $ink2; font-family: m; white-space: nowrap) 自発的な解約
    div#c2(left: 166px; cy: 50%; width: 14px; height: 14px; border-radius: 4px; background: $amber)
    p#t2(left: 190px; cy: 50%; font-size: 20px; color: $ink2; font-family: m; white-space: nowrap) 決済失敗
panel#p3b(left: 1252px; top: 232px; width: 556px; height: 648px; t: "9月の内訳"; tk: $amber; delay: 240ms)
  p#kl(left: 40px; top: 94px; font-size: 24px; color: $ink3) 9月の解約率
  p#kv(left: 36px; top: 146px; font-size: 108px; line-height: 1; font-family: n; letter-spacing: -0.02em; in: {y:12, opacity:0, duration:0.5, ease:'power3.out'}) 10.8%
  # 割合の帯: 破線の枠の上に 8.5 (珊瑚) と 2.3 (黄) が語で左から伸びる
  shape#sbt(left: 40px; top: 290px; width: 476px; height: 40px; path: rect,r=0.19; background: #AABEE614; border: 2px solid #AABEE638; dash: 4,3)
  div#sba(left: 40px; top: 290px; width: 372px; height: 40px; border-radius: 8px 0px 0px 8px; background: $coral; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#sbb(left: 416px; top: 290px; width: 100px; height: 40px; border-radius: 0px 8px 8px 0px; background: $amber; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  # 内訳の 2 行 (先に 0.42 で置き、語で 1 にして % を出す)
  div#r(left: "41;41"; top: "372;452"; width: 476px; height: 70px; opacity: 0.42; delay: 550ms; in: {opacity:0, duration:0.5}) ×2
    div#chip(left: 0px; cy: 50%; width: 14px; height: 14px; border-radius: 4px; background: "$coral;$amber")
    p#nm(left: 28px; cy: 50%; font-size: 28px) 自発的な解約;決済失敗
    p#pv(right: 0px; cy: 50%; font-size: 46px; font-family: n; in: {opacity:0, duration:0.35}) 8.5%;2.3%
    div#ul(left: 0px; bottom: 0px; width: 476px; height: 2px; background: $line)
  p#nb(left: 40px; top: 568px; font-size: 22px; color: $note; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) 分母は月初の有料契約

# s04 週次の動き: 折れ線が 63 → 26 を左から描き (下の面も同じ速さで明ける)・点と値が線の到着で弾む・「63 → 26 件」の札・右の板は申請の 2 本の棒と破線の基準・「2割少ない」・93% の注記
section#s04(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch4(n: "03"; t: "週次の動き")
headline#hl4 9月は、週ごとに見ると{a}減っている{/}
panel#p4a(left: 112px; top: 232px; width: 1060px; height: 648px; t: "週次の解約成立"; s: "件／週"; tk: $coral; delay: 100ms)
  div#grid(left: "110;110;110"; top: "188;308;428"; width: 920px; height: 2px; background: $line) ×3
  div#base(left: 110px; top: 548px; width: 920px; height: 3px; background: $line2)
  p#gl(left: "20;20;20;20"; top: "176;296;416;536"; width: 72px; text-align: right; font-size: 20px; color: $ink3; font-family: n) ×4 60;40;20;0
  # 線の下の面: hf は上 30% → 下 0% の縦グラデ。グラデの塗りの形は絵の段 (線・点・札の上) に上がるので、単色の 14% で塗る
  shape#area(path: "M191 170 L450 260 L710 320 L971 392 L971 548 L191 548 Z"; background: #FF6B6B24; in: wipe {dir: 'right', duration: 1.89, ease: 'power1.inOut'})
  shape#line(path: "M191 170 L450 260 L710 320 L971 392"; background: none; border: 4px solid $coral; in: draw {duration: 1.89})
  shape#dot(left: "180;440;699;959"; top: "159;249;309;380"; width: "20;20;20;24"; height: "20;20;20;24"; border-radius: 50%; background: $coral; border: 4px solid #131B33; in: {scale:0, duration:0.35, ease:'back.out(2.5)'}) ×4
  p#vl(left: "131;390;650;911"; top: "107;197;257;329"; width: 120px; text-align: center; font-size: 42px; line-height: 1.14; font-family: n; in: {y:10, opacity:0, duration:0.35, ease:'power3.out'}) ×4 63;48;38;26
  p#xl(left: "110;371;630;890"; top: "566;566;566;566"; width: 160px; text-align: center; font-size: 22px; color: $ink2; font-family: n; delay: 150ms; in: {opacity:0, duration:0.5, stagger:{each:0.08}}) ×4 8/31週;9/7週;9/14週;9/21週
  div#call(left: 640px; top: 104px; width: 380px; height: 112px; border-radius: 16px; background: #FF6B6B14; border: 2px solid #FF6B6B73; in: {scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.8)'})
    p#t(cx: 50%; cy: 50%; font-size: 58px; font-family: n; color: $ink2; white-space: nowrap) 63 {ar}→{/} {cr}26{/}{un}件{/}
panel#p4b(left: 1212px; top: 232px; width: 596px; height: 648px; t: "解約の申請"; s: "件／週"; delay: 240ms)
  div#trk(left: "36;36"; top: "132;252"; width: 400px; height: 42px; border-radius: 0px 8px 8px 0px; background: #AABEE612) ×2
  div#b1(left: 36px; top: 132px; width: 356px; height: 42px; border-radius: 0px 8px 8px 0px; background: $slate2; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  p#bl(left: "36;36"; top: "96;216"; font-size: 24px; color: $ink2; white-space: nowrap) ×2 7月・8月の平均;9月
  div#b2(left: 36px; top: 252px; width: 267px; height: 42px; background: $blue; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#b2x(left: 303px; top: 252px; width: 27px; height: 42px; border-radius: 0px 8px 8px 0px; background: #5B9DFF61; in: {opacity:0, duration:0.4})
  p#bv1(left: 406px; top: 132px; font-size: 40px; line-height: 1.05; font-family: n; white-space: nowrap; in: {x:-10, opacity:0, duration:0.4}) 40{un}件{/}
  p#bv2(left: 406px; top: 252px; font-size: 40px; line-height: 1.05; font-family: n; white-space: nowrap; in: {x:-10, opacity:0, duration:0.4}) 30〜33{un}件{/}
  # 7・8 月の平均の位置に黄の破線 (上から下りる) と、差の幅のかぎ + 札
  shape#ref(left: 390px; top: 124px; width: 3px; height: 182px; path: line_v; border: 3px solid #F4B942B3; dash: 5,4; in: {scaleY:0, opacity:0, duration:0.45, ease:'power2.out', pivot:'top'})
  shape#gap(path: "M330 305 L330 317 L392 317 L392 305"; background: none; border: 3px solid #F4B942D9; in: {opacity:0, duration:0.3})
  badge#badge(left: 292px; top: 326px) 2割少ない
  div#note(left: 36px; top: 418px; width: 524px; height: 170px; border-radius: 16px; border: 2px solid $line2; background: #35D3B50F; delay: 650ms; in: {y:16, opacity:0, duration:0.55, ease:'power3.out'})
    p#t0(left: 28px; top: 16px; font-size: 20px; letter-spacing: 0.08em; color: $teal; white-space: nowrap) 申請から成立まで
    p#big(left: 28px; top: 40px; font-size: 76px; line-height: 1.16; font-family: n; color: $teal) 93%
    p#t1(left: 222px; top: 44px; font-size: 26px; white-space: nowrap) の申請が
    p#t2(left: 222px; top: 88px; font-size: 26px; white-space: nowrap) 45日以内に成立

# s05 在籍期間: 横棒 5 本 (3 か月未満 = 珊瑚・以上 = 青緑) を期間の語で 1 本ずつ・破線で 2 群に分け札・下の 3 本をかぎで括って「ひとケタ台」
section#s05(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch5(n: "04"; t: "在籍期間")
headline#hl5 在籍期間が短いほど、解約率は{a}高い{/}
panel#p5(left: 112px; top: 232px; width: 1696px; height: 648px; t: "在籍期間別の解約率"; s: "9月"; tk: $coral; delay: 100ms)
  div#vg(left: "705;1038;1371"; top: "92;92;92"; width: 2px; height: 468px; background: $line) ×3
  p#vgl(left: "323;656;989;1322"; top: "572;572;572;572"; width: 100px; text-align: center; font-size: 20px; color: $ink3; font-family: n) ×4 0%;10%;20%;30%
  div#axis(left: 370px; top: 88px; width: 3px; height: 476px; background: $line2)
  div#r(left: "0;0;0;0;0"; top: "101;197;300;396;492"; width: 1696px; height: 64px) ×5
    p#lb(left: 40px; cy: 50%; width: 300px; text-align: right; font-size: 30px; white-space: nowrap; in: {x:-14, opacity:0, duration:0.4, ease:'power3.out'}) 1か月未満;1〜3か月;3〜6か月;6〜12か月;12か月以上
    div#bar(left: 372px; top: 6px; width: "968;633;300;233;167"; height: 52px; border-radius: 0px 8px 8px 0px; background: "linear(#E0525C,#FF7A7A,90);linear(#E0525C,#FF7A7A,90);linear(#22A58D,#35D3B5,90);linear(#22A58D,#35D3B5,90);linear(#22A58D,#35D3B5,90)"; in: {scaleX:0, duration:0.75, ease:'power3.out', pivot:'left'})
    p#vv(left: "1356;1022;689;623;557"; cy: 50%; font-size: 48px; line-height: 1.17; font-family: n; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 29%;19%;9%;7%;5%
  shape#dv(left: 40px; top: 278px; width: 1616px; height: 3px; path: line_h; border: 3px solid #AABEE647; dash: 5,5; in: {opacity:0, duration:0.4})
  badge#tag_u(left: 1488px; top: 150px; color: $coral; background: #FF6B6B1F; border: 2px solid #FF6B6B73; in: {x:12, opacity:0, duration:0.45, ease:'power3.out'}) 契約3か月未満
  badge#tag_o(left: 1488px; top: 396px; color: $teal; background: #35D3B51A; border: 2px solid #35D3B573; in: {x:12, opacity:0, duration:0.45, ease:'power3.out'}) 3か月以上
  shape#br(path: "M836 306 L852 306 L852 551 L836 551"; background: none; border: 3px solid $teal; in: draw {duration: 0.5})
  badge#hk(left: 880px; top: 392px; font-size: 26px; color: #04201A; background: $teal; in: {x:-10, scale:0.9, opacity:0, duration:0.45, ease:'back.out(2)'}) ひとケタ台

# s06 最初の 3 か月: 左の板は母数と解約者の 2 本の帯 (3 か月未満の幅 25% → 53%) を破線の台形でつなぐ・右の板は 3 か月以上の折れ線が下がり、3 か月未満の赤い帯は 20〜23% に張り付く
section#s06(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch6(n: "05"; t: "最初の3か月")
headline#hl6 解約の{an}53%{/}は、契約3か月未満の人
panel#p6a(left: 112px; top: 232px; width: 820px; height: 648px; t: "契約3か月未満の比重"; s: "9月"; tk: $coral; delay: 100ms)
  p#l1(left: 40px; top: 104px; font-size: 26px; color: $ink2; white-space: nowrap; in: {opacity:0, duration:0.4}) 有料契約者（母数）
  shape#rib(path: "M41 234 L225 234 L432 384 L41 384 Z"; background: #FF6B6B24; border: 2px solid #FF6B6B59; dash: 4,4; in: {opacity:0, duration:0.6})
  div#a1(left: 40px; top: 150px; width: 184px; height: 84px; border-radius: 10px 0px 0px 10px; background: linear(#E0525C,#FF7A7A,90); in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  div#b1(left: 228px; top: 150px; width: 552px; height: 84px; border-radius: 0px 10px 10px 0px; background: #3A4766; in: {opacity:0, duration:0.5})
    p#t(cx: 50%; cy: 50%; font-size: 24px; color: #DDE4F1) 3か月以上
  div#a2(left: 40px; top: 384px; width: 392px; height: 84px; border-radius: 10px 0px 0px 10px; background: linear(#E0525C,#FF7A7A,90); in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#b2(left: 435px; top: 384px; width: 345px; height: 84px; border-radius: 0px 10px 10px 0px; background: #3A4766; in: {opacity:0, duration:0.5})
    p#t(cx: 50%; cy: 50%; font-size: 24px; color: #DDE4F1) 3か月以上
  p#t1(cx: 134px; cy: 192px; font-size: 50px; font-family: n; color: #FFFFFF; in: {scale:0.7, opacity:0, duration:0.45, ease:'back.out(2.2)'}) 25%
  p#t2(cx: 237px; cy: 426px; font-size: 50px; font-family: n; color: #FFFFFF; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 53%
  p#l2(left: 40px; top: 482px; font-size: 26px; color: $ink2; in: {opacity:0, duration:0.4}) 解約者
  div#leg(left: 40px; top: 574px; width: 345px; height: 30px; in: {opacity:0, duration:0.5})
    div#c1(left: 0px; cy: 50%; width: 14px; height: 14px; border-radius: 4px; background: $coral)
    p#t1(left: 24px; cy: 50%; font-size: 20px; color: $ink2; font-family: m; white-space: nowrap) 契約3か月未満
    div#c2(left: 178px; cy: 50%; width: 14px; height: 14px; border-radius: 4px; background: #3A4766)
    p#t2(left: 202px; cy: 50%; font-size: 20px; color: $ink2; font-family: m; white-space: nowrap) 3か月以上
panel#p6b(left: 972px; top: 232px; width: 836px; height: 648px; t: "解約率の推移"; s: "在籍期間別"; tk: $teal; delay: 240ms)
  div#grid(left: "101;101"; top: "221;380"; width: 690px; height: 2px; background: $line) ×2
  div#base(left: 100px; top: 540px; width: 690px; height: 3px; background: $line2)
  p#gl(left: "14;14;14"; top: "207;368;527"; width: 70px; text-align: right; font-size: 20px; color: $ink3; font-family: n) ×3 20%;10%;0%
  div#band(left: 130px; top: 172px; width: 620px; height: 48px; border-radius: 8px; background: #FF6B6B33; border: 2px solid #FF6B6B8C; in: {scaleX:0, opacity:0, duration:0.8, ease:'power3.out', pivot:'left'})
  p#bandl(left: 132px; top: 126px; font-size: 24px; color: $coral; white-space: nowrap; in: {y:8, opacity:0, duration:0.4}) 3か月未満 {nn}20〜23%{/}
  shape#line(path: "M180 390 L440 404 L701 434"; background: none; border: 4px solid $teal; in: draw {duration: 1})
  shape#dot(left: "171;431;690"; top: "381;395;423"; width: "20;20;23"; height: "20;20;23"; border-radius: 50%; background: $teal; border: 4px solid #131B33; in: {scale:0, duration:0.3, ease:'back.out(2.5)'}) ×3
  p#pl(left: "120;380;641"; top: "326;341;369"; width: 120px; text-align: center; font-size: 34px; font-family: n; color: $teal; in: {y:8, opacity:0, duration:0.3}) ×3 9.4%;8.5%;6.7%
  p#xl(left: "131;390;650"; top: "557;557;557"; width: 100px; text-align: center; font-size: 24px; color: $ink2; delay: 550ms; in: {opacity:0, duration:0.4, stagger:{each:0.06}}) ×3 7月;8月;9月
  div#leg(left: 522px; top: 92px; width: 285px; height: 30px; delay: 650ms; in: {opacity:0, duration:0.5})
    div#c1(left: 0px; cy: 50%; width: 28px; height: 4px; border-radius: 3px; background: $teal)
    p#t1(left: 39px; cy: 50%; font-size: 20px; color: $ink2; font-family: m; white-space: nowrap) 3か月以上
    div#c2(left: 154px; cy: 50%; width: 28px; height: 14px; border-radius: 3px; background: #FF6B6B4D; border: 2px solid #FF6B6BB3)
    p#t2(left: 194px; cy: 50%; font-size: 20px; color: $ink2; font-family: m; white-space: nowrap) 3か月未満

# s07 解約理由: 6 本の横棒を頭で一斉に (行ごとに 0.09 秒ずらし) 灰で伸ばし、上位 3 つを語で青に塗り替え順位の丸を弾ませ、残り 3 本を沈める
section#s07(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch7(n: "06"; t: "解約理由")
headline#hl7 解約理由の上位{a}3つ{/}
panel#p7(left: 112px; top: 232px; width: 1696px; height: 648px; t: "解約理由"; s: "9月・アンケート127件"; delay: 80ms)
  div#vg(left: "824;1157;1490"; top: "89;89;89"; width: 2px; height: 470px; background: $line) ×3
  p#vgl(left: "441;774;1107;1440"; top: "566;566;566;566"; width: 100px; text-align: center; font-size: 20px; color: $ink3; font-family: n) ×4 0%;10%;20%;30%
  div#axis(left: 488px; top: 84px; width: 3px; height: 478px; background: $line2)
  div#r(left: "0;0;0;0;0;0"; top: "96;176;257;336;416;497"; width: 1696px; height: 60px) ×6
    p#lb(left: 110px; cy: 50%; width: 350px; text-align: right; font-size: 30px; color: $ink2; white-space: nowrap; delay: "100ms;190ms;280ms;370ms;460ms;550ms"; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 一時的に使わない;思い通りに作れない;料金;選択なし;クレジットが余る;本数が足りない
    div#bar(left: 490px; top: 8px; width: "933;800;701;467;333;300"; height: 44px; border-radius: 0px 8px 8px 0px; background: #4A5878; delay: "150ms;240ms;330ms;420ms;510ms;600ms"; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#vv(left: "1442;1308;1208;975;842;809"; cy: 50%; font-size: 44px; line-height: 1.27; font-family: n; color: $ink2; delay: "550ms;640ms;730ms;820ms;910ms;1000ms"; in: {opacity:0, duration:0.4}) 28%;24%;21%;14%;10%;9%
  div#hi(left: "491;491;491"; top: "104;183;264"; width: "933;800;701"; height: 44px; border-radius: 0px 8px 8px 0px; background: linear(#4C8DF0,#8CBBFF,90); box-shadow: 0px 0px 26px #5B9DFF59; in: {scaleX:0, duration:0.55, ease:'power3.out', pivot:'left'}) ×3
  div#rk(left: "60;60;60"; top: "104;183;264"; width: 44px; height: 44px; border-radius: 148px; background: $blue; in: {scale:0, opacity:0, duration:0.4, ease:'back.out(2.4)'}) ×3
    p#t(cx: 50%; cy: 50%; font-size: 24px; font-family: n; color: #06122A) 1;2;3

# s08 期間別の理由: 左の板に 2 枚の札 (初回サイクル / 1 か月以上) を語で順に出し、理由の棒を伸ばす・右の板は音声系の icon が脈打ち 21% → 26% と「最多」の札
section#s08(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch8(n: "07"; t: "期間別の理由")
headline#hl8 解約理由は、利用期間で{a}変わる{/}
panel#p8a(left: 112px; top: 232px; width: 1040px; height: 648px; t: "利用期間別の解約理由"; s: "9月"; delay: 100ms)
  div#cl(left: 32px; top: 96px; width: 472px; height: 452px; border-radius: 16px; border: 2px solid $line2; background: #FFFFFF06; delay: 50ms; in: {y:18, opacity:0, duration:0.6, ease:'power3.out'})
    shape#dot(left: 26px; top: 34px; width: 12px; height: 12px; border-radius: 50%; background: $coral)
    p#tg(left: 50px; cy: 40px; font-size: 27px; white-space: nowrap) 初回サイクルで解約
    reason#i1(left: 26px; top: 124px; l: "思い通りに作れない"; v: "34%"; w: 357px)
    reason#i2(left: 26px; top: 284px; l: "本数が足りない"; v: "15%"; w: 158px; c: #5A6B8F; vc: $ink2)
  div#cr(left: 536px; top: 96px; width: 472px; height: 452px; border-radius: 16px; border: 2px solid $line2; background: #FFFFFF06; in: {y:18, opacity:0, duration:0.6, ease:'power3.out'})
    shape#dot(left: 26px; top: 34px; width: 12px; height: 12px; border-radius: 50%; background: $teal)
    p#tg(left: 50px; cy: 40px; font-size: 27px; white-space: nowrap) 1か月以上使って解約
    reason#i3(left: 26px; top: 124px; l: "一時的に使わない"; v: "29%"; w: 304px)
    reason#i4(left: 26px; top: 284px; l: "クレジットが余る"; v: "17%"; w: 178px; c: #5A6B8F; vc: $ink2)
  p#na(left: 34px; top: 574px; font-size: 22px; color: $note; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) バーの長さは 0〜40% の目盛り
panel#p8b(left: 1192px; top: 232px; width: 616px; height: 648px; t: "機能への不満"; tk: $amber; delay: 240ms)
  svg#ico(left: 36px; top: 98px; width: 84px; height: 84px; part: voice_ico; delay: 550ms; in: {scale:0.8, opacity:0, duration:0.45, ease:'back.out(2)'})
  p#kind(left: 136px; top: 104px; font-size: 27px; delay: 650ms; in: {x:-10, opacity:0, duration:0.45, ease:'power3.out'}) 音声系
  p#kind2(left: 136px; top: 146px; font-size: 21px; color: $ink3; font-family: m; white-space: nowrap; delay: 750ms; in: {x:-10, opacity:0, duration:0.45, ease:'power3.out'}) 読み間違い・イントネーション
  p#cap(left: 40px; top: 238px; font-size: 21px; color: $ink3; white-space: nowrap; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) 機能への不満に占める割合
  p#from(left: 40px; top: 306px; font-size: 66px; line-height: 1.06; font-family: n; color: $ink3; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) 21%
  shape#arr(left: 196px; top: 318px; width: 70px; height: 46px; path: arrow_r; background: $amber; border: 6px solid $amber; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'})
  p#to(left: 282px; top: 262px; font-size: 128px; line-height: 1.06; font-family: n; color: $amber; transform-origin: 0% 60%; in: {scale:0.8, opacity:0, duration:0.6, ease:'power3.out'}) 26%
  badge#most(left: 40px; top: 470px; font-size: 26px; padding: 10px 22px) 機能への不満で最多

# s09 利用行動: 100 マス (1 マス = 申請者の 1%) が中央に 10 × 10 で弾んで並び、「二極化」で左 45 (青)・中 32 (暗)・右 23 (黄) に分かれて色が付く・両端に大きな %
section#s09(stagger: {each:0}; out: {y:-16, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch9(n: "08"; t: "利用行動")
headline#hl9 解約する人の行動は{a}二極化{/}している
panel#p9(left: 112px; top: 232px; width: 1696px; height: 648px; t: "解約申請者の直前30日の動画作成本数"; s: "申請者に占める割合"; delay: 80ms)
  div#scale(left: 1290px; top: 90px; width: 300px; height: 33px; delay: 650ms; in: {opacity:0, duration:0.5})
    div#sq(left: 0px; cy: 50%; width: 22px; height: 22px; border-radius: 4px; background: #56627E)
    p#t(left: 34px; cy: 50%; font-size: 24px; color: #B4BED0; white-space: nowrap) 1マス ＝ 申請者の1%
  p#n45(left: 120px; top: 150px; width: 420px; text-align: center; font-size: 104px; line-height: 1.06; font-family: n; color: $blue; in: {y:18, scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.8)'}) 45%
  p#n23(left: 1156px; top: 150px; width: 420px; text-align: center; font-size: 104px; line-height: 1.06; font-family: n; color: $amber; in: {y:18, scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.8)'}) 23%
  p#l45(left: 120px; top: 566px; width: 420px; text-align: center; font-size: 28px; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) 動画 0本
  p#l23(left: 1156px; top: 566px; width: 420px; text-align: center; font-size: 28px; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) 動画 10本以上
  # 3 つの字は 10 × 10 の最初の位置の下端より下 (分かれた後に出る字でも、最初の位置に掛けると隠れになる)
  p#lmid(left: 648px; top: 566px; width: 400px; text-align: center; font-size: 26px; color: $ink2; in: {opacity:0, duration:0.5}) それ以外
# 100 マスは 3 つの ×N (0 本 45・それ以外 32・10 本以上 23)。最初の位置は 10 × 10 の列順、変種 .split が分かれた先と色 (語で 1 秒かけて補間して移る)
shape#wb(left: "755;755;755;755;755;755;755;755;755;755;797;797;797;797;797;797;797;797;797;797;839;839;839;839;839;839;839;839;839;839;881;881;881;881;881;881;881;881;881;881;923;923;923;923;923"; top: "383;425;467;509;551;593;635;677;719;761;383;425;467;509;551;593;635;677;719;761;383;425;467;509;551;593;635;677;719;761;383;425;467;509;551;593;635;677;719;761;383;425;467;509;551"; width: 34px; height: 34px; path: rect,r=0.22; background: $slate; border: none; delay: 100ms; in: {scale:0, duration:0.35, ease:'back.out(2)', stagger:{each:0.006}}) ×45
#wb.split(left: "258;258;258;258;258;300;300;300;300;300;342;342;342;342;342;384;384;384;384;384;426;426;426;426;426;468;468;468;468;468;510;510;510;510;510;552;552;552;552;552;594;594;594;594;594"; top: "531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;531;573;615;657;699"; background: $blue; move: 1000ms,power3.inOut)
shape#wm(left: "923;923;923;923;923;965;965;965;965;965;965;965;965;965;965;1007;1007;1007;1007;1007;1007;1007;1007;1007;1007;1049;1049;1049;1049;1049;1049;1049"; top: "593;635;677;719;761;383;425;467;509;551;593;635;677;719;761;383;425;467;509;551;593;635;677;719;761;383;425;467;509;551;593;635"; width: 34px; height: 34px; path: rect,r=0.22; background: $slate; border: none; delay: 370ms; in: {scale:0, duration:0.35, ease:'back.out(2)', stagger:{each:0.006}}) ×32
#wm.split(left: "797;797;797;797;839;839;839;839;881;881;881;881;923;923;923;923;965;965;965;965;1007;1007;1007;1007;1049;1049;1049;1049;1091;1091;1091;1091"; top: "552;594;636;678;552;594;636;678;552;594;636;678;552;594;636;678;552;594;636;678;552;594;636;678;552;594;636;678;552;594;636;678"; background: #2B3550; move: 1000ms,power3.inOut)
shape#wa(left: "1049;1049;1049;1091;1091;1091;1091;1091;1091;1091;1091;1091;1091;1133;1133;1133;1133;1133;1133;1133;1133;1133;1133"; top: "677;719;761;383;425;467;509;551;593;635;677;719;761;383;425;467;509;551;593;635;677;719;761"; width: 34px; height: 34px; path: rect,r=0.22; background: $slate; border: none; delay: 562ms; in: {scale:0, duration:0.35, ease:'back.out(2)', stagger:{each:0.006}}) ×23
#wa.split(left: "1377;1377;1377;1377;1377;1419;1419;1419;1419;1419;1461;1461;1461;1461;1461;1503;1503;1503;1503;1503;1545;1545;1545"; top: "531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;531;573;615;657;699;615;657;699"; background: $amber; move: 1000ms,power3.inOut)

# s10 まとめ: 3 枚の札を頭に並べ (1 枚目だけ点灯・2 / 3 枚目は 0.36 で待機)、文の頭で 1 枚ずつ点けて番号を弾ませ中身を出す・最後に札と見出しが上へ抜ける
section#s10(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.55, ease:'power2.in'})
chap#ch10(n: "09"; t: "まとめ")
headline#hl10 まとめ：3か月のデータから言えること
card#card1(left: 112px; n: "1"; t: "解約率は11%前後で[br]横ばい"; s: "ただし9月は、週ごとに減っている"; cap: "週次の解約成立（件）　8/31週 → 9/21週"; c: $blue; g: "linear(#5B9DFF,#86B8FF,90)")
  p#t(delay: 50ms)
  p#s(delay: 250ms)
  p#cap(delay: 700ms)
  div#base(left: 32px; top: 525px; width: 472px; height: 3px; background: $line2)
  shape#ml(path: "M62 360 L201 410 L342 443 L482 483"; background: none; border: 4px solid $coral; in: draw {duration: 1.2})
  shape#md(left: "53;192;333;473"; top: "351;401;434;474"; width: "17;17;17;18"; height: "17;17;17;18"; border-radius: 50%; background: $coral; border: 3px solid #141D37; in: {scale:0, duration:0.3, ease:'back.out(2.5)', stagger:{each:0.36}}) ×4
  p#m63(left: 39px; top: 302px; font-size: 34px; font-family: n; in: {opacity:0, duration:0.3}) 63
  p#m26(left: 456px; top: 418px; font-size: 34px; font-family: n; in: {opacity:0, duration:0.3}) 26
card#card2(left: 692px; n: "2"; t: "勝負は[br]最初の3か月"; s: "3か月未満の解約率が下がらない"; cap: "解約の53%が契約3か月未満"; c: $coral; g: "linear(#E0525C,#FF7A7A,90)"; opacity: 0.36; delay: 140ms)
  p#b20(left: 32px; top: 310px; font-size: 120px; line-height: 1.08; font-family: n; color: $coral; white-space: nowrap; transform-origin: 0% 50%; in: {scale:0.85, opacity:0, duration:0.55, ease:'power3.out'}) 20%{dai}台{/}
  p#b20s(left: 36px; top: 450px; font-size: 24px; color: $ink2; white-space: nowrap; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) 3か月未満の解約率（7〜9月）
  p#imp(left: 36px; top: 496px; font-size: 22px; color: $teal; white-space: nowrap; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) 3か月以上は {nn}9.4% → 6.7%{/} に改善
card#card3(left: 1272px; n: "3"; t: "まず直す所"; s: "初回サイクルと音声の品質"; cap: "9月の解約アンケートより"; c: $amber; g: "linear(#F4B942,#FFD27A,90)"; opacity: 0.36; delay: 260ms)
  div#it1(left: 32px; top: 300px; width: 472px; height: 104px; border-radius: 14px; border: 2px solid $line2; background: #FFFFFF08; in: {x:-16, opacity:0, duration:0.5, ease:'power3.out'})
    svg#ic(left: 18px; top: 22px; width: 60px; height: 60px; part: wand_ico)
    p#it(left: 94px; top: 16px; font-size: 26px; white-space: nowrap) 思い通りに作れない
    p#is(left: 94px; top: 58px; font-size: 20px; color: $ink3; font-family: m; white-space: nowrap) 初回サイクルの解約理由で {nn}34%{/}
  div#it2(left: 32px; top: 424px; width: 472px; height: 104px; border-radius: 14px; border: 2px solid $line2; background: #FFFFFF08; in: {x:-16, opacity:0, duration:0.5, ease:'power3.out'})
    svg#ic(left: 18px; top: 22px; width: 60px; height: 60px; part: bubble_ico)
    p#it(left: 94px; top: 16px; font-size: 26px; white-space: nowrap) 音声の読み間違い
    p#is(left: 94px; top: 58px; font-size: 20px; color: $ink3; font-family: m; white-space: nowrap) 機能への不満で最多{nn}（26%）{/}

# outro 締めの題: 上端の帯を抜き、題の絵が溶けて戻り、小札 → 2 行 → 下線 → 注記を組んで暗転
section#outro(stagger: {each:0})
img#out_bg(inset: 0; content: @title_img; main: kb {scale: [1, 1.04]}; in: {opacity:0, duration:1.6, ease:'power2.inOut'})
div#ok(left: 150px; top: 356px; width: 900px; height: 38px; delay: 400ms; in: {x:-20, opacity:0, duration:0.6, ease:'power3.out'})
  div#ln(left: 0px; cy: 50%; width: 44px; height: 3px; background: $teal)
  p#t(left: 60px; cy: 50%; font-size: 24px; letter-spacing: 0.14em; color: $teal; white-space: nowrap) 解約分析レポート ｜ まとめ
p#ot1(left: 150px; top: 399px; font-size: 66px; font-family: h; line-height: 1.27; white-space: nowrap; delay: 550ms; in: {y:24, opacity:0, duration:0.7, ease:'power3.out'}) 動画生成サービスの解約、
p#ot2(left: 150px; top: 483px; font-size: 66px; font-family: h; line-height: 1.27; white-space: nowrap; delay: 700ms; in: {y:24, opacity:0, duration:0.7, ease:'power3.out'}) 勝負は{a}最初の3か月{/}
div#ob(left: 150px; top: 591px; width: 460px; height: 4px; border-radius: 3px; background: linear($teal,$blue,90); delay: 900ms; in: {scaleX:0, duration:0.8, ease:'power3.inOut', pivot:'left'})
p#om(left: 150px; top: 624px; font-size: 22px; letter-spacing: 0.06em; color: $ink2; font-family: m; white-space: nowrap; delay: 1150ms; in: {y:10, opacity:0, duration:0.6, ease:'power3.out'}) 対象　有料契約者 ｜ 期間　7〜9月 ｜ 社内共有
```

```timeline.txt
#v2
cast n = "落ち着いた30代女性のナレーター、明瞭で聞き取りやすい声、社内の分析報告らしく淡々と丁寧に読む"
silence head=0ms tail=300ms
# 切替は書かない (場面は section の out で上へ抜けて消え、次の場面は境目から組み上がる・地と上端の帯は常設)。場面の境目の 0.47 秒前に風切り (前の cut の末尾の無音の間)

*** s01
[>#subtitle]
bgm music
@n: [silence:0.9s][♪air -2.7dB -750ms][♪deep -4.4dB -280ms][♪chime -5.4dB +200ms]この{b}3{/}か月の解約データから、[|]分かったことをまとめます。[silence:0.13s][♪swoosh -3.5dB][silence:0.47s]

*** s02
@n: [silence:0.15s][♪pop -2.7dB +50ms]有料契約者は、[|][>#p2a.k1 -450ms][>#p2a.k1.bar -300ms][>#p2a.k1.n -150ms][♪chime -3.5dB +50ms]{b}1,776{/}人から[>#p2a.arrow -750ms][>#p2a.k2 -500ms][>#p2a.k2.bar -350ms][>#p2a.k2.n -150ms][♪chime -1.9dB +50ms][>#p2a.na +600ms]{b}1,682{/}人へ。
@: [!#p2b.core to,{opacity:1, duration:0.45} -350ms][!#p2b.core punch {scale: 1.06, duration: .6} -350ms][!#p2b.node_in to,{opacity:1, duration:0.45} -100ms][>#p2b.node_in.v +50ms][>#p2b.node_in.u +130ms][>#p2b.a1 +350ms][>#p2b.fi[1] +900ms][!#p2b.fi[1] to,{x:39, duration:0.9, ease:'none', repeat:-1} +900ms][>#p2b.fi[2] +1200ms][!#p2b.fi[2] to,{x:39, duration:0.9, ease:'none', repeat:-1} +1200ms][>#p2b.fi[3] +1500ms][!#p2b.fi[3] to,{x:39, duration:0.9, ease:'none', repeat:-1} +1500ms][♪sub -4.4dB +50ms]毎月の新規課金は、解約で[!#p2b.node_out to,{opacity:1, duration:0.45} -450ms][>#p2b.a2 -200ms][>#p2b.node_out.r -100ms][♪sub -4.4dB -100ms][>#p2b.fo[1] +400ms][!#p2b.fo[1] to,{x:56, duration:0.9, ease:'none', repeat:-1} +400ms][>#p2b.fo[2] +700ms][!#p2b.fo[2] to,{x:56, duration:0.9, ease:'none', repeat:-1} +700ms][>#p2b.fo[3] +1000ms][!#p2b.fo[3] to,{x:56, duration:0.9, ease:'none', repeat:-1} +1000ms]相殺され、[|][>#p2b.res -50ms][♪deep -3.5dB +50ms][♪pop -1.9dB +70ms][>#p2b.res_sub +350ms][!#p2b.res glow,#F4B94261 {blur: 47} +500ms][=#p2b.res +1000ms]純増はゼロです。[silence:0.38s][♪swoosh -3.5dB][silence:0.47s]

*** s03
@n: [silence:0.15s]解約率は、[>#p3a.c1 -150ms][>#p3a.x[1] -150ms][>#p3a.v[1] +250ms][♪pop -3.5dB]{b}7{/}月の[>#p3a.c2 -90ms][>#p3a.x[2] -90ms][>#p3a.v[2] +310ms][♪pop -4.4dB -90ms]{b}13.2%{/}から、[|][>#p3a.c3 -150ms][>#p3a.x[3] -150ms][>#p3a.v[3] +250ms][♪pop -2.7dB]{b}9{/}月は[♪chime -2.7dB +100ms]{b}10.8%{/}。
@: [!#p3a.c1 to,{opacity:0.45, duration:0.5} -50ms][!#p3a.c2 to,{opacity:0.45, duration:0.5} -50ms][!#p3a.v[1] to,{opacity:0.45, duration:0.5} -50ms][!#p3a.v[2] to,{opacity:0.45, duration:0.5} -50ms][!#p3a.x[1] to,{opacity:0.45, duration:0.5} -50ms][!#p3a.x[2] to,{opacity:0.45, duration:0.5} -50ms][!#p3a.c3.b to,{y:-4, fill:'#F0B744', duration:0.5, ease:'power2.inOut'} -50ms][>#p3a.leg +100ms][>#p3b.kv -200ms][♪sub -5.4dB -50ms]内訳は、自発的な解約[>#p3a.lab_a -100ms][>#p3b.sba -200ms][!#p3b.r[1] to,{opacity:1, duration:0.4} -150ms][>#p3b.r[1].pv -50ms][♪pop -3.5dB]{b}8.5%{/}、[|]決済失敗[>#p3a.lab_b -100ms][>#p3b.sbb -200ms][!#p3b.r[2] to,{opacity:1, duration:0.4} -150ms][>#p3b.r[2].pv -50ms][>#p3b.nb +400ms][♪pop -3.5dB]{b}2.3%{/}です。[silence:0.38s][♪swoosh -3.5dB][silence:0.47s]

*** s04
@n: [silence:0.15s]ただ{b}9{/}月は、週ごとの解約成立が、[|][>#p4a.area -150ms][>#p4a.line -150ms][>#p4a.dot[1] -200ms][>#p4a.vl[1] -150ms][>#p4a.dot[2] +430ms][>#p4a.vl[2] +480ms][♪blip -3.5dB -250ms]{b}63{/}件から[>#p4a.dot[3] -380ms][>#p4a.vl[3] -330ms][>#p4a.dot[4] +250ms][>#p4a.vl[4] +300ms][♪chime -2.7dB +100ms][>#p4a.call +350ms]{b}26{/}件まで減りました。
@: [!#p4a to,{opacity:0.8, duration:0.6} -300ms][♪pop -3.5dB]申請も、[>#p4b.b1 -300ms][>#p4b.bv1 +200ms][>#p4b.b2 +250ms][>#p4b.b2x +800ms][>#p4b.bv2 +750ms][♪pop -4.4dB]{b}7{/}月と{b}8{/}月の平均より[>#p4b.ref -350ms][>#p4b.gap -200ms][>#p4b.badge -50ms][♪tick -1.9dB][♪pop -4.4dB +935ms]{b}2{/}割少ない水準です。[silence:0.73s][♪swoosh -3.5dB][silence:0.47s]

*** s05
@n: [silence:0.15s]在籍期間で見ると、[>#p5.r[1] -250ms][♪pop -3.5dB]{b}1{/}か月未満は[>#p5.r[1].bar -550ms][>#p5.r[1].vv -50ms]{b}29%{/}、[|][>#p5.r[2] -250ms][>#p5.tag_u +500ms][♪pop -3.5dB]{b}1{/}から{b}3{/}か月は[>#p5.r[2].bar -550ms][>#p5.r[2].vv -50ms]{b}19%{/}。
@: [>#p5.dv -400ms][>#p5.r[3] -150ms][>#p5.r[3].bar -100ms][>#p5.r[3].vv +400ms][>#p5.r[4] +50ms][>#p5.r[4].bar +100ms][>#p5.r[4].vv +600ms][>#p5.r[5] +250ms][>#p5.r[5].bar +300ms][>#p5.r[5].vv +800ms][>#p5.tag_o +400ms][♪pop -4.4dB]{b}3{/}か月以上は、[>#p5.br -350ms][>#p5.hk -50ms][♪tick -2.7dB]ひとケタ台に下がります。[silence:0.33s][♪swoosh -3.5dB][silence:0.47s]

*** s06
@n: [silence:0.15s]{b}3{/}か月未満の人は、母数の[>#p6a.l1 -800ms][>#p6a.a1 -350ms][>#p6a.b1 -100ms][>#p6a.t1 -50ms][♪pop -3.5dB]{b}25%{/}なのに、[|]解約の[>#p6a.a2 -400ms][>#p6a.l2 -400ms][>#p6a.b2 -100ms][>#p6a.t2 -50ms][>#p6a.rib +100ms][>#p6a.leg +500ms][♪chime -1.9dB +50ms][♪deep -6.6dB +50ms]{b}53%{/}を占めます。
@: [!#p6a to,{opacity:0.8, duration:0.6} -300ms]{b}3{/}か月以上は[>#p6b.line -300ms][>#p6b.dot[1] -300ms][>#p6b.pl[1] -250ms][>#p6b.dot[2] +180ms][>#p6b.pl[2] +230ms][>#p6b.dot[3] +660ms][>#p6b.pl[3] +710ms][♪blip -4.4dB -200ms]改善していますが、[|][>#p6b.band -100ms][♪pop -4.4dB]{b}3{/}か月未満は[>#p6b.bandl -200ms]{b}20%{/}台のままです。[silence:0.68s][♪swoosh -3.5dB][silence:0.47s]

*** s07
@n: [silence:0.15s]解約理由の上位は、[>#p7.hi[1] -150ms][>#p7.rk[1] -100ms][!#p7.r[1].lb recolor,$ink {duration: .3} -100ms][!#p7.r[1].vv recolor,$ink {duration: .3} -100ms][♪pop -3.5dB]一時的に使わない、[|][>#p7.hi[2] -150ms][>#p7.rk[2] -100ms][!#p7.r[2].lb recolor,$ink {duration: .3} -100ms][!#p7.r[2].vv recolor,$ink {duration: .3} -100ms][♪pop -3.5dB]思い通りに作れない、[>#p7.hi[3] -150ms][>#p7.rk[3] -100ms][!#p7.r[3].lb recolor,$ink {duration: .3} -100ms][!#p7.r[3].vv recolor,$ink {duration: .3} -100ms][♪pop -3.5dB]料金の[!#p7.r[4] to,{opacity:0.55, duration:0.5} -200ms][!#p7.r[5] to,{opacity:0.55, duration:0.5} -200ms][!#p7.r[6] to,{opacity:0.55, duration:0.5} -200ms]{b}3{/}つです。[silence:0.63s][♪swoosh -3.5dB][silence:0.47s]

*** s08
@n: [silence:0.15s][♪pop -4.4dB +100ms]初回サイクルでの解約は、[|]思い通りに作れないが[>#p8a.cl.i1 -700ms][>#p8a.cl.i1.bar -600ms][>#p8a.cl.i1.vv -250ms][>#p8a.cl.i2 +150ms][>#p8a.cl.i2.bar +250ms][>#p8a.cl.i2.vv +600ms][♪chime -2.7dB +50ms]{b}34%{/}。
@: [>#p8a.cr -450ms]{b}1{/}か月以上使った人では、[|][>#p8a.cr.i3 -450ms][>#p8a.cr.i3.bar -350ms][>#p8a.cr.i3.vv][♪pop -4.4dB -100ms]一時的と[>#p8a.cr.i4 -450ms][>#p8a.cr.i4.bar -350ms][>#p8a.cr.i4.vv][>#p8a.na +600ms][♪pop -4.4dB -100ms]クレジットの余りが目立ちます。
@: [!#p8a to,{opacity:0.8, duration:0.6} -300ms][♪sub -5.4dB -50ms]機能への不満では、[|]読み間違いなど[!#p8b.ico punch {scale: 1.12, duration: .6} -300ms][>#p8b.cap +100ms][>#p8b.from +180ms]音声系が[>#p8b.arr -450ms][>#p8b.to -350ms][♪chime -1.9dB +50ms]{b}26%{/}に増え、[|][>#p8b.most -50ms][♪deep -5.4dB]最多になりました。[silence:0.53s][♪swoosh -3.5dB][silence:0.47s]

*** s09
@n: [silence:0.15s]行動は[!#wb[*] .split -350ms][!#wm[*] .split -350ms][!#wa[*] .split -350ms][♪sub -3.5dB -100ms]二極化しています。
@: 申請者の[>#p9.n45 -200ms][>#p9.l45 +500ms][>#p9.lmid +900ms][♪chime -2.7dB +50ms]{b}45%{/}は、直前{b}30{/}日に{b}1{/}本も作らず、[|][>#p9.n23 -200ms][♪chime -2.7dB +50ms]{b}23%{/}は[>#p9.l23 -200ms]{b}10{/}本以上作っていました。[silence:0.43s][♪swoosh -3.5dB][silence:0.47s]

*** s10
@n: [silence:0.15s][♪click -1.9dB]解約率は{b}11%{/}前後で横ばいですが、[|][>#card1.ml -300ms][>#card1.md -300ms][>#card1.m63 -200ms][>#card1.m26 +900ms]{b}9{/}月は週ごとに減っています。
@: [!#card2 to,{opacity:1, duration:0.45, ease:'power2.out'} -300ms][!#card2.no punch {scale: 1.18, duration: .44} -300ms][>#card2.t -250ms][>#card2.s -50ms][>#card2.cap +400ms][>#card2.b20 +500ms][>#card2.b20s +1000ms][>#card2.imp +1250ms][♪click -1.9dB]勝負は、{b}20%{/}台のままの最初の{b}3{/}か月。
@: [!#card3 to,{opacity:1, duration:0.45, ease:'power2.out'} -300ms][!#card3.no punch {scale: 1.18, duration: .44} -300ms][>#card3.t -250ms][>#card3.s -50ms][>#card3.cap +400ms][>#card3.it1 +900ms][♪click -1.9dB]まず直すのは、[|]初回サイクルで思い通りに作れないことと、[|][>#card3.it2 -250ms]音声の読み間違いです。[silence:0.4s][♪air -5.4dB][silence:0.15s]

*** outro
@n: [<#hdr][<#prog][♪deep -6.6dB][silence:2.6s]
fade out,900ms
```

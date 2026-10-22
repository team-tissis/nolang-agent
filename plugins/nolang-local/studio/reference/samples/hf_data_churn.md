# data · churn-report (hf 全力版の全量の写し — 動画生成サービスの解約、この3か月で分かったこと・暗い紺の地に板と図を場面ごとに組む 10 場面のデータ図解) — canvas 1280x720

見せる作り: 全編の地 (紺の写真 + 周辺減光 + grain) と 2 場面目から常設の上端の帯 (題・期間・場面の境の目盛り・全編で伸びる進行・場面ごとに入れ替わる章札)・場面 = 見出しの帯 + 板 1〜2 枚 (板の def)・数字の語で伸びる図 (人数の棒・薄く置いて語で点ける流れ図と流れ続ける点・2 段に割れる縦棒・左から描く折れ線と面・期間別の横棒とかぎ・25% → 53% の帯と台形・上位 3 つを塗り替える横棒・100 マスが 3 群に分かれる)・話し終えた板を 0.8 に沈める・まとめの 3 枚の札を文の頭で点ける・題の絵で始まり題の絵で締めて暗転・字幕は黒い半透明の札で数字だけ黄の欧文・音の層 (場面の境の風切り + 語に結んだ効果音 59)

```design.txt
#v2
# 学ぶ作り: 暗い data の design system を根に 1 回 (palette・書体 3・数字の run・見出しの帯・板 panel の def・章札 chap の def) → 場面は板の中身だけ
# 常設の層: 全編の地 (紺の写真 + 周辺減光 + grain)・2 場面目から sticky の上端の帯 (題・期間・目盛り 8 本の線と全編で伸びる進行) と場面ごとに入れ替わる章札
# 場面 = 見出しの帯 + 板 1〜2 枚。板の中の図 (縦棒・折れ線・横棒・帯・流れ図・100 マス) は数字の語と同時に伸び、話し終えた板は 0.8 に沈めて次の板へ目を移す
# hf churn churn-report (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の退場は section の out (上へ抜けて消える)・切替は書かない (地は常設なので素の切替)
canvas 1280x720 bg=#05080F
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
subtitle.hug(bottom: 33px; font-size: 25px; line-height: 1.24; letter-spacing: 0.03em; color: #F4F7FC; background: #04070F94; border-radius: 8px; padding: 5px 17px 7px 17px; box-shadow: 0px 4px 16px #00000040; unit: sentence; strip: 、。>space; lead: 50; tail: 0; hold: off; in: {y:5, opacity:0, duration:0.16, ease:'power2.out'}; out: {opacity:0, duration:0.14, ease:'power2.in'})
# 曲: 頭の 1 秒と締めの題だけ前に出し、台詞の間は 6 dB 下げる
bgm#music(keys: "0:+6|800ms:+6|1300ms:0|end-3s:0|end-2.2s:+6"; fade: 600,1550) ミニマルで知的なディープテック寄りのアンビエント・エレクトロニカ、120 BPM 前後、シンセのアルペジオと柔らかいパッド、控えめなキックとハイハットとサブベース、主旋律なし、データ分析の解説向け

# 見出しの帯 (青緑 → 青の縦棒 + 50 px の題・語の強調は黄の run a)
def headline(t) = div(left: 75px; top: 85px; width: 1131px; height: 48px; in: {y:13, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 5px; height: 33px; border-radius: 3px; background: linear($teal,$blue,180))
  p#t(left: 20px; cy: 50%; font-size: 33px; line-height: 1.1; letter-spacing: 0.01em; white-space: nowrap; content: {t})
# 板: 紺の縦グラデ + 細い縁 + 深い影・頭の行 (色の小さな縦棒 + 題 + 補足) と下の罫
def panel(t, s="", tk=$blue) = div(border-radius: 13px; background: linear(#161F38E6,#0D1325E6,180); border: 1px solid #AABEE624; box-shadow: 0px 19px 40px #00000061; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
  div#tick(left: 20px; top: 15px; width: 4px; height: 16px; border-radius: 2px; background: {tk})
  p#pt(left: 33px; cy: 23px; font-size: 18px; letter-spacing: 0.02em; white-space: nowrap; content: {t})
  p#ps(left: .pt.right+9; cy: 23px; font-size: 13px; color: $ink3; font-family: m; white-space: nowrap; content: {s})
  div#rule(left: 0px; top: 45px; width: 100%; height: 1px; background: $line)
# 上端の帯の章札 (番号は青緑の欧文 + 題)・場面の頭に下から入り、場面の終わりに上へ抜ける
def chap(n, t) = div(left: 268px; top: 25px; width: 360px; height: 29px; z-index: front; delay: 50; in: {y:9, opacity:0, duration:0.45, ease:'power3.out'}; out: {y:-9, opacity:0, duration:0.3, ease:'power2.in'})
  p#n(left: 0px; cy: 50%; font-size: 13px; font-family: n; letter-spacing: 0.04em; color: $teal; content: {n})
  p#t(left: .n.right+8; cy: 50%; font-size: 15px; white-space: nowrap; content: {t})
# 丸い札 (既定は黄の地に黒文字・色は実体で上書き)
def badge(t) = p(font-size: 16px; line-height: 1.2; color: #1A1204; background: $amber; border-radius: 99px; padding: 5px 12px; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.45, ease:'back.out(2)'}; content: {t})
# 主役の人数 (月末の題 + 大きな数字 + 人 + 人数に比例した棒)
def kpi(l, v, w, c, vc=$ink) = div(width: 427px; height: 147px; in: {y:11, opacity:0, duration:0.5, ease:'power3.out'})
  p#l(left: 0px; top: 0px; font-size: 17px; letter-spacing: 0.06em; color: $ink3; content: {l})
  p#n(left: 0px; top: 31px; font-size: 75px; line-height: 1.08; font-family: n; letter-spacing: -0.02em; color: {vc}; in: {y:17, opacity:0, duration:0.55, ease:'power3.out'}; content: {v})
  p#u(left: .n.right+6; top: 74px; font-size: 25px; color: $ink2) 人
  div#bar(left: 0px; top: 123px; width: {w}; height: 9px; border-radius: 5px; background: {c}; in: {scaleX:0, duration:1, ease:'power3.out', pivot:'left'})
# 理由の行 (題 + 右端の % + 0〜40% の地の上の棒)
def reason(l, v, w, c="linear(#4C8DF0,#8CBBFF,90)", vc=$ink) = div(width: 280px; height: 93px)
  p#lb(left: 0px; top: 0px; font-size: 19px; white-space: nowrap; in: {x:-7, opacity:0, duration:0.4, ease:'power3.out'}; content: {l})
  div#tr(left: 0px; top: 39px; width: 280px; height: 20px; border-radius: 4px; background: #AABEE614)
  div#bar(left: 0px; top: 39px; width: {w}; height: 20px; border-radius: 4px; background: {c}; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  p#vv(right: 0px; top: -8px; font-size: 36px; line-height: 1.11; font-family: n; color: {vc}; in: {y:5, opacity:0, duration:0.4, ease:'power3.out'}; content: {v})
# まとめの札 (上端の色の線 + 番号の丸 + 題 2 行 + 補足 + 中身 + 出典)
# hf の作り: 番号は色の丸の上の暗い字 (check は全編の grain の幕と比べて low_contrast を出す)・hf の上端の線は札の角丸で切れる全幅の線 (ここは角を避けて内側に)
def card(n, t, s, cap, c, g) = div(top: 157px; width: 357px; height: 413px; border-radius: 15px; background: linear(#18223EF0,#0D1325F0,180); border: 1px solid #AABEE629; box-shadow: 0px 20px 47px #00000066; in: {y:27, scale:0.97, opacity:0, duration:0.7, ease:'power3.out'})
  div#top(left: 9px; top: 0px; width: 339px; height: 4px; border-radius: 2px; background: {g})
  div#no(left: 21px; top: 23px; width: 40px; height: 40px; border-radius: 99px; background: {c})
    p#t(cx: 50%; cy: 50%; font-size: 20px; font-family: n; color: #06122A; content: {n})
  p#t(left: 21px; top: 79px; width: 320px; font-size: 25px; line-height: 1.32; font-family: h; in: {y:9, opacity:0, duration:0.5, ease:'power3.out'}; content: {t})
  p#s(left: 21px; top: 155px; font-size: 17px; line-height: 1.36; color: $ink2; white-space: nowrap; in: {y:7, opacity:0, duration:0.5, ease:'power3.out'}; content: {s})
  p#cap(left: 21px; top: 373px; font-size: 13px; color: $ink3; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}; content: {cap})

# 全編の地 (根): 紺の写真が 119 秒かけて 1.08 → 1.16 に寄る + 周辺減光 + grain
img#plate(inset: 0; content: @plate; opacity: 0.95; z-index: back; main: kb {scale: [1.08, 1.16], focus: ['45% 50%', '55% 50%']}; in: none)
veil#vig(background: radial(#05080F00@55%,#03050A8C@100%,50%,45%); z-index: back; in: none)
veil#grain(grain: 0.05; color: #00000000; z-index: back; in: none)

# s01 題: 粒子の光の絵が寄りながら明け、左の空きに小札 → mask から上がる 2 行 → 下線 → 3 つの注記。題の組ごとゆっくり寄って上へ抜ける
section#s01(stagger: {each:0})
img#title_bg(inset: 0; content: @title_img; main: none; in: keys(at=0 scale=1.12 opacity=0 | at=0.374 scale=1.03 opacity=1 ease=power2.out | at=1 scale=1 ease=none),duration=4280; out: {opacity:0, duration:0.6, ease:'power2.inOut'})
group#title(left: 100px; top: 220px; width: 733px; height: 307px; main: keys(at=0 scale=1 | at=1 scale=1.025),window=0,4900,forwards; transform-origin: 0% 50%; out: {y:-12, opacity:0, duration:0.4, ease:'power2.in'})
  div#kicker(left: 0px; top: 0px; width: 600px; height: 25px; delay: 300; in: {x:-16, opacity:0, duration:0.6, ease:'power3.out'})
    div#ln(left: 0px; cy: 50%; width: 29px; height: 2px; background: $teal)
    p#t(left: 40px; cy: 50%; font-size: 17px; letter-spacing: 0.14em; color: $teal; white-space: nowrap) 社内共有 ｜ 解約分析レポート
  p#l1(left: 0px; top: 35px; font-size: 61px; font-family: h; line-height: 1.3; letter-spacing: 0.01em; white-space: nowrap; delay: 500; in: {y:83, duration:0.8, ease:'power4.out', clip:true}) 動画生成サービスの解約、
  p#l2(left: 0px; top: 113px; font-size: 61px; font-family: h; line-height: 1.3; letter-spacing: 0.01em; white-space: nowrap; delay: 660; in: {y:83, duration:0.8, ease:'power4.out', clip:true}) この{a}3か月{/}で分かったこと
  div#bar(left: 0px; top: 212px; width: 413px; height: 4px; border-radius: 2px; background: linear($teal,$blue,90); delay: 1050; in: {scaleX:0, duration:0.9, ease:'power3.inOut', pivot:'left'})
  p#meta(left: "0;153;275"; top: "237;237;237"; font-size: 17px; color: $ink2; font-family: m; white-space: nowrap; delay: 1350; in: {y:9, opacity:0, duration:0.5, ease:'power3.out', stagger:{each:0.12}}) ×3 {lb}対象{/} 有料契約者;{lb}期間{/} 7〜9月;{lb}データ{/} 解約・申請・アンケート

# s02 現状: 上端の帯が降りて進行が伸び始める・左の板で 1,776 → 1,682 人を棒で比べ、右の板の流れ図 (新規 → 契約者 → 解約) を薄く置いて語で点ける・点が矢印を流れ続け「純増ゼロ」が光る
section#s02(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
# 上端の帯 (sticky・締めの題で抜く): 左の題・右の期間・細い線に場面の境の目盛り 8 本
div#hdr.sticky(left: 75px; top: 25px; width: 1131px; height: 40px; z-index: front; delay: 100; in: {y:-8, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-7, opacity:0, duration:0.6, ease:'power2.in'})
  div#dot(left: 0px; top: 11px; width: 7px; height: 7px; border-radius: 1px; background: linear($teal,$blue,135))
  p#l(left: 16px; cy: 15px; font-size: 14px; letter-spacing: 0.12em; color: #8E9AB2; white-space: nowrap) 解約分析レポート
  p#r(right: 0px; cy: 15px; font-size: 13px; letter-spacing: 0.06em; color: $ink3; font-family: m; white-space: nowrap) 7〜9月 ｜ 社内共有
  div#track(left: 0px; top: 37px; width: 1131px; height: 2px; background: #AABEE624)
  div#tk(left: "109;240;366;469;597;670;842;949"; top: 35px; width: 2px; height: 5px; background: #AABEE659) ×8
# 進行 (線の上を全編の残りで左から伸びる)
progress#prog.sticky(left: 75px; top: 62px; width: 1131px; height: 2px; background: linear($teal,$blue,90); until: end; z-index: front; overlap: hdr)
chap#ch2(n: "01"; t: "現状")
headline#hl2 新規課金があっても、契約者数は{a}増えていない{/}
panel#p2a(left: 75px; top: 155px; width: 480px; height: 432px; t: "有料契約者数"; s: "各月末時点"; delay: 80)
  kpi#k1(left: 29px; top: 69px; l: "6月末"; v: "1,776"; w: 400px; c: $slate2; vc: $ink2)
  div#arrow(left: 29px; top: 212px; width: 400px; height: 33px; in: {y:-7, opacity:0, duration:0.45, ease:'power3.out'})
    icon#i(left: 0px; cy: 50%; font-size: 24px; name: arrow-down; color: #6E7A92)
    p#t(left: 27px; cy: 50%; font-size: 15px; color: $ink3; font-family: m) 3か月後
  kpi#k2(left: 29px; top: 257px; l: "9月末"; v: "1,682"; w: 379px; c: "linear(#4C8DF0,#86B8FF,90)")
  p#na(left: 29px; top: 399px; font-size: 15px; color: $note; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) バーの長さ ＝ 人数（0 起点）
# 流れ図: 3 つの枠を 0.32 で先に置き、語で 1 に点ける (点は矢印の上を 0.9 秒で流れ続ける)
panel#p2b(left: 581px; top: 155px; width: 624px; height: 432px; t: "毎月の出入り"; s: "7〜9月"; tk: $amber; delay: 220)
  shape#a1(left: 208px; top: 173px; width: 32px; height: 14px; path: arrow_r; background: $teal; border: 3px solid $teal; in: draw {duration: 0.5})
  shape#a2(left: 381px; top: 173px; width: 44px; height: 14px; path: arrow_r; background: $coral; border: 3px solid $coral; in: draw {duration: 0.5})
  shape#fi.ellipse(left: "206;207;208"; top: "177;177;177"; width: 6px; height: 6px; background: #BFF5EA; in: {opacity:0, duration:0.3}) ×3
  shape#fo.ellipse(left: "380;381;382"; top: "177;177;177"; width: 6px; height: 6px; background: #FFD0D0; in: {opacity:0, duration:0.3}) ×3
  div#node_in(left: 20px; top: 113px; width: 184px; height: 133px; border-radius: 12px; background: #35D3B512; border: 2px solid #35D3B58C; opacity: 0.32; delay: 450; in: {y:9, opacity:0, duration:0.6, ease:'power3.out'})
    p#t(left: 0px; top: 15px; width: 184px; text-align: center; font-size: 17px; color: $teal) 新規課金
    p#v(left: 0px; top: 48px; width: 184px; text-align: center; font-size: 31px; line-height: 1.39; font-family: n; in: {y:5, opacity:0, duration:0.45, ease:'power3.out'}) 170〜178
    p#u(left: 0px; top: 93px; width: 184px; text-align: center; font-size: 15px; color: $ink3; font-family: m; in: {y:5, opacity:0, duration:0.45, ease:'power3.out'}) 人／月
  div#core(left: 245px; top: 113px; width: 133px; height: 133px; border-radius: 99px; background: radial(#5B9DFF38,#5B9DFF0A@70%,50%,40%); border: 2px solid #AABEE659; opacity: 0.32; delay: 550; in: {y:9, opacity:0, duration:0.6, ease:'power3.out'})
    p#t(cx: 50%; cy: 50%; font-size: 17px; white-space: nowrap) 有料契約者
  div#node_out(left: 431px; top: 79px; width: 167px; height: 203px; border-radius: 12px; background: #FF6B6B12; border: 2px solid #FF6B6B8C; opacity: 0.32; delay: 650; in: {y:9, opacity:0, duration:0.6, ease:'power3.out'})
    p#t(left: 0px; top: 15px; width: 167px; text-align: center; font-size: 17px; color: $coral) 解約成立
    div#r(left: "20;20;20"; top: "52;97;143"; width: 127px; height: 43px; in: {x:11, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.12}}) ×3
      p#m(left: 0px; cy: 50%; font-size: 16px; color: $ink3) 7月;8月;9月
      p#v(right: 0px; cy: 50%; font-size: 29px; font-family: n; white-space: nowrap) 234{u}人{/};193{u}人{/};181{u}人{/}
  div#res(left: 195px; top: 305px; width: 233px; height: 56px; border-radius: 28px; background: #F4B9421A; border: 2px solid $amber; box-shadow: 0px 0px 27px #F4B9422E; in: {scale:0.7, opacity:0, duration:0.55, ease:'back.out(2)'})
    p#t(cx: 50%; cy: 50%; font-size: 28px; color: $amber; white-space: nowrap) 純増ゼロ
  p#res_sub(left: 0px; top: 373px; width: 624px; text-align: center; font-size: 15px; color: $ink2; font-family: m; in: {y:5, opacity:0, duration:0.5, ease:'power3.out'}) 新規課金を、解約が相殺している

# s03 月次の解約率: 縦棒 3 本が月の語で下から伸び、9 月の棒の頭が黄に割れて「決済失敗」・前の 2 本を沈める・右の板は 10.8% と内訳の割合の帯 + 2 行
section#s03(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch3(n: "02"; t: "月次の解約率")
headline#hl3 月次の解約率は {nn}13.2%{/} から {nn}10.8%{/} へ
panel#p3a(left: 75px; top: 155px; width: 733px; height: 432px; t: "月次の解約率"; s: "月内の解約成立 ÷ 月初の有料契約"; tk: $coral; delay: 100)
  div#grid(left: "73;73;73"; top: "80;173;267"; width: 640px; height: 1px; background: $line) ×3
  p#gl(left: "13;13;13;13"; top: "71;165;258;351"; width: 48px; text-align: right; font-size: 13px; color: $ink3; font-family: n) ×4 15%;10%;5%;0%
  div#c1(left: 103px; top: 114px; width: 100px; height: 246px; border-radius: 4px 4px 0px 0px; background: linear(#E26A72,#B9505B,180); in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom'})
  div#c2(left: 257px; top: 149px; width: 100px; height: 211px; border-radius: 4px 4px 0px 0px; background: linear(#E26A72,#B9505B,180); in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom'})
  # 9 月の棒は 2 段 (下 = 自発的な解約・上 = 決済失敗 — 内訳の語で上の段が黄に変わり 3 px 浮く)
  div#c3(left: 410px; top: 158px; width: 100px; height: 202px; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom'})
    div#a(left: 0px; top: 43px; width: 100px; height: 159px; background: linear(#FF7A7A,#E0525C,180))
    div#b(left: 0px; top: 0px; width: 100px; height: 43px; border-radius: 4px 4px 0px 0px; background: #FF7676)
  div#base(left: 73px; top: 360px; width: 640px; height: 2px; background: $line2)
  p#v(left: "73;227;380"; top: "69;105;115"; width: 160px; text-align: center; font-size: 33px; line-height: 1.12; font-family: n; letter-spacing: -0.02em; in: {y:9, opacity:0, duration:0.4, ease:'power3.out'}) ×3 13.2%;11.3%;10.8%
  div#x(left: "67;220;373"; top: "371;371;371"; width: 173px; height: 46px; in: {y:7, opacity:0, duration:0.45, ease:'power3.out'}) ×3
    p#mo(left: 0px; top: 0px; width: 173px; text-align: center; font-size: 19px; line-height: 1.2) 7月;8月;9月
    p#fr(left: 0px; top: 26px; width: 173px; text-align: center; font-size: 15px; color: #A3AEC4; font-family: n) 234 / 1,771;193 / 1,705;181 / 1,682
  div#lab_b(left: 524px; top: 164px; width: 190px; height: 24px; in: {x:-7, opacity:0, duration:0.4, ease:'power3.out'})
    div#ln(left: 0px; cy: 50%; width: 12px; height: 2px; background: $amber)
    p#t(left: 19px; cy: 50%; font-size: 17px; color: $amber; white-space: nowrap) 決済失敗 {nn}2.3%{/}
  div#lab_a(left: 524px; top: 264px; width: 190px; height: 24px; in: {x:-7, opacity:0, duration:0.4, ease:'power3.out'})
    div#ln(left: 0px; cy: 50%; width: 12px; height: 2px; background: $coral)
    p#t(left: 19px; cy: 50%; font-size: 17px; color: $coral; white-space: nowrap) 自発的な解約 {nn}8.5%{/}
  div#leg(left: 531px; top: 64px; width: 180px; height: 20px; in: {y:-5, opacity:0, duration:0.45, ease:'power3.out'})
    div#c1(left: 0px; cy: 50%; width: 9px; height: 9px; border-radius: 3px; background: $coral)
    p#t1(left: 16px; cy: 50%; font-size: 13px; color: $ink2; font-family: m; white-space: nowrap) 自発的な解約
    div#c2(left: 111px; cy: 50%; width: 9px; height: 9px; border-radius: 3px; background: $amber)
    p#t2(left: 127px; cy: 50%; font-size: 13px; color: $ink2; font-family: m; white-space: nowrap) 決済失敗
panel#p3b(left: 835px; top: 155px; width: 371px; height: 432px; t: "9月の内訳"; tk: $amber; delay: 240)
  p#kl(left: 27px; top: 63px; font-size: 16px; color: $ink3) 9月の解約率
  p#kv(left: 24px; top: 97px; font-size: 72px; line-height: 1; font-family: n; letter-spacing: -0.02em; in: {y:8, opacity:0, duration:0.5, ease:'power3.out'}) 10.8%
  # 割合の帯: 破線の枠の上に 8.5 (珊瑚) と 2.3 (黄) が語で左から伸びる
  shape#sbt(left: 27px; top: 193px; width: 317px; height: 27px; path: rect,r=0.19; background: #AABEE614; border: 1px solid #AABEE638; dash: 4,3)
  div#sba(left: 27px; top: 193px; width: 248px; height: 27px; border-radius: 5px 0px 0px 5px; background: $coral; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#sbb(left: 277px; top: 193px; width: 67px; height: 27px; border-radius: 0px 5px 5px 0px; background: $amber; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  # 内訳の 2 行 (先に 0.42 で置き、語で 1 にして % を出す)
  div#r(left: "27;27"; top: "248;301"; width: 317px; height: 47px; opacity: 0.42; delay: 550; in: {opacity:0, duration:0.5}) ×2
    div#chip(left: 0px; cy: 50%; width: 9px; height: 9px; border-radius: 3px; background: "$coral;$amber")
    p#nm(left: 19px; cy: 50%; font-size: 19px) 自発的な解約;決済失敗
    p#pv(right: 0px; cy: 50%; font-size: 31px; font-family: n; in: {opacity:0, duration:0.35}) 8.5%;2.3%
    div#ul(left: 0px; bottom: 0px; width: 317px; height: 1px; background: $line)
  p#nb(left: 27px; top: 379px; font-size: 15px; color: $note; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) 分母は月初の有料契約

# s04 週次の動き: 折れ線が 63 → 26 を左から描き (下の面も同じ速さで明ける)・点と値が線の到着で弾む・「63 → 26 件」の札・右の板は申請の 2 本の棒と破線の基準・「2割少ない」・93% の注記
section#s04(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch4(n: "03"; t: "週次の動き")
headline#hl4 9月は、週ごとに見ると{a}減っている{/}
panel#p4a(left: 75px; top: 155px; width: 707px; height: 432px; t: "週次の解約成立"; s: "件／週"; tk: $coral; delay: 100)
  div#grid(left: "73;73;73"; top: "125;205;285"; width: 613px; height: 1px; background: $line) ×3
  div#base(left: 73px; top: 365px; width: 613px; height: 2px; background: $line2)
  p#gl(left: "13;13;13;13"; top: "117;197;277;357"; width: 48px; text-align: right; font-size: 13px; color: $ink3; font-family: n) ×4 60;40;20;0
  # 線の下の面: hf は上 30% → 下 0% の縦グラデ。グラデの塗りの形は絵の段 (線・点・札の上) に上がるので、単色の 14% で塗る
  shape#area(path: "M127 113 L300 173 L473 213 L647 261 L647 365 L127 365 Z"; background: #FF6B6B24; in: wipe {dir: 'right', duration: 1.89, ease: 'power1.inOut'})
  shape#line(path: "M127 113 L300 173 L473 213 L647 261"; background: none; border: 3px solid $coral; in: draw {duration: 1.89})
  shape#dot.ellipse(left: "120;293;466;639"; top: "106;166;206;253"; width: "13;13;13;16"; height: "13;13;13;16"; background: $coral; border: 3px solid #131B33; in: {scale:0, duration:0.35, ease:'back.out(2.5)'}) ×4
  p#vl(left: "87;260;433;607"; top: "71;131;171;219"; width: 80px; text-align: center; font-size: 28px; line-height: 1.14; font-family: n; in: {y:7, opacity:0, duration:0.35, ease:'power3.out'}) ×4 63;48;38;26
  p#xl(left: "73;247;420;593"; top: "377;377;377;377"; width: 107px; text-align: center; font-size: 15px; color: $ink2; font-family: n; delay: 150; in: {opacity:0, duration:0.5, stagger:{each:0.08}}) ×4 8/31週;9/7週;9/14週;9/21週
  div#call(left: 427px; top: 69px; width: 253px; height: 75px; border-radius: 11px; background: #FF6B6B14; border: 1px solid #FF6B6B73; in: {scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.8)'})
    p#t(cx: 50%; cy: 50%; font-size: 39px; font-family: n; color: $ink2; white-space: nowrap) 63 {ar}→{/} {cr}26{/}{un}件{/}
panel#p4b(left: 808px; top: 155px; width: 397px; height: 432px; t: "解約の申請"; s: "件／週"; delay: 240)
  p#bl(left: "24;24"; top: "64;144"; font-size: 16px; color: $ink2; white-space: nowrap) ×2 7月・8月の平均;9月
  div#trk(left: "24;24"; top: "88;168"; width: 267px; height: 28px; border-radius: 0px 5px 5px 0px; background: #AABEE612) ×2
  div#b1(left: 24px; top: 88px; width: 237px; height: 28px; border-radius: 0px 5px 5px 0px; background: $slate2; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#b2(left: 24px; top: 168px; width: 178px; height: 28px; background: $blue; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#b2x(left: 202px; top: 168px; width: 18px; height: 28px; border-radius: 0px 5px 5px 0px; background: #5B9DFF61; in: {opacity:0, duration:0.4})
  p#bv1(left: 271px; top: 88px; font-size: 27px; line-height: 1.05; font-family: n; white-space: nowrap; in: {x:-7, opacity:0, duration:0.4}) 40{un}件{/}
  p#bv2(left: 271px; top: 168px; font-size: 27px; line-height: 1.05; font-family: n; white-space: nowrap; in: {x:-7, opacity:0, duration:0.4}) 30〜33{un}件{/}
  # 7・8 月の平均の位置に黄の破線 (上から下りる) と、差の幅のかぎ + 札
  shape#ref(left: 260px; top: 83px; width: 2px; height: 121px; path: line_v; border: 2px solid #F4B942B3; dash: 5,4; in: {scaleY:0, opacity:0, duration:0.45, ease:'power2.out', pivot:'top'})
  shape#gap(path: "M220 203 L220 211 L261 211 L261 203"; background: none; border: 2px solid #F4B942D9; in: {opacity:0, duration:0.3})
  badge#badge(left: 195px; top: 217px) 2割少ない
  div#note(left: 24px; top: 279px; width: 349px; height: 113px; border-radius: 11px; border: 1px solid $line2; background: #35D3B50F; delay: 650; in: {y:11, opacity:0, duration:0.55, ease:'power3.out'})
    p#t0(left: 19px; top: 11px; font-size: 13px; letter-spacing: 0.08em; color: $teal; white-space: nowrap) 申請から成立まで
    p#big(left: 19px; top: 27px; font-size: 51px; line-height: 1.16; font-family: n; color: $teal) 93%
    p#t1(left: 148px; top: 29px; font-size: 17px; white-space: nowrap) の申請が
    p#t2(left: 148px; top: 59px; font-size: 17px; white-space: nowrap) 45日以内に成立

# s05 在籍期間: 横棒 5 本 (3 か月未満 = 珊瑚・以上 = 青緑) を期間の語で 1 本ずつ・破線で 2 群に分け札・下の 3 本をかぎで括って「ひとケタ台」
section#s05(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch5(n: "04"; t: "在籍期間")
headline#hl5 在籍期間が短いほど、解約率は{a}高い{/}
panel#p5(left: 75px; top: 155px; width: 1131px; height: 432px; t: "在籍期間別の解約率"; s: "9月"; tk: $coral; delay: 100)
  div#vg(left: "470;692;914"; top: "61;61;61"; width: 1px; height: 312px; background: $line) ×3
  p#vgl(left: "215;437;659;881"; top: "381;381;381;381"; width: 67px; text-align: center; font-size: 13px; color: $ink3; font-family: n) ×4 0%;10%;20%;30%
  div#axis(left: 247px; top: 59px; width: 2px; height: 317px; background: $line2)
  div#r(left: "0;0;0;0;0"; top: "67;131;200;264;328"; width: 1131px; height: 43px) ×5
    p#lb(left: 27px; cy: 50%; width: 200px; text-align: right; font-size: 20px; white-space: nowrap; in: {x:-9, opacity:0, duration:0.4, ease:'power3.out'}) 1か月未満;1〜3か月;3〜6か月;6〜12か月;12か月以上
    div#bar(left: 248px; top: 4px; width: "645;422;200;155;111"; height: 35px; border-radius: 0px 5px 5px 0px; background: "linear(#E0525C,#FF7A7A,90);linear(#E0525C,#FF7A7A,90);linear(#22A58D,#35D3B5,90);linear(#22A58D,#35D3B5,90);linear(#22A58D,#35D3B5,90)"; in: {scaleX:0, duration:0.75, ease:'power3.out', pivot:'left'})
    p#vv(left: "904;681;459;415;371"; cy: 50%; font-size: 32px; line-height: 1.17; font-family: n; in: {x:-8, opacity:0, duration:0.4, ease:'power3.out'}) 29%;19%;9%;7%;5%
  shape#dv(left: 27px; top: 185px; width: 1077px; height: 2px; path: line_h; border: 2px solid #AABEE647; dash: 5,5; in: {opacity:0, duration:0.4})
  badge#tag_u(left: 968px; top: 100px; color: $coral; background: #FF6B6B1F; border: 1px solid #FF6B6B73; in: {x:8, opacity:0, duration:0.45, ease:'power3.out'}) 契約3か月未満
  badge#tag_o(left: 968px; top: 264px; color: $teal; background: #35D3B51A; border: 1px solid #35D3B573; in: {x:8, opacity:0, duration:0.45, ease:'power3.out'}) 3か月以上
  shape#br(path: "M557 204 L568 204 L568 367 L557 367"; background: none; border: 2px solid $teal; in: draw {duration: 0.5})
  badge#hk(left: 587px; top: 261px; font-size: 17px; color: #04201A; background: $teal; in: {x:-7, scale:0.9, opacity:0, duration:0.45, ease:'back.out(2)'}) ひとケタ台

# s06 最初の 3 か月: 左の板は母数と解約者の 2 本の帯 (3 か月未満の幅 25% → 53%) を破線の台形でつなぐ・右の板は 3 か月以上の折れ線が下がり、3 か月未満の赤い帯は 20〜23% に張り付く
section#s06(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch6(n: "05"; t: "最初の3か月")
headline#hl6 解約の{an}53%{/}は、契約3か月未満の人
panel#p6a(left: 75px; top: 155px; width: 547px; height: 432px; t: "契約3か月未満の比重"; s: "9月"; tk: $coral; delay: 100)
  p#l1(left: 27px; top: 69px; font-size: 17px; color: $ink2; white-space: nowrap; in: {opacity:0, duration:0.4}) 有料契約者（母数）
  shape#rib(path: "M27 156 L150 156 L288 256 L27 256 Z"; background: #FF6B6B24; border: 1px solid #FF6B6B59; dash: 4,4; in: {opacity:0, duration:0.6})
  div#a1(left: 27px; top: 100px; width: 123px; height: 56px; border-radius: 7px 0px 0px 7px; background: linear(#E0525C,#FF7A7A,90); in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  div#b1(left: 152px; top: 100px; width: 368px; height: 56px; border-radius: 0px 7px 7px 0px; background: #3A4766; in: {opacity:0, duration:0.5})
    p#t(cx: 50%; cy: 50%; font-size: 16px; color: #DDE4F1) 3か月以上
  div#a2(left: 27px; top: 256px; width: 261px; height: 56px; border-radius: 7px 0px 0px 7px; background: linear(#E0525C,#FF7A7A,90); in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#b2(left: 290px; top: 256px; width: 230px; height: 56px; border-radius: 0px 7px 7px 0px; background: #3A4766; in: {opacity:0, duration:0.5})
    p#t(cx: 50%; cy: 50%; font-size: 16px; color: #DDE4F1) 3か月以上
  p#t1(cx: 89px; cy: 128px; font-size: 33px; font-family: n; color: #FFFFFF; in: {scale:0.7, opacity:0, duration:0.45, ease:'back.out(2.2)'}) 25%
  p#t2(cx: 158px; cy: 284px; font-size: 33px; font-family: n; color: #FFFFFF; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 53%
  p#l2(left: 27px; top: 321px; font-size: 17px; color: $ink2; in: {opacity:0, duration:0.4}) 解約者
  div#leg(left: 27px; top: 383px; width: 230px; height: 20px; in: {opacity:0, duration:0.5})
    div#c1(left: 0px; cy: 50%; width: 9px; height: 9px; border-radius: 3px; background: $coral)
    p#t1(left: 16px; cy: 50%; font-size: 13px; color: $ink2; font-family: m; white-space: nowrap) 契約3か月未満
    div#c2(left: 119px; cy: 50%; width: 9px; height: 9px; border-radius: 3px; background: #3A4766)
    p#t2(left: 135px; cy: 50%; font-size: 13px; color: $ink2; font-family: m; white-space: nowrap) 3か月以上
panel#p6b(left: 648px; top: 155px; width: 557px; height: 432px; t: "解約率の推移"; s: "在籍期間別"; tk: $teal; delay: 240)
  div#grid(left: "67;67"; top: "147;253"; width: 460px; height: 1px; background: $line) ×2
  div#base(left: 67px; top: 360px; width: 460px; height: 2px; background: $line2)
  p#gl(left: "9;9;9"; top: "138;245;351"; width: 47px; text-align: right; font-size: 13px; color: $ink3; font-family: n) ×3 20%;10%;0%
  div#band(left: 87px; top: 115px; width: 413px; height: 32px; border-radius: 5px; background: #FF6B6B33; border: 1px solid #FF6B6B8C; in: {scaleX:0, opacity:0, duration:0.8, ease:'power3.out', pivot:'left'})
  p#bandl(left: 88px; top: 84px; font-size: 16px; color: $coral; white-space: nowrap; in: {y:5, opacity:0, duration:0.4}) 3か月未満 {nn}20〜23%{/}
  shape#line(path: "M120 260 L293 269 L467 289"; background: none; border: 3px solid $teal; in: draw {duration: 1})
  shape#dot.ellipse(left: "114;287;460"; top: "254;263;282"; width: "13;13;15"; height: "13;13;15"; background: $teal; border: 3px solid #131B33; in: {scale:0, duration:0.3, ease:'back.out(2.5)'}) ×3
  p#pl(left: "80;253;427"; top: "217;227;246"; width: 80px; text-align: center; font-size: 23px; font-family: n; color: $teal; in: {y:5, opacity:0, duration:0.3}) ×3 9.4%;8.5%;6.7%
  p#xl(left: "87;260;433"; top: "371;371;371"; width: 67px; text-align: center; font-size: 16px; color: $ink2; delay: 550; in: {opacity:0, duration:0.4, stagger:{each:0.06}}) ×3 7月;8月;9月
  div#leg(left: 348px; top: 61px; width: 190px; height: 20px; delay: 650; in: {opacity:0, duration:0.5})
    div#c1(left: 0px; cy: 50%; width: 19px; height: 3px; border-radius: 2px; background: $teal)
    p#t1(left: 26px; cy: 50%; font-size: 13px; color: $ink2; font-family: m; white-space: nowrap) 3か月以上
    div#c2(left: 103px; cy: 50%; width: 19px; height: 9px; border-radius: 2px; background: #FF6B6B4D; border: 1px solid #FF6B6BB3)
    p#t2(left: 129px; cy: 50%; font-size: 13px; color: $ink2; font-family: m; white-space: nowrap) 3か月未満

# s07 解約理由: 6 本の横棒を頭で一斉に (行ごとに 0.09 秒ずらし) 灰で伸ばし、上位 3 つを語で青に塗り替え順位の丸を弾ませ、残り 3 本を沈める
section#s07(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch7(n: "06"; t: "解約理由")
headline#hl7 解約理由の上位{a}3つ{/}
panel#p7(left: 75px; top: 155px; width: 1131px; height: 432px; t: "解約理由"; s: "9月・アンケート127件"; delay: 80)
  div#vg(left: "549;771;993"; top: "59;59;59"; width: 1px; height: 313px; background: $line) ×3
  p#vgl(left: "294;516;738;960"; top: "377;377;377;377"; width: 67px; text-align: center; font-size: 13px; color: $ink3; font-family: n) ×4 0%;10%;20%;30%
  div#axis(left: 325px; top: 56px; width: 2px; height: 319px; background: $line2)
  div#r(left: "0;0;0;0;0;0"; top: "64;117;171;224;277;331"; width: 1131px; height: 40px) ×6
    p#lb(left: 73px; cy: 50%; width: 233px; text-align: right; font-size: 20px; color: $ink2; white-space: nowrap; delay: "100;190;280;370;460;550"; in: {x:-8, opacity:0, duration:0.4, ease:'power3.out'}) 一時的に使わない;思い通りに作れない;料金;選択なし;クレジットが余る;本数が足りない
    div#bar(left: 327px; top: 5px; width: "622;533;467;311;222;200"; height: 29px; border-radius: 0px 5px 5px 0px; background: #4A5878; delay: "150;240;330;420;510;600"; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#vv(left: "961;872;805;650;561;539"; cy: 50%; font-size: 29px; line-height: 1.27; font-family: n; color: $ink2; delay: "550;640;730;820;910;1000"; in: {opacity:0, duration:0.4}) 28%;24%;21%;14%;10%;9%
  div#hi(left: "327;327;327"; top: "69;122;176"; width: "622;533;467"; height: 29px; border-radius: 0px 5px 5px 0px; background: linear(#4C8DF0,#8CBBFF,90); box-shadow: 0px 0px 17px #5B9DFF59; in: {scaleX:0, duration:0.55, ease:'power3.out', pivot:'left'}) ×3
  div#rk(left: "40;40;40"; top: "69;122;176"; width: 29px; height: 29px; border-radius: 99px; background: $blue; in: {scale:0, opacity:0, duration:0.4, ease:'back.out(2.4)'}) ×3
    p#t(cx: 50%; cy: 50%; font-size: 16px; font-family: n; color: #06122A) 1;2;3

# s08 期間別の理由: 左の板に 2 枚の札 (初回サイクル / 1 か月以上) を語で順に出し、理由の棒を伸ばす・右の板は音声系の icon が脈打ち 21% → 26% と「最多」の札
section#s08(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch8(n: "07"; t: "期間別の理由")
headline#hl8 解約理由は、利用期間で{a}変わる{/}
panel#p8a(left: 75px; top: 155px; width: 693px; height: 432px; t: "利用期間別の解約理由"; s: "9月"; delay: 100)
  div#cl(left: 21px; top: 64px; width: 315px; height: 301px; border-radius: 11px; border: 1px solid $line2; background: #FFFFFF06; delay: 50; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'})
    shape#dot.ellipse(left: 17px; top: 23px; width: 8px; height: 8px; background: $coral)
    p#tg(left: 33px; cy: 27px; font-size: 18px; white-space: nowrap) 初回サイクルで解約
    reason#i1(left: 17px; top: 83px; l: "思い通りに作れない"; v: "34%"; w: 238px)
    reason#i2(left: 17px; top: 189px; l: "本数が足りない"; v: "15%"; w: 105px; c: #5A6B8F; vc: $ink2)
  div#cr(left: 357px; top: 64px; width: 315px; height: 301px; border-radius: 11px; border: 1px solid $line2; background: #FFFFFF06; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'})
    shape#dot.ellipse(left: 17px; top: 23px; width: 8px; height: 8px; background: $teal)
    p#tg(left: 33px; cy: 27px; font-size: 18px; white-space: nowrap) 1か月以上使って解約
    reason#i3(left: 17px; top: 83px; l: "一時的に使わない"; v: "29%"; w: 203px)
    reason#i4(left: 17px; top: 189px; l: "クレジットが余る"; v: "17%"; w: 119px; c: #5A6B8F; vc: $ink2)
  p#na(left: 23px; top: 383px; font-size: 15px; color: $note; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) バーの長さは 0〜40% の目盛り
panel#p8b(left: 795px; top: 155px; width: 411px; height: 432px; t: "機能への不満"; tk: $amber; delay: 240)
  svg#ico(left: 24px; top: 65px; width: 56px; height: 56px; part: voice_ico; delay: 550; in: {scale:0.8, opacity:0, duration:0.45, ease:'back.out(2)'})
  p#kind(left: 91px; top: 69px; font-size: 18px; delay: 650; in: {x:-7, opacity:0, duration:0.45, ease:'power3.out'}) 音声系
  p#kind2(left: 91px; top: 97px; font-size: 14px; color: $ink3; font-family: m; white-space: nowrap; delay: 750; in: {x:-7, opacity:0, duration:0.45, ease:'power3.out'}) 読み間違い・イントネーション
  p#cap(left: 27px; top: 159px; font-size: 14px; color: $ink3; white-space: nowrap; in: {y:7, opacity:0, duration:0.45, ease:'power3.out'}) 機能への不満に占める割合
  p#from(left: 27px; top: 204px; font-size: 44px; line-height: 1.06; font-family: n; color: $ink3; in: {y:7, opacity:0, duration:0.45, ease:'power3.out'}) 21%
  shape#arr(left: 123px; top: 212px; width: 47px; height: 31px; path: arrow_r; background: $amber; border: 4px solid $amber; in: {x:-8, opacity:0, duration:0.4, ease:'power3.out'})
  p#to(left: 179px; top: 175px; font-size: 85px; line-height: 1.06; font-family: n; color: $amber; transform-origin: 0% 60%; in: {scale:0.8, opacity:0, duration:0.6, ease:'power3.out'}) 26%
  badge#most(left: 27px; top: 313px; font-size: 17px; padding: 7px 15px) 機能への不満で最多

# s09 利用行動: 100 マス (1 マス = 申請者の 1%) が中央に 10 × 10 で弾んで並び、「二極化」で左 45 (青)・中 32 (暗)・右 23 (黄) に分かれて色が付く・両端に大きな %
section#s09(stagger: {each:0}; out: {y:-11, opacity:0, duration:0.34, ease:'power2.in'})
chap#ch9(n: "08"; t: "利用行動")
headline#hl9 解約する人の行動は{a}二極化{/}している
panel#p9(left: 75px; top: 155px; width: 1131px; height: 432px; t: "解約申請者の直前30日の動画作成本数"; s: "申請者に占める割合"; delay: 80)
  div#scale(left: 860px; top: 60px; width: 200px; height: 22px; delay: 650; in: {opacity:0, duration:0.5})
    div#sq(left: 0px; cy: 50%; width: 15px; height: 15px; border-radius: 3px; background: #56627E)
    p#t(left: 23px; cy: 50%; font-size: 16px; color: #B4BED0; white-space: nowrap) 1マス ＝ 申請者の1%
  p#n45(left: 80px; top: 100px; width: 280px; text-align: center; font-size: 69px; line-height: 1.06; font-family: n; color: $blue; in: {y:12, scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.8)'}) 45%
  p#n23(left: 771px; top: 100px; width: 280px; text-align: center; font-size: 69px; line-height: 1.06; font-family: n; color: $amber; in: {y:12, scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.8)'}) 23%
  p#l45(left: 80px; top: 353px; width: 280px; text-align: center; font-size: 19px; in: {y:7, opacity:0, duration:0.45, ease:'power3.out'}) 動画 0本
  p#l23(left: 771px; top: 353px; width: 280px; text-align: center; font-size: 19px; in: {y:7, opacity:0, duration:0.45, ease:'power3.out'}) 動画 10本以上
  # hf の作り: 「それ以外」は 10 × 10 の格子の最初の位置の下端に掛かる (格子が分かれた後に出る)
  p#lmid(left: 432px; top: 336px; width: 267px; text-align: center; font-size: 17px; color: $ink2; in: {opacity:0, duration:0.5}) それ以外
# 100 マスは 3 つの ×N (0 本 45・それ以外 32・10 本以上 23)。最初の位置は 10 × 10 の列順、変種 .split が分かれた先と色 (語で 1 秒かけて補間して移る)
shape#wb(left: "503;503;503;503;503;503;503;503;503;503;531;531;531;531;531;531;531;531;531;531;559;559;559;559;559;559;559;559;559;559;587;587;587;587;587;587;587;587;587;587;615;615;615;615;615"; top: "255;283;311;339;367;395;423;451;479;507;255;283;311;339;367;395;423;451;479;507;255;283;311;339;367;395;423;451;479;507;255;283;311;339;367;395;423;451;479;507;255;283;311;339;367"; width: 23px; height: 23px; path: rect,r=0.22; background: $slate; border: none; delay: 100; in: {scale:0, duration:0.35, ease:'back.out(2)', stagger:{each:0.006}}) ×45
#wb.split(left: "172;172;172;172;172;200;200;200;200;200;228;228;228;228;228;256;256;256;256;256;284;284;284;284;284;312;312;312;312;312;340;340;340;340;340;368;368;368;368;368;396;396;396;396;396"; top: "354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;354;382;410;438;466"; background: $blue; move: 1000,power3.inOut)
shape#wm(left: "615;615;615;615;615;643;643;643;643;643;643;643;643;643;643;671;671;671;671;671;671;671;671;671;671;699;699;699;699;699;699;699"; top: "395;423;451;479;507;255;283;311;339;367;395;423;451;479;507;255;283;311;339;367;395;423;451;479;507;255;283;311;339;367;395;423"; width: 23px; height: 23px; path: rect,r=0.22; background: $slate; border: none; delay: 370; in: {scale:0, duration:0.35, ease:'back.out(2)', stagger:{each:0.006}}) ×32
#wm.split(left: "531;531;531;531;559;559;559;559;587;587;587;587;615;615;615;615;643;643;643;643;671;671;671;671;699;699;699;699;727;727;727;727"; top: "368;396;424;452;368;396;424;452;368;396;424;452;368;396;424;452;368;396;424;452;368;396;424;452;368;396;424;452;368;396;424;452"; background: #2B3550; move: 1000,power3.inOut)
shape#wa(left: "699;699;699;727;727;727;727;727;727;727;727;727;727;755;755;755;755;755;755;755;755;755;755"; top: "451;479;507;255;283;311;339;367;395;423;451;479;507;255;283;311;339;367;395;423;451;479;507"; width: 23px; height: 23px; path: rect,r=0.22; background: $slate; border: none; delay: 562; in: {scale:0, duration:0.35, ease:'back.out(2)', stagger:{each:0.006}}) ×23
#wa.split(left: "918;918;918;918;918;946;946;946;946;946;974;974;974;974;974;1002;1002;1002;1002;1002;1030;1030;1030"; top: "354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;354;382;410;438;466;410;438;466"; background: $amber; move: 1000,power3.inOut)

# s10 まとめ: 3 枚の札を頭に並べ (1 枚目だけ点灯・2 / 3 枚目は 0.36 で待機)、文の頭で 1 枚ずつ点けて番号を弾ませ中身を出す・最後に札と見出しが上へ抜ける
section#s10(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.55, ease:'power2.in'})
chap#ch10(n: "09"; t: "まとめ")
headline#hl10 まとめ：3か月のデータから言えること
card#card1(left: 75px; n: "1"; t: "解約率は11%前後で[br]横ばい"; s: "ただし9月は、週ごとに減っている"; cap: "週次の解約成立（件）　8/31週 → 9/21週"; c: $blue; g: "linear(#5B9DFF,#86B8FF,90)")
  p#t(delay: 50)
  p#s(delay: 250)
  p#cap(delay: 700)
  div#base(left: 21px; top: 350px; width: 315px; height: 2px; background: $line2)
  shape#ml(path: "M41 240 L134 273 L228 295 L321 322"; background: none; border: 3px solid $coral; in: draw {duration: 1.2})
  shape#md.ellipse(left: "35;128;222;315"; top: "234;267;289;316"; width: "11;11;11;12"; height: "11;11;11;12"; background: $coral; border: 2px solid #141D37; in: {scale:0, duration:0.3, ease:'back.out(2.5)', stagger:{each:0.36}}) ×4
  p#m63(left: 26px; top: 201px; font-size: 23px; font-family: n; in: {opacity:0, duration:0.3}) 63
  p#m26(left: 304px; top: 279px; font-size: 23px; font-family: n; in: {opacity:0, duration:0.3}) 26
card#card2(left: 461px; n: "2"; t: "勝負は[br]最初の3か月"; s: "3か月未満の解約率が下がらない"; cap: "解約の53%が契約3か月未満"; c: $coral; g: "linear(#E0525C,#FF7A7A,90)"; opacity: 0.36; delay: 140)
  p#b20(left: 21px; top: 207px; font-size: 80px; line-height: 1.08; font-family: n; color: $coral; white-space: nowrap; transform-origin: 0% 50%; in: {scale:0.85, opacity:0, duration:0.55, ease:'power3.out'}) 20%{dai}台{/}
  p#b20s(left: 24px; top: 300px; font-size: 16px; color: $ink2; white-space: nowrap; in: {y:7, opacity:0, duration:0.45, ease:'power3.out'}) 3か月未満の解約率（7〜9月）
  p#imp(left: 24px; top: 331px; font-size: 15px; color: $teal; white-space: nowrap; in: {y:7, opacity:0, duration:0.45, ease:'power3.out'}) 3か月以上は {nn}9.4% → 6.7%{/} に改善
card#card3(left: 848px; n: "3"; t: "まず直す所"; s: "初回サイクルと音声の品質"; cap: "9月の解約アンケートより"; c: $amber; g: "linear(#F4B942,#FFD27A,90)"; opacity: 0.36; delay: 260)
  div#it1(left: 21px; top: 200px; width: 315px; height: 69px; border-radius: 9px; border: 1px solid $line2; background: #FFFFFF08; in: {x:-11, opacity:0, duration:0.5, ease:'power3.out'})
    svg#ic(left: 12px; top: 15px; width: 40px; height: 40px; part: wand_ico)
    p#it(left: 63px; top: 11px; font-size: 17px; white-space: nowrap) 思い通りに作れない
    p#is(left: 63px; top: 39px; font-size: 13px; color: $ink3; font-family: m; white-space: nowrap) 初回サイクルの解約理由で {nn}34%{/}
  div#it2(left: 21px; top: 283px; width: 315px; height: 69px; border-radius: 9px; border: 1px solid $line2; background: #FFFFFF08; in: {x:-11, opacity:0, duration:0.5, ease:'power3.out'})
    svg#ic(left: 12px; top: 15px; width: 40px; height: 40px; part: bubble_ico)
    p#it(left: 63px; top: 11px; font-size: 17px; white-space: nowrap) 音声の読み間違い
    p#is(left: 63px; top: 39px; font-size: 13px; color: $ink3; font-family: m; white-space: nowrap) 機能への不満で最多{nn}（26%）{/}

# outro 締めの題: 上端の帯を抜き、題の絵が溶けて戻り、小札 → 2 行 → 下線 → 注記を組んで暗転
section#outro(stagger: {each:0})
img#out_bg(inset: 0; content: @title_img; main: kb {scale: [1, 1.04]}; in: {opacity:0, duration:1.6, ease:'power2.inOut'})
div#ok(left: 100px; top: 237px; width: 600px; height: 25px; delay: 400; in: {x:-13, opacity:0, duration:0.6, ease:'power3.out'})
  div#ln(left: 0px; cy: 50%; width: 29px; height: 2px; background: $teal)
  p#t(left: 40px; cy: 50%; font-size: 16px; letter-spacing: 0.14em; color: $teal; white-space: nowrap) 解約分析レポート ｜ まとめ
p#ot1(left: 100px; top: 266px; font-size: 44px; font-family: h; line-height: 1.27; white-space: nowrap; delay: 550; in: {y:16, opacity:0, duration:0.7, ease:'power3.out'}) 動画生成サービスの解約、
p#ot2(left: 100px; top: 322px; font-size: 44px; font-family: h; line-height: 1.27; white-space: nowrap; delay: 700; in: {y:16, opacity:0, duration:0.7, ease:'power3.out'}) 勝負は{a}最初の3か月{/}
div#ob(left: 100px; top: 394px; width: 307px; height: 3px; border-radius: 2px; background: linear($teal,$blue,90); delay: 900; in: {scaleX:0, duration:0.8, ease:'power3.inOut', pivot:'left'})
p#om(left: 100px; top: 416px; font-size: 15px; letter-spacing: 0.06em; color: $ink2; font-family: m; white-space: nowrap; delay: 1150; in: {y:7, opacity:0, duration:0.6, ease:'power3.out'}) 対象　有料契約者 ｜ 期間　7〜9月 ｜ 社内共有
```

```timeline.txt
#v2
cast n = "落ち着いた30代女性のナレーター、明瞭で聞き取りやすい声、社内の分析報告らしく淡々と丁寧に読む"
silence head=0 tail=300
# 切替は書かない (場面は section の out で上へ抜けて消え、次の場面は境目から組み上がる・地と上端の帯は常設)。場面の境目の 0.47 秒前に風切り (前の cut の末尾の無音の間)

*** s01
[>#subtitle]
bgm music
@n: [silence:0.9s][♪air -2.7dB -750][♪deep -4.4dB -280][♪chime -5.4dB +200]この{b}3{/}か月の解約データから、[|]分かったことをまとめます。[silence:0.13s][♪swoosh -3.5dB][silence:0.47s]

*** s02
@n: [silence:0.15s][♪pop -2.7dB +50]有料契約者は、[|][>#p2a.k1 -450][>#p2a.k1.bar -300][>#p2a.k1.n -150][♪chime -3.5dB +50]{b}1,776{/}人から[>#p2a.arrow -750][>#p2a.k2 -500][>#p2a.k2.bar -350][>#p2a.k2.n -150][♪chime -1.9dB +50][>#p2a.na +600]{b}1,682{/}人へ。
@: [!#p2b.core to,{opacity:1, duration:0.45} -350][!#p2b.core punch,1.06,duration=600 -350][!#p2b.node_in to,{opacity:1, duration:0.45} -100][>#p2b.node_in.v +50][>#p2b.node_in.u +130][>#p2b.a1 +350][>#p2b.fi[1] +900][!#p2b.fi[1] to,{x:26, duration:0.9, ease:'none', repeat:-1} +900][>#p2b.fi[2] +1200][!#p2b.fi[2] to,{x:26, duration:0.9, ease:'none', repeat:-1} +1200][>#p2b.fi[3] +1500][!#p2b.fi[3] to,{x:26, duration:0.9, ease:'none', repeat:-1} +1500][♪sub -4.4dB +50]毎月の新規課金は、解約で[!#p2b.node_out to,{opacity:1, duration:0.45} -450][>#p2b.a2 -200][>#p2b.node_out.r -100][♪sub -4.4dB -100][>#p2b.fo[1] +400][!#p2b.fo[1] to,{x:37, duration:0.9, ease:'none', repeat:-1} +400][>#p2b.fo[2] +700][!#p2b.fo[2] to,{x:37, duration:0.9, ease:'none', repeat:-1} +700][>#p2b.fo[3] +1000][!#p2b.fo[3] to,{x:37, duration:0.9, ease:'none', repeat:-1} +1000]相殺され、[|][>#p2b.res -50][♪deep -3.5dB +50][♪pop -1.9dB +70][>#p2b.res_sub +350][!#p2b.res glow,#F4B94261,blur=47 +500][=#p2b.res +1000]純増はゼロです。[silence:0.38s][♪swoosh -3.5dB][silence:0.47s]

*** s03
@n: [silence:0.15s]解約率は、[>#p3a.c1 -150][>#p3a.x[1] -150][>#p3a.v[1] +250][♪pop -3.5dB]{b}7{/}月の[>#p3a.c2 -90][>#p3a.x[2] -90][>#p3a.v[2] +310][♪pop -4.4dB -90]{b}13.2%{/}から、[|][>#p3a.c3 -150][>#p3a.x[3] -150][>#p3a.v[3] +250][♪pop -2.7dB]{b}9{/}月は[♪chime -2.7dB +100]{b}10.8%{/}。
@: [!#p3a.c1 to,{opacity:0.45, duration:0.5} -50][!#p3a.c2 to,{opacity:0.45, duration:0.5} -50][!#p3a.v[1] to,{opacity:0.45, duration:0.5} -50][!#p3a.v[2] to,{opacity:0.45, duration:0.5} -50][!#p3a.x[1] to,{opacity:0.45, duration:0.5} -50][!#p3a.x[2] to,{opacity:0.45, duration:0.5} -50][!#p3a.c3.b to,{y:-3, fill:'#F0B744', duration:0.5, ease:'power2.inOut'} -50][>#p3a.leg +100][>#p3b.kv -200][♪sub -5.4dB -50]内訳は、自発的な解約[>#p3a.lab_a -100][>#p3b.sba -200][!#p3b.r[1] to,{opacity:1, duration:0.4} -150][>#p3b.r[1].pv -50][♪pop -3.5dB]{b}8.5%{/}、[|]決済失敗[>#p3a.lab_b -100][>#p3b.sbb -200][!#p3b.r[2] to,{opacity:1, duration:0.4} -150][>#p3b.r[2].pv -50][>#p3b.nb +400][♪pop -3.5dB]{b}2.3%{/}です。[silence:0.38s][♪swoosh -3.5dB][silence:0.47s]

*** s04
@n: [silence:0.15s]ただ{b}9{/}月は、週ごとの解約成立が、[|][>#p4a.area -150][>#p4a.line -150][>#p4a.dot[1] -200][>#p4a.vl[1] -150][>#p4a.dot[2] +430][>#p4a.vl[2] +480][♪blip -3.5dB -250]{b}63{/}件から[>#p4a.dot[3] -380][>#p4a.vl[3] -330][>#p4a.dot[4] +250][>#p4a.vl[4] +300][♪chime -2.7dB +100][>#p4a.call +350]{b}26{/}件まで減りました。
@: [!#p4a to,{opacity:0.8, duration:0.6} -300][♪pop -3.5dB]申請も、[>#p4b.b1 -300][>#p4b.bv1 +200][>#p4b.b2 +250][>#p4b.b2x +800][>#p4b.bv2 +750][♪pop -4.4dB]{b}7{/}月と{b}8{/}月の平均より[>#p4b.ref -350][>#p4b.gap -200][>#p4b.badge -50][♪tick -1.9dB][♪pop -4.4dB +935]{b}2{/}割少ない水準です。[silence:0.73s][♪swoosh -3.5dB][silence:0.47s]

*** s05
@n: [silence:0.15s]在籍期間で見ると、[>#p5.r[1] -250][♪pop -3.5dB]{b}1{/}か月未満は[>#p5.r[1].bar -550][>#p5.r[1].vv -50]{b}29%{/}、[|][>#p5.r[2] -250][>#p5.tag_u +500][♪pop -3.5dB]{b}1{/}から{b}3{/}か月は[>#p5.r[2].bar -550][>#p5.r[2].vv -50]{b}19%{/}。
@: [>#p5.dv -400][>#p5.r[3] -150][>#p5.r[3].bar -100][>#p5.r[3].vv +400][>#p5.r[4] +50][>#p5.r[4].bar +100][>#p5.r[4].vv +600][>#p5.r[5] +250][>#p5.r[5].bar +300][>#p5.r[5].vv +800][>#p5.tag_o +400][♪pop -4.4dB]{b}3{/}か月以上は、[>#p5.br -350][>#p5.hk -50][♪tick -2.7dB]ひとケタ台に下がります。[silence:0.33s][♪swoosh -3.5dB][silence:0.47s]

*** s06
@n: [silence:0.15s]{b}3{/}か月未満の人は、母数の[>#p6a.l1 -800][>#p6a.a1 -350][>#p6a.b1 -100][>#p6a.t1 -50][♪pop -3.5dB]{b}25%{/}なのに、[|]解約の[>#p6a.a2 -400][>#p6a.l2 -400][>#p6a.b2 -100][>#p6a.t2 -50][>#p6a.rib +100][>#p6a.leg +500][♪chime -1.9dB +50][♪deep -6.6dB +50]{b}53%{/}を占めます。
@: [!#p6a to,{opacity:0.8, duration:0.6} -300]{b}3{/}か月以上は[>#p6b.line -300][>#p6b.dot[1] -300][>#p6b.pl[1] -250][>#p6b.dot[2] +180][>#p6b.pl[2] +230][>#p6b.dot[3] +660][>#p6b.pl[3] +710][♪blip -4.4dB -200]改善していますが、[|][>#p6b.band -100][♪pop -4.4dB]{b}3{/}か月未満は[>#p6b.bandl -200]{b}20%{/}台のままです。[silence:0.68s][♪swoosh -3.5dB][silence:0.47s]

*** s07
@n: [silence:0.15s]解約理由の上位は、[>#p7.hi[1] -150][>#p7.rk[1] -100][!#p7.r[1].lb recolor,$ink,duration=300 -100][!#p7.r[1].vv recolor,$ink,duration=300 -100][♪pop -3.5dB]一時的に使わない、[|][>#p7.hi[2] -150][>#p7.rk[2] -100][!#p7.r[2].lb recolor,$ink,duration=300 -100][!#p7.r[2].vv recolor,$ink,duration=300 -100][♪pop -3.5dB]思い通りに作れない、[>#p7.hi[3] -150][>#p7.rk[3] -100][!#p7.r[3].lb recolor,$ink,duration=300 -100][!#p7.r[3].vv recolor,$ink,duration=300 -100][♪pop -3.5dB]料金の[!#p7.r[4] to,{opacity:0.55, duration:0.5} -200][!#p7.r[5] to,{opacity:0.55, duration:0.5} -200][!#p7.r[6] to,{opacity:0.55, duration:0.5} -200]{b}3{/}つです。[silence:0.63s][♪swoosh -3.5dB][silence:0.47s]

*** s08
@n: [silence:0.15s][♪pop -4.4dB +100]初回サイクルでの解約は、[|]思い通りに作れないが[>#p8a.cl.i1 -700][>#p8a.cl.i1.bar -600][>#p8a.cl.i1.vv -250][>#p8a.cl.i2 +150][>#p8a.cl.i2.bar +250][>#p8a.cl.i2.vv +600][♪chime -2.7dB +50]{b}34%{/}。
@: [>#p8a.cr -450]{b}1{/}か月以上使った人では、[|][>#p8a.cr.i3 -450][>#p8a.cr.i3.bar -350][>#p8a.cr.i3.vv][♪pop -4.4dB -100]一時的と[>#p8a.cr.i4 -450][>#p8a.cr.i4.bar -350][>#p8a.cr.i4.vv][>#p8a.na +600][♪pop -4.4dB -100]クレジットの余りが目立ちます。
@: [!#p8a to,{opacity:0.8, duration:0.6} -300][♪sub -5.4dB -50]機能への不満では、[|]読み間違いなど[!#p8b.ico punch,1.12,duration=600 -300][>#p8b.cap +100][>#p8b.from +180]音声系が[>#p8b.arr -450][>#p8b.to -350][♪chime -1.9dB +50]{b}26%{/}に増え、[|][>#p8b.most -50][♪deep -5.4dB]最多になりました。[silence:0.53s][♪swoosh -3.5dB][silence:0.47s]

*** s09
@n: [silence:0.15s]行動は[!#wb[*] .split -350][!#wm[*] .split -350][!#wa[*] .split -350][♪sub -3.5dB -100]二極化しています。
@: 申請者の[>#p9.n45 -200][>#p9.l45 +500][>#p9.lmid +900][♪chime -2.7dB +50]{b}45%{/}は、直前{b}30{/}日に{b}1{/}本も作らず、[|][>#p9.n23 -200][♪chime -2.7dB +50]{b}23%{/}は[>#p9.l23 -200]{b}10{/}本以上作っていました。[silence:0.43s][♪swoosh -3.5dB][silence:0.47s]

*** s10
@n: [silence:0.15s][♪click -1.9dB]解約率は{b}11%{/}前後で横ばいですが、[|][>#card1.ml -300][>#card1.md -300][>#card1.m63 -200][>#card1.m26 +900]{b}9{/}月は週ごとに減っています。
@: [!#card2 to,{opacity:1, duration:0.45, ease:'power2.out'} -300][!#card2.no punch,1.18,duration=440 -300][>#card2.t -250][>#card2.s -50][>#card2.cap +400][>#card2.b20 +500][>#card2.b20s +1000][>#card2.imp +1250][♪click -1.9dB]勝負は、{b}20%{/}台のままの最初の{b}3{/}か月。
@: [!#card3 to,{opacity:1, duration:0.45, ease:'power2.out'} -300][!#card3.no punch,1.18,duration=440 -300][>#card3.t -250][>#card3.s -50][>#card3.cap +400][>#card3.it1 +900][♪click -1.9dB]まず直すのは、[|]初回サイクルで思い通りに作れないことと、[|][>#card3.it2 -250]音声の読み間違いです。[silence:0.4s][♪air -5.4dB][silence:0.15s]

*** outro
@n: [<#hdr][<#prog][♪deep -6.6dB][silence:2.6s]
fade out,900
```

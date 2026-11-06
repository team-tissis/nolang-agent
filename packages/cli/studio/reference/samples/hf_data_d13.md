# data · office-electricity (hf 全力版の全量の写し — オフィスの電気代、どこに消えている？・明るい格子の地に白い板と図を場面ごとに組む 9 場面のデータ図解) — canvas 1920x1080

見せる作り: 全編の地 (淡い緑灰 + 点の格子 + 角の 2 つの光) と下端の進行線・2 場面目から常設の上端の帯 (社名の札 + 7 章の札と場面の頭で滑って伸びる緑の指示子)・場面 = 番号札つきの小見出し + 題 + 白い板 (板の def)・数字の語で動く図 (数え上がる 4 枚の数字の札・12 本の月の棒を語で塗り最少の破線とかぎと倍率の札・時計回りに描く 4 弧のドーナツと太る空調の弧・語で伸びるピークの横棒 4 本と注記の板・円で開く紺の夜の場面で 3 枚のガラスの板から内訳の 3 色の帯とかぎへ組み替え・3 枚の対策の札・滝の図と合計の板)・まとめの 3 行を語で入れ、締めの間で 1 と 3 を沈めて 2 を大きく・字幕は濃い半透明の札・音の層 (場面の境のシュワッ + 語に結んだ電子のチャイム 30 余)

```design.txt
#v2
# 学ぶ作り: 明るい data の design system を根に 1 回 (palette・書体 4・場面の見出し sec / title の def・白い板 card の def・板の題と注記の def) → 場面は板の中の図だけ
# 常設の層: 全編の地 (淡い緑灰 + 点の格子 + 角の 2 つの光)・下端の進行線・2 場面目から sticky の上端の帯 (社名の札 + 7 章の札と、場面の頭で滑る緑の指示子)
# 図は数字の語と同時に動く: 12 本の月の棒 (語で 8 月と 1 月を塗る・最少の線とかぎと倍率の札)・4 弧のドーナツ (時計回りに描く)・ピークの横棒 4 本・夜の場面は円で開く紺の地と 2 段の板 (31% の帯 → 内訳の 3 色の帯とかぎ)・3 枚の対策の札・滝の図と合計の板・まとめの 3 行
# hf d13 office-electricity (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の退場は section の out (少し上へ抜けて消える)・切替は書かない (地は常設なので素の切替)
canvas 1920x1080 bg=#F3F6F5
theme light
palette ink=#13222B ink2=#3F5058 muted=#56656B line=#DCE4E2 grid=#E4EBE9 green=#0E9F6E green_d=#07704D green_l=#E3F4EC ac=#2F6FDB oa=#7A5AF8 lighting=#F0A92E other=#9AA8AE summer=#F07C3E winter=#2FA4E7 base=#C9D6D2 avg=#7FAE9C navy=#0D1936 mint=#5FE3B5 fixed=#8A9AC0 standby=#A98CFF forgot=#FFC24B
font "清潔で中立的な太字のゴシック体 (Bold)、均整の取れたかなと漢字と端正な欧文、明快で読みやすい"
fonts n="数字が力強くくっきりした極太の角ゴシック体、データの大きな数字向け"
fonts h="清潔で中立的な極太のゴシック体 (Black)、均整の取れたかなと漢字と端正な欧文、明快で読みやすい見出し向け"
fonts m="標準の太さの角ゴシック体、字幕向けで読みやすい"
sfx off
# hf の作り: 場面の見出しは台詞より先に結論を出す (見出し → 図 → 台詞が数字を読む)
lint off=spoiler
# hf の作り: 板の中の目盛り・凡例・注記・補足は 12〜15 px (1080 の 19〜22 px)
lint off=small_text
# hf の作り: 図の色 (半透明の地・薄い縁・グラデの端) は場面ごとに直書き
lint off=palette_drift
# hf の作り: 図の場面 (月別・用途・ピーク・合計・まとめ) は絵を置かず白い板の図だけ・夜の場面は 1 枚の等角図を 17 秒見せて板を替える
lint off=text_only_cut,same_picture
# hf の作り: 合計の場面の題は結論の全文を場面の頭に出す・題の出典行と締めの出典の注記は短く出る
lint off=all_at_once,flash_text
art "清潔感のある現代的なフラットのベクターイラスト、やわらかいグラデーションと控えめな影、丸みのある親しみやすい形、企業のインフォグラフィック調、輪郭がくっきり"
prompt_tail "文字・数字・ロゴ・透かしは一切入れない"
sound title = "ソナーのような澄んだ高いサイン波の単音、深い残響のある企業向けの合図"
sound whoosh = "高域の空気を切る短いデジタルのシュッという音、深い残響"
sound swish = "高域のノイズが短く流れるシュワッという場面転換の音、深い残響"
sound multi = "明るく澄んだ電子チャイムの短い連打、軽いディレイ"
sound ping = "明るく前向きな柔らかいシンセのチャイムの単音"
sound rise = "低い音から高い音へ上がる明るい電子のチャイム、ポップな立ち上がり"
sound pop = "短く明るい電子のチャイムの単音、控えめで軽いディレイ"
sound chime = "高く澄んだ金属のベルの単音、ピーンと響く"
sound soft = "ゆっくり立ち上がる柔らかなサイン波の短い音"
sound low = "低く温かな 2 音のシンセのベル"
run em { color: $green_d }
run uem { color: $green_d; marker: #0E9F6E38,22% }
run mi { color: $mint }
run u { font-size: 0.65em }
run nn { font-family: n }
run pc { font-size: 0.56em }
run s { font-size: 0.67em; font-family: m }
run s2 { font-size: 0.63em; font-family: m }
run s3 { font-size: 0.48em; font-family: m; color: $ink2 }
run s4 { font-size: 0.61em; font-family: m; color: #D9E2F5 }
# 章の札の切替: 緑の指示子が次の章札へ滑って章札の幅に伸び、前の章の文字を灰に・新しい章の文字を白に
cue chap(a, b, l, w) = [!#chap.ind to,{left: {l}, w: {w}, duration: .5, ease: 'power3.inOut'}][!#a recolor,$muted {duration: .3} +50ms][!#b recolor,#FFFFFF {duration: .3} +200ms]
svg leaf = """<svg viewBox="0 0 24 24"><path d="M20 4C11 4 5 8.5 5 15c0 1.6.4 3 1 4.2C8 14 12 10.5 16 9c-3.5 2.5-6.6 6-8.3 10.6C9 20.5 10.5 21 12 21c6 0 8.5-6.5 8-17z" fill="#FFFFFF"/></svg>"""
p { color: $ink }
# 字幕: 下端中央の濃い半透明の札・白の中字・句末の約物は外す・札 = 文 ([|] で句に切る)
subtitle.hug(bottom: 42px; font-size: 38px; line-height: 1.35; letter-spacing: 0.03em; color: #FFFFFF; font-family: m; background: #0F1C24DB; border-radius: 14px; padding: 12px 36px 14px 36px; unit: sentence; strip: 、。; lead: 60ms; tail: 250ms; hold: off; in: {y:8, opacity:0, duration:0.18, ease:'power1.out'})
# 曲: 声の無い頭と締めだけ前に出し、台詞の間は下げる
bgm#music(keys: "0:+6|500ms:+6|1000ms:0|end-2.3s:0|end-1.7s:+6"; fade: 500,1900) シンコペーションの効いた軽快なピアノのリズムに一定の電子ビートと温かいシンセパッドを重ねた、明るくモダンで主張しすぎない企業の解説向けの曲

# 場面の見出し: 緑の番号札 + 小見出し (上) と 37 px の題 (下)・場面の頭に下から入る
def sec(n, l, c=$green_d, nc=#FFFFFF) = div(left: 120px; top: 112px; width: 900px; height: 33px; delay: 60ms; in: {y:22, opacity:0, duration:0.6, ease:'power3.out'})
  p#n(left: 0px; cy: 50%; font-size: 22px; font-family: n; color: {nc}; background: {c}; border-radius: 8px; padding: 3px 10px; content: {n})
  p#l(left: .n.right+14; cy: 50%; font-size: 24px; letter-spacing: 0.08em; color: {c}; content: {l})
def title(t, c=$ink) = p(left: 120px; cy: 184px; font-size: 56px; line-height: 1.25; letter-spacing: 0.01em; color: {c}; delay: 160ms; in: {y:22, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-10, opacity:0, duration:0.3, ease:'power2.in'}; content: {t})
# 白い板 (細い縁 + 柔らかい影)・場面の頭に下から入る
def card = div(background: #FFFFFF; border: 2px solid #E0E8E5; border-radius: 24px; box-shadow: 0px 14px 34px #13222B12; delay: 140ms; in: {y:36, opacity:0, duration:0.6, ease:'power3.out'})
def ctitle(t) = p(left: 40px; cy: 48px; font-size: 30px; content: {t})
def cnote(t) = p(left: 40px; cy: 87px; font-size: 20px; color: $muted; font-family: m; content: {t})

# 全編の地 (根): 淡い緑灰に点の格子・右上に緑・左下に青の淡い光
div#bg_base(inset: 0; background: #F3F6F5; pattern: dots,21,#13222B12,0.8; z-index: back; in: none)
div#glow1(inset: 0; background: radial(#0E9F6E1A,#0E9F6E00@34%,88%,8%); z-index: back; in: none)
div#glow2(inset: 0; background: radial(#2FA4E717,#2FA4E700@32%,6%,96%); z-index: back; in: none)
# 下端の進行線 (全編で左から伸びる)
div#prog_track(left: 0px; top: 1074px; width: 1920px; height: 6px; background: #13222B14; z-index: front; in: none)
progress#prog(left: 0px; top: 1074px; width: 1920px; height: 6px; background: $green; until: end; z-index: front; overlap: prog_track)

# s1 題: 右に昼のオフィスの等角図が浮き上がり、左に小札 → 2 行の題 (「消えている」の下に緑の帯) → 出典 → 3 つの数字の札
section#s1(stagger: {each:0}; out: {y:-30, opacity:0, duration:0.3, ease:'power2.in'})
div#s1_b1(left: 1010px; top: 150px; width: 820px; height: 820px; border-radius: 1498px; background: radial(#0E9F6E29,#0E9F6E00@68%); in: none)
div#s1_b2(left: 1240px; top: 90px; width: 520px; height: 520px; border-radius: 1498px; background: radial(#2FA4E724,#2FA4E700@68%); in: none)
img#s1_hero(left: 930px; top: 230px; width: 960px; height: 640px; object-fit: contain; main: kb {scale: [1, 1.05]}; delay: 100ms; in: {y:60, scale:0.96, opacity:0, duration:1, ease:'power3.out'}) [transparent]明るい現代的なオープンオフィスの 1 フロアを斜め上 30 度から見下ろした等角図の切り抜き。白い机が並びモニターとノートPC、天井の LED 照明パネル、壁掛けのエアコン、複合機、小さなサーバーラック、観葉植物、昼の光が入る大きな窓。顔のない小さな人が働いている。宙に浮いた 1 枚のフロアのブロックで、枠いっぱいに大きく描く。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
div#s1_kicker(left: 120px; top: 250px; width: 360px; height: 46px; border-radius: 148px; background: $green_l; delay: 150ms; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  icon#i(left: 14px; cy: 50%; font-size: 28px; name: lightning; weight: fill; color: $green_d)
  p#t(left: 50px; cy: 50%; font-size: 26px; letter-spacing: 0.06em; color: $green_d) 社内向け 電力データ分析
p#s1_l1(left: 120px; top: 336px; font-size: 92px; font-family: h; line-height: 1.22; letter-spacing: 0.01em; delay: 300ms; in: {y:40, opacity:0, duration:0.7, ease:'power3.out'}) オフィスの電気代、
p#s1_l2(left: 120px; top: 448px; font-size: 92px; font-family: h; line-height: 1.22; letter-spacing: 0.01em; delay: 500ms; in: {y:40, opacity:0, duration:0.7, ease:'power3.out'}) どこに{uem}消えている{/}？
p#s1_sub(left: 124px; cy: 609px; font-size: 28px; color: $ink2; font-family: m; delay: 1000ms; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}) 株式会社ミドリノ設計　昨年度（4月〜3月）の電力データより
div#s1_chip(left: "120;321;561"; top: 700px; width: "183;222;279"; height: 70px; border-radius: 16px; background: #FFFFFF; border: 2px solid #DFE7E4; box-shadow: 0px 8px 22px #13222B0F; delay: 1300ms; in: {y:20, opacity:0, duration:0.6, ease:'power3.out', stagger:{each:0.12}}) ×3
  p#k(left: 24px; cy: 50%; font-size: 20px; color: $muted; font-family: m) 社員;延床;30分値
  p#v(left: .k.right+10; cy: 50%; font-size: 34px; font-family: n; letter-spacing: -0.02em) 200{u}人{/};2,400{u}m²{/};17,520{u}コマ{/}

# s2 分析の概要: 上端の帯が降りる・左の板にメーターの絵と 3 行・「分析」で 3 枚の数字の札が数え上がり、「1171」で緑の主役の札が数えて光る
section#s2(stagger: {each:0}; out: {y:-21, opacity:0, duration:0.3, ease:'power2.in'})
# 上端の帯 (sticky・最後まで): 左の社名の札・右の 7 章の札 (緑の指示子が場面の頭で滑り、文字が白に替わる)
div#brand.sticky(left: 120px; top: 34px; width: 420px; height: 50px; border-radius: 26px; background: #FFFFFFF0; border: 2px solid #DFE7E4; z-index: front; delay: 50ms; in: {y:-20, opacity:0, duration:0.6, ease:'power3.out'})
  div#logo(left: 9px; cy: 50%; width: 34px; height: 34px; border-radius: 148px; background: $green)
    svg#leaf(cx: 50%; cy: 50%; width: 20px; height: 20px; part: leaf)
  p#b(left: 56px; cy: 50%; font-size: 20px) ミドリノ設計
  div#sep(left: .b.right+12; cy: 50%; width: 2px; height: 20px; background: #CFD9D6)
  p#s(left: .sep.right+12; cy: 50%; font-size: 20px; color: $ink2; font-family: m) オフィス電力レポート
# hf の作り: 指示子が次の章へ滑る間、前の章の文字を灰に戻す (滑り終えるまで灰の字が緑の上に一瞬乗る — check の low_contrast)
div#chap.sticky(left: 890px; top: 34px; width: 910px; height: 50px; border-radius: 26px; background: #FFFFFFF0; border: 2px solid #DFE7E4; z-index: front; delay: 130ms; in: {y:-20, opacity:0, duration:0.6, ease:'power3.out'})
  div#ind(left: 4px; top: 4px; width: 112px; height: 38px; border-radius: 20px; background: $green_d)
  p#ch(left: "5;122;237;353;488;659;776"; cy: 50%; width: "113;113;113;131;168;113;131"; font-size: 18px; text-align: center; color: "#FFFFFF;$muted;$muted;$muted;$muted;$muted;$muted") ×7 01 概要;02 月別;03 用途;04 ピーク;05 夜間・休日;06 対策;07 まとめ
sec#s2_sec(n: "01"; l: "分析の概要")
title#s2_title 1年分の30分値で、電気の行き先を追う
card#s2_method(left: 120px; top: 268px; width: 620px; height: 632px; delay: 160ms)
  img#pic(left: 190px; top: 22px; width: 240px; height: 240px; object-fit: contain; main: sine {y: -8, period: 3.4}) [transparent]白い四角いスマートメーターの箱 1 台、小さな空の液晶と無線の印、その横に抽象的な棒グラフを挟んだクリップボード。斜め前から見た 3/4 の構図、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#row(left: 40px; top: "281;389;497"; width: 540px; height: 108px; delay: 800ms; in: {y:16, opacity:0, duration:0.6, ease:'power3.out', stagger:{each:0.18}}) ×3
    div#ln(left: 0px; top: 0px; width: 540px; height: 2px; background: $line)
    p#k(left: 0px; cy: 40px; font-size: 22px; color: $green_d) データ;突き合わせ;対象
    p#v(left: 152px; cy: 39px; font-size: 26px; font-family: m) スマートメーターの30分値;フロア別・系統別の子メーター;社員200人・延床2,400m²
    p#s(left: 152px; cy: 72px; font-size: 20px; color: $muted; font-family: m) 30分ごと × 1年分 ＝ 17,520コマ;どの用途・時間帯で使ったかを特定;期間：昨年度（4月〜3月）
# 数字の札 (題 + 数え上がる数字 + 単位 + 注記)
def kpi(l, v, u, f) = div(width: 500px; height: 306px; background: #FFFFFF; border: 2px solid #E0E8E5; border-radius: 24px; box-shadow: 0px 14px 34px #13222B12; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  p#l(left: 36px; cy: 50px; font-size: 26px; color: $ink2; content: {l})
  p#v(left: 34px; cy: 136px; font-size: 90px; line-height: 1; font-family: n; letter-spacing: -0.02em; content: {v})
  p#u(left: .v.right+10; cy: 159px; font-size: 32px; color: $ink2; content: {u})
  p#f(left: 36px; cy: 261px; font-size: 21px; color: $muted; font-family: m; content: {f})
kpi#s2_k1(left: 780px; top: 268px; l: "年間の使用量"; v: "[count:384,000 start=0 ms=1200ms delay=100ms]"; u: "kWh"; f: "スマートメーター30分値の年間合計")
kpi#s2_k3(left: 780px; top: 594px; l: "平均単価"; v: "[count:30.5 start=0 ms=1000ms delay=240ms]"; u: "円/kWh"; f: "電気代 ÷ 使用量")
kpi#s2_k4(left: 1300px; top: 594px; l: "社員1人あたり"; v: "[count:5.9 start=0 ms=1000ms delay=280ms]"; u: "万円/年"; f: "1,171万円 ÷ 200人")
# 主役の札: 緑の縁と縦の淡いグラデ・左端の緑の短い棒・数字は緑
kpi#s2_k2(left: 1300px; top: 268px; l: "年間の電気代"; v: "[count:1,171 start=0 ms=1100ms delay=100ms]"; u: "万円"; f: "昨年度（4月〜3月）の実績"; background: linear(#F2FBF7,#FFFFFF@60%,180); border: 3px solid $green; in: {y:30, scale:0.96, opacity:0, duration:0.6, ease:'power3.out'})
  p#v(color: $green_d)
  div#bar(left: 0px; top: 30px; width: 8px; height: 40px; border-radius: 0px 6px 6px 0px; background: $green)

# s3 月別: 12 本の灰の棒が左から順に伸び、語で 8 月を橙・1 月を青に塗って値の札・「5月」で最少の札と破線・「1.7」でかぎと倍率の黒札
section#s3(stagger: {each:0}; out: {y:-21, opacity:0, duration:0.3, ease:'power2.in'})
sec#s3_sec(n: "02"; l: "月別の使用量")
title#s3_title 山は{em}夏（8月）{/}と{em}冬（1月）{/}の2つ
card#s3_card(left: 120px; top: 262px; width: 1680px; height: 640px)
  ctitle#t 月別の電力使用量
  cnote#n 単位：千kWh　※スマートメーター30分値の月合計（年間 384,000 kWh）
  # 凡例 (右上・色の四角 + 語)
  div#leg(left: "1013;1218;1430"; cy: 48px; width: "195;195;143"; height: 22px) ×3
    div#sw(left: 0px; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: "$summer;$winter;$base")
    p#t(left: 27px; cy: 50%; font-size: 20px; color: $ink2; font-family: m) 夏のピーク（8月）;冬のピーク（1月）;その他の月
  # 目盛り (0〜40 千kWh = 213 px) と月の札
  div#gl(left: 120px; top: "511.0;431.0;351;271.0;190.9"; width: 1520px; height: 2px; background: $grid) ×5
  div#bar(left: "145.4;272.0;398.7;525.3;652.0;778.7;905.2;1032;1158.6;1285.3;1411.9;1538.6"; top: "304.0;308.9;273.6;203.2;172.8;239.2;294.5;300;264;227.2;238.4;246.5"; width: 76px; height: "208.0;203.2;238.4;308.9;339.1;272.9;217.6;212.0;248.0;284.9;273.6;265.6"; border-radius: 6px; background: $base; delay: 550ms; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom', stagger:{each:0.06}}) ×12
  p#gn(left: 50px; cy: "512;432;353;272;192"; width: 56px; text-align: right; font-size: 20px; color: $muted; font-family: m) ×5 0;10;20;30;40
  p#mo(left: "133.4;260.0;386.7;513.3;640.0;766.7;893.4;1020;1146.6;1273.3;1399.9;1526.7"; cy: 540px; width: 100px; text-align: center; font-size: 22px; color: $ink2; font-family: m) ×12 4月;5月;6月;7月;8月;9月;10月;11月;12月;1月;2月;3月
  # 季節の帯 (軸の下の色の線 + 語)
  div#season(left: "506.0;1139.4"; top: 566px; width: "368.0;494.7"; height: 36px) ×2
    div#ln(left: 0px; top: 0px; width: 100%; height: 4px; background: "$summer;$winter")
    p#t(cx: 50%; cy: 21px; font-size: 20px; color: "#A2481B;#0B5C8A") 夏（7〜9月）;冬（12〜3月）
  # 値の札 (語で弾む)
  p#lab_aug_t(left: 630px; cy: 122px; width: 120px; text-align: center; font-size: 18px; color: $muted; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 最大
  p#lab_aug(left: 630px; cy: 152px; width: 120px; text-align: center; font-size: 32px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 42.4
  p#lab_jan(left: 1263px; cy: 202px; width: 120px; text-align: center; font-size: 32px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 35.6
  p#lab_may_t(left: 250px; cy: 258px; width: 120px; text-align: center; font-size: 18px; color: $muted; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 最少
  p#lab_may(left: 250px; cy: 288px; width: 120px; text-align: center; font-size: 32px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 25.4
  # 5 月の水準の破線と 8 月までのかぎ・倍率の黒札
  shape#ref(path: "M350.0 309.3 L736.0 309.3"; background: none; border: 3px solid #4C5D64; dash: 6,4; in: draw {duration: 0.6})
  shape#brk(path: "M734.0 172.8 L742.0 172.8 Q750 172.8 750 180.8 L750 300.8 Q750 308.9 742.0 308.9 L734.0 308.9"; background: none; border: 3px solid $ink; in: draw {duration: 0.45})
  p#ratio(left: 760px; cy: 194px; font-size: 30px; font-family: n; color: #FFFFFF; background: $ink; border-radius: 12px; padding: 6px 16px; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2.2)'}) {s}5月の{/}1.7倍

# s4 用途別: ドーナツの 4 弧が時計回りに描かれ、右に 4 行の凡例・「空調」で空調の行に青い地と弧が太る・「半分」で青い札
section#s4(stagger: {each:0}; out: {y:-21, opacity:0, duration:0.3, ease:'power2.in'})
sec#s4_sec(n: "03"; l: "用途別の構成")
title#s4_title {em}空調{/}だけで44%、半分近くを占める
card#s4_card(left: 120px; top: 262px; width: 1680px; height: 640px)
  ctitle#t 用途別の内訳（年間の電気代）
  # ドーナツ (中心 273,237・半径 133・太さ 51・弧の間 1.1°・角の端)。弧は塗りの扇形 (外の弧 + 内の弧を Z で閉じる)・頭の 2 点で箱をドーナツ全体の正方形にし、12 時から時計回りの clock_wipe を弧ごとの delay と速さで hf の順の描き出しに合わせる
  shape#seg1(path: "M171 117 M648 594 M409.5 117.4 L417.8 117.6 L426.0 118.1 L434.2 118.8 L442.5 119.9 L450.6 121.1 L458.7 122.7 L466.8 124.5 L474.8 126.6 L482.7 129.0 L490.5 131.7 L498.3 134.7 L505.8 137.9 L513.3 141.3 L520.8 145.1 L528.0 149.1 L535.0 153.3 L542.1 157.8 L548.8 162.6 L555.5 167.6 L561.9 172.6 L568.2 178.1 L574.2 183.8 L580.0 189.4 L585.8 195.6 L591.2 201.8 L596.4 208.2 L601.3 214.8 L606.2 221.5 L610.8 228.5 L615.0 235.5 L619.0 242.7 L622.8 250.0 L626.4 257.5 L629.7 265.0 L632.7 272.9 L635.4 280.6 L638.0 288.5 L640.0 296.5 L642.0 304.5 L643.7 312.6 L645.0 320.9 L646.0 329.0 L646.8 337.2 L647.2 345.5 L647.5 353.7 L647.4 362.0 L647.1 370.2 L646.3 378.5 L645.5 386.7 L644.2 395.0 L642.8 403.0 L641.0 411.2 L638.8 419.1 L636.5 427.0 L633.9 434.8 L631.0 442.7 L627.8 450.3 L624.5 457.8 L620.7 465.2 L616.8 472.5 L612.6 479.5 L608.1 486.6 L603.5 493.3 L598.7 500.1 L593.4 506.5 L588.2 512.8 L582.5 519.0 L576.8 524.8 L570.8 530.5 L564.6 536.1 L558.2 541.3 L551.7 546.3 L545.0 551.2 L538.0 555.8 L531.0 560.1 L523.8 564.3 L516.6 568.0 L509.1 571.7 L501.5 575.0 L472.2 504.9 L477.3 502.7 L482.4 500.2 L487.3 497.5 L492.3 494.8 L497.0 491.8 L501.8 488.7 L506.2 485.4 L510.8 482.0 L515.1 478.3 L519.3 474.6 L523.3 470.7 L527.2 466.8 L531.0 462.6 L534.8 458.2 L538.2 453.9 L541.5 449.4 L544.7 444.8 L547.8 440.0 L550.7 435.2 L553.2 430.2 L555.8 425.1 L558.2 420.0 L560.2 414.8 L562.2 409.5 L564.0 404.2 L565.7 398.8 L567.0 393.3 L568.2 387.9 L569.2 382.4 L570.2 376.8 L570.8 371.1 L571.2 365.5 L571.5 360.0 L571.5 354.3 L571.3 348.6 L571.0 343.0 L570.5 337.5 L569.7 331.8 L568.8 326.2 L567.8 320.9 L566.4 315.3 L564.9 309.9 L563.2 304.5 L561.5 299.2 L559.3 294.0 L557.1 288.8 L554.7 283.6 L552.2 278.7 L549.5 273.8 L546.5 269.0 L543.5 264.3 L540.2 259.6 L536.7 255.1 L533.1 250.8 L529.5 246.6 L525.6 242.5 L521.5 238.5 L517.5 234.8 L513.2 231.0 L508.8 227.5 L504.3 224.1 L499.7 221.0 L495.0 218.0 L490.2 215.0 L485.2 212.2 L480.2 209.7 L475.0 207.5 L470.0 205.2 L464.7 203.2 L459.3 201.3 L453.9 199.6 L448.5 198.3 L443.0 197.0 L437.5 195.9 L432.0 195.0 L426.3 194.4 L420.8 194.0 L415.2 193.6 L409.5 193.5 Z"; background: $ac; delay: 600ms; in: clock_wipe {duration: 1.68, ease: 'none', dir: 'right'})
  # 空調の弧が 76 → 94 px に弾んで太る hf の動きは、太い扇形 (内 102・外 165) を重ねて溶かして出す (描き終わる前に全長が見えないよう印は語の +200)
  shape#seg1w(path: "M162 108 M657 603 M409.5 108.4 L418.0 108.6 L426.6 109.1 L435.2 109.8 L443.7 110.9 L452.2 112.2 L460.7 113.9 L469.0 115.8 L477.3 118.1 L485.5 120.4 L493.7 123.3 L501.6 126.3 L509.5 129.6 L517.3 133.2 L525.0 137.1 L532.5 141.3 L539.8 145.6 L547.0 150.3 L554.1 155.2 L561.0 160.4 L567.6 165.8 L574.2 171.3 L580.5 177.1 L586.5 183.3 L592.3 189.4 L598.0 195.9 L603.5 202.6 L608.7 209.4 L613.7 216.5 L618.3 223.6 L622.8 231.0 L627.0 238.5 L630.9 246.0 L634.7 253.8 L638.0 261.8 L641.1 269.7 L644.0 277.8 L646.5 285.9 L648.8 294.3 L650.7 302.5 L652.5 311.0 L653.8 319.5 L654.9 328.0 L655.8 336.5 L656.2 345.1 L656.5 353.7 L656.4 362.2 L656.0 370.8 L655.3 379.4 L654.3 387.9 L653.1 396.5 L651.6 404.8 L649.7 413.2 L647.5 421.5 L645.2 429.8 L642.3 437.8 L639.3 446.0 L636.2 453.9 L632.5 461.7 L628.7 469.3 L624.6 476.8 L620.2 484.3 L615.6 491.5 L610.8 498.6 L605.7 505.5 L600.5 512.2 L594.9 518.7 L589.0 525.2 L583.0 531.3 L576.9 537.2 L570.5 542.8 L563.8 548.4 L557.1 553.7 L550.0 558.6 L543.0 563.4 L535.7 567.9 L528.2 572.1 L520.7 576.2 L512.8 579.9 L505.0 583.3 L468.6 496.7 L473.5 494.4 L478.3 492.2 L483.0 489.8 L487.7 487.0 L492.2 484.2 L496.7 481.3 L500.8 478.2 L505.0 474.9 L509.2 471.6 L513.2 468.0 L517.0 464.4 L520.8 460.5 L524.2 456.6 L527.7 452.5 L531.0 448.3 L534.2 444.2 L537.2 439.8 L540.0 435.3 L542.7 430.7 L545.2 426.0 L547.7 421.2 L549.9 416.4 L551.8 411.5 L553.8 406.5 L555.5 401.5 L557.0 396.5 L558.3 391.2 L559.3 386.1 L560.4 380.9 L561.2 375.6 L561.8 370.4 L562.2 365.0 L562.5 359.7 L562.5 354.3 L562.3 349.0 L562.0 343.8 L561.6 338.4 L560.8 333.1 L560.0 327.9 L558.9 322.8 L557.7 317.5 L556.3 312.5 L554.7 307.4 L552.9 302.4 L551.1 297.5 L549.0 292.5 L546.6 287.7 L544.2 283.0 L541.7 278.4 L538.8 273.8 L536.0 269.4 L533.0 265.0 L529.7 260.9 L526.3 256.6 L522.8 252.6 L519.2 248.9 L515.4 245.1 L511.5 241.5 L507.5 237.9 L503.2 234.6 L499.0 231.5 L494.7 228.5 L490.2 225.6 L485.7 222.8 L481.0 220.2 L476.2 217.8 L471.5 215.5 L466.5 213.6 L461.5 211.6 L456.6 209.9 L451.5 208.4 L446.4 207.0 L441.2 205.8 L435.9 204.8 L430.7 204.0 L425.4 203.4 L420.2 202.8 L414.8 202.6 L409.5 202.5 Z"; background: $ac; in: {opacity:0, duration:0.5, ease:'power2.out'})
  shape#seg2(path: "M171 117 M648 594 M497.1 576.8 L489.5 579.6 L481.7 582.3 L473.8 584.7 L465.9 586.8 L457.8 588.6 L449.8 590.1 L441.8 591.3 L433.5 592.3 L425.4 593.0 L417.2 593.4 L409.0 593.5 L400.8 593.4 L392.5 593.0 L384.5 592.2 L376.4 591.2 L368.2 590.0 L360.1 588.3 L352.2 586.5 L344.2 584.4 L336.5 582.0 L328.6 579.3 L321.0 576.5 L313.4 573.3 L306.0 569.8 L298.6 566.1 L291.5 562.2 L284.4 558.0 L277.5 553.5 L270.8 548.8 L264.1 543.9 L257.7 538.8 L251.5 533.5 L245.5 528.0 L239.7 522.2 L234.0 516.3 L228.6 510.2 L223.4 503.8 L218.4 497.2 L213.6 490.7 L209.1 483.8 L204.8 476.8 L200.7 469.7 L196.8 462.5 L193.4 455.1 L190.1 447.5 L260.1 418.2 L262.4 423.3 L264.8 428.2 L267.3 433.2 L270.1 438.0 L273.0 442.8 L276.1 447.5 L279.5 452.0 L282.8 456.5 L286.4 460.8 L290.1 465.0 L293.9 469.0 L297.9 473.0 L302.0 476.7 L306.1 480.3 L310.6 483.8 L315.0 487.0 L319.6 490.3 L324.3 493.3 L329.1 496.2 L334.0 498.9 L339.0 501.3 L344.1 503.7 L349.2 505.8 L354.5 507.9 L359.7 509.7 L365.1 511.3 L370.5 512.7 L375.9 514.0 L381.5 515.1 L386.8 515.8 L392.4 516.6 L398.0 517.0 L403.7 517.3 L409.2 517.5 L414.8 517.3 L420.3 517.2 L425.8 516.6 L431.4 516.0 L437.0 515.1 L442.5 514.0 L447.9 512.8 L453.3 511.5 L458.5 509.8 L464.0 508.0 L469.2 506.1 Z"; background: $oa; delay: 398ms; in: clock_wipe {duration: 2.127, ease: 'none', dir: 'right'})
  shape#seg3(path: "M171 117 M648 594 M188.2 443.1 L185.2 435.3 L182.7 427.5 L180.3 419.5 L178.2 411.6 L176.4 403.5 L174.9 395.4 L173.6 387.2 L172.6 379.0 L172.1 370.8 L171.6 362.5 L171.4 354.1 L171.8 345.9 L172.2 337.6 L172.9 329.4 L174.0 321.3 L175.4 313.0 L176.9 305.0 L178.8 296.9 L181.1 288.9 L183.4 281.1 L186.1 273.3 L189.1 265.5 L192.5 257.9 L195.9 250.5 L199.8 243.0 L203.7 235.8 L208.0 228.8 L212.5 221.9 L217.4 215.1 L222.3 208.5 L227.5 202.0 L233.0 195.9 L238.6 189.8 L244.5 183.9 L250.5 178.4 L256.8 172.9 L263.2 167.7 L269.9 162.8 L276.6 157.9 L283.6 153.6 L290.7 149.2 L328.6 215.1 L323.9 218.0 L319.0 221.1 L314.4 224.2 L309.9 227.7 L305.5 231.3 L301.4 234.9 L297.1 238.8 L293.2 242.7 L289.4 246.9 L285.6 251.1 L282.1 255.5 L278.7 260.0 L275.4 264.6 L272.4 269.2 L269.4 274.0 L266.7 279.0 L264.1 284.0 L261.8 289.0 L259.5 294.3 L257.5 299.5 L255.6 304.8 L254.0 310.2 L252.5 315.6 L251.2 321.1 L250.0 326.7 L249.1 332.2 L248.4 337.8 L248.0 343.4 L247.6 349.0 L247.5 354.6 L247.5 360.3 L247.8 365.9 L248.2 371.5 L249.0 377.1 L249.8 382.6 L250.8 388.2 L252.0 393.8 L253.5 399.2 L255.1 404.5 L257.0 409.8 L258.9 415.2 Z"; background: $lighting; delay: 329ms; in: clock_wipe {duration: 2.218, ease: 'none', dir: 'right'})
  shape#seg4(path: "M171 117 M648 594 M294.9 147.0 L302.1 143.1 L309.5 139.5 L317.0 136.2 L324.6 133.2 L332.2 130.4 L340.0 127.8 L348.0 125.6 L356.0 123.6 L364.0 121.9 L372.1 120.4 L380.2 119.2 L388.3 118.5 L396.6 117.9 L404.7 117.6 L406.2 193.5 L400.7 193.8 L395.1 194.1 L389.5 194.7 L384.0 195.5 L378.6 196.5 L373.0 197.7 L367.6 199.0 L362.2 200.5 L357.0 202.2 L351.8 204.1 L346.5 206.2 L341.4 208.5 L336.5 210.9 L331.5 213.6 Z"; background: $other; delay: 0ms; in: clock_wipe {duration: 2.709, ease: 'none', dir: 'right'})
  cnote#n 合計 1,171万円＝100%
  p#c_l(cx: 410px; cy: 321px; font-size: 22px; color: $muted; delay: 900ms; in: {y:10, opacity:0, duration:0.6, ease:'power3.out'}) 年間の電気代
  p#c_v(cx: 410px; cy: 372px; font-size: 64px; font-family: n; letter-spacing: -0.02em; delay: 900ms; in: {y:10, opacity:0, duration:0.6, ease:'power3.out'}) 1,171{s2}万円{/}
  # 凡例の 4 行 (色の四角・名と説明・% と金額)・空調の行だけ淡い青の地 (語で出す)
  div#row(left: 800px; top: "120;240;360;480"; width: 840px; height: 112px; border-radius: 18px; delay: 750ms; in: {x:30, opacity:0, duration:0.6, ease:'power3.out', stagger:{each:0.14}}) ×4
    div#hl(inset: 0; border-radius: 18px; background: #EEF3FD; border: 3px solid #C8D8F7; opacity: "1;0;0;0"; in: {opacity:0, duration:0.4})
    div#sw(left: 28px; top: 40px; width: 30px; height: 30px; border-radius: 8px; background: "$ac;$oa;$lighting;$other")
    p#name(left: 80px; cy: 45px; font-size: 34px) 空調;OA機器;照明;その他
    p#desc(left: 82px; cy: 84px; font-size: 20px; color: $muted; font-family: m) 冷房・暖房;PC・複合機・モニターなど;現在は蛍光灯;給湯・エレベーター・冷蔵庫など
    p#pct(right: 260px; cy: 56px; font-size: 64px; font-family: n; letter-spacing: -0.02em) 44{pc}%{/};25{pc}%{/};23{pc}%{/};8{pc}%{/}
    p#yen(right: 30px; cy: 57px; font-size: 38px; font-family: n; color: $ink2) 515{s2}万円{/};293{s2}万円{/};269{s2}万円{/};94{s2}万円{/}
  p#badge(left: 1060px; cy: 120px; font-size: 22px; color: #FFFFFF; background: $ac; border-radius: 20px; padding: 6px 16px; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 半分近く

# s5 ピーク: 縦の目盛りの上に横棒 4 本 (夏 → 冬 → 平日昼 → 夜間) を語で伸ばし、値の札が弾む・「暖房」で右に朝 9:00 の注記の板・「朝」で板の縁が脈打つ
section#s5(stagger: {each:0}; out: {y:-21, opacity:0, duration:0.3, ease:'power2.in'})
sec#s5_sec(n: "04"; l: "ピーク電力")
title#s5_title 冬の山は、{em}始業時の朝{/}に来る
card#s5_card(left: 120px; top: 262px; width: 1680px; height: 640px)
  ctitle#t 30分値の最大と平均
  cnote#n 単位：kW（30分ごとの平均電力）
  # 縦の目盛り (0〜200 kW = 507 px) と区切りの破線
  div#gl(left: "470.0;660;850.1;1039.9;1230"; top: 128px; width: 2px; height: 430px; background: $grid) ×5
  p#gn(left: "442.0;632.0;822;1012.1;1201.9"; cy: 579px; width: 56px; text-align: center; font-size: 20px; color: $muted; font-family: m) ×5 0;50;100;150;200
  p#gu(left: 1256px; cy: 579px; font-size: 20px; color: $muted; font-family: m) kW
  shape#div(path: "M40.0 351 L1639.9 351"; background: none; border: 2px solid $line; dash: 5,4)
# ピークの行 (丸い地の icon + 名 + 日時 + 棒 + 値)・行は左から入り、棒と値は語で
def prow(i, c, t, s, w, v, vl) = div(left: 120px; width: 1680px; height: 56px; in: {x:-20, opacity:0, duration:0.45, ease:'power3.out'})
  icon#ic(left: 40px; cy: 28px; font-size: 32px; padding: 12px; name: {i}; weight: bold; color: #FFFFFF; background: {c})
  p#nm(left: 112px; cy: 15px; font-size: 30px; content: {t})
  p#sb(left: 112px; cy: 50px; font-size: 22px; color: $muted; font-family: m; content: {s})
  div#bar(left: 470px; top: 3px; width: {w}; height: 50px; border-radius: 4px 10px 10px 4px; background: {c}; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
  p#val(left: {vl}; cy: 24px; font-size: 50px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}; content: {v})
prow#s5_r1(i: sun; c: $summer; t: "夏のピーク"; s: "8月7日 14:30"; w: 706px; v: "186{s3}kW{/}"; vl: 1192px; top: 390px)
prow#s5_r2(i: snowflake; c: $winter; t: "冬のピーク"; s: "1月23日 9:00"; w: 600px; v: "158{s3}kW{/}"; vl: 1086px; top: 502px)
prow#s5_r3(i: briefcase; c: $avg; t: "平日昼の平均"; s: ""; w: 411px; v: "108{s3}kW{/}"; vl: 897px; top: 646px; height: 56px)
  icon#ic(cy: 20px; font-size: 26px; padding: 10px)
  p#nm(cy: 20px; font-size: 26px)
  div#bar(top: 0px; height: 36px)
  p#val(cy: 18px; font-size: 36px)
prow#s5_r4(i: moon; c: #26356B; t: "夜間・休日の平均"; s: "平日19時〜翌9時・休日"; w: 72px; v: "19{s3}kW{/}"; vl: 558px; top: 735px; height: 56px)
  icon#ic(cy: 20px; font-size: 26px; padding: 10px)
  p#nm(cy: 20px; font-size: 26px)
  p#sb(cy: 50px; font-size: 20px)
  div#bar(top: 0px; height: 36px)
  p#val(cy: 18px; font-size: 36px)
# 注記の板 (時計の icon + 青い題 + 2 行)
div#s5_call(left: 1410px; top: 498px; width: 350px; height: 162px; border-radius: 18px; background: #EAF6FD; border: 3px solid #BFE3F7; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  icon#ic(left: 24px; cy: 42px; font-size: 30px; name: clock; weight: bold; color: #0B5C8A)
  p#h(left: 64px; cy: 42px; font-size: 28px; color: #0B5C8A) 冬の山は朝 9:00
  p#p(left: 24px; top: 70px; font-size: 22px; line-height: 1.5; font-family: m) 始業時に全フロアの[br]暖房が一斉に立ち上がる

# s6 夜間・休日: 紺の地が円で開き、夜のオフィスの等角図・右に 3 枚のガラスの板 (19 kW・31% と帯・363 万円) を語で → 「その」で板と題を払い、内訳の板 (3 色の帯が語で伸び、かぎと「止められる分 59%」)
section#s6(stagger: {each:0}; out: {y:-21, opacity:0, duration:0.3, ease:'power2.in'})
div#s6_bg(inset: 0; background: linear(#0F1D42,#0B1530@70%,160); pattern: dots,21,#FFFFFF0F,0.8; in: circle_wipe {duration: 0.75, ease: 'power2.inOut'}; out: iris_wipe {duration: 0.5, ease: 'power2.in'})
div#s6_glow(inset: 0; background: radial(#506EDC47,#506EDC00@45%,20%,30%); in: circle_wipe {duration: 0.75, ease: 'power2.inOut'}; out: iris_wipe {duration: 0.5, ease: 'power2.in'})
sec#s6_sec(n: "05"; l: "誰もいない時間の電気"; c: $mint; nc: $navy; delay: 400ms)
title#s6_ta(c: #FFFFFF; delay: 500ms) 夜と休日も、電気は{mi}ゼロにならない{/}
title#s6_tb(c: #FFFFFF; delay: 0ms) そのうち{mi}59%{/}は、止められる電気
img#s6_img(left: 60px; top: 262px; width: 960px; height: 640px; object-fit: contain; main: kb {scale: [1, 1.06]}; delay: 400ms; in: {x:-40, opacity:0, duration:0.9, ease:'power3.out'}) [transparent]夜の現代的なオープンオフィスの 1 フロアを斜め上 30 度から見下ろした等角図の切り抜き。人は誰もいない。深い紺と藍の夜の色調。待機中でかすかに光るモニターがいくつか、小さな待機ランプの灯る複合機、小さな緑のランプが点滅するサーバーラック、冷蔵庫、消し忘れで暖かい光を落とす天井の照明 1 列、動いたままのエアコン。宙に浮いた 1 枚のフロアのブロックで、枠いっぱいに大きく描く。静かで清潔
# ガラスの板 (白 7% の地 + 白 16% の細い縁)
def glass = div(left: 1060px; width: 740px; border-radius: 22px; background: #FFFFFF12; border: 2px solid #FFFFFF29; in: {y:24, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-12, opacity:0, duration:0.35, ease:'power2.in'})
def glab(t) = p(left: 32px; cy: 42px; font-size: 24px; color: #C9D4EE; content: {t})
glass#s6_a1(top: 262px; height: 196px)
  glab#l 夜間・休日の平均電力
  p#v(left: 30px; cy: 130px; font-size: 100px; line-height: 1; font-family: n; color: #FFFFFF; letter-spacing: -0.02em) [count:19 start=0 ms=800ms delay=150ms]
  p#u(left: .v.right+10; cy: 156px; font-size: 32px; color: #D9E2F5) kW
  p#nt(left: 330px; top: 96px; font-size: 20px; line-height: 1.45; color: #B9C6E4; font-family: m) 夜間＝平日19時〜翌9時[br]休日＝終日
glass#s6_a2(top: 474px; height: 220px)
  glab#l 年間使用量に占める割合
  p#v(left: 30px; cy: 110px; font-size: 76px; line-height: 1; font-family: n; color: #FFFFFF; letter-spacing: -0.02em) [count:31 start=0 ms=900ms delay=150ms]
  p#u(left: .v.right+10; cy: 126px; font-size: 32px; color: #D9E2F5) %
  p#nt(left: 250px; cy: 118px; font-size: 20px; color: #B9C6E4; font-family: m) 119,040 kWh ／ 384,000 kWh
  div#tr(left: 32px; top: 168px; width: 676px; height: 30px; border-radius: 15px; background: #FFFFFF1F)
  div#fill(left: 32px; top: 168px; width: 210px; height: 30px; border-radius: 15px; background: linear(#7C95FF,#A98CFF,90); in: {scaleX:0, duration:0.9, ease:'power3.out', pivot:'left'})
glass#s6_a3(top: 710px; height: 190px)
  glab#l 電気代にすると
  p#v(left: 30px; cy: 122px; font-size: 92px; line-height: 1; font-family: n; color: $mint; letter-spacing: -0.02em) [count:363 start=0 ms=1000ms delay=150ms]
  p#u(left: .v.right+10; cy: 144px; font-size: 32px; color: $mint) 万円/年
# 内訳の板: 3 色の帯 (41 / 37 / 22%) が語ごとに左から伸び、止められる 2 つの上にかぎと緑の札・下に 3 行の凡例
glass#s6_b(top: 262px; height: 638px)
  p#hd(left: 32px; cy: 45px; font-size: 26px; color: #C9D4EE) 夜間・休日の電気 119,040 kWh の内訳
  div#seg1(left: 32px; top: 160px; width: 274px; height: 76px; border-radius: 12px 0px 0px 12px; background: $fixed; in: {scaleX:0, duration:0.5, ease:'power2.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 30px; font-family: n; color: $navy) 41%
  div#seg2(left: 309px; top: 160px; width: 247px; height: 76px; background: $standby; in: {scaleX:0, duration:0.45, ease:'power2.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 30px; font-family: n; color: $navy) 37%
  div#seg3(left: 559px; top: 160px; width: 149px; height: 76px; border-radius: 0px 12px 12px 0px; background: $forgot; in: {scaleX:0, duration:0.4, ease:'power2.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 30px; font-family: n; color: $navy) 22%
  shape#brk(path: "M309.1 150 L309.1 132 Q309.1 127.9 317.1 127.9 L699.9 127.9 Q708 127.9 708 132 L708 150"; background: none; border: 3px solid $mint; in: draw {duration: 0.4})
  p#brk_l(left: 390px; cy: 96px; font-size: 24px; font-family: n; color: $navy; background: $mint; border-radius: 16px; padding: 4px 16px; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 止められる分 59%
  div#lg(left: 32px; top: "290.0;400.0;510"; width: 676px; height: 96px; in: {x:20, opacity:0, duration:0.45, ease:'power3.out'}) ×3
    div#ln(left: 0px; top: 0px; width: 676px; height: 2px; background: #FFFFFF24)
    div#sw(left: 0px; top: 30px; width: 26px; height: 26px; border-radius: 8px; background: "$fixed;$standby;$forgot")
    p#n(left: 44px; cy: 36px; font-size: 28px; color: #FFFFFF) 止められない分;待機電力;消し忘れ
    p#d(left: 45px; cy: 72px; font-size: 20px; color: #B9C6E4; font-family: m) サーバー・冷蔵庫など;PC・複合機・モニター;照明・空調
    p#tag(right: 190px; cy: 42px; font-size: 18px; color: $mint; background: #5FE3B529; border-radius: 12px; padding: 3px 12px; opacity: "0;1;1") 止められる
    p#v(right: 0px; cy: 44px; font-size: 36px; font-family: n; color: #FFFFFF) 4.9{s4}万kWh{/};4.4{s4}万kWh{/};2.6{s4}万kWh{/}

# s8 対策: 3 枚の札が語ごとに下から入り (絵は弾んで浮き続ける)、金額の語で年の削減額が数え上がる
section#s8(stagger: {each:0}; out: {y:-21, opacity:0, duration:0.3, ease:'power2.in'})
sec#s8_sec(n: "06"; l: "削減の試算（年額）")
title#s8_title 3つの対策で、どれだけ減らせるか
# 対策の札 (工事の札・番号・絵・題・箇条・罫・年の削減額・kWh)
def mcard(no, tg, tgc, tgf, h, res, kwh) = div(top: 262px; width: 532px; height: 640px; background: #FFFFFF; border: 2px solid #E0E8E5; border-radius: 24px; box-shadow: 0px 14px 34px #13222B12; in: {y:40, opacity:0, duration:0.7, ease:'power3.out'})
  p#tag(z-index: front; left: 28px; cy: 46px; font-size: 21px; color: {tgc}; background: {tgf}; border-radius: 16px; padding: 6px 16px; content: {tg})
  p#no(right: 28px; cy: 40px; font-size: 30px; font-family: n; color: #7B8D87; content: {no})
  p#h(left: 34px; cy: 292px; font-size: 32px; content: {h})
  div#ln(left: 34px; top: 462px; width: 465px; height: 2px; background: $line)
  div#res(left: 32px; top: 480px; width: 465px; height: 90px; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'})
    p#s(left: 0px; cy: 68px; font-size: 24px; color: $ink2) 年
    p#v(left: .s.right+8; cy: 45px; font-size: 86px; line-height: 1; font-family: n; color: $green_d; letter-spacing: -0.02em; content: {res})
    p#u(left: .v.right+8; cy: 66px; font-size: 30px; color: $green_d) 万円
  p#kwh(left: 34px; cy: 602px; font-size: 22px; color: $muted; font-family: m; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'}; content: {kwh})
mcard#s8_c1(left: 120px; no: "01"; tg: "工事なし"; tgc: $green_d; tgf: $green_l; h: "空調の設定温度を1℃見直し"; res: "[count:51.5 start=0 ms=900ms delay=100ms]"; kwh: "16,900 kWh／年")
  img#pic(left: 150px; top: 26px; width: 260px; height: 230px; object-fit: contain; main: sine {y: -8, period: 3.2}; delay: 150ms; in: {scale:0.85, y:10, duration:0.8, ease:'back.out(1.8)'}) [transparent]白くすっきりした壁掛けのオフィス用エアコン 1 台からやわらかな風の線が流れ、その横に空の液晶の白いリモコンが浮かぶ。単体の物、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#dot(left: 34px; top: "338;374"; width: 8px; height: 8px; border-radius: 148px; background: $green) ×2
  p#li(left: 54px; cy: "342;377"; font-size: 22px; color: $ink2; font-family: m) ×2 夏 26℃→27℃／冬 22℃→21℃;空調の電力を10%削減
mcard#s8_c2(left: 693px; no: "02"; tg: "工事なし"; tgc: $green_d; tgf: $green_l; h: "待機電力・消し忘れ対策"; res: "[count:142.8 start=0 ms=900ms delay=100ms]"; kwh: "46,800 kWh／年")
  img#pic(left: 150px; top: 26px; width: 260px; height: 230px; object-fit: contain; main: sine {y: -8, period: 3.2}; delay: 150ms; in: {scale:0.85, y:10, duration:0.8, ease:'back.out(1.8)'}) [transparent]デスクトップのモニター 1 台と、プラグを抜いて電源を切る電源タップ、丸い時計のタイマーの印と小さな三日月の印。省エネの考え方、単体の物、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#dot(left: 34px; top: "338;374;408"; width: 8px; height: 8px; border-radius: 148px; background: $green) ×3
  p#li(left: 54px; cy: "342;377;413"; font-size: 22px; color: $ink2; font-family: m) ×3 OA機器の自動電源オフ;照明・空調のタイマー;止められる分の3分の2を削減
mcard#s8_c3(left: 1268px; no: "03"; tg: "工事あり　960万円"; tgc: #8A5300; tgf: #FFF3DF; h: "照明のLED化"; res: "[count:148.2 start=0 ms=900ms delay=100ms]"; kwh: "48,600 kWh／年")
  img#pic(left: 150px; top: 26px; width: 260px; height: 230px; object-fit: contain; main: sine {y: -8, period: 3.2}; delay: 150ms; in: {scale:0.85, y:10, duration:0.8, ease:'back.out(1.8)'}) [transparent]白い清潔な光でやわらかく輝く、現代的な薄い正方形の LED 天井照明パネル 1 枚を少し下から斜めに見上げた形、省エネを表す小さな葉の印。単体の物、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#dot(left: 34px; top: "338;374"; width: 8px; height: 8px; border-radius: 148px; background: $green) ×2
  p#li(left: 54px; cy: "342;377"; font-size: 22px; color: $ink2; font-family: m) ×2 蛍光灯→LED（照明の電力55%減）;工事費は約6.5年で回収

# s9 合計: 滝の図 (現在 → 3 つの削減 → 対策後) が左から順に伸び、点線で段をつなぐ・「342.5」で右の合計の板が数え上がり、「29%」で割合と前後の金額
section#s9(stagger: {each:0}; out: {y:-21, opacity:0, duration:0.3, ease:'power2.in'})
sec#s9_sec(n: "06"; l: "削減の試算（合計）")
title#s9_title 合わせて年{em}342.5万円{/}、電気代の29%を削減
card#s9_card(left: 120px; top: 262px; width: 1090px; height: 640px)
  ctitle#t 年間の電気代の変化
  cnote#n 単位：万円
  # 目盛り (0〜1,200 万円 = 288 px)
  div#gl(left: 110px; top: "555;447;339;231;123"; width: 940px; height: 2px; background: $grid) ×5
  p#gn(left: 34px; cy: "557;449;341;233;125"; width: 62px; text-align: right; font-size: 20px; color: $muted; font-family: m) ×5 0;300;600;900;1,200
  # 棒 (現在と対策後は下から・削減の 3 本は上から伸びる)
  div#b0(left: 150px; top: 134px; width: 132px; height: 422px; border-radius: 6px; background: #7D8F96; delay: 550ms; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom'})
  div#b1(left: 334px; top: 134px; width: 132px; height: 19px; border-radius: 6px; background: $green; delay: 1100ms; in: {scaleY:0, duration:0.45, ease:'power3.out', pivot:'top'})
  div#b2(left: 518px; top: 153px; width: 132px; height: 51px; border-radius: 6px; background: $green; delay: 1500ms; in: {scaleY:0, duration:0.45, ease:'power3.out', pivot:'top'})
  div#b3(left: 702px; top: 204px; width: 132px; height: 53px; border-radius: 6px; background: $green; delay: 1900ms; in: {scaleY:0, duration:0.45, ease:'power3.out', pivot:'top'})
  div#b4(left: 886px; top: 258px; width: 132px; height: 298px; border-radius: 6px; background: $ink; delay: 2300ms; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom'})
  p#l(left: "115.9;300;484.0;668.0;852"; cy: "108.6;108.6;108.6;179;231.9"; width: 200px; text-align: center; font-size: 30px; font-family: n; color: "$ink;$green_d;$green_d;$green_d;$ink"; delay: "850ms;1400ms;1800ms;2200ms;2600ms"; in: {scale:0.7, opacity:0, duration:0.4, ease:'back.out(2.2)'}) ×5 1,171;−51.5;−142.8;−148.2;829
  p#cat(left: "115.9;300;484.0;668.0;852"; top: 568px; width: 200px; text-align: center; font-size: 21px; line-height: 1.3; color: $ink2; font-family: m) ×5 現在;設定温度[br]1℃見直し;待機・[br]消し忘れ対策;照明の[br]LED化;対策後
  shape#c0(path: "M282 134 L334.0 134"; background: none; border: 2px solid #9FB0B5; dash: 4,3; delay: 950ms; in: draw {duration: 0.3})
  shape#c1(path: "M466.0 151.9 L518.0 151.9"; background: none; border: 2px solid #9FB0B5; dash: 4,3; delay: 1500ms; in: draw {duration: 0.3})
  shape#c2(path: "M650.0 203.4 L702 203.4"; background: none; border: 2px solid #9FB0B5; dash: 4,3; delay: 1900ms; in: draw {duration: 0.3})
  shape#c3(path: "M834 256.8 L886.1 256.8"; background: none; border: 2px solid #9FB0B5; dash: 4,3; delay: 2300ms; in: draw {duration: 0.3})
# 合計の板 (淡い緑のグラデ + 緑の縁): 削減額・罫・割合・前後の金額・kWh・注記
div#s9_total(left: 1250px; top: 262px; width: 550px; height: 640px; border-radius: 24px; background: linear(#E9F8F1,#FFFFFF@75%,180); border: 3px solid #BFE6D4; box-shadow: 0px 14px 34px #13222B12; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  p#lab(left: 44px; cy: 58px; font-size: 26px; color: $ink2) 年間の削減額
  p#v(left: 40px; cy: 154px; font-size: 124px; line-height: 1; font-family: n; color: $green_d; letter-spacing: -0.02em) [count:342.5 start=0 ms=1100ms delay=150ms]
  p#u(left: .v.right+8; cy: 186px; font-size: 38px; color: $green_d) 万円
  div#ln(left: 44px; top: 262px; width: 462px; height: 2px; background: #CFE7DC)
  div#pct(left: 44px; top: 290px; width: 462px; height: 81px; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'})
    p#a(left: 0px; cy: 60px; font-size: 28px) 年間電気代の
    p#v(left: .a.right+10; cy: 40px; font-size: 80px; line-height: 1; font-family: n; color: $green_d) 29
    p#b(left: .v.right+10; cy: 60px; font-size: 28px) %
  p#flow(left: 44px; cy: 434px; font-size: 32px; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) {nn}1,171{/}万円 {em}→{/} {nn}829{/}万円
  p#kwh(left: 44px; cy: 488px; font-size: 24px; color: $ink2; font-family: m; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) 使用量は年 112,300 kWh 減
  p#nt(left: 44px; cy: 592px; font-size: 20px; color: $muted; font-family: m) ※3つの対策の合計（年額）

# s10 まとめ: 3 行の結論の札が語ごとに下から入り、2 行目 (緑の縁) に「まずはここから」の札・締めの間で 1 と 3 を沈め、2 を少し大きく
section#s10(stagger: {each:0})
sec#s10_sec(n: "07"; l: "まとめ")
title#s10_title まずは、{em}工事のいらない対策{/}から
def srow(no, t, s) = div(left: 120px; width: 1680px; height: 178px; background: #FFFFFF; border: 2px solid #E0E8E5; border-radius: 24px; box-shadow: 0px 14px 34px #13222B12; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  p#no(left: 40px; cy: 88px; width: 78px; height: 78px; text-align: center; align-items: center; font-size: 40px; line-height: 1; font-family: n; color: #FFFFFF; background: $green_d; border-radius: 148px; content: {no})
  p#t(left: 150px; cy: 63px; font-size: 40px; content: {t})
  p#s(left: 152px; cy: 122px; font-size: 24px; color: $ink2; font-family: m; content: {s})
srow#s10_r1(top: 268px; no: "1"; t: "電気代の{em}44%{/}は空調、{em}31%{/}は誰もいない夜と休日に"; s: "空調 515万円／夜間・休日 363万円（いずれも年額）"; delay: 200ms)
srow#s10_r2(top: 466px; no: "2"; t: "設定温度1℃と待機・消し忘れ対策で、{em}年194万円{/}"; s: "工事なしで実施できる（51.5万円＋142.8万円）"; background: linear(#EEFAF4,#FFFFFF@70%,90); border: 3px solid $green)
  div#first(right: 40px; top: 58px; width: 266px; height: 62px; border-radius: 30px; background: $green_d; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2.2)'})
    icon#i(left: 24px; cy: 50%; font-size: 26px; name: check; weight: bold; color: #FFFFFF)
    p#t(left: 64px; cy: 50%; font-size: 26px; color: #FFFFFF) まずはここから
srow#s10_r3(top: 664px; no: "3"; t: "LED化も合わせれば、{em}年342万円・約3割{/}の削減"; s: "LED化の工事費960万円は約6.5年で回収")
p#s10_src(left: 120px; cy: 884px; font-size: 20px; color: $muted; font-family: m; in: {y:10, opacity:0, duration:0.6, ease:'power3.out'}) データ：スマートメーター30分値 17,520コマ（昨年度4月〜3月）、フロア別・系統別子メーター／金額は年額の試算
```

```timeline.txt
#v2
# hf の作り: 声は 1.10 倍に詰めて 84 s。ここで引く話者は既定の速さで hf の話速と尺に近い (110% にすると 75 s に縮む) ので速さは書かない
cast n = "明るくクリアな中高音の20代の女性ナレーター、滑らかで明瞭な発声、丁寧で快活、落ち着いて信頼感のある語り口"
silence head=0ms tail=0ms

*** s1
[>#subtitle]
bgm music
se title +180ms
se whoosh -2dB +550ms
@n: [silence:0.8s][!#s1_l2{uem} marker +200ms]オフィスの電気代、どこに消えているのでしょうか。[silence:0.22s]

*** s2
se swish -3dB +20ms
@n: [silence:0.3s]社員200人のオフィスで1年分の電力データを[>#s2_k1 -200ms][>#s2_k3 -40ms][>#s2_k4 +120ms][♪multi -2dB +50ms]分析すると、[|]電気代は年[>#s2_k2 -550ms][♪ping -2dB +50ms][!#s2_k2 glow,#0E9F6E47 {blur: 29} +600ms]1,171万円でした。[silence:0.26s]

*** s3
se swish -3dB +20ms
se rise -3.5dB +450ms
@n: [silence:0.3s][chap #chap.ch[1] #chap.ch[2] 81 75 -250ms]月別では、夏の[!#s3_card.bar[5] fill,$summer {duration: .4}][>#s3_card.lab_aug_t +100ms][>#s3_card.lab_aug +100ms][♪pop -3dB]8月と冬の[!#s3_card.bar[10] fill,$winter {duration: .4}][>#s3_card.lab_jan +100ms][♪pop -3dB]1月に2つの山。8月は、最も少ない[>#s3_card.lab_may_t][>#s3_card.lab_may][>#s3_card.ref +150ms]5月の[>#s3_card.brk -300ms][>#s3_card.ratio -50ms][♪chime -1dB]1.7倍です。[silence:0.25s]

*** s4
se swish -3dB +20ms
se soft -2dB +400ms
@n: [silence:0.3s][chap #chap.ch[2] #chap.ch[3] 158 75 -250ms]用途別では[>#s4_card.row[1].hl][>#s4_card.seg1w +200ms][♪pop -2dB]空調が44%と、[>#s4_card.badge]半分近くを占めます。[silence:0.65s]

*** s5
se swish -3dB +20ms
@n: [silence:0.35s][chap #chap.ch[3] #chap.ch[4] 235 87 -300ms]ピークは[>#s5_r1 -150ms][>#s5_r1.bar][>#s5_r1.val +450ms][♪pop -3dB]夏が186kW。[>#s5_r2 -150ms][>#s5_r2.bar][>#s5_r2.val +450ms][♪pop -3dB]冬は158kWで、[|][>#s5_r3 -750ms][>#s5_r3.bar -600ms][>#s5_r3.val -150ms][>#s5_r4 -450ms][>#s5_r4.bar -300ms][>#s5_r4.val +150ms][>#s5_call][♪chime -2dB]暖房が一斉に立ち上がる始業時の[!#s5_call glow,#2FA4E72E {blur: 0, spread: 7}][=#s5_call +500ms]朝に来ます。[silence:0.22s]

*** s6
se swish -3dB +20ms
@n: [silence:0.4s][chap #chap.ch[4] #chap.ch[5] 325 112 -350ms]そして、[♪low -1dB -250ms]誰もいない夜と休日も平均[>#s6_a1 -350ms][♪pop -3dB]19kW。この時間だけで全体の[>#s6_a2 -450ms][>#s6_a2.fill -200ms][♪pop -3dB]31%、[|]電気代にして[>#s6_a3 -500ms][♪chime -2dB]363万円です。[silence:0.5s]
@: [<#s6_a1 -700ms][<#s6_a2 -700ms][<#s6_a3 -700ms][<#s6_ta -650ms][>#s6_tb -350ms][>#s6_b -350ms][>#s6_b.seg1 -100ms][>#s6_b.lg[1]]その[♪soft -2dB -100ms]59%は、[>#s6_b.seg2 -150ms][>#s6_b.lg[2] -100ms]待機電力と[>#s6_b.seg3 -150ms][>#s6_b.lg[3] -100ms]消し忘れ。[>#s6_b.brk -200ms][>#s6_b.brk_l -50ms][♪ping -2dB]止められる電気です。[silence:0.45s]
[<#s6_bg -20ms][<#s6_glow -20ms]

*** s8
se swish -3dB +20ms
@n: [silence:0.4s][chap #chap.ch[5] #chap.ch[6] 439 75 -350ms]試算では、[>#s8_c1 -350ms][♪pop -3dB]設定温度の1℃見直しで年[>#s8_c1.res -400ms][>#s8_c1.kwh -280ms]51.5万円、[|][>#s8_c2 -350ms][♪pop -3dB]待機と消し忘れ対策で[>#s8_c2.res -400ms][>#s8_c2.kwh -280ms]142.8万円、[|][>#s8_c3 -350ms][♪pop -3dB]LED化で[>#s8_c3.res -400ms][>#s8_c3.kwh -280ms]148.2万円。[silence:0.28s]

*** s9
se swish -3dB +20ms
se rise -3.5dB +350ms
@n: [silence:0.3s]合わせて年[>#s9_total -500ms][♪ping -1dB]342.5万円、[|]電気代の[>#s9_total.pct -200ms][>#s9_total.flow +400ms][>#s9_total.kwh +550ms]29%を減らせます。[silence:0.43s]

*** s10
se swish -3dB +20ms
se multi -3dB +450ms
@n: [silence:0.35s][chap #chap.ch[6] #chap.ch[7] 517 87 -300ms]まずは[>#s10_r2 -300ms][♪multi -3dB]工事のいらない対策から始めれば、年[!#s10_r2 glow,#0E9F6E42 {blur: 29}][>#s10_r2.first +100ms]194万円。[>#s10_r3 -300ms][♪multi -3dB]LED化の工事費も、[>#s10_src +500ms]6.5年で回収できます。[silence:0.25s][!#s10_r1 dim {opacity: .45, duration: .6}][!#s10_r3 dim {opacity: .45, duration: .6}][!#s10_r2 to,{scale:1.025, duration:0.6, ease:'power2.out'}][!#s10_r2.first punch {scale: 1.12, duration: .7} +100ms][♪title +100ms][silence:2.05s]
```

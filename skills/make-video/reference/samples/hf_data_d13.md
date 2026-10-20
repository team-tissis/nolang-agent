# data · office-electricity (hf 全力版の全量の写し — オフィスの電気代、どこに消えている？・明るい格子の地に白い板と図を場面ごとに組む 9 場面のデータ図解) — canvas 1280x720

見せる作り: 全編の地 (淡い緑灰 + 点の格子 + 角の 2 つの光) と下端の進行線・2 場面目から常設の上端の帯 (社名の札 + 7 章の札と場面の頭で滑って伸びる緑の指示子)・場面 = 番号札つきの小見出し + 題 + 白い板 (板の def)・数字の語で動く図 (数え上がる 4 枚の数字の札・12 本の月の棒を語で塗り最少の破線とかぎと倍率の札・時計回りに描く 4 弧のドーナツと太る空調の弧・語で伸びるピークの横棒 4 本と注記の板・円で開く紺の夜の場面で 3 枚のガラスの板から内訳の 3 色の帯とかぎへ組み替え・3 枚の対策の札・滝の図と合計の板)・まとめの 3 行を語で入れ、締めの間で 1 と 3 を沈めて 2 を大きく・字幕は濃い半透明の札・音の層 (場面の境のシュワッ + 語に結んだ電子のチャイム 30 余)

```design.txt
#v2
# 学ぶ作り: 明るい data の design system を根に 1 回 (palette・書体 4・場面の見出し sec / title の def・白い板 card の def・板の題と注記の def) → 場面は板の中の図だけ
# 常設の層: 全編の地 (淡い緑灰 + 点の格子 + 角の 2 つの光)・下端の進行線・2 場面目から sticky の上端の帯 (社名の札 + 7 章の札と、場面の頭で滑る緑の指示子)
# 図は数字の語と同時に動く: 12 本の月の棒 (語で 8 月と 1 月を塗る・最少の線とかぎと倍率の札)・4 弧のドーナツ (時計回りに描く)・ピークの横棒 4 本・夜の場面は円で開く紺の地と 2 段の板 (31% の帯 → 内訳の 3 色の帯とかぎ)・3 枚の対策の札・滝の図と合計の板・まとめの 3 行
# hf d13 office-electricity (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の退場は section の out (少し上へ抜けて消える)・切替は書かない (地は常設なので素の切替)
canvas 1280x720 bg=#F3F6F5
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
# hf の作り: 台詞の「8月」「1月」は依頼の数字の語のまま (読みは後段の読み検査が直す)
lint off=month_reading
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
run em = color=$green_d
run uem = color=$green_d marker=#0E9F6E38,22%
run mi = color=$mint
run u = size=0.65em
run nn = font=n
run pc = size=0.56em
run s = size=0.67em font=m
run s2 = size=0.63em font=m
run s3 = size=0.48em font=m color=$ink2
run s4 = size=0.61em font=m color=#D9E2F5
# 章の札の切替: 緑の指示子が次の章札へ滑って章札の幅に伸び、前の章の文字を灰に・新しい章の文字を白に
cue chap(a, b, l, w) = [!#chap.ind to,left={l},w={w},duration=500,ease=power3.inOut][!#a recolor,$muted,duration=300 +50][!#b recolor,#FFFFFF,duration=300 +200]
svg leaf = """<svg viewBox="0 0 24 24"><path d="M20 4C11 4 5 8.5 5 15c0 1.6.4 3 1 4.2C8 14 12 10.5 16 9c-3.5 2.5-6.6 6-8.3 10.6C9 20.5 10.5 21 12 21c6 0 8.5-6.5 8-17z" fill="#FFFFFF"/></svg>"""
p { color: $ink }
div { border-radius: 0px; background: none; padding: 0px; border: none; box-shadow: none }
# 字幕: 下端中央の濃い半透明の札・白の中字・句末の約物は外す・札 = 文 ([|] で句に切る)
subtitle.hug(bottom: 28px; font-size: 25px; line-height: 1.35; letter-spacing: 0.03em; color: #FFFFFF; font-family: m; background: #0F1C24DB; border-radius: 9px; padding: 8px 24px 9px 24px; unit: sentence; strip: 、。; lead: 60; tail: 250; hold: off; in: {y:5, opacity:0, duration:0.18, ease:'power1.out'})
# 曲: 声の無い頭と締めだけ前に出し、台詞の間は下げる
bgm#music(keys: "0:+6|500ms:+6|1000ms:0|end-2.3s:0|end-1.7s:+6"; fade: 500,1900) シンコペーションの効いた軽快なピアノのリズムに一定の電子ビートと温かいシンセパッドを重ねた、明るくモダンで主張しすぎない企業の解説向けの曲

# 場面の見出し: 緑の番号札 + 小見出し (上) と 37 px の題 (下)・場面の頭に下から入る
def sec(n, l, c=$green_d, nc=#FFFFFF) = div(left: 80px; top: 75px; width: 600px; height: 22px; delay: 60; in: {y:15, opacity:0, duration:0.6, ease:'power3.out'})
  p#n(left: 0px; cy: 50%; font-size: 15px; font-family: n; color: {nc}; background: {c}; border-radius: 5px; padding: 2px 7px; content: {n})
  p#l(left: .n.right+9; cy: 50%; font-size: 16px; letter-spacing: 0.08em; color: {c}; content: {l})
def title(t, c=$ink) = p(left: 80px; cy: 123px; font-size: 37px; line-height: 1.25; letter-spacing: 0.01em; color: {c}; delay: 160; in: {y:15, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-7, opacity:0, duration:0.3, ease:'power2.in'}; content: {t})
# 白い板 (細い縁 + 柔らかい影)・場面の頭に下から入る
def card = div(background: #FFFFFF; border: 1px solid #E0E8E5; border-radius: 16px; box-shadow: 0px 9px 23px #13222B12; delay: 140; in: {y:24, opacity:0, duration:0.6, ease:'power3.out'})
def ctitle(t) = p(left: 27px; cy: 32px; font-size: 20px; content: {t})
def cnote(t) = p(left: 27px; cy: 58px; font-size: 13px; color: $muted; font-family: m; content: {t})

# 全編の地 (根): 淡い緑灰に点の格子・右上に緑・左下に青の淡い光
div#bg_base(inset: 0; background: #F3F6F5; pattern: dots,21,#13222B12,0.8; z-index: back; in: none)
div#glow1(inset: 0; background: radial(#0E9F6E1A,#0E9F6E00@34%,88%,8%); z-index: back; in: none)
div#glow2(inset: 0; background: radial(#2FA4E717,#2FA4E700@32%,6%,96%); z-index: back; in: none)
# 下端の進行線 (全編で左から伸びる)
div#prog_track(left: 0px; top: 716px; width: 1280px; height: 4px; background: #13222B14; z-index: front; in: none)
progress#prog(left: 0px; top: 716px; width: 1280px; height: 4px; background: $green; until: end; z-index: front; overlap: prog_track)

# s1 題: 右に昼のオフィスの等角図が浮き上がり、左に小札 → 2 行の題 (「消えている」の下に緑の帯) → 出典 → 3 つの数字の札
section#s1(stagger: {each:0}; out: {y:-20, opacity:0, duration:0.3, ease:'power2.in'})
div#s1_b1(left: 673px; top: 100px; width: 547px; height: 547px; border-radius: 999px; background: radial(#0E9F6E29,#0E9F6E00@68%); in: none)
div#s1_b2(left: 827px; top: 60px; width: 347px; height: 347px; border-radius: 999px; background: radial(#2FA4E724,#2FA4E700@68%); in: none)
img#s1_hero(left: 620px; top: 153px; width: 640px; height: 427px; fit: contain; main: kb {scale: [1, 1.05]}; delay: 100; in: {y:40, scale:0.96, opacity:0, duration:1, ease:'power3.out'}) [transparent]明るい現代的なオープンオフィスの 1 フロアを斜め上 30 度から見下ろした等角図の切り抜き。白い机が並びモニターとノートPC、天井の LED 照明パネル、壁掛けのエアコン、複合機、小さなサーバーラック、観葉植物、昼の光が入る大きな窓。顔のない小さな人が働いている。宙に浮いた 1 枚のフロアのブロックで、枠いっぱいに大きく描く。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
div#s1_kicker(left: 80px; top: 167px; width: 240px; height: 31px; border-radius: 99px; background: $green_l; delay: 150; in: {y:13, opacity:0, duration:0.6, ease:'power3.out'})
  icon#i(left: 9px; cy: 50%; font-size: 19px; name: lightning; weight: fill; color: $green_d)
  p#t(left: 33px; cy: 50%; font-size: 17px; letter-spacing: 0.06em; color: $green_d) 社内向け 電力データ分析
p#s1_l1(left: 80px; top: 224px; font-size: 61px; font-family: h; line-height: 1.22; letter-spacing: 0.01em; delay: 300; in: {y:27, opacity:0, duration:0.7, ease:'power3.out'}) オフィスの電気代、
p#s1_l2(left: 80px; top: 299px; font-size: 61px; font-family: h; line-height: 1.22; letter-spacing: 0.01em; delay: 500; in: {y:27, opacity:0, duration:0.7, ease:'power3.out'}) どこに{uem}消えている{/}？
p#s1_sub(left: 83px; cy: 406px; font-size: 19px; color: $ink2; font-family: m; delay: 1000; in: {y:11, opacity:0, duration:0.6, ease:'power3.out'}) 株式会社ミドリノ設計　昨年度（4月〜3月）の電力データより
div#s1_chip(left: "80;214;374"; top: 467px; width: "122;148;186"; height: 47px; border-radius: 11px; background: #FFFFFF; border: 1px solid #DFE7E4; box-shadow: 0px 5px 15px #13222B0F; delay: 1300; in: {y:13, opacity:0, duration:0.6, ease:'power3.out', stagger:{each:0.12}}) ×3
  p#k(left: 16px; cy: 50%; font-size: 13px; color: $muted; font-family: m) 社員;延床;30分値
  p#v(left: .k.right+7; cy: 50%; font-size: 23px; font-family: n; letter-spacing: -0.02em) 200{u}人{/};2,400{u}m²{/};17,520{u}コマ{/}

# s2 分析の概要: 上端の帯が降りる・左の板にメーターの絵と 3 行・「分析」で 3 枚の数字の札が数え上がり、「1171」で緑の主役の札が数えて光る
section#s2(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
# 上端の帯 (sticky・最後まで): 左の社名の札・右の 7 章の札 (緑の指示子が場面の頭で滑り、文字が白に替わる)
div#brand.sticky(left: 80px; top: 23px; width: 260px; height: 33px; border-radius: 17px; background: #FFFFFFF0; border: 1px solid #DFE7E4; z-index: front; delay: 50; in: {y:-13, opacity:0, duration:0.6, ease:'power3.out'})
  div#logo(left: 6px; cy: 50%; width: 23px; height: 23px; border-radius: 99px; background: $green)
    svg#leaf(cx: 50%; cy: 50%; width: 13px; height: 13px; part: leaf)
  p#b(left: 37px; cy: 50%; font-size: 13px) ミドリノ設計
  div#sep(left: .b.right+8; cy: 50%; width: 1px; height: 13px; background: #CFD9D6)
  p#s(left: .sep.right+8; cy: 50%; font-size: 13px; color: $ink2; font-family: m) オフィス電力レポート
# hf の作り: 指示子が次の章へ滑る間、前の章の文字を灰に戻す (滑り終えるまで灰の字が緑の上に一瞬乗る — check の low_contrast)
div#chap.sticky(left: 593px; top: 23px; width: 607px; height: 33px; border-radius: 17px; background: #FFFFFFF0; border: 1px solid #DFE7E4; z-index: front; delay: 130; in: {y:-13, opacity:0, duration:0.6, ease:'power3.out'})
  div#ind(left: 3px; top: 3px; width: 75px; height: 25px; border-radius: 13px; background: $green_d)
  p#ch(left: "3;81;158;235;325;439;517"; cy: 50%; width: "75;75;75;87;112;75;87"; font-size: 12px; text-align: center; color: "#FFFFFF;$muted;$muted;$muted;$muted;$muted;$muted") ×7 01 概要;02 月別;03 用途;04 ピーク;05 夜間・休日;06 対策;07 まとめ
sec#s2_sec(n: "01"; l: "分析の概要")
title#s2_title 1年分の30分値で、電気の行き先を追う
card#s2_method(left: 80px; top: 179px; width: 413px; height: 421px; delay: 160)
  img#pic(left: 127px; top: 15px; width: 160px; height: 160px; fit: contain; main: sine {y: -5, period: 3.4}) [transparent]白い四角いスマートメーターの箱 1 台、小さな空の液晶と無線の印、その横に抽象的な棒グラフを挟んだクリップボード。斜め前から見た 3/4 の構図、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#row(left: 27px; top: "187;259;331"; width: 360px; height: 72px; delay: 800; in: {y:11, opacity:0, duration:0.6, ease:'power3.out', stagger:{each:0.18}}) ×3
    div#ln(left: 0px; top: 0px; width: 360px; height: 1px; background: $line)
    p#k(left: 0px; cy: 27px; font-size: 15px; color: $green_d) データ;突き合わせ;対象
    p#v(left: 101px; cy: 26px; font-size: 17px; font-family: m) スマートメーターの30分値;フロア別・系統別の子メーター;社員200人・延床2,400m²
    p#s(left: 101px; cy: 48px; font-size: 13px; color: $muted; font-family: m) 30分ごと × 1年分 ＝ 17,520コマ;どの用途・時間帯で使ったかを特定;期間：昨年度（4月〜3月）
# 数字の札 (題 + 数え上がる数字 + 単位 + 注記)
def kpi(l, v, u, f) = div(width: 333px; height: 204px; background: #FFFFFF; border: 1px solid #E0E8E5; border-radius: 16px; box-shadow: 0px 9px 23px #13222B12; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  p#l(left: 24px; cy: 33px; font-size: 17px; color: $ink2; content: {l})
  p#v(left: 23px; cy: 91px; font-size: 60px; line-height: 1; font-family: n; letter-spacing: -0.02em; content: {v})
  p#u(left: .v.right+7; cy: 106px; font-size: 21px; color: $ink2; content: {u})
  p#f(left: 24px; cy: 174px; font-size: 14px; color: $muted; font-family: m; content: {f})
kpi#s2_k1(left: 520px; top: 179px; l: "年間の使用量"; v: "[count:384,000 start=0 ms=1200 delay=100]"; u: "kWh"; f: "スマートメーター30分値の年間合計")
kpi#s2_k3(left: 520px; top: 396px; l: "平均単価"; v: "[count:30.5 start=0 ms=1000 delay=240]"; u: "円/kWh"; f: "電気代 ÷ 使用量")
kpi#s2_k4(left: 867px; top: 396px; l: "社員1人あたり"; v: "[count:5.9 start=0 ms=1000 delay=280]"; u: "万円/年"; f: "1,171万円 ÷ 200人")
# 主役の札: 緑の縁と縦の淡いグラデ・左端の緑の短い棒・数字は緑
kpi#s2_k2(left: 867px; top: 179px; l: "年間の電気代"; v: "[count:1,171 start=0 ms=1100 delay=100]"; u: "万円"; f: "昨年度（4月〜3月）の実績"; background: linear(#F2FBF7,#FFFFFF@60%,180); border: 2px solid $green; in: {y:20, scale:0.96, opacity:0, duration:0.6, ease:'power3.out'})
  p#v(color: $green_d)
  div#bar(left: 0px; top: 20px; width: 5px; height: 27px; border-radius: 0px 4px 4px 0px; background: $green)

# s3 月別: 12 本の灰の棒が左から順に伸び、語で 8 月を橙・1 月を青に塗って値の札・「5月」で最少の札と破線・「1.7」でかぎと倍率の黒札
section#s3(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
sec#s3_sec(n: "02"; l: "月別の使用量")
title#s3_title 山は{em}夏（8月）{/}と{em}冬（1月）{/}の2つ
card#s3_card(left: 80px; top: 175px; width: 1120px; height: 427px)
  ctitle#t 月別の電力使用量
  cnote#n 単位：千kWh　※スマートメーター30分値の月合計（年間 384,000 kWh）
  # 凡例 (右上・色の四角 + 語)
  div#leg(left: "675;812;953"; cy: 32px; width: "130;130;95"; height: 15px) ×3
    div#sw(left: 0px; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: "$summer;$winter;$base")
    p#t(left: 18px; cy: 50%; font-size: 13px; color: $ink2; font-family: m) 夏のピーク（8月）;冬のピーク（1月）;その他の月
  # 目盛り (0〜40 千kWh = 213 px) と月の札
  div#gl(left: 80px; top: "340.7;287.3;234;180.7;127.3"; width: 1013px; height: 1px; background: $grid) ×5
  p#gn(left: 33px; cy: "341;288;235;181;128"; width: 37px; text-align: right; font-size: 13px; color: $muted; font-family: m) ×5 0;10;20;30;40
  div#bar(left: "96.9;181.3;265.8;350.2;434.7;519.1;603.5;688;772.4;856.9;941.3;1025.7"; top: "202.7;205.9;182.4;135.5;115.2;159.5;196.3;200;176;151.5;158.9;164.3"; width: 51px; height: "138.7;135.5;158.9;205.9;226.1;181.9;145.1;141.3;165.3;189.9;182.4;177.1"; border-radius: 4px; background: $base; delay: 550; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom', stagger:{each:0.06}}) ×12
  p#mo(left: "88.9;173.3;257.8;342.2;426.7;511.1;595.6;680;764.4;848.9;933.3;1017.8"; cy: 360px; width: 67px; text-align: center; font-size: 15px; color: $ink2; font-family: m) ×12 4月;5月;6月;7月;8月;9月;10月;11月;12月;1月;2月;3月
  # 季節の帯 (軸の下の色の線 + 語)
  div#season(left: "337.3;759.6"; top: 377px; width: "245.3;329.8"; height: 24px) ×2
    div#ln(left: 0px; top: 0px; width: 100%; height: 3px; background: "$summer;$winter")
    p#t(cx: 50%; cy: 14px; font-size: 13px; color: "#A2481B;#0B5C8A") 夏（7〜9月）;冬（12〜3月）
  # 値の札 (語で弾む)
  p#lab_aug_t(left: 420px; cy: 81px; width: 80px; text-align: center; font-size: 12px; color: $muted; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 最大
  p#lab_aug(left: 420px; cy: 101px; width: 80px; text-align: center; font-size: 21px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 42.4
  p#lab_jan(left: 842px; cy: 135px; width: 80px; text-align: center; font-size: 21px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 35.6
  p#lab_may_t(left: 167px; cy: 172px; width: 80px; text-align: center; font-size: 12px; color: $muted; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 最少
  p#lab_may(left: 167px; cy: 192px; width: 80px; text-align: center; font-size: 21px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 25.4
  # 5 月の水準の破線と 8 月までのかぎ・倍率の黒札
  shape#ref(path: "M233.3 206.2 L490.7 206.2"; background: none; border: 2px solid #4C5D64; dash: 6,4; in: draw {duration: 0.6})
  shape#brk(path: "M489.3 115.2 L494.7 115.2 Q500 115.2 500 120.5 L500 200.5 Q500 205.9 494.7 205.9 L489.3 205.9"; background: none; border: 2px solid $ink; in: draw {duration: 0.45})
  p#ratio(left: 507px; cy: 129px; font-size: 20px; font-family: n; color: #FFFFFF; background: $ink; border-radius: 8px; padding: 4px 11px; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2.2)'}) {s}5月の{/}1.7倍

# s4 用途別: ドーナツの 4 弧が時計回りに描かれ、右に 4 行の凡例・「空調」で空調の行に青い地と弧が太る・「半分」で青い札
section#s4(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
sec#s4_sec(n: "03"; l: "用途別の構成")
title#s4_title {em}空調{/}だけで44%、半分近くを占める
card#s4_card(left: 80px; top: 175px; width: 1120px; height: 427px)
  ctitle#t 用途別の内訳（年間の電気代）
  cnote#n 合計 1,171万円＝100%
  # ドーナツ (中心 273,237・半径 133・太さ 51・弧の間 1.1°・角の端)。弧は塗りの扇形 (外の弧 + 内の弧を Z で閉じる)・頭の 2 点で箱をドーナツ全体の正方形にし、12 時から時計回りの clock_wipe を弧ごとの delay と速さで hf の順の描き出しに合わせる
  shape#seg1(path: "M114,78 M432,396 M273.0,78.3 L278.5,78.4 L284.0,78.7 L289.5,79.2 L295.0,79.9 L300.4,80.7 L305.8,81.8 L311.2,83.0 L316.5,84.4 L321.8,86.0 L327.0,87.8 L332.2,89.8 L337.2,91.9 L342.2,94.2 L347.2,96.7 L352.0,99.4 L356.7,102.2 L361.4,105.2 L365.9,108.4 L370.3,111.7 L374.6,115.1 L378.8,118.7 L382.8,122.5 L386.7,126.3 L390.5,130.4 L394.1,134.5 L397.6,138.8 L400.9,143.2 L404.1,147.7 L407.2,152.3 L410.0,157.0 L412.7,161.8 L415.2,166.7 L417.6,171.7 L419.8,176.7 L421.8,181.9 L423.6,187.1 L425.3,192.3 L426.7,197.7 L428.0,203.0 L429.1,208.4 L430.0,213.9 L430.7,219.3 L431.2,224.8 L431.5,230.3 L431.7,235.8 L431.6,241.3 L431.4,246.8 L430.9,252.3 L430.3,257.8 L429.5,263.3 L428.5,268.7 L427.3,274.1 L425.9,279.4 L424.3,284.7 L422.6,289.9 L420.7,295.1 L418.5,300.2 L416.3,305.2 L413.8,310.1 L411.2,315.0 L408.4,319.7 L405.4,324.4 L402.3,328.9 L399.1,333.4 L395.6,337.7 L392.1,341.9 L388.3,346.0 L384.5,349.9 L380.5,353.7 L376.4,357.4 L372.1,360.9 L367.8,364.2 L363.3,367.5 L358.7,370.5 L354.0,373.4 L349.2,376.2 L344.4,378.7 L339.4,381.1 L334.3,383.3 L314.8,336.6 L318.2,335.1 L321.6,333.5 L324.9,331.7 L328.2,329.9 L331.3,327.9 L334.5,325.8 L337.5,323.6 L340.5,321.3 L343.4,318.9 L346.2,316.4 L348.9,313.8 L351.5,311.2 L354.0,308.4 L356.5,305.5 L358.8,302.6 L361.0,299.6 L363.1,296.5 L365.2,293.3 L367.1,290.1 L368.8,286.8 L370.5,283.4 L372.1,280.0 L373.5,276.5 L374.8,273.0 L376.0,269.5 L377.1,265.9 L378.0,262.2 L378.8,258.6 L379.5,254.9 L380.1,251.2 L380.5,247.4 L380.8,243.7 L381.0,240.0 L381.0,236.2 L380.9,232.4 L380.7,228.7 L380.3,225.0 L379.8,221.2 L379.2,217.5 L378.5,213.9 L377.6,210.2 L376.6,206.6 L375.5,203.0 L374.3,199.5 L372.9,196.0 L371.4,192.5 L369.8,189.1 L368.1,185.8 L366.3,182.5 L364.3,179.3 L362.3,176.2 L360.1,173.1 L357.8,170.1 L355.4,167.2 L353.0,164.4 L350.4,161.7 L347.7,159.0 L345.0,156.5 L342.1,154.0 L339.2,151.7 L336.2,149.4 L333.1,147.3 L330.0,145.3 L326.8,143.3 L323.5,141.5 L320.1,139.8 L316.7,138.3 L313.3,136.8 L309.8,135.5 L306.2,134.2 L302.6,133.1 L299.0,132.2 L295.3,131.3 L291.7,130.6 L288.0,130.0 L284.2,129.6 L280.5,129.3 L276.8,129.1 L273.0,129.0 Z"; background: $ac; delay: 600; in: clock_wipe {duration: 1.68, ease: 'none', dir: 'right'})
  # 空調の弧が 76 → 94 px に弾んで太る hf の動きは、太い扇形 (内 102・外 165) を重ねて溶かして出す (描き終わる前に全長が見えないよう印は語の +200)
  shape#seg1w(path: "M108,72 M438,402 M273.0,72.3 L278.7,72.4 L284.4,72.7 L290.1,73.2 L295.8,73.9 L301.5,74.8 L307.1,75.9 L312.7,77.2 L318.2,78.7 L323.7,80.3 L329.1,82.2 L334.4,84.2 L339.7,86.4 L344.9,88.8 L350.0,91.4 L355.0,94.2 L359.9,97.1 L364.7,100.2 L369.4,103.5 L374.0,106.9 L378.4,110.5 L382.8,114.2 L387.0,118.1 L391.0,122.2 L394.9,126.3 L398.7,130.6 L402.3,135.1 L405.8,139.6 L409.1,144.3 L412.2,149.1 L415.2,154.0 L418.0,159.0 L420.6,164.0 L423.1,169.2 L425.3,174.5 L427.4,179.8 L429.3,185.2 L431.0,190.6 L432.5,196.2 L433.8,201.7 L435.0,207.3 L435.9,213.0 L436.6,218.7 L437.2,224.3 L437.5,230.1 L437.7,235.8 L437.6,241.5 L437.3,247.2 L436.9,252.9 L436.2,258.6 L435.4,264.3 L434.4,269.9 L433.1,275.5 L431.7,281.0 L430.1,286.5 L428.2,291.9 L426.2,297.3 L424.1,302.6 L421.7,307.8 L419.1,312.9 L416.4,317.9 L413.5,322.9 L410.4,327.7 L407.2,332.4 L403.8,337.0 L400.3,341.5 L396.6,345.8 L392.7,350.1 L388.7,354.2 L384.6,358.1 L380.3,361.9 L375.9,365.6 L371.4,369.1 L366.7,372.4 L362.0,375.6 L357.1,378.6 L352.1,381.4 L347.1,384.1 L341.9,386.6 L336.7,388.9 L312.4,331.1 L315.7,329.6 L318.9,328.1 L322.0,326.5 L325.1,324.7 L328.1,322.8 L331.1,320.9 L333.9,318.8 L336.7,316.6 L339.5,314.4 L342.1,312.0 L344.7,309.6 L347.2,307.0 L349.5,304.4 L351.8,301.7 L354.0,298.9 L356.1,296.1 L358.1,293.2 L360.0,290.2 L361.8,287.1 L363.5,284.0 L365.1,280.8 L366.6,277.6 L367.9,274.3 L369.2,271.0 L370.3,267.7 L371.3,264.3 L372.2,260.8 L372.9,257.4 L373.6,253.9 L374.1,250.4 L374.5,246.9 L374.8,243.3 L375.0,239.8 L375.0,236.2 L374.9,232.7 L374.7,229.2 L374.4,225.6 L373.9,222.1 L373.3,218.6 L372.6,215.2 L371.8,211.7 L370.9,208.3 L369.8,204.9 L368.6,201.6 L367.4,198.3 L366.0,195.0 L364.4,191.8 L362.8,188.7 L361.1,185.6 L359.2,182.5 L357.3,179.6 L355.3,176.7 L353.1,173.9 L350.9,171.1 L348.5,168.4 L346.1,165.9 L343.6,163.4 L341.0,161.0 L338.3,158.6 L335.5,156.4 L332.7,154.3 L329.8,152.3 L326.8,150.4 L323.8,148.5 L320.7,146.8 L317.5,145.2 L314.3,143.7 L311.0,142.4 L307.7,141.1 L304.4,139.9 L301.0,138.9 L297.6,138.0 L294.1,137.2 L290.6,136.5 L287.1,136.0 L283.6,135.6 L280.1,135.2 L276.5,135.1 L273.0,135.0 Z"; background: $ac; in: {opacity:0, duration:0.5, ease:'power2.out'})
  shape#seg2(path: "M114,78 M432,396 M331.4,384.5 L326.3,386.4 L321.1,388.2 L315.9,389.8 L310.6,391.2 L305.2,392.4 L299.9,393.4 L294.5,394.2 L289.0,394.9 L283.6,395.3 L278.1,395.6 L272.7,395.7 L267.2,395.6 L261.7,395.3 L256.3,394.8 L250.9,394.1 L245.5,393.3 L240.1,392.2 L234.8,391.0 L229.5,389.6 L224.3,388.0 L219.1,386.2 L214.0,384.3 L208.9,382.2 L204.0,379.9 L199.1,377.4 L194.3,374.8 L189.6,372.0 L185.0,369.0 L180.5,365.9 L176.1,362.6 L171.8,359.2 L167.7,355.7 L163.7,352.0 L159.8,348.1 L156.0,344.2 L152.4,340.1 L148.9,335.9 L145.6,331.5 L142.4,327.1 L139.4,322.5 L136.5,317.9 L133.8,313.1 L131.2,308.3 L128.9,303.4 L126.7,298.3 L173.4,278.8 L174.9,282.2 L176.5,285.5 L178.2,288.8 L180.1,292.0 L182.0,295.2 L184.1,298.3 L186.3,301.3 L188.5,304.3 L190.9,307.2 L193.4,310.0 L195.9,312.7 L198.6,315.3 L201.3,317.8 L204.1,320.2 L207.1,322.5 L210.0,324.7 L213.1,326.9 L216.2,328.9 L219.4,330.8 L222.7,332.6 L226.0,334.2 L229.4,335.8 L232.8,337.2 L236.3,338.6 L239.8,339.8 L243.4,340.9 L247.0,341.8 L250.6,342.7 L254.3,343.4 L257.9,343.9 L261.6,344.4 L265.3,344.7 L269.1,344.9 L272.8,345.0 L276.5,344.9 L280.2,344.8 L283.9,344.4 L287.6,344.0 L291.3,343.4 L295.0,342.7 L298.6,341.9 L302.2,341.0 L305.7,339.9 L309.3,338.7 L312.8,337.4 Z"; background: $oa; delay: 398; in: clock_wipe {duration: 2.127, ease: 'none', dir: 'right'})
  shape#seg3(path: "M114,78 M432,396 M125.5,295.4 L123.5,290.2 L121.8,285.0 L120.2,279.7 L118.8,274.4 L117.6,269.0 L116.6,263.6 L115.7,258.1 L115.1,252.7 L114.7,247.2 L114.4,241.7 L114.3,236.1 L114.5,230.6 L114.8,225.1 L115.3,219.6 L116.0,214.2 L116.9,208.7 L117.9,203.3 L119.2,197.9 L120.7,192.6 L122.3,187.4 L124.1,182.2 L126.1,177.0 L128.3,171.9 L130.6,167.0 L133.2,162.0 L135.8,157.2 L138.7,152.5 L141.7,147.9 L144.9,143.4 L148.2,139.0 L151.7,134.7 L155.3,130.6 L159.1,126.5 L163.0,122.6 L167.0,118.9 L171.2,115.3 L175.5,111.8 L179.9,108.5 L184.4,105.3 L189.1,102.4 L193.8,99.5 L219.1,143.4 L215.9,145.3 L212.7,147.4 L209.6,149.5 L206.6,151.8 L203.7,154.2 L200.9,156.6 L198.1,159.2 L195.5,161.8 L192.9,164.6 L190.4,167.4 L188.1,170.3 L185.8,173.3 L183.6,176.4 L181.6,179.5 L179.6,182.7 L177.8,186.0 L176.1,189.3 L174.5,192.7 L173.0,196.2 L171.7,199.7 L170.4,203.2 L169.3,206.8 L168.3,210.4 L167.5,214.1 L166.7,217.8 L166.1,221.5 L165.6,225.2 L165.3,228.9 L165.1,232.7 L165.0,236.4 L165.0,240.2 L165.2,243.9 L165.5,247.7 L166.0,251.4 L166.5,255.1 L167.2,258.8 L168.0,262.5 L169.0,266.1 L170.1,269.7 L171.3,273.2 L172.6,276.8 Z"; background: $lighting; delay: 329; in: clock_wipe {duration: 2.218, ease: 'none', dir: 'right'})
  shape#seg4(path: "M114,78 M432,396 M196.6,98.0 L201.4,95.4 L206.3,93.0 L211.3,90.8 L216.4,88.8 L221.5,86.9 L226.7,85.2 L232.0,83.7 L237.3,82.4 L242.7,81.3 L248.1,80.3 L253.5,79.5 L258.9,79.0 L264.4,78.6 L269.8,78.4 L270.8,129.0 L267.1,129.2 L263.4,129.4 L259.7,129.8 L256.0,130.3 L252.4,131.0 L248.7,131.8 L245.1,132.7 L241.5,133.7 L238.0,134.8 L234.5,136.1 L231.0,137.5 L227.6,139.0 L224.3,140.6 L221.0,142.4 Z"; background: $other; delay: 0; in: clock_wipe {duration: 2.709, ease: 'none', dir: 'right'})
  p#c_l(cx: 273px; cy: 214px; font-size: 15px; color: $muted; delay: 900; in: {y:7, opacity:0, duration:0.6, ease:'power3.out'}) 年間の電気代
  p#c_v(cx: 273px; cy: 248px; font-size: 43px; font-family: n; letter-spacing: -0.02em; delay: 900; in: {y:7, opacity:0, duration:0.6, ease:'power3.out'}) 1,171{s2}万円{/}
  # 凡例の 4 行 (色の四角・名と説明・% と金額)・空調の行だけ淡い青の地 (語で出す)
  div#row(left: 533px; top: "80;160;240;320"; width: 560px; height: 75px; border-radius: 12px; delay: 750; in: {x:20, opacity:0, duration:0.6, ease:'power3.out', stagger:{each:0.14}}) ×4
    div#hl(inset: 0; border-radius: 12px; background: #EEF3FD; border: 2px solid #C8D8F7; opacity: "1;0;0;0"; in: {opacity:0, duration:0.4})
    div#sw(left: 19px; top: 27px; width: 20px; height: 20px; border-radius: 5px; background: "$ac;$oa;$lighting;$other")
    p#name(left: 53px; cy: 30px; font-size: 23px) 空調;OA機器;照明;その他
    p#desc(left: 55px; cy: 56px; font-size: 13px; color: $muted; font-family: m) 冷房・暖房;PC・複合機・モニターなど;現在は蛍光灯;給湯・エレベーター・冷蔵庫など
    p#pct(right: 173px; cy: 37px; font-size: 43px; font-family: n; letter-spacing: -0.02em) 44{pc}%{/};25{pc}%{/};23{pc}%{/};8{pc}%{/}
    p#yen(right: 20px; cy: 38px; font-size: 25px; font-family: n; color: $ink2) 515{s2}万円{/};293{s2}万円{/};269{s2}万円{/};94{s2}万円{/}
  p#badge(left: 707px; cy: 80px; font-size: 15px; color: #FFFFFF; background: $ac; border-radius: 13px; padding: 4px 11px; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 半分近く

# s5 ピーク: 縦の目盛りの上に横棒 4 本 (夏 → 冬 → 平日昼 → 夜間) を語で伸ばし、値の札が弾む・「暖房」で右に朝 9:00 の注記の板・「朝」で板の縁が脈打つ
section#s5(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
sec#s5_sec(n: "04"; l: "ピーク電力")
title#s5_title 冬の山は、{em}始業時の朝{/}に来る
card#s5_card(left: 80px; top: 175px; width: 1120px; height: 427px)
  ctitle#t 30分値の最大と平均
  cnote#n 単位：kW（30分ごとの平均電力）
  # 縦の目盛り (0〜200 kW = 507 px) と区切りの破線
  div#gl(left: "313.3;440;566.7;693.3;820"; top: 85px; width: 1px; height: 287px; background: $grid) ×5
  p#gn(left: "294.7;421.3;548;674.7;801.3"; cy: 386px; width: 37px; text-align: center; font-size: 13px; color: $muted; font-family: m) ×5 0;50;100;150;200
  p#gu(left: 837px; cy: 386px; font-size: 13px; color: $muted; font-family: m) kW
  shape#div(path: "M26.7 234 L1093.3 234"; background: none; border: 1px solid $line; dash: 5,4)
# ピークの行 (丸い地の icon + 名 + 日時 + 棒 + 値)・行は左から入り、棒と値は語で
def prow(i, c, t, s, w, v, vl) = div(left: 80px; width: 1120px; height: 37px; in: {x:-13, opacity:0, duration:0.45, ease:'power3.out'})
  icon#ic(left: 27px; cy: 19px; font-size: 21px; padding: 8px; name: {i}; weight: bold; color: #FFFFFF; background: {c})
  p#nm(left: 75px; cy: 10px; font-size: 20px; content: {t})
  p#sb(left: 75px; cy: 33px; font-size: 15px; color: $muted; font-family: m; content: {s})
  div#bar(left: 313px; top: 2px; width: {w}; height: 33px; border-radius: 3px 7px 7px 3px; background: {c}; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
  p#val(left: {vl}; cy: 16px; font-size: 33px; font-family: n; letter-spacing: -0.02em; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2.2)'}; content: {v})
prow#s5_r1(i: sun; c: $summer; t: "夏のピーク"; s: "8月7日 14:30"; w: 471px; v: "186{s3}kW{/}"; vl: 795px; top: 260px)
prow#s5_r2(i: snowflake; c: $winter; t: "冬のピーク"; s: "1月23日 9:00"; w: 400px; v: "158{s3}kW{/}"; vl: 724px; top: 335px)
prow#s5_r3(i: briefcase; c: $avg; t: "平日昼の平均"; s: ""; w: 274px; v: "108{s3}kW{/}"; vl: 598px; top: 431px; height: 37px)
  icon#ic(cy: 13px; font-size: 17px; padding: 7px)
  p#nm(cy: 13px; font-size: 17px)
  div#bar(top: 0px; height: 24px)
  p#val(cy: 12px; font-size: 24px)
prow#s5_r4(i: moon; c: #26356B; t: "夜間・休日の平均"; s: "平日19時〜翌9時・休日"; w: 48px; v: "19{s3}kW{/}"; vl: 372px; top: 490px; height: 37px)
  icon#ic(cy: 13px; font-size: 17px; padding: 7px)
  p#nm(cy: 13px; font-size: 17px)
  p#sb(cy: 33px; font-size: 13px)
  div#bar(top: 0px; height: 24px)
  p#val(cy: 12px; font-size: 24px)
# 注記の板 (時計の icon + 青い題 + 2 行)
div#s5_call(left: 940px; top: 332px; width: 233px; height: 108px; border-radius: 12px; background: #EAF6FD; border: 2px solid #BFE3F7; in: {y:13, opacity:0, duration:0.6, ease:'power3.out'})
  icon#ic(left: 16px; cy: 28px; font-size: 20px; name: clock; weight: bold; color: #0B5C8A)
  p#h(left: 43px; cy: 28px; font-size: 19px; color: #0B5C8A) 冬の山は朝 9:00
  p#p(left: 16px; top: 47px; font-size: 15px; line-height: 1.5; font-family: m) 始業時に全フロアの[br]暖房が一斉に立ち上がる

# s6 夜間・休日: 紺の地が円で開き、夜のオフィスの等角図・右に 3 枚のガラスの板 (19 kW・31% と帯・363 万円) を語で → 「その」で板と題を払い、内訳の板 (3 色の帯が語で伸び、かぎと「止められる分 59%」)
section#s6(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
div#s6_bg(inset: 0; background: linear(#0F1D42,#0B1530@70%,160); pattern: dots,21,#FFFFFF0F,0.8; in: circle_wipe {duration: 0.75, ease: 'power2.inOut'}; out: iris_wipe {duration: 0.5, ease: 'power2.in'})
div#s6_glow(inset: 0; background: radial(#506EDC47,#506EDC00@45%,20%,30%); in: circle_wipe {duration: 0.75, ease: 'power2.inOut'}; out: iris_wipe {duration: 0.5, ease: 'power2.in'})
sec#s6_sec(n: "05"; l: "誰もいない時間の電気"; c: $mint; nc: $navy; delay: 400)
title#s6_ta(c: #FFFFFF; delay: 500) 夜と休日も、電気は{mi}ゼロにならない{/}
title#s6_tb(c: #FFFFFF; delay: 0) そのうち{mi}59%{/}は、止められる電気
img#s6_img(left: 40px; top: 175px; width: 640px; height: 427px; fit: contain; main: kb {scale: [1, 1.06]}; delay: 400; in: {x:-27, opacity:0, duration:0.9, ease:'power3.out'}) [transparent]夜の現代的なオープンオフィスの 1 フロアを斜め上 30 度から見下ろした等角図の切り抜き。人は誰もいない。深い紺と藍の夜の色調。待機中でかすかに光るモニターがいくつか、小さな待機ランプの灯る複合機、小さな緑のランプが点滅するサーバーラック、冷蔵庫、消し忘れで暖かい光を落とす天井の照明 1 列、動いたままのエアコン。宙に浮いた 1 枚のフロアのブロックで、枠いっぱいに大きく描く。静かで清潔
# ガラスの板 (白 7% の地 + 白 16% の細い縁)
def glass = div(left: 707px; width: 493px; border-radius: 15px; background: #FFFFFF12; border: 1px solid #FFFFFF29; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-8, opacity:0, duration:0.35, ease:'power2.in'})
def glab(t) = p(left: 21px; cy: 28px; font-size: 16px; color: #C9D4EE; content: {t})
glass#s6_a1(top: 175px; height: 131px)
  glab#l 夜間・休日の平均電力
  p#v(left: 20px; cy: 87px; font-size: 67px; line-height: 1; font-family: n; color: #FFFFFF; letter-spacing: -0.02em) [count:19 start=0 ms=800 delay=150]
  p#u(left: .v.right+7; cy: 104px; font-size: 21px; color: #D9E2F5) kW
  p#nt(left: 220px; top: 64px; font-size: 13px; line-height: 1.45; color: #B9C6E4; font-family: m) 夜間＝平日19時〜翌9時[br]休日＝終日
glass#s6_a2(top: 316px; height: 147px)
  glab#l 年間使用量に占める割合
  p#v(left: 20px; cy: 73px; font-size: 51px; line-height: 1; font-family: n; color: #FFFFFF; letter-spacing: -0.02em) [count:31 start=0 ms=900 delay=150]
  p#u(left: .v.right+7; cy: 84px; font-size: 21px; color: #D9E2F5) %
  p#nt(left: 167px; cy: 79px; font-size: 13px; color: #B9C6E4; font-family: m) 119,040 kWh ／ 384,000 kWh
  div#tr(left: 21px; top: 112px; width: 451px; height: 20px; border-radius: 10px; background: #FFFFFF1F)
  div#fill(left: 21px; top: 112px; width: 140px; height: 20px; border-radius: 10px; background: linear(#7C95FF,#A98CFF,90); in: {scaleX:0, duration:0.9, ease:'power3.out', pivot:'left'})
glass#s6_a3(top: 473px; height: 127px)
  glab#l 電気代にすると
  p#v(left: 20px; cy: 81px; font-size: 61px; line-height: 1; font-family: n; color: $mint; letter-spacing: -0.02em) [count:363 start=0 ms=1000 delay=150]
  p#u(left: .v.right+7; cy: 96px; font-size: 21px; color: $mint) 万円/年
# 内訳の板: 3 色の帯 (41 / 37 / 22%) が語ごとに左から伸び、止められる 2 つの上にかぎと緑の札・下に 3 行の凡例
glass#s6_b(top: 175px; height: 425px)
  p#hd(left: 21px; cy: 30px; font-size: 17px; color: #C9D4EE) 夜間・休日の電気 119,040 kWh の内訳
  div#seg1(left: 21.3px; top: 107px; width: 182.8px; height: 51px; border-radius: 8px 0px 0px 8px; background: $fixed; in: {scaleX:0, duration:0.5, ease:'power2.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 20px; font-family: n; color: $navy) 41%
  div#seg2(left: 206.1px; top: 107px; width: 164.7px; height: 51px; background: $standby; in: {scaleX:0, duration:0.45, ease:'power2.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 20px; font-family: n; color: $navy) 37%
  div#seg3(left: 372.8px; top: 107px; width: 99.1px; height: 51px; border-radius: 0px 8px 8px 0px; background: $forgot; in: {scaleX:0, duration:0.4, ease:'power2.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 20px; font-family: n; color: $navy) 22%
  shape#brk(path: "M206.1 100 L206.1 88 Q206.1 85.3 211.4 85.3 L466.6 85.3 Q472 85.3 472 88 L472 100"; background: none; border: 2px solid $mint; in: draw {duration: 0.4})
  p#brk_l(left: 260px; cy: 64px; font-size: 16px; font-family: n; color: $navy; background: $mint; border-radius: 11px; padding: 3px 11px; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2.2)'}) 止められる分 59%
  div#lg(left: 21px; top: "193.3;266.7;340"; width: 451px; height: 64px; in: {x:13, opacity:0, duration:0.45, ease:'power3.out'}) ×3
    div#ln(left: 0px; top: 0px; width: 451px; height: 1px; background: #FFFFFF24)
    div#sw(left: 0px; top: 20px; width: 17px; height: 17px; border-radius: 5px; background: "$fixed;$standby;$forgot")
    p#n(left: 29px; cy: 24px; font-size: 19px; color: #FFFFFF) 止められない分;待機電力;消し忘れ
    p#d(left: 30px; cy: 48px; font-size: 13px; color: #B9C6E4; font-family: m) サーバー・冷蔵庫など;PC・複合機・モニター;照明・空調
    p#tag(right: 127px; cy: 28px; font-size: 12px; color: $mint; background: #5FE3B529; border-radius: 8px; padding: 2px 8px; opacity: "0;1;1") 止められる
    p#v(right: 0px; cy: 29px; font-size: 24px; font-family: n; color: #FFFFFF) 4.9{s4}万kWh{/};4.4{s4}万kWh{/};2.6{s4}万kWh{/}

# s8 対策: 3 枚の札が語ごとに下から入り (絵は弾んで浮き続ける)、金額の語で年の削減額が数え上がる
section#s8(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
sec#s8_sec(n: "06"; l: "削減の試算（年額）")
title#s8_title 3つの対策で、どれだけ減らせるか
# 対策の札 (工事の札・番号・絵・題・箇条・罫・年の削減額・kWh)
def mcard(no, tg, tgc, tgf, h, res, kwh) = div(top: 175px; width: 355px; height: 427px; background: #FFFFFF; border: 1px solid #E0E8E5; border-radius: 16px; box-shadow: 0px 9px 23px #13222B12; in: {y:27, opacity:0, duration:0.7, ease:'power3.out'})
  p#tag(left: 19px; cy: 31px; font-size: 14px; color: {tgc}; background: {tgf}; border-radius: 11px; padding: 4px 11px; content: {tg})
  p#no(right: 19px; cy: 27px; font-size: 20px; font-family: n; color: #7B8D87; content: {no})
  p#h(left: 23px; cy: 195px; font-size: 21px; content: {h})
  div#ln(left: 23px; top: 308px; width: 310px; height: 1px; background: $line)
  div#res(left: 21px; top: 320px; width: 310px; height: 60px; in: {y:8, opacity:0, duration:0.45, ease:'power3.out'})
    p#s(left: 0px; cy: 45px; font-size: 16px; color: $ink2) 年
    p#v(left: .s.right+5; cy: 30px; font-size: 57px; line-height: 1; font-family: n; color: $green_d; letter-spacing: -0.02em; content: {res})
    p#u(left: .v.right+5; cy: 44px; font-size: 20px; color: $green_d) 万円
  p#kwh(left: 23px; cy: 401px; font-size: 15px; color: $muted; font-family: m; in: {y:8, opacity:0, duration:0.45, ease:'power3.out'}; content: {kwh})
mcard#s8_c1(left: 80px; no: "01"; tg: "工事なし"; tgc: $green_d; tgf: $green_l; h: "空調の設定温度を1℃見直し"; res: "[count:51.5 start=0 ms=900 delay=100]"; kwh: "16,900 kWh／年")
  img#pic(left: 100px; top: 17px; width: 173px; height: 153px; fit: contain; main: sine {y: -5, period: 3.2}; delay: 150; in: {scale:0.85, y:7, duration:0.8, ease:'back.out(1.8)'}) [transparent]白くすっきりした壁掛けのオフィス用エアコン 1 台からやわらかな風の線が流れ、その横に空の液晶の白いリモコンが浮かぶ。単体の物、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#dot(left: 23px; top: "225;249"; width: 5px; height: 5px; border-radius: 99px; background: $green) ×2
  p#li(left: 36px; cy: "228;251"; font-size: 15px; color: $ink2; font-family: m) ×2 夏 26℃→27℃／冬 22℃→21℃;空調の電力を10%削減
mcard#s8_c2(left: 462px; no: "02"; tg: "工事なし"; tgc: $green_d; tgf: $green_l; h: "待機電力・消し忘れ対策"; res: "[count:142.8 start=0 ms=900 delay=100]"; kwh: "46,800 kWh／年")
  img#pic(left: 100px; top: 17px; width: 173px; height: 153px; fit: contain; main: sine {y: -5, period: 3.2}; delay: 150; in: {scale:0.85, y:7, duration:0.8, ease:'back.out(1.8)'}) [transparent]デスクトップのモニター 1 台と、プラグを抜いて電源を切る電源タップ、丸い時計のタイマーの印と小さな三日月の印。省エネの考え方、単体の物、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#dot(left: 23px; top: "225;249;272"; width: 5px; height: 5px; border-radius: 99px; background: $green) ×3
  p#li(left: 36px; cy: "228;251;275"; font-size: 15px; color: $ink2; font-family: m) ×3 OA機器の自動電源オフ;照明・空調のタイマー;止められる分の3分の2を削減
mcard#s8_c3(left: 845px; no: "03"; tg: "工事あり　960万円"; tgc: #8A5300; tgf: #FFF3DF; h: "照明のLED化"; res: "[count:148.2 start=0 ms=900 delay=100]"; kwh: "48,600 kWh／年")
  img#pic(left: 100px; top: 17px; width: 173px; height: 153px; fit: contain; main: sine {y: -5, period: 3.2}; delay: 150; in: {scale:0.85, y:7, duration:0.8, ease:'back.out(1.8)'}) [transparent]白い清潔な光でやわらかく輝く、現代的な薄い正方形の LED 天井照明パネル 1 枚を少し下から斜めに見上げた形、省エネを表す小さな葉の印。単体の物、背景は透明、枠いっぱいに大きく。白・明るい灰・ミントグリーン・空色に小さな琥珀色の差し色
  div#dot(left: 23px; top: "225;249"; width: 5px; height: 5px; border-radius: 99px; background: $green) ×2
  p#li(left: 36px; cy: "228;251"; font-size: 15px; color: $ink2; font-family: m) ×2 蛍光灯→LED（照明の電力55%減）;工事費は約6.5年で回収

# s9 合計: 滝の図 (現在 → 3 つの削減 → 対策後) が左から順に伸び、点線で段をつなぐ・「342.5」で右の合計の板が数え上がり、「29%」で割合と前後の金額
section#s9(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.3, ease:'power2.in'})
sec#s9_sec(n: "06"; l: "削減の試算（合計）")
title#s9_title 合わせて年{em}342.5万円{/}、電気代の29%を削減
card#s9_card(left: 80px; top: 175px; width: 727px; height: 427px)
  ctitle#t 年間の電気代の変化
  cnote#n 単位：万円
  # 目盛り (0〜1,200 万円 = 288 px)
  div#gl(left: 73px; top: "370;298;226;154;82"; width: 627px; height: 1px; background: $grid) ×5
  p#gn(left: 23px; cy: "371;299;227;155;83"; width: 41px; text-align: right; font-size: 13px; color: $muted; font-family: m) ×5 0;300;600;900;1,200
  # 棒 (現在と対策後は下から・削減の 3 本は上から伸びる)
  div#b0(left: 100px; top: 89.6px; width: 88px; height: 281px; border-radius: 4px; background: #7D8F96; delay: 550; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom'})
  div#b1(left: 222.7px; top: 89.6px; width: 88px; height: 12.4px; border-radius: 4px; background: $green; delay: 1100; in: {scaleY:0, duration:0.45, ease:'power3.out', pivot:'top'})
  div#b2(left: 345.3px; top: 102px; width: 88px; height: 34.3px; border-radius: 4px; background: $green; delay: 1500; in: {scaleY:0, duration:0.45, ease:'power3.out', pivot:'top'})
  div#b3(left: 468px; top: 136.3px; width: 88px; height: 35.6px; border-radius: 4px; background: $green; delay: 1900; in: {scaleY:0, duration:0.45, ease:'power3.out', pivot:'top'})
  div#b4(left: 590.7px; top: 171.8px; width: 88px; height: 198.8px; border-radius: 4px; background: $ink; delay: 2300; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom'})
  p#l(left: "77.3;200;322.7;445.3;568"; cy: "72.4;72.4;84.8;119;154.6"; width: 133px; text-align: center; font-size: 20px; font-family: n; color: "$ink;$green_d;$green_d;$green_d;$ink"; delay: "850;1400;1800;2200;2600"; in: {scale:0.7, opacity:0, duration:0.4, ease:'back.out(2.2)'}) ×5 1,171;−51.5;−142.8;−148.2;829
  p#cat(left: "77.3;200;322.7;445.3;568"; top: 379px; width: 133px; text-align: center; font-size: 14px; line-height: 1.3; color: $ink2; font-family: m) ×5 現在;設定温度[br]1℃見直し;待機・[br]消し忘れ対策;照明の[br]LED化;対策後
  shape#c0(path: "M188 89 L222.7 89"; background: none; border: 1px solid #9FB0B5; dash: 4,3; delay: 950; in: draw {duration: 0.3})
  shape#c1(path: "M310.7 101.3 L345.3 101.3"; background: none; border: 1px solid #9FB0B5; dash: 4,3; delay: 1500; in: draw {duration: 0.3})
  shape#c2(path: "M433.3 135.6 L468 135.6"; background: none; border: 1px solid #9FB0B5; dash: 4,3; delay: 1900; in: draw {duration: 0.3})
  shape#c3(path: "M556 171.2 L590.7 171.2"; background: none; border: 1px solid #9FB0B5; dash: 4,3; delay: 2300; in: draw {duration: 0.3})
# 合計の板 (淡い緑のグラデ + 緑の縁): 削減額・罫・割合・前後の金額・kWh・注記
div#s9_total(left: 833px; top: 175px; width: 367px; height: 427px; border-radius: 16px; background: linear(#E9F8F1,#FFFFFF@75%,180); border: 2px solid #BFE6D4; box-shadow: 0px 9px 23px #13222B12; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  p#lab(left: 29px; cy: 39px; font-size: 17px; color: $ink2) 年間の削減額
  p#v(left: 27px; cy: 103px; font-size: 83px; line-height: 1; font-family: n; color: $green_d; letter-spacing: -0.02em) [count:342.5 start=0 ms=1100 delay=150]
  p#u(left: .v.right+5; cy: 124px; font-size: 25px; color: $green_d) 万円
  div#ln(left: 29px; top: 175px; width: 308px; height: 1px; background: #CFE7DC)
  div#pct(left: 29px; top: 193px; width: 308px; height: 54px; in: {y:9, opacity:0, duration:0.6, ease:'power3.out'})
    p#a(left: 0px; cy: 40px; font-size: 19px) 年間電気代の
    p#v(left: .a.right+7; cy: 27px; font-size: 53px; line-height: 1; font-family: n; color: $green_d) 29
    p#b(left: .v.right+7; cy: 40px; font-size: 19px) %
  p#flow(left: 29px; cy: 289px; font-size: 21px; in: {y:9, opacity:0, duration:0.6, ease:'power3.out'}) {nn}1,171{/}万円 {em}→{/} {nn}829{/}万円
  p#kwh(left: 29px; cy: 325px; font-size: 16px; color: $ink2; font-family: m; in: {y:9, opacity:0, duration:0.6, ease:'power3.out'}) 使用量は年 112,300 kWh 減
  p#nt(left: 29px; cy: 395px; font-size: 13px; color: $muted; font-family: m) ※3つの対策の合計（年額）

# s10 まとめ: 3 行の結論の札が語ごとに下から入り、2 行目 (緑の縁) に「まずはここから」の札・締めの間で 1 と 3 を沈め、2 を少し大きく
section#s10(stagger: {each:0})
sec#s10_sec(n: "07"; l: "まとめ")
title#s10_title まずは、{em}工事のいらない対策{/}から
def srow(no, t, s) = div(left: 80px; width: 1120px; height: 119px; background: #FFFFFF; border: 1px solid #E0E8E5; border-radius: 16px; box-shadow: 0px 9px 23px #13222B12; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  p#no(left: 27px; cy: 59px; width: 52px; height: 52px; text-align: center; align-items: center; font-size: 27px; line-height: 1; font-family: n; color: #FFFFFF; background: $green_d; border-radius: 99px; content: {no})
  p#t(left: 100px; cy: 42px; font-size: 27px; content: {t})
  p#s(left: 101px; cy: 81px; font-size: 16px; color: $ink2; font-family: m; content: {s})
srow#s10_r1(top: 179px; no: "1"; t: "電気代の{em}44%{/}は空調、{em}31%{/}は誰もいない夜と休日に"; s: "空調 515万円／夜間・休日 363万円（いずれも年額）"; delay: 200)
srow#s10_r2(top: 311px; no: "2"; t: "設定温度1℃と待機・消し忘れ対策で、{em}年194万円{/}"; s: "工事なしで実施できる（51.5万円＋142.8万円）"; background: linear(#EEFAF4,#FFFFFF@70%,90); border: 2px solid $green)
  div#first(right: 27px; top: 39px; width: 177px; height: 41px; border-radius: 20px; background: $green_d; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2.2)'})
    icon#i(left: 16px; cy: 50%; font-size: 17px; name: check; weight: bold; color: #FFFFFF)
    p#t(left: 43px; cy: 50%; font-size: 17px; color: #FFFFFF) まずはここから
srow#s10_r3(top: 443px; no: "3"; t: "LED化も合わせれば、{em}年342万円・約3割{/}の削減"; s: "LED化の工事費960万円は約6.5年で回収")
p#s10_src(left: 80px; cy: 589px; font-size: 13px; color: $muted; font-family: m; in: {y:7, opacity:0, duration:0.6, ease:'power3.out'}) データ：スマートメーター30分値 17,520コマ（昨年度4月〜3月）、フロア別・系統別子メーター／金額は年額の試算
```

```timeline.txt
#v2
# hf の作り: 声は 1.10 倍に詰めて 84 s。ここで引く話者は既定の速さで hf の話速と尺に近い (110% にすると 75 s に縮む) ので速さは書かない
cast n = "明るくクリアな中高音の20代の女性ナレーター、滑らかで明瞭な発声、丁寧で快活、落ち着いて信頼感のある語り口"
silence head=0 tail=0

*** s1
[>#subtitle]
bgm music
se title +180
se whoosh -2dB +550
@n: [silence:0.8s][!#s1_l2{uem} marker +200]オフィスの電気代、どこに消えているのでしょうか。[silence:0.22s]

*** s2
se swish -3dB +20
@n: [silence:0.3s]社員200人のオフィスで1年分の電力データを[>#s2_k1 -200][>#s2_k3 -40][>#s2_k4 +120][♪multi -2dB +50]分析すると、[|]電気代は年[>#s2_k2 -550][♪ping -2dB +50][!#s2_k2 glow,#0E9F6E47,blur=29 +600]{1,171万円|1171万円}でした。[silence:0.26s]

*** s3
se swish -3dB +20
se rise -3.5dB +450
@n: [silence:0.3s][chap #chap.ch[1] #chap.ch[2] 81 75 -250]月別では、夏の[!#s3_card.bar[5] fill,$summer,duration=400][>#s3_card.lab_aug_t +100][>#s3_card.lab_aug +100][♪pop -3dB]8月と冬の[!#s3_card.bar[10] fill,$winter,duration=400][>#s3_card.lab_jan +100][♪pop -3dB]1月に2つの山。8月は、最も少ない[>#s3_card.lab_may_t][>#s3_card.lab_may][>#s3_card.ref +150]5月の[>#s3_card.brk -300][>#s3_card.ratio -50][♪chime -1dB]1.7倍です。[silence:0.25s]

*** s4
se swish -3dB +20
se soft -2dB +400
@n: [silence:0.3s][chap #chap.ch[2] #chap.ch[3] 158 75 -250]用途別では[>#s4_card.row[1].hl][>#s4_card.seg1w +200][♪pop -2dB]空調が44%と、[>#s4_card.badge]半分近くを占めます。[silence:0.65s]

*** s5
se swish -3dB +20
@n: [silence:0.35s][chap #chap.ch[3] #chap.ch[4] 235 87 -300]ピークは[>#s5_r1 -150][>#s5_r1.bar][>#s5_r1.val +450][♪pop -3dB]夏が{186kW|186キロワット}。[>#s5_r2 -150][>#s5_r2.bar][>#s5_r2.val +450][♪pop -3dB]冬は{158kW|158キロワット}で、[|][>#s5_r3 -750][>#s5_r3.bar -600][>#s5_r3.val -150][>#s5_r4 -450][>#s5_r4.bar -300][>#s5_r4.val +150][>#s5_call][♪chime -2dB]暖房が一斉に立ち上がる始業時の[!#s5_call glow,#2FA4E72E,blur=0,spread=7][=#s5_call +500]朝に来ます。[silence:0.22s]

*** s6
se swish -3dB +20
@n: [silence:0.4s][chap #chap.ch[4] #chap.ch[5] 325 112 -350]そして、[♪low -1dB -250]誰もいない夜と休日も平均[>#s6_a1 -350][♪pop -3dB]{19kW|19キロワット}。この時間だけで全体の[>#s6_a2 -450][>#s6_a2.fill -200][♪pop -3dB]31%、[|]電気代にして[>#s6_a3 -500][♪chime -2dB]363万円です。[silence:0.5s]
@: [<#s6_a1 -700][<#s6_a2 -700][<#s6_a3 -700][<#s6_ta -650][>#s6_tb -350][>#s6_b -350][>#s6_b.seg1 -100][>#s6_b.lg[1]]その[♪soft -2dB -100]59%は、[>#s6_b.seg2 -150][>#s6_b.lg[2] -100]待機電力と[>#s6_b.seg3 -150][>#s6_b.lg[3] -100]消し忘れ。[>#s6_b.brk -200][>#s6_b.brk_l -50][♪ping -2dB]止められる電気です。[silence:0.45s]
[<#s6_bg -20][<#s6_glow -20]

*** s8
se swish -3dB +20
@n: [silence:0.4s][chap #chap.ch[5] #chap.ch[6] 439 75 -350]試算では、[>#s8_c1 -350][♪pop -3dB]設定温度の{1℃|1度}見直しで年[>#s8_c1.res -400][>#s8_c1.kwh -280]51.5万円、[|][>#s8_c2 -350][♪pop -3dB]待機と消し忘れ対策で[>#s8_c2.res -400][>#s8_c2.kwh -280]142.8万円、[|][>#s8_c3 -350][♪pop -3dB]LED化で[>#s8_c3.res -400][>#s8_c3.kwh -280]148.2万円。[silence:0.28s]

*** s9
se swish -3dB +20
se rise -3.5dB +350
@n: [silence:0.3s]合わせて年[>#s9_total -500][♪ping -1dB]342.5万円、[|]電気代の[>#s9_total.pct -200][>#s9_total.flow +400][>#s9_total.kwh +550]29%を減らせます。[silence:0.43s]

*** s10
se swish -3dB +20
se multi -3dB +450
@n: [silence:0.35s][chap #chap.ch[6] #chap.ch[7] 517 87 -300]まずは[>#s10_r2 -300][♪multi -3dB]工事のいらない対策から始めれば、年[!#s10_r2 glow,#0E9F6E42,blur=29][>#s10_r2.first +100]194万円。[>#s10_r3 -300][♪multi -3dB]LED化の工事費も、[>#s10_src +500]6.5年で回収できます。[silence:0.25s][!#s10_r1 dim,0.45,duration=600][!#s10_r3 dim,0.45,duration=600][!#s10_r2 to,scale=1.025,duration=600,ease=power2.out][!#s10_r2.first punch,1.12,duration=700 +100][♪title +100][silence:2.05s]
```

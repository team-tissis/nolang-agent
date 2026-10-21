# data · remote-work-survey (hf 全力版の全量の写し — 出社とリモート、社員 800 人の本音・働き方調査を白い板に番号つきの題と図を組む 10 場面の経営会議向け調査報告) — canvas 1280x720

見せる作り: 全編の地 (淡い青のグラデ + 点の格子 + 漂う 3 色の光)・題の場面 (右から入る角丸の絵・mask から上がる 2 行と数え上がる 800 と黄の下帯・3 つの数字の札)・2 場面目から常設の左上のロゴと上端の進行線・場面ごとに入れ替わる右上の章札・白い板の def (番号札 + 題 + 補足 + 伸びる罫 + 出典と凡例)・数字の語で動く図 (描かれる輪と数える 76%・100 点の単位図を語ごとに 3 色で塗る・全体の基準の破線つき横棒と差のかぎ・積み上げの帯から理由の板へ下ろす線・働き方別と年代別の縦棒で 20 代を塗り替えて札と矢印・度数の縦棒で中央とかぎ・平均の破線と「2倍」・頻出語の棒を声の向きで塗り分け・3 枚の施策の札と 12→30 室・結論の 3 行と数字の札)・締めの題の 1 枚・濃紺の札の字幕・音の層 (場面の境のシュッ + 語に結んだ電子音 60 余)

```design.txt
#v2
# 学ぶ作り: 明るいコーポレートの調査報告の design system を根に 1 回 (palette・書体 4・白い板 board の def = 番号札 + 題 + 補足 + 罫 + 出典・右上の章札 chap の def) → 場面は板の中の図だけを書く
# 常設の層: 全編の地 (淡い青のグラデ + 点の格子 + 漂う 3 色の光)・2 場面目から sticky の左上のロゴと上端の進行線・場面ごとに入れ替わる右上の章札 (場面の out で上へ抜ける)
# 図は数字の語と同時に動く: 描かれる輪 + 数える 76%・100 点の単位図を語ごとに 3 色で塗る・全体の基準線つきの横棒と差のかぎ・積み上げの帯から理由の板へ下ろす線・縦棒 2 組 (20 代を塗り替えて札と矢印)・度数の縦棒と中央の札とかぎ・平均の破線と倍率の札・頻出語の棒を声の向きで塗り分け・3 枚の施策の札・結論の 3 行と数字の札・締めの題の 1 枚
# hf d03 remote-work-survey (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の退場は要素の out (板は少し上へ抜けて消える)・切替は根の `transition = none,370` (混ぜない — 旧い板の退場が次の板の入りに重なる・地は常設)
canvas 1280x720 bg=#F3F7FC
theme light
palette ink=#16233F ink2=#4A5A75 ink3=#66728A line=#E3E9F2 tint=#F2F6FB brand=#34508F brand_t=#DCE4F3 mid=#7F95C4 neutral=#B7C4D8 full=#E69F00 hyb=#009E73 rem=#0072B2 flat=#C9D2DE down=#D64545 down_t=#FDF1F0 age=#CDC3EC age_hi=#6B4FC4 mark=#FFD54A env=#6B7A90 track=#F1F4F9 gl=#EDF1F7 base=#CFD8E6
font "日本語のゴシック体の太字 (Bold)、清潔で中立的、かなと漢字の均整が取れて読みやすい"
fonts b="日本語のゴシック体の太字 (Bold)、清潔で中立的、かなと漢字の均整が取れて読みやすい"
# engine: 極太 (Black / Heavy) の説明文は字間の広い・癖のある和文書体に当たる — 見出しは本文と同じ素直な太字のゴシックで引く (hf は同じ書体の Black)
fonts h="日本語のゴシック体の太字 (Bold)、清潔で中立的、かなと漢字の均整が取れて読みやすい"
fonts m="清潔で中立的なサンセリフ、均整の取れたゴシックの日本語 (ひらがな・カタカナ・漢字) と鮮明な欧文、中くらいの太さ (Medium)、注記と字幕向け"
fonts n="清潔で中立的なネオグロテスクの欧文サンセリフ、均整の取れたくっきりした数字、極太のウェイト (ExtraBold)、データの大きな数字向け"
sfx off
# hf の作り: 板の見出しは台詞より先に場面の題を出す (見出し → 図 → 台詞が数字を読む)
lint off=spoiler
# hf の作り: 板の中の目盛り・凡例・出典・補足は 11〜13 px (1080 の 17〜20 px)
lint off=small_text
# hf の作り: 図の色 (半透明の地・薄い縁・グラデの端) は場面ごとに直書き
lint off=palette_drift
# hf の作り: 2 場面目からは絵の無い白い板の図だけの場面が続く (絵は板の中の小さな挿絵だけ)
lint off=text_only_cut,same_picture
# hf の作り: 灰の帯・目盛りの帯・施策の破線の枠は中身より先に置き、語で中身が入る
lint off=empty_board
# hf の作り: 冒頭の題の一文は字幕を出さない (画面の題がそのまま台詞)・結論の行の題は字幕と同じ文・締めの 1 枚は 2 秒強で終わる
lint off=caption_gap,duplicate_text,flash_text
art "清潔で現代的なフラットのベクターイラスト、丸みのある幾何学的な形、控えめで柔らかい影とやさしいグラデーション、明るく前向きな配色 (空色・明るい青緑・暖かいコーラルオレンジの差し色・白と淡い青灰)、親しみやすい企業のインフォグラフィック調"
prompt_tail "文字・数字・ロゴ・透かしは一切入れない"
sound hit = "明るく澄んだ企業向けの電子チャイムの短い連打、題が出る合図"
sound whoosh = "場面転換の短く軽いシュッという電子の風切り音"
sound pop_hi = "高めの短い上昇の電子音、ポップで明るい"
sound pop_mid = "中くらいの高さの短い上昇の電子音、控えめ"
sound tick = "軽く短いクリックの電子音の単音"
sound graph = "グラフが伸びていく上昇のシンセの効果音"
sound shwip = "短く鋭いシュッと線を引く電子の効果音"
sound bell = "明るいベルのような電子チャイムの単音"
# 文字の一部: 数字は欧文の極太 (nn)・大きな数字の横の単位は小さく (u43〜u63 = 数字の比)・凡例の色の札 (■ ● ━ を色で)
run nn { font-family: n }
run nk { font-family: n; color: $ink }
run n24 { font-family: n; font-size: 1.44em }
run n17 { font-family: n; font-size: 1.24em }
run uj { font-size: 0.5em; font-family: b }
run u43 { font-size: 0.43em }
run u46 { font-size: 0.46em }
run u48 { font-size: 0.48em }
run u54 { font-size: 0.54em }
run u50 { font-size: 0.5em }
run u53 { font-size: 0.53em }
run u55 { font-size: 0.55em }
run u63 { font-size: 0.63em }
run fs { font-size: 0.55em; font-family: m; color: $ink2 }
run s12 { font-size: 0.7em; font-family: m; color: $ink3 }
run bai { font-size: 0.61em; font-family: h }
run ar { color: $brand }
run cf { color: $full }
run ch { color: $hyb }
run cr { color: $rem }
run cb { color: $brand }
run cm { color: $mid }
run cn { color: $neutral }
run cg { color: $age_hi }
run ce { color: $env }
run ci { color: $ink }
run cd { color: $down }
run cl { color: $flat }
# 施策の札の中身を語でまとめて出す
cue card(x) = [>#x.bg][>#x.pic][>#x.no][>#x.tag][>#x.t][>#x.d]
svg logo = """<svg viewBox="0 0 46 46"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2f80ed"/><stop offset="1" stop-color="#12b5a6"/></linearGradient></defs><rect width="46" height="46" rx="13" fill="url(#g)"/><path d="M14.5 31h17.5a6 6 0 0 0 .6-12 8.2 8.2 0 0 0-15.6 2.4A4.9 4.9 0 0 0 14.5 31z" fill="#fff"/></svg>"""
svg ring = """<svg viewBox="0 0 400 400"><circle cx="200" cy="200" r="160" fill="none" stroke="#DCE4F3" stroke-width="44"/></svg>"""
# 子は親 (板) と一緒に 1 枚で抜ける (自分の退場を持たない)・場面の頭の要素は自分の out を書く
p { color: $ink; out: none }
div { border-radius: 0px; background: none; padding: 0px; border: none; box-shadow: none; out: none }
img { out: none }
svg { out: none }
shape { out: none }
icon { out: none }
# 字幕: 下端中央の濃紺の札・白の中字・句ごとの札 ([|] で hf の句に切る)・入りも抜けも素の切替
subtitle.hug(bottom: 40px; font-size: 27px; line-height: 1.3; letter-spacing: 0.03em; color: #FFFFFF; font-family: m; background: #16233FE6; border-radius: 11px; padding: 8px 24px 9px 24px; box-shadow: 0px 5px 16px #16233F2E; unit: sentence; strip: 。; lead: 0; tail: 250; hold: next,500; in: none; out: none)
# 曲: 声の無い頭と締めだけ前に出し、台詞の間は下げる
bgm#music(keys: "0:+8|450ms:+8|1200ms:0|end-2.4s:0|end-1.6s:+7"; fade: 800,1500) 軽快なピアノのリズムを刻む明るく前向きなコーポレートの曲、主張しすぎない調査報告向け

# 白い板 (番号札 + 題 + 補足 + 罫 + 出典): 板は下から上がり、見出しの 3 つが左から順に・罫が左から伸び・出典が遅れて出る。退場は少し上へ抜ける
def board(no, t, m, f) = div(left: 53px; top: 72px; width: 1173px; height: 537px; background: #FFFFFF; border-radius: 19px; box-shadow: 0px 15px 40px #16233F17; in: {y:31, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-19, opacity:0, duration:0.42, ease:'power2.in'})
  p#no(left: 37px; cy: 48px; font-size: 16px; font-family: n; color: $brand; background: $brand_t; border-radius: 8px; padding: 5px 10px; delay: 120; in: {x:-16, opacity:0, duration:0.5, ease:'power3.out'}; content: {no})
  p#t(left: .no.right+13; cy: 48px; font-size: 33px; font-family: h; letter-spacing: 0.02em; delay: 190; in: {x:-16, opacity:0, duration:0.5, ease:'power3.out'}; content: {t})
  p#m(right: 37px; cy: 48px; font-size: 15px; font-family: m; color: $ink2; delay: 260; in: {x:-16, opacity:0, duration:0.5, ease:'power3.out'}; content: {m})
  div#rule(left: 37px; top: 84px; width: 1099px; height: 1px; background: $line; delay: 150; in: {scaleX:0, duration:0.8, ease:'power2.inOut', pivot:'left'})
  p#src(left: 37px; cy: 513px; font-size: 11px; font-family: m; color: $ink3; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}; content: {f})
# 右上の章札 (紺の丸の番号 + 章名 + 「/ 10」)・場面ごとに下から入り上へ抜ける
def chap(n, t, w) = div(right: 53px; top: 21px; width: {w}; height: 33px; border-radius: 99px; background: #FFFFFF; box-shadow: 0px 3px 11px #16233F14; delay: 100; in: {y:11, opacity:0, duration:0.45, ease:'power3.out'}; out: {y:-11, opacity:0, duration:0.3, ease:'power2.in'})
  div#c(left: 5px; cy: 50%; width: 24px; height: 24px; border-radius: 99px; background: $brand)
    p#n(cx: 50%; cy: 50%; font-size: 11px; font-family: n; color: #FFFFFF; content: {n})
  p#t(left: 37px; cy: 50%; font-size: 14px; content: {t})
  p#o(left: .t.right+8; cy: 50%; font-size: 11px; font-family: n; color: $ink3) / 10
# 施策の札 (破線の枠が先に出て、語で淡い地・挿絵・番号・題・説明・根拠の行が入る)
def pcard(no, t, d, b) = div(top: 101px; width: 347px; height: 393px)
  shape#fr(left: 0px; top: 0px; width: 347px; height: 393px; path: rect,r=0.05; background: none; border: 1px solid #CFD8E6; dash: 5,4; delay: 300; in: {opacity:0, duration:0.4, ease:'power1.out'})
  div#bg(left: 0px; top: 0px; width: 347px; height: 393px; border-radius: 16px; background: $tint; in: {opacity:0, duration:0.35, ease:'power1.out'})
  img#pic(left: 93px; top: 9px; width: 160px; height: 143px; object-fit: contain; delay: 50; in: {scale:0.85, opacity:0, duration:0.5, ease:'back.out(1.7)'})
  p#no(left: 23px; cy: 171px; font-size: 23px; font-family: n; color: $brand; delay: 150; in: {y:9, opacity:0, duration:0.55, ease:'power3.out'}; content: {no})
  p#tag(left: .no.right+7; cy: 173px; font-size: 12px; color: $ink3; letter-spacing: 0.1em; delay: 150; in: {y:9, opacity:0, duration:0.55, ease:'power3.out'}) 施策
  p#t(left: 23px; top: 187px; width: 310px; font-size: 21px; font-family: h; line-height: 1.3; delay: 230; in: {y:9, opacity:0, duration:0.55, ease:'power3.out'}; content: {t})
  p#d(left: 23px; top: 255px; width: 310px; font-size: 14px; font-family: m; line-height: 1.6; color: $ink2; delay: 350; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}; content: {d})
  div#bt(left: 23px; top: 346px; width: 304px; height: 30px; in: {y:7, opacity:0, duration:0.55, ease:'power3.out'})
    div#ln(left: 0px; top: 0px; width: 304px; height: 1px; background: #DFE6F0)
    p#k(left: 0px; cy: 20px; font-size: 11px; color: #FFFFFF; background: $ink; border-radius: 5px; padding: 3px 8px) 根拠
    p#s(left: 43px; cy: 20px; font-size: 13px; content: {b})
# 結論の行 (淡い地 + 紺の丸の番号 + 題 + 補足 + 右に 2 枚の数字の札)
def crow(num, head, sub, c1, k1, v1, c2, k2, v2) = div(left: 37px; width: 1099px; height: 121px; border-radius: 15px; background: $tint; in: {opacity:0, duration:0.3, ease:'power1.out'})
  div#no(left: 20px; cy: 50%; width: 56px; height: 56px; border-radius: 99px; background: $brand; in: {y:11, opacity:0, duration:0.55, ease:'power3.out'})
    p#t(cx: 50%; cy: 50%; font-size: 27px; font-family: n; color: #FFFFFF; content: {num})
  p#h(left: 97px; cy: 45px; font-size: 28px; font-family: h; delay: 80; in: {y:11, opacity:0, duration:0.55, ease:'power3.out'}; content: {head})
  p#s(left: 97px; cy: 83px; font-size: 16px; font-family: m; color: $ink2; delay: 160; in: {y:7, opacity:0, duration:0.55, ease:'power3.out'}; content: {sub})
  # 数字の札 2 枚 (色の四角 + 題・下に大きな数字)・2 枚目は 150 ms 遅れて弾む
  div#c1(left: 728px; top: 22px; width: 167px; height: 77px; border-radius: 12px; background: #FFFFFF; border: 1px solid $line; in: {scale:0.8, opacity:0, duration:0.5, ease:'back.out(1.7)'})
    div#sq(left: 15px; cy: 19px; width: 9px; height: 9px; border-radius: 3px; background: {c1})
    p#k(left: 29px; cy: 19px; font-size: 13px; color: $ink2; content: {k1})
    p#v(left: 15px; cy: 49px; font-size: 33px; font-family: n; line-height: 1; content: {v1})
  div#c2(left: 912px; top: 22px; width: 167px; height: 77px; border-radius: 12px; background: #FFFFFF; border: 1px solid $line; delay: 150; in: {scale:0.8, opacity:0, duration:0.5, ease:'back.out(1.7)'})
    div#sq(left: 15px; cy: 19px; width: 9px; height: 9px; border-radius: 3px; background: {c2})
    p#k(left: 29px; cy: 19px; font-size: 13px; color: $ink2; content: {k2})
    p#v(left: 15px; cy: 49px; font-size: 33px; font-family: n; line-height: 1; content: {v2})

# 全編の地 (根): 淡い青の縦グラデ・点の格子・左上の青・右下の緑・上の琥珀の淡い光が全編でゆっくり漂う
div#bg_base(inset: 0; background: linear(#F7FAFF,#E9F0FA,180); z-index: back; in: none)
div#dots(inset: 0; pattern: dots,20,#34508F0E; z-index: back; in: none)
shape#blob1.ellipse(left: -200px; top: -280px; width: 653px; height: 653px; background: radial(#2F80ED2B,#2F80ED00@70%); z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=120 y=73 ease=sine.inOut),duration=156500)
shape#blob2.ellipse(left: 787px; top: 307px; width: 720px; height: 720px; background: radial(#009E731F,#009E7300@70%); z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=-133 y=-80 ease=sine.inOut),duration=156500)
shape#blob3.ellipse(left: 507px; top: -200px; width: 507px; height: 507px; background: radial(#E69F0014,#E69F0000@70%); z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=-80 y=60 ease=sine.inOut),duration=156500)

# s01 題: 右に角丸の題の絵が寄りながら右から入り、左に小札 → mask から上がる 2 行 (800 が数え上がり、「800人の本音」に黄の下帯) → 罫と社名 → 語で補足と 3 つの数字の札・架空の注記
section#s01(stagger: {each:0})
img#s01_kv(left: 567px; top: 64px; width: 660px; height: 513px; border-radius: 24px; box-shadow: 0px 20px 53px #16233F29; object-fit: cover; object-position: 80% 50%; main: kb {scale: [1.12, 1], ease:'power1.out'}; delay: 50; in: {x:47, opacity:0, duration:1, ease:'power3.out'}; out: {x:27, opacity:0, duration:0.42, ease:'power2.in'}) 働き方調査の報告の横長のキービジュアル。左に明るいガラス張りのモダンなオフィスビルの断面があり、中の階で同僚 3 人がテーブルを囲んで談笑している。右には窓辺の在宅ワークの机 (ノートPC と観葉植物、オレンジのブランケットを掛けた白い椅子) を大きく描き、二つの場面を点線の道と小さな吹き出しや円グラフ・棒グラフの丸いアイコンがつなぐ。明るい水色の空と白い雲、遠くに淡いビル群と緑の木々。オフィスと在宅の机を画面いっぱいに大きく描いて余白を作らず、下端まで木々と床を描き切る (左下に数字の札が重なる)
div#s01_kicker(left: 73px; top: 175px; width: 350px; height: 35px; border-radius: 99px; background: #FFFFFF; box-shadow: 0px 3px 11px #16233F14; delay: 250; in: {y:16, opacity:0, duration:0.55, ease:'power3.out'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'})
  div#dot(left: 15px; cy: 50%; width: 7px; height: 7px; border-radius: 99px; background: linear(#2F80ED,#12B5A6,135))
  p#t(left: 29px; cy: 50%; font-size: 15px; color: $brand) 経営会議 報告 ｜ 人事部 働き方調査 2026
p#s01_t1(left: 73px; cy: 271px; font-size: 53px; font-family: h; line-height: 1.12; letter-spacing: 0.01em; delay: 400; in: mask_rise {duration: 0.8, ease: 'power4.out'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'}) 出社とリモート、
# 「800人の本音」の黄の下帯 (文字の下の段・語で左から伸びる)
div#s01_mark(left: 181px; top: 371px; width: 374px; height: 20px; border-radius: 4px; background: $mark; in: {scaleX:0, duration:0.5, ease:'power2.inOut', pivot:'left'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'})
p#s01_t2a(left: 73px; cy: 360px; font-size: 53px; font-family: h; line-height: 1.12; letter-spacing: 0.01em; delay: 700; in: mask_rise {duration: 0.8, ease: 'power4.out'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'}) 社員
p#s01_t2n(left: 184px; cy: 356px; font-size: 80px; font-family: n; line-height: 1; color: $brand; letter-spacing: -0.02em; delay: 700; in: mask_rise {duration: 0.8, ease: 'power4.out'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'}) [count:800 start=0 ms=1300 delay=100]
p#s01_t2b(left: s01_t2n.right+6; cy: 360px; font-size: 53px; font-family: h; line-height: 1.12; letter-spacing: 0.01em; delay: 700; in: mask_rise {duration: 0.8, ease: 'power4.out'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'}) 人の本音
div#s01_rule(left: 73px; top: 422px; width: 48px; height: 4px; border-radius: 2px; background: linear(#2F80ED,#12B5A6,90); delay: 1150; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'})
p#s01_ci1(left: 73px; cy: 456px; font-size: 20px; delay: 1250; in: {y:9, opacity:0, duration:0.55, ease:'power3.out'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'}) 株式会社ソラリンク 全社員アンケート
p#s01_ci2(left: 73px; cy: 490px; font-size: 16px; font-family: m; color: $ink2; in: {y:9, opacity:0, duration:0.55, ease:'power3.out'}; out: {y:-17, opacity:0, duration:0.42, ease:'power2.in'}) 来期の出社方針を決める前に、社員の本音を聞きました
# 3 つの数字の札 (絵の左下に重ねる・語で弾んで 1 枚ずつ)
def stat(l, v) = div(top: 528px; width: 157px; height: 79px; border-radius: 13px; background: #FFFFFF; box-shadow: 0px 9px 27px #16233F24; overlap: s01_kv; in: {scale:0.86, opacity:0, duration:0.5, ease:'back.out(1.7)'}; out: {opacity:0, duration:0.35, ease:'power2.in'})
  p#l(left: 16px; top: 12px; font-size: 13px; font-family: m; color: $ink2; content: {l})
  p#v(left: 16px; top: 30px; font-size: 31px; font-family: n; line-height: 1.15; content: {v})
stat#s01_st1(left: 593px; l: "回答者"; v: "800{uj}人{/}")
stat#s01_st2(left: 762px; l: "回答率"; v: "76{uj}%{/}")
stat#s01_st3(left: 931px; l: "実施"; v: "2026.9")
p#s01_note(left: 73px; top: 603px; font-size: 11px; font-family: m; color: $ink3; in: {opacity:0, duration:0.5, ease:'power1.out'}; out: {opacity:0, duration:0.35, ease:'power2.in'}) ※ 本動画に登場する企業・人物・数値はすべて架空のものです

# s02 調査の概要: 常設の層 (ロゴ・進行線) が降り、板の左に描かれる輪と数える 76%・中に 4 行の事実が語ごとに・右に挿絵と調べた 4 項目の札
section#s02(stagger: {each:0})
# 左上のロゴ (sticky・締めまで)
div#logo.sticky(left: 53px; top: 20px; width: 200px; height: 35px; z-index: front; in: {y:-8, opacity:0, duration:0.55, ease:'power3.out'}; out: {opacity:0, duration:0.4, ease:'power2.in'})
  svg#mark(left: 0px; cy: 50%; width: 31px; height: 31px; part: logo)
  p#b(left: 40px; top: 3px; font-size: 14px; font-family: h; letter-spacing: 0.06em) ソラリンク
  p#s(left: 40px; top: 20px; font-size: 10px; font-family: m; color: $ink2; letter-spacing: 0.04em) 人事部 ｜ 働き方調査 2026
# 上端の進行線 (sticky・2 場面目から終わりまで伸びる青→緑)
div#prog_track.sticky(left: 0px; top: 0px; width: 1280px; height: 4px; background: #34508F14; z-index: front; in: none; out: {opacity:0, duration:0.4})
progress#prog.sticky(left: 0px; top: 0px; width: 1280px; height: 4px; background: linear(#2F80ED,#12B5A6,90); until: end; z-index: front; overlap: prog_track; out: {opacity:0, duration:0.4})
chap#s02_chap(n: "01"; t: "調査の概要"; w: 157px)
board#b2(no: "01"; t: "調査の概要"; m: "株式会社ソラリンク ｜ 人事部 実施"; f: "出典：株式会社ソラリンク 人事部「働き方調査」（2026年9月実施）")
  # 回答率の輪 (淡い輪の上に紺の弧が 12 時から時計回りに描かれ、中の数字が同じ尺で数える)
  svg#ring(left: 64px; top: 104px; width: 267px; height: 267px; part: ring; delay: 300; in: {opacity:0, duration:0.4, ease:'power1.out'})
  shape#arc(path: "M197.5 130.8 L206.0 131.1 L214.4 132.1 L222.7 133.8 L230.9 136.2 L238.8 139.1 L246.5 142.7 L253.9 146.9 L260.9 151.7 L267.6 157.0 L273.7 162.8 L279.4 169.1 L284.6 175.9 L289.2 183.0 L293.3 190.5 L296.7 198.2 L299.5 206.2 L301.7 214.4 L303.2 222.8 L304.0 231.2 L304.2 239.7 L303.7 248.2 L302.5 256.6 L300.6 264.9 L298.1 273.0 L295.0 280.9 L291.2 288.5 L286.9 295.8 L281.9 302.7 L276.5 309.2 L270.5 315.3 L264.1 320.8 L257.3 325.9 L250.1 330.3 L242.5 334.2 L234.7 337.5 L226.6 340.1 L218.4 342.1 L210.0 343.5 L201.5 344.1 L193.0 344.1 L184.6 343.4 L176.2 342.1 L167.9 340.0 L159.9 337.4 L152.1 334.0 L144.5 330.1 L137.3 325.6 L130.5 320.6 L124.1 315.0 L118.2 308.9 L112.8 302.4 L107.9 295.4 L103.6 288.1 L99.8 280.5 L96.7 272.6 L94.3 264.5 L92.4 256.2 L91.3 247.8 L90.8 239.3 L91.0 230.8"; background: none; border: 29px solid $brand; z-index: front; in: draw {duration: 2.49})
  # 2 桁の数える数は語の count まで start の値 (0%) で止まる — 輪と一緒に「0%」で出し、弧を描く語で数える
  p#dv(cx: 197px; cy: 222px; font-size: 79px; font-family: n; line-height: 1; delay: 300; in: {opacity:0, duration:0.4, ease:'power1.out'}) [count:76 start=0 ms=2490]{u46}%{/}
  p#dl(cx: 197px; cy: 277px; font-size: 17px; color: $ink2; delay: 300; in: {opacity:0, duration:0.4, ease:'power1.out'}) 回答率
  p#cap(cx: 197px; cy: 408px; font-size: 17px; in: {y:9, opacity:0, duration:0.55, ease:'power3.out'}) 社員{n24}1,050{/}人中{n24}800{/}人が回答
  # 事実の 4 行 (小さな題 + 太い値 + 補足・下に罫)
  div#fact(left: 410px; top: "101;189;277;365"; width: 373px; height: 88px; in: {y:17, opacity:0, duration:0.55, ease:'power3.out'}) ×4
    div#ln(left: 0px; top: 87px; width: 373px; height: 1px; background: $line)
    p#l(left: 0px; cy: 25px; font-size: 13px; color: $ink3; letter-spacing: 0.12em) 実施;時期;対象;回答
    p#v(left: 0px; cy: 57px; font-size: 29px; font-family: h; line-height: 1.2) 人事部{fs}　全社員を対象に{/};{nn}2026{/}年{nn}9{/}月;社員 {nn}1,050{/}人{fs}　IT企業{/};{nn}800{/}人{fs}　回答率 76%{/}
  img#pic(left: 870px; top: 101px; width: 220px; height: 220px; object-fit: contain; delay: 450; in: {scale:0.86, opacity:0, duration:0.5, ease:'back.out(1.7)'}) [transparent]大きなクリップボードにチェックボックスと空欄の線が並ぶアンケート用紙、ペン、簡単な質問票を表示したスマートフォン、小さな円グラフと棒グラフのアイコンが浮かぶ。ひとまとまりの物を中央に、枠いっぱいに大きく描く
  p#ql(left: 824px; cy: 342px; font-size: 13px; color: $ink3; letter-spacing: 0.12em; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) 調べたこと（働き方ごとに比較）
  div#chip(left: "824;985;824;985"; top: "357;357;427;427"; width: 152px; height: 61px; border-radius: 12px; background: $tint; in: {scale:0.84, opacity:0, duration:0.5, ease:'back.out(1.7)', stagger:{each:0.12}}) ×4
    icon#i(left: 12px; cy: 50%; font-size: 23px; name: "smiley;trend-up;user;calendar-blank"; color: $brand)
    p#t(left: 43px; cy: 50%; font-size: 14px; line-height: 1.3) 満足度;生産性の[br]自己評価;孤独感;出社日数の[br]希望

# s03 いまの働き方: 100 点の単位図が灰で一斉に弾み出て、語ごとにハイブリッド → ほぼリモート → フル出社の順に点を塗り、右の行が数え上がる・実績の板で週の 5 枠が 2.2 日分埋まる
section#s03(stagger: {each:0})
chap#s03_chap(n: "02"; t: "いまの働き方"; w: 171px)
board#b3(no: "02"; t: "いまの働き方"; m: "回答者 800人"; f: "出典：人事部「働き方調査」（2026年9月, n=800）")
  p#lg(right: 37px; cy: 513px; font-size: 12px; font-family: m; color: $ink2; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}) {cn}●{/} 1つ＝8人　{cf}■{/} フル出社　{ch}■{/} ハイブリッド　{cr}■{/} ほぼリモート
  # 単位図 (10 × 10・1 点 = 8 人)。灰の点の上に色の点を重ね、語で 1 点ずつ溶かして塗る
  div#dot(left: "53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401;53;91.7;130.3;169;207.7;246.4;285;323.7;362.4;401"; top: "107;107;107;107;107;107;107;107;107;107;145.7;145.7;145.7;145.7;145.7;145.7;145.7;145.7;145.7;145.7;184.3;184.3;184.3;184.3;184.3;184.3;184.3;184.3;184.3;184.3;223;223;223;223;223;223;223;223;223;223;261.7;261.7;261.7;261.7;261.7;261.7;261.7;261.7;261.7;261.7;300.4;300.4;300.4;300.4;300.4;300.4;300.4;300.4;300.4;300.4;339;339;339;339;339;339;339;339;339;339;377.7;377.7;377.7;377.7;377.7;377.7;377.7;377.7;377.7;377.7;416.4;416.4;416.4;416.4;416.4;416.4;416.4;416.4;416.4;416.4;455;455;455;455;455;455;455;455;455;455"; width: 33px; height: 33px; border-radius: 99px; background: #E3E9F2; delay: 350; in: {scale:0.2, opacity:0, duration:0.32, ease:'back.out(2)', stagger:{each:0.005}}) ×100
  div#full(left: "53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7"; top: "107.0;107.0;107.0;107.0;107.0;107.0;107.0;107.0;107.0;107.0;145.7;145.7;145.7;145.7;145.7;145.7;145.7;145.7"; width: 33px; height: 33px; border-radius: 99px; background: $full; in: {scale:1.16, opacity:0, duration:0.3, ease:'power1.out', stagger:{each:0.008}}) ×18
  div#hyb(left: "362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7"; top: "145.7;145.7;184.3;184.3;184.3;184.3;184.3;184.3;184.3;184.3;184.3;184.3;223.0;223.0;223.0;223.0;223.0;223.0;223.0;223.0;223.0;223.0;261.7;261.7;261.7;261.7;261.7;261.7;261.7;261.7;261.7;261.7;300.4;300.4;300.4;300.4;300.4;300.4;300.4;300.4;300.4;300.4;339.0;339.0;339.0;339.0;339.0"; width: 33px; height: 33px; border-radius: 99px; background: $hyb; in: {scale:1.16, opacity:0, duration:0.3, ease:'power1.out', stagger:{each:0.008}}) ×47
  div#rem(left: "246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0;53.0;91.7;130.3;169.0;207.7;246.4;285.0;323.7;362.4;401.0"; top: "339.0;339.0;339.0;339.0;339.0;377.7;377.7;377.7;377.7;377.7;377.7;377.7;377.7;377.7;377.7;416.4;416.4;416.4;416.4;416.4;416.4;416.4;416.4;416.4;416.4;455.0;455.0;455.0;455.0;455.0;455.0;455.0;455.0;455.0;455.0"; width: 33px; height: 33px; border-radius: 99px; background: $rem; in: {scale:1.16, opacity:0, duration:0.3, ease:'power1.out', stagger:{each:0.008}}) ×35
  # 働き方の 3 行 (色の縦棒 + 名と出社日数 + 数える % + 人数・下に罫)
  div#row(left: 490px; top: "101;192;283"; width: 645px; height: 91px; in: {y:12, opacity:0, duration:0.55, ease:'power3.out'}) ×3
    div#ln(left: 0px; top: 90px; width: 645px; height: 1px; background: $line)
    div#bar(left: 0px; cy: 50%; width: 8px; height: 56px; border-radius: 4px; background: "$full;$hyb;$rem")
    p#nm(left: 23px; cy: 33px; font-size: 25px; font-family: h; line-height: 1.2) フル出社;ハイブリッド;ほぼリモート
    p#nt(left: 23px; cy: 61px; font-size: 15px; font-family: m; color: $ink2) 週5日 出社;週2〜3日 出社;週1日以下 出社
    p#pc(right: 115px; cy: 44px; font-size: 56px; font-family: n; line-height: 1) [count:18 start=0 ms=800]{u48}%{/};[count:47 start=0 ms=800]{u48}%{/};[count:35 start=0 ms=800]{u48}%{/}
    p#ct(right: 0px; cy: 46px; font-size: 17px; color: $ink2) {nk}144{/}人;{nk}376{/}人;{nk}280{/}人
  # 実績の板 (題 + 数える週 2.2 日 + 月〜金の 5 枠が 2.2 日分だけ左から埋まる)
  div#kpi(left: 490px; top: 400px; width: 645px; height: 95px; border-radius: 15px; background: $tint; in: {y:13, opacity:0, duration:0.55, ease:'power3.out'})
    p#l(left: 23px; cy: 39px; font-size: 16px) 出社日数の実績
    p#s(left: 23px; cy: 59px; font-size: 13px; font-family: m; color: $ink2) 全体の平均
    p#w(left: 171px; cy: 55px; font-size: 20px; font-family: h) 週
    p#v0(left: 194px; cy: 48px; font-size: 51px; font-family: n; line-height: 1) 0.0
    p#v(left: 194px; cy: 48px; font-size: 51px; font-family: n; line-height: 1; in: none) [count:2.2 start=0 ms=900]
    p#d(left: 276px; cy: 55px; font-size: 20px; font-family: h) 日
    div#wk(left: "387;435;483;531;579"; top: 24px; width: 43px; height: 28px; border-radius: 5px; background: #FFFFFF; border: 1px solid #CFD8E6) ×5
    div#wf(left: "387;435;483"; top: 24px; width: "43;43;9"; height: 28px; border-radius: 5px; background: $brand; in: {scaleX:0, duration:0.3, ease:'none', pivot:'left'}) ×3
    p#wl(cx: "408.5;456.5;504.5;552.5;600.5"; cy: 65px; font-size: 11px; color: $ink2) ×5 月;火;水;木;金

# s04 満足度: 左に全体の大きな数字 (数えて下の棒が 64% 伸びる)・右に目盛りと 3 本の横棒 (語ごとに伸びて数える)・全体 64% の破線・「最も高い」の札・フル出社とハイブリッドの差のかぎと 31 ポイント
section#s04(stagger: {each:0})
chap#s04_chap(n: "03"; t: "満足度"; w: 129px)
board#b4(no: "03"; t: "働き方への満足度"; m: "5段階で「4以上」と答えた人の割合"; f: "出典：人事部「働き方調査」（2026年9月, n=800）")
  p#lg(right: 37px; cy: 513px; font-size: 12px; font-family: m; color: $ink2; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}) {cf}■{/} フル出社　{ch}■{/} ハイブリッド　{cr}■{/} ほぼリモート　{ci}━{/} 全体の満足度
  div#hero(left: 37px; top: 101px; width: 293px; height: 393px; border-radius: 16px; background: $tint; delay: 400; in: {y:15, opacity:0, duration:0.55, ease:'power3.out'})
    p#l(left: 27px; cy: 81px; font-size: 21px; font-family: h) 全体
    p#v(left: 27px; cy: 157px; font-size: 100px; font-family: n; line-height: 1) [count:64 start=0 ms=900]{u43}%{/}
    p#s(left: 27px; cy: 227px; font-size: 18px; color: $ink2) {nk}515{/}人 ／ {nk}800{/}人
    div#tr(left: 27px; top: 268px; width: 240px; height: 15px; border-radius: 8px; background: #FFFFFF)
    div#bar(left: 27px; top: 268px; width: 154px; height: 15px; border-radius: 8px; background: $brand; in: {scaleX:0, duration:0.9, ease:'power2.out', pivot:'left'})
    p#c(left: 27px; cy: 305px; font-size: 13px; font-family: m; color: $ink2) 満足（4以上）と答えた人の割合
  # 目盛り (0〜100% = 547 px) と行の札・灰の帯
  div#gl(left: "549;686;823;959;1096"; top: 128px; width: 1px; height: 337px; background: $gl; delay: 350; in: {opacity:0, duration:0.5, ease:'power1.out'}) ×5
  p#ax(cx: "550;687;823;960;1097"; cy: 480px; font-size: 11px; font-family: m; color: $ink3; delay: 350; in: {opacity:0, duration:0.5, ease:'power1.out'}) ×5 0%;25%;50%;75%;100%
  div#lab(left: 370px; top: "148;268;388"; width: 167px; height: 73px; delay: 350; in: {opacity:0, duration:0.5, ease:'power1.out'}) ×3
    p#b(left: 0px; cy: 27px; font-size: 21px; font-family: h) フル出社;ハイブリッド;ほぼリモート
    p#n(left: 0px; cy: 53px; font-size: 13px; font-family: m; color: $ink3) n = 144人;n = 376人;n = 280人
  div#tk(left: 550px; top: "163;283;403"; width: 547px; height: 43px; border-radius: 3px; background: $track; delay: 350; in: {opacity:0, duration:0.5, ease:'power1.out'}) ×3
  # 横棒 (幅 = 値 × 547 px)・値の札は棒の右端に (語で数える)
  div#f_full(left: 550px; top: 163px; width: 224px; height: 43px; border-radius: 0px 4px 4px 0px; background: $full; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
  div#f_hyb(left: 550px; top: 283px; width: 393px; height: 43px; border-radius: 0px 4px 4px 0px; background: $hyb; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
  div#f_rem(left: 550px; top: 403px; width: 361px; height: 43px; border-radius: 0px 4px 4px 0px; background: $rem; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
  div#v_full(left: 786px; top: 148px; width: 120px; height: 73px; in: {opacity:0, duration:0.3, ease:'power1.out'})
    p#pv(left: 0px; cy: 25px; font-size: 35px; font-family: n; line-height: 1) [count:41 start=0 ms=800]{u54}%{/}
    p#pc(left: 0px; cy: 56px; font-size: 13px; font-family: m; color: $ink2) {nn}59{/} / {nn}144{/}人
  div#v_hyb(left: 955px; top: 268px; width: 120px; height: 73px; in: {opacity:0, duration:0.3, ease:'power1.out'})
    p#pv(left: 0px; cy: 25px; font-size: 35px; font-family: n; line-height: 1) [count:72 start=0 ms=800]{u54}%{/}
    p#pc(left: 0px; cy: 56px; font-size: 13px; font-family: m; color: $ink2) {nn}271{/} / {nn}376{/}人
  div#v_rem(left: 923px; top: 388px; width: 120px; height: 73px; in: {opacity:0, duration:0.3, ease:'power1.out'})
    p#pv(left: 0px; cy: 25px; font-size: 35px; font-family: n; line-height: 1) [count:66 start=0 ms=800]{u54}%{/}
    p#pc(left: 0px; cy: 56px; font-size: 13px; font-family: m; color: $ink2) {nn}185{/} / {nn}280{/}人
  # 全体 64% の破線 (上から下へ伸びる) と札
  shape#refl(path: "M898.7 128 L898.7 465"; background: none; border: 2px solid $ink; dash: 5,4; in: draw {duration: 0.6})
  p#reft(cx: 899px; cy: 111px; font-size: 13px; in: {y:-7, opacity:0, duration:0.55, ease:'power3.out'}) 全体 {nn}64%{/}
  div#badge(left: 1041px; top: 290px; width: 85px; height: 29px; border-radius: 99px; background: #E2F4EE; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(1.7)'})
    div#d(left: 11px; cy: 50%; width: 7px; height: 7px; border-radius: 99px; background: $hyb)
    p#t(left: 22px; cy: 50%; font-size: 13px) 最も高い
  # 差のかぎ (41% と 72% の棒の端から降りる破線 + 両矢印 + 札)
  shape#gd1(path: "M774 205.7 L774 244.3"; background: none; border: 1px solid $ink2; dash: 3,3; in: {opacity:0, duration:0.3, ease:'power1.out'})
  shape#gd2(path: "M943.3 244.3 L943.3 283"; background: none; border: 1px solid $ink2; dash: 3,3; in: {opacity:0, duration:0.3, ease:'power1.out'})
  shape#ga(path: "M778 244.3 L939.3 244.3 M784.7 239 L778 244.3 L784.7 249.7 M932.7 239 L939.3 244.3 L932.7 249.7"; background: none; border: 2px solid $ink; in: {scaleX:0.2, opacity:0, duration:0.45, ease:'back.out(1.6)'})
  p#gapl(left: 957px; cy: 244px; font-size: 15px; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(1.7)'}) 差 {n24}31{/}ポイント

# s05 生産性: 灰の帯の上に 3 色の積み上げが語ごとに左から伸び、中の % と人数が入る・「下がった」の端から赤の線が降り、淡い赤の板に理由の 2 枚が弾む
section#s05(stagger: {each:0})
chap#s05_chap(n: "04"; t: "生産性"; w: 129px)
board#b5(no: "04"; t: "生産性の自己評価"; m: "フル出社以外の 656人"; f: "出典：人事部「働き方調査」（2026年9月, フル出社以外 n=656）")
  p#lg(right: 37px; cy: 513px; font-size: 12px; font-family: m; color: $ink2; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}) {cb}■{/} 上がった　{cl}■{/} 変わらない　{cd}■{/} 下がった
  p#cap(left: 37px; cy: 113px; font-size: 17px; color: $ink2; delay: 350; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) 「出社中心だった頃と比べて」生産性は？
  div#tk(left: 37px; top: 136px; width: 1099px; height: 100px; border-radius: 5px; background: $track; delay: 350; in: {opacity:0, duration:0.4, ease:'power1.out'})
  # 積み上げの 3 区画 (幅 = 割合 × 帯)・中の文字は区画が伸びた後に下から
  div#seg(left: "37;455.7;950.3"; top: 136px; width: "416;492;185.3"; height: 100px; border-radius: 4px; background: "$brand;$flat;$down"; in: {scaleX:0, duration:0.55, ease:'power2.out', pivot:'left'}) ×3
  div#st(left: "37;455.7;950.3"; top: 136px; width: "416;492;185.3"; height: 100px; in: {y:7, opacity:0, duration:0.4, ease:'power3.out'}) ×3
    p#v(cx: 50%; cy: 36px; font-size: 43px; font-family: n; line-height: 1; color: "#FFFFFF;#16233E;#FFFFFF") 38{u53}%{/};45{u53}%{/};17{u53}%{/}
    p#n(cx: 50%; cy: 74px; font-size: 15px; color: "#FFFFFF;#16233E;#FFFFFF") 上がった ・ {nn}249{/}人;変わらない ・ {nn}295{/}人;下がった ・ {nn}112{/}人
  div#conn(left: 1042px; top: 238px; width: 3px; height: 60px; border-radius: 2px; background: $down; in: {scaleY:0, duration:0.35, ease:'power2.inOut', pivot:'top'})
  div#rs(left: 37px; top: 298px; width: 1099px; height: 196px; border-radius: 16px; background: $down_t; in: {y:13, opacity:0, duration:0.55, ease:'power3.out'})
    p#h(left: 29px; cy: 60px; font-size: 25px; font-family: h; delay: 150; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) 下がった理由
    p#s1(left: 29px; cy: 92px; font-size: 14px; font-family: m; color: $ink2; delay: 150; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) 上位にあがった回答
    p#s2(left: 29px; cy: 120px; font-size: 14px; font-family: m; color: $ink2; delay: 150; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) 対象：「下がった」112人
    div#rc(left: "253;675"; top: 31px; width: 397px; height: 133px; border-radius: 13px; background: #FFFFFF; box-shadow: 0px 7px 20px #D645451A; in: {scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.7)'}) ×2
      icon#k(left: 23px; cy: 50%; font-size: 20px; padding: 9.5px; name: quotes; weight: fill; color: #FFFFFF; background: $down)
      p#q(left: 78px; cy: 50%; font-size: 27px; font-family: h) 相談がすぐできない;家に作業環境がない

# s06 孤独感: 左に全体の数字 (数える) と在宅で一人の若手の絵・中の働き方別の縦棒 (ほぼリモートだけ遅れて高く伸び数える)・右の年代別 4 本 (語で 20 代を紫に塗り弾ませ、札と矢印)
section#s06(stagger: {each:0})
chap#s06_chap(n: "05"; t: "孤独感"; w: 129px)
board#b6(no: "05"; t: "孤独を感じることがある"; m: "回答者 800人"; f: "出典：人事部「働き方調査」（2026年9月, n=800）")
  p#lg(right: 37px; cy: 513px; font-size: 12px; font-family: m; color: $ink2; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}) {cf}■{/} フル出社　{ch}■{/} ハイブリッド　{cr}■{/} ほぼリモート　{cg}■{/} 年代（20代を強調）
  div#hero(left: 37px; top: 101px; width: 267px; height: 170px; in: {y:13, opacity:0, duration:0.55, ease:'power3.out'})
    p#l(left: 0px; cy: 15px; font-size: 20px; font-family: h) 全体
    p#v(left: 0px; cy: 87px; font-size: 93px; font-family: n; line-height: 1) [count:26 start=0 ms=900]{u43}%{/}
    p#s(left: 0px; cy: 151px; font-size: 17px; color: $ink2) {nk}206{/}人 ／ {nk}800{/}人
  img#pic(left: 60px; top: 268px; width: 224px; height: 224px; object-fit: contain; in: {scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.7)'}) [transparent]20代の若い会社員が自宅の小さな机で一人ノートPC に向かい、画面には誰も映っていないビデオ会議の格子、頬杖をついて少し寂しげな表情。マグカップ、窓、観葉植物。やさしく共感的な柔らかい光、明るいパステル調のまま。ひとまとまりの場面を中央に、枠いっぱいに大きく描く
  div#vd(left: "328;728"; top: 108px; width: 1px; height: 380px; background: $line) ×2
  # 働き方別 (縦棒の高さ = 値 × 8 px)
  p#ct1(left: 350px; cy: 114px; font-size: 20px; font-family: h; in: {opacity:0, duration:0.4, ease:'power1.out'}) 働き方別
  div#base1(left: 350px; top: 434px; width: 347px; height: 1px; background: $base; in: {opacity:0, duration:0.4, ease:'power1.out'})
  div#sb(left: "370;484"; top: "359.7;333"; width: 80px; height: "74.7;101.3"; border-radius: 4px 4px 0px 0px; background: "$full;$hyb"; in: {scaleY:0, duration:0.6, ease:'power2.out', pivot:'bottom', stagger:{each:0.15}}) ×2
  div#sb_rem(left: 597px; top: 215.7px; width: 80px; height: 218.7px; border-radius: 4px 4px 0px 0px; background: $rem; in: {scaleY:0, duration:0.8, ease:'power2.out', pivot:'bottom'})
  p#sv(cx: "410.3;523.7"; cy: "337;310.4"; font-size: 29px; font-family: n; line-height: 1; in: {y:7, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.15}}) ×2 14{u55}%{/};19{u55}%{/}
  p#sv_rem(cx: 637px; cy: 193px; font-size: 29px; font-family: n; line-height: 1; in: {opacity:0, duration:0.3, ease:'power1.out'}) [count:41 start=0 ms=800]{u55}%{/}
  div#sl(left: "350.3;463.7;577"; top: 442px; width: 120px; height: 40px; in: {y:7, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.1}}) ×3
    p#b(cx: 50%; cy: 11px; font-size: 16px) フル出社;ハイブリッド;ほぼリモート
    p#n(cx: 50%; cy: 29px; font-size: 11px; font-family: m; color: $ink3) {nn}20{/}人;{nn}71{/}人;{nn}115{/}人
  # 年代別 (淡い紫の 4 本・語で 20 代だけ濃い紫に)
  p#ct2(left: 750px; cy: 114px; font-size: 20px; font-family: h; in: {opacity:0, duration:0.4, ease:'power1.out'}) 年代別
  div#base2(left: 750px; top: 434px; width: 373px; height: 1px; background: $base; in: {opacity:0, duration:0.4, ease:'power1.out'})
  div#ab(left: "763.7;854.3;945;1035.7"; top: "226.3;306.3;327.7;343.7"; width: 66.7px; height: "208;128;106.7;90.7"; border-radius: 4px 4px 0px 0px; background: $age; in: {scaleY:0, duration:0.6, ease:'power2.out', pivot:'bottom', stagger:{each:0.12}}) ×4
  p#av(cx: "797;887.7;978.3;1069"; cy: "203.7;283.7;305;321"; font-size: 29px; font-family: n; line-height: 1; in: {y:7, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.12}}) ×4 39{u55}%{/};24{u55}%{/};20{u55}%{/};17{u55}%{/}
  div#al(left: "747;837.7;928.3;1019"; top: 442px; width: 100px; height: 40px; in: {y:7, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.08}}) ×4
    p#b(cx: 50%; cy: 11px; font-size: 16px) 20代;30代;40代;50代以上
    p#n(cx: 50%; cy: 29px; font-size: 11px; font-family: m; color: $ink3) {nn}78{/} / {nn}200{/}人;{nn}68{/} / {nn}280{/}人;{nn}41{/} / {nn}210{/}人;{nn}19{/} / {nn}110{/}人
  p#call(left: 901px; top: 128px; font-size: 16px; color: #FFFFFF; background: $age_hi; border-radius: 99px; padding: 7px 15px; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(1.7)'}) 若手ほど孤独が強い
  shape#arr(path: "M898.3 145 C870.3 147.7 854.3 158.3 846.3 178.3 M839.7 171.7 L845.7 181 L854.3 174.3"; background: none; border: 2px solid $age_hi; in: {opacity:0, duration:0.3, ease:'power1.out'})

# s07 希望の出社日数: 6 本の度数の縦棒が順に伸び、語で週 2 日を紺に (「中央」の札)・週 1 と 3 日を中間の青に塗ってかぎと 68%・右の 2 枚の板 (希望と実績の横棒と差の札 → 週 3 日以上の全体と 20 代)
section#s07(stagger: {each:0})
chap#s07_chap(n: "06"; t: "出社日数の希望"; w: 185px)
board#b7(no: "06"; t: "希望する出社日数"; m: "回答者 800人 ｜ 週あたり"; f: "出典：人事部「働き方調査」（2026年9月, n=800）")
  p#lg(right: 37px; cy: 513px; font-size: 12px; font-family: m; color: $ink2; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}) {cb}■{/} 中央（週2日）　{cm}■{/} 週1〜3日　{cn}■{/} その他
  div#base(left: 57px; top: 447.7px; width: 613px; height: 1px; background: $base; delay: 200; in: {opacity:0, duration:0.3, ease:'power1.out'})
  div#h(left: "71.7;173;274.3;375.7;477;578.3"; top: "280.3;265;227;333.7;417;401.7"; width: 77.3px; height: "167.3;182.7;220.7;114;30.7;46"; border-radius: 4px 4px 0px 0px; background: $neutral; delay: 400; in: {scaleY:0, duration:0.6, ease:'power2.out', pivot:'bottom', stagger:{each:0.1}}) ×6
  p#hv(cx: "110.3;211.7;313;414.3;515.7;617"; cy: "260.3;245;207;314;397;382"; font-size: 25px; font-family: n; line-height: 1; delay: 700; in: {y:7, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.1}}) ×6 22{u63}%{/};24{u63}%{/};29{u63}%{/};15{u63}%{/};4{u63}%{/};6{u63}%{/}
  div#hl(left: "63.7;165;266.3;367.7;469;570.3"; top: 455.7px; width: 93.3px; height: 34px; delay: 500; in: {y:7, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.08}}) ×6
    p#b(cx: 50%; cy: 11px; font-size: 16px) 0日;1日;2日;3日;4日;5日
    p#n(cx: 50%; cy: 28px; font-size: 11px; font-family: m; color: $ink3) {nn}176{/}人;{nn}192{/}人;{nn}232{/}人;{nn}120{/}人;{nn}32{/}人;{nn}48{/}人
  p#med(cx: 313px; cy: 245px; font-size: 12px; color: #FFFFFF; in: {y:-5, opacity:0, duration:0.55, ease:'power3.out'}) 中央
  shape#brk(path: "M174.3 186.3 L174.3 175.7 L451.7 175.7 L451.7 186.3"; background: none; border: 2px solid $ink; in: {y:8, opacity:0, duration:0.4, ease:'power3.out'})
  p#brl1(left: 228px; cy: 152px; font-size: 17px; in: {y:7, opacity:0, duration:0.55, ease:'power3.out'}) 週1〜3日で
  p#brl2(left: 333px; cy: 147px; font-size: 31px; font-family: n; line-height: 1; in: {y:7, opacity:0, duration:0.55, ease:'power3.out'}) [count:68 start=0 ms=700]%
  # 平均の板 (希望と実績の横棒が語で伸びて数える・差の黒札)
  div#pa(left: 717px; top: 101px; width: 419px; height: 188px; border-radius: 15px; background: $tint; in: {y:13, opacity:0, duration:0.55, ease:'power3.out'})
    p#t(left: 20px; cy: 27px; font-size: 17px; font-family: h) 平均の出社日数{s12}　週あたり{/}
    p#l1(left: 20px; cy: 70px; font-size: 17px) 希望
    div#b1(left: 83px; top: 56px; width: 129px; height: 27px; border-radius: 0px 4px 4px 0px; background: $brand; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'})
    p#v1(left: 221px; cy: 69px; font-size: 28px; font-family: n; line-height: 1; in: {opacity:0, duration:0.3, ease:'power1.out'}) [count:1.7 start=0 ms=600]{uj}日{/}
    p#l2(left: 20px; cy: 114px; font-size: 17px) 実績
    div#b2(left: 83px; top: 100px; width: 166px; height: 27px; border-radius: 0px 4px 4px 0px; background: $ink3; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'})
    p#v2(left: 259px; cy: 113px; font-size: 28px; font-family: n; line-height: 1; in: {opacity:0, duration:0.3, ease:'power1.out'}) [count:2.2 start=0 ms=600]{uj}日{/}
    p#dl(left: 20px; top: 143px; font-size: 14px; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 6px 13px; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(1.7)'}) 希望は実績より {n17}0.5{/}日 少ない
  div#pb(left: 717px; top: 304px; width: 419px; height: 191px; border-radius: 15px; background: $tint; in: {y:13, opacity:0, duration:0.55, ease:'power3.out'})
    p#t(left: 20px; cy: 27px; font-size: 17px; font-family: h) 週3日以上を望む人
    p#l1(left: 20px; cy: 73px; font-size: 17px) 全体
    div#b1(left: 83px; top: 59px; width: 141px; height: 27px; border-radius: 0px 4px 4px 0px; background: $brand; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'})
    p#v1(left: 235px; cy: 72px; font-size: 28px; font-family: n; line-height: 1; in: {opacity:0, duration:0.3, ease:'power1.out'}) [count:25 start=0 ms=600]{u50}%{/}
    p#l2(left: 20px; cy: 124px; font-size: 17px) 20代
    div#b2(left: 83px; top: 109px; width: 176px; height: 27px; border-radius: 0px 4px 4px 0px; background: $age_hi; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'})
    p#v2(left: 269px; cy: 123px; font-size: 28px; font-family: n; line-height: 1; in: {opacity:0, duration:0.3, ease:'power1.out'}) [count:31 start=0 ms=600]{u50}%{/}{fs}　62 / 200人{/}

# s08 職種別: 目盛りと職種の札・灰の横棒 4 本が順に伸び値が入り、全体の平均の破線が降りる・語でエンジニアと営業を紺に塗り、右にかぎと「2倍の開き」
section#s08(stagger: {each:0})
chap#s08_chap(n: "07"; t: "職種別の希望"; w: 171px)
board#b8(no: "07"; t: "職種別の希望出社日数"; m: "平均 ｜ 週あたり"; f: "出典：人事部「働き方調査」（2026年9月, n=800）")
  p#lg(right: 37px; cy: 513px; font-size: 12px; font-family: m; color: $ink2; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}) {cb}■{/} 最小・最大　{cn}■{/} その他の職種　{ci}━{/} 全体の平均
  # 目盛り (0〜3 日 = 600 px)
  div#g(left: "236.3;436.3;636.3;836.3"; top: 113px; width: 1px; height: 341px; background: $gl; delay: 300; in: {opacity:0, duration:0.4, ease:'power1.out'}) ×4
  p#ax(cx: "237;437;637;837"; cy: 473px; font-size: 13px; color: $ink3; delay: 300; in: {opacity:0, duration:0.4, ease:'power1.out'}) ×4 0日;1日;2日;3日
  div#l(left: 37px; top: "121;205;289;373"; width: 193px; height: 69px; delay: 300; in: {opacity:0, duration:0.4, ease:'power1.out'}) ×4
    p#b(left: 0px; cy: 25px; font-size: 21px; font-family: h) エンジニア;管理部門;企画・デザイン;営業
    p#n(left: 0px; cy: 51px; font-size: 13px; font-family: m; color: $ink3) n = 360人;n = 160人;n = 120人;n = 160人
  div#f(left: 237px; top: "135.7;219.7;303.7;387.7"; width: "260;340;380;520"; height: 40px; border-radius: 0px 4px 4px 0px; background: $neutral; delay: 450; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left', stagger:{each:0.12}}) ×4
  p#v(left: "507.7;587.7;627.7;767.7"; cy: "155.7;239.7;323.7;407.7"; font-size: 31px; font-family: n; line-height: 1; delay: 800; in: {y:7, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.12}}) ×4 1.3{uj}日{/};1.7{uj}日{/};1.9{uj}日{/};2.6{uj}日{/}
  shape#ref(path: "M576.3 122.3 L576.3 454.3"; background: none; border: 2px solid $ink; dash: 5,4; delay: 1050; in: draw {duration: 0.5})
  p#reft(left: 584px; cy: 111px; font-size: 13px; delay: 1250; in: {opacity:0, duration:0.3, ease:'power1.out'}) 全体の平均 {nn}1.7{/}日
  shape#brk(path: "M862.3 155.7 L878.3 155.7 L878.3 407.7 L862.3 407.7 M878.3 281.7 L893 281.7"; background: none; border: 2px solid $brand; in: {opacity:0, duration:0.3, ease:'power1.out'})
  div#call(left: 904px; top: 189px; width: 232px; height: 205px; delay: 100; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(1.7)'})
    p#big(left: 0px; top: 0px; font-size: 100px; font-family: n; color: $brand; line-height: 1) 2{bai}倍{/}
    p#t(left: 0px; top: 104px; font-size: 27px; font-family: h) の開き
    p#d1(left: 0px; top: 155px; font-size: 15px; color: $ink2) 最少　エンジニア {n17}1.3{/}日
    p#d2(left: 0px; top: 179px; font-size: 15px; color: $ink2) 最多　営業 {n17}2.6{/}日

# s09 自由記述: 6 語の順位の灰の棒が順に伸び件数が入り、右に通勤と雑談の 2 場面の絵・語で棒を声の向きの 3 色に塗り分け、色の札の行を 1 つずつ
section#s09(stagger: {each:0})
chap#s09_chap(n: "08"; t: "自由記述"; w: 143px)
board#b9(no: "08"; t: "自由記述の頻出語"; m: "記入 412人（回答者の 52%）"; f: "出典：人事部「働き方調査」自由記述（2026年9月, 記入 412人）")
  p#lg(right: 37px; cy: 513px; font-size: 12px; font-family: m; color: $ink2; delay: 500; in: {opacity:0, duration:0.5, ease:'power1.out'}) {cr}■{/} リモート志向の声　{cf}■{/} 出社志向の声　{ce}■{/} 環境・制度の声
  div#r(left: 37px; top: "107.7;171.7;235.7;299.7;363.7;427.7"; width: 640px; height: 53px; delay: 200; in: {opacity:0, duration:0.3, ease:'power1.out'}) ×6
    p#k(left: 0px; cy: 27px; font-size: 17px; font-family: n; color: $ink3) 1;2;3;4;5;6
    p#w(left: 27px; cy: 27px; font-size: 23px; font-family: h) 通勤;雑談;会議室;評価;質問しづらい;集中
  # 棒 (幅 = 件数 × 2.51 px)
  div#f(left: 217px; top: "119;183;247;311;375;439"; width: "346.7;241.3;178.7;160.7;146;130.7"; height: 31px; border-radius: 0px 4px 4px 0px; background: $neutral; delay: 400; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left', stagger:{each:0.1}}) ×6
  p#c(left: "573;467.7;405;387;372.3;357"; cy: "134.4;198.4;262.4;326.4;390.4;454.4"; font-size: 25px; font-family: n; line-height: 1; delay: 700; in: {y:5, opacity:0, duration:0.55, ease:'power3.out', stagger:{each:0.1}}) ×6 138{uj}件{/};96{uj}件{/};71{uj}件{/};64{uj}件{/};58{uj}件{/};52{uj}件{/}
  img#pic(left: 706px; top: 101px; width: 413px; height: 275px; object-fit: contain; delay: 550; in: {scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.7)'}) [transparent]1 枚の中で左右に分けた横長の構図。左は混み合う通勤電車でつり革を持つ疲れた会社員たち、右は明るいオフィスのラウンジのコーヒーマシンのそばで気軽に雑談して笑う同僚たち。両側を同じ画風で横に並べ、枠いっぱいに大きく描く
  div#vc(left: 690px; top: "383.7;422.3;461"; width: 445px; height: 32px; border-radius: 8px; background: $tint; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) ×3
    div#i(left: 12px; cy: 50%; width: 5px; height: 19px; border-radius: 3px; background: "$rem;$full;$env")
    p#b(left: 25px; cy: 50%; font-size: 14px) リモートを望む声;出社の場を望む声;「会議室」
    p#s(left: .b.right+8; cy: 50%; font-size: 13px; font-family: m; color: $ink2) 通勤の負担・集中;雑談・質問しづらい;オンライン会議用の個室が足りない

# s10 施策: 3 枚の破線の枠が先に並び、語ごとに淡い地・挿絵・番号・題・説明が入り、文の後半で根拠の行・3 枚目は 12 室 → 30 室を数える
section#s10(stagger: {each:0})
chap#s10_chap(n: "09"; t: "施策の提案"; w: 157px)
board#b10(no: "09"; t: "施策の提案"; m: "調査結果から導いた 3つの打ち手"; f: "出典：人事部「働き方調査」（2026年9月, n=800）をもとに人事部が提案")
  pcard#p1(left: 37px; no: "01"; t: "「チーム出社日」を[br]部署ごとに固定"; d: "一律の日数ではなく、[br]部署ごとに週2日を固定する"; b: "希望の中心は週2日・職種で希望が違う")
    img#pic [transparent]明るいオフィスで、多様な 5 人の同僚が週 1 回のチームの日に 1 つのテーブルを囲み、付箋とノートPC を前に笑顔で話し合っている。背後の壁のカレンダーに 2 日分の印。ひとまとまりの場面を中央に、枠いっぱいに大きく描く
  pcard#p2(left: 413px; no: "02"; t: "若手社員に[br]先輩の伴走役を付ける"; d: "対象は入社3年以内の社員[br]チーム出社日に週1回の 1on1"; b: "20代の 39% が孤独を感じている")
    img#pic [transparent]親しみやすい先輩社員が若い新入社員と 1 対 1 の面談をしている。小さな丸テーブルを挟んで座り、コーヒーカップとノート、二人とも笑顔で支え合う雰囲気。ひとまとまりの場面を中央に、枠いっぱいに大きく描く
  pcard#p3(left: 789px; no: "03"; t: "会議用の個室を増やし、[br]評価基準を明文化"; d: "オンライン会議用の個室"; b: "自由記述の「会議室」「評価」")
    img#pic [transparent]オフィスに置かれた現代的な防音の 1 人用の会議ブース 2 台、片方の中で人がノートPC とヘッドセットでビデオ通話をしている。きれいなガラスと明るい木。ひとまとまりの物を中央に、枠いっぱいに大きく描く
    # 個室の数 (12 室 → 語で 12 から 30 へ数える・数える語まで start の 12 で止まる)
    p#rm(left: 23px; cy: 293px; font-size: 25px; font-family: n; line-height: 1; delay: 350; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) 12{uj}室{/} {ar}→{/}
    p#n30(left: 100px; cy: 293px; font-size: 25px; font-family: n; line-height: 1; delay: 350; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) [count:30 start=12 ms=600]{uj}室{/}
    p#d3(left: 23px; cy: 320px; font-size: 14px; font-family: m; color: $ink2; delay: 350; in: {y:8, opacity:0, duration:0.55, ease:'power3.out'}) 評価基準を成果ベースで明文化

# s11 結論: 3 行の淡い板が語ごとに入り (番号 → 題 → 補足)、右の 2 枚の数字の札が弾む
section#s11(stagger: {each:0})
chap#s11_chap(n: "10"; t: "結論"; w: 115px)
board#b11(no: "10"; t: "結論"; m: "来期の出社方針に向けて"; f: "出典：人事部「働き方調査」（2026年9月, n=800）")
  crow#r1(top: 101px; num: "1"; head: "満足が最も高いのはハイブリッド"; sub: "一律の出社回帰は、満足を下げる"; c1: $hyb; k1: "ハイブリッドの満足"; v1: "72{u48}%{/}"; c2: $full; k2: "フル出社の満足"; v2: "41{u48}%{/}")
  crow#r2(top: 237px; num: "2"; head: "本当の課題は、場所より孤独"; sub: "孤独を感じる人が多いのは、ほぼリモートと20代"; c1: $rem; k1: "ほぼリモートの孤独"; v1: "41{u48}%{/}"; c2: $age_hi; k2: "20代の孤独"; v2: "39{u48}%{/}")
  crow#r3(top: 373px; num: "3"; head: "出社日数は、チーム単位で決める"; sub: "希望の中心は週1〜3日。ただし職種で2倍の差がある"; c1: $mid; k1: "週1〜3日の希望"; v1: "68{u48}%{/}"; c2: $brand; k2: "職種による差"; v2: "2{u48}倍{/}")

# 締め: 淡い地が溶けて覆い、ロゴ・題・調査の札・架空の注記が順に上がる (最後の frame まで)
section#end(stagger: {each:0})
div#ec_bg(inset: 0; background: linear(#F7FAFF,#E9F0FA,180); in: {opacity:0, duration:0.5, ease:'power1.out'})
svg#ec_logo(left: 612px; top: 232px; width: 56px; height: 56px; part: logo; delay: 200; in: {y:12, opacity:0, duration:0.55, ease:'power3.out'})
p#ec_t(cx: 640px; cy: 342px; font-size: 44px; font-family: h; letter-spacing: 0.02em; delay: 320; in: {y:12, opacity:0, duration:0.55, ease:'power3.out'}) 出社とリモート、社員800人の本音
p#ec_s(cx: 640px; cy: 402px; font-size: 19px; font-family: m; color: $ink2; delay: 440; in: {y:12, opacity:0, duration:0.55, ease:'power3.out'}) 株式会社ソラリンク 人事部 ｜ 働き方調査（2026年9月・回答 800人）
p#ec_n(cx: 640px; cy: 450px; font-size: 12px; font-family: m; color: $ink3; delay: 560; in: {y:12, opacity:0, duration:0.55, ease:'power3.out'}) ※ 本動画に登場する企業・人物・数値はすべて架空のものです
```

```timeline.txt
#v2
# hf の作り: 声は 1 人のナレーター (明るく高めの大人の女性) を 1.14 倍に詰めて 154 s。ここで引く話者は既定の速さで hf の話速に近い (114% は声が詰まりすぎる) ので速さは書かない・場面の頭と文の間は hf の間
cast n = "明るく高めの音域の大人の女性ナレーター、滑らかで粒立ちのよい明瞭な発音、快活で親しみやすく信頼感のある語り口"
silence head=0 tail=250
# 切替: 旧い板と章札の退場 (0.42 s) が次の板の入りに重なる = 混ぜない切替 (hf の boardOut は境目から走る)
transition = none,370

*** s01
bgm music
se hit -2dB +280
@n: [silence:0.6s]出社とリモート、社員800[>#s01_mark +30]人の本音。
[>#subtitle]
@: [>#s01_ci2 +50][♪pop_mid -8dB +50][>#s01_st1 +350][>#s01_st2 +510][>#s01_st3 +670]来期の出社[>#s01_note +70]方針を決める前に、[|]働き方調査の結果を報告します。[silence:0.45s]

*** s02
se whoosh -3dB
@n: [silence:0.25s][>#b2.fact[1] -150]調査[>#b2.ql +50][>#b2.chip[*] +170][♪tick -6dB +50]は[>#b2.fact[2] +100][♪pop_hi -6dB +100]2026年{9月|くがつ}。[|][>#b2.fact[3]][♪pop_hi -6dB]社員1,050人のうち[>#b2.fact[4] -100][♪pop_hi -6dB -100][!#b2.dv count +200][>#b2.arc +200][♪graph -8dB +200][>#b2.cap +150]800人が回答し、[|]回答率は76%でした。[silence:0.45s]

*** s03
se whoosh -3dB
@n: [silence:0.25s]いまの働き方は、[>#b3.hyb -350][>#b3.row[2] -350][>#b3.row[2].pc count -350][♪pop_mid -8dB -350]ハイブリッドが47%で最多。[|][>#b3.rem -150][>#b3.row[3] -150][>#b3.row[3].pc count -150][♪pop_mid -8dB -150]ほぼリモートが35%、[>#b3.full -100][>#b3.row[1] -100][>#b3.row[1].pc count -100][♪pop_mid -8dB -100]フル出社が18%です。
@: [>#b3.kpi -100]出社日数の実績は、平均[<#b3.kpi.v0 none +180][>#b3.kpi.v +180][>#b3.kpi.wf[1] +180][>#b3.kpi.wf[2] +480][>#b3.kpi.wf[3] +780]で週[♪bell -3dB +90]2.2日です。[silence:0.45s]

*** s04
se whoosh -3dB
@n: [silence:0.25s]働き方への満足度は、[!#b4.hero.v count][>#b4.hero.bar]全体で[♪bell -3dB]64%。
@: [>#b4.refl -150][>#b4.reft +50]最も高いのは[>#b4.f_hyb +150][>#b4.v_hyb +250][>#b4.v_hyb.pv count +250][♪pop_hi -6dB +150]ハイブリッドの[>#b4.badge +200][♪tick -6dB +200]72%で、[|][>#b4.f_rem -150][>#b4.v_rem +50][>#b4.v_rem.pv count +50][♪pop_hi -6dB -150]ほぼリモートが66%。
@: [>#b4.f_full -50][>#b4.v_full +50][>#b4.v_full.pv count +50][♪pop_hi -6dB -50]フル出社は41%にとどまり、[|]ハイブリッドとの[>#b4.gd1 -100][>#b4.gd2 -100][>#b4.ga +50][>#b4.gapl +200][♪shwip -4dB -100]差は31ポイントです。[silence:0.45s]

*** s05
se whoosh -3dB
@n: [silence:0.25s]出社中心だった頃と比べた生産性は、[>#b5.seg[1] -300][>#b5.st[1]][♪pop_mid -8dB -300]上がったが38%、[|][>#b5.seg[2] -100][>#b5.st[2] +200][♪pop_mid -8dB -100]変わらないが45%、[>#b5.seg[3] -100][>#b5.st[3] +200][♪pop_mid -8dB -100]下がったが17%。
@: [>#b5.conn -100][>#b5.rs +100]下がった理由の上位は[>#b5.rs.rc[1]][♪tick -6dB]「相談がすぐできない」[|][>#b5.rs.rc[2] +150][♪tick -6dB +150]「家に作業環境がない」です。[silence:0.45s]

*** s06
se whoosh -3dB
@n: [silence:0.25s][>#b6.hero -100]孤独を[>#b6.pic]感じることがある人は、[!#b6.hero.v count]全体で[♪bell -3dB]26%。
@: [>#b6.ct1 -600][>#b6.base1 -600][>#b6.sb[*] -350][>#b6.sl[*] -250][>#b6.sv[*] -50][♪pop_hi -6dB -350]ほぼリモート[>#b6.sb_rem][>#b6.sv_rem count +100][♪pop_mid -8dB]では41%に上ります。
@: [>#b6.ct2 -350][>#b6.base2 -350][>#b6.ab[*] -100][>#b6.al[*]][>#b6.av[*] +250][♪graph -8dB -100]年代別で[!#b6.ab[1] fill,$age_hi,duration=350 +200][!#b6.ab[1] punch,1.05,duration=320 +200]は20代が39%と最も高く、[|][>#b6.call -100][>#b6.arr +100][♪shwip -4dB -100]若手ほど孤独が強い傾向です。[silence:0.45s]

*** s07
se whoosh -3dB
@n: [silence:0.25s][♪graph -8dB -100]希望する出社日数は[!#b7.h[3] fill,$brand,duration=300 +300][>#b7.med +450][♪tick -6dB +300]週2日が最多で、[|][!#b7.h[2] fill,$mid,duration=300 -250][!#b7.h[4] fill,$mid,duration=300 -250][>#b7.brk -150][>#b7.brl1][♪shwip -4dB -250]週1日から3日が[>#b7.brl2 count +70]68%を占めます。
@: [>#b7.pa -150]希望の平均[>#b7.pa.b1][>#b7.pa.v1 +100][♪pop_hi -6dB]は週{1.7日|1.7にち}。[|][>#b7.pa.b2 +100][>#b7.pa.v2 +200][♪pop_hi -6dB +100]実績の{2.2日|2.2にち}[>#b7.pa.dl +150][♪bell -3dB +150]より{0.5日|0.5にち}少なめです。
@: [>#b7.pb -150]週3日以上の希望は、[|][>#b7.pb.b1 -100][>#b7.pb.v1 count][♪pop_mid -8dB -100]全体の25%に対し、20代[>#b7.pb.b2 +70][>#b7.pb.v2 count +170][♪pop_mid -8dB +70]では31%です。[silence:0.45s]

*** s08
se whoosh -3dB
@n: [silence:0.25s][♪graph -8dB -50]職種別では、[!#b8.f[1] fill,$brand,duration=300 -250][♪pop_hi -6dB -250]エンジニアの週1.3日から[!#b8.f[4] fill,$brand,duration=300 -100][♪pop_hi -6dB -100]営業の2.6日まで、[|][>#b8.brk -200][>#b8.call -200][♪bell -3dB -200]2倍の開きがあります。[silence:0.45s]

*** s09
se whoosh -3dB
@n: [silence:0.25s][♪graph -8dB -100]自由記述では、[!#b9.f[1] fill,$rem,duration=300 -300][!#b9.f[6] fill,$rem,duration=300 -300][>#b9.vc[1] -300][♪pop_hi -6dB -300]通勤や集中を理由にリモートを望む声と、[|][!#b9.f[2] fill,$full,duration=300 -250][!#b9.f[5] fill,$full,duration=300 -250][>#b9.vc[2] -250][♪pop_hi -6dB -250]雑談や質問のしにくさから出社の場を望む声が並びました。
@: [!#b9.f[3] fill,$env,duration=300 -50][!#b9.f[4] fill,$env,duration=300 -50][>#b9.vc[3] -50][♪tick -6dB -50]「会議室」は、オンライン会議用の個室が足りないという不満が中心です。[silence:0.45s]

*** s10
se whoosh -3dB
@n: [silence:0.25s]施策は三つです。
@: [card #b10.p1 -100][♪pop_hi -6dB -100]まず、部署ごとに週2日の「チーム出社[>#b10.p1.bt +80][♪tick -6dB +80]日」を固定する。
@: [card #b10.p2 -100][♪pop_hi -6dB -100]次に、入社3年以内の社員に先輩の伴走役を付け、[|][>#b10.p2.bt -100][♪tick -6dB -100]週1回の{1on1|ワンオンワン}を組む。
@: [card #b10.p3 -100][>#b10.p3.rm -100][>#b10.p3.n30 -100][>#b10.p3.d3 -100][♪pop_hi -6dB -100]そして、オンライン会議用の個室を12室[!#b10.p3.n30 count]から[♪bell -3dB +70]30室に増やし、[|][>#b10.p3.bt -100][♪tick -6dB -100]評価基準を成果ベースで明文化します。[silence:0.45s]

*** s11
se whoosh -3dB
@n: [silence:0.25s][>#b11.r1 -100][♪pop_mid -8dB -100]結論です。満足が最も高いの[>#b11.r1.c1 +75][>#b11.r1.c2 +75]はハイブリッド。[|][>#b11.r1.s -200]一律に出社へ戻せば、満足は下がります。
@: [>#b11.r2 -100][♪pop_mid -8dB -100]本当の課題は、場所[>#b11.r2.c1 +150][>#b11.r2.c2 +150]より孤独。
@: [>#b11.r3 -100][♪pop_mid -8dB -100]出社日数は、会社一律では[>#b11.r3.c1 +150][>#b11.r3.c2 +150]なく、[|]チーム単位で決めるべきです。[silence:0.35s]
[<#logo cut-0][<#prog cut-0][<#prog_track cut-0][<#subtitle]

*** end
se hit -2dB +100
@n: [silence:2.2s]
```

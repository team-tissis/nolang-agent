# concept · pm-roles (hf 全力版の全量の写し — PdM・PM・POなど開発チームの役割・プロダクト開発に関わる 6 役を同じ骨組みの場面で並べ、常設のヘッダーと役の色の帯で区切る) — canvas 1920x1080

見せる作り: 常設のヘッダー (6 役の札を役の場面で塗り、済んだ役は縁だけ残す)・役ごとの色の斜めの帯 (panel) が払う章の区切り・紺の題の札 (斜めの淡い帯・6 色の線・役の札)・略称の札が落ちて揺れすれ違う導入・役の場面の骨組みを def で 6 回 (淡い丸 + 浮遊する透過の人物・ROLE 0N と略称の大字・正式名と和名・POINT の帯)・場面ごとの図 (問いの札と枠・ガントの棒・VS の札と付箋・並び替わるバックログ・判子・1 行ずつ出るコード・色づくワイヤー・3 社の札・チェックリスト)・6 役のおさらいを 1 枚ずつ濃くする締め・音の層 (BGM + 語ごとの効果音 + 帯の風切り)

```design.txt
#v2
# 学ぶ作り: 全編の常設のヘッダー (左に研修の札・右に 6 役の札 — 役の場面で塗り、済んだ役は縁と字だけ役の色に残す) と、役ごとの色の斜めの帯 (panel) が払う章の区切り
# 役の場面は 1 つの骨組みを def で 6 回: 左に淡い丸 + 透過の人物 (浮遊)・右上に ROLE 0N + 略称の大字 + 英語の正式名 (頭文字だけ役の色) と和名 (略称の語で下から)・本文の札・下の POINT の帯 (左から開く)
# 本文の図は場面ごとに 1 つ: 問いの札 3 段と枠・管理 4 項目とガントの棒 → PdM と PM の VS 札と付箋・並び替わるバックログ・3 枚の札と承認の判子・1 行ずつ出るコードと画面とサーバー・色づくワイヤー・3 社の札とチェックリスト・6 役のおさらい
# hf b04 pm-roles (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#F6F4EF
theme light
palette ink=#1E2A4A sub=#5B6478 bg=#F6F4EF line=#ECE8DF pdm=#12A4A0 pm=#3E7BEA po=#E95C3A bo=#C88400 eng=#6A5AE0 des=#E2558E pdm_t=#E3F5F4 pm_t=#E6EFFD po_t=#FFF0EB bo_t=#FDF3DE eng_t=#EDEAFC des_t=#FCE9F1 yellow=#FFC24B
font "くせの無い現代的な太い角ゴシック体"
fonts h="極太の、清潔で中立的なゴシック体、客観的で現代的な印象" m="日本語も入る等幅のプログラミング用の書体"
sfx off
# hf の作り: 見出し・札は台詞より先に置く (spoiler)・章の帯の名は 0.8 秒で通り抜ける (flash_text)・注記と札の小さな字は 1080 の 18〜36px を 2/3 にした大きさ (small_text)
# hf の作り: 前の組が去った同じ場所に次の組が出る / 装飾の丸が札の後ろに敷かれる (empty_board)・役の場面は 15〜30 秒同じ人物の絵 (same_picture)・ヘッダーの役の札と場面の略称が同時に出る (duplicate_text)・役の色と淡色を直書きする (palette_drift)
lint off=spoiler,flash_text,small_text,empty_board,same_picture,duplicate_text,palette_drift
# hf の作り: 締めの NEXT STEP の帯は沈めた 6 枚の札の上に重ね、締めの札は全面を覆う (covered_text・overlap)・付箋のテープは紙の上にはみ出す (child_overflow)
# 章の帯 (panel) の窓は境界の 800 ms 前から: 帯が覆うのは窓の 340 ms 目 — cut 頭の要素は delay 400 で帯の裏から始め、cut 頭は 300 ms の無音 (ヘッダーの札の印をその中に)・cut 末は声の後 0.56 秒 (tail 250 + 310) — 帯が覆うのは声の 0.1 秒後
art "フラットなベクターのイラスト、清潔で現代的な企業向けの画風。単純な幾何学形状、なめらかなベタ塗りとごく弱い陰影、輪郭線なし。配色は濃紺・ティール・コーラル・暖かい黄色・淡い空色・明るい暖色グレーに限る。人物は点の目と小さな笑顔の親しみやすい顔"
prompt_tail "背景は完全な透過。背景の景色・地面の影の板・枠は描かない。文字・数字・ロゴは入れない"
# 人物は根の基準画像で全編を揃える (役の場面は全身・札とおさらいは同じ絵の上 1/3 を丸く切り抜いた顔)
image pdm = "[transparent]全身の人物: プロダクトマネージャーの30代前半の日本人女性。紺のブレザーにティールのトップス、明るい灰色のパンツ。斜め45度の向きで堂々と立ち、片手に大きな金色の方位磁針を持ち、もう片方の手で前方の上に浮かぶ暖かい黄色の光る星を指さす" aspect=2:3
image pm = "[transparent]全身の人物: プロジェクトマネージャーの30代前半の日本人男性。袖をまくった淡い空色のシャツに紺のスラックス。チェック印と線だけのチェックリストを挟んだクリップボードとペンを持って立つ。横にチェック印のついた小さなカレンダーの紙とコーラル色の小さな砂時計が浮かぶ" aspect=2:3
image po = "[transparent]全身の人物: プロダクトオーナーの20代後半の日本人女性。白いブラウスにコーラル色のカーディガン、紺のスカート。色とりどりの長方形の付箋を順位のように縦一列に積んだ高い列の横に立ち、ティールの付箋を1枚、列のいちばん上に置いている。付箋には点の印だけで文字はない" aspect=2:3
image bo = "[transparent]全身の人物: ビジネスオーナーの40代半ばの日本人男性。紺のスーツにティールのネクタイ、短く整えた髪。片手に紺の書類かばんを持ち、もう片方の手で、ティールと黄色の伸びる棒グラフ・上向きのコーラル色の矢印・金貨2枚が浮かぶ方を示す" aspect=2:3
image eng = "[transparent]全身の人物: ソフトウェアエンジニアの若い日本人男性。ティールのパーカー、濃紺のジーンズ、スニーカー。色の付いたコードの線 (色の棒だけで読める文字はない) が映る開いたノート PC を持って立つ。まわりに波括弧の形・歯車・小さなサーバーの積み重ねの小さな印が浮かぶ" aspect=2:3
image des = "[transparent]全身の人物: UI/UX デザイナーの若い日本人女性。からし色のセーター、紺のワイドパンツ、短いボブの髪。角丸の四角だけの簡単なアプリ画面のワイヤーフレームが映るタブレットと、反対の手にスタイラスを持って立つ。横にティール・コーラル・黄色の色見本の小さなパレットとマウスの矢印が浮かぶ" aspect=2:3
image team = "[transparent]横長の集合のイラスト: 年齢の違う日本人の同僚6人が長い白い会議机を囲む、和やかなプロダクト開発チームの打ち合わせ。1人は色とりどりの付箋を貼った小さなホワイトボードの前に立ち、2人はノート PC で作業し、1人はタブレットを持ち、1人は簡単なロードマップの図を指し、1人はマグカップを持って笑う。人物と机と持ち物だけ" aspect=3:2
image newbie_ask = "[transparent]2人のイラスト: 白いシャツに紺のパンツ、ティールのストラップの社員証を下げた新卒の若い日本人の新入社員が、小さな手帳を持って質問し、コーラル色のカーディガンの親しみやすい先輩が手のひらを開いて説明している。新入社員のそばに疑問符の形の小さな吹き出しが浮かぶ。2人とも全身で立つ" aspect=3:2
image newbie_confused = "[transparent]全身の人物: 白いシャツに紺のパンツ、ティールのストラップの社員証を下げた新卒の若い日本人の新入社員が、困った顔で頭をかいている。頭のまわりに空の吹き出しが3つと疑問符の形が2つ浮かぶ"
sound whoosh = "場面転換のシュッという短い風切り音"
sound sparkle = "デジタルにきらめく近未来的なチャイム"
sound pop_soft = "やわらかく小さいポンという出現音"
sound pop = "軽快なポンという出現音"
sound ping = "注意を引く高く澄んだピンという電子音"
sound click = "カチッという短いクリック音"
sound chime = "明るく短い正解のチャイム"
sound typing = "キーボードを軽快に打つタイプ音"
# 役の色の語 (字幕と見出し)・コードの色・小さな注記・下線の帯
# 章の帯の名札: 番号は名の半分の大きさで薄く (hf の `.wl small`)
run lsm { font-size: 50%; color: #FFFFFFCC }
run kpdm { color: $pdm }
run kpm { color: $pm }
run kpo { color: $po }
run kbo { color: $bo }
run keng { color: $eng }
run kdes { color: $des }
run ck { color: #FF9E7D }
run cf { color: #7FD6CF }
run cs { color: #FFD479 }
run cc { color: #7F8BAB }
run cn { color: #B3A8FF }
run sm { font-size: 0.72em; color: $sub }
run small { font-size: 0.8em }
run mk { marker: #FFC24BA6,40% }
# おさらいの札を 1 枚ずつ濃くし、顔を一度弾ませる
cue hl(x) = [!#x to,opacity=1,duration=250][!#x.rp to,scale=1.12,duration=200,repeat=1,yoyo,ease=sine.inOut]
p { color: $ink; out: none }
div { out: none }
img { out: none }
icon { out: none }
shape { out: none }
group { out: none }
# 字幕: 白い札 (薄い縁と影)・句 (hf の / ) は台詞の [|] で切る・役の名は役の色・出入りの動きは無い
subtitle.hug(bottom: 40px; width: 1860px; font-size: 46px; line-height: 1.35; letter-spacing: .02em; color: $ink; background: #FFFFFFF7; border: 2px solid #EBE7DE; border-radius: 20px; padding: 14px 44px 16px 44px; box-shadow: 0px 10px 30px #1E2A4A29; unit: sentence; lead: 0; tail: 250; hold: next,600; in: none; out: none)
bgm#music(fade: 350,1400; keys: "0:+6|2.65s:+6|3.15s:0|end-1.7s:0|end-1.2s:+4") 明るく軽快なピアノのリズムが刻む前向きな曲、企業の研修の解説動画向け、落ち着いたテンポ

# 全編の地: 生成りの紙に薄い点の格子
div#bg_base(inset: 0; background: $bg; pattern: dots,24,#D9D4C88C; z-index: back; in: none)

# 役の場面の骨組み (def 4 つ)
# 1. 右上の装飾の丸 (役の色の放射グラデ・場面の間ずっと左下へ漂う)
def deco(c) = div(left: 1280px; top: -380px; width: 1000px; height: 1000px; background: radial({c},#F6F4EF00@68%); delay: 400; in: {scale:.7, opacity:0, duration:1.2, ease:'power2.out'}; main: ramp {x: -90, y: 60})
# 2. 左の人物 (役の色の淡い丸 + 床の影 + 透過の人物が浮遊)
def role_char(img, t) = group(left: 70px; top: 150px; width: 560px; height: 740px)
  div#circle(left: 30px; top: 210px; width: 500px; height: 500px; border-radius: 1498px; background: {t}; delay: 400; in: {scale:.4, opacity:0, duration:.6, ease:'back.out(1.7)'})
  shape#floor.ellipse(left: 130px; top: 699px; width: 300px; height: 34px; background: #1E2A4A1A; delay: 550; in: {scale:.4, opacity:0, duration:.5, ease:'power3.out'})
  img#char(left: 46px; top: 26px; width: 466px; height: 700px; content: @{img}; object-fit: contain; delay: 470; in: {y:70, opacity:0, duration:.6, ease:'power3.out'}; main: sine {y: -8, period: 2.2})
# 3. 右上の見出し (ROLE 0N・略称の大字・英語の正式名と和名は略称の語で下から — 正式名の文字は実体の子 en に書く)
def role_head(n, a, ja, c, s=100, et=54, jt=96) = group(left: 680px; top: 110px; width: 1170px; height: 202px)
  p#chap(left: 4px; top: 0px; font-size: 26px; font-family: h; letter-spacing: .12em; color: {c}; delay: 500; in: {x:-30, opacity:0, duration:.4, ease:'power3.out'}; content: {n})
  p#acr(left: 0px; top: 46px; font-size: {s}; font-family: h; line-height: 1; letter-spacing: -.01em; color: {c}; delay: 530; in: {x:-40, opacity:0, duration:.5, ease:'power3.out'}; content: {a})
  p#en(left: .acr.right+34; top: {et}; font-size: 46px; line-height: 1.15; in: {y:24, opacity:0, duration:.45, ease:'power3.out'})
  p#ja(left: .acr.right+34; top: {jt}; font-size: 30px; color: $sub; in: {y:20, opacity:0, duration:.45, ease:'power3.out'}; content: {ja})
# 4. 下の POINT の帯 (役の色の板が左から開き、文が右から寄る)
def sum(t, c) = group(left: 680px; top: 760px; width: 1140px; height: 104px)
  div#bg(left: 0px; top: 0px; width: 1140px; height: 104px; border-radius: 22px; background: {c}; box-shadow: 0px 14px 34px #1E2A4A2E; in: wipe {dir: 'right', duration: 0.55, ease: 'power3.out'})
  p#pt(left: 34px; cy: 50%; font-size: 24px; font-family: h; letter-spacing: .1em; color: #FFFFFF; background: #14182847; border-radius: 10px; padding: 6px 16px; delay: 60; in: {opacity:0, duration:.15}) POINT
  p#st(left: 174px; cy: 50%; font-size: 50px; font-family: h; letter-spacing: .02em; color: #FFFFFF; white-space: nowrap; delay: 200; in: {x:30, opacity:0, duration:.45, ease:'power2.out'}; content: {t})

# title — 紺の地 (白い点の格子) に斜めの淡い帯 2 本・左に題の組 (シリーズ名 → 黄の札 → 2 行の大字 → 6 色の線 → 6 役の札)・右にチームの絵
section#title
div#t_bg(inset: 0; background: $ink; pattern: dots,24,#FFFFFF17; in: none)
div#t_b1.bleed(left: 900px; top: 120px; width: 1400px; height: 220px; border-radius: 40px; background: #12A4A029; transform: rotate(-14deg); in: {x:300, opacity:0, duration:.9, ease:'power3.out'})
div#t_b2.bleed(left: 1000px; top: 700px; width: 1400px; height: 220px; border-radius: 40px; background: #FF7A5924; transform: rotate(-14deg); delay: 100; in: {x:300, opacity:0, duration:.9, ease:'power3.out'})
img#t_team(left: 1110px; top: 350px; width: 760px; height: 507px; content: @team; object-fit: contain; delay: 350; in: {x:120, opacity:0, duration:.8, ease:'power3.out'}; main: keys(at=0 scale=1 | at=0.42 scale=1 | at=1 scale=1.04 ease=none),duration=2700)
p#t_series(left: 140px; top: 214px; font-size: 30px; letter-spacing: .08em; color: #CFD6E6; delay: 120; in: {y:-20, opacity:0, duration:.5, ease:'power3.out'}) 新入社員研修シリーズ ｜ 動画②　プロダクト開発に関わる役割を知る
p#t_pill(left: 140px; top: 286px; font-size: 52px; font-family: h; background: $yellow; border-radius: 16px; padding: 8px 30px; delay: 320; in: {scale:.6, opacity:0, duration:.5, ease:'back.out(1.7)'}) 3分でわかる！
p#t_l1(left: 136px; top: 400px; font-size: 100px; font-family: h; letter-spacing: .01em; color: #FFFFFF; white-space: nowrap; delay: 450; in: {y:50, opacity:0, duration:.55, ease:'power3.out'}) PdM・PM・POなど
p#t_l2(left: 136px; top: 536px; font-size: 114px; font-family: h; letter-spacing: .02em; color: #FFFFFF; white-space: nowrap; delay: 600; in: {y:50, opacity:0, duration:.55, ease:'power3.out'}) 開発チームの役割
div#t_bar(left: 140px; top: 704px; width: 900px; height: 14px; border-radius: 8px; background: linear($pdm,$pm,$po,$bo,$eng,$des,90); delay: 900; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
p#t_chip(left: "93;171;239;306;373;512"; top: 780px; font-size: 30px; font-family: h; color: #FFFFFF; background: "$pdm;$pm;$po;$bo;$eng;$des"; border-radius: 148px; padding: 8px 22px; delay: 1050; in: {scale:.5, opacity:0, duration:.45, ease:'back.out(1.7)', stagger:{each:.08}}) ×6 PdM;PM;PO;BO;エンジニア;デザイナー

# intro — チームの絵と 5 つの職種の札 → 3 つの略称の札が落ちて揺れ、すれ違い、？ と困った新人 → 6 役の札が並び、今回のゴールの帯
section#intro
# 常設のヘッダー (sticky・この cut の語で出し、締めの暗転で閉じる)。右の 6 役の札は役の場面で .on (塗り) → .done (縁と字が役の色)
div#hdr.sticky(left: 0px; top: 0px; width: 1920px; height: 110px; z-index: front; in: {y:-30, opacity:0, duration:.5, ease:'power3.out'}; out: {opacity:0, duration:.3, ease:'power1.in'})
  p#badge(left: 64px; top: 34px; font-size: 22px; font-family: h; letter-spacing: .04em; color: #FFFFFF; background: $ink; border-radius: 10px; padding: 6px 16px) 新入社員研修 ②
  p#ttl(left: .badge.right+16; cy: .badge.cy; font-size: 24px; font-family: h; letter-spacing: .02em) プロダクト開発に関わる役割を知る
  p#c(left: "835;891;939;987;1035;1137"; top: 32px; font-size: 21px; font-family: h; color: #85817A; background: #FFFFFF; border: 3px solid #CFCABF; border-radius: 148px; padding: 6px 16px) ×6 PdM;PM;PO;BO;エンジニア;デザイナー
#hdr.c.on(color: #FFFFFF; background: "$pdm;$pm;$po;$bo;$eng;$des"; border: "3px solid $pdm;3px solid $pm;3px solid $po;3px solid $bo;3px solid $eng;3px solid $des"; transform: scale(1.08))
#hdr.c.done(color: "$pdm;$pm;$po;$bo;$eng;$des"; background: #FFFFFF; border: "3px solid $pdm;3px solid $pm;3px solid $po;3px solid $bo;3px solid $eng;3px solid $des")
div#in_d1(left: -260px; top: 520px; width: 900px; height: 900px; background: radial(#12A4A029,#F6F4EF00@68%); delay: 400; in: {scale:.7, opacity:0, duration:1.2, ease:'power2.out'}; main: ramp {x: 70, y: -40})
div#in_d2(left: 1300px; top: -300px; width: 900px; height: 900px; background: radial(#FF7A5924,#F6F4EF00@68%); delay: 400; in: {scale:.7, opacity:0, duration:1.2, ease:'power2.out'}; main: ramp {x: 70, y: -40})
img#in_team(left: 480px; top: 176px; width: 960px; height: 640px; content: @team; object-fit: contain; delay: 500; in: {y:40, scale:.94, opacity:0, duration:.7, ease:'power3.out'}; out: {scale:.92, opacity:0, duration:.35, ease:'power1.in'}; main: keys(at=0 scale=1 | at=0.13 scale=1 | at=1 scale=1.05 ease=none),duration=6200)
# 5 つの職種の札 (白い丸の icon + 職種の語)
div#in_b(left: "167;127;1013;1053;967"; top: "167;373;147;333;480"; width: 170px; height: 158px; in: {scale:.3, opacity:0, duration:.5, ease:'back.out(1.7)', stagger:{each:.22}}; out: {opacity:0, duration:.3, ease:'power1.in'}) ×5
  icon#i(cx: 50%; top: 0px; font-size: 52px; name: "compass;calendar-blank;chart-bar;code;pen-nib"; color: "$pdm;$pm;$bo;$eng;$des"; background: #FFFFFF; padding: 26px; box-shadow: 0px 10px 26px #1E2A4A24)
  p#t(cx: 50%; top: 111px; font-size: 30px; font-family: h; color: "$pdm;$pm;$bo;$eng;$des") 企画;管理;ビジネス;開発;デザイン
# 3 つの略称の札 (上から傾いて落ちる・揺れる・1 と 2 が上下に逃げてすれ違う)
def tile(t) = div(top: 330px; width: 330px; height: 230px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; out: {y:-40, opacity:0, duration:.3, ease:'power1.in'})
  p#t(cx: 50%; cy: 50%; font-size: 120px; font-family: h; content: {t})
tile#in_t1(left: 240px; t: PdM; in: {y:-120, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
tile#in_t2(left: 620px; t: PM; in: {y:-120, rotation:5, opacity:0, duration:.55, ease:'back.out(1.6)'})
tile#in_t3(left: 1000px; t: PO; in: {y:-120, rotation:-4, opacity:0, duration:.55, ease:'back.out(1.6)'})
p#in_qm(left: "347;620;833"; top: "133;380;140"; font-size: 110px; font-family: h; color: $po; in: {scale:.2, opacity:0, duration:.45, ease:'back.out(1.7)', stagger:{each:.15}}; out: {y:-40, opacity:0, duration:.3, ease:'power1.in'}) ×3 ?;?;?
img#in_conf(left: 1360px; top: 300px; width: 520px; height: 520px; content: @newbie_confused; object-fit: contain; in: {x:160, opacity:0, duration:.55, ease:'power3.out'}; out: {x:120, opacity:0, duration:.3, ease:'power1.in'})
# 6 役の札 (丸い顔 = 人物の絵の上 1/3・略称・正式名)
div#in_rc(left: "73;260;447;633;820;1007"; top: 250px; width: 250px; height: 380px; in: {y:60, opacity:0, duration:.5, ease:'back.out(1.5)', stagger:{each:.12}}) ×6
  div#bg(inset: 0; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A)
  img#ph(cx: 50%; top: 26px; width: 196px; height: 196px; border-radius: 1498px; background: #FFFFFF; border: "8px solid $pdm;8px solid $pm;8px solid $po;8px solid $bo;8px solid $eng;8px solid $des"; content: "@pdm;@pm;@po;@bo;@eng;@des"; object-fit: cover; object-position: top; zoom: 200%)
  p#ac(cx: 50%; top: "160;160;160;160;165;165"; font-size: "35;35;35;35;27;27"; font-family: h; line-height: 1.1; color: "$pdm;$pm;$po;$bo;$eng;$des") PdM;PM;PO;BO;エンジニア;デザイナー
  p#jn(cx: 50%; top: 306px; font-size: 20px; color: $sub; white-space: nowrap) プロダクトマネージャー;プロジェクトマネージャー;プロダクトオーナー;ビジネスオーナー;Engineer;Designer
div#in_goal(left: 340px; top: 700px; width: 1238px; height: 94px; border-radius: 18px; background: $ink; in: {y:30, opacity:0, duration:.5, ease:'power3.out'})
  p#l(left: 40px; cy: 50%; font-size: 26px; font-family: h; letter-spacing: .1em; color: $yellow) 今回のゴール
  p#t(left: 231px; cy: 50%; font-size: 42px; font-family: h; color: #FFFFFF; white-space: nowrap) それぞれが「何を考える役割か」を大まかにつかむ

# pdm — 役 01: 問いの札 3 段が右から語ごとに入り、方向性の語で枠と札 (方位磁針が 1 回転)・まとめで POINT の帯
section#pdm
deco#pdm_deco(c: #12A4A024)
role_char#pdm_char(img: pdm; t: $pdm_t)
role_head#pdm_head(n: "ROLE 01"; a: PdM; ja: プロダクトマネージャー; c: $pdm)
  p#en {kpdm}P{/}ro{kpdm}d{/}uct {kpdm}M{/}anager
div#pdm_frame(left: 664px; top: 330px; width: 1172px; height: 418px; border-radius: 30px; border: 4px solid $pdm; in: {scale:1.06, opacity:0, duration:.5, ease:'power3.out'})
p#pdm_ftag(left: 1430px; top: 306px; font-size: 30px; font-family: h; color: #FFFFFF; background: $pdm; border-radius: 12px; padding: 6px 22px 6px 63px; in: {scale:.5, opacity:0, duration:.45, ease:'back.out(1.7)'}) プロダクト全体の方向性
  icon#i(left: 20px; cy: 50%; font-size: 34px; name: compass; color: #FFFFFF)
# 問いの札 (役の色の地の icon + 問い + 右端の英語の札)
def qcard(i, t, g) = div(width: 1140px; height: 114px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {x:80, opacity:0, duration:.5, ease:'power3.out'})
  icon#i(left: 30px; cy: 50%; font-size: 40px; name: {i}; color: $pdm; background: $pdm_t; border-radius: 20px; padding: 16px)
  p#t(left: 132px; cy: 50%; font-size: 44px; font-family: h; letter-spacing: .01em; white-space: nowrap; content: {t})
  p#g(right: 30px; cy: 50%; font-size: 22px; font-family: h; letter-spacing: .12em; color: $pdm; background: $pdm_t; border-radius: 10px; padding: 6px 14px; content: {g})
qcard#pdm_q(left: 680px; top: "237;324;411"; i: "cube;user;trend-up"; t: "「どんなプロダクトをつくるのか」;「誰のどんな課題を解決するのか」;「どうすれば事業として成長するのか」"; g: "WHAT;WHO;GROWTH") ×3
sum#pdm_sum(t: プロダクトの価値と方向性を考える人; c: $pdm)

# pm — 役 02: 管理の 4 項目が語ごとに弾み、ガントの棒が順に伸びて「計画通り」→ 前半を左へ払い、PdM と PM の VS 札 2 枚・下線の帯・補足の付箋
section#pm
deco#pm_deco(c: #3E7BEA24)
# 前半の組 (L09 の頭で群ごと左へ抜ける)
group#pm_a(out: {x:-60, opacity:0, duration:.35, ease:'power1.in'})
  role_char#char(img: pm; t: $pm_t)
  role_head#head(n: "ROLE 02"; a: PM; ja: プロジェクトマネージャー; c: $pm)
    p#en {kpm}P{/}roject {kpm}M{/}anager
    p#often(left: .en.right+16; cy: 102px; font-size: 22px; font-family: h; color: $pm; background: $pm_t; border: 3px solid $pm; border-radius: 148px; padding: 2px 12px; in: {y:24, opacity:0, duration:.45, ease:'power3.out'}) 多くの場合
  div#m(left: "453;648;843;1037"; top: 340px; width: 266px; height: 196px; in: {scale:.6, opacity:0, duration:.45, ease:'back.out(1.7)'}) ×4
    div#bg(inset: 0; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A)
    icon#i(cx: 50%; top: 26px; font-size: 44px; name: "calendar-blank;currency-jpy;users;gauge"; color: $pm; background: $pm_t; padding: 20px)
    p#t(cx: 50%; top: 124px; font-size: 36px; font-family: h) スケジュール;予算;人員;進捗
  div#gantt(left: 680px; top: 556px; width: 1140px; height: 186px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {y:30, opacity:0, duration:.45, ease:'power3.out'})
    p#gl(left: 30px; cy: "24;50;76;102"; font-size: 22px; color: $sub) ×4 要件定義;設計;開発;テスト
    div#bar(left: "120;244;380;566"; cy: "24;50;76;102"; width: "149;161;211;136"; height: 22px; border-radius: 10px; background: $pm; in: {scaleX:0, duration:.45, ease:'power2.out', pivot:'left', stagger:{each:.35}}) ×4
    p#ok(right: 24px; top: 16px; font-size: 24px; font-family: h; color: #FFFFFF; background: $pm; border-radius: 10px; padding: 4px 14px 4px 44px; in: {scale:.5, opacity:0, duration:.4, ease:'back.out(1.7)'}) 計画通り
      icon#i(left: 12px; cy: 50%; font-size: 26px; name: check; weight: bold; color: #FFFFFF)
  sum#sum(t: 計画通りにプロジェクトを進める人; c: $pm)
# 後半: PdM と PM の違い (VS の札 2 枚 + 中央の VS の丸 + 補足の付箋)
p#pm_vs_title(cx: 960px; top: 126px; font-size: 60px; font-family: h; in: {y:-24, opacity:0, duration:.45, ease:'power3.out'}) {kpdm}PdM{/} と {kpm}PM{/} の違い
def vcard(img, a, b, c, t, kw) = div(top: 230px; width: 780px; height: 470px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A)
  div#band(left: 0px; top: 0px; width: 780px; height: 132px; border-radius: 16,16,0,0; background: {c})
  img#av(left: 34px; top: 20px; width: 150px; height: 150px; border-radius: 1498px; background: #FFFFFF; border: 6px solid #FFFFFF; box-shadow: 0px 6px 16px #0000001F; content: @{img}; object-fit: cover; object-position: top; zoom: 200%)
  p#a(left: 214px; top: 20px; font-size: 54px; font-family: h; line-height: 1.05; color: #FFFFFF; transform-origin: left; content: {a})
  p#b(left: 214px; top: 80px; font-size: 26px; color: #FFFFFFEB; content: {b})
  p#q(left: 50px; top: 196px; font-size: 64px; font-family: h; line-height: 1.25; white-space: nowrap)
  p#kw(left: 50px; top: 390px; font-size: 24px; font-family: h; letter-spacing: .14em; color: {c}; background: {t}; border-radius: 10px; padding: 6px 14px; content: {kw})
  p#kv(left: .kw.right+16; cy: .kw.cy; font-size: 38px; font-family: h)
vcard#pm_vl(left: 110px; img: pdm; a: PdM; b: プロダクトマネージャー; c: $pdm; t: $pdm_t; kw: WHAT・WHY; in: {x:-80, opacity:0, duration:.55, ease:'power3.out'})
  p#q {kpdm}何を、なぜ{/}[br]つくるか
  p#kv {mk}を考える{/}
vcard#pm_vr(left: 1030px; img: pm; a: PM; b: プロジェクトマネージャー; c: $pm; t: $pm_t; kw: HOW; in: {x:80, opacity:0, duration:.55, ease:'power3.out'})
  p#q {kpm}どうやって{/}[br]計画通りにつくるか
  p#kv {mk}を管理する{/}
p#pm_vs(left: 904px; top: 405px; width: 110px; height: 110px; font-size: 34px; font-family: h; line-height: 110px; text-align: center; color: #FFFFFF; background: $ink; border-radius: 1498px; in: {scale:.3, opacity:0, duration:.5, ease:'back.out(1.7)'}) VS
# 補足の付箋 (黄の紙・上に半透明のテープ)
div#pm_note(left: 470px; top: 716px; width: 980px; height: 150px; background: #FFE89A; border-radius: 10px; box-shadow: 0px 14px 30px #1E2A4A33; in: {y:80, rotation:4, opacity:0, duration:.55, ease:'back.out(1.4)'})
  div#pin(cx: 50%; top: -14px; width: 120px; height: 30px; background: #FFFFFF99; transform: rotate(2deg))
  icon#i(left: 34px; top: 21px; font-size: 36px; name: lightbulb; color: #8A5A00)
  p#nt(left: 80px; top: 20px; font-size: 30px; font-family: h; color: #8A5A00) 補足
  p#nb(left: 34px; top: 68px; font-size: 44px; font-family: h; white-space: nowrap) 「PM」が Product Manager を指す企業もある

# po — 役 03: スクラムと価値の札が右に入り、バックログの 5 行が出て、優先順位の語で並び替わり (番号・最優先・上向きの矢印)
section#po
deco#po_deco(c: #FF7A5924)
role_char#po_char(img: po; t: $po_t)
role_head#po_head(n: "ROLE 03"; a: PO; ja: プロダクトオーナー; c: $po)
  p#en {kpo}P{/}roduct {kpo}O{/}wner
div#po_blog(left: 680px; top: 330px; width: 600px; height: 420px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {y:30, opacity:0, duration:.45, ease:'power3.out'})
  p#bh(left: 26px; top: 20px; font-size: 32px; font-family: h) プロダクトバックログ{sm}（やることの一覧）{/}
shape#po_arrow(left: 702px; top: 412px; width: 34px; height: 300px; path: arrow_u; background: $po; border: 4px solid $po; in: {scaleY:0, duration:.5, ease:'power2.out', pivot:'bottom'})
# バックログの行 (行ごとに語で縦に移って並び替わる・番号と最優先の札は後から弾む)
div#po_it(left: 752px; top: "267;310;353;396;439"; width: 500px; height: 56px; border-radius: 14px; background: $bg; in: {y:20, opacity:0, duration:.35, ease:'power3.out', stagger:{each:.08}}) ×5
  p#no(left: 18px; cy: 50%; width: 38px; font-size: 22px; font-family: h; line-height: 1; text-align: center; color: #FFFFFF; background: $po; border-radius: 148px; padding: 8px 0px; in: {scale:.3, opacity:0, duration:.35, ease:'back.out(2)', stagger:{each:.06}}) 3;1;5;2;4
  p#t(left: 69px; cy: 50%; font-size: 28px) お気に入り登録;会員登録・ログイン;ダークモード;商品の検索;レビュー投稿
#po_it.first(background: $po_t; border: 4px solid $po)
# 最優先の札は並び替えた後の 1 行目の右端に
p#po_top(right: 687px; cy: 428px; font-size: 20px; font-family: h; color: #FFFFFF; background: $po; border-radius: 8px; padding: 3px 12px; in: {scale:.3, opacity:0, duration:.35, ease:'back.out(2)'}) 最優先
def pinfo(i, t, d) = div(left: 1320px; width: 500px; height: 190px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {x:80, opacity:0, duration:.5, ease:'power3.out'})
  icon#i(left: 28px; top: 24px; font-size: 32px; name: {i}; color: $po; background: $po_t; border-radius: 16px; padding: 12px)
  p#t(left: 98px; top: 27px; font-size: 36px; font-family: h; content: {t})
  p#d(left: 28px; top: 93px; font-size: 26px; line-height: 1.45; color: $sub; content: {d})
pinfo#po_p1(top: 330px; i: arrows-clockwise; t: スクラム開発; d: "短い期間で「計画→開発→ふり返り」を[br]くり返す開発の進め方")
pinfo#po_p2(top: 542px; height: 206px; i: star; t: 価値を最大化; d: "価値の高いものから順に[br]つくれるよう、並びを決める")
sum#po_sum(t: 何から先につくるかを決める人; c: $po)

# bo — 役 04: 3 枚の札が下から語ごとに (責任者・目標の棒が伸びる・硬貨と承認の判子が落ちる)・PdM と PO を結ぶ線
section#bo
deco#bo_deco(c: #E39A0B29)
role_char#bo_char(img: bo; t: $bo_t)
role_head#bo_head(n: "ROLE 04"; a: BO; ja: ビジネスオーナー; c: $bo)
  p#en {kbo}B{/}usiness {kbo}O{/}wner
def bcard(i, t) = div(top: 330px; width: 366px; height: 262px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {y:50, opacity:0, duration:.5, ease:'power3.out'})
  icon#i(left: 24px; top: 22px; font-size: 30px; name: {i}; color: $bo; background: $bo_t; border-radius: 16px; padding: 12px)
  p#t(left: 90px; top: 27px; font-size: 32px; font-family: h; white-space: nowrap; content: {t})
bcard#bo_c1(left: 680px; i: buildings; t: 事業の責任者)
  p#s(left: 24px; bottom: 26px; font-size: 26px; line-height: 1.45; color: $sub) プロダクトを含む[br]事業全体を任される
bcard#bo_c2(left: 1066px; i: chart-bar; t: 売上・利益の目標)
  shape#tgt(left: 34px; top: 124px; width: 300px; height: 4px; path: line_h; border: 4px solid #D6CFC0; dash: 6,5)
  p#tl(right: 32px; top: 96px; font-size: 18px; color: $sub) 目標
  div#bar(left: "30;78;126;174"; bottom: 24px; width: 46px; height: "27;41;59;77"; border-radius: 5,5,0,0; background: "#F3D48E;#EFC163;#E2A42C;$bo"; in: {scaleY:0, duration:.5, ease:'power2.out', pivot:'bottom', stagger:{each:.12}}) ×4
bcard#bo_c3(left: 1454px; i: briefcase; t: 予算・投資の判断)
  div#coin(left: 40px; top: 108px; width: 116px; height: 116px; border-radius: 1498px; background: $yellow; in: {scale:.3, opacity:0, duration:.45, ease:'back.out(1.7)'})
    p#t(cx: 50%; cy: 50%; font-size: 64px; font-family: h; color: #8A5A00) ¥
  div#stamp(left: 182px; top: 112px; width: 146px; height: 106px; border-radius: 16px; border: 6px solid #E0443A; transform: rotate(-10deg); background: $panel; in: {scale:2.4, opacity:0, duration:.3, ease:'power4.in'})
    p#t(cx: 50%; cy: 50%; font-size: 46px; font-family: h; color: #E0443A) 承認
# PdM・BO・PO を線で結ぶ (中央の BO が先に弾み、線が伸びて両脇が出る)
group#bo_rel(left: 680px; top: 616px; width: 1140px; height: 126px)
  div#ln(left: "220;427"; top: 62px; width: "133;127"; height: 6px; border-radius: 3px; background: #D9D3C6; in: {scaleX:0, duration:.4, ease:'power2.out', pivot:'left'}) ×2
  p#lab(cx: 570px; top: 0px; font-size: 24px; font-family: h; letter-spacing: .1em; color: $sub; in: {y:10, opacity:0, duration:.4, ease:'power3.out'}) 連携しながら進める
  p#n1(left: 180px; top: 34px; font-size: 36px; font-family: h; color: #FFFFFF; background: $pdm; border-radius: 148px; padding: 8px 28px; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(1.7)'}) PdM
  p#n2(left: 525px; top: 28px; font-size: 42px; font-family: h; color: #FFFFFF; background: $bo; border-radius: 148px; padding: 8px 34px; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(1.7)'}) BO
  p#n3(left: 840px; top: 34px; font-size: 36px; font-family: h; color: #FFFFFF; background: $po; border-radius: 148px; padding: 8px 28px; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(1.7)'}) PO
sum#bo_sum(t: 事業の成果に責任を持つ人; c: $bo)

# eng — 役 05: 工程の札 3 つが語ごとに点灯し、エディタのコードが 1 行ずつ左から出る・画面 (スマホ) とサーバーの間を点が往復
section#eng
deco#eng_deco(c: #6A5AE024)
role_char#eng_char(img: eng; t: $eng_t)
role_head#eng_head(n: "ROLE 05"; a: エンジニア; ja: 開発者; c: $eng; s: 75; et: 29; jt: 69)
  p#en Engineer
group#eng_steps(in: {y:20, opacity:0, duration:.4, ease:'power3.out'})
  p#st(left: "453;578;808"; top: 326px; font-size: 32px; font-family: h; color: #A29E94; background: #FFFFFF; border: 3px solid #D6D0C4; border-radius: 148px; padding: 8px 26px) ×3 設計;プログラミング;テスト
  icon#ar(left: "544;774"; top: 342px; font-size: 34px; name: arrow-right; color: #C8C2B6) ×2
#eng_steps.st.on(color: #FFFFFF; background: $eng; border: 3px solid $eng)
# エディタ (紺の窓・上の帯に 3 つの点と file 名・コードは行ごとに左から拭いて出る)
div#eng_ed(left: 680px; top: 404px; width: 590px; height: 344px; border-radius: 20px; background: $ink; box-shadow: 0px 14px 34px #1E2A4A40; in: {y:40, opacity:0, duration:.45, ease:'power3.out'})
  div#eb(left: 0px; top: 0px; width: 590px; height: 44px; border-radius: 13,13,0,0; background: #16203A)
  div#dot(left: "12;27;41"; top: 15px; width: 14px; height: 14px; border-radius: 148px; background: "#FF6B6B;#FFC24B;#4CD4A0") ×3
  p#fn(left: 94px; top: 10px; font-size: 18px; font-family: m; color: #8F9BB8) app.js
  p#l1(left: 24px; top: 60px; font-size: 26px; font-family: m; color: #E8ECF5; white-space: nowrap; delay: 350; in: wipe {dir: 'right', duration: 0.35, ease: 'none'}) {cc}// 商品を検索する{/}
  p#l2(left: 24px; top: 102px; font-size: 26px; font-family: m; color: #E8ECF5; white-space: nowrap; delay: 680; in: wipe {dir: 'right', duration: 0.35, ease: 'none'}) {ck}function{/} {cf}search{/}(keyword) {
  p#l3(left: 54px; top: 142px; font-size: 26px; font-family: m; color: #E8ECF5; white-space: nowrap; delay: 1010; in: wipe {dir: 'right', duration: 0.35, ease: 'none'}) {ck}const{/} items = db.{cf}find{/}(keyword);
  p#l4(left: 54px; top: 184px; font-size: 26px; font-family: m; color: #E8ECF5; white-space: nowrap; delay: 1340; in: wipe {dir: 'right', duration: 0.35, ease: 'none'}) {ck}return{/} items.{cf}slice{/}({cn}0{/}, {cn}20{/});
  p#l5(left: 24px; top: 225px; font-size: 26px; font-family: m; color: #E8ECF5; delay: 1670; in: wipe {dir: 'right', duration: 0.35, ease: 'none'}) }
  p#l6(left: 24px; top: 267px; font-size: 26px; font-family: m; color: #E8ECF5; white-space: nowrap; delay: 2000; in: wipe {dir: 'right', duration: 0.35, ease: 'none'}) {cf}test{/}({cs}"検索できる"{/}, ...) {cc}// ✓ OK{/}
# 画面 (スマホの枠に色の棒が上から落ちて組み上がる)
div#eng_ph(left: 1330px; top: 404px; width: 190px; height: 280px; border-radius: 30px; background: #FFFFFF; border: 8px solid $ink; in: {y:40, opacity:0, duration:.45, ease:'power3.out'})
  div#pb(left: "14;14;14;14;32"; top: "14;44;110;132;154"; width: "99;99;99;99;63"; height: "23;60;16;16;20"; border-radius: 10px; background: "$eng;#D9D3FF;#E8E4DA;#E8E4DA;$po"; in: {y:-30, opacity:0, duration:.35, ease:'back.out(1.6)', stagger:{each:.1}}) ×5
div#eng_flow(left: 1530px; top: 540px; width: 100px; height: 8px; border-radius: 4px; background: #DDD7CA; in: {scaleX:0, duration:.35, ease:'power2.out', pivot:'left'})
shape#eng_d1.ellipse(left: 1530px; top: 534px; width: 20px; height: 20px; background: $eng; in: fade {duration: 0.2})
shape#eng_d2.ellipse(left: 1610px; top: 534px; width: 20px; height: 20px; background: $eng; in: fade {duration: 0.2})
# サーバー (紺の箱 3 段・青緑の灯と線)
div#eng_sv(left: 1640px; top: 440px; width: 150px; height: 208px; in: {x:60, opacity:0, duration:.45, ease:'power3.out'})
  div#sv(left: 0px; top: "0;49;98"; width: 150px; height: 62px) ×3
    div#bx(inset: 0; border-radius: 14px; background: $ink)
    div#i(left: 20px; top: 24px; width: 14px; height: 14px; border-radius: 148px; background: #7FD6CF)
    div#b(left: 50px; top: 27px; width: 70px; height: 8px; border-radius: 4px; background: #3C4A70)
p#eng_lf(left: 1296px; top: 690px; width: 258px; font-size: 22px; font-family: h; line-height: 1.2; text-align: center; color: $eng; background: $eng_t; border-radius: 10px; padding: 4px 12px; in: {scale:.5, opacity:0, duration:.4, ease:'back.out(1.7)'}) フロントエンド[br]{small}（画面側）{/}
p#eng_lb(left: 1598px; top: 690px; width: 236px; font-size: 22px; font-family: h; line-height: 1.2; text-align: center; color: $eng; background: $eng_t; border-radius: 10px; padding: 4px 12px; in: {scale:.5, opacity:0, duration:.4, ease:'back.out(1.7)'}) バックエンド[br]{small}（サーバー側）{/}
sum#eng_sum(t: 技術でプロダクトを形にする人; c: $eng)

# des — 役 06: スマホの灰色のワイヤーが「迷わず」の語で色づき、カーソルが押して波紋と「迷わず使える」の札・UI と UX の札が右に入る
section#des
deco#des_deco(c: #E2558E24)
role_char#des_char(img: des; t: $des_t)
role_head#des_head(n: "ROLE 06"; a: デザイナー; ja: UI / UX デザイン; c: $des; s: 75; et: 29; jt: 69)
  p#en Designer
p#des_l1(cx: 844px; top: 292px; font-size: 26px; font-family: h; color: $des; in: {y:10, opacity:0, duration:.35, ease:'power3.out'}; out: {opacity:0, duration:.2, ease:'power1.in'}) 見た目
p#des_l2(cx: 844px; top: 292px; font-size: 26px; font-family: h; color: $des; in: {y:10, opacity:0, duration:.35, ease:'power3.out'}) 使いやすさ
div#des_ph(left: 720px; top: 330px; width: 250px; height: 420px; border-radius: 36px; background: #FFFFFF; border: 9px solid $ink; in: {y:40, opacity:0, duration:.5, ease:'power3.out'})
  div#wb(left: "18;18;18;18;37"; top: "18;57;153;178;218"; width: "131;131;90;116;93"; height: "29;87;17;17;31"; border-radius: 10px; background: #E3E0D8) ×5
  div#ub(left: "18;18;18;18;37"; top: "18;57;153;178;218"; width: "131;131;90;116;93"; height: "29;87;17;17;31"; border-radius: 12px; background: "$des;#FFDED3;#F1D6E2;#F6E3EB;$ink"; in: {opacity:0, duration:.5, ease:'power1.inOut'}) ×5
# カーソル (白い矢印に紺の縁)・押した所に広がる輪・「迷わず使える」の札
shape#des_ring.ellipse(left: 796px; top: 632px; width: 96px; height: 96px; background: none; border: 4px solid $des; opacity: 0; in: keys(at=0 scale=0.19 opacity=0.9 | at=1 ease=power2.out),duration=600)
shape#des_cur(left: 836px; top: 676px; width: 56px; height: 56px; path: cursor; background: #FFFFFF; border: 2px solid $ink; in: {x:120, y:60, opacity:0, duration:.5, ease:'power2.out'})
p#des_ok(left: 990px; top: 612px; font-size: 24px; font-family: h; color: #FFFFFF; background: $des; border-radius: 12px; padding: 8px 14px 8px 45px; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(1.7)'}) 迷わず使える
  icon#i(left: 14px; cy: 50%; font-size: 26px; name: check; weight: bold; color: #FFFFFF)
def dcard(k, n, d) = div(left: 1240px; width: 580px; height: 176px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {x:80, opacity:0, duration:.5, ease:'power3.out'})
  p#k(left: 30px; cy: 50%; width: 110px; font-size: 76px; font-family: h; line-height: 1; text-align: center; color: $des; content: {k})
  p#n(left: 168px; top: 45px; font-size: 30px; font-family: h; content: {n})
  p#d(left: 168px; top: 93px; font-size: 28px; color: $sub; content: {d})
dcard#des_c1(top: 350px; k: UI; n: ユーザーインターフェース; d: 画面の見た目や操作する部分)
dcard#des_c2(top: 556px; k: UX; n: ユーザーエクスペリエンス; d: 使ったときの体験全体)
sum#des_sum(t: 使いやすさと体験を設計する人; c: $des)

# diff — 注意: 見出しの i が脈打ち、3 社の札 (兼ねる・1 人で複数・PM の別の意味) を語ごとに縁で光らせて顔と説明 → 上へ払い、新人と先輩の絵 + 確認のチェックリストに 3 つの ✓
section#diff
div#diff_deco(left: -300px; top: -300px; width: 1000px; height: 1000px; background: radial(#FF7A591F,#F6F4EF00@68%); delay: 400; in: {scale:.7, opacity:0, duration:1.2, ease:'power2.out'}; main: ramp {x: 90, y: 60})
# 3 社の札 (紺の帯に社名・中に役の札と顔・下に説明)。語ごとに .hl (外側の太い縁 + 少し拡大) で 1 枚ずつ光らせる
def ccard(t) = div(top: 270px; width: 500px; height: 470px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {y:60, opacity:0, duration:.5, ease:'power3.out'})
  div#hd(left: 0px; top: 0px; width: 500px; height: 96px; border-radius: 16,16,0,0; background: $ink)
    icon#i(left: 30px; cy: 50%; font-size: 46px; name: buildings; color: #FFFFFF)
    p#t(left: 93px; cy: 50%; font-size: 42px; font-family: h; color: #FFFFFF; content: {t})
  p#cl(left: 0px; bottom: 30px; width: 500px; font-size: 32px; font-family: h; text-align: center; in: {y:14, opacity:0, duration:.4, ease:'power3.out'})
def chip = p(top: 126px; font-size: 32px; font-family: h; color: #FFFFFF; border-radius: 148px; padding: 6px 22px; in: {scale:.4, opacity:0, duration:.4, ease:'back.out(1.7)'})
# 前半の組 (L20 の頭で群ごと上へ抜ける)
group#da(out: {y:-40, opacity:0, duration:.35, ease:'power1.in'})
  group#h(in: {y:-30, opacity:0, duration:.5, ease:'power3.out'})
    icon#i(left: 450px; top: 138px; font-size: 70px; name: info; color: $po)
    p#t(left: 543px; top: 140px; font-size: 64px; font-family: h; white-space: nowrap) 役割の定義は、企業によって異なる
  ccard#a(left: 150px; t: A社)
    chip#p1(left: 118px; background: $pdm) PdM
    p#plus(left: 242px; top: 120px; font-size: 40px; font-family: h; color: $sub; in: {scale:.4, opacity:0, duration:.4, ease:'back.out(1.7)'}) ＋
    chip#p2(left: 292px; background: $po) PO
    img#av(left: 176px; top: 204px; width: 150px; height: 150px; border-radius: 1498px; background: #FFFFFF; border: 6px solid $ink; content: @pdm; object-fit: cover; object-position: top; zoom: 200%; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(1.7)'})
    p#cl PdM が PO を兼ねる
  ccard#b(left: 710px; t: B社)
    img#av(left: 176px; top: 204px; width: 150px; height: 150px; border-radius: 1498px; background: #FFFFFF; border: 6px solid $ink; content: @eng; object-fit: cover; object-position: top; zoom: 200%; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(1.7)'})
    chip#p1(left: 44px; background: $pm) PM
    chip#p2(left: 152px; background: $po) PO
    chip#p3(left: 258px; background: $eng) エンジニア
    p#cl 1人で複数の役割
  ccard#c(left: 1270px; t: C社)
    chip#p1(left: 180px; top: 156px; font-size: 44px; background: $pm) PM
    p#c2(cx: 50%; top: 256px; font-size: 40px; font-family: h; line-height: 1.2; text-align: center; color: $pdm; in: {y:20, opacity:0, duration:.45, ease:'power3.out'}) ↓[br]Product Manager
    p#cl PM ＝ プロダクトマネージャー
#da.a.hl(box-shadow: 0px 0px 0px 8px $pdm; transform: scale(1.03))
#da.b.hl(box-shadow: 0px 0px 0px 8px $eng; transform: scale(1.03))
#da.c.hl(box-shadow: 0px 0px 0px 8px $pm; transform: scale(1.03))
# 後半: 新人と先輩の絵 + 確認のチェックリスト (行が順に上がり、✓ が 0.55 秒おきに弾む)
img#diff_ask(left: 110px; top: 300px; width: 820px; height: 548px; content: @newbie_ask; object-fit: contain; in: {x:-100, opacity:0, duration:.55, ease:'power3.out'})
div#diff_chk(left: 960px; top: 300px; width: 860px; height: 450px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; in: {y:40, opacity:0, duration:.5, ease:'power3.out'})
  icon#i(left: 44px; top: 38px; font-size: 54px; name: flag; color: $pdm)
  p#t(left: 114px; top: 36px; font-size: 46px; font-family: h) 配属されたら確認しよう
  div#ci(left: 44px; top: "100;160;220"; width: 780px; height: 50px; in: {y:16, opacity:0, duration:.35, ease:'power3.out', stagger:{each:.12}}) ×3
    div#bx(left: 0px; top: 0px; width: 50px; height: 50px; border-radius: 12px; border: 4px solid #CFC9BC; background: #FFFFFF)
    icon#ck(left: -2px; top: -6px; font-size: 54px; name: check; weight: bold; color: $pdm; in: {scale:.2, opacity:0, duration:.35, ease:'back.out(1.7)'})
    p#t(left: 72px; cy: 50%; font-size: 36px; white-space: nowrap) 自分のチームの PdM・PO は誰？;PM はどちらの意味で使っている？;1人で兼ねている役割はある？

# recap — おさらい: 6 役の札を薄く並べ、役の語ごとに 1 枚ずつ濃くして顔を弾ませる → 全部を沈めて NEXT STEP の帯 → 紺の締めの札
section#recap
group#rc_head(delay: 550; in: {y:-30, opacity:0, duration:.5, ease:'power3.out'})
  p#s(cx: 960px; top: 128px; font-size: 26px; font-family: h; letter-spacing: .3em; color: $sub) REVIEW
  p#t(cx: 960px; top: 158px; font-size: 64px; font-family: h) おさらい
div#rc(left: "100;467;833;100;467;833"; top: "187;187;187;381;381;381"; width: 520px; height: 262px; background: #FFFFFF; border-radius: 24px; border: 2px solid $line; box-shadow: 0px 12px 34px #1E2A4A1A; opacity: .35; in: {y:40, opacity:0, duration:.45, ease:'power2.out', stagger:{each:.07}}) ×6
  img#rp(left: 26px; cy: 50%; width: 166px; height: 166px; border-radius: 1498px; background: #FFFFFF; border: "8px solid $pdm;8px solid $pm;8px solid $po;8px solid $bo;8px solid $eng;8px solid $des"; content: "@pdm;@pm;@po;@bo;@eng;@des"; object-fit: cover; object-position: top; zoom: 200%)
  p#ra(left: 214px; top: "31;31;31;31;35;35"; font-size: "31;31;31;31;25;25"; font-family: h; line-height: 1.1; color: "$pdm;$pm;$po;$bo;$eng;$des") PdM;PM;PO;BO;エンジニア;デザイナー
  p#rk(left: 214px; top: 99px; font-size: 44px; font-family: h; line-height: 1.2; white-space: nowrap) 方向性;計画;優先順位;事業の成果;技術;使いやすさ
  p#rs(left: 214px; top: 159px; font-size: 20px; line-height: 1.4; color: $sub) プロダクトの価値と[br]方向性を考える人;計画通りにプロジェクトを[br]進める人;何から先につくるかを[br]決める人;事業の成果に[br]責任を持つ人;技術でプロダクトを[br]形にする人;使いやすさと体験を[br]設計する人
div#rc_close(left: 326px; top: 438px; width: 1269px; height: 192px; overlap: rc; border-radius: 26px; background: $ink; box-shadow: 0px 20px 50px #1E2A4A59; in: {scale:.7, opacity:0, duration:.55, ease:'back.out(1.7)'})
  p#s(left: 64px; top: 34px; font-size: 28px; font-family: h; letter-spacing: .12em; color: $yellow) NEXT STEP
  p#t(left: 64px; top: 76px; font-size: 60px; font-family: h; color: #FFFFFF; white-space: nowrap) 役割を知って、チームの会話に参加しよう
# 締めの札 (最後の句の語から +2050 = 声の直後に紺の全面が溶けて出て、シリーズ名・題・6 色の線が順に)
div#endcard(inset: 0; background: $ink; z-index: front; overlap: rc,rc_close,rc_head; in: {opacity:0, duration:.5, ease:'power1.inOut'})
  p#e1(cx: 960px; top: 448px; font-size: 32px; letter-spacing: .08em; color: #CFD6E6; white-space: nowrap; delay: 200; in: {y:20, opacity:0, duration:.4, ease:'power3.out'}) 新入社員研修シリーズ ｜ 動画② プロダクト開発に関わる役割を知る
  p#e2(cx: 960px; top: 512px; font-size: 64px; font-family: h; color: #FFFFFF; white-space: nowrap; delay: 300; in: {y:24, opacity:0, duration:.45, ease:'power3.out'}) 3分でわかる！ PdM・PM・POなど開発チームの役割
  div#e3(left: 640px; top: 620px; width: 640px; height: 12px; border-radius: 6px; background: linear($pdm,$pm,$po,$bo,$eng,$des,90); delay: 450; in: {scaleX:0, duration:.5, ease:'power3.out'})
```

```timeline.txt
#v2
cast n = "落ち着いた30代の女性のナレーター、研修の講師のように明るく丁寧に、はっきりと説明する"
silence head=0 tail=250
read PdM = ピーディーエム
read PM = ピーエム
read PO = ピーオー
read BO = ビーオー
read IT = アイティー
read UI = ユーアイ
read UX = ユーエックス

*** title
bgm music
se whoosh -1dB +50
se sparkle 0dB +420
@n: [silence:2.83s]
transition panel,800,color=#2B3A63,label="はじめに",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** intro
[>#subtitle]
@n: [silence:300][>#hdr -250][>#in_b[*] +900]ITのプロダクト開発では、[|]多くの専門職が一緒に仕事をします。
@: [<#in_team +530][<#in_b +530][>#in_t1 +880][♪pop_soft -1dB +880][>#in_t2 +2120][♪pop_soft -1dB +2120][>#in_t3 +3040][♪pop_soft -1dB +3040]その中でも「{kpdm}PdM{/}」「{kpm}PM{/}」「{kpo}PO{/}」など、[|][!#in_t1 to,{rotation:4, x:30, duration:.18, repeat:3, yoyo:true, ease:'sine.inOut'}][!#in_t2 to,{rotation:-4, duration:.18, repeat:3, yoyo:true, ease:'sine.inOut'} +50][!#in_t3 to,{rotation:4, x:-30, duration:.18, repeat:3, yoyo:true, ease:'sine.inOut'} +100]似た略称が多く、[!#in_t1 to,{x:380, duration:.5, ease:'power2.inOut'}][!#in_t1 to,{y:-70, duration:.25, ease:'sine.out', repeat:1, yoyo:true}][!#in_t2 to,{x:-380, duration:.5, ease:'power2.inOut'}][!#in_t2 to,{y:70, duration:.25, ease:'sine.out', repeat:1, yoyo:true}][!#in_t3 to,{y:-30, duration:.3, repeat:1, yoyo:true, ease:'sine.inOut'} +300][!#in_t1 to,{x:0, duration:.5, ease:'power2.inOut'} +750][!#in_t1 to,{y:70, duration:.25, ease:'sine.out', repeat:1, yoyo:true} +750][!#in_t2 to,{x:0, duration:.5, ease:'power2.inOut'} +750][!#in_t2 to,{y:-70, duration:.25, ease:'sine.out', repeat:1, yoyo:true} +750][>#in_qm[*] +100][>#in_conf -100][♪ping -1dB]最初は混乱しやすい用語があります。
@: 今回は、[<#in_t1 -400][<#in_t2 -400][<#in_t3 -400][<#in_qm -400][<#in_conf -400][>#in_rc[*] -50][♪pop -3dB]それぞれが何を考える役割なのかを[|][>#in_goal -50]大まかにつかみましょう。[silence:+310]
transition panel,800,color=$pdm,label="{lsm}01{/}  PdM",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** pdm
@n: [silence:300][!#hdr.c[1] .on -300]{kpdm}PdM{/}は[>#pdm_head.en][>#pdm_head.ja +180]{Product Manager|プロダクトマネージャー}の略です。
@: [>#pdm_q[1] -50][♪pop_soft -1dB]「どんなプロダクトをつくるのか」[|][>#pdm_q[2] -50][♪pop_soft -1dB]「誰のどんな課題を解決するのか」[|][>#pdm_q[3] -50][♪pop_soft -1dB]「どうすれば事業として成長するのか」など、[|][>#pdm_frame -50][>#pdm_ftag +100][!#pdm_ftag.i to,{rotation:360, duration:1.2, ease:'power2.inOut'} +300][♪click -2dB]プロダクト全体の方向性を考える役割です。
@: [silence:100]まとめると、{kpdm}PdM{/}は[>#pdm_sum -100][♪chime -1dB]「プロダクトの価値と方向性を考える人」です。[silence:+310]
transition panel,800,color=$pm,label="{lsm}02{/}  PM",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** pm
@n: [silence:300][!#hdr.c[1] .done -300][!#hdr.c[2] .on -300]{kpm}PM{/}は[>#pm_a.head.en][>#pm_a.head.often][>#pm_a.head.ja +180]{Project Manager|プロジェクトマネージャー}を指すことが多くあります。
@: プロジェクトの[>#pm_a.m[1] -50][♪pop_soft -2dB]スケジュール、[>#pm_a.m[2] -50][♪pop_soft -2dB]予算、[>#pm_a.m[3] -50][♪pop_soft -2dB]人員、[>#pm_a.m[4] -50][♪pop_soft -2dB]進捗などを管理し、[|][>#pm_a.gantt -250][>#pm_a.gantt.bar[*] +100][>#pm_a.gantt.ok +1600][>#pm_a.sum +300][♪chime -2dB]計画通りにプロジェクトを進める役割です。
@: [silence:150][<#pm_a -450][>#pm_vs_title -200][>#pm_vl][♪pop -2dB]{kpdm}PdM{/}が「何を、なぜつくるか」を考えるのに対し、[|][>#pm_vr -100][♪pop -2dB]{kpm}PM{/}は「どうやって計画通りにつくるか」を管理する、[|][>#pm_vs -100][!#pm_vl.kv{mk} marker][!#pm_vr.kv{mk} marker +250][♪click -1dB]という違いがあります。
@: [>#pm_note -50][!#pm_vr.a to,{scale:1.15, duration:.25, repeat:3, yoyo:true, ease:'sine.inOut'} +900][♪ping 0dB]なお、{kpm}PM{/}という略称が[|]{Product Manager|プロダクトマネージャー}を指す企業もあります。[silence:+310]
transition panel,800,color=$po,label="{lsm}03{/}  PO",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** po
@n: [silence:300][!#hdr.c[2] .done -300][!#hdr.c[3] .on -300]{kpo}PO{/}は[>#po_head.en][>#po_head.ja +180]{Product Owner|プロダクトオーナー}の略です。
@: [>#po_p1 -50][!#po_p1.i to,{rotation:360, duration:1.4, ease:'power2.inOut'} +300][♪pop_soft -2dB]スクラム開発などで使われる役割で、[|][>#po_p2 -50][♪pop_soft -2dB]プロダクトの価値が最大になるように、[|][>#po_blog -150][>#po_it[*] +100][♪pop -2dB]やることの一覧である「プロダクトバックログ」の[|][!#po_it[1] to,{y:129, duration:.55, ease:'power3.inOut'}][!#po_it[2] to,{y:-64, duration:.55, ease:'power3.inOut'}][!#po_it[3] to,{y:129, duration:.55, ease:'power3.inOut'}][!#po_it[4] to,{y:-129, duration:.55, ease:'power3.inOut'}][!#po_it[5] to,{y:-64, duration:.55, ease:'power3.inOut'}][>#po_arrow +200][>#po_it[*].no +500][>#po_top +800][!#po_it[2] .first +500][♪click -1dB][♪click -2dB +350]優先順位を決めます。
@: つまり{kpo}PO{/}は、[>#po_sum -100][♪chime -1dB]「何から先につくるかを決める人」です。[silence:+310]
transition panel,800,color=$bo,label="{lsm}04{/}  BO",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** bo
@n: [silence:300][!#hdr.c[3] .done -300][!#hdr.c[4] .on -300]{kbo}BO{/}は[>#bo_head.en][>#bo_head.ja +180]{Business Owner|ビジネスオーナー}の略です。
@: [>#bo_c1 -50][♪pop_soft -2dB]事業の責任者として、[|][>#bo_c2 -50][>#bo_c2.bar[*] +250][♪pop_soft -2dB]売上や利益などの目標を持ち、[|][>#bo_c3 -50][>#bo_c3.stamp][>#bo_c3.coin +100][♪click 0dB +250]予算や投資を判断します。
@: [>#bo_rel.n2 -100][>#bo_rel.ln[*] +100][>#bo_rel.n1 +300][>#bo_rel.n3 +400][>#bo_rel.lab +450][♪pop_soft -2dB]{kpdm}PdM{/}や{kpo}PO{/}と連携しながら、[|][>#bo_sum -100][♪chime -1dB]「事業の成果に責任を持つ人」です。[silence:+310]
transition panel,800,color=$eng,label="{lsm}05{/}  エンジニア",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** eng
@n: [silence:300][!#hdr.c[4] .done -300][!#hdr.c[5] .on -300][>#eng_head.en][>#eng_head.ja +180]{keng}エンジニア{/}は、[>#eng_steps -200][>#eng_ed -100][♪typing -7dB to=2.2s][!#eng_steps.st[1] .on]設計や[!#eng_steps.st[2] .on]プログラミング、[!#eng_steps.st[3] .on]テストを通して、[|][>#eng_ph -100][>#eng_ph.pb[*] +150][♪pop -3dB]プロダクトを実際につくる役割です。
@: [>#eng_lf -50][!#eng_ph to,{scale:1.06, duration:.25, repeat:1, yoyo:true, ease:'sine.inOut'}][♪pop_soft -2dB]画面側のフロントエンドや、[>#eng_sv -100][>#eng_lb +100][>#eng_flow +150][>#eng_d1 +400][!#eng_d1 to,{x:80, duration:.8, ease:'none', repeat:4} +400][>#eng_d2 +800][!#eng_d2 to,{x:-80, duration:.8, ease:'none', repeat:4} +800][♪pop_soft -2dB]サーバー側のバックエンドなど、[|]専門もさまざま。[>#eng_sum -100][♪chime -1dB]「技術でプロダクトを形にする人」です。[silence:+310]
transition panel,800,color=$des,label="{lsm}06{/}  デザイナー",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** des
@n: [silence:300][!#hdr.c[5] .done -300][!#hdr.c[6] .on -300][>#des_head.en][>#des_head.ja +180]{kdes}デザイナー{/}は、[>#des_ph -150][>#des_l1][♪pop_soft -2dB]画面の見た目だけでなく、[|][>#des_ph.ub[*] -100][<#des_l1 -100][>#des_l2 +50][>#des_cur +50][!#des_cur to,{scale:.85, duration:.12, repeat:1, yoyo:true} +550][>#des_ring +580][>#des_ok +750][♪click -1dB +550]ユーザーが迷わず使えるかまで考える役割です。
@: [>#des_c1 -50][>#des_c2 +600][♪pop_soft -2dB]「UI」や「UX」という言葉もよく使われます。[|][>#des_sum -100][♪chime -1dB]「使いやすさと体験を設計する人」です。[silence:+310]
transition panel,800,color=$ink,label="注意したいこと",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** diff
@n: [silence:300][!#hdr.c[6] .done -300][>#da.h -100][!#da.h.i to,{scale:1.25, duration:.25, repeat:3, yoyo:true, ease:'sine.inOut'} +300][>#da.a +700][>#da.b +850][>#da.c +1000][>#da.a.p1 +1100][>#da.a.plus +1180][>#da.a.p2 +1260][>#da.b.p1 +1300][>#da.b.p2 +1380][>#da.b.p3 +1460][>#da.c.p1 +1500][♪ping -1dB]ただし、ここで紹介した役割の定義は、[|]企業によって異なることがあります。
@: [!#da.a .hl -100][>#da.a.av +150][>#da.a.cl +400][♪pop -2dB]たとえば、{kpdm}PdM{/}が{kpo}PO{/}を兼ねる会社や、[|][=#da.a -300][!#da.b .hl -100][>#da.b.av +100][>#da.b.cl +400][=#da.b +1400][!#da.c .hl +1400][>#da.c.c2 +1600][>#da.c.cl +1900][♪pop -2dB]一人で複数の役割を担うチームもあります。
@: [=#da.c -500][<#da -450][>#diff_ask -100][>#diff_chk][>#diff_chk.ci[*] +250][>#diff_chk.ci[1].ck +600][♪click -2dB +600][>#diff_chk.ci[2].ck +1150][♪click -2dB +1150][>#diff_chk.ci[3].ck +1700][♪click -2dB +1700]配属されたら、自分のチームでは[|]誰がどの役割を担っているのか、確認してみましょう。[silence:+310]
transition panel,800,color=$ink,label="おさらい",skew=-12,label_skew=0,dir=left,se=whoosh -760

*** recap
@n: [silence:300][>#rc[*] +100]最後におさらいです。
@: [silence:50][hl #rc[1] -50][♪pop_soft -3dB]{kpdm}PdM{/}は方向性、[hl #rc[2] -50][♪pop_soft -3dB]{kpm}PM{/}は計画、[hl #rc[3] -50][♪pop_soft -3dB]{kpo}PO{/}は優先順位、[|][hl #rc[4] -50][♪pop_soft -3dB]{kbo}BO{/}は事業の成果、[hl #rc[5] -50][♪pop_soft -3dB]{keng}エンジニア{/}は技術、[hl #rc[6] -50][♪pop_soft -3dB]{kdes}デザイナー{/}は使いやすさを担います。
@: [!#rc[*] to,{opacity:.18, duration:.4} -100][!#rc_head to,{opacity:.18, duration:.4} -100][>#rc_close][♪sparkle -1dB]それぞれの役割を知って、[|][>#endcard +2050][<#hdr +2050]チームの会話に参加していきましょう。[silence:1.6s]
```

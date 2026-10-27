# data · cafe-weather-sales (hf 全力版の全量の写し — 雨の日、売れる店と売れない店・明るい紙の地に題の札つきの板を組む 9 場面の店舗データ図解) — canvas 1920x1080

見せる作り: 全編の地 (暖色の紙の写真 + 漂う光 + 周辺の陰)・2 場面目から常設の上端の帯 (社名・場面ごとに入れ替わる章札・8 つの点の上を場面の頭で滑る丸い帯の進行) を切替の上に残す・場面 = 語ごとに上がる見出し 3 語 + 題の札つきの板 (板の def)・横に押し出す切替と後半 2 回の紙が横切る切替・題の場面 (3 行の題と語で引く 2 色の下線・テープで貼った雨の街角の絵と降り続ける雨の筋)・0 から数える 112 日と 1 年の帯・月別の縦棒と 6〜7 月の帯とかぎと判子・2 本の横棒の数え上げと −6% の丸札・揺れる矢印の立地の札・立地のカード 3 枚 (絵が寄りから引く・前後 2 本の棒・増減の数字の判子)・カップの単位図 24 個が弾んで積む分布と上下のかぎと破線の囲み・積み上げの帯 2 本と 37% → 44% の破線・気温帯の縦棒と 50% の破線と 22℃ / 24℃ の境目 (破線が右へ滑る)・ルールの板と 56 日のマス・前後の点の比較 4 行 (点が左へ動き帯が伸びる)・廃棄額の判子と 9 個の点が薄れる品切れの札・まとめの 3 枚の札に丸の ✓・署名と全体が溶ける締め・音の層 (場の雨音・語に結んだ紙・ペン・木琴・判子の効果音 59)

```design.txt
#v2
# 学ぶ作り: 明るい紙の地 (紙の写真 + 漂う暖色の光 + 周辺の陰) の上に、場面 = 見出し 3 語 + 題の札つきの板 1〜3 枚 で 9 場面のデータ図解を組む
# 2 場面目から常設の上端の帯 (社名・章札の入れ替え・8 つの点の進行・下の線) を z curtain で切替の上に残し、場面は横に押し出す切替 (後半 2 回は紙が横切る)
# 図は数字の語と同時に伸びる: 月別の縦棒と 6〜7 月の帯とかぎ・2 本の横棒と丸札・立地のカード 3 枚・カップの単位図 24 個・積み上げの帯 2 本・気温帯の縦棒と 2 本の境目・前後の点の比較 (dumbbell)・56 日のマス・まとめの 3 枚の札
# hf d02 cafe-weather-sales (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#F1E6D3
theme light
palette paper=#F1E6D3 card=#FBF6EC ink=#3A2A1E ink2=#6B5444 terra=#C9573A terra_d=#A8432A terra_l=#EFB79F mustard=#E0A13A mustard_d=#8A5F12 sage=#7E9B62 sage_d=#566F3F rain=#4E7896 rain_d=#3A6180 rain_l=#B9CFDE fair=#B98B5E hot=#9C6B4E cold=#E39B48
font "癖の少ない角ゴシック体の太字、現代的で読みやすい"
fonts k="癖の少ない角ゴシック体の太字、現代的で読みやすい"
fonts m="癖の少ない角ゴシック体の普通の太さ、現代的で読みやすい"
fonts h="太く丸い丸ゴシック体の最も太いウェイト"
fonts n="表情のある極太のディスプレイ用セリフ欧文、有機的な曲線とレトロで温かい味わい、雑誌の見出しや料理の映像向け"
# engine: 数字の札は「万円」「店」「%」の和文と一緒なので欧文だけの書体に当たらず、和文も持つ太いセリフ体に解決される (hf の丸く太い欧文の数字より細身)
sfx off
# hf の作り: 見出しは場面の頭に結論ごと出し、台詞が後から数字を読む
lint off=spoiler
# hf の作り: 地は全編 1 枚の紙の写真 (場面は板と図で替える)
lint off=same_picture
# hf の作り: 板の中の注記・目盛り・凡例は 13〜15 px (1080 の 20〜22 px)
lint off=small_text
# hf の作り: 図の色 (薄い地・半透明の線・帯の色) は場面ごとに直書き
lint off=palette_drift
# hf の作り: 白い字は濃い色の丸札・帯の上 (check は全編の周辺の陰の幕と比べる)
lint off=low_contrast
# hf の作り: 場面の終わりに紙が全面を覆って横切る (sc7 → sc8 → sc9)
lint off=covered_text
# hf の作り: 立地のカード 3 枚と単位図の積み上げは語ごとに 8〜9 回の効果音を重ねる (飾りの木琴・判子・ペン)
lint off=se_dense
# hf の作り: 題の下の期間の注記と図の注記は最後の文の途中で出る
lint off=flash_text
# hf の作り: 試行のルールの板と結果の板の題の札が縦に並ぶ・まとめの札の題は台詞と同じ文
lint off=stacked_labels,duplicate_text
# hf の作り: 章札は前の札が上へ抜けた直後に同じ場所へ下から入る (時刻は重ならない)・写真の札のテープ 2 枚は台紙の角からはみ出して貼る
lint off=overlap,child_overflow
run t { color: $terra_d }
run r { color: $rain_d }
run up { marker: #EFB79FE6,30% }
run dn { marker: #B9CFDEF2,30% }
run b { color: $ink; font-family: k }
run cn { color: $terra_d; font-family: n; font-size: 1.08em }
run u { font-family: h; font-size: 0.36em }
run n2 { color: #8A5C34; font-family: n; font-size: 2.4em }
run pn { font-family: n; font-size: 1.67em }
run hv { font-family: n; font-size: 2em }
run pc { font-size: 0.58em }
run pp { font-size: 0.5em }
run vn { font-family: n; font-size: 1.55em }
run bn { font-family: n; font-size: 1.69em }
run gn { font-family: n; font-size: 1.25em }
run sp { font-size: 0.5em }
run sn { font-family: n; font-size: 1.29em }
run ip { font-size: 0.7em }
run mu { font-family: k; font-size: 0.62em }
run dd { color: $rain_d; font-family: n; font-size: 1.67em }
run pb { font-family: n; font-size: 1.27em }
run dv { font-family: n; font-size: 1.42em }
run tn { font-family: n; font-size: 2.36em }
run ta { color: $terra_d; font-family: n; font-size: 2.36em }
run tb { font-family: n; font-size: 1.46em }
run ft { color: $terra_d }
run fr { color: $rain_d }
run ftp { color: $terra_d; font-size: 0.53em }
run frp { color: $rain_d; font-size: 0.53em }
run fp { font-size: 0.53em }
run sl { color: $ink2; font-family: k; font-size: 0.66em }
run lb { color: $rain_d; font-family: k; font-size: 0.34em }
run av { font-family: h; font-size: 1.15em }
sound rain = "弱い雨がしとしと降る音とかすかな風の音"
sound paper = "紙を一枚手に取る乾いたカサッという音"
sound pageflip = "紙のページをめくる乾いた音"
sound pop = "短く明るい電子のチャイム、控えめな残響"
sound fuwan = "ゆっくり立ち上がる柔らかなサイン波のフワーンという短い音"
sound piron = "低めの澄んだ 2 音のシンセのベル、ピロン"
sound chime = "高く澄んだ金属のベルの一打、企業の映像向け"
sound swoosh = "高域の鋭く空気感のあるデジタルのシュッという音、深い残響"
sound pen = "太いフェルトペンで紙に直線を引くキュッという音"
sound pen_circle = "細いフェルトペンで紙に丸を描くキュキュッという音"
sound check = "鉛筆で紙にチェックを付けるカリッという音"
sound stamp = "判子を紙に押す乾いた音"
sound m1 = "木琴の温かい単音、いちばん低い音"
sound m2 = "木琴の温かい単音、少し低い音"
sound m3 = "木琴の温かい単音、真ん中の高さ"
sound m4 = "木琴の温かい単音、少し高い音"
sound m5 = "木琴の明るい単音、いちばん高い音"
sound m_up = "木琴の速い上昇のグリッサンド"
sound m_down = "木琴の速い下降のグリッサンド"
sound whoosh = "低めの柔らかい空気のヒュッという風切り、ほうきで掃くような音"
image paper = "[photo]温かいクリーム色 (生成り) の再生紙の白紙 1 枚を真上から撮った写真が画面いっぱいに広がる。細かな紙の繊維、ごく小さな斑点、ゆるやかな濃淡のむら。物も影も折り目も縁も文字も無い、継ぎ目のない一様な紙の質感の背景" aspect=16:9
image park = "雨の日の郊外の公園沿いのカフェ。濡れた木のテラスに人のいない椅子と閉じたパラソル、小道に水たまり、雨の中の木々、外に客はおらず店内に静かな暖かい灯り。画面いっぱいに風景を描き余白を作らない。温かく親しみやすいエディトリアルイラスト、リソグラフ印刷風 (平らな形・紙の粒子・少しずれたインク・手描きの縁)。色はテラコッタ・マスタード・コーヒーブラウン・セージグリーン、雨だけくすんだスレートブルー、生成りの紙の地。文字・数字・ロゴ・看板の文字は一切入れない" aspect=3:2
p { color: $ink; out: none }
div { out: none }
img { out: none }
shape { out: none }
icon { out: none }
# 字幕: 下端中央の生成りの札 (濃い茶の太字)・札 = 文 (長い文は読点で 2 枚に)・句末の約物は外す
subtitle.hug(bottom: 48px; font-size: 36px; line-height: 1.3; letter-spacing: 0.02em; text-align: center; color: $ink; background: #FBF6ECED; border-radius: 14px; padding: 9px 30px 10px 30px; box-shadow: 0px 6px 16px #5032141F; unit: sentence; strip: 、。; lead: 80; tail: 150; hold: off; in: {y:10, opacity:0, duration:0.18, ease:'power1.out'})
bgm#music(fade: 2000,2600) 明るく温かいボサノバ調のポップ、ピアノとアコースティックギターとやさしいドラム、雨の日のカフェの日常、店長会議の解説向け

# 上端の帯の部品の入退場 (上から降りる・終わりに溶ける)
motion tbar { in: {y:-20, opacity:0, duration:0.6, ease:'power2.out'}; out: {opacity:0, duration:0.7, ease:'power1.in'} }

# 見出し 3 語 (丸ゴシックの最も太い 40 px・語ごとに下から 90 ms おきに上がる・強調は run t / r)
def hl(a, b, c, d1=400, d2=490, d3=580) = div(left: 110px; top: 118px; width: 1700px; height: 72px)
  p#a(left: 0px; top: 0px; font-size: 60px; font-family: h; line-height: 1.2; white-space: nowrap; delay: {d1}; in: {y:46, opacity:0, duration:0.6, ease:'power3.out'}; content: {a})
  p#b(left: .a.right; top: 0px; font-size: 60px; font-family: h; line-height: 1.2; white-space: nowrap; delay: {d2}; in: {y:46, opacity:0, duration:0.6, ease:'power3.out'}; content: {b})
  p#c(left: .b.right; top: 0px; font-size: 60px; font-family: h; line-height: 1.2; white-space: nowrap; delay: {d3}; in: {y:46, opacity:0, duration:0.6, ease:'power3.out'}; content: {c})
# 板: 生成りの地 + 薄い縁 + 柔らかい影・左上に濃い茶の題の札 (板の縁に跨る)
def board(t) = div(background: $card; border-radius: 22px; border: 2px solid #785A3C24; box-shadow: 0px 18px 40px #5A3C1E1F; delay: 450; in: {y:40, opacity:0, duration:0.6, ease:'power3.out'})
  p#tab(left: 30px; top: -24px; font-size: 24px; letter-spacing: 0.02em; color: $card; background: $ink; border-radius: 10px; padding: 8px 20px 9px 20px; white-space: nowrap; content: {t})
# 上端の帯の章札 (番号は柔らかいセリフの欧文・場面の頭の 0.3 秒後に下から入り、次の場面の頭で上へ抜ける)
def chap = p(right: 321px; top: 40px; font-size: 24px; white-space: nowrap; z-index: curtain; delay: 350; in: {y:12, opacity:0, duration:0.45, ease:'power2.out'}; out: {y:-12, opacity:0, duration:0.3})
# 凡例の 1 項 (色の角丸の四角 + 語)
def leg(t, c) = div(height: 30px)
  div#sw(left: 0px; cy: 50%; width: 22px; height: 22px; border-radius: 4px; background: {c})
  p#t(left: 30px; cy: 50%; font-size: 22px; font-family: m; color: $ink2; white-space: nowrap; content: {t})
# 立地のカード: 上端の色の線・絵・名と店数・前後 2 本の棒・増減の大きな数字・向きの矢印 (絵と色の線は実体の群 ph = カードの角丸で切る窓 + in = 絵の帯 167 px で切る窓に入れる)
def loc(nm, cnt, cd, va, vb, wa, wb, pct, dir, ic, dc) = div(top: 248px; width: 540px; height: 668px; background: $card; border-radius: 22px; border: 2px solid #785A3C24; box-shadow: 0px 18px 40px #5A3C1E1F; in: {y:70, opacity:0, duration:0.7, ease:'power3.out'})
  p#name(left: 34px; top: 276px; font-size: 42px; font-family: h; white-space: nowrap; content: {nm})
  p#n(left: .name.right+14; top: 288px; font-size: 24px; color: {cd}; border: 2px solid {cd}; border-radius: 148px; padding: 4px 14px 4px 14px; content: {cnt})
  p#cap(left: 34px; top: 350px; font-size: 21px; font-family: m; color: $ink2) 1店あたりの1日売上
  p#la(left: 34px; top: 400px; font-size: 21px; color: $ink2) 晴れ・曇り
  p#lb(left: 34px; top: 456px; font-size: 21px; color: $ink2) 雨の日
  div#ba(left: 160px; top: 402px; width: {wa}; height: 34px; border-radius: 4px 8px 8px 4px; background: $fair; delay: 400; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  div#bb(left: 160px; top: 458px; width: {wb}; height: 34px; border-radius: 4px 8px 8px 4px; background: $rain; delay: 650; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  p#va(left: .ba.right+12; top: 396px; font-size: 22px; delay: 800; in: {x:-10, opacity:0, duration:0.35}; content: {va})
  p#vb(left: .bb.right+12; top: 452px; font-size: 22px; delay: 1050; in: {x:-10, opacity:0, duration:0.35}; content: {vb})
  icon#ar(left: 34px; bottom: 40px; font-size: 27px; name: {ic}; weight: bold; background: {dc}; color: $card; delay: 900; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'})
  p#dir(left: 86px; bottom: 46px; font-size: 24px; color: {dc}; delay: 900; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}; content: {dir})
  p#badge(right: 34px; bottom: 26px; font-size: 111px; font-family: n; line-height: 1; color: {dc}; in: {scale:1.6, opacity:0, rotation:-6, duration:0.45, ease:'back.out(2.2)'}; content: {pct})
# 前後の点の比較の行 (前年 = 白抜きの輪・試行 = 塗りの点が左へ動き、間の帯が右から伸びる)
def dbrow(l, va, vb, ax, bx, sl, sw) = div(left: 30px; width: 1030px; height: 56px; in: {x:-20, opacity:0, duration:0.4, ease:'power2.out'})
  p#l(left: 0px; cy: 50%; font-size: 26px; white-space: nowrap; content: {l})
  div#tk(left: 190px; top: 27px; width: 620px; height: 2px; background: #3A2A1E1F)
  div#sg(left: {sl}; top: 22px; width: {sw}; height: 12px; border-radius: 6px; background: #C9573A59; in: {scaleX:0, duration:0.9, ease:'power3.inOut', pivot:'right'})
  div#da(left: {ax}; top: 15px; width: 26px; height: 26px; border-radius: 148px; background: $card; border: 4px solid $hot)
  div#db(left: {bx}; top: 14px; width: 30px; height: 30px; border-radius: 148px; background: $terra; box-shadow: 0px 3px 8px #A8432A4D)
  p#va(left: 830px; cy: 50%; font-size: 24px; white-space: nowrap; content: {va})
  p#vb(left: .va.right+6; cy: 50%; font-size: 34px; font-family: n; color: $terra_d; in: {opacity:0, duration:0.3}; content: {vb})
  p#vp(left: .vb.right; cy: 50%; font-size: 24px) %
# まとめの札 (番号の丸・題 2 行・大きな数字の行・補足・破線の下の行動・右上の丸の ✓)
def card(no, t1, t2, fig, sub, n1, n2) = div(top: 256px; width: 540px; height: 610px; background: $card; border-radius: 22px; border: 2px solid #785A3C24; box-shadow: 0px 18px 40px #5A3C1E1F; in: {y:60, opacity:0, duration:0.65, ease:'power3.out'})
  div#no(left: 36px; top: 40px; width: 72px; height: 72px; border-radius: 148px; background: $terra_d)
    p#t(cx: 50%; cy: 50%; font-size: 44px; font-family: n; line-height: 1; color: $card; content: {no})
  p#t(left: 36px; top: 136px; font-size: 42px; font-family: h; line-height: 1.3; white-space: nowrap; content: "{t1}[br]{t2}")
  p#fig(left: 36px; top: 264px; font-size: 76px; font-family: n; line-height: 1.3; white-space: nowrap; content: {fig})
  p#sub(left: 36px; top: 360px; font-size: 22px; color: $ink2; white-space: nowrap; content: {sub})
  shape#rule(left: 36px; top: 480px; width: 468px; height: 3px; path: line_h; border: 2px solid #3A2A1E33; dash: 4,4)
  p#note(left: 36px; top: 504px; font-size: 26px; line-height: 1.45; white-space: nowrap; content: "{n1}[br]{n2}")
  shape#ring(left: 440px; top: 30px; width: 70px; height: 70px; border-radius: 50%; background: none; border: 4px solid $terra_d; in: {scale:0.5, opacity:0, duration:0.35, ease:'back.out(2.2)'})
  icon#ck(left: 453px; top: 45px; font-size: 42px; name: check; weight: bold; color: $terra_d; in: draw {duration: 0.35})

# 全編の地 (根): 紙の写真・左上から 93 秒かけて右下へ漂う暖色の光・周辺の陰
img#paper(inset: 0; content: @paper; main: none; look: #CDB996/#F6EBD8; z-index: back; in: none)
div#glow(left: -200px; top: -420px; width: 1100px; height: 1100px; border-radius: 550px; background: radial(#FFD6A059,#FFD6A000@65%,50%,50%); z-index: back; in: none; main: keys(at=0 x=0 y=0 scale=1 | at=1 x=600 y=253 scale=1.25 ease=sine.inOut),duration=93200)
veil#vig(background: radial(#FFFAF000@55%,#7A522C29@100%,50%,46%); z-index: back; in: none)

# sc1 題: 左に札 → 3 行の題 (行ごとに上がる) → 語で引く 2 色の下線 → 期間の注記・右に雨の街角の絵を貼った写真の札 (傾いて落ち、テープ 2 枚・雨の筋が降り続ける)
section#sc1(stagger: {each:0})
p#pill(left: 120px; top: 200px; font-size: 26px; letter-spacing: 0.04em; color: $card; background: $terra_d; border-radius: 148px; padding: 12px 24px 12px 24px; white-space: nowrap; delay: 350; in: {x:-45, opacity:0, duration:0.6, ease:'power3.out'}) こもれび珈琲　24店 × 天気データ
p#t1(left: 120px; top: 300px; font-size: 124px; font-family: h; line-height: 1.16; letter-spacing: 0.01em; white-space: nowrap; delay: 550; in: {y:90, opacity:0, duration:0.75, ease:'power4.out'}) 雨の日、
p#t2(left: 120px; top: 442px; font-size: 124px; font-family: h; line-height: 1.16; letter-spacing: 0.01em; white-space: nowrap; delay: 710; in: {y:90, opacity:0, duration:0.75, ease:'power4.out'}) {up}売れる店{/}と
p#t3(left: 120px; top: 585px; font-size: 124px; font-family: h; line-height: 1.16; letter-spacing: 0.01em; white-space: nowrap; delay: 870; in: {y:90, opacity:0, duration:0.75, ease:'power4.out'}) {dn}売れない店{/}
p#sub(left: 120px; top: 760px; font-size: 30px; font-family: m; color: $ink2; white-space: nowrap; in: {y:34, opacity:0, duration:0.6, ease:'power2.out'}) {b}2025年10月〜2026年9月{/}の日別売上 × 最寄り観測点の天気
# 写真の札: 生成りの台紙 (余白 12) の中に絵と雨の筋 (台紙の内側で切る)・-2° に傾けて置く
div#photo(left: 1010px; top: 168px; width: 800px; height: 646px; background: $card; border-radius: 10px; box-shadow: 0px 24px 50px #50321438; transform: rotate(-2deg); delay: 150; in: {y:-60, rotation:-5, opacity:0, duration:0.9, ease:'back.out(1.3)'})
  group#inner(left: 18px; top: 18px; width: 764px; height: 610px; clip: 3,photo.inner.hero)
    img#hero(inset: 0; main: kb {scale: [1.04, 1.13], focus: ['50% 50%', '53% 50%']}) 雨の日の日本の小さな町の角のカフェ。テラコッタ色の縞模様の日よけの下の大きな窓から暖かい金色の灯りがもれ、戸口に鉢植え。カフェの店先は画面の右半分。左半分には濡れた歩道を傘をさして歩く 2 人の後ろ姿、その奥に海辺の町並みと山並み、上には灰青の雨空と斜めの細い雨。路面に柔らかな映り込み。絵は画面の端から端まで描き込み、白い余白や紙の地だけの所を作らない。温かく親しみやすいエディトリアルイラスト、リソグラフ印刷風 (平らな形・紙の粒子・少しずれたインク・手描きの縁)。色はテラコッタ・マスタード・コーヒーブラウン・セージグリーン、雨だけくすんだスレートブルー、生成りの紙の地。明るく穏やかで居心地のよい雰囲気。文字・数字・ロゴ・看板の文字は一切入れない
    div#streak(left: "27;63;100;140;175;212;247;287;325;360;397;433;468;490;47;120;200;303;407;460"; top: -60px; width: 3px; height: 46px; border-radius: 2px; background: #4E78968C; transform: rotate(14deg); main: sawtooth {y: 720, period: 0.95, phase_offset: '0;0.326;0.653;0.179;0.505;0.832;0.095;0.421;0.747;0.253;0.579;0.905;0.137;0.463;0.789;0.295;0.621;0.053;0.379;0.705'}) ×20
  div#tape1(left: -40px; top: -14px; width: 150px; height: 42px; border-radius: 3px; background: #E0A13A8C; transform: rotate(-24deg); delay: 550; in: {scale:0.4, opacity:0, duration:0.35, ease:'back.out(2)'})
  div#tape2(left: 692px; top: -10px; width: 150px; height: 42px; border-radius: 3px; background: #E0A13A8C; transform: rotate(21deg); delay: 670; in: {scale:0.4, opacity:0, duration:0.35, ease:'back.out(2)'})

# sc2 雨の日の数: 上端の帯が降りる・左に札 → 0 から数える 112 日 → 253 日・1 年の帯・注記・右の板に月別の縦棒 12 本 (6・7 月だけ濃い)、語で 6〜7 月に帯とかぎ → 「年間の 27%」の判子
section#sc2(stagger: {each:0})
# 上端の帯 (sticky・z curtain = 押し出しの切替と横切る紙の上に残る — 子を持つ箱は z curtain に置けないので部品ごとに): 社名の印と題・右に 8 つの点 (今の場面は横長の濃い点)・下の細い線
div#tb_mark.sticky(left: 110px; top: 42px; width: 30px; height: 30px; border-radius: 148px; background: $terra; z-index: curtain; delay: 100; in: tbar)
div#tb_slash.sticky(left: 123px; top: 48px; width: 4px; height: 18px; border-radius: 2px; background: $card; transform: rotate(18deg); z-index: curtain; delay: 100; in: tbar)
p#tb_brand.sticky(left: 153px; cy: 57px; font-size: 24px; white-space: nowrap; z-index: curtain; delay: 100; in: tbar) こもれび珈琲
div#tb_sep.sticky(left: 309px; cy: 57px; width: 2px; height: 22px; background: #3A2A1E4D; z-index: curtain; delay: 100; in: tbar)
p#tb_sub.sticky(left: 324px; cy: 57px; font-size: 22px; font-family: m; color: $ink2; white-space: nowrap; z-index: curtain; delay: 100; in: tbar) 店長会議｜雨と売上の分析
# 点の進行: 今の場面の点が右端を留めて 20 px の横長の丸い帯 (濃い茶) に伸び、場面の頭の語で次の点が伸びる。済んだ点は左端を留めて 7 px に戻り薄い茶の点になる (= 13 px 左へ寄った点・timeline の to の w と x)
div#tb_dot.sticky(left: "1115;1127;1139;1151;1163;1175;1187;1199"; top: 52px; width: 10px; height: 10px; border-radius: 148px; background: #3A2A1E38; z-index: curtain; delay: 100; in: tbar) ×8
div#tb_line.sticky(left: 110px; top: 96px; width: 1700px; height: 2px; background: #3A2A1E29; z-index: curtain; delay: 300; in: {scaleX:0, duration:0.9, ease:'power2.inOut', pivot:'left'}; out: {opacity:0, duration:0.7, ease:'power1.in'})
chap#ch2.sticky {cn}01{/} 雨の日の数
hl#h2(a: "雨の日は年間"; b: "{r}112日{/}、"; c: "6〜7月に集中")
p#chip(left: 110px; top: 264px; font-size: 26px; color: $card; background: $rain_d; border-radius: 148px; padding: 9px 20px 9px 46px; white-space: nowrap; delay: 450; in: {x:-36, opacity:0, duration:0.6, ease:'power3.out'}) 雨の日
  icon#i(left: 16px; cy: 50%; font-size: 22px; name: drop; weight: fill; color: $card)
p#big(left: 110px; top: 368px; font-size: 214px; font-family: n; line-height: 0.9; color: $rain_d; white-space: nowrap; delay: 550; in: {y:34, opacity:0, duration:0.6, ease:'power2.out'}) [count:112 start=0 ms=1150]{u}日{/}
p#cmp(left: 110px; top: 594px; font-size: 30px; white-space: nowrap; delay: 1050; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) 晴れ・曇りの日 {n2}253{/} 日
div#yb(left: 110px; top: 686px; width: 520px; height: 34px; border-radius: 16px; background: #E3D2B8; delay: 1150; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'})
  div#fill(left: 0px; top: 0px; width: 159px; height: 34px; border-radius: 16px 0px 0px 16px; background: $rain; delay: 100; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
p#ybl(left: 110px; top: 738px; font-size: 22px; font-family: m; color: $ink2; white-space: nowrap; delay: 1270; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) 雨 112日
p#ybr(right: 1290px; top: 738px; font-size: 22px; font-family: m; color: $ink2; white-space: nowrap; delay: 1270; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) 1年 365日
p#note1(left: 110px; top: 786px; font-size: 21px; font-family: m; color: $ink2; white-space: nowrap; delay: 1390; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) ※ 雨の日＝日降水量 1mm 以上
p#note2(left: 135px; top: 820px; font-size: 21px; font-family: m; color: $ink2; white-space: nowrap; delay: 1510; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) 各店の最寄り観測点の値で判定
# 月別の縦棒の板 (棒の高さ = 日数 × 14.33 px・底は板の上から 360)
board#b2(left: 690px; top: 262px; width: 1120px; height: 650px; t: "図1　月別の雨の日数")
  div#band(left: 724px; top: 124px; width: 156px; height: 416px; border-radius: 14px; background: #3A61801A; in: {scaleY:0.9, opacity:0, duration:0.45, ease:'power2.out', pivot:'bottom'})
  div#base(left: 54px; top: 540px; width: 1004px; height: 2px; background: #3A2A1E59)
  div#bar(left: "51;106;161;215;270;325;379;434;489;543;598;653"; top: "231;260;288;303;274;217;202;217;116;174;245;188"; width: 56px; height: "129;100;72;57;86;143;158;143;244;186;115;172"; border-radius: 8px 8px 2px 2px; background: "#9FBDD2;#9FBDD2;#9FBDD2;#9FBDD2;#9FBDD2;#9FBDD2;#9FBDD2;#9FBDD2;#3A6180;#3A6180;#9FBDD2;#9FBDD2"; delay: 550; in: {scaleY:0, duration:0.55, ease:'back.out(1.4)', pivot:'bottom', stagger: {each: 0.07}}) ×12
  p#val(left: "42;97;152;206;261;316;370;425;480;534;589;644"; top: "200;229;257;272;243;186;171;186;85;143;214;157"; width: 84px; font-size: 34px; font-family: n; text-align: center; color: "$ink;$ink;$ink;$ink;$ink;$ink;$ink;$ink;$rain_d;$rain_d;$ink;$ink"; delay: 800; in: {y:12, opacity:0, duration:0.35, ease:'power2.out', stagger: {each: 0.07}}) ×12 9;7;5;4;6;10;11;10;17;13;8;12
  p#mo(left: "42;97;152;206;261;316;370;425;480;534;589;644"; top: 552px; width: 84px; font-size: 24px; font-family: m; text-align: center; color: $ink2) ×12 10月;11月;12月;1月;2月;3月;4月;5月;6月;7月;8月;9月
  div#yr(left: "47;211"; top: 592px; width: "156;484"; height: 33px; border-top: 2px solid #3A2A1E38; border-radius: 24px; delay: 1150; in: {y:34, opacity:0, duration:0.6, ease:'power3.out', stagger: {each: 0.1}}) ×2
    p#t(left: 0px; top: 8px; width: 100%; font-size: 20px; text-align: center; color: $ink2) 2025年;2026年
  # 6〜7 月のかぎ (上の線 + 両端の短い縦線・下から立つ)
  div#br(left: 730px; top: 96px; width: 144px; height: 18px; in: {scaleY:0, opacity:0, duration:0.4, ease:'power2.out', pivot:'bottom'})
    div#top(left: 0px; top: 0px; width: 144px; height: 3px; background: $rain_d)
    div#l(left: 0px; top: 0px; width: 3px; height: 18px; background: $rain_d)
    div#r(left: 141px; top: 0px; width: 3px; height: 18px; background: $rain_d)
  p#bt(left: 590px; top: 32px; font-size: 24px; color: $rain_d; white-space: nowrap; in: {y:14, opacity:0, duration:0.45, ease:'power2.out'}) 6〜7月の2か月で30日
  p#p27(left: 864px; top: 21px; font-size: 24px; color: $card; background: $rain_d; border-radius: 12px; padding: 4px 16px 6px 16px; white-space: nowrap; in: {scale:1.6, opacity:0, rotation:-6, duration:0.45, ease:'back.out(2.2)'}) 年間の{pn}27{/}%

# sc3 チェーン全体: 2 本の横棒 (614 → 577 万円・数えて出る) と「雨の日は −6%」の丸札 → 「ところが、立地で分けると…」と 3 つの立地の札 (矢印が上下に揺れる)
section#sc3(stagger: {each:0})
chap#ch3.sticky(overlap: ch2) {cn}02{/} チェーン全体
hl#h3(a: "チェーン全体では、"; b: "雨の日の売上"; c: "{r}−6%{/}")
board#b3(left: 110px; top: 262px; width: 1700px; height: 400px; t: "図2　1日の全店売上（24店合計）")
  div#r1(left: 40px; top: 94px; width: 270px; height: 45px; delay: 100; in: {x:-20, opacity:0, duration:0.6, ease:'power3.out'})
    icon#i(left: 0px; cy: 50%; font-size: 36px; name: sun; weight: fill; color: $mustard)
    p#t(left: 50px; cy: 50%; font-size: 30px; white-space: nowrap) 晴れ・曇りの日
  div#r2(left: 40px; top: 220px; width: 270px; height: 45px; delay: 250; in: {x:-20, opacity:0, duration:0.6, ease:'power3.out'})
    icon#i(left: 0px; cy: 50%; font-size: 36px; name: drop; weight: fill; color: $rain)
    p#t(left: 50px; cy: 50%; font-size: 30px; white-space: nowrap) 雨の日
  div#f1(left: 320px; top: 80px; width: 820px; height: 76px; border-radius: 6px 12px 12px 6px; background: $fair; delay: 300; in: {scaleX:0, duration:0.9, ease:'power3.out', pivot:'left'})
  div#f2(left: 320px; top: 206px; width: 771px; height: 76px; border-radius: 6px 12px 12px 6px; background: $rain; delay: 800; in: {scaleX:0, duration:0.9, ease:'power3.out', pivot:'left'})
  p#v1(left: 1162px; top: 86px; font-size: 30px; white-space: nowrap; delay: 900; in: {x:-16, opacity:0, duration:0.6, ease:'power3.out'}) {hv}[count:614 start=0 ms=900]{/}万円
  p#v2(left: 1112px; top: 212px; font-size: 30px; white-space: nowrap; delay: 1400; in: {x:-16, opacity:0, duration:0.6, ease:'power3.out'}) {hv}[count:577 start=0 ms=900]{/}万円
  p#note(left: 40px; bottom: 26px; font-size: 21px; font-family: m; color: $ink2; white-space: nowrap; delay: 1800; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) ※ 晴れ・曇りの日 253日／雨の日 112日の、1日あたりの全店売上
  div#badge(left: 1424px; top: 76px; width: 236px; height: 236px; border-radius: 148px; background: $rain_d; box-shadow: 0px 10px 24px #3A618040; in: {scale:1.6, opacity:0, rotation:-6, duration:0.45, ease:'back.out(2.2)'})
    p#l(cx: 50%; top: 56px; font-size: 24px; color: $card) 雨の日は
    p#v(cx: 50%; top: 96px; font-size: 96px; font-family: n; line-height: 1; color: $card; white-space: nowrap) −6{pc}%{/}
p#lead(left: 110px; top: 699px; font-size: 46px; font-family: h; white-space: nowrap; in: {x:-60, opacity:0, duration:0.6, ease:'power3.out'}) ところが、立地で分けると…
div#tz(left: "73;323;553"; top: 782px; width: "232;213;232"; height: 81px; background: $card; border: 2px solid #3A2A1E1F; border-radius: 16px; box-shadow: 0px 8px 18px #5A3C1E1A; in: {y:30, scale:0.92, opacity:0, duration:0.5, ease:'back.out(1.8)', stagger: {each: 0.18}}) ×3
  div#sq(left: 24px; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: "$terra;$mustard;$sage")
  icon#ar(left: "186;167;186"; cy: 50%; font-size: 26px; name: "arrow-up;arrow-down;arrow-down"; weight: bold; color: $card; background: "$terra_d;$rain_d;$rain_d")
  p#t(left: 56px; cy: 50%; font-size: 30px; white-space: nowrap) 駅直結・地下街;路面・商店街;公園沿い・郊外

# sc4 立地別: 右上に凡例・立地のカード 3 枚が語ごとに下から入り、絵が寄りから引き、2 本の棒が伸び、増減の数字が判子で着く (−31% は最後に沈む)
section#sc4(stagger: {each:0})
chap#ch4.sticky(overlap: ch3) {cn}03{/} 立地別
hl#h4(a: "立地で、"; b: "雨の日の"; c: "{t}向きが逆{/}になる")
leg#lg4a(left: 1504px; top: 136px; width: 188px; t: "晴れ・曇りの日"; c: $fair; delay: 600; in: {y:-12, opacity:0, duration:0.6, ease:'power3.out'})
leg#lg4b(left: 1718px; top: 136px; width: 93px; t: "雨の日"; c: $rain; delay: 600; in: {y:-12, opacity:0, duration:0.6, ease:'power3.out'})
loc#lc1(left: 110px; transform: rotate(0deg); nm: "駅直結・地下街"; cnt: "7店"; cd: $terra_d; va: "{vn}32.0{/}万円"; vb: "{vn}36.5{/}万円"; wa: 184px; wb: 210px; pct: "+14{pp}%{/}"; dir: "雨の日に増加"; ic: arrow-up; dc: $terra_d)
  group#ph(left: 0px; top: 0px; width: 540px; height: 668px; clip: 15,lc1.ph.win; in: {opacity:0, duration:0.35, ease:'power2.out'})
    div#win(left: 0px; top: 0px; width: 540px; height: 668px)
    group#in(left: 0px; top: 0px; width: 540px; height: 250px; clip: true)
      img#pic(inset: 0; in: none; main: keys(at=0 scale=1.18 | at=1 scale=1.02 ease=power1.out),duration=3200) 駅に直結した明るい地下街の小さなカフェのカウンター。通勤客でにぎわい、閉じて水滴の落ちる傘を持つ人が何人も並ぶ短い列、暖かい天井の灯り、タイルの床。屋内は乾いていて活気がある。横長の画面いっぱいに描き余白を作らない。温かく親しみやすいエディトリアルイラスト、リソグラフ印刷風 (平らな形・紙の粒子・少しずれたインク・手描きの縁)。色はテラコッタ・マスタード・コーヒーブラウン・セージグリーン、雨だけくすんだスレートブルー、生成りの紙の地。文字・数字・ロゴ・看板の文字は一切入れない
    div#stripe(left: 0px; top: 0px; width: 540px; height: 10px; background: $terra; border-radius: 24px)
loc#lc2(left: 690px; nm: "路面・商店街"; cnt: "11店"; cd: $mustard_d; va: "{vn}24.0{/}万円"; vb: "{vn}21.4{/}万円"; wa: 138px; wb: 123px; pct: "−11{pp}%{/}"; dir: "雨の日に減少"; ic: arrow-down; dc: $rain_d)
  group#ph(left: 0px; top: 0px; width: 540px; height: 668px; clip: 15,lc2.ph.win; in: {opacity:0, duration:0.35, ease:'power2.out'})
    div#win(left: 0px; top: 0px; width: 540px; height: 668px)
    group#in(left: 0px; top: 0px; width: 540px; height: 250px; clip: true)
      img#pic(inset: 0; in: none; main: keys(at=0 scale=1.18 | at=1 scale=1.02 ease=power1.out),duration=3200) 雨の日の開けた商店街の通りにある小さなカフェ。濡れた通りを傘をさした通行人が数人、暖かい窓越しに客が 2 人ほど見える落ち着いた店内、静かに降る雨。横長の画面いっぱいに描き余白を作らない。温かく親しみやすいエディトリアルイラスト、リソグラフ印刷風 (平らな形・紙の粒子・少しずれたインク・手描きの縁)。色はテラコッタ・マスタード・コーヒーブラウン・セージグリーン、雨だけくすんだスレートブルー、生成りの紙の地。文字・数字・ロゴ・看板の文字は一切入れない
    div#stripe(left: 0px; top: 0px; width: 540px; height: 10px; background: $mustard; border-radius: 24px)
loc#lc3(left: 1270px; nm: "公園沿い・郊外"; cnt: "6店"; cd: $sage_d; va: "{vn}21.0{/}万円"; vb: "{vn}14.5{/}万円"; wa: 122px; wb: 84px; pct: "−31{pp}%{/}"; dir: "雨の日に減少"; ic: arrow-down; dc: $rain_d)
  group#ph(left: 0px; top: 0px; width: 540px; height: 668px; clip: 15,lc3.ph.win; in: {opacity:0, duration:0.35, ease:'power2.out'})
    div#win(left: 0px; top: 0px; width: 540px; height: 668px)
    group#in(left: 0px; top: 0px; width: 540px; height: 250px; clip: true)
      img#pic(inset: 0; content: @park; in: none; main: keys(at=0 scale=1.18 | at=1 scale=1.02 ease=power1.out),duration=3200)
    div#stripe(left: 0px; top: 0px; width: 540px; height: 10px; background: $sage; border-radius: 24px)

# sc5 店別の分布: 増減率の 5 つの区分にカップの札を 1 店 1 枚で積む (区分ごとに弾んで落ちる)・0% の縦線・語で「上がる 8 店」「下がる 16 店」のかぎ → −20% 以下の 6 店を破線で囲み「6店すべて 公園沿い・郊外」
section#sc5(stagger: {each:0})
chap#ch5.sticky(overlap: ch4) {cn}04{/} 店別の分布
hl#h5(a: "雨で上がる店は{t}8店{/}、"; b: "下がる店は"; c: "{r}16店{/}")
board#b5(left: 110px; top: 250px; width: 1700px; height: 668px; t: "図3　雨の日の売上増減率（店別・24店）")
  shape#hl(left: 1132px; top: 62px; width: 136px; height: 400px; path: rect,r=0.13; background: #7E9B621F; border: 3px solid $sage_d; dash: 5,4; in: {scale:0.86, opacity:0, duration:0.5, ease:'back.out(1.8)'})
  div#base(left: 140px; top: 456px; width: 1180px; height: 2px; background: #3A2A1E59)
  div#zero(left: 614px; top: 70px; width: 2px; height: 386px; background: #3A2A1E73; delay: 150; in: {scaleY:0, duration:0.5, ease:'power2.out', pivot:'bottom'})
  p#zl(cx: 615px; top: 32px; font-size: 28px; font-family: n; delay: 150; in: {opacity:0, duration:0.5}) 0%
  div#q1(left: 226px; top: "267;231;195;159;123;87"; width: 48px; height: 48px; border-radius: 10px; background: #C9573A; delay: 350; in: {y:-50, opacity:0, duration:0.42, ease:'bounce.out', stagger: {each: 0.07}}) ×6
    icon#c(cx: 50%; cy: 50%; font-size: 28px; name: coffee; weight: fill; color: #FFFAF2D9)
  div#q2(left: 446px; top: "267;231"; width: 48px; height: 48px; border-radius: 10px; background: #E39A7E; delay: 700; in: {y:-50, opacity:0, duration:0.42, ease:'bounce.out', stagger: {each: 0.07}}) ×2
    icon#c(cx: 50%; cy: 50%; font-size: 28px; name: coffee; weight: fill; color: #FFFAF2D9)
  div#q3(left: 736px; top: "267;231;195"; width: 48px; height: 48px; border-radius: 10px; background: #A9C1D3; delay: 1050; in: {y:-50, opacity:0, duration:0.42, ease:'bounce.out', stagger: {each: 0.07}}) ×3
    icon#c(cx: 50%; cy: 50%; font-size: 28px; name: coffee; weight: fill; color: #FFFAF2D9)
  div#q4(left: 956px; top: "267;231;195;159;123;87;51"; width: 48px; height: 48px; border-radius: 10px; background: #6F93AE; delay: 1400; in: {y:-50, opacity:0, duration:0.42, ease:'bounce.out', stagger: {each: 0.07}}) ×7
    icon#c(cx: 50%; cy: 50%; font-size: 28px; name: coffee; weight: fill; color: #FFFAF2D9)
  div#q5(left: 1176px; top: "267;231;195;159;123;87"; width: 48px; height: 48px; border-radius: 10px; background: #3A6180; delay: 1750; in: {y:-50, opacity:0, duration:0.42, ease:'bounce.out', stagger: {each: 0.07}}) ×6
    icon#c(cx: 50%; cy: 50%; font-size: 28px; name: coffee; weight: fill; color: #FFFAF2D9)
  p#cnt(cx: "167;313;507;653;800"; top: "52;196;160;16;52"; font-size: 26px; white-space: nowrap; color: "$terra_d;$terra_d;$rain_d;$rain_d;$rain_d"; delay: "920;990;1410;2040;2320"; in: {y:10, opacity:0, duration:0.6, ease:'power3.out'}) ×5 {bn}6{/}店;{bn}2{/}店;{bn}3{/}店;{bn}7{/}店;{bn}6{/}店
  p#lab(cx: "167;313;507;653;800"; top: 468px; font-size: 26px; white-space: nowrap; delay: 100; in: {y:14, opacity:0, duration:0.6, ease:'power3.out', stagger: {each: 0.06}}) ×5 +10%以上;0〜+10%;0〜−10%;−10〜−20%;−20%以下
  div#gup(left: 180px; top: 516px; width: 360px; height: 20px; in: {scaleY:0, opacity:0, duration:0.35, pivot:'top'})
    div#l(left: 0px; top: 0px; width: 3px; height: 20px; background: $terra_d)
    div#r(left: 357px; top: 0px; width: 3px; height: 20px; background: $terra_d)
    div#b(left: 0px; top: 16px; width: 360px; height: 3px; border-radius: 2px; background: $terra_d)
  p#gut(cx: 360px; top: 544px; font-size: 40px; font-family: h; color: $terra_d; white-space: nowrap; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}) 上がる {gn}8{/}店
  p#gus(cx: 360px; top: 604px; font-size: 22px; font-family: m; color: $ink2; white-space: nowrap; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}) 駅直結・地下街 7店 ＋ 路面 1店
  div#gdn(left: 690px; top: 516px; width: 580px; height: 20px; in: {scaleY:0, opacity:0, duration:0.35, pivot:'top'})
    div#l(left: 0px; top: 0px; width: 3px; height: 20px; background: $rain_d)
    div#r(left: 578px; top: 0px; width: 3px; height: 20px; background: $rain_d)
    div#b(left: 0px; top: 16px; width: 580px; height: 3px; border-radius: 2px; background: $rain_d)
  p#gdt(cx: 980px; top: 544px; font-size: 40px; font-family: h; color: $rain_d; white-space: nowrap; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}) 下がる {gn}16{/}店
  div#call(left: 1296px; top: 160px; width: 360px; height: 129px; border-radius: 18px; background: #EEF2E6; border: 2px solid $sage; in: {x:40, opacity:0, duration:0.55, ease:'back.out(1.6)'})
    img#pic(left: 20px; cy: 50%; width: 96px; height: 96px; border-radius: 148px; content: @park; main: none)
    p#a(left: 134px; top: 27px; font-size: 34px; font-family: h; color: $sage_d; white-space: nowrap) 6店すべて
    p#b(left: 134px; top: 72px; font-size: 26px; white-space: nowrap) 公園沿い・郊外

# sc5 → sc6 は同じ押し出し。sc6 売上の構成: 2 本の積み上げの帯 (立地の 3 色・左から順に伸びる)・「最大」の札・37% → 44% の破線・語で「雨の日の最大」の判子と帯の弾み
section#sc6(stagger: {each:0})
chap#ch6.sticky(overlap: ch5) {cn}05{/} 売上の構成
hl#h6(a: "雨の日は、"; b: "{t}駅直結・地下街{/}が"; c: "最大の稼ぎ頭")
board#b6(left: 110px; top: 250px; width: 1700px; height: 620px; t: "図4　全店売上に占める立地別の割合")
  div#r1(left: 40px; top: 162px; width: 270px; height: 45px; delay: 50; in: {x:-20, opacity:0, duration:0.6, ease:'power3.out'})
    icon#i(left: 0px; cy: 50%; font-size: 36px; name: sun; weight: fill; color: $mustard)
    p#t(left: 50px; cy: 50%; font-size: 30px; white-space: nowrap) 晴れ・曇りの日
  div#r2(left: 40px; top: 423px; width: 270px; height: 45px; delay: 250; in: {x:-20, opacity:0, duration:0.6, ease:'power3.out'})
    icon#i(left: 0px; cy: 50%; font-size: 36px; name: drop; weight: fill; color: $rain)
    p#t(left: 50px; cy: 50%; font-size: 30px; white-space: nowrap) 雨の日
  div#s1(left: 310px; top: 120px; width: 1300px; height: 130px)
    div#g1(left: 0px; top: 0px; width: 482px; height: 130px; border-radius: 14px 0px 0px 14px; background: $terra; delay: 150; in: {scaleX:0, opacity:0, duration:0.5, ease:'power3.out', pivot:'left'})
      p#v(left: 24px; cy: 50%; font-size: 60px; font-family: n; color: #FFFAF2; white-space: nowrap) 37{sp}%{/}
    div#g2(left: 484px; top: 0px; width: 556px; height: 130px; background: $mustard; border-radius: 24px; delay: 310; in: {scaleX:0, opacity:0, duration:0.5, ease:'power3.out', pivot:'left'})
      p#v(left: 24px; cy: 50%; font-size: 60px; font-family: n; white-space: nowrap) 43{sp}%{/}
    div#g3(left: 1044px; top: 0px; width: 256px; height: 130px; border-radius: 0px 14px 14px 0px; background: $sage; delay: 470; in: {scaleX:0, opacity:0, duration:0.5, ease:'power3.out', pivot:'left'})
      p#v(left: 24px; cy: 50%; font-size: 60px; font-family: n; white-space: nowrap) 20{sp}%{/}
  div#s2(left: 310px; top: 380px; width: 1300px; height: 130px)
    div#g1(left: 0px; top: 0px; width: 572px; height: 130px; border-radius: 14px 0px 0px 14px; background: $terra; in: {scaleX:0, opacity:0, duration:0.5, ease:'power3.out', pivot:'left'})
      p#v(left: 24px; cy: 50%; font-size: 60px; font-family: n; color: #FFFAF2; white-space: nowrap) 44{sp}%{/}
    div#g2(left: 574px; top: 0px; width: 531px; height: 130px; background: $mustard; border-radius: 24px; in: {scaleX:0, opacity:0, duration:0.5, ease:'power3.out', pivot:'left'})
      p#v(left: 24px; cy: 50%; font-size: 60px; font-family: n; white-space: nowrap) 41{sp}%{/}
    div#g3(left: 1108px; top: 0px; width: 192px; height: 130px; border-radius: 0px 14px 14px 0px; background: $sage; in: {scaleX:0, opacity:0, duration:0.5, ease:'power3.out', pivot:'left'})
      p#v(left: 24px; cy: 50%; font-size: 60px; font-family: n; white-space: nowrap) 15{sp}%{/}
  p#tag1(left: 1032px; cy: 94px; font-size: 24px; color: $card; background: $ink; border-radius: 148px; padding: 6px 16px 8px 16px; delay: 850; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'}) 最大
  shape#shift(left: 549px; top: 252px; width: 4px; height: 120px; path: line_v; border: 4px solid $terra_d; dash: 4,4; in: {scaleY:0, opacity:0, duration:0.45, ease:'power2.out', pivot:'top'})
  p#shl(left: 570px; cy: 315px; font-size: 28px; color: $terra_d; background: $card; border-radius: 10px; padding: 2px 12px 2px 12px; white-space: nowrap; in: {x:-12, opacity:0, duration:0.6, ease:'power3.out'}) {sn}37{/}% → {sn}44{/}%
  p#tag2(left: 486px; cy: 580px; font-size: 28px; color: $card; background: $terra_d; border-radius: 148px; padding: 8px 20px 9px 54px; white-space: nowrap; in: {scale:1.6, opacity:0, rotation:-6, duration:0.45, ease:'back.out(2.2)'}) 雨の日の最大
    icon#i(left: 18px; cy: 50%; font-size: 26px; name: crown; weight: fill; color: #F4C66B)
  leg#lg1(left: 1076px; top: 32px; width: 192px; t: "駅直結・地下街"; c: $terra; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'})
  leg#lg2(left: 1286px; top: 32px; width: 170px; t: "路面・商店街"; c: $mustard; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'})
  leg#lg3(left: 1474px; top: 32px; width: 186px; t: "公園沿い・郊外"; c: $sage; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'})

# sc7 冷たい飲み物: 左に温かい / 冷たい飲み物の絵と凡例と定義・右の板に気温帯の縦棒 7 本 (50% を超える帯だけ橙)・語で 50% の破線 → 22℃ の実線 → 雨の日の 24℃ の破線が右へ滑る
section#sc7(stagger: {each:0})
chap#ch7.sticky(overlap: ch6) {cn}06{/} 冷たい飲み物
hl#h7(a: "冷たい飲み物は、"; b: "最高気温{t}22℃{/}で"; c: "逆転")
img#drinks(left: 110px; top: 262px; width: 460px; height: 306px; border-radius: 18px; box-shadow: 0px 14px 30px #5A3C1E24; main: none; delay: 350; in: {y:30, scale:0.96, opacity:0, duration:0.6, ease:'power3.out'}) 生成りの無地の背景の中央に並ぶカフェの飲み物 2 つ。左に湯気の立つ陶器のマグのホットラテ (小さなハートのラテアート)、右に氷とストローと水滴の付いた背の高いグラスのアイスコーヒー。横長の画面の中央に 2 つを大きめに置き、周りは生成りの地のまま。温かく親しみやすいエディトリアルイラスト、リソグラフ印刷風 (平らな形・紙の粒子・少しずれたインク・手描きの縁)。色はテラコッタ・マスタード・コーヒーブラウン・セージグリーン、生成りの紙の地。文字・数字・ロゴは一切入れない
leg#dl1(left: 110px; top: 590px; width: 460px; t: "温かい飲み物のほうが多い"; c: $hot; delay: 700; in: {x:-16, opacity:0, duration:0.6, ease:'power3.out'})
  p#t(font-size: 26px; font-family: k; color: $ink)
leg#dl2(left: 110px; top: 644px; width: 460px; t: "冷たい飲み物のほうが多い"; c: $cold; delay: 820; in: {x:-16, opacity:0, duration:0.6, ease:'power3.out'})
  p#t(font-size: 26px; font-family: k; color: $ink)
p#dn1(left: 110px; top: 693px; font-size: 21px; font-family: m; color: $ink2; white-space: nowrap; delay: 950; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) ※ 冷たい飲み物の比率
p#dn2(left: 110px; top: 746px; font-size: 21px; font-family: m; color: $ink2; white-space: nowrap; delay: 1050; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) ＝ドリンク杯数に占めるアイス系の割合
board#b7(left: 610px; top: 262px; width: 1200px; height: 654px; t: "図5　最高気温帯別・冷たい飲み物の比率")
  div#base(left: 81px; top: 520px; width: 1062px; height: 2px; background: #3A2A1E59)
  div#bar(left: "75;175;275;375;475;575;675"; top: "316;299;263;230;200;167;147"; width: 104px; height: "31;48;84;117;147;180;200"; border-radius: 8px 8px 2px 2px; background: "$hot;$hot;$hot;$hot;$cold;$cold;$cold"; delay: 250; in: {scaleY:0, duration:0.55, ease:'back.out(1.3)', pivot:'bottom', stagger: {each: 0.13}}) ×7
  p#val(left: "60;160;260;360;460;560;660"; top: "285;268;232;199;169;136;116"; width: 150px; font-size: 34px; font-family: n; text-align: center; white-space: nowrap; delay: 550; in: {y:10, opacity:0, duration:0.35, stagger: {each: 0.13}}) ×7 12{ip}%{/};19{ip}%{/};33{ip}%{/};46{ip}%{/};58{ip}%{/};71{ip}%{/};79{ip}%{/}
  p#band(left: "60;160;260;360;460;560;660"; top: 532px; width: 150px; font-size: 22px; text-align: center; color: $ink2; white-space: nowrap; delay: 50; in: {y:10, opacity:0, duration:0.6, ease:'power3.out', stagger: {each: 0.05}}) ×7 10℃未満;10〜15℃;15〜20℃;20〜23℃;23〜26℃;26〜30℃;30℃以上
  shape#l50(left: 81px; top: 328px; width: 1062px; height: 3px; path: line_h; border: 3px solid #3A2A1E99; dash: 5,5; in: {scaleX:0, duration:0.7, ease:'power2.inOut', pivot:'left'})
  p#l50t(left: 22px; top: 310px; font-size: 28px; font-family: n; in: {x:-10, opacity:0, duration:0.6, ease:'power3.out'}) 50%
  div#m22(left: 638px; top: 96px; width: 4px; height: 424px; background: $terra_d; in: {scaleY:0, duration:0.45, ease:'power3.out', pivot:'bottom'})
  shape#m24(left: 638px; top: 96px; width: 4px; height: 424px; path: line_v; border: 4px solid $rain_d; dash: 5,4; in: {scaleY:0, opacity:0, duration:0.3, ease:'power2.out', pivot:'bottom'})
  p#t22(right: 570px; top: 44px; font-size: 52px; font-family: n; line-height: 1.1; color: $terra_d; text-align: right; white-space: nowrap; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) 22{mu}℃{/}
  p#s22(right: 570px; top: 104px; font-size: 21px; color: $terra_d; text-align: right; white-space: nowrap; in: {y:14, opacity:0, duration:0.6, ease:'power3.out'}) 晴れ・曇りの日の逆転点
  p#t24(left: 756px; top: 44px; font-size: 52px; font-family: n; line-height: 1.1; color: $rain_d; white-space: nowrap; in: {x:-16, opacity:0, duration:0.6, ease:'power3.out'}) 24{mu}℃{/}
  p#s24(left: 756px; top: 104px; font-size: 21px; color: $rain_d; white-space: nowrap; in: {x:-16, opacity:0, duration:0.6, ease:'power3.out'}) 雨の日の逆転点
  p#note(left: 40px; bottom: 22px; font-size: 21px; color: $rain_d; white-space: nowrap; in: {y:10, opacity:0, duration:0.6, ease:'power3.out'}) ※ 雨の日は同じ気温でも冷たい飲み物が出にくく、境目が24℃に上がる
# 紙が右から横切る切替 (sc7 の終わりに右から覆い、sc8 の頭で左へ抜ける・前後に柔らかい影)
img#sheet1.sticky(inset: 0; content: @paper; main: none; look: #CDB996/#F6EBD8; box-shadow: 0px 0px 50px #50321447; z-index: front; in: {x:1990, duration:0.5, ease:'power2.in'}; out: {x:-1990, duration:0.6, ease:'power2.out'})

# sc8 予報で仕込み: 試行のルールの板 (仕込みの絵・ルールの 2 行・3 店の札・56 日のマス) → 廃棄率の前後の点の比較 4 行 (点が左へ動き帯が伸びる) → 廃棄額の札 (−46 万円の判子) → 品切れの札 (9 個の点が 2 個を残して薄れる)
section#sc8(stagger: {each:0})
chap#ch8.sticky(overlap: ch7) {cn}07{/} 予報で仕込み
hl#h8(a: "前日の予報で仕込みを変えると、"; b: "廃棄率"; c: "{t}7.8%→4.6%{/}"; d1: 300; d2: 390; d3: 480)
board#rule(left: 110px; top: 248px; width: 1700px; height: 258px; t: "試行　2026年6〜7月の8週間（56日）・3店"; in: {y:50, opacity:0, rotation:-1, duration:0.7, ease:'power3.out'})
  img#prep(left: 22px; top: 22px; width: 320px; height: 214px; border-radius: 14px; main: none; delay: 150; in: {scale:1.1, opacity:0, duration:0.8, ease:'power2.out'}) 夕方のカフェの奥の仕込み台。店員の手が翌日のサンドイッチと焼き菓子のトレイを並べ、台の上に立てたタブレットの画面には雨粒の付いた雲の簡単な絵だけ、罫線だけのクリップボード、暖かい灯り。横長の画面いっぱいに描き余白を作らない。温かく親しみやすいエディトリアルイラスト、リソグラフ印刷風 (平らな形・紙の粒子・少しずれたインク・手描きの縁)。色はテラコッタ・マスタード・コーヒーブラウン・セージグリーン、雨だけくすんだスレートブルー、生成りの紙の地。文字・数字・ロゴは一切入れない
  p#k(left: 372px; top: 34px; font-size: 22px; color: $card; background: $terra_d; border-radius: 8px; padding: 4px 14px 4px 14px; delay: 300; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) ルール
  p#chip(left: "249;404;547"; top: 178px; font-size: 22px; color: "$terra_d;$mustard_d;$sage_d"; background: #F3EAD9; border: "2px solid $terra_d;2px solid $mustard_d;2px solid $sage_d"; border-radius: 12px; padding: 8px 16px 8px 16px; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.4, ease:'back.out(2)', stagger: {each: 0.25}}) ×3 駅直結 1店 {pb}+15%{/};路面 1店 {pb}−10%{/};公園沿い 1店 {pb}−25%{/}
  p#days(left: 1206px; top: 28px; font-size: 24px; line-height: 1.35; white-space: nowrap; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'}) 対象日 {dd}21{/}日 ／ 56日
  p#dsub(left: 1206px; top: 80px; font-size: 20px; font-family: m; color: $ink2; white-space: nowrap; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'}) 実際に雨 17日・予報の外れ 4日
  div#cell(left: "804;825;847;868;889;911;932;953;975;996;1017;1039;1060;1081;804;825;847;868;889;911;932;953;975;996;1017;1039;1060;1081;804;825;847;868;889;911;932;953;975;996;1017;1039;1060;1081;804;825;847;868;889;911;932;953;975;996;1017;1039;1060;1081"; top: "80;80;80;80;80;80;80;80;80;80;80;80;80;80;100;100;100;100;100;100;100;100;100;100;100;100;100;100;120;120;120;120;120;120;120;120;120;120;120;120;120;120;140;140;140;140;140;140;140;140;140;140;140;140;140;140"; width: 26px; height: 26px; border-radius: 6px; background: "#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#4E7896;#FBF6EC;#FBF6EC;#FBF6EC;#FBF6EC;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4;#E7DAC4"; in: {scale:0, opacity:0, duration:0.25, ease:'back.out(2)', stagger: {each: 0.022}}) ×56
  # 予報の外れの 4 日 (白抜きの縁)
  div#miss(left: "868;889;911;932"; top: 150px; width: 26px; height: 26px; border-radius: 6px; border: 3px solid $rain; in: {scale:0, opacity:0, duration:0.25, ease:'back.out(2)', stagger: {each: 0.022}}) ×4
  p#t(left: 372px; top: 74px; font-size: 36px; font-family: h; line-height: 1.32; white-space: nowrap; delay: 420; in: {y:34, opacity:0, duration:0.6, ease:'power3.out'}) 前日17時の予報で、翌日の[br]{r}降水確率が60%以上{/}なら、仕込みを変える
board#res(left: 110px; top: 540px; width: 1060px; height: 376px; t: "廃棄率（仕込み額に対する廃棄額）"; in: {y:50, opacity:0, duration:0.6, ease:'power3.out'})
  div#avgbg(left: 30px; top: 272px; width: 1000px; height: 56px; border-radius: 14px; background: #EFB79F47)
  dbrow#r1(top: 78px; l: "駅直結"; va: "{dv}6.2{/}% →"; vb: "4.9"; ax: 561px; bx: 560px; sl: 494px; sw: 81px)
  dbrow#r2(top: 140px; l: "路面"; va: "{dv}7.5{/}% →"; vb: "4.4"; ax: 642px; bx: 640px; sl: 464px; sw: 192px)
  dbrow#r3(top: 202px; l: "公園沿い"; va: "{dv}9.7{/}% →"; vb: "4.5"; ax: 778px; bx: 777px; sl: 470px; sw: 322px)
  dbrow#r4(top: 272px; l: "{av}3店平均{/}"; va: "{dv}7.8{/}% →"; vb: "4.6"; ax: 660px; bx: 658px; sl: 476px; sw: 198px)
  p#x(cx: "147;229;312;395;477;560"; top: 336px; font-size: 20px; font-family: n; color: $ink2; in: {y:8, opacity:0, duration:0.6, ease:'power3.out', stagger: {each: 0.04}}) ×6 0%;2%;4%;6%;8%;10%
  div#lg(right: 30px; top: 22px; width: 240px; height: 30px)
    div#a(left: 0px; cy: 50%; width: 22px; height: 22px; border-radius: 148px; background: $card; border: 4px solid $hot)
    p#at(left: 30px; cy: 50%; font-size: 21px; color: $ink2; white-space: nowrap) 前年同期
    div#b(left: 130px; cy: 50%; width: 22px; height: 22px; border-radius: 148px; background: $terra)
    p#bt(left: 160px; cy: 50%; font-size: 21px; color: $ink2; white-space: nowrap) 試行期間
div#cost(left: 1204px; top: 540px; width: 606px; height: 178px; background: $card; border-radius: 22px; border: 2px solid #785A3C24; box-shadow: 0px 18px 40px #5A3C1E1F; in: {x:40, opacity:0, duration:0.6, ease:'power3.out'})
  p#l(left: 28px; top: 22px; font-size: 22px; color: $ink2; white-space: nowrap) 廃棄額（3店合計・8週間）
  p#v(left: 28px; top: 62px; font-size: 28px; white-space: nowrap) {tn}112{/}万円 → {ta}66{/}万円
  p#tb(right: 26px; top: 70px; font-size: 26px; color: $card; background: $terra_d; border-radius: 14px; padding: 8px 16px 10px 16px; white-space: nowrap; in: {scale:1.6, opacity:0, rotation:-6, duration:0.45, ease:'back.out(2.2)'}) {tb}−46{/}万円
div#stock(left: 1204px; top: 738px; width: 606px; height: 178px; background: $card; border-radius: 22px; border: 2px solid #785A3C24; box-shadow: 0px 18px 40px #5A3C1E1F; in: {x:40, opacity:0, duration:0.6, ease:'power3.out'})
  p#l(left: 28px; top: 22px; font-size: 22px; color: $ink2; white-space: nowrap) 駅直結・雨の日夕方の品切れ
  p#v(left: 28px; top: 62px; font-size: 28px; white-space: nowrap) {tn}9{/}回 → {ta}2{/}回
  div#sd(left: "267;287;307;327;347;267;287;307;327"; top: "56;56;56;56;56;76;76;76;76"; width: 18px; height: 18px; border-radius: 148px; background: $rain; in: {scale:0, opacity:0, duration:0.25, ease:'back.out(2)', stagger: {each: 0.05}}) ×9
img#sheet2.sticky(inset: 0; content: @paper; main: none; look: #CDB996/#F6EBD8; box-shadow: 0px 0px 50px #50321447; z-index: front; in: {x:1990, duration:0.5, ease:'power2.in'}; out: {x:-1990, duration:0.6, ease:'power2.out'})

# sc9 まとめ: 3 枚の札が文の頭で下から入り、右上の丸に ✓ が描かれる・最後に社名と題の署名・終わりの 0.85 秒で全部が消えて紙だけが残る
section#sc9(stagger: {each:0})
chap#ch9.sticky(overlap: ch8; out: {opacity:0, duration:0.7, ease:'power1.in'}) {cn}08{/} まとめ
hl#h9(a: "まとめ："; b: "雨の日の打ち手は、"; c: "{t}店ごとに{/}変える"; d1: 300; d2: 390; d3: 480; out: {opacity:0, duration:0.7, ease:'power1.in'})
card#cc1(left: 110px; no: "1"; t1: "雨の日の手は、"; t2: "店ごとに逆向き"; fig: "{ft}+14{/}{ftp}%{/}{sl} ／ {/}{fr}−31{/}{frp}%{/}"; sub: "駅直結・地下街 ／ 公園沿い・郊外"; n1: "全体の −6% で判断せず、"; n2: "立地ごとに逆向きの手を打つ"; out: {opacity:0, duration:0.7, ease:'power1.in'})
card#cc2(left: 690px; no: "2"; t1: "冷たい飲み物は"; t2: "最高気温で逆転"; fig: "{ft}22{/}{ftp}℃{/}{sl} ／ {/}{lb}雨の日{/}{fr}24{/}{frp}℃{/}"; sub: "この気温を超えると冷たい飲み物が半数超"; n1: "この気温を、メニューの"; n2: "入れ替えと仕込みの目安に"; out: {opacity:0, duration:0.7, ease:'power1.in'})
card#cc3(left: 1270px; no: "3"; t1: "前日の予報で"; t2: "仕込みを変える"; fig: "7.8{fp}%{/}{sl} → {/}{ft}4.6{/}{ftp}%{/}"; sub: "廃棄率・3店の試行（前年同期比）"; n1: "雨の多い6〜7月を前に、"; n2: "全店へ広げたい"; out: {opacity:0, duration:0.7, ease:'power1.in'})
p#signoff(cx: 960px; top: 922px; font-size: 30px; letter-spacing: 0.12em; color: $ink2; white-space: nowrap; in: {y:16, opacity:0, duration:0.6, ease:'power3.out'}; out: {opacity:0, duration:0.6, ease:'power1.in'}) こもれび珈琲　店長会議　｜　雨の日、売れる店と売れない店
```

```timeline.txt
#v2
cast n = "明るく高めの声の30〜40代の女性のナレーター、滑らかで明瞭な発音、快活で親しみやすく信頼感のある語り" speed=110%
silence head=0 tail=0
# 場面は横に押し出して替える (新しい場面が右から入り、境目の後 0.72 秒で前の場面を左へ押し出す)・上端の帯と章札は z curtain で残る
transition = push,720,dir=left,overlap=720,ease=power3.inOut
# 場面の頭は 0.5 秒の無音 (見出しが上がる間)、台詞の後は 0.12 秒で次の場面へ

*** sc1
[>#subtitle]
bgm music +600
se rain -1.9dB to=8.6s fade=600,1600
@n: [silence:1.0s][♪paper -1.9dB -850][♪fuwan -5.8dB -450]雨の日、[!#t2{up} marker +50][♪pen -5.8dB +50]売れる店と、[!#t3{dn} marker +50][♪pen -5.8dB +50]売れない店。こもれび珈琲24店の、1年分の[>#sub -600]データで見ていきます。[silence:0.12s]

*** sc2
@n: [silence:0.5s][!#tb_dot[1] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][♪paper -3.5dB -380][♪m_up -6.4dB +500]雨の日は、1年で[♪stamp -2.9dB -330]112日。[>#b2.band -50][>#b2.br][>#b2.bt +200][♪pen -6.4dB]6月と7月の2か月に、その[>#b2.p27][♪pop -4.3dB]27%が集まります。[silence:0.12s]

*** sc3
@n: [silence:0.5s][<#ch2 -500][!#tb_dot[1] to,{x:-20, w:10, fill:'#A8432A73', duration:0.4, ease:'power2.out'} -250][!#tb_dot[2] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][♪paper -3.5dB -380][♪m2 -6.9dB +250][♪m4 -6.9dB +750]チェーン全体では、雨の日の売上は[>#b3.badge][♪stamp -2.2dB]6%減。[>#lead +100][>#tz +550][♪piron -5.3dB +100]ところが立地で分けると、向きが[!#tz[1].ar to,{y:-6, duration:0.4, ease:'sine.inOut', repeat:5, yoyo:true}][!#tz[2].ar to,{y:6, duration:0.4, ease:'sine.inOut', repeat:5, yoyo:true} +180][!#tz[3].ar to,{y:6, duration:0.4, ease:'sine.inOut', repeat:5, yoyo:true} +360]逆になります。[silence:0.12s]

*** sc4
@n: [silence:0.5s][<#ch3 -500][!#tb_dot[2] to,{x:-20, w:10, fill:'#A8432A73', duration:0.4, ease:'power2.out'} -250][!#tb_dot[3] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][♪paper -3.5dB -380][>#lc1 -150][>#lc1.ph -150][♪fuwan -6.4dB -150]駅直結・地下街の店は[>#lc1.badge][♪stamp -2.9dB]14%増。[>#lc2 -200][>#lc2.ph -200][♪fuwan -6.4dB -200]路面・商店街は[>#lc2.badge][♪stamp -2.9dB]11%減、[|][>#lc3 -200][>#lc3.ph -200][♪fuwan -6.4dB -200]公園沿い・郊外は[>#lc3.badge][♪stamp -2.2dB][♪m_down -9.1dB +80][!#lc3.badge to,{y:8, duration:0.5, ease:'sine.inOut', repeat:1, yoyo:true} +600]31%減です。[silence:0.12s]

*** sc5
@n: [silence:0.5s][<#ch4 -500][!#tb_dot[3] to,{x:-20, w:10, fill:'#A8432A73', duration:0.4, ease:'power2.out'} -250][!#tb_dot[4] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][♪paper -3.5dB -380][♪m1 -7.6dB +300][♪m2 -7.6dB +650][♪m3 -7.6dB +1000][♪m4 -7.6dB +1350][♪m5 -7.6dB +1700]雨で売上が上がる店は[>#b5.gup][>#b5.gut +100][>#b5.gus +100][♪pen -6.4dB][!#b5.q1[*] to,{scale:1.1, duration:0.22, ease:'power2.out', repeat:1, yoyo:true} +100][!#b5.q2[*] to,{scale:1.1, duration:0.22, ease:'power2.out', repeat:1, yoyo:true} +100]8店、下がる店は[>#b5.gdn][>#b5.gdt +100][♪pen -6.4dB]16店。20%以上落ちた6店は、すべて[>#b5.hl][>#b5.call +350][♪pen_circle -5.3dB]公園沿い・郊外です。[silence:0.12s]

*** sc6
@n: [silence:0.5s][<#ch5 -500][!#tb_dot[4] to,{x:-20, w:10, fill:'#A8432A73', duration:0.4, ease:'power2.out'} -250][!#tb_dot[5] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][♪paper -3.5dB -380][♪swoosh -6.4dB +100]売上の構成も入れ替わり、[>#b6.s2.g1 -100][>#b6.s2.g2 +60][>#b6.s2.g3 +220][♪swoosh -6.4dB -100][>#b6.lg1 +400][>#b6.lg2 +400][>#b6.lg3 +400][>#b6.shift +700][>#b6.shl +900]雨の日は、[|]駅直結・地下街がシェアで[>#b6.tag2][♪stamp -2.2dB][♪piron -6.4dB +50][!#b6.s2.g1 to,{scale:1.04, duration:0.22, ease:'power2.out', repeat:1, yoyo:true} +50]トップに立ちます。[silence:0.12s]

*** sc7
@n: [silence:0.5s][<#ch6 -500][!#tb_dot[5] to,{x:-20, w:10, fill:'#A8432A73', duration:0.4, ease:'power2.out'} -250][!#tb_dot[6] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][♪paper -3.5dB -380][♪m_up -6.4dB +200]冷たい飲み物は、最高気温[>#b7.l50 -450][>#b7.l50t -250][♪pen -6.4dB -450][>#b7.m22][>#b7.t22 +150][>#b7.s22 +150][♪pop -4.3dB]22度で温かい飲み物を逆転。雨の日は、この境目が[>#b7.m24 -550][!#b7.m24 to,{x:100, duration:0.6, ease:'power3.inOut'} -250][♪whoosh -4.8dB -250][>#b7.t24 +250][>#b7.s24 +250][♪pop -5.3dB +300][>#b7.note +500]24度に[>#sheet1 +255][♪pageflip -1.9dB +705]上がります。[silence:0.12s]
# 紙が横切る間に場面を替える (切替そのものは無し)
transition cut

*** sc8
@n: [silence:0.5s][<#sheet1 -380][<#ch7 -500][!#tb_dot[6] to,{x:-20, w:10, fill:'#A8432A73', duration:0.4, ease:'power2.out'} -250][!#tb_dot[7] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][♪paper -4.8dB -50]前日の天気予報で仕込みを変えた[>#rule.chip -100][♪pop -6.4dB -100][♪pop -6.4dB +150][♪pop -6.4dB +400][>#rule.days +200][>#rule.dsub +200][>#rule.cell +500][>#rule.miss +870][♪m_up -8.3dB +500]3店では、[|][>#res -150][♪swoosh -6.4dB -150][>#res.r1 +100][>#res.r2 +220][>#res.r3 +340][>#res.r4 +460][>#res.x +350]廃棄率が平均[>#res.r1.sg +350][!#res.r1.db to,{x:-81, duration:0.9, ease:'power3.inOut'} +350][>#res.r1.vb +1000][>#res.r2.sg +470][!#res.r2.db to,{x:-192, duration:0.9, ease:'power3.inOut'} +470][>#res.r2.vb +1120][>#res.r3.sg +590][!#res.r3.db to,{x:-322, duration:0.9, ease:'power3.inOut'} +590][>#res.r3.vb +1240][>#res.r4.sg +710][!#res.r4.db to,{x:-198, duration:0.9, ease:'power3.inOut'} +710][>#res.r4.vb +1360]7.8%から[!#res.r4 to,{scale:1.04, duration:0.22, ease:'power2.out', repeat:1, yoyo:true}][!#res.avgbg to,{scale:1.04, duration:0.22, ease:'power2.out', repeat:1, yoyo:true}][♪stamp -2.2dB][>#cost +900][♪pop -5.8dB +900][>#cost.tb +1350]4.6%に。駅直結の店では、雨の日夕方の[>#stock -200][♪fuwan -6.4dB -200][>#stock.sd +150]品切れも、[|]9回から[!#stock.sd[3] to,{opacity:0.18, scale:0.7, duration:0.4}][!#stock.sd[4] to,{opacity:0.18, scale:0.7, duration:0.4} +40][!#stock.sd[5] to,{opacity:0.18, scale:0.7, duration:0.4} +80][!#stock.sd[6] to,{opacity:0.18, scale:0.7, duration:0.4} +120][!#stock.sd[7] to,{opacity:0.18, scale:0.7, duration:0.4} +160][!#stock.sd[8] to,{opacity:0.18, scale:0.7, duration:0.4} +200][!#stock.sd[9] to,{opacity:0.18, scale:0.7, duration:0.4} +240][♪stamp -2.9dB]2回に[>#sheet2 +110][♪pageflip -1.9dB +560]減りました。[silence:0.12s]
transition cut

*** sc9
@n: [silence:0.5s][<#sheet2 -380][<#ch8 -500][!#tb_dot[7] to,{x:-20, w:10, fill:'#A8432A73', duration:0.4, ease:'power2.out'} -250][!#tb_dot[8] to,{x:-20, w:30, fill:'#A8432A', duration:0.4, ease:'power2.out'} -250][>#cc1 -450][>#cc1.ring -50][>#cc1.ck +20][♪check -2.9dB -100]雨の日の手は、店ごとに逆向き。[>#cc2 -450][>#cc2.ring -50][>#cc2.ck +20][♪check -2.9dB -100]メニューの切り替えは、最高気温22度、[|]雨の日は24度が目安。[>#cc3 -450][>#cc3.ring -50][>#cc3.ck +20][♪check -2.9dB -100]そして雨の多い6月、7月を前に、[|]予報で仕込みを変える運用を、全店へ広げましょう。
[<#subtitle]
@: [silence:0.2s][>#signoff][♪chime -2.9dB][silence:2.2s]
# 終わりの 0.85 秒で見出し・札・帯・署名が消え、紙の地だけが残る
[<#h9 cut-150][<#cc1 cut-150][<#cc2 cut-150][<#cc3 cut-150][<#tb_mark cut-150][<#tb_slash cut-150][<#tb_brand cut-150][<#tb_sep cut-150][<#tb_sub cut-150][<#tb_dot cut-150][<#tb_line cut-150][<#ch9 cut-150][<#signoff cut-50]
```

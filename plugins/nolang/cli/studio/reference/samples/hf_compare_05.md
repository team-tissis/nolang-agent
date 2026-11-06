# compare · cad-reverse (hf 全力版の全量の写し — 通常のCADモデリングとリバースモデリングの違い・方眼の図解 7 場面で形が変形して見せる 2 つの向き) — canvas 1920x1080

見せる作り: 方眼の明るい地と下端の進行線・青 (通常の CAD) と橙 (リバース) で通す 2 色・開幕の題 (半分が線画の金具の写真・語で伸びる下線・逆向きの矢印 2 本)・点線の置き場を語ごとに埋める 2 段の流れ図・中央に大きく出て左上へ収まる章の見出し・右の工程の板を語ごとに点灯 (cue)・スケッチの輪郭を描いて等角の立体へ変形し押し出し・カーソルで寸法の数値を替えると形ごと伸びる・写真の板 (判子・光の帯が走るスキャン)・点群 → メッシュ → 寄って「寸法 = ？」→ 面と穴を当てはめた CAD モデル・測った形が本来の形へ整う 2 枚の板・2 列の比較表・写真つきの使い分けの板を沈めて組み合わせの流れ図・2 行の式で締め・音の層 (BGM + 語ごとの効果音 40 発)

```design.txt
#v2
# 学ぶ作り: 方眼の明るい地の上で 7 場面を溶かして替える (場面の要素は自分では退場せず、切替の dissolve でまとめて替わる)・下端に全編の進行線・白い札の字幕
# 2 つの手法を色で通す: 通常の CAD = 青・リバース = 橙。章の見出しは中央に大きく出してから左上へ縮んで収まる (keys の入場 1 本)
# 図の主役は path= の図形の変形 (morph・全部の状態の先頭に線を引かない M 2 つで同じ枠を固定し、頂点だけを補間させる): スケッチの輪郭 → 等角の正面 → 押し出しで面が伸びる → 寸法の数値で長くなる・測った面と穴が本来の形へ整う
# 点群とメッシュは path=scatter (L 字の輪郭 + 穴 2 つの path を clip に・同じ seed の 2 枚で点と辺)・右の工程の板は語ごとに点灯 (cue)
# hf 05 cad-reverse (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#F5F7FA
theme light
palette a=#2563EB b=#E4600F ink=#14213D sub=#5B6B82 mute=#8A97AA blue=#2563EB blue_d=#1D3B8B blue_t=#DCE7FF blue_tt=#EEF3FF orange=#E4600F orange_d=#9A3D0A orange_t=#FFE3CC orange_tt=#FFF3EA line=#D5DEEA paper=#F5F7FA mark=#FFE08A ph=#C3CEDC grid=#EDF1F6 grid2=#E4EAF2 vgrid=#EEF2F7 bulb=#F2B705 f1=#9DB6F5 f2=#7F9CEB f3=#BCD0FA hole=#22325E r1=#FDB98A r2=#F79A5C r3=#FFD0AE rhole=#5B2A0C meshc=#F08A4B step=#8592A6 st_t=#6F7C90 st_s=#7F8CA0 done=#4F5D72 rule=#E2E8F0
font "クセのない現代的な角ゴシック体の極太、ビジネス資料の見出し向け"
fonts m="クセのない現代的な角ゴシック体のBold、太すぎず細すぎない本文と字幕向け" e="丸みのあるジオメトリックで癖のない現代的な欧文サンセリフのExtraBold、UIやウェブ向け、数字がくっきり"
sfx off
# hf の作り: 章の見出し・表の列の見出しは台詞より先に置く (spoiler)・点群やメッシュの札は台詞の語をそのまま札にする (duplicate_text)・図と札だけの場面が続く (text_only_cut)
lint off=spoiler,duplicate_text,text_only_cut
# hf の作り: 1080p の 20〜36px の小さな説明 (工程の板の小文字・PROCESS・寸法の値) をそのまま 2/3 に写す (small_text)・工程の板は番号が縦に積まれる一覧 (stacked_labels)
# hf の作り: スケッチの寸法は押し出しの 0.75 秒前に消える・点群やメッシュの札は次の文の頭で替わる (flash_text)・開幕の矢印は最後の語で出て溶ける (entrance_in_fadeout / ghost_dissolve)
# hf の作り: 組み合わせの図を出す語で使い分けの 2 枚を 0.16 まで沈める (low_contrast)・同じ古い部品の写真を板と流れ図に 2 度使う (duplicate_media)・使い分けの 2 枚は 6 秒動かない (still_stretch)
prompt_tail "文字なし、ラベルなし、ロゴなし、人物なし、手なし"
run m { color: $ink; marker: $mark,38% }
run bn { color: $blue; font-family: e }
run bl { color: $blue }
run sm { font-size: 22px; color: $sub; font-family: m }
p { color: $ink; line-height: 1.2; out: none }
div { out: none }
img { out: none }
icon { out: none }
shape { out: none }
group { out: none }
# 入場の型 (hf の inn / pop: 下から 39px・0.55 s・power3.out / 0.55 倍から back.out)
motion up { in: {y:26, opacity:0, duration:0.55, ease:'power3.out'} }
motion popin { in: {scale:0.55, opacity:0, duration:0.5, ease:'back.out(1.9)'} }
image old = "[photo]使い込まれた古い鋳鉄のL字の機械用ブラケット、丸いボルト穴が2つ、くすんだ濃い灰色の金属に傷と小さな欠けと角の丸い摩耗と錆の点、明るい木の作業台の中央に1つだけ置かれている、明るい工房、柔らかい自然光、背景の工具棚はぼけている" aspect=16:9
image product = "[photo]新しく削り出したアルミのL字ブラケット（穴が2つ）が何個も同じ向きでステンレスの作業台に一列に並ぶ、明るい現代的な工場、奥にCNCフライス盤がぼけて見える、冷たく澄んだ昼の光、整然として精密" aspect=16:9
sound title = "力強いシンセの和音に明るい高域のノイズが重なる、タイトルが出るシャキーン"
sound pop = "ビジネス動画向けの短く明るい電子音のポンッ"
sound pop2 = "控えめで明るいシンプルな電子のピコン"
sound soft = "サイン波がゆったり膨らむ柔らかいふわん"
sound swish = "リバーブの効いた空気感のある短いシュッ"
sound chapter = "点火音から広がるリバーブの深いシューン、章の切り替わり"
sound click = "マウスのカチッという乾いたクリック音"
sound scan = "未来的なサイバーの上昇音シュイーン"
sound data = "コンピューターが解析するピピピピという連続した電子音"
sound mesh = "デジタルに音色が変わりながら上がるサイバーの起動音ヒュイーン"
sound emph = "柔らかいシンセベルの高い和音のポーン"
# 工程の板の点灯 (地と縁・番号の丸・字の色・小さく弾む) と済み (地を戻し字を少し沈める)
cue on(x, c) = [!#x .on][!#x.n fill,{c}][!#x.t recolor,$ink][!#x.s recolor,$sub][!#x punch {scale: 1.03, duration: .36}]
cue done(x) = [=#x][!#x.t recolor,$done][!#x.s recolor,$st_t]
bgm#music(fade: 800,3200) 軽快にシンコペーションするピアノのリズムに一定の電子ビートと温かいシンセパッドが重なる、明るくモダンで邪魔にならない、企業のプレゼンや技術解説向け
# 字幕: 白い札 (下に寄せ・文ごと・句末の約物は外す・長い文は台詞の [|] で 2 枚に)
subtitle.hug(bottom: 44px; font-family: m; font-size: 40px; line-height: 1.3; color: $ink; background: #FFFFFFF0; border-radius: 18px; padding: 14px 36px 16px 36px; box-shadow: 0 8px 26px #14213D1F; unit: sentence; strip: 、。; lead: 0ms; tail: 0ms; hold: off; in: {y:10, opacity:0, duration:.16, ease:'power2.out'}; out: {opacity:0, duration:.12, ease:'power1.in'})

# 部品: 白い板 (角丸 + 柔らかい影)
def card = div(border-radius: 26px; background: #FFFFFF; box-shadow: 0 18px 50px #14213D1A)
# 英字の小見出し + 題 (場面の頭に印なしで置く)
def khead(k, t) = div(left: 130px; top: 64px; width: 1350px; height: 90px; delay: 200ms; in: up)
  p#k(left: 0px; top: 0px; font-family: e; font-size: 20px; letter-spacing: .22em; color: $sub; content: {k})
  p#t(left: 0px; top: 24px; font-size: 50px; line-height: 1.05; content: {t})
# 章の見出し: 画面の中央に 1.75 倍で出て 1 秒待ち、左上へ縮んで収まる (hf の chapterHead = keys の入場 1 本)
def chead(n, t, s, c, w) = div(left: 130px; top: 64px; width: {w}; height: 69px; delay: 250ms; in: keys(at=0 x=401 y=410 scale=1.75 opacity=0 | at=0.28 x=401 y=410 scale=1.75 opacity=1 ease=power3.out | at=0.67 x=401 y=410 scale=1.75 | at=1 ease=power3.inOut),duration=1800)
  p#n(left: 0px; bottom: 0px; font-family: e; font-size: 64px; line-height: .9; color: {c}; content: {n})
  p#t(left: 105px; bottom: 0px; font-size: 50px; line-height: 1.05; content: {t})
  p#s(left: .t.right+22; bottom: 6px; font-family: m; font-size: 24px; color: $sub; white-space: nowrap; content: {s})
# 右の工程の板 (番号の丸 + 題 + 小さな説明・灰で置いて語ごとに点灯)
def step(n, t, s, tt=23, st=65) = div(width: 550px; height: 112px; border-radius: 20px; background: #FFFFFF8C; in: {y:20, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.08}})
  p#n(left: 26px; cy: 50%; width: 62px; font-family: e; font-size: 28px; line-height: 1; text-align: center; color: #FFFFFF; background: $step; border-radius: 148px; padding: 16px 0px; content: {n})
  p#t(left: 110px; top: {tt}; font-size: 32px; color: $st_t; content: {t})
  p#s(left: 110px; top: {st}; font-family: m; font-size: 21px; color: $st_s; content: {s})
# 図の左上の札 (白 + 色の縁・小さな説明は run sm)
def chip(t, c, bc) = p(left: 166px; top: 226px; font-size: 30px; color: {c}; background: #FFFFFF; border: 3px solid {bc}; border-radius: 14px; padding: 10px 22px; box-shadow: 0 8px 24px #14213D1F; in: {y:-12, opacity:0, duration:.55, ease:'power3.out'}; out: {opacity:0, duration:.25, ease:'power2.in'}; content: {t})
# 流れ図の丸 (白い円 + 色の縁 + 下に名)・中身の icon / 写真は実体ごとに子を足す
def node(t, c) = div(width: 240px; height: 210px; in: popin)
  div#d(cx: 50%; top: 0px; width: 150px; height: 150px; border-radius: 148px; background: #FFFFFF; border: 4px solid {c}; box-shadow: 0 12px 30px #14213D1F)
  p#t(cx: 50%; top: 164px; font-size: 32px; content: {t})
# 手法の色の丸札
def pill(t, c) = p(font-size: 30px; color: #FFFFFF; background: {c}; border-radius: 148px; padding: 10px 26px; content: {t})
# 結果の行き先の板 (icon / 写真の角丸 + 題 + 説明)
def flowcard(t, s) = div(left: 1240px; width: 550px; height: 200px; border-radius: 26px; background: #FFFFFF; box-shadow: 0 18px 50px #14213D1A; in: {x:60, opacity:0, duration:.55, ease:'power3.out'})
  div#f(left: 30px; cy: 50%; width: 130px; height: 130px; border-radius: 20px; background: $blue_tt)
  p#t(left: 186px; top: 54px; font-size: 40px; content: {t})
  p#s(left: 186px; top: 111px; font-family: m; font-size: 22px; color: $sub; content: {s})
# 方眼の地 (40 px と 240 px の 2 重の格子・全編でゆっくり左上へ流れる) + 右上の白い光 + 下端の進行線
div#grid1(left: 0px; top: 0px; width: 2160px; height: 1200px; pattern: grid,27,$grid; bleed; z-index: back; border-radius: 24px; in: none; main: ramp {x: -240, y: -120, period: '180s'})
div#grid2(left: 0px; top: 0px; width: 2160px; height: 1200px; pattern: grid,160,$grid2; bleed; z-index: back; border-radius: 24px; in: none; main: ramp {x: -240, y: -120, period: '180s'})
div#glow(inset: 0; background: radial(#FFFFFFBF,#FFFFFF00,70%,40%); z-index: back; border-radius: 24px; in: none)
div#prog_track(left: 0px; top: 1074px; width: 1920px; height: 6px; background: #14213D0F; z-index: front; border-radius: 24px; in: none)
progress#prog(left: 0px; top: 1074px; width: 1920px; height: 6px; background: linear($blue,$orange,90); until: end; z-index: front; overlap: prog_track)

# s1 開幕: 右に半分 CAD の線画・半分実物の金具の写真、左に題 (小見出し → 青 → と → 橙) が組み上がり、語で下線が伸びる・「なにが違う？」と逆向きの矢印 2 本
section#s1
img#s1_hero(left: 700px; top: 70px; width: 1240px; height: 698px; bleed; delay: 100ms; in: {scale:1.08, opacity:0, duration:1.2, ease:'power2.out'}; main: kb {scale: [1.04, 1.04], focus: ['45% 50%', '55% 50%']}) [photo]アルミを削り出したL字の取り付けブラケット（丸いボルト穴が2つ）が1つ、斜め45度から見た姿で中央に。左半分は青く光る精密なCADのワイヤーフレームと細い作図線、右半分はヘアラインの金属の実物で柔らかい反射、縦の境目でくっきり分かれる。ごく明るい冷たい灰色の継ぎ目のないスタジオの背景が画面の縁へ溶ける、拡散した柔らかい光、ミニマルで現代的な工業デザイン
div#s1_k(left: 130px; top: 176px; width: 450px; height: 36px; delay: 300ms; in: {y:16, opacity:0, duration:.55, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 46px; height: 4px; border-radius: 3px; background: $ink)
  p#t(left: 62px; cy: 50%; font-size: 30px; letter-spacing: .08em; color: $sub) 3分でわかる
div#s1_cad_u(left: 130px; top: 336px; width: 690px; height: 14px; border-radius: 8px; background: $blue; opacity: .22; in: {scaleX:0, pivot:'left', duration:.6, ease:'power3.out'})
p#s1_cad(left: 130px; top: 230px; font-size: 104px; line-height: 1.22; color: $blue; delay: 450ms; in: {y:44, opacity:0, duration:.7, ease:'power3.out'}) CADモデリング
p#s1_to(left: 138px; top: 370px; font-size: 50px; color: $sub; delay: 700ms; in: {y:20, opacity:0, duration:.55, ease:'power3.out'}) と
div#s1_rev_u(left: 130px; top: 550px; width: 940px; height: 14px; border-radius: 8px; background: $orange; opacity: .22; in: {scaleX:0, pivot:'left', duration:.7, ease:'power3.out'})
p#s1_rev(left: 130px; top: 444px; font-size: 104px; line-height: 1.22; color: $orange; delay: 850ms; in: {y:44, opacity:0, duration:.7, ease:'power3.out'}) リバースモデリング
p#s1_q(left: 130px; top: 700px; font-size: 64px; color: #FFFFFF; background: $ink; border-radius: 14px; padding: 6px 26px 10px 26px; in: {y:20, opacity:0, duration:.55, ease:'power3.out'}) なにが違う？
shape#s1_ar_b(left: 141px; top: 826px; width: 394px; height: 40px; path: arrow_r,head=fill; background: $blue; border: 10px solid $blue; in: {x:-90, opacity:0, duration:.55, ease:'power3.out'})
shape#s1_ar_o(left: 582px; top: 870px; width: 394px; height: 40px; path: arrow_l,head=fill; background: $orange; border: 10px solid $orange; in: {x:90, opacity:0, duration:.55, ease:'power3.out'})

# s2 ひとことで: 点線の丸の置き場 6 つを先に敷き、上の段は左から右へ (アイデア → 形 → 製品)、下の段は右から左へ (実物 → 測る → 設計データ) 語ごとに弾んで埋まる
section#s2
khead#s2_head(k: "IN A WORD"; t: "ひとことで言うと、{m}進む「向き」が逆{/}")
shape#s2_ph(left: "695;1095;1496;1496;1095;695"; top: "326;326;326;645;645;645"; width: 150px; height: 150px; path: rect,r=0.5; background: #FFFFFF80; border: 3px solid $ph; dash: 6,6; delay: 350ms; in: {opacity:0, duration:.4, ease:'power3.out', stagger:{each:.05}}) ×6
pill#s2_l1(left: 130px; top: 370px; t: "CADモデリング"; c: $blue; in: {x:-40, opacity:0, duration:.55, ease:'power3.out'})
pill#s2_l2(left: 130px; top: 690px; t: "リバースモデリング"; c: $orange; in: {x:-40, opacity:0, duration:.55, ease:'power3.out'})
p#s2_fwd(left: 130px; top: 470px; font-size: 30px; color: $blue_d; in: {x:-20, opacity:0, duration:.55, ease:'power3.out'}) 向き →
p#s2_rev(left: 130px; top: 790px; font-size: 30px; color: $orange_d; in: {x:30, opacity:0, duration:.55, ease:'power3.out'}) ← 向きが逆
shape#s2_a1(left: 888px; top: 386px; width: 164px; height: 30px; path: arrow_r; background: $blue; border: 8px solid $blue; in: draw {duration: 0.5})
shape#s2_a2(left: 1288px; top: 386px; width: 164px; height: 30px; path: arrow_r; background: $blue; border: 8px solid $blue; in: draw {duration: 0.5})
shape#s2_a3(left: 1288px; top: 705px; width: 164px; height: 30px; path: arrow_l; background: $orange; border: 8px solid $orange; in: draw {duration: 0.5})
shape#s2_a4(left: 888px; top: 705px; width: 164px; height: 30px; path: arrow_l; background: $orange; border: 8px solid $orange; in: draw {duration: 0.5})
node#s2_n1(left: 651px; top: 326px; t: "アイデア"; c: $blue)
  icon#i(cx: 50%; top: 38px; font-size: 76px; name: lightbulb; color: $blue)
node#s2_n2(left: 1050px; top: 326px; t: "形（3Dモデル）"; c: $blue)
  icon#i(cx: 50%; top: 38px; font-size: 76px; name: cube; color: $blue)
node#s2_n3(left: 1450px; top: 326px; t: "製品"; c: $blue)
  img#p(cx: 50%; top: 4px; width: 141px; height: 141px; border-radius: 148px; object-fit: cover; object-position: 30% 60%; content: @product; main: none)
node#s2_n4(left: 1450px; top: 645px; t: "実物"; c: $orange)
  img#p(cx: 50%; top: 4px; width: 141px; height: 141px; border-radius: 148px; object-fit: cover; object-position: 45% 50%; zoom: 160%; content: @old; main: none)
node#s2_n5(left: 1050px; top: 645px; t: "測る"; c: $orange)
  icon#i(cx: 50%; top: 38px; font-size: 76px; name: scan; color: $orange)
node#s2_n6(left: 651px; top: 645px; t: "設計データ"; c: $orange)
  icon#i(cx: 50%; top: 38px; font-size: 76px; name: file-text; color: $orange)

# s3 通常の CAD: 章の見出し → 方眼の図の板と右の工程 4 段。要望の板 → スケッチの輪郭を描く (draw) と寸法 → 輪郭が等角の正面へ変形し 4 面が押し出しで伸びる → カーソルが寸法を 120 → 160 に替えると形ごと伸びる
section#s3
chead#s3_head(n: "01"; t: "通常のCADモデリング"; s: "アイデア → 形"; c: $blue; w: 810)
card#s3_vp(left: 130px; top: 196px; width: 1060px; height: 690px; pattern: grid,23,$vgrid; in: {y:30, opacity:0, duration:.7, ease:'power3.out'})
p#s3_ptitle(left: 1245px; top: 195px; font-family: e; font-size: 20px; letter-spacing: .2em; color: $sub; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}) PROCESS
step#s3_st(left: 1240px; top: "236;366;497;626"; n: "1;2;3;4"; t: "アイデア・仕様;スケッチ＋寸法;押し出し・回転;寸法を変えれば"; s: "つくりたい形と寸法を決める;平面に輪郭を描く;立体に起こす;形もそれに合わせて更新") ×4
#s3_st.on(background: $blue_tt; border: 3px solid $blue)
# 要望の板 (電球 + 題 + 例 + 3 行の仕様・数字は欧文の青)
card#req(left: 430px; top: 346px; width: 460px; height: 310px; in: up; out: {x:40, opacity:0, duration:.35, ease:'power2.in'})
  icon#i(left: 38px; top: 32px; font-size: 50px; name: lightbulb; weight: fill; color: $bulb)
  p#h(left: 96px; top: 38px; font-size: 34px) こんな部品がほしい
  p#ex(left: 38px; top: 88px; font-family: m; font-size: 20px; color: $sub) （例）L字の取り付け金具
  p#l(left: 38px; top: "131;180;230"; font-family: m; font-size: 28px; in: {y:12, opacity:0, duration:.55, ease:'power3.out'}) ×3 ・長さ {bn}120{/} / 高さ {bn}90{/} mm;・板の厚さ {bn}14{/} mm;・ネジ穴を {bn}2{/} か所
# 等角の L 字 (群 iso: 正面 = スケッチの輪郭の変種・残り 4 面は潰れた形で出て押し出しで伸びる・穴 2 つ・群ごと上下に浮く)
group#iso
shape#iso.front(path: "M377.0 317.5 M966.8 807.0 M380.0 716.0 L811.9 716.0 L811.9 665.5 L430.3 665.5 L430.3 392.0 L380.0 392.0 Z"; background: #2563EB0F; border: 4px solid $blue; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: draw {duration: 1.7})
#iso.front.iso(path: "M377.0 317.5 M966.8 807.0 M460.0 666.0 L795.9 758.0 L795.9 716.4 L499.2 635.2 L499.2 409.8 L460.0 399.0 Z"; background: $f1; border: 3px solid $blue_d; move: 700ms,power2.inOut)
#iso.front.long(path: "M377.0 317.5 M966.8 807.0 M404.1 681.3 L851.8 804.0 L851.8 762.5 L443.2 650.5 L443.2 425.1 L404.1 414.5 Z"; move: 1100ms,power2.inOut)
shape#iso.top_h(path: "M377.0 317.5 M966.8 807.0 M499.2 635.2 L795.9 716.4 L795.9 716.4 L499.2 635.2 Z"; background: $blue_t; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.top_h.ext(path: "M377.0 317.5 M966.8 807.0 M499.2 635.2 L795.9 716.4 L907.8 638.0 L611.1 556.7 Z"; move: 1300ms,power2.inOut)
#iso.top_h.long(path: "M377.0 317.5 M966.8 807.0 M443.2 650.5 L851.8 762.5 L963.8 684.0 L555.2 572.0 Z"; move: 1100ms,power2.inOut)
shape#iso.end_h(path: "M377.0 317.5 M966.8 807.0 M795.9 758.0 L795.9 758.0 L795.9 716.4 L795.9 716.4 Z"; background: $f2; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.end_h.ext(path: "M377.0 317.5 M966.8 807.0 M795.9 758.0 L907.8 679.5 L907.8 638.0 L795.9 716.4 Z"; move: 1300ms,power2.inOut)
#iso.end_h.long(path: "M377.0 317.5 M966.8 807.0 M851.8 804.0 L963.8 725.4 L963.8 684.0 L851.8 762.5 Z"; move: 1100ms,power2.inOut)
shape#iso.inner_v(path: "M377.0 317.5 M966.8 807.0 M499.2 635.2 L499.2 635.2 L499.2 409.8 L499.2 409.8 Z"; background: $f3; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.inner_v.ext(path: "M377.0 317.5 M966.8 807.0 M499.2 635.2 L611.1 556.7 L611.1 331.2 L499.2 409.8 Z"; move: 1300ms,power2.inOut)
#iso.inner_v.long(path: "M377.0 317.5 M966.8 807.0 M443.2 650.5 L555.2 572.0 L555.2 346.6 L443.2 425.1 Z"; move: 1100ms,power2.inOut)
shape#iso.top_v(path: "M377.0 317.5 M966.8 807.0 M460.0 399.0 L499.2 409.8 L499.2 409.8 L460.0 399.0 Z"; background: $blue_t; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.top_v.ext(path: "M377.0 317.5 M966.8 807.0 M460.0 399.0 L499.2 409.8 L611.1 331.2 L572.0 320.5 Z"; move: 1300ms,power2.inOut)
#iso.top_v.long(path: "M377.0 317.5 M966.8 807.0 M404.1 414.5 L443.2 425.1 L555.2 346.6 L516.0 335.9 Z"; move: 1100ms,power2.inOut)
shape#iso.ha(points: "815.4,698.0 817.2,696.5 818.6,694.8 819.4,693.2 819.9,691.5 819.8,689.7 819.2,688.0 818.1,686.4 816.4,684.9 814.3,683.4 811.9,682.2 809.1,681.0 805.9,680.0 802.5,679.2 798.9,678.6 795.2,678.2 791.2,678.0 787.3,678.0 783.6,678.3 779.8,678.8 776.2,679.5 772.9,680.4 769.9,681.5 767.2,682.8 765.0,684.2 763.2,685.7 761.8,687.2 761.0,688.8 760.5,690.6 760.7,692.2 761.2,693.9 762.5,695.5 764.0,697.0 766.0,698.5 768.4,699.9 771.3,701.1 774.4,702.0 777.9,702.9 781.5,703.5 785.2,703.8 789.2,704.0 793.1,704.0 796.9,703.7 800.6,703.2 804.2,702.5 807.4,701.5 810.4,700.5 813.2,699.3"; background: $hole; border: 2px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: popin)
shape#iso.hb(points: "515.0,475.7 514.8,472.3 514.3,469.2 513.8,466.3 512.8,463.8 511.7,461.7 510.3,460.0 508.8,458.8 507.0,458.1 505.2,457.8 503.2,458.1 501.2,458.8 499.2,460.0 497.1,461.7 495.2,463.8 493.2,466.2 491.2,469.0 489.6,472.2 488.1,475.7 486.8,479.2 485.5,482.8 484.7,486.8 483.9,490.5 483.6,494.1 483.5,497.7 483.6,501.2 483.9,504.3 484.7,507.2 485.5,509.5 486.8,511.7 488.1,513.5 489.6,514.7 491.2,515.4 493.2,515.5 495.2,515.4 497.1,514.7 499.2,513.5 501.2,511.8 503.2,509.7 505.2,507.2 507.0,504.3 508.8,501.2 510.3,497.8 511.7,494.2 512.8,490.5 513.8,486.8 514.3,483.0 514.8,479.2"; background: $hole; border: 2px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: popin)
# スケッチの寸法 (細い線と端の目盛り + 欧文の数字)
group#sk_dims(in: {opacity:0, duration:.4}; out: {opacity:0, duration:.25, ease:'power2.in'})
  div#h(left: 380px; top: 760px; width: 432px; height: 3px; background: $blue_d)
  div#hl(left: 378px; top: 744px; width: 3px; height: 36px; background: $blue_d)
  div#hr(left: 810px; top: 744px; width: 3px; height: 36px; background: $blue_d)
  div#v(left: 328px; top: 392px; width: 3px; height: 324px; background: $blue_d)
  div#vt(left: 312px; top: 390px; width: 36px; height: 3px; background: $blue_d)
  div#vb(left: 312px; top: 714px; width: 36px; height: 3px; background: $blue_d)
  div#s(left: 849px; top: 666px; width: 3px; height: 51px; background: $blue_d)
  div#st(left: 834px; top: 664px; width: 32px; height: 3px; background: $blue_d)
  div#sb(left: 834px; top: 716px; width: 32px; height: 3px; background: $blue_d)
  p#n120(cx: 596px; top: 784px; font-family: e; font-size: 30px; color: $blue_d) 120
  p#n90(left: 267px; top: 540px; font-family: e; font-size: 30px; color: $blue_d) 90
  p#n14(left: 878px; top: 676px; font-family: e; font-size: 30px; color: $blue_d) 14
chip#s3_chip(t: "3Dモデル"; c: $blue_d; bc: $blue)
# 等角の寸法線 (線 + 両端の点 + 数値の札) とカーソル: 数値を替える語で線・点・札が形と一緒に伸びる (群の member の to は transform・カーソルの下がりは語からの main ramp)
group#isodim(in: {opacity:0, duration:.4}; out: {opacity:0, duration:.3, ease:'power2.in'})
  shape#l(path: "M385.7 719.0 M839.6 862.9 M444.8 722.0 L780.4 813.9"; background: none; border: 3px solid $blue_d)
  shape#a(left: 438px; top: 716px; width: 12px; height: 12px; border-radius: 50%; background: $blue_d)
  shape#b(left: 774px; top: 808px; width: 12px; height: 12px; border-radius: 50%; background: $blue_d)
  p#tag(left: 540px; top: 780px; width: 124px; font-family: e; font-size: 30px; text-align: center; color: $blue_d; background: #FFFFFF; border: 3px solid $blue; border-radius: 14px; padding: 12px 0px) 120
  shape#cur(left: 628px; top: 814px; width: 34px; height: 48px; path: cursor; background: $ink; border: 3px solid #FFFFFF; in: {x:90, y:-60, opacity:0, duration:.6, ease:'power3.out'}; out: {opacity:0, duration:.3, ease:'power2.in'})
#isodim.l.long(path: "M385.7 719.0 M839.6 862.9 M388.7 737.2 L836.6 859.9"; move: 1100ms,power2.inOut)
# 作業の履歴の板 (右の工程と入れ替わる)・項目 4 つ + 意図の帯
card#tree(left: 1240px; top: 196px; width: 550px; height: 690px; in: up; out: {x:40, opacity:0, duration:.35, ease:'power2.in'})
  p#h(left: 36px; top: 34px; font-size: 34px) 作業の手順が残る
  p#ex(left: 36px; top: 81px; font-family: m; font-size: 21px; color: $sub) （例）履歴・フィーチャーの一覧
  div#it(left: 36px; top: "117;206;294;383"; width: 478px; height: 78px; border-radius: 16px; background: $blue_tt; in: {y:12, opacity:0, duration:.55, ease:'power3.out'}) ×4
    icon#i(left: 20px; cy: 50%; font-size: 40px; name: "pencil-simple;stack;record;record"; color: $blue)
    p#t(left: 78px; cy: 50%; font-size: 30px; color: $blue_d) スケッチ;押し出し;穴;穴
    p#v(right: 20px; cy: 50%; font-family: e; font-size: 24px; color: $sub) 120×90;64;φ18;φ18
  p#intent(left: 36px; top: 486px; width: 478px; font-size: 30px; text-align: center; color: #FFFFFF; background: $blue; border-radius: 16px; padding: 18px 0px; in: {y:12, opacity:0, duration:.55, ease:'power3.out'}) 寸法と手順 ＝ 設計者の意図
flowcard#fc1(top: 196px; t: "図面"; s: "寸法や指示を伝える")
  icon#i(left: 58px; cy: 50%; font-size: 74px; name: blueprint; color: $blue)
flowcard#fc2(top: 441px; t: "試作"; s: "形や組み付けを確かめる")
  icon#i(left: 58px; cy: 50%; font-size: 74px; name: package; color: $blue)
flowcard#fc3(top: 686px; t: "製造"; s: "同じ形をつくる")
  img#p(left: 30px; cy: 50%; width: 130px; height: 130px; border-radius: 20px; content: @product; main: none)

# s4 リバース: 章の見出し → 図の板と右の工程 5 段。古い部品の写真 (判子「図面なし」) → スキャナーの写真を光の帯が走る → 点群が左から湧き → 同じ点を辺でつないだメッシュ → 寄って「寸法 = ？」→ 面と穴を当てはめた CAD モデル → 測った形と本来の形の 2 枚の板
section#s4
chead#s4_head(n: "02"; t: "リバースモデリング"; s: "モノ → データ"; c: $orange; w: 740)
card#s4_vp(left: 130px; top: 196px; width: 1060px; height: 690px; pattern: grid,23,$vgrid; in: {y:30, opacity:0, duration:.7, ease:'power3.out'})
p#s4_ptitle(left: 1245px; top: 195px; font-family: e; font-size: 20px; letter-spacing: .2em; color: $sub; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}) PROCESS
step#s4_st(left: 1240px; top: "236;356;476;596;716"; height: 104px; tt: 18; st: 59; n: "1;2;3;4;5"; t: "実物;3Dスキャン;点群データ;メッシュ;CADモデル"; s: "図面のない部品など;表面の形を測る;無数の点の集まり;三角形の面でつなぐ;平面・円筒を当てはめる") ×5
#s4_st.on(background: $orange_tt; border: 3px solid $orange)
img#ph_old(left: 130px; top: 196px; width: 1060px; height: 690px; border-radius: 26px; content: @old; in: fade {duration: 0.6}; out: fade {duration: 0.6}; main: kb {scale: [1.14, 1], ease:'power1.out'})
p#stamp(left: 770px; top: 286px; font-size: 44px; color: $orange; background: #FFFFFFDB; border: 4px solid $orange; border-radius: 14px; padding: 10px 26px; transform: rotate(-7deg); in: {scale:1.7, opacity:0, duration:.5, ease:'back.out(1.7)'}; out: {opacity:0, duration:.25, ease:'power2.in'}) 図面なし
img#ph_scan(left: 130px; top: 196px; width: 1060px; height: 690px; border-radius: 26px; in: fade {duration: 0.5}; out: fade {duration: 0.6}; main: kb {scale: [1, 1.08]}) [ref:@old]三脚に載った業務用の構造化光3Dスキャナーが、小さな丸いターンテーブルの上の同じ古い金属のL字ブラケットに細い平行な青い光の縞を投影している。明るい灰色の背景の清潔な工房、周りの光は少し落として部品の上の青い縞がくっきり見える、部品にピント
# スキャンの光の帯 (板の窓で切る群・帯は main の keys で出てから 2.8 秒かけて左から右へ走る)
group#scan(clip: 17,scan.win)
  div#win(left: 130px; top: 196px; width: 1060px; height: 690px)
  div#bar(left: -30px; top: 196px; width: 140px; height: 690px; background: linear(#3B82F600,#60A5FA8C@70%,#DBEAFEF2@92%,#3B82F600,90); mix-blend-mode: screen; bleed; border-radius: 24px; in: fade {duration: 0.15}; out: fade {duration: 0.2}; main: keys(at=0 x=0 | at=1 x=1241 ease=power1.inOut),freq_ms=2800,window=0,2800,forwards)
# 点群 → メッシュ → CAD モデルの群 (外の群 rv が図の板の窓で切り、中の群 rv.rev を寄る / 戻す / 薄める)・L 字の輪郭と穴 2 つの path が scatter の clip
group#rv(clip: 17,rv.win)
div#rv.win(left: 130px; top: 196px; width: 1060px; height: 690px)
group#rv.rev
shape#rv.rev.sil(path: "M416.0 682.0 L782.4 782.4 L904.5 696.8 L904.5 651.5 L580.8 562.8 L580.8 316.8 L538.0 305.1 L416.0 390.8 ZM742.7 666.6 L746.1 663.3 L747.6 659.5 L746.7 656.0 L743.8 652.5 L738.9 649.3 L732.3 647.1 L724.7 645.5 L716.2 644.8 L707.8 645.3 L699.9 646.5 L693.2 648.8 L687.8 651.6 L684.2 654.9 L682.8 658.7 L683.5 662.2 L686.5 665.7 L691.5 668.8 L698.0 671.1 L705.8 672.8 L714.0 673.3 L722.4 672.9 L730.3 671.7 L737.2 669.5 ZM537.0 457.7 L536.4 450.5 L534.6 444.8 L531.9 440.5 L528.3 438.5 L524.2 438.5 L519.8 440.5 L515.4 444.6 L511.2 450.5 L507.6 457.7 L504.9 465.6 L503.2 473.8 L502.7 481.8 L503.2 488.8 L504.9 494.7 L507.6 498.8 L511.2 501.0 L515.4 501.0 L519.8 498.8 L524.2 494.7 L528.3 488.8 L531.9 481.8 L534.6 473.8 L536.4 465.6 Z"; background: none; border: none; opacity: 0; in: none)
shape#rv.rev.top_h(points: "458.7,648.5 782.4,737.1 904.5,651.5 580.8,562.8"; background: $orange_t; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.inner_v(points: "458.7,648.5 580.8,562.8 580.8,316.8 458.7,402.5"; background: $r3; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.front(points: "416.0,682.0 782.4,782.4 782.4,737.1 458.7,648.5 458.7,402.5 416.0,390.8"; background: $r1; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.end_h(points: "782.4,782.4 904.5,696.8 904.5,651.5 782.4,737.1"; background: $r2; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.top_v(points: "416.0,390.8 458.7,402.5 580.8,316.8 538.0,305.1"; background: $orange_t; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.mesh(left: 410px; top: 298px; width: 501px; height: 489px; path: scatter,n=1200,seed=5,dot=3,clip=rv.rev.sil,mesh=3; background: $orange; border: 2px solid $meshc; in: wipe {dir: 'right', duration: 1.4}; out: fade {duration: 0.6})
shape#rv.rev.cloud(left: 410px; top: 298px; width: 501px; height: 489px; path: scatter,n=1200,seed=5,dot=3,clip=rv.rev.sil; background: $orange; in: wipe {dir: 'right', duration: 1.5}; out: fade {duration: 0.7})
shape#rv.rev.ha(points: "742.7,666.6 744.6,665.0 746.1,663.3 747.2,661.5 747.6,659.5 747.5,657.8 746.7,656.0 745.5,654.2 743.8,652.5 741.6,650.8 738.9,649.3 735.8,648.2 732.3,647.1 728.5,646.2 724.7,645.5 720.6,645.2 716.2,644.8 712.0,645.0 707.8,645.3 703.8,645.8 699.9,646.5 696.3,647.5 693.2,648.8 690.2,650.1 687.8,651.6 685.7,653.2 684.2,654.9 683.2,656.7 682.8,658.7 683.0,660.5 683.5,662.2 684.9,664.0 686.5,665.7 688.8,667.3 691.5,668.8 694.5,670.0 698.0,671.1 701.7,672.0 705.8,672.8 709.8,673.0 714.0,673.3 718.3,673.2 722.4,672.9 726.6,672.5 730.3,671.7 734.0,670.7 737.2,669.5 740.2,668.1"; background: $rhole; border: 3px solid $orange_d; in: popin)
shape#rv.rev.hb(points: "537.0,457.7 536.8,453.9 536.4,450.5 535.7,447.5 534.6,444.8 533.4,442.3 531.9,440.5 530.2,439.2 528.3,438.5 526.3,438.2 524.2,438.5 522.0,439.2 519.8,440.5 517.5,442.3 515.4,444.6 513.2,447.5 511.2,450.5 509.4,453.9 507.6,457.7 506.1,461.5 504.9,465.6 504.0,469.7 503.2,473.8 502.8,477.9 502.7,481.8 502.8,485.4 503.2,488.8 504.0,492.0 504.9,494.7 506.1,497.0 507.6,498.8 509.4,500.1 511.2,501.0 513.2,501.2 515.4,501.0 517.5,500.1 519.8,498.8 522.0,497.0 524.2,494.7 526.3,492.0 528.3,488.8 530.2,485.4 531.9,481.8 533.4,477.9 534.6,473.8 535.7,469.7 536.4,465.6 536.8,461.5"; background: $rhole; border: 3px solid $orange_d; in: popin)
shape#rv.rev.edges(path: "M416.0 682.0 L782.4 782.4 L782.4 737.1 L458.7 648.5 L458.7 402.5 L416.0 390.8 ZM458.7 648.5 L782.4 737.1 L904.5 651.5 L580.8 562.8 ZM782.4 782.4 L904.5 696.8 L904.5 651.5 L782.4 737.1 ZM458.7 648.5 L580.8 562.8 L580.8 316.8 L458.7 402.5 ZM416.0 390.8 L458.7 402.5 L580.8 316.8 L538.0 305.1 Z"; background: none; border: 3px solid $orange_d; in: {opacity:0, duration:.4})
# 「寸法 = ？」の引き出し (点線 + 点 + 札)
group#qtag(in: {opacity:0, duration:.35, ease:'power3.out'}; out: {opacity:0, duration:.25, ease:'power2.in'})
  shape#l(points: "865.1,364.0 769.9,666"; background: none; border: 3px solid $orange_d; dash: 5,5)
  shape#d(left: 762px; top: 658px; width: 16px; height: 16px; border-radius: 50%; background: $orange_d)
  p#t(left: 770px; top: 300px; width: 220px; font-family: e; font-size: 30px; text-align: center; color: $orange_d; background: #FFFFFF; border: 3px solid $orange; border-radius: 14px; padding: 14px 0px) 寸法 = ？
chip#c_pc(t: "点群データ {sm}表面の位置を示す無数の点{/}"; c: $orange_d; bc: $orange)
chip#c_mesh(t: "メッシュ {sm}点を三角形の面でつないだ表面{/}"; c: $orange_d; bc: $orange)
chip#c_hard(t: "メッシュのままでは {sm}寸法を変える編集がしにくい{/}"; c: $orange_d; bc: $orange)
chip#c_cad(t: "CADモデル {sm}平面・円筒などを当てはめて作り直す{/}"; c: $orange_d; bc: $orange)
chip#c_pt(t: "ポイント：測ったまま ≠ 本来の形"; c: $orange_d; bc: $orange; font-size: 34px)
# 測った形と本来の形の 2 枚の板: 波打つ面 → まっすぐ・ゆがんだ穴 → 真円 (points の変形 + 点線の理想形 + 札の文言の差し替え)
group#worn(in: {y:24, opacity:0, duration:.6, ease:'power3.out'})
  div#lb(left: 190px; top: 316px; width: 440px; height: 430px; border-radius: 22px; background: #FFFFFF; border: 2px solid $rule)
  shape#wavy(path: "M227.0 503.5 M593.0 629.0 M230.0 510.2 L239.0 508.5 L248.0 513.5 L257.0 521.5 L266.0 524.8 L275.0 522.0 L284.0 518.8 L293.0 520.0 L302.0 522.0 L311.0 518.4 L320.0 510.6 L329.0 506.5 L338.0 509.7 L347.0 515.2 L356.0 517.2 L365.0 517.7 L374.0 522.9 L383.0 533.8 L392.0 543.5 L401.0 545.8 L410.0 544.0 L419.0 544.8 L428.0 547.7 L437.0 546.3 L446.0 538.0 L455.0 528.8 L464.0 525.8 L473.0 527.7 L482.0 527.7 L491.0 523.3 L500.0 520.3 L509.0 523.0 L518.0 527.4 L527.0 526.2 L536.0 519.0 L545.0 513.2 L554.0 513.2 L563.0 514.7 L572.0 512.0 L581.0 506.8 L590.0 506.7 L590.0 626.0 L230.0 626.0 Z"; background: #EF6A1A24; border: 4px solid $orange)
  p#ls(left: 262px; top: 352px; font-family: m; font-size: 24px; color: $sub) 測った形
  p#lh(left: 220px; top: 348px; font-size: 30px) 面
  shape#wideal(points: "216,516 604.0,516"; background: none; border: 3px solid $blue; dash: 7,7; opacity: 0)
  p#lk(cx: 410px; top: 650px; font-size: 30px; color: $orange_d) すり減り
  div#rb(left: 690px; top: 316px; width: 440px; height: 430px; border-radius: 22px; background: #FFFFFF; border: 2px solid $rule)
  p#rh(left: 720px; top: 348px; font-size: 30px) 穴
  p#rs(left: 762px; top: 352px; font-family: m; font-size: 24px; color: $sub) 測った形
  div#rplate(left: 746px; top: 411px; width: 330px; height: 260px; border-radius: 10px; background: #EF6A1A24; border: 3px solid $orange)
  shape#blob(path: "M809.2 446.0 M1021.3 636.0 M1018.3 541.0 L1013.1 561.5 L1000.3 578.4 L984.6 590.8 L969.3 600.3 L954.8 608.1 L940.3 614.4 L925.5 618.6 L910.1 620.8 L893.8 622.2 L876.0 623.2 L856.2 621.6 L836.7 614.4 L821.4 600.2 L813.4 581.0 L812.2 560.4 L814.9 541.0 L819.0 522.9 L824.7 505.7 L833.7 490.0 L846.6 477.6 L862.1 469.3 L878.1 464.0 L893.8 459.6 L910.1 456.2 L927.0 455.4 L943.9 459.0 L959.7 466.7 L974.2 476.7 L988.8 488.4 L1003.1 502.5 L1014.3 520.2 Z"; background: #FFFFFF; border: 4px solid $orange)
  shape#cideal(points: "1002.0,541.0 1000.2,558.9 994.9,576.2 986.6,592.0 975.0,606.0 961.1,617.5 945.2,626.0 927.9,631.2 910.1,633.0 892.1,631.2 874.8,626.0 858.9,617.5 844.9,606.0 833.6,592.0 825.0,576.2 819.8,558.9 817.9,541.0 819.8,523.0 825.0,505.8 833.6,489.9 844.9,476.0 858.9,464.5 874.8,456.0 892.1,450.8 910.1,449.0 927.9,450.8 945.2,456.0 961.1,464.5 975.0,476.0 986.6,489.9 994.9,505.8 1000.2,523.0"; background: none; border: 3px solid $blue; dash: 7,7; opacity: 0)
  p#rk(cx: 910px; top: 690px; font-size: 30px; color: $orange_d) ゆがみ
#worn.wavy.ok(path: "M227.0 503.5 M593.0 629.0 M230.0 516.0 L239.0 516.0 L248.0 516.0 L257.0 516.0 L266.0 516.0 L275.0 516.0 L284.0 516.0 L293.0 516.0 L302.0 516.0 L311.0 516.0 L320.0 516.0 L329.0 516.0 L338.0 516.0 L347.0 516.0 L356.0 516.0 L365.0 516.0 L374.0 516.0 L383.0 516.0 L392.0 516.0 L401.0 516.0 L410.0 516.0 L419.0 516.0 L428.0 516.0 L437.0 516.0 L446.0 516.0 L455.0 516.0 L464.0 516.0 L473.0 516.0 L482.0 516.0 L491.0 516.0 L500.0 516.0 L509.0 516.0 L518.0 516.0 L527.0 516.0 L536.0 516.0 L545.0 516.0 L554.0 516.0 L563.0 516.0 L572.0 516.0 L581.0 516.0 L590.0 516.0 L590.0 626.0 L230.0 626.0 Z"; background: #2563EB1F; border: 4px solid $blue; move: 900ms,power2.inOut)
#worn.blob.ok(path: "M809.2 446.0 M1021.3 636.0 M1002.0 541.0 L1000.2 558.9 L994.9 576.2 L986.6 592.0 L975.0 606.0 L961.1 617.5 L945.2 626.0 L927.9 631.2 L910.1 633.0 L892.1 631.2 L874.8 626.0 L858.9 617.5 L844.9 606.0 L833.6 592.0 L825.0 576.2 L819.8 558.9 L817.9 541.0 L819.8 523.0 L825.0 505.8 L833.6 489.9 L844.9 476.0 L858.9 464.5 L874.8 456.0 L892.1 450.8 L910.1 449.0 L927.9 450.8 L945.2 456.0 L961.1 464.5 L975.0 476.0 L986.6 489.9 L994.9 505.8 L1000.2 523.0 Z"; border: 4px solid $blue; move: 900ms,power2.inOut)
p#c_intent(left: 380px; top: 788px; font-size: 32px; color: $blue_d; background: #FFFFFF; border: 3px solid $blue; border-radius: 14px; padding: 10px 22px; box-shadow: 0 8px 24px #14213D1F; in: {y:16, opacity:0, duration:.55, ease:'power3.out'}) 設計の意図を読み取って、形を整える

# s5 比べる: 2 列の色の見出し → 4 行 (項目名 → 青の欄 → 橙の欄 を語ごと)
section#s5
khead#s5_head(k: "COMPARE"; t: "違いを並べると")
p#th_b(left: 460px; top: 200px; width: 650px; font-size: 38px; line-height: 1; text-align: center; color: #FFFFFF; background: $blue; border-radius: 13,13,0,0; padding: 28px 0px; in: up) 通常のCADモデリング
p#th_o(left: 1140px; top: 200px; width: 650px; font-size: 38px; line-height: 1; text-align: center; color: #FFFFFF; background: $orange; border-radius: 13,13,0,0; padding: 28px 0px; in: up) リバースモデリング
div#r(left: 130px; top: "312;456;600;744"; width: 1660px; height: 136px) ×4
  p#rl(left: 30px; cy: 50%; font-size: 34px; color: $sub; out: none; in: {x:-20, opacity:0, duration:.55, ease:'power3.out'}) 出発点;流れ;主に扱うもの;難しさ
  p#cb(left: 330px; top: 12px; width: 650px; font-size: 40px; line-height: 1.25; text-align: center; color: $blue_d; background: #FFFFFF; border-radius: 18px; padding: 32px 0px; box-shadow: 0 8px 22px #14213D14; out: none; in: up) アイデア・仕様;データ → モノ;寸法つきの形状;ゼロから考える
  p#co(left: 1010px; top: 12px; width: 650px; font-size: "41;41;41;36"; line-height: 1.25; text-align: center; color: $orange_d; background: #FFFFFF; border-radius: 18px; padding: "32,0;32,0;32,0;12,0"; box-shadow: 0 8px 22px #14213D14; out: none; in: up) 実物;モノ → データ;点群・メッシュ;測った形から[br]意図を読み取る
  div#ln(left: 0px; bottom: 0px; width: 1660px; height: 2px; background: $rule; opacity: "1;1;1;0"; out: none; in: {opacity:0, duration:.55})

# s6 使い分け: 写真つきの 2 枚の板 (こんなとき → 手法の丸札) → 両方を薄め、組み合わせの流れ図 (実物 → スキャンデータ → 改良した形) を上に重ねる
section#s6
khead#s6_head(k: "USE CASE"; t: "どちらを使う？")
card#u1(left: 130px; top: 196px; width: 800px; height: 690px; overflow: hidden; in: {y:40, opacity:0, duration:.7, ease:'power3.out'})
  img#p(left: 0px; top: 0px; width: 800px; height: 400px; main: kb {scale: [1.08, 1], ease:'power1.out'}) [photo]明るく現代的な製品デザインのオフィス、白い机の大きなモニターに青と白の機械部品のブラケットの3D CADモデル、机の上に小さな3Dプリントの試作部品とデジタルノギス、観葉植物、大きな窓から柔らかい昼の光、落ち着いて風通しのよい親しみのある雰囲気、読める文字なし
  p#q(left: 44px; top: 430px; font-family: m; font-size: 24px; color: $sub) こんなとき
  p#a(left: 44px; top: 466px; font-size: 40px; line-height: 1.3) 新しい製品を[br]一から考える
  pill#pl(left: 44px; bottom: 40px; t: "通常のCADモデリング"; c: $blue)
card#u2(left: 990px; top: 196px; width: 800px; height: 690px; overflow: hidden; in: {y:40, opacity:0, duration:.7, ease:'power3.out'})
  img#p1(left: 0px; top: 0px; width: 398px; height: 400px; content: @old; object-fit: cover; object-position: center; main: kb {scale: [1.1, 1], ease:'power1.out'})
  img#p2(left: 402px; top: 0px; width: 398px; height: 400px; main: kb {scale: [1.1, 1], ease:'power1.out'}) [photo]手で削り出した工業デザインのクレイモデル、コンパクトで現代的な車、なめらかな艶消しの暖かい灰色の粘土の面、明るいデザインスタジオの白い机の上、そばにクレイ用のヘラが数本、柔らかく均一なスタジオの光、ミニマルで清潔な背景
  p#c1(left: 14px; top: 350px; font-size: 24px; color: #FFFFFF; background: #14213DC7; border-radius: 10px; padding: 6px 16px) 図面のない部品
  p#c2(left: 416px; top: 350px; font-size: 24px; color: #FFFFFF; background: #14213DC7; border-radius: 10px; padding: 6px 16px) 手作りの試作品
  p#q(left: 44px; top: 430px; font-family: m; font-size: 24px; color: $sub) こんなとき
  p#a(left: 44px; top: 466px; font-size: 40px; line-height: 1.3) 今ある形を[br]データにしたい
  pill#pl(left: 44px; bottom: 40px; t: "リバースモデリング"; c: $orange)
card#combo(left: 260px; top: 300px; width: 1400px; height: 470px; overlap: u1,u2; in: {y:30, scale:.97, opacity:0, duration:.55, ease:'power3.out'})
  p#t(left: 50px; top: 36px; font-size: 38px) 組み合わせて使うことも多い
  div#n1(left: 60px; top: 120px; width: 230px; height: 190px; border-radius: 22px; background: $orange_tt; in: popin)
    img#p(cx: 50%; top: 30px; width: 120px; height: 90px; border-radius: 12px; content: @old; object-fit: cover; object-position: center; main: none)
    p#t(cx: 50%; top: 134px; font-size: 30px; color: $orange_d) 実物
  div#n2(left: 585px; top: 120px; width: 230px; height: 190px; border-radius: 22px; background: $orange_tt; in: popin)
    icon#i(cx: 50%; top: 33px; font-size: 64px; name: file-text; color: $orange)
    p#t(cx: 50%; top: 123px; font-size: 30px; color: $orange_d; overlap: u2.c1) スキャンデータ
  div#n3(left: 1110px; top: 120px; width: 230px; height: 190px; border-radius: 22px; background: $blue_tt; in: popin)
    icon#i(cx: 50%; top: 33px; font-size: 64px; name: cube; color: $blue)
    p#t(cx: 50%; top: 123px; font-size: 30px; color: $blue_d; overlap: u2.c2) 改良した形
  shape#a1(left: 310px; top: 200px; width: 249px; height: 30px; path: arrow_r; background: $orange; border: 8px solid $orange; in: draw {duration: 0.5})
  shape#a2(left: 836px; top: 200px; width: 249px; height: 30px; path: arrow_r; background: $blue; border: 8px solid $blue; in: draw {duration: 0.5})
  p#l1(cx: 435px; top: 345px; font-size: 28px; color: $orange_d) リバースで取り込み
  p#l2(cx: 960px; top: 345px; font-size: 28px; color: $blue_d; overlap: u2.a) CADで改良

# s7 まとめ: 2 行の式 (箱 → 矢印が描かれる → 箱 ＝ 手法名) と一言 (黄の下帯)・最後は地の色へ溶ける
section#s7
khead#s7_head(k: "SUMMARY"; t: "まとめ")
div#sm1(left: 0px; top: 300px; width: 1920px; height: 96px; display: flex; justify-content: center; align-items: center; gap: 30px; in: {y:30, opacity:0, duration:.55, ease:'power3.out'})
  p#a(font-size: 54px; background: #FFFFFF; border-radius: 22px; padding: 18px 40px; box-shadow: 0 12px 34px #14213D1A) アイデア
  shape#ar(width: 200px; height: 60px; path: arrow_r; background: $blue; border: 10px solid $blue; in: draw {duration: 0.55})
  p#b(font-size: 54px; background: #FFFFFF; border-radius: 22px; padding: 18px 40px; box-shadow: 0 12px 34px #14213D1A) 形
  p#eq(font-size: 54px) ＝ {bl}CADモデリング{/}
div#sm2(left: 0px; top: 520px; width: 1920px; height: 96px; display: flex; justify-content: center; align-items: center; gap: 30px; in: {y:30, opacity:0, duration:.55, ease:'power3.out'})
  p#a(font-size: 54px; background: #FFFFFF; border-radius: 22px; padding: 18px 40px; box-shadow: 0 12px 34px #14213D1A) 今ある形
  shape#ar(width: 200px; height: 60px; path: arrow_r; background: $orange; border: 10px solid $orange; in: draw {duration: 0.55})
  p#b(font-size: 54px; background: #FFFFFF; border-radius: 22px; padding: 18px 40px; box-shadow: 0 12px 34px #14213D1A) 設計データ
  p#eq(font-size: 54px; color: $orange) ＝ リバースモデリング
p#sm3(cx: 960px; top: 735px; font-size: 44px; color: $sub; in: {y:20, opacity:0, duration:.55, ease:'power3.out'}) 向きの違いがわかれば、{m}使い分けが見えてくる{/}
```

```timeline.txt
#v2
cast n = "落ち着いたトーンで非常にクリアで聞き取りやすい20〜30代の大人の女性のナレーター、親しみやすく丁寧で安定したテンポ" speed=108%
silence head=0ms tail=250ms
transition = dissolve {duration: .4, overlap: .2}

*** s1
[>#subtitle]
bgm music
se title +200ms
@n: [silence:1.2s]ものづくりの現場でよく聞く、[|][>#s1_cad_u][♪pop -2dB -50ms]「CADモデリング」と、[>#s1_rev_u][♪pop -2dB -50ms]「リバースモデリング」。
@: [>#s1_q +100ms]名前は似ていますが、じつは進む向きが[>#s1_ar_b -100ms][♪swish -2dB -100ms][>#s1_ar_o +50ms]正反対です。[silence:0.4s]

*** s2
se soft +100ms
@: [silence:0.5s][>#s2_l1]通常のCADモデリングは、[|]頭の中の[>#s2_n1][♪pop2 -4dB][>#s2_a1 +350ms]アイデアから[>#s2_n2][♪pop2 -4dB][>#s2_a2 +350ms]形をつくり、それが[>#s2_n3][♪pop2 -4dB][>#s2_fwd +300ms]製品になります。
@: [>#s2_l2]リバースモデリングはその[>#s2_rev]逆。すでにある[>#s2_n4][♪pop2 -4dB][>#s2_a3 +350ms]実物から[>#s2_n5][>#s2_a4 +350ms]出発して、[>#s2_n6][♪pop2 -4dB]設計データをつくります。[silence:0.4s]

*** s3
se chapter +50ms
@: [silence:0.5s][>#s3_vp +1250ms][>#s3_ptitle +1400ms][>#s3_st[*] +1450ms]まずは、通常のCADモデリングから。
@: [on #s3_st[1] $blue][>#req +150ms]出発点は「こんなものをつくりたい」という[♪pop -4dB]アイデアと、[|][>#req.l[1] -200ms][>#req.l[2] +150ms]仕様や[>#req.l[3]]寸法です。
@: [done #s3_st[1]][on #s3_st[2] $blue][<#req -150ms][♪soft -2dB][>#iso][>#iso.front +100ms]平面にスケッチを描いて[>#sk_dims -100ms]寸法を入れ、
@: [!#iso.front .iso -700ms][<#sk_dims -750ms][>#iso.top_h +50ms][>#iso.end_h +50ms][>#iso.inner_v +50ms][>#iso.top_v +50ms][!#iso.top_h .ext +80ms][!#iso.end_h .ext +80ms][!#iso.inner_v .ext +80ms][!#iso.top_v .ext +80ms][done #s3_st[2]][on #s3_st[3] $blue][♪swish -3dB]押し出しや回転といった操作で、[>#s3_chip]立体に起こしていきます。
@: [done #s3_st[3]][on #s3_st[4] $blue][>#isodim +100ms]多くのCADでは、寸法の[>#isodim.cur -800ms][!#isodim.cur to,{scale:0.82, duration:.09, yoyo:true, repeat:1} -100ms][!#isodim.tag text,"160"][♪click -2dB][!#iso.front .long +350ms][!#iso.top_h .long +350ms][!#iso.end_h .long +350ms][!#iso.inner_v .long +350ms][!#iso.top_v .long +350ms][!#isodim.l .long +350ms][!#isodim.a to,{x:-56, y:15, duration:1.1, ease:'power2.inOut'} +350ms][!#isodim.b to,{x:56, y:46, duration:1.1, ease:'power2.inOut'} +350ms][!#isodim.tag to,{y:30, duration:1.1, ease:'power2.inOut'} +350ms][!#isodim.cur main,ramp,y=20,freq_ms=1100,window=0,1100 +350ms][<#isodim.cur +1150ms]数値を変えると、[|]形もそれに合わせて更新されます。
@: [<#s3_st fade -100ms][<#s3_ptitle fade -100ms][<#isodim +100ms][>#tree][>#tree.it[1] +350ms][>#tree.it[2] +600ms][>#tree.it[3] +850ms][>#iso.ha +850ms][>#tree.it[4] +1100ms][>#iso.hb +1100ms][!#iso to,{y:-10, duration:1.7, ease:'sine.inOut', repeat:5, yoyo:true} +1400ms][♪pop2 -4dB +100ms]設計者の[>#tree.intent -100ms]意図が、寸法や作業の手順として、[|]最初からデータに残るのが特徴です。
@: できあがった3Dモデルは、[|][<#tree -450ms][>#fc1 -100ms][♪pop2 -5dB]図面や[>#fc2 -100ms][♪pop2 -5dB]試作、[>#fc3 -100ms][♪pop2 -5dB]製造へとつながります。[silence:0.4s]

*** s4
se chapter +50ms
@: [silence:0.5s][>#s4_vp +1050ms][>#s4_ptitle +1200ms][>#s4_st[*] +1250ms]続いて、リバースモデリングです。
@: [on #s4_st[1] $orange][>#ph_old -400ms]出発点は、手元にある[♪soft -2dB]実物。[||]たとえば、[|][>#stamp -100ms]図面が残っていない古い部品です。
@: [done #s4_st[1]][on #s4_st[2] $orange][<#stamp -200ms][>#ph_scan -150ms]まず、[>#scan][>#scan.bar][♪scan -3dB -100ms][<#scan.bar +2700ms]3Dスキャナーで表面の形を測ります。
@: [done #s4_st[2]][on #s4_st[3] $orange][<#ph_scan -100ms][<#ph_old -100ms][>#rv][>#rv.rev +50ms][>#rv.rev.cloud +50ms]すると、[♪data -8dB]無数の点の集まり[>#c_pc -100ms]「点群データ」が得られます。
@: [done #s4_st[3]][on #s4_st[4] $orange][<#c_pc -100ms]点どうしを[>#rv.rev.mesh -100ms][♪mesh -6dB][!#rv.rev.cloud to,{opacity:0.55, duration:.6} +1200ms]三角形の面でつなぐと、[|][>#c_mesh -100ms]「メッシュ」と呼ばれる表面のデータになります。
@: [<#c_mesh -100ms][!#rv.rev to,{scale:1.85, duration:1.3, ease:'power2.inOut', pivot:'47.2%,64.1%'} +50ms]ただ、メッシュのままでは、[|][>#qtag -150ms][♪pop -4dB][>#c_hard +100ms]寸法を変えるような編集がしにくいんです。
@: [<#qtag -150ms][<#c_hard -150ms][=#rv.rev -50ms]そこで、メッシュを下敷きに[done #s4_st[4]][on #s4_st[5] $orange][>#rv.rev.top_h -100ms][>#rv.rev.inner_v +60ms][>#rv.rev.front +220ms][>#rv.rev.end_h +380ms][>#rv.rev.top_v +540ms][<#rv.rev.cloud][!#rv.rev.mesh to,{opacity:0.35, duration:.7} +200ms]平面や[>#rv.rev.ha -100ms][>#rv.rev.hb +100ms]円筒といった形を当てはめ、[|][>#rv.rev.edges -100ms][♪emph -4dB -100ms][<#rv.rev.mesh][>#c_cad -100ms]CADで扱えるモデルに作り直します。
@: [<#c_cad -100ms][!#rv.rev to,{opacity:0.1, duration:.5}][♪soft -3dB][>#c_pt +100ms][>#worn +600ms]ポイントは、測ったままを写すのではないこと。
@: 実物には、[!#worn.lk to,{scale:1.15, duration:.2, yoyo:true, repeat:1}]すり減りや[!#worn.rk to,{scale:1.15, duration:.2, yoyo:true, repeat:1}]ゆがみがあるからです。
@: 「本来は[!#worn.wideal to,{opacity:0.9, duration:.3} -350ms][!#worn.wavy .ok][♪emph -5dB][!#worn.ls text,"本来の形" +200ms][!#worn.ls recolor,$blue +200ms][!#worn.lk text,"本来はまっすぐ" +300ms][!#worn.lk recolor,$blue_d +300ms]まっすぐな面のはず」「[!#worn.cideal to,{opacity:0.9, duration:.3} -300ms][!#worn.blob .ok +100ms][♪emph -5dB][!#worn.rs text,"本来の形" +400ms][!#worn.rs recolor,$blue +400ms][!#worn.rk text,"本来は真円" +450ms][!#worn.rk recolor,$blue_d +450ms]この穴は真円のはず」と、[|][>#c_intent -100ms]設計の意図を読み取りながら形を整えます。[silence:0.4s]

*** s5
se chapter -1dB +50ms
@: [silence:0.5s][>#th_b +200ms][>#th_o +450ms]二つの違いを並べてみましょう。
@: [>#r[1].rl -50ms][>#r[1].ln][>#r[1].cb +150ms][♪pop2 -4dB]出発点は、アイデアか、[>#r[1].co -150ms]実物か。
@: [>#r[2].rl -50ms][>#r[2].ln][>#r[2].cb +150ms][♪pop2 -4dB]流れは、データからモノへ、か、[>#r[2].co -150ms]モノからデータへ、か。
@: [>#r[3].rl -50ms][>#r[3].ln][>#r[3].cb +150ms][♪pop2 -4dB]主に扱うのは、寸法つきの形状か、[>#r[3].co -150ms]点群やメッシュか。
@: [>#r[4].rl -50ms][>#r[4].cb +150ms][♪pop2 -4dB]難しさは、ゼロから考えることと、[|][>#r[4].co -150ms]測った形から意図を読み取ることです。[silence:0.4s]

*** s6
se soft -1dB +100ms
@: [silence:0.5s][>#u1 -100ms]新しい製品を一から考えるなら、通常のCADモデリング。
@: [>#u2 -350ms][♪pop -4dB]図面のない部品の作り直しや、手作りの[♪pop -4dB]試作品のデータ化には、[|]リバースモデリングが活躍します。
@: [!#u1 to,{opacity:0.16, duration:.5} -100ms][!#u2 to,{opacity:0.16, duration:.5} -100ms][>#combo +50ms][>#combo.n1 +350ms]実際には、[>#combo.a1 -100ms][>#combo.n2 +250ms]スキャンデータをもとに[>#combo.a2 -100ms]CADで[>#combo.n3]改良するなど、[|]両方を[♪swish -3dB -100ms]組み合わせることも多いです。[silence:0.4s]

*** s7
se chapter -1dB +50ms
@: [silence:0.5s][>#sm1 -50ms][>#sm1.ar +350ms]アイデアから形をつくるのが、CADモデリング。
@: [>#sm2 -50ms][>#sm2.ar +350ms]今ある形から設計データを起こすのが、[|]リバースモデリング。
@: [>#sm3]向きの違いをつかめば、使い分けもすっきり見え[♪emph -2dB +700ms]てきます。[silence:1.6s]
fade out,1000ms
```

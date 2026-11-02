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
def chead(n, t, s, c, w) = div(left: 130px; top: 64px; width: {w}; height: 69px; delay: 250ms; in: keys(at=0 x=267 y=273 scale=1.75 opacity=0 | at=0.28 x=267 y=273 scale=1.75 opacity=1 ease=power3.out | at=0.67 x=267 y=273 scale=1.75 | at=1 ease=power3.inOut),duration=1800)
  p#n(left: 0px; bottom: 0px; font-family: e; font-size: 64px; line-height: .9; color: {c}; content: {n})
  p#t(left: 105px; bottom: 0px; font-size: 50px; line-height: 1.05; content: {t})
  p#s(left: .t.right+22; bottom: 6px; font-family: m; font-size: 24px; color: $sub; white-space: nowrap; content: {s})
# 右の工程の板 (番号の丸 + 題 + 小さな説明・灰で置いて語ごとに点灯)
def step(n, t, s, tt=15, st=43) = div(width: 550px; height: 112px; border-radius: 20px; background: #FFFFFF8C; in: {y:20, opacity:0, duration:.55, ease:'power3.out', stagger:{each:.08}})
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
shape#s2_ph(left: "463;730;997;997;730;463"; top: "217;217;217;430;430;430"; width: 150px; height: 150px; path: rect,r=0.5; background: #FFFFFF80; border: 3px solid $ph; dash: 6,6; delay: 350ms; in: {opacity:0, duration:.4, ease:'power3.out', stagger:{each:.05}}) ×6
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
chead#s3_head(n: "01"; t: "通常のCADモデリング"; s: "アイデア → 形"; c: $blue; w: 540)
card#s3_vp(left: 130px; top: 196px; width: 1060px; height: 690px; pattern: grid,23,$vgrid; in: {y:30, opacity:0, duration:.7, ease:'power3.out'})
p#s3_ptitle(left: 1245px; top: 195px; font-family: e; font-size: 20px; letter-spacing: .2em; color: $sub; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}) PROCESS
step#s3_st(left: 1240px; top: "157;244;331;417"; n: "1;2;3;4"; t: "アイデア・仕様;スケッチ＋寸法;押し出し・回転;寸法を変えれば"; s: "つくりたい形と寸法を決める;平面に輪郭を描く;立体に起こす;形もそれに合わせて更新") ×4
#s3_st.on(background: $blue_tt; border: 3px solid $blue)
# 要望の板 (電球 + 題 + 例 + 3 行の仕様・数字は欧文の青)
card#req(left: 430px; top: 346px; width: 460px; height: 310px; in: up; out: {x:40, opacity:0, duration:.35, ease:'power2.in'})
  icon#i(left: 38px; top: 32px; font-size: 50px; name: lightbulb; weight: fill; color: $bulb)
  p#h(left: 96px; top: 38px; font-size: 34px) こんな部品がほしい
  p#ex(left: 38px; top: 88px; font-family: m; font-size: 20px; color: $sub) （例）L字の取り付け金具
  p#l(left: 38px; top: "87;120;153"; font-family: m; font-size: 28px; in: {y:12, opacity:0, duration:.55, ease:'power3.out'}) ×3 ・長さ {bn}120{/} / 高さ {bn}90{/} mm;・板の厚さ {bn}14{/} mm;・ネジ穴を {bn}2{/} か所
# 等角の L 字 (群 iso: 正面 = スケッチの輪郭の変種・残り 4 面は潰れた形で出て押し出しで伸びる・穴 2 つ・群ごと上下に浮く)
group#iso
shape#iso.front(path: "M251.3,211.7 M644.5,538.0 M253.3,477.3 L541.3,477.3 L541.3,443.7 L286.9,443.7 L286.9,261.3 L253.3,261.3 Z"; background: #2563EB0F; border: 4px solid $blue; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: draw {duration: 1.7})
#iso.front.iso(path: "M251.3,211.7 M644.5,538.0 M306.7,444.0 L530.6,505.3 L530.6,477.6 L332.8,423.5 L332.8,273.2 L306.7,266.0 Z"; background: $f1; border: 3px solid $blue_d; move: 700ms,power2.inOut)
#iso.front.long(path: "M251.3,211.7 M644.5,538.0 M269.4,454.2 L567.9,536.0 L567.9,508.3 L295.5,433.7 L295.5,283.4 L269.4,276.3 Z"; move: 1100ms,power2.inOut)
shape#iso.top_h(path: "M251.3,211.7 M644.5,538.0 M332.8,423.5 L530.6,477.6 L530.6,477.6 L332.8,423.5 Z"; background: $blue_t; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.top_h.ext(path: "M251.3,211.7 M644.5,538.0 M332.8,423.5 L530.6,477.6 L605.2,425.3 L407.4,371.1 Z"; move: 1300ms,power2.inOut)
#iso.top_h.long(path: "M251.3,211.7 M644.5,538.0 M295.5,433.7 L567.9,508.3 L642.5,456.0 L370.1,381.3 Z"; move: 1100ms,power2.inOut)
shape#iso.end_h(path: "M251.3,211.7 M644.5,538.0 M530.6,505.3 L530.6,505.3 L530.6,477.6 L530.6,477.6 Z"; background: $f2; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.end_h.ext(path: "M251.3,211.7 M644.5,538.0 M530.6,505.3 L605.2,453.0 L605.2,425.3 L530.6,477.6 Z"; move: 1300ms,power2.inOut)
#iso.end_h.long(path: "M251.3,211.7 M644.5,538.0 M567.9,536.0 L642.5,483.6 L642.5,456.0 L567.9,508.3 Z"; move: 1100ms,power2.inOut)
shape#iso.inner_v(path: "M251.3,211.7 M644.5,538.0 M332.8,423.5 L332.8,423.5 L332.8,273.2 L332.8,273.2 Z"; background: $f3; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.inner_v.ext(path: "M251.3,211.7 M644.5,538.0 M332.8,423.5 L407.4,371.1 L407.4,220.8 L332.8,273.2 Z"; move: 1300ms,power2.inOut)
#iso.inner_v.long(path: "M251.3,211.7 M644.5,538.0 M295.5,433.7 L370.1,381.3 L370.1,231.1 L295.5,283.4 Z"; move: 1100ms,power2.inOut)
shape#iso.top_v(path: "M251.3,211.7 M644.5,538.0 M306.7,266.0 L332.8,273.2 L332.8,273.2 L306.7,266.0 Z"; background: $blue_t; border: 3px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: none)
#iso.top_v.ext(path: "M251.3,211.7 M644.5,538.0 M306.7,266.0 L332.8,273.2 L407.4,220.8 L381.3,213.7 Z"; move: 1300ms,power2.inOut)
#iso.top_v.long(path: "M251.3,211.7 M644.5,538.0 M269.4,276.3 L295.5,283.4 L370.1,231.1 L344.0,223.9 Z"; move: 1100ms,power2.inOut)
shape#iso.ha(points: "543.6,465.3 544.8,464.3 545.7,463.2 546.3,462.1 546.6,461.0 546.5,459.8 546.1,458.7 545.4,457.6 544.3,456.6 542.9,455.6 541.3,454.8 539.4,454.0 537.3,453.3 535.0,452.8 532.6,452.4 530.1,452.1 527.5,452.0 524.9,452.0 522.4,452.2 519.9,452.5 517.5,453.0 515.3,453.6 513.3,454.3 511.5,455.2 510.0,456.1 508.8,457.1 507.9,458.1 507.3,459.2 507.0,460.4 507.1,461.5 507.5,462.6 508.3,463.7 509.3,464.7 510.7,465.7 512.3,466.6 514.2,467.4 516.3,468.0 518.6,468.6 521.0,469.0 523.5,469.2 526.1,469.3 528.7,469.3 531.3,469.1 533.7,468.8 536.1,468.3 538.3,467.7 540.3,467.0 542.1,466.2"; background: $hole; border: 2px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: popin)
shape#iso.hb(points: "343.3,317.1 343.2,314.9 342.9,312.8 342.5,310.9 341.9,309.2 341.1,307.8 340.2,306.7 339.2,305.9 338.0,305.4 336.8,305.2 335.5,305.4 334.1,305.9 332.8,306.7 331.4,307.8 330.1,309.2 328.8,310.8 327.5,312.7 326.4,314.8 325.4,317.1 324.5,319.5 323.7,321.9 323.1,324.5 322.6,327.0 322.4,329.4 322.3,331.8 322.4,334.1 322.6,336.2 323.1,338.1 323.7,339.7 324.5,341.1 325.4,342.3 326.4,343.1 327.5,343.6 328.8,343.7 330.1,343.6 331.4,343.1 332.8,342.3 334.1,341.2 335.5,339.8 336.8,338.1 338.0,336.2 339.2,334.1 340.2,331.9 341.1,329.5 341.9,327.0 342.5,324.5 342.9,322.0 343.2,319.5"; background: $hole; border: 2px solid $blue_d; overlap: iso.front,iso.top_h,iso.end_h,iso.inner_v,iso.top_v,iso.ha,iso.hb,req,sk_dims,isodim,s3_chip; in: popin)
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
  shape#l(path: "M257.1,479.3 M559.7,575.3 M296.5,481.3 L520.3,542.6"; background: none; border: 3px solid $blue_d)
  shape#a(left: 438px; top: 716px; width: 12px; height: 12px; border-radius: 50%; background: $blue_d)
  shape#b(left: 774px; top: 808px; width: 12px; height: 12px; border-radius: 50%; background: $blue_d)
  p#tag(left: 540px; top: 780px; width: 124px; font-family: e; font-size: 30px; text-align: center; color: $blue_d; background: #FFFFFF; border: 3px solid $blue; border-radius: 14px; padding: 12px 0px) 120
  shape#cur(left: 628px; top: 814px; width: 34px; height: 48px; path: cursor; background: $ink; border: 3px solid #FFFFFF; in: {x:90, y:-60, opacity:0, duration:.6, ease:'power3.out'}; out: {opacity:0, duration:.3, ease:'power2.in'})
#isodim.l.long(path: "M257.1,479.3 M559.7,575.3 M259.1,491.5 L557.7,573.3"; move: 1100ms,power2.inOut)
# 作業の履歴の板 (右の工程と入れ替わる)・項目 4 つ + 意図の帯
card#tree(left: 1240px; top: 196px; width: 550px; height: 690px; in: up; out: {x:40, opacity:0, duration:.35, ease:'power2.in'})
  p#h(left: 36px; top: 34px; font-size: 34px) 作業の手順が残る
  p#ex(left: 36px; top: 81px; font-family: m; font-size: 21px; color: $sub) （例）履歴・フィーチャーの一覧
  div#it(left: 36px; top: "78;137;196;255"; width: 478px; height: 78px; border-radius: 16px; background: $blue_tt; in: {y:12, opacity:0, duration:.55, ease:'power3.out'}) ×4
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
chead#s4_head(n: "02"; t: "リバースモデリング"; s: "モノ → データ"; c: $orange; w: 493)
card#s4_vp(left: 130px; top: 196px; width: 1060px; height: 690px; pattern: grid,23,$vgrid; in: {y:30, opacity:0, duration:.7, ease:'power3.out'})
p#s4_ptitle(left: 1245px; top: 195px; font-family: e; font-size: 20px; letter-spacing: .2em; color: $sub; in: {y:10, opacity:0, duration:.55, ease:'power3.out'}) PROCESS
step#s4_st(left: 1240px; top: "157;237;317;397;477"; height: 104px; tt: 12; st: 39; n: "1;2;3;4;5"; t: "実物;3Dスキャン;点群データ;メッシュ;CADモデル"; s: "図面のない部品など;表面の形を測る;無数の点の集まり;三角形の面でつなぐ;平面・円筒を当てはめる") ×5
#s4_st.on(background: $orange_tt; border: 3px solid $orange)
img#ph_old(left: 130px; top: 196px; width: 1060px; height: 690px; border-radius: 26px; content: @old; in: fade {duration: 0.6}; out: fade {duration: 0.6}; main: kb {scale: [1.14, 1], ease:'power1.out'})
p#stamp(left: 770px; top: 286px; font-size: 44px; color: $orange; background: #FFFFFFDB; border: 4px solid $orange; border-radius: 14px; padding: 10px 26px; transform: rotate(-7deg); in: {scale:1.7, opacity:0, duration:.5, ease:'back.out(1.7)'}; out: {opacity:0, duration:.25, ease:'power2.in'}) 図面なし
img#ph_scan(left: 130px; top: 196px; width: 1060px; height: 690px; border-radius: 26px; in: fade {duration: 0.5}; out: fade {duration: 0.6}; main: kb {scale: [1, 1.08]}) [ref:@old]三脚に載った業務用の構造化光3Dスキャナーが、小さな丸いターンテーブルの上の同じ古い金属のL字ブラケットに細い平行な青い光の縞を投影している。明るい灰色の背景の清潔な工房、周りの光は少し落として部品の上の青い縞がくっきり見える、部品にピント
# スキャンの光の帯 (板の窓で切る群・帯は main の keys で出てから 2.8 秒かけて左から右へ走る)
group#scan(clip: 17,scan.win)
  div#win(left: 130px; top: 196px; width: 1060px; height: 690px)
  div#bar(left: -30px; top: 196px; width: 140px; height: 690px; background: linear(#3B82F600,#60A5FA8C@70%,#DBEAFEF2@92%,#3B82F600,90); mix-blend-mode: screen; bleed; border-radius: 24px; in: fade {duration: 0.15}; out: fade {duration: 0.2}; main: keys(at=0 x=0 | at=1 x=827 ease=power1.inOut),freq_ms=2800,window=0,2800,forwards)
# 点群 → メッシュ → CAD モデルの群 (外の群 rv が図の板の窓で切り、中の群 rv.rev を寄る / 戻す / 薄める)・L 字の輪郭と穴 2 つの path が scatter の clip
group#rv(clip: 17,rv.win)
div#rv.win(left: 130px; top: 196px; width: 1060px; height: 690px)
group#rv.rev
shape#rv.rev.sil(path: "M277.3,454.7 L521.6,521.6 L603.0,464.5 L603.0,434.3 L387.2,375.2 L387.2,211.2 L358.7,203.4 L277.3,260.5 Z M495.1,444.4 L497.4,442.2 L498.4,439.7 L497.8,437.3 L495.9,435.0 L492.6,432.9 L488.2,431.4 L483.1,430.3 L477.5,429.9 L471.9,430.2 L466.6,431.0 L462.1,432.5 L458.5,434.4 L456.1,436.6 L455.2,439.1 L455.7,441.5 L457.7,443.8 L461.0,445.9 L465.3,447.4 L470.5,448.5 L476.0,448.9 L481.6,448.6 L486.9,447.8 L491.5,446.3 Z M358.0,305.1 L357.6,300.3 L356.4,296.5 L354.6,293.7 L352.2,292.3 L349.5,292.3 L346.5,293.7 L343.6,296.4 L340.8,300.3 L338.4,305.1 L336.6,310.4 L335.5,315.9 L335.1,321.2 L335.5,325.9 L336.6,329.8 L338.4,332.5 L340.8,334.0 L343.6,334.0 L346.5,332.5 L349.5,329.8 L352.2,325.9 L354.6,321.2 L356.4,315.9 L357.6,310.4 Z"; background: none; border: none; opacity: 0; in: none)
shape#rv.rev.top_h(points: "305.8,432.3 521.6,491.4 603.0,434.3 387.2,375.2"; background: $orange_t; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.inner_v(points: "305.8,432.3 387.2,375.2 387.2,211.2 305.8,268.3"; background: $r3; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.front(points: "277.3,454.7 521.6,521.6 521.6,491.4 305.8,432.3 305.8,268.3 277.3,260.5"; background: $r1; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.end_h(points: "521.6,521.6 603.0,464.5 603.0,434.3 521.6,491.4"; background: $r2; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.top_v(points: "277.3,260.5 305.8,268.3 387.2,211.2 358.7,203.4"; background: $orange_t; in: {opacity:0, duration:.45, ease:'power1.out'})
shape#rv.rev.mesh(left: 410px; top: 298px; width: 501px; height: 489px; path: scatter,n=1200,seed=5,dot=3,clip=rv.rev.sil,mesh=3; background: $orange; border: 2px solid $meshc; in: wipe {dir: 'right', duration: 1.4}; out: fade {duration: 0.6})
shape#rv.rev.cloud(left: 410px; top: 298px; width: 501px; height: 489px; path: scatter,n=1200,seed=5,dot=3,clip=rv.rev.sil; background: $orange; in: wipe {dir: 'right', duration: 1.5}; out: fade {duration: 0.7})
shape#rv.rev.ha(points: "495.1,444.4 496.4,443.3 497.4,442.2 498.1,441.0 498.4,439.7 498.3,438.5 497.8,437.3 497.0,436.1 495.9,435.0 494.4,433.9 492.6,432.9 490.5,432.1 488.2,431.4 485.7,430.8 483.1,430.3 480.4,430.1 477.5,429.9 474.7,430.0 471.9,430.2 469.2,430.5 466.6,431.0 464.2,431.7 462.1,432.5 460.1,433.4 458.5,434.4 457.1,435.5 456.1,436.6 455.5,437.8 455.2,439.1 455.3,440.3 455.7,441.5 456.6,442.7 457.7,443.8 459.2,444.9 461.0,445.9 463.0,446.7 465.3,447.4 467.8,448.0 470.5,448.5 473.2,448.7 476.0,448.9 478.9,448.8 481.6,448.6 484.4,448.3 486.9,447.8 489.3,447.1 491.5,446.3 493.5,445.4"; background: $rhole; border: 3px solid $orange_d; in: popin)
shape#rv.rev.hb(points: "358.0,305.1 357.9,302.6 357.6,300.3 357.1,298.3 356.4,296.5 355.6,294.9 354.6,293.7 353.5,292.8 352.2,292.3 350.9,292.1 349.5,292.3 348.0,292.8 346.5,293.7 345.0,294.9 343.6,296.4 342.1,298.3 340.8,300.3 339.6,302.6 338.4,305.1 337.4,307.7 336.6,310.4 336.0,313.1 335.5,315.9 335.2,318.6 335.1,321.2 335.2,323.6 335.5,325.9 336.0,328.0 336.6,329.8 337.4,331.3 338.4,332.5 339.6,333.4 340.8,334.0 342.1,334.1 343.6,334.0 345.0,333.4 346.5,332.5 348.0,331.3 349.5,329.8 350.9,328.0 352.2,325.9 353.5,323.6 354.6,321.2 355.6,318.6 356.4,315.9 357.1,313.1 357.6,310.4 357.9,307.7"; background: $rhole; border: 3px solid $orange_d; in: popin)
shape#rv.rev.edges(path: "M277.3,454.7 L521.6,521.6 L521.6,491.4 L305.8,432.3 L305.8,268.3 L277.3,260.5 Z M305.8,432.3 L521.6,491.4 L603.0,434.3 L387.2,375.2 Z M521.6,521.6 L603.0,464.5 L603.0,434.3 L521.6,491.4 Z M305.8,432.3 L387.2,375.2 L387.2,211.2 L305.8,268.3 Z M277.3,260.5 L305.8,268.3 L387.2,211.2 L358.7,203.4 Z"; background: none; border: 3px solid $orange_d; in: {opacity:0, duration:.4})
# 「寸法 = ？」の引き出し (点線 + 点 + 札)
group#qtag(in: {opacity:0, duration:.35, ease:'power3.out'}; out: {opacity:0, duration:.25, ease:'power2.in'})
  shape#l(points: "576.7,242.7 513.3,444"; background: none; border: 3px solid $orange_d; dash: 5,5)
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
  shape#wavy(path: "M151.3,335.7 M395.3,419.3 M153.3,340.1 L159.3,339.0 L165.3,342.3 L171.3,347.7 L177.3,349.9 L183.3,348.0 L189.3,345.9 L195.3,346.7 L201.3,348.0 L207.3,345.6 L213.3,340.4 L219.3,337.7 L225.3,339.8 L231.3,343.5 L237.3,344.8 L243.3,345.1 L249.3,348.6 L255.3,355.9 L261.3,362.3 L267.3,363.9 L273.3,362.7 L279.3,363.2 L285.3,365.1 L291.3,364.2 L297.3,358.7 L303.3,352.5 L309.3,350.5 L315.3,351.8 L321.3,351.8 L327.3,348.9 L333.3,346.9 L339.3,348.7 L345.3,351.6 L351.3,350.8 L357.3,346.0 L363.3,342.1 L369.3,342.1 L375.3,343.1 L381.3,341.3 L387.3,337.9 L393.3,337.8 L393.3,417.3 L153.3,417.3 Z"; background: #EF6A1A24; border: 4px solid $orange)
  p#ls(left: 262px; top: 352px; font-family: m; font-size: 24px; color: $sub) 測った形
  p#lh(left: 220px; top: 348px; font-size: 30px) 面
  shape#wideal(points: "144,344 402.7,344"; background: none; border: 3px solid $blue; dash: 7,7; opacity: 0)
  p#lk(cx: 410px; top: 650px; font-size: 30px; color: $orange_d) すり減り
  div#rb(left: 690px; top: 316px; width: 440px; height: 430px; border-radius: 22px; background: #FFFFFF; border: 2px solid $rule)
  p#rh(left: 720px; top: 348px; font-size: 30px) 穴
  p#rs(left: 762px; top: 352px; font-family: m; font-size: 24px; color: $sub) 測った形
  div#rplate(left: 746px; top: 411px; width: 330px; height: 260px; border-radius: 10px; background: #EF6A1A24; border: 3px solid $orange)
  shape#blob(path: "M539.5,297.3 M680.9,424.0 M678.9,360.7 L675.4,374.3 L666.9,385.6 L656.4,393.9 L646.2,400.2 L636.5,405.4 L626.9,409.6 L617.0,412.4 L606.7,413.9 L595.9,414.8 L584.0,415.5 L570.8,414.4 L557.8,409.6 L547.6,400.1 L542.3,387.3 L541.5,373.6 L543.3,360.7 L546.0,348.6 L549.8,337.1 L555.8,326.7 L564.4,318.4 L574.7,312.9 L585.4,309.3 L595.9,306.4 L606.7,304.1 L618.0,303.6 L629.3,306.0 L639.8,311.1 L649.5,317.8 L659.2,325.6 L668.7,335.0 L676.2,346.8 Z"; background: #FFFFFF; border: 4px solid $orange)
  shape#cideal(points: "668.0,360.7 666.8,372.6 663.3,384.1 657.7,394.7 650.0,404.0 640.7,411.7 630.1,417.3 618.6,420.8 606.7,422.0 594.7,420.8 583.2,417.3 572.6,411.7 563.3,404.0 555.7,394.7 550.0,384.1 546.5,372.6 545.3,360.7 546.5,348.7 550.0,337.2 555.7,326.6 563.3,317.3 572.6,309.7 583.2,304.0 594.7,300.5 606.7,299.3 618.6,300.5 630.1,304.0 640.7,309.7 650.0,317.3 657.7,326.6 663.3,337.2 666.8,348.7"; background: none; border: 3px solid $blue; dash: 7,7; opacity: 0)
  p#rk(cx: 910px; top: 690px; font-size: 30px; color: $orange_d) ゆがみ
#worn.wavy.ok(path: "M151.3,335.7 M395.3,419.3 M153.3,344.0 L159.3,344.0 L165.3,344.0 L171.3,344.0 L177.3,344.0 L183.3,344.0 L189.3,344.0 L195.3,344.0 L201.3,344.0 L207.3,344.0 L213.3,344.0 L219.3,344.0 L225.3,344.0 L231.3,344.0 L237.3,344.0 L243.3,344.0 L249.3,344.0 L255.3,344.0 L261.3,344.0 L267.3,344.0 L273.3,344.0 L279.3,344.0 L285.3,344.0 L291.3,344.0 L297.3,344.0 L303.3,344.0 L309.3,344.0 L315.3,344.0 L321.3,344.0 L327.3,344.0 L333.3,344.0 L339.3,344.0 L345.3,344.0 L351.3,344.0 L357.3,344.0 L363.3,344.0 L369.3,344.0 L375.3,344.0 L381.3,344.0 L387.3,344.0 L393.3,344.0 L393.3,417.3 L153.3,417.3 Z"; background: #2563EB1F; border: 4px solid $blue; move: 900ms,power2.inOut)
#worn.blob.ok(path: "M539.5,297.3 M680.9,424.0 M668.0,360.7 L666.8,372.6 L663.3,384.1 L657.7,394.7 L650.0,404.0 L640.7,411.7 L630.1,417.3 L618.6,420.8 L606.7,422.0 L594.7,420.8 L583.2,417.3 L572.6,411.7 L563.3,404.0 L555.7,394.7 L550.0,384.1 L546.5,372.6 L545.3,360.7 L546.5,348.7 L550.0,337.2 L555.7,326.6 L563.3,317.3 L572.6,309.7 L583.2,304.0 L594.7,300.5 L606.7,299.3 L618.6,300.5 L630.1,304.0 L640.7,309.7 L650.0,317.3 L657.7,326.6 L663.3,337.2 L666.8,348.7 Z"; border: 4px solid $blue; move: 900ms,power2.inOut)
p#c_intent(left: 380px; top: 788px; font-size: 32px; color: $blue_d; background: #FFFFFF; border: 3px solid $blue; border-radius: 14px; padding: 10px 22px; box-shadow: 0 8px 24px #14213D1F; in: {y:16, opacity:0, duration:.55, ease:'power3.out'}) 設計の意図を読み取って、形を整える

# s5 比べる: 2 列の色の見出し → 4 行 (項目名 → 青の欄 → 橙の欄 を語ごと)
section#s5
khead#s5_head(k: "COMPARE"; t: "違いを並べると")
p#th_b(left: 460px; top: 200px; width: 650px; font-size: 38px; line-height: 1; text-align: center; color: #FFFFFF; background: $blue; border-radius: 13,13,0,0; padding: 28px 0px; in: up) 通常のCADモデリング
p#th_o(left: 1140px; top: 200px; width: 650px; font-size: 38px; line-height: 1; text-align: center; color: #FFFFFF; background: $orange; border-radius: 13,13,0,0; padding: 28px 0px; in: up) リバースモデリング
div#r(left: 130px; top: "208;304;400;496"; width: 1660px; height: 136px) ×4
  p#rl(left: 30px; cy: 50%; font-size: 34px; color: $sub; out: none; in: {x:-20, opacity:0, duration:.55, ease:'power3.out'}) 出発点;流れ;主に扱うもの;難しさ
  p#cb(left: 330px; top: 12px; width: 650px; font-size: 40px; line-height: 1.25; text-align: center; color: $blue_d; background: #FFFFFF; border-radius: 18px; padding: 32px 0px; box-shadow: 0 8px 22px #14213D14; out: none; in: up) アイデア・仕様;データ → モノ;寸法つきの形状;ゼロから考える
  p#co(left: 1010px; top: 12px; width: 650px; font-size: "27;27;27;24"; line-height: 1.25; text-align: center; color: $orange_d; background: #FFFFFF; border-radius: 18px; padding: "21,0;21,0;21,0;8,0"; box-shadow: 0 8px 22px #14213D14; out: none; in: up) 実物;モノ → データ;点群・メッシュ;測った形から[br]意図を読み取る
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
read CAD = キャド
read 3D = スリーディー
read 点群 = てんぐん
read 真円 = しんえん

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

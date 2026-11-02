# data · pet-insurance-market (hf 全力版の全量の写し — ペット保険の市場、あと何倍伸びる？・白地のコンサル資料風に題の帯と題つきの板を 8 場面で組むデータ図解) — canvas 1920x1080

見せる作り: 題の場面 (広がる淡い円と回り込む破線の輪・mask の下から上がる 2 行と「何倍」の橙の下帯・犬と猫の絵が浮かび漂う・分解の式の札が 1 つずつ)・2 場面目から常設の右上の進行 7 本・場面 = 題の帯 (番号札 + 章名・結論の 1 行・伸びる罫・出典と頁) + 題つきの板 1〜3 枚・数字の語で伸びる図 (6 本の縦棒と 2021 年の破線と 1.6 倍の矢印・左から描く前年比の折れ線・語ごとに升と記号で組む掛け算の表・頭数と収入の横棒と斜線の差・3 群の加入率の縦棒と 3 分の 1 の矢印・順位つきの横棒・数直線の点・数え上がるシナリオの棒と倍率の札・弾んで落ちる滝の棒と括弧・両向きの赤い矢印)・数字の札は最終値で出て語で数え直す・結論の 3 枚の札に語で伸びる下帯・言い終えて番号の丸が順に弾み白へ溶けて終わる・字幕は下端中央の白い札・音の層 (BGM + 場面の境の風切り + 語に結んだ効果音 41)

```design.txt
#v2
# 学ぶ作り: 白地のコンサル資料の design system を根に 1 回 (palette・書体 4・数字の run・題の帯 header の def・板 panel / card の def) → 場面は板の中身だけ
# 場面 = 上端の題の帯 (番号札 + 章名・結論の 1 行・伸びる罫・下端の出典と頁) + 題つきの板 1〜3 枚。板の中の図 (縦棒・折れ線・掛け算の表・横棒・差の破線と矢印・滝の棒) は数字の語と同時に伸びる
# 常設の層は 2 場面目から右上の進行 7 本 (場面の頭で 1 本ずつ埋まる)・場面は section の out で左へ抜け、次の場面は頭から組み上がる (切替は書かない)・最後は白へ溶けて終わる
# hf d09 pet-insurance-market (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#FFFFFF
theme light
palette ink=#14213D ink2=#3D4A5C mut=#5F6B7A hair=#DCE2EA dog=#2E6DB4 cat=#E8833A catd=#C9621C red=#C8453A gray=#B8C4D1 pale=#F3F6F9 gl=#8A96A6 grid=#EEF1F5 line2=#E3E8EF low=#9DBBE0 high=#1B3F73 lift=#8A9BB3
font "太い角ゴシック体、すっきりした現代的な印象"
fonts g="太い角ゴシック体、すっきりした現代的な印象"
fonts h="極太の角ゴシック体、すっきりした現代的な印象"
fonts m="標準の太さの角ゴシック体、すっきりした現代的な印象"
fonts n="極太の幾何学的な欧文サンセリフ体、ウェブやUIで定番のモダンな書体"
sfx off
# hf の作り: 題の帯は場面の頭に結論を数字ごと全文で出す (見出し → 図 → 台詞が数字を読む)
lint off=spoiler,all_at_once
# hf の作り: 板の目盛り・凡例・出典・頁は 11〜14 px (1080 の 17〜21 px)・図の色 (淡い地・枠・破線) は場面ごとに直書き
lint off=small_text,palette_drift
# hf の作り: 絵は題の 1 枚と犬猫の小さな icon だけ・場面は白地の板と図で組む
lint off=text_only_cut,empty_cut,blank_band,sparse_cut
prompt_tail "Minimal flat vector illustration in a clean corporate editorial style, simple geometric shapes, no outlines, subtle two-tone shading. Strictly limited palette: deep navy blue (#1E3A5F), slate blue (#2E6DB4), warm orange (#E8833A), light warm gray and cream white. No text, no letters, no logo, no background scenery."
image dog = "[transparent]A single dog (friendly mixed breed, sitting, three-quarter view) as a minimal flat vector icon. Slate blue (#2E6DB4) body with deep navy (#1E3A5F) details and a little white. The dog fills the frame from top to bottom, centered, no margin."
image cat = "[transparent]A single cat (sitting upright, three-quarter view, tail curled around paws) as a minimal flat vector icon. Warm orange (#E8833A) body with deep navy (#1E3A5F) details and a little cream white. The cat fills the frame from top to bottom, centered, no margin."
image young = "[transparent]A small puppy and a small kitten (both clearly babies, under one year old) sitting close together, curious and cute but not cartoonish. Slate blue, warm orange, deep navy and cream white. The pair fills the frame, centered."
# 文字の一部の run: 題の強調 (o 橙 / b 青の極太)・升の単位 (u / uw / uc = 0.5em)・欧文の数字 (nn hn an …)・語で伸びる下帯 (hl 題 / mk 結論)
run o { color: $catd; font-family: h }
run b { color: $dog; font-family: h }
run u { color: $mut; font-size: 0.5em; font-family: g }
run uw { color: #FFFFFFD9; font-size: 0.5em; font-family: g }
run uc { font-size: 0.5em; font-family: g }
run nn { font-family: n }
run hn { color: $ink; font-family: n; font-size: 1.36em }
run hw { color: #FFFFFF; font-family: n; font-size: 1.36em }
run an { font-family: n; font-size: 1.27em }
run pc { font-size: 0.38em }
run pc2 { font-size: 0.44em }
run sm { color: $mut; font-size: 0.6em; font-family: m }
run sm2 { font-size: 0.79em; font-family: m }
run bk { color: $ink; font-family: h }
run b9 { color: $ink; font-family: n; font-size: 1.24em }
run b7 { font-family: n; font-size: 1.33em }
run bu { font-size: 0.4em }
run cg { font-family: n; font-size: 1.18em }
run pb { color: $ink }
run em { color: $mut; font-size: 0.91em }
# hf の作り: 題の帯 (s1-hl) は字の下 1/7 の細い帯だが、run の地の形 (marker の比) は 1 式 (字幕が全 run を持つ) なので結論の mk と同じ 42% にする
run hl { color: $catd; marker: #E8833A47,42% }
run mk { color: $ink; font-family: h; marker: #E8833A52,42% }
run nr { color: $red; font-family: h }
run ao { color: $catd; font-family: n; font-size: 1.36em }
# 効果音はビジネス系の電子音 7 種を語に結んで 41 回 (自動の音は止める)
sound swoosh = "高域の空気感のある短いデジタルのシュッという音、深い残響、場面の切り替わり"
sound title = "シンセの和音と明るい高域のノイズスイープが重なる力強いタイトルの効果音"
sound soft = "ゆっくり立ち上がる柔らかく温かいサイン波の短いビジネスの効果音"
sound tick = "明るく短い電子のチャイム、わずかなディレイ、チェックリストの強調"
sound hit = "クリーンな通知のビープに低域のしっかりしたアタックが重なる中音域のビジネスのアクセント"
sound pop = "泡がはじけるような明るい電子のチャイム、上がる音程、要点の強調"
sound bell = "ゆっくり立ち上がる中音域の柔らかく温かいシンセのベルの和音、上品な締め"
motion pp { in: {scale:0.82, opacity:0, duration:0.45, ease:'back.out(1.8)'} }
p { color: $ink }
# 字幕: 下端中央の白い札 (細い縁・薄い影)・1 行で折らない・札 = 句 (2 文を 1 枚にする所は台詞の [||])
subtitle.hug(bottom: 84px; font-size: 32px; font-family: m; line-height: 1.35; color: $ink; background: #FFFFFFF7; border: 2px solid $hair; border-radius: 12px; padding: 9px 30px 10px 30px; box-shadow: 0px 6px 18px #14213D14; unit: sentence; lead: 50ms; tail: 350ms; hold: next,800ms; in: {y:8, opacity:0, duration:0.16, ease:'power2.out'}; out: {opacity:0, duration:0.08})
bgm#music(fade: 1200,3200) 落ち着いたジャズ寄りのエレクトロニカ、エレクトリックピアノとウッドベースとシンセ、控えめで知的なグルーヴ、企業のデータ解説やプレゼン向け

# 題の帯 (2 場面目から): 左上の番号札 + 章名・結論の 1 行 (語の強調は橙 o / 青 b の極太)・左から伸びる罫と太い頭・下端の出典と頁
def header(n, k, t, f, pg) = group(left: 0px; top: 0px; width: 1920px; height: 1080px)
  div#rule(left: 96px; top: 176px; width: 1728px; height: 2px; background: $hair; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
  div#rule_i(left: 96px; top: 174px; width: 150px; height: 6px; background: $ink; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
  div#kick(left: 96px; top: 33px; width: 900px; height: 33px; delay: 50ms; in: {x:-24, opacity:0, duration:0.45, ease:'power3.out'})
    p#kn(left: 0px; cy: 50%; font-size: 21px; font-family: n; color: #FFFFFF; background: $ink; border-radius: 6px; padding: 2px 10px; content: {n})
    p#kt(left: .kn.right+14; cy: 50%; font-size: 22px; letter-spacing: 0.04em; color: $dog; content: {k})
  p#ttl(left: 96px; top: 92px; font-size: 50px; line-height: 1.25; letter-spacing: 0.01em; white-space: nowrap; delay: 180ms; in: {y:22, opacity:0, duration:0.6, ease:'power3.out'}; content: {t})
  p#foot(left: 96px; top: 1036px; font-size: 16px; font-family: m; color: $mut; delay: 600ms; in: {opacity:0, duration:0.5, ease:'power3.out'}; content: {f})
  p#pg(right: 96px; top: 1034px; font-size: 18px; font-family: n; color: $mut; delay: 600ms; in: {opacity:0, duration:0.5, ease:'power3.out'}; content: {pg})
# 題つきの板: 白地・細い縁・薄い影・頭の行 (紺の小さな縦棒 + 題 + 単位) と下の罫
def panel(t, u="") = div(border-radius: 16px; background: #FFFFFF; border: 2px solid $hair; box-shadow: 0px 6px 22px #14213D0D; in: {y:20, opacity:0, duration:0.5, ease:'power3.out'})
  div#bar(left: 26px; top: 18px; width: 6px; height: 26px; border-radius: 3px; background: $ink)
  p#pt(left: 44px; cy: 32px; font-size: 26px; white-space: nowrap; content: {t})
  p#pu(left: .pt.right+12; cy: 32px; font-size: 20px; font-family: m; color: $mut; white-space: nowrap; content: {u})
  div#rule(left: 0px; top: 62px; width: 100%; height: 2px; background: $hair)
# 題の無い板 (大きい数字の札)
def card = div(border-radius: 16px; background: #FFFFFF; border: 2px solid $hair; box-shadow: 0px 6px 22px #14213D0D; in: {y:20, opacity:0, duration:0.5, ease:'power3.out'})
# 掛け算の表の升 (淡い地の角丸 + 中央の数字と小さな単位)・語で弾んで出る
def cell(v, c=$pale, tc=#14213D, bd=#FFFFFF00) = div(width: 220px; height: 104px; border-radius: 14px; background: {c}; border: 2px solid {bd}; in: {scale:0.82, opacity:0, duration:0.45, ease:'back.out(1.8)'})
  p#t(cx: 50%; cy: 50%; font-size: 44px; font-family: n; color: {tc}; white-space: nowrap; content: {v})
# 論点の箱 (題 + 補足を縦に中央寄せ)
def tbox(t, s, c=$pale, bc=$line2, tc=#14213D) = div(width: 236px; height: 150px; border-radius: 14px; background: {c}; border: 2px solid {bc}; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 8px)
  p#t(font-size: 27px; font-family: h; color: {tc}; content: {t})
  p#s(font-size: 18px; line-height: 1.35; text-align: center; font-family: m; color: $mut; content: {s})
# 結論の札: 上端の色の線 + 番号の丸 + 題 2 行 + 大きい数字 + 補足 + 罫 + 本文 (語で下帯の伸びる強調 mk)
def concl(n, h, c, big, s, b) = div(width: 560px; height: 690px; border-radius: 16px; background: #FFFFFF; border: 2px solid $hair; box-shadow: 0px 6px 22px #14213D0D; in: {y:26, opacity:0, duration:0.55, ease:'power3.out'})
  div#top(left: 0px; top: 0px; width: 560px; height: 6px; border-radius: 16px 16px 0px 0px; background: {c})
  div#bd(left: 28px; top: 28px; width: 60px; height: 60px; border-radius: 148px; background: {c})
    p#t(cx: 50%; cy: 50%; font-size: 30px; font-family: n; color: #FFFFFF; content: {n})
  p#h(left: 104px; top: 26px; width: 430px; font-size: 34px; line-height: 1.3; font-family: h; content: {h})
  p#big(left: 28px; top: 144px; font-size: 96px; line-height: 1.15; letter-spacing: -0.02em; font-family: n; color: {c}; white-space: nowrap; content: {big})
  p#s(left: 30px; top: 262px; font-size: 21px; font-family: m; color: $mut; white-space: nowrap; content: {s})
  div#r(left: 28px; top: 306px; width: 504px; height: 2px; background: $line2)
  p#b(z-index: front; left: 28px; top: 324px; width: 504px; font-size: 26px; line-height: 1.65; font-family: m; color: $ink2; content: {b})

# s1 題: 淡い青の円が広がり破線の輪が回り込む・題の 2 行は mask の下から上がり「何倍」に橙の下帯・右の円に犬と猫の絵が浮かび上下に漂う・分解の式の札が 1 つずつ・出典の札
section#s1(stagger: {each:0}; out: {x:-48, opacity:0, duration:0.3, ease:'power2.in'})
div#s1_circle(left: 1000px; top: 90px; width: 880px; height: 880px; border-radius: 1498px; background: #EEF3F9; in: {scale:0.72, opacity:0, duration:1.1, ease:'power3.out'})
shape#s1_ring(left: 960px; top: 50px; width: 960px; height: 960px; path: arc,start=0,to=360; background: none; border: 2px solid #C9D6E6; dash: 5,5; delay: 200ms; in: {scale:0.9, opacity:0, rotation:-20, duration:1.4, ease:'power2.out'})
img#s1_hero(left: 1040px; top: 190px; width: 780px; height: 668px; object-fit: contain; subject: center 90%; delay: 700ms; in: {y:46, scale:0.95, opacity:0, duration:1.0, ease:'power3.out'}) [transparent]A friendly medium-sized dog and a cat sitting side by side, facing slightly toward the viewer, calm and dignified. Both animals fill the frame from top to bottom, the dog on the left a little taller than the cat on the right.
p#s1_tag(left: 120px; top: 226px; font-size: 24px; background: #FFFFFF; border: 2px solid $ink; border-radius: 148px; padding: 8px 24px; white-space: nowrap; delay: 150ms; in: {x:-24, opacity:0, duration:0.5, ease:'power3.out'}) 国内ペット保険市場｜2036年までの市場推計
p#s1_t1(left: 120px; top: 292px; font-size: 96px; line-height: 1.3; letter-spacing: 0.01em; font-family: h; white-space: nowrap; delay: 300ms; in: {y:130, duration:0.75, ease:'power4.out', clip:true}) ペット保険の市場、
p#s1_t2(left: 120px; top: 410px; font-size: 96px; line-height: 1.3; letter-spacing: 0.01em; font-family: h; white-space: nowrap; delay: 480ms; in: {y:130, duration:0.75, ease:'power4.out', clip:true}) あと{hl}何倍{/}伸びる？
# 分解の式: 淡い札 3 枚 + 記号 + 紺の札 (左から 0.09 秒ずつ)
div#s1_eq(left: 120px; top: 586px; width: 930px; height: 66px; display: flex; gap: 14px; align-items: center; delay: 1450ms; in: {opacity:0, duration:0.05})
  p#c1(font-size: 30px; background: #F1F4F8; border: 2px solid #DFE5EC; border-radius: 12px; padding: 10px 22px; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) 飼育頭数
  p#o1(font-size: 32px; color: $gl; delay: 90ms; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) ×
  p#c2(font-size: 30px; background: #F1F4F8; border: 2px solid #DFE5EC; border-radius: 12px; padding: 10px 22px; delay: 180ms; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) 加入率
  p#o2(font-size: 32px; color: $gl; delay: 270ms; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) ×
  p#c3(font-size: 30px; background: #F1F4F8; border: 2px solid #DFE5EC; border-radius: 12px; padding: 10px 22px; delay: 360ms; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) 年間保険料
  p#o3(font-size: 32px; color: $gl; delay: 450ms; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) ＝
  p#c4(font-size: 30px; color: #FFFFFF; background: $ink; border-radius: 12px; padding: 10px 22px; delay: 540ms; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) 市場規模
div#s1_src(left: 120px; top: 700px; width: 840px; height: 36px; delay: 2200ms; in: {x:-20, opacity:0, duration:0.5, ease:'power3.out'})
  div#bar(left: 0px; top: 0px; width: 4px; height: 36px; background: $cat)
  p#t(left: 20px; cy: 50%; font-size: 26px; font-family: m; color: $ink2; white-space: nowrap) 架空の調査会社「みなとリサーチ」による推計（2026年）
# hf の作り: 下端の英字の帯は題の場面の 2.4 秒目から出て 3.3 秒で場面ごと抜ける (warn flash_text)
p#s1_foot(left: 120px; top: 1000px; font-size: 16px; letter-spacing: 0.24em; font-family: n; color: #6E7784; white-space: nowrap; delay: 2400ms; in: {opacity:0, duration:0.5, ease:'power3.out'}) PET INSURANCE MARKET OUTLOOK 2026–2036

# s2 市場の現在地: 左の板に 6 本の縦棒が順に伸び、2026 年の紺の棒・右の板に 1,014 億円が数え上がる・「1.6 倍」で 2021 年の高さの破線と橙の矢印・下の板に前年比の折れ線が左から描かれ「毎年低下」
# hf の作り: hf は場面の容器ごと右 48 px から溶けて入る — 写しは容器の入場を書かず、各要素の入場と section の out で場面を替える
section#s2(stagger: {each:0}; out: {x:-48, opacity:0, duration:0.3, ease:'power2.in'})
# 右上の進行 (sticky・2 場面目から最後まで): 灰の溝 7 本の上を場面の頭で紺が 1 本ずつ埋める
div#prog.sticky(left: 1454px; top: 60px; width: 370px; height: 6px; z-index: front; in: {opacity:0, duration:0.5})
  div#tr(left: "0;36;72;108;144;180;216"; top: 0px; width: 46px; height: 6px; border-radius: 3px; background: $line2) ×7
  div#f(left: "0;36;72;108;144;180;216"; top: 0px; width: 46px; height: 6px; border-radius: 3px; background: $ink; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'}) ×7
header#h2(n: "01"; k: "市場の現在地"; t: "市場は5年で{o}1.6倍{/}。ただし、伸び率は毎年下がっている"; f: "出典：みなとリサーチ（架空の調査会社）による国内ペット保険市場の推計（2026年）。市場規模は保険料収入ベース。"; pg: "{pb}02{/} / 08")
panel#s2pl(left: 96px; top: 206px; width: 1060px; height: 690px; t: "市場規模の推移"; u: "（保険料収入・億円）")
  div#b(left: "46.7;146.7;246.7;346.7;446.7;546.7"; top: "223.2;202.6;180.2;157.9;137.2;116"; width: 100px; height: "183.5;204.1;226.5;248.8;269.5;290.7"; border-radius: 6px 6px 0px 0px; background: "$gray;$gray;$gray;$gray;$gray;$ink"; in: {scaleY:0, duration:0.6, ease:'power3.out', pivot:'bottom', stagger:{each:0.16}}) ×6
  p#v(left: "26.7;126.7;226.7;326.7;426.7;526.7"; top: "193.9;173.2;150.9;128.5;107.9;85.4"; width: 160px; text-align: center; font-size: "19;19;19;19;19;21"; font-family: n; color: "$ink2;$ink2;$ink2;$ink2;$ink2;$ink"; in: {y:8, opacity:0, duration:0.35, ease:'power3.out', stagger:{each:0.16}}) ×6 640;712;790;868;940;1,014
  p#y(left: "26.7;126.7;226.7;326.7;426.7;526.7"; top: 622px; width: 160px; text-align: center; font-size: 21px; font-family: "m;m;m;m;m;g"; color: "$mut;$mut;$mut;$mut;$mut;$ink") ×6 2021年;2022年;2023年;2024年;2025年;2026年
  div#base(left: 40px; top: 609px; width: 950px; height: 2px; background: $ink)
  # 2021 年の高さの破線 (左から伸びる)・2026 年の棒の右に上向きの橙の矢印と「1.6倍」
  shape#ref(left: 70px; top: 333px; width: 880px; height: 3px; path: line_h; border: 3px solid #94A2B3; dash: 4,3; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'})
  shape#arw(left: 930px; top: 162px; width: 39px; height: 172px; path: arrow_u; background: $cat; border: 4px solid $cat; in: {y:20, opacity:0, duration:0.4, ease:'power3.out'})
  p#x16(left: 958px; top: 228px; font-size: 34px; font-family: h; color: $catd; white-space: nowrap; in: pp) {nn}1.6{/}倍
  div#cagr(left: 70px; top: 84px; width: 228px; height: 46px; background: #FFFFFF; border: 2px solid $ink; border-radius: 148px; in: {x:-16, opacity:0, duration:0.45, ease:'power3.out'})
    icon#i(left: 16px; cy: 50%; font-size: 24px; name: arrow-up-right; weight: bold; color: $dog)
    p#t(left: 48px; cy: 50%; font-size: 22px; white-space: nowrap) 年平均 {cg}+9.6%{/}
card#s2kpi(left: 1190px; top: 206px; width: 634px; height: 300px)
  div#edge(left: 0px; top: 0px; width: 8px; height: 300px; border-radius: 16px 0px 0px 16px; background: $ink)
  p#l(left: 34px; top: 22px; font-size: 24px; font-family: m; color: $mut; white-space: nowrap) 2026年の市場規模（保険料収入）
  p#n(left: 28px; top: 69px; font-size: 140px; line-height: 1.1; letter-spacing: -0.02em; font-family: n) [count:1,014 start=0 ms=1000ms delay=200ms]
  p#u(left: .n.right+10; top: 152px; font-size: 50px) 億円
  p#chip(left: 34px; top: 236px; font-size: 30px; color: #FFFFFF; background: $ink; border-radius: 12px; padding: 9px 22px; white-space: nowrap; in: pp) 5年前（2021年）の {cg}1.6{/} 倍
panel#s2yoy(left: 1190px; top: 525px; width: 634px; height: 370px; t: "前年比の伸び率"; u: "（%）")
  div#g(left: 40px; top: "111;155;200"; width: 560px; height: 2px; background: $grid) ×3
  p#gl(left: 6px; top: "102;147;191"; width: 33px; text-align: right; font-size: 16px; font-family: n; color: $gl) ×3 10;8;6
  # 折れ線は 11.3% の語から 7.9% の語の後まで 1.95 秒で左から描き、点と値は線の到着に合わせて出る
  shape#line(path: "M53.3 82.2 L133.3 88.9 L213.3 113.3 L293.3 148.8 L373.3 157.7"; background: none; border: 5px solid $red; in: draw {duration: 1.95})
  shape#d(left: "47.3;127.3;207.3;287.3;367.3"; top: "76.2;82.9;107.3;142.8;151.7"; width: 18px; height: 18px; border-radius: 50%; background: #FFFFFF; border: 4px solid $red; in: {scale:0.82, opacity:0, duration:0.3, ease:'back.out(1.8)'}) ×5
  p#v(left: "13.3;93.3;173.3;253.3;333.3"; top: "50.2;56.9;81.3;116.8;125.7"; width: 120px; text-align: center; font-size: 22px; font-family: n; color: $ink2; in: {y:8, opacity:0, duration:0.3, ease:'power3.out'}) ×5 11.3%;11.0%;9.9%;8.3%;7.9%
  p#x(left: "13.3;93.3;173.3;253.3;333.3"; top: 318px; width: 120px; text-align: center; font-size: 21px; font-family: n; color: $mut) ×5 2022;2023;2024;2025;2026
  p#down(left: 400px; top: 76px; font-size: 22px; color: $red; background: #FBECEA; border: 2px solid #F0C9C4; border-radius: 148px; padding: 6px 18px; white-space: nowrap; in: pp) ▼ 毎年低下

# s3 市場の分解: 列の題が分解の語で出て、犬・猫の行を語ごとに升 → 記号 → 升と組み、合計の行と点線の矢印・下の 2 枚の板で頭数と収入の横棒を比べ (猫の頭数の差は斜線・+220 万頭)、「半分」で中央の破線と札
# hf の作り: 題の帯だけを頭に置き、表は分解の語から組み始める (warn cut_head_gap)
section#s3(stagger: {each:0}; out: {x:-48, opacity:0, duration:0.3, ease:'power2.in'})
header#h3(n: "02"; k: "市場の分解（2026年）"; t: "猫は犬より220万頭多いのに、市場は{o}犬の半分{/}"; f: "出典：みなとリサーチ（架空の調査会社）による国内ペット保険市場の推計（2026年）。加入率＝加入頭数÷飼育頭数。"; pg: "{pb}03{/} / 08")
p#s3h(left: "210.7;394.7;552;736;920;1106.7"; top: 208px; width: "146.7;120;146.7;146.7;173.3;109.3"; text-align: center; font-size: 22px; color: $mut; in: {y:10, opacity:0, duration:0.4, ease:'power3.out'}) ×6 飼育頭数;加入率;加入頭数;年間保険料;保険料収入;構成比
img#s3dogi(left: 99px; top: 258px; width: 88px; height: 88px; content: @dog; object-fit: contain; in: {scale:0.8, opacity:0, duration:0.45, ease:'power3.out'})
p#s3dogl(left: 200px; cy: 302px; font-size: 38px; font-family: h; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 犬
cell#s3dog(left: "210.7;394.7;552;736;920;1106.7"; top: 250px; width: "146.7;120;146.7;146.7;173.3;109.3"; v: "680{u}万頭{/};19{u}%{/};129.2{u}万頭{/};52,000{u}円{/};672{uw}億円{/};66{uc}%{/}"; c: "$pale;$pale;$pale;$pale;$dog;#FFFFFF"; tc: "$ink;$ink;$ink;$ink;#FFFFFF;$dog"; bd: "#FFFFFF00;#FFFFFF00;#FFFFFF00;#FFFFFF00;#FFFFFF00;$hair") ×6
  p#t(font-size: "29;29;29;29;32;29")
p#s3dop(left: "357.3;514.7;698.7;882.7"; cy: 302px; width: 56px; text-align: center; font-size: 38px; color: $gl; in: {opacity:0, duration:0.3, ease:'power3.out'}) ×4 ×;＝;×;＝
img#s3cati(left: 105px; top: 376px; width: 88px; height: 88px; content: @cat; object-fit: contain; in: {scale:0.8, opacity:0, duration:0.45, ease:'power3.out'})
p#s3catl(left: 200px; cy: 420px; font-size: 38px; font-family: h; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 猫
cell#s3cat(left: "210.7;394.7;552;736;920;1106.7"; top: 368px; width: "146.7;120;146.7;146.7;173.3;109.3"; v: "900{u}万頭{/};10{u}%{/};90{u}万頭{/};38,000{u}円{/};342{uw}億円{/};34{uc}%{/}"; c: "$pale;$pale;$pale;$pale;$catd;#FFFFFF"; tc: "$ink;$ink;$ink;$ink;#FFFFFF;$catd"; bd: "#FFFFFF00;#FFFFFF00;#FFFFFF00;#FFFFFF00;#FFFFFF00;$hair") ×6
  p#t(font-size: "29;29;29;29;32;29")
p#s3cop(left: "357.3;514.7;698.7;882.7"; cy: 420px; width: 56px; text-align: center; font-size: 38px; color: $gl; in: {opacity:0, duration:0.3, ease:'power3.out'}) ×4 ×;＝;×;＝
# 合計の行 (年間保険料の升は無く、点線の矢印が保険料収入の升へ)・升 → 記号 → 矢印の順に 0.07 秒ずつ下から
p#s3totl(left: 110px; cy: 532px; font-size: 32px; font-family: h; in: {x:-12, opacity:0, duration:0.4, ease:'power3.out'}) 合計
cell#s3tot(left: "210.7;394.7;552;920;1106.7"; top: 486px; width: "146.7;120;146.7;173.3;109.3"; height: 92px; v: "1,580{u}万頭{/};13.9{u}%{/};219{u}万頭{/};1,014{uw}億円{/};100{uc}%{/}"; c: "$pale;$pale;$pale;$ink;#FFFFFF"; tc: "$ink;$ink;$ink;#FFFFFF;$ink"; bd: "#FFFFFF00;#FFFFFF00;#FFFFFF00;#FFFFFF00;$hair"; in: {y:10, opacity:0, duration:0.35, ease:'power3.out'}) ×5
  p#t(font-size: "29;29;29;32;29")
p#s3top(left: "357.3;514.7"; cy: 532px; width: 56px; text-align: center; font-size: 38px; color: $gl; in: {y:10, opacity:0, duration:0.35, ease:'power3.out'}) ×2 ×;＝
shape#s3tarw(left: 1066px; top: 524px; width: 294px; height: 18px; path: arrow_r,head=fill; background: $gl; border: 3px solid $gl; dash: 5,5; in: {y:10, opacity:0, duration:0.35, ease:'power3.out'})
panel#s3pa(left: 96px; top: 606px; width: 846px; height: 290px; t: "飼育頭数"; u: "（万頭）")
  p#ld(left: 26px; top: 96px; font-size: 26px; font-family: h) 犬
  p#lc(left: 26px; top: 170px; font-size: 26px; font-family: h) 猫
  div#bd(left: 90px; top: 92px; width: 423px; height: 46px; border-radius: 0px 6px 6px 0px; background: $dog; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  div#bc(left: 90px; top: 166px; width: 560px; height: 46px; border-radius: 0px 6px 6px 0px; background: $cat; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  p#vd(left: 526px; top: 99px; font-size: 22px; color: $ink2; white-space: nowrap; in: {opacity:0, duration:0.3, ease:'power3.out'}) {hn}680{/}万頭
  p#vc(left: 664px; top: 172px; font-size: 22px; color: $ink2; white-space: nowrap; in: {opacity:0, duration:0.3, ease:'power3.out'}) {hn}900{/}万頭
  # 犬より多い 220 万頭の分は白の斜線を重ねる (CSS の 135deg の縞 = hatch 45)
  div#ex(left: 513px; top: 166px; width: 136px; height: 46px; border-radius: 0px 6px 6px 0px; pattern: hatch,45,#FFFFFF61,9,4; in: {opacity:0, duration:0.4, ease:'power3.out'})
  shape#dl(left: 512px; top: 84px; width: 3px; height: 140px; path: line_v; border: 3px solid $gl; dash: 4,3; in: {opacity:0, duration:0.3, ease:'power3.out'})
  p#plus(left: 494px; top: 224px; font-size: 22px; color: $catd; white-space: nowrap; in: pp) {an}+220{/}万頭
panel#s3pb(left: 978px; top: 606px; width: 846px; height: 290px; t: "保険料収入"; u: "（億円）")
  p#ld(left: 26px; top: 96px; font-size: 26px; font-family: h) 犬
  p#lc(left: 26px; top: 170px; font-size: 26px; font-family: h) 猫
  div#bd(left: 90px; top: 92px; width: 560px; height: 46px; border-radius: 0px 6px 6px 0px; background: $dog; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  div#bc(left: 90px; top: 166px; width: 285px; height: 46px; border-radius: 0px 6px 6px 0px; background: $cat; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#vd(left: 460px; top: 99px; width: 180px; text-align: right; font-size: 22px; color: #FFFFFFE6; white-space: nowrap; in: {opacity:0, duration:0.3, ease:'power3.out'}) {hw}672{/}億円
  p#vc(left: 388px; top: 172px; font-size: 22px; color: $ink2; white-space: nowrap; in: {opacity:0, duration:0.3, ease:'power3.out'}) {hn}342{/}億円
  shape#dl(left: 369px; top: 84px; width: 3px; height: 140px; path: line_v; border: 3px solid $gl; dash: 4,3; in: {opacity:0, duration:0.3, ease:'power3.out'})
  p#half(left: 525px; top: 170px; font-size: 22px; color: #FFFFFF; background: $catd; border-radius: 148px; padding: 6px 18px; white-space: nowrap; in: pp) 犬の半分

# s4 欧州との比較: 3 群の犬・猫の縦棒を群の語で伸ばし、国内の群に淡い橙の帯・右の札に猫の icon と 10% が数え上がる・「3分の1」で北欧の猫の高さの橙の破線と下向きの矢印と札
section#s4(stagger: {each:0}; out: {x:-48, opacity:0, duration:0.3, ease:'power2.in'})
header#h4(n: "03"; k: "欧州の先行市場との比較（加入率）"; t: "国内の猫の加入率は10%。北欧の{o}3分の1{/}にとどまる"; f: "出典：みなとリサーチ（架空の調査会社）による国内ペット保険市場の推計（2026年）。加入率は飼育頭数に対する加入頭数の割合。"; pg: "{pb}04{/} / 08")
panel#s4pl(left: 96px; top: 206px; width: 1110px; height: 690px; t: "犬・猫の加入率"; u: "（%）")
  div#lg1(left: 972px; top: 22px; width: 18px; height: 18px; border-radius: 4px; background: $dog)
  p#lt1(left: 998px; cy: 32px; font-size: 20px; color: $ink2) 犬
  div#lg2(left: 1040px; top: 22px; width: 18px; height: 18px; border-radius: 4px; background: $cat)
  p#lt2(left: 1065px; cy: 32px; font-size: 20px; color: $ink2) 猫
  div#band(left: 740px; top: 76px; width: 320px; height: 584px; border-radius: 14px; background: #FFF5EC; in: {opacity:0, duration:0.4, ease:'power3.out'})
  div#g(left: 70px; top: "340;286.7;233.3;180;126.7"; width: 1010px; height: 2px; background: $grid) ×5
  p#gl(left: 14px; top: "331.3;278;224.7;171.3;118"; width: 50px; text-align: right; font-size: 16px; font-family: n; color: $gl) ×5 10%;20%;30%;40%;50%
  div#d(left: "118.7;318.7;518.7"; top: "116;233.3;292"; width: 114px; height: "277.3;160;101.3"; border-radius: 6px 6px 0px 0px; background: $dog; in: {scaleY:0, duration:0.6, ease:'power3.out', pivot:'bottom'}) ×3
  div#c(left: "205.3;405.3;605.3"; top: "228;292;340"; width: 114px; height: "165.3;101.3;53.3"; border-radius: 6px 6px 0px 0px; background: $cat; in: {scaleY:0, duration:0.6, ease:'power3.out', pivot:'bottom'}) ×3
  # 西欧の犬 30% の値は橙の破線が横切るので白の地を敷く
  p#dv(left: "110;310;510"; top: "86.7;204;262.7"; width: 140px; text-align: center; font-size: 28px; font-family: n; color: $ink2; background: "none;#FFFFFF;none"; in: {y:8, opacity:0, duration:0.35, ease:'power3.out'}) ×3 52%;30%;19%
  p#cv(left: "196.7;396.7;596.7"; top: "198.7;262.7;309.3"; width: 140px; text-align: center; font-size: "19;19;21"; font-family: n; color: "$ink2;$ink2;$catd"; in: {y:8, opacity:0, duration:0.35, ease:'power3.out'}) ×3 31%;19%;10%
  p#gn(left: "93.3;293.3;493.3"; top: 604px; width: 320px; text-align: center; font-size: "16;16;19"; font-family: "g;g;h"; color: "$ink2;$ink2;$catd"; in: {y:8, opacity:0, duration:0.4, ease:'power3.out'}) ×3 北欧の先行市場;西欧の大市場;国内
  div#base(left: 70px; top: 590px; width: 1010px; height: 2px; background: $ink)
  shape#ref(left: 308px; top: 340px; width: 760px; height: 3px; path: line_h; border: 3px solid $cat; dash: 4,3; in: {scaleX:0, duration:0.5, ease:'power2.out', pivot:'left'})
  shape#arw(left: 1041px; top: 345px; width: 39px; height: 165px; path: arrow_d; background: $cat; border: 4px solid $cat; in: {y:-14, opacity:0, duration:0.35, ease:'power3.out'})
  p#third(left: 760px; top: 272px; font-size: 26px; color: #FFFFFF; background: $catd; border-radius: 148px; padding: 8px 22px; white-space: nowrap; in: pp) 北欧の {nn}3分の1{/}
card#s4card(left: 1240px; top: 206px; width: 584px; height: 690px)
  img#cat(left: 188px; top: 34px; width: 210px; height: 210px; content: @cat; object-fit: contain)
  p#l(left: 0px; top: 258px; width: 584px; text-align: center; font-size: 26px; color: $mut) 国内の猫の加入率
  p#n(left: 0px; top: 318px; width: 584px; text-align: center; font-size: 170px; line-height: 1; letter-spacing: -0.03em; font-family: n; color: $catd) 10{pc}%{/}
  p#s(left: 0px; top: 506px; width: 584px; text-align: center; font-size: 26px; font-family: m; color: $ink2) 北欧の先行市場（{nn}31%{/}）の
  p#b(left: 0px; top: 546px; width: 584px; text-align: center; font-size: 66px; line-height: 1.2; font-family: h; color: $catd) 3分の1
  div#fl(left: 40px; top: 638px; width: 504px; height: 2px; background: $hair)
  p#f(left: 40px; top: 651px; width: 504px; text-align: center; font-size: 21px; font-family: m; color: $mut) 犬も 北欧 {nn}52%{/} に対し 国内 {nn}19%{/}
#s4card.n.cnt(content: "[count:10 start=0 ms=600ms]{pc}%{/}")

# s5 ためらう理由: 左の板に順位の丸と 5 本の横棒 (1 位だけ紺)・「41%」で 1 位が脈打つ・右に 3 枚の札を語ごとに (室内飼いの 2 本の棒と絵・47% と保険料の数直線の点・68% と子犬子猫の絵)
section#s5(stagger: {each:0}; out: {x:-48, opacity:0, duration:0.3, ease:'power2.in'})
header#h5(n: "04"; k: "加入をためらう理由"; t: "ためらう理由の1位は{b}保険料{/}。月2,000円以下なら{o}47%{/}が検討"; f: "出典：みなとリサーチ（架空）による未加入の飼い主 2,000人への調査（複数回答）。平均保険料は月額。"; pg: "{pb}05{/} / 08")
panel#s5pl(left: 96px; top: 206px; width: 900px; height: 690px; t: "加入をためらう理由"; u: "（複数回答・%）")
  p#rk(left: 22px; top: "69.3;141.3;213.3;285.3;357.3"; width: 36px; text-align: center; font-size: 20px; line-height: 1.4; font-family: n; color: "#FFFFFF;$ink2;$ink2;$ink2;$ink2"; background: "$ink;#E9EDF2;#E9EDF2;#E9EDF2;#E9EDF2"; border-radius: 148px; padding: 4px 0px) ×5 1;2;3;4;5
  p#rl(left: 66px; top: "70;142;214;286;358"; width: 300px; text-align: right; font-size: 24px; font-family: "h;m;m;m;m"; color: "$ink;$ink2;$ink2;$ink2;$ink2"; white-space: nowrap; in: {y:8, opacity:0, duration:0.35, ease:'power3.out', stagger:{each:0.12}}) ×5 保険料が高い;元が取れるか分からない;若くて健康だから不要;補償内容が分かりにくい;年齢・持病で入れない
  div#rb(left: 380px; top: "64;136;208;280;352"; width: "257;207;176;138;75"; height: 52px; border-radius: 0px 6px 6px 0px; background: "$ink;$gray;$gray;$gray;$gray"; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left', stagger:{each:0.12}}) ×5
  p#rv(left: "520;470;439;401;338"; top: "65;140;212;284;356"; font-size: "24;20;20;20;20"; font-family: n; color: "$ink;$ink2;$ink2;$ink2;$ink2"; white-space: nowrap; in: {y:6, opacity:0, duration:0.3, ease:'power3.out', stagger:{each:0.12}}) ×5 41%;33%;28%;22%;12%
  p#nt(left: 26px; top: 640px; font-size: 20px; font-family: m; color: $mut; white-space: nowrap) 未加入の飼い主 2,000人への調査（複数回答）
card#s5ca(left: 1030px; top: 206px; width: 794px; height: 214px)
  p#t(left: 26px; top: 18px; font-size: 24px; white-space: nowrap) 「室内飼いだから不要」と答えた割合
  p#l1(left: 26px; cy: 92px; font-size: 21px; color: $ink2) 猫の飼い主
  p#l2(left: 26px; cy: 150px; font-size: 21px; color: $ink2) 犬の飼い主
  div#bc(left: 160px; top: 72px; width: 266px; height: 40px; border-radius: 0px 6px 6px 0px; background: $cat; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  div#bd(left: 160px; top: 130px; width: 63px; height: 40px; border-radius: 0px 6px 6px 0px; background: $dog; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#vc(left: 438px; cy: 92px; font-size: 30px; font-family: n; color: $catd; in: {opacity:0, duration:0.3, ease:'power3.out'}) 38%
  p#vd(left: 236px; cy: 150px; font-size: 30px; font-family: n; color: $dog; in: {opacity:0, duration:0.3, ease:'power3.out'}) 9%
  img#ic(left: 548px; top: 30px; width: 226px; height: 154px; object-fit: contain) [transparent]A relaxed cat lying on a cushion beside a simple window frame and a small potted plant, cozy indoor feeling. Warm orange cat, deep navy and light gray window and cushion, a touch of muted green for the plant. Isolated objects that fill the frame, no wall or floor.
card#s5cb(left: 1030px; top: 442px; width: 794px; height: 214px)
  p#t(left: 26px; top: 18px; font-size: 24px; white-space: nowrap) 月2,000円以下なら加入を検討
  p#n(left: 22px; top: 64px; font-size: 100px; line-height: 1; letter-spacing: -0.02em; font-family: n) 47{pc2}%{/}
  # 月額の数直線 (0〜5,000 円・目盛り 1,000 / 3,000 / 4,000)・2,000 円の検討ラインの破線と札・猫と犬の今の平均の点
  div#ax(left: 330px; top: 150px; width: 440px; height: 3px; background: #C9D2DC)
  div#tk(left: "278.7;396;454.7"; top: 145px; width: 2px; height: 13px; background: #C9D2DC) ×3
  shape#th(left: 506px; top: 78px; width: 3px; height: 74px; path: line_v; border: 3px solid $ink; dash: 4,3; in: {opacity:0, duration:0.3, ease:'power3.out'})
  p#thl(left: 396px; top: 50px; width: 220px; text-align: center; font-size: 20px; white-space: nowrap; in: {y:8, opacity:0, duration:0.35, ease:'power3.out'}) 検討ライン 月{nn}2,000{/}円
  div#pc(left: 602px; top: 141px; width: 20px; height: 20px; border-radius: 148px; background: $cat; border: 3px solid #FFFFFF; box-shadow: 0px 0px 0px 2px #14213D40; in: pp)
  p#pcl(left: 531px; top: 96px; width: 160px; text-align: center; font-size: 18px; color: #B4561A; white-space: nowrap; in: {y:6, opacity:0, duration:0.3, ease:'power3.out'}) 猫 月約{nn}3,200{/}円
  div#pd(left: 699px; top: 141px; width: 20px; height: 20px; border-radius: 148px; background: $dog; border: 3px solid #FFFFFF; box-shadow: 0px 0px 0px 2px #14213D40; in: pp)
  p#pdl(left: 628px; top: 168px; width: 160px; text-align: center; font-size: 18px; color: $dog; white-space: nowrap; in: {y:-6, opacity:0, duration:0.3, ease:'power3.out'}) 犬 月約{nn}4,300{/}円
# hf の作り: 札の数字は先に最終値で出て、数字の語で 0 から数え直す (変種 .cnt の content が数える数字)
#s5cb.n.cnt(content: "[count:47 start=0 ms=800ms]{pc2}%{/}")
card#s5cc(left: 1030px; top: 681px; width: 794px; height: 214px)
  p#t(left: 26px; top: 18px; font-size: 24px; white-space: nowrap) 加入のタイミング
  p#n(left: 22px; top: 64px; font-size: 100px; line-height: 1; letter-spacing: -0.02em; font-family: n) 68{pc2}%{/}
  p#c1(left: 236px; top: 78px; font-size: 26px; line-height: 1.4; font-family: m; color: $ink2; white-space: nowrap) の加入者は[br]{bk}1歳未満{/}で加入
  p#c2(left: 26px; top: 170px; font-size: 21px; font-family: m; color: $mut; white-space: nowrap; in: {y:8, opacity:0, duration:0.4, ease:'power3.out'}) 3歳を過ぎてからの新規加入は {b9}9%{/}
  img#yp(left: 578px; top: 22px; width: 213px; height: 178px; content: @young; object-fit: contain)
#s5cc.n.cnt(content: "[count:68 start=0 ms=800ms]{pc2}%{/}")

# s6 3 つのシナリオ: 上の帯に共通の前提 (犬猫の icon + 頭数)・4 本の縦棒をシナリオの語で伸ばし金額を数え上げ倍率の札 (中位だけ橙)・下の 2 行の表・右の板で高位と北欧の加入率を横棒で並べ「まだ届かない」
section#s6(stagger: {each:0}; out: {x:-48, opacity:0, duration:0.3, ease:'power2.in'})
header#h6(n: "05"; k: "2036年の3つのシナリオ"; t: "2036年の市場は1.2〜2.9倍。中位で{o}約1,900億円{/}"; f: "出典：みなとリサーチ（架空の調査会社）による国内ペット保険市場の推計（2026年）。シナリオ別の加入率・保険料の変化を置いた試算。"; pg: "{pb}06{/} / 08")
# hf の作り: 前提の帯の犬猫の icon は右の板の icon と同じ絵 (warn duplicate_media)
div#s6asm(left: 96px; top: 200px; width: 1728px; height: 66px; border-radius: 14px; background: $pale; border: 2px solid $line2; in: {y:14, opacity:0, duration:0.5, ease:'power3.out'})
  p#l(left: 28px; cy: 50%; font-size: 22px; white-space: nowrap) 共通の前提｜2036年の飼育頭数
  img#di(left: 400px; cy: 50%; width: 46px; height: 46px; content: @dog; object-fit: contain)
  p#dt(left: .di.right+10; cy: 50%; font-size: 22px; font-family: m; color: $ink2; white-space: nowrap) 犬 {hn}610{/}万頭{em}（減少）{/}
  img#ci(left: 699px; cy: 50%; width: 46px; height: 46px; content: @cat; object-fit: contain)
  p#ct(left: .ci.right+10; cy: 50%; font-size: 22px; font-family: m; color: $ink2; white-space: nowrap) 猫 {hn}930{/}万頭{em}（微増）{/}
panel#s6pl(left: 96px; top: 286px; width: 1160px; height: 610px; t: "保険料収入"; u: "（億円）")
  div#b(left: "150;310;470;630"; top: "226.4;214.4;175.3;112"; width: 150px; height: "58.9;70.9;110;173.3"; border-radius: 6px 6px 0px 0px; background: "$gray;$low;$dog;$high"; in: {scaleY:0, duration:0.75, ease:'power3.out', pivot:'bottom'}) ×4
  p#v(left: "126.7;286.7;446.7;606.7"; top: "191.8;179.8;140.7;77.3"; width: 220px; text-align: center; font-size: 40px; font-family: n; white-space: nowrap; in: {y:8, opacity:0, duration:0.3, ease:'power3.out'}) ×4 1,014{sm}億円{/};[count:1,221 start=0 ms=900ms]{sm}億円{/};[count:1,894 start=0 ms=900ms]{sm}億円{/};[count:2,985 start=0 ms=900ms]{sm}億円{/}
  p#m(left: "320;480;640"; top: "150.5;111.3;48"; width: 120px; text-align: center; font-size: 24px; font-family: n; color: "$dog;#FFFFFF;$dog"; background: "#EAF1FA;$catd;#EAF1FA"; border-radius: 148px; padding: 3px 0px; in: pp) ×3 ×1.2;×1.9;×2.9
  p#sn(left: "126.7;286.7;446.7;606.7"; top: 438px; width: 220px; text-align: center; font-size: 27px; line-height: 1.1; font-family: h; color: "$ink;$ink;$catd;$ink"; in: {y:8, opacity:0, duration:0.35, ease:'power3.out'}) ×4 2026年;低位[br]{sm}2036年{/};中位[br]{sm}2036年{/};高位[br]{sm}2036年{/}
  p#r(left: "126.7;286.7;446.7;606.7"; top: 507px; width: 220px; text-align: center; font-size: 22px; font-family: n; color: $ink2; in: {y:6, opacity:0, duration:0.3, ease:'power3.out'}) ×4 19%／10%;24%／13%;32%／20%;45%／30%
  p#p(left: "126.7;286.7;446.7;606.7"; top: 554px; width: 220px; text-align: center; font-size: 22px; font-family: n; color: $ink2; in: {y:6, opacity:0, duration:0.3, ease:'power3.out'}) ×4 基準;据え置き;+10%;+20%
  div#base(left: 40px; top: 428px; width: 1090px; height: 2px; background: $ink)
  div#rl(left: 24px; top: "330.7;362.7"; width: 1110px; height: 2px; background: $line2) ×2
  p#tr1(left: 24px; top: 508px; width: 170px; font-size: 20px; color: $mut; white-space: nowrap) 加入率 {sm2}犬／猫{/}
  p#tr2(left: 24px; top: 556px; width: 170px; font-size: 20px; color: $mut; white-space: nowrap) 年間保険料
panel#s6cmp(left: 1290px; top: 286px; width: 534px; height: 610px; t: "高位シナリオの加入率"; u: "（%）")
  img#di(left: 12px; top: 98px; width: 96px; height: 96px; content: @dog; object-fit: contain)
  p#dn(left: 26px; top: 200px; width: 80px; text-align: center; font-size: 26px; font-family: h) 犬
  img#ci(left: 4px; top: 288px; width: 96px; height: 96px; content: @cat; object-fit: contain)
  p#cn(left: 26px; top: 390px; width: 80px; text-align: center; font-size: 26px; font-family: h) 猫
  div#da(left: 120px; top: 126px; width: 270px; height: 34px; border-radius: 0px 6px 6px 0px; background: $dog; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  p#dav(left: 400px; cy: 143px; font-size: 26px; font-family: n; in: {opacity:0, duration:0.3, ease:'power3.out'}) 45%
  div#db(left: 120px; top: 202px; width: 312px; height: 34px; border-radius: 0px 6px 6px 0px; background: #C3CCD6; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  p#l(left: 120px; top: "64;114.7;190.7;241.3"; font-size: 18px; color: $mut; white-space: nowrap) ×4 2036年 高位;北欧の先行市場;2036年 高位;北欧の先行市場
  p#dbv(left: 442px; cy: 219px; font-size: 26px; font-family: n; color: $gl; in: {opacity:0, duration:0.3, ease:'power3.out'}) 52%
  div#ca(left: 120px; top: 316px; width: 180px; height: 34px; border-radius: 0px 6px 6px 0px; background: $cat; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  p#cav(left: 310px; cy: 333px; font-size: 26px; font-family: n; in: {opacity:0, duration:0.3, ease:'power3.out'}) 30%
  div#cb(left: 120px; top: 392px; width: 186px; height: 34px; border-radius: 0px 6px 6px 0px; background: #C3CCD6; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  p#cbv(left: 316px; cy: 410px; font-size: 26px; font-family: n; color: $gl; in: {opacity:0, duration:0.3, ease:'power3.out'}) 31%
  # hf の作り: 「まだ届かない」の注記は場面の最後の 2 秒だけ (warn flash_text)
  div#note(left: 26px; top: 470px; width: 480px; height: 105px; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'})
    div#ln(left: 0px; top: 0px; width: 480px; height: 2px; background: $hair)
    p#t(left: 0px; top: 14px; width: 480px; font-size: 22px; line-height: 1.5; font-family: m; color: $ink2) 高位でも加入率は、[br]北欧の先行市場に{nr}まだ届かない{/}

# s7 2 つの変数: 左の板は 1,014 → +708 → +172 → 1,894 の滝の棒 (足す 2 本は上から弾んで落ちる)・上の括弧「伸び 880 億円」・右上は 1 ポイントの重みの横棒 (猫 > 犬)・右下は単価と加入率の 2 つの箱が両向きの赤い矢印で「ぶつかる」
section#s7(stagger: {each:0}; out: {x:-48, opacity:0, duration:0.3, ease:'power2.in'})
header#h7(n: "06"; k: "伸びを決める2つの変数"; t: "伸びの大半は{b}加入率{/}から。値上げは加入率とぶつかる"; f: "出典：みなとリサーチ（架空の調査会社）による国内ペット保険市場の推計（2026年）。中位シナリオ（加入率 犬32%・猫20%、保険料+10%）。"; pg: "{pb}07{/} / 08")
panel#s7pl(left: 96px; top: 206px; width: 1060px; height: 690px; t: "中位シナリオの伸びの内訳"; u: "（億円・2026→2036年）")
  div#b0(left: 70px; top: 397px; width: 170px; height: 203px; border-radius: 6px 6px 0px 0px; background: $gray; in: {scaleY:0, duration:0.6, ease:'power3.out', pivot:'bottom'})
  div#b1(left: 310px; top: 256px; width: 170px; height: 142px; border-radius: 6px 6px 0px 0px; background: $dog; in: {y:-60, opacity:0, duration:0.55, ease:'bounce.out'})
  div#b2(left: 550px; top: 221px; width: 170px; height: 34px; border-radius: 6px 6px 0px 0px; background: $lift; in: {y:-50, opacity:0, duration:0.5, ease:'bounce.out'})
  div#b3(left: 790px; top: 221px; width: 170px; height: 379px; border-radius: 6px 6px 0px 0px; background: $ink; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom'})
  p#n(left: "30;190;350;510"; top: 612px; width: 220px; text-align: center; font-size: 22px; color: $ink2; white-space: nowrap; in: {y:6, opacity:0, duration:0.3, ease:'power3.out'}) ×4 2026年;加入率の上昇;保険料の値上げ;2036年（中位）
  shape#cn(left: "160;320;480"; top: "264;169.6;146.7"; width: 70px; height: 3px; path: line_h; border: 3px solid #94A2B3; dash: 4,3; in: {scaleX:0, duration:0.3, ease:'power3.out', pivot:'left'}) ×3
  p#v(left: "30;190;350;510"; top: "234.1;139.7;116.8;116.8"; width: 220px; text-align: center; font-size: 28px; font-family: n; color: "$ink2;$dog;$ink2;$ink2"; in: {y:8, opacity:0, duration:0.3, ease:'power3.out'}) ×4 1,014;+708;+172;1,894
  div#base(left: 40px; top: 600px; width: 990px; height: 2px; background: $ink)
  shape#br(path: "M208 98.7 L208 89.3 L335.3 89.3 L343.3 81.3 L351.3 89.3 L478.7 89.3 L478.7 98.7"; background: none; border: 3px solid $ink; in: {y:8, opacity:0, duration:0.4, ease:'power3.out'})
  p#bl(left: 310px; top: 78px; width: 410px; text-align: center; font-size: 24px; white-space: nowrap; in: pp) 伸び {b7}880{/}億円
panel#s7pw(left: 1190px; top: 206px; width: 634px; height: 320px; t: "加入率 1ポイントの重み"; u: "（2036年）")
  p#lc(left: 26px; top: 96px; font-size: 26px; font-family: h) 猫
  p#ld(left: 26px; top: 164px; font-size: 26px; font-family: h) 犬
  div#wc(left: 90px; top: 92px; width: 390px; height: 46px; border-radius: 0px 6px 6px 0px; background: $cat; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  div#wd(left: 90px; top: 160px; width: 350px; height: 46px; border-radius: 0px 6px 6px 0px; background: $dog; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#wcv(left: 492px; top: 99px; font-size: 22px; color: $ink2; white-space: nowrap; in: {opacity:0, duration:0.3, ease:'power3.out'}) {ao}39{/}億円
  p#wdv(left: 452px; top: 166px; font-size: 22px; color: $ink2; white-space: nowrap; in: {opacity:0, duration:0.3, ease:'power3.out'}) {hn}35{/}億円
  p#wn(left: 26px; top: 236px; font-size: 21px; color: $ink2; white-space: nowrap; in: {y:8, opacity:0, duration:0.4, ease:'power3.out'}) 頭数の多い猫の方が、1ポイントの重みが大きい
panel#s7pp(left: 1190px; top: 544px; width: 634px; height: 350px; t: "2つ目の変数：年間保険料")
  p#q(left: 26px; top: 84px; font-size: 22px; white-space: nowrap; in: {y:8, opacity:0, duration:0.4, ease:'power3.out'}) 論点｜補償を厚くして、単価を上げられるか
  tbox#t1(left: 26px; top: 138px; t: "単価を上げる"; s: "補償を厚くする"; in: {x:-20, opacity:0, duration:0.4, ease:'power3.out'})
  tbox#t2(left: 372px; top: 138px; t: "加入率が下がる"; s: "ためらう理由1位は[br]「保険料が高い」"; c: #FBF0EE; bc: #F0C9C4; tc: $red; in: {x:20, opacity:0, duration:0.4, ease:'power3.out'})
  shape#tx(left: 285px; top: 188px; width: 64px; height: 27px; path: arrow_lr,head=line; background: $red; border: 4px solid $red; in: pp)
  # hf の作り: 「ぶつかる」は場面の最後の語で弾んで出る (warn flash_text)
  p#txl(left: 262px; top: 236px; width: 110px; text-align: center; font-size: 20px; font-family: h; color: $red; in: pp) ぶつかる

# s8 結論: 3 枚の結論の札を文ごとに下から (上端の色の線・番号の丸・大きい数字・語で伸びる橙の下帯)・1 枚目に 4 本のシナリオの小さな棒・2 枚目に猫・3 枚目に子犬と子猫・言い終えて番号の丸が順に弾み、白へ溶けて終わる
section#s8(stagger: {each:0})
header#h8(n: "07"; k: "結論"; t: "伸びしろは{b}加入率{/}。鍵は{o}猫{/}と{o}1歳未満{/}での加入"; f: "出典：みなとリサーチ（架空の調査会社）による国内ペット保険市場の推計（2026年）。"; pg: "{pb}08{/} / 08")
concl#c8a(left: 96px; top: 206px; n: "1"; h: "市場は10年で[br]1.2〜2.9倍"; c: $dog; big: "約1,900{bu}億円{/}"; s: "中位シナリオ（2026年の1.9倍）"; b: "伸び率の鈍化は{mk}飽和ではない{/}。[br]加入率が、まだ低いまま。")
  div#mb(left: "38.7;117.3;196;274.7"; top: "386.3;380.8;362.8;333.7"; width: 80px; height: "27;32.5;50.5;79.6"; border-radius: 6px 6px 0px 0px; background: "$gray;$low;$dog;$high"; in: {scaleY:0, duration:0.5, ease:'power3.out', pivot:'bottom', stagger:{each:0.12}}) ×4
  p#ml(left: "25.3;104;182.7;261.3"; top: 628px; width: 120px; text-align: center; font-size: 16px; color: $mut) ×4 2026;低位;中位;高位
concl#c8b(left: 680px; top: 206px; n: "2"; h: "最大の伸びしろは[br]猫"; c: $catd; big: "10{bu}%{/}"; s: "国内の猫の加入率。北欧の3分の1"; b: "頭数は最多。「室内飼いだから不要」という{mk}思い込みを崩せるか{/}。")
  img#ic(left: 180px; top: 470px; width: 190px; height: 190px; content: @cat; object-fit: contain)
concl#c8c(left: 1264px; top: 206px; n: "3"; h: "加入は[br]1歳未満で決まる"; c: $ink; big: "68{bu}%{/}"; s: "加入者のうち1歳未満で加入した割合"; b: "若いうちに{mk}月2,000円台{/}で入れる商品が、[br]加入率と単価の両立の鍵。")
  img#ic(left: 171px; top: 478px; width: 218px; height: 182px; content: @young; object-fit: contain)
```

```timeline.txt
#v2
cast n = "落ち着いた低音域の30〜40代の男性ナレーター、響きが豊かで滑らか、知的で信頼感のある語り口、企業の解説動画らしく明瞭に淡々と読む" speed=120%
silence head=0ms tail=0ms
# 切替は書かない (場面は section の out で左へ抜け、次の場面は境目から組み上がる・進行は常設)。場面の境目の 0.3 秒前に風切り (前の cut の末尾の無音の間)・声は境目の 0.2 秒後から

*** s1
[>#subtitle]
bgm music
@n: [silence:0.6s][♪title -0.9dB -550ms][♪soft -3.1dB +450ms][!#s1_t2{hl} marker +450ms][!#s1_hero to,{y:-10, duration:2.2, ease:'sine.inOut', yoyo:true, repeat:1} +1100ms]ペット保険の市場は、あと何倍伸びるのか。[♪tick -4.4dB -100ms]「みなとリサーチ」の推計で見ていきます。[silence:0.05s][♪swoosh -4.4dB][silence:0.3s]

*** s2
@n: [silence:0.2s][>#prog.f[1] -200ms][>#s2pl -200ms][>#s2pl.b[*] +100ms][>#s2pl.v[*] +400ms]2026年の市場規模は[>#s2kpi -550ms][!#s2pl.b[6] punch {scale: 1.04, duration: .36} +200ms][♪hit -0.9dB]1,014億円。[||]5年前の[>#s2pl.ref -200ms][>#s2pl.arw][>#s2pl.x16 +150ms][>#s2kpi.chip +100ms][♪pop -0.9dB][>#s2pl.cagr +900ms][♪tick -5.2dB +900ms]1.6倍です。ただ、[>#s2yoy -350ms][♪soft -3.1dB -300ms]前年比の伸びは[>#s2yoy.line][>#s2yoy.d[1] -50ms][>#s2yoy.v[1]][>#s2yoy.d[2] +437ms][>#s2yoy.v[2] +487ms][>#s2yoy.d[3] +925ms][>#s2yoy.v[3] +975ms][>#s2yoy.d[4] +1412ms][>#s2yoy.v[4] +1462ms][>#s2yoy.d[5] +1900ms][>#s2yoy.v[5] +1950ms]11.3%から7.9%へ、[>#s2yoy.down][♪tick -4.4dB]毎年下がっています。[silence:0.05s][♪swoosh -4.4dB][silence:0.3s]

*** s3
@n: [silence:0.2s][>#prog.f[2] -200ms]市場を、[>#s3h[1] -100ms][>#s3h[3] +150ms]頭数、[>#s3h[2] -100ms]加入率、[>#s3h[4] -100ms][>#s3h[5] +300ms][>#s3h[6] +500ms]保険料に分解します。[>#s3dogi -150ms][>#s3dogl -50ms][>#s3dog[1] +250ms][>#s3dop[1] +450ms]犬は680万頭、加入率[>#s3dog[2] -50ms][>#s3dop[2] +250ms][>#s3dog[3] +400ms]19%で[>#s3dop[3] -750ms][>#s3dog[4] -600ms][>#s3dop[4] -250ms][>#s3dog[5] -100ms][♪pop -1.4dB -50ms][>#s3dog[6] +350ms]672億円。[>#s3cati -150ms][>#s3catl -50ms][>#s3cat[1] +250ms][>#s3cop[1] +450ms]猫は900万頭、[>#s3cat[2] -50ms][>#s3cop[2] +250ms][>#s3cat[3] +400ms]10%で[>#s3cop[3] -750ms][>#s3cat[4] -600ms][>#s3cop[4] -250ms][>#s3cat[5] -100ms][♪pop -1.4dB -50ms][>#s3cat[6] +350ms][>#s3totl +900ms][>#s3tot[1] +1000ms][>#s3tot[2] +1070ms][>#s3tot[3] +1140ms][>#s3tot[4] +1210ms][>#s3tot[5] +1280ms][>#s3top[1] +1350ms][>#s3top[2] +1420ms][>#s3tarw +1490ms][♪tick -5.2dB +1000ms]342億円。[>#s3pa -400ms][>#s3pa.bd -100ms][>#s3pa.bc +50ms][>#s3pa.vd +400ms][>#s3pa.vc +600ms]猫の方が[>#s3pa.dl -100ms][>#s3pa.ex][>#s3pa.plus +100ms][♪pop -1.9dB +100ms]220万頭多いのに、[>#s3pb -450ms][>#s3pb.bd -200ms][>#s3pb.bc -50ms][>#s3pb.vd +300ms][>#s3pb.vc +450ms]市場は犬の[>#s3pb.dl -150ms][>#s3pb.half][♪hit -1.4dB]半分です。[silence:0.55s][♪swoosh -4.4dB][silence:0.3s]

*** s4
@n: [silence:0.2s][>#prog.f[3] -200ms][>#s4pl -200ms][>#s4pl.gn[1]][>#s4pl.d[1] +100ms][>#s4pl.c[1] +250ms]北欧の先行市場では、犬の[>#s4pl.dv[1] -100ms][♪tick -6dB -100ms]52%、猫の[>#s4pl.cv[1] -100ms]31%が[>#s4pl.gn[2] -250ms][>#s4pl.d[2] -200ms][>#s4pl.c[2] -50ms][>#s4pl.dv[2] +300ms][>#s4pl.cv[2] +400ms]加入しています。[>#s4pl.band -350ms][>#s4pl.gn[3] -300ms][>#s4pl.d[3] -200ms][>#s4pl.c[3]][>#s4pl.dv[3] +300ms][>#s4card +450ms]国内の猫は[>#s4pl.cv[3] pop {scale: .82, duration: .45} -50ms][!#s4card.n .cnt -250ms][♪hit -1.4dB]10%、北欧の[>#s4pl.ref -500ms][>#s4pl.arw -150ms][>#s4pl.third][!#s4card.b punch {scale: 1.1, duration: .36} +100ms][♪pop -0.9dB]3分の1です。[silence:0.05s][♪swoosh -4.4dB][silence:0.3s]

*** s5
@n: [silence:0.2s][>#prog.f[4] -200ms][>#s5pl -200ms][>#s5pl.rl[*] -200ms][>#s5pl.rb[*]][>#s5pl.rv[*] +350ms]加入をためらう理由の1位は、「保険料が高い」[||][!#s5pl.rv[1] punch {scale: 1.25, duration: .36, pivot: 'left'}][!#s5pl.rb[1] punch {scale: 1.03, duration: .36, pivot: 'left'}][♪hit -1.4dB]41%。[>#s5ca -300ms][♪pop -1.9dB -250ms]猫の飼い主の[>#s5ca.bc -250ms][>#s5ca.vc +100ms][>#s5ca.bd +500ms][>#s5ca.vd +800ms]38%は、「室内飼いだから不要」と答えています。[>#s5cb -300ms][♪pop -1.9dB -250ms][>#s5cb.th +200ms][>#s5cb.thl +250ms]月2,000円以下なら検討する人は[!#s5cb.n .cnt -450ms][>#s5cb.pc +300ms][>#s5cb.pcl +400ms][>#s5cb.pd +550ms][>#s5cb.pdl +650ms]47%。[>#s5cc -300ms][♪pop -1.9dB -250ms]そして加入者の[!#s5cc.n .cnt -450ms][>#s5cc.c2 +900ms]68%は、1歳未満で入っています。[silence:0.75s][♪swoosh -4.4dB][silence:0.3s]

*** s6
@n: [silence:0.2s][>#prog.f[5] -200ms]では、[>#s6asm -300ms][>#s6pl +200ms]10年後の[>#s6pl.b[1] -100ms][>#s6pl.sn[1]][>#s6pl.r[1] +150ms][>#s6pl.v[1] +250ms][>#s6pl.p[1] +250ms]2036年はどうなるか。[>#s6pl.sn[2] -100ms][>#s6pl.b[2] +50ms][♪pop -1.9dB +50ms][>#s6pl.r[2] +200ms][>#s6pl.p[2] +300ms]低位で[>#s6pl.v[2] -200ms]1,221億円、[>#s6pl.m[1] -50ms]1.2倍。[>#s6pl.sn[3] -100ms][>#s6pl.b[3] +50ms][♪pop -1.9dB +50ms][>#s6pl.r[3] +200ms][>#s6pl.p[3] +300ms]中位で[>#s6pl.v[3] -200ms]1,894億円、[>#s6pl.m[2] -50ms]1.9倍。[>#s6pl.sn[4] -100ms][>#s6pl.b[4] +50ms][♪hit -0.9dB +50ms][>#s6pl.r[4] +200ms][>#s6pl.p[4] +300ms]高位なら[>#s6pl.v[4] -200ms]2,985億円、[>#s6pl.m[3] -50ms]2.9倍です。[>#s6cmp -450ms][♪soft -2.5dB -400ms][>#s6cmp.da -100ms][>#s6cmp.db +50ms][>#s6cmp.dav +250ms][>#s6cmp.ca +250ms][>#s6cmp.dbv +400ms][>#s6cmp.cb +400ms][>#s6cmp.cav +600ms][>#s6cmp.cbv +750ms]それでも加入率は、北欧に[>#s6cmp.note -200ms]届きません。[silence:0.35s][♪swoosh -4.4dB][silence:0.3s]

*** s7
@n: [silence:0.2s][>#prog.f[6] -200ms]伸びを決める[>#s7pl -300ms][>#s7pl.b0 +100ms][>#s7pl.n[1] +200ms][>#s7pl.v[1] +450ms]1つ目の変数は、加入率。中位の伸び[>#s7pl.br -200ms][>#s7pl.bl -100ms][♪tick -5.2dB -100ms]880億円のうち、[>#s7pl.cn[1] -350ms][>#s7pl.n[2] -300ms][>#s7pl.b1 -200ms][♪pop -1.4dB][>#s7pl.v[2] pop {scale: .82, duration: .45} +250ms]708億円は加入率の効果で、値上げ分は[>#s7pl.cn[2] -450ms][>#s7pl.n[3] -400ms][>#s7pl.b2 -300ms][♪pop -1.9dB -100ms][>#s7pl.v[3] pop {scale: .82, duration: .45} +150ms][>#s7pl.cn[3] +450ms][>#s7pl.b3 +600ms][>#s7pl.n[4] +600ms][♪tick -5.2dB +650ms][>#s7pl.v[4] +1100ms]172億円です。加入率[>#s7pw -400ms][♪soft -3.1dB -350ms]1ポイントの重みは、[>#s7pw.wc -100ms][>#s7pw.wcv +350ms]猫39億円、[>#s7pw.wd -100ms][>#s7pw.wdv +350ms][>#s7pw.wn +800ms]犬35億円。[>#s7pp -350ms][>#s7pp.q +50ms][>#s7pp.t1 +500ms]2つ目の保険料は、[>#s7pp.t2 +200ms]上げるほど加入率と[>#s7pp.tx -150ms][>#s7pp.txl -50ms][♪hit -1.4dB -100ms][!#s7pp.t2 punch {scale: 1.05, duration: .36} +200ms]ぶつかります。[silence:0.05s][♪swoosh -4.4dB][silence:0.3s]

*** s8
@n: [silence:0.2s][>#prog.f[7] -200ms]結論です。[||][>#c8a -300ms][♪pop -1.9dB -250ms][>#c8a.mb[*] +300ms]市場は10年で1.2〜2.9倍、中位でおよそ1,900億円。鈍化は[!#c8a.b{mk} marker -100ms]飽和ではなく、加入率がまだ低いままなのです。[>#c8b -300ms][♪pop -1.9dB -250ms][!#c8b.b{mk} marker +900ms]最大の伸びしろは猫。[||][>#c8c -300ms][♪pop -1.9dB -250ms]加入は1歳未満で決まります。若いうちに[!#c8c.b{mk} marker -100ms]月2,000円台で入れる商品が、加入率と単価の両立の鍵です。[silence:0.05s][♪bell -1.9dB][silence:0.05s][!#c8a.bd punch {scale: 1.18, duration: .36}][!#c8b.bd punch {scale: 1.18, duration: .36} +120ms][!#c8c.bd punch {scale: 1.18, duration: .36} +240ms][silence:2.5s]
fade out,550ms
```

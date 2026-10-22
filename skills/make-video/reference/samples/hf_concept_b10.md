# concept · effectuation (hf 全力版の全量の写し — 1分でわかるエフェクチュエーション・10 場面のパステルの白いカードと札で原則を重ねる図解) — canvas 1080x1920

見せる作り: 全編の生成りの地 (漂う色の光・点の地紋・丘・回る菱形) を語で塗り替える・上端の進行線と題の札・場面ごとに傾いて弾む白いカード 1 枚 (語で横へ払って入れ替え・前のカードを後ろへ重ねる)・左上の紫の原則札とカード下端の判子札・1 字ずつ落ちる題・中央で弾んでから上へ縮む POINT の丸・× / ○ の判子と彩度落ち・2×2 の絵を切り抜く資源の札・弾けて散る菱形・5 枚の小カードのまとめ・カーソルが押すボタンと揺れる三角・語の帯つきの白い札の字幕・音の層 (BGM + 語に結んだ効果音 39 + 場面の頭の払う音 7)

```design.txt
#v2
# 学ぶ作り: 全編に敷く生成りの地 (漂う 5 つの色の光・点の地紋・下端の 3 つの丘・回りながら漂う菱形) の色を、場面の気分に合わせて語で塗り替える (#tint の fill)
# 主役は場面ごとに 1 枚の白い角丸のカード (少し傾けて弾んで入り、語で横へ払われて次のカードと入れ替わる)・その上に紫の原則札 (左上) と黄の判子札 (カードの下端に重ねる)
# 比べる場面は 2 枚の小さなカードに × と ○ の判子・× の絵は彩度を落とす・まとめは 5 枚の小カードが順に弾む・締めはボタンをカーソルが押す
# hf b10 effectuation (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#FFF7EC
theme light
palette ink=#4A3B33 cream=#FFF7EC peach=#FFB8A3 coral=#E5563F coralsoft=#FF8F7A mint=#9EE3C8 mintd=#1F9A75 lav=#C9BDFF lavd=#7462E0 butter=#FFE38A sky=#BFE3FF ngc=#F2605C negbg=#E6E0F7 negink=#6B5F86 neglabel=#8A7FA6
font "極太の丸ゴシック体 — bold rounded Japanese sans-serif (Maru Gothic) with thick, solid strokes and soft circular terminals"
fonts m="ころんと丸いポップな極太の見出し書体、手書き風のやわらかい太字ゴシック" r="丸ゴシック体 (Maru Gothic) の ExtraBold、円い端の均一な線 — rounded sans-serif with gentle circular stroke terminals, ExtraBold weight"
sfx off
master lufs=-14.5
art "soft pastel flat illustration with a subtle grainy paper texture, thin warm-brown outlines, rounded friendly shapes and gentle soft shading, pastel palette of mint green, peach pink, lavender, butter yellow and baby blue"
prompt_tail "Plain light cream background (#FFF6EA). Simple uncluttered composition centered with generous margins, cute modern Japanese editorial illustration. Absolutely no text, no letters, no numbers, no logos."
# 同じ人物を全部の絵に: 主人公の基準画像 + 2 回以上出る絵は根に置き @名 で使い回す (まとめの 5 枚は前の場面の絵そのもの)
image hero = "A cheerful young Japanese woman with a short wavy brown bob, rosy cheeks, wearing a mint green cardigan over a cream t-shirt, beige pants and white sneakers, standing full-body and smiling, one hand raised with a glowing light bulb floating above her palm. Around her float small everyday items: an open book, a little toolbox, a heart-shaped puzzle piece, a potted sprout and a few sparkles."
image stuck = "[ref:@hero]The young woman sits at a small desk holding her head with both hands, looking troubled and stuck, in front of a big blank planning board covered with empty boxes, arrows and question-mark shapes (no writing). Crumpled paper balls lie on the floor and a small gray cloud with a squiggle floats above her head. Keep soft pastel colors."
image bag = "[ref:@hero]The young woman happily pulls everyday items out of her canvas tote bag: an open book, a small wrench, a smartphone, a potted sprout and a heart, which float out of the bag in a cheerful arc."
image pool = "[ref:@hero]The young woman carefully dips just one toe into a small shallow round kiddie pool with a floating swim ring and a rubber duck, testing the water with a relaxed smile, conveying a small and safe trial."
image quilt = "[ref:@hero]The young woman and three diverse friends (a young man with round glasses, a woman with a ponytail, a man with curly hair) happily sew together one big colorful patchwork quilt made of mismatched pastel patches, each person adding a different patch."
image lemon = "[ref:@hero]Lemons unexpectedly tumble down from a lemon tree around the young woman; she smiles brightly and squeezes them into a glass pitcher of fresh lemonade on a small table, with lemon slices and sparkles."
image pilot = "[ref:@hero]The young woman wearing a leather pilot cap and goggles flies a small cute pastel propeller airplane through soft fluffy clouds, holding the control stick confidently and smiling, with a sunny horizon ahead of her."
# 4 つの資源の絵は 1 枚の 2×2 の絵から象限ごとに切り抜く (fit の focus + zoom 200%)
image icons = "A 2x2 grid of four separate cute pastel icons, evenly spaced on a plain light cream background, each icon centered in its own quadrant with plenty of empty space between them and no borders or frames: top-left an open book with a small glowing light bulb above it; top-right a pair of footprints next to a small flag on a little hill; bottom-left a wrench and a paintbrush crossed over a gear; bottom-right three smiling round-faced people connected by dotted lines."
sound whoosh = "柔らかく短いシュッという風切り音"
sound pop_high = "高く軽いポンという可愛いポップ音"
sound pop_dry = "乾いた短いポコッというポップ音"
sound sparkle = "ハープのグリッサンドのようなキラキラと輝く音"
sound buzz = "短く低いブッという不正解のブザー音"
sound idea = "ひらめきを表す明るいチャイムのピコーンという音"
sound correct = "鉄琴の明るい正解音、ピンポロンと上がる"
sound xylo = "木琴がコロコロと駆け上がる上昇音"
sound click = "マウスのカチッという短いクリック音"
# 字幕の語の印: 前向きの語はバターの帯・打ち消す語はラベンダーの帯 (hf は語の下 38% の帯が語で伸びる — 字幕の run は字の高さいっぱいの地になる)
run hl { marker: $butter,37%; border-radius: 14px; padding: 6px }
run ng { marker: #DDD5FB,37%; border-radius: 14px; padding: 6px }
p { color: $ink; out: {scale:.92, opacity:0, duration:.2, ease:'power2.in'} }
div { out: {y:-70, scale:.9, rotation:1.5, opacity:0, duration:.22, ease:'power2.in'} }
shape { out: {scale:.92, opacity:0, duration:.2, ease:'power2.in'} }
icon { out: {scale:.92, opacity:0, duration:.2, ease:'power2.in'} }
group { out: {scale:.92, opacity:0, duration:.2, ease:'power2.in'} }
# 場面の頭の要素は一斉に (hf は場面の頭のカードと札を同じ拍で出す)
cut { stagger: 0 }
# hf の作り: 字幕は画面の中ほど (下端から 1/3 の高さ) に置き、下は丘の地だけ (色の光が字幕帯に掛かる = caption_collision)・上端の題の札は 2 場面目の頭から出し続ける (spoiler)
# hf の作り: 開幕の英字・名の札の副題・原則札は 1.2〜2.7 秒で入れ替わる (flash_text)・4 つの資源の札は 1 枚の絵の象限 (duplicate_media)・判子札「手元にあるもので今すぐ動く」は字幕と同文 (duplicate_text)
# hf の作り: 言い換えの場面とまとめの場面は 5 秒に 8〜9 回の効果音 (払う音・× のブザー・正解音・カード 5 枚の pop) (se_dense)
lint off=caption_collision,spoiler,flash_text,duplicate_media,duplicate_text,se_dense
bgm#music(fade: 250,2600) 明るく軽快なアコースティックポップ、弾むアコースティックギターのリフと口笛、軽やかなパーカッション、晴れやかで楽しい
# 字幕: 白い角丸の札・極太の丸ゴシック・下から少し弾んで出て上へ抜ける・文の中の行で札を替え ([|])、札は次の札か cut の終わりまで残る (tail=10000 = 札の区間の終わりまで)
subtitle.hug(top: 1300px; width: 1020px; font-size: 56px; line-height: 1.36; text-align: center; color: $ink; background: #FFFFFF; border-radius: 42px; padding: 22px 42px 26px 42px; box-shadow: 0px 18px 40px #785A3C1A; unit: sentence; lead: 0; tail: 10000; hold: next,1200; in: {y:34, scale:.94, opacity:0, duration:.24, ease:'back.out(1.8)'}; out: {y:-14, opacity:0, duration:.14, ease:'power1.in'})

# 地 (全編・最背面): 地の色 (語で塗り替える) → 漂う色の光 5 つ → 点の地紋 → 下端の丘 3 つ → 回りながら漂う菱形 5 つ
div#tint(inset: 0; background: $cream; z-index: back; in: none; out: none)
div#b1(left: -280px; top: -200px; width: 780px; height: 780px; border-radius: 390px; background: radial(#FFB8A39E,#FFB8A300@68%,50%,50%); z-index: back; in: none; out: none; main: keys(at=0 x=0 y=0 | at=0.25 x=80 y=64 ease=none | at=0.5 x=16 y=107 ease=none | at=0.75 x=64 y=32 ease=none | at=1 ease=none),duration=60000)
div#b2(left: 560px; top: 380px; width: 860px; height: 860px; border-radius: 430px; background: radial(#9EE3C899,#9EE3C800@68%,50%,50%); z-index: back; in: none; out: none; main: keys(at=0 x=0 y=0 | at=0.25 x=-93 y=48 ease=none | at=0.5 x=-19 y=80 ease=none | at=0.75 x=-75 y=24 ease=none | at=1 ease=none),duration=60000)
div#b3(left: -300px; top: 960px; width: 760px; height: 760px; border-radius: 381px; background: radial(#C9BDFF8C,#C9BDFF00@68%,50%,50%); z-index: back; in: none; out: none; main: keys(at=0 x=0 y=0 | at=0.25 x=107 y=-56 ease=none | at=0.5 x=21 y=-93 ease=none | at=0.75 x=85 y=-28 ease=none | at=1 ease=none),duration=60000)
div#b4(left: 560px; top: 1300px; width: 700px; height: 700px; border-radius: 351px; background: radial(#FFE38A9E,#FFE38A00@68%,50%,50%); z-index: back; in: none; out: none; main: keys(at=0 x=0 y=0 | at=0.25 x=-80 y=-64 ease=none | at=0.5 x=-16 y=-107 ease=none | at=0.75 x=-64 y=-32 ease=none | at=1 ease=none),duration=60000)
div#b5(left: 300px; top: -300px; width: 600px; height: 600px; border-radius: 300px; background: radial(#BFE3FF99,#BFE3FF00@68%,50%,50%); z-index: back; in: none; out: none; main: keys(at=0 x=0 y=0 | at=0.25 x=60 y=44 ease=none | at=0.5 x=12 y=73 ease=none | at=0.75 x=48 y=22 ease=none | at=1 ease=none),duration=60000)
div#dots(inset: 0; pattern: dots,31,#4A3B331A; z-index: back; in: none; out: none)
shape#h1.ellipse.bleed(left: -460px; top: 1590px; width: 1500px; height: 760px; background: #D9F2E6; z-index: back; in: none; out: none; main: keys(at=0 x=0 | at=0.25 x=40 ease=none | at=0.5 x=-13 ease=none | at=0.75 x=20 ease=none | at=1 ease=none),duration=60000)
shape#h2.ellipse.bleed(left: 320px; top: 1650px; width: 1300px; height: 700px; background: #FFE4D9; z-index: back; in: none; out: none; main: keys(at=0 x=0 | at=0.25 x=-47 ease=none | at=0.5 x=7 ease=none | at=0.75 x=-27 ease=none | at=1 ease=none),duration=60000)
shape#h3.ellipse.bleed(left: -120px; top: 1760px; width: 900px; height: 520px; background: #ECE7FF; z-index: back; in: none; out: none)
# 漂う菱形 (45° に回した角丸の四角・60 秒で 270° 回りながら上下に揺れる)
def gem(c) = div(border-radius: 8px; background: {c}; transform: rotate(45deg))
gem#bgs(left: "68;622;127;572;354"; top: "978;1002;1127;1152;1101"; width: "18;22;13;15;11"; height: "18;22;13;15;11"; c: "$butter;$mint;$peach;$lav;#FFFFFF"; z-index: back; in: none; out: none; main: keys(at=0 y=0 rotation=0 | at=0.1667 y=-12 rotation=45 ease=none | at=0.3333 y=0 rotation=90 ease=none | at=0.5 y=-8 rotation=135 ease=none | at=0.6667 y=0 rotation=180 ease=none | at=0.8333 y=-11 rotation=225 ease=none | at=1 rotation=270 ease=none),duration=60000) ×5
# 上端の進行線 (淡い地 + 珊瑚 → 橙 → 緑のグラデの棒が 60 秒で伸びる)
div#track(left: 0px; top: 0px; width: 1080px; height: 12px; background: #4A3B3314; z-index: front; in: none; out: none)
progress#bar(left: 0px; top: 0px; width: 1080px; height: 12px; background: linear(#FF8F7A,#FFC46B,#5CCFA5,90); until: end; z-index: front; overlap: track)

# 部品
# 弾けて散る菱形 (語で 5 つが外へ跳ねて回り、0.55 秒後にさらに外へ散って消える)・群の member ごとに向きの x / y を書く (×N の object は instance ごとに分けられない)
def burst(c) = div(width: 39px; height: 39px; border-radius: 9px; background: {c}; transform: rotate(45deg))
# 主役のカード (白い角丸 + 内側の絵がゆっくり寄る)・既定は下から傾いて弾んで入り、上へ傾いて抜ける
def card(src) = div(left: 90px; top: 250px; width: 900px; height: 900px; border-radius: 64px; background: #FFFFFF; box-shadow: 0px 30px 60px #785A3C29; transform: rotate(-1.2deg); in: {y:110, scale:.82, rotation:-4.8, opacity:0, duration:.6, ease:'back.out(1.5)'}; out: {y:-70, scale:.9, rotation:4.2, opacity:0, duration:.22, ease:'power2.in'})
  img#img(left: 18px; top: 18px; width: 864px; height: 864px; border-radius: 48px; main: kb {scale: [1, 1.07]}; content: {src})
# 比べる場面の小さなカード
def mini(src) = div(top: 470px; width: 470px; height: 470px; border-radius: 52px; background: #FFFFFF; box-shadow: 0px 26px 50px #785A3C26; out: {y:-60, opacity:0, duration:.22, ease:'power2.in'})
  img#img(left: 14px; top: 14px; width: 442px; height: 442px; border-radius: 40px; main: none; content: {src})
# × の判子 (白い縁の赤い太い棒 2 本を ±45°・大きく回って叩きつけられる)
def ngx(w, h) = div(cx: 50%; cy: 50%; width: {w}; height: {w}; z-index: front; in: {scale:2.2, rotation:-25, opacity:0, duration:.32, ease:'back.out(2.6)'})
  div#a(left: 0px; cy: 50%; width: {w}; height: {h}; border-radius: 148px; background: $ngc; box-shadow: 0px 0px 0px 9px #FFFFFF; transform: rotate(45deg))
  div#b(left: 0px; cy: 50%; width: {w}; height: {h}; border-radius: 148px; background: $ngc; box-shadow: 0px 0px 0px 9px #FFFFFF; transform: rotate(-45deg))
# 原則の札 (紫の地・白い縁・白い丸札の番号 + 名 + 小さな英名)・板は群の中の兄弟 (文字が板の上に乗るのを check が読める形)
def tag(n, t, e, w) = group(left: 70px; top: 214px; width: {w}; height: 69px; transform: rotate(-2deg); in: {scale:.5, rotation:-4, opacity:0, duration:.45, ease:'back.out(2.2)'})
  div#bg(left: 0px; top: 0px; width: {w}; height: 69px; border-radius: 148px; background: $lavd; border: 4px solid #FFFFFF; box-shadow: 0px 6px 0px #4A3B3324)
  p#n(left: 26px; cy: 34px; font-size: 28px; font-family: r; line-height: 1; white-space: nowrap; color: $lavd; background: #FFFFFF; border-radius: 148px; padding: 6px 14px 8px 14px; content: {n})
  p#t(left: .n.right+14; cy: 34px; font-size: 38px; font-family: r; line-height: 1; white-space: nowrap; color: #FFFFFF; content: {t})
  p#e(left: .t.right+14; cy: 38px; font-size: 26px; font-family: r; line-height: 1; white-space: nowrap; letter-spacing: .04em; color: #FFFFFFE6; content: {e})
# 判子札 (カードの下端に重ねるバターの丸札・白い縁・硬い影)・neg = 灰紫の地 + 紫の字・ok = ミント
def sticker(t, c=$butter, s=40, r=-2) = p(cx: 540px; top: 1090px; font-size: {s}; font-family: m; line-height: 1.15; background: {c}; border: 8px solid #FFFFFF; border-radius: 148px; padding: 18px 46px 22px 46px; box-shadow: 0px 10px 0px #4A3B331A; white-space: nowrap; rotation: {r}; in: {scale:.4, rotation:-6, opacity:0, duration:.45, ease:'back.out(2.2)'}; content: {t})

# title — 開幕: 主人公のカードが傾いて弾み、珊瑚の札「1分でわかる」→ 題が 1 字ずつ上から回って落ち → 英字が横に縮んで締まる・四隅に菱形
section#title
div#t_hero(left: 140px; top: 640px; width: 800px; height: 800px; border-radius: 80px; background: #FFFFFF; box-shadow: 0px 30px 60px #785A3C29; delay: 80; in: {scale:.6, rotation:-8, opacity:0, duration:.7, ease:'back.out(1.6)'}; out: {y:120, scale:.7, rotation:6, opacity:0, duration:.24, ease:'power2.in'})
  img#img(left: 16px; top: 16px; width: 766px; height: 766px; border-radius: 48px; content: @hero; main: kb {scale: [1, 1.07]})
p#t_chip(cx: 540px; top: 262px; font-size: 58px; font-family: r; line-height: 1; color: #FFFFFF; background: $coral; border: 8px solid #FFFFFF; border-radius: 148px; padding: 18px 48px 22px 48px; box-shadow: 0px 10px 0px #4A3B331A; rotation: -2; in: {scale:.2, rotation:-10, opacity:0, duration:.45, ease:'back.out(2.2)'}; out: {y:-90, opacity:0, duration:.22, ease:'power2.in'}) 1分でわかる
p#t_title(cx: 540px; top: 400px; font-size: 90px; font-family: m; line-height: 1.1; white-space: nowrap; text-shadow: 0px 8px 0px #FF7E6B47; in: {y:-70, scale:.3, rotation:-14, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:.08}; out: {y:-90, opacity:0, duration:.22, ease:'power2.in'}) エフェクチュエーション
p#t_sub(cx: 540px; top: 530px; font-size: 42px; font-family: r; line-height: 1; letter-spacing: .32em; color: $lavd; in: {scaleX:1.6, y:10, opacity:0, duration:.6, ease:'power3.out'}; out: {y:-90, opacity:0, duration:.22, ease:'power2.in'}) EFFECTUATION
gem#t_gems(left: "73;613;100;600"; top: "467;507;887;860"; width: 33px; height: 33px; c: "$butter;$mint;$peach;$lav"; in: {scale:0, rotation:-180, opacity:0, duration:.5, ease:'back.out(2)', stagger:.12}; out: {scale:0, opacity:0, duration:.22}) ×4

# start — 始めたい / 動けない: 扉の前のカード → 語で左へ払われ、机で頭を抱えるカードが右から入って揺れる・地が灰紫に・上端の題の札 (以後ずっと)
section#start
p#header.sticky(cx: 540px; top: 108px; font-size: 32px; font-family: r; line-height: 1; background: #FFFFFF; border-radius: 148px; padding: 12px 30px 14px 60px; box-shadow: 0px 6px 0px #4A3B3314; in: {y:-30, opacity:0, duration:.5, ease:'back.out(2)'}; out: none) 1分でわかる {c}エフェクチュエーション{/}
  div#dot(left: 30px; cy: 50%; width: 18px; height: 18px; border-radius: 148px; background: $coralsoft)
run c { color: $coral }
card#c1a(src: "[ref:@hero]The young woman stands in front of a slightly open pastel-colored door with warm light and sparkles spilling out of the gap, leaning forward with excited shining eyes and clasped hands, eager to start something new. Small stars and confetti float around."; transform: rotate(-1.5deg); in: {y:110, scale:.82, rotation:-6.5, opacity:0, duration:.6, ease:'back.out(1.5)'}; out: {x:-1050, rotation:-10.5, opacity:0, duration:.45, ease:'power3.in'})
card#c1b(src: "@stuck"; transform: rotate(1.5deg); in: {x:1000, rotation:8.5, opacity:0, duration:.55, ease:'back.out(1.3)'})
  img#img(main: kb {scale: [1, 1.06]})

# term — 名を出す: 主人公のカード (語で一度ふくらむ) の下端に、黄の縁の白い札「エフェクチュエーション」が弾み菱形が散る・地が桃色に
section#term
card#c2(src: "@hero"; in: {y:110, scale:.6, rotation:6.8, opacity:0, duration:.6, ease:'back.out(1.5)'})
  img#img(main: kb {scale: [1, 1.1]})
div#term(left: 60px; top: 1010px; width: 960px; height: 195px; border-radius: 44px; background: #FFFFFF; border: 8px solid $butter; box-shadow: 0px 12px 0px #4A3B331A; overlap: c2; in: {y:30, scale:.3, opacity:0, duration:.55, ease:'back.out(2)'}; out: {scale:.92, opacity:0, duration:.2, ease:'power2.in'})
  p#main(cx: 50%; top: 20px; font-size: 76px; font-family: m; line-height: 1.1; color: $coral; white-space: nowrap) エフェクチュエーション
  p#sub(cx: 50%; top: 116px; font-size: 32px; font-family: r; line-height: 1; letter-spacing: .04em; white-space: nowrap) {e}EFFECTUATION{/}｜熟達した起業家の思考法
run e { color: $lavd }
group#b2(in: {opacity:0, duration:.05, stagger:.03}; out: none)
  burst#p1(left: 158px; top: 1054px; c: $butter; in: {x:-38, y:-15, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:45, y:20, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p2(left: 916px; top: 1071px; c: $mint; in: {x:3, y:-40, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-4, y:50, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p3(left: 160px; top: 1209px; c: $peach; in: {x:39, y:-9, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-48, y:12, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p4(left: 838px; top: 1176px; c: $lav; in: {x:21, y:34, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-26, y:-42, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p5(left: 548px; top: 930px; c: $butter; in: {x:-27, y:30, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:33, y:-38, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})

# point — 比べる: 黄の丸札 POINT が中央に大きく弾み (菱形が散る)、語で上へ縮んで退く (静止の姿は中央の大きな丸・語の to で上へ 0.476 倍に) → 左の小カード「完璧な計画を待つ」に × (絵の彩度が落ちて縮む) → 矢印 → 右の小カード「今あるものから始める」に ○
section#point(out: {y:-60, opacity:0, duration:.22, ease:'power2.in'})
div#point(left: 309px; top: 506px; width: 464px; height: 464px; border-radius: 232px; background: $butter; border: 20px solid #FFFFFF; box-shadow: 0px 22px 0px #4A3B331A; transform: rotate(-6deg); in: {scale:.19, rotation:-24, opacity:0, duration:.5, ease:'back.out(2.2)'})
  p#t(cx: 50%; cy: 50%; font-size: 110px; font-family: r; line-height: 1) POINT
group#b3(in: {opacity:0, duration:.05, stagger:.03}; out: none)
  burst#p1(left: 338px; top: 656px; c: $butter; in: {x:-38, y:-15, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:45, y:20, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p2(left: 736px; top: 640px; c: $mint; in: {x:3, y:-40, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-4, y:50, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p3(left: 280px; top: 909px; c: $peach; in: {x:39, y:-9, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-48, y:12, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p4(left: 699px; top: 896px; c: $lav; in: {x:21, y:34, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-26, y:-42, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p5(left: 548px; top: 490px; c: #FFFFFF; in: {x:-27, y:30, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:33, y:-38, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
mini#c3a(left: 45px; src: "[ref:@hero]The young woman stands still holding a huge unrolled blueprint plan that is taller than she is, with a big wall clock and a large hourglass behind her, looking bored and tired of waiting for the perfect plan."; transform: rotate(-2.5deg); in: {x:-60, y:110, scale:.82, rotation:-7.5, opacity:0, duration:.6, ease:'back.out(1.5)'})
  ngx#ng(w: 187; h: 31)
mini#c3b(left: 566px; src: "@bag"; transform: rotate(2.5deg); in: {x:80, y:110, scale:.82, rotation:7.5, opacity:0, duration:.6, ease:'back.out(1.5)'})
  div#ok(cx: 50%; cy: 50%; width: 250px; height: 250px; border-radius: 148px; z-index: front; border: 36px solid $mintd; box-shadow: 0px 0px 0px 9px #FFFFFF; in: {scale:2.2, rotation:-25, opacity:0, duration:.32, ease:'back.out(2.6)'})
icon#arrow3(left: 496px; top: 662px; font-size: 40px; name: play; weight: fill; color: #FFFFFF; background: $coral; border: 8px solid #FFFFFF; in: {scale:.2, opacity:0, duration:.45, ease:'back.out(2.2)'})
p#l3a(left: 30px; top: 986px; width: 500px; font-size: 54px; font-family: m; line-height: 1.25; text-align: center; color: $neglabel; in: {y:20, scale:.6, opacity:0, duration:.45, ease:'back.out(2.2)'}) 完璧な計画を[br]待つ
p#l3b(left: 550px; top: 986px; width: 500px; font-size: 54px; font-family: m; line-height: 1.25; text-align: center; color: $mintd; in: {y:20, scale:.6, opacity:0, duration:.45, ease:'back.out(2.2)'}) 今あるものから[br]始める

# means — 原則①: 紫の札「手中の鳥」と 4 枚の資源の札 (知識・経験・スキル・人脈) が語ごとに弾む → 札が縮んで消え、飛び石を踏み出すカード + 判子札「まず小さく動く」
section#means
# 資源の札 (白い角丸の札 + 2×2 の絵の象限 + 色つきの名)・語ごとに弾み、語で一斉に縮んで消える
def tile(t, c, f) = div(width: 410px; height: 410px; border-radius: 52px; background: #FFFFFF; box-shadow: 0px 24px 46px #785A3C24; in: {scale:.3, rotation:-10, opacity:0, duration:.5, ease:'back.out(2.2)'}; out: {y:-40, scale:.6, opacity:0, duration:.22, ease:'power2.in'})
  img#i(cx: 50%; top: 22px; width: 290px; height: 290px; border-radius: 30px; content: @icons; object-fit: cover; object-position: {f}; zoom: 200%; main: none)
  p#t(cx: 50%; top: 318px; font-size: 54px; font-family: m; line-height: 1; color: {c}; content: {t})
tile#tl(left: "73;373;73;373"; top: "200;200;500;500"; height: 410px; rotation: "-1.5;1.5;-1.5;1.5"; t: "知識;経験;スキル;人脈"; c: "#4E8FD6;$mintd;#E0795F;$lavd"; f: "0% 0%;100% 0%;0% 100%;100% 100%") ×4
card#c4(src: "[ref:@hero]The young woman takes a small first step onto the first of a row of round pastel stepping stones that lead into the distance, with a tiny sprout growing beside her foot and small flowers along the path; she looks determined and happy."; in: {y:110, scale:.82, rotation:-4.8, opacity:0, duration:.6, ease:'back.out(1.5)'})
  img#img(main: kb {scale: [1, 1.08]})
tag#tag4(n: "原則①"; t: "手中の鳥"; e: "Bird in Hand"; w: 345)
sticker#st4(t: "まず小さく動く"; overlap: c4)

# principles — 原則②〜④: カードを重ねていく (前のカードは傾いて後ろへ下がり薄れる)・札と判子札は文ごとに入れ替え・最後に菱形が散る
section#principles
card#c5a(src: "@pool"; transform: rotate(-1.5deg); in: {x:120, y:110, scale:.82, rotation:9.5, opacity:0, duration:.6, ease:'back.out(1.5)'}; out: {y:-80, opacity:0, duration:.22, ease:'power2.in'})
  img#img(main: kb {scale: [1, 1.06]})
card#c5b(src: "@quilt"; transform: rotate(1.5deg); in: {x:160, y:110, scale:.82, rotation:8.5, opacity:0, duration:.6, ease:'back.out(1.5)'}; out: {y:-80, opacity:0, duration:.22, ease:'power2.in'})
  img#img(main: kb {scale: [1, 1.06]})
card#c5c(src: "@lemon"; transform: rotate(-.8deg); in: {y:160, scale:.82, rotation:-5.2, opacity:0, duration:.6, ease:'back.out(1.5)'}; out: {y:-80, opacity:0, duration:.22, ease:'power2.in'})
tag#tag5a(n: "原則②"; t: "許容可能な損失"; e: "Affordable Loss"; w: 444)
tag#tag5b(n: "原則③"; t: "クレイジーキルト"; e: "Crazy Quilt"; w: 437)
tag#tag5c(n: "原則④"; t: "レモネード"; e: "Lemonade"; w: 338)
sticker#st5a(t: "痛手にならない範囲で試す"; overlap: c5a)
sticker#st5b(t: "仲間を巻き込む"; r: 2; overlap: c5b)
sticker#st5c(t: "思いがけない出来事もチャンスに"; s: 33; r: -1.5; overlap: c5c)
group#b5(in: {opacity:0, duration:.05, stagger:.03}; out: none)
  burst#p1(left: 138px; top: 1076px; c: $butter; in: {x:-38, y:-15, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:45, y:20, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p2(left: 927px; top: 1090px; c: $mint; in: {x:3, y:-40, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-4, y:50, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p3(left: 130px; top: 1239px; c: $peach; in: {x:39, y:-9, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-48, y:12, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p4(left: 860px; top: 1196px; c: $lav; in: {x:21, y:34, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:-26, y:-42, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})
  burst#p5(left: 548px; top: 950px; c: #FFFFFF; in: {x:-27, y:30, scale:0, rotation:-90, opacity:0, duration:.35, ease:'back.out(2)'}; out: {x:33, y:-38, scale:.17, rotation:90, opacity:0, duration:.5, ease:'power1.in'})

# pilot — 原則⑤: 水晶玉のカードに灰紫の札「未来を予測する」と × → 下へ落ちて消え、飛行機のカードが左下から回って入る・地が水色に・ミントの札「行動しながら未来をつくる」
section#pilot
card#c6a(src: "A fortune teller's crystal ball resting on a small tasseled cushion, with a misty swirl and a few question-mark shapes floating inside the ball, small sparkles around it, centered on a plain cream background, no people."; transform: rotate(1.2deg); in: {y:110, scale:.82, rotation:4.8, opacity:0, duration:.6, ease:'back.out(1.5)'}; out: {y:260, rotation:12.8, opacity:0, duration:.45, ease:'power3.in'})
  img#img(main: kb {scale: [1, 1.08]})
  ngx#ng(w: 267; h: 43)
card#c6b(src: "@pilot"; transform: rotate(-1deg); in: {x:-900, y:260, scale:.85, rotation:-13, opacity:0, duration:.7, ease:'power3.out'}; out: {x:400, y:-120, scale:.9, rotation:9, opacity:0, duration:.22, ease:'power2.in'})
  img#img(main: kb {scale: [1.12, 1.02], focus: ['40% 50%', '60% 50%']})
tag#tag6(n: "原則⑤"; t: "飛行機のパイロット"; e: "Pilot in the Plane"; w: 518)
sticker#st6a(t: "未来を予測する"; c: $negbg; color: $negink; r: 2; overlap: c6a)
sticker#st6b(t: "行動しながら未来をつくる"; c: $mint; overlap: c6b)

# now — 言い換え: 机で頭を抱えるカード (少し色褪せ) に灰紫の札と × → 右へ払われ、走るカードが左から飛び込んで跳ねる・地が淡い緑に
section#now
card#c7a(src: "@stuck"; in: {y:110, scale:.82, rotation:-4.8, opacity:0, duration:.6, ease:'back.out(1.5)'}; out: {x:1100, rotation:15.2, opacity:0, duration:.4, ease:'power3.in'})
  img#img(filter: saturate(0.75); main: none)
  ngx#ng(w: 267; h: 43)
card#c7b(src: "[ref:@hero]The young woman runs forward energetically with a small backpack, a book, a wrench and a sprout peeking out of the backpack, soft motion lines behind her, bright and joyful, moving from left to right."; in: {x:-1100, rotation:-6.8, opacity:0, duration:.45, ease:'power4.out'})
  img#img(main: kb {scale: [1, 1.08]})
sticker#st7a(t: "計画がないから動けない"; c: $negbg; color: $negink; overlap: c7a)
sticker#st7b(t: "手元にあるもので今すぐ動く"; c: $mint; r: 2; overlap: c7b)

# recap — まとめ: 5 枚の小カード (前の場面の絵 + 番号の丸札と原則名) が順に弾み、題「エフェクチュエーション の考え方」→ カードが順に跳ねる
section#recap(out: {scale:.85, opacity:0, duration:.22, ease:'power2.in'})
# まとめの小カード (白い枠の絵 + 紫の番号の丸札つきの原則名)・入場の stagger で順に弾む
def rc(src, n, t) = div(width: 380px; height: 360px; in: {scale:.3, rotation:-8, opacity:0, duration:.5, ease:'back.out(2.2)', stagger:.16})
  div#f(left: 50px; top: 0px; width: 280px; height: 280px; border-radius: 44px; background: #FFFFFF; box-shadow: 0px 20px 36px #785A3C24)
    img#img(left: 10px; top: 10px; width: 260px; height: 260px; border-radius: 36px; main: none; content: {src})
  p#t(cx: 50%; top: 294px; font-size: 32px; font-family: r; line-height: 1.1; white-space: nowrap; padding: 0px 0px 0px 51px; content: {t})
    p#n(left: 0px; cy: 50%; width: 44px; font-size: 26px; font-family: r; line-height: 1; text-align: center; color: #FFFFFF; background: $lavd; border-radius: 148px; padding: 9px 0px; content: {n})
rc#rc(left: "8;234;459;121;346"; top: "360;360;360;613;613"; rotation: "-2;2;-2;2;-2"; src: "@bag;@pool;@quilt;@lemon;@pilot"; n: "1;2;3;4;5"; t: "手中の鳥;許容可能な損失;クレイジーキルト;レモネード;飛行機のパイロット") ×5
group#rc_title(in: {y:-30, scale:.4, opacity:0, duration:.55, ease:'back.out(2.2)'})
  p#b(cx: 540px; top: 236px; font-size: 82px; font-family: m; line-height: 1.1; color: $coral; white-space: nowrap; text-shadow: 0px 8px 0px #FF7E6B38) エフェクチュエーション
  p#s(cx: 540px; top: 336px; font-size: 46px; font-family: r; line-height: 1; background: #FFFFFF; border-radius: 148px; padding: 12px 34px 14px 34px; box-shadow: 0px 6px 0px #4A3B3314) の考え方

# cta — 案内: 記事と対談の 2 枚のカード → 語ごとに札・概要欄 / コメント欄の札 → 珊瑚のボタン → カーソルが来て押す → 下向きの三角が揺れ続ける
section#cta
# 案内のカード (白い枠の絵 + 語で弾むバターの札)
def kcard(src, l, r=-2) = div(width: 450px; height: 555px; in: {scale:.4, rotation:-8, opacity:0, duration:.55, ease:'back.out(2.2)'})
  div#f(left: 0px; top: 0px; width: 450px; height: 450px; border-radius: 52px; background: #FFFFFF; box-shadow: 0px 26px 50px #785A3C26)
    img#img(left: 14px; top: 14px; width: 423px; height: 423px; border-radius: 40px; main: none; content: {src})
  p#l(cx: 50%; top: 468px; font-size: 46px; font-family: m; line-height: 1; background: $butter; border: 6px solid #FFFFFF; border-radius: 148px; padding: 14px 32px 18px 32px; box-shadow: 0px 8px 0px #4A3B331A; rotation: {r}; in: {scale:.3, rotation:-6, opacity:0, duration:.45, ease:'back.out(2.2)'}; content: {l})
kcard#k1(left: 70px; top: 268px; rotation: -2.5; src: "An open laptop showing a cheerful article page made of pastel blocks, small charts and picture placeholders (no readable text), next to a cup of coffee, a notebook and a small potted plant, centered on a plain cream background."; l: "解説記事")
kcard#k2(left: 560px; top: 268px; rotation: 2.5; delay: 160; in: {scale:.4, rotation:7.5, opacity:0, duration:.55, ease:'back.out(2.2)'}; src: "Two people sitting in comfy armchairs having a lively conversation in a cozy pastel studio, with two small desk microphones on a little round table between them; one gestures while explaining and the other listens with a smile, like a talk show interview."; l: "対談本編動画"; r: 2)
p#ch1(left: 266px; top: 880px; font-size: 46px; font-family: r; line-height: 1; background: #FFFFFF; border: 4px solid $sky; border-radius: 22px; padding: 16px 34px 18px 34px; box-shadow: 0px 8px 0px #4A3B3314; in: {scale:.3, opacity:0, duration:.45, ease:'back.out(2.2)'}) 概要欄
p#ch2(left: 506px; top: 880px; font-size: 46px; font-family: r; line-height: 1; background: #FFFFFF; border: 4px solid $sky; border-radius: 22px; padding: 16px 34px 18px 34px; box-shadow: 0px 8px 0px #4A3B3314; in: {scale:.3, opacity:0, duration:.45, ease:'back.out(2.2)'}) コメント欄
p#btn(cx: 540px; top: 1010px; font-size: 64px; font-family: m; line-height: 1; color: #FFFFFF; background: $coral; border: 9px solid #FFFFFF; border-radius: 148px; padding: 30px 60px 34px 60px; box-shadow: 0px 14px 0px #C2432E; white-space: nowrap; in: {scale:.3, opacity:0, duration:.5, ease:'back.out(2.2)'}) リンクからチェック！
shape#downs(left: "296;343;390"; top: 1239px; width: 52px; height: 30px; path: tri,rot=180; background: $coral; opacity: .85; overlap: btn; in: {y:-20, opacity:0, duration:.3, ease:'power1.out', stagger:.08}; main: sine {y: 16, period: 0.9}) ×3
shape#cur(left: 760px; top: 1100px; width: 90px; height: 110px; path: cursor; background: #FFFFFF; border: 6px solid $ink; overlap: btn; in: {x:220, y:260, opacity:0, duration:.55, ease:'power2.out'})
```

```timeline.txt
#v2
cast n = "明るくエネルギッシュな20代の女性ナレーター、高めでクリアな声に微かな吐息、快活なテンポで親しみやすく誠実に語る"
silence head=0 tail=0

*** title
bgm music
se whoosh -8dB +100
@n: [silence:0.45s][>#t_chip -50][♪pop_high -4dB]{1分|いっぷん}でわかる、[>#t_title -60][>#t_gems][♪sparkle -2dB to=2.1s][>#t_sub +910]エフェクチュエーション。[silence:0.7s]

*** start
[>#subtitle]
se whoosh -8dB
@n: {hl}新しいこと{/}を始めたい。[<#c1a -140][♪whoosh -8dB -120][>#c1b -50][!#tint fill,#EFEDF5,duration=600]でも、計画が立たないから[br][!#c1b wiggle,2,duration=170,count=3,x=11][♪buzz -6dB]{ng}動けない{/}。[silence:0.95s]

*** term
se pop_dry -5dB
[!#tint fill,#FFF7EC,duration=600]
@n: そんなときに[!#c2 punch,1.045,duration=450][♪idea -3dB]{hl}役立つ{/}のが、[|][>#term -40][>#b2][!#tint fill,#FFF1E6,duration=600][♪sparkle -2dB to=2.1s][<#b2 +550]{hl}エフェクチュエーション{/}です。[silence:0.8s]

*** point
[!#tint fill,#FFF7EC,duration=600]
@n: [>#point][>#b3 +50][♪pop_high -4dB][<#b3 +600]{hl}ポイント{/}は、[|][!#point to,{y:-430, scale:.476, duration:.45, ease:'power3.inOut'} -300][>#c3a -80][♪whoosh -8dB -50][>#l3a +150]{ng}完璧な計画を待つ{/}のでは[>#c3a.ng][!#c3a.img filter,sat:0.15,duration=350][!#c3a to,{scale:.94, duration:.35}][♪buzz -6dB]なく、[|][>#arrow3 -150][>#c3b -50][♪pop_dry -5dB -50][>#l3b +200]{hl}今あるもの{/}から[>#c3b.ok][!#c3b to,{scale:1.04, duration:.5, ease:'sine.out'}][♪correct -3dB]始めること。[silence:0.85s]

*** means
@n: [>#tl[1]][♪pop_high -4dB]知識や[>#tl[2] -60][♪pop_dry -4dB]経験、[>#tl[3] -60][♪pop_high -4dB]スキル、[>#tl[4] -60][♪pop_dry -4dB]人脈を使って、[|][<#tl[*] -340][>#c4 -20][♪whoosh -8dB -100]{hl}まず小さく{/}[>#st4 -50][♪xylo -4dB]動いてみる。[silence:0.85s]

*** principles
se whoosh -8dB
@n: 失敗しても大きな[>#st5a -50][♪pop_dry -5dB]{hl}痛手{/}に[br]ならない{hl}範囲で試し{/}、[|][!#c5a to,{x:-70, y:40, rotation:-7, scale:.88, duration:.45, ease:'power2.out'} -100][!#c5a.img to,{opacity:.55, duration:.45} -100][<#tag5a -180][<#st5a -180][>#c5b -80][♪whoosh -8dB -120][>#tag5b +50][>#st5b +50][♪pop_dry -5dB +50]{hl}仲間{/}を巻き込み、[|][!#c5a to,{x:-110, y:70, rotation:-11, scale:.8, duration:.45, ease:'power2.out'} -100][!#c5b to,{x:70, y:40, rotation:7, scale:.88, duration:.45, ease:'power2.out'} -100][!#c5b.img to,{opacity:.55, duration:.45} -100][<#tag5b -180][<#st5b -180][>#c5c -80][♪whoosh -8dB -120][>#tag5c +50]思いがけない出来事も[br][>#st5c -350][>#b5][♪correct -3dB][<#b5 +550]{hl}チャンス{/}に変えていきます。[silence:0.95s]

*** pilot
se whoosh -8dB
@n: 未来を[>#st6a -50]{ng}予測{/}するのでは[>#c6a.ng][!#c6a.img filter,sat:0.2,duration=350][♪buzz -6dB]なく、[|][<#c6a -200][<#st6a -200][!#tint fill,#EEF7FF,duration=600 -100][>#c6b -120][♪whoosh -8dB -150][>#tag6 +100]{hl}行動しながら{/}[br]未来を[>#st6b -250][♪xylo -4dB]つくっていく。[silence:0.85s]

*** now
se whoosh -8dB
[!#tint fill,#F3F1F7,duration=600]
@n: 計画がないから[br][>#st7a -100]{ng}動けない{/}のでは[>#c7a.ng][!#c7a.img filter,sat:0.15,duration=350][♪buzz -6dB]なく、[|][<#c7a -200][<#st7a -200][!#tint fill,#EAF8F1,duration=600 -100][>#c7b -100][♪whoosh -8dB -100]手元にあるもので[>#st7b -300][!#c7b to,{y:-24, duration:.15, ease:'sine.out', repeat:3, yoyo:true}][♪correct -3dB]{hl}今すぐ動く{/}。[silence:1.0s]

*** recap
[!#tint fill,#FFF4DC,duration=600]
@n: [>#rc[*]][♪pop_high -5dB][♪pop_dry -5dB +160][♪pop_high -5dB +320][♪pop_dry -5dB +480][♪pop_high -5dB +640]これが、[|][>#rc_title -50][♪sparkle -2dB to=2.1s][!#rc[*] to,{y:-18, duration:.25, ease:'sine.inOut', repeat:1, yoyo:true, stagger:.08} +300]{hl}エフェクチュエーション{/}の[br]考え方です。[silence:0.85s]

*** cta
se whoosh -8dB
[!#tint fill,#FFF7EC,duration=600]
@n: 詳しい[>#k1.l -80][♪pop_high -4dB]{hl}解説記事{/}や[br][>#k2.l -80][♪pop_dry -4dB]{hl}対談本編動画{/}は、[|][>#ch1 -50][♪pop_high -5dB]{hl}概要欄{/}や[>#ch2 -50][♪pop_dry -5dB]{hl}コメント欄{/}の[>#btn -150]リンクから[br][>#cur -600][!#cur to,{scale:.82, duration:.12, repeat:1, yoyo:true} -20][!#btn punch,0.92,duration=400 -20][♪click][>#downs[*] +300][!#btn to,{scale:1.05, duration:.45, ease:'sine.inOut', repeat:-1, yoyo:true} +800][!#k1 main,float +800][!#k2 main,float +1100]チェックしてみてください！[silence:3.2s]
```

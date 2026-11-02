# data · supermarket-food-loss (hf 全力版の全量の写し — スーパーの食品ロス、半分は 3 つの棚から・生成りの地に白い板を下から差し込む 7 場面のデータ図解) — canvas 1080x1920

見せる作り: 全編の地 (生成りの縦グラデ・流れる点の格子・漂う 3 色のぼけ) と常設の上端 (白い丸札の題・店名・全編で伸びる進行線) と下端の出典・場面ごとに下から傾いて差し込む白い板 (番号札 + 題 + 補足札の def)・同じ板の中身を語で抜き差しして替える (店の絵と数字の札 → はかりの絵・数える合計・弾んで並ぶボトル 33 本)・7 本の横棒が重さ → 金額の切替で縮み行が入れ替わる (切替の札・黄の帯・順位の札・POINT の札)・曜日の縦棒と平均の破線と判子・2 時間戻る時計の針と前後の横棒とレシート・100 マスを語で塗る比べる 2 列とシャッターの閃光・番号つきのまとめの札 3 枚・白い札の字幕 (強調は朱)・音の層 (場面の頭の遷移音 + 語に結んだ効果音 57)

```design.txt
#v2
# 学ぶ作り: 明るい生成りの地 (縦グラデ + 動く点の格子 + 漂う 3 色のぼけ) の上に、常設の上端 (白い丸札の題・店名・全編で伸びる進行線) と下端の出典の 1 行を敷き、場面ごとに白い大きな板 1 枚を下から差し込む
# 板 = 番号札 + 題 + 右肩の補足札 + 破線の罫の def (board)。中身は板の内側の座標で組み、板の中の容器 (div#a → div#b) を語で抜き差しして同じ板の中身を替える (題も同じ語で入れ替える)
# 図は数字の語と同時に伸びる: 棚ごとの横棒 ×7 (語で上位 3 つに黄の帯が伸び、重さ → 金額の切替で棒の長さ (to scaleX・左を軸) と行の順 (to y) が動く)・曜日の縦棒 ×7・回る時計の針と前後の横棒・100 マスの点 ×2 を語で塗る・33 本のボトルが弾んで並ぶ
# hf d08 supermarket-food-loss (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3 (板の中身は板の左上からの相対)
canvas 1080x1920 bg=#FFF6E8
theme light
palette bg=#FFF6E8 ink=#2B2522 ink2=#6A5F57 line=#EFE2CF a=#E8502F ai=#C93C1F good=#24935C souzai=#F08A24 seika=#45A862 pan=#D9A23A nichi=#6FA8DC niku=#DF4F78 sengyo=#3A82C4 other=#B3AAA0 mk=#FFE066 card=#FFF7EA cardline=#F3DFC2 cbar=#F5C38F cmin=#7F9FBF
font "太く丸い丸ゴシック体の最も太いウェイト（Black）、親しみやすく明るい"
fonts e="太く丸い丸ゴシック体の太いウェイト（ExtraBold）"
fonts d="丸ゴシック体の太字ウェイト（Bold）"
sfx off
# hf の作り: 板の題・図の題・凡例は台詞より先に場面の頭に出す (見出し → 図 → 台詞が数字を読む)
lint off=spoiler
# hf の作り: 地は全編 1 枚の生成りのグラデと点の格子 (場面は板で替える・写真は店の 1 枚だけ)
lint off=same_picture
# hf の作り: 板の中の注記・凡例・目盛りは 13〜17 px (1080 の 20〜25 px)
lint off=small_text
# hf の作り: 図の色 (棚の 7 色・薄い地・罫) は場面ごとに直書き
lint off=palette_drift
# hf の作り: 地と板と図だけで絵の無い場面がある (曜日別・棚ごと)
lint off=text_only_cut
# hf の作り: 板の注記 (※…) は語の直後に出て 1〜2 秒で板ごと抜ける・POINT の札も場面の最後の 2 秒
lint off=flash_text
# hf の作り: 出現の音を語ごとに重ねる (ボトルの 3 連・時計の 4 連のクリック・判子 2 発)
lint off=se_dense
# hf の作り: 上端の店名は全編の常設 (台詞が店名を言う前から出ている)
lint off=all_at_once
# lint の読み違い: 金額の値 (vm) を重さの棒の上の位置に先置きする (棒は板でない)・行は to y で動くので静止の箱で POINT と重なって見える (covered_text)
lint off=empty_board
prompt_tail "Flat vector illustration with soft rounded shapes and clean simple shading, warm friendly palette (cream, leaf green, tomato red, wheat yellow), cheerful and appetizing. No text, no letters, no numbers, no logos, no labels, no price tags."
# 字幕の強調 (語の色) と図の文字の一部 (単位を小さく・語の色・下の帯)
run e { color: $ai }
run r { color: $a }
run mk { marker: $mk,36% }
run sm { font-size: 0.69em }
run ku { font-size: 0.45em }
run yu { font-size: 0.54em }
run k2 { font-size: 0.48em }
run u { font-size: 0.5em }
run u2 { font-size: 0.55em }
run p2 { font-size: 0.55em; color: $ink2; font-family: e }
run k3 { font-size: 0.54em; color: $ink2 }
run k5 { font-size: 0.62em }
run pu { font-size: 0.48em }
run yn { font-size: 0.5em }
run t9 { font-size: 0.45em }
run g { color: #2E8A4B }
run nr { color: #C23A62 }
run ra { color: $a }
run sw1 { color: #D9D0C4 }
run sw2 { color: $a }
run hb { color: $good; font-size: 1.35em }
run s21 { font-size: 0.59em; font-family: e }
run ea { color: $ai; font-family: e }
sound swoosh = "軽く短いシュッという風切り音"
sound scene = "場面が切り替わる柔らかいシュワッという短い遷移音"
sound pop = "軽くかわいいポンという短い音"
sound pophi = "高めで明るいポンという短い音"
sound perc = "ポコッと響く木の打楽器の短い一打"
sound kira = "キラリンと光るきらめきの効果音"
sound register = "レジのチーンという音"
sound click = "カチッという短いクリック音"
sound stamp = "判子をポンと押す音"
sound correct = "ピンポンという明るい正解音"
sound shutter = "スマホのカメラのシャッター音"
# 同じ食べ物の絵を 3 場面 (題の丸窓・実験の札・まとめの札) で使うので基準画像を 1 枚ずつ
image souzai = "[transparent]Japanese supermarket deli dishes (sozai) in clear plastic takeout packs: fried chicken karaage, golden croquettes, and a bento box with rice, egg and vegetables, arranged as a small tidy cluster filling the frame. Isolated object, centered."
image seika = "[transparent]A small tidy cluster of fresh produce: a green cabbage, red tomatoes, carrots, a bunch of bananas, an eggplant and a cucumber, filling the frame. Isolated object, centered."
image pan = "[transparent]A small tidy cluster of bakery bread: a Japanese melon pan, a croissant, a loaf of soft white shokupan and a baguette, filling the frame. Isolated object, centered."
image fridge = "[transparent]An open kitchen refrigerator stocked with milk, eggs, vegetables, tofu and leftover containers, and in the foreground a hand holding a smartphone up to take a photo of the fridge, the phone screen showing a preview of the shelves. Isolated scene, centered, filling the frame."
svg cart = """<svg viewBox="0 0 24 24"><path d="M3 5h3l2 10h10l2-7H7" fill="none" stroke="#FFFFFF" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="10" cy="19.5" r="1.8" fill="#FFFFFF"/><circle cx="17" cy="19.5" r="1.8" fill="#FFFFFF"/></svg>"""
svg bottle = """<svg viewBox="0 0 50 92"><rect x="17" y="1" width="16" height="9" rx="3" fill="#3A82C4"/><path d="M18 10 h14 v6 c0 4 9 8 9 18 v48 c0 5 -4 9 -9 9 h-14 c-5 0 -9 -4 -9 -9 v-48 c0 -10 9 -14 9 -18 z" fill="#D6ECFA" stroke="#3A82C4" stroke-width="3"/><rect x="11" y="44" width="28" height="18" rx="3" fill="#FFFFFF" stroke="#3A82C4" stroke-width="2"/><path d="M14 30 c3 -4 6 -6 8 -6" stroke="#FFFFFF" stroke-width="3" fill="none" stroke-linecap="round"/></svg>"""
svg sun = """<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="13" fill="#FFB627"/><g stroke="#FFB627" stroke-width="5" stroke-linecap="round"><line x1="32" y1="4" x2="32" y2="12"/><line x1="32" y1="52" x2="32" y2="60"/><line x1="4" y1="32" x2="12" y2="32"/><line x1="52" y1="32" x2="60" y2="32"/><line x1="12" y1="12" x2="18" y2="18"/><line x1="46" y1="46" x2="52" y2="52"/><line x1="12" y1="52" x2="18" y2="46"/><line x1="46" y1="18" x2="52" y2="12"/></g></svg>"""
svg sunset = """<svg viewBox="0 0 64 64"><path d="M14 42 a18 18 0 0 1 36 0 z" fill="#F2703F"/><g stroke="#F2703F" stroke-width="5" stroke-linecap="round"><line x1="32" y1="8" x2="32" y2="16"/><line x1="10" y1="22" x2="15" y2="27"/><line x1="54" y1="22" x2="49" y2="27"/></g><line x1="4" y1="44" x2="60" y2="44" stroke="#8D6E63" stroke-width="5" stroke-linecap="round"/><line x1="14" y1="54" x2="50" y2="54" stroke="#8D6E63" stroke-width="5" stroke-linecap="round"/></svg>"""
svg chev = """<svg viewBox="0 0 44 66"><path d="M8 6 L36 33 L8 60" fill="none" stroke="#2B2522" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
# 時計の盤 (白い円 + 12 の目盛り)・5 時から 7 時の赤い弧 (針は回すので別の箱)
svg clockface = """<svg viewBox="0 0 380 380"><circle cx="190" cy="190" r="176" fill="#FFFFFF" stroke="#2B2522" stroke-width="10"/><line x1="190" y1="54" x2="190" y2="30" stroke="#2B2522" stroke-width="8" stroke-linecap="round"/><line x1="263" y1="63.6" x2="270" y2="51.4" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/><line x1="316.4" y1="117" x2="328.6" y2="110" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/><line x1="326" y1="190" x2="350" y2="190" stroke="#2B2522" stroke-width="8" stroke-linecap="round"/><line x1="316.4" y1="263" x2="328.6" y2="270" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/><line x1="263" y1="316.4" x2="270" y2="328.6" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/><line x1="190" y1="326" x2="190" y2="350" stroke="#2B2522" stroke-width="8" stroke-linecap="round"/><line x1="117" y1="316.4" x2="110" y2="328.6" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/><line x1="63.6" y1="263" x2="51.4" y2="270" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/><line x1="54" y1="190" x2="30" y2="190" stroke="#2B2522" stroke-width="8" stroke-linecap="round"/><line x1="63.6" y1="117" x2="51.4" y2="110" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/><line x1="117" y1="63.6" x2="110" y2="51.4" stroke="#2B2522" stroke-width="5" stroke-linecap="round"/></svg>"""
svg clockarc = """<svg viewBox="0 0 380 380"><path d="M 278 342.4 A 176 176 0 0 1 102 342.4" fill="none" stroke="#E8502F" stroke-width="22" stroke-linecap="round"/></svg>"""
svg hhand = """<svg viewBox="0 0 380 380"><line x1="190" y1="190" x2="190" y2="96" stroke="#2B2522" stroke-width="16.5" stroke-linecap="round"/></svg>"""
svg mhand = """<svg viewBox="0 0 380 380"><line x1="190" y1="190" x2="190" y2="51" stroke="#2B2522" stroke-width="10.5" stroke-linecap="round"/></svg>"""
p { color: $ink }
# 曲: 頭の 0.3 秒と締めの余韻だけ前に出す
bgm#music(keys: "0:+7|320ms:+7|620ms:0|end-1.6s:0|end-1.1s:+6"; fade: 0,1600) 明るく軽やかなアコースティックのポップ、木琴とウクレレと手拍子、暮らしの情報やキッチンの解説向け、主旋律は控えめ
# 字幕: 下の帯の中央に白い札 (黒の縁 + 下に硬い影)・強調の語は朱 (台詞の {e})・札は文 (句は [|] で切り、文を跨ぐ札は [||])
subtitle.hug(left: 30px; bottom: 372px; width: 1020px; wrap: comma,30; font-size: 42px; font-family: e; line-height: 1.38; color: $ink; background: #FFFFFF; border: 3px solid $ink; border-radius: 26px; box-shadow: 0px 6px 0px $ink; padding: 16px 28px 18px 28px; unit: sentence; lead: 0ms; in: {y:14, opacity:0, duration:.16, ease:'power2.out'})

# 全編の地: 縦グラデ・点の格子 (全編で 27 px 上へ流れる)・3 色のぼけ (全編でゆっくり漂う)
div#bg_base(inset: 0; background: linear(#FFF9EF,#FFF1DC,180); z-index: back; in: none)
div#dots(left: -40px; top: -40px; width: 1161px; height: 2001px; pattern: dots,27,#96693221; z-index: back; in: none; main: ramp {y: -40})
div#blob1(left: -380px; top: -260px; width: 900px; height: 900px; background: radial(#FFC4788C,#FFC47800@68%,50%,50%); z-index: back; in: none; main: ramp {x: 120, y: 80, ease: 'sine.inOut'})
div#blob2(left: 520px; top: 760px; width: 980px; height: 980px; background: radial(#96D6A073,#96D6A000@68%,50%,50%); z-index: back; in: none; main: ramp {x: -140, y: -120, ease: 'sine.inOut'})
div#blob3(left: -260px; top: 1320px; width: 760px; height: 760px; background: radial(#FFAA9666,#FFAA9600@68%,50%,50%); z-index: back; in: none; main: ramp {x: 160, y: -60, ease: 'sine.inOut'})
# 常設の上端: 白い丸札の題 (朱の丸 + カート) と右の店名・その下に全編で伸びる進行線・下端の出典
div#brand(left: 48px; top: 69px; width: 393px; height: 66px; background: #FFFFFF; border: 3px solid $ink; border-radius: 148px; box-shadow: 0px 4px 0px $ink; in: {y:-30, opacity:0, duration:.5, ease:'power3.out'})
  div#dot(left: 9px; cy: 50%; width: 40px; height: 40px; border-radius: 148px; background: $a)
  svg#cart(left: 16px; cy: 50%; width: 24px; height: 24px; part: cart)
  p#t(left: 63px; cy: 50%; font-size: 30px; letter-spacing: .02em; white-space: nowrap) 食品ロスを数字で見る
p#store(right: 48px; cy: 102px; font-size: 26px; font-family: e; line-height: 1.25; text-align: right; color: $ink2; in: {y:-30, opacity:0, duration:.5, ease:'power3.out'}) まるみ屋 ひばり台店[br]（架空の地域スーパー）
div#ptrack(left: 48px; top: 164px; width: 984px; height: 10px; border-radius: 4px; background: #2B25221A; in: none)
progress#pbar(left: 48px; top: 164px; width: 984px; height: 10px; border-radius: 4px; background: linear(#F08A24,#E8502F,90); until: end; overlap: ptrack)
p#foot(cx: 540px; top: 1578px; font-size: 24px; font-family: d; color: $ink2; in: none) ※架空の店舗「まるみ屋 ひばり台店」の4週間の記録より

# 板: 白の角丸 + 淡い縁 + 柔らかい影・下から傾いて差し込み (y 1167・2.5°)、場面の終わりに奥へ縮んで消える
def board(n, t) = div(left: 48px; top: 212px; width: 984px; height: 1100px; background: #FFFFFF; border-radius: 44px; border: 3px solid #F1E3CF; box-shadow: 0px 26px 60px #8C5A2829; in: {y:1750, rotation:2.5, duration:.55, ease:'power3.out'}; out: {y:-40, scale:.92, opacity:0, duration:.45, ease:'power1.in'})
  p#tag(z-index: front; left: 40px; cy: 57px; font-size: 28px; line-height: 1; color: #FFFFFF; background: $a; border-radius: 18px; padding: 10px 16px 12px 16px; content: {n})
  p#ttl(z-index: front; left: .tag.right+20; cy: 57px; font-size: 46px; line-height: 1.1; white-space: nowrap; content: {t})
  shape#hr(left: 0px; top: 114px; width: 984px; height: 3px; path: line_h; border: 3px solid $line; dash: 6,6)
# 板の右肩の補足札
def bsub(t) = p(right: 40px; cy: 57px; font-size: 26px; font-family: e; color: $ink2; background: #FFF3E2; border-radius: 148px; padding: 10px 20px 10px 20px; white-space: nowrap; content: {t})

# 題: 黒の小札 → 2 行の大見出し (「半分」が拡大から着地・「3つの棚」に黄の帯が伸びる) → 灰色で薄く並ぶ 3 つの丸窓が語で色づいて弾む
section#title(out: {y:-60, scale:.94, opacity:0, duration:.45, ease:'power1.in'})
p#kick(cx: 540px; top: 268px; font-size: 32px; font-family: e; color: #FFFFFF; background: $ink; border-radius: 148px; padding: 12px 30px 14px 30px; in: {y:-24, opacity:0, duration:.4, ease:'power3.out'}) 4週間 × 棚ごとの廃棄データ
p#l1(cx: 540px; top: 372px; font-size: 86px; in: {y:40, opacity:0, duration:.5, ease:'power3.out'}) スーパーの食品ロス、
p#l2(cx: 540px; top: 486px; font-size: 176px; line-height: 1; in: {scale:1.6, opacity:0, duration:.42, ease:'back.out(1.8)'}) {r}半分{/}は
p#l3(cx: 540px; top: 690px; font-size: 150px; line-height: 1; in: {y:50, opacity:0, duration:.42, ease:'power3.out'}) {mk}3つの棚{/}{sm}から{/}
# 丸窓の札 (白い円 + 色の輪 + 透過の絵 + 色の名札)・半分の濃さで灰色に置き、語で濃く色づく
def badge(t, c, lc, im) = div(width: 276px; height: 366px; opacity: .5; in: {y:50, opacity:0, duration:.5, ease:'power3.out', stagger: {each: .1}})
  div#ring(left: 0px; top: 0px; width: 276px; height: 276px; border-radius: 148px; background: #FFFFFF; border: 8px solid {c}; box-shadow: 0px 14px 30px #8C5A282E)
  img#img(cx: 138px; cy: 138px; width: 226px; height: 226px; object-fit: contain; filter: saturate(0); main: none; content: {im})
  p#lb(cx: 138px; top: 294px; font-size: 46px; color: #FFFFFF; background: {lc}; border-radius: 148px; padding: 6px 28px 10px 28px; content: {t})
badge#bd(left: "47;268;489"; top: 930px; t: "惣菜;青果;パン"; c: "$souzai;$seika;$pan"; lc: "#B9560B;#2B7D45;#9A6A12"; im: "@souzai;@seika;@pan") ×3

# 01 調査の舞台: 店の絵が上から開き、店名の札と 3 つの数字の札 → 同じ板の中身を左へ抜き「4週間の廃棄」へ (はかりの絵・数える合計・売値・1 日あたり = ボトル 33 本)
section#stage
board#st(n: "01"; t: "調査の舞台")
  p#ttl(out: {y:-20, opacity:0, duration:.2})
  p#t2(left: .tag.right+20; cy: 57px; font-size: 46px; line-height: 1.1; white-space: nowrap; in: {y:20, opacity:0, duration:.3}) 4週間の廃棄
  bsub#sub(out: {opacity:0, duration:.25}) 架空の地域スーパー
  div#a(inset: 0; out: {x:-60, opacity:0, duration:.24, ease:'power2.in'})
    img#photo(left: 40px; top: 140px; width: 904px; height: 603px; border-radius: 30px; delay: 200ms; in: wipe {dir: 'down', duration: 0.7, ease: 'power3.out'}; main: kb {scale: [1.12, 1], ease:'sine.out'}; subject: top 65%; room: bottom 30%) A cozy neighborhood supermarket storefront on a quiet street in a Japanese residential area: a single-story shop with a green-and-cream striped awning, large glass windows showing produce and bread shelves, a couple of shoppers with eco bags, a parked bicycle and potted plants, soft morning light. The shop fills the whole frame edge to edge; the lower-left quarter is plain pavement for a name plate.
    div#plate(left: 70px; top: 586px; width: 558px; height: 136px; background: #FFFFFF; border-radius: 22px; box-shadow: 0px 10px 24px #00000029; overlap: st.a.photo; in: {x:-40, opacity:0, duration:.45, ease:'back.out(1.6)'})
      p#b(left: 28px; top: 16px; font-size: 54px; line-height: 1.1; white-space: nowrap) まるみ屋 ひばり台店
      p#s(left: 28px; top: 84px; font-size: 26px; font-family: e; color: $ink2; white-space: nowrap) 住宅街にある地域スーパー（架空）
    # 数字の札 ×3 (題 + 大きい数字 + 小さい単位)
    div#chips(left: "27;233;439"; top: 772px; width: 286px; height: 176px; background: $card; border: 3px solid $cardline; border-radius: 26px; in: {y:40, opacity:0, duration:.4, ease:'back.out(1.6)', stagger: {each: .15}}) ×3
      p#l(left: 22px; top: 20px; font-size: 26px; font-family: e; color: $ink2) 売場面積;1日の来店;記録した期間
      p#v(left: 22px; top: 69px; font-size: 56px; line-height: 1.15; white-space: nowrap) 1,200{u}m²{/};約2,100{u}人{/};28{u}日（4週間）{/}
    p#note(left: 40px; top: 978px; font-size: 26px; font-family: d; color: $ink2; in: {opacity:0, duration:.4}) ※棚ごとに毎日、はかりで廃棄の重さを記録
  div#b(inset: 0; in: {x:60, opacity:0, duration:.4, ease:'power3.out'})
    img#scale(left: 26px; top: 146px; width: 390px; height: 390px; object-fit: contain; main: none; in: {y:30, scale:.9, opacity:0, duration:.6, ease:'back.out(1.6)'}) [transparent]A white digital platform scale with a clear plastic crate on it, the crate filled with unsold food: wrapped deli bento packs, bread rolls, a cabbage and tomatoes. The scale display is blank. Isolated object, centered, filling the frame.
    p#lbl(left: 440px; top: 168px; font-size: 30px; font-family: e; color: $ink2) 廃棄の合計（28日間）
    # 合計は 0 で出て、語で 1,840 まで数える
    p#total(left: 432px; top: 219px; font-size: 132px; line-height: 1; letter-spacing: -.02em; white-space: nowrap) [count:1,840 start=0 ms=1000 ease=cubic_out]{ku}kg{/}
    div#yen(left: 440px; top: 392px; width: 510px; height: 120px; in: {y:30, opacity:0, duration:.4, ease:'back.out(1.6)'})
      p#l(left: 0px; top: 0px; font-size: 28px; font-family: e; color: $ink2) 売値で
      p#v(left: 0px; top: 39px; font-size: 74px; line-height: 1.12; color: $a; white-space: nowrap) 151万8,500{yu}円分{/}
    p#note1(left: 440px; top: 518px; font-size: 22px; font-family: d; color: $ink2; in: {opacity:0, duration:.3}) ※売値で換算した金額
    shape#rule(left: 40px; top: 566px; width: 904px; height: 3px; path: line_h; border: 3px solid $line; dash: 6,6; in: {scaleX:0, duration:.4, pivot:'left'})
    # ボトル 33 本 (11 列 × 3 段・下を軸に弾んで 52 ms ずつ)
    svg#bt(left: "61.3;111.3;161.3;211.3;261.3;311.3;361.3;411.3;461.3;511.3;561.3;61.3;111.3;161.3;211.3;261.3;311.3;361.3;411.3;461.3;511.3;561.3;61.3;111.3;161.3;211.3;261.3;311.3;361.3;411.3;461.3;511.3;561.3"; top: "485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3"; width: 50px; height: 92px; part: bottle; in: {scale:0, y:24, opacity:0, duration:.32, ease:'back.out(2.2)', pivot:'bottom', stagger: {each: .052}}) ×33
    div#perday(left: 40px; top: 592px; width: 330px; height: 138px; in: {y:30, opacity:0, duration:.4, ease:'back.out(1.6)'})
      p#l(left: 0px; top: 0px; font-size: 32px; font-family: e; color: $ink2) 1日あたり
      p#v(left: 0px; top: 52px; font-size: 96px; line-height: 1; white-space: nowrap) 約66{k2}kg{/}
    p#eq(left: 384px; top: 640px; font-size: 72px; color: $ink2; in: {scale:.5, opacity:0, duration:.3}) ＝
    p#bv(left: 470px; top: 645px; font-size: 96px; line-height: 1; color: $sengyo; white-space: nowrap; in: {scale:.5, opacity:0, duration:.4, ease:'back.out(2)', pivot:'0% 70%'}) 33{k2}本分{/}
    p#bl(left: 470px; top: 592px; font-size: 32px; font-family: e; color: $ink2; in: {y:16, opacity:0, duration:.3}) 2Lペットボトル
    p#note2(left: 40px; top: 1046px; width: 904px; text-align: center; font-size: 22px; font-family: d; color: $ink2; in: {opacity:0, duration:.4}) ※1,840kg ÷ 28日 ≒ 66kg（2Lのボトル1本＝約2kgとして換算）

# 02 棚ごとの廃棄: 7 本の横棒 (重さ) → 上位 3 つに黄の帯 → 3 つで 50.5% の帯 → 切替の札で金額へ (棒が縮み行が入れ替わり、順位の札・1kg あたりの札・POINT の札)
section#shelves
# 棚の行: 色の点 + 名 (+ 小さい補足) + 棒 (幅 = 値 ÷ 最大 × 304 px) + 棒の右の値 (重さ) / 金額の値
def shelf(nm, sub, c, bw, v, mx, mv) = div(width: 984px; height: 96px; in: none)
  shape#dot(left: 44px; top: 28px; width: 20px; height: 20px; border-radius: 50%; background: {c})
  p#nm(left: 74px; top: 16px; font-size: 42px; line-height: 1.05; content: {nm})
  p#sub(left: 75px; top: 64px; font-size: 20px; font-family: e; color: $ink2; white-space: nowrap; content: {sub})
  div#bar(left: 252px; top: 21px; width: {bw}; height: 52px; border-radius: 14px; background: {c}; in: {scaleX:0, duration:.7, ease:'expo.out', pivot:'left'})
  p#vw(left: .bar.right+16; top: 20px; font-size: 44px; line-height: 1; white-space: nowrap; in: {x:-150, opacity:0, duration:.7, ease:'expo.out'}; out: {opacity:0, duration:.15}; content: {v})
  p#vm(left: {mx}; top: 20px; font-size: 44px; line-height: 1; white-space: nowrap; in: {opacity:0, duration:.25}; content: {mv})
board#sh(n: "02"; t: "棚ごとの廃棄")
  # 重さ / 金額の切替の札 (黒い丸の knob が右へ滑る)・lint は knob を地と見ずに low_contrast を出す (白い字は黒い knob の上)
  div#tg(right: 40px; cy: 57px; width: 300px; height: 66px; background: #F4ECE1; border: 3px solid $ink; border-radius: 148px)
    div#knob(left: 3px; top: 3px; width: 144px; height: 54px; border-radius: 148px; background: $ink)
    p#w(left: 0px; cy: 50%; width: 147px; text-align: center; font-size: 30px; color: #FFFFFF) 重さ
    p#m(left: 147px; cy: 50%; width: 147px; text-align: center; font-size: 30px) 金額
  div#sw(left: 40px; top: 141px; width: 40px; height: 24px; border-radius: 8px; background: #FFF0B3; border: 2px solid #F4D65A; out: {opacity:0, duration:.2})
  p#lg(left: 88px; cy: 153px; font-size: 26px; font-family: e; color: $ink2; out: {opacity:0, duration:.2}) 上位3つの棚
  p#uw(right: 40px; cy: 153px; font-size: 26px; font-family: e; color: $ink2; white-space: nowrap; out: {opacity:0, duration:.2}) 単位：kg（全体に占める割合）
  p#um(right: 40px; cy: 153px; font-size: 26px; font-family: e; color: $ink2; white-space: nowrap; in: {opacity:0, duration:.2}) 単位：万円（売値で換算）／順位は「その他」を除く
  # 上位 3 つの黄の帯 (語ごとに 1 行ずつ下へ伸びる)
  # 帯は 1 行 64 px の箱 3 枚 (2・3 枚目は上の箱の角の丸みを 16 px 覆って続く 1 本に見せる)
  div#band(left: 22px; top: 186px; width: 940px; height: 288px; in: none; out: {opacity:0, duration:.25})
    div#b1(left: 0px; top: 0px; width: 940px; height: 96px; border-radius: 24px; background: #FFF3C4; in: {scaleY:0, opacity:0, duration:.3, ease:'power2.out', pivot:'top'})
    div#b2(left: 0px; top: 72px; width: 940px; height: 120px; border-radius: 0px 0px 24px 24px; background: #FFF3C4; overlap: sh.band.b1; in: {scaleY:0, opacity:0, duration:.3, ease:'power2.out', pivot:'top'})
    div#b3(left: 0px; top: 168px; width: 940px; height: 120px; border-radius: 0px 0px 24px 24px; background: #FFF3C4; overlap: sh.band.b2; in: {scaleY:0, opacity:0, duration:.3, ease:'power2.out', pivot:'top'})
  group#rows(left: 0px; top: 186px; width: 984px; height: 672px; display: flex; flex-direction: column; gap: 0px)
    shelf#r(flex: 1; width: 984px; nm: "惣菜;青果;パン;日配;精肉;鮮魚;その他"; sub: ";;;豆腐・乳製品・麺;;;加工食品・菓子など"; c: "$souzai;$seika;$pan;$nichi;$niku;$sengyo;$other"; bw: "304;205;148.5;134.3;127.3;113.1;268.7"; v: "430{u2}kg{/} {p2}23.4%{/};290{u2}kg{/} {p2}15.8%{/};210{u2}kg{/} {p2}11.4%{/};190{u2}kg{/} {p2}10.3%{/};180{u2}kg{/} {p2}9.8%{/};160{u2}kg{/} {p2}8.7%{/};380{u2}kg{/} {p2}20.7%{/}"; mx: "483;235;301;234;353;323;301"; mv: "47.3{u2}万円{/};8.7{u2}万円{/};18.9{u2}万円{/};8.6{u2}万円{/};27.0{u2}万円{/};22.4{u2}万円{/};19.0{u2}万円{/}") ×7
  # 順位の変化の札 (行が入れ替わった後の位置に)
  p#rk1(right: 36px; top: 306px; font-size: 28px; color: #FFFFFF; background: #C23A62; border-radius: 148px; padding: 6px 16px 8px 16px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2)'}) ▲ 5位→2位
  p#rk2(right: 36px; top: 594px; font-size: 28px; color: #FFFFFF; background: #6D7F8F; border-radius: 148px; padding: 6px 16px 8px 16px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2)'}) ▼ 2位→5位
  # 重さの合計の段: 3 つで 50.5% (数える)・930kg・3 色の積み上げの帯と半分の印
  div#sumw(left: 40px; top: 868px; width: 904px; height: 204px; in: {y:40, opacity:0, duration:.4, ease:'power3.out'}; out: {y:-20, opacity:0, duration:.25})
    p#t1(left: 0px; top: 4px; font-size: 32px; font-family: e) 惣菜・青果・パンの3つで
    p#pct(left: 0px; top: 46px; font-size: 116px; line-height: 1; color: $a; white-space: nowrap) [count:50.5 start=0 ms=800 ease=cubic_out]{pu}%{/}
    p#kg(left: 470px; top: 70px; font-size: 56px; line-height: 1; white-space: nowrap) 930{k3}kg ／ 全体 1,840kg{/}
    div#stk(left: 0px; top: 168px; width: 904px; height: 22px; border-radius: 10px; background: #ECE4D8)
    # 3 色の積み上げ (左から 1 本の帯として開く = 3 枚を続けて wipe)
    div#s1(left: 0px; top: 168px; width: 212px; height: 22px; border-radius: 10px 0px 0px 10px; background: $souzai; in: wipe {dir: 'right', duration: 0.33, ease: 'none'})
    div#s2(left: 212px; top: 168px; width: 142px; height: 22px; background: $seika; delay: 330ms; in: wipe {dir: 'right', duration: 0.22, ease: 'none'})
    div#s3(left: 354px; top: 168px; width: 104px; height: 22px; background: $pan; delay: 550ms; in: wipe {dir: 'right', duration: 0.15, ease: 'power2.out'})
    div#half(left: 452px; top: 154px; width: 4px; height: 50px; border-radius: 3px; background: $ink)
  # 金額の段: 1kg あたりの売値の札 ×3 が語ごとに弾む
  div#summ(left: 40px; top: 868px; width: 904px; height: 190px; in: {opacity:0, duration:.3})
    p#t1(left: 0px; top: 0px; font-size: 30px; font-family: e; in: {y:20, duration:.3}) 1kgあたりの売値
    div#pc(left: "0;205;410"; top: 46px; width: 290px; height: 100px; background: #FFFFFF; border: "3px solid $niku;3px solid $souzai;3px solid $seika"; border-radius: 22px; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) ×3
      p#n(left: 18px; cy: 50%; font-size: 32px; color: "$niku;#C96A10;#2E8A4B") 精肉;惣菜;青果
      p#v(left: .n.right+12; cy: 50%; font-size: 52px; white-space: nowrap) 1,500{yn}円{/};1,100{yn}円{/};300{yn}円{/}
    p#note(left: 0px; top: 158px; font-size: 22px; font-family: d; color: $ink2; in: {opacity:0, duration:.3}) ※惣菜・青果・パンの3つは、金額では74.9万円（49.3%）
  # POINT の札 (黒の縁 + 硬い影・少し傾けて弾む)
  div#point(left: 622px; top: 652px; width: 336px; height: 198px; background: #FFFFFF; border: 4px solid $ink; border-radius: 26px; box-shadow: 0px 8px 0px $ink; transform: rotate(-2deg); in: {scale:.6, rotation:-4, opacity:0, duration:.45, ease:'back.out(1.8)'})
    p#tag(left: 22px; top: 16px; font-size: 24px; background: $mk; border-radius: 10px; padding: 4px 12px 6px 12px) POINT
    p#t(left: 22px; top: 58px; font-size: 28px; font-family: e; line-height: 1.42; white-space: nowrap) 重さの2位は {g}青果{/}[br]金額の2位は {nr}精肉{/}[br]大きい棚が入れ替わる

# 03 曜日別: 目盛りの上に 7 本の縦棒 (日曜だけ朱・火曜は青灰) と平均の破線 → 最多 / 最少の札 → 約1.8倍 → 昼 → 夕方の札と判子
section#days
board#dy(n: "03"; t: "曜日別・1日の廃棄")
  bsub#sub 4週の平均
  shape#gl(left: 100px; top: "200;277;353;430"; width: 850px; height: 3px; path: line_h; border: 2px solid #EEE3D4) ×4
  div#axis(left: 100px; top: 759px; width: 850px; height: 3px; background: #CFC3B3)
  p#yl(left: 30px; top: "497;343;190"; width: 56px; text-align: right; font-size: 22px; font-family: e; color: $ink2) ×3 0;50;100
  p#ykg(left: 20px; top: 246px; width: 80px; text-align: right; font-size: 22px; font-family: e; color: $ink2) kg
  # 縦棒 (高さ = kg × 3.07 px・下を軸に 90 ms ずつ伸びる)
  div#col(left: "81;161.7;242.3;323;403.7;484.3;565"; top: "316.6;341.1;328.8;331.9;313.5;292;212.3"; width: 86px; height: "190.1;165.6;177.9;174.8;193.2;214.7;294.4"; border-radius: 16px 16px 6px 6px; background: "$cbar;$cmin;$cbar;$cbar;$cbar;$cbar;$a"; in: {scaleY:0, duration:.55, ease:'expo.out', pivot:'bottom', stagger: {each: .09}}) ×7
  p#cv(left: "63;143.7;224.3;305;385.7;466.3;547"; top: "324.6;349.1;336.8;339.9;321.5;300;220.3"; width: 140px; text-align: center; font-size: "21;21;21;21;21;21;29"; color: "$ink;$ink;$ink;$ink;$ink;$ink;#FFFFFF"; white-space: nowrap; in: {y:14, opacity:0, duration:.3, stagger: {each: .09}}) ×7 62{k5}kg{/};54{k5}kg{/};58{k5}kg{/};57{k5}kg{/};63{k5}kg{/};70{k5}kg{/};96{k5}kg{/}
  p#day(left: "76.3;157;237.7;318.3;399;479.7;560.3"; top: 774px; width: 100px; text-align: center; font-size: 38px; color: "$ink;$ink;$ink;$ink;$ink;$ink;$ai") ×7 月;火;水;木;金;土;日
  shape#avg(left: 104px; top: 456px; width: 846px; height: 4px; path: line_h; border: 4px solid #8D837A; dash: 8,6; overlap: dy.col; in: {scaleX:0, duration:.5, pivot:'left'})
  p#avgl(left: 10px; top: 428px; width: 92px; text-align: right; font-size: 21px; line-height: 1.2; color: $ink2; in: {opacity:0, duration:.3}) 平均[br]約66kg
  p#tmax(left: 854px; top: 268px; font-size: 24px; color: #FFFFFF; background: $ai; border-radius: 148px; padding: 4px 14px 6px 14px; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) 最多
  p#tmin(left: 249px; top: 465px; font-size: 24px; color: #FFFFFF; background: #5D7F9F; border-radius: 148px; padding: 4px 14px 6px 14px; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) 最少
  div#bai(left: 470px; top: 236px; width: 330px; height: 123px; in: {y:30, opacity:0, duration:.4, ease:'back.out(1.8)'})
    p#l(right: 0px; top: 0px; font-size: 26px; font-family: e; color: $ink2; white-space: nowrap) 日曜は火曜（54kg）の
    p#v(right: 0px; top: 38px; font-size: 84px; line-height: 1; color: $a; white-space: nowrap) 約1.8倍
  # 理由の札 ×2 (icon + 題 + 2 行)・間の矢印・夕方の札に判子
  div#w(left: "21;356"; top: 852px; width: 418px; height: 222px; border-radius: 28px; background: "#FFF6DF;#FFE9E0"; in: {y:60, opacity:0, duration:.45, ease:'back.out(1.6)'}) ×2
    svg#ic(left: 22px; top: 20px; width: 64px; height: 64px; part: "sun;sunset")
    p#h(left: 98px; top: 26px; font-size: 40px) 昼;夕方
    p#t(left: 24px; top: 104px; font-size: 32px; font-family: e; line-height: 1.38) 客足に合わせて[br]惣菜を多めに作る;客が早く引けて[br]売れ残る
  svg#arw(left: 470px; top: 930px; width: 44px; height: 66px; part: chev; in: {x:-20, opacity:0, duration:.3})
  div#stamp(left: 796px; top: 916px; width: 146px; height: 146px; border-radius: 148px; border: 6px solid $a; background: #FFFFFFD9; transform: rotate(-14deg); overlap: dy.w; in: {scale:2.2, rotation:-16, opacity:0, duration:.3, ease:'power4.in'})
    p#t(cx: 50%; cy: 50%; font-size: 30px; line-height: 1.1; text-align: center; color: $a) 売れ[br]残り

# 04 実験: 時計の針が 2 時間戻り 19:00 に線 → 17:00 → 半額シールを判子で 2 枚 → 同じ板を前後の横棒・−93kg の帯・レシートの差し引きへ入れ替える
section#exp
board#ex(n: "04"; t: "実験：値引きを2時間早く")
  bsub#sub 2週間
  div#a(inset: 0; out: {y:-40, opacity:0, duration:.24, ease:'power2.in'})
    group#clk(left: 58px; top: 160px; width: 380px; height: 380px; delay: 100ms; in: {scale:.7, opacity:0, duration:.5, ease:'back.out(1.6)'})
      svg#face(left: 0px; top: 0px; width: 380px; height: 380px; part: clockface)
      svg#arc(left: 0px; top: 0px; width: 380px; height: 380px; part: clockarc; in: {opacity:0, duration:.3})
      # 針は時計と同じ 253 px 四方の svg (中心 = 時計の中心) に描き、既定の中心軸で回す (時針 210° = 7 時)
      svg#hh(left: 0px; top: 0px; width: 380px; height: 380px; part: hhand; transform: rotate(210deg))
      svg#mh(left: 0px; top: 0px; width: 380px; height: 380px; part: mhand)
      shape#cdot(left: 176px; top: 176px; width: 28px; height: 28px; border-radius: 50%; background: $a)
    p#tl(left: 476px; top: 170px; font-size: 30px; font-family: e; color: $ink2; delay: 200ms; in: {opacity:0, duration:.3}) 半額シールを貼る時刻
    p#t19(left: 476px; top: 222px; font-size: 74px; color: #A79C92; delay: 300ms; in: {x:30, opacity:0, duration:.35}) 19:00
    p#t17(left: 476px; top: 322px; font-size: 128px; line-height: 1; color: $a; in: {y:40, opacity:0, duration:.4, ease:'back.out(1.8)'}) 17:00
    p#early(left: 480px; top: 470px; font-size: 32px; background: $mk; border-radius: 14px; padding: 6px 16px 8px 16px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2)'}) 2時間 早く！
    # 商品の札 ×2 (絵 + 名)・右上に半額シールを判子で
    div#it(left: "27;350"; top: 590px; width: 420px; height: 420px; border-radius: 30px; background: $card; border: 3px solid $cardline; in: {y:60, opacity:0, duration:.45, ease:'back.out(1.6)', stagger: {each: .15}}) ×2
      img#img(left: 60px; top: 30px; width: 300px; height: 300px; object-fit: contain; main: none; content: "@souzai;@pan")
      p#t(cx: 50%; bottom: 22px; font-size: 44px) 惣菜;パン
      div#st(left: 268px; top: 20px; width: 150px; height: 150px; border-radius: 148px; background: #FFD84D; border: 6px solid $a; box-shadow: 0px 6px 0px #0000001F; transform: rotate(-12deg); in: {scale:2.4, rotation:42, opacity:0, duration:.22, ease:'power4.in'})
        p#t(cx: 50%; cy: 50%; font-size: 50px; line-height: 1; color: $ai) 半額
    p#notea(left: 40px; top: 1036px; font-size: 26px; font-family: d; color: $ink2; in: {opacity:0, duration:.3}) ※試したのは2週間。直前の2週間と比べました
  div#b(inset: 0; in: none)
    div#strip(left: 40px; top: 136px; width: 904px; height: 92px; border-radius: 24px; background: $card; border: 3px solid $cardline; in: {y:-30, opacity:0, duration:.35, ease:'power3.out'})
      div#mini(left: 24px; cy: 50%; width: 62px; height: 62px; border-radius: 148px; background: #FFD84D; border: 4px solid $a)
        p#t(cx: 50%; cy: 50%; font-size: 20px; color: $ai) 半額
      p#b(left: 104px; cy: 50%; font-size: 34px; white-space: nowrap) シールを {ra}19:00 → 17:00{/} に
      p#s(right: 24px; cy: 50%; font-size: 26px; font-family: e; color: $ink2; white-space: nowrap) 直前の2週間と比較
    div#res(left: 40px; top: 250px; width: 904px; height: 440px)
      p#rt(left: 0px; top: 0px; font-size: 32px; in: {opacity:0, duration:.3}) 廃棄の重さ（各2週間）
      p#lg(right: 0px; top: 4px; font-size: 22px; font-family: e; color: $ink2; white-space: nowrap; in: {opacity:0, duration:.3}) {sw1}■{/} 直前　{sw2}■{/} 実験中
      p#nm1(left: 0px; top: 86px; font-size: 42px) 惣菜
      div#b1(left: 110px; top: 68px; width: 430px; height: 40px; border-radius: 10px; background: #D9D0C4; in: {scaleX:0, duration:.5, ease:'expo.out', pivot:'left'})
      p#v1(left: 556px; cy: 88px; font-size: 30px; in: {opacity:0, duration:.3}) 215kg
      div#b2(left: 110px; top: 117px; width: 296px; height: 40px; border-radius: 10px; background: $souzai; in: {scaleX:0, duration:.6, ease:'expo.out', pivot:'left'})
      p#v2(left: 422px; cy: 137px; font-size: 30px; in: {opacity:0, duration:.3}) 148kg
      p#d1(right: 0px; top: 78px; font-size: 54px; color: $good; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) −31%
      p#nm2(left: 0px; top: 214px; font-size: 42px) パン
      div#b3(left: 110px; top: 196px; width: 210px; height: 40px; border-radius: 10px; background: #D9D0C4; in: {scaleX:0, duration:.5, ease:'expo.out', pivot:'left'})
      p#v3(left: 336px; cy: 217px; font-size: 30px; in: {opacity:0, duration:.3}) 105kg
      div#b4(left: 110px; top: 246px; width: 158px; height: 40px; border-radius: 10px; background: $pan; in: {scaleX:0, duration:.6, ease:'expo.out', pivot:'left'})
      p#v4(left: 284px; cy: 266px; font-size: 30px; in: {opacity:0, duration:.3}) 79kg
      p#d2(right: 0px; top: 207px; font-size: 54px; color: $good; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) −25%
      div#tot(left: 0px; top: 312px; width: 904px; height: 120px; border-radius: 26px; background: #EAF6EE; in: {y:30, opacity:0, duration:.4, ease:'back.out(1.6)'})
        p#s(left: 26px; cy: 50%; font-size: 30px; font-family: e; white-space: nowrap) 2つ合わせて 320kg → 227kg
        p#b(right: 26px; cy: 50%; font-size: 80px; line-height: 1; color: $good; white-space: nowrap) −93{t9}kg（−29%）{/}
    # レシート (破線の枠・2 行の増減・緑の差し引きの帯)
    div#rc(left: 40px; top: 714px; width: 904px; height: 360px; border-radius: 22px; background: #FFFDF8; in: {y:50, opacity:0, duration:.45, ease:'power3.out'})
      shape#frame(left: 0px; top: 0px; width: 904px; height: 360px; path: rect,r=0.06; background: none; border: 3px solid #D8C7AE; dash: 6,5)
      p#h1(left: 34px; top: 24px; font-size: 30px; color: $ink2) お金で見ると（2週間）
      p#h2(right: 34px; top: 24px; font-size: 30px; color: $ink2) 売値換算
      div#l1(left: 34px; top: 76px; width: 836px; height: 64px; in: {x:-20, opacity:0, duration:.3})
        p#s(left: 0px; cy: 50%; font-size: 34px; font-family: e) 廃棄が減った分
        p#b(right: 0px; cy: 50%; font-size: 46px; color: $good) ＋9.7万円
      div#l2(left: 34px; top: 144px; width: 836px; height: 64px; in: {x:-20, opacity:0, duration:.3})
        p#s(left: 0px; cy: 50%; font-size: 34px; font-family: e) 値下げ額が増えた分
        p#b(right: 0px; cy: 50%; font-size: 46px; color: $ai) −3.8万円
      div#sum(left: 22px; top: 222px; width: 860px; height: 116px; border-radius: 20px; background: $good; in: {scaleY:0, opacity:0, duration:.35, ease:'back.out(1.6)'})
        p#s(left: 26px; cy: 50%; font-size: 36px; color: #FFFFFF) 差し引き ロスが減った
        p#b(right: 26px; cy: 50%; font-size: 84px; line-height: 1; color: #FFFFFF; white-space: nowrap) 5.9{t9}万円分{/}

# 05 家庭: アンケートの問い → 確かめない人 / 確かめる人の 100 マス (VS) → 語で 40 個・17 個を塗り % を数える → 冷蔵庫を撮る札が下から入り、シャッターの白い閃光
section#home
board#hm(n: "05"; t: "家庭でできる1つの工夫")
  p#ttl(font-size: 44px)
  p#q(left: 40px; top: 130px; width: 904px; text-align: center; font-size: 32px; line-height: 1.32; in: {y:20, opacity:0, duration:.4}; delay: 50ms) 店頭アンケート：{mk}同じ物を二重に買って捨てた{/}ことが[br]月1回以上ある人の割合
  # 比べる 2 列 (題 3 段 + 100 マス + 大きい % + 人数)
  div#ga(left: 24px; top: 230px; width: 432px; height: 610px; border-radius: 30px; background: #FFF1EC; in: {y:50, opacity:0, duration:.45, ease:'back.out(1.4)'})
    p#h1(left: 0px; top: 14px; width: 432px; text-align: center; font-size: 26px; font-family: e; color: $ink2) 買い物前に冷蔵庫を
    p#h2(left: 0px; top: 46px; width: 432px; text-align: center; font-size: 44px; color: $ai) 確かめない人
    div#don(left: "35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3"; top: "96;96;96;96;96;96;96;96;96;96;118;118;118;118;118;118;118;118;118;118;140;140;140;140;140;140;140;140;140;140;162;162;162;162;162;162;162;162;162;162"; width: 28px; height: 28px; border-radius: 148px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×40
    p#h3(left: 0px; top: 100px; width: 432px; text-align: center; font-size: 26px; font-family: e; color: $ink2) 140人（58%）
    div#doff(left: "35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3"; top: "184;184;184;184;184;184;184;184;184;184;206;206;206;206;206;206;206;206;206;206;228;228;228;228;228;228;228;228;228;228;250;250;250;250;250;250;250;250;250;250;272;272;272;272;272;272;272;272;272;272;294;294;294;294;294;294;294;294;294;294"; width: 28px; height: 28px; border-radius: 148px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×60
    p#pct(left: 0px; top: 480px; width: 432px; text-align: center; font-size: 104px; line-height: 1; color: $ai; in: {scale:.6, opacity:0, duration:.3, ease:'back.out(2)'}) [count:40 start=0 ms=600 ease=cubic_out]{pu}%{/}
    p#cnt(left: 0px; top: 580px; width: 432px; text-align: center; font-size: 24px; font-family: e; color: $ink2; in: {opacity:0, duration:.3}) 140人中 56人
  div#gb(left: 528px; top: 230px; width: 432px; height: 610px; border-radius: 30px; background: #EEF8F1; in: {y:50, opacity:0, duration:.45, ease:'back.out(1.4)'})
    p#h1(left: 0px; top: 14px; width: 432px; text-align: center; font-size: 26px; font-family: e; color: $ink2) 買い物前に冷蔵庫を
    p#h2(left: 0px; top: 46px; width: 432px; text-align: center; font-size: 44px; color: $good) 確かめる人
    div#don(left: "35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3"; top: "96;96;96;96;96;96;96;96;96;96;118;118;118;118;118;118;118"; width: 28px; height: 28px; border-radius: 148px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×17
    div#doff(left: "189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3"; top: "118;118;118;140;140;140;140;140;140;140;140;140;140;162;162;162;162;162;162;162;162;162;162;184;184;184;184;184;184;184;184;184;184;206;206;206;206;206;206;206;206;206;206;228;228;228;228;228;228;228;228;228;228;250;250;250;250;250;250;250;250;250;250;272;272;272;272;272;272;272;272;272;272;294;294;294;294;294;294;294;294;294;294"; width: 28px; height: 28px; border-radius: 148px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×83
    p#h3(left: 0px; top: 100px; width: 432px; text-align: center; font-size: 26px; font-family: e; color: $ink2) 100人
    p#pct(left: 0px; top: 480px; width: 432px; text-align: center; font-size: 104px; line-height: 1; color: $good; in: {scale:.6, opacity:0, duration:.3, ease:'back.out(2)'}) [count:17 start=0 ms=500 ease=cubic_out]{pu}%{/}
    p#cnt(left: 0px; top: 580px; width: 432px; text-align: center; font-size: 24px; font-family: e; color: $ink2; in: {opacity:0, duration:.3}) 100人中 17人
  div#vs(left: 466px; top: 440px; width: 52px; height: 52px; border-radius: 148px; background: $ink; in: {scale:0, duration:.3, ease:'back.out(2)'})
    p#t(cx: 50%; cy: 50%; font-size: 22px; color: #FFFFFF) VS
  # 工夫の札 (緑の縁・左に冷蔵庫を撮る絵が上へはみ出す)
  div#tip(left: 24px; top: 856px; width: 936px; height: 222px; border-radius: 30px; background: #E8F6EC; border: 4px solid $good; in: {y:260, opacity:0, duration:.5, ease:'power3.out'})
    # hf の作り: 絵は札の上へ 9 px はみ出す (child_overflow)
    img#img(left: 22px; top: -14px; width: 250px; height: 250px; object-fit: contain; main: none; transform-origin: 50% 80%; content: @fridge)
    p#s(left: 300px; top: 22px; font-size: 28px; font-family: e; color: $ink2) 出かける前に
    p#b(left: 300px; top: 66px; font-size: 56px; line-height: 1.15; white-space: nowrap) 冷蔵庫をスマホで1枚
    p#p(left: 300px; top: 138px; font-size: 30px; font-family: e; white-space: nowrap) 二重買いは {hb}半分以下{/} になりうる
  # シャッターの白い閃光 (板の上だけ)
  div#fl(inset: 0; border-radius: 44px; background: #FFFFFF; opacity: .85; overlap: hm.ga,hm.gb,hm.tip,hm.vs,hm.q; in: none)
  bsub#sub 来店客240人

# まとめ: 番号の丸つきの札 3 枚が右から語ごとに入り、最後の札で板がゆっくり 1.02 倍に寄る
section#wrap
board#sm(n: "まとめ"; t: "今日のポイント")
  div#c1(left: 32px; top: 140px; width: 920px; height: 296px; border-radius: 32px; background: #FFF8EE; border: 3px solid #F1E0C6; in: {x:80, opacity:0, duration:.45, ease:'back.out(1.4)'})
    div#no(left: 26px; top: 26px; width: 74px; height: 74px; border-radius: 148px; background: $a; in: {scale:0, duration:.35, ease:'back.out(2.4)'})
      p#t(cx: 50%; cy: 50%; font-size: 44px; color: #FFFFFF) 1
    p#a(left: 124px; top: 24px; font-size: 32px; font-family: e) ロスの半分は
    p#b(left: 124px; top: 69px; font-size: 54px; line-height: 1.2; white-space: nowrap) 惣菜・青果・パン{s21} の3つの棚から{/}
    p#p(left: 124px; top: 144px; font-size: 27px; font-family: e; line-height: 1.4; color: $ink2) 山は{ea}日曜{/}（火曜の約1.8倍）
    img#pic(left: "373;449;525"; top: 170px; width: 112px; height: 112px; object-fit: contain; main: none; content: "@souzai;@seika;@pan") ×3
  div#c2(left: 32px; top: 458px; width: 920px; height: 296px; border-radius: 32px; background: #FFF8EE; border: 3px solid #F1E0C6; in: {x:80, opacity:0, duration:.45, ease:'back.out(1.4)'})
    div#no(left: 26px; top: 26px; width: 74px; height: 74px; border-radius: 148px; background: $a; in: {scale:0, duration:.35, ease:'back.out(2.4)'})
      p#t(cx: 50%; cy: 50%; font-size: 44px; color: #FFFFFF) 2
    p#a(left: 124px; top: 24px; font-size: 32px; font-family: e) 値引きシールを
    p#b(left: 124px; top: 69px; font-size: 54px; line-height: 1.2) 2時間早く
    p#p(left: 124px; top: 144px; font-size: 27px; font-family: e; line-height: 1.4; color: $ink2) 惣菜・パンの廃棄は{ea}約3割減{/}[br]値下げ分を引いても{ea}5.9万円分{/}のロス減
    div#mini(right: 44px; top: 62px; width: 172px; height: 172px; border-radius: 148px; background: #FFD84D; border: 8px solid $a; transform: rotate(-10deg))
      p#b(cx: 50%; top: 38px; font-size: 54px; line-height: 1; color: $ai) 半額
      p#s(cx: 50%; top: 99px; font-size: 24px) 17:00〜
  div#c3(left: 32px; top: 776px; width: 920px; height: 296px; border-radius: 32px; background: #FFF8EE; border: 3px solid #F1E0C6; in: {x:80, opacity:0, duration:.45, ease:'back.out(1.4)'})
    div#no(left: 26px; top: 26px; width: 74px; height: 74px; border-radius: 148px; background: $a; in: {scale:0, duration:.35, ease:'back.out(2.4)'})
      p#t(cx: 50%; cy: 50%; font-size: 44px; color: #FFFFFF) 3
    p#a(left: 124px; top: 24px; font-size: 32px; font-family: e) 家では、買う前に
    p#b(left: 124px; top: 69px; font-size: 54px; line-height: 1.2) 冷蔵庫を1枚
    p#p(left: 124px; top: 144px; font-size: 27px; font-family: e; line-height: 1.4; color: $ink2) 二重買いの経験 {ea}40% → 17%{/} の水準へ
    img#pic(left: 700px; top: 82px; width: 200px; height: 200px; object-fit: contain; main: none; content: @fridge)
```

```timeline.txt
#v2
cast n = "明るく親しみやすい若い女性のナレーター、はっきりした声でテンポよく語りかける" speed=115%
silence head=0ms tail=220ms

*** title
[>#subtitle]
bgm music
@n: [silence:500ms][♪swoosh -5dB -380ms][>#kick -400ms][>#l1 -320ms][>#bd[*] -50ms]スーパーの食品ロス。その[>#l2 -80ms][♪perc -60ms]{e}半分{/}は、たった[>#l3 -100ms][!#l3{mk} marker +120ms][♪kira -9dB][!#bd[1] to,{opacity:1, duration:.2} +300ms][!#bd[1].img to,{filter:'saturate(1)', duration:.25} +300ms][!#bd[1] punch {scale: 1.12, duration: .32} +300ms][♪pop -2dB +300ms][!#bd[2] to,{opacity:1, duration:.2} +440ms][!#bd[2].img to,{filter:'saturate(1)', duration:.25} +440ms][!#bd[2] punch {scale: 1.12, duration: .32} +440ms][♪pop -2dB +440ms][!#bd[3] to,{opacity:1, duration:.2} +580ms][!#bd[3].img to,{filter:'saturate(1)', duration:.25} +580ms][!#bd[3] punch {scale: 1.12, duration: .32} +580ms][♪pop -2dB +580ms][!#bd[*].img to,{y:-8, duration:.9, ease:'sine.inOut', repeat:1, yoyo:true, stagger:.15} +1000ms]{e}3つの棚{/}から出ていました。

*** stage
@n: [silence:200ms][♪scene -5dB -200ms]架空のスーパー「[>#st.a.plate -50ms][♪pophi -3dB]まるみ屋 ひばり台店」で、[|][>#st.a.chips[*] -50ms][♪pop -3dB -50ms][♪pop -3dB +100ms][♪pop -3dB +250ms]{e}4週間{/}、廃棄を毎日[>#st.a.note]量りました。
@: [<#st.a -250ms][<#st.ttl -250ms][<#st.sub -250ms][>#st.t2 -50ms][>#st.b -30ms][♪swoosh -6dB -250ms]合計[!#st.b.total count][♪perc -2dB][♪pophi -4dB +1000ms]{e}1,840kg{/}、売値で[>#st.b.yen -50ms][♪register -5dB][>#st.b.note1 +300ms]{e}151万8,500円{/}分。[>#st.b.rule -200ms][>#st.b.perday -50ms][>#st.b.eq +350ms][>#st.b.bl +450ms][>#st.b.bt[*] +100ms][♪pop -8dB +50ms][♪pop -8dB +600ms][♪pop -8dB +1150ms]毎日、2Lペットボトル[>#st.b.bv][♪pophi -2dB][>#st.b.note2 +300ms]{e}33本{/}分です。

*** shelves
@n: [silence:200ms][♪scene -5dB -200ms][>#sh.rows.r[*] {stagger:{each:.07}} +50ms][♪swoosh -8dB +50ms]最多は[>#sh.band.b1 -50ms][!#sh.rows.r[1].nm punch {scale: 1.16, duration: .36, pivot: 'left'}][♪pop -4dB]惣菜。[||][>#sh.band.b2 -50ms][!#sh.rows.r[2].nm punch {scale: 1.16, duration: .36, pivot: 'left'}][♪pop -4dB]青果、[>#sh.band.b3 -50ms][!#sh.rows.r[3].nm punch {scale: 1.16, duration: .36, pivot: 'left'}][♪pop -4dB]パンと続き、[|][>#sh.sumw -50ms][>#sh.sumw.s1 +150ms][>#sh.sumw.s2 +150ms][>#sh.sumw.s3 +150ms]この3つで[!#sh.sumw.pct count -100ms][!#sh.sumw.pct punch {scale: 1.1, duration: .4, pivot: 'left'} +700ms][♪kira -9dB]{e}50.5%{/}です。
@: でも[!#sh.tg.knob to,{x:147, duration:.3, ease:'power2.inOut'}][!#sh.tg.w recolor,$ink {duration: .2}][!#sh.tg.m recolor,#FFFFFF {duration: .2} +100ms][<#sh.uw][>#sh.um +150ms][<#sh.band][<#sh.sw][<#sh.lg][<#sh.rows.r[*].vw +50ms][!#sh.rows.r[2].bar to,{scaleX:0.2727, duration:.6, ease:'power3.inOut', pivot:'left'} +120ms][!#sh.rows.r[3].bar to,{scaleX:0.8182, duration:.6, ease:'power3.inOut', pivot:'left'} +120ms][!#sh.rows.r[4].bar to,{scaleX:0.4118, duration:.6, ease:'power3.inOut', pivot:'left'} +120ms][!#sh.rows.r[5].bar to,{scaleX:1.3629, duration:.6, ease:'power3.inOut', pivot:'left'} +120ms][!#sh.rows.r[6].bar to,{scaleX:1.2732, duration:.6, ease:'power3.inOut', pivot:'left'} +120ms][!#sh.rows.r[7].bar to,{scaleX:0.4544, duration:.6, ease:'power3.inOut', pivot:'left'} +120ms][!#sh.rows.r[2] to,{y:288, duration:.7, ease:'power3.inOut'} +250ms][!#sh.rows.r[3] to,{y:96, duration:.7, ease:'power3.inOut'} +250ms][!#sh.rows.r[4] to,{y:192, duration:.7, ease:'power3.inOut'} +250ms][!#sh.rows.r[5] to,{y:-288, duration:.7, ease:'power3.inOut'} +250ms][!#sh.rows.r[6] to,{y:-288, duration:.7, ease:'power3.inOut'} +250ms][>#sh.rows.r[*].vm +800ms][>#sh.rk1 +950ms][>#sh.rk2 +1100ms][<#sh.sumw +100ms][♪click][♪register -5dB +50ms][♪pophi -5dB +750ms]{e}金額{/}では話が別。[>#sh.summ]1kgあたり、[|][>#sh.summ.pc[1]][♪pop -3dB]精肉{e}1,500円{/}、[|][>#sh.summ.pc[2]][♪pop -3dB]惣菜{e}1,100円{/}、青果は[>#sh.summ.pc[3]][♪pop -3dB][>#sh.summ.note +400ms]{e}300円{/}。
@: 重さか金額かで、[|][>#sh.point -100ms][♪pophi -3dB]「大きい棚」は{e}入れ替わります{/}。

*** days
@n: [silence:200ms][♪scene -5dB -200ms][>#dy.col[*] +80ms][>#dy.cv[*] +300ms][>#dy.avg +800ms][>#dy.avgl +1100ms][♪swoosh -8dB +80ms]曜日別では[>#dy.tmax][!#dy.col[7] to,{scaleX:1.12, duration:.18, ease:'power2.out'}][!#dy.col[7] to,{scaleX:1, duration:.18, ease:'power2.in'} +180ms][♪pophi -3dB]{e}日曜{/}が最多で、[>#dy.tmin]火曜の[>#dy.bai -100ms][♪kira -10dB]{e}約1.8倍{/}。
@: [>#dy.w[1] +140ms][♪pop -3dB +140ms]昼の客足に合わせて多めに作った惣菜が、[|][>#dy.arw -250ms][>#dy.w[2]][♪pop -3dB]{e}夕方{/}、[>#dy.stamp -250ms][♪stamp -2dB +50ms]売れ残るんです。

*** exp
@n: [silence:200ms][♪scene -5dB -200ms]そこで、[>#ex.a.it[*] -100ms][♪pop -4dB]惣菜とパンの{e}半額シール{/}を[|][!#ex.a.clk.mh to,{rotation:-720, duration:.95, ease:'power2.inOut'}][!#ex.a.clk.hh to,{rotation:150, duration:.95, ease:'power2.inOut'}][>#ex.a.clk.arc +500ms][!#ex.a.t19 strike,$ink +300ms][♪click -5dB +100ms][♪click -5dB +320ms][♪click -5dB +540ms][♪click -5dB +760ms]{e}2時間早め{/}、[>#ex.a.t17 -150ms][>#ex.a.early +250ms]17時に[>#ex.a.it[1].st -170ms][>#ex.a.it[2].st +30ms][>#ex.a.notea +300ms][♪stamp +50ms][♪stamp -1dB +250ms]貼ってみると、
@: [<#ex.a -220ms][>#ex.b -20ms][>#ex.b.res.b1 +100ms][>#ex.b.res.b3 +200ms][>#ex.b.res.b2 +570ms][>#ex.b.res.b4 +690ms][>#ex.b.res.v1 +720ms][>#ex.b.res.v2 +800ms][>#ex.b.res.v3 +880ms][>#ex.b.res.v4 +960ms][♪swoosh -6dB -50ms]2週間で、廃棄は[>#ex.b.res.d1 -200ms][>#ex.b.res.d2 -50ms]{e}約3割{/}、[>#ex.b.res.tot -200ms][!#ex.b.res.tot.b settle {scale: 1.3, duration: .35}][♪correct -5dB]{e}93kg{/}減。
@: [>#ex.b.rc -50ms][>#ex.b.rc.l1 +150ms][>#ex.b.rc.l2 +470ms][♪swoosh -8dB -20ms]値下げが増えた分を引いても、[|][>#ex.b.rc.sum -100ms][!#ex.b.rc.sum.b settle {scale: 1.4, duration: .35}][♪register -3dB]{e}5万9,000円{/}分ロスが減りました。

*** home
@n: [silence:200ms][♪scene -5dB -200ms]家庭では、[>#hm.ga -250ms][>#hm.gb -100ms][>#hm.vs +200ms][>#hm.ga.don[*] +100ms][>#hm.ga.doff[*] +260ms][>#hm.gb.don[*] +500ms][>#hm.gb.doff[*] +568ms][♪pop -5dB]冷蔵庫を確かめず[|]買い物に行く人の[!#hm.ga.don[*] fill,#E8502F {duration: .2} {stagger: {each: .012}} -200ms][>#hm.ga.pct count -120ms][♪pophi -3dB]{e}40%{/}が、[|][>#hm.ga.cnt]月1回以上、{e}二重買い{/}で食品を捨てていました。
@: 確かめる人は[!#hm.gb.don[*] fill,#24935C {duration: .2} {stagger: {each: .02}} -300ms][>#hm.gb.pct count -120ms][>#hm.gb.cnt +300ms][♪pophi -3dB]{e}17%{/}。
@: [>#hm.tip][♪swoosh -6dB +20ms]出かける前に、冷蔵庫を{e}スマホで1枚{/}[>#hm.fl +220ms][!#hm.fl to,{opacity:0, duration:.45, ease:'power2.out'} +280ms][!#hm.tip.img to,{rotation:-4, duration:.12, yoyo:true, repeat:1} +220ms][♪shutter +220ms]撮るだけで、[|]二重買いは[!#hm.tip.p{hb} punch {scale: 1.25, duration: .4}][♪correct -5dB]{e}半分以下{/}になりえます。

*** wrap
@n: [silence:200ms][♪scene -5dB -200ms][>#sm.c1 -100ms][>#sm.c1.no][♪pop -3dB]ロスの半分は{e}3つの棚{/}から。[>#sm.c2 -100ms][>#sm.c2.no][♪pop -3dB]値引きは{e}2時間早く{/}。[||][>#sm.c3 -100ms][>#sm.c3.no][♪pop -3dB][!#sm to,{scale:1.02, duration:3.2, ease:'sine.inOut'}]家では、{e}冷蔵庫を1枚{/}[♪kira -8dB +1500ms]。[silence:1.7s]
```

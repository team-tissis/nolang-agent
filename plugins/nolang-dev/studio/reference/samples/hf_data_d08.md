# data · supermarket-food-loss (hf 全力版の全量の写し — スーパーの食品ロス、半分は 3 つの棚から・生成りの地に白い板を下から差し込む 7 場面のデータ図解) — canvas 720x1280

見せる作り: 全編の地 (生成りの縦グラデ・流れる点の格子・漂う 3 色のぼけ) と常設の上端 (白い丸札の題・店名・全編で伸びる進行線) と下端の出典・場面ごとに下から傾いて差し込む白い板 (番号札 + 題 + 補足札の def)・同じ板の中身を語で抜き差しして替える (店の絵と数字の札 → はかりの絵・数える合計・弾んで並ぶボトル 33 本)・7 本の横棒が重さ → 金額の切替で縮み行が入れ替わる (切替の札・黄の帯・順位の札・POINT の札)・曜日の縦棒と平均の破線と判子・2 時間戻る時計の針と前後の横棒とレシート・100 マスを語で塗る比べる 2 列とシャッターの閃光・番号つきのまとめの札 3 枚・白い札の字幕 (強調は朱)・音の層 (場面の頭の遷移音 + 語に結んだ効果音 57)

```design.txt
#v2
# 学ぶ作り: 明るい生成りの地 (縦グラデ + 動く点の格子 + 漂う 3 色のぼけ) の上に、常設の上端 (白い丸札の題・店名・全編で伸びる進行線) と下端の出典の 1 行を敷き、場面ごとに白い大きな板 1 枚を下から差し込む
# 板 = 番号札 + 題 + 右肩の補足札 + 破線の罫の def (board)。中身は板の内側の座標で組み、板の中の容器 (div#a → div#b) を語で抜き差しして同じ板の中身を替える (題も同じ語で入れ替える)
# 図は数字の語と同時に伸びる: 棚ごとの横棒 ×7 (語で上位 3 つに黄の帯が伸び、重さ → 金額の切替で棒の長さ (to scaleX・左を軸) と行の順 (to y) が動く)・曜日の縦棒 ×7・回る時計の針と前後の横棒・100 マスの点 ×2 を語で塗る・33 本のボトルが弾んで並ぶ
# hf d08 supermarket-food-loss (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3 (板の中身は板の左上からの相対)
canvas 720x1280 bg=#FFF6E8
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
div { border-radius: 0px; background: none; padding: 0px; border: none; box-shadow: none }
# 曲: 頭の 0.3 秒と締めの余韻だけ前に出す
bgm#music(keys: "0:+7|320ms:+7|620ms:0|end-1.6s:0|end-1.1s:+6"; fade: 0,1600) 明るく軽やかなアコースティックのポップ、木琴とウクレレと手拍子、暮らしの情報やキッチンの解説向け、主旋律は控えめ
# 字幕: 下の帯の中央に白い札 (黒の縁 + 下に硬い影)・強調の語は朱 (台詞の {e})・札は文 (句は [|] で切り、文を跨ぐ札は [||])
subtitle.hug(left: 20px; bottom: 248px; width: 680px; wrap: comma,30; font-size: 28px; font-family: e; line-height: 1.38; color: $ink; background: #FFFFFF; border: 2px solid $ink; border-radius: 17px; box-shadow: 0px 4px 0px $ink; padding: 11px 19px 12px 19px; unit: sentence; lead: 0; in: {y:9, opacity:0, duration:.16, ease:'power2.out'})

# 全編の地: 縦グラデ・点の格子 (全編で 27 px 上へ流れる)・3 色のぼけ (全編でゆっくり漂う)
div#bg_base(inset: 0; background: linear(#FFF9EF,#FFF1DC,180); z-index: back; in: none)
div#dots(left: -27px; top: -27px; width: 774px; height: 1334px; pattern: dots,27,#96693221; z-index: back; in: none; main: ramp {y: -27})
div#blob1(left: -253px; top: -173px; width: 600px; height: 600px; background: radial(#FFC4788C,#FFC47800@68%,50%,50%); z-index: back; in: none; main: ramp {x: 80, y: 53, ease: 'sine.inOut'})
div#blob2(left: 347px; top: 507px; width: 653px; height: 653px; background: radial(#96D6A073,#96D6A000@68%,50%,50%); z-index: back; in: none; main: ramp {x: -93, y: -80, ease: 'sine.inOut'})
div#blob3(left: -173px; top: 880px; width: 507px; height: 507px; background: radial(#FFAA9666,#FFAA9600@68%,50%,50%); z-index: back; in: none; main: ramp {x: 107, y: -40, ease: 'sine.inOut'})
# 常設の上端: 白い丸札の題 (朱の丸 + カート) と右の店名・その下に全編で伸びる進行線・下端の出典
div#brand(left: 32px; top: 46px; width: 262px; height: 44px; background: #FFFFFF; border: 2px solid $ink; border-radius: 99px; box-shadow: 0px 3px 0px $ink; in: {y:-20, opacity:0, duration:.5, ease:'power3.out'})
  div#dot(left: 6px; cy: 50%; width: 27px; height: 27px; border-radius: 99px; background: $a)
  svg#cart(left: 11px; cy: 50%; width: 16px; height: 16px; part: cart)
  p#t(left: 42px; cy: 50%; font-size: 20px; letter-spacing: .02em; white-space: nowrap) 食品ロスを数字で見る
p#store(right: 32px; cy: 68px; font-size: 17px; font-family: e; line-height: 1.25; text-align: right; color: $ink2; in: {y:-20, opacity:0, duration:.5, ease:'power3.out'}) まるみ屋 ひばり台店[br]（架空の地域スーパー）
div#ptrack(left: 32px; top: 109px; width: 656px; height: 7px; border-radius: 3px; background: #2B25221A; in: none)
progress#pbar(left: 32px; top: 109px; width: 656px; height: 7px; border-radius: 3px; background: linear(#F08A24,#E8502F,90); until: end; overlap: ptrack)
p#foot(cx: 360px; top: 1052px; font-size: 16px; font-family: d; color: $ink2; in: none) ※架空の店舗「まるみ屋 ひばり台店」の4週間の記録より

# 板: 白の角丸 + 淡い縁 + 柔らかい影・下から傾いて差し込み (y 1167・2.5°)、場面の終わりに奥へ縮んで消える
def board(n, t) = div(left: 32px; top: 141px; width: 656px; height: 733px; background: #FFFFFF; border-radius: 29px; border: 2px solid #F1E3CF; box-shadow: 0px 17px 40px #8C5A2829; in: {y:1167, rotation:2.5, duration:.55, ease:'power3.out'}; out: {y:-27, scale:.92, opacity:0, duration:.45, ease:'power1.in'})
  p#tag(left: 27px; cy: 38px; font-size: 19px; line-height: 1; color: #FFFFFF; background: $a; border-radius: 12px; padding: 7px 11px 8px 11px; content: {n})
  p#ttl(left: .tag.right+13; cy: 38px; font-size: 31px; line-height: 1.1; white-space: nowrap; content: {t})
  shape#hr(left: 0px; top: 76px; width: 656px; height: 2px; path: line_h; border: 2px solid $line; dash: 6,6)
# 板の右肩の補足札
def bsub(t) = p(right: 27px; cy: 38px; font-size: 17px; font-family: e; color: $ink2; background: #FFF3E2; border-radius: 99px; padding: 7px 13px 7px 13px; white-space: nowrap; content: {t})

# 題: 黒の小札 → 2 行の大見出し (「半分」が拡大から着地・「3つの棚」に黄の帯が伸びる) → 灰色で薄く並ぶ 3 つの丸窓が語で色づいて弾む
section#title(out: {y:-40, scale:.94, opacity:0, duration:.45, ease:'power1.in'})
p#kick(cx: 360px; top: 179px; font-size: 21px; font-family: e; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 8px 20px 9px 20px; in: {y:-16, opacity:0, duration:.4, ease:'power3.out'}) 4週間 × 棚ごとの廃棄データ
p#l1(cx: 360px; top: 248px; font-size: 57px; in: {y:27, opacity:0, duration:.5, ease:'power3.out'}) スーパーの食品ロス、
p#l2(cx: 360px; top: 324px; font-size: 117px; line-height: 1; in: {scale:1.6, opacity:0, duration:.42, ease:'back.out(1.8)'}) {r}半分{/}は
p#l3(cx: 360px; top: 460px; font-size: 100px; line-height: 1; in: {y:33, opacity:0, duration:.42, ease:'power3.out'}) {mk}3つの棚{/}{sm}から{/}
# 丸窓の札 (白い円 + 色の輪 + 透過の絵 + 色の名札)・半分の濃さで灰色に置き、語で濃く色づく
def badge(t, c, lc, im) = div(width: 184px; height: 244px; opacity: .5; in: {y:33, opacity:0, duration:.5, ease:'power3.out', stagger: {each: .1}})
  div#ring(left: 0px; top: 0px; width: 184px; height: 184px; border-radius: 99px; background: #FFFFFF; border: 5px solid {c}; box-shadow: 0px 9px 20px #8C5A282E)
  img#img(cx: 92px; cy: 92px; width: 151px; height: 151px; object-fit: contain; filter: saturate(0); main: none; content: {im})
  p#lb(cx: 92px; top: 196px; font-size: 31px; color: #FFFFFF; background: {lc}; border-radius: 99px; padding: 4px 19px 7px 19px; content: {t})
badge#bd(left: "47;268;489"; top: 620px; t: "惣菜;青果;パン"; c: "$souzai;$seika;$pan"; lc: "#B9560B;#2B7D45;#9A6A12"; im: "@souzai;@seika;@pan") ×3

# 01 調査の舞台: 店の絵が上から開き、店名の札と 3 つの数字の札 → 同じ板の中身を左へ抜き「4週間の廃棄」へ (はかりの絵・数える合計・売値・1 日あたり = ボトル 33 本)
section#stage
board#st(n: "01"; t: "調査の舞台")
  p#ttl(out: {y:-13, opacity:0, duration:.2})
  p#t2(left: .tag.right+13; cy: 38px; font-size: 31px; line-height: 1.1; white-space: nowrap; in: {y:13, opacity:0, duration:.3}) 4週間の廃棄
  bsub#sub(out: {opacity:0, duration:.25}) 架空の地域スーパー
  div#a(inset: 0; out: {x:-40, opacity:0, duration:.24, ease:'power2.in'})
    img#photo(left: 27px; top: 93px; width: 603px; height: 402px; border-radius: 20px; delay: 200; in: wipe {dir: 'down', duration: 0.7, ease: 'power3.out'}; main: kb {scale: [1.12, 1], ease:'sine.out'}; subject: top 65%; room: bottom 30%) A cozy neighborhood supermarket storefront on a quiet street in a Japanese residential area: a single-story shop with a green-and-cream striped awning, large glass windows showing produce and bread shelves, a couple of shoppers with eco bags, a parked bicycle and potted plants, soft morning light. The shop fills the whole frame edge to edge; the lower-left quarter is plain pavement for a name plate.
    div#plate(left: 47px; top: 391px; width: 372px; height: 91px; background: #FFFFFF; border-radius: 15px; box-shadow: 0px 7px 16px #00000029; overlap: st.a.photo; in: {x:-27, opacity:0, duration:.45, ease:'back.out(1.6)'})
      p#b(left: 19px; top: 11px; font-size: 36px; line-height: 1.1; white-space: nowrap) まるみ屋 ひばり台店
      p#s(left: 19px; top: 56px; font-size: 17px; font-family: e; color: $ink2; white-space: nowrap) 住宅街にある地域スーパー（架空）
    # 数字の札 ×3 (題 + 大きい数字 + 小さい単位)
    div#chips(left: "27;233;439"; top: 515px; width: 191px; height: 117px; background: $card; border: 2px solid $cardline; border-radius: 17px; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.6)', stagger: {each: .15}}) ×3
      p#l(left: 15px; top: 13px; font-size: 17px; font-family: e; color: $ink2) 売場面積;1日の来店;記録した期間
      p#v(left: 15px; top: 46px; font-size: 37px; line-height: 1.15; white-space: nowrap) 1,200{u}m²{/};約2,100{u}人{/};28{u}日（4週間）{/}
    p#note(left: 27px; top: 652px; font-size: 17px; font-family: d; color: $ink2; in: {opacity:0, duration:.4}) ※棚ごとに毎日、はかりで廃棄の重さを記録
  div#b(inset: 0; in: {x:40, opacity:0, duration:.4, ease:'power3.out'})
    img#scale(left: 17px; top: 97px; width: 260px; height: 260px; object-fit: contain; main: none; in: {y:20, scale:.9, opacity:0, duration:.6, ease:'back.out(1.6)'}) [transparent]A white digital platform scale with a clear plastic crate on it, the crate filled with unsold food: wrapped deli bento packs, bread rolls, a cabbage and tomatoes. The scale display is blank. Isolated object, centered, filling the frame.
    p#lbl(left: 293px; top: 112px; font-size: 20px; font-family: e; color: $ink2) 廃棄の合計（28日間）
    # 合計は 0 で出て、語で 1,840 まで数える
    p#total(left: 288px; top: 146px; font-size: 88px; line-height: 1; letter-spacing: -.02em; white-space: nowrap) [count:1,840 start=0 ms=1000 ease=cubic_out]{ku}kg{/}
    div#yen(left: 293px; top: 261px; width: 340px; height: 80px; in: {y:20, opacity:0, duration:.4, ease:'back.out(1.6)'})
      p#l(left: 0px; top: 0px; font-size: 19px; font-family: e; color: $ink2) 売値で
      p#v(left: 0px; top: 26px; font-size: 49px; line-height: 1.12; color: $a; white-space: nowrap) 151万8,500{yu}円分{/}
    p#note1(left: 293px; top: 345px; font-size: 15px; font-family: d; color: $ink2; in: {opacity:0, duration:.3}) ※売値で換算した金額
    shape#rule(left: 27px; top: 377px; width: 603px; height: 2px; path: line_h; border: 2px solid $line; dash: 6,6; in: {scaleX:0, duration:.4, pivot:'left'})
    div#perday(left: 27px; top: 395px; width: 220px; height: 92px; in: {y:20, opacity:0, duration:.4, ease:'back.out(1.6)'})
      p#l(left: 0px; top: 0px; font-size: 21px; font-family: e; color: $ink2) 1日あたり
      p#v(left: 0px; top: 35px; font-size: 64px; line-height: 1; white-space: nowrap) 約66{k2}kg{/}
    p#eq(left: 256px; top: 427px; font-size: 48px; color: $ink2; in: {scale:.5, opacity:0, duration:.3}) ＝
    p#bl(left: 313px; top: 395px; font-size: 21px; font-family: e; color: $ink2; in: {y:11, opacity:0, duration:.3}) 2Lペットボトル
    p#bv(left: 313px; top: 430px; font-size: 64px; line-height: 1; color: $sengyo; white-space: nowrap; in: {scale:.5, opacity:0, duration:.4, ease:'back.out(2)', pivot:'0% 70%'}) 33{k2}本分{/}
    # ボトル 33 本 (11 列 × 3 段・下を軸に弾んで 52 ms ずつ)
    svg#bt(left: "61.3;111.3;161.3;211.3;261.3;311.3;361.3;411.3;461.3;511.3;561.3;61.3;111.3;161.3;211.3;261.3;311.3;361.3;411.3;461.3;511.3;561.3;61.3;111.3;161.3;211.3;261.3;311.3;361.3;411.3;461.3;511.3;561.3"; top: "485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;485.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;553.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3;621.3"; width: 33px; height: 61px; part: bottle; in: {scale:0, y:16, opacity:0, duration:.32, ease:'back.out(2.2)', pivot:'bottom', stagger: {each: .052}}) ×33
    p#note2(left: 27px; top: 697px; width: 603px; text-align: center; font-size: 15px; font-family: d; color: $ink2; in: {opacity:0, duration:.4}) ※1,840kg ÷ 28日 ≒ 66kg（2Lのボトル1本＝約2kgとして換算）

# 02 棚ごとの廃棄: 7 本の横棒 (重さ) → 上位 3 つに黄の帯 → 3 つで 50.5% の帯 → 切替の札で金額へ (棒が縮み行が入れ替わり、順位の札・1kg あたりの札・POINT の札)
section#shelves
# 棚の行: 色の点 + 名 (+ 小さい補足) + 棒 (幅 = 値 ÷ 最大 × 304 px) + 棒の右の値 (重さ) / 金額の値
def shelf(nm, sub, c, bw, v, mx, mv) = div(width: 656px; height: 64px; in: none)
  shape#dot.ellipse(left: 29px; top: 19px; width: 13px; height: 13px; background: {c})
  p#nm(left: 49px; top: 11px; font-size: 28px; line-height: 1.05; content: {nm})
  p#sub(left: 50px; top: 43px; font-size: 13px; font-family: e; color: $ink2; white-space: nowrap; content: {sub})
  div#bar(left: 168px; top: 14px; width: {bw}; height: 35px; border-radius: 9px; background: {c}; in: {scaleX:0, duration:.7, ease:'expo.out', pivot:'left'})
  p#vw(left: .bar.right+11; top: 13px; font-size: 29px; line-height: 1; white-space: nowrap; in: {x:-100, opacity:0, duration:.7, ease:'expo.out'}; out: {opacity:0, duration:.15}; content: {v})
  p#vm(left: {mx}; top: 13px; font-size: 29px; line-height: 1; white-space: nowrap; in: {opacity:0, duration:.25}; content: {mv})
board#sh(n: "02"; t: "棚ごとの廃棄")
  # 重さ / 金額の切替の札 (黒い丸の knob が右へ滑る)・lint は knob を地と見ずに low_contrast を出す (白い字は黒い knob の上)
  div#tg(right: 27px; cy: 38px; width: 200px; height: 44px; background: #F4ECE1; border: 2px solid $ink; border-radius: 99px)
    div#knob(left: 2px; top: 2px; width: 96px; height: 36px; border-radius: 99px; background: $ink)
    p#w(left: 0px; cy: 50%; width: 98px; text-align: center; font-size: 20px; color: #FFFFFF) 重さ
    p#m(left: 98px; cy: 50%; width: 98px; text-align: center; font-size: 20px) 金額
  div#sw(left: 27px; top: 94px; width: 27px; height: 16px; border-radius: 5px; background: #FFF0B3; border: 1px solid #F4D65A; out: {opacity:0, duration:.2})
  p#lg(left: 59px; cy: 102px; font-size: 17px; font-family: e; color: $ink2; out: {opacity:0, duration:.2}) 上位3つの棚
  p#uw(right: 27px; cy: 102px; font-size: 17px; font-family: e; color: $ink2; white-space: nowrap; out: {opacity:0, duration:.2}) 単位：kg（全体に占める割合）
  p#um(right: 27px; cy: 102px; font-size: 17px; font-family: e; color: $ink2; white-space: nowrap; in: {opacity:0, duration:.2}) 単位：万円（売値で換算）／順位は「その他」を除く
  # 上位 3 つの黄の帯 (語ごとに 1 行ずつ下へ伸びる)
  # 帯は 1 行 64 px の箱 3 枚 (2・3 枚目は上の箱の角の丸みを 16 px 覆って続く 1 本に見せる)
  div#band(left: 15px; top: 124px; width: 627px; height: 192px; in: none; out: {opacity:0, duration:.25})
    div#b1(left: 0px; top: 0px; width: 627px; height: 64px; border-radius: 16px; background: #FFF3C4; in: {scaleY:0, opacity:0, duration:.3, ease:'power2.out', pivot:'top'})
    div#b2(left: 0px; top: 48px; width: 627px; height: 80px; border-radius: 0px 0px 16px 16px; background: #FFF3C4; overlap: sh.band.b1; in: {scaleY:0, opacity:0, duration:.3, ease:'power2.out', pivot:'top'})
    div#b3(left: 0px; top: 112px; width: 627px; height: 80px; border-radius: 0px 0px 16px 16px; background: #FFF3C4; overlap: sh.band.b2; in: {scaleY:0, opacity:0, duration:.3, ease:'power2.out', pivot:'top'})
  shelf#r(left: 0px; top: 124px; width: 656px; height: 448px; display: flex; flex-direction: column; gap: 0px; nm: "惣菜;青果;パン;日配;精肉;鮮魚;その他"; sub: ";;;豆腐・乳製品・麺;;;加工食品・菓子など"; c: "$souzai;$seika;$pan;$nichi;$niku;$sengyo;$other"; bw: "304;205;148.5;134.3;127.3;113.1;268.7"; v: "430{u2}kg{/} {p2}23.4%{/};290{u2}kg{/} {p2}15.8%{/};210{u2}kg{/} {p2}11.4%{/};190{u2}kg{/} {p2}10.3%{/};180{u2}kg{/} {p2}9.8%{/};160{u2}kg{/} {p2}8.7%{/};380{u2}kg{/} {p2}20.7%{/}"; mx: "483;235;301;234;353;323;301"; mv: "47.3{u2}万円{/};8.7{u2}万円{/};18.9{u2}万円{/};8.6{u2}万円{/};27.0{u2}万円{/};22.4{u2}万円{/};19.0{u2}万円{/}") ×7
  # 順位の変化の札 (行が入れ替わった後の位置に)
  p#rk1(right: 24px; top: 204px; font-size: 19px; color: #FFFFFF; background: #C23A62; border-radius: 99px; padding: 4px 11px 5px 11px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2)'}) ▲ 5位→2位
  p#rk2(right: 24px; top: 396px; font-size: 19px; color: #FFFFFF; background: #6D7F8F; border-radius: 99px; padding: 4px 11px 5px 11px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2)'}) ▼ 2位→5位
  # 重さの合計の段: 3 つで 50.5% (数える)・930kg・3 色の積み上げの帯と半分の印
  div#sumw(left: 27px; top: 579px; width: 603px; height: 136px; in: {y:27, opacity:0, duration:.4, ease:'power3.out'}; out: {y:-13, opacity:0, duration:.25})
    p#t1(left: 0px; top: 3px; font-size: 21px; font-family: e) 惣菜・青果・パンの3つで
    p#pct(left: 0px; top: 31px; font-size: 77px; line-height: 1; color: $a; white-space: nowrap) [count:50.5 start=0 ms=800 ease=cubic_out]{pu}%{/}
    p#kg(left: 313px; top: 47px; font-size: 37px; line-height: 1; white-space: nowrap) 930{k3}kg ／ 全体 1,840kg{/}
    div#stk(left: 0px; top: 112px; width: 603px; height: 15px; border-radius: 7px; background: #ECE4D8)
    # 3 色の積み上げ (左から 1 本の帯として開く = 3 枚を続けて wipe)
    div#s1(left: 0px; top: 112px; width: 141px; height: 15px; border-radius: 7px 0px 0px 7px; background: $souzai; in: wipe {dir: 'right', duration: 0.33, ease: 'none'})
    div#s2(left: 141px; top: 112px; width: 95px; height: 15px; background: $seika; delay: 330; in: wipe {dir: 'right', duration: 0.22, ease: 'none'})
    div#s3(left: 236px; top: 112px; width: 69px; height: 15px; background: $pan; delay: 550; in: wipe {dir: 'right', duration: 0.15, ease: 'power2.out'})
    div#half(left: 301px; top: 103px; width: 3px; height: 33px; border-radius: 2px; background: $ink)
  # 金額の段: 1kg あたりの売値の札 ×3 が語ごとに弾む
  div#summ(left: 27px; top: 579px; width: 603px; height: 127px; in: {opacity:0, duration:.3})
    p#t1(left: 0px; top: 0px; font-size: 20px; font-family: e; in: {y:13, duration:.3}) 1kgあたりの売値
    div#pc(left: "0;205;410"; top: 31px; width: 193px; height: 67px; background: #FFFFFF; border: "$niku,2;$souzai,2;$seika,2"; border-radius: 15px; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) ×3
      p#n(left: 12px; cy: 50%; font-size: 21px; color: "$niku;#C96A10;#2E8A4B") 精肉;惣菜;青果
      p#v(left: .n.right+8; cy: 50%; font-size: 35px; white-space: nowrap) 1,500{yn}円{/};1,100{yn}円{/};300{yn}円{/}
    p#note(left: 0px; top: 105px; font-size: 15px; font-family: d; color: $ink2; in: {opacity:0, duration:.3}) ※惣菜・青果・パンの3つは、金額では74.9万円（49.3%）
  # POINT の札 (黒の縁 + 硬い影・少し傾けて弾む)
  div#point(left: 415px; top: 435px; width: 224px; height: 132px; background: #FFFFFF; border: 3px solid $ink; border-radius: 17px; box-shadow: 0px 5px 0px $ink; transform: rotate(-2deg); in: {scale:.6, rotation:-4, opacity:0, duration:.45, ease:'back.out(1.8)'})
    p#tag(left: 15px; top: 11px; font-size: 16px; background: $mk; border-radius: 7px; padding: 3px 8px 4px 8px) POINT
    p#t(left: 15px; top: 39px; font-size: 19px; font-family: e; line-height: 1.42; white-space: nowrap) 重さの2位は {g}青果{/}[br]金額の2位は {nr}精肉{/}[br]大きい棚が入れ替わる

# 03 曜日別: 目盛りの上に 7 本の縦棒 (日曜だけ朱・火曜は青灰) と平均の破線 → 最多 / 最少の札 → 約1.8倍 → 昼 → 夕方の札と判子
section#days
board#dy(n: "03"; t: "曜日別・1日の廃棄")
  bsub#sub 4週の平均
  shape#gl(left: 67px; top: "200;277;353;430"; width: 567px; height: 2px; path: line_h; border: 1px solid #EEE3D4) ×4
  div#axis(left: 67px; top: 506px; width: 567px; height: 2px; background: #CFC3B3)
  p#yl(left: 20px; top: "497;343;190"; width: 37px; text-align: right; font-size: 15px; font-family: e; color: $ink2) ×3 0;50;100
  p#ykg(left: 13px; top: 164px; width: 53px; text-align: right; font-size: 15px; font-family: e; color: $ink2) kg
  # 縦棒 (高さ = kg × 3.07 px・下を軸に 90 ms ずつ伸びる)
  div#col(left: "81;161.7;242.3;323;403.7;484.3;565"; top: "316.6;341.1;328.8;331.9;313.5;292;212.3"; width: 57px; height: "190.1;165.6;177.9;174.8;193.2;214.7;294.4"; border-radius: 11px 11px 4px 4px; background: "$cbar;$cmin;$cbar;$cbar;$cbar;$cbar;$a"; in: {scaleY:0, duration:.55, ease:'expo.out', pivot:'bottom', stagger: {each: .09}}) ×7
  p#cv(left: "63;143.7;224.3;305;385.7;466.3;547"; top: "324.6;349.1;336.8;339.9;321.5;300;220.3"; width: 93px; text-align: center; font-size: "21;21;21;21;21;21;29"; color: "$ink;$ink;$ink;$ink;$ink;$ink;#FFFFFF"; white-space: nowrap; in: {y:9, opacity:0, duration:.3, stagger: {each: .09}}) ×7 62{k5}kg{/};54{k5}kg{/};58{k5}kg{/};57{k5}kg{/};63{k5}kg{/};70{k5}kg{/};96{k5}kg{/}
  p#day(left: "76.3;157;237.7;318.3;399;479.7;560.3"; top: 516px; width: 67px; text-align: center; font-size: 25px; color: "$ink;$ink;$ink;$ink;$ink;$ink;$ai") ×7 月;火;水;木;金;土;日
  shape#avg(left: 69px; top: 304px; width: 564px; height: 3px; path: line_h; border: 3px solid #8D837A; dash: 8,6; overlap: dy.col; in: {scaleX:0, duration:.5, pivot:'left'})
  p#avgl(left: 7px; top: 285px; width: 61px; text-align: right; font-size: 14px; line-height: 1.2; color: $ink2; in: {opacity:0, duration:.3}) 平均[br]約66kg
  p#tmax(left: 569px; top: 179px; font-size: 16px; color: #FFFFFF; background: $ai; border-radius: 99px; padding: 3px 9px 4px 9px; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) 最多
  p#tmin(left: 166px; top: 310px; font-size: 16px; color: #FFFFFF; background: #5D7F9F; border-radius: 99px; padding: 3px 9px 4px 9px; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) 最少
  div#bai(left: 313px; top: 157px; width: 220px; height: 82px; in: {y:20, opacity:0, duration:.4, ease:'back.out(1.8)'})
    p#l(right: 0px; top: 0px; font-size: 17px; font-family: e; color: $ink2; white-space: nowrap) 日曜は火曜（54kg）の
    p#v(right: 0px; top: 25px; font-size: 56px; line-height: 1; color: $a; white-space: nowrap) 約1.8倍
  # 理由の札 ×2 (icon + 題 + 2 行)・間の矢印・夕方の札に判子
  div#w(left: "21;356"; top: 568px; width: 279px; height: 148px; border-radius: 19px; background: "#FFF6DF;#FFE9E0"; in: {y:40, opacity:0, duration:.45, ease:'back.out(1.6)'}) ×2
    svg#ic(left: 15px; top: 13px; width: 43px; height: 43px; part: "sun;sunset")
    p#h(left: 65px; top: 17px; font-size: 27px) 昼;夕方
    p#t(left: 16px; top: 69px; font-size: 21px; font-family: e; line-height: 1.38) 客足に合わせて[br]惣菜を多めに作る;客が早く引けて[br]売れ残る
  svg#arw(left: 313px; top: 620px; width: 29px; height: 44px; part: chev; in: {x:-13, opacity:0, duration:.3})
  div#stamp(left: 531px; top: 611px; width: 97px; height: 97px; border-radius: 99px; border: 4px solid $a; background: #FFFFFFD9; transform: rotate(-14deg); overlap: dy.w; in: {scale:2.2, rotation:-16, opacity:0, duration:.3, ease:'power4.in'})
    p#t(cx: 50%; cy: 50%; font-size: 20px; line-height: 1.1; text-align: center; color: $a) 売れ[br]残り

# 04 実験: 時計の針が 2 時間戻り 19:00 に線 → 17:00 → 半額シールを判子で 2 枚 → 同じ板を前後の横棒・−93kg の帯・レシートの差し引きへ入れ替える
section#exp
board#ex(n: "04"; t: "実験：値引きを2時間早く")
  bsub#sub 2週間
  div#a(inset: 0; out: {y:-27, opacity:0, duration:.24, ease:'power2.in'})
    group#clk(left: 39px; top: 107px; width: 253px; height: 253px; delay: 100; in: {scale:.7, opacity:0, duration:.5, ease:'back.out(1.6)'})
      svg#face(left: 0px; top: 0px; width: 253px; height: 253px; part: clockface)
      svg#arc(left: 0px; top: 0px; width: 253px; height: 253px; part: clockarc; in: {opacity:0, duration:.3})
      # 針は時計と同じ 253 px 四方の svg (中心 = 時計の中心) に描き、既定の中心軸で回す (時針 210° = 7 時)
      svg#hh(left: 0px; top: 0px; width: 253px; height: 253px; part: hhand; transform: rotate(210deg))
      svg#mh(left: 0px; top: 0px; width: 253px; height: 253px; part: mhand)
      shape#cdot.ellipse(left: 117px; top: 117px; width: 19px; height: 19px; background: $a)
    p#tl(left: 317px; top: 113px; font-size: 20px; font-family: e; color: $ink2; delay: 200; in: {opacity:0, duration:.3}) 半額シールを貼る時刻
    p#t19(left: 317px; top: 148px; font-size: 49px; color: #A79C92; delay: 300; in: {x:20, opacity:0, duration:.35}) 19:00
    p#t17(left: 317px; top: 215px; font-size: 85px; line-height: 1; color: $a; in: {y:27, opacity:0, duration:.4, ease:'back.out(1.8)'}) 17:00
    p#early(left: 320px; top: 313px; font-size: 21px; background: $mk; border-radius: 9px; padding: 4px 11px 5px 11px; in: {scale:0, opacity:0, duration:.35, ease:'back.out(2)'}) 2時間 早く！
    # 商品の札 ×2 (絵 + 名)・右上に半額シールを判子で
    div#it(left: "27;350"; top: 393px; width: 280px; height: 280px; border-radius: 20px; background: $card; border: 2px solid $cardline; in: {y:40, opacity:0, duration:.45, ease:'back.out(1.6)', stagger: {each: .15}}) ×2
      img#img(left: 40px; top: 20px; width: 200px; height: 200px; object-fit: contain; main: none; content: "@souzai;@pan")
      p#t(cx: 50%; bottom: 15px; font-size: 29px) 惣菜;パン
      div#st(left: 179px; top: 13px; width: 100px; height: 100px; border-radius: 99px; background: #FFD84D; border: 4px solid $a; box-shadow: 0px 4px 0px #0000001F; transform: rotate(-12deg); in: {scale:2.4, rotation:42, opacity:0, duration:.22, ease:'power4.in'})
        p#t(cx: 50%; cy: 50%; font-size: 33px; line-height: 1; color: $ai) 半額
    p#notea(left: 27px; top: 691px; font-size: 17px; font-family: d; color: $ink2; in: {opacity:0, duration:.3}) ※試したのは2週間。直前の2週間と比べました
  div#b(inset: 0; in: none)
    div#strip(left: 27px; top: 91px; width: 603px; height: 61px; border-radius: 16px; background: $card; border: 2px solid $cardline; in: {y:-20, opacity:0, duration:.35, ease:'power3.out'})
      div#mini(left: 16px; cy: 50%; width: 41px; height: 41px; border-radius: 99px; background: #FFD84D; border: 3px solid $a)
        p#t(cx: 50%; cy: 50%; font-size: 13px; color: $ai) 半額
      p#b(left: 69px; cy: 50%; font-size: 23px; white-space: nowrap) シールを {ra}19:00 → 17:00{/} に
      p#s(right: 16px; cy: 50%; font-size: 17px; font-family: e; color: $ink2; white-space: nowrap) 直前の2週間と比較
    div#res(left: 27px; top: 167px; width: 603px; height: 293px)
      p#rt(left: 0px; top: 0px; font-size: 21px; in: {opacity:0, duration:.3}) 廃棄の重さ（各2週間）
      p#lg(right: 0px; top: 3px; font-size: 15px; font-family: e; color: $ink2; white-space: nowrap; in: {opacity:0, duration:.3}) {sw1}■{/} 直前　{sw2}■{/} 実験中
      p#nm1(left: 0px; top: 57px; font-size: 28px) 惣菜
      div#b1(left: 73px; top: 45px; width: 287px; height: 27px; border-radius: 7px; background: #D9D0C4; in: {scaleX:0, duration:.5, ease:'expo.out', pivot:'left'})
      p#v1(left: 371px; cy: 58.5px; font-size: 20px; in: {opacity:0, duration:.3}) 215kg
      div#b2(left: 73px; top: 78px; width: 197px; height: 27px; border-radius: 7px; background: $souzai; in: {scaleX:0, duration:.6, ease:'expo.out', pivot:'left'})
      p#v2(left: 281px; cy: 91.5px; font-size: 20px; in: {opacity:0, duration:.3}) 148kg
      p#d1(right: 0px; top: 52px; font-size: 36px; color: $good; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) −31%
      p#nm2(left: 0px; top: 143px; font-size: 28px) パン
      div#b3(left: 73px; top: 131px; width: 140px; height: 27px; border-radius: 7px; background: #D9D0C4; in: {scaleX:0, duration:.5, ease:'expo.out', pivot:'left'})
      p#v3(left: 224px; cy: 144.5px; font-size: 20px; in: {opacity:0, duration:.3}) 105kg
      div#b4(left: 73px; top: 164px; width: 105px; height: 27px; border-radius: 7px; background: $pan; in: {scaleX:0, duration:.6, ease:'expo.out', pivot:'left'})
      p#v4(left: 189px; cy: 177.5px; font-size: 20px; in: {opacity:0, duration:.3}) 79kg
      p#d2(right: 0px; top: 138px; font-size: 36px; color: $good; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2)'}) −25%
      div#tot(left: 0px; top: 208px; width: 603px; height: 80px; border-radius: 17px; background: #EAF6EE; in: {y:20, opacity:0, duration:.4, ease:'back.out(1.6)'})
        p#s(left: 17px; cy: 50%; font-size: 20px; font-family: e; white-space: nowrap) 2つ合わせて 320kg → 227kg
        p#b(right: 17px; cy: 50%; font-size: 53px; line-height: 1; color: $good; white-space: nowrap) −93{t9}kg（−29%）{/}
    # レシート (破線の枠・2 行の増減・緑の差し引きの帯)
    div#rc(left: 27px; top: 476px; width: 603px; height: 240px; border-radius: 15px; background: #FFFDF8; in: {y:33, opacity:0, duration:.45, ease:'power3.out'})
      shape#frame(left: 0px; top: 0px; width: 603px; height: 240px; path: rect,r=0.06; background: none; border: 2px solid #D8C7AE; dash: 6,5)
      p#h1(left: 23px; top: 16px; font-size: 20px; color: $ink2) お金で見ると（2週間）
      p#h2(right: 23px; top: 16px; font-size: 20px; color: $ink2) 売値換算
      div#l1(left: 23px; top: 51px; width: 557px; height: 43px; in: {x:-13, opacity:0, duration:.3})
        p#s(left: 0px; cy: 50%; font-size: 23px; font-family: e) 廃棄が減った分
        p#b(right: 0px; cy: 50%; font-size: 31px; color: $good) ＋9.7万円
      div#l2(left: 23px; top: 96px; width: 557px; height: 43px; in: {x:-13, opacity:0, duration:.3})
        p#s(left: 0px; cy: 50%; font-size: 23px; font-family: e) 値下げ額が増えた分
        p#b(right: 0px; cy: 50%; font-size: 31px; color: $ai) −3.8万円
      div#sum(left: 15px; top: 148px; width: 573px; height: 77px; border-radius: 13px; background: $good; in: {scaleY:0, opacity:0, duration:.35, ease:'back.out(1.6)'})
        p#s(left: 17px; cy: 50%; font-size: 24px; color: #FFFFFF) 差し引き ロスが減った
        p#b(right: 17px; cy: 50%; font-size: 56px; line-height: 1; color: #FFFFFF; white-space: nowrap) 5.9{t9}万円分{/}

# 05 家庭: アンケートの問い → 確かめない人 / 確かめる人の 100 マス (VS) → 語で 40 個・17 個を塗り % を数える → 冷蔵庫を撮る札が下から入り、シャッターの白い閃光
section#home
board#hm(n: "05"; t: "家庭でできる1つの工夫")
  p#ttl(font-size: 29px)
  bsub#sub 来店客240人
  p#q(left: 27px; top: 87px; width: 603px; text-align: center; font-size: 21px; line-height: 1.32; in: {y:13, opacity:0, duration:.4}; delay: 50) 店頭アンケート：{mk}同じ物を二重に買って捨てた{/}ことが[br]月1回以上ある人の割合
  # 比べる 2 列 (題 3 段 + 100 マス + 大きい % + 人数)
  div#ga(left: 16px; top: 153px; width: 288px; height: 407px; border-radius: 20px; background: #FFF1EC; in: {y:33, opacity:0, duration:.45, ease:'back.out(1.4)'})
    p#h1(left: 0px; top: 9px; width: 288px; text-align: center; font-size: 17px; font-family: e; color: $ink2) 買い物前に冷蔵庫を
    p#h2(left: 0px; top: 31px; width: 288px; text-align: center; font-size: 29px; color: $ai) 確かめない人
    p#h3(left: 0px; top: 67px; width: 288px; text-align: center; font-size: 17px; font-family: e; color: $ink2) 140人（58%）
    div#don(left: "35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3"; top: "96;96;96;96;96;96;96;96;96;96;118;118;118;118;118;118;118;118;118;118;140;140;140;140;140;140;140;140;140;140;162;162;162;162;162;162;162;162;162;162"; width: 19px; height: 19px; border-radius: 99px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×40
    div#doff(left: "35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3"; top: "184;184;184;184;184;184;184;184;184;184;206;206;206;206;206;206;206;206;206;206;228;228;228;228;228;228;228;228;228;228;250;250;250;250;250;250;250;250;250;250;272;272;272;272;272;272;272;272;272;272;294;294;294;294;294;294;294;294;294;294"; width: 19px; height: 19px; border-radius: 99px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×60
    p#pct(left: 0px; top: 320px; width: 288px; text-align: center; font-size: 69px; line-height: 1; color: $ai; in: {scale:.6, opacity:0, duration:.3, ease:'back.out(2)'}) [count:40 start=0 ms=600 ease=cubic_out]{pu}%{/}
    p#cnt(left: 0px; top: 387px; width: 288px; text-align: center; font-size: 16px; font-family: e; color: $ink2; in: {opacity:0, duration:.3}) 140人中 56人
  div#gb(left: 352px; top: 153px; width: 288px; height: 407px; border-radius: 20px; background: #EEF8F1; in: {y:33, opacity:0, duration:.45, ease:'back.out(1.4)'})
    p#h1(left: 0px; top: 9px; width: 288px; text-align: center; font-size: 17px; font-family: e; color: $ink2) 買い物前に冷蔵庫を
    p#h2(left: 0px; top: 31px; width: 288px; text-align: center; font-size: 29px; color: $good) 確かめる人
    p#h3(left: 0px; top: 67px; width: 288px; text-align: center; font-size: 17px; font-family: e; color: $ink2) 100人
    div#don(left: "35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3"; top: "96;96;96;96;96;96;96;96;96;96;118;118;118;118;118;118;118"; width: 19px; height: 19px; border-radius: 99px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×17
    div#doff(left: "189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3;35.3;57.3;79.3;101.3;123.3;145.3;167.3;189.3;211.3;233.3"; top: "118;118;118;140;140;140;140;140;140;140;140;140;140;162;162;162;162;162;162;162;162;162;162;184;184;184;184;184;184;184;184;184;184;206;206;206;206;206;206;206;206;206;206;228;228;228;228;228;228;228;228;228;228;250;250;250;250;250;250;250;250;250;250;272;272;272;272;272;272;272;272;272;272;294;294;294;294;294;294;294;294;294;294"; width: 19px; height: 19px; border-radius: 99px; background: #E9E0D3; in: {scale:0, duration:.25, stagger: {each: .004}}) ×83
    p#pct(left: 0px; top: 320px; width: 288px; text-align: center; font-size: 69px; line-height: 1; color: $good; in: {scale:.6, opacity:0, duration:.3, ease:'back.out(2)'}) [count:17 start=0 ms=500 ease=cubic_out]{pu}%{/}
    p#cnt(left: 0px; top: 387px; width: 288px; text-align: center; font-size: 16px; font-family: e; color: $ink2; in: {opacity:0, duration:.3}) 100人中 17人
  div#vs(left: 311px; top: 293px; width: 35px; height: 35px; border-radius: 99px; background: $ink; in: {scale:0, duration:.3, ease:'back.out(2)'})
    p#t(cx: 50%; cy: 50%; font-size: 15px; color: #FFFFFF) VS
  # 工夫の札 (緑の縁・左に冷蔵庫を撮る絵が上へはみ出す)
  div#tip(left: 16px; top: 571px; width: 624px; height: 148px; border-radius: 20px; background: #E8F6EC; border: 3px solid $good; in: {y:173, opacity:0, duration:.5, ease:'power3.out'})
    # hf の作り: 絵は札の上へ 9 px はみ出す (child_overflow)
    img#img(left: 15px; top: -9px; width: 167px; height: 167px; object-fit: contain; main: none; transform-origin: 50% 80%; content: @fridge)
    p#s(left: 200px; top: 15px; font-size: 19px; font-family: e; color: $ink2) 出かける前に
    p#b(left: 200px; top: 44px; font-size: 37px; line-height: 1.15; white-space: nowrap) 冷蔵庫をスマホで1枚
    p#p(left: 200px; top: 92px; font-size: 20px; font-family: e; white-space: nowrap) 二重買いは {hb}半分以下{/} になりうる
  # シャッターの白い閃光 (板の上だけ)
  div#fl(inset: 0; border-radius: 29px; background: #FFFFFF; opacity: .85; overlap: hm.ga,hm.gb,hm.tip,hm.vs,hm.q; in: none)

# まとめ: 番号の丸つきの札 3 枚が右から語ごとに入り、最後の札で板がゆっくり 1.02 倍に寄る
section#wrap
board#sm(n: "まとめ"; t: "今日のポイント")
  div#c1(left: 21px; top: 93px; width: 613px; height: 197px; border-radius: 21px; background: #FFF8EE; border: 2px solid #F1E0C6; in: {x:53, opacity:0, duration:.45, ease:'back.out(1.4)'})
    div#no(left: 17px; top: 17px; width: 49px; height: 49px; border-radius: 99px; background: $a; in: {scale:0, duration:.35, ease:'back.out(2.4)'})
      p#t(cx: 50%; cy: 50%; font-size: 29px; color: #FFFFFF) 1
    p#a(left: 83px; top: 16px; font-size: 21px; font-family: e) ロスの半分は
    p#b(left: 83px; top: 46px; font-size: 36px; line-height: 1.2; white-space: nowrap) 惣菜・青果・パン{s21} の3つの棚から{/}
    p#p(left: 83px; top: 96px; font-size: 18px; font-family: e; line-height: 1.4; color: $ink2) 山は{ea}日曜{/}（火曜の約1.8倍）
    img#pic(left: "373;449;525"; top: 113px; width: 75px; height: 75px; object-fit: contain; main: none; content: "@souzai;@seika;@pan") ×3
  div#c2(left: 21px; top: 305px; width: 613px; height: 197px; border-radius: 21px; background: #FFF8EE; border: 2px solid #F1E0C6; in: {x:53, opacity:0, duration:.45, ease:'back.out(1.4)'})
    div#no(left: 17px; top: 17px; width: 49px; height: 49px; border-radius: 99px; background: $a; in: {scale:0, duration:.35, ease:'back.out(2.4)'})
      p#t(cx: 50%; cy: 50%; font-size: 29px; color: #FFFFFF) 2
    p#a(left: 83px; top: 16px; font-size: 21px; font-family: e) 値引きシールを
    p#b(left: 83px; top: 46px; font-size: 36px; line-height: 1.2) 2時間早く
    p#p(left: 83px; top: 96px; font-size: 18px; font-family: e; line-height: 1.4; color: $ink2) 惣菜・パンの廃棄は{ea}約3割減{/}[br]値下げ分を引いても{ea}5.9万円分{/}のロス減
    div#mini(right: 29px; top: 41px; width: 115px; height: 115px; border-radius: 99px; background: #FFD84D; border: 5px solid $a; transform: rotate(-10deg))
      p#b(cx: 50%; top: 25px; font-size: 36px; line-height: 1; color: $ai) 半額
      p#s(cx: 50%; top: 66px; font-size: 16px) 17:00〜
  div#c3(left: 21px; top: 517px; width: 613px; height: 197px; border-radius: 21px; background: #FFF8EE; border: 2px solid #F1E0C6; in: {x:53, opacity:0, duration:.45, ease:'back.out(1.4)'})
    div#no(left: 17px; top: 17px; width: 49px; height: 49px; border-radius: 99px; background: $a; in: {scale:0, duration:.35, ease:'back.out(2.4)'})
      p#t(cx: 50%; cy: 50%; font-size: 29px; color: #FFFFFF) 3
    p#a(left: 83px; top: 16px; font-size: 21px; font-family: e) 家では、買う前に
    p#b(left: 83px; top: 46px; font-size: 36px; line-height: 1.2) 冷蔵庫を1枚
    p#p(left: 83px; top: 96px; font-size: 18px; font-family: e; line-height: 1.4; color: $ink2) 二重買いの経験 {ea}40% → 17%{/} の水準へ
    img#pic(left: 467px; top: 55px; width: 133px; height: 133px; object-fit: contain; main: none; content: @fridge)
```

```timeline.txt
#v2
cast n = "明るく親しみやすい若い女性のナレーター、はっきりした声でテンポよく語りかける" speed=115%
silence head=0 tail=220

*** title
[>#subtitle]
bgm music
@n: [silence:500][♪swoosh -5dB -380][>#kick -400][>#l1 -320][>#bd[*] -50]スーパーの食品ロス。その[>#l2 -80][♪perc -60]{e}半分{/}は、たった[>#l3 -100][!#l3{mk} marker +120][♪kira -9dB][!#bd[1] to,{opacity:1, duration:.2} +300][!#bd[1].img filter,duration=250,sat:1 +300][!#bd[1] punch,1.12,duration=320 +300][♪pop -2dB +300][!#bd[2] to,{opacity:1, duration:.2} +440][!#bd[2].img filter,duration=250,sat:1 +440][!#bd[2] punch,1.12,duration=320 +440][♪pop -2dB +440][!#bd[3] to,{opacity:1, duration:.2} +580][!#bd[3].img filter,duration=250,sat:1 +580][!#bd[3] punch,1.12,duration=320 +580][♪pop -2dB +580][!#bd[*].img to,{y:-5, duration:.9, ease:'sine.inOut', repeat:1, yoyo:true, stagger:.15} +1000]{e}3つの棚{/}から出ていました。

*** stage
@n: [silence:200][♪scene -5dB -200]架空のスーパー「[>#st.a.plate -50][♪pophi -3dB]{まるみ屋 ひばり台店|まるみや ひばりだいてん}」で、[|][>#st.a.chips[*] -50][♪pop -3dB -50][♪pop -3dB +100][♪pop -3dB +250]{e}4週間{/}、廃棄を毎日[>#st.a.note]量りました。
@: [<#st.a -250][<#st.ttl -250][<#st.sub -250][>#st.t2 -50][>#st.b -30][♪swoosh -6dB -250]合計[!#st.b.total count][♪perc -2dB][♪pophi -4dB +1000]{e}1,840kg{/}、{売値|うりね}で[>#st.b.yen -50][♪register -5dB][>#st.b.note1 +300]{e}151万8,500円{/}分。[>#st.b.rule -200][>#st.b.perday -50][>#st.b.eq +350][>#st.b.bl +450][>#st.b.bt[*] +100][♪pop -8dB +50][♪pop -8dB +600][♪pop -8dB +1150]毎日、2Lペットボトル[>#st.b.bv][♪pophi -2dB][>#st.b.note2 +300]{e}33本{/}分です。

*** shelves
@n: [silence:200][♪scene -5dB -200][>#sh.r[*] {stagger:{each:.07}} +50][♪swoosh -8dB +50]最多は[>#sh.band.b1 -50][!#sh.r[1].nm punch,1.16,duration=360,pivot=left][♪pop -4dB]惣菜。[||][>#sh.band.b2 -50][!#sh.r[2].nm punch,1.16,duration=360,pivot=left][♪pop -4dB]青果、[>#sh.band.b3 -50][!#sh.r[3].nm punch,1.16,duration=360,pivot=left][♪pop -4dB]パンと続き、[|][>#sh.sumw -50][>#sh.sumw.s1 +150][>#sh.sumw.s2 +150][>#sh.sumw.s3 +150]この3つで[!#sh.sumw.pct count -100][!#sh.sumw.pct punch,1.1,duration=400,pivot=left +700][♪kira -9dB]{e}50.5%{/}です。
@: でも[!#sh.tg.knob to,{x:98, duration:.3, ease:'power2.inOut'}][!#sh.tg.w recolor,$ink,duration=200][!#sh.tg.m recolor,#FFFFFF,duration=200 +100][<#sh.uw][>#sh.um +150][<#sh.band][<#sh.sw][<#sh.lg][<#sh.r[*].vw +50][!#sh.r[2].bar to,{scaleX:0.2727, duration:.6, ease:'power3.inOut', pivot:'left'} +120][!#sh.r[3].bar to,{scaleX:0.8182, duration:.6, ease:'power3.inOut', pivot:'left'} +120][!#sh.r[4].bar to,{scaleX:0.4118, duration:.6, ease:'power3.inOut', pivot:'left'} +120][!#sh.r[5].bar to,{scaleX:1.3629, duration:.6, ease:'power3.inOut', pivot:'left'} +120][!#sh.r[6].bar to,{scaleX:1.2732, duration:.6, ease:'power3.inOut', pivot:'left'} +120][!#sh.r[7].bar to,{scaleX:0.4544, duration:.6, ease:'power3.inOut', pivot:'left'} +120][!#sh.r[2] to,{y:192, duration:.7, ease:'power3.inOut'} +250][!#sh.r[3] to,{y:64, duration:.7, ease:'power3.inOut'} +250][!#sh.r[4] to,{y:128, duration:.7, ease:'power3.inOut'} +250][!#sh.r[5] to,{y:-192, duration:.7, ease:'power3.inOut'} +250][!#sh.r[6] to,{y:-192, duration:.7, ease:'power3.inOut'} +250][>#sh.r[*].vm +800][>#sh.rk1 +950][>#sh.rk2 +1100][<#sh.sumw +100][♪click][♪register -5dB +50][♪pophi -5dB +750]{e}金額{/}では話が別。[>#sh.summ]1kgあたり、[|][>#sh.summ.pc[1]][♪pop -3dB]精肉{e}1,500円{/}、[|][>#sh.summ.pc[2]][♪pop -3dB]惣菜{e}1,100円{/}、青果は[>#sh.summ.pc[3]][♪pop -3dB][>#sh.summ.note +400]{e}300円{/}。
@: 重さか金額かで、[|][>#sh.point -100][♪pophi -3dB]「大きい棚」は{e}入れ替わります{/}。

*** days
@n: [silence:200][♪scene -5dB -200][>#dy.col[*] +80][>#dy.cv[*] +300][>#dy.avg +800][>#dy.avgl +1100][♪swoosh -8dB +80]曜日別では[>#dy.tmax][!#dy.col[7] to,{scaleX:1.12, duration:.18, ease:'power2.out'}][!#dy.col[7] to,{scaleX:1, duration:.18, ease:'power2.in'} +180][♪pophi -3dB]{e}日曜{/}が最多で、[>#dy.tmin]火曜の[>#dy.bai -100][♪kira -10dB]{e}約1.8倍{/}。
@: [>#dy.w[1] +140][♪pop -3dB +140]昼の客足に合わせて多めに作った惣菜が、[|][>#dy.arw -250][>#dy.w[2]][♪pop -3dB]{e}夕方{/}、[>#dy.stamp -250][♪stamp -2dB +50]売れ残るんです。

*** exp
@n: [silence:200][♪scene -5dB -200]そこで、[>#ex.a.it[*] -100][♪pop -4dB]惣菜とパンの{e}半額シール{/}を[|][!#ex.a.clk.mh to,{rotation:-720, duration:.95, ease:'power2.inOut'}][!#ex.a.clk.hh to,{rotation:150, duration:.95, ease:'power2.inOut'}][>#ex.a.clk.arc +500][!#ex.a.t19 strike,$ink +300][♪click -5dB +100][♪click -5dB +320][♪click -5dB +540][♪click -5dB +760]{e}2時間早め{/}、[>#ex.a.t17 -150][>#ex.a.early +250]17時に[>#ex.a.it[1].st -170][>#ex.a.it[2].st +30][>#ex.a.notea +300][♪stamp +50][♪stamp -1dB +250]貼ってみると、
@: [<#ex.a -220][>#ex.b -20][>#ex.b.res.b1 +100][>#ex.b.res.b3 +200][>#ex.b.res.b2 +570][>#ex.b.res.b4 +690][>#ex.b.res.v1 +720][>#ex.b.res.v2 +800][>#ex.b.res.v3 +880][>#ex.b.res.v4 +960][♪swoosh -6dB -50]2週間で、廃棄は[>#ex.b.res.d1 -200][>#ex.b.res.d2 -50]{e}約3割{/}、[>#ex.b.res.tot -200][!#ex.b.res.tot.b settle,1.3,duration=350][♪correct -5dB]{e}93kg{/}減。
@: [>#ex.b.rc -50][>#ex.b.rc.l1 +150][>#ex.b.rc.l2 +470][♪swoosh -8dB -20]値下げが増えた分を引いても、[|][>#ex.b.rc.sum -100][!#ex.b.rc.sum.b settle,1.4,duration=350][♪register -3dB]{e}5万9,000円{/}分ロスが減りました。

*** home
@n: [silence:200][♪scene -5dB -200]家庭では、[>#hm.ga -250][>#hm.gb -100][>#hm.vs +200][>#hm.ga.don[*] +100][>#hm.ga.doff[*] +260][>#hm.gb.don[*] +500][>#hm.gb.doff[*] +568][♪pop -5dB]冷蔵庫を確かめず[|]買い物に行く人の[!#hm.ga.don[*] fill,#E8502F,duration=200 stagger=12 -200][>#hm.ga.pct count -120][♪pophi -3dB]{e}40%{/}が、[|][>#hm.ga.cnt]月1回以上、{e}二重買い{/}で食品を捨てていました。
@: 確かめる人は[!#hm.gb.don[*] fill,#24935C,duration=200 stagger=20 -300][>#hm.gb.pct count -120][>#hm.gb.cnt +300][♪pophi -3dB]{e}17%{/}。
@: [>#hm.tip][♪swoosh -6dB +20]出かける前に、冷蔵庫を{e}スマホで1枚{/}[>#hm.fl +220][!#hm.fl to,{opacity:0, duration:.45, ease:'power2.out'} +280][!#hm.tip.img to,{rotation:-4, duration:.12, yoyo:true, repeat:1} +220][♪shutter +220]撮るだけで、[|]二重買いは[!#hm.tip.p{hb} punch,1.25,duration=400][♪correct -5dB]{e}半分以下{/}になりえます。

*** wrap
@n: [silence:200][♪scene -5dB -200][>#sm.c1 -100][>#sm.c1.no][♪pop -3dB]ロスの半分は{e}3つの棚{/}から。[>#sm.c2 -100][>#sm.c2.no][♪pop -3dB]値引きは{e}2時間早く{/}。[||][>#sm.c3 -100][>#sm.c3.no][♪pop -3dB][!#sm to,{scale:1.02, duration:3.2, ease:'sine.inOut'}]家では、{e}冷蔵庫を1枚{/}[♪kira -8dB +1500]。[silence:1.7s]
```

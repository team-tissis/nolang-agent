# concept · game-trick (hf 全力版の全量の写し — サクラスクールシミュレーターで敵と遊ぶ方法・STEP 5 段の裏ワザをゲーム画面風の絵と叩きつける擬音で) — canvas 1920x1080

見せる作り: 場面ごとの全面のゲーム画面風の絵 (設定画の基準画像で 2 人を揃える)・4 色の帯が斜めに払う切替・STEP 札の def (黄の札 + 縁取りの題 + 進みの点 5 つ)・語で叩きつける擬音の文字 (極太・紺の縁と影)・2 択の写真の板と「or」と判子・語ごとに光ってチェックが描かれる下準備の札・集中線と揺れと閃光の打撃・切替なしの暗い溜め (1 字ずつの大字 + ドラムロール) から閃光で結果 (星形の爆発の板・ハート・紙吹雪・ファンファーレ)・手順の札を矢印で並べたおさらい・字幕の下の暗い帯

```design.txt
#v2
# 学ぶ作り: ゲームの裏ワザを STEP 1〜5 で見せる。場面ごとに全面のゲーム画面風の絵 (設定画 [ref:@sheet] で 2 人を揃える) + 左上の STEP 札 (黄の札・縁取りの題・進みの点) + 語で叩きつける擬音の文字
# 切替は 4 色の帯が斜めに払う wipe (根の既定)・山場の前だけ切替なしで暗く溜め (ドラムロール)、白い閃光で結果へ (星形の爆発の板 + 1 字ずつ落ちる大字 + ハート + 紙吹雪)
# 字幕は下端の暗い帯の上に縁取りの白字 (語は黄)・溜めと結果の 2 文は字幕を消して画面の大字で見せる・締めは手順の札を矢印で並べたおさらい
# hf b03 game-trick (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#1E1B4B
theme dark
palette pink=#FF4F9A pink_deep=#E0337F yellow=#FFE14D navy=#1E1B4B sky=#38BDF8 cream=#FFFDF5 red=#E11D2E mint=#8FF7B0 hl=#FFF1A8 punch=#FFF36B dot=#FFFFFFD9
# 地の文字は hf と同じ極太の丸ゴシック (円い端の均一な線・いちばん太いウェイト)
font "極太の、均一な単線で描かれたすっきりした丸ゴシック体、線端がやわらかく丸い、和文のかな・漢字と英字、親しみやすくはっきり、スマホの UI や学習動画の字幕向け"
fonts r="極太の、均一な単線で描かれたすっきりした丸ゴシック体、線端がやわらかく丸い、和文のかな・漢字と英字、親しみやすくはっきり、スマホの UI や学習動画の字幕向け"
fonts d="超極太のディスプレイ用ゴシック、線が非常に太くふところが詰まったがっしりした形、和文と英字がそろう、ゲームの題やサムネイル向け"
sfx off
# hf の作り: STEP 札の題・ゲーム名の札・結果の大字は台詞より先に出る (spoiler)・溜めの点は 1 つずつ落ちて 1 秒で結果へ切り替わる (flash_text)・攻撃の場面は合図・打撃 2 発・切替の音が 5 秒に重なる (se_dense)・山形の 2 回目と 2 つ目の ✓ と「復活！」は切替の直前に出る (entrance_in_fadeout)・締めは大字でなく手順の札の並び (no_closer)・下準備の星の 1 つは字幕の帯に掛かる (caption_collision)・切替の帯は声の終わりの 0.3 秒後から払い始め、締めの字幕は帯の中で出る (transition_over_speech・entrance_in_transition)
lint off=spoiler,flash_text,se_dense,entrance_in_fadeout,no_closer,caption_collision,transition_over_speech,entrance_in_transition
art "明るい学園生活シミュレーターのスマホゲームの画面のような 3D アニメ調。トゥーンシェードで頭が少し大きく目の大きなキャラクター、なめらかでシンプルな質感、明るく彩度の高いパステルの色、すっきりした背景"
prompt_tail "画像の中に文字・数字・UI・ロゴ・透かしは入れない"
# 設定画 (3 人の全身の並び) を 1 枚作り、各場面の絵はこれを基準に人物だけを描き直す
image sheet = "キャラクターの設定画。明るい暖かい灰色の無地の背景に、3 人の全身を同じ大きさで横に並べて正面向きに立たせる。左: つやのある黒髪のショートボブにまっすぐな前髪、大きな琥珀色の目の日本の女子高生。白い襟線の紺のセーラー服に赤いリボン、紺のプリーツスカート、白いソックスに茶色のローファー。中央: 同じ黒髪ボブの女子高生が神父の服を着た姿 (首から足首まで小さなボタンが並ぶ長い黒のキャソック、白いローマンカラー、小さな銀の十字架のペンダント)。右: 険しい顔の強面の敵キャラの男。背が高く黒いスーツに襟を開けた白シャツ、オールバックの黒髪、黒いサングラス。" aspect=3:2
# 反撃の場面と溜めの場面で同じ絵を使う (溜めは暗い幕を掛けて寄る)
image seat = "[ref:@sheet]晴れた町の通りで、黒スーツにサングラスの敵の男が銀色の車椅子におとなしく座り、両手をひざに置いて驚いた素直な顔をしている。神父の服の黒髪ボブの女子高生が車椅子の後ろでハンドルを握ってにっこり笑う。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。" aspect=16:9
sound sweep = "ノイズが短く駆け上がるスイープ音"
sound jan = "ジャン！と鳴る驚きの短い一撃"
sound step = "ピコンと高く短く鳴るひらめきの合図音"
sound pop = "クイズの早押しボタンのピコピコッという電子音"
sound down = "格闘ゲームでキャラが倒れるドサッという音"
sound revive = "ゲームのレベルアップや回復のキラキラと上がる音"
sound item = "レトロゲームでアイテムを取った時の短い電子音"
sound change = "シャキーンと鳴る変身の効果音"
sound get = "宝物やアイテムを手に入れた時のきらびやかな音"
sound punch = "重いパンチのバシッという打撃音"
sound punch_echo = "パンチの打撃の残響"
sound lift = "スライドホイッスルが短く上がるヒューッという音"
sound alarm = "短い警告のアラーム音"
sound seat = "格闘ゲームの着地のストンという音"
sound drum = "ドラムロールの後にシンバルが鳴る結果発表の音"
sound sparkle = "キラリンと光る高い音"
sound fanfare = "短く華やかなファンファーレ"
sound cheer = "イェーイという歓声と拍手"
run y { color: $yellow }
cut { stagger: 0ms }
p { color: #FFFFFF; white-space: nowrap; out: none }
div { border: none; out: none }
img { out: none }
svg { out: none }
shape { out: none }
icon { out: none }
group { out: none }
bgm#music(fade: 350,300) ピコピコした電子音と跳ねるリズムの明るく軽快なエレクトロニカ、可愛くコミカルなゲーム実況向け、124 BPM
# 溜めで止めた曲を結果の後に同じ曲の続きの位置から戻す (2 本目の層)
bgm#music_b(fade: 500,2000) ピコピコした電子音と跳ねるリズムの明るく軽快なエレクトロニカ、可愛くコミカルなゲーム実況向け、124 BPM
# 字幕: 縁取りの白字・文で 1 枚・語は {y} で黄・下端の暗い帯 (sub_band) の上
subtitle(left: 0px; bottom: 46px; width: 1920px; font-size: 64px; line-height: 1.3; letter-spacing: 0.02em; text-align: center; color: #FFFFFF; -webkit-text-stroke: 10px $navy; background: none; padding: 0px; unit: sentence; lead: 60ms; tail: 0ms; hold: next,400ms; in: {y:14, opacity:0, duration:0.14, ease:'power2.out'}; out: none)
# 札は次の札まで最大 400 ms 残り (hold)、cut の最後の札は声の終わりで消える (tail 0) — 字幕は切替の帯より上に描かれるので帯に被らせない
# 全編の層: 字幕の下の暗い帯 (溜めと結果で to で消して締めで戻す)・全面の白い閃光 (攻撃・すぐに・結果の語で to)
div#sub_band(left: 0px; top: 810px; width: 1920px; height: 270px; background: linear(#120E3000,#120E3080@55%,#120E30C7,180); border-radius: 24px; in: {opacity:0, duration:0.3})
veil#flash(color: #FFFFFF; opacity: 0; z-index: curtain; in: none)
# 部品の svg (4 方向の星・点線の輪・上向きの山形・ハート・警告の三角・集中線・桃の斜めの縞・星形の爆発の板)
svg star = """<svg viewBox="-50 -50 100 100"><path d="M0 -48 C6 -10 10 -6 48 0 C10 6 6 10 0 48 C-6 10 -10 6 -48 0 C-10 -6 -6 -10 0 -48 Z" fill="#FFFBE0" stroke="#FFB3D4" stroke-width="4"/></svg>"""
svg ring = """<svg viewBox="0 0 420 420"><circle cx="210" cy="210" r="180" fill="none" stroke="#FFE14D" stroke-width="16" stroke-dasharray="40 22"/><circle cx="210" cy="210" r="180" fill="none" stroke="#1E1B4B" stroke-width="5" stroke-dasharray="40 22" opacity="0.6"/></svg>"""
svg chevron = """<svg viewBox="0 0 90 90"><path d="M12 62 L45 26 L78 62" fill="none" stroke="#1E1B4B" stroke-width="26" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 62 L45 26 L78 62" fill="none" stroke="#FFE14D" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg heart = """<svg viewBox="0 0 86 78"><path d="M43 74 C18 56 4 42 4 24 C4 12 13 4 24 4 C32 4 39 9 43 16 C47 9 54 4 62 4 C73 4 82 12 82 24 C82 42 68 56 43 74 Z" fill="#FF5FA8" stroke="#1E1B4B" stroke-width="6"/><ellipse cx="26" cy="22" rx="8" ry="5" fill="#FFFFFF" opacity="0.7"/></svg>"""
svg warn_tri = """<svg viewBox="0 0 92 82"><path d="M46 4 L88 78 L4 78 Z" fill="#FFE14D" stroke="#1E1B4B" stroke-width="7" stroke-linejoin="round"/><rect x="41" y="26" width="10" height="30" rx="4" fill="#1E1B4B"/><circle cx="46" cy="66" r="6" fill="#1E1B4B"/></svg>"""
svg speed = """<svg viewBox="0 0 1280 720"><defs><radialGradient id="g" gradientUnits="userSpaceOnUse" cx="819" cy="144" r="427"><stop offset="0.4" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.95"/></radialGradient></defs><path d="M819 144 L2519 144 L2519 183ZM819 144 L2508 336 L2503 375ZM819 144 L2475 526 L2466 564ZM819 144 L2421 711 L2408 748ZM819 144 L2347 889 L2330 924ZM819 144 L2253 1057 L2232 1090ZM819 144 L2140 1214 L2116 1244ZM819 144 L2011 1357 L1983 1383ZM819 144 L1866 1484 L1835 1507ZM819 144 L1707 1593 L1674 1613ZM819 144 L1537 1685 L1502 1701ZM819 144 L1358 1756 L1322 1768ZM819 144 L1172 1807 L1135 1814ZM819 144 L982 1836 L944 1839ZM819 144 L789 1844 L751 1843ZM819 144 L597 1829 L559 1824ZM819 144 L408 1794 L370 1784ZM819 144 L224 1736 L188 1722ZM819 144 L47 1659 L13 1641ZM819 144 L-119 1562 L-151 1540ZM819 144 L-274 1446 L-303 1421ZM819 144 L-414 1314 L-440 1286ZM819 144 L-539 1167 L-562 1136ZM819 144 L-646 1007 L-665 973ZM819 144 L-734 835 L-749 800ZM819 144 L-802 655 L-813 618ZM819 144 L-850 468 L-857 430ZM819 144 L-876 277 L-878 239ZM819 144 L-880 85 L-878 46ZM819 144 L-862 -107 L-856 -145ZM819 144 L-823 -296 L-813 -333ZM819 144 L-763 -479 L-748 -515ZM819 144 L-682 -654 L-664 -688ZM819 144 L-582 -819 L-560 -850ZM819 144 L-464 -971 L-438 -1000ZM819 144 L-330 -1109 L-301 -1135ZM819 144 L-180 -1231 L-149 -1254ZM819 144 L-18 -1336 L16 -1354ZM819 144 L155 -1421 L190 -1436ZM819 144 L336 -1486 L373 -1497ZM819 144 L524 -1530 L562 -1536ZM819 144 L715 -1553 L754 -1555ZM819 144 L908 -1554 L946 -1551ZM819 144 L1100 -1533 L1138 -1526ZM819 144 L1288 -1490 L1325 -1479ZM819 144 L1470 -1427 L1505 -1411ZM819 144 L1643 -1343 L1677 -1324ZM819 144 L1806 -1240 L1837 -1217ZM819 144 L1957 -1119 L1985 -1093ZM819 144 L2092 -982 L2117 -953ZM819 144 L2212 -831 L2233 -799ZM819 144 L2313 -667 L2331 -633ZM819 144 L2395 -493 L2409 -457ZM819 144 L2457 -310 L2467 -273ZM819 144 L2498 -122 L2504 -84Z" fill="url(#g)"/></svg>"""
svg stripes = """<svg viewBox="0 0 1280 720"><defs><pattern id="p" width="61" height="61" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="31" height="61" fill="#FFC1DC"/><rect x="31" width="30" height="61" fill="#FFD9EA"/></pattern></defs><rect width="1280" height="720" fill="url(#p)"/></svg>"""
svg burst = """<svg viewBox="0 0 1880 500"><polygon points="1814.0,250.0 1640.4,269.1 1828.9,299.0 1616.4,307.0 1779.3,347.0 1557.1,342.4 1645.2,382.9 1474.2,374.8 1514.1,415.4 1368.7,403.1 1373.6,444.9 1227.1,417.3 1210.7,466.2 1093.7,437.6 1033.1,479.8 940.0,438.4 850.2,471.6 788.9,434.4 671.4,464.5 652.6,417.5 486.9,453.6 505.6,405.1 360.3,417.0 397.2,376.8 208.0,388.0 304.1,345.3 126.7,343.9 279.8,305.7 53.0,298.9 207.8,270.0 77.8,250.0 218.6,230.3 64.7,201.7 279.6,194.3 113.4,154.5 314.6,156.3 204.7,111.4 419.9,128.5 356.8,82.0 528.9,103.2 496.4,50.7 654.2,83.4 669.0,33.6 787.5,63.8 848.2,23.5 940.0,64.9 1034.3,17.3 1086.4,71.3 1211.9,32.9 1240.8,74.7 1368.0,57.7 1365.7,98.0 1541.6,76.6 1459.9,128.5 1673.4,111.7 1573.8,155.1 1728.7,158.9 1631.5,191.7 1772.5,204.1 1675.3,229.9" fill="#FF4F9A" stroke="#1E1B4B" stroke-width="12" stroke-linejoin="round"/></svg>"""

# STEP 札: 黄の札 (STEP + 番号・傾き -4°) → 縁取りの題 → 進みの点 5 つ (済 = 黄・今 = 桃の横長)。札・題・点は切替の帯が過ぎてから順に出る
def step_tag(n, t, w, ta, pl, dl, dw, dc) = div(width: {w}; height: 210px)
  div#pill(left: {pl}; top: 0px; width: 255px; height: 84px; background: $yellow; border: 6px solid $navy; border-radius: 18px; box-shadow: 0px 8px 0px $navy; transform: rotate(-4deg); delay: 490ms; in: {scale:2.2, opacity:0, rotation:-24, duration:0.34, ease:'back.out(2.2)'})
    p#s(left: 20px; top: 22px; width: 138px; font-family: d; font-size: 38px; line-height: 1.25; color: $navy) STEP
    p#n(left: 162px; top: 0px; width: 75px; font-family: d; font-size: 66px; line-height: 1.2; color: $navy; content: {n})
  p#t(left: 0px; top: 93px; width: {w}; font-size: 64px; line-height: 1.3; text-align: {ta}; -webkit-text-stroke: 10px $navy; text-shadow: 0px 8px 0px $pink_deep; delay: 610ms; in: {x:-60, opacity:0, duration:0.36, ease:'power3.out'}; content: {t})
  div#dot(left: {dl}; top: 186px; width: {dw}; height: 22px; border-radius: 148px; background: {dc}; border: 4px solid $navy; delay: 710ms; in: {scale:0, duration:0.22, ease:'back.out(3)', stagger:{each:0.04}}) ×5
# 擬音の文字 (極太の角ゴシック・黄・紺の縁 + 紺の落ち影)
def sfx = p(font-family: d; color: $yellow; -webkit-text-stroke: 12px $navy; text-shadow: 0px 8px 0px $navy)
# 札の文字 (白地・紺の縁・紺の硬い影)
def plate = p(width: 276px; font-size: 84px; text-align: center; color: $navy; background: #FFFFFF; border: 8px solid $navy; border-radius: 22px; padding: 0px 44px 8px 44px; box-shadow: 0px 9px 0px $navy; in: {y:120, opacity:0, duration:0.35, ease:'back.out(2)'})
# 下準備の行: 黄の光 (語で点ける) + アイテムの絵 + 小見出し + 本文 + チェックの枠と描かれる ✓
def prep_row(s, b, pic) = div(width: 686px; height: 140px; in: {x:60, opacity:0, duration:0.3, ease:'power2.out'})
  div#hl(left: 10px; top: 6px; width: 664px; height: 128px; border-radius: 20px; background: $hl; in: {opacity:0, duration:0.2}; out: {opacity:0, duration:0.2})
  img#icon(left: 26px; cy: 50%; width: 112px; height: 112px; object-fit: contain; main: none; content: {pic})
  p#s(left: 158px; top: 20px; font-size: 28px; color: $pink_deep; content: {s})
  p#b(left: 158px; top: 52px; font-size: 50px; line-height: 1.15; color: $navy; content: {b})
  div#box(right: 26px; cy: 50%; width: 74px; height: 74px; border-radius: 18px; background: #FFFFFF; border: 6px solid $navy)
  icon#ck(right: 20px; top: 18px; font-size: 81px; name: check; weight: bold; color: $pink; in: draw {duration: 0.3})
# おさらいの札 (番号の桃の丸 + 語)
def chip(n, t) = p(font-size: 34px; color: $navy; background: $cream; border: 4px solid $navy; border-radius: 148px; padding: 6px 20px 8px 64px; box-shadow: 0px 6px 0px $navy; content: {t})
  p#n(left: 6px; cy: 50%; width: 46px; font-size: 26px; line-height: 1; text-align: center; background: $pink; border-radius: 148px; padding: 10px 0px; content: {n})

# 題: 桜並木の町の 2 人に寄りから引き、ゲーム名の桃の札が上から弾み、題が 1 字ずつ弾んで出て、「裏ワザ」の判子が叩きつけられる
section#title
img#title_bg(inset: 0; main: keys(at=0 scale=1.14 | at=0.25 scale=1 ease=power3.out | at=1 scale=1.04 ease=none),duration=6320,pivot=50%,40%) [ref:@sheet]春の晴れた日本の町の大通りの広い引きの構図。満開の桜並木、遠くに時計塔のある近代的な高校の校舎、青空にやわらかな雲。右下の手前にセーラー服の黒髪ボブの女子高生が腰に手を当てて自信たっぷりに笑って立ち、左下の手前に黒スーツの敵の男が腕を組んで彼女をにらんで立つ。二人とも全身が見え、小さめに描いて画面の中央と上半分を空ける。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。
svg#title_star(left: "406;644;498;507;643;526;882;473;525;412"; top: "424;359;376;331;336;374;341;330;375;417"; width: "19;39;32;40;41;29;27;44;23;41"; height: "19;39;32;40;41;29;27;44;23;41"; part: star; delay: 600ms; in: {scale:0.2, opacity:0, rotation:-90, duration:0.45, ease:'power2.out', stagger:{each:0.37}}) ×10
p#game_pill(cx: 960px; top: 118px; font-size: 50px; letter-spacing: 0.04em; background: $pink; border: 6px solid $navy; border-radius: 148px; padding: 10px 44px 14px 44px; box-shadow: 0px 8px 0px $navy; delay: 120ms; in: {y:-160, opacity:0, duration:0.55, ease:'back.out(1.8)'}) サクラスクールシミュレーター
p#title_main(cx: 960px; top: 240px; width: 1110px; text-align: center; font-size: 164px; line-height: 1.15; letter-spacing: 0.05em; color: $yellow; -webkit-text-stroke: 16px $navy; text-shadow: 0px 12px 0px $pink_deep; delay: 250ms; in: {scale:0, y:60, rotation:-14, opacity:0, duration:0.42, ease:'back.out(2.6)', stagger:{each:0.07}}) 敵と遊ぶ方法
div#title_stamp(left: 1418px; top: 26px; width: 190px; height: 190px; border-radius: 148px; background: $red; border: 8px solid #FFFFFF; box-shadow: 0px 10px 0px 6px $navy; transform: rotate(-12deg); in: {scale:3, rotation:-40, opacity:0, duration:0.2, ease:'power3.in'})
  p#t(cx: 50%; cy: 50%; font-size: 56px; line-height: 1.02; text-align: center) 裏[br]ワザ

# STEP 1 ダウン: のびた敵の絵・右上の STEP 札・「敵キャラ」の桃の札・「ダウン」で点線の輪が回り出し「ドサッ！」が叩きつけられて弾む
section#down
img#down_bg(inset: 0; main: kb {scale: [1, 1.08], focus: ['56% 40%', '56% 40%']}) [ref:@sheet]桜並木のある晴れた町の歩道で、黒スーツの敵の男が仰向けに大の字でのびている。目はマンガのぐるぐるの渦、頭の上を小さな黄色い星が回る (コミカルで無害、けがはない)。そばでセーラー服の黒髪ボブの女子高生が元気にピースサイン。少し高い位置から見下ろす構図。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。
step_tag#tag_down(left: 1340px; top: 44px; n: 1; t: 敵キャラをダウン; w: 525px; ta: right; pl: 270px; dl: "227;266;289;312;335"; dw: "31;15;15;15;15"; dc: "$pink;$dot;$dot;$dot;$dot")
svg#down_ring(left: 844px; top: 150px; width: 420px; height: 420px; part: ring; in: {scale:0.3, opacity:0, rotation:-90, duration:0.45, ease:'back.out(1.6)'})
p#down_label(left: 752px; top: 104px; width: 306px; text-align: center; font-family: d; font-size: 58px; background: $pink; border: 6px solid $navy; border-radius: 20px; padding: 4px 26px 10px 26px; box-shadow: 0px 8px 0px $navy; transform-origin: 0% 100%; in: {scale:0, opacity:0, duration:0.3, ease:'back.out(2.4)'}) 敵キャラ
sfx#down_sfx(left: 1260px; top: 520px; font-size: 132px; transform: rotate(-10deg); in: {scale:2.4, opacity:0, duration:0.2, ease:'power3.in'}) ドサッ！

# STEP 2 復活: 病院の前で光に包まれて立ち上がる敵・左上の STEP 札・下から昇って消える星 14 個 (7 個ずつ 2 列)・「復活」で緑の「復活！」が弾んで脈打つ
section#revive
img#revive_bg(inset: 0; main: kb {scale: [1, 1.08], focus: ['45% 30%', '45% 30%']}) [ref:@sheet]画面には一人だけ。明るい町の白い病院の入口の前で、黒スーツにサングラスの敵の男が再び立ち上がり復活している。金色の回復の光の柱とキラキラの粒に包まれ、少しぼうっとした様子。ファンタジーゲームの復活の演出、明るい雰囲気。設定画の人物のうち、この男だけを新しい自然なポーズで描き、設定画の並びは写さない。
step_tag#tag_revive(left: 56px; top: 44px; n: 2; t: キャラを復活させる; w: 690px; ta: left; pl: 0px; dl: "4;27;66;89;112"; dw: "15;31;15;15;15"; dc: "$yellow;$pink;$dot;$dot;$dot")
svg#rv_a(left: "635;793;635;610;704;461;559"; top: "391;349;391;532;435;192;376"; width: "34;36;21;32;31;23;30"; height: "34;36;21;32;31;23;30"; part: star; delay: 560ms; in: {y:120, scale:0.3, opacity:0, duration:0.6, ease:'power1.out', stagger:{each:0.28}}) ×7
svg#rv_b(left: "668;790;530;401;520;545;790"; top: "372;510;400;471;114;358;112"; width: "22;31;41;26;47;40;36"; height: "22;31;41;26;47;40;36"; part: star; delay: 560ms; in: {y:120, scale:0.3, opacity:0, duration:0.6, ease:'power1.out', stagger:{each:0.28}}) ×7
sfx#revive_sfx(left: 1330px; top: 330px; font-size: 150px; font-family: r; color: $mint; transform: rotate(6deg); in: {scale:0, opacity:0, rotation:-30, duration:0.42, ease:'back.out(2.5)'}) 復活！

# 病院 or 神社: 斜めの縞が流れる桃の地 (縞は svg の pattern を全面に敷き、kb の動かない点を右端から左端へ移して右へ流す)・上の紺の問いの札・語ごとに左右から写真の板と名札が滑り込み、間の「or」が回って出て、「どちらでも」で消えて赤の判子「どっちでもOK！」が叩きつけられ板が揺れる
section#where
svg#where_bg(inset: 0; z-index: back; part: stripes; main: kb {scale: [1.07, 1.07], focus: ['100% 50%', '0% 50%']})
p#where_head(cx: 960px; top: 54px; font-size: 64px; background: $navy; border-radius: 148px; padding: 10px 56px 16px 56px; box-shadow: 0px 8px 0px $pink_deep; delay: 410ms; in: {y:-130, opacity:0, duration:0.4, ease:'back.out(1.7)'}) 復活させる場所は？
img#panel_h(left: 110px; top: 214px; width: 800px; height: 450px; border-radius: 28px; border: 10px solid #FFFFFF; box-shadow: 0px 18px 0px 6px $navy; transform: rotate(-2.5deg); main: kb {scale: [1, 1.12]}; in: {x:-1150, rotation:-12, duration:0.5, ease:'power3.out'}) 明るいアニメ調のゲームの町の、ガラスの入口のある白い近代的な病院の外観。前に小さな救急車、刈り込んだ生け垣と桜の木、晴れた日、人物なし。
img#panel_s(left: 1010px; top: 214px; width: 800px; height: 450px; border-radius: 28px; border: 10px solid #FFFFFF; box-shadow: 0px 18px 0px 6px $navy; transform: rotate(2.5deg); main: kb {scale: [1, 1.12]}; in: {x:1150, rotation:12, duration:0.5, ease:'power3.out'}) 大きな朱色の鳥居、石灯籠、石畳の参道、桜の木に囲まれた木造の社殿のある神社。明るいアニメ調のゲームの町、晴れた日、人物なし。
plate#plate_h(cx: 510px; top: 708px) 病院
plate#plate_s(cx: 1410px; top: 708px) 神社
p#or_badge(left: 880px; top: 360px; width: 160px; font-family: d; font-size: 64px; line-height: 1; text-align: center; color: $navy; background: $yellow; border: 8px solid $navy; border-radius: 148px; padding: 40px 0px; box-shadow: 0px 9px 0px $navy; in: {scale:0, rotation:180, duration:0.4, ease:'back.out(2)'}; out: {scale:0, rotation:-90, duration:0.18, ease:'power2.in'}) or
p#ok_stamp(cx: 960px; top: 360px; font-family: d; font-size: 128px; line-height: 1.2; background: $red; border: 10px solid #FFFFFF; border-radius: 30px; padding: 6px 60px 20px 60px; box-shadow: 0px 16px 0px 8px $navy; transform: rotate(-7deg); in: {scale:2.6, opacity:0, duration:0.2, ease:'power3.in'}) どっちでもOK！

# 下準備: 神父の服の絵 → 文の頭で車椅子が現れる絵へ溶けて替わる・右上のチェックの札 (桃の見出し + 2 行) が右から入り、語ごとに行が黄に光って絵が弾み、文末に ✓ が描かれる・「車椅子」で星と「ゲット！」
section#prep
img#dress_bg(inset: 0; main: kb {scale: [1, 1.06], focus: ['45% 30%', '45% 30%']}) [ref:@sheet]画面には一人だけ。色とりどりの衣装が掛かったかわいく明るい洋服店の中で、神父の服を着た黒髪ボブの女子高生が中央で新しい服を誇らしげに見せる。片手を胸に当てて満面の笑み、まわりに小さなキラキラ、後ろに試着室のカーテン。設定画の人物のうち、この女子高生だけを新しい自然なポーズで描き、設定画の並びは写さない。
img#props_bg(inset: 0; main: kb {scale: [1.08, 1], focus: ['40% 50%', '40% 50%']}; in: {opacity:0, duration:0.35, ease:'power1.inOut'}) [ref:@sheet]桜並木の晴れた町の通りで、銀色の車椅子がキラキラとパステルの煙の中から魔法のように現れ、神父の服の黒髪ボブの女子高生がうれしそうにそれを指さす。画面にあるのは神父の服の女子高生と車椅子だけ。ゲームのアイテム出現の演出。設定画の人物のうち、この女子高生だけを描き、設定画の並びは写さない。
svg#prep_star(left: "609;742;1069;942;1086;959;914;1013;981;766"; top: "515;342;595;340;600;276;661;348;318;464"; width: "23;31;37;21;23;36;35;28;26;44"; height: "23;31;37;21;23;36;35;28;26;44"; part: star; in: {scale:0.2, opacity:0, rotation:-60, duration:0.35, ease:'power2.out', stagger:{each:0.09}}) ×10
sfx#get_sfx(left: 1040px; top: 520px; font-size: 104px; transform: rotate(-8deg); in: {scale:0, opacity:0, duration:0.35, ease:'back.out(2.6)'}) ゲット！
div#prep_card(left: 1167px; top: 40px; width: 700px; height: 399px; background: $cream; border: 8px solid $navy; border-radius: 30px; box-shadow: 0px 12px 0px $navy; delay: 460ms; in: {x:820, rotation:6, duration:0.5, ease:'power3.out'})
  div#head(left: 0px; top: 0px; width: 686px; height: 92px; background: $pink; border-radius: 22px 22px 0px 0px)
    p#t(left: 30px; cy: 50%; font-size: 58px) 下準備
    p#sub(left: 225px; cy: 50%; font-size: 30px; color: $navy; background: $yellow; border-radius: 148px; padding: 4px 18px 6px 18px) 復活させる前に
  div#rule(left: 0px; top: 92px; width: 686px; height: 8px; background: $navy; border-radius: 24px)
  prep_row#r1(left: 0px; top: 99px; s: 着替え; b: 神父に着替える; pic: "[transparent]木のハンガーに掛かった、白いローマンカラーと小さな銀の十字架のペンダントのついた長い黒の神父服。かわいいトゥーンシェードの 3D ゲームの衣装アイテムのアイコン、中央に一つだけ。"; delay: 760ms)
  shape#sep(left: 26px; top: 240px; width: 634px; height: 4px; path: line_h; border: 4px solid #1E1B4B40; dash: 9,7)
  prep_row#r2(left: 0px; top: 244px; s: 小道具から; b: 車椅子を出す; pic: "[transparent]黒い座面の光沢のある銀色の車椅子を斜め前から。かわいいトゥーンシェードの 3D ゲームのアイテムのアイコン、中央に一つだけ。"; delay: 860ms)

# STEP 3 攻撃: パンチの絵・左上の STEP 札・「攻撃」で集中線が点き、絵が揺れ、白く光り、「ドカッ！！」が叩きつけられる
section#attack
img#attack_bg(inset: 0; main: kb {scale: [1.02, 1.1], focus: ['62% 25%', '62% 25%']}) [ref:@sheet]晴れた町の通りで、神父の服の黒髪ボブの女子高生が黒スーツの敵の男にマンガのようなドタバタのパンチを当てる。当たった所に白いマンガの衝撃の星が弾け、男は驚いた顔でのけぞりサングラスが傾く。スピード線、楽しいゲームのアクション、無害で血もけがもない。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。
svg#speedlines(left: 0px; top: 0px; width: 1920px; height: 1080px; part: speed; in: {opacity:0, duration:0.06}; out: {opacity:0, duration:0.5, ease:'power1.in'})
sfx#attack_sfx(left: 1290px; top: 330px; font-size: 120px; color: $punch; transform: rotate(8deg); in: {scale:3, rotation:30, opacity:0, duration:0.2, ease:'power3.in'}) ドカッ！！
step_tag#tag_attack(left: 56px; top: 44px; n: 3; t: 復活したら攻撃; w: 690px; ta: left; pl: 0px; dl: "4;27;50;89;112"; dw: "15;15;31;15;15"; dc: "$yellow;$yellow;$pink;$dot;$dot")

# STEP 4 持ち上げ: 頭上に持ち上げる絵・左下の STEP 札・「持ち上げ」で絵が少し上へ動き、上向きの山形が 2 回ずつ昇り、「ヒョイッ！」が下から弾む
section#lift
img#lift_bg(inset: 0; main: kb {scale: [1, 1.08], focus: ['50% 15%', '50% 15%']}) [ref:@sheet]画面には二人だけ。晴れた町の通りで、神父の服の黒髪ボブの女子高生が気絶した黒スーツの男を両腕で頭の上に高々と持ち上げる (ゲームの物理のありえないコミカルさ)。男は水平にぐったりのび、目はぐるぐる、汗のしずく、ドタバタ喜劇。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。
# 山形: 1 回目 (a と b は 120 ms ずらし) と 2 回目 (c・d)
svg#lift_a(left: "373;887"; top: "240;200"; width: 90px; height: 90px; part: chevron; in: {y:80, opacity:0, duration:0.3, ease:'power2.out'}; out: {y:-50, opacity:0, duration:0.45, ease:'power1.in'}) ×2
svg#lift_b(left: "400;920"; top: "347;313"; width: 90px; height: 90px; part: chevron; in: {y:80, opacity:0, duration:0.3, ease:'power2.out'}; out: {y:-50, opacity:0, duration:0.45, ease:'power1.in'}) ×2
svg#lift_c(left: "373;887"; top: "240;200"; width: 90px; height: 90px; part: chevron; in: {y:80, opacity:0, duration:0.3, ease:'power2.out'}) ×2
svg#lift_d(left: "400;920"; top: "347;313"; width: 90px; height: 90px; part: chevron; in: {y:80, opacity:0, duration:0.3, ease:'power2.out'}) ×2
sfx#lift_sfx(left: 1240px; top: 470px; font-size: 112px; transform: rotate(-6deg); in: {y:90, opacity:0, duration:0.36, ease:'back.out(2.4)'}) ヒョイッ！
step_tag#tag_lift(left: 56px; top: 600px; n: 4; t: 倒れたら持ち上げる; w: 690px; ta: left; pl: 0px; dl: "4;27;50;73;112"; dw: "15;15;15;31;15"; dc: "$yellow;$yellow;$yellow;$pink;$dot")

# STEP 5 反撃 → 車椅子: 暴れる敵の絵で赤い縁が点滅し「反撃に注意！」の札が揺れる → 「すぐに」で白く光って車椅子の絵に切り替わり「すぐに！」→「座らせ」で「ストン」が弾んで絵が沈む
section#counter
img#counter_bg(inset: 0; main: kb {scale: [1, 1.08], focus: ['50% 30%', '50% 30%']}) [ref:@sheet]画面には二人だけ。晴れた町の通りで、神父の服の黒髪ボブの女子高生が黒スーツの男を両腕に抱えているが、男が突然怒って目を覚まし、暴れて拳を振り上げ反撃しようとしている。頭の上にマンガの怒りマークと湯気。女子高生は大きな汗をかいてあわてた顔。コミカルで無害。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。
img#seat_bg(inset: 0; content: @seat; main: kb {scale: [1.12, 1], focus: ['50% 40%', '50% 40%']}; in: none)
div#warn_frame(inset: 0; background: radial(#FF282800,#FF282800@50%,#FF2828A6,50%,50%); border: 16px solid #FF3B3BF2; opacity: 0; border-radius: 24px; in: none)
div#warn_sign(left: 1300px; top: 560px; width: 564px; height: 129px; background: $red; border: 8px solid #FFFFFF; border-radius: 24px; box-shadow: 0px 12px 0px 6px $navy; in: {scale:0, rotation:-25, duration:0.32, ease:'back.out(2.6)'}; out: {scale:0, opacity:0, duration:0.2, ease:'power2.in'})
  svg#tri(left: 22px; cy: 50%; width: 92px; height: 82px; part: warn_tri)
  p#t(left: 132px; cy: 50%; font-size: 64px) 反撃に注意！
sfx#quick_sfx(left: 1310px; top: 330px; font-size: 120px; color: #FFFFFF; transform: rotate(-7deg); in: {scale:2.6, opacity:0, duration:0.2, ease:'power3.in'}; out: {scale:0.8, opacity:0, duration:0.2}) すぐに！
sfx#seat_sfx(left: 1360px; top: 640px; width: 368px; font-size: 104px; transform: rotate(5deg); in: {y:-120, opacity:0, duration:0.3, ease:'bounce.out'}) ストン
step_tag#tag_counter(left: 56px; top: 44px; n: 5; t: すぐ車椅子に座らせる; w: 690px; ta: left; pl: 0px; dl: "4;27;50;73;96"; dw: "15;15;15;15;31"; dc: "$yellow;$yellow;$yellow;$yellow;$pink")

# 溜め: 切替なしで同じ車椅子の絵に寄り続け、周りを暗く沈め、「そうすると」が 1 字ずつ上がり、点が 1 つずつ落ちて弾む (字幕は消す)
section#suspense
img#sus_bg(inset: 0; content: @seat; main: kb {scale: [1, 1.42], focus: ['55% 26%', '55% 26%']})
div#sus_dim(inset: 0; background: radial(#0E0A2826,#0E0A28D1@62%,55%,30%); border-radius: 24px; in: {opacity:0, duration:0.5, ease:'power1.out'})
group#hero_sus(left: 0px; top: 0px; width: 1920px; height: 1080px; transform-origin: 50% 70%)
  p#word(left: 555px; top: 700px; width: 682px; font-family: d; font-size: 120px; letter-spacing: 0.09em; -webkit-text-stroke: 14px $navy; in: {y:50, opacity:0, duration:0.25, ease:'power2.out', stagger:{each:0.15}}) そうすると
  p#dot(left: "hero_sus.word.right-39;hero_sus.word.right+6;hero_sus.word.right+51"; top: 700px; width: 66px; font-family: d; font-size: 120px; -webkit-text-stroke: 14px $navy; in: {y:-40, opacity:0, duration:0.25, ease:'bounce.out', stagger:{each:0.28}}) ×3 .;.;.

# 結果: 白い閃光から駆け寄る敵の絵が弾んで寄り、星形の爆発の板が開いて脈打ち、「呼ぶことができます！！」が 1 字ずつ上から落ち、ハートが昇り、ファンファーレで紙吹雪 (字幕は消す)
section#reveal
img#call_bg(inset: 0; main: keys(at=0 scale=1.22 | at=0.22 scale=1 ease=power3.out | at=1 scale=1.05 ease=none),duration=3220) [ref:@sheet]桜の咲く晴れた町の通りで、神父の服の黒髪ボブの女子高生が片手を挙げて手を振って誰かを呼び、黒スーツにサングラスの男が満面の笑みで忠実な友だちのように彼女の方へ駆け寄ってくる。男のまわりに小さなピンクのハートが浮かぶ、楽しく仲良しの雰囲気。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。
svg#burst(left: 20px; top: 392px; width: 1880px; height: 500px; part: burst; in: {scale:0, rotation:-8, duration:0.42, ease:'back.out(1.8)'})
svg#hearts(left: "753;1040;807;1107;733;1160;1000;820;1200"; top: "80;27;200;133;260;247;180;20;53"; width: 86px; height: 78px; part: heart; in: {y:70, scale:0.2, opacity:0, duration:0.45, ease:'back.out(2)', stagger:{each:0.16}}) ×9
confetti#confetti(left: 180px; top: 90px; width: 1560px; height: 900px; n: 46; dot: 12-20; colors: $pink,$yellow,$sky,$mint,#FFFFFF; drift: down; in: {opacity:0, duration:0.1}; out: {opacity:0, duration:1, ease:'power1.in'})
p#hero_call(cx: 960px; top: 566px; font-family: d; font-size: 120px; letter-spacing: 0.09em; color: $yellow; -webkit-text-stroke: 18px $navy; text-shadow: 0px 12px 0px $pink_deep; in: {y:-260, scale:1.6, opacity:0, duration:0.32, ease:'back.out(2.2)', stagger:{each:0.1}}) 呼ぶことができます！！

# 締め: 夕焼けの校門で手を振る 2 人・「おさらい」の黄の札と、手順の札 6 枚 + 矢印 + 「呼べる！」が左から順に弾んで並び、最後の札が脈打つ・最後は暗い幕で閉じる
section#outro
img#outro_bg(inset: 0; main: kb {scale: [1, 1.06], focus: ['50% 40%', '50% 40%']}) [ref:@sheet]夕焼けの金色の光の中、桜の木のある校門の前で、神父の服の黒髪ボブの女子高生と黒スーツにサングラスの男が仲良しとして並んで立ち、二人とも笑顔でこちらに手を振る。暖かい光、花びらが舞う。設定画の人物のうち、この 2 人だけを新しい自然なポーズで描き、設定画の並びは写さない。
p#recap_label(cx: 960px; top: 608px; width: 264px; text-align: center; font-family: d; font-size: 44px; color: $navy; background: $yellow; border: 6px solid $navy; border-radius: 148px; padding: 2px 34px 8px 34px; box-shadow: 0px 6px 0px $navy; in: {scale:0, duration:0.3, ease:'back.out(2.4)'}) おさらい
chip#rc(left: "61;ra[1].right+10;ra[2].right+10;ra[3].right+10;ra[4].right+10;ra[5].right+10"; top: 705px; n: "1;2;準;3;4;5"; t: "ダウン;復活;神父＋車椅子;攻撃;持ち上げ;車椅子へ"; in: {y:60, opacity:0, duration:0.28, ease:'back.out(2)', stagger:{each:0.14}}) ×6
icon#ra(left: "rc[1].right+6;rc[2].right+6;rc[3].right+6;rc[4].right+6;rc[5].right+6;rc[6].right+6"; cy: 738px; font-size: 33px; name: caret-right; weight: fill; color: $navy; in: {y:60, opacity:0, duration:0.28, ease:'back.out(2)', stagger:{each:0.14}}) ×6
p#recap_goal(left: ra[6].right+6; top: 705px; font-size: 38px; color: $navy; background: $yellow; border: 4px solid $navy; border-radius: 148px; padding: 6px 26px 9px 26px; box-shadow: 0px 6px 0px $navy; in: {y:60, opacity:0, duration:0.28, ease:'back.out(2)'}) 呼べる！
veil#fade_out(color: #0D0B24; opacity: 1; z-index: curtain; in: {opacity:0, duration:1.1, ease:'power1.in'})
```

```timeline.txt
#v2
cast n = "高く明るい 20 代の女性の声、元気でアニメのキャラクターのようにはきはきと、ゲーム紹介のナレーション"
silence head=0ms tail=0ms
# 場面の切替: 右から左へ斜めの 4 色の帯 (紺・桃・黄・空色) が払い、帯の中で場面が替わる (帯は境目の前後 310 ms ずつ)
transition = wipe {duration: .62, dir: 'left', overlap: .31, angle: 16, ease: 'power2.inOut', bars: '#1E1B4B,520;#FF4F9A,600;#FFE14D,440;#38BDF8,440'}

*** title
[>#subtitle]
bgm music
@n: [silence:920ms][♪sweep -2dB -870ms][♪jan +3dB -670ms][>#sub_band -320ms][>#title_stamp +80ms][!#title_stamp to,{scale:1.08, duration:0.18, ease:'power1.out', repeat:1, yoyo:true} +280ms][♪pop -3dB +280ms][!#title_star[*] to,{opacity:0, scale:0.3, rotation:90, duration:0.5, ease:'power2.in', stagger:0.37} +280ms][!#title_main to,{y:-8, duration:0.9, ease:'sine.inOut', repeat:3, yoyo:true} +680ms]今回は、{y}サクラスクールシミュレーター{/}で[br]{y}敵と遊ぶ方法{/}を紹介します。[silence:460ms]

*** down
@n: [silence:320ms][♪step -3dB -100ms]まず、[>#down_label -160ms]遊びたい{y}敵キャラ{/}を[>#down_ring -250ms][!#down_ring to,{rotation:40, duration:1.075, ease:'none'} +200ms][>#down_sfx -200ms][♪down +1dB][!#down_sfx to,{y:10, duration:0.08, ease:'none', repeat:3, yoyo:true} +240ms]{y}ダウン{/}させましょう。[silence:400ms]

*** revive
@n: [silence:380ms][♪step -3dB -160ms][!#rv_a[*] to,{y:-80, opacity:0, duration:0.5, ease:'power1.in', stagger:0.28} +470ms][!#rv_b[*] to,{y:-80, opacity:0, duration:0.5, ease:'power1.in', stagger:0.28} +470ms]次に、そのキャラを[>#revive_sfx][♪revive -1dB][!#revive_sfx to,{scale:1.06, duration:0.35, ease:'sine.inOut', repeat:1, yoyo:true} +450ms]{y}復活{/}させます。[silence:290ms]

*** where
@n: [silence:420ms][>#panel_h -220ms][♪pop -2dB -80ms][>#plate_h +50ms]{y}病院{/}で復活させるか[>#or_badge -450ms][>#panel_s -220ms][♪pop -2dB -80ms][>#plate_s +50ms]{y}神社{/}で復活させるかは[br][<#or_badge -200ms][>#ok_stamp -180ms][♪item 0dB][!#panel_h to,{y:8, duration:0.06, ease:'none', repeat:3, yoyo:true} +250ms][!#panel_s to,{y:8, duration:0.06, ease:'none', repeat:3, yoyo:true} +250ms]{y}どちらでもいい{/}です。[silence:450ms]

*** prep
@n: [silence:380ms][♪step -3dB -80ms]{y}下準備{/}として、[>#prep_card.r1.hl -450ms][!#prep_card.r1.icon pop -150ms]{y}神父{/}に[♪change -2dB -50ms][>#prep_card.r1.ck +400ms]着替えます。[silence:590ms]
@: [silence:0ms][<#prep_card.r1.hl -240ms][>#props_bg -240ms][<#dress_bg +110ms][>#prep_card.r2.hl -140ms]そして{y}小道具{/}から[!#prep_card.r2.icon pop -150ms][>#prep_star[*] -200ms][!#prep_star[*] to,{opacity:0, scale:0.36, rotation:60, duration:0.45, ease:'power2.in', stagger:0.09} +250ms][♪get -2dB -50ms][>#get_sfx]{y}車椅子{/}を[>#prep_card.r2.ck +330ms]出しましょう。[silence:460ms]

*** attack
@n: [silence:340ms][♪step -3dB -120ms]復活させたら、[>#speedlines -20ms][<#speedlines +450ms][!#attack_bg shake {x: 17, duration: .28}][>#attack_sfx -200ms][!#flash to,{opacity:0.55, duration:0.04}][!#flash to,{opacity:0, duration:0.22, ease:'power1.out'} +40ms][♪punch +3dB][♪punch_echo -1dB +160ms]{y}攻撃{/}します。[silence:300ms]

*** lift
@n: [silence:380ms][♪step -3dB -160ms]敵が倒れたら[>#lift_a[*] -100ms][<#lift_a[*] +450ms][>#lift_b[*] +20ms][<#lift_b[*] +570ms][>#lift_c[*] +800ms][>#lift_d[*] +920ms][>#lift_sfx][♪lift 0dB -50ms][!#lift_bg to,{y:-18, duration:0.5, ease:'power2.out'}]{y}持ち上げ{/}ます。[silence:330ms]

*** counter
@n: [silence:360ms][♪step -3dB -140ms][!#warn_frame to,{opacity:1, duration:0.12, ease:'none', repeat:7, yoyo:true} -180ms][♪alarm -4dB -160ms][>#warn_sign -130ms][!#warn_sign to,{x:-10, duration:0.05, ease:'none', repeat:7, yoyo:true} +220ms]{y}反撃{/}してくるので[br][<#warn_sign -120ms][!#flash to,{opacity:0.7, duration:0.03} -30ms][!#flash to,{opacity:0, duration:0.25}][>#seat_bg][<#counter_bg][♪sweep -2dB -50ms][>#quick_sfx -150ms]{y}すぐに{/}{y}車椅子に{/}[<#quick_sfx -150ms][>#seat_sfx][♪seat 0dB][!#seat_bg to,{y:14, duration:0.08, ease:'power1.out', repeat:1, yoyo:true} +20ms]{y}座らせ{/}ます。[silence:440ms]
[<#subtitle]
transition cut

*** suspense
@n: [silence:410ms][!#sub_band to,{opacity:0, duration:0.25} -410ms][♪drum +2dB start=1.35s to=6s -340ms][<#music -210ms][>#hero_sus.word -160ms][>#hero_sus.dot[*] +890ms][!#hero_sus to,{scale:1.06, duration:0.6, ease:'sine.inOut', repeat:1, yoyo:true} +990ms]そうすると...[silence:1050ms]
transition cut

*** reveal
bgm music_b +1980ms
@n: [silence:380ms][!#flash to,{opacity:1, duration:0.03} -380ms][!#flash to,{opacity:0, duration:0.6, ease:'power2.out'} -350ms][♪sparkle -4dB -330ms][>#burst -300ms][!#burst to,{scale:1.04, duration:0.3, ease:'sine.inOut', repeat:5, yoyo:true} +220ms][>#hearts[*] -80ms][!#hearts[*] to,{y:-120, opacity:0, duration:1, ease:'power1.in', stagger:0.16} +720ms][>#hero_call -230ms][!#hero_call to,{scale:1.08, duration:0.16, ease:'power2.out', repeat:1, yoyo:true} +1350ms][!#hero_call to,{y:-10, duration:0.5, ease:'sine.inOut', repeat:1, yoyo:true} +1750ms][>#confetti +1300ms][<#confetti cut-0ms][♪fanfare +4dB +1350ms][♪cheer 0dB to=3.5s +1470ms]呼ぶことができます！！[silence:1640ms]

*** outro
[>#subtitle]
@n: [silence:570ms][!#sub_band to,{opacity:1, duration:0.3} -470ms][>#recap_label -120ms][>#rc[*] +30ms][>#ra[*] +100ms][>#recap_goal +870ms][!#recap_goal to,{scale:1.12, duration:0.25, ease:'sine.inOut', repeat:3, yoyo:true} +1280ms][♪sparkle -5dB +30ms][>#fade_out +3460ms]みなさんもぜひやってみてください[silence:2500ms]
```

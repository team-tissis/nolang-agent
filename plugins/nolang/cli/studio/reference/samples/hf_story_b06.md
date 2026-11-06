# story · usui-horse-rail (hf 全力版の全量の写し — 9月5日の歴史的珍事件「碓氷馬車鉄道」・17 場面を hard cut で畳みかける錦絵の豆知識コメディ) — canvas 1080x1920

見せる作り: 章の境目だけ朱の斜めの帯が払う切替 (panel)・左上に残る章の札 (sticky)・金の極太テロップ (墨の縁 + 朱の硬い影・青 / 白 / 朱の変種) と古活字の判子を語に叩きつける (画面ごと揺れる)・錦絵の全面画 (基準画像で馬車を揃える) と透過の切り抜き・和紙 / 青海波 / 放射の地・横から見た線路の景色の def (3 場面)・速度計と年表の板・文の途中の絵替え・3 人の声・語ごとの効果音 (拍子木・太鼓・蹄・汽笛) と BGM の差し替え

```design.txt
#v2
# 学ぶ作り: 17 場面を切替なしの hard cut で畳みかけ、章の境目 5 か所だけ朱の斜めの帯が払う (panel)・章の札は sticky で章のあいだ左上に残る
# 文字は 4 書体の class で組む: 金の極太テロップ (墨の縁 + 朱の硬い影・青 / 白 / 朱の変種)・アンチックの明朝 (新字体)の札と判子・丸ゴシックの字幕 (縁取り・句ごとの札)・筆の擬音
# 絵は錦絵の全面画 (基準画像で馬車と人物を揃える) と透過の切り抜き (馬・文豪・客車・歩く人)・和紙 / 青海波 / 放射の地は図形と svg で描く
# hf b06 usui-horse-rail (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#1B1511
theme dark
palette washi=#F3E7CF sumi=#1B1511 shu=#D23F2A ai=#1D3A63 kin=#FFD23F white=#FFFAF0 sky=#CFE6FF orange=#F39A2B purple=#5B2A86 paper=#F7EEDB
font "太く丸い丸ゴシック体、いちばん太いウェイト"
# engine: 字幕の丸ゴシックは hf (M+ 丸ゴシックの Black) よりわずかに細い — 書体の意味検索は family の既定の太さを返し、その family の既定は Regular なので説明文では Black に届かない (いま当たる丸ゴシックの Black が最も近い)
fonts d="超極太のディスプレイ用ゴシック体。最も太いウェイトで極めて太い画線と詰まった懐、ずっしりした幾何学的な字形の看板文字。パンチの効いたサムネイルや大見出し向き" z="新字体で組む、レトロで太いアンチックの明朝体、昭和の看板や見出しのような字面" b="荒々しい毛筆の楷書体、墨の勢いのある筆文字"
sfx off
# hf の作り: 見出しのテロップは台詞と同じ語を大きく先に見せる (spoiler・duplicate_text)・テロップで言う台詞には字幕を出さない (caption_gap)
# hf の作り: 判子と擬音は文末に叩きつけてすぐ次の場面へ切る (flash_text)・和紙の地の溜めと紀行文の場面は絵を置かない (text_only_cut)・語ごとに効果音を重ねる (se_dense)
# hf の作り: 金の放射の地に白の極太テロップ (墨の縁 + 朱の影で読ませる)
lint off=spoiler,duplicate_text,caption_gap,flash_text,text_only_cut,se_dense
art "明治時代の錦絵（多色刷りの浮世絵木版画）のスタイル。太く力強い墨の輪郭線、平坦で鮮やかな色面（藍・朱・黄土・若草色）、和紙の質感、ユーモラスで誇張された表情の戯画"
prompt_tail "画面内に文字・数字・ロゴ・署名・落款・題箋を一切描かない"
image hero = "急な山道に敷かれた細い線路の上を、馬が小さな木造の客車を必死に引っ張っている縦長の構図。客車には明治時代の洋装と和装の乗客がぎゅうぎゅう詰めで、窓から顔を出している。背景は険しい峠の山々と白い雲。馬は汗をかきながらも踏ん張っている。" aspect=9:16
image pass = "切り立った岩山の峠を間近に見上げる縦長 9:16 の構図。画面の上端から下端まで隙間なく色で描き込む: 画面の最上端は浮世絵の一文字ぼかし (濃い藍から群青へ移る帯) の空で塗り、そのすぐ下に白い雲海と青い連峰、岩山の頂は画面の上から 1 割の高さまでそびえる。画面の左上から松の大枝が張り出す。つづら折りの細い山道が画面の下から頂上まで続き、荷を背負った旅人が登る。右下の手前に藁葺きの小さな茶屋と休む客。空も色で塗り、和紙の無地の地や余白を画面のどこにも残さない。壮大でドラマチック。" aspect=9:16
image down = "[ref:@hero]急な下り坂の山道の線路を、馬車鉄道の小さな木造客車が猛スピードで暴走している縦長の構図。乗客たちは目を見開いて絶叫し、帽子や風呂敷包みが宙に舞う。後ろから馬が慌てて追いかけている。スピード線と土煙。ジェットコースターのような迫力とユーモア。" aspect=9:16
image cart = "[transparent]真横から見た、馬が小さな木造の客車（馬車鉄道の車両、車輪付き、レールの上を走る）を引っ張っている全身の図。客車の窓から明治時代の乗客が顔を出している。馬は画面の右側で右を向いて元気に歩き、客車はその左に続いて右へ進む。" aspect=3:2
image horse = "[transparent]得意げなドヤ顔でこちらを見る馬の顔のアップ。鼻息が荒く、片目をつぶってウインクしている。コミカルで力強い。"
image ogai = "[transparent]口ひげをたくわえた明治時代の洋装の若い紳士（文豪）の上半身。鼻をつまみ、顔を真っ赤にして目をむいて激怒している。頭から怒りの湯気。コミカルな戯画。"
sound hyoshigi = "拍子木をカンカンと打つ乾いた音"
sound swish = "カメラが流れるようなシュッという風切り音"
sound taiko = "和太鼓をドンと一発鳴らす音"
sound pon = "ポンと軽く鳴る明るいアクセントの音"
sound pon_hi = "ポンと鳴るアクセントの音、少し高め"
sound hooves = "馬の蹄がパカパカと鳴る足音"
sound whistle = "汽車のポーッという汽笛の音"
sound impact = "ドーンと響く衝撃のオノマトペの音"
sound jan = "ジャン！という驚きの効果音"
run k { color: $kin; font-family: d; font-size: 66px }
run wa { color: $sumi; font-family: z; font-size: 110px }
run r { color: $shu }
p { out: none }
div { border: none; out: none }
img { out: none }
svg { out: none }
shape { out: none }
group { out: none }
cut { stagger: 0ms }
bgm#music(fade: 50,350) 見世物小屋の呼び込みのような賑やかでコミカルな和風の曲、三味線と太鼓と笛のお祭り調でテンポが良い
bgm#rush(fade: 80,700) 慌てふためくコミカルな和風の大騒ぎの曲、速い太鼓と三味線が畳みかける
bgm#music_b(fade: 900,1600) 見世物小屋の呼び込みのような賑やかでコミカルな和風の曲、三味線と太鼓と笛のお祭り調でテンポが良い
# 字幕: 丸ゴシック 66px の白 + 墨の縁・下 193 px・句ごとの札 ([|])・読点は空白・下から軽く出る
subtitle(left: 30px; bottom: 290px; width: 1020px; font-size: 66px; line-height: 1.32; letter-spacing: 0.02em; text-align: center; color: $white; -webkit-text-stroke: 7px $sumi; background: none; unit: sentence; strip: 、。>space; lead: 0ms; tail: 0ms; hold: off; in: {y:26, opacity:0, duration:0.14, ease:'power2.out'}; out: none)
# 金の極太テロップ (墨の縁 + 朱の硬い影)。青 / 白 / 朱は色と影の引数で
def telop(t, s, c=$kin, sc=$sumi, sh=#A01E0FF2) = p(left: 24px; width: 1032px; font-family: d; font-size: {s}; line-height: 1.2; text-align: center; color: {c}; -webkit-text-stroke: 10px {sc}; text-shadow: 10px 10px 0px {sh}; content: {t})
# 縁取りの文字 (書体と大きさだけ変える)
def ol(t, s, f=d) = p(font-family: {f}; font-size: {s}; line-height: 1.25; text-align: center; -webkit-text-stroke: 5px $sumi; content: {t})
# 判子 (朱の太枠 + 生成りの地 + アンチックの明朝の朱文字)・叩きつけて傾いたまま残る
def stamp(t, s, w) = p(width: {w}; font-family: z; font-size: {s}; line-height: 1; text-align: center; color: $shu; background: #FFFAF0E0; border: 16px solid $shu; box-shadow: 10px 10px 0px #00000059; padding: 14px 0px 22px 0px; content: {t})
# 上下の減光 (上 62% → 透明 → 下 72%)
def shade() = div(inset: 0; background: linear(#0C08059E,#0C080500@22%,#0C080500@60%,#0C080573@82%,#0C0805B8,180); in: none)
# 和紙の地 (生成り + 左上の光 + 細い繊維の筋 + 周辺の焼け)
def washi(c=$washi) = div(inset: 0; background: {c}; pattern: hatch,-7,#785A280D,6,1; in: none)
  div#hi(inset: 0; background: radial(#FFFFFF59,#FFFFFF00@55%,30%,20%))
  div#vig(inset: 0; background: radial(#28140500@45%,#2814058C,50%,45%))
# 章の札 (朱の地に白の細枠の番号 + 縁取りの極太の題)・sticky で章のあいだ残る
def chapter(no, t) = div(left: 48px; top: 150px; width: 690px; height: 102px; z-index: front; in: none)
  div#no(left: 0px; cy: 50%; width: 206px; height: 96px; background: $shu; box-shadow: 8px 8px 0px #00000073; in: {x:-260, opacity:0, duration:0.3, ease:'back.out(1.8)'})
    div#line(left: 4px; top: 4px; width: 196px; height: 87px; border: 4px solid $white)
    p#t(cx: 50%; cy: 50%; font-family: z; font-size: 46px; content: {no})
  p#t(left: 228px; cy: 50%; width: 450px; font-family: d; font-size: 70px; letter-spacing: 0.02em; -webkit-text-stroke: 5px $sumi; delay: 80ms; in: {x:-120, opacity:0, duration:0.3, ease:'power3.out'}; content: {t})
# 横から見た線路の景色 (峠の絵の上半分 + 地面 + レール + 枕木)・3 場面で使う
def land() = div(inset: 0; background: $washi; in: none)
  # 峠の絵は上端の藍の空から雲海・連峰・頂・つづら折りの山道・右下の茶屋まで縦いっぱいに描き込まれている — 地面の上には絵の下半分 (雲海の下の峰と山道・茶屋の屋根) を敷く
  img#bg.bleed(left: -160px; top: -1320px; width: 1500px; height: 2656px; content: @pass; main: none; in: none)
  div#fade(left: 0px; top: 0px; width: 1080px; height: 1300px; background: linear(#F3E7CF00@40%,#F3E7CF73,180))
  div#top(left: 0px; top: 0px; width: 1080px; height: 420px; background: linear(#0C08059E,#0C080500,180))
  div#ground(left: 0px; top: 1290px; width: 1080px; height: 630px; background: linear(#C9A062,#B88A4C@40%,#7D5730,180); pattern: hatch,-28,#5A3C1E1A,15,2)
  div#edge(left: 0px; top: 1290px; width: 1080px; height: 6px; background: #6B4A2A)
  div#rail.bleed(left: -200px; top: 1272px; width: 1500px; height: 18px; background: linear(#8A8F99,#2A2B30,180))
  div#sleepers.bleed(left: -400px; top: 1288px; width: 2000px; height: 24px; pattern: hatch,0,#5A3B22,57,23)

svg gauge = """<svg viewBox="0 0 457 270"><path d="M46 227A187 187 0 0 1 49 193L135 209A100 100 0 0 0 133 227Z" fill="#549d49"/><path d="M49 195A187 187 0 0 1 58 162L139 192A100 100 0 0 0 135 210Z" fill="#68a348"/><path d="M57 163A187 187 0 0 1 72 132L147 176A100 100 0 0 0 139 193Z" fill="#7caa47"/><path d="M71 134A187 187 0 0 1 91 106L157 162A100 100 0 0 0 146 177Z" fill="#90b046"/><path d="M90 107A187 187 0 0 1 114 83L169 150A100 100 0 0 0 156 163Z" fill="#a4b644"/><path d="M113 84A187 187 0 0 1 141 64L184 140A100 100 0 0 0 169 150Z" fill="#b9bc43"/><path d="M140 65A187 187 0 0 1 170 51L199 133A100 100 0 0 0 183 140Z" fill="#cdc242"/><path d="M169 51A187 187 0 0 1 202 43L216 128A100 100 0 0 0 199 133Z" fill="#e1c941"/><path d="M201 43A187 187 0 0 1 234 40L234 127A100 100 0 0 0 216 129Z" fill="#f5cf40"/><path d="M233 40A187 187 0 0 1 267 43L251 129A100 100 0 0 0 233 127Z" fill="#fcca3e"/><path d="M265 43A187 187 0 0 1 298 52L268 133A100 100 0 0 0 250 129Z" fill="#f8ba3c"/><path d="M297 51A187 187 0 0 1 328 66L284 141A100 100 0 0 0 267 133Z" fill="#f2a939"/><path d="M326 65A187 187 0 0 1 354 85L298 151A100 100 0 0 0 283 140Z" fill="#ee9937"/><path d="M353 84A187 187 0 0 1 377 108L310 163A100 100 0 0 0 297 150Z" fill="#e88834"/><path d="M376 107A187 187 0 0 1 396 135L320 178A100 100 0 0 0 310 163Z" fill="#e47832"/><path d="M395 134A187 187 0 0 1 409 164L327 193A100 100 0 0 0 320 177Z" fill="#de6830"/><path d="M409 163A187 187 0 0 1 417 196L332 210A100 100 0 0 0 327 193Z" fill="#da582e"/><path d="M417 195A187 187 0 0 1 420 227L333 227A100 100 0 0 0 331 210Z" fill="#d4472b"/><line x1="233" y1="227" x2="79" y2="88" stroke="#1b1511" stroke-width="5" stroke-dasharray="11 8"/></svg>"""
svg seigaiha = """<svg viewBox="0 0 720 1280"><defs><pattern id="w" width="80" height="40" patternUnits="userSpaceOnUse"><rect width="80" height="40" fill="#1d3a63"/><circle cx="0" cy="20" r="40" fill="#27497a"/><circle cx="0" cy="20" r="36" fill="#1d3a63"/><circle cx="0" cy="20" r="28" fill="#27497a"/><circle cx="0" cy="20" r="24" fill="#1d3a63"/><circle cx="0" cy="20" r="17" fill="#27497a"/><circle cx="0" cy="20" r="12" fill="#1d3a63"/><circle cx="0" cy="20" r="4" fill="#27497a"/><circle cx="80" cy="20" r="40" fill="#27497a"/><circle cx="80" cy="20" r="36" fill="#1d3a63"/><circle cx="80" cy="20" r="28" fill="#27497a"/><circle cx="80" cy="20" r="24" fill="#1d3a63"/><circle cx="80" cy="20" r="17" fill="#27497a"/><circle cx="80" cy="20" r="12" fill="#1d3a63"/><circle cx="80" cy="20" r="4" fill="#27497a"/><circle cx="40" cy="40" r="40" fill="#27497a"/><circle cx="40" cy="40" r="36" fill="#1d3a63"/><circle cx="40" cy="40" r="28" fill="#27497a"/><circle cx="40" cy="40" r="24" fill="#1d3a63"/><circle cx="40" cy="40" r="17" fill="#27497a"/><circle cx="40" cy="40" r="13" fill="#1d3a63"/><circle cx="40" cy="40" r="6" fill="#27497a"/><circle cx="0" cy="60" r="40" fill="#27497a"/><circle cx="0" cy="60" r="36" fill="#1d3a63"/><circle cx="0" cy="60" r="28" fill="#27497a"/><circle cx="0" cy="60" r="24" fill="#1d3a63"/><circle cx="80" cy="60" r="40" fill="#27497a"/><circle cx="80" cy="60" r="36" fill="#1d3a63"/><circle cx="80" cy="60" r="28" fill="#27497a"/><circle cx="80" cy="60" r="24" fill="#1d3a63"/></pattern></defs><rect width="720" height="1280" fill="url(#w)"/></svg>"""
svg fly = """<svg viewBox="0 0 56 44"><ellipse cx="41" cy="14" rx="8" ry="12" transform="rotate(-30 41 14)" fill="#e1ebfabf"/><ellipse cx="19" cy="15" rx="11" ry="15" transform="rotate(-30 19 15)" fill="#e1ebfabf" stroke="#222" stroke-width="3"/><ellipse cx="28" cy="29" rx="16" ry="13" fill="#111"/></svg>"""
svg gloom = """<svg viewBox="0 0 427 400"><defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="400"><stop offset=".55" stop-color="#283c8c" stop-opacity=".55"/><stop offset="1" stop-color="#283c8c" stop-opacity="0"/></linearGradient><pattern id="p" width="17" height="400" patternUnits="userSpaceOnUse"><rect width="4" height="400" fill="url(#g)"/></pattern></defs><rect width="427" height="400" fill="url(#p)"/></svg>"""

# 冒頭: 馬が客車を引く絵に寄りから引き、上に「9月5日の歴史的珍事件」の帯・下に 2 行の大テロップが傾いて弾む
section#hook
img#hook_bg(inset: 0; content: @hero; main: kb {scale: [1.22, 1.06], focus: ['33% 36%', '50% 50%']})
shade#hook_shade
# hf の作り: 帯の書体はアンチックの明朝 (新字体)・「9月5日」だけ run k で極太ゴシックの金
p#hook_band(cx: 540px; top: 150px; font-family: z; font-size: 60px; letter-spacing: 0.07em; background: $shu; padding: 12px 40px 16px 40px; box-shadow: 0px 10px 0px #00000059; in: {y:-60, opacity:0, duration:0.3, ease:'power3.out'}) {k}9月5日{/}の歴史的珍事件
  div#rule_top(left: 0px; top: 0px; width: 100%; height: 4px; background: $kin)
  div#rule_bottom(left: 0px; bottom: 0px; width: 100%; height: 4px; background: $kin)
telop#ht1(top: 1180px; s: 150; transform-origin: 50% 80%; in: {scale:0.2, rotation:-6, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 馬が電車を
telop#ht2(top: 1362px; s: 176; c: $white; transform-origin: 50% 80%; in: {scale:0.2, rotation:5, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 引っ張る!?

# 其の一 開業: 峠の絵を下から上へ流し、年月日の札を叩きつけ (絵が揺れる)・「碓氷峠」の立て札のピンが弾む
section#pass
# hf は峠を上から下へ流す — 絵は上端の空から下端の茶屋まで描き込まれているので、不動点を下端の右寄りに置き、雲海の下の峰・つづら折りの山道・茶屋を大きく見せて引く
img#pass_bg(inset: 0; content: @pass; main: kb {scale: [1.95, 1.8], focus: ['60% 100%', '60% 100%']})
shade#pass_shade
# 章の札 (sticky・この章の最後の cut の末尾で閉じる)
chapter#ch1.sticky(no: "其の一"; t: "開業")
group#date_plate(left: 60px; top: 300px; width: 780px; height: 225px; transform: rotate(-3deg); in: {scale:1.9, rotation:-6, opacity:0, duration:0.2, ease:'power4.in'})
  ol#era(left: 0px; top: 0px; s: 53; f: z; text-align: left) 明治21年
  p#ymd(left: 0px; top: 75px; width: 750px; white-space: nowrap; font-family: d; font-size: 132px; line-height: 1.15; color: $kin; -webkit-text-stroke: 7px $sumi; text-shadow: 8px 8px 0px #A01E0FF2) 1888.9.5
div#pin(left: 470px; top: 760px; width: 339px; height: 334px; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'})
  div#tag(left: 0px; top: 0px; width: 339px; height: 186px; background: $washi; border: 6px solid $sumi; box-shadow: 10px 10px 0px #00000073)
    p#big(cx: 50%; top: 14px; font-family: z; font-size: 92px; line-height: 1; color: $sumi) 碓氷峠
    p#sm(cx: 50%; top: 116px; font-family: z; font-size: 40px; color: $shu) 群馬 ⇔ 長野
  div#stem(cx: 50%; top: 186px; width: 8px; height: 120px; background: $sumi)
  div#dot(cx: 50%; top: 300px; width: 34px; height: 34px; border-radius: 148px; background: $shu; border: 6px solid $white)

# 急勾配の前で止まる汽車の絵が傾きながら寄り、青のテロップ「急すぎて 登れない…」が弾んで出て文末でうなだれる
section#loco
img#loco_bg(inset: 0; main: keys(at=0 scale=1.08 rotation=-1.5 | at=1 scale=1.16 rotation=1.5 ease=none)) 壁のように急な坂のふもとで、明治時代の小さな蒸気機関車が坂を見上げて立ち往生している縦長の構図。画面の上端まで濃い青空と白いもくもくの雲が埋め、和紙の無地の余白を作らない。線路は画面の右下から右上の端へ壁のような岩山を一直線に登る。機関車は画面の下半分の左寄り、煙突から弱々しい煙、機関士が頭を抱えて途方に暮れている。コミカルな構図。
shade#loco_shade
telop#loco_t(top: 560px; s: 132; c: $sky; sh: #14285AF2; in: {scale:0.5, opacity:0, duration:0.42, ease:'back.out(1.6)'}) 急すぎて[br]登れない…

# 溜め: 和紙の地に朱の「？」が揺れ、「ポク」「ポク」と筆の「チーン」が順に弾む
section#think
washi#think_washi
ol#qmark(left: 0px; width: 1080px; top: 520px; s: 521; line-height: 1; color: $shu; -webkit-text-stroke: 9px $sumi; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'}) ？
ol#poku(left: "99;780"; top: "431;560"; width: 210px; s: 96; color: $sumi; -webkit-text-stroke: 5px $washi; in: {scale:0.5, opacity:0, duration:0.25, ease:'back.out(2.4)'}) ×2 ポク;ポク
ol#chiin(left: 0px; width: 1080px; top: 1130px; s: 191; f: b; color: $shu; -webkit-text-stroke: 7px $white; text-shadow: 6px 6px 0px #00000059; in: {scale:0.6, opacity:0, duration:0.3, ease:'back.out(2.4)'}) チーン

# 答え: 回る金と橙の放射の地に、ウインクする馬の顔が回りながら弾み、白のテロップ「馬に引かせる！」
section#answer
div#rays_bg(inset: 0; background: $orange; in: none)
shape#rays.bleed(left: -960px; top: -660px; width: 3000px; height: 3000px; path: sunburst,n=20; background: $kin; main: spin {period: 13.32}; in: none)
img#horse_pop(left: 90px; top: 360px; width: 900px; height: 900px; content: @horse; in: {scale:0.15, rotation:-12, opacity:0, duration:0.5, ease:'back.out(2.4)'})
telop#answer_t(left: 6px; width: 1068px; top: 1240px; s: 150; c: $white; in: {scale:0.3, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 馬に引かせる！

# 名前: 同じ絵に寄った構図で「その名も」の黒札が上がり、二重枠の名札「碓氷馬車鉄道」(ふりがな・開業年) を叩きつける
section#name
img#name_bg(inset: 0; content: @hero; main: kb {scale: [1.3, 1.16], focus: ['13% 22%', '15% 17%']})
shade#name_shade
p#sonna(cx: 540px; top: 600px; font-family: z; font-size: 64px; background: $sumi; padding: 6px 30px 10px 30px; in: {y:40, opacity:0, duration:0.25, ease:'power3.out'}) その名も
div#cartouche(left: 50px; top: 720px; width: 981px; height: 354px; background: $washi; border: 6px solid $sumi; box-shadow: 16px 16px 0px #00000080; in: {scale:1.8, opacity:0, duration:0.2, ease:'power4.in'})
  div#d1(left: 4px; top: 4px; width: 960px; height: 333px; border: 3px solid $shu)
  div#d2(left: 14px; top: 14px; width: 942px; height: 315px; border: 3px solid $shu)
  p#rt(left: 86px; top: 21px; width: 195px; font-family: z; font-size: 46px; letter-spacing: 0.17em; text-align: center; color: $shu) うすい
  p#nm(left: 0px; top: 90px; width: 100%; text-align: center; font-family: z; font-size: 150px; line-height: 1.15; letter-spacing: 0.04em; color: $sumi) 碓氷馬車鉄道
  p#yr(left: 0px; top: 273px; width: 100%; text-align: center; font-size: 44px; color: $shu) 1888年（明治21年）開業

# 横から: 峠の景色が流れ、客車を引く馬が左から入って揺れ続ける・「動力」の札が右から入り、文末の語で朱の「馬力」が弾む
section#side1
land#land1
  img#bg(left: -196px; in: {x:36, duration:5.05, ease:'none'})
  div#sleepers(left: -744px; in: {x:344, duration:5.05, ease:'none'})
img#cart1(left: 50px; top: 788px; width: 980px; height: 652px; content: @cart; in: {x:-1000, duration:2.0, ease:'power2.out'}; main: sine {y: -8, period: 0.26})
div#spec(left: 70px; top: 330px; width: 939px; height: 204px; background: $washi; border: 8px solid $sumi; box-shadow: 14px 14px 0px #00000066; padding: 18px 34px 26px 34px; display: flex; align-items: center; gap: 30px; in: {x:900, opacity:0, duration:0.35, ease:'back.out(1.4)'})
  p#k(font-family: z; font-size: 64px; background: $sumi; padding: 4px 18px 10px 18px) 動力
  p#v(width: 339px; font-family: d; font-size: 150px; line-height: 1.2; color: $shu; in: {scale:0.4, opacity:0, duration:0.35, ease:'back.out(1.7)'}) 馬力
  p#note(font-size: 40px; line-height: 1.2; color: $sumi) ※文字どおり[br]（馬が引く）

# 其の二 文豪、激怒: 青海波の地に光の輪・怒る文豪の切り抜きが下から弾み、縦書きの朱の名札「文豪 森鴎外」を叩きつける
section#ogai1
svg#wave(inset: 0; part: seigaiha; in: none)
div#spot(left: 40px; top: 300px; width: 1000px; height: 1000px; border-radius: 1498px; background: radial(#FFE6AA8C,#FFE6AA00@68%,50%,50%); in: none)
chapter#ch2.sticky(no: "其の二"; t: "文豪、激怒")
img#ogai_pop(left: 30px; top: 285px; width: 1020px; height: 1020px; content: @ogai; in: {y:300, scale:0.5, opacity:0, duration:0.45, ease:'back.out(1.6)'})
div#nameplate(left: 795px; top: 324px; width: 230px; height: 592px; background: $shu; box-shadow: 12px 12px 0px #00000073; in: {scale:1.7, opacity:0, duration:0.2, ease:'power4.in'})
  div#line(left: 4px; top: 4px; width: 220px; height: 584px; border: 6px solid $white)
  p#t(cx: 50%; top: 36px; font-family: z; font-size: 48px; letter-spacing: 0.13em; vertical: true) 文豪
  p#n(cx: 50%; top: 156px; font-family: z; font-size: 128px; letter-spacing: 0.08em; vertical: true) 森鴎外

# 紀行文: 暗い和紙の地に縦罫の原稿が上から開き、墨の行の上に朱の判子「要約」を傾けて押す
section#scroll
washi#scroll_washi(c: #C7BDAA)
div#paper(left: 150px; top: 330px; width: 780px; height: 1040px; background: $paper; border: 3px solid #B9A37A; box-shadow: 18px 18px 0px #00000059; pattern: hatch,0,#C83C288C,64,2; in: {scaleY:0.02, opacity:0, duration:0.45, ease:'power3.out', pivot:'top'})
  p#ttl(right: 30px; top: 40px; font-family: z; font-size: 72px; letter-spacing: 0.14em; color: $sumi; vertical: true) 紀行文
  div#col(left: "575;479;383;287;191;95"; top: 70px; width: 18px; height: "641;821;521;761;881;431"; border-radius: 9px; background: #1B1511C7) ×6
p#youyaku(left: 230px; top: 820px; width: 330px; height: 330px; font-family: z; font-size: 128px; line-height: 1; text-align: center; color: $shu; background: #F7EEDB40; border: 14px solid $shu; border-radius: 30px; transform: rotate(-10deg); in: {scale:2.2, rotation:-20, opacity:0, duration:0.2, ease:'power4.in'}) 要約

# 激怒: 揺れる車内で鼻をつまむ文豪の絵に寄り続け、ハエが飛び回る・「臭いと揺れが」→ 筆の朱「最悪！」で画面ごと揺れ → 判子「文豪、大激怒」
section#rage
img#rage_bg(inset: 0; main: kb {scale: [1.06, 1.2]}) [ref:@ogai]狭くて激しく揺れる馬車鉄道の木造客車の車内、縦長の構図。口ひげをたくわえた明治時代の洋装の若い紳士（文豪）が、片手で鼻をつまみ、もう片方の手で帽子を押さえながら、顔を真っ赤にして激怒している。周りの乗客と肩がぶつかり合い、皆よろけている。窓の外には客車を引く馬の後ろ姿。頭から湯気が出ている。
shade#rage_shade
svg#fly(left: "701;330;780"; top: "521;470;761"; width: 56px; height: 44px; part: fly; in: none; main: noise {x: 80, y: 60, rotation: 27, period: 0.44}) ×3
ol#brush1(left: 0px; width: 1080px; top: 880px; s: 104; -webkit-text-stroke: 7px $sumi; in: {scale:0.6, opacity:0, duration:0.42, ease:'back.out(2.4)'}; out: {opacity:0, duration:0.15, ease:'none'}) 臭いと揺れが
ol#brush2(left: 24px; width: 1032px; top: 1020px; s: 300; f: b; line-height: 1.25; color: $shu; -webkit-text-stroke: 7px $white; text-shadow: 12px 12px 0px #000000CC; transform: rotate(-4deg); in: {scale:2.4, rotation:-8, opacity:0, duration:0.2, ease:'power4.in'}; out: {opacity:0, duration:0.15, ease:'none'}) 最悪！
div#gekido(left: 250px; top: 880px; width: 580px; height: 320px; background: #FFFAF0E0; border: 16px solid $shu; box-shadow: 10px 10px 0px #00000059; transform: rotate(-9deg); in: {scale:2.6, rotation:-18, opacity:0, duration:0.2, ease:'power4.in'})
  p#sm(cx: 50%; top: 18px; font-family: z; font-size: 64px; line-height: 1; color: $sumi) 文豪、
  p#big(cx: 50%; top: 88px; font-family: z; font-size: 170px; line-height: 1; color: $shu) 大激怒

# 其の三 遅すぎ: 横の景色で客車がのろのろ進み、速度計の針が「徒歩の速さ」の手前で震える・青の「遅っ!!」が伸び縮み
# → 文の途中の語で「途中下車」の絵へ替え、金の「途中下車 続出!!」→ 乗客の吹き出し「歩いた方が早いわ！」で画面ごと揺れる
section#slow
land#land2
img#cart2(left: 20px; top: 788px; width: 980px; height: 652px; content: @cart; in: {x:-50, duration:1.69, ease:'none'}; main: sine {y: -3, period: 0.6})
chapter#ch3.sticky(no: "其の三"; t: "遅すぎ")
div#gauge(left: 190px; top: 330px; width: 700px; height: 420px; background: $washi; border: 8px solid $sumi; box-shadow: 14px 14px 0px #00000066; in: {y:-60, opacity:0, duration:0.3, ease:'power3.out'})
  svg#face(left: 0px; top: 0px; width: 686px; height: 405px; part: gauge)
  p#lab(left: 14px; top: 38px; width: 258px; text-align: center; font-family: d; font-size: 44px; background: $sumi; padding: 2px 14px 6px 14px; white-space: nowrap) 徒歩の速さ
  div#needle(left: 345px; top: 90px; width: 10px; height: 250px; border-radius: 6px; background: $sumi; transform: rotate(-20deg); transform-origin: 50% 100%)
  div#hub(left: 326px; top: 318px; width: 48px; height: 48px; border-radius: 148px; background: $shu; border: 6px solid $sumi)
  p#label(cx: 50%; top: 350px; font-family: z; font-size: 44px; color: $sumi) 馬車鉄道の速さ
  p#slow_end(left: 40px; top: 352px; width: 81px; font-family: d; font-size: 34px; color: $sumi) 遅い
  p#fast_end(right: 40px; top: 352px; width: 81px; font-family: d; font-size: 34px; color: $sumi) 速い
telop#slow_t(top: 1240px; s: 180; c: $sky; sh: #14285AF2; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 遅っ!!
img#walk_bg(inset: 0; in: none; main: kb {scale: [1.16, 1.1], focus: ['9% 50%', '96% 50%']}) [ref:@hero]山道の線路の上を、馬に引かれた小さな客車がのろのろと進んでいる。その横を、客車から降りた明治時代の乗客たち（着物の男性、洋装の紳士、荷物を背負った行商人）が呆れ顔ですたすた歩いて追い抜いていく縦長の構図。馬はへとへとで舌を出している。コミカル。
shade#walk_shade
telop#zoku_t(top: 440px; s: 150; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'}; out: {opacity:0, duration:0.12, ease:'none'}) 途中下車[br]続出!!
p#bubble(left: 70px; top: 330px; width: 940px; font-family: d; font-size: 116px; line-height: 1.15; text-align: center; color: $sumi; background: $white; border: 10px solid $sumi; border-radius: 70px; box-shadow: 14px 14px 0px #00000066; padding: 34px 20px 44px 20px; pointer: below,25%; in: {scale:0.3, opacity:0, duration:0.38, ease:'back.out(2.4)'}) 歩いた方が[br]{r}早いわ！{/}

# 追い抜かれる: 同じ横の景色で、歩く乗客が左から右へ跳ねながら客車を追い抜く・「スタスタ」が並んで流れ、文末に筆の「トボトボ…」と青い陰の筋
section#overtake
land#land3
img#cart3.bleed(left: 330px; top: 788px; width: 980px; height: 652px; content: @cart; in: none; main: sine {y: -2, period: 0.7})
svg#gloom(left: 360px; top: 700px; width: 640px; height: 600px; part: gloom; in: {y:-60, opacity:0, duration:0.5, ease:'power2.out'})
img#walker.bleed(left: 1120px; top: 724px; width: 380px; height: 570px; aspect: 2:3; in: {x:-1540, duration:2.3, ease:'none'}; main: sine {y: -9, rotation: 2, period: 0.28}) [transparent]真横から見た、右を向いてすたすた大股で歩く明治時代の着物姿の男性の全身。呆れたしかめ面で、風呂敷包みを肩にかついでいる。
ol#ono1(left: 430px; top: 600px; width: 354px; s: 80; overlap: land3.bg; in: {scale:0.4, opacity:0, duration:0.3, ease:'back.out(2.4)'}) スタスタ
ol#ono2(left: 420px; top: 1330px; s: 104; f: b; -webkit-text-stroke: 6px $sumi; in: {scale:0.6, opacity:0, duration:0.3, ease:'back.out(2.4)'}) トボトボ…

# 其の四 暴走: 暴走する客車の絵を暗く沈め、紫の「ゴ」が 4 つ震え・「本当の地獄は」→ 朱の「下り坂」を叩きつけ画面ごと揺れる
section#omen
img#omen_bg(inset: 0; content: @down; filter: saturate(0.6) brightness(0.55); main: kb {scale: [1.06, 1.18]})
shade#omen_shade
div#dark(inset: 0; background: radial(#3C000059,#140000D9,50%,50%); in: none)
chapter#ch4.sticky(no: "其の四"; t: "暴走")
ol#omen1(left: 0px; width: 1080px; top: 560px; s: 96; f: z; in: {scale:0.8, opacity:0, duration:0.35, ease:'power2.out'}) 本当の地獄は
telop#omen2(top: 720px; s: 230; c: $shu; sc: $white; sh: #000000D9; transform: rotate(-3deg); in: {scale:2.4, rotation:-6, opacity:0, duration:0.2, ease:'power4.in'}) 下り坂
# hf の作り: 紫の「ゴ」は 2 つずつ斜めに重ねて積む (overlap)
ol#go(left: "60;180;821;918"; top: "1061;1151;1080;1203"; width: 144px; s: 120; color: $purple; -webkit-text-stroke: 5px $white; in: {scale:0.5, opacity:0, duration:0.3, ease:'back.out(2.4)', stagger: {each: 0.25}}) ×4 ゴ;ゴ;ゴ;ゴ

# 暴走: 同じ絵を明るく戻して寄り続け、全編揺れる・白の集中線・金の「ブレーキ 効かず!!」→ 1 字ずつ弾む悲鳴 → 「明治の ジェットコースター」と判子「命がけ」
section#rush
img#rush_bg(inset: 0; content: @down; main: kb {scale: [1.08, 1.34]})
shade#rush_shade
shape#speed.bleed(left: -960px; top: -560px; width: 3000px; height: 3000px; path: rays,n=30,inner=0.28; background: none; border: 4px solid #FFFFFFBF; in: {opacity:0, duration:0.2, ease:'none'}; main: noise {rotation: 2.2, period: 0.12})
telop#rush1(top: 330px; s: 137; transform: rotate(-4deg); in: {scale:2.0, rotation:-8, opacity:0, duration:0.2, ease:'power4.in'}; out: {scale:0.8, opacity:0, duration:0.18, ease:'power2.in'}) ブレーキ[br]効かず!!
ol#scream(left: 0px; width: 1080px; top: 760px; s: 150; -webkit-text-stroke: 7px $sumi; in: {scale:0.3, opacity:0, duration:0.25, ease:'back.out(2.4)', stagger: 0.06}; out: {opacity:0, duration:0.15, ease:'none'}) ぎゃああ!!
ol#jc1(left: 0px; width: 1080px; top: 340px; s: 84; f: z; in: {scale:0.6, opacity:0, duration:0.3, ease:'back.out(2.4)'}) 明治の
telop#jc2(top: 450px; s: 101; line-height: 1.32; letter-spacing: -0.02em; in: {scale:0.3, opacity:0, duration:0.4, ease:'back.out(2.4)'}) ジェットコースター
stamp#inochi(left: 250px; top: 820px; w: 581; s: 150; white-space: nowrap; transform: rotate(-10deg); in: {scale:2.4, rotation:-20, opacity:0, duration:0.2, ease:'power4.in'}) 命がけ

# 其の五 引退: 赤レンガの橋を渡る汽車と見送る馬の絵を上から下へ・年表の板 (棒が伸びて 1893 に点)・判子「引退」→ 暖かい光と「馬たち、本当に おつかれさまでした」
section#bridge
img#bridge_bg(inset: 0; main: kb {scale: [1.22, 1.08], focus: ['50% 78%', '50% 0%']}) 深い緑の山あいに架かる赤レンガ造りの大きなアーチ橋を、明治時代の蒸気機関車が白い煙を上げて渡っていく縦長の構図。手前の野原では、引退した馬たちがのんびり草を食べながら機関車を見送っている。晴れやかで穏やかな雰囲気。
shade#bridge_shade
chapter#ch5.sticky(no: "其の五"; t: "引退")
div#warm(inset: 0; background: radial(#FFD67873,#FFD67800@70%,50%,70%); in: {opacity:0, duration:1.2, ease:'sine.inOut'})
div#tline(left: 70px; top: 330px; width: 939px; height: 330px; background: #F3E7CFF0; border: 8px solid $sumi; box-shadow: 14px 14px 0px #00000066; in: {y:-60, opacity:0, duration:0.35, ease:'power3.out'}; out: {y:-40, opacity:0, duration:0.3, ease:'power2.in'})
  p#mid(left: 0px; top: 104px; width: 100%; text-align: center; font-family: d; font-size: 54px; color: $shu; in: {scale:0.5, opacity:0, duration:0.3, ease:'back.out(2.4)'}) わずか5年足らず
  div#bar(left: 200px; top: 186px; width: 524px; height: 14px; background: $sumi; in: {scaleX:0, duration:1.3, ease:'power2.inOut', pivot:'left'})
  div#n1(left: 172px; top: 166px; width: 54px; height: 54px; border-radius: 148px; background: $shu; border: 8px solid $sumi)
  div#n2(left: 698px; top: 166px; width: 54px; height: 54px; border-radius: 148px; background: $shu; border: 8px solid $sumi; in: {scale:0, duration:0.3, ease:'back.out(2.4)'})
  p#y1(left: 50px; top: 226px; width: 300px; font-family: d; font-size: 58px; text-align: center; color: $sumi) 1888
  p#y2(left: 574px; top: 226px; width: 300px; font-family: d; font-size: 58px; text-align: center; color: $sumi) 1893
  p#ev1(left: 50px; top: 34px; width: 300px; font-family: z; font-size: 46px; text-align: center; color: $sumi; white-space: nowrap) 馬車鉄道 開業
  p#ev2(left: 574px; top: 34px; width: 300px; font-family: z; font-size: 46px; text-align: center; color: $shu; white-space: nowrap; in: {opacity:0, duration:0.2, ease:'none'}) 鉄道 開通
stamp#intai(left: 600px; top: 1010px; w: 380; s: 140; padding: 10px 0px 18px 0px; transform: rotate(8deg); in: {scale:2.4, rotation:16, opacity:0, duration:0.2, ease:'power4.in'}; out: {opacity:0, duration:0.25, ease:'none'}) 引退
ol#otsukare(left: 0px; width: 1080px; top: 1180px; s: 104; f: z; in: {scale:0.85, opacity:0, duration:0.6, ease:'power2.out'}) 馬たち、[br]本当に[br]おつかれさまでした

# 締め: 和紙の地に朱の「9月5日は」を叩きつけ、黒の名札「碓氷馬車鉄道」・「開業の日」・下から馬の顔が起き上がる
section#end
washi#end_washi
p#end_date(cx: 540px; top: 470px; font-family: d; font-size: 230px; line-height: 1.22; color: $shu; -webkit-text-stroke: 7px $sumi; transform: rotate(-2deg); in: {scale:1.8, rotation:-4, opacity:0, duration:0.2, ease:'power4.in'}) 9月5日{wa}は{/}
p#end_name(left: 60px; top: 800px; width: 960px; font-family: z; font-size: 120px; text-align: center; color: $washi; background: $sumi; border: 8px solid $sumi; padding: 18px 0px 26px 0px; in: {scale:0.6, opacity:0, duration:0.35, ease:'back.out(2.4)'}) 碓氷馬車鉄道
  div#line(left: 8px; top: 8px; width: 930px; height: 177px; border: 4px solid $washi)
p#end_sub(cx: 540px; top: 1060px; font-family: z; font-size: 96px; color: $sumi; in: {scale:0.6, opacity:0, duration:0.35, ease:'back.out(2.4)'}) 開業の日
img#end_horse(left: 600px; top: 1290px; width: 420px; height: 420px; content: @horse; in: {y:520, rotation:-8, duration:0.45, ease:'back.out(1.7)'})
p#end_note(left: 60px; top: 1500px; font-size: 36px; color: #1B15119E) ※諸説あり・一部演出を含みます
```

```timeline.txt
#v2
cast n = "明るくはきはきした30代の女性のナレーター、バラエティ番組の語りの声" manner="バラエティ番組のナレーターのように、明るく早口で、テンポよく畳みかけるように"
cast ogai = "渋く落ち着いた語り口の中年の男性の声" manner="格式ばった明治の文豪が、怒り心頭で苦々しく吐き捨てるように"
cast pass = "張りのある明るい若い男性の声" manner="呆れ果てて、声を張ってツッコむ"
silence head=0ms tail=0ms

*** hook
bgm music
se "拍子木をカンと打つ場面転換の音" -3dB
se hooves -9dB to=3.2s fade=0ms,600ms +100ms
@n: [manner:ワクワクした調子で、元気いっぱいに早口で][silence:350ms][>#hook_band -300ms][>#ht1 +280ms][♪pon -3dB +300ms][>#ht2 +620ms][!#ht2 to,{rotation:-3, duration:0.12, yoyo:true, repeat:5, ease:'power1.inOut'} +1900ms]9月5日は、馬が電車を引っ張った[!#ht1 punch {scale: 1.1, duration: .43}][♪jan -5dB]日！[silence:180ms]
transition panel {duration: .5, color: #D23F2A, skew: -14, dir: 'right'} se=swish -6dB

*** pass
[>#subtitle]
@n: [silence:120ms][>#ch1][>#date_plate -50ms][♪taiko -4dB -50ms][!#pass_bg shake {x: 7, duration: .25} -20ms][>#pin +1850ms][♪pon_hi -6dB +1850ms]1888年のこの日、碓氷峠に、[|]ある鉄道が開業しました。[silence:40ms]

*** loco
@n: [silence:40ms][>#loco_t +350ms][♪whistle -10dB +50ms to=0.95s fade=0ms,250ms]でも、坂が急すぎて[|]汽車は登れ[!#loco_t to,{y:40, rotation:4, duration:0.4, ease:'power2.in'} -100ms][♪"ヒューンと落ちていく落下音" -9dB -50ms]ない。[silence:100ms]

*** think
@n: [manner:早口で、もったいぶるように][silence:60ms][>#qmark -10ms][!#qmark to,{rotation:8, duration:0.4, yoyo:true, repeat:3, ease:'sine.inOut'} +240ms][>#poku[1] +10ms][♪"木魚をポクポクと叩いてチーンと鳴る音" -6dB +10ms start=0.85s to=3.25s fade=0ms,500ms][>#poku[2] +860ms][>#chiin +1710ms]そこで出した答えが……[silence:1200ms]
[<#subtitle]

*** answer
@n: [manner:勢いよく、得意げに言い切る][silence:50ms][>#horse_pop -20ms][♪"ピーンとひらめく音" -6dB -20ms][>#answer_t +120ms][!#horse_pop to,{rotation:4, duration:0.18, yoyo:true, repeat:3, ease:'sine.inOut'} +480ms][♪"馬がヒヒーンといななく声" -3dB +480ms]馬に引かせる！[silence:270ms]

*** name
@n: [silence:150ms][>#sonna +20ms]その名も、[>#cartouche -60ms][♪taiko -3dB -60ms][!#name_bg shake {x: 8, duration: .3} +120ms]碓氷馬車鉄道。[silence:60ms]

*** side1
[>#subtitle]
@n: [silence:20ms][♪hooves -11dB to=3.2s fade=0ms,500ms]線路の上の客車を、[|]馬がパカパカ引っ張ります。[silence:100ms]
@: [manner:ちょっと得意げに、早口でオチをつけるように][>#spec -50ms]動力は、文字どおりの[>#spec.v][♪pon_hi -5dB][!#spec.v punch {scale: 1.15, duration: .29} +480ms][♪"パフパフとラッパを鳴らす音" -2dB +480ms][♪hyoshigi -4dB +440ms to=0.7s]「馬力」。[silence:150ms]
[<#ch1 cut-0ms]
transition panel {duration: .5, color: #D23F2A, skew: -14, dir: 'right'}

*** ogai1
@n: [silence:250ms][>#ch2 -130ms][>#ogai_pop +80ms][♪pon -5dB +100ms]乗客には、あの文豪、[>#nameplate +280ms][♪pon_hi -5dB +280ms]森鴎外も。[silence:50ms]

*** scroll
@n: [manner:早口で、もったいぶるように][silence:30ms][>#paper -30ms][♪swish -10dB +20ms][>#youyaku +1340ms][♪pon_hi -4dB +1340ms][!#paper shake {x: 4, duration: .2} +1500ms]書き残した感想を、[|]ざっくりまとめると……[silence:160ms]
[<#subtitle]

*** rage
@ogai: [silence:100ms][♪impact -5dB -60ms to=2.5s fade=0ms,800ms][♪"ハエがブーンと飛び回る音" -13dB +100ms to=4.6s fade=300ms,800ms][>#brush1 +50ms]臭いと揺れが、[>#brush2 +180ms][♪"ガーンとショックを受けた時の短い音" -7dB +180ms][!#rage_bg shake {x: 15, duration: .55} +220ms][!#brush2 shake {x: 7, duration: .4} +300ms]最悪！[silence:340ms]
@n: [manner:あきれ半分に、面白がって早口で][<#brush1 -50ms][<#brush2 -50ms]文豪、[>#gekido +140ms][♪taiko -2dB +140ms][!#rage_bg shake {x: 12, duration: .45} +160ms][♪hyoshigi -4dB +740ms to=0.7s]大激怒。[silence:150ms]
[<#ch2 cut-0ms]
transition panel {duration: .5, color: #D23F2A, skew: -14, dir: 'right'}

*** slow
[>#subtitle]
@n: [manner:あきれたように、ツッコミ口調で早口で][silence:250ms][>#ch3 -130ms][>#gauge -150ms][!#gauge.needle to,{rotation:-84, duration:0.7, ease:'power3.out'} +100ms][!#gauge.needle to,{rotation:-81.5, duration:0.16, yoyo:true, repeat:3, ease:'sine.inOut'} +800ms][♪"キッチンタイマーのチクタクという音" -3dB to=2.6s fade=0ms,400ms][>#slow_t +550ms][!#slow_t to,{scaleX:1.25, scaleY:0.8, duration:0.5, ease:'sine.inOut'} +950ms][!#slow_t to,{scaleX:1, scaleY:1, duration:0.5, ease:'sine.inOut'} +1450ms][♪"土の上をザクザク歩く足音" -14dB +1200ms to=5.6s fade=400ms,800ms]しかも、あまりの遅さに、[|][<#land2 none -50ms][<#cart2 none -50ms][<#gauge none -50ms][<#slow_t none -50ms][>#walk_bg -50ms][>#walk_shade -50ms][>#zoku_t +100ms]途中で降りる乗客が続出。[silence:120ms]
[<#subtitle]
@pass: [<#zoku_t -100ms][>#bubble -20ms][♪"パシッと叩く打撃の音" +1dB +1530ms][!#bubble shake {x: 9, duration: .3} +1550ms][!#walk_bg shake {x: 7, duration: .3} +1550ms]歩いた方が早いわ！[silence:200ms]

*** overtake
[>#subtitle]
@n: [manner:哀愁をこめて、テンポよく][silence:100ms][>#ono1 +200ms][!#ono1 to,{x:200, duration:1.6, ease:'none'} +200ms][♪swish -9dB -150ms][>#ono2 +900ms]乗客に追い抜かれる[>#gloom][♪"チーンと低く鳴るりんの音" +4dB +50ms to=1.8s][♪hyoshigi -4dB -50ms to=0.7s]馬車。[silence:200ms]
[<#ch3 cut-0ms]
transition panel {duration: .5, color: #D23F2A, skew: -14, dir: 'right'}

*** omen
subtitle "でも 本当の地獄は下り坂"
@n: [manner:急に声を落として、早口で怖い話をするように][silence:250ms][>#ch4 -130ms][<#music +120ms][♪impact -6dB to=2.5s fade=0ms,800ms][>#go[*] +200ms][!#go[1] shake {x: 4, duration: 2} +500ms][!#go[2] shake {x: 4, duration: 2} +750ms][!#go[3] shake {x: 4, duration: 2} +1000ms][!#go[4] shake {x: 4, duration: 2} +1250ms][>#omen1 +450ms]でも本当の地獄は、[>#omen2 +50ms][♪taiko -4dB +50ms][!#omen_bg shake {x: 9, duration: .4} +70ms]下り坂。[silence:160ms]

*** rush
bgm rush
@n: [manner:大慌てで、スポーツ実況のように興奮して][silence:80ms][!#rush_bg shake {x: 8, duration: 8.1} -80ms][>#rush1 -60ms][♪"キーッと鳴る自転車のブレーキの音" -6dB -100ms][♪"ビューッと吹く強い風の音" -8dB +100ms][♪"ジェットコースターがゴーッと通過する音" -11dB +300ms start=1.5s to=8.1s fade=500ms,1000ms][>#speed +200ms]ブレーキが効かず、客車は[|]猛スピードで、山を駆け下りる！[silence:20ms]
[<#subtitle]
@pass: [manner:ジェットコースターに乗ったように、悲鳴を上げて][<#rush1 -200ms][>#scream][♪"キャッという女性の短い悲鳴" -7dB +100ms][♪"ホラーの甲高い絶叫" -5dB +300ms to=1.8s][!#scream shake {x: 9, duration: 1.7} +300ms]うわあああああっ！
@ogai: [manner:恐怖のあまり、情けない悲鳴を上げて]ひいいいいいっ！
[>#subtitle]
subtitle "まさにジェットコースター状態"
@n: [<#scream +300ms][>#jc1 +380ms][♪jan -8dB +420ms][>#jc2 +450ms]まさに、ジェットコースター状態。[|]明治の人、[>#inochi +20ms][♪taiko -6dB +20ms]命がけです。[silence:180ms]
[<#rush]
[<#ch4 cut-0ms]
transition panel {duration: .5, color: #D23F2A, skew: -14, dir: 'right'}

*** bridge
bgm music_b
@n: [silence:300ms][>#ch5 -180ms][>#tline +50ms][>#tline.bar +550ms][>#tline.mid +1100ms][♪whistle -14dB +1200ms start=1.6s to=2.9s fade=0ms,400ms][>#tline.n2 +1850ms][>#tline.ev2 +1850ms]結局、わずか5年足らずで[|]本格的な鉄道が開通し、[br]馬車鉄道は[>#intai][♪taiko -7dB]引退。[silence:260ms]
[<#subtitle]
@n: [manner:心をこめて、ねぎらうように、テンポよく][>#warm -300ms][<#tline -250ms][<#intai -250ms][>#otsukare +100ms]馬たち、本当におつかれさまでした。[silence:220ms]
[<#ch5 cut-0ms]
transition panel {duration: .5, color: #D23F2A, skew: -14, dir: 'right'}

*** end
@n: [♪"チャンチャンと締めるワンポイントの音" -4dB +100ms][>#end_date +120ms][>#end_name +360ms][>#end_sub +500ms][>#end_horse +700ms][silence:1.9s]
```

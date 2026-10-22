# story · usui-horse-rail (hf 全力版の全量の写し — 9月5日の歴史的珍事件「碓氷馬車鉄道」・17 場面を hard cut で畳みかける錦絵の豆知識コメディ) — canvas 720x1280

見せる作り: 章の境目だけ朱の斜めの帯が払う切替 (panel)・左上に残る章の札 (sticky)・金の極太テロップ (墨の縁 + 朱の硬い影・青 / 白 / 朱の変種) と古活字の判子を語に叩きつける (画面ごと揺れる)・錦絵の全面画 (基準画像で馬車を揃える) と透過の切り抜き・和紙 / 青海波 / 放射の地・横から見た線路の景色の def (3 場面)・速度計と年表の板・文の途中の絵替え・3 人の声・語ごとの効果音 (拍子木・太鼓・蹄・汽笛) と BGM の差し替え

```design.txt
#v2
# 学ぶ作り: 17 場面を切替なしの hard cut で畳みかけ、章の境目 5 か所だけ朱の斜めの帯が払う (panel)・章の札は sticky で章のあいだ左上に残る
# 文字は 4 書体の class で組む: 金の極太テロップ (墨の縁 + 朱の硬い影・青 / 白 / 朱の変種)・アンチックの明朝 (新字体)の札と判子・丸ゴシックの字幕 (縁取り・句ごとの札)・筆の擬音
# 絵は錦絵の全面画 (基準画像で馬車と人物を揃える) と透過の切り抜き (馬・文豪・客車・歩く人)・和紙 / 青海波 / 放射の地は図形と svg で描く
# hf b06 usui-horse-rail (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 720x1280 bg=#1B1511
theme dark
palette washi=#F3E7CF sumi=#1B1511 shu=#D23F2A ai=#1D3A63 kin=#FFD23F white=#FFFAF0 sky=#CFE6FF orange=#F39A2B purple=#5B2A86 paper=#F7EEDB
font "太く丸い丸ゴシック体、いちばん太いウェイト"
# engine: 字幕の丸ゴシックは hf (M+ 丸ゴシックの Black) よりわずかに細い — 書体の意味検索は family の既定の太さを返し、その family の既定は Regular なので説明文では Black に届かない (いま当たる丸ゴシックの Black が最も近い)
fonts d="超極太のディスプレイ用ゴシック体。最も太いウェイトで極めて太い画線と詰まった懐、ずっしりした幾何学的な字形の看板文字。パンチの効いたサムネイルや大見出し向き" z="新字体で組む、レトロで太いアンチックの明朝体、昭和の看板や見出しのような字面" b="荒々しい毛筆の楷書体、墨の勢いのある筆文字"
sfx off
# hf の作り: 見出しのテロップは台詞と同じ語を大きく先に見せる (spoiler・duplicate_text)・テロップで言う台詞には字幕を出さない (caption_gap)
# hf の作り: 判子と擬音は文末に叩きつけてすぐ次の場面へ切る (flash_text)・和紙の地の溜めと紀行文の場面は絵を置かない (text_only_cut)・語ごとに効果音を重ねる (se_dense)
# hf の作り: 金の放射の地に白の極太テロップ (墨の縁 + 朱の影で読ませる・low_contrast)
lint off=spoiler,duplicate_text,caption_gap,flash_text,text_only_cut,se_dense,low_contrast
art "明治時代の錦絵（多色刷りの浮世絵木版画）のスタイル。太く力強い墨の輪郭線、平坦で鮮やかな色面（藍・朱・黄土・若草色）、和紙の質感、ユーモラスで誇張された表情の戯画"
prompt_tail "画面内に文字・数字・ロゴ・署名・落款・題箋を一切描かない"
image hero = "急な山道に敷かれた細い線路の上を、馬が小さな木造の客車を必死に引っ張っている縦長の構図。客車には明治時代の洋装と和装の乗客がぎゅうぎゅう詰めで、窓から顔を出している。背景は険しい峠の山々と白い雲。馬は汗をかきながらも踏ん張っている。" aspect=9:16
image pass = "切り立った岩山の峠を間近に見上げる縦長 9:16 の構図。画面の上端から下端まで隙間なく色で描き込む: 画面の最上端は浮世絵の一文字ぼかし (濃い藍から群青へ移る帯) の空で塗り、そのすぐ下に白い雲海と青い連峰、岩山の頂は画面の上から 1 割の高さまでそびえる。画面の左上から松の大枝が張り出す。つづら折りの細い山道が画面の下から頂上まで続き、荷を背負った旅人が登る。右下の手前に藁葺きの小さな茶屋と休む客。空も色で塗り、和紙の無地の地や余白を画面のどこにも残さない。壮大でドラマチック。" aspect=9:16
image down = "[ref:@hero]急な下り坂の山道の線路を、馬車鉄道の小さな木造客車が猛スピードで暴走している縦長の構図。乗客たちは目を見開いて絶叫し、帽子や風呂敷包みが宙に舞う。後ろから馬が慌てて追いかけている。スピード線と土煙。ジェットコースターのような迫力とユーモア。" aspect=9:16
image cart = "[transparent]真横から見た、馬が小さな木造の客車（馬車鉄道の車両、車輪付き、レールの上を走る）を引っ張っている全身の図。客車の窓から明治時代の乗客が顔を出している。馬は画面の右側で右を向いて元気に歩き、客車はその左に続いて右へ進む。" aspect=3:2
image horse = "[transparent]得意げなドヤ顔でこちらを見る馬の顔のアップ。鼻息が荒く、片目をつぶってウインクしている。コミカルで力強い。"
image ogai = "[transparent]口ひげをたくわえた明治時代の洋装の若い紳士（文豪）の上半身。鼻をつまみ、顔を真っ赤にして目をむいて激怒している。頭から怒りの湯気。コミカルな戯画。"
sound hyoshigi = "拍子木をカンカンと打つ乾いた音"
sound whoosh = "スイングのシュッという速い動きの音"
sound swish = "カメラが流れるようなシュッという風切り音"
sound taiko = "和太鼓をドンと一発鳴らす音"
sound pon = "ポンと軽く鳴る明るいアクセントの音"
sound pon_hi = "ポンと鳴るアクセントの音、少し高め"
sound hooves = "馬の蹄がパカパカと鳴る足音"
sound whistle = "汽車のポーッという汽笛の音"
sound impact = "ドーンと響く衝撃のオノマトペの音"
sound jan = "ジャン！という驚きの効果音"
run k { color: $kin; font-family: d; font-size: 44px }
run wa { color: $sumi; font-family: z; font-size: 73px }
run r { color: $shu }
p { out: none }
div { border: none; out: none }
img { out: none }
svg { out: none }
shape { out: none }
group { out: none }
cut { stagger: 0 }
bgm#music(fade: 50,350) 見世物小屋の呼び込みのような賑やかでコミカルな和風の曲、三味線と太鼓と笛のお祭り調でテンポが良い
bgm#rush(fade: 80,700) 慌てふためくコミカルな和風の大騒ぎの曲、速い太鼓と三味線が畳みかける
bgm#music_b(fade: 900,1600) 見世物小屋の呼び込みのような賑やかでコミカルな和風の曲、三味線と太鼓と笛のお祭り調でテンポが良い
# 字幕: 丸ゴシック 44px の白 + 墨の縁・下 193 px・句ごとの札 ([|])・読点は空白・下から軽く出る
subtitle(left: 20px; bottom: 193px; width: 680px; font-size: 44px; line-height: 1.32; letter-spacing: 0.02em; text-align: center; color: $white; stroke: $sumi,7; background: none; unit: sentence; strip: 、。>space; lead: 0; tail: 0; hold: off; in: {y:17, opacity:0, duration:0.14, ease:'power2.out'}; out: none)
# 金の極太テロップ (墨の縁 + 朱の硬い影)。青 / 白 / 朱は色と影の引数で
def telop(t, s, c=$kin, sc=$sumi, sh=#A01E0FF2) = p(left: 16px; width: 688px; font-family: d; font-size: {s}; line-height: 1.2; text-align: center; color: {c}; stroke: {sc},10; text-shadow: 7px 7px 0px {sh}; content: {t})
# 縁取りの文字 (書体と大きさだけ変える)
def ol(t, s, f=d) = p(font-family: {f}; font-size: {s}; line-height: 1.25; text-align: center; stroke: $sumi,5; content: {t})
# 判子 (朱の太枠 + 生成りの地 + アンチックの明朝の朱文字)・叩きつけて傾いたまま残る
def stamp(t, s, w) = p(width: {w}; font-family: z; font-size: {s}; line-height: 1; text-align: center; color: $shu; background: #FFFAF0E0; border: 11px solid $shu; box-shadow: 7px 7px 0px #00000059; padding: 9px 0px 15px 0px; content: {t})
# 上下の減光 (上 62% → 透明 → 下 72%)
def shade() = div(inset: 0; background: linear(#0C08059E,#0C080500@22%,#0C080500@60%,#0C080573@82%,#0C0805B8,180); in: none)
# 和紙の地 (生成り + 左上の光 + 細い繊維の筋 + 周辺の焼け)
def washi(c=$washi) = div(inset: 0; background: {c}; pattern: hatch,-7,#785A280D,6,1; in: none)
  div#hi(inset: 0; background: radial(#FFFFFF59,#FFFFFF00@55%,30%,20%))
  div#vig(inset: 0; background: radial(#28140500@45%,#2814058C,50%,45%))
# 章の札 (朱の地に白の細枠の番号 + 縁取りの極太の題)・sticky で章のあいだ残る
def chapter(no, t) = div(left: 32px; top: 100px; width: 460px; height: 68px; z-index: front; in: none)
  div#no(left: 0px; cy: 50%; width: 137px; height: 64px; background: $shu; box-shadow: 5px 5px 0px #00000073; in: {x:-173, opacity:0, duration:0.3, ease:'back.out(1.8)'})
    div#line(left: 3px; top: 3px; width: 131px; height: 58px; border: 3px solid $white)
    p#t(cx: 50%; cy: 50%; font-family: z; font-size: 31px; content: {no})
  p#t(left: 152px; cy: 50%; width: 300px; font-family: d; font-size: 47px; letter-spacing: 0.02em; stroke: $sumi,5; delay: 80; in: {x:-80, opacity:0, duration:0.3, ease:'power3.out'}; content: {t})
# 横から見た線路の景色 (峠の絵の上半分 + 地面 + レール + 枕木)・3 場面で使う
def land() = div(inset: 0; background: $washi; in: none)
  # 峠の絵は上端の藍の空から雲海・連峰・頂・つづら折りの山道・右下の茶屋まで縦いっぱいに描き込まれている — 地面の上には絵の下半分 (雲海の下の峰と山道・茶屋の屋根) を敷く
  img#bg.bleed(left: -107px; top: -880px; width: 1000px; height: 1771px; content: @pass; main: none; in: none)
  div#fade(left: 0px; top: 0px; width: 720px; height: 867px; background: linear(#F3E7CF00@40%,#F3E7CF73,180); z-index: front)
  div#top(left: 0px; top: 0px; width: 720px; height: 280px; background: linear(#0C08059E,#0C080500,180); z-index: front)
  div#ground(left: 0px; top: 860px; width: 720px; height: 420px; background: linear(#C9A062,#B88A4C@40%,#7D5730,180); pattern: hatch,-28,#5A3C1E1A,15,2; z-index: front)
  div#edge(left: 0px; top: 860px; width: 720px; height: 4px; background: #6B4A2A; z-index: front)
  div#rail.bleed(left: -133px; top: 848px; width: 1000px; height: 12px; background: linear(#8A8F99,#2A2B30,180); z-index: front)
  div#sleepers.bleed(left: -267px; top: 859px; width: 1333px; height: 16px; pattern: hatch,0,#5A3B22,57,23; z-index: front)

svg gauge = """<svg viewBox="0 0 457 270"><path d="M46 227A187 187 0 0 1 49 193L135 209A100 100 0 0 0 133 227Z" fill="#549d49"/><path d="M49 195A187 187 0 0 1 58 162L139 192A100 100 0 0 0 135 210Z" fill="#68a348"/><path d="M57 163A187 187 0 0 1 72 132L147 176A100 100 0 0 0 139 193Z" fill="#7caa47"/><path d="M71 134A187 187 0 0 1 91 106L157 162A100 100 0 0 0 146 177Z" fill="#90b046"/><path d="M90 107A187 187 0 0 1 114 83L169 150A100 100 0 0 0 156 163Z" fill="#a4b644"/><path d="M113 84A187 187 0 0 1 141 64L184 140A100 100 0 0 0 169 150Z" fill="#b9bc43"/><path d="M140 65A187 187 0 0 1 170 51L199 133A100 100 0 0 0 183 140Z" fill="#cdc242"/><path d="M169 51A187 187 0 0 1 202 43L216 128A100 100 0 0 0 199 133Z" fill="#e1c941"/><path d="M201 43A187 187 0 0 1 234 40L234 127A100 100 0 0 0 216 129Z" fill="#f5cf40"/><path d="M233 40A187 187 0 0 1 267 43L251 129A100 100 0 0 0 233 127Z" fill="#fcca3e"/><path d="M265 43A187 187 0 0 1 298 52L268 133A100 100 0 0 0 250 129Z" fill="#f8ba3c"/><path d="M297 51A187 187 0 0 1 328 66L284 141A100 100 0 0 0 267 133Z" fill="#f2a939"/><path d="M326 65A187 187 0 0 1 354 85L298 151A100 100 0 0 0 283 140Z" fill="#ee9937"/><path d="M353 84A187 187 0 0 1 377 108L310 163A100 100 0 0 0 297 150Z" fill="#e88834"/><path d="M376 107A187 187 0 0 1 396 135L320 178A100 100 0 0 0 310 163Z" fill="#e47832"/><path d="M395 134A187 187 0 0 1 409 164L327 193A100 100 0 0 0 320 177Z" fill="#de6830"/><path d="M409 163A187 187 0 0 1 417 196L332 210A100 100 0 0 0 327 193Z" fill="#da582e"/><path d="M417 195A187 187 0 0 1 420 227L333 227A100 100 0 0 0 331 210Z" fill="#d4472b"/><line x1="233" y1="227" x2="79" y2="88" stroke="#1b1511" stroke-width="5" stroke-dasharray="11 8"/></svg>"""
svg seigaiha = """<svg viewBox="0 0 720 1280"><defs><pattern id="w" width="80" height="40" patternUnits="userSpaceOnUse"><rect width="80" height="40" fill="#1d3a63"/><circle cx="0" cy="20" r="40" fill="#27497a"/><circle cx="0" cy="20" r="36" fill="#1d3a63"/><circle cx="0" cy="20" r="28" fill="#27497a"/><circle cx="0" cy="20" r="24" fill="#1d3a63"/><circle cx="0" cy="20" r="17" fill="#27497a"/><circle cx="0" cy="20" r="12" fill="#1d3a63"/><circle cx="0" cy="20" r="4" fill="#27497a"/><circle cx="80" cy="20" r="40" fill="#27497a"/><circle cx="80" cy="20" r="36" fill="#1d3a63"/><circle cx="80" cy="20" r="28" fill="#27497a"/><circle cx="80" cy="20" r="24" fill="#1d3a63"/><circle cx="80" cy="20" r="17" fill="#27497a"/><circle cx="80" cy="20" r="12" fill="#1d3a63"/><circle cx="80" cy="20" r="4" fill="#27497a"/><circle cx="40" cy="40" r="40" fill="#27497a"/><circle cx="40" cy="40" r="36" fill="#1d3a63"/><circle cx="40" cy="40" r="28" fill="#27497a"/><circle cx="40" cy="40" r="24" fill="#1d3a63"/><circle cx="40" cy="40" r="17" fill="#27497a"/><circle cx="40" cy="40" r="13" fill="#1d3a63"/><circle cx="40" cy="40" r="6" fill="#27497a"/><circle cx="0" cy="60" r="40" fill="#27497a"/><circle cx="0" cy="60" r="36" fill="#1d3a63"/><circle cx="0" cy="60" r="28" fill="#27497a"/><circle cx="0" cy="60" r="24" fill="#1d3a63"/><circle cx="80" cy="60" r="40" fill="#27497a"/><circle cx="80" cy="60" r="36" fill="#1d3a63"/><circle cx="80" cy="60" r="28" fill="#27497a"/><circle cx="80" cy="60" r="24" fill="#1d3a63"/></pattern></defs><rect width="720" height="1280" fill="url(#w)"/></svg>"""
svg fly = """<svg viewBox="0 0 56 44"><ellipse cx="41" cy="14" rx="8" ry="12" transform="rotate(-30 41 14)" fill="#e1ebfabf"/><ellipse cx="19" cy="15" rx="11" ry="15" transform="rotate(-30 19 15)" fill="#e1ebfabf" stroke="#222" stroke-width="3"/><ellipse cx="28" cy="29" rx="16" ry="13" fill="#111"/></svg>"""
svg gloom = """<svg viewBox="0 0 427 400"><defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="400"><stop offset=".55" stop-color="#283c8c" stop-opacity=".55"/><stop offset="1" stop-color="#283c8c" stop-opacity="0"/></linearGradient><pattern id="p" width="17" height="400" patternUnits="userSpaceOnUse"><rect width="4" height="400" fill="url(#g)"/></pattern></defs><rect width="427" height="400" fill="url(#p)"/></svg>"""

# 冒頭: 馬が客車を引く絵に寄りから引き、上に「9月5日の歴史的珍事件」の帯・下に 2 行の大テロップが傾いて弾む
section#hook
img#hook_bg(inset: 0; content: @hero; main: kb {scale: [1.22, 1.06], focus: ['33% 36%', '50% 50%']})
shade#hook_shade
# hf の作り: 帯の書体はアンチックの明朝 (新字体)・「9月5日」だけ run k で極太ゴシックの金
p#hook_band(cx: 360px; top: 100px; font-family: z; font-size: 40px; letter-spacing: 0.07em; background: $shu; padding: 8px 27px 11px 27px; box-shadow: 0px 7px 0px #00000059; in: {y:-40, opacity:0, duration:0.3, ease:'power3.out'}) {k}9月5日{/}の歴史的珍事件
  div#rule_top(left: 0px; top: 0px; width: 100%; height: 3px; background: $kin)
  div#rule_bottom(left: 0px; bottom: 0px; width: 100%; height: 3px; background: $kin)
telop#ht1(top: 787px; s: 100; transform-origin: 50% 80%; in: {scale:0.2, rotation:-6, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 馬が電車を
telop#ht2(top: 899px; s: 117; c: $white; transform-origin: 50% 80%; in: {scale:0.2, rotation:5, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 引っ張る!?

# 其の一 開業: 峠の絵を下から上へ流し、年月日の札を叩きつけ (絵が揺れる)・「碓氷峠」の立て札のピンが弾む
section#pass
# hf は峠を上から下へ流す — 絵は上端の空から下端の茶屋まで描き込まれているので、不動点を下端の右寄りに置き、雲海の下の峰・つづら折りの山道・茶屋を大きく見せて引く
img#pass_bg(inset: 0; content: @pass; main: kb {scale: [1.95, 1.8], focus: ['60% 100%', '60% 100%']})
shade#pass_shade
# 章の札 (sticky・この章の最後の cut の末尾で閉じる)
chapter#ch1.sticky(no: "其の一"; t: "開業")
group#date_plate(left: 40px; top: 200px; width: 520px; height: 150px; transform: rotate(-3deg); in: {scale:1.9, rotation:-6, opacity:0, duration:0.2, ease:'power4.in'})
  ol#era(left: 0px; top: 0px; s: 35; f: z; text-align: left) 明治21年
  p#ymd(left: 0px; top: 50px; width: 500px; white-space: nowrap; font-family: d; font-size: 88px; line-height: 1.15; color: $kin; stroke: $sumi,7; text-shadow: 5px 5px 0px #A01E0FF2) 1888.9.5
div#pin(left: 313px; top: 507px; width: 226px; height: 223px; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'})
  div#tag(left: 0px; top: 0px; width: 226px; height: 124px; background: $washi; border: 4px solid $sumi; box-shadow: 7px 7px 0px #00000073)
    p#big(cx: 50%; top: 9px; font-family: z; font-size: 61px; line-height: 1; color: $sumi) 碓氷峠
    p#sm(cx: 50%; top: 77px; font-family: z; font-size: 27px; color: $shu) 群馬 ⇔ 長野
  div#stem(cx: 50%; top: 124px; width: 5px; height: 80px; background: $sumi)
  div#dot(cx: 50%; top: 200px; width: 23px; height: 23px; border-radius: 99px; background: $shu; border: 4px solid $white)

# 急勾配の前で止まる汽車の絵が傾きながら寄り、青のテロップ「急すぎて 登れない…」が弾んで出て文末でうなだれる
section#loco
img#loco_bg(inset: 0; main: keys(at=0 scale=1.08 rotation=-1.5 | at=1 scale=1.16 rotation=1.5 ease=none)) 壁のように急な坂のふもとで、明治時代の小さな蒸気機関車が坂を見上げて立ち往生している縦長の構図。画面の上端まで濃い青空と白いもくもくの雲が埋め、和紙の無地の余白を作らない。線路は画面の右下から右上の端へ壁のような岩山を一直線に登る。機関車は画面の下半分の左寄り、煙突から弱々しい煙、機関士が頭を抱えて途方に暮れている。コミカルな構図。
shade#loco_shade
telop#loco_t(top: 373px; s: 88; c: $sky; sh: #14285AF2; in: {scale:0.5, opacity:0, duration:0.42, ease:'back.out(1.6)'}) 急すぎて[br]登れない…

# 溜め: 和紙の地に朱の「？」が揺れ、「ポク」「ポク」と筆の「チーン」が順に弾む
section#think
washi#think_washi
ol#qmark(left: 0px; width: 720px; top: 347px; s: 347; line-height: 1; color: $shu; stroke: $sumi,9; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'}) ？
ol#poku(left: "66;520"; top: "287;373"; width: 140px; s: 64; color: $sumi; stroke: $washi,5; in: {scale:0.5, opacity:0, duration:0.25, ease:'back.out(2.4)'}) ×2 ポク;ポク
ol#chiin(left: 0px; width: 720px; top: 753px; s: 127; f: b; color: $shu; stroke: $white,7; text-shadow: 4px 4px 0px #00000059; in: {scale:0.6, opacity:0, duration:0.3, ease:'back.out(2.4)'}) チーン

# 答え: 回る金と橙の放射の地に、ウインクする馬の顔が回りながら弾み、白のテロップ「馬に引かせる！」
section#answer
div#rays_bg(inset: 0; background: $orange; in: none)
shape#rays.bleed(left: -640px; top: -440px; width: 2000px; height: 2000px; path: sunburst,n=20; background: $kin; main: spin {period: 13.32}; in: none)
img#horse_pop(left: 60px; top: 240px; width: 600px; height: 600px; content: @horse; in: {scale:0.15, rotation:-12, opacity:0, duration:0.5, ease:'back.out(2.4)'})
telop#answer_t(left: 4px; width: 712px; top: 827px; s: 100; c: $white; in: {scale:0.3, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 馬に引かせる！

# 名前: 同じ絵に寄った構図で「その名も」の黒札が上がり、二重枠の名札「碓氷馬車鉄道」(ふりがな・開業年) を叩きつける
section#name
img#name_bg(inset: 0; content: @hero; main: kb {scale: [1.3, 1.16], focus: ['13% 22%', '15% 17%']})
shade#name_shade
p#sonna(cx: 360px; top: 400px; font-family: z; font-size: 43px; background: $sumi; padding: 4px 20px 7px 20px; in: {y:27, opacity:0, duration:0.25, ease:'power3.out'}) その名も
div#cartouche(left: 33px; top: 480px; width: 654px; height: 236px; background: $washi; border: 4px solid $sumi; box-shadow: 11px 11px 0px #00000080; in: {scale:1.8, opacity:0, duration:0.2, ease:'power4.in'})
  div#d1(left: 3px; top: 3px; width: 640px; height: 222px; border: 2px solid $shu)
  div#d2(left: 9px; top: 9px; width: 628px; height: 210px; border: 2px solid $shu)
  p#rt(left: 57px; top: 14px; width: 130px; font-family: z; font-size: 31px; letter-spacing: 0.17em; text-align: center; color: $shu) うすい
  p#nm(left: 0px; top: 60px; width: 100%; text-align: center; font-family: z; font-size: 100px; line-height: 1.15; letter-spacing: 0.04em; color: $sumi) 碓氷馬車鉄道
  p#yr(left: 0px; top: 182px; width: 100%; text-align: center; font-size: 29px; color: $shu) 1888年（明治21年）開業

# 横から: 峠の景色が流れ、客車を引く馬が左から入って揺れ続ける・「動力」の札が右から入り、文末の語で朱の「馬力」が弾む
section#side1
land#land1
  img#bg(left: -131px; in: {x:24, duration:5.05, ease:'none'})
  div#sleepers(left: -496px; in: {x:229, duration:5.05, ease:'none'})
img#cart1(left: 33px; top: 525px; width: 653px; height: 435px; content: @cart; in: {x:-667, duration:2.0, ease:'power2.out'}; main: sine {y: -5, period: 0.26})
div#spec(left: 47px; top: 220px; width: 626px; height: 136px; background: $washi; border: 5px solid $sumi; box-shadow: 9px 9px 0px #00000066; padding: 12px 23px 17px 23px; display: flex; align-items: center; gap: 20px; in: {x:600, opacity:0, duration:0.35, ease:'back.out(1.4)'})
  p#k(font-family: z; font-size: 43px; background: $sumi; padding: 3px 12px 7px 12px) 動力
  p#v(width: 226px; font-family: d; font-size: 100px; line-height: 1.2; color: $shu; in: {scale:0.4, opacity:0, duration:0.35, ease:'back.out(1.7)'}) 馬力
  p#note(font-size: 27px; line-height: 1.2; color: $sumi) ※文字どおり[br]（馬が引く）

# 其の二 文豪、激怒: 青海波の地に光の輪・怒る文豪の切り抜きが下から弾み、縦書きの朱の名札「文豪 森鴎外」を叩きつける
section#ogai1
svg#wave(inset: 0; part: seigaiha; in: none)
div#spot(left: 27px; top: 200px; width: 667px; height: 667px; border-radius: 999px; background: radial(#FFE6AA8C,#FFE6AA00@68%,50%,50%); in: none)
chapter#ch2.sticky(no: "其の二"; t: "文豪、激怒")
img#ogai_pop(left: 20px; top: 190px; width: 680px; height: 680px; content: @ogai; in: {y:200, scale:0.5, opacity:0, duration:0.45, ease:'back.out(1.6)'})
div#nameplate(left: 530px; top: 216px; width: 153px; height: 395px; background: $shu; box-shadow: 8px 8px 0px #00000073; in: {scale:1.7, opacity:0, duration:0.2, ease:'power4.in'})
  div#line(left: 3px; top: 3px; width: 147px; height: 389px; border: 4px solid $white)
  p#t(cx: 50%; top: 24px; font-family: z; font-size: 32px; letter-spacing: 0.13em; vertical: true) 文豪
  p#n(cx: 50%; top: 104px; font-family: z; font-size: 85px; letter-spacing: 0.08em; vertical: true) 森鴎外

# 紀行文: 暗い和紙の地に縦罫の原稿が上から開き、墨の行の上に朱の判子「要約」を傾けて押す
section#scroll
washi#scroll_washi(c: #C7BDAA)
div#paper(left: 100px; top: 220px; width: 520px; height: 693px; background: $paper; border: 2px solid #B9A37A; box-shadow: 12px 12px 0px #00000059; pattern: hatch,0,#C83C288C,64,2; in: {scaleY:0.02, opacity:0, duration:0.45, ease:'power3.out', pivot:'top'})
  p#ttl(right: 20px; top: 27px; font-family: z; font-size: 48px; letter-spacing: 0.14em; color: $sumi; vertical: true) 紀行文
  div#col(left: "383;319;255;191;127;63"; top: 47px; width: 12px; height: "427;547;347;507;587;287"; border-radius: 6px; background: #1B1511C7) ×6
p#youyaku(left: 153px; top: 547px; width: 220px; height: 220px; font-family: z; font-size: 85px; line-height: 1; text-align: center; color: $shu; background: #F7EEDB40; border: 9px solid $shu; border-radius: 20px; transform: rotate(-10deg); in: {scale:2.2, rotation:-20, opacity:0, duration:0.2, ease:'power4.in'}) 要約

# 激怒: 揺れる車内で鼻をつまむ文豪の絵に寄り続け、ハエが飛び回る・「臭いと揺れが」→ 筆の朱「最悪！」で画面ごと揺れ → 判子「文豪、大激怒」
section#rage
img#rage_bg(inset: 0; main: kb {scale: [1.06, 1.2]}) [ref:@ogai]狭くて激しく揺れる馬車鉄道の木造客車の車内、縦長の構図。口ひげをたくわえた明治時代の洋装の若い紳士（文豪）が、片手で鼻をつまみ、もう片方の手で帽子を押さえながら、顔を真っ赤にして激怒している。周りの乗客と肩がぶつかり合い、皆よろけている。窓の外には客車を引く馬の後ろ姿。頭から湯気が出ている。
shade#rage_shade
svg#fly(left: "467;220;520"; top: "347;313;507"; width: 37px; height: 29px; part: fly; in: none; main: noise {x: 53, y: 40, rotation: 27, period: 0.44}) ×3
ol#brush1(left: 0px; width: 720px; top: 587px; s: 69; stroke: $sumi,7; in: {scale:0.6, opacity:0, duration:0.42, ease:'back.out(2.4)'}; out: {opacity:0, duration:0.15, ease:'none'}) 臭いと揺れが
ol#brush2(left: 16px; width: 688px; top: 680px; s: 200; f: b; line-height: 1.25; color: $shu; stroke: $white,7; text-shadow: 8px 8px 0px #000000CC; transform: rotate(-4deg); in: {scale:2.4, rotation:-8, opacity:0, duration:0.2, ease:'power4.in'}; out: {opacity:0, duration:0.15, ease:'none'}) 最悪！
div#gekido(left: 167px; top: 587px; width: 387px; height: 213px; background: #FFFAF0E0; border: 11px solid $shu; box-shadow: 7px 7px 0px #00000059; transform: rotate(-9deg); in: {scale:2.6, rotation:-18, opacity:0, duration:0.2, ease:'power4.in'})
  p#sm(cx: 50%; top: 12px; font-family: z; font-size: 43px; line-height: 1; color: $sumi) 文豪、
  p#big(cx: 50%; top: 59px; font-family: z; font-size: 113px; line-height: 1; color: $shu) 大激怒

# 其の三 遅すぎ: 横の景色で客車がのろのろ進み、速度計の針が「徒歩の速さ」の手前で震える・青の「遅っ!!」が伸び縮み
# → 文の途中の語で「途中下車」の絵へ替え、金の「途中下車 続出!!」→ 乗客の吹き出し「歩いた方が早いわ！」で画面ごと揺れる
section#slow
land#land2
img#cart2(left: 13px; top: 525px; width: 653px; height: 435px; content: @cart; in: {x:-33, duration:1.69, ease:'none'}; main: sine {y: -2, period: 0.6})
chapter#ch3.sticky(no: "其の三"; t: "遅すぎ")
div#gauge(left: 127px; top: 220px; width: 467px; height: 280px; background: $washi; border: 5px solid $sumi; box-shadow: 9px 9px 0px #00000066; in: {y:-40, opacity:0, duration:0.3, ease:'power3.out'})
  svg#face(left: 0px; top: 0px; width: 457px; height: 270px; part: gauge)
  p#lab(left: 9px; top: 25px; width: 172px; text-align: center; font-family: d; font-size: 29px; background: $sumi; padding: 1px 9px 4px 9px; white-space: nowrap) 徒歩の速さ
  div#needle(left: 230px; top: 60px; width: 7px; height: 167px; border-radius: 4px; background: $sumi; transform: rotate(-20deg); transform-origin: 50% 100%; z-index: front)
  div#hub(left: 217px; top: 212px; width: 32px; height: 32px; border-radius: 99px; background: $shu; border: 4px solid $sumi; z-index: front)
  p#label(cx: 50%; top: 233px; font-family: z; font-size: 29px; color: $sumi) 馬車鉄道の速さ
  p#slow_end(left: 27px; top: 235px; width: 54px; font-family: d; font-size: 23px; color: $sumi) 遅い
  p#fast_end(right: 27px; top: 235px; width: 54px; font-family: d; font-size: 23px; color: $sumi) 速い
telop#slow_t(top: 827px; s: 120; c: $sky; sh: #14285AF2; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'}) 遅っ!!
img#walk_bg(inset: 0; in: none; main: kb {scale: [1.16, 1.1], focus: ['9% 50%', '96% 50%']}) [ref:@hero]山道の線路の上を、馬に引かれた小さな客車がのろのろと進んでいる。その横を、客車から降りた明治時代の乗客たち（着物の男性、洋装の紳士、荷物を背負った行商人）が呆れ顔ですたすた歩いて追い抜いていく縦長の構図。馬はへとへとで舌を出している。コミカル。
shade#walk_shade
telop#zoku_t(top: 293px; s: 100; in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.4)'}; out: {opacity:0, duration:0.12, ease:'none'}) 途中下車[br]続出!!
p#bubble(left: 47px; top: 220px; width: 627px; font-family: d; font-size: 77px; line-height: 1.15; text-align: center; color: $sumi; background: $white; border: 7px solid $sumi; border-radius: 47px; box-shadow: 9px 9px 0px #00000066; padding: 23px 13px 29px 13px; pointer: below,25%; in: {scale:0.3, opacity:0, duration:0.38, ease:'back.out(2.4)'}) 歩いた方が[br]{r}早いわ！{/}

# 追い抜かれる: 同じ横の景色で、歩く乗客が左から右へ跳ねながら客車を追い抜く・「スタスタ」が並んで流れ、文末に筆の「トボトボ…」と青い陰の筋
section#overtake
land#land3
img#cart3.bleed(left: 220px; top: 525px; width: 653px; height: 435px; content: @cart; in: none; main: sine {y: -1, period: 0.7})
svg#gloom(left: 240px; top: 467px; width: 427px; height: 400px; part: gloom; in: {y:-40, opacity:0, duration:0.5, ease:'power2.out'})
img#walker.bleed(left: 747px; top: 483px; width: 253px; height: 380px; aspect: 2:3; in: {x:-1027, duration:2.3, ease:'none'}; main: sine {y: -6, rotation: 2, period: 0.28}) [transparent]真横から見た、右を向いてすたすた大股で歩く明治時代の着物姿の男性の全身。呆れたしかめ面で、風呂敷包みを肩にかついでいる。
ol#ono1(left: 287px; top: 400px; width: 236px; s: 53; overlap: land3.bg; in: {scale:0.4, opacity:0, duration:0.3, ease:'back.out(2.4)'}) スタスタ
ol#ono2(left: 280px; top: 887px; s: 69; f: b; stroke: $sumi,6; in: {scale:0.6, opacity:0, duration:0.3, ease:'back.out(2.4)'}) トボトボ…

# 其の四 暴走: 暴走する客車の絵を暗く沈め、紫の「ゴ」が 4 つ震え・「本当の地獄は」→ 朱の「下り坂」を叩きつけ画面ごと揺れる
section#omen
img#omen_bg(inset: 0; content: @down; filter: brightness(0.55) saturate(0.6); main: kb {scale: [1.06, 1.18]})
shade#omen_shade
div#dark(inset: 0; background: radial(#3C000059,#140000D9,50%,50%); in: none)
chapter#ch4.sticky(no: "其の四"; t: "暴走")
ol#omen1(left: 0px; width: 720px; top: 373px; s: 64; f: z; in: {scale:0.8, opacity:0, duration:0.35, ease:'power2.out'}) 本当の地獄は
telop#omen2(top: 480px; s: 153; c: $shu; sc: $white; sh: #000000D9; transform: rotate(-3deg); in: {scale:2.4, rotation:-6, opacity:0, duration:0.2, ease:'power4.in'}) 下り坂
# hf の作り: 紫の「ゴ」は 2 つずつ斜めに重ねて積む (overlap)
ol#go(left: "40;120;547;612"; top: "707;767;720;802"; width: 96px; s: 80; color: $purple; stroke: $white,5; in: {scale:0.5, opacity:0, duration:0.3, ease:'back.out(2.4)', stagger: {each: 0.25}}) ×4 ゴ;ゴ;ゴ;ゴ

# 暴走: 同じ絵を明るく戻して寄り続け、全編揺れる・白の集中線・金の「ブレーキ 効かず!!」→ 1 字ずつ弾む悲鳴 → 「明治の ジェットコースター」と判子「命がけ」
section#rush
img#rush_bg(inset: 0; content: @down; main: kb {scale: [1.08, 1.34]})
shade#rush_shade
shape#speed.bleed(left: -640px; top: -373px; width: 2000px; height: 2000px; path: rays,n=30,inner=0.28; background: none; border: 3px solid #FFFFFFBF; in: {opacity:0, duration:0.2, ease:'none'}; main: noise {rotation: 2.2, period: 0.12})
telop#rush1(top: 220px; s: 91; transform: rotate(-4deg); in: {scale:2.0, rotation:-8, opacity:0, duration:0.2, ease:'power4.in'}; out: {scale:0.8, opacity:0, duration:0.18, ease:'power2.in'}) ブレーキ[br]効かず!!
ol#scream(left: 0px; width: 720px; top: 507px; s: 100; stroke: $sumi,7; in: {scale:0.3, opacity:0, duration:0.25, ease:'back.out(2.4)', stagger: 0.06}; out: {opacity:0, duration:0.15, ease:'none'}) ぎゃああ!!
ol#jc1(left: 0px; width: 720px; top: 227px; s: 56; f: z; in: {scale:0.6, opacity:0, duration:0.3, ease:'back.out(2.4)'}) 明治の
telop#jc2(top: 300px; s: 67; line-height: 1.32; letter-spacing: -0.02em; in: {scale:0.3, opacity:0, duration:0.4, ease:'back.out(2.4)'}) ジェットコースター
stamp#inochi(left: 167px; top: 547px; w: 387; s: 100; white-space: nowrap; transform: rotate(-10deg); in: {scale:2.4, rotation:-20, opacity:0, duration:0.2, ease:'power4.in'}) 命がけ

# 其の五 引退: 赤レンガの橋を渡る汽車と見送る馬の絵を上から下へ・年表の板 (棒が伸びて 1893 に点)・判子「引退」→ 暖かい光と「馬たち、本当に おつかれさまでした」
section#bridge
img#bridge_bg(inset: 0; main: kb {scale: [1.22, 1.08], focus: ['50% 78%', '50% 0%']}) 深い緑の山あいに架かる赤レンガ造りの大きなアーチ橋を、明治時代の蒸気機関車が白い煙を上げて渡っていく縦長の構図。手前の野原では、引退した馬たちがのんびり草を食べながら機関車を見送っている。晴れやかで穏やかな雰囲気。
shade#bridge_shade
chapter#ch5.sticky(no: "其の五"; t: "引退")
div#warm(inset: 0; background: radial(#FFD67873,#FFD67800@70%,50%,70%); in: {opacity:0, duration:1.2, ease:'sine.inOut'})
div#tline(left: 47px; top: 220px; width: 626px; height: 220px; background: #F3E7CFF0; border: 5px solid $sumi; box-shadow: 9px 9px 0px #00000066; in: {y:-40, opacity:0, duration:0.35, ease:'power3.out'}; out: {y:-27, opacity:0, duration:0.3, ease:'power2.in'})
  p#mid(left: 0px; top: 69px; width: 100%; text-align: center; font-family: d; font-size: 36px; color: $shu; in: {scale:0.5, opacity:0, duration:0.3, ease:'back.out(2.4)'}) わずか5年足らず
  div#bar(left: 133px; top: 124px; width: 349px; height: 9px; background: $sumi; in: {scaleX:0, duration:1.3, ease:'power2.inOut', pivot:'left'})
  div#n1(left: 115px; top: 111px; width: 36px; height: 36px; border-radius: 99px; background: $shu; border: 5px solid $sumi)
  div#n2(left: 465px; top: 111px; width: 36px; height: 36px; border-radius: 99px; background: $shu; border: 5px solid $sumi; in: {scale:0, duration:0.3, ease:'back.out(2.4)'})
  p#y1(left: 33px; top: 151px; width: 200px; font-family: d; font-size: 39px; text-align: center; color: $sumi) 1888
  p#y2(left: 383px; top: 151px; width: 200px; font-family: d; font-size: 39px; text-align: center; color: $sumi) 1893
  p#ev1(left: 33px; top: 23px; width: 200px; font-family: z; font-size: 31px; text-align: center; color: $sumi; white-space: nowrap) 馬車鉄道 開業
  p#ev2(left: 383px; top: 23px; width: 200px; font-family: z; font-size: 31px; text-align: center; color: $shu; white-space: nowrap; in: {opacity:0, duration:0.2, ease:'none'}) 鉄道 開通
stamp#intai(left: 400px; top: 673px; w: 253; s: 93; padding: 7px 0px 12px 0px; transform: rotate(8deg); in: {scale:2.4, rotation:16, opacity:0, duration:0.2, ease:'power4.in'}; out: {opacity:0, duration:0.25, ease:'none'}) 引退
ol#otsukare(left: 0px; width: 720px; top: 787px; s: 69; f: z; in: {scale:0.85, opacity:0, duration:0.6, ease:'power2.out'}) 馬たち、[br]本当に[br]おつかれさまでした

# 締め: 和紙の地に朱の「9月5日は」を叩きつけ、黒の名札「碓氷馬車鉄道」・「開業の日」・下から馬の顔が起き上がる
section#end
washi#end_washi
p#end_date(cx: 360px; top: 313px; font-family: d; font-size: 153px; line-height: 1.22; color: $shu; stroke: $sumi,7; transform: rotate(-2deg); in: {scale:1.8, rotation:-4, opacity:0, duration:0.2, ease:'power4.in'}) 9月5日{wa}は{/}
p#end_name(left: 40px; top: 533px; width: 640px; font-family: z; font-size: 80px; text-align: center; color: $washi; background: $sumi; border: 5px solid $sumi; padding: 12px 0px 17px 0px; in: {scale:0.6, opacity:0, duration:0.35, ease:'back.out(2.4)'}) 碓氷馬車鉄道
  div#line(left: 5px; top: 5px; width: 620px; height: 118px; border: 3px solid $washi)
p#end_sub(cx: 360px; top: 707px; font-family: z; font-size: 64px; color: $sumi; in: {scale:0.6, opacity:0, duration:0.35, ease:'back.out(2.4)'}) 開業の日
img#end_horse(left: 400px; top: 860px; width: 280px; height: 280px; content: @horse; in: {y:347, rotation:-8, duration:0.45, ease:'back.out(1.7)'})
p#end_note(left: 40px; top: 1000px; font-size: 24px; color: #1B15119E) ※諸説あり・一部演出を含みます
```

```timeline.txt
#v2
cast n = "明るくはきはきした30代の女性のナレーター、バラエティ番組の語りの声" manner="バラエティ番組のナレーターのように、明るく早口で、テンポよく畳みかけるように"
cast ogai = "渋く落ち着いた語り口の中年の男性の声" manner="格式ばった明治の文豪が、怒り心頭で苦々しく吐き捨てるように"
cast pass = "張りのある明るい若い男性の声" manner="呆れ果てて、声を張ってツッコむ"
silence head=0 tail=0

*** hook
bgm music
se "拍子木をカンと打つ場面転換の音" -3dB
se hooves -9dB to=3.2s fade=0,600 +100
@n: [manner:ワクワクした調子で、元気いっぱいに早口で][silence:350][>#hook_band -300][>#ht1 +280][♪pon -3dB +300][>#ht2 +620][!#ht2 to,{rotation:-3, duration:0.12, yoyo:true, repeat:5, ease:'power1.inOut'} +1900]{9月5日|くがついつか}は、馬が電車を引っ張った[!#ht1 punch,1.1,duration=430][♪jan -5dB]日！[silence:180]
transition panel,500,color=#D23F2A,skew=-14,dir=right,se=swish -6dB

*** pass
[>#subtitle]
@n: [silence:120][>#ch1][>#date_plate -50][♪taiko -4dB -50][!#pass_bg shake,7,duration=250 -20][>#pin +1850][♪pon_hi -6dB +1850]1888年のこの日、{碓氷|うすい}峠に、[|]ある鉄道が開業しました。[silence:40]

*** loco
@n: [silence:40][>#loco_t +350][♪whistle -10dB +50 to=0.95s fade=0,250]でも、坂が急すぎて[|]汽車は登れ[!#loco_t to,{y:27, rotation:4, duration:0.4, ease:'power2.in'} -100][♪"ヒューンと落ちていく落下音" -9dB -50]ない。[silence:100]

*** think
@n: [manner:早口で、もったいぶるように][silence:60][>#qmark -10][!#qmark to,{rotation:8, duration:0.4, yoyo:true, repeat:3, ease:'sine.inOut'} +240][>#poku[1] +10][♪"木魚をポクポクと叩いてチーンと鳴る音" -6dB +10 start=0.85s to=3.25s fade=0,500][>#poku[2] +860][>#chiin +1710]そこで出した答えが……[silence:500]
[<#subtitle]

*** answer
@n: [manner:勢いよく、得意げに言い切る][silence:50][>#horse_pop -20][♪"ピーンとひらめく音" -6dB -20][>#answer_t +120][!#horse_pop to,{rotation:4, duration:0.18, yoyo:true, repeat:3, ease:'sine.inOut'} +1210][♪"馬がヒヒーンといななく声" -3dB +1180]馬に引かせる！[silence:270]

*** name
@n: [silence:150][>#sonna +20]その名も、[>#cartouche -60][♪taiko -3dB -60][!#name_bg shake,8,duration=300 +120]{碓氷|うすい}馬車鉄道。[silence:60]

*** side1
[>#subtitle]
@n: [silence:20][♪hooves -11dB to=3.2s fade=0,500]線路の上の客車を、[|]馬がパカパカ引っ張ります。[silence:100]
@: [manner:ちょっと得意げに、早口でオチをつけるように][>#spec -50]動力は、文字どおりの[>#spec.v][♪pon_hi -5dB][!#spec.v punch,1.15,duration=290 +480][♪"パフパフとラッパを鳴らす音" -2dB +480][♪hyoshigi -4dB +440 to=0.7s]「馬力」。[silence:150]
[<#ch1 cut-0]
transition panel,500,color=#D23F2A,skew=-14,dir=right,se=whoosh -4dB

*** ogai1
@n: [silence:250][>#ch2 -130][>#ogai_pop +80][♪pon -5dB +100]乗客には、あの文豪{・|、}[>#nameplate +280][♪pon_hi -5dB +280]森鴎外も。[silence:50]

*** scroll
@n: [manner:早口で、もったいぶるように][silence:30][>#paper -30][♪swish -10dB +20][>#youyaku +1340][♪pon_hi -4dB +1340][!#paper shake,4,duration=200 +1500]書き残した感想を、[|]ざっくりまとめると……[silence:160]
[<#subtitle]

*** rage
@ogai: [silence:100][♪impact -5dB -60 to=2.5s fade=0,800][♪"ハエがブーンと飛び回る音" -13dB +100 to=4.6s fade=300,800][>#brush1 +50]{臭い|におい}と揺れが、[>#brush2 +180][♪"ガーンとショックを受けた時の短い音" -7dB +180][!#rage_bg shake,15,duration=550 +220][!#brush2 shake,7,duration=400 +300]最悪！[silence:340]
@n: [manner:あきれ半分に、面白がって早口で][<#brush1 -50][<#brush2 -50]文豪、[>#gekido +140][♪taiko -2dB +140][!#rage_bg shake,12,duration=450 +160][♪hyoshigi -4dB +740 to=0.7s]大激怒。[silence:150]
[<#ch2 cut-0]
transition panel,500,color=#D23F2A,skew=-14,dir=right,se=whoosh -4dB

*** slow
[>#subtitle]
@n: [manner:あきれたように、ツッコミ口調で早口で][silence:250][>#ch3 -130][>#gauge -150][!#gauge.needle to,{rotation:-84, duration:0.7, ease:'power3.out'} +100][!#gauge.needle to,{rotation:-81.5, duration:0.16, yoyo:true, repeat:3, ease:'sine.inOut'} +800][♪"キッチンタイマーのチクタクという音" -3dB to=2.6s fade=0,400][>#slow_t +550][!#slow_t to,{scaleX:1.25, scaleY:0.8, duration:0.5, ease:'sine.inOut'} +950][!#slow_t to,{scaleX:1, scaleY:1, duration:0.5, ease:'sine.inOut'} +1450][♪"土の上をザクザク歩く足音" -14dB +1200 to=5.6s fade=400,800]しかも、あまりの遅さに、[|][<#land2 none -50][<#cart2 none -50][<#gauge none -50][<#slow_t none -50][>#walk_bg -50][>#walk_shade -50][>#zoku_t +100]途中で降りる乗客が続出。[silence:120]
[<#subtitle]
@pass: [<#zoku_t -100][>#bubble -20][♪"パシッと叩く打撃の音" +1dB +1530][!#bubble shake,9,duration=300 +1550][!#walk_bg shake,7,duration=300 +1550]歩いた方が早いわ！[silence:200]

*** overtake
[>#subtitle]
@n: [manner:哀愁をこめて、テンポよく][silence:100][>#ono1 +200][!#ono1 to,{x:133, duration:1.6, ease:'none'} +200][♪swish -9dB -150][>#ono2 +900]乗客に追い抜かれる[>#gloom][♪"チーンと低く鳴るりんの音" +4dB +50 to=1.8s][♪hyoshigi -4dB -50 to=0.7s]馬車。[silence:200]
[<#ch3 cut-0]
transition panel,500,color=#D23F2A,skew=-14,dir=right,se=whoosh -4dB

*** omen
subtitle "でも 本当の地獄は下り坂"
@n: [manner:急に声を落として、早口で怖い話をするように][silence:250][>#ch4 -130][<#music +120][♪impact -6dB to=2.5s fade=0,800][>#go[*] +200][!#go[1] shake,4,duration=2000 +500][!#go[2] shake,4,duration=2000 +750][!#go[3] shake,4,duration=2000 +1000][!#go[4] shake,4,duration=2000 +1250][>#omen1 +450]でも本当の地獄は、[>#omen2 +50][♪taiko -4dB +50][!#omen_bg shake,9,duration=400 +70]下り坂。[silence:160]

*** rush
bgm rush
@n: [manner:大慌てで、スポーツ実況のように興奮して][silence:80][!#rush_bg shake,8,duration=8100 -80][>#rush1 -60][♪"キーッと鳴る自転車のブレーキの音" -6dB -100][♪"ビューッと吹く強い風の音" -8dB +100][♪"ジェットコースターがゴーッと通過する音" -11dB +300 start=1.5s to=8.1s fade=500,1000][>#speed +200]ブレーキが効かず、客車は[|]猛スピードで、山を駆け下りる！[silence:20]
[<#subtitle]
@pass: [manner:ジェットコースターに乗ったように、悲鳴を上げて][<#rush1 -200][>#scream][♪"キャッという女性の短い悲鳴" -7dB +100][♪"ホラーの甲高い絶叫" -5dB +300 to=1.8s][!#scream shake,9,duration=1700 +300]うわあああああっ！
@ogai: [manner:恐怖のあまり、情けない悲鳴を上げて]ひいいいいいっ！
[>#subtitle]
subtitle "まさにジェットコースター状態"
@n: [<#scream +300][>#jc1 +380][♪jan -8dB +420][>#jc2 +450]まさに、ジェットコースター状態。[|]明治の人、[>#inochi +20][♪taiko -6dB +20]命がけです。[silence:180]
[<#rush]
[<#ch4 cut-0]
transition panel,500,color=#D23F2A,skew=-14,dir=right,se=whoosh -6dB

*** bridge
bgm music_b
@n: [silence:300][>#ch5 -180][>#tline +50][>#tline.bar +550][>#tline.mid +1100][♪whistle -14dB +1200 start=1.6s to=2.9s fade=0,400][>#tline.n2 +1850][>#tline.ev2 +1850]結局、わずか{5年|ごねん}足らずで[|]本格的な鉄道が開通し、[br]馬車鉄道は[>#intai][♪taiko -7dB]引退。[silence:260]
[<#subtitle]
@n: [manner:心をこめて、ねぎらうように、テンポよく][>#warm -300][<#tline -250][<#intai -250][>#otsukare +100]馬たち、本当におつかれさまでした。[silence:220]
[<#ch5 cut-0]
transition panel,500,color=#D23F2A,skew=-14,dir=right,se=whoosh -6dB

*** end
@n: [♪"チャンチャンと締めるワンポイントの音" -4dB +100][>#end_date +120][>#end_name +360][>#end_sub +500][>#end_horse +700][silence:1.9s]
```

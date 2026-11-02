# story · river-otter (hf 全力版の全量の写し — 日本の川にいたニホンカワウソが消えるまで・台本そのままの語りを 13 場面の全面写真と図の場面で) — canvas 1080x1920

見せる作り: 全編の質感 (黒 55% から明ける頭・周辺減光・grain・下の陰と明朝の字幕)・1 つの台詞の中で語ごとに溶けて替わる全面写真 (動く kb)・顔を出すカワウソの波紋・1 字ずつぼけから上がる題と中央から伸びる金の罫・「居ない版」を下に敷いて色を抜きカワウソだけを溶かす差分 (村・高知の川)・右から滑り込む番号つきの写真の札 3 枚 (前を薄め、語を足し、濃さを戻す)・回って止まる「1979 年」と着地の衝撃・シャッターの閃光と場所の札・金の輪・12 枚の格子が無作為な順に消える・記憶の写真に漂う塵・暖色の幕・金の光が流れる夕景で題の再掲と事実 2 行・暗転・音の層 (川の場の音 + 語に結んだ効果音 18 + 曲の沈み)

```design.txt
#v2
# 学ぶ作り: 場面ごとの全面写真を不透明な旧場面の上に溶かして替え、1 つの台詞の中でも語で写真を重ねて替える (川 → 顔を出すカワウソ・泳ぐ → 魚を追う → 村)
# 「いた → 消えた」を写真の差分で見せる: 同じ構図の「カワウソの居ない版」を基準画像から作って下に敷き、語で彩度を落とし上の版だけを溶かして消す (村・高知の川)
# 中盤は写真を離れて図の場面: 番号つきの写真の札 3 枚 (前を薄める)・回って止まる「1979 年」・12 枚の格子が無作為な順に消える・記憶の写真に漂う塵
# 全編の質感 (黒から明ける頭・周辺減光・grain) と下の陰 + 明朝の字幕、締めは金の光が流れる夕景で題を再掲し暗転
# hf 06 river-otter (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#0B0D0C
theme dark
palette ink=#F7F2E8 gold=#E9C27A hl=#F3C46A cream=#EFE6D4 stone=#CBBD9F mute=#E6D9BF dark=#0C0E0D moss=#1B201D night=#070807 bone=#E9E1CF mote=#FFF3D6 black=#000000 white=#FFFFFF
font "太字の古風で格調のある明朝体、筆の抑揚がある本文用"
fonts mb="最も太いブラックの太さの古風な明朝体、力強い見出し用" gb="太い角ゴシック体、くっきりした小見出し" gh="極太の角ゴシック体" gm="中くらいの太さの角ゴシック体"
sfx off
# hf の作り: 場面の間に黒 55% の幕 (理由 → 1979) と暖色の幕 (記憶 → あの日の川) を挟む
# hf の作り: 格子は同じ写真を別の切り出しで 2 度使う・塵は字幕帯の上も漂う・題の場面は 1.9 秒で学名と罫が出てすぐ去る・格子と字幕は切替の溶けの中で出始める
lint off=dip_black_frame,duplicate_media,caption_collision,entrance_in_transition,entrance_in_fadeout,flash_text
run g { color: $hl; font-family: mb }
p { color: $ink; out: none }
div { border: none; out: none }
img { out: none }
group { out: none }
shape { out: none }
icon { out: none }
# 写真は 1 枚ずつ根に置き、場面と 12 枚の格子で同じ絵を引き直す (content: @名)・居ない版は基準画像からの差分
image river = "[photo]A crystal-clear mountain river winding through a peaceful rural Japanese village in the 1950s. Smooth river stones visible under shallow turquoise water, a small wooden footbridge, thatched-roof farmhouses and rice terraces on the banks, forested green mountains behind, thin morning mist, soft sunlight. Vertical composition with the river leading from the bottom foreground into the distance; calm open sky in the upper third, river stones filling the whole bottom of the frame. Cinematic nature documentary photograph, natural light, subtle 35mm film grain, shallow depth of field. No text, no letters, no watermark, no border." aspect=9:16
image peek = "[photo]Close-up of an adorable Japanese river otter poking its head out of a clear mountain river, looking straight at the camera with big round dark eyes, wet glossy brown fur, pale cream throat, long whiskers with water droplets, tiny rounded ears, gentle ripples around its neck. Soft morning backlight, blurred green riverbank. The otter's face is centered slightly below the middle of the vertical frame. Cinematic nature documentary photograph, natural light, subtle 35mm film grain. No text, no letters, no watermark, no border." aspect=9:16
image portrait = "[photo]A Japanese river otter standing upright on a mossy boulder at the edge of a mountain stream, full body, sleek dark-brown fur, pale throat, thick tapering tail, looking alertly into the distance. Warm rim light outlining its fur, deep dark-green softly blurred forest background with plenty of empty dark space in the upper half of the vertical frame; the otter occupies the lower half. Cinematic nature documentary photograph, subtle 35mm film grain. No text, no letters, no watermark, no border." aspect=9:16
image swim = "[photo]Underwater photograph of a Japanese river otter swimming gracefully through a crystal-clear river, body stretched out, a trail of silver bubbles behind it, sunbeams streaming down through the surface, smooth pebbles on the riverbed, emerald-green water. Dynamic diagonal composition in a vertical frame. Cinematic nature documentary photograph, subtle film grain. No text, no letters, no watermark, no border." aspect=9:16
image fish = "[photo]A Japanese river otter chasing a small silver sweetfish (ayu) in shallow sparkling rapids, splashing water droplets frozen in mid-air, the otter's head lunging forward toward the fish, energetic action shot, sunlight glinting on the water. Vertical frame. Cinematic nature documentary photograph, subtle film grain. No text, no letters, no watermark, no border." aspect=9:16
image village = "[photo]Nostalgic scene of a 1950s Japanese riverside village: on stone steps leading down to a clear shallow river, a woman in simple traditional work clothes washes vegetables in a bamboo basket, two children in shorts play in the water with a small net, and in the lower foreground a Japanese river otter sits calmly on a flat rock watching them, all close together. Warm afternoon light, wooden houses and a persimmon tree in the background. Vertical frame. Cinematic documentary photograph, subtle film grain. No text, no letters, no watermark, no border." aspect=9:16
image kochi = "[photo]Faded 1970s color photograph with film grain and warm, washed-out tones: a quiet, gently flowing river in rural Kochi, Shikoku, Japan, at dusk, low forested hills, reeds on the banks. A single small Japanese river otter stands on a dark rock in the middle of the river, seen from a distance, silhouetted against the pale water. Lonely, elegiac mood. Vertical frame. No text, no watermark, no border." aspect=9:16
image kochi_empty = "[photo][ref:@kochi]Edit this photo: remove the otter standing on the rock in the middle of the river completely, leaving only the empty dark rock. Keep everything else exactly identical: framing, light, colors and film grain." aspect=9:16
image memory = "[photo]Still life: an old, faded square photograph of a river otter sitting by a river, with a white border and slightly curled, worn edges, lying on a weathered wooden table beside a pair of old round reading glasses, soft warm window light from the side, floating dust particles, shallow depth of field, nostalgic and melancholic. Vertical frame, the photograph centered. No text, no letters, no watermark." aspect=9:16
image golden = "[photo]A Japanese river otter swimming peacefully across a clear river at golden hour, only its head and back above the water, leaving soft V-shaped ripples that sparkle with warm golden light, backlit by the low sun, dreamy bokeh, hopeful and serene. Vertical frame, otter in the lower middle. Cinematic nature documentary photograph. No text, no letters, no watermark, no border." aspect=9:16
# 音は語に結ぶ: 水 (落ちる・飛び込む・跳ねる)・風・時計・衝撃・シャッターと打鍵・スウェル + 川の場の音
sound plop = "水面に小さく落ちるポチャンという水滴の音"
sound airy = "柔らかく長いフワッとした風切り音"
sound shimmer = "キラキラと輝く澄んだ高いシマー音"
sound dive = "動物が水に飛び込むドボンという音"
sound splash = "水しぶきがバシャッと跳ねる音"
sound swish = "乾いた短いシュッという風切り音"
sound wind = "寂しく吹き抜ける風の音"
sound low = "低く短いヒュッという風切り音"
sound clock = "時計の秒針がチクタク刻む音"
sound boom = "重低音のドーンと長く響く衝撃音"
sound shutter = "古いフィルムカメラのシャッター音"
sound typing = "タイプライターの打鍵音"
sound swell = "柔らかく盛り上がる幻想的なスウェル音"
sound river = "山あいの澄んだ川のせせらぎの環境音"
# 曲は声の下で 7 dB 沈み、「でも〜消えていきます」で更に 2.5 dB・「1979 年」の着地で 6 dB 一瞬あける (keys の秒は声の実尺から)
bgm#music(volume: 0dB; duck: -7; fade: 300,1000; keys: "0:0|13.9s:0|14.5s:-2.5|16.6s:-2.5|17.4s:0|26.25s:0|26.4s:-6|27.0s:-6|27.6s:0") 静かで郷愁を誘うゆっくりしたピアノのソロ、切なく温かい旋律、自然ドキュメンタリーの語り向け
# 字幕: 明朝の白文字 + 濃い落ち影 (板なし)・画面の下 1/5 の上に置く・強調の語は金の極太 {g}
subtitle(left: 60px; bottom: 392px; width: 960px; font-size: 60px; line-height: 1.42; letter-spacing: 0.04em; color: #FBF7EE; background: none; text-shadow: 0px 3px 10px #000000E6; unit: sentence; lead: 0ms; in: {y:12, opacity:0, duration:0.16, ease:'power2.out'}; out: {opacity:0, duration:0.14, ease:'power1.in'})
# 写真の下の陰 (字幕の地・下 760px で 78% まで) と上の陰 (題の地)
def shade_b() = div(left: 0px; top: 1160px; width: 1080px; height: 760px; background: linear(#06080700,#0608076B@55%,#060807C7,bottom); border-radius: 24px; in: none)
def shade_t() = div(left: 0px; top: 0px; width: 1080px; height: 640px; background: linear(#060807B8,#06080759@50%,#06080700,bottom); border-radius: 24px; in: none)
# 消えた理由の札: 写真 (ゆっくり寄る・左からの暗幕 scrim) + 金の番号 + 太いゴシックの題。右から滑り込む
def card(n, t, pic) = div(left: 70px; width: 940px; height: 290px; border-radius: 18px; background: $dark; border: 2px solid #FFFFFF1F; box-shadow: 0px 18px 40px #00000080; in: {x:140, opacity:0, duration:0.5, ease:'power3.out'})
  img#ph(inset: 0; content: {pic}; filter: saturate(0.85) contrast(1.05) brightness(1.18); scrim: left,0.86; main: kb {scale: [1, 1.12]})
  p#num(left: 40px; top: 30px; font-size: 92px; font-family: mb; color: $gold; line-height: 1; content: {n})
  p#lab(left: 44px; bottom: 40px; font-size: 52px; font-family: gh; letter-spacing: 0.04em; white-space: nowrap; content: {t})
# 全編の質感: 周辺減光 (中央 55% は素通し) + grain (最前面)
veil#vignette(background: radial(#00000000@55%,#0000008C@100%,50%,46%); z-index: front; in: none)
veil#grain(grain: 0.07; color: #00000000; z-index: front; in: none; main: noise {x: 6, y: 6, period: 0.083})

# 開幕: 黒 55% から明ける川の村 (寄りながら上へ) → 「この」で顔を出すカワウソが溶けて重なり、首もとに波紋が 2 重
section#open
img#river(inset: 0; content: @river; subject: center 90%; main: keys(at=0 scale=1 | at=1 scale=1.09 y=-24 ease=none),window=0,3400,forwards)
img#peek(inset: 0; content: @peek; main: kb {scale: [1.16, 1], ease:'power2.out'}; in: {opacity:0, duration:0.28, ease:'power2.out'})
shape#ripple(left: 330px; top: 1090px; width: 420px; height: 150px; border-radius: 50%; background: none; border: 3px solid #FFFFFF00; overlap: peek)
shade_b#open_shade
veil#intro(color: $black; opacity: 0.55; z-index: curtain; in: none; out: none)

# 題: 立つカワウソの写真の上に、小見出し → 1 字ずつぼけから上がる名 → 金の罫が中央から伸びる → 学名
section#title
img#portrait(inset: 0; content: @portrait; main: kb {scale: [1.12, 1], ease:'power2.out'})
shade_t#title_shade
group#ttl(out: {y:-24, opacity:0, duration:0.25, ease:'power1.in'})
  p#kicker(cx: 540px; top: 170px; font-size: 30px; font-family: gb; letter-spacing: 0.5em; color: $gold; in: {opacity:0, duration:0.4}) 日本の川の住人
  p#name(cx: 540px; top: 237px; font-size: 118px; font-family: mb; letter-spacing: 0.06em; line-height: 1.1; white-space: nowrap; text-shadow: 0px 6px 30px #00000099; in: {y:40, opacity:0, blur:8, duration:0.5, ease:'power3.out', stagger:0.06}) ニホンカワウソ
  shape#rule(left: 280px; top: 387px; width: 520px; height: 3px; path: rect; background: linear(#E9C27A00,#E9C27A,#E9C27A00,90); in: {scaleX:0, duration:0.6, ease:'power2.out'})
  p#sci(cx: 540px; top: 408px; font-size: 36px; font-style: italic; letter-spacing: 0.14em; color: $cream; in: {opacity:0, duration:0.5}) Lutra lutra nippon

# 暮らし: 泳ぐ (斜めに流れる) → 魚を追う (寄る) → 人のそばの村。「でも」で村の色が抜け、「その姿は」でカワウソだけが溶けて消える
section#life
img#swim(inset: 0; content: @swim; main: keys(at=0 x=-31 y=33 scale=1.12 | at=1 x=17 y=-16 scale=1.12 ease=none),window=0,1340,forwards)
img#fish(inset: 0; content: @fish; main: kb {scale: [1.04, 1.17], ease:'power1.out'}; in: {opacity:0, duration:0.08})
# 村は 2 枚 (下 = 居ない版・上 = 居る版) を群で一緒に寄せる
group#village(main: keys(at=0 scale=1 | at=1 scale=1.16 ease=sine.inOut),window=0,6000,forwards; transform-origin: 21% 71%; in: {opacity:0, duration:0.35, ease:'power1.out'})
  img#empty(inset: 0; main: none) [photo][ref:@village]Edit this photo: remove the river otter sitting on the flat rock in the foreground completely, leaving only the empty wet rock and water where it was. Keep everything else exactly identical: the same people, framing, lighting and colors.
  img#otter(inset: 0; content: @village; main: none)
shade_b#life_shade

# 消えた理由: 暗い地に見出し・語ごとに右から写真の札 (01 → 02 → 03)・新しい札が出ると前の札を薄め、「餌」で 03 に語を足し、言い終わりで濃さを戻す
section#causes
div#c_bg(inset: 0; background: radial($moss,$dark@70%,50%,30%); border-radius: 24px; in: none)
group#c_head(left: 70px; top: 176px; in: {y:18, opacity:0, duration:0.45, ease:'power2.out'})
  p#k(left: 0px; top: 0px; font-size: 28px; font-family: gb; letter-spacing: 0.42em; color: $gold) REASONS
  p#h(left: 0px; top: 54px; font-size: 78px; font-family: mb; letter-spacing: 0.06em) 消えた理由
card#card1(top: 372px; n: "01"; t: "毛皮目的の乱獲"; pic: "[photo]Early Showa-era Japan (1930s): several dried brown otter pelts hanging in a row on the wooden wall of a dim rural storehouse, a rusty iron trap and a coil of straw rope on the earthen floor, a shaft of dusty light through a slatted window. Somber documentary mood. No people, no blood. Faded vintage color photograph, washed-out colors, visible film grain. No text, no letters, no watermark.")
card#card2(top: 690px; n: "02"; t: "河川の開発"; pic: "[photo]1960s Japan: a river being straightened and lined with gray concrete embankments, a yellow excavator and workers in helmets in the distance, bare concrete walls replacing natural grassy banks, overcast sky. Faded vintage color photograph, washed-out colors, visible film grain. No text, no letters, no watermark.")
card#card3(top: 1008px; n: "03"; t: "水質汚染"; pic: "[photo]1970s Japan: a polluted river with murky brownish water and patches of white foam, factory smokestacks emitting gray smoke in the background, a few dead fish floating near the concrete bank, gloomy overcast light. Faded vintage color photograph, washed-out colors, visible film grain. No text, no letters, no watermark.")
  p#more(left: .lab.right; bottom: 40px; font-size: 52px; font-family: gh; letter-spacing: 0.04em; white-space: nowrap; in: {x:20, opacity:0, duration:0.4, ease:'power2.out'}) ・餌の減少

# 1979: ほぼ黒の地に居ない川の写真を 2 割で敷き、「そして」→ 1920 から回って 1979 に止まる年 (着地で締まる) → 金の「年」→ 昭和54年
section#year
div#y_bg(inset: 0; background: $night; border-radius: 24px; in: none)
img#y_photo(inset: 0; content: @kochi_empty; opacity: 0.2; filter: sepia(1) brightness(0.7); main: kb {scale: [1.18, 1.08]})
p#soshite(cx: 540px; top: 640px; font-size: 58px; letter-spacing: 0.3em; color: $bone; in: {y:14, opacity:0, duration:0.45, ease:'power2.out'}) そして
p#year(left: 99px; top: 760px; font-size: 300px; font-family: mb; line-height: 1; text-shadow: 0px 10px 50px #00000099; in: {scale:0.96, opacity:0, duration:0.4, ease:'power2.out'}) [count:1979 start=1920 roll ms=0,0,1380,1460 laps=0,0,0,4 delay=320 ease=ease_in_out]
p#nen(left: year.right+18; top: 904px; font-size: 120px; line-height: 1.3; color: $gold; in: {x:-16, opacity:0, duration:0.35, ease:'power2.out'}) 年
p#era(cx: 540px; top: 1110px; font-size: 40px; font-family: gb; letter-spacing: 0.5em; color: $stone; in: {opacity:0, duration:0.4}) 昭和54年

# 高知: 白い閃光 (シャッター) で居る版の夕景へ・左上に場所の札・名を言う語で金の輪が締まり、「姿を見た人は」でカワウソだけが溶けて消える
section#kochi
group#kochi(main: keys(at=0 scale=1.03 | at=1 scale=1.16 ease=sine.inOut),window=0,7100,forwards; transform-origin: 47.6% 49%)
  img#empty(inset: 0; content: @kochi_empty; main: none)
  img#otter(inset: 0; content: @kochi; main: none)
  shape#focus(left: 430px; top: 892px; width: 190px; height: 190px; border-radius: 50%; background: none; border: 3px solid $hl; box-shadow: 0px 0px 24px #F3C46A8C; in: {scale:1.6, opacity:0, duration:0.5, ease:'power3.out'}; out: {opacity:0, duration:0.9})
shade_b#kochi_shade
# 場所の札: 金の縦棒 + 半透明の黒の板 (右だけ角丸) + ピン + 地名 / 年
div#loc(left: 70px; top: 200px; width: 600px; height: 165px; background: #080A098C; border-radius: 0,9,9,0; in: {x:-24, opacity:0, duration:0.45, ease:'power2.out'})
  div#bar(left: 0px; top: 0px; width: 4px; height: 165px; background: $gold)
  icon#pin(left: 26px; top: 32px; font-size: 38px; name: map-pin; weight: fill; color: $gold)
  p#l1(left: 74px; top: 22px; font-size: 46px; font-family: gh; letter-spacing: 0.06em; white-space: nowrap) 高知県 須崎市・新荘川
  p#l2(left: 26px; top: 98px; font-size: 32px; font-family: gb; letter-spacing: 0.12em; color: $gold; white-space: nowrap) 1979年　最後の確認
veil#flash(color: $white; opacity: 0.85; z-index: curtain; in: none)

# 日本中 → 数十年: これまでの写真を切り出した 12 枚の格子が弾んで並び、「たった」から無作為な順に 1 枚ずつ消える → 「私たちの」で古い写真の静物が溶けて重なり、塵が漂う
section#grid
div#g_bg(inset: 0; background: $dark; border-radius: 24px; in: none)
group#grid(main: keys(at=0 scale=1 | at=1 scale=1.05 ease=none),window=0,4470,forwards)
  img#tile(left: "69;266;463;69;266;463;69;266;463;69;266;463"; top: "157;157;157;354;354;354;551;551;551;748;748;748"; width: 282px; height: 282px; border-radius: 14px; box-shadow: 0px 10px 26px #00000080; main: none; object-fit: cover; object-position: "50% 40%;52% 45%;60% 52%;42% 30%;8% 74%;52% 58%;47% 50%;50% 46%;72% 58%;52% 58%;50% 30%;34% 28%"; zoom: "140%;170%;150%;150%;300%;220%;300%;230%;230%;210%;260%;230%"; in: {opacity:0, scale:0.9, duration:0.35, ease:'back.out(1.6)', stagger:{each:0.075}}; out: {opacity:0, scale:0.94, duration:0.38, ease:'power1.in'}) ×12 @peek;@portrait;@swim;@fish;@village;@golden;@kochi;@peek;@swim;@memory;@portrait;@fish
img#memory(inset: 0; content: @memory; main: kb {scale: [1, 1.13], focus: ['52% 59%', '52% 59%'], ease:'sine.inOut'}; in: {opacity:0, duration:0.5})
# 塵 16 粒 (粒ごとの位置・大きさ・濃さ・同じ向きにゆっくり上へ漂う)
shape#dust(left: "389;613;481;405;144;447;350;500;441;245;303;434;532;357;295;100"; top: "924;651;463;763;638;886;991;777;376;743;634;493;391;709;851;381"; width: "6;4.7;3.3;6;4;2.7;4.7;3.3;2.7;2.7;6;4;4.7;2.7;3.3;6"; height: "6;4.7;3.3;6;4;2.7;4.7;3.3;2.7;2.7;6;4;4.7;2.7;3.3;6"; border-radius: 50%; background: $mote; box-shadow: 0px 0px 4px 2px #FFF3D680; opacity: "0.55;0.43;0.53;0.53;0.30;0.46;0.48;0.47;0.26;0.52;0.54;0.42;0.48;0.50;0.43;0.52"; in: {opacity:0, duration:0.5}; main: ramp {x: 30, y: -140}) ×16
shade_b#memory_shade(in: {opacity:0, duration:0.5})

# あの日の川: 開幕の川の夕景版 (引き) に金の光が流れ、「そこには」で泳ぐカワウソが溶けて重なり波紋が 2 重 → 上の陰の上に題の再掲と 2 行の事実 → 暗転
section#return
img#river_golden(inset: 0; main: kb {scale: [1.12, 1], ease:'power1.out'}) [photo][ref:@river]Edit this photo: the very same river village scene at golden hour just before sunset, warm golden sunlight, sparkling water surface, long soft shadows, gentle dreamy haze. Keep the composition, river, bridge and houses exactly the same.
img#swimmer(inset: 0; content: @golden; main: kb {scale: [1, 1.11], focus: ['51% 57%', '51% 57%']}; in: {opacity:0, duration:0.8, ease:'sine.inOut'})
shape#ripple2(left: 400px; top: 1110px; width: 300px; height: 96px; border-radius: 50%; background: none; border: 3px solid #FFFFFF00; overlap: swimmer)
shade_b#return_shade
shade_t#end_shade(height: 900px; in: {opacity:0, duration:1})
# 金の光 (画面の外から入る大きな丸い光を screen で重ね、ゆっくり流して消す)
# hf の作り: 光の丸は画面の左上の外まで大きく取る (check の offscreen はこの 1 件 — 意図した画面の外は `bleed`)
div#leak.bleed(left: -140px; top: -120px; width: 1300px; height: 1300px; border-radius: 1498px; background: radial(#FFBE6E8C,#FF96462E@45%,#FF964600@70%); mix-blend-mode: screen; opacity: 0.9; in: {x:-160, y:-80, opacity:0, duration:3, ease:'sine.inOut'})
p#e1(cx: 540px; cy: 327px; font-size: 104px; font-family: mb; letter-spacing: 0.08em; text-shadow: 0px 6px 30px #0000008C; in: {y:24, opacity:0, blur:6, duration:0.9, ease:'power2.out'}) ニホンカワウソ
p#e2(cx: 540px; cy: 456px; font-size: 38px; font-family: gb; letter-spacing: 0.08em; in: {y:14, opacity:0, duration:0.6, ease:'power2.out'}) 1979年を最後に、確認されていない
p#e3(cx: 540px; cy: 525px; font-size: 30px; font-family: gm; letter-spacing: 0.06em; color: $mute; in: {y:14, opacity:0, duration:0.6, ease:'power2.out'}) 2012年　環境省レッドリストで「絶滅」に
```

```timeline.txt
#v2
cast n = "落ち着いた低めの男性のプロのナレーター、静かで情感のあるドキュメンタリーの語り"
transition = dissolve {duration: .3, overlap: .3, ease: 'power2.out'}

*** open
[>#subtitle]
bgm music
se river -10dB to=14.2s fade=800ms,1800ms
@n: [silence:500ms][!#intro to,{opacity:0, duration:0.4, ease:'power1.out'} -500ms]昔、[<#intro]日本の川には……[|][>#peek -20ms][♪plop -5dB +20ms][!#ripple ping,#FFFFFFD9 {count: 2, interval: .37, duration: 1.3, scale: [.35, 1.5]} +70ms]この{g}可愛い動物{/}が[br]普通にいたんです。
transition dissolve {duration: .3, overlap: .3}

*** title
[<#subtitle]
@n: [silence:150ms][♪airy -6dB -200ms to=1.6s fade=0ms,400ms][>#ttl.kicker -50ms][♪shimmer -5dB][>#ttl.name +10ms][>#ttl.rule +350ms][>#ttl.sci +500ms][<#ttl cut-0ms]ニホンカワウソ。[silence:0.4s]
transition dissolve {duration: .14, overlap: .14}

*** life
[>#subtitle]
@n: [♪dive -3dB -90ms to=1.6s fade=0ms,500ms]川を泳ぎ、[>#fish -50ms][♪splash -3dB -30ms][<#swim +100ms]魚を追いかけ、[|][>#village -70ms][♪swish -6dB -250ms][<#fish +350ms]日本人のすぐそばで[br]暮らしていました。
@: [!#village.otter to,{filter:'saturate(.28) brightness(.72)', duration:4.4}][!#village.empty to,{filter:'saturate(.28) brightness(.72)', duration:4.4}]でも、いつからか、[|][!#village.otter to,{opacity:0, duration:2.3, ease:'sine.inOut'} +70ms][♪wind -6dB +120ms to=3.5s fade=0ms,800ms]その姿は[br]少しずつ消えていきます。
transition dissolve {duration: .32, overlap: .32}

*** causes
@n: [silence:150ms][>#c_head -130ms][>#card1][♪low -4dB -220ms]毛皮をとるために[br]捕まえられ、[|][>#card2][!#card1 to,{opacity:0.5, duration:0.4} +50ms][♪low -4dB -220ms]川は開発され、[|][>#card3][!#card2 to,{opacity:0.5, duration:0.4} +50ms][♪low -4dB -220ms]水が汚れ、[br][>#card3.more]餌となる魚も[!#card1 to,{opacity:0.85, duration:0.5} +170ms][!#card2 to,{opacity:0.85, duration:0.5} +170ms]減っていきました。
transition dip {duration: .6, level: .55}

*** year
[<#subtitle]
@n: [silence:300ms][♪clock -8dB -250ms to=2.45s fade=0ms,500ms][>#soshite -30ms]そして[>#year -370ms]1979[!#year settle {scale: 1.07, duration: .6} -110ms][>#nen -30ms][>#era +130ms][♪boom +3dB -210ms to=4.6s fade=0ms,1800ms]年。[silence:0.3s]
transition cut

*** kochi
[>#subtitle]
@n: [silence:200ms][>#flash -200ms][!#flash to,{opacity:0, duration:0.42, ease:'power2.out'} -140ms][♪shutter -3dB -200ms to=1.4s][>#loc +200ms][♪typing -6dB +200ms to=1.1s]{g}高知県{/}で最後に確認された[br][>#kochi.focus +40ms]ニホンカワウソを最後に、[|][!#kochi.otter to,{opacity:0, duration:1.7, ease:'sine.inOut'} +70ms][♪wind -5dB +20ms to=3.5s fade=0ms,1000ms]姿を見た人は[br][<#kochi.focus +150ms]いなくなりました。

*** grid
@n: [silence:150ms][>#grid.tile[*] -30ms]かつては日本中にいた動物が、[|][♪clock -8dB -80ms to=1.6s fade=0ms,500ms][<#grid.tile[8] -30ms][<#grid.tile[12] +80ms][<#grid.tile[4] +190ms][<#grid.tile[11] +300ms][<#grid.tile[9] +410ms][<#grid.tile[5] +520ms][<#grid.tile[10] +630ms][<#grid.tile[2] +740ms][<#grid.tile[1] +850ms][<#grid.tile[7] +960ms][<#grid.tile[3] +1070ms][<#grid.tile[6] +1180ms]たった{g}数十年{/}で、[|][>#memory -130ms][>#dust -130ms][>#memory_shade -130ms]私たちの{g}記憶の中だけ{/}の[br]存在になったので[♪swell -5dB +380ms to=3.4s fade=0ms,1200ms]す。
transition dip {duration: 1, color: #FFF1D8, level: .55}

*** return
se river -10dB to=12s fade=1800ms,1400ms
@n: もし、あの日の川に[br]戻れたなら――[|][!#leak to,{x:100, y:60, opacity:0.45, duration:5, ease:'sine.inOut'} -580ms][>#swimmer -130ms][>#ripple2 -130ms]そこには今も、[♪plop -8dB +70ms][!#ripple2 ping,#FFFFFFB3 {count: 2, interval: .7, duration: 1.8, scale: [.4, 1.7]} +70ms]カワウソが[br]泳いでいるのでしょう[>#end_shade +430ms][>#e1 +580ms][>#e2 +1280ms][>#e3 +1780ms][!#leak to,{opacity:0, duration:1.4} +1730ms]か。[silence:5.0s]
fade out,1000ms
```

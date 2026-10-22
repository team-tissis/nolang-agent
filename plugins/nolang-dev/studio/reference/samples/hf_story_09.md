# story · soma-nomaoi (hf の作りを draft src に写した物 — 相馬野馬追の紹介) — canvas 1920x1080

見せる作り: 黒からの開幕と全編の周辺減光・grain・字幕の下の陰・漂う塵・場面ごと揺れる写真と閃光 + 太鼓の切替・数えて上がる「約 400 騎」・朱の筆の帯に 1 字ずつ着地する題字 (締めで同じ組をもう一度)・墨絵の縦書きと朱の落款・押印で落ちて揺れる判子・中央から定位置へ縮む見出しと語ごとに出る札 3 枚・場面の札 (区分 > 名称 > 補足) の def・語で寄る絵・観覧の心得の板・エンドカード・音の層 (法螺貝・太鼓・蹄・歓声・花火と曲のつなぎ)

```design.txt
#v2
# この見本から学ぶ作り: 全編に敷く質感の層 (黒からの開幕・周辺減光・grain・字幕の下の陰) + 場面ごとの全面の絵替え (実写 ⇄ 墨絵・kb・揺れ・塵)
# 題字は朱の筆の帯に 1 字ずつ着地し、締めで同じ組をもう一度・墨絵の上は縦書き + 落款・文化財は押印の判子・場面の札 (区分 > 名称 > 補足) は def に 1 回
# 語と同時の主役 (数えて上がる 400 騎・判子・中央から定位置へ縮む見出しと札 3 枚・心得 2 つ・絵の寄り)・大きな文字は切替の前に fade で消す
# 座標は hf (1920x1080) の 2/3。主色 朱・金 / 見出し しっぽり明朝 ExtraBold・題字 佑字 朴・本文 ZEN角ゴシックNew
canvas 1920x1080 bg=#000000
theme dark
palette ink=#16120F shu=#B3261E gold=#D8B26A white=#FBF8F2 cream=#F3E9D6 ink2=#2C241D sepia=#5A4B3C gray=#D9D2C5 dark=#1A1410 pale=#E9E1D2
font "ZEN角ゴシックNew Medium"
fonts k="ZEN角ゴシックNew Bold" s="しっぽり明朝 ExtraBold" sm="しっぽり明朝 Medium" y="佑字 朴 Regular"
# hf の作り: 場面の札と判子は場面の頭 / 主題の語で出し、札の語 (行列・指定) は台詞が後から言う
lint off=spoiler
# 周辺減光 (端で 4 割の黒) の上の墨の字は明るい和紙の絵の上で読める — lint は幕の色だけを見て濃さを見ない
lint off=low_contrast
sfx off
master lufs=-15 tp=-1
run g { color: $gold }
run r { color: $shu }
run dn { color: #FFFFFF; font-size: 46px; font-family: s }
run sm { font-size: 32px; font-family: k; color: #D8D0C2 }
# 退場は書いた物だけ (型の既定の drift を切る)・群と板の out は子に継がれないので子に書く
p { color: $white; out: none }
div { out: none }
group { out: none }
img { out: none }
shape { out: none }
sound hora = "合戦の始まりを告げる法螺貝、ブォーと低く長く響く"
sound taiko = "大太鼓の一打、ドーンと長く響く"
sound taiko2 = "低く重い和太鼓の連打、ドドン"
sound wadaiko = "場面転換の和太鼓の一打、ドン"
sound kodaiko = "小太鼓の乾いた一打、ポン"
sound odeza = "威厳のある和太鼓の重い一打、ドーン"
sound gallop = "草地を駆ける馬の蹄、パカラッ"
sound horse = "硬い地面を進む馬の蹄、パカパカ"
sound neigh = "馬のいななき、ヒヒーン"
sound wind = "鋭い風切り音、ヒューン"
sound swing = "滑らかな振りの風切り音、シュッ"
sound flag = "布の旗がはためく音、パタパタ"
sound crowd = "イベントの大歓声と拍手"
sound cheer = "スタジアムの大群衆の歓声と指笛"
sound firework = "打ち上げ花火、ヒューと上がってドーンと開きパチパチ"
sound hanabiho = "花火砲、遠くで重くドーンと響く"
image dawn = "[photo]Wide cinematic shot at dawn on a vast grassy plain in Fukushima, Japan. Silhouettes of a long line of mounted samurai warriors in full armor, each with a tall rectangular banner (sashimono) on the back, standing still against a misty golden sunrise. Soft haze, strong rim light, dust particles glowing in the air, quiet tension before the festival begins. Photorealistic cinematic documentary photograph, open sky in the upper half. No text, no letters, no watermark." aspect=16:9
image sky = "[photo]Wide photograph of a huge grassy festival field in Japan with hundreds of mounted samurai riders in armor with colorful banners gathered below, while high in the blue sky several puffs of white firework smoke have burst and small sacred flags flutter slowly down toward the riders. Dramatic perspective, bright afternoon light, epic scale. Photorealistic documentary photograph. No readable text, no letters." aspect=16:9
image noma = "[photo]Documentary photograph of a Shinto horse ritual in Japan: men dressed entirely in white robes and white headbands catching a bare-backed horse with their bare hands inside a bamboo-fenced enclosure in a shrine precinct, the horse lifting its head, onlookers behind the bamboo fence, tall green trees, soft morning light. Photorealistic, respectful editorial photograph. No readable text, no letters." aspect=16:9
image procession = "[photo]Photograph of a grand festival procession in Japan: mounted samurai in full armor riding slowly in a long line along a wide street of a small Japanese town, each rider with a tall colorful banner on the back, a golden portable shrine carried in the procession, spectators lining both sides of the street, fresh green roadside trees, bright late-spring morning light, telephoto compression showing many riders. Photorealistic documentary photograph. No readable text, no signs, no letters." aspect=16:9
image brush = "[transparent]A single bold horizontal brush stroke of black sumi ink, thick and powerful in the middle with dry-brush streaks and small ink splatters at both ends, isolated on a fully transparent background, nothing else in the image." aspect=8:3
bgm#music(volume: 8dB; duck: -9.5; duck_attack: 120; duck_release: 450; duck_lead: 250; jump: at_cut:noma>180.9s; xfade: 1000; keys: "end-5.8s:0|end-4.3s:+5"; fade: 0,900) 温かく力強い和風の管弦楽、和太鼓と笛と弦、厳かで郷愁のある時代劇の曲
subtitle(font-size: 46px; bottom: 66px; width: 1600px; background: none; color: #FFFFFF; letter-spacing: 0.04em; text-shadow: 0px 2px 10px #000000E6; unit: sentence; in: {y:8, opacity:0, duration:0.16, ease:'power1.out'}; lead: 80; tail: 250)
# 左からの陰 (写真の上の札の地)
def shade() = div(inset: 0; background: linear(#0000009E,#00000040@34%,#00000000@55%,right))
# 場面の札 (区分 > 名称 > 補足): 朱の縦の罫が上から伸び、区分が左から・名称が左から拭われ・補足がせり上がり、切替の前に揃って消える
def scene_label(when, what, where) = group(left: 112px; top: 92px)
  shape#bar(left: 0px; top: 6px; width: 8px; height: 218px; background: $shu; in: wipe {dir: 'down', duration: 0.4, ease: 'power3.out'}; out: fade {duration: 0.35})
  p#when(left: 34px; top: 0px; content: {when}; font-size: 30px; font-family: k; color: $gold; letter-spacing: 0.22em; text-shadow: 0px 2px 10px #000000B3; in: {x:-24, opacity:0, duration:0.45, ease:'power2.out', delay:0.08}; out: fade {duration: 0.35})
  p#what(left: 34px; top: 54px; content: {what}; font-size: 104px; font-family: s; letter-spacing: 0.06em; text-shadow: 0px 4px 24px #000000A6; in: wipe {dir: 'right', duration: 0.7, ease: 'power2.inOut', delay: 0.15}; out: fade {duration: 0.35})
  p#where(left: 34px; top: 186px; content: {where}; font-size: 32px; color: #F1ECE2; letter-spacing: 0.08em; text-shadow: 0px 2px 12px #000000CC; in: {y:12, opacity:0, duration:0.5, ease:'power2.out', delay:0.45}; out: fade {duration: 0.35})
# 全編の質感: 周辺減光 (写真の上・文字と札の下) + 動く grain (最前面)
veil#vignette(background: radial(#00000000@55%,#0000006B@100%); in: none)
veil#grain(grain: 0.07; color: #00000000; z-index: front; in: none; main: noise {x: 6, y: 6, period: 0.1})

# 開幕: 黒から明ける夜明けの騎馬の列に塵が漂い、法螺貝で語りが始まる
section#open
img#open_photo(inset: 0; content: @dawn; main: kb {scale: [1.04, 1.17], focus: ['37% 22%', '59% 55%'], ease:'sine.inOut'})
# 塵 22 粒 (粒ごとの位置・大きさ・濃さと、場面の尺で漂う向き)
shape#open_dust.ellipse.bleed(left: "193;48;286;1099;745;871;895;1255;855;742;898;29;317;1049;193;5;791;502;208;33;157;439"; top: "453;319;438;231;445;315;203;126;522;333;450;337;293;583;161;310;468;298;262;589;574;216"; width: "3.3;4;2.5;2.2;2.7;2.8;5.2;3.1;2.1;4.4;2.3;4.7;2.5;5.5;5.8;3.1;4.1;5.2;2.9;3.5;3.5;2.4"; height: "3.3;4;2.5;2.2;2.7;2.8;5.2;3.1;2.1;4.4;2.3;4.7;2.5;5.5;5.8;3.1;4.1;5.2;2.9;3.5;3.5;2.4"; background: #FFF0D6F2; box-shadow: 0px 0px 6px 2px #FFE2B48C; opacity: "0.38;0.21;0.39;0.22;0.38;0.40;0.37;0.46;0.50;0.53;0.48;0.22;0.21;0.33;0.27;0.39;0.51;0.41;0.18;0.23;0.35;0.24"; in: none; main: ramp {x: '-3;7;3;-12;-53;12;83;-38;-11;16;-16;-54;11;-4;17;96;67;-54;-39;-22;17;-60', y: '-44;5;14;4;-44;-29;-1;-17;-4;-5;-23;1;-13;9;-10;-4;8;-44;-42;-26;-43;13'}) ×22
# 字幕の下の陰 (最初の台詞の手前で出て、エンドカードで消える)
veil#sub_shade.sticky(background: linear(#00000000@72%,#0000009E,bottom); z-index: front; in: fade {duration: 0.6}; out: fade {duration: 0.9})

# 突進: 閃光と太鼓で切り替わり、場面ごと揺れる写真の上に「約 400 騎」が数えて上がる
section#charge
veil#charge_fl(color: #FFFFFF; opacity: 0.7; z-index: curtain; in: none)
group#charge_shake(left: 0px; top: 0px; width: 1920px; height: 1080px; main: noise {x: 4, y: 4, period: 0.07})
img#charge_shake.photo(inset: 0; main: kb {scale: [1.06, 1.24], focus: ['', '46% 43%'], ease:'power1.in'}) [photo]Low-angle dynamic photograph of a group of Japanese samurai riders in colorful traditional armor and helmets galloping toward the camera across a green grass field, tall colorful banners with simple geometric crest designs fluttering on their backs, horses with ornate traditional Japanese tack, clods of earth and dust flying, bright late-morning sunlight, slight motion blur on the hooves. Photorealistic sports documentary photograph with a telephoto lens. No readable text, no letters.
shade#charge_shade
group#riders(left: 118px; top: 570px; in: {y:24, opacity:0, duration:0.4, ease:'power2.out'})
  p#cap(left: 6px; top: 0px; font-size: 32px; font-family: k; color: $gold; letter-spacing: 0.24em; out: fade {duration: 0.25}) 甲冑の騎馬武者
  p#pre(left: 0px; top: 186px; overlap: riders.num; font-size: 64px; font-family: s; text-shadow: 0px 6px 28px #00000099; out: fade {duration: 0.25}) 約
  p#num(left: 72px; top: 46px; font-size: 236px; font-family: s; letter-spacing: -0.01em; palt: off; text-shadow: 0px 6px 28px #00000099; out: fade {duration: 0.25}) [count:400 roll ms=1150,1000,850]
  p#unit(left: 495px; top: 150px; overlap: riders.num; font-size: 120px; font-family: s; text-shadow: 0px 6px 28px #00000099; out: fade {duration: 0.25}) 騎

# 題: 鎧の武者の寄りが暗く沈み、閃光と太鼓で題字が着地・英字は字間が締まり、地名がせり上がる
section#title
veil#title_fl(color: #FFFFFF; opacity: 0.38; z-index: curtain; in: none)
img#title_photo(inset: 0; main: kb {scale: [1.16, 1.02], focus: '58% 47%', ease:'power2.out'}) [photo]Close-up portrait of a mounted samurai warrior at a traditional festival in Japan: ornate black lacquered armor with dark blue silk lacing, kabuto helmet with a golden crescent crest, determined eyes, gloved hands on the reins, a tall black banner fluttering behind him showing a simple white crest of one large circle surrounded by eight smaller circles, shallow depth of field with bokeh of other riders and colorful flags in the background, warm early-summer light. Photorealistic editorial photograph. No text, no letters, no flower crests.
veil#title_dim(opacity: 0.52; color: #000000; in: fade {duration: 0.5, ease: 'power2.out'})
# 題字: 朱に染めた筆の帯が左から拭われ、1 字ずつ拡大とぼかしから着地 (GSAP の stagger:.07 を 1 字ずつ 70 ms で)
group#logo(left: 0px; top: 0px; width: 1920px; height: 1080px)
  img#brush(left: 180px; top: 226px; width: 1560px; height: 585px; content: @brush; look: #B3261E; in: wipe {dir: 'right', duration: 0.45, ease: 'power2.inOut'}; out: fade {duration: 0.5})
  p#jp(cx: 960px; cy: 471px; font-size: 236px; font-family: y; letter-spacing: 0.06em; text-shadow: 0px 6px 30px #00000073; in: {scale: 1.5, blur: 12, opacity: 0, duration: 0.5, ease: 'power3.out', delay: 0.22, stagger: 0.07, unit: 'grapheme'}; out: fade {duration: 0.5}) 相馬野馬追
  p#en(cx: 960px; cy: 648px; font-size: 34px; font-family: k; letter-spacing: 0.62em; in: {letter_spacing:0.48, opacity:0, duration:1, ease:'power2.out', delay:0.67}; out: fade {duration: 0.5}) SOMA NOMAOI
p#region(cx: 960px; cy: 708px; font-size: 40px; font-family: sm; color: $cream; letter-spacing: 0.3em; in: {y:14, opacity:0, duration:0.6, ease:'power2.out'}; out: fade {duration: 0.5}) 福島県・相馬地方

# 起源: 墨絵に替わり、縦書きの 2 列が上から拭われ、朱の落款「伝承」が押される
section#origin
img#origin_ink(inset: 0; main: kb {scale: [1.12, 1.12], focus: ['15% 50%', '76% 50%']}) Traditional Japanese suiboku ink wash painting on aged washi paper: ancient warriors on horseback chasing herds of wild horses across a vast open plain as military training, dynamic sweeping brush strokes, rising dust rendered as ink mist, distant low hills, monochrome sumi ink with a subtle warm sepia paper tone, generous empty space on the right side. No text, no seals, no letters, no signature.
p#origin_years(left: 1503px; top: 99px; font-size: 132px; font-family: s; color: $ink; letter-spacing: 0.08em; writing-mode: vertical-rl; in: wipe {dir: 'down', duration: 1, ease: 'power2.inOut'}; out: fade {duration: 0.35}) 千年以上前
p#origin_lead(left: 1706px; top: 105px; font-size: 54px; font-family: sm; color: $ink; letter-spacing: 0.2em; writing-mode: vertical-rl; in: wipe {dir: 'down', duration: 0.7, ease: 'power2.inOut'}; out: fade {duration: 0.35}) その起源は
p#origin_seal(left: 1660px; top: 820px; width: 92px; font-size: 34px; font-family: s; color: $shu; line-height: 1.05; text-align: center; padding: 9px 0px; background: none; border: 4px solid $shu; border-radius: 10px; opacity: 0.92; overlap: origin_years,subtitle; transform: rotate(-4deg); in: {scale:1.7, rotation:-10, opacity:0, duration:0.22, ease:'power4.in'}; out: fade {duration: 0.35}) 伝[br]承

# 祖: 平将門の墨絵・名が縦に拭われ、読みと「相馬氏の遠祖とされる」が続き、「軍事訓練」で絵が武者へ寄る
section#masakado
img#masakado_ink(inset: 0; main: kb {scale: [1, 1.1], focus: '86% 59%'}) Traditional Japanese suiboku ink wash painting on aged washi paper: a 10th-century Japanese warlord in classical armor on horseback atop a small hill, looking out over a wide plain where wild horses run free, dramatic clouds, expressive confident brush strokes, monochrome ink with a faint vermilion accent on the armor cords, empty space on the left side. No text, no letters, no seals, no signature.
p#masakado_note(left: 150px; top: 240px; font-size: 44px; font-family: sm; color: $ink2; letter-spacing: 0.2em; writing-mode: vertical-rl; in: wipe {dir: 'down', duration: 0.9, ease: 'power2.inOut'}; out: fade {duration: 0.4}) 相馬氏の遠祖とされる
p#masakado_name(left: 216px; top: 120px; font-size: 150px; font-family: s; color: $ink; letter-spacing: 0.12em; writing-mode: vertical-rl; in: wipe {dir: 'down', duration: 0.9, ease: 'power2.inOut'}; out: fade {duration: 0.4}) 平将門
p#masakado_ruby(left: 393px; top: 136px; font-size: 30px; font-family: sm; color: $sepia; letter-spacing: 0.32em; writing-mode: vertical-rl; in: fade {duration: 0.6}; out: fade {duration: 0.4}) たいらのまさかど

# 現在: 墨絵と同じ構図の丘の武者の実写に、国指定の判子が押印の勢いで落ちて揺れる
section#hill
img#hill_photo(inset: 0; main: kb {scale: [1.08, 1.17], focus: ['86% 59%', '84% 58%']}) [photo]Photorealistic photograph: a samurai rider in full armor with a tall banner on his back, on horseback atop a small grassy hill on the right side of the frame, seen from behind at three-quarter view, looking out over a wide green festival field on the left where hundreds of mounted samurai with colorful banners gather, distant low mountains, early summer, bright sky with soft clouds. Composition mirrors a classical ink painting: rider on the right, open plain on the left. No text, no letters.
div#hill_shade(left: 0px; top: 0px; width: 1920px; height: 420px; background: linear(#0000008C,#00000000,bottom); border-radius: 24px)
# 文化財の印: 朱の板 + 白の縁 + 外の朱の輪 (outline)・押印の勢いで落ちて揺れる
div#seal(left: 120px; top: 110px; width: 810px; height: 190px; background: #B3261EF0; border: 3px solid #FFEBDCD9; border2: #B3261EF0,1,4; border-radius: 6px; box-shadow: 0px 10px 40px #00000073; transform: rotate(-2deg); in: {scale:1.75, rotation:-5, opacity:0, duration:0.2, ease:'power4.in'})
  p#kind(left: 30px; cy: 50%; font-size: 40px; font-family: s; writing-mode: vertical-rl; letter-spacing: 0.12em; line-height: 1.15) 国指定
  shape#sep(left: 90px; top: 26px; width: 2px; height: 140px; background: #FFFFFF99)
  p#body(left: 117px; cy: 50%; font-size: 66px; font-family: s; letter-spacing: 0.08em) 重要無形民俗文化財

# 3 日間: 和紙の地の中央に見出しが出て定位置へ縮み、金の罫が伸びて 1〜3 日目の札が語ごとに出る・切替の前に揃って消える
section#schedule
img#schedule_washi(inset: 0; filter: brightness(0.78); main: kb {scale: [1.04, 1.1], focus: ['', '66% 50%']}) [photo]Flat top-down macro photograph of handmade Japanese washi paper dyed deep charcoal black with a subtle indigo tint, visible long kozo fibers and soft uneven texture, evenly lit, no objects, no text, no folds, seamless full-frame texture.
# 見出しは 1.5 倍で中央に出て、1 枚目の札の前に左上の定位置へ縮む
group#schedule_head(left: 380px; top: 364px; width: 1350px; height: 248px; in: {opacity:0, scale:1.03, duration:0.8, ease:'power2.out'})
  p#kick(left: 0px; top: 0px; font-size: 45px; font-family: k; color: $gold; letter-spacing: 0.3em; out: fade {duration: 0.4}) 開催時期
  p#head(left: 0px; top: 54px; font-size: 126px; font-family: s; letter-spacing: 0.06em; out: fade {duration: 0.4}) 毎年5月下旬 {r}・{/} 3日間
shape#schedule_rule(left: 150px; top: 300px; width: 1620px; height: 3px; background: linear(#D8B26A,#D8B26A40,right); in: wipe {dir: 'right', duration: 4.2, ease: 'power1.inOut'}; out: fade {duration: 0.4})
div#day_card(left: "100;473;847"; top: 332px; width: 500px; height: 574px; background: #0E0C0BD1; border: 2px solid #D8B26A73; box-shadow: 2; in: {y:70, opacity:0, duration:0.6, ease:'power3.out'}; out: fade {duration: 0.4}) ×3
  img#photo(left: 0px; top: 0px; width: 500px; height: 300px; content: "@dawn;@sky;@noma"; main: kb {scale: [1.16, 1], ease:'power1.out'}; out: fade {duration: 0.4})
  shape#tick.ellipse(left: 34px; top: 290px; width: 22px; height: 22px; background: $shu; border: 3px solid $gold; out: fade {duration: 0.4})
  p#day(left: 34px; top: 309px; font-size: 30px; font-family: k; color: $gold; letter-spacing: 0.2em; out: fade {duration: 0.4}) {dn}1{/}日目;{dn}2{/}日目;{dn}3{/}日目
  p#event(left: 34px; top: 378px; font-size: 60px; font-family: s; letter-spacing: 0.06em; out: fade {duration: 0.4}) 出陣・宵乗り;本祭り;野馬懸
  p#detail(left: 34px; top: 477px; width: 450px; overlap: day_card.event,day_card.day; font-size: 27px; color: $gray; letter-spacing: 0.06em; out: fade {duration: 0.4}) 出陣式 ・ 宵乗り競馬;お行列 ・ 甲冑競馬 ・ 神旗争奪戦;相馬小高神社

# 本祭り: 行列の実写に左からの陰と場面の札・「騎馬武者の行列」で絵が列へ寄る
section#procession
img#procession_photo(inset: 0; content: @procession; main: kb {scale: [1.02, 1.13], focus: ['100% 50%', '38% 54%']})
shade#procession_shade
scene_label#procession_label(when: "2日目・午前"; what: "お行列"; where: "野馬追通り{g} → {/}雲雀ヶ原祭場地")

# 甲冑競馬: 写真と塵が場面ごと小刻みに揺れ、塵が横へ大きく流れる・場面の札
section#race
group#race_shake(left: 0px; top: 0px; width: 1920px; height: 1080px; main: noise {x: 4, y: 4, period: 0.07})
img#race_shake.photo(inset: 0; main: kb {scale: [1.16, 1.22], focus: ['79% 50%', '33% 50%']}) [photo]Action photograph of an armored horse race at a traditional Japanese festival: riders in samurai armor without helmets, wearing white headbands, with tall colorful banners streaming from their backs, galloping at full speed side by side on a dirt track, thick clouds of dust kicked up behind them, spectators on a grassy hillside in the background, bright midday sun. Photorealistic sports photograph, fast shutter, panning motion blur in the background. No readable text, no letters.
shade#race_shake.shade
# 塵 16 粒 (横へ大きく流れる)
shape#race_shake.dust.ellipse.bleed(left: "717;806;53;676;1078;1277;90;1;806;151;573;273;505;989;769;234"; top: "620;540;656;90;372;664;523;182;531;205;170;219;577;255;281;148"; width: "3.8;4.1;4.8;2.1;3.7;3.1;3.1;5.4;2.3;5;4.3;3.7;2.9;3;3;5.5"; height: "3.8;4.1;4.8;2.1;3.7;3.1;3.1;5.4;2.3;5;4.3;3.7;2.9;3;3;5.5"; background: #FFF0D6F2; box-shadow: 0px 0px 6px 2px #FFE2B48C; opacity: "0.37;0.29;0.42;0.27;0.36;0.44;0.49;0.35;0.21;0.20;0.23;0.48;0.22;0.21;0.53;0.48"; in: none; main: ramp {x: '173;-244;197;-295;236;-55;5;504;-41;349;221;-65;511;-244;86;-110', y: '-60;6;-63;-31;-31;-56;22;-38;23;-61;-68;14;-57;-18;-19;-60'}) ×16
scene_label#race_label(when: "2日目・正午から"; what: "甲冑競馬"; where: "雲雀ヶ原祭場地")

# 神旗争奪戦: 空を仰ぐ引きを下から上へ流し、花火の閃光・「数百の騎馬武者」で争奪の寄りに切り替わる
section#sky
veil#sky_fl(color: #FFFFFF; opacity: 0.55; z-index: curtain; in: none)
veil#sky_fl2(color: #FFFFFF; opacity: 0.32; z-index: curtain; in: none)
img#sky_photo(inset: 0; content: @sky; main: kb {scale: [1.3, 1.3], focus: ['50% 96%', '50% 7%'], ease:'sine.inOut'})
# 争奪の寄り: 語で切り替わり、2.2 秒だけ揺れる
group#scramble(left: 0px; top: 0px; width: 1920px; height: 1080px; in: none; main: noise {x: 6, y: 6, period: 0.07, window: '0,2200'})
img#scramble.photo(inset: 0; in: none; main: kb {scale: [1.06, 1.2], focus: ['', '58% 41%'], ease:'power1.out'}) [photo]Intense close action photograph: several samurai riders on horseback crowd together, reaching up high with long riding whips to catch a small sacred flag fluttering down from the sky, horses jostling, banners on their backs tangling, dust lit by the sun, a dense crowd of riders behind them. Photorealistic, telephoto, dynamic diagonal composition. No readable text, no letters.
shade#sky_shade
scene_label#sky_label(when: "2日目・午後1時から"; what: "神旗争奪戦"; where: "雲雀ヶ原祭場地")

# 野馬懸: 神事の実写と場面の札・「素手で」で絵が馬を捕らえる手へ寄る
section#noma
img#noma_photo(inset: 0; content: @noma; main: kb {scale: [1.02, 1.12], focus: ['', '60% 58%']})
shade#noma_shade
scene_label#noma_label(when: "3日目（最終日）"; what: "野馬懸"; where: "相馬小高神社")

# 観覧の心得: ぼかした行列の上の暗い板に、2 つの決まりが語ごとに左から入り、板と中身が揃って消える
section#manners
img#manners_blur(inset: 0; content: @procession; filter: blur(24px); main: kb {scale: [1.05, 1.1]})
veil#manners_dim(opacity: 0.42; color: #000000; in: none)
div#manners_board(left: 300px; top: 170px; width: 1320px; height: 600px; background: #0C0A09C7; border: 2px solid #D8B26A80; in: {y:30, opacity:0, duration:0.6, ease:'power2.out'}; out: fade {duration: 0.4})
  p#kick(left: 80px; top: 64px; font-size: 30px; font-family: k; color: $gold; letter-spacing: 0.3em; out: fade {duration: 0.4}) お行列を見るときは
  p#head(left: 80px; top: 140px; font-size: 92px; font-family: s; letter-spacing: 0.1em; out: fade {duration: 0.4}) 観覧の心得
  div#rule(left: 80px; top: "190;280"; width: 1170px; height: 92px; in: {x:-36, opacity:0, duration:0.5, ease:'power3.out'}; out: fade {duration: 0.4}) ×2
    p#num(left: 0px; cy: 50%; width: 92px; height: 92px; font-size: 54px; font-family: s; text-align: center; vertical-align: center; background: $shu; border-radius: 148px; padding: 0px; out: fade {duration: 0.4}) 一;二
    p#words(left: 126px; cy: 50%; font-size: 62px; font-family: s; letter-spacing: 0.06em; out: fade {duration: 0.4}) お行列を横切らない;高い所から見下ろさない{sm}（建物の2階など）{/}

# 締め: 夕景の武者のシルエットに暗幕が降り、題字の組をもう一度 + 開催と会場の札 + URL (法螺貝と曲の山で終わる)
section#finale
img#finale_photo(inset: 0; main: kb {scale: [1, 1.1], focus: '71% 63%'}) [photo]Silhouette of a lone mounted samurai with a tall banner on his back, standing on a gentle grassy hill against a vast golden sunset sky with dramatic glowing clouds, the horse's mane and the banner blowing in the wind, epic and peaceful mood. Photorealistic cinematic photograph, wide shot, the rider placed in the lower right third with large open sky. No text, no letters.
# エンドカード: 中央を残す暗幕 + 題字 (帯・1 字ずつ・字間が締まる英字)
veil#end_dim(background: radial(#00000059@0%,#000000C7@100%,50%,45%); in: fade {duration: 0.9, ease: 'power1.inOut'})
group#end_logo(left: 0px; top: 0px; width: 1920px; height: 1080px)
  img#brush(left: 250px; top: 150px; width: 1420px; height: 532px; content: @brush; look: #B3261E; in: wipe {dir: 'right', duration: 0.5, ease: 'power2.inOut'})
  p#jp(cx: 960px; cy: 405px; font-size: 214px; font-family: y; letter-spacing: 0.06em; text-shadow: 0px 6px 30px #00000073; in: {scale: 1.45, blur: 12, opacity: 0, duration: 0.5, ease: 'power3.out', delay: 0.2, stagger: 0.07, unit: 'grapheme'}) 相馬野馬追
  p#en(cx: 960px; cy: 616px; font-size: 34px; font-family: k; letter-spacing: 0.62em; in: {letter_spacing:0.48, opacity:0, duration:1, ease:'power2.out', delay:0.75}) SOMA NOMAOI
group#end_info(left: 0px; top: 700px; width: 1920px; height: 60px; in: {y:16, opacity:0, duration:0.6, ease:'power2.out'})
  p#held_k(left: 304px; top: 9px; font-size: 28px; font-family: k; color: $dark; background: $gold; padding: 10px 14px 10px 18px; letter-spacing: 0.2em) 開催
  p#held(left: 432px; top: 3px; font-size: 40px; font-family: sm; letter-spacing: 0.08em) 毎年5月下旬の3日間
  p#venue_k(left: 898px; top: 9px; font-size: 28px; font-family: k; color: $dark; background: $gold; padding: 10px 14px 10px 18px; letter-spacing: 0.2em) 会場
  p#venue(left: 1026px; top: 3px; font-size: 40px; font-family: sm; letter-spacing: 0.08em) 福島県 相馬市・南相馬市ほか
p#end_url(cx: 960px; cy: 843px; font-size: 32px; color: $pale; letter-spacing: 0.14em; in: fade {duration: 0.6}) 詳しくは 相馬野馬追 公式サイト（soma-nomaoi.jp）へ
```

```timeline.txt
#v2
cast narrator = "落ち着いた低音の男性ナレーター、響きが豊かで滑らか、ドキュメンタリーの語り"
silence head=0 tail=0
transition = dissolve,300,overlap=300
read 法螺貝 = ほらがい
read 甲冑 = かっちゅう
read 約400騎 = やくよんひゃっき
read 相馬野馬追 = そうまのまおい
read 遠祖 = えんそ
read 平将門 = たいらのまさかど
read 宵乗り = よいのり
read 野馬懸 = のまかけ
read 本祭り = ほんまつり
read 旗指物 = はたさしもの
read 雲雀ヶ原祭場地 = ひばりがはらさいじょうち
read 正午 = しょうご
read 御神旗 = ごしんき
read 神旗 = しんき
read 小高 = おだか
read 白装束 = しろしょうぞく
read 御小人 = おこびと
read お行列 = おぎょうれつ

*** open
[>#subtitle]
fade in,1800
bgm music +600
@narrator: [silence:2.9s][♪hora +3dB fade=0,600 -2650][>#sub_shade -380]法螺貝の音を合図に、武者たちが動き出す。[silence:0.45s]
transition cut

*** charge
@narrator: [silence:0.3s][>#charge_fl -300][!#charge_fl to,{opacity:0, duration:.32} -300][♪taiko +2dB peak=0.086s -300][♪gallop -7dB fade=50,1200 to=4.4s -300]甲冑に身を固めた、[>#riders +50][<#riders cut-50]約400騎の騎馬武者。[silence:0.3s]
transition cut

*** title
@narrator: [silence:0.25s][♪wind -9dB peak=0.35s -250]福島県・相馬地方に伝わる祭り、[>#title_dim -350][>#logo -220][>#region +750][>#title_fl][!#title_fl to,{opacity:0, duration:.5}][♪taiko2 +2.5dB peak=0.185s][♪flag -14dB fade=400,1000 to=3.6s -200]相馬野馬追です。[silence:1.45s]
transition dissolve,300,overlap=300

*** origin
@narrator: [silence:0.75s][♪swing -8dB peak=0.15s -750]その起源は、[>#origin_lead -700][>#origin_years -50][>#origin_seal +1000]千年以上前にさかのぼります。[silence:0.2s]

*** masakado
@narrator: [silence:0.35s]相馬氏の遠祖とされる[>#masakado_name -100][>#masakado_ruby +300][>#masakado_note +750]平将門が、[|]野に放った馬を敵兵に見立て、[|][!#masakado_ink zoom_media,1.12,duration=2500,focus=80%,55%]軍事訓練を行ったのが始まりと伝えられています。[silence:0.15s]
transition dissolve,300,overlap=300

*** hill
@narrator: [silence:0.45s]現在は、国の[>#seal -200][!#seal shake,3,duration=280 +20][♪wadaiko -1dB peak=0.018s]重要無形民俗文化財に指定されています。[silence:0.55s]

*** schedule
@narrator: [silence:0.55s][♪wind -10dB peak=0.35s -550][>#schedule_head -300]祭りは毎年{5月|ごがつ}下旬の3日間。[|][!#schedule_head to,{x:-454, y:-309, scale:0.667, duration:0.75, ease:'power3.inOut'} -950][>#schedule_rule -200][>#day_card[1] -180][♪kodaiko -6dB peak=0.012s]出陣と宵乗り、[>#day_card[2] -180][♪kodaiko -6dB peak=0.012s]本祭り、そして[>#day_card[3] -180][♪kodaiko -6dB peak=0.012s]野馬懸へと続きます。[silence:0.5s]
transition dissolve,300,overlap=300

*** procession
@narrator: [silence:0.5s][>#procession_label -250][♪horse -9dB peak=0.41s fade=100,800 -500][♪crowd -18dB fade=1000,1500 to=7.5s -500]本祭りの朝。[||]旗指物をなびかせた[!#procession_photo zoom_media,1.1,duration=2500,focus=40%,55%]騎馬武者の行列が、[|]雲雀ヶ原祭場地へと進みます。[silence:0.45s]
transition cut

*** race
@narrator: [silence:0.4s][>#race_label -250][♪wind -7dB peak=0.35s -400][♪gallop -5dB fade=50,1000 to=6.4s -400][♪cheer -15dB fade=500,1500 to=6s]正午からは甲冑競馬。[|]土ぼこりを上げ、人馬一体となって駆け抜けます。[silence:0.45s]
transition cut

*** sky
@narrator: [silence:0.45s][>#sky_fl -450][!#sky_fl to,{opacity:0, duration:.4} -450][♪hanabiho -4dB peak=0.033s fade=0,800 -450][>#sky_label -250]そして神旗争奪戦。[|][>#sky_fl2 +250][!#sky_fl2 to,{opacity:0, duration:.55} +250][♪firework -3dB peak=4.02s fade=0,1500 +250]花火で打ち上げられ、空から舞い降りる御神旗を、[|][>#scramble -120][♪cheer -9dB fade=200,2000 to=7.2s -120]数百の騎馬武者が奪い合います。[silence:1.0s]

*** noma
@narrator: [silence:0.9s][♪wadaiko peak=0.018s -900][♪neigh -8dB -750][>#noma_label -400]最終日は、相馬小高神社の野馬懸。[|]白装束の御小人たちが、[!#noma_photo zoom_media,1.12,duration=2000,focus=60%,58%]素手で馬を捕らえ、[|]神前に献納します。[silence:0.45s]

*** manners
@narrator: [silence:0.55s][♪swing -10dB peak=0.15s -550][>#manners_board]観覧の心得は、[>#manners_board.rule[1] -150][♪kodaiko -8dB peak=0.012s]お行列を横切らないこと、[|][>#manners_board.rule[2] -150][♪kodaiko -8dB peak=0.012s]高い所から見下ろさないこと。[silence:0.3s]
transition dissolve,300,overlap=300

*** finale
@narrator: [silence:0.7s][♪flag -15dB fade=800,1500 to=6s -700]千年の歴史を受け継ぐ武者たちの勇姿を、[|]ぜひ、その目で。[silence:0.45s][>#end_dim -100][>#end_logo +50][>#end_info +1250][>#end_url +1700][<#sub_shade][♪odeza +1dB peak=0.015s fade=0,1200][♪hora -6dB fade=50,1000 +550][silence:5.6s]
```

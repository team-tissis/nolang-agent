# concept · tech-crime-law (hf 全力版の全量の写し — テクノロジー犯罪を抑制する法律が必要・14 場面の暗い絵と「赤枠 × 黄の文字」で訴える縦リール) — canvas 720x1280

見せる作り: 常設の層 (上下の暗幕 + 周辺減光・grain・上端の赤→黄の進行線)・場面ごとの暗い絵の溶け替え (文の途中の絵替え 3 回・グリッチで揺れて入る絵)・判子のように叩きつける赤枠 × 黄の札と画面の揺れ・字幕の強調 run・3 つの章扉 (薄い巨大な番号 + 線の icon + 2 段の見出し) と左上の章札 (sticky)・ぼけから浮かぶ囁きの吹き出し・赤縁の丸窓・伸びる帯・柱の札 3 枚 (白の地から赤枠へ移る強調)・赤と青緑にずれる写し・広がる光の輪・2 つの吹き出し・2 曲の BGM と語に結んだ効果音 46

```design.txt
#v2
# 学ぶ作り: 全編に敷く常設の層 (上下の暗幕 + 周辺減光・grain・上端の赤→黄の進行線) の上で、場面ごとに暗い絵を溶かして替える (文の途中の絵替え 3 回・グリッチの絵は揺らして入る)
# 「赤枠 × 黄の文字」を 1 つの class で通す: 主役の語は判子のように叩きつける札 (key)・字幕の強調は run・板の中の強調は白の地から赤枠へ移る変種 (.on)
# 3 つの章は章扉 (薄い巨大な番号 + 線の icon + 見出し) で区切り、章の間は左上の章札 (sticky) を残す・囁きの吹き出し・柱の札 3 枚・二重にずれる見出し・広がる光の輪
# hf b08 tech-crime-law (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 720x1280 bg=#05070D
theme dark
palette y=#FFE600 red=#E60012 warm=#FFC56B gr=#FF0030 gc=#00E5FF line=#FF2A3A
font "太字 (Bold) の角ゴシック体、力強く端正で読みやすい"
fonts m="太めの明朝体、繊細で静かな印象"
sfx off
# hf の作り: 章札は章の頭に置き題を先に見せる (spoiler)・囁き 3 本は字幕を閉じて吹き出しだけで見せる (caption_gap)・章札の下に囁き / 柱の札が積まれる (stacked_labels)
# hf の作り: 「見えない暴力」は赤と青緑の写しを本体に重ねて左右にずらし、透明へ消す (overlap・low_contrast・duplicate_text)・章扉の小札「問題点」は巨大な番号の上に乗る (overlap)
# hf の作り: 字幕と見出しは場面の切替 (溶け) の途中から出る (entrance_in_transition)
# hf の作り: 章扉 03 の「社会へ」は最後の語で出し、すぐ次の場面へ溶ける (entrance_in_fadeout)
lint off=spoiler,caption_gap,stacked_labels,overlap,low_contrast,duplicate_text,entrance_in_transition
master lufs=-15
art "Cinematic semi-realistic digital painting, volumetric lighting, subtle film grain, high detail"
prompt_tail "Vertical 9:16 portrait composition, the main subject large and centered in the middle of the frame, the scene fills the whole frame from top to bottom. Absolutely no text, no letters, no numbers, no logos, no watermarks, no UI text."
# 字幕の強調 = 赤枠 × 黄の字 (hf の .hl: border 7px / radius 12 / padding 0 14px を 2/3 に)
run h { color: $y; background: #0E0406CC; border: 5px solid $red; border-radius: 8px; padding: 9px }
cut { stagger: 0 }
p { color: #FFFFFF; out: {opacity:0, duration:0.3, ease:'power1.in'} }
div { border: none; box-shadow: none; padding: 0px; out: {opacity:0, duration:0.3, ease:'power1.in'} }
svg { out: {opacity:0, duration:0.3, ease:'power1.in'} }
shape { out: {opacity:0, duration:0.3, ease:'power1.in'} }
group { out: {opacity:0, duration:0.3, ease:'power1.in'} }
sound impact_bass = "重低音のドンという衝撃音、低く響く"
sound glitch_short = "短いデジタルのグリッチノイズ、ザッと途切れる電子音"
sound glitch_rhythm = "リズムを刻むデジタルのグリッチ音、ザザッと乱れる電子ノイズ"
sound glitch_long = "長めのデジタルグリッチノイズ、壊れた信号がザザザと乱れる"
sound swing_low = "低くうなる短い風切り音、ブンという振り"
sound impact_thud = "鈍く重いドスッという打撃音"
sound impact_bighit = "映画の予告編のような大きく重い衝撃音、ドーンと残響"
sound door_slam = "重い扉が閉まるバタンという音"
sound whoosh_soft = "柔らかく流れるシュワッという風の音"
sound whoosh_sharp = "鋭く速いヒュッという風切り音"
sound whoosh_swish = "シュッと横に払う素早い風切り音"
sound drone_dark = "暗く不穏な低いドローン、持続する唸り"
sound piano_chord = "ピアノの低い和音をジャーンと一度鳴らす、重く沈む響き"
sound heartbeat = "ドクンドクンと続く心臓の鼓動音"
sound riser = "徐々に高まっていく緊張のライザー音、シューッと上昇する"
sound pad_swell = "温かいシンセパッドがふわっと膨らむ音"
sound chime_soft = "柔らかく澄んだチャイムのキラリという音"
sound windchime = "ウィンドチャイムがキラキラと長く鳴る音"
# 線の icon (hf の線画を svg に・白 + 黄 / 赤 / 緑の 2 色)。章札の小さい icon は太い線の版 (_b)
svg mag = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M42 18 a24 24 0 1 0 0.01 0 Z" stroke="#FFFFFF"/><path d="M60 60 L84 84" stroke="#FF2A3A"/></g></svg>"""
svg mag_b = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><path d="M42 18 a24 24 0 1 0 0.01 0 Z" stroke="#FFFFFF"/><path d="M60 60 L84 84" stroke="#FF2A3A"/></g></svg>"""
svg shield = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M50 8 L84 20 V48 C84 70 68 86 50 94 C32 86 16 70 16 48 V20 Z" stroke="#FFFFFF"/><path d="M34 50 L46 62 L68 38" stroke="#FFE600"/></g></svg>"""
svg shield_b = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><path d="M50 8 L84 20 V48 C84 70 68 86 50 94 C32 86 16 70 16 48 V20 Z" stroke="#FFFFFF"/><path d="M34 50 L46 62 L68 38" stroke="#FFE600"/></g></svg>"""
svg sprout = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M26 92 H74" stroke="#FFFFFF"/><g stroke="#8BE89A"><path d="M50 92 V54"/><path d="M50 62 C36 62 24 52 22 36 C38 36 50 46 50 62 Z"/><path d="M50 54 C52 38 64 26 82 26 C80 44 68 54 50 54 Z"/></g></g></svg>"""
svg sprout_b = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"><path d="M26 92 H74" stroke="#FFFFFF"/><g stroke="#8BE89A"><path d="M50 92 V54"/><path d="M50 62 C36 62 24 52 22 36 C38 36 50 46 50 62 Z"/><path d="M50 54 C52 38 64 26 82 26 C80 44 68 54 50 54 Z"/></g></g></svg>"""
svg eye = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><g stroke="#FFFFFF"><path d="M8 50 C24 26 76 26 92 50 C76 74 24 74 8 50 Z"/><path d="M50 38 a12 12 0 1 0 0.01 0 Z"/></g><path d="M18 84 L82 16" stroke="#FF2A3A"/></g></svg>"""
svg folder = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M10 28 H40 L48 36 H90 V84 H10 Z" stroke="#FFFFFF"/><g stroke="#FFE600"><path d="M41 52 C41 42 59 42 59 52 C59 60 50 60 50 68"/><path d="M50 76 L50 77.5"/></g></g></svg>"""
svg chat = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 18 H86 V66 H46 L28 84 V66 H14 Z" stroke="#FFFFFF"/><path d="M50 57 C38 48 33 42 37 35 C41 29 50 31 50 38 C50 31 59 29 63 35 C67 42 62 48 50 57 Z" stroke="#FFE600"/></g></svg>"""
svg bolt = """<svg viewBox="0 0 100 100"><path d="M57 6 L22 56 H48 L41 94 L78 40 H52 Z" fill="none" stroke="#FFE600" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg scales = """<svg viewBox="0 0 100 100"><g fill="none" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><g stroke="#FFFFFF"><path d="M50 12 V84"/><path d="M30 88 H70"/><path d="M18 28 H82"/></g><g stroke="#FFE600"><path d="M18 28 L6 56 H30 Z"/><path d="M82 28 L70 56 H94 Z"/></g></g></svg>"""
# 暗い吹き出しの尻尾 (金の小さな下向き三角・右下)・div の板に shape: speech-bubble を付けると枠の下辺が切れるので、角丸の板 + この svg で組む
svg tail = """<svg viewBox="0 0 20 13"><path d="M0 0 L20 0 L10 13 Z" fill="#FFC56B"/></svg>"""
# 同じ絵を 2 回以上使う物は根の基準画像に (shadow = 冒頭と「見えない暴力」・alone = 章扉のぼかしと囁き・consult = 柱と締めの声・law = 章扉のぼかしと柱・dawn = 章扉の寄りと締め)
image shadow = "In the dark behind a wall of glowing computer monitors, a faceless hooded silhouette made of digital noise and glitch fragments stretches long shadowy fingers through the screens toward a tiny distant person who is looking down at a smartphone, unaware. Invisible attacker hiding in the network. Menacing, cold blue light with red glitch accents. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red." aspect=9:16
image alone = "A young person sitting alone on the floor of a dark bedroom at night, hugging their knees with face hidden in their arms, lit only by the cold blue glow of a smartphone lying on the floor beside them. Seen from the side and slightly behind. Loneliness, fear and silence, lots of dark empty space around them. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red." aspect=9:16
image consult = "A warm, safe consultation room. A kind counselor gently listens to a person sitting across a small round table with two cups of tea, soft lamp light, plants by the window. Both seen from the side so faces are soft and not detailed. Reassuring, calm, trustworthy atmosphere, the person's shoulders relaxing. Color palette: warm amber, soft gold and gentle peach light with calm teal shadows." aspect=9:16
image law = "A wooden judge's gavel resting on an open thick law book on a dark desk. From the pages, a luminous translucent shield made of cyan network lines rises into the air, and a masked shadow figure made of glitch fragments shatters and dissolves against the shield. Justice catching up with anonymous digital crime. Dramatic rim lighting. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red." aspect=9:16
image dawn = "Wide view of a quiet town at sunrise, warm golden light breaking through the clouds over the rooftops. In the foreground a small fresh green sprout grows from the soil, catching the light. In the middle distance a few people stand together side by side, seen from behind, looking toward the sunrise. Hope and a new beginning. Color palette: warm amber, soft gold and gentle peach light with calm teal shadows." aspect=9:16
# BGM は 2 曲: 問題提起は不穏な曲・「法律が必要」の章扉から希望の曲へ持ち替える
bgm#doc(fade: 400,2100) 不穏で不気味な社会派ドキュメンタリーの曲、ピアノとコントラバスと低いシンセ、BPM85の抑えた低い響き、ナレーションの邪魔をしない
bgm#hope(fade: 600,3200) 明るく温かく穏やかな希望の曲、三拍子のクラシカルなピアノと弦楽、後半に向けて壮大に広がる
# 字幕: 画面の中ほど (y 841) に白文字 + 黒の縁 + 黒い光彩・句の割り方は台詞の [|]・句点だけ外す
# hf の作り: 字幕を下端でなく画面の中ほどに置き、下 3 割は暗幕だけ
subtitle.hug(left: 27px; top: 841px; width: 667px; font-size: 41px; line-height: 1.42; letter-spacing: 0.02em; text-align: center; color: #FFFFFF; stroke: #000000,5; text-shadow: 0px 3px 17px #000000D9; background: none; unit: sentence; strip: 。; lead: 50; tail: 450; hold: off; in: {y:23, opacity:0, duration:0.32, ease:'power3.out'}; out: {y:-12, opacity:0, duration:0.22, ease:'power2.in'})

# 暗幕 (上 62% → 20〜50% は素通し → 下 90%) + 周辺減光の子 (章ごとに濃さを語で変える)
def shade() = div(inset: 0; background: linear(#03050C9E,#03050C00@20%,#03050C00@50%,#03050CB3@66%,#03050CDB@84%,#03050CE6,180); in: none; out: none)
  div#v(inset: 0; background: radial(#00000000@42%,#000000C7,50%,44%); opacity: 0.85; in: none; out: none)
# 見出しの白文字 (黒の縁 + 黒い光彩・下から上がる)
def head(t, s=67) = p(width: 640px; text-align: center; font-size: {s}; line-height: 1.2; letter-spacing: 0.03em; stroke: #000000,4; text-shadow: 0px 3px 17px #000000D9; in: {y:27, opacity:0, duration:0.45, ease:'power3.out'}; content: {t})
# 主役の語の札 = 赤枠 × 黄の文字 (判子: 1.9 倍から縮んで叩きつける)
def key(t, s=85) = p(font-size: {s}; line-height: 1.15; letter-spacing: 0.04em; color: $y; background: #0C0406D6; border: 8px solid $red; border-radius: 12px; padding: 5px 27px 13px 27px; box-shadow: 0px 0px 40px #E60012A6; text-shadow: 0px 3px 0px #00000099; in: {scale:1.9, opacity:0, duration:0.26, ease:'power4.in'}; content: {t})
# 章扉の薄い巨大な番号 (4 秒かけて濃く・大きく)
def bignum(t, c=#FFFFFF29) = p(cx: 360px; top: 200px; font-size: 413px; line-height: 1; letter-spacing: -0.02em; color: #FFFFFF1A; stroke: {c},3; in: {opacity:0, scale:0.85, duration:4.4, ease:'power1.out'}; content: {t})
# 左上の章札 (赤の丸に黄の番号 + 線の icon + 題・赤の縁の暗いピル)
def chap(n, ic, t, w, tw) = div(left: 37px; top: 117px; width: {w}; height: 51px; background: #080A14BD; border: 2px solid $red; border-radius: 99px; in: {x:-27, opacity:0, duration:0.4, ease:'power3.out'}; out: {opacity:0, duration:0.3})
  p#n(left: 5px; cy: 50%; width: 39px; font-size: 20px; line-height: 1; text-align: center; color: $y; background: $red; border-radius: 99px; padding: 10px 0px; content: {n})
  svg#i(left: 52px; cy: 50%; width: 27px; height: 27px; part: {ic})
  p#t(left: 87px; cy: 50%; width: {tw}; font-size: 27px; line-height: 1.2; content: {t})
# 囁きの吹き出し (明朝・青い光・ぼけから浮かぶ)
def whisper(t, s=41) = p(font-family: m; font-size: {s}; line-height: 1.35; color: #EEF4FF; background: #060C1CA3; border: 2px solid #AAC8FF99; border-radius: 24px; padding: 13px 23px 16px 23px; box-shadow: 0px 0px 27px #5A96FF47; text-shadow: 0px 0px 8px #78AAFF99; in: {y:17, opacity:0, blur:9, duration:0.6, ease:'power2.out'}; out: {opacity:0, blur:8, duration:0.9, ease:'power1.in'}; content: {t})
# 赤縁の丸い窓 + 線の icon
def orb(ic) = div(top: 427px; width: 240px; height: 240px; border-radius: 120px; background: radial(#1E2846E0,#060812EB,50%,40%); border: 5px solid $red; box-shadow: 0px 0px 33px #E6001280; in: {scale:0.4, opacity:0, duration:0.5, ease:'back.out(2)'}; out: {opacity:0, duration:0.35, ease:'power1.in'})
  svg#i(left: 53px; top: 53px; width: 133px; height: 133px; part: {ic})
# 柱の札 (左の赤い縁 + 番号の丸 + icon + 2 行)・2 行目の強調 k は白の地で出て語で赤枠へ移る (変種 .on)
def pillar(n, ic, l1, k, l2) = div(left: 29px; width: 661px; height: 121px; background: #080C18D6; border: 2px solid #FFFFFF29; border-radius: 15px; box-shadow: 0px 7px 27px #00000080; in: {x:107, opacity:0, duration:0.5, ease:'power3.out'}; out: {opacity:0, duration:0.35, ease:'power1.in'})
  div#edge(left: 0px; top: 0px; width: 9px; height: 117px; background: $red; border-radius: 13px 0px 0px 13px)
  p#n(left: 25px; cy: 50%; width: 51px; font-size: 31px; line-height: 1; text-align: center; color: $y; background: $red; border-radius: 99px; padding: 10px 0px; content: {n})
  svg#i(left: 91px; cy: 50%; width: 64px; height: 64px; part: {ic}; delay: 150; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(1.7)'})
  p#l1(left: 170px; top: 12px; width: 470px; font-size: 32px; line-height: 1.42; content: {l1})
  p#k(left: 168px; top: 56px; font-size: 32px; line-height: 1.22; background: #0E040680; border: 4px solid #E6001200; border-radius: 8px; padding: 0px 6px 3px 6px; content: {k})
  p#l2(left: .k.right+2; top: 58px; width: 215px; font-size: 32px; line-height: 1.42; content: {l2})

# 全編の層: 暗幕と周辺減光・grain・上端の進行線 (地 16% の白 + 赤→黄の棒)
shade#shade
veil#grain(grain: 0.08; mix-blend-mode: multiply; main: noise {x: 4, y: 4, period: 0.083})
div#prog_track(left: 0px; top: 0px; width: 720px; height: 5px; background: #FFFFFF29; z-index: front; in: none; out: none)
progress#prog(left: 0px; top: 0px; width: 720px; height: 5px; background: linear($red,$y,90); until: end; z-index: front; overlap: prog_track)

# 開幕: 夜の街の俯瞰がグリッチで揺れて入り、走査線が上から下へ走る・題を 3 段に語ごとに組み「必要です」を判子で
section#hook
img#city(inset: 0; object-fit: cover; object-position: bottom; zoom: 200%; main: kb {scale: [1, 1.1], focus: ['50% 55%', '50% 55%']}) A vast modern city at night seen from high above. Countless windows and smartphone screens glow in the streets like stars. Thin luminous cyan network lines connect the buildings like a giant spider web over the city, and a few of the lines pulse in an ominous red. Calm surface, hidden danger. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
# グリッチの帯: 同じ絵を clip-path: inset() で 5 本の帯に切り、steps(1) で x を飛ばす (hf の .gs)
img#gs1(inset: 0; object-fit: cover; object-position: bottom; zoom: 200%; clip-path: inset(8% 0 78% 0); opacity: 0; main: none; in: none; out: none) A vast modern city at night seen from high above. Countless windows and smartphone screens glow in the streets like stars. Thin luminous cyan network lines connect the buildings like a giant spider web over the city, and a few of the lines pulse in an ominous red. Calm surface, hidden danger. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
img#gs2(inset: 0; object-fit: cover; object-position: bottom; zoom: 200%; clip-path: inset(30% 0 58% 0); opacity: 0; main: none; in: none; out: none) A vast modern city at night seen from high above. Countless windows and smartphone screens glow in the streets like stars. Thin luminous cyan network lines connect the buildings like a giant spider web over the city, and a few of the lines pulse in an ominous red. Calm surface, hidden danger. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
img#gs3(inset: 0; object-fit: cover; object-position: bottom; zoom: 200%; clip-path: inset(52% 0 36% 0); opacity: 0; main: none; in: none; out: none) A vast modern city at night seen from high above. Countless windows and smartphone screens glow in the streets like stars. Thin luminous cyan network lines connect the buildings like a giant spider web over the city, and a few of the lines pulse in an ominous red. Calm surface, hidden danger. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
img#gs4(inset: 0; object-fit: cover; object-position: bottom; zoom: 200%; clip-path: inset(71% 0 18% 0); opacity: 0; main: none; in: none; out: none) A vast modern city at night seen from high above. Countless windows and smartphone screens glow in the streets like stars. Thin luminous cyan network lines connect the buildings like a giant spider web over the city, and a few of the lines pulse in an ominous red. Calm surface, hidden danger. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
img#gs5(inset: 0; object-fit: cover; object-position: bottom; zoom: 200%; clip-path: inset(88% 0 4% 0); opacity: 0; main: none; in: none; out: none) A vast modern city at night seen from high above. Countless windows and smartphone screens glow in the streets like stars. Thin luminous cyan network lines connect the buildings like a giant spider web over the city, and a few of the lines pulse in an ominous red. Calm surface, hidden danger. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
div#scan.bleed(left: 0px; top: -13px; width: 720px; height: 3px; background: linear(#78F0FF00,#78F0FFE6@25%,#FFFFFF,#78F0FFE6@75%,#78F0FF00,90); box-shadow: 0px 0px 17px 4px #50DCFF8C; in: none; out: none)
head#t1a(cx: 360px; cy: 449px; s: 64; in: {y:33, opacity:0, duration:0.45, ease:'power3.out'}) テクノロジー犯罪を
head#t1b(cx: 360px; cy: 538px; s: 64; in: {y:33, opacity:0, duration:0.45, ease:'power3.out'}) 抑制する法律が
key#t1c(cx: 360px; cy: 669px; width: 418px; text-align: center) 必要です

# 便利な暮らし → 文の途中で「見えない」影の絵へグリッチで替わる・「増えています」で赤い上昇の矢印を描く
section#life
img#life_photo(inset: 0; object-fit: cover; object-position: bottom; zoom: 180%; main: kb {scale: [1.1, 1], focus: ['50% 45%', '50% 45%']}) Close-up of a person's hands holding a smartphone in a bright, cozy living room in the morning. Translucent floating icons around the phone suggest online shopping, maps, messaging, video calls and cashless payment, but drawn only as simple symbols without any text. Convenient, comfortable modern digital life. Face not visible. Color palette: warm amber, soft gold and gentle peach light with calm teal shadows.
# 文の中の絵替え (語で出す絵は全編の暗幕より上に乗るので暗幕を重ね直す)・影の絵はフードと伸びる爪と右下の小さな人 (狙われる側) を全部入れる範囲に寄せる
img#shadow_photo(inset: 0; content: @shadow; object-fit: cover; object-position: 72% 100%; zoom: 160%; main: kb {scale: [1, 1.06], focus: ['88% 100%', '88% 100%']}; in: {opacity:0, duration:0.12, ease:'power1.inOut'})
# 爪と小さな人は絵の下 (y 55〜86%) にいるので、この絵の暗幕は下を浅く (55% まで素通し・周辺減光も薄く) して見せる
shade#life_shade(background: linear(#03050C9E,#03050C00@20%,#03050C00@55%,#03050C59@78%,#03050CB3@92%,#03050CD9,180); life_shade.v.opacity: 0.35)
shape#up_line(path: "M542 779 L585 739 L613 754 L662 687"; background: none; border: 6px solid $line; box-shadow: 0px 0px 11px #FF283CB3; in: draw {duration: 0.6})
shape#up_head(path: "M628 684 L665 684 L665 721"; background: none; border: 6px solid $line; box-shadow: 0px 0px 11px #FF283CB3; in: draw {duration: 0.6})

# 大きな壁: 霧の中にそびえる壁の絵・「大きな壁」の札を判子で
section#wall
img#wall_photo(inset: 0; object-fit: cover; object-position: 50% 85%; zoom: 190%; main: kb {scale: [1, 1.08], focus: ['50% 85%', '50% 85%']}) Low-angle shot of a small lone person seen from behind, standing in front of an enormous towering dark concrete wall that fills the whole frame and disappears into the fog above. Faint glowing circuit-board lines and cracks run across the wall surface. Overwhelming sense of scale and obstruction, cold mist on the ground. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
key#wall_key(cx: 360px; cy: 498px; width: 452px; text-align: center; s: 93; in: {scale:2.2, opacity:0, duration:0.26, ease:'power4.in'}; out: {opacity:0, duration:0.35, ease:'power1.in'}) 大きな壁

# 章扉 01: ぼかした孤独の絵に薄い巨大な「01」・回りながら出る虫眼鏡・判子の「問題点」・2 段の見出し (2 段目は赤枠の札)
section#problem
img#problem_photo(inset: 0; content: @alone; filter: blur(12px); main: kb {scale: [1.12, 1.18]})
bignum#s4n 01
svg#s4i(left: 284px; top: 337px; width: 153px; height: 153px; part: mag; overlap: s4n; delay: 50; in: {rotation:-25, scale:0.6, opacity:0, duration:0.9, ease:'back.out(1.6)'})
key#s4l(cx: 360px; cy: 545px; s: 39; overlap: s4n; letter-spacing: 0.12em; border: 5px solid $red; border-radius: 8px; padding: 4px 20px 7px 20px; box-shadow: 0px 0px 15px #E6001273; in: {scale:1.7, opacity:0, duration:0.26, ease:'power4.in'}) 問題点
head#s4h1(cx: 360px; cy: 645px) 被害者が
key#s4h2(cx: 360px; cy: 757px; width: 554px; text-align: center; s: 69; line-height: 1.22; border: 7px solid $red; border-radius: 8px; padding: 3px 20px 9px 20px; box-shadow: 0px 0px 15px #E6001273; in: {y:27, opacity:0, duration:0.45, ease:'power3.out'}) 声を上げづらい

# 被害者の声: 膝を抱える人の絵に、囁きの吹き出しが 1 つずつぼけから浮かび前の囁きは沈む → 「そんな気持ち」で同じ絵の寄りへ溶けて替わる
section#voices
img#alone_photo(inset: 0; content: @alone; object-fit: cover; object-position: bottom; zoom: 150%; main: kb {scale: [1, 1.12], focus: ['52% 100%', '54% 100%']})
chap#ch1.sticky(n: "01"; ic: mag_b; t: "問題点"; w: 192; tw: 86)
whisper#w1(left: 40px; top: 280px) 「恥ずかしい…」
whisper#w2(left: 427px; top: 200px) 「怖い…」
whisper#w3(left: 47px; top: 393px; s: 37) 「どう相談したら[br]いいのか分からない…」
img#alone_zoom(inset: 0; content: @alone; object-fit: cover; object-position: bottom; zoom: 185%; main: kb {scale: [1, 1.07], focus: ['51% 100%', '51% 100%']}; in: {opacity:0, duration:0.3, ease:'power1.inOut'})
shade#zoom_shade

# デジタル空間: 画素のドームの絵がグリッチで入り、「周囲」で目の窓・「証拠」でフォルダの窓 (前の窓は沈む)
section#digital
img#digital_photo(inset: 0; object-fit: cover; object-position: bottom; zoom: 160%; main: kb {scale: [1, 1.1], focus: ['50% 45%', '50% 45%']}) A person standing alone inside a translucent dome made of floating pixels and blurred chat bubbles, notification icons and broken file icons, cut off from the world. Outside the dome, blurred passers-by on a city street walk past without noticing anything. The harm is invisible from outside. Surreal, cold, quiet. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
orb#o1(left: 80px; ic: eye)
orb#o2(left: 400px; ic: folder)

# 長期化: 時計と舞う暦の絵・「長期化」で字幕の下に橙→赤の帯が伸びる
section#longterm
img#time_photo(inset: 0; main: kb {scale: [1.06, 1.17], focus: ['50% 40%', '50% 43%']}) A dim room at night: torn pages of a wall calendar fly through the air, a large wall clock looms in the background, and on the desk a smartphone screen glows with many unread message bubbles shown only as shapes. Days passing while suffering continues. Gloomy blue light, slow and heavy atmosphere. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
div#stretch(left: 107px; top: 928px; width: 507px; height: 11px; background: #FFFFFF24; border-radius: 5px; in: {opacity:0, duration:0.2}; out: {opacity:0, duration:0.25})
  div#fill(left: 0px; top: 0px; width: 507px; height: 11px; background: linear(#FF9A00,$red,90); border-radius: 5px; box-shadow: 0px 0px 12px #FF3C00CC; delay: 100; in: {scaleX:0.02, duration:1.76, ease:'power1.inOut', pivot:'left'})

# 章扉 02: 白い閃光 → ぼかした法の絵に「02」・盾の icon・「だからこそ、」と判子の「法律が必要です」
section#law
img#law_blur(inset: 0; content: @law; filter: blur(12px); main: kb {scale: [1.1, 1.16]})
veil#flash(color: #FFFFFF; opacity: 0.6; z-index: curtain; in: {opacity:0, duration:0.08}; out: none)
bignum#s8n 02
svg#s8i(left: 277px; top: 373px; width: 167px; height: 167px; part: shield; overlap: s8n; in: {scale:0.5, opacity:0, duration:0.7, ease:'back.out(1.8)'})
head#s8h1(cx: 360px; cy: 605px) だからこそ、
key#s8k(cx: 360px; cy: 727px; width: 612px; text-align: center; s: 75; in: {scale:1.8, opacity:0, duration:0.26, ease:'power4.in'}) 法律が必要です

# 3 つの柱: 文ごとに絵を替え (相談室 → 対応の現場 → 法の盾)、柱の札を右から 1 枚ずつ積む (前の札は沈み、言い終えて戻る)
section#pillars
img#consult_photo(inset: 0; content: @consult; main: kb {scale: [1.18, 1.08], focus: ['50% 28%', '50% 26%']})
chap#ch2.sticky(n: "02"; ic: shield_b; t: "法律が必要"; w: 246; tw: 140)
img#team_photo(inset: 0; main: kb {scale: [1.08, 1.18], focus: ['50% 30%', '50% 30%']}; in: {opacity:0, duration:0.4, ease:'power1.inOut'}) A team of specialists in a modern response center moving quickly and decisively: people seen from behind in front of large screens showing glowing network maps and connection lines, one person pointing, another talking on a headset. Urgent but organized. Cool blue light with warm highlights, sense of speed. Color palette: deep navy, midnight blue and cold cyan glow with small accents of warning red.
shade#team_shade(team_shade.v.opacity: 0.7)
img#law_photo(inset: 0; content: @law; object-fit: cover; object-position: 60% 100%; zoom: 186%; main: kb {scale: [1, 1.06], focus: ['60% 100%', '60% 100%']}; in: {opacity:0, duration:0.4, ease:'power1.inOut'})
shade#law_shade(law_shade.v.opacity: 0.7)
pillar#pl1(top: 593px; pl1.k.width: 216px; n: 1; ic: chat; l1: "被害者が"; k: "安心して相談"; l2: "できる仕組み")
pillar#pl2(top: 728px; pl2.k.width: 216px; n: 2; ic: bolt; l1: "専門機関が"; k: "迅速に動ける"; l2: "ルール")
pillar#pl3(top: 863px; pl3.k.width: 278px; n: 3; ic: scales; l1: "匿名性を悪用した加害行為を、"; k: "確実に取り締まる"; l2: "ための法整備")
#pl1.k.on(color: $y; background: #0E0406CC; border: 4px solid $red; box-shadow: 0px 0px 15px #E6001273)
#pl2.k.on(color: $y; background: #0E0406CC; border: 4px solid $red; box-shadow: 0px 0px 15px #E6001273)
#pl3.k.on(color: $y; background: #0E0406CC; border: 4px solid $red; box-shadow: 0px 0px 15px #E6001273)

# 見えない暴力: 影の絵を赤く染めてグリッチで入り、「見えない暴力」の札に赤と青緑の写しが左右にずれて消える
section#violence
img#violence_photo(inset: 0; content: @shadow; object-fit: cover; object-position: 48% 100%; zoom: 185%; main: kb {scale: [1, 1.06], focus: ['40% 100%', '40% 100%']})
div#tint(inset: 0; background: linear(#AA0A149E,#460000B3,180); mix-blend-mode: multiply; in: none)
head#s10a(cx: 360px; cy: 496px) テクノロジー犯罪は
group#vk(left: 0px; top: 520px; width: 720px; height: 226px; in: {scale:2, opacity:0, duration:0.26, ease:'power4.in'})
  key#m(cx: 50%; cy: 50%; s: 93) 見えない暴力
  key#ghost_r(cx: 50%; cy: 50%; s: 93; color: $gr; background: none; border: 8px solid $gr; box-shadow: none; opacity: 0; overlap: vk.m; delay: 220; in: keys(at=0 x=-11 opacity=0.8 | at=0.2 x=7 opacity=0.8 | at=0.4 x=-5 opacity=0.8 | at=0.6 x=3 opacity=0.8 | at=0.8 x=-6 opacity=0.8 | at=1 x=0),duration=1400) 見えない暴力
  key#ghost_c(cx: 50%; cy: 50%; s: 93; color: $gc; background: none; border: 8px solid $gc; box-shadow: none; opacity: 0; overlap: vk.m,vk.ghost_r; delay: 220; in: keys(at=0 x=11 opacity=0.8 | at=0.2 x=-7 opacity=0.8 | at=0.4 x=5 opacity=0.8 | at=0.6 x=-3 opacity=0.8 | at=0.8 x=6 opacity=0.8 | at=1 x=0),duration=1400) 見えない暴力

# 社会全体で守る: 光の輪を囲む手の絵・「社会全体」で中央から金色の輪が 4 重に 3 回広がる
section#society
img#hands_photo(inset: 0; object-fit: cover; object-position: bottom; zoom: 180%; main: kb {scale: [1, 1.1], focus: ['50% 55%', '50% 55%']}) Many hands of diverse people of different ages and skin tones reaching in from all sides to form a protective circle of warm light around a small glowing figure of a person in the center. The dark background is turning warm and golden where the light spreads. Solidarity, society protecting someone together. Color palette: warm amber, soft gold and gentle peach light with calm teal shadows.
shape#ring.ellipse(left: 293px; top: 640px; width: 134px; height: 134px; background: none; border: 4px solid #FFD68C66; mix-blend-mode: screen; in: {scale:0.4, opacity:0, duration:0.3})

# 章扉 03: 夜明けの絵の芽に寄った構図・温かい縁の「03」・芽の icon・赤枠の「声を上げられる」と「社会へ」
section#voice_up
img#dawn_zoom(inset: 0; content: @dawn; object-fit: cover; object-position: bottom; zoom: 260%; main: kb {scale: [1.08, 1], focus: ['50% 100%', '50% 100%']})
bignum#s12n(c: #FFD68C38) 03
svg#s12i(left: 280px; top: 381px; width: 160px; height: 160px; part: sprout; overlap: s12n; delay: 180; in: {y:27, scale:0.6, opacity:0, duration:1.2, ease:'power3.out'})
key#s12h1(cx: 360px; cy: 625px; s: 69; line-height: 1.22; border: 7px solid $red; border-radius: 8px; padding: 3px 20px 9px 20px; box-shadow: 0px 0px 15px #E6001273; in: {y:27, opacity:0, duration:0.45, ease:'power3.out'}) 声を上げられる
head#s12h2(cx: 360px; cy: 740px) 社会へ

# 二つの声: 相談室の絵に、白い吹き出し (相談していいんだ) と暗い金縁の吹き出し (あなたは ひとりじゃない) が弾んで出る
section#bubbles
img#bubbles_photo(inset: 0; content: @consult; main: kb {scale: [1.28, 1.18], focus: ['35% 45%', '35% 45%']})
chap#ch3.sticky(n: "03"; ic: sprout_b; t: "声を上げられる社会へ"; w: 384; tw: 278)
p#b1(left: 43px; top: 260px; font-family: m; font-size: 44px; line-height: 1.32; color: #2B2018; background: #FFFAF0F2; border-radius: 29px; padding: 16px 27px 20px 27px; box-shadow: 0px 8px 27px #00000059; shape: speech-bubble; in: {scale:0.6, y:20, opacity:0, duration:0.55, ease:'back.out(2.2)'}; out: {opacity:0, duration:0.4, ease:'power1.in'}) 「相談していいんだ」
div#b2(left: 220px; top: 767px; width: 463px; height: 165px; background: #16100AD6; border: 2px solid $warm; border-radius: 29px; box-shadow: 0px 8px 27px #00000059; in: {scale:0.6, y:20, opacity:0, duration:0.55, ease:'back.out(2.2)'}; out: {opacity:0, duration:0.4, ease:'power1.in'})
  p#l1(right: 27px; top: 16px; font-family: m; font-size: 44px; line-height: 1.32) 「あなたは
  p#k(left: 27px; top: 78px; font-size: 47px; line-height: 1.22; background: #0E040680; border: 5px solid #E6001200; border-radius: 8px; padding: 0px 9px 3px 9px) ひとりじゃない
  p#q(left: .k.right+2; top: 84px; font-family: m; font-size: 44px; line-height: 1.32) 」
  svg#tail.bleed(left: 380px; top: 163px; width: 20px; height: 13px; part: tail)
#b2.k.on(color: $y; background: #0E0406CC; border: 5px solid $red; box-shadow: 0px 0px 15px #E6001273)

# 結び: 夜明けの街の全景に、文を語ごとに 4 段で組み「欠かせません」を判子で・最後は黒へ落ちる
section#closing
img#dawn_photo(inset: 0; content: @dawn; object-fit: cover; object-position: bottom; zoom: 190%; main: kb {scale: [1, 1.08], focus: ['50% 100%', '50% 100%']})
head#t2a(cx: 360px; cy: 409px; s: 40; line-height: 1.3; letter-spacing: 0.02em) そう言える社会をつくるために、
head#t2b(cx: 360px; cy: 491px; s: 64) テクノロジー犯罪を
head#t2c(cx: 360px; cy: 579px; s: 64) 抑制する法律は
key#t2d(cx: 360px; cy: 704px; width: 534px; text-align: center; s: 75; in: {scale:1.8, opacity:0, duration:0.26, ease:'power4.in'}) 欠かせません
```

```timeline.txt
#v2
cast n = "落ち着いた低音の男性ナレーター、響きが豊かで滑らかな声、知的で信頼感のあるドキュメンタリーの語り"
cast v = "息を多く含んだ柔らかく繊細な若い女性の声、小さく不安げにつぶやく"
silence head=0 tail=0
transition = dissolve,400,overlap=400,ease=power1.inOut

*** hook
bgm doc
@n: [silence:0.55s][!#city shake,30,duration=240 -550][!#gs1 to,{x:-90, opacity:1, duration:0.01} -550][!#gs1 to,{x:45, duration:0.07, ease:'steps(1)'} -480][!#gs1 to,{x:-30, duration:0.07, ease:'steps(1)'} -410][!#gs1 to,{x:0, opacity:0, duration:0.08, ease:'steps(1)'} -320][!#gs2 to,{x:70, opacity:1, duration:0.01} -550][!#gs2 to,{x:-35, duration:0.07, ease:'steps(1)'} -480][!#gs2 to,{x:23, duration:0.07, ease:'steps(1)'} -410][!#gs2 to,{x:0, opacity:0, duration:0.08, ease:'steps(1)'} -320][!#gs3 to,{x:-50, opacity:1, duration:0.01} -550][!#gs3 to,{x:25, duration:0.07, ease:'steps(1)'} -480][!#gs3 to,{x:-17, duration:0.07, ease:'steps(1)'} -410][!#gs3 to,{x:0, opacity:0, duration:0.08, ease:'steps(1)'} -320][!#gs4 to,{x:110, opacity:1, duration:0.01} -550][!#gs4 to,{x:-55, duration:0.07, ease:'steps(1)'} -480][!#gs4 to,{x:36, duration:0.07, ease:'steps(1)'} -410][!#gs4 to,{x:0, opacity:0, duration:0.08, ease:'steps(1)'} -320][!#gs5 to,{x:-70, opacity:1, duration:0.01} -550][!#gs5 to,{x:35, duration:0.07, ease:'steps(1)'} -480][!#gs5 to,{x:-24, duration:0.07, ease:'steps(1)'} -410][!#gs5 to,{x:0, opacity:0, duration:0.08, ease:'steps(1)'} -320][♪impact_bass -550][♪glitch_short -5dB -530][!#scan to,{y:1300, duration:1.1, ease:'power1.inOut'} -500][<#scan +800][♪swing_low -9dB -50][>#t1a]テクノロジー犯罪を[>#t1b][♪swing_low -9dB -50]抑制する法律が[>#t1c -200][♪impact_thud +40][!#t1a shake,9,duration=320 +40][!#t1b shake,9,duration=320 +40][!#t1c shake,9,duration=320 +40]必要です。[silence:0.55s]
transition dissolve,450,overlap=450

*** life
[>#subtitle]
@n: [silence:0.45s][♪whoosh_soft -6dB -450 to=1.3s]いま、私たちの生活は[br]便利になった一方で、[|][>#shadow_photo -120][>#life_shade -120][!#shadow_photo shake,30,duration=240 -120][♪glitch_short -2dB -140][♪drone_dark -13dB -120 fade=400,1500 to=5.4s]見えない場所で[br]人を傷つける[|]“[♪impact_thud -6dB]{h}テクノロジー犯罪{/}”が[br][>#up_line -150][>#up_head -150][♪swing_low -9dB -100]増えています。[silence:0.4s]

*** wall
@n: [silence:0.4s][♪whoosh_sharp -6dB -300]でも――[|]この問題には、[br]まだ[>#wall_key -250][♪door_slam +10][♪impact_bighit -6dB +10 to=4.3s fade=0,1500][!#wall_key shake,9,duration=320 -10]{h}大きな壁{/}があります。[silence:1.25s]
[<#subtitle]
transition dissolve,350,overlap=350

*** problem
@n: [silence:0.45s][♪whoosh_swish -6dB -450][>#s4l -120][♪piano_chord -6dB -50][!#s4l shake,9,duration=320 +120][!#s4i shake,9,duration=320 +120]問題点。[>#s4h1 -80]被害者が[>#s4h2 -80][!#s4h2 punch,1.16,duration=440]声を上げづらい。[silence:0.2s]
transition dissolve,600,overlap=600

*** voices
[>#subtitle]
@n: [silence:0.6s][>#ch1 -200]テクノロジー犯罪の被害者は、[silence:0.55s]
[<#subtitle]
@v: [>#w1 -150][♪whoosh_soft -12dB -200 to=1.3s][!#w1 to,{y:-11, duration:9.4, ease:'none'} +450]恥ずかしい…[silence:0.6s]
@: [>#w2 -150][!#w1 dim,0.55 -100][♪whoosh_soft -12dB -200 to=1.3s][!#w2 to,{y:-11, duration:7.1, ease:'none'} +450]怖い…[silence:0.6s]
@: [>#w3 -150][!#w2 dim,0.55 -100][!#w1 dim,0.4 -100][♪whoosh_soft -12dB -200 to=1.3s][!#w3 to,{y:-11, duration:5.1, ease:'none'} +450]どう相談したらいいのか分からない…[silence:0.9s]
[>#subtitle]
@n: [♪heartbeat -11dB -400 fade=800,1600 to=6.2s][>#alone_zoom -120][>#zoom_shade -120][!#shade.v to,{opacity:1, duration:3.5, ease:'power1.inOut'}][!#zoom_shade.v to,{opacity:1, duration:3.5, ease:'power1.inOut'}][<#w1 +700][<#w2 +700][<#w3 +700]そんな気持ちを抱えたまま、[|]{h}ひとりで苦しんで{/}しまうことが[br]多いんです。[silence:0.6s]
transition dissolve,120,overlap=120

*** digital
@n: [silence:0.4s][!#digital_photo shake,30,duration=240 -400][♪glitch_rhythm -6dB -400][!#shade.v to,{opacity:0.7, duration:1} -400]デジタル空間で起きる被害は、[|][>#o1 -100][♪swing_low -8dB -100]周囲から{h}見えにくく{/}、[|][>#o2 -100][!#o1 to,{opacity:0.55, scale:0.92, duration:0.4} -100][♪swing_low -8dB -100]{h}証拠の集め方{/}も[br]分からない。[silence:0.15s]
transition dissolve,450,overlap=450

*** longterm
@n: [silence:0.45s][♪whoosh_soft -6dB -300 to=1.3s]だから相談が[♪riser -7dB -130 fade=2500,0]遅れ、[|]被害が[>#stretch -100][♪impact_thud -5dB]{h}長期化{/}[<#stretch +1200]してしまう。[silence:1.3s]
[<#ch1]
[<#doc]
[<#subtitle]
transition dissolve,500,overlap=500

*** law
bgm hope +390
@n: [silence:0.6s][>#flash -90][!#flash to,{opacity:0, duration:0.45} -10][>#s8i -60][♪impact_bass -1dB -60][>#s8h1 -50][♪pad_swell -12dB +140 fade=600,2000]だからこそ、[>#s8k -200][♪impact_thud -2dB +40][!#s8h1 shake,9,duration=320 +40][!#s8i shake,9,duration=320 +40][!#s8k shake,9,duration=320 +40]法律が必要です。[silence:0.5s]

*** pillars
@n: [silence:0.4s][>#pl1 -120][♪whoosh_swish -8dB -170][♪chime_soft -13dB -20][>#ch2 +100]被害者が[!#pl1.k .on][!#pl1.k punch,1.16,duration=440]安心して相談できる仕組み。[silence:0.6s]
@: [>#team_photo -170][>#team_shade -170][>#pl2 -120][!#pl1 dim,0.62,duration=350 -120][♪whoosh_swish -8dB -170][♪chime_soft -13dB -20]専門機関が[!#pl2.k .on][!#pl2.k punch,1.16,duration=440]迅速に動けるルール。[silence:0.6s]
@: [>#law_photo -150][>#law_shade -150][>#pl3 -120][!#pl2 dim,0.62,duration=350 -120][♪whoosh_swish -8dB -170][♪chime_soft -13dB -20]匿名性を悪用した加害行為を、[!#pl3.k .on][!#pl3.k punch,1.16,duration=440]確実に取り締まるための法整[=#pl1 +440][=#pl2 +440]備。[silence:1.1s]
transition dissolve,120,overlap=120

*** violence
@n: [silence:0.2s][!#violence_photo shake,30,duration=240 -200][♪glitch_long -6dB -200 to=1.8s][>#s10a -60]テクノロジー犯罪は“[>#vk -220][♪impact_bighit -3dB +20 to=4.3s fade=0,1500][♪glitch_short -6dB +20][!#s10a shake,9,duration=320 +20][!#vk shake,9,duration=320 +20]見えない[!#vk.ghost_r to,{opacity:0.75, x:-5, duration:0.05} +500][!#vk.ghost_c to,{opacity:0.75, x:-5, duration:0.05} +500][!#vk.ghost_r to,{opacity:0, x:0, duration:0.08} +620][!#vk.ghost_c to,{opacity:0, x:0, duration:0.08} +620][♪glitch_short -11dB +500]暴力”。[silence:0.2s]
[<#vk.m fade][<#vk.ghost_r fade][<#vk.ghost_c fade]
transition dissolve,600,overlap=600

*** society
[>#subtitle]
@n: [silence:0.6s][♪whoosh_soft -7dB -250 to=1.3s][!#shade.v to,{opacity:0.55, duration:1.2} -200]見えないからこそ、[|][>#ring -400][!#ring ping,#FFD68C,4,interval=320,duration=1250,scale=0.4>4.2 -400][!#ring ping,#FFD68C,4,interval=320,duration=1250,scale=0.4>4.2 +900][!#ring ping,#FFD68C,3,interval=320,duration=1250,scale=0.4>4.2 +1300][♪chime_soft -11dB -100]{h}社会全体で守る{/}仕組みが[br]必要です。[silence:1.2s]
[<#ch2]
[<#subtitle]
transition dissolve,700,overlap=700

*** voice_up
@n: [silence:0.7s][♪windchime -11dB -420 fade=0,1500 to=4.5s][>#s12h1 -60][!#s12h1 punch,1.16,duration=440]声を上げられる[>#s12h2 -60]社会へ。[silence:0.4s]
transition dissolve,600,overlap=600

*** bubbles
@v: [silence:0.6s][>#ch3 -40][>#b1 -150][♪chime_soft -11dB -120]相談していいんだ。[silence:0.7s]
@n: [>#b2 -150][♪chime_soft -10dB -120]あなたは[!#b2.k .on][!#b2.k punch,1.16,duration=440]ひとりじゃない。[silence:0.1s]
[<#b2 fade]
transition dissolve,800,overlap=800

*** closing
@n: [silence:0.8s][♪whoosh_soft -9dB -290 to=1.3s][>#t2a -60]そう言える社会をつくるために、[>#t2b -60]テクノロジー犯罪を[>#t2c -60]抑制する法律は[>#t2d -200][♪impact_thud -1dB +40][!#t2a shake,9,duration=320 +40][!#t2b shake,9,duration=320 +40][!#t2c shake,9,duration=320 +40][!#t2d shake,9,duration=320 +40]欠かせません。[silence:0.4s][♪windchime -14dB fade=0,1500 to=3.5s][silence:1.7s][<#ch3][silence:1.5s]
fade out,1000
```

# concept · sun-blackhole (hf 全力版の全量の写し — もしも太陽がブラックホールになったら・宇宙の思考実験を 7 場面の CG と図解で) — canvas 1080x1920

見せる作り: 全編を貫く画面中央上部の極太縁取りテロップ (場面の頭に 1.45 倍から弾む・文の途中で差し替え) と句ごとの縁取り字幕・太陽が縮んで閃光と揺れで漆黒の円盤に変わる冒頭・渦を巻いて吸い込まれる地球と「巻き戻し」・2 重の群の sine で回る楕円の公転 (尾の点 7 つ)・語ごとに組む図解 (式の札・縮む太陽と数え下ろす半径・伸びる距離の線と数え上げ・引力の矢・判子)・赤い脈と吸い込まれる光の筋・昼の街で 8:20 を数え下ろして夜へ・気温を数え下ろす凍結と全面写真の差し替え・夜明けの安心と眠りの Z・プロフィールの札の誘導・音の層 (語に結んだ効果音 29 + 曲 2 本の切替)

```design.txt
#v2
# 学ぶ作り: 7 場面を全部「画面中央上部の大きな縁取りテロップ (場面の頭に弾んで出る・文の途中で差し替える)」+「下 3 割の縁取り字幕 (句ごとの札)」の 2 段で通す
# 宇宙の場面は同じ星空の絵の上に部品 (ブラックホールの円盤・地球・軌道の楕円) を重ね、楕円の公転は 2 重の群の sine (x と y の位相を 1/4 ずらす) で回す。奥へ回り込む半周は円盤の下に置いた写し (earth_b) を square の alpha で半周ずつ入れ替えて見せる (hf の zIndex の切替)
# 図解は語ごとに組む: 式の札 → 太陽と地球と距離の点線 → 太陽が縮んで数字が減る → 距離の線が伸びて数字が増える → 引力の矢 → 判子・写真の場面は全面の絵を語で差し替え、幕 (赤い脈・霜・青い光) を重ねる
# hf b05 sun-blackhole (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#000000
theme dark
palette ye=#FFE14D chip=#FFD23A mass=#FFC23A cyan=#5FE0FF red=#FF4057 sunc=#FFD43B ice=#9BE7FF warm=#FFE3A3 ok=#6DFFB0 ink=#05060B lilac=#D9C8FF pale=#C9D6FF
font "清潔で中立的な極太のゴシック体、均整の取れたかなと漢字と端正な欧文、明快で読みやすい標準の字幕向け"
fonts d="超極太のディスプレイ用ゴシック体、極端に太い画と詰まった懐でどっしりした字面、勢いとパンチのあるサムネや広告の見出し向け"
sfx off
# hf の作り: テロップは場面の頭に台詞より先に出る (spoiler)・字幕と同じ語をテロップにも出す (duplicate_text)
lint off=spoiler,duplicate_text
# hf の作り: 太陽・衝撃波・吸い込まれる地球・全面のブラックホールの寄り・夜の街の寄りはわざと画面の外へはみ出す
# hf の作り: 効果音は素材を切らずに最後まで鳴らす (se_long)・テロップの炎のグラデと札の赤は palette 外の直書き (palette_drift)
prompt_tail "No text, no letters, no logos, no watermark."
# 字幕の強調 (黄)・テロップの語の色 (質量 = 橙・距離 = 水色・恐怖 = 赤・光 = 黄・氷 = 水色)・札の太字 (黄 / 緑)
run y { color: $ye }
run m { color: $mass }
run d { color: $cyan }
run r { color: $red }
run s { color: $sunc }
run i { color: $ice }
run b { color: $chip }
run g { color: $ok }
run nb { font-size: 1.4em }
p { color: #FFFFFF; line-height: 1.45; out: none }
div { border: none; out: none }
img { out: none }
group { out: none }
shape { out: none }
cut { stagger: 0 }
sound doom = "重く響く映画的な低音の衝撃音、破滅を告げる一撃"
sound riser = "短いホラーのライザー、逆再生のノイズが膨らんで鋭く切れる"
sound bighit = "金属的に響く劇的なドーンという衝撃音と長い残響"
sound comet = "彗星が宇宙を飛び去る、風のようにうねるシューンという音"
sound suck = "宇宙のうなりのような低い吸い込まれる音、金属的な震え"
sound camera = "残響のある近未来的なカメラの動きのスウッシュ"
sound comet2 = "彗星が速く横切る明るいシュッという音"
sound impact = "ローファイな短い衝撃音、重い低音のドスッ"
sound sweep = "乾いた短いノイズスイープ、シュッ"
sound click = "低めの軽い電子のボタン音、ポチッ"
sound drone = "暗く不穏な低いシンセのうなり、場面転換のダークなドローン"
sound heart = "心臓の鼓動のような重い低音のドクン、不気味な残響"
sound tick = "速く刻む時計の秒針の音"
sound ice = "ガラスのようにきらめく氷の魔法、冷たく走って凍りつく音"
sound wind = "隙間を抜ける冷たい風のひゅうという音"
sound sparkle = "低めの穏やかなキラキラ、柔らかい鈴の揺らぎ"
# 絵: 同じ星空・太陽・ブラックホール・地球・街を場面を跨いで使う (基準画像)
image space = "[photo]Deep space background: pitch-black void with countless tiny faint stars of varied brightness and a very subtle dark blue-violet nebula haze drifting diagonally, minimal and elegant, mostly empty dark space. No planets, no sun." aspect=9:16
image sun = "[transparent]Ultra-detailed photorealistic CGI of our Sun seen from space, the whole round disc centered and filling about 90% of the frame. Blazing white-yellow core fading to deep orange-red at the limb, turbulent plasma granulation, looping solar prominences and flares at the edge, glowing corona halo."
image blackhole = "[photo]Photorealistic cinematic CGI of a black hole in deep space. A perfectly pitch-black sphere (the event horizon) at the center slightly above the middle, about 40% of the frame width, outlined by a thin razor-sharp bright white-gold photon ring and a faint secondary ring of lensed light. The starfield around it is visibly warped by gravitational lensing into an Einstein ring of distorted stars. No accretion disk, no jets, no planets. Eerie, silent, cold." aspect=9:16
image bh_disc = "[transparent][ref:@blackhole]The same black hole cut out as a round disc: the black sphere, its photon ring and the swirl of lensed starlight around it, fading softly to transparent at the outer edge."
image earth = "[transparent]Photorealistic planet Earth seen from space, a complete sphere perfectly centered and filling the frame edge to edge, lit from the upper left with a soft day-night terminator on the right, deep blue oceans, white swirling clouds, thin glowing blue atmosphere rim."
image earth_ice = "[transparent][ref:@earth]The same planet Earth completely frozen over: oceans turned into cracked white and pale-blue ice sheets, continents buried under snow, no clouds, dim cold bluish light from the upper left, the rest in deep shadow."
image city_day = "[photo]Cinematic low-angle photo looking up a busy modern Tokyo business street at midday. Tall glass office skyscrapers line both sides and rise from the bottom edge all the way to the top edge of the frame, converging toward the top, with street trees along the sidewalks. A narrow wedge of clear deep-blue sky shows between them at the top center, with the bright blazing sun near the top and a strong lens flare. Pedestrians and cars on the street at the bottom, warm summer daylight." aspect=9:16
image city_night = "[ref:@city_day]Edit: the same street, the same buildings and the same framing at deep night after the sun has vanished: the wedge of sky between the buildings pitch black and full of stars, no sun, no flare, the buildings dark with only a few lit windows, cold blue tones" aspect=9:16
image city_frozen = "[photo]Cinematic low-angle photo looking up a narrow Tokyo street canyon completely frozen in an eternal night. Ice-covered skyscrapers with frosted windows and long hanging icicles line both sides and rise from the bottom edge all the way to the top edge of the frame, converging toward the top. Further down the street more frozen skyscrapers and a frozen spired tower rise into the upper half; an ice-encrusted traffic light on a cable hangs across the street in the upper middle; abandoned cars buried in snow and snow drifts on the road at the bottom. A narrow wedge of pitch-black starry sky shows between the converging buildings at the top center. No sun, no people. Eerie cold blue tones lit by faint starlight and a few dying streetlights." aspect=9:16
image sleep = "[photo]Photorealistic cinematic photo of a young Japanese adult sleeping peacefully and deeply in a cozy bed at night, eyes closed with a soft gentle smile, warm amber bedside lamp glow, soft bluish moonlight through the window, fluffy white blanket, camera slightly above looking down at the face in the middle of the frame." aspect=9:16
# 街の写真 3 枚と凍った海は主体を枠いっぱいに宣言する (宣言が無いと engine が同じ cut のテロップの箱から「上を空ける」構図を生成に足し、街や波が下 3〜4 割に固まって上が空の帯になる)・hf と同じくビルの上にテロップが乗る (warn text_over_subject は承知)
# 曲: 太陽が消える瞬間だけ一瞬落とす (timeline の語の印 [!#music to,{volume:-13dB}])
bgm#music 冷たく暗く緊張感のあるシネマティックなアンビエント、シンセパッドと合唱と遠い打楽器、遅い四拍子、宇宙の静かな恐怖
bgm#piano 静かで穏やかなソロピアノ、ゆっくりした安心させる目覚めの曲
# 字幕: 白の極太 + 黒の太い縁 + 落ち影・句ごとの札 (句は台詞の [|])・強調の語は黄 {y}
subtitle.hug(bottom: 370px; padding: 18px 0px; font-size: 62px; line-height: 1.28; text-align: center; color: #FFFFFF; stroke: #05060B,13; text-shadow: 0px 10px 26px #000000A6; background: none; unit: sentence; lead: 0; in: {y:18, scale:.94, opacity:0, duration:.14, ease:'power2.out'})
# 画面中央上部のテロップ (群): 場面の頭に 1.45 倍から弾んで出る・行は tl の段 (極太の見出し書体 + 黒の太い縁取り)
def telop = group(left: 30px; top: 178px; width: 1020px; height: 510px; transform-origin: 50% 40%; in: {scale:1.45, opacity:0, duration:.24, ease:'back.out(2.4)'})
def tl(t, s, w) = p(left: 0px; width: 1020px; text-align: center; color: #FFFFFF; font-family: d; font-size: {s}; line-height: 1.35; white-space: nowrap; stroke: #05060B,{w}; text-shadow: 0px 10px 26px #000000A6; content: {t})
# 上 4 割の暗幕 (テロップの下地・どの写真の場面にも)
def topshade = div(left: 0px; top: 0px; width: 1080px; height: 760px; background: linear(#0000009E,#00000059@55%,#00000000,180); border-radius: 24px; in: none)
# 図の白い名札 (極太・中央揃え・ふわっと出る)
def lab(t) = p(font-size: 56px; text-align: center; white-space: nowrap; in: {opacity:0, duration:.3, ease:'power2.out'}; content: {t})
# 結論の札 (紺の丸札 + 水色の縁・弾んで出る・太字は {b} 黄 / {g} 緑)
def chip(t) = p(top: 1214px; font-size: 46px; white-space: nowrap; padding: 14px 30px; border-radius: 148px; background: #080E1EC7; border: 3px solid #96D2FFD9; box-shadow: 0px 8px 22px #00000080; in: {scale:.6, opacity:0, duration:.35, ease:'back.out(2.2)'}; out: {opacity:0, duration:.15}; content: {t})
# 判子 (縁と同じ色の極太の字・傾けて 2.2 倍から叩きつける)
def stamp(t, c, bg) = p(font-family: d; text-align: center; color: {c}; background: {bg}; border: 10px solid {c}; border-radius: 22px; box-shadow: 0px 0px 40px {c}; in: {scale:2.2, opacity:0, duration:.28, ease:'back.out(2.6)'}; content: {t})
# 光の筋 (外側だけ光る細い帯・回すと左端が中心に来るよう中点を置く)
def ray(r) = div(width: 760px; height: 8px; border-radius: 4px; rotation: {r}; background: linear(#FFD65A00,#FFD65A00@36%,#FFD65AF2@52%,#FFF4BE,90))
# 全編の周辺減光 (写真と図の上・テロップの下)
div#grade(inset: 0; background: radial(#00000000@60%,#00000073,50%,50%); border-radius: 24px; in: none)

# 冒頭: 星空の大きな太陽が呼吸して、語で一気に縮み、白い閃光と揺れで漆黒の円盤に変わる。地球が渦を巻いて吸い込まれ、「巻き戻し」で戻る
section#hook
img#h_space(inset: 0; content: @space; main: none)
# 太陽 (光の輪 + 円盤 + 縮むときに白く光る芯) を 1 つの群で縮める・中心はブラックホールと同じ点 (360,753)・円盤は hf と同じく画面の左右の端に届く (約 710 px)
group#h_sun.bleed(left: 0px; top: 480px; width: 1080px; height: 1300px; transform-origin: 50% 50%; in: none)
  div#glow.bleed(left: -204px; top: -93px; width: 1488px; height: 1488px; border-radius: 50%; background: radial(#FFBE5A00@38%,#FF962859@47%,#FF781400@70%,50%,50%); in: none)
  img#img.bleed(left: -108px; top: 2px; width: 1296px; height: 1296px; content: @sun; object-fit: contain; in: none)
  div#core(left: 380px; top: 490px; width: 320px; height: 320px; border-radius: 50%; background: radial(#FFFFFF,#FFF0C8F2@25%,#FFB45080@55%,#FF781400@72%,50%,50%); opacity: 0; in: none)
img#h_bh(left: 228px; top: 818px; width: 624px; height: 624px; content: @bh_disc; object-fit: contain; in: {scale:.32, opacity:0, duration:.75, ease:'expo.out'})
# 衝撃波の輪 (0.2 倍から 6.5 倍へ広がって消える)
shape#h_ring(left: 390px; top: 980px; width: 300px; height: 300px; border-radius: 50%; background: none; border: 10px solid #FFE1AAF2; box-shadow: 0px 0px 40px #FFBE6EE6; in: {scale:.2, duration:.05, ease:'none'})
# 半径の札 (引き出し線 + 2 行)
group#h_label(left: 514px; top: 1200px; width: 566px; height: 135px; in: {x:40, opacity:0, duration:.35, ease:'power2.out'}; out: {opacity:0, duration:.2})
  div#line(left: 0px; top: 40px; width: 86px; height: 4px; background: #FFFFFF; box-shadow: 0px 0px 10px #FFFFFFCC)
  p#txt(left: 96px; top: -4px; width: 450px; font-size: 58px; line-height: 1.3; white-space: nowrap; text-shadow: 0px 4px 14px #000000E6) 半径 わずか3km
  p#small(left: 96px; top: 69px; width: 390px; font-size: 38px; color: $pale; white-space: nowrap; text-shadow: 0px 4px 14px #000000E6) 太陽の約23万分の1
# 吸い込まれる地球 (静止 = 渦の外側の始点・語で 5 区間の to を続けて中心へ)
img#h_earth.bleed(left: 922px; top: 1216px; width: 190px; height: 190px; content: @earth; object-fit: contain; in: {opacity:0, duration:.05})
p#h_q(left: 620px; top: 790px; width: 300px; font-family: d; font-size: 300px; line-height: 1; text-align: center; color: $red; stroke: #05060B,17; text-shadow: 0px 10px 26px #000000A6; transform: rotate(12deg); in: {scale:.2, rotation:-32, opacity:0, duration:.38, ease:'back.out(2.6)'}; out: {opacity:0, duration:.15}) ？
# 巻き戻しの走査線 + 札
div#h_rew(inset: 0; pattern: hatch,90,#FFFFFF12,5,1; border-radius: 24px; in: {opacity:0, duration:.08})
  p#tag(left: 60px; top: 1215px; width: 360px; text-align: center; font-size: 46px; padding: 6px 22px; border: 4px solid #FFFFFF; border-radius: 10px; background: #00000059) ◀◀ 巻き戻し
topshade#h_shade
# 表紙のテロップは 0 frame 目から見えている (1.08 から締まり、呼吸する)・ブラックホールは炎のグラデの文字
telop#t_hook(in: {scale:1.08, duration:.45, ease:'power3.out'})
  tl#a(top: 0px; s: 106px; w: 15) もしも太陽が
  tl#b(top: 132px; s: 140px; w: 17; color: linear(#FFF6B8,#FFD23A@42%,#FF7A12@78%,#FF3D0A,180)) ブラックホール
  tl#c(top: 306px; s: 106px; w: 15) になったら？
veil#h_flash(color: #FFFFFF; opacity: 1; z-index: curtain; in: {opacity:0, duration:.05, ease:'none'})

# 衝撃: 白の閃光と揺れで入り、円盤が上へ縮む。楕円の軌道が描かれ、地球が尾を引いて回り続ける・札が語ごとに弾む
section#shock
img#s_space(inset: 0; content: @space; main: none)
# 地球の奥の半周 (円盤の下の写し — 前の半周は見えない)
group#s_orb_b(left: 0px; top: 0px; width: 1080px; height: 1920px; delay: 350; main: sine {x: 400, period: 4.804, phase_offset: 0.274}; in: {opacity:0, duration:.3})
  group#oy_b(left: 0px; top: 0px; width: 1080px; height: 1920px; main: sine {y: 140, period: 4.804, phase_offset: 0.024})
    img#earth_b(left: 468px; top: 938px; width: 146px; height: 146px; content: @earth; object-fit: contain; main: sine {scale: 0.19, period: 4.804, phase_offset: 0.024})
img#s_bh(left: 276px; top: 746px; width: 528px; height: 528px; content: @bh_disc; object-fit: contain; in: {y:120, scale:1.18, duration:.9, ease:'power3.out'})
shape#s_orbit(left: 140px; top: 870px; width: 800px; height: 280px; border-radius: 50%; background: none; border: 4px solid #9FE6FFB3; delay: 200; in: draw {duration: 1.1})
#s_orbit.bold(border: 8px solid #BFF0FFE6)
# 尾の点 7 つ: 地球と同じ楕円を位相を少しずつ遅らせて回る (x の群 → y の群 → 点)
group#s_tr(left: 0px; top: 0px; width: 1080px; height: 1920px; delay: 350; main: sine {x: 400, period: 4.804, phase_offset: '0.260;0.233;0.206;0.179;0.152;0.125;0.098'}; in: {opacity:0, duration:.3}) ×7
  group#ty(left: 0px; top: 0px; width: 1080px; height: 1920px; main: sine {y: 140, period: 4.804, phase_offset: '0.010;0.983;0.956;0.929;0.902;0.875;0.848'})
    shape#d(left: "352;352;353;353;354;355;355"; top: "665;665;666;666;667;668;668"; width: "17;16;14;13;12;11;10"; height: "17;16;14;13;12;11;10"; border-radius: 50%; background: radial(#8CDCFFF2,#8CDCFF00@70%,50%,50%); opacity: "0.85;0.73;0.61;0.49;0.36;0.24;0.12")
# 地球の公転 (楕円 rx 267 / ry 93・周期 4.8 s・手前で大きく奥で小さく)
group#s_orb(left: 0px; top: 0px; width: 1080px; height: 1920px; delay: 350; main: sine {x: 400, period: 4.804, phase_offset: 0.274}; in: {opacity:0, duration:.3})
  group#oy(left: 0px; top: 0px; width: 1080px; height: 1920px; main: sine {y: 140, period: 4.804, phase_offset: 0.024})
    img#earth(left: 468px; top: 938px; width: 146px; height: 146px; content: @earth; object-fit: contain; main: sine {scale: 0.19, period: 4.804, phase_offset: 0.024})
chip#s_c1(left: 92px; width: 338px; text-align: center) 質量 {b}＝ 同じ{/}
chip#s_c2(left: 544px; width: 435px; text-align: center) 重力 {b}＝ そのまま{/}
chip#s_c3(left: 70px; width: 458px; text-align: center; border: 3px solid $ok) {g}✓{/} 吸い込まれない
chip#s_c4(left: 585px; width: 360px; text-align: center; border: 3px solid $ok) {g}↻{/} 公転は続く
topshade#s_shade
telop#t_shock
  p#badge(left: 428px; top: 0px; width: 165px; text-align: center; font-family: d; font-size: 64px; line-height: 1.3; background: linear(#FF3B4F,#C4001D,180); border-radius: 16px; padding: 0px 0px 4px 0px; box-shadow: 0px 8px 26px #0000008C) 衝撃
  tl#a(top: 102px; s: 92px; w: 13) 地球は
  tl#b(top: 212px; s: 104px; w: 15) 吸い込まれない！？
veil#s_flash(color: #FFFFFF; opacity: .85; z-index: curtain; in: {opacity:0, duration:.04, ease:'none'})

# なぜ: 方眼の宇宙に式の札、太陽と地球と距離の点線を置き、太陽が縮んで半径の数字が 696,000 → 3 に減り、距離の線が伸びて 1億5000万 km、引力の矢、全体を薄めて判子
section#why
img#w_space(inset: 0; content: @space; opacity: .8; main: none)
div#w_grid(inset: 0; pattern: grid,60,#78B4FF59; opacity: .28; border-radius: 24px; in: none)
topshade#w_shade
p#w_formula(left: 90px; top: 520px; width: 900px; font-size: 74px; line-height: 1.35; text-align: center; padding: 26px 0px; border-radius: 26px; background: #060C1CD1; border: 3px solid #8CBEFF99; box-shadow: 0px 10px 30px #00000080; delay: 250; in: {y:40, opacity:0, duration:.4, ease:'power3.out'}) 重力 ∝ {m}質量{/} ÷ {d}距離{/}²
group#w_diag(left: 0px; top: 0px; width: 1080px; height: 1920px; in: none)
  lab#name(left: 40px; top: 762px; width: 460px; delay: 550) 太陽
  lab#name2(left: 40px; top: 762px; width: 460px; color: $lilac; in: {opacity:0, duration:.2}) ブラックホール
  img#sun(left: 70px; top: 880px; width: 360px; height: 360px; content: @sun; object-fit: contain; delay: 450; in: {scale:0, duration:.45, ease:'back.out(1.8)'})
  div#bh(left: 195px; top: 1005px; width: 112px; height: 112px; border-radius: 50%; background: #000000; border: 4px solid #FFECC8F2; box-shadow: 0px 0px 26px 8px #FFC882BF; in: {scale:.2, opacity:0, duration:.35, ease:'back.out(2)'})
  p#radius(left: 10px; top: 1208px; width: 520px; font-size: 48px; text-align: center; color: $mass; white-space: nowrap; in: {opacity:0, duration:.3, ease:'power2.out'}) 半径 {nb}[count:0,003 start=696,000 ms=2180 delay=450]{/} km
  shape#dline(points: "227,673 527,673"; background: none; border: 4px solid #5FE0FFD9; dash: 12,11; in: {opacity:0, duration:.25}; out: {opacity:0, duration:.3})
  lab#dlab(left: 340px; top: 920px; width: 450px; color: $cyan; in: {opacity:0, duration:.25}; out: {opacity:0, duration:.15}) 距離
  div#line(left: 340px; top: 1006px; width: 450px; height: 8px; background: linear(#5FE0FF,#A9F0FF,90); box-shadow: 0px 0px 14px #5FE0FFCC; border-radius: 24px; in: {scaleX:0, duration:1.2, ease:'power2.inOut', pivot:'left'})
  p#dist(left: 300px; top: 910px; width: 540px; font-size: 62px; text-align: center; color: $cyan; white-space: nowrap; in: {opacity:0, duration:.25}) 1億[count:5000 start=0 ms=1250]万 km
  img#earth(left: 795px; top: 926px; width: 170px; height: 170px; content: @earth; object-fit: contain; delay: 750; in: {scale:.3, opacity:0, duration:.4, ease:'back.out(2.2)'})
  p#pull(left: 350px; top: 1040px; width: 460px; font-size: 54px; text-align: center; white-space: nowrap; in: {x:40, opacity:0, duration:.35, ease:'power2.out'}) ◀── 引力
# hf の作り: 判子は薄めた図の上に重ねる (overlap)
stamp#w_stamp(overlap: w_diag.dist,w_diag.pull; left: 240px; top: 952px; width: 600px; font-size: 92px; c: $ok; bg: #001A12F0; transform: rotate(-8deg); in: {scale:2.2, rotation:-6, opacity:0, duration:.28, ease:'back.out(2.6)'}) 変わらない！
telop#t_why
  tl#a(top: 0px; s: 70px; w: 11) 重力を決めるのは
  tl#b(top: 90px; s: 92px; w: 14) 「{m}質量{/}」と「{d}距離{/}」だけ

# 光: 全面のブラックホールに寄り続け、赤い周辺が心音で脈打ち、光の筋が円盤へ吸い込まれる → 昼の街に替えて 8:20 を数え下ろし、太陽の光が消えて夜になる
section#light
group#l_a.bleed(left: 0px; top: 0px; width: 1080px; height: 1920px; in: none; out: {opacity:0, duration:.25})
  # 光の輪は画面幅の 6 割 (hf と同じ大きさ)・正方の絵を全面に cover で敷くと輪の中心は高さの 41.5% (796px) — 上を空けずに hf の 52% まで下げられないので、光の筋の中心も 531 に合わせる
  img#bh.bleed(inset: 0; content: @blackhole; transform-origin: 49.3% 41.5%; main: none)
  # 吸い込まれる光の筋 14 本: 中心 (360,531) から放射 (筋の中点を角度の向きに 253 px 置いて回す = 左端が中心・群を 136 px 上げて輪の中心に)・群ごと 0.3 倍へ縮めて中心へ吸い込む (hf と同じく約 1.8 s 残す・閉じる印は次の語に置く — 出した語と同じ語で閉じると群の縮みが落ちる)
  group#rays.bleed(left: 0px; top: -204px; width: 1080px; height: 1920px; transform-origin: 50% 52.1%; in: {opacity:0, duration:.15, stagger:{each:.06}}; out: {opacity:0, duration:.15})
    ray#r1(left: 538px; top: 1023px; r: 4deg)
    ray#r2(left: 492px; top: 1180px; r: 29deg)
    ray#r3(left: 378px; top: 1308px; r: 55deg)
    ray#r4(left: 219px; top: 1372px; r: 81deg)
    ray#r5(left: 56px; top: 1362px; r: 106deg)
    ray#r6(left: -90px; top: 1284px; r: 131deg)
    ray#r7(left: -188px; top: 1152px; r: 156deg)
    ray#r8(left: -220px; top: 976px; r: 183deg)
    ray#r9(left: -172px; top: 813px; r: 209deg)
    ray#r10(left: -69px; top: 693px; r: 233deg)
    ray#r11(left: 81px; top: 626px; r: 258deg)
    ray#r12(left: 264px; top: 632px; r: 286deg)
    ray#r13(left: 410px; top: 710px; r: 311deg)
    ray#r14(left: 504px; top: 836px; r: 335deg)
  div#red(inset: 0; background: radial(#780A0A00@40%,#960014A6,50%,42%); opacity: .95; border-radius: 24px; in: none)
  topshade#shade
group#l_b.bleed(left: 0px; top: 0px; width: 1080px; height: 1920px; in: {opacity:0, duration:.25})
  group#ph(left: 0px; top: 0px; width: 1080px; height: 1920px; transform-origin: 60% 12%; in: none)
    img#day(inset: 0; content: @city_day; subject: "0%,0%,100%,100%"; main: none)
    img#night(inset: 0; content: @city_night; subject: "0%,0%,100%,100%"; main: none; in: {opacity:0, duration:.5, ease:'power2.inOut'})
  div#glow.bleed(left: 387px; top: -22px; width: 520px; height: 520px; border-radius: 50%; background: radial(#FFFFFF,#FFFAD7E6@14%,#FFDC7859@40%,#FFC85A00@70%,50%,50%); in: none)
  div#timer(left: 190px; top: 900px; width: 700px; height: 290px; border-radius: 30px; background: #040A18B8; border: 3px solid #FFD43BBF; box-shadow: 0px 12px 36px #0000008C; in: {y:30, opacity:0, duration:.3, ease:'power2.out'}; out: {opacity:0, duration:.4})
    p#lab(left: 0px; top: 16px; width: 700px; text-align: center; font-size: 40px; color: #FFE9A8; white-space: nowrap) 太陽の光が地球に届くまで
    p#num(left: 0px; top: 75px; width: 700px; text-align: center; font-size: 168px; line-height: 1.12; white-space: nowrap) [count:00:00 start=08:20 ms=1930 delay=200]
    # 数え終えた 00:00 を語で赤の 00:00 に差し替える (数える数字の p は recolor の変種に色が乗らない)
    p#num2(left: 0px; top: 75px; width: 700px; text-align: center; font-size: 168px; line-height: 1.12; white-space: nowrap; color: $red; in: none) 00:00
telop#t_light_a
  tl#a(top: 0px; s: 70px; w: 11) ただし…
  tl#b(top: 90px; s: 94px; w: 13) 本当の{r}恐怖{/}はここから
telop#t_light_a2
  tl#a(top: 0px; s: 70px; w: 11) ブラックホールは
  tl#b(top: 90px; s: 104px; w: 15) {s}光{/}を一切出さない
telop#t_light_b(top: 470px)
  tl#a(top: 0px; s: 104px; w: 15; color: $sunc) 8分20秒後
  tl#b(top: 130px; s: 92px; w: 13) 空から太陽が消える

# 凍結: 消灯した街が凍った街へ溶け、霜と青い光が縁から広がり雪が降る・平均気温を数え下ろす (15℃ → −18℃ → −73℃) → 凍った海 → 凍った街の寄り → 宇宙で氷の地球が回り続ける
section#freeze
group#f_a(left: 0px; top: 0px; width: 1080px; height: 1920px; in: none)
  img#city(inset: 0; content: @city_frozen; subject: "0%,0%,100%,100%"; main: kb {scale: [1.12, 1], focus: ['50% 40%', '50% 40%']})
  img#night.bleed(left: -45px; top: -16px; width: 1155px; height: 2055px; content: @city_night; subject: "0%,0%,100%,100%"; main: none; in: none; out: {opacity:0, duration:2.68, ease:'power1.inOut'})
  div#tint(inset: 0; background: #3C8CFF29; mix-blend-mode: screen; border-radius: 24px; in: {opacity:0, duration:2})
  div#frost(inset: 0; background: radial(#C8F0FF00@52%,#CDF2FF80@88%,#EBFAFFCC,50%,50%); border-radius: 24px; in: {opacity:0, duration:2, ease:'power2.out'})
  topshade#shade
particles#f_snow(n: 46; dot: 3-9; color: #F0FAFFE6; drift: down)
group#f_b(left: 0px; top: 0px; width: 1080px; height: 1920px; in: none)
  img#ocean(inset: 0; content: "[photo]Vertical 9:16 cinematic photo of an ocean frozen solid at night with no sun: towering waves frozen mid-motion into jagged translucent blue ice rise from the bottom edge of the frame up to near the top and fill the whole frame, only a thin strip of pitch-black starry sky at the very top edge, frost mist drifting between the ice crests, cold blue and teal tones, low camera close to the frozen waves, no empty sky band"; subject: "0%,0%,100%,100%"; main: none; in: {scale:1.16, duration:.9, ease:'power2.out'})
  div#icy(inset: 0; background: linear(#96D2FF1A,#C8F0FF47,180); mix-blend-mode: screen; border-radius: 24px)
  div#frost(inset: 0; background: radial(#C8F0FF00@50%,#D7F5FF8C@90%,#F0FCFFD9,50%,50%); border-radius: 24px)
  topshade#shade
group#f_a2(left: 0px; top: 0px; width: 1080px; height: 1920px; in: none)
  img#city.bleed(left: -64px; top: -142px; width: 1209px; height: 2151px; content: @city_frozen; subject: "0%,0%,100%,100%"; transform-origin: 50% 62%; main: none; in: {scale:1.18, duration:1, ease:'power2.out'})
  topshade#shade
# 宇宙の場面: カメラが 1.35 倍から引き、氷の地球が楕円を回る (x の群 → y の群 → 地球)
group#f_c(left: 0px; top: 0px; width: 1080px; height: 1920px; in: {opacity:0, duration:.35})
  # hf の #f-c は地が黒 (下の凍った街を透かさない)
  div#void(inset: 0; background: #000000; border-radius: 24px)
  img#space(inset: 0; content: @space; opacity: .55; main: none)
  group#cam(left: 0px; top: 0px; width: 1080px; height: 1920px; transform-origin: 50% 53.7%; in: {scale:1.35, duration:4.63, ease:'power1.out'})
    img#bh(left: 372px; top: 862px; width: 336px; height: 336px; content: @bh_disc; object-fit: contain; opacity: .9)
    shape#orbit(left: 160px; top: 900px; width: 760px; height: 260px; border-radius: 50%; background: none; border: 3px solid #A0D7FF47)
    group#ox(left: 0px; top: 0px; width: 1080px; height: 1920px; main: sine {x: 380, period: 6.17, phase_offset: 0.441})
      group#oy(left: 0px; top: 0px; width: 1080px; height: 1920px; main: sine {y: 130, period: 6.17, phase_offset: 0.191})
        img#earth(left: 462px; top: 952px; width: 156px; height: 156px; content: @earth_ice; object-fit: contain; main: sine {scale: 0.17, period: 6.17, phase_offset: 0.191})
  topshade#shade
# 気温のテロップ: 上の札を語で差し替え、数字を数え下ろして弾ませる
# hf の作り: 凍った街の写真は 2 回使う (duplicate_media)・消灯した街の写真を凍った街に重ねて溶かす (photo_hidden)
telop#t_freeze_a
  tl#l(top: 0px; s: 70px; w: 11) いまの平均気温
  tl#n(top: 86px; s: 190px; w: 17; color: $ice) [count:-18 start=15 ms=2380]℃
  tl#n2(top: 86px; s: 190px; w: 17; color: $ice; in: none) [count:-73 start=-18 ms=1260]℃
telop#t_freeze_b
  tl#a(top: 0px; s: 92px; w: 13) 海も街も
  tl#b(top: 110px; s: 104px; w: 15; color: $ice) 凍りつく
telop#t_freeze_c
  tl#a(top: 0px; s: 70px; w: 11) 地球は
  tl#b(top: 90px; s: 104px; w: 15) 「{i}氷の星{/}」に

# 安心: 地球の夜明けに暖かい光 → 暗く沈めて「ブラックホールになる星」と「太陽」を並べ、判子「永遠に来ない」→ 眠る人の写真に Z が 3 つ浮かぶ
section#relief
group#r_a(left: 0px; top: 0px; width: 1080px; height: 1920px; in: none)
  img#sunrise(inset: 0; content: "[photo]Cinematic photo of a warm, gentle sunrise seen from space over the curved horizon of planet Earth, a soft golden sun peeking over the blue atmosphere glow near the center, thin clouds below, horizon in the lower third, hopeful, calm and reassuring"; main: kb {scale: [1.14, 1], focus: ['50% 52%', '50% 52%']})
  div#glow(inset: 0; background: radial(#FFC87873,#FFAA5000@45%,50%,52%); border-radius: 24px; delay: 200; in: {opacity:0, duration:1.2, ease:'power2.out'})
  div#dim(inset: 0; background: #040610A8; border-radius: 24px; in: {opacity:0, duration:.35})
  topshade#shade
group#r_b(left: 0px; top: 0px; width: 1080px; height: 1920px; in: {opacity:0, duration:.2})
  div#star(left: 490px; top: 770px; width: 460px; height: 460px; border-radius: 50%; background: radial(#FFFFFF,#DFF3FF@22%,#8FD0FF@50%,#3C7DFF@74%,#285AFF00,42%,40%); box-shadow: 0px 0px 80px 20px #78BEFF73; in: {scale:0, duration:.5, ease:'back.out(1.6)'})
  img#sun(left: 195px; top: 945px; width: 190px; height: 190px; content: @sun; object-fit: contain; in: {scale:0, duration:.45, ease:'back.out(1.8)'})
  lab#l1(left: 110px; top: 1142px; width: 360px; font-size: 52px) 太陽
  lab#l2(left: 70px; top: 1218px; width: 440px; font-size: 46px; color: #FF4F63) 質量が足りない
  lab#l3(left: 435px; top: 1240px; width: 570px; font-size: 46px) ブラックホールになる星
  lab#l4(left: 435px; top: 1302px; width: 570px; font-size: 42px; color: #9FD8FF) 太陽の数十倍の質量
  stamp#stamp(left: 250px; top: 540px; width: 580px; font-size: 80px; line-height: 1.5; c: $red; bg: #280008B8; transform: rotate(6deg); in: {scale:2.2, rotation:4, opacity:0, duration:.28, ease:'back.out(2.6)'}) 永遠に来ない
group#r_c(left: 0px; top: 0px; width: 1080px; height: 1920px; in: {opacity:0, duration:.5, ease:'power1.inOut'})
  img#sleep(inset: 0; content: @sleep; main: kb {scale: [1.06, 1], focus: ['50% 45%', '50% 45%']})
  topshade#shade
  p#z(left: "507;547;593"; top: "373;313;240"; width: 150px; font-family: d; font-size: "43;56;69"; color: #FFF3C9; text-shadow: 0px 0px 18px #FFDC96E6; in: {y:30, opacity:0, duration:.35, ease:'power2.out'}) ×3 Z;Z;Z
telop#t_relief_a
  tl#a(top: 0px; s: 70px; w: 11) でも…
  tl#b(top: 90px; s: 104px; w: 15; color: $warm) 安心してください
telop#t_relief_b
  tl#a(top: 0px; s: 92px; w: 13) 太陽は軽すぎて
  tl#b(top: 116px; s: 82px; w: 13) ブラックホールに{r}なれない{/}
telop#t_relief_c
  tl#a(top: 0px; s: 70px; w: 11) 今夜も
  tl#b(top: 90px; s: 104px; w: 15; color: $warm) ぐっすり

# 誘導: ぼかした寝顔の上にプロフィールの札 (丸い icon・名前・赤いフォローの釦) が下から弾み、icon に輪・釦を押すと「フォロー中 ✓」に替わる
section#cta
img#c_bg(inset: 0; content: @sleep; filter: blur(36px) brightness(.6); main: none)
div#c_card(left: 110px; top: 760px; width: 860px; height: 470px; border-radius: 40px; background: #0A0E1CDB; border: 3px solid #FFFFFF2E; box-shadow: 0px 20px 60px #00000099; delay: 100; in: {y:90, opacity:0, duration:.5, ease:'back.out(1.6)'})
  img#avatar(left: 60px; top: 60px; width: 190px; height: 190px; border-radius: 50%; border: 6px solid $chip; content: @blackhole; object-fit: cover; object-position: 49% 39%; zoom: 250%)
  p#name(left: 290px; top: 92px; width: 540px; font-size: 54px; white-space: nowrap) 宇宙の思考実験ラボ
  p#handle(left: 292px; top: 170px; width: 510px; font-size: 36px; color: #AAB4C8; white-space: nowrap) @uchu_shiko_lab
  p#follow(left: 60px; top: 310px; width: 740px; font-size: 52px; line-height: 1.35; text-align: center; padding: 20px 0px; border-radius: 148px; background: linear(#FF4560,#E0002A,180); box-shadow: 0px 10px 26px #FF285073; out: {opacity:0, duration:.15}) フォローする
  shape#tap(left: 370px; top: 304px; width: 120px; height: 120px; border-radius: 50%; background: none; border: 8px solid #FFFFFFF2; in: {scale:.3, duration:.03, ease:'none'})
  p#following(left: 60px; top: 310px; width: 740px; font-size: 52px; line-height: 1.35; text-align: center; padding: 20px 0px; border-radius: 148px; background: #2B3242; color: #D9DFEB; in: {opacity:0, duration:.15}) フォロー中 ✓
p#c_arrow(left: 150px; top: 1262px; width: 780px; font-size: 46px; text-align: center; color: $chip; white-space: nowrap; in: {opacity:0, duration:.3, ease:'power2.out'}) ▲ アイコンからプロフィールへ
telop#t_cta
  tl#a(top: 0px; s: 70px; w: 11) ほかの思考実験は
  tl#b(top: 90px; s: 104px; w: 15) プロフィールから！
```

```timeline.txt
#v2
cast n = "知的でテンポのよい若い男性ナレーター、落ち着いた低めの声にスピード感と宇宙の静かな緊張感をにじませる"
silence head=0 tail=0
transition = dissolve,300,overlap=300

*** hook
[>#subtitle]
bgm music
@n: [silence:450][♪doom +4dB -450][♪riser -4dB -450 start=1.02s][!#h_sun to,{scale:1.06, duration:2.44, ease:'none'} -450][!#h_sun.img to,{rotation:4, duration:2.5, ease:'none'} -450][!#h_sun.glow to,{opacity:.45, duration:.55, ease:'sine.inOut', repeat:3, yoyo:true} -450][!#t_hook to,{scale:1.035, duration:1.6, ease:'sine.inOut', repeat:3, yoyo:true}]もしも太陽が突然、[|][!#h_sun to,{scale:.012, rotation:28, duration:.85, ease:'power3.in'} +373][!#h_sun.core to,{opacity:1, scale:1.6, duration:.85, ease:'power2.in'} +373][♪bighit +7dB +1063][>#h_flash +1183][!#h_flash to,{opacity:0, duration:.55, ease:'power2.out'} +1233][<#h_sun none +1203][>#h_bh +1223][!#h_bh to,{rotation:14, duration:4.4, ease:'none'} +1223][>#h_ring +1223][!#h_ring to,{scale:6.5, opacity:0, duration:1, ease:'power2.out'} +1223][!#h_space shake,18,duration=500 +1223][!#h_bh shake,18,duration=500 +1223]同じ質量の{y}ブラックホール{/}に[|][>#h_label +132][♪comet +612]なったらどうなる？[|][♪suck -3dB -186 start=5s to=8.2s fade=300,800][<#h_label -50][>#h_earth -50][!#h_earth to,{x:-420, y:123, scale:.921, rotation:23, duration:.477, ease:'none'} -50][!#h_earth to,{x:-855, y:-162, scale:.78, rotation:65, duration:.318, ease:'none'} +427][!#h_earth to,{x:-320, y:-282, scale:.569, rotation:127, duration:.318, ease:'none'} +745][!#h_earth to,{x:-471, y:-118, scale:.366, rotation:187, duration:.239, ease:'none'} +1063][!#h_earth to,{x:-477, y:-182, scale:.12, rotation:260, opacity:0, duration:.239, ease:'none'} +1302]地球は一瞬で{y}吸い込まれる{/}…[|][>#h_q][>#h_rew +150][!#h_earth to,{x:-322, y:-152, scale:.472, rotation:156, opacity:1, duration:.5, ease:'power1.in'} +150][!#h_earth to,{x:-666, y:-336, scale:.692, rotation:91, duration:.47, ease:'power1.out'} +650][!#h_bh shake,x=4,y=0,duration=600 +150][<#h_q +850][♪doom +7dB +850]と思っていませんか？[silence:220]
transition cut

*** shock
@: [silence:330][>#s_flash -330][!#s_flash to,{opacity:0, duration:.3, ease:'power2.out'} -290][!#s_space shake,16,duration=400 -330][!#s_bh shake,16,duration=400 -330][!#s_orb.oy.earth main,square,alpha=1,freq_ms=4804,phase_offset=0.024 +20][!#s_orb_b.oy_b.earth_b main,square,alpha=-1,freq_ms=4804,phase_offset=0.024 +20][>#s_c1 +250]実は、質量が変わらないため[|][>#s_c2][♪camera -3dB +786]{y}重力もそのまま{/}。[|][<#s_c1 -120][<#s_c2 -120][>#s_c3]地球は{y}吸い込まれず{/}、[|][>#s_c4][!#s_orbit .bold][=#s_orbit +300][♪comet2 +1dB +828]これまで通り{y}公転{/}を続けます。[silence:200]
transition dissolve,300,overlap=300

*** why
@: [silence:200]重力の強さを決めるのは、[|][!#w_formula{m} punch,1.25,duration=360][!#w_diag.sun punch,1.12,duration=400][>#w_diag.dline +400][>#w_diag.dlab +400][!#w_diag.dlab punch,1.15,duration=360 +450][!#w_formula{d} punch,1.25,duration=360 +450]{y}質量と距離{/}だけ。[|][♪suck -5dB -31 start=6s to=8.3s fade=400,500][>#w_diag.radius +50][!#w_diag.sun to,{scale:.05, rotation:90, duration:2.18, ease:'power3.in'} +500]太陽が半径わずか[|][♪impact +3dB +545][>#w_diag.bh +1206][<#w_diag.name none +1156][<#w_diag.sun none +1256][>#w_diag.name2 +1276][!#w_diag.radius punch,1.12,duration=300 +1256]{y}{3キロ|さんキロ}{/}に縮んでも、[|][♪sweep -3dB -26][<#w_diag.dlab -50][>#w_diag.line][>#w_diag.dist][<#w_diag.dline +900][!#w_diag.earth punch,1.15,duration=360 +1150]{y}{1億5000万キロ|いちおくごせんまんキロ}{/}離れた[|][>#w_diag.pull][!#w_diag.pull to,{x:-21, duration:.35, repeat:3, yoyo:true, ease:'sine.inOut'} +400]地球が受ける引力は、[|][♪click -1dB -91][!#w_diag to,{opacity:.32, duration:.25} -50][>#w_stamp][♪impact +7dB +779]{y}まったく変わりません{/}。[silence:220]
transition dissolve,120,overlap=120

*** light
@: [silence:330][♪drone -7dB -288 to=5s fade=0,2000][♪heart -88 to=4.6s fade=0,1200][!#l_a.bh to,{scale:1.129, rotation:5, duration:5.3, ease:'none'} -330][!#l_a.bh shake,12,duration=350 -280][!#l_a.red pulse,5,opacity=0.35>0.95,duration=950 -80]ただし、{y}本当の恐怖{/}はここから。[|][<#t_light_a none -50][>#t_light_a2 -50][>#l_a.rays][!#l_a.rays to,{scale:.3, duration:1.6, ease:'power2.in'} +200]{y}ブラックホール{/}は、[|][<#l_a.rays +850]{y}光を一切出しません{/}。[|][♪tick -2dB -2 to=2.3s][<#t_light_a2 none -50][>#t_light_b -50][>#l_b -50][<#l_a +150][!#l_b.ph to,{scale:1.07, duration:4.05, ease:'none'} -50][!#l_b.glow to,{scale:1.15, duration:.25, repeat:3, yoyo:true, ease:'sine.inOut'} -50][>#l_b.timer +100]{y}{8分20秒後|はっぷんにじゅうびょうご}{/}、[|]地球の空から[|][<#l_b.timer.num none -50][>#l_b.timer.num2 -50][♪bighit +4dB +308][!#music to,{volume:-13dB, duration:.1} +308][!#music to,{volume:0dB, duration:.1} +1408][!#l_b.glow to,{scale:.01, opacity:0, duration:.4, ease:'power3.in'} +300][>#l_b.ph.night +450][<#l_b.timer +800][<#t_light_b none +1500]{y}太陽が消える{/}のです。[silence:220]
transition dissolve,450,overlap=450

*** freeze
@: [silence:330][♪wind -4dB -230 to=12s fade=1000,1200][<#f_a.night +300][>#f_a.tint +800][>#f_a.frost +800][♪ice +3dB +370][!#t_freeze_a.l text,"1週間後" +600][!#t_freeze_a.n count +650]わずか{1週間|いっしゅうかん}で、[|]地球の平均気温は[|][♪sweep -1dB +44][!#t_freeze_a.n punch,1.12,duration=240 +450]{y}{マイナス18度|マイナスじゅうはちど}{/}。[|][!#t_freeze_a.l text,"1年後" +20][<#t_freeze_a.n none +100][>#t_freeze_a.n2 +100][!#t_freeze_a.n2 count +100]{1年後|いちねんご}には、[|][♪impact -1dB +21][♪sweep +201][!#t_freeze_a.n2 punch,1.16,duration=280 +550][!#f_a shake,8,duration=300 +500][♪camera -1dB +1091]{y}{マイナス73度|マイナスななじゅうさんど}{/}。[|][<#t_freeze_a none][>#t_freeze_b][>#f_b][<#f_snow none][>#f_a2 +720][♪sweep -3dB +700]海も街も{y}凍りつき{/}、[|][<#t_freeze_b none][>#t_freeze_c][>#f_c -100]地球は漆黒の宇宙を[|]ひとり回り続ける、[|][♪sparkle +1dB +1283]{y}氷の星{/}になります。[silence:400]
[<#music]
transition dissolve,600,overlap=600

*** relief
bgm piano -270
@: [silence:400]でも、{y}安心してください{/}。[|][<#t_relief_a none][>#t_relief_b][>#r_a.dim -100][>#r_b -100][>#r_b.star][>#r_b.l3 +200][>#r_b.l4 +450]太陽は{y}ブラックホール{/}になるには[|][>#r_b.sun -150][>#r_b.l1 -50][>#r_b.l2 +200][!#r_b.sun shake,x=5,y=0,duration=400 +350]{y}軽すぎる{/}ため、[|][♪click -3dB -4][>#r_b.stamp +100]そんな日は{y}永遠に来ません{/}。[|][♪sparkle -5dB -134][<#t_relief_b none][>#t_relief_c][>#r_c -50][<#r_b none +450][>#r_c.z[1] +250][>#r_c.z[2] +600][>#r_c.z[3] +950][!#r_c.z[1] to,{y:-40, duration:1.6, ease:'sine.inOut'} +600][!#r_c.z[2] to,{y:-40, duration:1.6, ease:'sine.inOut'} +950][!#r_c.z[3] to,{y:-40, duration:1.6, ease:'sine.inOut'} +1300]今夜も、{y}ぐっすり{/}眠れますね。[silence:200]
transition dissolve,350,overlap=350

*** cta
@: [silence:200][♪sweep -3dB -185]ほかの思考実験は、[|][>#c_arrow -100][!#c_card.avatar ping,$chip,3,interval=800,duration=800,scale=1>1.35][!#c_arrow to,{y:-12, duration:.3, repeat:5, yoyo:true, ease:'sine.inOut'} +200][♪click +1dB +77][>#c_card.tap +150][!#c_card.tap to,{scale:1.6, opacity:0, duration:.45, ease:'power2.out'} +150][!#c_card.follow punch,0.94,duration=160 +150][<#c_card.follow +310][>#c_card.following +310]{y}プロフィール{/}からチェック！[silence:1.5s]
```

# story · monday-blues (hf 全力版の全量の写し — 日曜夜〜月曜朝の絶望あるある5選・常設の題の帯と番号の札で数える 5 項目の判子と見出し) — canvas 1080x1920

見せる作り: 常設の層 (紺の題の帯に流れる斜めの縞・番号の札 5 つが項目ごとに黄 → 赤・下半分の暗いグラデ・周辺減光)・1 つ目から跨ぐ時計の札 (曜日の色札と時刻を語で差し替え・深夜 2 時で赤く脈打つ)・震える前置きと白の閃光で叩きつける題 (つかみ)・項目ごとの 3 拍の組 (星形の判子が弾んで落ち、白い板の見出しが傾いて着地)・項目ごとのギャグ (数え減る札と吹き出し・擬音・伸び縮みする体温計と判定・落ちてくる「重力 ×10」と足元の寄りの丸窓・数え上がる残り時間 → 白黒と縦縞で沈める)・向きを替える押し出しと閃光つきの寄りの切替・句ごとに弾む縁取りの字幕・音の層 (語に結んだ効果音 20 余り + 切替の風切り)

```design.txt
#v2
# 学ぶ作り: 全編に敷く常設の層 (上の紺の題の帯 = 斜めの縞が流れる地・赤の前置き・黄の「5選」・番号の札 5 つが項目ごとに黄 → 赤へ・下半分を沈める暗いグラデ) と、1 つ目から跨ぐ左上の時計の札 (曜日の色札 + 時刻を語ごとに差し替え・深夜 2 時で赤に脈打つ)
# 項目の cut は同じ 3 拍の組: 星形の判子「N つ目！」が回って弾み → 0.5 秒で下へ落ちて消え → 白い板の見出し (赤丸の番号 + 2 段・決め語は赤) が傾いて着地
# 項目ごとのギャグを 1 つずつ語に結ぶ: 数え減る残り時間の札と「……」の吹き出し・「スッ」の擬音・体温計が上がって下がる + 「ペタ」+ 平熱の判定・落ちてくる「重力 ×10」と足元の寄りの丸窓 + 「ズシッ」・数え上がる「あと 105 時間」→ 白黒に沈めて縦縞の陰
# hf b07 monday-blues (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3。切替は項目ごとに向きを替えた押し出しと、白の閃光つきの寄り (3 つ目・5 つ目)
canvas 1080x1920 bg=#05060F
theme dark
palette navy=#0B0F2A y=#FFD400 red=#E60033 pink=#FF2D55 rose=#FF3B5C blue=#2F6BFF ink=#111111 night=#05060F hy=#FFE100 ice=#DFE8FF sky=#BFE3FF peta=#FFCF33
# 書体は font を書かない既定の太い角ゴシック (hf の書体と同じ系統)
sfx off
# hf の作り: 判子・擬音・時計の時刻は 0.3〜0.7 秒で入れ替わる (flash_text)・cut 末の 0.8 秒の中で出る擬音と吹き出し (entrance_in_fadeout)・題の帯は最後の frame まで残る (title_on_close)
# hf の作り: 4 つ目は同じ絵を全面と寄りの丸窓に出す (duplicate_media)・見出しの板は台詞より先に項目の要を見せる (spoiler)
# hf の作り: 2 つ目は時計の刻み・ツッコミ・スワイプ 2 回が 5 秒に重なる (se_dense)
lint off=flash_text,entrance_in_fadeout,title_on_close,duplicate_media,spoiler,se_dense
# hf の作り: 体温計の目盛りは管の左へ食み出す (child_overflow)・2 つ目の「ペタ」は目盛りの 37 に、2 つ目の「ズシッ」は見出しの番号に掛かる (overlap)
# 判子の黒字 (黄の星の上) と全面の周辺減光の幕を比べた low_contrast は残る (判子の地は星の svg で、幕の濃さでは沈まない)
master lufs=-15 tp=-1.5
prompt_tail "日本のテレビアニメ調のセル塗りイラスト、太く綺麗な主線、コミカルな漫画的誇張表現。縦長の構図で、人物の顔と上半身は画面の上から35〜60%の高さに大きく配置し、画面の上端15%と下端30%は背景だけのシンプルな余白にする。文字・数字・ロゴ・透かし・吹き出しは一切描かない。"
image tsukio = "日本のテレビアニメ調のキャラクター設定画。25歳の日本人男性会社員。ぼさっとした黒髪の短髪、眠そうなタレ目、目の下にうっすらクマ、細身で猫背気味。グレーのパーカーに黒いスウェットパンツ。正面向きの膝上までの立ち姿、少し疲れたニュートラルな表情。背景は真っ白の無地。"
# 4 つ目の絵は全面と寄りの丸窓の 2 か所に出すので根に 1 枚
image walk = "[ref:@tsukio]月曜の朝、どんよりした灰色の曇り空の下の住宅街の歩道。紺色のスーツにリュックを背負った彼が、遠くに見える駅へ向かって前かがみで一歩一歩足を引きずるように歩いている。両足首には鎖でつながった重そうな黒い鉄球（コミカルな比喩表現）、踏みしめたアスファルトにひび、背中から黒いどんよりしたオーラが立ち上る。周囲は彩度の低い灰色で、彼だけ色がはっきりしている。" aspect=9:16
run y { color: $y }
run five { color: $pink; font-size: 172px }
run l2 { font-size: 96px }
run l2r { font-size: 96px; color: $red }
sound gaan = "ガーンという漫画的なショックの衝撃音"
sound jan = "ジャン！という短く鋭い驚きのアクセント音"
sound tick = "時計の秒針がチクタク刻む乾いた音"
sound chiin_s = "お鈴をチーンと短く打つ音"
sound tsukkomi = "ツッコミのハリセンのような乾いた軽い打撃音"
sound swipe = "スマホの画面を指でスッと払う軽い音"
sound pat = "手のひらでおでこをペタッと軽く叩く音"
sound impact = "ズドンと重く響く低音の衝撃音"
sound step = "重くゆっくり踏みしめる鈍い足音"
sound thud = "短く鈍いドスッという打撃音"
sound digital = "電子音のデジタルカウントダウンのピピピという連続音"
sound piano = "ピアノの低音をジャーンと叩く衝撃と絶望の音"
sound chiin = "低く沈んだお鈴のチーンという余韻の長い音"
# 判子の星形 (hf の 36 頂点の polygon そのまま)・時計の icon
svg burst = """<svg viewBox="-160 -160 320 320"><polygon points="0.0,-150.0 19.4,-110.3 51.3,-141.0 56.0,-97.0 96.4,-114.9 85.8,-72.0 129.9,-75.0 105.2,-38.3 147.7,-26.0 112.0,0.0 147.7,26.0 105.2,38.3 129.9,75.0 85.8,72.0 96.4,114.9 56.0,97.0 51.3,141.0 19.4,110.3 0.0,150.0 -19.4,110.3 -51.3,141.0 -56.0,97.0 -96.4,114.9 -85.8,72.0 -129.9,75.0 -105.2,38.3 -147.7,26.0 -112.0,0.0 -147.7,-26.0 -105.2,-38.3 -129.9,-75.0 -85.8,-72.0 -96.4,-114.9 -56.0,-97.0 -51.3,-141.0 -19.4,-110.3" fill="#ffd400" stroke="#111" stroke-width="10" stroke-linejoin="round"/></svg>"""
svg clock = """<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="16" fill="none" stroke="#fff" stroke-width="4"/><line x1="20" y1="20" x2="20" y2="9" stroke="#fff" stroke-width="4" stroke-linecap="round"/><line x1="20" y1="20" x2="28" y2="24" stroke="#fff" stroke-width="4" stroke-linecap="round"/></svg>"""
cut { stagger: 0ms }
p { out: none }
div { border: none; out: none }
img { in: none; out: none }
bgm#music(fade: 120,1100) テンポが速くコミカルで慌ただしい、焦りを煽るドタバタのBGM
# 字幕: 白の太字 + 黒の太い縁・中央・句ごとの札 (hf の割り方を [|] で)・札は縮んだ所から弾んで出て、次の札まで残る
subtitle(left: 0px; top: 1392px; width: 1080px; font-size: 72px; line-height: 1.2; color: #FFFFFF; -webkit-text-stroke: 10px #111111; background: none; text-align: center; unit: segment; lead: 0ms; tail: 0ms; hold: next,800ms; in: {scale:.86, opacity:0, duration:.09, ease:'back.out(2.5)'}; out: {opacity:0, duration:.05})
subtitle.small(font-size: 66px)

# 星形の判子「N つ目！」(-8° に傾けて置き、-30° の 0.2 倍から 1.12 倍へ弾んで 1 倍に・退場は縮みながら下の見出しへ落ちる)・出ている間は字幕を消す
def stamp(n) = div(left: 36px; top: 452px; width: 340px; height: 340px; transform: rotate(-8deg); hide_subtitle: true; in: keys(at=0 scale=0.2 rotation=-22 opacity=0 | at=0.57 scale=1.12 opacity=1 ease=back(3) | at=1 ease=power1.out),duration=280; out: {scale:.3, x:-60, y:560, opacity:0, duration:.16, ease:'power2.in'})
  svg#burst(left: 10px; top: 10px; width: 320px; height: 320px; part: burst)
  p#n(cx: 50%; top: 74px; font-size: 150px; line-height: .91; color: $ink; content: {n})
  p#s(cx: 50%; top: 210px; font-size: 50px; line-height: 1.1; color: $ink) つ目！
# 見出しの板 (白地・黒の太い縁・硬い影・2 段目は大きく決め語は赤) + 左上に食み出す赤丸の番号 (丸い札の文字 1 つ・板の左端に位置の式で付ける)。群ごと -1.5° で 1.35 倍から着地
def headline(c, n) = group(left: 0px; top: 1090px; width: 1080px; height: 255px; transform: rotate(-1.5deg); in: {scale:1.35, rotation:3.5, opacity:0, duration:.2, ease:'back.out(2.2)'}; out: {y:40, opacity:0, duration:.1, ease:'power1.in'})
  p#card(cx: 50%; top: 0px; font-size: 64px; line-height: 1.18; color: $ink; text-align: center; background: #FFFFFF; border: 8px solid $ink; border-radius: 20px; padding: 22px 46px 26px 104px; box-shadow: 12px 12px 0px $ink; content: {c})
  p#num(left: .card.left-24; top: -38px; width: 98px; font-size: 70px; line-height: 1; padding: 14px 0px; text-align: center; color: #FFFFFF; background: $red; border: 8px solid $ink; border-radius: 148px; overlap: .card; content: {n})
# 黒の縁取りの擬音 (スッ・ペタ・ズシッ)
def ono(t, w, s=53, c=#FFFFFF) = p(width: {w}; font-size: {s}; line-height: 1.25; color: {c}; -webkit-text-stroke: 9px $ink; content: {t})
# 場面の絵 (題の帯の裏 180 から下端までの枠・絵ごとに寄る kb — 語で下へ沈めても帯との間に隙が出ないよう帯の裏まで敷く)
def scene() = img(left: 0px; top: 270px; width: 1080px; height: 1650px; z-index: back)

# 常設の層: 題の帯 (紺の地 + 下に黄の線 + 影・白の斜めの縞が全編で左へ流れる)・前置き・題・番号の札 5 つ
div#header(left: 0px; top: 0px; width: 1080px; height: 330px; background: $navy; border-bottom: 6px solid $y; box-shadow: 0px 10px 24px #0000008C; z-index: front; border-radius: 24px; in: none)
div#stripes.bleed(left: -200px; top: 0px; width: 1500px; height: 324px; pattern: hatch,-45,#FFFFFF0B,48,24; z-index: front; border-radius: 24px; in: none; main: ramp {x: -160})
p#hd_kicker(cx: 540px; top: 86px; font-size: 46px; color: $rose; letter-spacing: .04em; z-index: front; in: none) 【毎週の悪夢】
p#hd_title(left: 0px; top: 144px; width: 1080px; font-size: 80px; line-height: 1.25; text-align: center; color: #FFFFFF; -webkit-text-stroke: 8px $ink; z-index: front; in: {scale:1.12, duration:.32, ease:'back.out(2)'}) 月曜日が嫌すぎる瞬間{y}5選{/}
# 番号の札: 淡い枠で並び、項目の頭で黄 (.on)・次の項目で赤 (.done)
p#pc(left: "344;426;509;591;674"; top: 262px; width: 64px; font-size: 32px; line-height: 1; padding: 6px 0px; text-align: center; color: #FFFFFFBF; background: #FFFFFF0F; border: 3px solid #FFFFFF73; border-radius: 12px; z-index: front; in: {scale:.4, opacity:0, duration:.18, ease:'back.out(3)', stagger: {each: .06}}) ×5 1;2;3;4;5
#pc.on(background: $y; color: $ink; border: 3px solid $y)
#pc.done(background: #FF3B5CD9; color: #FFFFFF; border: 3px solid #FF3B5CD9)
# 全編の周辺減光 (場面の絵の直上) と、下半分を沈める暗いグラデ (字幕と見出しの地)
veil#vig(vignette: 0.5; in: none)
div#bottomfade(left: 0px; top: 960px; width: 1080px; height: 960px; background: linear(#05061400,#05061480@32%,#050614D1@62%,#050614E6,180); border-radius: 24px; in: none)

# つかみ: 日曜の夜に絶望する彼。青い縦縞の陰が上から降り、震える「明日が来るな…」→ 白の閃光と一緒に「月曜の絶望 あるある5選」が叩きつけられ、番号の札が並ぶ
section#hook
scene#p0(in: {scale:1.14, duration:.38, ease:'power3.out'}; main: kb {scale: [1, 1.08], focus: ['33% 36%', '33% 36%']}) [ref:@tsukio]日曜の夜、薄暗いワンルームの部屋。グレーのパーカー姿の彼が床に体育座りし、壁に掛かったカレンダーの赤丸のついたマスを見つめ、真っ青な顔で絶望している。顔の上半分に縦線の影（ガーンという漫画表現）、大粒の冷や汗。窓の外は真っ暗な夜。部屋全体は青紫の暗いトーンで、カレンダーだけがスポットライトのように白く浮かび上がる。
div#gloom0(left: 0px; top: 330px; width: 1080px; height: 900px; pattern: hatch,0,#283CBE8C,19,3; mask-image: linear-gradient(180deg, #000000 0%, #000000D9 55%, #00000000 100%); opacity: .9; border-radius: 24px; in: {scaleY:.2, opacity:0, duration:.35, ease:'power2.out', pivot:'top'}; out: {opacity:0, duration:.5, ease:'power1.in'})
p#hook1(cx: 540px; top: 1000px; font-size: 100px; color: $ice; -webkit-text-stroke: 10px $ink; text-shadow: 0px 0px 26px #5078FFE6; in: {scale:1.25, duration:.3, ease:'back.out(2.2)'}; main: noise {x: 4, y: 4, period: 0.06, window: '320ms,2900ms'}) 明日が来るな…
p#hook2(left: 0px; top: 1110px; width: 1080px; font-size: 142px; line-height: 1.12; color: $hy; text-align: center; -webkit-text-stroke: 12px $ink; text-shadow: 10px 10px 0px $red; hide_subtitle: true; overlap: subtitle; in: {scale:1.6, opacity:0, duration:.2, ease:'back.out(2.4)'}) 月曜の絶望[br]あるある{five}5選{/}
veil#fl0(color: #FFFFFF; opacity: .55; z-index: curtain; in: none)

# 1 つ目: 夕日のリビング。左上の時計の札が入り (日 18:30)、残り時間の札が数え減り、「……」の吹き出しがしぼむ
section#one
scene#p1(main: kb {scale: [1, 1.08], focus: ['42% 24%', '42% 24%']}) [ref:@tsukio]日曜の夕方6時半、リビングのソファ。グレーのパーカー姿の彼がソファに座り、片手で胃のあたりを押さえ、口を真一文字に結んで青ざめた顔でテレビを見つめている。テレビ画面には夕焼けの街並みと家族のシルエットが歩く穏やかなアニメのエンディング風の映像（特定の作品やキャラクターは描かない）。窓から差し込む濃いオレンジの夕日と長い紫の影、哀愁とコミカルさ。
stamp#st1(n: 1)
headline#hl1(c: "サザエさんのエンディングで[br]{l2r}胃が痛む{/}"; n: 1)
# 時計の札 (sticky・最後まで): 時計の icon + 曜日の色札 (日 = 赤 / 月 = 青) + 時刻。深夜 2 時で丸い札ごと赤 (赤い地の子 al は透明で札と一緒に出し、2 つ目の語で to で灯して 3 つ目の頭で消す — 後の cut で初めて出すと確定済みの前の cut を書き換える)
div#clock.sticky(left: 34px; top: 362px; width: 300px; height: 78px; border-radius: 39px; background: #080A1EB8; border: 3px solid #FFFFFF59; in: {x:-40, opacity:0, duration:.22, ease:'back.out(2)'})
  div#al(left: 0px; top: 0px; width: 300px; height: 78px; border-radius: 39px; background: #E60033EB; border: 3px solid #FFFFFF59; opacity: 0; out: {opacity:0, duration:.2})
  svg#ico(left: 18px; top: 20px; width: 40px; height: 40px; part: clock)
  p#day(left: 70px; cy: 50%; width: 52px; font-size: 36px; line-height: 1; padding: 8px 0px; text-align: center; background: $red; border-radius: 10px) 日
  p#hm(left: 135px; cy: 50%; font-size: 50px; line-height: 1; letter-spacing: .02em) 18:30
# 休日終了までの札 (赤の縁と光・秒が 59 → 52 へ数え減る)
div#cd(left: 640px; top: 366px; width: 400px; height: 162px; border-radius: 18px; background: #0A0814D1; border: 4px solid $pink; box-shadow: 0px 0px 30px #FF2D5580; in: {scale:.6, y:-20, opacity:0, duration:.18, ease:'back.out(2.5)'})
  p#l(cx: 50%; top: 14px; font-size: 38px; line-height: 1.2; color: $y) 休日終了まで
  p#d(cx: 50%; top: 66px; font-size: 82px; line-height: 1; color: $pink; letter-spacing: .02em; text-shadow: 0px 0px 18px #FF2D55CC) 05:29:[count:52 start=59 ms=1660ms delay=50ms]
# 「……」の吹き出し (左下の尻尾・弾んで出てしぼむ)
p#bub(left: 600px; top: 560px; width: 250px; font-size: 70px; line-height: 1; color: $ink; text-align: center; background: #FFFFFF; border: 6px solid $ink; padding: 34px 0px; shape: rounded-speech-bubble; in: {scale:.3, opacity:0, duration:.16, ease:'back.out(3)'}) ……

# 2 つ目: 深夜の寝室でスマホ。時計の札が 23:00 → 2:00 まで刻んで赤に脈打ち、「スッ」が 2 回流れる
section#two
scene#p2(main: kb {scale: [1, 1.08], focus: ['48% 27%', '48% 27%']}) [ref:@tsukio]深夜2時の真っ暗な寝室。ベッドで布団にくるまったグレーのパーカー姿の彼が、スマホの青白い光に顔だけを照らされ、充血した目を大きく見開いて画面を凝視している。目の下に濃いクマ。枕元には文字盤を簡略化した目覚まし時計とお菓子の空き袋。部屋は濃紺の闇で、スマホの光だけが強く輝く。
stamp#st2(n: 2)
headline#hl2(c: "謎の[br]{l2r}「寝たら負け」{/}{l2}精神{/}"; n: 2)
ono#sw1(left: 640px; top: 780px; w: 130; t: スッ; c: $sky; transform: rotate(-12deg); in: {scale:.5, x:30, opacity:0, duration:.1, ease:'power2.out'}; out: {x:-50, opacity:0, duration:.22, ease:'power1.in'})
ono#sw2(left: 680px; top: 880px; w: 130; t: スッ; c: $sky; transform: rotate(-6deg); in: {scale:.5, x:30, opacity:0, duration:.1, ease:'power2.out'}; out: {x:-50, opacity:0, duration:.22, ease:'power1.in'})

# 3 つ目: 朝の寝起きにおでこを触る。白の閃光で寄って入り、体温計が上がって下がり、「ペタ」2 つ → 「36.5℃ 平熱…」
section#three
scene#p3(main: kb {scale: [1, 1.08], focus: ['56% 20%', '56% 20%']}) [ref:@tsukio]月曜の早朝、カーテンの隙間から差し込む冷たく青白い朝の光。ベッドで上半身を起こした寝ぐせ頭・パジャマ姿の彼が、片手のひらを自分のおでこにペタッと当て、熱があってほしいと祈るような必死の期待の表情で上目遣いをしている。枕元にはまだ鳴る前の目覚まし時計。
stamp#st3(n: 3)
veil#fl3(color: #FFFFFF; opacity: .75; z-index: curtain; in: none)
headline#hl3(c: "アラーム前の[br]{l2}謎の{/}{l2r}微熱チェック{/}"; n: 3)
# 体温計 (白い管 + 赤い液 = 下を軸に伸び縮み + 赤い球 + 目盛り 38 / 37 / 36)・右から入る
div#th(left: 900px; top: 470px; width: 120px; height: 520px; in: {x:220, opacity:0, duration:.22, ease:'back.out(1.8)'})
  div#tube(left: 34px; top: 0px; width: 52px; height: 430px; border-radius: 26px; background: #FFFFFFEB; border: 6px solid $ink)
  div#fill(left: 48px; width: 24px; top: 399px; height: 20px; border-radius: 12px; background: $pink)
  div#bulb(left: 14px; top: 404px; width: 92px; height: 92px; border-radius: 148px; background: $pink; border: 6px solid $ink)
  p#s(left: -52px; top: "41;173;306"; font-size: 34px; line-height: 1; text-shadow: 0px 2px 6px #000000) ×3 38;37;36
#th.fill.hi(top: 50px; height: 369px; move: 900ms,power2.out)
#th.fill.mid(top: 219px; height: 200px; move: 600ms,power2.inOut)
ono#pt1(left: 500px; top: 500px; w: 170; overlap: th; t: ペタ; s: 69; c: $peta; -webkit-text-stroke: 10px $ink; transform: rotate(-12deg); in: {scale:1.8, opacity:0, duration:.1, ease:'power3.out'}; out: {opacity:0, duration:.15})
ono#pt2(left: 660px; top: 590px; w: 170; overlap: th; t: ペタ; s: 69; c: $peta; -webkit-text-stroke: 10px $ink; transform: rotate(-12deg); in: {scale:1.8, opacity:0, duration:.1, ease:'power3.out'}; out: {opacity:0, duration:.15})
# 判定: 「36.5℃」+ 青の札「平熱…」が 1.6 倍から弾む
div#read(left: 40px; top: 560px; width: 420px; height: 188px; in: {scale:1.6, opacity:0, duration:.14, ease:'back.out(2.5)'})
  p#t(left: 0px; top: -6px; width: 420px; font-size: 86px; line-height: 1.25; text-align: center; color: #FFFFFF; -webkit-text-stroke: 9px $ink) 36.5℃
  p#v(cx: 50%; top: 105px; font-size: 52px; line-height: 1.1; background: $blue; border: 4px solid $ink; border-radius: 14px; padding: 4px 22px) 平熱…

# 4 つ目: 鉄球を引きずって駅へ。左から押し出して入り、「重力 ×10」が上から落ちて画面が揺れ、足元の寄りの丸窓 + 「ズシッ」2 歩
section#four
scene#p4.bleed(content: @walk; main: kb {scale: [1, 1.08], focus: ['45% 17%', '45% 17%']})
stamp#st4(n: 4)
headline#hl4(c: "駅へ向かう足が[br]{l2r}鉛{/}{l2}のように重い{/}"; n: 4)
div#gv(left: 0px; top: 420px; width: 1080px; height: 315px; in: {y:-420, scale:1.3, opacity:0, duration:.18, ease:'power4.in'}; out: {opacity:0, duration:.15})
  p#l(left: 0px; top: -9px; width: 1080px; font-size: 92px; line-height: 1.2; text-align: center; color: #FFFFFF; -webkit-text-stroke: 9px $ink) 重力
  p#x(left: 0px; top: 92px; width: 1080px; text-align: center; font-size: 230px; line-height: .95; color: $pink; -webkit-text-stroke: 14px $ink; text-shadow: 12px 12px 0px $ink; content: "×10")
# 足元の寄りの丸窓 (同じ絵を 3.2 倍に寄せて鉄球の足元だけ・黄の縁 + 黒の外縁・3° 傾けて弾む)。絵は縁の内側に置く (inset: 0 だと縁を覆う)
div#ins.bleed(left: 640px; top: 512px; width: 400px; height: 380px; border-radius: 24px; background: #222222; border: 8px solid $y; box-shadow: 0px 0px 0px 6px $ink; transform: rotate(3deg); in: {scale:.3, rotation:-11, opacity:0, duration:.2, ease:'back.out(2.2)'})
  img#p(left: 8px; top: 8px; width: 386px; height: 364px; border-radius: 16px; content: @walk; object-fit: cover; object-position: 65% 76%; zoom: 324%; main: none)
ono#zu1(left: 560px; top: 880px; w: 250; t: ズシッ; s: 75; -webkit-text-stroke: 11px $ink; transform: rotate(-8deg); in: {y:-60, scale:1.3, opacity:0, duration:.09, ease:'power4.in'}; out: {opacity:0, duration:.15})
ono#zu2(left: 90px; top: 930px; w: 250; overlap: hl4; t: ズシッ; s: 75; -webkit-text-stroke: 11px $ink; transform: rotate(7deg); in: {y:-60, scale:1.3, opacity:0, duration:.09, ease:'power4.in'}; out: {opacity:0, duration:.15})

# 5 つ目: 会社のデスクで魂が抜ける。白の閃光で寄って入り、「あと 105 時間」が数え上がって赤に跳ね、白黒 + 紺の陰 + 縦縞で沈めて暗転
section#five
scene#p5.bleed(main: kb {scale: [1, 1.08], focus: ['48% 22%', '48% 22%']}) [ref:@tsukio]月曜の朝のオフィスの自分のデスク。紺色のスーツの彼が椅子に座り、卓上カレンダーを前に指を折って何かを数えながら白目になり、口から白い魂がふわっと抜け出しかけている（漫画的な表現）。蛍光灯の白っぽい無機質な光、背景の同僚たちはぼかしたシルエット。
# 絶望の幕 3 枚 (絵の直上・見出しと札より下): 彩度を抜く・紺を乗算・上から降りる暗い縦縞
veil#desat(filter: saturate(0.1); in: {opacity:0, duration:.5, ease:'power1.out'})
div#tint(left: 0px; top: 330px; width: 1080px; height: 1590px; background: #1B2350; mix-blend-mode: multiply; opacity: .55; border-radius: 24px; in: {opacity:0, duration:.5, ease:'power1.out'})
div#gloom5(left: 0px; top: 330px; width: 1080px; height: 900px; pattern: hatch,0,#08081E9E,21,3; mask-image: linear-gradient(180deg, #000000 0%, #000000D9 55%, #00000000 100%); opacity: .95; border-radius: 24px; in: {scaleY:.1, opacity:0, duration:.45, ease:'power2.out', pivot:'top'})
stamp#st5(n: 5)
veil#fl5(color: #FFFFFF; opacity: .75; z-index: curtain; in: none)
# 締め: 声の 0.55 秒後に全面を夜の地の色へ 0.4 秒で落とす (hf の暗転と同じ時刻・最後の frame は真っ暗)
veil#out5(color: $night; opacity: 1; z-index: curtain; in: {opacity:0, duration:.4, ease:'power1.in'})
headline#hl5(c: "金曜までの残り時間を[br]{l2}計算して{/}{l2r}絶望{/}"; n: 5)
# 残り時間の札 (濃紺の地 + 黄の縁・「あと」+ 数え上がる数字 + 「時間」)
div#cnt.bleed(left: 356px; top: 368px; width: 690px; height: 260px; border-radius: 22px; background: #080A1EF2; border: 4px solid $y; in: {scale:.6, y:-30, opacity:0, duration:.2, ease:'back.out(2.2)'})
  p#l(cx: 50%; top: 14px; font-size: 50px; line-height: 1.2) 金曜 18:00 まで
  p#ato(left: 58px; top: 170px; font-size: 58px; line-height: 1) あと
  p#num(left: 172px; top: 74px; width: 330px; font-size: 168px; line-height: 1; text-align: center; color: $y) [count:105 start=0 ms=1380ms delay=740ms]
  p#unit(left: 501px; top: 165px; font-size: 64px; line-height: 1) 時間
```

```timeline.txt
#v2
cast n = "テンション高めのバラエティ番組風の若い男性ナレーター、張りのある声で早口に勢いよく語る" speed=130% manner="テンション高めのバラエティ番組ナレーション風に、早口で勢いよく"
silence head=0ms tail=120ms
transition = push {duration: .24, dir: 'left', overlap: .24, ease: 'power3.out'}

*** hook
[>#subtitle]
bgm music
@n: [!#p0 shake {x: 16, duration: .4}][♪gaan to=1.7s fade=0ms,600ms]毎週日曜の夜に[|]これ耐えてる奴、[|][<#gloom0 -250ms]全員仲間！[|][!#hook1 to,{scale:.86, y:-30, duration:.18, ease:'power2.out'} -50ms][>#hook2 -30ms][>#fl0 -30ms][!#fl0 to,{opacity:0, duration:.18, ease:'power1.out'} +20ms][♪jan -4dB -30ms][>#pc[*] +60ms][!#p0 shake {x: 12, duration: .35} +120ms]月曜の絶望あるある5選！

*** one
[!#pc[1] .on][!#pc[1] punch {scale: 1.3, duration: .32}]
@n: [♪jan -6dB][>#st1 +20ms][>#clock +220ms][<#st1 +500ms][>#hl1 +500ms]1つ目！日曜18時半のアニメが[|]終わった瞬間、[|]休日の終わりを告げる[|][>#cd][♪tick -10dB to=1.7s fade=50ms,150ms]カウントダウンが始まって[|][>#bub +50ms][!#bub to,{scale:.82, duration:.3, ease:'power2.in'} +320ms][♪chiin_s -4dB +280ms to=1.2s fade=0ms,500ms]口数が減る。
transition push {duration: .26, dir: 'top', overlap: .26, ease: 'power3.out'}

*** two
[!#pc[2] .on][!#pc[2] punch {scale: 1.3, duration: .32}][!#pc[1] .done]
@n: [♪jan -6dB][>#st2 +20ms][<#st2 +520ms][>#hl2 +520ms][!#clock.hm text,"23:00" +300ms]2つ目！早く寝なきゃいけないのに、[|][♪tick -12dB to=2.4s fade=50ms,120ms][!#clock.hm text,"23:30" +300ms]「寝たら[!#clock.day text,"月"][!#clock.day fill,$blue][!#clock.hm text,"0:00"]明日に[!#clock.hm text,"0:30"]なっちゃう」[|][!#clock.hm text,"1:00"]と思[!#clock.hm text,"1:30"]って[|][!#clock.hm text,"2:00" +50ms][!#clock.al to,{opacity:1, duration:.1} +50ms][!#clock punch {scale: 1.12, duration: .3} +50ms][♪tsukkomi -8dB +20ms]深夜2時まで[|][>#sw1 +50ms][<#sw1 +270ms][>#sw2 +420ms][<#sw2 +640ms][♪swipe -1dB +50ms to=0.45s][♪swipe -2dB +420ms to=0.45s]無駄にスマホを見る。
transition dissolve {duration: .26, overlap: .26, zoom: 1.45, ease: 'power3.out'}

*** three
[!#pc[3] .on][!#pc[3] punch {scale: 1.3, duration: .32}][!#pc[2] .done]
@n: [>#fl3][!#fl3 to,{opacity:0, duration:.2, ease:'power1.out'} +50ms][♪jan -6dB][>#st3 +20ms][<#st3 +520ms][>#hl3 +520ms][<#clock.al][!#clock.hm text,"6:59" +300ms]3つ目！月曜の朝起きた瞬間、[|][card:small][>#th][!#th.fill .hi +200ms]「ワンチャン熱出てないかな…」[|]と自分のおでこを[|][!#th.fill .mid -100ms][>#pt1][<#pt1 +320ms][>#pt2 +240ms][<#pt2 +560ms][♪pat -3dB to=0.35s][♪pat -3dB +240ms to=0.35s][>#read +840ms][♪tsukkomi -7dB +840ms]ペタペタ触って確認する。
transition push {duration: .24, dir: 'right', overlap: .24, ease: 'power3.out'}

*** four
[!#pc[4] .on][!#pc[4] punch {scale: 1.3, duration: .32}][!#pc[3] .done]
@n: [♪jan -6dB][>#st4 +20ms][<#st4 +520ms][>#hl4 +520ms][!#clock.hm text,"7:45" +300ms]4つ目！家を出て駅に向かう道中、[|][>#gv -120ms][♪impact -1dB +20ms to=1.4s fade=0ms,600ms][!#p4 shake {x: 15, duration: .55} +60ms][!#gv shake {x: 15, duration: .55} +60ms]まるで重力10倍の[|][<#gv +300ms][>#ins +450ms]部屋にいるかのように[|][>#zu1 -30ms][!#p4 to,{y:30, duration:.06, ease:'power2.out'} +20ms][!#p4 to,{y:10, duration:.2, ease:'power2.out'} +80ms][!#ins shake {x: 7, duration: .225} +20ms][♪step +20ms to=0.5s][♪thud -11dB +20ms to=0.6s][<#zu1 +320ms][>#zu2 +350ms][!#p4 to,{y:30, duration:.06, ease:'power2.out'} +400ms][!#p4 to,{y:10, duration:.2, ease:'power2.out'} +460ms][!#ins shake {x: 7, duration: .225} +400ms][♪step +400ms to=0.5s][♪thud -11dB +400ms to=0.6s][<#zu2 +700ms]一歩一歩が重い。
transition dissolve {duration: .26, overlap: .26, zoom: 1.45, ease: 'power3.out'}

*** five
[!#pc[5] .on][!#pc[5] punch {scale: 1.3, duration: .32}][!#pc[4] .done]
@n: [>#fl5][!#fl5 to,{opacity:0, duration:.2, ease:'power1.out'} +50ms][♪jan -6dB][>#st5 +20ms][<#st5 +520ms][>#hl5 +520ms][!#clock.hm text,"8:58" +300ms]5つ目！会社に着いた瞬間、[|][>#cnt][♪digital -12dB to=2.1s fade=0ms,120ms]金曜の定時まで[|]あと何時間かを計算して、[|][!#cnt punch {scale: 1.18, duration: .35}][!#cnt.num recolor,$pink {duration: .08}][!#p5 shake {x: 14, duration: .45}][♪piano -3dB -20ms to=1.8s fade=0ms,600ms]その長さに[|][>#desat][>#tint][>#gloom5]もう一回絶望する。[silence:0.1s][♪chiin to=1.0s fade=0ms,450ms][!#pc[5] .done][!#p5 to,{scale:1.07, duration:.9, ease:'power2.out'}][<#hl5][>#out5 +450ms][silence:0.9s]
```

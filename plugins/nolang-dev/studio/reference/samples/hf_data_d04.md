# data · teen-sleep-phone (hf 全力版の全量の写し — 高校生の睡眠、スマホを置く時刻で変わる・夜の街の地に題つきの板を場面ごとに組む 7 場面のデータ図解) — canvas 1080x1920

見せる作り: 全編の地 (夜の街の絵の kb + 漂う紫とピンクの光 + 瞬く星 46 + 上下の陰)・冒頭はスマホを持つ少女の絵に光と振動の弧・1 字ずつ弾む問い → 陰を下ろして題 (傾いて弾む黄の「変わる」+ ピンクの下線)・回って決まる 1,236 の札・2 場面目から常設の上端 (題の札 + 章の丸 5 つを語で黄に点す)・場面 = 題つきの板 1 枚が下から弾んで入り上へ抜ける・板の中の図は数字の語で動く (回る平均・順に伸びる縦棒 → 6 時間未満をピンクに沈め分けてかぎと札と判子・順に伸びる横棒を語で塗り分け → 基準線と差の斜線と 95 分の札・左から描く 2 本の折れ線と弾む点・前 → 後の 4 行と割合の細い棒)・決まる数字に散る放射の線・まとめの 3 枚と黄に光る注記の縁・締めは地だけに呼びかけ 2 行と伸びをする少女・字幕は黒い半透明の札で数字だけ黄・音の層 (BGM + 語に結んだ効果音 50)

```design.txt
#v2
# 学ぶ作り: 夜の data の design system を根に 1 回 (palette・丸ゴシック 2 太さ + ポップ体・黄の語の run・題つきの板 board の def・黒い半透明の札の字幕)
# 全編の地は根に (夜の街の絵の kb + 動く紫とピンクの光 + 瞬く星 46 + 上下の陰)・2 場面目から常設の上端 (題の札 + 章の丸 5 つ・語で黄に点く)
# 場面 = 板 1 枚が下から弾んで入り上へ抜ける (切替は書かない・地は常設)。板の中の図は数字の語で伸び / 色が変わり、決まる数字には放射の線が散る
# hf d04 teen-sleep-phone (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#0B0D2A
theme dark
palette ink=#FFFFFF ink2=#D3D5F7 ink3=#A3A7DC navy=#12143F mint=#39E0B8 pink=#FF5C9E yellow=#FFD23F sky=#4FC3FF lav=#A88BFF muted=#5D62A6 dim=#4C5196 deep=#1E2163
font "やわらかい丸い線端の丸ゴシック体の最も太いウェイト (Black)"
fonts r="やわらかい丸い線端の丸ゴシック体の最も太いウェイト (Black)" m="やわらかい丸い線端の丸ゴシック体の太字 (Bold)" p="極太でぽってり丸みのある、弾むような手書き風のポップな日本語の見出し書体"
sfx off
# hf の作り: 板の題・副題・凡例・注記は板と一緒に先に出し、台詞が後から数字を読む (spoiler・all_at_once)・注記と軸の目盛りは 16〜19 px (hf の 24〜29 px) (small_text)
# hf の作り: 地は全編 1 枚の夜の街の絵で、場面は板で替える (same_picture)・図の色 (半透明の地・線・暗い縁) は直書き (palette_drift)・語ごとの効果音 50 (se_dense)
# hf の作り: 数字は丸いポップ体で大きく (script_font_digits)・結果の札と注記は話す間だけ出る (flash_text)・板の題と字幕が同じ語 (duplicate_text)・ルールの題の札は枠の上辺に乗る (child_overflow・stacked_labels)
# hf の作り: 冒頭の問いは画面の大きな文字で読ませて字幕を出さない (caption_gap)・スマホの光は字幕の帯まで広がる (caption_collision)
lint off=spoiler,all_at_once,small_text,same_picture,palette_drift,se_dense,script_font_digits,flash_text,duplicate_text,child_overflow,stacked_labels,caption_gap,caption_collision
art "モダンでポップなフラットイラスト、日本の SNS 解説動画向け。きれいなベクターの形、やわらかいグラデーションと控えめな粒子の質感、丸みのある親しみやすい形、くっきりした輪郭。夜の配色: 深い藍色、青紫、ラベンダーに、ピンク・ミント・月の黄色の小さなネオンのアクセント。10 代向けでかわいくおしゃれ、子どもっぽくない"
prompt_tail "文字・数字・ロゴ・透かしは一切入れない"
run y { color: $yellow }
run b { font-family: p; font-size: 40px; color: $yellow }
run sb { font-size: 26px; color: $ink2 }
run sn { font-size: 24px; color: $ink3; font-family: m }
run e { font-size: 26px; color: $ink3; font-family: m }
run ks { font-size: 22px; color: $ink3; font-family: m }
run as { font-size: 30px; font-family: r }
run pn { font-family: p; font-size: 46px; color: $ink }
run pm { font-family: p; font-size: 46px; color: $mint }
run b8 { font-family: p; font-size: 44px; color: $yellow }
run s33 { font-size: 50px }
run wsm { font-size: 30px; color: $ink2 }
run u { font-size: 30px; font-family: r }
p { color: #FFFFFF; in: none; out: none }
div { border: none; in: none; out: none }
img { out: none }
svg { out: none }
group { out: none }
sound vibe = "スマホのバイブレーションのブーッという短い振動音"
sound pop_hi = "高く軽い、弾むポンという電子音"
sound pop_soft = "やわらかく小さいポッという出現音"
sound whoosh_swing = "ヒュンと振り抜く風切り音"
sound whoosh_short = "短く軽いシュッという場面転換の風切り音"
sound rise_pop = "下から上がっていくポップな電子音、ピュイッ"
sound tick = "数字が回るカチカチという小さな刻み音"
sound sparkle = "キラッと光る短いきらめき音"
sound chime_soft = "やわらかく澄んだ短いチャイム"
sound chime_ok = "明るい正解のチャイム、ピンポロン"
sound click = "カチッという軽いクリック音"
sound alarm = "目覚まし時計のジリリリというベル"
svg moon = """<svg viewBox="0 0 40 40"><path d="M27 6a15 15 0 1 0 8 22A12 12 0 0 1 27 6z" fill="#FFD23F"/></svg>"""
svg buzz_l = """<svg viewBox="0 0 120 120"><path d="M30 30Q12 60 30 90" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M14 18Q-8 60 14 102" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".6"/></svg>"""
svg buzz_r = """<svg viewBox="0 0 120 120"><path d="M90 30Q108 60 90 90" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M106 18Q128 60 106 102" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round" opacity=".6"/></svg>"""
svg brk = """<svg viewBox="0 0 192 23"><path d="M1.5 23V15A13.5 13.5 0 0 1 15 1.5H177A13.5 13.5 0 0 1 190.5 15V23" fill="none" stroke="#FF5C9E" stroke-width="3"/></svg>"""
svg stairs = """<svg viewBox="0 0 48 48"><path d="M6 10h10v10h10v10h10v10h6" stroke="#FF5C9E" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M36 32l6 4-6 4" stroke="#FF5C9E" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg trend = """<svg viewBox="0 0 34 34"><path d="M4 28L14 18l6 6L30 8" stroke="#FFD23F" stroke-width="4.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M21 8h9v9" stroke="#FFD23F" stroke-width="4.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg line_a = """<svg viewBox="105 245 480 335"><path d="M113 451.7L230 416.3L347 360.5L463 284.5L580 254.1" fill="none" stroke="#FFD23F" stroke-width="5.3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg area_a = """<svg viewBox="105 245 480 335"><path d="M113 573L113 451.7L230 416.3L347 360.5L463 284.5L580 254.1L580 573Z" fill="#FFD23F" fill-opacity=".1"/></svg>"""
svg line_b = """<svg viewBox="105 245 480 335"><path d="M113 532.8L230 517.6L347 487.2L463 441.6L580 416.3" fill="none" stroke="#FF5C9E" stroke-width="5.3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg area_b = """<svg viewBox="105 245 480 335"><path d="M113 573L113 532.8L230 517.6L347 487.2L463 441.6L580 416.3L580 573Z" fill="#FF5C9E" fill-opacity=".1"/></svg>"""
svg arr_gray = """<svg viewBox="0 0 44 36"><path d="M2 18h34M24 6l14 12-14 12" stroke="#A3A7DC" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg arr_mint = """<svg viewBox="0 0 44 36"><path d="M2 18h34M24 6l14 12-14 12" stroke="#39E0B8" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg rsn_alarm = """<svg viewBox="0 0 110 110"><rect x="34" y="12" width="42" height="80" rx="9" fill="none" stroke="#FF5C9E" stroke-width="6"/><circle cx="55" cy="80" r="4" fill="#FF5C9E"/><path d="M18 34q-8 14 0 28M8 26q-14 22 0 44M92 34q8 14 0 28M102 26q14 22 0 44" stroke="#FFD23F" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M55 34v14l9 6" stroke="#FFFFFF" stroke-width="5" fill="none" stroke-linecap="round"/></svg>"""
svg rsn_chat = """<svg viewBox="0 0 110 110"><path d="M16 22h78a8 8 0 0 1 8 8v40a8 8 0 0 1-8 8H48l-18 16v-16H16a8 8 0 0 1-8-8V30a8 8 0 0 1 8-8z" fill="none" stroke="#4FC3FF" stroke-width="6" stroke-linejoin="round"/><circle cx="36" cy="50" r="5" fill="#fff"/><circle cx="55" cy="50" r="5" fill="#fff"/><circle cx="74" cy="50" r="5" fill="#fff"/></svg>"""
# 決まる数字に散る放射の線 12 本 (外の半径に描き、内の半径の比から広がる)
svg burst2 = """<svg viewBox="-270 -270 540 540"><path d="M217 58L246 66M58 217L66 246M-159 159L-180 180M-217 -58L-246 -66M-58 -217L-66 -246M159 -159L180 -180" stroke="#FFD23F" stroke-width="12" stroke-linecap="round"/><path d="M159 159L180 180M-58 217L-66 246M-217 58L-246 66M-159 -159L-180 -180M58 -217L66 -246M217 -58L246 -66" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/></svg>"""
svg burst3 = """<svg viewBox="-200 -200 400 400"><path d="M150 40L179 48M40 150L48 179M-110 110L-131 131M-150 -40L-179 -48M-40 -150L-48 -179M110 -110L131 -131" stroke="#FFD23F" stroke-width="12" stroke-linecap="round"/><path d="M110 110L131 131M-40 150L-48 179M-150 40L-179 48M-110 -110L-131 -131M40 -150L48 -179M150 -40L179 -48" stroke="#FF5C9E" stroke-width="12" stroke-linecap="round"/></svg>"""
svg burst5 = """<svg viewBox="-260 -260 520 520"><path d="M208 56L237 63M56 208L63 237M-152 152L-173 173M-208 -56L-237 -63M-56 -208L-63 -237M152 -152L173 -173" stroke="#39E0B8" stroke-width="12" stroke-linecap="round"/><path d="M152 152L173 173M-56 208L-63 237M-208 56L-237 63M-152 -152L-173 -173M56 -208L63 -237M208 -56L237 -63" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/></svg>"""
svg burst6 = """<svg viewBox="-320 -320 640 640"><path d="M266 71L295 79M71 266L79 295M-194 194L-216 216M-266 -71L-295 -79M-71 -266L-79 -295M194 -194L216 -216" stroke="#FFD23F" stroke-width="12" stroke-linecap="round"/><path d="M194 194L216 216M-71 266L-79 295M-266 71L-295 79M-194 -194L-216 -216M71 -266L79 -295M266 -71L295 -79" stroke="#FF5C9E" stroke-width="12" stroke-linecap="round"/></svg>"""
svg burst8 = """<svg viewBox="-430 -430 860 860"><path d="M372 100L401 107M-100 372L-107 401M-372 -100L-401 -107M100 -372L107 -401" stroke="#FFD23F" stroke-width="12" stroke-linecap="round"/><path d="M272 272L293 293M-272 272L-293 293M-272 -272L-293 -293M272 -272L293 -293" stroke="#39E0B8" stroke-width="12" stroke-linecap="round"/><path d="M100 372L107 401M-372 100L-401 107M-100 -372L-107 -401M372 -100L401 -107" stroke="#FF5C9E" stroke-width="12" stroke-linecap="round"/></svg>"""
# 同じ少女を 4 枚 (冒頭・居眠り・2 部屋・伸び) に描くので基準画像を 1 枚
image girl = "縦長 9:16 のイラスト。夜遅く、ベッドで横向きに寝そべり、ふわふわの紺色の毛布をかけた日本の女子高校生 (黒髪のショートボブ、ゆったりしたラベンダー色のパジャマ)。顔の近くで光るスマートフォンを持ち、スマホの青白い光が眠そうな半目の顔を照らす。小さな寝室: 三日月と瞬く星の見える窓、枕の上のぬいぐるみ。構図: ベッドと少女は画面の下 45% だけに収め、上半分は落ち着いた暗い夜の壁と窓だけでほとんど何も描かず、大きな題の文字を置く余白にする" aspect=9:16
bgm#music(fade: 400,1600) おしゃれで懐かしい中くらいのテンポのシティポップ、サイン波のシンセの旋律にエレキギター・エレキベース・ドラム、夜の都会のゆったりした雰囲気、ボーカルなし
# 字幕: 下寄りの黒い半透明の角丸の札・白の太字 32 px・数字だけ黄 ({y})・札は文ごと (台詞の [|] で句に割る)・札は声の後 60 ms で閉じ、同じ場面の次の文までは hold で残る (文の間の無音は次の文の頭に置く = 札の後ろに無音が無い)。場面の末の無音 70〜100 ms は tail より長いので、札は次の場面へ跨がない (hf は板が替わる時に札が消える)
subtitle.hug(left: 50px; top: 1424px; width: 980px; font-size: 48px; line-height: 1.32; letter-spacing: 0.01em; text-align: center; color: #FFFFFF; background: #090A24C7; border: 2px solid #FFFFFF1A; border-radius: 30px; padding: 14px 34px 16px 34px; unit: sentence; strip: 。; lead: 40ms; tail: 60ms; in: {y:14, scale:0.96, opacity:0, duration:0.16, ease:'power2.out'})

# 全編の地: 夜の街の絵 (ゆっくり引く) + 紫とピンクのぼけた光 (漂う) + 瞬く星 46 (大きさの 3 群・群ごとの周期) + 上下の陰
img#bg_base(inset: 0; z-index: back; main: kb {scale: [1.134, 1.05], focus: ['50% 46%', '50% 54%']}) 縦長の夜空の背景。深い藍色から青紫へのなめらかなグラデーションに小さな星と柔らかく光る点が散り、右上の隅に小さな光る三日月。画面の最下部 (下 16%) だけに、静かな日本の住宅街の平らなシルエット (屋根・小さな集合住宅・電柱と電線) と暖かい黄色の灯りの窓がいくつか。中央は大きく空いた何もない夜空。人物なし
div#blob1(left: -160px; top: 520px; width: 520px; height: 520px; border-radius: 1498px; background: radial(#6B3FE08C,#6B3FE000@70%); z-index: back; main: sine {x: 120, y: -160, period: '256s'}; bleed)
div#blob2(left: 720px; top: 1180px; width: 520px; height: 520px; border-radius: 1498px; background: radial(#FF5C9E40,#FF5C9E00@70%); z-index: back; main: sine {x: -140, y: -120, period: '256s'}; bleed)
div#star(left: "388;107;334;99;250;317;521;580;58;176;684;172;679;39;374;339;601;324;466;300;229;222;583;682;674;183;383;441;179;706;658;459;609;28;688;579;227;649;381;351;140;634;167;107;448;112"; top: "838;590;444;393;37;886;104;767;661;697;480;670;277;120;837;620;963;694;376;33;188;617;690;951;191;632;845;568;180;244;269;289;323;102;600;843;802;755;288;25;457;718;580;884;205;379"; width: "3;3;3;3;3;3;3;3;3;3;3;3;3;3;3;4;4;4;4;4;4;4;4;4;4;4;4;4;4;4;4;5;5;5;5;5;5;5;5;5;5;5;5;5;5;5"; height: "3;3;3;3;3;3;3;3;3;3;3;3;3;3;3;4;4;4;4;4;4;4;4;4;4;4;4;4;4;4;4;5;5;5;5;5;5;5;5;5;5;5;5;5;5;5"; border-radius: 148px; background: #FFFFFF; box-shadow: 0px 0px 10px 2px #FFFFFF8C; opacity: "0.74;0.54;0.95;0.52;0.82;0.50;0.61;0.93;0.62;0.91;0.69;0.95;0.95;0.58;0.80;0.95;0.97;0.55;0.67;0.64;0.77;0.70;0.81;0.49;0.80;0.52;0.88;0.72;0.55;0.68;0.55;0.88;0.84;0.67;0.75;0.94;0.65;0.88;0.50;0.67;0.63;0.79;0.63;0.92;0.68;0.50"; z-index: back; main: sine {opacity: 0.225, period: 1.716}) ×46
div#bgshade(inset: 0; background: linear(#0B0D2A59,#0B0D2A00@35%,#0B0D2A00@70%,#0B0D2A40,180); z-index: back)

# 題つきの板 (番号の黄の丸札 + 題)・下から弾んで入り、上へ抜けて消える
def board(n, t="", nw=56) = div(left: 48px; top: 236px; width: 984px; height: 1150px; border-radius: 48px; background: linear(#212462F0,#17194AF0,180); border: 2px solid #FFFFFF21; box-shadow: 0px 30px 80px #05061E8C; in: {y:90, scale:0.93, opacity:0, duration:0.55, ease:'back.out(1.5)'}; out: {y:-50, scale:0.96, opacity:0, duration:0.3, ease:'power2.in'})
  p#no(left: 40px; cy: 68px; width: {nw}; font-size: 34px; font-family: p; text-align: center; color: $navy; background: $yellow; border-radius: 148px; padding: 10px 0px; content: {n})
  p#tt(left: .no.right+18; cy: 68px; font-size: 52px; content: {t})
# 冒頭の札 (濃紺の半透明の丸札・弾んで出る)
def chip = p(font-size: 32px; background: #10123AD1; border: 2px solid #FFFFFF33; border-radius: 34px; padding: 18px 28px; in: {scale:0.7, y:24, opacity:0, duration:0.4, ease:'back.out(2.2)'})
# 板の下の注記 (細い丸ゴシック・薄い紫)
def note = p(left: 44px; font-size: 26px; color: $ink3; font-family: m)

# 問い → 題: スマホを持つ少女の絵が引き、光と振動の弧の上に問いを 1 字ずつ → 陰を下ろして題・札・数え上げ
section#hook
# hf の作り: 架空の注は少女の絵の上に乗る (text_over_subject)
# 生成の絵の少女は hf より小さく低い (顔が画面の 7 割下) — 不動点を下端左寄りに置いて拡大し、顔を字幕の帯の上 (画面の 6〜7 割) に上げる
img#hero(inset: 0; content: @girl; subject: bottom 45%; room: top 55%; main: kb {scale: [1.58, 1.42], focus: ['30% 100%', '30% 100%'], ease:'power1.out'}; out: {opacity:0, duration:0.35})
# スマホの光 (screen で重ねる丸い光・振動で横に震え、呼吸する)
div#glow(left: 64px; top: 1234px; width: 400px; height: 400px; border-radius: 1498px; background: radial(#AAE1FFD9,#78BEFF59@35%,#78BEFF00@70%); mix-blend-mode: screen; in: {scale:0.7, opacity:0, duration:0.25, ease:'power2.out'})
svg#bz_l(left: 86px; top: 1284px; width: 132px; height: 132px; part: buzz_l; in: {scale:0.55, opacity:0, duration:0.18, ease:'power2.out'})
svg#bz_r(left: 334px; top: 1284px; width: 132px; height: 132px; part: buzz_r; in: {scale:0.55, opacity:0, duration:0.18, ease:'power2.out'})
div#heroshade(inset: 0; background: linear(#090A24EB,#090A24BF@38%,#090A2433@62%,#090A2459,180); in: {opacity:0, duration:0.5, ease:'power1.out'}; out: {opacity:0, duration:0.35})
# 問いの 2 行 (1 字ずつ弾む・題の前に上へ抜ける)
group#q(out: {y:-80, opacity:0, duration:0.25, ease:'power2.in'})
  p#l1(cx: 540px; cy: 376px; font-size: 74px; font-family: p; line-height: 1.25; in: {scale:0.3, y:40, opacity:0, duration:0.42, ease:'back.out(2.2)', stagger:0.035}) 寝る前のスマホ、
  p#l2(cx: 540px; cy: 484px; font-size: 96px; font-family: p; line-height: 1.3; in: {scale:0.3, y:40, opacity:0, duration:0.42, ease:'back.out(2.2)', stagger:0.035}) {y}何時{/}に手放してる？
# 題の組: 小札 → 2 行 → 黄の「変わる」(傾いて弾む) → ピンクの下線 → 3 つの札 (1,236 は回って決まる) → 架空の注
group#ttl(out: {y:-40, opacity:0, duration:0.3, ease:'power2.in'})
  div#kicker(left: 350px; top: 250px; width: 381px; height: 64px; border-radius: 32px; background: #FFFFFF1F; border: 2px solid #FFFFFF38; in: {scale:0.7, y:20, opacity:0, duration:0.4, ease:'back.out(2.2)'})
    svg#m(left: 20px; cy: 50%; width: 38px; height: 38px; part: moon)
    p#t(left: 69px; cy: 50%; font-size: 32px) よふかしラボ 調べ
  p#t1(cx: 540px; cy: 402px; font-size: 86px; font-family: p; line-height: 1.22; in: {scale:0.7, y:40, opacity:0, duration:0.45, ease:'back.out(2.2)'}) 高校生の睡眠、
  p#t2(cx: 540px; cy: 507px; font-size: 86px; font-family: p; line-height: 1.22; in: {scale:0.7, y:40, opacity:0, duration:0.45, ease:'back.out(2.2)'}) スマホを置く時刻で
  div#ul(left: 278px; top: 711px; width: 525px; height: 30px; border-radius: 15px; background: $pink; in: {scaleX:0, duration:0.4, ease:'power3.out', pivot:'left'})
  p#t3(cx: 540px; cy: 654px; font-size: 168px; font-family: p; line-height: 1.12; color: $yellow; overlap: ttl.ul; in: {scale:0.2, y:20, rotation:-8, opacity:0, duration:0.6, ease:'back.out(2.6)'}) 変わる
  chip#ch1(cx: 362px; cy: 952px) 全国の高校1〜3年生
  chip#ch2(cx: 723px; cy: 952px) 有効回答 {b}[count:1,236 start=0 roll ms=800,880,960,1040 delay=190]{/}人
  chip#ch3(cx: 540px; cy: 1040px) オンライン調査・自己申告
  p#fict(cx: 540px; top: 1110px; font-size: 26px; color: $ink2; font-family: m; in: {opacity:0, duration:0.4}) ※よふかしラボは架空の教育NPOです

# 01 睡眠時間の分布: 平均が回って決まり、5 本の縦棒が順に伸びる →「35%」で 6 時間未満の 2 本をピンクに、残りを沈め、かぎと札 →「3人に1人」の判子
section#dist(stagger: {each:0})
# 常設の上端 (2 場面目から sticky): 題の札 + 章の丸 5 つ (今の章が黄に点く)
div#hchip.sticky(left: 48px; top: 140px; width: 412px; height: 64px; border-radius: 32px; background: #FFFFFF1A; border: 2px solid #FFFFFF24; delay: 100ms; in: {x:-40, opacity:0, duration:0.45, ease:'back.out(1.8)'}; out: {opacity:0, duration:0.3})
  svg#m(left: 18px; cy: 50%; width: 36px; height: 36px; part: moon)
  p#t(left: 66px; cy: 50%; font-size: 30px) 高校生の睡眠 × スマホ
p#pd.sticky(left: "505;543;581;619;657"; top: 148px; width: 46px; font-size: 22px; font-family: p; text-align: center; color: $ink3; background: #FFFFFF14; border: 2px solid #FFFFFF24; border-radius: 148px; padding: 10px 0px; delay: 150ms; in: {scale:0.4, opacity:0, duration:0.35, ease:'back.out(2.2)', stagger:{each:0.05}}; out: {opacity:0, duration:0.3}) ×5 1;2;3;4;5
#pd.on(color: $navy; background: $yellow; border: 2px solid $yellow)
board#b2(n: "01"; t: "平日の睡眠時間")
  # 主役の数字: 平均 + 時と分が別々に回る (odometer)
  # 板と一緒に 0 時間 00 分で出て、「平均」の語で回り始める
  div#hero(left: 44px; top: 140px; width: 900px; height: 146px; delay: 300ms; in: {scale:0.8, y:20, opacity:0, duration:0.45, ease:'back.out(2.2)'})
    p#lab(left: 0px; cy: 50%; font-size: 40px; color: $ink2; background: #FFFFFF1A; border-radius: 16px; padding: 6px 18px) 平均
    p#h(left: 130px; top: 0px; font-size: 132px; font-family: p; line-height: 1.1) [count:6 start=0 roll ms=1000]
    p#hu(left: 231px; top: 66px; font-size: 58px) 時間
    p#m(left: 346px; top: 0px; font-size: 132px; font-family: p; line-height: 1.1) [count:21 start=0 roll ms=1080,1160]
    p#mu(left: 542px; top: 66px; font-size: 58px) 分
  # 縦棒 5 本 (1% = 6.67 px・下端 600 から上へ伸びる)・値・軸の札 (時間帯 / 人数)
  div#base(left: 52px; top: 898px; width: 880px; height: 3px; background: #FFFFFF59; delay: 400ms; in: {scaleX:0, duration:0.5, ease:'power2.out', pivot:'left'})
  div#col(left: "56;173;291;408;525"; top: "547;420;347;460;560"; width: 112px; height: "53;180;253;140;40"; border-radius: 20px 20px 0px 0px; background: $sky; delay: 500ms; in: {scaleY:0, duration:0.7, ease:'back.out(1.4)', pivot:'bottom', stagger:{each:0.12}}) ×5
  # 35% の語でピンクに点く 2 本 (角ごとの角丸の棒は fill の印で塗り替えられないので、同じ形の色の棒を重ねて溶かす)
  div#hot(left: "56;173"; top: "547;420"; width: 112px; height: "53;180"; border-radius: 20px 20px 0px 0px; background: $pink; overlap: b2.col; in: {opacity:0, duration:0.3}) ×2
  p#colv(cx: "93;211;328;445;563"; top: "504;377;304;417;517"; font-size: 46px; delay: 850ms; in: {scale:0.5, y:16, opacity:0, duration:0.35, ease:'back.out(2.2)', stagger:{each:0.12}}) ×5 8%;27%;38%;21%;6%
  p#colx(cx: "93;211;328;445;563"; top: 912px; font-size: 32px; line-height: 1.3; text-align: center; delay: 600ms; in: {scale:0.9, y:10, opacity:0, duration:0.3, ease:'power2.out', stagger:{each:0.12}}) ×5 5時間[br]{sb}未満{/}[br]{sn}99人{/};5〜6[br]{sb}時間{/}[br]{sn}334人{/};6〜7[br]{sb}時間{/}[br]{sn}470人{/};7〜8[br]{sb}時間{/}[br]{sn}259人{/};8時間[br]{sb}以上{/}[br]{sn}74人{/}
  # 6 時間未満のかぎと札 (語で出る)
  svg#brk(left: 84px; top: 548px; width: 288px; height: 34px; part: brk; in: {scaleX:0.3, opacity:0, duration:0.35, ease:'back.out(2)'})
  div#pill(left: 62px; top: 398px; width: 312px; height: 132px; border-radius: 30px; background: $pink; box-shadow: 0px 12px 30px #FF5C9E59; in: {scale:0.4, y:30, opacity:0, duration:0.5, ease:'back.out(2.2)'})
    p#k(cx: 50%; top: 15px; font-size: 30px) 6時間未満
    p#v(left: 32px; top: 51px; font-size: 60px; font-family: p; line-height: 1.05) 35%
    p#c(left: .v.right+6; top: 78px; font-size: 26px) （433人）
  # 黄の判子 (傾いて大きく叩きつける)
  div#stamp(left: 590px; top: 318px; width: 380px; height: 128px; border-radius: 30px; background: $yellow; box-shadow: 0px 14px 34px #FFD23F4D; transform: rotate(-5deg); in: {scale:2.2, rotation:-14, opacity:0, duration:0.45, ease:'back.out(1.6)'})
    p#a(cx: 50%; top: 14px; font-size: 54px; font-family: p; line-height: 1.05; color: $navy) 3人に1人
    p#b(cx: 50%; top: 78px; font-size: 30px; color: $navy) を超える
  note#note(top: 1100px) ※自己申告・全国の高校1〜3年生 1,236人
svg#fx2(left: -4px; top: 430px; width: 540px; height: 540px; part: burst2; overlap: b2; in: {scale:0.625, opacity:0, duration:0.55, ease:'power2.out'}; out: {opacity:0, duration:0.3, ease:'power1.in'}; bleed)

# 02 手放す時刻別の睡眠: 横棒 5 本が順に伸び、語で 22 時前をミント・24 時以降と寝落ちをピンクに → 傾きの札 → 7 時間 19 分の基準線と差の斜線 → 95 分の札
section#phone(stagger: {each:0})
board#b3(n: "02"; t: "スマホを手から離す時刻")
  p#sub(left: 44px; top: 112px; font-size: 28px; color: $ink3; font-family: m) 時刻別の平日の平均睡眠時間
  # 傾きの札 (ピンクの縁の丸札 + 階段の矢印)
  div#per30(left: 44px; top: 170px; width: 608px; height: 76px; border-radius: 38px; background: #FF5C9E29; border: 3px solid $pink; in: {scale:0.6, y:20, opacity:0, duration:0.45, ease:'back.out(2.2)'})
    svg#i(left: 20px; cy: 50%; width: 46px; height: 46px; part: stairs)
    p#k1(left: 80px; cy: 50%; font-size: 34px) 1時間遅いごとに
    p#v(left: .k1.right+14; cy: 50%; font-size: 44px; font-family: p; color: $yellow) 約30分
    p#k2(left: .v.right+14; cy: 50%; font-size: 34px) 短く
  # 目盛り (0〜8 時間・1 分 = 0.867 px)
  div#grid(left: "195;299;403;507;611"; top: 270px; width: 2px; height: 690px; background: #FFFFFF17; delay: 400ms; in: {opacity:0, duration:0.4}) ×5
  p#tick(cx: "195;299;403;507;611"; top: 968px; font-size: 24px; color: $ink3; font-family: m; delay: 400ms; in: {opacity:0, duration:0.4}) ×5 0;2;4;6;8時間
  # 行 = 札 (時刻 + 人数) + 棒 (幅 = 分 × 0.867) + 棒の中の右寄せの値
  div#row(left: 0px; top: "181;273;365;457;549"; width: 984px; height: 120px) ×5
    p#a(left: 40px; top: 18px; font-size: 34px; delay: "450ms;580ms;710ms;840ms;970ms"; in: {scale:0.8, y:16, opacity:0, duration:0.35, ease:'power2.out'}) 22時より前;22〜23時;23〜24時;24時以降;見ながら寝落ち
    p#b(left: 40px; top: 66px; font-size: 26px; color: $ink3; font-family: m; delay: "450ms;580ms;710ms;840ms;970ms"; in: {scale:0.8, y:16, opacity:0, duration:0.35, ease:'power2.out'}) 136人・11%;297人・24%;408人・33%;272人・22%;123人・10%
    div#bar(left: 292px; top: 22px; width: "381;357;327;298;287"; height: 70px; border-radius: 0px 20px 20px 0px; background: $muted; delay: "500ms;630ms;760ms;890ms;1020ms"; in: {scaleX:0, duration:0.75, ease:'power3.out', pivot:'left'})
    # 語で色が変わる棒 (ミント / 沈める紺 / ピンクを同じ形で重ねて溶かす)
    div#hot(left: 292px; top: 22px; width: "381;357;327;298;287"; height: 70px; border-radius: 0px 20px 20px 0px; background: "$mint;$dim;$dim;$pink;$pink"; overlap: b3.row.bar; in: {opacity:0, duration:0.3})
    p#val(left: 292px; cy: 57px; width: "368;344;314;285;274"; font-size: 34px; text-align: right; delay: "1000ms;1130ms;1260ms;1390ms;1520ms"; in: {opacity:0, duration:0.3}) 7時間19分;6時間52分;6時間18分;5時間44分;5時間31分
  # 22 時前との差 (斜線のピンクの枠 + 差の分)・7 時間 19 分の黄の基準線
  div#ghost(left: "493;482"; top: "472;564"; width: "82;94"; height: 70px; border-radius: 0px 20px 20px 0px; background: #FF5C9E29; pattern: hatch,45,#FF5C9E6B,13,7; border: 3px solid $pink; in: {scaleX:0, opacity:0, duration:0.45, ease:'power3.out', pivot:'left', stagger:{each:0.12}}) ×2
  p#glab(cx: "534;529"; cy: "496;588"; font-size: 26px; text-shadow: 0px 2px 6px #0A0A28E6; overlap: b3.ghost; in: {scale:0.5, opacity:0, duration:0.35, ease:'back.out(2.2)', stagger:{each:0.12}}) ×2 −95分;−108分
  div#ref(left: 861px; top: 280px; width: 4px; height: 670px; border-radius: 3px; background: $yellow; in: {scaleY:0, duration:0.45, ease:'power2.out', pivot:'top'})
  p#reflab(left: 742px; top: 252px; font-size: 24px; color: $navy; background: $yellow; border-radius: 20px; padding: 6px 14px; in: {scale:0.6, y:10, opacity:0, duration:0.35, ease:'back.out(2.2)'}) 22時前 7時間19分
  # 95 分の札 (大きな数字が弾み、下線が伸びる)
  div#call95(left: 40px; top: 1010px; width: 904px; height: 112px; border-radius: 30px; background: #FFFFFF14; border: 2px solid #FFFFFF24; in: {scale:0.85, y:30, opacity:0, duration:0.45, ease:'back.out(2.2)'})
    p#big(left: 26px; top: 8px; font-size: 76px; font-family: p; line-height: 1.2; in: {scale:0.3, opacity:0, duration:0.5, ease:'back.out(2.6)'}) 95
    p#u(left: .big.right+4; top: 45px; font-size: 34px) 分
    div#bar(left: 26px; top: 94px; width: 190px; height: 8px; border-radius: 4px; background: $pink; in: {scaleX:0, duration:0.4, ease:'power2.out', pivot:'left'})
    p#k(left: 250px; top: 18px; font-size: 30px) 22時前と24時以降の差
    p#k2(left: 250px; top: 60px; font-size: 24px; color: $ink2; font-family: m) 寝落ちとは108分差／24時以降＋寝落ち＝32%（395人）
svg#fx3(left: 14px; top: 1100px; width: 400px; height: 400px; part: burst3; overlap: b3; in: {scale:0.529, opacity:0, duration:0.55, ease:'power2.out'}; out: {opacity:0, duration:0.3, ease:'power1.in'}; bleed)

# 03 朝の眠気と居眠り: 凡例と目盛りを先に置き、黄の線 → ピンクの線が左から描かれ、点と値が順に弾む →「段階的」で札と右端の値を弾ませる・右下に居眠りの少女
section#sleepy(stagger: {each:0})
board#b4(n: "03"; t: "朝の眠気・授業中の居眠り")
  div#lg(left: 44px; top: "113;144"; width: 900px; height: 36px; delay: 300ms; in: {scale:0.8, y:10, opacity:0, duration:0.35, ease:'power2.out', stagger:{each:0.12}}) ×2
    div#sw(left: 0px; cy: 50%; width: 52px; height: 8px; border-radius: 4px; background: "$yellow;$pink")
    div#dot(left: 16px; cy: 50%; width: 24px; height: 24px; border-radius: 148px; background: "$yellow;$pink"; box-shadow: 0px 0px 0px 4px #1D2060)
    p#t(left: 68px; cy: 50%; font-size: 30px) 朝とても眠い{e}（全体 43%・528人）{/};授業中に週3回以上 居眠り{e}（全体 18%・222人）{/}
  # 目盛り (0〜60%・1% = 5.07 px・0% は 573)
  div#gl(left: 110px; top: "573;472;371;269"; width: 820px; height: 2px; background: #FFFFFF1A; delay: 300ms; in: {opacity:0, duration:0.4}) ×4
  p#yt(left: 21px; width: 75px; cy: "573;472;371;269"; font-size: 24px; text-align: right; color: $ink3; font-family: m; delay: 300ms; in: {opacity:0, duration:0.4}) ×4 0%;20%;40%;60%
  p#xt(cx: "113;230;347;463;580"; cy: 898px; font-size: 27px; color: $ink2; delay: 300ms; in: {opacity:0, duration:0.4}) ×5 22時前;22〜23時;23〜24時;24時以降;寝落ち
  # 線 (左から描く)・面 (薄く溶ける)・点 (弾む)・値 (上がる) を系列ごとに
  svg#aa(left: 158px; top: 368px; width: 720px; height: 502px; part: area_a; in: {opacity:0, duration:0.8})
  svg#ab(left: 158px; top: 368px; width: 720px; height: 502px; part: area_b; in: {opacity:0, duration:0.8})
  svg#la(left: 158px; top: 368px; width: 720px; height: 502px; part: line_a; in: wipe {dir: 'right', duration: 1.1, ease: 'power1.inOut'})
  svg#lb(left: 158px; top: 368px; width: 720px; height: 502px; part: line_b; in: wipe {dir: 'right', duration: 1.1, ease: 'power1.inOut'})
  div#da(left: "102;219;336;452;569"; top: "440;405;349;273;243"; width: 34px; height: 34px; border-radius: 148px; background: $yellow; border: 6px solid $deep; in: {scale:0, duration:0.35, ease:'back.out(3)', stagger:{each:0.25}}) ×5
  div#db(left: "102;219;336;452;569"; top: "521;506;476;430;405"; width: 34px; height: 34px; border-radius: 148px; background: $pink; border: 6px solid $deep; in: {scale:0, duration:0.35, ease:'back.out(3)', stagger:{each:0.25}}) ×5
  p#va(cx: "113;230;347;463;580"; cy: "422;392;336;260;224"; font-size: "28;20;20;20;28"; color: "#FFFFFF;$ink2;$ink2;$ink2;#FFFFFF"; in: {y:10, opacity:0, duration:0.3, ease:'power2.out', stagger:{each:0.25}}) ×5 24%;31%;42%;57%;63%
  p#vb(cx: "113;230;347;463;580"; cy: "562;544;513;468;445"; font-size: "28;20;20;20;28"; color: "#FFFFFF;$ink2;$ink2;$ink2;#FFFFFF"; in: {y:10, opacity:0, duration:0.3, ease:'power2.out', stagger:{each:0.25}}) ×5 8%;11%;17%;26%;31%
  div#step(left: 44px; top: 962px; width: 408px; height: 68px; border-radius: 32px; background: #FFD23F24; border: 3px solid $yellow; in: {scale:0.5, y:10, opacity:0, duration:0.45, ease:'back.out(2.2)'})
    svg#i(left: 24px; cy: 50%; width: 34px; height: 34px; part: trend)
    p#t(left: 69px; cy: 50%; font-size: 30px) 遅いほど 段階的に増加
  img#sleepy(left: 716px; top: 918px; width: 240px; height: 240px; object-fit: contain; delay: 600ms; in: {scale:0.5, y:40, rotation:8, opacity:0, duration:0.55, ease:'back.out(2.2)'}) [transparent][ref:@girl]授業中に机で居眠りする同じ少女 (紺のブレザーにピンクのリボンの制服): 開いたノートと鉛筆の上で組んだ腕に頭をのせ、目を閉じ、鼻から小さな丸い鼻ちょうちん。机ごと全体が入る斜め 3/4 の見下ろし、細い白のふちどりのステッカー、枠いっぱいに大きく
  note#note(top: 1062px; delay: 800ms; in: {opacity:0, duration:0.4}) ※スマホを手から離す時刻別・自己申告

# 04 2 週間の実験: 2 部屋の絵 → ルールの札 (22:30 が弾む) → 札 2 枚 → 参加の帯 → 文の頭で前半が上へ抜け、結果の 4 行 (前 → 後) が組み上がる
section#exp(stagger: {each:0})
board#b5(n: "04"; t: "2週間の実験")
  div#parta(left: 0px; top: 0px; width: 984px; height: 1150px; out: {y:-40, opacity:0, duration:0.3, ease:'power2.in'})
    img#room(left: 40px; top: 168px; width: 904px; height: 540px; border-radius: 34px; border: 3px solid #FFFFFF2E; main: kb {scale: [1.12, 1], ease:'power1.out'}; delay: 250ms; in: {scale:0.85, y:30, opacity:0, duration:0.5, ease:'back.out(2.2)'}) [ref:@girl]夜の小さな日本の家の、壁を挟んで隣り合う 2 部屋の断面図を横長の画面いっぱいに描く (周りに黒い余白や額縁を作らない)。左の部屋 (居間): 小さな棚の上でスマートフォンが立てて充電され、画面は暗く、充電ケーブルがミント色にやさしく光る。右の部屋 (寝室): 同じ少女がベッドで目を閉じて安らかに眠り、窓から三日月が見える。真ん中に閉じたドアのある壁。スマホが寝ている少女と別の部屋にあることがはっきり分かる。左上と右下に札が乗るので、そこは壁と床の平らな面にする
    p#pinphone(left: 94px; top: 214px; font-size: 28px; color: $navy; background: $mint; border-radius: 30px; padding: 15px 22px; box-shadow: 0px 8px 20px #0000004D; overlap: b5.parta.room; in: {scale:0.5, y:10, opacity:0, duration:0.4, ease:'back.out(2.2)'}) スマホは別の部屋で充電
    p#pinbed(left: 632px; top: 616px; font-size: 28px; color: $navy; background: #FFFFFF; border-radius: 30px; padding: 15px 22px; box-shadow: 0px 8px 20px #0000004D; overlap: b5.parta.room; in: {scale:0.5, y:10, opacity:0, duration:0.4, ease:'back.out(2.2)'}) 寝室にスマホなし
    # ルールの札 (黄の縁 + 上辺に乗る題の札 + 大きな時刻)
    div#rule(left: 40px; top: 736px; width: 904px; height: 196px; border-radius: 34px; background: #FFD23F1A; border: 3px solid $yellow; in: {scale:0.85, y:30, opacity:0, duration:0.45, ease:'back.out(2.2)'})
      p#tag(left: 28px; top: -24px; font-size: 26px; color: $navy; background: $yellow; border-radius: 24px; padding: 10px 20px) ルールはこれだけ
      p#time(left: 30px; top: 40px; font-size: 96px; font-family: p; line-height: 1.2; in: {scale:0.3, opacity:0, duration:0.5, ease:'back.out(2.6)'}) 22:30
      p#what(left: 372px; top: 44px; font-size: 42px; line-height: 1.3) スマホを別の部屋で充電[br]{wsm}希望者が 2週間 続ける{/}
    # 参加の帯 (84 人 → 76 人・90% まで伸びる)
    div#part(left: 40px; top: 960px; width: 904px; height: 150px; in: {scale:0.9, y:20, opacity:0, duration:0.4, ease:'power2.out'})
      p#t(left: 4px; top: 0px; font-size: 30px; color: $ink2) 参加の希望者 {pn}84{/}人 → 最後まで続けた {pm}76{/}人
      div#track(left: 4px; top: 86px; width: 896px; height: 26px; border-radius: 14px; background: #FFFFFF1F)
      div#fill(left: 4px; top: 86px; width: 806px; height: 26px; border-radius: 14px; background: $mint; overlap: b5.parta.part.track; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
      p#pc(left: 4px; top: 118px; font-size: 24px; color: $ink3; font-family: m) 続けられた人 90%
  # 結果 (語で出す容器・中の要素は容器からの遅れで組み上がる)
  div#res(left: 0px; top: 0px; width: 984px; height: 1150px)
    p#rc(left: 40px; top: 170px; font-size: 27px; background: #FFD23F24; border: 2px solid $yellow; border-radius: 30px; padding: 14px 22px; delay: 50ms; in: {scale:0.8, y:10, opacity:0, duration:0.35, ease:'back.out(2.2)'}) 22:30 別の部屋で充電 ×2週間・続けた76人
    # 行 = 題 + 前 (薄い) → 矢印 → 後 (大きいポップ体)・2・3 行目はミントの地
    div#rr(left: 40px; top: "168;299;429;560"; width: 904px; height: 180px; border-radius: 30px; background: "#FFFFFF0F;#39E0B81A;#39E0B81A;#FFFFFF0F"; border: "2px solid #FFFFFF1A;2px solid #39E0B88C;2px solid #39E0B88C;2px solid #FFFFFF1A"; delay: 150ms; in: {scale:0.9, y:40, opacity:0, duration:0.45, ease:'back.out(1.6)', stagger:{each:0.1}}) ×4
      p#k(left: 28px; top: 22px; font-size: 32px; line-height: 1.3) 寝る時刻[br]{ks}平日の平均{/};睡眠時間[br]{ks}平日の平均{/};朝とても眠い;週3回以上の居眠り
      p#bef(left: 330px; top: 30px; width: 230px; font-size: 38px; text-align: right; color: $ink3) 0時31分;6時間04分;44人 58%;22人 29%
      svg#arr(left: 578px; top: 22.5%; width: 44px; height: 36px; part: "arr_gray;arr_mint;arr_mint;arr_gray")
      p#aft(left: 632px; top: 20px; font-size: 48px; font-family: p; line-height: 1.25) 23時58分;6時間41分;26人 {as}34%{/};13人 {as}17%{/}
    p#dl1(left: 69px; top: 358px; font-size: 30px; color: $navy; background: $sky; border-radius: 26px; padding: 10px 20px; delay: 600ms; in: {scale:0.5, opacity:0, duration:0.35, ease:'back.out(2.2)'}) 33分 早く
    p#dl2(left: 69px; top: 555px; font-size: 30px; color: $navy; background: $mint; border-radius: 26px; padding: 10px 20px; in: {scale:0.3, opacity:0, duration:0.45, ease:'back.out(3)'}) +37分
    # 前 (灰) と後 (ミント) の細い棒 (割合の長さ)
    div#mba(left: 370px; top: "504;635"; width: "220;110"; height: 18px; border-radius: 0px 9px 9px 0px; background: #6E73B0; delay: 700ms; in: {scaleX:0, duration:0.5, ease:'power2.out', pivot:'left'}) ×2
    div#mbb(left: 370px; top: "524;655"; width: "129;65"; height: 18px; border-radius: 0px 9px 9px 0px; background: $mint; in: {scaleX:0, duration:0.5, ease:'power2.out', pivot:'left'}) ×2
    p#mla(left: "475;365"; top: "499;630"; font-size: 24px; color: $ink3; delay: "350ms;450ms"; in: {scale:0.9, y:40, opacity:0, duration:0.45, ease:'back.out(1.6)'}) ×2 実験前 58%;実験前 29%
    p#mlb(left: "384;320"; top: "519;650"; font-size: 24px; delay: "350ms;450ms"; in: {scale:0.9, y:40, opacity:0, duration:0.45, ease:'back.out(1.6)'}) ×2 2週間後 34%;2週間後 17%
    note#note(top: 1060px; delay: 1000ms; in: {opacity:0, duration:0.4}) ※希望者だけの実験で、比べる対照の群はありません
svg#fx5(left: 590px; top: 476px; width: 520px; height: 520px; part: burst5; overlap: b5; in: {scale:0.652, opacity:0, duration:0.55, ease:'power2.out'}; out: {opacity:0, duration:0.3, ease:'power1.in'}; bleed)

# 05 続けるコツ: 理由の 2 枚 (1 枚目が弾んで icon が震える) → 目覚まし時計が傾いて弾み震える + コツの 3 行 → 黄の下線
section#tip(stagger: {each:0})
board#b6(n: "05"; t: "続けるコツ")
  p#lead(left: 44px; top: 174px; font-size: 36px; delay: 300ms; in: {scale:0.9, y:16, opacity:0, duration:0.4, ease:'power2.out'}) 続けられなかった{b8}8{/}人の理由で多かったのは…
  div#rsn(left: "27;341"; top: 290px; width: 432px; height: 250px; border-radius: 34px; background: "#FF5C9E1F;#FFFFFF12"; border: "2px solid #FF5C9EB3;2px solid #FFFFFF24"; delay: "500ms;650ms"; in: {scale:0.6, y:30, opacity:0, duration:0.45, ease:'back.out(2.2)'}) ×2
    svg#ic(cx: 50%; top: 12%; width: 110px; height: 110px; part: "rsn_alarm;rsn_chat")
    p#t(cx: 50%; top: 160px; font-size: 40px) 目覚ましがスマホ;友だちへの返信
  img#alarm(left: 30px; top: 628px; width: 430px; height: 430px; object-fit: contain; in: {scale:0.3, y:60, rotation:-20, opacity:0, duration:0.55, ease:'back.out(2.2)'}) [transparent]かわいいレトロな双子ベルの目覚まし時計: 月の黄色の本体、ピンクのベルとハンマー、目盛りだけの丸い白い文字盤 (数字なし)、短い針 2 本、鳴っていることを示すベルのまわりの小さな曲線。細い白のふちどりのステッカー、枠いっぱいに大きく
  p#tip(left: 456px; top: 682px; font-size: 62px; font-family: p; line-height: 1.35; in: {scale:0.8, y:30, opacity:0, duration:0.45, ease:'back.out(2.2)'}) {y}目覚まし時計{/}を[br]{s33}用意するのが{/}[br]続けるコツ！
  div#tipline(left: 462px; top: 946px; width: 470px; height: 12px; border-radius: 6px; background: $yellow; in: {scaleX:0, duration:0.45, ease:'power3.out', pivot:'left'})
svg#fx6(left: -27px; top: 759px; width: 640px; height: 640px; part: burst6; overlap: b6; in: {scale:0.690, opacity:0, duration:0.55, ease:'power2.out'}; out: {opacity:0, duration:0.3, ease:'power1.in'}; bleed)

# まとめ: 結論の 3 枚 (番号 + 大きな数字 + 色の下線 + 文) が順に弾み、注記の板は「数字は」で出て「原因が」で縁が黄に 2 度光る
section#summary(stagger: {each:0})
board#b7(n: "まとめ"; nw: 93)
  div#sm(left: 40px; top: "88;252;416"; width: 904px; height: 214px; border-radius: 32px; background: #FFFFFF0F; border: 2px solid #FFFFFF1F; delay: 350ms; in: {scale:0.85, y:40, opacity:0, duration:0.45, ease:'back.out(1.6)', stagger:{each:0.2}}) ×3
    p#n(left: 24px; top: 24px; width: 54px; font-size: 30px; font-family: p; text-align: center; color: $navy; background: $yellow; border-radius: 148px; padding: 12px 0px) 1;2;3
    p#st(left: 24px; top: 84px; font-size: 76px; font-family: p; line-height: 1.2) 35{u}%{/};95{u}分差{/};+37{u}分{/}
    div#bar(left: 24px; top: 86%; width: 220px; height: 8px; border-radius: 4px; background: "$pink;$yellow;$mint")
    p#tx(left: 292px; top: 30px; font-size: 33px; line-height: 1.5) 高校生の{y}3人に1人以上{/}が[br]平日6時間未満しか寝ていない;離すのが1時間遅いと睡眠は{y}約30分{/}短く[br]22時前と24時以降で95分の差[br]眠気・居眠りも同じ順に増える;別の部屋に置くだけで2週間で[br]睡眠+37分・朝の眠気58%→34%[br]続けるコツは{y}目覚まし時計{/}
  div#notes(left: 40px; top: 876px; width: 904px; height: 238px; border-radius: 32px; background: #090A248C; border: 3px solid #FFFFFF2E; in: {scale:0.9, y:30, opacity:0, duration:0.4, ease:'power2.out'})
    p#tag(left: 24px; top: 22px; font-size: 26px; background: #FFFFFF29; border-radius: 24px; padding: 10px 20px) 注記
    p#li(left: 30px; top: "59;89;120"; font-size: 28px; color: $ink2; font-family: m) ×3 ・数字はすべて自己申告;・調査は関係を示すもので、スマホだけが原因とは言い切れない;・実験は希望者だけで、比べる対照の群はない
    div#hl(left: 0px; top: 0px; width: 904px; height: 238px; border-radius: 32px; border: 3px solid $yellow; opacity: 0)

# 締め: 地だけに戻り、2 行の呼びかけ → 伸びをする少女が下から弾んで漂う → 出典 (常設の上端は前の場面の終わりで消す)
section#end(stagger: {each:0})
p#ea(cx: 540px; cy: 384px; font-size: 84px; font-family: p; line-height: 1.3; in: {scale:0.6, y:30, opacity:0, duration:0.45, ease:'back.out(2.2)'}) 今夜は、
p#eb(cx: 540px; cy: 504px; font-size: 100px; font-family: p; line-height: 1.3; in: {scale:0.5, y:30, opacity:0, duration:0.5, ease:'back.out(2.4)'}) スマホを{y}別の部屋{/}へ。
img#morning(left: 230px; top: 690px; width: 620px; height: 620px; object-fit: contain; in: {scale:0.4, y:80, opacity:0, duration:0.6, ease:'back.out(1.8)'}) [transparent][ref:@girl]同じ少女 (紺のブレザーにピンクのリボンの制服) が目覚めた直後に両腕を上に伸ばして嬉しそうに伸びをする、すっきりした明るい笑顔、まわりに小さなきらめき。上半身から膝まで、細い白のふちどりのステッカー、枠いっぱいに大きく
p#src(cx: 540px; top: 1376px; font-size: 26px; line-height: 1.5; text-align: center; color: $ink2; font-family: m; in: {opacity:0, duration:0.5}) 調査：よふかしラボ（架空の教育NPO）[br]全国の高校1〜3年生 1,236人・オンライン・自己申告
svg#fx8(left: 110px; top: 570px; width: 860px; height: 860px; part: burst8; overlap: morning; in: {scale:0.750, opacity:0, duration:0.55, ease:'power2.out'}; out: {opacity:0, duration:0.3, ease:'power1.in'}; bleed)
```

```timeline.txt
#v2
cast n = "明るくクリアな若い女性のナレーター、10 代後半から 20 代前半、ピッチはやや高めでハキハキとエネルギッシュ、親しみやすく聞き取りやすい" speed=115%
silence head=0ms tail=0ms

*** hook
bgm music
@n: [silence:350ms][>#glow -350ms][♪vibe -1.4dB -300ms][>#bz_l -300ms][>#bz_r -300ms][!#glow to,{x:6, duration:0.05, repeat:9, yoyo:true, ease:'none'} -300ms][!#bz_l to,{opacity:0, duration:0.3} +250ms][!#bz_r to,{opacity:0, duration:0.3} +250ms][!#bz_l to,{opacity:1, duration:0.18} +600ms][!#bz_r to,{opacity:1, duration:0.18} +600ms][♪vibe -5.2dB +600ms][!#glow to,{x:6, duration:0.05, repeat:9, yoyo:true, ease:'none'} +600ms][!#bz_l to,{opacity:0, duration:0.3} +1150ms][!#bz_r to,{opacity:0, duration:0.3} +1150ms][!#glow to,{opacity:0.55, scale:0.92, duration:0.6, repeat:5, yoyo:true, ease:'sine.inOut'} +1250ms][>#q.l1][♪pop_hi -5.2dB +20ms][>#q.l2 +280ms]寝る前のスマホ、何時に手放してる？[silence:250ms]
[>#subtitle]
@: [<#q -350ms][>#heroshade -150ms][♪whoosh_swing -6dB -100ms][>#ttl.kicker -50ms][!#glow to,{opacity:0.35, duration:0.5} -50ms][>#ttl.t1 +30ms][♪rise_pop -6dB +130ms][>#ttl.t2 +150ms][>#ttl.t3 +310ms][>#ttl.ul +650ms][>#ttl.ch1 +700ms][>#ttl.ch2 +820ms][>#ttl.ch3 +940ms][>#ttl.fict +1150ms]全国の高校生、[br][♪tick -9dB -50ms to=1.4s]{y}1,236人{/}に聞きました。[silence:80ms]

*** dist
se whoosh_short -4.4dB
@: [silence:320ms][!#pd[1] .on -120ms][♪pop_soft -6dB +230ms][♪pop_soft -7dB +380ms][♪pop_soft -7dB +530ms]平日の睡眠は、[br][♪tick -10dB to=1.4s]平均[!#b2.hero.h count +110ms][!#b2.hero.m count +110ms]{y}6時間21分{/}[♪sparkle -7dB +500ms]。
@: [silence:220ms]6時間未満の人が[>#b2.hot[*] -100ms][!#b2.col[3] to,{opacity:0.4, duration:0.3} -100ms][!#b2.col[4] to,{opacity:0.4, duration:0.3} -100ms][!#b2.col[5] to,{opacity:0.4, duration:0.3} -100ms][!#b2.colv[3] to,{opacity:0.62, duration:0.3} -100ms][!#b2.colv[4] to,{opacity:0.62, duration:0.3} -100ms][!#b2.colv[5] to,{opacity:0.62, duration:0.3} -100ms][!#b2.colx[3] to,{opacity:0.62, duration:0.3} -100ms][!#b2.colx[4] to,{opacity:0.62, duration:0.3} -100ms][!#b2.colx[5] to,{opacity:0.62, duration:0.3} -100ms][>#b2.brk -50ms][>#b2.pill][♪pop_hi -6dB -50ms][♪sparkle -8dB +150ms][>#fx2 +150ms][<#fx2 +400ms]{y}35%{/}と、[|][>#b2.stamp -50ms][♪rise_pop -6dB]{y}3人に1人{/}を超えます。[silence:80ms]

*** phone
se whoosh_short -4.4dB
@: [silence:320ms][=#pd[1] -120ms][!#pd[2] .on -120ms][♪pop_soft -7dB +130ms][♪pop_soft -8dB +330ms][♪pop_soft -8dB +530ms]手放す時刻別に見ると、[|][>#b3.row[1].hot -50ms][!#b3.row[1].val recolor,$navy {duration: .3} -50ms][!#b3.row[1] punch {scale: 1.04, duration: .36, pivot: 'left'} -50ms][♪chime_soft -7dB]22時前は{y}7時間19分{/}。
@: [silence:220ms][>#b3.row[4].hot -50ms][!#b3.row[4].val recolor,$navy {duration: .3} -50ms][!#b3.row[4] punch {scale: 1.04, duration: .36, pivot: 'left'} -50ms][>#b3.row[2].hot -50ms][>#b3.row[3].hot -50ms][♪pop_hi -7dB]24時以降は{y}5時間44分{/}、[|][>#b3.row[5].hot -50ms][!#b3.row[5].val recolor,$navy {duration: .3} -50ms][!#b3.row[5] punch {scale: 1.04, duration: .36, pivot: 'left'} -50ms][♪pop_hi -7dB]見ながら寝落ちは[br]{y}5時間31分{/}。
@: [silence:250ms]1時間遅いごとに[br][>#b3.per30 -100ms][♪click -8dB]{y}約30分{/}短く、[|][>#b3.ref -50ms][>#b3.reflab -50ms][♪whoosh_short -7dB +100ms][>#b3.ghost[*] +250ms][>#b3.glab[*] +550ms]22時前と24時以降では[br][>#b3.call95 -150ms][>#b3.call95.big -50ms][>#b3.call95.bar +150ms][♪sparkle -6dB][>#fx3 +50ms][<#fx3 +300ms]{y}95分{/}の差です。[silence:100ms]

*** sleepy
se whoosh_short -4.4dB
@: [silence:350ms][=#pd[2] -150ms][!#pd[3] .on -150ms][>#b4.la][>#b4.da[*]][>#b4.aa +300ms][>#b4.va[*] +100ms][♪tick -10dB +50ms to=1.4s][!#b4.sleepy to,{y:-10, duration:0.9, yoyo:true, repeat:5, ease:'sine.inOut'} +850ms]朝の眠気も[br][>#b4.lb][>#b4.db[*]][>#b4.ab +300ms][>#b4.vb[*] +100ms][♪tick -10dB +50ms to=1.4s]授業中の居眠りも、[|]遅いほど[br][>#b4.step -100ms][!#b4.va[5] punch {scale: 1.25, duration: .4} +100ms][!#b4.vb[5] punch {scale: 1.25, duration: .4} +100ms][♪pop_hi -7dB]{y}段階的に{/}増えます。[silence:430ms]

*** exp
se whoosh_short -4.4dB
@: [silence:420ms][=#pd[3] -220ms][!#pd[4] .on -220ms]そこで、[>#b5.parta.rule -150ms][>#b5.parta.rule.time -50ms][♪pop_hi -6dB]{y}22時30分{/}に[br]スマホを[>#b5.parta.pinphone -50ms][>#b5.parta.pinbed +300ms][♪chime_soft -8dB +100ms]別の部屋で充電する、[|][>#b5.parta.part +100ms][>#b5.parta.part.fill +300ms][♪click -8dB]{y}2週間{/}の実験。
@: [silence:300ms][<#b5.parta -250ms][>#b5.res -100ms][♪whoosh_short -6dB -100ms]続けた[♪pop_soft -7dB]76人は、[br]睡眠が[!#b5.res.rr[2].aft punch {scale: 1.12, duration: .4} -50ms][>#b5.res.dl2 -50ms][♪chime_ok -7dB][>#fx5 +50ms][<#fx5 +300ms]{y}37分{/}増え、[|]朝とても眠い人は[br][♪sparkle -7dB +250ms]{y}58%{/}から[>#b5.res.mbb[*] -100ms][!#b5.res.rr[3].aft punch {scale: 1.12, duration: .4} -50ms]{y}34%{/}に減りました。[silence:100ms]

*** tip
se whoosh_short -4.4dB
@: [silence:350ms][=#pd[4] -150ms][!#pd[5] .on -150ms][♪pop_soft -7dB +200ms][♪pop_soft -8dB +350ms]続かなかった理由は[br][!#b6.rsn[1] to,{scale:1.07, duration:0.18, yoyo:true, repeat:1, ease:'power2.out'} -50ms][!#b6.rsn[1].ic to,{rotation:8, duration:0.08, repeat:7, yoyo:true, ease:'none'} +200ms][♪pop_hi -7dB]「目覚ましがスマホ」。
@: [>#b6.alarm -100ms][!#b6.alarm to,{rotation:6, duration:0.06, repeat:13, yoyo:true, ease:'none'} +450ms][>#b6.tip +50ms][♪alarm -6dB to=1.5s][♪rise_pop -9dB +50ms][>#fx6 +250ms][<#fx6 +500ms]{y}目覚まし時計{/}を用意するのが、[br][>#b6.tipline]続けるコツです。[silence:80ms]

*** summary
se whoosh_short -4.4dB
@: [silence:320ms][♪pop_soft -7dB +80ms][♪pop_soft -7dB +280ms][♪pop_soft -7dB +480ms]ただし、[>#b7.notes -100ms][♪click -9dB]数字は自己申告。
@: [!#b7.notes.hl to,{opacity:1, duration:0.3, repeat:3, yoyo:true}]原因がスマホだけとは[br]言い切れません。[silence:70ms]
[<#hchip][<#pd]

*** end
se whoosh_swing -6dB
[<#subtitle]
@: [silence:280ms][>#ea -80ms][>#eb -20ms][♪chime_ok -6dB +200ms][>#morning +300ms][>#fx8 +550ms][<#fx8 +800ms][>#src +600ms][!#morning to,{y:-14, duration:0.7, yoyo:true, repeat:3, ease:'sine.inOut'} +950ms]今夜は、スマホを別の部屋へ。[silence:2.1s]
```

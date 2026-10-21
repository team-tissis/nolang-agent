# story · office-comedy (hf の全力版を draft src に全量で写した物 — 部下が上司をにこやかに褒め殺す 2 人の職場コメディ) — canvas 720x1280・6 cut

見せる作り: 常設の層 (上下の暗いグラデ・題の帯の決め語が語で弾む)・冒頭だけの組織図 (svg の部品を def で組む・語で × を叩きつけ、資格証を脈打たせる)・台詞ごとの全面の絵替え 17 枚 (寄り / 引き / 横流れ / 打ち込みの kb・cut の中は重ねて替える)・右から被さる切替 + 風切り音・cut ごとの 2 段テロップ (def 1 つ・落ちの 2 行目を語で落として揺らす)・話者札つき字幕・締めの 1 枚 (真顔の寄り + 周辺減光 + 太鼓で絵とテロップが揺れる)・語に結んだ効果音 10

```design.txt
#v2
# 学ぶ作り: 全 cut を通す常設の層 (上下の暗いグラデ・題の帯 — 帯の決め語だけを語で弾ませる)・冒頭だけの図 (svg の部品を def で組んだ組織図 — 節点が弾み、語で × を叩きつけ、語で資格証を脈打たせる)
# 台詞ごとの全面の絵替え (寄り / 引き / 横流れ / 打ち込みの kb・cut 頭は右から被さる切替)・cut ごとの 2 段テロップ (def 1 つ — 前置きを先に置き、落ちの 2 行目を語で落として揺らす)
# 話者札つき字幕・締めの 1 枚 (笑顔を真顔の寄りに替え、周辺減光 + 太鼓で絵とテロップを揺らす)
# 座標は hf の 1080x1920 × 2/3。地は濃紺・書体は テロップと帯 = Dela・字幕 = 源真ゴシック・絵は全部 [ref:@sheet] (2 人の設定画) で顔と服を揃え、2 度使う絵は根の image に 1 回
canvas 720x1280 bg=#0B0F1A
palette y=#FFD43B punch=#FFE14D ink=#111111 navy=#10182D sub=#1F5FBF boss=#9B2335 bg=#0B0F1A
run big { color: $y; font-size: 41px }
font "源真ゴシック Heavy"
fonts d="デラゴシック Regular" m="源真ゴシック Medium"
prompt_tail "【上司】55歳くらいの日本人男性の部長。少しふくよかな体型、後ろになでつけた白髪まじりのグレーの髪、太い眉、丸顔、ひげなし。濃紺のスリーピーススーツ、えんじ色のネクタイ、金のネクタイピン、左胸に金の社章バッジ。余裕たっぷりで偉そうな雰囲気。【部下】27歳くらいの日本人男性社員。細身、短く整えた黒髪、細い銀縁の四角いメガネ、白いワイシャツにライトグレーのスーツ、紺色の細いネクタイ、首から青いストラップの社員証 (カード面は無地)。礼儀正しく、にこやかな表情。日本のテレビアニメ風の2Dイラスト。セル塗り、くっきりした主線、やわらかい光、落ち着いた上品な色調、職場コメディの一場面。画像内に文字・ロゴ・字幕・吹き出しは一切描かない。縦長の構図。"
image sheet = "キャラクター設定画。左に上司、右に部下が並んで立つ全身像、2人とも正面向き、白い無地の背景、足元まで全身が入る。" aspect=3:2
image sub_smile = "[ref:@sheet]部下のバストアップ。にこやかに目を細めて、丁寧に褒めるように話している。胸の前で軽く両手を合わせている。顔は画面の左側を向いている。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。背景は少しぼかす。" aspect=9:16
image boss_pleased = "[ref:@sheet]上司のバストアップ。褒められたと勘違いして、照れくさそうに嬉しそうに笑い、片手を後頭部に当てている。頬が少し赤い。顔は画面の右側を向いている。背景は部長室、少しぼかす。" aspect=9:16
sound pop = "紙筒で鳴らす乾いた軽いポンという弾ける音"
sound stamp = "判子を紙に強く押す乾いた音"
sound chiin = "お鈴を打つ温かく太いチーンという音"
sound whoosh = "風を切る明るく強いシュッという振りの音"
sound hyoshigi = "拍子木を打つ鋭く乾いた音"
sound slide = "小さなスライドホイッスルの高く可愛い下降音"
sound taiko = "和太鼓の大太鼓を一打、低く重く響く"
sfx off
shadow_default 0
cut { stagger: 0 }
img { in: none; out: none }
p { out: none }
div { out: none }
bgm#music(fade: 600,60; keys: "0:0") ファゴットとマリンバとアコースティックギターが跳ねる、とぼけて愉快な軽いコメディ曲
# 字幕 (白の極太 + 紺の縁・中央・話者札は上・文ごとの札・16 字を超える文は読点で 2 行)
subtitle(left: 40px; width: 640px; top: 960px; font-size: 39px; line-height: 1.3; color: #FFFFFF; stroke: #0D1222,4; background: none; unit: sentence; wrap: comma,16; label: above; label_in: pop; lead: 0; tail: 250; hold: same,1500; in: {y:12, opacity:0, duration:.16, ease:'power2.out'})

# 2 段テロップ (Dela・前置き 白 52 / 落ち 黄 75 (9 字以上は 65)・-2° 傾き・拡大から back で着地・落ちは着地後に横に揺れる)
def telop(setup, punchline, punch_size=75) = group(left: 0px; top: 687px; width: 720px; height: 170px)
  p#setup(cx: 50%; top: 0px; overlap: self.punch; font-size: 52px; font-family: d; line-height: 1.12; color: #FFFFFF; stroke: $ink,5; text-shadow: 0px 5px 0px #0000008C; transform: rotate(-2deg); transform-origin: 50% 60%; in: {scale:1.6, opacity:0, rotation:-4, duration:.28, ease:'back.out(2.2)'}; content: {setup})
  p#punch(cx: 50%; top: 62px; font-size: {punch_size}; font-family: d; line-height: 1.12; color: $punch; stroke: $ink,5; text-shadow: 0px 7px 0px #00000099; transform: rotate(-2deg); transform-origin: 50% 60%; in: {scale:1.7, opacity:0, rotation:3, duration:.3, ease:'back.out(2.6)'}; content: {punchline})

# 組織図の部品 (hf の svg を節点ごとに切った物: 結線 2 段・役員 / 管理職 / 社員の札・資格証・赤い ×)。× と社員の資格証は語で動かすので別の部品
svg links_upper = """<svg viewBox="0 0 900 640"><path d="M450 150 V215 M250 215 H650 M250 215 V260 M650 215 V260" stroke="#ffffff" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85"/></svg>"""
svg links_lower = """<svg viewBox="0 0 900 640"><path d="M250 370 V420 M650 370 V420 M150 420 H750 M150 420 V460 M450 420 V460 M750 420 V460" stroke="#ffffff" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.85"/></svg>"""
svg plate_exec = """<svg viewBox="-120 -62 240 124"><rect x="-120" y="-62" width="240" height="124" rx="22" fill="#8e2232"/><circle cx="-52" cy="-14" r="20" fill="#fff"/><path d="M-86 36 a34 30 0 0 1 68 0 z" fill="#fff"/><g transform="translate(42 0)"><rect x="-34" y="-34" width="68" height="56" rx="6" fill="#fff4cf"/><circle cx="0" cy="-8" r="12" fill="#e2a51b"/><path d="M-8 2 l-6 22 l14 -8 l14 8 l-6 -22 z" fill="#c8551b"/></g></svg>"""
svg plate_mgr = """<svg viewBox="-120 -56 240 112"><rect x="-120" y="-56" width="240" height="112" rx="22" fill="#2c3e66"/><circle cx="-52" cy="-12" r="19" fill="#fff"/><path d="M-84 34 a32 28 0 0 1 64 0 z" fill="#fff"/><g transform="translate(42 0)"><rect x="-32" y="-32" width="64" height="52" rx="6" fill="#fff4cf"/><circle cx="0" cy="-8" r="11" fill="#e2a51b"/><path d="M-7 2 l-6 20 l13 -7 l13 7 l-6 -20 z" fill="#c8551b"/></g></svg>"""
svg plate_staff = """<svg viewBox="-110 -52 220 104"><rect x="-110" y="-52" width="220" height="104" rx="20" fill="#3d6fb6"/><circle cx="-48" cy="-12" r="17" fill="#fff"/><path d="M-78 32 a30 26 0 0 1 60 0 z" fill="#fff"/></svg>"""
svg badge = """<svg viewBox="-30 -30 60 50"><rect x="-30" y="-30" width="60" height="48" rx="6" fill="#fff4cf"/><circle cx="0" cy="-8" r="10" fill="#e2a51b"/><path d="M-7 1 l-5 18 l12 -6 l12 6 l-5 -18 z" fill="#c8551b"/></svg>"""
svg red_x = """<svg viewBox="-38 -38 76 76"><rect x="-44" y="-9" width="88" height="18" rx="9" fill="#ff2d3d" transform="rotate(45)"/><rect x="-44" y="-9" width="88" height="18" rx="9" fill="#ff2d3d" transform="rotate(-45)"/></svg>"""
def org_node(plate) = div(border-radius: 0px; border: none; box-shadow: none; padding: 0px; in: {scale:.2, opacity:0, duration:.32, ease:'back.out(2)'})
  svg#plate(part: {plate})
def slam_x() = svg(width: 51px; height: 51px; part: red_x; in: {scale:2.4, opacity:0, duration:.18, ease:'power4.in'})

# 常設の層: 上下の暗いグラデ (上 330 px・下 760 px) と題の帯 (紺の板・下に黄の縁・硬い影・「役職はあります。」だけ大きく黄)
div#shade_top(border-radius: 0px; border: none; box-shadow: none; padding: 0px; left: 0px; top: 0px; width: 720px; height: 220px; background: linear(#0508129E,#05081200,180); in: none)
div#shade_bottom(border-radius: 0px; border: none; box-shadow: none; padding: 0px; left: 0px; top: 773px; width: 720px; height: 507px; background: linear(#05081200,#05081273@45%,#050812CC,180); in: none)
div#title_bar.sticky(left: 56px; top: 47px; width: 608px; height: 66px; background: $navy; border-radius: 4px; border-bottom: 5px solid $y; box-shadow: 0px 7px 0px #00000059; in: none)
  p#title(cx: 50%; cy: 52%; font-size: 33px; font-family: d; color: #FFFFFF; letter-spacing: .01em) 資格はないけど、{big}役職はあります。{/}

# 発端: 2 人の引き → 幕を沈めて組織図 (「上の人は誰も資格なし」を × で見せる) → 部下の驚き
section#org_chart
img#desk_wide(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部長席の引きの構図。大きな木製デスクの革張りの椅子に上司が深く座って満足げに微笑み、デスクの横に部下がタブレットを胸に抱えて立ち、にこやかに上司に話しかけている。2人とも全身に近い大きさで画面に収まる。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。
img#sub_surprised(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部下のバストアップ。少し目を見開いて意外そうな表情、片手でメガネのブリッジを押し上げている。顔は画面の左側を向いている。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。背景は少しぼかす。
# 組織図 (幕で沈めた上に、節点が順に弾み、線が出て、上の 3 つの資格証に赤い × が叩きつけられ、下の 3 つの資格証が脈打つ)
div#org_dim(inset: 0; border-radius: 0px; border: none; box-shadow: none; padding: 0px; background: #080C1A94; in: {opacity:0, duration:.3, ease:'power1.out'}; out: {opacity:0, duration:.25, ease:'power1.in'})
group#org(in: {stagger: {each: .06}}; left: 60px; top: 253px; width: 600px; height: 427px; out: {opacity:0, duration:.25, ease:'power1.in'})
  svg#upper(part: links_upper; in: {opacity:0, duration:.3})
  svg#lower(part: links_lower; in: {opacity:0, duration:.3})
  org_node#exec(left: 220px; top: 22px; width: 160px; height: 83px; plate: plate_exec)
    slam_x#cross(left: 83px; top: 12px)
  org_node#mgr_l(left: 87px; top: 173px; width: 160px; height: 75px; plate: plate_mgr)
    slam_x#cross(left: 84px; top: 9px; width: 48px; height: 48px)
  org_node#mgr_r(left: 353px; top: 173px; width: 160px; height: 75px; plate: plate_mgr)
    slam_x#cross(left: 84px; top: 9px; width: 48px; height: 48px)
  org_node#staff(left: "27;227;427"; top: 312px; width: 147px; height: 69px; plate: plate_staff) ×3
    svg#cert(left: 80px; top: 15px; width: 40px; height: 33px; part: badge)
telop#nobody(setup: "上の人たち、"; punchline: "誰も持ってなかった。"; punch_size: 65)

# 上司の自慢 → 部下の褒め殺し (落ち「役職取得。」) → 照れる上司の打ち込み
section#promoted
img#boss_smug(inset: 0; main: kb {scale: [1.13, 1.05], focus: ['50% 40%', '50% 40%']}) [ref:@sheet]上司のバストアップ。革張りの椅子にふんぞり返って腕を組み、得意げにニヤリと笑っている。顔は画面の右側を向いている。背景は部長室、少しぼかす。
img#sub_praise(inset: 0; content: @sub_smile; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']})
# 打ち込み (1.18 → 1.07 を back で・その後 1.10 へ)
img#boss_blush(inset: 0; content: @boss_pleased; in: {scale:1.1, duration:.35, ease:'back.out(2)'}; main: kb {scale: [1.07, 1.1], focus: ['50% 40%', '50% 40%']})
telop#rank_first(setup: "資格取得より、"; punchline: "役職取得。")

# 資格を勧めない理由 → 横流れでうなずく上司 → メモする部下 (落ち「自己申告。」)
section#experience
img#sub_ask(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部下のバストアップ。タブレットを胸に抱え、首を少しかしげて丁寧に質問している、柔らかい笑顔。顔は画面の左側を向いている。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。背景は少しぼかす。
# 横流れ (x +18 → −18)
img#boss_nod(inset: 0; main: kb {scale: [1.08, 1.1], focus: ['29% 40%', '67% 40%']}) [ref:@sheet]上司のバストアップ。片手を胸に当て、目を閉じて、もっともらしく深くうなずいている。顔は画面の右側を向いている。背景は部長室、少しぼかす。
img#sub_memo(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部下のバストアップ。手帳にペンでメモを取りながら、にこやかにうなずいている。顔は画面の左側を向いている。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。背景は少しぼかす。
telop#self_report(setup: "実力の証明は、"; punchline: "自己申告。")

# 制度を尋ねる → はぐらかす上司の打ち込み → 「おや」の部下 (落ち「思ってました。」)
section#ask_rules
img#paper_offer(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部長席の横からの構図。部下が両手で白紙の書類を上司に差し出して丁寧に質問している。椅子に座った上司は書類から目をそらし、気まずそうに天井の方を見ている。2人とも上半身以上が大きく画面に収まる。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。
img#boss_dodge(inset: 0; in: {scale:1.1, duration:.35, ease:'back.out(2)'}; main: kb {scale: [1.07, 1.1], focus: ['50% 40%', '50% 40%']}) [ref:@sheet]上司のバストアップ。気まずそうに目をそらし、親指で自分の肩越しに後ろの方を指して、話をはぐらかしている。こめかみに汗が一筋。顔は画面の右側を向いている。背景は部長室、少しぼかす。
img#sub_puzzled(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部下のバストアップ。口元に軽く片手を添え、目を少し丸くして『おや』と意外そうな表情。それでも口角は上がった丁寧な笑顔。顔は画面の左側を向いている。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。背景は少しぼかす。
telop#not_expert(setup: "専門家かと"; punchline: "思ってました。")

# 窓の前で胸を張る上司 → 拍手する部下 (落ち「決定権は上。」) → 照れる上司の打ち込み (顔に寄せて)
section#overview
img#boss_window(inset: 0; main: kb {scale: [1.13, 1.05], focus: ['50% 40%', '50% 40%']}) [ref:@sheet]上司が大きな窓の前に立ち、両手を腰に当てて胸を張り、窓の外の高層ビル街を見下ろしている。斜め後ろからの全身に近い構図で、上司の横顔が少し見える。誇らしげな表情。明るい昼の光。
img#sub_clap(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部下のバストアップ。胸の前で小さく拍手しながら、感心したように目を細めてにこやかに笑っている。顔は画面の左側を向いている。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。背景は少しぼかす。
# 打ち込み 2 (顔を上に寄せて 1.30 → 1.20 を back で・その後 1.23 へ)
img#boss_blush_close(inset: 0; content: @boss_pleased; in: {scale:1.08, duration:.35, ease:'back.out(2)'}; main: kb {scale: [1.2, 1.23], focus: ['50% 24%', '50% 26%']})
telop#top_decides(setup: "知識は現場。"; punchline: "決定権は上。")

# 締め: 正面で語りかける部下 → 笑顔の寄り → 真顔の寄り + 周辺減光 (落ち「社内のプロ。」に太鼓で絵とテロップが揺れる)
section#deadpan
img#sub_talk(inset: 0; main: kb {scale: [1.04, 1.11], focus: ['50% 40%', '50% 45%']}) [ref:@sheet]部下のバストアップ、ほぼ正面向き。穏やかに微笑んで、片手を軽く上げて語りかけている。背景は明るく清潔な日本のオフィス (木目のデスク、観葉植物、大きな窓、白い壁)。背景は少しぼかす。
img#sub_smile_close(inset: 0; content: @sub_smile; main: kb {scale: [1.16, 1.24], focus: ['62% 27%', '58% 29%']})
img#sub_deadpan(inset: 0; main: kb {scale: [1.03, 1.16], focus: ['50% 40%', '50% 27%'], ease:'power1.inOut'}) [ref:@sheet]部下の顔のアップ。正面向きで、カメラ (見ている人) をまっすぐ見つめている。笑顔は完全に消えた無表情の真顔。口は真一文字。メガネのレンズが少し光る。背景はぼかしたオフィスで、少し暗めの照明。
# 真顔の周辺減光 (中心 50% 38%・40% から外へ)
veil#vignette(background: radial(#00000000@40%,#0000009E,50%,38%); in: {opacity:0, duration:.6, ease:'power2.out'})
telop#inhouse_pro(setup: "業界のプロ？"; punchline: "社内のプロ。")
```

```timeline.txt
#v2
# cut = 6 場面 = 次の絵が右 38% から被さって来る境目 (旧場面は動かない・0.26 秒)・その頭に風切り音。cut の中の絵替えは [>#次の絵][<#前の絵 +350] で重ねて替える
# 落ちは毎 cut 同じ型: 前置きの 1 行目を cut の途中で出し、落ちの 2 行目を語で効果音 (チーン / 拍子木 / 太鼓) と同時に落として、着地の後に揺らす
cast sub = "爽やかで少し高めの若い男性の声、20代、明瞭で誠実な話し方" speed=106% manner="上司を褒めるように、にこやかで丁寧な口調。心から感心しているように明るく" label="部下" label_fill=$sub
cast boss = "低めで穏やかなシニア男性の声、60代、温かく語りかける話し方" speed=106% manner="偉そうで得意げな中年の上司。余裕たっぷりに胸を張って" label="上司" label_fill=$boss
silence head=0 tail=0
transition = slide,260,dir=left,offset=38%,opacity=0,overlap=260,ease=power3.out,se=whoosh -10dB

# 帯の決め語が弾む → 組織図が組み上がり、「管理職」「上層部」の語で × を叩きつけ、「資格」の語で社員の資格証が脈打つ → 落ちのあと絵を驚きの部下へ
*** org_chart
[>#subtitle]
bgm music
@sub: [silence:0.4s][♪pop -7dB -280][!#title_bar.title{big} punch,1.35,duration=350 -100][>#org_dim +500][>#org +550][>#org.upper +650][>#org.lower +750][<#nobody cut-100]管理職も[>#org.mgr_l.cross -160][>#org.mgr_r.cross -80][♪stamp -2dB -80]上層部[>#org.exec.cross][♪stamp -2dB +70]も、業界の[!#org.staff[*].cert to,{scale:1.18, duration:.25, yoyo:true, repeat:1, ease:'sine.inOut', stagger:.08} -20]資格を持ってません[>#nobody +480][♪chiin -3dB +480][>#nobody.punch +600][!#nobody.punch shake,6,duration=240 +900]でした。[<#org_dim -360][<#org -360][>#sub_surprised -110][<#desk_wide +240]てっきり、持ってるものかと。[silence:1.15s]

# 上司の自慢 → 褒める部下に替えて前置き → 「効率的」に落ち + 拍子木 → 「ですねえ」で照れる上司を打ち込む
*** promoted
@boss: 資格がなくても、ここまで来たからな。[silence:0.3s]
@sub: [>#sub_praise][<#boss_smug +350][>#rank_first][<#rank_first cut-50]取得より先に、出世を済ませたんですね。[>#rank_first.punch -450][♪hyoshigi -5dB -450][!#rank_first.punch shake,6,duration=240 -150]効率的[>#boss_blush][<#sub_praise +350]ですねえ。[silence:0.75s]

# 質問 → うなずく上司 (横流れ) → メモする部下と前置き → 落ちは「主義」の語で
*** experience
@sub: 資格取得を勧めないんですか？[silence:0.3s]
@boss: [>#boss_nod][<#sub_ask +350]経験が大事だからね。[silence:0.35s]
@sub: [>#sub_memo][<#boss_nod +350][<#self_report cut-50]なるほど。[>#self_report]合格発表のない実力[>#self_report.punch][♪hyoshigi -5dB][!#self_report.punch shake,6,duration=240 +300]主義。[silence:1.3s]

# 制度を尋ねる → はぐらかす上司の打ち込み → 下降音で「おや」の部下 → 文末に前置きと落ちを続けて
*** ask_rules
@sub: では、この制度の仕組みは？[silence:0.3s]
@boss: [>#boss_dodge][<#paper_offer +350]詳しい者に聞いてくれ。[silence:0.85s]
@sub: [>#sub_puzzled -750][<#boss_dodge -400][♪slide -8dB -780][<#not_expert cut-50]詳しい者って、そちらではなかったんです[>#not_expert +400][♪chiin -3dB +400][>#not_expert.punch +520][!#not_expert.punch shake,6,duration=240 +820]ね。[silence:1.75s]

# 胸を張る上司 → 拍手する部下と前置き → 文末の「ね」で落ちと照れる上司の打ち込みを同時に
*** overview
@boss: 俺は全体を見てるんだ。[silence:0.3s]
@sub: [>#sub_clap][<#boss_window +350][<#top_decides cut-50]なるほど。[>#top_decides]専門知識は現場調達。決定権だけは自前なんです[>#boss_blush_close][<#sub_clap +350][>#top_decides.punch][♪hyoshigi -5dB][!#top_decides.punch shake,6,duration=240 +300]ね。[silence:1.35s]

# 締め: 語りかけ → 笑顔の寄りと前置き → BGM を止めて真顔 + 減光 → 「社内のプロ」に落ち + 太鼓で絵とテロップが揺れる
*** deadpan
@sub: 資格だけで実力は決まりません。でも、肩書きだけでも[br]決まりません。[silence:0.35s]
@: [>#sub_smile_close][<#sub_talk +350][>#inhouse_pro +50]業界のプロかと思ったら、[silence:0.75s]
[<#music -650]
@: [>#sub_deadpan -650][<#sub_smile_close -300][>#vignette -650]社内のプロ[>#inhouse_pro.punch +420][♪taiko +7dB +420][!#sub_deadpan shake,11,duration=420 +420][!#inhouse_pro shake,7,duration=360 +490]でした。[silence:1.85s]
```

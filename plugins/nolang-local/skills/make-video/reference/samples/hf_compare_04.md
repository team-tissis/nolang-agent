# compare · 車椅子への移乗介助 (hf の全力版を draft src に全量で写した物 — 介護の基本手順を 3 章で) — canvas 1280x720・約 42s

見せる作り: 常設の章札と進行 3 本・2 枚の色の板が払う章の区切り・話者札つきの字幕 (話者ごとに縁の色)・場面ごとの絵替え (基準画像で人物を揃える)・写真の上の見出しと寄りの丸窓・語と同時に動く主役 (輪とカチッ・走り出す NG 図の車椅子・上から見た図で回る車椅子)・語ごとのチェック・締めの題の再掲・音の層 (BGM + 語ごとの効果音)

```design.txt
#v2
# 学ぶ作り: 常設の章札と進行 3 本 (sticky・章ごとに語で入れ替え)・2 枚の色の板が払う章の区切り (前の cut の末尾で出し次の cut の頭で抜く)・話者ごとに縁の色が変わる字幕
# 場面ごとの絵替え (基準画像 [ref:@hero] で人物を揃える)・写真の上の見出しと寄りの丸窓・語と同時に動く主役 (ブレーキの輪とカチッ・走り出す車椅子・上から見た図で回る車椅子)・語ごとのチェック・締めは題の再掲の 1 枚
# 地 = cream・主色 mint・補色 orange・見出し navy・書体は 1 つ (BIZ UDPゴシック Bold)。座標は hf の 1920 px × 2/3
canvas 1280x720 bg=#FBF7EF
theme light
palette navy=#23446B ink=#1F2A37 mint=#2E9C7A mint_l=#CFEFE3 cream=#FBF7EF orange=#E8762A red=#D7263D gray=#5B6B7C bar=#9FE0C9 kw=#CF5A1F ok=#C2560F track=#DFE5EA mute=#66768A pane=#F8F3EC pane2=#F3ECE2 ngline=#F3C2C8 ngbg=#FDECEE tag=#EEF3F7 sep=#E3E9EE
font "BIZ UDPゴシック Bold"
# 冒頭の題札・章の見出し・まとめの板の題は台詞より先に置く (hf の作り: 見出しを先に見せ、台詞が後から説明する)
lint off=spoiler
# 章の区切りの板の文字は 0.8 秒で通り抜ける (hf の作り: 同じ章名が直後の章札と見出しに残る)
lint off=flash_text
# 締めは cream の地に題を再掲する文字だけの 1 枚 (hf の作り)
lint off=text_only_cut
sfx off
prompt_tail "人物の見た目（すべての画像で統一）: 介護スタッフ＝30代の日本人女性。黒髪を後ろで一つにまとめ、ネイビーの半袖ポロシャツのユニフォーム、胸に白い名札、ベージュのパンツ。介護学生3人＝20歳前後。全員ミントグリーンの半袖スクラブ（実習着）と白いパンツ。学生A＝ミディアムボブの女性、学生B＝短い黒髪の男性、学生C＝ポニーテールの女性。車椅子は日本の介護施設で一般的な自走式（大きな後輪にハンドリム、前に小さなキャスター、左右のアームサポート、フットサポート、後輪のすぐ前にブレーキレバー）。構造を正確に描く。画風: 日本の介護福祉士養成テキストの挿絵のような、清潔感のある高品質なデジタルイラスト。やわらかく細い主線、フラットな塗りにやさしいグラデーションの陰影、明るく温かいパステル調（ミントグリーン・クリーム・ネイビー・木目のベージュが基調）。人物は日本人で自然な等身。表情はやさしく親しみやすい。画像の中に文字・ロゴ・数字・記号・透かしは一切入れない。"
image hero = "介護実習室の全景（横長の構図）。窓から柔らかな自然光が入る明るく清潔な部屋。画面の右半分に、手すり付きの介護用電動ベッドと自走式車椅子があり、介護スタッフが車椅子のグリップに片手を添えて、学生3人に笑顔で説明している。学生3人はバインダーを持ち、真剣に話を聞いている。画面の左側3分の1は、落ち着いた明るい壁と窓だけの余白にする（人物や物を置かない）。" aspect=16:9
image closeup = "自走式車椅子のブレーキ部分の寄りのアップ（手元だけを写し、人物の顔や上半身は写さない）。灰色のタイヤの大きな後輪と、そのすぐ前・座面の下にあるブレーキレバー。ネイビーの半袖ポロシャツから出た右手がレバーを前方へしっかり押し込み、ブレーキの当て金がタイヤに押し当てられてロックされている。背景はやわらかくぼかしたクリーム色の室内と木目の床。"
sound title = "タイトルが出る瞬間の明るいきらめき音"
sound trans = "場面転換のシュワッと流れる効果音"
sound whoosh = "ヒュンという短い風切り音"
sound click = "カチッというロックの音"
sound pop = "紙の筒で鳴らした乾いた軽いポンという音"
sound check = "チェックを付ける軽いポップな確認音"
sound correct = "明るいチャイムの正解音"
sound warn = "短く低いブーという不正解のブザー"
sound kira = "キラリンと輝く高い音"
run k = color=$kw
run r = color=$red
run o = color=$orange
run p = color=$ok
cue turn_chair(a, d, e=power2.inOut) = [!#top_view.chair to,rotation={a},duration={d},ease={e},pivot=97.14%,5.88%][!#top_view.axis to,rotation={a},duration={d},ease={e},pivot=97.14%,5.88%]
cue tick(x) = [>#x.box_fill][>#x.mark +80]
cue bumper_in(b) = [>#b.s][>#b.t][>#b.u]
cue bumper_out(b) = [<#b.s][<#b.t][<#b.u]
p { line-height: 1; out: none }
div { padding: 0px; border: none; box-shadow: none; out: none }
img { out: none }
svg { out: none }
shape { out: none }
icon { out: none }
subtitle.hug(bottom: 27px; font-size: 31px; line-height: 1.46; text-align: center; color: $ink; background: #FFFFFFF5; border-radius: 17px; padding: 21px 43px 17px 43px; border: 3px solid $gray; box-shadow: 0px 8px 21px #192D4638; label: top_left; unit: sentence; lead: 150; tail: 300; hold: off; in: {y:15, opacity:0, duration:0.3, ease:'power3.out'}; out: {y:7, opacity:0, duration:0.2, ease:'power2.in'})
subtitle.staff(border: 3px solid $navy)
subtitle.student(border: 3px solid $mint)
bgm#music(duck: -6; volume: 6dB; fade: 800,2400; keys: "0:+5|15s:+5|30s:0") 明るく温かく穏やかなアコースティックのピアノとギター、弦と鉄琴、日常と希望の雰囲気の遅めの曲

# 章の区切り: 淡い mint と mint の 2 枚の板が左から払い、mint の板の上に章の文字が出て右へ抜ける (sticky — 前の cut の末尾で出し次の cut の頭で抜く・文字の板が上)
def bumper_back(c) = div(inset: 0; background: {c}; z-index: front; in: {x:-1280, duration:0.42, ease:'power3.inOut'}; out: {x:1280, duration:0.4, ease:'power3.inOut'})
def bumper(s, t, u) = div(inset: 0; background: $mint; z-index: front; in: {x:-1280, duration:0.42, ease:'power3.inOut'}; out: {x:1280, duration:0.4, ease:'power3.inOut'})
  p#s(cx: 50%; top: 253px; font-size: 36px; letter-spacing: 0.3em; color: #FFFFFF; opacity: 0.9; content: {s}; in: {x:-47, opacity:0, duration:0.32, ease:'power3.out'}; out: {x:47, opacity:0, duration:0.22, ease:'power2.in'})
  p#t(cx: 50%; top: 289px; font-size: 100px; line-height: 1.2; letter-spacing: 0.06em; color: #FFFFFF; content: {t}; in: {x:-47, opacity:0, duration:0.32, ease:'power3.out'}; out: {x:47, opacity:0, duration:0.22, ease:'power2.in'})
  p#u(cx: 50%; top: 421px; font-size: 27px; color: #FFFFFF; border: 2px solid #FFFFFFD9; border-radius: 99px; padding: 7px 23px 8px 23px; content: {u}; in: {x:-47, opacity:0, duration:0.32, ease:'power3.out'}; out: {x:47, opacity:0, duration:0.22, ease:'power2.in'})
# 左上の章札 (番号の色の丸札 + 右に白い題の札)
def chapter_chip(n, t, w, wn, c=$mint) = div(left: 37px; top: 29px; width: {w}; height: 38px; border-radius: 99px; background: {c}; box-shadow: 0px 5px 15px #192D4633; z-index: front; in: {x:-20, opacity:0, duration:0.4, ease:'power3.out'}; out: {x:-20, opacity:0, duration:0.25})
  p#n(left: 0px; cy: 50%; width: {wn}; font-size: 19px; letter-spacing: 0.08em; text-align: center; color: #FFFFFF; content: {n})
  p#t(left: {wn}; right: 0px; top: 0px; font-size: 21px; color: $navy; background: #FFFFFF; border-radius: 0,99,99,0; padding: 8px 0px 9px 15px; content: {t})
# 写真の上の見出し (小さな前置き + 題)
def heading(s, t, w) = div(left: 37px; top: 91px; width: {w}; height: 81px; border-radius: 13px; background: #FFFFFFF2; box-shadow: 0px 5px 16px #192D4629; in: {x:-33, opacity:0, duration:0.5, ease:'power3.out'})
  p#s(left: 21px; top: 11px; font-size: 20px; color: $gray; content: {s})
  p#t(left: 21px; top: 34px; font-size: 36px; color: $navy; content: {t})
# NG 図・上から見た図の部品 (svg の viewBox ごとの枠)
def ng_part(pt) = svg(left: 23px; top: 59px; width: 533px; height: 287px; part: {pt})
def top_part(pt) = svg(left: 11px; top: 43px; width: 587px; height: 400px; part: {pt})

# NG 図 (1 枚の svg を部品ごとに・viewBox は共通・車椅子の部品は自分の枠で回す)
svg ng_floor = """<svg viewBox="0 0 800 430"><line x1="20" y1="382" x2="780" y2="382" stroke="#c9d3dc" stroke-width="5" stroke-linecap="round"/></svg>"""
svg ng_person = """<svg viewBox="160 70 130 330"><g stroke="#5b6b7c" stroke-linecap="round"><line x1="214" y1="276" x2="196" y2="378" stroke-width="24"/><line x1="226" y1="276" x2="246" y2="378" stroke-width="24"/><line x1="208" y1="158" x2="222" y2="272" stroke-width="46"/><line x1="214" y1="178" x2="262" y2="236" stroke-width="17"/></g><circle cx="200" cy="112" r="30" fill="#5b6b7c"/></svg>"""
svg ng_streaks = """<svg viewBox="0 0 800 430"><g stroke="#9aa5b1" stroke-width="7" stroke-linecap="round"><line x1="214" y1="236" x2="274" y2="236"/><line x1="196" y1="290" x2="276" y2="290"/><line x1="222" y1="344" x2="270" y2="344"/></g></svg>"""
svg ng_frame = """<svg viewBox="0 0 800 430"><line x1="318" y1="300" x2="470" y2="300" stroke="#9aa5b1" stroke-width="7"/><line x1="318" y1="242" x2="306" y2="336" stroke="#9aa5b1" stroke-width="8" stroke-linecap="round"/><line x1="306" y1="336" x2="262" y2="344" stroke="#4a5663" stroke-width="10" stroke-linecap="round"/><line x1="350" y1="180" x2="350" y2="236" stroke="#9aa5b1" stroke-width="7"/><line x1="455" y1="180" x2="455" y2="236" stroke="#9aa5b1" stroke-width="7"/><line x1="488" y1="234" x2="504" y2="118" stroke="#23446b" stroke-width="16" stroke-linecap="round"/><line x1="504" y1="118" x2="536" y2="114" stroke="#3a4654" stroke-width="11" stroke-linecap="round"/></svg>"""
svg ng_rear_wheel = """<svg viewBox="390 227 160 160"><circle cx="470" cy="307" r="72" fill="none" stroke="#3a4654" stroke-width="13"/><circle cx="470" cy="307" r="57" fill="none" stroke="#9aa5b1" stroke-width="4"/><g stroke="#b8c2cc" stroke-width="4"><line x1="470" y1="241" x2="470" y2="373"/><line x1="413" y1="274" x2="527" y2="340"/><line x1="413" y1="340" x2="527" y2="274"/></g><circle cx="470" cy="307" r="11" fill="#3a4654"/></svg>"""
svg ng_seat = """<svg viewBox="0 0 800 430"><rect x="306" y="222" width="186" height="24" rx="8" fill="#2f5d8c"/><line x1="338" y1="178" x2="468" y2="178" stroke="#4a5663" stroke-width="11" stroke-linecap="round"/></svg>"""
svg ng_caster = """<svg viewBox="276 333 52 52"><circle cx="302" cy="359" r="21" fill="#fff" stroke="#3a4654" stroke-width="8"/><line x1="302" y1="342" x2="302" y2="376" stroke="#3a4654" stroke-width="4"/><circle cx="302" cy="359" r="5" fill="#3a4654"/></svg>"""
svg ng_brake_off = """<svg viewBox="0 0 800 430"><line x1="402" y1="250" x2="420" y2="212" stroke="#d7263d" stroke-width="9" stroke-linecap="round"/><line x1="412" y1="206" x2="392" y2="124" stroke="#d7263d" stroke-width="3" stroke-dasharray="6 6"/><rect x="318" y="76" width="168" height="48" rx="12" fill="#d7263d"/><text x="402" y="110" text-anchor="middle" font-size="27" fill="#fff" font-family="BIZ UDPGothic" font-weight="700">ブレーキOFF</text></svg>"""
svg ng_burst = """<svg viewBox="0 0 800 430"><circle cx="318" cy="150" r="40" fill="#d7263d"/><text x="318" y="166" text-anchor="middle" font-size="50" fill="#fff" font-family="BIZ UDPGothic" font-weight="700">!</text></svg>"""
# 上から見た図 (1 枚の svg を部品ごとに・車椅子と軸だけ回す点 (550,300) を含む枠に切る・扇の濃くなる往復は重ねた扇の出入り)
svg top_bed = """<svg viewBox="0 0 880 600"><rect x="40" y="40" width="800" height="260" rx="20" fill="#ead9bd"/><rect x="58" y="56" width="764" height="228" rx="14" fill="#dcebf7"/><rect x="74" y="86" width="100" height="168" rx="24" fill="#fff" stroke="#c9d6e2" stroke-width="3"/><text x="640" y="186" text-anchor="middle" font-size="34" fill="#4f6075" font-family="BIZ UDPGothic" font-weight="700">ベッド</text></svg>"""
svg top_person = """<svg viewBox="0 0 880 600"><g fill="#fff" stroke="#b3c0cc" stroke-width="3"><rect x="164" y="286" width="24" height="104" rx="11"/><rect x="194" y="286" width="24" height="104" rx="11"/><ellipse cx="176" cy="404" rx="13" ry="17"/><ellipse cx="206" cy="404" rx="13" ry="17"/></g><ellipse cx="191" cy="282" rx="62" ry="30" fill="#8edcc0"/><circle cx="191" cy="276" r="27" fill="#2b2b2b"/><text x="191" y="222" text-anchor="middle" font-size="26" fill="#5b6b7c" font-family="BIZ UDPGothic" font-weight="700">利用者</text></svg>"""
svg top_edge = """<svg viewBox="0 0 880 600"><line x1="250" y1="300" x2="552" y2="300" stroke="#e8762a" stroke-width="6" stroke-linecap="round"/></svg>"""
svg top_sector = """<svg viewBox="0 0 880 600"><path d="M 550 300 L 250.6 380.2 A 310 310 0 0 0 281.5 455 Z" fill="#f6a35b" fill-opacity="0.22"/></svg>"""
svg top_sector2 = """<svg viewBox="0 0 880 600"><path d="M 550 300 L 250.6 380.2 A 310 310 0 0 0 281.5 455 Z" fill="#f6a35b" fill-opacity="0.23"/></svg>"""
svg top_range = """<svg viewBox="0 0 880 600"><g stroke="#e8762a" stroke-width="3"><line x1="550" y1="300" x2="250.6" y2="380.2"/><line x1="550" y1="300" x2="281.5" y2="455"/></g></svg>"""
svg top_axis = """<svg viewBox="210 290 350 170"><line x1="550" y1="300" x2="214" y2="300" stroke="#e8762a" stroke-width="4" stroke-dasharray="14 10"/></svg>"""
svg top_chair = """<svg viewBox="210 290 350 170"><g fill="#3a4654"><rect x="400" y="300" width="140" height="17" rx="8"/><rect x="400" y="433" width="140" height="17" rx="8"/><rect x="360" y="306" width="22" height="15" rx="6"/><rect x="360" y="429" width="22" height="15" rx="6"/></g><rect x="345" y="330" width="66" height="7" fill="#9aa5b1"/><rect x="345" y="413" width="66" height="7" fill="#9aa5b1"/><rect x="322" y="334" width="32" height="36" rx="6" fill="#4a5663"/><rect x="322" y="380" width="32" height="36" rx="6" fill="#4a5663"/><rect x="410" y="322" width="118" height="106" rx="12" fill="#2f5d8c"/><rect x="526" y="316" width="16" height="118" rx="6" fill="#23446b"/><g fill="#56636f"><rect x="430" y="313" width="72" height="13" rx="6"/><rect x="430" y="424" width="72" height="13" rx="6"/><rect x="540" y="318" width="14" height="10" rx="4"/><rect x="540" y="422" width="14" height="10" rx="4"/></g></svg>"""
svg top_chair_label = """<svg viewBox="0 0 880 600"><text x="590" y="548" text-anchor="middle" font-size="30" fill="#5b6b7c" font-family="BIZ UDPGothic" font-weight="700">車椅子</text></svg>"""
svg top_callout = """<svg viewBox="0 0 880 600"><line x1="282" y1="411" x2="236" y2="470" stroke="#e8762a" stroke-width="3"/><rect x="28" y="468" width="300" height="112" rx="18" fill="#fff4ea" stroke="#e8762a" stroke-width="4"/><text x="178" y="532" text-anchor="middle" font-size="58" fill="#c2560f" font-family="BIZ UDPGothic" font-weight="700">15°〜30°</text><text x="178" y="566" text-anchor="middle" font-size="22" fill="#7a5a3f" font-family="BIZ UDPGothic" font-weight="700">ベッドの側面に対する角度</text></svg>"""

# title — 開幕: 写真が寄りながら現れ、左の余白に題札 (前置き・字ごとに上がる 2 行・下線の帯)・「基本手順」で 3 つの目次の札
section#title(stagger: {each:0})
img#title_photo(inset: 0; content: @hero; main: keys(at=0 scale=1.12 opacity=0 | at=0.31 scale=1 opacity=1 ease=power2.out | at=0.999 scale=1.035 ease=none),duration=8450,pivot=70%,55%)
div#title_veil(inset: 0; background: linear(#FBF7EFF7,#FBF7EFEB@36%,#FBF7EF00@56%,90); delay: 150; in: {opacity:0, duration:0.8, ease:'power2.out'})
group#title_card(out: {x:-40, opacity:0, duration:0.35, ease:'power2.in'})
p#title_card.kicker(left: 75px; top: 140px; font-size: 21px; letter-spacing: 0.08em; color: #FFFFFF; background: $mint; border-radius: 99px; padding: 7px 17px 7px 17px; delay: 450; in: {x:-27, opacity:0, duration:0.5, ease:'power3.out'}) 介護の基本技術
p#title_card.line1(left: 75px; top: 198px; font-size: 55px; line-height: 1.15; letter-spacing: 0.02em; color: $navy; delay: 650; in: {y:31, opacity:0, duration:0.5, ease:'power3.out', stagger:.05}) 車椅子への
shape#title_card.bar(left: 71px; top: 324px; width: 522px; height: 20px; path: rect,r=0.25; background: $bar; delay: 1450; in: {scaleX:0, duration:0.6, ease:'power2.inOut', pivot:'left'})
p#title_card.line2(left: 75px; top: 265px; font-size: 72px; line-height: 1.15; letter-spacing: 0.02em; color: $navy; delay: 900; in: {y:40, opacity:0, duration:0.55, ease:'power3.out', stagger:.05}) 安全な移乗介助
p#title_card.sub(left: 75px; top: 365px; font-size: 33px; letter-spacing: 0.12em; color: $mint; delay: 1650; in: {y:13, opacity:0, duration:0.5, ease:'power3.out'}) ― 基本手順 ―
div#title_card.agenda(left: "75;197;363"; top: 434px; width: "111;153;130"; height: 47px; border-radius: 99px; background: #FFFFFF; box-shadow: 0px 4px 12px #23446B24; in: {scale:0.7, opacity:0, duration:0.45, ease:'back.out(2.2)', stagger: {each: 0.14}}) ×3
  p#n(left: 7px; cy: 50%; width: 33px; font-size: 19px; text-align: center; color: #FFFFFF; background: "$mint;$mint;$orange"; border-radius: 99px; padding: 7px 0px) 1;2;✓
  p#t(left: 49px; cy: 50%; font-size: 21px; color: $navy) 準備;位置調整;まとめ
# 左上の章札と右上の進行 (sticky・後の cut の語で出す・区切りの板より先に書く = 板の下)
chapter_chip#chapter1.sticky(n: "STEP 1"; t: "準備"; w: 188; wn: 110)
chapter_chip#chapter2.sticky(n: "STEP 2"; t: "位置調整"; w: 233; wn: 113)
chapter_chip#chapter3.sticky(n: "POINT"; t: "まとめ"; w: 201; wn: 104; c: $orange; out: {opacity:0, duration:0.4})
div#progress.sticky(left: 939px; top: 33px; width: 304px; height: 44px; border-radius: 13px; background: #FFFFFFEB; box-shadow: 0px 4px 12px #192D4624; z-index: front; in: none; out: {opacity:0, duration:0.4})
  div#track(left: "15;109;204"; top: 9px; width: 85px; height: 7px; border-radius: 4px; background: $track) ×3
    div#bar(left: 0px; top: 0px; width: 85px; height: 7px; border-radius: 4px; background: $mint; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'})
  p#step(left: "15;109;204"; top: 21px; width: 85px; font-size: 18px; text-align: center; color: $mute) ×3 準備;位置調整;まとめ
bumper_back#bumper1_back.sticky(c: $mint_l)
bumper#bumper1.sticky(s: "STEP 1"; t: "準備"; u: "ブレーキの確認")

# brake — STEP 1: 屈んでブレーキを押す絵に寄り続け、「ブレーキ」で輪とカチッ・「しっかり」で寄りの丸窓と説明・「確認」の前にチェック
section#brake(stagger: {each:0})
group#brake_zoom(main: keys(at=0 scale=1 | at=1 scale=1.2 ease=sine.inOut),window=100,7500,forwards; transform-origin: 48.7% 96.3%)
  img#photo(inset: 0; main: none) [ref:@hero]介護実習室。介護ベッドの横に置かれた自走式車椅子の横に介護スタッフがしゃがみ、後輪のすぐ前のブレーキレバーを右手でしっかり押してロックしている。スタッフは手元のブレーキを確認しながら、顔を少し上げて学生たちに語りかけている。背景で学生3人が身を乗り出して手元をのぞき込んでいる。
  shape#ring.ellipse(left: 570px; top: 470px; width: 107px; height: 107px; background: none; border: 6px solid $orange; in: draw,450)
heading#brake_head(s: "いちばん大切なこと"; t: "ブレーキの確認"; w: 288)
p#click_word(left: 671px; top: 371px; font-size: 51px; letter-spacing: 0.04em; color: $orange; stroke: #FFFFFF,7; transform: rotate(-8deg); in: {scale:0.5, opacity:0, duration:0.35, ease:'back.out(3)'}; out: {y:-11, opacity:0, duration:0.3, ease:'power2.in'}) カチッ
img#brake_inset(left: 907px; top: 131px; width: 267px; height: 267px; border-radius: 999px; border: 7px solid #FFFFFF; box-shadow: 0px 9px 24px #192D464D; content: @closeup; main: kb,1.18>1.0,ease=power2.out; in: {scale:0.4, opacity:0, duration:0.55, ease:'back.out(2.2)'})
p#brake_cap(left: 867px; top: 411px; width: 347px; font-size: 25px; line-height: 1.35; text-align: center; color: $navy; background: #FFFFFFF5; border-radius: 12px; padding: 11px 13px 12px 13px; box-shadow: 0px 5px 15px #192D462E; in: {y:13, opacity:0, duration:0.45, ease:'power3.out'}) {o}ブレーキレバー{/}を押して[br]確実にロック
p#brake_check(left: 879px; top: 507px; font-size: 21px; color: #FFFFFF; background: $mint; border-radius: 99px; padding: 11px 17px 12px 45px; box-shadow: 0px 5px 13px #2E9C7A59; in: {scale:0.7, opacity:0, duration:0.45, ease:'back.out(2.2)'}) 左右両方のブレーキを確認
  p#ok(left: 8px; cy: 50%; width: 29px; font-size: 19px; text-align: center; color: $mint; background: #FFFFFF; border-radius: 99px; padding: 5px 0px) ✓

# ng — 学生の気づき: 学生の顔に寄る → 写真を左へずらし右から NG 図 → 「動いちゃって」で車椅子が走り「危険」で警告 → 「その通り」で写真を戻して丸
section#ng(stagger: {each:0})
img#ng_photo(inset: 0; main: none) [ref:@hero]介護実習室。学生A（ミディアムボブの女性）の上半身のアップ。ハッと気づいた表情で少し眉を寄せ、右手の人差し指を立てて話している。そばに車椅子のグリップの一部が見える。背景には学生Bと学生Cがうなずいている姿をやわらかくぼかして描く。
div#ng_panel(left: 640px; top: 0px; width: 640px; height: 720px; background: linear($pane,$pane2,180); box-shadow: -12px 0px 27px #192D462E; in: {x:653, duration:0.6, ease:'power3.out'}; out: {x:653, duration:0.5, ease:'power3.in'})
div#ng_card(left: 667px; top: 93px; width: 573px; height: 447px; border-radius: 19px; background: #FFFFFF; border: 3px solid $ngline; box-shadow: 0px 11px 27px #192D4640; in: {x:653, duration:0.6, ease:'power3.out'}; out: {x:653, duration:0.5, ease:'power3.in'})
  p#pill(left: 23px; top: 20px; font-size: 23px; letter-spacing: 0.06em; color: #FFFFFF; background: $red; border-radius: 8px; padding: 4px 12px 5px 12px) NG
  p#head(left: 99px; top: 23px; font-size: 25px; color: $ink) ブレーキをかけずに立ち上がると…
  ng_part#floor(pt: ng_floor)
  svg#person(left: 210px; top: 149px; width: 87px; height: 220px; part: ng_person; overlap: ng_chair.caster)
  ng_part#burst(pt: ng_burst; in: {scale:0.3, opacity:0, duration:0.4, ease:'back.out(2.2)'})
  div#danger(left: 23px; top: 371px; width: 528px; height: 56px; border-radius: 12px; background: $ngbg; in: {scale:0.8, opacity:0, duration:0.45, ease:'back.out(2.2)'})
    p#bang(left: 101px; cy: 50%; width: 39px; font-size: 27px; text-align: center; color: #FFFFFF; background: $red; border-radius: 99px; padding: 6px 0px) !
    p#t(left: 150px; cy: 50%; font-size: 31px; color: $red) 車椅子が動いて危険
# 車椅子は群 (板と同じ入退場・語で右へ走る・後輪と前輪は自分の中心で回る)
group#ng_chair(in: {x:653, duration:0.6, ease:'power3.out'}; out: {x:653, duration:0.5, ease:'power3.in'})
  svg#streaks(left: 690px; top: 152px; width: 533px; height: 287px; part: ng_streaks; in: fade,150; out: fade,400)
  svg#body(left: 690px; top: 152px; width: 533px; height: 287px; part: ng_frame)
  svg#rear_wheel(left: 950px; top: 303px; width: 107px; height: 107px; part: ng_rear_wheel)
  svg#seat(left: 690px; top: 152px; width: 533px; height: 287px; part: ng_seat)
  svg#caster(left: 874px; top: 374px; width: 35px; height: 35px; part: ng_caster)
  svg#brake_off(left: 690px; top: 152px; width: 533px; height: 287px; part: ng_brake_off)
shape#ok_circle.ellipse(left: 472px; top: 92px; width: 177px; height: 177px; background: none; border: 20px solid #E8762AEB; in: draw,450)
bumper_back#bumper2_back.sticky(c: $mint_l)
bumper#bumper2.sticky(s: "STEP 2"; t: "位置調整"; u: "ベッドと車椅子の角度")

# angle — STEP 2: 格子の地に写真と上から見た図を並べ、「角度」で軸・「15度」「30度」で車椅子を回し、角度の札と扇の明滅
section#angle(stagger: {each:0})
div#angle_bg(inset: 0; background: $cream; pattern: grid,40,#23446B0F)
heading#angle_head(s: "ステップ2"; t: "ベッドと車椅子の角度"; w: 389; delay: 350)
img#angle_photo(left: 37px; top: 175px; width: 568px; height: 323px; border-radius: 17px; border: 5px solid #FFFFFF; box-shadow: 0px 9px 23px #192D4638; main: kb,1.0@40%,60%>1.08@40%,60%; delay: 300; in: {y:27, opacity:0, duration:0.55, ease:'power3.out'}) [ref:@hero]介護実習室を斜め上から見下ろした構図。介護ベッドの長い辺の中央に、利用者役の学生B（短い黒髪の男性）が端座位で座っている（足は床につけ、ベッドの外側を向いている）。介護スタッフが、学生Bのすぐ横に車椅子を置き、ベッドの側面に対して浅い斜め（約20〜30度）の角度に向きを整えている。車椅子の座面は学生Bの方を向いている。学生Aと学生Cが横で見学している。
p#angle_cap(left: 37px; top: 508px; width: 568px; font-size: 24px; text-align: center; color: $navy; delay: 750; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'}) ベッドのすぐ横に、斜めに置く
div#top_view(left: 633px; top: 91px; width: 609px; height: 451px; border-radius: 19px; background: #FFFFFF; box-shadow: 0px 9px 23px #192D462E; delay: 400; in: {y:27, opacity:0, duration:0.55, ease:'power3.out'})
  p#badge(left: 20px; top: 15px; font-size: 18px; color: $gray; background: $tag; border-radius: 7px; padding: 4px 12px 5px 12px) 上から見た図
  top_part#bed(pt: top_bed; delay: 100; in: fade,450)
  top_part#person(pt: top_person; delay: 220; in: fade,450)
  top_part#edge(pt: top_edge; in: fade,350)
  top_part#sector(pt: top_sector; in: fade,350)
  top_part#sector2(pt: top_sector2; in: {opacity:0, duration:0.5, ease:'sine.inOut'}; out: {opacity:0, duration:0.5, ease:'sine.inOut'})
  top_part#range(pt: top_range; in: fade,350)
  shape#arc(path: "M 191 293 Q 198 318 210 340"; background: none; border: 6px solid $orange; in: draw,600)
  svg#axis(left: 151px; top: 236px; width: 233px; height: 113px; part: top_axis; in: fade,350)
  svg#chair(left: 151px; top: 236px; width: 233px; height: 113px; part: top_chair; delay: 300; in: {x:173, opacity:0, duration:0.65, ease:'power3.out'})
  top_part#chair_label(pt: top_chair_label; delay: 750; in: fade,400)
  top_part#callout(pt: top_callout; in: pop,0.6,500,ease=back(2),pivot=13.4%,68.5%)
bumper_back#bumper3_back.sticky(c: $mint_l)
bumper#bumper3.sticky(s: "POINT"; t: "まとめ"; u: "移乗介助のポイント")

# summary — まとめ: 写真の右に 4 項目の板・語ごとにチェックが付き、最後に板の縁が光る
section#summary(stagger: {each:0})
img#sum_photo(inset: 0; main: kb,1.12@87%,46%>1.16@81%,42%) [ref:@hero]介護実習室。介護ベッドの端に座る高齢の女性利用者（白髪のショートヘア、薄いピンクのカーディガン）の前で、介護スタッフがしゃがんで目線を合わせ、両手で利用者の手をやさしく取りながら笑顔で声をかけている。ベッドのすぐ横には車椅子が斜めに置かれている。少し離れて学生3人が温かく見守っている。午後のやわらかな光。
div#sum_veil(inset: 0; background: linear(#FBF7EF00,#FBF7EF00@56%,#FBF7EF66@70%,#FBF7EFBF,90))
div#points(left: 797px; top: 100px; width: 445px; height: 403px; border-radius: 19px; background: #FFFFFFF7; box-shadow: 0px 11px 27px #192D463D; delay: 200; in: {x:53, opacity:0, duration:0.55, ease:'power3.out'})
  p#head(left: 27px; top: 23px; font-size: 31px; color: $navy) 移乗介助のポイント
  shape#rule(left: 27px; top: 65px; width: 392px; height: 3px; path: rect; background: $bar)
  div#item(left: 27px; top: "82;161;239;318"; width: 392px; height: 79px; in: {y:16, opacity:0, duration:0.4, ease:'power3.out'}) ×4
    div#box(left: 0px; cy: 50%; width: 40px; height: 40px; border-radius: 9px; background: #FFFFFF; border: 3px solid $mint)
    div#box_fill(left: 0px; cy: 50%; width: 40px; height: 40px; border-radius: 9px; background: $mint; in: {scale:0, duration:0.25, ease:'back.out(2)'})
    icon#mark(left: 7px; cy: 50%; font-size: 26px; name: check; weight: bold; color: #FFFFFF; in: draw,300)
    p#t(left: 55px; cy: 50%; font-size: 25px; line-height: 1.3; color: $ink) 車椅子の{p}ブレーキ{/}を確認;ベッドとの角度は{p}15°〜30°{/};{p}声かけ{/}を忘れずに;{p}利用者のペース{/}に合わせる
    shape#sep(left: 0px; bottom: 0px; width: 392px; height: 2px; path: line_h; border: 1px solid $sep; dash: 5,5; opacity: "1;1;1;0")

# end — 締め: 開幕の題札を cream の地の中央に組み直す
section#end(stagger: {each:0})
p#end_kicker(cx: 640px; top: 235px; font-size: 21px; letter-spacing: 0.08em; color: #FFFFFF; background: $mint; border-radius: 99px; padding: 7px 17px 7px 17px; delay: 400; in: {y:13, opacity:0, duration:0.45, ease:'power3.out'}) 介護の基本技術
p#end_line1(cx: 640px; top: 290px; font-size: 51px; line-height: 1.15; letter-spacing: 0.02em; color: $navy; delay: 520; in: {y:17, opacity:0, duration:0.5, ease:'power3.out'}) 車椅子への
shape#end_bar(left: 389px; top: 408px; width: 503px; height: 20px; path: rect,r=0.25; background: $bar; delay: 1000; in: {scaleX:0, duration:0.6, ease:'power2.inOut', pivot:'left'})
p#end_line2(cx: 640px; top: 352px; font-size: 69px; line-height: 1.15; letter-spacing: 0.02em; color: $navy; delay: 660; in: {y:20, opacity:0, duration:0.55, ease:'power3.out'}) 安全な移乗介助
p#end_sub(cx: 640px; top: 452px; font-size: 33px; letter-spacing: 0.12em; color: $mint; delay: 1100; in: {y:13, opacity:0, duration:0.5, ease:'power3.out'}) ― 基本手順 ―
```

```timeline.txt
#v2
cast narr = "低く響く安定感のある20代の男性のナレーター、落ち着いた明瞭な声で淡々と丁寧に伝える" label="ナレーション" label_fill=$gray
cast staff = "柔らかく息まじりの低めの声の30代の女性の介護スタッフ、優しく親しみやすい話し方" label="介護スタッフ" label_fill=$navy subtitle=.staff
cast student = "高めで明るく快活な20歳前後の女性の介護学生、ハキハキと元気な話し方" label="介護学生" label_fill=$mint subtitle=.student
silence head=0 tail=0

*** title
[>#subtitle]
bgm music
se title +300
@narr: [silence:1.5s]今回は、車椅子への安全な移乗介助の[br][>#title_card.agenda[*]][♪pop -3dB +50]基本手順について学んでいきましょう。[silence:0.32s][<#title_card][silence:0.22s][>#bumper1_back][♪trans][>#bumper1 +70][bumper_in #bumper1 +300][silence:0.53s]

*** brake
@staff: [silence:0.9s][bumper_out #bumper1 -570][<#bumper1 -510][<#bumper1_back -450][>#progress -600][>#chapter1 -400][>#progress.track[1].bar -300][!#progress.step[1] recolor,$mint,duration=50 -300][>#brake_head -100]まず一番大切なのは、[br]車椅子の[>#brake_zoom.ring][!#brake_zoom.ring ping,#FFB36B,2,interval=730,duration=700,scale=0.9>1.6 +50][>#click_word +40][<#click_word +1300][♪click +40]{k}ブレーキ{/}が[>#brake_inset -50][♪whoosh -5dB -50][>#brake_cap +300]しっかりかかっているかの[>#brake_check -350][♪check -1dB -300]確認です。[silence:0.35s]
transition dissolve,330,overlap=330

*** ng
@student: [silence:0.43s][!#ng_photo to,{x:-49, y:-19, scale:1.07, duration:2.5, ease:'sine.out', pivot:'0%,0%'} -380][♪whoosh -7dB -430]{k}ブレーキ{/}がかかっていないと、[br][!#ng_photo to,{x:-400, duration:0.65, ease:'power3.inOut'} -150][>#ng_panel -150][>#ng_card -100][>#ng_chair -100][♪whoosh -4dB -100][!#ng_card.person to,{x:-80, y:-43, duration:0.55, ease:'power2.out'} +350]立ち上がった時に[!#ng_chair to,{x:137, duration:1, ease:'power2.out'}][!#ng_chair.rear_wheel to,{rotation:163, duration:1, ease:'power2.out'}][!#ng_chair.caster to,{rotation:560, duration:1, ease:'power2.out'}][>#ng_chair.streaks -50][<#ng_chair.streaks +750]車椅子が動いちゃって[>#ng_card.burst -50][>#ng_card.danger][♪warn -1dB +20]{r}危険{/}なんだね。
subtitle "その通りです。[br]次に、ベッドと車椅子の{k}角度{/}を{k}15度から30度{/}に配置します。"
@staff: [silence:0.62s][<#chapter1 cut-0][<#ng_card -450][<#ng_chair -450][<#ng_panel -400][!#ng_photo to,{x:0, y:0, scale:1.18, duration:0.8, ease:'power3.inOut', pivot:'0%,0%'} -400][>#ok_circle +100][♪correct -1dB +80]その通りです。[silence:0.13s][>#bumper2_back][♪trans][>#bumper2 +70][bumper_in #bumper2 +300][silence:0.53s]

*** angle
subtitle "その通りです。[br]次に、ベッドと車椅子の{k}角度{/}を{k}15度から30度{/}に配置します。"
@staff: [silence:0.15s][<#chapter2 cut-0][bumper_out #bumper2 +180][<#bumper2 +240][<#bumper2_back +300][>#chapter2 +200][>#progress.track[2].bar +200][!#progress.step[2] recolor,$mint,duration=50 +200][♪whoosh -6dB +450]次に、ベッドと車椅子の[>#top_view.edge][>#top_view.axis]角度を[turn_chair -15 550][>#top_view.range +200][>#top_view.sector +200]15度から[turn_chair -30 600 power2.inOut -50][>#top_view.arc -50][turn_chair -22 550 power2.out +750][>#top_view.callout +550][♪pop -1dB +550][>#top_view.sector2 +1200][<#top_view.sector2 +1700]30度に配置します。[silence:0.47s][>#bumper3_back][♪trans][>#bumper3 +70][bumper_in #bumper3 +300][silence:0.53s]

*** summary
@narr: [silence:1.0s][<#chapter3 cut-0][<#progress cut-0][bumper_out #bumper3 -670][<#bumper3 -610][<#bumper3_back -550][>#chapter3 -650][>#progress.track[3].bar -650][!#progress.step[3] recolor,$orange,duration=50 -650][>#points.item[1] -700][tick #points.item[1] -600][♪check -4dB -630][>#points.item[2] -550][tick #points.item[2] -450][>#points.item[3] -100][tick #points.item[3] +250][♪check -2dB +250]{k}声かけ{/}を忘れず、[br][>#points.item[4] -100][tick #points.item[4] +250][♪check -2dB +250]{k}利用者のペース{/}に合わせて[!#points glow,#9FE0C9E6,blur=0,spread=7]安全に移乗を行いましょう。[silence:0.4s][♪kira -2dB][silence:0.85s]
transition dissolve,300,overlap=300,ease=power2.inOut

*** end
@narr: [silence:3.4s]
```

# concept · b2b-support — 企業向けオンライン接客「Live Assist」の紹介 (横・16 cut・写真 + タブレットの画面・hf 全力版の全量の写し) — canvas 1280x720

見せる作り: 写真が主役の場面ごとの絵替え (同じ 2 人を基準画像で揃える)・字幕の代わりの左下のテロップ札と左上の STEP 章札・def の部品で組むタブレットの画面 (カーソル・強調枠・吹き出し・page 送り)・cue で段を送る進行の板 → 完了の板・薄く並べて語った列から点灯する 3 列・1 字ずつ上がるロゴの題と締め・音の層

```design.txt
#v2
# この見本から学ぶ作り: 写真が主役の場面ごとの絵替え (同じ 2 人を [ref:@名] で揃える)・字幕の代わりに左下のテロップ札と左上の STEP 章札 (def)・
# タブレットの画面を def の部品 (form と確認の page・通話の側板・吹き出し・強調枠・カーソル) で組み、語に合わせてカーソルと枠を動かす・
# 4 段の進行の板 (cue で ✓ を送り縦線が伸びる → 完了の板)・3 列を薄く並べて語った列から点灯・1 字ずつ上がるロゴの題と締め・音の層 (効果音 + BGM の duck / jump)。座標は hf の 1920 px × 2/3・白地 + 青 1 色
canvas 1280x720 bg=#FFFFFF
theme light
palette a=#1F6FE0 b2=#5AA2F5 ink=#0E2A47 ink2=#23384F sky=#EAF2FD line=#D9E4F1 rule=#E3EAF3 gray=#5B6B7E mute=#8796A8 paper=#F5F8FC ok=#3EC27A red=#E5484D bg=#FFFFFF
font "ZEN角ゴシックNew Medium"
fonts b="ZEN角ゴシックNew Bold" r="ZEN角ゴシックNew Regular" e="Manrope Bold"
run a { color: $a }
run bb { color: $a; font-family: b }
run nv { color: $ink }
run gn { color: #3ED37F }
run k { font-family: e; font-size: 13px; color: $a }
run k2 { font-family: e; font-size: 10px; color: $a }
run l { color: $line }
run ph { color: #8492A2 }
prompt_tail "Photorealistic still from a high-end Japanese corporate commercial film, full-frame cinema camera, natural soft daylight, clean white interior with subtle calm blue accents, refined trustworthy warm mood, realistic skin, gentle shallow depth of field, bright airy neutral whites and soft blues. Absolutely no text, letters, numbers, logos or watermark; any screen shows only soft abstract UI shapes or a video call without readable text."
image cust = "[photo]Medium close-up portrait of a Japanese woman in her early 30s on a light linen sofa in a bright modern apartment living room, holding a white tablet on her lap, soft natural smile, shoulder-length wavy dark brown hair, cream-white knit sweater, small pearl stud earrings" aspect=16:9
image staff = "[photo]Medium close-up portrait of a Japanese female customer-support staff member in her late 20s at a clean white desk in a bright modern support office, slim single-ear headset with boom microphone, warm professional gentle smile, black hair neatly tied in a low bun, navy blazer over white blouse" aspect=16:9
image conf = "[ref:@cust]Close-up of the same woman looking down at the white tablet in her hands with a slightly puzzled, hesitant expression, eyebrows gently drawn together, one index finger hovering above the screen, unsure what to tap, soft daylight" aspect=16:9
image tabtbl = "[ref:@cust][ref:@staff]A white tablet propped on a stand on a light oak dining table at home; the screen shows a video call with the staff woman smiling and greeting; in the soft-focus foreground the hands of the customer woman (cream-white knit sleeves)" aspect=16:9
image staff_face = "[ref:@staff]Tight head-and-shoulders close-up of the same staff woman (navy blazer, low bun, single-ear headset) smiling warmly toward the camera, soft bright office background"
sfx off
# テロップ・見出し・札は文の頭に文の要旨を一度に出し、進行の板は 4 段を頭から並べる (字幕 off の代わり・hf の作り)
lint off=spoiler,all_at_once
# 画面の UI の写し (タブレット・資料の札・進行の板) と英字の小見出しは hf の実寸 (1080p で 14〜24 px)
lint off=small_text
# 画面に寄った後 (タブレットを to で動かした後) に出す枠と吹き出しを、lint は動く前のタブレットの箱と比べる (誤検知)
lint off=child_overflow
# 切替は hf の 600 ms の crossfade (新しい場面が旧場面の上に溶ける) — 半面の写真と大きな字も溶け合う
lint off=ghost_dissolve
# 題と締めは白地のロゴだけの 1 枚 (hf の作り)
lint off=text_only_cut,sparse_cut
p { color: $ink; out: none }
div { out: none }
img { out: none }
shape { out: none }
icon { out: none }
cut { stagger: 0 }
sound pad = "柔らかいシンセパッドの持続音、静かな広がり"
sound bell = "澄んだベルの単音、短い余韻"
sound bell_lo = "低めのベルの単音"
sound tap = "軽いタップ音、短いクリック"
sound whoosh = "短い風切り音"
sound smooth = "滑らかなスライドの音"
sound connect = "接続した時の柔らかい電子音"
sound shimmer = "きらめく高いシマー音"
sound end_sh = "長い余韻のシマー音"
sound shwip = "軽い布のひるがえる音"
sound notify = "通知の柔らかい電子音"
sound click = "軽いクリック音"
sound swell = "ゆっくり膨らむ弦の音"
sound paper = "紙をめくる音"
sound done = "完了を告げる明るい二音"
bgm#music(duck: -7; fade: 1200,1500; keys: "0:+2|8s:0|end-6s:+2"; jump: at_cut:anywhere>166.8s; xfade: 1300) 上品で落ち着いたコーポレート向けのピアノと弦、企業紹介向け
# 進行の板の 1 段: 今の段 (輪・「サポート中」・名を濃く) / 済んだ段 (✓)
cue step_on(x) = [>#x.cur][>#x.st][!#x.nm recolor,$ink,duration=300]
cue step_done(x) = [<#x.cur][<#x.st][>#x.ck +50][>#x.ci +50]

# テロップ (左下の白い札・青の縁) と章の札 (左上の白い丸札)
def telop(t, y=582) = p(left: 64px; top: {y}; font-size: 31px; line-height: 1.42; letter-spacing: 0.05em; content: {t}; background: #FFFFFFF5; border-radius: 7px; padding: 16px 29px 17px 31px; edge: left,4,$a; box-shadow: 0px 11px 29px #0E2A472E; in: wipe {dir: 'right', duration: 0.55, ease: 'power3.out'}; out: {y:-4, opacity:0, duration:0.35})
def chap(n, t) = p(left: 61px; top: 51px; font-size: 18px; letter-spacing: 0.06em; background: #FFFFFFF2; border-radius: 99px; padding: 11px 20px 11px 17px; box-shadow: 0px 7px 20px #0E2A471F; in: {x:-16, opacity:0, duration:0.55, ease:'power3.out'}; out: {x:-8, opacity:0, duration:0.3}) {k}STEP {n}{/}　{l}｜{/}　{t}
# 写真の左下の札 (icon の丸 + 2 行)
def photo_tag(ic, t) = div(width: 320px; height: 104px; background: #FFFFFFF2; border-radius: 8px; box-shadow: 0px 9px 27px #0E2A4724; in: rise {y: 11, duration: 0.55})
  shape#c.ellipse(left: 17px; cy: 50%; width: 39px; height: 39px; background: #EEF1F5)
  icon#i(left: 27px; cy: 50%; font-size: 20px; name: {ic}; color: #5D6D80)
  p#t(left: 69px; cy: 50%; font-size: 27px; line-height: 1.35; content: {t})
# 白地の場面の地 (淡い光 + 画面の外へはみ出す薄い輪 2 つ) とロゴ (1 字ずつせり上がる)
def soft_bg() = div(inset: 0; background: radial(#F2F7FE,#FFFFFF@70%,50%,45%); z-index: back; border-radius: 16px)
def rings(x1, x2, y=-140, d=1000) = div.bleed(inset: 0)
  shape#r1.ellipse(left: {x1}; top: {y}; width: {d}; height: {d}; background: none; border: 1px solid #1F6FE01F; main: ramp {scale: 0.08})
  shape#r2.ellipse(left: {x2}; top: {y}; width: {d}; height: {d}; background: none; border: 1px solid #1F6FE01F; main: ramp {scale: 0.08})
def wordmark(y) = p(cx: 640px; top: {y}; font-size: 100px; font-family: e; in: {y:27, opacity:0, duration:0.8, ease:'power3.out', stagger:.045}) Live {a}Assist{/}

# タブレット: 枠・上の帯・右の側板。中の page と側板の中身は場面ごとに子で差す (def の実体の scale で縮める)
def tablet() = div(width: 787px; height: 533px; border-radius: 31px; background: #FFFFFF; border: 1px solid #DCE4EE; box-shadow: 0px 33px 73px #0E2A4738)
  div#scr(left: 12px; top: 12px; width: 763px; height: 509px; border-radius: 20px; background: $paper)
  div#bar(left: 12px; top: 12px; width: 763px; height: 51px; border-radius: 20,20,0,0; background: #FFFFFF)
  shape#lg(left: 36px; top: 28px; width: 19px; height: 19px; path: rect,r=0.28; background: linear(#2F7FF0,#63ADF7,135))
  p#tt(left: 64px; top: 24px; font-size: 17px; font-family: b; letter-spacing: 0.06em) マイページ
  p#us(left: 640px; top: 29px; font-size: 13px; color: $gray) 佐藤 美咲 様
  div#sd(left: 519px; top: 63px; width: 256px; height: 459px; background: #EEF3F9; border-radius: 0,0,20,0)
    p#br(left: 19px; top: 430px; font-size: 11px; font-family: e; color: $a) Live {nv}Assist{/}
# 1 枚目の page: 契約変更の form (段の札 4 つ・項目 3 行・次へ)。×N は 1 枠 + flex で等分し、×N の子は 1 段まで (入力の字は入力枠の兄弟)
def form_page() = div(width: 507px; height: 459px)
  p#t(left: 29px; top: 20px; font-size: 23px; font-family: b; letter-spacing: 0.05em) ご契約内容の変更
  div#st(left: 29px; top: 61px; width: 441px; height: 25px; display: flex; gap: 7px; border-radius: 13px; background: "#DBE9FB;$a;#E9EEF5;#E9EEF5") ×4
    p#t(cx: 50%; cy: 50%; font-size: 11px; color: "$a;#FFFFFF;#8A97A6;#8A97A6") 1 お客様情報;2 プラン選択;3 お支払い;4 確認
  div#row(left: 29px; top: 100px; width: 448px; height: 204px; display: flex; flex-direction: column; gap: 0px) ×3
    p#lb(left: 0px; top: 0px; font-size: 12px; color: $gray) ご契約者名;ご契約プラン;ご利用開始日
    div#in(left: 0px; top: 17px; width: 448px; height: 39px; border-radius: 7px; background: #FFFFFF; border: 1px solid #D5DEE9)
    p#v(left: 13px; top: 27px; font-size: 15px) 佐藤 美咲;{ph}選択してください{/};2026年11月1日
  icon#cv(left: 452px; top: 197px; font-size: 10px; name: caret-down; color: #7D8A99)
  div#btn(left: 29px; top: 316px; width: 200px; height: 41px; border-radius: 21px; background: $a; box-shadow: 0px 5px 12px #1F6FE040)
    p#t(cx: 50%; cy: 50%; font-size: 15px; font-family: b; color: #FFFFFF; letter-spacing: 0.1em) 次へ進む
# 2 枚目の page: 契約内容の確認 (項目の札 4 枚)
def plan_page() = div(width: 507px; height: 459px)
  p#t(left: 29px; top: 20px; font-size: 23px; font-family: b; letter-spacing: 0.05em) ご契約内容の確認
  p#s(left: 29px; top: 56px; font-size: 12px; color: $gray) 現在のご契約内容をご確認いただけます
  div#ic(left: 29px; top: 87px; width: 448px; height: 266px; display: flex; flex-direction: column; gap: 10px; border-radius: 8px; background: #FFFFFF; border: 1px solid #E3E9F1) ×4
    p#k(left: 16px; top: 9px; font-size: 11px; color: $gray) 現在のご契約プラン;オプション;お支払い方法;次回更新日
    p#v(left: 16px; top: 27px; font-size: 17px; font-family: b) スタンダードプラン;安心サポートパック;クレジットカード（**** 1234）;2027年3月31日
# 画面に差す部品: 通話中の側板 (スタッフの映像・名の帯・通話の釦 3 つ)・操作の案内・form の上に開くプランの一覧・スタッフのメッセージ
def call_panel() = div(width: 256px; height: 330px)
  img#fd(left: 19px; top: 19px; width: 219px; height: 157px; border-radius: 9px; content: @staff; object-fit: cover; object-position: 50% 30%)
  p#lv(left: 27px; top: 27px; font-size: 9px; color: #FFFFFF; background: #0E2A478C; border-radius: 99px; padding: 4px 8px) {gn}●{/} 通話中
  p#nm(left: 19px; top: 150px; width: 219px; padding: 6px 9px 6px 9px; font-size: 10px; color: #FFFFFF; letter-spacing: 0.05em; background: #0E2A4773; border-radius: 9px) 高橋（サポート担当）
  div#b(left: 55px; top: 188px; width: 150px; height: 35px; display: flex; gap: 0px) ×3
    shape#c.ellipse(cx: 50%; cy: 50%; width: 35px; height: 35px; background: "#FFFFFF;#FFFFFF;$red")
    icon#i(cx: 50%; cy: 50%; font-size: 20px; name: "microphone;video-camera;phone-x"; color: "$ink2;$ink2;#FFFFFF")
def help_panel() = div(width: 219px; height: 220px; border-radius: 11px; background: #FFFFFF; box-shadow: 0px 7px 17px #0E2A471A)
  shape#c.ellipse(left: 19px; top: 20px; width: 43px; height: 43px; background: $sky)
  icon#i(left: 30px; top: 31px; font-size: 20px; name: headset; color: $a)
  p#h(left: 19px; top: 77px; font-size: 16px; font-family: b) 操作でお困りですか？
  p#d(left: 19px; top: 105px; width: 184px; font-size: 11px; color: $gray; line-height: 1.55) Live Assist なら、スタッフが画面を見ながらご案内します。
  div#b(left: 19px; top: 164px; width: 181px; height: 37px; border-radius: 19px; background: $a)
    p#t(cx: 50%; cy: 50%; font-size: 13px; font-family: b; color: #FFFFFF) スタッフにつなぐ
def dropdown() = div(width: 448px; height: 144px; border-radius: 8px; background: #FFFFFF; box-shadow: 0px 12px 27px #0E2A4729; in: {y:-5, opacity:0, duration:0.3, ease:'power2.out'}; out: fade {duration: 0.3})
  div#hv(left: 0px; top: 36px; width: 448px; height: 36px; background: #F0F5FC; border-radius: 16px)
  p#o1(left: 15px; top: 9px; font-size: 14px) スタンダードプラン
  p#o2(left: 15px; top: 45px; font-size: 14px) スタンダードプラス
  p#o3(left: 15px; top: 81px; font-size: 14px) プレミアムプラン
  p#o4(left: 15px; top: 117px; font-size: 14px) プレミアムライト
def staff_msg() = div(width: 219px; height: 118px; border-radius: 9px; background: #FFFFFF; box-shadow: 0px 5px 15px #0E2A471A; in: {y:9, opacity:0, duration:0.5, ease:'power2.out'})
  p#w(left: 12px; top: 12px; font-size: 9px; color: $gray) スタッフ 高橋
  p#t(left: 12px; top: 28px; width: 195px; font-size: 13px; line-height: 1.5) こちらのページで、現在のプランをご確認いただけます。
  div#lk(left: 12px; top: 76px; width: 195px; height: 31px; border-radius: 7px; background: $sky)
    p#t(left: 11px; cy: 50%; font-size: 12px; font-family: b; color: $a) ご契約内容の確認
    icon#i(left: 172px; cy: 50%; font-size: 10px; name: caret-right; color: $a)
# 画面の上に重ねる物: 共有中の札・青い強調枠・スタッフの吹き出し・カーソル + 名札 (吹き出しとカーソルは page の文字より前 = z-index: front)
def share_badge() = p(cx: 50%; top: 24px; font-size: 11px; font-family: b; color: #FFFFFF; letter-spacing: 0.08em; background: $a; border-radius: 99px; padding: 6px 16px; in: {scale:0.8, opacity:0, duration:0.4, ease:'back.out(2)'}) ●  画面共有中
def focus_box(w, h) = div(width: {w}; height: {h}; border-radius: 9px; border: 2px solid $a; box-shadow: 0px 0px 0px 5px #1F6FE029; in: {scale:1.04, opacity:0, duration:0.35, ease:'power2.out'}; out: fade {duration: 0.3})
def bubble(t, w) = div(width: {w}; height: 35px; border-radius: 99px; background: #FFFFFF; box-shadow: 0px 8px 19px #0E2A472E; z-index: front; in: {y:7, opacity:0, duration:0.4, ease:'power2.out'}; out: fade {duration: 0.3})
  img#f(left: 5px; cy: 50%; width: 27px; height: 27px; border-radius: 99px; content: @staff_face; object-fit: cover; object-position: 50% 35%)
  p#t(left: 40px; cy: 50%; font-size: 13px; content: {t})
def cursor() = shape(width: 27px; height: 27px; path: cursor; background: $a; border: 1px solid #FFFFFF; z-index: front)
def cursor_tag() = p(font-size: 9px; font-family: b; color: #FFFFFF; background: $a; border-radius: 99px; padding: 5px 8px; z-index: front) スタッフ

# 冒頭: 白から溶ける全面の写真に、手続きの札 4 枚が順に
section#intro
img#in_p(inset: 0; main: kb {scale: [1.1, 1], focus: '19% 50%', ease:'power1.out'}) [ref:@cust]Wide establishing shot of the same woman (same face, wavy dark brown hair, cream-white knit sweater, pearl earrings) on a light linen sofa in her bright white living room, relaxed, using a white tablet held in both hands, 3/4 side angle, large window, plants
div#ch(left: 69px; top: "191;259;327;395"; width: 227px; height: 56px; border-radius: 9px; background: #FFFFFFF5; box-shadow: 0px 8px 20px #0E2A471A; in: {x:-17, opacity:0, duration:0.6, ease:'power3.out', stagger: {each: 0.2}}) ×4
  shape#c.ellipse(left: 16px; cy: 50%; width: 31px; height: 31px; background: $sky)
  icon#i(left: 23px; cy: 50%; font-size: 17px; color: $a; name: "file-text;clipboard-text;arrows-clockwise;credit-card")
  p#t(left: 59px; cy: 50%; font-size: 18px; letter-spacing: 0.05em) お申し込み;ご契約のお手続き;登録内容の変更;お支払い
telop#in_tel オンラインで{bb}完結する{/}時代

# 問い: 戸惑う顔の寄り → ぼかした写真の上にタブレット (指が迷い、プランの一覧が開いて閉じる)
section#confused
img#cf_p(inset: 0; content: @conf; main: kb {scale: [1, 1.09], focus: '67% 29%'})
img#cf_b(inset: 0; content: @conf; filter: blur(6px); delay: 3500; in: fade {duration: 0.6}; main: kb {scale: [1, 1.06]})
tablet#tc(left: 286px; top: 91px; scale: 0.9; delay: 3500; in: fade {duration: 0.6})
  form_page#p1(left: 11px; top: 57px; scale: 0.9)
  help_panel#hp(left: 484px; top: 81px; scale: 0.9)
  dropdown#dd(left: 37px; top: 261px; scale: 0.9; z-index: front; overlap: tc.p1)
  shape#tch.ellipse(left: 379px; top: 225px; width: 32px; height: 32px; background: #0E2A4729; border: 2px solid #FFFFFFF2; z-index: front; in: {x:156, y:82, opacity:0, duration:0.9, ease:'power2.inOut'}; overlap: tc.p1,tc.hp)
telop#cf_tel 「{bb}誰かに聞きたい{/}」と思う瞬間

# つなぐ: 画面を押す指の波紋 → 白地で 2 人の顔を弧で結び、点が渡って「つなぐ。」
section#tap_connect
img#tp_p(inset: 0; main: kb {scale: [1.02, 1.12], focus: ['', '76% 65%']}; out: fade {duration: 0.6}) [ref:@cust]Over-the-shoulder close-up from behind the same woman (cream-white knit sleeve and wavy dark brown hair visible) tapping a white tablet with her index finger; the screen shows a clean white app with one round soft-blue button glowing gently, very shallow depth of field
shape#rp.ellipse(left: "853;821"; top: "300;268"; width: "144;208"; height: "144;208"; background: none; border: 2px solid #FFFFFFF2; glow: #1F6FE08C,16; in: keys(at=0 scale=0.1 opacity=0.95 | at=1 ease=power2.out),duration=1000; out: fade {duration: 0.4}) ×2
soft_bg#cn_bg(delay: 2300; in: fade {duration: 0.6})
rings#cn_r(x1: 173; x2: 507; top: -40px; d: 600; delay: 2300; in: fade {duration: 0.6})
shape#cn_l1(path: "M 507 300 C 600 233, 680 233, 773 300"; background: none; border: 3px solid #1F6FE073; dash: 1,9; delay: 2600; in: fade {duration: 0.4})
shape#cn_l2(path: "M 507 300 C 600 233, 680 233, 773 300"; background: none; border: 3px solid $a; delay: 2750; in: draw {duration: 0.8})
img#av1(left: 207px; top: 200px; width: 200px; height: 200px; border-radius: 100px; border: 5px solid #FFFFFF; box-shadow: 0px 13px 33px #0E2A4729; content: @cust; object-fit: cover; object-position: 55% 28%; zoom: 190%; delay: 2450; in: {scale:0.85, opacity:0, duration:0.7, ease:'back.out(1.4)'})
img#av2(left: 773px; top: 200px; width: 200px; height: 200px; border-radius: 100px; border: 5px solid #FFFFFF; box-shadow: 0px 13px 33px #0E2A4729; content: @staff; object-fit: cover; object-position: 50% 28%; zoom: 190%; delay: 2650; in: {scale:0.85, opacity:0, duration:0.7, ease:'back.out(1.4)'})
p#wh1(cx: 307px; top: 427px; font-size: 20px; letter-spacing: 0.12em; text-align: center; line-height: 1.3; color: $ink2; delay: 2750; in: {y:8, opacity:0, duration:0.5, ease:'power2.out'}) {k2}CUSTOMER{/}[br]お客様
p#wh2(cx: 873px; top: 427px; font-size: 20px; letter-spacing: 0.12em; text-align: center; line-height: 1.3; color: $ink2; delay: 2950; in: {y:8, opacity:0, duration:0.5, ease:'power2.out'}) {k2}STAFF{/}[br]スタッフ
shape#cd.ellipse(left: 501px; top: 294px; width: 12px; height: 12px; background: $a; box-shadow: 0px 0px 0px 5px #1F6FE02E; in: fade {duration: 0.15}; out: fade {duration: 0.2})
p#cbig(cx: 640px; top: 528px; font-size: 37px; letter-spacing: 0.08em; in: {y:11, opacity:0, duration:0.6, ease:'power2.out'}) お客様とスタッフを、{bb}つなぐ。{/}

# 題: 1 字ずつ上がるロゴ + 罫 + 一言
section#title
soft_bg#ti_bg
rings#ti_r(x1: 220; x2: 60)
wordmark#ti_w(top: 237px; delay: 250)
shape#ti_rl(left: 593px; top: 377px; width: 93px; height: 2px; path: rect,r=0.5; background: $a; delay: 900; in: wipe {dir: 'center', duration: 0.6, ease: 'power2.inOut'})
p#ti_t(cx: 640px; top: 404px; font-size: 28px; letter-spacing: 0.1em; color: $ink2; delay: 1350; in: {y:9, opacity:0, duration:0.8, ease:'power2.out'}) オンラインなのに、まるで隣にいるようなサポート。

# 今の不便: チャットの写真が左半分に寄り、右から電話の写真が入る (写真の左下に札)
section#chat_phone
img#pn_c(inset: 0; object-fit: cover; object-position: 58% 50%; filter: saturate(0.8); main: kb {scale: [1.04, 1.1], focus: ['', '60% 50%']}) [ref:@cust]Medium shot of the same woman at a white dining table at home, typing on the white tablet with a slightly troubled thoughtful expression, as if struggling to explain her problem in a text chat; the screen shows abstract gray and blue chat bubbles
photo_tag#lb_c(left: 43px; top: 560px; ic: chat-circle-dots; t: "チャットだけでは[br]伝えにくい")
img#pn_p(left: 640px; top: 0px; width: 640px; height: 720px; object-fit: cover; object-position: 52% 50%; filter: saturate(0.8); main: kb {scale: [1.06, 1.12], focus: ['', '41% 50%']}; in: {x:640, duration:0.75, ease:'power3.inOut'}) [ref:@cust]Medium shot of the same woman at home holding a smartphone to her ear while looking down at a white tablet on the table with a confused expression, trying to follow spoken instructions about a screen the other person cannot see
shape#pn_d.bleed(left: 640px; top: 0px; width: 4px; height: 720px; path: rect; background: #FFFFFF; in: {x:640, duration:0.75, ease:'power3.inOut'})
photo_tag#lb_p(left: 683px; top: 560px; ic: phone; t: "電話だけでは[br]確認しにくい")

# STEP 01: 通話する客の肩越し → スタッフの側へ溶ける
section#face
img#fc1(inset: 0; main: kb {scale: [1, 1.08], focus: '30% 50%'}) [ref:@cust][ref:@staff]Over-the-shoulder shot from behind and slightly to the side of the customer woman (cream-white knit sweater, wavy dark brown hair) on her sofa holding a white tablet; the tablet clearly shows a live video call with the staff woman (navy blazer, headset, low bun) smiling
img#fc2(inset: 0; main: kb {scale: [1.05, 1], focus: '81% 50%'}; in: fade {duration: 0.7, ease: 'power1.inOut'}) [ref:@staff][ref:@cust]The staff woman (navy blazer, low bun, single-ear headset) at her white desk in the bright support office, turning toward her monitor with a warm welcoming smile as an incoming video call with the customer woman connects, one hand lightly touching the headset
chap#c1(n: 01; t: "顔を見て相談")
telop#fc_tel {bb}顔を見ながら{/}、状況に合わせてサポート

# STEP 02: スタッフの写真 + 共有中のタブレット。カーソルが動き、画面に寄って強調枠と吹き出しで案内
section#share_screen
div#sc_bg(inset: 0; background: $paper; border-radius: 16px)
img#pn_s(left: 0px; top: 0px; width: 573px; height: 720px; object-fit: cover; object-position: 47% 50%; main: kb {scale: [1, 1.06], focus: '31% 50%'}) [ref:@staff]Medium close-up of the same staff woman at her desk looking attentively at her monitor while guiding with a mouse, gentle focused expression, speaking into the headset microphone, soft monitor glow, bright office
tablet#ts(left: 612px; top: 147px; scale: 0.8; delay: 200; in: {x:293, duration:0.9, ease:'power3.out'})
  form_page#p1(left: 10px; top: 50px; scale: 0.8)
  call_panel#cp(left: 415px; top: 50px; scale: 0.8)
  share_badge#sh(top: 19px; scale: 0.8)
  focus_box#h1(left: 29px; top: 194px; width: 459px; height: 49px; scale: 0.8; overlap: ts.p1)
  focus_box#h2(left: 29px; top: 298px; width: 211px; height: 52px; scale: 0.8; overlap: ts.p1)
  bubble#a1(left: 186px; top: 237px; t: "こちらからプランをお選びください"; width: 266px; scale: 0.8; overlap: ts.p1)
  bubble#a2(left: 208px; top: 304px; t: "最後にこちらを押してください"; width: 240px; scale: 0.8; overlap: ts.p1)
  cursor#p(left: 468px; top: 308px; scale: 0.8; in: {x:64, y:43, opacity:0, duration:0.6, ease:'power2.out'}; overlap: ts.p1,ts.cp,ts.a1,ts.a2)
  cursor_tag#pl(left: 484px; top: 324px; scale: 0.8; in: {x:64, y:43, opacity:0, duration:0.6, ease:'power2.out'}; overlap: ts.p1,ts.cp,ts.a1,ts.a2)
chap#c2(n: 02; t: "画面を見ながらご案内")
telop#sc_tel(top: 538px) お客様の{bb}画面を見ながら{/}[br]リアルタイムにご案内

# 安心: ほっとした顔の寄り
section#relief
img#rl_p(inset: 0; main: kb {scale: [1, 1.08], focus: '63% 38%'}) [ref:@cust]Medium close-up of the same woman on her sofa looking at the white tablet with a relieved, understanding smile, nodding slightly, one hand lightly on her chest, soft warm daylight
telop#rl_tel 迷いを、{bb}その場で解消{/}

# STEP 03: スタッフのメッセージ → カーソルがリンクを押し、確認の page へ送る
section#navigate
img#nv_b(inset: 0; content: @tabtbl; filter: blur(6px); main: kb {scale: [1, 1.05]})
tablet#tn(left: 286px; top: 127px; scale: 0.9)
  form_page#p1(left: 11px; top: 57px; scale: 0.9; out: {x:-30, opacity:0, duration:0.45, ease:'power3.in'})
  plan_page#p2(left: 11px; top: 57px; scale: 0.9; in: {x:30, opacity:0, duration:0.6, ease:'power3.out'})
  call_panel#cp(left: 467px; top: 57px; scale: 0.9)
  share_badge#sh(top: 22px; scale: 0.9; delay: 300)
  staff_msg#msg(left: 484px; top: 273px; scale: 0.9)
  focus_box#h3(left: 32px; top: 130px; width: 459px; height: 69px; scale: 0.9; overlap: tn.p2)
  cursor#p(left: 395px; top: 347px; scale: 0.9; in: {x:-24, y:24, opacity:0, duration:0.4}; overlap: tn.p1,tn.p2,tn.cp,tn.msg)
  cursor_tag#pl(left: 413px; top: 365px; scale: 0.9; in: {x:-24, y:24, opacity:0, duration:0.4}; overlap: tn.p1,tn.p2,tn.cp,tn.msg)
chap#c3(n: 03; t: "必要な情報へご案内")
telop#nv_tel 必要な情報へ、{bb}スムーズに{/}ご案内

# STEP 04: 資料の札が飛んで来て、共有の通知
section#document
img#dc_p(inset: 0; main: kb {scale: [1, 1.07], focus: '72% 50%'}) [ref:@cust][ref:@staff]Close shot of the customer woman (cream-white knit sweater, wavy dark brown hair) holding a white tablet tilted toward the camera; the screen shows a clean document page preview (white brochure page with a blue header band and gray lines) on the left and a small video call window with the staff woman on the right
div#doc1(left: 891px; top: 119px; width: 293px; height: 88px; border-radius: 11px; background: #FFFFFF; box-shadow: 0px 16px 40px #0E2A4738; in: {x:280, y:-27, rotation:6, opacity:0, duration:0.65, ease:'power3.out'})
  div#fi(left: 17px; cy: 50%; width: 49px; height: 61px; border-radius: 7px; background: $sky)
    icon#i(cx: 50%; top: 11px; font-size: 29px; name: file-text; color: $a)
    p#pdf(left: 7px; top: 48px; font-size: 9px; font-family: e; color: #FFFFFF; background: $red; border-radius: 4px; padding: 3px 5px) PDF
  p#n(left: 81px; top: 24px; font-size: 17px; font-family: b; letter-spacing: 0.03em) サービスご案内資料
  p#s(left: 81px; top: 52px; font-size: 11px; color: $gray) スタッフ 高橋より ・ 2.4MB
p#toast(left: 891px; top: 224px; font-size: 15px; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 11px 19px 11px 48px; box-shadow: 0px 9px 23px #0E2A4747; in: {y:9, opacity:0, duration:0.45, ease:'power2.out'}) 資料が共有されました
  shape#ok.ellipse(left: 12px; cy: 50%; width: 23px; height: 23px; background: $ok)
  icon#i(left: 16px; cy: 50%; font-size: 15px; name: check; weight: bold; color: #FFFFFF)
chap#c4(n: 04; t: "資料をその場で共有")
telop#dc_tel 資料や書類も、{bb}その場で共有{/}

# STEP 05: 左に写真・右に進行の板 (段ごとに ✓ と縦線が伸び → 完了の板) → 完了の写真が覆う
section#procedure
div#pr_bg(inset: 0; background: $paper; border-radius: 16px)
img#pr_p(left: 0px; top: 0px; width: 653px; height: 720px; main: kb {scale: [1, 1.07], focus: '21% 50%'}) [ref:@cust]Medium shot of the same woman at a white dining table at home, entering information on a white tablet with her finger, calm and focused, a cup of tea and a pen beside her, a printed document on the table; the screen shows a simple form with blue progress steps
div#fl(left: 701px; top: 80px; width: 520px; height: 560px; border-radius: 15px; background: #FFFFFF; border: 1px solid $rule; box-shadow: 0px 20px 53px #0E2A4724; delay: 300; in: {x:40, opacity:0, duration:0.8, ease:'power3.out'})
  p#h(left: 32px; top: 29px; font-size: 21px; font-family: b; letter-spacing: 0.06em) お手続きの進行状況
  p#sub(left: 32px; top: 63px; font-size: 13px; color: $gray) ご契約内容の変更 ・ 4 ステップ
  div#sup(left: 32px; top: 100px; width: 456px; height: 85px; border-radius: 11px; background: $paper; border: 1px solid $rule)
    img#f(left: 11px; top: 11px; width: 85px; height: 64px; border-radius: 7px; content: @staff; object-fit: cover; object-position: 50% 30%)
    p#a(left: 112px; top: 17px; font-size: 16px; font-family: b) スタッフがサポート中
    p#b(left: 112px; top: 47px; font-size: 12px; color: $gray) {gn}●{/} Live Assist で通話中
  div#vl(left: 48px; top: 248px; width: 2px; height: 200px; background: $rule)
  div#vf(left: 48px; top: 248px; width: 2px; height: 2px; background: $a)
  div#s(left: 32px; top: "216;283;349;416"; width: 456px; height: 64px) ×4
    shape#d.ellipse(left: 0px; cy: 50%; width: 35px; height: 35px; background: #FFFFFF; border: 2px solid $line)
    p#n(left: 13px; cy: 50%; font-size: 14px; font-family: e; color: $mute) 1;2;3;4
    p#nm(left: 51px; cy: 50%; font-size: 18px; color: $mute; letter-spacing: 0.05em) お客様情報の入力;ご契約プランの選択;お支払い方法の登録;内容の確認・完了
    p#st(left: 380px; cy: 50%; font-size: 11px; font-family: b; color: $a; in: fade {duration: 0.3}; out: fade {duration: 0.25}) サポート中
    shape#cur.ellipse(left: -5px; cy: 50%; width: 45px; height: 45px; background: none; border: 2px solid #1F6FE059; in: {scale:0.8, opacity:0, duration:0.35}; out: fade {duration: 0.25})
    shape#ck.ellipse(left: 0px; cy: 50%; width: 35px; height: 35px; background: $a; in: {scale:0.6, opacity:0, duration:0.35, ease:'back.out(2)'})
    icon#ci(left: 8px; cy: 50%; font-size: 19px; name: check; weight: bold; color: #FFFFFF; in: {scale:0.6, opacity:0, duration:0.35, ease:'back.out(2)'})
  div#done(left: 0px; top: 0px; width: 520px; height: 560px; border-radius: 15px; background: #FFFFFF; in: fade {duration: 0.5}; overlap: fl.s)
    shape#c.ellipse(cx: 50%; top: 150px; width: 127px; height: 127px; background: $a; box-shadow: 0px 0px 0px 12px #1F6FE01F; in: {scale:0.5, opacity:0, duration:0.6, ease:'back.out(1.8)'})
    icon#i(cx: 50%; top: 180px; font-size: 66px; name: check; weight: bold; color: #FFFFFF; in: {scale:0.5, opacity:0, duration:0.6, ease:'back.out(1.8)'})
    p#t1(cx: 50%; top: 314px; font-size: 28px; font-family: b; letter-spacing: 0.08em) お手続きが完了しました
    p#t2(cx: 50%; top: 365px; font-size: 15px; color: $gray; letter-spacing: 0.06em) ご利用ありがとうございました
img#cp_p(inset: 0; main: kb {scale: [1.04, 1.1], focus: ['', '50% 59%']}; in: fade {duration: 0.6, ease: 'power1.inOut'}; overlap: fl) [ref:@cust]Medium shot of the same woman leaning back on her sofa with a satisfied bright smile, holding the white tablet whose screen shows one large soft-blue check mark in a circle on a white background, warm soft daylight, relief and completion
chap#c5(n: 05; t: "手続きをサポート")
telop#pr_tel(top: 538px) 手続きの途中も、[br]{bb}リアルタイム{/}にサポート
telop#pr_tel2(top: 538px) 完了まで、[br]{bb}迷わせない{/}サポート

# どこでも: 5 枚の写真の格子 (左下に端末の札・札の中身も tile の直下)。見出しは「人による」の語で
section#anywhere
soft_bg#aw_bg
p#aw_h(cx: 640px; top: 49px; font-size: 35px; letter-spacing: 0.1em; in: {y:11, opacity:0, duration:0.7, ease:'power2.out'}) どこにいても、{bb}人による{/}サポートを。
img#tl(left: "48;447;847;48;647"; top: "127;127;127;381;381"; width: "385;385;385;585;585"; height: 240px; border-radius: 11px; box-shadow: 0px 12px 29px #0E2A4724; delay: "350;690;1030;1370;1710"; in: {y:27, opacity:0, duration:0.7, ease:'power3.out'}; main: kb {scale: [1.12, 1.02]}) ×5 [ref:@cust][ref:@staff]The customer woman wearing a light beige trench coat over the cream knit, standing on a calm clean city sidewalk near a cafe terrace, looking at a smartphone whose screen shows a video call with the staff woman;[ref:@cust][ref:@staff]The customer woman at a small white desk in a quiet corner of her bright home, looking at a laptop PC with a relaxed smile, the laptop shows a video call with the staff woman;[ref:@cust][ref:@staff]A white tablet propped on a stand on a light oak dining table at home showing a video call with the smiling staff woman, the customer's hands in soft-focus foreground;[ref:@cust][ref:@staff]Inside a bright modern Japanese service store with white counters and light blue accents, the customer woman in a beige trench coat at a counter where a tablet on a stand shows a video call with the staff woman;[ref:@cust][ref:@staff]The customer woman wearing a light gray blazer at a desk in a bright modern office, looking at a laptop that shows a video call with the staff woman next to a document
  div#lb(left: 15px; top: 188px; width: 150px; height: 36px; border-radius: 99px; background: #FFFFFFF2; box-shadow: 0px 4px 12px #0E2A4724)
  shape#c.ellipse(left: 24px; cy: 206px; width: 23px; height: 23px; background: $sky)
  icon#i(left: 28px; cy: 206px; font-size: 15px; color: $a; name: "device-mobile;laptop;device-tablet;storefront;buildings")
  p#t(left: 56px; cy: 206px; font-size: 16px; font-family: b; letter-spacing: 0.08em) スマートフォン;PC;タブレット;店舗;オフィス

# 価値: 3 枚の写真を薄く並べ、語った列から点灯して下の文字の組が上がる
section#values
soft_bg#vl_bg
img#vp(left: "80;467;853"; top: 77px; width: 347px; height: 347px; border-radius: 12px; box-shadow: 0px 13px 33px #0E2A4724; in: {y:20, opacity:0, duration:0.8, ease:'power3.out'}; main: kb {scale: [1.12, 1]}) ×3 [ref:@cust]Tight close-up of the same woman looking at a tablet just below frame with a warm genuine smile, soft window light, creamy bokeh of the white living room, 85mm lens;[ref:@staff]The same staff woman working in a calm bright flexible workspace by a large window with plants and a light wood table, smiling while talking on a video call through a slim laptop;[photo]A modern Japanese corporate meeting room with large windows over a bright city, a small team of Japanese business people reviewing a large wall display showing an abstract customer-engagement dashboard with blue charts and connecting lines
#vp.dim(opacity: 0.32)
div#vc(left: "80;467;853"; top: 454px; width: 347px; height: 196px; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'}) ×3
  p#k(left: 3px; top: 0px; font-size: 11px; font-family: e; color: $a; letter-spacing: 0.26em) FOR CUSTOMERS;FOR STAFF;FOR BUSINESS
  p#n(left: 0px; top: 24px; font-size: 31px; font-family: b; letter-spacing: 0.1em) お客様;スタッフ;企業
  shape#ul(left: 0px; top: 66px; width: 40px; height: 2px; path: rect; background: $a; in: wipe {dir: 'right', duration: 0.5, ease: 'power2.out', delay: 0.4})
  p#d(left: 0px; top: 83px; font-size: 21px; line-height: 1.5; letter-spacing: 0.05em; color: $ink2) より安心で、[br]スムーズな体験を。;より柔軟な[br]接客環境を。;新たな[br]顧客接点を。

# 人: スタッフの寄り + 右へ白む幕に 2 段の言葉 (「人。」は語で)
section#human
img#hm_p(inset: 0; main: kb {scale: [1.12, 1.17], focus: ['80% 50%', '87% 50%']}) [ref:@staff]Tight close-up of the same staff woman, warm genuine smile, looking slightly off-camera toward her monitor, speaking softly into the headset microphone, soft key light from the window, creamy bokeh of the bright office, 85mm lens
div#hm_v(inset: 0; background: linear(#FFFFFF00@44%,#FFFFFFB3@62%,#FFFFFFE0,90); border-radius: 16px; delay: 200; in: fade {duration: 0.8})
p#hm1(left: 833px; top: 208px; font-size: 37px; font-family: r; letter-spacing: 0.12em; line-height: 1.55; in: {y:11, opacity:0, duration:0.7, ease:'power2.out'}) テクノロジーの[br]先にいるのは、
p#hm2(left: 829px; top: 333px; font-size: 112px; letter-spacing: 0.06em; in: {y:16, opacity:0, duration:0.9, ease:'power3.out'}) {a}人{/}。

# 結び: 2 人の写真を左右に、境目を点が降りる + 中央の札
section#together
img#tg1(left: 0px; top: 0px; width: 640px; height: 720px; content: @cust; object-fit: cover; object-position: 47% 50%; main: kb {scale: [1.08, 1], focus: '24% 50%'})
img#tg2(left: 640px; top: 0px; width: 640px; height: 720px; content: @staff; object-fit: cover; object-position: center; main: kb {scale: [1.08, 1], focus: '76% 50%'})
shape#tg_d.bleed(left: 638px; top: 0px; width: 4px; height: 720px; path: rect; background: #FFFFFF)
shape#tg_p.ellipse(left: 634px; top: 87px; width: 12px; height: 12px; background: $a; box-shadow: 0px 0px 0px 5px #1F6FE02E; in: fade {duration: 0.2}; out: fade {duration: 0.3})
p#tg_t(cx: 640px; top: 582px; font-size: 31px; letter-spacing: 0.06em; background: #FFFFFFF2; border-radius: 7px; padding: 16px 35px 17px 35px; box-shadow: 0px 9px 27px #0E2A4724; in: {y:9, opacity:0, duration:0.6, ease:'power2.out'}) デジタルと、人の接客を、{bb}もっと自然に。{/}

# 締め: ロゴ + 罫 + by Kumolis
section#end
soft_bg#en_bg
rings#en_r(x1: 220; x2: 60)
wordmark#en_w(top: 253px; delay: 450)
shape#en_rl(left: 593px; top: 392px; width: 93px; height: 2px; path: rect,r=0.5; background: $a; delay: 1100; in: wipe {dir: 'center', duration: 0.6, ease: 'power2.inOut'})
p#en_by(cx: 640px; top: 420px; font-size: 27px; font-family: e; letter-spacing: 0.08em; color: $ink2; in: {y:8, opacity:0, duration:0.8, ease:'power2.out'}) by {nv}Kumolis{/}
```

```timeline.txt
#v2
cast narrator = "落ち着いた上品な男性ナレーター" manner="落ち着いた上品なトーンで、企業紹介ビデオのナレーションとして、ゆったりと丁寧に"
silence head=0 tail=0
transition = dissolve,300,overlap=300

*** intro
fade in,1600
bgm music
@narrator: [silence:3.4s][♪pad -1dB -3250][>#in_tel +300][<#in_tel cut-150][>#ch[*] +550][♪bell -7dB +550]さまざまなサービスが、オンラインで完結する時代。[silence:0.55s]

*** confused
@: [silence:0.45s][>#cf_tel +2500][<#cf_tel cut-200][>#tc.tch +3650][>#tc.dd +4600][!#tc.tch to,{x:-72, y:82, duration:.8, ease:'power1.inOut'} +4950][!#tc.tch to,{x:-24, y:51, duration:.7, ease:'power1.inOut'} +5850][!#tc.tch to,{x:-103, y:114, duration:.7, ease:'power1.inOut'} +6650][<#tc.dd +7450][!#tc.tch to,{x:187, y:4, duration:.7, ease:'power2.inOut'} +7550]便利になった一方で、お客様が『誰かに聞きたい』と思う瞬間は、今もなくなっていません。[silence:1.95s]

*** tap_connect
@: [silence:0.25s][♪tap +550][>#rp[1] +550][>#rp[2] +730][<#rp[1] +1050][<#rp[2] +1300][<#tp_p +2050][♪whoosh -4dB +1950][>#cd +2500][!#cd to,{x:266, arc:0.3, duration:0.8, ease:'power2.inOut'} +2550][<#cd +3350][>#cbig +3200][!#av1 ping,$b2,scale=1>1.35 +3300][!#av2 ping,$b2,scale=1>1.35 +3300][♪connect -1dB +3300]そんな瞬間に、お客様とスタッフをつなぐ。[silence:1.55s]

*** title
@: [silence:0.15s][♪shimmer -50]それが、Live Assistです。[silence:2.55s]

*** chat_phone
@: [silence:0.55s][♪shwip -6dB -500][>#lb_c +200]チャットだけでは伝えにくいこと。[silence:0.8s]
@: [>#pn_p -350][>#pn_d -350][!#pn_c to,{w:640, duration:0.75, ease:'power3.inOut'} -350][♪shwip -6dB -200][>#lb_p +250]電話だけでは確認しにくいこと。[silence:1.25s]

*** face
@: [silence:0.35s][♪smooth -4dB -330][>#c1][<#c1 cut-100][>#fc_tel +500][<#fc_tel cut-150][>#fc2 +3550][♪whoosh -8dB +3550]Live Assistなら、顔を見ながら、お客様の状況に合わせてサポートできます。[silence:1.85s]

*** share_screen
@: [silence:0.45s][>#c2 -100][<#c2 cut-100][>#sc_tel +450][♪notify -4dB +650][>#ts.sh +650][>#ts.p +1150][>#ts.pl +1150][!#ts.p to,{x:-160, y:-96, duration:1.2, ease:'power2.inOut'} +1950][!#ts.pl to,{x:-160, y:-96, duration:1.2, ease:'power2.inOut'} +1950][!#ts.p to,{x:-298, y:0, duration:1.1, ease:'power2.inOut'} +3550][!#ts.pl to,{x:-298, y:0, duration:1.1, ease:'power2.inOut'} +3550]さらに、お客様が見ている画面を確認しながら、リアルタイムで[<#sc_tel -300][!#pn_s to,{x:-587, duration:0.9, ease:'power3.inOut'} -100][!#ts to,{x:-287, y:31, duration:1, ease:'power3.inOut'} -100][!#ts.p to,{x:-117, y:-93, duration:.8, ease:'power2.inOut'} +300][!#ts.pl to,{x:-117, y:-93, duration:.8, ease:'power2.inOut'} +300][>#ts.h1 +800][♪click -4dB +800][>#ts.a1 +1000]ご案内。[silence:1.0s]
@: どこを見ればいいのか、[!#ts.p to,{x:-325, y:13, duration:.8, ease:'power2.inOut'} -650][!#ts.pl to,{x:-325, y:13, duration:.8, ease:'power2.inOut'} -650][<#ts.h1 +100][<#ts.a1 +100][>#ts.h2 +100][♪click -4dB +100][>#ts.a2 +300]どこを操作すればいいのか。[silence:0.6s]

*** relief
@: [silence:0.3s][♪swell -6dB -250][>#rl_tel +350][<#rl_tel cut-150]そんな迷いを、その場で解消します。[silence:1.85s]

*** navigate
@: [silence:0.45s][>#c3 -100][<#c3 cut-100][>#nv_tel +400][<#nv_tel cut-150][>#tn.msg +1200][♪bell_lo -4dB +1200][>#tn.p +1400][>#tn.pl +1400][!#tn.p to,{x:189, y:5, duration:1, ease:'power2.inOut'} +1700][!#tn.pl to,{x:189, y:5, duration:1, ease:'power2.inOut'} +1700][!#tn.msg.lk punch,0.96,duration=240 +2750][♪click -4dB +2750][<#tn.p1 +2950][>#tn.p2 +2950][♪shwip -5dB +2950][!#tn.p to,{x:-49, y:-174, duration:.9, ease:'power2.inOut'} +3450][!#tn.pl to,{x:-49, y:-174, duration:.9, ease:'power2.inOut'} +3450][>#tn.h3 +4150]必要な情報が別のページにある場合も、スタッフからスムーズにご案内。[silence:0.7s]

*** document
@: [silence:0.4s][>#c4 -50][<#c4 cut-100][>#dc_tel +350][<#dc_tel cut-150][>#doc1 +650][♪shwip -4dB +650][♪paper -2dB +1250][>#toast +1450][♪bell -6dB +1450]必要な資料や書類も、その場でお客様へ共有できます。[silence:1.85s]

*** procedure
@: [silence:0.45s][>#c5 -100][>#pr_tel +400][step_on #fl.s[1] +50]手続きの途中で[step_done #fl.s[1] -50][step_on #fl.s[2]][!#fl.vf to,{h:67, duration:.5, ease:'power2.inOut'}][♪click -6dB]分からないことがあっても、スタッフが[step_done #fl.s[2] -50][step_on #fl.s[3]][!#fl.vf to,{h:133, duration:.5, ease:'power2.inOut'}][♪click -6dB]リアルタイムでサポート。[silence:1.0s]
@: [<#pr_tel -250][>#pr_tel2 +300]お客様を迷わせることなく、[step_done #fl.s[3] -50][step_on #fl.s[4]][!#fl.vf to,{h:200, duration:.5, ease:'power2.inOut'}][♪click -6dB]手続きの[step_done #fl.s[4] +300]完了まで[>#fl.done][♪done]サポート[<#c5 +100][<#pr_tel2 +100][>#cp_p +500]します。[silence:2.55s]

*** anywhere
@: [silence:0.45s][♪pad -4dB -400]お客様がどこにいても、必要な瞬間に、[>#aw_h]人によるサポートを届ける。[silence:2.65s]

*** values
@: [silence:0.55s][>#vp[1] -300][>#vp[2] .dim -180][>#vp[3] .dim -60][>#vc[1] -50][♪bell_lo -7dB +50]お客様には、より安心でスムーズな体験を。[silence:1.1s]
@: [=#vp[2] -150][>#vc[2] -50][♪bell_lo -7dB +50]スタッフには、より柔軟な接客環境を。[silence:1.1s]
@: [=#vp[3] -150][>#vc[3] -50][♪bell_lo -7dB +50]企業には、新たな顧客接点を。[silence:2.3s]

*** human
@: [silence:0.5s][♪swell -5dB -450][>#hm1 +100]テクノロジーの先にいるのは、[>#hm2]人。[silence:1.6s]

*** together
@: [silence:0.45s][>#tg_p +350][!#tg_p to,{y:534, duration:2.4, ease:'power1.inOut'} +400][<#tg_p +2550][♪whoosh -8dB +450][>#tg_t +400]デジタルと、人による接客を、もっと自然につなげていく。[silence:1.8s]

*** end
@: [silence:0.7s][♪end_sh -1dB -600]Live Assist [>#en_by]by Kumolis。[silence:5.5s]
```

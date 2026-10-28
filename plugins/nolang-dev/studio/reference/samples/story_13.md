# story · 碓氷馬車鉄道 (縦・語り + 2 人の役・錦絵調) — canvas 1080x1920・69.8s・視聴者 88.5 (Gemini・vs hf)

見せる文法: ×N・stack・manner・se・sticky・def・run・bgm 切替・2 cast+

```design.txt
#v2
# 計画: 明 (生成りの和紙) + 朱 1 色 + 藍の差し色・墨の太い縁 + ずらした硬い影 (札・板に共通)・書体 極太の筆文字 (見出しの telop) + 太い丸ゴシック (本文・札) + 太い明朝 (年号・名)
# 絵は錦絵風のコミカルなイラストで全 cut 統一・全面の絵 + 上だけ暗くする幕 + 傾いた札・字幕は墨の札
canvas 1080x1920 bg=#F4EBD9
theme light
palette a=#D9472B b=#2F5E8E ink=#2A1E17 paper=#F7F0E1 mute=#7A6A58 gold=#E0A526
font "太い丸ゴシック体、親しみやすくやさしい印象"
fonts f="極太の筆文字、勢いのある見出し" e="太い明朝体、明治の活字のような格調"
art "明治時代の錦絵風のコミカルなイラスト、太い墨の輪郭線、平塗りの鮮やかな色、和紙の質感、誇張された表情"
prompt_tail "文字を描かない、ロゴなし"
image car = "明治時代の碓氷峠の馬車鉄道、茶色い馬一頭が小さな木造の客車を細いレールの上で引く、客車は箱形で窓が四つ、錦絵風のコミカルなイラスト、文字なし"
image ogai = "明治の文豪風の男性、口ひげ、丸刈り、黒い詰襟の軍服風の上着、知的で気難しい顔、錦絵風のコミカルなイラスト、上半身、文字なし"
motion title { in: {scale:0.5, opacity:0, duration:0.45, ease:'back.out(2.0)'}; out: {scale:0.9, opacity:0, duration:0.2} }
motion big { in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.6)'}; out: {scale:0.8, opacity:0, duration:0.18} }
motion div { in: {scale:0.85, y:45, opacity:0, duration:0.45, ease:'back.out(1.8)'}; out: fade {duration:0.2} }
motion row { in: {x:-120, opacity:0, duration:0.38, ease:'back.out(1.4)'}; out: fade {duration:0.18} }
motion note { in: {y:30, opacity:0, duration:0.35, ease:'back.out(1.4)'}; out: fade {duration:0.18} }
div { border-radius: 24px; border: 6px solid $ink; box-shadow: 10px 10px 0px $ink; background: $paper }
img { scrim: 0.2 }
cut { stagger: sentence }
run a { color: $a }
run g { color: $gold }
# 文字の段: telop 60 / 名 64 / kick 26 / 札 34
def tel(t) = p(font-size: 90px; font-family: f; color: $ink; background: $paper; border-radius: 15px; padding: 15px 39px; border: 6px solid $ink; box-shadow: 10px 10px 0px $ink; in: pop; content: {t})
def kick(t) = p(font-size: 39px; color: $paper; background: $a; border-radius: 148px; padding: 9px 30px; in: {x:-45, opacity:0, duration:0.4, ease:'power3.out'}; content: {t})
def tag(t) = p(font-size: 54px; color: $paper; background: $a; border-radius: 12px; padding: 12px 33px; border: 6px solid $ink; box-shadow: 8px 8px 0px $ink; in: pop; content: {t}; transform: rotate(-7deg))
subtitle.hug(font-size: 51px; bottom: 72px; background: #2A1E17EE; color: $paper; border-radius: 18px; padding: 15px 36px; line-height: 1.35)
bgm#music(volume: 4dB) 明治の雰囲気のとぼけた和風コミカル曲、三味線と木琴と拍子木、軽快でのんびり
bgm#music2(volume: 4dB) ドタバタの疾走感ある和風コミカル曲、速い太鼓と三味線の速弾き、慌ただしい追いかけっこ
bgm#music3(volume: 4dB) 穏やかでほのぼのした和風の曲、尺八と琴、夕暮れの余韻
sfx off

section#open
img#op_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 60%', '50% 55%']}) [ref:@car]霧のかかった険しい山の峠道、急な坂のレールを一頭の馬が小さな客車を引いて登っていく、引きの構図、明治の山村
veil#op_v(color: #2A1E17; opacity: 0.7; to: top; start: 0.45)
p#op_y(left: 72px; top: 180px; font-size: 45px; font-family: e; color: $ink; background: $gold; border-radius: 9px; padding: 6px 24px; in: {x:-45, opacity:0, duration:0.4, ease:'power3.out'}) 明治21年
p#op_d(left: 66px; top: 255px; font-size: 180px; font-family: e; color: $paper; text-shadow: 0px 6px 12px #00000099; in: drop {stagger: .045, duration: .7}) 1888.9.5
shape#op_r(left: 72px; top: 495px; width: 450px; height: 9px; path: line_h; background: $a; border: 9px solid $a; in: wipe {dir: 'right', duration: 0.6})
p#op_t(left: 72px; top: 534px; font-size: 96px; font-family: f; color: $paper; text-shadow: 0px 6px 12px #000000AA; in: rise {y: 45, duration: 0.5, stagger: .03}) 歴史的{a}珍{/}事件

section#horse
img#hs_p(inset: 0; main: kb {scale: [1.08, 1], focus: '50% 40%'}) [ref:@car]得意げに胸を張る茶色い馬の寄り、馬は客車につながれ、背後に急な坂とレール、晴れた山
veil#hs_v(color: #2A1E17; opacity: 0.55; to: top; start: 0.5)
p#hs_n(left: 72px; top: 180px; font-size: 84px; font-family: e; color: $paper; background: $ink; border-radius: 12px; padding: 12px 36px; border: 4px solid $gold; in: {x:-60, opacity:0, duration:0.45, ease:'power3.out'}) 碓氷馬車鉄道
tel#hs_t(left: 72px; top: 375px) 馬が電車を{a}引っ張る{/}!?
tag#hs_s(left: 570px; top: 1320px) 動力：馬 1頭

section#ogai
img#og_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 40%', '55% 35%']}) [ref:@ogai]客車の座席に背筋を伸ばして座り、窓の外の山を期待に満ちた顔で眺める文豪の男性、車内の木の壁
veil#og_v(color: #2A1E17; opacity: 0.55; to: top; start: 0.45)
div#og_c(left: 72px; top: 180px; width: 600px; height: 255px; in: {x:-60, opacity:0, duration:0.45, ease:'power3.out'})
  kick#k(left: 30px; top: 27px) 文豪
  p#n(left: 33px; top: 99px; font-size: 108px; font-family: e; color: $ink) 森鴎外
p#og_q(left: 495px; top: 1290px; font-size: 54px; color: $ink; background: $paper; border-radius: 30px; padding: 15px 36px; border: 6px solid $ink; shape: speech-bubble; in: pop) わくわく♪

section#rage
img#rg_p(inset: 0; main: kb {scale: [1.06, 1], focus: '50% 40%'}) [ref:@ogai]ガタガタ揺れる客車の中で鼻をつまみ顔を真っ赤にして怒る文豪の男性、帽子がずり落ちる、誇張された表情、車内が傾く、窓の外に馬の尻
veil#rg_v(color: #2A1E17; opacity: 0.5; to: top; start: 0.45)
tel#rg_t(left: 72px; top: 180px) 臭いと揺れが{a}最悪{/}
group#rg_row(left: 72px; top: 1170px; width: 936px; height: 300px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px)
  div#rg_k(in: rise {y: 45, duration: 0.45, stagger: 0.15}) ×2
    icon#i(cx: 50%; cy: 34%; font-size: 108px; name: "wind;wave-sine"; color: "$b;$a")
    p#t(cx: 50%; cy: 76%; font-size: 51px; color: $ink) 馬の臭い;大揺れ
tag#rg_s(left: 645px; top: 450px; font-size: 72px) 激怒

section#slow
img#sl_p(inset: 0; main: kb {scale: [1, 1.06], focus: ['40% 50%', '60% 50%']}) [ref:@car]のろのろと坂を登る馬車鉄道の横の山道を、旅姿の男が涼しい顔ですたすた歩いて追い越していく、横からの構図
veil#sl_v(color: #2A1E17; opacity: 0.55; to: top; start: 0.45)
tel#sl_t(left: 72px; top: 180px) とにかく{a}遅い{/}
div#sl_b(left: 72px; top: 1140px; width: 936px; height: 375px)
  shape#ln(left: 225px; top: 186px; width: 660px; height: 6px; path: line_h; background: $mute; border: 4px solid $mute; dash: 8,8)
  p#l1(left: 36px; top: 63px; font-size: 45px; color: $ink) 馬車
  p#l2(left: 36px; top: 243px; font-size: 45px; color: $a) 歩き
  icon#h(left: 225px; top: 36px; font-size: 120px; name: horse; color: $ink)
  icon#w(left: 225px; top: 213px; font-size: 120px; name: person-simple-walk; color: $a)

section#walk
img#wk_p(inset: 0; main: kb {scale: [1, 1.07], focus: '50% 45%'}) [ref:@car]止まりそうな客車から次々に降りてあきれ顔で歩き出す乗客たち、着物と荷物、のんびり立ち止まる馬、峠道
veil#wk_v(color: #2A1E17; opacity: 0.55; to: top; start: 0.45)
tel#wk_t(left: 72px; top: 180px) 歩いた方が{a}早い{/}!
icon#wk_i(left: "48;160;272"; top: 1260px; font-size: 144px; name: person-simple-walk; color: $ink; in: {x:-60, opacity:0, duration:0.4, ease:'power2.out', stagger: {each: 0.18}}) ×3
tag#wk_s(left: 600px; top: 1320px) 途中下車 続出

section#down
img#dn_p(inset: 0; main: kb {scale: [1, 1.12], focus: ['50% 50%', '60% 60%']}) [ref:@car]急な下り坂を猛スピードで駆け下りる客車、悲鳴をあげて帽子を押さえる乗客、必死に走る馬、飛び散る小石、スピード線、ダイナミックな斜めの構図
veil#dn_v(color: #2A1E17; opacity: 0.55; to: top; start: 0.45)
kick#dn_k(left: 72px; top: 180px) ところが下り坂
p#dn_br(left: 72px; top: 285px; font-size: 66px; color: $ink; background: $paper; border-radius: 12px; padding: 9px 30px; border: 6px solid $ink; in: {x:-45, opacity:0, duration:0.35, ease:'power3.out'}) ブレーキ {x}効く{/}
tag#dn_ng(left: 570px; top: 294px) 効かない!
tel#dn_t(left: 60px; top: 1290px; font-size: 81px; in: punch; transform: rotate(-4deg)) ジェットコースター状態

section#close
img#cl_p(inset: 0; main: kb {scale: [1, 1.05], focus: ['50% 50%', '45% 55%']}) [ref:@car]夕暮れの峠、役目を終えて草を食みながらのんびり振り返る茶色い馬、遠くの山のトンネルから蒸気機関車の白い煙、穏やかな橙の空
veil#cl_v(color: #2A1E17; opacity: 0.55; to: top; start: 0.45)
p#cl_y(left: 72px; top: 180px; font-size: 45px; font-family: e; color: $ink; background: $gold; border-radius: 9px; padding: 6px 24px; in: {x:-45, opacity:0, duration:0.4, ease:'power3.out'}) 1893年 アプト式 開通
p#cl_n(left: 72px; top: 270px; font-size: 66px; font-family: e; color: $paper; text-shadow: 0px 4px 9px #00000099; in: rise {y: 30, duration: 0.5, stagger: .03}) わずか5年で引退
tel#cl_t(left: 72px; top: 1230px; font-size: 72px; transform: rotate(-3deg)) おつかれさま、{a}お馬さん{/}
```

```timeline.txt
#v2
cast narrator = "明るくテンポのいい30代男性のナレーター、とぼけた味のある語り口で聞き手に語りかける" speed=112% manner="楽しそうに、軽快に"
cast ogai = "40代の男性、威厳のある明治の文士風の声、気難しく堅い話し方"
cast pass = "気さくな中年男性、江戸っ子風の早口でからっとした話し方"
transition = dissolve,300,overlap=300,zoom=1.04,ease=power2.out

*** open
[>#subtitle]
bgm music
se "山の峠の環境音、風と遠くの鳥の声" -8dB to=6s fade=300,1500
@narrator: [silence:+0.3s][>#op_y][>#op_d]1888年、9月5日。
@: 群馬と長野の境、[>#op_r]碓氷峠で、[>#op_t]とんでもない鉄道が[!#op_t punch]開業しました。

*** horse
se "馬の蹄の音とレールの軋む音" -8dB to=6s fade=300,1500
@narrator: [silence:+0.3s]その名も、[>#hs_n]碓氷馬車鉄道。
@: 急な山を越えるため、[>#hs_t]なんと馬が電車を[♪"馬のいななき" -3dB]引っ張るんです。
@: [>#hs_s]動力は、[!#hs_s punch]馬一頭。[silence:0.4s]
transition wipe,500,dir=left,overlap=500

*** ogai
se "古い木造の客車が軋む音" -8dB to=5s fade=300,1200
@narrator: [silence:+0.3s]この珍鉄道に乗り込んだのが、[>#og_c]文豪・森鴎外。
@ogai: [>#og_q]ふむ、[!#og_q pop]楽しみだ。

*** rage
se "ガタガタと激しく揺れる木の車輪の音" -8dB to=7s fade=200,1500
@narrator: [silence:+0.3s]ところが車内は、[>#rg_row.rg_k[1]]馬の臭いと、[>#rg_row.rg_k[2]]ガタガタの[!#rg_p shake][!#rg_v shake][!#rg_row.rg_k[1] shake][!#rg_row.rg_k[2] shake]大揺れ。
@ogai: [>#rg_t]臭いと揺れが、[!#rg_t{a} recolor,$a][>#rg_s][♪"打撃　パンチ03-1(ドライ)"]最悪だ!
@narrator: [!#rg_row.rg_k[*] tint,$a]文豪、大激怒です。

*** slow
se "のどかな山道の環境音、遠くの鳥" -8dB to=8s fade=300,1500
@narrator: [silence:+0.3s]しかも、[>#sl_t]とにかく遅い。
@: [>#sl_b]坂をのんびり登る馬の横を、[!#sl_b.h to,{x:110, duration:3.2, ease:'none'}][!#sl_b.w to,{x:420, duration:3.2, ease:'power1.inOut'}]歩く人が、すいすい追い越していきます。
@: [!#sl_b.w punch][!#sl_t{a} recolor,$a]歩きの勝ちです。

*** walk
@pass: [silence:+0.3s][>#wk_t]こりゃ、歩いた方が早いや!
@narrator: あまりの遅さに、[>#wk_i[*] {stagger:{each:0.18}}][♪"足音" -6dB to=2s]途中で降りて歩き出す乗客が、[>#wk_s][!#wk_s punch]続出したそうです。
[<#music -400]

*** down
bgm music2 -800
se "猛スピードで走る車輪の轟音と風切り音" -8dB to=8s fade=100,1500
@narrator: [silence:+0.3s][>#dn_k]ところが下り坂では、一転。
@: [>#dn_br]ブレーキが[!#dn_br{x} strike,$a][>#dn_ng]効かず、[♪"急ブレーキの金属が軋む音" -3dB]客車は猛スピードで駆け下ります。
@pass: [!#dn_p shake][!#dn_v shake][!#dn_k shake][!#dn_br shake][!#dn_ng shake]ひぃぃ、止まらなーい!
@narrator: [>#dn_t][♪"ジャン！・驚き" +3dB]まるでジェットコースター状態!
transition dissolve,300,overlap=300
[<#music2]

*** close
bgm music3 -1500
se "夕暮れの山の環境音、ひぐらしと風" -8dB to=10s fade=500,2000
@narrator: [silence:+0.4s]その5年後、[>#cl_y]アプト式の鉄道が開通し、[>#cl_n]馬車鉄道は、あっさり引退。
@: 9月5日は、[>#cl_t]馬が峠を越えた、ちょっと笑える記念日なのです。[silence:3.0s]
```

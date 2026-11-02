# concept · 麻辣湯の解説 (縦・章立て 13 cut・写真 + 板) — canvas 1080x1920・125.0s・視聴者 89.0 (Gemini・vs hf)

見せる文法: ×N・stack・manner・se・sticky・def・run・bgm 切替

```design.txt
#v2
# 計画: 民藝の色 — 生成りの地・唐辛子の赤 (主) + 花椒の緑 (副) + 山吹 (札)・墨の太い縁 + ずらした硬い影の板・写真は全面 + 幕
# 書体: 太い丸ゴシック (本文) + 極太の筆文字 (麻 / 辣 / 題だけ・数字なし) + 太い欧文 (英字の小見出し)
canvas 1080x1920 bg=#FBF4E8
theme light
palette a=#D7261E b=#2F7D4F ink=#2A1A14 paper=#FFF9EF mute=#7A6A5E gold=#F2B134 rt=#D7261E26 gt=#2F7D4F26
font "太い丸ゴシック体、親しみやすく元気な印象"
fonts h="極太の筆文字の毛筆体、力強い中華料理店の看板風" e="太い幾何学的なサンセリフの欧文、ポスター風"
photo_style "実写の料理写真、明るい自然光、立ちのぼる湯気、鮮やかな赤と緑、浅い被写界深度"
prompt_tail "文字なし、ロゴなし、看板の文字なし"
motion title { in: {scale:0.5, opacity:0, duration:0.45, ease:'back.out(2.0)'}; out: {scale:0.9, opacity:0, duration:0.2} }
motion big { in: {scale:0.4, opacity:0, duration:0.42, ease:'back.out(2.6)'}; out: {scale:0.8, opacity:0, duration:0.18} }
motion div { in: {scale:0.85, y:45, opacity:0, duration:0.45, ease:'back.out(1.8)'}; out: fade {duration:0.2} }
motion row { in: {x:-120, opacity:0, duration:0.38, ease:'back.out(1.4)'}; out: fade {duration:0.18} }
motion note { in: {y:30, opacity:0, duration:0.35, ease:'back.out(1.4)'}; out: fade {duration:0.18} }
cut { stagger: sentence }
div { in: div; border-radius: 33px; background: $paper; border: 4px solid $ink; box-shadow: 9px 9px 0px $ink }
run g { color: $gold }
run r { color: $a }
# 章の見出しの板: 番号つきの段 (赤い札) + 題
def head(n="", t="") = div(left: 54px; top: 84px; width: 972px; height: 225px; in: title)
  p#n(left: 36px; top: 30px; font-size: 36px; color: $paper; background: $a; border-radius: 148px; padding: 6px 24px; content: {n})
  p#t(left: 36px; top: 99px; font-size: 81px; color: $ink; content: {t})
# icon の地つきの行の札
def feat(i="fire", c=$a, d=$rt, t="", s="") = div(width: 972px; height: 270px)
  shape#bg(left: 36px; cy: 50%; width: 168px; height: 168px; path: rect,r=0.5; background: {d})
  icon#i(left: 69px; cy: 50%; font-size: 102px; name: {i}; color: {c})
  p#t(left: 240px; top: 60px; font-size: 60px; color: $ink; content: {t})
  p#s(left: 240px; top: 156px; font-size: 42px; color: $mute; content: {s})
subtitle.hug(font-size: 51px; bottom: 60px; background: $ink; color: $paper; border-radius: 21px; padding: 18px 39px; line-height: 1.35)
bgm#music 軽快でポップな中華風のビート、二胡と琵琶の旋律に手拍子、明るいグルメ解説向け
bgm#music2(volume: 1dB) 同じ中華風ポップでテンポを上げた高揚感のあるビート、太鼓と琵琶が重なる、流行を語る山場向け

section#hook
img#hk_p(inset: 0; main: kb {scale: [1, 1.08], focus: ['50% 50%', '50% 55%']}; scrim: 0.2) [photo]真上から見た湯気の立つ真っ赤な麻辣湯の丼、赤い唐辛子油、青菜、きのこ、春雨、木のテーブル
veil#hk_v(color: #2A1A14; opacity: 0.75; to: top; start: 0.55)
p#hk_k(left: 72px; top: 144px; font-size: 39px; font-family: e; color: $gold; letter-spacing: 0.25em) MALATANG
p#hk_t(left: 60px; top: 204px; font-size: 225px; font-family: h; color: $paper; text-shadow: 0px 6px 18px #00000080; in: zoom) 麻辣湯
p#hk_r(left: 72px; top: 477px; font-size: 51px; color: $paper) マーラータン
p#hk_s(left: 615px; top: 1155px; font-size: 45px; color: $ink; background: $gold; border-radius: 18px; padding: 12px 27px; border: 4px solid $ink; in: pop; transform: rotate(5deg)) 若者に行列
p#hk_q(left: 60px; top: 1290px; font-size: 69px; color: $paper; background: $a; border-radius: 24px; padding: 21px 36px; border: 4px solid $ink; box-shadow: 9px 9px 0px $ink; in: pop; transform: rotate(-3deg)) なぜ今、爆発的ヒット？

section#map
img#mp_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.6,#2A1A14) [photo]夜の街に赤い提灯が灯る麻辣湯の店先、店の前に並ぶ若者たち、ぼけた背景
p#mp_h(left: 60px; top: 120px; font-size: 78px; color: $paper; text-shadow: 0px 3px 12px #00000080) この動画でわかること
group#mp_col(left: 60px; top: 285px; width: 960px; height: 840px; display: flex; flex-direction: column; gap: 16px; out: fade {duration: .2})
  div#mp_l(flex: 1; in: div; box-shadow: 6px 6px 0px $ink) ×5
    p#n(left: 33px; cy: 50%; font-size: 48px; font-family: e; color: $a) 01;02;03;04;05
    p#t(left: 150px; cy: 50%; font-size: 54px; color: $ink) 中身;ルーツ;流行の理由;体への影響;具材の選び方

section#parts
img#pt_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.4) [photo]ステンレスのトレーにずらりと並んだ麻辣湯の具材、青菜、きのこ、豆腐、春雨、肉団子、明るい店内
head#pt_h(n: "01 構成要素"; t: "麻辣湯は4つでできる")
group#pt_grid(left: 60px; top: 375px; width: 960px; height: 900px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px)
  div#pt_c(in: div) ×4
    icon#i(cx: 50%; cy: 36%; font-size: 144px; name: "cooking-pot;pepper;carrot;bowl-food"; color: "$a;$a;$b;$b")
    p#t(cx: 50%; cy: 74%; font-size: 57px; color: $ink) スープ;麻辣タレ;具材;麺

section#soup
img#sp_p(inset: 0; main: kb {scale: [1, 1.08], focus: ['50% 60%', '']}; scrim: 0.3) [photo]大きな寸胴鍋で白く濁った豚骨と鶏ガラのスープがぐつぐつ煮立つ、立ちのぼる湯気、中華の厨房
head#sp_h(n: "01 スープ"; t: "濃厚な白いスープ")
div#sp_a(left: 60px; top: 930px; width: 960px; height: 195px)
  p#t(left: 42px; cy: 50%; font-size: 60px; color: $ink) 豚骨・鶏ガラの出汁
p#sp_x(left: 492px; top: 1140px; font-size: 108px; font-family: e; color: $a; text-shadow: 0px 3px 12px #00000080) +
div#sp_b(left: 60px; top: 1290px; width: 960px; height: 195px)
  p#t(left: 42px; cy: 50%; font-size: 60px; color: $ink) 白湯（パイタン）
#sp_b.on(background: $gold)

section#mala
img#ml_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.35) [photo]木の台に山盛りの真っ赤な乾燥唐辛子と、緑がかった花椒の実、横からの暖かい光
head#ml_h(n: "01 麻辣タレ"; t: "味の決め手")
div#ml_m(left: 60px; top: 435px; width: 450px; height: 690px)
  p#k(cx: 50%; top: 36px; font-size: 270px; font-family: h; color: $b) 麻
  p#r(cx: 50%; top: 348px; font-size: 45px; font-family: e; color: $b; letter-spacing: 0.2em) MA
  p#d(cx: 50%; top: 450px; font-size: 54px; text-align: center; line-height: 1.3; color: $ink) 花椒の[br]シビれ
div#ml_l(left: 570px; top: 435px; width: 450px; height: 690px)
  p#k(cx: 50%; top: 36px; font-size: 270px; font-family: h; color: $a) 辣
  p#r(cx: 50%; top: 348px; font-size: 45px; font-family: e; color: $a; letter-spacing: 0.2em) LA
  p#d(cx: 50%; top: 450px; font-size: 54px; text-align: center; line-height: 1.3; color: $ink) 唐辛子の[br]辛味

section#spice
img#sc_p(inset: 0; main: kb {scale: [1, 1.1], focus: ['50% 50%', '']}; scrim: 0.35) [photo]中華鍋の熱い油で八角、クローブ、シナモンスティック、草果、唐辛子を炒める、立ちのぼる香りの煙
head#sc_h(n: "01 薬膳・香辛料"; t: "香りの決め手")
p#sc_s(left: 570px; top: 705px; font-size: 54px; color: $paper; background: $a; border-radius: 18px; padding: 12px 30px; border: 4px solid $ink; box-shadow: 8px 8px 0px $ink; in: pop; transform: rotate(-4deg)) 数十種類！
group#sc_grid(left: 60px; top: 900px; width: 960px; height: 570px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px)
  div#sc_c(in: div; box-shadow: 6px 6px 0px $ink) ×4
    p#t(cx: 50%; cy: 38%; font-size: 66px; color: $ink) 八角;丁香;桂皮;草果
    p#s(cx: 50%; cy: 74%; font-size: 36px; color: $mute) スターアニス;クローブ;シナモン;ソウカ

section#roots
img#rt_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.4) [photo]中国四川省の夜の屋台、串に刺した具材を赤いスープの大鍋で煮る、湯気と裸電球、庶民的な雰囲気
head#rt_h(n: "02 歴史とルーツ"; t: "四川の屋台から")
div#rt_a(left: 60px; top: 405px; width: 960px; height: 255px)
  p#n(left: 36px; top: 33px; font-size: 36px; color: $paper; background: $b; border-radius: 148px; padding: 6px 21px) はじまり
  p#t(left: 36px; top: 123px; font-size: 60px; color: $ink) 四川省の屋台「麻辣燙」
shape#rt_x1(left: 495px; top: 678px; width: 90px; height: 75px; path: arrow_d; background: $gold; border: 4px solid $ink)
div#rt_b(left: 60px; top: 771px; width: 960px; height: 255px)
  p#n(left: 36px; top: 33px; font-size: 36px; color: $paper; background: $b; border-radius: 148px; padding: 6px 21px) 進化
  p#t(left: 36px; top: 123px; font-size: 57px; color: $ink) 選べるファストフード型
shape#rt_x2(left: 495px; top: 1044px; width: 90px; height: 75px; path: arrow_d; background: $gold; border: 4px solid $ink)
div#rt_c(left: 60px; top: 1137px; width: 960px; height: 255px)
  p#n(left: 36px; top: 33px; font-size: 36px; color: $paper; background: $a; border-radius: 148px; padding: 6px 21px) いま
  p#t(left: 36px; top: 123px; font-size: 60px; color: $ink) 日本でも大流行

section#trend
img#tr_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.4) [photo]明るい店内で真っ赤な麻辣湯の丼をスマートフォンで撮影する若い女性の手元、背景はぼけた店内
head#tr_h(n: "03 流行の背景"; t: "ヒットの3つの理由")
group#tr_col(left: 54px; top: 375px; height: 990px; display: flex; flex-direction: column; gap: 20px)
  feat#tr_c(flex: 1; in: div; i: "camera;sliders-horizontal;heartbeat"; c: "$a;$a;$b"; d: "$rt;$rt;$gt"; t: "SNS映え;カスタマイズ性;健康・ダイエット"; s: "真っ赤な見た目;具材も辛さも自由;野菜たっぷり") ×3

section#merit
img#me_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.35) [photo]湯気の立つ赤いスープをれんげですくう手元、温かい光、木のテーブル
head#me_h(n: "04 身体への影響"; t: "うれしい効果")
feat#me_a(left: 54px; top: 840px; i: fire; t: "カプサイシン"; s: "体を温め、代謝を助ける")
feat#me_b(left: 54px; top: 1155px; i: leaf; c: $b; d: $gt; t: "薬膳スパイス"; s: "香りで食欲を後押し")

section#caution
img#ca_p(inset: 0; main: kb {scale: [1, 1.1], focus: ['50% 50%', '']}; scrim: 0.4) [photo]赤い唐辛子油が厚く浮いた麻辣湯のスープの寄り、表面の油の輝き
head#ca_h(n: "04 注意点"; t: "ただし注意も")
p#ca_s(left: 150px; top: 450px; font-size: 66px; color: $paper; background: $a; border-radius: 21px; padding: 18px 39px; border: 4px solid $ink; box-shadow: 9px 9px 0px $ink; in: pop; transform: rotate(-4deg)) スープは飲み干さない
feat#ca_a(left: 54px; top: 840px; i: drop; t: "塩分が多め"; s: "スープに溶け込んでいる")
feat#ca_b(left: 54px; top: 1155px; i: drop-half; t: "脂質が多め"; s: "表面の赤い油")

section#choose
img#ch_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.4) [photo]麻辣湯店の冷蔵ショーケースに並ぶ色とりどりの具材、葉物野菜、きのこ、肉団子、練り物、トングとボウル
head#ch_h(n: "05 具材選び"; t: "お店の形式で変わる")
div#ch_g(left: 60px; top: 780px; width: 960px; height: 375px)
  p#tag(left: 36px; top: 33px; font-size: 39px; color: $paper; background: $a; border-radius: 148px; padding: 6px 24px) グラム売り
  p#ok(left: 36px; top: 138px; font-size: 54px; color: $ink) 軽くてお得：葉物・きのこ
  p#ng(left: 36px; top: 243px; font-size: 54px; color: $ink) 重め：肉団子・練り物
div#ch_t(left: 60px; top: 1200px; width: 960px; height: 270px)
  p#tag(left: 36px; top: 33px; font-size: 39px; color: $paper; background: $b; border-radius: 148px; padding: 6px 24px) トッピング形式
  p#ok(left: 36px; top: 141px; font-size: 54px; color: $ink) たんぱく質を1品足す

section#order
img#or_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.3) [photo]青菜ときのこがたっぷり、豆腐と鶏肉、春雨が入った赤い麻辣湯の一杯を真上から、木のテーブル
head#or_h(n: "おすすめ"; t: "注文の組み立て例")
p#or_s(left: 570px; top: 375px; font-size: 48px; color: $ink; background: $gold; border-radius: 18px; padding: 12px 27px; border: 4px solid $ink; in: pop; transform: rotate(5deg)) 辛さは控えめから
group#or_col(left: 60px; top: 870px; width: 960px; height: 600px; display: flex; flex-direction: column; gap: 16px)
  div#or_c(flex: 1; in: div; box-shadow: 6px 6px 0px $ink) ×3
    p#n(left: 36px; cy: 50%; font-size: 39px; color: $paper; background: $b; border-radius: 148px; padding: 6px 21px) 野菜;たんぱく質;麺
    p#t(left: 315px; cy: 50%; font-size: 51px; color: $ink) 青菜ときのこたっぷり;豆腐か鶏肉を1品;春雨

section#outro
img#ou_p(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '']}; scrim: 0.25) [photo]夜の明るい麻辣湯の店で、湯気の立つ赤い丼を囲んで笑う若者たち、温かい光
veil#ou_v(color: #2A1A14; opacity: 0.75; to: top; start: 0.6)
p#ou_t(left: 60px; top: 165px; font-size: 96px; color: $paper; line-height: 1.25; text-shadow: 0px 3px 12px #00000080) あなただけの[br]{g}一杯{/}を組もう
p#ou_s(left: 66px; top: 450px; font-size: 45px; color: $paper) 仕組みを知れば、もっとおいしい
group#ou_row(left: 60px; top: 1245px; width: 960px; height: 180px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px)
  div#ou_c(in: div; box-shadow: 6px 6px 0px $ink) ×3
    p#t(cx: 50%; cy: 50%; font-size: 45px; color: $ink) 薬膳スープ;自由に組む;スープは残す
```

```timeline.txt
#v2
cast narrator = "明るく親しみのある20代後半女性のナレーター、テンポよく語りかける解説口調" speed=110%
transition = dissolve {duration: .3, overlap: .3, zoom: 1.04, ease: 'power2.out'}

*** hook
[>#subtitle]
bgm music
se "鍋のスープがぐつぐつ煮立つ音" -8dB to=10s fade=300ms,1500ms
@narrator: [silence:+0.3s][>#hk_k]今、[>#hk_s]若者の行列が絶えない一杯があります。
@: 真っ赤なスープの、[>#hk_t][>#hk_r >][♪"ジャン！・驚き" +3dB]麻辣湯。
@: なぜ今、ここまで[>#hk_q]爆発的にヒットしているのでしょうか？[silence:0.4s]

*** map
se "夜の繁華街のにぎやかなざわめき" -8dB to=9s fade=300ms,1500ms
@narrator: [silence:+0.3s]この動画では、[>#mp_col.mp_l[1]]中身、[>#mp_col.mp_l[2]]ルーツ、[>#mp_col.mp_l[3]]流行の理由、[>#mp_col.mp_l[4]]体への影響、[>#mp_col.mp_l[5]]そして具材の選び方まで、まるごと解説します。
transition wipe {duration: .6, dir: 'right', overlap: .6}

*** parts
@narrator: [silence:+0.3s]麻辣湯のベースは、[>#pt_grid.pt_c[1]]スープ、[>#pt_grid.pt_c[2]]麻辣タレ、[>#pt_grid.pt_c[3]]具材、[>#pt_grid.pt_c[4]]麺の、
@: [!#pt_grid.pt_c[*] punch]4つの要素で成り立っています。

*** soup
se "大きな寸胴鍋がぐつぐつ煮える音" -8dB to=9s fade=300ms,1500ms
@narrator: [silence:+0.3s]スープは、[>#sp_a]豚骨や鶏ガラをベースにした濃厚な出汁に、
@: [>#sp_x][>#sp_b >][!#sp_b .on +900ms]白湯、パイタン状のスープを加えることが多いんです。

*** mala
@narrator: [silence:+0.3s]味の決め手は麻辣タレ。
@: [>#ml_m][!#ml_m punch +200ms]麻は、花椒によるシビれ。
@: [>#ml_l][!#ml_l punch +200ms]辣は、唐辛子による辛味です。

*** spice
se "中華鍋で油とスパイスをジュージュー炒める音" -8dB to=10s fade=300ms,1500ms
@narrator: [silence:+0.3s]さらに[>#sc_grid.sc_c[1]]八角、[>#sc_grid.sc_c[2]]丁香、[>#sc_grid.sc_c[3]]桂皮、[>#sc_grid.sc_c[4]]草果など、
@: [>#sc_s]数十種類の生薬やスパイスを油で炒めて、香りを引き出します。
transition wipe {duration: .6, dir: 'right', overlap: .6}

*** roots
se "夜の屋台のにぎわい、遠くの話し声" -8dB to=14s fade=300ms,1500ms
@narrator: [silence:+0.3s]ルーツは中国・四川省の屋台料理、[>#rt_a]麻辣燙。
@: [!#rt_a punch]串に刺した具を鍋で煮て食べる、庶民の味でした。
@: それが、[>#rt_x1][>#rt_b >]具材を選んで一杯にするファストフード型へと進化し、
@: [>#rt_x2][>#rt_c >][!#rt_c fill,$gold +900ms]日本にも広がりました。[silence:0.8s]
transition wipe {duration: .6, dir: 'right', overlap: .6}
[<#music]

*** trend
bgm music2 -1500ms
@narrator: [silence:+0.3s]流行の理由は3つ。
@: [>#tr_col.tr_c[1]][♪"カメラのシャッター音" -2dB]真っ赤な見た目が[!#tr_col.tr_c[1] check]SNS映えすること。
@: [>#tr_col.tr_c[2]]具材も辛さも[!#tr_col.tr_c[2] check]自分好みにカスタマイズできること。
@: [>#tr_col.tr_c[3]]そして野菜たっぷりで、[!#tr_col.tr_c[3] check]健康・ダイエット需要に合うことです。
transition wipe {duration: .6, dir: 'right', overlap: .6}

*** merit
@narrator: [silence:+0.3s]体へのうれしい点も。
@: [>#me_a]唐辛子のカプサイシンは[>#me_a.s]体を温め、[!#me_a.s recolor,$a]代謝を助けると言われます。
@: [>#me_b]薬膳スパイスの香りは、食欲を後押ししてくれます。

*** caution
@narrator: [silence:+0.3s]ただし注意点も。
@: スープは[>#ca_a]塩分と[>#ca_b]脂質が多めです。
@: [>#ca_s][♪"判子を押す"]飲み干さずに、少し残すのがおすすめです。
transition wipe {duration: .6, dir: 'right', overlap: .6}

*** choose
se "店内のにぎやかな環境音、トングが触れる音" -8dB to=14s fade=300ms,1500ms
@narrator: [silence:+0.3s]具材選びは、お店の形式で変わります。
@: [>#ch_g]グラム売りなら、[>#ch_g.ok][!#ch_g.ok recolor,$b +500ms]葉物やきのこは軽くてお得、[>#ch_g.ng][!#ch_g.ng recolor,$a +500ms]肉団子や練り物は重めです。
@: [>#ch_t]トッピング形式なら、[>#ch_t.ok][!#ch_t.ok recolor,$b +500ms]たんぱく質を一品足すのが賢い選び方。

*** order
@narrator: [silence:+0.3s]おすすめは、[>#or_col.or_c[1]]青菜ときのこをたっぷり、[>#or_col.or_c[2]]豆腐か鶏肉を一品、[>#or_col.or_c[3]]麺は春雨。
@: [>#or_s]辛さは控えめから試してみてください。
transition dissolve {duration: .3, overlap: .3}

*** outro
se "にぎやかな店内の笑い声と食器の音" -9dB to=10s fade=300ms,2000ms
@narrator: [silence:+0.3s][>#ou_t]仕組みを知れば、[>#ou_s +600ms]麻辣湯はもっと楽しくなります。
@: [>#ou_row.ou_c[*] {stagger:{each:0.15}}]あなただけの一杯を、組んでみてください。[silence:2.0s]
```

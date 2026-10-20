# story · 夏フェスのオタク語り (縦・構文風の一人語り) — canvas 720x1280・44.5s・視聴者 84.5 (Gemini・vs hf)

見せる文法: count・×N・stack・manner・se・sticky・def・run・bgm 切替

```design.txt
#v2
# 計画: 大型の文字の組 — 夜の黒紫の地・青〜赤のネオンの勾配の幕を全 cut の絵に掛ける・主色 ネオンの赤 (a)・差し色 シアン (b)
# 書体 極太の角ゴシック (見出し・叫び) + 太い幾何学的な欧文 (時刻・数字・英字)・字幕は画面中央に大きく短い句で
# 画面は 3 段: 上 = 見出しと大きな数字 / 中央 = 字幕 / 下 = 札と一覧。人物は出さない (物と会場と光だけ)
canvas 720x1280 bg=#0A0614
theme dark
palette a=#FF2E63 b=#2EE8FF ink=#F6F2FF paper=#FFF5FA mute=#B7B0DE deep=#0A0614 card=#160B30E6
font "極太の角ゴシック体、力強くポスター風の印象"
fonts e="太い幾何学的なサンセリフの欧文、ポスター風、数字がくっきり"
photo_style "夜の野外音楽フェスの実写、青と赤のネオンの強い光、高いコントラスト、スモークと光の筋、浅い被写界深度"
prompt_tail "文字なし、ロゴなし、人物なし"
motion title = in=scale=0.5,opacity=0,duration=450 ease=back(2.0) out=scale=0.9,opacity=0,duration=200
motion big = in=scale=0.4,opacity=0,duration=420 ease=back(2.6) out=scale=0.8,opacity=0,duration=180
motion div = in=scale=0.85,y=30,opacity=0,duration=450 ease=back(1.8) out=fade,200
motion row = in=x=-80,opacity=0,duration=380 ease=back(1.4) out=fade,180
motion note = in=y=20,opacity=0,duration=350 ease=back(1.4) out=fade,180
div { in: div; background: $card; border: 2px solid $b; border-radius: 18px; box-shadow: 0px 0px 24px #2EE8FF55 }
img { scrim: 0.35 }
cut { stagger: sentence }
run r = color=$a
run c = color=$b
run u = size=72 color=$a
# 全 cut の絵に掛ける青〜赤のネオン勾配の幕
def neon = veil(background: linear(#1F2BFF99,#0A061420@50%,#FF1E5A99,160))
# 文字の段 30 / 60 / 96 / 160
def kick(t) = p(font-size: 28px; font-family: e; color: $b; letter-spacing: 0.2em; in: note; content: {t})
def h1(t) = p(font-size: 64px; line-height: 1.12; color: $ink; text-shadow: 0px 0px 18px #FF2E63AA; in: title; content: {t})
def big(t) = p(font-size: 96px; color: $ink; in: big; content: {t})
subtitle.hug(font-size: 52px; top: 600px; width: 660px; unit: phrase; strip: 、。; background: #0A0614E0; color: $ink; border-radius: 14px; padding: 10px 24px; border: 3px solid $a; line-height: 1.25)
bgm#music(volume: 4dB) 疾走感のあるアップテンポのロック、歪んだエレキギターと速いドラム、夏フェスの高揚感
bgm#music2(volume: 4dB) さらに激しく高揚する疾走感のあるロック、シンガロングの大合唱が入るクライマックス、夏フェスのヘッドライナー
sfx off

section#hook
img#hk_p(inset: 0; main: kb {scale: [1, 1.08], focus: '50% 60%'}) 真夜中の暗い部屋、ベッドの上で光るスマートフォンの画面、青と赤のネオンの反射
neon#hk_v
shape#hk_ring(left: 380px; top: 70px; width: 300px; height: 300px; path: circle; background: none; border: 3px solid $b; opacity: 0.35; main: pulse)
kick#hk_k(left: 40px; top: 88px) DEEP NIGHT
p#hk_t(left: 36px; top: 124px; font-size: 170px; font-family: e; color: $ink; text-shadow: 0px 0px 24px #2EE8FFAA; in: big) 0:00
div#hk_n(left: 40px; top: 800px; width: 640px; height: 170px)
  icon#i(left: 26px; top: 26px; font-size: 34px; name: bell-ringing; weight: fill; color: $b)
  p#app(left: 72px; top: 30px; font-size: 24px; font-family: e; color: $b) FES 2026
  p#title(left: 26px; top: 74px; font-size: 34px; color: $ink) 新着のお知らせ
  p#body(left: 26px; top: 120px; font-size: 26px; color: $mute) 重要なお知らせが1件あります
p#hk_q(right: 40px; top: 1020px; font-size: 110px; color: $a; text-shadow: 0px 0px 22px #FF2E63CC; in: pop; transform: rotate(-6deg)) は？

section#clash
img#cs_p(inset: 0; main: kb {scale: [1.06, 1], focus: '50% 50%'}) 夜の野外フェス会場を高い所から見下ろす、遠く離れた2つのステージがネオンに光る、広い芝生
neon#cs_v
h1#cs_h(left: 40px; top: 90px) 推しAと推しB[br]{r}まさかの同時刻{/}
div#cs_c(in: {stagger: {each: 0.15}}; left: 40px; top: 780px; width: 640px; height: 210px; gap: 24; padding: 0px; display: flex) ×2
  p#s(left: 24px; top: 20px; font-size: 26px; font-family: e; color: $b; letter-spacing: 0.15em) MAIN STAGE;SUB STAGE
  p#t(left: 24px; top: 58px; font-size: 72px; font-family: e; color: $ink) 18:30;18:30
  p#n(left: 24px; bottom: 18px; font-size: 32px; color: $mute) 推しA;推しB
shape#cs_l(left: 40px; top: 1030px; width: 640px; height: 4px; path: line_h; background: $a; border: 3px solid $a; in: wipe {dir: 'right', duration: 0.6})
p#cs_s(right: 40px; top: 1060px; font-size: 48px; font-family: e; color: $paper; background: $a; border-radius: 12px; padding: 8px 22px; in: pop; transform: rotate(-4deg)) ⇄ 20 MIN

section#heat
img#ht_p(inset: 0; main: kb {scale: [1, 1.07], focus: '60% 30%'}) 真夏の昼の野外フェス会場、照りつける太陽と強いレンズフレア、陽炎のゆらぐ芝生とステージ、空は青から赤へ
neon#ht_v
shape#ht_sun(left: 330px; top: 50px; width: 360px; height: 360px; path: sunburst,n=16; background: #FF2E6326; border: none; main: spin {period: 40})
p#ht_n(right: 40px; top: 70px; font-size: 210px; font-family: e; color: $ink; text-align: right; text-shadow: 0px 0px 26px #FF2E63CC; in: big) [count:36]{u}℃{/}
p#ht_l(right: 44px; top: 320px; font-size: 32px; color: $mute; text-align: right; in: note) 当日の最高気温
div#ht_r(in: {stagger: {each: 0.15}}; left: 40px; top: 780px; width: 640px; height: 250px; gap: 18; padding: 0px; display: flex; flex-direction: column) ×2
  icon#i(left: 24px; cy: 50%; font-size: 48px; name: "drop;t-shirt"; color: "$b;$a")
  p#t(left: 96px; cy: 50%; font-size: 38px; color: $ink) 日焼け止め、汗で消滅;タオル、絞れる
p#ht_s(right: 40px; top: 1060px; font-size: 48px; color: $deep; background: $b; border-radius: 12px; padding: 8px 22px; in: pop; transform: rotate(4deg)) 最前死守

section#climax
img#cx_p(inset: 0; main: kb {scale: [1, 1.1], focus: '50% 40%'}) 夜の野外フェスのメインステージ、強烈な赤と青のサーチライトとスモーク、宙を舞う紙吹雪、観客なし
neon#cx_v
h1#cx_h(left: 40px; top: 90px) イントロ一音目で[br]全部、飛んだ
p#cx_w(left: 40px; top: 260px; font-size: 128px; color: $a; text-shadow: 0px 0px 30px #FF2E63; in: punch; transform: rotate(-5deg)) 完全勝利
div#cx_r(in: {stagger: {each: 0.12}}; left: 40px; top: 790px; width: 640px; height: 200px; gap: 18; padding: 0px; display: flex) ×3
  p#l(cx: 50%; top: 24px; font-size: 30px; color: $mute) 体力;声;足
  p#v(cx: 50%; bottom: 30px; font-size: 52px; color: $ink) ゼロ;ガラガラ;棒
confetti#cx_cf
veil#cx_fl(color: #FFFFFF; opacity: 0.6; z: curtain; in: none)

section#phil
img#ph_p(inset: 0; main: kb {scale: [1.08, 1], focus: '40% 50%'}) 暗い部屋の机の上に置かれたヘッドホンとスマートフォン、窓の外に遠く光るフェスのネオン
neon#ph_v
kick#ph_k(left: 40px; top: 88px) THEORY
p#ph_a(left: 40px; top: 130px; font-size: 60px; color: $mute; in: title) 音源を聴くこと
p#ph_ne(left: 40px; top: 210px; font-size: 130px; font-family: e; color: $a; text-shadow: 0px 0px 24px #FF2E63CC; in: pop) ≠
p#ph_b(left: 40px; top: 370px; font-size: 60px; color: $ink; in: title) 現場で{c}浴びる{/}こと
p#ph_s(left: 40px; top: 820px; width: 640px; font-size: 100px; text-align: center; color: $paper; background: $a; border-radius: 16px; padding: 12px 20px; box-shadow: 0px 0px 30px #FF2E63AA; in: punch; transform: rotate(-3deg)) 全くの別物

section#close
img#ed_p(inset: 0; main: kb {scale: [1, 1.06], focus: '50% 35%'}) 夜の野外フェス会場の上に上がる大きな花火、青と赤の光、静かになった芝生、遠景
neon#ed_v
kick#ed_k(left: 40px; top: 88px) NEXT TIMETABLE
p#ed_l(left: 40px; top: 130px; font-size: 34px; color: $mute; in: note) 来年のタイテ解禁まで、あと
p#ed_d(left: 36px; top: 170px; font-size: 180px; font-family: e; color: $ink; text-shadow: 0px 0px 24px #2EE8FFAA; in: big) [count:300]{u}日{/}
p#ed_f(left: 40px; top: 820px; width: 640px; font-size: 118px; text-align: center; color: $ink; text-shadow: 0px 0px 30px #FF2E63; in: punch) 震えて待て。
```

```timeline.txt
#v2
cast n = "早口でテンポのいい20代男性、熱量の高いオタクの一人語り、畳み掛けるように話す" speed=125% manner="早口で畳み掛ける、少し大げさに"
transition = push,300,dir=left

*** hook
[>#subtitle]
bgm music
@n: [silence:+0.3s]深夜、[!#hk_t recolor,$b]0時。[>#hk_n][♪"スマートフォン UIサウンド01-09（スピーカー）" -2dB]スマホが[!#hk_n shake]震えた。震える指でアプリを開く。
@: [!#hk_n.title text,"タイムテーブル解禁"][!#hk_n.body text,"全ステージの出演時刻を公開"]タイテ解禁。[silence:0.3s][>#hk_q][♪"ジャン！・驚き" +3dB][!#hk_p shake][!#hk_v shake][!#hk_ring shake][!#hk_k shake][!#hk_t shake][!#hk_n shake][!#hk_q shake]……は？[silence:0.8s]

*** clash
@n: [silence:+0.2s][>#cs_c[*] {stagger:{each:0.15}}]推しAと推しB、まさかの[!#cs_c[*] punch]同時刻。
@: [>#cs_l]メインからサブまで、[>#cs_s]徒歩20分。[♪"クイズ　ブザー02-2(短)"][!#cs_s shake]物理的に無理。
@: [!#cs_c[2] dim]分身の術を習得していない自分を呪った。[silence:0.4s]

*** heat
se "真夏の野外の蝉の声と熱気、遠くのサウンドチェックの音" -8dB to=9s fade=300,1500
@n: [silence:+0.2s]そして当日、[>#ht_n count]気温36度。
@: [>#ht_r[1]]日焼け止めは汗で流れ、[>#ht_r[2]]タオルは絞れる。
@: それでも、[>#ht_s][!#ht_s punch]最前は譲らない。[silence:0.6s]
[<#music -400]

*** climax
bgm music2
se "野外フェスの大歓声とライブの轟音" -8dB to=10s fade=200,1500
@n: [silence:+0.2s]イントロの一音目で、[>#cx_fl][!#cx_fl to,{opacity:0, duration:.4}]全部飛んだ。
@: [>#cx_r[1]]体力ゼロ、[>#cx_r[2]]声ガラガラ、[>#cx_r[3]]足は棒。
@: [!#cx_r[*] dim]でも、[>#cx_w][>#cx_cf][♪"オノマトペ 衝撃13-2（長）" +3dB to=2.5s fade=0,800]完全勝利。俺たちが、[!#cx_w pulse]夏そのものだった。[silence:0.6s]
transition wipe,500,dir=left

*** phil
@n: [silence:+0.3s]いいか、よく聞け。
@: [>#ph_a]音源を聴くことと、[>#ph_ne][>#ph_b]現場で[!#ph_b{c} recolor,$a]浴びることは、
@: [>#ph_s][♪"打撃　パンチ03-1(ドライ)"][♪"打撃　パンチ03-4(ディレイ)" -4dB +160]全くの別物である。[silence:0.5s]
transition dissolve,300,overlap=300

*** close
se "夜の野外会場を抜ける風と遠くの花火の音" -8dB to=8s fade=300,2000
@n: [silence:+0.3s]次回、[>#ed_l]来年のタイテ解禁まで、[>#ed_d count]あと300日。[silence:0.5s]
@: [>#ed_f][♪"オノマトペ 衝撃13-2（長）" +3dB to=2.5s fade=0,800][!#ed_f shake]震えて待て。[silence:2.0s]
```

# concept · 和風きのこパスタ (縦・手順 + コツ) — canvas 720x1280・72.3s・視聴者 90.0 (Gemini・vs hf)

見せる文法: ×N・stack・manner・se・sticky・def・run・bgm 切替

```design.txt
#v2
# 計画: 民藝の色 (食・暮らし) — 生成りの紙の地・主色 朱 (醤油と火)・差し色 ねぎの緑 / バターの黄・墨の縁 + ずらした硬い影
# 絵は全面の料理写真 (上 6 割に主役)・下に手順の札 (番号 + 一文)・字幕は墨の札。書体 太い丸ゴシック (本文) + 筆の見出し (題だけ・数字は本文の書体)
canvas 720x1280 bg=#FBF5EA
theme light
palette a=#C8452C b=#3E7A3A c=#E8A820 ink=#2B2118 paper=#FFFBF2 mute=#6E5E4C cream=#FBF5EA
font "太い丸ゴシック体、やさしい印象"
fonts f="太い筆文字の毛筆体、和風の見出し" e="極太の丸ゴシック体、数字が力強い"
photo_style "実写の料理写真、自然光、木のテーブル、温かい色調、浅い被写界深度、和の器"
prompt_tail "文字なし、ロゴなし、手元だけで顔は映さない"
motion title = in=scale=0.5,opacity=0,duration=450 ease=back(2.0) out=scale=0.9,opacity=0,duration=200
motion big = in=scale=0.4,opacity=0,duration=420 ease=back(2.6) out=scale=0.8,opacity=0,duration=180
motion div = in=scale=0.85,y=30,opacity=0,duration=450 ease=back(1.8) out=fade,200
motion row = in=x=-80,opacity=0,duration=380 ease=back(1.4) out=fade,180
motion note = in=y=20,opacity=0,duration=350 ease=back(1.4) out=fade,180
div { in: div; border-radius: 24px; border: 3px solid $ink; box-shadow: 6px 6px 0px $ink; background: $paper }
img { scrim: vignette,0.25 }
cut { stagger: sentence }
run r = color=$a
run g = color=$b
run m = marker=$c
image dish = "[photo]和風きのこパスタ、しめじとえのきとバター醤油のスパゲッティ、上に刻みのりと青ねぎ、和食器の深皿、木のテーブル、真上より少し斜め"
def num(t) = p(font-size: 72px; font-family: e; color: $a; in: big; content: {t})
def ttl(t) = p(font-size: 40px; color: $ink; line-height: 1.25; in: row; content: {t})
def chip(t) = p(font-size: 30px; color: $paper; background: $a; border-radius: 99px; padding: 6px 20px; border: 3px solid $ink; in: pop; content: {t})
subtitle.hug(font-size: 32px; bottom: 48px; background: #2B2118E8; color: #FFFBF2; border-radius: 14px; padding: 10px 24px; line-height: 1.35)
bgm#music 軽やかなアコースティックギターと木琴の明るいBGM、和やかな料理動画向け、ほのぼの
bgm#music2(volume: 1dB) 同じ系統で少し弾むアコースティックポップ、手拍子とウクレレ、料理の仕上げ向け

section#open
img#op_p(inset: 0; main: kb,1.0@50%,40%>1.08@50%,38%) [ref:@dish]湯気の立つ和風きのこパスタ、真上より少し斜め、皿は画面の上半分に大きく
veil#op_v(color: #FBF5EA; opacity: 0.92; to: bottom; start: 0.5)
p#op_k(left: 40px; top: 72px; font-size: 30px; color: $paper; background: $a; border-radius: 99px; padding: 6px 22px; border: 3px solid $ink; in: pop) 調理 10分
p#op_t(left: 40px; top: 760px; width: 640px; font-size: 84px; font-family: f; color: $ink; line-height: 1.15; in: title) 和風[br]きのこパスタ
shape#op_r(left: 40px; top: 980px; width: 300px; height: 6px; path: line_h; background: $a; border: 6px solid $a; in: wipe,right,600)
p#op_s(left: 40px; top: 1006px; font-size: 34px; color: $mute; in: note) しめじ × えのき × バター醤油
p#op_n(right: 40px; top: 72px; font-size: 30px; color: $ink; background: $paper; border: 3px solid $ink; border-radius: 99px; padding: 6px 22px; in: pop; transform: rotate(6deg)) 2人分

section#ing
img#ig_p(inset: 0; main: kb,1.06@50%,50%>1.0) [photo]木のテーブルの上に並べたパスタの材料を真上から、乾麺のスパゲッティ、しめじ、えのき、バター、醤油の小瓶、にんにく、刻みのり、青ねぎ
veil#ig_v(color: #2B2118; opacity: 0.35)
p#ig_h(left: 40px; top: 64px; font-size: 40px; color: $paper; background: $a; border-radius: 99px; padding: 8px 24px; border: 3px solid $ink; in: pop) 材料（2人分）
div#ig_c(left: 40px; top: 150px; width: 640px; height: 860px; padding: 0px)
p#ig_i(left: 72px; top: 180px; width: 576px; height: 800px; overlap: ig_c; gap: 14; font-size: 36px; color: $ink; in: {x:-24, opacity:0, duration:0.4, ease:'power3.out'}; display: flex; flex-direction: column) ×7 スパゲッティ　200g;しめじ　1パック;えのき　1/2袋;バター　20g;醤油　大さじ1.5;にんにく　1片;刻みのり・青ねぎ　適量

section#s1
img#s1_p(inset: 0; main: kb,1.0@50%,35%>1.07@50%,30%) [photo]大きな鍋で沸騰した湯の中にスパゲッティを放射状に入れる手元、湯気、ガスの火
num#s1_n(left: 40px; top: 64px) 01
div#s1_c(left: 32px; top: 760px; width: 656px; height: 250px; padding: 0px)
  ttl#t1(left: 32px; top: 28px; right: 32px) 塩を入れた湯で茹でる
  ttl#t2(left: 32px; top: 84px; right: 32px) 袋の表示より{m}1分短く{/}
  p#q(left: 32px; bottom: 28px; font-size: 28px; color: $mute) あとでフライパンで仕上げるから
p#s1_st(left: 470px; top: 640px; font-size: 48px; font-family: e; color: $paper; background: $a; border-radius: 20px; padding: 10px 24px; border: 4px solid $ink; box-shadow: 6px 6px 0px $ink; in: pop; transform: rotate(-8deg)) −1分

section#s2
img#s2_p(inset: 0; main: kb,1.08@50%,40%>1.0) [photo]鉄のフライパンでバターが溶けて刻んだにんにくが泡立ち、しめじとえのきを炒めている手元、木べら、湯気
num#s2_n(left: 40px; top: 64px) 02
p#s2_h(right: 40px; top: 80px; font-size: 40px; color: $paper; background: $b; border-radius: 99px; padding: 8px 26px; border: 3px solid $ink; in: pop) 弱火
#s2_h.hot(background: $a) 強火
div#s2_c(left: 32px; top: 760px; width: 656px; height: 250px; padding: 0px)
  ttl#t1(left: 32px; top: 28px; right: 32px) バター＋にんにくで香り
  ttl#t2(left: 32px; top: 84px; right: 32px) きのこを{r}強火{/}で炒める
  p#q(left: 32px; bottom: 28px; font-size: 28px; color: $mute) バター 20g・にんにく 1片

section#tip
img#tp_p(inset: 0; main: kb,1.0@50%,45%>1.12@50%,45%) [photo]フライパンの中で焼き色が付いたしめじとえのきのクローズアップ、こんがりときつね色、湯気
veil#tp_v(color: #2B2118; opacity: 0.75; to: bottom; start: 0.45)
p#tp_k(left: 40px; top: 72px; font-size: 34px; color: $ink; background: $c; border-radius: 99px; padding: 6px 22px; border: 3px solid $ink; in: pop) コツ
p#tp_t(left: 40px; top: 760px; width: 640px; font-size: 60px; font-family: f; color: $paper; line-height: 1.25; in: title) 触らずに[br]焼き付ける
p#tp_s(left: 40px; top: 940px; font-size: 36px; color: $paper; in: note) 1分待てば、{m}香ばしさ{/}が段違い
p#tp_st(left: 440px; top: 620px; font-size: 44px; color: $ink; background: $c; border-radius: 20px; padding: 10px 22px; border: 4px solid $ink; box-shadow: 6px 6px 0px $ink; in: pop; transform: rotate(-6deg)) こんがり

section#s3
img#s3_p(inset: 0; main: kb,1.0@50%,40%>1.07@50%,35%) [photo]フライパンのきのこにお玉でパスタの茹で汁を注ぎ、醤油を回しかける手元、湯気が立つ
num#s3_n(left: 40px; top: 64px) 03
div#s3_c(left: 32px; top: 760px; width: 656px; height: 250px; padding: 0px)
  ttl#t1(left: 32px; top: 28px; right: 32px) 茹で汁＋醤油を回しかけ
  ttl#t2(left: 32px; top: 84px; right: 32px) よく混ぜて{m}乳化{/}させる
  p#q(left: 32px; bottom: 28px; font-size: 28px; color: $mute) 醤油 大さじ1.5 を回しかける
p#s3_a(left: 40px; top: 650px; font-size: 34px; color: $ink; background: $paper; border: 3px solid $ink; border-radius: 99px; padding: 6px 20px; in: pop) お玉1杯
p#s3_b(left: 260px; top: 650px; font-size: 34px; color: $paper; background: $a; border: 3px solid $ink; border-radius: 99px; padding: 6px 20px; in: pop) 大さじ1.5

section#s4
img#s4_p(inset: 0; main: kb,1.06@50%,40%>1.0) [photo]フライパンでスパゲッティときのこをトングで和えている手元、ソースが絡んでつやつや、湯気
num#s4_n(left: 40px; top: 64px) 04
div#s4_c(left: 32px; top: 760px; width: 656px; height: 250px; padding: 0px)
  ttl#t1(left: 32px; top: 28px; right: 32px) パスタを和える
  ttl#t2(left: 32px; top: 84px; right: 32px) のりと青ねぎをのせる
  p#q(left: 32px; bottom: 28px; font-size: 28px; color: $mute) さっと和えたら火を止める
chip#s4_a(left: 40px; top: 650px) 刻みのり
#s4_a.done(background: $ink)
chip#s4_b(left: 250px; top: 650px) 青ねぎ
#s4_b.done(background: $b)

section#close
img#cl_p(inset: 0; main: kb,1.0@50%,40%>1.06@50%,42%) [ref:@dish]食卓に置かれた二皿の和風きのこパスタとお箸、夕方の温かい灯り、湯気
veil#cl_v(color: #FBF5EA; opacity: 0.92; to: bottom; start: 0.5)
p#cl_t(left: 40px; top: 770px; width: 640px; font-size: 72px; font-family: f; color: $ink; line-height: 1.2; in: title) 今日の晩ごはんに[br]どうぞ
p#cl_a(left: 40px; top: 990px; font-size: 30px; color: $paper; background: $a; border-radius: 99px; padding: 6px 20px; border: 3px solid $ink; in: pop) 10分
p#cl_b(left: 170px; top: 990px; font-size: 30px; color: $ink; background: $c; border-radius: 99px; padding: 6px 20px; border: 3px solid $ink; in: pop) フライパン1つ
p#cl_c(left: 440px; top: 990px; font-size: 30px; color: $paper; background: $b; border-radius: 99px; padding: 6px 20px; border: 3px solid $ink; in: pop) 2人分
```

```timeline.txt
#v2
cast narrator = "明るくやさしい30代女性のナレーター、料理番組のように親しみやすく語りかける" speed=110% manner="やさしく語りかけるように"
transition = wipe,500,dir=right,overlap=500

*** open
[>#subtitle]
bgm music
se "キッチンで湯気が立つ静かな環境音、食器が軽く触れる音" -8dB to=6s fade=300,1500
@narrator: [silence:+0.3s][>#op_k]10分でできる、[>#op_t +200]和風きのこパスタ。
@: [>#op_s]バター醤油で香ばしく、[>#op_n][!#op_n punch]2人分を作ります。
transition dissolve,300,overlap=300

*** ing
@narrator: [silence:+0.3s][>#ig_h]材料はこちら。[>#ig_i[1]]スパゲッティ200グラム、[>#ig_i[2]]しめじ1パック、[>#ig_i[3]]えのき半袋。
@: [>#ig_i[4]]バター20グラム、[>#ig_i[5]]醤油[!#ig_i[5] recolor,$a]大さじ1.5、[>#ig_i[6]]にんにく1片。
@: 仕上げに、刻みのりと青ねぎを[>#ig_i[7]]適量です。

*** s1
se "大きな鍋でお湯がぐつぐつ沸騰する音" -8dB to=6s fade=300,1500
@narrator: [silence:+0.3s]まずは、塩を入れたお湯でパスタを[>#s1_c][>#s1_c.t1]茹でます。
@: 袋の表示より[>#s1_c.t2][>#s1_st][♪"キラリン 21" -5dB]1分短く。[>#s1_c.q check]フライパンで仕上げるからです。[silence:0.8s]

*** s2
se "フライパンでバターがじゅうじゅう溶ける音" -8dB to=8s fade=300,1500
@narrator: [silence:+0.3s]フライパンにバターとにんにくを入れ、[>#s2_h]弱火で[>#s2_c][>#s2_c.t1]香りを出します。
@: 香りが立ったら[>#s2_c.t2][>#s2_c.q][!#s2_h .hot][!#s2_h punch][♪"強火できのこを炒めるじゅわっという音" -4dB]強火にして、きのこを炒めます。
[<#music]

*** tip
bgm music2 -1500
@narrator: [silence:+0.3s][>#tp_k]ここがコツ。[>#tp_t]きのこは触らずに、焼き付けること。
@: [>#tp_s]じっと待つと、[>#tp_st][♪"ジャン！・驚き" +3dB]ぐっと[!#tp_t recolor,$c]香ばしくなります。

*** s3
se "フライパンで湯気が立ちぐつぐつ煮立つ音" -8dB to=6s fade=300,1500
@narrator: [silence:+0.3s][>#s3_a]茹で汁をお玉1杯加えて、[>#s3_b][>#s3_c][>#s3_c.t1][♪"醤油を回しかけるじゅっという音" -5dB]醤油を回しかけ、
@: [>#s3_c.t2][>#s3_c.q]よく混ぜて[!#s3_c.t2{m} marker,$c][!#s3_c punch]乳化させます。

*** s4
@narrator: [silence:+0.3s][>#s4_c]茹で上がったパスタを入れて、[>#s4_c.t1][♪"トングで麺を和える音" -6dB]さっと和えたら、
@: [>#s4_c.q]お皿に盛って、[>#s4_a]刻みのりと[>#s4_b][>#s4_c.t2]青ねぎをのせれば[!#s4_a .done][!#s4_b .done][!#s4_c check]完成です。[silence:1.0s]
transition dissolve,300,overlap=300

*** close
@narrator: [silence:+0.3s][>#cl_t]今日の晩ごはんに、どうぞ。[>#cl_a][>#cl_b >][>#cl_c >][silence:2.0s]
```

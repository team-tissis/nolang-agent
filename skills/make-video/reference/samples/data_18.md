# data · 家計の固定費 (横・前後の数字 + 棒グラフ) — canvas 1280x720・74.3s・視聴者 84.0 (Gemini・vs hf)

見せる文法: 横棒の段の def (hbar・幅は %)・count・×N・stack・focus・manner・se・sticky・def・run・bgm 切替

```design.txt
#v2
# 計画: 明の地 (生成りの紙)・主色は深緑 (見直し後・浮く額)・前の数字は温かい灰・差し色は銅 (指す線だけ)
# 書体 太い角ゴシック (見出し) + 細い欧文 sans (大きな数字) + 細い角ゴシック (注記)・写真は全面 + 紙色の幕・図は幕の上に板なし
canvas 1280x720 bg=#F4F1EA
theme light
palette a=#1E6B52 a2=#CFE3D7 b=#B5643C ink=#1D2B33 paper=#F4F1EA mute=#8C8A84 line=#D9D3C7 card=#FFFFFF
font "太い角ゴシック体、端正で引き締まったビジネス文書の印象"
fonts e="細いサンセリフの欧文、数字が揃う端正な書体" m="細い角ゴシック体、本文向き"
photo_style "実写の写真、日本の明るい住まい、柔らかな自然光、落ち着いた中間色、浅い被写界深度"
prompt_tail "文字なし、ロゴなし、画面に文字を表示しない"
motion title = in=y=-24,opacity=0,duration=700 ease=power3.out out=fade,300
motion big = in=scale=0.92,opacity=0,duration=600 ease=power3.out out=fade,300
motion div = in=y=18,opacity=0,duration=600 ease=power3.out out=fade,260
motion row = in=x=-30,opacity=0,duration=500 ease=power3.out out=fade,240
motion note = in=opacity=0,duration=450 ease=power2.out out=fade,240
div { in: div; border-radius: 12px; background: $card; border: 1px solid $line; box-shadow: none }
cut { stagger: sentence }
run u = color=$a
run y = size=0.6em color=$mute font=m
def h1(t) = p(font-size: 60px; line-height: 1.2; color: $ink; in: title; content: {t})
def num(t) = p(font-size: 64px; font-family: e; color: $a; in: big; content: {t})
def sub(t) = p(font-size: 26px; color: $mute; font-family: m; in: note; content: {t})
def body(t) = p(font-size: 32px; color: $ink; in: row; content: {t})
def note(t) = p(font-size: 24px; color: $mute; font-family: m; in: note; content: {t})
def kick(t) = p(font-size: 20px; color: $a; letter-spacing: 0.2em; font-family: m; in: note; content: {t})
def paper = veil(color: #F4F1EA; opacity: 0.6)
# 横棒の段 (×N で並べ、印は #名[k]): 札 + 棒 (幅 = 値 ÷ 最大 × 50% — 段の幅の比・棒は左から伸びる) + 棒の右端に値
def hbar(v, t, n, c=$a) = div(width: 740px; height: 60px; padding: 0px; background: none; border: none)
  p#t(left: 0px; cy: 50%; width: 200px; font-size: 26px; color: $ink; text-align: right; content: {t})
  div#b(left: 220px; cy: 50%; width: {v}%; height: 40px; border-radius: 4px; background: {c}; border: none; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#n(left: .b.right+12; cy: 50%; font-size: 26px; font-family: e; color: {c}; content: {n})
bgm#music 落ち着いたピアノと柔らかなローファイのビート、静かで知的、ビジネス向けのお金の解説動画
bgm#music2 同じ系統で少し前向きに高まるピアノとストリングス、穏やかなビート、結論の場面向け
subtitle.hug(font-size: 30px; bottom: 24px; background: #1D2B33E6; color: #F4F1EA; border-radius: 6px; padding: 8px 24px)

section#open
img#op_p(inset: 0; main: kb,1.0@60%,50%>1.06@64%,48%) [photo]木のダイニングテーブルに広げた家計簿のノートと公共料金の請求書と電卓、30代夫婦の手元だけ、朝の自然光
veil#op_v(color: #F4F1EA; opacity: 0.7; to: left; start: 0.45)
shape#op_c(left: 24px; top: 430px; width: 260px; height: 260px; path: circle; background: $a; opacity: 0.06; main: breathe)
kick#op_k(left: 72px; top: 150px) HOUSEHOLD FIXED COSTS
shape#op_r(left: 72px; top: 186px; width: 96px; height: 3px; path: line_h; background: $a; border: 3px solid $a; in: wipe,right,700)
h1#op_h(left: 72px; top: 214px; width: 640px) 固定費を見直すと、[br]{t}年間{/}いくら浮く?
sub#op_s(left: 72px; top: 380px) 30 代夫婦のモデルケース (架空) で試算

section#model
img#md_p(left: 660px; top: 0px; width: 620px; height: 720px; main: kb,1.0@50%,50%>1.05@50%,45%) [photo]30代の夫婦がリビングのソファに並んでノートパソコンで家計を確認する横顔、穏やかな表情、自然光
kick#md_k(left: 64px; top: 56px) MODEL CASE
h1#md_h(left: 64px; top: 84px; font-size: 48px) 30 代の夫婦、3 つの固定費
div#md_r(left: 64px; top: 184px; width: 560px; height: 264px; gap: 16; padding: 0px; display: flex; flex-direction: column) ×3
  icon#i(left: 22px; cy: 50%; font-size: 34px; name: "device-mobile;lightning;television-simple"; color: $a)
  p#n(left: 76px; cy: 50%; font-size: 28px; color: $ink) スマホ (2 人);電気;サブスク (3 本)
  p#v(right: 24px; cy: 50%; font-size: 36px; font-family: e; color: $ink) 16,000{y}円 / 月{/};11,000{y}円 / 月{/};3,300{y}円 / 月{/}
shape#md_l(left: 64px; top: 476px; width: 560px; height: 2px; path: line_h; background: $ink; border: 2px solid $ink; in: wipe,right,600)
p#md_t(left: 64px; top: 494px; font-size: 28px; color: $ink) 3 つの合計
p#md_v(right: 656px; top: 482px; font-size: 56px; font-family: e; color: $a; text-align: right) [count:30,300]{y}円 / 月{/}

section#phone
img#ph_p(inset: 0; main: kb,1.0@50%,50%>1.05@55%,50%) [photo]木の机の上に並べて置かれた2台のスマートフォン、画面は暗い、柔らかな自然光
paper#ph_v
num#ph_n(left: 64px; top: 44px) 01
h1#ph_h(left: 152px; top: 52px; font-size: 52px) スマホ
sub#ph_s(left: 64px; top: 128px) 大手キャリア 2 人 → 格安プラン
hbar#ph_c(left: 64px; top: 240px; width: 740px; height: 160px; display: flex; flex-direction: column; gap: 40px; v: "50;16"; t: "今 (大手キャリア);見直し後 (格安)"; n: "16,000 円;5,000 円"; c: "$mute;$a") ×2
div#ph_d(left: 860px; top: 196px; width: 356px; height: 250px; padding: 0px)
  p#l(left: 28px; top: 26px; font-size: 22px; font-family: m; color: $mute) 年間の差
  p#v(left: 28px; top: 70px; font-size: 64px; font-family: e; color: $a) [count:132,000]{y}円{/}
  shape#r(left: 28px; top: 162px; width: 300px; height: 2px; path: line_h; background: $line; border: 2px solid $line)
  p#s(left: 28px; top: 182px; font-size: 24px; font-family: m; color: $ink) 月 11,000 円 × 12 か月

section#power
img#pw_p(inset: 0; main: kb,1.0@50%,50%>1.05@45%,50%) [photo]明るい部屋の壁のスイッチと電気メーター、柔らかな自然光、すっきりした住まい
paper#pw_v
num#pw_n(left: 64px; top: 44px) 02
h1#pw_h(left: 152px; top: 52px; font-size: 52px) 電気
div#pw_t(left: 64px; top: 124px; width: 480px; height: 52px; padding: 0px; background: $a2; border: none; border-radius: 26px)
  icon#i(left: 18px; cy: 50%; font-size: 26px; name: check-circle; color: $a)
  p#t(left: 54px; cy: 50%; font-size: 24px; color: $a) 使用量はそのまま、契約先だけ変更
hbar#pw_c(left: 64px; top: 240px; width: 740px; height: 160px; display: flex; flex-direction: column; gap: 40px; v: "50;43"; t: "今の契約;新しい契約"; n: "11,000 円;9,400 円"; c: "$mute;$a") ×2
div#pw_d(left: 860px; top: 196px; width: 356px; height: 250px; padding: 0px)
  p#l(left: 28px; top: 26px; font-size: 22px; font-family: m; color: $mute) 年間の差
  p#v(left: 28px; top: 70px; font-size: 64px; font-family: e; color: $a) [count:19,200]{y}円{/}
  shape#r(left: 28px; top: 162px; width: 300px; height: 2px; path: line_h; background: $line; border: 2px solid $line)
  p#s(left: 28px; top: 182px; font-size: 24px; font-family: m; color: $ink) 月 1,600 円 × 12 か月

section#subs
img#sb_p(inset: 0; main: kb,1.0@50%,50%>1.05@50%,55%) [photo]夜のリビングでテレビの前のソファに置かれたリモコンとヘッドホン、誰もいない、落ち着いた間接照明
paper#sb_v
num#sb_n(left: 64px; top: 44px) 03
h1#sb_h(left: 152px; top: 52px; font-size: 52px) サブスク
sub#sb_s(left: 64px; top: 128px) 使っていない動画・音楽の 3 本を解約
div#sb_k(left: 64px; top: 196px; width: 740px; height: 76px; gap: 16; padding: 0px; display: flex) ×3
  icon#i(left: 18px; cy: 50%; font-size: 28px; name: "film-strip;film-strip;music-notes"; color: $mute)
  p#t(left: 56px; cy: 50%; font-size: 24px; color: $ink) 動画配信 A;動画配信 B;音楽配信
hbar#sb_c(left: 64px; top: 310px; width: 740px; height: 130px; display: flex; flex-direction: column; gap: 30px; v: "50;1"; t: "今;解約後"; n: "3,300 円;0 円"; c: "$mute;$a") ×2
div#sb_d(left: 860px; top: 196px; width: 356px; height: 250px; padding: 0px)
  p#l(left: 28px; top: 26px; font-size: 22px; font-family: m; color: $mute) 年間の差
  p#v(left: 28px; top: 70px; font-size: 64px; font-family: e; color: $a) [count:39,600]{y}円{/}
  shape#r(left: 28px; top: 162px; width: 300px; height: 2px; path: line_h; background: $line; border: 2px solid $line)
  p#s(left: 28px; top: 182px; font-size: 24px; font-family: m; color: $ink) 月 3,300 円 × 12 か月

section#total
img#tt_p(inset: 0; main: kb,1.0@50%,50%>1.04@50%,50%) [photo]整えられた家計簿のノートと電卓と万年筆を真上から、白い机、明るい自然光
paper#tt_w
kick#tt_k(left: 64px; top: 56px) ANNUAL SAVINGS
h1#tt_h(left: 64px; top: 84px; font-size: 48px) 3 つ合わせると、1 年で
hbar#tt_c(left: 64px; top: 207px; width: 640px; height: 216px; display: flex; flex-direction: column; gap: 30px; v: "40;12;6"; t: "スマホ;サブスク;電気"; n: "132,000 円;39,600 円;19,200 円"; c: "$a;$mute;$mute") ×3
shape#tt_l(left: 730px; top: 196px; width: 2px; height: 250px; path: line_v; background: $line; border: 2px solid $line)
p#tt_lb(left: 776px; top: 206px; font-size: 24px; font-family: m; color: $mute) 年間で浮く額
p#tt_v(left: 770px; top: 246px; font-size: 104px; font-family: e; color: $a) [count:190,800]{y}円{/}
p#tt_s(left: 776px; top: 396px; font-size: 26px; color: $ink) うち 7 割がスマホ

section#month
img#mo_p(inset: 0; main: kb,1.0@40%,50%>1.06@35%,50%) [photo]木の机の上の白い給与明細の封筒と電卓と観葉植物、窓からの柔らかな光
veil#mo_v(color: #F4F1EA; opacity: 0.7; to: left; start: 0.5)
shape#mo_c(left: 24px; top: 24px; width: 240px; height: 240px; path: circle; background: $a; opacity: 0.06; main: breathe)
p#mo_k(left: 72px; top: 150px; font-size: 30px; font-family: m; color: $mute) 年 190,800 円は
h1#mo_h(left: 72px; top: 200px; font-size: 72px) 月の手取りの[br]{m}1 か月分近く{/}
div#mo_n(left: 72px; top: 420px; width: 420px; height: 64px; padding: 0px)
  icon#i(left: 20px; cy: 50%; font-size: 28px; name: arrows-clockwise; color: $a)
  p#t(left: 62px; cy: 50%; font-size: 26px; color: $ink) 一度の手続きで、毎年続く

section#close
img#cl_p(inset: 0; main: kb,1.0@60%,50%>1.06@65%,50%) [photo]朝の窓辺のテーブルでコーヒーを片手にスマートフォンを見る人の手元、明るい自然光、すがすがしい
veil#cl_v(color: #F4F1EA; opacity: 0.7; to: left; start: 0.5)
kick#cl_k(left: 72px; top: 120px) THIS WEEK
h1#cl_h(left: 72px; top: 150px; font-size: 76px) まず 1 つだけ、[br]{u}今週やる。{/}
div#cl_c(left: 72px; top: 380px; width: 600px; height: 70px; gap: 14; padding: 0px; display: flex) ×3
  icon#i(left: 16px; cy: 50%; font-size: 26px; name: "device-mobile;lightning;television-simple"; color: $a)
  p#t(left: 50px; cy: 50%; font-size: 24px; color: $ink) スマホ;電気;サブスク
```

```timeline.txt
#v2
cast narrator = "落ち着いた30代女性のナレーター、明瞭で知的なビジネス向けの解説口調" speed=105%
transition = dissolve,300,overlap=300

*** open
[>#subtitle]
bgm music
se "静かな朝の室内の環境音、遠くの鳥の声" -8dB to=8s fade=300,1500
@narrator: [silence:+0.4s]毎月、自動で出ていく固定費。
@: [>#op_h]見直すと、[!#op_h{t} underline,$a]一年でいくら浮くのでしょうか。[silence:0.6s]

*** model
@narrator: [silence:+0.3s]架空の30代夫婦をモデルに、[>#md_r[1]]スマホ、[>#md_r[2]]電気、[>#md_r[3]]サブスクの三つを見直します。
@: [>#md_l][>#md_t][>#md_v]三つ合わせて、今は毎月3万300円です。[silence:0.5s]
transition wipe,600,dir=left,overlap=600

*** phone
@narrator: [silence:+0.3s]まずはスマホ。[>#ph_c[1]]大手キャリアで2人、月1万6000円。
@: これを[>#ph_c[2]]格安プランにすると、月5000円。
@: 差は月1万1000円、[>#ph_d][!#ph_d.v count][♪"お金・財宝・アイテムゲット" -6dB]一年で13万2000円です。[silence:0.5s]

*** power
@narrator: [silence:+0.3s]次に電気。[!#pw_t check]使う量はそのままで、契約先だけを変えます。
@: [>#pw_c[1]]月1万1000円が、[>#pw_c[2]]9400円に。
@: 一年で、[>#pw_d][!#pw_d.v count]1万9200円です。[silence:0.5s]

*** subs
@narrator: [silence:+0.3s]最後はサブスク。[>#sb_k[*] {stagger:{each:0.12}}]使っていない動画と音楽の三本を、
@: [!#sb_k[1].t strike,$b][!#sb_k[2].t strike,$b +150][!#sb_k[3].t strike,$b +300]解約して、[>#sb_c[1]]月3300円が、[>#sb_c[2]]0円に。
@: 一年で、[>#sb_d][!#sb_d.v count]3万9600円です。[silence:0.5s]
transition dip,400
[<#music]

*** total
bgm music2 -1500
@narrator: [silence:+0.4s][>#tt_c[*] {stagger:{each:0.12}}]三つを合わせると、[>#tt_lb][>#tt_v][♪"キラリン 21" -2dB]一年で19万800円。
@: [!#tt_c[1] focus][>#tt_s]スマホだけで、その7割を占めます。[silence:0.6s]

*** month
@narrator: [silence:+0.4s][>#mo_h]これは、[!#mo_h{m} marker,$a2]月の手取りの{1か月|いっかげつ}分近く。
@: [>#mo_n]一度手続きをすれば、毎年この差が続きます。[silence:0.6s]

*** close
@narrator: [silence:+0.4s]全部を一度にやる必要はありません。
@: [>#cl_h]まず1つだけ、[!#cl_c[1] check][♪"決定音" -6dB]今週やってみませんか。[silence:2.5s]
```

## 3 分以上の data の時だけ: 累計の札

数字が 2 cut 以上続いて合計になる題材で、動画が 3 分以上 (plan の見込み秒の和が 180 以上) の時だけ根に 1 つ足す。1 分程度の動画には置かない (この見本は 74 秒なので置いていない)。
累計の値は plan の行の見せ物に先に書き (和の計算は plan で 1 回)、各 cut はそれを写す (check の `running_total` は値が cut を跨いで減ると warn)。
この見本に足して check で確かめた形 (warn は増えず、最後の frame に「累計 190,800円」が残る):

```
# design の根 (`section#` より前): 上端に 1 つ。他の cut の要素を上端の帯に置かない (置くと札に重なって occluded)
p#sum.sticky(right: 32px; top: 14px; font-size: 24px; color: $a; background: $card; border-radius: 99px; padding: 4px 16px) 累計 [count:0]円
# timeline: その額を言う語に (cut の頭に置くと台詞より先に和が見える)・数字は 3 桁区切りで書く (区切らずに書くと区切りの無いまま出る)・数え始めは前の値から自動
@: 差は月1万1000円、[>#ph_d][!#ph_d.v count][!#sum text,"累計 [count:132,000]円"]一年で13万2000円です。
@: 一年で、[>#pw_d][!#pw_d.v count][!#sum text,"累計 [count:151,200]円"]1万9200円です。
@: 一年で、[>#sb_d][!#sb_d.v count][!#sum text,"累計 [count:190,800]円"]3万9600円です。
```

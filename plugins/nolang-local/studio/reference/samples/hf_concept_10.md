# concept · find-interest (hf 全力版の全量の写し — やりたいことが見つかってから選ぶ順番は逆かもしれない、サルトルと興味の研究・8 場面の線画イラストと語で組む図解) — canvas 720x1280

見せる作り: 生成りの紙の地 (点の地紋・周辺の明るみ・細い枠) と上端の章札・場面ごとの中央の線画 1 枚 (右から入って寄る)・切替なしで要素が一斉に左へ抜ける場面替え + 紙をめくる音・3 段の文字 (灰の明朝の前置き → 太い明朝の主文 + 砂色の下線 → 小さな注記)・番号つきの 2 枚の札の入れ替え・「逆」を囲む手描きの丸・語ごとの 2 段の矢印図 (× と灰)・縮む寸法線・条件の板の取り消し線・入れ替わる札と引き直す矢印・字幕を出さない文 2 つ・最後は地の色へ溶ける・音の層 (BGM + 語に結んだ鉛筆と鈴の音 16)

```design.txt
#v2
# 学ぶ作り: 生成りの紙の地 (点の地紋 + 周辺の明るみ + 細い枠) を全編に敷き、場面ごとに上端の章札 (両脇の線) と中央の線画イラスト 1 枚を替える
# 文字は 3 段の class で組む: 小さい明朝の前置き (灰) → 語で下から出る太い明朝の主文 (語の下に砂色の下線が伸びる) → 中ほどの小さな注記 (出典・肩書)
# 説明の図は 1 場面に 1 つ: 番号つきの 2 枚の札が入れ替わる・語ごとの 2 段の矢印図 (× で打ち消して灰に)・寸法線が縮む・条件の板に取り消し線・2 つの札が入れ替わって矢印が引き直される
# 場面の替わりは切替なし: 前の場面の要素が一斉に左へ抜け (cut の out)、次の要素が右から入る・境目ごとに紙をめくる音
# hf 10 find-interest (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 720x1280 bg=#F3EDE3
theme light
palette paper=#F3EDE3 ink=#1F2A3D sub=#5B6577 accent=#C2643F sand=#EAD8B8 card=#FBF8F2 cardline=#D9CCB6 gray=#7D8696 grayline=#B9B2A6
font "太めの標準的な角ゴシック体"
fonts s="太い明朝体、端正で知的な見出し向け" sr="標準の太さの明朝体、静かな前置き向け" r="標準の太さの角ゴシック体、字幕向けで読みやすい"
art "細く少し揺れる紺のインクの手描きの線画、平塗りは控えめにくすんだテラコッタと淡い砂色だけ、余白が多い、影・グラデーション・枠なし、知的で落ち着いた雑誌の挿絵、シンプルでひと目で分かる"
prompt_tail "文字・数字・ロゴなし、白い無地の背景、主題は画面いっぱいに大きく中央に"
sfx off
master lufs=-15
# hf の作り: 章札・板の題・図の札は台詞より先に置く (spoiler)・「この順番、逆かもしれません。」と最後の問いは字幕を出さず大きな明朝の文字だけで見せる (caption_gap)
# hf の作り: 結論の場面は絵を置かず条件の板 1 枚 (text_only_cut)・出典と肩書の注記は 1080 換算 24 px の小さな字 (small_text)
lint off=spoiler,caption_gap,text_only_cut,small_text
run m { marker: $sand,36% }
run q { color: $accent }
p { color: $ink }
# 場面の要素は一斉に左へ抜ける (hf の leave: x -26 px・0.4 s)・頭の組み上がりは一斉
cut { stagger: 0; out: {x:-17, opacity:0, duration:.4, ease:'power1.in'} }
sound page = "紙のページを1枚めくる乾いた短いペラッという音"
sound sweep = "中域の柔らかいノイズが滑らかに上がっていくスゥーッという音"
sound airy = "空気感のある短い風のようなノイズのシュッという音、回想に入る瞬間の"
sound pencil = "丸い鉛筆で紙に直線を引くサラサラという音"
sound circle = "シャープペンで紙に丸を描く滑らかなサラサラという音"
sound switch = "プラスチックのスイッチを押すカチッという乾いた短い音"
sound accent = "低めの柔らかいシンセのベルが短く上がるポロンという音"
sound accent2 = "空間的な響きの柔らかいシンセのベルが上がるピロリンという音"
# hf の作り: 曲は声より 11.5 LU 下 (engine の既定 = 台詞中 11 LU 下のまま・gap は書かない)
bgm#music(fade: 800,3200) 静かでゆっくりしたアンビエント、繊細なソロピアノに温かいシンセパッドと柔らかなチェロ、内省的で穏やかに広がる
# 字幕: 板なし・墨色の細い角ゴシック・画面の下 1/4 の位置・0.14 s の fade だけ
subtitle(left: 20px; top: 964px; width: 680px; font-size: 31px; line-height: 1.58; letter-spacing: .02em; text-align: center; color: $ink; font-family: r; background: none; border: none; box-shadow: none; padding: 0px; unit: sentence; lead: 0; tail: 110; hold: off; in: {opacity:0, duration:.14}; out: {opacity:0, duration:.14})
# 地: 点の地紋 + 中央が明るく縁がくすむ周辺の明るみ + 内側 24 px の細い枠 (全編・最背面)
div#grain(inset: 0; pattern: dots,5,#7864460A; z-index: back; border-radius: 16px; in: none; out: none)
div#vignette(inset: 0; background: radial(#FFFFFF59,#FFFFFF00@60%,#785F3C1A,50%,45%); z-index: back; border-radius: 16px; in: none; out: none)
div#frame(left: 24px; top: 24px; width: 672px; height: 1232px; border: 1px solid #A08C6E47; border-radius: 4px; z-index: back; in: none; out: none)

# 上端の章札 (煉瓦色の字 + 両脇の短い線)・場面の頭に右から
def label(t) = p(cx: 360px; top: 131px; font-size: 20px; letter-spacing: .32em; color: $accent; rules: both,36,1,#C2643F8C,17; delay: 100; in: {x:20, opacity:0, duration:.6, ease:'power2.out'}; content: {t})
# 中央の線画 (透過・枠の中に収める)・右から入ってゆっくり寄る
def illus = img(object-fit: contain; in: {x:24, opacity:0, duration:.8, ease:'power2.out'}; delay: 50)
# 文字の段: 前置き (標準の明朝・灰)・主文 (太い明朝)・注記 (小さな角ゴシック・灰)
def lead(t) = p(cx: 360px; font-family: sr; color: $sub; letter-spacing: .03em; in: {y:11, opacity:0, duration:.55, ease:'power2.out'}; content: {t})
def tel(t) = p(cx: 360px; font-family: s; line-height: 1.3; letter-spacing: .03em; in: {y:13, opacity:0, duration:.65, ease:'power2.out'}; content: {t})
def cap(t) = p(cx: 360px; font-size: 19px; letter-spacing: .12em; color: $sub; font-family: r; in: {y:8, opacity:0, duration:.6, ease:'power2.out'}; content: {t})
# 図の札 (墨の縁の角丸の箱 + 太い明朝の語)・語で下から
def box(t, w=173) = div(width: {w}; height: 73px; background: $card; border: 2px solid $ink; border-radius: 13px; in: {y:11, opacity:0, duration:.55, ease:'power2.out'})
  p#t(cx: 50%; cy: 50%; font-family: s; font-size: 39px; content: {t})
# 矢印 (線の矢じり・線で描く)・矢印の上の小さな札
def arrow(c=$accent) = shape(height: 29px; path: arrow_r,head=line; background: {c}; border: 3px solid {c}; in: draw {duration: 0.6})
def alabel(t, c=$accent) = p(cx: 360px; font-size: 20px; letter-spacing: .12em; color: {c}; in: {y:7, opacity:0, duration:.5, ease:'power2.out'}; content: {t})
# 打ち消しの × (線で描く)
def cross = shape(width: 34px; height: 34px; path: cross; background: none; border: 5px solid $accent; in: draw {duration: 0.45})
# 番号の丸札・番号つきの札 (絵 + 文)
def badge(n) = div(width: 43px; height: 43px; border-radius: 99px; background: $card; border: 2px solid $accent; in: {opacity:0, duration:.5, ease:'power2.out'})
  p#n(cx: 50%; cy: 50%; font-family: s; font-size: 23px; color: $accent; content: {n})
def card = div(left: 107px; width: 567px; height: 200px; background: $card; border: 2px solid $cardline; border-radius: 19px; box-shadow: 0px 12px 27px #5A46281A; in: {y:20, opacity:0, duration:.7, ease:'power2.out'})

# order — 問い: 「見つかる → 選ぶ」の 2 枚の札を語で積み、「順番」で札が入れ替わり、「逆」に手描きの丸
section#order
label#lab1 順番
card#card_a(top: 313px)
  img#i(left: 17px; cy: 50%; width: 153px; height: 153px; object-fit: contain) [transparent]少し傾けた虫眼鏡が小さなきらめきをのぞいている
  p#s(cx: 355px; top: 43px; font-family: s; font-size: 33px; color: $sub) やりたいことが
  p#t(cx: 355px; top: 84px; font-family: s; font-size: 57px) 見つかる
badge#b1(left: 41px; top: 392px; n: "1"; delay: 330)
shape#arr1(left: 374px; top: 523px; width: 32px; height: 75px; path: arrow_d,head=line; background: $accent; border: 3px solid $accent; in: draw {duration: 0.45})
card#card_b(top: 607px)
  img#i(left: 17px; cy: 50%; width: 153px; height: 153px; object-fit: contain) [transparent]テーブルに扇形に広げた 3 枚のカードから片手が 1 枚を選び取っている
  p#t(cx: 355px; cy: 50%; font-family: s; font-size: 69px) 選ぶ
#card_b.hot(border: 2px solid $accent)
badge#b2(left: 41px; top: 685px; n: "2")
lead#t2a(top: 824px; font-size: 36px) この順番、
tel#t2b(top: 871px; font-size: 61px; in: {y:13, opacity:0, duration:.6, ease:'power2.out'}) {q}逆{/}かもしれません。
# 「逆」を囲む手描きの丸 (文字の後ろに描いていく)
shape#circ2(left: 61px; top: 858px; width: 96px; height: 104px; path: circle_hand; background: none; border: 3px solid $accent; overlap: t2b; in: draw {duration: 0.6})

# lost — 迷い: 分かれ道の人の線画に、前置き → 「就職で迷う」が語で出て下線が伸びる
section#lost
label#lab2 迷い
illus#im2(left: 160px; top: 193px; width: 400px; height: 497px; aspect: 4:5; main: kb {scale: [1, 1.06]}) [transparent]地味なスーツの若い人の後ろ姿、一本の道が四方向に分かれる所に立ち止まる、分岐に何も書いていない四枚の矢印板の木の道標、頭の上に小さな疑問符の落書きが三つ
lead#t3a(top: 720px; font-size: 35px) やりたいことがないまま、
tel#t3b(top: 768px; font-size: 77px) {m}就職で迷う{/}

# sartre — 人物の紹介: 向かい合う 2 つのカップのカフェの卓に、名 → 肩書 → 札つきの引用 → 出典 (章札は次の場面へ跨ぐ)
section#sartre
label#lab3.sticky サルトル
illus#im3(left: 67px; top: 212px; width: 587px; height: 407px; aspect: 3:2; main: kb {scale: [1, 1.05]}) [transparent]パリの小さな丸いカフェのテーブル、向かい合わせに置いた 2 つのコーヒーカップ、間に開いたノートとペン、曲げ木の椅子が 2 脚、人物なし、先生と教え子の静かな会話を思わせる
tel#nm(top: 632px; font-size: 36px; in: {y:12, opacity:0, duration:.7, ease:'power2.out'}) ジャン＝ポール・サルトル
cap#nm2(top: 687px) フランスの哲学者（1905–1980）
# 引用の組: 灰の丸札「教え子」+ 煉瓦色の鉤括弧の引用 (札と文を 1 つの組で出す)
group#q3(in: {y:15, opacity:0, duration:.7, ease:'power2.out'})
  p#tag(left: 63px; cy: 773px; font-size: 20px; letter-spacing: .1em; color: $card; background: $sub; border-radius: 99px; padding: 4px 15px) 教え子
  p#text(left: 174px; top: 739px; font-family: s; font-size: 52px; line-height: 1.3) {q}「{/}気持ちで決める{q}」{/}
cap#src3(top: 845px; font-size: 16px; letter-spacing: .02em; in: {y:5, opacity:0, duration:.6, ease:'power2.out'}) サルトル『実存主義とは何か』より

# clay — 要約: 粘土の壺を形づくる手の線画に、2 段の矢印図を語ごとに組み、下段に × を描いて灰に沈める
section#clay
illus#im4(left: 187px; top: 191px; width: 347px; height: 373px; main: kb {scale: [1, 1.05]}) [transparent]ろくろの上で粘土の壺を両手でそっと形づくる、横から見た手元
box#r1a(left: 100px; top: 615px) 行動
alabel#r1l(top: 592px) 形づくる
arrow#r1arr(left: 279px; top: 637px; width: 163px)
box#r1b(left: 447px; top: 615px) 気持ち
box#r2a(left: 100px; top: 767px) 気持ち
#r2a.off(border: 2px solid $grayline)
alabel#r2l(top: 744px; c: $sub) 手引き
arrow#r2arr(left: 279px; top: 789px; width: 163px; c: $sub; in: draw {duration: 0.5})
cross#x5(left: 343px; top: 787px)
box#r2b(left: 447px; top: 767px) 行動
#r2b.off(border: 2px solid $grayline)

# study — ある研究: 懐中電灯が 1 冊だけ照らす線画が明滅して点き、引用 → 「興味の幅」の寸法線が縮んで「狭い」
section#study
label#lab4 ある研究
# 明滅して点く絵 (0 → 0.28 で止まり → 1)
img#im5(left: 47px; top: 235px; width: 627px; height: 393px; object-fit: contain; aspect: 16:10; main: kb {scale: [1, 1.06]}; in: keys(at=0 opacity=0 | at=0.6 opacity=0.28 | at=0.71 opacity=0.28 | at=1),duration=420) [transparent]左の懐中電灯がとても細い光の筋で小さな本を 1 冊だけ照らしている、周りにギター・鉢植え・カメラ・絵筆・地球儀・サッカーボールが光の外に塗りなしの細い線だけで置かれている
p#cite6(right: 80px; top: 669px; font-size: 16px; color: $sub; italic: true; letter-spacing: .02em; in: {y:5, opacity:0, duration:.6, ease:'power2.out'}) O’Keefe, Dweck & Walton (2018)
tel#t6a(top: 701px; font-size: 47px; in: {y:12, opacity:0, duration:.7, ease:'power2.out'}) {q}「{/}興味は見つけるもの{q}」{/}
lead#t6b(top: 772px; font-size: 29px) と考える人ほど
# 興味の幅: 札 + 寸法線 (|—|) — 線は中心へ scaleX で縮み、両端の縦棒は x で寄り、札も中央へ寄る (寸法線の shape は幅を補間しないので 3 本の群に分ける)
p#wlab(left: 75px; cy: 872px; font-family: s; font-size: 36px; in: {y:9, opacity:0, duration:.55, ease:'power2.out'}) 興味の幅
group#wbar(in: {y:9, opacity:0, duration:.55, ease:'power2.out'})
  div#line(left: 242px; cy: 872px; width: 293px; height: 3px; background: $ink)
  div#tl(left: 242px; cy: 872px; width: 3px; height: 24px; background: $ink)
  div#tr(left: 532px; cy: 872px; width: 3px; height: 24px; background: $ink)
p#wn(left: 439px; cy: 872px; font-family: s; font-size: 44px; color: $accent; in: {x:-11, opacity:0, duration:.5, ease:'power2.out'}) 狭い

# conclusion — 結論: 「選ぶ前の条件」の板に □ やりたいこと → 語で題が煉瓦色・取り消し線・× と灰・下に「できない」+ 下線 (章札は次の場面へ跨ぐ)
section#conclusion
label#lab5.sticky 結論
div#cc7(left: 87px; top: 267px; width: 547px; height: 347px; background: $card; border: 2px solid $cardline; border-radius: 20px; box-shadow: 0px 12px 27px #5A46281A; delay: 100; in: {y:20, opacity:0, duration:.8, ease:'power2.out'})
  p#head(cx: 50%; top: 41px; font-family: s; font-size: 41px; letter-spacing: .06em) 選ぶ前の条件
  div#rule(left: 60px; top: 115px; width: 427px; height: 1px; background: $cardline)
  div#item(left: 0px; top: 167px; width: 547px; height: 107px; in: {y:8, opacity:0, duration:.55, ease:'power2.out'})
    div#box(left: 66px; cy: 50%; width: 56px; height: 56px; border: 3px solid $ink; border-radius: 9px)
    shape#x(left: 80px; cy: 50%; width: 29px; height: 29px; path: cross; background: none; border: 5px solid $accent; in: draw {duration: 0.4})
    p#t(left: 145px; cy: 50%; font-family: s; font-size: 56px) やりたいこと
    shape#st(left: 137px; cy: 52%; width: 352px; height: 29px; path: strike; background: none; border: 5px solid $accent; overlap: cc7.item.t; in: draw {duration: 0.55})
lead#t7a(top: 697px; font-size: 41px) 選ぶ前の条件には
tel#t7b(top: 753px; font-size: 80px; in: {y:13, opacity:0, duration:.6, ease:'power2.out'}) {m}できない{/}

# reverse — 言い換え: 水やりで芽が出る線画に「意識が向く → 関わる」と × → 2 つの札が弧を描いて入れ替わり、煉瓦色の矢印が引き直される
section#reverse
illus#im6(left: 203px; top: 200px; width: 313px; height: 387px; aspect: 4:5; main: kb {scale: [1, 1.04]}) [transparent]小さなじょうろを持つ手が、土の小山から出た双葉の小さな芽に水をやっている
box#r8a(left: 60px; top: 640px; w: 240) 意識が向く
#r8a.hot(border: 2px solid $accent)
arrow#arr8(left: 304px; top: 662px; width: 112px; c: $ink; in: draw {duration: 0.45}; out: {opacity:0, duration:.2})
cross#x8(left: 343px; top: 660px; in: draw {duration: 0.4}; out: {opacity:0, duration:.25})
box#r8b(left: 420px; top: 640px; w: 240) 関わる
#r8b.hot(border: 2px solid $accent)
arrow#arr8b(left: 304px; top: 662px; width: 112px; in: draw {duration: 0.4})
tel#t8(top: 780px; font-size: 43px; in: {y:11, opacity:0, duration:.6, ease:'power2.out'}) {m}関わるから{/}意識が向く。

# question — 問いかけ: 少し開いた扉の線画に、前置き → 「止めているものは / ありますか。」を 2 行で語ごとに・下線 (字幕なし・最後は地の色へ溶ける)
section#question
label#lab6 問いかけ
illus#im7(left: 240px; top: 188px; width: 240px; height: 457px; aspect: 9:16; main: kb {scale: [1, 1.08]}; in: {x:24, opacity:0, duration:.9, ease:'power2.out'}) [transparent]少しだけ開いた扉が 1 枚立ち、隙間から暖かい光が床にこぼれている、扉の手前に小さな足跡がひとつ
lead#t9a(top: 667px; font-size: 40px) 見つかったら選ぶ、で
tel#t9b(top: 727px; font-size: 64px; in: {y:12, opacity:0, duration:.7, ease:'power2.out'}) {m}止めているもの{/}は
tel#t9c(top: 819px; font-size: 64px; in: {y:12, opacity:0, duration:.7, ease:'power2.out'}) ありますか。
```

```timeline.txt
#v2
cast n = "落ち着いた低音域の若い男性ナレーター、芯の通ったクリアな声で、一定のテンポで静かに穏やかに語る" speed=95%
silence head=0 tail=0

*** order
[>#subtitle]
bgm music start=13.7s
@n: [silence:0.7s]やりたいことが見つかって[>#arr1 -100]から[>#card_b -200][>#b2]選ぶ。[silence:0.5s]
[<#subtitle]
@: [>#t2a -50]この[!#b1 to,{scale:1.18, duration:.22, ease:'power1.out', repeat:1, yoyo:true}][!#b2 to,{scale:1.18, duration:.22, ease:'power1.out', repeat:1, yoyo:true}]順番[!#card_a to,{y:293, arc:.1, duration:.95, ease:'power2.inOut'} +220][!#card_b to,{y:-293, arc:.1, duration:.95, ease:'power2.inOut'} +220][♪sweep -2dB +180]、[>#t2b -100]逆[>#circ2 +350][♪circle -3dB +300]かもし[!#card_b .hot]れません。[silence:1.15s]

*** lost
se page -2.5dB
[>#subtitle]
@n: [silence:0.55s][>#t3a]やりたいことがないまま、[br][>#t3b -100]就職で[!#t3b{m} marker]迷う人は多いのではないでしょうか。[silence:0.8s]

*** sartre
se page -2.5dB
@n: [silence:0.6s][>#nm -50][>#nm2 +250]サルトルは、[>#q3 -150]気持ちで[>#src3]決めると言った[br]教え子の話をしています。[silence:0.55s]

*** clay
@n: [silence:0.45s]サルトルの考えを要約すると、[br][>#r1b -100]気持ちは[>#r1a -100]行動で[>#r1arr -150][♪pencil -1dB -150][>#r1l]形づくられるので、[|][>#r2a -200][>#r2b -200]行[>#r2arr][>#r2l +80]動の手引きには[>#x5 -50][♪pencil -1dB -50]で[!#r2a .off -50][!#r2b .off -50][!#r2a.t recolor,$gray -50][!#r2b.t recolor,$gray -50]きない。[silence:1.0s]
[<#lab3]

*** study
se page -2.5dB
se switch +330 -3dB
@n: [silence:0.6s][>#cite6 +300]ある研究では、[br][>#t6a -100]興味は見つけるものと[>#t6b -100]考える[>#wlab -200][>#wbar -200]人ほど、[|]興味の幅[♪airy -3dB +120][!#wbar.line to,{scaleX:.191, duration:.85, ease:'power3.inOut'} +170][!#wbar.tl to,{x:118, duration:.85, ease:'power3.inOut'} +170][!#wbar.tr to,{x:-119, duration:.85, ease:'power3.inOut'} +170][!#wlab to,{x:118, duration:.85, ease:'power3.inOut'} +170]が[>#wn +200]狭い傾向がありました。[silence:1.3s]

*** conclusion
se page -2.5dB
@n: [silence:0.6s]結論は、[>#cc7.item -150]やりたいことを、[br]選ぶ前の[!#cc7.head recolor,$accent -100][>#t7a -100]条件に[>#cc7.item.st][♪pencil -1dB]は[>#t7b -50]で[>#cc7.item.x]き[!#cc7.item.t recolor,$gray][♪accent -2dB][!#t7b{m} marker +50]ない、ということ。[silence:0.65s]

*** reverse
@n: [silence:0.45s][>#r8a -50]意識が[>#arr8 -100]向いてから[>#r8b -100]関わる[>#x8][♪pencil -1dB]のではなく、[<#x8 -250][<#arr8 -250][!#r8a to,{x:360, arc:.15, duration:.9, ease:'power2.inOut'} -250][!#r8b to,{x:-360, arc:.15, duration:.9, ease:'power2.inOut'} -250][♪sweep -3dB -340]関わるか[>#arr8b -60][!#r8a .hot -60][!#r8b .hot -60][>#t8 -80]ら[!#im6 to,{y:-5, duration:1.2, ease:'sine.inOut'}][♪accent2 -2.5dB +150][!#t8{m} marker +200]意識が向く。[silence:1.25s]
[<#lab5]

*** question
se page -2.5dB
[<#subtitle]
@n: [silence:0.65s][>#t9a -50]見つかったら選ぶ、で[>#t9b -150]止めているものは[>#t9c -100]ありま[!#t9b{m} marker]すか。[silence:3.72s]
fade out,900
```

# story · 食品の「賞味期限」と「消費期限」 (縦・札と写真の解説) — canvas 1080x1920・editable profile 準拠 (縦の見本)

見せる文法: 編集可能モードの縦の作り — 上に見出し・中段に札 1〜2 枚・下に字幕の帯を空ける 3 段の画面 / 対比の札は def を per-instance の値で 2 枚並べる (×2) / preset と単純 object の入退場・`!` / `=` の印は書かない / count / run / group / sticky なし

```design.txt
#v2
# 計画: 明るい台所の地 (cream) に、賞味 = 緑 (a)・消費 = 赤 (b)。縦なので文字は上 1/3 に寄せ、下 1/4 は字幕の帯のために空ける
# editable: 動きは preset と単純 object
# 書体 太い丸ゴシック (見出し) + 太い等幅 (数字) + 細い角ゴシック (注記)
canvas 1080x1920 bg=#FBF7EF
lint profile=editable
palette a=#2E9E6A b=#D9483B bg=#FBF7EF ink=#2B2622 mute=#7A6F66 line=#E6DCCD card=#FFFFFF a_t=#2E9E6A1F b_t=#D9483B1F
font "太い丸ゴシック体、やさしく親しみやすい"
fonts e="太い等幅の数字が揃う書体" m="細い角ゴシック体、本文向き"
photo_style "明るい家庭の台所の写真、柔らかい自然光、清潔感、浅い被写界深度"
prompt_tail "文字なし、ロゴなし、ラベルの文字は読めない程度にぼかす"
motion title { in: fade {duration:0.55}; out: fade {duration:0.25} }
motion card { in: rise {duration:0.5}; out: fade {duration:0.22} }
motion note { in: fade {duration:0.4}; out: fade {duration:0.2} }
div { in: card; border-radius: 30px; background: $card; border: 3px solid $line }
cut { stagger: sentence }
def h1(t) = p(font-size: 84px; line-height: 1.2; color: $ink; text-align: center; in: title; content: {t})
def kick(t, c=$a) = p(font-size: 39px; font-family: e; color: {c}; letter-spacing: 0.15em; text-align: center; in: note; content: {t})
def sub(t) = p(font-size: 45px; font-family: m; color: $mute; text-align: center; in: note; content: {t})
# 期限の札: 色の帯 + 名前 + 意味 (×2 で並べる時は c と t を per-instance で)
def tag(t, m, c=$a) = div(width: 900px; height: 330px)
  div#band(left: 0px; top: 0px; width: 24px; height: 100%; border-radius: 12px; background: {c}; border: none)
  p#t(left: 72px; top: 54px; font-size: 72px; color: {c}; content: {t})
  p#m(left: 72px; top: 177px; width: 780px; font-size: 45px; font-family: m; color: $ink; content: {m})
subtitle.hug(font-size: 48px; bottom: 150px; background: #2B2622E6; color: #FBF7EF; border-radius: 15px; padding: 15px 36px)
bgm#music 明るく軽やかなアコースティックギターとピアノ、家庭的でやさしい、生活の豆知識の解説向け

section#open
img#op_p(left: 0px; top: 0px; width: 1080px; height: 1080px; main: kb {scale: [1, 1.06], focus: ['50% 55%', '50% 50%']}) [photo]冷蔵庫の扉を開けた中、牛乳パックとプリンと卵が並ぶ、明るい台所
kick#op_k(left: 90px; top: 1170px; width: 900px) FOOD LABEL BASICS
h1#op_h(left: 90px; top: 1242px; width: 900px; font-weight: 700) 「賞味期限」と[br]「消費期限」
sub#op_s(left: 90px; top: 1470px; width: 900px) 同じ「期限」でも、意味がちがう

section#pair
h1#pr_h(left: 90px; top: 240px; width: 900px; font-weight: 700) 2 つの期限
tag#pr_t(left: 90px; top: "540px;930px"; t: "賞味期限;消費期限"; m: "おいしく食べられる目安;安全に食べられる期限"; c: "$a;$b") ×2
sub#pr_s(left: 90px; top: 1320px; width: 900px) どちらも「開けずに、表示どおりに保存」が前提

section#best
img#bs_p(left: 0px; top: 0px; width: 1080px; height: 900px; main: kb {scale: [1, 1.05], focus: ['50% 50%', '']}) [photo]棚に並んだスナック菓子の袋と缶詰とカップ麺、明るい台所の棚
kick#bs_k(left: 90px; top: 990px; width: 900px) 賞味期限
h1#bs_h(left: 90px; top: 1062px; width: 900px; font-weight: 700) 傷みにくい食品
div#bs_c(left: 90px; top: 1290px; width: 900px; height: 210px; border: 3px solid $a; background: $a_t)
  p#t(left: 54px; cy: 50%; width: 792px; font-size: 48px; color: $ink) 過ぎても、すぐに食べられなくなるわけではない

section#use
img#us_p(left: 0px; top: 0px; width: 1080px; height: 900px; main: kb {scale: [1, 1.05], focus: ['50% 50%', '']}) [photo]パック入りのお弁当とサンドイッチと生菓子が並ぶ冷蔵ケース、明るい店内
kick#us_k(left: 90px; top: 990px; width: 900px; c: $b) 消費期限
h1#us_h(left: 90px; top: 1062px; width: 900px; font-weight: 700) 傷みやすい食品
div#us_c(left: 90px; top: 1290px; width: 900px; height: 210px; border: 3px solid $b; background: $b_t)
  p#t(left: 54px; cy: 50%; width: 792px; font-size: 48px; color: $ink) 過ぎたら、食べないのが安心

section#open_pack
h1#ok_h(left: 90px; top: 240px; width: 900px; font-weight: 700) 開けたら、[br]期限は関係なし
img#ok_p(left: 90px; top: 600px; width: 900px; height: 600px; border-radius: 30px; in: fade) [photo]封を開けた牛乳パックを冷蔵庫に戻す手元、明るい台所
sub#ok_s(left: 90px; top: 1290px; width: 900px) 表示の期限は「未開封」の話

section#close
kick#cl_k(left: 90px; top: 300px; width: 900px; c: $mute) まとめ
tag#cl_t(left: 90px; top: "480px;870px"; t: "賞味 = おいしさ;消費 = 安全"; m: "過ぎても、においや見た目を確かめて;過ぎたら、食べない"; c: "$a;$b") ×2
h1#cl_h(left: 90px; top: 1290px; width: 900px; font-size: 66px) 期限の意味を知って、[br]食べ物をむだなく
```

```timeline.txt
#v2
cast narrator = "やさしい30代女性のナレーター、明るく親しみやすい解説口調" speed=105%
transition = dissolve {duration: .3, overlap: .3, ease: 'power2.out'}

*** open
[>#subtitle]
bgm music
@narrator: [silence:+0.3s]食品のパッケージにある、[>#op_h]賞味期限と消費期限。
@: [>#op_s]どちらも同じ「期限」ですが、意味がちがいます。
# 台詞 2 文 ~8 s

*** pair
@narrator: [silence:+0.3s][>#pr_t[1]]賞味期限は、おいしく食べられる目安。
@: [>#pr_t[2]]消費期限は、安全に食べられる期限です。
@: [>#pr_s]どちらも、開けずに、表示どおりに保存したときの話です。
# 台詞 3 文 ~13 s

*** best
@narrator: [silence:+0.3s][>#bs_h]賞味期限が書かれるのは、お菓子や缶詰など、傷みにくい食品。
@: [>#bs_c]過ぎても、すぐに食べられなくなるわけではありません。
# 台詞 2 文 ~10 s

*** use
@narrator: [silence:+0.3s][>#us_h]消費期限が書かれるのは、お弁当やサンドイッチなど、傷みやすい食品。
@: [>#us_c]期限を過ぎたら、食べないのが安心です。
# 台詞 2 文 ~10 s

*** open_pack
@narrator: [silence:+0.3s]そして大事なのが、[>#ok_h]開けたあと。
@: [>#ok_p]封を開けたら、[>#ok_s]表示の期限に関係なく、早めに食べきりましょう。
# 台詞 2 文 ~9 s

*** close
@narrator: [silence:+0.3s]まとめると、[>#cl_t[1]]賞味期限は、おいしさの目安。[>#cl_t[2]]消費期限は、安全の期限。
@: [>#cl_h]期限の意味を知って、食べ物をむだなく使いましょう。[silence:2.0s]
# 台詞 2 文 ~11 s
```

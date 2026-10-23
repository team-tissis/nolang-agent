# concept · サルトルと「やりたいこと」(縦・線画・静かな語り) — canvas 1080x1920・49.8s・視聴者 90.0 (Gemini・vs hf)

見せる文法: manner・se・sticky・def・run・bgm 切替

```design.txt
#v2
# 計画: 明 (生成りの紙)・墨の文字・accent は煉瓦色 1 色 + 中間の砂色・書体 太い明朝 (見出し) + 細い角ゴシック (注記・札)
# 絵は全面のシンプルな線画イラスト (同じ若者が通しで出る)・上下に紙色の幕を敷いて文字を載せる・板は細い縁の札だけ
canvas 1080x1920 bg=#F3EEE4
theme light
palette a=#B5523B ink=#23262B paper=#F3EEE4 mute=#6F6A62 sand=#E4D8C4 line=#CFC3AE
font "太い明朝体、端正で知的な印象"
fonts m="細い角ゴシック体、静かで読みやすい本文向き"
art "シンプルで簡単な線画イラスト、細い墨色の線、生成りの紙の地、色は煉瓦色と淡い砂色を少しだけ、余白が多い、静かで知的"
prompt_tail "文字を描かない、ロゴなし"
image yo = "白いシャツに紺のズボンの20代の若者、短い黒髪、穏やかな表情、シンプルな線画"
motion title { in: {y:-36, opacity:0, duration:0.7, ease:'power3.out'}; out: fade {duration:0.3} }
motion big { in: {scale:0.92, opacity:0, duration:0.6, ease:'power3.out'}; out: fade {duration:0.3} }
motion div { in: {y:27, opacity:0, duration:0.6, ease:'power3.out'}; out: fade {duration:0.26} }
motion row { in: {x:-45, opacity:0, duration:0.5, ease:'power3.out'}; out: fade {duration:0.24} }
motion note { in: {opacity:0, duration:0.45, ease:'power2.out'}; out: fade {duration:0.24} }
div { border-radius: 21px; border: 3px solid $line; background: #FBF8F2; in: div }
cut { stagger: sentence }
run a { color: $a }
run m { marker: #B5523B40 }
def kick(t) = p(font-size: 36px; font-family: m; color: $a; letter-spacing: 0.2em; in: note; content: {t})
def h1(t) = p(font-size: 87px; line-height: 1.25; color: $ink; in: title; content: {t})
def body(t) = p(font-size: 54px; font-family: m; color: $ink; in: row; content: {t})
def note(t) = p(font-size: 42px; font-family: m; color: $mute; in: note; content: {t})
def chip(t) = p(font-size: 54px; color: $ink; background: #FBF8F2; border: 3px solid $line; border-radius: 148px; padding: 15px 42px; in: pop; content: {t})
subtitle.hug(font-size: 48px; font-family: m; bottom: 60px; background: #23262BE6; color: $paper; border-radius: 15px; padding: 15px 36px; line-height: 1.4)
bgm#music 静かなピアノのミニマルな曲、ゆっくりした単音と柔らかいパッド、知的で落ち着いた解説向け
bgm#music2 同じ静かなピアノに柔らかいストリングスが加わり少しだけ前向きに広がる曲、穏やか

section#hook
img#h_bg(inset: 0; main: kb {scale: [1, 1.05], focus: ['50% 50%', '50% 45%']}) [ref:@yo]同じ若者が二つに分かれた小道の前で立ち止まり、あごに手を当てて考えている、全身、画面の中ほど
veil#h_vt(color: $paper; opacity: 0.95; to: top; start: 0.7)
veil#h_vb(color: $paper; opacity: 0.95; to: bottom; start: 0.6)
kick#h_k(left: 72px; top: 144px) 選ぶ順番
h1#h_h(left: 72px; top: 210px; font-weight: 700) この順番、[br]{a}逆{/}かもしれない
chip#h_o1(left: 72px; top: 1350px; width: 375px; text-align: center) 見つかる
shape#h_ar(left: 480px; top: 1383px; width: 120px; height: 60px; path: arrow_r,head=line; background: none; border: 4px solid $ink; in: wipe {dir: 'right', duration: 0.5})
chip#h_o2(left: 633px; top: 1350px; width: 375px; text-align: center) 選ぶ
note#h_n(left: 72px; top: 1515px) やりたいこと → 選択

section#worry
img#w_bg(inset: 0; main: kb {scale: [1.04, 1], focus: '50% 45%'}) [ref:@yo]同じ若者が求人票の束を両手に持って首をかしげている、頭の上に小さな疑問符が三つ、上半身
veil#w_vt(color: $paper; opacity: 0.95; to: top; start: 0.7)
veil#w_vb(color: $paper; opacity: 0.95; to: bottom; start: 0.6)
kick#w_k(left: 72px; top: 144px) 就職の迷い
h1#w_h(left: 72px; top: 210px; font-weight: 700) やりたいことが[br]{a}ない{/}まま
div#w_c(left: 72px; top: 1335px; width: 936px; height: 195px)
  icon#i(left: 48px; cy: 50%; font-size: 84px; name: question; color: $a)
  p#t(left: 165px; cy: 50%; font-size: 54px; font-family: m; color: $ink) 迷う人は、{m}多い{/}のでは

section#sartre
img#s_bg(inset: 0; main: kb {scale: [1, 1.05], focus: ['50% 50%', '40% 50%']}) [ref:@yo]丸眼鏡をかけた年配の哲学者風の男性と同じ若者がカフェの小さなテーブルで向かい合って話している、横からの構図
veil#s_vt(color: $paper; opacity: 0.95; to: top; start: 0.7)
veil#s_vb(color: $paper; opacity: 0.96; to: bottom; start: 0.55)
kick#s_k(left: 72px; top: 144px) JEAN-PAUL SARTRE
h1#s_h(left: 72px; top: 210px; font-weight: 700) サルトル
div#s_q(left: 72px; top: 1170px; width: 630px; height: 144px)
  p#t(left: 42px; cy: 50%; font-size: 54px; color: $ink) {s}気持ちで決める{/}
note#s_qn(left: 726px; top: 1218px) 教え子の言葉
chip#s_a(left: 72px; top: 1350px; width: 330px; text-align: center) 行動
shape#s_ar(left: 432px; top: 1383px; width: 165px; height: 60px; path: arrow_r,head=line; background: none; border: 4px solid $a; in: wipe {dir: 'right', duration: 0.6})
chip#s_b(left: 627px; top: 1350px; width: 381px; text-align: center) 気持ち
body#s_c(left: 72px; top: 1500px) だから、{a}手引き{/}にならない

section#study
img#st_bg(inset: 0; main: kb {scale: [1.05, 1], focus: '50% 55%'}) [ref:@yo]同じ若者が虫眼鏡で足元の一点だけをのぞき込んでいる、周りには気づかれない小さな花や本や楽器が点々と置かれている、引きの構図
veil#st_vt(color: $paper; opacity: 0.95; to: top; start: 0.7)
veil#st_vb(color: $paper; opacity: 0.95; to: bottom; start: 0.6)
kick#st_k(left: 72px; top: 144px) ある研究
h1#st_h(left: 72px; top: 210px; font-weight: 700) 興味は{a}見つけるもの{/}、[br]と考える人ほど
note#st_l(left: 72px; top: 1320px) 興味の幅
shape#st_bar(left: 72px; top: 1392px; width: 936px; height: 42px; path: rect,r=0.5; background: $sand; border: none; in: wipe {dir: 'right', duration: 0.7})
shape#st_core(left: 441px; top: 1392px; width: 198px; height: 42px; path: rect,r=0.5; background: $a; border: none; in: fade {duration: 0.4})
body#st_c(left: 72px; top: 1485px) {a}狭い{/}傾向があった

section#concl
img#c_bg(inset: 0; main: kb {scale: [1, 1.06], focus: ['50% 55%', '50% 50%']}) [ref:@yo]同じ若者がしゃがんで小さな鉢の苗に水差しで水をやっている、芽が少し伸びている、穏やかな朝
veil#c_vt(color: $paper; opacity: 0.96; to: top; start: 0.65)
veil#c_vb(color: $paper; opacity: 0.96; to: bottom; start: 0.55)
kick#c_k(left: 72px; top: 144px) 結論
h1#c_h(left: 72px; top: 210px; font-weight: 700) やりたいことは、[br]選ぶ前の{a}条件{/}にできない
div#c_r1(left: 72px; top: 1200px; width: 936px; height: 144px)
  p#t(left: 48px; cy: 50%; font-size: 51px; font-family: m; color: $mute) {x}意識が向く → 関わる{/}
div#c_r2(left: 72px; top: 1374px; width: 936px; height: 165px; border: 4px solid $a)
  p#t(left: 48px; cy: 50%; font-size: 60px; color: $ink) 関わる → {a}意識が向く{/}
#c_r2.on(background: #F6E3DC)

section#close
img#cl_bg(inset: 0; main: kb {scale: [1, 1.07], focus: ['50% 50%', '50% 45%']}) [ref:@yo]同じ若者が少し開いた扉の前で一歩を踏み出そうとしている、扉の向こうから柔らかい光、後ろ姿
veil#cl_vt(color: $paper; opacity: 0.95; to: top; start: 0.7)
veil#cl_vb(color: $paper; opacity: 0.95; to: bottom; start: 0.6)
h1#cl_h(left: 72px; top: 180px; font-weight: 700) 見つかったら選ぶ、[br]で止めていませんか
shape#cl_rule(left: 72px; top: 1380px; width: 180px; height: 4px; path: line_h; background: $a; border: 4px solid $a; in: wipe {dir: 'right', duration: 0.7})
body#cl_n(left: 72px; top: 1425px) まず一つ、{a}関わって{/}みる
```

```timeline.txt
#v2
cast narrator = "落ち着いた40代男性のナレーター、低めで穏やか、知的で静かな語り口" speed=100%
transition = dissolve,300,overlap=300

*** hook
[>#subtitle]
bgm music
se "屋外の静かな風の音、遠くの鳥" -8dB to=7s fade=300,1500
@narrator: [silence:+0.3s][>#h_o1]やりたいことが[>#h_ar]見つかってから[>#h_o2][>#h_n +300]選ぶ。[silence:0.4s]
@: [>#h_h][>#h_k]この順番、[!#h_o1 to,{x:561, duration:0.9, ease:'power2.inOut', arc:0.3}][!#h_o2 to,{x:-561, duration:0.9, ease:'power2.inOut', arc:-0.3}][!#h_n text,"選択 → やりたいこと"]逆かもしれません。[silence:0.8s]

*** worry
@narrator: [silence:+0.3s][>#w_h]やりたいことがないまま、[>#w_c]就職で迷う人は[!#w_c.t{m} marker,$a]多いのではないでしょうか。[!#w_c.i pulse][silence:0.4s]
transition dissolve,300,overlap=300

*** sartre
se "静かなカフェの環境音、遠くの食器の音" -8dB to=15s fade=300,1500
@narrator: [silence:+0.3s][>#s_h]サルトルは、[>#s_q]気持ちで決めると言った[>#s_qn]教え子の話をしています。
@: サルトルの考えを要約すると、[>#s_b]気持ちは[>#s_a]行動で[>#s_ar]形づくられるので、[!#s_q.t{s} strike,$a][>#s_c]行動の手引きにはできない。[silence:0.4s]

*** study
@narrator: [silence:+0.3s][>#st_k]ある研究では、[>#st_h]興味は見つけるものと考える人ほど、[>#st_l]興味の幅が[!#st_bar to,{scaleX:0.3, duration:0.9, ease:'power2.inOut'}][!#st_bar recolor,$line]狭い[>#st_c]傾向がありました。[silence:0.4s]
transition dip,400
[<#music]

*** concl
bgm music2 -1500
se "朝の庭の静かな環境音、小鳥のさえずり" -8dB to=13s fade=300,1500
@narrator: [silence:+0.3s]結論は、[>#c_h]やりたいことを、選ぶ前の[!#c_h{a} underline,$a +300]条件にはできない、ということ。[silence:0.5s]
@: [>#c_r1]意識が向いてから関わるのではなく、[!#c_r1.t{x} strike,$a][>#c_r2]関わるから[♪"水差しで鉢に水をそそぐ音" -6dB][!#c_r2 .on][!#c_r2.t{a} marker,#B5523B40]意識が向く。[silence:0.5s]

*** close
@narrator: [silence:+0.3s][>#cl_h]見つかったら選ぶ、で止めているものは[>#cl_rule]ありますか。[>#cl_n +600][silence:3.0s]
```

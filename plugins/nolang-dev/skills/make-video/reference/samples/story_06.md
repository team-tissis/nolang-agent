# story · ニホンカワウソ (縦・台本そのまま・絵本調) — canvas 720x1280・57.8s・視聴者 86.0 (Gemini・vs hf)

見せる文法: ×N・stack・manner・se・sticky・def・run・bgm 切替

```design.txt
#v2
# 計画: 明るい和紙の生成りの地 + 水彩の絵本の全面の絵・主色は川の青緑・差し色は錆の朱 (1979 と失われた物)
# 書体 太い明朝 (見出し・縦書きの名) + 太い角ゴシック (字幕・札) + セリフの欧文 (学名・番号・年号)
# 文字は上 1/3 に置き、上だけ生成りの幕で絵から浮かせる・字幕は下端の墨の札
canvas 720x1280 bg=#F4EEE2
theme light
palette a=#2F6F73 b=#B5532F ink=#2A2622 paper=#F4EEE2 mute=#6E665C
font "太い明朝体、端正で文学的な印象"
fonts s="太い角ゴシック体、読みやすい" e="端正なセリフ体の欧文、クラシックな書籍風"
art "やわらかい水彩画の絵本のイラスト、和紙の質感、淡くにじむ色、繊細な鉛筆の線、郷愁のある光"
prompt_tail "文字を描かない、ロゴなし"
image otter = "ニホンカワウソ、こげ茶色の短く濡れた毛、白っぽい喉、丸い小さな耳、長いひげ、つぶらな黒い目、可愛らしい表情"
motion title { in: {y:-24, opacity:0, duration:0.7, ease:'power3.out'}; out: fade {duration:0.3} }
motion big { in: {scale:0.92, opacity:0, duration:0.6, ease:'power3.out'}; out: fade {duration:0.3} }
motion div { in: {y:18, opacity:0, duration:0.6, ease:'power3.out'}; out: fade {duration:0.26} }
motion row { in: {x:-30, opacity:0, duration:0.5, ease:'power3.out'}; out: fade {duration:0.24} }
motion note { in: {opacity:0, duration:0.45, ease:'power2.out'}; out: fade {duration:0.24} }
lint off=duplicate_text
cut { stagger: sentence }
img { main: kb {scale: [1, 1.06]} }
run a { color: $a }
run b { color: $b }
sfx off
subtitle.hug(font-size: 32px; font-family: s; bottom: 56px; background: #2A2622E6; color: $paper; border-radius: 10px; padding: 10px 22px; line-height: 1.35)
bgm#music(volume: 4dB) 静かなピアノと柔らかい弦、郷愁のある素朴な旋律、自然ドキュメンタリーの語り向け
bgm#music2(volume: 4dB) 余韻の長いピアノの独奏、まばらな音、喪失と追憶の静かな曲
def kick(t) = p(font-size: 22px; font-family: e; color: $a; letter-spacing: 0.2em; in: fade {duration: 0.7}; content: {t})
def h1(t) = p(font-size: 52px; line-height: 1.3; color: $ink; in: title; content: {t})
def rule = shape(width: 96px; height: 3px; path: line_h; background: $a; border: 3px solid $a; in: wipe {dir: 'right', duration: 0.7})

section#hook
img#hk_p(inset: 0; main: kb {scale: [1, 1.12], focus: ['50% 65%', '50% 62%']}) [ref:@otter]澄んだ川面から顔を出してこちらを見つめるニホンカワウソの顔の寄り、水滴、木漏れ日の光、画面の下半分に顔
veil#hk_v(color: #F4EEE2; opacity: 0.9; to: top; start: 0.5)
kick#hk_k(left: 48px; top: 88px) SHOWA ERA — JAPAN
rule#hk_r(left: 48px; top: 128px)
h1#hk_h(left: 48px; top: 156px) 昔、日本の{a}川{/}には

section#name
img#nm_p(inset: 0) [ref:@otter]緑の澄んだ川を水中で体を伸ばして泳ぐニホンカワウソの全身の横からの引き、泡の筋、川底の小石、画面の左下寄り
veil#nm_v(color: #F4EEE2; opacity: 0.85; to: top; start: 0.45)
kick#nm_k(left: 48px; top: 88px) Lutra nippon
rule#nm_r(left: 48px; top: 128px)
div#nm_c(left: 584px; top: 72px; width: 96px; height: 560px; background: #F4EEE2E6; border-radius: 4px; border: 2px solid $a; in: mask_rise)
  p#t(cx: 50%; cy: 50%; font-size: 64px; writing-mode: vertical-rl; text-align: center; color: $ink) ニホンカワウソ
p#nm_s(left: 48px; top: 160px; width: 480px; font-size: 36px; line-height: 1.5; color: $ink; in: rise) 川を泳ぎ、[br]魚を追いかけ

section#life
img#lf_p(inset: 0; main: kb {scale: [1.08, 1], focus: '50% 55%'}) 昭和の田舎の小川、石段で野菜を洗う着物姿の女性と、すぐそばの岩の上で魚をくわえたニホンカワウソ、夏の午後の光、茅葺きの家
veil#lf_v(color: #F4EEE2; opacity: 0.9; to: top; start: 0.45)
kick#lf_k(left: 48px; top: 88px) NEIGHBORS
rule#lf_r(left: 48px; top: 128px)
h1#lf_h(left: 48px; top: 156px) 日本人の[br]{a}すぐそば{/}で

section#vanish
img#vn_p(inset: 0; main: kb {scale: [1, 1.06], focus: '40% 50%'}) 夕暮れの誰もいない川岸、葦と濡れた岩、水面に長い影、寂しい空気
veil#vn_v(color: #F4EEE2; opacity: 0.9; to: top; start: 0.45)
kick#vn_k(left: 48px; top: 88px) FADING
rule#vn_r(left: 48px; top: 128px)
h1#vn_h(left: 48px; top: 156px; font-size: 46px) その姿は[br]少しずつ{b}消えて{/}いく

section#causes
img#cz_p(inset: 0; main: kb {scale: [1, 1.08], focus: ['50% 60%', '']}) コンクリートの護岸で固められた濁った川、遠くに工場の煙突と重機、灰色の空、生き物の気配のない水面
veil#cz_v(color: #F4EEE2; opacity: 0.9; to: top; start: 0.55)
kick#cz_k(left: 48px; top: 88px) WHY THEY VANISHED
rule#cz_r(left: 48px; top: 128px)
div#cz(left: 48px; top: 160px; width: 440px; height: 344px; gap: 12; background: #F4EEE2F0; border-radius: 8px; box-shadow: 0px 4px 12px #2A262233; in: {x:-30, opacity:0, duration:0.5, ease:'power3.out'}; display: flex; flex-direction: column) ×4
  p#n(left: 20px; cy: 50%; font-size: 26px; font-family: e; color: $b) 01;02;03;04
  p#t(left: 72px; cy: 50%; font-size: 32px; font-family: s; color: $ink) 毛皮をとるために;川の開発;水の汚れ;餌の魚が減る

section#last
img#ls_p(inset: 0; main: kb {scale: [1, 1.05], focus: '50% 45%'}) 夕暮れの高知の山あいの清流、青い山並みと赤く染まる空、静かな淵、誰もいない
veil#ls_v(color: #F4EEE2; opacity: 0.9; to: top; start: 0.5)
kick#ls_k(left: 48px; top: 88px) KOCHI PREFECTURE
rule#ls_r(left: 48px; top: 128px)
p#ls_n(left: 40px; top: 140px; font-size: 150px; font-family: e; color: $ink; letter-spacing: 0.02em; in: mask_rise) 1979
p#ls_t(left: 48px; top: 330px; font-size: 34px; font-family: s; color: $ink; in: rise) 高知県で{b}最後{/}の確認

section#memory
img#mm_p(inset: 0; main: kb {scale: [1.06, 1]}) [ref:@otter]色褪せた古い写真のような、岩の上でこちらを振り返るニホンカワウソ、セピア色、白い縁、時間の経った紙のしみ
veil#mm_v(color: #F4EEE2; opacity: 0.9; to: top; start: 0.5)
kick#mm_k(left: 48px; top: 88px) ONLY IN MEMORY
rule#mm_r(left: 48px; top: 128px)
p#mm_s(left: 48px; top: 156px; font-size: 32px; font-family: s; color: $mute; in: fade {duration: 0.7}) たった数十年で
h1#mm_h(left: 48px; top: 212px; font-size: 50px) {b}記憶{/}の中だけの[br]存在に

section#ending
img#ed_p(inset: 0; main: kb {scale: [1, 1.1], focus: ['50% 60%', '50% 55%']}) [ref:@otter]朝の光が差し込む澄んだ川を、背を向けて上流へ泳いでいくニホンカワウソ、水面のきらめき、緑の木々、希望のある静けさ
veil#ed_v(color: #F4EEE2; opacity: 0.85; to: top; start: 0.45)
kick#ed_k(left: 48px; top: 88px) IF WE COULD RETURN
rule#ed_r(left: 48px; top: 128px)
h1#ed_h(left: 48px; top: 156px; font-size: 46px) あの日の{a}川{/}に[br]戻れたなら
```

```timeline.txt
#v2
cast n = "落ち着いた30代女性のナレーター、やさしく語りかける、少し郷愁を帯びた調子" speed=100%
transition = dissolve,300,overlap=300

*** hook
[>#subtitle]
bgm music
se "山あいの小川のせせらぎ、遠くの鳥の声" -8dB to=6s fade=300,1500
@n: [silence:+0.3s]昔、日本の川には……[silence:0.5s][!#hk_p zoom_media,1.1]この可愛い動物が普通にいたんです。[silence:0.4s]

*** name
se "川の水中の泡の音と水のはねる音" -8dB to=5s fade=300,1200
@n: [silence:+0.3s][>#nm_c]ニホンカワウソ。[silence:0.4s]
@: [>#nm_s]川を泳ぎ、[♪"水に飛び込む" -8dB]魚を追いかけ、

*** life
se "夏の田舎の川辺の環境音、せせらぎと蝉の声" -8dB to=5s fade=300,1200
@n: [silence:+0.2s][>#lf_h]日本人の[!#lf_h{a} underline,$a]すぐそばで暮らしていました。[silence:0.5s]

*** vanish
se "夕暮れの川辺に吹く寂しい風の音" -8dB to=6s fade=300,1500
@n: [silence:+0.3s]でも、いつからか、[>#vn_h]その姿は少しずつ[!#vn_p gray,duration=1800]消えていきます。[silence:0.6s]
transition wipe,600,dir=left

*** causes
se "遠くの工事現場の重機の低い音" -10dB to=9s fade=300,1500
@n: [silence:+0.3s][>#cz[1]]毛皮をとるために捕まえられ、
@: [>#cz[2]]川は開発され、
@: [>#cz[3]]水が汚れ、[>#cz[4]]餌となる魚も[!#cz_p gray,duration=1500]減っていきました。[silence:0.6s]
transition dip,400
[<#music -400]

*** last
se "夕暮れの静かな清流の音、ひぐらしの声" -8dB to=10s fade=500,2000
@n: [silence:+0.4s]そして[>#ls_n]1979年。[silence:0.5s]
@: [>#ls_t]高知県で[!#ls_t{b} underline,$b]最後に確認されたニホンカワウソを最後に、姿を見た人は[!#ls_n recolor,$b,duration=900]いなくなりました。[silence:0.8s]

*** memory
bgm music2 -1500
se "静かな風の音" -10dB to=8s fade=500,2000
@n: [silence:+0.3s]かつては日本中にいた動物が、
@: [>#mm_s]たった数十年で、[>#mm_h]私たちの[!#mm_h{b} underline,$b]記憶の中だけの存在になったのです。[silence:0.8s]
transition dissolve,300,overlap=300

*** ending
se "朝の澄んだ川のせせらぎと小鳥のさえずり" -8dB to=10s fade=500,2500
@n: [silence:+0.4s][>#ed_h]もし、あの日の川に戻れたなら――[silence:0.5s]
@: そこには今も、[!#ed_p zoom_media,1.1,duration=2500]カワウソが泳いでいるのでしょうか。[silence:3.0s]
```

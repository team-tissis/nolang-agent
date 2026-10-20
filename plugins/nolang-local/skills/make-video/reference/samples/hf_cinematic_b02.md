# cinematic · classroom-morning (hf 全力版の全量の写し — 爽やかな朝の高校の教室・一問一答クイズの途中に流れる気まずくも甘酸っぱい沈黙・語りの無い 5 人の掛け合いを 13 ショットの実写ドラマで) — canvas 1280x720

見せる作り: 語りの無い 5 人の掛け合い (役ごとの cast と台詞ごとの話し方)・13 ショットを 6 cut に畳む硬い切替と、cut の中で語 / 無音の間に替える絵・全編の映画の質感 (上下の黒帯・窓明かりの漏れ・暖色と寒色の色の幕・漂う塵・周辺減光・grain)・下の黒帯の中の字幕・基準画像 2 枚から派生させて揃える人物と教室・ショットごとの寄りとパン (kb)・立ち上がりの持ち上がりと揺れ・凍る沈黙で止まる曲と秒針・音の層 (スズメの場の音 + 足音・椅子・秒針・紙・チャイム)・黒から明けて黒へ

```design.txt
#v2
# 学ぶ作り: 実写の短編ドラマ (語りなし・5 人の掛け合い) の 13 ショットを 6 cut に畳む — cut の境目は硬い切替 (切替を書かない)・cut の中のショット替えは台詞の語か無音 [silence] の間の印 [>#次の絵][<#前の絵] で
# 台詞の無い間 (立ち上がる・視線の交差・凍る沈黙) も無音の長さとショットで演じる。寄り・パンはショットごとの kb (倍率と動かない点)・立ち上がりは keys の持ち上がり + 揺れ
# 全編の映画の質感は常設の層 (z-index: front): 窓明かりの漏れ (screen で呼吸)・上が暖かく下が冷たい色の幕・漂う塵・周辺減光・動く grain・上下の黒帯 (シネスコ)。字幕は下の黒帯の中に細い角ゴシックで
# 人物と教室は基準画像 (4 人の席の組 seats・戻ってくるえり eri — 立つルキ stand・えりの寄り eri_face・5 人の再開 five もここから) から [ref:@名] で派生させて揃える。音は台詞 + 曲 (凍る沈黙で止めて別の箇所から再開) + 場の音 (スズメ) + 動作の foley
# hf b02 classroom-morning (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1280x720 bg=#000000
theme dark
palette a=#FFD096 sub=#F3EFE6 mote=#FFF6E4
font "すっきりした細めの角ゴシック体、映画の字幕向け"
sfx off
# hf の作り: 最後の笑い声「あははっ」には字幕を出さない・締めは文字の札でなく笑顔の寄りの 1 枚で終える
lint off=caption_gap,no_closer
art "Photorealistic cinematic film still from a contemporary Japanese live-action youth drama film. Shot on ARRI Alexa Mini with a 35mm prime lens, shallow depth of field, subtle 35mm film grain, natural skin texture, realistic anatomy and hands, understated natural acting, warm golden highlights with soft cool shadows."
prompt_tail "Setting: a clean, bright Japanese high school classroom in the early morning before homeroom - green chalkboard at the front, rows of light wooden desks with grey steel frames neatly aligned, cream-colored walls, white curtains, large aluminum-framed windows along one side. Natural soft morning sunlight pouring in through the windows, gentle haze and floating dust particles in the light beams. No text overlays, no captions, no subtitles, no watermark, no logos."
# 絵は hf の色の整え (コントラスト 1.05・彩度 0.93) を全部に・退場は書いた物だけ
img { filter: sat:0.93,contrast:1.05; out: none }
div { border: none; box-shadow: none; padding: 0px; border-radius: 0px; out: none }
# 基準画像: 4 人の席の組 (ルキ・男子 A・女子 A・女子 B) と戻ってくるえり。他のショットはこの 2 枚 (と派生の 3 枚) から作る
image seats = "[photo]Characters: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Boy A: a 17-year-old Japanese boy with very short black hair, wearing a navy-blue polo shirt and navy-blue trousers. Girl A: a 17-year-old Japanese girl with long black hair tied in a low ponytail, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Girl B: a 17-year-old Japanese girl with a chin-length black bob, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Shot: medium-wide shot from the front of the classroom at seated eye level, facing the students, the windows are on the right side of the frame and sunlight streams in from the right. Ruki sits at the desk in the exact center of the frame, holding a plain white A4 printout (a biology question-and-answer quiz sheet with small printed lines) in both hands, looking to his left (toward frame right) at Girl A with a playful grin as he reads out a question. Boy A sits at the desk in front of Ruki, in the left foreground slightly off-center, and has twisted around in his chair to face Ruki, one arm hooked over the backrest, laughing. Girl A sits at the desk immediately to Ruki's left (frame right, next to the window), leaning toward him and answering with a bright laugh, one hand half raised. Girl B sits at the desk diagonally behind Ruki on his left (frame right, one row back), leaning forward over her desk with a big smile. All four are happily playing a quiz together, relaxed and natural, genuine laughter. The other desks are neat and empty." aspect=16:9
image eri = "[photo]Character: Eri: a 17-year-old Japanese girl with shoulder-length straight black hair and soft bangs, wearing a white short-sleeve collared blouse under a navy-blue knitted school vest, and a navy-blue pleated skirt. Shot: medium shot of Eri walking back down the sunlit aisle between the desks toward the camera, returning to her seat. The windows are on the right side of the frame, bright window light creates a soft golden rim light on her hair and shoulder. She holds a small folded handkerchief in one hand, a calm, relaxed expression, just about to notice something ahead of her. Shallow depth of field with blurred desks in the foreground and background." aspect=16:9
image stand = "[photo][ref:@seats][ref:@eri]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Characters: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Eri: a 17-year-old Japanese girl with shoulder-length straight black hair and soft bangs, wearing a white short-sleeve collared blouse under a navy-blue knitted school vest, and a navy-blue pleated skirt. Boy A: a 17-year-old Japanese boy with very short black hair, wearing a navy-blue polo shirt and navy-blue trousers. Girl A: a 17-year-old Japanese girl with long black hair tied in a low ponytail, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Shot: medium shot. Ruki is in the middle of hastily getting up from the chair at the center desk - knees still slightly bent, the chair scraping back - holding the white A4 printout against his chest with one hand, the other hand raised in a small apologetic gesture, with an awkward, embarrassed wry smile (a bashful 'oh, sorry!' grimace-smile, eyebrows slightly raised), looking toward Eri, who stands in the aisle at the left edge of the frame, seen from behind and out of focus (white blouse, navy knit vest). Girl A watches from her desk by the window on the right, Boy A at the left edge. Window light from frame right." aspect=16:9
image eri_face = "[photo][ref:@eri][ref:@seats]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Character: Eri: a 17-year-old Japanese girl with shoulder-length straight black hair and soft bangs, wearing a white short-sleeve collared blouse under a navy-blue knitted school vest, and a navy-blue pleated skirt. Shot: close-up of Eri standing still in the aisle, slightly surprised, lips softly parted, eyes fixed on Ruki who is just off-camera to frame right, the faintest blush, natural and subtle. Soft morning backlight through her hair, creamy bokeh of the sunny classroom behind her." aspect=16:9
image five = "[photo][ref:@seats][ref:@eri]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Characters: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Eri: a 17-year-old Japanese girl with shoulder-length straight black hair and soft bangs, wearing a white short-sleeve collared blouse under a navy-blue knitted school vest, and a navy-blue pleated skirt. Boy A: a 17-year-old Japanese boy with very short black hair, wearing a navy-blue polo shirt and navy-blue trousers. Girl A: a 17-year-old Japanese girl with long black hair tied in a low ponytail, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Girl B: a 17-year-old Japanese girl with a chin-length black bob, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Shot: medium-wide shot. Eri is now seated at the center desk, Ruki stands right beside her desk holding up the white A4 biology quiz printout and reading the next question with a slightly embarrassed but warm smile. Boy A (turned around in front), Girl A (by the window) and Girl B (behind) lean in, and all five are breaking from shy, awkward smiles into genuine laughter. Eri smiles shyly, looking up at the printout. Bright warm morning sunlight from the windows on the right, joyful and natural." aspect=16:9
bgm#music(duck: -7; fade: 1400,160) 温かく穏やかで少し切ない、ゆっくりしたピアノソロのポップ、68 BPM、青春の日常や回想の場面向け
# 凍る沈黙の後に同じ曲を別の箇所 (句の終わり) から入れ直す
bgm#music_b(duck: -7; fade: 1000,1100) 温かく穏やかで少し切ない、ゆっくりしたピアノソロのポップ、68 BPM、青春の日常や回想の場面向け
# 字幕: 下の黒帯の中央に細い角ゴシックの生成り色・黒の柔らかい影・板なし・札は文ごとに 0.12 秒で出入り
subtitle(left: 0px; top: 651px; width: 1280px; height: 69px; font-size: 24px; letter-spacing: 0.08em; color: $sub; background: none; text-align: center; align-items: center; text-shadow: 0px 0px 5px #000000CC; unit: sentence; lead: 0; tail: 0; hold: off; in: {opacity:0, duration:0.12, ease:'none'}; out: {opacity:0, duration:0.12, ease:'none'})
# 全編の質感 (常設・最前面の段・書いた順に重なる)
# 窓明かりの漏れ: 右上の暖色の光を screen で重ねてゆっくり呼吸させる (hf はショットごとに 0.55 → 0.85 → 0.6)
div#leak_r(inset: 0; background: radial(#FFD0968C,#FFD09633@45%,#FFD09600@100%,82%,18%); blend: screen; opacity: 0.7; z-index: front; in: none; main: sine,opacity=0.15,freq_ms=4400)
# 色の幕: 上が暖かく下が冷たい (soft-light で重ねる)
div#grade(inset: 0; background: linear(#FFD2A038,#FFECD20F@45%,#1E3C5A29,180); mix-blend-mode: soft-light; z-index: front; in: none)
# 窓の光の中を漂う塵 22 粒 (黒帯の内側・ゆっくり右上へ)
particles#motes(left: 0px; top: 93px; width: 1280px; height: 534px; n: 22; dot: 3-8; color: $mote; opacity: 0.3; drift: random,dx=-40..60,dy=-80..-20; speed: 3; seed: 5; z-index: front)
veil#vignette(background: radial(#00000000@55%,#00000066@100%,50%,50%); z-index: front; in: none)
veil#grain(grain: 0.075; color: #00000000; mix-blend-mode: overlay; z-index: front; in: none; main: noise,x=4,y=4,freq_ms=83)
# 上下の黒帯 (シネスコ・hf の 104 px)
div#bar_top.bleed(left: -4px; top: -4px; width: 1288px; height: 73px; background: #000000; z-index: front; in: none)
div#bar_bottom.bleed(left: -4px; top: 651px; width: 1288px; height: 73px; background: #000000; z-index: front; in: none)

# 出題: 揺れるカーテンの差し込み → 0.25 秒で溶けて教室の全景 (この 1 枚だけ漏れの光が左) → 「細胞」でルキの寄り
section#quiz
img#curtain(inset: 0; main: kb,1.05@52%,50%>1.1@35%,50%,ease=sine.inOut) [photo]Shot: close-up insert of a white classroom curtain gently swaying in the morning breeze at a half-open window, bright sunlight glowing through the thin fabric, floating dust in the light, out-of-focus green trees outside, a quiet and still mood. No people.
img#establish(inset: 0; in: {opacity:0, duration:0.25, ease:'none'}; main: kb,1.03@50%,45%>1.08@64%,52%,ease=sine.inOut) [photo][ref:@seats]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Characters: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Boy A: a 17-year-old Japanese boy with very short black hair, wearing a navy-blue polo shirt and navy-blue trousers. Girl A: a 17-year-old Japanese girl with long black hair tied in a low ponytail, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Girl B: a 17-year-old Japanese girl with a chin-length black bob, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Shot: wide establishing shot of the same classroom from the back corner near the door, looking diagonally toward the front and the windows, which are on the left side of the frame. Sunlight floods in through the windows, long soft shadows of the desks stretch across the floor, the white curtains glow. In the middle distance the same four students are gathered around the center desk, small in the frame, laughing (Ruki in the light-blue shirt holding the white printout, Boy A turned around, Girl A and Girl B leaning in). Many neat empty desks in the foreground. Calm, fresh, luminous morning atmosphere.
div#leak_l(inset: 0; background: radial(#FFD0968C,#FFD09633@45%,#FFD09600@100%,18%,18%); blend: screen; opacity: 0.7; in: {opacity:0, duration:0.25, ease:'none'})
img#ruki_quiz(inset: 0; main: kb,1.04@55%,7%>1.1@55%,30%,ease=sine.inOut) [photo][ref:@seats]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Character: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Shot: medium close-up of Ruki (the boy in the light-blue short-sleeve shirt from the reference) seated at the desk, holding the plain white A4 biology quiz printout in front of his chest, looking to his left (toward frame right) with a cheerful, playful smile as he asks a question. Camera at eye level from the front, window light from frame right with soft fill. The classroom behind him is softly out of focus, with Girl B faintly visible in the background bokeh.

# 答え: 4 人の組を横へパン → 「思った」で廊下側から戻ってくるえり (足音)
section#answer
img#group_shot(inset: 0; content: @seats; main: kb,1.07@31%,37%>1.07@69%,37%,ease=sine.inOut)
img#eri_walk(inset: 0; content: @eri; main: kb,1.02@40%,0%>1.1@40%,34%,ease=sine.inOut)

# 気づく: 慌てて立ち上がるルキ (絵が下から持ち上がって少し行き過ぎ、椅子の音と同時に 2 px 揺れる) → 無音の間に えりの寄り → ルキの寄り (視線の交差)
section#sorry
img#ruki_stand(inset: 0; content: @stand; main: keys(at=0 scale=1.08 y=31 | at=0.323 scale=1.08 y=-5 ease=power3.out | at=1 scale=1.08 y=0 ease=sine.inOut),window=0,1920,forwards,pivot=55%,35%)
img#eri_close(inset: 0; content: @eri_face; main: kb,1.05@40%,35%>1.085@40%,35%,ease=sine.inOut)
img#ruki_close(inset: 0; main: kb,1.05@58%,28%>1.085@58%,28%,ease=sine.inOut) [photo][ref:@seats][ref:@stand]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Character: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Shot: close-up of Ruki, standing, looking toward frame left at Eri who is just off-camera, with a bashful, awkward wry smile, his eyes meeting hers, ears slightly flushed, holding the white printout near his chest. Window light from frame right gives a soft rim light on his hair, creamy bokeh of the sunny classroom behind him. Natural, subtle and realistic.

# 冷やかし: 窓際で頬杖をつく女子 A の寄り 1 枚で台詞を通す
section#tease
img#tease_shot(inset: 0; main: kb,1.03@62%,32%>1.11@62%,32%,ease=sine.inOut) [photo][ref:@seats]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Character: Girl A: a 17-year-old Japanese girl with long black hair tied in a low ponytail, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Shot: close-up of Girl A (low black ponytail, navy polo shirt) seated at her desk by the window, chin resting on her hand, looking up toward frame left at Eri and Ruki with a mischievous, teasing grin and playfully narrowed eyes, as if saying something cheeky. The bright window behind her gives a glowing rim light, curtains softly blurred.

# 凍る沈黙: 曲が止まり秒針だけ — 全員が止まった引き (動かない) → 目をそらし合う 2 人
section#freeze
img#freeze_shot(inset: 0; main: kb,1.06@50%,0%>1.06@50%,0%) [photo][ref:@seats][ref:@eri]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Characters: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Eri: a 17-year-old Japanese girl with shoulder-length straight black hair and soft bangs, wearing a white short-sleeve collared blouse under a navy-blue knitted school vest, and a navy-blue pleated skirt. Boy A: a 17-year-old Japanese boy with very short black hair, wearing a navy-blue polo shirt and navy-blue trousers. Girl A: a 17-year-old Japanese girl with long black hair tied in a low ponytail, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Girl B: a 17-year-old Japanese girl with a chin-length black bob, wearing a navy-blue polo shirt and a navy-blue pleated skirt. Shot: medium-wide shot of the group in a moment of frozen, awkward silence. Ruki stands beside the center desk holding the white printout, Eri stands in the aisle facing him a step away, both look away from each other in embarrassment (Ruki rubbing the back of his neck, Eri glancing down at the floor). Boy A, Girl A and Girl B are frozen mid-motion, wide-eyed, glancing at each other and suppressing grins. Sunlight from the windows on the right, dust particles hanging in the air, everything still. Realistic and understated, not exaggerated.
img#avert(inset: 0; main: kb,1.04@50%,21%>1.07@50%,27%,ease=sine.inOut) [photo][ref:@seats][ref:@eri]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Characters: Ruki: a 17-year-old Japanese boy with short, soft black hair and a gentle face, wearing a light sky-blue short-sleeve button-up school shirt (no tie) and navy-blue trousers. Eri: a 17-year-old Japanese girl with shoulder-length straight black hair and soft bangs, wearing a white short-sleeve collared blouse under a navy-blue knitted school vest, and a navy-blue pleated skirt. Shot: two-shot at chest height. Eri stands on the LEFT side of the frame and Ruki stands on the RIGHT side of the frame, facing each other about one meter apart, the windows are on the right side of the frame behind Ruki. Both turn their faces away to hide their embarrassment - Eri looks down and away toward frame left, tucking her hair behind her ear, Ruki looks off toward frame right with a bashful half smile, rubbing the back of his neck. Soft window light between them, shallow depth of field, tender, bittersweet mood.

# 再開: えりが座り 5 人が笑顔でクイズに戻る引き (曲が入り直す) → 「赤血球」でえりの笑顔の寄り・最後は黒へ
section#resume
img#resume_shot(inset: 0; content: @five; main: kb,1.1@50%,30%>1.04@50%,7%,ease=sine.inOut)
img#eri_smile(inset: 0; main: kb,1.03@45%,10%>1.07@45%,35%,ease=sine.inOut) [photo][ref:@five][ref:@eri_face]Keep exactly the same characters (same faces, hairstyles and outfits), the same classroom design and the same warm morning lighting as in the reference image(s). Create a new camera angle as described, do not copy the reference composition. Character: Eri: a 17-year-old Japanese girl with shoulder-length straight black hair and soft bangs, wearing a white short-sleeve collared blouse under a navy-blue knitted school vest, and a navy-blue pleated skirt. Shot: close-up of Eri seated at her desk, looking up toward frame right at Ruki, who is just out of frame holding the quiz printout, breaking into a shy, warm smile with a faint blush as she answers the quiz together with her friends. Soft morning backlight through her hair, the bright classroom and her laughing friends softly blurred behind her. Natural, joyful, tender.
```

```timeline.txt
#v2
# 5 人の声 (役ごとの cast・話し方は cast の manner + 台詞ごとの [manner:])。語りは無い
cast ruki = "柔らかく息まじりの優しい10代後半の男子高校生の声、明瞭な発音" manner="友達にクイズを出すように、楽しそうに軽やかに、高校生らしい自然な会話のトーンで"
cast girl_a = "明るく高めのピッチで活気のある10代後半の女子高校生の声、ハキハキした発音と豊かな抑揚" manner="嬉しそうに元気よく即答する、女子高校生の自然な声で"
cast boy_a = "明るくエネルギーのある10代後半の男子高校生の声、やや高めでハキハキした口調" manner="思わず笑いながら、驚いて短くツッコむ"
cast girl_b = "明るく元気で高めのピッチの10代の女子高校生の声、ハキハキした滑舌" manner="笑いながら悔しがる、女子高校生の自然な声で"
cast eri = "明るく澄んだ高めのピッチの10代後半の女子高校生の声、クリアで柔らかい" manner="少し照れながらも、みんなと声を揃えて笑顔で"
# 声の端の無音は 0 (掛け合いの間は台詞の [silence] で書く)
silence head=0 tail=0

*** quiz
[>#subtitle]
fade in,500
bgm music
se "朝のスズメのさえずり、チュンチュンと軽やかな屋外の環境音" -10dB to=13s fade=600,500
@ruki: [speed:108%][>#establish +960][>#leak_l +960][!#leak_r to,{opacity:0, duration:0.25, ease:'none'} +960][<#curtain +1210][silence:2.0s]じゃあ次。[>#ruki_quiz -40][<#establish -40][<#leak_l -40][!#leak_r to,{opacity:0.7, duration:0.04} -40]細胞の中でエネルギーをつくる、細胞小器官は？

*** answer
@girl_a: [silence:0.05s]ミトコンドリア！
@boy_a: はやっ！
@girl_b: [speed:104%][>#eri_walk +850][<#group_shot +850][♪"上履きで教室の床を歩く柔らかい足音" -8dB +850 to=2.2s fade=80,250]言おうと思ったのにー！[silence:0.6s]

*** sorry
se "朝のスズメのさえずり、チュンチュンと軽やかな屋外の環境音" -10dB to=13s fade=600,500
@ruki: [manner:慌てて立ち上がりながら、照れくさそうに、でもはっきりと][♪"椅子を後ろに引くガタッという音" -3dB][silence:0.35s][!#ruki_stand shake,2,duration=260 -300]あ、ごめん[silence:0.1s][>#eri_close][<#ruki_stand][silence:1.3s][>#ruki_close][<#eri_close][silence:1.08s]

*** tease
@girl_a: [manner:いたずらっぽく、にやにやしながら、軽いテンポでからかうように][speed:103%][silence:0.13s]えりちゃん、カド ルキに座られて嬉しいもんね
[<#music]

*** freeze
@ruki: [♪"残響のある掛け時計の秒針の音、チッ、チッとゆっくり刻む" -2dB +50 to=4.2s fade=0,500][silence:2.05s][>#avert][<#freeze_shot][silence:1.8s]

*** resume
bgm music_b
se "朝のスズメのさえずり、チュンチュンと軽やかな屋外の環境音" -10dB to=6s fade=600,500
subtitle "じゃ、じゃあ次！ 血液の中で酸素を運ぶ細胞は？"
@ruki: [manner:照れ隠しで少し早口に、気を取り直して明るく][speed:112%][♪"紙のプリントを持ち上げるカサッという乾いた音" -6dB +30][silence:0.2s]じゃ、じゃあ次！[||]血液の中で酸素を運ぶ細胞は？
@eri: [silence:0.14s][>#eri_smile +620][<#resume_shot +620][♪"遠くで鳴る学校のチャイム、ゆっくりした鐘の音" -3dB +350 to=1.9s fade=0,700]赤血球！
@girl_b: [<#subtitle][manner:楽しそうに思わず笑う]あははっ
fade out,600
```

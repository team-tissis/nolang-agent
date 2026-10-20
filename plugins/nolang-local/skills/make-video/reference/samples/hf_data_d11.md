# data · marathon-pacing (hf 全力版の全量の写し — マラソン、前半を飛ばした人は何分損した？・暗い方眼の地の 9 場面のデータ図解 (100 マス・折れ線・割合の帯・貯金と借金の左右の棒・横棒・達成率の輪)) — canvas 720x1280・約 62s

見せる作り: 全編の地 (紺のグラデ + 2 色の光 + 方眼 + 斜めに流れ続ける光の線)・2 場面目からの常設のコース型の進行 (S〜G の目盛り + 伸びる線 + 走る点)・題つきの板の def (色の縦棒 + 斜めの札 + 題 + 副題 + 注記) を場面ごとに色替え・数字の語で動く図 (数え上がる時計と人数・100 マスを語ごとに 3 色で塗る・折れ線を 30km から赤で描き継ぐ・割合の帯・貯金 / 借金の左右の棒と差の斜線・横棒の比較と全体の破線・達成率の輪)・叩きつける主役の札 (閃光と板の揺れ)・他を沈めて主役を弾ませる・写真の場面 (題の頭・疲れた終盤・おすすめ・ゴール) と締めのテープ・斜めの帯が払う切替・音の層 (BGM + 語に結んだ効果音 28 + 切替の風切り 8)

```design.txt
#v2
# 学ぶ作り: 縦のデータ図解の design system を根に 1 回 (palette・書体 4・数字の run・板 board の def・札 chip の def) → 場面は板の中身 (図) だけ
# 常設の層: 全編の地 (紺のグラデ + 2 色の光 + 方眼 + 斜めに流れ続ける光の線)・2 場面目からのコース型の進行 (S〜G の目盛り + 伸びる線 + 走る点)
# 図は数字の語で動く: 100 マスを 3 群に塗る・折れ線を 30km で赤に描き継ぐ・帯の割合・貯金 / 借金の左右の棒・横棒の比較・達成率の輪
# hf d11 marathon-pacing (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3。切替は全部の境目に斜めの紺の板 + 黄緑と赤の帯が払う wipe
canvas 720x1280 bg=#070B14
theme dark
palette ink=#F4F6FA sub=#9AA6B8 lime=#C6FF3D fast=#FF4D2E even=#2EE6C9 slow=#7C93FF gold=#FFC83D steel=#4C5A73 coral=#FF8A73 pale=#C9D2E0 dim=#8B96A8
font "癖のない標準的な日本語のゴシック体の極太 (Heavy)、画面の資料や UI 向けの読みやすい書体"
fonts j="癖のない標準的な日本語のゴシック体の極太 (Heavy)、画面の資料や UI 向けの読みやすい書体"
# 字幕は同じ書体を別の説明文で引く (本文の文字と書体の pin を分ける — 字幕の縁取りが本文の文字の計測に写らないように)
fonts sb="癖のない標準的な日本語のゴシック体の極太 (Heavy)、画面の資料や UI 向けの読みやすい書体、字幕向け"
fonts m="癖のない標準的な日本語のゴシック体の太字 (Bold)、画面の資料や UI 向けの読みやすい書体"
fonts r="標準の太さのすっきりした角ゴシック体"
fonts n="幅の狭い縦長のコンデンス体の極太の欧文サンセリフ、スポーツの数字向け"
sfx off
# hf の作り: 板の注記・凡例・目盛り・札は 13〜17 px (hf の 20〜25 px の 2/3)
# hf の作り: 板の札・題・副題・軸は場面の頭に出して台詞が後から読む (spoiler・stacked_labels)・図だけの板の場面 (text_only_cut)・札と字幕が同じ語 (duplicate_text)
# hf の作り: 切替の板は声の終わりの 0.05 秒前から払い始める (transition_over_speech)・字幕は払いの窓の中で出る (entrance_in_transition)・締めの札は場面の終わり際に出る (entrance_in_fadeout・flash_text)
# hf の作り: 写真の主役の胴に時計・板を重ねる (text_over_subject — s8 の顔は札・問いと板の間の空きに出し、上端の帯は顔に掛けない)・灰の段の色は直書き (palette_drift)
lint off=small_text,spoiler,stacked_labels,text_only_cut,duplicate_text,transition_over_speech,entrance_in_transition,entrance_in_fadeout,flash_text,text_over_subject,palette_drift
run hl = color=$lime
run fs = color=#FF7B64
run r = color=$coral
run g = color=$gold
run nb = color=$ink font=n size=1.43em
run lb = color=$sub font=m size=0.8em
run s = color=$sub font=m size=0.4em
run big = font=n size=2.48em
run so = size=1.22em
run gd = color=$gold font=n size=2.6em
prompt_tail "No text, no letters, no numbers, no logos, no watermark, no readable race bibs."
p { color: $ink; out: none }
div { border: none; box-shadow: none; padding: 0px; background: none; border-radius: 0px; out: none }
shape { out: none }
svg { out: none }
img { out: none }
veil { out: none }
sound sw_start = "ストップウォッチのボタンを押すカチッという短い電子音"
sound whoosh = "速く鋭いシュッという風切り音、画面を横切る"
sound whoosh2 = "低く太いヒュッという風切り音、場面の切り替わり"
sound impact = "重く短いドンという衝撃音、数字を叩きつける"
sound pop = "軽く弾むポンという短い音"
sound bell = "明るく澄んだチーンというベルの音"
sound negative = "下がっていく残念なブブーという短い電子音"
sound sparkle = "キラキラと輝く高い音、達成の瞬間"
sound rise = "上昇していくシューッというライザーの音"
svg target = """<svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="54" fill="none" stroke="#FFC83D" stroke-width="7"/><circle cx="60" cy="60" r="35" fill="none" stroke="#FFC83D" stroke-width="7"/><circle cx="60" cy="60" r="15" fill="#FFC83D"/></svg>"""
# 白い閃光 (全編に 1 枚・語で 0.03 秒光って 0.22 秒で引く)
cue flash(o) = [!#flash to,opacity={o},duration=30][!#flash to,opacity=0,duration=220 >]
bgm#music スポーティでテンポの速いエレクトロ・ロックのビート、力強いドラムと歪んだシンセ、競技の高揚感、ランニングのデータ解説の縦型動画向け
# 字幕: 下の帯の中央に白の極太 + 紺の太い縁 (地なし)・数字は黄緑 (台詞の {hl})・句末の約物は外す
subtitle(font-family: sb; left: 27px; top: 932px; width: 667px; height: 113px; padding: 0px; font-size: 33px; line-height: 1.28; letter-spacing: 0.01em; color: #FFFFFF; stroke: #070B14,8; background: none; unit: sentence; strip: 、。; lead: 60; tail: 350; hold: off; in: {y:12, opacity:0, duration:0.16, ease:'power2.out'}; out: {opacity:0, duration:0.08})
# 札 (欧文の斜体・黄緑の地・斜めに傾く)。和文の札は chipj
def chip(t) = p(font-size: 20px; line-height: 1.2; font-family: n; font-style: italic; letter-spacing: 0.04em; color: #0A0E17; background: $lime; border-radius: 3px; padding: 4px 12px 5px 12px; transform: skewX(-10deg); content: {t})
def chipj(t) = p(font-size: 18px; line-height: 1.3; letter-spacing: 0.02em; color: #0A0E17; background: $lime; border-radius: 3px; padding: 4px 12px 5px 12px; transform: skewX(-10deg); content: {t})
# 題つきの板 (紺の板 + 左の色の縦棒 + 札 + 題 + 副題 + 下の注記)・下から 47 px 上がって出る
def board(k, t, s="", fn="", c=$lime) = div(left: 40px; top: 153px; width: 640px; height: 760px; border-radius: 23px; background: #0C1220ED; border: 1px solid #FFFFFF14; box-shadow: 0px 20px 60px #00000080; delay: 20; in: {y:47, scale:0.97, opacity:0, duration:0.5, ease:'power3.out'})
  div#acc(left: 0px; top: 0px; width: 7px; height: 100%; border-radius: 23px 0px 0px 23px; background: {c})
  chip#k(left: 32px; top: 24px; background: {c}; content: {k})
  p#t(left: 32px; top: 66px; font-size: 39px; line-height: 1.15; letter-spacing: -0.01em; white-space: nowrap; content: {t})
  p#s(left: 32px; top: 118px; font-size: 18px; font-family: m; color: $sub; white-space: nowrap; content: {s})
  p#fn(left: 32px; bottom: 17px; font-size: 15px; font-family: r; color: $dim; white-space: nowrap; content: {fn})
# 入り方の 3 群の札 (左の色の縦棒 + 群の名 + 定義 + 右に % と人数)
def gcard(nm, df, pc, ct, c) = div(left: 32px; width: 576px; height: 109px; border-radius: 15px; background: #FFFFFF0D; border: 1px solid #FFFFFF14; in: {x:-40, opacity:0, duration:0.35, ease:'power3.out', stagger:{each:0.15}})
  div#bl(left: 0px; top: 0px; width: 8px; height: 100%; border-radius: 15px 0px 0px 15px; background: {c})
  p#nm(left: 23px; top: 13px; font-size: 33px; line-height: 1.2; color: {c}; content: {nm})
  p#df(left: 24px; top: 65px; font-size: 19px; font-family: m; color: $pale; white-space: nowrap; content: {df})
  p#pc(right: 23px; top: 7px; font-size: 57px; line-height: 1; font-family: n; font-style: italic; color: {c}; content: {pc})
  p#ct(right: 24px; top: 80px; font-size: 17px; line-height: 1; font-family: m; color: $sub; content: {ct})
# 群の横棒の行 (群の名 + 左から伸びる棒 + 値と人数)
def hrow(k, bw, v, c, o=1) = div(left: 32px; width: 576px; height: 37px; in: {opacity:0, duration:0.15, stagger:{each:0.15}})
  p#k(left: 0px; top: 4px; font-size: 20px; color: {c}; white-space: nowrap; content: {k})
  div#bar(left: 115px; top: 4px; width: {bw}; height: 29px; border-radius: 7px; background: {c}; opacity: {o}; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
  p#v(left: .bar.right+10; top: -3px; font-size: 37px; line-height: 1; font-family: n; font-style: italic; color: {c}; white-space: nowrap; content: {v})

# 全編の地 (根): 紺の縦グラデ + 左上の黄緑・右下の赤の光 + 40 px の方眼 + 斜め −14° の光の線 9 本が左から右へ流れ続ける
div#bg_base(inset: 0; background: linear(#0A1020,#070B14,180); z-index: back; in: none)
veil#glow_a(background: radial(#C6FF3D1A,#C6FF3D00@60%,0%,0%); z-index: back; in: none)
veil#glow_b(background: radial(#FF4D2E1F,#FF4D2E00@60%,100%,100%); z-index: back; in: none)
div#grid(inset: 0; pattern: grid,40,#FFFFFF09; opacity: 0.6; z-index: back; in: none)
div#speed.bleed(inset: 0; z-index: back; in: none)
  div#l(left: 0px; top: "107;244;381;517;654;791;927;1064;1201"; width: "173;253;333;173;253;333;173;253;333"; height: 3px; border-radius: 3px; background: linear(#C6FF3D00,#C6FF3D59,#C6FF3D00,90); transform: rotate(-14deg); in: none; main: "sawtooth,x=1467,freq_ms=1100;sawtooth,x=1467,freq_ms=1330,phase_offset=0.28;sawtooth,x=1467,freq_ms=1560,phase_offset=0.47;sawtooth,x=1467,freq_ms=1790,phase_offset=0.62;sawtooth,x=1467,freq_ms=1100,phase_offset=0.35;sawtooth,x=1467,freq_ms=1330,phase_offset=0.39;sawtooth,x=1467,freq_ms=1560,phase_offset=0.42;sawtooth,x=1467,freq_ms=1790,phase_offset=0.45;sawtooth,x=1467,freq_ms=1100,phase_offset=0.69") ×9
veil#flash(color: #FFFFFF; opacity: 0; z-index: curtain; in: none)

# s1 問い: 湾岸の橋を埋めるランナーの写真が 1.16 → 1.02 に引き、完走タイムの時計が数え上がる → 曲の山で題が叩きつけられ (閃光)、「何分」が 2.6 倍から落ちて揺れる
section#s1(stagger: {each:0})
img#s1_img(inset: 0; subject: bottom 60%; room: top 40%; main: kb,1.16>1.02,ease=power1.out) [photo]縦長 9:16 の写真。朝日の湾岸を走る大都市マラソン。広い湾の橋を何百人もの市民ランナーが川のように埋めて走る様子を、やや上の後方から見下ろす。地平線から低い金色の太陽がフレアを放ち、影は深い青緑、ハイライトは暖かい橙、動きと熱気。ランナーの群れは画面の下 6 割を埋め、上 4 割は落ち着いた朝の空で見出しの余白。
veil#s1_shade(background: linear(#070B14DB,#070B1473@30%,#070B140D@46%,#070B1459@62%,#070B14EB,180); in: none)
chipj#s1_kick(left: 40px; top: 157px; in: {x:-53, opacity:0, duration:0.3, ease:'power3.out'}) 完走者8,214人のデータで検証
group#s1_title(left: 40px; top: 209px; width: 660px; height: 330px; in: none)
  p#l1(left: 0px; top: 0px; font-size: 57px; line-height: 1.1; stroke: #070B14E0,4; text-shadow: 0px 4px 20px #00000099; white-space: nowrap; in: {x:-80, skewX:-18, opacity:0, duration:0.3, ease:'power4.out'}) マラソン、
  p#l2(left: 0px; top: 67px; font-size: 71px; line-height: 1.12; letter-spacing: -0.02em; stroke: #070B14E0,4; text-shadow: 0px 4px 20px #00000099; white-space: nowrap; in: {scale:1.5, opacity:0, duration:0.3, ease:'power4.out'}) 前半を{fs}飛ばした{/}人は
  p#nanpun(left: 0px; top: 164px; width: 322px; font-size: 157px; line-height: 1; color: $lime; stroke: #070B14E0,4; text-shadow: 0px 7px 33px #C6FF3D59; transform-origin: 30% 70%; white-space: nowrap; in: {scale:2.6, opacity:0, duration:0.32, ease:'power4.out'}) 何分
  p#son(left: 321px; top: 238px; font-size: 83px; line-height: 1; stroke: #070B14E0,4; text-shadow: 0px 4px 20px #00000099; white-space: nowrap; in: {x:40, opacity:0, duration:0.3, ease:'power3.out'}) 損した？
# 完走タイムの時計 (黄緑の縁の暗い札・0:00 → 4:24 を 2.2 秒で数える)
# 時計は時:分:秒の桁送りで 0:00:00 → 4:24:15 (hf の秒の桁まで回る)
div#s1_clock(left: 140px; top: 740px; width: 440px; height: 133px; border-radius: 17px; background: #070B14C7; border: 2px solid #C6FF3D8C; box-shadow: 0px 0px 40px #C6FF3D2E; delay: 100; in: {scale:0.7, opacity:0, duration:0.3, ease:'back.out(2.4)'})
  p#lbl(cx: 50%; top: 13px; font-size: 20px; font-family: n; font-style: italic; letter-spacing: 0.12em; color: $lime; white-space: nowrap) FINISH TIME {lb}完走タイムの中央値{/}
  p#clock(cx: 50%; top: 43px; font-size: 83px; line-height: 1; font-family: n; font-style: italic; white-space: nowrap) [count:4:24:15 start=0:00:00 ms=2200]

# s2 調べたデータ: 上端にコース型の進行が降り (以後常設)、板の上で大会名 → 完走者 8,214 人が数え上がり 95% の帯 → 5km ごとの点 9 個 × 目標の的と 4 つの札 → 「突き合わせ」の金の行
section#s2(stagger: {each:0})
# 常設の上端の帯 (sticky): 札 DATA RUN・大会名・コースの線に S〜G の 10 目盛り
div#hdr.sticky(left: 0px; top: 0px; width: 720px; height: 120px; z-index: front; delay: 50; in: {y:-20, opacity:0, duration:0.4, ease:'power3.out'})
  chip#chip(left: 40px; top: 43px) DATA RUN
  p#race(right: 40px; top: 47px; font-size: 17px; font-family: m; color: $sub; white-space: nowrap) みなと湾岸シティマラソン（架空）
  div#base(left: 40px; top: 93px; width: 640px; height: 3px; border-radius: 2px; background: #FFFFFF29)
  div#tk(left: "39;115;191;267;342;418;494;570;646;679"; top: 90px; width: 2px; height: 9px; background: #FFFFFF59) ×10
  p#tl(cx: "40;116;192;268;343;419;495;571;647;680"; top: 102px; font-size: 13px; font-family: "n;n;n;n;n;n;n;n;n;j"; color: "#7F8A9C;#7F8A9C;#7F8A9C;#7F8A9C;#7F8A9C;#7F8A9C;#7F8A9C;#7F8A9C;#7F8A9C;$lime") ×10 S;5;10;15;20;25;30;35;40;G
# 進行: 黄緑の線が残りの全尺で伸び、光る点が線の先を走る
progress#prog.sticky(left: 40px; top: 93px; width: 640px; height: 3px; background: $lime; border-radius: 2px; until: end; z-index: front; overlap: hdr)
shape#runner.ellipse.sticky(left: 33px; top: 87px; width: 15px; height: 15px; background: $lime; box-shadow: 0px 0px 0px 4px #C6FF3D40; z-index: front; overlap: hdr; in: {opacity:0, duration:0.4}; main: ramp,x=640)
board#b2(k: "DATA"; t: "調べたデータ"; s: "申込時の目標タイム × 実際の走り"; fn: "※架空の市民マラソン1大会分のデータ（作例）")
  p#name(left: 32px; top: 152px; font-size: 33px; line-height: 1.2; white-space: nowrap; delay: 180; in: {y:27, opacity:0, duration:0.4, ease:'power3.out'}) みなと湾岸シティマラソン
  p#tag(left: .name.right+9; top: 158px; font-size: 16px; font-family: m; color: #C9D2E0; background: #2A3345; border-radius: 7px; padding: 3px 9px 4px 9px; delay: 180; in: {y:27, opacity:0, duration:0.4, ease:'power3.out'}) 架空の大会
  p#meta(left: 32px; top: 202px; font-size: 19px; font-family: m; color: $sub; white-space: nowrap; delay: 280; in: {y:27, opacity:0, duration:0.4, ease:'power3.out'}) フル{nb}42.195{/}km ｜ 制限{nb}6{/}時間 ｜ 出走{nb}8,650{/}人
  chipj#lbl(left: 32px; top: 245px; in: {scale:0.5, opacity:0, duration:0.38, ease:'back.out(2.4)'}) 完走者
  p#big(left: 27px; top: 291px; font-size: 136px; line-height: 1; font-family: n; font-style: italic; color: $lime; white-space: nowrap; in: {opacity:0, duration:0.15}) [count:8,214 start=0 ms=900]
  p#unit(left: .big.right+5; top: 364px; font-size: 51px; line-height: 1; in: {opacity:0, duration:0.15}) 人
  p#rate(left: 32px; top: 444px; font-size: 19px; font-family: m; color: $sub; white-space: nowrap; in: {y:13, opacity:0, duration:0.35, ease:'power3.out'}) 完走率 {nb}95.0{/}%（8,214人 ÷ 8,650人）
  div#bar(left: 32px; top: 481px; width: 576px; height: 11px; border-radius: 5px; background: #232C3D; in: {opacity:0, duration:0.2})
    div#fill(left: 0px; top: 0px; width: 95%; height: 11px; border-radius: 5px; background: $lime; delay: 50; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
  # 5km ごとの通過記録 (線の上に点 9 つ・G だけ金) × 目標タイム (的 + 4 つの札)
  div#ca(left: 32px; top: 508px; width: 261px; height: 152px; border-radius: 15px; background: #FFFFFF0B; border: 1px solid #FFFFFF14; in: {y:20, opacity:0, duration:0.35, ease:'power3.out'})
    p#ct(left: 16px; top: 13px; font-size: 20px; white-space: nowrap) 5kmごとの通過記録
    div#ln(left: 9px; top: 87px; width: 219px; height: 3px; border-radius: 2px; background: #FFFFFF40)
    shape#dot.ellipse(left: "26;50;75;99;123;147;172;196;220"; top: 81px; width: 15px; height: 15px; background: "$lime;$lime;$lime;$lime;$lime;$lime;$lime;$lime;$gold"; in: {y:7, opacity:0, duration:0.18, ease:'back.out(2)', stagger:{each:0.07}}) ×9
    p#dl(cx: "34;58;83;107;131;155;180;204;228"; top: 103px; font-size: 15px; font-family: n; color: $pale; in: {y:7, opacity:0, duration:0.18, ease:'back.out(2)', stagger:{each:0.07}}) ×9 5;10;15;20;25;30;35;40;G
  p#x(cx: 320px; top: 551px; font-size: 64px; line-height: 1; font-family: n; color: $lime; in: {scale:0.3, opacity:0, duration:0.38, ease:'back.out(2.4)'}) ×
  div#cb(left: 347px; top: 508px; width: 261px; height: 152px; border-radius: 15px; background: #FFFFFF0B; border: 1px solid #FFFFFF14; in: {y:20, opacity:0, duration:0.35, ease:'power3.out'})
    p#ct(left: 16px; top: 13px; font-size: 20px; white-space: nowrap) 申込時の目標タイム
    svg#tg(left: 15px; top: 64px; width: 80px; height: 80px; part: target)
    p#gc(left: "104;181;104;181"; top: "61;61;99;99"; width: 70px; text-align: center; font-size: 15px; font-family: m; white-space: nowrap; border: 1px solid #FFFFFF40; border-radius: 7px; padding: 4px 0px 5px 0px) ×4 サブ3.5;サブ4;サブ5;5時間超
  p#match(left: 32px; top: 676px; font-size: 21px; color: $gold; white-space: nowrap; in: {x:-27, opacity:0, duration:0.35, ease:'power3.out'}) ▶ 全完走者の走りを、目標と突き合わせ

# s3 前半 vs 後半: 100 マスが左上から並び、語ごとに 7 マス (黄緑) → 15 マス (灰) → 78 マス (赤) と塗られて凡例の % が数える・板が揺れ、中央値の前半 / 後半の棒と「+12:35」の札
section#s3(stagger: {each:0})
board#b3(k: "前半 vs 後半"; t: "後半の方が速かった人は？"; s: "中間点21.1kmで比較｜1マス＝完走者の1%"; fn: "※ネガティブスプリット＝後半の方が速いペース配分")
  chip#k(font-size: 18px; line-height: 1.3; font-family: j; font-style: normal; letter-spacing: 0.02em)
  # 1 マス = 1%: 速くなった 7・ほぼ同じ 15・遅くなった 78 (10 列の行順)
  div#wn(left: "32;71;109;148;187;225;264"; top: 163px; width: 34px; height: 34px; border-radius: 7px; background: #1B2333; border: 1px solid #FFFFFF1A; delay: 200; in: {scale:0.4, opacity:0, duration:0.22, ease:'back.out(2)', stagger:{each:0.006}}) ×7
  div#we(left: "303;341;380;32;71;109;148;187;225;264;303;341;380;32;71"; top: "163;163;163;202;202;202;202;202;202;202;202;202;202;240;240"; width: 34px; height: 34px; border-radius: 7px; background: #1B2333; border: 1px solid #FFFFFF1A; delay: 242; in: {scale:0.4, opacity:0, duration:0.22, ease:'back.out(2)', stagger:{each:0.006}}) ×15
  div#wp(left: "109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380"; top: "240;240;240;240;240;240;240;240;279;279;279;279;279;279;279;279;279;279;318;318;318;318;318;318;318;318;318;318;356;356;356;356;356;356;356;356;356;356;395;395;395;395;395;395;395;395;395;395;434;434;434;434;434;434;434;434;434;434;472;472;472;472;472;472;472;472;472;472;511;511;511;511;511;511;511;511;511;511"; width: 34px; height: 34px; border-radius: 7px; background: #1B2333; border: 1px solid #FFFFFF1A; delay: 332; in: {scale:0.4, opacity:0, duration:0.22, ease:'back.out(2)', stagger:{each:0.006}}) ×78
  # 塗る語で同じ位置に色のマスを重ねて溶かし出す (hf はマスの地と縁の色を tween)
  div#wnc(left: "32;71;109;148;187;225;264"; top: 163px; width: 34px; height: 34px; border-radius: 7px; background: $lime; border: 1px solid $lime; in: {opacity:0, duration:0.2}) ×7
  div#wec(left: "303;341;380;32;71;109;148;187;225;264;303;341;380;32;71"; top: "163;163;163;202;202;202;202;202;202;202;202;202;202;240;240"; width: 34px; height: 34px; border-radius: 7px; background: #6B778C; border: 1px solid #6B778C; in: {opacity:0, duration:0.2}) ×15
  div#wpc(left: "109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380;32;71;109;148;187;225;264;303;341;380"; top: "240;240;240;240;240;240;240;240;279;279;279;279;279;279;279;279;279;279;318;318;318;318;318;318;318;318;318;318;356;356;356;356;356;356;356;356;356;356;395;395;395;395;395;395;395;395;395;395;434;434;434;434;434;434;434;434;434;434;472;472;472;472;472;472;472;472;472;472;511;511;511;511;511;511;511;511;511;511"; width: 34px; height: 34px; border-radius: 7px; background: $fast; border: 1px solid $fast; in: {opacity:0, duration:0.16}) ×78
  # 凡例 3 段 (色の四角 + 題・大きな %・人数)・語ごとに右から入る
  div#lga(left: 433px; top: 163px; width: 187px; height: 130px; in: {x:27, opacity:0, duration:0.3, ease:'power3.out'})
    div#sw(left: 0px; top: 5px; width: 15px; height: 15px; border-radius: 4px; background: $lime)
    p#h(left: 22px; top: 0px; font-size: 17px; white-space: nowrap) 後半の方が速い
    p#v(left: 0px; top: 29px; font-size: 72px; line-height: 1; font-family: n; font-style: italic; color: $lime; white-space: nowrap) [count:7.3 start=0 ms=600]%
    p#n(left: 0px; top: 105px; font-size: 15px; font-family: m; color: $sub; white-space: nowrap) 600人｜ネガティブスプリット
  div#lgb(left: 433px; top: 313px; width: 187px; height: 105px; in: {x:27, opacity:0, duration:0.3, ease:'power3.out'})
    div#sw(left: 0px; top: 5px; width: 15px; height: 15px; border-radius: 4px; background: #8A96AA)
    p#h(left: 22px; top: 0px; font-size: 17px; white-space: nowrap) ほぼ同じ（差±2分）
    p#v(left: 0px; top: 29px; font-size: 48px; line-height: 1; font-family: n; font-style: italic; color: #A9B4C6) 14.6%
    p#n(left: 0px; top: 81px; font-size: 15px; font-family: m; color: $sub) 1,199人
  div#lgc(left: 433px; top: 424px; width: 187px; height: 130px; in: {x:27, opacity:0, duration:0.3, ease:'power3.out'})
    div#sw(left: 0px; top: 5px; width: 15px; height: 15px; border-radius: 4px; background: $fast)
    p#h(left: 22px; top: 0px; font-size: 17px; white-space: nowrap; transform-origin: 0% 50%) 後半が{tf}2分以上{/}遅い
    p#v(left: 0px; top: 29px; font-size: 72px; line-height: 1; font-family: n; font-style: italic; color: $fast; white-space: nowrap) [count:78.1 start=0 ms=700]%
    p#n(left: 0px; top: 105px; font-size: 15px; font-family: m; color: $sub) 6,415人
  # 中央値の走り: 前半 (鋼色) と後半 (赤) の棒が左から伸び、差の札が傾いて弾む
  p#medh(left: 32px; top: 568px; font-size: 19px; white-space: nowrap; in: {y:13, opacity:0, duration:0.3, ease:'power3.out'}) 中央値の走り {lb}（完走者を記録順に並べた真ん中）{/}
  p#mka(left: 32px; top: 609px; font-size: 18px; in: {opacity:0, duration:0.15}) 前半
  div#mba(left: 89px; top: 603px; width: 363px; height: 35px; border-radius: 7px; background: $steel; in: {scaleX:0, duration:0.45, ease:'power3.out', pivot:'left'})
    p#t(right: 9px; cy: 50%; font-size: 28px; font-family: n; font-style: italic) 2:05:50
  p#mkb(left: 32px; top: 651px; font-size: 18px; in: {opacity:0, duration:0.15}) 後半
  div#mbb(left: 89px; top: 645px; width: 400px; height: 35px; border-radius: 7px; background: $fast; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})
    p#t(right: 9px; cy: 50%; font-size: 28px; font-family: n; font-style: italic) 2:18:25
  p#badge(left: 499px; top: 636px; font-size: 36px; line-height: 1.05; font-family: n; font-style: italic; color: #FFFFFF; background: $fast; border-radius: 8px; padding: 1px 11px 4px 11px; box-shadow: 0px 5px 20px #FF4D2E73; transform: rotate(-4deg); in: {scale:0.3, opacity:0, duration:0.38, ease:'back.out(2.4)'}) +12:35

# s4 5km ごとのペース: 疲れたランナーの写真 (彩度を落として 0.55) の上の板に、6'00" 〜 7'00" の目盛り → 白の折れ線が 25-30 まで描かれ点と値が順に弾む → 30km からの赤い帯と破線 → 赤の線が描き継がれて +40秒 → 52% の札 → 「キロ +64秒」の札が叩きつけられ板が揺れる
section#s4(stagger: {each:0})
img#s4_img(inset: 0; opacity: 0.55; filter: sat:0.6; subject: center 50%; main: kb,1.12>1.0; in: {opacity:0, duration:7.85, ease:'none'}) [photo]縦長 9:16 のスポーツ写真。マラソン終盤で疲れ切った市民ランナー。脚が重く顔をゆがめ汗をかき、湾沿いの誰もいないアスファルトの道で失速している。低い位置からの望遠、霞んだ午後の強い光、ざらついた高コントラストの劇的な雰囲気、暗く彩度の低い色調。人物は画面の中央に置き、上下に余白。
div#s4_top(left: 0px; top: 0px; width: 720px; height: 213px; background: linear(#070B14F0,#070B14B3@45%,#070B1400,180); in: none)
board#b4(k: "PACE"; t: "5kmごとのペース"; s: "完走者の中央値｜1kmあたり"; fn: "※各区間の1kmあたりペース（完走者の中央値）"; c: $fast; background: #0A0F1BDB)
  chip#k(color: #FFFFFF)
  # 目盛り (横の破線 4 本・縦軸のペース・横軸の区間・速い / 遅い)・cut 頭の 0.2 秒後に
  p#hint(left: 30px; top: "150;508"; font-size: 15px; color: $dim; delay: 200; in: {opacity:0, duration:0.3}) ×2 ↑速い;↓遅い
  shape#grid(left: 80px; top: "213;293;373;453"; width: 527px; height: 2px; path: line_h; border: 1px solid #FFFFFF1A; dash: 4,5; delay: 200; in: {opacity:0, duration:0.3}) ×4
  p#yl(left: 12px; cy: "214;294;374;454"; width: 60px; text-align: right; font-size: 17px; font-family: n; color: $dim; delay: 200; in: {opacity:0, duration:0.3}) ×4 6′00″;6′20″;6′40″;7′00″
  p#xl(cx: "93;155;216;278;340;401;463;525;586"; cy: 529px; font-size: 17px; font-family: n; color: "$pale;$pale;$pale;$pale;$pale;$pale;$coral;$coral;$coral"; delay: 200; in: {opacity:0, duration:0.3}) ×9 0-5;5-10;10-15;15-20;20-25;25-30;30-35;35-40;40-G
  p#unit(right: 27px; top: 547px; font-size: 13px; font-family: m; color: $dim; delay: 200; in: {opacity:0, duration:0.3}) 区間（km）
  # 30km からの赤い帯と縦の破線 (語で出る)
  div#zone(left: 432px; top: 160px; width: 181px; height: 347px; border-radius: 12px; background: linear(#FF4D2E47,#FF4D2E0F,180); in: {opacity:0, duration:0.3})
  shape#m30(left: 431px; top: 160px; width: 3px; height: 350px; path: line_v; border: 3px solid $fast; dash: 7,5; in: {opacity:0, duration:0.2})
  # 折れ線: 白の 0〜30km (1 秒で描く) と赤の 30km〜G (0.8 秒)
  shape#la(path: "M93 205.7 L154.7 193.7 L216.3 201.7 L278 213.7 L339.7 233.7 L401.3 269.7"; background: none; border: 6px solid $ink; in: draw,1000,ease=power1.inOut)
  shape#lb(path: "M401.3 269.7 L463 365.7 L524.7 461.7 L586.3 433.7"; background: none; border: 7px solid $fast; in: draw,800,ease=power2.in)
  shape#pa.ellipse(left: "84;146;208;269;331;393"; top: "197;185;193;205;225;261"; width: 17px; height: 17px; background: $lime; border: 3px solid #0B1020; in: {scale:0.2, opacity:0, duration:0.25, ease:'back.out(2.4)', stagger:{each:0.19}}) ×6
  p#va(cx: "93;155;216;278;340;401"; cy: "179;167;175;187;207;243"; font-size: 20px; font-family: n; font-style: italic; delay: 40; in: {y:5, opacity:0, duration:0.2, stagger:{each:0.19}}) ×6 5′58″;5′55″;5′57″;6′00″;6′05″;6′14″
  shape#pb.ellipse(left: "455;516;578"; top: "357;453;425"; width: 17px; height: 17px; background: $fast; border: 3px solid #0B1020; delay: 260; in: {scale:0.2, opacity:0, duration:0.25, ease:'back.out(2.4)', stagger:{each:0.26}}) ×3
  p#vb(cx: "463;525;586"; cy: "400;496;407"; font-size: 20px; font-family: n; font-style: italic; color: $coral; delay: 300; in: {y:-5, opacity:0, duration:0.2, stagger:{each:0.26}}) ×3 6′38″;7′02″;6′55″
  chipj#chip(left: 429px; top: 160px; font-size: 16px; color: #FFFFFF; background: $fast; in: {scale:0.4, opacity:0, duration:0.38, ease:'back.out(2.4)'}) 崩れるのは30kmから
  p#d40(left: 484px; top: 341px; font-size: 23px; font-family: n; font-style: italic; color: $coral; in: {scale:0.4, opacity:0, duration:0.38, ease:'back.out(2.4)'}) +40秒
  # 52% の札 (薄い赤の板)
  div#info(left: 32px; top: 589px; width: 576px; height: 100px; border-radius: 15px; background: #FF4D2E1F; border: 1px solid #FF4D2E73; in: {y:20, opacity:0, duration:0.35, ease:'power3.out'})
    p#t(left: 20px; top: 15px; font-size: 20px; line-height: 1.35; white-space: nowrap) 30km以降にキロ30秒以上[br]ペースが落ちた人
    p#s(left: 20px; top: 70px; font-size: 15px; font-family: m; color: #FFB3A5; white-space: nowrap) 完走者8,214人のうち
    p#p(right: 20px; top: 5px; font-size: 61px; line-height: 1; font-family: n; font-style: italic; color: $fast) 52%
    p#c(right: 20px; top: 71px; font-size: 16px; font-family: m; color: #FFB3A5) 4,277人
  # 主役の札: 「キロ +64秒」(赤の縁の暗い札・1.7 倍から叩きつける)
  div#call(left: 92px; top: 371px; width: 280px; height: 133px; border-radius: 15px; background: #070B14E0; border: 2px solid $fast; box-shadow: 0px 7px 27px #FF4D2E59; in: {scale:1.7, opacity:0, duration:0.3, ease:'power4.out'})
    p#k(left: 16px; top: 12px; font-size: 17px; color: #FFB3A5; white-space: nowrap) 35〜40km｜最初の5kmより
    p#ki(left: 16px; top: 76px; font-size: 29px; line-height: 1; white-space: nowrap) キロ
    p#v(left: .ki.right+4; top: 44px; font-size: 75px; line-height: 1; font-family: n; font-style: italic; color: $fast; white-space: nowrap) +64秒

# s5 入り方で 3 群: 左右の向きの札 → 36 / 42 / 22% の帯が左から順に伸び → 3 群の札が左から入る → 「飛ばし」で他の 2 枚が沈み、飛ばしの札が赤く光って 36% が弾む
section#s5(stagger: {each:0})
board#b5(k: "GROUP"; t: "入り方で3グループに"; s: "前半のペースを、申込時の目標ペースと比べる"; fn: "※前半のペースを申告した目標タイムのペースと比較して分類"; c: $even)
  p#axl(left: 32px; top: 157px; font-size: 16px; color: $coral; white-space: nowrap; delay: 200; in: {opacity:0, duration:0.3}) ◀ 目標より速く入った
  p#axr(right: 32px; top: 157px; font-size: 16px; color: $slow; white-space: nowrap; delay: 200; in: {opacity:0, duration:0.3}) 目標より遅く入った ▶
  div#sa(left: 32px; top: 184px; width: 207px; height: 83px; border-radius: 12px 0px 0px 12px; background: $fast; delay: 220; in: {scaleX:0, duration:0.35, ease:'power3.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 41px; font-family: n; font-style: italic; color: #FFFFFF) 36%
  div#sb(left: 239px; top: 184px; width: 242px; height: 83px; background: $even; delay: 400; in: {scaleX:0, duration:0.35, ease:'power3.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 41px; font-family: n; font-style: italic; color: #062A26) 42%
  div#sc(left: 481px; top: 184px; width: 127px; height: 83px; border-radius: 0px 12px 12px 0px; background: $slow; delay: 580; in: {scaleX:0, duration:0.35, ease:'power3.out', pivot:'left'})
    p#t(cx: 50%; cy: 50%; font-size: 41px; font-family: n; font-style: italic; color: #0A0E17) 22%
  gcard#g(top: "293;416;539"; nm: "飛ばし;設定どおり;抑えめ"; df: "前半が目標より2%以上速い;前半が目標の±2%以内;前半が目標より2%以上遅い"; pc: "36%;42%;22%"; ct: "2,957人;3,450人;1,807人"; c: "$fast;$even;$slow") ×3

# s6 貯金が借金に: 目標の縦の破線を挟み、前半の貯金 (黄緑・左へ) → 後半の借金 (赤・右へ・板が揺れる) → 差し引き +7:40 (斜線) → 下段で 3 群の遅れの横棒 → 設定どおりの端から破線が下り、飛ばしの棒の差の分が白の斜線で光り「3分50秒の損」の札が叩きつけられる
section#s6(stagger: {each:0})
board#b6(k: "飛ばし"; t: "貯金が、借金に変わる"; s: "目標タイムとのずれ（中央値）"; fn: "※設定どおり：前半−0:20・後半+4:10／抑えめ：前半+3:10・後半+1:50"; c: $fast)
  chip#k(font-size: 18px; line-height: 1.3; font-family: j; font-style: normal; letter-spacing: 0.02em; color: #FFFFFF)
  p#lgl(left: 32px; top: 159px; font-size: 16px; color: $lime; white-space: nowrap; delay: 200; in: {opacity:0, duration:0.3}) ◀ 貯金（目標より速い）
  p#lgr(right: 32px; top: 159px; font-size: 16px; color: $coral; white-space: nowrap; delay: 200; in: {opacity:0, duration:0.3}) 借金（目標より遅い）▶
  shape#axis(left: 312px; top: 189px; width: 2px; height: 213px; path: line_v; border: 2px solid #FFFFFF73; dash: 5,4; delay: 200; in: {scaleY:0, duration:0.4, ease:'power2.out', pivot:'top'})
  p#axl(cx: 313px; top: 407px; font-size: 15px; color: $pale; delay: 200; in: {opacity:0, duration:0.3}) 目標
  p#rk(left: 32px; top: "207;274;340"; font-size: 21px; color: "$ink;$ink;$coral"; delay: 200; in: {opacity:0, duration:0.3}) ×3 前半;後半;差し引き
  div#ba(left: 240px; top: 197px; width: 73px; height: 48px; border-radius: 8px; background: $lime; in: {scaleX:0, duration:0.4, ease:'power3.out', pivot:'right'})
  p#va(right: 408px; top: 199px; font-size: 40px; line-height: 1; font-family: n; font-style: italic; color: $lime; text-align: right; in: {x:27, opacity:0, duration:0.3, ease:'power3.out'}) −3:20
  p#vas(right: 408px; top: 243px; font-size: 17px; color: $lime; text-align: right; in: {x:27, opacity:0, duration:0.3, ease:'power3.out'}) 貯金
  div#bb(left: 313px; top: 264px; width: 242px; height: 48px; border-radius: 8px; background: $fast; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
    p#t(left: 15px; cy: 50%; font-size: 17px; white-space: nowrap; in: {opacity:0, duration:0.2}) 借金 {nb}+11:00{/}
  div#bc(left: 313px; top: 331px; width: 169px; height: 48px; border-radius: 8px; background: #FF4D2ED9; pattern: hatch,-45,#FF4D2E73,19,9; border: 2px solid $fast; in: {scaleX:0, duration:0.45, ease:'power3.out', pivot:'left'})
  p#vc(left: 492px; top: 333px; font-size: 40px; line-height: 1; font-family: n; font-style: italic; color: $fast; in: {x:-20, opacity:0, duration:0.3, ease:'power3.out'}) +7:40
  p#vcs(left: 492px; top: 377px; font-size: 17px; in: {x:-20, opacity:0, duration:0.3, ease:'power3.out'}) の遅れ
  div#rule(left: 32px; top: 424px; width: 576px; height: 1px; background: #FFFFFF1A; delay: 200; in: {opacity:0, duration:0.3})
  p#h6b(left: 32px; top: 437px; font-size: 20px; white-space: nowrap; in: {y:13, opacity:0, duration:0.3, ease:'power3.out'}) 差し引きの遅れ（中央値）
  hrow#cr(top: "475;533;592"; k: "設定どおり;抑えめ;飛ばし"; bw: "131;170;261"; v: "+3:50;+5:00;+7:40"; c: "$even;$slow;$fast"; in: {opacity:0, duration:0.15, stagger:{each:0.16}}) ×3
  # 設定どおりの棒の端から下りる破線と、飛ばしの棒の差の分 (白の斜線)
  shape#guide(left: 277px; top: 477px; width: 2px; height: 152px; path: line_v; border: 2px solid #FFFFFFB3; dash: 5,4; in: {scaleY:0, opacity:0, duration:0.3, pivot:'top'})
  div#loss(left: 277px; top: 595px; width: 130px; height: 32px; border-radius: 0px 7px 7px 0px; pattern: hatch,-45,#FFFFFF55,13,7; border: 2px solid #FFFFFF; in: {scaleX:0, opacity:0, duration:0.3, ease:'power3.out', pivot:'left'})
  # 「設定どおりより 3分50秒 の損」(赤の札・上向きの三角の尾)
  shape#tri(points: "320,629 334,641 306,641"; background: $fast; in: {scale:1.8, opacity:0, duration:0.3, ease:'power4.out'})
  div#call(left: 195px; top: 641px; width: 413px; height: 67px; border-radius: 12px; background: $fast; box-shadow: 0px 8px 27px #FF4D2E80; in: {scale:1.8, opacity:0, duration:0.3, ease:'power4.out'})
    p#t(cx: 50%; cy: 50%; font-size: 23px; line-height: 1; white-space: nowrap) 設定どおりより {big}3分50秒{/}{so}の損{/}

# s7 結果: 30km 以降の大失速の横棒 3 本 (0 / 50 / 100% の目盛り) → 70% で他を沈め値が弾む → 目標達成率の横棒 3 本と全体 29.9% の金の破線 → 21% で他を沈め板が揺れる
section#s7(stagger: {each:0})
board#b7(k: "RESULT"; t: "飛ばすと、後半に崩れる"; s: "入り方の3グループで比較"; fn: "※大失速＝30km以降にキロ30秒以上ペースが落ちた人"; c: $fast)
  p#h7a(left: 32px; top: 159px; font-size: 23px; white-space: nowrap; delay: 200; in: {y:13, opacity:0, duration:0.3, ease:'power3.out'}) 30km以降の大失速 {lb}キロ30秒以上のペースダウン{/}
  div#sc(left: "147;347;547"; top: 197px; width: 2px; height: 147px; background: #FFFFFF14; delay: 200; in: {opacity:0, duration:0.3}) ×3
  p#sl(cx: "148;348;548"; top: 347px; font-size: 13px; font-family: n; color: #6F7A8C; delay: 200; in: {opacity:0, duration:0.3}) ×3 0;50;100%
  hrow#ra(top: "200;248;296"; k: "飛ばし;設定どおり;抑えめ"; bw: "280;172;160"; v: "[count:70 start=0 ms=600]%{s} 2,070人{/};43%{s} 1,484人{/};40%{s} 723人{/}"; c: "$fast;$even;$slow"; o: "1;0.85;0.85") ×3
    p#v(transform-origin: 0% 60%)
  p#h7b(left: 32px; top: 399px; font-size: 23px; white-space: nowrap; in: {y:13, opacity:0, duration:0.3, ease:'power3.out'}) 目標達成率 {lb}申告した目標タイムを達成{/}
  shape#avg(left: 265px; top: 435px; width: 2px; height: 152px; path: line_v; border: 2px solid #FFC83DD9; dash: 5,4; in: {scaleY:0, opacity:0, duration:0.35, pivot:'top'})
  p#avgl(left: 272px; top: 589px; font-size: 14px; color: $gold; white-space: nowrap; in: {opacity:0, duration:0.25}) 全体 29.9%（2,456人）
  hrow#rd(top: "440;488;536"; k: "飛ばし;設定どおり;抑えめ"; bw: "84;152;116"; v: "[count:21 start=0 ms=600]%{s} 621人{/};38%{s} 1,311人{/};29%{s} 524人{/}"; c: "$fast;$even;$slow"; o: "1;0.85;0.85") ×3
    p#v(transform-origin: 0% 60%)

# s8 おすすめ: 海沿いを落ち着いて走るランナーの写真に閃光 → 上に金の札「BEST PACE」と問い → 下の板に「キロ 4〜7秒 ゆっくり」が叩きつけられ → 達成率の輪が 47% まで描かれ、4 群の横棒が並び、注記
section#s8(stagger: {each:0})
img#s8_img(inset: 0; subject: 25%,20%,50%,80%; face: 40%,25%,20%,9%; room: top 20%; main: kb,1.2>1.04,ease=power1.out) [photo]縦長 9:16 の写真。マラソン序盤、海沿いの遊歩道を他のランナーに混じってリラックスして走る、落ち着いて集中した市民ランナーを正面からやや引いて撮る。左手首の GPS スポーツウォッチにちらりと目をやる。柔らかい朝の光、涼しい青と青緑の色調、浅い被写界深度、時計の画面は抽象的な光だけ。主役は画面の左右の中央。画面の上 2 割は霞んだ空と遠くの山並みだけで人の頭を入れない (主役の頭のてっぺんは上から 2 割の高さ)。主役の顔は画面の上から 25〜32% の高さ、肩と胴と腕時計は画面の中ほど (上から 35〜60%)、下 4 割は走る脚と濡れた路面。背後のランナーも頭は上から 2 割より下。
veil#s8_shade(background: linear(#070B14D9,#070B1440@16%,#070B1426@26%,#070B14BF@36%,#070B14F2,180); in: none)
chip#s8_chip(cx: 360px; top: 157px; background: $gold; in: {y:-20, opacity:0, duration:0.3}) BEST PACE
p#s8_q(cx: 360px; top: 201px; font-size: 40px; line-height: 1.2; stroke: #070B14,5; white-space: nowrap; in: {scale:1.3, opacity:0, duration:0.35, ease:'power3.out'}) いちばん目標を達成したのは？
board#b8(k: "おすすめ"; t: "前半は、目標より少しだけ遅く"; c: $gold; top: 445px; height: 468px; background: #0A0F1CE6; delay: 0)
  chip#k(font-size: 18px; line-height: 1.3; font-family: j; font-style: normal; letter-spacing: 0.02em)
  p#big(cx: 320px; top: 124px; font-size: 43px; line-height: 1; white-space: nowrap; in: {scale:1.6, opacity:0, duration:0.32, ease:'power4.out'}) キロ{gd}4〜7秒{/}ゆっくり
  p#sub(cx: 320px; top: 245px; font-size: 19px; font-family: m; color: $pale; white-space: nowrap; in: {y:11, opacity:0, duration:0.3, ease:'power3.out'}) 設定どおり群のうち、目標より1〜2%遅く入った812人
  # 達成率の輪 (紺の輪の上に金の弧が 0 → 47% を 0.8 秒で描く)
  div#donut(left: 29px; top: 279px; width: 153px; height: 153px; in: {scale:0.6, opacity:0, duration:0.35, ease:'back.out(2)'})
    shape#ring.ellipse(left: 15px; top: 15px; width: 122px; height: 122px; background: none; border: 19px solid #263047)
    shape#arc(path: "M76.5 15.5 L91.4 17.3 L105.3 22.7 L117.6 31.4 L127.3 42.7 L134 56.1 L137.2 70.8 L136.8 85.7 L132.7 100.1 L125.3 113.1 L114.9 123.9 L102.2 131.8 L87.9 136.4"; background: none; border: 19px solid $gold; in: draw,800,ease=power2.out)
    p#c(cx: 50%; top: 45px; font-size: 57px; line-height: 1; font-family: n; font-style: italic; color: $gold; white-space: nowrap) [count:47 start=0 ms=800]%
    p#cl(cx: 50%; top: 104px; font-size: 15px; white-space: nowrap) 目標達成率
  hrow#r(left: 200px; width: 413px; height: 31px; top: "285;321;357;393"; k: "少し遅め;設定どおり;抑えめ;飛ばし"; bw: "163;132;101;73"; v: "47%{s} 382人{/};38%;29%;21%"; c: "$gold;$even;$slow;$fast"; o: "1;0.8;0.8;0.8"; in: {opacity:0, duration:0.15, stagger:{each:0.12}}) ×4
    p#k(top: 3px; font-size: 17px)
    div#bar(left: 100px; height: 23px)
    p#v(top: -1px; font-size: 29px)
  p#note(left: 32px; top: 440px; font-size: 15px; font-family: m; color: $sub; white-space: nowrap; in: {y:9, opacity:0, duration:0.3, ease:'power3.out'}) 目標とのずれ {g}+2:10{/}（前半+1:30・後半+0:40）｜飛ばしと{g}5分30秒{/}の差

# s9 まとめ: ゴールで両手を挙げる後ろ姿の逆光の写真に、まとめの札 3 枚が左から順に入る → 「前半は」とゴールテープが張られ → 「「少し遅い」が正解。」が叩きつけられ (閃光) テープが左右に切れて飛ぶ
section#s9(stagger: {each:0})
img#s9_img(inset: 0; subject: bottom 55%; room: top 45%; main: kb,1.14>1.02,ease=power1.out) [photo]縦長 9:16 の写真。両手を高く挙げてゴールに飛び込む市民マラソンランナーを後ろから見た姿。湾岸の街のスカイラインの上の金色の太陽に逆光で照らされたシルエット、ゴールのアーチの影。祝福と感動の雰囲気、暖かい橙と深い紺の色調。人物は画面の下半分の中央、上半分は広い空。
veil#s9_shade(background: linear(#070B14E0,#070B14B3@40%,#070B148C@62%,#070B14E6,180); in: none)
div#s9_head(left: 40px; top: 155px; width: 640px; height: 40px; delay: 80; in: {x:-40, opacity:0, duration:0.35, ease:'power3.out'})
  chipj#k(left: 0px; cy: 50%) まとめ
  p#t(left: .k.right+12; cy: 50%; font-size: 27px; white-space: nowrap) 数字が示す3つのこと
div#tk(left: 40px; top: "211;332;453"; width: 640px; height: 109px; border-radius: 16px; background: #080C16D6; border: 1px solid #FFFFFF1A; delay: 150; in: {x:-80, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.3}}) ×3
  div#bl(left: 0px; top: 0px; width: 8px; height: 100%; border-radius: 16px 0px 0px 16px; background: "$lime;$lime;$gold")
  p#no(left: 17px; top: 12px; font-size: 69px; line-height: 1; font-family: n; font-style: italic; color: "$lime;$lime;$gold") 1;2;3
  p#tx(left: 80px; cy: 50%; font-size: 25px; line-height: 1.32; white-space: nowrap) 完走者の{r}8割近く{/}が後半に失速。[br]崩れは{r}30km{/}から始まる;飛ばすと貯金{hl}3:20{/}が借金{r}11:00{/}に。[br]設定どおりより{r}3分50秒{/}の損;目標より{g}キロ数秒{/}遅く入る人が、[br]いちばん目標を達成している
p#s9_a(cx: 360px; top: 600px; font-size: 43px; line-height: 1.2; white-space: nowrap; in: {y:20, opacity:0, duration:0.3, ease:'power3.out'}) 前半は
p#s9_b(cx: 360px; top: 651px; font-size: 60px; line-height: 1.2; letter-spacing: -0.02em; text-shadow: 0px 5px 27px #000000B3; white-space: nowrap; in: {scale:1.7, opacity:0, duration:0.32, ease:'power4.out'}) {g}「少し遅い」{/}が正解。
# ゴールテープ (中央から左右へ張られ、決めの語で左右に切れて飛ぶ)
div#tape_l(left: 0px; top: 787px; width: 360px; height: 7px; background: $gold; box-shadow: 0px 0px 16px #FFC83DB3; in: {scaleX:0, opacity:0, duration:0.3, ease:'power2.out', pivot:'right'}; out: {x:-200, rotation:-8, opacity:0, duration:0.5, ease:'power2.in'})
div#tape_r(left: 360px; top: 787px; width: 360px; height: 7px; background: $gold; box-shadow: 0px 0px 16px #FFC83DB3; in: {scaleX:0, opacity:0, duration:0.3, ease:'power2.out', pivot:'left'}; out: {x:200, rotation:8, opacity:0, duration:0.5, ease:'power2.in'})
```

```timeline.txt
#v2
cast n = "明るくエネルギッシュな若い男性のナレーター、スポーツ番組のように歯切れのよい声" manner="スポーツ番組のナレーターのように、明るくエネルギッシュに、テンポよく歯切れよく、やや早口で読む"
# 場面の境は声の終わりの 0.18 秒後・次の声はその 0.22 秒後 (hf の間)
silence head=0 tail=180
# 切替: 斜めの紺の板 (skew -14・左から入って覆い切り右へ抜ける) = `transition panel` (板が覆い切った所で場面が替わる・600 ms = 覆う 255 / 覆ったまま 75 / 抜ける 270)
# engine: hf の板の先頭の縁 (黄緑 90 px → 紺の隙間 → 赤 26 px) は panel に書けない (板は 1 色)・panel は常設の上端の帯 (hdr・prog・runner) も覆う (hf は帯 z6 が板 z5 の上に残る)

*** s1
bgm music
@n: [silence:950][♪sw_start -4dB -830][♪whoosh -6dB -180][♪impact -6dB -140][>#s1_kick -170][>#s1_title.l1 -120][flash 0.5 -120][>#s1_title.l2]前半を飛ばしたランナーは、[>#s1_title.nanpun -40][flash 0.35 -20][♪impact -30][!#s1_title shake,9,duration=300 +20][>#s1_title.son +300][!#s1_title.nanpun to,{scale:1.04, duration:0.5, ease:'sine.inOut', repeat:1, yoyo:true} +500]何分損したのか？
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh -6dB -140

*** s2
[>#subtitle]
@n: [silence:220][>#b2.lbl -50]完走者[>#b2.big -120][>#b2.unit -120][♪pop -5dB -50][>#b2.rate +450][>#b2.bar +450]{hl}8,214人{/}の、[|][>#b2.ca -80][>#b2.ca.dot[*] +50][>#b2.ca.dl[*] +85][♪pop -8dB]5kmごとの記録と[>#b2.x -150][>#b2.cb -50][♪pop -8dB]目標タイムを[>#b2.match -100][♪bell -3dB]{突き合わせ|突き合わせました}。
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh2 -6dB -140

*** s3
@n: [silence:220]後半の方が速かったのは、わずか[>#b3.lga -100][>#b3.wnc[*] {stagger:{each:0.05}} -50][>#b3.lgb +750][>#b3.wec[*] {stagger:{each:0.012}} +750][♪pop -4dB]{hl}7.3%{/}。
@: [>#b3.lgc -100][>#b3.wpc[*] {stagger:{each:0.007}} -80][!#b3 shake,5,duration=300 +50][♪impact -2dB]{hl}78.1%{/}は、[>#b3.medh -150][>#b3.mka -50][>#b3.mba -50][>#b3.mkb +150][>#b3.mbb +150][>#b3.badge +600]後半に[!#b3.lgc.h{tf} recolor,$fast,duration=200 -50][!#b3.lgc.h punch,1.08,duration=400 -50]{hl}2分以上{/}遅れました。
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh -6dB -140

*** s4
@n: [silence:220][>#b4.la][>#b4.pa[*] +20][>#b4.va[*] +20]崩れるのは[>#b4.zone -50][>#b4.m30 -50][>#b4.chip -20][♪negative -3dB to=1.75s]{hl}30km{/}から。[|]
@: [>#b4.lb -100][>#b4.pb[*] -100][>#b4.vb[*] -100][>#b4.d40 +450]35〜40kmでは、[>#b4.info -100]最初の5kmより、[|]キロ[>#b4.call -60][!#b4 shake,8,duration=300][flash 0.25 -40][♪impact -20]{hl}64秒{/}も遅くなります。
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh2 -6dB -140

*** s5
@n: [silence:220][>#b5.g[*] +50]目標より2%以上速く入った[|][!#b5.g[2] to,{opacity:0.45, duration:0.25} -50][!#b5.g[3] to,{opacity:0.45, duration:0.25} -50][!#b5.g[1] to,{scale:1.04, duration:0.25} -50][!#b5.g[1] glow,#FF4D2E73,blur=33 -50][♪pop -5dB]「飛ばし」{は|は、}[!#b5.g[1].pc to,{scale:1.18, duration:0.3, ease:'back.out', pivot:'100% 20%'} -50][!#b5.sa to,{scaleY:1.12, duration:0.2} -50][!#b5.sa to,{scaleY:1, duration:0.2} +150][♪impact -4dB]{hl}36%{/}。
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh -6dB -140

*** s6
@n: [silence:220]前半[>#b6.ba -50][>#b6.va +100][>#b6.vas +100][♪bell -3dB]{hl}3分20秒{/}の貯金が、[|]後半は[>#b6.bb -80][>#b6.bb.t +250][!#b6 shake,5,duration=300 +50][♪negative -2dB to=1.75s]{hl}11分{/}の[>#b6.bc +350][>#b6.vc +600][>#b6.vcs +600]借金に。
@: [>#b6.h6b -200][>#b6.cr[*] -100]設定どおりの人より、[>#b6.guide -350][>#b6.loss -150][>#b6.tri -60][>#b6.call -60][flash 0.25 -40][♪impact -20]{hl}3分50秒{/}の損です。
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh2 -6dB -140

*** s7
@n: [silence:220][>#b7.ra[*] +150]飛ばした人は、30km以降の大失速が[!#b7.ra[2] to,{opacity:0.4, duration:0.25} -50][!#b7.ra[3] to,{opacity:0.4, duration:0.25} -50][!#b7.ra[1].v to,{scale:1.25, duration:0.25, ease:'back.out'} -50][♪pop -4dB]{hl}70%{/}。
@: [>#b7.h7b -250][>#b7.rd[*] -100][>#b7.avg +400][>#b7.avgl +600]目標達成率は、[!#b7.rd[2] to,{opacity:0.4, duration:0.25} -50][!#b7.rd[3] to,{opacity:0.4, duration:0.25} -50][!#b7.rd[1].v to,{scale:1.3, duration:0.25, ease:'back.out'} -50][!#b7 shake,5,duration=300 +20][♪negative -3dB to=1.75s]{hl}21%{/}どまり。
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh -6dB -140

*** s8
@n: [silence:220][flash 0.4 -95][♪rise -3dB -170][>#s8_chip -100][>#s8_q -20][>#b8 +900]いちばん達成したのは、[|]前半を[>#b8.big -60][>#b8.sub +500][♪whoosh -5dB -40]キロ{hl}4〜7秒{/}ゆっくり入った人。
@: 達成率は[>#b8.donut -450][>#b8.r[*] +100][>#b8.note +700][♪sparkle]{hl}47%{/}です。
transition panel,600,color=#0B1224,skew=-14,dir=right,se=whoosh2 -6dB -140

*** s9
@n: [silence:220][♪pop -8dB -70][♪pop -8dB +230][♪pop -8dB +530]最初の5kmは我慢して、30kmに余力を。
@: [>#s9_a -100][>#tape_l][>#tape_r]前半{は|は、}[>#s9_b -80][flash 0.4 -60][<#tape_l -40][<#tape_r -40][♪impact -4dB -50][♪sparkle -3dB +20][!#s9_b glow,$gold +300][=#s9_b +700]「少し遅い」が正解[♪sw_start -4dB +1290]です。[silence:1.4s]
```

# data · support-tickets (hf 全力版の全量の写し — 問い合わせ 4,000 件を分類してわかったこと・暗い地に番号つきの見出しと題つきの板を場面ごとに組む 10 場面のデータ図解) — canvas 1280x720

見せる作り: 全編の地 (紺の放射の地 + 斜めに流れる方眼 + 2 つの光 + grain)・2 場面目から常設の上端の帯 (題・9 つの点と「0N / 09」・全編で伸びる進行線) と下端の出典の帯・光の縦線が左から払う場面の切替・場面 = 番号の札 + mask から上がる見出し + 題つきの板 1〜2 枚 (板の def)・数字の語で伸びる図 (数える 3 枚の札・4 列の流れ図・縦棒と破線の伸び・構成比の帯と 7 行の横棒・弧を描く輪と全体の破線・6 本の分布とかぎと中央値の札・2 本の積み上げとつなぐ帯・斜線の帯と合計の枠・実績 / 目標の 2 本の棒)・語で点く行の枠と沈む他の行・まとめの 3 行から締めの題へ幕が明けて暗転・字幕なし・音の層 (切替の風切り + 語に結んだ効果音)

```design.txt
#v2
# 学ぶ作り: 暗い data の design system を根に 1 回 (palette・書体 4・数字の run・場面の見出し head・題つきの板 board の def) → 場面は板の中身だけ
# 常設の層: 全編の地 (紺の放射の地 + 流れる方眼 + 2 つの光 + grain) を根に・2 場面目から sticky の上端の帯 (題・9 つの点と「0N / 09」・全編で伸びる進行線) と下端の出典の帯
# 場面 = 番号つきの見出し + 板 1〜2 枚。板の骨組み (目盛り・行の札) は場面の頭に組み上げ、台詞の数字の語で枠が点き・棒が伸び・数字が数える。場面の切替は光の縦線が左から右へ払う wipe
# hf d10 support-tickets (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。字幕は無い (hf の作り)
canvas 1280x720 bg=#0A0F17
theme dark
palette bg=#0A0F17 panel2=#152030 line=#233148 line2=#2C3D58 fg=#E9EEF5 fg2=#C3CDDA muted=#8F9DB1 teal=#2EC4B6 teal2=#7ADFD3 amber=#F6C35B orange=#F2914A coral=#E8615A slate=#8A97AD slate2=#5C677A
font "すっきりした現代的な角ゴシック体の太字、IT 企業の資料らしい癖のない字形"
fonts r="すっきりした現代的な角ゴシック体の標準の太さ、IT 企業の資料らしい癖のない字形"
fonts g="すっきりした現代的な角ゴシック体の太字、IT 企業の資料らしい癖のない字形"
fonts n="縦長に詰まった欧文のコンデンス体のサンセリフのセミボールド、太くくっきりした数字、ダッシュボードの KPI の数字向け"
fonts m="すっきりした欧文の等幅体"
sfx off
# hf の作り: 場面の見出しは台詞より先に結論を出す (見出し → 板 → 台詞が数字を読む)・板の骨組みは場面の頭に全部組む
lint off=spoiler,all_at_once
# hf の作り: 板の題の補足・目盛り・凡例・注記・出典の帯は 11〜13 px (1080 の 17〜19 px)
lint off=small_text
# hf の作り: 図の色 (グラデの端・半透明の地・薄い線) は場面ごとに直書き
lint off=palette_drift
# hf の作り: 絵は題・ヘルプページ・締めの 3 枚だけで、場面 2〜8 は暗い地の上の板と図だけ (字幕も無い)
lint off=text_only_cut,empty_cut,blank_band
# hf の作り: 板の注記・結論の矢印の行は場面の終わり近くに出て 1〜2 秒で次の場面へ払われる
lint off=flash_text,entrance_in_fadeout
# hf の作り: ヘルプページの場面は 2 本の帯が伸びた後「合わせて」の枠まで 6 秒ほど画面が止まる・締めの場面は引き継ぎの絵 1 枚を濃い幕の下に 16 秒敷く
lint off=still_stretch,photo_hidden,same_picture
# hf の作り: 台詞の「7月から9月」「3か月」は hf の台詞のまま (読みは後段の読み検査に任せる)
lint off=month_reading
run t { color: $teal2 }
run a { color: $amber }
run c { color: $coral }
run b { color: $fg }
run mu { color: $muted; font-family: r; font-size: 12px }
run sp { color: #7E8796 }
run sc { color: $muted; font-family: r }
run big { color: $amber; font-family: n; font-size: 79px }
run nf { color: $fg; font-family: n; font-size: 35px }
run ar { color: $teal2; font-size: 23px }
run n21 { color: $fg; font-family: n; font-size: 21px }
run n19 { color: $teal2; font-family: n; font-size: 19px }
run n16 { color: $fg2; font-family: n; font-size: 16px }
run an { color: $fg; font-family: n; font-size: 21px }
run ab { color: $amber }
run arr { color: $fg2; font-size: 43px }
run u21 { color: $fg; font-family: g; font-size: 21px }
run cb { color: $coral }
sound telop = "電子的なテロップの出現音、短いデジタルのきらめき"
sound pop = "柔らかく短いポップ音"
sound blip = "柔らかい短い電子のブリップ音"
sound chime = "短く澄んだチャイム"
sound swish = "乾いた短いシュッという音"
sound whoosh = "低く柔らかい風切りのウーッシュ"
sound click = "乾いた短いクリック音"
sound chime_low = "低めに響く落ち着いたチャイム"
sound chime_warm = "温かみのある柔らかなチャイム"
sound shimmer = "低めのきらめくシマー音、余韻が残る"
# 上端の帯の題の印 (紺の角丸の枠 + 青緑の 3 本線)・方法の板の矢印 (線 + 青緑の山形)
svg mark = """<svg viewBox="0 0 30 30"><rect x="1" y="1" width="28" height="28" rx="7" fill="#152030" stroke="#7adfd3" stroke-width="1.5"/><path d="M8 11h14M8 15.5h10M8 20h7" stroke="#7adfd3" stroke-width="2" stroke-linecap="round"/></svg>"""
svg arrow = """<svg viewBox="0 0 64 24"><path d="M2 12h54" stroke="#3d5373" stroke-width="3" stroke-linecap="round"/><path d="M48 4l10 8-10 8" fill="none" stroke="#7adfd3" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
# 上端の帯の点: 今の場面を青緑で 1.3 倍に、前の場面を暗い青緑に戻す
cue step(x, p) = [!#x to,scale=1.3,duration=50][!#x recolor,#2EC4B6,duration=50][!#p to,scale=1,duration=50][!#p recolor,#3F6B78,duration=50]
p { color: $fg; line-height: 1.2; out: none }
div { border-radius: 0px; background: none; padding: 0px; border: none; box-shadow: none; out: none }
img { out: none }
shape { out: none }
svg { out: none }
icon { out: none }
group { out: none }
# 曲: 頭の 1 秒と締めの題の 2 秒だけ前に出し、台詞の間は下げる (締めの場面は少し上げる)
bgm#music(keys: "0:+7.5|800ms:+7.5|1400ms:0|end-16.1s:0|end-15.1s:+3|end-2.6s:+3|end-2s:+9|end-1.3s:+8"; fade: 600,1300) シンセのアルペジオが静かに刻む知的なサイエンス系の電子音楽、柔らかいパッドと控えめなビート、主旋律なし、データ分析の解説向け

# 場面の見出し: 番号の札 + 小見出し (左から) → 見出し (下の mask から上がる・語の強調は run t / a / c)
def head(n, k, t) = div(left: 64px; top: 83px; width: 1152px; height: 80px)
  div#k(left: 0px; top: 0px; width: 700px; height: 22px; delay: 120; in: {x:-17, opacity:0, duration:0.5, ease:'power3.out'})
    p#no(left: 0px; cy: 50%; font-size: 13px; font-family: m; color: $bg; background: $teal2; border-radius: 3px; padding: 1px 6px; content: {n})
    p#t(left: .no.right+9; cy: 50%; font-size: 15px; color: $teal2; letter-spacing: 0.06em; white-space: nowrap; content: {k})
  p#h(left: 0px; top: 31px; font-size: 35px; line-height: 1.22; letter-spacing: -0.01em; white-space: nowrap; delay: 200; in: {y:49, duration:0.75, ease:'expo.out', clip:true}; content: {t})
# 題つきの板: 半透明の紺 + 細い縁 + 深い影・頭の行 (色の縦棒 + 題 + 右の単位) と下の罫
def board(t, u, pc=$teal) = div(border-radius: 12px; background: #111925E6; border: 1px solid $line; box-shadow: 0px 16px 40px #00000059; in: {y:24, opacity:0, duration:0.65, ease:'power3.out'})
  div#pip(left: 21px; top: 19px; width: 7px; height: 17px; border-radius: 2px; background: {pc})
  p#t(left: 37px; cy: 27px; font-size: 17px; white-space: nowrap; content: {t})
  p#u(right: 21px; cy: 27px; font-size: 12px; color: $muted; font-family: r; white-space: nowrap; content: {u})
  div#rule(left: 21px; right: 21px; top: 49px; height: 1px; background: $line)
# 札の行の色の四角 + 名 (カテゴリの名札)
def cat(t, c) = div(width: 253px; height: 24px)
  div#sw(left: 0px; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: {c})
  p#t(left: 21px; cy: 50%; font-size: 16px; white-space: nowrap; content: {t})
# 目標の札 (上端の色の帯 + 番号 + 題 + 大きな目標値 + 実績 + 実績 / 目標の 2 本の棒 + 説明)
def goal(ix, t, g, u, f, c, gw, tw, gv, tv, d) = div(top: 200px; width: 363px; height: 440px; border-radius: 12px; background: #111925E6; border: 1px solid $line; box-shadow: 0px 16px 40px #00000059; in: {y:33, opacity:0, duration:0.6, ease:'power3.out'})
  div#top(left: 0px; top: 0px; width: 363px; height: 5px; border-radius: 12px 12px 0px 0px; background: {c})
  p#ix(left: 23px; top: 25px; font-size: 12px; font-family: m; color: $muted; border: 1px solid $line2; border-radius: 3px; padding: 0px 5px; content: {ix})
  p#t(left: 56px; top: 23px; font-size: 17px; white-space: nowrap; content: {t})
  p#g(left: 23px; top: 66px; font-size: 100px; line-height: 0.9; font-family: n; color: {c}; content: {g})
  p#u(left: .g.right+7; top: 124px; font-size: 20px; content: {u})
  p#f(left: 23px; top: 180px; font-size: 15px; color: $fg2; font-family: r; white-space: nowrap; content: {f})
  p#k1(left: 23px; top: 229px; font-size: 11px; color: $muted) 実績
  div#b1(left: 73px; top: 226px; width: {gw}; height: 20px; border-radius: 0px 3px 3px 0px; background: #8A97AD59; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#v1(left: 283px; top: 224px; width: 57px; text-align: right; font-size: 20px; font-family: n; color: $muted; content: {gv})
  p#k2(left: 23px; top: 269px; font-size: 11px; color: $muted) 目標
  div#b2(left: 73px; top: 266px; width: {tw}; height: 20px; border-radius: 0px 3px 3px 0px; background: {c}; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#v2(left: 283px; top: 264px; width: 57px; text-align: right; font-size: 20px; font-family: n; content: {tv})
  div#rule(left: 23px; top: 347px; width: 317px; height: 1px; background: $line)
  p#d(left: 23px; top: 359px; width: 317px; font-size: 14px; line-height: 1.55; color: $fg2; font-family: r; content: {d})
# まとめの行 (左の色の縁 + 番号 + 大きな数字 + 太字の 1 行 + 補足)・文の列は hf の 389 px より 11 px 右 (数字の書体が hf より幅広く「43% → 75%」が文に掛かるため)
def item(ix, c, f, b, s) = div(left: 64px; width: 1152px; height: 128px; border-radius: 12px; background: #111925E0; border: 1px solid $line2; in: {x:-27, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-16, opacity:0, duration:0.6, ease:'power2.in'})
  div#edge(left: 0px; top: 0px; width: 4px; height: 128px; border-radius: 12px 0px 0px 12px; background: {c})
  p#ix(left: 27px; cy: 50%; font-size: 40px; font-family: n; color: $slate2; content: {ix})
  p#f(left: 78px; cy: 50%; font-size: 72px; line-height: 1; font-family: n; color: {c}; white-space: nowrap; content: {f})
  p#b(left: 400px; top: 34px; font-size: 23px; line-height: 1.35; white-space: nowrap; content: {b})
  p#s(left: 400px; top: 72px; font-size: 16px; color: $fg2; font-family: r; white-space: nowrap; content: {s})

# 全編の地 (根・z back): 紺の放射の地・全編で斜めに流れる方眼 (縁へ薄れる)・左上の青緑と右下の琥珀の光 (ゆっくり揺れる)・grain
div#bg_base(inset: 0; background: radial(#0F1724,#0A0F17@60%,#080C13,30%,20%); z-index: back; in: none)
div#bg_grid.bleed(left: -53px; top: -53px; width: 1386px; height: 826px; pattern: grid,32,#94A3B814; z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=-32 y=-16 ease=none),duration=106000)
div#bg_vig(inset: 0; background: radial(#0A0F1700@40%,#0A0F17D9,50%,50%); z-index: back; in: none)
div#bg_glow1.bleed(left: -253px; top: -347px; width: 733px; height: 733px; background: radial(#2EC4B621,#2EC4B600@65%,50%,50%); z-index: back; in: none; main: sine {x: 23, period: 18})
div#bg_glow2.bleed(left: 787px; top: 347px; width: 800px; height: 800px; background: radial(#F6C35B17,#F6C35B00@65%,50%,50%); z-index: back; in: none; main: sine {y: -20, period: 22})
veil#bg_grain(grain: 0.05; color: #00000000; z-index: back; in: none)

# a 題: 夜のサポート机の写真が 1.12 → 1 に引き、左の暗い余白に小札 → mask から上がる 2 行 → 副題。数字の語で 3 枚の札が弾み (4,128 は数える)、「分類」で 7 つの名札
section#a(stagger: {each:0})
img#a_img(inset: 0; subject: right 38%; room: left 60%; main: kb {scale: [1.12, 1], focus: ['70% 50%', '70% 50%']}) [photo]夜のモダンなオフィスのカスタマーサポートの机の広角。キーボードの横にヘッドセットが置かれ、2 台のモニターに問い合わせの札の列と小さな棒グラフが読めない抽象的な形で柔らかく光る。深い紺と青緑の色調に琥珀色のかすかな差し色の明かり、浅い被写界深度、暗めの照明。机とモニターは画面の右 4 割に置き、画面の左 6 割は暗く何もない余白にする。文字・数字・ロゴなし
# 左から暗くする幕 (左 97% → 右 32%) と右の主体の周りの減光
div#a_shade(inset: 0; background: linear(#0A0F17F7,#0A0F17ED@34%,#0A0F1799@58%,#0A0F1752,90))
div#a_shade2(inset: 0; background: radial(#0A0F1700@40%,#0A0F17B3,75%,45%))
div#a_kick(left: 80px; top: 113px; width: 700px; height: 24px; delay: 150; in: {x:-20, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 29px; height: 2px; background: $teal2)
  p#t(left: 39px; cy: 50%; font-size: 16px; color: $teal2; letter-spacing: 0.06em; white-space: nowrap) ワークノート サポート窓口 ｜ 7〜9 月の問い合わせ分析
p#a_t1(left: 80px; top: 156px; font-size: 65px; line-height: 1.16; letter-spacing: -0.02em; white-space: nowrap; delay: 250; in: {y:90, duration:0.85, ease:'expo.out', clip:true}) 問い合わせ {big}4,000{/} 件を
p#a_t2(left: 80px; top: 249px; font-size: 65px; line-height: 1.16; letter-spacing: -0.02em; white-space: nowrap; delay: 420; in: {y:82, duration:0.85, ease:'expo.out', clip:true}) 分類してわかったこと
p#a_sub(left: 80px; top: 350px; font-size: 19px; color: $fg2; font-family: r; white-space: nowrap; delay: 800; in: {y:12, opacity:0, duration:0.6, ease:'power2.out'}) 勤怠・経費精算 SaaS{b}「ワークノート」{/}サポート窓口の 3 か月
# 3 枚の札 (大きな数字 + 単位 + 補足)
div#a_st(left: "80;288;590"; top: 460px; width: "193;287;193"; height: 100px; border-radius: 11px; background: #111925DB; border: 1px solid $line2; in: {y:20, opacity:0, duration:0.55, ease:'back.out(1.4)'}) ×3
  p#v(left: 16px; top: 12px; font-size: 51px; line-height: 1; font-family: n; color: "$fg;$amber;$fg") 3;[count:4,128 start=0 ms=1000 delay=100];7
  p#u(left: .v.right+6; top: 36px; font-size: 17px; color: $fg2) か月;件;カテゴリ
  p#l(left: 16px; top: 70px; font-size: 13px; color: $muted; font-family: r; white-space: nowrap) 7 月・8 月・9 月;メール・チャット・フォームの合計;全件を読んで分類
# 7 つのカテゴリの名札 (色の四角 + 名・2 行に折り返す)
p#a_cat(left: "80;245;332;445;636;80;180"; top: "580;580;580;580;580;608;608"; font-size: 13px; color: $fg2; padding: 0px 0px 0px 18px; white-space: nowrap; in: {y:11, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.07}}) ×7 ログイン・アカウント;操作方法;請求・プラン;データ連携（CSV・API）;不具合の報告;権限・設定;その他
  div#sw(left: 0px; cy: 50%; width: 11px; height: 11px; border-radius: 3px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2")

# b 方法: 上端の帯と下端の出典の帯が溶けて出る (sticky・最後まで)・板の 4 列 (チャネル → 全件 → 7 分類 → 3 つの指標) を頭に組み、指標の札を語で右から
section#b(stagger: {each:0})
# 上端の帯: 題の印 + 題 (左)・9 つの点 + 「0N / 09」(右)・細い線の上の進行
div#hdr.sticky(left: 64px; top: 23px; width: 1152px; height: 27px; z-index: front; delay: 100; in: {opacity:0, duration:0.6, ease:'power2.out'})
  svg#mk(left: 0px; cy: 50%; width: 20px; height: 20px; part: mark)
  p#br(left: 29px; cy: 50%; font-size: 14px; color: $fg2; font-family: r; white-space: nowrap) ワークノート サポート窓口{sp}　｜　{/}{sc}問い合わせ分析 7〜9 月{/}
  shape#d.ellipse(left: "961;975;989;1003;1017;1031;1045;1059;1073"; cy: 50%; width: 7px; height: 7px; background: #2A3850) ×9
  p#lbl(right: 0px; cy: 50%; width: 64px; text-align: right; font-size: 12px; font-family: m; color: $muted; letter-spacing: 0.06em) 01 / 09
div#hdr_line.sticky(left: 64px; top: 61px; width: 1152px; height: 1px; background: #1C2840; z-index: front; delay: 100; in: {opacity:0, duration:0.6, ease:'power2.out'})
progress#prog.sticky(left: 64px; top: 61px; width: 1152px; height: 1px; background: linear($teal,$teal2,90); until: end; z-index: front; overlap: hdr_line)
# 下端の出典の帯
div#ftr.sticky(left: 64px; top: 680px; width: 1152px; height: 20px; z-index: front; delay: 100; in: {opacity:0, duration:0.6, ease:'power2.out'})
  p#tag(left: 0px; cy: 50%; font-size: 10px; font-family: m; color: $fg2; letter-spacing: 0.08em; border: 1px solid $line2; border-radius: 3px; padding: 0px 5px) DATA
  p#src(left: .tag.right+7; cy: 50%; font-size: 12px; color: $muted; font-family: r; white-space: nowrap) 対象：7〜9 月に届いた問い合わせ 4,128 件（メール・チャット・フォーム）
  p#own(right: 0px; cy: 50%; font-size: 12px; color: $muted; font-family: r; white-space: nowrap) ワークノート サポートチーム 社内共有
head#b_h(n: "01"; k: "分析の方法"; t: "4,128 件を 7 カテゴリに分け、{t}3 つの指標{/}で比べた")
board#b_bd(left: 64px; top: 195px; width: 1152px; height: 451px; t: "分析の流れ"; u: "対象：7〜9 月の問い合わせ 全件"; delay: 150)
  # 列の頭 (番号の枠 + 題)
  div#ch(left: "32;287;567;849"; top: 67px; width: 270px; height: 21px; delay: 400; in: {y:7, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.18}}) ×4
    p#n(left: 0px; cy: 50%; font-size: 11px; font-family: m; color: $teal2; border: 1px solid #7ADFD380; border-radius: 3px; padding: 0px 5px) 1;2;3;4
    p#t(left: 21px; cy: 50%; font-size: 14px; color: $muted; letter-spacing: 0.04em; white-space: nowrap) 受付チャネル;全件を読む;7 カテゴリに分類;3 つの指標で突き合わせ
  div#chan(left: 32px; top: "103;185;267"; width: 200px; height: 69px; border-radius: 8px; background: $panel2; border: 1px solid $line2; delay: 500; in: {x:-17, opacity:0, duration:0.45, ease:'power2.out', stagger:{each:0.1}}) ×3
    icon#i(left: 15px; cy: 50%; font-size: 25px; name: "envelope-simple;chat-centered-text;article"; color: $teal2)
    p#t(left: 52px; cy: 50%; font-size: 18px) メール;チャット;フォーム
  svg#ar(left: "235;515;797"; top: 215px; width: 43px; height: 16px; part: arrow; delay: 850; in: {scaleX:0, opacity:0, duration:0.4, ease:'power2.out', pivot:'left', stagger:{each:0.3}}) ×3
  div#ra(left: 287px; top: 103px; width: 213px; height: 235px; border-radius: 9px; background: $panel2; border: 1px solid $line2; delay: 950; in: {scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.5)'})
    p#v(cx: 50%; top: 48px; font-size: 77px; line-height: 1; font-family: n; color: $amber) 4,128
    p#u(cx: 50%; top: 129px; font-size: 19px; color: $fg2) 件
    p#s(cx: 50%; top: 166px; font-size: 13px; color: $muted; font-family: r; white-space: nowrap) 3 か月分をすべて
  div#cat(left: 567px; top: "103;137;171;205;239;273;307"; width: 220px; height: 28px; border-radius: 5px; background: #152030B3; border: 1px solid $line; delay: 1250; in: {x:-12, opacity:0, duration:0.35, ease:'power2.out', stagger:{each:0.06}}) ×7
    div#sw(left: 9px; cy: 50%; width: 11px; height: 11px; border-radius: 3px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2")
    p#t(left: 27px; cy: 50%; font-size: 13px; color: $fg2; white-space: nowrap) ログイン・アカウント;操作方法;請求・プラン;データ連携（CSV・API）;不具合の報告;権限・設定;その他
  # 3 つの指標 (語で右から弾んで入る)
  div#m(left: 849px; top: "103;184;265"; width: 273px; height: 72px; border-radius: 8px; background: $panel2; border: 1px solid $line2; in: {x:20, opacity:0, duration:0.45, ease:'back.out(1.6)'}) ×3
    p#ix(left: 13px; cy: 50%; width: 20px; text-align: center; font-size: 29px; font-family: n; color: $teal2) A;B;C
    p#b(left: 44px; top: 16px; font-size: 17px; white-space: nowrap) 初回で解決したか;解決までの時間;担当者の対応時間
    p#s(left: 44px; top: 41px; font-size: 12px; color: $muted; font-family: r; white-space: nowrap) 初回解決率;受付から解決まで;3 か月の合計・1 件あたり平均
  p#note(left: 21px; bottom: 13px; font-size: 12px; line-height: 1.5; color: $muted; font-family: r; in: {opacity:0, duration:0.5}) ※ 「解決までの時間」は受付から解決までの経過時間、「対応時間」は担当者が対応にかけた時間。

# c 月別: 右の板に縦棒 3 本が 0.15 秒ずつ伸び、値と破線の伸び (点) が乗る・「12%」で左に大きな +12% が数えて弾み、件数の前後と「利用企業」の札
section#c(stagger: {each:0})
head#c_h(n: "02"; k: "月別の件数"; t: "3 か月で {t}12% 増{/}。利用企業の増加とほぼ同じ伸び")
p#c_lab(left: 64px; top: 220px; font-size: 16px; color: $muted; delay: 300; in: {x:-13, opacity:0, duration:0.45, ease:'power2.out'}) 7 月 → 9 月の増加
p#c_pct(left: 64px; top: 280px; font-size: 153px; line-height: 0.86; font-family: n; color: $teal2; transform-origin: 0% 70%; in: {scale:0.7, opacity:0, duration:0.6, ease:'back.out(1.5)'}) +[count:12 start=0 ms=800]%
p#c_ft(left: 64px; top: 444px; font-size: 17px; color: $fg2; white-space: nowrap; in: {y:9, opacity:0, duration:0.45, ease:'power2.out'}) {nf}1,296{/} 件 {ar}→{/} {nf}1,448{/} 件
p#c_call(left: 64px; top: 507px; font-size: 15px; background: #152030F5; border: 1px solid #7ADFD38C; border-radius: 7px; padding: 7px 12px 7px 37px; white-space: nowrap; in: {x:-20, opacity:0, duration:0.5, ease:'power3.out'}) 利用企業の増加とほぼ同じ伸び
  icon#i(left: 12px; cy: 50%; font-size: 17px; name: buildings; color: $teal2)
board#c_bd(left: 467px; top: 195px; width: 749px; height: 451px; t: "月別の問い合わせ件数"; u: "単位：件"; delay: 120)
  # 目盛り (0 起点・400 刻み)
  div#gl(left: 80px; top: "80;153;227;300"; width: 627px; height: 1px; background: #94A3B81F) ×4
  div#zero(left: 80px; top: 372px; width: 627px; height: 2px; background: #3A4B66)
  p#gll(left: 0px; top: "73;146;220;293;365"; width: 71px; text-align: right; font-size: 11px; font-family: m; color: $muted) ×5 1,600;1,200;800;400;0
  div#bar(left: "127;337;545"; top: "135;119;108"; width: 113px; height: "238;254;265"; border-radius: 5px 5px 0px 0px; background: "linear(#4F6684,#3B4E68,180);linear(#5D7899,#455C7A,180);linear(#7ADFD3,#2A9D92,180)"; delay: 550; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom', stagger:{each:0.15}}) ×3
  p#bv(left: "127;337;545"; top: "145;129;117"; width: 113px; text-align: center; font-size: 31px; font-family: n; color: "$fg;$fg;#0A0F17"; delay: 950; in: {y:8, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.15}}) ×3 1,296;1,384;1,448
  p#bx(left: "127;337;545"; top: 384px; width: 113px; text-align: center; font-size: 16px; color: $fg2) ×3 7 月;8 月;9 月
  shape#trend(path: "M184 121 L393 105 L602 93"; background: none; border: 2px solid $teal2; dash: 5,5; delay: 1400; in: {opacity:0, duration:0.5})
  shape#dot.ellipse(left: "179;388;597"; top: "116;100;88"; width: 10px; height: 10px; background: $teal2; delay: 1350; in: {scale:0, duration:0.35, ease:'back.out(2.2)', stagger:{each:0.12}}) ×3
  p#note(left: 21px; bottom: 13px; font-size: 12px; color: $muted; font-family: r; in: {opacity:0, duration:0.5}) ※ 3 か月の合計は 4,128 件。縦軸は 0 から。

# d 構成: 構成比の帯 (7 色) が左から 1 枚ずつ開き、7 行の横棒が伸びて件数と % が出る・「ログイン」「操作方法」で行に枠が点き、他の 5 行を沈め、凡例
section#d(stagger: {each:0})
head#d_h(n: "03"; k: "カテゴリ別の件数"; t: "件数が多いのは {t}ログイン・アカウント{/} と {t}操作方法{/}")
board#d_bd(left: 64px; top: 195px; width: 1152px; height: 451px; t: "カテゴリ別の件数と構成比"; u: "N = 4,128 件"; delay: 120)
  div#seg(left: "21;265;498;687;853;975;1075"; top: 64px; width: "242;231;187;164;120;98;56"; height: 39px; border-radius: "5,0,0,5;0;0;0;0;0;0,5,5,0"; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2"; delay: 450; in: {scaleX:0, opacity:0, duration:0.45, ease:'power2.out', pivot:'left', stagger:{each:0.07}}) ×7
    p#t(cx: 50%; cy: 50%; font-size: 19px; font-family: n; color: "#0A0F17;#0A0F17;#0A0F17;#0A0F17;#0A0F17;#0A0F17;$fg") 22%;21%;17%;15%;11%;9%;5%
  div#r(left: 12px; top: "124;160;196;232;268;304;340"; width: 1127px; height: 36px; in: none) ×7
    # 行の枠 (語で点く 2 行だけ・他の行の枠は透明)
    div#hl(left: 0px; top: 3px; width: 1127px; height: 30px; border-radius: 7px; background: #2EC4B614; border: 2px solid #7ADFD3B3; opacity: "1;1;0;0;0;0;0"; in: {opacity:0, duration:0.35, ease:'power2.out'})
    cat#nm(left: 9px; cy: 50%; t: "ログイン・アカウント;操作方法;請求・プラン;データ連携（CSV・API）;不具合の報告;権限・設定;その他"; c: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2"; delay: "600;660;720;780;840;900;960"; in: {x:-13, opacity:0, duration:0.4, ease:'power2.out'})
    div#bar(left: 262px; cy: 50%; width: "600;573;464;409;300;245;137"; height: 20px; border-radius: 0px 4px 4px 0px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2"; delay: "750;820;890;960;1030;1100;1170"; in: {scaleX:0, duration:0.75, ease:'power3.out', pivot:'left'})
    div#val(left: 929px; cy: 50%; width: 140px; height: 30px; delay: "1050;1120;1190;1260;1330;1400;1470"; in: {x:-8, opacity:0, duration:0.4, ease:'power2.out'})
      p#n(left: 0px; cy: 50%; width: 60px; text-align: right; font-size: 24px; font-family: n) 908;867;702;619;454;371;207
      p#u(left: 69px; cy: 50%; font-size: 13px; color: $muted) 件
      p#pc(left: 89px; cy: 50%; width: 47px; text-align: right; font-size: 20px; font-family: n; color: $fg2) 22%;21%;17%;15%;11%;9%;5%
  # 色の見方 (凡例)
  div#leg(left: 21px; top: 416px; width: 1000px; height: 20px; in: {y:7, opacity:0, duration:0.5, ease:'power2.out'})
    p#t0(left: 0px; cy: 50%; font-size: 13px; color: $muted) 色の見方
    div#s(left: "75;86;251;262;273;571;582"; cy: 50%; width: 9px; height: 9px; border-radius: 2px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2") ×7
    p#t(left: "102;289;598"; cy: 50%; font-size: 13px; color: $muted; white-space: nowrap) ×3 件数が多い 2 カテゴリ;対応に時間がかかる 3 カテゴリ（後半で詳しく）;その他の 2 カテゴリ

# e 初回解決率: 右の板の 7 行が頭に伸び、「59%」で左の輪が弧を描いて数え、板に全体の破線・81 / 34 / 22 の語で行に枠 (青緑 / 珊瑚)・中の 4 行を沈める
section#e(stagger: {each:0})
head#e_h(n: "04"; k: "初回解決率"; t: "初回で解決するのは {t}59%{/}。カテゴリで大きく違う")
# 輪 (地の輪 + 59% の弧を描く + 中央の数字)
group#e_g(in: {scale:0.86, opacity:0, duration:0.6, ease:'power3.out'})
  shape#track.ellipse(left: 84px; top: 231px; width: 273px; height: 273px; background: none; border: 19px solid #1D2A3E)
  # 59% の弧 (12 時から時計回りに 212°・線の中心が地の輪の中心に乗る枠)
  shape#arc(left: 93px; top: 240px; width: 254px; height: 254px; path: arc,start=0,to=212.4; background: none; border: 19px solid $teal2; in: draw {duration: 1.2})
  p#v(cx: 220px; cy: 352px; font-size: 100px; line-height: 0.95; font-family: n) [count:59 start=0 ms=1200]%
  p#l(cx: 220px; cy: 416px; font-size: 16px; color: $fg2; white-space: nowrap) 初回で解決（全体）
p#e_cap(left: 64px; top: 532px; width: 313px; text-align: center; font-size: 15px; color: $muted; in: {y:7, opacity:0, duration:0.5, ease:'power2.out'}) {n21}2,442{/} 件 / {n21}4,128{/} 件
board#e_bd(left: 427px; top: 195px; width: 789px; height: 451px; t: "カテゴリ別の初回解決率"; u: "単位：%"; delay: 300; in: {x:27, opacity:0, duration:0.65, ease:'power3.out'})
  # 行の枠は語で点く 3 行 (81 の青緑・34 / 22 の珊瑚) だけ・他の行の枠は透明
  div#r(left: 12px; top: "93;134;175;216;257;298;339"; width: 765px; height: 41px; in: none) ×7
    div#hl(left: 0px; top: 4px; width: 765px; height: 33px; border-radius: 7px; background: "#2EC4B614;#2EC4B614;#2EC4B614;#2EC4B614;#2EC4B614;#E8615A14;#E8615A14"; border: "#7ADFD3BF,2;#7ADFD3BF,2;#7ADFD3BF,2;#7ADFD3BF,2;#7ADFD3BF,2;#E8615ABF,2;#E8615ABF,2"; opacity: "1;0;0;0;0;1;1"; in: {opacity:0, duration:0.3})
    cat#nm(left: 9px; cy: 50%; width: 220px; t: "ログイン・アカウント;操作方法;権限・設定;請求・プラン;その他;データ連携（CSV・API）;不具合の報告"; c: "$teal;$teal2;$slate;$amber;$slate2;$orange;$coral"; delay: "600;660;720;780;840;900;960"; in: {x:-11, opacity:0, duration:0.4, ease:'power2.out'})
    div#tr(left: 229px; cy: 50%; width: 400px; height: 21px; border-radius: 0px 4px 4px 0px; background: #FFFFFF0A)
    div#bar(left: 229px; cy: 50%; width: "324;296;252;232;220;136;88"; height: 21px; border-radius: 0px 4px 4px 0px; background: "$teal;$teal2;$slate;$amber;$slate2;$orange;$coral"; delay: "700;770;840;910;980;1050;1120"; in: {scaleX:0, duration:0.75, ease:'power3.out', pivot:'left'})
    p#v(left: 642px; cy: 50%; width: 73px; text-align: right; font-size: 27px; font-family: n; color: "$fg;$fg;$fg;$fg;$fg;$coral;$coral"; delay: "1000;1070;1140;1210;1280;1350;1420"; in: {opacity:0, duration:0.4}) 81%;74%;63%;58%;55%;34%;22%
  # 全体 59% の破線 (上から下りる) と札
  shape#avg(left: 477px; top: 85px; width: 2px; height: 300px; path: line_v; border: 2px solid #E9EEF58C; dash: 5,5; in: {scaleY:0, opacity:0, duration:0.5, ease:'power2.out', pivot:'top'})
  p#al(left: 435px; top: 62px; width: 85px; text-align: center; font-size: 13px; background: $panel2; border: 1px solid $line2; border-radius: 4px; padding: 1px 0px; in: {opacity:0, duration:0.5})  全体 59%
  p#note(left: 21px; bottom: 13px; font-size: 12px; color: $muted; font-family: r; white-space: nowrap; in: {opacity:0, duration:0.5}) ※ 破線は全体の初回解決率 59%（2,442 件 / 4,128 件）。{b}データ連携 34%・不具合の報告 22%{/} は全体を大きく下回る。

# f 解決までの時間: 6 本の縦棒が伸びて値が乗り、「4 時間以内に約 6 割」のかぎ・「中央値」で札と破線の引き出し・「3 日を」で長い尾のかぎと右の板・372 で尾の 2 本が明るく脈打ち、78% が数えて帯が伸びる
section#f(stagger: {each:0})
head#f_h(n: "05"; k: "解決までの時間"; t: "中央値は {t}1 時間 50 分{/}。ただし 3 日超の“長い尾”が {c}372 件{/}")
board#f_bd(left: 64px; top: 195px; width: 767px; height: 451px; t: "受付から解決までの時間"; u: "単位：件（構成比）"; delay: 120)
  div#base(left: 47px; top: 365px; width: 673px; height: 2px; background: #3A4B66)
  div#bar(left: "61;173;285;397;509;622"; top: "174;245;281;306;336;352"; width: 85px; height: "193;122;86;61;31;15"; border-radius: 5px 5px 0px 0px; background: "linear(#7ADFD3,#2A9D92,180);linear(#7ADFD3,#2A9D92,180);linear(#5D7899,#455C7A,180);linear(#5D7899,#455C7A,180);linear(#F07A6F,#C84B45,180);linear(#F07A6F,#C84B45,180)"; delay: 550; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom', stagger:{each:0.1}}) ×6
  # 尾の 2 本を明るくする薄い白の板 (372 の語で 1 往復だけ点く = hf の brightness(1.35) の yoyo)
  div#hi(left: "509;622"; top: "336;352"; width: 85px; height: "31;15"; border-radius: 5px 5px 0px 0px; background: #FFFFFF; opacity: 0; in: none) ×2
  div#hv(left: "47;159;272;384;496;608"; top: "127;198;234;259;289;305"; width: 112px; height: 46px; delay: 900; in: {y:7, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.1}}) ×6
    p#n(cx: 50%; top: 0px; font-size: 27px; line-height: 1; font-family: n; color: "$fg;$fg;$fg;$fg;$coral;$coral") 1,568;991;702;495;248;124
    p#p(cx: 50%; top: 29px; font-size: 13px; color: $muted) 38%;24%;17%;12%;6%;3%
  p#hx(left: "47;159;272;384;496;608"; top: 376px; width: 112px; text-align: center; font-size: 15px; color: $fg2; white-space: nowrap; delay: 700; in: {opacity:0, duration:0.4, stagger:{each:0.06}}) ×6 1 時間以内;1〜4 時間;4〜24 時間;1〜3 日;3〜7 日;7 日超
  # かぎ (4 時間以内 / 3 日超) と札
  shape#brf(path: "M60.5 121.3 V112 H258 V121.3"; background: none; border: 2px solid $teal2; delay: 1700; in: {opacity:0, duration:0.4})
  p#labf(left: 61px; top: 87px; width: 197px; text-align: center; font-size: 14px; color: $teal2; white-space: nowrap; delay: 1750; in: {y:5, opacity:0, duration:0.4, ease:'power2.out'}) 4 時間以内に約 6 割
  shape#brt(path: "M509.3 284.1 V274.7 H706.9 V284.1"; background: none; border: 2px solid $coral; in: {opacity:0, duration:0.4})
  p#labt(left: 469px; top: 249px; width: 278px; text-align: center; font-size: 14px; color: $coral; white-space: nowrap; in: {y:5, opacity:0, duration:0.4, ease:'power2.out'}) 3 日超：372 件（9%）
  # 中央値の札と、1〜4 時間の棒へ下りる破線の引き出し
  shape#lead(path: "M420.3 155.1 L235.3 191.1"; background: none; border: 1.5px solid $teal2; dash: 3,4; in: {opacity:0, duration:0.4})
  shape#ldot.ellipse(left: 231px; top: 187px; width: 8px; height: 8px; background: $teal2; in: {opacity:0, duration:0.4})
  p#pin(left: 420px; top: 138px; font-size: 14px; background: $panel2; border: 1px solid $teal2; border-radius: 5px; padding: 4px 8px; white-space: nowrap; in: {y:-8, opacity:0, duration:0.45, ease:'back.out(1.8)'}) 中央値　1 時間 50 分
  p#note(left: 21px; bottom: 13px; font-size: 12px; color: $muted; font-family: r; in: {opacity:0, duration:0.5}) ※ 受付から解決までの経過時間で 6 区分。中央値は 1 時間 50 分。
board#f_sd(left: 853px; top: 195px; width: 363px; height: 451px; t: "長い尾（3 日超）の内訳"; u: "受付から 3 日超"; pc: $coral; in: {x:27, opacity:0, duration:0.65, ease:'power3.out'})
  div#st1(left: 21px; top: 67px; width: 321px; height: 100px; in: {y:12, opacity:0, duration:0.5, ease:'power3.out'})
    p#l(left: 0px; top: 0px; font-size: 14px; color: $fg2) 3 日を超えた案件
    p#n(left: 0px; top: 23px; font-size: 69px; line-height: 1.02; font-family: n; color: $coral) 372
    p#u(left: .n.right+8; top: 57px; font-size: 20px) 件
    p#s(left: .u.right+4; top: 60px; font-size: 15px; color: $fg2; font-family: r) 全体の 9%
  div#st2(left: 21px; top: 200px; width: 321px; height: 110px; in: {y:12, opacity:0, duration:0.5, ease:'power3.out'})
    div#rule(left: 0px; top: 0px; width: 321px; height: 1px; background: $line)
    p#l(left: 0px; top: 15px; font-size: 14px; color: $fg2; white-space: nowrap) そのうち、データ連携・不具合の報告が
    p#n(left: 0px; top: 38px; font-size: 69px; line-height: 1.02; font-family: n; color: $orange) [count:78 start=0 ms=800 delay=100]%
    p#u(left: .n.right+8; top: 72px; font-size: 20px) 291 件
  div#split(left: 21px; top: 317px; width: 320px; height: 33px; border-radius: 5px; background: #2A3850; in: {opacity:0, duration:0.4})
    div#a(left: 0px; top: 0px; width: 250px; height: 33px; border-radius: 5px 0px 0px 5px; background: linear($orange,$coral,90); in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
      # hf の作り: 橙の帯の上の暗い字 (check は全編の grain の幕と比べて low_contrast を出す)
      p#t(left: 11px; cy: 50%; font-size: 20px; font-family: n; color: #0A0F17) 291 件
  div#lsw(left: "21;32;21"; top: "367;367;391"; width: 9px; height: 9px; border-radius: 2px; background: "$orange;$coral;#2A3850"; in: {opacity:0, duration:0.4}) ×3
  p#lt(left: "48;37"; top: "361;385"; font-size: 13px; color: $fg2; font-family: r; white-space: nowrap; in: {opacity:0, duration:0.4}) ×2 データ連携・不具合の報告;そのほかのカテゴリ
  p#note(left: 21px; bottom: 13px; font-size: 12px; color: $muted; font-family: r; white-space: nowrap) ※ 3 日を超えた 372 件（全体の 9%）が対象。

# g 対応時間: 左の板に件数の積み上げ棒が頭に積み上がり、「対応時間」で右の棒が積み上がる・「データ連携」で 2 本をつなぐ帯と上位 3 以外を沈め、右の板の 3 行 + 参考の行・43% と 75% の大きな札
section#g(stagger: {each:0})
head#g_h(n: "06"; k: "担当者の対応時間"; t: "件数の {a}43%{/} が、対応時間の {a}75%{/} を占める")
board#g_cmp(left: 64px; top: 195px; width: 547px; height: 451px; t: "件数と対応時間の構成比"; u: "3 か月"; pc: $amber; delay: 120)
  # 2 本をつなぐ帯 (上位 3 の境を結ぶ琥珀の面 + 破線・その上の灰の面)
  shape#rib(points: "213,380;213,245;333,144;333,380"; background: #F6C35B29; border: none; in: {opacity:0, duration:0.6, ease:'power1.out'})
  shape#rib2(points: "213,245;213,67;333,67;333,144"; background: #8A97AD12; border: none; in: {opacity:0, duration:0.6, ease:'power1.out'})
  shape#ribl(path: "M213.3 245.3 L333.3 143.8"; background: none; border: 2px solid $amber; dash: 4,4; in: {opacity:0, duration:0.6, ease:'power1.out'})
  # 件数の積み上げ (下から データ連携・不具合・請求・ログイン・操作方法・権限・その他)
  div#sc(left: 113px; top: "335;300;247;178;112;84;67"; width: 100px; height: "45;33;51;67;64;26;15"; background: "$orange;$coral;$amber;$teal;$teal2;$slate;$slate2"; delay: 550; in: {scaleY:0, duration:0.4, ease:'power2.out', pivot:'bottom', stagger:{each:0.06}}) ×7
  # 対応時間の積み上げ (下から データ連携・不具合・請求・ログイン・残り)
  div#st(left: 333px; top: "284;196;146;122;67"; width: 100px; height: "96;86;48;22;53"; background: "$orange;$coral;$amber;$teal;#3B4A62"; in: {scaleY:0, duration:0.45, ease:'power2.out', pivot:'bottom', stagger:{each:0.08}}) ×5
  div#slab(left: "87;307"; top: 383px; width: 153px; height: 40px) ×2
    p#t(cx: 50%; top: 0px; font-size: 15px) 件数;対応時間
    p#s(cx: 50%; top: 22px; font-size: 12px; color: $muted; font-family: r; white-space: nowrap) 4,128 件;4,175 時間
  p#g43(left: 20px; top: 279px; font-size: 51px; line-height: 1; font-family: n; color: $amber; in: {x:-13, opacity:0, duration:0.5, ease:'power3.out'}) 43%
    p#s(left: 0px; top: 55px; font-size: 12px; color: $fg2; font-family: g; white-space: nowrap) 1,775 件
  p#g75(left: 441px; top: 225px; font-size: 57px; line-height: 1; font-family: n; color: $amber; transform-origin: 0% 50%; in: {scale:0.7, opacity:0, duration:0.6, ease:'back.out(1.6)'}) 75%
    p#s(left: 0px; top: 61px; font-size: 12px; color: $fg2; font-family: g; white-space: nowrap) 3,147 時間
board#g_top(left: 633px; top: 195px; width: 583px; height: 451px; t: "時間を食っている上位 3 カテゴリ"; u: "対応時間の合計（3 か月）"; pc: $amber; in: {x:27, opacity:0, duration:0.65, ease:'power3.out'})
  div#r(left: 21px; top: "72;136;200;287"; width: 540px; height: 64px; opacity: "1;1;1;0.92"; in: {y:9, opacity:0, duration:0.45, ease:'power2.out'}) ×4
    div#sw(left: 0px; top: 6px; width: 11px; height: 11px; border-radius: 3px; background: "$orange;$coral;$amber;$teal")
    p#nm(left: 19px; top: 1px; font-size: 15px; white-space: nowrap) データ連携（CSV・API）;不具合の報告;請求・プラン;ログイン・アカウント{mu}（908 件）{/}
    div#bar(left: 0px; top: 28px; width: "313;284;161;77"; height: 20px; border-radius: 0px 4px 4px 0px; background: "$orange;$coral;$amber;$teal"; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#n(left: 327px; top: 20px; width: 87px; text-align: right; font-size: 31px; font-family: n) 1,300;1,180;667;318
    p#u(left: 418px; top: 34px; font-size: 13px; color: $fg2) 時間
    p#avg(right: 0px; top: 20px; text-align: right; font-size: 12px; line-height: 1.2; color: $muted; font-family: r) 1 件平均[br]{an}2.1{/} 時間;1 件平均[br]{an}2.6{/} 時間;1 件平均[br]{an}0.95{/} 時間;1 件平均[br]{an}0.35{/} 時間
  div#dv(left: 21px; top: 263px; width: 540px; height: 23px; in: {opacity:0, duration:0.45})
    p#t(left: 0px; cy: 50%; font-size: 12px; color: $muted; white-space: nowrap) 参考：件数が最も多いカテゴリ
    div#ln(left: 188px; cy: 50%; width: 352px; height: 1px; background: $line2)
  div#sum(left: 21px; top: 405px; width: 541px; height: 33px; in: {y:7, opacity:0, duration:0.5})
    div#rule(left: 0px; top: 0px; width: 541px; height: 1px; background: $line)
    p#a(left: 0px; top: 10px; font-size: 13px; color: $fg2; white-space: nowrap) 3 カテゴリ合計：件数 {ab}1,775 件（43%）{/}
    p#b(left: .a.right+17; top: 10px; font-size: 13px; color: $fg2; white-space: nowrap) 対応時間 {ab}3,147 時間（75%）{/}

# h ヘルプページ: 左にノートパソコンのヘルプページの写真 (寄り続ける) と条件・右の板に 2 本の斜線の帯が語で伸び、「655」で合計の枠が数え、「247」で時間が数える
section#h(stagger: {each:0})
head#h_h(n: "07"; k: "ヘルプページで減らせる問い合わせ"; t: "{t}655 件（全体の 16%）{/}は、ヘルプページで答えられる内容だった")
div#h_fr(left: 64px; top: 200px; width: 507px; height: 313px; border-radius: 11px; border: 1px solid $line2; box-shadow: 0px 20px 47px #00000080; delay: 150; in: {y:20, opacity:0, duration:0.7, ease:'power3.out'})
  img#p(inset: 0; subject: center 70%; main: kb {scale: [1, 1.08], focus: ['55% 45%', '55% 45%']}) [photo]夜の暗い木の机に置かれたノートパソコンを斜め前から。画面にはすっきりしたヘルプセンターのページが映り、上に検索欄、その下に整った FAQ の項目の列が光の線と角丸の塊で抽象的に並ぶ (読める文字はない)。項目の横に小さく光る鍵のアイコンがパスワード再設定をほのめかす。紺と青緑のほのかな光、柔らかな映画的な縁の光、落ち着いて整った雰囲気、周りは暗い。斜め前から寄った構図で、ノートパソコンの画面と本体が枠の横幅の 8 割を占めるほど大きく写り、机の奥の暗がりにぼけた観葉植物と街の灯り。余白を作らない。文字・数字・ロゴなし
  div#fx(inset: 0; background: linear(#0A0F1700@55%,#0A0F178C,180); z-index: front)
div#h_cap(left: 64px; top: 531px; width: 507px; height: 50px; delay: 600; in: {y:7, opacity:0, duration:0.5, ease:'power2.out'})
  p#q(left: 0px; top: 2px; font-size: 12px; font-family: m; color: $teal2; border: 1px solid #7ADFD380; border-radius: 3px; padding: 0px 5px) 条件
  p#t(left: 45px; top: 0px; width: 462px; font-size: 14px; line-height: 1.55; color: $fg2; font-family: r) 既存のヘルプページに答えがある、または 1 ページ足せば答えられる問い合わせを数えた
board#h_bd(left: 600px; top: 195px; width: 616px; height: 451px; t: "ヘルプページで減らせる見込み"; u: "単位：件"; delay: 300; in: {x:27, opacity:0, duration:0.65, ease:'power3.out'})
  div#rh(left: 21px; top: "75;170"; width: 573px; height: 90px; in: {y:8, opacity:0, duration:0.45, ease:'power2.out'}) ×2
    div#sw(left: 0px; top: 6px; width: 11px; height: 11px; border-radius: 3px; background: "$teal2;$teal")
    p#t(left: 19px; top: 0px; font-size: 16px; white-space: nowrap) 操作方法;ログイン・アカウント
    div#tr(left: 0px; top: 31px; width: 533px; height: 27px; border-radius: 4px; background: #8A97AD2E; border: 1px solid #8A97AD59)
    # 斜線の帯 (減らせる分・左から伸びる)
    div#rd(left: 0px; top: 31px; width: "218;176"; height: 27px; border-radius: 4px 0px 0px 4px; background: #7ADFD3F2; pattern: hatch,45,#2EC4B6F2,13,7; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#l(left: 0px; top: 63px; font-size: 13px; color: $fg2; white-space: nowrap) うち {n19}355{/} 件（41%）;うち {n19}300{/} 件（33%）
    p#r(right: 40px; top: 64px; font-size: 13px; color: $muted; white-space: nowrap) 全 {n16}867{/} 件;全 {n16}908{/} 件
  p#tag(left: 205px; top: 172px; font-size: 12px; color: $bg; background: $teal2; border-radius: 3px; padding: 1px 6px; white-space: nowrap; in: {y:8, opacity:0, duration:0.45, ease:'power2.out'}) ほぼパスワード再設定
  # 合わせての枠 (655 件 | 約 247 時間)
  div#tot(left: 21px; top: 279px; width: 573px; height: 127px; border-radius: 9px; background: #2EC4B614; border: 1px solid #7ADFD366; in: {y:13, opacity:0, duration:0.5, ease:'power3.out'})
    p#l(left: 20px; top: 16px; font-size: 13px; color: $fg2) 合わせて
    p#n(left: 20px; top: 50px; font-size: 69px; line-height: 0.86; font-family: n; color: $teal2) [count:655 start=0 ms=800 delay=100]
    p#u(left: .n.right+5; top: 86px; font-size: 19px) 件
    p#s(left: .u.right+5; top: 89px; font-size: 15px; color: $fg2; font-family: r; white-space: nowrap) 全体の 16%
    div#sep(left: 253px; top: 23px; width: 1px; height: 80px; background: #7ADFD359)
    div#hrs(left: 276px; top: 0px; width: 280px; height: 127px; in: {opacity:0, duration:0.4})
      p#l(left: 0px; top: 16px; font-size: 13px; color: $fg2) 対応時間にして
      p#a(left: 0px; top: 82px; font-size: 17px) 約
      p#n(left: 22px; top: 58px; font-size: 51px; line-height: 0.86; font-family: n) [count:247 start=0 ms=700 delay=50]
      p#u(left: .n.right+5; top: 84px; font-size: 19px) 時間
  p#note(left: 21px; bottom: 13px; font-size: 12px; color: $fg2; font-family: r; white-space: nowrap; in: {x:-8, opacity:0, duration:0.5, ease:'power2.out'}) {a}→{/} 浮いた時間を、時間を食っている上位 3 カテゴリに回す

# i 目標: 3 枚の札が語ごとに下から入り、実績 (灰) と目標 (色) の 2 本の棒が続けて伸びる
section#i(stagger: {each:0})
head#i_h(n: "08"; k: "次の四半期（10〜12 月）の目標"; t: "件数・初回解決率・長い尾、{t}3 つの目標{/}")
goal#i_c1(left: 64px; ix: "01"; t: "問い合わせ件数"; g: "3,600"; u: "件以下"; f: "7〜9 月の実績 {n21}4,128{/} 件 {t}→ 目標{/}"; c: $teal2; gw: 201px; tw: 175px; gv: "4,128"; tv: "3,600"; d: "ヘルプページの整備で 655 件減を見込み、利用企業の増加分を差し引いた値")
goal#i_c2(left: 459px; ix: "02"; t: "初回解決率"; g: "65%"; u: ""; f: "7〜9 月の実績 {n21}59%{/} {a}→ 目標{/}"; c: $amber; gw: 119px; tw: 131px; gv: "59%"; tv: "65%"; d: "7〜9 月は 2,442 件 / 4,128 件が初回で解決")
goal#i_c3(left: 853px; ix: "03"; t: "3 日を超える案件"; g: "250"; u: "件以下"; f: "7〜9 月の実績 {n21}372{/} 件 {c}→ 目標{/}"; c: $coral; gw: 201px; tw: 135px; gv: "372"; tv: "250"; d: "データ連携と不具合に、開発チームへの引き継ぎ手順を決める")

# j まとめ: 引き継ぎの光の橋の絵 (1.08 → 1 に引く) を暗い幕の下に・3 行が語ごとに左から入り、3 行目の縁が珊瑚に光る → 行と見出しが上へ抜けて幕が明け、「NEXT ACTION」の題が出て暗転
section#j(stagger: {each:0})
# hf の作り: 引き継ぎの絵は濃い幕の下の地で、まとめの 3 行と締めの題は絵の主体の上に乗る (text_over_subject)
img#j_img(inset: 0; subject: center 60%; room: top 30%; main: kb {scale: [1.08, 1], focus: ['50% 60%', '50% 60%']}) [photo]深い紺の背景の上の、ミニマルな概念的 3D レンダー。暗い空間を挟んで向かい合う 2 つの光る作業机が光の橋でつながり、小さな長方形の札が橋の上を、青緑に光る左の机から温かい琥珀色に光る右の机へ渡っていく (サポートと開発のはっきりした引き継ぎ)。柔らかな立体の光、上品で落ち着いた雰囲気、2 つの机と橋は画面の中ほどから下に横いっぱいに置き、上の 3 割は暗い余白。人物なし、文字・数字・ロゴなし
div#j_shade(inset: 0; background: linear(#0A0F17F0,#0A0F17DB@45%,#0A0F17C7,180))
head#j_h(n: "09"; k: "まとめ"; t: "わかったことと、{a}次の一手{/}"; out: {opacity:0, duration:0.45, ease:'power2.in'})
item#j_i1(top: 200px; ix: "1"; c: $amber; f: "43%{arr} → {/}75%"; b: "時間を食うのは、データ連携・不具合・請求の 3 つ"; s: "件数の 43% で、対応時間の 75%（件数が多いのはログインと操作方法）")
item#j_i2(top: 343px; ix: "2"; c: $teal2; f: "655{u21}件{/}"; b: "ログインと操作方法の 655 件は、ヘルプページで減らせる"; s: "浮いた時間を上位 3 カテゴリに回す")
item#j_i3(top: 486px; ix: "3"; c: $coral; f: "8{u21}割{/}"; b: "3 日超の長い尾の 8 割は、データ連携と不具合"; s: "{cb}次の一手：{/}開発への引き継ぎ手順を決める"; border: 1px solid #E8615A8C)
  p#s(color: $fg)
# 締めの題 (行が抜けた後に出る)
div#j_ek(left: 64px; top: 100px; width: 300px; height: 22px; in: {x:-16, opacity:0, duration:0.5, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 29px; height: 2px; background: $teal2)
  p#t(left: 37px; cy: 50%; font-size: 15px; font-family: m; color: $teal2; letter-spacing: 0.14em; white-space: nowrap) NEXT ACTION
p#j_et(left: 64px; top: 129px; font-size: 43px; line-height: 1.25; letter-spacing: -0.01em; white-space: nowrap; in: {y:17, opacity:0, duration:0.7, ease:'expo.out'}) 次の一手は、{a}開発への引き継ぎ手順{/}を決めること
p#j_es(left: 64px; top: 199px; font-size: 17px; color: $fg2; font-family: r; white-space: nowrap; in: {y:9, opacity:0, duration:0.5, ease:'power2.out'}) 3 日を超える長い尾の 8 割は、データ連携と不具合の報告
```

```timeline.txt
#v2
cast n = "落ち着いた30代男性のナレーター、低めで明瞭な声、社内の分析報告らしく淡々と丁寧に読む"
silence head=0 tail=0
# 切替: 細い光の縦線 (芯 2 px・両脇は淡い光) が左から右へ払い、新しい場面を見せる (窓 600 ms は境目の後ろ・声は窓の頭の 300 ms 後)。風切りは窓の頭の 80 ms 前・乾いたシュッは各場面の最初の語の 250 ms 後
# 線は上から下へ青緑 → 琥珀の縦のグラデ (帯の linear(…,180))
# engine: hf の線の青緑の光の滲み (box-shadow 22 px) は帯に添えられない — グラデの帯は 1 本だけ (縦グラデの芯の両側に半透明の帯を並べると DEFECT:RUNTIME)・滲みを幅方向のグラデで書くと縦の青緑 → 琥珀が消える
transition = wipe,600,dir=right,overlap=600,ease=power2.inOut,bars=linear(#7ADFD300,#7ADFD3F2@30%,#F6C35BF2@70%,#F6C35B00,180),3,se=whoosh -3.5dB -380

*** a
bgm music
@n: [silence:0.9s][♪telop -1.5dB -650]ワークノートのサポート窓口に、[>#a_st[1] -100][♪pop -8dB]7月から9月に届いた問い合わせ[>#a_st[2] -150][♪blip -10dB][♪chime -4.5dB +950]4,128件。全件を読み、[>#a_st[3] -100][♪pop -7dB]7つのカテゴリに[>#a_cat[*] -150][♪swish -3dB]分類しました。[silence:0.20s]

*** b
@n: [silence:0.3s][!#hdr.d[1] to,{scale:1.3, fill:'#2EC4B6', duration:0.05} -50][♪swish -4.5dB +250]あわせて、[>#b_bd.m[1] -100][♪pop -7dB]初回で解決したか、[>#b_bd.m[2] -100][♪pop -7dB]解決までの時間、[>#b_bd.m[3] -100][♪pop -7dB][>#b_bd.note +500]対応時間を突き合わせました。[silence:0.20s]

*** c
@n: [silence:0.3s][step #hdr.d[2] #hdr.d[1] -50][!#hdr.lbl text,"02 / 09" -50][♪swish -4dB +250]件数は3か月で[>#c_pct -200][♪chime -4.5dB][>#c_ft +350]12%増。[>#c_call -100][♪pop -8dB][>#c_bd.note +600]利用企業の増加と、ほぼ同じ伸びです。[silence:0.20s]

*** d
@n: [silence:0.3s][step #hdr.d[3] #hdr.d[2] -50][!#hdr.lbl text,"03 / 09" -50][♪swish -4dB +250]内訳で多いのは、[>#d_bd.r[1].hl -50][!#d_bd.r[3] to,{opacity:0.5, duration:0.5}][!#d_bd.r[4] to,{opacity:0.5, duration:0.5}][!#d_bd.r[5] to,{opacity:0.5, duration:0.5}][!#d_bd.r[6] to,{opacity:0.5, duration:0.5}][!#d_bd.r[7] to,{opacity:0.5, duration:0.5}][♪click -4dB]ログイン・アカウントの22%と、[>#d_bd.r[2].hl -50][♪click -4dB][>#d_bd.leg +500]操作方法の21%です。[silence:0.45s]

*** e
@n: [silence:0.3s][step #hdr.d[4] #hdr.d[3] -50][!#hdr.lbl text,"04 / 09" -50][♪swish -4.5dB +250]初回で解決した割合は全体で[>#e_g -750][>#e_bd.avg][>#e_bd.al][♪chime -4.5dB][>#e_cap +500]59%。ログインの[>#e_bd.r[1].hl -50][♪click -4.5dB]81%に対し、データ連携は[>#e_bd.r[6].hl -50][!#e_bd.r[2] to,{opacity:0.5, duration:0.5} -50][!#e_bd.r[3] to,{opacity:0.5, duration:0.5} -50][!#e_bd.r[4] to,{opacity:0.5, duration:0.5} -50][!#e_bd.r[5] to,{opacity:0.5, duration:0.5} -50][♪click -4.5dB]34%、不具合の報告は[>#e_bd.r[7].hl -50][♪click -4.5dB][>#e_bd.note +600]22%です。[silence:0.20s]

*** f
@n: [silence:0.3s][step #hdr.d[5] #hdr.d[4] -50][!#hdr.lbl text,"05 / 09" -50][♪swish -4.5dB +250]解決までの時間の[>#f_bd.pin -50][♪pop -7dB][>#f_bd.lead +150][>#f_bd.ldot +150]中央値は、1時間50分。ただ、[>#f_sd -350][>#f_bd.brt -100][>#f_bd.labt][♪chime_low -1.5dB]3日を超える長い尾が[>#f_sd.st1 -250][>#f_sd.split][!#f_bd.hi[*] to,{opacity:0.3, duration:0.4, repeat:1, yoyo:true}]372件あり、その[>#f_sd.st2 -350][>#f_sd.split.a -200][♪chime -5dB][>#f_sd.lsw[*] +400][>#f_sd.lt[*] +400]78%がデータ連携と不具合の報告です。[silence:0.25s]

*** g
@n: [silence:0.3s][step #hdr.d[6] #hdr.d[5] -50][!#hdr.lbl text,"06 / 09" -50][♪swish -4.5dB +250]ところが[>#g_cmp.st[*]]対応時間で見ると、景色が変わります。[>#g_top -300][>#g_cmp.rib -100][>#g_cmp.rib2 -100][>#g_cmp.ribl -100][!#g_cmp.sc[4] to,{opacity:0.35, duration:0.5}][!#g_cmp.sc[5] to,{opacity:0.35, duration:0.5}][!#g_cmp.sc[6] to,{opacity:0.35, duration:0.5}][!#g_cmp.sc[7] to,{opacity:0.35, duration:0.5}][!#g_cmp.st[4] to,{opacity:0.35, duration:0.5}][!#g_cmp.st[5] to,{opacity:0.35, duration:0.5}][>#g_top.r[1] +100][>#g_top.r[1].bar +200][>#g_top.r[2] +320][>#g_top.r[2].bar +420][>#g_top.r[3] +540][>#g_top.r[3].bar +640][>#g_top.dv +1000][>#g_top.r[4] +1150][>#g_top.r[4].bar +1150]データ連携、不具合、請求の3つは、件数では[>#g_cmp.g43 -150][♪chime -4.5dB]43%なのに、対応時間では[>#g_cmp.g75 -150][♪chime_low][>#g_top.sum +500]75%を占めています。[silence:0.35s]

*** h
@n: [silence:0.3s][step #hdr.d[7] #hdr.d[6] -50][!#hdr.lbl text,"07 / 09" -50][♪swish -4.5dB +250]一方、[>#h_bd.rh[1] -200][>#h_bd.rh[1].rd +50][♪pop -8dB]操作方法の355件と、[>#h_bd.rh[2] -200][>#h_bd.tag -200][>#h_bd.rh[2].rd +50][♪pop -8dB]ログインの300件は、ヘルプページで答えられる内容でした。合わせて[>#h_bd.tot -250][♪chime -4.5dB]655件、約[>#h_bd.tot.hrs -250][♪pop -8dB][>#h_bd.note +700]247時間分です。[silence:0.20s]

*** i
@n: [silence:0.3s][step #hdr.d[8] #hdr.d[7] -50][!#hdr.lbl text,"08 / 09" -50][♪swish -4.5dB +250]次の四半期は、件数[>#i_c1 -450][>#i_c1.b1 -100][>#i_c1.b2 +80][♪pop -6.5dB]3,600件以下、初回解決率[>#i_c2 -450][>#i_c2.b1 -100][>#i_c2.b2 +80][♪pop -6.5dB]65%、3日を超える案件[>#i_c3 -450][>#i_c3.b1 -100][>#i_c3.b2 +80][♪pop -6.5dB]250件以下を目指します。[silence:0.25s]

*** j
@n: [silence:0.3s][step #hdr.d[9] #hdr.d[8] -50][!#hdr.lbl text,"09 / 09" -50]件数の[>#j_i1 -250][♪chime_warm -4.5dB to=1.1s]43%が、時間の75%。[>#j_i2 -250][♪chime_warm -4.5dB to=1.1s]ヘルプページで浮いた時間を上位3カテゴリに回し、[>#j_i3 -250][♪chime_warm -4.5dB to=1.1s]長い尾には、開発への引き継ぎ手順を決める。それが[!#j_i3 glow,#E8615A73,blur=31 -100][♪shimmer -1.5dB to=1.8s][<#j_i1 +150][<#j_i2 +150][<#j_i3 +150][<#j_h +150][!#j_shade to,{opacity:0.42, duration:1, ease:'power2.inOut'} +350][>#j_ek +600][>#j_et +700][>#j_es +950]次の一手です。[silence:2.6s]
fade out,900
```

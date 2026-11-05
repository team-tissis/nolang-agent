# data · support-tickets (hf 全力版の全量の写し — 問い合わせ 4,000 件を分類してわかったこと・暗い地に番号つきの見出しと題つきの板を場面ごとに組む 10 場面のデータ図解) — canvas 1920x1080

見せる作り: 全編の地 (紺の放射の地 + 斜めに流れる方眼 + 2 つの光 + grain)・2 場面目から常設の上端の帯 (題・9 つの点と「0N / 09」・全編で伸びる進行線) と下端の出典の帯・光の縦線が左から払う場面の切替・場面 = 番号の札 + mask から上がる見出し + 題つきの板 1〜2 枚 (板の def)・数字の語で伸びる図 (数える 3 枚の札・4 列の流れ図・縦棒と破線の伸び・構成比の帯と 7 行の横棒・弧を描く輪と全体の破線・6 本の分布とかぎと中央値の札・2 本の積み上げとつなぐ帯・斜線の帯と合計の枠・実績 / 目標の 2 本の棒)・語で点く行の枠と沈む他の行・まとめの 3 行から締めの題へ幕が明けて暗転・字幕なし・音の層 (切替の風切り + 語に結んだ効果音)

```design.txt
#v2
# 学ぶ作り: 暗い data の design system を根に 1 回 (palette・書体 4・数字の run・場面の見出し head・題つきの板 board の def) → 場面は板の中身だけ
# 常設の層: 全編の地 (紺の放射の地 + 流れる方眼 + 2 つの光 + grain) を根に・2 場面目から sticky の上端の帯 (題・9 つの点と「0N / 09」・全編で伸びる進行線) と下端の出典の帯
# 場面 = 番号つきの見出し + 板 1〜2 枚。板の骨組み (目盛り・行の札) は場面の頭に組み上げ、台詞の数字の語で枠が点き・棒が伸び・数字が数える。場面の切替は光の縦線が左から右へ払う wipe
# hf d10 support-tickets (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。字幕は無い (hf の作り)
canvas 1920x1080 bg=#0A0F17
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
run t { color: $teal2 }
run a { color: $amber }
run c { color: $coral }
run b { color: $fg }
run mu { color: $muted; font-family: r; font-size: 18px }
run sp { color: #7E8796 }
run sc { color: $muted; font-family: r }
run big { color: $amber; font-family: n; font-size: 118px }
run nf { color: $fg; font-family: n; font-size: 52px }
run ar { color: $teal2; font-size: 34px }
run n21 { color: $fg; font-family: n; font-size: 32px }
run n19 { color: $teal2; font-family: n; font-size: 28px }
run n16 { color: $fg2; font-family: n; font-size: 24px }
run an { color: $fg; font-family: n; font-size: 32px }
run ab { color: $amber }
run arr { color: $fg2; font-size: 64px }
run u21 { color: $fg; font-family: g; font-size: 32px }
run cb { color: $coral }
sound telop = "電子的なテロップの出現音、短いデジタルのきらめき"
sound pop = "柔らかく短いポップ音"
sound blip = "柔らかい短い電子のブリップ音"
sound chime = "短く澄んだチャイム"
sound swish = "乾いた短いシュッという音"
sound click = "乾いた短いクリック音"
sound chime_low = "低めに響く落ち着いたチャイム"
sound chime_warm = "温かみのある柔らかなチャイム"
sound shimmer = "低めのきらめくシマー音、余韻が残る"
# 上端の帯の題の印 (紺の角丸の枠 + 青緑の 3 本線)・方法の板の矢印 (線 + 青緑の山形)
svg mark = """<svg viewBox="0 0 30 30"><rect x="1" y="1" width="28" height="28" rx="7" fill="#152030" stroke="#7adfd3" stroke-width="1.5"/><path d="M8 11h14M8 15.5h10M8 20h7" stroke="#7adfd3" stroke-width="2" stroke-linecap="round"/></svg>"""
svg arrow = """<svg viewBox="0 0 64 24"><path d="M2 12h54" stroke="#3d5373" stroke-width="3" stroke-linecap="round"/><path d="M48 4l10 8-10 8" fill="none" stroke="#7adfd3" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
# 上端の帯の点: 今の場面を青緑で 1.3 倍に、前の場面を暗い青緑に戻す
cue step(x, p) = [!#x to,{scale: 1.3, duration: .05}][!#x recolor,#2EC4B6 {duration: .05}][!#p to,{scale: 1, duration: .05}][!#p recolor,#3F6B78 {duration: .05}]
p { color: $fg; line-height: 1.2; out: none }
div { border: none; out: none }
img { out: none }
shape { out: none }
svg { out: none }
icon { out: none }
group { out: none }
# 曲: 頭の 1 秒と締めの題の 2 秒だけ前に出し、台詞の間は下げる (締めの場面は少し上げる)
bgm#music(keys: "0:+7.5|800ms:+7.5|1400ms:0|end-16.1s:0|end-15.1s:+3|end-2.6s:+3|end-2s:+9|end-1.3s:+8"; fade: 600,1300) シンセのアルペジオが静かに刻む知的なサイエンス系の電子音楽、柔らかいパッドと控えめなビート、主旋律なし、データ分析の解説向け

# 場面の見出し: 番号の札 + 小見出し (左から) → 見出し (下の mask から上がる・語の強調は run t / a / c)
def head(n, k, t) = div(left: 96px; top: 124px; width: 1728px; height: 120px)
  div#k(left: 0px; top: 0px; width: 1050px; height: 33px; delay: 120ms; in: {x:-26, opacity:0, duration:0.5, ease:'power3.out'})
    p#no(left: 0px; cy: 50%; font-size: 20px; font-family: m; color: $bg; background: $teal2; border-radius: 4px; padding: 2px 9px; content: {n})
    p#t(left: .no.right+14; cy: 50%; font-size: 22px; color: $teal2; letter-spacing: 0.06em; white-space: nowrap; content: {k})
  p#h(left: 0px; top: 46px; font-size: 52px; line-height: 1.22; letter-spacing: -0.01em; white-space: nowrap; delay: 200ms; in: {y:74, duration:0.75, ease:'expo.out', clip:true}; content: {t})
# 題つきの板: 半透明の紺 + 細い縁 + 深い影・頭の行 (色の縦棒 + 題 + 右の単位) と下の罫
def board(t, u, pc=$teal) = div(border-radius: 18px; background: #111925E6; border: 2px solid $line; box-shadow: 0px 24px 60px #00000059; in: {y:36, opacity:0, duration:0.65, ease:'power3.out'})
  div#pip(left: 32px; top: 28px; width: 10px; height: 26px; border-radius: 3px; background: {pc})
  p#t(left: 56px; cy: 40px; font-size: 26px; white-space: nowrap; content: {t})
  p#u(right: 32px; cy: 40px; font-size: 18px; color: $muted; font-family: r; white-space: nowrap; content: {u})
  div#rule(left: 32px; right: 32px; top: 74px; height: 2px; background: $line)
# 札の行の色の四角 + 名 (カテゴリの名札)
def cat(t, c) = div(width: 380px; height: 36px)
  div#sw(left: 0px; cy: 50%; width: 18px; height: 18px; border-radius: 4px; background: {c})
  p#t(left: 32px; cy: 50%; font-size: 24px; white-space: nowrap; content: {t})
# 目標の札 (上端の色の帯 + 番号 + 題 + 大きな目標値 + 実績 + 実績 / 目標の 2 本の棒 + 説明)
def goal(ix, t, g, u, f, c, gw, tw, gv, tv, d) = div(top: 300px; width: 544px; height: 660px; border-radius: 18px; background: #111925E6; border: 2px solid $line; box-shadow: 0px 24px 60px #00000059; in: {y:50, opacity:0, duration:0.6, ease:'power3.out'})
  div#top(left: 0px; top: 0px; width: 544px; height: 8px; border-radius: 18px 18px 0px 0px; background: {c})
  p#ix(left: 34px; top: 38px; font-size: 18px; font-family: m; color: $muted; border: 2px solid $line2; border-radius: 4px; padding: 0px 8px; content: {ix})
  p#t(left: 84px; top: 34px; font-size: 26px; white-space: nowrap; content: {t})
  p#g(left: 34px; top: 99px; font-size: 150px; line-height: 0.9; font-family: n; color: {c}; content: {g})
  p#u(left: .g.right+10; top: 186px; font-size: 30px; content: {u})
  p#f(left: 34px; top: 270px; font-size: 22px; color: $fg2; font-family: r; white-space: nowrap; content: {f})
  p#k1(left: 34px; top: 344px; font-size: 16px; color: $muted) 実績
  div#b1(left: 110px; top: 339px; width: {gw}; height: 30px; border-radius: 0px 4px 4px 0px; background: #8A97AD59; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#v1(left: 424px; top: 336px; width: 86px; text-align: right; font-size: 30px; font-family: n; color: $muted; content: {gv})
  p#k2(left: 34px; top: 404px; font-size: 16px; color: $muted) 目標
  div#b2(left: 110px; top: 399px; width: {tw}; height: 30px; border-radius: 0px 4px 4px 0px; background: {c}; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#v2(left: 424px; top: 396px; width: 86px; text-align: right; font-size: 30px; font-family: n; content: {tv})
  div#rule(left: 34px; top: 520px; width: 476px; height: 2px; background: $line)
  p#d(left: 34px; top: 538px; width: 476px; font-size: 21px; line-height: 1.55; color: $fg2; font-family: r; content: {d})
# まとめの行 (左の色の縁 + 番号 + 大きな数字 + 太字の 1 行 + 補足)・文の列は hf の 389 px より 11 px 右 (数字の書体が hf より幅広く「43% → 75%」が文に掛かるため)
def item(ix, c, f, b, s) = div(left: 96px; width: 1728px; height: 192px; border-radius: 18px; background: #111925E0; border: 2px solid $line2; in: {x:-40, opacity:0, duration:0.6, ease:'power3.out'}; out: {y:-24, opacity:0, duration:0.6, ease:'power2.in'})
  div#edge(left: 0px; top: 0px; width: 6px; height: 192px; border-radius: 18px 0px 0px 18px; background: {c})
  p#ix(left: 40px; cy: 50%; font-size: 60px; font-family: n; color: $slate2; content: {ix})
  p#f(left: 117px; cy: 50%; font-size: 108px; line-height: 1; font-family: n; color: {c}; white-space: nowrap; content: {f})
  p#b(left: 600px; top: 51px; font-size: 34px; line-height: 1.35; white-space: nowrap; content: {b})
  p#s(left: 600px; top: 108px; font-size: 24px; color: $fg2; font-family: r; white-space: nowrap; content: {s})

# 全編の地 (根・z back): 紺の放射の地・全編で斜めに流れる方眼 (縁へ薄れる)・左上の青緑と右下の琥珀の光 (ゆっくり揺れる)・grain
div#bg_base(inset: 0; background: radial(#0F1724,#0A0F17@60%,#080C13,30%,20%); z-index: back; in: none)
div#bg_grid.bleed(left: -80px; top: -80px; width: 2079px; height: 1239px; pattern: grid,32,#94A3B814; z-index: back; in: none; main: keys(at=0 x=0 y=0 | at=1 x=-48 y=-24 ease=none),duration=106000)
div#bg_vig(inset: 0; background: radial(#0A0F1700@40%,#0A0F17D9,50%,50%); z-index: back; in: none)
div#bg_glow1.bleed(left: -380px; top: -520px; width: 1100px; height: 1100px; background: radial(#2EC4B621,#2EC4B600@65%,50%,50%); z-index: back; in: none; main: sine {x: 34, period: 18})
div#bg_glow2.bleed(left: 1180px; top: 520px; width: 1200px; height: 1200px; background: radial(#F6C35B17,#F6C35B00@65%,50%,50%); z-index: back; in: none; main: sine {y: -30, period: 22})
veil#bg_grain(grain: 0.05; color: #00000000; z-index: back; in: none)

# a 題: 夜のサポート机の写真が 1.12 → 1 に引き、左の暗い余白に小札 → mask から上がる 2 行 → 副題。数字の語で 3 枚の札が弾み (4,128 は数える)、「分類」で 7 つの名札
section#a(stagger: {each:0})
img#a_img(inset: 0; subject: right 38%; room: left 60%; main: kb {scale: [1.12, 1], focus: ['70% 50%', '70% 50%']}) [photo]夜のモダンなオフィスのカスタマーサポートの机の広角。キーボードの横にヘッドセットが置かれ、2 台のモニターに問い合わせの札の列と小さな棒グラフが読めない抽象的な形で柔らかく光る。深い紺と青緑の色調に琥珀色のかすかな差し色の明かり、浅い被写界深度、暗めの照明。机とモニターは画面の右 4 割に置き、画面の左 6 割は暗く何もない余白にする。文字・数字・ロゴなし
# 左から暗くする幕 (左 97% → 右 32%) と右の主体の周りの減光
div#a_shade(inset: 0; background: linear(#0A0F17F7,#0A0F17ED@34%,#0A0F1799@58%,#0A0F1752,90))
div#a_shade2(inset: 0; background: radial(#0A0F1700@40%,#0A0F17B3,75%,45%))
div#a_kick(left: 120px; top: 170px; width: 1050px; height: 36px; delay: 150ms; in: {x:-30, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 44px; height: 3px; background: $teal2)
  p#t(left: 58px; cy: 50%; font-size: 24px; color: $teal2; letter-spacing: 0.06em; white-space: nowrap) ワークノート サポート窓口 ｜ 7〜9 月の問い合わせ分析
p#a_t1(left: 120px; top: 234px; font-size: 98px; line-height: 1.16; letter-spacing: -0.02em; white-space: nowrap; delay: 250ms; in: {y:135, duration:0.85, ease:'expo.out', clip:true}) 問い合わせ {big}4,000{/} 件を
p#a_t2(left: 120px; top: 374px; font-size: 98px; line-height: 1.16; letter-spacing: -0.02em; white-space: nowrap; delay: 420ms; in: {y:123, duration:0.85, ease:'expo.out', clip:true}) 分類してわかったこと
p#a_sub(left: 120px; top: 525px; font-size: 28px; color: $fg2; font-family: r; white-space: nowrap; delay: 800ms; in: {y:18, opacity:0, duration:0.6, ease:'power2.out'}) 勤怠・経費精算 SaaS{b}「ワークノート」{/}サポート窓口の 3 か月
# 3 枚の札 (大きな数字 + 単位 + 補足)
div#a_st(left: "120;432;885"; top: 690px; width: "290;431;290"; height: 150px; border-radius: 16px; background: #111925DB; border: 2px solid $line2; in: {y:30, opacity:0, duration:0.55, ease:'back.out(1.4)'}) ×3
  p#v(left: 24px; top: 18px; font-size: 76px; line-height: 1; font-family: n; color: "$fg;$amber;$fg") 3;[count:4,128 start=0 ms=1000ms delay=100ms];7
  p#u(left: .v.right+9; top: 54px; font-size: 26px; color: $fg2) か月;件;カテゴリ
  p#l(left: 24px; top: 105px; font-size: 20px; color: $muted; font-family: r; white-space: nowrap) 7 月・8 月・9 月;メール・チャット・フォームの合計;全件を読んで分類
# 7 つのカテゴリの名札 (色の四角 + 名・2 行に折り返す)
p#a_cat(left: "120;368;498;668;954;120;270"; top: "870;870;870;870;870;912;912"; font-size: 20px; color: $fg2; padding: 0px 0px 0px 27px; white-space: nowrap; in: {y:16, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.07}}) ×7 ログイン・アカウント;操作方法;請求・プラン;データ連携（CSV・API）;不具合の報告;権限・設定;その他
  div#sw(left: 0px; cy: 50%; width: 16px; height: 16px; border-radius: 4px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2")

# b 方法: 上端の帯と下端の出典の帯が溶けて出る (sticky・最後まで)・板の 4 列 (チャネル → 全件 → 7 分類 → 3 つの指標) を頭に組み、指標の札を語で右から
section#b(stagger: {each:0})
# 上端の帯: 題の印 + 題 (左)・9 つの点 + 「0N / 09」(右)・細い線の上の進行
div#hdr.sticky(left: 96px; top: 34px; width: 1728px; height: 40px; z-index: front; delay: 100ms; in: {opacity:0, duration:0.6, ease:'power2.out'})
  svg#mk(left: 0px; cy: 50%; width: 30px; height: 30px; part: mark)
  p#br(left: 44px; cy: 50%; font-size: 21px; color: $fg2; font-family: r; white-space: nowrap) ワークノート サポート窓口{sp}　｜　{/}{sc}問い合わせ分析 7〜9 月{/}
  shape#d(left: "1442;1463;1484;1505;1526;1547;1568;1589;1610"; cy: 50%; width: 10px; height: 10px; border-radius: 50%; background: #2A3850) ×9
  p#lbl(right: 0px; cy: 50%; width: 96px; text-align: right; font-size: 18px; font-family: m; color: $muted; letter-spacing: 0.06em) 01 / 09
div#hdr_line.sticky(left: 96px; top: 92px; width: 1728px; height: 2px; background: #1C2840; z-index: front; delay: 100ms; in: {opacity:0, duration:0.6, ease:'power2.out'})
progress#prog.sticky(left: 96px; top: 92px; width: 1728px; height: 2px; background: linear($teal,$teal2,90); until: end; z-index: front; overlap: hdr_line)
# 下端の出典の帯
div#ftr.sticky(left: 96px; top: 1020px; width: 1728px; height: 30px; z-index: front; delay: 100ms; in: {opacity:0, duration:0.6, ease:'power2.out'})
  p#tag(left: 0px; cy: 50%; font-size: 15px; font-family: m; color: $fg2; letter-spacing: 0.08em; border: 2px solid $line2; border-radius: 4px; padding: 0px 8px) DATA
  p#src(left: .tag.right+10; cy: 50%; font-size: 18px; color: $muted; font-family: r; white-space: nowrap) 対象：7〜9 月に届いた問い合わせ 4,128 件（メール・チャット・フォーム）
  p#own(right: 0px; cy: 50%; font-size: 18px; color: $muted; font-family: r; white-space: nowrap) ワークノート サポートチーム 社内共有
head#b_h(n: "01"; k: "分析の方法"; t: "4,128 件を 7 カテゴリに分け、{t}3 つの指標{/}で比べた")
board#b_bd(left: 96px; top: 292px; width: 1728px; height: 676px; t: "分析の流れ"; u: "対象：7〜9 月の問い合わせ 全件"; delay: 150ms)
  # 列の頭 (番号の枠 + 題)
  div#ch(left: "48;431;851;1274"; top: 100px; width: 405px; height: 32px; delay: 400ms; in: {y:10, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.18}}) ×4
    p#n(left: 0px; cy: 50%; font-size: 16px; font-family: m; color: $teal2; border: 2px solid #7ADFD380; border-radius: 4px; padding: 0px 8px) 1;2;3;4
    p#t(left: 32px; cy: 50%; font-size: 21px; color: $muted; letter-spacing: 0.04em; white-space: nowrap) 受付チャネル;全件を読む;7 カテゴリに分類;3 つの指標で突き合わせ
  div#chan(left: 48px; top: "155;278;401"; width: 300px; height: 104px; border-radius: 12px; background: $panel2; border: 2px solid $line2; delay: 500ms; in: {x:-26, opacity:0, duration:0.45, ease:'power2.out', stagger:{each:0.1}}) ×3
    icon#i(left: 22px; cy: 50%; font-size: 38px; name: "envelope-simple;chat-centered-text;article"; color: $teal2)
    p#t(left: 78px; cy: 50%; font-size: 27px) メール;チャット;フォーム
  svg#ar(left: "353;773;1196"; top: 322px; width: 64px; height: 24px; part: arrow; delay: 850ms; in: {scaleX:0, opacity:0, duration:0.4, ease:'power2.out', pivot:'left', stagger:{each:0.3}}) ×3
  div#ra(left: 430px; top: 154px; width: 320px; height: 352px; border-radius: 14px; background: $panel2; border: 2px solid $line2; delay: 950ms; in: {scale:0.9, opacity:0, duration:0.5, ease:'back.out(1.5)'})
    p#v(cx: 50%; top: 72px; font-size: 116px; line-height: 1; font-family: n; color: $amber) 4,128
    p#u(cx: 50%; top: 194px; font-size: 28px; color: $fg2) 件
    p#s(cx: 50%; top: 249px; font-size: 20px; color: $muted; font-family: r; white-space: nowrap) 3 か月分をすべて
  div#cat(left: 850px; top: "155;206;257;308;359;410;461"; width: 330px; height: 42px; border-radius: 8px; background: #152030B3; border: 2px solid $line; delay: 1250ms; in: {x:-18, opacity:0, duration:0.35, ease:'power2.out', stagger:{each:0.06}}) ×7
    div#sw(left: 14px; cy: 50%; width: 16px; height: 16px; border-radius: 4px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2")
    p#t(left: 40px; cy: 50%; font-size: 20px; color: $fg2; white-space: nowrap) ログイン・アカウント;操作方法;請求・プラン;データ連携（CSV・API）;不具合の報告;権限・設定;その他
  # 3 つの指標 (語で右から弾んで入る)
  div#m(left: 1274px; top: "155;276;398"; width: 410px; height: 108px; border-radius: 12px; background: $panel2; border: 2px solid $line2; in: {x:30, opacity:0, duration:0.45, ease:'back.out(1.6)'}) ×3
    p#ix(left: 20px; cy: 50%; width: 30px; text-align: center; font-size: 44px; font-family: n; color: $teal2) A;B;C
    p#b(left: 66px; top: 24px; font-size: 26px; white-space: nowrap) 初回で解決したか;解決までの時間;担当者の対応時間
    p#s(left: 66px; top: 62px; font-size: 18px; color: $muted; font-family: r; white-space: nowrap) 初回解決率;受付から解決まで;3 か月の合計・1 件あたり平均
  p#note(left: 32px; bottom: 20px; font-size: 18px; line-height: 1.5; color: $muted; font-family: r; in: {opacity:0, duration:0.5}) ※ 「解決までの時間」は受付から解決までの経過時間、「対応時間」は担当者が対応にかけた時間。

# c 月別: 右の板に縦棒 3 本が 0.15 秒ずつ伸び、値と破線の伸び (点) が乗る・「12%」で左に大きな +12% が数えて弾み、件数の前後と「利用企業」の札
section#c(stagger: {each:0})
head#c_h(n: "02"; k: "月別の件数"; t: "3 か月で {t}12% 増{/}。利用企業の増加とほぼ同じ伸び")
p#c_lab(left: 96px; top: 330px; font-size: 24px; color: $muted; delay: 300ms; in: {x:-20, opacity:0, duration:0.45, ease:'power2.out'}) 7 月 → 9 月の増加
p#c_pct(left: 96px; top: 420px; font-size: 230px; line-height: 0.86; font-family: n; color: $teal2; transform-origin: 0% 70%; in: {scale:0.7, opacity:0, duration:0.6, ease:'back.out(1.5)'}) +[count:12 start=0 ms=800ms]%
p#c_ft(left: 96px; top: 666px; font-size: 26px; color: $fg2; white-space: nowrap; in: {y:14, opacity:0, duration:0.45, ease:'power2.out'}) {nf}1,296{/} 件 {ar}→{/} {nf}1,448{/} 件
p#c_call(left: 96px; top: 760px; font-size: 22px; background: #152030F5; border: 2px solid #7ADFD38C; border-radius: 10px; padding: 10px 18px 10px 56px; white-space: nowrap; in: {x:-30, opacity:0, duration:0.5, ease:'power3.out'}) 利用企業の増加とほぼ同じ伸び
  icon#i(left: 18px; cy: 50%; font-size: 26px; name: buildings; color: $teal2)
board#c_bd(left: 700px; top: 292px; width: 1124px; height: 676px; t: "月別の問い合わせ件数"; u: "単位：件"; delay: 120ms)
  # 目盛り (0 起点・400 刻み)
  div#gl(left: 120px; top: "120;230;341;450"; width: 940px; height: 2px; background: #94A3B81F) ×4
  div#zero(left: 120px; top: 558px; width: 940px; height: 3px; background: #3A4B66)
  p#gll(left: 0px; top: "110;219;330;440;548"; width: 106px; text-align: right; font-size: 16px; font-family: m; color: $muted) ×5 1,600;1,200;800;400;0
  div#bar(left: "191;506;818"; top: "203;179;162"; width: 170px; height: "357;381;398"; border-radius: 8px 8px 0px 0px; background: "linear(#4F6684,#3B4E68,180);linear(#5D7899,#455C7A,180);linear(#7ADFD3,#2A9D92,180)"; delay: 550ms; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom', stagger:{each:0.15}}) ×3
  p#bv(left: "191;506;818"; top: "218;194;176"; width: 170px; text-align: center; font-size: 46px; font-family: n; color: "$fg;$fg;#0A0F17"; delay: 950ms; in: {y:12, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.15}}) ×3 1,296;1,384;1,448
  p#bx(left: "191;506;818"; top: 576px; width: 170px; text-align: center; font-size: 24px; color: $fg2) ×3 7 月;8 月;9 月
  shape#trend(path: "M276 182 L590 158 L903 140"; background: none; border: 3px solid $teal2; dash: 5,5; delay: 1400ms; in: {opacity:0, duration:0.5})
  shape#dot(left: "269;582;896"; top: "174;150;132"; width: 15px; height: 15px; border-radius: 50%; background: $teal2; delay: 1350ms; in: {scale:0, duration:0.35, ease:'back.out(2.2)', stagger:{each:0.12}}) ×3
  p#note(left: 32px; bottom: 20px; font-size: 18px; color: $muted; font-family: r; in: {opacity:0, duration:0.5}) ※ 3 か月の合計は 4,128 件。縦軸は 0 から。

# d 構成: 構成比の帯 (7 色) が左から 1 枚ずつ開き、7 行の横棒が伸びて件数と % が出る・「ログイン」「操作方法」で行に枠が点き、他の 5 行を沈め、凡例
section#d(stagger: {each:0})
head#d_h(n: "03"; k: "カテゴリ別の件数"; t: "件数が多いのは {t}ログイン・アカウント{/} と {t}操作方法{/}")
board#d_bd(left: 96px; top: 292px; width: 1728px; height: 676px; t: "カテゴリ別の件数と構成比"; u: "N = 4,128 件"; delay: 120ms)
  div#seg(left: "32;398;747;1031;1280;1463;1613"; top: 96px; width: "363;347;281;246;180;147;84"; height: 58px; border-radius: "8,0,0,8;0;0;0;0;0;0,8,8,0"; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2"; delay: 450ms; in: {scaleX:0, opacity:0, duration:0.45, ease:'power2.out', pivot:'left', stagger:{each:0.07}}) ×7
    p#t(cx: 50%; cy: 50%; font-size: 28px; font-family: n; color: "#0A0F17;#0A0F17;#0A0F17;#0A0F17;#0A0F17;#0A0F17;$fg") 22%;21%;17%;15%;11%;9%;5%
  div#r(left: 18px; top: "186;240;294;348;402;456;510"; width: 1690px; height: 54px; in: none) ×7
    # 行の枠 (語で点く 2 行だけ・他の行の枠は透明)
    div#hl(left: 0px; top: 4px; width: 1690px; height: 45px; border-radius: 10px; background: #2EC4B614; border: 3px solid #7ADFD3B3; opacity: "1;1;0;0;0;0;0"; in: {opacity:0, duration:0.35, ease:'power2.out'})
    cat#nm(left: 14px; cy: 50%; t: "ログイン・アカウント;操作方法;請求・プラン;データ連携（CSV・API）;不具合の報告;権限・設定;その他"; c: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2"; delay: "600ms;660ms;720ms;780ms;840ms;900ms;960ms"; in: {x:-20, opacity:0, duration:0.4, ease:'power2.out'})
    div#bar(left: 393px; cy: 50%; width: "900;860;696;614;450;368;206"; height: 30px; border-radius: 0px 6px 6px 0px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2"; delay: "750ms;820ms;890ms;960ms;1030ms;1100ms;1170ms"; in: {scaleX:0, duration:0.75, ease:'power3.out', pivot:'left'})
    div#val(left: 1394px; cy: 50%; width: 210px; height: 45px; delay: "1050ms;1120ms;1190ms;1260ms;1330ms;1400ms;1470ms"; in: {x:-12, opacity:0, duration:0.4, ease:'power2.out'})
      p#n(left: 0px; cy: 50%; width: 90px; text-align: right; font-size: 36px; font-family: n) 908;867;702;619;454;371;207
      p#u(left: 104px; cy: 50%; font-size: 20px; color: $muted) 件
      p#pc(left: 134px; cy: 50%; width: 70px; text-align: right; font-size: 30px; font-family: n; color: $fg2) 22%;21%;17%;15%;11%;9%;5%
  # 色の見方 (凡例)
  div#leg(left: 32px; top: 624px; width: 1500px; height: 30px; in: {y:10, opacity:0, duration:0.5, ease:'power2.out'})
    p#t0(left: 0px; cy: 50%; font-size: 20px; color: $muted) 色の見方
    div#s(left: "113;129;377;393;410;857;873"; cy: 50%; width: 14px; height: 14px; border-radius: 3px; background: "$teal;$teal2;$amber;$orange;$coral;$slate;$slate2") ×7
    p#t(left: "153;434;897"; cy: 50%; font-size: 20px; color: $muted; white-space: nowrap) ×3 件数が多い 2 カテゴリ;対応に時間がかかる 3 カテゴリ（後半で詳しく）;その他の 2 カテゴリ

# e 初回解決率: 右の板の 7 行が頭に伸び、「59%」で左の輪が弧を描いて数え、板に全体の破線・81 / 34 / 22 の語で行に枠 (青緑 / 珊瑚)・中の 4 行を沈める
section#e(stagger: {each:0})
head#e_h(n: "04"; k: "初回解決率"; t: "初回で解決するのは {t}59%{/}。カテゴリで大きく違う")
# 輪 (地の輪 + 59% の弧を描く + 中央の数字)
group#e_g(in: {scale:0.86, opacity:0, duration:0.6, ease:'power3.out'})
  shape#track(left: 126px; top: 346px; width: 410px; height: 410px; border-radius: 50%; background: none; border: 28px solid #1D2A3E)
  # 59% の弧 (12 時から時計回りに 212°・線の中心が地の輪の中心に乗る枠)
  shape#arc(left: 140px; top: 360px; width: 381px; height: 381px; path: arc,start=0,to=212.4; background: none; border: 28px solid $teal2; in: draw {duration: 1.2})
  p#v(cx: 330px; cy: 528px; font-size: 150px; line-height: 0.95; font-family: n) [count:59 start=0 ms=1200ms]%
  p#l(cx: 330px; cy: 624px; font-size: 24px; color: $fg2; white-space: nowrap) 初回で解決（全体）
p#e_cap(left: 96px; top: 798px; width: 470px; text-align: center; font-size: 22px; color: $muted; in: {y:10, opacity:0, duration:0.5, ease:'power2.out'}) {n21}2,442{/} 件 / {n21}4,128{/} 件
board#e_bd(left: 640px; top: 292px; width: 1184px; height: 676px; t: "カテゴリ別の初回解決率"; u: "単位：%"; delay: 300ms; in: {x:40, opacity:0, duration:0.65, ease:'power3.out'})
  # 行の枠は語で点く 3 行 (81 の青緑・34 / 22 の珊瑚) だけ・他の行の枠は透明
  div#r(left: 18px; top: "140;201;263;324;386;447;509"; width: 1148px; height: 62px; in: none) ×7
    div#hl(left: 0px; top: 6px; width: 1148px; height: 50px; border-radius: 10px; background: "#2EC4B614;#2EC4B614;#2EC4B614;#2EC4B614;#2EC4B614;#E8615A14;#E8615A14"; border: "3px solid #7ADFD3BF;3px solid #7ADFD3BF;3px solid #7ADFD3BF;3px solid #7ADFD3BF;3px solid #7ADFD3BF;3px solid #E8615ABF;3px solid #E8615ABF"; opacity: "1;0;0;0;0;1;1"; in: {opacity:0, duration:0.3})
    cat#nm(left: 14px; cy: 50%; width: 330px; t: "ログイン・アカウント;操作方法;権限・設定;請求・プラン;その他;データ連携（CSV・API）;不具合の報告"; c: "$teal;$teal2;$slate;$amber;$slate2;$orange;$coral"; delay: "600ms;660ms;720ms;780ms;840ms;900ms;960ms"; in: {x:-16, opacity:0, duration:0.4, ease:'power2.out'})
    div#tr(left: 344px; cy: 50%; width: 600px; height: 32px; border-radius: 0px 6px 6px 0px; background: #FFFFFF0A)
    div#bar(left: 344px; cy: 50%; width: "486;444;378;348;330;204;132"; height: 32px; border-radius: 0px 6px 6px 0px; background: "$teal;$teal2;$slate;$amber;$slate2;$orange;$coral"; delay: "700ms;770ms;840ms;910ms;980ms;1050ms;1120ms"; in: {scaleX:0, duration:0.75, ease:'power3.out', pivot:'left'})
    p#v(left: 963px; cy: 50%; width: 110px; text-align: right; font-size: 40px; font-family: n; color: "$fg;$fg;$fg;$fg;$fg;$coral;$coral"; delay: "1000ms;1070ms;1140ms;1210ms;1280ms;1350ms;1420ms"; in: {opacity:0, duration:0.4}) 81%;74%;63%;58%;55%;34%;22%
  # 全体 59% の破線 (上から下りる) と札
  shape#avg(left: 716px; top: 128px; width: 3px; height: 450px; path: line_v; border: 3px solid #E9EEF58C; dash: 5,5; in: {scaleY:0, opacity:0, duration:0.5, ease:'power2.out', pivot:'top'})
  p#al(left: 652px; top: 93px; width: 128px; text-align: center; font-size: 20px; background: $panel2; border: 2px solid $line2; border-radius: 6px; padding: 2px 0px; in: {opacity:0, duration:0.5})  全体 59%
  p#note(left: 32px; bottom: 20px; font-size: 18px; color: $muted; font-family: r; white-space: nowrap; in: {opacity:0, duration:0.5}) ※ 破線は全体の初回解決率 59%（2,442 件 / 4,128 件）。{b}データ連携 34%・不具合の報告 22%{/} は全体を大きく下回る。

# f 解決までの時間: 6 本の縦棒が伸びて値が乗り、「4 時間以内に約 6 割」のかぎ・「中央値」で札と破線の引き出し・「3 日を」で長い尾のかぎと右の板・372 で尾の 2 本が明るく脈打ち、78% が数えて帯が伸びる
section#f(stagger: {each:0})
head#f_h(n: "05"; k: "解決までの時間"; t: "中央値は {t}1 時間 50 分{/}。ただし 3 日超の“長い尾”が {c}372 件{/}")
board#f_bd(left: 96px; top: 292px; width: 1150px; height: 676px; t: "受付から解決までの時間"; u: "単位：件（構成比）"; delay: 120ms)
  div#base(left: 70px; top: 548px; width: 1010px; height: 3px; background: #3A4B66)
  div#bar(left: "92;260;428;596;764;933"; top: "261;368;422;459;504;528"; width: 128px; height: "290;183;129;92;47;23"; border-radius: 8px 8px 0px 0px; background: "linear(#7ADFD3,#2A9D92,180);linear(#7ADFD3,#2A9D92,180);linear(#5D7899,#455C7A,180);linear(#5D7899,#455C7A,180);linear(#F07A6F,#C84B45,180);linear(#F07A6F,#C84B45,180)"; delay: 550ms; in: {scaleY:0, duration:0.7, ease:'power3.out', pivot:'bottom', stagger:{each:0.1}}) ×6
  # 尾の 2 本を明るくする薄い白の板 (372 の語で 1 往復だけ点く = hf の brightness(1.35) の yoyo)
  div#hi(left: "764;933"; top: "504;528"; width: 128px; height: "47;23"; border-radius: 8px 8px 0px 0px; background: #FFFFFF; opacity: 0; in: none) ×2
  div#hv(left: "71;239;408;576;744;912"; top: "191;297;351;389;434;458"; width: 168px; height: 69px; delay: 900ms; in: {y:10, opacity:0, duration:0.4, ease:'power2.out', stagger:{each:0.1}}) ×6
    p#n(cx: 50%; top: 0px; font-size: 40px; line-height: 1; font-family: n; color: "$fg;$fg;$fg;$fg;$coral;$coral") 1,568;991;702;495;248;124
    p#p(cx: 50%; top: 44px; font-size: 20px; color: $muted) 38%;24%;17%;12%;6%;3%
  p#hx(left: "71;239;408;576;744;912"; top: 564px; width: 168px; text-align: center; font-size: 22px; color: $fg2; white-space: nowrap; delay: 700ms; in: {opacity:0, duration:0.4, stagger:{each:0.06}}) ×6 1 時間以内;1〜4 時間;4〜24 時間;1〜3 日;3〜7 日;7 日超
  # かぎ (4 時間以内 / 3 日超) と札
  shape#brf(path: "M90.8 181.9 V168 H387 V181.9"; background: none; border: 3px solid $teal2; delay: 1700ms; in: {opacity:0, duration:0.4})
  p#labf(left: 92px; top: 130px; width: 296px; text-align: center; font-size: 21px; color: $teal2; white-space: nowrap; delay: 1750ms; in: {y:8, opacity:0, duration:0.4, ease:'power2.out'}) 4 時間以内に約 6 割
  shape#brt(path: "M764.0 426.2 V412.0 H1060.3 V426.2"; background: none; border: 3px solid $coral; in: {opacity:0, duration:0.4})
  p#labt(left: 704px; top: 374px; width: 417px; text-align: center; font-size: 21px; color: $coral; white-space: nowrap; in: {y:8, opacity:0, duration:0.4, ease:'power2.out'}) 3 日超：372 件（9%）
  # 中央値の札と、1〜4 時間の棒へ下りる破線の引き出し
  shape#lead(path: "M630.5 232.6 L353.0 286.6"; background: none; border: 2px solid $teal2; dash: 3,4; in: {opacity:0, duration:0.4})
  shape#ldot(left: 346px; top: 280px; width: 12px; height: 12px; border-radius: 50%; background: $teal2; in: {opacity:0, duration:0.4})
  p#pin(left: 630px; top: 207px; font-size: 21px; background: $panel2; border: 2px solid $teal2; border-radius: 8px; padding: 6px 12px; white-space: nowrap; in: {y:-12, opacity:0, duration:0.45, ease:'back.out(1.8)'}) 中央値　1 時間 50 分
  p#note(left: 32px; bottom: 20px; font-size: 18px; color: $muted; font-family: r; in: {opacity:0, duration:0.5}) ※ 受付から解決までの経過時間で 6 区分。中央値は 1 時間 50 分。
board#f_sd(left: 1280px; top: 292px; width: 544px; height: 676px; t: "長い尾（3 日超）の内訳"; u: "受付から 3 日超"; pc: $coral; in: {x:40, opacity:0, duration:0.65, ease:'power3.out'})
  div#st1(left: 32px; top: 100px; width: 482px; height: 150px; in: {y:18, opacity:0, duration:0.5, ease:'power3.out'})
    p#l(left: 0px; top: 0px; font-size: 21px; color: $fg2) 3 日を超えた案件
    p#n(left: 0px; top: 34px; font-size: 104px; line-height: 1.02; font-family: n; color: $coral) 372
    p#u(left: .n.right+12; top: 86px; font-size: 30px) 件
    p#s(left: .u.right+6; top: 90px; font-size: 22px; color: $fg2; font-family: r) 全体の 9%
  div#st2(left: 32px; top: 300px; width: 482px; height: 165px; in: {y:18, opacity:0, duration:0.5, ease:'power3.out'})
    div#rule(left: 0px; top: 0px; width: 482px; height: 2px; background: $line)
    p#l(left: 0px; top: 22px; font-size: 21px; color: $fg2; white-space: nowrap) そのうち、データ連携・不具合の報告が
    p#n(left: 0px; top: 57px; font-size: 104px; line-height: 1.02; font-family: n; color: $orange) [count:78 start=0 ms=800ms delay=100ms]%
    p#u(left: .n.right+12; top: 108px; font-size: 30px) 291 件
  div#split(left: 32px; top: 476px; width: 480px; height: 50px; border-radius: 8px; background: #2A3850; in: {opacity:0, duration:0.4})
    div#a(left: 0px; top: 0px; width: 375px; height: 50px; border-radius: 8px 0px 0px 8px; background: linear($orange,$coral,90); in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
      # hf の作り: 橙の帯の上の暗い字 (check は全編の grain の幕と比べて low_contrast を出す)
      p#t(left: 16px; cy: 50%; font-size: 30px; font-family: n; color: #0A0F17) 291 件
  div#lsw(left: "32;48;32"; top: "551;551;587"; width: 14px; height: 14px; border-radius: 3px; background: "$orange;$coral;#2A3850"; in: {opacity:0, duration:0.4}) ×3
  p#lt(left: "72;56"; top: "542;578"; font-size: 20px; color: $fg2; font-family: r; white-space: nowrap; in: {opacity:0, duration:0.4}) ×2 データ連携・不具合の報告;そのほかのカテゴリ
  p#note(left: 32px; bottom: 20px; font-size: 18px; color: $muted; font-family: r; white-space: nowrap) ※ 3 日を超えた 372 件（全体の 9%）が対象。

# g 対応時間: 左の板に件数の積み上げ棒が頭に積み上がり、「対応時間」で右の棒が積み上がる・「データ連携」で 2 本をつなぐ帯と上位 3 以外を沈め、右の板の 3 行 + 参考の行・43% と 75% の大きな札
section#g(stagger: {each:0})
head#g_h(n: "06"; k: "担当者の対応時間"; t: "件数の {a}43%{/} が、対応時間の {a}75%{/} を占める")
board#g_cmp(left: 96px; top: 292px; width: 820px; height: 676px; t: "件数と対応時間の構成比"; u: "3 か月"; pc: $amber; delay: 120ms)
  # 2 本をつなぐ帯 (上位 3 の境を結ぶ琥珀の面 + 破線・その上の灰の面)
  shape#rib(points: "320,570;320,368;500,216;500,570"; background: #F6C35B29; border: none; in: {opacity:0, duration:0.6, ease:'power1.out'})
  shape#rib2(points: "320,368;320,101;500,101;500,216"; background: #8A97AD12; border: none; in: {opacity:0, duration:0.6, ease:'power1.out'})
  shape#ribl(path: "M320.0 368.0 L500.0 215.7"; background: none; border: 3px solid $amber; dash: 4,4; in: {opacity:0, duration:0.6, ease:'power1.out'})
  # 件数の積み上げ (下から データ連携・不具合・請求・ログイン・操作方法・権限・その他)
  div#sc(left: 170px; top: "503;450;371;267;168;126;101"; width: 150px; height: "68;50;77;101;96;39;23"; background: "$orange;$coral;$amber;$teal;$teal2;$slate;$slate2"; delay: 550ms; in: {scaleY:0, duration:0.4, ease:'power2.out', pivot:'bottom', stagger:{each:0.06}}) ×7
  # 対応時間の積み上げ (下から データ連携・不具合・請求・ログイン・残り)
  div#st(left: 500px; top: "426;294;219;183;101"; width: 150px; height: "144;129;72;33;80"; background: "$orange;$coral;$amber;$teal;#3B4A62"; in: {scaleY:0, duration:0.45, ease:'power2.out', pivot:'bottom', stagger:{each:0.08}}) ×5
  div#slab(left: "131;461"; top: 574px; width: 230px; height: 60px) ×2
    p#t(cx: 50%; top: 0px; font-size: 22px) 件数;対応時間
    p#s(cx: 50%; top: 33px; font-size: 18px; color: $muted; font-family: r; white-space: nowrap) 4,128 件;4,175 時間
  p#g43(left: 30px; top: 418px; font-size: 76px; line-height: 1; font-family: n; color: $amber; in: {x:-20, opacity:0, duration:0.5, ease:'power3.out'}) 43%
    p#s(left: 0px; top: 82px; font-size: 18px; color: $fg2; font-family: g; white-space: nowrap) 1,775 件
  p#g75(left: 662px; top: 338px; font-size: 86px; line-height: 1; font-family: n; color: $amber; transform-origin: 0% 50%; in: {scale:0.7, opacity:0, duration:0.6, ease:'back.out(1.6)'}) 75%
    p#s(left: 0px; top: 92px; font-size: 18px; color: $fg2; font-family: g; white-space: nowrap) 3,147 時間
board#g_top(left: 950px; top: 292px; width: 874px; height: 676px; t: "時間を食っている上位 3 カテゴリ"; u: "対応時間の合計（3 か月）"; pc: $amber; in: {x:40, opacity:0, duration:0.65, ease:'power3.out'})
  div#r(left: 32px; top: "108;204;300;431"; width: 810px; height: 96px; opacity: "1;1;1;0.92"; in: {y:14, opacity:0, duration:0.45, ease:'power2.out'}) ×4
    div#sw(left: 0px; top: 9px; width: 16px; height: 16px; border-radius: 4px; background: "$orange;$coral;$amber;$teal")
    p#nm(left: 28px; top: 2px; font-size: 22px; white-space: nowrap) データ連携（CSV・API）;不具合の報告;請求・プラン;ログイン・アカウント{mu}（908 件）{/}
    div#bar(left: 0px; top: 42px; width: "470;426;242;116"; height: 30px; border-radius: 0px 6px 6px 0px; background: "$orange;$coral;$amber;$teal"; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#n(left: 490px; top: 30px; width: 130px; text-align: right; font-size: 46px; font-family: n) 1,300;1,180;667;318
    p#u(left: 627px; top: 51px; font-size: 20px; color: $fg2) 時間
    p#avg(right: 0px; top: 30px; text-align: right; font-size: 18px; line-height: 1.2; color: $muted; font-family: r) 1 件平均[br]{an}2.1{/} 時間;1 件平均[br]{an}2.6{/} 時間;1 件平均[br]{an}0.95{/} 時間;1 件平均[br]{an}0.35{/} 時間
  div#dv(left: 32px; top: 394px; width: 810px; height: 34px; in: {opacity:0, duration:0.45})
    p#t(left: 0px; cy: 50%; font-size: 18px; color: $muted; white-space: nowrap) 参考：件数が最も多いカテゴリ
    div#ln(left: 282px; cy: 50%; width: 528px; height: 2px; background: $line2)
  div#sum(left: 32px; top: 608px; width: 812px; height: 50px; in: {y:10, opacity:0, duration:0.5})
    div#rule(left: 0px; top: 0px; width: 812px; height: 2px; background: $line)
    p#a(left: 0px; top: 15px; font-size: 20px; color: $fg2; white-space: nowrap) 3 カテゴリ合計：件数 {ab}1,775 件（43%）{/}
    p#b(left: .a.right+26; top: 15px; font-size: 20px; color: $fg2; white-space: nowrap) 対応時間 {ab}3,147 時間（75%）{/}

# h ヘルプページ: 左にノートパソコンのヘルプページの写真 (寄り続ける) と条件・右の板に 2 本の斜線の帯が語で伸び、「655」で合計の枠が数え、「247」で時間が数える
section#h(stagger: {each:0})
head#h_h(n: "07"; k: "ヘルプページで減らせる問い合わせ"; t: "{t}655 件（全体の 16%）{/}は、ヘルプページで答えられる内容だった")
div#h_fr(left: 96px; top: 300px; width: 760px; height: 470px; border-radius: 16px; border: 2px solid $line2; overflow: hidden; box-shadow: 0px 30px 70px #00000080; delay: 150ms; in: {y:30, opacity:0, duration:0.7, ease:'power3.out'})
  img#p(inset: 0; subject: center 70%; main: kb {scale: [1, 1.08], focus: ['55% 45%', '55% 45%']}) [photo]夜の暗い木の机に置かれたノートパソコンを斜め前から。画面にはすっきりしたヘルプセンターのページが映り、上に検索欄、その下に整った FAQ の項目の列が光の線と角丸の塊で抽象的に並ぶ (読める文字はない)。項目の横に小さく光る鍵のアイコンがパスワード再設定をほのめかす。紺と青緑のほのかな光、柔らかな映画的な縁の光、落ち着いて整った雰囲気、周りは暗い。斜め前から寄った構図で、ノートパソコンの画面と本体が枠の横幅の 8 割を占めるほど大きく写り、机の奥の暗がりにぼけた観葉植物と街の灯り。余白を作らない。文字・数字・ロゴなし
  div#fx(inset: 0; background: linear(#0A0F1700@55%,#0A0F178C,180))
div#h_cap(left: 96px; top: 796px; width: 760px; height: 75px; delay: 600ms; in: {y:10, opacity:0, duration:0.5, ease:'power2.out'})
  p#q(left: 0px; top: 3px; font-size: 18px; font-family: m; color: $teal2; border: 2px solid #7ADFD380; border-radius: 4px; padding: 0px 8px) 条件
  p#t(left: 68px; top: 0px; width: 693px; font-size: 21px; line-height: 1.55; color: $fg2; font-family: r) 既存のヘルプページに答えがある、または 1 ページ足せば答えられる問い合わせを数えた
board#h_bd(left: 900px; top: 292px; width: 924px; height: 676px; t: "ヘルプページで減らせる見込み"; u: "単位：件"; delay: 300ms; in: {x:40, opacity:0, duration:0.65, ease:'power3.out'})
  div#rh(left: 32px; top: "113;255"; width: 860px; height: 135px; in: {y:12, opacity:0, duration:0.45, ease:'power2.out'}) ×2
    div#sw(left: 0px; top: 9px; width: 16px; height: 16px; border-radius: 4px; background: "$teal2;$teal")
    p#t(left: 28px; top: 0px; font-size: 24px; white-space: nowrap) 操作方法;ログイン・アカウント
    div#tr(left: 0px; top: 46px; width: 800px; height: 40px; border-radius: 6px; background: #8A97AD2E; border: 2px solid #8A97AD59)
    # 斜線の帯 (減らせる分・左から伸びる)
    div#rd(left: 0px; top: 46px; width: "327;264"; height: 40px; border-radius: 6px 0px 0px 6px; background: #7ADFD3F2; pattern: hatch,45,#2EC4B6F2,13,7; in: {scaleX:0, duration:0.7, ease:'power3.out', pivot:'left'})
    p#l(left: 0px; top: 94px; font-size: 20px; color: $fg2; white-space: nowrap) うち {n19}355{/} 件（41%）;うち {n19}300{/} 件（33%）
    p#r(right: 60px; top: 96px; font-size: 20px; color: $muted; white-space: nowrap) 全 {n16}867{/} 件;全 {n16}908{/} 件
  p#tag(left: 308px; top: 258px; font-size: 18px; color: $bg; background: $teal2; border-radius: 4px; padding: 2px 9px; white-space: nowrap; in: {y:12, opacity:0, duration:0.45, ease:'power2.out'}) ほぼパスワード再設定
  # 合わせての枠 (655 件 | 約 247 時間)
  div#tot(left: 32px; top: 418px; width: 860px; height: 190px; border-radius: 14px; background: #2EC4B614; border: 2px solid #7ADFD366; in: {y:20, opacity:0, duration:0.5, ease:'power3.out'})
    p#l(left: 30px; top: 24px; font-size: 20px; color: $fg2) 合わせて
    p#n(left: 30px; top: 75px; font-size: 104px; line-height: 0.86; font-family: n; color: $teal2) [count:655 start=0 ms=800ms delay=100ms]
    p#u(left: .n.right+8; top: 129px; font-size: 28px) 件
    p#s(left: .u.right+8; top: 134px; font-size: 22px; color: $fg2; font-family: r; white-space: nowrap) 全体の 16%
    div#sep(left: 380px; top: 34px; width: 2px; height: 120px; background: #7ADFD359)
    div#hrs(left: 414px; top: 0px; width: 420px; height: 190px; in: {opacity:0, duration:0.4})
      p#l(left: 0px; top: 24px; font-size: 20px; color: $fg2) 対応時間にして
      p#a(left: 0px; top: 123px; font-size: 26px) 約
      p#n(left: 33px; top: 87px; font-size: 76px; line-height: 0.86; font-family: n) [count:247 start=0 ms=700ms delay=50ms]
      p#u(left: .n.right+8; top: 126px; font-size: 28px) 時間
  p#note(left: 32px; bottom: 20px; font-size: 18px; color: $fg2; font-family: r; white-space: nowrap; in: {x:-12, opacity:0, duration:0.5, ease:'power2.out'}) {a}→{/} 浮いた時間を、時間を食っている上位 3 カテゴリに回す

# i 目標: 3 枚の札が語ごとに下から入り、実績 (灰) と目標 (色) の 2 本の棒が続けて伸びる
section#i(stagger: {each:0})
head#i_h(n: "08"; k: "次の四半期（10〜12 月）の目標"; t: "件数・初回解決率・長い尾、{t}3 つの目標{/}")
goal#i_c1(left: 96px; ix: "01"; t: "問い合わせ件数"; g: "3,600"; u: "件以下"; f: "7〜9 月の実績 {n21}4,128{/} 件 {t}→ 目標{/}"; c: $teal2; gw: 302px; tw: 262px; gv: "4,128"; tv: "3,600"; d: "ヘルプページの整備で 655 件減を見込み、利用企業の増加分を差し引いた値")
goal#i_c2(left: 688px; ix: "02"; t: "初回解決率"; g: "65%"; u: ""; f: "7〜9 月の実績 {n21}59%{/} {a}→ 目標{/}"; c: $amber; gw: 178px; tw: 196px; gv: "59%"; tv: "65%"; d: "7〜9 月は 2,442 件 / 4,128 件が初回で解決")
goal#i_c3(left: 1280px; ix: "03"; t: "3 日を超える案件"; g: "250"; u: "件以下"; f: "7〜9 月の実績 {n21}372{/} 件 {c}→ 目標{/}"; c: $coral; gw: 302px; tw: 202px; gv: "372"; tv: "250"; d: "データ連携と不具合に、開発チームへの引き継ぎ手順を決める")

# j まとめ: 引き継ぎの光の橋の絵 (1.08 → 1 に引く) を暗い幕の下に・3 行が語ごとに左から入り、3 行目の縁が珊瑚に光る → 行と見出しが上へ抜けて幕が明け、「NEXT ACTION」の題が出て暗転
section#j(stagger: {each:0})
# hf の作り: 引き継ぎの絵は濃い幕の下の地で、まとめの 3 行と締めの題は絵の主体の上に乗る (text_over_subject)
img#j_img(inset: 0; subject: center 60%; room: top 30%; main: kb {scale: [1.08, 1], focus: ['50% 60%', '50% 60%']}) [photo]深い紺の背景の上の、ミニマルな概念的 3D レンダー。暗い空間を挟んで向かい合う 2 つの光る作業机が光の橋でつながり、小さな長方形の札が橋の上を、青緑に光る左の机から温かい琥珀色に光る右の机へ渡っていく (サポートと開発のはっきりした引き継ぎ)。柔らかな立体の光、上品で落ち着いた雰囲気、2 つの机と橋は画面の中ほどから下に横いっぱいに置き、上の 3 割は暗い余白。人物なし、文字・数字・ロゴなし
div#j_shade(inset: 0; background: linear(#0A0F17F0,#0A0F17DB@45%,#0A0F17C7,180))
head#j_h(n: "09"; k: "まとめ"; t: "わかったことと、{a}次の一手{/}"; out: {opacity:0, duration:0.45, ease:'power2.in'})
item#j_i1(top: 300px; ix: "1"; c: $amber; f: "43%{arr} → {/}75%"; b: "時間を食うのは、データ連携・不具合・請求の 3 つ"; s: "件数の 43% で、対応時間の 75%（件数が多いのはログインと操作方法）")
item#j_i2(top: 514px; ix: "2"; c: $teal2; f: "655{u21}件{/}"; b: "ログインと操作方法の 655 件は、ヘルプページで減らせる"; s: "浮いた時間を上位 3 カテゴリに回す")
item#j_i3(top: 729px; ix: "3"; c: $coral; f: "8{u21}割{/}"; b: "3 日超の長い尾の 8 割は、データ連携と不具合"; s: "{cb}次の一手：{/}開発への引き継ぎ手順を決める"; border: 2px solid #E8615A8C)
  p#s(color: $fg)
# 締めの題 (行が抜けた後に出る)
div#j_ek(left: 96px; top: 150px; width: 450px; height: 33px; in: {x:-24, opacity:0, duration:0.5, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 44px; height: 3px; background: $teal2)
  p#t(left: 56px; cy: 50%; font-size: 22px; font-family: m; color: $teal2; letter-spacing: 0.14em; white-space: nowrap) NEXT ACTION
p#j_et(left: 96px; top: 194px; font-size: 64px; line-height: 1.25; letter-spacing: -0.01em; white-space: nowrap; in: {y:26, opacity:0, duration:0.7, ease:'expo.out'}) 次の一手は、{a}開発への引き継ぎ手順{/}を決めること
p#j_es(left: 96px; top: 298px; font-size: 26px; color: $fg2; font-family: r; white-space: nowrap; in: {y:14, opacity:0, duration:0.5, ease:'power2.out'}) 3 日を超える長い尾の 8 割は、データ連携と不具合の報告
```

```timeline.txt
#v2
cast n = "落ち着いた30代男性のナレーター、低めで明瞭な声、社内の分析報告らしく淡々と丁寧に読む"
silence head=0ms tail=0ms
# 切替: 細い光の縦線 (芯 2 px・両脇は淡い光) が左から右へ払い、新しい場面を見せる (窓 600 ms は境目の後ろ・声は窓の頭の 300 ms 後)。風切りは窓の頭の 80 ms 前・乾いたシュッは各場面の最初の語の 250 ms 後
# 線は上から下へ青緑 → 琥珀の縦のグラデ (帯の linear(…,180))
# engine: hf の線の青緑の光の滲み (box-shadow 22 px) は帯に添えられない — グラデの帯は 1 本だけ (縦グラデの芯の両側に半透明の帯を並べると DEFECT:RUNTIME)・滲みを幅方向のグラデで書くと縦の青緑 → 琥珀が消える
transition = wipe {duration: .6, dir: 'right', overlap: .6, ease: 'power2.inOut', bars: 'linear(#7ADFD300,#7ADFD3F2@30%,#F6C35BF2@70%,#F6C35B00,180),3'}

*** a
bgm music
@n: [silence:0.9s][♪telop -1.5dB -650ms]ワークノートのサポート窓口に、[>#a_st[1] -100ms][♪pop -8dB]7月から9月に届いた問い合わせ[>#a_st[2] -150ms][♪blip -10dB][♪chime -4.5dB +950ms]4,128件。全件を読み、[>#a_st[3] -100ms][♪pop -7dB]7つのカテゴリに[>#a_cat[*] -150ms][♪swish -3dB]分類しました。[silence:0.20s]

*** b
@n: [silence:0.3s][!#hdr.d[1] to,{scale:1.3, fill:'#2EC4B6', duration:0.05} -50ms][♪swish -4.5dB +250ms]あわせて、[>#b_bd.m[1] -100ms][♪pop -7dB]初回で解決したか、[>#b_bd.m[2] -100ms][♪pop -7dB]解決までの時間、[>#b_bd.m[3] -100ms][♪pop -7dB][>#b_bd.note +500ms]対応時間を突き合わせました。[silence:0.20s]

*** c
@n: [silence:0.3s][step #hdr.d[2] #hdr.d[1] -50ms][!#hdr.lbl text,"02 / 09" -50ms][♪swish -4dB +250ms]件数は3か月で[>#c_pct -200ms][♪chime -4.5dB][>#c_ft +350ms]12%増。[>#c_call -100ms][♪pop -8dB][>#c_bd.note +600ms]利用企業の増加と、ほぼ同じ伸びです。[silence:0.20s]

*** d
@n: [silence:0.3s][step #hdr.d[3] #hdr.d[2] -50ms][!#hdr.lbl text,"03 / 09" -50ms][♪swish -4dB +250ms]内訳で多いのは、[>#d_bd.r[1].hl -50ms][!#d_bd.r[3] to,{opacity:0.5, duration:0.5}][!#d_bd.r[4] to,{opacity:0.5, duration:0.5}][!#d_bd.r[5] to,{opacity:0.5, duration:0.5}][!#d_bd.r[6] to,{opacity:0.5, duration:0.5}][!#d_bd.r[7] to,{opacity:0.5, duration:0.5}][♪click -4dB]ログイン・アカウントの22%と、[>#d_bd.r[2].hl -50ms][♪click -4dB][>#d_bd.leg +500ms]操作方法の21%です。[silence:0.45s]

*** e
@n: [silence:0.3s][step #hdr.d[4] #hdr.d[3] -50ms][!#hdr.lbl text,"04 / 09" -50ms][♪swish -4.5dB +250ms]初回で解決した割合は全体で[>#e_g -750ms][>#e_bd.avg][>#e_bd.al][♪chime -4.5dB][>#e_cap +500ms]59%。ログインの[>#e_bd.r[1].hl -50ms][♪click -4.5dB]81%に対し、データ連携は[>#e_bd.r[6].hl -50ms][!#e_bd.r[2] to,{opacity:0.5, duration:0.5} -50ms][!#e_bd.r[3] to,{opacity:0.5, duration:0.5} -50ms][!#e_bd.r[4] to,{opacity:0.5, duration:0.5} -50ms][!#e_bd.r[5] to,{opacity:0.5, duration:0.5} -50ms][♪click -4.5dB]34%、不具合の報告は[>#e_bd.r[7].hl -50ms][♪click -4.5dB][>#e_bd.note +600ms]22%です。[silence:0.20s]

*** f
@n: [silence:0.3s][step #hdr.d[5] #hdr.d[4] -50ms][!#hdr.lbl text,"05 / 09" -50ms][♪swish -4.5dB +250ms]解決までの時間の[>#f_bd.pin -50ms][♪pop -7dB][>#f_bd.lead +150ms][>#f_bd.ldot +150ms]中央値は、1時間50分。ただ、[>#f_sd -350ms][>#f_bd.brt -100ms][>#f_bd.labt][♪chime_low -1.5dB]3日を超える長い尾が[>#f_sd.st1 -250ms][>#f_sd.split][!#f_bd.hi[*] to,{opacity:0.3, duration:0.4, repeat:1, yoyo:true}]372件あり、その[>#f_sd.st2 -350ms][>#f_sd.split.a -200ms][♪chime -5dB][>#f_sd.lsw[*] +400ms][>#f_sd.lt[*] +400ms]78%がデータ連携と不具合の報告です。[silence:0.25s]

*** g
@n: [silence:0.3s][step #hdr.d[6] #hdr.d[5] -50ms][!#hdr.lbl text,"06 / 09" -50ms][♪swish -4.5dB +250ms]ところが[>#g_cmp.st[*]]対応時間で見ると、景色が変わります。[>#g_top -300ms][>#g_cmp.rib -100ms][>#g_cmp.rib2 -100ms][>#g_cmp.ribl -100ms][!#g_cmp.sc[4] to,{opacity:0.35, duration:0.5}][!#g_cmp.sc[5] to,{opacity:0.35, duration:0.5}][!#g_cmp.sc[6] to,{opacity:0.35, duration:0.5}][!#g_cmp.sc[7] to,{opacity:0.35, duration:0.5}][!#g_cmp.st[4] to,{opacity:0.35, duration:0.5}][!#g_cmp.st[5] to,{opacity:0.35, duration:0.5}][>#g_top.r[1] +100ms][>#g_top.r[1].bar +200ms][>#g_top.r[2] +320ms][>#g_top.r[2].bar +420ms][>#g_top.r[3] +540ms][>#g_top.r[3].bar +640ms][>#g_top.dv +1000ms][>#g_top.r[4] +1150ms][>#g_top.r[4].bar +1150ms]データ連携、不具合、請求の3つは、件数では[>#g_cmp.g43 -150ms][♪chime -4.5dB]43%なのに、対応時間では[>#g_cmp.g75 -150ms][♪chime_low][>#g_top.sum +500ms]75%を占めています。[silence:0.35s]

*** h
@n: [silence:0.3s][step #hdr.d[7] #hdr.d[6] -50ms][!#hdr.lbl text,"07 / 09" -50ms][♪swish -4.5dB +250ms]一方、[>#h_bd.rh[1] -200ms][>#h_bd.rh[1].rd +50ms][♪pop -8dB]操作方法の355件と、[>#h_bd.rh[2] -200ms][>#h_bd.tag -200ms][>#h_bd.rh[2].rd +50ms][♪pop -8dB]ログインの300件は、ヘルプページで答えられる内容でした。合わせて[>#h_bd.tot -250ms][♪chime -4.5dB]655件、約[>#h_bd.tot.hrs -250ms][♪pop -8dB][>#h_bd.note +700ms]247時間分です。[silence:0.20s]

*** i
@n: [silence:0.3s][step #hdr.d[8] #hdr.d[7] -50ms][!#hdr.lbl text,"08 / 09" -50ms][♪swish -4.5dB +250ms]次の四半期は、件数[>#i_c1 -450ms][>#i_c1.b1 -100ms][>#i_c1.b2 +80ms][♪pop -6.5dB]3,600件以下、初回解決率[>#i_c2 -450ms][>#i_c2.b1 -100ms][>#i_c2.b2 +80ms][♪pop -6.5dB]65%、3日を超える案件[>#i_c3 -450ms][>#i_c3.b1 -100ms][>#i_c3.b2 +80ms][♪pop -6.5dB]250件以下を目指します。[silence:0.25s]

*** j
@n: [silence:0.3s][step #hdr.d[9] #hdr.d[8] -50ms][!#hdr.lbl text,"09 / 09" -50ms]件数の[>#j_i1 -250ms][♪chime_warm -4.5dB to=1.1s]43%が、時間の75%。[>#j_i2 -250ms][♪chime_warm -4.5dB to=1.1s]ヘルプページで浮いた時間を上位3カテゴリに回し、[>#j_i3 -250ms][♪chime_warm -4.5dB to=1.1s]長い尾には、開発への引き継ぎ手順を決める。それが[!#j_i3 glow,#E8615A73 {blur: 31} -100ms][♪shimmer -1.5dB to=1.8s][<#j_i1 +150ms][<#j_i2 +150ms][<#j_i3 +150ms][<#j_h +150ms][!#j_shade to,{opacity:0.42, duration:1, ease:'power2.inOut'} +350ms][>#j_ek +600ms][>#j_et +700ms][>#j_es +950ms]次の一手です。[silence:2.6s]
fade out,900ms
```

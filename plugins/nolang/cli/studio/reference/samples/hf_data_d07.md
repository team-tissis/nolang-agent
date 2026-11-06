# data · kakeibo-interviews (hf 全力版の全量の写し — 家計簿アプリをやめた 12 人に聞いた・明るい付箋と手書きの線で組む定性調査の報告 9 場面 (人数の四角・折れ線・型の札・比べる点と棒・ジャーニーの波・機会の札・結論の帯)) — canvas 1920x1080

見せる作り: 全編 1 枚の方眼の紙と 2 場面目からの常設の上端 (マスキングテープの題・章の 7 札の上を黄の付箋が滑る)・3 場面目からの脚注・場面の骨組みの def (紺の丸の番号 + 手書きの題 + 下に伸びる黄のマーカー + 補足)・叩きつけて出る色の付箋の def (光沢・めくれの角・傾き)・数字の語で描く手書きの図 (数字を囲む赤い丸・矢印・中括弧・稲妻・チェック・打ち消し線と下線)・降り積もる 1 人 = 1 枚の四角・左から描く折れ線と面・語で浮く型の札と 12 マスの塗り替え・1 点 = 1 人の点と棒の比較・波のジャーニー・ラフの図つきの機会の札・場面は左へ抜け次の場面が右から滑り込む切替・音の層 (BGM + 紙・付箋・ペンの効果音を場面の頭と数字の語に)

```design.txt
#v2
# 学ぶ作り: 全編 1 枚の方眼の紙と周辺の焼け・2 場面目から常設の上端 (マスキングテープの題 + 章の 7 札と黄の付箋が滑る)・3 場面目から常設の脚注
# 場面 = 番号の丸 + 手書きの見出し (黄のマーカーが下に伸びる) + 付箋の板。付箋は def (色・めくれの角・傾き・叩きつける入場) で揃え、中身は数字の語で出す
# 図は手書きの線で描く: 数字を囲む赤い丸 (circle_hand を draw)・矢印と波の道 (path を draw)・中括弧・稲妻・チェック・打ち消し線と下線
# hf d07 kakeibo-interviews (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面は左へ抜けて (section の out)、次の場面が右から滑り込む (slide)
canvas 1920x1080 bg=#FBF7EE
theme light
palette ink=#24304A ink2=#4F5A73 red=#D93F45 pen=#2A63C9 yel=#FFE66B blu=#A9D7FF pnk=#FFB7D0 lav=#D6C6FF mnt=#A6EBC6 cor=#FFB59C org=#FFC978 wht=#FFFDF7 later=#FFF0A8 mnt_ink=#1F8D62 cor_ink=#DF5F43 dred=#B4232A tape=#E9DBB2 empty=#ECE5D3 over=#FF8F8F
font "鉛筆で丁寧に書いたような、やや太めの教科書体風の手書きの日本語書体"
fonts m="丸みのあるマーカーで書いたような、太く親しみやすい手書き風の日本語書体、数字もくっきり"
fonts h="細いペンでさらさらと書いたような、やわらかい手書きの日本語書体"
art "やわらかい黒の手描きの主線、明るいパステルのフラットな塗りにごく軽い陰影、白地に切り抜いたステッカー風のイラスト、人物は日本の 20〜30 代"
prompt_tail "文字・数字・ロゴは入れない"
sfx off
# hf の作り: 注記・凡例・章の札・内訳は 12〜15 px (hf の 18〜23 px の 2/3)・数字も見出しと同じ手書きの書体
# hf の作り: 見出し・列の題・付箋の題は台詞より先に出る・発言と結論の補足は札ごと出る (spoiler)・図だけの場面は絵が無い (text_only_cut)
# hf の作り: 結論の絵は締めの 19 秒そのまま (same_picture)・場面の頭と数字の語ごとに紙・付箋・ペンの音を重ねる (se_dense)
# hf の作り: 機会の札は 3 枚を先に並べ、題と中身は文の頭で 1 枚ずつ (empty_board)・場面の終わり際に丸・下線・凡例・最後の発言を出す (entrance_in_fadeout・flash_text)
lint off=small_text,script_font_digits,spoiler,text_only_cut,same_picture,se_dense,empty_board,entrance_in_fadeout,flash_text
run hl { marker: #FFD633BF,42% }
run dr { color: $dred }
run cu { font-size: 0.57em }
run ku { font-size: 0.56em }
run nu { font-size: 0.43em }
run sm { font-size: 22px; color: $ink2 }
run x2 { color: $ink2 }
run cn { font-family: m; color: $ink }
# 場面の退場 (左へ 93 px 抜けて消える・hf の leave): def の根と群は section の out を継がないので根に付ける
motion leave { out: {x:-140, opacity:0, duration:0.36, ease:'power2.in'} }
sound page = "紙のページをめくる軽い音"
sound swish = "短く柔らかい風切りのシュッという音"
sound tape = "マスキングテープを引き出して貼る音"
sound note = "付箋を紙にペタッと貼る軽い音"
sound pop = "木琴のポンという明るく短い音"
sound marker = "フェルトペンでキュッと線を引く音"
sound ding = "グロッケンの澄んだキラッという短い音"
sound blip = "やわらかく短い電子のピッという合図の音"
sound peta = "シールをペタッと貼る音"
sound check = "鉛筆でチェックを付けるシュッという音"
p { color: $ink }
div { in: none }
bgm#music 明るく前向きで軽やかなアコースティックの曲、ギターと木琴と軽い手拍子、穏やかなテンポで主旋律は控えめ、調査報告の解説の下地

# 付箋 (色の地 + 上の光沢 + 右下のめくれ + 柔らかい落ち影)・叩きつけて出る (上から・大きめ・傾けて・back で着地)
def note(c) = div(out: leave; border-radius: 3px 3px 18px 3px; background: {c}; box-shadow: 0px 14px 18px #503C1440; in: {y:-46, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 3px 3px 18px 3px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 46px; height: 46px; border-radius: 0px 0px 18px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
# 白いカード (グラフの板・凡例)
def card = div(out: leave; border-radius: 8px; background: $wht; box-shadow: 0px 12px 18px #503C1430; in: {y:-20, scale:1.03, rotation:-2, opacity:0, duration:.55, ease:'back.out(1.6)'})
# マスキングテープ (付箋の上端からはみ出して貼る — hf の作り: child_overflow)
def tape = div(width: 150px; height: 40px; background: #E9DBB2DB; box-shadow: 0px 2px 3px #00000014)
# 場面の見出し: 紺の丸の番号 (弾む) + 手書きの題 (左から拭き出し・下に黄のマーカーが伸びる) + 補足
def btitle(n, t, s="") = div(out: leave; left: 90px; top: 102px; width: 1650px; height: 84px)
  div#c(left: 0px; cy: 50%; width: 70px; height: 70px; border-radius: 148px; background: $ink; delay: 280ms; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)'})
    p#n(cx: 50%; cy: 50%; font-size: 34px; font-family: m; color: #FFFFFF; content: {n})
  p#t(left: 93px; cy: 50%; font-size: 66px; font-family: m; line-height: 1; white-space: nowrap; delay: 340ms; in: wipe {dir: 'right', duration: 0.55}; content: "{hl}{t}{/}")
  p#s(left: .t.right+28; top: 39px; font-size: 28px; color: $ink2; white-space: nowrap; delay: 750ms; in: {y:12, opacity:0, duration:.45, ease:'power3.out'}; content: {s})
# 赤い手書きの丸 (数字を囲む)
def loop(d=.55) = shape(path: circle_hand; background: none; border: 8px solid $red; in: draw {duration: {d}})
# 1〜12 人の札 (付箋の小さな四角)
def sq(c) = div(out: leave; width: 92px; height: 92px; border-radius: 2px 2px 10px 2px; background: {c}; box-shadow: 0px 6px 8px #503C1440)
# 比べる値 (大きな値 + 下に小さな割合)
def cval(v, s="") = div(out: leave; width: 225px; height: 90px; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'})
  p#v(left: 0px; top: 0px; font-size: 52px; font-family: m; line-height: 1; white-space: nowrap; content: {v})
  p#s(left: 4px; top: 60px; font-size: 26px; color: $ink2; content: {s})
# 4 つの型の札 (色の付箋 + 絵 + 名 + 人数と割合 + 説明 + 白い付箋の発言)
def pcard(c, img, nm, n, pct, ds, who, q, qr) = div(out: leave; top: 196px; width: 404px; height: 680px; border-radius: 3px 3px 18px 3px; background: {c}; box-shadow: 0px 14px 18px #503C1440; in: {y:-34, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 3px 3px 18px 3px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 46px; height: 46px; border-radius: 0px 0px 18px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
  img#img(left: 20px; top: 14px; width: 364px; height: 218px; object-fit: contain; main: none; content: {img})
  p#nm(left: 0px; top: 246px; width: 404px; font-size: 50px; font-family: m; line-height: 1; text-align: center; content: {nm})
  div#ct(left: 0px; top: 308px; width: 404px; height: 92px; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(2.2)'})
    p#n(left: 82px; top: 0px; font-size: 92px; font-family: m; line-height: 1; content: {n})
    p#u(left: .n.right+2; top: 40px; font-size: 44px; font-family: m; line-height: 1) 人
    p#p(left: .u.right+8; top: 45px; font-size: 34px; color: $ink2; line-height: 1; content: {pct})
  shape#loop(left: 63px; top: 298px; width: 138px; height: 102px; path: circle_hand; background: none; border: 4px solid #D93F45CC; in: draw {duration: 0.5})
  p#ds(left: 26px; top: 416px; width: 352px; font-size: 26px; line-height: 1.38; text-align: center; in: {y:12, opacity:0, duration:.45, ease:'power3.out'}; content: {ds})
  div#qt(left: 14px; top: 495px; width: 376px; height: 176px; border-radius: 3px 3px 18px 3px; background: $wht; box-shadow: 0px 14px 18px #503C1440; transform: rotate({qr}deg); in: {y:-26, scale:1.08, rotation:-6, opacity:0, duration:.5, ease:'back.out(1.6)'})
    p#who(left: 20px; top: 16px; font-size: 20px; color: #FFFFFF; background: $ink; border-radius: 4px; padding: 4px 9px 4px 9px; line-height: 1; content: {who})
    p#q(left: 20px; top: 48px; width: 342px; font-size: 24px; font-family: h; line-height: 1.3; content: {q})
# 離脱の瞬間の札 (白い付箋 + 赤い番号 + 題 + 人数 + 内訳の札 + 理由)
def mcard(b, t, n, brk, why) = div(out: leave; top: 470px; height: 392px; border-radius: 3px 3px 18px 3px; background: $wht; box-shadow: 0px 14px 18px #503C1440; in: {y:-30, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 3px 3px 18px 3px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#bd(left: 26px; top: 24px; width: 58px; height: 58px; border-radius: 148px; background: $red)
    p#t(cx: 50%; cy: 50%; font-size: 32px; font-family: m; color: #FFFFFF; content: {b})
  p#tt(left: 96px; top: 34px; font-size: 34px; font-family: m; line-height: 1.15; white-space: nowrap; content: {t})
  p#nn(left: 28px; top: 112px; font-size: 116px; font-family: m; line-height: 1; color: $red; in: {scale:.3, opacity:0, duration:.42, ease:'back.out(2.4)'}; content: {n})
  p#brk(left: 252px; top: 186px; font-size: 22px; color: $ink2; white-space: nowrap; in: {y:26, opacity:0, duration:.5, ease:'power3.out'}; content: {brk})
  p#why(left: 30px; top: 258px; font-size: 27px; font-family: h; line-height: 1.38; in: {y:26, opacity:0, duration:.5, ease:'power3.out'}; content: {why})
# 機会の札 (色の付箋 + 丸の番号 + 題 + ラフの図 + 箇条 + 由来)
def ocard(c, no, tt, f) = div(out: leave; top: 216px; width: 540px; height: 700px; border-radius: 3px 3px 18px 3px; background: {c}; box-shadow: 0px 14px 18px #503C1440; in: {y:-36, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 3px 3px 18px 3px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 46px; height: 46px; border-radius: 0px 0px 18px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
  div#no(left: 30px; top: 28px; width: 66px; height: 66px; border-radius: 148px; border: 4px solid $ink)
    p#t(cx: 50%; cy: 50%; font-size: 36px; font-family: m; content: {no})
  p#tt(left: 112px; top: 40px; font-size: 46px; font-family: m; line-height: 1.05; white-space: nowrap; in: wipe {dir: 'right', duration: 0.5}; content: {tt})
  p#for(left: 44px; top: 628px; font-size: 22px; color: $ink2; white-space: nowrap; in: {y:8, opacity:0, duration:.45, ease:'power3.out'}; content: {f})
# 箇条の 1 行 (黒い点 + 文)
def li(t) = div(width: 460px; height: 78px; in: {y:12, opacity:0, duration:.5, ease:'power3.out'})
  shape#dot(left: 2px; top: 14px; width: 14px; height: 14px; border-radius: 50%; background: $ink)
  p#t(left: 30px; top: 0px; width: 430px; font-size: 28px; line-height: 1.36; content: {t})
# 結論の帯の付箋 (紺の丸の番号 + 題 (左から拭き出し) + 補足)
def ccard(c, n, h, s) = div(out: leave; left: 96px; width: 1300px; height: 210px; border-radius: 3px 3px 18px 3px; background: {c}; box-shadow: 0px 14px 18px #503C1440; in: {y:-30, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 3px 3px 18px 3px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 46px; height: 46px; border-radius: 0px 0px 18px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
  div#nb(left: 34px; top: 46px; width: 112px; height: 112px; border-radius: 148px; background: $ink)
    p#t(cx: 50%; cy: 50%; font-size: 64px; font-family: m; color: #FFFFFF; content: {n})
  p#h(z-index: front; left: 182px; top: 40px; font-size: 56px; font-family: m; line-height: 1.05; white-space: nowrap; in: wipe {dir: 'right', duration: 0.7}; content: {h})
  p#s(left: 184px; top: 124px; font-size: 30px; color: $ink2; white-space: nowrap; in: {y:10, opacity:0, duration:.5, ease:'power3.out'}; content: {s})

# 全編の地 (根・z back): 方眼の紙 + 周辺の焼け
# hf の作り: 方眼は画面より広く敷き (hf 4200×1160 の 2/3)、場面ごとに左へ 96 px (3 マス) 送る (hf は -150 px × 場面番号 = 100 px・0.9 s power3.inOut) — timeline の各 cut の頭の `[!#grid to,{x:-144×n}]`・根の層は cut を跨いで続くので値は累積の絶対値
# engine: pattern の板 (svg) は resource-service が 1 辺 2048 px まで — 幅 1280 + 8 場面 × 96 = 2048 に収める (100 px × 8 = 2800 px 幅は描けない)
div#grid.bleed(left: 0px; top: -40px; width: 3072px; height: 1160px; pattern: grid,32,#406EAA16; z-index: back)
div#vig(inset: 0; background: radial(#FBF7EE00@55%,#785F3221,50%,45%); z-index: back)

# title — 黄の付箋が叩きつけられ、題を 1 行ずつ拭き出す (12 は赤で弾み、赤い丸で囲む)・右に座り込む人の絵・「ポケットノート」で桃の付箋
section#title(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
img#cover(left: 1150px; top: 168px; width: 700px; height: 466px; object-fit: contain; main: none; delay: 350ms; in: {scale:.92, y:20, opacity:0, duration:.9, ease:'power3.out'}) [transparent]床にあぐらをかいて座る若い人が、スマートフォンをゆるく持ち、退屈そうに小さくため息をついて横を向いている。まわりにくしゃくしゃのレシート、数枚の硬貨、閉じた小さなノートが散らばる。人物と小物を枠いっぱいに収め、余白を作らない
note#t_note(left: 130px; top: 190px; width: 1010px; height: 650px; c: $yel; transform: rotate(-2deg); delay: 80ms; in: {y:-70, scale:1.14, rotation:-8, opacity:0, duration:.6, ease:'back.out(1.6)'})
  tape#tp(left: 420px; top: -20px; transform: rotate(2deg))
  p#kick(left: 78px; top: 64px; font-size: 34px; color: $ink2; letter-spacing: .06em; line-height: 1; delay: 320ms; in: {y:10, opacity:0, duration:.5, ease:'power3.out'}) 定性調査レポート ｜ ユーザーインタビュー
  p#l1(left: 78px; top: 140px; font-size: 112px; font-family: m; line-height: 1; white-space: nowrap; delay: 370ms; in: wipe {dir: 'right', duration: 0.5}) 家計簿アプリを
  p#l2a(left: 78px; top: 333px; font-size: 112px; font-family: m; line-height: 1; delay: 620ms; in: wipe {dir: 'right', duration: 0.3}) やめた
  p#n12(left: 392px; top: 246px; font-size: 212px; font-family: m; line-height: 1; letter-spacing: -.02em; color: $red; delay: 770ms; in: {scale:.1, opacity:0, duration:.5, ease:'back.out(2.4)'}) 12
  p#l2b(left: 596px; top: 333px; font-size: 112px; font-family: m; line-height: 1; delay: 920ms; in: wipe {dir: 'right', duration: 0.25}) 人に
  p#l3(left: 78px; top: 462px; font-size: 112px; font-family: m; line-height: 1; delay: 1070ms; in: wipe {dir: 'right', duration: 0.3}) 聞いた
  loop#ring(left: 368px; top: 279px; width: 279px; height: 170px; d: .65; delay: 1040ms; overlap: t_note.n12)
  shape#u3(left: 72px; top: 558px; width: 357px; height: 12px; path: line_h; border: 9px solid $red; in: draw {duration: 0.45})
note#t_sub(left: 660px; top: 735px; width: 610px; height: 200px; c: $pnk; transform: rotate(3deg); overlap: t_note; in: {y:-30, scale:1.14, rotation:8, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#a(left: 40px; top: 30px; font-size: 30px; color: $ink2) 架空の家計簿アプリ
  p#b(left: 40px; top: 75px; font-size: 54px; font-family: m; line-height: 1.2) 「ポケットノート」
p#t_team(left: 1290px; top: 958px; font-size: 26px; color: $ink2; in: {y:10, opacity:0, duration:.5, ease:'power3.out'}) アプリデザインチーム 共有用

# method — 上端の常設が降り、青・黄・緑の付箋を語で 1 枚ずつ (214 を数える)・矢印でインタビューの絵へ・「比較」の両矢印・赤い手書きの一文と「型」の丸
section#method(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
# 常設の上端 (sticky・最後まで): マスキングテープの題 + 章の 7 札 (黄の付箋が場面の章へ滑る)
# 題・章の札・脚注は hf の $ink2 だと細い手書きの本文書体で薄く読めるので既定の $ink (文字の縁 stroke は 1 px 未満に絞れず潰れるので使わない)
div#hdr.sticky(left: 0px; top: 0px; width: 1920px; height: 90px; z-index: front; delay: 100ms; in: {opacity:0, duration:.5, ease:'power1.out'})
  p#tag(left: 70px; top: 30px; font-size: 22px; background: #E9DBB2CC; padding: 10px 22px 8px 22px; line-height: 1.3; white-space: nowrap) 定性調査レポート ｜ 家計簿アプリ「ポケットノート」（架空）
  div#hl(left: 1035px; top: 30px; width: 112px; height: 46px; border-radius: 3px 3px 10px 3px; background: $yel; box-shadow: 0px 4px 8px #503C1440)
  p#ch(left: "1035;1154;1271;1389;1508;1625;1743"; top: 30px; width: 112px; height: 46px; font-size: 21px; text-align: center; line-height: 2.2; white-space: nowrap) ×7 {cn}01{/}設計;{cn}02{/}時期;{cn}03{/}型;{cn}04{/}違い;{cn}05{/}瞬間;{cn}06{/}機会;{cn}07{/}結論
btitle#bt1(n: "01"; t: "調査の設計"; s: "誰に、どう聞いたか")
note#m_a(left: 100px; top: 290px; width: 480px; height: 470px; c: $blu; transform: rotate(-2.5deg))
  p#lbl(left: 44px; top: 42px; font-size: 32px; color: $ink2) 声をかけた人
  p#n(left: 44px; top: 94px; font-size: 178px; font-family: m; line-height: 1; in: {opacity:0, duration:.12}) [count:214 start=0 ms=2100ms]
  p#u(left: .n.right+3; top: 183px; font-size: 78px; font-family: m; line-height: 1) 人
  p#d(left: 44px; top: 291px; font-size: 34px; line-height: 1.32) 記録が{dr}30日以上{/}[br]止まった人
shape#m_arrow(path: "M600 530 Q681 533 732 470"; background: none; border: 6px solid $ink; in: draw {duration: 0.35})
shape#m_arrow_h(path: "M731 494 L732 470 L708 476"; background: none; border: 6px solid $ink; in: draw {duration: 0.35})
img#m_img(left: 735px; top: 228px; width: 520px; height: 346px; object-fit: contain; main: none; in: {scale:.9, opacity:0, duration:.6, ease:'power3.out'}) [transparent]小さな丸テーブルで向かい合う 2 人の和やかな 1 対 1 のインタビュー。1 人はクリップボードとペンでメモを取り、もう 1 人は手を開いて話している。テーブルにコーヒーカップが 2 つ、頭上に白紙の付箋が数枚ふわりと浮かぶ。人物とテーブルを枠いっぱいに収め、余白を作らない
note#m_b(left: 770px; top: 650px; width: 470px; height: 258px; c: $yel; transform: rotate(1.8deg); overlap: m_img)
  p#lbl(left: 40px; top: 30px; font-size: 32px; color: $ink2) インタビュー
  p#n12(left: 40px; top: 80px; font-size: 104px; font-family: m; line-height: 1) 12
  p#u1(left: .n12.right+2; top: 123px; font-size: 54px; font-family: m; line-height: 1) 人
  p#x(left: .u1.right+10; top: 124px; font-size: 52px; font-family: m; line-height: 1) ×
  p#n45(left: .x.right+10; top: 90px; font-size: 92px; font-family: m; line-height: 1) 45
  p#u2(left: .n45.right+2; top: 128px; font-size: 50px; font-family: m; line-height: 1) 分
  p#s(left: 40px; top: 195px; font-size: 26px; color: $ink2) P1～P12 に 1人ずつ
note#m_c(left: 1340px; top: 300px; width: 480px; height: 470px; c: $mnt; transform: rotate(2.2deg); in: {y:-46, scale:1.14, rotation:7, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#lbl(left: 46px; top: 42px; font-size: 32px; color: $ink2) 比較のため
  p#t(left: 46px; top: 92px; font-size: 36px; line-height: 1.3) 1年以上[br]続けている人
  p#n(left: 46px; top: 190px; font-size: 180px; font-family: m; line-height: 1) 6
  p#u(left: .n.right+3; top: 286px; font-size: 72px; font-family: m; line-height: 1) 人
  p#s(left: 46px; top: 375px; font-size: 28px; color: $ink2) にも同じ質問をした
# 「比較」の両矢印 (青いペン)
shape#m_cmp_l(path: "M1262 548 Q1299 534 1337 548"; background: none; border: 4px solid #2A63C9E6; in: draw {duration: 0.3})
shape#m_cmp_h1(path: "M1320 552 L1337 548 L1326 533"; background: none; border: 4px solid #2A63C9E6; in: draw {duration: 0.2})
shape#m_cmp_h2(path: "M1272 533 L1262 548 L1280 552"; background: none; border: 4px solid #2A63C9E6; in: draw {duration: 0.2})
p#m_cmp(left: 1262px; top: 478px; font-size: 36px; font-family: h; color: $pen; in: {opacity:0, duration:.35, ease:'power1.out'}) 比較
p#m_note(left: 460px; top: 926px; width: 1000px; font-size: 50px; font-family: h; color: $red; text-align: center; white-space: nowrap; in: wipe {dir: 'right', duration: 1.1}) 数が少ないので、割合より「型」を見る
shape#m_note_u(path: "M530 986 Q960 990 1391 981"; background: none; border: 4px solid #D93F45B3; overlap: m_note; in: draw {duration: 0.6})
loop#m_kata(left: 1094px; top: 915px; width: 183px; height: 72px; border: 6px solid $red; overlap: m_note)

# when — 方眼が送られ、章の付箋が「02」へ・4 列の付箋の四角が列ごとに降り積もる・「中央値」で黄の付箋に 26 を数えて丸・「12人中7人」で中括弧と赤字・「最初の1か月」で橙の列が弾む
section#when(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
# 常設の脚注 (sticky・最後まで)
p#foot.sticky(left: 70px; top: 1028px; font-size: 21px; z-index: front; white-space: nowrap; delay: 300ms; in: {opacity:0, duration:.6, ease:'power1.out'}) ※ n＝12（やめた人）＋6（続けている人）。数が少ないため、割合より「型」を見る調査
btitle#bt2(n: "02"; t: "いつ、やめたか"; s: "最後に記録した日まで（12人）")
sq#c1(left: 204px; top: "803;701"; c: $org; rotation: "-1.8;-0.6"; delay: 550ms; in: {y:-40, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×2
sq#c2(left: 453px; top: "803;701;599;497;395"; c: $org; rotation: "0.6;1.8;-1.2;0;1.2"; delay: 750ms; in: {y:-40, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×5
sq#c3(left: 704px; top: "803;701;599"; c: $later; rotation: "-1.2;0;1.2"; delay: 950ms; in: {y:-40, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×3
sq#c4(left: 954px; top: "803;701"; c: $later; rotation: "1.2;-1.8"; delay: 1150ms; in: {y:-40, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×2
div#w_axis(left: 110px; top: 906px; width: 1020px; height: 4px; background: #24304AD9; delay: 450ms; in: {scaleX:0, duration:.6, ease:'power1.inOut', pivot:'left'})
p#w_col(left: "141;390;641;891"; top: 922px; width: 220px; font-size: 32px; text-align: center; line-height: 1; delay: 550ms; in: {y:10, opacity:0, duration:.35, ease:'power3.out', stagger:{each:.2}}) ×4 1週間以内;1～4週;1～3か月;3か月以上
p#w_cnt1(left: 141px; top: 639px; width: 220px; font-size: 52px; font-family: m; text-align: center; line-height: 1; delay: 770ms; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 2{cu}人{/}
p#w_cnt2(left: 390px; top: 333px; width: 220px; font-size: 52px; font-family: m; text-align: center; line-height: 1; delay: 1150ms; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 5{cu}人{/}
p#w_cnt3(left: 640px; top: 537px; width: 220px; font-size: 52px; font-family: m; text-align: center; line-height: 1; delay: 1230ms; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 3{cu}人{/}
p#w_cnt4(left: 891px; top: 639px; width: 220px; font-size: 52px; font-family: m; text-align: center; line-height: 1; delay: 1370ms; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 2{cu}人{/}
# 凡例 (橙 = 最初の 1 か月・淡い黄 = それ以降)
div#w_leg(left: 120px; top: 974px; width: 720px; height: 30px; delay: 1400ms; in: {opacity:0, duration:.4, ease:'power1.out'})
  div#s1(left: 0px; top: 2px; width: 26px; height: 26px; border-radius: 2px 2px 6px 2px; background: $org)
  p#t1(left: 36px; top: 0px; font-size: 26px; color: $ink2; white-space: nowrap) ＝1人（最初の1か月）
  div#s2(left: 333px; top: 2px; width: 26px; height: 26px; border-radius: 2px 2px 6px 2px; background: $later)
  p#t2(left: 369px; top: 0px; font-size: 26px; color: $ink2; white-space: nowrap) ＝1人（それ以降）
shape#w_brace(path: "M191 333 Q191 311 213 311 L353 311 Q375 311 375 288 Q375 311 398 311 L537 311 Q560 311 560 333"; background: none; border: 6px solid $red; in: draw {duration: 0.55})
p#w_brace_l(left: 150px; top: 206px; width: 560px; font-size: 50px; font-family: m; color: $red; text-align: center; white-space: nowrap; in: {y:14, opacity:0, duration:.45, ease:'back.out(1.8)'}) 12人中 7人が最初の1か月
note#w_med(left: 1234px; top: 300px; width: 590px; height: 520px; c: $yel; transform: rotate(2deg))
  p#lbl(left: 52px; top: 40px; font-size: 32px; color: $ink2) やめるまでの期間
  p#mid(left: 52px; top: 87px; font-size: 30px; color: $ink2) 中央値
  p#n(left: 52px; top: 124px; font-size: 250px; font-family: m; line-height: 1; in: {opacity:0, duration:.12}) [count:26 start=0 ms=900ms]
  loop#ring(left: 9px; top: 153px; width: 363px; height: 220px; overlap: w_med.n)
  p#u(left: .n.right+3; top: 261px; font-size: 96px; font-family: m; line-height: 1) 日

# weekly — 白い板に方眼の軸を描き、「5.8日」から「1.3日」まで折れ線と面を左から描く (点と値が線の到着で弾む)・凡例の板・「2週目」で桃の付箋と赤い丸・「坂」で赤い矢印と斜めの手書き
section#weekly(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt3(n: "02"; t: "記録日数の推移"; s: "やめた人・1週あたりの平均")
card#k_panel(left: 96px; top: 218px; width: 1230px; height: 770px; transform: rotate(-.6deg); delay: 250ms)
  tape#tp(left: 540px; top: -18px; transform: rotate(-2deg))
div#k_g0(left: 240px; top: 879px; width: 1010px; height: 4px; background: $ink; delay: 450ms; in: {scaleX:0, duration:.5, ease:'power1.inOut', pivot:'left'})
div#k_gl(left: 240px; top: "800;720;639;560;480;399;320"; width: 1010px; height: 2px; background: #24304A2E; delay: 480ms; in: {scaleX:0, duration:.5, ease:'power1.inOut', pivot:'left', stagger:{each:.03}}) ×7
div#k_ya(left: 238px; top: 300px; width: 4px; height: 582px; background: $ink; delay: 450ms; in: {scaleY:0, duration:.5, ease:'power1.inOut', pivot:'bottom'})
p#k_ay(left: 150px; top: "867;788;708;627;548;468;387;308"; width: 70px; font-size: 24px; color: $ink2; text-align: right; line-height: 1; delay: 550ms; in: {opacity:0, duration:.3, ease:'power1.out'}) ×8 0;1;2;3;4;5;6;7日
p#k_ax(left: "251;521;791;1061"; top: 900px; width: 160px; font-size: 30px; text-align: center; line-height: 1; delay: 600ms; in: {y:8, opacity:0, duration:.3, ease:'power3.out', stagger:{each:.08}}) ×4 1週目;2週目;3週目;4週目
shape#k_area(path: "M330 417 L600 552 L870 672 L1140 777 L1140 881 L330 881 Z"; background: #DF5F4324; in: wipe {dir: 'right', duration: 1.27, ease: 'none'})
shape#k_line(path: "M330 417 L600 552 L870 672 L1140 777"; background: none; border: 8px solid $cor_ink; in: draw {duration: 1.27, ease: 'none'})
shape#k_pt(left: "315;585;855;1125"; top: "402;537;657;762"; width: 30px; height: 30px; border-radius: 50%; background: $cor_ink; border: 4px solid #FFFFFF; box-shadow: 0px 2px 6px #00000040; in: {scale:.1, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.42}}) ×4
p#k_val(left: "290;612;882;1152"; top: "335;470;590;695"; font-size: 54px; font-family: m; line-height: 1; white-space: nowrap; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.42}}) ×4 5.8{ku}日{/};4.1{ku}日{/};2.6{ku}日{/};1.3{ku}日{/}
card#k_legend(left: 1380px; top: 250px; width: 450px; height: 220px; transform: rotate(1deg); delay: 900ms; in: {y:-16, scale:1.04, rotation:3, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sw(left: 30px; top: 39px; width: 60px; height: 8px; border-radius: 4px; background: $cor_ink)
  shape#dot(left: 50px; top: 32px; width: 22px; height: 22px; border-radius: 50%; background: $cor_ink; border: 4px solid #FFFFFF)
  p#t(left: 108px; top: 26px; font-size: 27px; white-space: nowrap) やめた人12人の平均
  p#n(left: 30px; top: 78px; font-size: 22px; line-height: 1.4; color: $ink2) 1週あたりの記録日数[br]（ログと本人の話を突き合わせた値）
note#k_take(left: 1395px; top: 544px; width: 440px; height: 360px; c: $pnk; transform: rotate(-2deg); in: {y:-46, scale:1.14, rotation:-8, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(left: 40px; top: 40px; font-size: 62px; font-family: m; line-height: 1.15) 2週目から[br]坂を[br]下り始める
loop#k_loop(left: 556px; top: 512px; width: 87px; height: 80px; d: .45; border: 6px solid $red; overlap: k_val)
shape#k_arrow(path: "M630 614 Q879 705 1110 834"; background: none; border: 6px solid $red; overlap: k_val; in: draw {duration: 0.55})
shape#k_arrow_h(path: "M1088 837 L1110 834 L1101 813"; background: none; border: 6px solid $red; in: draw {duration: 0.2})
p#k_slope(left: 640px; top: 700px; font-size: 40px; font-family: h; color: $red; white-space: nowrap; transform: rotate(21deg); transform-origin: 0% 0%; in: {opacity:0, duration:.4, ease:'power1.out'}) 2週目から下り坂

# patterns — 4 色の付箋の札が並び、型の名の語で札が浮き、人数の語で数と赤い丸・発言の白い付箋・下の 12 マスを型の色に塗る
section#patterns(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt4(n: "03"; t: "4つの離脱パターン"; s: "12人の「やめ方」の型")
pcard#pc1(left: 92px; c: $yel; transform: rotate(-1.2deg); nm: "入力疲れ"; n: "5"; pct: "（42%）"; ds: "レシートや現金の支出を[br]毎回打ち込むのが続かない"; who: "P3"; q: "「夜まとめて入れようとし[br]て、思い出せない支出が3つ[br]あった時点で嫌になった」"; qr: 1.4; img: "[transparent]夜遅く机のライトの下で、片手にスマートフォン、もう片手に長く丸まった紙のレシートを持ち、半目で眠そうな人。机にくしゃくしゃのレシートの山、そばに小さな三日月。人物を枠いっぱいに収め、余白を作らない")
pcard#pc2(left: 536px; c: $blu; transform: rotate(.8deg); nm: "分類迷子"; n: "3"; pct: "（25%）"; ds: "初期設定24個のカテゴリの[br]どれに入れるか迷う"; who: "P6"; q: "「コンビニのお弁当とお茶、食費？日用品？で毎回止まる」"; qr: -1.2; img: "[transparent]片手にコンビニの弁当、もう片手に緑茶のペットボトルを持ち、開いた空の段ボール箱 2 つの間で首をかしげる人。頭の上に疑問符が 3 つ浮かぶ。人物と箱を枠いっぱいに収め、余白を作らない")
pcard#pc3(left: 980px; c: $pnk; transform: rotate(-.6deg); nm: "見て落ち込む"; n: "2"; pct: "（17%）"; ds: "予算超過の[br]赤い表示がつらい"; who: "P9"; q: "「開くたびに怒られている気がして、開かなくなった」"; qr: 1.1; img: "[transparent]肩を落とし、赤く光る警告の三角が出たスマートフォンの画面を見下ろす落ち込んだ人。頭の上に小さな灰色の雨雲。人物を枠いっぱいに収め、余白を作らない")
pcard#pc4(left: 1424px; c: $lav; transform: rotate(1.1deg); nm: "用済み"; n: "2"; pct: "（17%）"; ds: "貯金の目標を達成した[br]家計の形が分かった"; who: "P12"; q: "「3か月つけて、だいたい分かったからもういいかなって」"; qr: -1.3; img: "[transparent]スマートフォンをポケットにしまいながら満足そうに手を振る人。隣に三角の小旗を立てた大きな笑顔の豚の貯金箱、まわりに小さなきらめき。人物と貯金箱を枠いっぱいに収め、余白を作らない")
p#p_lbl(left: 96px; top: 900px; font-size: 28px; line-height: 1; delay: 800ms; in: {opacity:0, duration:.4, ease:'power1.out'}) 12人の内訳
# 12 マス (型ごとの組・灰の地で先に並び、人数の語で型の色に塗って弾む)
div#pba(left: "290;345;402;458;513"; top: 888px; width: 50px; height: 50px; border-radius: 4px; background: $empty; delay: 800ms; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×5
div#pbb(left: "570;626;681"; top: 888px; width: 50px; height: 50px; border-radius: 4px; background: $empty; delay: 1000ms; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×3
div#pbc(left: "738;794"; top: 888px; width: 50px; height: 50px; border-radius: 4px; background: $empty; delay: 1120ms; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×2
div#pbd(left: "849;906"; top: 888px; width: 50px; height: 50px; border-radius: 4px; background: $empty; delay: 1200ms; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×2
div#p_leg(left: 1000px; top: 898px; width: 750px; height: 30px; in: {opacity:0, duration:.5, ease:'power1.out'})
  div#s(left: "0;182;363;596"; top: 2px; width: 24px; height: 24px; border-radius: 2px 2px 6px 2px; background: "$yel;$blu;$pnk;$lav") ×4
  p#t(left: "32;213;395;627"; top: 0px; font-size: 26px; white-space: nowrap) ×4 入力疲れ 5;分類迷子 3;見て落ち込む 2;用済み 2

# compare — 2 列の見出しの付箋・行の題を語で・続けている人 (緑) とやめた人 (珊瑚) を点・棒・値で比べる・最後に緑の付箋の発言 (「全部正確に」を赤で消し、「だいたい…」に緑の下線)
section#compare(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt5(n: "04"; t: "続けている人と、何が違う？")
note#c_h1(left: 700px; top: 212px; width: 500px; height: 58px; c: $mnt; transform: rotate(-1deg); in: {y:-24, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(cx: 50%; cy: 50%; font-size: 36px; font-family: m; white-space: nowrap) 続けている人（6人）
note#c_h2(left: 1262px; top: 212px; width: 540px; height: 58px; c: $cor; transform: rotate(1deg); in: {y:-24, scale:1.14, rotation:6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(cx: 50%; cy: 50%; font-size: 36px; font-family: m; white-space: nowrap) やめた人（12人）
div#c_sep(left: 96px; top: "432;581;728"; width: 1730px; height: 2px; background: #24304A40; delay: 600ms; in: {scaleX:0, duration:.6, ease:'power1.inOut', pivot:'left', stagger:{each:.08}}) ×3
p#c_l1(left: 96px; top: 320px; font-size: 33px; line-height: 1.25; in: {y:10, opacity:0, duration:.5, ease:'power3.out'}) 銀行・カードの自動連携を使う
p#c_l2(left: 96px; top: 468px; font-size: 33px; line-height: 1.25; in: {y:10, opacity:0, duration:.5, ease:'power3.out'}) 実際に使うカテゴリの数[br]{sm}中央値{/}
p#c_l3(left: 96px; top: 616px; font-size: 33px; line-height: 1.25; in: {y:10, opacity:0, duration:.5, ease:'power3.out'}) 1日の入力にかける時間[br]{sm}本人の申告・中央値{/}
p#c_l4(left: 96px; top: 764px; font-size: 33px; line-height: 1.25; in: {y:10, opacity:0, duration:.5, ease:'power3.out'}) 週に1回ふり返る習慣
# 1 点 = 1 人 (塗り = 該当・輪 = 非該当)
shape#c_d1(left: "720;773;824;876;929;980"; top: 333px; width: 42px; height: 42px; border-radius: 50%; background: "$mnt_ink;$mnt_ink;$mnt_ink;$mnt_ink;$mnt_ink;none"; border: 4px solid $mnt_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.05}}) ×6
cval#c_v1(left: 1050px; top: 315px; v: "5/6人"; s: "83%")
shape#c_q1(left: "1283;1325;1367;1409;1451;1493;1283;1325;1367;1409;1451;1493"; top: "309;309;309;309;309;309;353;353;353;353;353;353"; width: 34px; height: 34px; border-radius: 50%; background: "$cor_ink;$cor_ink;$cor_ink;none;none;none;none;none;none;none;none;none"; border: 4px solid $cor_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.035}}) ×12
cval#c_w1(left: 1552px; top: 315px; v: "3/12人"; s: "25%")
div#c_b2a(left: 720px; top: 484px; width: 160px; height: 44px; border-radius: 4px 10px 10px 4px; background: $mnt; in: {scaleX:0, duration:.45, ease:'power2.out', pivot:'left'})
p#c_v2a(left: 898px; top: 480px; font-size: 52px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 8{cu}個{/}
div#c_b2b(left: 1282px; top: 484px; width: 380px; height: 44px; border-radius: 4px 10px 10px 4px; background: $cor; in: {scaleX:0, duration:.6, ease:'power2.out', pivot:'left'})
p#c_v2b(left: 1680px; top: 480px; font-size: 52px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 19{cu}個{/}
div#c_b3a(left: 720px; top: 633px; width: 80px; height: 44px; border-radius: 4px 10px 10px 4px; background: $mnt; in: {scaleX:0, duration:.35, ease:'power2.out', pivot:'left'})
p#c_v3a(left: 818px; top: 628px; font-size: 52px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 1{cu}分{/}
div#c_b3b(left: 1282px; top: 633px; width: 320px; height: 44px; border-radius: 4px 10px 10px 4px; background: $cor; in: {scaleX:0, duration:.5, ease:'power2.out', pivot:'left'})
p#c_v3b(left: 1620px; top: 628px; font-size: 52px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 4{cu}分{/}
shape#c_d4(left: "720;773;824;876;929;980"; top: 777px; width: 42px; height: 42px; border-radius: 50%; background: $mnt_ink; border: 4px solid $mnt_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.05}}) ×6
cval#c_v4(left: 1050px; top: 774px; v: "6/6人")
shape#c_q4(left: "1283;1325;1367;1409;1451;1493;1283;1325;1367;1409;1451;1493"; top: "753;753;753;753;753;753;797;797;797;797;797;797"; width: 34px; height: 34px; border-radius: 50%; background: "$cor_ink;$cor_ink;none;none;none;none;none;none;none;none;none;none"; border: 4px solid $cor_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.035}}) ×12
cval#c_w4(left: 1552px; top: 774px; v: "2/12人")
note#c_quote(left: 360px; top: 866px; width: 1200px; height: 138px; c: $mnt; transform: rotate(-1deg); in: {y:-30, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#w(left: 46px; top: 86px; font-size: 26px; color: $ink2; white-space: nowrap) ― 続けている人 6人中5人がこう話した
  shape#x(left: 52px; top: 44px; width: 303px; height: 9px; path: line_h; border: 6px solid $red; in: draw {duration: 0.4})
  p#q(left: 46px; top: 24px; font-size: 45px; font-family: h; line-height: 1; white-space: nowrap) {x2}「全部正確に」{/}より 「だいたい合っていればいい」
  shape#u(left: 478px; top: 74px; width: 556px; height: 9px; path: line_h; border: 8px solid #1F8D62D9; in: draw {duration: 0.8})

# moments — 波のジャーニーの線を左から描いて段階の札・「3日以上」「初めて」で谷に赤い丸と稲妻 + 白い付箋 (人数・内訳の四角・理由)・「11人」で橙の付箋
section#moments(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt6(n: "05"; t: "離脱が起きる2つの瞬間"; s: "ジャーニーのどこでやめたか")
shape#j_path(path: "M120 330 C260 300 380 296 521 318 C650 338 720 420 821 432 C920 444 980 330 1100 318 C1241 306 1361 440 1460 449 C1560 456 1620 341 1800 312"; background: none; border: 8px solid #24304AE6; delay: 500ms; in: draw {duration: 1.4})
shape#j_head(path: "M1775 290 L1806 312 L1772 335"; background: none; border: 8px solid $ink; delay: 1850ms; in: draw {duration: 0.2})
p#j_lab(left: "50;330;590;960;1610"; top: 236px; width: 220px; font-size: 26px; color: $ink2; text-align: center; white-space: nowrap; delay: 600ms; in: {y:8, opacity:0, duration:.35, ease:'power2.out', stagger:{each:.18}}) ×5 記録をはじめる;毎日つける;記録がたまる;月末・予算;目標を達成
loop#j_loop1(left: 750px; top: 374px; width: 141px; height: 117px; d: .45; border: 9px solid $red)
# hf の boltD (32x70 @1920 = 21x47) を canvas px の素の path で (名の bolt は縦横比を保って枠の幅に縮み半分の大きさになる)
shape#j_bolt1(path: "M859.9 338.0 L843.9 376.0 L858.0 376.0 L849.9 408.0 L876.0 366.0 L861.9 366.0 L870.0 338.0 Z"; background: #FFD633F2; border: 4px solid $red; in: draw {duration: 0.35})
loop#j_loop2(left: 1389px; top: 390px; width: 141px; height: 117px; d: .45; border: 9px solid $red)
shape#j_bolt2(path: "M1500.0 354.0 L1483.9 392.1 L1498.1 392.1 L1489.9 424.0 L1516.1 382.0 L1501.9 382.0 L1510.1 354.0 Z"; background: #FFD633F2; border: 4px solid $red; in: draw {duration: 0.35})
mcard#mc1(left: 520px; width: 610px; transform: rotate(-.8deg); b: "1"; t: "記録を3日以上ためた後の再開"; n: "7{nu}人{/}"; brk: "入力疲れ5・分類迷子2"; why: "たまった分を思い出せず、[br]「抜けがある家計簿」に戻る気がしなくなる")
  div#chips(left: "251;296;341;386;431;476;521"; top: 132px; width: 38px; height: 38px; border-radius: 2px 2px 8px 2px; background: "$yel;$yel;$yel;$yel;$yel;$blu;$blu"; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.06}}) ×7
mcard#mc2(left: 1170px; width: 640px; transform: rotate(.9deg); b: "2"; t: "初めて予算を超えた月の通知"; n: "4{nu}人{/}"; brk: "見て落ち込む2・分類迷子1・用済み1"; why: "「開くたびに怒られている気がして、[br]開かなくなった」（見て落ち込む）"; in: {y:-30, scale:1.14, rotation:6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#chips(left: "251;296;341;386"; top: 132px; width: 38px; height: 38px; border-radius: 2px 2px 8px 2px; background: "$pnk;$pnk;$blu;$lav"; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.06}}) ×4
  p#why(left: 78px)
  p#who(left: 30px; top: 262px; font-size: 18px; color: #FFFFFF; background: $ink; border-radius: 4px; padding: 4px 8px 3px 8px; line-height: 1; in: {y:26, opacity:0, duration:.5, ease:'power3.out'}) P9
note#j11(left: 92px; top: 486px; width: 384px; height: 360px; c: $org; transform: rotate(-2deg); in: {y:-46, scale:1.14, rotation:-9, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#a(left: 36px; top: 34px; font-size: 34px) 12人のうち
  p#n(left: 36px; top: 87px; font-size: 150px; font-family: m; line-height: 1; color: $red) 11{nu}人{/}
  p#s(left: 36px; top: 248px; font-size: 30px; line-height: 1.32) が、どちらかの[br]直後にやめた
note#j_rest(left: 1140px; top: 884px; width: 690px; height: 92px; c: $lav; transform: rotate(.6deg); in: {y:-20, scale:1.14, rotation:4, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(left: 30px; top: 24px; font-size: 27px; line-height: 1.25; white-space: nowrap) 残る1人（用済み）は、目標を達成して自然にやめた

# opps — 3 色の付箋の札・札ごとに題を拭き出し、ラフの図 (ためた日のまとめ入力・8 個のカテゴリと提案・超過の帯と調整案)・箇条と由来・「予算超過」で赤い × を引く
section#opps(stagger: {each:0}; out: {x:-140, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt7(n: "06"; t: "3つの機会領域"; s: "2つの瞬間と、迷いをほどく")
ocard#oc1(left: 92px; c: $yel; transform: rotate(-1.4deg); no: "1"; tt: "ためても戻れる"; f: "← 瞬間1：ためた後の再開")
  group#sk(left: 40px; top: 128px; width: 460px; height: 270px; out: leave; in: {y:8, opacity:0, duration:.3, ease:'power2.out', stagger:.08})
    div#phone(left: 150px; top: 10px; width: 184px; height: 252px; border-radius: 26px; border: 4px solid $ink; background: #FFFFFF)
    p#t1(left: 172px; top: 44px; font-size: 22px; white-space: nowrap) 3日分まとめて
    shape#box(left: 172px; top: 88px; width: 140px; height: 46px; path: rect,r=0.17; background: none; border: 3px solid $ink2; dash: 5,4)
    p#t2(left: 184px; top: 100px; font-size: 22px; color: $ink2; white-space: nowrap) だいたい ￥
    div#pill(left: 166px; top: 156px; width: 152px; height: 42px; border-radius: 21px; background: $mnt)
    p#t3(left: 182px; top: 166px; font-size: 20px; white-space: nowrap) 未分類でOK
    shape#day(left: "8;54;101"; top: 64px; width: 40px; height: 40px; path: rect,r=0.15; background: none; border: 3px solid $ink2; dash: 4,3) ×3
    p#dt(left: "8;54;101"; top: 72px; width: 40px; font-size: 20px; color: $ink2; text-align: center; line-height: 1) ×3 月;火;水
    p#t4(left: 14px; top: 118px; font-size: 21px; color: $ink2; white-space: nowrap) 抜けた日
    p#ar(left: 40px; top: 150px; font-size: 40px; font-family: m) →
  li#li1(left: 44px; top: 420px; t: "抜けた日を「だいたいの金額」で[br]まとめて入れられる")
  li#li2(left: 44px; top: 510px; t: "未分類のままでよい")
ocard#oc2(left: 690px; c: $blu; transform: rotate(.9deg); no: "2"; tt: "分類は後で・少なく"; f: "← 分類迷子")
  div#chip(left: "59;165;272;378;59;165;272;378"; top: "150;150;150;150;204;204;204;204"; width: 96px; height: 40px; border-radius: 20px; border: 3px solid $ink; background: #FFFFFF; in: {scale:.3, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.05}}) ×8
  group#sk(left: 40px; top: 128px; width: 460px; height: 270px; out: leave; in: {y:8, opacity:0, duration:.35, ease:'power2.out', stagger:.12})
    p#t1(left: 22px; top: 140px; font-size: 24px; color: $ink2; white-space: nowrap) カテゴリ 8個からスタート
    div#box(left: 100px; top: 182px; width: 340px; height: 70px; border-radius: 16px; border: 3px solid $ink; background: #FFFFFF)
    p#t2(left: 120px; top: 206px; font-size: 22px; white-space: nowrap) {cn}✦{/} アプリから分け方の提案
  li#li1(left: 44px; top: 420px; t: "最初はカテゴリ8個から始める")
  li#li2(left: 44px; top: 471px; t: "分け方はアプリが提案する")
ocard#oc3(left: 1288px; c: $pnk; transform: rotate(-.7deg); no: "3"; tt: "責めない表示"; f: "← 瞬間2：初めての予算超過")
  group#sk(left: 40px; top: 128px; width: 460px; height: 270px; out: leave; in: {y:8, opacity:0, duration:.3, ease:'power2.out', stagger:.08})
    div#track(left: 20px; top: 20px; width: 420px; height: 40px; border-radius: 20px; border: 3px solid $ink; background: #FFFFFF)
    div#fill(left: 22px; top: 22px; width: 340px; height: 34px; border-radius: 16px 0px 0px 16px; background: $org)
    div#over(left: 363px; top: 22px; width: 74px; height: 34px; border-radius: 0px 16px 16px 0px; background: $over)
    p#t1(left: 300px; top: 76px; font-size: 40px; font-family: m; color: $red; white-space: nowrap) 超過！
  group#sk2(left: 40px; top: 128px; width: 460px; height: 270px; out: leave; in: {y:10, opacity:0, duration:.35, ease:'power2.out', stagger:.1})
    div#box(left: 20px; top: 146px; width: 420px; height: 104px; border-radius: 16px; border: 3px solid $ink; background: #FFFFFF)
    p#t1(left: 42px; top: 166px; font-size: 26px; white-space: nowrap) 来月の調整案
    p#t2(left: 42px; top: 206px; font-size: 21px; color: $ink2; white-space: nowrap) ここを少し見直してみませんか？
  li#li1(left: 44px; top: 420px; t: "予算超過を赤字で示すより、[br]来月の調整案として見せる")
shape#o_x1(path: "M1619 467 L1748 426"; background: none; border: 8px solid $red; overlap: oc3,oc3.sk.t1; in: draw {duration: 0.3})
shape#o_x2(path: "M1620 426 L1746 467"; background: none; border: 8px solid $red; overlap: oc3,oc3.sk.t1; in: draw {duration: 0.3})

# concl — 3 枚の帯の付箋を文の頭で 1 枚ずつ (題を拭き出し・要の語に赤い下線)・要の語で右端に赤いチェック・右にチームの絵・最後に桃の付箋の署名
section#concl(stagger: {each:0})
btitle#bt8(n: "07"; t: "結論"; s: "デザインで直すべきところ")
img#e_team(left: 1440px; top: 300px; width: 420px; height: 280px; object-fit: contain; main: none; delay: 500ms; in: {scale:.9, y:16, opacity:0, duration:.8, ease:'power3.out'}) [transparent]壁の前に立つ 3 人の小さなプロダクトデザインチームが、色とりどりの白紙の付箋を貼り、マーカーで付箋の間に矢印を描いている。協力的で楽しげ。人物と付箋を枠いっぱいに収め、余白を作らない
ccard#cs1(top: 222px; c: $org; transform: rotate(-.6deg); n: "1"; h: "やめる人の半分以上は、最初の1か月"; s: "2週目から記録が減り始める（1週目 5.8日 → 4週目 1.3日）")
  shape#u(left: 796px; top: 99px; width: 300px; height: 9px; path: line_h; border: 8px solid #D93F45D9; in: draw {duration: 0.5})
ccard#cs2(top: 462px; c: $yel; transform: rotate(.5deg); n: "2"; h: "離脱の11/12は、2つの瞬間に集まる"; s: "→ 機能より「ためた後の再開」「初めての予算超過」の体験を直す")
  shape#u(left: 626px; top: 99px; width: 255px; height: 9px; path: line_h; border: 8px solid #D93F45D9; in: draw {duration: 0.5})
ccard#cs3(top: 702px; c: $mnt; transform: rotate(-.4deg); n: "3"; h: "続く人は「だいたいでいい」"; s: "正確さを求める設計が、離脱を生んでいる")
  shape#u(left: 404px; top: 99px; width: 500px; height: 9px; path: line_h; border: 8px solid #D93F45D9; in: draw {duration: 0.5})
shape#ck(left: 1308px; top: "293;533;773"; width: 66px; height: 57px; path: check; background: none; border: 9px solid $red; in: draw {duration: 0.35}) ×3
note#e_sign(left: 1446px; top: 640px; width: 410px; height: 230px; c: $pnk; transform: rotate(2deg); in: {y:-46, scale:1.14, rotation:8, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#a(left: 34px; top: 30px; font-size: 26px; line-height: 1.35; color: $ink2) 定性調査レポート[br]家計簿アプリ（架空）
  p#b(left: 34px; top: 110px; font-size: 46px; font-family: m) ポケットノート
```

```timeline.txt
#v2
cast n = "やわらかく落ち着いた明るい若い女性のナレーター、社内のデザインチームに定性調査の結果を丁寧に分かりやすく報告する"
silence head=0ms tail=180ms
# 切替: 旧場面は左へ抜け (section の out)、境目の後に新場面が右から 100 px 滑り込みながら明ける (hf の enterExit)・境目で紙をめくる音
transition = slide {duration: .6, dir: 'left', offset: '8%', opacity: 0, overlap: .6, ease: 'power3.out'} se=page -4dB

# title — 付箋と題は頭に組み上がる・「ポケットノート」で桃の付箋・「12人」で 12 が弾む・「聞きました」で赤い下線
*** title
bgm music
se note -6dB +120ms
se pop -6dB +900ms
se marker -8dB to=0.8s +1150ms
@n: [silence:0.8s][!#t_note to,{y:-4, rotation:-1.5, duration:5, ease:'sine.inOut'}][!#cover to,{y:-12, duration:4.7, ease:'sine.inOut'} +450ms]架空の家計簿アプリ[>#t_sub -200ms][>#t_team +300ms][♪note -6dB -150ms]『ポケットノート』。やめた[!#t_note.n12 punch {scale: 1.12, duration: .32}]12人に、話を[>#t_note.u3 -100ms][♪marker -8dB to=0.8s -100ms]聞きました。[silence:+0.05s]

# method — 語ごとに付箋を叩きつけ、214 を数える・矢印で絵へ・「同じ質問」で両矢印と「比較」・2 文目で赤い一文と下線と「型」の丸
*** method
se swish -10dB
se tape -8dB +300ms
@n: [silence:0.5s][!#grid to,{x:-144, duration:.9, ease:'power3.inOut'} -450ms][>#hdr -400ms][!#bt1.t{hl} marker +120ms][>#m_a -50ms][>#m_a.n +300ms][♪note -6dB -50ms]記録が30日以上止まった[!#m_a.n punch {scale: 1.12, duration: .32} +120ms][♪pop -6dB +50ms]214人に[>#m_arrow][>#m_arrow_h +300ms][♪marker -8dB to=0.8s -50ms]声をかけ、[>#m_img -300ms][>#m_b -200ms][!#m_img to,{y:-8, duration:8.8, ease:'sine.inOut'} +400ms][♪note -6dB -250ms]12人に[!#m_b.n45 punch {scale: 1.12, duration: .32}][♪pop -6dB -50ms]45分ずつインタビュー。[>#m_c -150ms][♪note -6dB -200ms]続けている6人にも、[>#m_cmp_l][>#m_cmp_h1 +200ms][>#m_cmp_h2 +400ms][>#m_cmp +200ms][♪marker -8dB to=0.8s]同じ質問をしました。
@: [!#m_a to,{y:-4, rotation:-2, duration:4, ease:'sine.inOut'} -80ms][!#m_c to,{y:-4, rotation:2.7, duration:4, ease:'sine.inOut'} -80ms][>#m_note][♪marker -8dB to=0.8s]数は少ないので、見るのは[>#m_note_u]割合より『[>#m_kata -50ms][♪ding -6dB]型』です。[silence:+0.02s]

# when — 頭で 4 列の四角が列ごとに降り、人数が弾む・「中央値」で 26 を数え「26日」で丸・「12人中7人」で中括弧・「最初の1か月」で橙の列が跳ねる
*** when
se swish -10dB
se tape -8dB +300ms
se pop -10dB +550ms
se pop -10dB +750ms
se pop -10dB +950ms
se pop -10dB +1150ms
@n: [silence:0.5s][!#grid to,{x:-288, duration:.9, ease:'power3.inOut'} -450ms][!#hdr.hl to,{x:118, duration:.55, ease:'back.inOut'} -400ms][!#bt2.t{hl} marker +120ms]やめた時期の[>#w_med -250ms][>#w_med.n +100ms][!#w_med.n count +100ms][♪note -6dB -250ms]中央値は[>#w_med.ring +150ms][♪ding -6dB +150ms]26日。[>#w_brace -100ms][>#w_brace_l +150ms][♪marker -8dB to=0.8s -100ms]12人中7人が、[!#c1[*] to,{y:-10, duration:.18, yoyo:true, repeat:1, ease:'power2.out'}][!#c2[*] to,{y:-10, duration:.18, yoyo:true, repeat:1, ease:'power2.out'}]最初の1か月でやめています。[silence:+0.15s]

# weekly — 頭で白い板と軸・「5.8日」から線と面を左から描き点と値が順に弾む・「2週目」で桃の付箋と丸・「坂」で矢印と斜めの字
*** weekly
se swish -10dB
se tape -8dB +300ms
se marker -8dB to=0.8s +500ms
@n: [silence:0.5s][!#grid to,{x:-432, duration:.9, ease:'power3.inOut'} -450ms][!#bt3.t{hl} marker +120ms]週あたりの記録日数は、[>#k_area +250ms][>#k_line +250ms][>#k_pt[*] +230ms][>#k_val[*] +280ms][♪pop -6dB -50ms][♪marker -8dB to=0.8s +350ms]5.8日から[♪pop -6dB -50ms]1.3日へ。[>#k_take -200ms][>#k_loop -50ms][♪note -6dB -200ms]2週目から、[>#k_arrow -100ms][>#k_arrow_h +450ms][>#k_slope +250ms][♪marker -8dB to=0.8s]坂を下り始めます。[silence:+0.2s]

# patterns — 「4つ」で札を 4 枚・型の名の語で札が浮き (前の札は戻る)・人数の語で数・赤い丸・発言・12 マスを型の色に
*** patterns
se swish -10dB
se tape -8dB +300ms
@n: [silence:0.5s][!#grid to,{x:-576, duration:.9, ease:'power3.inOut'} -450ms][!#hdr.hl to,{x:236, duration:.55, ease:'back.inOut'} -400ms][!#bt4.t{hl} marker +120ms]やめ方は、[>#pc1 -200ms][>#pc2 -70ms][>#pc3 +60ms][>#pc4 +190ms][♪note -6dB -150ms][♪note -8dB +250ms]4つの型に分かれました。
@: 最も多いのは『[!#pc1 to,{y:-14, scale:1.035, duration:.35, ease:'power2.out'} -250ms][♪blip -8dB]入力疲れ』で[>#pc1.ct -80ms][>#pc1.loop +50ms][>#pc1.ds +250ms][>#pc1.qt +350ms][!#pba[*] fill,$yel {duration: .25} {stagger: {each: .05}}][♪pop -6dB]5人。[♪note -6dB]毎回の打ち込みが続かない。
@: [>#pc2.ds]カテゴリ選びで止まる『[!#pc1 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -300ms][!#pc2 to,{y:-14, scale:1.035, duration:.35, ease:'power2.out'} -250ms][♪blip -8dB]分類迷子』が[>#pc2.ct -80ms][>#pc2.loop +50ms][>#pc2.qt +350ms][!#pbb[*] fill,$blu {duration: .25} {stagger: {each: .05}}][♪pop -6dB]3人。
@: [>#pc3.ds]予算超過の赤い表示がつらい『[!#pc2 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -300ms][!#pc3 to,{y:-14, scale:1.035, duration:.35, ease:'power2.out'} -250ms][♪blip -8dB]見て落ち込む』が[>#pc3.ct -80ms][>#pc3.loop +50ms][>#pc3.qt +350ms][!#pbc[*] fill,$pnk {duration: .25} {stagger: {each: .05}}][♪pop -6dB]2人。
@: [>#pc4.ds]目標を達成した『[!#pc3 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -300ms][!#pc4 to,{y:-14, scale:1.035, duration:.35, ease:'power2.out'} -250ms][♪blip -8dB]用済み』も[>#pc4.ct -80ms][>#pc4.loop +50ms][>#pc4.qt +350ms][!#pbd[*] fill,$lav {duration: .25} {stagger: {each: .05}}][>#p_leg +500ms][!#pc4 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} +700ms][♪pop -6dB]2人です。[silence:+0.25s]

# compare — 「違う」で 2 列の見出し・行の頭で行の題・数の語で点・棒・値・最後の文で発言の付箋と赤い消し線・緑の下線
*** compare
se swish -10dB
se tape -8dB +300ms
@n: [silence:0.5s][!#grid to,{x:-720, duration:.9, ease:'power3.inOut'} -450ms][!#hdr.hl to,{x:354, duration:.55, ease:'back.inOut'} -400ms][!#bt5.t{hl} marker +120ms]続けている6人とは、何が[>#c_h1 -250ms][>#c_h2 -100ms][♪note -6dB -200ms]違うのか。
@: [>#c_l1 -100ms][♪marker -8dB to=0.8s]自動連携を使う人は[>#c_d1[*] -150ms][>#c_v1 +200ms][♪pop -6dB]6人中5人、やめた人は[>#c_q1[*] -150ms][>#c_w1 +250ms][♪pop -6dB]12人中3人。
@: [>#c_l2 -100ms]使うカテゴリは[>#c_b2a -200ms][>#c_v2a +50ms][♪marker -8dB to=0.8s]8個と[>#c_b2b -200ms][>#c_v2b +150ms][♪marker -8dB to=0.8s]19個。[>#c_l3 -150ms]入力時間は、1日[>#c_b3a -200ms][>#c_v3a +50ms][♪marker -8dB to=0.8s]1分と[>#c_b3b -200ms][>#c_v3b +120ms][♪marker -8dB to=0.8s]4分。
@: [>#c_l4 -100ms]週1回のふり返りは、[>#c_d4[*] -150ms][>#c_v4 +200ms][♪pop -6dB]6人全員と、[>#c_q4[*] -150ms][>#c_w4 +250ms][♪pop -6dB]12人中2人。
@: [>#c_quote -100ms][♪note -6dB -100ms]そして続く人の6人中5人が、『[>#c_quote.x -350ms][>#c_quote.u +100ms][♪marker -8dB to=0.8s -350ms]だいたい合っていればいい』と[♪ding -6dB]言います。[silence:+0.3s]

# moments — 頭で波の道を描き段階の札・「3日以上」「初めて」で谷に丸と稲妻と札・人数の語で数と四角と理由・「11人」で橙の付箋
*** moments
se swish -10dB
se tape -8dB +300ms
se marker -8dB to=0.8s +550ms
@n: [silence:0.5s][!#grid to,{x:-864, duration:.9, ease:'power3.inOut'} -450ms][!#hdr.hl to,{x:472, duration:.55, ease:'back.inOut'} -400ms][!#bt6.t{hl} marker +120ms]離脱は、ジャーニーの2つの瞬間に集まっていました。
@: [>#j_loop1 -200ms][>#j_bolt1][>#mc1 -100ms][♪note -6dB -150ms]3日以上ためた後の再開で[>#mc1.nn -100ms][>#mc1.chips[*]][>#mc1.brk +400ms][>#mc1.why +600ms][♪pop -6dB]7人。[>#j_loop2 -200ms][>#j_bolt2][>#mc2 -100ms][♪note -6dB -150ms]初めて予算を超えた月の通知で[>#mc2.nn -100ms][>#mc2.chips[*]][>#mc2.brk +400ms][>#mc2.why +600ms][>#mc2.who +600ms][>#j_rest +850ms][♪pop -6dB][♪peta -6dB +850ms]4人。
@: 12人のうち[>#j11 -350ms][♪note -6dB -300ms][♪ding -6dB +100ms]11人が、このどちらかの直後にやめています。[silence:+0.2s]

# opps — 「3つ」で札を 3 枚・各文の頭で札が浮き題を拭き出してラフの図・箇条・由来・「8個」でカテゴリの札・「予算超過」で赤い ×・「来月」で調整案
*** opps
se swish -10dB
se tape -8dB +300ms
@n: [silence:0.5s][!#grid to,{x:-1008, duration:.9, ease:'power3.inOut'} -450ms][!#hdr.hl to,{x:590, duration:.55, ease:'back.inOut'} -400ms][!#bt7.t{hl} marker +120ms]だから、機会は[>#oc1 -250ms][>#oc2 -100ms][>#oc3 +50ms][♪note -6dB -200ms][♪note -8dB +100ms]3つ。[silence:+0.05s]
@: [!#oc1 to,{y:-12, scale:1.025, duration:.35, ease:'power2.out'} -200ms][>#oc1.tt -50ms][>#oc1.sk +150ms][>#oc1.li1 +900ms][>#oc1.li2 +1250ms][>#oc1.for +1600ms][♪marker -8dB to=0.8s +100ms]ためても戻れる。だいたいの金額でまとめて入れ、未分類でもいい。
@: [!#oc1 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -250ms][!#oc2 to,{y:-12, scale:1.025, duration:.35, ease:'power2.out'} -200ms][>#oc2.tt -50ms][>#oc2.li1 +900ms][>#oc2.li2 +1250ms][>#oc2.for +1600ms][♪marker -8dB to=0.8s +100ms]分類は後で、少なく。最初は[>#oc2.chip[*] -150ms][>#oc2.sk +300ms][♪pop -6dB]8個、分け方はアプリが[♪blip -8dB]提案。
@: [!#oc2 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -250ms][!#oc3 to,{y:-12, scale:1.025, duration:.35, ease:'power2.out'} -200ms][>#oc3.tt -50ms][>#oc3.sk +150ms][>#oc3.li1 +900ms][>#oc3.for +1600ms][♪marker -8dB to=0.8s +100ms]そして、責めない表示。[>#o_x1 +100ms][>#o_x2 +350ms]予算超過は、[>#oc3.sk2 -100ms][!#oc3 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} +1700ms][♪ding -6dB]来月の調整案として見せる。[silence:+0.5s]

# concl — 文の頭で帯の付箋を 1 枚ずつ (題を拭き出し・要の語に赤い下線・補足)・要の語で赤いチェック・最後に署名の付箋
*** concl
se swish -10dB
se tape -8dB +300ms
@n: [silence:0.5s][!#grid to,{x:-1152, duration:.9, ease:'power3.inOut'} -450ms][!#hdr.hl to,{x:708, duration:.55, ease:'back.inOut'} -400ms][!#bt8.t{hl} marker +120ms][>#cs1 -150ms][>#cs1.u +750ms][>#cs1.s +700ms][♪note -6dB -150ms]やめる人の半分以上は、最初の1か月。記録は[>#ck[1] +150ms][♪check -4dB +200ms]2週目から減り始めます。
@: [>#cs2 -150ms][>#cs2.u +750ms][>#cs2.s +700ms][♪note -6dB -150ms]離脱は2つの瞬間に集まる。[>#ck[2] +150ms][♪check -4dB]機能より、その瞬間の体験を直しましょう。
@: [>#cs3 -150ms][>#cs3.u +750ms][>#cs3.s +700ms][♪note -6dB -150ms]続く人は『だいたいでいい』。[>#ck[3] +150ms][>#e_sign +3050ms][♪check -4dB][♪ding -6dB +3100ms]正確さを求める設計が、離脱を生んでいます。[silence:2.7s]
```

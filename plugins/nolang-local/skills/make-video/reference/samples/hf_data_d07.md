# data · kakeibo-interviews (hf 全力版の全量の写し — 家計簿アプリをやめた 12 人に聞いた・明るい付箋と手書きの線で組む定性調査の報告 9 場面 (人数の四角・折れ線・型の札・比べる点と棒・ジャーニーの波・機会の札・結論の帯)) — canvas 1280x720

見せる作り: 全編 1 枚の方眼の紙と 2 場面目からの常設の上端 (マスキングテープの題・章の 7 札の上を黄の付箋が滑る)・3 場面目からの脚注・場面の骨組みの def (紺の丸の番号 + 手書きの題 + 下に伸びる黄のマーカー + 補足)・叩きつけて出る色の付箋の def (光沢・めくれの角・傾き)・数字の語で描く手書きの図 (数字を囲む赤い丸・矢印・中括弧・稲妻・チェック・打ち消し線と下線)・降り積もる 1 人 = 1 枚の四角・左から描く折れ線と面・語で浮く型の札と 12 マスの塗り替え・1 点 = 1 人の点と棒の比較・波のジャーニー・ラフの図つきの機会の札・場面は左へ抜け次の場面が右から滑り込む切替・音の層 (BGM + 紙・付箋・ペンの効果音を場面の頭と数字の語に)

```design.txt
#v2
# 学ぶ作り: 全編 1 枚の方眼の紙と周辺の焼け・2 場面目から常設の上端 (マスキングテープの題 + 章の 7 札と黄の付箋が滑る)・3 場面目から常設の脚注
# 場面 = 番号の丸 + 手書きの見出し (黄のマーカーが下に伸びる) + 付箋の板。付箋は def (色・めくれの角・傾き・叩きつける入場) で揃え、中身は数字の語で出す
# 図は手書きの線で描く: 数字を囲む赤い丸 (circle_hand を draw)・矢印と波の道 (path を draw)・中括弧・稲妻・チェック・打ち消し線と下線
# hf d07 kakeibo-interviews (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面は左へ抜けて (section の out)、次の場面が右から滑り込む (slide)
canvas 1280x720 bg=#FBF7EE
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
run sm { font-size: 15px; color: $ink2 }
run x2 { color: $ink2 }
run cn { font-family: m; color: $ink }
# 場面の退場 (左へ 93 px 抜けて消える・hf の leave): def の根と群は section の out を継がないので根に付ける
motion leave { out: {x:-93, opacity:0, duration:0.36, ease:'power2.in'} }
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
div { padding: 0px; border: none; box-shadow: none; border-radius: 0px; background: none; in: none }
bgm#music 明るく前向きで軽やかなアコースティックの曲、ギターと木琴と軽い手拍子、穏やかなテンポで主旋律は控えめ、調査報告の解説の下地

# 付箋 (色の地 + 上の光沢 + 右下のめくれ + 柔らかい落ち影)・叩きつけて出る (上から・大きめ・傾けて・back で着地)
def note(c) = div(out: leave; border-radius: 2px 2px 12px 2px; background: {c}; box-shadow: 0px 9px 12px #503C1440; in: {y:-31, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 2px 2px 12px 2px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 31px; height: 31px; border-radius: 0px 0px 12px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
# 白いカード (グラフの板・凡例)
def card = div(out: leave; border-radius: 5px; background: $wht; box-shadow: 0px 8px 12px #503C1430; in: {y:-13, scale:1.03, rotation:-2, opacity:0, duration:.55, ease:'back.out(1.6)'})
# マスキングテープ (付箋の上端からはみ出して貼る — hf の作り: child_overflow)
def tape = div(width: 100px; height: 27px; background: #E9DBB2DB; box-shadow: 0px 1px 2px #00000014)
# 場面の見出し: 紺の丸の番号 (弾む) + 手書きの題 (左から拭き出し・下に黄のマーカーが伸びる) + 補足
def btitle(n, t, s="") = div(out: leave; left: 60px; top: 68px; width: 1100px; height: 56px)
  div#c(left: 0px; cy: 50%; width: 47px; height: 47px; border-radius: 99px; background: $ink; delay: 280; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)'})
    p#n(cx: 50%; cy: 50%; font-size: 23px; font-family: m; color: #FFFFFF; content: {n})
  p#t(left: 62px; cy: 50%; font-size: 44px; font-family: m; line-height: 1; white-space: nowrap; delay: 340; in: wipe {dir: 'right', duration: 0.55}; content: "{hl}{t}{/}")
  p#s(left: .t.right+19; top: 26px; font-size: 19px; color: $ink2; white-space: nowrap; delay: 750; in: {y:8, opacity:0, duration:.45, ease:'power3.out'}; content: {s})
# 赤い手書きの丸 (数字を囲む)
def loop(d=.55) = shape(path: circle_hand; background: none; border: 5px solid $red; in: draw {duration: {d}})
# 1〜12 人の札 (付箋の小さな四角)
def sq(c) = div(out: leave; width: 61px; height: 61px; border-radius: 1px 1px 7px 1px; background: {c}; box-shadow: 0px 4px 5px #503C1440)
# 比べる値 (大きな値 + 下に小さな割合)
def cval(v, s="") = div(out: leave; width: 150px; height: 60px; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'})
  p#v(left: 0px; top: 0px; font-size: 35px; font-family: m; line-height: 1; white-space: nowrap; content: {v})
  p#s(left: 3px; top: 40px; font-size: 17px; color: $ink2; content: {s})
# 4 つの型の札 (色の付箋 + 絵 + 名 + 人数と割合 + 説明 + 白い付箋の発言)
def pcard(c, img, nm, n, pct, ds, who, q, qr) = div(out: leave; top: 131px; width: 269px; height: 453px; border-radius: 2px 2px 12px 2px; background: {c}; box-shadow: 0px 9px 12px #503C1440; in: {y:-23, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 2px 2px 12px 2px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 31px; height: 31px; border-radius: 0px 0px 12px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
  img#img(left: 13px; top: 9px; width: 243px; height: 145px; object-fit: contain; main: none; content: {img})
  p#nm(left: 0px; top: 164px; width: 269px; font-size: 33px; font-family: m; line-height: 1; text-align: center; content: {nm})
  div#ct(left: 0px; top: 205px; width: 269px; height: 61px; in: {scale:.4, opacity:0, duration:.45, ease:'back.out(2.2)'})
    p#n(left: 55px; top: 0px; font-size: 61px; font-family: m; line-height: 1; content: {n})
    p#u(left: .n.right+1; top: 27px; font-size: 29px; font-family: m; line-height: 1) 人
    p#p(left: .u.right+5; top: 30px; font-size: 23px; color: $ink2; line-height: 1; content: {pct})
  shape#loop(left: 42px; top: 199px; width: 92px; height: 68px; path: circle_hand; background: none; border: 3px solid #D93F45CC; in: draw {duration: 0.5})
  p#ds(left: 17px; top: 277px; width: 235px; font-size: 17px; line-height: 1.38; text-align: center; in: {y:8, opacity:0, duration:.45, ease:'power3.out'}; content: {ds})
  div#qt(left: 9px; top: 330px; width: 251px; height: 117px; border-radius: 2px 2px 12px 2px; background: $wht; box-shadow: 0px 9px 12px #503C1440; transform: rotate({qr}deg); in: {y:-17, scale:1.08, rotation:-6, opacity:0, duration:.5, ease:'back.out(1.6)'})
    p#who(left: 13px; top: 11px; font-size: 13px; color: #FFFFFF; background: $ink; border-radius: 3px; padding: 3px 6px 3px 6px; line-height: 1; content: {who})
    p#q(left: 13px; top: 32px; width: 228px; font-size: 16px; font-family: h; line-height: 1.3; content: {q})
# 離脱の瞬間の札 (白い付箋 + 赤い番号 + 題 + 人数 + 内訳の札 + 理由)
def mcard(b, t, n, brk, why) = div(out: leave; top: 313px; height: 261px; border-radius: 2px 2px 12px 2px; background: $wht; box-shadow: 0px 9px 12px #503C1440; in: {y:-20, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 2px 2px 12px 2px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#bd(left: 17px; top: 16px; width: 39px; height: 39px; border-radius: 99px; background: $red)
    p#t(cx: 50%; cy: 50%; font-size: 21px; font-family: m; color: #FFFFFF; content: {b})
  p#tt(left: 64px; top: 23px; font-size: 23px; font-family: m; line-height: 1.15; white-space: nowrap; content: {t})
  p#nn(left: 19px; top: 75px; font-size: 77px; font-family: m; line-height: 1; color: $red; in: {scale:.3, opacity:0, duration:.42, ease:'back.out(2.4)'}; content: {n})
  p#brk(left: 168px; top: 124px; font-size: 15px; color: $ink2; white-space: nowrap; in: {y:17, opacity:0, duration:.5, ease:'power3.out'}; content: {brk})
  p#why(left: 20px; top: 172px; font-size: 18px; font-family: h; line-height: 1.38; in: {y:17, opacity:0, duration:.5, ease:'power3.out'}; content: {why})
# 機会の札 (色の付箋 + 丸の番号 + 題 + ラフの図 + 箇条 + 由来)
def ocard(c, no, tt, f) = div(out: leave; top: 144px; width: 360px; height: 467px; border-radius: 2px 2px 12px 2px; background: {c}; box-shadow: 0px 9px 12px #503C1440; in: {y:-24, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 2px 2px 12px 2px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 31px; height: 31px; border-radius: 0px 0px 12px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
  div#no(left: 20px; top: 19px; width: 44px; height: 44px; border-radius: 99px; border: 3px solid $ink)
    p#t(cx: 50%; cy: 50%; font-size: 24px; font-family: m; content: {no})
  p#tt(left: 75px; top: 27px; font-size: 31px; font-family: m; line-height: 1.05; white-space: nowrap; in: wipe {dir: 'right', duration: 0.5}; content: {tt})
  p#for(left: 29px; top: 419px; font-size: 15px; color: $ink2; white-space: nowrap; in: {y:5, opacity:0, duration:.45, ease:'power3.out'}; content: {f})
# 箇条の 1 行 (黒い点 + 文)
def li(t) = div(width: 307px; height: 52px; in: {y:8, opacity:0, duration:.5, ease:'power3.out'})
  shape#dot(left: 1px; top: 9px; width: 9px; height: 9px; path: ellipse; background: $ink)
  p#t(left: 20px; top: 0px; width: 287px; font-size: 19px; line-height: 1.36; content: {t})
# 結論の帯の付箋 (紺の丸の番号 + 題 (左から拭き出し) + 補足)
def ccard(c, n, h, s) = div(out: leave; left: 64px; width: 867px; height: 140px; border-radius: 2px 2px 12px 2px; background: {c}; box-shadow: 0px 9px 12px #503C1440; in: {y:-20, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sheen(inset: 0; border-radius: 2px 2px 12px 2px; background: linear(#FFFFFF80,#FFFFFF00@30%,#5A3C0000@60%,#5A3C000F,172))
  div#curl(right: 0px; bottom: 0px; width: 31px; height: 31px; border-radius: 0px 0px 12px 0px; background: linear(#00000000@45%,#0000001A@50%,#FFFFFFA6@57%,#FFFFFF00@78%,315))
  div#nb(left: 23px; top: 31px; width: 75px; height: 75px; border-radius: 99px; background: $ink)
    p#t(cx: 50%; cy: 50%; font-size: 43px; font-family: m; color: #FFFFFF; content: {n})
  p#h(left: 121px; top: 27px; font-size: 37px; font-family: m; line-height: 1.05; white-space: nowrap; in: wipe {dir: 'right', duration: 0.7}; content: {h})
  p#s(left: 123px; top: 83px; font-size: 20px; color: $ink2; white-space: nowrap; in: {y:7, opacity:0, duration:.5, ease:'power3.out'}; content: {s})

# 全編の地 (根・z back): 方眼の紙 + 周辺の焼け
# hf の作り: 方眼は画面より広く敷き (hf 4200×1160 の 2/3)、場面ごとに左へ 96 px (3 マス) 送る (hf は -150 px × 場面番号 = 100 px・0.9 s power3.inOut) — timeline の各 cut の頭の `[!#grid to,{x:-96×n}]`・根の層は cut を跨いで続くので値は累積の絶対値
# engine: pattern の板 (svg) は resource-service が 1 辺 2048 px まで — 幅 1280 + 8 場面 × 96 = 2048 に収める (100 px × 8 = 2800 px 幅は描けない)
div#grid.bleed(left: 0px; top: -27px; width: 2048px; height: 773px; pattern: grid,32,#406EAA16; z-index: back)
div#vig(inset: 0; background: radial(#FBF7EE00@55%,#785F3221,50%,45%); z-index: back)

# title — 黄の付箋が叩きつけられ、題を 1 行ずつ拭き出す (12 は赤で弾み、赤い丸で囲む)・右に座り込む人の絵・「ポケットノート」で桃の付箋
section#title(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
img#cover(left: 767px; top: 112px; width: 467px; height: 311px; object-fit: contain; main: none; delay: 350; in: {scale:.92, y:13, opacity:0, duration:.9, ease:'power3.out'}) [transparent]床にあぐらをかいて座る若い人が、スマートフォンをゆるく持ち、退屈そうに小さくため息をついて横を向いている。まわりにくしゃくしゃのレシート、数枚の硬貨、閉じた小さなノートが散らばる。人物と小物を枠いっぱいに収め、余白を作らない
note#t_note(left: 87px; top: 127px; width: 673px; height: 433px; c: $yel; transform: rotate(-2deg); delay: 80; in: {y:-47, scale:1.14, rotation:-8, opacity:0, duration:.6, ease:'back.out(1.6)'})
  tape#tp(left: 280px; top: -13px; transform: rotate(2deg))
  p#kick(left: 52px; top: 43px; font-size: 23px; color: $ink2; letter-spacing: .06em; line-height: 1; delay: 320; in: {y:7, opacity:0, duration:.5, ease:'power3.out'}) 定性調査レポート ｜ ユーザーインタビュー
  p#l1(left: 52px; top: 93px; font-size: 75px; font-family: m; line-height: 1; white-space: nowrap; delay: 370; in: wipe {dir: 'right', duration: 0.5}) 家計簿アプリを
  p#l2a(left: 52px; top: 222px; font-size: 75px; font-family: m; line-height: 1; delay: 620; in: wipe {dir: 'right', duration: 0.3}) やめた
  p#n12(left: 261px; top: 164px; font-size: 141px; font-family: m; line-height: 1; letter-spacing: -.02em; color: $red; delay: 770; in: {scale:.1, opacity:0, duration:.5, ease:'back.out(2.4)'}) 12
  p#l2b(left: 397px; top: 222px; font-size: 75px; font-family: m; line-height: 1; delay: 920; in: wipe {dir: 'right', duration: 0.25}) 人に
  p#l3(left: 52px; top: 308px; font-size: 75px; font-family: m; line-height: 1; delay: 1070; in: wipe {dir: 'right', duration: 0.3}) 聞いた
  loop#ring(left: 245px; top: 186px; width: 186px; height: 113px; d: .65; delay: 1040; overlap: t_note.n12)
  shape#u3(left: 48px; top: 372px; width: 238px; height: 8px; path: line_h; border: 6px solid $red; in: draw {duration: 0.45})
note#t_sub(left: 440px; top: 490px; width: 407px; height: 133px; c: $pnk; transform: rotate(3deg); overlap: t_note; in: {y:-20, scale:1.14, rotation:8, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#a(left: 27px; top: 20px; font-size: 20px; color: $ink2) 架空の家計簿アプリ
  p#b(left: 27px; top: 50px; font-size: 36px; font-family: m; line-height: 1.2) 「ポケットノート」
p#t_team(left: 860px; top: 639px; font-size: 17px; color: $ink2; in: {y:7, opacity:0, duration:.5, ease:'power3.out'}) アプリデザインチーム 共有用

# method — 上端の常設が降り、青・黄・緑の付箋を語で 1 枚ずつ (214 を数える)・矢印でインタビューの絵へ・「比較」の両矢印・赤い手書きの一文と「型」の丸
section#method(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
# 常設の上端 (sticky・最後まで): マスキングテープの題 + 章の 7 札 (黄の付箋が場面の章へ滑る)
# 題・章の札・脚注は hf の $ink2 だと細い手書きの本文書体で薄く読めるので既定の $ink (文字の縁 stroke は 1 px 未満に絞れず潰れるので使わない)
div#hdr.sticky(left: 0px; top: 0px; width: 1280px; height: 60px; z-index: front; delay: 100; in: {opacity:0, duration:.5, ease:'power1.out'})
  p#tag(left: 47px; top: 20px; font-size: 15px; background: #E9DBB2CC; padding: 7px 15px 5px 15px; line-height: 1.3; white-space: nowrap) 定性調査レポート ｜ 家計簿アプリ「ポケットノート」（架空）
  div#hl(left: 690px; top: 20px; width: 75px; height: 31px; border-radius: 2px 2px 7px 2px; background: $yel; box-shadow: 0px 3px 5px #503C1440)
  p#ch(left: "690;769;847;926;1005;1083;1162"; top: 20px; width: 75px; height: 31px; font-size: 14px; text-align: center; line-height: 2.2; white-space: nowrap) ×7 {cn}01{/}設計;{cn}02{/}時期;{cn}03{/}型;{cn}04{/}違い;{cn}05{/}瞬間;{cn}06{/}機会;{cn}07{/}結論
btitle#bt1(n: "01"; t: "調査の設計"; s: "誰に、どう聞いたか")
note#m_a(left: 67px; top: 193px; width: 320px; height: 313px; c: $blu; transform: rotate(-2.5deg))
  p#lbl(left: 29px; top: 28px; font-size: 21px; color: $ink2) 声をかけた人
  p#n(left: 29px; top: 63px; font-size: 119px; font-family: m; line-height: 1; in: {opacity:0, duration:.12}) [count:214 start=0 ms=2100]
  p#u(left: .n.right+2; top: 122px; font-size: 52px; font-family: m; line-height: 1) 人
  p#d(left: 29px; top: 194px; font-size: 23px; line-height: 1.32) 記録が{dr}30日以上{/}[br]止まった人
shape#m_arrow(path: "M400 353 Q454 355 488 313"; background: none; border: 4px solid $ink; in: draw {duration: 0.35})
shape#m_arrow_h(path: "M487 329 L488 313 L472 317"; background: none; border: 4px solid $ink; in: draw {duration: 0.35})
img#m_img(left: 490px; top: 152px; width: 347px; height: 231px; object-fit: contain; main: none; in: {scale:.9, opacity:0, duration:.6, ease:'power3.out'}) [transparent]小さな丸テーブルで向かい合う 2 人の和やかな 1 対 1 のインタビュー。1 人はクリップボードとペンでメモを取り、もう 1 人は手を開いて話している。テーブルにコーヒーカップが 2 つ、頭上に白紙の付箋が数枚ふわりと浮かぶ。人物とテーブルを枠いっぱいに収め、余白を作らない
note#m_b(left: 513px; top: 433px; width: 313px; height: 172px; c: $yel; transform: rotate(1.8deg); overlap: m_img)
  p#lbl(left: 27px; top: 20px; font-size: 21px; color: $ink2) インタビュー
  p#n12(left: 27px; top: 53px; font-size: 69px; font-family: m; line-height: 1) 12
  p#u1(left: .n12.right+1; top: 82px; font-size: 36px; font-family: m; line-height: 1) 人
  p#x(left: .u1.right+7; top: 83px; font-size: 35px; font-family: m; line-height: 1) ×
  p#n45(left: .x.right+7; top: 60px; font-size: 61px; font-family: m; line-height: 1) 45
  p#u2(left: .n45.right+1; top: 85px; font-size: 33px; font-family: m; line-height: 1) 分
  p#s(left: 27px; top: 130px; font-size: 17px; color: $ink2) P1～P12 に 1人ずつ
note#m_c(left: 893px; top: 200px; width: 320px; height: 313px; c: $mnt; transform: rotate(2.2deg); in: {y:-31, scale:1.14, rotation:7, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#lbl(left: 31px; top: 28px; font-size: 21px; color: $ink2) 比較のため
  p#t(left: 31px; top: 61px; font-size: 24px; line-height: 1.3) 1年以上[br]続けている人
  p#n(left: 31px; top: 127px; font-size: 120px; font-family: m; line-height: 1) 6
  p#u(left: .n.right+2; top: 191px; font-size: 48px; font-family: m; line-height: 1) 人
  p#s(left: 31px; top: 250px; font-size: 19px; color: $ink2) にも同じ質問をした
# 「比較」の両矢印 (青いペン)
shape#m_cmp_l(path: "M841 365 Q866 356 891 365"; background: none; border: 3px solid #2A63C9E6; in: draw {duration: 0.3})
shape#m_cmp_h1(path: "M880 368 L891 365 L884 355"; background: none; border: 3px solid #2A63C9E6; in: draw {duration: 0.2})
shape#m_cmp_h2(path: "M848 355 L841 365 L853 368"; background: none; border: 3px solid #2A63C9E6; in: draw {duration: 0.2})
p#m_cmp(left: 841px; top: 319px; font-size: 24px; font-family: h; color: $pen; in: {opacity:0, duration:.35, ease:'power1.out'}) 比較
p#m_note(left: 307px; top: 617px; width: 667px; font-size: 33px; font-family: h; color: $red; text-align: center; white-space: nowrap; in: wipe {dir: 'right', duration: 1.1}) 数が少ないので、割合より「型」を見る
shape#m_note_u(path: "M353 657 Q640 660 927 654"; background: none; border: 3px solid #D93F45B3; overlap: m_note; in: draw {duration: 0.6})
loop#m_kata(left: 729px; top: 610px; width: 122px; height: 48px; border: 4px solid $red; overlap: m_note)

# when — 方眼が送られ、章の付箋が「02」へ・4 列の付箋の四角が列ごとに降り積もる・「中央値」で黄の付箋に 26 を数えて丸・「12人中7人」で中括弧と赤字・「最初の1か月」で橙の列が弾む
section#when(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
# 常設の脚注 (sticky・最後まで)
p#foot.sticky(left: 47px; top: 685px; font-size: 14px; z-index: front; white-space: nowrap; delay: 300; in: {opacity:0, duration:.6, ease:'power1.out'}) ※ n＝12（やめた人）＋6（続けている人）。数が少ないため、割合より「型」を見る調査
btitle#bt2(n: "02"; t: "いつ、やめたか"; s: "最後に記録した日まで（12人）")
sq#c1(left: 136px; top: "535;467"; c: $org; rotation: "-1.8;-0.6"; delay: 550; in: {y:-27, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×2
sq#c2(left: 302px; top: "535;467;399;331;263"; c: $org; rotation: "0.6;1.8;-1.2;0;1.2"; delay: 750; in: {y:-27, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×5
sq#c3(left: 469px; top: "535;467;399"; c: $later; rotation: "-1.2;0;1.2"; delay: 950; in: {y:-27, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×3
sq#c4(left: 636px; top: "535;467"; c: $later; rotation: "1.2;-1.8"; delay: 1150; in: {y:-27, scale:1.1, rotation:-8, opacity:0, duration:.35, ease:'back.out(1.8)', stagger:{each:.06}}) ×2
div#w_axis(left: 73px; top: 604px; width: 680px; height: 3px; background: #24304AD9; delay: 450; in: {scaleX:0, duration:.6, ease:'power1.inOut', pivot:'left'})
p#w_col(left: "94;260;427;594"; top: 615px; width: 147px; font-size: 21px; text-align: center; line-height: 1; delay: 550; in: {y:7, opacity:0, duration:.35, ease:'power3.out', stagger:{each:.2}}) ×4 1週間以内;1～4週;1～3か月;3か月以上
p#w_cnt1(left: 94px; top: 426px; width: 147px; font-size: 35px; font-family: m; text-align: center; line-height: 1; delay: 770; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 2{cu}人{/}
p#w_cnt2(left: 260px; top: 222px; width: 147px; font-size: 35px; font-family: m; text-align: center; line-height: 1; delay: 1150; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 5{cu}人{/}
p#w_cnt3(left: 427px; top: 358px; width: 147px; font-size: 35px; font-family: m; text-align: center; line-height: 1; delay: 1230; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 3{cu}人{/}
p#w_cnt4(left: 594px; top: 426px; width: 147px; font-size: 35px; font-family: m; text-align: center; line-height: 1; delay: 1370; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 2{cu}人{/}
# 凡例 (橙 = 最初の 1 か月・淡い黄 = それ以降)
div#w_leg(left: 80px; top: 649px; width: 480px; height: 20px; delay: 1400; in: {opacity:0, duration:.4, ease:'power1.out'})
  div#s1(left: 0px; top: 1px; width: 17px; height: 17px; border-radius: 1px 1px 4px 1px; background: $org)
  p#t1(left: 24px; top: 0px; font-size: 17px; color: $ink2; white-space: nowrap) ＝1人（最初の1か月）
  div#s2(left: 222px; top: 1px; width: 17px; height: 17px; border-radius: 1px 1px 4px 1px; background: $later)
  p#t2(left: 246px; top: 0px; font-size: 17px; color: $ink2; white-space: nowrap) ＝1人（それ以降）
shape#w_brace(path: "M127 222 Q127 207 142 207 L235 207 Q250 207 250 192 Q250 207 265 207 L358 207 Q373 207 373 222"; background: none; border: 4px solid $red; in: draw {duration: 0.55})
p#w_brace_l(left: 100px; top: 137px; width: 373px; font-size: 33px; font-family: m; color: $red; text-align: center; white-space: nowrap; in: {y:9, opacity:0, duration:.45, ease:'back.out(1.8)'}) 12人中 7人が最初の1か月
note#w_med(left: 823px; top: 200px; width: 393px; height: 347px; c: $yel; transform: rotate(2deg))
  p#lbl(left: 35px; top: 27px; font-size: 21px; color: $ink2) やめるまでの期間
  p#mid(left: 35px; top: 58px; font-size: 20px; color: $ink2) 中央値
  p#n(left: 35px; top: 83px; font-size: 167px; font-family: m; line-height: 1; in: {opacity:0, duration:.12}) [count:26 start=0 ms=900]
  p#u(left: .n.right+2; top: 174px; font-size: 64px; font-family: m; line-height: 1) 日
  loop#ring(left: 6px; top: 102px; width: 242px; height: 147px; overlap: w_med.n)

# weekly — 白い板に方眼の軸を描き、「5.8日」から「1.3日」まで折れ線と面を左から描く (点と値が線の到着で弾む)・凡例の板・「2週目」で桃の付箋と赤い丸・「坂」で赤い矢印と斜めの手書き
section#weekly(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt3(n: "02"; t: "記録日数の推移"; s: "やめた人・1週あたりの平均")
card#k_panel(left: 64px; top: 145px; width: 820px; height: 513px; transform: rotate(-.6deg); delay: 250)
  tape#tp(left: 360px; top: -12px; transform: rotate(-2deg))
div#k_g0(left: 160px; top: 586px; width: 673px; height: 3px; background: $ink; delay: 450; in: {scaleX:0, duration:.5, ease:'power1.inOut', pivot:'left'})
div#k_gl(left: 160px; top: "533;480;426;373;320;266;213"; width: 673px; height: 1px; background: #24304A2E; delay: 480; in: {scaleX:0, duration:.5, ease:'power1.inOut', pivot:'left', stagger:{each:.03}}) ×7
div#k_ya(left: 159px; top: 200px; width: 3px; height: 388px; background: $ink; delay: 450; in: {scaleY:0, duration:.5, ease:'power1.inOut', pivot:'bottom'})
p#k_ay(left: 100px; top: "578;525;472;418;365;312;258;205"; width: 47px; font-size: 16px; color: $ink2; text-align: right; line-height: 1; delay: 550; in: {opacity:0, duration:.3, ease:'power1.out'}) ×8 0;1;2;3;4;5;6;7日
p#k_ax(left: "167;347;527;707"; top: 600px; width: 107px; font-size: 20px; text-align: center; line-height: 1; delay: 600; in: {y:5, opacity:0, duration:.3, ease:'power3.out', stagger:{each:.08}}) ×4 1週目;2週目;3週目;4週目
shape#k_area(path: "M220 278 L400 368 L580 448 L760 518 L760 587 L220 587 Z"; background: #DF5F4324; in: wipe {dir: 'right', duration: 1.27, ease: 'none'})
shape#k_line(path: "M220 278 L400 368 L580 448 L760 518"; background: none; border: 5px solid $cor_ink; in: draw {duration: 1.27, ease: 'none'})
shape#k_pt(left: "210;390;570;750"; top: "268;358;438;508"; width: 20px; height: 20px; path: ellipse; background: $cor_ink; border: 3px solid #FFFFFF; box-shadow: 0px 1px 4px #00000040; in: {scale:.1, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.42}}) ×4
p#k_val(left: "193;408;588;768"; top: "223;313;393;463"; font-size: 36px; font-family: m; line-height: 1; white-space: nowrap; in: {scale:.4, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.42}}) ×4 5.8{ku}日{/};4.1{ku}日{/};2.6{ku}日{/};1.3{ku}日{/}
card#k_legend(left: 920px; top: 167px; width: 300px; height: 147px; transform: rotate(1deg); delay: 900; in: {y:-11, scale:1.04, rotation:3, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#sw(left: 20px; top: 26px; width: 40px; height: 5px; border-radius: 3px; background: $cor_ink)
  shape#dot(left: 33px; top: 21px; width: 15px; height: 15px; path: ellipse; background: $cor_ink; border: 3px solid #FFFFFF)
  p#t(left: 72px; top: 17px; font-size: 18px; white-space: nowrap) やめた人12人の平均
  p#n(left: 20px; top: 52px; font-size: 15px; line-height: 1.4; color: $ink2) 1週あたりの記録日数[br]（ログと本人の話を突き合わせた値）
note#k_take(left: 930px; top: 363px; width: 293px; height: 240px; c: $pnk; transform: rotate(-2deg); in: {y:-31, scale:1.14, rotation:-8, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(left: 27px; top: 27px; font-size: 41px; font-family: m; line-height: 1.15) 2週目から[br]坂を[br]下り始める
loop#k_loop(left: 371px; top: 341px; width: 58px; height: 53px; d: 450; border: 4px solid $red; overlap: k_val)
shape#k_arrow(path: "M420 409 Q586 470 740 556"; background: none; border: 4px solid $red; overlap: k_val; in: draw {duration: 0.55})
shape#k_arrow_h(path: "M725 558 L740 556 L734 542"; background: none; border: 4px solid $red; in: draw {duration: 0.2})
p#k_slope(left: 427px; top: 467px; font-size: 27px; font-family: h; color: $red; white-space: nowrap; transform: rotate(21deg); transform-origin: 0% 0%; in: {opacity:0, duration:.4, ease:'power1.out'}) 2週目から下り坂

# patterns — 4 色の付箋の札が並び、型の名の語で札が浮き、人数の語で数と赤い丸・発言の白い付箋・下の 12 マスを型の色に塗る
section#patterns(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt4(n: "03"; t: "4つの離脱パターン"; s: "12人の「やめ方」の型")
pcard#pc1(left: 61px; c: $yel; transform: rotate(-1.2deg); nm: "入力疲れ"; n: "5"; pct: "（42%）"; ds: "レシートや現金の支出を[br]毎回打ち込むのが続かない"; who: "P3"; q: "「夜まとめて入れようとし[br]て、思い出せない支出が3つ[br]あった時点で嫌になった」"; qr: 1.4; img: "[transparent]夜遅く机のライトの下で、片手にスマートフォン、もう片手に長く丸まった紙のレシートを持ち、半目で眠そうな人。机にくしゃくしゃのレシートの山、そばに小さな三日月。人物を枠いっぱいに収め、余白を作らない")
pcard#pc2(left: 357px; c: $blu; transform: rotate(.8deg); nm: "分類迷子"; n: "3"; pct: "（25%）"; ds: "初期設定24個のカテゴリの[br]どれに入れるか迷う"; who: "P6"; q: "「コンビニのお弁当とお茶、食費？日用品？で毎回止まる」"; qr: -1.2; img: "[transparent]片手にコンビニの弁当、もう片手に緑茶のペットボトルを持ち、開いた空の段ボール箱 2 つの間で首をかしげる人。頭の上に疑問符が 3 つ浮かぶ。人物と箱を枠いっぱいに収め、余白を作らない")
pcard#pc3(left: 653px; c: $pnk; transform: rotate(-.6deg); nm: "見て落ち込む"; n: "2"; pct: "（17%）"; ds: "予算超過の[br]赤い表示がつらい"; who: "P9"; q: "「開くたびに怒られている気がして、開かなくなった」"; qr: 1.1; img: "[transparent]肩を落とし、赤く光る警告の三角が出たスマートフォンの画面を見下ろす落ち込んだ人。頭の上に小さな灰色の雨雲。人物を枠いっぱいに収め、余白を作らない")
pcard#pc4(left: 949px; c: $lav; transform: rotate(1.1deg); nm: "用済み"; n: "2"; pct: "（17%）"; ds: "貯金の目標を達成した[br]家計の形が分かった"; who: "P12"; q: "「3か月つけて、だいたい分かったからもういいかなって」"; qr: -1.3; img: "[transparent]スマートフォンをポケットにしまいながら満足そうに手を振る人。隣に三角の小旗を立てた大きな笑顔の豚の貯金箱、まわりに小さなきらめき。人物と貯金箱を枠いっぱいに収め、余白を作らない")
p#p_lbl(left: 64px; top: 600px; font-size: 19px; line-height: 1; delay: 800; in: {opacity:0, duration:.4, ease:'power1.out'}) 12人の内訳
# 12 マス (型ごとの組・灰の地で先に並び、人数の語で型の色に塗って弾む)
div#pba(left: "193;230;268;305;342"; top: 592px; width: 33px; height: 33px; border-radius: 3px; background: $empty; delay: 800; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×5
div#pbb(left: "380;417;454"; top: 592px; width: 33px; height: 33px; border-radius: 3px; background: $empty; delay: 1000; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×3
div#pbc(left: "492;529"; top: 592px; width: 33px; height: 33px; border-radius: 3px; background: $empty; delay: 1120; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×2
div#pbd(left: "566;604"; top: 592px; width: 33px; height: 33px; border-radius: 3px; background: $empty; delay: 1200; in: {scale:.5, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.04}}) ×2
div#p_leg(left: 667px; top: 599px; width: 500px; height: 20px; in: {opacity:0, duration:.5, ease:'power1.out'})
  div#s(left: "0;121;242;397"; top: 1px; width: 16px; height: 16px; border-radius: 1px 1px 4px 1px; background: "$yel;$blu;$pnk;$lav") ×4
  p#t(left: "21;142;263;418"; top: 0px; font-size: 17px; white-space: nowrap) ×4 入力疲れ 5;分類迷子 3;見て落ち込む 2;用済み 2

# compare — 2 列の見出しの付箋・行の題を語で・続けている人 (緑) とやめた人 (珊瑚) を点・棒・値で比べる・最後に緑の付箋の発言 (「全部正確に」を赤で消し、「だいたい…」に緑の下線)
section#compare(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt5(n: "04"; t: "続けている人と、何が違う？")
note#c_h1(left: 467px; top: 141px; width: 333px; height: 39px; c: $mnt; transform: rotate(-1deg); in: {y:-16, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(cx: 50%; cy: 50%; font-size: 24px; font-family: m; white-space: nowrap) 続けている人（6人）
note#c_h2(left: 841px; top: 141px; width: 360px; height: 39px; c: $cor; transform: rotate(1deg); in: {y:-16, scale:1.14, rotation:6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(cx: 50%; cy: 50%; font-size: 24px; font-family: m; white-space: nowrap) やめた人（12人）
div#c_sep(left: 64px; top: "288;387;485"; width: 1153px; height: 1px; background: #24304A40; delay: 600; in: {scaleX:0, duration:.6, ease:'power1.inOut', pivot:'left', stagger:{each:.08}}) ×3
p#c_l1(left: 64px; top: 213px; font-size: 22px; line-height: 1.25; in: {y:7, opacity:0, duration:.5, ease:'power3.out'}) 銀行・カードの自動連携を使う
p#c_l2(left: 64px; top: 312px; font-size: 22px; line-height: 1.25; in: {y:7, opacity:0, duration:.5, ease:'power3.out'}) 実際に使うカテゴリの数[br]{sm}中央値{/}
p#c_l3(left: 64px; top: 411px; font-size: 22px; line-height: 1.25; in: {y:7, opacity:0, duration:.5, ease:'power3.out'}) 1日の入力にかける時間[br]{sm}本人の申告・中央値{/}
p#c_l4(left: 64px; top: 509px; font-size: 22px; line-height: 1.25; in: {y:7, opacity:0, duration:.5, ease:'power3.out'}) 週に1回ふり返る習慣
# 1 点 = 1 人 (塗り = 該当・輪 = 非該当)
shape#c_d1(left: "480;515;549;584;619;653"; top: 222px; width: 28px; height: 28px; path: ellipse; background: "$mnt_ink;$mnt_ink;$mnt_ink;$mnt_ink;$mnt_ink;none"; border: 3px solid $mnt_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.05}}) ×6
cval#c_v1(left: 700px; top: 210px; v: "5/6人"; s: "83%")
shape#c_q1(left: "855;883;911;939;967;995;855;883;911;939;967;995"; top: "206;206;206;206;206;206;235;235;235;235;235;235"; width: 23px; height: 23px; path: ellipse; background: "$cor_ink;$cor_ink;$cor_ink;none;none;none;none;none;none;none;none;none"; border: 3px solid $cor_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.035}}) ×12
cval#c_w1(left: 1035px; top: 210px; v: "3/12人"; s: "25%")
div#c_b2a(left: 480px; top: 323px; width: 107px; height: 29px; border-radius: 3px 7px 7px 3px; background: $mnt; in: {scaleX:0, duration:.45, ease:'power2.out', pivot:'left'})
p#c_v2a(left: 599px; top: 320px; font-size: 35px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 8{cu}個{/}
div#c_b2b(left: 855px; top: 323px; width: 253px; height: 29px; border-radius: 3px 7px 7px 3px; background: $cor; in: {scaleX:0, duration:.6, ease:'power2.out', pivot:'left'})
p#c_v2b(left: 1120px; top: 320px; font-size: 35px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 19{cu}個{/}
div#c_b3a(left: 480px; top: 422px; width: 53px; height: 29px; border-radius: 3px 7px 7px 3px; background: $mnt; in: {scaleX:0, duration:.35, ease:'power2.out', pivot:'left'})
p#c_v3a(left: 545px; top: 419px; font-size: 35px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 1{cu}分{/}
div#c_b3b(left: 855px; top: 422px; width: 213px; height: 29px; border-radius: 3px 7px 7px 3px; background: $cor; in: {scaleX:0, duration:.5, ease:'power2.out', pivot:'left'})
p#c_v3b(left: 1080px; top: 419px; font-size: 35px; font-family: m; line-height: 1; in: {scale:.5, opacity:0, duration:.42, ease:'back.out(2.4)'}) 4{cu}分{/}
shape#c_d4(left: "480;515;549;584;619;653"; top: 518px; width: 28px; height: 28px; path: ellipse; background: $mnt_ink; border: 3px solid $mnt_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.05}}) ×6
cval#c_v4(left: 700px; top: 516px; v: "6/6人")
shape#c_q4(left: "855;883;911;939;967;995;855;883;911;939;967;995"; top: "502;502;502;502;502;502;531;531;531;531;531;531"; width: 23px; height: 23px; path: ellipse; background: "$cor_ink;$cor_ink;none;none;none;none;none;none;none;none;none;none"; border: 3px solid $cor_ink; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.035}}) ×12
cval#c_w4(left: 1035px; top: 516px; v: "2/12人")
note#c_quote(left: 240px; top: 577px; width: 800px; height: 92px; c: $mnt; transform: rotate(-1deg); in: {y:-20, scale:1.14, rotation:-6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#q(left: 31px; top: 16px; font-size: 30px; font-family: h; line-height: 1; white-space: nowrap) {x2}「全部正確に」{/}より 「だいたい合っていればいい」
  p#w(left: 31px; top: 57px; font-size: 17px; color: $ink2; white-space: nowrap) ― 続けている人 6人中5人がこう話した
  shape#x(left: 35px; top: 29px; width: 202px; height: 6px; path: line_h; border: 4px solid $red; in: draw {duration: 0.4})
  shape#u(left: 319px; top: 49px; width: 371px; height: 6px; path: line_h; border: 5px solid #1F8D62D9; in: draw {duration: 0.8})

# moments — 波のジャーニーの線を左から描いて段階の札・「3日以上」「初めて」で谷に赤い丸と稲妻 + 白い付箋 (人数・内訳の四角・理由)・「11人」で橙の付箋
section#moments(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt6(n: "05"; t: "離脱が起きる2つの瞬間"; s: "ジャーニーのどこでやめたか")
shape#j_path(path: "M80 220 C173 200 253 197 347 212 C433 225 480 280 547 288 C613 296 653 220 733 212 C827 204 907 293 973 299 C1040 304 1080 227 1200 208"; background: none; border: 5px solid #24304AE6; delay: 500; in: draw {duration: 1.4})
shape#j_head(path: "M1183 193 L1204 208 L1181 223"; background: none; border: 5px solid $ink; delay: 1850; in: draw {duration: 0.2})
p#j_lab(left: "33;220;393;640;1073"; top: 157px; width: 147px; font-size: 17px; color: $ink2; text-align: center; white-space: nowrap; delay: 600; in: {y:5, opacity:0, duration:.35, ease:'power2.out', stagger:{each:.18}}) ×5 記録をはじめる;毎日つける;記録がたまる;月末・予算;目標を達成
loop#j_loop1(left: 500px; top: 249px; width: 94px; height: 78px; d: 450; border: 6px solid $red)
# hf の boltD (32x70 @1920 = 21x47) を canvas px の素の path で (名の bolt は縦横比を保って枠の幅に縮み半分の大きさになる)
shape#j_bolt1(path: "M573.3,225.3 L562.6,250.7 L572.0,250.7 L566.6,272.0 L584.0,244.0 L574.6,244.0 L580.0,225.3 Z"; background: #FFD633F2; border: 3px solid $red; in: draw {duration: 0.35})
loop#j_loop2(left: 926px; top: 260px; width: 94px; height: 78px; d: 450; border: 6px solid $red)
shape#j_bolt2(path: "M1000.0,236.0 L989.3,261.4 L998.7,261.4 L993.3,282.7 L1010.7,254.7 L1001.3,254.7 L1006.7,236.0 Z"; background: #FFD633F2; border: 3px solid $red; in: draw {duration: 0.35})
mcard#mc1(left: 347px; width: 407px; transform: rotate(-.8deg); b: "1"; t: "記録を3日以上ためた後の再開"; n: "7{nu}人{/}"; brk: "入力疲れ5・分類迷子2"; why: "たまった分を思い出せず、[br]「抜けがある家計簿」に戻る気がしなくなる")
  div#chips(left: "167;197;227;257;287;317;347"; top: 88px; width: 25px; height: 25px; border-radius: 1px 1px 5px 1px; background: "$yel;$yel;$yel;$yel;$yel;$blu;$blu"; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.06}}) ×7
mcard#mc2(left: 780px; width: 427px; transform: rotate(.9deg); b: "2"; t: "初めて予算を超えた月の通知"; n: "4{nu}人{/}"; brk: "見て落ち込む2・分類迷子1・用済み1"; why: "「開くたびに怒られている気がして、[br]開かなくなった」（見て落ち込む）"; in: {y:-20, scale:1.14, rotation:6, opacity:0, duration:.55, ease:'back.out(1.6)'})
  div#chips(left: "167;197;227;257"; top: 88px; width: 25px; height: 25px; border-radius: 1px 1px 5px 1px; background: "$pnk;$pnk;$blu;$lav"; in: {scale:.2, opacity:0, duration:.42, ease:'back.out(2.4)', stagger:{each:.06}}) ×4
  p#why(left: 52px)
  p#who(left: 20px; top: 175px; font-size: 12px; color: #FFFFFF; background: $ink; border-radius: 3px; padding: 3px 5px 2px 5px; line-height: 1; in: {y:17, opacity:0, duration:.5, ease:'power3.out'}) P9
note#j11(left: 61px; top: 324px; width: 256px; height: 240px; c: $org; transform: rotate(-2deg); in: {y:-31, scale:1.14, rotation:-9, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#a(left: 24px; top: 23px; font-size: 23px) 12人のうち
  p#n(left: 24px; top: 58px; font-size: 100px; font-family: m; line-height: 1; color: $red) 11{nu}人{/}
  p#s(left: 24px; top: 165px; font-size: 20px; line-height: 1.32) が、どちらかの[br]直後にやめた
note#j_rest(left: 760px; top: 589px; width: 460px; height: 61px; c: $lav; transform: rotate(.6deg); in: {y:-13, scale:1.14, rotation:4, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#t(left: 20px; top: 16px; font-size: 18px; line-height: 1.25; white-space: nowrap) 残る1人（用済み）は、目標を達成して自然にやめた

# opps — 3 色の付箋の札・札ごとに題を拭き出し、ラフの図 (ためた日のまとめ入力・8 個のカテゴリと提案・超過の帯と調整案)・箇条と由来・「予算超過」で赤い × を引く
section#opps(stagger: {each:0}; out: {x:-93, opacity:0, duration:.36, ease:'power2.in'})
btitle#bt7(n: "06"; t: "3つの機会領域"; s: "2つの瞬間と、迷いをほどく")
ocard#oc1(left: 61px; c: $yel; transform: rotate(-1.4deg); no: "1"; tt: "ためても戻れる"; f: "← 瞬間1：ためた後の再開")
  group#sk(left: 27px; top: 85px; width: 307px; height: 180px; out: leave; in: {y:5, opacity:0, duration:.3, ease:'power2.out', stagger:.08})
    div#phone(left: 100px; top: 7px; width: 123px; height: 168px; border-radius: 17px; border: 3px solid $ink; background: #FFFFFF)
    p#t1(left: 115px; top: 29px; font-size: 15px; white-space: nowrap) 3日分まとめて
    shape#box(left: 115px; top: 59px; width: 93px; height: 31px; path: rect,r=0.17; background: none; border: 2px solid $ink2; dash: 5,4)
    p#t2(left: 123px; top: 67px; font-size: 15px; color: $ink2; white-space: nowrap) だいたい ￥
    div#pill(left: 111px; top: 104px; width: 101px; height: 28px; border-radius: 14px; background: $mnt)
    p#t3(left: 121px; top: 111px; font-size: 13px; white-space: nowrap) 未分類でOK
    shape#day(left: "5;36;67"; top: 43px; width: 27px; height: 27px; path: rect,r=0.15; background: none; border: 2px solid $ink2; dash: 4,3) ×3
    p#dt(left: "5;36;67"; top: 48px; width: 27px; font-size: 13px; color: $ink2; text-align: center; line-height: 1) ×3 月;火;水
    p#t4(left: 9px; top: 79px; font-size: 14px; color: $ink2; white-space: nowrap) 抜けた日
    p#ar(left: 27px; top: 100px; font-size: 27px; font-family: m) →
  li#li1(left: 29px; top: 280px; t: "抜けた日を「だいたいの金額」で[br]まとめて入れられる")
  li#li2(left: 29px; top: 340px; t: "未分類のままでよい")
ocard#oc2(left: 460px; c: $blu; transform: rotate(.9deg); no: "2"; tt: "分類は後で・少なく"; f: "← 分類迷子")
  div#chip(left: "39;110;181;252;39;110;181;252"; top: "100;100;100;100;136;136;136;136"; width: 64px; height: 27px; border-radius: 13px; border: 2px solid $ink; background: #FFFFFF; in: {scale:.3, opacity:0, duration:.3, ease:'back.out(2)', stagger:{each:.05}}) ×8
  group#sk(left: 27px; top: 85px; width: 307px; height: 180px; out: leave; in: {y:5, opacity:0, duration:.35, ease:'power2.out', stagger:.12})
    p#t1(left: 15px; top: 93px; font-size: 16px; color: $ink2; white-space: nowrap) カテゴリ 8個からスタート
    div#box(left: 67px; top: 121px; width: 227px; height: 47px; border-radius: 11px; border: 2px solid $ink; background: #FFFFFF)
    p#t2(left: 80px; top: 137px; font-size: 15px; white-space: nowrap) {cn}✦{/} アプリから分け方の提案
  li#li1(left: 29px; top: 280px; t: "最初はカテゴリ8個から始める")
  li#li2(left: 29px; top: 314px; t: "分け方はアプリが提案する")
ocard#oc3(left: 859px; c: $pnk; transform: rotate(-.7deg); no: "3"; tt: "責めない表示"; f: "← 瞬間2：初めての予算超過")
  group#sk(left: 27px; top: 85px; width: 307px; height: 180px; out: leave; in: {y:5, opacity:0, duration:.3, ease:'power2.out', stagger:.08})
    div#track(left: 13px; top: 13px; width: 280px; height: 27px; border-radius: 13px; border: 2px solid $ink; background: #FFFFFF)
    div#fill(left: 15px; top: 15px; width: 227px; height: 23px; border-radius: 11px 0px 0px 11px; background: $org)
    div#over(left: 242px; top: 15px; width: 49px; height: 23px; border-radius: 0px 11px 11px 0px; background: $over)
    p#t1(left: 200px; top: 51px; font-size: 27px; font-family: m; color: $red; white-space: nowrap) 超過！
  group#sk2(left: 27px; top: 85px; width: 307px; height: 180px; out: leave; in: {y:7, opacity:0, duration:.35, ease:'power2.out', stagger:.1})
    div#box(left: 13px; top: 97px; width: 280px; height: 69px; border-radius: 11px; border: 2px solid $ink; background: #FFFFFF)
    p#t1(left: 28px; top: 111px; font-size: 17px; white-space: nowrap) 来月の調整案
    p#t2(left: 28px; top: 137px; font-size: 14px; color: $ink2; white-space: nowrap) ここを少し見直してみませんか？
  li#li1(left: 29px; top: 280px; t: "予算超過を赤字で示すより、[br]来月の調整案として見せる")
shape#o_x1(path: "M1079 311 L1165 284"; background: none; border: 5px solid $red; overlap: oc3; in: draw {duration: 0.3})
shape#o_x2(path: "M1080 284 L1164 311"; background: none; border: 5px solid $red; overlap: oc3; in: draw {duration: 0.3})

# concl — 3 枚の帯の付箋を文の頭で 1 枚ずつ (題を拭き出し・要の語に赤い下線)・要の語で右端に赤いチェック・右にチームの絵・最後に桃の付箋の署名
section#concl(stagger: {each:0})
btitle#bt8(n: "07"; t: "結論"; s: "デザインで直すべきところ")
img#e_team(left: 960px; top: 200px; width: 280px; height: 187px; object-fit: contain; main: none; delay: 500; in: {scale:.9, y:11, opacity:0, duration:.8, ease:'power3.out'}) [transparent]壁の前に立つ 3 人の小さなプロダクトデザインチームが、色とりどりの白紙の付箋を貼り、マーカーで付箋の間に矢印を描いている。協力的で楽しげ。人物と付箋を枠いっぱいに収め、余白を作らない
ccard#cs1(top: 148px; c: $org; transform: rotate(-.6deg); n: "1"; h: "やめる人の半分以上は、最初の1か月"; s: "2週目から記録が減り始める（1週目 5.8日 → 4週目 1.3日）")
  shape#u(left: 531px; top: 66px; width: 200px; height: 6px; path: line_h; border: 5px solid #D93F45D9; in: draw {duration: 0.5})
ccard#cs2(top: 308px; c: $yel; transform: rotate(.5deg); n: "2"; h: "離脱の11/12は、2つの瞬間に集まる"; s: "→ 機能より「ためた後の再開」「初めての予算超過」の体験を直す")
  shape#u(left: 417px; top: 66px; width: 170px; height: 6px; path: line_h; border: 5px solid #D93F45D9; in: draw {duration: 0.5})
ccard#cs3(top: 468px; c: $mnt; transform: rotate(-.4deg); n: "3"; h: "続く人は「だいたいでいい」"; s: "正確さを求める設計が、離脱を生んでいる")
  shape#u(left: 269px; top: 66px; width: 333px; height: 6px; path: line_h; border: 5px solid #D93F45D9; in: draw {duration: 0.5})
shape#ck(left: 872px; top: "195;355;515"; width: 44px; height: 38px; path: check; background: none; border: 6px solid $red; in: draw {duration: 0.35}) ×3
note#e_sign(left: 964px; top: 427px; width: 273px; height: 153px; c: $pnk; transform: rotate(2deg); in: {y:-31, scale:1.14, rotation:8, opacity:0, duration:.55, ease:'back.out(1.6)'})
  p#a(left: 23px; top: 20px; font-size: 17px; line-height: 1.35; color: $ink2) 定性調査レポート[br]家計簿アプリ（架空）
  p#b(left: 23px; top: 73px; font-size: 31px; font-family: m) ポケットノート
```

```timeline.txt
#v2
cast n = "やわらかく落ち着いた明るい若い女性のナレーター、社内のデザインチームに定性調査の結果を丁寧に分かりやすく報告する"
silence head=0 tail=180
# 切替: 旧場面は左へ抜け (section の out)、境目の後に新場面が右から 100 px 滑り込みながら明ける (hf の enterExit)・境目で紙をめくる音
transition = slide,600,dir=left,offset=8%,opacity=0,overlap=600,ease=power3.out,se=page -4dB

# title — 付箋と題は頭に組み上がる・「ポケットノート」で桃の付箋・「12人」で 12 が弾む・「聞きました」で赤い下線
*** title
bgm music
se note -6dB +120
se pop -6dB +900
se marker -8dB to=0.8s +1150
@n: [silence:0.8s][!#t_note to,{y:-3, rotation:-1.5, duration:5, ease:'sine.inOut'}][!#cover to,{y:-8, duration:4.7, ease:'sine.inOut'} +450]架空の家計簿アプリ[>#t_sub -200][>#t_team +300][♪note -6dB -150]『ポケットノート』。やめた[!#t_note.n12 punch,1.12,duration=320]12人に、話を[>#t_note.u3 -100][♪marker -8dB to=0.8s -100]聞きました。[silence:+0.05s]

# method — 語ごとに付箋を叩きつけ、214 を数える・矢印で絵へ・「同じ質問」で両矢印と「比較」・2 文目で赤い一文と下線と「型」の丸
*** method
se swish -10dB
se tape -8dB +300
@n: [silence:0.5s][!#grid to,{x:-96, duration:.9, ease:'power3.inOut'} -450][>#hdr -400][!#bt1.t{hl} marker +120][>#m_a -50][>#m_a.n +300][♪note -6dB -50]記録が30日以上止まった[!#m_a.n punch,1.12,duration=320 +120][♪pop -6dB +50]214人に[>#m_arrow][>#m_arrow_h +300][♪marker -8dB to=0.8s -50]声をかけ、[>#m_img -300][>#m_b -200][!#m_img to,{y:-5, duration:8.8, ease:'sine.inOut'} +400][♪note -6dB -250]12人に[!#m_b.n45 punch,1.12,duration=320][♪pop -6dB -50]45分ずつインタビュー。[>#m_c -150][♪note -6dB -200]続けている6人にも、[>#m_cmp_l][>#m_cmp_h1 +200][>#m_cmp_h2 +400][>#m_cmp +200][♪marker -8dB to=0.8s]同じ質問をしました。
@: [!#m_a to,{y:-3, rotation:-2, duration:4, ease:'sine.inOut'} -80][!#m_c to,{y:-3, rotation:2.7, duration:4, ease:'sine.inOut'} -80][>#m_note][♪marker -8dB to=0.8s]数は少ないので、見るのは[>#m_note_u]割合より『[>#m_kata -50][♪ding -6dB]型』です。[silence:+0.02s]

# when — 頭で 4 列の四角が列ごとに降り、人数が弾む・「中央値」で 26 を数え「26日」で丸・「12人中7人」で中括弧・「最初の1か月」で橙の列が跳ねる
*** when
se swish -10dB
se tape -8dB +300
se pop -10dB +550
se pop -10dB +750
se pop -10dB +950
se pop -10dB +1150
@n: [silence:0.5s][!#grid to,{x:-192, duration:.9, ease:'power3.inOut'} -450][!#hdr.hl to,{x:79, duration:.55, ease:'back.inOut'} -400][!#bt2.t{hl} marker +120]やめた時期の[>#w_med -250][>#w_med.n +100][!#w_med.n count +100][♪note -6dB -250]中央値は[>#w_med.ring +150][♪ding -6dB +150]26日。[>#w_brace -100][>#w_brace_l +150][♪marker -8dB to=0.8s -100]12人中7人が、[!#c1[*] to,{y:-7, duration:.18, yoyo:true, repeat:1, ease:'power2.out'}][!#c2[*] to,{y:-7, duration:.18, yoyo:true, repeat:1, ease:'power2.out'}]最初の{1か月|いっかげつ}でやめています。[silence:+0.15s]

# weekly — 頭で白い板と軸・「5.8日」から線と面を左から描き点と値が順に弾む・「2週目」で桃の付箋と丸・「坂」で矢印と斜めの字
*** weekly
se swish -10dB
se tape -8dB +300
se marker -8dB to=0.8s +500
@n: [silence:0.5s][!#grid to,{x:-288, duration:.9, ease:'power3.inOut'} -450][!#bt3.t{hl} marker +120]週あたりの記録日数は、[>#k_area +250][>#k_line +250][>#k_pt[*] +230][>#k_val[*] +280][♪pop -6dB -50][♪marker -8dB to=0.8s +350]5.8日から[♪pop -6dB -50]1.3日へ。[>#k_take -200][>#k_loop -50][♪note -6dB -200]2週目から、[>#k_arrow -100][>#k_arrow_h +450][>#k_slope +250][♪marker -8dB to=0.8s]坂を下り始めます。[silence:+0.2s]

# patterns — 「4つ」で札を 4 枚・型の名の語で札が浮き (前の札は戻る)・人数の語で数・赤い丸・発言・12 マスを型の色に
*** patterns
se swish -10dB
se tape -8dB +300
@n: [silence:0.5s][!#grid to,{x:-384, duration:.9, ease:'power3.inOut'} -450][!#hdr.hl to,{x:157, duration:.55, ease:'back.inOut'} -400][!#bt4.t{hl} marker +120]やめ方は、[>#pc1 -200][>#pc2 -70][>#pc3 +60][>#pc4 +190][♪note -6dB -150][♪note -8dB +250]4つの型に分かれました。
@: 最も多いのは『[!#pc1 to,{y:-9, scale:1.035, duration:.35, ease:'power2.out'} -250][♪blip -8dB]入力疲れ』で[>#pc1.ct -80][>#pc1.loop +50][>#pc1.ds +250][>#pc1.qt +350][!#pba[*] fill,$yel,duration=250 stagger=50][♪pop -6dB]5人。[♪note -6dB]毎回の打ち込みが続かない。
@: [>#pc2.ds]カテゴリ選びで止まる『[!#pc1 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -300][!#pc2 to,{y:-9, scale:1.035, duration:.35, ease:'power2.out'} -250][♪blip -8dB]分類迷子』が[>#pc2.ct -80][>#pc2.loop +50][>#pc2.qt +350][!#pbb[*] fill,$blu,duration=250 stagger=50][♪pop -6dB]3人。
@: [>#pc3.ds]予算超過の赤い表示がつらい『[!#pc2 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -300][!#pc3 to,{y:-9, scale:1.035, duration:.35, ease:'power2.out'} -250][♪blip -8dB]見て落ち込む』が[>#pc3.ct -80][>#pc3.loop +50][>#pc3.qt +350][!#pbc[*] fill,$pnk,duration=250 stagger=50][♪pop -6dB]2人。
@: [>#pc4.ds]目標を達成した『[!#pc3 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -300][!#pc4 to,{y:-9, scale:1.035, duration:.35, ease:'power2.out'} -250][♪blip -8dB]用済み』も[>#pc4.ct -80][>#pc4.loop +50][>#pc4.qt +350][!#pbd[*] fill,$lav,duration=250 stagger=50][>#p_leg +500][!#pc4 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} +700][♪pop -6dB]2人です。[silence:+0.25s]

# compare — 「違う」で 2 列の見出し・行の頭で行の題・数の語で点・棒・値・最後の文で発言の付箋と赤い消し線・緑の下線
*** compare
se swish -10dB
se tape -8dB +300
@n: [silence:0.5s][!#grid to,{x:-480, duration:.9, ease:'power3.inOut'} -450][!#hdr.hl to,{x:236, duration:.55, ease:'back.inOut'} -400][!#bt5.t{hl} marker +120]続けている6人とは、何が[>#c_h1 -250][>#c_h2 -100][♪note -6dB -200]違うのか。
@: [>#c_l1 -100][♪marker -8dB to=0.8s]自動連携を使う人は[>#c_d1[*] -150][>#c_v1 +200][♪pop -6dB]6人中5人、やめた人は[>#c_q1[*] -150][>#c_w1 +250][♪pop -6dB]12人中3人。
@: [>#c_l2 -100]使うカテゴリは[>#c_b2a -200][>#c_v2a +50][♪marker -8dB to=0.8s]8個と[>#c_b2b -200][>#c_v2b +150][♪marker -8dB to=0.8s]19個。[>#c_l3 -150]入力時間は、1日[>#c_b3a -200][>#c_v3a +50][♪marker -8dB to=0.8s]1分と[>#c_b3b -200][>#c_v3b +120][♪marker -8dB to=0.8s]4分。
@: [>#c_l4 -100]週1回のふり返りは、[>#c_d4[*] -150][>#c_v4 +200][♪pop -6dB]6人全員と、[>#c_q4[*] -150][>#c_w4 +250][♪pop -6dB]12人中2人。
@: [>#c_quote -100][♪note -6dB -100]そして続く人の6人中5人が、『[>#c_quote.x -350][>#c_quote.u +100][♪marker -8dB to=0.8s -350]だいたい合っていればいい』と[♪ding -6dB]言います。[silence:+0.3s]

# moments — 頭で波の道を描き段階の札・「3日以上」「初めて」で谷に丸と稲妻と札・人数の語で数と四角と理由・「11人」で橙の付箋
*** moments
se swish -10dB
se tape -8dB +300
se marker -8dB to=0.8s +550
@n: [silence:0.5s][!#grid to,{x:-576, duration:.9, ease:'power3.inOut'} -450][!#hdr.hl to,{x:315, duration:.55, ease:'back.inOut'} -400][!#bt6.t{hl} marker +120]離脱は、ジャーニーの2つの瞬間に集まっていました。
@: [>#j_loop1 -200][>#j_bolt1][>#mc1 -100][♪note -6dB -150]3日以上ためた後の再開で[>#mc1.nn -100][>#mc1.chips[*]][>#mc1.brk +400][>#mc1.why +600][♪pop -6dB]7人。[>#j_loop2 -200][>#j_bolt2][>#mc2 -100][♪note -6dB -150]初めて予算を超えた月の通知で[>#mc2.nn -100][>#mc2.chips[*]][>#mc2.brk +400][>#mc2.why +600][>#mc2.who +600][>#j_rest +850][♪pop -6dB][♪peta -6dB +850]4人。
@: 12人のうち[>#j11 -350][♪note -6dB -300][♪ding -6dB +100]11人が、このどちらかの直後にやめています。[silence:+0.2s]

# opps — 「3つ」で札を 3 枚・各文の頭で札が浮き題を拭き出してラフの図・箇条・由来・「8個」でカテゴリの札・「予算超過」で赤い ×・「来月」で調整案
*** opps
se swish -10dB
se tape -8dB +300
@n: [silence:0.5s][!#grid to,{x:-672, duration:.9, ease:'power3.inOut'} -450][!#hdr.hl to,{x:393, duration:.55, ease:'back.inOut'} -400][!#bt7.t{hl} marker +120]だから、機会は[>#oc1 -250][>#oc2 -100][>#oc3 +50][♪note -6dB -200][♪note -8dB +100]3つ。[silence:+0.05s]
@: [!#oc1 to,{y:-8, scale:1.025, duration:.35, ease:'power2.out'} -200][>#oc1.tt -50][>#oc1.sk +150][>#oc1.li1 +900][>#oc1.li2 +1250][>#oc1.for +1600][♪marker -8dB to=0.8s +100]ためても戻れる。だいたいの金額でまとめて入れ、未分類でもいい。
@: [!#oc1 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -250][!#oc2 to,{y:-8, scale:1.025, duration:.35, ease:'power2.out'} -200][>#oc2.tt -50][>#oc2.li1 +900][>#oc2.li2 +1250][>#oc2.for +1600][♪marker -8dB to=0.8s +100]分類は後で、少なく。最初は[>#oc2.chip[*] -150][>#oc2.sk +300][♪pop -6dB]8個、分け方はアプリが[♪blip -8dB]提案。
@: [!#oc2 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} -250][!#oc3 to,{y:-8, scale:1.025, duration:.35, ease:'power2.out'} -200][>#oc3.tt -50][>#oc3.sk +150][>#oc3.li1 +900][>#oc3.for +1600][♪marker -8dB to=0.8s +100]そして、責めない表示。[>#o_x1 +100][>#o_x2 +350]予算超過は、[>#oc3.sk2 -100][!#oc3 to,{y:0, scale:1, duration:.4, ease:'power2.inOut'} +1700][♪ding -6dB]来月の調整案として見せる。[silence:+0.5s]

# concl — 文の頭で帯の付箋を 1 枚ずつ (題を拭き出し・要の語に赤い下線・補足)・要の語で赤いチェック・最後に署名の付箋
*** concl
se swish -10dB
se tape -8dB +300
@n: [silence:0.5s][!#grid to,{x:-768, duration:.9, ease:'power3.inOut'} -450][!#hdr.hl to,{x:472, duration:.55, ease:'back.inOut'} -400][!#bt8.t{hl} marker +120][>#cs1 -150][>#cs1.u +750][>#cs1.s +700][♪note -6dB -150]やめる人の半分以上は、最初の{1か月|いっかげつ}。記録は[>#ck[1] +150][♪check -4dB +200]2週目から減り始めます。
@: [>#cs2 -150][>#cs2.u +750][>#cs2.s +700][♪note -6dB -150]離脱は2つの瞬間に集まる。[>#ck[2] +150][♪check -4dB]機能より、その瞬間の体験を直しましょう。
@: [>#cs3 -150][>#cs3.u +750][>#cs3.s +700][♪note -6dB -150]続く人は『だいたいでいい』。[>#ck[3] +150][>#e_sign +3050][♪check -4dB][♪ding -6dB +3100]正確さを求める設計が、離脱を生んでいます。[silence:2.7s]
```

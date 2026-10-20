# data · pricing-ab-test (hf 全力版の全量の写し — 料金ページの A/B テスト、年額を先に見せたら・暗い紺の地に板と図を場面ごとに組む 9 場面のデータ図解) — canvas 1280x720

見せる作り: 全編の地 (紺の放射の光 + 漂う方眼 + 周辺減光 + 字幕の下の暗い帯) と 2 場面目から常設の上端の帯 (社名・題・期間・全編で伸びる進行・場面ごとに入れ替わる右上の章札)・題の絵が寄りながら明け mask から上がる 2 行と数え上げの 3 つの数字・場面 = 板 1〜2 枚 + 右の結論の小板・数字の語で伸びる図 (12 マスの料金と点線の 2 マス・3 案の画面の模型と語で光る縁・信頼区間の横線と 0 をまたぐ差の区間・左から描く 2 本の折れ線と面・積み上げの帯・2 組の縦棒と数え上げ・横棒と吹き出し・1 件 1 マスの絵グラフ・返金前の点線の枠を残して縮む横棒)・A/B/C の色を全編で通す・結論は絵の上に色の線の札 3 枚を語ごとに上げて暗転・字幕は地なしの白い字・音の層 (場面の境の風切り + 語に結んだ効果音 50)

```design.txt
#v2
# 学ぶ作り: 暗い data の design system を根に 1 回 (palette・書体 4 つ・板 board / 結論の小板 callout の def・A/B/C の色札 chip と行の札 rowlab・右上の章札 sec) → 場面は板の中身だけ
# 常設の層: 全編の地 (紺の放射の光 2 つ + 漂う方眼 + 周辺減光 + 字幕の下の暗い帯)・2 場面目から sticky の上端の帯 (社名・題・期間・全編で伸びる進行) と、場面ごとに入れ替わる右上の章札
# 図は台詞の数字の語で伸ばす: 12 マスの料金・3 案の画面の模型・信頼区間の横線・週ごとの折れ線と面・積み上げの帯・縦棒・横棒・1 件 1 マスの絵グラフ・返金前の点線の枠。A/B/C の色 (灰・青緑・暗い灰) を全編で通す
# hf d05 pricing-ab-test (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の退場は section の out (上へ抜けて消える)・切替は書かない (地は常設なので素の切替)
canvas 1280x720 bg=#060A11
theme dark
palette tx=#EAF0F6 tx2=#A9B6C4 tx3=#8593A5 line=#94A3B824 line2=#94A3B847 amber=#F5B544 blue=#5B8DEF cyan=#3DD9EB va=#94A3B8 vc=#5F6E83 rose=#FF6B81 ink=#0A0F16 a=#3DD9EB b=#F5B544
font "クリーンでモダンなサンセリフの日本語ゴシック体、バランスの良いかなと漢字に設計された欧文と数字、端正で中立で読みやすく技術系の資料や字幕向け"
fonts m="クリーンでモダンなサンセリフの日本語ゴシック体、バランスの良いかなと漢字に設計された欧文と数字、端正で中立で読みやすく技術系の資料や字幕向け、標準の太さ"
fonts b="クリーンでモダンなサンセリフの日本語ゴシック体、バランスの良いかなと漢字に設計された欧文と数字、端正で中立で読みやすく技術系の資料や字幕向け、太字"
fonts c="工業的でクリーンな等幅の欧文書体、設計された字形と鋭い線、ゼロに点、技術的で合理的な開発者向けの印象、プログラミング解説やデータのインフォグラフィック向け"
sfx off
# hf の作り: 板の中の小札・軸・凡例・注記・数の補足は 1080 で 18〜24 px の小さな字 (small_text)・板の題と結論の札の題は台詞より先に出る (spoiler)・図だけの場面 (text_only_cut)
# hf の作り: A/B/C の色札が縦に 3 枚並ぶ行の札 (stacked_labels)・C の模型と帯は枠を先に置き、語で中身を入れる (empty_board)・注記は場面の末尾 1〜2 秒だけ (flash_text)
# hf の作り: 図の色 (グラデの端・半透明の地・薄い線) は場面ごとに直書き (palette_drift)・結論の 1 場面は 17 秒 1 枚の絵 (same_picture)・頭の 5 秒に効果音が 9 回 (se_dense)
lint off=small_text,spoiler,text_only_cut,stacked_labels,empty_board,flash_text,palette_drift,same_picture,se_dense
run cy = color=$cyan
run ro = color=$rose
run am = color=$amber
run bl = color=$blue
run va = color=$va
run w = color=$tx font=m
run u = size=20 color=$tx2 font=c
run s15 = size=15 color=$tx2
run s14 = size=14 color=$tx2
run s13 = size=13 color=$tx3
run pt = size=29 color=$tx2 font=m
run pt16 = size=16
run pb = size=27 color=$tx font=b
run b17 = size=17 color=$tx font=b
run yn = size=12 font=m
run mb = size=19 font=b
run ar27 = size=27 color=$tx3
run u17 = size=17 color=$tx2
sound whoosh = "短く鋭いエフェクトのかかったビジネス系のシュッという風切り音、動画の頭"
sound whoosh2 = "短いビジネス系のシュッという風切り音、場面の切り替わり"
sound pop = "ポコッという軽く丸い短い音"
sound tick = "高めの短いビジネス系の電子音、チッと鳴る小さな合図"
sound click = "システムの選択音、短く澄んだクリック"
sound bell = "低めのビジネス系の短い電子のベル、要の数字が出る"
sound chime = "低めのビジネス系の落ち着いたチャイム、結論の合図"
sound rise = "上昇していく短い電子音、伸びていく感じ"
sound burst = "短く弾けるバーストの効果音、強い否定"
sound tension = "低めのビジネス系の緊張感のある電子音、注意を促す"
sound blip = "高めのビジネス系の電子音、ピコッと上がる気づきの合図"
svg dots = """<svg viewBox="0 0 34 22"><circle cx="4" cy="17" r="3" fill="#f5b544"/><circle cx="14" cy="12" r="3" fill="#c9c47f"/><circle cx="24" cy="8" r="3" fill="#7fd0c6"/><circle cx="31" cy="4" r="2.5" fill="#3dd9eb"/></svg>"""
p { color: $tx; line-height: 1.2 }
div { border-radius: 0px; background: none; padding: 0px; border: none; box-shadow: none }
# 字幕: 下端中央に地なしの白い字 + 濃い影 (下の暗い帯の上)・句末の約物は外す・声の 0.08 秒前に出て声と同時に消える
subtitle(left: 93px; top: 638px; width: 1093px; height: 50px; font-size: 22px; font-family: m; line-height: 1.2; letter-spacing: 0.03em; color: #E6EDF4; text-shadow: 0px 1px 9px #000000E6; background: none; border: none; box-shadow: none; text-align: center; align-items: center; unit: sentence; strip: 、。; lead: 80; tail: 0; hold: off; in: {y:7, opacity:0, duration:0.2, ease:'power2.out'}; out: {opacity:0, duration:0.14, ease:'power1.in'})
# 曲: 最後の 2.7 秒だけ前に出してから消える (hf は同じ曲の末尾を大きめの音量で重ねる)
bgm#music(fade: 1200,2200; keys: "end-2.7s:0|end-1.8s:+4") 知的で落ち着いたサイエンス系のシンセとピアノの曲、軽いビートと柔らかいパッド、データや研究の解説向け、主旋律は控えめ

# 板: 紺の縦グラデ + 細い縁 + 深い影・頭の行 (等幅の小札「01 ／ 前提」 + 25 px の題 + 補足) と下の罫・場面の頭から 0.2 秒で下から上がる
def board(k, t, s="") = div(border-radius: 15px; background: linear(#151F2FEB,#0B111BF0,180); border: 1px solid $line; box-shadow: 0px 27px 60px #00000080; delay: 200; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  p#k(left: 29px; top: 19px; font-size: 13px; font-family: c; letter-spacing: 0.14em; color: $tx3; white-space: nowrap; content: {k})
  p#t(left: 29px; top: 40px; font-size: 25px; font-family: m; letter-spacing: 0.01em; white-space: nowrap; content: {t})
  p#s(left: .t.right+11; top: 49px; font-size: 15px; color: $tx2; white-space: nowrap; content: {s})
  div#hr(left: 29px; right: 29px; top: 81px; height: 1px; background: $line)
# 板の右の結論の小板 (暗い半透明の地 + 縁)
def callout = div(border-radius: 13px; background: #060A118C; border: 1px solid $line2; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
# 等幅の小札 (板の中の前置き)
def kick = p(font-size: 13px; font-family: c; letter-spacing: 0.14em; color: $tx3; white-space: nowrap)
# A/B/C の色札 (A = 灰・B = 青緑・C = 暗い灰に白字)
def chip(t, c=$va, ink=$ink) = p(width: 31px; font-size: 17px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 8px; padding: 7px 0px; content: {t})
# 行の札 (色札 + 名 + 等幅の補足)
def rowlab(ch, nm, sb, c=$va, ink=$ink) = div(left: 29px; width: 250px; height: 40px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
  p#c(left: 0px; cy: 50%; width: 31px; font-size: 17px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 8px; padding: 7px 0px; content: {ch})
  p#nm(left: 42px; top: 0px; font-size: 17px; font-family: m; white-space: nowrap; content: {nm})
  p#sb(left: 42px; top: 23px; font-size: 13px; font-family: c; color: $tx3; white-space: nowrap; content: {sb})
# 行の札 (色札 + 名だけ)
def rowlab2(ch, nm, c=$va, ink=$ink) = div(left: 29px; width: 160px; height: 31px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
  p#c(left: 0px; cy: 50%; width: 31px; font-size: 17px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 8px; padding: 7px 0px; content: {ch})
  p#nm(left: 42px; cy: 50%; font-size: 17px; font-family: m; white-space: nowrap; content: {nm})
# 右上の章札 (青緑の番号 + 題)・場面の頭に下から入り、場面の終わりに上へ抜ける
def sec = p(right: 64px; cy: 37px; font-size: 13px; font-family: c; letter-spacing: 0.06em; white-space: nowrap; z-index: front; delay: 100; in: {y:7, opacity:0, duration:0.4, ease:'power2.out'}; out: {y:-7, opacity:0, duration:0.3, ease:'power2.in'})
# 信頼区間の横線 (両端に縦の小さな棒・中心から伸びる)
def ci(c) = div(height: 5px; border-radius: 3px; background: {c}; in: {scaleX:0, duration:0.7, ease:'power3.out'})
  div#l(left: 0px; cy: 50%; width: 2px; height: 16px; border-radius: 1px; background: {c})
  div#r(right: 0px; cy: 50%; width: 2px; height: 16px; border-radius: 1px; background: {c})
# 3 案の画面の模型 (料金の切り替えタブ + 価格 + 行 2 本 + ボタン)
def mockp(on, off, pr, c, ink) = div(width: 197px; height: 175px; border-radius: 9px; background: #0B121D; border: 1px solid #94A3B82E)
  div#bar(left: 1px; top: 1px; width: 195px; height: 17px; border-radius: 8,8,0,0; background: #94A3B814)
  shape#dot.ellipse(left: "8;17;26"; top: 7px; width: 5px; height: 5px; background: #94A3B859) ×3
  div#seg(left: 32px; top: 29px; width: 133px; height: 27px; border-radius: 99px; background: #94A3B81F)
    p#on(left: 3px; cy: 50%; width: 63px; font-size: 12px; font-family: m; line-height: 1.75; text-align: center; color: {ink}; background: {c}; border-radius: 99px; content: {on})
    p#off(left: 67px; cy: 50%; width: 63px; font-size: 12px; line-height: 1.75; text-align: center; color: $tx3; content: {off})
  p#pr(cx: 50%; top: 64px; font-size: 14px; color: $tx2; white-space: nowrap; content: {pr})
  div#l1(cx: 50%; top: 108px; width: 138px; height: 6px; border-radius: 3px; background: #94A3B829)
  div#l2(cx: 50%; top: 122px; width: 102px; height: 6px; border-radius: 3px; background: #94A3B829)
  div#cta(left: 23px; top: 140px; width: 151px; height: 20px; border-radius: 5px; background: {c})
# 3 案の札 (色札 + 題 + 補足 + 模型 + 訪問の人数)・語で縁が光る
def vcard(ch, tl, sb, n, c=$va, ink=$ink, gc=$va, gs=#94A3B840) = div(top: 139px; width: 229px; height: 347px; border-radius: 13px; background: linear(#151F2FEB,#0B111BF0,180); border: 1px solid $line; box-shadow: 0px 20px 47px #00000073; in: {y:27, opacity:0, duration:0.6, ease:'power3.out'})
  div#glow(left: 0px; top: 0px; width: 229px; height: 347px; border-radius: 13px; border: 1px solid {gc}; box-shadow: 0px 0px 27px {gs}; in: {opacity:0, duration:0.3}; out: {opacity:0, duration:0.3})
  p#ch(left: 19px; top: 17px; width: 31px; font-size: 17px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 8px; padding: 7px 0px; content: {ch})
  p#tl(left: 19px; top: 61px; font-size: 19px; font-family: m; white-space: nowrap; content: {tl})
  p#sb(left: 19px; top: 89px; font-size: 13px; color: $tx3; white-space: nowrap; content: {sb})
  p#fl(left: 19px; bottom: 17px; font-size: 13px; color: $tx3) 訪問
  p#fn(right: 19px; bottom: 15px; font-size: 20px; font-family: m; white-space: nowrap; content: {n})
# 折れ線の点 (縁取りの丸 + 値)・ポンと出る
def pt(v, c, lc, ly, lx=8) = div(width: 16px; height: 16px; in: {scale:0.3, opacity:0, duration:0.5, ease:'back.out(2)'})
  shape#d.ellipse(left: 0px; top: 0px; width: 16px; height: 16px; background: {c}; border: 3px solid #0B121D)
  p#v(cx: {lx}; cy: {ly}; font-size: 15px; font-family: b; color: {lc}; white-space: nowrap; content: {v})
# 結論の札 (上端の色の線 + 番号 + 色の札 + 2 行の題 + 罫)
def ccard(n, l, h, c) = div(top: 200px; width: 371px; height: 373px; border-radius: 15px; background: linear(#151F2FF0,#0B111BF5,180); border: 1px solid $line; box-shadow: 0px 27px 60px #0000008C; in: {y:27, opacity:0, duration:0.7, ease:'power3.out'})
  div#top(left: 9px; top: 0px; width: 353px; height: 3px; border-radius: 2px; background: {c})
  p#no(left: 24px; top: 27px; font-size: 15px; font-family: c; letter-spacing: 0.12em; color: $tx3; content: {n})
  p#lb(left: 24px; top: 53px; font-size: 15px; font-family: b; color: $ink; background: {c}; border-radius: 99px; padding: 4px 11px; content: {l})
  p#hd(left: 24px; top: 95px; font-size: 24px; font-family: b; line-height: 1.34; white-space: nowrap; content: {h})
  div#dv(left: 24px; top: 179px; width: 323px; height: 1px; background: $line2)
# 結論の札の行 (色の点 + 文・語の頭で下から上がる)
def li(t, c) = div(left: 24px; width: 330px; height: 24px; in: {y:8, opacity:0, duration:0.45, ease:'power3.out'})
  shape#d.ellipse(left: 1px; top: 10px; width: 5px; height: 5px; background: {c})
  p#t(left: 16px; top: 0px; font-size: 16px; line-height: 1.5; color: $tx2; white-space: nowrap; content: {t})

# 全編の地 (根): 紺の地に右上と左下の放射の光・方眼が全編で右下へ 32 / 16 px 漂う・周辺減光・字幕の下の暗い帯
veil#glow1(background: radial(#142540,#14254000@70%,72%,0%); z-index: back; in: none)
veil#glow2(background: radial(#0F1D30,#0F1D3000@70%,0%,100%); z-index: back; in: none)
div#grid.bleed(left: -64px; top: -64px; width: 1408px; height: 848px; pattern: grid,32,#94A3B80E; mask-image: radial-gradient(ellipse 72% 62% at 50% 46%, #000 25%, transparent 100%); z-index: back; in: none; main: ramp,x=32,y=16)
veil#vig(background: radial(#00000000@55%,#00000099,50%,45%); z-index: back; in: none)
div#capband(left: 0px; top: 607px; width: 1280px; height: 113px; background: linear(#060A1100,#060A11DB@70%,180); z-index: front; in: none)

# title 題: 料金ページの絵が 1.12 → 1 に寄りながら明け、左の暗い空きに小札 → mask から上がる 2 行 → 架空の社名 → 3 つの数字 (訪問者は数え上げ)
section#title(stagger: {each:0}; out: {y:-9, opacity:0, blur:5, duration:0.32, ease:'power2.in'})
img#hero(inset: 0; subject: right 45%; room: left 50%; main: keys(at=0 scale=1.12 opacity=0 | at=0.197 scale=1 opacity=1 ease=power2.out | at=1 scale=0.97 ease=none),duration=8118,pivot=72%,45%; in: none; out: {y:-9, opacity:0, blur:5, duration:0.32, ease:'power2.in'}) [photo]暗い紺の空間に浮かぶ SaaS の料金ページ。半透明のガラスの料金プランのカード 2 枚が横に並び、その上に光るトグルスイッチが 1 つ。左のカードは暖かい琥珀の光、右のカードは冷たい青みの光、縁に青緑の光、柔らかい靄、浅い被写界深度。カードとスイッチは画面の右半分 (中心は横 70%) に置き、左半分はほぼ真っ暗な空き (題の文字の場所)、下の 2 割は暗い床の反射。ミニマルで上質な技術の雰囲気、文字・数字・ロゴ・UI の表記なし
div#shade_l(inset: 0; background: linear(#060A11F7,#060A11DB@36%,#060A114D@58%,#060A1100@74%,90); in: none; out: {y:-9, opacity:0, blur:5, duration:0.32, ease:'power2.in'})
div#shade_b(inset: 0; background: linear(#060A1100@68%,#060A11E6,180); in: none; out: {y:-9, opacity:0, blur:5, duration:0.32, ease:'power2.in'})
div#kk(left: 80px; top: 143px; width: 640px; height: 25px; delay: 300; in: {y:12, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 35px; height: 2px; background: $amber)
  p#t(left: 45px; cy: 50%; font-size: 21px; font-family: m; letter-spacing: 0.06em; color: $amber; white-space: nowrap) 料金ページの A/B テスト
p#l1(left: 80px; top: 184px; font-size: 92px; font-family: b; line-height: 1.1; white-space: nowrap; delay: 450; in: {y:111, duration:0.9, ease:'power4.out', clip:true}) {am}年額{/}を
p#l2(left: 80px; top: 290px; font-size: 92px; font-family: b; line-height: 1.1; white-space: nowrap; delay: 610; in: {y:111, duration:0.9, ease:'power4.out', clip:true}) 先に見せたら
p#sub(left: 80px; top: 422px; font-size: 21px; color: $tx2; white-space: nowrap; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'}) 架空のタスク管理 SaaS「ノートレイル」
# 3 つの数字 (2・3 つ目は左に細い縦線)
div#st(left: "80;313;497"; top: 479px; width: "233;184;220"; height: 78px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out', stagger: {each: 0.18}}) ×3
  div#sep(left: 0px; top: 0px; width: 1px; height: 78px; background: $line2; opacity: "0;1;1")
  p#k(left: "0;29;29"; top: 8px; font-size: 13px; letter-spacing: 0.12em; color: $tx3) 期間;比較;訪問者
  p#v(left: "0;29;29"; cy: 53px; font-size: 31px; font-family: m; white-space: nowrap) 9/1〜9/28{s15} 4 週間{/};3 案{s15} A・B・C{/};[count:38,440 start=0 ms=1100]{s15} 人{/}

# setup 前提: 上端の帯が明ける・左の板に月額と年額 (12 マスのうち 2 マスが点線 = 2 か月分お得)・右に 3 案の画面の模型が並び、案の名の語で縁が順に光る
section#setup(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.32, ease:'power2.in'})
# 上端の帯 (sticky・最後まで): 点の印・社名・題・期間と、全編で伸びる進行の線
div#hud.sticky(left: 0px; top: 0px; width: 1280px; height: 72px; z-index: front; in: {opacity:0, duration:0.6, ease:'power1.out'})
  svg#logo(left: 64px; cy: 37px; width: 23px; height: 15px; part: dots)
  p#brand(left: 97px; cy: 37px; font-size: 15px; font-family: m; letter-spacing: 0.04em; white-space: nowrap) ノートレイル
  div#sep(left: .brand.right+11; cy: 37px; width: 1px; height: 13px; background: $line2)
  p#sub(left: .sep.right+11; cy: 37px; font-size: 15px; color: $tx2; white-space: nowrap) 料金ページの A/B テスト
  p#period(right: 219px; cy: 37px; font-size: 13px; font-family: c; letter-spacing: 0.06em; color: $tx3; white-space: nowrap) 9/1–9/28 · 訪問 38,440 人
  div#track(left: 64px; top: 61px; width: 1152px; height: 1px; background: #94A3B81F)
progress#prog.sticky(left: 64px; top: 61px; width: 1152px; height: 1px; background: linear($cyan,$amber,90); until: end; z-index: front; overlap: hud)
sec#sec2 {cy}01{/} 前提
board#price(left: 64px; top: 93px; width: 407px; height: 507px; k: "{cy}01{/} ／ 前提"; t: "料金プラン")
  div#m(left: 29px; top: 107px; width: 349px; height: 100px)
    p#pl(left: 0px; top: 0px; font-size: 15px; font-family: m; color: $ink; background: $blue; border-radius: 99px; padding: 4px 11px) 月額プラン
    p#v(left: 0px; top: 35px; font-size: 61px; font-family: b; line-height: 1; letter-spacing: -0.01em; white-space: nowrap) 4,980{u} 円 / 月{/}
  div#y(left: 29px; top: 227px; width: 349px; height: 140px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
    p#pl(left: 0px; top: 0px; font-size: 15px; font-family: m; color: $ink; background: $amber; border-radius: 99px; padding: 4px 11px) 年額プラン
    p#v(left: 0px; top: 35px; font-size: 61px; font-family: b; line-height: 1; letter-spacing: -0.01em; white-space: nowrap) 49,800{u} 円 / 年{/}
    p#n(left: 0px; top: 112px; font-size: 15px; color: $amber; white-space: nowrap) ＝ 月額の 10 か月分
  # 12 マス (払う 10 マスは琥珀・お得の 2 マスは点線) と下のかぎ
  div#mo(left: 29px; top: 381px; width: 349px; height: 100px)
    p#lab(left: 0px; top: 0px; font-size: 14px; color: $tx2; white-space: nowrap; in: {opacity:0, duration:0.5}) 12 か月使えて、払うのは 10 か月分
    div#pay(left: "0;29;58;87;116;145;174;203;232;261"; top: 28px; width: 23px; height: 23px; border-radius: 5px; background: $amber; in: {scale:0.3, opacity:0, duration:0.35, ease:'back.out(2)', stagger: {each: 0.05}}) ×10
    shape#free(left: "290;319"; top: 28px; width: 23px; height: 23px; path: rect,r=0.22; background: #F5B54714; border: 1px solid $amber; dash: 3,3; in: {scale:0.3, opacity:0, duration:0.45, ease:'back.out(2)', stagger: {each: 0.08}}) ×2
    div#fl(left: 287px; top: 61px; width: 51px; height: 30px; in: {y:-5, opacity:0, duration:0.45, ease:'back.out(2)'})
      shape#brk(path: "M0 0 L0 9 L51 9 L51 0"; background: none; border: 1px solid $amber)
      p#t(cx: 50%; top: 13px; font-size: 15px; font-family: b; color: $amber; white-space: nowrap) 2 か月分お得
p#vh(left: 493px; top: 97px; font-size: 23px; font-family: m; white-space: nowrap; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'}) 3 つの案　{s15}訪問者をランダムに振り分け{/}
vcard#ca(left: 493px; ch: A; tl: 月額を先に表示; sb: 現行の料金ページ; n: "[count:12,840 start=0 ms=900 delay=1470]{s13} 人{/}")
  p#tag(left: 58px; top: 20px; font-size: 12px; color: $tx2; border: 1px solid $line2; border-radius: 99px; padding: 2px 8px) 現行
  mockp#mock(left: 16px; top: 117px; on: 月額; off: 年額; pr: "{pb}4,980{/}円 / 月"; c: $blue; ink: "#08101C")
vcard#cb(left: 740px; ch: B; tl: 年額を先に表示; sb: 月額は切り替えタブ; n: "[count:12,810 start=0 ms=900 delay=1420]{s13} 人{/}"; c: $cyan; gc: $cyan; gs: "#3DD9EB59")
  mockp#mock(left: 16px; top: 117px; on: 年額; off: 月額; pr: "{pb}49,800{/}円 / 年"; c: $amber; ink: "#1C1306")
vcard#cc(left: 987px; ch: C; tl: 3 段の比較表; sb: 月額・年額・チーム向け; n: "[count:12,790 start=0 ms=900 delay=1370]{s13} 人{/}"; c: "#526076"; ink: "#F4F7FA"; gc: "#8796AB")
  # C の模型: 3 段の比較表 (月額・年額・チームの列)・「C は」の語で列が順に弾む
  div#mock(left: 16px; top: 117px; width: 197px; height: 175px; border-radius: 9px; background: #0B121D; border: 1px solid #94A3B82E)
    div#bar(left: 1px; top: 1px; width: 195px; height: 17px; border-radius: 8,8,0,0; background: #94A3B814)
    shape#dot.ellipse(left: "8;17;26"; top: 7px; width: 5px; height: 5px; background: #94A3B859) ×3
    div#col(left: "8;70;132"; top: 29px; width: 57px; height: 100px; border-radius: 7px; border: 1px solid #94A3B833; in: {scale:0.8, opacity:0, duration:0.5, ease:'back.out(2)', stagger: {each: 0.08}}) ×3
      p#h(cx: 50%; top: 7px; font-size: 11px; font-family: m; color: $tx2) 月額;年額;チーム
      div#p(left: 4px; top: 28px; width: 49px; height: 15px; border-radius: 3px; background: "#5B8DEF8C;#F5B54799;#94A3B838")
      div#l1(left: 3px; top: 50px; width: 51px; height: 5px; border-radius: 3px; background: #94A3B81F)
      div#l2(left: 3px; top: 62px; width: 51px; height: 5px; border-radius: 3px; background: #94A3B81F)
      div#b(left: 4px; top: 78px; width: 49px; height: 13px; border-radius: 4px; background: #94A3B84D)
# 期間・振り分け・合計の帯 (合計は数え上げ)
div#info(left: 493px; top: 507px; width: 723px; height: 80px; border-radius: 12px; border: 1px solid $line; background: #0D141FCC; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
  p#k(left: "24;279;507"; top: 16px; font-size: 13px; letter-spacing: 0.1em; color: $tx3; white-space: nowrap) ×3 期間;振り分け;訪問者 合計
  p#v(left: "24;279;507"; top: 35px; font-size: 24px; font-family: m; white-space: nowrap) ×3 9/1〜9/28{s14} 4 週間{/};ランダム{s14} 3 案に振り分け{/};[count:38,440 start=0 ms=1000 delay=200]{s14} 人{/}
  div#vl(left: "253;481"; top: 17px; width: 1px; height: 45px; background: $line2) ×2

# conv 転換率: 6 本の目盛りの上に A・B・C の推定値 (点) と 95% 信頼区間 (横線) を語で伸ばす → 右の小板で差 +0.34 を数え、差の区間が 0 をまたぐ所で赤い判定の札
section#conv(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec3 {cy}02{/} 転換率
board#cv(left: 64px; top: 93px; width: 1152px; height: 513px; k: "{cy}02{/} ／ 転換率"; t: "有料転換率"; s: "訪問から 14 日以内の課金")
  div#hr(right: 373px)
  shape#lg_dot.ellipse(left: 584px; top: 52px; width: 12px; height: 12px; background: $tx)
  p#lg1(left: 603px; cy: 58px; font-size: 14px; color: $tx2; white-space: nowrap) 推定値
  div#lg_ln(left: 664px; cy: 58px; width: 20px; height: 3px; border-radius: 2px; background: $tx2)
  p#lg2(left: 691px; cy: 58px; font-size: 14px; color: $tx2; white-space: nowrap) 95% 信頼区間
  div#gv(left: "378;443;507;573;637;702"; top: 112px; width: 1px; height: 297px; background: #94A3B81F; delay: 250; in: {opacity:0, duration:0.6}) ×6
  p#ax(cx: "378;443;507;573;637;702"; top: 419px; font-size: 12px; font-family: c; color: $tx3; delay: 250; in: {opacity:0, duration:0.6}) ×6 2.8%;3.0%;3.2%;3.4%;3.6%;3.8%
  rowlab#la(top: 170px; ch: A; nm: 現行（月額が先）; sb: "398 / 12,840 人")
  rowlab#lb(top: 263px; ch: B; nm: 年額が先; sb: "441 / 12,810 人"; c: $cyan)
  rowlab#lc(top: 357px; ch: C; nm: 3 段の比較表; sb: "390 / 12,790 人"; c: "#526076"; ink: "#F4F7FA")
  ci#cia(left: 378px; top: 185px; width: 194px; c: "#94A3B8BF")
  ci#cib(left: 485px; top: 279px; width: 204px; c: "#3DD9EBD9")
  ci#cic(left: 362px; top: 372px; width: 194px; c: "#5F6E83F2")
  shape#da.ellipse(left: 467px; top: 180px; width: 17px; height: 17px; background: $va; border: 3px solid #0B121D; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
  shape#db.ellipse(left: 577px; top: 273px; width: 17px; height: 17px; background: $cyan; border: 3px solid #0B121D; box-shadow: 0px 0px 15px #3DD9EB99; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
  shape#dc.ellipse(left: 451px; top: 366px; width: 17px; height: 17px; background: #8A98AD; border: 3px solid #0B121D; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
  p#va(cx: 475px; top: 143px; font-size: 27px; font-family: b; white-space: nowrap; in: {y:9, opacity:0, duration:0.45, ease:'power3.out'}) 3.10%
  p#vb(cx: 585px; top: 236px; font-size: 27px; font-family: b; color: $cyan; white-space: nowrap; in: {y:9, opacity:0, duration:0.45, ease:'power3.out'}) 3.44%
  p#vc(cx: 459px; top: 329px; font-size: 27px; font-family: b; color: #B3BFCD; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.05%
  p#ca(cx: 475px; top: 201px; font-size: 12px; font-family: c; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) 2.80〜3.40%
  p#cb(cx: 585px; top: 295px; font-size: 12px; font-family: c; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.13〜3.76%
  p#cc(cx: 459px; top: 388px; font-size: 12px; font-family: c; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) 2.75〜3.35%
  # 差の小板: +0.34 pt を数え、差の区間 (白) と 0 より下の端 (赤) を伸ばし、赤い縁の判定の札が傾いて着地
  callout#df(left: 793px; top: 23px; width: 333px; height: 467px; border: 1px solid $line)
    p#l(left: 23px; top: 16px; font-size: 16px; color: $tx2; white-space: nowrap) B と A の差
    p#n(left: 20px; top: 57px; font-size: 85px; font-family: b; line-height: 1; letter-spacing: -0.02em; white-space: nowrap) +[count:0.34 start=0 ms=800 delay=150]{pt} pt{/}
    p#ci(left: 23px; top: 164px; font-size: 14px; font-family: c; color: $tx2; white-space: nowrap; in: {opacity:0, duration:0.5}) 95% 信頼区間 −0.09 〜 +0.78 pt
    div#ax(left: 0px; top: 190px; width: 333px; height: 80px; in: {opacity:0, duration:0.5})
      div#gl(left: 27px; top: 30px; width: 280px; height: 1px; background: #94A3B840)
      div#zero(left: 90px; top: 5px; width: 2px; height: 53px; border-radius: 1px; background: $tx)
      p#zl(cx: 91px; top: 63px; font-size: 12px; font-family: c; white-space: nowrap) 差 0
      p#p5(cx: 195px; top: 63px; font-size: 12px; font-family: c; color: $tx3; white-space: nowrap) +0.5
      div#tk(left: 195px; top: 23px; width: 1px; height: 13px; background: #94A3B866)
    div#dn(left: 71px; top: 217px; width: 19px; height: 7px; border-radius: 4px; background: $rose; in: {scaleX:0, duration:0.4, ease:'power2.out', pivot:'right'})
    div#dp(left: 90px; top: 217px; width: 165px; height: 7px; border-radius: 4px; background: #EAF0F6D9; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
    shape#dd.ellipse(left: 154px; top: 212px; width: 17px; height: 17px; background: $tx; border: 3px solid #0B121D; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
    div#vd(left: 20px; top: 300px; width: 293px; height: 72px; border-radius: 9px; border: 1px solid $rose; background: #FF6B8114; in: {scale:1.25, rotation:-3, opacity:0, duration:0.45, ease:'back.out(1.6)'})
      p#v1(left: 13px; top: 11px; font-size: 15px; color: $rose; opacity: 0.9; white-space: nowrap) 信頼区間がゼロをまたぐ
      p#v2(left: 13px; top: 34px; font-size: 21px; font-family: b; color: $rose; white-space: nowrap) 統計的には言い切れない
    p#nt(left: 23px; top: 403px; width: 290px; font-size: 13px; line-height: 1.5; color: $tx3; in: {opacity:0, duration:0.5}) B の転換率が A より高いとも、差がないとも断定できない

# weekly 週ごと: 方眼の上に 1 週目の 2 点と差 +0.88pt → B と A の折れ線を左から描き、週ごとの点と差の数字が順に出て面が染まる → 2 週目以降のかぎ → 右の小板に光るきらめきの絵と「物珍しさの効果？」
section#weekly(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec4 {cy}03{/} 週ごと
board#wk(left: 64px; top: 93px; width: 1152px; height: 513px; k: "{cy}03{/} ／ 週ごと"; t: "週ごとの転換率"; s: "B と A")
  div#hr(right: 400px)
  div#lg1(left: 542px; cy: 58px; width: 20px; height: 3px; border-radius: 2px; background: $cyan)
  p#lt1(left: 569px; cy: 58px; font-size: 14px; color: $tx2; white-space: nowrap) B 年額が先
  div#lg2(left: 657px; cy: 58px; width: 20px; height: 3px; border-radius: 2px; background: $va)
  p#lt2(left: 684px; cy: 58px; font-size: 14px; color: $tx2; white-space: nowrap) A 現行
  div#gh(left: 102px; top: "127;175;225;273;322;371;420"; width: 593px; height: 1px; background: "#94A3B81F;#94A3B81F;#94A3B81F;#94A3B81F;#94A3B81F;#94A3B81F;#94A3B84D"; delay: 250; in: {opacity:0, duration:0.6}) ×7
  p#yl(left: 43px; cy: "127;175;225;273;322;371;420"; width: 50px; text-align: right; font-size: 12px; font-family: c; color: #7A889A; delay: 250; in: {opacity:0, duration:0.6}) ×7 4.0%;3.8%;3.6%;3.4%;3.2%;3.0%;2.8%
  p#xl(cx: "182;329;476;622"; cy: 445px; font-size: 15px; color: $tx2; white-space: nowrap; delay: 250; in: {opacity:0, duration:0.6}) ×4 1 週目;2 週目;3 週目;4 週目
  # hf の作り: B と A の間の面は 9% の青緑 (check はこの面の上の数字を low_contrast に数えるが、面はほぼ透明で読める)
  shape#area(path: "M182 159 L329 281 L476 310 L622 303 L622 327 L476 352 L329 335 L182 374 Z"; background: #3DD9EB17; in: {opacity:0, duration:0.8})
  shape#lb(path: "M182 159 L329 281 L476 310 L622 303"; background: none; border: 3px solid $cyan; in: draw,1200)
  shape#la(path: "M182 374 L329 335 L476 352 L622 327"; background: none; border: 3px solid $va; in: draw,1200)
  shape#g1(path: "M182 168 L182 364"; background: none; border: 1px solid $cyan; dash: 3,4; in: {opacity:0, duration:0.4})
  shape#g2(path: "M329 290 L329 325"; background: none; border: 1px solid $cyan; dash: 3,3; in: {opacity:0, duration:0.5})
  shape#g3(path: "M476 319 L476 342"; background: none; border: 1px solid $cyan; dash: 3,3; in: {opacity:0, duration:0.5})
  shape#g4(path: "M622 312 L622 318"; background: none; border: 1px solid $cyan; in: {opacity:0, duration:0.5})
  pt#pb1(left: 174px; top: 151px; v: 3.87%; c: $cyan; lc: $cyan; ly: -14)
  pt#pa1(left: 174px; top: 366px; v: 2.99%; c: $va; lc: "#C3CDD9"; ly: 26)
  pt#pb2(left: 321px; top: 273px; v: 3.37%; c: $cyan; lc: $cyan; ly: -6; lx: 43)
  pt#pa2(left: 321px; top: 327px; v: 3.15%; c: $va; lc: "#C3CDD9"; ly: 26)
  pt#pb3(left: 468px; top: 302px; v: 3.25%; c: $cyan; lc: $cyan; ly: -13)
  pt#pa3(left: 468px; top: 344px; v: 3.08%; c: $va; lc: "#C3CDD9"; ly: 26)
  pt#pb4(left: 614px; top: 295px; v: 3.28%; c: $cyan; lc: $cyan; ly: -13)
  pt#pa4(left: 614px; top: 319px; v: 3.18%; c: $va; lc: "#C3CDD9"; ly: 26)
  p#gl1(cx: 256px; cy: 308px; font-size: 31px; font-family: b; color: $cyan; white-space: nowrap; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'}) +0.88{pt16}pt{/}
  p#gl2(cx: 368px; cy: 307px; font-size: 15px; font-family: b; color: #9FE9F3; white-space: nowrap; in: {opacity:0, duration:0.5}) +0.22
  p#gl3(cx: 515px; cy: 331px; font-size: 15px; font-family: b; color: #9FE9F3; white-space: nowrap; in: {opacity:0, duration:0.5}) +0.17
  p#gl4(cx: 661px; cy: 315px; font-size: 15px; font-family: b; color: #9FE9F3; white-space: nowrap; in: {opacity:0, duration:0.5}) +0.10
  shape#rb(path: "M313 460 L313 469 L660 469 L660 460"; background: none; border: 1px solid #3DD9EBB3; in: {scaleX:0.2, opacity:0, duration:0.5, ease:'power2.out'})
  p#rl(cx: 487px; top: 475px; font-size: 14px; color: $cyan; white-space: nowrap; in: {opacity:0, duration:0.5}) 2 週目以降の差は 0.1〜0.2pt
  callout#co(left: 767px; top: 23px; width: 360px; height: 467px)
    img#ic(left: 220px; top: 17px; width: 120px; height: 120px; fit: contain; box-shadow: 0px 18px 30px #00000080; main: none; in: {scale:0.4, rotation:-20, opacity:0, duration:0.7, ease:'back.out(2.2)'}) [transparent]琥珀の金色に柔らかく光る、艶のある小さな 4 つの角の星形のきらめきと、その横の小さな 2 つのきらめき。クリーンでモダンな 3D の icon の質感、柔らかなスタジオの光、中央に 1 つだけ置く。文字なし
    kick#k(left: 24px; top: 36px) 考えられること
    p#t(left: 24px; top: 64px; font-size: 27px; font-family: b; white-space: nowrap) 物珍しさの効果？
    p#b1(left: 24px; top: 157px; width: 320px; font-size: 17px; line-height: 1.6; color: $tx2) B の差は {w}1 週目が +0.88pt{/} と大きく、[br]{w}2 週目以降は 0.1〜0.2pt{/} に縮む。
    p#b2(left: 24px; top: 235px; width: 325px; font-size: 15px; line-height: 1.6; color: $tx2) 新しい見せ方への一時的な反応が、[br]1 週目の転換率に混じっている可能性がある。
    div#hr(left: 24px; top: 313px; width: 312px; height: 1px; background: $line)
    kick#k2(left: 24px; top: 333px) 1 週目
    p#r(left: 24px; top: 357px; font-size: 35px; font-family: b; color: $cyan; white-space: nowrap) 3.87%{s13} B ／ A {/}{va}2.99%{/}

# share 年額の割合: 3 本の帯が月額の青で満ち、年額の琥珀が左から伸びる → A・B の割合の札が弾み、右の小板に 22% → 41% と「倍近くに」・月額の人数 310 → 260
section#share(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec5 {cy}04{/} 年額の割合
board#sh(left: 64px; top: 93px; width: 1152px; height: 513px; k: "{cy}04{/} ／ 年額の割合"; t: "課金者のうち、年額を選んだ割合")
  div#hr(right: 373px)
  div#lq1(left: 663px; cy: 58px; width: 12px; height: 12px; border-radius: 3px; background: $amber)
  p#lt1(left: 682px; cy: 58px; font-size: 14px; color: $tx2) 年額
  div#lq2(left: 729px; cy: 58px; width: 12px; height: 12px; border-radius: 3px; background: $blue)
  p#lt2(left: 748px; cy: 58px; font-size: 14px; color: $tx2) 月額
  rowlab#la(top: 135px; ch: A; nm: 現行; sb: "課金 398 人"; delay: 250)
  rowlab#lb(top: 235px; ch: B; nm: 年額が先; sb: "課金 441 人"; c: $cyan; delay: 350)
  rowlab#lc(top: 335px; ch: C; nm: 3 段比較表; sb: "課金 390 人"; c: "#526076"; ink: "#F4F7FA"; delay: 450)
  div#tr(left: 220px; top: "124;224;324"; width: 533px; height: 56px; border-radius: 8px; background: #94A3B80F) ×3
    div#m(left: 0px; top: 0px; width: 533px; height: 56px; border-radius: 8px; background: linear(#5B8DEFBF,#5B8DEF8C,90); in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
    div#y(left: 0px; top: 0px; width: "117;219;160"; height: 56px; border-radius: 8,0,0,8; background: $amber; box-shadow: 3px 0px 12px #00000059; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
    p#yl(left: 12px; cy: 50%; font-size: 25px; font-family: b; line-height: 1.05; color: #1C1306; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 22%[br]{yn}88 人{/};41%[br]{yn}181 人{/};30%[br]{yn}117 人{/}
    p#ml(right: 15px; cy: 50%; font-size: 15px; color: #E9F0FF; white-space: nowrap; in: {opacity:0, duration:0.5}) 月額 {mb}310{/} 人;月額 {mb}260{/} 人;月額
  p#a0(left: 220px; top: 400px; font-size: 12px; font-family: c; color: $tx3) 0%
  p#a1(cx: 753px; top: 400px; font-size: 12px; font-family: c; color: $tx3) 100%
  p#nt(left: 220px; top: 433px; font-size: 13px; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) ※ 割合は各案の課金者に占める年額プランの課金者
  callout#co(left: 793px; top: 23px; width: 333px; height: 467px)
    kick#k(left: 24px; top: 27px; in: {opacity:0, duration:0.5}) 年額の割合　A → B
    p#p1(left: 24px; top: 85px; font-size: 43px; font-family: b; line-height: 1; color: $va; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 22%
    p#ar(left: .p1.right+9; top: 98px; font-size: 27px; line-height: 1; color: $tx3; in: {opacity:0, duration:0.5}) →
    p#p2(left: .ar.right+9; top: 64px; font-size: 67px; font-family: b; line-height: 1; letter-spacing: -0.02em; color: $amber; white-space: nowrap; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2)'}) 41%
    p#bd(left: 24px; top: 167px; font-size: 20px; font-family: b; color: #1C1306; background: $amber; border-radius: 99px; padding: 5px 16px; white-space: nowrap; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2)'}) 倍近くに
    div#hr(left: 24px; top: 233px; width: 285px; height: 1px; background: $line)
    div#mon(left: 24px; top: 256px; width: 290px; height: 130px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
      kick#k(left: 0px; top: 0px) 月額の課金者　A → B
      p#r(left: 0px; top: 27px; font-size: 43px; font-family: b; color: $va; white-space: nowrap) 310{u17} 人{/}{ar27} → {/}{bl}260{/}{u17} 人{/}
      p#nt(left: 0px; top: 104px; font-size: 14px; color: $tx2; white-space: nowrap) 年額へ移った分、月額の課金者は減った

# revenue 売上: 月額と年額の単価の札 → 左の縦棒 (課金者 1 人あたり・+5.9%) → 右の縦棒 (訪問者 1 人あたり・数え上げ・+17.6% の大きな札) → 下の結びの一行に琥珀の下線
section#revenue(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec6 {cy}05{/} 売上
board#rv(left: 64px; top: 93px; width: 1152px; height: 513px; k: "{cy}05{/} ／ 売上"; t: "初年度売上の推計"; s: "1 人あたり")
  div#c1(left: 29px; top: 99px; width: 364px; height: 39px; border-radius: 99px; border: 1px solid $line2; background: #060A1180; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
    p#pl(left: 7px; cy: 50%; font-size: 13px; font-family: m; color: $ink; background: $blue; border-radius: 99px; padding: 3px 9px) 月額
    p#t(left: .pl.right+9; cy: 50%; font-size: 15px; white-space: nowrap) 初年度の平均継続 7.5 か月 → {b17}37,350{/} 円
  div#c2(left: 513px; top: 99px; width: 157px; height: 39px; border-radius: 99px; border: 1px solid $line2; background: #060A1180; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
    p#pl(left: 7px; cy: 50%; font-size: 13px; font-family: m; color: $ink; background: $amber; border-radius: 99px; padding: 3px 9px) 年額
    p#t(left: .pl.right+9; cy: 50%; font-size: 15px; white-space: nowrap) {b17}49,800{/} 円
  p#lt(left: 29px; top: 157px; font-size: 17px; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) 課金者 1 人あたり{s13} 円{/}
  div#lbase(left: 29px; top: 400px; width: 507px; height: 1px; background: $line2; in: {opacity:0, duration:0.5})
  div#lb(left: "73;227;380"; top: "253;244;249"; width: 88px; height: "147;156;151"; border-radius: 8,8,3,3; background: "linear(#A6B3C4,#6F7E93,180);linear(#62E6F3,#1AA9BD,180);linear(#71819A,#4A5870,180)"; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom', stagger: {each: 0.12}}) ×3
  p#lv(cx: "117;271;424"; top: "221;212;217"; font-size: 20px; font-family: b; color: "$tx;$cyan;$tx"; white-space: nowrap; in: {opacity:0, duration:0.5, stagger: {each: 0.12}}) ×3 40,103;42,460;41,085
  p#lbd(left: 324px; top: 188px; font-size: 15px; font-family: m; color: $cyan; border: 1px solid $cyan; border-radius: 99px; padding: 3px 9px; white-space: nowrap; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'}) +5.9%
  p#lx(cx: "117;271;424"; top: 408px; width: 27px; font-size: 15px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 7px; padding: 6px 0px; in: {opacity:0, duration:0.5}) ×3 A;B;C
  div#dv(left: 576px; top: 157px; width: 1px; height: 280px; background: $line)
  p#rt(left: 616px; top: 157px; font-size: 17px; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) 訪問者 1 人あたり{s13} 円{/}
  div#rbase(left: 616px; top: 400px; width: 507px; height: 1px; background: $line2; in: {opacity:0, duration:0.5})
  div#rb(left: "660;813;967"; top: "259;234;258"; width: 88px; height: "141;166;142"; border-radius: 8,8,3,3; background: "linear(#A6B3C4,#6F7E93,180);linear(#62E6F3,#1AA9BD,180);linear(#71819A,#4A5870,180)"; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom', stagger: {each: 0.12}}) ×3
  p#rv(cx: "704;857;1011"; top: "227;202;226"; font-size: 20px; font-family: b; color: "$tx;$cyan;$tx"; white-space: nowrap; in: {opacity:0, duration:0.3}) ×3 [count:1,243 start=0 ms=800 delay=100];[count:1,462 start=0 ms=800 delay=220];[count:1,253 start=0 ms=800 delay=340]
  p#rbd(left: 915px; top: 163px; font-size: 27px; font-family: b; color: #061317; background: $cyan; border-radius: 99px; padding: 5px 15px; white-space: nowrap; in: {scale:0.4, opacity:0, duration:0.5, ease:'back.out(2)'}) +17.6%
  p#rx(cx: "704;857;1011"; top: 408px; width: 27px; font-size: 15px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 7px; padding: 6px 0px; in: {opacity:0, duration:0.5}) ×3 A;B;C
  div#bn(left: 29px; top: 455px; width: 1094px; height: 43px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
    p#a(left: 0px; cy: 50%; font-size: 21px; font-family: m; white-space: nowrap) 差を生んでいるのは、
    p#b(left: .a.right+12; cy: 50%; font-size: 17px; color: $tx3; white-space: nowrap) 転換率より
    p#c(left: .b.right+12; cy: 50%; font-size: 21px; font-family: m; color: $amber; white-space: nowrap) 「年額の割合」
    div#ul(left: .c.left; top: 36px; width: 140px; height: 3px; border-radius: 2px; background: $amber; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})

# side 副作用: 板 2 枚 (問い合わせの横棒と B の吹き出し・返金申請の 1 件 1 マスの絵グラフ)・それぞれ右上に 3D の絵の icon が弾む
section#side(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec7 {ro}06{/} 副作用
board#sl(left: 64px; top: 93px; width: 568px; height: 493px; k: "{ro}06{/} ／ 副作用"; t: "料金の問い合わせ"; s: "訪問 1,000 人あたり")
  img#ic(left: 440px; top: 5px; width: 100px; height: 100px; fit: contain; main: none; in: {scale:0.4, opacity:0, duration:0.5, ease:'back.out(2)'}) [transparent]2 つの重なった吹き出しの艶のある 3D の icon。手前の吹き出しに大きな疑問符が 1 つ。柔らかな珊瑚のピンクと冷たい青みの灰色、柔らかなスタジオの光、クリーンでモダンな 3D の質感、中央に 1 つだけ置く。疑問符の他に文字なし
  p#c(left: 29px; top: "124;191;257"; width: 31px; font-size: 17px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 8px; padding: 7px 0px) ×3 A;B;C
  div#b(left: 80px; top: "124;191;257"; width: "147;249;191"; height: 31px; border-radius: 5px; background: "linear(#6F7E93,#A6B3C4,90);linear(#D94A62,#FF8597,90);linear(#4A5870,#71819A,90)"; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left', stagger: {each: 0.12}}) ×3
  p#la(left: 241px; cy: 140px; font-size: 24px; font-family: b; white-space: nowrap; in: {opacity:0, duration:0.5}) 4.0{s13} 件（計 52 件）{/}
  p#lb(left: 344px; cy: 207px; font-size: 24px; font-family: b; color: #FFB3C0; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 6.8{s13} 件（計 87 件）{/}
  p#lc(left: 285px; cy: 273px; font-size: 24px; font-family: b; white-space: nowrap; in: {opacity:0, duration:0.5}) 5.2{s13} 件（計 66 件）{/}
  # B で増えた問い合わせの中身 (珊瑚の縁の吹き出し・上辺の尻尾は三角の shape)
  div#bub(left: 29px; top: 347px; width: 509px; height: 76px; border-radius: 12px; background: #FF6B811A; border: 1px solid #FF6B8180; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
    # hf の作り: 吹き出しの尻尾は板の上辺から外へ出る三角 (child_overflow)
    shape#tip(points: "58,1 69,-10 80,1"; background: #2A1A24; border: 1px solid #FF6B8180)
    p#b1(left: 19px; top: 15px; font-size: 14px; color: $tx2; white-space: nowrap) B で増えた問い合わせの多くは
    p#b2(left: 19px; top: 37px; font-size: 21px; font-family: b; color: #FFD5DC; white-space: nowrap) 「年額の途中解約・返金はできるか」
board#sr(left: 648px; top: 93px; width: 568px; height: 493px; k: "{ro}06{/} ／ 副作用"; t: "年額の返金申請"; s: "14 日以内"; delay: 320)
  img#ic(left: 440px; top: 5px; width: 100px; height: 100px; fit: contain; main: none; in: {scale:0.4, opacity:0, duration:0.5, ease:'back.out(2)'}) [transparent]紙のレシートと、1 枚の金色の硬貨を回り込む曲がった戻りの矢印の、艶のある 3D の icon。柔らかな珊瑚のピンクと琥珀の色、柔らかなスタジオの光、クリーンでモダンな 3D の質感、中央に 1 つだけ置く。文字・数字なし
  p#c(left: 29px; top: "131;211;291"; width: 31px; font-size: 17px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 8px; padding: 7px 0px) ×3 A;B;C
  div#pa(left: "80;102;124"; top: 136px; width: 17px; height: 17px; border-radius: 4px; background: #8B99AD; in: {scale:0.2, opacity:0, duration:0.3, ease:'back.out(2)', stagger: {each: 0.05}}) ×3
  div#pb(left: "80;102;124;146;168;190;212;234;256;278;300"; top: 216px; width: 17px; height: 17px; border-radius: 4px; background: $rose; box-shadow: 0px 0px 8px #FF6B8159; in: {scale:0.2, opacity:0, duration:0.3, ease:'back.out(2)', stagger: {each: 0.05}}) ×11
  div#pc(left: "80;102;124;146"; top: 296px; width: 17px; height: 17px; border-radius: 4px; background: $vc; in: {scale:0.2, opacity:0, duration:0.3, ease:'back.out(2)', stagger: {each: 0.05}}) ×4
  p#ra(left: 347px; top: 125px; font-size: 28px; font-family: b; line-height: 1.25; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.4%[br]{s13}3 件 ／ 年額 88 人{/}
  p#rb(left: 347px; top: 205px; font-size: 28px; font-family: b; line-height: 1.25; color: #FFB3C0; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 6.1%[br]{s13}11 件 ／ 年額 181 人{/}
  p#rc(left: 347px; top: 285px; font-size: 28px; font-family: b; line-height: 1.25; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.4%[br]{s13}4 件 ／ 年額 117 人{/}
  p#nt(left: 29px; top: 387px; width: 510px; font-size: 14px; line-height: 1.5; color: $tx2; in: {opacity:0, duration:0.5}) ■ 1 マス = 返金申請 1 件。割合は年額の課金者に占める申請の割合。

# net 返金後: 3 本の横棒が伸びて置かれ、「返金」の語で返金前の点線の枠を残して棒が縮み、値が返金後へ替わる → 右の小板で +15.2% を数え、C は A とほぼ同じ
section#net(stagger: {each:0}; out: {y:-9, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec8 {cy}07{/} 返金後
board#nt(left: 64px; top: 93px; width: 1152px; height: 513px; k: "{cy}07{/} ／ 返金後"; t: "返金を差し引いた初年度売上"; s: "訪問者 1 人あたり")
  div#hr(right: 373px)
  div#lq1(left: 635px; cy: 58px; width: 12px; height: 12px; border-radius: 3px; background: $tx2)
  p#lt1(left: 654px; cy: 58px; font-size: 14px; color: $tx2) 返金後
  shape#lq2(left: 715px; top: 52px; width: 12px; height: 12px; path: rect,r=0.25; background: none; border: 1px solid #94A3B899; dash: 2,2)
  p#lt2(left: 734px; cy: 58px; font-size: 14px; color: $tx2) 返金前
  rowlab2#la(top: 137px; ch: A; nm: 現行; delay: 200)
  rowlab2#lb(top: 231px; ch: B; nm: 年額が先; c: $cyan; delay: 300)
  rowlab2#lc(top: 324px; ch: C; nm: 3 段比較表; c: "#526076"; ink: "#F4F7FA"; delay: 400)
  shape#g(left: 200px; top: "133;227;320"; width: "348;409;351"; height: 39px; path: rect,r=0.18; background: none; border: 1px solid #94A3B873; dash: 4,4; in: {opacity:0, duration:0.4}) ×3
  div#b(left: 200px; top: "133;227;320"; width: "348;409;351"; height: 39px; border-radius: 7px; background: "linear(#6F7E93,#A6B3C4,90);linear(#1AA9BD,#62E6F3,90);linear(#4A5870,#71819A,90)"; delay: 350; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left', stagger: {each: 0.12}}) ×3
  # hf は「返金」の語で 1,243 → 1,231 と 0.8 秒で数え下げる — 語で [count:] の文字に差し替える (出ている値から数える)
  p#v(left: "564;625;567"; top: "129;223;316"; font-size: 25px; font-family: b; color: "$tx;$cyan;$tx"; white-space: nowrap; delay: 800; in: {opacity:0, duration:0.5, stagger: {each: 0.1}}) ×3 1,243{s15} 円{/};1,462{s15} 円{/};1,253{s15} 円{/}
  p#sw(left: "564;625;567"; top: "161;255;348"; font-size: 13px; color: $tx3; white-space: nowrap; delay: 800; in: {opacity:0, duration:0.5, stagger: {each: 0.1}}) ×3 返金前;返金前;返金前
  p#nn(left: 200px; top: 407px; font-size: 14px; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) ※ 年額の返金申請（14 日以内）の分を差し引いた推計
  callout#co(left: 793px; top: 23px; width: 333px; height: 467px)
    kick#k(left: 24px; top: 24px) B − A（返金後）
    # 写し: hf は小板が出た時点で +0.0% を置き「15.2」の語で数え始める — ここは数字を語で出し、出ると同時に数える
    p#big(left: 20px; top: 72px; font-size: 75px; font-family: b; line-height: 1; letter-spacing: -0.02em; color: $cyan; white-space: nowrap; in: {opacity:0, duration:0.2}) +[count:15.2 start=0 ms=900]%
    p#pre(left: 24px; top: 167px; font-size: 16px; line-height: 1.5; color: $tx2; white-space: nowrap; in: {opacity:0, duration:0.5}) 返金前は {w}+17.6%{/}[br]返金を差し引いても差は残る
    div#hr(left: 24px; top: 240px; width: 285px; height: 1px; background: $line)
    div#cn(left: 24px; top: 261px; width: 290px; height: 100px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
      kick#k(left: 0px; top: 0px) C（3 段比較表）
      p#t(left: 0px; top: 27px; font-size: 27px; font-family: b; white-space: nowrap) A とほぼ同じ
      p#n(left: 0px; top: 72px; font-size: 14px; font-family: c; color: $tx2; white-space: nowrap) C 1,237 円 ／ A 1,231 円

# conc 結論: 光の点の帯の絵が 17 秒かけて明け、題の一行 → 色の線の札 3 枚 (採用・対策・次の検証) が語ごとに上がり、札の行も語で 1 行ずつ → 暗転
section#conc(stagger: {each:0})
sec#sec9(out: none) {cy}08{/} 結論
img#end_bg(inset: 0; subject: bottom 20%; room: top 78%; main: keys(at=0 scale=1.1 opacity=0 | at=1 scale=1 opacity=0.85 ease=power1.out),duration=17500; in: none) [photo]暗くミニマルな抽象の風景。小さな光の点が細い帯になって、うっすら見える透視の格子の床の上を左下から右上へゆるやかに昇っていく。琥珀と青緑の光、紺に近い黒の背景、柔らかい霧、落ち着いて前向きな雰囲気。光の帯は画面の下 5 分の 1 を左下から右へ横切り、右端で少しだけ昇る。中央から上は大きな暗い空き (札の場所)。文字・数字・ロゴなし
div#end_sh(inset: 0; background: linear(#060A11E0,#060A119E@50%,#060A11E0,180); in: none)
div#ttl(left: 64px; top: 93px; width: 900px; height: 70px; in: {y:17, opacity:0, duration:0.6, ease:'power3.out'})
  kick#k(left: 0px; top: 0px) {cy}08{/} ／ 結論
  p#t(left: 0px; top: 20px; font-size: 35px; font-family: b; white-space: nowrap) B を採用し、条件を明記して次の検証へ
ccard#c1(left: 64px; n: "01"; l: 採用; h: "B「年額を先に表示」[br]を採用する"; c: $cyan)
  li#li(top: "195;228;261"; height: "24;24;48"; t: "転換率の差は統計的には言い切れない;年額の割合 {w}22% → 41%{/};訪問者 1 人あたり初年度売上は[br]返金後でも {w}+15%{/}"; c: $cyan; in: {y:8, opacity:0, duration:0.45, ease:'power3.out', stagger: {each: 0.15}}) ×3
ccard#c2(left: 455px; n: "02"; l: 対策; h: "途中解約・返金の条件を[br]料金ページに明記する"; c: $amber)
  li#li(top: "195;252"; height: "48;24"; t: "料金の問い合わせ {w}4.0 → 6.8 件{/}[br]（訪問 1,000 人あたり）;年額の返金申請 {w}3.4% → 6.1%{/}"; c: $amber; in: {y:8, opacity:0, duration:0.45, ease:'power3.out', stagger: {each: 0.15}}) ×2
ccard#c3(left: 845px; n: "03"; l: 次の検証; h: "返金条件を明記した B と[br]現行の B を比べる"; c: "#C8D3DF")
  li#li(top: "195;228;261"; t: "期間は {w}4 週間{/};{w}1 週目を除いた{/}転換率で判定;{w}90 日後{/}の返金・継続で判定"; c: "#C8D3DF") ×3
```

```timeline.txt
#v2
cast n = "明瞭でやや高めの音域の20代の男性のナレーター、粒立ちの良いハキハキした発声で、落ち着いて技術解説を伝える" speed=110%
silence head=0 tail=0

*** title
[>#subtitle]
bgm music
@n: [silence:0.85s][♪whoosh -1dB -800]料金ページで、年額を先に見せたら、[|]どうなるのか。[>#sub -150][>#st[*] +450]タスク管理 {SaaS|サース}「ノートレイル」の{　|、}[♪tick -3.6dB +50][♪tick -4.2dB +250][♪tick -4.2dB +450]{A/B|エービー} テストで[♪whoosh2 -1.2dB +260]す。[silence:0.05s]

*** setup
@n: [silence:0.45s][>#price.y +50][>#price.mo.lab +300][>#price.mo.pay[*] +350][♪pop -5.3dB +150]年額プランは{　|、}[>#price.mo.free[*] -50][>#price.mo.fl +50][♪bell -2.1dB +100]{2 か月|にかげつ}分お得。[>#vh -200][>#ca -50][>#cb +100][>#cc +250][♪pop -5.3dB +50][♪pop -5.6dB +200][♪pop -5.6dB +350]4 週間、訪問者を [>#info +100]3 つの案に振り分けました。
@: [>#ca.glow][!#ca to,{scale:1.03, duration:0.25, ease:'power1.inOut', yoyo:true, repeat:1}][♪tick -4dB]A は月額が先、[<#ca.glow][>#cb.glow][!#cb to,{scale:1.03, duration:0.25, ease:'power1.inOut', yoyo:true, repeat:1}][!#cb.mock.seg.on glow,#F5B54740,blur=0,spread=5 +150][=#cb.mock.seg.on +850][♪click -3.2dB +50]B は年額が先、[|][!#cb.glow to,{opacity:0.45, duration:0.3}][>#cc.glow][!#cc to,{scale:1.03, duration:0.25, ease:'power1.inOut', yoyo:true, repeat:1}][>#cc.mock.col[*] +50][♪tick -4dB]C は 3 段の比較表で[♪whoosh2 -1.2dB +240]す。[silence:0.05s]

*** conv
@n: [silence:0.45s][>#cv.la -50][>#cv.lb +100][>#cv.lc +250]有料転換率は{　|、}[>#cv.cia][>#cv.da][♪pop -5.3dB +50]A が [>#cv.va -100][>#cv.ca +200]{3.10%|3.1パーセント}、[>#cv.cib][>#cv.db][♪pop -5.3dB +50]B が [>#cv.vb -100][>#cv.cb +200][>#cv.cic +600][>#cv.dc +600][>#cv.vc +750][>#cv.cc +850][♪tick -4.8dB +700]3.44%。
@: [>#cv.df -100][♪pop -5.6dB +50]ただ、[>#cv.df.ci -50][>#cv.df.ax][>#cv.df.dp +200][>#cv.df.dd +200]差の信頼区間は[>#cv.df.dn][!#cv.df.ax.zero to,{scaleY:1.25, duration:0.2, ease:'power1.inOut'}][!#cv.df.ax.zero to,{scaleY:1, duration:0.2, ease:'power1.inOut'} +200]ゼロをまたぎ、[|][>#cv.df.vd]統計的には[>#cv.df.nt +300]言い[♪burst -4dB +30]切れませ[♪whoosh2 -1.2dB +250]ん。[silence:0.1s]

*** weekly
@n: [silence:0.45s][>#wk.pb1][>#wk.pa1 +120]差は [>#wk.g1][>#wk.gl1 +100][♪bell -2.1dB +50]1 週目に集中し、[|][>#wk.lb][>#wk.la][>#wk.pb2 +250][>#wk.pa2 +300][>#wk.g2 +400][>#wk.gl2 +400][>#wk.pb3 +550][>#wk.pa3 +600][>#wk.g3 +700][>#wk.gl3 +700][>#wk.pb4 +850][>#wk.pa4 +900][>#wk.g4 +1000][>#wk.gl4 +1000][>#wk.area +1000][♪tick -4.4dB +250][♪tick -4.4dB +550][♪tick -4.4dB +850]その後は {0.1〜0.2|0.1から0.2} ポイントに[>#wk.rb -200][>#wk.rl]縮小。
@: [>#wk.co -200][>#wk.co.ic][!#wk.co.ic to,{y:-7, rotation:6, duration:1.4, ease:'sine.inOut', yoyo:true, repeat:1} +700][♪blip -2.8dB +50]物珍しさの効果かもしれませ[♪whoosh2 -1.2dB +190]ん。[silence:0.05s]

*** share
@n: [silence:0.45s][>#sh.tr[1].m -100][>#sh.tr[2].m +20][>#sh.tr[3].m +140][♪rise -6.4dB +100]はっきり動いたのは、[>#sh.tr[1].y][>#sh.tr[2].y +150][>#sh.tr[3].y +300][>#sh.tr[1].ml +500][>#sh.tr[2].ml +600][>#sh.tr[3].ml +700]年額を選んだ人の割合。
@: [>#sh.co -200][>#sh.co.k]A の [>#sh.tr[1].yl -50][>#sh.co.p1][♪tick -4.2dB]22% に対し、[>#sh.co.ar -100]B は [>#sh.tr[2].yl -50][>#sh.co.p2][>#sh.tr[3].yl +450][>#sh.co.mon +550][>#sh.nt +800][♪bell -2.1dB +50]41% と、[>#sh.co.bd]ほぼ倍で[♪whoosh2 -1.2dB +600]す。[silence:0.4s]

*** revenue
@n: [silence:0.45s][>#rv.c1 +50][>#rv.c2 +250][>#rv.lt +350][>#rv.lbase +390][>#rv.lx[*] +430][>#rv.lb[*] +500][>#rv.lv[*] +900][>#rv.lbd +1300][♪pop -5.6dB +100]初年度の売上を推計すると、[|][>#rv.rt -300][>#rv.rbase -260][>#rv.rx[*] -220][>#rv.rb[*]][>#rv.rv[*]][♪rise -6.8dB +50]訪問者 {1 人|ひとり}あたりで{　|、}B が A より [>#rv.rbd][♪blip -2.8dB +50]17.6% 多い。
@: [>#rv.bn -100]効いたのは転換率より、[>#rv.bn.ul][♪tick -4.2dB]年額の割合で[♪whoosh2 -1.2dB +350]す。[silence:0.15s]

*** side
@n: [silence:0.45s][♪tension -0.6dB +50]ただし、副作用も。
@: [>#sl.ic -100]料金の問い合わせは[>#sl.b[*]]訪問 1,000 人あたり、[|][>#sl.la -50][>#sl.lc +200][♪pop -5.6dB]4.0 件から [>#sl.lb -50][!#sl.b[2] glow,#FF859799,blur=20][=#sl.b[2] +600][>#sl.bub +450][♪pop -5dB]6.8 件に。
@: [>#sr.ic -100][>#sr.pa[*] +150][>#sr.pb[*] +300][>#sr.pc[*] +450][♪tick -4.7dB +200]年額の返金申請も{　|、}[>#sr.ra -50]3.4% から [>#sr.rb -50][>#sr.rc +400][♪tick -4.2dB]6.1% に[>#sr.nt +200]上がりまし[♪whoosh2 -1.2dB +150]た。[silence:0.05s]

*** net
@n: [silence:0.45s]それでも、[>#nt.g[*]][!#nt.b[1] to,{scaleX:0.99, duration:0.8, ease:'power2.inOut', pivot:'left'} +200][!#nt.b[2] to,{scaleX:0.971, duration:0.8, ease:'power2.inOut', pivot:'left'} +200][!#nt.b[3] to,{scaleX:0.987, duration:0.8, ease:'power2.inOut', pivot:'left'} +200][!#nt.v[1] text,"[count:1,231]{s15} 円{/}" +200][!#nt.v[2] text,"[count:1,419]{s15} 円{/}" +200][!#nt.v[3] text,"[count:1,237]{s15} 円{/}" +200][!#nt.sw[1] text,"返金後 ／ 返金前 1,243" +350][!#nt.sw[2] text,"返金後 ／ 返金前 1,462" +350][!#nt.sw[3] text,"返金後 ／ 返金前 1,253" +350][♪whoosh -2.4dB +100]返金を差し引いた売上で、[|][>#nt.co -250]B は A を{　|、}[>#nt.co.big -50][♪bell -2.1dB +50]15.2% [>#nt.nn][>#nt.co.pre]上回ります。
@: [>#nt.co.cn -50][♪tick -4.4dB +50]C は{　|、}A と[!#nt.b[3] glow,#71819A99,blur=18][=#nt.b[3] +600]ほぼ同じでし[♪whoosh2 -1.2dB +370]た。[silence:0.2s]

*** conc
@n: [silence:0.45s][>#ttl -200][♪chime -2.4dB +50]結論です。
@: [>#c1 -150][>#c1.li[*] +250][♪pop -5.3dB +50]B を採用し、[|][>#c2 -150][>#c2.li[*] +250][♪pop -5.3dB +50]年額の途中解約と返金の条件を、料金ページに明記。
@: [>#c3 -150][♪pop -5.3dB +50]次は、明記した B と現行の B を{　|、}[>#c3.li[1] -100]4 週間比べ、[|][>#c3.li[2] -100]1 週目を除いた転換率と、[>#c3.li[3] -100]90 日後の{返金・継続|返金と継続}で判定しま[♪chime -3.2dB +740]す。[silence:2.3s]
fade out,900
```

# data · pricing-ab-test (hf 全力版の全量の写し — 料金ページの A/B テスト、年額を先に見せたら・暗い紺の地に板と図を場面ごとに組む 9 場面のデータ図解) — canvas 1920x1080

見せる作り: 全編の地 (紺の放射の光 + 漂う方眼 + 周辺減光 + 字幕の下の暗い帯) と 2 場面目から常設の上端の帯 (社名・題・期間・全編で伸びる進行・場面ごとに入れ替わる右上の章札)・題の絵が寄りながら明け mask から上がる 2 行と数え上げの 3 つの数字・場面 = 板 1〜2 枚 + 右の結論の小板・数字の語で伸びる図 (12 マスの料金と点線の 2 マス・3 案の画面の模型と語で光る縁・信頼区間の横線と 0 をまたぐ差の区間・左から描く 2 本の折れ線と面・積み上げの帯・2 組の縦棒と数え上げ・横棒と吹き出し・1 件 1 マスの絵グラフ・返金前の点線の枠を残して縮む横棒)・A/B/C の色を全編で通す・結論は絵の上に色の線の札 3 枚を語ごとに上げて暗転・字幕は地なしの白い字・音の層 (場面の境の風切り + 語に結んだ効果音 50)

```design.txt
#v2
# 学ぶ作り: 暗い data の design system を根に 1 回 (palette・書体 4 つ・板 board / 結論の小板 callout の def・A/B/C の色札 chip と行の札 rowlab・右上の章札 sec) → 場面は板の中身だけ
# 常設の層: 全編の地 (紺の放射の光 2 つ + 漂う方眼 + 周辺減光 + 字幕の下の暗い帯)・2 場面目から sticky の上端の帯 (社名・題・期間・全編で伸びる進行) と、場面ごとに入れ替わる右上の章札
# 図は台詞の数字の語で伸ばす: 12 マスの料金・3 案の画面の模型・信頼区間の横線・週ごとの折れ線と面・積み上げの帯・縦棒・横棒・1 件 1 マスの絵グラフ・返金前の点線の枠。A/B/C の色 (灰・青緑・暗い灰) を全編で通す
# hf d05 pricing-ab-test (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の退場は section の out (上へ抜けて消える)・切替は書かない (地は常設なので素の切替)
canvas 1920x1080 bg=#060A11
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
run cy { color: $cyan }
run ro { color: $rose }
run am { color: $amber }
run bl { color: $blue }
run va { color: $va }
run w { color: $tx; font-family: m }
run u { font-size: 30px; color: $tx2; font-family: c }
run s15 { font-size: 22px; color: $tx2 }
run s14 { font-size: 21px; color: $tx2 }
run s13 { font-size: 20px; color: $tx3 }
run pt { font-size: 44px; color: $tx2; font-family: m }
run pt16 { font-size: 24px }
run pb { font-size: 40px; color: $tx; font-family: b }
run b17 { font-size: 26px; color: $tx; font-family: b }
run yn { font-size: 18px; font-family: m }
run mb { font-size: 28px; font-family: b }
run ar27 { font-size: 40px; color: $tx3 }
run u17 { font-size: 26px; color: $tx2 }
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
div { border: none }
# 字幕: 下端中央に地なしの白い字 + 濃い影 (下の暗い帯の上)・句末の約物は外す・声の 0.08 秒前に出て声と同時に消える
subtitle.hug(left: 140px; bottom: 66px; width: 1640px; font-size: 33px; font-family: m; line-height: 1.2; letter-spacing: 0.03em; color: #E6EDF4; text-shadow: 0px 2px 14px #000000E6; background: none; border: none; box-shadow: none; text-align: center; unit: sentence; strip: 、。; lead: 80ms; tail: 0ms; hold: off; in: {y:10, opacity:0, duration:0.2, ease:'power2.out'}; out: {opacity:0, duration:0.14, ease:'power1.in'})
# 曲: 最後の 2.7 秒だけ前に出してから消える (hf は同じ曲の末尾を大きめの音量で重ねる)
bgm#music(fade: 1200,2200; keys: "end-2.7s:0|end-1.8s:+4") 知的で落ち着いたサイエンス系のシンセとピアノの曲、軽いビートと柔らかいパッド、データや研究の解説向け、主旋律は控えめ

# 板: 紺の縦グラデ + 細い縁 + 深い影・頭の行 (等幅の小札「01 ／ 前提」 + 25 px の題 + 補足) と下の罫・場面の頭から 0.2 秒で下から上がる
def board(k, t, s="") = div(border-radius: 22px; background: linear(#151F2FEB,#0B111BF0,180); border: 2px solid $line; box-shadow: 0px 40px 90px #00000080; delay: 200ms; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  p#k(left: 44px; top: 28px; font-size: 20px; font-family: c; letter-spacing: 0.14em; color: $tx3; white-space: nowrap; content: {k})
  p#t(left: 44px; top: 60px; font-size: 38px; font-family: m; letter-spacing: 0.01em; white-space: nowrap; content: {t})
  p#s(left: .t.right+16; top: 74px; font-size: 22px; color: $tx2; white-space: nowrap; content: {s})
  div#hr(left: 44px; right: 44px; top: 122px; height: 2px; background: $line)
# 板の右の結論の小板 (暗い半透明の地 + 縁)
def callout = div(border-radius: 20px; background: #060A118C; border: 2px solid $line2; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
# 等幅の小札 (板の中の前置き)
def kick = p(font-size: 20px; font-family: c; letter-spacing: 0.14em; color: $tx3; white-space: nowrap)
# A/B/C の色札 (A = 灰・B = 青緑・C = 暗い灰に白字)
def chip(t, c=$va, ink=$ink) = p(width: 46px; font-size: 26px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 12px; padding: 10px 0px; content: {t})
# 行の札 (色札 + 名 + 等幅の補足)
def rowlab(ch, nm, sb, c=$va, ink=$ink) = div(left: 44px; width: 375px; height: 60px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
  p#c(left: 0px; cy: 50%; width: 46px; font-size: 26px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 12px; padding: 10px 0px; content: {ch})
  p#nm(left: 63px; top: 0px; font-size: 26px; font-family: m; white-space: nowrap; content: {nm})
  p#sb(left: 63px; top: 34px; font-size: 20px; font-family: c; color: $tx3; white-space: nowrap; content: {sb})
# 行の札 (色札 + 名だけ)
def rowlab2(ch, nm, c=$va, ink=$ink) = div(left: 44px; width: 240px; height: 46px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
  p#c(left: 0px; cy: 50%; width: 46px; font-size: 26px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 12px; padding: 10px 0px; content: {ch})
  p#nm(left: 63px; cy: 50%; font-size: 26px; font-family: m; white-space: nowrap; content: {nm})
# 右上の章札 (青緑の番号 + 題)・場面の頭に下から入り、場面の終わりに上へ抜ける
def sec = p(right: 96px; cy: 56px; font-size: 20px; font-family: c; letter-spacing: 0.06em; white-space: nowrap; z-index: front; delay: 100ms; in: {y:10, opacity:0, duration:0.4, ease:'power2.out'}; out: {y:-10, opacity:0, duration:0.3, ease:'power2.in'})
# 信頼区間の横線 (両端に縦の小さな棒・中心から伸びる)
def ci(c) = div(height: 8px; border-radius: 4px; background: {c}; in: {scaleX:0, duration:0.7, ease:'power3.out'})
  div#l(left: 0px; cy: 50%; width: 3px; height: 24px; border-radius: 2px; background: {c})
  div#r(right: 0px; cy: 50%; width: 3px; height: 24px; border-radius: 2px; background: {c})
# 3 案の画面の模型 (料金の切り替えタブ + 価格 + 行 2 本 + ボタン)
def mockp(on, off, pr, c, ink) = div(width: 296px; height: 262px; border-radius: 14px; background: #0B121D; border: 2px solid #94A3B82E)
  div#bar(left: 2px; top: 2px; width: 292px; height: 26px; border-radius: 8,8,0,0; background: #94A3B814)
  shape#dot(left: "8;17;26"; top: 10px; width: 8px; height: 8px; border-radius: 50%; background: #94A3B859) ×3
  div#seg(left: 48px; top: 44px; width: 200px; height: 40px; border-radius: 148px; background: #94A3B81F)
    p#on(left: 4px; cy: 50%; width: 94px; font-size: 18px; font-family: m; line-height: 1.75; text-align: center; color: {ink}; background: {c}; border-radius: 148px; content: {on})
    p#off(left: 100px; cy: 50%; width: 94px; font-size: 18px; line-height: 1.75; text-align: center; color: $tx3; content: {off})
  p#pr(cx: 50%; top: 96px; font-size: 21px; color: $tx2; white-space: nowrap; content: {pr})
  div#l1(cx: 50%; top: 162px; width: 207px; height: 9px; border-radius: 4px; background: #94A3B829)
  div#l2(cx: 50%; top: 183px; width: 153px; height: 9px; border-radius: 4px; background: #94A3B829)
  div#cta(left: 34px; top: 210px; width: 226px; height: 30px; border-radius: 8px; background: {c})
# 3 案の札 (色札 + 題 + 補足 + 模型 + 訪問の人数)・語で縁が光る
def vcard(ch, tl, sb, n, c=$va, ink=$ink, gc=$va, gs=#94A3B840) = div(top: 208px; width: 344px; height: 520px; border-radius: 20px; background: linear(#151F2FEB,#0B111BF0,180); border: 2px solid $line; box-shadow: 0px 30px 70px #00000073; in: {y:40, opacity:0, duration:0.6, ease:'power3.out'})
  div#glow(left: 0px; top: 0px; width: 344px; height: 520px; border-radius: 20px; border: 2px solid {gc}; box-shadow: 0px 0px 40px {gs}; in: {opacity:0, duration:0.3}; out: {opacity:0, duration:0.3})
  p#ch(left: 28px; top: 26px; width: 46px; font-size: 26px; font-family: c; line-height: 1; text-align: center; color: {ink}; background: {c}; border-radius: 12px; padding: 10px 0px; content: {ch})
  p#tl(left: 28px; top: 92px; font-size: 28px; font-family: m; white-space: nowrap; content: {tl})
  p#sb(left: 28px; top: 134px; font-size: 20px; color: $tx3; white-space: nowrap; content: {sb})
  p#fl(left: 28px; bottom: 26px; font-size: 20px; color: $tx3) 訪問
  p#fn(right: 28px; bottom: 22px; font-size: 30px; font-family: m; white-space: nowrap; content: {n})
# 折れ線の点 (縁取りの丸 + 値)・ポンと出る
def pt(v, c, lc, ly, lx=8) = div(width: 24px; height: 24px; in: {scale:0.3, opacity:0, duration:0.5, ease:'back.out(2)'})
  shape#d(left: 0px; top: 0px; width: 24px; height: 24px; border-radius: 50%; background: {c}; border: 4px solid #0B121D)
  p#v(cx: {lx}; cy: {ly}; font-size: 22px; font-family: b; color: {lc}; white-space: nowrap; content: {v})
# 結論の札 (上端の色の線 + 番号 + 色の札 + 2 行の題 + 罫)
def ccard(n, l, h, c) = div(top: 300px; width: 556px; height: 560px; border-radius: 22px; background: linear(#151F2FF0,#0B111BF5,180); border: 2px solid $line; box-shadow: 0px 40px 90px #0000008C; in: {y:40, opacity:0, duration:0.7, ease:'power3.out'})
  div#top(left: 14px; top: 0px; width: 530px; height: 4px; border-radius: 3px; background: {c})
  p#no(left: 36px; top: 40px; font-size: 22px; font-family: c; letter-spacing: 0.12em; color: $tx3; content: {n})
  p#lb(left: 36px; top: 80px; font-size: 22px; font-family: b; color: $ink; background: {c}; border-radius: 148px; padding: 6px 16px; content: {l})
  p#hd(z-index: front; left: 36px; top: 142px; font-size: 36px; font-family: b; line-height: 1.34; white-space: nowrap; content: {h})
  div#dv(left: 36px; top: 268px; width: 484px; height: 2px; background: $line2)
# 結論の札の行 (色の点 + 文・語の頭で下から上がる)
def li(t, c) = div(left: 36px; width: 495px; height: 36px; in: {y:12, opacity:0, duration:0.45, ease:'power3.out'})
  shape#d(left: 2px; top: 15px; width: 8px; height: 8px; border-radius: 50%; background: {c})
  p#t(left: 24px; top: 0px; font-size: 24px; line-height: 1.5; color: $tx2; white-space: nowrap; content: {t})

# 全編の地 (根): 紺の地に右上と左下の放射の光・方眼が全編で右下へ 32 / 16 px 漂う・周辺減光・字幕の下の暗い帯
veil#glow1(background: radial(#142540,#14254000@70%,72%,0%); z-index: back; in: none)
veil#glow2(background: radial(#0F1D30,#0F1D3000@70%,0%,100%); z-index: back; in: none)
div#grid.bleed(left: -96px; top: -96px; width: 2112px; height: 1272px; pattern: grid,32,#94A3B80E; mask-image: radial-gradient(ellipse 72% 62% at 50% 46%, #000 25%, transparent 100%); z-index: back; in: none; main: ramp {x: 48, y: 24})
veil#vig(background: radial(#00000000@55%,#00000099,50%,45%); z-index: back; in: none)
div#capband(left: 0px; top: 910px; width: 1920px; height: 170px; background: linear(#060A1100,#060A11DB@70%,180); z-index: front; in: none)

# title 題: 料金ページの絵が 1.12 → 1 に寄りながら明け、左の暗い空きに小札 → mask から上がる 2 行 → 架空の社名 → 3 つの数字 (訪問者は数え上げ)
section#title(stagger: {each:0}; out: {y:-14, opacity:0, blur:8, duration:0.32, ease:'power2.in'})
img#hero(inset: 0; subject: right 45%; room: left 50%; main: keys(at=0 scale=1.12 opacity=0 | at=0.197 scale=1 opacity=1 ease=power2.out | at=1 scale=0.97 ease=none),duration=8118,pivot=72%,45%; in: none; out: {y:-14, opacity:0, blur:8, duration:0.32, ease:'power2.in'}) [photo]暗い紺の空間に浮かぶ SaaS の料金ページ。半透明のガラスの料金プランのカード 2 枚が横に並び、その上に光るトグルスイッチが 1 つ。左のカードは暖かい琥珀の光、右のカードは冷たい青みの光、縁に青緑の光、柔らかい靄、浅い被写界深度。カードとスイッチは画面の右半分 (中心は横 70%) に置き、左半分はほぼ真っ暗な空き (題の文字の場所)、下の 2 割は暗い床の反射。ミニマルで上質な技術の雰囲気、文字・数字・ロゴ・UI の表記なし
div#shade_l(inset: 0; background: linear(#060A11F7,#060A11DB@36%,#060A114D@58%,#060A1100@74%,90); in: none; out: {y:-14, opacity:0, blur:8, duration:0.32, ease:'power2.in'})
div#shade_b(inset: 0; background: linear(#060A1100@68%,#060A11E6,180); in: none; out: {y:-14, opacity:0, blur:8, duration:0.32, ease:'power2.in'})
div#kk(left: 120px; top: 214px; width: 960px; height: 38px; delay: 300ms; in: {y:18, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 0px; cy: 50%; width: 52px; height: 3px; background: $amber)
  p#t(left: 68px; cy: 50%; font-size: 32px; font-family: m; letter-spacing: 0.06em; color: $amber; white-space: nowrap) 料金ページの A/B テスト
p#l1(left: 120px; top: 276px; font-size: 138px; font-family: b; line-height: 1.1; white-space: nowrap; delay: 450ms; in: {y:166, duration:0.9, ease:'power4.out', clip:true}) {am}年額{/}を
p#l2(left: 120px; top: 435px; font-size: 138px; font-family: b; line-height: 1.1; white-space: nowrap; delay: 610ms; in: {y:166, duration:0.9, ease:'power4.out', clip:true}) 先に見せたら
p#sub(left: 120px; top: 633px; font-size: 32px; color: $tx2; white-space: nowrap; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'}) 架空のタスク管理 SaaS「ノートレイル」
# 3 つの数字 (2・3 つ目は左に細い縦線)
div#st(left: "80;313;497"; top: 718px; width: "233;184;220"; height: 117px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out', stagger: {each: 0.18}}) ×3
  div#sep(left: 0px; top: 0px; width: 2px; height: 117px; background: $line2; opacity: "0;1;1")
  p#k(left: "0;29;29"; top: 12px; font-size: 20px; letter-spacing: 0.12em; color: $tx3) 期間;比較;訪問者
  p#v(left: "0;29;29"; cy: 80px; font-size: 46px; font-family: m; white-space: nowrap) 9/1〜9/28{s15} 4 週間{/};3 案{s15} A・B・C{/};[count:38,440 start=0 ms=1100ms]{s15} 人{/}

# setup 前提: 上端の帯が明ける・左の板に月額と年額 (12 マスのうち 2 マスが点線 = 2 か月分お得)・右に 3 案の画面の模型が並び、案の名の語で縁が順に光る
section#setup(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.32, ease:'power2.in'})
# 上端の帯 (sticky・最後まで): 点の印・社名・題・期間と、全編で伸びる進行の線
div#hud.sticky(left: 0px; top: 0px; width: 1920px; height: 108px; z-index: front; in: {opacity:0, duration:0.6, ease:'power1.out'})
  svg#logo(left: 96px; cy: 56px; width: 34px; height: 22px; part: dots)
  p#brand(left: 146px; cy: 56px; font-size: 22px; font-family: m; letter-spacing: 0.04em; white-space: nowrap) ノートレイル
  div#sep(left: .brand.right+16; cy: 56px; width: 2px; height: 20px; background: $line2)
  p#sub(left: .sep.right+16; cy: 56px; font-size: 22px; color: $tx2; white-space: nowrap) 料金ページの A/B テスト
  p#period(right: 328px; cy: 56px; font-size: 20px; font-family: c; letter-spacing: 0.06em; color: $tx3; white-space: nowrap) 9/1–9/28 · 訪問 38,440 人
  div#track(left: 96px; top: 92px; width: 1728px; height: 2px; background: #94A3B81F)
progress#prog.sticky(left: 96px; top: 92px; width: 1728px; height: 2px; background: linear($cyan,$amber,90); until: end; z-index: front; overlap: hud)
sec#sec2 {cy}01{/} 前提
board#price(left: 96px; top: 140px; width: 610px; height: 760px; k: "{cy}01{/} ／ 前提"; t: "料金プラン")
  div#m(left: 44px; top: 160px; width: 524px; height: 150px)
    p#pl(left: 0px; top: 0px; font-size: 22px; font-family: m; color: $ink; background: $blue; border-radius: 148px; padding: 6px 16px) 月額プラン
    p#v(left: 0px; top: 52px; font-size: 92px; font-family: b; line-height: 1; letter-spacing: -0.01em; white-space: nowrap) 4,980{u} 円 / 月{/}
  div#y(left: 44px; top: 340px; width: 524px; height: 210px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
    p#pl(left: 0px; top: 0px; font-size: 22px; font-family: m; color: $ink; background: $amber; border-radius: 148px; padding: 6px 16px) 年額プラン
    p#v(left: 0px; top: 52px; font-size: 92px; font-family: b; line-height: 1; letter-spacing: -0.01em; white-space: nowrap) 49,800{u} 円 / 年{/}
    p#n(left: 0px; top: 168px; font-size: 22px; color: $amber; white-space: nowrap) ＝ 月額の 10 か月分
  # 12 マス (払う 10 マスは琥珀・お得の 2 マスは点線) と下のかぎ
  div#mo(left: 44px; top: 572px; width: 524px; height: 150px)
    p#lab(left: 0px; top: 0px; font-size: 21px; color: $tx2; white-space: nowrap; in: {opacity:0, duration:0.5}) 12 か月使えて、払うのは 10 か月分
    div#pay(left: "0;29;58;87;116;145;174;203;232;261"; top: 42px; width: 34px; height: 34px; border-radius: 8px; background: $amber; in: {scale:0.3, opacity:0, duration:0.35, ease:'back.out(2)', stagger: {each: 0.05}}) ×10
    shape#free(left: "290;319"; top: 42px; width: 34px; height: 34px; path: rect,r=0.22; background: #F5B54714; border: 2px solid $amber; dash: 3,3; in: {scale:0.3, opacity:0, duration:0.45, ease:'back.out(2)', stagger: {each: 0.08}}) ×2
    div#fl(left: 430px; top: 92px; width: 76px; height: 45px; in: {y:-8, opacity:0, duration:0.45, ease:'back.out(2)'})
      shape#brk(path: "M0 0 L0 9 L51 9 L51 0"; background: none; border: 2px solid $amber)
      p#t(cx: 50%; top: 20px; font-size: 22px; font-family: b; color: $amber; white-space: nowrap) 2 か月分お得
p#vh(left: 740px; top: 146px; font-size: 34px; font-family: m; white-space: nowrap; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'}) 3 つの案　{s15}訪問者をランダムに振り分け{/}
vcard#ca(left: 740px; ch: A; tl: 月額を先に表示; sb: 現行の料金ページ; n: "[count:12,840 start=0 ms=900ms delay=1470ms]{s13} 人{/}")
  p#tag(left: 87px; top: 30px; font-size: 18px; color: $tx2; border: 2px solid $line2; border-radius: 148px; padding: 3px 12px) 現行
  mockp#mock(left: 24px; top: 176px; on: 月額; off: 年額; pr: "{pb}4,980{/}円 / 月"; c: $blue; ink: "#08101C")
vcard#cb(left: 1110px; ch: B; tl: 年額を先に表示; sb: 月額は切り替えタブ; n: "[count:12,810 start=0 ms=900ms delay=1420ms]{s13} 人{/}"; c: $cyan; gc: $cyan; gs: "#3DD9EB59")
  mockp#mock(left: 24px; top: 176px; on: 年額; off: 月額; pr: "{pb}49,800{/}円 / 年"; c: $amber; ink: "#1C1306")
vcard#cc(left: 1480px; ch: C; tl: 3 段の比較表; sb: 月額・年額・チーム向け; n: "[count:12,790 start=0 ms=900ms delay=1370ms]{s13} 人{/}"; c: "#526076"; ink: "#F4F7FA"; gc: "#8796AB")
  # C の模型: 3 段の比較表 (月額・年額・チームの列)・「C は」の語で列が順に弾む
  div#mock(left: 24px; top: 176px; width: 296px; height: 262px; border-radius: 14px; background: #0B121D; border: 2px solid #94A3B82E)
    div#bar(left: 2px; top: 2px; width: 292px; height: 26px; border-radius: 8,8,0,0; background: #94A3B814)
    shape#dot(left: "8;17;26"; top: 10px; width: 8px; height: 8px; border-radius: 50%; background: #94A3B859) ×3
    div#col(left: "8;70;132"; top: 44px; width: 86px; height: 150px; border-radius: 10px; border: 2px solid #94A3B833; in: {scale:0.8, opacity:0, duration:0.5, ease:'back.out(2)', stagger: {each: 0.08}}) ×3
      p#h(cx: 50%; top: 10px; font-size: 16px; font-family: m; color: $tx2) 月額;年額;チーム
      div#p(left: 6px; top: 42px; width: 74px; height: 22px; border-radius: 4px; background: "#5B8DEF8C;#F5B54799;#94A3B838")
      div#l1(left: 4px; top: 75px; width: 76px; height: 8px; border-radius: 4px; background: #94A3B81F)
      div#l2(left: 4px; top: 93px; width: 76px; height: 8px; border-radius: 4px; background: #94A3B81F)
      div#b(left: 6px; top: 117px; width: 74px; height: 20px; border-radius: 6px; background: #94A3B84D)
# 期間・振り分け・合計の帯 (合計は数え上げ)
div#info(left: 740px; top: 760px; width: 1084px; height: 120px; border-radius: 18px; border: 2px solid $line; background: #0D141FCC; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
  p#k(left: "24;279;507"; top: 24px; font-size: 20px; letter-spacing: 0.1em; color: $tx3; white-space: nowrap) ×3 期間;振り分け;訪問者 合計
  p#v(left: "24;279;507"; top: 52px; font-size: 36px; font-family: m; white-space: nowrap) ×3 9/1〜9/28{s14} 4 週間{/};ランダム{s14} 3 案に振り分け{/};[count:38,440 start=0 ms=1000ms delay=200ms]{s14} 人{/}
  div#vl(left: "253;481"; top: 26px; width: 2px; height: 68px; background: $line2) ×2

# conv 転換率: 6 本の目盛りの上に A・B・C の推定値 (点) と 95% 信頼区間 (横線) を語で伸ばす → 右の小板で差 +0.34 を数え、差の区間が 0 をまたぐ所で赤い判定の札
section#conv(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec3 {cy}02{/} 転換率
board#cv(left: 96px; top: 140px; width: 1728px; height: 770px; k: "{cy}02{/} ／ 転換率"; t: "有料転換率"; s: "訪問から 14 日以内の課金")
  div#hr(right: 560px)
  shape#lg_dot(left: 876px; top: 78px; width: 18px; height: 18px; border-radius: 50%; background: $tx)
  p#lg1(left: 904px; cy: 87px; font-size: 21px; color: $tx2; white-space: nowrap) 推定値
  div#lg_ln(left: 996px; cy: 87px; width: 30px; height: 4px; border-radius: 3px; background: $tx2)
  p#lg2(left: 1036px; cy: 87px; font-size: 21px; color: $tx2; white-space: nowrap) 95% 信頼区間
  div#gv(left: "378;443;507;573;637;702"; top: 168px; width: 2px; height: 446px; background: #94A3B81F; delay: 250ms; in: {opacity:0, duration:0.6}) ×6
  p#ax(cx: "378;443;507;573;637;702"; top: 628px; font-size: 18px; font-family: c; color: $tx3; delay: 250ms; in: {opacity:0, duration:0.6}) ×6 2.8%;3.0%;3.2%;3.4%;3.6%;3.8%
  rowlab#la(top: 255px; ch: A; nm: 現行（月額が先）; sb: "398 / 12,840 人")
  rowlab#lb(top: 394px; ch: B; nm: 年額が先; sb: "441 / 12,810 人"; c: $cyan)
  rowlab#lc(top: 536px; ch: C; nm: 3 段の比較表; sb: "390 / 12,790 人"; c: "#526076"; ink: "#F4F7FA")
  ci#cia(left: 567px; top: 278px; width: 291px; c: "#94A3B8BF")
  ci#cib(left: 728px; top: 418px; width: 306px; c: "#3DD9EBD9")
  ci#cic(left: 543px; top: 558px; width: 291px; c: "#5F6E83F2")
  shape#da(left: 700px; top: 270px; width: 26px; height: 26px; border-radius: 50%; background: $va; border: 4px solid #0B121D; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
  shape#db(left: 866px; top: 410px; width: 26px; height: 26px; border-radius: 50%; background: $cyan; border: 4px solid #0B121D; box-shadow: 0px 0px 22px #3DD9EB99; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
  shape#dc(left: 676px; top: 549px; width: 26px; height: 26px; border-radius: 50%; background: #8A98AD; border: 4px solid #0B121D; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
  p#va(cx: 712px; top: 214px; font-size: 40px; font-family: b; white-space: nowrap; in: {y:14, opacity:0, duration:0.45, ease:'power3.out'}) 3.10%
  p#vb(cx: 878px; top: 354px; font-size: 40px; font-family: b; color: $cyan; white-space: nowrap; in: {y:14, opacity:0, duration:0.45, ease:'power3.out'}) 3.44%
  p#vc(cx: 688px; top: 494px; font-size: 40px; font-family: b; color: #B3BFCD; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.05%
  p#ca(cx: 712px; top: 302px; font-size: 18px; font-family: c; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) 2.80〜3.40%
  p#cb(cx: 878px; top: 442px; font-size: 18px; font-family: c; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.13〜3.76%
  p#cc(cx: 688px; top: 582px; font-size: 18px; font-family: c; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) 2.75〜3.35%
  # 差の小板: +0.34 pt を数え、差の区間 (白) と 0 より下の端 (赤) を伸ばし、赤い縁の判定の札が傾いて着地
  callout#df(left: 1190px; top: 34px; width: 500px; height: 700px; border: 2px solid $line)
    p#l(left: 34px; top: 24px; font-size: 24px; color: $tx2; white-space: nowrap) B と A の差
    p#n(left: 30px; top: 86px; font-size: 128px; font-family: b; line-height: 1; letter-spacing: -0.02em; white-space: nowrap) +[count:0.34 start=0 ms=800ms delay=150ms]{pt} pt{/}
    p#ci(left: 34px; top: 246px; font-size: 21px; font-family: c; color: $tx2; white-space: nowrap; in: {opacity:0, duration:0.5}) 95% 信頼区間 −0.09 〜 +0.78 pt
    div#ax(left: 0px; top: 285px; width: 500px; height: 120px; in: {opacity:0, duration:0.5})
      div#gl(left: 40px; top: 45px; width: 420px; height: 2px; background: #94A3B840)
      div#zero(left: 135px; top: 8px; width: 3px; height: 80px; border-radius: 2px; background: $tx)
      p#zl(cx: 136px; top: 94px; font-size: 18px; font-family: c; white-space: nowrap) 差 0
      p#p5(cx: 292px; top: 94px; font-size: 18px; font-family: c; color: $tx3; white-space: nowrap) +0.5
      div#tk(left: 292px; top: 34px; width: 2px; height: 20px; background: #94A3B866)
    div#dn(left: 106px; top: 326px; width: 28px; height: 10px; border-radius: 6px; background: $rose; in: {scaleX:0, duration:0.4, ease:'power2.out', pivot:'right'})
    div#dp(left: 135px; top: 326px; width: 248px; height: 10px; border-radius: 6px; background: #EAF0F6D9; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
    shape#dd(left: 231px; top: 318px; width: 26px; height: 26px; border-radius: 50%; background: $tx; border: 4px solid #0B121D; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'})
    div#vd(left: 30px; top: 450px; width: 440px; height: 108px; border-radius: 14px; border: 2px solid $rose; background: #FF6B8114; in: {scale:1.25, rotation:-3, opacity:0, duration:0.45, ease:'back.out(1.6)'})
      p#v1(left: 20px; top: 16px; font-size: 22px; color: $rose; opacity: 0.9; white-space: nowrap) 信頼区間がゼロをまたぐ
      p#v2(left: 20px; top: 51px; font-size: 32px; font-family: b; color: $rose; white-space: nowrap) 統計的には言い切れない
    p#nt(left: 34px; top: 604px; width: 435px; font-size: 20px; line-height: 1.5; color: $tx3; in: {opacity:0, duration:0.5}) B の転換率が A より高いとも、差がないとも断定できない

# weekly 週ごと: 方眼の上に 1 週目の 2 点と差 +0.88pt → B と A の折れ線を左から描き、週ごとの点と差の数字が順に出て面が染まる → 2 週目以降のかぎ → 右の小板に光るきらめきの絵と「物珍しさの効果？」
section#weekly(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec4 {cy}03{/} 週ごと
board#wk(left: 96px; top: 140px; width: 1728px; height: 770px; k: "{cy}03{/} ／ 週ごと"; t: "週ごとの転換率"; s: "B と A")
  div#hr(right: 600px)
  div#lg1(left: 813px; cy: 87px; width: 30px; height: 4px; border-radius: 3px; background: $cyan)
  p#lt1(left: 854px; cy: 87px; font-size: 21px; color: $tx2; white-space: nowrap) B 年額が先
  div#lg2(left: 986px; cy: 87px; width: 30px; height: 4px; border-radius: 3px; background: $va)
  p#lt2(left: 1026px; cy: 87px; font-size: 21px; color: $tx2; white-space: nowrap) A 現行
  div#gh(left: 153px; top: "127;175;225;273;322;371;420"; width: 890px; height: 2px; background: "#94A3B81F;#94A3B81F;#94A3B81F;#94A3B81F;#94A3B81F;#94A3B81F;#94A3B84D"; delay: 250ms; in: {opacity:0, duration:0.6}) ×7
  p#yl(left: 64px; cy: "127;175;225;273;322;371;420"; width: 75px; text-align: right; font-size: 18px; font-family: c; color: #7A889A; delay: 250ms; in: {opacity:0, duration:0.6}) ×7 4.0%;3.8%;3.6%;3.4%;3.2%;3.0%;2.8%
  p#xl(cx: "182;329;476;622"; cy: 668px; font-size: 22px; color: $tx2; white-space: nowrap; delay: 250ms; in: {opacity:0, duration:0.6}) ×4 1 週目;2 週目;3 週目;4 週目
  # hf の作り: B と A の間の面は 9% の青緑 (check はこの面の上の数字を low_contrast に数えるが、面はほぼ透明で読める)
  shape#area(path: "M182 159 L329 281 L476 310 L622 303 L622 327 L476 352 L329 335 L182 374 Z"; background: #3DD9EB17; in: {opacity:0, duration:0.8})
  shape#lb(path: "M182 159 L329 281 L476 310 L622 303"; background: none; border: 4px solid $cyan; in: draw {duration: 1.2})
  shape#la(path: "M182 374 L329 335 L476 352 L622 327"; background: none; border: 4px solid $va; in: draw {duration: 1.2})
  shape#g1(path: "M182 168 L182 364"; background: none; border: 2px solid $cyan; dash: 3,4; in: {opacity:0, duration:0.4})
  shape#g2(path: "M329 290 L329 325"; background: none; border: 2px solid $cyan; dash: 3,3; in: {opacity:0, duration:0.5})
  shape#g3(path: "M476 319 L476 342"; background: none; border: 2px solid $cyan; dash: 3,3; in: {opacity:0, duration:0.5})
  shape#g4(path: "M622 312 L622 318"; background: none; border: 2px solid $cyan; in: {opacity:0, duration:0.5})
  pt#pb1(left: 261px; top: 226px; v: 3.87%; c: $cyan; lc: $cyan; ly: -14)
  pt#pa1(left: 261px; top: 549px; v: 2.99%; c: $va; lc: "#C3CDD9"; ly: 26)
  pt#pb2(left: 482px; top: 410px; v: 3.37%; c: $cyan; lc: $cyan; ly: -6; lx: 43)
  pt#pa2(left: 482px; top: 490px; v: 3.15%; c: $va; lc: "#C3CDD9"; ly: 26)
  pt#pb3(left: 702px; top: 453px; v: 3.25%; c: $cyan; lc: $cyan; ly: -13)
  pt#pa3(left: 702px; top: 516px; v: 3.08%; c: $va; lc: "#C3CDD9"; ly: 26)
  pt#pb4(left: 921px; top: 442px; v: 3.28%; c: $cyan; lc: $cyan; ly: -13)
  pt#pa4(left: 921px; top: 478px; v: 3.18%; c: $va; lc: "#C3CDD9"; ly: 26)
  p#gl3(cx: 772px; cy: 496px; font-size: 22px; font-family: b; color: #9FE9F3; white-space: nowrap; in: {opacity:0, duration:0.5}) +0.17
  p#gl4(cx: 992px; cy: 472px; font-size: 22px; font-family: b; color: #9FE9F3; white-space: nowrap; in: {opacity:0, duration:0.5}) +0.10
  shape#rb(path: "M313 460 L313 469 L660 469 L660 460"; background: none; border: 2px solid #3DD9EBB3; in: {scaleX:0.2, opacity:0, duration:0.5, ease:'power2.out'})
  p#gl2(cx: 552px; cy: 460px; font-size: 22px; font-family: b; color: #9FE9F3; white-space: nowrap; in: {opacity:0, duration:0.5}) +0.22
  p#gl1(cx: 384px; cy: 462px; font-size: 46px; font-family: b; color: $cyan; white-space: nowrap; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'}) +0.88{pt16}pt{/}
  p#rl(cx: 730px; top: 712px; font-size: 21px; color: $cyan; white-space: nowrap; in: {opacity:0, duration:0.5}) 2 週目以降の差は 0.1〜0.2pt
  callout#co(left: 1150px; top: 34px; width: 540px; height: 700px)
    img#ic(left: 330px; top: 26px; width: 180px; height: 180px; object-fit: contain; box-shadow: 0px 27px 45px #00000080; main: none; in: {scale:0.4, rotation:-20, opacity:0, duration:0.7, ease:'back.out(2.2)'}) [transparent]琥珀の金色に柔らかく光る、艶のある小さな 4 つの角の星形のきらめきと、その横の小さな 2 つのきらめき。クリーンでモダンな 3D の icon の質感、柔らかなスタジオの光、中央に 1 つだけ置く。文字なし
    kick#k(left: 36px; top: 54px) 考えられること
    p#t(left: 36px; top: 96px; font-size: 40px; font-family: b; white-space: nowrap) 物珍しさの効果？
    p#b1(left: 36px; top: 236px; width: 480px; font-size: 26px; line-height: 1.6; color: $tx2) B の差は {w}1 週目が +0.88pt{/} と大きく、[br]{w}2 週目以降は 0.1〜0.2pt{/} に縮む。
    p#b2(left: 36px; top: 352px; width: 488px; font-size: 22px; line-height: 1.6; color: $tx2) 新しい見せ方への一時的な反応が、[br]1 週目の転換率に混じっている可能性がある。
    div#hr(left: 36px; top: 470px; width: 468px; height: 2px; background: $line)
    kick#k2(left: 36px; top: 500px) 1 週目
    p#r(left: 36px; top: 536px; font-size: 52px; font-family: b; color: $cyan; white-space: nowrap) 3.87%{s13} B ／ A {/}{va}2.99%{/}

# share 年額の割合: 3 本の帯が月額の青で満ち、年額の琥珀が左から伸びる → A・B の割合の札が弾み、右の小板に 22% → 41% と「倍近くに」・月額の人数 310 → 260
section#share(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec5 {cy}04{/} 年額の割合
board#sh(left: 96px; top: 140px; width: 1728px; height: 770px; k: "{cy}04{/} ／ 年額の割合"; t: "課金者のうち、年額を選んだ割合")
  div#hr(right: 560px)
  div#lq1(left: 994px; cy: 87px; width: 18px; height: 18px; border-radius: 4px; background: $amber)
  p#lt1(left: 1023px; cy: 87px; font-size: 21px; color: $tx2) 年額
  div#lq2(left: 1094px; cy: 87px; width: 18px; height: 18px; border-radius: 4px; background: $blue)
  p#lt2(left: 1122px; cy: 87px; font-size: 21px; color: $tx2) 月額
  rowlab#la(top: 202px; ch: A; nm: 現行; sb: "課金 398 人"; delay: 250ms)
  rowlab#lb(top: 352px; ch: B; nm: 年額が先; sb: "課金 441 人"; c: $cyan; delay: 350ms)
  rowlab#lc(top: 502px; ch: C; nm: 3 段比較表; sb: "課金 390 人"; c: "#526076"; ink: "#F4F7FA"; delay: 450ms)
  div#tr(left: 330px; top: "124;224;324"; width: 800px; height: 84px; border-radius: 12px; background: #94A3B80F) ×3
    div#m(left: 0px; top: 0px; width: 800px; height: 84px; border-radius: 12px; background: linear(#5B8DEFBF,#5B8DEF8C,90); in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
    div#y(left: 0px; top: 0px; width: "117;219;160"; height: 84px; border-radius: 8,0,0,8; background: $amber; box-shadow: 4px 0px 18px #00000059; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
    p#yl(left: 18px; cy: 50%; font-size: 38px; font-family: b; line-height: 1.05; color: #1C1306; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 22%[br]{yn}88 人{/};41%[br]{yn}181 人{/};30%[br]{yn}117 人{/}
    p#ml(right: 22px; cy: 50%; font-size: 22px; color: #E9F0FF; white-space: nowrap; in: {opacity:0, duration:0.5}) 月額 {mb}310{/} 人;月額 {mb}260{/} 人;月額
  p#a0(left: 330px; top: 600px; font-size: 18px; font-family: c; color: $tx3) 0%
  p#a1(cx: 1130px; top: 600px; font-size: 18px; font-family: c; color: $tx3) 100%
  p#nt(left: 330px; top: 650px; font-size: 20px; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) ※ 割合は各案の課金者に占める年額プランの課金者
  callout#co(left: 1190px; top: 34px; width: 500px; height: 700px)
    kick#k(left: 36px; top: 40px; in: {opacity:0, duration:0.5}) 年額の割合　A → B
    p#p1(left: 36px; top: 128px; font-size: 64px; font-family: b; line-height: 1; color: $va; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 22%
    p#ar(left: .p1.right+14; top: 147px; font-size: 40px; line-height: 1; color: $tx3; in: {opacity:0, duration:0.5}) →
    p#p2(left: .ar.right+14; top: 96px; font-size: 100px; font-family: b; line-height: 1; letter-spacing: -0.02em; color: $amber; white-space: nowrap; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2)'}) 41%
    p#bd(left: 36px; top: 250px; font-size: 30px; font-family: b; color: #1C1306; background: $amber; border-radius: 148px; padding: 8px 24px; white-space: nowrap; in: {scale:0.5, opacity:0, duration:0.5, ease:'back.out(2)'}) 倍近くに
    div#hr(left: 36px; top: 350px; width: 428px; height: 2px; background: $line)
    div#mon(left: 36px; top: 384px; width: 435px; height: 195px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
      kick#k(left: 0px; top: 0px) 月額の課金者　A → B
      p#r(left: 0px; top: 40px; font-size: 64px; font-family: b; color: $va; white-space: nowrap) 310{u17} 人{/}{ar27} → {/}{bl}260{/}{u17} 人{/}
      p#nt(left: 0px; top: 156px; font-size: 21px; color: $tx2; white-space: nowrap) 年額へ移った分、月額の課金者は減った

# revenue 売上: 月額と年額の単価の札 → 左の縦棒 (課金者 1 人あたり・+5.9%) → 右の縦棒 (訪問者 1 人あたり・数え上げ・+17.6% の大きな札) → 下の結びの一行に琥珀の下線
section#revenue(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec6 {cy}05{/} 売上
board#rv(left: 96px; top: 140px; width: 1728px; height: 770px; k: "{cy}05{/} ／ 売上"; t: "初年度売上の推計"; s: "1 人あたり")
  div#c1(left: 44px; top: 148px; width: 546px; height: 58px; border-radius: 148px; border: 2px solid $line2; background: #060A1180; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
    p#pl(left: 10px; cy: 50%; font-size: 20px; font-family: m; color: $ink; background: $blue; border-radius: 148px; padding: 4px 14px) 月額
    p#t(left: .pl.right+14; cy: 50%; font-size: 22px; white-space: nowrap) 初年度の平均継続 7.5 か月 → {b17}37,350{/} 円
  div#c2(left: 770px; top: 148px; width: 236px; height: 58px; border-radius: 148px; border: 2px solid $line2; background: #060A1180; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
    p#pl(left: 10px; cy: 50%; font-size: 20px; font-family: m; color: $ink; background: $amber; border-radius: 148px; padding: 4px 14px) 年額
    p#t(left: .pl.right+14; cy: 50%; font-size: 22px; white-space: nowrap) {b17}49,800{/} 円
  div#lbase(left: 44px; top: 600px; width: 760px; height: 2px; background: $line2; in: {opacity:0, duration:0.5})
  div#lb(left: "73;227;380"; top: "253;244;249"; width: 132px; height: "147;156;151"; border-radius: 8,8,3,3; background: "linear(#A6B3C4,#6F7E93,180);linear(#62E6F3,#1AA9BD,180);linear(#71819A,#4A5870,180)"; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom', stagger: {each: 0.12}}) ×3
  p#lt(left: 44px; top: 236px; font-size: 26px; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) 課金者 1 人あたり{s13} 円{/}
  p#lv(cx: "117;271;424"; top: "221;212;217"; font-size: 30px; font-family: b; color: "$tx;$cyan;$tx"; white-space: nowrap; in: {opacity:0, duration:0.5, stagger: {each: 0.12}}) ×3 40,103;42,460;41,085
  p#lbd(left: 486px; top: 282px; font-size: 22px; font-family: m; color: $cyan; border: 2px solid $cyan; border-radius: 148px; padding: 4px 14px; white-space: nowrap; in: {scale:0.6, opacity:0, duration:0.5, ease:'back.out(2)'}) +5.9%
  p#lx(cx: "117;271;424"; top: 612px; width: 40px; font-size: 22px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 10px; padding: 9px 0px; in: {opacity:0, duration:0.5}) ×3 A;B;C
  div#dv(left: 864px; top: 236px; width: 2px; height: 420px; background: $line)
  p#rt(left: 924px; top: 236px; font-size: 26px; font-family: m; white-space: nowrap; in: {opacity:0, duration:0.5}) 訪問者 1 人あたり{s13} 円{/}
  div#rbase(left: 924px; top: 600px; width: 760px; height: 2px; background: $line2; in: {opacity:0, duration:0.5})
  div#rb(left: "660;813;967"; top: "259;234;258"; width: 132px; height: "141;166;142"; border-radius: 8,8,3,3; background: "linear(#A6B3C4,#6F7E93,180);linear(#62E6F3,#1AA9BD,180);linear(#71819A,#4A5870,180)"; in: {scaleY:0, duration:0.8, ease:'power3.out', pivot:'bottom', stagger: {each: 0.12}}) ×3
  p#rv(cx: "704;857;1011"; top: "227;202;226"; font-size: 30px; font-family: b; color: "$tx;$cyan;$tx"; white-space: nowrap; in: {opacity:0, duration:0.3}) ×3 [count:1,243 start=0 ms=800ms delay=100ms];[count:1,462 start=0 ms=800ms delay=220ms];[count:1,253 start=0 ms=800ms delay=340ms]
  p#rbd(left: 1372px; top: 244px; font-size: 40px; font-family: b; color: #061317; background: $cyan; border-radius: 148px; padding: 8px 22px; white-space: nowrap; in: {scale:0.4, opacity:0, duration:0.5, ease:'back.out(2)'}) +17.6%
  p#rx(cx: "704;857;1011"; top: 612px; width: 40px; font-size: 22px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 10px; padding: 9px 0px; in: {opacity:0, duration:0.5}) ×3 A;B;C
  div#bn(left: 44px; top: 682px; width: 1641px; height: 64px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
    p#a(left: 0px; cy: 50%; font-size: 32px; font-family: m; white-space: nowrap) 差を生んでいるのは、
    p#b(left: .a.right+18; cy: 50%; font-size: 26px; color: $tx3; white-space: nowrap) 転換率より
    p#c(left: .b.right+18; cy: 50%; font-size: 32px; font-family: m; color: $amber; white-space: nowrap) 「年額の割合」
    div#ul(left: .c.left; top: 54px; width: 210px; height: 4px; border-radius: 3px; background: $amber; in: {scaleX:0, duration:0.5, ease:'power3.out', pivot:'left'})

# side 副作用: 板 2 枚 (問い合わせの横棒と B の吹き出し・返金申請の 1 件 1 マスの絵グラフ)・それぞれ右上に 3D の絵の icon が弾む
section#side(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec7 {ro}06{/} 副作用
board#sl(left: 96px; top: 140px; width: 852px; height: 740px; k: "{ro}06{/} ／ 副作用"; t: "料金の問い合わせ"; s: "訪問 1,000 人あたり")
  img#ic(left: 660px; top: 8px; width: 150px; height: 150px; object-fit: contain; main: none; in: {scale:0.4, opacity:0, duration:0.5, ease:'back.out(2)'}) [transparent]2 つの重なった吹き出しの艶のある 3D の icon。手前の吹き出しに大きな疑問符が 1 つ。柔らかな珊瑚のピンクと冷たい青みの灰色、柔らかなスタジオの光、クリーンでモダンな 3D の質感、中央に 1 つだけ置く。疑問符の他に文字なし
  p#c(left: 44px; top: "124;191;257"; width: 46px; font-size: 26px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 12px; padding: 10px 0px) ×3 A;B;C
  div#b(left: 120px; top: "124;191;257"; width: "147;249;191"; height: 46px; border-radius: 8px; background: "linear(#6F7E93,#A6B3C4,90);linear(#D94A62,#FF8597,90);linear(#4A5870,#71819A,90)"; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left', stagger: {each: 0.12}}) ×3
  p#la(left: 362px; cy: 210px; font-size: 36px; font-family: b; white-space: nowrap; in: {opacity:0, duration:0.5}) 4.0{s13} 件（計 52 件）{/}
  p#lb(left: 516px; cy: 310px; font-size: 36px; font-family: b; color: #FFB3C0; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 6.8{s13} 件（計 87 件）{/}
  p#lc(left: 428px; cy: 410px; font-size: 36px; font-family: b; white-space: nowrap; in: {opacity:0, duration:0.5}) 5.2{s13} 件（計 66 件）{/}
  # B で増えた問い合わせの中身 (珊瑚の縁の吹き出し・上辺の尻尾は三角の shape)
  div#bub(left: 44px; top: 520px; width: 764px; height: 114px; border-radius: 18px; background: #FF6B811A; border: 2px solid #FF6B8180; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
    # hf の作り: 吹き出しの尻尾は板の上辺から外へ出る三角 (child_overflow)
    shape#tip(points: "58,1 69,-10 80,1"; background: #2A1A24; border: 2px solid #FF6B8180)
    p#b1(left: 28px; top: 22px; font-size: 21px; color: $tx2; white-space: nowrap) B で増えた問い合わせの多くは
    p#b2(left: 28px; top: 56px; font-size: 32px; font-family: b; color: #FFD5DC; white-space: nowrap) 「年額の途中解約・返金はできるか」
board#sr(left: 972px; top: 140px; width: 852px; height: 740px; k: "{ro}06{/} ／ 副作用"; t: "年額の返金申請"; s: "14 日以内"; delay: 320ms)
  img#ic(left: 660px; top: 8px; width: 150px; height: 150px; object-fit: contain; main: none; in: {scale:0.4, opacity:0, duration:0.5, ease:'back.out(2)'}) [transparent]紙のレシートと、1 枚の金色の硬貨を回り込む曲がった戻りの矢印の、艶のある 3D の icon。柔らかな珊瑚のピンクと琥珀の色、柔らかなスタジオの光、クリーンでモダンな 3D の質感、中央に 1 つだけ置く。文字・数字なし
  div#pa(left: "80;102;124"; top: 204px; width: 26px; height: 26px; border-radius: 6px; background: #8B99AD; in: {scale:0.2, opacity:0, duration:0.3, ease:'back.out(2)', stagger: {each: 0.05}}) ×3
  p#c(left: 44px; top: "131;211;291"; width: 46px; font-size: 26px; font-family: c; line-height: 1; text-align: center; color: "$ink;$ink;#F4F7FA"; background: "$va;$cyan;#526076"; border-radius: 12px; padding: 10px 0px) ×3 A;B;C
  div#pb(left: "80;102;124;146;168;190;212;234;256;278;300"; top: 324px; width: 26px; height: 26px; border-radius: 6px; background: $rose; box-shadow: 0px 0px 12px #FF6B8159; in: {scale:0.2, opacity:0, duration:0.3, ease:'back.out(2)', stagger: {each: 0.05}}) ×11
  div#pc(left: "80;102;124;146"; top: 444px; width: 26px; height: 26px; border-radius: 6px; background: $vc; in: {scale:0.2, opacity:0, duration:0.3, ease:'back.out(2)', stagger: {each: 0.05}}) ×4
  p#ra(left: 520px; top: 188px; font-size: 42px; font-family: b; line-height: 1.25; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.4%[br]{s13}3 件 ／ 年額 88 人{/}
  p#rb(left: 520px; top: 308px; font-size: 42px; font-family: b; line-height: 1.25; color: #FFB3C0; white-space: nowrap; in: {scale:0.7, opacity:0, duration:0.5, ease:'back.out(2)'}) 6.1%[br]{s13}11 件 ／ 年額 181 人{/}
  p#rc(left: 520px; top: 428px; font-size: 42px; font-family: b; line-height: 1.25; white-space: nowrap; in: {opacity:0, duration:0.5}) 3.4%[br]{s13}4 件 ／ 年額 117 人{/}
  p#nt(left: 44px; top: 580px; width: 765px; font-size: 21px; line-height: 1.5; color: $tx2; in: {opacity:0, duration:0.5}) ■ 1 マス = 返金申請 1 件。割合は年額の課金者に占める申請の割合。

# net 返金後: 3 本の横棒が伸びて置かれ、「返金」の語で返金前の点線の枠を残して棒が縮み、値が返金後へ替わる → 右の小板で +15.2% を数え、C は A とほぼ同じ
section#net(stagger: {each:0}; out: {y:-14, opacity:0, duration:0.32, ease:'power2.in'})
sec#sec8 {cy}07{/} 返金後
board#nt(left: 96px; top: 140px; width: 1728px; height: 770px; k: "{cy}07{/} ／ 返金後"; t: "返金を差し引いた初年度売上"; s: "訪問者 1 人あたり")
  div#hr(right: 560px)
  div#lq1(left: 952px; cy: 87px; width: 18px; height: 18px; border-radius: 4px; background: $tx2)
  p#lt1(left: 981px; cy: 87px; font-size: 21px; color: $tx2) 返金後
  shape#lq2(left: 1072px; top: 78px; width: 18px; height: 18px; path: rect,r=0.25; background: none; border: 2px solid #94A3B899; dash: 2,2)
  p#lt2(left: 1101px; cy: 87px; font-size: 21px; color: $tx2) 返金前
  rowlab2#la(top: 206px; ch: A; nm: 現行; delay: 200ms)
  rowlab2#lb(top: 346px; ch: B; nm: 年額が先; c: $cyan; delay: 300ms)
  rowlab2#lc(top: 486px; ch: C; nm: 3 段比較表; c: "#526076"; ink: "#F4F7FA"; delay: 400ms)
  shape#g(left: 300px; top: "133;227;320"; width: "348;409;351"; height: 58px; path: rect,r=0.18; background: none; border: 2px solid #94A3B873; dash: 4,4; in: {opacity:0, duration:0.4}) ×3
  div#b(left: 300px; top: "133;227;320"; width: "348;409;351"; height: 58px; border-radius: 10px; background: "linear(#6F7E93,#A6B3C4,90);linear(#1AA9BD,#62E6F3,90);linear(#4A5870,#71819A,90)"; delay: 350ms; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left', stagger: {each: 0.12}}) ×3
  # hf は「返金」の語で 1,243 → 1,231 と 0.8 秒で数え下げる — 語で [count:] の文字に差し替える (出ている値から数える)
  p#v(left: "564;625;567"; top: "129;223;316"; font-size: 38px; font-family: b; color: "$tx;$cyan;$tx"; white-space: nowrap; delay: 800ms; in: {opacity:0, duration:0.5, stagger: {each: 0.1}}) ×3 1,243{s15} 円{/};1,462{s15} 円{/};1,253{s15} 円{/}
  p#sw(left: "564;625;567"; top: "161;255;348"; font-size: 20px; color: $tx3; white-space: nowrap; delay: 800ms; in: {opacity:0, duration:0.5, stagger: {each: 0.1}}) ×3 返金前;返金前;返金前
  p#nn(left: 300px; top: 610px; font-size: 21px; color: $tx3; white-space: nowrap; in: {opacity:0, duration:0.5}) ※ 年額の返金申請（14 日以内）の分を差し引いた推計
  callout#co(left: 1190px; top: 34px; width: 500px; height: 700px)
    kick#k(left: 36px; top: 36px) B − A（返金後）
    # 写し: hf は小板が出た時点で +0.0% を置き「15.2」の語で数え始める — ここは数字を語で出し、出ると同時に数える
    p#big(left: 30px; top: 108px; font-size: 112px; font-family: b; line-height: 1; letter-spacing: -0.02em; color: $cyan; white-space: nowrap; in: {opacity:0, duration:0.2}) +[count:15.2 start=0 ms=900ms]%
    p#pre(left: 36px; top: 250px; font-size: 24px; line-height: 1.5; color: $tx2; white-space: nowrap; in: {opacity:0, duration:0.5}) 返金前は {w}+17.6%{/}[br]返金を差し引いても差は残る
    div#hr(left: 36px; top: 360px; width: 428px; height: 2px; background: $line)
    div#cn(left: 36px; top: 392px; width: 435px; height: 150px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
      kick#k(left: 0px; top: 0px) C（3 段比較表）
      p#t(left: 0px; top: 40px; font-size: 40px; font-family: b; white-space: nowrap) A とほぼ同じ
      p#n(left: 0px; top: 108px; font-size: 21px; font-family: c; color: $tx2; white-space: nowrap) C 1,237 円 ／ A 1,231 円

# conc 結論: 光の点の帯の絵が 17 秒かけて明け、題の一行 → 色の線の札 3 枚 (採用・対策・次の検証) が語ごとに上がり、札の行も語で 1 行ずつ → 暗転
section#conc(stagger: {each:0})
sec#sec9(out: none) {cy}08{/} 結論
img#end_bg(inset: 0; subject: bottom 20%; room: top 78%; main: keys(at=0 scale=1.1 opacity=0 | at=1 scale=1 opacity=0.85 ease=power1.out),duration=17500; in: none) [photo]暗くミニマルな抽象の風景。小さな光の点が細い帯になって、うっすら見える透視の格子の床の上を左下から右上へゆるやかに昇っていく。琥珀と青緑の光、紺に近い黒の背景、柔らかい霧、落ち着いて前向きな雰囲気。光の帯は画面の下 5 分の 1 を左下から右へ横切り、右端で少しだけ昇る。中央から上は大きな暗い空き (札の場所)。文字・数字・ロゴなし
div#end_sh(inset: 0; background: linear(#060A11E0,#060A119E@50%,#060A11E0,180); in: none)
div#ttl(left: 96px; top: 140px; width: 1350px; height: 105px; in: {y:26, opacity:0, duration:0.6, ease:'power3.out'})
  kick#k(left: 0px; top: 0px) {cy}08{/} ／ 結論
  p#t(left: 0px; top: 30px; font-size: 52px; font-family: b; white-space: nowrap) B を採用し、条件を明記して次の検証へ
ccard#c1(left: 96px; n: "01"; l: 採用; h: "B「年額を先に表示」[br]を採用する"; c: $cyan)
  li#li(top: "195;228;261"; height: "24;24;48"; t: "転換率の差は統計的には言い切れない;年額の割合 {w}22% → 41%{/};訪問者 1 人あたり初年度売上は[br]返金後でも {w}+15%{/}"; c: $cyan; in: {y:12, opacity:0, duration:0.45, ease:'power3.out', stagger: {each: 0.15}}) ×3
ccard#c2(left: 682px; n: "02"; l: 対策; h: "途中解約・返金の条件を[br]料金ページに明記する"; c: $amber)
  li#li(top: "195;252"; height: "48;24"; t: "料金の問い合わせ {w}4.0 → 6.8 件{/}[br]（訪問 1,000 人あたり）;年額の返金申請 {w}3.4% → 6.1%{/}"; c: $amber; in: {y:12, opacity:0, duration:0.45, ease:'power3.out', stagger: {each: 0.15}}) ×2
ccard#c3(left: 1268px; n: "03"; l: 次の検証; h: "返金条件を明記した B と[br]現行の B を比べる"; c: "#C8D3DF")
  li#li(top: "195;228;261"; t: "期間は {w}4 週間{/};{w}1 週目を除いた{/}転換率で判定;{w}90 日後{/}の返金・継続で判定"; c: "#C8D3DF") ×3
```

```timeline.txt
#v2
cast n = "明瞭でやや高めの音域の20代の男性のナレーター、粒立ちの良いハキハキした発声で、落ち着いて技術解説を伝える" speed=110%
silence head=0ms tail=0ms

*** title
[>#subtitle]
bgm music
@n: [silence:0.85s][♪whoosh -1dB -800ms]料金ページで、年額を先に見せたら、[|]どうなるのか。[>#sub -150ms][>#st[*] +450ms]タスク管理 SaaS「ノートレイル」の、[♪tick -3.6dB +50ms][♪tick -4.2dB +250ms][♪tick -4.2dB +450ms]A/B テストで[♪whoosh2 -1.2dB +260ms]す。[silence:0.05s]

*** setup
@n: [silence:0.45s][>#price.y +50ms][>#price.mo.lab +300ms][>#price.mo.pay[*] +350ms][♪pop -5.3dB +150ms]年額プランは、[>#price.mo.free[*] -50ms][>#price.mo.fl +50ms][♪bell -2.1dB +100ms]2 か月分お得。[>#vh -200ms][>#ca -50ms][>#cb +100ms][>#cc +250ms][♪pop -5.3dB +50ms][♪pop -5.6dB +200ms][♪pop -5.6dB +350ms]4 週間、訪問者を [>#info +100ms]3 つの案に振り分けました。
@: [>#ca.glow][!#ca to,{scale:1.03, duration:0.25, ease:'power1.inOut', yoyo:true, repeat:1}][♪tick -4dB]A は月額が先、[<#ca.glow][>#cb.glow][!#cb to,{scale:1.03, duration:0.25, ease:'power1.inOut', yoyo:true, repeat:1}][!#cb.mock.seg.on glow,#F5B54740 {blur: 0, spread: 5} +150ms][=#cb.mock.seg.on +850ms][♪click -3.2dB +50ms]B は年額が先、[|][!#cb.glow to,{opacity:0.45, duration:0.3}][>#cc.glow][!#cc to,{scale:1.03, duration:0.25, ease:'power1.inOut', yoyo:true, repeat:1}][>#cc.mock.col[*] +50ms][♪tick -4dB]C は 3 段の比較表で[♪whoosh2 -1.2dB +240ms]す。[silence:0.05s]

*** conv
@n: [silence:0.45s][>#cv.la -50ms][>#cv.lb +100ms][>#cv.lc +250ms]有料転換率は、[>#cv.cia][>#cv.da][♪pop -5.3dB +50ms]A が [>#cv.va -100ms][>#cv.ca +200ms]3.10%、[>#cv.cib][>#cv.db][♪pop -5.3dB +50ms]B が [>#cv.vb -100ms][>#cv.cb +200ms][>#cv.cic +600ms][>#cv.dc +600ms][>#cv.vc +750ms][>#cv.cc +850ms][♪tick -4.8dB +700ms]3.44%。
@: [>#cv.df -100ms][♪pop -5.6dB +50ms]ただ、[>#cv.df.ci -50ms][>#cv.df.ax][>#cv.df.dp +200ms][>#cv.df.dd +200ms]差の信頼区間は[>#cv.df.dn][!#cv.df.ax.zero to,{scaleY:1.25, duration:0.2, ease:'power1.inOut'}][!#cv.df.ax.zero to,{scaleY:1, duration:0.2, ease:'power1.inOut'} +200ms]ゼロをまたぎ、[|][>#cv.df.vd]統計的には[>#cv.df.nt +300ms]言い[♪burst -4dB +30ms]切れませ[♪whoosh2 -1.2dB +250ms]ん。[silence:0.1s]

*** weekly
@n: [silence:0.45s][>#wk.pb1][>#wk.pa1 +120ms]差は [>#wk.g1][>#wk.gl1 +100ms][♪bell -2.1dB +50ms]1 週目に集中し、[|][>#wk.lb][>#wk.la][>#wk.pb2 +250ms][>#wk.pa2 +300ms][>#wk.g2 +400ms][>#wk.gl2 +400ms][>#wk.pb3 +550ms][>#wk.pa3 +600ms][>#wk.g3 +700ms][>#wk.gl3 +700ms][>#wk.pb4 +850ms][>#wk.pa4 +900ms][>#wk.g4 +1000ms][>#wk.gl4 +1000ms][>#wk.area +1000ms][♪tick -4.4dB +250ms][♪tick -4.4dB +550ms][♪tick -4.4dB +850ms]その後は 0.1〜0.2 ポイントに[>#wk.rb -200ms][>#wk.rl]縮小。
@: [>#wk.co -200ms][>#wk.co.ic][!#wk.co.ic to,{y:-10, rotation:6, duration:1.4, ease:'sine.inOut', yoyo:true, repeat:1} +700ms][♪blip -2.8dB +50ms]物珍しさの効果かもしれませ[♪whoosh2 -1.2dB +190ms]ん。[silence:0.05s]

*** share
@n: [silence:0.45s][>#sh.tr[1].m -100ms][>#sh.tr[2].m +20ms][>#sh.tr[3].m +140ms][♪rise -6.4dB +100ms]はっきり動いたのは、[>#sh.tr[1].y][>#sh.tr[2].y +150ms][>#sh.tr[3].y +300ms][>#sh.tr[1].ml +500ms][>#sh.tr[2].ml +600ms][>#sh.tr[3].ml +700ms]年額を選んだ人の割合。
@: [>#sh.co -200ms][>#sh.co.k]A の [>#sh.tr[1].yl -50ms][>#sh.co.p1][♪tick -4.2dB]22% に対し、[>#sh.co.ar -100ms]B は [>#sh.tr[2].yl -50ms][>#sh.co.p2][>#sh.tr[3].yl +450ms][>#sh.co.mon +550ms][>#sh.nt +800ms][♪bell -2.1dB +50ms]41% と、[>#sh.co.bd]ほぼ倍で[♪whoosh2 -1.2dB +600ms]す。[silence:0.4s]

*** revenue
@n: [silence:0.45s][>#rv.c1 +50ms][>#rv.c2 +250ms][>#rv.lt +350ms][>#rv.lbase +390ms][>#rv.lx[*] +430ms][>#rv.lb[*] +500ms][>#rv.lv[*] +900ms][>#rv.lbd +1300ms][♪pop -5.6dB +100ms]初年度の売上を推計すると、[|][>#rv.rt -300ms][>#rv.rbase -260ms][>#rv.rx[*] -220ms][>#rv.rb[*]][>#rv.rv[*]][♪rise -6.8dB +50ms]訪問者 1 人あたりで、B が A より [>#rv.rbd][♪blip -2.8dB +50ms]17.6% 多い。
@: [>#rv.bn -100ms]効いたのは転換率より、[>#rv.bn.ul][♪tick -4.2dB]年額の割合で[♪whoosh2 -1.2dB +350ms]す。[silence:0.15s]

*** side
@n: [silence:0.45s][♪tension -0.6dB +50ms]ただし、副作用も。
@: [>#sl.ic -100ms]料金の問い合わせは[>#sl.b[*]]訪問 1,000 人あたり、[|][>#sl.la -50ms][>#sl.lc +200ms][♪pop -5.6dB]4.0 件から [>#sl.lb -50ms][!#sl.b[2] glow,#FF859799 {blur: 20}][=#sl.b[2] +600ms][>#sl.bub +450ms][♪pop -5dB]6.8 件に。
@: [>#sr.ic -100ms][>#sr.pa[*] +150ms][>#sr.pb[*] +300ms][>#sr.pc[*] +450ms][♪tick -4.7dB +200ms]年額の返金申請も、[>#sr.ra -50ms]3.4% から [>#sr.rb -50ms][>#sr.rc +400ms][♪tick -4.2dB]6.1% に[>#sr.nt +200ms]上がりまし[♪whoosh2 -1.2dB +150ms]た。[silence:0.05s]

*** net
@n: [silence:0.45s]それでも、[>#nt.g[*]][!#nt.b[1] to,{scaleX:0.99, duration:0.8, ease:'power2.inOut', pivot:'left'} +200ms][!#nt.b[2] to,{scaleX:0.971, duration:0.8, ease:'power2.inOut', pivot:'left'} +200ms][!#nt.b[3] to,{scaleX:0.987, duration:0.8, ease:'power2.inOut', pivot:'left'} +200ms][!#nt.v[1] text,"[count:1,231]{s15} 円{/}" +200ms][!#nt.v[2] text,"[count:1,419]{s15} 円{/}" +200ms][!#nt.v[3] text,"[count:1,237]{s15} 円{/}" +200ms][!#nt.sw[1] text,"返金後 ／ 返金前 1,243" +350ms][!#nt.sw[2] text,"返金後 ／ 返金前 1,462" +350ms][!#nt.sw[3] text,"返金後 ／ 返金前 1,253" +350ms][♪whoosh -2.4dB +100ms]返金を差し引いた売上で、[|][>#nt.co -250ms]B は A を、[>#nt.co.big -50ms][♪bell -2.1dB +50ms]15.2% [>#nt.nn][>#nt.co.pre]上回ります。
@: [>#nt.co.cn -50ms][♪tick -4.4dB +50ms]C は、A と[!#nt.b[3] glow,#71819A99 {blur: 18}][=#nt.b[3] +600ms]ほぼ同じでし[♪whoosh2 -1.2dB +370ms]た。[silence:0.2s]

*** conc
@n: [silence:0.45s][>#ttl -200ms][♪chime -2.4dB +50ms]結論です。
@: [>#c1 -150ms][>#c1.li[*] +250ms][♪pop -5.3dB +50ms]B を採用し、[|][>#c2 -150ms][>#c2.li[*] +250ms][♪pop -5.3dB +50ms]年額の途中解約と返金の条件を、料金ページに明記。
@: [>#c3 -150ms][♪pop -5.3dB +50ms]次は、明記した B と現行の B を、[>#c3.li[1] -100ms]4 週間比べ、[|][>#c3.li[2] -100ms]1 週目を除いた転換率と、[>#c3.li[3] -100ms]90 日後の返金・継続で判定しま[♪chime -3.2dB +740ms]す。[silence:2.3s]
fade out,900ms
```

# data · survey-week1 (hf 全力版の全量の写し — 登録時アンケート、1週間の結果・暗い地の 7 場面のデータ図解 (ファネル・前後の縦棒・waffle・横棒・1 点 = 1 人・目盛りの輪)) — canvas 1280x720

見せる作り: 全編 1 枚の暗い点の格子の地 + 場面ごとに動く琥珀の光・2 場面目からの常設の枠 (上端の進行線・左上の題・右上の章の番号)・場面の骨組みの def (番号 + 見出し + 副題 + 題つきの板)・語で伸びる図 (割れるファネルの帯と引き出し線・数え上げ・目盛りの輪の弧・前 → 後の縦棒と「有意差なし」・100 マスの waffle の塗り替え・薄く先出しした札を点灯して伸ばす横棒・1 点 = 1 人の点と光る 1 点・差の破線の枠)・旧場面が上へ抜けて琥珀の光の帯が払う切替・締めの 3 枚の札と黒への fade・音の層 (BGM + 語に結んだ効果音 50 + 切替の風切り)

```design.txt
#v2
# 学ぶ作り: 全編の地は根に 1 回 (暗い点の格子の絵 + 場面ごとに動く琥珀の光 + 周辺減光)・2 場面目から常設の枠 (上端の進行線・左上の題・右上の章の番号) を sticky で
# 場面は同じ骨組み (左上の番号 + 見出し + 副題 → 題つきの板) を def で揃え、板の中の図 (横棒の行・縦棒・100 マスの waffle・1 点 = 1 人の点・目盛りの輪) は台詞の数字の語で伸ばす
# 板の中は「構造を先に薄く出し、読む語で点灯する」(札の opacity を to で 1 に)・切替は旧場面が上へ抜けた後に琥珀の光の帯が左から払う wipe・締めは 3 枚の札を行ごとに
# hf survey survey-week1 (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1280x720 bg=#0A0F1C
theme dark
palette fg=#EEF2F8 fg2=#B9C3D5 fg3=#909CB2 amber=#F5B544 amber_hi=#FFD27F slate=#52617C slate2=#7D8CA8 steel=#6FA8DC panel=#0D1424DB line=#A0B6DE2B empty=#7D8CA829 ink=#1B1206 drop=#3E4A60 am0=#DF9526 am1=#E39A2B st0=#4F88C0 edge=#0D1424 lit=#B3BED3
font "細すぎず太すぎない標準の太さ (Regular) の日本語のゴシック体、癖がなく読みやすい本文用"
fonts b="癖のない標準的な日本語のゴシック体の太字 (Bold)、画面の資料や UI 向けの読みやすい書体" r="細すぎず太すぎない標準の太さ (Regular) の日本語のゴシック体、癖がなく読みやすい本文用"
sfx off
# hf の作り: 注記・凡例・札・板の題は 13〜17 px (hf の 20〜25 px の 2/3)
# hf の作り: 見出し・副題・板の骨組みは場面の頭に出して台詞が後から読む (spoiler・all_at_once)・行の札は薄く先出しして棒は語で伸ばす (empty_board)
# hf の作り: 全編 1 枚の点の格子の絵を地にして場面は図で替える (same_picture)・場面の頭の帯は切替の窓の中で伸び始める (entrance_in_transition)・結論の帯は場面の終わり際に出る (flash_text・entrance_in_fadeout)
lint off=small_text,spoiler,all_at_once,empty_board,same_picture,entrance_in_transition,flash_text,entrance_in_fadeout
run a { color: $amber }
run ab { color: $amber; font-family: b }
run hi { color: $amber_hi }
run w { color: $fg; font-family: b }
run s { color: $steel }
run pn { font-size: 13px; color: $fg3; font-family: r }
run pc { font-size: 0.54em }
run pcs { font-size: 0.4em; color: $steel }
run pca { font-size: 0.4em; color: $amber }
run vs { font-size: 20px; color: $fg3 }
run sec { font-size: 0.38em; color: $fg2 }
run v19 { font-size: 19px; color: $fg; font-family: b }
run v21 { font-size: 21px; color: $fg; font-family: b }
run n27 { font-size: 27px; color: $fg; font-family: b }
run n27a { font-size: 27px; color: $amber; font-family: b }
run sl { color: $slate2 }
sound hit = "抑えた深く柔らかい低音のドーンに空気感のある余韻、題が出る瞬間の控えめな映画風の音"
sound swipe = "札が滑り込む軽く速いスワイプの音"
sound whoosh = "短く滑らかな風切りのシュッという場面転換の音"
sound rise = "棒グラフが伸びる短く柔らかいシンセの上昇音"
sound blip = "データの点が出る柔らかく短い電子音のピッ"
sound tick = "数字が回って増える速く柔らかい電子のカチカチ音"
sound chime = "穏やかなマリンバの 2 音の明るい通知のチャイム"
# 横棒を伸ばして値を出す (値は def の delay 450 で伸び切る直前に)・札を点灯してから伸ばす
cue bar(r) = [>#r.b][>#r.v]
cue lit(r) = [!#r.l to,opacity=1,duration=300 -100][>#r.b][>#r.v]
# 場面の要素は一斉に上へ抜ける (hf の leave: y -18・scale .985・opacity 0・0.32 s)
motion leave { out: {y:-12, scale:0.985, opacity:0, duration:0.32, ease:'power2.in'} }
p { color: $fg; out: leave }
div { padding: 0px; border: none; box-shadow: none; border-radius: 0px; background: none; out: leave }
shape { out: leave }
svg { out: leave }
# 字幕: 下端中央の暗い札・句点で割り、句末の。は外す (声の 60 ms 前に出て 150 ms 後に消える)
subtitle.hug(bottom: 27px; font-size: 22px; line-height: 1.4; letter-spacing: .02em; color: $fg; background: #050912BD; border-radius: 8px; padding: 7px 20px 8px 20px; unit: sentence; strip: 。; lead: 60; tail: 150; hold: off; in: fade {duration: 0.14}; out: fade {duration: 0.12})
bgm#music(fade: 1200,3200) 落ち着いたミニマルな電子音の下地、柔らかく脈打つアナログシンセのアルペジオと温かいパッド、軽いキックと控えめなハイハットと低いベース、100 BPM の一定のテンポで盛り上がりのない、データ報告の解説向けの曲

# 全編の地 (根・z back): 点の格子の絵 (1.4 秒で明け、全編でゆっくり引く)・周辺減光
img#bg_plate(inset: 0; z-index: back; main: kb {scale: [1.17, 1.06], focus: ['50% 50%', '48% 50%']}; in: {opacity:0, duration:1.4, ease:'power2.out'}; out: none) [photo]データ分析の解説動画のための抽象的な背景。深い夜の紺から炭色へのグラデーション、遠くの地平へ遠近で消えていく小さな点の格子がかすかに並ぶ床、右下にとても柔らかい琥珀色の光、細かいフィルムの粒子、左の 3 分の 2 は静かな広い余白。文字・数字・ロゴ・人物・グラフは入れない
div#bg_vig(inset: 0; background: radial(#03060C00@55%,#03060CB3,45%,45%); z-index: back; in: none; out: none)

# 目盛りの輪 (12 本の目盛り + 地の輪) と AI の輪の地
svg dial = """<svg viewBox="0 0 200 200"><g stroke="#B9C3D58C" stroke-linecap="butt"><line x1="100" y1="10" x2="100" y2="19" stroke-width="3"/><line x1="145" y1="22.1" x2="142.5" y2="26.4" stroke-width="2"/><line x1="177.9" y1="55" x2="173.6" y2="57.5" stroke-width="2"/><line x1="190" y1="100" x2="181" y2="100" stroke-width="3"/><line x1="177.9" y1="145" x2="173.6" y2="142.5" stroke-width="2"/><line x1="145" y1="177.9" x2="142.5" y2="173.6" stroke-width="2"/><line x1="100" y1="190" x2="100" y2="181" stroke-width="3"/><line x1="55" y1="177.9" x2="57.5" y2="173.6" stroke-width="2"/><line x1="22.1" y1="145" x2="26.4" y2="142.5" stroke-width="2"/><line x1="10" y1="100" x2="19" y2="100" stroke-width="3"/><line x1="22.1" y1="55" x2="26.4" y2="57.5" stroke-width="2"/><line x1="55" y1="22.1" x2="57.5" y2="26.4" stroke-width="2"/></g><circle cx="100" cy="100" r="72" fill="none" stroke="#7D8CA838" stroke-width="14"/></svg>"""
svg ring = """<svg viewBox="0 0 160 160"><circle cx="80" cy="80" r="62" fill="none" stroke="#7D8CA838" stroke-width="16"/></svg>"""

# 場面の骨組み: 右上の章の番号 (場面ごとに入れ替え)・左上の番号 (琥珀 + 下線)・見出し・副題・題つきの板
def idx(t) = p(right: 53px; top: 21px; font-size: 13px; color: $fg2; letter-spacing: .06em; delay: 250; in: {y:8, opacity:0, duration:.45, ease:'power3.out'}; out: {y:-8, opacity:0, duration:.3, ease:'power2.in'}; content: {t})
def snum(t, w=26) = div(left: 53px; top: 88px; width: {w}; height: 32px; delay: 150; in: {x:-13, opacity:0, duration:.55, ease:'power3.out'})
  p#t(left: 0px; top: 0px; font-size: 20px; font-family: b; color: $amber; letter-spacing: .08em; line-height: 1.3; white-space: nowrap; content: {t})
  div#u(left: 0px; top: 30px; width: {w}; height: 2px; background: $amber)
def h2(t, x=97) = p(left: {x}; top: 59px; font-size: 36px; font-family: b; line-height: 1.18; letter-spacing: .01em; delay: 220; in: {y:19, opacity:0, duration:.7, ease:'expo.out'}; content: {t})
def hsub(t, x=97) = p(left: {x}; top: 105px; font-size: 17px; color: $fg2; delay: 340; in: {y:9, opacity:0, duration:.55, ease:'power3.out'}; content: {t})
def panel = div(background: $panel; border: 1px solid $line; border-radius: 12px; box-shadow: 0px 16px 40px #00000059; in: {y:24, opacity:0, duration:.6, ease:'power3.out'})
def ptitle(t) = p(left: 21px; top: 15px; font-size: 17px; font-family: b; content: {t})
def legend(t) = p(font-size: 13px; color: $fg2; in: {y:5, opacity:0, duration:.4, ease:'power3.out'}; content: {t})
def note(t) = p(font-size: 14px; color: $fg3; content: {t})
# 横棒の行: 札 (右揃え) + 縦の軸線 + 棒 (左から伸びる・CSS の scaleX 0 → 1) + 棒の右端に値。lw = 札の幅・x = 棒の始まり・w = 棒の長さ (値 ÷ 軸の最大 × 棒に使える幅を著者が計算)
def hbar(l, bw, v, lw=167, x=180, bh=25, ah=33, c=$slate2, vc=$fg, lc=$fg2, lo=1, ls=16, vs=19) = div(height: 39px)
  p#l(left: 0px; cy: 50%; width: {lw}; font-size: {ls}; color: {lc}; opacity: {lo}; text-align: right; white-space: nowrap; content: {l})
  div#ax(left: {x}; cy: 50%; width: 1.3px; height: {ah}; background: #A0B6DE59)
  div#b(left: {x}; cy: 50%; width: {bw}; height: {bh}; border-radius: 0,4,4,0; background: {c}; in: {scaleX:0, duration:.75, ease:'power3.out', pivot:'left'})
  p#v(left: .b.right+9; cy: 50%; font-size: {vs}; font-family: b; color: {vc}; line-height: 1; white-space: nowrap; delay: 450; in: {x:-8, opacity:0, duration:.3, ease:'power2.out'}; content: {v})
# 縦棒 (下から伸びる) と上の値・下の札
def vbar(c=$slate2) = div(width: 55px; border-radius: 5,5,0,0; background: {c}; in: {scaleY:0, duration:.75, ease:'power3.out', pivot:'bottom'})
def vval(t, c=$fg) = p(font-size: 20px; font-family: b; color: {c}; white-space: nowrap; in: {y:5, opacity:0, duration:.3, ease:'power2.out'}; content: {t})
def glab(t) = p(font-size: 15px; color: $fg2; white-space: nowrap; in: {y:5, opacity:0, duration:.35, ease:'power3.out'}; content: {t})
# 1 点 = 1 人の点 (grid に並べて左上から 8 ms ずつ弾んで出る)
def dot = div(border-radius: 99px; background: $slate2; in: {scale:0, opacity:0, duration:.25, ease:'back.out(1.7)', stagger: {each: .008}})

# title — 開幕: 地の絵が明け、左の余白に琥珀の点つきの前置き → mask から上がる 2 行の題 → 短い琥珀の罫 →「アンケート」で概要 →「結果」で 5 つの目次の札
section#title(stagger: {each:0})
# 琥珀の光の円: 場面ごとに 1 枚・前の場面の位置から 2.4 秒で次の位置へ動いて入る (2 場面目からは地を沈める幕の上なので濃さを 0.45 倍に)
div#glow_t.bleed(left: 833px; top: 373px; width: 600px; height: 600px; border-radius: 300px; background: radial(#F5B54438,#F5B5440F@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: none; out: none)
div#t_dot(left: 100px; top: 158px; width: 7px; height: 7px; border-radius: 4px; background: $amber; box-shadow: 0px 0px 12px $amber; delay: 250; in: {x:-20, opacity:0, duration:.6, ease:'power3.out'})
p#t_kicker(left: 118px; top: 151px; font-size: 16px; font-family: b; color: $amber; letter-spacing: .16em; delay: 250; in: {x:-20, opacity:0, duration:.6, ease:'power3.out'}) 社内共有レポート｜オンボーディング
p#t_l1(left: 100px; top: 197px; font-size: 77px; font-family: b; line-height: 1.14; letter-spacing: .01em; delay: 450; in: {y:97, duration:.9, ease:'expo.out', clip:true}) 登録時アンケート、
p#t_l2(left: 100px; top: 291px; font-size: 77px; font-family: b; line-height: 1.14; letter-spacing: .01em; delay: 590; in: {y:97, duration:.9, ease:'expo.out', clip:true}) {a}1週間{/}の結果
div#t_rule(left: 100px; top: 403px; width: 120px; height: 3px; background: $amber; delay: 950; in: {scaleX:0, duration:.7, ease:'power4.out', pivot:'left'})
p#t_sub(left: 100px; top: 427px; width: 880px; font-size: 20px; line-height: 1.6; color: $fg2; in: {y:12, opacity:0, duration:.7, ease:'power2.out'}) 登録直後に{w}用途・作りたい本数・知った経路{/}などを聞く短いアンケートを始めて1週間。答えた人の数と、課金との関係を見た。
p#t_chip(left: "100;270;447;651;813"; top: 529px; font-size: 15px; color: $fg2; background: #0D1424B3; border: 1px solid $line; border-radius: 99px; padding: 8px 16px; white-space: nowrap; in: {y:15, scale:.94, opacity:0, duration:.45, ease:'back.out(1.7)', stagger: {each: .09}}) ×5 {ab}01{/}　回答のファネル;{ab}02{/}　課金率への影響;{ab}03{/}　課金を予告する回答;{ab}04{/}　多数派の課金;{ab}05{/}　流入経路のずれ

# funnel — 01 回答のファネル: 常設の枠が入り、板の帯が伸びて同意 696 を数え →「586人」で完了の琥珀が伸び残りが割れる →「84%」→ 割れた 2 つに引き出し線と札 → 時間の板 (目盛りの輪) → 登録方法の横棒 2 本
section#funnel(stagger: {each:0})
div#glow_f.bleed(left: -200px; top: 253px; width: 600px; height: 600px; border-radius: 300px; background: radial(#F5B54438,#F5B5440F@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:1033, y:120, duration:2.4, ease:'sine.inOut'}; out: none)
# 地を沈める幕と常設の枠 (sticky・最後の cut の末尾で枠だけ消す)
div#bg_dim.sticky(inset: 0; background: #070B158C; z-index: back; in: {opacity:0, duration:1, ease:'power2.inOut'}; out: none)
div#prog_track.sticky(left: 0px; top: 0px; width: 1280px; height: 3px; background: #A0B6DE1A; z-index: front; in: none; out: {opacity:0, duration:.8})
progress#prog.sticky(left: 0px; top: 0px; width: 1280px; height: 3px; background: $amber; until: end; z-index: front; overlap: prog_track; out: {opacity:0, duration:.8})
p#crumb.sticky(left: 53px; top: 21px; font-size: 13px; color: $fg3; letter-spacing: .06em; z-index: front; delay: 200; in: {y:-7, opacity:0, duration:.55, ease:'power3.out'}; out: {opacity:0, duration:.8}) 登録時アンケート{a}　｜　{/}1週間の結果
idx#funnel_idx {ab}01 / 05{/}　回答のファネル
snum#funnel_n 01
h2#funnel_h 回答のファネル
hsub#funnel_s アンケートに同意した人は、どこまで答えたか
panel#fun(left: 53px; top: 146px; width: 1174px; height: 224px; delay: 200)
  ptitle#t 回答の状況{pn}　人数（同意した人に占める割合）{/}
  p#lab(left: 22px; top: 55px; font-size: 16px; color: $fg2; in: {y:7, opacity:0, duration:.4, ease:'power3.out'}) 同意
  p#n(left: 63px; top: 46px; font-size: 27px; font-family: b; line-height: 1.2; in: {y:7, opacity:0, duration:.4, ease:'power3.out'}) [count:696 start=0 ms=950]
  p#u(left: 112px; top: 55px; font-size: 16px; color: $fg2; in: {y:7, opacity:0, duration:.4, ease:'power3.out'}) 人
  p#drop_lab(right: 22px; top: 47px; font-size: 15px; color: $fg2; white-space: nowrap; in: {y:-8, opacity:0, duration:.4, ease:'power3.out'}) 途中離脱　{v19}27人{/}　{v19}3.9%{/}
  # 帯: 地 (slate) → 完了 84.2% (琥珀のグラデ) → 全部スキップ 11.9%・途中離脱 3.9% (左の縁は板の色)
  div#base(left: 22px; top: 88px; width: 1130px; height: 40px; border-radius: 5px; background: $slate; in: {scaleX:0, duration:.95, ease:'power3.inOut', pivot:'left'})
  div#done(left: 22px; top: 88px; width: 951px; height: 40px; border-radius: 5,0,0,5; background: linear($am0,#F5B544,90); in: {scaleX:0, duration:.85, ease:'power3.inOut', pivot:'left'})
    p#lab(left: 19px; cy: 50%; font-size: 17px; font-family: b; color: $ink; in: {x:-7, opacity:0, duration:.35}) 完了
  div#skip(left: 973px; top: 88px; width: 134px; height: 40px; background: $slate2; edge: left,3,$edge; in: {opacity:0, duration:.45, ease:'power2.out'})
  div#drop(left: 1107px; top: 88px; width: 45px; height: 40px; border-radius: 0,5,5,0; background: $drop; edge: left,3,$edge; in: {opacity:0, duration:.45, ease:'power2.out'})
  div#lead_drop(left: 1129px; top: 77px; width: 1.5px; height: 11px; background: $fg3; in: {scaleY:0, duration:.3, ease:'power2.out', pivot:'bottom'})
  div#lead_skip(left: 1040px; top: 128px; width: 1.5px; height: 17px; background: $fg3; in: {scaleY:0, duration:.3, ease:'power2.out', pivot:'top'})
  p#big(left: 22px; top: 135px; font-size: 64px; font-family: b; line-height: 1; letter-spacing: -.01em; color: $amber; in: {y:16, opacity:0, duration:.5, ease:'back.out(1.7)'}) [count:84 start=0 ms=800]{pc}%{/}
  p#cap(left: 147px; top: 172px; font-size: 17px; color: $fg2; white-space: nowrap; in: {x:-9, opacity:0, duration:.45, ease:'power3.out'}) 最後まで完了　{v21}586人{/}
  p#skip_lab(right: 66px; top: 155px; font-size: 15px; color: $fg2; white-space: nowrap; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) 全部スキップ　{v19}83人{/}　{v19}12%{/}
#fun.skip.lit(background: $lit)
# 回答時間の板: 60 秒の目盛りの輪に 21 秒の弧を描き、数字を数える
panel#time(left: 53px; top: 387px; width: 374px; height: 245px)
  ptitle#t 回答にかかった時間{pn}　中央値{/}
  svg#dial(left: 22px; top: 68px; width: 127px; height: 127px; part: dial)
  shape#arc(path: "M 86 86.3 C 111.2 86.3 131.7 106.8 131.7 132 C 131.7 141.7 128.6 151.1 123 158.9"; z-index: front; background: none; border: 9px solid $amber; in: draw {duration: 0.9, ease: 'power2.out'})
  p#num(left: 169px; top: 92px; font-size: 69px; font-family: b; line-height: 1; in: {y:20, opacity:0, duration:.55, ease:'power3.out'}) [count:21 start=0 ms=900]{sec}秒{/}
  p#sub(left: 169px; top: 164px; font-size: 14px; color: $fg3) 目盛りは 1 分
# 登録方法別の全部スキップ (横軸 0〜40%)
panel#meth(left: 443px; top: 387px; width: 784px; height: 245px)
  ptitle#t 登録方法別「全部スキップ」の割合{pn}　各登録方法の人のうち{/}
  hbar#mail(left: 21px; top: 79px; width: 742px; l: "メール＋パスワード"; bw: 407; v: "29%"; c: "linear($am1,#F5B544,90)"; vc: $amber)
  hbar#google(left: 21px; top: 126px; width: 742px; l: "Google 等のログイン"; bw: 112; v: "8%")
  note#note(left: 21px; top: 205px; in: {y:7, opacity:0, duration:.4, ease:'power3.out'}) スキップは、メールとパスワードで登録した人に多い

# paid — 02 課金率は動いていない: 縦棒の組 2 つ (前 → 後) と「有意差なし」の札 → 100 マスの waffle が 77 → 65 に減る (減った分は枠だけ) → 作った人の縦棒 2 本が同じ高さ → 結論の帯
section#paid(stagger: {each:0})
div#glow_p.bleed(left: 866px; top: -167px; width: 600px; height: 600px; border-radius: 300px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:-1066, y:420, duration:2.4, ease:'sine.inOut'}; out: none)
idx#paid_idx {ab}02 / 05{/}　課金率への影響
snum#paid_n 02
h2#paid_h 課金率は動いていない
hsub#paid_s アンケート開始前 → 開始後の比較
panel#rate(left: 53px; top: 146px; width: 421px; height: 424px; delay: 300)
  ptitle#t 登録からの課金率
  div#axis(left: 30px; top: 367px; width: 361px; height: 1.5px; background: #A0B6DE59)
legend#rate_lg(left: 76px; top: 192px; delay: 600) {sl}■{/} 開始前　{a}■{/} 開始後
# 縦棒の高さ = 値 × 33.3 px (hf の 50 px / 1 % の 2/3)
vbar#r24a(left: 114px; top: 371px; height: 143px)
vbar#r24b(left: 178px; top: 411px; height: 103px; c: "linear($am0,#F5B544,0)")
vbar#r3a(left: 295px; top: 351px; height: 163px)
vbar#r3b(left: 359px; top: 391px; height: 123px; c: "linear($am0,#F5B544,0)")
vval#r24a_v(cx: 141px; top: 338px) 4.3%
vval#r24b_v(cx: 205px; top: 378px; c: $amber) 3.1%
vval#r3a_v(cx: 322px; top: 318px) 4.9%
vval#r3b_v(cx: 386px; top: 358px; c: $amber) 3.7%
glab#g24_lab(cx: 173px; top: 522px) 24時間以内
glab#g3_lab(cx: 354px; top: 522px) 3日以内
p#ns24(cx: 173px; top: 276px; font-size: 14px; font-family: b; background: #0D1424E6; border: 1.3px solid $fg3; border-radius: 99px; padding: 4px 11px; white-space: nowrap; in: {scale:.6, opacity:0, duration:.45, ease:'back.out(1.7)'}) 有意差なし
p#ns3(cx: 354px; top: 276px; font-size: 14px; font-family: b; background: #0D1424E6; border: 1.3px solid $fg3; border-radius: 99px; padding: 4px 11px; white-space: nowrap; in: {scale:.6, opacity:0, duration:.45, ease:'back.out(1.7)'}) 有意差なし
# 24 時間以内に動画を作った人: 100 マス (1 マス = 1%)・65 マス (A) と減った 12 マス (B) と残り 23 マス (C) に分けて塗り替える
panel#made(left: 490px; top: 146px; width: 376px; height: 424px)
  ptitle#t 24時間以内に動画を1本作った人
p#wf_a(left: 512px; top: 205px; font-size: 43px; font-family: b; line-height: 1; color: $slate2; in: {y:9, opacity:0, duration:.4, ease:'power3.out'}) 77%
p#wf_arrow(left: 615px; top: 216px; font-size: 27px; line-height: 1; color: $fg3; in: {x:-8, opacity:0, duration:.35, ease:'power3.out'}) →
p#wf_b(left: 655px; top: 205px; font-size: 43px; font-family: b; line-height: 1; color: $amber; in: {y:9, opacity:0, duration:.4, ease:'back.out(1.7)'}) 65%
div#wfa(left: "576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8"; top: "264;264;264;264;264;264;264;264;264;264;284.7;284.7;284.7;284.7;284.7;284.7;284.7;284.7;284.7;284.7;305.4;305.4;305.4;305.4;305.4;305.4;305.4;305.4;305.4;305.4;326.1;326.1;326.1;326.1;326.1;326.1;326.1;326.1;326.1;326.1;346.8;346.8;346.8;346.8;346.8;346.8;346.8;346.8;346.8;346.8;367.5;367.5;367.5;367.5;367.5;367.5;367.5;367.5;367.5;367.5;388.2;388.2;388.2;388.2;388.2"; width: 17px; height: 17px; border-radius: 3px; background: $empty; in: {scale:.4, opacity:0, duration:.3, ease:'power2.out', stagger: {each: .004}}) ×65
div#wfb(left: "679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2"; top: "388.2;388.2;388.2;388.2;388.2;408.9;408.9;408.9;408.9;408.9;408.9;408.9"; width: 17px; height: 17px; border-radius: 3px; background: $empty; in: {scale:.4, opacity:0, duration:.3, ease:'power2.out', stagger: {each: .004}}) ×12
#wfa.was(background: $slate2)
#wfa.made(background: $amber)
#wfb.was(background: $slate2)
#wfb.gone(background: #7D8CA81A; border: 1px solid #B9C3D599)
div#wfc(left: "720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3"; top: "408.9;408.9;408.9;429.6;429.6;429.6;429.6;429.6;429.6;429.6;429.6;429.6;429.6;450.3;450.3;450.3;450.3;450.3;450.3;450.3;450.3;450.3;450.3"; width: 17px; height: 17px; border-radius: 3px; background: $empty; in: {scale:.4, opacity:0, duration:.3, ease:'power2.out', stagger: {each: .004}}) ×23
legend#wf_leg(cx: 677px; top: 478px) {a}■{/} 作った人（開始後）　□ 減った分
note#made_note(left: 512px; top: 532px; in: {y:7, opacity:0, duration:.4, ease:'power3.out'}) 作らない人が増え、全体の課金率が薄まった（希釈）
# 動画を作った人の 24 時間課金率 (ほぼ同じ高さの 2 本)
panel#cre(left: 882px; top: 146px; width: 345px; height: 424px)
  ptitle#t 動画を作った人の24時間課金率
  div#axis(left: 28px; top: 367px; width: 288px; height: 1.5px; background: #A0B6DE59)
legend#cre_lg(left: 904px; top: 192px) {sl}■{/} 開始前　{a}■{/} 開始後
p#same(cx: 1054px; top: 218px; font-size: 20px; font-family: b; color: $amber_hi; white-space: nowrap; in: {scale:.7, opacity:0, duration:.45, ease:'back.out(1.7)'}) ≈ ほぼ同じ
vbar#c475(left: 984px; top: 356px; height: 158px)
vbar#c457(left: 1070px; top: 362px; height: 152px; c: "linear($am0,#F5B544,0)")
vval#c475_v(cx: 1011px; top: 323px) 4.75%
vval#c457_v(cx: 1097px; top: 329px; c: $amber) 4.57%
glab#cre_lab(cx: 1054px; top: 522px) 動画を作った人
p#insight(left: 53px; top: 587px; font-size: 18px; background: #F5B54429; border: 1px solid #F5B54473; border-radius: 9px; padding: 9px 19px; white-space: nowrap; in: {x:-20, opacity:0, duration:.6, ease:'expo.out'}) {ab}→{/}　下がって見えるのは希釈。アンケートは課金率を下げていない

# pred — 03 課金を予告する回答: 1 枚の板に 4 段の組 (題・札は 0.38 で薄く先出し) → 読む語で札を点灯して棒を伸ばす → 最後の段 (太い棒 + 光) を「21.7%」で弾ませる
section#pred(stagger: {each:0})
div#glow_r.bleed(left: 900px; top: 280px; width: 600px; height: 600px; border-radius: 300px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:-34, y:-447, duration:2.4, ease:'sine.inOut'}; out: none)
idx#pred_idx {ab}03 / 05{/}　課金を予告する回答
snum#pred_n 03
h2#pred_h 課金を予告する回答
hsub#pred_s 回答別に見た、登録から3日以内の課金率
panel#pr(left: 53px; top: 146px; width: 1174px; height: 486px; delay: 300)
  ptitle#t 3日以内の課金率{pn}　回答別{/}
legend#pr_lg(right: 75px; top: 166px; delay: 600) {a}■{/} 課金を予告する回答　{sl}■{/} 比べる回答
# 段の組 (上の罫 + 題 + 行 2 本)・横軸 0〜25% = 棒に使える幅 782 px
div#g_org(left: 76px; top: 201px; width: 1129px; height: 86px; delay: 450; in: {y:11, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1129px; height: 1px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 15px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 利用形態
  hbar#sig(left: 133px; top: 8px; width: 996px; height: 33px; l: "組織で使う"; bw: 416; v: "13.3%"; lw: 200; x: 213; bh: 23; ah: 31; c: "linear($am1,#F5B544,90)"; vc: $amber; lo: .38)
  hbar#cmp(left: 133px; top: 45px; width: 996px; height: 33px; l: "個人"; bw: 119; v: "3.8%"; lw: 200; x: 213; bh: 23; ah: 31; lo: .38)
div#g_num(left: 76px; top: 307px; width: 1129px; height: 86px; delay: 530; in: {y:11, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1129px; height: 1px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 15px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 作りたい本数
  hbar#sig(left: 133px; top: 8px; width: 996px; height: 33px; l: "月4本以上"; bw: 253; v: "8.1%"; lw: 200; x: 213; bh: 23; ah: 31; c: "linear($am1,#F5B544,90)"; vc: $amber; lo: .38)
  hbar#cmp(left: 133px; top: 45px; width: 996px; height: 33px; l: "未定"; bw: 2; v: "0%"; lw: 200; x: 213; bh: 23; ah: 31; lo: .38)
div#g_use(left: 76px; top: 412px; width: 1129px; height: 86px; delay: 610; in: {y:11, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1129px; height: 1px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 15px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 用途
  hbar#sig(left: 133px; top: 8px; width: 996px; height: 33px; l: "ビジネス用途を含む"; bw: 400; v: "12.8%"; lw: 200; x: 213; bh: 23; ah: 31; c: "linear($am1,#F5B544,90)"; vc: $amber; lo: .38)
  hbar#cmp(left: 133px; top: 45px; width: 996px; height: 33px; l: "エンタメ系のみ"; bw: 113; v: "3.6%"; lw: 200; x: 213; bh: 23; ah: 31; lo: .38)
# 主役の段: 札は太字の白・棒は太く琥珀の光・値は大きな淡い琥珀 (「21.7%」の語で弾む)
div#g_prod(left: 76px; top: 517px; width: 1129px; height: 58px; delay: 690; in: {y:11, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1129px; height: 1px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 15px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 単独で選んだ
  hbar#sig(left: 133px; top: 8px; width: 996px; height: 44px; l: "商品・サービス紹介"; bw: 679; v: "21.7%"; lw: 200; x: 213; bh: 33; ah: 41; c: "linear($am1,#F5B544,90)"; vc: $amber_hi; lc: $fg; lo: .38; ls: 17; vs: 33)
    p#l(font-family: b)
    div#b(box-shadow: 0px 0px 23px #F5B54473; in: {scaleX:0, duration:1.1, ease:'power3.inOut', pivot:'left'})
    p#v(delay: 0; in: {scale:.6, opacity:0, duration:.5, ease:'back.out(1.7)', pivot:'left'})
note#pr_note(left: 76px; top: 595px; in: {y:5, opacity:0, duration:.4, ease:'power3.out'}) ビジネス用途＝商品紹介・会社紹介・研修　／　横軸は 0〜25%

# major — 04 多数派は課金しない: 左の板に用途の上位 4 本の棒 → 右の板に 1 点 = 1 人の点を 3 組 (語ごとに 8 ms ずつ弾んで出る) → アニメの 1 点だけ琥珀に光る →「ゼロ」で課金 0 人の札
section#major(stagger: {each:0})
div#glow_m.bleed(left: -167px; top: 333px; width: 600px; height: 600px; border-radius: 300px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:1067, y:-53, duration:2.4, ease:'sine.inOut'}; out: none)
idx#major_idx {ab}04 / 05{/}　多数派の課金
snum#major_n 04
h2#major_h 多数派は課金しない
hsub#major_s よく選ばれる用途と、その課金人数
panel#top(left: 53px; top: 146px; width: 475px; height: 486px; delay: 300)
  ptitle#t 用途の上位{pn}　回答者に占める割合{/}
  hbar#u(left: 23px; top: "115;186;256;327"; width: 429px; height: 61px; l: "エンタメ;アニメクリップ;ストーリー;解説"; bw: "230;181;181;181"; v: "19%;15%;15%;15%"; lw: 113; x: 127; bh: 31; ah: 39; vs: 21) ×4
  note#note(left: 23px; top: 449px; in: {y:5, opacity:0, duration:.4, ease:'power3.out'}) 横軸は 0〜25%
panel#dots(left: 544px; top: 146px; width: 683px; height: 486px; delay: 420)
  ptitle#t 選んだ人と、課金した人{pn}　1点＝1人{/}
legend#dots_lg(right: 75px; top: 166px; delay: 700) {sl}■{/} 課金なし　{a}■{/} 課金あり
p#ent_h(left: 566px; top: 259px; font-size: 15px; color: $fg2; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) エンタメだけ
p#ent_n(left: 566px; top: 281px; font-size: 23px; font-family: b; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) 63人
dot#ent_d(left: "566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4"; top: "319;319;319;319;319;319;319;319;319;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;375;375;375;375;375;375;375;375;375;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;431;431;431;431;431;431;431;431;431"; width: 13px; height: 13px) ×63
p#ani_h(left: 789px; top: 259px; font-size: 15px; color: $fg2; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) アニメ
p#ani_n(left: 789px; top: 281px; font-size: 23px; font-family: b; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) 50人
dot#ani_d(left: "789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957"; top: "319;319;319;319;319;319;319;319;319;319;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;375;375;375;375;375;375;375;375;375;375;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7"; width: 13px; height: 13px) ×50
p#und_h(left: 1012px; top: 259px; font-size: 15px; color: $fg2; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) 作りたい本数「未定」
p#und_n(left: 1012px; top: 281px; font-size: 23px; font-family: b; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) 81人
dot#und_d(left: "1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4"; top: "319;319;319;319;319;319;319;319;319;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;375;375;375;375;375;375;375;375;375;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;431;431;431;431;431;431;431;431;431;449.7;449.7;449.7;449.7;449.7;449.7;449.7;449.7;449.7;468.4;468.4;468.4;468.4;468.4;468.4;468.4;468.4;468.4"; width: 13px; height: 13px) ×81
# 課金の札 (上の罫 + 課金 N 人)
div#ent_f(left: 566px; top: 491px; width: 194px; height: 50px; in: {y:7, opacity:0, duration:.45, ease:'back.out(1.7)'})
  div#ln(left: 0px; top: 0px; width: 194px; height: 1px; background: $line)
  p#t(left: 0px; top: 12px; font-size: 16px; color: $fg2) 課金 {n27}0人{/}
div#ani_f(left: 789px; top: 491px; width: 194px; height: 50px; in: {y:7, opacity:0, duration:.4, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 194px; height: 1px; background: $line)
  p#t(left: 0px; top: 12px; font-size: 16px; color: $fg2) 課金 {n27a}1人{/}
div#und_f(left: 1012px; top: 491px; width: 194px; height: 50px; in: {y:7, opacity:0, duration:.45, ease:'back.out(1.7)'})
  div#ln(left: 0px; top: 0px; width: 194px; height: 1px; background: $line)
  p#t(left: 0px; top: 12px; font-size: 16px; color: $fg2) 課金 {n27}0人{/}

# route — 05 流入経路のずれ: 計測 67% と自己申告 23% の棒 → 差を破線の枠と斜線で「← ずれ」→ 自己申告の上位 5 本 → 右の板で AI アシスタントの数字 3 つ (札は薄く先出し・輪の弧・数え上げ)
section#route(stagger: {each:0})
div#glow_o.bleed(left: 800px; top: 300px; width: 600px; height: 600px; border-radius: 300px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:-967, y:33, duration:2.4, ease:'sine.inOut'}; out: none)
idx#route_idx {ab}05 / 05{/}　流入経路のずれ
snum#route_n 05
h2#route_h 流入経路は、自己申告と計測がずれる
hsub#route_s 「どこで知ったか」の自己申告と、GA の計測
panel#gap(left: 53px; top: 146px; width: 672px; height: 144px; delay: 300)
  ptitle#t 「検索」経由の割合{pn}　計測と自己申告{/}
  hbar#ga(left: 23px; top: 49px; width: 627px; height: 36px; l: "計測（GA）自然検索"; bw: 300; v: "67%"; lw: 167; x: 180; bh: 24; ah: 32; c: "linear($st0,#6FA8DC,90)"; vc: $steel)
    p#l(in: {x:-7, opacity:0, duration:.35, ease:'power3.out'})
    div#b(in: {scaleX:0, duration:.9, ease:'power3.out', pivot:'left'})
    p#v(delay: 540)
  # 差の枠: 斜線の地 + 破線の縁 (左から伸びる)・右に「← ずれ」
  div#zone(left: 306px; top: 95px; width: 197px; height: 29px; border-radius: 4px; background: #F5B5440A; pattern: hatch,45,#F5B5441F,11,5; overlap: gap.self; in: {scaleX:0, opacity:0, duration:.6, ease:'power2.out', pivot:'left'})
  shape#dash(left: 306px; top: 95px; width: 197px; height: 29px; path: rect,r=0.14; background: none; border: 1.3px solid #F5B544BF; dash: 5,4; overlap: gap.zone; in: {scaleX:0, opacity:0, duration:.6, ease:'power2.out', pivot:'left'})
  hbar#self(left: 23px; top: 91px; width: 627px; height: 36px; l: "自己申告「検索」"; bw: 103; v: "23%"; lw: 167; x: 180; bh: 24; ah: 32; c: "linear($am1,#F5B544,90)"; vc: $amber)
    p#l(in: {x:-7, opacity:0, duration:.35, ease:'power3.out'})
    div#b(in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(delay: 360)
  p#lab(left: 514px; top: 98px; font-size: 16px; font-family: b; color: $amber_hi; white-space: nowrap; in: {scale:.6, opacity:0, duration:.4, ease:'back.out(1.7)'}) ← ずれ
panel#rank(left: 53px; top: 306px; width: 672px; height: 326px)
  ptitle#t 自己申告の流入経路{pn}　上位5つ{/}
  hbar#r(left: 23px; top: "78;118;158;198;238"; width: 640px; height: 37px; l: "検索;AIアシスタント;Web記事;X;YouTube"; bw: "443;308;250;231;212"; v: "23%;16%;13%;12%;11%"; c: "$slate2;linear($am1,#F5B544,90);$slate2;$slate2;$slate2"; vc: "$fg;$amber;$fg;$fg;$fg"; lw: 133; x: 147; bh: 23; ah: 31; vs: 17) ×5
    div#b(in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(delay: 360)
# AI アシスタントで知った人: 3 段 (16% / 輪の弧 84% / 7.8%)・札は 0.35 で薄く先出し・「AI」で板の縁が琥珀に
panel#ai(left: 741px; top: 146px; width: 486px; height: 486px; in: {x:27, opacity:0, duration:.6, ease:'power3.out'})
  ptitle#t AIアシスタントで知った人
  p#big(left: 22px; top: 64px; font-size: 61px; font-family: b; line-height: 1; color: $amber; in: {y:9, opacity:0, duration:.45, ease:'back.out(1.7)'}) [count:16 start=0 ms=600]{pc}%{/}
  p#share(left: 136px; top: 98px; font-size: 15px; line-height: 1.45; color: $fg2; opacity: .35) 自己申告の流入経路に[br]占める割合
  div#ln1(left: 22px; top: 160px; width: 443px; height: 1px; background: $line)
  svg#ring(left: 22px; top: 172px; width: 120px; height: 120px; part: ring)
  shape#arc(path: "M 82 185.5 C 107.7 185.5 128.5 206.3 128.5 232 C 128.5 257.7 107.7 278.5 82 278.5 C 56.3 278.5 35.5 257.7 35.5 232 C 35.5 223.2 38 214.5 42.7 207.1"; z-index: front; background: none; border: 12px solid $amber; in: draw {duration: 1, ease: 'power2.out'})
  p#num(left: 160px; top: 197px; font-size: 48px; font-family: b; line-height: 1.15; in: {y:9, opacity:0, duration:.4, ease:'power3.out'}) [count:84 start=0 ms=1000]{pc}%{/}
  p#lab1(left: 160px; top: 255px; font-size: 15px; color: $fg2; opacity: .35) 24時間以内の生成到達
  div#ln2(left: 22px; top: 310px; width: 443px; height: 1px; background: $line)
  p#paid(left: 22px; top: 330px; font-size: 48px; font-family: b; line-height: 1.15; color: $amber; in: {y:9, opacity:0, duration:.4, ease:'back.out(1.7)'}) [count:7.8 start=0 ms=700]{pc}%{/}
  p#lab2(left: 132px; top: 343px; font-size: 15px; color: $fg2; opacity: .35) 24時間以内の課金
  note#note(left: 22px; top: 449px; in: {y:5, opacity:0, duration:.4, ease:'power3.out'}) 生成到達・課金とも高い水準
#ai.on(border: 1px solid #F5B5448C)

# sum — まとめ: 3 枚の札を行の頭で 1 枚ずつ (札が上がり、中身が 70 ms ずつ続く)・最後は常設の枠を消して黒へ
section#sum(stagger: {each:0})
div#glow_s.bleed(left: 346px; top: 200px; width: 600px; height: 600px; border-radius: 300px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:454, y:100, duration:2.4, ease:'sine.inOut'}; out: none)
idx#sum_idx(out: {opacity:0, duration:.8}) {ab}まとめ{/}　1週間でわかったこと
snum#sum_n(w: 59) まとめ
h2#sum_h(x: 130) 1週間でわかったこと
hsub#sum_s(x: 130) 登録時アンケートの結果から
panel#c1(left: 53px; top: 189px; width: 381px; height: 400px; in: {y:33, opacity:0, duration:.65, ease:'expo.out'})
  div#n(left: 24px; top: 21px; width: 36px; height: 36px; border-radius: 18px; border: 1.3px solid $amber; delay: 200; in: {y:9, opacity:0, duration:.4, ease:'power2.out'})
    p#t(cx: 50%; cy: 50%; font-size: 19px; font-family: b; color: $amber) 1
  p#k(left: 24px; top: 70px; font-size: 67px; font-family: b; line-height: 1.05; color: $amber; delay: 270; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) 84{pc}%{/}
  p#ksub(left: 24px; top: 146px; font-size: 15px; color: $fg2; delay: 340; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) が最後まで回答
  p#h(left: 24px; top: 185px; width: 334px; font-size: 27px; font-family: b; line-height: 1.42; delay: 410; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) アンケートは課金率を[br]下げていない
  p#act(left: 24px; top: 332px; width: 334px; font-size: 15px; color: $fg2; background: #7D8CA81F; border: 1px solid #A0B6DE47; border-radius: 8px; padding: 10px 12px; delay: 480; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) 下がって見えたのは、作る人が減った希釈
panel#c2(left: 450px; top: 189px; width: 381px; height: 400px; in: {y:33, opacity:0, duration:.65, ease:'expo.out'})
  div#n(left: 24px; top: 21px; width: 36px; height: 36px; border-radius: 18px; border: 1.3px solid $amber; delay: 200; in: {y:9, opacity:0, duration:.4, ease:'power2.out'})
    p#t(cx: 50%; cy: 50%; font-size: 19px; font-family: b; color: $amber) 2
  p#tg(left: "23;90;201"; top: 102px; font-size: 17px; font-family: b; color: $amber_hi; background: #F5B54429; border: 1px solid #F5B54480; border-radius: 7px; padding: 5px 12px; white-space: nowrap; delay: 270; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) ×3 組織;月4本以上;ビジネス用途
  p#h(left: 24px; top: 152px; width: 334px; font-size: 27px; font-family: b; line-height: 1.42; delay: 340; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) この回答が課金を予告する
  p#act(left: 24px; top: 330px; width: 334px; font-size: 17px; background: #F5B5441F; border: 1px solid #F5B54459; border-radius: 8px; padding: 9px 12px; delay: 410; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) {ab}→{/} 有料の案内を早く出す
panel#c3(left: 846px; top: 189px; width: 381px; height: 400px; in: {y:33, opacity:0, duration:.65, ease:'expo.out'})
  div#n(left: 24px; top: 21px; width: 36px; height: 36px; border-radius: 18px; border: 1.3px solid $amber; delay: 200; in: {y:9, opacity:0, duration:.4, ease:'power2.out'})
    p#t(cx: 50%; cy: 50%; font-size: 19px; font-family: b; color: $amber) 3
  p#k(left: 24px; top: 70px; font-size: 67px; font-family: b; line-height: 1.05; white-space: nowrap; delay: 270; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) {s}67{/}{pcs}%{/}{vs}　vs　{/}{a}23{/}{pca}%{/}
  p#ksub(left: 24px; top: 146px; font-size: 15px; color: $fg2; delay: 340; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) GA の自然検索 ／ 自己申告の検索
  p#h(left: 24px; top: 185px; width: 334px; font-size: 27px; font-family: b; line-height: 1.42; delay: 410; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) 流入経路は[br]自己申告と計測がずれる
  p#act(left: 24px; top: 330px; width: 334px; font-size: 17px; background: #F5B5441F; border: 1px solid #F5B54459; border-radius: 8px; padding: 9px 12px; delay: 480; in: {y:9, opacity:0, duration:.4, ease:'power2.out'}) {ab}→{/} AIアシスタント経由が伸びている
```

```timeline.txt
#v2
cast n = "明るく澄んだ若い女性のナレーター、落ち着いて明瞭に、社内向けの報告をテンポよく読む" speed=110%
silence head=0 tail=0
# 切替: 旧場面が溶けて新場面が出る上を、琥珀の光の帯が左から右へ払う (hf の cross fade + sweep・帯は溶けと独立・境目で風切り)
transition = dissolve,850,dir=right,overlap=850,ease=power2.inOut,bars=linear(#F5B54400,#F5B5441A@60%,#FFD27F8C@97%,#FFD27F00),173,se=whoosh -4dB

# title — 題は頭に組み上がり、「アンケート」で概要・「結果」で目次の札 5 つ
*** title
[>#subtitle]
bgm music
se hit -3dB +250
@n: [silence:1.0s]登録時[>#t_sub +340]アンケート、1週間の[>#t_chip[*] +140][♪swipe -4dB +140]結果です。[silence:1.3s]

# funnel — 頭で帯の地が伸びて 696 を数え、「586人」で完了の琥珀・「84%」で大きな数字・割れた 2 つに引き出し線と札・時間の板と弧・登録方法の棒 2 本
*** funnel
@n: [silence:0.75s][>#fun.base -400][♪rise -7dB -400][>#fun.lab -300][>#fun.n -300][>#fun.u -300]同意した696人のうち、[>#fun.done -100][>#fun.done.lab +450][>#fun.skip +350][>#fun.drop +470][♪blip -6dB]586人、[>#fun.big count -120][>#fun.cap +250][♪tick -8dB]84%が最後まで答えました。[silence:0.3s]
@: [>#fun.lead_skip -100][>#fun.skip_lab][!#fun.skip .lit][=#fun.skip +300][♪blip -8dB]全部スキップは12%、[>#fun.lead_drop -100][>#fun.drop_lab][♪blip -8dB]途中離脱は3.9%。[>#time -200][♪swipe -6dB -200]回答時間の中央値は[>#time.arc -100][>#time.num count -100][♪tick -8dB]21秒です。[silence:0.3s]
@: [>#meth -100][♪swipe -6dB -100]スキップはメール登録に多く[bar #meth.mail -150][♪blip -7dB]29%、[bar #meth.google -100][>#meth.note +500][♪blip -8dB]Googleなどのログインでは8%です。[silence:0.3s]

# paid — 「24時間以内」「3日以内」で縦棒の組・「有意差」で札・2 文目の頭で waffle が組み上がり「77%」で灰・「65%」で減った枠と琥珀・3 文目で作った人の 2 本と「ほぼ同じ」
*** paid
@n: [silence:0.75s]課金率は、[>#r24a -50][>#r24b +230][>#r24a_v +500][>#r24b_v +780][>#g24_lab -50][♪rise -9dB]24時間以内が4.3%から3.1%、[>#r3a -50][>#r3b +230][>#r3a_v +500][>#r3b_v +780][>#g3_lab -50][♪rise -9dB]3日以内が4.9%から3.7%。どちらも[>#ns24][>#ns3 +120][♪chime -8dB]有意差はありません。[silence:0.3s]
@: [>#made -150][>#wfa[*]][>#wfb[*] +260][>#wfc[*] +308][♪swipe -6dB -150]下がって見えるのは、動画を作る人が[!#wfa[*] .was stagger=6 -200][!#wfb[*] .was stagger=6 +190][>#wf_a -100][♪blip -8dB]77%から[>#wf_arrow -200][!#wfb[*] .gone stagger=30 -100][!#wfa[*] .made stagger=5 +100][>#wf_b][>#wf_leg +300][♪tick -8dB]65%に減った[>#made_note -200]希釈です。[silence:0.3s]
@: [>#cre -150][>#cre_lg +150][♪swipe -6dB -150]作った人に限れば、[>#c475 -100][>#c475_v +400][>#cre_lab][♪blip -8dB]4.75%と[>#c457 -100][>#c457_v +400][♪blip -8dB]4.57%。[||][>#same][>#insight +500][♪chime -7dB]ほぼ同じです。[silence:0.6s]

# pred — 読む語で段の題と札を点灯して棒を伸ばす (比べる回答も同じ)・「商品」で太い棒・「21.7%」で値が弾む
*** pred
@n: [silence:0.75s]課金を予告する回答もあります。[!#g_org.cat to,{opacity:1, duration:.3} -100][lit #g_org.sig][♪rise -9dB]組織で使う人は13.3%、[lit #g_org.cmp][♪blip -9dB]個人は3.8%。[silence:0.3s]
@: [!#g_num.cat to,{opacity:1, duration:.3} -100][lit #g_num.sig][♪rise -9dB]月に4本以上なら8.1%、[lit #g_num.cmp][♪blip -9dB]未定は0%。[silence:0.3s]
@: [!#g_use.cat to,{opacity:1, duration:.3} -100][lit #g_use.sig][lit #g_use.cmp +800][♪rise -9dB]ビジネス用途を含むと12.8%、[!#g_prod.cat to,{opacity:1, duration:.3} -100][!#g_prod.sig.l to,{opacity:1, duration:.3} -100][>#g_prod.sig.b][♪rise -8dB]商品・サービス紹介だけなら[>#g_prod.sig.v -100][>#pr_note +600][♪chime -6dB]21.7%です。[silence:0.8s]

# major — 頭で上位 4 本の棒・語ごとに点の組 (アニメの 1 点は琥珀に光る)・「ゼロ」で課金 0 人の札 2 枚
*** major
@n: [silence:0.75s][bar #top.u[1] -300][bar #top.u[2] -160][bar #top.u[3] -20][bar #top.u[4] +120][>#top.note +600][♪rise -9dB -300]一方、多数派は課金しません。[>#ent_h -100][>#ent_n -100][>#ent_d[*]][♪blip -8dB]エンタメだけの[>#ani_h +80][>#ani_n +80][>#ani_d[*] +180][!#ani_d[1] fill,$amber +730][!#ani_d[1] to,{scale:1.25, duration:.35, ease:'back.out'} +730][!#ani_d[1] glow,$amber,blur=11 +730][>#ani_f +780][♪blip -9dB +180]63人も、[>#und_h -100][>#und_n -100][>#und_d[*]][♪blip -8dB]本数未定の81人も、課金は[>#ent_f -150][>#und_f -50][♪hit -12dB -150]ゼロでした。[silence:1.2s]
# この境目だけ混ぜない切替: 旧場面は境目から一斉に上へ抜け (hf の leave は境目から 0.32 s)、新場面の上に重なる (光の帯は無し)
transition none,320,se=whoosh -4dB

# route — 1 文目の「自己申告」で下と右の板・「GA」「自己申告」で棒・文末で差の枠と「← ずれ」・2 行目は AI の数字を語ごとに点灯して数える
*** route
@n: [silence:0.75s]流入経路は、計測と[>#rank -100][bar #rank.r[1] +500][bar #rank.r[2] +620][bar #rank.r[3] +740][bar #rank.r[4] +860][bar #rank.r[5] +980][>#ai +250][♪swipe -7dB]自己申告が食い違います。[>#gap.ga.l -200][bar #gap.ga][♪rise -9dB]GAでは自然検索が67%、[>#gap.self.l -200][bar #gap.self][♪rise -9dB]自己申告の検索は23%[>#gap.zone][>#gap.dash][>#gap.lab +400][♪blip -8dB]です。[silence:0.3s]
@: [!#rank.r[2].l recolor,$amber_hi,duration=300][!#ai .on][♪blip -8dB]AIアシスタント経由は[>#ai.big count -150][!#ai.share to,{opacity:1, duration:.3} -150][!#rank.r[2].b glow,#FFD27F,blur=14][=#rank.r[2].b +350][♪blip -8dB]16%。[>#ai.arc -100][>#ai.num count -150][!#ai.lab1 to,{opacity:1, duration:.3} -150][♪tick -9dB]生成到達84%、[>#ai.paid -150][!#ai.lab2 to,{opacity:1, duration:.3} -150][>#ai.note +900][♪blip -8dB]課金7.8%と、質の高い層です。[silence:0.6s]

# sum — 行の頭で札を 1 枚ずつ (チャイム)・最後は常設の枠を 0.8 秒で消し 1.3 秒で黒へ
*** sum
@n: [silence:0.75s][>#c1 +200][♪chime -8dB +450]まとめです。アンケートは84%が答え、課金率は下げていません。[silence:0.3s]
@: [>#c2 -300][♪chime -8dB -50]組織、月に4本以上、ビジネス用途の人には、有料の案内を早く出します。[silence:0.3s]
@: [>#c3 -300][♪chime -8dB -50]そして流入は、自己申告と計測がずれ、AIアシスタント経由が伸びています。[silence:2.4s]
[<#prog_track cut-600][<#prog cut-600][<#crumb cut-600][<#sum_idx cut-600]
fade out,1300
```

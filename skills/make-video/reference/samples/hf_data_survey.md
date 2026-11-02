# data · survey-week1 (hf 全力版の全量の写し — 登録時アンケート、1週間の結果・暗い地の 7 場面のデータ図解 (ファネル・前後の縦棒・waffle・横棒・1 点 = 1 人・目盛りの輪)) — canvas 1920x1080

見せる作り: 全編 1 枚の暗い点の格子の地 + 場面ごとに動く琥珀の光・2 場面目からの常設の枠 (上端の進行線・左上の題・右上の章の番号)・場面の骨組みの def (番号 + 見出し + 副題 + 題つきの板)・語で伸びる図 (割れるファネルの帯と引き出し線・数え上げ・目盛りの輪の弧・前 → 後の縦棒と「有意差なし」・100 マスの waffle の塗り替え・薄く先出しした札を点灯して伸ばす横棒・1 点 = 1 人の点と光る 1 点・差の破線の枠)・旧場面が上へ抜けて琥珀の光の帯が払う切替・締めの 3 枚の札と黒への fade・音の層 (BGM + 語に結んだ効果音 50 + 切替の風切り)

```design.txt
#v2
# 学ぶ作り: 全編の地は根に 1 回 (暗い点の格子の絵 + 場面ごとに動く琥珀の光 + 周辺減光)・2 場面目から常設の枠 (上端の進行線・左上の題・右上の章の番号) を sticky で
# 場面は同じ骨組み (左上の番号 + 見出し + 副題 → 題つきの板) を def で揃え、板の中の図 (横棒の行・縦棒・100 マスの waffle・1 点 = 1 人の点・目盛りの輪) は台詞の数字の語で伸ばす
# 板の中は「構造を先に薄く出し、読む語で点灯する」(札の opacity を to で 1 に)・切替は旧場面が上へ抜けた後に琥珀の光の帯が左から払う wipe・締めは 3 枚の札を行ごとに
# hf survey survey-week1 (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#0A0F1C
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
run pn { font-size: 20px; color: $fg3; font-family: r }
run pc { font-size: 0.54em }
run pcs { font-size: 0.4em; color: $steel }
run pca { font-size: 0.4em; color: $amber }
run vs { font-size: 30px; color: $fg3 }
run sec { font-size: 0.38em; color: $fg2 }
run v19 { font-size: 28px; color: $fg; font-family: b }
run v21 { font-size: 32px; color: $fg; font-family: b }
run n27 { font-size: 40px; color: $fg; font-family: b }
run n27a { font-size: 40px; color: $amber; font-family: b }
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
cue lit(r) = [!#r.l to,{opacity: 1, duration: .3} -100ms][>#r.b][>#r.v]
# 場面の要素は一斉に上へ抜ける (hf の leave: y -18・scale .985・opacity 0・0.32 s)
motion leave { out: {y:-18, scale:0.985, opacity:0, duration:0.32, ease:'power2.in'} }
p { color: $fg; out: leave }
div { border: none; out: leave }
shape { out: leave }
svg { out: leave }
# 字幕: 下端中央の暗い札・句点で割り、句末の。は外す (声の 60 ms 前に出て 150 ms 後に消える)
subtitle.hug(bottom: 40px; font-size: 33px; line-height: 1.4; letter-spacing: .02em; color: $fg; background: #050912BD; border-radius: 12px; padding: 10px 30px 12px 30px; unit: sentence; strip: 。; lead: 60ms; tail: 150ms; hold: off; in: fade {duration: 0.14}; out: fade {duration: 0.12})
bgm#music(fade: 1200,3200) 落ち着いたミニマルな電子音の下地、柔らかく脈打つアナログシンセのアルペジオと温かいパッド、軽いキックと控えめなハイハットと低いベース、100 BPM の一定のテンポで盛り上がりのない、データ報告の解説向けの曲

# 全編の地 (根・z back): 点の格子の絵 (1.4 秒で明け、全編でゆっくり引く)・周辺減光
img#bg_plate(inset: 0; z-index: back; main: kb {scale: [1.17, 1.06], focus: ['50% 50%', '48% 50%']}; in: {opacity:0, duration:1.4, ease:'power2.out'}; out: none) [photo]データ分析の解説動画のための抽象的な背景。深い夜の紺から炭色へのグラデーション、遠くの地平へ遠近で消えていく小さな点の格子がかすかに並ぶ床、右下にとても柔らかい琥珀色の光、細かいフィルムの粒子、左の 3 分の 2 は静かな広い余白。文字・数字・ロゴ・人物・グラフは入れない
div#bg_vig(inset: 0; background: radial(#03060C00@55%,#03060CB3,45%,45%); z-index: back; in: none; out: none)

# 目盛りの輪 (12 本の目盛り + 地の輪) と AI の輪の地
svg dial = """<svg viewBox="0 0 200 200"><g stroke="#B9C3D58C" stroke-linecap="butt"><line x1="100" y1="10" x2="100" y2="19" stroke-width="3"/><line x1="145" y1="22.1" x2="142.5" y2="26.4" stroke-width="2"/><line x1="177.9" y1="55" x2="173.6" y2="57.5" stroke-width="2"/><line x1="190" y1="100" x2="181" y2="100" stroke-width="3"/><line x1="177.9" y1="145" x2="173.6" y2="142.5" stroke-width="2"/><line x1="145" y1="177.9" x2="142.5" y2="173.6" stroke-width="2"/><line x1="100" y1="190" x2="100" y2="181" stroke-width="3"/><line x1="55" y1="177.9" x2="57.5" y2="173.6" stroke-width="2"/><line x1="22.1" y1="145" x2="26.4" y2="142.5" stroke-width="2"/><line x1="10" y1="100" x2="19" y2="100" stroke-width="3"/><line x1="22.1" y1="55" x2="26.4" y2="57.5" stroke-width="2"/><line x1="55" y1="22.1" x2="57.5" y2="26.4" stroke-width="2"/></g><circle cx="100" cy="100" r="72" fill="none" stroke="#7D8CA838" stroke-width="14"/></svg>"""
svg ring = """<svg viewBox="0 0 160 160"><circle cx="80" cy="80" r="62" fill="none" stroke="#7D8CA838" stroke-width="16"/></svg>"""

# 場面の骨組み: 右上の章の番号 (場面ごとに入れ替え)・左上の番号 (琥珀 + 下線)・見出し・副題・題つきの板
def idx(t) = p(right: 80px; top: 32px; font-size: 20px; color: $fg2; letter-spacing: .06em; delay: 250ms; in: {y:12, opacity:0, duration:.45, ease:'power3.out'}; out: {y:-12, opacity:0, duration:.3, ease:'power2.in'}; content: {t})
def snum(t, w=26) = div(left: 80px; top: 132px; width: {w}; height: 48px; delay: 150ms; in: {x:-20, opacity:0, duration:.55, ease:'power3.out'})
  p#t(left: 0px; top: 0px; font-size: 30px; font-family: b; color: $amber; letter-spacing: .08em; line-height: 1.3; white-space: nowrap; content: {t})
  div#u(left: 0px; top: 45px; width: {w}; height: 3px; background: $amber)
def h2(t, x=97) = p(left: {x}; top: 88px; font-size: 54px; font-family: b; line-height: 1.18; letter-spacing: .01em; delay: 220ms; in: {y:28, opacity:0, duration:.7, ease:'expo.out'}; content: {t})
def hsub(t, x=97) = p(left: {x}; top: 158px; font-size: 26px; color: $fg2; delay: 340ms; in: {y:14, opacity:0, duration:.55, ease:'power3.out'}; content: {t})
def panel = div(background: $panel; border: 2px solid $line; border-radius: 18px; box-shadow: 0px 24px 60px #00000059; in: {y:36, opacity:0, duration:.6, ease:'power3.out'})
def ptitle(t) = p(left: 32px; top: 22px; font-size: 26px; font-family: b; content: {t})
def legend(t) = p(font-size: 20px; color: $fg2; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}; content: {t})
def note(t) = p(font-size: 21px; color: $fg3; content: {t})
# 横棒の行: 札 (右揃え) + 縦の軸線 + 棒 (左から伸びる・CSS の scaleX 0 → 1) + 棒の右端に値。lw = 札の幅・x = 棒の始まり・w = 棒の長さ (値 ÷ 軸の最大 × 棒に使える幅を著者が計算)
def hbar(l, bw, v, lw=167, x=180, bh=25, ah=33, c=$slate2, vc=$fg, lc=$fg2, lo=1, ls=16, vs=19) = div(height: 58px)
  p#l(left: 0px; cy: 50%; width: {lw}; font-size: {ls}; color: {lc}; opacity: {lo}; text-align: right; white-space: nowrap; content: {l})
  div#ax(left: {x}; cy: 50%; width: 2px; height: {ah}; background: #A0B6DE59)
  div#b(left: {x}; cy: 50%; width: {bw}; height: {bh}; border-radius: 0,4,4,0; background: {c}; in: {scaleX:0, duration:.75, ease:'power3.out', pivot:'left'})
  p#v(left: .b.right+14; cy: 50%; font-size: {vs}; font-family: b; color: {vc}; line-height: 1; white-space: nowrap; delay: 450ms; in: {x:-12, opacity:0, duration:.3, ease:'power2.out'}; content: {v})
# 縦棒 (下から伸びる) と上の値・下の札
def vbar(c=$slate2) = div(width: 82px; border-radius: 5,5,0,0; background: {c}; in: {scaleY:0, duration:.75, ease:'power3.out', pivot:'bottom'})
def vval(t, c=$fg) = p(font-size: 30px; font-family: b; color: {c}; white-space: nowrap; in: {y:8, opacity:0, duration:.3, ease:'power2.out'}; content: {t})
def glab(t) = p(font-size: 22px; color: $fg2; white-space: nowrap; in: {y:8, opacity:0, duration:.35, ease:'power3.out'}; content: {t})
# 1 点 = 1 人の点 (grid に並べて左上から 8 ms ずつ弾んで出る)
def dot = div(border-radius: 148px; background: $slate2; in: {scale:0, opacity:0, duration:.25, ease:'back.out(1.7)', stagger: {each: .008}})

# title — 開幕: 地の絵が明け、左の余白に琥珀の点つきの前置き → mask から上がる 2 行の題 → 短い琥珀の罫 →「アンケート」で概要 →「結果」で 5 つの目次の札
section#title(stagger: {each:0})
# 琥珀の光の円: 場面ごとに 1 枚・前の場面の位置から 2.4 秒で次の位置へ動いて入る (2 場面目からは地を沈める幕の上なので濃さを 0.45 倍に)
div#glow_t.bleed(left: 1250px; top: 560px; width: 900px; height: 900px; border-radius: 450px; background: radial(#F5B54438,#F5B5440F@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: none; out: none)
div#t_dot(left: 150px; top: 237px; width: 10px; height: 10px; border-radius: 6px; background: $amber; box-shadow: 0px 0px 18px $amber; delay: 250ms; in: {x:-30, opacity:0, duration:.6, ease:'power3.out'})
p#t_kicker(left: 177px; top: 226px; font-size: 24px; font-family: b; color: $amber; letter-spacing: .16em; delay: 250ms; in: {x:-30, opacity:0, duration:.6, ease:'power3.out'}) 社内共有レポート｜オンボーディング
p#t_l1(left: 150px; top: 296px; font-size: 116px; font-family: b; line-height: 1.14; letter-spacing: .01em; delay: 450ms; in: {y:146, duration:.9, ease:'expo.out', clip:true}) 登録時アンケート、
p#t_l2(left: 150px; top: 436px; font-size: 116px; font-family: b; line-height: 1.14; letter-spacing: .01em; delay: 590ms; in: {y:146, duration:.9, ease:'expo.out', clip:true}) {a}1週間{/}の結果
div#t_rule(left: 150px; top: 604px; width: 180px; height: 4px; background: $amber; delay: 950ms; in: {scaleX:0, duration:.7, ease:'power4.out', pivot:'left'})
p#t_sub(left: 150px; top: 640px; width: 1320px; font-size: 30px; line-height: 1.6; color: $fg2; in: {y:18, opacity:0, duration:.7, ease:'power2.out'}) 登録直後に{w}用途・作りたい本数・知った経路{/}などを聞く短いアンケートを始めて1週間。答えた人の数と、課金との関係を見た。
p#t_chip(left: "100;270;447;651;813"; top: 794px; font-size: 22px; color: $fg2; background: #0D1424B3; border: 2px solid $line; border-radius: 148px; padding: 12px 24px; white-space: nowrap; in: {y:22, scale:.94, opacity:0, duration:.45, ease:'back.out(1.7)', stagger: {each: .09}}) ×5 {ab}01{/}　回答のファネル;{ab}02{/}　課金率への影響;{ab}03{/}　課金を予告する回答;{ab}04{/}　多数派の課金;{ab}05{/}　流入経路のずれ

# funnel — 01 回答のファネル: 常設の枠が入り、板の帯が伸びて同意 696 を数え →「586人」で完了の琥珀が伸び残りが割れる →「84%」→ 割れた 2 つに引き出し線と札 → 時間の板 (目盛りの輪) → 登録方法の横棒 2 本
section#funnel(stagger: {each:0})
div#glow_f.bleed(left: -300px; top: 380px; width: 900px; height: 900px; border-radius: 450px; background: radial(#F5B54438,#F5B5440F@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:1550, y:180, duration:2.4, ease:'sine.inOut'}; out: none)
# 地を沈める幕と常設の枠 (sticky・最後の cut の末尾で枠だけ消す)
div#bg_dim.sticky(inset: 0; background: #070B158C; z-index: back; in: {opacity:0, duration:1, ease:'power2.inOut'}; out: none)
div#prog_track.sticky(left: 0px; top: 0px; width: 1920px; height: 4px; background: #A0B6DE1A; z-index: front; in: none; out: {opacity:0, duration:.8})
progress#prog.sticky(left: 0px; top: 0px; width: 1920px; height: 4px; background: $amber; until: end; z-index: front; overlap: prog_track; out: {opacity:0, duration:.8})
p#crumb.sticky(left: 80px; top: 32px; font-size: 20px; color: $fg3; letter-spacing: .06em; z-index: front; delay: 200ms; in: {y:-10, opacity:0, duration:.55, ease:'power3.out'}; out: {opacity:0, duration:.8}) 登録時アンケート{a}　｜　{/}1週間の結果
idx#funnel_idx {ab}01 / 05{/}　回答のファネル
snum#funnel_n 01
h2#funnel_h(font-weight: 700) 回答のファネル
hsub#funnel_s アンケートに同意した人は、どこまで答えたか
panel#fun(left: 80px; top: 219px; width: 1761px; height: 336px; delay: 200ms)
  ptitle#t 回答の状況{pn}　人数（同意した人に占める割合）{/}
  p#lab(left: 33px; top: 82px; font-size: 24px; color: $fg2; in: {y:10, opacity:0, duration:.4, ease:'power3.out'}) 同意
  p#n(left: 94px; top: 69px; font-size: 40px; font-family: b; line-height: 1.2; in: {y:10, opacity:0, duration:.4, ease:'power3.out'}) [count:696 start=0 ms=950ms]
  p#u(left: 168px; top: 82px; font-size: 24px; color: $fg2; in: {y:10, opacity:0, duration:.4, ease:'power3.out'}) 人
  p#drop_lab(right: 33px; top: 70px; font-size: 22px; color: $fg2; white-space: nowrap; in: {y:-12, opacity:0, duration:.4, ease:'power3.out'}) 途中離脱　{v19}27人{/}　{v19}3.9%{/}
  # 帯: 地 (slate) → 完了 84.2% (琥珀のグラデ) → 全部スキップ 11.9%・途中離脱 3.9% (左の縁は板の色)
  div#base(left: 33px; top: 132px; width: 1695px; height: 60px; border-radius: 8px; background: $slate; in: {scaleX:0, duration:.95, ease:'power3.inOut', pivot:'left'})
  div#done(left: 33px; top: 132px; width: 1426px; height: 60px; border-radius: 5,0,0,5; background: linear($am0,#F5B544,90); in: {scaleX:0, duration:.85, ease:'power3.inOut', pivot:'left'})
    p#lab(left: 28px; cy: 50%; font-size: 26px; font-family: b; color: $ink; in: {x:-10, opacity:0, duration:.35}) 完了
  div#skip(left: 1460px; top: 132px; width: 201px; height: 60px; background: $slate2; border-left: 3px solid $edge; in: {opacity:0, duration:.45, ease:'power2.out'})
  div#drop(left: 1660px; top: 132px; width: 68px; height: 60px; border-radius: 0,5,5,0; background: $drop; border-left: 3px solid $edge; in: {opacity:0, duration:.45, ease:'power2.out'})
  div#lead_drop(left: 1694px; top: 116px; width: 2px; height: 16px; background: $fg3; in: {scaleY:0, duration:.3, ease:'power2.out', pivot:'bottom'})
  div#lead_skip(left: 1560px; top: 192px; width: 2px; height: 26px; background: $fg3; in: {scaleY:0, duration:.3, ease:'power2.out', pivot:'top'})
  p#big(left: 33px; top: 202px; font-size: 96px; font-family: b; line-height: 1; letter-spacing: -.01em; color: $amber; in: {y:24, opacity:0, duration:.5, ease:'back.out(1.7)'}) [count:84 start=0 ms=800ms]{pc}%{/}
  p#cap(left: 220px; top: 258px; font-size: 26px; color: $fg2; white-space: nowrap; in: {x:-14, opacity:0, duration:.45, ease:'power3.out'}) 最後まで完了　{v21}586人{/}
  p#skip_lab(right: 99px; top: 232px; font-size: 22px; color: $fg2; white-space: nowrap; in: {y:12, opacity:0, duration:.4, ease:'power3.out'}) 全部スキップ　{v19}83人{/}　{v19}12%{/}
#fun.skip.lit(background: $lit)
# 回答時間の板: 60 秒の目盛りの輪に 21 秒の弧を描き、数字を数える
panel#time(left: 80px; top: 580px; width: 561px; height: 368px)
  ptitle#t 回答にかかった時間{pn}　中央値{/}
  svg#dial(left: 33px; top: 102px; width: 190px; height: 190px; part: dial)
  shape#arc(path: "M 86 86.3 C 111.2 86.3 131.7 106.8 131.7 132 C 131.7 141.7 128.6 151.1 123 158.9"; background: none; border: 14px solid $amber; in: draw {duration: 0.9, ease: 'power2.out'})
  p#num(left: 254px; top: 138px; font-size: 104px; font-family: b; line-height: 1; in: {y:30, opacity:0, duration:.55, ease:'power3.out'}) [count:21 start=0 ms=900ms]{sec}秒{/}
  p#sub(left: 254px; top: 246px; font-size: 21px; color: $fg3) 目盛りは 1 分
# 登録方法別の全部スキップ (横軸 0〜40%)
panel#meth(left: 664px; top: 580px; width: 1176px; height: 368px)
  ptitle#t 登録方法別「全部スキップ」の割合{pn}　各登録方法の人のうち{/}
  hbar#mail(left: 32px; top: 118px; width: 1113px; l: "メール＋パスワード"; bw: 407; v: "29%"; c: "linear($am1,#F5B544,90)"; vc: $amber)
  hbar#google(left: 32px; top: 189px; width: 1113px; l: "Google 等のログイン"; bw: 112; v: "8%")
  note#note(left: 32px; top: 308px; in: {y:10, opacity:0, duration:.4, ease:'power3.out'}) スキップは、メールとパスワードで登録した人に多い

# paid — 02 課金率は動いていない: 縦棒の組 2 つ (前 → 後) と「有意差なし」の札 → 100 マスの waffle が 77 → 65 に減る (減った分は枠だけ) → 作った人の縦棒 2 本が同じ高さ → 結論の帯
section#paid(stagger: {each:0})
div#glow_p.bleed(left: 1299px; top: -250px; width: 900px; height: 900px; border-radius: 450px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:-1599, y:630, duration:2.4, ease:'sine.inOut'}; out: none)
idx#paid_idx {ab}02 / 05{/}　課金率への影響
snum#paid_n 02
h2#paid_h(font-weight: 700) 課金率は動いていない
hsub#paid_s アンケート開始前 → 開始後の比較
panel#rate(left: 80px; top: 219px; width: 632px; height: 636px; delay: 300ms)
  ptitle#t 登録からの課金率
  div#axis(left: 45px; top: 550px; width: 542px; height: 2px; background: #A0B6DE59)
legend#rate_lg(left: 114px; top: 288px; delay: 600ms) {sl}■{/} 開始前　{a}■{/} 開始後
# 縦棒の高さ = 値 × 33.3 px (hf の 50 px / 1 % の 2/3)
vbar#r24a(left: 171px; top: 556px; height: 214px)
vbar#r24b(left: 267px; top: 616px; height: 154px; c: "linear($am0,#F5B544,0)")
vbar#r3a(left: 442px; top: 526px; height: 244px)
vbar#r3b(left: 538px; top: 586px; height: 184px; c: "linear($am0,#F5B544,0)")
vval#r24a_v(cx: 212px; top: 507px) 4.3%
vval#r24b_v(cx: 308px; top: 567px; c: $amber) 3.1%
vval#r3a_v(cx: 483px; top: 477px) 4.9%
vval#r3b_v(cx: 579px; top: 537px; c: $amber) 3.7%
glab#g24_lab(cx: 260px; top: 783px) 24時間以内
glab#g3_lab(cx: 531px; top: 783px) 3日以内
p#ns24(cx: 260px; top: 414px; font-size: 21px; font-family: b; background: #0D1424E6; border: 2px solid $fg3; border-radius: 148px; padding: 6px 16px; white-space: nowrap; in: {scale:.6, opacity:0, duration:.45, ease:'back.out(1.7)'}) 有意差なし
p#ns3(cx: 531px; top: 414px; font-size: 21px; font-family: b; background: #0D1424E6; border: 2px solid $fg3; border-radius: 148px; padding: 6px 16px; white-space: nowrap; in: {scale:.6, opacity:0, duration:.45, ease:'back.out(1.7)'}) 有意差なし
# 24 時間以内に動画を作った人: 100 マス (1 マス = 1%)・65 マス (A) と減った 12 マス (B) と残り 23 マス (C) に分けて塗り替える
panel#made(left: 735px; top: 219px; width: 564px; height: 636px)
  ptitle#t 24時間以内に動画を1本作った人
p#wf_a(left: 768px; top: 308px; font-size: 64px; font-family: b; line-height: 1; color: $slate2; in: {y:14, opacity:0, duration:.4, ease:'power3.out'}) 77%
p#wf_arrow(left: 922px; top: 324px; font-size: 40px; line-height: 1; color: $fg3; in: {x:-12, opacity:0, duration:.35, ease:'power3.out'}) →
p#wf_b(left: 982px; top: 308px; font-size: 64px; font-family: b; line-height: 1; color: $amber; in: {y:14, opacity:0, duration:.4, ease:'back.out(1.7)'}) 65%
div#wfa(left: "576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8"; top: "264;264;264;264;264;264;264;264;264;264;284.7;284.7;284.7;284.7;284.7;284.7;284.7;284.7;284.7;284.7;305.4;305.4;305.4;305.4;305.4;305.4;305.4;305.4;305.4;305.4;326.1;326.1;326.1;326.1;326.1;326.1;326.1;326.1;326.1;326.1;346.8;346.8;346.8;346.8;346.8;346.8;346.8;346.8;346.8;346.8;367.5;367.5;367.5;367.5;367.5;367.5;367.5;367.5;367.5;367.5;388.2;388.2;388.2;388.2;388.2"; width: 26px; height: 26px; border-radius: 4px; background: $empty; in: {scale:.4, opacity:0, duration:.3, ease:'power2.out', stagger: {each: .004}}) ×65
div#wfb(left: "679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2"; top: "388.2;388.2;388.2;388.2;388.2;408.9;408.9;408.9;408.9;408.9;408.9;408.9"; width: 26px; height: 26px; border-radius: 4px; background: $empty; in: {scale:.4, opacity:0, duration:.3, ease:'power2.out', stagger: {each: .004}}) ×12
#wfa.was(background: $slate2)
#wfa.made(background: $amber)
#wfb.was(background: $slate2)
#wfb.gone(background: #7D8CA81A; border: 2px solid #B9C3D599)
div#wfc(left: "720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3;576;596.7;617.4;638.1;658.8;679.5;700.2;720.9;741.6;762.3"; top: "408.9;408.9;408.9;429.6;429.6;429.6;429.6;429.6;429.6;429.6;429.6;429.6;429.6;450.3;450.3;450.3;450.3;450.3;450.3;450.3;450.3;450.3;450.3"; width: 26px; height: 26px; border-radius: 4px; background: $empty; in: {scale:.4, opacity:0, duration:.3, ease:'power2.out', stagger: {each: .004}}) ×23
legend#wf_leg(cx: 1016px; top: 717px) {a}■{/} 作った人（開始後）　□ 減った分
note#made_note(left: 768px; top: 798px; in: {y:10, opacity:0, duration:.4, ease:'power3.out'}) 作らない人が増え、全体の課金率が薄まった（希釈）
# 動画を作った人の 24 時間課金率 (ほぼ同じ高さの 2 本)
panel#cre(left: 1323px; top: 219px; width: 518px; height: 636px)
  ptitle#t 動画を作った人の24時間課金率
  div#axis(left: 42px; top: 550px; width: 432px; height: 2px; background: #A0B6DE59)
legend#cre_lg(left: 1356px; top: 288px) {sl}■{/} 開始前　{a}■{/} 開始後
p#same(cx: 1581px; top: 327px; font-size: 30px; font-family: b; color: $amber_hi; white-space: nowrap; in: {scale:.7, opacity:0, duration:.45, ease:'back.out(1.7)'}) ≈ ほぼ同じ
vbar#c475(left: 1476px; top: 534px; height: 237px)
vbar#c457(left: 1605px; top: 543px; height: 228px; c: "linear($am0,#F5B544,0)")
vval#c475_v(cx: 1516px; top: 484px) 4.75%
vval#c457_v(cx: 1646px; top: 494px; c: $amber) 4.57%
glab#cre_lab(cx: 1581px; top: 783px) 動画を作った人
p#insight(left: 80px; top: 880px; font-size: 27px; background: #F5B54429; border: 2px solid #F5B54473; border-radius: 14px; padding: 14px 28px; white-space: nowrap; in: {x:-30, opacity:0, duration:.6, ease:'expo.out'}) {ab}→{/}　下がって見えるのは希釈。アンケートは課金率を下げていない

# pred — 03 課金を予告する回答: 1 枚の板に 4 段の組 (題・札は 0.38 で薄く先出し) → 読む語で札を点灯して棒を伸ばす → 最後の段 (太い棒 + 光) を「21.7%」で弾ませる
section#pred(stagger: {each:0})
div#glow_r.bleed(left: 1350px; top: 420px; width: 900px; height: 900px; border-radius: 450px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:-51, y:-670, duration:2.4, ease:'sine.inOut'}; out: none)
idx#pred_idx {ab}03 / 05{/}　課金を予告する回答
snum#pred_n 03
h2#pred_h(font-weight: 700) 課金を予告する回答
hsub#pred_s 回答別に見た、登録から3日以内の課金率
panel#pr(left: 80px; top: 219px; width: 1761px; height: 729px; delay: 300ms)
  ptitle#t 3日以内の課金率{pn}　回答別{/}
legend#pr_lg(right: 112px; top: 249px; delay: 600ms) {a}■{/} 課金を予告する回答　{sl}■{/} 比べる回答
# 段の組 (上の罫 + 題 + 行 2 本)・横軸 0〜25% = 棒に使える幅 782 px
div#g_org(left: 114px; top: 302px; width: 1694px; height: 129px; delay: 450ms; in: {y:16, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1694px; height: 2px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 22px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 利用形態
  hbar#sig(left: 200px; top: 12px; width: 1494px; height: 50px; l: "組織で使う"; bw: 416; v: "13.3%"; lw: 200; x: 213; bh: 23; ah: 31; c: "linear($am1,#F5B544,90)"; vc: $amber; lo: .38)
  hbar#cmp(left: 200px; top: 68px; width: 1494px; height: 50px; l: "個人"; bw: 119; v: "3.8%"; lw: 200; x: 213; bh: 23; ah: 31; lo: .38)
div#g_num(left: 114px; top: 460px; width: 1694px; height: 129px; delay: 530ms; in: {y:16, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1694px; height: 2px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 22px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 作りたい本数
  hbar#sig(left: 200px; top: 12px; width: 1494px; height: 50px; l: "月4本以上"; bw: 253; v: "8.1%"; lw: 200; x: 213; bh: 23; ah: 31; c: "linear($am1,#F5B544,90)"; vc: $amber; lo: .38)
  hbar#cmp(left: 200px; top: 68px; width: 1494px; height: 50px; l: "未定"; bw: 2; v: "0%"; lw: 200; x: 213; bh: 23; ah: 31; lo: .38)
div#g_use(left: 114px; top: 618px; width: 1694px; height: 129px; delay: 610ms; in: {y:16, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1694px; height: 2px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 22px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 用途
  hbar#sig(left: 200px; top: 12px; width: 1494px; height: 50px; l: "ビジネス用途を含む"; bw: 400; v: "12.8%"; lw: 200; x: 213; bh: 23; ah: 31; c: "linear($am1,#F5B544,90)"; vc: $amber; lo: .38)
  hbar#cmp(left: 200px; top: 68px; width: 1494px; height: 50px; l: "エンタメ系のみ"; bw: 113; v: "3.6%"; lw: 200; x: 213; bh: 23; ah: 31; lo: .38)
# 主役の段: 札は太字の白・棒は太く琥珀の光・値は大きな淡い琥珀 (「21.7%」の語で弾む)
div#g_prod(left: 114px; top: 776px; width: 1694px; height: 87px; delay: 690ms; in: {y:16, opacity:0, duration:.45, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 1694px; height: 2px; background: $line)
  p#cat(left: 0px; cy: 50%; font-size: 22px; font-family: b; color: $fg3; letter-spacing: .04em; opacity: .38) 単独で選んだ
  hbar#sig(left: 200px; top: 12px; width: 1494px; height: 66px; l: "商品・サービス紹介"; bw: 679; v: "21.7%"; lw: 200; x: 213; bh: 33; ah: 41; c: "linear($am1,#F5B544,90)"; vc: $amber_hi; lc: $fg; lo: .38; ls: 17; vs: 33)
    p#l(font-family: b)
    div#b(box-shadow: 0px 0px 34px #F5B54473; in: {scaleX:0, duration:1.1, ease:'power3.inOut', pivot:'left'})
    p#v(delay: 0ms; in: {scale:.6, opacity:0, duration:.5, ease:'back.out(1.7)', pivot:'left'})
note#pr_note(left: 114px; top: 892px; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) ビジネス用途＝商品紹介・会社紹介・研修　／　横軸は 0〜25%

# major — 04 多数派は課金しない: 左の板に用途の上位 4 本の棒 → 右の板に 1 点 = 1 人の点を 3 組 (語ごとに 8 ms ずつ弾んで出る) → アニメの 1 点だけ琥珀に光る →「ゼロ」で課金 0 人の札
section#major(stagger: {each:0})
div#glow_m.bleed(left: -250px; top: 500px; width: 900px; height: 900px; border-radius: 450px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:1600, y:-80, duration:2.4, ease:'sine.inOut'}; out: none)
idx#major_idx {ab}04 / 05{/}　多数派の課金
snum#major_n 04
h2#major_h(font-weight: 700) 多数派は課金しない
hsub#major_s よく選ばれる用途と、その課金人数
panel#top(left: 80px; top: 219px; width: 712px; height: 729px; delay: 300ms)
  ptitle#t 用途の上位{pn}　回答者に占める割合{/}
  hbar#u(left: 34px; top: "115;186;256;327"; width: 644px; height: 92px; l: "エンタメ;アニメクリップ;ストーリー;解説"; bw: "230;181;181;181"; v: "19%;15%;15%;15%"; lw: 113; x: 127; bh: 31; ah: 39; vs: 21) ×4
  note#note(left: 34px; top: 674px; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) 横軸は 0〜25%
panel#dots(left: 816px; top: 219px; width: 1024px; height: 729px; delay: 420ms)
  ptitle#t 選んだ人と、課金した人{pn}　1点＝1人{/}
legend#dots_lg(right: 112px; top: 249px; delay: 700ms) {sl}■{/} 課金なし　{a}■{/} 課金あり
p#ent_h(left: 849px; top: 388px; font-size: 22px; color: $fg2; in: {y:12, opacity:0, duration:.4, ease:'power3.out'}) エンタメだけ
p#ent_n(left: 849px; top: 422px; font-size: 34px; font-family: b; in: {y:12, opacity:0, duration:.4, ease:'power3.out'}) 63人
dot#ent_d(left: "566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4;566;584.7;603.3;622;640.7;659.4;678;696.7;715.4"; top: "319;319;319;319;319;319;319;319;319;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;375;375;375;375;375;375;375;375;375;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;431;431;431;431;431;431;431;431;431"; width: 20px; height: 20px) ×63
p#ani_h(left: 1184px; top: 388px; font-size: 22px; color: $fg2; in: {y:12, opacity:0, duration:.4, ease:'power3.out'}) アニメ
p#ani_n(left: 1184px; top: 422px; font-size: 34px; font-family: b; in: {y:12, opacity:0, duration:.4, ease:'power3.out'}) 50人
dot#ani_d(left: "789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957;789;807.7;826.3;845;863.7;882.4;901;919.7;938.4;957"; top: "319;319;319;319;319;319;319;319;319;319;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;375;375;375;375;375;375;375;375;375;375;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7"; width: 20px; height: 20px) ×50
p#und_h(left: 1518px; top: 388px; font-size: 22px; color: $fg2; in: {y:12, opacity:0, duration:.4, ease:'power3.out'}) 作りたい本数「未定」
p#und_n(left: 1518px; top: 422px; font-size: 34px; font-family: b; in: {y:12, opacity:0, duration:.4, ease:'power3.out'}) 81人
dot#und_d(left: "1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4;1012;1030.7;1049.3;1068;1086.7;1105.3;1124;1142.7;1161.4"; top: "319;319;319;319;319;319;319;319;319;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;337.7;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;356.3;375;375;375;375;375;375;375;375;375;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;393.7;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;412.4;431;431;431;431;431;431;431;431;431;449.7;449.7;449.7;449.7;449.7;449.7;449.7;449.7;449.7;468.4;468.4;468.4;468.4;468.4;468.4;468.4;468.4;468.4"; width: 20px; height: 20px) ×81
# 課金の札 (上の罫 + 課金 N 人)
div#ent_f(left: 849px; top: 736px; width: 291px; height: 75px; in: {y:10, opacity:0, duration:.45, ease:'back.out(1.7)'})
  div#ln(left: 0px; top: 0px; width: 291px; height: 2px; background: $line)
  p#t(left: 0px; top: 18px; font-size: 24px; color: $fg2) 課金 {n27}0人{/}
div#ani_f(left: 1184px; top: 736px; width: 291px; height: 75px; in: {y:10, opacity:0, duration:.4, ease:'power3.out'})
  div#ln(left: 0px; top: 0px; width: 291px; height: 2px; background: $line)
  p#t(left: 0px; top: 18px; font-size: 24px; color: $fg2) 課金 {n27a}1人{/}
div#und_f(left: 1518px; top: 736px; width: 291px; height: 75px; in: {y:10, opacity:0, duration:.45, ease:'back.out(1.7)'})
  div#ln(left: 0px; top: 0px; width: 291px; height: 2px; background: $line)
  p#t(left: 0px; top: 18px; font-size: 24px; color: $fg2) 課金 {n27}0人{/}

# route — 05 流入経路のずれ: 計測 67% と自己申告 23% の棒 → 差を破線の枠と斜線で「← ずれ」→ 自己申告の上位 5 本 → 右の板で AI アシスタントの数字 3 つ (札は薄く先出し・輪の弧・数え上げ)
section#route(stagger: {each:0})
div#glow_o.bleed(left: 1200px; top: 450px; width: 900px; height: 900px; border-radius: 450px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:-1450, y:50, duration:2.4, ease:'sine.inOut'}; out: none)
idx#route_idx {ab}05 / 05{/}　流入経路のずれ
snum#route_n 05
h2#route_h(font-weight: 700) 流入経路は、自己申告と計測がずれる
hsub#route_s 「どこで知ったか」の自己申告と、GA の計測
panel#gap(left: 80px; top: 219px; width: 1008px; height: 216px; delay: 300ms)
  ptitle#t 「検索」経由の割合{pn}　計測と自己申告{/}
  hbar#ga(left: 34px; top: 74px; width: 940px; height: 54px; l: "計測（GA）自然検索"; bw: 300; v: "67%"; lw: 167; x: 180; bh: 24; ah: 32; c: "linear($st0,#6FA8DC,90)"; vc: $steel)
    p#l(in: {x:-10, opacity:0, duration:.35, ease:'power3.out'})
    div#b(in: {scaleX:0, duration:.9, ease:'power3.out', pivot:'left'})
    p#v(delay: 540ms)
  # 差の枠: 斜線の地 + 破線の縁 (左から伸びる)・右に「← ずれ」
  div#zone(left: 459px; top: 142px; width: 296px; height: 44px; border-radius: 6px; background: #F5B5440A; pattern: hatch,45,#F5B5441F,11,5; overlap: gap.self; in: {scaleX:0, opacity:0, duration:.6, ease:'power2.out', pivot:'left'})
  shape#dash(left: 459px; top: 142px; width: 296px; height: 44px; path: rect,r=0.14; background: none; border: 2px solid #F5B544BF; dash: 5,4; overlap: gap.zone; in: {scaleX:0, opacity:0, duration:.6, ease:'power2.out', pivot:'left'})
  hbar#self(left: 34px; top: 136px; width: 940px; height: 54px; l: "自己申告「検索」"; bw: 103; v: "23%"; lw: 167; x: 180; bh: 24; ah: 32; c: "linear($am1,#F5B544,90)"; vc: $amber)
    p#l(in: {x:-10, opacity:0, duration:.35, ease:'power3.out'})
    div#b(in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(delay: 360ms)
  p#lab(left: 771px; top: 147px; font-size: 24px; font-family: b; color: $amber_hi; white-space: nowrap; in: {scale:.6, opacity:0, duration:.4, ease:'back.out(1.7)'}) ← ずれ
panel#rank(left: 80px; top: 459px; width: 1008px; height: 489px)
  ptitle#t 自己申告の流入経路{pn}　上位5つ{/}
  hbar#r(left: 34px; top: "78;118;158;198;238"; width: 960px; height: 56px; l: "検索;AIアシスタント;Web記事;X;YouTube"; bw: "443;308;250;231;212"; v: "23%;16%;13%;12%;11%"; c: "$slate2;linear($am1,#F5B544,90);$slate2;$slate2;$slate2"; vc: "$fg;$amber;$fg;$fg;$fg"; lw: 133; x: 147; bh: 23; ah: 31; vs: 17) ×5
    div#b(in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(delay: 360ms)
# AI アシスタントで知った人: 3 段 (16% / 輪の弧 84% / 7.8%)・札は 0.35 で薄く先出し・「AI」で板の縁が琥珀に
panel#ai(left: 1112px; top: 219px; width: 729px; height: 729px; in: {x:40, opacity:0, duration:.6, ease:'power3.out'})
  ptitle#t AIアシスタントで知った人
  p#big(left: 33px; top: 96px; font-size: 92px; font-family: b; line-height: 1; color: $amber; in: {y:14, opacity:0, duration:.45, ease:'back.out(1.7)'}) [count:16 start=0 ms=600ms]{pc}%{/}
  p#share(left: 204px; top: 147px; font-size: 22px; line-height: 1.45; color: $fg2; opacity: .35) 自己申告の流入経路に[br]占める割合
  div#ln1(left: 33px; top: 240px; width: 664px; height: 2px; background: $line)
  svg#ring(left: 33px; top: 258px; width: 180px; height: 180px; part: ring)
  shape#arc(path: "M 82 185.5 C 107.7 185.5 128.5 206.3 128.5 232 C 128.5 257.7 107.7 278.5 82 278.5 C 56.3 278.5 35.5 257.7 35.5 232 C 35.5 223.2 38 214.5 42.7 207.1"; background: none; border: 18px solid $amber; in: draw {duration: 1, ease: 'power2.out'})
  p#num(left: 240px; top: 296px; font-size: 72px; font-family: b; line-height: 1.15; in: {y:14, opacity:0, duration:.4, ease:'power3.out'}) [count:84 start=0 ms=1000ms]{pc}%{/}
  p#lab1(left: 240px; top: 382px; font-size: 22px; color: $fg2; opacity: .35) 24時間以内の生成到達
  div#ln2(left: 33px; top: 465px; width: 664px; height: 2px; background: $line)
  p#paid(left: 33px; top: 495px; font-size: 72px; font-family: b; line-height: 1.15; color: $amber; in: {y:14, opacity:0, duration:.4, ease:'back.out(1.7)'}) [count:7.8 start=0 ms=700ms]{pc}%{/}
  p#lab2(left: 198px; top: 514px; font-size: 22px; color: $fg2; opacity: .35) 24時間以内の課金
  note#note(left: 33px; top: 674px; in: {y:8, opacity:0, duration:.4, ease:'power3.out'}) 生成到達・課金とも高い水準
#ai.on(border: 2px solid #F5B5448C)

# sum — まとめ: 3 枚の札を行の頭で 1 枚ずつ (札が上がり、中身が 70 ms ずつ続く)・最後は常設の枠を消して黒へ
section#sum(stagger: {each:0})
div#glow_s.bleed(left: 519px; top: 300px; width: 900px; height: 900px; border-radius: 450px; background: radial(#F5B54419,#F5B54407@40%,#F5B54400@70%,#F5B54400,50%,50%); z-index: back; in: {x:681, y:150, duration:2.4, ease:'sine.inOut'}; out: none)
idx#sum_idx(out: {opacity:0, duration:.8}) {ab}まとめ{/}　1週間でわかったこと
snum#sum_n(w: 59) まとめ
h2#sum_h(x: 130; font-weight: 700) 1週間でわかったこと
hsub#sum_s(x: 130) 登録時アンケートの結果から
panel#c1(left: 80px; top: 284px; width: 572px; height: 600px; in: {y:50, opacity:0, duration:.65, ease:'expo.out'})
  div#n(left: 36px; top: 32px; width: 54px; height: 54px; border-radius: 27px; border: 2px solid $amber; delay: 200ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'})
    p#t(cx: 50%; cy: 50%; font-size: 28px; font-family: b; color: $amber) 1
  p#k(left: 36px; top: 105px; font-size: 100px; font-family: b; line-height: 1.05; color: $amber; delay: 270ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) 84{pc}%{/}
  p#ksub(left: 36px; top: 219px; font-size: 22px; color: $fg2; delay: 340ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) が最後まで回答
  p#h(left: 36px; top: 278px; width: 501px; font-size: 40px; font-family: b; line-height: 1.42; delay: 410ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) アンケートは課金率を[br]下げていない
  p#act(left: 36px; top: 498px; width: 501px; font-size: 22px; color: $fg2; background: #7D8CA81F; border: 2px solid #A0B6DE47; border-radius: 12px; padding: 15px 18px; delay: 480ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) 下がって見えたのは、作る人が減った希釈
panel#c2(left: 675px; top: 284px; width: 572px; height: 600px; in: {y:50, opacity:0, duration:.65, ease:'expo.out'})
  div#n(left: 36px; top: 32px; width: 54px; height: 54px; border-radius: 27px; border: 2px solid $amber; delay: 200ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'})
    p#t(cx: 50%; cy: 50%; font-size: 28px; font-family: b; color: $amber) 2
  p#tg(left: "23;90;201"; top: 153px; font-size: 26px; font-family: b; color: $amber_hi; background: #F5B54429; border: 2px solid #F5B54480; border-radius: 10px; padding: 8px 18px; white-space: nowrap; delay: 270ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) ×3 組織;月4本以上;ビジネス用途
  p#h(left: 36px; top: 228px; width: 501px; font-size: 40px; font-family: b; line-height: 1.42; delay: 340ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) この回答が課金を予告する
  p#act(left: 36px; top: 495px; width: 501px; font-size: 26px; background: #F5B5441F; border: 2px solid #F5B54459; border-radius: 12px; padding: 14px 18px; delay: 410ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) {ab}→{/} 有料の案内を早く出す
panel#c3(left: 1269px; top: 284px; width: 572px; height: 600px; in: {y:50, opacity:0, duration:.65, ease:'expo.out'})
  div#n(left: 36px; top: 32px; width: 54px; height: 54px; border-radius: 27px; border: 2px solid $amber; delay: 200ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'})
    p#t(cx: 50%; cy: 50%; font-size: 28px; font-family: b; color: $amber) 3
  p#k(left: 36px; top: 105px; font-size: 100px; font-family: b; line-height: 1.05; white-space: nowrap; delay: 270ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) {s}67{/}{pcs}%{/}{vs}　vs　{/}{a}23{/}{pca}%{/}
  p#ksub(left: 36px; top: 219px; font-size: 22px; color: $fg2; delay: 340ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) GA の自然検索 ／ 自己申告の検索
  p#h(left: 36px; top: 278px; width: 501px; font-size: 40px; font-family: b; line-height: 1.42; delay: 410ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) 流入経路は[br]自己申告と計測がずれる
  p#act(left: 36px; top: 495px; width: 501px; font-size: 26px; background: #F5B5441F; border: 2px solid #F5B54459; border-radius: 12px; padding: 14px 18px; delay: 480ms; in: {y:14, opacity:0, duration:.4, ease:'power2.out'}) {ab}→{/} AIアシスタント経由が伸びている
```

```timeline.txt
#v2
cast n = "明るく澄んだ若い女性のナレーター、落ち着いて明瞭に、社内向けの報告をテンポよく読む" speed=110%
silence head=0ms tail=0ms
# 切替: 旧場面が溶けて新場面が出る上を、琥珀の光の帯が左から右へ払う (hf の cross fade + sweep・帯は溶けと独立・境目で風切り)
transition = dissolve {duration: .85, dir: 'right', overlap: .85, ease: 'power2.inOut', bars: 'linear(#F5B54400,#F5B5441A@60%,#FFD27F8C@97%,#FFD27F00),173'}

# title — 題は頭に組み上がり、「アンケート」で概要・「結果」で目次の札 5 つ
*** title
[>#subtitle]
bgm music
se hit -3dB +250ms
@n: [silence:1.0s]登録時[>#t_sub +340ms]アンケート、1週間の[>#t_chip[*] +140ms][♪swipe -4dB +140ms]結果です。[silence:1.3s]

# funnel — 頭で帯の地が伸びて 696 を数え、「586人」で完了の琥珀・「84%」で大きな数字・割れた 2 つに引き出し線と札・時間の板と弧・登録方法の棒 2 本
*** funnel
@n: [silence:0.75s][>#fun.base -400ms][♪rise -7dB -400ms][>#fun.lab -300ms][>#fun.n -300ms][>#fun.u -300ms]同意した696人のうち、[>#fun.done -100ms][>#fun.done.lab +450ms][>#fun.skip +350ms][>#fun.drop +470ms][♪blip -6dB]586人、[>#fun.big count -120ms][>#fun.cap +250ms][♪tick -8dB]84%が最後まで答えました。[silence:0.3s]
@: [>#fun.lead_skip -100ms][>#fun.skip_lab][!#fun.skip .lit][=#fun.skip +300ms][♪blip -8dB]全部スキップは12%、[>#fun.lead_drop -100ms][>#fun.drop_lab][♪blip -8dB]途中離脱は3.9%。[>#time -200ms][♪swipe -6dB -200ms]回答時間の中央値は[>#time.arc -100ms][>#time.num count -100ms][♪tick -8dB]21秒です。[silence:0.3s]
@: [>#meth -100ms][♪swipe -6dB -100ms]スキップはメール登録に多く[bar #meth.mail -150ms][♪blip -7dB]29%、[bar #meth.google -100ms][>#meth.note +500ms][♪blip -8dB]Googleなどのログインでは8%です。[silence:0.3s]

# paid — 「24時間以内」「3日以内」で縦棒の組・「有意差」で札・2 文目の頭で waffle が組み上がり「77%」で灰・「65%」で減った枠と琥珀・3 文目で作った人の 2 本と「ほぼ同じ」
*** paid
@n: [silence:0.75s]課金率は、[>#r24a -50ms][>#r24b +230ms][>#r24a_v +500ms][>#r24b_v +780ms][>#g24_lab -50ms][♪rise -9dB]24時間以内が4.3%から3.1%、[>#r3a -50ms][>#r3b +230ms][>#r3a_v +500ms][>#r3b_v +780ms][>#g3_lab -50ms][♪rise -9dB]3日以内が4.9%から3.7%。どちらも[>#ns24][>#ns3 +120ms][♪chime -8dB]有意差はありません。[silence:0.3s]
@: [>#made -150ms][>#wfa[*]][>#wfb[*] +260ms][>#wfc[*] +308ms][♪swipe -6dB -150ms]下がって見えるのは、動画を作る人が[!#wfa[*] .was {stagger: {each: .006}} -200ms][!#wfb[*] .was {stagger: {each: .006}} +190ms][>#wf_a -100ms][♪blip -8dB]77%から[>#wf_arrow -200ms][!#wfb[*] .gone {stagger: {each: .03}} -100ms][!#wfa[*] .made {stagger: {each: .005}} +100ms][>#wf_b][>#wf_leg +300ms][♪tick -8dB]65%に減った[>#made_note -200ms]希釈です。[silence:0.3s]
@: [>#cre -150ms][>#cre_lg +150ms][♪swipe -6dB -150ms]作った人に限れば、[>#c475 -100ms][>#c475_v +400ms][>#cre_lab][♪blip -8dB]4.75%と[>#c457 -100ms][>#c457_v +400ms][♪blip -8dB]4.57%。[||][>#same][>#insight +500ms][♪chime -7dB]ほぼ同じです。[silence:0.6s]

# pred — 読む語で段の題と札を点灯して棒を伸ばす (比べる回答も同じ)・「商品」で太い棒・「21.7%」で値が弾む
*** pred
@n: [silence:0.75s]課金を予告する回答もあります。[!#g_org.cat to,{opacity:1, duration:.3} -100ms][lit #g_org.sig][♪rise -9dB]組織で使う人は13.3%、[lit #g_org.cmp][♪blip -9dB]個人は3.8%。[silence:0.3s]
@: [!#g_num.cat to,{opacity:1, duration:.3} -100ms][lit #g_num.sig][♪rise -9dB]月に4本以上なら8.1%、[lit #g_num.cmp][♪blip -9dB]未定は0%。[silence:0.3s]
@: [!#g_use.cat to,{opacity:1, duration:.3} -100ms][lit #g_use.sig][lit #g_use.cmp +800ms][♪rise -9dB]ビジネス用途を含むと12.8%、[!#g_prod.cat to,{opacity:1, duration:.3} -100ms][!#g_prod.sig.l to,{opacity:1, duration:.3} -100ms][>#g_prod.sig.b][♪rise -8dB]商品・サービス紹介だけなら[>#g_prod.sig.v -100ms][>#pr_note +600ms][♪chime -6dB]21.7%です。[silence:0.8s]

# major — 頭で上位 4 本の棒・語ごとに点の組 (アニメの 1 点は琥珀に光る)・「ゼロ」で課金 0 人の札 2 枚
*** major
@n: [silence:0.75s][bar #top.u[1] -300ms][bar #top.u[2] -160ms][bar #top.u[3] -20ms][bar #top.u[4] +120ms][>#top.note +600ms][♪rise -9dB -300ms]一方、多数派は課金しません。[>#ent_h -100ms][>#ent_n -100ms][>#ent_d[*]][♪blip -8dB]エンタメだけの[>#ani_h +80ms][>#ani_n +80ms][>#ani_d[*] +180ms][!#ani_d[1] fill,$amber +730ms][!#ani_d[1] to,{scale:1.25, duration:.35, ease:'back.out'} +730ms][!#ani_d[1] glow,$amber {blur: 11} +730ms][>#ani_f +780ms][♪blip -9dB +180ms]63人も、[>#und_h -100ms][>#und_n -100ms][>#und_d[*]][♪blip -8dB]本数未定の81人も、課金は[>#ent_f -150ms][>#und_f -50ms][♪hit -12dB -150ms]ゼロでした。[silence:1.2s]
# この境目だけ混ぜない切替: 旧場面は境目から一斉に上へ抜け (hf の leave は境目から 0.32 s)、新場面の上に重なる (光の帯は無し)
transition none {duration: .32} se=whoosh -4dB

# route — 1 文目の「自己申告」で下と右の板・「GA」「自己申告」で棒・文末で差の枠と「← ずれ」・2 行目は AI の数字を語ごとに点灯して数える
*** route
@n: [silence:0.75s]流入経路は、計測と[>#rank -100ms][bar #rank.r[1] +500ms][bar #rank.r[2] +620ms][bar #rank.r[3] +740ms][bar #rank.r[4] +860ms][bar #rank.r[5] +980ms][>#ai +250ms][♪swipe -7dB]自己申告が食い違います。[>#gap.ga.l -200ms][bar #gap.ga][♪rise -9dB]GAでは自然検索が67%、[>#gap.self.l -200ms][bar #gap.self][♪rise -9dB]自己申告の検索は23%[>#gap.zone][>#gap.dash][>#gap.lab +400ms][♪blip -8dB]です。[silence:0.3s]
@: [!#rank.r[2].l recolor,$amber_hi {duration: .3}][!#ai .on][♪blip -8dB]AIアシスタント経由は[>#ai.big count -150ms][!#ai.share to,{opacity:1, duration:.3} -150ms][!#rank.r[2].b glow,#FFD27F {blur: 14}][=#rank.r[2].b +350ms][♪blip -8dB]16%。[>#ai.arc -100ms][>#ai.num count -150ms][!#ai.lab1 to,{opacity:1, duration:.3} -150ms][♪tick -9dB]生成到達84%、[>#ai.paid -150ms][!#ai.lab2 to,{opacity:1, duration:.3} -150ms][>#ai.note +900ms][♪blip -8dB]課金7.8%と、質の高い層です。[silence:0.6s]

# sum — 行の頭で札を 1 枚ずつ (チャイム)・最後は常設の枠を 0.8 秒で消し 1.3 秒で黒へ
*** sum
@n: [silence:0.75s][>#c1 +200ms][♪chime -8dB +450ms]まとめです。アンケートは84%が答え、課金率は下げていません。[silence:0.3s]
@: [>#c2 -300ms][♪chime -8dB -50ms]組織、月に4本以上、ビジネス用途の人には、有料の案内を早く出します。[silence:0.3s]
@: [>#c3 -300ms][♪chime -8dB -50ms]そして流入は、自己申告と計測がずれ、AIアシスタント経由が伸びています。[silence:2.4s]
[<#prog_track cut-600ms][<#prog cut-600ms][<#crumb cut-600ms][<#sum_idx cut-600ms]
fade out,1300ms
```

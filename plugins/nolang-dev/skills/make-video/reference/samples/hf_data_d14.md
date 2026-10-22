# data · exercise-memory-review (hf 全力版の全量の写し — 運動は記憶に効くのか、研究 6 本を読み比べる・生成りの方眼の地に番号つきの明朝の見出しと板を組む 8 場面のメタ分析の図解) — canvas 1280x720

見せる作り: 全編の地 (全編で流れる生成りの方眼 + 周辺の薄い陰) と 2 文目から常設の上端の帯 (小札・題・架空データの札・全編で伸びる進行・場面ごとに入れ替わる章札)・頭は走る人の絵の左に明朝の題と「?」が回る問いと 6 つの点の予告 → 絵を紙色で覆って研究デザインの流れ図と桁ごとに回る 6 本 / 682 人・2 つの山の分布が語で寄って離れる物差し (平均の差と ▼)・語ごとに上がる 6 枚の研究の札 (絵 + 期間の棒)・52 秒の 1 場面で使い回すフォレストプロット (区間を順に描く・語で青緑 / 灰に塗り分け・◆ のまとめ・予測区間の破線と 0 より下の赤茶・右の板を語で 7 枚差し替え: 凡例の光る行・3 本 / 6 本・g = 0.34・100 個の点の 63 個・重みの横棒・I² の帯・予測区間)・群ごとの帯と ◆ と重なりの表 (黄土の帯)・散布図に傾向の破線と見えない研究の破線の丸と引き出しの絵・縁が黄土に点く限界の札 4 枚・道の絵の上の 3 行の結論 (チェック + 語で引く下帯)・紙色の締めの題・字幕は生成りの札・音の層 (場面の境の風切り + 語に結んだ効果音 68)

```design.txt
#v2
# 学ぶ作り: 生成りの方眼の地 (全編でゆっくり流れる) と 2 文目から常設の上端の帯 (題・架空データの札・全編で伸びる進行) の上に、場面ごとに「番号 + 明朝の題」の見出しと板を組む
# 主役の図はフォレストプロット 1 枚を 3 段 (各研究 → まとめた効果 → ばらつき) で使い回し、右の板だけを語で差し替える (話し終えた板は消して次の板)・数字は桁ごとに回って止まる
# 図の部品: 2 つの山の分布 (svg) と動く平均の差・6 枚の研究の札 (絵 + 期間の棒)・点と区間の行・◆ のまとめ・100 個の点・群ごとの帯・散布図と引き出しの絵・語で点ける限界の札・チェックの結論
# hf d14 exercise-memory-review (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3。場面の切替は hf と同じ 0.6 秒の溶け (旧場面の要素が消え新場面が出る・地と上端の帯は常設)
canvas 1280x720 bg=#F2EDE2
theme light
palette paper=#F2EDE2 paper2=#E8E0CF card=#FBF8F1 ink=#1E2B3C ink2=#46535F ink3=#5B6570 rule=#CFC5B2 teal=#24727A teal_l=#D3E7E4 ochre=#8F5A14 ochre_f=#B87523 ochre_l=#F2E1C3 brick=#A9472F brick_l=#F0D6CD slate=#66707C slate_l=#E2E5E9 a=#B87523 b=#24727A
font "端正で読みやすい角ゴシック体の太字"
fonts b="端正で読みやすい角ゴシック体の太字"
fonts m="工業的に設計された端正でモダンな角ゴシック体の標準の太さ、和文と欧文の釣り合いが良く読みやすい"
fonts s="繊細で上品な筆の抑揚を持つ明朝体の太字"
fonts n="太い幾何学的な欧文サンセリフ体、ウェブやUIで定番のモダンな書体"
art "落ち着いた学術解説向けの洗練されたエディトリアルなフラットイラスト。くすんだ紺・くすんだ青緑・温かい黄土・くすんだ赤茶・柔らかな生成りに絞った色、ごく薄い紙の粒子の質感、すっきりした幾何学的な形とやわらかな陰影、落ち着いた知的な雰囲気"
prompt_tail "文字・数字・ロゴ・透かしは入れない"
sfx off
# hf の作り: 場面の見出し (番号 + 題 + 補足) は台詞より先に出る
lint off=spoiler
# hf の作り: 板の中の目盛り・凡例・注記は 11〜13 px (1080 の 16〜20 px)
lint off=small_text
# hf の作り: 図の色 (半透明の地・灰の線・帯の淡い色) は場面ごとに直書き
lint off=palette_drift
# hf の作り: 地は全編の方眼の紙 (写真は頭と結論の 2 枚だけ)・場面は図と板で替える
lint off=text_only_cut,same_picture
# hf の作り: 問い・見出し・結論の行は字幕と同じ文を板にも出す
lint off=duplicate_text
# hf の作り: 凡例の注記・締めの注記は 2〜3 秒で次の板に替わる / 0.6 秒の溶けで大きな数字が透ける / 頭の 6 つの点にタップ音を 0.13 秒おき (-16dB) / 期間の札と種類の札が縦に並ぶ
lint off=flash_text,ghost_dissolve,se_dense,stacked_labels
# hf の作り: 頭の題は走る人の絵の左寄りに掛かり (左を紙色のグラデで空ける)、「運動群」からは絵を紙色で覆って図と数字を絵の上に組む
lint off=text_over_subject
# hf の作り: 副題と締めの題の「6」は明朝のまま
lint off=script_font_digits
# hf の作り: 「682」は場面の最後の文で回り始め、回り終えてすぐ次の場面へ溶ける
lint off=entrance_in_fadeout
# 効果音: hf の data-volume v を 20·log10(v) + 4 dB に写す (タップ 0.14 → -13dB・グロッケン 0.8 → +2dB)
sound tap = "乾いた木を軽く叩くような短いコッという操作音"
sound page = "紙を一枚めくるペラッという乾いた短い音"
sound whoosh = "低めで柔らかいサーという控えめな風切りの音、画面の切り替わり"
sound pencil = "シャープペンで紙にまっすぐ線を引くサッという音"
sound glock = "小さな鉄琴を一回鳴らすピーンという澄んだ単音"
sound bell = "低めの二音のシンセベル、ティロンと上品に鳴る提示の音"
sound check = "フェルトペンでチェックを付けるキュッという短い音"
run nb { color: $ink; font-family: b }
run c { color: $ink3; font-family: m }
run cn { color: $ochre; font-family: n }
run tb { color: $teal; font-family: b }
run sb { color: #56606C; font-family: b }
run tl { color: $ink2; font-size: 0.6em }
run m { marker: #C4832F61,42% }
# 2 つの山の分布 (viewBox は hf の svg と同じ 1180x520・平均 480・山の高さ 300)
svg curve_ct = """<svg viewBox="0 0 1180 520"><defs><linearGradient id="gct" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7d8794" stop-opacity="0.34"/><stop offset="1" stop-color="#7d8794" stop-opacity="0.06"/></linearGradient></defs><path d="M0 436.7 L20 435.2 L40 433.2 L60 430.4 L80 426.8 L100 422.1 L120 416.1 L140 408.6 L160 399.4 L180 388.3 L200 375.1 L220 359.9 L240 342.6 L260 323.4 L280 302.6 L300 280.7 L320 258.0 L340 235.4 L360 213.5 L380 193.2 L400 175.3 L420 160.4 L440 149.2 L460 142.3 L480 140.0 L500 142.3 L520 149.2 L540 160.4 L560 175.3 L580 193.2 L600 213.5 L620 235.4 L640 258.0 L660 280.7 L680 302.6 L700 323.4 L720 342.6 L740 359.9 L760 375.1 L780 388.3 L800 399.4 L820 408.6 L840 416.1 L860 422.1 L880 426.8 L900 430.4 L920 433.2 L940 435.2 L960 436.7 Z" fill="url(#gct)" stroke="#7d8794" stroke-width="3"/><line x1="480" y1="140" x2="480" y2="440" stroke="#7d8794" stroke-width="2" stroke-dasharray="6 6"/></svg>"""
svg curve_ex = """<svg viewBox="0 0 1180 520"><defs><linearGradient id="gex" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#24727a" stop-opacity="0.38"/><stop offset="1" stop-color="#24727a" stop-opacity="0.08"/></linearGradient></defs><path d="M0 436.7 L20 435.2 L40 433.2 L60 430.4 L80 426.8 L100 422.1 L120 416.1 L140 408.6 L160 399.4 L180 388.3 L200 375.1 L220 359.9 L240 342.6 L260 323.4 L280 302.6 L300 280.7 L320 258.0 L340 235.4 L360 213.5 L380 193.2 L400 175.3 L420 160.4 L440 149.2 L460 142.3 L480 140.0 L500 142.3 L520 149.2 L540 160.4 L560 175.3 L580 193.2 L600 213.5 L620 235.4 L640 258.0 L660 280.7 L680 302.6 L700 323.4 L720 342.6 L740 359.9 L760 375.1 L780 388.3 L800 399.4 L820 408.6 L840 416.1 L860 422.1 L880 426.8 L900 430.4 L920 433.2 L940 435.2 L960 436.7 Z" fill="url(#gex)" stroke="#24727a" stroke-width="3.5"/><line x1="480" y1="140" x2="480" y2="440" stroke="#24727a" stroke-width="2.5" stroke-dasharray="6 6"/></svg>"""
motion up { in: {y:17, opacity:0, duration:0.7, ease:'power3.out'} }
p { color: $ink }
# 字幕: 下端中央の生成りの札 (細い縁 + 薄い影)・句ごとに 1 枚 (札 = 文、[|] で句に切る)・句末の。は外す
subtitle.hug(bottom: 27px; font-size: 22px; font-family: m; line-height: 1.3; letter-spacing: 0.02em; color: $ink; background: #FBF8F1F0; border: 1px solid #1E2B3C1A; border-radius: 5px; padding: 6px 20px 7px 20px; box-shadow: 0px 4px 12px #1E2B3C14; unit: sentence; strip: 、。; lead: 0; tail: 0; hold: next; in: {y:5, opacity:0, duration:0.22, ease:'power2.out'}; out: none)
# 曲: 台詞の下はごく小さく (hf 0.07)、締めの題で前に出て 2.4 秒で消える
bgm#music(fade: 600,2400; keys: "0:0|end-3.6s:0|end-2.8s:+8") 温かいシンセのパッドときらめくチャイムに控えめなビートが乗る、浮遊感のある穏やかなアンビエント、知的な解説向け

# 場面の見出し: 黄土の欧文の番号 + 明朝の題 + 補足 (下から上がる・場面の中で差し替える時は上へ消える)
def bt(no, ttl, sub="") = div(left: 64px; top: 85px; width: 1000px; height: 64px; in: up; out: {opacity:0, duration:0.3, ease:'power2.in'})
  p#n(left: 0px; top: 3px; font-size: 39px; line-height: 1; font-family: n; color: $ochre; content: {no})
  p#t(left: .n.right+15; top: 0px; font-size: 33px; line-height: 1.15; font-family: s; white-space: nowrap; content: {ttl})
  p#s(left: .n.right+15; top: 44px; font-size: 15px; font-family: m; color: $ink2; white-space: nowrap; content: {sub})
# 上端の帯の章札 (右寄せ・番号は黄土の欧文)。場面の頭に下から入り、上へ抜ける
def chap(t) = p(right: 140px; top: 30px; font-size: 13px; white-space: nowrap; z-index: front; in: {y:7, opacity:0, duration:0.5, ease:'power2.out'}; out: {y:-7, opacity:0, duration:0.35, ease:'power2.in'}; content: {t})
# 板: 生成りの白の地 + 細い縁 + 柔らかい影 + 字間の広い題
def panel(hd) = div(background: $card; border: 1px solid #1E2B3C1A; border-radius: 9px; box-shadow: 0px 9px 23px #3C321E1A; in: up; out: {opacity:0, duration:0.35, ease:'power2.in'})
  p#h(left: 20px; top: 18px; font-size: 14px; letter-spacing: 0.06em; color: $ink2; content: {hd})
# 研究デザインの箱 (題 + 補足を中央に)
def dbox(t, s, bc="#1E2B3C2E", fl=$card, tc=$ink) = div(height: 87px; background: {fl}; border: 1px solid {bc}; border-radius: 8px; box-shadow: 0px 7px 17px #3C321E14; in: up)
  p#t(cx: 50%; cy: 38%; font-size: 20px; color: {tc}; content: {t})
  p#s(cx: 50%; cy: 68%; font-size: 13px; font-family: m; color: $ink2; content: {s})
# 研究の札: 左に絵 (生成りのグラデの地)・右に文字の丸 + 題 + 種類の札・人数・3 行の内訳・期間の棒 (語で伸びる)
def card(k, tag, n, g, who, ex, test, fw, pv, tg=$teal_l, tc=#1A5F66) = div(width: 373px; height: 212px; background: $card; border: 1px solid #1E2B3C1F; border-radius: 9px; box-shadow: 0px 8px 20px #3C321E1A; in: {y:23, scale:0.97, opacity:0, duration:0.7, ease:'power3.out'})
  div#ci(left: 0px; top: 0px; width: 143px; height: 212px; border-radius: 9px 0px 0px 9px; background: linear(#EFE7D6,#E6DCC6,180))
  img#im(left: 4px; top: 16px; width: 135px; height: 192px; object-fit: contain; main: none)
  p#lc(left: 157px; top: 13px; width: 31px; text-align: center; font-size: 17px; font-family: n; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 4px 0px; content: {k})
  p#nm(left: 196px; cy: 29px; font-size: 13px; content: 研究 {k})
  p#tag(left: .nm.right+8; cy: 29px; font-size: 11px; color: {tc}; background: {tg}; border-radius: 4px; padding: 2px 7px; content: {tag})
  p#n(left: 157px; top: 52px; font-size: 31px; line-height: 1; font-family: n; content: {n})
  p#u(left: .n.right+5; top: 62px; font-size: 15px) 人
  p#g(left: .u.right+7; top: 53px; font-size: 10px; line-height: 1.25; color: $ink3; content: {g})
  p#d1(left: 157px; top: 101px; font-size: 12px; color: $ink3) 対象
  p#d2(left: 157px; top: 121px; font-size: 12px; color: $ink3) 運動
  p#d3(left: 157px; top: 141px; font-size: 12px; color: $ink3) テスト
  p#v1(left: 195px; top: 101px; font-size: 12px; font-family: m; content: {who})
  p#v2(left: 195px; top: 121px; font-size: 12px; font-family: m; content: {ex})
  p#v3(left: 195px; top: 141px; font-size: 12px; font-family: m; content: {test})
  p#pl(left: 157px; top: 183px; font-size: 11px; color: $ink3) 期間
  div#tr(left: 199px; top: 188px; width: 104px; height: 7px; border-radius: 4px; background: $paper2)
  div#pf(left: 199px; top: 188px; width: {fw}; height: 7px; border-radius: 4px; background: $ochre_f; in: {scaleX:0, duration:0.9, ease:'power3.out', pivot:'left'})
  p#pv(left: 311px; top: 182px; width: 49px; text-align: right; font-size: 13px; font-family: n; in: {opacity:0, duration:0.4}; content: {pv})
# 限界の札 (黄土の番号の丸 + 題 + 補足)・語で点けた札だけ縁が黄土 (実体ごとの変種 .on)
def lcard(no, hd, d) = div(left: 673px; width: 543px; height: 100px; background: $card; border: 1px solid #1E2B3C1A; border-radius: 9px; box-shadow: 0px 9px 23px #3C321E1A; in: up)
  p#no(left: 17px; top: 16px; width: 32px; text-align: center; font-size: 17px; font-family: n; color: #FFFFFF; background: $ochre_f; border-radius: 99px; padding: 4px 0px; content: {no})
  p#h(left: 64px; top: 13px; width: 460px; font-size: 18px; line-height: 1.3; content: {hd})
  p#d(left: 64px; top: 43px; width: 460px; font-size: 13px; font-family: m; line-height: 1.45; color: $ink2; content: {d})
# 結論の行 (青緑の丸のチェック + 明朝の題 + 補足)・題の語に語で下帯 (marker) を引く
def concl(hd, d) = div(left: 64px; width: 867px; height: 80px; in: {x:-20, opacity:0, duration:0.7, ease:'power3.out'})
  icon#ck(left: 0px; top: 3px; font-size: 20px; padding: 8px; name: check; weight: bold; color: #FFFFFF; background: $teal; in: {scale:0, duration:0.45, ease:'back.out(2.5)'})
  p#h(left: 53px; top: 0px; font-size: 28px; line-height: 1.28; font-family: s; content: {hd})
  p#d(left: 53px; top: 40px; font-size: 15px; font-family: m; color: $ink2; content: {d})

# 全編の地 (根): 生成りに 32 px の方眼が 157 秒かけて左上へ流れる + 周辺の薄い陰
div#bg_base.bleed(left: -80px; top: -80px; width: 1440px; height: 880px; background: $paper; pattern: grid,32,#1E2B3C0D; z-index: back; in: none; main: ramp {x: -64, y: -32})
veil#vig(background: radial(#F2EDE200@55%,#78644624@100%,50%,45%); z-index: back; in: none)

# s01 問い: 走る人の絵が寄りから引き、左の空きに小札 → 明朝の 2 行の題 → 副題 → 「?」が回って弾む問い → 6 つの点の予告の板。「運動群」で全部を消して絵を紙色で覆い、研究デザインの図と 6 本 / 682 人を組む
section#s01(stagger: {each:0})
img#hero(inset: 0; subject: right 62%; room: left 36%; main: kb {scale: [1.1, 1], focus: ['72% 40%', '70% 40%'], ease:'sine.out'}) 横長の絵。画面の右 3 分の 2 に、早朝のやわらかな光の川沿いの道を走る若い女性 (紺のジャケットと青緑のレギンス)。走る人の頭上と周りに、脳の形をした神経のネットワークの半透明の線画と、白紙の単語カードが数枚浮かび、記憶と学びを表す。画面の左 3 分の 1 は何も置かない淡い生成りの空の余白
div#s1_fade(inset: 0; background: linear(#F2EDE2F5,#F2EDE2DB@34%,#F2EDE200@62%,90); in: none)
div#s1_dim(inset: 0; background: #F2EDE2E6; in: {opacity:0, duration:0.7, ease:'power2.inOut'})
group#title(out: {opacity:0, duration:0.45, ease:'power2.in'})
  p#kick(left: 80px; top: 131px; font-size: 14px; letter-spacing: 0.24em; color: $ochre; delay: 150; in: up) RESEARCH REVIEW ｜ 研究レビュー
  p#t1(left: 80px; top: 166px; font-size: 75px; line-height: 1.12; font-family: s; delay: 300; in: {y:17, opacity:0, duration:0.9, ease:'power3.out'}) 運動は
  p#t2(left: 80px; top: 250px; font-size: 75px; line-height: 1.12; font-family: s; delay: 480; in: {y:17, opacity:0, duration:0.9, ease:'power3.out'}) 記憶に効くのか
  p#sub(left: 80px; top: 347px; font-size: 29px; font-family: s; color: $ink2; delay: 800; in: up) — 研究 6 本を読み比べる
p#quote(left: 80px; top: 460px; font-size: 25px; font-family: s; in: up; out: {opacity:0, duration:0.45, ease:'power2.in'}) 「運動すると記憶力が上がる」
p#qm(left: quote.right+9; cy: quote.cy; font-size: 29px; font-family: n; color: $ochre; in: {scale:0.2, rotation:-30, opacity:0, duration:0.5, ease:'back.out(3)'}; out: {opacity:0, duration:0.45, ease:'power2.in'}) ?
# 予告の板: 6 本の効果の点が軸の上に弾む (0 の破線と「差なし 0」「効果あり →」)
div#teaser(left: 69px; top: 515px; width: 541px; height: 88px; background: #FBF8F1DB; border: 1px solid #1E2B3C1A; border-radius: 8px; in: up; out: {opacity:0, duration:0.45, ease:'power2.in'})
  p#ttl(left: 17px; top: 7px; font-size: 13px; color: $ink2) 研究ごとの結果（効果の大きさ）
  div#ax(left: 17px; top: 44px; width: 507px; height: 1.5px; background: $ink2; in: {scaleX:0, duration:0.7, ease:'power2.out', pivot:'left'})
  shape#zero(left: 101px; top: 27px; width: 2px; height: 36px; path: line_v; border: 1.5px solid $brick; dash: 4,3)
  p#l0(left: 75px; top: 62px; font-size: 13px; color: $ink2) 差なし 0
  p#l1(left: 451px; top: 62px; font-size: 13px; color: $ink2) 効果あり →
  shape#dot.ellipse(left: "282;379;168;480;67;185"; top: 35px; width: 20px; height: 20px; background: $teal; border: 3px solid #FBF8F1F2; in: {scale:0, opacity:0, duration:0.4, ease:'back.out(2.5)', stagger:{each:0.13}}) ×6
# 研究デザインの図: 参加者 → 無作為に 2 群 → 運動群 / 対照群 → 記憶テスト (矢印は語で左から描く)
div#dg(left: 64px; top: 140px; width: 753px; height: 427px)
  dbox#pop(left: 0px; top: 167px; width: 153px; t: "参加者"; s: "研究ごとに募集")
  shape#l1(left: 157px; top: 203px; width: 73px; height: 12px; path: arrow_r,head=fill; background: $ink2; border: 2px solid $ink2; in: draw {duration: 0.4})
  p#rand(left: 164px; top: 165px; font-size: 13px; line-height: 1.3; color: $ochre; in: up) 無作為に[br]2 群へ
  shape#l2a(left: 209px; top: 162px; width: 93px; height: 12px; path: arrow_r,head=fill; background: $ink2; border: 2px solid $ink2; transform: rotate(-61.5deg); in: draw {duration: 0.35})
  shape#l2b(left: 209px; top: 244px; width: 93px; height: 12px; path: arrow_r,head=fill; background: $ink2; border: 2px solid $ink2; transform: rotate(61.5deg); in: draw {duration: 0.35})
  dbox#ex(left: 280px; top: 80px; width: 193px; t: "運動群"; s: "決められた運動をする"; bc: $teal; fl: $teal_l; tc: $teal)
  dbox#ct(left: 280px; top: 253px; width: 193px; t: "対照群"; s: "運動しない"; bc: $slate; fl: $slate_l; tc: #4F5966)
  shape#l3(left: 462px; top: 157px; width: 131px; height: 12px; path: arrow_r,head=fill; background: $ink2; border: 2px solid $ink2; transform: rotate(38deg); in: draw {duration: 0.45})
  shape#l4(left: 462px; top: 250px; width: 131px; height: 12px; path: arrow_r,head=fill; background: $ink2; border: 2px solid $ink2; transform: rotate(-38deg); in: draw {duration: 0.45})
  dbox#test(left: 587px; top: 160px; width: 167px; height: 100px; t: "記憶テスト"; s: "成績の差を比べる")
  p#note(left: 0px; top: 393px; font-size: 13px; color: $brick; in: up) ※ 研究 A〜F はこの動画の解説用に設定した架空の研究です
# 大きい数字 2 段 (上の黒い罫 + 題 + 桁ごとに回って止まる数字 + 単位)
div#st6(left: 860px; top: 153px; width: 360px; height: 180px; in: up)
  div#rule(left: 0px; top: 0px; width: 360px; height: 1.5px; background: $ink)
  p#l(left: 0px; top: 17px; font-size: 15px; color: $ink2) 読み比べる研究（無作為化比較試験）
  p#v(left: 0px; top: 48px; font-size: 88px; line-height: 1; font-family: n; in: {opacity:0, duration:0.35, ease:'power2.out'}) [count:6 start=0 roll ms=1000]
  p#u(left: .v.right+9; top: 90px; font-size: 31px) 本
  div#mini(left: "0;36;72;108;144;180"; top: 148px; width: 29px; height: 29px; background: $card; border: 1.5px solid $ink2; border-radius: 5px) ×6
    p#t(cx: 50%; cy: 50%; font-size: 15px; font-family: n) A;B;C;D;E;F
div#st682(left: 860px; top: 362px; width: 360px; height: 175px; in: up)
  div#rule(left: 0px; top: 0px; width: 360px; height: 1.5px; background: $ink)
  p#l(left: 0px; top: 17px; font-size: 15px; color: $ink2) 参加者の合計
  p#v(left: 0px; top: 50px; font-size: 88px; line-height: 1; font-family: n; in: {opacity:0, duration:0.35, ease:'power2.out'}) [count:682 start=0 roll ms=1400,1520,1640]
  p#u(left: .v.right+9; top: 92px; font-size: 31px) 人
  p#f(left: 0px; top: 152px; font-size: 12px; font-family: m; color: $ink3) 各研究で運動群と対照群に半数ずつ
# 常設の上端の帯 (sticky・「運動群」の語から締めの題まで): 左に小札と題、右に架空データの札、下の細い線の上を進行が伸びる
div#hdr.sticky(left: 64px; top: 27px; width: 1152px; height: 27px; z-index: front; in: {opacity:0, duration:0.6, ease:'power2.out'}; out: {opacity:0, duration:0.5, ease:'power2.in'})
  p#k(left: 0px; cy: 50%; font-size: 10px; letter-spacing: 0.22em; color: $ochre) RESEARCH NOTE
  div#sep(left: .k.right+12; cy: 50%; width: 1px; height: 12px; background: $rule)
  p#t(left: .sep.right+12; cy: 50%; font-size: 13px; font-family: m; color: $ink2; white-space: nowrap) 運動は記憶に効くのか ― 研究 6 本を読み比べる
  p#bd(right: 0px; cy: 50%; font-size: 10px; letter-spacing: 0.04em; color: $brick; background: #FBF8F1B3; border: 1px solid $brick; border-radius: 3px; padding: 2px 7px) 架空データ
div#hdr_rule.sticky(left: 64px; top: 62px; width: 1152px; height: 1.5px; background: #1E2B3C1F; z-index: front; in: {opacity:0, duration:0.6, ease:'power2.out'}; out: {opacity:0, duration:0.5, ease:'power2.in'})
progress#prog.sticky(left: 64px; top: 62px; width: 1152px; height: 1.5px; background: $ink; until: end; z-index: front; overlap: hdr_rule; out: {opacity:0, duration:0.5, ease:'power2.in'})
chap#ch0 {cn}序{/} 問い

# s02 物差し: 軸が引かれ、灰の山 (対照群) → 青緑の山 (運動群) が上がり「平均の差」。右に g の式の板と目安の物差しの板。0 / 0.2 / 0.5 の語で青緑の山と ▼ が動き、目盛りの札が膨らむ
section#s02(stagger: {each:0})
chap#ch1 {cn}01{/} 物差し
bt#bt2(no: "01"; ttl: "効果の大きさをそろえる物差し"; sub: "標準化平均差 g ― 研究ごとに違う記憶テストを、同じ尺度で比べる")
div#base2(left: 64px; top: 493px; width: 760px; height: 1.5px; background: $ink; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'left'})
group#ct(in: {y:20, opacity:0, duration:0.8, ease:'power3.out'})
  svg#c(left: 64px; top: 200px; width: 787px; height: 347px; part: curve_ct)
  p#l(right: 1016px; top: 350px; font-size: 17px; color: #56606C; overlap: ex.c) 対照群
# 運動群の山は g = 0.5 の位置 (右へ 53 px) に置き、語で x を動かす (g × 107 px)
group#ex(in: {y:20, opacity:0, duration:0.8, ease:'power3.out'})
  svg#c(left: 117px; top: 200px; width: 787px; height: 347px; part: curve_ex)
  p#l(left: 560px; top: 350px; font-size: 17px; color: $teal) 運動群
group#gap(in: {opacity:0, duration:0.5})
  div#ln(left: 384px; top: 272px; width: 53px; height: 3px; background: $ochre_f)
  p#t(cx: 411px; top: 247px; font-size: 15px; color: $ochre) 平均の差
p#cap2(left: 64px; top: 513px; font-size: 13px; font-family: m; color: $ink3; in: none) 記憶テストの成績 →（イメージ図）
panel#defs(left: 887px; top: 200px; width: 329px; height: 180px; hd: "g の求め方")
  p#eq(left: 20px; cy: 85px; font-size: 23px; font-family: n; italic: true) g =
  p#nu(left: 65px; top: 55px; width: 222px; text-align: center; font-size: 16px; white-space: nowrap) 運動群の平均 − 対照群の平均
  div#bar(left: 65px; top: 84px; width: 222px; height: 1.5px; background: $ink)
  p#de(left: 65px; top: 91px; width: 222px; text-align: center; font-size: 16px) ばらつき（標準偏差）
  p#nt(left: 20px; top: 124px; font-size: 13px; font-family: m; color: $ink2) 単位の違うテストどうしでも比べられる
# 目安の物差し: 0 / 0.2 / 0.5 の目盛りと札・黄土の ▼ は g = 0.5 の位置 (語で x を動かす・g × 460 px)
panel#scale(left: 887px; top: 397px; width: 329px; height: 179px; hd: "大きさの目安")
  div#ruler(left: 27px; top: 80px; width: 276px; height: 1.5px; background: $ink)
  div#tk(left: "27;119;257"; top: 74px; width: 1.5px; height: 15px; background: $ink) ×3
  div#rl(left: "-1;91;229"; top: 95px; width: 56px; height: 42px) ×3
    p#v(cx: 50%; top: 0px; font-size: 16px; font-family: n) 0;0.2;0.5
    p#w(cx: 50%; top: 21px; font-size: 13px; color: $ink2) 差なし;小;中程度
  shape#mk(left: 249px; top: 56px; width: 16px; height: 12px; path: tri; background: $ochre_f; transform: rotate(180deg))

# s03 6 本の研究: 3 × 2 の札を研究の語ごとに上げ、上がった札の縁を一瞬黄土に。「期間」で右上の札と 6 本の期間の棒が順に伸びる
section#s03(stagger: {each:0})
chap#ch2 {cn}02{/} 6 本の研究
bt#bt3(no: "02"; ttl: "読み比べる 6 本の研究"; sub: "どれも運動群と、運動しない対照群を比べた無作為化比較試験（架空）")
p#period(right: 64px; top: 100px; font-size: 13px; color: #8A5512; background: $ochre_l; border-radius: 99px; padding: 3px 11px; in: up) 期間：1 回きり 〜 52 週
card#ca(left: 64px; top: 167px; k: "A"; tag: "有酸素"; n: "120"; g: "運動群 {nb}60{/}[br]対照群 {nb}60{/}"; who: "18〜25 歳の大学生"; ex: "ジョギング 週 3 回"; test: "単語リストの再生"; fw: 24px; pv: "12 週")
  img#im [transparent]20 歳前後の日本人の大学生 2 人がシンプルなスポーツウェアで並んでジョギングしている、走る途中の姿、集中して明るい表情。全身が入り周りに少し余白、背景・地面・床の影なし
card#cb(left: 453px; top: 167px; k: "B"; tag: "有酸素"; n: "64"; g: "運動群 {nb}32{/}[br]対照群 {nb}32{/}"; who: "60〜75 歳"; ex: "早歩き 週 5 回"; test: "単語リストの遅延再生"; fw: 48px; pv: "24 週")
  img#im [transparent]60 代後半の日本人の男性と女性が並んで早歩きしている、スポーティな普段着、腕を振り姿勢がよい。全身が入り周りに少し余白、背景・地面・床の影なし
card#cc(left: 843px; top: 167px; k: "C"; tag: "組み合わせ"; n: "210"; g: "運動群 {nb}105{/}[br]対照群 {nb}105{/}"; who: "65〜80 歳"; ex: "有酸素と筋トレの組み合わせ"; test: "物語の再生"; fw: 104px; pv: "52 週"; tg: $ochre_l; tc: #8A5512)
  img#im [transparent]70 代の日本人女性が有酸素運動と筋トレを組み合わせた運動をしている。低い踏み台に片足で上りながら、両手に軽いダンベルを持つ。全身が入り周りに少し余白、背景・地面・床の影なし
card#cd(left: 64px; top: 395px; k: "D"; tag: "有酸素"; n: "48"; g: "運動群 {nb}24{/}[br]対照群 {nb}24{/}"; who: "20〜30 歳"; ex: "自転車こぎ 20 分 × 1 回"; test: "直後の単語リスト再生"; fw: 3px; pv: "1 回")
  img#im [transparent]20 代の日本人の若者が室内の固定式の自転車 (エアロバイク) を力強くこいでいる、横から見た姿、スポーツウェア。全身が入り周りに少し余白、背景・地面・床の影なし
card#ce(left: 453px; top: 395px; k: "E"; tag: "ヨガ"; n: "90"; g: "運動群 {nb}45{/}[br]対照群 {nb}45{/}"; who: "30〜50 歳の会社員"; ex: "ヨガとストレッチ"; test: "数字の順唱（作業記憶）"; fw: 16px; pv: "8 週"; tg: $ochre_l; tc: #8A5512)
  img#im [transparent]40 代の日本人の会社員がシンプルなシャツとスラックスで、裸足でヨガマットの上に立ち、両腕を頭上へまっすぐ伸ばす穏やかなヨガのストレッチ。全身が入り周りに少し余白、背景・地面・床の影なし
card#cf(left: 843px; top: 395px; k: "F"; tag: "筋トレ"; n: "150"; g: "運動群 {nb}75{/}[br]対照群 {nb}75{/}"; who: "60〜80 歳"; ex: "筋トレ 週 2 回"; test: "図形の位置の記憶"; fw: 52px; pv: "26 週"; tg: $ochre_l; tc: #8A5512)
  img#im [transparent]70 代の日本人男性が低いベンチに座り、片手のダンベルでアームカールをしている、真剣な表情。全身が入り周りに少し余白、背景・地面・床の影なし

# forest フォレストプロット (3 段): 表と点 → 軸・0 の破線・区間を上から順に描く → 右の板を語で差し替え (読み方 → 判定 → まとめた効果 → 63% → 重み → 異質性 → 予測区間)
# 段の替わり目は見出しと章札だけを入れ替え、表と図は同じ場面に残す (hf も 52 秒の 1 場面)
section#forest(stagger: {each:0})
chap#ch3 {cn}03{/} 各研究の結果
chap#ch4 {cn}04{/} まとめた効果
chap#ch5 {cn}05{/} ばらつき
bt#bt4(no: "03"; ttl: "各研究の結果 ― フォレストプロット"; sub: "効果量 g（点）と 95% 信頼区間（横線）")
bt#bt5(no: "04"; ttl: "6 本をまとめた効果"; sub: "ランダム効果モデルで統合（◆ ＝ まとめた効果と 95% 信頼区間）")
bt#bt6(no: "05"; ttl: "研究ごとのばらつき"; sub: "異質性 I² と予測区間")
group#tbl(in: {opacity:0, duration:0.5})
  p#h1(left: 64px; top: 167px; font-size: 12px; letter-spacing: 0.04em; color: $ink3) 研究
  p#h2(left: 273px; top: 167px; font-size: 12px; letter-spacing: 0.04em; color: $ink3) 人数
  p#h3(left: 337px; top: 167px; font-size: 12px; letter-spacing: 0.04em; color: $ink3) g［95% 信頼区間］
  p#gh(left: 640px; top: 167px; font-size: 12px; letter-spacing: 0.04em; color: $ink3; out: {opacity:0, duration:0.3}) 効果量 g
  div#hair(left: 64px; top: "246;290;334;378;422"; width: 796px; height: 1px; background: #1E2B3C1A) ×5
# 表の行 (文字の丸・研究の中身・人数・g と区間)。g の数字は {v} で語ごとに色を替える
div#row(left: 64px; top: "203;247;291;335;379;423"; width: 796px; height: 41px; in: {x:-13, opacity:0, duration:0.5, ease:'power2.out', stagger:{each:0.09}}) ×6
  p#l(left: 0px; cy: 50%; width: 25px; text-align: center; font-size: 14px; font-family: n; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 3px 0px) A;B;C;D;E;F
  p#nm(left: 35px; cy: 50%; font-size: 15px; white-space: nowrap) 大学生 ジョギング;高齢者 早歩き;高齢者 有酸素＋筋トレ;若年 自転車こぎ 1 回;会社員 ヨガ;高齢者 筋トレ
  p#nn(left: 217px; cy: 50%; width: 36px; text-align: right; font-size: 15px; font-family: n) 120;64;210;48;90;150
  p#g(left: 273px; cy: 50%; font-size: 15px; font-family: n; white-space: nowrap) {v}0.45{/} {c}[0.09, 0.81]{/};{v}0.68{/} {c}[0.18, 1.18]{/};{v}0.18{/} {c}[−0.09, 0.45]{/};{v}0.92{/} {c}[0.33, 1.51]{/};{v}−0.06{/} {c}[−0.47, 0.35]{/};{v}0.22{/} {c}[−0.10, 0.54]{/}
# 軸 (−0.5〜1.5・0 は x = 592・1 あたり 167 px) と目盛り・両側の注記
div#axis(left: 493px; top: 548px; width: 367px; height: 1.5px; background: $ink; in: {scaleX:0, duration:0.7, ease:'power2.out', pivot:'left'})
group#ticks(in: {opacity:0, duration:0.4})
  div#tk(left: "509;593;676;759;843"; top: 549px; width: 1.5px; height: 7px; background: $ink) ×5
  p#tl(left: "490;573;657;740;823"; top: 557px; width: 40px; text-align: center; font-size: 12px; font-family: n; color: $ink2) ×5 −0.5;0;0.5;1.0;1.5
  p#al(right: 693px; top: 577px; font-size: 11px; font-family: m; color: $ink3) ← 対照群のほうが良い
  p#ar(left: 600px; top: 577px; font-size: 11px; font-family: m; color: $ink3) 運動群のほうが良い →
shape#zero(left: 592px; top: 200px; width: 2px; height: 348px; path: line_v; border: 2px solid $brick; dash: 5,4; in: {scaleY:0, duration:0.6, ease:'power2.out', pivot:'top'})
p#co0(left: 600px; top: 525px; font-size: 13px; color: $brick; in: {y:7, opacity:0, duration:0.4}; out: {opacity:0, duration:0.3}) 0 ＝ 差なし
# 区間 (両端にかぎ・語で左から伸びる)・点の正方形の大きさ = まとめるときの重み
shape#ci_a(path: "M608 219 L608 229 M608 224 L728 224 M728 219 L728 229"; background: none; border: 1.5px solid $ink; in: wipe {dir: 'right', duration: 0.55, ease: 'power2.out'})
shape#ci_b(path: "M623 263 L623 273 M623 268 L790 268 M790 263 L790 273"; background: none; border: 1.5px solid $ink; in: wipe {dir: 'right', duration: 0.55, ease: 'power2.out'})
shape#ci_c(path: "M578 307 L578 317 M578 312 L668 312 M668 307 L668 317"; background: none; border: 1.5px solid $ink; in: wipe {dir: 'right', duration: 0.55, ease: 'power2.out'})
shape#ci_d(path: "M648 351 L648 361 M648 356 L845 356 M845 351 L845 361"; background: none; border: 1.5px solid $ink; in: wipe {dir: 'right', duration: 0.55, ease: 'power2.out'})
shape#ci_e(path: "M515 395 L515 405 M515 400 L652 400 M652 395 L652 405"; background: none; border: 1.5px solid $ink; in: wipe {dir: 'right', duration: 0.55, ease: 'power2.out'})
shape#ci_f(path: "M577 439 L577 449 M577 444 L683 444 M683 439 L683 449"; background: none; border: 1.5px solid $ink; in: wipe {dir: 'right', duration: 0.55, ease: 'power2.out'})
# hf の作り: 点の正方形は場面の頭から出ている (scale 0 から出す入場が fromTo の即時描画で効かず、区間だけが後から伸びる)
div#sq(left: "658;698;612;739;573;619"; top: "213;259;300;348;390;433"; width: "21;18;24;16;20;22"; height: "21;18;24;16;20;22"; background: $ink; in: none) ×6
# まとめの行と罫・予測区間 (破線) と 0 より下の赤茶の部分・◆ (まとめた効果)・区間の端の値
div#sep(left: 64px; top: 479px; width: 796px; height: 1.5px; background: $ink; in: {scaleX:0, duration:0.6, ease:'power2.out', pivot:'left'})
div#pooled(left: 64px; top: 487px; width: 796px; height: 41px; in: {x:-13, opacity:0, duration:0.5, ease:'power2.out'})
  p#l(left: 0px; cy: 50%; width: 25px; text-align: center; font-size: 14px; color: #FFFFFF; background: $ochre; border-radius: 99px; padding: 3px 0px) ◆
  p#nm(left: 35px; cy: 50%; font-size: 15px; white-space: nowrap) まとめ（ランダム効果）
  p#nn(left: 217px; cy: 50%; width: 36px; text-align: right; font-size: 15px; font-family: n) 682
  p#g(left: 273px; cy: 50%; font-size: 15px; font-family: n; color: $ochre; white-space: nowrap) 0.34 {c}[0.11, 0.58]{/}
shape#pi(left: 538px; top: 506px; width: 223px; height: 2px; path: line_h; border: 2px solid $ochre_f; dash: 4,3; in: {scaleX:0, duration:1.4, ease:'power2.inOut'})
div#pineg(left: 538px; top: 506px; width: 55px; height: 3px; border-radius: 2px; background: $brick; in: {scaleX:0, duration:0.8, ease:'power2.out', pivot:'right'})
shape#dia(points: "612,508 651,495 690,508 651,521"; background: $ochre_f; in: {scaleX:0, scaleY:0.2, duration:0.9, ease:'power3.out'})
p#ci_lo(cx: 612px; top: 524px; font-size: 12px; font-family: n; color: $ochre; in: {y:5, opacity:0, duration:0.4}; out: {opacity:0, duration:0.4}) 0.11
p#ci_hi(cx: 690px; top: 524px; font-size: 12px; font-family: n; color: $ochre; in: {y:5, opacity:0, duration:0.4}; out: {opacity:0, duration:0.4}) 0.58
p#pi_lo(cx: 538px; top: 524px; font-size: 12px; font-family: n; color: $ochre; in: {opacity:0, duration:0.4}) −0.33
p#pi_hi(cx: 762px; top: 524px; font-size: 12px; font-family: n; color: $ochre; in: {opacity:0, duration:0.4}) 1.01
# 6 本の結果の広がり (かぎ + 札)
shape#spread(path: "M583 205 L583 193 L746 193 L746 205"; background: none; border: 1.5px solid $ink2; in: {scaleX:0.3, opacity:0, duration:0.7, ease:'power3.out'}; out: {opacity:0, duration:0.4})
p#spread_l(left: 583px; top: 172px; width: 163px; text-align: center; font-size: 12px; color: $ink2; in: {opacity:0, duration:0.4}; out: {opacity:0, duration:0.4}) 6 本の結果の広がり
# 右の板 1: 読み方 (語ごとに凡例の行の地が黄土に光る)
panel#fp1(left: 897px; top: 157px; width: 319px; height: 246px; hd: "読み方")
  div#leg1(left: 20px; top: 53px; width: 279px; height: 38px; border-radius: 4px)
    div#sw(left: 10px; top: 11px; width: 16px; height: 16px; background: $ink)
    p#t(left: 47px; top: 0px; font-size: 14px; font-family: m) 点 ＝ 効果量 g
    p#s(left: 47px; top: 21px; font-size: 11px; font-family: m; color: $ink3) 大きさ ＝ まとめるときの重み
  div#leg2(left: 20px; top: 104px; width: 279px; height: 21px; border-radius: 4px)
    div#sw(left: 0px; top: 10px; width: 36px; height: 2px; background: $ink)
    p#t(left: 47px; top: 0px; font-size: 14px; font-family: m) 横線 ＝ 95% 信頼区間
  div#leg3(left: 20px; top: 139px; width: 279px; height: 21px; border-radius: 4px)
    shape#sw(left: 17px; top: -2px; width: 2px; height: 24px; path: line_v; border: 1.5px solid $brick; dash: 3,2)
    p#t(left: 47px; top: 0px; font-size: 14px; font-family: m) 0 の線 ＝ 差なし
  div#rule(left: 20px; top: 174px; width: 279px; height: 1px; background: #1E2B3C1F)
  p#nt(left: 20px; top: 184px; font-size: 13px; font-family: m; line-height: 1.55; color: $ink2) 区間が 0 をまたがなければ[br]「差あり」と言える
# 右の板 2: 判定 (3 本 ／ 6 本)
panel#fp2(left: 897px; top: 157px; width: 319px; height: 240px; hd: "判定")
  p#big(left: 20px; top: 46px; font-size: 69px; line-height: 1; font-family: n; color: $teal) 3
  p#u(left: .big.right+7; top: 86px; font-size: 20px; color: $teal) 本
  p#o(left: .u.right+7; top: 90px; font-size: 16px; color: $ink2) ／ 6 本
  p#n1(left: 20px; top: 122px; font-size: 14px; font-family: m; line-height: 1.55; color: $ink2) {tb}差あり：A・B・D{/}[br]区間が 0 をまたがない
  p#n2(left: 20px; top: 176px; font-size: 14px; font-family: m; line-height: 1.55; color: $ink2) {sb}0 をまたぐ：C・E・F{/}[br]差があるとは言い切れない
# 右の板 3: まとめた効果 (g = 0.34 が桁ごとに回る)
# hf の作り: 「小〜中程度の効果」の札は板が消えた後の語に出る (見えない) ので写さない
panel#fp3(left: 897px; top: 157px; width: 319px; height: 205px; hd: "まとめた効果（ランダム効果モデル）")
  p#g(left: 20px; top: 68px; font-size: 36px; font-family: n; italic: true) g =
  p#v(left: .g.right+12; top: 46px; font-size: 69px; line-height: 1; font-family: n; color: $ochre; in: {opacity:0, duration:0.35, ease:'power2.out'}) [count:0.34 start=0 roll ms=1350,1470,1590]
  p#ci(left: 20px; top: 125px; font-size: 14px; font-family: m; color: $ink2) 95% 信頼区間 {nb}0.11 〜 0.58{/}
# 右の板 4: 0.34 を言い換えると (約 63% が 4 秒かけて回り、100 個の点のうち 63 個が順に青緑に)
panel#fp4(left: 897px; top: 157px; width: 319px; height: 437px; hd: "0.34 を言い換えると")
  p#y(left: 20px; top: 86px; font-size: 20px) 約
  p#v(left: .y.right+4; top: 46px; font-size: 69px; line-height: 1; font-family: n; color: $teal; in: {opacity:0, duration:0.35, ease:'power2.out'}) [count:63 start=0 roll ms=3890,4010 ease=ease_in_out]
  p#u(left: .v.right+4; top: 82px; font-size: 29px) %
  p#nt(left: 20px; top: 118px; width: 279px; font-size: 13px; font-family: m; line-height: 1.55; color: $ink2) 平均的な運動群の人は、対照群の約 63% の人より成績が良い
  shape#dot.ellipse(left: "20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230"; top: "170;170;170;170;170;170;170;170;170;170;193;193;193;193;193;193;193;193;193;193;217;217;217;217;217;217;217;217;217;217;240;240;240;240;240;240;240;240;240;240;263;263;263;263;263;263;263;263;263;263;286;286;286;286;286;286;286;286;286;286;310;310;310;310;310;310;310;310;310;310;333;333;333;333;333;333;333;333;333;333;356;356;356;356;356;356;356;356;356;356;380;380;380;380;380;380;380;380;380;380"; width: 17px; height: 17px; background: $slate_l; border: 1.5px solid #C4CBD3) ×100
  shape#fill.ellipse(left: "20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67;90;113;136;160;183;206;230;20;43;67"; top: "170;170;170;170;170;170;170;170;170;170;193;193;193;193;193;193;193;193;193;193;217;217;217;217;217;217;217;217;217;217;240;240;240;240;240;240;240;240;240;240;263;263;263;263;263;263;263;263;263;263;286;286;286;286;286;286;286;286;286;286;310;310;310"; width: 17px; height: 17px; background: $teal; in: {scale:0, duration:0.3, ease:'back.out(2)', stagger:{each:0.035}}) ×63
  p#cp(left: 20px; top: 402px; width: 279px; font-size: 11px; font-family: m; color: $ink3) ● ＝ 対照群 100 人のうち、平均的な運動群の人が上回る人
# 右の板 5: まとめるときの重み (人数の多い順の横棒・棒の幅 = 重み ÷ 24% × 181 px)
panel#fp5(left: 897px; top: 157px; width: 319px; height: 281px; hd: "まとめるときの重み")
  p#nt(left: 20px; top: 42px; font-size: 13px; font-family: m; color: $ink2) 人数の多い研究ほど重い
  div#w(left: 20px; top: "71;105;138;171;205;238"; width: 279px; height: 24px) ×6
    p#l(left: 0px; cy: 50%; width: 24px; text-align: center; font-size: 13px; font-family: n; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 3px 0px) C;F;A;E;B;D
    div#tr(left: 35px; cy: 50%; width: 181px; height: 17px; border-radius: 3px; background: $paper2)
    div#f(left: 35px; cy: 50%; width: "169;151;137;122;97;79"; height: 17px; border-radius: 3px; background: $ink; in: {scaleX:0, duration:0.8, ease:'power3.out', pivot:'left'})
    p#n(left: 42px; cy: 50%; font-size: 10px; color: #FFFFFF) 210 人;150 人;120 人;90 人;64 人;48 人
    p#v(right: 0px; cy: 50%; font-size: 14px; font-family: n) 22.4%;20.0%;18.1%;16.1%;12.9%;10.5%
# 右の板 6: 研究間の異質性 (I² = 54% が回り、0〜100% の帯が 54% まで伸びる)
panel#fp6(left: 897px; top: 157px; width: 319px; height: 251px; hd: "研究間の異質性")
  p#g(left: 20px; top: 72px; font-size: 33px; font-family: n; italic: true) I² =
  p#v(left: .g.right+9; top: 46px; font-size: 69px; line-height: 1; font-family: n; color: $ochre; in: {opacity:0, duration:0.35, ease:'power2.out'}) [count:54 start=0 roll ms=1300,1420]
  p#u(left: .v.right+4; top: 82px; font-size: 29px) %
  div#mt(left: 20px; top: 129px; width: 279px; height: 20px; border-radius: 4px; background: $paper2)
  div#mf(left: 20px; top: 129px; width: 151px; height: 20px; border-radius: 4px 0px 0px 4px; background: $ochre_f; in: {scaleX:0, duration:1.2, ease:'power3.out', pivot:'left'})
  p#m0(left: 20px; top: 152px; font-size: 11px; font-family: n; color: $ink3) 0%
  p#m1(cx: 171px; top: 152px; font-size: 11px; font-family: n; color: $ink3) 54%
  p#m2(right: 20px; top: 152px; font-size: 11px; font-family: n; color: $ink3) 100%
  p#chip(left: 20px; top: 178px; font-size: 13px; color: #8A5512; background: $ochre_l; border-radius: 99px; padding: 3px 11px) 中程度のばらつき
  p#nt(left: 20px; top: 213px; font-size: 13px; font-family: m; color: $ink2) 結果の違いが、偶然だけでは説明しきれない
# 右の板 7: 予測区間 (語で赤茶の注意の札)
panel#fp7(left: 897px; top: 157px; width: 319px; height: 230px; hd: "予測区間")
  p#v(left: 20px; top: 46px; font-size: 43px; line-height: 1.2; font-family: n; color: $ochre; white-space: nowrap) −0.33{tl} 〜 {/}1.01
  p#nt(left: 20px; top: 106px; font-size: 13px; font-family: m; line-height: 1.55; color: $ink2) 次に同じような研究をしたときに[br]出そうな効果の幅
  p#neg(left: 20px; top: 156px; width: 279px; font-size: 13px; line-height: 1.55; color: #7C3322; background: $brick_l; border-radius: 5px; padding: 8px 11px; in: up) 0 より下まで届く ＝ 効果がほぼ出ない研究もありうる

# s07 運動の種類: 軸 → 青緑の帯 (有酸素・A B D の丸と ◆ 0.61) → 灰の帯 (それ以外・◆ 0.15)。右の表は「ただし」でテストの列が入り、有酸素の 3 行に黄土の帯 → 「?」の板
section#s07(stagger: {each:0})
chap#ch6 {cn}06{/} 運動の種類
bt#bt7(no: "06"; ttl: "運動の種類で分けると"; sub: "有酸素運動の 3 本 と それ以外の 3 本")
div#ax7(left: 280px; top: 493px; width: 387px; height: 1.5px; background: $ink; in: {scaleX:0, duration:0.7, ease:'power2.out', pivot:'left'})
group#tk7(in: {opacity:0, duration:0.4})
  div#tk(left: "307;362;417;473;528;583;638"; top: 494px; width: 1.5px; height: 7px; background: $ink) ×7
  p#tl(left: "288;343;398;453;509;564;619"; top: 504px; width: 40px; text-align: center; font-size: 12px; font-family: n; color: $ink2) ×7 −0.2;0;0.2;0.4;0.6;0.8;1.0
  p#cap(left: 280px; top: 528px; width: 387px; text-align: center; font-size: 11px; font-family: m; color: $ink3) 効果量 g（◆ ＝ グループごとにまとめた効果と 95% 信頼区間）
shape#z7(left: 361px; top: 220px; width: 2px; height: 273px; path: line_v; border: 2px solid $brick; dash: 5,4; in: {scaleY:0, duration:0.6, ease:'power2.out', pivot:'top'})
div#band1(left: 53px; top: 225px; width: 733px; height: 117px; border-radius: 9px; background: #D3E7E48C; in: {scaleX:0.96, opacity:0, duration:0.6, ease:'power2.out'})
group#lab1(in: up)
  p#t(left: 64px; top: 245px; font-size: 24px; color: $teal) 有酸素運動
  p#s(left: 64px; top: 281px; font-size: 13px; font-family: m; line-height: 1.45; color: $ink2) A・B・D ／ 232 人[br]ジョギング・早歩き・自転車こぎ
shape#d1.ellipse(left: "482;545;612"; top: 248px; width: 11px; height: 11px; background: $card; border: 1.7px solid $teal; in: {scale:0, duration:0.4, ease:'back.out(2)', stagger:{each:0.15}}) ×3
p#d1l(cx: "487;551;617"; top: 229px; font-size: 11px; font-family: n; color: $teal; in: {scale:0, duration:0.4, ease:'back.out(2)', stagger:{each:0.15}}) ×3 A;B;D
shape#dia1(points: "457,287 530,272 603,287 530,301"; background: $teal; in: {scaleX:0, duration:0.9, ease:'power3.out'})
group#big1(in: up)
  p#v(right: 494px; top: 260px; font-size: 48px; line-height: 1; font-family: n; color: $teal) 0.61
  p#c(right: 494px; top: 311px; font-size: 13px; font-family: n; color: $ink3) [0.34, 0.87]
div#band2(left: 53px; top: 365px; width: 733px; height: 117px; border-radius: 9px; background: #E2E5E999; in: {scaleX:0.96, opacity:0, duration:0.6, ease:'power2.out'})
group#lab2(in: up)
  p#t(left: 64px; top: 385px; font-size: 24px; color: #4F5965) それ以外
  p#s(left: 64px; top: 421px; font-size: 13px; font-family: m; line-height: 1.45; color: $ink2) C・E・F ／ 450 人[br]筋トレ・組み合わせ・ヨガ
shape#d2.ellipse(left: "407;341;418"; top: 388px; width: 11px; height: 11px; background: $card; border: 1.7px solid $slate; in: {scale:0, duration:0.4, ease:'back.out(2)', stagger:{each:0.15}}) ×3
p#d2l(cx: "407;346;430"; top: 369px; font-size: 11px; font-family: n; color: #4F5965; in: {scale:0, duration:0.4, ease:'back.out(2)', stagger:{each:0.15}}) ×3 C;E;F
shape#dia2(points: "352,427 403,412 454,427 403,441"; background: $slate; in: {scaleX:0, duration:0.9, ease:'power3.out'})
group#big2(in: up)
  p#v(right: 494px; top: 400px; font-size: 48px; line-height: 1; font-family: n; color: #4F5965) 0.15
  p#c(right: 494px; top: 451px; font-size: 13px; font-family: n; color: $ink3) [−0.04, 0.33]
# 重なりの表: 運動とテストの列・有酸素の 3 行のテストに黄土の帯 (語で左から)
panel#t7(left: 797px; top: 167px; width: 419px; height: 305px; hd: "ただし：運動とテストが重なっている")
  p#hd(left: "17;53;196"; top: 52px; font-size: 11px; color: $ink3) ×3 研究;運動;記憶テスト
  div#mk(left: 196px; top: "80;116;152"; width: 199px; height: 22px; border-radius: 3px; background: $ochre_l; in: {scaleX:0, duration:0.5, ease:'power2.out', pivot:'left'}) ×3
  div#r(left: 17px; top: "73;109;145;181;217;253"; width: 384px; height: 36px) ×6
    div#ln(left: 0px; top: 0px; width: 384px; height: 1px; background: #1E2B3C1A)
    p#lt(left: 0px; cy: 50%; font-size: 15px; font-family: n; color: "$teal;$teal;$teal;#56606C;#56606C;#56606C") A;B;D;C;E;F
    p#ex(left: 36px; cy: 50%; font-size: 13px; font-family: m) ジョギング;早歩き;自転車こぎ（1 回）;有酸素＋筋トレ;ヨガ・ストレッチ;筋トレ
    p#tc(left: 184px; cy: 50%; font-size: 13px; font-family: m; in: {x:-9, opacity:0, duration:0.4}) 単語リストの再生;単語リストの遅延再生;直後の単語リスト再生;物語の再生;数字の順唱（作業記憶）;図形の位置の記憶
div#conf(left: 797px; top: 493px; width: 419px; height: 89px; background: $card; border: 1px solid #1E2B3C1A; border-radius: 9px; box-shadow: 0px 9px 23px #3C321E1A; in: up)
  p#q(left: 17px; cy: 50%; font-size: 36px; font-family: n; color: $brick) ?
  p#t(left: 53px; top: 22px; font-size: 15px; white-space: nowrap) 差は「運動の種類」？ それとも「テストの種類」？
  p#s(left: 53px; top: 47px; font-size: 13px; font-family: m; color: $ink2) この 6 本では切り分けられない

# s08 言えないこと: 左に散布図 (参加者数 × 効果量) の点が弾み、右に限界の札 4 枚を語ごとに。D と B が赤茶に膨らみ、下がる傾向の破線・見えない研究の破線の丸・引き出しの絵
section#s08(stagger: {each:0})
chap#ch7 {cn}07{/} 言えないこと
bt#bt8(no: "07"; ttl: "言えないこと（限界）"; sub: "結果を読むときに注意したい 4 点")
group#fr8(in: {opacity:0, duration:0.6})
  div#xa(left: 120px; top: 533px; width: 373px; height: 1.5px; background: $ink)
  div#ya(left: 119px; top: 220px; width: 1.5px; height: 314px; background: $ink)
  div#xt(left: "119;197;275;353;430"; top: 534px; width: 1.5px; height: 7px; background: $ink) ×5
  p#xl(left: "100;178;256;333;411"; top: 543px; width: 40px; text-align: center; font-size: 12px; font-family: n; color: $ink2) ×5 0;50;100;150;200
  div#yt(left: 113px; top: "480;350;219"; width: 7px; height: 1.5px; background: $ink) ×3
  p#yl(left: 75px; top: "472;342;211"; width: 33px; text-align: right; font-size: 12px; font-family: n; color: $ink2) ×3 0;0.5;1.0
  shape#z(left: 121px; top: 480px; width: 372px; height: 2px; path: line_h; border: 1.5px solid $brick; dash: 4,3)
  p#xn(left: 120px; top: 564px; width: 373px; text-align: center; font-size: 13px; color: $ink2) 参加者数（人）
  p#yn(left: 64px; top: 193px; font-size: 13px; color: $ink2) 効果量 g
shape#sd.ellipse(left: "299;212;439;187;253;346"; top: "356;296;427;234;489;416"; width: 15px; height: 15px; background: $ink2; in: {scale:0, duration:0.4, ease:'back.out(2)', stagger:{each:0.12}}) ×6
group#sl(in: {opacity:0, duration:0.4})
  p#l(left: "317;230;457;205;271;364"; top: "355;295;426;232;488;415"; font-size: 12px; color: $ink2) ×6 A;B;C;D;E;F
p#db_d(left: 217px; top: 232px; font-size: 12px; color: $brick; in: {opacity:0, duration:0.4}) 48 人・g 0.92
p#db_b(left: 242px; top: 295px; font-size: 12px; color: $brick; in: {opacity:0, duration:0.4}) 64 人・g 0.68
shape#trend(path: "M220 270 L460 410"; background: none; border: 2px solid $ochre; dash: 5,4; in: draw {duration: 0.9})
p#trend_l(left: 365px; top: 292px; font-size: 13px; line-height: 1.35; color: $ochre; in: {opacity:0, duration:0.4}) 小さい研究ほど[br]効果が大きい
shape#gh(left: "172;200;225"; top: "463;508;450"; width: 15px; height: 15px; path: rect,r=0.5; background: none; border: 1.5px solid $brick; dash: 1,5; in: {scale:0.4, opacity:0, duration:0.45, ease:'back.out(2)', stagger:{each:0.15}}) ×3
p#gh_l(left: 131px; top: 429px; font-size: 12px; line-height: 1.3; color: $brick; in: {opacity:0, duration:0.4}) ここにあるはずの研究が[br]見えていない？
img#drawer(left: 527px; top: 400px; width: 113px; height: 133px; object-fit: contain; main: none; in: {y:20, opacity:0, duration:0.7, ease:'power3.out'}) [transparent]上の引き出しが開いた濃い紺の金属の書類棚。公表されなかった研究論文とマニラフォルダーが詰め込まれ、紙が数枚はみ出している。単体で全体が入り周りに少し余白、背景・地面・床の影なし
p#drawer_l(left: 507px; top: 541px; width: 153px; text-align: center; font-size: 11px; line-height: 1.4; color: $ink2; in: {opacity:0, duration:0.4}) 結果の出なかった研究は[br]引き出しの中？
lcard#lc1(top: 167px; no: "1"; hd: "効果が大きい 2 本は、参加者がいちばん少ない 2 本"; d: "D 0.92（48 人）・B 0.68（64 人）。結果の出なかった研究が公表されていない可能性")
lcard#lc2(top: 277px; no: "2"; hd: "D は 1 回だけの運動の直後に測った結果"; d: "長く続けたときの効果とは別物")
lcard#lc3(top: 388px; no: "3"; hd: "6 本では数が少ない"; d: "年齢や期間による違いは確かめられない")
lcard#lc4(top: 499px; no: "4"; hd: "最長でも 52 週"; d: "何年も先の記憶や、{m}認知症の予防までは言えない{/}")
#lc1.on(border: 1px solid #B87523E6)
#lc2.on(border: 1px solid #B87523E6)
#lc3.on(border: 1px solid #B87523E6)
#lc4.on(border: 1px solid #B87523E6)

# s09 結論: 遠くへ伸びる道の絵がゆっくり寄り、上を紙色の幕で空けて 3 行の結論を文の頭で。要の語に黄土の下帯が左から引かれる
section#s09(stagger: {each:0})
chap#ch8 {cn}08{/} 結論
img#road(inset: 0; subject: bottom 40%; room: top 55%; main: kb {scale: [1, 1.12], focus: ['50% 62%', '50% 62%'], ease:'sine.inOut'}) 横長の風景。日の出の、なだらかに起伏する丘のあいだを遠くの地平線までまっすぐ伸びる長い一本道。道のずっと先に小さな走る人がひとり、まだ長い道のりが続く感じ。丘と道は画面の下半分、上半分は柔らかなグラデーションの空で何も置かない
div#veil9(inset: 0; background: linear(#F2EDE2F2,#F2EDE2E6@50%,#F2EDE28C@62%,#F2EDE214@80%,#F2EDE200,180); in: none)
bt#bt9(no: "08"; ttl: "結論")
concl#cc1(top: 157px; hd: "運動は記憶を「小〜中程度」良くする"; d: "6 本をまとめた効果　g = 0.34［95% 信頼区間 0.11〜0.58］")
concl#cc2(top: 248px; height: 112px; hd: "ただし差は大きく、はっきりしているのは[br]{m}有酸素運動 × 単語の記憶{/}"; d: "異質性 I² = 54%・予測区間 −0.33〜1.01")
  p#d(top: 76px)
concl#cc3(top: 365px; hd: "言い切るには、{m}大きくて長い研究{/}がまだ足りない"; d: "大きな効果は小さい研究に偏り、期間も最長 52 週")

# end 締めの題: 紙色の地に小札 → 明朝の題 → 副題 → 注記を中央に順に (最後の frame まで残す)
section#end(stagger: {each:0})
div#endbg(inset: 0; background: $paper; in: none)
p#ek(cx: 640px; top: 222px; font-size: 13px; letter-spacing: 0.24em; color: $ochre; delay: 300; in: {y:11, opacity:0, duration:0.6, ease:'power2.out'}) RESEARCH REVIEW
p#et(cx: 640px; top: 257px; font-size: 61px; font-family: s; delay: 450; in: {y:16, opacity:0, duration:0.8, ease:'power3.out'}) 運動は記憶に効くのか
p#es(cx: 640px; top: 350px; font-size: 27px; font-family: s; color: $ink2; delay: 700; in: {y:11, opacity:0, duration:0.6, ease:'power2.out'}) — 研究 6 本を読み比べる
p#ef(cx: 640px; top: 419px; font-size: 13px; font-family: m; line-height: 1.8; text-align: center; color: $ink3; delay: 1000; in: {opacity:0, duration:0.6}) ※ 研究 A〜F は解説用の架空データです[br]効果量：標準化平均差 g ／ 統合：ランダム効果モデル ／ 参加者 合計 682 人
```

```timeline.txt
#v2
cast n = "落ち着いた低めの声の 30〜40 代の男性ナレーター、響きが豊かで滑らか、知的で信頼感のある語り口で学術的な調査を落ち着いて解説する" speed=114%
silence head=0 tail=0
# 場面の切替は hf と同じ 0.6 秒の溶け (新場面の頭で風切り・hf の旧場面 / 新場面の左右 27 px の流れは写さない)。場面ごとの台詞は 1 行 = 1 回の合成で、句の切れ目は [|]
# 字幕は hf の表示の文字 (数字・記号) で、声は hf の読み ({表記|読み})
transition = dissolve,600,overlap=600,se=whoosh -6dB

*** s01
[>#subtitle]
bgm music
@n: [silence:1.1s][♪glock -1dB -800][>#quote +100][♪page -2dB +100][>#qm +500]「運動すると記憶力が上がる」。よく聞く話ですが、研究によって結果は[>#teaser -400][>#teaser.ax -300][>#teaser.dot +100][♪tap -16dB +100][♪tap -16dB +230][♪tap -16dB +360][♪tap -16dB +490][♪tap -16dB +620][♪tap -16dB +750]まちまちです。[<#title -550][<#quote -550][<#qm -550][<#teaser -550][>#s1_dim -550][!#hero to,{blur:2, duration:0.7, ease:'power2.inOut'} -550][♪whoosh -6dB -550][>#hdr -400][>#hdr_rule -400][>#prog -400][>#ch0 -400][>#dg.pop -100][♪tap -13dB -100][>#dg.l1 +200][>#dg.rand +300][>#dg.l2a +400][♪tap -13dB +450][>#dg.ex +550]運動群と[>#dg.l2b -150][>#dg.ct][♪tap -13dB][>#dg.l3 +600][>#dg.l4 +700][>#dg.test +900][♪tap -13dB +900]対照群を比べた、架空の無作為化比較[>#st6 -150][>#st6.v -100][!#st6.v count -100][♪tap -14dB +50][>#dg.note +200]試験 6 本、[|][>#st682 +150][>#st682.v +200][♪bell -5dB +1700]合計 682 人を読み比べます。[silence:0.05s]

*** s02
@n: [silence:0.45s][>#bt2 -250][>#base2 -150][>#ct +50][>#ex +450][>#gap +1150]記憶テストは研究ごとに違うため、[|]効果の大きさを「[>#defs -200][♪page -2dB -200]標準化平均差 {g|ジー}」という物差しにそろえます。[>#scale -900][!#ex to,{x:-53, duration:0.9, ease:'power3.inOut'}][!#gap to,{opacity:0, duration:0.3}][!#gap.ln to,{scaleX:0.02, pivot:'left', duration:0.9, ease:'power3.inOut'}][!#gap.t to,{x:-27, duration:0.9, ease:'power3.inOut'}][!#scale.mk to,{x:-230, duration:0.9, ease:'power3.inOut'}][!#scale.rl[1] to,{scale:1.22, duration:0.25} +400][!#scale.rl[1] to,{scale:1, duration:0.4, ease:'power2.inOut'} +1100][♪tap -13dB]0 なら差なし、[!#ex to,{x:-32, duration:0.9, ease:'power3.inOut'}][!#gap.ln to,{scaleX:0.4, pivot:'left', duration:0.9, ease:'power3.inOut'}][!#gap.t to,{x:-16, duration:0.9, ease:'power3.inOut'}][!#gap to,{opacity:1, duration:0.3} +300][!#scale.mk to,{x:-138, duration:0.9, ease:'power3.inOut'}][!#scale.rl[2] to,{scale:1.22, duration:0.25} +400][!#scale.rl[2] to,{scale:1, duration:0.4, ease:'power2.inOut'} +1100][♪tap -13dB]0.2 で小、[!#ex to,{x:0, duration:0.9, ease:'power3.inOut'}][!#gap.ln to,{scaleX:1, pivot:'left', duration:0.9, ease:'power3.inOut'}][!#gap.t to,{x:0, duration:0.9, ease:'power3.inOut'}][!#scale.mk to,{x:0, duration:0.9, ease:'power3.inOut'}][!#scale.rl[3] to,{scale:1.22, duration:0.25} +400][!#scale.rl[3] to,{scale:1, duration:0.4, ease:'power2.inOut'} +1100][♪tap -13dB]0.5 で{中程度|中程度です}。[silence:0.05s]

*** s03
@n: [silence:0.45s][>#bt3 -250]6 本の中身はさまざまです。[>#ca -150][!#ca frame,#B87523D9 -100][=#ca +1100][♪page -1dB -150]大学生のジョギング、高齢者の[>#cb -150][!#cb frame,#B87523D9 -100][=#cb +1100][♪page -1dB -150]早歩きや[>#cf -150][!#cf frame,#B87523D9 -100][=#cf +1100][♪page -1dB -150]筋トレ、その[>#cc -150][!#cc frame,#B87523D9 -100][=#cc +1100][♪page -1dB -150]組み合わせ、[|]1 回だけの[>#cd -150][!#cd frame,#B87523D9 -100][=#cd +1100][♪page -1dB -150]自転車こぎ、会社員の[>#ce -150][!#ce frame,#B87523D9 -100][=#ce +1100][♪page -1dB -150]ヨガ。[>#period -200][>#ca.pf +100][♪pencil -3dB +100][>#ca.pv +300][>#cb.pf +220][>#cb.pv +420][>#cc.pf +340][>#cc.pv +540][>#cd.pf +460][>#cd.pv +660][>#ce.pf +580][>#ce.pv +780][>#cf.pf +700][>#cf.pv +900]期間も、1 回きりから 52 週までと幅があります。[silence:0.05s]

*** forest
@n: [silence:0.45s][>#bt4 -250][>#tbl -150][>#row -50]結果を[>#axis -200][>#zero][>#ticks +200][>#ci_a +350][>#ci_b +570][>#ci_c +790][>#ci_d +1010][>#ci_e +1230][>#ci_f +1450][♪pencil +0dB +350][>#fp1 +400]フォレストプロットに並べます。[!#fp1.leg1 fill,#F2E1C3,duration=300][=#fp1.leg1 +1600][!#sq[*] to,{scale:1.4, duration:0.25, stagger:0.08} +100][!#sq[*] to,{scale:1, duration:0.45, ease:'power2.inOut', stagger:0.08} +450][♪tap -13dB]点が効果量、[!#fp1.leg2 fill,#F2E1C3,duration=300][=#fp1.leg2 +1600][!#ci_a to,{scaleY:2.2, duration:0.25} +100][!#ci_a to,{scaleY:1, duration:0.45} +450][!#ci_b to,{scaleY:2.2, duration:0.25} +180][!#ci_b to,{scaleY:1, duration:0.45} +530][!#ci_c to,{scaleY:2.2, duration:0.25} +260][!#ci_c to,{scaleY:1, duration:0.45} +610][!#ci_d to,{scaleY:2.2, duration:0.25} +340][!#ci_d to,{scaleY:1, duration:0.45} +690][!#ci_e to,{scaleY:2.2, duration:0.25} +420][!#ci_e to,{scaleY:1, duration:0.45} +770][!#ci_f to,{scaleY:2.2, duration:0.25} +500][!#ci_f to,{scaleY:1, duration:0.45} +850][♪tap -13dB]横線が 95% {信頼区間|信頼区間です}。区間が [!#zero to,{scaleX:2, duration:0.3}][!#zero to,{scaleX:1, duration:0.6} +1000][>#co0][!#fp1.leg3 fill,#F2E1C3,duration=300][=#fp1.leg3 +1600][♪tap -13dB]0 をまたがず「差あり」と言えるのは [<#co0 -300][<#fp1 -400][>#fp2][!#ci_a recolor,#24727A,duration=400 +150][!#sq[1] fill,#24727A,duration=400 +150][!#row[1].l fill,#24727A,duration=400 +150][!#row[1].g{v} recolor,#24727A,duration=400 +150][!#ci_b recolor,#24727A,duration=400 +400][!#sq[2] fill,#24727A,duration=400 +400][!#row[2].l fill,#24727A,duration=400 +400][!#row[2].g{v} recolor,#24727A,duration=400 +400][!#ci_d recolor,#24727A,duration=400 +650][!#sq[4] fill,#24727A,duration=400 +650][!#row[4].l fill,#24727A,duration=400 +650][!#row[4].g{v} recolor,#24727A,duration=400 +650][♪bell -7dB +150]{A・B・D|エー、ビー、ディー}の 3 本。[!#ci_c recolor,#8D97A4,duration=400 +150][!#sq[3] fill,#8D97A4,duration=400 +150][!#row[3].l fill,#66707C,duration=400 +150][!#row[3].g{v} recolor,#5B6570,duration=400 +150][!#ci_e recolor,#8D97A4,duration=400 +400][!#sq[5] fill,#8D97A4,duration=400 +400][!#row[5].l fill,#66707C,duration=400 +400][!#row[5].g{v} recolor,#5B6570,duration=400 +400][!#ci_f recolor,#8D97A4,duration=400 +650][!#sq[6] fill,#8D97A4,duration=400 +650][!#row[6].l fill,#66707C,duration=400 +650][!#row[6].g{v} recolor,#5B6570,duration=400 +650][♪tap -13dB +150]{C・E・F|シー、イー、エフ}は 0 をまたいでいます。[silence:0.5s]
@: [<#bt4 -550][<#ch3 -450][>#ch4 -450][>#bt5 -250][♪whoosh -9dB -450][>#sep +100][>#pooled +300]ランダム効果モデルで 6 本をまとめると {g = |ジーは}[<#fp2 -1250][>#fp3 -900][>#fp3.v -800][>#dia -200][♪glock +2dB -150]{0.34|れいてんさんよん}。[>#ci_lo][>#ci_hi][♪tap -13dB]95% 信頼区間は {0.11〜0.58|れいてんいちいちから、れいてんごはち}。[<#fp3 -350][>#fp4][♪bell -6dB][♪page -2dB][>#fp4.v +500][!#fp4.v count +500][>#fp4.fill +600]{小〜中程度|小から中程度}の効果で、平均的な運動群の人は、[|]対照群の[♪bell -5dB +1000]約 63% の人より成績が良い計算です。[<#fp4 -350][>#fp5][♪page -2dB][>#fp5.w[1].f +300][!#sq[3] to,{scale:1.35, duration:0.22} +300][!#sq[3] to,{scale:1, duration:0.4} +550][>#fp5.w[2].f +420][!#sq[6] to,{scale:1.35, duration:0.22} +420][!#sq[6] to,{scale:1, duration:0.4} +670][>#fp5.w[3].f +540][!#sq[1] to,{scale:1.35, duration:0.22} +540][!#sq[1] to,{scale:1, duration:0.4} +790][>#fp5.w[4].f +660][!#sq[5] to,{scale:1.35, duration:0.22} +660][!#sq[5] to,{scale:1, duration:0.4} +910][>#fp5.w[5].f +780][!#sq[2] to,{scale:1.35, duration:0.22} +780][!#sq[2] to,{scale:1, duration:0.4} +1030][>#fp5.w[6].f +900][!#sq[4] to,{scale:1.35, duration:0.22} +900][!#sq[4] to,{scale:1, duration:0.4} +1150]{まとめるときの重みは|重みは}、人数の多い研究ほど{大きい|大きくなります}。[silence:0.5s]
@: [<#bt5 -550][<#ch4 -450][>#ch5 -450][>#bt6 -250][♪whoosh -9dB -450]ただし、[<#tbl.gh -300][>#spread][>#spread_l +300][♪tap -13dB]ばらつきも{中程度|中程度です}。{異質性 |いしつせい、}[<#fp5 -950][>#fp6 -600][>#fp6.v -450][!#fp6.v count -450][>#fp6.mf +100][♪bell -5dB +1900]{I² = 54%|アイ二乗は 54%}。[<#fp6 -350][>#fp7][<#ci_lo][<#ci_hi][<#spread][<#spread_l][>#pi +300][♪pencil -1dB +300]次に同じような研究をしたときに出そうな効果の幅{ ＝ |、}予測区間は、[|][>#pi_lo][>#pi_hi]{−0.33〜1.01|マイナスれいてんさんさんから、いってんれいいち}と広く、[|][>#pineg -100][>#fp7.neg][♪tap -13dB]効果がほぼ出ない研究も、ありえます。[silence:0.05s]

*** s07
@n: [silence:0.45s][>#bt7 -250][>#ax7 -50][>#z7 +150][>#tk7 +250][>#t7 +450]運動の種類で分けると、[|][>#band1 -400][>#lab1 -300][>#d1][>#d1l][>#dia1 +500][♪glock +3dB +500][>#big1 +700]有酸素運動の 3 本は 0.61、[>#band2 -400][>#lab2 -300][>#d2][>#d2l][>#dia2 +500][♪tap -11dB +500][>#big2 +700]それ以外の 3 本は 0.15。[>#t7.r[1].tc +200][>#t7.r[2].tc +300][>#t7.r[3].tc +400][>#t7.r[4].tc +500][>#t7.r[5].tc +600][>#t7.r[6].tc +700][♪page -2dB +200]ただし、有酸素の 3 本は、記憶テストも[>#t7.mk[1]][♪pencil -3dB][>#t7.mk[2] +180][>#t7.mk[3] +360]単語リストに偏っていて、[|][>#conf][♪bell -4dB]運動とテスト、どちらの違いなのかは、切り分けられません。[silence:0.05s]

*** s08
@n: [silence:0.45s][>#bt8 -250][>#fr8 -50][>#sd +350][>#sl +950]言えないことも整理します。[>#lc1 .on -200][♪page -2dB -200][!#sd[4] to,{scale:1.35, fill:'#A9472F', duration:0.4} +400][!#sd[2] to,{scale:1.35, fill:'#A9472F', duration:0.4} +400][♪bell -5dB +400][>#db_d +600][>#db_b +600]効果が大きい D と B は、参加者がいちばん少ない {2 本|2 本です}。[>#trend][♪pencil -3dB][>#trend_l +500]小さい研究ほど効果が大きく出るこの傾向は、[|][>#drawer][>#gh +200][♪tap -13dB +200][>#drawer_l +400][>#gh_l +600]結果の出なかった研究が、公表されていない可能性を疑わせます。[=#lc1 -200][>#lc2 .on -200][♪page -2dB -200]D は 1 回だけの運動の直後の測定で、続けた効果とは別物。[=#lc2 -200][>#lc3 .on -200][♪page -2dB -200]6 本では、年齢や期間による違いも確かめられず、[|][=#lc3 -200][>#lc4 .on -200][♪page -2dB -200]最長でも 52 週。[||][!#lc4.d{m} marker]認知症の予防までは言えません。[silence:0.05s]

*** s09
@n: [silence:0.45s][>#bt9 -200]{まとめ|まとめます}。[>#cc1 -250][>#cc1.ck -100][♪check -100]{運動は記憶を小〜中程度良くする|運動は記憶を、小から中程度、良くする}。[>#cc2 -250][>#cc2.ck -100][♪check -100]{ただし差は大きく|ただし研究ごとの差は大きく}、はっきりしているのは[!#cc2.h{m} marker]{有酸素運動 × 単語の記憶|、有酸素運動と単語の記憶の組み合わせです}。[>#cc3 -250][>#cc3.ck -100][♪check -100]「運動すれば記憶が良くなる」と言い切るには、[|][!#cc3.h{m} marker][♪glock +1dB]大きくて長い研究が、まだ足りません。[silence:0.35s]

*** end
@n: [<#hdr][<#hdr_rule][<#prog][♪glock +2dB +450][silence:3.45s]
```

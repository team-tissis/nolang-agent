# concept · password-reuse (hf 全力版の全量の写し — パスワードの使い回しはなぜ危険か・新入社員向けの情報セキュリティ研修、7 場面の図解で漏えい → リスト型攻撃 → 被害 → 3 つの対策) — canvas 1920x1080

見せる作り: 明るい灰青の地 (淡い光だまり 2 つ + 点の地紋) に白い札を組む研修の図解・切替なしで前の要素が左へ抜ける場面替え・常設の帯 (題 + STEP 札 4 つを語で「今 → 済み ✓」)・場面の頭の STEP の小札と題・打鍵で出るパスワードと伏せ字・語で描く結びの線と矢印・稲妻と赤い縁の揺れ・表から一覧へ流れる札・打鍵で埋まるログインの札と判子・語で替わる題 (定義つき)・被害の札 3 枚を沈めて結論の札・番号の幽霊の枠を本物の札で置き換える 3 つの対策 (鍵・壁と盾・点の列・×)・締めの薄い 3 行を語で濃くして ✓・音の層 (BGM + 語に結んだ効果音 77)

```design.txt
#v2
# 学ぶ作り: 明るい灰青の地 (2 つの淡い光だまり + 点の地紋) に白い札を組む研修の図解。場面替えは切替なしで前の要素が左へ抜け (cut の out)、次の板が語で組み上がる
# 常設の帯 (sticky・左に題・右に 4 段の STEP 札) を語で「今の段 → 済み (✓)」に替え、各場面の頭に STEP の小札 + 題を置く
# 図は語ごとに 1 手ずつ: 打鍵で出る文字と点滅しない入力の棒・語で描く線と矢印・流れる札・判子・赤の縁の点灯・点の列の伸び・幽霊の枠を本物の札で置き換える 3 つの対策
# hf security password-reuse (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#F4F6F9
theme light
palette a=#2B6CB0 b=#2A9D8F ink=#1E2B3C sub=#56657A line=#DDE3EA field=#F7F9FC blue=#2B6CB0 blue_l=#E6EFFA blue_m=#BCD3EE teal=#2A9D8F teal_l=#E1F3F0 indigo=#4C5BD4 indigo_l=#ECEEFB red=#D94A38 red_d=#C23F2E red_t=#B83A2C red_l=#FCE9E6 amber=#E9A23B amber_t=#8A5A12 amber_l=#FDF1DC green=#2F9E6E green_t=#1F7A50 green_l=#E3F5EC chip=#D3DBE5 gray=#E9EEF4 tile=#DFE5EC arrow=#9AA7B8
font "太く読みやすい現代的な角ゴシック体、画面の解説向けの太字"
fonts m="等幅のプログラミング用の英数字の書体、すっきりした形"
art "清潔で現代的な企業の e ラーニング風のフラットなベクターイラスト、単純な幾何学的な形と柔らかく丸い形、最小限の平らな陰影、輪郭線なし、落ち着いた限られた色 (深い紺・落ち着いた青・柔らかい青緑・暖かい肌色・明るい灰・小さな暖かい珊瑚色)"
prompt_tail "文字・数字・ロゴ・透かしなし。主題 1 つだけを中央に置き、全体が見えるように周りに余白を取る"
sfx off
# hf の作り: 場面の頭の STEP の題と札の見出しは台詞より先に置く (spoiler)・図解だけの場面で写真を敷かない (text_only_cut)・札の中の注記は 1080 換算 18〜24 px の小さな字 (small_text)
# hf の作り: 鍵・✓・同じ・ログイン成功・偽の小札は札の角からはみ出して付く (child_overflow)・番号の幽霊の枠は番号だけの空の枠 (empty_board)・語ごとの音は 1 本に 77 回 (se_dense)・「使い回し」の札は問いの最後の 1 秒だけ (flash_text)
# hf の作り: まとめの札は沈めた被害の 3 枚の上に重ね、漏れた札は一覧の板の下へ流れ込む (covered_text)
lint off=spoiler,text_only_cut,small_text,child_overflow,empty_board,se_dense,flash_text,covered_text
run em { color: $blue }
run u { color: $red_t; marker: #E9A23B66,30% }
run sm { font-size: 28px; color: $sub }
run a { font-size: 26px; color: $sub }
run b { color: $green_t }
run s { font-size: 32px; color: $sub }
p { color: $ink }
img { main: none }
# 場面の要素は一斉に左へ抜ける (hf の leave: x -40 px・0.35 s)・頭は印で組む
cut { stagger: 0ms; out: {x:-40, opacity:0, duration:.35, ease:'power2.in'} }
sound pop = "柔らかく澄んだ短い UI のポップ音、アイコンが画面に出る時の小さな泡が弾ける音、乾いた控えめな音"
sound tick = "1 回だけのはっきりした柔らかいマウスのクリック音、乾いた UI の音"
sound ding = "柔らかく明るい通知のディン、1 音だけの穏やかな UI の音"
sound whoosh = "スライドの切り替えの柔らかく空気感のあるシュッという音、短くなめらか"
sound type = "ノートパソコンのキーボードを 8 回ほど素早く打つ短い打鍵音、近くで静か"
sound leak = "小さなファイルがこぼれ出るような短いデジタルのグリッチと散らばる電子音、控えめで耳に痛くない"
sound alert = "低く落ち着いた 2 音のデジタルの警告音、きつくない UI の警告"
sound unlock = "小さな鍵がカチッと開いて短い電子音が上がる、ロック解除の UI の音"
sound denied = "短く柔らかいくぐもったエラーのブザー、アクセス拒否の UI の音"
sound chime = "明るく穏やかな正解のチャイム、柔らかいベルの 2 音が上がる"
sound impact = "題が出る瞬間の柔らかく深い映画的な低いブーン、暖かく短い余韻"
sound stamp = "紙にゴム印を押す短く乾いたドンという音"
sound shimmer = "盾が作動するような柔らかく上がるきらめき音、明るく短い"
# 人物は透過の絵 2 体 (新入社員・攻撃者)・締めの社員は同じ人物の立ち姿を基準画像から派生
image employee = "[transparent]日本人の20代前半の新入社員、紺の簡素なスーツに白いシャツ、小さな現代的な机で開いたノートパソコンを前に座り、片手にスマートフォンを持って少し首をかしげて考え込むように見つめている、斜め横からの構図で机全体が見える"
image attacker = "[transparent]顔が影で完全に隠れた濃い炭色のフード付きパーカーの匿名の攻撃者、椅子に座ってノートパソコンを打っている、画面は青く柔らかく光る、象徴的で簡素、怖すぎない、斜めからの構図で全身とノートパソコンが見える"
bgm#music(fade: 800,2400) 落ち着いて明るく安心感のある企業研修向けの曲、柔らかいフェルトピアノの和音と軽く弾くシンセのアルペジオ、暖かいパッド、控えめなミュートのエレキギター、ブラシの軽い打楽器、96 BPM 前後の長調、声の邪魔をしない一定の流れ
# 字幕: 白い札 (95%・角丸 12・薄い縁と影)・墨色の太字・1 行の台詞を 1 枚 (2 文の行は [||] で繋ぎ [br] で 2 行)・語の強調は青
subtitle.hug(bottom: 38px; font-size: 38px; line-height: 1.5; letter-spacing: .03em; text-align: center; color: $ink; background: #FFFFFFF2; border-radius: 18px; padding: 12px 40px 14px 40px; border: 2px solid #1E2B3C12; box-shadow: 0px 8px 26px #1E2B3C1F; unit: sentence; lead: 50ms; tail: 200ms; hold: off; in: {y:8, opacity:0, duration:0.18, ease:'power2.out'}; out: {opacity:0, duration:0.1})

# 帯の STEP 札の状態: 今の段 (青の地・白字・白い番号) → 済み (淡い青の地・青字・番号の上に ✓ — ✓ は帯と一緒に透明で出しておき、
# 後の cut の語で to で灯す。後の cut で初めて出すと確定済みの前の cut を書き換える)
cue step_on(x) = [!#x .on][!#x.t recolor,#FFFFFF][!#x.n fill,#FFFFFF][!#x.n.v recolor,$blue]
cue step_done(x) = [!#x .done][!#x.t recolor,$blue][!#x.ck to,{opacity:1, duration:0.3}]

# 白い札 (角丸 16・薄い縁・柔らかい影)
def card = div(background: #FFFFFF; border-radius: 24px; border: 2px solid #1E2B3C0F; box-shadow: 0px 14px 34px #1E2B3C17; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
# 場面の頭: STEP の小札 + 題 (下から)
def board(s, t, c=$blue, cbg=$blue_l) = div(left: 96px; top: 140px; width: 1650px; height: 72px; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  p#s(left: 0px; cy: 50%; font-size: 22px; letter-spacing: .08em; color: {c}; background: {cbg}; border-radius: 148px; padding: 8px 18px; content: {s})
  p#t(left: 141px; cy: 50%; font-size: 50px; letter-spacing: .02em; out: {y:-30, opacity:0, duration:0.3, ease:'power2.in'}; content: {t})
# 問いの場面のサービスの札 (丸い地の icon + 名・右上に鍵の丸札)
def svc(t, i, ic, bg) = div(top: 556px; width: 290px; height: 236px; background: #FFFFFF; border-radius: 24px; border: 2px solid #1E2B3C0F; box-shadow: 0px 14px 34px #1E2B3C17; in: {y:34, scale:0.96, opacity:0, duration:0.6, ease:'power3.out'})
  icon#i(cx: 50%; top: 40px; font-size: 50px; name: {i}; color: {ic}; background: {bg}; padding: 22px)
  p#t(cx: 50%; cy: 176px; font-size: 30px; content: {t})
  icon#k(left: 248px; top: -14px; font-size: 28px; name: key; color: #FFFFFF; background: $amber; padding: 14px; in: {scale:0.6, opacity:0, duration:0.45, ease:'power3.out'})
# 攻撃の場面のログインの札 (icon + 名 + ID とパスワードの欄 2 つ・打鍵で埋まる)・同じ / 赤の縁 / ログイン成功 / 乗っ取りの判子
def panel(t, i, ic, bg) = div(width: 740px; height: 158px; background: #FFFFFF; border-radius: 24px; border: 2px solid #1E2B3C0F; box-shadow: 0px 14px 34px #1E2B3C17; in: {x:40, opacity:0, duration:0.6, ease:'power3.out'})
  icon#i(left: 26px; cy: 50%; font-size: 39px; name: {i}; color: {ic}; background: {bg}; padding: 18px)
  p#t(left: 124px; cy: 50%; font-size: 28px; content: {t})
  div#fi(left: 362px; top: 27px; width: 352px; height: 46px; border-radius: 10px; background: $field; border: 2px solid #D5DDE7)
    icon#u(left: 12px; cy: 50%; font-size: 22px; name: user; color: $sub)
    p#v(left: 45px; cy: 50%; font-size: 20px; font-family: m; in: {opacity:0, duration:0.01, stagger:{each:0.019}}) taro.s@example.com
  div#fp(left: 362px; top: 84px; width: 352px; height: 46px; border-radius: 10px; background: $field; border: 2px solid #D5DDE7)
    icon#u(left: 12px; cy: 50%; font-size: 22px; name: lock; color: $sub)
    p#v(left: 45px; cy: 50%; font-size: 20px; font-family: m; in: {opacity:0, duration:0.01, stagger:{each:0.037}}) taro0401
    p#same(left: 284px; top: -14px; font-size: 16px; color: #FFFFFF; background: $amber; border-radius: 148px; padding: 3px 10px 3px 28px; white-space: nowrap; in: {scale:0.6, opacity:0, duration:0.45, ease:'power3.out'}; out: {opacity:0, duration:0.2}) 同じ
      icon#k(left: 6px; cy: 50%; font-size: 18px; name: key; color: #FFFFFF)
  div#ring(inset: 0; border-radius: 24px; border: 4px solid $red; in: {opacity:0, duration:0.25})
  p#ok(left: 26px; top: 141px; font-size: 18px; color: #FFFFFF; background: $red_d; border-radius: 148px; padding: 4px 12px 4px 33px; in: {scale:0.7, opacity:0, duration:0.35, ease:'power3.out'}) ログイン成功
    icon#k(left: 8px; cy: 50%; font-size: 20px; name: lock-open; color: #FFFFFF)
  p#x(left: 528px; top: 74px; font-size: 34px; white-space: nowrap; letter-spacing: .06em; color: $red_t; background: #FFFFFFEB; border: 4px solid $red; border-radius: 14px; padding: 8px 18px; transform: rotate(-8deg); overlap: .fp; in: {scale:1.7, rotation:-6, opacity:0, duration:0.28, ease:'power4.out'}) 乗っ取り
# 被害の場面の札 (icon + 名 + 右の赤い札) と中の灰の段
def dcard(t, i, ic, bg, tag) = div(top: 272px; width: 540px; height: 480px; background: #FFFFFF; border-radius: 24px; border: 2px solid #1E2B3C0F; box-shadow: 0px 14px 34px #1E2B3C17; in: {y:36, opacity:0, duration:0.6, ease:'power3.out'})
  icon#i(left: 28px; top: 26px; font-size: 36px; name: {i}; color: {ic}; background: {bg}; padding: 15px)
  p#t(left: 112px; cy: 60px; font-size: 32px; content: {t})
  p#tag(right: 28px; cy: 60px; font-size: 22px; color: $red_t; background: $red_l; border-radius: 148px; padding: 8px 16px; in: {scale:0.7, opacity:0, duration:0.45, ease:'power3.out'}; content: {tag})
def dbody = div(left: 28px; top: 116px; width: 483px; height: 330px; border-radius: 18px; background: $field)
# 判子 (赤の縁・少し傾けて大きく → 小さく着地)
def stamp = p(color: $red_t; letter-spacing: .06em; background: #FFFFFFEB; border: 4px solid $red; border-radius: 14px; padding: 8px 18px; transform: rotate(-8deg); in: {scale:1.7, rotation:-6, opacity:0, duration:0.28, ease:'power4.out'})
# 対策の場面: 番号の幽霊の枠 (破線) と本物の札 (緑の番号 + 2 行の題 + 灰の段 + 緑の結び)
def ghost(n) = div(top: 262px; width: 540px; height: 412px; border-radius: 24px; background: #FFFFFF73; in: {y:24, scale:0.97, opacity:0, duration:0.6, ease:'power3.out'}; out: {opacity:0, duration:0.3})
  shape#d(inset: 0; path: rect,r=0.06; background: none; border: 3px solid #C9D3DF; dash: 6,5)
  div#c(cx: 50%; cy: 50%; width: 110px; height: 110px; border-radius: 148px; background: #E3E9F0)
    p#n(cx: 50%; cy: 50%; font-size: 60px; color: #5F6F84; content: {n})
def mcard(n, t, f) = div(top: 262px; width: 540px; height: 412px; background: #FFFFFF; border-radius: 24px; border: 2px solid #1E2B3C0F; box-shadow: 0px 14px 34px #1E2B3C17; in: {y:36, opacity:0, duration:0.6, ease:'power3.out'})
  div#c(left: 28px; top: 36px; width: 70px; height: 70px; border-radius: 148px; background: $green)
    p#n(cx: 50%; cy: 50%; font-size: 38px; color: #FFFFFF; content: {n})
  p#t(left: 117px; cy: 72px; font-size: 34px; line-height: 1.3; content: {t})
  div#foot(left: 28px; top: 350px; width: 483px; height: 36px; in: {y:10, opacity:0, duration:0.4, ease:'power3.out'})
    icon#i(left: 0px; cy: 50%; font-size: 30px; name: check-circle; color: $green_t)
    p#t(left: 40px; cy: 50%; font-size: 26px; color: $green_t; content: {f})
def vis = div(left: 28px; top: 134px; width: 483px; height: 200px; border-radius: 18px; background: $field)

# 全編の地: 左上と右下の淡い光だまり + 点の地紋 (最背面)
div#bg_glow1(inset: 0; background: radial(#E3EDF9,#E3EDF900@32%,8%,4%); z-index: back; border-radius: 24px; in: none; out: none)
div#bg_glow2(inset: 0; background: radial(#E0F1EE,#E0F1EE00@32%,96%,100%); z-index: back; border-radius: 24px; in: none; out: none)
div#bg_dots(inset: 0; pattern: dots,24,#1E2B3C11; z-index: back; border-radius: 24px; in: none; out: none)

# hook — 問い: 机の新入社員 → いつものパスワードを打って伏せ字に → 3 つのサービスの札 → 線で結んで鍵 → 「危険」で線と鍵が赤く・札に「使い回し」
section#hook(out: {scale:0.97, opacity:0, duration:0.4, ease:'power2.in'})
# 絵の枠は hf より大きく取る (生成の絵は余白が広い — 見える人物の大きさを hf に合わせた)
img#hk_emp(left: 38px; top: 76px; width: 662px; height: 897px; content: @employee; object-fit: contain; delay: 150ms; in: {x:-40, opacity:0, duration:0.9, ease:'power3.out'})
shape#hk_l1(path: "M1260 374 C1260 461 935 470 935 552"; background: none; border: 4px solid $amber; in: draw {duration: 0.6})
shape#hk_l2(path: "M1260 374 L1260 552"; background: none; border: 4px solid $amber; in: draw {duration: 0.6})
shape#hk_l3(path: "M1260 374 C1260 461 1586 470 1586 552"; background: none; border: 4px solid $amber; in: draw {duration: 0.6})
card#hk_pw(left: 910px; top: 196px; width: 700px; height: 176px; in: {y:24, opacity:0, duration:0.6, ease:'power3.out'})
  icon#ki(left: 30px; top: 24px; font-size: 22px; name: key; color: $amber; background: $amber_l; padding: 10px)
  p#label(left: 87px; cy: 46px; font-size: 26px; color: $sub) いつものパスワード
  div#field(left: 30px; top: 84px; width: 640px; height: 70px; border-radius: 14px; background: $field; border: 2px solid #D5DDE7)
    # 打鍵: 1 字ずつ出る平文と、一緒に右へ進む入力の棒 → 打ち終えると伏せ字に替わる
    p#plain(left: 24px; cy: 50%; font-size: 38px; font-family: m; letter-spacing: .12em; in: {opacity:0, duration:0.01, stagger:{each:0.11}}; out: {opacity:0, duration:0.2}) taro0401
    p#mask(left: 24px; cy: 50%; font-size: 30px; letter-spacing: .2em; in: {opacity:0, duration:0.2}) ●●●●●●●●
    div#caret(left: 24px; cy: 50%; width: 3px; height: 36px; background: $blue; in: none; out: {opacity:0, duration:0.01})
  p#warn(left: 518px; top: 22px; font-size: 22px; color: $red_t; background: $red_l; border-radius: 148px; padding: 9px 16px 9px 45px; in: {scale:0.8, opacity:0, duration:0.45, ease:'power3.out'}) 使い回し
    icon#i(left: 14px; cy: 50%; font-size: 26px; name: warning; color: $red_t)
#hk_pw.bad(border: 3px solid #D94A38E6; box-shadow: 0px 0px 0px 4px #D94A3840)
svc#hk_s(left: "791;1115;1440"; height: 236px; t: "通販サイト;SNS;会社のアカウント"; i: "shopping-cart;chat-circle;buildings"; ic: "$blue;$teal;$indigo"; bg: "$blue_l;$teal_l;$indigo_l") ×3

# title — 声のない題: 2 重の輪を描き、研修の札・2 行の題 (「使い回し」は赤字 + 琥珀の下帯)・流れの 4 札が順に
section#title(out: {scale:1.03, opacity:0, duration:0.4, ease:'power2.in'})
shape#tt_r1(left: 630px; top: 170px; width: 660px; height: 660px; border-radius: 50%; background: none; border: 3px solid $blue_m; in: draw {duration: 1.2})
shape#tt_r2(left: 698px; top: 237px; width: 525px; height: 525px; border-radius: 50%; background: none; border: 3px solid $blue_m; in: draw {duration: 1.2})
p#tt_chip(cx: 960px; cy: 279px; font-size: 28px; letter-spacing: .06em; color: #FFFFFF; background: $blue; border-radius: 148px; padding: 10px 26px; in: {y:20, opacity:0, duration:0.5, ease:'power3.out'}) 新入社員向け 情報セキュリティ研修
p#tt_l1(cx: 960px; cy: 411px; font-size: 96px; line-height: 1.28; letter-spacing: .03em; in: {y:44, opacity:0, duration:0.7, ease:'power3.out'}) パスワードの{u}使い回し{/}は、
p#tt_l2(cx: 960px; cy: 534px; font-size: 96px; line-height: 1.28; letter-spacing: .03em; in: {y:44, opacity:0, duration:0.7, ease:'power3.out'}) なぜ危険か
group#tt_flow(in: {y:14, opacity:0, duration:0.4, ease:'power3.out', stagger:{each:0.07}})
  p#f1(left: 632px; cy: 657px; font-size: 26px; color: $sub; background: #FFFFFF; border: 2px solid $chip; border-radius: 148px; padding: 8px 20px) 漏えい
  icon#a1(left: 764px; cy: 657px; font-size: 26px; name: arrow-right; color: $arrow)
  p#f2(left: 802px; cy: 657px; font-size: 26px; color: $sub; background: #FFFFFF; border: 2px solid $chip; border-radius: 148px; padding: 8px 20px) リスト型攻撃
  icon#a2(left: 1011px; cy: 657px; font-size: 26px; name: arrow-right; color: $arrow)
  p#f3(left: 1050px; cy: 657px; font-size: 26px; color: $sub; background: #FFFFFF; border: 2px solid $chip; border-radius: 148px; padding: 8px 20px) 被害
  icon#a3(left: 1156px; cy: 657px; font-size: 26px; name: arrow-right; color: $arrow)
  p#f4(left: 1196px; cy: 657px; font-size: 26px; color: $sub; background: #FFFFFF; border: 2px solid $chip; border-radius: 148px; padding: 8px 20px) 対策

# leak — STEP 1: 常設の帯が上から → 学生時代のサービスの会員の表 →「あなた」の行 →「漏えい」で稲妻が刺さり赤く揺れ、ID とパスワードが右の漏えいの一覧へ流れる → POINT の札
section#leak
# 常設の帯 (sticky・締めまで): 左に盾の丸札 + 題 + 縦線 + 副題・右に STEP 札 4 つ (間に短い線)
div#hdr.sticky(left: 80px; top: 36px; width: 1761px; height: 60px; z-index: front; in: {y:-24, opacity:0, duration:0.6, ease:'power3.out'})
  icon#logo(left: 0px; cy: 50%; font-size: 26px; name: shield-check; color: #FFFFFF; background: $blue; border-radius: 14px; padding: 10px)
  p#brand(left: 62px; cy: 50%; font-size: 24px; letter-spacing: .06em) 情報セキュリティ研修
  div#sep(left: 310px; cy: 50%; width: 2px; height: 26px; background: $line)
  p#topic(left: 328px; cy: 50%; font-size: 24px; color: $sub) パスワードの使い回し
  div#ln(left: "1200;1451;1611"; cy: 50%; width: 22px; height: 2px; background: $chip) ×3
  div#st(left: "1050;1233;1484;1644"; cy: 50%; width: "140;207;117;117"; height: 50px; border-radius: 148px; background: #FFFFFF; border: 2px solid $chip) ×4
    div#n(left: 8px; cy: 50%; width: 34px; height: 34px; border-radius: 148px; background: $gray)
      p#v(cx: 50%; cy: 50%; font-size: 20px; color: $sub) 1;2;3;4
    p#t(left: 52px; cy: 50%; font-size: 22px; color: $sub) 漏えい;リスト型攻撃;被害;対策
    icon#ck(left: 8px; cy: 50%; font-size: 20px; name: check; weight: bold; color: #FFFFFF; background: $blue; padding: 8px; overlap: .n,.n.v; opacity: 0)
#hdr.st.on(background: $blue; border: 2px solid $blue)
#hdr.st.done(background: $blue_l; border: 2px solid $blue_m)
board#lk_head(s: "STEP 1"; t: "IDとパスワードの漏えい")
# 会員の表 (窓の帯 + 地球の丸札の題 + 3 行)
card#lk_site(left: 110px; top: 280px; width: 640px; height: 460px; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  div#bar(left: 0px; top: 0px; width: 640px; height: 62px; border-radius: 24px 24px 0px 0px; background: #EEF2F7)
    div#dot(left: "23;47;71"; cy: 50%; width: 14px; height: 14px; border-radius: 148px; background: #CFD8E3) ×3
    p#url(left: 106px; cy: 50%; width: 512px; font-size: 21px; color: $sub; background: #FFFFFF; border-radius: 10px; padding: 6px 16px) 学生時代に登録したサービス
  icon#g(left: 30px; top: 86px; font-size: 36px; name: globe; color: $blue; background: $blue_l; padding: 16px)
  p#h(left: 118px; top: 88px; font-size: 28px) 会員データベース
  p#hs(left: 118px; top: 128px; font-size: 20px; color: $sub) 登録ユーザーのID・パスワード
  div#r(left: 30px; top: "174;248;321"; width: 580px; height: 62px; border-radius: 14px; background: $field; border: 2px solid #F7F9FC00) ×3
    icon#u(left: 18px; cy: 50%; font-size: 26px; name: user; color: $sub)
    p#e(left: 58px; cy: 50%; font-size: 21px; font-family: m) taro.s@example.com;hanako.k@example.com;yamada88@example.com
    p#pw(right: 18px; cy: 50%; font-size: 21px; font-family: m; letter-spacing: .12em; color: $sub) ●●●●●●●●
  p#you(left: 18px; top: 160px; font-size: 18px; color: $amber_t; background: $amber_l; border-radius: 148px; padding: 4px 12px; in: {scale:0.7, opacity:0, duration:0.45, ease:'power3.out'}) あなた
  div#flash(inset: 0; border-radius: 24px; border: 4px solid $red; in: {opacity:0, duration:0.15})
#lk_site.r.you(background: $amber_l; border: 2px solid $amber)
icon#lk_zap(left: 70px; top: 238px; font-size: 48px; name: lightning; color: #FFFFFF; background: $red; padding: 22px; box-shadow: 0px 8px 18px #D94A3859; in: {scale:0.4, opacity:0, duration:0.35, ease:'power3.out'})
p#lk_badge(left: 632px; top: 256px; overlap: lk_site; font-size: 26px; color: #FFFFFF; background: $red_d; border-radius: 148px; padding: 10px 20px 10px 50px; in: {scale:0.7, opacity:0, duration:0.45, ease:'power3.out'}) 漏えい
  icon#i(left: 14px; cy: 50%; font-size: 28px; name: warning; color: #FFFFFF)
shape#lk_arrow(path: "M773 510 L989 510 M954 479 L990 510 L954 542"; background: none; border: 6px solid $red; in: draw {duration: 0.5})
# 漏れた ID とパスワードの札が表から飛び出し、右の一覧へ流れて消える
p#lk_fly(left: 770px; overlap: lk_list; top: "464;537;611"; font-size: 20px; font-family: m; color: $red_t; background: $red_l; border-radius: 10px; padding: 10px 14px; in: {x:-130, scale:0.9, opacity:0, duration:0.3, ease:'power2.out'}) ×3 taro.s@example.com / taro0401;hanako.k@example.com / hana1234;yamada88@example.com / yamada88
# 漏えいの一覧 (赤の題の帯 + 4 行 + 「ほかにも」)・自分の行は琥珀
card#lk_list(left: 1010px; top: 280px; width: 800px; height: 460px; in: {x:30, opacity:0, duration:0.5, ease:'power3.out'})
  div#hd(left: 0px; top: 0px; width: 800px; height: 76px; border-radius: 24px 24px 0px 0px; background: $red_l)
    icon#i(left: 28px; cy: 50%; font-size: 34px; name: warning; color: $red_t)
    p#t(left: 76px; cy: 50%; font-size: 28px; color: $red_t) 漏えいしたID・パスワード
  div#r(left: 28px; top: "92;156;221;284"; width: 742px; height: 54px; border-radius: 12px; background: "$amber_l;$field;$field;$field"; border: "2px solid $amber;2px solid #F7F9FC00;2px solid #F7F9FC00;2px solid #F7F9FC00"; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) ×4
    p#e(left: 18px; cy: 50%; font-size: 22px; font-family: m) taro.s@example.com;hanako.k@example.com;yamada88@example.com;s.suzuki@example.com
    p#pw(right: 18px; cy: 50%; font-size: 22px; font-family: m; color: $red_t) taro0401;hana1234;yamada88;suzu0715
  p#more(cx: 50%; cy: 375px; font-size: 22px; color: $sub; in: {y:14, opacity:0, duration:0.4, ease:'power3.out'}) ほかにも大量のID・パスワード
card#lk_note(left: 1010px; top: 762px; width: 800px; height: 96px; in: {y:20, opacity:0, duration:0.6, ease:'power3.out'})
  p#c(left: 28px; cy: 50%; font-size: 20px; letter-spacing: .08em; color: #FFFFFF; background: $blue; border-radius: 148px; padding: 6px 14px) POINT
  p#t(left: 142px; cy: 50%; font-size: 30px) {em}自分のせいでなくても{/}、漏えいは起きる

# attack — STEP 2: 攻撃者 → 漏えいの一覧と矢印 → ログインの札 3 枚 →「次々に」で矢印と打鍵 → 題が「リスト型攻撃」に替わり定義 → 同じ → 赤の縁とログイン成功 → 乗っ取りの判子
section#attack
board#at_head(s: "STEP 2"; t: "漏れたパスワードの使われ方")
p#at_t2(left: 237px; cy: 176px; font-size: 50px; letter-spacing: .02em; color: $red_t; in: {y:30, opacity:0, duration:0.5, ease:'power3.out'}) リスト型攻撃 {sm}（パスワードリスト攻撃）{/}
p#at_def(left: 96px; top: 216px; font-size: 26px; color: $sub; in: {y:10, opacity:0, duration:0.5, ease:'power3.out'}) 漏れたIDとパスワードの組み合わせを、別のサービスで次々に試す攻撃
card#at_list(left: 96px; top: 330px; width: 400px; height: 330px; in: {x:-40, opacity:0, duration:0.6, ease:'power3.out'})
  div#hd(left: 0px; top: 0px; width: 400px; height: 64px; border-radius: 24px 24px 0px 0px; background: $red_l)
    icon#i(left: 20px; cy: 50%; font-size: 28px; name: warning; color: $red_t)
    p#t(left: 58px; cy: 50%; font-size: 24px; color: $red_t) 漏えいしたリスト
  div#r(left: 18px; top: "78;134;188;243"; width: 364px; height: 46px; border-radius: 12px; background: "$amber_l;$field;$field;$field"; border: "2px solid $amber;2px solid #F7F9FC00;2px solid #F7F9FC00;2px solid #F7F9FC00") ×4
    p#e(left: 14px; cy: 50%; font-size: 18px; font-family: m) taro.s@example.com;hanako.k@example.com;yamada88@example.com;s.suzuki@example.com
    p#pw(right: 14px; cy: 50%; font-size: 18px; font-family: m; color: $red_t) taro0401;hana1234;yamada88;suzu0715
img#at_att(left: 621px; top: 300px; width: 225px; height: 330px; content: @attacker; object-fit: contain; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  p#l(cx: 50%; cy: 363px; font-size: 30px) 攻撃者
  p#s(cx: 50%; cy: 411px; font-size: 20px; color: $red_t; background: $red_l; border-radius: 148px; padding: 6px 14px; white-space: nowrap) 自動で次々にログインを試す
shape#at_a0(path: "M506 495 L575 495 M551 473 L576 495 L551 518"; background: none; border: 4px solid $red; in: draw {duration: 0.4})
shape#at_a1(path: "M890 470 C975 470 975 351 1052 351 M1031 333 L1055 351 L1031 369"; background: none; border: 4px solid $red; in: draw {duration: 0.45})
shape#at_a2(path: "M890 500 L1052 536 M1028 522 L1055 536 L1032 558"; background: none; border: 4px solid $red; in: draw {duration: 0.45})
shape#at_a3(path: "M890 530 C975 530 975 719 1052 719 M1031 701 L1055 719 L1031 737"; background: none; border: 4px solid $red; in: draw {duration: 0.45})
panel#at_p(left: 1070px; top: "272;456;641"; t: "通販サイト;SNS;会社のクラウド"; i: "shopping-cart;chat-circle;cloud"; ic: "$blue;$teal;$indigo"; bg: "$blue_l;$teal_l;$indigo_l") ×3

# damage — STEP 3: 被害の札 3 枚を語ごとに (注文の判子・偽の札と友人への手紙・赤い縁と目) →「たった一つ」で 3 枚を沈め、鍵 → 矢印 → 会社の札
section#damage
board#dm_head(s: "STEP 3"; t: "乗っ取られると、どうなる？")
dcard#dm_c1(left: 96px; t: "通販サイト"; i: shopping-cart; ic: $blue; bg: $blue_l; tag: "勝手に注文")
  dbody#b
    p#h(left: 24px; top: 22px; font-size: 24px) ご注文を承りました
    p#s(left: 24px; top: 60px; font-size: 18px; color: $sub) 注文者：あなたのアカウント
    div#r1(left: 24px; top: 99px; width: 435px; height: 64px; border-radius: 12px; background: #FFFFFF)
      icon#i(left: 16px; cy: 50%; font-size: 28px; name: package; color: $sub)
      p#t(left: 58px; cy: 50%; font-size: 22px) 商品 3点
      icon#p(left: "330;362;393"; cy: 50%; font-size: 26px; name: package; color: $indigo) ×3
    div#r2(left: 24px; top: 177px; width: 435px; height: 64px; border-radius: 12px; background: #FFFFFF; border: 2px solid #FFFFFF00)
      icon#i(left: 16px; cy: 50%; font-size: 28px; name: credit-card; color: $sub)
      p#t(left: 58px; cy: 50%; font-size: 22px) 登録済みのカードで支払い
    stamp#stamp(left: 174px; top: 226px; font-size: 28px) 身に覚えのない注文
#dm_c1.b.r2.hit(background: $red_l; border: 2px solid $red)
dcard#dm_c2(left: 690px; t: "SNS"; i: chat-circle; ic: $teal; bg: $teal_l; tag: "なりすまし")
  dbody#b
    div#post(left: 24px; top: 22px; width: 435px; height: 160px; border-radius: 14px; background: #FFFFFF)
      icon#av(left: 18px; top: 16px; font-size: 28px; name: user; color: $teal; background: $teal_l; padding: 10px)
      p#fake(left: 4px; top: 4px; font-size: 16px; color: #FFFFFF; background: $red_d; border-radius: 148px; padding: 3px 9px; in: {scale:0.5, opacity:0, duration:0.45, ease:'power3.out'}) 偽
      p#n(left: 80px; top: 16px; font-size: 22px) あなた
      p#tm(left: 80px; top: 46px; font-size: 16px; color: $sub) たった今
      p#msg(left: 18px; top: 81px; font-size: 22px) このリンク、見てみて！
      p#link(left: 18px; top: 118px; font-size: 18px; font-family: m; color: $blue) https://example.com/xxxx
    icon#fr(left: "128;191;254"; cy: 225px; font-size: 26px; name: user-circle; color: $sub; background: $gray; padding: 12px) ×3
    p#lbl(left: 24px; cy: 225px; font-size: 18px; color: $sub) 友人へ送信
    icon#m(left: "161;224;287"; top: 190px; font-size: 15px; name: envelope; color: #FFFFFF; background: $red; padding: 6px; in: {scale:0.3, opacity:0, duration:0.45, ease:'power3.out'}) ×3
dcard#dm_c3(left: 1284px; t: "会社のクラウド"; i: cloud; ic: $indigo; bg: $indigo_l; tag: "侵入")
  dbody#b
    icon#bd(left: 24px; top: 22px; font-size: 33px; name: buildings; color: $indigo; background: $indigo_l; padding: 15px)
    p#n(left: 104px; cy: 54px; font-size: 22px) 社内の共有フォルダ
    div#f(left: 24px; top: "101;185"; width: 435px; height: 70px; border-radius: 12px; background: #FFFFFF; border: 2px solid #FFFFFF00) ×2
      icon#i(left: 16px; cy: 50%; font-size: 32px; name: "folder;folder-lock"; color: $indigo)
      p#t(left: 62px; cy: 50%; font-size: 24px) 社内の資料;お客さまの情報
      icon#e(left: 378px; cy: 50%; font-size: 22px; name: eye; color: #FFFFFF; background: $red; padding: 9px; in: {scale:0.5, opacity:0, duration:0.45, ease:'power3.out'})
#dm_c3.b.f.hit(border: 2px solid $red)
# まとめの札: たった一つのパスワード → 会社全体のリスク (矢印は札の上に描く)
card#dm_sum(left: 260px; top: 318px; width: 1400px; height: 380px; overlap: dm_c1,dm_c2,dm_c3; in: {y:30, opacity:0, duration:0.5, ease:'power3.out'})
  div#a(left: 90px; top: 66px; width: 420px; height: 246px; in: {x:-30, opacity:0, duration:0.5, ease:'power3.out'})
    icon#i(cx: 50%; top: 0px; font-size: 88px; name: key; color: $amber_t; background: $amber_l; padding: 40px)
    p#t(cx: 50%; cy: 218px; font-size: 40px; white-space: nowrap) たった一つのパスワード
  div#b(left: 891px; top: 66px; width: 420px; height: 246px; in: {scale:0.85, opacity:0, duration:0.45, ease:'power3.out'})
    icon#i(cx: 50%; top: 0px; font-size: 88px; name: buildings; color: $red_t; background: $red_l; padding: 40px)
    p#t(cx: 50%; cy: 218px; font-size: 40px; color: $red_t) 会社全体のリスク
shape#dm_arrow(path: "M821 507 L1092 507 M1058 479 L1094 507 L1058 536"; background: none; border: 8px solid $red; in: draw {duration: 0.45})

# measures — STEP 4: 番号の幽霊の枠 3 つ → 「1 つ目」ごとに本物の札が置き換わり、札の中の図を語で動かす → 下の帯「覚えずに → 管理ツール」
section#measures
board#ms_head(s: "STEP 4"; t: "今日からできる 3つの対策"; c: $green; cbg: $green_l)
ghost#ms_g(left: "96;690;1284"; n: "1;2;3") ×3
# 1: サービスごとの札に別々の鍵 → 1 つが漏れて赤く揺れ、緑の壁と盾が止め、他の 2 つに ✓
mcard#ms_c1(left: 96px; n: 1; t: "サービスごとに[br]別のパスワード"; f: "被害はそこで止まる")
  vis#v
    div#t(left: "26;206;347"; top: 38px; width: 122px; height: 122px; border-radius: 20px; background: #FFFFFF; border: 2px solid $tile) ×3
      icon#i(cx: 50%; cy: 50%; font-size: 52px; name: "shopping-cart;chat-circle;buildings"; color: $sub)
      icon#k(left: 88px; top: 88px; font-size: 24px; name: key; color: #FFFFFF; background: "$blue;$teal;$indigo"; padding: 10px; in: {scale:0.6, opacity:0, duration:0.45, ease:'power3.out'})
      icon#ok(left: 98px; top: -10px; font-size: 20px; name: check; weight: bold; color: #FFFFFF; background: $green; padding: 8px; opacity: "0;1;1"; in: {scale:0.6, opacity:0, duration:0.45, ease:'power3.out'})
    p#leak(left: 22px; top: 8px; font-size: 16px; color: #FFFFFF; background: $red_d; border-radius: 148px; padding: 3px 10px; in: {scale:0.6, opacity:0, duration:0.45, ease:'power3.out'}) 漏えい
    div#wall(left: 164px; top: 26px; width: 20px; height: 150px; border-radius: 10px; background: $green; in: {scaleY:0, opacity:0, duration:0.4, ease:'power3.out', pivot:'bottom'})
    icon#wi(left: 147px; top: 72px; font-size: 28px; name: shield-check; color: #FFFFFF; background: $green; padding: 12px; in: {scale:0.5, opacity:0, duration:0.45, ease:'power3.out'})
#ms_c1.v.t.bad(background: $red_l; border: 2px solid $red)
# 2: 8 個の赤い点に灰の 6 個が足され 12 文字の印を越え、全部が緑に →「8文字：短い」が「複雑さ より 長さ」に替わる
mcard#ms_c2(left: 690px; n: 2; t: "12文字以上の[br]長さにする"; f: "複雑さより、長さが大切")
  vis#v
    p#ml(left: 356px; top: 14px; font-size: 22px; in: {y:8, opacity:0, duration:0.35, ease:'power3.out'}) 12文字
    div#mk(left: 388px; top: 50px; width: 4px; height: 82px; border-radius: 3px; background: $ink; in: {scale:0.4, opacity:0, duration:0.45, ease:'power3.out'})
    div#dots(left: 26px; top: 78px; width: 435px; height: 26px; display: flex; gap: 6px)
      div#d(flex: 1; border-radius: 148px; background: "$red;$red;$red;$red;$red;$red;$red;$red;#D5DDE7;#D5DDE7;#D5DDE7;#D5DDE7;#D5DDE7;#D5DDE7"; in: none) ×14
    p#len(left: 26px; top: 128px; font-size: 22px; color: $red_t; out: {opacity:0, duration:0.25}) 8文字：短い
    p#cmp(left: 26px; top: 114px; font-size: 46px; color: $green_t; in: {y:10, opacity:0, duration:0.45, ease:'power3.out'}) {a}複雑さ　より{/}　{b}長さ{/}
# 3: パスワード → スマホで確認・攻撃者の顔が間に入り込み × で止まる
mcard#ms_c3(left: 1284px; n: 3; t: "二段階認証を[br]有効にする"; f: "パスワードだけでは入れない")
  vis#v
    div#f1(left: 22px; top: 50px; width: 170px; height: 96px; border-radius: 16px; background: #FFFFFF; border: 2px solid $tile)
      icon#i(left: 14px; cy: 50%; font-size: 30px; name: key; color: $amber_t)
      p#t(left: 52px; cy: 50%; font-size: 21px) パスワード
    icon#ar(left: 198px; top: 86px; font-size: 26px; name: arrow-right; color: $arrow)
    div#f2(left: 262px; top: 50px; width: 206px; height: 96px; border-radius: 16px; background: #FFFFFF; border: 2px solid $tile)
      icon#i(left: 14px; cy: 50%; font-size: 30px; name: device-mobile; color: $blue)
      p#t(left: 52px; cy: 50%; font-size: 21px) スマホで確認
    img#att(left: 70px; top: 150px; width: 64px; height: 64px; border-radius: 148px; border: 3px solid $red; background: #FFFFFF; content: @attacker; object-fit: cover; object-position: 50% 15%; zoom: 230%; in: {opacity:0, duration:0.3})
    icon#x(left: 338px; top: 22px; font-size: 32px; name: x; weight: bold; color: #FFFFFF; background: $red; padding: 12px; in: {scale:0.4, opacity:0, duration:0.45, ease:'power3.out'})
    p#blk(left: 300px; top: 156px; font-size: 18px; color: $red_t; background: $red_l; border-radius: 148px; padding: 4px 12px; in: {scale:0.7, opacity:0, duration:0.45, ease:'power3.out'}) ここで止まる
#ms_c3.v.f2.on(background: $blue_l; border: 2px solid $blue)
#ms_c3.v.f2.ng(border: 2px solid $red)
# 下の帯: 覚えずに → 青い錠の丸札 + 管理ツール・右に色違いの鍵 4 つ
card#ms_strip(left: 96px; top: 700px; width: 1728px; height: 150px)
  icon#ki(left: 44px; cy: 50%; font-size: 38px; name: key; color: $amber_t; background: $amber_l; padding: 18px)
  p#a(left: 134px; cy: 50%; font-size: 32px; color: $sub) パスワードは覚えずに
  icon#ar(left: 477px; cy: 50%; font-size: 34px; name: arrow-right; color: $arrow)
  icon#vault(left: 567px; cy: 50%; font-size: 50px; name: lock; color: #FFFFFF; background: $blue; padding: 22px; in: {x:20, opacity:0, duration:0.5, ease:'power3.out'})
  icon#kf(left: "1385;1464;1545;1625"; top: 40px; font-size: 26px; name: key; color: #FFFFFF; background: "$blue;$teal;$indigo;$amber"; padding: 12px; in: {x:40, scale:0.6, opacity:0, duration:0.4, ease:'power3.out'}) ×4
  p#b(left: 682px; cy: 50%; font-size: 40px; color: $blue; in: {x:20, opacity:0, duration:0.5, ease:'power3.out'}) パスワード管理ツールに任せる
  p#kl(left: 1384px; top: 104px; font-size: 18px; color: $sub; in: {opacity:0, duration:0.4}) サービスごとの長いパスワードも

# outro — 締め: 立った社員 + 「今日から、この3つ」の薄い 3 行を語ごとに濃くして ✓ を緑に → 青い帯の結び → 地の色へ溶ける
section#outro
img#ot_emp(left: 330px; top: 170px; width: 238px; height: 700px; object-fit: contain; in: {x:-40, opacity:0, duration:0.8, ease:'power3.out'}) [transparent][ref:@employee]同じ若い社員 (同じ顔・髪・紺のスーツ・白いシャツ) が背筋を伸ばして立ち、自信のある笑顔で片手にスマートフォンを持つ、安心したくつろいだ姿勢、全身、机なし
card#ot_card(left: 740px; top: 214px; width: 1040px; height: 440px; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  p#h(left: 48px; top: 34px; font-size: 30px; color: $sub) 今日から、この3つ
  div#i(left: 48px; top: "102;212;321"; width: 944px; height: 84px; opacity: 0.18) ×3
    icon#ck(left: 0px; cy: 50%; font-size: 42px; name: check; weight: bold; color: #FFFFFF; background: #D5DDE7; padding: 15px)
    p#t(left: 96px; cy: 50%; font-size: 52px) 使い回さない;長くする {s}（12文字以上）{/};二段階認証をオンに
div#ot_banner(left: 740px; top: 690px; width: 1040px; height: 130px; border-radius: 24px; background: $blue; box-shadow: 0px 16px 36px #2B6CB047; in: {y:30, opacity:0, duration:0.6, ease:'power3.out'})
  icon#i(left: 108px; cy: 50%; font-size: 56px; name: shield-check; color: #FFFFFF)
  p#t(left: 188px; cy: 50%; font-size: 46px; letter-spacing: .03em; color: #FFFFFF) 今日から、自分のアカウントを守ろう
```

```timeline.txt
#v2
cast n = "明瞭で落ち着いた30〜40代の女性のナレーター、企業研修らしく信頼感のある一定のテンポで丁寧に話す"
silence head=0ms tail=300ms

*** hook
[>#subtitle]
bgm music
@n: [silence:600ms][♪pop -10dB -350ms]あなたが学生時代から使っている、[>#hk_pw -300ms][♪pop -9dB -250ms][>#hk_pw.field.plain +50ms][>#hk_pw.field.caret +50ms][!#hk_pw.field.caret to,{x:214, duration:0.9, ease:'none'} +50ms][♪type -5dB +50ms][br]お気に入りの[<#hk_pw.field.caret +633ms][<#hk_pw.field.plain +683ms][>#hk_pw.field.mask +683ms][♪tick -4dB +683ms]パスワード。
@: [>#hk_s[1]][♪pop -7dB]通販サイトや[>#hk_s[2]][♪pop -7dB]SNS、[>#hk_s[3]][♪pop -7dB]会社のアカウントにも、[>#hk_l1][>#hk_l2 +120ms][>#hk_l3 +240ms][♪whoosh -10dB][>#hk_s[1].k +500ms][>#hk_s[2].k +630ms][>#hk_s[3].k +760ms][♪tick -8dB +500ms][♪tick -8dB +630ms][♪tick -8dB +760ms][br]同じものを使っていませんか？
@: 便利ですが、実はとても[!#hk_l1 recolor,$red {duration: .35}][!#hk_l2 recolor,$red {duration: .35}][!#hk_l3 recolor,$red {duration: .35}][!#hk_s[1].k recolor,$red][!#hk_s[2].k recolor,$red][!#hk_s[3].k recolor,$red][!#hk_pw .bad][>#hk_pw.warn +50ms][♪alert -9dB]危険です。

*** title
se whoosh -8dB
@n: [>#tt_r1 +100ms][>#tt_r2 +250ms][>#tt_chip +200ms][>#tt_l1 +300ms][>#tt_l2 +460ms][!#tt_l1{u} marker +850ms][>#tt_flow +1000ms][♪impact -2.5dB +250ms][silence:2.3s]

*** leak
@n: [silence:600ms][>#hdr -300ms][step_on #hdr.st[1] -200ms][>#lk_head -250ms][>#lk_site +50ms][♪pop -8dB +50ms]たとえば、学生時代に登録したサービスから、[!#lk_site.r[1] .you][>#lk_site.you +100ms][♪tick -4dB][br]IDとパスワードが[>#lk_zap -250ms][!#lk_zap to,{x:36, y:40, duration:0.25, ease:'power2.in'} -50ms][>#lk_site.flash +150ms][!#lk_site shake {x: 8, duration: .38} +150ms][>#lk_badge +250ms][>#lk_arrow +300ms][>#lk_fly[1] +350ms][>#lk_fly[2] +470ms][>#lk_fly[3] +590ms][!#lk_fly[1] to,{x:270, y:-86, opacity:0, duration:0.55, ease:'power2.in'} +650ms][!#lk_fly[2] to,{x:270, y:-86, opacity:0, duration:0.55, ease:'power2.in'} +770ms][!#lk_fly[3] to,{x:270, y:-86, opacity:0, duration:0.55, ease:'power2.in'} +890ms][>#lk_list +300ms][>#lk_list.r[*] {stagger:{each:0.12}} +700ms][>#lk_list.more +1180ms][♪alert -9dB -200ms][♪leak -6dB]漏えいしたとします。
@: [>#lk_note +100ms][♪ding -9dB +100ms]あなたに落ち度がなくても、[!#lk_note glow,#2B6CB040 {blur: 0, spread: 3}]漏えいは起きるのです。

*** attack
se whoosh -9dB +50ms
@n: [silence:700ms][step_done #hdr.st[1] -400ms][step_on #hdr.st[2] -400ms][>#at_head -400ms][>#at_att][♪pop -8dB]攻撃者は、[>#at_list][♪tick -8dB][>#at_a0 +350ms]漏れたIDとパスワードを、[>#at_p[*] {stagger:{each:0.15}}][♪pop -9dB][♪pop -9dB +150ms][♪pop -9dB +300ms][br]別のサービスで[>#at_a1][>#at_p[1].fi.v +250ms][>#at_p[1].fp.v +600ms][>#at_a2 +420ms][>#at_p[2].fi.v +670ms][>#at_p[2].fp.v +1020ms][>#at_a3 +840ms][>#at_p[3].fi.v +1090ms][>#at_p[3].fp.v +1440ms][♪type -7dB][♪type -8dB +600ms]次々に試します。
@: これが「[<#at_head.t -150ms][>#at_t2 +180ms][>#at_def +350ms][♪impact -12dB -50ms]{em}リスト型攻撃{/}」です。
@: [>#at_p[1].fp.same +200ms][>#at_p[2].fp.same +320ms][>#at_p[3].fp.same +440ms][♪tick -8dB +200ms][♪tick -8dB +320ms][♪tick -8dB +440ms]同じパスワードなら、[>#at_p[1].ring][>#at_p[1].ok][>#at_p[2].ring +280ms][>#at_p[2].ok +280ms][>#at_p[3].ring +560ms][>#at_p[3].ok +560ms][♪unlock -13dB][♪unlock -13dB +280ms][♪unlock -13dB +560ms]ログインは成功。[||][br]アカウントは[<#at_p[1].fp.same -250ms][<#at_p[2].fp.same -250ms][<#at_p[3].fp.same -250ms][>#at_p[1].x][>#at_p[2].x +200ms][>#at_p[3].x +400ms][♪stamp -8dB][♪stamp -8dB +200ms][♪stamp -8dB +400ms]乗っ取られてしまいます。

*** damage
se whoosh -9dB +50ms
@n: [silence:800ms][step_done #hdr.st[2] -500ms][step_on #hdr.st[3] -500ms][>#dm_head -500ms][>#dm_c1][♪pop -7dB]通販サイトでは、[!#dm_c1.b.r2 .hit][♪tick -8dB]登録済みのカードで、[>#dm_c1.b.stamp][>#dm_c1.tag +100ms][♪stamp -6dB]勝手に注文される。
@: [>#dm_c2][♪pop -7dB]SNSでは、[>#dm_c2.b.post.fake][>#dm_c2.tag +100ms][♪alert -10dB]あなたのふりをした投稿やメッセージが[>#dm_c2.b.m[1]][>#dm_c2.b.m[2] +120ms][>#dm_c2.b.m[3] +240ms][♪tick -4dB][♪tick -4dB +120ms][♪tick -4dB +240ms]送られる。
@: [>#dm_c3][>#dm_c3.tag +800ms][♪pop -7dB]会社のクラウドに侵入されれば、[!#dm_c3.b.f[1] .hit][♪tick -8dB][br]社内の資料や[!#dm_c3.b.f[2] .hit][>#dm_c3.b.f[1].e +1000ms][>#dm_c3.b.f[2].e +1150ms][♪tick -8dB][♪alert -9dB +1000ms]お客さまの情報まで見られてしまいます。
@: [!#dm_c1 to,{opacity:0.18, scale:0.97, duration:0.5, ease:'power2.inOut'} -100ms][!#dm_c2 to,{opacity:0.18, scale:0.97, duration:0.5, ease:'power2.inOut'} -100ms][!#dm_c3 to,{opacity:0.18, scale:0.97, duration:0.5, ease:'power2.inOut'} -100ms][>#dm_sum][>#dm_sum.a +50ms][♪whoosh -9dB -100ms]たった一つのパスワードが、[>#dm_arrow -450ms][>#dm_sum.b][♪impact -10dB]会社全体のリスクになるのです。

*** measures
se whoosh -9dB +50ms
@n: [silence:700ms][step_done #hdr.st[3] -400ms][step_on #hdr.st[4] -400ms][>#ms_head -150ms][♪ding -8dB]対策は、[>#ms_g[*] {stagger:{each:0.12}} -100ms][♪tick -6dB -100ms][♪tick -6dB +20ms][♪tick -6dB +140ms]3つです。
@: [<#ms_g[1]][>#ms_c1][♪pop -7dB]1つ目、{em}サービスごとに[>#ms_c1.v.t[1].k][>#ms_c1.v.t[2].k +130ms][>#ms_c1.v.t[3].k +260ms][♪tick -8dB][♪tick -8dB +130ms][♪tick -8dB +260ms]別のパスワード{/}にする。[||][!#ms_c1.v.t[1] .bad][>#ms_c1.v.leak +50ms][!#ms_c1.v.t[1] shake {x: 8, duration: .38} +50ms][♪alert -10dB][br]どこかで漏れても、[>#ms_c1.v.wall][>#ms_c1.v.wi +200ms][>#ms_c1.v.t[2].ok +350ms][>#ms_c1.v.t[3].ok +470ms][>#ms_c1.foot +400ms][♪shimmer -9dB]被害はそこで止まります。
@: [<#ms_g[2]][>#ms_c2][♪pop -7dB]2つ目、[>#ms_c2.v.mk][>#ms_c2.v.ml +50ms][>#ms_c2.v.dots.d[9] pop +150ms][>#ms_c2.v.dots.d[10] pop +220ms][>#ms_c2.v.dots.d[11] pop +290ms][>#ms_c2.v.dots.d[12] pop +360ms][>#ms_c2.v.dots.d[13] pop +430ms][>#ms_c2.v.dots.d[14] pop +500ms][!#ms_c2.v.dots.d[1] fill,$green {duration: .3} +650ms][!#ms_c2.v.dots.d[2] fill,$green {duration: .3} +670ms][!#ms_c2.v.dots.d[3] fill,$green {duration: .3} +690ms][!#ms_c2.v.dots.d[4] fill,$green {duration: .3} +710ms][!#ms_c2.v.dots.d[5] fill,$green {duration: .3} +730ms][!#ms_c2.v.dots.d[6] fill,$green {duration: .3} +750ms][!#ms_c2.v.dots.d[7] fill,$green {duration: .3} +770ms][!#ms_c2.v.dots.d[8] fill,$green {duration: .3} +790ms][!#ms_c2.v.dots.d[9] fill,$green {duration: .3} +810ms][!#ms_c2.v.dots.d[10] fill,$green {duration: .3} +830ms][!#ms_c2.v.dots.d[11] fill,$green {duration: .3} +850ms][!#ms_c2.v.dots.d[12] fill,$green {duration: .3} +870ms][!#ms_c2.v.dots.d[13] fill,$green {duration: .3} +890ms][!#ms_c2.v.dots.d[14] fill,$green {duration: .3} +910ms][♪type -8dB +100ms]{em}12文字以上{/}の長さにする。[||][<#ms_c2.v.len -300ms][>#ms_c2.v.cmp][br]複雑さより、[!#ms_c2.v.cmp{b} punch {scale: 1.15, duration: .45} -100ms][>#ms_c2.foot][♪ding -8dB]長さが大切です。
@: [<#ms_g[3]][>#ms_c3][♪pop -7dB]3つ目、[!#ms_c3.v.f2 .on][♪tick -8dB]{em}二段階認証{/}を有効にする。[||][>#ms_c3.v.att][!#ms_c3.v.att to,{x:126, y:-84, duration:0.7, ease:'power2.inOut'} +250ms][♪whoosh -12dB][br]パスワードだけでは、[>#ms_c3.v.x][!#ms_c3.v.f2 .ng][!#ms_c3.v.att shake {x: 8, duration: .38} +50ms][>#ms_c3.v.blk +150ms][>#ms_c3.foot +300ms][♪denied -7dB]ログインできなくなります。
@: パスワードは[>#ms_strip -350ms][♪whoosh -9dB -50ms]覚えずに、[>#ms_strip.vault][>#ms_strip.b][>#ms_strip.kf[*] {stagger:{each:0.1}} +300ms][>#ms_strip.kl +750ms][!#ms_strip.vault punch {scale: 1.08, duration: .43} +950ms][♪shimmer -8dB +200ms][br]{em}パスワード管理ツール{/}に任せましょう。

*** outro
se whoosh -9dB +50ms
@n: [silence:700ms][step_done #hdr.st[4] -400ms][>#ot_emp -500ms][>#ot_card -400ms][!#ot_card.i[1] to,{opacity:1, duration:0.35} -50ms][!#ot_card.i[1].ck recolor,$green][!#ot_card.i[1].ck pop][♪chime -12dB]使い回さない、[!#ot_card.i[2] to,{opacity:1, duration:0.35} -50ms][!#ot_card.i[2].ck recolor,$green][!#ot_card.i[2].ck pop][♪chime -12dB]長くする、[!#ot_card.i[3] to,{opacity:1, duration:0.35} -50ms][!#ot_card.i[3].ck recolor,$green][!#ot_card.i[3].ck pop][♪chime -12dB]二段階認証。[||][>#ot_banner][♪shimmer -8dB][br]今日から、自分のアカウントを守りましょう。[silence:2.6s]
fade out,900ms
```

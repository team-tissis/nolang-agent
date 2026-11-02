# data · library-survey-dialog (hf 全力版の全量の写し — 市立図書館、来ない人は何を求めている？・図書館職員と研究者の 2 人の掛け合いで市民調査を 9 場面のデータ図解に) — canvas 1920x1080

見せる作り: 全編の常設の層 (生成りの紙の地・左上の章札と右上の 8 段の進行・話者の顔の丸窓と色の名札つきの字幕の帯・grain)・夕景の題札と出演者の札・場面の骨組みの def (黒い題の札が跨る板・事実の行・大きい数字の組)・語で伸びる図 (数える 4,000 → 2,000 と回収率の輪の弧・100 マスの waffle の塗り替えと判子・7 本の縦棒と 4 割の破線と括弧・先に伸ばして 1 位を後から出す理由の横棒・灯る要望の行・利用者 vs 来ない人のダンベル図・延長した 2 時間の帯と前後の横棒と倍率の札)・場面ごとの切替 (紙がめくれる wipe・溶ける・押し出す・夜の色の幕の暗転・寄りながら溶ける)・夜の写真の締めと夜の色への fade・音の層 (BGM + 語に結んだ効果音 45 + 切替の音)

```design.txt
#v2
# 学ぶ作り: 2 人の掛け合いの調査報告。全編に敷く常設の層 (紙の地・左上の章札と右上の 8 段の進行・顔の丸窓つきの字幕の帯・grain) の上で、場面ごとに題つきの板の図を替える
# 図は台詞の数字の語で伸ばす: 数える大きい数字・回収率の輪の弧・100 マスの waffle の塗り替え・年代の縦棒と 4 割の破線・理由と要望の横棒・利用者 vs 来ない人のダンベル図・延長した 2 時間の帯と前後の横棒
# 切替は場面ごとに替える (紙がめくれる wipe・溶ける・押し出す・夜の色への暗転・寄りながら溶ける) — 締めは夜の写真に題を再掲し夜の色へ fade
# hf d12 library-survey-dialog (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#F5EEE2
theme light
palette a=#BF4F34 b=#2A6F7D paper=#F5EEE2 paper2=#FFFBF3 ink=#2E2823 ink2=#625649 line=#E4D6C1 terra=#BF4F34 teal=#2A6F7D sage=#A9BFB3 amber=#D7882A lamp=#F4C46A night=#1B2440 cream=#FFF4DF mark=#F4C46A9E mori=#94561B takagi=#46508C sand=#D8CDB9 brown=#B0631A rust=#B0640C kick=#8A4F12 qred=#8E2E17 gold=#A8620F cell=#E9DFCF ringbg=#EADFCD segbg=#E2D5C2 tick=#E2D4BF dline=#D9C9B2 ibg=#F2E5D3 track=#EEE3D3 hlbg=#FDF0E8 actbg=#FDF3E2 fade=#F4EDE1 org=#E6DCCB foot=#C9BFAE deep=#11172A
font "癖のない標準的な日本語のゴシック体の太字 (Bold)、画面の資料や UI 向けの読みやすい書体"
# hf の注記は中太 (Medium) — 中太の説明文は略字の書体に当たる (「本」が崩れる) ので注記も本文の太字で
fonts b="癖のない標準的な日本語のゴシック体の太字 (Bold)、画面の資料や UI 向けの読みやすい書体" s="端正な日本語の明朝体の太字 (Bold)、見出しと大きな数字向けの読みやすい明朝"
sfx off
art "やわらかな水彩と色鉛筆の日本の絵本風イラスト、生成り・琥珀・テラコッタ・セージグリーン・くすんだ藍の落ち着いた色、紙の質感が見える"
prompt_tail "文字・数字・ロゴ・看板の文字は入れない"
# hf の作り: 板の題・見出し・図の骨組みは場面の頭に出し、台詞が後から数字を読む (spoiler・empty_board)・注記と凡例は 14〜17 px (small_text)
# hf の作り: 黒い題の札は板の上辺に跨って外へ出る・判子は札の角から外へ・時刻の目盛りは帯の両端から外へ (child_overflow)
# hf の作り: 切替は前の場面の最後の声の 40 ms 前から溶け始め、注記・数字・終わりの札は場面の終わり際まで出る (transition_over_speech・ghost_dissolve・entrance_in_fadeout・entrance_in_transition・flash_text)
# hf の作り: 試行の場面は 20 秒同じ夜の写真・冒頭の出演者の札と字幕の帯に同じ顔・夜の場面へは夜の色の幕で暗転・まとめは章札・結論の札・番号の札が縦に並ぶ (same_picture・duplicate_media・dip_black_frame・stacked_labels)
# hf の作り: 冒頭の出演者の札 2 枚は絵の右の図書館の上に重ねる (warn text_over_subject はそのまま)
lint off=spoiler,empty_board,small_text,child_overflow,transition_over_speech,ghost_dissolve,entrance_in_fadeout,entrance_in_transition,flash_text,same_picture,duplicate_media,dip_black_frame,stacked_labels
run b { color: $ink }
run pc { font-size: 0.48em }
run un { font-size: 0.43em; color: $ink2; font-family: b }
run pw { font-size: 0.45em }
run hu { font-size: 0.54em; font-family: b }
run pn { font-size: 24px; color: $ink2; font-family: b }
run bx { font-size: 0.5em }
run sm { font-size: 22px; color: $ink2 }
run t { color: $terra }
run lp { color: $lamp }
run lo { font-size: 52px; color: $terra; font-family: s }
run hi { font-size: 52px; color: $teal; font-family: s }
run mid { font-size: 40px; color: $gold; font-family: s }
sound riffle = "厚い辞書の薄いページを指で素早くパラパラとめくる軽い紙の音"
sound page = "紙のページを 1 枚さっとめくる乾いた短い音"
sound pop = "紙の筒で鳴らした乾いた軽いポンという音"
sound pop2 = "口で鳴らしたような短く乾いたパッという軽いポップ音"
sound sparkle = "シンセのハープの分散和音と風鈴がきらめく、明るく高いアクセント音"
sound tick = "掛け時計のスイッチを切り替えるカチッという乾いたプラスチックの音"
sound pencil = "鉛筆で紙にさっとチェックを書くカリッという柔らかい音"
sound bell = "高く澄んだ短いシンセのベルのアクセント音"
image mori = "日本人の女性の図書館司書の胸から上の肖像。30代後半、肩までの黒髪、白いブラウスにベージュのカーディガン、職員証のストラップ、温かい笑顔で少し右を向く。顔は画面の中央やや上に大きく。背景は無地の生成り色に淡い水彩のにじみ"
image takagi = "日本人の男性の大学研究者の胸から上の肖像。40代後半、白髪まじりの短髪に丸めがね、襟付きシャツに紺のニットのセーター、落ち着いた温かい笑顔で少し左を向く。顔は画面の中央やや上に大きく。背景は無地の生成り色に淡い水彩のにじみ"
image station = "夜の日本の通勤駅のすぐ前の建物に入った小さな図書館の分館。大きな窓から金色の温かい光があふれ、仕事帰りの人が駅から入っていく (トートバッグの30代の女性・スーツの40代の男性・リュックの大学生)。中では本棚を見る人や机で読む人。奥の高架を電車が走り、空は深い藍の夜。希望のある迎え入れる雰囲気。明るい館は画面の右 6 割に置き、左 4 割は夜の街と人の影で静かに" aspect=16:9
# 板の中の動き: 段の入場 (cue) と、話者が替わる時に字幕の帯の顔の丸窓を入れ替える
cue spk(on, off) = [!#off to,{opacity: 0, scale: .8, duration: .15, ease: 'none'}][!#on to,{opacity: 1, scale: 1, duration: .3, ease: 'back.out'}]
p { color: $ink; in: none; out: none }
div { in: none; out: none }
img { in: none; out: none }
shape { in: none; out: none }
icon { in: none; out: none }
# 字幕: 帯 (下の白い板) の中に、話者の名札 (色の字) と台詞の 1 行。札は hf の句の割り方 ([|]) どおり
# 字幕の名札 (top_left) は字幕の枠の上辺の 51px 上・枠の左 +14px — 台詞は枠の上端に寄せ、hf の名札 (字面 628〜639) と台詞 (656〜681)・左端 210 に合わせる
# 字幕の 」。 は約物の連続として詰まる (engine の約物詰めは書体を問わない)
subtitle.hug(left: 300px; bottom: 30px; width: 1395px; padding: 0px 39px 0px 12px; font-size: 42px; line-height: 1; letter-spacing: .03em; color: $ink; text-align: left; background: none; label: top_left; unit: sentence; lead: 0ms; tail: 150ms; hold: next,500ms; in: {y:10, opacity:0, duration:.18, ease:'power1.out'}; out: {opacity:0, duration:.1})
bgm#music(fade: 1400,900) 明るく温かく穏やかな、懐かしさと希望のあるピアノとアコースティックギターと弦の日常系のポップ、四拍子の普通の速さ、やさしい調査報告の解説向け
# 全編の地: 生成りの紙 (中央がわずかに明るい)・最前面に薄い grain
div#paper(inset: 0; background: radial(#FAF5EC,#F5EEE2@60%,#ECE2D2,50%,40%); z-index: back)
veil#grain(grain: 0.05; color: #00000000; z-index: curtain; in: none)

# 部品: 題つきの板 (生成りの板 + 黒い題の札)・左上の章札 (茶の番号 + 題)・事実の行・写真の札
def board = div(background: $paper2; border: 2px solid $line; border-radius: 28px; box-shadow: 0px 20px 44px #5C3E1E1F)
def tab(t) = p(left: 40px; top: -26px; font-size: 27px; color: $paper2; background: $ink; border-radius: 14px; padding: 9px 24px 10px 48px; letter-spacing: .04em; content: {t})
  div#sq(left: 24px; cy: 50%; width: 12px; height: 12px; border-radius: 3px; background: $lamp)
def chap(n, t) = p(left: 70px; top: 30px; font-size: 28px; line-height: 1.2; letter-spacing: .04em; background: #FFFBF3F0; border-radius: 18px; padding: 15px 26px 16px 75px; box-shadow: 0px 8px 22px #3C28141F; z-index: front; in: {x:-30, opacity:0, duration:.55, ease:'back.out(1.6)'}; out: {x:20, opacity:0, duration:.3, ease:'power2.in'}; content: {t})
  p#n(left: 10px; cy: 50%; width: 48px; font-size: 26px; font-family: s; line-height: 1.4; text-align: center; color: #FFFFFF; background: $brown; border-radius: 14px; padding: 6px 0px; content: {n})
def card = div(background: $paper2; border-radius: 26px; box-shadow: 0px 18px 42px #5C3E1E21)
# 冒頭の出演者の札 (丸い顔 + 名 + 読み + 肩書)
def cast_card(n, k, r, c) = div(left: 1290px; width: 560px; height: 150px; background: $paper2; border-radius: 26px; box-shadow: 0px 18px 42px #5C3E1E21; in: {x:80, opacity:0, duration:.6, ease:'back.out(1.5)'})
  img#p(left: 16px; cy: 50%; width: 120px; height: 120px; border-radius: 148px; box-shadow: 0px 0px 0px 4px {c}; object-fit: cover; object-position: 50% 25%; main: none)
  p#n(left: 162px; top: 18px; font-size: 50px; font-family: s; line-height: 1.1; content: {n})
  p#k(left: .n.right+10; top: 36px; font-size: 24px; color: $ink2; content: {k})
  p#r(left: 162px; top: 86px; font-size: 26px; color: {c}; content: {r})
# 調査の事実の行 (線の icon + 題 + 右寄せの値)
def fact(i, t, e, c=$teal, bc=$line) = div(left: 90px; width: 800px; height: 69px; background: $paper2; border: 2px solid {bc}; border-radius: 18px; in: {x:-40, opacity:0, duration:.5, ease:'power2.out', stagger: {each: .14}})
  icon#i(left: 21px; cy: 50%; font-size: 39px; name: {i}; color: {c})
  p#t(left: 81px; cy: 50%; font-size: 28px; content: {t})
  p#e(right: 22px; cy: 50%; font-size: 24px; color: $ink2; content: {e})
# 大きい数字の組 (線の icon + 題 → 明朝の数字と単位 → 注記)
# 大きい数字の横の単位は数字の run (baseline に乗る)・hf の margin-left 9px は run に書けないので詰めて置く
def flow(i, l, v, u, n) = div(top: 74px; width: 390px; height: 202px; in: {y:30, opacity:0, duration:.5, ease:'back.out(1.4)'})
  icon#i(left: 0px; top: 3px; font-size: 36px; name: {i}; color: $teal)
  p#l(left: 48px; top: 0px; font-size: 28px; color: $ink2; content: {l})
  p#v(left: 0px; top: 46px; font-size: 112px; font-family: s; line-height: 1; letter-spacing: -.035em; content: {v}{un}{u}{/})
  p#n(left: 0px; top: 165px; font-size: 22px; color: $ink2; content: {n})

# title — 夕暮れの図書館の絵に寄りから引き、左の余白に題札 (前置き → 2 行の大題 → 揺れる ？ → 罫 → 副題)・語で出演者の札 2 枚
section#title(stagger: {each:0})
img#a_img(inset: 0; subject: right 60%; room: left 40%; main: kb {scale: [1.12, 1], focus: ['42% 50%', '50% 50%'], ease:'sine.out'}) 夕暮れの日本の小さな市の、2 階建ての現代的な市立図書館を、並木のある静かな通りの向かいから見た横長の構図。大きなガラス窓から琥珀色の温かい光がもれ、中の本棚が見える。空は桃色からくすんだ藍へのやわらかなグラデーション。コートを着た通勤の人が数人、歩道を歩く。図書館と人は画面の右 6 割に置き、左の 4 割は空と並木だけの静かな余白にする
div#a_shade(inset: 0; background: linear(#F7F0E5F5,#F7F0E5E6@36%,#F7F0E559@58%,#F7F0E500@72%,90))
p#a_kick(left: 120px; top: 150px; font-size: 24px; color: $kick; background: #FFFBF3CC; border: 3px solid $amber; border-radius: 148px; padding: 8px 20px; delay: 200ms; in: {y:20, opacity:0, duration:.5, ease:'power2.out'}) 市民調査レポート
p#a_t1(left: 120px; top: 230px; font-size: 70px; font-family: s; line-height: 1.15; color: $ink2; delay: 400ms; in: {x:-40, opacity:0, duration:.7, ease:'expo.out'}) 市立図書館、
p#a_t2a(left: 120px; top: 336px; font-size: 118px; font-family: s; line-height: 1.16; letter-spacing: .01em; delay: 620ms; in: {y:46, opacity:0, duration:.8, ease:'power3.out'}) 来ない人は
p#a_t2b(left: 120px; top: 478px; font-size: 118px; font-family: s; line-height: 1.16; letter-spacing: .01em; delay: 800ms; in: {y:46, opacity:0, duration:.8, ease:'power3.out'}) 何を求めている
# ？ だけ別の文字にして、下寄りの点を軸に左右に揺らす
p#a_q(left: a_t2b.right+21; top: 478px; font-size: 118px; font-family: s; line-height: 1.16; color: $qred; transform-origin: 50% 80%; delay: 800ms; in: {y:46, opacity:0, duration:.8, ease:'power3.out'}) ？
div#a_rule(left: 120px; top: 634px; width: 520px; height: 4px; border-radius: 3px; background: $amber; delay: 1200ms; in: {scaleX:0, duration:.7, ease:'power2.inOut', pivot:'left'})
p#a_sub(left: 120px; top: 656px; font-size: 30px; letter-spacing: .04em; color: $ink2; delay: 1500ms; in: {opacity:0, duration:.6, ease:'sine.out'}) みなと野市　{b}16歳以上の市民 2,000人{/}の回答から
cast_card#cast_mori(top: 394px; n: "森"; k: "もり"; r: "みなと野市立図書館 職員"; c: $mori)
  img#p(content: @mori)
cast_card#cast_takagi(top: 574px; n: "高木"; k: "たかぎ"; r: "みなと野学園大学 研究室"; c: $takagi)
  img#p(content: @takagi)
# 字幕の帯 (sticky・締めの前まで): 白い板 + 話者の顔の丸窓 2 つ (話者が替わる語で cue spk が入れ替える)
div#subbar.sticky(left: 190px; top: 930px; width: 1540px; height: 120px; background: #FFFBF3F5; border-radius: 30px; box-shadow: 0px 14px 34px #32201033; z-index: front; in: {y:40, opacity:0, duration:.5, ease:'power3.out'}; out: {y:30, opacity:0, duration:.35, ease:'power2.in'})
  img#av_mori(left: 14px; cy: 50%; width: 86px; height: 86px; border-radius: 148px; box-shadow: 0px 0px 0px 4px $mori; content: @mori; object-fit: cover; object-position: 50% 25%; opacity: 0; main: none)
  img#av_takagi(left: 14px; cy: 50%; width: 86px; height: 86px; border-radius: 148px; box-shadow: 0px 0px 0px 4px $takagi; content: @takagi; object-fit: cover; object-position: 50% 25%; opacity: 0; main: none)

# survey — 01 調査のあらまし: 常設の上端 (章札・進行) が入り、傾いた写真の札と事実の行 3 本 → 板の「4,000人」「2,000人」を数え、回収率の輪の弧を半周描く
section#survey(stagger: {each:0})
chap#ch1.sticky(n: "01"; t: "調査のあらまし")
# 右上の進行 (sticky・8 段の小さな棒を章ごとに左から満たす)
div#hdr_r.sticky(left: 1260px; top: 36px; width: 590px; height: 56px; background: #FFFBF3F0; border-radius: 18px; box-shadow: 0px 8px 22px #3C28141F; z-index: front; in: {y:-24, opacity:0, duration:.6, ease:'power3.out'}; out: {y:-20, opacity:0, duration:.4, ease:'power2.in'})
  div#seg(left: "210;231;252;273;294;315;336;357"; cy: 50%; width: 26px; height: 8px; border-radius: 4px; background: $segbg) ×8
    div#fill(left: 0px; top: 0px; width: 26px; height: 8px; border-radius: 4px; background: $amber; in: {scaleX:0, duration:.5, ease:'power2.out', pivot:'left'})
  p#brand(left: 24px; cy: 50%; font-size: 21px; letter-spacing: .06em; color: $ink2) みなと野市 図書館利用調査
card#b_photo(left: 90px; top: 150px; width: 800px; height: 500px; transform: rotate(-1.6deg); delay: 450ms; in: {y:40, rotation:-3.4, opacity:0, duration:.8, ease:'power3.out'})
  img#img(left: 16px; top: 16px; width: 766px; height: 466px; border-radius: 16px; main: kb {scale: [1.12, 1], ease:'sine.out'}) 大学の研究室の木の机を真上から見た構図。返送された紙の調査票と封筒がきちんと積まれ、鉛筆でチェックが入った調査票が数枚、簡単な棒グラフを映すノートパソコン、紅茶のマグ、鉛筆、温かい光のデスクランプ。机の上の物を画面いっぱいに配して余白を作らない。読める文字や数字は描かない
fact#b_fact(top: "467;522;576"; i: "map-pin;bank;clock"; t: "みなと野市;市立図書館;平日の閉館"; e: "人口 18万人;本館 1・分館 3;19時"; c: "$teal;$teal;$amber"; bc: "$line;$line;$amber"; delay: 700ms) ×3
board#b_board(left: 960px; top: 160px; width: 880px; height: 700px; delay: 550ms; in: {y:30, opacity:0, duration:.6, ease:'power2.out'})
  tab#tab 調査のあらまし
  flow#send(left: 50px; i: envelope-simple; l: "調査票を送った人"; v: "[count:4,000 start=0 ms=1000ms]"; u: "人"; n: "16歳以上の市民")
  p#arrow(left: 423px; top: 129px; font-size: 58px; color: $amber; in: {x:-30, opacity:0, duration:.5, ease:'power2.out'}) →
  flow#back(left: 483px; i: users; l: "回答した人"; v: "[count:2,000 start=0 ms=900ms]"; u: "人"; n: "市と大学の研究室が集計")
  # 回収率の輪: 地の輪 + 上から右回りに半周の弧 (語で描く)・中に数える 50%
  div#ring(left: 50px; top: 360px; width: 290px; height: 290px; in: {scale:.85, opacity:0, duration:.5, ease:'power2.out'})
    shape#bg(left: 9px; top: 9px; width: 272px; height: 272px; border-radius: 50%; background: none; border: 34px solid $ringbg)
    shape#arc(left: 0px; top: 0px; width: 290px; height: 290px; path: "M 96.5 17.5 C 140.1 17.5 175.5 52.9 175.5 96.5 C 175.5 140.1 140.1 175.5 96.5 175.5"; background: none; border: 34px solid $teal; main: sine {rotation: 6, period: 1.6}; in: draw {duration: 1, ease: 'power2.inOut'})
    p#v(cx: 50%; top: 84px; font-size: 92px; font-family: s; line-height: 1; color: $teal) [count:50 start=0 ms=1000ms delay=200ms]{pc}%{/}
    p#l(cx: 50%; top: 180px; font-size: 26px; color: $ink2) 回収率
  div#note(left: 380px; top: 420px; width: 450px; height: 150px; in: {x:30, opacity:0, duration:.6, ease:'power2.out'})
    # 語の下の帯 (hf の inline の地の下 42%): 字面の下 1/3 に掛かり字の下へ 8px 出る — 行の頭から +0.85 字・高さ 0.55 字。run の marker の帯は行の頭 +1.02 字が下端で、行高 1.5 では字の中央を横切る
    div#mk(left: b_board.note.t.chars(4,9).left; right: b_board.note.t.chars(4,9).right; top: b_board.note.t.chars(4,9).top+26; height: 16px; background: $mark)
    p#t(left: 0px; top: 0px; font-size: 30px; line-height: 1.5) 送った 2人に1人が[br]答えてくれた
    p#n(left: 0px; top: 106px; font-size: 22px; color: $ink2) ※ 回答 2,000人 ÷ 送付 4,000人

# used — 02 この1年の利用: 100 マスの waffle (1 マス = 1%) を語で青緑 38 → テラコッタ 62 に塗り、右に 38% と 62% の札 (数える)・「6割が来ていない」の判子
section#used(stagger: {each:0})
# 省いた: hf の紙の場面 (02・06・08) は場面の尺で全体が 1.5〜2% ゆっくり寄る (常設の層まで寄るので camera を置かず静止)
chap#ch2.sticky(n: "02"; t: "この1年の利用")
board#c_board(left: 90px; top: 160px; width: 860px; height: 700px; delay: 250ms; in: {scale:.96, opacity:0, duration:.6, ease:'power2.out'})
  tab#tab 回答者 2,000人のうち
  div#lg(left: 666px; top: "60;92"; width: 180px; height: 30px; delay: 400ms; in: {x:-16, opacity:0, duration:.4, ease:'power1.out', stagger: {each: .12}}) ×2
    div#sq(left: 0px; cy: 50%; width: 24px; height: 24px; border-radius: 6px; background: "$teal;$terra")
    p#t(left: 36px; cy: 50%; font-size: 22px) 使った;使っていない
  p#wnote(left: 666px; top: 540px; width: 170px; font-size: 21px; line-height: 1.45; color: $ink2; delay: 700ms; in: {opacity:0, duration:.4, ease:'none'}) 1マス ＝ 1%[br]（20人）
# マスは薄い地の色で置き、語で色を塗る (変種 .on・左上から 26 ms / 18 ms ずつ)
div#c_wu(cx: "123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05"; cy: "174.25;174.25;174.25;174.25;174.25;174.25;174.25;174.25;174.25;174.25;212.05;212.05;212.05;212.05;212.05;212.05;212.05;212.05;212.05;212.05;249.95;249.95;249.95;249.95;249.95;249.95;249.95;249.95;249.95;249.95;287.75;287.75;287.75;287.75;287.75;287.75;287.75;287.75"; width: 49px; height: 49px; border-radius: 9px; transform: scale(0.6); background: $cell) ×38
div#c_wn(cx: "425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75;123.25;161.05;198.95;236.75;274.55;312.45;350.25;388.05;425.95;463.75"; cy: "287.75;287.75;325.55;325.55;325.55;325.55;325.55;325.55;325.55;325.55;325.55;325.55;363.45;363.45;363.45;363.45;363.45;363.45;363.45;363.45;363.45;363.45;401.25;401.25;401.25;401.25;401.25;401.25;401.25;401.25;401.25;401.25;439.05;439.05;439.05;439.05;439.05;439.05;439.05;439.05;439.05;439.05;476.95;476.95;476.95;476.95;476.95;476.95;476.95;476.95;476.95;476.95;514.75;514.75;514.75;514.75;514.75;514.75;514.75;514.75;514.75;514.75"; width: 49px; height: 49px; border-radius: 9px; transform: scale(0.6); background: $cell) ×62
#c_wu.on(background: $teal; transform: scale(1); move: 350ms,back.out)
#c_wn.on(background: $terra; transform: scale(1); move: 300ms,back.out)
card#c_use(left: 1010px; top: 170px; width: 830px; height: 320px; in: {x:60, opacity:0, duration:.6, ease:'power3.out'})
  p#v(left: 40px; top: 24px; font-size: 168px; font-family: s; line-height: .95; letter-spacing: -.02em; color: $teal) [count:38 start=0 ms=900ms delay=100ms]{pw}%{/}
  p#l(left: 334px; top: 136px; font-size: 36px; line-height: 1.35) この1年に[br]図書館を使った
  p#s(left: 334px; top: 246px; font-size: 30px; color: $ink2) 760人
card#c_non(left: 1010px; top: 525px; width: 830px; height: 324px; border: 3px solid $terra; in: {x:60, opacity:0, duration:.6, ease:'power3.out'})
  p#v(left: 40px; top: 27px; font-size: 168px; font-family: s; line-height: .95; letter-spacing: -.02em; color: $terra) [count:62 start=0 ms=900ms delay=100ms]{pw}%{/}
  p#l(left: 334px; top: 140px; font-size: 36px; line-height: 1.35) 1年間[br]一度も使っていない
  p#s(left: 334px; top: 249px; font-size: 30px; color: $ink2) 1,240人
  # 判子: 板の右上の角に傾けて弾ませ、少し戻して揺らす
  p#stamp(right: 34px; top: -30px; font-size: 30px; color: #FFFFFF; background: $terra; border-radius: 14px; padding: 10px 24px; box-shadow: 0px 10px 20px #96321E40; transform: rotate(4deg); in: {scale:1.6, rotation:-12, opacity:0, duration:.45, ease:'back.out(2.2)'}) 6割が来ていない
p#c_note(left: 1020px; top: 888px; font-size: 22px; color: $ink2; in: {opacity:0, duration:.5, ease:'none'}) ※ 過去1年に1回以上使ったかどうか（16歳以上の回答者）

# age — 03 年代別の利用率: 基線が伸びて 7 本の縦棒が左から立ち上がり値・年代・人数 →「26%」で 20 代を縁取り脈打たせる → 働く世代の括弧と 4 割の破線 → 4 割に届かない 3 本が跳ねる・右に札 3 枚
section#age(stagger: {each:0})
chap#ch3.sticky(n: "03"; t: "年代別の利用率")
board#d_board(left: 80px; top: 150px; width: 1250px; height: 730px)
  tab#tab 年代別の利用率（利用者 ÷ 回答者）
  div#base(left: 70px; top: 588px; width: 1120px; height: 3px; border-radius: 2px; background: $ink2; delay: 450ms; in: {scaleX:0, duration:.6, ease:'power2.out', pivot:'left'})
  # 4 割の破線 (左から伸びる) と札・働く世代 (20〜50 代) の括弧
  shape#d40(left: 70px; top: 220px; width: 1120px; height: 3px; path: line_h; border: 3px solid $terra; dash: 6,5; in: {scaleX:0, duration:.8, ease:'power2.inOut', pivot:'left'})
  p#d40l(left: 6px; top: 202px; font-size: 26px; color: $terra; background: $paper2; padding: 0px 8px; in: {opacity:0, duration:.3, ease:'none'}) 4割
  shape#bracket(path: "M 163 100 L 163 85 Q 163 77 171 77 L 562 77 Q 570 77 570 85 L 570 100"; background: none; border: 3px solid $ink2; in: {y:-14, opacity:0, duration:.5, ease:'power2.out'})
  p#blabel(cx: 549px; top: 76px; font-size: 26px; background: $paper2; padding: 0px 12px; in: {y:-14, opacity:0, duration:.5, ease:'power2.out'}) 働く世代（20〜50代）
  # 縦棒の段: 高さ = 値 × 6.13 px (hf の 9.2 px / 1% の 2/3)・基線は段の上端から 353 px
  div#col(left: "67;172.3;277.7;383;488.3;593.7;699"; top: 60px; width: 108px; height: 630px) ×7
    div#bar(left: 0px; top: "34.1;193.5;144.5;101.5;150.6;126.1;52.5"; width: 108px; height: "318.9;159.5;208.5;251.5;202.4;226.9;300.5"; border-radius: 14px 14px 4px 4px; background: "$teal;$terra;$sage;$amber;$sage;$sage;$teal"; delay: "650ms;750ms;850ms;950ms;1050ms;1150ms;1250ms"; in: {scaleY:0, duration:.7, ease:'power3.out', pivot:'bottom'})
    p#v(cx: 50%; top: "-5;154.5;105.5;62.5;111.6;87.1;13.5"; font-size: 46px; font-family: s; line-height: 1; color: "$teal;$terra;$ink;$ink;$ink;$ink;$teal"; background: $paper2; border-radius: 10px; padding: 0px 8px; delay: "1050ms;1150ms;1250ms;1350ms;1450ms;1550ms;1650ms"; in: {y:16, opacity:0, duration:.4, ease:'power2.out'}) 52{pc}%{/};26{pc}%{/};34{pc}%{/};41{pc}%{/};33{pc}%{/};37{pc}%{/};49{pc}%{/}
    p#a(cx: 50%; top: 542px; width: 165px; font-size: 30px; text-align: center; white-space: nowrap; delay: "500ms;560ms;620ms;680ms;740ms;800ms;860ms"; in: {opacity:0, duration:.4, ease:'none'}) 10代;20代;30代;40代;50代;60代;70歳以上
    p#c(cx: 50%; top: 584px; width: 165px; font-size: 21px; text-align: center; white-space: nowrap; color: $ink2; delay: "500ms;560ms;620ms;680ms;740ms;800ms;860ms"; in: {opacity:0, duration:.4, ease:'none'}) 78 / 150人;65 / 250人;112 / 330人;148 / 360人;109 / 330人;111 / 300人;137 / 280人
#d_board.col.bar.halo(box-shadow: 0px 0px 0px 10px #BF4F3438)
board#d_low(left: 1370px; top: 150px; width: 470px; height: 152px; border: 3px solid $terra; border-radius: 22px; in: {x:40, opacity:0, duration:.5, ease:'back.out(1.6)'})
  p#h(left: 26px; top: 22px; font-size: 24px; letter-spacing: .04em; color: $ink2) いちばん低い
  p#p(left: 26px; top: 63px; font-size: 34px; line-height: 1.3) 20代 {lo}26%{/}
board#d_hi(left: 1370px; top: 324px; width: 470px; height: 216px; border: 3px solid $line; border-radius: 22px; in: {x:40, opacity:0, duration:.5, ease:'power2.out'})
  p#h(left: 26px; top: 22px; font-size: 24px; letter-spacing: .04em; color: $ink2) よく来ている
  p#p(left: 26px; top: 60px; font-size: 34px; line-height: 1.3) 10代 {hi}52%{/}[br]70歳以上 {hi}49%{/}
board#d_40(left: 1370px; top: 564px; width: 470px; height: 194px; border: 3px solid $amber; border-radius: 22px; in: {x:40, opacity:0, duration:.55, ease:'back.out(1.5)'})
  img#thumb(left: 26px; top: 21px; width: 150px; height: 150px; border-radius: 16px; object-fit: cover; object-position: 62% 50%; main: none) 40代の日本人の親と 5 歳くらいの子どもが、公立図書館の児童コーナーの低いクッションのベンチに並んで座り、色とりどりの絵本を一緒に選んでいる。午後の温かい光、やさしい笑顔。親子を画面の中央に大きく置き、余白を作らない
  p#t(left: 196px; top: 24px; width: 255px; font-size: 27px; line-height: 1.45) 40代 {mid}41%{/}[br]子どもの絵本を[br]借りに来る親が多い

# reasons — 04 使わない理由: 右半分に閉まった図書館の前に立つ人の絵 (左の縁は紙へ溶ける)・板に理由の横棒 4 本を先に伸ばし「1位は…？」→ 1 位の行を語で伸ばして 41%・本の理由 2 行を薄め、時計の icon を回す
section#reasons(stagger: {each:0})
chap#ch4.sticky(n: "04"; t: "使わない理由")
img#e_img(left: 960px; top: 0px; width: 960px; height: 1080px; object-fit: cover; object-position: 16% 50%; main: kb {scale: [1.1, 1], ease:'sine.out'}) 夜、公立図書館の閉まったガラスの入口扉の前に立つ、20 代の疲れた日本人の会社員の男性。スーツに肩掛けのかばん、うつむきぎみに扉を見つめる。館内は暗く本棚がかすかに見え、入口近くの小さな壁掛け時計は 7 時過ぎを指す。街灯が歩道を温かく照らす。静かで少しさみしいがやさしい雰囲気。男性を画面の中央に大きく置く
div#e_fade(left: 960px; top: 0px; width: 220px; height: 1080px; background: linear($fade,#F4EDE100,90))
p#e_tag(left: 1420px; top: 770px; font-size: 30px; color: $cream; background: #1B2440E0; border-radius: 16px; padding: 14px 26px 14px 70px; delay: 1150ms; in: {y:20, opacity:0, duration:.5, ease:'power2.out'}) 平日は 19時に閉館
  icon#i(left: 22px; cy: 50%; font-size: 39px; name: clock; color: $lamp)
board#e_board(left: 80px; top: 160px; width: 960px; height: 700px; delay: 450ms; in: {y:30, opacity:0, duration:.55, ease:'power2.out'})
  tab#tab 図書館を使わない理由（非利用者 1,240人・複数回答）
  div#hl(left: 44px; top: 60px; width: 876px; height: 84px; background: #F4C46A2E; in: {opacity:0, duration:.4, ease:'none'})
  p#q(left: 44px; top: 60px; font-size: 30px; letter-spacing: .2em; color: $ink2; in: {opacity:0, duration:.3, ease:'none'}; out: {opacity:0, duration:.2, ease:'none'}) 1位は…？
  # 1 位の行: 時計の icon + 題 → テラコッタの棒 → 41% と 508人
  div#top(left: 44px; top: 60px; width: 876px; height: 84px)
    # 変えた: 「時間」の語で時計の icon を -180° から戻す動きは 1 回転 (0 → 360°) にした (状態の to は今の角度からしか回せない)
    div#lab(left: 0px; top: 0px; width: 600px; height: 38px; in: {y:12, opacity:0, duration:.45, ease:'back.out(1.8)'})
      icon#i(left: 0px; cy: 50%; font-size: 33px; name: clock; color: $terra)
      p#t(left: 44px; cy: 50%; font-size: 30px) 開いている時間に行けない
    div#b(left: 0px; top: 46px; width: 640px; height: 36px; border-radius: 0px 12px 12px 0px; background: $terra; in: {scaleX:0, duration:.9, ease:'power3.out', pivot:'left'})
    p#v(left: 660px; top: 40px; font-size: 48px; font-family: s; line-height: 1; color: $terra; in: {x:-20, opacity:0, duration:.4, ease:'power2.out'}) 41{pc}%{/}　{pn}508人{/}
  # 2〜5 位の行 (語の頭から 160 ms ずつ: 題 → 棒 → 値)・棒の長さ = 値 × 10.4 px
  div#r(left: 44px; top: "105;170;235;300"; width: 876px; height: 84px) ×4
    p#l(left: 0px; top: 0px; font-size: 30px; in: {x:-20, opacity:0, duration:.4, ease:'power2.out'}) 本は買うかネットで足りる;読みたい本がない;遠い・駐車場がない;長くいられる席がない
    div#b(left: 0px; top: 46px; width: "343;229;198;145"; height: 36px; border-radius: 0px 12px 12px 0px; background: $sage; delay: 100ms; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
    p#v(left: "356;242;211;158"; top: 40px; font-size: 48px; font-family: s; line-height: 1; delay: 500ms; in: {opacity:0, duration:.3, ease:'none'}) 33{pc}%{/};22{pc}%{/};19{pc}%{/};14{pc}%{/}
  p#btag(left: "277;197"; top: "105;170"; font-size: 20px; color: $ink2; border: 2px solid $line; border-radius: 148px; padding: 2px 12px; in: {x:-20, opacity:0, duration:.4, ease:'power2.out'}) ×2 本;本
  div#sum(left: 44px; top: 614px; width: 840px; height: 52px; in: {y:20, opacity:0, duration:.5, ease:'power3.out'})
    icon#i(left: 6px; cy: 50%; font-size: 44px; name: clock; color: $amber)
    div#mk(left: e_board.sum.t.chars(10,14).left-6; top: e_board.sum.t.chars(10,14).top+24; width: 142px; height: 21px; background: $mark)
    p#t(left: 63px; cy: 50%; font-size: 34px) 1位は「本」ではなく「時間」の問題

# wants — 05 来ない人が欲しいもの: 傾いた館内の写真の札・板に要望の行 4 本 (icon の地・題・人数・細い棒・%) → 語で 1 位・2 位の行に枠と地を灯し、% を弾ませる
section#wants(stagger: {each:0})
chap#ch5.sticky(n: "05"; t: "来ない人が欲しいもの")
card#f_photo(left: 80px; top: 160px; width: 760px; height: 700px; transform: rotate(1.2deg); delay: 250ms; in: {y:40, rotation:3.8, opacity:0, duration:.8, ease:'power3.out'})
  img#img(left: 16px; top: 16px; width: 728px; height: 668px; border-radius: 16px; object-fit: cover; object-position: 30% 50%; main: kb {scale: [1.12, 1], ease:'sine.out'}) 夕方の明るく居心地のよい日本の公立図書館の館内。卓上ランプの並ぶ長い学習机で大人がノートパソコンやノートに向かい、隅には小さなカフェのカウンターとコーヒーマシンと丸いテーブル、やわらかい肘掛け椅子でタブレットの電子書籍を読む人、背の高い木の本棚。温かいランプの光でくつろいだ雰囲気。机と人を画面いっぱいに置いて余白を作らない
board#f_board(left: 900px; top: 160px; width: 940px; height: 700px; delay: 400ms; in: {x:40, opacity:0, duration:.6, ease:'power2.out'})
  tab#tab 来ない人が欲しいサービス（非利用者・複数回答）
  div#s(left: 40px; top: "47;147;247;347"; width: 860px; height: 134px; border-radius: 22px; border: 3px solid #FFFBF300; delay: 200ms; in: {y:24, opacity:0, duration:.45, ease:'power2.out', stagger: {each: .13}}) ×4
    div#ib(left: 22px; cy: 50%; width: 84px; height: 84px; border-radius: 22px; background: $ibg)
      icon#i(cx: 50%; cy: 50%; font-size: 50px; name: "moon;device-tablet;desk;coffee"; color: $terra)
    p#n(left: 129px; top: 27px; font-size: 32px; line-height: 1.25) 夜間の開館{sm}（21時まで）{/};電子書籍の貸出;学習席・作業席;カフェ
    p#c(left: 129px; top: 72px; font-size: 22px; color: $ink2) 570人;471人;360人;298人
    # 棒の長さ = 値 ÷ 50 × 帯の幅 (hf の width 92% / 76% / 58% / 48%)
    div#tr(left: 482px; cy: 50%; width: 183px; height: 26px; border-radius: 14px; background: $track)
      div#b(left: 0px; top: 0px; width: "112;93;71;59"; height: 26px; border-radius: 14px; background: $terra; delay: 150ms; in: {scaleX:0, duration:.8, ease:'power3.out', pivot:'left'})
    p#p(right: 22px; cy: 50%; font-size: 62px; font-family: s; line-height: 1; color: $terra) 46{pc}%{/};38{pc}%{/};29{pc}%{/};24{pc}%{/}
#f_board.s.hl(border: 3px solid $terra; background: $hlbg; move: 350ms,none)

# gap — 06 利用者とのずれ: 0〜60% の軸に 5 行のダンベル図 (青緑 = 利用者・テラコッタ = 来ない人)・「新刊」の行から語で点・値・線を出し、残り 4 行を順に → 時間・行き方の行に札を付けて灯す・右に凡例と 2 枚の注記
section#gap(stagger: {each:0})
chap#ch6.sticky(n: "06"; t: "利用者とのずれ")
board#g_board(left: 80px; top: 160px; width: 1330px; height: 700px; delay: 400ms; in: {y:24, opacity:0, duration:.55, ease:'power2.out'})
  tab#tab 利用者と来ない人、望むものは同じ？（複数回答）
  div#hl(left: 40px; top: "55;130;205"; width: 1240px; height: 112px; background: #F4C46A38; in: {opacity:0, duration:.4, ease:'none'}; out: {opacity:0, duration:.4, ease:'none'}) ×3
  # 軸: 15% ごとの破線と上の目盛り (x = 313.7 + 値 × 8.89 px)
  shape#tk(left: "313;446;580;713;846"; top: 64px; width: 3px; height: 590px; path: line_v; border: 3px solid $tick; dash: 5,5; delay: 200ms; in: {opacity:0, duration:.5, ease:'none', stagger: {each: .05}}) ×5
  p#tl(cx: "313;446;580;713;846"; top: 26px; font-size: 22px; color: $ink2; delay: 200ms; in: {opacity:0, duration:.5, ease:'none', stagger: {each: .05}}) ×5 0%;15%;30%;45%;60%
  p#lb(left: 40px; top: "77;152;227;302;377"; font-size: 32px; delay: 300ms; in: {x:-20, opacity:0, duration:.4, ease:'power2.out', stagger: {each: .1}}) ×5 新刊を増やす;夜間の開館;電子書籍の貸出;学習席・作業席;カフェ
  p#tag_t(left: 210px; top: 231px; font-size: 22px; color: #FFFFFF; background: $amber; border-radius: 148px; padding: 4px 14px; in: {scale:.4, opacity:0, duration:.4, ease:'back.out(2.4)'}) 時間
  p#tag_i(left: 273px; top: 344px; font-size: 22px; color: #FFFFFF; background: $amber; border-radius: 148px; padding: 4px 14px; in: {scale:.4, opacity:0, duration:.4, ease:'back.out(2.4)'}) 行き方
  # 1 行目 (新刊を増やす): 語ごとに 利用者の点 → 52% → 395人 → 右から伸びる線 → 来ない人の点 → 18%
  div#r0_line(left: 711px; top: 135px; width: 453px; height: 6px; border-radius: 3px; background: $dline; in: {scaleX:0, duration:.6, ease:'power2.inOut', pivot:'right'})
  div#r0_u(left: 1144px; top: 118px; width: 40px; height: 40px; border-radius: 148px; background: $teal; border: 4px solid $paper2; box-shadow: 0px 4px 10px #3C281433; in: {scale:0, duration:.45, ease:'back.out(2.5)'})
  div#r0_n(left: 690px; top: 118px; width: 40px; height: 40px; border-radius: 148px; background: $terra; border: 4px solid $paper2; box-shadow: 0px 4px 10px #3C281433; in: {scale:0, duration:.45, ease:'back.out(2.5)'})
  p#r0_uv(cx: 1164px; top: 74px; font-size: 34px; font-family: s; line-height: 1; color: $teal; in: {y:10, opacity:0, duration:.35, ease:'power2.out'}) 52%
  p#r0_nv(cx: 711px; top: 74px; font-size: 34px; font-family: s; line-height: 1; color: $terra; in: {y:10, opacity:0, duration:.35, ease:'power2.out'}) 18%
  p#r0_cnt(cx: 1164px; top: 162px; font-size: 21px; color: $teal; in: {y:-6, opacity:0, duration:.35, ease:'power2.out'}) 395人
  # 2〜5 行目 (語の 550 ms 後から 160 ms ずつ: 点 2 つ → 線 → 値)
  div#r(left: 450px; top: "130;205;280;355"; width: 880px; height: 112px) ×4
    div#ln(left: "289.3;209.3;271.5;120.4"; top: 52px; width: "133.3;142.2;53.3;106.6"; height: 6px; border-radius: 3px; background: $dline; delay: 50ms; in: {scaleX:0, duration:.45, ease:'power2.out', pivot:'left'})
    div#du(left: "275.8;195.8;311.3;106.9"; top: 35px; width: 40px; height: 40px; border-radius: 148px; background: $teal; border: 4px solid $paper2; box-shadow: 0px 4px 10px #3C281433; in: {scale:0, duration:.4, ease:'back.out(2.2)'})
    div#dn(left: "409.1;338;258;213.5"; top: 35px; width: 40px; height: 40px; border-radius: 148px; background: $terra; border: 4px solid $paper2; box-shadow: 0px 4px 10px #3C281433; delay: 60ms; in: {scale:0, duration:.4, ease:'back.out(2.2)'})
    p#vu(cx: "289.3;209.3;324.8;120.4"; top: -9px; font-size: 34px; font-family: s; line-height: 1; color: $teal; delay: 150ms; in: {opacity:0, duration:.3, ease:'none'}) 31%;22%;35%;12%
    p#vn(cx: "422.6;351.5;271.5;227"; top: -9px; font-size: 34px; font-family: s; line-height: 1; color: $terra; delay: 150ms; in: {opacity:0, duration:.3, ease:'none'}) 46%;38%;29%;24%
card#g_leg(left: 1450px; top: 160px; width: 390px; height: 130px; delay: 800ms; in: {x:30, opacity:0, duration:.5, ease:'power2.out'})
  div#c(left: 26px; top: "21;55"; width: 24px; height: 24px; border-radius: 148px; background: "$teal;$terra") ×2
  p#t(left: 62px; top: "16;50"; font-size: 26px) ×2 利用者（760人）;来ない人（1,240人）
board#g_n1(left: 1450px; top: 315px; width: 390px; height: 172px; border: 3px solid $line; border-radius: 22px; in: {x:30, opacity:0, duration:.5, ease:'power2.out'})
  div#mk(left: g_n1.t.chars(17,24).left; top: g_n1.t.chars(17,24).top+24; width: 196px; height: 16px; background: $mark)
  p#t(left: 26px; top: 22px; width: 339px; font-size: 28px; line-height: 1.5) 今来ている人の[br]声だけを聞くと、[br]「本を増やす」方へ寄る
board#g_n2(left: 1450px; top: 510px; width: 390px; height: 172px; border: 3px solid $amber; border-radius: 22px; in: {x:30, opacity:0, duration:.5, ease:'power2.out'})
  div#mk(left: "g_n2.t.chars(5,9).left;g_n2.t.chars(11,16).left"; top: "g_n2.t.chars(5,9).top+26;g_n2.t.chars(11,16).top+24"; width: "73;92"; height: 16px; background: $mark) ×2
  p#t(left: 26px; top: 22px; width: 339px; font-size: 28px; line-height: 1.5) 来ない人の「時間」と[br]「行き方」が[br]見えなくなる
# 夜の場面への暗転 (前半): 夜の色の幕を台詞の後の間で濃くする (後半は trial の頭で引く)
veil#g_dip(color: $night; opacity: 1; z-index: curtain; in: {opacity:0, duration:.2, ease:'power1.in'})

# trial — 07 試しにやってみた: 夜の駅前分館の写真 (左を夜の色で沈め、灯りのぼけが昇る)・題と時刻の帯 (これまで 19 時 → 延長した 2 時間が伸びる) → 来館と新しい利用カードの前後の横棒を数え、倍率の札を弾ませる
section#trial(stagger: {each:0})
chap#ch7.sticky(n: "07"; t: "試しにやってみた")
img#h_img(inset: 0; content: @station; main: kb {scale: [1.14, 1.02], focus: ['64% 50%', '70% 50%'], ease:'sine.inOut'})
div#h_shade(inset: 0; background: linear(#141B32F2,#141B32E6@44%,#141B3273@62%,#141B320D@80%,90))
# 灯りのぼけ 16 個 (hf の種つき乱数の位置・場面の尺で昇りながら灯る)
div#h_bk.bleed(left: "971.3;971.6;1055.5;879.5;1159.9;687.1;861.7;1145.5;969;680.4;865.1;986.2;1027.5;1031.3;962;701.2"; top: "342.8;351;412.6;355.2;450.4;399.2;310.8;242.6;145.5;242;2;171.5;66.5;204.7;2;427.7"; width: "57.5;25.9;50.8;49;50.7;38.5;74.5;82.3;56.5;67.2;54.2;42;66.2;82.5;42.6;29.1"; height: "57.5;25.9;50.8;49;50.7;38.5;74.5;82.3;56.5;67.2;54.2;42;66.2;82.5;42.6;29.1"; border-radius: 148px; background: radial(#FFD68C8C,#FFD68C2E@45%,#FFD68C00@70%,50%,50%); opacity: "0.78;0.59;0.44;0.65;0.51;0.50;0.77;0.39;0.72;0.84;0.56;0.43;0.54;0.64;0.50;0.61"; delay: "807ms;1265ms;414ms;864ms;934ms;219ms;214ms;1261ms;133ms;642ms;1139ms;177ms;1405ms;652ms;612ms;155ms"; in: {y:60, opacity:0, duration:19, ease:'sine.inOut'}) ×16
p#h_chip(left: 90px; top: 144px; font-size: 24px; color: $night; background: $lamp; border-radius: 148px; padding: 8px 20px; delay: 400ms; in: {y:16, opacity:0, duration:.45, ease:'power2.out'}) 試行
p#h_title(left: 90px; top: 210px; font-size: 60px; font-family: s; line-height: 1.25; color: $cream; in: {x:-40, opacity:0, duration:.7, ease:'expo.out'}) 駅前分館で、平日を{lp}21時{/}まで
p#h_sub(left: 90px; top: 291px; font-size: 28px; color: $sand; in: {opacity:0, duration:.5, ease:'none'}) 7〜9月の3か月間（分館 1か所）
# 時刻の帯: 地の帯 + これまでの斜線 + 延長した 2 時間 (左から伸びて光る)・16〜22 時の目盛り (19 時と 21 時は灯りの色)
div#h_ruler(left: 90px; top: 360px; width: 960px; height: 110px)
  div#track(left: 0px; top: 40px; width: 960px; height: 30px; border-radius: 15px; background: #FFF4DF1F; in: {opacity:0, duration:.5, ease:'none'})
  div#open(left: 0px; top: 40px; width: 480px; height: 30px; background: #FFF4DF4D; pattern: hatch,45,#FFF4DF80,13,7; in: {opacity:0, duration:.5, ease:'none'})
  # engine: hf は延長の帯の光 (影) を 0.9 秒周期で 8 回強める — 繰り返しの tween に影の強さは書けないので静止の光
  div#ext(left: 480px; top: 40px; width: 320px; height: 30px; border-radius: 0px 15px 15px 0px; background: $lamp; box-shadow: 0px 0px 26px #F4C46ABF; in: {scaleX:0, duration:1, ease:'power2.inOut', pivot:'left'})
  p#tk(cx: "0;107;213;320;427;533;640"; top: 82px; font-size: "15;15;15;17;15;17;15"; color: "$sand;$sand;$sand;$lamp;$sand;$lamp;$sand"; in: {opacity:0, duration:.5, ease:'none', stagger: {each: .03}}) ×7 16時;17時;18時;19時;20時;21時;22時
  p#old(left: 250px; top: 0px; font-size: 22px; color: $sand; in: {y:10, opacity:0, duration:.4, ease:'power2.out'}) これまで
  p#new(left: 560px; top: 0px; font-size: 24px; color: $lamp; in: {x:-14, opacity:0, duration:.45, ease:'power2.out'}) 延長した 2時間
# 前後の横棒の組 (題 → 延長前 → 延長後 → 倍率の札)・棒の長さ = 延長後を 313 px とした比
def hrow(l, w, c, v, u, vc) = div(left: 0px; width: 840px; height: 54px; in: {opacity:0, duration:.3, ease:'none'})
  p#l(left: 0px; cy: 50%; font-size: 22px; color: $sand; content: {l})
  div#b(left: 110px; cy: 50%; width: {w}; height: 38px; border-radius: 0px 10px 10px 0px; background: {c}; delay: 100ms; in: {scaleX:0, duration:.7, ease:'power3.out', pivot:'left'})
  p#v(left: .b.right+16; cy: 50%; font-size: 40px; font-family: s; line-height: 1; color: {vc}; content: {v}{hu}{u}{/})
def badge(v, s) = div(left: 900px; top: 40px; width: 230px; height: 124px; border-radius: 22px; background: $cream; box-shadow: 0px 0px 40px #F4C46A73; in: {scale:.4, rotation:-10, opacity:0, duration:.55, ease:'back.out(2.2)'})
  p#b(cx: 50%; top: 16px; font-size: 68px; font-family: s; line-height: 1; color: $rust; content: {v})
  p#s(cx: 50%; top: 82px; font-size: 22px; color: $night; content: {s})
div#h_c1(left: 90px; top: 500px; width: 1130px; height: 180px)
  div#t(left: 0px; top: 0px; width: 600px; height: 42px; in: {x:-20, opacity:0, duration:.45, ease:'power2.out'})
    icon#i(left: 0px; cy: 50%; font-size: 33px; name: users; color: $lamp)
    p#t(left: 46px; cy: 50%; font-size: 28px; color: $cream) 19時以降の来館（月平均）
  hrow#ra(top: 52px; l: "延長前"; w: 135; c: "#FFF4DF73"; v: "[count:1,240 start=0 ms=800ms delay=100ms]"; u: "人"; vc: $cream)
  hrow#rb(top: 117px; l: "延長後"; w: 313; c: $lamp; v: "[count:2,890 start=0 ms=1100ms delay=100ms]"; u: "人"; vc: $lamp)
    div#b(box-shadow: 0px 0px 22px #F4C46A80; in: {scaleX:0, duration:1.1, ease:'power3.out', pivot:'left'})
  badge#badge(v: "2.3{bx}倍{/}"; s: "＋1,650人")
div#h_c2(left: 90px; top: 700px; width: 1130px; height: 180px)
  div#t(left: 0px; top: 0px; width: 600px; height: 42px; in: {x:-20, opacity:0, duration:.45, ease:'power2.out'})
    icon#i(left: 0px; cy: 50%; font-size: 33px; name: identification-card; color: $lamp)
    p#t(left: 46px; cy: 50%; font-size: 28px; color: $cream) 新しく作られた利用カード（月）
  hrow#ra(top: 52px; l: "延長前"; w: 107; c: "#FFF4DF73"; v: "38"; u: "枚"; vc: $cream)
  hrow#rb(top: 117px; l: "延長後"; w: 313; c: $lamp; v: "[count:112 start=0 ms=1000ms delay=100ms]"; u: "枚"; vc: $lamp)
    div#b(box-shadow: 0px 0px 22px #F4C46A80; in: {scaleX:0, duration:1, ease:'power3.out', pivot:'left'})
  badge#badge(v: "{bx}約{/}2.9{bx}倍{/}"; s: "38枚 → 112枚"; in: {scale:.4, rotation:10, opacity:0, duration:.55, ease:'back.out(2.2)'})
# 暗転 (後半): 頭は夜の色で覆い、最初の台詞の頭で引く
veil#h_dip(color: $night; opacity: 1; z-index: curtain; in: none)

# summary — 08 まとめ: 夜の色の結論の帯 (右上に灯りの光が脈打つ・「行ける時間と手段を増やす」の下に帯が伸びる) → 番号つきの札 3 枚 → 3 枚目に次の一手 2 つを語でチェック
section#summary(stagger: {each:0})
chap#ch8.sticky(n: "08"; t: "まとめ")
div#i_shadow(left: 80px; top: 140px; width: 1760px; height: 190px; border-radius: 30px; background: $night; box-shadow: 0px 20px 44px #1B244040; delay: 300ms; in: {y:-30, opacity:0, duration:.6, ease:'power3.out'})
group#i_banner(left: 80px; top: 140px; width: 1760px; height: 190px; clip: 20,i_banner.bg; delay: 300ms; in: {y:-30, opacity:0, duration:.6, ease:'power3.out'})
  div#bg(left: 0px; top: 0px; width: 1760px; height: 190px; border-radius: 30px; background: $night)
  div#glow(left: 1362px; top: -118px; width: 476px; height: 476px; border-radius: 148px; background: radial(#F4C46A6B,#F4C46A00@65%,#F4C46A00,50%,50%); opacity: .6)
p#i_tag(left: 129px; top: 170px; font-size: 24px; color: $night; background: $lamp; border-radius: 148px; padding: 6px 18px; delay: 600ms; in: {x:-20, opacity:0, duration:.4, ease:'power2.out'}) 結論
p#i_b1(left: 129px; top: 252px; font-size: 44px; font-family: s; line-height: 1.5; color: $sand; in: {y:20, opacity:0, duration:.5, ease:'power2.out'}) 「本を増やす」より先に、
# 結論の下の帯: run の marker の帯は行の頭 +1.02 字が下端で字の下 1/3 に掛かる — hf の帯 (字面の下端に触れて下へ) は文字の underline の印 (字の下 +1.02 字から 0.3 字・地の 40%) で、line-height 1.15 で字面の下端に触れる
p#i_b2(left: i_b1.right+24; top: 234px; font-size: 70px; font-family: s; line-height: 1.15; color: $cream; in: {y:20, opacity:0, duration:.6, ease:'power3.out'}) 「行ける時間と手段を増やす」
def pt(n, h, d) = div(left: 80px; width: 1760px; height: 129px; background: $paper2; border-radius: 26px; box-shadow: 0px 18px 42px #5C3E1E21; in: {x:-50, opacity:0, duration:.55, ease:'power3.out'})
  div#n(left: 34px; top: 22px; width: 62px; height: 62px; border-radius: 18px; background: $ink)
    p#t(cx: 50%; cy: 50%; font-size: 34px; font-family: s; line-height: 1; color: $paper2; content: {n})
  p#h(left: 122px; top: 20px; font-size: 34px; line-height: 1.35; content: {h})
  p#d(left: 122px; top: 70px; font-size: 26px; line-height: 1.5; color: $ink2; content: {d})
pt#pt1(top: 360px; n: "1"; h: "回答した市民の{t}6割（62%）{/}は、この1年 図書館を使っていない"; d: "いちばんの理由は本ではなく「開いている時間に行けない」（41%）")
pt#pt2(top: 506px; n: "2"; h: "来ない人の期待（夜間・電子書籍・カフェ）は、今の利用者とずれている"; d: "利用者の声だけで、次の手を決めない")
div#pt3(left: 80px; top: 651px; width: 1760px; height: 168px; background: $paper2; border: 3px solid $amber; border-radius: 26px; box-shadow: 0px 18px 42px #5C3E1E21; in: {y:30, opacity:0, duration:.6, ease:'back.out(1.3)'})
  div#n(left: 34px; top: 22px; width: 62px; height: 62px; border-radius: 18px; background: $amber)
    p#t(cx: 50%; cy: 50%; font-size: 34px; font-family: s; line-height: 1; color: $paper2) 3
  p#h(left: 122px; top: 20px; font-size: 34px; line-height: 1.35) 市の次の一手
  # 次の一手の札 (チェックの枠 + 語で描くチェック + 文)
  div#a(left: "81;576"; top: 81px; width: "480;271"; height: 64px; border-radius: 16px; background: $actbg; in: {x:-20, opacity:0, duration:.45, ease:'power2.out'}) ×2
    div#bx(left: 14px; cy: 50%; width: 44px; height: 44px; border-radius: 12px; border: 3px solid $amber; background: $paper2)
    icon#ck(left: 20px; cy: 50%; font-size: 32px; name: check; weight: bold; color: $amber; in: draw {duration: 0.5})
    p#t(left: 70px; cy: 50%; font-size: 28px) 駅前分館の夜間開館を続け、ほかの分館へ広げる;電子書籍の貸出を始める

# end — 締め: 夜の駅前分館の写真に寄りから引き、左に題の 2 行 → 罫 → 主催 → 2 人の顔 → 注記・最後に夜の色へ溶ける
section#end(stagger: {each:0})
img#end_img(inset: 0; content: @station; main: kb {scale: [1.16, 1.04], focus: ['55% 50%', '55% 50%'], ease:'sine.out'})
div#end_shade(inset: 0; background: radial(#141B32E0,#141B3299@55%,#141B3226,26%,52%))
div#end_bk.bleed(left: "644.6;1220;1243.8;1028.1;1111.6;1099.9;741.9;1021.6;705.3;946.4;732;719.7;1142.6;1032.9"; top: "374.3;508.4;488.7;591.9;64.7;495.5;168.8;149.8;367.6;442.3;396.9;73.2;402.3;378.6"; width: "26.8;57.6;26.3;53.2;34;89.4;72;79.4;78.8;62.7;20.8;70.9;25.1;32.2"; height: "26.8;57.6;26.3;53.2;34;89.4;72;79.4;78.8;62.7;20.8;70.9;25.1;32.2"; border-radius: 148px; background: radial(#FFD68C8C,#FFD68C2E@45%,#FFD68C00@70%,50%,50%); opacity: "0.51;0.70;0.72;0.77;0.54;0.67;0.80;0.45;0.74;0.50;0.64;0.63;0.70;0.56"; delay: "321ms;313ms;82ms;345ms;763ms;1217ms;1427ms;591ms;7ms;78ms;1406ms;460ms;34ms;360ms"; in: {y:60, opacity:0, duration:5.5, ease:'sine.inOut'}) ×14
p#end_l1(left: 140px; top: 270px; font-size: 96px; font-family: s; line-height: 1.3; color: $cream; delay: 300ms; in: {y:30, opacity:0, duration:.7, ease:'power3.out'}) 夜の図書館でも、
p#end_l2(left: 140px; top: 394px; font-size: 96px; font-family: s; line-height: 1.3; color: $lamp; delay: 1450ms; in: {y:30, opacity:0, duration:.8, ease:'power3.out'}) お待ちしています。
div#end_rule(left: 140px; top: 549px; width: 420px; height: 4px; border-radius: 3px; background: $lamp; delay: 2200ms; in: {scaleX:0, duration:.8, ease:'power2.inOut', pivot:'left'})
p#end_org(left: 140px; top: 580px; font-size: 30px; letter-spacing: .05em; color: $org; delay: 2500ms; in: {opacity:0, duration:.6, ease:'none'}) みなと野市立図書館 ｜ みなと野学園大学 研究室
img#end_mori(left: 140px; top: 654px; width: 84px; height: 84px; border-radius: 148px; box-shadow: 0px 0px 0px 3px #FFF4DFCC; content: @mori; object-fit: cover; object-position: 50% 25%; main: none; delay: 2700ms; in: {scale:.6, opacity:0, duration:.45, ease:'back.out(2)'})
img#end_takagi(left: 246px; top: 654px; width: 84px; height: 84px; border-radius: 148px; box-shadow: 0px 0px 0px 3px #FFF4DFCC; content: @takagi; object-fit: cover; object-position: 50% 25%; main: none; delay: 2850ms; in: {scale:.6, opacity:0, duration:.45, ease:'back.out(2)'})
p#end_foot(left: 140px; top: 988px; font-size: 21px; color: $foot; delay: 3000ms; in: {opacity:0, duration:.6, ease:'none'}) ※ みなと野市・みなと野学園大学は架空の名称です。数値は市民調査（回答者 2,000人）より。
veil#fade_out(color: $deep; opacity: 1; z-index: curtain; in: {opacity:0, duration:.9, ease:'power1.in'})
```

```timeline.txt
#v2
cast mori = "落ち着いたトーンで明るく親しみやすい、30歳前後の大人の女性の声。クリアではきはきした発音で丁寧" manner="やわらかく温かい、親しみのある口調で" label="森｜図書館 職員" label_fill=#FFFBF300 label_color=$mori
cast takagi = "落ち着いたトーンで温かみと安心感のある、30〜40代の大人の男性の声。滑舌がよく明瞭で、語りかけるよう" manner="落ち着いて温かい、やさしい口調で" label="高木｜大学 研究者" label_fill=#FFFBF300 label_color=$takagi
silence head=0ms tail=0ms

# title — 頭に題札が組み上がり、名乗りの語で出演者の札・字幕の帯は最初の台詞の 200 ms 前
*** title
[>#subtitle]
bgm music
se riffle -5dB +100ms
@mori: [silence:0.8s][>#subbar -200ms][spk #subbar.av_mori #subbar.av_takagi -50ms][>#cast_mori +250ms][♪pop -6dB +250ms]みなと野市立図書館の森です。[silence:0.14s]
@: [!#a_q to,{rotation:8, duration:.5, ease:'sine.inOut', repeat:5, yoyo:true} -540ms]来ない人は、図書館に何を求めているのか。[silence:0.26s]
@takagi: [spk #subbar.av_takagi #subbar.av_mori -50ms][>#cast_takagi +120ms][♪pop -6dB +120ms]調査した、みなと野学園大学の高木です。[silence:0.21s]
# 紙がめくれる切替: 新しい頁が右から現れ、紙の縁の陰と光の帯が左へ走る (hf は旧場面も 60 px 左へずれる — 省いた)
transition wipe {duration: .75, dir: 'left', overlap: .6, ease: 'power2.inOut', bars: 'linear(#3C281400,#3C281438@55%,#FFFCF5E6@70%,#3C28141F),93'} se=page -4dB

# survey — 頭で常設の上端と写真・事実の行・板・「4,000」「2,000」で数え、「50%」の手前で輪の弧
*** survey
@mori: [silence:0.21s][>#ch1 +140ms][>#hdr_r +140ms][>#hdr_r.seg[1].fill +240ms][spk #subbar.av_mori #subbar.av_takagi -50ms]市民[>#b_board.send -200ms][♪pop -6dB -150ms]4,000人に、調査票を送りました。[silence:0.26s]
@takagi: [spk #subbar.av_takagi #subbar.av_mori -50ms]回答は[>#b_board.arrow -600ms][>#b_board.back -200ms][♪pop -6dB -150ms]2,000人、回収率は[>#b_board.ring -1100ms][>#b_board.ring.arc -900ms][>#b_board.note +200ms][♪bell -5dB +50ms]50%です。[silence:0.21s][<#ch1 cut-0ms]
transition dissolve {duration: .5, overlap: .25}

# used — 最初の語で waffle の 38 マスを塗り、「38%」の手前で札・2 行目の頭で残り 62 マス・「62%」で札と判子
*** used
@mori: [silence:0.21s][>#ch2 +140ms][>#hdr_r.seg[2].fill +240ms][spk #subbar.av_mori #subbar.av_takagi -50ms][>#c_wu -210ms][>#c_wn -210ms][!#c_wu .on {stagger: {each: .026}} +240ms][♪riffle -10dB +240ms]この1年に図書館を使った方は、[>#c_use -500ms][♪pop2 -7dB -100ms]38%。[silence:0.26s]
@takagi: [spk #subbar.av_takagi #subbar.av_mori -50ms][!#c_wn .on {stagger: {each: .018}} +50ms][♪riffle -10dB +50ms]残る[>#c_non -400ms][>#c_non.stamp +500ms][♪pop -6dB +450ms][!#c_non.stamp to,{rotation:1, duration:.9, ease:'sine.inOut', repeat:1, yoyo:true} +1000ms][>#c_note +900ms]62%は、一度も来ていません。[silence:0.21s][<#ch2 cut-0ms]
transition push {duration: .7, dir: 'left', overlap: .5, ease: 'power3.inOut'}

# age — 頭で縦棒が立ち上がり (棒ごとの小さな音 3 つ)・「26%」で 20 代を縁取り脈打たせる・2 行目で括弧と 4 割の破線・「40代」で親子の札・「4割」で 3 本が跳ねる
*** age
@takagi: [silence:0.21s][>#ch3 +140ms][>#hdr_r.seg[3].fill +240ms][♪pop2 -7dB +240ms][♪pop2 -7dB +540ms][♪pop2 -7dB +840ms]いちばん低いのは20代、[>#d_low -100ms][♪pop -6dB -50ms][!#d_board.col[2].bar .halo][!#d_board.col[2].bar to,{opacity:.82, duration:.8, ease:'sine.inOut', repeat:3, yoyo:true} +600ms][>#d_hi +700ms]26%です。[silence:0.26s]
@mori: [spk #subbar.av_mori #subbar.av_takagi -50ms][>#d_board.bracket +100ms][>#d_board.blabel +100ms][>#d_board.d40 +250ms][♪pencil -5dB +250ms][>#d_board.d40l +900ms]働く世代は、[>#d_40 +100ms][♪pop -6dB +100ms]40代をのぞいて[!#d_board.col[2] to,{y:-6, duration:.25, ease:'power1.out', repeat:1, yoyo:true}][!#d_board.col[3] to,{y:-6, duration:.25, ease:'power1.out', repeat:1, yoyo:true} +100ms][!#d_board.col[5] to,{y:-6, duration:.25, ease:'power1.out', repeat:1, yoyo:true} +200ms]4割に届きません。[silence:0.21s][<#ch3 cut-0ms]
transition wipe {duration: .75, dir: 'left', overlap: .6, ease: 'power2.inOut', bars: 'linear(#3C281400,#3C281438@55%,#FFFCF5E6@70%,#3C28141F),93'} se=page -4dB

# reasons — 問いの行で 2〜5 位を先に伸ばし「1位は…？」・答えの行で 1 位の行が伸びて「41%」で値と地・「本」で本の 2 行を薄めて結論・「時間」で時計を回す
*** reasons
@mori: [silence:0.21s][>#ch4 +140ms][>#hdr_r.seg[4].fill +240ms][>#e_board.r[*] {stagger:{each:0.16}} +200ms][>#e_board.btag[1] +200ms][>#e_board.btag[2] +360ms][>#e_board.q +200ms][♪pop2 -7dB +250ms][♪pop2 -7dB +650ms]来ない理由のトップは？[silence:0.26s]
@takagi: [spk #subbar.av_takagi #subbar.av_mori -50ms][<#e_board.q -50ms][>#e_board.top.lab +50ms][>#e_board.top.b +250ms][♪tick -4dB +100ms]「開いている時間に行けない」。[||][>#e_board.top.v -100ms][>#e_board.hl][♪pop -6dB]41%です。[silence:0.26s]
@mori: [spk #subbar.av_mori #subbar.av_takagi -50ms][!#e_board.r[1] to,{opacity:.45, duration:.4, ease:'none'}][!#e_board.r[2] to,{opacity:.45, duration:.4, ease:'none'}][!#e_board.btag[1] to,{opacity:.45, duration:.4, ease:'none'}][!#e_board.btag[2] to,{opacity:.45, duration:.4, ease:'none'}][>#e_board.sum -50ms][♪pencil -5dB +50ms]本ではなく、[!#e_board.top.lab.i to,{rotation:360, duration:.8, ease:'back.out'} -200ms]時間なんですね。[silence:0.21s][<#ch4 cut-0ms]
transition dissolve {duration: .5, overlap: .25}

# wants — 頭で写真の札と板と 4 行・「夜9時」「電子書籍」で行を灯し、「46%」「38%」で値を弾ませる
*** wants
@takagi: [silence:0.21s][>#ch5 +140ms][>#hdr_r.seg[5].fill +240ms][spk #subbar.av_takagi #subbar.av_mori -50ms]欲しいのは、[!#f_board.s[1] .hl -50ms][♪pop -6dB -50ms]夜9時までの開館が[!#f_board.s[1].p to,{scale:1.18, duration:.25, ease:'power2.out', repeat:1, yoyo:true}]46%、[|][!#f_board.s[2] .hl -50ms][♪pop -6dB -50ms]電子書籍が[!#f_board.s[2].p to,{scale:1.18, duration:.25, ease:'power2.out', repeat:1, yoyo:true}]38%。[silence:0.21s][<#ch5 cut-0ms]
transition push {duration: .7, dir: 'left', overlap: .5, ease: 'power3.inOut'}

# gap — 「新刊」で 1 行目を灯して利用者の点・「52%」で値と人数・「18%」で線と来ない人の点 → 残り 4 行を 160 ms ずつ・森の行で注記・「時間」「行き方」で札と地・台詞の後の間で夜の色へ暗転
*** gap
@takagi: [silence:0.21s][>#ch6 +140ms][>#hdr_r.seg[6].fill +240ms]ところが、今の利用者の一番は[|]「[>#g_board.hl[1] -200ms][>#g_board.r0_u -50ms][♪pop -6dB -50ms]新刊を増やす」で、[>#g_board.r0_uv -100ms][>#g_board.r0_cnt +100ms]52%。[silence:0.14s]
@: 来ない人では、[>#g_board.r0_line -300ms][>#g_board.r0_n -50ms][♪pop -6dB -50ms][>#g_board.r0_nv][>#g_board.r[*] {stagger:{each:0.16}} +550ms][♪pop2 -7dB +600ms]18%です。[silence:0.26s]
@mori: [spk #subbar.av_mori #subbar.av_takagi -50ms][>#g_n1 +100ms][<#g_board.hl[1] +1600ms]今の利用者の声だけでは、[|]来ない人の「[>#g_board.tag_t -50ms][>#g_board.hl[2] -50ms][♪pencil -5dB -50ms][>#g_n2 +200ms]時間」と「[>#g_board.tag_i -50ms][>#g_board.hl[3] -50ms][♪pencil -5dB -50ms]行き方」が見えないんですね。[silence:0.01s][>#g_dip][♪page -4dB][silence:0.2s][<#ch6 cut-0ms]
transition cut

# trial — 頭で夜の色を引き、「駅前」で題と時刻の帯・「夜9時」で延長の 2 時間が伸びる → 来館の 2 本を数え「2.3倍」で札 → カードの 2 本と「約2.9倍」
*** trial
@mori: [silence:0.21s][!#h_dip to,{opacity:0, duration:.7, ease:'power1.out'} -90ms][>#ch7 +140ms][>#hdr_r.seg[7].fill +240ms]そこで[>#h_title -300ms][>#h_ruler.track +600ms][>#h_ruler.open +630ms][>#h_ruler.tk[*] +660ms][>#h_ruler.old +1000ms][>#h_sub +1200ms]駅前分館で、7月から3か月、[|]平日を[>#h_ruler.ext -100ms][♪tick -4dB +100ms][>#h_ruler.new +600ms]夜9時まで開けました。[silence:0.26s]
@takagi: [spk #subbar.av_takagi #subbar.av_mori -50ms][>#h_c1.t -100ms]19時以降の来館は、[|]月平均[>#h_c1.ra -400ms][♪pop2 -7dB -50ms]1,240人から[>#h_c1.rb -400ms][♪pop -6dB -50ms]2,890人へ。[silence:0.14s]
@: [>#h_c1.badge -100ms][♪sparkle -3dB -80ms]2.3倍です。[silence:0.26s]
@mori: [spk #subbar.av_mori #subbar.av_takagi -50ms][>#h_c2.t -50ms]新しい利用カードも、月[>#h_c2.ra -400ms][♪pop2 -7dB -50ms]38枚から[>#h_c2.rb -400ms][♪pop -6dB -50ms][>#h_c2.badge +350ms]112枚に。[silence:0.21s][<#ch7 cut-0ms]
transition dissolve {duration: .7, overlap: .45, zoom: 1.04, ease: 'power2.out'} se=page -4dB

# summary — 頭で結論の帯と光・1 行目で前置きと札 1・2・「行ける」で主文と下の帯 → 2 行目で札 3 と次の一手 1 (チェック)・3 行目で次の一手 2・最後に常設の層を閉じる
*** summary
@takagi: [silence:0.21s][>#ch8 +140ms][>#hdr_r.seg[8].fill +240ms][spk #subbar.av_takagi #subbar.av_mori -50ms][♪pop -6dB +100ms][!#i_banner.glow to,{scale:1.29, opacity:1, duration:3, ease:'sine.inOut', repeat:3, yoyo:true} -210ms][>#i_b1 +100ms][>#pt1 +500ms][>#pt2 +750ms]本を増やすより先に、[>#i_b2 -250ms][!#i_b2 underline,$lamp +300ms][♪pencil -5dB -50ms]行ける時間と手段を増やす。[silence:0.26s]
@mori: [spk #subbar.av_mori #subbar.av_takagi -50ms][>#pt3 -100ms][!#pt1 to,{opacity:.72, duration:.5, ease:'none'} +200ms][!#pt2 to,{opacity:.72, duration:.5, ease:'none'} +200ms]次の一手は、[>#pt3.a[1] -300ms][>#pt3.a[1].ck +400ms][♪pencil -5dB -50ms]駅前分館の夜間開館を続けて、[|]ほかの分館へ広げること。[silence:0.14s]
@: そして、[>#pt3.a[2] -300ms][>#pt3.a[2].ck +400ms][♪pencil -5dB -50ms]電子書籍の貸出を始めることです。[silence:0.04s]
[<#subtitle]
[<#subbar cut-0ms][<#hdr_r cut-0ms][<#ch8 cut-0ms]
transition dissolve {duration: .8, overlap: .8} se=riffle -9dB

# end — 夜の写真に題を再掲 (字幕なし)・声の後 2.1 秒で夜の色へ 0.9 秒で溶ける
*** end
@mori: [silence:0.1s]夜の図書館でも、お待ちしています。[silence:2.1s][>#fade_out][silence:0.9s]
```

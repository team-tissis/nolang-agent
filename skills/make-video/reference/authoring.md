# 文法 (timeline.txt + design.txt) — draft src v2

正本は `docs/draft_src_v2/grammar-spec.md` (規則) と `grammar-spec-types.md` (型ごとの全 key・preset・やり方・形の名)。この辞書は著者向けの写し。型は raw の要素 (文字・箱・絵・icon・図形・幕・群) だけで、札の行・横棒・流れ図は根の `def` + `×N` で書く (下の「根の雛形」)。runtime の field ごとの書き方と書けない物は `capabilities.md`。
`src/` = `timeline.txt` (台詞・音・印 = いつ) + `design.txt` (要素・既定・palette = なに) + `src.json` (出力の設定・素材の pin)。両 file の 1 行目は `#v2` ちょうど (DEFECT:VERSION)。
短く書く順: 2 回以上書く物は根に 1 回 (`palette` `default` `def` `cast` `transition =`) → section はその場面の差分だけ。

## HTML 形 (著者が書く綴り)

design の要素は `tag#id.class(css 宣言) 内容` で書く (= HTML / CSS / GSAP の圧縮形。閉じタグは字下げ・style は要素の行・gsap.from は `in:{…}`・秒は台詞の語)。
この辞書の key は v2 の綴り (`[型 名] key=値`) で載っているが、CSS の名と単位でそのまま書ける: `left top width height` (= `left top w h`・px・`x y` は GSAP の移動量だけ)・`background` (= fill)・`border: 3px solid $a` (= `border=$a,3`)・
`border-radius` (= radius)・`box-shadow: 0 4px 12px #0003` (= `shadow=0,4,12,#0003`)・`font-size` (= size)・`font-family` (= font)・`letter-spacing: .2em`・`line-height`・`text-align` (= align)・`text-shadow: 0 4px 3px #0008`・
`transform: rotate(-5deg) scale(1.1)` (= rotation / scale)・`transform-origin` (= pivot)・`filter: saturate(.3) sepia(1)`・`mix-blend-mode` (= blend)・`display:flex; gap:24px` (= `stack=h`)・`flex: 1` (= `flex=1` 残りを取る子)・`align-items` / `justify-content` (= 文字は `valign` / `align`・箱は子の寄せ `valign=center|bottom|between` `align=center|right|between` (`space-between` = between)・`flex-direction: column` は軸が逆)・`inset:0` (= `inset=0` 全面)・`z-index`。`div` の `padding` は書かなければ 0 (CSS と同じ)。
動きは GSAP の object: `in:{y:30, opacity:0, duration:.5, ease:'power3.out', stagger:{each:.12, from:'end'}}` (= `in=y=30,opacity=0,duration=500,ease=power3.out,stagger=120,from=end`・stagger は tween の object の中だけ — 1 つの文字なら 1 字ずつ・×N と群なら instance の間隔)・印は `[!#id to,{scale:1.1, duration:.4, yoyo:true}]`。
`section#名(宣言)` = `[cut 名]`・`#名.tag(宣言)` = 変種 `[名 .tag]`・`@#名` = 再掲 `[@名]`・`def 名(引数) = tag(宣言) 内容` = def・`img { main: kb,1.0>1.06 }` = `default image = …`。両方の綴りが同じ file に混ざってよい。

## 字句 (両 file 共通)
| 種 | 規則 | 例 | 違反 |
|---|---|---|---|
| 行 | 1 行 = 1 文。継続行なし。空行は無視。tab は欠陥。字下げは 2 空白 × 深さ (深さ +1 = 直前のより浅い section の子)。注記は行頭か空白の直後の `#` から行末 (文字列の中・色 `#RRGGBB` は注記でない) | `  [text .t]  # 子` | DEFECT:TAB / INDENT |
| 名 | `[a-z][a-z0-9_]*`。大文字は欠陥 (読み替えない・直し方に snake_case)。予約語 `cut screen self prev bg se subtitle` (根に書いた名の先頭だけ — 字下げの `.bg` は書ける・cut の名には掛からない)。派生: `親.子` (子は親と同じ cut に書く — 後で見せる子は後の cut の `[>親.子]`)・`名[k]` (×N の k 番目・k ≥ 1 — ×N の無い基底の `名[k]` は欠陥)・`名[*]`・`名[k].子`・文字の一部 `名{tok}` (印だけ)。先頭 `.` = 包む section (字下げの親・def の根) からの相対。名を省いた section は engine の自動名 `_cut名.型N` (`_` 先頭は書けない = 印で呼べない) | `org.l[2].c`・`[text .t]` = `box.t` | DEFECT:NAME |
| 数 | `12` `-3.5` `1.2s` `300ms` `40%` `30deg` `-6dB`。無単位 = slot の既定単位: 位置・寸法・移動 = px (`%` = 親の内側・根は canvas の比) / 時刻 (duration delay stagger ±N hold lead tail overlap fade start peak to silence) = ms / 角度 = deg / 比 (scale opacity level kb) = 無次元 / `letter_spacing` = 文字サイズ比。音量は必ず `dB`。長さは `48px` も可 (正準形は `48`)。`em` `pt` は書かない | `in=y=-44` `w=40%` `start=13.7s` | DEFECT:UNIT |
| 色 | `#RRGGBB` `#RRGGBBAA` `$名` (palette) `none`・`linear(色[@N%],…[,角度\|top\|right\|bottom\|left])`・`radial(色,…[,cx%,cy%[,rx%,ry%]])` | `linear(#000080,#00000000,180)` | DEFECT:COLOR |
| 文字列・列 | `"…"` だけ。逃げは `\"` `\\` `\;`。複数行は `"""` … `"""` (svg・長い prompt)。列は `;` 区切り (×N の instance ごと・rows の行)・行の中の cell は `\|` | `rows="a\|1;b\|2"` | DEFECT:QUOTE |
| 値つき語 | `種[,位置引数…][,key=値…]`。位置引数が先。`,` 区切り・値の中に空白なし (空白は `"…"` と `keys(…)` の中だけ)。`key=値` は同じ key 2 回で欠陥。値の無い既知の語は flag (`hug sticky bleed arrow dash ellipse`・全面は `inset=0`) | `in=rise,20,550,ease=back(1.7)` | DEFECT:ARG / KEY_DUP / KEY |
| 式 | 位置 slot だけ `名.辺[±N]` (辺 = left top right bottom cx cy)。後ろの section も可。絵の中の点 `絵.mouth.x\|y[±N]` (口)・`絵.face.辺[±N]` (顔の箱) — 生成直後に測った点で解く (測る前の check は絵の `face=` の目安・info `mouth_provisional`) | `top=hdr.bottom+16`・吹き出し `p#say(left: pic.face.right+20; top: pic.mouth.y-40; width: 300px; background: #FFFFFF; padding: 12px 22px; shape: speech-bubble; pointer: pic.mouth)` (尻尾は板の辺から出る — 口の横か真上 / 真下に置くと口を指す) | DEFECT:REF |

根の定義 = section より前の行 (順は自由・同じ名の 2 定義は DEFECT:DUP_NAME)。名つきの `def svg sound motion run cue` は初めて使う cut の block (cut の頭の後) にも書ける — その cut の持ち物。他の根 (設定・`image default style use`・timeline の `cast read transition`) は `[cut]` の後なら DEFECT:ROOT_AFTER_CUT:
- `種 名 = 値` — design: `def` (後述)・`svg mark = """<svg viewBox=…>…</svg>"""` (viewBox 必須)・`sound pon = "ポンという音"` / `= id=8桁`・`image boss = "[photo]55歳の部長"` (`aspect=16:9` を足すと全面に敷く比率で作る・無ければ 1:1。根の絵は 1 度だけ作られ、比率の違う枠に置いても作り直されない — 切り抜きは `fit=contain`) / `= id=<uuid>` (自分の素材か NoLang の素材の画像・動画素材をそのまま使う — 生成しない。動画素材は置いた所に `play=loop`。`--remote` では全桁で書く — 8 桁と `= file=名` は台帳の pin を引く書き方)・`motion up = in=rise,20,550 ease=back(1.7)` (`out=` `main=` も・`in=up` / `main=名` で付く)・`run hl = color=$o size=48 stroke= font= marker=$y,38% background=$色 border=$red,7 radius=12 padding=14` (`size=0.5em` = 入る文字の比 — 数字の横の単位を小さく。`background` = 行の箱いっぱいの地・`marker=$色,42%` = 行の箱の下 42% の帯・`border` `radius` `padding` (左右) は地の枠 — 1 つの文字の中の run の形は同じ・色だけ run ごと)・`cue` (後述)・`default text = color=#FFFFFF align=center`・`style s1 = "太い見出し"`・`use tpl = 8桁` (template の根と section を取り込み `[tpl.名 新名] props` で実体化)。timeline: `cast narrator = "落ち着いた30代女性" speed=110%`・`read 3日 = みっか`。
- `種 = 値` — timeline: `transition = dissolve,320,color=#000000,se="シュッ" -2dB` (`se=` = 切替の境目で鳴らす音)。
- `種 引数…` — design: `canvas 1280x720 bg=#0B1220`・`theme dark`・`palette a=#1F6F5B bg=#0B1220` (主色 `$a` 副色 `$b` — 書かなければ theme の accent / accent2・theme の `$ink $mute $panel $line $accent $accent2 $band $ok $bad $bg` を上書き)・`font "ZEN角ゴシックNew Bold"`・`fonts m="Manrope ExtraBold"`・`art` `photo_style` `prompt_tail "文字なし"` (全部の絵・タグごとは `photo="…"`)・`shadow_default 0` (箱の既定の影・`=` 無し)・`lint off=duplicate_text,bgm_gap`・`sfx off`・`master lufs=-15 tp=-1`。timeline: `silence head=250 tail=250`。

## design.txt — 要素 (なに)
```
#v2
canvas 1280x720 bg=#0B1220                         # 根 (設定・定義) は section より前
palette o=#F0A030
sound pon = "ポンという音"
def tile(t) = div(width: 180px; height: 96px; padding: 0; border-radius: 16px)   # 根の def (= class)。引数は {t}
  p#t(cx: 50%; cy: 50%; font-size: 28px) {t}
subtitle.hug(font-size: 28px; bottom: 24px)        # 字幕 (根・cut 外)。札の変種 subtitle.hit(transform: rotate(-3deg)) → timeline の [card:hit]
bgm#music 静かなピアノ
section#intro                                      # cut 見出し (宣言が要る時は `section#intro(stagger: {each: .12})`)。以後の要素はこの cut
img#hero(inset: 0) [photo]夜の街、文字なし           # 要素 = tag#id(宣言) 内容。印が無ければ cut 頭に出る
div#box(left: 150px; top: 70px; width: 980px; height: 436px; border-radius: 24px; in: rise,20,550)
  p#t(font-size: 48px) 見出し                       # 字下げ = 子。名は box.t
  p#k(left: 0px; top: 96px; font-size: 96px; color: $o) [count:9.4]%   # 数える数字
#box.hot(background: $o; scale: 1.05)              # 変種 = #名.tag(宣言)
tile#org.l(left: "87;287;487"; top: 560px) ×3 a;b;c      # ×N。instance = org.l[1]・子 = org.l[1].t
section#paid
p#pd(cx: 640px; top: 300px; font-size: 48px) 課金率
```
| 行 | 形 | 規則 |
|---|---|---|
| cut 見出し | `[cut 名] [props]` | 名は timeline の `*** 名` に在ること (DEFECT:CUT_UNKNOWN)。順序は timeline が正。2 回は DEFECT:DUP_CUT |
| section | `[型 名] props` / `[型 .子] props` / `[型] props` | 型は下表の型名か def 名。1 行 1 section。`[cut]` より前の section は全編の根 = 最初の cut の頭から跨いで出る (`show` は要らない・全面の地は `z=back` — 無いと後の cut の絵の上に乗る)。同じ名は cut が違っても DEFECT:DUP_NAME |
| 子 | section の直下に字下げ | 親の内側座標・親と一緒に出入り。子を持つ要素は型を問わず子ごと 1 枚 (CSS の stacking context — 入退場・印の動き・薄さ・回転は群が子ごと (子は自分で書いた入退場だけ・`in=none` の親の子も入場なし)・子の `z` は要素の中に閉じる・絵の Ken Burns と文字の 1 字ずつの入場は要素自身)。`z` は親の段 |
| 変種 | `[名 .tag] props` | 書いた key だけ替わる状態。`[!名 .tag]` で補間して移り `[=名]` で戻る (object — 書体 / style・画像・fit の種類・形の種類・blend・mask・svg の部品 — が違う変種は補間せず、その語で層を閉じて開き直す: 変種の `in=` があれば入場、無ければその frame で替わる)。×N の変種 `[hg .lo] w=29;18;55 fill=$a;$b;$c` は instance ごと (`z=` の section があっても効く・家族の子の変種 `[hg.t .lo]` も)・印は `[!hg[*] .lo]` / `[!hg[k] .lo]`。位置 key を書かない変種は今の位置の上に重なる。文字の変種の `content=` は文字も替える (`[!名 .tag]` = 同じ語で入れ替え → 変種・`[>名 .tag]` = その文字で出す・`[=名]` で元の文字と見た目へ)。`content=` は `[text]` の変種だけ (字幕の変種・run・板の印で子の文字は DEFECT:KEY) |
| 既定 | `default 型 = props` | その型の section に書いていない key を足す (section > default > 型の既定)。変種には足さない (×N の全 instance には足す)。既定と同じ値は info:SAME_AS_DEFAULT |

### 型
| 型 | 一言と key |
|---|---|
| `text` | `content="見出し[br]2 行目"` `size=48` (`hero\|h1\|h2\|body\|label\|note` = 120/48/36/26/24/22) `font=m` `style="太い見出し、白文字"` (preset を意味検索で引く — 縁・影・グラデが付き得るので、その効果が欲しい時だけ書く・色・縁・書体は key が勝つ・`flat` で消えるのはグラデと光彩系の影だけ。`style=` を書かない文字は検索せず、白・縁と影なし・書体は根の `font` (無ければ 源真ゴシック Bold) に `color=` を当てた物) `color=` `align= valign=` `stroke=#000000,10` `text_shadow=0,4,#0000008C,3` `letter_spacing=0.1` `line_height=` `palt=off` (詰め組みは既定 on・数える数字は off) `vertical=true` `nowrap=true` `shrink` (1 行に収まるまで縮む) `hide_subtitle` `underline=$色` `rules=both,36,2,$a`。`fill=$a radius=99 padding=6,14` を書けば札 (`shape=speech-bubble` で板の形)。`{tok}…{/}` = 文字の一部 (根の `run tok =` の class か印の的)・`[count:9.4 start=0 roll ms=1400 delay=320 ease=ease_in_out]` (start= を書かなければ値の 8 割から・10 未満は 0 から。出ると同時に数えるのは 3 桁以上・小数・時刻の数だけ — `38℃` のような 1〜2 桁は静止・数えるなら `[!名 count]` — 出した語より後の印なら出た時は start の値 (`0%`) で印の語から数える) `[count:8:20]` `[count:4:24:15]` = 数える数字 (`:` の桁は 60 進 — 分:秒・時:分・時:分:秒 も同じ桁送りで `[count:14:30 start=15:00]` は 15:00 → 14:59 → … → 14:30・`roll` は不可)。出ている数字を別の値へ数え直す (1,243 → 1,231) は `[!名 text,"[count:1,231]円"]` (start= を書かなければ出ている値から) |
| `div` | 箱 (CSS の div): 塗り・縁・影 `fill= border=$b,2 radius= shadow= padding= gradient= pattern=` + 子を字下げ (子は箱の内側から)。`stack=h\|v gap=` で位置を書かない子を並べる・`valign= align=` は子の寄せ (`center\|bottom\|between`)。`h` を書かない箱 (1 枠を割った ×N の枠も) は中身の高さ (枠の上端・`valign=center` で枠の中央)。箱の角に接する子の `image` は箱の角丸で切れる (書いた `radius=` が勝つ)。題や項目の配置は持たない — 中身は子の `[text]` `[icon]` `[image]` と ×N で書く |
| `image` | `content="[photo\|transparent\|diagram]…"` / `content=@名` / `content="[ref:@名]肩越しの寄り"` (基準画像からの派生・透過は `[transparent][ref:@名]…` と書いた時だけ — 書かなければ不透明で、場面を書かなければ白地・2 人を揃えた 1 枚は基準画像を並べる `"[ref:@me][ref:@foe]向かい合う二人"` — 3 つまで・`@名` は根の `image 名 =` だけ (cut の section の名は DEFECT:ARG — 画面に出した絵を基準にするなら根に `image 名 =` を書いて `content=@名` で出す)) / `content="icon:名"` / `content=@clip`。`fit=cover,focus=60%,0%,zoom=130%\|contain` `flip=x` `scrim=right,0.45` (`vignette,0.6` / 一様 `0.4` / `def` の幕を消す `none`) `tone=light\|dark` `quality= aspect= alt=` `subject="top 30%" face= room=` (主体・人物の顔・文字のために空ける所 = `left\|right\|top\|bottom\|center N%` か `x%,y%,w%,h%`・構図は文でなくこの key で — 生成に伝わり、生成後に測って切り出しを寄せ、文字が主体に乗れば warn `text_over_subject`・絵ごとに書く (根の `img { }` は DEFECT)・宣言の無い絵の主体に乗った板なしの文字は engine が塊ごと空いた所へ逃がす) `play=loop\|stretch[,start=][,to=][,speed=N%][,mute]` (`start` = 素材の使い始め・`stretch` = 窓の尺に合わせた速さ)。全面は `in=none out=none main=kb,1.0>1.08` (`main=` を書かなければ kb が付く — 静止は `main=none`) |
| `icon` | `name=shield-check` (Phosphor / Lucide・無い名は DEFECT:ICON_UNKNOWN) か著述 `content="封筒と送信の矢印"`。`size=120` `color=$a` `stroke=` `weight=duotone\|bold\|fill` `flip=` `in=draw,600`。地: `fill=$a` (既定は丸・`radius=12` で角丸の四角・`padding=` は既定 size の 0.3・`border=$b,2` で縁・`border=` だけなら輪) — 地の箱は size + 2 × padding の正方形で icon と同じ中心 (書いた `left top` は地の箱の左上・位置の式の辺も地の箱)・icon の色は書かなければ地と反対の ink・`recolor` は地の色を替える。地は名前の icon だけ (線の icon `in=draw` `stroke=` と著述の icon は DEFECT:KEY) |
| `shape` | `path=arrow_r,curve=0.2` (形の名は types・無い名は DEFECT:SHAPE_UNKNOWN・子の寸法は `h=100%` / `top=0 bottom=0` で親の内側いっぱい) / `ellipse` / `points="900,560;980,440;1060,560"` (×N で個体ごとに分けるなら点は空白区切り `points="x,y x,y x,y;x,y x,y x,y"` — `;` は個体の区切り) / `path="M…"` (canvas px)。矢印 (`arrow_*`) は線で描く形 — 色は `fill=$色` だけ・太さは `border=$色,8` (`border=none` は何も描かれない = DEFECT:ARG・面で塗る太い矢印は `[icon] name=arrow-fat-up weight=fill`)。`fill=` `border=$b,8` `dash=6,6` (path / points の形だけ — 箱の破線の枠は `[shape] path=rect,r=0.1 fill=none … dash=` を重ねる) `stroke-linecap: butt` (線の端・既定は round) `rotation=180`。`path="M…"` に `left top width height` の 4 つを書けばそれが svg の箱 (回転・倍率の原点 = 箱の中心・弧を輪の中心で回す)。楕円の吹き出しは文字に `shape: rounded-speech-bubble` (`rot=` は DEFECT:KEY) `flip=` `in=draw`。変種に別の `points=` で頂点が補間 |
| `svg` / `veil` | 根の `svg 名 =` の部品 `[svg logo] left=80 top=160 w=120 h=120 part=mark` / 幕: `opacity=0.5 color=#000000` / `to=bottom start=0.4` (グラデ — `to=` は濃くなる向き: `to=top` = 上が暗い) / `fill=radial(…)` / `vignette=0.6` / `grain=0.06` / `filter=sat:0` (色調の幕 = 下の層を色の変種へ)。既定 `in=fade,500`・全面 |
| `group` | member は `[型 g.x]` (字下げ不要)。`clip=24,g.bg\|true` `sheen=g.bg,900,soft,sine.inOut` `in=…,stagger=60` (member の出る間隔は入場の tween の中) `out main sticky` |
| `bgm` `se` | `[bgm music] volume=-3dB (曲の大きさ・既定 +7dB = 声の 9 LU 下 = hf の大きさ — 書かない) fade=1500,2500 duck=off keys="0:+5\|15s:0\|end-3s:+3" (keys の既定 = 末尾 3 s 前から +6 dB の余韻) align=end lowpass=650 jump=91.6s>166.8s xfade=1300` (曲は層の尺より短ければ周期で繰り返す — 止めるのは `[<#名]`)・`[se] volume=-6dB fade=100,800` (全効果音の既定・名は書かない) |
| studio `link backdrop progress particles confetti html camera avatar voice` | `[link l] start=a to=b arrow dash route=elbow via=(x,y) arc=0.3 label= draw` (名を指した 2 点を結ぶ線)・`[backdrop bd] look=grid spacing=40 drift=left`・`[progress p] until=cut\|end total=51s` (時間の帯・total= は stream の orchestrator が plan の見込み秒から入れる)・`[particles pt] n=40 dot=4-9 drift=up` (`dot` = 粒の直径 px の範囲)・`[camera cam] left top zoom=` + `[cam .tight] left top zoom= move=700`・`[avatar lay] cast=名[.衣装] left top w h fit=contain speaking=bounce`・`[voice 名] volume=+3dB filter=echo` |

どの層にも: `left top w h` `right bottom` (縁から) `inset=0` (全面) — 子は親の内側から `stack=h\|v\|z\|grid gap=24` `rotation rotationX rotationY skewX skewY depth` (静止姿勢・`rotation` は子ごと回る・子を持つ要素に傾き / 3D は書けない) `pivot=center\|top\|…\|x%,y%` `opacity` (子孫にも) `z cam=none` `in out main delay` `sticky` `overlap over` `bleed` `se=none` (自動の出現音を消す) `emph=frame,$bad` (`[!名]` の引数無しの既定) `filter=sat:0.3,bright:1.2,blur:6,dim:0.6,look:sepia\|#暗/#明\|#色` (素材だけ・look の名だけ `filter=sepia` / `[!名 filter,gray]` も可) `blend=screen\|multiply\|add\|overlay\|soft-light` (`filter` `blend` `glow` は子を持つ div に書けない — 子の無い div か子に) `fill border=色,幅 radius=a,b,c,d shadow=1..5\|dx,dy,blur[,spread],色 glow=色[,blur[,spread]] padding gradient=色[,色],角度 pattern=hatch[,角,色,間隔,幅]\|grid\|dots\|paper vignette grain edge=辺,px,色 border2 pointer=below[,位置]\|相手\|絵.mouth` (pointer = 吹き出しの尻尾・`shape=speech-bubble` の札は engine が相手 / 口の点へ向ける — 絵の点はこの形だけ) `mask="[transparent]…"` `clip-path=inset(8% 0 78% 0)` (CSS の `clip-path: inset(上 右 下 左)` — 要素を自分の箱の内側の矩形で切る・動きは切り口ごと) `mask-image=linear(…)|radial(…)` (CSS の `mask-image: linear-gradient(…)` / `radial-gradient(ellipse W% H% at X% Y%, …)` — 板の alpha mask・絵には書けない) `clip=true` `exclusive=相手` (両側に書く・開くと相手を閉じる) `tone` `telopbase`。型に無い key は DEFECT:KEY (似た key を出す)。

### 位置と重ね
| 規則 | 形 | 例 |
|---|---|---|
| 根の位置 | `left top w h` (canvas px・左上原点) か全面の `inset=0`。`x y` は位置の key でない (GSAP の移動量 `in=x=` / `to,x=` だけ・位置に書けば DEFECT:KEY)。寸法を書かない文字は `cx= cy=` で中心を置ける (箱は文字幅のまま — `left=0 w=100% align=center` は箱が全幅になり、`fill=` を書くと札が画面幅の帯になる・回転の中心が canvas 中央)。`cx cy` (子の `cy=50%` も) は書いた点が基準で、文字の箱が中身に合わせて伸び縮みしても動かない | `[div b] left=80 top=112 w=643 h=480`・`[text t] cx=640 top=300` |
| 子の位置 | `left top right bottom w h` = 親の内側からの相対 (根と同じ key)。全面は `inset=0` (親の内側いっぱい)。子の変種 (`[箱.子 .tag] top=`) の位置も親の内側から。幅を書かない子は内側いっぱい。中央に置く子は `cx=50%` (`%` は親の内側の比・icon は `w=100%` でなく `cx=50% size=`)。横に並べた子 (帯の icon + 文字 + 札) の縦を揃えるなら `cy=50%` (`top=` は箱の高さが見えず 1〜4 px ずれる)。親に `stack=h\|v\|z\|grid gap=24` で位置を書かない子を左から / 上から等分・`z` は同じ枠に重ねる | `[text .t] left=0 top=50`・`[icon .i] cx=50% top=20 size=80`・`[text .tag] right=16 cy=50%`・`[div row] stack=h gap=24` |
| 寸法・参照 | `w h`。文字に `h` は書かない。`%` は親 (根は canvas) の比。`名.辺±N` で参照 (回した要素は DEFECT:REF)。`bleed` = 画面外の warn を出さない (子孫と群の member も — 画面の外から入る光の筋・はみ出す太陽。縁が透明に落ちる gradient の層 (radial の末端 / linear の両端が `#RRGGBB00` の光彩・幕) は書かなくても同じ扱い) | `w=40%`・`top=hdr.bottom+16` |
| 収まり | 書いた値は確定 — engine は書いた枠の文字を縮めない・折り直さない・押し出さない。寸法を書かない軸は中身に合わせる (hug: 幅は書いた幅か親の内側で折り、高さは行の箱の積み)・`.shrink` を書いた文字だけ字の床 (宣言の 0.7 倍と読める字 = 本文 26 / 字幕 36 × min(canvas) / 1080 の大きい方) まで縮める。書いた枠に入らない文字は severe:overflow (`今 N 字 → M 字以内なら入る`)・宣言の無い前面が文字を隠せば severe:occluded (どちらも描く — 直すのは著者) | `div#c(height: 120px)` の子の長文 → 箱が伸びる |
| z | `z=back\|front\|curtain` (書かない = 既定の段)。子は親の段。字幕は front と curtain の間に固定 (`z=curtain` の幕と切替の dip / flash は字幕も覆う)。`cam=none` = camera の寄りを受けない。同じ段は書いた順 (後が上)。`overlap=a,b` = 意図した重なり (監査の occluded を黙らせる)。`over=相手` = 相手の外接箱に置く | `[veil k] z=curtain`・`overlap=box` |
| 縦 canvas | `canvas 720x1280`: 本文の目安は左右 48・上下 128〜1066 (字幕帯 h=150 が下 18 に付く)・**全高を使う**: 字幕は下端 (`bottom=` 24〜80) に置き、本文は上の余白から字幕のすぐ上まで埋める — 字幕を画面の中ほど (`bottom=300` など) に上げてその下を飾りだけにしない (投稿先の UI が被る前提の余白は取らない・下 3 割が全編で空く)・地の丘や色の面は字幕の後ろに敷ける (`overlap=subtitle` で宣言・`z=back` の `[shape]` は `[backdrop]` の下に隠れる — 全面の `[div] … z=back` の色の斑は backdrop の上に見える)・文字は横より 1 段大きく (見出し 56〜84・本文 30〜36)・×N の 1 枠は `stack=v` が既定 | `[subtitle] size=32 hug w=640 h=150` |

字幅の目安 (1 字の幅 ÷ size・engine の計測器で実測・詰め組み palt on)。1 行の幅 ≒ size × 比 × 字数 (+ letter-spacing)。実寸は check の `今 N 字 → M 字以内` (check と render は台帳の書体を本番と同じ書体の並び — 英字書体の和文は代わりの和文書体 — で測り、文字の箱 (幅・折る行数) も cut 実現の頭の stage 2 でその実寸で決める。下線の帯は目安の幅。`overflow` の字数も同じ計測器):

| 書体 | 漢字 | かな | 数字 | 英小 | 英大 |
|---|---|---|---|---|---|
| 源真ゴシック Bold (既定)・Zen Kaku Gothic New Bold | 1.00 | 1.00 | 0.59・0.47 | 0.56・0.49 | 0.67・0.63 |
| Shippori Mincho B1 Bold (明朝)・Rounded Mplus 1c Bold (丸ゴ) | 1.00 | 0.80・1.00 | 0.62・0.64 | 0.56・0.55 | 0.77・0.65 |
| Dela Gothic One (極太)・Manrope ExtraBold (欧文) | 1.00・— | 1.00・— | 0.83・0.59 | 0.67・0.56 | 0.91・0.67 |

### 動き (GSAP 語彙)
| 規則 | 形 | 例 |
|---|---|---|
| 入退場 | `in=preset[,引数…]` `out=preset[,引数…]`。位置引数: 数 1 つ = ms・2 つ = 量, ms。`slide` `wipe` は向き `left\|right\|up\|down` が先頭 (`in=slide,left` = 左から来る・`out=slide,left` = 左へ抜ける — slideInLeft / slideOutLeft と同じ)。key 引数 `ease= delay= stagger= from= dir=`。`none` = 無し。1 層に `in=` は 1 つ (箱と文字を別に動かすなら箱 + 子の文字に分ける)。箱の入場 (rise・x / y の px・slide) に乗る子の文字と札は箱と同じ px で動く。px は書いた値どおり (板の無い文字の `filter=blur:` と `in=travel` の経路も・展開後の design も px)。cut 末の自動 close も `out=` を再生する (def の子を止めるなら `実体.子.out=none`・動画の終わりまで出ている層 (最後の cut の自動 close・跨いだ sticky・根) は退場せず最後の frame まで残る)。退場は cut 境界で終わる (退場を次の cut の入りに重ねるのは `transition none,N`・旧場面ごと残すのは `overlap=`) | `in=slide,left,30,400` |
| preset | `fade` (300) `rise` (px 下から・24 / 450) `drop` (px 上から・弾む・700) `slide` (向き,px・400) `zoom` (倍率・0.3 / 500・fade つき) `pop` (倍率・0.5 / 500・back) `wipe` (向き\|center[,angle=deg]・600)。studio: `spring settle bounce flash mask_rise swing_in travel,start=名,arc=0.3 punch typewriter fade_stagger blur pixelate circle_wipe iris_wipe clock_wipe,left,splits=3 spin_zoom zoom_reverse draw drift ping` + `then=punch:1.3:450` | `in=rise,20,550`・`in=pop` |
| custom | key だけを並べる。channel = `x y scale scaleX scaleY rotation rotationX rotationY skewX skewY opacity blur depth` + 文字 `letter_spacing glow color scramble` + `duration ease delay pivot clip=true`。`x y` は px (層の寸法で換算しない・子は親と同じ px)・`scale*` は倍率・`rotation*` は deg。文字は `stagger=40` (1 字ずつ・ms)・`from=start\|end\|center\|random[,seed=N]` | `in=x=-44,opacity=0,duration=550,ease=power2.out`・`in=rise,20,400,stagger=40` |
| keys | `keys(at=0 … \| at=0.7 … ease=… \| at=1 ease=…)[,duration=ms]`。key 24 個まで (at=1 は数えない) | `in=keys(at=0 x=441 opacity=0 \| at=0.7 x=-8 ease=power2.out \| at=1 ease=sine.inOut),duration=900` |
| ease | GSAP の名 (`power1〜4.in/.out/.inOut` `sine.*` `expo.*` `circ.*` `back.out(1.7)` `elastic.*` `bounce.*` `none`・向きの省略は out)。engine の内部名 (`ease_out cubic_out …`) は書かない (読めるが欠陥文にも出ない)。係数つき `back(2.2) bezier(.2/.8/.2/1) spring(10/240) steps(4)` は preset の入場と keys の key だけ。無い名は DEFECT:EASE_UNKNOWN。名前つき: 根の `motion 名 = in=… out=… ease=…` を `in=名` で全部付ける (section の key が勝つ・組み込みと同じ名は DEFECT:NAME_SHADOW) | `ease=power2.out`・`in=up` |
| 常時 | `main=preset[,引数]`: `float breathe sway pulse` (`level=1..5`)・`spin,ms[,ccw][,pivot=名\|x%,y%]`・`kb,始[@x%,y%]>終[@x%,y%][,ease=名]` (@ = 動かない点・ease の既定は linear = 一定速のカメラ。全面の写真は 3〜9% + 平行移動が相場: `kb,1.04@55%,48%>1.12@45%,50%`)・波形 `sine triangle square noise sawtooth ramp constant` (channel = custom と同じ名・`freq_ms= window=a,b phase_offset= target=media start_ratio= end_ratio=`・noise の `ease=steps(1)` = 周期ごとに次の乱数へ飛ぶ — 毎 frame 動く grain は幕に `main=noise,x=4,y=4,freq_ms=33,ease=steps(1)`)・`keys(…),window=0,1300,forwards` (窓の後も終わりの姿) | `main=kb,1.1@40%,60%>1.0`・`main=constant,rotationX=70,depth=4,pivot=top` |
| 既定 | 退場は `out=drift` (少し上へ・縮み・ぼけ)。全面の image / div は `in=none out=none`・veil は `in=fade,500`。一回きりの効果は印でだけ書く・design には書かない | |

### ×N・群・def と根の雛形
| 規則 | 形 | 例 |
|---|---|---|
| ×N | `[型 名] ×N props`。値は `;` で instance ごと (1 つだけ書けば全部同じ・def の引数も・tween の中も `in:{rotation:'-10;10'}` で instance ごと・大きさ `width: "2;3;5"` も可・位置を instance ごとに書いた箱の `height` は CSS と同じ箱の高さ)。静止の `transform: scale(.6)` は要素の transform (変種の `transform: scale(1)` へ補間)。基底名への印 `[>名]` `[<名]` `[!名 dim]` `[=名]` は全 instance に効く。instance = `名[k]`・子は `名[k].子`。字下げの子は全 instance に写る (値も `;` で配る)。入場の tween の中の `in=…,stagger=40` = instance の入場を 40 ms ずつ (印 `[>名[*]]` と `[<名[*] from=]` の間隔も・`in=stagger=40` は既定の入場に間隔だけ・section の `stagger=` は DEFECT:KEY・×N の text の 1 字ずつは書けない)。状態の印 `[!名[*] …]` は全 instance 同時・順に変えるなら `stagger=N` (`[!x[*] fill,$c stagger=20]`)。入場と退場の間隔が違うなら退場は instance ごとに `[<名[k] +N]` | `[div dm] ×3 left=80 top=112 w=1120 h=400 in=rise,stagger=40` + `  [text .t] content="a;b;c"` |
| 枠 | 位置を 1 つ書いて `stack` を書かなければ横に並べる (縦長の枠は縦 = CSS の flex と同じ)。1 枠 + `stack=h` = 枠幅を N 等分 (`gap=` 24)・`stack=grid` = 枠を行 × 列に (列は √N の切り上げ・`grid,3` で 3 列・左上から横へ詰める)。字下げの ×N (`[div .r] ×4 stack=v`) は枠を書かず `stack=` だけで親の内側を N 等分 (子の位置は `left top` か `;` で instance ごと) | `×3 left=87;287;487` か `×3 left=87 stack=h` |
| group | `[group g] props` + member `[型 g.x]` (字下げすれば g の内側座標 — 群の `left top w h` が字下げの member の原点と内側 (書かなければ canvas)。def の根が `[group]` の実体も同じ。字下げの ×N は枠を書く)。群の中に群 `[group g.in]`。性質: `clip=半径,g.bg\|true` `sheen=g.bg[,ms][,色][,soft][,ease]` `in out main` (member の出る間隔は `in=…,stagger=`) `sticky` | `[group org] in=stagger=60 clip=24,org.bg` |
| 群の印 | `[>g]` = member を stagger で (群の `in=…,stagger=N` は 0 / N / 2N・`delay=` を持つ member は数えない)・`[>g +300]` = 群ごと 300 後。自分の印を持つ member は `[>g]` で出ない。群の `[!g dim]` / `opacity` は群をまとめて合成 (member ごとでない) | `[!g to,x=100,scale=0.9,rotation=-6]` |
| 薄く出して濃くする | ×N の行に `stagger=dim` = instance を一緒に 0.4 で薄く出し、instance の印 (`[>名[k]]`・focus) の語で濃くする (`stagger=sentence,dim` は印の無い instance も 2 つ目から文の頭で 1 つずつ) | `div#r(…; stagger: dim) ×3` |
| 主役の切替 | `[!名[k] focus[,比][,keep=名]]` = k を出し (前に k の印が無ければ)・沈んだ k を戻し・他の instance を 0.4 に沈める。積み上げる一覧 (材料・手順) は `focus,0.75` か済んだ行に ✓ (`[!#r[1] check]`) — 0.4 は写真の上で読めない | `[!#r[1] focus]…[!#r[2] focus]` |

一覧 = 箱の ×N: `div#c(left: 48px; top: 400px; width: 624px; height: 420px; display: flex; flex-direction: column; gap: 16px) ×3` で 1 枠を 3 段に割り、字下げの子 `  p#t(left: 24px; cy: 50%; font-size: 30px) 下ごしらえ;火入れ;仕上げ` に `;` で段ごとの文言 (`c[k].t`)。印は `[>#c[2]]`・箱は中身の高さで段の上端に付く。

```
def step(n, t, w=240) = div(width: {w}; height: 200px)     # 根 = tag(宣言)。引数は名・既定値は "…" か素の値
  p#n(font-size: 72px) {n}                              # 子 = tag#子。実体 s1 の下で s1.n
  #step.hot(background: $o)                             # 根の変種は def 名で (実体では #s1.hot)
step#s1(left: 40px; top: 60px; n: 1; t: "…")                 # 実体 = def名#名(引数 + 根への上書き)
step#s2(left: 320px; top: 60px; n: 2; s2.n.size: 40)         # 子の上書きは 実体.子.key か、字下げの同名の子 (slot・下の s3)
step#s3(left: 600px; top: 60px; n: 3; t: "…")
  p#n(font-size: 40px; color: $o)                       # def の子 n の差し替え: 書いた宣言が勝ち・他は def のまま (型は同じ型)・他の名は新しい子
```

- 形: `def 名(引数[=既定],…) = [型] props` + 字下げの子。引数は `{名}` で値の中に (`content={n}`・`"@{who}、笑顔"`)。未指定で既定の無い引数は DEFECT:ARG。引数が無ければ `def 名 = [型] props` (見た目だけの名 = class・`[名 x] content="…"` で使う — 同じ形の 2 つ目はこれに上げて実体を並べる)。根に自分の型を書く def (`def div = [div] …`) は輪になるので DEFECT:NAME_SHADOW。`self` = def の中で根の名 (`[link .l] start=self to={to} dash`)。
- 実体: `[def名 名] 引数=値 … 根の key=値 … 実体.子.key=値`。字下げの子のうち def の同名の子 (`[.v] …`・型は省くか def の子と同じ) はその子の差し替え (書いた key が勝ち・他は def のまま)・他の名は新しい子。×N・変種も section と同じ。群が根の def は子が member。`scale=0.8` = 実体を寸法ごと縮める (w h — 実体の行に書いた `w= h=` も・子の位置・size・padding・gap — 置き場の left top はそのまま・check の箱も縮む。他の section の `scale=` は DEFECT:KEY)。
- 根の雛形 (見本 — 色と寸法は題材で変える。札の行・横棒・流れ図は組み込みの部品でなく、この形の def を根に書いて ×N で並べる):

```
fonts n="太い幾何学的なサンセリフの欧文、数字がくっきり"   # 数字の書体 (細いセリフ・等幅・筆の数字は細く見える)
# 主役の数字: 題 + 数字 (書体 n) + 単位。count はこの段で
def stat(v, u, l) = div(width: 624px; height: 210px; padding: 0px; background: none; border: none; box-shadow: none)
  p#l(left: 0px; top: 0px; font-size: 30px; color: $mute; content: {l})
  p#v(left: 0px; top: 46px; font-size: 144px; font-family: n; color: $a; line-height: 1; content: {v})
  p#u(left: .v.right+12; top: 126px; font-size: 56px; line-height: 1; content: {u})
# 札の行: icon (丸い地) + 題 1 行
def row(i, t) = div(width: 560px; height: 76px; padding: 0px; border-radius: 16px)
  icon#i(left: 18px; cy: 50%; font-size: 30px; name: {i}; color: #FFFFFF; background: $a)
  p#t(left: 90px; cy: 50%; font-size: 30px; content: {t})
# 横棒: 札 + 棒 (幅 = 段の内側の比) + 棒の右端に値
def hbar(v, t, n, c=$a) = div(width: 640px; height: 64px; padding: 0px; background: none; border: none; box-shadow: none)
  p#t(left: 0px; cy: 50%; width: 140px; font-size: 34px; text-align: right; content: {t})
  div#b(left: 156px; cy: 50%; width: {v}%; height: 52px; border-radius: 4px; background: {c}; border: none; in: {scaleX:0, duration:0.6, ease:'power3.out', pivot:'left'})
  p#n(left: .b.right+12; cy: 50%; font-size: 44px; font-family: n; color: {c}; content: {n})
# 流れ図の札 (間の矢印は shape を札の辺に位置の式で)
def node(t) = div(width: 220px; height: 110px; padding: 0px; border-radius: 16px)
  p#t(cx: 50%; cy: 50%; font-size: 36px; content: {t})
row#r(left: 64px; top: 120px; width: 560px; height: 260px; display: flex; flex-direction: column; gap: 16px; stagger: dim; i: "key;ruler;check"; t: "鍵を開ける;寸法を測る;確かめる") ×3
hbar#hb(left: 660px; top: 120px; width: 560px; height: 240px; display: flex; flex-direction: column; gap: 16px; v: "50;29;12"; t: "A 社;B 社;C 社"; n: "60%;35%;15%") ×3
node#f(left: 64px; top: 440px; width: 800px; height: 110px; display: flex; gap: 70px; t: "注文;発送;到着") ×3
shape#fa(left: "f[1].right+14;f[2].right+14"; cy: f[1].cy; width: 42px; height: 30px; path: arrow_r; background: $a; border: 4px solid $a) ×2
stat#sv(left: 900px; top: 400px; width: 340px; v: "[count:120]"; u: "件"; l: "3 か月の配達")
```

  棒の幅 `{v}%` は段の内側の幅の比 (値 ÷ 最大 × 棒に使える比を著者が計算する)・値の札は棒の右端に `.b.right+12`・矢印は札の辺に位置の式で置き、印は `[>#f[1]]…[>#fa[1]][>#f[2]]` (矢印と次の札を同じ語で)・行は `[!#r[2] focus]`・棒は `[>#hb[*] {stagger:{each:0.12}}]`・数字は `[>#sv]` (3 桁以上と小数は出ると同時に数える)。icon の地は `background:` (= `fill=`)。
- ×N の箱の札・絵は子として書く (`;` で instance ごと): `div#dm(…) ×3` の下に `  p#s(right: 8px; bottom: 8px; background: $a; padding: 4px 12px) a;b;c`。

### 字幕・cut
- 字幕: `[subtitle] size=28 hug bottom=24` (根に 1 つ)。`left top bottom w h fill border radius padding color font style telopbase in=pop out=fade`・声の窓 `lead=100 tail=300 hold=next,800|same|off` (ms・lead / tail は 10000 まで — 窓は札の区間 = 次の札の頭か cut の終わりで切れるので、cut の最後の札を cut の終わりまで残すなら `tail=10000`)・`wrap=comma,16 strip=、。|all|、。>space unit=phrase|sentence min_phrase=0 label=edge|above|top_left|inside label_in=pop`。変種 `[subtitle .x] rotation=-3 ghost=#00E5FF,#FF2BD6,17 main= lead tail hold` + timeline の `[card:x]` (その札 1 枚)。
- cut: `[cut 名] stagger=ms out=preset,…`。切替は timeline の cut の末尾に書く (design の `transition=` は DEFECT)。`out=` = 末尾の一斉退場 (境界で終わる)・地の色は cut の最初に全面の箱 `[div 名] inset=0 fill=色 radius=0 border=none shadow=0 padding=0 in=none out=none z=back` (生成画像は `[image 名] inset=0 sticky`)・sticky を閉じるのは前の cut の末尾の `[<名]`・`stagger=` = 頭の組み上がり間隔 (既定 120・`0` で一斉)。

## timeline.txt — 時間 (いつ)
```
#v2
cast narrator = "落ち着いた30代女性" speed=110% manner="ゆっくり" label="部下" label_fill=#1F5FBF subtitle=.em
transition = dissolve,300,overlap=300,ease=power2.out        # 書かない cut 末尾の既定 (最後の cut を除く)
read 3日 = みっか                                              # 全出現の読み (任意・誤読は check の読み照合が直す)

*** intro                                                       # cut 境界 = section#intro
[>#subtitle]                                                    # 字幕を出す (次の台詞の札から・cut を跨いで続く・閉じるのは [<#subtitle])
bgm music start=13.7s +1500                                     # design の bgm#music が要る (音量は design の gap:)
@narrator: [silence:600][>#box]クラウドストレージは、          # 台詞 + 印
@: [!#box.k count]サーバーに[♪pon -4dB]保存して使う仕組みです。 # @: = 直前と同じ話者
@| 次の文。                                                     # @| = 折り目 (音声は続き・字幕と anchor が増える・行頭だけ)
[<#music -3800]                                                 # cut 末の印だけの行 = cut 末の拍 (末尾の 3800 ms 前に閉じる・bgm も要素も同じ)
transition push,400,dir=left                                    # この cut の末尾の切替
*** paid
@: [>#pd]課金率です。[silence:1.0s]
# 末尾は書かなければ締めの画面が 3 秒残る (最後の frame まで)。`fade out,700` (地の色へ) は頼まれた時だけ
```
| 行 | 形 | 規則 |
|---|---|---|
| 根 | `cast 名 = "説明"\|id=8桁\|character="ずんだもん"\|@clip clip-s0 [speed=N%] [manner="…"] [avatar="…"] [label="…" label_fill=色 label_color=色 (#RRGGBB か design の palette の `$名`)] [subtitle=.tag]`・`silence head= tail=` (書かなければ head=0 tail=500 = 文末の間 500 ms。TTS の端の無音はこの値に揃う・`[silence:+N]` はこれに足す) / `silence source=cut`・`transition = 種,ms[,key=値…]`・`read 表記 = 読み` | 根は `***` より前だけ。cast は 1 つ以上。clip の cast は `@名:` の台詞行に書けない (DEFECT:CAST_KIND) |
| cut | `*** 名` / 2 回目以降の同じ型は `*** main[2]` (+ `[cut main[2]]` に section を書く) | 各 cut に台詞行 1 つ以上 (無音だけなら `@名: [silence:4s]`) |
| subtitle | 印 `[>subtitle]` / `[<subtitle]`・`subtitle "文"` / `subtitle .tag` / `subtitle .tag "文"` | 字幕は印 `[>subtitle]` で出す (印だけの行 = 次の台詞の札から・cut を跨いで続く)・`[<subtitle]` で閉じる (cut 末の印だけの行 = その cut の終わり)。書かなければ字幕は出ない。`"文"` = 次の札 1 枚だけ上書き。`.tag` だけ = 以後の字幕の変種 |
| bgm / se / show | `bgm 名 [start=時刻] [±N]` (start = 曲の頭出し・音量は design の `bgm#名(volume: NdB)` — `±NdB` は DEFECT:KEY・語で変えるのは `[!#名 to,{volume:-12dB, duration:.6}]`)・`se 音 [token…]`・`show 名 [+N]` (手で出す・+N は **cut 頭から** N ms 後 — 声の無い cut `@名: [silence:4s]` の途中で出すのはこれ・-N は DEFECT:BEAT_BEFORE_CUT) | 音 = `sound` の名 \| `"説明"` \| `id=8桁`。素の名は根の `sound 名` を先に引く (説明文は `"…"`)。`id=8桁` は check が台帳で全桁に補う (pin に無ければ DEFECT:ASSET_UNPINNED — 全桁の uuid か根の `sound 名 = id=` 経由で)。token = `±NdB` `fade=頭,末尾` `±N` `start=時刻` (素材の頭出し) `peak=時刻` (素材の山を語に合わせる) `to=時刻` (順不同)。最後の台詞より後の行は次の cut の頭 (閉じるのは印 `[<名]`) |
| 台詞 | `@名[.style] [.tag]: 文` / `@: 文` / `@\| 文` / `@clip id [.tag] [原文]` | 1 行 400 字まで。行の途中の `@\|` は DEFECT:FOLD。最初の台詞は話者を書く。`.style` = キャラの声色・` .tag` = `[voice 名 .tag]` の変種 |
| transition / fade | `transition 種,ms[,key=値…][,se=音 [token…]]` (cut の末尾・`se=` = 境目 = 次の cut の頭で鳴らす音・切替の無い境目は次の cut の頭に `se 音`)・`fade in,ms` (cut 頭・地の色から) / `fade out,ms` (最終 cut 末尾・末尾の無音の最後の ms だけ地の色へ — 頼まれた時だけ (「暗転して終わって」)。書かなければ締めの画面が最後の frame まで残る) | cut の頭 (台詞より前) の transition は DEFECT:TRANSITION_PLACE。締めの無音の中で画面を変える: `…ください！[silence:1.0s][>名][silence:2.0s]` (印の後の無音は fade の ms より長く)。行末 (無音の後ろ) の印は DEFECT:FADE_MARK — 最後の語からの遅れ `[>名 +1500]最後の語。[silence:3.0s]` でも書ける |

台詞の中の注釈 (印でない): `[silence:N]` (行頭 = 頭の無音・行末 = 末尾・文中 = 間 — 読点の後は 0.5 秒まで (`pause_in_sentence`)・`[silence:+N]` = 既定に足す・`[silence:3s]`) / `{表記|読み}` (その 1 か所だけ声は読み・字幕は表記・台本の文字は変えない (TTS の尺が変わる)・`{　|、}` で字幕の読点を空白に) / `[br]` (字幕の改行) / `[speed:N%]` (その台詞だけ・行頭 — 頭の `[silence:1.2s]` とはどちらが先でもよい。話し方は cast の `manner=` が基本。`[manner:怒って早口で]` (その台詞だけ・行頭) は Fish Audio の声だけに効き、他の声では無視される) / `[card:tag]` (札の頭に書き、その札 1 枚を `[subtitle .tag]` で描く) / `[|]` `[||]` (字幕の札だけ切る / 文の境界を跨いで繋ぐ) / `[♪…]` (効果音・折り目になる) / `[名 引数…]` (cue の呼び出し)。

### 印 — 4 動詞
形: `[動詞 名[{tok}] [やり方[,引数…]] [±N | cut-N]`。名は design の section (派生名も)。引数の無い `[>名]` が最短。 印だけの行 (`[!bar .s2]` を行頭に) = 次の台詞行の頭の印 (文字や注釈は書けない)。後に台詞行が無い (cut 末の) 印だけの行は cut 末の拍: `[<名 -N]` = `[<名 cut-N]` (`+N`・出す・変える印と音は DEFECT:ARG)。

| 動詞 | 意味 | 例 |
|---|---|---|
| `>` 出現 | その語で出す (design の `in=`)。印の無い要素は cut 頭。`[>名 preset]` = その時だけの in=・`[>名 .tag]` = 変種の状態で出す (箱の子も・`[=名]` で base へ戻る)・`[>名 状態]` = 出すと同時に当てる (= `[>名][!名 状態]`・check tint frame glow focus count highlight fill dim …)・`[>名 clear]` = 出す前に画面を払う・`[>名[*]]` = stagger で順に | `[>box]` `[>cl[1] check]` `[>hero .dark]` |
| `<` 退場 | その語から `out=` で消え始める (子孫と随伴も)。`cut-N` = cut 末尾の N ms 前に消え終わる (`cut-0` の退場も描く・`cut+N` は無い)。bgm と camera は退場の尺なしで拍で閉じる。字幕は `[>subtitle]` で出し `[<subtitle]` で閉じる (台詞の行の頭か印だけの行・やり方も拍も書かない) | `[<box +300]` `[<名[*] from=end]` `[<ch cut-400]` |
| `!` 変化 | 状態 (補間して移り `[=名]` か要素が閉じるまで続く。sticky の要素は cut を跨いでも続く — 次の cut の `[=名]` で戻す・object の違う変種への `.tag` はその語で開き直す) か効果 (一回きり・自分で戻る)。下のやり方。文の途中の `>` と状態の `!` は字幕の札もその語で替える (字幕は句)・効果 (punch ping … 一回きり) と文字の差し替え (`text,"…"` / `count`) は替えない (時計・番号札の刻みは語の途中でよい) — 札を割らずに状態だけ変えるなら `[subtitle] unit=sentence` (札 = 文) か、印を行頭に置いて `+N` | `[!org.l[2] tint,$bad +300]` `[!t{b} recolor,$o]` |
| `=` 戻す | その語より前に開いた状態を前の状態へ補間して戻す (`[=名{tok}]` も) | `[=org.l[2]]` `[=t{b} +600]` |
| `[*]` 一括 | ×N の全 instance に同じ印 | `[!r[*] check]` `[!list[*] strike]` `[<pa[*]]` |
| `[♪…]` | `[♪音 [±NdB] [fade=頭,末尾] [±N] [start=時刻] [peak=時刻] [to=時刻]]`。音 = `sound` の名 \| `"説明"` \| `id=8桁` | `[♪pon -4dB +200]` |
| (画面全体) | 閃光・暗転は全面の幕 `[veil 名] color=#FFFFFF opacity=0.6 z=curtain in=none` を印で: 閃光 = `[>名][!名 to,opacity=0,duration=400]`・暗転 = `[>名]` … `[<名]`。揺れは出ている要素ごとの `[!名 shake]` を同じ語に | `[>fl][!fl to,opacity=0,duration=400]` |

やり方 (状態): `.tag` (design の変種へ) `tint,$c` (薄い地 + 縁) `frame,$c` `glow,$c[,blur=][,spread=]` `underline,$c` `highlight,$c` (文字の後ろの地・箱は動かない) `strike,$c` (文字だけ・箱は `tint` / `dim`・線の太さは指定できない = 字の大きさの 1 割・最低 4px) / `[!名{tok} strike]` (文字の一部 = content の `{tok}…{/}` だけに線・左から・線は字の色で色は書けない) `fill,$c[,duration=]` (地色・地の無い文字は文字色・札 = `fill=` の文字は札の地・400) `recolor,$c[,duration=][,back=]` (文字・図形・icon・`{tok}`・250) `dim[,比][,duration=]` (0.35・400) `to,x= y= left= top= cx= cy= scale= rotation= opacity= w= h= pivot= arc= via=(x,y) duration= ease= rotationX= skewX= glow= color= fill= border= letter_spacing= blur= volume=` (`volume=` は曲だけ — 曲の既定の大きさからの dB・`0dB` で戻る・`[=#曲]` も戻す) (値は静止の姿からの絶対値 = GSAP・今の状態からは `x+=50`・行き先は `left= top= cx= cy=` — 子は親の内側から・根は canvas から・移動と伸縮も `to` で: `move` `scale` のやり方は無い) `focus[,比][,keep=名]` (×N の instance `名[k]` は 1 つの印で主役の切替: k を出し (前に k の印が無ければ — `[>名[k]]` を兼ねる)・沈んだ k を戻し・出ている他の instance を `比` (0.4) に沈める — `[!r[1] focus]…[!r[2] focus]` / 他の要素は兄弟 — 同じ親の見出しも — を幕で沈める・残す物は `keep=名`・次の focus が前を戻す) `count` (0 から数え直す) `text,"文"` (入れ替え・何度でも — 番号札 3 → 4 → 5 を 1 枚で・cut の最初の語に書けば cut の最初の frame から替わる (cut が 1 つだけの project でも) = 根の章の札 / 現在地を cut ごとに `[!ch text,"其の二"][!ch fill,$b]`・替えた文字と色は次の入れ替えまで cut を跨いで残る) `gray` (絵・写真・svg だけ — 文字・文字の札・図形は DEFECT:ARG・代わりに `dim` か `fill,$mute` / `recolor,$mute`) `sat[,比]` (既定 0.3) `filter,sat:…[,duration=]` `zoom_media,比[,duration=][,focus=]` `zoom[,倍率][,duration=]` (camera が寄る・1.35・cut の最初の語には書けない) `pulse[,回数][,opacity=a>b][,duration=]` `main,<design の main= と同じ値>` (その語から常時・`window=0,ms` で止める・窓は印の拍から) `check` (右上に ✓) `expression,表情` / `motion,仕草` (avatar・無い名は DEFECT:ARG)。
効果 (一回きり・`=` 不要・写しを作らず今の層が動く): `punch[,倍率][,duration=][,rotation=][,pivot=]` (1.18・450) `wiggle[,角度][,duration=][,count=][,x=,y=]` (揺れ・4°・180・2 往復・減衰しない) `pop` `spring` `swing` (この 3 つは揺れでなく出し直す着地) `shake[,px][,duration=]|x=,y=` (12・420) `settle[,倍率][,duration=]` (1.07) `blink[,回数][,duration=]` `ping[,色][,回数][,interval=][,duration=][,scale=始>終]` (輪は縁 = 1 から減速して広がる・既定 `1>1.6`・1 つの値は 1 からその倍率・1 重 600・`ping,3` = 280 ms おきに 3 重) `clear` (`>` だけ)。
引数の規則は 1 つ: 位置の数は 1 つ・色は `$名` / `#RRGGBB` で位置を問わない・残りは `key=値` (2 つ目の数を位置に書くと DEFECT:ARG — 直し方に key の形)。表は docs/draft_src_v2/mark-args.md (code から生成)。
拍 (やり方の後ろ・空白区切り): 無し = その語の頭 / `+N` `-N` = その語から N ms 後 / 前 (`+0` と無しは同じ) / `>` `>+N` = 同じ語で直前に並べた印の終わり (拍 + 所要) から N ms (GSAP の `">"`・語はまたげない・cue の本体でも同じ) / `cut-N` = `<` だけ・cut 末尾 (最終 cut は動画の終わり) の N ms 前に消え終わる (`cut+N` は DEFECT:ARG)。
`to` の値は絶対値 (GSAP): `x=100` = 静止の位置から 100 px・`scale=1.2` = 静止の 1.2 倍・`rotation=-30` = −30°・今の状態からは `x+=50` / `rotation-=10`。`x= y= scale= scaleX= scaleY= rotation=` は transform (CSS と同じく箱は変えない — 拡大した文字の隣の `名.right` は動かず、重なりと画面の外は check が箱で測るので見ない)・箱を変えるのは `w= h= left= top=`。`pivot=` は留める点 (`scaleX=1.5,pivot=left` = 左端から伸ばす・既定は scaleX が中心・w= が左上)。`to,…,repeat=N[,yoyo][,repeatDelay=M]` は一回きりの効果 (`repeat=-1` = 常時)。

### 時刻の規則 (覚えるのは 4 つ・残りは check が言う)
1. 印はその語の頭で効く。ずらすのは `+N` / `-N` (ms) と `>` (同じ語の直前の印の終わりから) だけ (design の `delay=` は印の語からの遅れで、印に `+N` を書けばそれが勝つ)。札 (stamp) も同じ (文末に出すなら文末の語に書く)。状態の印 (`.tag` `to` `fill` …) の `-N` は変種の `move=` の lead 込みで 1000 ms まで (超えると DEFECT:BEAT_TOO_EARLY・前の語に打つか lead を縮める)。
2. 同じ語に並べた印は**同時** (暗黙の連鎖は無い)。cue の印も同じ。
3. cut の外へは出ない: `-N` は cut の頭より前へ出られず (頭の `[silence:N]` か根の `silence head=` の無音の中は可)、`+N` が末尾を越えた分は描かれない (warn:BEAT_AFTER_CUT・GSAP の clip と同じ)。退場は cut 境界で終わる (退場を次の cut の入りに重ねるのは cut 末の `transition none,N`・旧場面ごと残すのは `overlap=`)。
4. 尺は合わせない: 動画の尺は台本で決まる。依頼の長さ・`target_s`・章の時刻は目安で、寄せるために話速・無音・台詞を変えない (TTS は合成のたびに揺れる)。演出の無音 (溜め・声の無い場面・締めの余韻) は書く: 声の無い cut は `@名: [>名 +N][silence:4s]` (cut 頭から N ms)・溜めは `[silence:0.8s][>札]`・余韻は `[silence:1.0s][>名][silence:2.0s]`。

書かなければこうなる (既定): cut 頭の印の無い要素は文書順に `[cut] stagger=` (120 ms) で組み上がる (`in=none` は数えない)・文字の下の細い横線 (`path=line_h` h≤8・印なし) はすぐ上の文字が `[>名]` で出るならその語で一緒に出る (線だけが先に走らない)・印の無い板 (子を持つ箱か、後の要素が `overlap=` で名指す div) は中身 (子と乗る要素) が全部 `[>…]` で出るなら最初の中身の語で一緒に出る (空の板が先に出ない — 先に見せたい枠は `[>板]` を書く)・`stagger=sentence` (雛形の根 `default cut = stagger=sentence`) なら印の無い文字と一覧 (×N・群) を頭に積まず、文書順の 1 つ目は cut 頭・2 つ目からは 2 文目以降の頭に 1 つずつ `[>名]` で出る (単位は名 / 群 / `名[k]`・文より多い分は最後の文に 120 ms ずつ・絵・箱・図形と `in=none` / `delay=` を書いた物は頭・自分で印 (どの動詞でも) を書いた物は頭のまま・足した印は保存の timeline に残る・`stagger=sentence,dim` は同じ単位を頭に全部出し 2 つ目からを入場から薄く置いて、その文の頭の `[=名]` で戻す)・最後の cut の末尾は書かなければ `[silence:3s]` (書けばその値・`[silence:0]` も — BGM の既定の余韻 (持ち上げと末尾の fade) はこの無音の中に収まる)・`[>名[*] +300]` は 300 ms 後に全部で間隔は印の `{stagger:{each:…, from:…}}` か design の入場の `in=…,stagger=`・`[>群 +300]` も同じ・子は親と同じ時刻と px で動き `[>子]` の印があればその時・cut の t=0 は切替の窓の始まり (check が `窓 N ms` と書く)・状態 (`!` の変種) は `=` か要素が閉じるまで続き、sticky の要素は cut を跨いでも続く・cut 末尾の印 (`…ます。[>札]`) は最後の語の頭 (後ろに置くなら `[silence:N]` を足して `+N`)・同じ拍の 1 状態 + 1 効果 / 2 効果は 1 つに畳む・絵文字つきの見出しはそのまま出る (TTS は読まない)・出した語と同じ拍の補間 `[>a][!a to,…]` と `{tok}` の印 `[>a][!a{t} strike]` は出現の 1 frame 後に送る (出た見た目を変えるなら `[>a .tag]`)。
check が止める物 (黙って直さない): 出ていない要素への `!` `=` = DEFECT:NOT_OPEN・`>` は要素ごとに 1 回。同じ語で同じ要素を拍を書き分けて移す印は拍ごとに続き (逆順の拍でも後の拍の状態が勝つ)、文字全体の変化と `{tok}` の印も同じ語に並べてよい。

### cue と切替
- cue: `cue 名(引数[=既定], …) = [印][印]…` (design の根)。本体は印だけ。引数は印の名の位置 (`x`) か派生 (`x.c`・`x[2]`)、やり方の中の `{引数}` は値 (数も)。`prev` = 同じ cut で前に呼んだ時の最初の引数 (最初の呼び出しでは `prev` の印を落とす)。呼び出し `[名 値 値 [±N]]` (空白区切り・既定値のある引数は省ける・末尾の `+N` / `-N` は展開した印の全部に足す)・印は並べた印と同じ = 同時。例: `cue on(x) = [=prev][!x tint,$a][!x.c fill,$a]` → `[on org.l[2]]`・`cue slam(x, s=2.4) = [>x pop][!x punch,300,{s} +300]` → `[slam v 1.3]`。
- 切替: `transition 種,ms[,key=値…]` (cut の末尾)・根の `transition = …` が既定。ms は 100〜3000。`overlap=N` = 窓のうち境界の後ろの長さ (既定 0 = 窓は境界の前)。窓が最後の声に掛かると check が warn (`transition_over_speech`)。幕の切替 (`dip` `flash` `panel`) は最後の cut と根の既定に書けない (DEFECT:TRANSITION_PLACE)。`se=音 [token…]` = 境目 (次の cut の頭) で鳴らす音 (`cut` 以外のどの種にも)。`sticky` / `z=front` の要素は切替の上に残る (次の cut の頭で閉じる帯も)。`transition cut` (ms 無し) = その cut だけ切替なし (根の既定を打ち消す)。`transition panel,1000,color=$色,label="01 原因"[,skew=-12][,label_skew=0][,dir=right]` = 斜めの色の帯が覆い、帯の裏で場面が替わる (章の名は既定で帯と同じに傾く・`label_skew=0` で立てる・大小は label の中の run `{sm}01{/} 原因`・章の帯・最後の cut と根の既定には書けない・label を読ませるので 1000 以上 — 短いと warn:flash_text)。幕 (dip / flash / panel) に `overlap=` `ease=` は書けない。
- `none,N` = 混ぜない: 次の cut は、この cut の退場が終わる N ms 前に始まる (旧場面を新場面の上にそのまま描く — 退場 (`out=`・`[cut] out=`・自動の閉じ) は境界 + N で終わる・N だけで key は無い・根の既定にも書ける)。`dissolve,ms[,overlap=][,zoom=][,ease=][,color=#色]` = 溶ける (linear が既定・`color=` = 旧場面を描かず色の上から出る — 400 ms を超えると暗転に見えて warn:DARK_DIP・`dissolve,300,overlap=300` = 窓が境界の後ろ — 前の cut の退場が済んでから溶ける)。`push,ms,dir=left|right|up|down[,overlap=][,ease=]` = 新場面が旧場面を押し出す (cut を跨ぐ sticky の地・帯と字幕は止まったまま)。`slide,ms,dir=[,offset=38%][,opacity=0][,drift=px][,dim=0.38]` = 新場面が滑り込む (旧場面は `drift=` だけ同じ向きへずれ、`dim=` まで暗く沈む — 頁替え)。`dissolve,…,dir=right,bars=…` = 溶けの上を帯が払う (帯は溶けと独立)。
- `wipe,ms,dir=[,bars=#色,18;#色,8][,drift=px][,angle=deg][,overlap=]` = 縁が走る (帯は 4 本まで・1 本目が新場面側・`linear(…)` 可・`linear(…,180)` = 帯の箱の CSS の向き (縦のグラデ))。`zoom,ms,dir=in|out[,zoom=1.08]` = 寄って / 引いて替わる。`dip,ms[,color=#000000][,level=1]` = 幕を挟む (前半で濃く後半で薄れ)。`flash,ms[,color=#FFFFFF][,level=1]` = 閃光 (ms/3 で光り残りで引く) — 峰の 1〜2 frame は画面が色だけになる (見比べでは白 frame の欠陥に数えられる)。cut の切替には使わず、閃光は全面の `[veil 名]` を語で出して `to,opacity=0` で引く。例: `wipe,700,dir=left,bars=#E8743B,18`・`dip,400,color=#FFFFFF,level=0.6`。

## 欠陥 — 効くか欠陥か
書いた物が効かない状況は全部欠陥。黙って捨てる・割る・丸める・詰めるは無い。

| 状況 | 結果 |
|---|---|
| ×N に枠 1 つで `stack` 無し | 横に並べる (縦長の枠は縦)。`stack=h\|v` の 1 枠の `w= h=` は枠全体 (N 等分して 40 px 未満なら DEFECT — 1 枚の寸法なら N 枚 + gap を書く) |
| 退場の `-N` が cut の頭より前・前の印と交差 | DEFECT:BEAT_BEFORE_CUT / BEAT_OVERLAP (直前の語まで詰めない) |
| `[cut] out=fade,40`・`[<名 cut-0]` + `out=` | 書いた ms どおり描く・境界で終わる |
| 出した語の後の子の punch・def の `out=`・`[count:… delay= ease=]`・`[card:x]` の `lead tail hold`・文字全体の `recolor` | 効く (子に継ぐ・補間する) |
| `to` の後の `.tag`・`pattern=` だけの箱・群の clip の箱の border | 重なる (位置は戻らない)・地は透明 (既定の白地は無い)・clip の窓は border の外周 |
| run の class が無い `{t}…{/}` | 印の的だけ (可)。`{hl}` が class でも的でもなければ DEFECT:RUN_UNKNOWN |
| 同じ語の印・cue の印・`+N` | 同時 (規則 2)。`+N` は ×N でも群でも遅れだけ (規則 3)。札の文末着地 (`now`) は無い (規則 1) |
| runtime の値域・大文字の名 | compile が検査し DEFECT:RANGE に下限・上限を書く (`Input should be ≥ 0` は出ない)・DEFECT:NAME (読み替えない) |

報告の形 `DEFECT:コード  file:行 [section か *** cut]  原因。直し方: …` (1 行 1 件・著者の語彙で)。欠陥の section は捨てて compile を続け、その名を指す印・参照は巻き添えの欠陥に数えない。似た名・似た key があれば `似た名: a, b`。段: DEFECT (描けない・compile が止める) / severe (描けるが崩れる = `overflow occluded offcanvas`) / warn (engine が書いた値を変えた・判定で損 = `overridden shrunk transition_over_speech`) / info (参考 = `SAME_AS_DEFAULT Z_CHILD substituted long_still`)。直すかは段でなく規則の台帳の直しの列・`lint off=` は台帳の mutable の規則の warn / info を黙らせる。コード: `VERSION TAB INDENT NAME UNIT COLOR QUOTE ARG KEY KEY_DUP REF ROOT_AFTER_CUT DUP_NAME DUP_CUT CUT_UNKNOWN CHILD_UNKNOWN CHILD_TYPE NAME_SHADOW TIMES_N_FRAME FOLD TRANSITION_PLACE FADE_MARK BEAT_BEFORE_CUT BEAT_AFTER_CUT BEAT_OVERLAP NOT_OPEN RANGE SVG_VIEWBOX ASSET_AMBIGUOUS RUN_UNKNOWN ICON_UNKNOWN SHAPE_UNKNOWN EASE_UNKNOWN CAST_KIND CSS`・check の配置の崩れ severe `overflow occluded` (engine が解けなかった収まり — 描けるが崩れる)。決定性: 素材 id・font の pin は `src.json` (`asset_pins`)。曖昧な説明文は check が解いて pin に書く。pin に無い素材を説明文で書いた src は決定的でない。

書き間違えやすい物 (check が DEFECT にし、直しの 1 往復 10〜15 s が乗る — 担当の版で多い順):
- 効果 (`punch` `shake` `pulse` …) の key は duration= rotation= pivot= scale= だけ。`stagger` は出現 (`[>#c[*] {stagger:{each:0.08}}]`) と入場の tween の中にだけある
- `to` の key は x= y= (base からの px) left= top= cx= cy= (行き先) scale= (倍率) だけ — 幅や高さは `width=` / `{w:…}` でなく、静止の別の姿を変種にして移る (`#名.wide(width: 420px)` → `[!#名 .wide]`)
- `flip=` は名前の icon と写真・絵・svg だけ (文字・箱には無い)
- 塗りを焼く箱 (`background:` のある div) は width と height の両方が要る (`def` の `p` を div に替えた時に抜けやすい)
- 字下げした行は親 (div / group) の子だけ。親の無い要素の行は字下げしない
- 随伴 (`overlap: 親` で親に乗る札・判子) は親を動かす語より前の語で出す。同じ語で出して動かすと DEFECT

## HTML の動画を写すとき (HTML + GSAP の動画を NoLang で)
- 切替: 古い場面が境目で消え新しい場面だけが黒の上で opacity 0→1・scale 1.08→1 → `transition = dissolve,320,color=#000000,zoom=1.08,ease=power2.out` (根の既定にも)・新しい場面が不透明な旧場面の上に重なる → `dissolve,600,overlap=600`・黒 / 白の挟み → `dip,400` / `dip,600,color=#FFFFFF`・横に払う色帯 → `wipe,700,dir=left,bars=#E8743B,18` (境界から払うなら `overlap=700`)・斜めの光の帯 → `wipe,340,dir=right,overlap=170,angle=14,bars=linear(#00E5FF00,#00E5FF@30%,#FFFFFF,#FF2BD6@70%,#FF2BD600),470`・cross fade の上を光の帯が払う → `dissolve,850,overlap=850,dir=right,bars=linear(#F5B54400,#FFD27F8C@97%,#FFD27F00),173`・払う線の上下のグラデ → `wipe,600,dir=right,bars=linear(#7ADFD300,#7ADFD3F2@30%,#F6C35BF2@70%,#F6C35B00,180),3`・頁替え (旧頁が `x:-360` へずれて暗む) → `slide,850,dir=left,drift=240,dim=0.38`・`clip-path: circle(0% at 50% 0%)` から開く → `in=circle_wipe,750,ease=power2.inOut,pivot=top` (円の中心は pivot の 9 名)・`xPercent:38,opacity:0` で被さる → `slide,260,dir=left,offset=38%,opacity=0,ease=expo.out`・場面の要素が一斉に去る leave() → `[cut 名] out=x=-26,opacity=0,duration=400`・旧場面の一部だけ流す → その要素に `out=x=-140,ease=power1.inOut,duration=700` + `[<box cut-0]`・旧い板が抜ける間に新しい板が入る (`tl.to(old,{y:-28,opacity:0,duration:.42}, t)` の直後に新しい場面) → `transition = none,370`・黒から入る → `fade in,1800`。切替の窓には次の cut の頭の層が描かれ入場も窓の頭から走る — 帯が過ぎてから入れるなら `delay=尺`。
- 時刻: 声の尺は元の動画と違ってよい (`[silence:]` で合わせない)。要素・切替・字幕は**台詞の同じ語**に合わせる (元の動画でその語の何秒後に出るかを見て `+N`)。配列の同時の tween (`tl.to([a, b], …)`) = 同じ語に並べるだけ (同時)・順に続くなら `+130` `+260`。
- 素材: 声・BGM・効果音・書体は元の動画と同じ素材を `id=8桁` か表示名で固定・同じ人物は根の `image 名 = "…"` + `content="[ref:@名]場面"`・同じ写真の差分は `[ref:@名]消す物 / Edit only the sky to dusk`。絵の中身・構図は作り直してよい — 一貫性 (`[ref:@名]`) と文脈 (台詞の被写体が写る) を保ち、絵に重ねる輪・矢印は新しい絵に合わせて置く (render の frame で確かめる)。
- 入場: GSAP の px (`y: -44`) → `in=y=-44,opacity=0,duration=600`・keyframe 列 (`fromTo({x: 441})` + 行き過ぎ) → `in=keys(at=0 x=441 opacity=0 | at=0.7 x=-8 ease=power2.out | at=1 ease=sine.inOut),duration=900` (子は同じ px で一緒に動く)・`scaleX: 0` の罫 → `in=wipe,center`・文字を 1 字ずつ → `in=rise,20,400,stagger=40`・`stagger: {from: "random"}` → `[<名[*] from=random]`・CSS の `border` は箱の外・`border=` は内側 (w / h に線幅 × 2 を足す)。
- 動き: 1 文の中で続ける tween (`-15° → -30° → -22°`) → 静止 `rotation=-15` + 1 語に拍を書き分けた `to` (`[!a to,rotation=-30,duration=600 -50][!a to,rotation=-22,duration=550 +750]`・GSAP と同じ絶対値・相対は `rotation+=8`)・揺れ (`rotation:4, x:30, .18s, yoyo, repeat:3`) → `[!a to,rotation=4,x=20,duration=180,repeat=3,yoyo]` か `[!a wiggle,4,duration=180,count=2,x=20]`・広がる波紋 (輪 0.3→1.6) → `[!a ping,scale=0.3>1.6]`・語から始まる浮遊や流れ → `[!a main,sine,y=-7,freq_ms=1100,window=0,3300]`・`motionPath` / 弧の入れ替え → `[!a to,x=760,arc=0.4][!b to,x=160,arc=0.4]`・scale と位置の Ken Burns → `main=kb,1.04@55%,48%>1.17@45%,50%`・`attr: {points}` の tween → `[shape s .ex] points="…"` + `[!s .ex]`・2〜4 重の波紋 → `[!名 ping,3,interval=280]`・白い閃光 → 全面の `[veil fl] color=#FFFFFF opacity=0.55 z=curtain in=none` + `[>fl][!fl to,opacity=0,duration=400]`・画面の揺れ → 出ている要素ごとの `[!名 shake,6,duration=2200]` を同じ語に・odometer → `[count:400 roll ms=1150,1000,850]` (回らない上位の桁は `ms=0,0,1380,1460`)・`background-position` で走る光 → `[group g] sheen=g.bg,900,soft,ease_in_out`・`perspective: 520px` + `rotateX(70deg)` の床 → 群に `main=constant,rotationX=70,depth=4,pivot=top`・公転 → `[group orb] main=spin,9000,pivot=orb.sun`・奥へ回り込む公転 (GSAP の zIndex の切替) → 同じ軌道の写しを相手の下に置き、square の alpha で半周ずつ見せる (`[!#orb.oy.earth main,square,alpha=1,freq_ms=T,phase_offset=p]` / 奥の写しは `alpha=-1`・p は y の sine と同じ)。
- 文字の一部: `余裕` だけ 1.12 倍 → `content="…{t}余裕{/}…"` + `[!名{t} punch,1.12,duration=440]`・色の tween (0.25 s → 戻り 0.4 s) → `[!名{t} recolor,$o,duration=250,back=400]` … `[=名{t} +600]`・語の下帯 (`linear-gradient(transparent 62%, 色 62%)`) → `run m = marker=$y,38%` + `[!名{m} marker]` (帯は文字の直下の段で行の箱 (line-height) の下から比だけ・字の下へはみ出す。字幕では run の地で同じ形 (印の拍では伸びず札と一緒に出る))・拡大したまま保つ → 別の文字に分けて `[text t2] left=t1.right top=t1.top overlap=t1` + `[!t2 to,scale=1.08]`。
- 配置: `display:flex` の行と列はそのまま書ける — 横は文字幅のまま並び `flex: 1` の子が残りを取る (icon + 文字の行)・縦は子の実の高さ + `gap` で積む・`align-items` / `justify-content` の center / flex-end / space-between は子の寄せ・`margin-left:auto` は `right=`。
- 見た目: `skewX` → `skewX=-12` (語で `[!名 to,skewX=12]`)・`rotateX` の立体 → `rotationX=30 depth=0.8` (下辺を軸に `main=constant,rotationX=30,depth=0.8,pivot=bottom`)・`scaleX: -1` → `flip=x`・`box-shadow: 0 0 0 14px` → `shadow=0,0,0,14,#色`・`filter: saturate() sepia()` → `filter=sat:0.3,look:sepia` / 語で `[!名 filter,duration=600,sat:0]`・全面の `mix-blend-mode: saturation` → `[veil g] filter=sat:0 z=front` を `[>g]` … `[<g]`・`background-clip: text` の金文字 → `color=linear(#FFE58A,#C2410C,180)`・`linear-gradient(… 42%, … 72%)` → `fill=linear(#a,#b@42%,#c@72%,90)`・`repeating-linear-gradient(100deg, …)` → `pattern=hatch,10,…` (CSS の勾配の向きと 90° ずれる)・`mask-image` + 単色 → `filter=look:#色`・duotone → `filter=look:#暗/#明`・写真の上の光 → `[div lk] inset=0 fill=radial(#FFE6A0,#00000000,70%,25%) blend=screen`・写真の暗幕 → `[image p] scrim=right,0.45`・`transformOrigin` → `pivot=`・`steps(1)` → `ease=steps(1)`・左右 2 色の札 → `[text b] left=a.right top=a.top radius=0,99,99,0 overlap=a`・両脇の線 → `rules=both,36,2,$a`。
- 字幕: 元の動画の句の割り方 → `[|]` (札だけ切る)・`[||]` (文を跨いで 1 枚)・`subtitle "…"` の上書き・`[subtitle] min_phrase=0`。句ごとに傾き・入り方・色ずれが違う字幕 → `[subtitle .変種]` を句の数だけ + 札の頭に `[card:変種]`・切替の前に字幕だけ先に消す → `[subtitle .early] tail=0 hold=off` + `[card:early]`。
- 場面の組み立て: 「空にしてから組み立てる」 → 切替を書かない + 前の cut に `[cut 名] out=…` + 次の cut の要素に `delay=`。場面の頭の札 (章・STEP) には印を付けず cut 頭に (`[cut 名] stagger=0` で一斉)。通しの章の札 (sticky の帯) を cut ごとに置き直さない — 根に 1 つ + 変種 `[!bar .s2]` か文字の差し替え `[!bar.t text,"2 / 5"]` で段を替える (章・STEP・累計の常設は 3 分以上の動画だけ・上端に・飾りの header は置かない)。元の動画に無い効果 (閃光・弾む入場) を足さず、小さな飾り (カーソルの名札・点・鳥) も省かない (`[group]` + `to`・`path=scatter,n=800,seed=3`・`ping,n`)。camera の寄る cut で `cam=none` の見出しより上に幕を出すなら幕に `cam=none z=curtain`。

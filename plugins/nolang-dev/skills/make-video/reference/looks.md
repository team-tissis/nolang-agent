# 見た目の組と見本 (判定で勝った実 src・check を通る design + timeline)

色・書体・文字の段・板・地は題材ごとに決める物で、値は見本。
素材 (話者・BGM・書体・絵) は説明文で書いている。

## style の組 (気分で 1 つ選び、根の 4 行に写す)

| 組 | 気分 / 向く題材 | `palette` | `font` / `fonts` | 動き (`motion`) / `transition` | しない事 |
|---|---|---|---|---|---|
| 端正な格子 | 精密・SaaS・data・開発 | 暗 `#141414`・accent 1 色 (電気の青 / 琥珀) | 太い角ゴシック / 細い角ゴシック・数字は等幅寄りの欧文グロテスクで 80〜180px | 締まる / `dissolve,300,overlap=300` か hard cut | 飾りの切替・丸い角 |
| 静かな高級 | 高級品・企業・基調講演 | 黒 + 白 + 濃紺か金 1 色 | 細い角ゴシックの大文字 + 字間広め / 明朝・数字は細めの欧文セリフ | 行き過ぎない / `dissolve,300,overlap=300,ease=power2.inOut` | 速い動き・詰め込み |
| 分解 | 技術の発表・警告・反骨 | 黒 + 赤か黄 1 色 | 極太の角ゴシック + 等幅・数字は極太の欧文グロテスク | 締まる / `wipe,400,dir=left` か hard cut | 柔らかい ease・中央揃え |
| 大型の文字 | 発表・告知・音楽 | 鮮やかな 2 色 + 黒 | 極太の角ゴシック (画面幅の 8 割)・数字も極太の欧文サンセリフ | 弾む / `push,300` | 小さい字・余白の多さ |
| 流れる data | AI・未来・科学 | 濃紺 + 青緑の光 | 細い角ゴシック + 等幅・数字は欧文の等幅 | ゆっくり溶ける / `dissolve,300,overlap=300,zoom=1.06` | 定規の目盛り・凡例 |
| やわらかい信号 | 健康・個人の話・ブランド | 明 (生成りか淡い色) + 暖色 1 色 | 明朝 + 細い角ゴシック・数字は丸みのある欧文サンセリフ | 行き過ぎない / `dissolve,300,overlap=300` | 角張った札・黒 |
| 民藝の色 | 食・地域・祭・消費者向け | 明 + 鮮やか 2〜3 色 | 太い丸ゴシック + 筆の見出し・数字は太い丸ゴシック | 弾む / `wipe,600,dir=right` | 無彩色・薄い字 |
| 影と切れ | 事件・暴露・映画 | 黒 + 白 + 赤 1 色 | 極太の明朝 + 細い欧文・数字はクラシックな欧文セリフ | ゆっくり溶ける / `dip,400` `zoom` | 明るい地・丸い角 |

全面の絵に文字を重ねる cut で、文字が絵の主体に乗りそうな時だけ、主体の置き場を文字の反対側に宣言する — `img#p(inset: 0; subject: top 35%; room: bottom 55%) 説明` + 文字は下 55% に。宣言は「重心をそちらへ・文字の側は静かな背景に」の希望で、主体の大きさや寄り引きは本文の prompt が決める。`face=` か `room=` を書いた絵は、生成した絵の顔 (主体) が文字の側に掛かれば範囲に収める文で 1 回だけ作り直す (2 枚目は通らなくても採る — check の表に「作り直し 1 回」)。文字が主体に乗らない絵 (小さな札・帯の上の文字・絵の外の文字) には書かない — 全部に書くと絵が同じ構図に揃う。

組を決めたら、根に `palette` `font` `fonts` `motion` `transition` を書き、以後の cut はその差分だけ。 数字 / 強調の書体 (`fonts`) も組ごとに違える — 骨組みの値を写さない。欧文 (数字・英字) の記述なら欧文専用の書体も候補になる (和文の字は代わりの書体が描く)。切替は 1 本 1 種が基本 (章の境目だけ別の 1 種)。dissolve は 300 ms 以下 + `overlap=` 同じ尺が無難 — 窓が境界の前に掛かると退場中の文字が次の絵に重なり、400 ms を超える溶けは前の絵が残像に見える。`motion` は雛形の 5 行 (題 title・主役の語 big・箱 div・本文 row・注記 note — 締まる / 行き過ぎない) の値を気分に合わせて書き換える (弾む動きは見本 story_03 の根)。組は例で、題材に合わせて自分で作ってよい (名 → 色 2〜3 → 書体 2 → 動き → 切替 → しない事 2 つ)。前後の値は両方とも読める濃さで (前を灰で沈めるなら字は太く大きく)。

## 見本 (reference/samples/ — 自分の type の 2 本を読む。stream の 3 役には hf の写し 2 本を同梱する (`reference/stream.md`)。story → story_*・concept → concept_*・data / compare → data_* と compare_*・cinematic → cinematic_*。題材が同じ見本は読まない)

- `samples/story_03.md` — story・夏フェスのオタク語り (縦・構文風の一人語り)・1080x1920・44.5s・139 行・文法: count・×N・stack・manner・se・sticky・def・run・bgm 切替
- `samples/story_06.md` — story・ニホンカワウソ (縦・台本そのまま・絵本調)・1080x1920・57.8s・145 行・文法: ×N・stack・manner・se・sticky・def・run・bgm 切替
- `samples/story_13.md` — story・碓氷馬車鉄道 (縦・語り + 2 人の役・錦絵調)・1080x1920・69.8s・159 行・文法: ×N・stack・manner・se・sticky・def・run・bgm 切替・2 cast+
- `samples/concept_10.md` — concept・サルトルと「やりたいこと」(縦・線画・静かな語り)・1080x1920・49.8s・133 行・文法: manner・se・sticky・def・run・bgm 切替
- `samples/concept_16.md` — concept・麻辣湯の解説 (縦・章立て 13 cut・写真 + 板)・1080x1920・125.0s・231 行・文法: ×N・stack・manner・se・sticky・def・run・bgm 切替
- `samples/concept_17.md` — concept・和風きのこパスタ (縦・手順 + コツ)・1080x1920・72.3s・153 行・文法: ×N・stack・manner・se・sticky・def・run・bgm 切替
- `samples/compare_05.md` — compare・通常 CAD とリバース (横・比較 + 流れ図)・1920x1080・170.2s・256 行・文法: 流れ図の札 (def node ×N + 位置の式の矢印)・比べる 2 列 (div の段 ×N)・count・×N・stack・manner・se・sticky・def・run・bgm 切替
- `samples/cinematic_05.md` — cinematic・奥多摩の渓流の朝 (横・実写調・台詞 5 文の観光 PR)・1920x1080・33.0s・99 行・文法: 常設の質感 (根の veil の周辺減光と grain)・絵の置き場 (subject / room)・同じ cut で絵を重ねて替える・count・recolor・filter・hide_subtitle・read・場の音・bgm
- `samples/data_18.md` — data・家計の固定費 (横・前後の数字 + 棒グラフ)・1920x1080・74.3s・180 行・文法: 横棒の段の def (hbar・幅は %)・count・×N・focus・stack・manner・se・sticky・def・run・bgm 切替
- `samples/hf_compare_04.md` — compare・care-transfer・1920x1080・230 行・hf (全力版) の全量の写しを見本の形に: 常設の章札と進行 3 本・色の板で払う章の区切り・話者札つきの字幕・svg 部品の図
- `samples/hf_concept_01.md` — concept・b2b-support・1920x1080・392 行・hf (全力版) の全量の写しを見本の形に: 写真が主役の場面ごとの絵替え・左下のテロップ札と STEP 章札・def の部品で組むタブレットの画面 (カーソル・強調枠・吹き出し・page 送り)・cue で段を送る進行の板・1 字ずつ上がるロゴ
- `samples/hf_concept_07.md` — concept・black-tire・1080x1920・191 行・hf (全力版) の全量の写しを見本の形に: 常設の上下の暗幕と上端の進行線・場面ごとの全面写真 (動く cam・黒から溶ける切替・文の途中の絵替え)
- `samples/hf_story_02.md` — story・office-comedy・1080x1920・164 行・hf (全力版) の全量の写しを見本の形に: 常設の題の帯・冒頭の組織図・台詞ごとの絵替え・2 行テロップの def
- `samples/hf_data_08.md` — data・cityhall-hours・1920x1080・241 行・hf (全力版) の全量の写しを見本の形に: 常設の帯 (紺の丸札・sticky)・時計の盤の def (針は回した細い箱)・濃紺の札の字幕・題の札と mask から上がる 2 行と下線
- `samples/hf_story_09.md` — story・soma-nomaoi・1920x1080・270 行・hf (全力版) の全量の写しを見本の形に: 黒からの開幕と全編の周辺減光・grain・字幕の下の陰・漂う塵
- `samples/hf_story_03.md` — story・fes-otaku・1080x1920・330 行・hf (全力版) の全量の写しを見本の形に: 常設のネオンの地 (グラデ・光の柱・透視の格子の床)・画面中央に 1 句ずつ叩きつける極太の大字幕 (句の型ごとの札の変種)・写真カードの場面
- `samples/hf_compare_05.md` — compare・cad-reverse・1920x1080・386 行・hf (全力版) の全量の写しを見本の形に: 方眼の地と 2 色で通す比較・語ごとに埋める 2 段の流れ図・工程の板の点灯 (cue)・path の形が変形する図・点群とメッシュ
- `samples/hf_story_06.md` — story・river-otter・1080x1920・202 行・hf (全力版) の全量の写しを見本の形に: 全編の質感 (黒から明ける頭・周辺減光・grain・明朝の字幕)・台詞の中で語ごとに溶けて替わる全面写真・「居ない版」の差分で 1 匹だけ溶かす
- `samples/hf_concept_10.md` — concept・find-interest・1080x1920・215 行・hf (全力版) の全量の写しを見本の形に: 生成りの紙の地と上端の章札・場面ごとの中央の線画・要素が一斉に左へ抜ける場面替え・3 段の文字 (前置き → 主文 + 下線 → 注記)・番号つきの札

## 文法で書けなかった物・罠

1. **字幕の語の印は色と地だけ** — `run m { marker: 色 }` は字幕では字の高さいっぱいの地 (比は効かない)・語の下の細い帯は字幕に敷けない (design の文字なら `[!#名{m} marker]` で伸ばせる)。
2. **`path: "M…"` / `points:` の shape は枠 (left top width height) を持てない** (点は canvas px) → `×N` で並べられず 1 本ずつ書く (名の形 `path: zigzag` などは枠を持てる)。
4. **箱の影は 2 本まで** — CSS と同じく `box-shadow: a, b` で重ねる (輪 + 落ち影・光彩 + 落ち影)。3 本目は近い影にまとめる。硬い影は blur 0 (`box-shadow: 12px 12px 0 $ink`)。
5. **組み込みの部品は無い**: 人物の舞台 (箱 + 地の形 + 透過の人物 = 3〜4 行)・結論の帯 (地つき icon + 文 + tag = 3 行)・手順の札 (番号 + 文 = 3 行)・lockup (3 行) は繰り返すなら `def` に畳む (authoring.md「根の雛形」)。
6. **icon の地は 1 行** — `icon#i(font-size: 60px; name: leaf; background: $a)` で丸い地 (`border-radius: 18px` で角丸の四角・`padding:` は既定 size の 0.3・icon の色は地と反対の ink)。地の箱は size + 2 × padding で、書いた left / top と位置の式の辺もこの箱。線の icon (Lucide の名・`in: draw`) と著述の icon の地も同じ書き方 (描き出しは線だけ・地は fade で出る)。
7. **`run` に letter-spacing が無い** — 小見出しの字間は文字ごとに `letter-spacing:`。
8. **`div` は素の箱** — CSS の div と同じく地・縁・影・角丸・余白を持たない (容器はそのまま書く)。板は宣言で書く: `div#c(…; background: $panel; border: 2px solid $line; border-radius: 24px; box-shadow: 0 6px 18px #0003; padding: 36px)`・繰り返すなら `def card = div(…)` か根の `div { … }`。暗い theme の塗りの板は glass (淡い縁つき — 縁を消すなら `border: none`)。
9. **縦書きの主文は 1 列 600 px まで** (8 字 × 76 は入らない・`height` を超えると offcanvas) — 字数か size を落とす。
11. **棒の長さは著者が計算する** — 横棒は `width: {v}%` (段の内側の幅の比) で、値 ÷ 最大 × 棒に使える比 (段の幅 − 札 − 値の札) を書く。値 0 は `1%` の切れ端で見せる。行の色は ×N の `;` の列 (`c: "$mute;$a"`)・語で替えるなら `[!#名[k].b fill,$c]`。
13. **記述の書体は字ごと幅の詰め組み書体に当たりにくい** (「詰めて組める」と書いても等幅かなのゴシックに解決) — 行頭の「 が空くので見出しは括弧を使わず `run` の色で強調する。欧文の記述は代替字形の癖の強い family に当たることがあり、「細い / 細身」は写真の上で読めない Light になる — render の frame で字形を見て記述を替える。
14. **縦の字幕は 34 px で 18 字を超えると札の余白が潰れて縁に付く** (warn は出ない) — 台詞に `[|]` を置いて札を割る。
15. **台詞の「1月」は `{1月|いちがつ}` や `read` を書いても `month_reading` が消えない** — 言い換える (「真冬の請求」)。読みの誤りは後段の読み検査が拾う (「反動は」→「反動を」と読まれた例)。

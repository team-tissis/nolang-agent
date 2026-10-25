# story · fes-otaku (hf 全力版の全量の写し — 夏フェスに人生を捧げるオタクの熱狂的な語り・中央に 1 句ずつ叩きつける大字幕と 6 場面の写真カード + 情報パネル) — canvas 1080x1920

見せる作り: 常設のネオンの地 (青→赤のグラデ・漂う光の斑・揺れる光の柱・透視の格子の床・走査線) と上端 (進行線・ドット書体の番号の章札・タグ)・画面中央に 1 句ずつ極太の大字幕 (句の型ごとの札の変種 — 決め語の傾き・驚き・判子・色ずれの分身・被弾・復活・沈む・勝利の金)・字幕を閉じて design の文字で積む 3 つの「待て」と締めの「震えて待て」・上の写真カード + 下の情報パネルを語で組む (通知のバナーとドット時計・タイムテーブルと地図のピン・数える温度計・HP ゲージ・比べる 2 列・予告のカレンダーと流れる帯)・語ごとの揺れと白の閃光・全面を灰に沈める色調の幕・閃光で切り替える全面の勝利 (放射光・紙吹雪)・斜めの光の帯の切替・音の層 (3 区間の BGM + 語に結んだ効果音 40)

```design.txt
#v2
# 学ぶ作り: 全編に敷く常設の地 (青→赤のネオングラデ + 漂う光の斑 + 揺れる光の柱 + 透視の格子の床 + 走査線) と常設の上端 (進行線・章札・タグ)
# 字幕が主役: 画面中央に 1 句ずつ極太の大きな札 (句の型ごとに字幕の変種 — 判子・色ずれ・突進・勝利の金)・3 つの「待て」と締めの「震えて待て」は字幕を閉じて design の文字で
# 場面 = 上の写真カード + 下の情報パネル (通知・タイムテーブル・温度計・HP ゲージ・比べる 2 列・予告) を語で組み、語ごとに揺れ・閃光・効果音を当てる
# hf 03 fes-otaku (全力版) の全量の写し。座標は hf の 1080x1920 × 2/3
canvas 1080x1920 bg=#07031A
theme dark
palette y=#FFE94A c=#3FF5FF m=#FF2BD6 red=#FF2448 ink=#0B0730 navy=#120A3A
font "とても太い角ゴシック、Black の太さ"
fonts d="極太で丸みのあるポップな見出し用ゴシック" dot="ドット絵のようなレトロなビットマップのゴシック、デジタル時計の数字"
sfx off
# hf の作り: 章札・通知の題・パネルの見出しを台詞より先に見せる (spoiler)・3 つの「待て」は同じ語を積む (duplicate_text)・句の札と「待て」は 1 秒未満で替わる早口の作り (flash_text)
# hf の作り: 効果音は語ごとに 40 発 (se_dense)・光の帯は声に掛けて払い、場面の頭の板も帯の中で組む (transition_over_speech・entrance_in_transition・entrance_in_fadeout)
# hf の作り: 地の光の柱と斑は中央の字幕の後ろにも敷く (caption_collision)・ピンの名札と SAME TIME の札を縦に重ねる (stacked_labels)・判子の後に推しの枠を沈める (low_contrast)・色は部品ごとに直書き (palette_drift)
lint off=spoiler,duplicate_text,flash_text,se_dense,transition_over_speech,entrance_in_transition,entrance_in_fadeout,caption_collision,stacked_labels,low_contrast,palette_drift
prompt_tail "文字・ロゴは一切無し。人物なし。"
# 字幕の語の色 (句の型ごと)・通知の題の黄の下帯・章札の番号
run y { color: $y }
run r { color: #FF3B6B }
run red { color: $red }
run o { color: #FF8A1F }
run cy { color: $c }
run dmg { color: #FF3B5C }
run cl { color: #7FE3FF }
run hot { color: #FF4FA8 }
run gold { color: #FFD84A }
run m { marker: $y,45% }
run no { color: $c; font-family: dot }
cut { stagger: 0 }
p { color: #FFFFFF; out: none }
div { border: none; out: none }
img { out: none }
svg { out: none }
shape { out: none }
group { out: none }
sound vibe = "スマートフォンのバイブレーションの短い振動音"
sound notif = "メッセージ受信の通知音、ピロンと鳴る短く明るい電子音"
sound sweep = "短く鋭いノイズのスイープ音"
sound scratch = "DJ がレコードを急に止めるスクラッチ音"
sound cymbal = "ドラムのシンバルを一打、明るく響く"
sound swish = "短く鋭い風切り音、シュッ"
sound dash = "素早く動くモーションの風切り音、少し長め"
sound stamp = "判子を強く押す乾いた音"
sound shock = "ドーンと響く衝撃のオノマトペ、リバーブ付き"
sound glitch = "ホラーのアクセント音、短く歪んだノイズ"
sound cicada = "真夏のセミの鳴き声"
sound run = "地面を蹴って走る足音"
sound dmg1 = "レトロゲームの RPG でダメージを受ける電子音"
sound dmg2 = "レトロゲームのダメージ音、低く鈍い別の種類"
sound riser = "上昇していくような風の音"
sound revive = "レベルアップ、経験値アップの明るい効果音"
sound cheer = "大観衆の歓声、高く長い"
sound heart = "ドクンと一回鳴る心臓の鼓動"
sound boom = "爆発音、ドカーン"
sound pikiin = "ひらめきのピキーンという高い音"
sound bass = "重く響くベースの一音"
sound jaan = "ジャーンと鳴るワンポイントの効果音"
sound tremble = "ブルブルと震えるモーションの音"
# 同じ会場・同じステージを 2 度使う絵は根に 1 回
image grounds = "[photo]夕暮れの巨大な野外音楽フェス会場を高所から見下ろす写真。遠く離れた位置に2つの巨大なステージがあり、左のステージは青、右のステージは赤い照明で光っている。間には広大な芝生と通路が広がる。開場前で無人。空は青から赤へのグラデーション。シネマティック。"
image stage = "[photo]夜の野外フェスのメインステージを客席側の正面から捉えた縦構図の写真。青と赤のレーザー光線が夜空へ放射状に伸び、スモーク、舞い散る紙吹雪、巨大なスピーカーと照明リグ。ステージ上も客席も無人。スクリーン表示は一切無し。迫力のあるコンサート写真。" aspect=9:16
# 勝利の放射光 (20 本の楔・中心から外へ消える)・陽炎の線・4 つ角の星
svg rays = """<svg viewBox="0 0 200 200"><defs><radialGradient id="g"><stop offset="0" stop-color="#FFE078" stop-opacity=".42"/><stop offset=".35" stop-color="#FFE078" stop-opacity=".34"/><stop offset=".7" stop-color="#FFE078" stop-opacity="0"/></radialGradient></defs><path fill="url(#g)" d="M100 100L100.0 0.0A100 100 0 0 1 112.2 0.7ZM100 100L130.9 4.9A100 100 0 0 1 142.3 9.4ZM100 100L158.8 19.1A100 100 0 0 1 168.2 26.9ZM100 100L180.9 41.2A100 100 0 0 1 187.5 51.5ZM100 100L195.1 69.1A100 100 0 0 1 198.2 80.9ZM100 100L200.0 100.0A100 100 0 0 1 199.3 112.2ZM100 100L195.1 130.9A100 100 0 0 1 190.6 142.3ZM100 100L180.9 158.8A100 100 0 0 1 173.1 168.2ZM100 100L158.8 180.9A100 100 0 0 1 148.5 187.5ZM100 100L130.9 195.1A100 100 0 0 1 119.1 198.2ZM100 100L100.0 200.0A100 100 0 0 1 87.8 199.3ZM100 100L69.1 195.1A100 100 0 0 1 57.7 190.6ZM100 100L41.2 180.9A100 100 0 0 1 31.8 173.1ZM100 100L19.1 158.8A100 100 0 0 1 12.5 148.5ZM100 100L4.9 130.9A100 100 0 0 1 1.8 119.1ZM100 100L0.0 100.0A100 100 0 0 1 0.7 87.8ZM100 100L4.9 69.1A100 100 0 0 1 9.4 57.7ZM100 100L19.1 41.2A100 100 0 0 1 26.9 31.8ZM100 100L41.2 19.1A100 100 0 0 1 51.5 12.5ZM100 100L69.1 4.9A100 100 0 0 1 80.9 1.8Z"/></svg>"""
svg waves = """<svg viewBox="0 0 160 120"><g stroke="#ffb27a" stroke-width="8" fill="none" stroke-linecap="round"><path d="M30 110 C10 80 50 60 30 30 C20 15 35 5 40 0"/><path d="M80 110 C60 80 100 60 80 30 C70 15 85 5 90 0"/><path d="M130 110 C110 80 150 60 130 30 C120 15 135 5 140 0"/></g></svg>"""
svg spark = """<svg viewBox="0 0 100 100"><polygon points="50,0 61,39 100,50 61,61 50,100 39,61 0,50 39,39" fill="#ffffff"/></svg>"""
# BGM は同じ疾走感の曲を 3 区間: 冒頭は籠った音 (lowpass) → 「待って」から頭出し → 「限界？知らん。」で止めて無音 → 「完全勝利」で曲の山から
bgm#music_a(volume: 2dB; lowpass: 650; fade: 400,60) 疾走感のあるアップテンポの明るい EDM ポップ、シンセのリードと力強いドラム、夏フェスの高揚感
bgm#music_b(volume: 5dB; fade: 0,50) 疾走感のあるアップテンポの明るい EDM ポップ、シンセのリードと力強いドラム、夏フェスの高揚感
bgm#music_c(volume: 6dB; fade: 0,40) 疾走感のあるアップテンポの明るい EDM ポップ、シンセのリードと力強いドラム、夏フェスの高揚感
# 字幕: 画面中央に 1 句ずつ、極太の丸ゴシック・紺の太い縁・マゼンタの光・ポンと弾んで出て次の句まで残る
subtitle.hug(bottom: 710px; padding: 0px; font-size: 150px; font-family: d; line-height: 1.12; color: #FFFFFF; stroke: #0B0730,9; text-shadow: 0px 0px 22px #FF28C8E6; background: none; text-align: center; unit: phrase; min_phrase: 0; strip: 、。; lead: 0; tail: 0; hold: next; in: {scale:.62, opacity:0, duration:.16, ease:'back.out(1.7)'}; out: {opacity:0, duration:.05})
# 句の型 (札の頭の [card:型]): 小さい前置き・決め語 (傾いて弾む)・驚き・判子・色ずれの分身・熱・突進・被弾・復活・沈む・勝利の金・冷たい音源・熱いフェス
subtitle.small(font-size: 112px; in: {scale:.7, opacity:0, duration:.16, ease:'back.out(1.7)'})
subtitle.big85(font-size: 128px)
subtitle.hit(font-size: 168px; rotation: -3; in: {scale:.45, rotation:-3, opacity:0, duration:.2, ease:'back.out(1.7)'})
subtitle.hit85(font-size: 128px; rotation: -3; in: {scale:.45, rotation:-3, opacity:0, duration:.2, ease:'back.out(1.7)'})
subtitle.huh(font-size: 225px; in: {scale:.3, opacity:0, duration:.18, ease:'back.out(1.7)'})
subtitle.stamp(font-size: 168px; color: $red; stroke: #FFFFFF,9; text-shadow: 0px 0px 26px #FF2448E6; background: #FFFFFFEB; border: 14px solid $red; border-radius: 26px; padding: 0px 46px; rotation: -10; in: {scale:3.2, rotation:-14, opacity:0, duration:.16, ease:'power4.in'})
subtitle.clone(ghost: #00F0FF,#FF2BD6,17; in: {scale:.6, opacity:0, duration:.18, ease:'back.out(1.7)'})
subtitle.heat(font-size: 160px; in: {scale:.45, rotation:-6, opacity:0, duration:.2, ease:'back.out(1.7)'})
subtitle.dash(in: {scale:1.4, opacity:0, duration:.18, ease:'power4.out'})
subtitle.damage(font-size: 165px; in: {scale:1.5, opacity:0, duration:.12, ease:'power4.out'})
subtitle.revive(font-size: 170px; color: #B6FFE9; text-shadow: 0px 0px 30px #3FFFB0; in: {scale:.45, rotation:-6, opacity:0, duration:.2, ease:'back.out(1.7)'})
subtitle.dim(font-size: 120px; color: #B9B4D8; text-shadow: 0px 0px 0px #00000000; in: {scale:.9, opacity:0, duration:.3, ease:'power2.out'})
subtitle.victory(font-size: 214px; stroke: #2A0B00,10; text-shadow: 0px 0px 40px #FFC83C; in: {scale:.2, opacity:0, duration:.34, ease:'back.out(1.7)'}; main: sine {scale: 0.06, period: 1})
subtitle.cool(font-size: 112px)

# 部品: 写真カード (白の細い縁 + 青緑の光・下を暗く)・情報パネル (濃紺の半透明 + 薄い縁)・閃光の幕・字幕と同じ見た目の design の文字
def card(p) = div(left: 80px; top: 250px; width: 920px; height: 800px; border-radius: 44px; background: #0A0630; border: 4px solid #FFFFFFEB; box-shadow: 0px 0px 46px 10px #00E5FF8C; in: none)
  img#p(inset: 0; content: {p})
  div#shade(inset: 0; background: linear(#08042800@58%,#080428C7,180))
def panel(h) = div(left: 80px; top: 1230px; width: 920px; height: {h}; border-radius: 30px; background: #080526CC; border: 3px solid #FFFFFF47; box-shadow: 0px 0px 36px #00E5FF47; in: {y:80, scale:.92, opacity:0, duration:.28, ease:'power3.out'})
def flash(o) = veil(color: #FFFFFF; opacity: {o}; z-index: curtain; in: none)
def capword(t, s=107) = p(font-size: {s}; font-family: d; line-height: 1.12; stroke: #0B0730,9; text-shadow: 0px 0px 22px #FF28C8E6; content: {t})
# タイムテーブルの枠 (地 + 文字)・地図のピン (色の点 + 名札・輪は ping で広げる)・HP の段 (名 + 枠 + 赤の地 + 緑の残量 + ダメージ数字)
def blk(t, bg, fg=#FFFFFF8C, s=20) = div(width: 380px; border-radius: 14px; background: {bg})
  p#t(left: 16px; cy: 50%; font-size: {s}; color: {fg}; content: {t})
def pin(lab, c, glow) = div(width: 120px; height: 120px; in: {y:-60, scale:.2, opacity:0, duration:.25, ease:'back.out(1.7)'})
  div#dot(cx: 50%; cy: 50%; width: 44px; height: 44px; border-radius: 148px; background: {c}; border: 6px solid #FFFFFF; box-shadow: 0px 0px 26px {glow})
  p#lab(cx: 50%; top: -62px; font-size: 30px; background: {c}; border-radius: 148px; padding: 4px 20px; content: {lab})
def hudrow(n, d) = div(left: 30px; width: 860px; height: 106px; in: none)
  p#nm(left: 0px; top: 44px; font-size: 40px; font-family: dot; content: {n})
  div#tr(left: 210px; top: 46px; width: 560px; height: 48px; background: #FFFFFF14; border: 4px solid #FFFFFF)
  div#red(left: 214px; top: 51px; width: 550px; height: 39px; background: $red)
  div#grn(left: 214px; top: 51px; width: 550px; height: 39px; background: linear(#3FFFB0,#3FF5FF,90))
  p#dmg(left: 640px; top: 0px; font-size: 54px; font-family: dot; color: #FF3B5C; text-shadow: 0px 0px 12px #FFFFFF; in: {y:30, scale:.4, opacity:0, duration:.25, ease:'back.out(1.7)'}; out: {opacity:0, duration:.2}; content: {d})

# 全編の地 (z: back): 斜めのネオングラデ・光の斑 4 つ (screen・36 秒で往復)・光の柱 4 本 (下を軸に揺れる)・透視の格子の床 (横線と縦線の 2 枚を 70° 倒す・hf の格子の流れは省略)・床の上の紫の霞・走査線
div#neon(inset: 0; background: linear(#050A3C,#0B2BE0@26%,#5A1FD8@52%,#D4166A@78%,#FF2E3A,172); z-index: back; in: none)
div#blob1(left: -380px; top: -260px; width: 900px; height: 900px; background: radial(#00D5FF,#00D5FF00@70%); opacity: .7; mix-blend-mode: screen; z-index: back; in: none; main: sine {x: 130, y: 90, period: 36}; bleed)
div#blob2(left: 620px; top: 520px; width: 820px; height: 820px; background: radial(#FF2BD6,#FF2BD600@70%); opacity: .7; mix-blend-mode: screen; z-index: back; in: none; main: sine {x: -120, y: -80, period: 36}; bleed)
div#blob3(left: -300px; top: 1250px; width: 1100px; height: 1100px; background: radial(#FF2A3A,#FF2A3A00@70%); opacity: .7; mix-blend-mode: screen; z-index: back; in: none; main: sine {x: 100, period: 24}; bleed)
div#blob4(left: 640px; top: -200px; width: 760px; height: 760px; background: radial(#2A4BFF,#2A4BFF00@70%); opacity: .7; mix-blend-mode: screen; z-index: back; in: none; main: sine {x: -90, y: 110, period: 36}; bleed)
div#beam(left: "53;220;427;587"; top: -180px; width: 130px; height: 2300px; background: "linear(#FFFFFF00,#78F0FFE6@18%,#78F0FF00,0);linear(#FFFFFF00,#FF50BEE6@18%,#FF50BE00,0);linear(#FFFFFF00,#78F0FFE6@18%,#78F0FF00,0);linear(#FFFFFF00,#FF50BEE6@18%,#FF50BE00,0)"; opacity: .32; mix-blend-mode: screen; transform-origin: 50% 100%; rotation: "-3;3;3;3"; main: sine {rotation: '21;-17;19;-23', period: '4.8;5.8;6.8;7.8', pivot: 'bottom'}; z-index: back; in: none; bleed) ×4
div#floor_h(left: -540px; top: 1380px; width: 2160px; height: 760px; pattern: hatch,0,#00F0FFBF,80,3; main: constant {rotationX: 70, depth: 0.85, pivot: 'top'}; z-index: back; in: none; bleed)
div#floor_v(left: -540px; top: 1380px; width: 2160px; height: 760px; pattern: hatch,90,#FF46D2A6,80,3; main: constant {rotationX: 70, depth: 0.85, pivot: 'top'}; z-index: back; in: none; bleed)
div#floor_fade(left: 0px; top: 1380px; width: 1080px; height: 200px; background: linear(#5A14AAE6,#5A14AA00,180); z-index: back; in: none)
div#scan(inset: 0; pattern: hatch,0,#00000038,4,1.3; opacity: .45; z-index: back; in: none)

# 常設の上端 (z: front): 進行線 (青緑→マゼンタ→赤)・章札 (番号はドット書体・cut の頭で文字を差し替えて弾む)・右上のタグ
div#prog_track(left: 0px; top: 0px; width: 1080px; height: 12px; background: #FFFFFF26; z-index: front; in: none)
progress#prog(left: 0px; top: 0px; width: 1080px; height: 12px; background: linear(#00E5FF,#FF2BD6@50%,#FF3B3B,90); until: end; z-index: front; overlap: prog_track)
p#chap(left: 80px; top: 150px; font-size: 38px; background: #05031EB8; border: 3px solid $c; border-radius: 148px; padding: 8px 22px; box-shadow: 0px 0px 22px #3FF5FF8C; z-index: front; in: {x:-40, scale:.8, opacity:0, duration:.25, ease:'power3.out'}) {no}01{/} 解禁
p#tag(right: 80px; top: 156px; font-size: 32px; opacity: .9; background: linear(#FF2BD6D9,#FF3B3BD9,90); border-radius: 12px; padding: 8px 20px; z-index: front; in: none) ＃夏フェス

# 解禁: 寝室のスマホの写真に通知のバナーが上から落ち、光が 2 回広がり、AM 0:00 のドット時計 (コロンが点滅)・「は？」で全面を灰に・「待て」3 つ
section#hook
card#c1(p: "[photo]真夜中の暗い寝室。ベッドのシーツの上に置かれたスマートフォンが画面を上にして強く発光している（画面は青白く光っているだけで文字やアイコンは無い）。画面の光が周囲をほのかに照らし、窓の外から赤いネオンの光が差し込む。縦構図、シネマティック、浅い被写界深度、青と赤の色調。")
  img#p(main: kb {scale: [1.18, 1], ease:'power1.out'})
  # 画面の光 (静止は 1.6 倍で消えた姿・入場で 0.4 倍の濃い光から広がる)
  div#glow1(left: 141px; top: 150px; width: 640px; height: 640px; border-radius: 148px; background: radial(#8CF0FFF2,#8CF0FF00@70%); mix-blend-mode: screen; opacity: 0; delay: 120; in: {scale:.25, opacity:.95, duration:.9, ease:'power2.out'})
  div#glow2(left: 141px; top: 150px; width: 640px; height: 640px; border-radius: 148px; background: radial(#8CF0FFE6,#8CF0FF00@70%); mix-blend-mode: screen; opacity: 0; in: {scale:.25, opacity:.9, duration:.9, ease:'power2.out'})
# 通知のバナー (アプリの icon + 未読の赤丸 + 3 行)・題に黄の下帯が語で伸びる
div#notif(left: 110px; top: 300px; width: 860px; height: 200px; border-radius: 36px; background: #F8F8FFF0; box-shadow: 0px 0px 40px #00E5FFBF; delay: 100; in: {y:-260, scale:.9, opacity:0, duration:.42, ease:'back.out(1.6)'})
  div#icon(left: 30px; cy: 50%; width: 120px; height: 120px; border-radius: 30px; background: linear(#00E5FF,#6A3BFF@50%,#FF2BD6,135))
    p#t(cx: 50%; cy: 50%; font-size: 38px; font-family: d) FES
  p#badge(left: 117px; top: 22px; font-size: 34px; background: $red; border: 4px solid #FFFFFF; border-radius: 148px; padding: 2px 16px; in: {scale:.2, opacity:0, duration:.22, ease:'back.out(1.7)'}) 1
  p#app(left: 176px; top: 33px; font-size: 27px; color: #666666) NEON SUMMER FES 2026 公式
  p#now(right: 34px; top: 33px; font-size: 27px; color: #666666) 今
  p#title(left: 176px; top: 69px; font-size: 44px; color: #111111) {m}【速報】タイムテーブル解禁!!{/}
  p#text(left: 176px; top: 132px; font-size: 26px; color: #555555) 全ステージの出演時間を公開しました
# AM 0:00 のドット時計 (数字は青白く光り、コロンだけ 0.5 秒ごとに点滅)
p#ampm(cx: 540px; top: 1257px; font-size: 56px; font-family: dot; color: $y; letter-spacing: .2em; text-shadow: 0px 0px 18px #FFE94AE6) AM
group#digits(left: 80px; top: 1332px; width: 920px; height: 230px)
  p#h(left: 214px; top: 0px; font-size: 230px; font-family: dot; line-height: 1; color: #BFF8FF; text-shadow: 0px 0px 30px #3FF5FF) 0
  p#colon(left: 339px; top: 0px; font-size: 230px; font-family: dot; line-height: 1; color: #BFF8FF; text-shadow: 0px 0px 30px #3FF5FF) :
  p#m(left: 464px; top: 0px; font-size: 230px; font-family: dot; line-height: 1; color: #BFF8FF; text-shadow: 0px 0px 30px #3FF5FF) 00
p#hayakuchi(overlap: c1; left: 70px; top: 904px; font-size: 40px; color: $navy; background: $y; border-radius: 148px; padding: 8px 22px; box-shadow: 0px 0px 0px 4px #120A3A; transform: rotate(-8deg); in: {scale:.5, rotation:-12, opacity:0, duration:.2, ease:'back.out(1.7)'}) （早口）
veil#desat1(filter: saturate(0); z-index: front; in: {opacity:0, duration:.05}; out: {opacity:0, duration:.05})
# 「待て」3 つ (字幕と同じ見た目・左上 / 中下 / 右上に傾けて積む)
capword#wait(overlap: hayakuchi,c1,notif,ampm,digits; cx: "167;360;553"; cy: "663;745;683"; s: "93;107;122"; rotation: "-10;6;-6"; t: 待て; in: {scale:2.4, rotation:-15, opacity:0, duration:.16, ease:'power4.out'}) ×3
flash#fl_w(o: .28) ×3

# 絶望: 会場の写真に東西のピンと点線 (徒歩25分)・下のタイムテーブルで推し 2 つが同じ段に光り、黄の枠 SAME TIME → 判子「被り確定」・分身の色ずれのカード
section#clash
img#gl(left: 20px; top: 250px; width: 920px; height: 800px; border-radius: 44px; content: @grounds; look: #000000/#00E5FF; mix-blend-mode: screen; opacity: .55; in: {x:60, opacity:0, duration:.5, ease:'power2.out'})
img#gr(left: 140px; top: 250px; width: 920px; height: 800px; border-radius: 44px; content: @grounds; look: #000000/#FF2BD6; mix-blend-mode: screen; opacity: .55; in: {x:-60, opacity:0, duration:.5, ease:'power2.out'})
card#c2(p: "@grounds")
  img#p(main: kb {scale: [1.12, 1], focus: ['47% 50%', '52% 50%'], ease:'sine.inOut'})
  shape#dash(left: 160px; top: 374px; width: 600px; height: 8px; path: line_h; border: 8px solid #FFFFFF; dash: 17,12; in: {scaleX:0, duration:.45, ease:'power2.inOut', pivot:'left'})
  pin#pinw(left: 100px; top: 320px; lab: WEST; c: #2B7BFF; glow: #3FB5FF)
  pin#pine(left: 700px; top: 320px; lab: EAST; c: $red; glow: #FF4A6A)
  p#dist(cx: 460px; top: 410px; font-size: 34px; background: #05031ED9; border: 3px solid #FFFFFF; border-radius: 148px; padding: 8px 22px; in: {scale:.4, opacity:0, duration:.22, ease:'back.out(1.7)'}) 徒歩25分
panel#tt(h: 372px)
  p#hw(left: 120px; top: 12px; width: 380px; font-size: 27px; font-family: d; letter-spacing: .06em; text-align: center; background: #1D5DFF; border-radius: 12px; padding: 6px 0px) WEST STAGE
  p#he(left: 514px; top: 12px; width: 380px; font-size: 27px; font-family: d; letter-spacing: .06em; text-align: center; background: $red; border-radius: 12px; padding: 6px 0px) EAST STAGE
  div#row(left: 0px; top: "44;94;144;194"; width: 914px; height: 2px; background: #FFFFFF29) ×4
  p#time(left: 18px; top: "48;98;148;198"; font-size: 28px; font-family: dot; color: #C9C4FF) ×4 17:00;18:00;19:00;20:00
  blk#g1(left: 120px; top: 70px; height: 52px; t: DJ NEON; bg: #FFFFFF1F)
  blk#g2(left: 514px; top: 88px; height: 46px; t: SHOUT!; bg: #FFFFFF1F)
  blk#g3(left: 120px; top: 256px; height: 60px; t: BAND Z; bg: #FFFFFF1F)
  blk#g4(left: 514px; top: 268px; height: 70px; t: IDOL Q; bg: #FFFFFF1F)
  blk#ow(left: 120px; top: 144px; height: 84px; t: 推しA ♥; bg: linear(#2B7BFF,#3FD2FF,135); s: 27; box-shadow: 0px 0px 28px #3FB5FFE6; in: {scale:.6, opacity:0, duration:.2, ease:'back.out(1.7)'})
  blk#oe(left: 514px; top: 144px; height: 84px; t: 推しB ♥; bg: linear(#FF2448,#FF6A3D,135); s: 27; box-shadow: 0px 0px 28px #FF4A6AE6; in: {scale:.6, opacity:0, duration:.2, ease:'back.out(1.7)'})
  div#band(left: 112px; top: 136px; width: 794px; height: 100px; border-radius: 18px; border: 6px solid $y; box-shadow: 0px 0px 30px #FFE94AE6; overlap: tt.ow; in: keys(at=0 scale=1.25 opacity=0 | at=0.165 scale=1 opacity=1 ease=power3.out | at=0.188 opacity=1 | at=0.323 opacity=0.45 | at=0.459 opacity=1 | at=0.594 opacity=0.45 | at=0.729 opacity=1 | at=0.865 opacity=0.45 | at=1 ease=none),duration=1330)
  p#same(right: 8px; top: 88px; overlap: tt.g2; font-size: 28px; color: $navy; background: $y; border-radius: 148px; padding: 4px 16px; in: keys(at=0 scale=1.25 opacity=0 | at=0.165 scale=1 opacity=1 ease=power3.out | at=0.188 opacity=1 | at=0.323 opacity=0.45 | at=0.459 opacity=1 | at=0.594 opacity=0.45 | at=0.729 opacity=1 | at=0.865 opacity=0.45 | at=1 ease=none),duration=1330) SAME TIME
  p#stamp(left: 260px; top: 186px; font-size: 70px; font-family: d; color: $red; background: #FFFFFFE0; border: 10px solid $red; border-radius: 16px; padding: 6px 30px; box-shadow: 0px 0px 30px #FF2448CC; transform: rotate(-12deg); overlap: tt.ow; in: {scale:3, rotation:-18, opacity:0, duration:.15, ease:'power4.in'}) 被り確定

# 灼熱: 太陽の写真・温度計のパネル (25.0 → 36.0℃ を数え、帯が伸び、危険が点滅、日陰 0%)・ぬるいスポドリが右から転がり込み陽炎が立つ・「走る」で流線とカードが左へ流れる
section#heat
card#c3(p: "[photo]真夏の野外フェス会場の芝生広場を低いアングルから見上げた縦構図の写真。真上でギラギラと輝く灼熱の太陽、強烈なレンズフレア、陽炎で揺らぐ空気、日陰がまったく無い。遠くにステージの骨組みと旗。彩度が高く暑さが伝わる色調。")
  img#p(main: kb {scale: [1.2, 1.05], focus: ['50% 52%', '50% 50%'], ease:'sine.out'})
panel#thermo(h: 340px; out: {x:-200, opacity:0, duration:.3, ease:'power2.in'})
  p#lab(left: 40px; top: 16px; font-size: 32px; font-family: dot; color: #FFD27A) TEMP
  p#num(left: 34px; top: 62px; font-size: 128px; font-family: d; line-height: 1; color: linear(#FFE08A,#FF7A1C@55%,#FF2448,180); text-shadow: 0px 0px 18px #FF781ECC) [count:36.0 start=25.0 ms=605]
  p#unit(left: .num.right+3; top: 122px; font-size: 60px; font-family: d; line-height: 1; color: #FF4A2A) ℃
  div#track(left: 520px; top: 92px; width: 360px; height: 54px; border-radius: 27px; background: #FFFFFF24; border: 3px solid #FFFFFF80)
    div#fill(left: 0px; top: 0px; width: 224px; height: 48px; border-radius: 24px; background: linear(#FFD23A,#FF7A1C@50%,#FF2448,90))
  p#tick(left: "347;392;445;499;551"; top: 154px; font-size: 27px; font-family: dot; color: #D8D2FF) ×5 0;10;20;30;40℃
  p#danger(left: 700px; top: 26px; font-size: 30px; background: $red; border-radius: 148px; padding: 4px 20px; in: {scale:.3, opacity:0, duration:.2, ease:'back.out(1.7)'}) 危険
  p#shade0(left: 40px; top: 246px; font-size: 40px; color: $navy; background: #FFFFFFF2; border-radius: 148px; padding: 10px 26px; in: {scale:.4, rotation:-10, opacity:0, duration:.22, ease:'back.out(1.7)'}) 日陰 0%
img#bottle(left: 650px; top: 380px; width: 340px; height: 502px; transform-origin: 50% 80%; transform: rotate(-8deg); in: {x:420, scale:.7, rotation:48, opacity:0, duration:.35, ease:'back.out(1.6)'}; out: {x:-200, opacity:0, duration:.3, ease:'power2.in'}) [transparent]飲みかけでぬるくなったスポーツドリンクのペットボトル1本。ラベルは無地の水色で文字・ロゴは一切無し。結露は無く、少しへこんでいる。正面からのプロダクト写真、斜めに少し傾いている。
svg#waves(left: 770px; top: 250px; width: 160px; height: 120px; part: waves; in: {opacity:0, duration:.2}; out: {x:-200, opacity:0, duration:.3, ease:'power2.in'})
p#nurui(left: 560px; top: 330px; font-size: 44px; color: $ink; background: #7FE3FF; border-radius: 148px; padding: 8px 22px; box-shadow: 0px 0px 0px 4px #0B0730; transform: rotate(10deg); in: {scale:.3, rotation:20, opacity:0, duration:.22, ease:'back.out(1.7)'}; out: {x:-200, opacity:0, duration:.3, ease:'power2.in'}) ぬるい…
# 流線 (100° の白い斜線を screen で・左へ流れる)
div#speed(left: 0px; top: 0px; width: 1800px; height: 1920px; pattern: hatch,10,#FFFFFF8C,100,3; mix-blend-mode: screen; in: {opacity:0, duration:.08}; bleed)

# 限界突破: ステージの写真・HP のパネル (曲数・声 / 膝 / HP の残量が語で削れて赤くなり、ダメージ数字・警告の赤枠)・膝のポラロイド・「全部」で全回復と FULL RECOVERY・「限界？」で周辺減光 + 灰に沈む
section#limit
card#c4(p: "@stage")
  img#p(main: kb {scale: [1.25, 1.12], ease:'power1.out'})
panel#hud(h: 352px; border: 3px solid $c)
  p#song(left: 30px; top: 22px; font-size: 38px; font-family: dot; color: $y) SONG
  p#cnt(left: 170px; top: 16px; font-size: 50px; font-family: dot) 03 / 12
  hudrow#r(top: "40;93;147"; n: "声 VOICE;膝 LEGS;HP"; d: "-92;-95;-88") ×3
  div#warn(left: -3px; top: -3px; width: 926px; height: 358px; border-radius: 30px; border: 8px solid $red; box-shadow: 0px 0px 40px #FF2448E6; in: {opacity:0, duration:.05})
# 膝のポラロイド (白い台紙 + 泥のスニーカー + 手書き風の一言・群ごと 8° 傾ける)
group#shoe(left: 560px; top: 330px; width: 400px; height: 470px; rotation: 8; in: {x:200, scale:.4, rotation:22, opacity:0, duration:.28, ease:'back.out(1.7)'}; out: {opacity:0, duration:.15})
  div#paper(left: 0px; top: 0px; width: 400px; height: 470px; background: #FFFFFF; box-shadow: 0px 20px 50px #0000008C)
  img#ph(left: 16px; top: 16px; width: 368px; height: 384px) [photo]泥と草にまみれ、紐がほどけたボロボロのスニーカーが一足、芝生の上に置かれている。夜の野外フェス会場で、背後のステージから青と赤の照明が差す。足も写さない。ローアングルのクローズアップ写真、縦構図。
  p#cap(cx: 200px; top: 412px; font-size: 34px; color: #222222) 膝、ガクガク
p#full(cx: 540px; top: 800px; font-size: 64px; font-family: d; color: #062A2A; background: linear(#3FFFB0,#3FF5FF,90); border-radius: 148px; padding: 10px 36px; box-shadow: 0px 0px 40px #3FFFB0; in: {scale:.3, opacity:0, duration:.25, ease:'back.out(1.7)'}; out: {opacity:0, duration:.15}) FULL RECOVERY!!
veil#vig(background: radial(#00000000@30%,#000000EB@85%,50%,46%); in: {opacity:0, duration:.25})
veil#desat2(filter: saturate(0.1); z-index: front; in: {opacity:0, duration:.25}; out: {opacity:0, duration:.05})
flash#fl_voice(o: .25)
flash#fl_knee(o: .25)
flash#fl_revive(o: .6)

# 完全勝利: 白の閃光で全面のステージ写真へ切り替え、金の放射光が回り、紙吹雪、PERFECT VICTORY
section#victory
img#vimg(inset: 0; content: @stage; main: kb {scale: [1.3, 1.08], ease:'power2.out'})
svg#rays(left: -420px; top: 140px; width: 1920px; height: 1920px; part: rays; mix-blend-mode: screen; in: {opacity:0, duration:1.04, ease:'none'}; bleed)
confetti#cf(n: 70; dot: 10-17; colors: #FFE94A,#3FF5FF,#FF2BD6,#FFFFFF,#FF3B3B,#3FFFB0; drift: down)
p#perfect(cx: 540px; top: 870px; font-size: 58px; font-family: dot; color: #FFF3B0; letter-spacing: .3em; text-shadow: 0px 0px 20px #FFD84A; in: {scale:.5, opacity:0, duration:.25, ease:'back.out(1.7)'}) PERFECT VICTORY
flash#fl_vic(o: 1)

# 持論: 左右 2 枚の縦カード (音源 = 青く沈んだイヤホン / フェス = 赤いスピーカーの壁)・比べる 2 列の板・「別物」で巨大な ≠・「鼓膜」で音源に赤の ×・「細胞」でフェスが中央へ寄り衝撃の輪が 4 重に広がる
section#theory
div#half_l(left: 70px; top: 250px; width: 440px; height: 800px; border-radius: 40px; background: #0A0630; border: 4px solid #BEE6FFE6; box-shadow: 0px 0px 50px 10px #3FB5FF99; in: {x:-300, scale:.9, opacity:0, duration:.3, ease:'power3.out'}; out: {opacity:0, duration:.2})
  img#p(inset: 0; main: kb {scale: [1.1, 1], ease:'none'}) [photo]暗い部屋の机の上に置かれたワイヤレスイヤホンとそのケース、横に画面の消えたスマートフォン。冷たい青い光だけが当たる、静かでミニマルな構図。プロダクト写真、縦構図。
  div#tint(inset: 0; background: #143CA059; mix-blend-mode: multiply)
  p#lbl(cx: 220px; top: 30px; font-size: 40px; background: #1D5DFF; border-radius: 148px; padding: 8px 22px) 音源
div#half_r(left: 570px; top: 250px; width: 440px; height: 800px; border-radius: 40px; background: #0A0630; border: 4px solid #FFDCEBF2; box-shadow: 0px 0px 60px 14px #FF2B78BF; delay: 80; in: {x:300, scale:.9, opacity:0, duration:.3, ease:'power3.out'})
  img#p(inset: 0; main: kb {scale: [1.1, 1], ease:'none'}) [photo]野外フェスのステージ脇にそびえる巨大なスピーカーの壁（ラインアレイ）をローアングルで見上げた縦構図の写真。重低音で空気が震えるような迫力、赤とマゼンタのステージ照明、スモークと光の粒。
  p#lbl(cx: 220px; top: 30px; font-size: 40px; background: $red; border-radius: 148px; padding: 8px 22px) フェス
# 赤の × (白の縁取り・2 本の棒を ±45°)
group#xmark(left: 90px; top: 447px; width: 400px; height: 400px; in: {scale:1.8, opacity:0, duration:.18, ease:'power4.out'}; out: {opacity:0, duration:.2})
  div#a(left: 0px; top: 183px; width: 400px; height: 34px; border-radius: 16px; background: $red; box-shadow: 0px 0px 0px 6px #FFFFFF; rotation: 45)
  div#b(left: 0px; top: 183px; width: 400px; height: 34px; border-radius: 16px; background: $red; box-shadow: 0px 0px 0px 6px #FFFFFF; rotation: -45)
# 衝撃の輪 (同じ枠に 4 つ重ねる = 位置を instance ごとに書く・0.15 倍から入場で 400 px へ・退場で 2.6 倍に広がって消える・0.12 秒おき)
shape#sring(left: "240;240;240;240"; top: 350px; width: 600px; height: 600px; border-radius: 50%; background: none; border: 16px solid #FF6EC8; opacity: .95; in: {scale:.15, duration:.25, ease:'power1.out'}; out: {scale:2.6, opacity:0, duration:.45, ease:'power1.out'}; bleed) ×4
p#neq(cx: 540px; cy: 620px; font-size: 300px; line-height: 1; stroke: #FF2BD6,7; text-shadow: 0px 0px 30px #FF2BD6; in: {scale:3, rotation:-30, opacity:0, duration:.18, ease:'power4.in'}; out: {scale:.6, opacity:0, duration:.2}) ≠
panel#cmp(h: 340px)
  p#lh(left: 30px; top: 24px; font-size: 44px; color: #7FE3FF; letter-spacing: .08em) 音源
  p#li(left: 30px; top: 88px; font-size: 40px; line-height: 1.55; color: #E9E6FF; opacity: .78) 耳で聴く[br]いつでも[br]何度でも
  div#vs(left: 454px; top: 30px; width: 4px; height: 280px; background: linear(#00E5FF,#FF2BD6,180))
  div#cr(left: 470px; top: 24px; width: 420px; height: 300px; in: {x:40, scale:.6, opacity:0, duration:.22, ease:'back.out(1.7)'})
    p#h(left: 0px; top: 0px; font-size: 44px; color: #FF6AB0; letter-spacing: .08em) フェス
    p#i(left: 0px; top: 64px; font-size: 40px; line-height: 1.55; text-shadow: 0px 0px 18px #FF4FA8E6) 全身で浴びる[br]一度きり[br]一生モノ
flash#fl_neq(o: .5)

# 予告: 夜のベランダのタオルの写真 (ゆっくり寄る・星がきらめく)・NEXT 7 DAYS LEFT のカレンダーと第2弾発表の板・斜めの帯を文字が流れる・「震えて待て」は字幕を閉じた design の文字 (色ずれ + 震え + 閃光で上へ跳ねる)
section#next
card#c6(p: "[photo]夜のベランダの物干しに干された、洗いたてで少し濡れたフェス用のマフラータオル（無地で青から赤へのグラデーション）。背景は青と赤のネオンに染まった都会の夜景のボケ。シネマティックな写真、縦構図。")
  img#p(main: kb {scale: [1, 1.18], ease:'none'})
  svg#sp(left: "200;407;280"; top: "173;280;400"; width: 60px; height: 60px; part: spark; in: {scale:.2, rotation:-90, opacity:0, duration:.25, ease:'power2.out'}; out: {scale:.2, rotation:90, opacity:0, duration:.25, ease:'power2.in'}) ×3
panel#next_box(h: 300px)
  div#cal(left: 34px; top: 34px; width: 210px; height: 230px; border-radius: 22px; background: #FFFFFF)
    div#top(left: 0px; top: 0px; width: 210px; height: 64px; border-radius: 22px,22px,0px,0px; background: linear(#FF2BD6,#FF3B3B,90))
    p#nx(cx: 50%; cy: 32px; font-size: 38px; font-family: dot) NEXT
    p#big(cx: 50%; top: 68px; font-size: 96px; font-family: d; line-height: 1.2; color: $navy) 7
    p#sm(cx: 50%; top: 184px; font-size: 27px; color: $navy) DAYS LEFT
  p#l1(left: 290px; top: 52px; font-size: 40px; font-family: dot; color: $c; letter-spacing: .12em) COMING SOON
  p#l2(left: 290px; top: 102px; font-size: 76px; font-family: d; line-height: 1.2; text-shadow: 0px 0px 24px #FF2BD6E6) 第2弾 発表
  p#l3(left: 290px; top: 202px; font-size: 34px; color: $y) 出演アーティスト追加
# 斜めの帯 (-4°・マゼンタ→紫→青のグラデ + 上下の白線)・中の文字が左へ流れ続ける
group#band(left: -200px; top: 1586px; width: 1480px; height: 96px; rotation: -4; clip: true; in: {opacity:0, duration:.12}; bleed)
  div#bg(left: 0px; top: 0px; width: 1480px; height: 96px; background: linear(#FF2BD6,#6A3BFF@50%,#00C8FF,90); border: 4px solid #FFFFFF; box-shadow: 0px 0px 40px #FF2BD6B3)
  p#t(left: 0px; top: 14px; font-size: 54px; font-family: d; letter-spacing: .04em; white-space: nowrap) 第2弾発表まで あと7日 ▶ NEXT ANNOUNCEMENT ▶ 第2弾発表まで あと7日 ▶ NEXT ANNOUNCEMENT ▶ 第2弾発表まで あと7日 ▶
# 締めの文字 (字幕の位置に・青緑とマゼンタの写しを左右にずらして重ねる)
group#shiver(left: 0px; top: 960px; width: 1080px; height: 250px; in: {scale:.4, opacity:0, duration:.2, ease:'back.out(1.7)'})
  p#gc(cx: 528px; cy: 50%; font-size: 160px; font-family: d; line-height: 1.12; color: #00F0FF; opacity: .85; mix-blend-mode: screen; in: {opacity:0, duration:.1}) 震えて待て
  p#gm(cx: 552px; cy: 50%; font-size: 160px; font-family: d; line-height: 1.12; color: #FF2BD6; opacity: .85; mix-blend-mode: screen; overlap: shiver.gc; in: {opacity:0, duration:.1}) 震えて待て
  capword#t(cx: 540px; cy: 50%; t: 震えて待て; text-shadow: 0px 0px 30px #FF2D55; overlap: shiver.gc,shiver.gm)
flash#fl_end(o: .95)
```

```timeline.txt
#v2
# cut = hf の 6 場面 (限界突破は「完全勝利」の閃光で全面の 1 枚へ切るので 2 cut)。境目は斜めの光の帯が左から右へ払う (0.34 秒・境界の前後に半分ずつ)
# 字幕は 1 句 1 札 ([|] で hf の句の割り方どおりに切る)・札の頭の [card:型] で句ごとの見た目と入り方を替える・語の色は台詞の {y} {o} …
cast n = "明るくハキハキした若い男性の声、10代後半から20代前半、元気でエネルギッシュ" manner="早口でまくし立てる熱狂的なオタク。少し大げさでドラマチックに、リズミカルに畳み掛ける"
silence head=0 tail=0
transition = wipe,340,dir=right,overlap=170,angle=14,bars=linear(#00E5FF00,#00E5FF@30%,#FFFFFF,#FF2BD6@70%,#FF2BD600),470

# 解禁: バイブ + 通知音で開け、語ごとに 光 / 時計の拍 / 未読の 1 / バナーの寄り / 題の下帯・「は？」でスクラッチ + 全面を灰に + 籠った曲を止める
*** hook
[>#subtitle]
bgm music_a
# 曲は語の印で開けないので、2 区間目は cut 頭からの ms で「待って」の語に合わせて頭から入れる
bgm music_b +7600
@n: [silence:450][♪vibe -5dB -430][♪notif +3dB -350][!#digits.colon to,{opacity:.15, duration:.5, repeat:9, yoyo:true} -450][card:small]ピロン。[|][>#c1.glow2 -90][!#digits punch,1.14,duration=280][>#hayakuchi +100]午前{y}0時{/}、[|][>#notif.badge +150]通知が{y}一件{/}。[|][card:big85][♪sweep -4dB -50][!#notif to,{scale:1.07, duration:.18, ease:'power2.out'}]タイムテーブル[|][card:hit][!#notif.title{m} marker -50]{y}解禁{/}。[|][card:huh][♪scratch -100][<#music_a][>#desat1][!#c1 to,{scale:1.18, duration:.12, ease:'power4.out'}][!#notif shake,9,duration=300 +50]……{r}は？{/}
# 「待って」×3: 字幕を閉じ、語ごとに 待て が傾いて叩きつけられ、カードが揺れ、白が瞬く
@| [<#subtitle][<#desat1 -20][!#c1 to,{scale:1, duration:.2, ease:'power2.out'}][>#wait[1]][♪cymbal][♪swish -2dB][!#c1 shake,12,duration=220][>#fl_w[1]][!#fl_w[1] to,{opacity:0, duration:.2}]待って[>#wait[2]][♪swish -2dB][!#c1 shake,12,duration=220][>#fl_w[2]][!#fl_w[2] to,{opacity:0, duration:.2}]待って[>#wait[3]][♪swish -2dB][!#c1 shake,12,duration=220][>#fl_w[3]][!#fl_w[3] to,{opacity:0, duration:.2}]待って。

# 絶望: 推し 2 つが段に光る → SAME TIME の黄枠が点滅 → 東西のピン (輪が広がる) と点線 → 判子「被り確定」で全体が揺れる → 分身の色ずれ
*** clash
[>#subtitle]
@n: [!#chap text,"{no}02{/} 絶望"][!#chap pop][♪sweep -3dB -30][>#tt.ow +20][>#tt.oe +220]{y}推し{/}と推しが、[|][card:hit][♪sweep -3dB -30][>#tt.band][>#tt.same]{y}同じ時間{/}。[|][card:small]しかも[|][♪dash -2dB -100 to=1s][>#c2.pinw][!#c2.pinw.dot ping,#3FB5FF,5,interval=800,duration=800,scale=1.65>4.4][>#c2.pine +350][!#c2.pine.dot ping,#FF4A6A,5,interval=800,duration=800,scale=1.65>4.4 +350]東と西の[|][card:hit][>#c2.dash -100][>#c2.dist +200]{y}端と端{/}。[|][!#tt shake,7,duration=250 +100]タイテ{y}被り{/}、[|][card:stamp][♪stamp +3dB][♪shock +1dB to=2.8s][>#tt.stamp][!#tt.ow to,{opacity:.6, duration:.2} +100][!#tt.oe to,{opacity:.6, duration:.2} +100][!#tt shake,12,duration=300 +160][!#c2 shake,12,duration=300 +160]{red}確定{/}。[|][!#tt to,{opacity:.35, duration:.3}]人類は[|][card:clone][♪glitch -2dB][>#gl][>#gr][!#c2 to,{scale:.94, duration:.6, ease:'power2.out'}]なぜ{y}分身{/}[|][card:clone][♪glitch -5dB]できないのか。

# 灼熱: セミの場の音・温度が 25.0 → 36.0℃ と数えて帯が伸び、危険が点滅 → 日陰 0% → スポドリが転がり込み、陽炎とぬるい札 → 「走る」で流線とカードが左へ流れ、札と板が抜ける
*** heat
@n: [!#chap text,"{no}03{/} 灼熱"][!#chap pop][♪sweep -3dB -50][♪cicada -5dB -150 to=3.6s fade=200,1600][!#thermo.track.fill to,{w:324, duration:.7, ease:'power2.out'}][!#thermo.num punch,1.1,duration=240 +605][>#thermo.danger +650][!#thermo.danger to,{opacity:.35, duration:.2, repeat:7, yoyo:true} +900][card:heat]気温{o}36度{/}、[|][card:heat][>#thermo.shade0]日陰{o}ゼロ{/}、[|][♪swish -3dB][>#bottle]スポドリは[|][>#nurui][>#waves][!#waves to,{y:-30, duration:.5, yoyo:true, repeat:1}][!#bottle to,{rotation:-14, duration:.25, yoyo:true, repeat:1} +200]もう{y}ぬるい{/}。[|][card:dash][♪run -2dB][♪dash -2dB to=1s][>#speed][!#speed to,{x:-600, duration:.9, ease:'none'}][!#c3 to,{x:-140, duration:.88, ease:'power2.in'}][<#bottle +150][<#nurui +150][<#waves +150][<#thermo +150]それでも{cy}走る{/}。

# 限界突破: 曲数が 03 → 05 → LAST SONG と替わり、被弾の語で残量が削れ (ダメージ数字・揺れ・閃光・赤枠の点滅・膝のポラロイド)、「全部」で全回復 + 歓声、「限界？」で曲を止めて周辺減光と灰・鼓動
*** limit
@n: [!#chap text,"{no}04{/} 限界突破"][!#chap pop]{y}3曲目{/}で[|][card:damage][♪dmg1 +2dB][!#hud.r[1].grn to,{w:44, duration:.3, ease:'power3.out'}][>#hud.r[1].dmg][<#hud.r[1].dmg +700][!#c4 shake,13,duration=300][>#fl_voice][!#fl_voice to,{opacity:0, duration:.15}]声が{dmg}枯れ{/}、[|][!#hud.cnt text,"05 / 12"][!#hud.cnt pop]{y}5曲目{/}で[|][card:damage][>#shoe -50][♪dmg2 +2dB][!#hud.r[2].grn to,{w:27, duration:.3, ease:'power3.out'}][!#hud.r[3].grn to,{w:82, duration:.4, ease:'power3.out'} +50][>#hud.r[2].dmg][>#hud.r[3].dmg +120][<#hud.r[2].dmg +750][<#hud.r[3].dmg +750][!#c4 shake,15,duration=320][>#fl_knee][!#fl_knee to,{opacity:0, duration:.15}][>#hud.warn +50][!#hud.warn to,{opacity:.1, duration:.14, repeat:5, yoyo:true} +100]膝が{dmg}笑い{/}、[|][<#shoe +100][♪riser -2dB -150][!#hud.cnt text,"LAST SONG"][!#hud.cnt recolor,#FFD84A][!#c4.p zoom_media,1.16,duration=880]{y}ラスト{/}の[|]{y}イントロ{/}で[|][card:revive][♪revive +2dB][♪cheer -3dB to=1.4s][<#hud.warn][!#c4.p zoom_media,1.07,duration=1300][!#hud.r[*].grn to,{w:550, duration:.3, ease:'power3.out', stagger:.07}][>#fl_revive][!#fl_revive to,{opacity:0, duration:.4}][!#hud glow,#3FFFB0,blur=53]全部[|][card:revive][>#full]生き返る。[|][card:dim][<#full][<#music_b][♪heart +3dB][>#vig][>#desat2][!#hud to,{opacity:.25, duration:.25}][!#c4 punch,1.04,duration=240]限界？[|][♪heart +3dB][!#c4 punch,1.05,duration=240][<#desat2 +350]知らん。
[<#vig cut-0]

transition cut

# 完全勝利: 白の閃光で全面のステージへ・爆発 + シンバル + 歓声・曲を山から・放射光が回り、紙吹雪、PERFECT VICTORY
*** victory
bgm music_c start=56.6s
@n: [♪boom +6dB -50][♪cymbal +2dB][♪cheer +2dB -50 to=3.2s fade=200,1400][>#fl_vic][!#fl_vic to,{opacity:0, duration:.5, ease:'power2.out'}][!#vimg shake,17,duration=400 +50][!#rays to,{rotation:40, duration:1.04, ease:'none'}][>#perfect +180][card:victory]{gold}完全勝利{/}。[silence:0.4s]

# 持論: 2 枚のカードが左右から → 「音源」で左が寄る → 「フェス」で右が弾み左が沈む → 「別物」で ≠ + 閃光 + 重低音 → 「鼓膜」で左に × → 「細胞」で右が中央へ寄り輪が 4 重に広がる
*** theory
@n: [!#chap text,"{no}05{/} 持論"][!#chap pop][card:small][♪pikiin -3dB]いいか。[|][card:cool][>#cmp][!#half_l to,{scale:1.04, duration:.25, ease:'power2.out'}]{cl}音源{/}を聴くことと、[|][♪dash -2dB -50 to=1s][!#half_l to,{scale:.96, opacity:.75, duration:.25}][!#half_r to,{scale:1.07, duration:.2, ease:'back.out'}]{y}フェス{/}で[|][>#cmp.cr][!#half_r shake,9,duration=300]{hot}浴びる{/}ことは、[|]全くの[|][card:hit][♪bass +2dB][>#neq][>#fl_neq +150][!#fl_neq to,{opacity:0, duration:.3} +150][!#half_l shake,9,duration=300 +160][!#half_r shake,9,duration=300 +160][!#cmp shake,9,duration=300 +160]{y}別物{/}である。[|][>#xmark +250][!#half_l to,{opacity:.4, duration:.2} +300]{y}鼓膜{/}じゃない、[|][card:hit85][♪bass -2dB][<#neq -50][!#half_r to,{x:-250, scale:1.12, duration:.35, ease:'power3.inOut'}][<#half_l][<#xmark][>#sring[1] -150][>#sring[2] -30][>#sring[3] +90][>#sring[4] +210][<#sring[1] +100][<#sring[2] +220][<#sring[3] +340][<#sring[4] +460]{y}細胞{/}で聴くんだ。

# 予告: 風の上昇音 → 「第2弾」でジャーン + 斜めの帯が流れ出す → タオルに星 3 つ → 字幕を閉じて「震えて待て」(震え → 写しの色ずれ → 爆発 + 閃光で上へ跳ね、曲を止める)
*** next
@n: [!#chap text,"{no}06{/} 予告"][!#chap pop][♪riser -3dB -600]{y}来週{/}、[|][card:hit][♪jaan +1dB][>#band -50][!#band.t to,{x:-1600, duration:4.4, ease:'none'} -50][!#next_box.l2 punch,1.12,duration=300]{y}第2弾{/}発表。[|][♪sweep -4dB -30][>#c6.sp[1]][<#c6.sp[1] +250][>#c6.sp[2] +150][<#c6.sp[2] +400][>#c6.sp[3] +300][<#c6.sp[3] +550]{y}タオル{/}洗って、
@| [<#subtitle][♪tremble -3dB to=2s][>#shiver][!#shiver shake,6,duration=2000 +200][!#c6 shake,5,duration=2000 +200][!#next_box shake,5,duration=2000 +200][>#shiver.gc +480][>#shiver.gm +480][♪boom +6dB +480][♪cymbal +2dB +480][<#music_c +480][>#fl_end +480][!#fl_end to,{opacity:0, duration:.6, ease:'power2.out'} +480][!#shiver to,{y:-390, scale:1.12, duration:.32, ease:'back.out'} +520][!#c6 to,{opacity:.4, duration:.3} +550]震えて待て。[silence:1.6s]
```

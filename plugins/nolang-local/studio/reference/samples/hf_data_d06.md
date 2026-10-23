# data · onsen-inbound (hf 全力版の全量の写し — 温泉町の外国人観光客、5年でどう変わった・和の調査報告を紙の頁をめくる 6 章の図解で) — canvas 1920x1080

見せる作り: 夕暮れの温泉町の写真に左の暗幕と明朝の 2 行の題・朱の判子・語で 4 枚の札 (湯気が漂う)・紙の頁が右から滑り込む頁替え (めくる音)・頁の頭の 3 点 (上端の帯と章の目次・朱の章番号と明朝の題・下の注記) と右下の薄い大きな一字・板の design system (縦棒の数え上げ・100 マス・積み上げの帯 2 本と間の帯・横棒の対・月別の縦棒と写真の小窓と括弧・税の帯と 2 枚の札・困りごとの横棒と 34 マス)・語ごとの色替えと手書きの丸と下線のマーカー・夜の写真の上のまとめの板と出典・生成りの札の字幕・音の層 (和の BGM + 鳴子・紙・電子音の効果音)

```design.txt
#v2
# 学ぶ作り: 和の調査報告の design system を根に 1 回 (生成りの紙の地・明朝の見出しと数字・角ゴシックの本文・朱と藍の 2 色・板 board と札 card の class・頁の頭の 3 点 (上端の帯 hdr・章番号と題 chap・下の注記 note) の def) → 頁は図の中身だけ
# 頁替えは紙をめくる: 新しい頁が右から滑り込み (切替 slide・境界の後ろに窓)、頁の頭の章番号 → 小見出し → 題 → 板 → 注記が窓の中で delay で順に組み上がる・境目に紙をめくる音
# 図は台詞の数字の語で動く: 縦棒が下から伸びて数え上げ (cue で棒と値を 1 語に)・100 マスの格子が語でマスを埋める・積み上げの帯 2 本と間の帯・横棒の対・月別の縦棒の色替えと括弧・語ごとの丸と下線のマーカー
# hf d06 onsen-inbound (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1920x1080 bg=#100D0A
theme light
palette paper=#F1EBDF paper2=#E8DFCE paper3=#D9CCB5 card=#FAF6EE ink=#26211C ink2=#574D44 ink3=#8A7F72 rule=#C9BCA6 shu=#B23C27 ai=#2B4A6F tw=#2B4A6F hk=#6B87A5 kr=#73855A cn=#B49C6E sea=#CF8549 wa=#B23C27 sea_t=#9C561F mute=#9A8F82 cream=#FBF7F0 lt1=#E9E0D0 lt2=#D8CCB8 lt3=#F8F3EA lt4=#FBF3E8 lt5=#E6DCCB lt6=#F7F1E6 lt7=#FDFAF4 lt8=#F1E9DC lt9=#DDD3C3 lt10=#F3C9A8 lt11=#FBF4EA f18=#CF7A68 a=#B23C27 b=#2B4A6F
font "軽く均一な線とくっきりした幾何学的な形、均整のとれた比率を持つクリーンでモダンな日本語の角ゴシック体、中立的な印象の Medium"
fonts b="軽く均一な線とくっきりした幾何学的な形、均整のとれた比率を持つクリーンでモダンな日本語の角ゴシック体、中立的な印象、太い"
fonts r="軽く均一な線とくっきりした幾何学的な形、均整のとれた比率を持つクリーンでモダンな日本語の角ゴシック体、中立的な印象の Medium"
fonts m="繊細な明朝体、優美なひらがな・カタカナ・漢字と古典的な欧文、しなやかな線の強弱と伝統的な書に由来する曲線、極太"
sfx off
# 頁替え: 旧頁が 240 px (hf の 360 px) 左へずれながら暗く沈む (slide の drift= / dim=)
# engine: hf の新頁の左縁に落ちる影 (box-shadow) は切替に無い
# engine: 明朝の記述は catalog の別の上品な明朝の Bold に解ける (hf の ExtraBold より細い)・本文の角ゴシックは Medium が無く Regular
# hf の作り: 板の題・軸・凡例・注記・上端の帯は 1080 で 17〜23 px の小さな字 (small_text)・頁の頭の章の題は台詞より先に出る (spoiler)・結論の札は台詞と同文 (duplicate_text)
lint off=small_text,spoiler,duplicate_text
# hf の作り: 推移・滞在と消費・宿泊税の頁は紙の地に図だけ (text_only_cut)・章の題は頁の頭に全文 (all_at_once)・最後の語の棒と数字は頁替えの 1 秒前 (entrance_in_fadeout)
# hf の作り: 頁の右下の大きな薄い一字は板と札の後ろに沈む (covered_text の warn は残す)
# hf の作り: まとめは夜の写真 1 枚で 20 秒 (same_picture)・要点の 2 と 3 の間は 6 秒動かない (still_stretch の warn は残す)・出典の札は声の後の 3.4 秒だけ (flash_text)
lint off=text_only_cut,all_at_once,entrance_in_fadeout,same_picture,flash_text
prompt_tail "Photorealistic, natural cinematic color grading, high detail. Absolutely no text, no letters, no signs with writing, no logos, no watermark."
run nv { font-family: m }
run em { color: $lt10 }
run fg { font-family: m; font-size: 26px; color: $shu }
run tt { font-family: b; color: $ink }
run n { font-family: m; font-size: 38px; color: $ink }
run n27 { font-family: m; font-size: 40px; color: $ink }
run n27s { font-family: m; font-size: 40px; color: $shu }
run n20 { font-family: m; font-size: 30px; color: $ink }
run s40 { font-size: 60px }
run s51 { font-size: 76px }
run s29 { font-size: 44px }
run s35 { font-size: 52px }
run s20 { font-size: 30px }
run yk { font-family: b; font-size: 30px; color: $ink2 }
run yu { font-size: 50px }
run k { font-family: b; color: $ink }
run bk { font-family: b; color: $ink }
run ar { font-family: b; font-size: 30px; color: $shu }
run sm { font-family: b; font-size: 20px; color: $ink2 }
run qn { font-family: m; color: $shu }
run mk { marker: #B23C273D,45% }
p { color: $ink; out: none }
div { out: none }
img { out: none }
shape { out: none }
svg { out: none }
sound naruko = "和の木の鳴子が柔らかくカラカラと鳴る乾いた音"
sound page = "紙のページを1枚めくる乾いた短い音"
sound paper = "紙を手で扱う乾いたカサッという短い音"
sound whoosh = "短く乾いたノイズのスイープ、シュッと流れる音"
sound chime = "中低音の電子のベルが2回軽く鳴る控えめなチャイム"
sound pop = "柔らかく膨らむ短いサイン波の電子音、控えめなビジネスの合図"
sound circle = "シャープペンで紙に丸をくるりと描く音"
sound marker = "蛍光ペンで紙にまっすぐ線を引く音"
cue vbar(b, v) = [>#b][>#v +150]
# 字幕: 下端中央の生成りの札 (角 3・柔らかい影)・句末の読点と句点は外す・声の 0.08 秒前に下から出る
subtitle.hug(bottom: 38px; font-size: 38px; letter-spacing: .03em; color: $ink; background: #F8F4ECF2; border-radius: 4px; padding: 9px 30px 10px 30px; box-shadow: 0px 6px 15px #00000033; unit: sentence; strip: 、。; lead: 80; tail: 350; hold: next,800; in: {y:8, opacity:0, duration:.18, ease:'power2.out'}; out: {opacity:0, duration:.12})
bgm#music(fade: 350,1700) 温かく穏やかで懐かしい和風の曲、高い弦と低い弦、木管の旋律、柔らかいシンセパッドと和の民族楽器、四拍子の普通の速さ、落ち着いた調査報告や地域の解説向け
svg waf = """<svg viewBox="0 0 157 157"><defs><pattern id="c" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="13" height="13" rx="2" fill="#D9CCB5"/></pattern></defs><rect width="157" height="157" fill="url(#c)"/></svg>"""
svg rib_near = """<svg viewBox="0 0 870 110"><polygon points="0,0 330.6,0 234.9,110 0,110" fill="#2b4a6f" fill-opacity="0.22"/><polygon points="330.6,0 522,0 330.6,110 234.9,110" fill="#6b87a5" fill-opacity="0.24"/><polygon points="522,0 678.6,0 513.3,110 330.6,110" fill="#73855a" fill-opacity="0.24"/><polygon points="678.6,0 756.9,0 582.9,110 513.3,110" fill="#b49c6e" fill-opacity="0.28"/></svg>"""
svg rib_far = """<svg viewBox="0 0 870 110"><polygon points="756.9,0 817.8,0 713.4,110 582.9,110" fill="#cf8549" fill-opacity="0.32"/><polygon points="817.8,0 870,0 870,110 713.4,110" fill="#b23c27" fill-opacity="0.3"/></svg>"""

# 紙の頁の地 (生成り + 紙の目 + 左上の明かりと右下の陰) と右下の大きな薄い明朝の一字 (16 秒で 54 px 上へ漂う)
def paper(g, o) = div(inset: 0; background: $paper; pattern: paper; z-index: back; in: none)
  div#hi(inset: 0; background: radial(#FFFDF8A6,#FFFDF800@70%,28%,18%))
  div#lo(inset: 0; background: radial(#9673461A,#96734600@70%,85%,95%))
  p#ghost.bleed(right: 40px; top: 420px; font-size: 700px; line-height: 1; font-family: m; color: #26211C06; main: keys(at=0 y=27 | at=1 y=-27),window=0,16000,forwards; overlap: {o}; content: {g})
# 上端の帯: 朱の角札「湯」+ 報告名 + 右寄せの章の目次 6 つ (今の章は朱の太字) + 下の細い罫
def hdr(c, f) = div(left: 96px; top: 38px; width: 1728px; height: 54px; in: none)
  p#mark(left: 0px; cy: 50%; width: 34px; font-size: 22px; line-height: 1.5; font-family: m; text-align: center; color: $lt11; background: $shu; border-radius: 3px) 湯
  p#lab(left: 51px; cy: 50%; font-size: 20px; letter-spacing: .08em; color: $ink2) 湯ノ瀬町 観光課｜外国人観光客の5年 調査報告
  p#nav(left: "741;803;865;969;1031;1107"; cy: 50%; font-size: 20px; letter-spacing: .06em; color: {c}; font-family: {f}) ×6 {nv}一{/} 推移;{nv}二{/} 構成;{nv}三{/} 滞在と消費;{nv}四{/} 季節;{nv}五{/} 宿泊税;{nv}六{/} 課題
  div#rule(left: 0px; top: 52px; width: 1728px; height: 2px; background: $rule)
# 章の頭: 朱の明朝の章番号 + 細い縦の罫 → 小見出し (字間広め) → 明朝の題 (頁の窓の中で 0.5 / 0.62 / 0.7 秒に順に)
def chap(n, k, t) = div(left: 96px; top: 118px; width: 1200px; height: 104px; in: none)
  p#n(left: 0px; cy: 50%; font-size: 86px; line-height: 1.16; font-family: m; color: $shu; delay: 500; in: {y:26, opacity:0, duration:.6, ease:'power3.out'}; content: {n})
  div#bar(left: 110px; top: 0px; width: 2px; height: 104px; background: $rule; delay: 500; in: {y:26, opacity:0, duration:.6, ease:'power3.out'})
  p#k(left: 141px; top: 2px; font-size: 21px; letter-spacing: .18em; color: $ink2; delay: 620; in: {x:-18, opacity:0, duration:.5, ease:'power2.out'}; content: {k})
  p#t(left: 141px; top: 39px; font-size: 54px; line-height: 1.15; letter-spacing: .01em; font-family: m; delay: 700; in: {x:-26, opacity:0, duration:.7, ease:'expo.out'}; content: {t})
# 頁の下の注記 (1.6 秒に溶けて出る)
def note(t) = p(left: 96px; top: 904px; font-size: 20px; letter-spacing: .02em; color: $ink2; delay: 1600; in: {opacity:0, duration:.6, ease:'power1.out'}; content: {t})
# 板 (半透明の白 + 細い罫 + 下に沈む影)・板の題の行 (図番号 + 太字の題 + 注) と下の罫・札 (生成りの地)
def board = div(top: 252px; height: 636px; background: #FCF9F3C7; border: 2px solid $rule; border-radius: 6px; box-shadow: 0px 14px 24px #462D141C; delay: 800; in: {y:30, opacity:0, duration:.7, ease:'power3.out'})
def btitle = p(left: 32px; top: 22px; font-size: 22px; color: $ink2)
def brule = div(left: 32px; top: 62px; height: 2px; background: $paper3)
def card = div(background: $card; border: 2px solid $rule; border-radius: 6px; box-shadow: 0px 14px 24px #462D1420)
def ctitle = p(left: 32px; top: 24px; font-size: 22px; letter-spacing: .04em; font-family: b; color: $ink2)
# 題の頁の札 (朱の小見出し + 明朝の値 + 注)
def chip(k, v, s) = div(top: 732px; width: 392px; height: 132px; background: #F8F4ECF2; border-radius: 6px; box-shadow: 0px 9px 21px #00000059; in: {y:30, opacity:0, duration:.6, ease:'back.out(1.5)'})
  p#k(left: 24px; top: 18px; font-size: 20px; letter-spacing: .1em; font-family: b; color: $shu; content: {k})
  p#v(left: 24px; top: 51px; font-size: 38px; line-height: 1.1; font-family: m; content: {v})
  p#s(left: 24px; top: 99px; font-size: 20px; color: $ink2; content: {s})
# 写真の小窓 (生成りの太い縁 + 影)
def thumb = img(width: 140px; height: 94px; border: 6px solid $lt7; box-shadow: 0px 4px 12px #00000059; main: none; in: {scale:.85, opacity:0, rotation:-3, duration:.55, ease:'back.out(1.6)'})

# title — 題の頁: 夕暮れの温泉町の写真が 1.0 → 1.085 に寄り、左の暗幕の上に小札 → 2 行の明朝の題 → 朱の判子 → 朱の線 → 副題、湯気が漂い、語で 4 枚の札
section#title(stagger: {each: 0})
img#t_photo(inset: 0; subject: "60%,10%,40%,55%"; room: left 45%; main: kb {scale: [1, 1.085], focus: ['62% 55%', '62% 55%']}) [photo]A quiet hot-spring town in a mountain valley in Japan at dusk. A narrow river with stone embankments runs through the right half of the frame; traditional two-story wooden ryokan inns with dark tiled roofs line both banks on the right; soft white steam rises from the river and from small vents between the buildings; warm paper lanterns glow along the riverside path; cedar-covered mountains fade into blue mist behind. Only a few tiny figures far away, seen from behind. The left 45% of the frame is calm, darker and uncluttered (misty mountain slope and dusky sky) to leave room for a title; the bottom quarter is the dark river and embankment, quiet enough for cards.
div#t_shade(inset: 0; background: linear(#100C09D6,#100C09A8@34%,#100C092E@62%,#100C0900@78%,90); in: {opacity:0, duration:1, ease:'power1.out'})
div#t_shade_b(left: 0px; top: 660px; width: 1920px; height: 420px; background: linear(#100C09B8,#100C0900,0); in: none)
# 湯気 8 つ (右端の 2 つは hf より 13 px 内へ寄せた・放射の白い斑が 5.6 秒の周期で上下しながら濃くなり薄れる・位相は粒ごと)
shape#t_steam(left: "787;947;867;1027;720;973;827;1080"; top: "347;400;280;313;407;253;427;373"; width: "280;240;200;253;227;187;267;200"; height: "280;240;200;253;227;187;267;200"; border-radius: 50%; background: radial(#FFFAF28C,#FFFAF22E@40%,#FFFAF200@70%,50%,50%); opacity: .45; in: none; main: sine {y: -75, opacity: .45, period: 5.6, phase_offset: '0;.245;.489;.734;.979;.241;.486;.73'}) ×8
div#t_grain(inset: 0; grain: 0.06; in: none)
div#t_kick(left: 120px; top: 200px; height: 38px; display: flex; gap: 18px; align-items: center; delay: 250; in: {y:16, opacity:0, duration:.7, ease:'power2.out'})
  p#a(font-size: 26px; letter-spacing: .22em; color: $lt1) 湯ノ瀬町 観光課
  div#ln(width: 56px; height: 2px; background: $lt2)
  p#b(font-size: 26px; letter-spacing: .22em; color: $lt1) 調査報告 2021–2025
p#t_l1(left: 120px; top: 262px; font-size: 94px; line-height: 1.2; letter-spacing: .01em; font-family: m; color: $lt3; text-shadow: 0px 2px 24px #00000059; delay: 400; in: {y:46, opacity:0, duration:1, ease:'expo.out'}) 温泉町の外国人観光客、
p#t_l2(left: 120px; top: 376px; font-size: 94px; line-height: 1.2; letter-spacing: .01em; font-family: m; color: $lt3; text-shadow: 0px 2px 24px #00000059; delay: 620; in: {y:46, opacity:0, duration:1, ease:'expo.out'}) {em}5年{/}でどう変わった
# 朱の判子 (内側に生成りの細い縁・2×2 の明朝の字・-4° に傾く)
div#t_seal(left: 1010px; top: 384px; width: 118px; height: 118px; background: $shu; border: 3px solid #F8F3EAE6; border-radius: 6px; box-shadow: 0px 6px 15px #00000066; transform: rotate(-4deg); delay: 900; in: {scale:1.7, rotation:-18, opacity:0, duration:.45, ease:'back.out(2.2)'})
  p#c(cx: "24;55;24;55"; cy: "24;24;55;55"; font-size: 36px; line-height: 1; font-family: m; color: $lt4) ×4 調;査;報;告
div#t_rule(left: 120px; top: 520px; width: 120px; height: 4px; background: $shu; delay: 1200; in: {scaleX:0, duration:.7, ease:'power3.inOut', pivot:'left'})
p#t_sub(left: 120px; top: 549px; font-size: 28px; letter-spacing: .06em; color: $lt1; delay: 1400; in: {y:14, opacity:0, duration:.7, ease:'power2.out'}) 宿泊統計と旅行者アンケートで読む、この5年の変化
chip#t_chips(left: "80;356;632;908"; k: "宿泊統計;アンケート;町の宿泊者;町議会の議題"; v: "町内34軒の宿;外国人旅行者612人;18万2,000人;宿泊税の導入"; s: "2021〜2025年;2025年に実施・回答者数;2025年;試算は「五」で") ×4
p#t_fic(right: 96px; top: 900px; font-size: 20px; letter-spacing: .06em; color: $lt5; delay: 1800; in: {opacity:0, duration:.8, ease:'power1.out'}) ※湯ノ瀬町は架空の町です

# trend — 一 推移: 縦棒 5 本が語で下から伸びて数え上げ (2025 年は朱)・「約5倍」で右上の札・「割合」で 100 マスの札、「2.2%」「9.0%」でマスを埋める
section#trend(stagger: {each: 0})
paper#tr_pg(g: 増; o: "tr_bd,tr_x5,tr_sh,subtitle")
hdr#tr_hd(c: "$shu;$ink2;$ink2;$ink2;$ink2;$ink2"; f: "b;r;r;r;r;r")
chap#tr_ch(n: 一; k: "推移｜2021〜2025年"; t: "外国人宿泊者は、5年で約5倍に")
board#tr_bd(left: 96px; width: 1000px)
  btitle#t {fg}図1{/}  {tt}外国人宿泊者数の推移{/}  （実人数・人）
  brule#r(width: 938px)
  # 目盛りの線 3 本 (左に値の札)・底の線
  div#g(left: 102px; top: "121.5;203;284.5"; width: 850px; height: 2px; background: $paper3; delay: 1100; in: {opacity:0, duration:.5, stagger:{each:.08}}) ×3
  p#gl(right: 910px; cy: "121.5;203;284.5"; font-size: 18px; color: $ink2; white-space: nowrap; delay: 1100; in: {opacity:0, duration:.5, stagger:{each:.08}}) ×3 1万5,000;1万;5,000
  div#base(left: 102px; top: 548px; width: 850px; height: 3px; background: $ink2)
  div#bar(left: "96;208;320;432"; top: "313.9;269.9;206.3;144.4"; width: 104px; height: "52.1;96.1;159.7;221.6"; background: $ai; border-radius: 2px; in: {scaleY:0, duration:.65, ease:'power3.out', pivot:'bottom'}) ×4
  div#hot(left: 816px; top: 148px; width: 104px; height: 401px; background: $shu; border-radius: 2px; in: {scaleY:0, duration:.9, ease:'expo.out', pivot:'bottom'})
  p#val(left: "74.5;186.5;298.5;410.5;522.5"; top: "280.5;235.5;172.5;111.5;65.5"; width: 168px; font-size: 32px; line-height: 1.2; font-family: m; text-align: center; color: "$ink;$ink;$ink;$ink;$shu"; in: {y:12, opacity:0, duration:.4, ease:'power2.out'}) ×5 [count:3,200 start=0 ms=600];[count:5,900 start=0 ms=600];[count:9,800 start=0 ms=600];[count:13,600 start=0 ms=600];[count:16,400 start=0 ms=900]
  p#yr(left: "74.5;186.5;298.5;410.5;522.5"; top: 564px; width: 168px; font-size: 22px; text-align: center; color: "$ink2;$ink2;$ink2;$ink2;$shu"; font-family: "r;r;r;r;b") ×5 2021年;2022年;2023年;2024年;2025年
card#tr_x5(left: 1136px; top: 252px; width: 688px; height: 268px; in: {y:34, opacity:0, duration:.6, ease:'power3.out'})
  ctitle#t 5年間の伸び
  p#big(left: 36px; top: 93px; font-size: 144px; line-height: 1; font-family: m; color: $shu; in: {scale:.6, opacity:0, duration:.7, ease:'back.out(1.8)', pivot:'20%,70%'}) {s40}約{/}5{s51}倍{/}
  p#sub(left: 320px; top: 112px; font-size: 26px; line-height: 1.5; color: $ink2; in: {x:20, opacity:0, duration:.6, ease:'power2.out'}) {n27}3,200{/}人（2021年）[br]→ {n27s}16,400{/}人（2025年）
card#tr_sh(left: 1136px; top: 540px; width: 688px; height: 348px; in: {y:34, opacity:0, duration:.6, ease:'power3.out'})
  ctitle#t 町の宿泊者全体に占める割合
  svg#w0(left: 32px; top: 74px; width: 158px; height: 158px; part: waf)
  svg#w1(left: 362px; top: 74px; width: 158px; height: 158px; part: waf)
  # 埋まるマス (2021 年は 2 マス + 2 割のマス・2025 年は 9 マス)・最下段の左から 1 マスずつ
  div#f0(left: "21;31.7"; top: 218px; width: 14px; height: 14px; border-radius: 2px; background: $ai; in: {opacity:0, duration:.03, stagger:{each:.08}}) ×2
  div#f0p(left: 63px; top: 218px; width: 14px; height: 14px; border-radius: 2px; background: linear($ai,$ai@20%,$paper3@20%,$paper3,90); in: {opacity:0, duration:.03})
  div#f1(left: "241;251.7;262.3;273;283.7;294.3;305;315.7;326.3"; top: 218px; width: 14px; height: 14px; border-radius: 2px; background: $shu; in: {opacity:0, duration:.03, stagger:{each:.07}}) ×9
  p#y0(left: 207px; top: 126px; font-size: 22px; font-family: b; color: $ink2) 2021年
  p#p0(left: 207px; top: 156px; font-size: 46px; line-height: 1.1; font-family: m; in: {opacity:0, duration:.25}) [count:2.2 start=0 ms=600]%
  p#d0(left: 207px; top: 210px; font-size: 18px; color: $ink2) 14万8,000人中
  p#y1(left: 537px; top: 126px; font-size: 22px; font-family: b; color: $ink2) 2025年
  p#p1(left: 537px; top: 156px; font-size: 46px; line-height: 1.1; font-family: m; color: $shu; in: {opacity:0, duration:.25}) [count:9.0 start=0 ms=800]%
  p#d1(left: 537px; top: 210px; font-size: 18px; color: $ink2) 18万2,000人中
  p#lg(left: 32px; top: 304px; font-size: 18px; color: $ink2) 1マス＝宿泊者全体の1%
note#tr_nt 注：実人数。町内34軒の宿の宿泊統計より。割合の母数は町の宿泊者全体。

# mix — 二 構成: 2021 年と 2025 年の積み上げの帯を間の帯で結ぶ・「欧米豪と東南アジア」で近場を沈め遠方の凡例に朱の縁・右の札に写真と 3 行 (語で倍率が弾む)・下に「近場 → 遠方」の矢印とマーカー
section#mix(stagger: {each: 0})
paper#mx_pg(g: 客; o: "mx_bd,mx_cd,subtitle")
hdr#mx_hd(c: "$ink2;$shu;$ink2;$ink2;$ink2;$ink2"; f: "r;b;r;r;r;r")
chap#mx_ch(n: 二; k: "構成｜国・地域別"; t: "伸びの中心は、欧米豪と東南アジア")
board#mx_bd(left: 96px; width: 1064px)
  btitle#t {fg}図2{/}  {tt}国・地域別の構成{/}  （外国人宿泊者に占める割合）
  brule#r(width: 1000px)
  p#y0(left: 32px; top: 108px; font-size: 24px; font-family: b; color: $ink2) 2021年
  p#y1(left: 32px; top: 285px; font-size: 24px; font-family: b; color: $ink2) 2025年
  div#b0(left: "100;320.4;448;552.4;604.6;645.2"; top: 92px; width: "219.4;126.6;103.4;51.2;39.6;34.8"; height: 66px; background: "$tw;$hk;$kr;$cn;$sea;$wa"; delay: 1000; in: {scaleX:0, duration:.45, ease:'power2.out', pivot:'left', stagger:{each:.07}}) ×6
    p#t(cx: 50%; cy: 50%; font-size: 22px; font-family: b; color: "$cream;$cream;$cream;$ink;$ink;$cream") 38%;22%;18%;9%;7%;6%
  svg#rn(left: 150px; top: 158px; width: 870px; height: 110px; part: rib_near; delay: 1500; in: {opacity:0, duration:.6, ease:'power1.out'})
  svg#rf(left: 150px; top: 158px; width: 870px; height: 110px; part: rib_far; delay: 1740; in: {opacity:0, duration:.6, ease:'power1.out'})
  div#b1(left: "100;256.6;320.4;442.2;488.6;575.6"; top: 268px; width: "155.6;62.8;120.8;45.4;86;104.4"; height: 66px; background: "$tw;$hk;$kr;$cn;$sea;$wa"; delay: 1550; in: {scaleX:0, duration:.45, ease:'power2.out', pivot:'left', stagger:{each:.07}}) ×6
    p#t(cx: 50%; cy: 50%; font-size: 22px; font-family: b; color: "$cream;$cream;$cream;$ink;$ink;$cream") 27%;11%;21%;8%;15%;18%
  # 凡例 2 組 (近場 4 つ・遠方 2 つ) を細い罫の枠で
  div#ln(left: 34px; top: 374px; width: 423px; height: 52px; border: 2px solid $paper3; border-radius: 6px; delay: 2000; in: {y:14, opacity:0, duration:.6, ease:'power2.out'})
    p#k(left: 15px; cy: 50%; font-size: 20px; letter-spacing: .12em; font-family: b; color: $ink2) 近場
    div#c(left: "54;111;168;225"; cy: 50%; width: 15px; height: 15px; border-radius: 3px; background: "$tw;$hk;$kr;$cn") ×4
    p#t(left: "69;126;183;240"; cy: 50%; font-size: 22px) ×4 台湾;香港;韓国;中国
  div#lf(left: 504px; top: 374px; width: 340px; height: 52px; border: 2px solid $paper3; border-radius: 6px; delay: 2000; in: {y:14, opacity:0, duration:.6, ease:'power2.out'})
    p#k(left: 15px; cy: 50%; font-size: 20px; letter-spacing: .12em; font-family: b; color: $ink2) 遠方
    div#c(left: "54;156"; cy: 50%; width: 15px; height: 15px; border-radius: 3px; background: "$sea;$wa") ×2
    p#t(left: "69;171"; cy: 50%; font-size: 22px) ×2 東南アジア;欧米豪
  div#sr(left: 32px; top: 470px; width: 1000px; height: 2px; background: $paper3)
  p#from(left: 33px; cy: 540px; font-size: 38px; font-family: m; color: $ink2; in: {x:-16, opacity:0, duration:.6, ease:'power2.out'}) 近場の常連が中心
  p#to(left: 478px; cy: 540px; font-size: 42px; font-family: m; in: {x:-14, opacity:0, duration:.6, ease:'power3.out'}) {mk}遠方の客が混ざる構成へ{/}
#mx_bd.lf.hot(border: 2px solid $shu)
shape#mx_arrow(path: "M306.3 528 H358.3 M349 520.7 L359.7 528 L349 535.3"; background: none; border: 3px solid $shu; in: draw {duration: 0.6})
card#mx_cd(left: 1196px; top: 252px; width: 628px; height: 636px; delay: 1300; in: {x:40, opacity:0, duration:.7, ease:'power3.out'})
  img#ph(left: 0px; top: 0px; width: 628px; height: 195px; border-radius: 6px 6px 0px 0px; subject: center 60%; room: bottom 25%; main: kb {scale: [1.1, 1], focus: ['50% 60%', '50% 60%']}) [photo]Travelers from several different countries walking up a gentle stone-paved slope in a Japanese hot-spring town in soft daylight, pulling small suitcases and carrying backpacks, seen from behind at a moderate distance, the group in the middle of the frame, wooden inns on both sides and drifting steam around them, a mountain in the distance. Wide panoramic composition; the bottom fifth is plain stone pavement for a caption band.
  div#cap(left: 0px; top: 142px; width: 628px; height: 52px; background: linear(#14100CCC,#14100C00,0); delay: 2000; in: {y:12, opacity:0, duration:.5, ease:'power2.out'})
    p#t(left: 22px; cy: 50%; font-size: 21px; letter-spacing: .04em; font-family: b; color: $lt6) 遠方からの旅行者が増えた
  ctitle#t(top: 219px; in: {opacity:0, duration:.5}) 人数の変化（2021年 → 2025年）
  div#r0(left: 32px; top: 252px; width: 566px; height: 124px; in: {y:18, opacity:0, duration:.5, ease:'power2.out'})
    div#c(left: 2px; top: 26px; width: 16px; height: 16px; border-radius: 3px; background: $tw)
    p#nm(left: 28px; top: 15px; font-size: 28px; font-family: b) 台湾
    p#fl(left: 0px; top: 63px; font-size: 22px; color: $ink2) {n}1,216{/}人 → {n}4,428{/}人
    p#tag(right: 0px; top: 39px; font-size: 21px; font-family: b; color: $cream; background: $ai; border-radius: 4px; padding: 6px 14px) 今も最多
    div#sep(left: 0px; top: 123px; width: 566px; height: 2px; background: $paper3)
  div#r1(left: 32px; top: 376px; width: 566px; height: 124px; in: {y:18, opacity:0, duration:.5, ease:'power2.out'})
    div#c(left: 2px; top: 26px; width: 16px; height: 16px; border-radius: 3px; background: $wa)
    p#nm(left: 28px; top: 15px; font-size: 28px; font-family: b) 欧米豪
    p#fl(left: 0px; top: 63px; font-size: 22px; color: $ink2) {n}192{/}人 → {n}2,952{/}人
    p#mul(right: 0px; top: 26px; font-size: 76px; line-height: 1; font-family: m; color: $shu; in: {scale:.6, opacity:0, duration:.55, ease:'back.out(1.8)', pivot:'right'}) 約15倍
    div#sep(left: 0px; top: 123px; width: 566px; height: 2px; background: $paper3)
  div#r2(left: 32px; top: 501px; width: 566px; height: 124px; in: {y:18, opacity:0, duration:.5, ease:'power2.out'})
    div#c(left: 2px; top: 26px; width: 16px; height: 16px; border-radius: 3px; background: $sea)
    p#nm(left: 28px; top: 15px; font-size: 28px; font-family: b) 東南アジア
    p#fl(left: 0px; top: 63px; font-size: 22px; color: $ink2) {n}224{/}人 → {n}2,460{/}人
    p#mul(right: 0px; top: 26px; font-size: 76px; line-height: 1; font-family: m; color: $sea_t; in: {scale:.6, opacity:0, duration:.55, ease:'back.out(1.8)', pivot:'right'}) 約11倍
note#mx_nt 注：構成比は外国人宿泊者（実人数）に占める割合。人数は2021年→2025年。

# spend — 三 滞在と消費: 6 行の横棒の対 (泊数・消費額) が語で伸び、欧米豪の行に朱の地と朱の棒・平均の行・右に消費総額の札 (2 本の棒と「約6.8倍」) と占める割合の札 (語で数え、28% を丸で囲む)
section#spend(stagger: {each: 0})
paper#sp_pg(g: 泊; o: "sp_bd,sp_tot,sp_share,sp_circ,subtitle")
hdr#sp_hd(c: "$ink2;$ink2;$shu;$ink2;$ink2;$ink2"; f: "r;r;b;r;r;r")
chap#sp_ch(n: 三; k: "滞在と消費｜2025年"; t: "長く泊まり、よくお金を使う客層")
board#sp_bd(left: 96px; width: 1036px)
  btitle#t {fg}図3{/}  {tt}平均滞在日数と1人あたり消費額{/}  （2025年・国・地域別）
  brule#r(width: 974px)
  p#th(left: "193;413"; top: 80px; font-size: 21px; letter-spacing: .06em; font-family: b; color: $ink2; delay: 1000; in: {opacity:0, duration:.5, stagger:{each:.1}}) ×2 平均滞在日数;1人あたり消費額
  div#hl(left: 20px; top: 118px; width: 998px; height: 64px; background: #B23C2717; border-radius: 4px; in: {scaleX:.96, opacity:0, duration:.5, ease:'power2.out'})
  p#nm(left: 39px; top: "89.5;135.5;182.5;229.5;275.5;322.5"; font-size: 26px; font-family: b; padding: 0px 0px 0px 26px; delay: 1050; in: {x:-14, opacity:0, duration:.45, ease:'power2.out', stagger:{each:.07}}) ×6 欧米豪;東南アジア;中国;香港;台湾;韓国
    div#c(left: 0px; cy: 50%; width: 15px; height: 15px; border-radius: 3px; background: "$wa;$sea;$cn;$hk;$tw;$kr")
  div#nb(left: 290px; top: "90;136;183;230;276;323"; width: "130.7;93.3;84;79.3;74.7;65.3"; height: 30px; background: $mute; border-radius: 2px; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left', stagger:{each:.08}}) ×6
  p#nv(left: "331.7;294.3;285;280.3;275.7;266.3"; cy: "100.5;146.5;193.5;240.5;286.5;333.5"; font-size: 28px; font-family: m; white-space: nowrap; in: {opacity:0, duration:.4, stagger:{each:.08}}) ×6 2.8泊;2.0泊;1.8泊;1.7泊;1.6泊;1.4泊
  div#sb(left: 620px; top: "90;136;183;230;276;323"; width: "143.3;94.8;87.9;83.2;78.6;67.1"; height: 30px; background: $mute; border-radius: 2px; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left', stagger:{each:.08}}) ×6
  p#sv(left: "564.3;515.7;509;504.3;499.7;488.3"; cy: "100.5;146.5;193.5;240.5;286.5;333.5"; font-size: 28px; font-family: m; white-space: nowrap; in: {opacity:0, duration:.4, stagger:{each:.08}}) ×6 6万2,000円;4万1,000円;3万8,000円;3万6,000円;3万4,000円;2万9,000円
  # 全体の平均の行 (上の罫 + 題 + 2021 年 → 2025 年)
  div#avg(left: 32px; top: 548px; width: 974px; height: 66px; in: {y:16, opacity:0, duration:.6, ease:'power2.out'})
    div#rl(left: 0px; top: 0px; width: 974px; height: 2px; background: $paper3)
    p#k(left: 3px; cy: 45px; font-size: 22px; letter-spacing: .08em; font-family: b) 外国人全体の平均
    p#a(left: 214px; cy: 45px; font-size: 22px; color: $ink2; white-space: nowrap) {n20}1.4{/}泊・約{n20}3{/}万円（2021年）
    p#ar(left: 530px; cy: 45px; font-size: 30px; font-family: b; color: $shu) →
    p#b(left: 570px; cy: 45px; font-size: 22px; color: $ink2; white-space: nowrap) {n20}1.9{/}泊・約{n20}3万9,600{/}円（2025年）
card#sp_tot(left: 1166px; top: 252px; width: 658px; height: 318px; in: {x:40, opacity:0, duration:.6, ease:'power3.out'})
  ctitle#t 外国人の消費総額
  p#x(right: 34px; top: 32px; font-size: 104px; line-height: 1; font-family: m; color: $shu; in: {scale:.6, opacity:0, duration:.6, ease:'back.out(1.8)', pivot:'100%,30%'}) {s29}約{/}6.8{s35}倍{/}
  p#y0(left: 34px; cy: 182px; font-size: 22px; font-family: b; color: $ink2) 2021年
  p#y1(left: 34px; cy: 256px; font-size: 22px; font-family: b; color: $ink2) 2025年
  div#m0(left: 129px; top: 165px; width: 44px; height: 33px; background: $ai; border-radius: 2px; in: {scaleX:0, duration:.5, ease:'power2.out', pivot:'left'})
  div#m1(left: 129px; top: 240px; width: 300px; height: 33px; background: $shu; border-radius: 2px; in: {scaleX:0, duration:1, ease:'expo.out', pivot:'left'})
  p#v0(left: 183px; cy: 182px; font-size: 32px; font-family: m; in: {opacity:0, duration:.4}) 約0.96億円
  p#v1(left: 440px; cy: 256px; font-size: 32px; font-family: m; color: $shu; in: {opacity:0, duration:.4}) 約6.5億円
card#sp_share(left: 1166px; top: 590px; width: 658px; height: 298px; in: {x:40, opacity:0, duration:.6, ease:'power3.out'})
  ctitle#t 欧米豪が占める割合（2025年）
  p#y0(left: 34px; cy: 108px; font-size: 24px; font-family: b; color: $ink2) 人数
  p#y1(left: 34px; cy: 196px; font-size: 24px; font-family: b; color: $ink2) 消費額
  div#k0(left: 144px; top: 90px; width: 380px; height: 36px; background: $paper2; border-radius: 3px)
  div#f0(left: 144px; top: 90px; width: 68px; height: 36px; background: $f18; border-radius: 3px 0px 0px 3px; in: {scaleX:0, duration:.6, ease:'power3.out', pivot:'left'})
  div#k1(left: 144px; top: 178px; width: 380px; height: 36px; background: $paper2; border-radius: 3px)
  div#f1(left: 144px; top: 178px; width: 106px; height: 36px; background: $shu; border-radius: 3px 0px 0px 3px; in: {scaleX:0, duration:.7, ease:'power3.out', pivot:'left'})
  p#v0(left: 536px; cy: 105px; font-size: 46px; line-height: 1; font-family: m; in: {opacity:0, duration:.25}) [count:18 start=0 ms=600]%
  p#v1(left: 536px; cy: 194px; font-size: 46px; line-height: 1; font-family: m; color: $shu; in: {opacity:0, duration:.25}) [count:28 start=0 ms=700]%
# 28% を囲む手書きの丸 (svg の path を canvas の px に写して線で描く)
shape#sp_circ(overlap: sp_share; path: "M1109 527.3 C1105 506 1178.3 499.3 1185 520.7 C1190.3 540.7 1133 555.3 1110.3 540.7 C1101 534 1105 518 1119.7 512.7"; background: none; border: 3px solid $shu; in: draw {duration: 0.7})
note#sp_nt 注：平均滞在日数・1人あたり消費額は2025年。外国人全体の平均のみ2021年と比較。

# season — 四 季節: 月別の縦棒 12 本が頭に順に伸び、「雪」「紅葉」で写真の小窓と朱の棒と括弧・「37%」を数える・「3.4倍」の札と最少の月への破線・「6月から9月」で藍の棒と閑散期の括弧と「18%」
section#season(stagger: {each: 0})
paper#se_pg(g: 季; o: "se_bd,se_ba,se_la,se_bs,subtitle")
hdr#se_hd(c: "$ink2;$ink2;$ink2;$shu;$ink2;$ink2"; f: "r;r;r;b;r;r")
chap#se_ch(n: 四; k: "季節｜2025年の月別"; t: "季節の偏りは、大きいまま")
board#se_bd(left: 96px; width: 1728px)
  btitle#t {fg}図4{/}  {tt}月別の外国人宿泊者数{/}  （2025年・人）
  brule#r(width: 1665px)
  div#bar(left: "58;147.3;236.7;326;415.3;504.6;594;683.3;772.6;862;951.3;1040.6"; top: "175.3;188.7;250.9;219.8;268.7;306.9;292.7;282;305.1;210.9;179.8;205.6"; width: 80px; height: "186.7;173.3;111.1;142.2;93.3;55.1;69.3;80;56.9;151.1;182.2;156.4"; background: $mute; border-radius: 2px; delay: 1000; in: {scaleY:0, duration:.55, ease:'power3.out', pivot:'bottom', stagger:{each:.07}}) ×12
  p#mon(left: "40;129.3;218.7;308;397.3;486.6;576;665.3;754.6;844;933.3;1022.6"; top: 550px; width: 134px; font-size: 22px; text-align: center; color: $ink2; delay: 1000; in: {opacity:0, duration:.4, stagger:{each:.04}}) ×12 1月;2月;3月;4月;5月;6月;7月;8月;9月;10月;11月;12月
  thumb#ts(left: 36px; top: 100px) [photo]A steaming outdoor rock hot-spring bath at a Japanese mountain inn in deep winter, thick snow on the rocks and pine branches, snowflakes falling, cool blue morning light with warm steam, no people, the bath in the center of the frame.
  thumb#ta(left: 194px; top: 100px; in: {scale:.85, opacity:0, rotation:3, duration:.55, ease:'back.out(1.6)'}) [photo]A Japanese hot-spring town at the peak of autumn foliage, a small vermilion arched wooden bridge over a clear mountain river in the center of the frame, maple trees in crimson and orange covering the slopes, light steam over the water, soft overcast light, no people.
  p#val(left: "40;129.3;218.7;308;397.3;486.6;576;665.3;754.6;844;933.3;1022.6"; top: "153;166.3;228.6;197.4;246.3;284.6;270.3;259.7;282.8;188.6;157.4;183.2"; width: 134px; font-size: 21px; line-height: 1.2; font-family: b; text-align: center; delay: 1250; in: {y:10, opacity:0, duration:.35, ease:'power2.out', stagger:{each:.07}}) ×12 2,100;1,950;1,250;1,600;1,050;620;780;900;640;1,700;2,050;1,760
  p#c1(left: 351px; top: 99px; font-size: 72px; line-height: 1; font-family: m; color: $shu; in: {x:-12, opacity:0, duration:.5, ease:'power2.out'}) [count:37 start=0 ms=800]%
  p#l1(left: 351px; top: 174px; font-size: 21px; color: $ink2; white-space: nowrap; in: {x:-12, opacity:0, duration:.5, ease:'power2.out'}) 雪の{bk}1〜2月{/}＋紅葉の{bk}11月{/}（3か月）
  div#co2(left: 740px; top: 92px; width: 495px; height: 112px; in: {y:20, opacity:0, duration:.5, ease:'power2.out'})
    p#c(left: 0px; top: 8px; font-size: 72px; line-height: 1; font-family: m) 3.4倍
    p#l(left: 0px; top: 82px; font-size: 21px; color: $ink2; white-space: nowrap) {bk}1月{/}（最多 2,100人）は{bk}6月{/}（最少 620人）の
  thumb#tm(left: 1240px; top: 100px; in: {scale:.85, opacity:0, rotation:-2, duration:.55, ease:'back.out(1.6)'}) [photo]A quiet Japanese hot-spring town street on an early summer afternoon in the off-season, lush deep-green mountains, an almost empty stone-paved street in the center of the frame, wooden inns with bamboo blinds, one distant pedestrian, gentle hazy light, a calm slightly lonely atmosphere.
  p#c3(left: 1398px; top: 99px; font-size: 72px; line-height: 1; font-family: m; color: $ai; in: {opacity:0, duration:.25}) [count:18 start=0 ms=700]%
  p#l3(left: 1398px; top: 174px; font-size: 21px; color: $ink2; white-space: nowrap; in: {y:20, opacity:0, duration:.5, ease:'power2.out'}) {bk}6〜9月{/}の4か月の合計
# 最多の 1 月の高さから最少の 6 月へ引く破線 (3.4 倍)・3 つの括弧と名札
shape#se_dash(path: "M148.7 474.5 H595.3"; background: none; border: 2px solid $ink; dash: 5,5; in: {opacity:0, duration:.5})
shape#se_bw(path: "M117.3 558 V566 H269.3 V558"; background: none; border: 3px solid $shu; in: {scaleY:0, opacity:0, duration:.4, pivot:'top'})
p#se_lw(cx: 290px; top: 852px; font-size: 18px; font-family: b; color: $shu; in: {opacity:0, duration:.4}) 雪
shape#se_ba(path: "M1010.7 558 V566 H1073.3 V558"; background: none; border: 3px solid $shu; in: {scaleY:0, opacity:0, duration:.4, pivot:'top'})
p#se_la(cx: 1563px; top: 852px; font-size: 18px; font-family: b; color: $shu; in: {opacity:0, duration:.4}) 紅葉
shape#se_bs(path: "M564 558 V566 H894.7 V558"; background: none; border: 3px solid $ai; in: {scaleY:0, opacity:0, duration:.4, pivot:'top'})
p#se_ls(cx: 1094px; top: 852px; font-size: 18px; font-family: b; color: $ai; in: {opacity:0, duration:.4}) 閑散期（6〜9月）
note#se_nt 注：2025年の外国人宿泊者（実人数）の月別。合計1万6,400人。

# tax — 五 宿泊税: 延べ宿泊数と日本人 / 外国人の帯 (頭に伸びる)・「1泊200円なら」で左の札と年額を数え上げ・「外国人の分」で内訳の帯と 2 つの札・右に 300 円の札・「13%」で朱の帯が弾み・「大半は」で下線のマーカー
section#tax(stagger: {each: 0})
paper#tx_pg(g: 税; o: "tx_bd,subtitle")
hdr#tx_hd(c: "$ink2;$ink2;$ink2;$ink2;$shu;$ink2"; f: "r;r;r;r;b;r")
chap#tx_ch(n: 五; k: "宿泊税｜2025年の実績で試算"; t: "税収の大半は、日本人客から")
board#tx_bd(left: 96px; width: 1728px)
  btitle#t {fg}図5{/}  {tt}宿泊税の試算{/}  （日本人を含む全宿泊者に、1人1泊あたり定額）
  brule#r(width: 1665px)
  p#nk(left: 32px; top: 80px; font-size: 22px; font-family: b; color: $ink2; delay: 1000; in: {y:14, opacity:0, duration:.5, ease:'power2.out'}) 延べ宿泊数（2025年）
  p#nv(left: 32px; top: 120px; font-size: 56px; line-height: 1.05; font-family: m; delay: 1120; in: {y:14, opacity:0, duration:.5, ease:'power2.out'}) 22万9,240{s20}泊{/}
  div#jp(left: 420px; top: 112px; width: 1099px; height: 62px; background: $ai; delay: 1100; in: {scaleX:0, duration:.8, ease:'power3.out', pivot:'left'})
    p#t(left: 24px; cy: 50%; font-size: 24px; font-family: b; color: $cream) 日本人 19万8,720泊
  div#fr(left: 1521px; top: 112px; width: 169px; height: 62px; background: $shu; delay: 1800; in: {scaleX:0, duration:.5, ease:'power3.out', pivot:'left'})
  p#fl(left: 1496px; top: 78px; font-size: 21px; font-family: b; color: $shu; delay: 2100; in: {y:-10, opacity:0, duration:.45, ease:'power2.out'}) 外国人 3万520泊 ↓
  div#ca(left: 32px; top: 236px; width: 1040px; height: 366px; background: $card; border: 2px solid $rule; border-radius: 6px; in: {y:30, opacity:0, duration:.6, ease:'power3.out'})
    p#pill(left: 30px; top: 26px; font-size: 24px; font-family: b; color: $cream; background: $shu; border-radius: 148px; padding: 8px 22px) 1泊200円なら
    p#yen(left: 30px; top: 86px; font-size: 112px; line-height: 1; font-family: m; in: {opacity:0, duration:.4}) {yk}年に{/} {yu}約{/}[count:4,585 start=0 ms=1300 delay=100]{yu}万円{/}
    div#sj(left: 30px; top: 232px; width: 815px; height: 40px; background: $ai; in: {scaleX:0, duration:.7, ease:'power3.out', pivot:'left'})
    div#sf(left: 845px; top: 232px; width: 125px; height: 40px; background: $shu; in: {scaleX:0, duration:.45, ease:'power3.out', pivot:'left'})
    p#lj(left: 30px; top: 280px; font-size: 21px; font-family: b; color: $ai; in: {opacity:0, duration:.4}) 日本人客の分（大半）
    p#lf(left: 700px; top: 280px; font-size: 21px; font-family: b; color: $shu; in: {x:12, opacity:0, duration:.5, ease:'power2.out'}) 外国人の分 約610万円（13%）
    p#st(left: 30px; top: 316px; font-size: 34px; font-family: m; in: {y:10, opacity:0, duration:.5, ease:'power2.out'}) {mk}税収の大半は、日本人客から入る{/}
  div#cb(left: 1104px; top: 236px; width: 590px; height: 366px; background: $card; border: 2px solid $rule; border-radius: 6px; in: {x:30, opacity:0, duration:.6, ease:'power3.out'})
    p#pill(left: 30px; top: 26px; font-size: 24px; font-family: b; color: $cream; background: $ai; border-radius: 148px; padding: 8px 22px) 1泊300円なら
    p#yen(left: 30px; top: 98px; font-size: 96px; line-height: 1; font-family: m) {yk}年に{/} {yu}約{/}6,877{yu}万円{/}
    p#n(left: 30px; top: 236px; font-size: 21px; color: $ink2) 同じ2025年の延べ宿泊数で計算
note#tx_nt 注：延べ宿泊数 22万9,240泊（日本人 19万8,720泊・外国人 3万520泊）に定額を掛けた試算。

# issue — 六 課題: 困りごと 4 行の横棒が語で伸びて数える (1 位は朱)・右上に駅の写真と札・「日本語だけ」「現金しか」で宿の対応の札に 34 マスを 1 マスずつ
section#issue(stagger: {each: 0})
paper#is_pg(g: 課; o: "is_bd,is_ph,is_cap,is_un,subtitle")
hdr#is_hd(c: "$ink2;$ink2;$ink2;$ink2;$ink2;$shu"; f: "r;r;r;r;r;b")
chap#is_ch(n: 六; k: "課題｜2025年アンケート"; t: "受け入れの課題は、足・表示・支払い")
board#is_bd(left: 96px; width: 1044px)
  btitle#t {fg}図6{/}  {tt}外国人旅行者が困ったこと{/}  （複数回答・回答612人）
  brule#r(width: 981px)
  p#lb(left: 32px; top: "59;139;219;299"; font-size: 26px; font-family: b; white-space: nowrap; delay: 1100; in: {x:-12, opacity:0, duration:.45, ease:'power2.out', stagger:{each:.1}}) ×4 {qn}1{/} 駅から宿・湯めぐりへの移動手段;{qn}2{/} 案内表示が日本語だけ;{qn}3{/} 現金しか使えない店;{qn}4{/} 入浴の作法が分からない
  div#trk(left: 32px; top: "88;168;248;328"; width: 760px; height: 44px; background: $paper2; border-radius: 3px; delay: 1150; in: {opacity:0, duration:.45, stagger:{each:.1}}) ×4
  div#bar(left: 32px; top: "88;168;248;328"; width: "439.1;346.2;320.9;160.5"; height: 44px; background: "$shu;$ai;$ai;$ai"; border-radius: 3px 0px 0px 3px; in: {scaleX:0, duration:.7, ease:'power3.out', pivot:'left'}) ×4
  p#v(left: 822px; cy: "103;183;263;343"; font-size: 54px; line-height: 1; font-family: m; color: "$shu;$ink;$ink;$ink"; in: {opacity:0, duration:.3}) ×4 [count:52 start=0 ms=700]%;[count:41 start=0 ms=700]%;[count:38 start=0 ms=700]%;[count:19 start=0 ms=700]%
  p#sc(cx: "29;190;354;518"; top: 562px; font-size: 16px; color: $ink2; delay: 1500; in: {opacity:0, duration:.5}) ×4 0%;20%;40%;60%
# 写真の額 (生成りの 5 px の縁 + 影) の中で写真が 1.12 → 1.0 に引く (縁つきの絵に kb を掛けると絵が額の中で小さく縮んだので、額の箱 + 子の絵に分けた)
div#is_ph(left: 1180px; top: 252px; width: 644px; height: 280px; background: $lt7; box-shadow: 0px 9px 18px #00000059; delay: 1000; in: {scale:.94, opacity:0, duration:.8, ease:'power2.out'})
  img#p(left: 8px; top: 8px; width: 628px; height: 266px; subject: center 45%; room: bottom 20%; main: kb {scale: [1.12, 1], focus: ['50% 45%', '50% 45%']}) [photo]A full-bleed wide photograph that fills the entire canvas edge to edge, with no white border, no mat, no margins and no frame around it. A small rural railway station in a Japanese mountain valley: one platform with a modest wooden shelter on the left, the rails leading into the frame toward a distant hot-spring town where faint steam rises in the center, a lone bus-stop pole and a bench by the narrow road on the right, overcast soft light, nobody waiting. Wide panoramic composition with the scene running to all four edges: the shelter touches the left edge, the road and bench reach the right edge, the sky touches the top; the bottom fifth is the quiet platform edge and gravel for a caption band.
div#is_cap(left: 1188px; top: 471px; width: 628px; height: 54px; background: linear(#14100CD1,#14100C00,0); overlap: is_ph; in: {y:16, opacity:0, duration:.5, ease:'power2.out'})
  p#b(left: 20px; cy: 50%; font-size: 20px; font-family: b; color: $cream; background: $shu; border-radius: 3px; padding: 2px 10px) 困りごと1位
  p#t(left: 156px; cy: 50%; font-size: 21px; font-family: b; color: $lt6) 駅から宿・湯めぐりへの足
card#is_un(left: 1180px; top: 552px; width: 644px; height: 336px; in: {x:30, opacity:0, duration:.6, ease:'power3.out'})
  ctitle#t(left: 30px; top: 27px) 宿の側の対応（町内34軒）
  div#u0(left: 30px; top: 78px; width: 584px; height: 118px)
    p#lb(left: 0px; top: 3px; font-size: 22px; font-family: b; in: {opacity:0, duration:.4}) 多言語で予約を受けられる
    p#v(right: 0px; top: -4px; font-size: 34px; font-family: m; color: $ai; in: {opacity:0, duration:.4}) 12軒{sm} 35%{/}
    div#c(left: "0;22.6;45.1;67.7;90.2;112.8;135.4;157.9;180.5;203;225.6;248.2;270.7;293.3;315.8;338.4;361;0;22.6;45.1;67.7;90.2;112.8;135.4;157.9;180.5;203;225.6;248.2;270.7;293.3;315.8;338.4;361"; top: "29;29;29;29;29;29;29;29;29;29;29;29;29;29;29;29;29;51;51;51;51;51;51;51;51;51;51;51;51;51;51;51;51;51"; width: 28px; height: 28px; border-radius: 4px; background: "$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none;none"; border: "2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3"; in: {scale:.4, opacity:0, duration:.25, ease:'back.out(2)', stagger:{each:.02}}) ×34
  div#u1(left: 30px; top: 204px; width: 584px; height: 118px)
    p#lb(left: 0px; top: 3px; font-size: 22px; font-family: b; in: {opacity:0, duration:.4}) キャッシュレス決済に対応
    p#v(right: 0px; top: -4px; font-size: 34px; font-family: m; color: $ai; in: {opacity:0, duration:.4}) 21軒{sm} 62%{/}
    div#c(left: "0;22.6;45.1;67.7;90.2;112.8;135.4;157.9;180.5;203;225.6;248.2;270.7;293.3;315.8;338.4;361;0;22.6;45.1;67.7;90.2;112.8;135.4;157.9;180.5;203;225.6;248.2;270.7;293.3;315.8;338.4;361"; top: "29;29;29;29;29;29;29;29;29;29;29;29;29;29;29;29;29;51;51;51;51;51;51;51;51;51;51;51;51;51;51;51;51;51"; width: 28px; height: 28px; border-radius: 4px; background: "$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;$ai;none;none;none;none;none;none;none;none;none;none;none;none;none"; border: "2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $ai;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3;2px solid $paper3"; in: {scale:.4, opacity:0, duration:.25, ease:'back.out(2)', stagger:{each:.02}}) ×34
note#is_nt 注：アンケートの「困ったこと」は複数回答。宿の対応は町内34軒のうちの軒数。

# wrap — まとめ: 夜の温泉街の写真 (1.0 → 1.07)・右に暗幕と生成りの板 (題 + 朱の丸い判子「提言」)・語で 3 つの要点・締めの一文に下線のマーカー・声の後に左下の出典
section#wrap(stagger: {each: 0})
img#wr_photo(inset: 0; subject: "24%,44%,20%,28%"; room: right 52%; main: kb {scale: [1, 1.07], focus: ['30% 60%', '30% 60%']}) [photo]Night in a Japanese hot-spring town: warm paper lanterns glow at the entrance of a wooden ryokan on the left side, steam drifting across the lamplit wet stone street that leads into the distance, two travelers in yukata walking away in the middle distance at about one third from the left, reflections on damp stones, a deep indigo sky over dark mountains. The right half of the frame is the calm dark sky, mountains and far street, uncluttered for an overlay panel; the bottom-left corner is dark pavement.
div#wr_shade(inset: 0; background: linear(#0A0C14B3,#0A0C1459@45%,#0A0C1426@70%,270); in: none)
div#wr_grain(inset: 0; grain: 0.06; in: none)
div#wr_cs(left: 0px; top: 560px; width: 1100px; height: 520px; background: radial(#080706DB,#0807068C@45%,#08070600@75%,10%,95%); in: {opacity:0, duration:.9, ease:'power1.out'})
div#wr_credit(left: 96px; top: 765px; width: 750px; height: 144px; in: {y:14, opacity:0, duration:.8, ease:'power2.out'})
  p#t(left: 0px; top: 0px; font-size: 30px; letter-spacing: .06em; font-family: m; color: $lt8) 湯ノ瀬町 観光課｜調査報告
  p#s(left: 0px; top: 51px; width: 750px; font-size: 20px; line-height: 1.6; color: $lt9) 出典：町内34軒の宿の宿泊統計（2021〜2025年）、外国人旅行者アンケート（2025年・回答612人）。※湯ノ瀬町は架空の町です。
div#wr_panel(left: 892px; top: 106px; width: 932px; height: 800px; background: #F6F1E8F5; border-radius: 8px; box-shadow: 0px 18px 42px #00000080; delay: 550; in: {x:50, opacity:0, duration:.8, ease:'power3.out'})
  p#h(left: 52px; cy: 87px; font-size: 58px; font-family: m; delay: 200; in: {y:16, opacity:0, duration:.6, ease:'power2.out'}) まとめ
  p#hs(left: 248px; cy: 94px; font-size: 22px; letter-spacing: .06em; color: $ink2; delay: 400; in: {opacity:0, duration:.6}) 5年の変化と、これから
  div#stamp(left: 802px; top: 48px; width: 76px; height: 76px; border: 3px solid $shu; border-radius: 148px; transform: rotate(-8deg); delay: 250; in: {scale:1.8, rotation:-30, opacity:0, duration:.45, ease:'back.out(2.4)'})
    p#t(cx: 50%; cy: 50%; font-size: 26px; font-family: m; color: $shu) 提言
  div#hr(left: 52px; top: 132px; width: 826px; height: 2px; background: $rule)
  div#p1(left: 52px; top: 160px; width: 826px; height: 150px; in: {x:26, opacity:0, duration:.6, ease:'power3.out'})
    p#n(left: 0px; top: 0px; font-size: 64px; line-height: 1; font-family: m; color: $shu) 一
    p#m(left: 96px; top: 0px; font-size: 34px; line-height: 1.32; font-family: m) 外国人客は5年で約5倍、宿泊者の9%に
    p#d(left: 96px; top: 52px; font-size: 22px; line-height: 1.45; color: $ink2) 伸びの中心は欧米豪と東南アジア。[br]長く泊まり、お金を使う客が増えた。
  div#p2(left: 52px; top: 330px; width: 826px; height: 150px; in: {x:26, opacity:0, duration:.6, ease:'power3.out'})
    p#n(left: 0px; top: 0px; font-size: 64px; line-height: 1; font-family: m; color: $shu) 二
    p#m(left: 96px; top: 0px; font-size: 34px; line-height: 1.32; font-family: m) 弱点は、夏の閑散期と3つの不便
    p#d(left: 96px; top: 52px; font-size: 22px; line-height: 1.45; color: $ink2) 駅からの足、多言語の表示、現金のみの店。
  div#p3(left: 52px; top: 480px; width: 826px; height: 150px; in: {x:26, opacity:0, duration:.6, ease:'power3.out'})
    p#n(left: 0px; top: 0px; font-size: 64px; line-height: 1; font-family: m; color: $shu) 三
    p#m(left: 96px; top: 0px; font-size: 34px; line-height: 1.32; font-family: m) 宿泊税は1泊200円で、年約4,600万円
    p#d(left: 96px; top: 52px; font-size: 22px; line-height: 1.45; color: $ink2) 使い道を、二次交通と案内表示に向ける。
  div#hr2(left: 52px; top: 680px; width: 826px; height: 2px; background: $rule)
  p#fin(left: 52px; cy: 729px; font-size: 44px; font-family: m; in: {y:12, opacity:0, duration:.6, ease:'power2.out'}) {mk}税を払う客の不便が、そのまま減る。{/}
```

```timeline.txt
#v2
cast n = "落ち着いた低音の30〜40代の男性ナレーター、響きが豊かで滑らか、息の成分が適度にあり発音が明瞭、知的で信頼感のあるドキュメンタリーの語り" speed=107%
silence head=0 tail=0
transition = slide,850,dir=left,overlap=850,ease=power3.inOut,drift=240,dim=0.38,se=page -2dB

*** title
[>#subtitle]
bgm music
@n: [silence:1.0s][♪naruko -1dB -100]山あいの温泉町、{湯ノ瀬町|ゆのせまち}。[>#t_chips[1] -50][♪pop -10dB]町の宿の宿泊統計と、外国人旅行者への[>#t_chips[2] -50][♪pop -10dB]アンケートから、[|][>#t_chips[3] -50][>#t_chips[4] +250][♪pop -10dB][♪pop -10dB +300]この5年の変化を見ていきます。[silence:0.25s]

*** trend
@n: [silence:0.55s]外国人の宿泊者は、[vbar #tr_bd.bar[1] #tr_bd.val[1]][vbar #tr_bd.bar[2] #tr_bd.val[2] +620][vbar #tr_bd.bar[3] #tr_bd.val[3] +1220][vbar #tr_bd.bar[4] #tr_bd.val[4] +1820][♪whoosh -8dB]2021年の3,200人から、[|][vbar #tr_bd.hot #tr_bd.val[5]]2025年には1万6,400人。5年で[>#tr_x5 -350][>#tr_x5.big -50][>#tr_x5.sub +350][♪chime -8dB to=0.9s]約5倍です。[>#tr_sh -300][♪paper -5dB]宿泊者全体に占める割合も、[|][>#tr_sh.p0][>#tr_sh.f0[*] +100][>#tr_sh.f0p +260]2.2%から[>#tr_sh.p1][>#tr_sh.f1[*] +50]9.0%に上がりました。[silence:0.15s]

*** mix
@n: [silence:0.55s][♪whoosh -8dB +550]伸びたのは、[!#mx_bd.b0[*] to,{opacity:.38, duration:.4}][!#mx_bd.b1[1] to,{opacity:.38, duration:.4}][!#mx_bd.b1[2] to,{opacity:.38, duration:.4}][!#mx_bd.b1[3] to,{opacity:.38, duration:.4}][!#mx_bd.b1[4] to,{opacity:.38, duration:.4}][!#mx_bd.rn to,{opacity:.38, duration:.4}][!#mx_bd.ln to,{opacity:.45, duration:.4}][!#mx_bd.lf .hot]欧米豪と東南アジアです。[>#mx_cd.t -400][>#mx_cd.r0 -100][♪paper -5dB -50][=#mx_bd.b0[*] -100][=#mx_bd.b1[1] -100][=#mx_bd.b1[2] -100][=#mx_bd.b1[3] -100][=#mx_bd.b1[4] -100][=#mx_bd.rn -100][=#mx_bd.ln -100]人数の最多は今も台湾ですが、[|][>#mx_cd.r1 -150][♪pop -10dB][!#mx_bd.b1[6] to,{scaleY:1.18, duration:.3, ease:'sine.inOut'} +100][!#mx_bd.b1[6] to,{scaleY:1, duration:.3, ease:'sine.inOut'} +400][>#mx_cd.r1.mul +500]欧米豪は約15倍、[>#mx_cd.r2 -150][♪pop -10dB][!#mx_bd.b1[5] to,{scaleY:1.18, duration:.3, ease:'sine.inOut'} +100][!#mx_bd.b1[5] to,{scaleY:1, duration:.3, ease:'sine.inOut'} +400][>#mx_cd.r2.mul +600]東南アジアは約11倍に増え、[|][>#mx_bd.from -100]近場の常連が中心だった客層に、[|][>#mx_arrow -600][>#mx_bd.to -250][!#mx_bd.to{mk} marker][♪marker -6dB -100]遠方の客が加わりました。[silence:0.15s]

*** spend
@n: [silence:0.55s]この客層は、[>#sp_bd.nb[*]][>#sp_bd.nv[*] +350][♪whoosh -8dB]長く泊まり、[>#sp_bd.sb[*]][>#sp_bd.sv[*] +350]よくお金を使います。[>#sp_bd.hl -100][!#sp_bd.nb[1] fill,$shu,duration=500 -100][!#sp_bd.sb[1] fill,$shu,duration=500 -100][♪pop -10dB]欧米豪は平均2.8泊、1人6万2,000円。[>#sp_bd.avg -500][>#sp_tot -350][♪paper -5dB -50][>#sp_tot.m0 +150][>#sp_tot.v0 +400][>#sp_tot.m1 +550][>#sp_tot.v1 +800]外国人の消費総額は[>#sp_tot.x -50][♪chime -8dB to=0.9s]約6.8倍、約6.5億円になり、[|]欧米豪は[>#sp_share -450][>#sp_share.f0 +100][>#sp_share.v0 count +100]人数の18%で、[|][>#sp_share.f1 +50][>#sp_share.v1 count +50][>#sp_circ +150][♪circle -5dB +100]消費額の28%を占めます。[silence:0.15s]

*** season
@n: [silence:0.55s][♪whoosh -8dB +200]ただ、季節の偏りは大きく、[|][>#se_bd.ts -50][♪pop -10dB][!#se_bd.bar[1] fill,$shu,duration=450 +100][!#se_bd.bar[2] fill,$shu,duration=450 +100][>#se_bw +300][>#se_lw +300]雪の{1月|いちがつ}、{2月|にがつ}と、[>#se_bd.ta -50][!#se_bd.bar[11] fill,$shu,duration=450 +100][>#se_ba +300][>#se_la +300]紅葉の{11月|じゅういちがつ}で、全体の[>#se_bd.c1 count -200][>#se_bd.l1 -200][♪circle -6dB]37%。[>#se_bd.co2 -770][>#se_dash -720][>#se_bd.l3 -150][>#se_bd.tm -50][♪pop -10dB][!#se_bd.bar[6] fill,$hk,duration=450 +100][!#se_bd.bar[7] fill,$hk,duration=450 +160][!#se_bd.bar[8] fill,$hk,duration=450 +220][!#se_bd.bar[9] fill,$hk,duration=450 +280][>#se_bs +350][>#se_ls +350]{6月|ろくがつ}から{9月|くがつ}は、{4か月|よんかげつ}合わせても[>#se_bd.c3 count -200]18%です。[silence:0.15s]

*** tax
@n: [silence:0.55s][♪whoosh -8dB +300]議題の宿泊税は、[>#tx_bd.ca -350][♪paper -5dB -50]1泊200円なら、[>#tx_bd.ca.yen -100][♪chime -8dB to=0.9s +100]年に約4,585万円。[>#tx_bd.ca.sj -450][>#tx_bd.ca.lj -200][♪pop -10dB][>#tx_bd.ca.sf +150][>#tx_bd.ca.lf +350][>#tx_bd.cb +1600]外国人の分は約610万円、[!#tx_bd.ca.sf to,{scaleY:1.35, duration:.25, ease:'sine.inOut'}][!#tx_bd.ca.sf to,{scaleY:1, duration:.25, ease:'sine.inOut'} +250]13%で、[|][>#tx_bd.ca.st -150][!#tx_bd.ca.st{mk} marker +200][♪marker -6dB]税収の大半は、日本人客から入ります。[silence:0.15s]

*** issue
@n: [silence:0.55s]受け入れの課題もはっきりしています。[♪whoosh -8dB][>#is_bd.bar[1] +250][>#is_bd.v[1] count +350][>#is_cap +600]困ったことの1位は、駅から宿や湯めぐりへの移動手段で52%。[>#is_un -300][>#is_bd.bar[2]][>#is_bd.v[2] count +100][>#is_un.u0.lb][>#is_un.u0.v][>#is_un.u0.c[*] +200][♪pop -10dB]日本語だけの案内表示、[|][>#is_bd.bar[3]][>#is_bd.v[3] count +100][>#is_un.u1.lb][>#is_un.u1.v][>#is_un.u1.c[*] +200][♪pop -10dB]現金しか使えない店が[>#is_bd.bar[4]][>#is_bd.v[4] count +100]続きます。[silence:0.25s]

*** wrap
@n: [silence:0.55s][>#wr_panel.p1][♪pop -10dB][♪naruko -2dB +250]外国人客は5年で約5倍。[>#wr_panel.p2 -150][♪pop -10dB]弱点は夏の閑散期と、駅からの足、多言語表示、現金のみの店です。[>#wr_panel.p3 -150][♪pop -10dB]1泊200円で年約4,600万円の税を、[|]二次交通と案内表示に向ければ、[|][>#wr_panel.fin -150][!#wr_panel.fin{mk} marker +250][♪marker -6dB +200]税を払う客の不便が、そのまま[>#wr_cs +700][>#wr_credit +850]減ります。[silence:3.4s]
fade out,1300
```

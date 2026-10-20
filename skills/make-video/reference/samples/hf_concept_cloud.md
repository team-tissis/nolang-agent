# concept · cloud-storage (hf 全力版の全量の写し — クラウドストレージの仕組み・端末 / ネットワーク / 保存先の 1 枚の図を 6 章 + まとめで組み直す) — canvas 1280x720

見せる作り: 明るい紙の地 (流れる点の格子と呼吸する色の光)・題の白い大きな板 (円の中に雲・保存先・端末が弾む)・左上の章の見出し (番号の札が回って弾み、下線が伸びる) と右上の進行 7 本 (sticky)・1 枚の図を def に畳んで 3 章で使う (寄りの姿から引く・流れ続ける破線の配線・ハブを経由して飛ぶファイルとパケット・語で光る区画)・POINT の注記・使い方の例の 2 枚の挿絵と弧の矢印・用語の札・中央から左へ寄って薄まる比較の板・権限の流れ (アカウント → 鍵 → 範囲に ✓ と錠)・締めの青い札・音の層 (BGM + 語ごとの効果音 68 発)

```design.txt
#v2
# 学ぶ作り: 明るい紙の地 (点の格子が流れ、色の光が呼吸する) の上で、1 枚の図 (手元の端末 / ネットワーク / サービス側) を def に畳み、章ごとに組み直して見せる
# 章は 8 cut (題 → 6 章 → まとめ)・左上の章の見出し (番号の札 + 題 + 伸びる下線) は cut ごとに出し直し、右上のシリーズ表記と 7 本の進行は sticky で章ごとに 1 本埋める
# 図の主役は語で動く小物: 線を描いて流れる破線 (dash_offset)・経由点を辿って飛ぶファイルとパケット (to,via=)・語で光る枠 (glow)・用語の札・比較の 2 枚・権限の流れ
# hf cloud cloud-storage (全力版) の全量の写し。座標は hf の 1920x1080 × 2/3
canvas 1280x720 bg=#F2F5FA
theme light
palette a=#2159E0 b=#D9680B ink=#17223A ink2=#34445E mute=#5E6D84 line=#D6DEEA blue=#2159E0 blue_d=#1742B0 blue_l=#E4ECFF blue_m=#A9C1F7 orange=#D9680B orange_d=#B45309 orange_l=#FFEFDF orange_m=#F6C08F teal=#0B8F80 teal_m=#8FD6CB wire=#CDEFEA violet=#6D3FD0 violet_l=#EEE7FD violet_m=#C4B0F3 red=#CF3B2E red_l=#FDE8E6 red_m=#F2B3AC gray=#6B7A90 card_line=#E1E8F2 track=#D3DBE8 off=#EEF1F6 pale=#DCE6FF
font "癖のない現代的な角ゴシック体の極太 (Black)、かなが小さめで字間が詰まって見える、解説動画の見出しと図の札向け"
fonts m="線のしっかり太い現代的な角ゴシック体の太字 (Bold)、字幕・ラベル・注記向け" e="幾何学的な欧文サンセリフの Black、数字と記号がくっきり"
sfx off
# hf の作り: 章の見出しと右上のシリーズ表記・区画の札は台詞より先に置く (spoiler)・図と札だけの解説で絵は使い方の例の 2 枚だけ (text_only_cut)
# hf の作り: 区画の板を先に出し中身は語で 1 つずつ (empty_board)・POINT の小札は 1080p の 22px をそのまま 2/3 (small_text)・注記は次の文の頭で消える (flash_text)
# hf の作り: 要求と渡すの間はネットワークを 0.25 まで沈める (low_contrast)・図の名札と注記の札が縦に並ぶ (stacked_labels)・アクセスの札は 3 本同時 (duplicate_text)
lint off=spoiler,text_only_cut,empty_board,small_text,flash_text,low_contrast,stacked_labels,duplicate_text
art "教育用の解説動画のフラットなベクターイラスト。清潔でミニマル、親しみやすい現代の日本のエディトリアル調。明るい地 (淡い青灰から白)、紺の線と髪、青と暖かい橙のアクセント、淡い灰色。単純な形と柔らかい影"
prompt_tail "画像の中に文字・数字・ロゴ・透かしは一切入れない"
image worker = "日本人の若い男性会社員。短い黒髪、紺のスーツに白いシャツと青いネクタイ、穏やかな表情"
run b = color=$blue
run o = color=$orange
run t = color=$teal
run v = color=$violet
run bd = color=$blue_d
run kb = color=$blue_d
run ko = color=$orange_d
run ne = color=#FFD5A8 size=43 font=e
p { color: $ink; line-height: 1.2; out: {opacity:0, duration:.35, ease:'power2.in'} }
div { border: none; box-shadow: none; padding: 0px; out: {opacity:0, duration:.35, ease:'power2.in'} }
svg { out: {opacity:0, duration:.35, ease:'power2.in'} }
shape { out: {opacity:0, duration:.35, ease:'power2.in'} }
img { main: none; out: {opacity:0, duration:.35, ease:'power2.in'} }
group { in: none; out: {opacity:0, duration:.35, ease:'power2.in'} }
# hf の小さな演出の型 (pop = 縮んだ所から back.out(1.9)・rise = 下から 17px・slideIn = 左から 27px・板 = 0.92 倍から power3.out)
motion pin7 = in=scale=0.7,opacity=0,duration=500 ease=back(1.9)
motion pin6 = in=scale=0.6,opacity=0,duration=500 ease=back(1.9)
motion pin5 = in=scale=0.5,opacity=0,duration=500 ease=back(1.9)
motion pin4 = in=scale=0.4,opacity=0,duration=500 ease=back(1.9)
motion pin3 = in=scale=0.3,opacity=0,duration=500 ease=back(1.9)
motion up = in=y=17,opacity=0,duration=500 ease=power3.out
motion slx = in=x=-27,opacity=0,duration=550 ease=power3.out
motion boxin = in=scale=0.92,opacity=0,duration=600 ease=power3.out
# 動くファイルの退場 (着いたら縮んで消える)
motion gone = out=scale=0.5,opacity=0,duration=220 ease=power2.in
sound whoosh = "短く軽い風切りのシュッという音、場面の切り替わり"
sound pop = "紙の筒で鳴らした乾いた軽いポンという音"
sound pop2 = "高く短いかわいいポコッという UI の出現音"
sound click = "トラックパッドの乾いた短いカチッというクリック音"
sound swipe = "軽く短いスワイプのシュッという UI の音"
sound shine = "キラッと光る短い高いきらめきの音"
sound q = "はてなを示す短いコミカルな疑問の効果音"
sound pen = "ペンでサッと線を引く音"
sound data = "データを送るピピッという短い電子音"
sound ok = "明るい鉄琴の上がる 2 音の正解チャイム"
sound accent = "乾いた短いポンというアクセントの音"
sound paper = "紙のカードを置くパサッという音"
sound notify = "パソコンの通知のポロンという電子音"
sound lock = "鍵をかけるカチャッという音"
sound kira = "キラリンと輝く高いきらめきの音"
# 部品の絵 (hf の icons.svg の symbol を色ごとに焼いた物)
svg laptop = """<svg viewBox="0 0 200 140"><rect x="28" y="8" width="144" height="96" rx="10" fill="#FFFFFF" stroke="#D9680B" stroke-width="6"/><rect x="40" y="20" width="120" height="72" rx="4" fill="#FFE7D0"/><path d="M8 112 H192 L182 130 Q180 134 175 134 H25 Q20 134 18 130 Z" fill="#D9680B"/><rect x="84" y="112" width="32" height="6" rx="3" fill="#FFFFFF" opacity=".55"/></svg>"""
svg phone = """<svg viewBox="0 0 100 170"><rect x="6" y="4" width="88" height="162" rx="16" fill="#FFFFFF" stroke="#D9680B" stroke-width="6"/><rect x="15" y="22" width="70" height="120" rx="4" fill="#FFE7D0"/><rect x="38" y="11" width="24" height="5" rx="2.5" fill="#D9680B"/><rect x="36" y="150" width="28" height="6" rx="3" fill="#D9680B" opacity=".8"/></svg>"""
svg phone_g = """<svg viewBox="0 0 100 170"><rect x="6" y="4" width="88" height="162" rx="16" fill="#FFFFFF" stroke="#8795AA" stroke-width="6"/><rect x="15" y="22" width="70" height="120" rx="4" fill="#FFE7D0"/><rect x="38" y="11" width="24" height="5" rx="2.5" fill="#8795AA"/><rect x="36" y="150" width="28" height="6" rx="3" fill="#8795AA" opacity=".8"/></svg>"""
svg server = """<svg viewBox="0 0 160 200"><rect x="8" y="6" width="144" height="188" rx="14" fill="#FFFFFF" stroke="#2159E0" stroke-width="6"/><g fill="#E3ECFF" stroke="#2159E0" stroke-width="4"><rect x="24" y="24" width="112" height="42" rx="7"/><rect x="24" y="79" width="112" height="42" rx="7"/><rect x="24" y="134" width="112" height="42" rx="7"/></g><g fill="#2159E0"><rect x="38" y="40" width="46" height="9" rx="4.5"/><rect x="38" y="95" width="46" height="9" rx="4.5"/><rect x="38" y="150" width="46" height="9" rx="4.5"/></g><g fill="#22C55E"><circle cx="114" cy="45" r="6"/><circle cx="114" cy="100" r="6"/><circle cx="114" cy="155" r="6"/></g></svg>"""
svg storage = """<svg viewBox="0 0 140 150"><path d="M10 26 V124 C10 138 130 138 130 124 V26" fill="#E3ECFF" stroke="#2159E0" stroke-width="6" stroke-linejoin="round"/><ellipse cx="70" cy="26" rx="60" ry="17" fill="#FFFFFF" stroke="#2159E0" stroke-width="6"/><path d="M10 60 C10 74 130 74 130 60" fill="none" stroke="#2159E0" stroke-width="5"/><path d="M10 93 C10 107 130 107 130 93" fill="none" stroke="#2159E0" stroke-width="5"/></svg>"""
svg storage_w = """<svg viewBox="0 0 140 150"><path d="M10 26 V124 C10 138 130 138 130 124 V26" fill="#FFFFFF" stroke="#2159E0" stroke-width="6" stroke-linejoin="round"/><ellipse cx="70" cy="26" rx="60" ry="17" fill="#FFFFFF" stroke="#2159E0" stroke-width="6"/><path d="M10 60 C10 74 130 74 130 60" fill="none" stroke="#2159E0" stroke-width="5"/><path d="M10 93 C10 107 130 107 130 93" fill="none" stroke="#2159E0" stroke-width="5"/></svg>"""
svg file = """<svg viewBox="0 0 100 124"><path d="M8 10 Q8 4 14 4 H64 L92 32 V114 Q92 120 86 120 H14 Q8 120 8 114 Z" fill="#FFFFFF" stroke="#2159E0" stroke-width="6" stroke-linejoin="round"/><path d="M64 4 V26 Q64 32 70 32 H92" fill="#DCE7FF" stroke="#2159E0" stroke-width="6" stroke-linejoin="round"/><g fill="#2159E0" opacity=".85"><rect x="22" y="50" width="56" height="7" rx="3.5"/><rect x="22" y="68" width="56" height="7" rx="3.5"/><rect x="22" y="86" width="36" height="7" rx="3.5"/></g></svg>"""
svg file_o = """<svg viewBox="0 0 100 124"><path d="M8 10 Q8 4 14 4 H64 L92 32 V114 Q92 120 86 120 H14 Q8 120 8 114 Z" fill="#FFFFFF" stroke="#D9680B" stroke-width="6" stroke-linejoin="round"/><path d="M64 4 V26 Q64 32 70 32 H92" fill="#DCE7FF" stroke="#D9680B" stroke-width="6" stroke-linejoin="round"/><g fill="#D9680B" opacity=".85"><rect x="22" y="50" width="56" height="7" rx="3.5"/><rect x="22" y="68" width="56" height="7" rx="3.5"/><rect x="22" y="86" width="36" height="7" rx="3.5"/></g></svg>"""
svg deck = """<svg viewBox="0 0 100 124"><path d="M8 10 Q8 4 14 4 H64 L92 32 V114 Q92 120 86 120 H14 Q8 120 8 114 Z" fill="#FFFFFF" stroke="#D9680B" stroke-width="6" stroke-linejoin="round"/><path d="M64 4 V26 Q64 32 70 32 H92" fill="#FFE3C8" stroke="#D9680B" stroke-width="6" stroke-linejoin="round"/><rect x="20" y="44" width="60" height="38" rx="4" fill="#FFE3C8"/><g fill="#D9680B"><rect x="28" y="64" width="9" height="12" rx="1.5"/><rect x="41" y="56" width="9" height="20" rx="1.5"/><rect x="54" y="50" width="9" height="26" rx="1.5"/><rect x="20" y="92" width="52" height="7" rx="3.5" opacity=".85"/></g></svg>"""
svg globe = """<svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" fill="#FFFFFF" stroke="#0B8F80" stroke-width="6"/><ellipse cx="60" cy="60" rx="22" ry="52" fill="none" stroke="#0B8F80" stroke-width="5"/><path d="M10 60 H110 M18 34 H102 M18 86 H102" fill="none" stroke="#0B8F80" stroke-width="5"/></svg>"""
svg cloud = """<svg viewBox="0 0 220 140"><path d="M58 128 Q14 128 14 90 Q14 56 50 52 Q56 14 100 12 Q138 10 150 44 Q158 38 170 40 Q206 44 206 86 Q206 128 164 128 Z" fill="#E4ECFF" stroke="#2159E0" stroke-width="7" stroke-linejoin="round"/></svg>"""
svg cloud_w = """<svg viewBox="0 0 220 140"><path d="M58 128 Q14 128 14 90 Q14 56 50 52 Q56 14 100 12 Q138 10 150 44 Q158 38 170 40 Q206 44 206 86 Q206 128 164 128 Z" fill="#FFFFFF" stroke="#2159E0" stroke-width="7" stroke-linejoin="round"/></svg>"""
svg user = """<svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="54" fill="#EEE7FD" stroke="#6D3FD0" stroke-width="6"/><circle cx="60" cy="46" r="18" fill="#6D3FD0"/><path d="M26 96 Q32 70 60 70 Q88 70 94 96" fill="#6D3FD0"/></svg>"""
svg key = """<svg viewBox="0 0 120 60"><circle cx="30" cy="30" r="22" fill="#FFFFFF" stroke="#6D3FD0" stroke-width="7"/><circle cx="30" cy="30" r="7" fill="#6D3FD0"/><path d="M52 30 H112 M96 30 V46 M80 30 V42" fill="none" stroke="#6D3FD0" stroke-width="8" stroke-linecap="round"/></svg>"""
svg lock = """<svg viewBox="0 0 100 120"><path d="M26 54 V36 Q26 10 50 10 Q74 10 74 36 V54" fill="none" stroke="#6B7A90" stroke-width="9" stroke-linecap="round"/><rect x="10" y="50" width="80" height="62" rx="12" fill="#6B7A90"/><circle cx="50" cy="76" r="8" fill="#FFFFFF"/><rect x="46" y="78" width="8" height="18" rx="4" fill="#FFFFFF"/></svg>"""
svg check = """<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="#17894D"/><path d="M28 52 L44 67 L73 35" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>"""
svg usb = """<svg viewBox="0 0 80 150"><rect x="22" y="6" width="36" height="34" rx="4" fill="#FFFFFF" stroke="#6B7A90" stroke-width="6"/><rect x="31" y="16" width="6" height="8" fill="#6B7A90"/><rect x="43" y="16" width="6" height="8" fill="#6B7A90"/><rect x="10" y="40" width="60" height="104" rx="14" fill="#6B7A90"/><rect x="26" y="60" width="28" height="7" rx="3.5" fill="#FFFFFF" opacity=".6"/></svg>"""
svg folder = """<svg viewBox="0 0 140 110"><path d="M6 16 Q6 8 14 8 H52 L64 22 H126 Q134 22 134 30 V96 Q134 104 126 104 H14 Q6 104 6 96 Z" fill="#E4ECFF" stroke="#2159E0" stroke-width="6" stroke-linejoin="round"/><path d="M6 38 H134" stroke="#2159E0" stroke-width="5"/></svg>"""
svg folder_g = """<svg viewBox="0 0 140 110"><path d="M6 16 Q6 8 14 8 H52 L64 22 H126 Q134 22 134 30 V96 Q134 104 126 104 H14 Q6 104 6 96 Z" fill="#DDE3EC" stroke="#8C99AD" stroke-width="6" stroke-linejoin="round"/><path d="M6 38 H134" stroke="#8C99AD" stroke-width="5"/></svg>"""
svg train = """<svg viewBox="0 0 120 120"><rect x="18" y="8" width="84" height="88" rx="20" fill="#FFFFFF" stroke="#2159E0" stroke-width="7"/><rect x="30" y="22" width="60" height="30" rx="6" fill="#2159E0" opacity=".9"/><circle cx="40" cy="74" r="7" fill="#2159E0"/><circle cx="80" cy="74" r="7" fill="#2159E0"/><path d="M34 98 L22 114 M86 98 L98 114" stroke="#2159E0" stroke-width="7" stroke-linecap="round"/></svg>"""
svg office = """<svg viewBox="0 0 120 120"><rect x="22" y="10" width="76" height="102" rx="8" fill="#FFFFFF" stroke="#D9680B" stroke-width="7"/><g fill="#D9680B"><rect x="36" y="26" width="14" height="12" rx="2"/><rect x="70" y="26" width="14" height="12" rx="2"/><rect x="36" y="48" width="14" height="12" rx="2"/><rect x="70" y="48" width="14" height="12" rx="2"/><rect x="36" y="70" width="14" height="12" rx="2"/><rect x="70" y="70" width="14" height="12" rx="2"/><rect x="52" y="90" width="16" height="22" rx="2"/></g></svg>"""
svg sil_pc = """<svg viewBox="0 0 200 140"><rect x="28" y="8" width="144" height="96" rx="10" fill="none" stroke="#9AA8BD" stroke-width="5" stroke-dasharray="10 10"/><path d="M8 112 H192 L182 130 Q180 134 175 134 H25 Q20 134 18 130 Z" fill="none" stroke="#9AA8BD" stroke-width="5" stroke-dasharray="10 10"/><text x="100" y="78" text-anchor="middle" font-size="60" font-weight="900" fill="#9AA8BD" font-family="sans-serif">?</text></svg>"""
svg sil_sp = """<svg viewBox="0 0 100 170"><rect x="6" y="4" width="88" height="162" rx="16" fill="none" stroke="#9AA8BD" stroke-width="5" stroke-dasharray="10 10"/><text x="50" y="104" text-anchor="middle" font-size="56" font-weight="900" fill="#9AA8BD" font-family="sans-serif">?</text></svg>"""
svg qmark = """<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="46" fill="#9AA8BD"/><text x="50" y="70" text-anchor="middle" font-size="62" font-weight="900" fill="#FFFFFF" font-family="sans-serif">?</text></svg>"""
svg brace = """<svg viewBox="0 0 44 540"><path d="M6 6 Q30 6 30 40 L30 236 Q30 270 44 270 Q30 270 30 304 L30 500 Q30 534 6 534" fill="none" stroke="#D9680B" stroke-width="6" stroke-linecap="round"/></svg>"""
cue hop(x, cx, cy, vx, vy, d=1300, e=1280) = [>#x][!#x to,cx={cx},cy={cy},via=({vx},{vy}),duration={d},ease=power1.inOut][<#x +{e}]
cue net(w, o, d=300) = [!#w.hub to,opacity={o},duration={d}][!#w.hub_ring to,opacity={o},duration={d}][!#w.lb_net to,opacity={o},duration={d}]
cue wires(w, o, d=500) = [!#w.wb_pc to,opacity={o},duration={d}][!#w.wb_sp to,opacity={o},duration={d}][!#w.wb_sv to,opacity={o},duration={d}][!#w.wf_pc to,opacity={o},duration={d}][!#w.wf_sp to,opacity={o},duration={d}][!#w.wf_sv to,opacity={o},duration={d}][!#w.w_db to,opacity={o},duration={d}]
bgm#music(fade: 1200,2800) 明るく軽やかなエレクトロニカ、きらめくシンセのアルペジオと柔らかいビート、テクノロジーの解説動画向けの控えめで前向きな曲
# 字幕: 白い札 + 淡い縁 + 影・文ごとに 1 枚 (読点で 2 行に割る)・語の色は台詞の {b}{o}{t}{v}
subtitle.hug(bottom: 13px; font-family: m; font-size: 29px; line-height: 1.42; letter-spacing: .01em; color: $ink; text-align: center; background: #FFFFFFF7; border: 2px solid #E3E9F2; border-radius: 17px; padding: 11px 29px 12px 29px; box-shadow: 0px 8px 20px #17223A24; unit: sentence; lead: 80; tail: 550; hold: next,800; in: {y:7, opacity:0, duration:.18, ease:'power2.out'}; out: {opacity:0, duration:.14, ease:'power2.in'})

# 部品: 左上の章の見出し (番号の青い札が回って弾み → 題が左から → 下線が伸びる)・前の章の見出しは上へ抜ける
def hdr(n, t, w, nw=56, tl=72, ns=25) = div(left: 51px; top: 33px; width: 700px; height: 60px; background: none; z-index: front; out: {y:-17, opacity:0, duration:.35, ease:'power2.in'})
  div#nb(left: 0px; top: 0px; width: {nw}; height: 56px; border-radius: 15px; background: $blue; box-shadow: 0px 7px 15px #2159E047; in: {scale:.4, rotation:-12, duration:.55, ease:'back.out(2.2)'})
    p#n(cx: 50%; cy: 50%; font-family: e; font-size: {ns}; line-height: 1; letter-spacing: -.02em; color: #FFFFFF; content: {n})
  p#t(left: {tl}; top: 6px; font-size: 36px; line-height: 1.1; letter-spacing: -.02em; delay: 80; in: {x:-23, opacity:0, duration:.55, ease:'power3.out'}; content: {t})
  div#r(left: {tl}; top: 52px; width: {w}; height: 5px; border-radius: 3px; background: $blue; delay: 200; in: {scaleX:0, pivot:'left', duration:.7, ease:'power3.inOut'})
# 色の丸札 (図の区画の名) と、白い丸札 (図の中の名)・色の小札 (状態の語)
def chip(t, c) = p(font-family: m; font-size: 20px; line-height: 1; color: #FFFFFF; background: {c}; border-radius: 99px; padding: 9px 16px; in: pin6; content: {t})
def lbl(t, c) = p(font-family: m; font-size: 21px; line-height: 1.4; color: {c}; background: #FFFFFF; border-radius: 9px; padding: 4px 12px; box-shadow: 0px 4px 11px #17223A1A; in: up; content: {t})
def pill(t, c) = p(font-size: 19px; line-height: 1.1; color: #FFFFFF; background: {c}; border-radius: 99px; padding: 6px 13px; in: pin5; content: {t})
# POINT の注記 (白い板 + 黒い小札 + 太字の語)
def note(t) = p(font-family: m; font-size: 20px; line-height: 1.45; color: $ink2; background: #FFFFFF; border-radius: 13px; padding: 12px 17px 12px 92px; box-shadow: 0px 9px 23px #17223A24; in: up; content: {t})
  p#tag(left: 17px; cy: 50%; font-family: e; font-size: 15px; line-height: 1.1; letter-spacing: .06em; color: #FFFFFF; background: $ink2; border-radius: 5px; padding: 1px 7px) POINT
# 区画の板 (白 + 色の縁 + 柔らかい影)
def zone(c) = div(border-radius: 20px; background: #FFFFFFEB; border: 3px solid {c}; box-shadow: 0px 12px 27px #17223A14; in: boxin)
# 保存先の行 (フォルダ + 名)
def frow(t, ic, c, bg) = div(left: 753px; width: 420px; height: 88px; border-radius: 16px; background: {bg}; box-shadow: 0px 7px 17px #17223A1A; in: {y:17, opacity:0, duration:.5, ease:'power3.out', stagger:{each:.12}})
  svg#i(left: 20px; cy: 50%; width: 61px; height: 48px; part: {ic})
  p#t(left: 98px; cy: 50%; font-family: m; font-size: 24px; color: {c}; content: {t})
# 図の全体 (1 枚の図を 3 つの章で使う: 手元の端末 / ネットワーク / サービス側)。子は全部 in なし — 最初の章は子ごとに印のやり方で出し、後の章は群ごと溶けて出る
def world = div(left: 0px; top: 0px; width: 1280px; height: 720px; background: none; in: none)
  div#zone_dev(left: 60px; top: 131px; width: 347px; height: 448px; border-radius: 20px; background: #FFFFFFEB; border: 3px solid $orange_m; box-shadow: 0px 12px 27px #17223A14; in: none)
  div#zone_svc(left: 873px; top: 131px; width: 347px; height: 448px; border-radius: 20px; background: #FFFFFFEB; border: 3px solid $blue_m; box-shadow: 0px 12px 27px #17223A14; in: none)
  p#chip_dev(left: 84px; top: 112px; font-family: m; font-size: 20px; line-height: 1; color: #FFFFFF; background: $orange; border-radius: 99px; padding: 9px 16px; in: none) 手元の端末
  p#chip_svc(left: 897px; top: 112px; font-family: m; font-size: 20px; line-height: 1; color: #FFFFFF; background: $blue; border-radius: 99px; padding: 9px 16px; in: none) サービス側
  # 配線: 太い淡色の下地 + 流れ続ける破線 (dash_offset の鋸波 = hf の strokeDashoffset)
  shape#wb_pc(path: "M341 273 C467 273 480 355 593 355"; background: none; border: 15px solid $wire; in: none)
  shape#wb_sp(path: "M280 470 C453 470 480 355 593 355"; background: none; border: 15px solid $wire; in: none)
  shape#wb_sv(path: "M687 355 C833 355 847 245 985 245"; background: none; border: 15px solid $wire; in: none)
  shape#wf_pc(path: "M341 273 C467 273 480 355 593 355"; background: none; border: 4px solid $teal; dash: 2,11; in: none; main: sawtooth {dash_offset: 1, period: 0.36})
  shape#wf_sp(path: "M280 470 C453 470 480 355 593 355"; background: none; border: 4px solid $teal; dash: 2,11; in: none; main: sawtooth {dash_offset: 1, period: 0.36})
  shape#wf_sv(path: "M687 355 C833 355 847 245 985 245"; background: none; border: 4px solid $teal; dash: 2,11; in: none; main: sawtooth {dash_offset: 1, period: 0.36})
  shape#w_db(path: "M1047 324 L1047 396"; background: none; border: 5px solid $blue; in: none)
  svg#pc(left: 133px; top: 203px; width: 200px; height: 140px; part: laptop; in: none)
  svg#sp(left: 196px; top: 407px; width: 75px; height: 127px; part: phone; in: none)
  p#lb_pc(cx: 233px; top: 351px; font-family: m; font-size: 21px; line-height: 1.4; color: $orange_d; background: #FFFFFF; border-radius: 9px; padding: 4px 12px; box-shadow: 0px 4px 11px #17223A1A; in: none) パソコン
  p#lb_sp(cx: 233px; top: 540px; font-family: m; font-size: 21px; line-height: 1.4; color: $orange_d; background: #FFFFFF; border-radius: 9px; padding: 4px 12px; box-shadow: 0px 4px 11px #17223A1A; in: none) スマートフォン
  div#hub_ring(left: 581px; top: 296px; width: 117px; height: 117px; border-radius: 999px; background: none; border: 3px solid $teal_m; in: none)
  svg#hub(left: 595px; top: 309px; width: 91px; height: 91px; part: globe; in: none)
  p#lb_net(cx: 640px; top: 409px; font-family: m; font-size: 21px; line-height: 1.4; color: $teal; background: #FFFFFF; border-radius: 9px; padding: 4px 12px; box-shadow: 0px 4px 11px #17223A1A; in: none) ネットワーク
  # サーバーのランプはゆっくり点滅し続ける (opacity の正弦波)
  svg#srv(left: 990px; top: 175px; width: 113px; height: 142px; part: server; in: none)
    div#led(left: 76px; top: "27;66;105"; width: 9px; height: 9px; border-radius: 99px; background: #8BF5B5; box-shadow: 0px 0px 7px 2px #22C55EBF; opacity: .575; main: sine {opacity: 0.425, period: 1.1}) ×3
  p#lb_srv(cx: 1047px; top: 323px; font-family: m; font-size: 21px; line-height: 1.4; color: $blue_d; background: #FFFFFF; border-radius: 9px; padding: 4px 12px; box-shadow: 0px 4px 11px #17223A1A; overlap: .w_db; in: none) サーバー
  svg#db(left: 990px; top: 401px; width: 113px; height: 121px; part: storage; in: none)
  p#lb_db(cx: 1047px; top: 533px; font-family: m; font-size: 21px; line-height: 1.4; color: $blue_d; background: #FFFFFF; border-radius: 9px; padding: 4px 12px; box-shadow: 0px 4px 11px #17223A1A; in: none) 保存先
  svg#f1(left: 1000px; top: 451px; width: 29px; height: 37px; part: file; in: none)
  svg#f2(left: 1032px; top: 445px; width: 29px; height: 37px; part: file; in: none)

# 全編の地: 紙色に点の格子 (左上へゆっくり流れる) と 3 つの色の光 (ゆっくり呼吸する)
div#dots(left: -40px; top: -40px; width: 1360px; height: 800px; background: none; pattern: dots,27,#C9D4E5; opacity: .55; bleed; z-index: back; in: none; out: none; main: ramp {x: -27, y: -27, period: '102.4s'})
div#glow1(left: 733px; top: -347px; width: 733px; height: 733px; border-radius: 999px; background: radial(#2159E029,#2159E000@68%); z-index: back; in: none; out: none; main: sine {scale: 0.06, period: '51.2s'})
div#glow2(left: -280px; top: 280px; width: 667px; height: 667px; border-radius: 999px; background: radial(#D9680B1F,#D9680B00@68%); z-index: back; in: none; out: none; main: sine {scale: 0.06, period: '68s'})
div#glow3(left: 373px; top: 120px; width: 533px; height: 533px; border-radius: 999px; background: radial(#0B8F8014,#0B8F8000@70%); z-index: back; in: none; out: none; main: sine {x: 40, period: '102.4s'})

# title — 開幕: 白い大きな板に「図解でわかる」→ 2 行の題 → 下線 → 副題、右の円の中に雲・保存先・端末が順に弾んで乗り、全体が少し浮く
section#title(stagger: {each: 0})
group#ti(left: 0px; top: 0px; width: 1280px; height: 720px; out: {opacity:0, scale:1.04, duration:.5, ease:'power2.in'})
  div#card(left: 153px; top: 140px; width: 973px; height: 413px; border-radius: 29px; background: #FFFFFF; border: 3px solid $card_line; box-shadow: 0px 20px 47px #17223A1F; delay: 100; in: {scale:.94, opacity:0, duration:.7, ease:'power3.out'})
  group#art(left: 824px; top: 204px; width: 280px; height: 280px)
    div#disc(left: 7px; top: 7px; width: 267px; height: 267px; border-radius: 999px; background: $blue_l; in: none)
    svg#cloud(left: 27px; top: 40px; width: 227px; height: 144px; part: cloud_w; delay: 450; in: {scale:.7, opacity:0, duration:.7, ease:'back.out(1.9)'})
    svg#db(left: 107px; top: 85px; width: 67px; height: 71px; part: storage; delay: 800; in: pin4)
    shape#l1(path: "M80 215 C87 193 107 187 120 180"; background: none; border: 4px solid $teal; dash: 2,9; in: none)
    shape#l2(path: "M212 212 C200 195 180 188 164 180"; background: none; border: 4px solid $teal; dash: 2,9; in: none)
    svg#pc(left: 16px; top: 200px; width: 113px; height: 79px; part: laptop; delay: 1050; in: pin4)
    svg#sp(left: 197px; top: 193px; width: 49px; height: 84px; part: phone; delay: 1200; in: pin4)
  div#kicker(left: 220px; top: 212px; width: 220px; height: 37px; background: none; delay: 350; in: {x:-20, opacity:0, duration:.55, ease:'power3.out'})
    div#bar(left: 0px; cy: 50%; width: 8px; height: 28px; border-radius: 4px; background: $orange)
    p#t(left: 17px; cy: 50%; font-family: m; font-size: 23px; letter-spacing: .08em; color: $mute) 図解でわかる
  p#main(left: 216px; top: 257px; font-size: 67px; line-height: 1.14; letter-spacing: -.03em; delay: 500; in: {y:27, opacity:0, duration:.7, ease:'power3.out'}) クラウドストレージ[br]{b}の仕組み{/}
  div#rule(left: 220px; top: 424px; width: 467px; height: 5px; border-radius: 3px; background: $blue; delay: 900; in: {scaleX:0, pivot:'left', duration:.8, ease:'power3.inOut'})
  p#sub(left: 220px; top: 445px; font-family: m; font-size: 27px; color: $ink2; delay: 1050; in: {y:13, opacity:0, duration:.5, ease:'power3.out'}) 保存先と端末を分けて考える

# ch1 — 01 クラウドストレージとは: サービス側に寄った図 (群の変種 .tight) にサーバー → 飛んでくるファイル → 保存先 → POINT の注記、「どこから」で引いて手元の「？」を見せる
section#ch1(stagger: {each: 0})
hdr#h1(n: "01"; t: "クラウドストレージとは"; w: 388)
# 右上のシリーズ表記と章の進行 7 本 (sticky・章ごとに 1 本ずつ左から埋まる)
div#brand.sticky(left: 963px; top: 39px; width: 264px; height: 36px; background: none; z-index: front; in: {y:-11, opacity:0, duration:.5, ease:'power3.out'}; out: {opacity:0, duration:.6})
  svg#ic(left: -6px; top: 0px; width: 31px; height: 20px; part: cloud)
  p#t(left: 32px; top: -1px; width: 232px; font-family: m; font-size: 17px; letter-spacing: .02em; color: $ink2; text-align: right; white-space: nowrap) クラウドストレージの仕組み
  div#pg(left: "45;77;109;141;173;205;237"; top: 30px; width: 27px; height: 6px; border-radius: 3px; background: $track) ×7
    div#b(left: 0px; top: 0px; width: 100%; height: 6px; border-radius: 3px; background: $blue; in: {scaleX:0, pivot:'left', duration:.6, ease:'power2.inOut'})
# 図 (sticky で ch2 まで続く)・サービス側へ寄せた変種 .tight で出し、語で to,x=285 を 1.4 秒かけて引きの姿へ (hf の #world の scale / x)
world#w1.sticky(out: {opacity:0, scale:.97, duration:.45, ease:'power2.in'})
  svg#sil_pc(left: 133px; top: 203px; width: 200px; height: 140px; part: sil_pc; in: {y:12, opacity:0, duration:.5, ease:'power3.out'})
  svg#sil_sp(left: 196px; top: 407px; width: 75px; height: 127px; part: sil_sp; in: {y:12, opacity:0, duration:.5, ease:'power3.out'})
  svg#brace(left: 419px; top: 193px; width: 29px; height: 360px; part: brace; in: {scaleY:0, duration:.6, ease:'power2.out'})
  div#nt_dev3(left: 460px; top: 333px; width: 300px; height: 80px; background: none; in: {x:-16, opacity:0, duration:.55, ease:'power3.out'})
    p#s(left: 0px; top: 4px; font-family: m; font-size: 17px; color: $mute) パソコンやスマートフォンなど
    p#t(left: 0px; top: 31px; font-size: 29px; color: $orange_d) ファイルを使う端末
  pill#pl_acc(left: "404;373;767"; top: "253;416;251"; t: "アクセス"; c: $teal) ×3
  pill#pl_save(left: 417px; top: 249px; t: "保存"; c: $blue)
  pill#pl_open(left: 399px; top: 419px; t: "開く"; c: $orange)
  div#ring_a(left: 970px; top: 392px; width: 153px; height: 137px; border-radius: 27px; background: none; border: 3px solid $blue; z-index: front; in: {scale:.85, opacity:0, duration:.45, ease:'back.out(2)'}; out: {opacity:0, duration:.5})
  div#ring_b(left: 970px; top: 392px; width: 153px; height: 137px; border-radius: 27px; background: none; border: 3px solid $blue; z-index: front; in: {scale:.85, opacity:0, duration:.45, ease:'back.out(2)'}; out: {opacity:0, duration:.4})
  lbl#lb_same(cx: 1047px; top: 533px; t: "同じ保存先"; c: $blue_d; in: pin7)
  svg#pc_doc(left: 212px; top: 219px; width: 43px; height: 53px; part: file; in: pin3)
  svg#sp_doc(left: 216px; top: 440px; width: 35px; height: 43px; part: file; in: pin3)
  svg#sp_ok(left: 253px; top: 413px; width: 36px; height: 36px; part: check; in: pin3)
  # 飛ぶファイルとパケット (静止の位置 = 出発点・to の cx cy = 着く点・via = 経由点 (ハブ))
  svg#mv_in(left: 376px; top: 171px; width: 47px; height: 58px; part: file; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)
  svg#mv_drop1(left: 1033px; top: 227px; width: 29px; height: 36px; part: file; in: {scale:.86, duration:.25, ease:'power2.out'}; out: gone)
  svg#mv_save(left: 290px; top: 238px; width: 47px; height: 58px; part: file; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)
  svg#mv_drop2(left: 1033px; top: 227px; width: 29px; height: 36px; part: file; in: {scale:.86, duration:.25, ease:'power2.out'}; out: gone)
  svg#mv_open(left: 1030px; top: 440px; width: 33px; height: 41px; part: file; in: {scale:.75, duration:.25, ease:'power2.out'}; out: {scale:.5, opacity:0, duration:.2})
  div#pk(left: "334;273;334;273"; top: "266;463;266;463"; width: 15px; height: 15px; border-radius: 99px; background: $teal; box-shadow: 0px 0px 0px 4px #0B8F802E; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone) ×4
  note#nt_1(left: 427px; top: 499px) ファイルの保存先 ＝ {bd}サービス側のサーバー{/}
  shape#ld_1(path: "M841 527 L920 527 L980 480"; background: none; border: 3px solid $ink2; in: draw {duration: 0.45, ease: 'power2.inOut'})
  div#ld_dot(left: 974px; top: 474px; width: 12px; height: 12px; border-radius: 99px; background: $ink2; in: fade {duration: 0.2})
  note#nt_5(left: 445px; top: 495px) 保存先が同じなら{bd}別の端末からも開ける{/}
  p#q_bubble(left: 413px; top: 195px; width: 453px; font-size: 47px; text-align: center; background: #FFFFFF; border: 3px solid $ink; border-radius: 99px; padding: 20px 0px; box-shadow: 0px 12px 27px #17223A24; in: pin7; out: {scale:.9, opacity:0, duration:.35, ease:'power2.in'}) どこから開ける？
#w1.tight(left: -285px; top: 0px)

# ch2 — 02 端末から保存先へアクセス: 手元の区画に端末 → 括弧と説明 → ネットワークの配線 → アクセスのパケット → 同じ保存先へ保存して別の端末で開く
section#ch2(stagger: {each: 0})
hdr#h2(n: "02"; t: "端末から保存先へアクセス"; w: 423)

# ch3 — 03 使い方の例: 左に「パソコンで用意」の板 (挿絵 + 端末 + 研修資料)・中央の雲へ弧の矢印・右に「移動先で確認」の板
section#ch3(stagger: {each: 0})
hdr#h3(n: "03"; t: "使い方の例"; w: 176)
group#ex_l(left: 60px; top: 131px; width: 427px; height: 448px; in: {x:-40, opacity:0, duration:.6, ease:'power3.out'})
  zone#zone(left: 0px; top: 0px; width: 427px; height: 448px; c: $orange_m; in: none)
  chip#chip(left: 24px; top: -19px; t: "パソコンで用意"; c: $orange; padding: 9px 16px 9px 50px; in: none)
    svg#i(left: 15px; cy: 50%; width: 27px; height: 27px; part: office)
  img#img(left: 17px; top: 32px; width: 392px; height: 220px; border-radius: 15px; fit: cover) [ref:@worker]明るいオフィスの整った机でノートパソコンに向かい、研修用のスライド資料を作っている。画面には四角と小さな棒グラフの形だけ (文字なし)。鉢植えの観葉植物と窓の街並み。横長の構図で人物は中央
  svg#pc(left: 47px; top: 280px; width: 200px; height: 140px; part: laptop; in: pin6)
  svg#deck(left: 273px; top: 269px; width: 80px; height: 99px; part: deck; in: pin3)
  lbl#decklb(cx: 313px; top: 377px; t: "研修資料"; c: $orange_d)
group#ex_r(left: 793px; top: 131px; width: 427px; height: 448px; in: {x:40, opacity:0, duration:.6, ease:'power3.out'})
  zone#zone(left: 0px; top: 0px; width: 427px; height: 448px; c: $blue_m; in: none)
  chip#chip(left: 24px; top: -19px; t: "移動先で確認"; c: $blue; padding: 9px 16px 9px 50px; in: none)
    svg#i(left: 15px; cy: 50%; width: 27px; height: 27px; part: train)
  img#img(left: 17px; top: 32px; width: 392px; height: 220px; border-radius: 15px; fit: cover) [ref:@worker]通勤電車の中でつり革を持って立ち、スマートフォンで同じスライド資料 (四角と小さな棒グラフの形だけ・文字なし) を確認している。窓の外に柔らかい街の景色。横長の構図で人物は中央
  svg#sp(left: 80px; top: 267px; width: 88px; height: 149px; part: phone; in: pin6)
  svg#spdeck(left: 100px; top: 299px; width: 48px; height: 59px; part: deck; in: pin3)
  svg#ok(left: 152px; top: 261px; width: 41px; height: 41px; part: check; in: pin3)
  p#rlb(left: 187px; top: 301px; font-size: 21px; line-height: 1.42; in: {y:11, opacity:0, duration:.5, ease:'power3.out'}) 同じ研修資料を[br]{b}スマートフォンで確認{/}
# 雲 (保存先) と弧の矢印 (線を描いてから矢じり)
shape#ex_a1(path: "M360 313 C427 220 480 220 539 276"; background: none; border: 5px solid $blue; in: draw {duration: 0.6, ease: 'power2.inOut'})
shape#ex_a1h(points: "524,275 545,281 537,261"; background: $blue; in: fade {duration: 0.08})
shape#ex_a2(path: "M741 276 C800 220 847 220 908 301"; background: none; border: 5px solid $blue; in: draw {duration: 0.6, ease: 'power2.inOut'})
shape#ex_a2h(points: "893,298 913,307 909,286"; background: $blue; in: fade {duration: 0.08})
group#ex_cloud(left: 527px; top: 253px; width: 227px; height: 200px; in: {scale:.6, opacity:0, duration:.5, ease:'back.out(1.9)'})
  svg#c(left: 7px; top: 0px; width: 213px; height: 136px; part: cloud)
  svg#s(left: 83px; top: 44px; width: 60px; height: 64px; part: storage_w)
  lbl#l(cx: 113px; top: 143px; t: "クラウドストレージ"; c: $blue_d; in: none)
svg#ex_mv1(left: 342px; top: 290px; width: 37px; height: 47px; part: deck; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)
svg#ex_mv2(left: 723px; top: 253px; width: 37px; height: 47px; part: deck; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)

# ch4 — 04 使う端末と保存場所: 図が戻り、区画が語で光って「端末」と「場所」の札 →「≠ 同じとは限らない」→ 保管・要求・渡すの矢印 → 用語の札「サーバー」
section#ch4(stagger: {each: 0})
hdr#h4(n: "04"; t: "使う端末と保存場所"; w: 318)
world#w4(in: {opacity:0, duration:.45, ease:'power2.out'}; out: {opacity:0, duration:.4, ease:'power2.in'})
  pill#nt_dev(left: 427px; top: 469px; t: "◀ ファイルを使う端末"; c: $orange; font-size: 21px; padding: 8px 17px; in: {x:20, opacity:0, duration:.55, ease:'power3.out'})
  pill#nt_svc(left: 491px; top: 523px; t: "ファイルが保存されている場所 ▶"; c: $blue; font-size: 21px; padding: 8px 17px; in: {x:-20, opacity:0, duration:.55, ease:'power3.out'})
  p#neq(left: 440px; top: 179px; width: 400px; font-size: 33px; text-align: center; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 14px 0px; box-shadow: 0px 12px 27px #17223A38; in: pin6) {ne}≠{/} 同じとは限らない
  pill#pl_keep(left: 891px; top: 427px; t: "保管"; c: $blue)
  svg#f3(left: 1064px; top: 451px; width: 29px; height: 37px; part: file; in: pin3)
  shape#ar_req(path: "M287 440 C427 440 460 316 593 316 L687 316 C813 316 827 212 980 212"; background: none; border: 5px solid $orange; in: draw {duration: 0.9, ease: 'power2.inOut'})
  shape#ar_req_h(points: "968,202 988,212 968,222"; background: $orange; in: fade {duration: 0.08})
  shape#ar_res(path: "M980 279 C853 279 840 393 687 393 L593 393 C480 393 460 500 287 500"; background: none; border: 5px solid $blue; in: draw {duration: 0.9, ease: 'power2.inOut'})
  shape#ar_res_h(points: "299,490 279,500 299,510"; background: $blue; in: fade {duration: 0.08})
  pill#lb_req(left: 707px; top: 261px; t: "① 要求"; c: $orange)
  pill#lb_res(left: 727px; top: 404px; t: "② 渡す"; c: $blue)
  pill#mv_req(left: 255px; top: 424px; t: "要求"; c: $orange; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)
  svg#mv_res(left: 959px; top: 253px; width: 41px; height: 51px; part: file; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)
  svg#sp_doc(left: 216px; top: 440px; width: 35px; height: 43px; part: file; in: pin3)
  svg#sp_ok(left: 253px; top: 413px; width: 36px; height: 36px; part: check; in: pin3)
# 用語の札: 図を消して淡い幕の上に白い大きな札 (左に絵の枠・右に「用語」「サーバー」と定義を 1 行ずつ・右端に保管 / 渡すの小札)
div#tm_veil(inset: 0; background: #F2F5FAC7; in: {opacity:0, duration:.45, ease:'power2.out'})
div#tm(left: 153px; top: 133px; width: 973px; height: 427px; border-radius: 27px; background: #FFFFFF; border: 3px solid $card_line; box-shadow: 0px 20px 47px #17223A2E; in: {scale:.9, y:20, opacity:0, duration:.6, ease:'back.out(1.4)'})
  div#art(left: 47px; top: 60px; width: 280px; height: 307px; border-radius: 23px; background: $blue_l; in: {scale:.8, opacity:0, duration:.5, ease:'power3.out'})
    svg#srv(left: 73px; top: 47px; width: 133px; height: 167px; part: server; in: pin6)
    p#l(cx: 140px; top: 233px; font-size: 23px; color: $blue_d) コンピューター
  p#tag(left: 373px; top: 56px; font-size: 19px; line-height: 1.1; letter-spacing: .08em; color: #FFFFFF; background: $ink; border-radius: 8px; padding: 6px 13px; in: pin5) 用語
  p#word(left: 371px; top: 92px; font-size: 75px; line-height: 1.15; letter-spacing: -.02em; color: $blue; in: {x:-20, opacity:0, duration:.55, ease:'power3.out'}) サーバー
  p#d1(left: 373px; top: 193px; font-family: m; font-size: 28px; line-height: 1.55; color: $ink2; in: {y:11, opacity:0, duration:.5, ease:'power3.out'}) データを{kb}保管{/}したり、
  p#d2(left: 373px; top: 236px; font-family: m; font-size: 28px; line-height: 1.55; color: $ink2; in: {y:11, opacity:0, duration:.5, ease:'power3.out'}) 求められたデータを{ko}渡{/}したりする
  p#d3(left: 373px; top: 280px; font-size: 28px; line-height: 1.55; in: {y:11, opacity:0, duration:.5, ease:'power3.out'}) コンピューター
  div#uline(left: 373px; top: 324px; width: 200px; height: 5px; border-radius: 3px; background: $blue; in: {scaleX:0, pivot:'left', duration:.6, ease:'power3.inOut'})
  div#r1(left: 813px; top: 201px; width: 133px; height: 56px; border-radius: 15px; background: $blue_l; in: pin5)
    svg#i(left: 27px; cy: 50%; width: 29px; height: 31px; part: storage)
    p#t(left: 64px; cy: 50%; font-size: 21px; color: $blue_d) 保管
  div#r2(left: 813px; top: 267px; width: 133px; height: 56px; border-radius: 15px; background: $orange_l; in: pin5)
    svg#i(left: 27px; cy: 50%; width: 29px; height: 37px; part: file_o)
    p#t(left: 64px; cy: 50%; font-size: 21px; color: $orange_d) 渡す

# ch5 — 05 端末だけに保存した場合: 中央の板に端末とファイル → 別の端末へ USB で移す → 準備が必要、板が左へ寄って薄まり、右にクラウドストレージの板
section#ch5(stagger: {each: 0})
hdr#h5(n: "05"; t: "端末だけに保存した場合"; w: 388)
# 左の板は最初は画面の中央 (変種 .mid で 297px 右に出し、語で .home へ寄せて薄める)
div#cl(left: 60px; top: 112px; width: 567px; height: 467px; background: none; in: none)
  zone#card(left: 0px; top: 19px; width: 567px; height: 448px; c: $orange_m; in: {scale:.94, opacity:0, duration:.6, ease:'power3.out'})
  chip#chip(left: 24px; top: 0px; t: "端末の中だけに保存"; c: $orange)
  shape#mv(path: "M220 201 C287 108 367 108 421 164"; background: none; border: 5px solid $gray; in: draw {duration: 0.7, ease: 'power2.inOut'})
  shape#mvh(points: "408,163 426,169 420,151"; background: $gray; in: fade {duration: 0.08})
  # 端末の組 (hf の #grp-clpc = 左の板の中の層: 板の中のさらに右に出し、語で板の中の左 .l へ寄る。板が .home へ寄れば一緒に寄って薄まる)
  div#clpc(left: 167px; top: 201px; width: 220px; height: 215px; background: none; in: none)
    svg#pc(left: 0px; top: 0px; width: 220px; height: 154px; part: laptop; in: pin6)
    svg#f(left: 85px; top: 26px; width: 48px; height: 60px; part: file_o; in: {y:-53, scale:.6, opacity:0, duration:.55, ease:'back.out(1.6)'})
    p#tag(cx: 110px; top: 174px; font-size: 20px; color: $orange_d; background: $orange_l; border: 2px solid $orange_m; border-radius: 11px; padding: 7px 15px; in: pin6) 保存先 ＝ その端末
  svg#sp(left: 407px; top: 175px; width: 87px; height: 147px; part: phone_g; in: pin6)
  svg#spq(left: 429px; top: 221px; width: 41px; height: 41px; part: qmark; in: pin3)
  lbl#lbsp(cx: 450px; top: 333px; t: "別の端末"; c: $mute)
  svg#usb(left: 204px; top: 171px; width: 32px; height: 60px; part: usb; in: {scale:.6, duration:.25, ease:'power2.out'}; out: gone)
  pill#mvlbl(left: 253px; top: 76px; t: "ファイルを移す"; c: #FFFFFF; color: $ink; box-shadow: 0px 5px 13px #17223A24; in: pin6)
  p#warn(left: 313px; top: 395px; font-size: 21px; color: $red; background: $red_l; border: 2px solid $red_m; border-radius: 99px; padding: 11px 0px; width: 170px; text-align: center; white-space: nowrap; in: pin6) ⚠ 準備が必要
# hf の作り: 左の板 (端末の組ごと) は .home へ寄せてから右の板が出る
#cl.mid(left: 357px; top: 112px)
#cl.home(left: 60px; top: 112px; opacity: .55; move: 800,power3.inOut)
#cl.clpc.l(left: 40px; top: 201px; move: 700,power3.inOut)
zone#cr_card(left: 653px; top: 131px; width: 567px; height: 448px; c: $blue_m; in: {scale:.94, opacity:0, duration:.6, ease:'power3.out'})
chip#cr_chip(left: 677px; top: 112px; t: "クラウドストレージ"; c: $blue)
shape#cr_wb1(path: "M937 303 C937 360 800 347 800 407"; background: none; border: 13px solid $wire; in: draw {duration: 0.7, ease: 'power2.inOut'})
shape#cr_wb2(path: "M937 303 C937 360 1093 347 1093 397"; background: none; border: 13px solid $wire; in: draw {duration: 0.7, ease: 'power2.inOut'})
shape#cr_w1(path: "M937 303 C937 360 800 347 800 407"; background: none; border: 4px solid $teal; dash: 2,11; in: fade {duration: 0.4}; main: sawtooth {dash_offset: 1, period: 0.36})
shape#cr_w2(path: "M937 303 C937 360 1093 347 1093 397"; background: none; border: 4px solid $teal; dash: 2,11; in: fade {duration: 0.4}; main: sawtooth {dash_offset: 1, period: 0.36})
svg#cr_cloud(left: 830px; top: 167px; width: 213px; height: 136px; part: cloud; in: pin6)
svg#cr_db(left: 907px; top: 213px; width: 60px; height: 64px; part: storage_w; in: pin4)
pill#cr_same(left: 1040px; top: 195px; t: "同じ保存先"; c: $blue; in: pin6)
pill#cr_net(left: 887px; top: 347px; t: "ネットワーク"; c: $teal; in: pin6)
svg#cr_pc(left: 707px; top: 412px; width: 187px; height: 131px; part: laptop; in: pin6)
svg#cr_sp(left: 1057px; top: 403px; width: 72px; height: 123px; part: phone; in: pin6)
div#cr_pk(left: "793;1086"; top: "400;390"; width: 15px; height: 15px; border-radius: 99px; background: $teal; box-shadow: 0px 0px 0px 4px #0B8F802E; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone) ×2

# ch6 — 06 開ける範囲を決めるもの: 右に保存先のファイル 3 行 → 点線の「開ける範囲」→ 左にアカウント → 矢印で鍵 (アクセス権限) → 範囲の 2 行に ✓・外の 1 行に錠
section#ch6(stagger: {each: 0})
hdr#h6(n: "06"; t: "開ける範囲を決めるもの"; w: 388)
shape#ac_l1(path: "M349 347 L419 347"; background: none; border: 5px solid $violet; in: draw {duration: 0.4, ease: 'power2.inOut'})
shape#ac_l1h(points: "409,339 426,347 409,355"; background: $violet; in: fade {duration: 0.08})
shape#ac_l2(path: "M623 347 L699 347"; background: none; border: 5px solid $violet; in: draw {duration: 0.4, ease: 'power2.inOut'})
shape#ac_l2h(points: "689,339 706,347 689,355"; background: $violet; in: fade {duration: 0.08})
zone#ac_card(left: 67px; top: 173px; width: 280px; height: 347px; c: $violet_m; in: {scale:.9, opacity:0, duration:.5, ease:'power3.out'})
svg#ac_user(left: 143px; top: 213px; width: 127px; height: 127px; part: user; in: pin5)
chip#ac_lb(cx: 207px; top: 360px; t: "アカウント"; c: $violet)
div#ac_id(left: 100px; top: 420px; width: 213px; height: 64px; border-radius: 13px; background: $violet_l; in: up)
  div#dot(left: 44px; cy: 50%; width: 29px; height: 29px; border-radius: 99px; background: $violet)
  p#t(left: 82px; cy: 50%; font-family: m; font-size: 20px; color: $violet) 利用者のID
div#ac_kbox(left: 427px; top: 233px; width: 193px; height: 227px; border-radius: 20px; background: #FFFFFF; border: 3px solid $violet_m; box-shadow: 0px 12px 27px #17223A1A; in: {scale:.9, opacity:0, duration:.5, ease:'power3.out'})
svg#ac_key(left: 450px; top: 280px; width: 147px; height: 73px; part: key; in: {rotation:-40, scale:.5, opacity:0, duration:.6, ease:'back.out(1.8)'})
chip#ac_kl(cx: 523px; top: 387px; t: "アクセス権限"; c: $violet)
zone#ac_st(left: 707px; top: 131px; width: 513px; height: 448px; c: $blue_m; in: {scale:.94, opacity:0, duration:.6, ease:'power3.out'})
chip#ac_stc(left: 731px; top: 112px; t: "保存先のファイル"; c: $blue)
shape#ac_range(left: 733px; top: 165px; width: 460px; height: 237px; path: rect,r=0.08; background: #6D3FD00D; border: 4px solid $violet; dash: 9,6; in: {scale:.9, opacity:0, duration:.5, ease:'power3.out'})
pill#ac_rlb(left: 1040px; top: 149px; t: "開ける範囲"; c: $violet)
frow#ac_r(top: "188;292;440"; t: "自分のファイル;共有された資料;他の人のファイル"; ic: "folder;folder;folder_g"; c: "$ink;$ink;$mute"; bg: "#FFFFFF;#FFFFFF;$off") ×3
svg#ac_ok1(left: 1112px; top: 209px; width: 45px; height: 45px; part: check; in: pin3)
svg#ac_ok2(left: 1112px; top: 313px; width: 45px; height: 45px; part: check; in: pin3)
svg#ac_lock(left: 1115px; top: 457px; width: 40px; height: 48px; part: lock; in: pin3)

# sum — まとめ: 図に戻り、配線を薄めて 2 つの区画を語で光らせ札を言い換える → 点線で分けて区画を左右へ → 戻して 2 つの端末へファイルが届き「端末が変わっても 保存先は同じ」
section#sum(stagger: {each: 0})
hdr#h7(n: "まとめ"; t: "保存先と端末を分けて考える"; w: 459; nw: 94; tl: 110; ns: 21; out: {opacity:0, duration:.6})
world#w8(in: {opacity:0, duration:.5, ease:'power2.out'}; out: {opacity:0, duration:1, ease:'power2.in'})
  shape#divider(path: "M640 143 L640 573"; background: none; border: 4px solid $ink2; in: draw {duration: 0.8, ease: 'power2.inOut'})
  chip#sm_dev(left: 84px; top: 112px; t: "アクセスする端末"; c: $orange)
  chip#sm_svc(left: 897px; top: 112px; t: "ファイルの保存先"; c: $blue)
  p#sep(left: 507px; top: 160px; width: 267px; font-size: 29px; text-align: center; color: #FFFFFF; background: $ink; border-radius: 99px; padding: 16px 0px; in: pin6) 分けて考える
  svg#pc_doc(left: 212px; top: 219px; width: 43px; height: 53px; part: file; in: pin3)
  svg#pc_ok(left: 308px; top: 200px; width: 36px; height: 36px; part: check; in: pin3)
  svg#sp_doc(left: 216px; top: 440px; width: 35px; height: 43px; part: file; in: pin3)
  svg#sp_ok(left: 253px; top: 413px; width: 36px; height: 36px; part: check; in: pin3)
  svg#mv_a(left: 1024px; top: 216px; width: 47px; height: 58px; part: file; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)
  svg#mv_b(left: 1024px; top: 216px; width: 47px; height: 58px; part: file; in: {scale:.7, duration:.25, ease:'power2.out'}; out: gone)
  div#ring(left: 970px; top: 392px; width: 153px; height: 137px; border-radius: 27px; background: none; border: 3px solid $blue; z-index: front; in: {scale:.85, opacity:0, duration:.45, ease:'back.out(2)'})
# 結論の青い札 (図の外・最後に少し大きくなって残る)
div#takeaway(left: 427px; top: 143px; width: 427px; height: 109px; border-radius: 23px; background: $blue; box-shadow: 0px 15px 33px #2159E059; in: {scale:.7, opacity:0, duration:.6, ease:'back.out(1.9)'}; out: {opacity:0, duration:1, ease:'power2.in'})
  p#s(cx: 50%; top: 13px; font-family: m; font-size: 23px; color: $pale) 端末が変わっても
  p#t(cx: 50%; top: 43px; font-size: 39px; letter-spacing: -.01em; color: #FFFFFF) 保存先は同じ
```

```timeline.txt
#v2
cast n = "落ち着いた30代男性のプロのナレーター、低めで明瞭な声で、解説を丁寧にはっきり伝える"
silence head=0 tail=500

*** title
bgm music
@n: [♪whoosh -0.2dB +100][♪pop -1.9dB +450][♪pop2 -4.1dB +1050][♪pop2 -4.1dB +1200][!#ti.art to,{y:-8, duration:1.1, ease:'sine.inOut', repeat:1, yoyo:true} +1000][♪whoosh -1dB +2150][silence:2.7s]

*** ch1
[>#subtitle]
@n: [>#brand][>#brand.pg[1].b +100][>#w1 .tight][silence:0.1s][>#w1.zone_svc scale=0.9,opacity=0,duration=600,ease=power3.out +150][♪pop +0.6dB +150]{b}クラウドストレージ{/}は、[br][>#w1.chip_svc scale=0.6,opacity=0,duration=500,ease=back.out(1.7)][♪click -1dB]サービス側の[>#w1.srv scale=0.5,opacity=0,duration=500,ease=back.out(1.7)][>#w1.lb_srv y=17,opacity=0,duration=500,ease=power3.out +200][♪pop2 -0.2dB]{b}サーバー{/}に[hop #w1.mv_in 1047 245 718 156 1010 890 -100][♪swipe +2.5dB -100]ファイルを[!#w1.srv punch,1.08,duration=560 +300][>#w1.db scale=0.5,opacity=0,duration=500,ease=back.out(1.7) +350][>#w1.w_db draw,400 +450][>#w1.lb_db y=17,opacity=0,duration=500,ease=power3.out +600][hop #w1.mv_drop1 1047 460 1047 350 550 530 +550][>#w1.f1 scale=0.3,opacity=0,duration=500,ease=back.out(1.7) +1050][♪click +0.6dB +1050]保存して使う[>#w1.nt_1 +150][>#w1.ld_1 +150][>#w1.ld_dot +150][♪shine -1.9dB +150]仕組みです。
@: [!#w1.f1 punch,1.3,duration=600]保存したファイルは、[<#w1.nt_1 -300][<#w1.ld_1 -300][<#w1.ld_dot -300][!#w1 to,{x:285, duration:1.4, ease:'power3.inOut'} -250][>#w1.q_bubble +100][♪q +1.3dB +100][>#w1.sil_pc +450][>#w1.sil_sp +600][!#w1.sil_pc to,{y:-7, duration:.7, ease:'sine.inOut', repeat:3, yoyo:true} +1100][!#w1.sil_sp to,{y:-7, duration:.7, ease:'sine.inOut', repeat:3, yoyo:true} +1100]どこから開けるのでしょうか。

*** ch2
@n: [♪whoosh -1dB][>#brand.pg[2].b +100][<#w1.q_bubble][silence:0.6s][>#w1.zone_dev scale=0.9,opacity=0,duration=600,ease=power3.out][>#w1.chip_dev scale=0.6,opacity=0,duration=500,ease=back.out(1.7) +150][♪pop +0.6dB]手元には、[<#w1.sil_pc][>#w1.pc scale=0.5,opacity=0,duration=500,ease=back.out(1.7)][>#w1.lb_pc y=17,opacity=0,duration=500,ease=power3.out +200][♪pop2 +1.3dB]{o}パソコン{/}や[<#w1.sil_sp][>#w1.sp scale=0.5,opacity=0,duration=500,ease=back.out(1.7)][>#w1.lb_sp y=17,opacity=0,duration=500,ease=power3.out +200][♪pop2 +1.3dB]{o}スマートフォン{/}など、[br][>#w1.brace -150][>#w1.nt_dev3][♪pen -1dB -150]ファイルを使う{o}端末{/}があります。
@: [<#w1.brace -150][<#w1.nt_dev3 -150]{o}端末{/}は、[>#w1.hub scale=0.4,opacity=0,duration=500,ease=back.out(1.7)][>#w1.hub_ring scale=0.6,opacity=0,duration=600,ease=power3.out +100][>#w1.lb_net y=17,opacity=0,duration=500,ease=power3.out +200][>#w1.wb_pc draw,700,ease=power2.inOut][>#w1.wb_sp draw,700,ease=power2.inOut +100][>#w1.wf_pc fade,400 +500][>#w1.wf_sp fade,400 +500][♪pop +1.3dB]{t}ネットワーク{/}を通して、[br]サービス側の[>#w1.wb_sv draw,700,ease=power2.inOut -100][>#w1.wf_sv fade,400 +400][>#w1.ring_a +200][<#w1.ring_a +1600]{b}保存先{/}へ[>#w1.pl_acc[1]][>#w1.pl_acc[2] +120][>#w1.pl_acc[3] +240][hop #w1.pk[1] 985 245 640 355][hop #w1.pk[2] 985 245 640 355 +200][hop #w1.pk[3] 985 245 640 355 +700][hop #w1.pk[4] 985 245 640 355 +900][!#w1.hub punch,1.1,duration=400 +550][!#w1.srv punch,1.06,duration=400 +1200][♪data -4.9dB]アクセスします。
@: [<#w1.pl_acc -50][>#w1.ring_b][<#w1.lb_db -100][>#w1.lb_same +200][♪click -1dB]同じ{b}保存先{/}を使うことで、[>#w1.pc_doc]{o}パソコン{/}から[>#w1.pl_save -100][hop #w1.mv_save 1047 245 640 355 1350 1330][hop #w1.mv_drop2 1047 460 1047 350 500 480 +1300][>#w1.f2 scale=0.3,opacity=0,duration=500,ease=back.out(1.7) +1750][♪swipe +0.6dB]保存したファイルを、[br][<#w1.ring_b -200][>#w1.pl_open][♪whoosh -3dB][>#w1.mv_open -50][!#w1.mv_open to,cy=245,duration=400,ease=power2.out -50][!#w1.mv_open to,cx=233,cy=467,via=(640,355),duration=800,ease=power1.inOut +350]{o}スマートフォン{/}から[<#w1.mv_open][>#w1.sp_doc][>#w1.sp_ok +250][>#w1.nt_5 +350][♪ok -2.5dB +250]開くこともできます。
[<#w1]

*** ch3
@n: [♪whoosh -1dB][>#brand.pg[3].b +100][silence:0.6s][>#ex_l +120]たとえば、[>#ex_l.pc][♪pop2 +0.6dB]{o}パソコン{/}で用意した[>#ex_l.deck][>#ex_l.decklb +150][>#ex_cloud +500][>#ex_a1 +600][>#ex_a1h +1200][hop #ex_mv1 539 276 452 239 800 780 +600][♪pop +0.6dB][♪swipe -1dB +600]研修資料を、[br][>#ex_r -100]移動先の[>#ex_r.sp][>#ex_a2 +100][>#ex_a2h +700][hop #ex_mv2 908 301 824 237 800 780 +100][♪whoosh -3.4dB +100]{o}スマートフォン{/}で[>#ex_r.spdeck -100][>#ex_r.ok +200][>#ex_r.rlb +100][♪ok -2.5dB +200]確認する使い方です。

*** ch4
@n: [♪whoosh -1dB][>#brand.pg[4].b +100][silence:0.6s]ここで、[!#w4.zone_dev glow,#D9680B47,blur=0,spread=7][=#w4.zone_dev +3200][>#w4.nt_dev +50][♪click -1dB]ファイルを使う{o}端末{/}と、[br][!#w4.zone_svc glow,#2159E042,blur=0,spread=7][=#w4.zone_svc +2400][>#w4.nt_svc +50][♪click -1dB]ファイルが保存されている場所は[>#w4.neq][net #w4 0.25][♪accent +0.6dB]同じとは限りません。
@: [<#w4.neq -100][<#w4.nt_dev -100][<#w4.nt_svc -100][net #w4 1 300 -100]{b}クラウドストレージ{/}では、サービス側の[!#w4.srv punch,1.1,duration=500]{b}サーバー{/}がファイルを[>#w4.pl_keep][>#w4.f3 +100][!#w4.f1 punch,1.15,duration=400 +350][!#w4.f2 punch,1.15,duration=400 +350][!#w4.f3 punch,1.15,duration=400 +350][♪pop2 -0.2dB +100]保管し、[br]{o}端末{/}からの[>#w4.ar_req -100][>#w4.ar_req_h +800][>#w4.lb_req][hop #w4.mv_req 980 212 640 316 950 830 -100][!#w4.srv punch,1.08,duration=400 +850][♪swipe -0.2dB -100]要求に応じて[>#w4.ar_res -200][>#w4.ar_res_h +700][>#w4.lb_res -50][hop #w4.mv_res 287 500 640 393 1000 780 -200][>#w4.sp_doc +800][>#w4.sp_ok +1000][♪whoosh -3dB -200][♪ok -3.4dB +1000]渡します。
@: [<#w4 -200][>#tm_veil -200][>#tm -100][>#tm.tag +150][>#tm.word +100][>#tm.art +100][>#tm.art.srv +250][♪paper +3.6dB -100]{b}サーバー{/}とは、このようにデータを[>#tm.d1 -350][>#tm.r1 +150][♪pop2 -1.9dB +150]保管したり、[br][>#tm.d2 -100]求められたデータを[>#tm.r2 +100][♪pop2 -1.9dB +100]渡したりする[>#tm.d3 -100][>#tm.uline +300][♪pen -1.9dB +300]コンピューターです。

*** ch5
@n: [♪whoosh -1dB][>#brand.pg[5].b +100][>#cl .mid][silence:0.6s][>#cl.card +50][♪pop -0.2dB +100]一方、[>#cl.chip][>#cl.clpc.pc +250][♪pop2 -0.2dB +250]{o}端末{/}の中だけにファイルを[>#cl.clpc.f][♪pop2 -0.2dB]保存した場合、[br][>#cl.clpc.tag][♪click -1dB]{b}保存先{/}はその{o}端末{/}です。
@: [!#cl.clpc .l -350][>#cl.sp][>#cl.lbsp +150][>#cl.spq +300][♪pop2 -0.2dB]別の{o}端末{/}で使うには、[br][>#cl.mv -100][>#cl.mvh +600][>#cl.mvlbl][hop #cl.usb 427 168 326 127 1000 980 +100][♪whoosh -3dB +100]ファイルを移すなどの[>#cl.warn][!#cl.warn to,{x:5, duration:.06, ease:'none', repeat:5, yoyo:true} +450][♪notify -0.2dB]準備が必要です。
@: [!#cl .home -200]これに対し、[>#cr_card -100][>#cr_chip][>#cr_cloud +200][>#cr_db +350][♪pop +0.6dB -100]{b}クラウドストレージ{/}は、[br][>#cr_pc -100][>#cr_sp][>#cr_wb1][>#cr_wb2 +100][>#cr_w1 +500][>#cr_w2 +500][>#cr_net +300][♪pop2 -1dB]{t}ネットワーク{/}を通して[>#cr_same][!#cr_db punch,1.2,duration=500 +100][♪click -1dB]同じ{b}保存先{/}へ[hop #cr_pk[1] 937 267 868 349 1000 980][hop #cr_pk[2] 937 267 1015 348 1000 980 +200][♪data -5.5dB]アクセスする仕組みです。

*** ch6
@n: [♪whoosh -1dB][>#brand.pg[6].b +100][silence:0.6s][>#ac_st][>#ac_stc +100][>#ac_r[*] +200]ファイルを開ける[>#ac_range][>#ac_rlb +100][♪pen -1.9dB]範囲は、[br]利用する[>#ac_card -100][>#ac_user][>#ac_lb +150][>#ac_id +300][♪pop -1.9dB]{v}アカウント{/}や[>#ac_l1 -200][>#ac_l1h +200][>#ac_kbox -50][>#ac_key +50][>#ac_kl +200][>#ac_l2 +500][>#ac_l2h +900][♪click -1.9dB +50]{v}アクセス権限{/}によって[>#ac_ok1 -100][>#ac_ok2 +50][>#ac_lock +250][!#ac_lock to,{rotation:10, duration:.07, ease:'none', repeat:5, yoyo:true} +700][!#ac_range punch,1.02,duration=600 +200][♪ok -3dB -100][♪lock -3dB +250]決まります。

*** sum
@n: [♪whoosh -1dB][>#brand.pg[7].b +100][net #w8 0.22 10][wires #w8 0.22 10][silence:0.6s]仕組みを捉えるときは、[!#w8.zone_svc glow,#2159E042,blur=0,spread=7][=#w8.zone_svc +3400][<#w8.chip_svc -100][>#w8.sm_svc +200][♪click -1dB +100]ファイルの{b}保存先{/}と、[br]そこへ[!#w8.zone_dev glow,#D9680B47,blur=0,spread=7][=#w8.zone_dev +2400][<#w8.chip_dev -100][>#w8.sm_dev +200][♪click -1dB +100]アクセスする{o}端末{/}を[>#w8.divider -100][>#w8.sep +100][!#w8.zone_dev to,{x:-9, duration:.6, ease:'power2.out'} +100][!#w8.zone_svc to,{x:9, duration:.6, ease:'power2.out'} +100][♪pen -1dB -100]分けて考えましょう。
@: [<#w8.sep -100][!#w8.divider to,opacity=0.25,duration=400 -100][!#w8.zone_dev to,{x:0, duration:.6, ease:'power2.inOut'} -100][!#w8.zone_svc to,{x:0, duration:.6, ease:'power2.inOut'} -100][net #w8 1 500 -100][wires #w8 1 500 -100][!#w8.f1 punch,1.3,duration=600][!#w8.f2 punch,1.3,duration=600]同じ資料を[hop #w8.mv_a 233 267 640 355 1000 780 -200][>#w8.pc_doc +750][>#w8.pc_ok +950][♪swipe -1dB -200][♪pop2 -1dB +950]{o}パソコン{/}でも[hop #w8.mv_b 233 467 640 355 1000 780 -200][>#w8.sp_doc +750][>#w8.sp_ok +950][♪whoosh -3.4dB -200][♪ok -3dB +950]{o}スマートフォン{/}でも開けるのは、[br][!#w8.pc punch,1.06,duration=440][!#w8.sp punch,1.08,duration=440 +300]{o}端末{/}が変わっても、[>#w8.ring][>#takeaway +150][♪kira +1.9dB +150 to=1.7s]同じ{b}保存先{/}を使えるからです。[silence:0.8s][!#w8 to,{opacity:0.35, duration:.9, ease:'power2.inOut'}][!#takeaway to,{scale:1.1, duration:.9, ease:'power2.inOut'}][<#h7 +300][<#brand +300][silence:4.2s]
[<#w8 cut-200][<#takeaway cut-200]
```

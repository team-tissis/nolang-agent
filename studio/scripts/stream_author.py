"""stream の著者 — Opus を Claude Code (`claude -p`・tool 無し) で呼び、本文の src を token の stream で受けて section が閉じた順に file に落とす。

著者は 1 call (`claude -p --output-format stream-json`・system prompt = skill の文書 + type の見本 2 本・既定 low):
  `=== plan ===` (cut 一覧) → `=== root_design ===` → `=== root_timeline ===` → `=== cut 名 ===` を構成の順に (design の block・`---timeline---`・
  timeline の block) → `=== end ===`。plan が閉じた時点で solo/order.txt を書く (orchestrator が cut を待ち始める)。
  low は書き始めるまで数秒で、書く速さ (約 180 字/s・1 cut 約 3.5 s) が再生より速いので、cut を分けて並行に書かせる理由が無い。質は cut ごとの
  担当 (medium) が運ぶ (docs/draft_src_v2/stream-evidence-261013.md s9 / s10)。1 人が全 cut を書くので、cut を跨ぐ名の衝突・型のばらつきも出ない。
直し (low) は stream_run.py が cut ごとに頼む (`fix` subcommand: block + check の指摘 → 直した block)。
担当・直し役の system prompt (見本込み) は著者の call と並んで 1 回だけ温める (`warmup`・author.jsonl の `warmup` event)。

usage (repo root から):
  python stream_author.py run  <project>   [--effort low] [--samples a.md,b.md]
      --samples = system prompt に同梱する見本 (reference/samples/ の file 名・2 本以上)。省略時は reference/samples/ の NoLang の src
                  `<type>_NN.md` 1 本 + hf max の写し `hf_<type>_*.md` 1 本 (どちらも依頼と同じ題材を外し、依頼と同じ向きの物を先に・pick_samples)。
                  stream/samples.txt に記録し fix も同じ見本を使う
  python stream_author.py staff <project> <cut> <findings>  [--effort medium]   # 担当: 8 観点で cut を見直して block を stdout へ
  python stream_author.py fix  <project> <cut 名> <findings file> [--root] [--effort low] [--review] [--shots a.png,b.png]
      → stdout に直した block (--root = 根の 2 file も直す・--review = 見直し (確認表で指摘に出ない崩れも探す)・
        --shots = 見直しに cut の静止画も見せる (stream_run の --look))
project = tmp/studio/<name>/ (request.txt・params.txt = "type aspect seconds"・studio/ = `new` の雛形)。
出力: project/stream/ (system_prompt.md・claude_*.jsonl・author.jsonl = 時刻の記録) と project/solo/ (plan.txt・order.txt・root_design.txt・root_timeline.txt・cut_<名>.txt)。
"""

from __future__ import annotations

import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
import unicodedata
from collections.abc import Callable
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
# 見本の置き場。既定の見本は NoLang の src `<type>_NN.md` 1 本 + hf max の写し `hf_<type>_*.md` 1 本 (pick_samples)。自分の type の見本が
# 足りない時に借りる近い type と、system prompt に同梱する見本 1 本の大きさの上限 (超える物は選ばない)
SAMPLES_DIR = SKILL / "reference/samples"
NEAR_TYPE = {"cinematic": "story", "compare": "concept", "data": "compare", "story": "cinematic", "concept": "compare"}
SAMPLE_MAX_BYTES = 70_000
# 題の語: 漢字・片仮名の続き 2 字以上 (`カゴ落` `麻辣湯` のように混ざって良い)・英字で始まる英数 3 字以上。平仮名だけの語は数えない
# (「きている」「れない」のような活用の切れ端が題の語になる) — 1 字の漢字と助詞も数えない
TOPIC_WORD = re.compile(r"[\u4e00-\u9fff々\u30a0-\u30ffー]{2,}|[A-Za-z][A-Za-z0-9]{2,}")
MARK = re.compile(r"^\s*===\s*(plan|root_design|root_timeline|end|cut\s+([A-Za-z0-9_\-]+))\s*===\s*$")
FENCE = re.compile(r"^\s*```")
CUTHEAD = re.compile(r"^section#([A-Za-z0-9_\-]+)")
TLHEAD = re.compile(r"^\*\*\*\s+\S+")
# claude を起動する cwd: CLAUDE.md の無い場所 (repo の CLAUDE.md を読ませない)
CWD = Path("/tmp/nolang-stream-cwd")  # claude -p の cwd (repo の外 — project の CLAUDE.md / settings を読ませない)
MODEL = "claude-opus-5-5"
# 見直し役に見せる静止画の幅 (1920 のままだと 1 枚 2.7k token・960 で 0.7k — 字の重なりは 960 でも見える)
SHOT_WIDTH = 960
# 状態を運ぶ常設 (章番号・STEP の進み・累計) を根に置ける動画の長さ (plan の見込み秒の和)。1 分程度の動画には置かない (ユーザーの裁定 10-15)
LONG_VIDEO_S = 180


# claude の実体を起動時に解決する (PATH 上の shim が更新中だと一時的に見つからない)
def claude_bin() -> str:
    """`claude` の実体。shim は自動更新の瞬間に消える事があるので呼ぶたびに引く (見つからなければ名前のまま → 呼ぶ側がやり直す)。"""
    return shutil.which("claude") or "claude"


def log(st: Path, **kw: object) -> None:
    kw["t"] = time.time()
    with (st / "author.jsonl").open("a") as f:
        f.write(json.dumps(kw, ensure_ascii=False) + "\n")
    print(json.dumps(kw, ensure_ascii=False), file=sys.stderr, flush=True)  # stdout は fix の本文に使う


def sample_head(name: str) -> str:
    """見本の 1 行目 `# type · 題 (注記) — canvas WxH`。"""
    return (SAMPLES_DIR / name).read_text(encoding="utf-8").split("\n", 1)[0]


def sample_portrait(name: str) -> bool:
    """見本が縦か (1 行目の `— canvas WxH` で幅 < 高さ)。"""
    m = re.search(r"— canvas (\d+)x(\d+)", sample_head(name))
    return bool(m) and int(m[1]) < int(m[2])


def sample_topic_words(name: str) -> list[str]:
    """見本の 1 行目 `# type · 題 (注記) — canvas …` の題の語。hf の写しは英字の slug (`black-tire`) を除き、注記の `— ` の後の
    和文の題 (`タイヤが黒い理由`) を足す。NoLang の見本の注記 (`縦・台本そのまま・絵本調`) は題でないので読まない。"""
    head = sample_head(name).split(" · ", 1)[-1].split(" — canvas", 1)[0]
    m = re.fullmatch(r"(.*?)\s*\((.*)\)\s*", head)
    title, note = m.groups() if m else (head, "")
    parts = [
        p.split("・", 1)[0] for p in title.split(" — ") + note.split(" — ")[1:] if not re.fullmatch(r"[a-z0-9-]+", p)
    ]
    return sorted({w for p in parts for w in TOPIC_WORD.findall(unicodedata.normalize("NFKC", p))})


def same_topic(name: str, request: str) -> bool:
    """見本が依頼と同じ題材か: 題の語の半分以上が依頼にあり、それが 2 語以上か 3 字以上の語を含む (「解説」「紹介」のような
    2 字の語 1 つだけの一致は曖昧なので同じ題材と見ない)。"""
    words = sample_topic_words(name)
    req = unicodedata.normalize("NFKC", request).lower()
    hit = [w for w in words if w.lower() in req]
    return 2 * len(hit) >= len(words) > 0 and (len(hit) >= 2 or any(len(w) >= 3 for w in hit))


def pick_samples(typ: str, aspect: str, request: str) -> tuple[tuple[str, ...], list[str]]:
    """reference/samples/ から 2 本 = NoLang の src (`<type>_NN.md`) 1 本 + hf max の写し (`hf_<type>_*.md`) 1 本 → ((NoLang, hf), 外した見本)。
    両側とも規則は同じ 3 つ: SAMPLE_MAX_BYTES 以下の自分の type の見本から (後ろに NEAR_TYPE の見本を足す)・依頼と同じ題材の物を外す・
    依頼と同じ向き (canvas の縦横) の物を先に。その中の順番は file 名順 (大きさ順だと見本を 1 行直すたびに選ばれる物が替わる)。
    片側に 1 本も無ければもう片側の 2 本目を取る。自分の type の NoLang の見本に依頼と同じ向きの物が無ければ NoLang 側を使わず、hf の
    写し 2 本 (同じ向きを先に) にする。NoLang の src は製品の文法で勝った書き方 (字幕・cut の組み方)、hf の写しは
    絵と動きの作り込みの見本 — 10-16 の bs7 はこの混合で回していた。
    著者は見本を逐語で写す (s1 で 50〜68%・pv で台詞と印ごと) ので、同じ題材の見本は既定でも渡さない。"""
    portrait = aspect == "9:16"
    skipped: list[str] = []

    def ranked(pattern: str) -> list[str]:
        out: list[str] = []
        for t in (typ, NEAR_TYPE[typ]):
            names = sorted(
                p.name
                for p in SAMPLES_DIR.iterdir()
                if re.fullmatch(pattern.format(t=t), p.name) and p.stat().st_size <= SAMPLE_MAX_BYTES
            )
            same = [n for n in names if same_topic(n, request)]
            skipped.extend(same)
            out += sorted((n for n in names if n not in same), key=lambda n: sample_portrait(n) != portrait)
        return out

    nolang, hf = ranked(r"{t}_\d+\.md"), ranked(r"hf_{t}_.+\.md")
    if not any(n.startswith(f"{typ}_") and sample_portrait(n) == portrait for n in nolang):
        # 自分の type の NoLang の見本に依頼と同じ向きの物が無い — 向き違いの src は字幕・cut の組み方ごと写される (16:9 の concept に
        # 縦の見本が付き、縦の配置で書いた) ので NoLang 側を諦め、hf の写し 2 本を同じ向き優先で取る
        nolang, hf = [], sorted(hf, key=lambda n: sample_portrait(n) != portrait)
    picked = nolang[:1] + hf[:1]
    picked += (nolang[1:] + hf[1:])[: 2 - len(picked)]
    if len(picked) < 2:
        raise SystemExit(f"reference/samples/ に {typ} ({NEAR_TYPE[typ]}) の見本が 2 本無い: {picked}")
    return (picked[0], picked[1]), skipped


def build_system_prompt(out: Path, samples: tuple[str, ...] | None) -> Path:
    """SKILL + looks + sounds + authoring + capabilities + 見本 2 本 (道具の無い call は file を読めないので全部同梱)。samples=None は見本なし
    (著者の静的な system prompt — 見本は user turn に置く)。担当と直し役は見本入り — 見本を外すと担当の組み上げ・状態の変化が半分に
    減り、両順の比べで 6 題材中 4 題材負けた (10-22)。"""
    head = (
        "あなたは HTML + CSS + GSAP で動画を作るプロの制作者です (scene の DOM を書き、class で見た目を揃え、GSAP の timeline で"
        "要素ごとの入場・状態変化・退場を打つ、いつもの作り方)。今回はその動画の設計図を NoLang の draft src (HTML / CSS / GSAP の圧縮形) で"
        "書きます。役は 3 つ — 全体を書く著者・cut を見直す担当・check の指摘を直す直し役 — で、どの役か・変えてよい物は user の指示に従います。"
        "見た目 (色・書体・構図・動き) は著者が題材から決め、担当と直し役は根 (palette・font・cast) をそのまま使います。"
        "目標は、プロの制作会社が作った動画と並べて見劣りしない質です。\n"
        "この会話に道具はありません (file は読めず書けず、command も打てません)。文法と作法は下の文書が全部です — file を読もうとしないでください。"
        "文書の中の `studio.py check / render` の手順は別の process が代わりに打ちます。あなたは本文に src を書くだけです。\n"
    )
    parts = [head]
    for rel in (
        "SKILL.md",
        "reference/looks.md",
        "reference/sounds.md",
        "reference/authoring.md",
        "reference/capabilities.md",
    ):
        parts.append(f"\n<!-- ===== {rel} ===== -->\n\n" + (SKILL / rel).read_text())
    parts.append(samples_text(samples or ()))
    out.write_text("".join(parts))
    return out


def samples_text(samples: tuple[str, ...]) -> str:
    """見本 2 本の本文 (著者の user turn に置く)。"""
    return "".join(
        f"\n<!-- ===== 見本 reference/samples/{name} ===== -->\n\n" + (SAMPLES_DIR / name).read_text()
        for name in samples
    )


def author_prompt(
    typ: str, aspect: str, seconds: str, skeleton_d: str, skeleton_t: str, request: str, samples: str = ""
) -> str:
    canvas = next((line.split()[1] for line in skeleton_d.splitlines() if line.startswith("canvas ")), "")
    return f"""下の依頼の動画の src を書きます。まず構成 (plan) と根、続けて cut を構成の順に上から一度に書きます。書いた端から別の process が
cut ごとに check と描画を始めるので、書きながら前に戻って直さない。画面は {aspect} — 根の canvas は雛形と同じ `canvas {canvas}` (見本や
辞書の例の canvas を写さない・要素の位置と大きさもこの画面で決める)。根に置く物は動画全体の設定だけ:
palette / font / fonts / photo_style / cut の既定 / subtitle (開く印) / bgm / cast / transition= / read / 常設の層。
palette・font・fonts は style の組 (looks.md) から題材に合わせて決める — 雛形の値を写さない (数字の書体 `fonts n` も組ごとに違える)。
名のある定義 (def・motion・run・svg・sound・cue) は、それを初めて使う cut の design の行 (`section#名` の次) に書く — 後の cut もその名を
使える (前の cut の定義は参照できる・同じ名を 2 度は定義しない・使う cut より後の cut に定義を書かない)。根の層 (`.sticky` の札・帯) には
`out:` と `end` 基準の key を書かない (閉じる cut が来るまで描画が止まる)。
常設の層 (cut を跨いで居続ける札・帯): 飾りの header (題の帯・番組名) は置かない。章番号・STEP の進み・累計のような状態を運ぶ常設は、動画が
3 分以上 (plan の見込み秒の和が {LONG_VIDEO_S} 以上) の時だけ根に 1 つ (上端・`.sticky`)。それより短い動画 (1 分程度) には置かない。
累計 (data の題材で数字が 2 cut 以上続いて合計になり、3 分以上の時だけ): plan の各行の見せ物に、その cut の後の累計 (`累計 151,200円`) を書き
(和は plan で 1 回だけ計算する)、根の上端の札 `p#sum.sticky(…) 累計 [count:0]円` を各 cut で `[!#sum text,"累計 [count:151,200]円"]` に
替える (plan の値を写す・数字は 3 桁区切りで書く・数え始めは前の値から自動)。印はその数字を言う語に (cut の頭に置くと台詞より先に和が見える)・
上端の帯に他の cut の要素を置かない (札が押されて動く)。

出力の形 (この形以外は書かない。前置き・説明・code fence・見出しは書かない。各 `=== … ===` の行は行頭から):
=== plan ===
名: 台詞の要約 / 見せ物 (見込み秒)      ← 1 行 1 cut・名は英小文字 (hook / close など)・この順で cut が並ぶ・1 cut は 4〜25 秒
                                         見せ物 = その cut で大きく見せる 1 つ (数字・図・比べる 2 つ・結論の一言のどれか・台本にある語から)。
                                         台本に数字の無い「急・遅い・多い」は図で (数字は足さない)
                                         冒頭の cut は題の語を最初の文で言い、見せ物は問いか主張の一言 (語ごとに組み上げる)・
                                         最後の cut は主題の名と結論の一言で終える
=== root_design ===
design.txt の `section#` より前の全部 (`#v2` から。計画の # 行・canvas・theme・palette・font・fonts・photo_style・cut の既定・subtitle・bgm・常設の層。def・motion・run は使う cut に)
=== root_timeline ===
timeline.txt の `***` より前の全部 (`#v2`・cast・transition=・read)
=== cut 名 ===
section#名(…)            ← この cut の design の行 (字下げ 0。字下げ 2 空白は子だけ)。この cut で初めて使う def・motion・run はこの直後に
…
---timeline---
*** 名                    ← この cut の timeline の block (台詞・印・se・最後の行に transition)
…
=== cut 次の名 ===
…
=== end ===

書き方: 依頼の台本・テロップの文言はそのまま使う (途中で切れていれば依頼の構成に沿って残りを書く)。尺は合わせない (依頼の長さは目安)。素材は説明文で書く。
絵の説明文: 時代・形・数の段階・前後の違い (「1950 年代の四角い窓」「乗客がまばら」) は写真に担わせず図か文字で言い、写真は場の雰囲気に (生成は時代や形を守らない)。
1 枚に 1 場面 (「A と、B」の 2 場面は上下 2 枚の合成になる)。物語で同じ物 (人物・器・時計) が 2 枚以上に出るなら根に `image 名 = "…"` を置き各絵は `[ref:@名]` で派生させる。
各 cut の design は要素が全部出た時の位置と大きさ、timeline は台詞と語の印 (`[>#名]` 出す・`[!#名 …]` 変える・`[<#名]` 消す)。cut の切替は前の cut の
timeline の最後の行に `transition …`。
要素の名は cut の名を頭に (`hook` の cut なら `hook_t`・`hook_img`)。根の物を除き、cut を跨いで同じ名を使わない。

雛形 (`new --type {typ} --aspect {aspect} --seconds {seconds}` の出力・根の形の参考・台詞と題材は架空の例):
--- design.txt ---
{skeleton_d}
--- timeline.txt ---
{skeleton_t}
{samples}{request}"""


STAFF_VIEW = """1. 同期: 要素がその語の瞬間に出るか (先に全部見えている・語より何秒も遅れる、はどちらも減点。答えを待つ ? の箱や前後の板も、中身を言う語で)
2. メリハリ: 溜め → 組み上がる → 主役が立つ → 次へ、と動くか (語の間の溜めは 3 秒まで・cut の頭は 1.2 秒以内に中身を出す)
3. 主役: その瞬間に見るべき 1 つが分かるか (大きさ・色・前の札を沈める・動き)。全部が同じ強さの札の列は弱い。
   構成の行の見せ物がその cut で一番大きく見えるか — 要の語 (数字・比べる 2 つ・結論) は横 96px・縦 108px 以上
   (stat / big の段・根に無ければ大きな文字)。物 (道具・画面・通知) は icon か絵を画面の中ほどに大きく
4. 読みやすさ: 写真の上に直接置いた細い文字・小さな札は沈む。大きく太い字でも、絵の主な色と同じ系統の色なら沈む (全面の閃光の直後も同じ)
   — 文字の側に幕 (veil の `to:`・image の `scrim:` の向き) か板を敷く・絵を窓にして文字は地に置く (縁取りは最後の手段で blur の影)
5. 図と変化: 内容に合った図か、同じ絵を長く使い回していないか、状態の変化 (色・数字・位置) が見えるか。絵の説明文は 1 枚 1 場面・時代 / 形 / 数の段階は
   写真でなく図か文字に・根の `image 名 =` にある物を描く絵は `[ref:@名]` で派生 (別物になる)。比べる 2 つや前後の値は
   片方ずつ語で出し、差は最後に大きく見せる (板を先に完成させない)。位置の小さなずれや揺れだけでは変化に見えない — 伸びる・数える・色が変わる・現れて消える
6. so what と締め: 場面の結論の一言は、その cut で一番大きな字で (横 96px・縦 108px 以上。pill・札・板の中の小さな字にしない)。
   最後の cut は結論か問いを画面の主役に (台詞が問いなら問いの文を見せる)。締めの無音の間にも 1 つ変化を (色を落とす・判子・名の札)
7. 連続性: 黒 frame (暗い絵に濃い黒の幕を重ねた、ほぼ黒い画面も同じ)・突然の消失・位置の飛びを作らない
8. 作り込み: 板と中身が一体で動くか (板は中身の最初の値と同じ語で出す — 板だけが 1 秒以上見えると空の板)・写真が素材として成立しているか・
   章札や判子など番組としての質感"""

# 担当の版で審査に多く出た欠陥の型 (新題材 12 本・Opus 審査 138 件のうち担当が作った 59 件・10-22)。数字は check の規則と同じ値
STAFF_PITFALLS = """担当の版で多い欠陥 (どれも check にほぼ出ないので、書く時に避ける)。これは足し方の注意で、足す量を減らす理由ではない —
語ごとの組み上げ・数える・前の札を沈める・場面を替える寄りの絵・結論の大きな一言は、今までどおり足す:
- 空の板: 印の無い板は engine が中身の最初の語で出す (中身が全部 `[>#]` で出る時だけ — 印の無い子が 1 つでもあれば板ごと cut の頭に出る)。
  板・名札・見出しの小札・地のある ×N の枠・棒の track は、中身の最初の値と同じ語で出す — 小札や枠だけを先に出して値を後の語に分けない
  (板だけが 1 秒以上見えると empty_board)。例: `[>#c[1]]新NISAは、[>#c[1].v]いつでも` は板と名札だけが先に見える →
  `新NISAは、[>#c[1]]いつでも` (板・名札・値を値の語で一緒に・名札の語を言う間は待ってよい)。書いた後、板に付けた `[>#板]` と
  `[>#板.子]` が別の語に分かれていないかを見直す。中身は板の字下げの子に書く (`overlap:` の兄弟は中身に数えない)。比べる 2 行は行ごとの板に。
- 小さい字: 画面の字は 54px 以上 (補足・ラベル・chip・凡例・kicker・小札も。check の small_text はそれより下の読める床)。54px で収まらない字は
  足さず、著者の版の 54px 未満の字は上げるか消す (出典・注記の 1 行だけ 42px まで)。`$mute` の字に `dim` を重ねない。
- 顔・主体に乗る板: 絵の上に不透明な板・帯・飾り線・ラベルを置くなら、絵に `subject:` と `room:` を書き、板と文字は room の中だけに置く
  (`subject: right 40%` なら横 1280 で x < 768)。人物を大きく描かせた絵の上 1/3 に不透明な板を置かない (頭がそこに来る)。
- 沈めた字・幕の上の字: 地と逆の明るさに (暗い幕に白・明るい板に濃い色)。沈めは `dim,0.6` 程度まで、溶けるなら `[<#名]` で閉じる。
  全面の写真の幕 (`scrim:`・veil の opacity) は 0.7 未満 (0.7 以上が 3 秒続くと写真が消える — photo_hidden)。もっと濃くしたいなら写真を片側の
  窓にして文字は地に。明るい空・白い地の絵に、中心の暗い radial の幕を敷かない (しみに見える)。
- 字幕と同じ文: 画面の文字は台詞の要点の短い語 (字幕と同じ文が 2 か所に並ぶ)。`.hide_subtitle` は足さない。
- 入場の時刻: 切替・fade out の 0.8 秒前より後に新しく出さない (締めの判子も)。前の切替の窓 (cut の頭の 0.3〜0.4 秒) にも出さない —
  頭の要素は印なしで cut の頭に置くか、最初の台詞の頭に `[silence:+0.4s]`。
- 絵: 場面を替える 2 枚目の絵 (寄り・別の角度) は良い — 2 枚目の in は 0.5 秒以下で、1 枚目をその語で閉じる (1 秒を超える溶け合いは
  二重写し)。同じ物を 2 枚以上描くなら (この cut の中でも前の cut とでも) 色・服・画風・顔の有無を同じ語で書く。絵の一部を指す丸・矢印は
  その部分の大きさに (絵全体を囲まない)。
- 締め: 最後の変化の後の無音は 1.5 秒まで。答え (数字・結論) を閉じて新しい絵に替えない。
- 書き方: `×N` の width / height は 1 枚の寸法 (枠全体ではない)。著者の版にある注記・依頼の数字は削らない。"""


def cut_place(name: str, order: list[str]) -> str:
    """cut の位置の 1 行 (担当の prompt) — 何番目か・最初 / 本題 / 最後のどれか。"""
    k, m = (order.index(name) + 1, len(order)) if name in order else (0, len(order))
    if k == 1:
        role = "最初の cut — 最初の語で 1 つ立て、続く語ごとに 1 つずつ組み上げて、問いか主張の一言を一番大きく見せる (題や空の箱を先に全部出して止めない)"
    elif k == m:
        role = "最後の cut — 主題の名と結論の一言 (か問い) を画面の主役にして終える"
    else:
        role = "本題の cut"
    return f"この cut は {k} 番目 / 全 {m} cut ({role})。"


def staff_prompt(
    name: str,
    block: str,
    findings: str,
    root_d: str,
    root_t: str,
    plan: str,
    prev_name: str | None,
    prev_block: str | None,
    planned_s: float,
    defs_before: str = "",
    *,
    request: str = "",
    order: list[str] | None = None,
    target_s: str = "",
    timing: str = "",
) -> str:
    # 常設: 3 分未満の動画と最初の cut (再生開始の経路 — prompt を増やさない) は足さないだけ。3 分以上は根の常設の札への差し替えを許す
    persistent = (
        "常設の帯は足さない。"
        if planned_s < LONG_VIDEO_S or prev_name is None
        else f"常設の帯・飾りの header は足さない (常設は根の物だけ)。この動画は構成の見込みで {planned_s:.0f} 秒 (3 分以上) — 根の sticky の札"
        ' (累計・章番号・STEP) には、構成の行の値で `[!#名 text,"…"]` を当ててよい (その数字・章を言う語に・値は構成のとおり・著者の版にあれば残す)。'
    )
    prev = (
        f"前の cut `{prev_name}` (著者の版・参考。変えない。前の cut も別の担当が並列に書き換えるので、実際の画面はこの版と違う — "
        f"揃えるのは根と定義の型と大きさ):\n=== cut {prev_name} ===\n{prev_block}=== end ===\n"
        if prev_name and prev_block
        else ""
    )
    length = (
        f"動画の長さ: 依頼の目安 {target_s} 秒・構成の見込みの和 {planned_s:.0f} 秒 (構成の各行の末尾の `(数)` はその cut の見込み秒)。"
        "尺は台詞で決まる — 無音で寄せない。"
    )
    return f"""あなたはこの動画のディレクターです。著者が書いた cut `{name}` の block を、視聴者として見たときの良さで見直し、必要なら作り替えて返してください。
見るのは画面が埋まる速さや情報の量ではなく、次の 8 つです:
{STAFF_VIEW}

守る事: 台詞 (`@` の行の文字) は一字も変えない (許すのは読点の追加と `{{表記|読み}}` の読みの指定だけ・依頼の台本の文言は声になる)。話者 (`@名:`) は保つ。
根 (palette・font・cast) と前の cut の定義 (def・motion・run) は変えない (使ってよい)。この cut の block の定義も後の cut が同じ名で使っている — 名・引数の形・見た目 (大きさ・余白・色) を変えない。別の形や見た目が要るなら新しい名で定義してこの block で使う (後の cut が使う定義の見た目を変えると、元の定義が戻り、変えた版は `名_<cut>` に改名される)。
板・札・見出しの台は、根と前の cut の定義があればそれを使う (手組みの div に替えない — 隣の cut と見た目が揃わなくなる)。新しい台が要るなら def にする。要素の名の接頭辞 (`{name}` の cut の名) は保つ。
変えてよい事: 要素の追加と削除 (絵・図・板・札・判子・締めの 1 文)、大きさ・色・位置・下地、印の位置と動き、絵の説明文、`lint off=規則` (意図した先出しなど)。
絵の説明文を書き換えるのはこの段だけ — この後の直し役は変えない (絵はこの版から作り始める・あなたは生成された絵を見られないので、文字を置く所は `subject:` / `room:` で空ける)。
箱の書き方: 板は div (子は字下げで親の内側から置く・親の内側は border と padding の分だけ狭く、kb の絵は箱を越え、長い文字は折れる — 字数は check の目安を見る)。{persistent}
key は authoring の「型」の表にある物だけ (無い key は DEFECT で cut が落ちる)。`hug` は字幕専用。印 (`[>#名]` `[!#名 …]`) はこの cut の層にだけ付ける (他の cut の層は不可)。
返す前に見直す 4 つ (DEFECT の常連): `"a;b"` の列は ×N の instance ごとの値 — その要素 (か def の呼び出し) の行末に `×N` が要る / 同じ key は 1 要素に 1 回 /
`名{{tok}}` の tok は空にしない / `to,{{…}}` に GSAP の位置の引数 (`,2`) は無い — 時刻は `+N` `-N` (例 `[!#a to,{{scale:1.1}} +300]`) /
`filter` の look は全掛けの `sepia(1)` `grayscale(1)` `invert(1)` だけ (`sepia(.45)` は DEFECT)。

{STAFF_PITFALLS}

依頼 (この動画の依頼文 — 対象・必須の語・数字・締めの一言はこれに従う):
{request.strip() or "(なし)"}

{cut_place(name, order or [])}{length}
構成 (参考):
{plan}
根 (参考・変えない):
=== root_design ===
{root_d}
=== root_timeline ===
{root_t}
{"前の cut の定義 (参考・変えない・使ってよい):" + chr(10) + defs_before if defs_before.strip() else ""}
{prev}
check の指摘 (著者の版・参考。消す事が目的ではない。判定で損をする物だけ直す):
{findings or "(なし)"}
著者の版の時刻 (check の見積り — 秒は動画の頭から。印を動かせば変わる):
{timing.strip() or "(なし)"}

見直す block:
=== cut {name} ===
{block}
=== end ===

出力は見直した block だけを同じ形式で (前置き・説明・code fence は書かない。`=== cut {name} ===` から `=== end ===` まで)。
"""


def _numbered(text: str) -> str:
    return "\n".join(f"{k}| {line}" for k, line in enumerate(text.rstrip("\n").split("\n"), start=1))


def fix_prompt(
    name: str,
    block: str,
    findings: str,
    root_d: str,
    root_t: str,
    *,
    own_root: bool = False,
    defs_before: str = "",
    review: bool = False,
    shots: list[str] | None = None,
) -> str:
    """own_root = この cut が根の持ち主 (動画の最初の live な cut・根が流れる前) — 根の 2 block も直せる (`@ root_design 行`)。他の cut
    の直し役は根と前の cut の定義を変えない (参考として見るだけ)。review = 見直し (確認表で指摘に出ない崩れも探す・指摘が無くても呼ぶ)。
    shots = 見直しに見せる静止画の名 (無ければ block を読んで描いた姿を想像させる)。"""
    if own_root:
        root_part = f"""根 (この cut の持ち物 — 直してよい。ただし image・cast・read・photo_style・prompt_tail・art・canvas の行と、名のある定義の名は変えない):
=== root_design ===
{_numbered(root_d)}
=== root_timeline ===
{_numbered(root_t)}
"""
        where = "`@ 行番号` は cut の block の行・根の行は `@ root_design 行番号` / `@ root_timeline 行番号`"
    else:
        root_part = f"""根 (参考・変えない — 根の行の指摘はこの cut の行で避ける):
=== root_design ===
{root_d}
=== root_timeline ===
{root_t}
"""
        where = "`@ 行番号` は cut の block の行だけ (根・前の cut は変えられない — 前の cut の定義が合わなければ自分の block に別の名で定義して使う)"
    defs = f"前の cut の定義 (参考・変えない・使ってよい):\n{defs_before}\n" if defs_before.strip() else ""
    look = ""
    if review or shots:
        if shots:
            names = "・".join(shots)
            intro = f"""画像はこの cut を本番の renderer で描いた静止画です ({names}・時刻は cut 頭から。動画素材と立ち絵は止まった姿・口は閉じたまま・
切替の窓は写らない)。check の指摘とは別に、画像を 1 枚ずつ見て、見る人が「未完成・崩れている」と感じる所を探して直す。"""
        else:
            intro = "check の指摘とは別に、block を読んで、描いた時に見る人が「未完成・崩れている」と感じる所を想像して探して直す。"
        look = f"""
{intro}必ず次を確かめる:
- 空き: 板・枠・画面に中身の無い面が大きく残っていないか (板の下半分が空・cut の頭に見出しだけの板・画面の片側だけに寄って反対側が空)。
  中身を大きくする・板を中身に合わせて縮める・置き場を変える・空いた面に図や札を置く
- 揃い: 並んだ要素が中央や軸からずれていないか (左右の余白が違う・行の頭が揃わない)
- 重なり・読みやすさ: 文字が絵・他の文字・字幕に重なる・背景に沈む・小さすぎる
- 主体: 絵の主体 (顔・物) が文字や板の下に隠れる・切れる
- 場面との食い違い: 絵の中身が台詞と合わない (説明文は変えられない — 置き方・大きさ・幕・入れ替えで避ける)
配置は大きく組み替えてよい (行の置き換え・追加・削除。台詞の文字と絵の説明文だけは変えない)。
まず `=== look ===` に{"画像ごとに" if shots else ""}見つけた崩れを 1 行ずつ (無ければ「なし」) 書き、続けて edits を書く。直す所が無ければ
`=== edits ===` の直後に `=== end ===`。
"""
    head = (
        f"cut `{name}` の block に check の指摘が出ました。"
        if findings.strip() or not look
        else f"cut `{name}` の block を見直して、崩れがあれば直してください (check の指摘はありません)。"
    )
    return f"""{head}直す行だけを返してください (block 全体は書き直さない — 書く時間がそのまま再生の待ちになる)。他の cut は変えない。前置きは書かない{" (`=== look ===` は書く)" if look else ""}。
変えない物 (声と絵はもう作り始めている — 変えると作り直しで再生が待つ): 台詞の文字 (`@` の行の、印 `[…]` を除いた文字。印は動かしてよい)・絵の説明文 (img の行の内容。宣言は直してよい・絵を足すのは可)。
形式:
=== edits ===
@ 行番号
その行の新しい中身 (複数行にしてよい・行を消すなら空のまま次の `@` へ)
@ 行番号
…
=== end ===
{where}。block の末尾に行を足すなら `@ 最後の行番号+1`。行番号は下の `N|` の物 (指摘の file:行 は 根 + cut の順に並べた design.txt / timeline.txt の行で、別物)。`N|` は番号で、行の中身ではない。
直しが新しい欠陥を作らないために: 印で使う変種 (`[!#名 .tag]`) は design にその `#名.tag(…)` の行がある物だけ・`size=` は文字と icon だけ (箱は w= h=)・
1 行 1 要素のまま (要素の行を途中で割らない・字下げの子は親の直後)。
{look}check の指摘 (file:行 と直し方つき):
{findings or "なし"}

{root_part}{defs}
直す block:
=== cut {name} ===
{_numbered(block)}
=== end ===
"""


def _without_marks(line: str) -> str:
    """台詞の行から印 `[…]` を外す (`[!#c[*] …]` のような入れ子の `]` も 1 つの印として)。"""
    out, depth = [], 0
    for ch in line:
        if ch == "[":
            depth += 1
        elif ch == "]" and depth:
            depth -= 1
        elif not depth:
            out.append(ch)
    return "".join(out).strip()


_SPEAKER = re.compile(r"^\s*@[^:\s\[]*:")  # 台詞の行の頭 `@n:` / `@:`
_READING = re.compile(r"\{([^{}|]*)\|[^{}]*\}")  # 読みの指定 `{表記|読み}`


def spoken(line: str) -> str:
    """台詞の行の声になる文字 — 話者・印 `[…]`・読点 `、。`・読みの指定 (`{表記|読み}` は表記に)・空白を除く。担当と直し役が台詞を
    変えたかの比較はこれで見る (読点の追加と読みの指定は変えた事にしない)。"""
    body = _READING.sub(r"\1", _without_marks(_SPEAKER.sub("", line, count=1)))
    return re.sub(r"[、。\s]", "", body)


def _split_marks(body: str) -> tuple[str, list[tuple[int, str]]]:
    """台詞の本文を (印を除いた文字, [(文字の中の位置, 印)]) に割る (`_without_marks` と同じ入れ子の数え方)。"""
    bare: list[str] = []
    marks: list[tuple[int, str]] = []
    depth, cur = 0, ""
    for ch in body:
        if ch == "[" or depth:
            cur += ch
            depth += 1 if ch == "[" else -1 if ch == "]" else 0
            if not depth:
                marks.append((len(bare), cur))
                cur = ""
            continue
        bare.append(ch)
    return "".join(bare), marks


def _author_words_staff_marks(staff_line: str, author_line: str) -> str:
    """著者の行の話者と文字に、担当の行の印を載せる。印の位置は担当の文字と著者の文字の対応 (difflib) で写す — 同じ文字の上の印は
    同じ文字の前に、書き換えた区間の印はその区間の頭に (読みの指定 `{…}` の中には置かない)。"""
    import difflib  # noqa: PLC0415

    m_a, m_s = _SPEAKER.match(author_line), _SPEAKER.match(staff_line)
    head, body_a = (author_line[: m_a.end()], author_line[m_a.end() :]) if m_a else ("", author_line)
    bare_s, marks = _split_marks(staff_line[m_s.end() :] if m_s else staff_line)
    bare_a, _ = _split_marks(body_a)
    ops = difflib.SequenceMatcher(None, bare_s, bare_a, autojunk=False).get_opcodes()
    braces = [(m.start(), m.end()) for m in re.finditer(r"\{[^{}]*\}", bare_a)]

    def at(k: int) -> int:
        j = next((j1 + (k - i1 if tag == "equal" else 0) for tag, i1, i2, j1, _j2 in ops if i1 <= k < i2), len(bare_a))
        return next((a for a, b in braces if a < j < b), j)

    placed = sorted(((at(k), n, mark) for n, (k, mark) in enumerate(marks)), key=lambda x: (x[0], x[1]))
    out, last = [], 0
    for j, _n, mark in placed:
        out += [bare_a[last:j], mark]
        last = j
    return head + "".join(out) + bare_a[last:]


def restore_speech(author: str, staff: str) -> tuple[str, list[dict[str, str]]]:
    """担当の block の台詞 (`@` の行) を著者の版の文字に戻す → (戻した block, 戻した行の記録)。比べるのは `spoken` (読点の追加と読みの
    指定は許す)。台詞の行の数が同じ区間は行ごとに著者の文字へ担当の印を載せ (`marks`)、行を足した / 消した区間は著者の行ごと
    戻す (`author_line`・印も著者の物)。台詞の行の割り方だけ変えた (文字の並びは同じ) なら戻さない。声は担当の版から作るので、ここで
    戻さないと後段では戻せない。"""
    import difflib  # noqa: PLC0415

    def speech_rows(text: str) -> list[str]:  # timeline の台詞の行 (design の `@#名` は定義の見出し)
        return [l for l in text.split("---timeline---", 1)[-1].splitlines() if l.lstrip().startswith("@")]

    rows_a, rows_s = speech_rows(author), speech_rows(staff)
    norm_a, norm_s = [spoken(l) for l in rows_a], [spoken(l) for l in rows_s]
    if "".join(norm_a) == "".join(norm_s):
        return staff, []
    replace: dict[int, list[str]] = {}  # 担当の台詞の行の番号 → 置き換える行 (空 = 消す)
    insert: dict[int, list[str]] = {}  # 担当の台詞の行の番号 → その前に足す著者の行 (行の数 = 最後の台詞の行の後ろ)
    log: list[dict[str, str]] = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, norm_a, norm_s, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        if i2 - i1 == j2 - j1:
            for i, j in zip(range(i1, i2), range(j1, j2)):
                replace[j] = [_author_words_staff_marks(rows_s[j], rows_a[i])]
                log.append({"mode": "marks", "staff": norm_s[j][:80], "author": norm_a[i][:80]})
            continue
        insert.setdefault(j1, []).extend(rows_a[i1:i2])
        replace.update({j: [] for j in range(j1, j2)})
        log.append({"mode": "author_line", "staff": "".join(norm_s[j1:j2])[:80], "author": "".join(norm_a[i1:i2])[:80]})
    design, sep, timeline = staff.rpartition("---timeline---")
    out: list[str] = []
    k = 0
    for line in timeline.rstrip("\n").split("\n"):
        if line.lstrip().startswith("@"):
            out += insert.get(k, []) + replace.get(k, [line])
            k += 1
            if k == len(rows_s):
                out += insert.get(k, [])
        else:
            out.append(line)
    if not rows_s:  # 担当が台詞を全部消した — 著者の台詞を block の後ろに戻す
        out += insert.get(0, [])
    return design + sep + "\n".join(out) + "\n", log


def touched_fixed(before: str, after: str) -> tuple[int, int]:
    """直し役が変えない約束の物 — 台詞の文字 (`spoken`) と絵の説明文 — を変えた数 (記録用。`fix_edits` の speech_changed / picture_changed)。"""

    def speech(text: str) -> list[str]:
        return [spoken(l) for l in text.split("---timeline---", 1)[-1].splitlines() if l.lstrip().startswith("@")]

    def pictures(text: str) -> list[str]:
        return [
            m.group(1).strip()
            for l in text.splitlines()
            if (m := re.match(r"^\s*img#\S+\((?:[^()]|\([^()]*\))*\)\s*(.*)$", l))
        ]

    sb, sa = speech(before), speech(after)
    pb, pa = pictures(before), pictures(after)
    return sum(a != b for a, b in zip(sb, sa)) + abs(len(sb) - len(sa)), sum(p not in pb for p in pa)


def parse_edits(text: str, blocks: dict[str, str]) -> tuple[dict[str, dict[int, list[str]]] | None, list[str]]:
    """直し役の `=== edits ===` を block ごと (`@ 行番号` = cut・`@ root_design 行番号` …) の行番号 → 新しい中身に読む
    → (edits, 捨てた `@` の行)。`@ 行数+1` は block の末尾に足す edit (nt10 hook の transition 行)。知らない block・それより外の行番号の
    edit はその 1 つだけ捨てて残りを当てる (1 つの範囲外で正しい edit まで捨てない)。edits が無い・当てる edit が 1 つも無ければ None。"""
    m = re.search(r"===\s*edits\s*===\s*\n(.*?)(?:\n===\s*end\s*===|\Z)", text, re.S)
    if m is None:
        return None, []
    sizes = {name: len(body.rstrip("\n").split("\n")) for name, body in blocks.items()}
    edits: dict[str, dict[int, list[str]]] = {name: {} for name in blocks}
    dropped: list[str] = []
    current: list[str] | None = None
    for raw in m.group(1).split("\n"):
        head = re.match(r"^@\s*(?:([A-Za-z_]+)\s+)?(\d+)\s*$", raw)
        if head:
            target = head.group(1) or "cut"
            n = int(head.group(2))
            if target not in sizes or not 1 <= n <= sizes[target] + 1:
                dropped.append(raw.strip())
                current = None  # 捨てた edit の中身の行も読み飛ばす
                continue
            current = edits[target].setdefault(n, [])
            continue
        if current is not None:
            current.append(re.sub(r"^\d+\|\s?", "", raw))  # 番号を写してしまった行は剥がす
    return (edits if any(edits.values()) else None), dropped


def apply_line_edits(body: str, edits: dict[int, list[str]]) -> str:
    """行番号 → 新しい中身 (空 = 行を消す) を当てる。行数+1 の edit は末尾に足す。"""
    lines = body.rstrip("\n").split("\n")
    out: list[str] = []
    for k, line in enumerate([*lines, None], start=1):
        if k in edits:
            new = edits[k]
            while new and new[-1] == "":
                new = new[:-1]
            out.extend(new)
        elif line is not None:
            out.append(line)
    return "\n".join(out) + "\n"


class Splitter:
    """stream の本文を `=== … ===` と `section#` / `*** ` の境目で section に割り、閉じた順に solo/ へ書く。"""

    def __init__(self, proj: Path, st: Path, tag: str) -> None:
        self.proj, self.st, self.tag = proj, st, tag
        self.buf = ""
        self.sec: tuple[str, str | None] | None = None
        self.lines: list[str] = []
        self.sep = False
        self.out: dict[str, str] = {}
        self.order: list[str] = []

    def feed(self, text: str) -> None:
        self.buf += text
        while "\n" in self.buf:
            line, self.buf = self.buf.split("\n", 1)
            self.line(line)

    def line(self, line: str) -> None:
        if FENCE.match(line):
            return
        m = MARK.match(line)
        if m:
            self.close()
            name = m.group(1)
            if name == "end":
                self.sec = None
                return
            self.sec = ("cut", m.group(2)) if m.group(2) else (name, None)
            self.lines, self.sep = [], False
            return
        mc = CUTHEAD.match(line)
        if mc and (self.sec is None or self.sec[0] != "cut" or self.sec[1] != mc.group(1) or self.sep):
            self.close()
            self.sec, self.lines, self.sep = ("cut", mc.group(1)), [line], False
            return
        if (
            self.sec
            and self.sec[0] == "cut"
            and not self.sep
            and (line.strip() == "---timeline---" or TLHEAD.match(line))
        ):
            self.sep = True
            self.lines.append("---timeline---")
            if line.strip() == "---timeline---":
                return
        if self.sec:
            self.lines.append(line)

    def close(self) -> None:
        if not self.sec:
            return
        kind, name = self.sec
        body = "\n".join(self.lines).strip("\n") + "\n"
        if kind == "cut":
            if "---timeline---" not in body:
                body += "---timeline---\n"
            key, f = f"cut_{name}", self.proj / f"cut_{name}.txt"
            if name not in self.order:
                self.order.append(name)
        else:
            key, f = kind, self.proj / f"{kind}.txt"
        tmp = f.with_suffix(".tmp")
        tmp.write_text(body)
        os.replace(tmp, f)
        self.out[key] = body
        log(self.st, event="section_out", section=key, chars=len(body), tag=self.tag)
        if kind == "plan":  # 構成が決まった時点で cut の順を出す — orchestrator は cut が届くのを待ち始める
            names = [n for n, _ in plan_names(body)]
            tmp = self.proj / "order.tmp"
            tmp.write_text("\n".join(names) + "\n")
            os.replace(tmp, self.proj / "order.txt")
            log(self.st, event="plan", cuts=names)
        self.sec, self.lines = None, []

    def finish(self) -> None:
        if self.buf:
            self.line(self.buf)
            self.buf = ""
        self.close()


def claude_args(system_prompt: Path, *, effort: str, json_input: bool = False) -> list[str]:
    return [
        claude_bin(),
        "-p",
        "--verbose",
        *(["--input-format", "stream-json"] if json_input else []),  # 画像を渡す時は user message を JSON で
        "--output-format",
        "stream-json",
        "--include-partial-messages",
        "--model",
        MODEL,
        "--effort",
        effort,
        "--tools",
        "",
        "--disable-slash-commands",
        # 起動を軽くする: claude.ai の MCP connector と settings の hook / plugin を読まない (init まで 4.1 → 3.5 s・10-18 実測。
        # `--bare` は OAuth で使えない)。system prompt は file で渡すので settings は要らない
        "--strict-mcp-config",
        "--mcp-config",
        '{"mcpServers":{}}',
        "--setting-sources",
        "",
        "--system-prompt-file",
        str(system_prompt),
    ]


def image_message(prompt: str, images: list[Path]) -> str:
    """画像 (幅 SHOT_WIDTH の JPEG に縮める) + prompt の user message 1 つ (`--input-format stream-json` の 1 行)。"""
    import base64
    import io

    from PIL import Image

    content: list[dict[str, object]] = []
    for path in images:
        image = Image.open(path).convert("RGB")
        image.thumbnail((SHOT_WIDTH, SHOT_WIDTH))
        buf = io.BytesIO()
        image.save(buf, "JPEG", quality=85)
        data = base64.b64encode(buf.getvalue()).decode()
        content.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": data}})
    content.append({"type": "text", "text": prompt})
    return json.dumps({"type": "user", "message": {"role": "user", "content": content}}, ensure_ascii=False) + "\n"


def stream_claude(
    st: Path,
    prompt: str,
    on_text,
    *,
    system_prompt: Path,
    effort: str,
    tag: str,
    cache_ttl: str | None = None,
    images: list[Path] | None = None,
) -> dict[str, object]:
    """claude -p を stream-json で回し、text delta を on_text に流す。最初の thinking / text の時刻と費用を記録する。
    images = prompt の前に見せる画像 (見直し役の cut の静止画)。
    text delta が 1 つも来ずに終わった応答 (長い思考の後、本文が最後の assistant message にだけ乗る — now7_10 の担当 hook・246 s で
    delta 0) は、最後の assistant message の text の block を本文として流す (`text_from_message`)。"""
    CWD.mkdir(parents=True, exist_ok=True)
    # prompt は stdin で渡す (argv だと見本 2 本で 120 KB を超えた時に E2BIG「Argument list too long」で著者が起動できない)
    args = claude_args(system_prompt, effort=effort, json_input=bool(images))
    raw = (st / f"claude_{tag}.jsonl").open("a")
    t0 = time.time()
    first: dict[str, float] = {}
    # ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN は claude.ai の login より優先されるので外す — dev container の環境に key が
    # あると subscription でなくその key で呼ばれ、枠が無ければ 0 token の応答 + exit 1 で著者が黙って死ぬ (cut 0 になる)
    drop = ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")
    env = {k: v for k, v in os.environ.items() if k not in drop}
    if cache_ttl is not None:
        env["CLAUDE_CODE_PROMPT_CACHE_TTL"] = cache_ttl
    for attempt in range(3):  # shim が自動更新の瞬間に消える → 2 秒おいて実体を引き直す
        try:
            p = subprocess.Popen(
                args,
                cwd=CWD,
                env=env,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=(st / f"claude_{tag}.err").open("a"),
                text=True,
            )
            break
        except FileNotFoundError:
            log(st, event="claude_missing", tag=tag, attempt=attempt)
            if attempt == 2:
                raise
            time.sleep(2)
            args[0] = claude_bin()
    assert p.stdout is not None and p.stdin is not None
    p.stdin.write(image_message(prompt, images) if images else prompt)
    p.stdin.close()
    result: dict[str, object] = {}
    chars = 0
    # 最後の assistant message の id と text の block (stream-json は block ごとに同じ id の `assistant` 行を 1 つずつ出す)
    last_id: object = None
    last_text: list[str] = []
    for line in p.stdout:
        raw.write(line)
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("type") == "stream_event":
            e = r.get("event", {})
            if e.get("type") == "content_block_delta":
                d = e.get("delta", {})
                if d.get("type") == "thinking_delta" and "thinking" not in first:
                    first["thinking"] = time.time()
                    log(st, event="first_thinking", tag=tag, s=round(first["thinking"] - t0, 1))
                if d.get("type") == "text_delta":
                    if "text" not in first:
                        first["text"] = time.time()
                        log(st, event="first_text", tag=tag, s=round(first["text"] - t0, 1))
                    chars += len(d.get("text", ""))
                    on_text(d.get("text", ""))
        elif r.get("type") == "assistant":
            msg = r.get("message", {})
            if msg.get("id") != last_id:
                last_id, last_text = msg.get("id"), []
            last_text += [b.get("text", "") for b in msg.get("content", []) if b.get("type") == "text"]
        elif r.get("type") == "result":
            result = r
    p.wait()
    if chars == 0 and "".join(last_text):
        body = "".join(last_text)
        chars = len(body)
        log(st, event="text_from_message", tag=tag, chars=chars)
        on_text(body)
    raw.close()
    if p.returncode != 0 and chars == 0:  # 黙って死んだ著者の理由は .err の 1 行目にある (login / 枠など)
        err = (st / f"claude_{tag}.err").read_text(encoding="utf-8", errors="replace").strip().splitlines()
        log(st, event="claude_failed", tag=tag, exit=p.returncode, err=err[-1][:200] if err else None)
    log(
        st,
        event="stream_end",
        tag=tag,
        s=round(time.time() - t0, 1),
        chars=chars,
        exit=p.returncode,
        cost=result.get("total_cost_usd"),
        session=result.get("session_id"),
        write_s=round(time.time() - first["text"], 1) if "text" in first else None,
    )
    return result


def stream_model(
    st: Path,
    prompt: str,
    on_text: Callable[[str], None],
    *,
    system_prompt: Path,
    effort: str,
    tag: str,
    cache_ttl: str | None = None,
    images: list[Path] | None = None,
) -> dict[str, object]:
    """制御と原稿形式は共通にし、明示された実行エンジンだけを切り替える。"""
    engine = os.environ.get("NOLANG_STUDIO_ENGINE", "claude")
    if engine == "claude":
        return stream_claude(
            st, prompt, on_text, system_prompt=system_prompt, effort=effort, tag=tag, cache_ttl=cache_ttl, images=images
        )
    if engine != "codex":
        raise ValueError(f"unknown studio engine: {engine}")
    from stream_codex import stream_codex

    try:
        stream_codex(st, prompt, on_text, system_prompt=system_prompt, effort=effort, tag=tag, images=images)
    except BaseException as exc:
        failure = st / f"engine.failed.{tag}.tmp"
        failure.write_text(f"{tag}: {type(exc).__name__}: {exc}\n")
        failure.replace(st / "engine.failed")
        raise
    return {}


def warmup(st: Path, system_prompt: Path) -> None:
    """担当・直し役の system prompt (見本込み・84〜105k token) を著者の call と並んで 1 回だけ cache に書く。担当は cut が出始めると
    数秒差で 2 本以上起動し、まだ書けていないとそれぞれが全量を書く (nt03 は 2 本で $1.71 / nt04・nt10 も同じ)。著者が書いている間に
    prefill が終わるので、最初の担当から読める。失敗しても run は止めない (担当が自分で書くだけ)。"""
    t0 = time.time()
    try:
        result = stream_claude(
            st,
            "準備の呼び出しです。「ok」とだけ返してください。",
            lambda _t: None,
            system_prompt=system_prompt,
            effort="low",
            tag="warmup",
        )
    except OSError as e:
        log(st, event="warmup_failed", s=round(time.time() - t0, 1), error=repr(e)[:200])
        return
    usage = result.get("usage")
    log(
        st,
        event="warmup",
        s=round(time.time() - t0, 1),
        cost=result.get("total_cost_usd"),
        cache_write=usage.get("cache_creation_input_tokens") if isinstance(usage, dict) else None,
        cache_read=usage.get("cache_read_input_tokens") if isinstance(usage, dict) else None,
    )


def plan_names(plan_text: str) -> list[tuple[str, float]]:
    out: list[tuple[str, float]] = []
    for l in plan_text.splitlines():
        if ":" not in l or l.startswith("#"):
            continue
        name = l.split(":", 1)[0].strip()
        secs = re.findall(r"\((\d+(?:\.\d+)?)", l)  # 見込み秒は行の最後の `(数` (見せ物の中の `(3 つ` を秒と読まない)
        out.append((name, float(secs[-1]) if secs else 10.0))
    return out


def run(project: Path, *, effort: str, samples: tuple[str, ...] | None) -> int:
    proj, st, studio = project / "solo", project / "stream", project / "studio"
    proj.mkdir(exist_ok=True)
    st.mkdir(exist_ok=True)
    typ, aspect, seconds = (project / "params.txt").read_text().split()
    request = (project / "request.txt").read_text()
    if samples is None:
        samples, skipped = pick_samples(typ, aspect, request)
    else:  # 明示の見本はそのまま使う (同じ題材なら記録だけ)
        skipped = []
        if same := [n for n in samples if same_topic(n, request)]:
            log(st, event="samples_same_topic", samples=same)
    # 担当・直し役の system prompt (見本込み — 同じ見本の run どうしで cache を共有する)。著者の call と並んで 1 回だけ温める
    shared_prompt = build_system_prompt(st / "system_prompt.md", samples)
    warm = None
    if os.environ.get("NOLANG_STUDIO_ENGINE", "claude") == "claude":
        warm = threading.Thread(target=warmup, args=(st, shared_prompt), daemon=True)
        warm.start()
    # 著者の system prompt は見本を含めない静的な物 — 見本は題材ごとに変わるので system に置くと動画ごとに 85〜95k token が
    # cache miss になる (o20 / o21 の著者は cache read 0)。見本は user turn の末尾 (依頼の前) に同じ内容で置く (10-18)
    sp = build_system_prompt(st / "system_prompt_author.md", None)
    (st / "samples.txt").write_text(",".join(samples) + "\n")  # fix / fix-root も同じ見本で
    skeleton_d, skeleton_t = (studio / "design.txt").read_text(), (studio / "timeline.txt").read_text()
    if not request.lstrip().startswith("---- ユーザーの依頼 ----"):
        request = "---- ユーザーの依頼 ----\n" + request.rstrip("\n") + "\n---- ここまで ----\n"
    log(
        st,
        event="launch",
        type=typ,
        aspect=aspect,
        seconds=seconds,
        effort=effort,
        samples=list(samples),
        samples_skipped=skipped,
    )
    prompt = author_prompt(typ, aspect, seconds, skeleton_d, skeleton_t, request, samples_text(samples))
    sp0 = Splitter(proj, st, "author")
    stream_model(st, prompt, sp0.feed, system_prompt=sp, effort=effort, tag="author")
    sp0.finish()
    if os.environ.get("NOLANG_STUDIO_ENGINE", "claude") == "claude":
        (st / "src.done").touch()
    if warm is not None:
        warm.join(timeout=30)  # warmup の記録を残してから終わる (著者の call の方が長いので普通は終わっている)
    if not all((proj / f).exists() for f in ("order.txt", "root_design.txt", "root_timeline.txt")):
        log(st, event="root_failed", have=sorted(p.name for p in proj.iterdir()))
        return 1
    if os.environ.get("NOLANG_STUDIO_ENGINE") == "codex":
        (st / "src.done").touch()
    log(st, event="src_done", cuts=sp0.order)
    return 0


def _emit_block(st: Path, name: str, text: str, *, event: str) -> int:
    """著者 / 直し役 / 担当の出力から cut の block を切り出して stdout へ (見出し無し・fence 付きも受ける)。"""
    m = re.search(r"===\s*cut\s+" + re.escape(name) + r"\s*===\s*\n(.*?)(?:\n===\s*end\s*===|\Z)", text, re.S)
    if m:
        body = m.group(1)
    else:
        # 見出し無しで `section#名` から書き始める著者もいる → `=== end ===` と code fence を剥がして全部を block とする
        body = re.sub(r"^\s*```.*$", "", text, flags=re.M)
        body = re.sub(r"===\s*end\s*===.*$", "", body, flags=re.S)
        ms = re.search(r"^section#", body, re.M)
        if ms is None:
            log(st, event=event, cut=name, chars=len(text))
            return 1
        body = body[ms.start() :]
    body = body.strip("\n") + "\n"
    if "---timeline---" not in body:
        # 印無しで timeline が始まる形も受ける
        mt = re.search(r"^\*\*\* ", body, re.M)
        body = body[: mt.start()] + "---timeline---\n" + body[mt.start() :] if mt else body + "---timeline---\n"
    sys.stdout.write(body)
    return 0


def defs_before_text(proj: Path, name: str) -> str:
    """cut `name` より前の cut の block (と壊れた cut から残した `defs_<cut>.txt`) にある名のある定義の行 (字下げの子も) — 担当・直し役の
    参考 (orchestrator が `defs_before_<name>.txt` に書く。無ければ空)。"""
    path = proj / f"defs_before_{name}.txt"
    return path.read_text() if path.exists() else ""


def fix(
    project: Path,
    name: str,
    findings_file: Path,
    *,
    own_root: bool = False,
    effort: str,
    review: bool,
    shots: list[Path],
) -> int:
    """直し役。own_root = この cut が根の持ち主 (最初の live な cut・根が流れる前) — 根の 2 file も直せる (`@ root_design 行`) 。
    review = 見直し (確認表で指摘に出ない崩れも探す)・shots = 見直しに見せる cut の静止画。"""
    proj, st = project / "solo", project / "stream"
    sp = st / "system_prompt.md"
    root_d, root_t = (proj / "root_design.txt").read_text(), (proj / "root_timeline.txt").read_text()
    block = (proj / f"cut_{name}.txt").read_text()
    out: list[str] = []
    stream_model(
        st,
        fix_prompt(
            name,
            block,
            findings_file.read_text(),
            root_d,
            root_t,
            own_root=own_root,
            defs_before=defs_before_text(proj, name),
            review=review,
            shots=[path.stem for path in shots],
        ),
        out.append,
        system_prompt=sp,
        effort=effort,
        tag=f"{'look' if shots else 'review' if review else 'fix'}_{name}",
        # 直し役の prompt は system prompt (担当と同じ file・担当が 1 時間の cache に書いた物を読む) の後ろが毎回変わる (cut・指摘)。
        # その末尾も cache に書かれ 2 度と読まれないので、書き込みを 1 時間 (入力の 2 倍) でなく 5 分 (1.25 倍) にする
        cache_ttl="5m",
        images=shots,
    )
    text = "".join(out)
    blocks = {"cut": block, **({"root_design": root_d, "root_timeline": root_t} if own_root else {})}
    edits, dropped = parse_edits(text, blocks)
    if dropped:
        log(st, event="fix_edits_dropped", cut=name, edits=dropped)
    if edits is None and not dropped and re.search(r"===\s*edits\s*===\s*\n\s*===\s*end\s*===", text):
        # 直す所が無い (見直しで崩れが無かった) — block をそのまま返す
        log(st, event="fix_no_edits", cut=name)
        sys.stdout.write(block)
        return 0
    if edits is not None:
        edited = apply_line_edits(block, edits["cut"]) if edits["cut"] else block
        if "---timeline---" not in edited:
            edited = block
        for root_name in ("root_design", "root_timeline"):
            if edits.get(root_name):
                new_root = apply_line_edits(blocks[root_name], edits[root_name])
                if new_root.strip():
                    (proj / f"{root_name}.txt").write_text(new_root)
                    log(st, event="fix_root_edits", cut=name, block=root_name, lines=sorted(edits[root_name]))
        speech, pictures = touched_fixed(block, edited)
        log(st, event="fix_edits", cut=name, chars=len(text), speech_changed=speech, picture_changed=pictures)
        sys.stdout.write(edited)
        return 0
    return _emit_block(st, name, text, event="fix_unparsed")  # block 全体を返した出力もそのまま受ける


def staff(project: Path, name: str, findings_file: Path, *, effort: str) -> int:
    """担当: 判定役の 8 観点で cut を見直して書き直す (前の cut は著者の版を参考に渡す = cut ごとに並列に走らせるため)。依頼文・cut の
    位置・著者の版の時刻 (orchestrator が指摘の隣に置く `timing_author.txt`) も渡す。"""
    proj, st = project / "solo", project / "stream"
    sp = st / "system_prompt.md"
    root_d, root_t = (proj / "root_design.txt").read_text(), (proj / "root_timeline.txt").read_text()
    plan = (proj / "plan.txt").read_text()
    block = (proj / f"cut_{name}.txt").read_text()
    order = [l.strip() for l in (proj / "order.txt").read_text().splitlines() if l.strip()]
    prev_name = order[order.index(name) - 1] if name in order and order.index(name) > 0 else None
    prev_block = None
    if prev_name:
        for cand in (proj / f"author_cut_{prev_name}.txt", proj / f"cut_{prev_name}.txt"):
            if cand.exists():
                prev_block = cand.read_text()
                break
    findings = findings_file.read_text() if findings_file.exists() else ""
    timing_file = findings_file.with_name("timing_author.txt")
    # 動画の長さの門 = plan の見込み秒の和 (orchestrator の進行線の total と同じ値)
    planned_s = sum(sec for _, sec in plan_names(plan))
    _typ, _aspect, target_s = (project / "params.txt").read_text().split()
    out: list[str] = []
    stream_model(
        st,
        staff_prompt(
            name,
            block,
            findings,
            root_d,
            root_t,
            plan,
            prev_name,
            prev_block,
            planned_s,
            defs_before_text(proj, name),
            request=(project / "request.txt").read_text(),
            order=order,
            target_s=target_s,
            timing=timing_file.read_text() if timing_file.exists() else "",
        ),
        out.append,
        system_prompt=sp,
        effort=effort,
        tag=f"staff_{name}",
    )
    text = "".join(out)
    return _emit_block(st, name, text, event="staff_unparsed")


def main(argv: list[str]) -> int:
    if os.environ.get("NOLANG_STUDIO_ENGINE") == "codex":

        def interrupted(_signum: int, _frame: object) -> None:
            raise SystemExit(143)

        signal.signal(signal.SIGTERM, interrupted)
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, project = argv[0], Path(argv[1]).resolve()
    if cmd == "run":
        eff = argv[argv.index("--effort") + 1] if "--effort" in argv else "low"  # 質は担当 medium が運ぶ (s9 / s10)
        samples = None
        if "--samples" in argv:
            samples = tuple(x.strip() for x in argv[argv.index("--samples") + 1].split(",") if x.strip())
        return run(project, effort=eff, samples=samples)
    if cmd == "fix":
        eff = argv[argv.index("--effort") + 1] if "--effort" in argv else "low"
        shots = [Path(x) for x in argv[argv.index("--shots") + 1].split(",") if x] if "--shots" in argv else []
        return fix(
            project,
            argv[2],
            Path(argv[3]),
            own_root="--root" in argv,
            effort=eff,
            review="--review" in argv,
            shots=shots,
        )
    if cmd == "staff":
        eff = argv[argv.index("--effort") + 1] if "--effort" in argv else "medium"
        return staff(project, argv[2], Path(argv[3]), effort=eff)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

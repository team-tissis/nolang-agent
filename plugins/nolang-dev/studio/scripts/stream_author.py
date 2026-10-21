"""stream の著者 — Opus を Claude Code (`claude -p`・tool 無し) で呼び、本文の src を token の stream で受けて section が閉じた順に file に落とす。

著者は 1 call (`claude -p --output-format stream-json`・system prompt = skill の文書 + type の見本 2 本・既定 low):
  `=== plan ===` (cut 一覧) → `=== root_design ===` → `=== root_timeline ===` → `=== cut 名 ===` を構成の順に (design の block・`---timeline---`・
  timeline の block) → `=== end ===`。plan が閉じた時点で solo/order.txt を書く (orchestrator が cut を待ち始める)。
  low は書き始めるまで数秒で、書く速さ (約 180 字/s・1 cut 約 3.5 s) が再生より速いので、cut を分けて並行に書かせる理由が無い。質は cut ごとの
  担当 (medium) が運ぶ (docs/draft_src_v2/stream-evidence-261013.md s9 / s10)。1 人が全 cut を書くので、cut を跨ぐ名の衝突・型のばらつきも出ない。
直し (low) は stream_run.py が cut ごとに頼む (`fix` subcommand: block + check の指摘 → 直した block)。

usage (repo root から):
  python stream_author.py run  <project>   [--effort low] [--samples a.md,b.md]
      --samples = system prompt に同梱する見本 (reference/samples/ の file 名・2 本以上)。省略時は reference/samples/ の NoLang の src
                  `<type>_NN.md` 1 本 + hf max の写し `hf_<type>_*.md` 1 本 (どちらも依頼と同じ題材を外し、依頼と同じ向きの物を先に・pick_samples)。
                  stream/samples.txt に記録し fix も同じ見本を使う
  python stream_author.py staff <project> <cut> <findings>  [--effort medium]   # 担当: 8 観点で cut を見直して block を stdout へ
  python stream_author.py fix  <project> <cut 名> <findings file> [--root]   → stdout に直した block (--root = 根の 2 file も直す)
project = tmp/studio/<name>/ (request.txt・params.txt = "type aspect seconds"・studio/ = `new` の雛形)。
出力: project/stream/ (system_prompt.md・claude_*.jsonl・author.jsonl = 時刻の記録) と project/solo/ (plan.txt・order.txt・root_design.txt・root_timeline.txt・cut_<名>.txt)。
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
import unicodedata
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
    片側に 1 本も無ければもう片側の 2 本目を取る。NoLang の src は製品の文法で勝った書き方 (字幕・cut の組み方)、hf の写しは
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
    picked = nolang[:1] + hf[:1]
    picked += (nolang[1:] + hf[1:])[: 2 - len(picked)]
    if len(picked) < 2:
        raise SystemExit(f"reference/samples/ に {typ} ({NEAR_TYPE[typ]}) の見本が 2 本無い: {picked}")
    return (picked[0], picked[1]), skipped


def build_system_prompt(out: Path, samples: tuple[str, ...] | None) -> Path:
    """SKILL + looks + sounds + authoring + capabilities + 見本 2 本 (著者は file を読めないので全部同梱)。samples=None は見本なし
    (著者の静的な system prompt — 見本は user turn に置く)。"""
    head = (
        "あなたは HTML + CSS + GSAP で動画を作るプロの制作者です (scene の DOM を書き、class で見た目を揃え、GSAP の timeline で"
        "要素ごとの入場・状態変化・退場を打つ、いつもの作り方)。今回はその動画の設計図を NoLang の draft src (HTML / CSS / GSAP の圧縮形) で書きます。"
        "見た目 (色・書体・構図・動き) は題材からあなたが決めます。目標は、プロの制作会社が作った動画と並べて見劣りしない質です。\n"
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
    for name in samples or ():
        parts.append(f"\n<!-- ===== 見本 reference/samples/{name} ===== -->\n\n" + (SAMPLES_DIR / name).read_text())
    out.write_text("".join(parts))
    return out


def samples_text(samples: tuple[str, ...]) -> str:
    """見本 2 本の本文 (著者の user turn に置く・内容は system prompt に同梱していた物と同じ)。"""
    return "".join(
        f"\n<!-- ===== 見本 reference/samples/{name} ===== -->\n\n" + (SAMPLES_DIR / name).read_text()
        for name in samples
    )


def author_prompt(
    typ: str, aspect: str, seconds: str, skeleton_d: str, skeleton_t: str, request: str, samples: str = ""
) -> str:
    return f"""下の依頼の動画の src を書きます。まず構成 (plan) と根、続けて cut を構成の順に上から一度に書きます。書いた端から別の process が
cut ごとに check と描画を始めるので、書きながら前に戻って直さない。根に置く物は動画全体の設定だけ:
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
各 cut の design は要素が全部出た時の位置と大きさ、timeline は台詞と語の印 (`[>#名]` 出す・`[!#名 …]` 変える・`[<#名]` 消す)。cut の切替は前の cut の
timeline の最後の行に `transition …`。
要素の名は cut の名を頭に (`hook` の cut なら `hook_t`・`hook_img`)。根の物を除き、cut を跨いで同じ名を使わない。

雛形 (`new --type {typ} --aspect {aspect} --seconds {seconds}` の出力・根の形の参考・台詞と題材は架空の例):
--- design.txt ---
{skeleton_d}
--- timeline.txt ---
{skeleton_t}
{samples}{request}"""


STAFF_VIEW = """1. 同期: 要素がその語の瞬間に出るか (先に全部見えている・語より何秒も遅れる、はどちらも減点。答えを待つ ? の箱や前後の板もその語で)
2. メリハリ: 溜め → 組み上がる → 主役が立つ → 次へ、と動くか (次を待つ 1〜3 秒の間は溜めで良い)
3. 主役: その瞬間に見るべき 1 つが分かるか (大きさ・色・前の札を沈める・動き)。全部が同じ強さの札の列は弱い。
   構成の行の見せ物がその cut で一番大きく見えるか — 要の語 (数字・比べる 2 つ・結論) が板・札の中の 40px 以下の字なら
   stat / big の段 (根に無ければ大きな文字) に上げ、物 (道具・画面・通知) は icon か絵を画面の中ほどに大きく
4. 読みやすさ: 写真の上に直接置いた細い文字・小さな札は沈む。大きく太い字でも、絵の主な色と同じ系統の色なら沈む (全面の閃光の直後も同じ)
   — 文字の側に幕 (veil の `to:`・image の `scrim:` の向き) か板を敷く・絵を窓にして文字は地に置く (縁取りは最後の手段で blur の影)
5. 図と変化: 内容に合った図か、同じ絵を長く使い回していないか、状態の変化 (色・数字・位置) が見えるか。比べる 2 つや前後の値は
   片方ずつ語で出し、差は最後に大きく見せる (板を先に完成させない)。位置の小さなずれや揺れだけでは変化に見えない — 伸びる・数える・色が変わる・現れて消える
6. so what と締め: 場面の結論の一言は、その cut で一番大きな字で (縦 72px・横 64px 以上。pill・札・板の中の小さな字にしない)。
   最後の cut は結論か問いを画面の主役に (台詞が問いなら問いの文を見せる)。締めの無音の間にも 1 つ変化を (色を落とす・判子・名の札)
7. 連続性: 黒 frame (暗い絵に濃い黒の幕を重ねた、ほぼ黒い画面も同じ)・突然の消失・位置の飛びを作らない
8. 作り込み: 板と中身が一体で動くか (板は中身の 1 行目と同じ語で出す・空の板を 2 秒より長く見せない)・写真が素材として成立しているか・
   章札や判子など番組としての質感"""


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
) -> str:
    # 常設: 3 分未満の動画と最初の cut (再生開始の経路 — prompt を増やさない) は足さないだけ。3 分以上は根の常設の札への差し替えを許す
    persistent = (
        "常設の帯は足さない。"
        if planned_s < LONG_VIDEO_S or prev_name is None
        else f"常設の帯・飾りの header は足さない (常設は根の物だけ)。この動画は構成の見込みで {planned_s:.0f} 秒 (3 分以上) — 根の sticky の札"
        ' (累計・章番号・STEP) には、構成の行の値で `[!#名 text,"…"]` を当ててよい (その数字・章を言う語に・値は構成のとおり・著者の版にあれば残す)。'
    )
    prev = (
        f"前の cut `{prev_name}` (著者の版・参考。型を揃える。変えない):\n=== cut {prev_name} ===\n{prev_block}=== end ===\n"
        if prev_name and prev_block
        else "この cut は最初の cut。最初の語で 1 つ立て、続く語ごとに 1 つずつ組み上げて、問いか主張の一言を一番大きく見せる"
        " (題や空の箱を先に全部出して止めない)。\n"
    )
    return f"""あなたはこの動画のディレクターです。著者が書いた cut `{name}` の block を、視聴者として見たときの良さで見直し、必要なら作り替えて返してください。
見るのは画面が埋まる速さや情報の量ではなく、次の 8 つです:
{STAFF_VIEW}

守る事: 台詞 (`@` の行の文字) は一字も変えない (許すのは読点の追加と `{{表記|読み}}` の読みの指定だけ・依頼の台本の文言は声になる)。話者 (`@名:`) は保つ。
根 (palette・font・cast) と前の cut の定義 (def・motion・run) は変えない (使ってよい。この cut の block の定義は中身の見た目を変えてよいが、名と引数の形 (引数の並び・既定値) は変えない — 後の cut がその形で使っている。別の形が要るなら新しい名で定義する・新しい定義はこの block に書く)。要素の名の接頭辞 (`{name}` の cut の名) は保つ。
変えてよい事: 要素の追加と削除 (絵・図・板・札・判子・締めの 1 文)、大きさ・色・位置・下地、印の位置と動き、絵の説明文、`lint off=規則` (意図した先出しなど)。
絵の説明文を書き換えるのはこの段だけ — この後の直し役は変えない (絵はこの版から作り始める)。
箱の書き方: 板は div (子は字下げで親の内側から置く・親の内側は border と padding の分だけ狭く、kb の絵は箱を越え、長い文字は折れる — 字数は check の目安を見る)。{persistent}
key は types の表にある物だけ (無い key は DEFECT で cut が落ちる)。`hug` は字幕専用。印 (`[>#名]` `[!#名 …]`) はこの cut の層にだけ付ける (他の cut の層は不可)。
check の指摘 (参考。消す事が目的ではない。判定で損をする物だけ直す):
{findings or "(なし)"}

構成 (参考):
{plan}
根 (参考・変えない):
=== root_design ===
{root_d}
=== root_timeline ===
{root_t}
{"前の cut の定義 (参考・変えない・使ってよい):" + chr(10) + defs_before if defs_before.strip() else ""}
{prev}
見直す block:
=== cut {name} ===
{block}
=== end ===

出力は見直した block だけを同じ形式で (前置き・説明・code fence は書かない。`=== cut {name} ===` から `=== end ===` まで)。
"""


def _numbered(text: str) -> str:
    return "\n".join(f"{k}| {line}" for k, line in enumerate(text.rstrip("\n").split("\n"), start=1))


def fix_prompt(
    name: str, block: str, findings: str, root_d: str, root_t: str, *, own_root: bool = False, defs_before: str = ""
) -> str:
    """own_root = この cut が根の持ち主 (動画の最初の live な cut・根が流れる前) — 根の 2 block も直せる (`@ root_design 行`)。他の cut
    の直し役は根と前の cut の定義を変えない (参考として見るだけ)。"""
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
    return f"""cut `{name}` の block に check の指摘が出ました。直す行だけを返してください (block 全体は書き直さない — 書く時間がそのまま再生の待ちになる)。他の cut は変えない。前置きは書かない。
変えない物 (声と絵はもう作り始めている — 変えると作り直しで再生が待つ): 台詞の文字 (`@` の行の、印 `[…]` を除いた文字。印は動かしてよい)・絵の説明文 (img の行の内容。宣言は直してよい・絵を足すのは可)。
形式:
=== edits ===
@ 行番号
その行の新しい中身 (複数行にしてよい・行を消すなら空のまま次の `@` へ)
@ 行番号
…
=== end ===
{where}。行番号は下の `N|` の物 (指摘の file:行 は 根 + cut の順に並べた design.txt / timeline.txt の行で、別物)。`N|` は番号で、行の中身ではない。
直しが新しい欠陥を作らないために: 印で使う変種 (`[!#名 .tag]`) は design にその `#名.tag(…)` の行がある物だけ・`size=` は文字と icon だけ (箱は w= h=)・
1 行 1 要素のまま (要素の行を途中で割らない・字下げの子は親の直後)・同じ語で同じ要素を 2 回更新しない (2 回目は `+N` を前より大きく)。
check の指摘 (file:行 と直し方つき):
{findings}

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


def parse_edits(text: str, blocks: dict[str, str]) -> dict[str, dict[int, list[str]]] | None:
    """直し役の `=== edits ===` を block ごと (`@ 行番号` = cut・`@ root_design 行番号` …) の行番号 → 新しい中身に読む。edits が無い・
    知らない block・行番号が block の外なら None。"""
    m = re.search(r"===\s*edits\s*===\s*\n(.*?)(?:\n===\s*end\s*===|\Z)", text, re.S)
    if m is None:
        return None
    sizes = {name: len(body.rstrip("\n").split("\n")) for name, body in blocks.items()}
    edits: dict[str, dict[int, list[str]]] = {name: {} for name in blocks}
    current: list[str] | None = None
    for raw in m.group(1).split("\n"):
        head = re.match(r"^@\s*(?:([A-Za-z_]+)\s+)?(\d+)\s*$", raw)
        if head:
            target = head.group(1) or "cut"
            n = int(head.group(2))
            if target not in sizes or not 1 <= n <= sizes[target]:
                return None
            current = edits[target].setdefault(n, [])
            continue
        if current is not None:
            current.append(re.sub(r"^\d+\|\s?", "", raw))  # 番号を写してしまった行は剥がす
    return edits if any(edits.values()) else None


def apply_line_edits(body: str, edits: dict[int, list[str]]) -> str:
    lines = body.rstrip("\n").split("\n")
    out: list[str] = []
    for k, line in enumerate(lines, start=1):
        if k in edits:
            new = edits[k]
            while new and new[-1] == "":
                new = new[:-1]
            out.extend(new)
        else:
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


def claude_args(system_prompt: Path, *, effort: str) -> list[str]:
    return [
        claude_bin(),
        "-p",
        "--verbose",
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


def stream_claude(st: Path, prompt: str, on_text, *, system_prompt: Path, effort: str, tag: str) -> dict[str, object]:
    """claude -p を stream-json で回し、text delta を on_text に流す。最初の thinking / text の時刻と費用を記録する。
    text delta が 1 つも来ずに終わった応答 (長い思考の後、本文が最後の assistant message にだけ乗る — now7_10 の担当 hook・246 s で
    delta 0) は、最後の assistant message の text の block を本文として流す (`text_from_message`)。"""
    CWD.mkdir(parents=True, exist_ok=True)
    # prompt は stdin で渡す (argv だと見本 2 本で 120 KB を超えた時に E2BIG「Argument list too long」で著者が起動できない)
    args = claude_args(system_prompt, effort=effort)
    raw = (st / f"claude_{tag}.jsonl").open("a")
    t0 = time.time()
    first: dict[str, float] = {}
    # ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN は claude.ai の login より優先されるので外す — dev container の環境に key が
    # あると subscription でなくその key で呼ばれ、枠が無ければ 0 token の応答 + exit 1 で著者が黙って死ぬ (cut 0 になる)
    drop = ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT", "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN")
    env = {k: v for k, v in os.environ.items() if k not in drop}
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
    p.stdin.write(prompt)
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
    build_system_prompt(st / "system_prompt.md", samples)  # 担当・直し役の system prompt (見本込み・従来どおり)
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
    stream_claude(st, prompt, sp0.feed, system_prompt=sp, effort=effort, tag="author")
    sp0.finish()
    (st / "src.done").touch()
    if not all((proj / f).exists() for f in ("order.txt", "root_design.txt", "root_timeline.txt")):
        log(st, event="root_failed", have=sorted(p.name for p in proj.iterdir()))
        return 1
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


def fix(project: Path, name: str, findings_file: Path, *, own_root: bool = False) -> int:
    """直し役。own_root = この cut が根の持ち主 (最初の live な cut・根が流れる前) — 根の 2 file も直せる (`@ root_design 行`) 。"""
    proj, st = project / "solo", project / "stream"
    sp = st / "system_prompt.md"
    root_d, root_t = (proj / "root_design.txt").read_text(), (proj / "root_timeline.txt").read_text()
    block = (proj / f"cut_{name}.txt").read_text()
    out: list[str] = []
    stream_claude(
        st,
        fix_prompt(
            name,
            block,
            findings_file.read_text(),
            root_d,
            root_t,
            own_root=own_root,
            defs_before=defs_before_text(proj, name),
        ),
        out.append,
        system_prompt=sp,
        effort="low",
        tag=f"fix_{name}",
    )
    text = "".join(out)
    blocks = {"cut": block, **({"root_design": root_d, "root_timeline": root_t} if own_root else {})}
    edits = parse_edits(text, blocks)
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
    """担当: 判定役の 8 観点で cut を見直して書き直す (前の cut は著者の版を参考に渡す = cut ごとに並列に走らせるため)。"""
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
    # 動画の長さの門 = plan の見込み秒の和 (orchestrator の進行線の total と同じ値)
    planned_s = sum(sec for _, sec in plan_names(plan))
    out: list[str] = []
    stream_claude(
        st,
        staff_prompt(
            name, block, findings, root_d, root_t, plan, prev_name, prev_block, planned_s, defs_before_text(proj, name)
        ),
        out.append,
        system_prompt=sp,
        effort=effort,
        tag=f"staff_{name}",
    )
    text = "".join(out)
    return _emit_block(st, name, text, event="staff_unparsed")


def main(argv: list[str]) -> int:
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
        return fix(project, argv[2], Path(argv[3]), own_root="--root" in argv)
    if cmd == "staff":
        eff = argv[argv.index("--effort") + 1] if "--effort" in argv else "medium"
        return staff(project, argv[2], Path(argv[3]), effort=eff)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

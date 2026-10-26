"""stream の orchestrator — 著者 (stream_author.py・1 call) が落とす cut を出た順に check → 直し (低 effort の claude -p) → warm (絵・声) →
確定 → 投入。描画は製品の外部の著者の run (`authored_stream_run`) が seal ごとに HLS を伸ばす (cut 0 が seal された時点から再生
できる)。run は local ならこの機械の 1 process (`studio.py stream`・studio_stream.py)・remote なら NoLang の server。投入・先行解決
(warm)・check・改名・中断はどちらも nolang-api `drafts/` の同じ flow 関数を通る (`call` — remote は HTTP・local は `studio.py api`)。
cut の段は全 cut 同じで、orchestrator は cut の index でも local / remote でも分岐しない。

cut ごとの段 (全部 thread・cut ごとに並列):
  受け (前の cut が使う定義はそちらへ移す) → 著者版 check → 担当 (Opus medium) → check + 直し (2 回まで・担当の直後と最初の DEFECT 0 の
  check で warm を頼む) → staged (ready) → 投入 (構成の順・投入検査で弾かれた cut は直し役を 1 回・別枠)。
  直しきれない DEFECT は捨てる前に最後の手段 (著者版に差し替え → DEFECT の印を落として台詞を残す・last_resort) を掛ける。
根の規則: 名のある定義 (def・motion・run・svg・sound・image・cue) は初めて使う cut の block に書き、その cut だけが直す。根 (設定・cast・字幕と
BGM の開き・常設の層) の持ち主は最初の live な cut — その直し役だけが根を直し、根はその cut が受理された時に凍る。壊れた cut の定義は
次の live な cut の block へ移る。
cut を跨ぐ待ちは 投入の順・持ち主待ち (他の cut の行の DEFECT で check が止まった時だけ・相手は持ち主 1 つ) だけ。素材 (絵・声) は
run が warm の頼みで先に作る (頼んだ cut の check と直しは待たない)。

usage (repo root から): python stream_run.py <project> [--staff medium] [--staff-edits-assets] [--review low|medium|none] [--fix severe|defect|none|low] [--look]
  --remote http://host:18000 [--token nlg-c-…] = 投入先を NoLang API (製品の draft stream・server が描く) にする。視聴 URL を `WATCH …`
    の 1 行で出す (token は --token か env NOLANG_API_KEY・無ければ Claude Code が `/mcp` の OAuth で得た token)。
  --staff = 担当 (Opus・cut をプロの解説動画の密度と階層に仕上げる) を全 cut に、cut ごとに並列に (前の cut は著者の版を参考に渡す)。
  --review = 見直しの effort (既定 low・`medium` も可・`none` で見直しなし): 全 cut の 1 回目の直し役を、厳しい監督として
    指摘に出ない弱い所・崩れも探す見直しにする (指摘の無い cut も呼ぶ)。見直しの call は直し役の 2 回の上限に数えない。
  --fix = 直し役の範囲。既定 `severe` = DEFECT と severe の指摘 (隠れる文字・画面の外 …) だけ直し役 (low) を呼ぶ (見直しなし・warn は
    直さない — 担当後の severe は cut の 9% で、大半は担当が作る)。`defect` = DEFECT と隠れる文字 (severe の occluded) だけ。`none` = 直し役も
    呼ばない (DEFECT は機械の直しと最後の手段 — 著者の版・DEFECT の印を落とす — だけ)。`low` = 見直し (--review) と、指摘も直す直し役。
  担当は既定で絵 (説明文) と台詞を変えない (変えていれば著者の版に戻す)。絵と声は著者の cut が届いた時点で warm に頼み、担当と並列に
    作る。--staff-edits-assets = 担当が絵と台詞も変えてよい (素材は担当の版から・担当の後に作る)。
  既定 (担当 medium・素材は著者の版・DEFECT だけ直す) の根拠: 10-26 の 4 題材 bench で、担当 + 素材は著者の版 + 直しなしが、担当 + 見直し +
    直しに Opus 両順 3 勝 1 分・担当なしに 4 勝・最初の segment 中央 118 → 87 s (担当なし 70 s)・担当後の DEFECT 0/21 cut。DEFECT だけの
    直し役は、落ちる cut を減らす網 (DEFECT が無ければ呼ばれない)。
  --look = 見直しに cut の静止画も見せ、REVIEW_ROUNDS_LOOK (2) 回にする (local だけ・質を取りに行く mode — 速さの枠の外): 担当の後、
    prewarm の絵で cut を GPU で描き (`studio.py shots`)、round ごとに撮り直す。
  直し役に回す規則は製品の台帳 (`drafts/rules/` の fixed)。最後の cut 以外の doc は open_ended (後に cut が続く prefix) で check する。
記録: project/stream/run.jsonl (event ごとの時刻・製品の segment の時刻も)・最終 project/studio/out/video.mp4 と、流した doc を
studio/ (design.txt・timeline.txt・src.json) に書き戻した物。solo/ の cut は著者の版 author_cut_<名>・担当の版 staff_cut_<名>・最終
cut_<名>。
"""

from __future__ import annotations

import contextlib
import functools
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

HERE = Path(__file__).resolve().parent
# repo の中の skill なら自 repo の製品で描ける (local)。plugin で入れた skill (repo 無し) は --remote だけが動く
REPO = HERE.parents[3] if (HERE.parents[3] / "pyproject.toml").exists() else None
sys.path.insert(0, str(HERE))
if REPO is not None:
    sys.path.insert(1, str(REPO))

PY = sys.executable  # この script を動かしている python (repo は /opt/venv・plugin の client は使う側の python3)
STUDIO = HERE / "studio.py"


def _prefer_cpu() -> None:
    """stream の process を CPU で優先する (子 process の preexec)。権限が無ければ何もしない。"""
    try:
        os.nice(-10)
    except (PermissionError, OSError):
        pass


AUTHOR = HERE / "stream_author.py"
# cut の block の字下げ無しの行で定義される要素の名 (`img#cl_p(inset: 0; …)`・`kick#cl_k(…)`)。字下げの子 (`  p#l`) は親の名の下に付く
_TOP_DEF = re.compile(r"^([A-Za-z][\w-]*)#([A-Za-z0-9_]+)", re.M)
# 自動で改名する名: `_` か数字を含む物 (`cl_p`・`h2`)。`hd` `bar` のような短い名は根の物を意図して書いた事もあるので直し役に任せる
_RENAMABLE = re.compile(r"^[a-z]+(?:_[a-z0-9_]+|[0-9][a-z0-9_]*)$")
# grammar の予約 lane (`bg` `se` `subtitle`) と予約語 (LayerPath.reserved)。層の名に書くと DEFECT:NAME — 著者 / 担当が `div#bg` と
# 書いた根の 1 行で全 cut が直し役に回った (cur10_03: 5 回 × 15 s) ので、doc を組む時に機械で改名する (rename_collisions / normalize_root)
_RESERVED_NAMES = frozenset({"bg", "se", "subtitle", "cut", "screen", "self", "prev"})


def rows_naming_layers(text: str, layers: list[str]) -> tuple[set[int], int]:
    """text (cut の block) の中で層の名を指す行 (section の `#名(`・印の `#名`) の 0 始まりの行番号と、見つかった層の数。板の子の層
    (`板._board`・`板._text`) は板の名でも引く (板の出現の印は `[>#板]`)。子の名 (`板.k`) は自分の名だけ。"""
    lines = text.split("\n")
    rows: set[int] = set()
    hit = 0
    for layer in layers:
        names = {name for name in (layer, layer.split("._")[0]) if name and name != "-"}
        if not names:
            continue
        pattern = re.compile(r"#(?:" + "|".join(re.escape(name) for name in names) + r")(?![\w.])")
        found = {k for k, line in enumerate(lines) if pattern.search(line)}
        if found:
            rows |= found
            hit += 1
    return rows, hit


def cut_timing(check_out: str, cut: str) -> str:
    """check の出力から担当に渡す時刻の行を取る: 動画全体の `cut の見積り` と、cut の `scene の尺` と `出る時刻` の行 (見出しを頭に付ける)。"""
    keep: list[str] = []
    header = ""
    for line in check_out.splitlines():
        if line.startswith("  cut の見積り"):
            keep.append(line.strip())
        elif line.startswith("  ") and not line.startswith("    "):
            header = line.strip().split(" (", 1)[0].rstrip(":")
        elif line.startswith(f"    {cut}:") and header in ("scene の尺", "出る時刻"):
            keep.append(f"{header} — {line.strip()}")
    return "\n".join(keep)


def revert_changed_regions(before: str, after: str, bad: set[int]) -> str | None:
    """after (直し役の出力) のうち、bad (0 始まりの行番号) を含む変更の塊 (before との差分の塊) を before の行に戻した text。
    bad が変更の塊の外にしか無ければ None (直し役の変更が原因ではない)。"""
    import difflib  # noqa: PLC0415

    b_lines, a_lines = before.split("\n"), after.split("\n")
    out = list(a_lines)
    hit = False
    for tag, i1, i2, j1, j2 in reversed(difflib.SequenceMatcher(None, b_lines, a_lines, autojunk=False).get_opcodes()):
        if tag == "equal":
            continue
        # 消した塊 (j1 == j2) は境界の行が壊れる — その行も塊に含めて見る
        if any(j1 <= k < max(j2, j1 + 1) for k in bad):
            out[j1:j2] = b_lines[i1:i2]
            hit = True
    return "\n".join(out) if hit else None


# 直し役・見直しの 1 回の待ちの上限 — server は投入の行が 180 秒届かないと run を落とすので、その内側で諦めて直す前の版で続ける
FIX_TIMEOUT_S = 120
# 持ち込み音声の転写を待つ上限 (`drafts/speeches/` が ready になるまで — 1 時間の音声で数分) と問い合わせの間隔
SPEECH_WAIT_S = 15 * 60
SPEECH_POLL_S = 5
_CUT_HEAD = re.compile(r"^(?:section#[A-Za-z0-9_\-]+|\*\*\*\s+\S+)")


def cut_heads(block: str) -> list[str]:
    """cut の block の見出し (design の `section#名` と timeline の `*** 名` の行) の並び — 直し役は cut を分けない・改名しない。"""
    return [m.group(0).split("(")[0].strip() for line in block.splitlines() if (m := _CUT_HEAD.match(line))]


def edit_lines(now: str, fixed: str) -> str:
    """戻した直し役の edit の本文 (now = 戻した後の cut の text・fixed = 直し役の出力) — `+` は直し役が書いた行・`-` は今の行。"""
    import difflib  # noqa: PLC0415

    diff = difflib.unified_diff(now.split("\n"), fixed.split("\n"), lineterm="", n=0)
    return "\n".join(l for l in diff if l[:1] in "+-" and not l.startswith(("---", "+++")))


_SE = re.compile(r'\[♪"([^"]+)"')  # 台詞の効果音の説明 (warm の鍵)
_MARK_NOT_SE = re.compile(
    r"\[(?!♪)[^\[\]]*\]"
)  # 台詞行の印 (効果音の `[♪…]` を除く) — 先行 warm が DEFECT の印を落とす
# cut の block に書ける名のある定義 (grammar の CUT_DEFINITION_ROOTS) — 持ち主はその block の cut。字下げの子の行も定義の一部
_NAMED_DEF = re.compile(r"^(def|svg|sound|image|motion|run|cue)\s+([A-Za-z_][\w-]*)\b")
# 投入検査の render 文から editable_motion の的 (層の dotted path) と slot を引く (機械 degrade の的)
_EDITABLE_MOTION_RE = re.compile(
    r"DEFECT:editable_motion\b.*?#(?P<name>[\w.\[\]]+) の (?P<slot>motion_in|motion_out|motion_main|in|out|main)\b"
)
_MOTION_SLOT_GROUP = {
    "in": "in",
    "motion_in": "in",
    "out": "out",
    "motion_out": "out",
    "main": "main",
    "motion_main": "main",
}


def _split_top_level(body: str) -> list[str]:
    """`(宣言)` の中身を top-level の `;` で割る (括弧 `(){}[]` と quote の中は割らない)。"""
    parts: list[str] = []
    depth = 0
    quote: str | None = None
    start = 0
    for k, ch in enumerate(body):
        if quote is not None:
            if ch == quote:
                quote = None
            continue
        if ch in "'\"":
            quote = ch
        elif ch in "({[":
            depth += 1
        elif ch in ")}]":
            depth -= 1
        elif ch == ";" and depth == 0:
            parts.append(body[start:k])
            start = k + 1
    parts.append(body[start:])
    return parts


def _degrade_motion_decls(line: str, slots: set[str] | None) -> tuple[str, int]:
    """行の `(宣言)` の中の動きの宣言を編集可能 profile の preset へ機械で寄せる (editable_motion の最後の網 — 層を落とさない)。

    slots = 書き換える slot ({"in","out","main"})。None = blanket (的の行が引けなかった時): object 形の `in:`/`out:` を
    `fade` に・custom 形 (`{…}`/keys/波形) の `main:` を落とす (named の `main: kb {…}` は残す)。戻り = (行, 書き換えた数)。"""
    open_at = line.find("(")
    if open_at < 0:
        return line, 0
    depth = 0
    quote: str | None = None
    close_at = -1
    for k in range(open_at, len(line)):
        ch = line[k]
        if quote is not None:
            if ch == quote:
                quote = None
            continue
        if ch in "'\"":
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                close_at = k
                break
    if close_at < 0:
        return line, 0
    changed = 0
    kept: list[str] = []
    for part in _split_top_level(line[open_at + 1 : close_at]):
        head = re.match(r"\s*(in|out|main)\s*:", part)
        if head is None:
            kept.append(part)
            continue
        key = head.group(1)
        value = part[head.end() :]
        if slots is not None and key not in slots:
            kept.append(part)
            continue
        if slots is None and key in ("in", "out") and "{" not in value:
            kept.append(part)  # preset 語のまま
            continue
        if (
            slots is None
            and key == "main"
            and not (value.lstrip().startswith("{") or "keys" in value or "waveform" in value)
        ):
            kept.append(part)  # named の main (kb 等) は残す
            continue
        changed += 1
        if key in ("in", "out"):
            kept.append(f"{part[: head.start(1)]}{key}: fade")
        # main は decl ごと落とす (常時の custom は preset に写せない)
    if not changed:
        return line, 0
    return line[: open_at + 1] + ";".join(kept).strip("; ") + line[close_at:], changed


ROOT = ""  # 行の無い DEFECT の持ち主が根 (Run.unlocated_owner の値)
_DEF_CHILD = re.compile(r"^[ \t]+[A-Za-z_][\w-]*#([A-Za-z_][\w-]*)", re.M)  # 定義の字下げの子の行 `  icon#i(…` → 子の名


def def_children(text: str) -> set[str]:
    """名のある定義 (見出しの行 + 字下げの子) の子の名 — 後の cut は実体の子を `実体.子` で参照する。"""
    return set(_DEF_CHILD.findall(text))


def drop_token(line: str, token: str) -> str:
    """行から著者の綴りを 1 つ消す (宣言なら隣の `;` も 1 つ) — 製品の `grammar.unshown._without` と同じ消し方 (skill は repo の
    code を import しない)。"""
    at = line.find(token)
    before, after = line[:at], line[at + len(token) :]
    if not token.startswith("["):
        if after.lstrip().startswith(";"):
            after = after.lstrip()[1:].lstrip()
        elif before.rstrip().endswith(";"):
            before = before.rstrip()[:-1].rstrip()
    return before + after


@dataclass(frozen=True)
class Defect:
    """check の欠陥 (製品の `grammar.lexicon.Defect.as_record()` の形 — local は doc の out/defects.json・remote は API の `defects`)。
    `text` は描いた 1 行 (直し役に渡す文面)・場所と同一性は欄で見る (文面の正規表現に戻さない)。"""

    code: str
    file: str  # design.txt / timeline.txt
    line: int  # 0 / 1 = 行の無い欠陥 (RUNTIME など・持ち主は attribute_unlocated が確かめる)
    cause: str
    where: str | None
    level: str  # DEFECT (描けない) / severe / warn / info
    text: str

    @classmethod
    def read(cls, d: dict[str, object]) -> Defect:
        return cls(
            code=str(d.get("code", "")),
            file=str(d.get("file", "")),
            line=int(str(d.get("line") or 0)),
            cause=str(d.get("cause", "")),
            where=str(d["where"]) if d.get("where") else None,
            level=str(d.get("level", "DEFECT")),
            text=str(d.get("text", "")),
        )

    @property
    def sig(self) -> tuple[str, str | None, str]:
        """同一性 (file:行を除く) — 同じ根の欠陥が別の doc で別の行番号に出ても 1 つと数える。"""
        return (self.code, self.where, self.cause)

    @property
    def which(self) -> int:
        return 0 if self.file == "design.txt" else 1


@dataclass
class WarmState:
    """cut 1 つの先行解決の頼み (run の warm) の状態。"""

    thread: threading.Thread | None = None  # 走っている / 走った頼み
    key: tuple[object, ...] | None = None  # 頼んだ text の素材の鍵 (asset_key)・同じなら頼み直さない
    ok: bool = False  # 頼みが投入と同じ検査を通った


class FixerUnavailable(Exception):
    """直し役が返らない・process が落ちた — 呼び直しても同じなので、直す前の版で続ける (出力が使えないだけなら呼び直す)。"""


class Rejected(Exception):
    """受け口が止めた頼み (HTTP の 400 と同じ中身)。defects = 投入検査の DEFECT の行 (無ければ error の文)。"""

    def __init__(self, op: str, defects: list[str]) -> None:
        super().__init__(f"{op}: " + " / ".join(defects)[:600])
        self.defects = defects


# 見直しの回数。既定は画像なしで 1 回 — 53 cut の盲検 (両順で一致した差) で今の直し役 (low・指摘のある cut だけ) に 9 対 3・
# 投入の遅れは全 cut 平均 1.5 s (p90 5.5 s)。--look は静止画を見せて 2 回 (2 回目は 1 回目の直しを描き直した絵を見る) — 5 cut の点で
# 直し役だけ 5.2・見直し 1 回 5.8・画像なし 2 回 6.4・画像あり 2 回 6.5 (10-22・effort medium・low は直し役と差が出ない)
REVIEW_ROUNDS = 1
REVIEW_ROUNDS_LOOK = 2

# 台詞の尺の指摘 (`Run.length_finding`): check の見積りが cut の予算から ±20% (短い cut は ±2.5 s — 文 1 本より細かく寄せない) を
# 超えたら直し役に文の刈り込み / 足しを頼む。締めの cut の予算は依頼の残りを 10〜30 s の範囲で (弾性)
LENGTH_TOLERANCE = 0.2
LENGTH_SLACK_S = 2.5
CLOSING_BUDGET_S = (10.0, 30.0)

# 機械全体で同時に走らせる warm の数 (run を跨ぐ・期限の近い cut から)。4 core の機械で 3 本並列の run が check の直後に 4 本ずつ warm を
# 起こすと 12 本が重なり、1 本 13 s の warm が 40〜64 s に伸びた (cur12・svg の描画と主体計測が CPU 待ち)


def claude_mcp_token(remote: str) -> str | None:
    """Claude Code が remote MCP (`<remote>/mcp`) の OAuth で得た access token (`~/.claude/.credentials.json` の mcpOAuth)。
    plugin で入れた skill は API key を持たない — `/mcp` で NoLang に接続した token をそのまま REST にも使う (同じ Bearer)。"""
    path = Path(os.environ.get("CLAUDE_CONFIG_DIR", str(Path.home() / ".claude"))) / ".credentials.json"
    try:
        entries = json.loads(path.read_text()).get("mcpOAuth", {})
    except (OSError, ValueError):
        return None
    base = remote.rstrip("/")
    for entry in entries.values():
        url = str(entry.get("serverUrl", "")).rstrip("/")
        if url in (base, base + "/mcp") and entry.get("accessToken"):
            return str(entry["accessToken"])
    return None


class Run:
    def __init__(
        self,
        project: Path,
        *,
        staff: str | None = None,
        fix: str | None = "low",
        review: str | None = "low",
        fix_scope: str = "severe",
        keep_assets: bool = True,
        look: bool = False,
        remote: str | None = None,
        token: str | None = None,
        editable: bool = False,
    ) -> None:
        self.project = project
        # 編集可能モード: start に editable を立て、check に profile=editable を渡す (投入の門は server が video の
        # create_setting から読む)。著者・担当・直しの prompt の節は env NOLANG_STUDIO_PROFILE (stream_make.sh が立てる)
        self.editable = editable
        # remote = NoLang API (nolang-api consumer) の base URL。著者・担当・直しはこの機械の claude -p のまま、確定した cut の stream の
        # text を `unstable/drafts/{id}/cuts/` へ投入し、素材・描画・配信は server (製品の draft stream) に任せる。None = この機械の
        # `studio.py stream` (同じ製品の外部の著者の run) に同じ flow 関数で流す (`call`)。根は閉じた時点で根だけを先に流し (`submit_root`)、
        # 以後凍る
        self.remote = remote.rstrip("/") if remote else None
        self.token = token
        self.video_id: str | None = None  # run の video (start で決まる)
        self.watch_url = ""  # 視聴 URL (remote だけ・`WATCH` / `PLAYABLE` の行に出す)
        self.root_submitted = False
        self.fixed: frozenset[str] = frozenset()  # 直し役に回す規則 = 製品の台帳の fixed (run の頭で `rules` から)
        self.staff_effort = staff  # 担当 (cut を仕上げる) の effort。None = 担当なし
        self.fix_effort = fix  # 直し役の effort。None = 直し役なし (見直しもなし)
        # 直し役の範囲: "defect" = DEFECT と隠れる文字だけ・"severe" = + severe 全部・"warn" = 見直しと台帳の指摘の直し
        self.fix_scope = fix_scope
        self.review_effort = (
            review if fix is not None and fix_scope == "warn" else None
        )  # 見直し (指摘に出ない弱い所・崩れも探す 1 回目の直し役) の effort。None = 見直しなし
        # 担当は絵と台詞を変えない — 絵と声は著者の版から担当と並列に作る (`_stage` が担当の前に warm を頼む)
        self.keep_assets = keep_assets
        self.look = look  # 見直しに cut の静止画も見せる (REVIEW_ROUNDS_LOOK 回)
        self.solo, self.st, self.studio = project / "solo", project / "stream", project / "studio"
        self.weave = project / "weave"
        self.weave.mkdir(parents=True, exist_ok=True)
        self.env = dict(
            os.environ,
            **({"PYTHONPATH": str(REPO), "STUDIO_SERVER_SOCK": str(REPO / "tmp/studio/.server/sock")} if REPO else {}),
            # run で 1 つの素材の置き場 — prefetch・warm・stream の render が同じ dir を使い、落とした絵と音を引き直さない
            STUDIO_PROCESS_ID=f"studio-{uuid5(NAMESPACE_URL, str(project.resolve())).hex[:12]}",
        )
        self.name_lock = threading.Lock()
        self.warms: defaultdict[str, WarmState] = defaultdict(WarmState)
        self.root_renames: dict[str, str] = {}  # 根の予約名の改名 (normalize_root) — 後から届く cut の参照にも当てる
        self.root_checked = False
        self.root_renamed: set[str] = set()
        self.submitted: set[str] = set()  # 流した cut — その text は変えない (後の doc も同じ text で組む)
        # 行の無い DEFECT の sig → 持ち主の cut (根は ROOT)。attribute_unlocated が書く
        self.unlocated_owner: dict[str, str] = {}
        self.author_clean: set[str] = set()  # 著者の版 (担当が触る前) が check で DEFECT 0 だった cut
        self.staged: dict[str, bool] = {}
        self.broken: dict[str, str] = {}
        self.stream_proc: subprocess.Popen[bytes] | None = None
        self.t0 = time.time()
        self.order: list[str] = []
        self.cut_estimate: dict[str, float] = {}  # cut → check が測った見込み秒 (字数 × 話速 + 間・実尺 cache 込み)

    # ---- 記録 ----
    def log(self, **kw: object) -> None:
        kw["t"] = time.time()
        kw["since"] = round(float(kw["t"]) - self.t0, 1)
        with (self.st / "run.jsonl").open("a") as f:
            f.write(json.dumps(kw, ensure_ascii=False) + "\n")
        print(json.dumps(kw, ensure_ascii=False), flush=True)

    def studio_cmd(self, *args: str, timeout: int = 1800, stdin: str | None = None) -> str:
        r = subprocess.run(
            [PY, str(STUDIO), *args],
            cwd=REPO or HERE.parent,
            env=self.env,
            capture_output=True,
            text=True,
            timeout=timeout,
            input=stdin,
        )
        return r.stdout + r.stderr

    # ---- 受け口 (nolang-api `drafts/` の flow 関数) ----
    _ROUTES = {  # op → (method, path) — {id} は run の video
        "cut": ("POST", "/v1/unstable/drafts/{id}/cuts/"),
        "warm": ("POST", "/v1/unstable/drafts/{id}/warm/"),
        "check": ("POST", "/v1/unstable/drafts/check/"),
        "rename": ("POST", "/v1/unstable/drafts/rename/"),
        "rules": ("GET", "/v1/unstable/drafts/rules/"),
        "abort": ("DELETE", "/v1/unstable/drafts/{id}/"),
    }

    def call(self, op: str, body: dict[str, object] | None = None) -> dict[str, object]:
        """受け口を 1 回呼ぶ。remote は HTTP (`_ROUTES`)・local は同じ flow 関数を手元の user で (`studio.py api <op>`・body は stdin)。
        止めた頼み (HTTP の 400) は `Rejected`・届かない時は RuntimeError。"""
        body = dict(body or {})
        if self.remote is None:
            if self.video_id is not None:
                body.setdefault("video_id", self.video_id)
            out = self.studio_cmd("api", op, timeout=600, stdin=json.dumps(body, ensure_ascii=False))
            last = next((l for l in reversed(out.strip().splitlines()) if l.startswith("{")), None)
            if last is None:
                raise RuntimeError(f"{op}: {out[-400:]}")
            loaded = json.loads(last)
        else:
            method, path = self._ROUTES[op]
            req = urllib.request.Request(
                f"{self.remote}{path.format(id=self.video_id)}",
                data=json.dumps(body).encode("utf-8") if method == "POST" else None,
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"},
                method=method,
            )
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    loaded = json.loads(resp.read().decode("utf-8") or "{}")
            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", "replace")
                if e.code != 400:
                    raise RuntimeError(f"{op} -> {e.code}: {detail[:600]}") from e
                try:
                    loaded = {"status": 400, **json.loads(detail)}
                except ValueError:
                    loaded = {"status": 400, "error": detail[:600]}
        if loaded.get("status") == 500:
            raise RuntimeError(f"{op} -> 500: {loaded.get('error')}")
        if loaded.get("status") == 400:
            defects = loaded.get("defects")
            raise Rejected(op, [str(d) for d in defects] if isinstance(defects, list) else [str(loaded)[:600]])
        return loaded

    # ---- 著者の file ----
    def cut_block(self, name: str) -> tuple[str, str] | None:
        f = self.solo / f"cut_{name}.txt"
        if not f.exists():
            return None
        return self.split_block(name, f.read_text())

    @staticmethod
    def split_block(name: str, txt: str) -> tuple[str, str] | None:
        """cut の file の text を (design, timeline) に割る (cut_block と同じ正規化)。"""
        if "---timeline---" not in txt:
            return None
        d, t = txt.split("---timeline---", 1)
        d = d.strip("\n") + "\n"
        if not re.search(r"^section#", d, re.M):
            # 著者が cut の design の頭の `section#名` を落とすと、その要素は doc の中で次の `section#` の cut に付く
            # (s9 03: 先行 call の hook / clash に頭が無く、hook の写真が本体の cut で開いて `~` の継続が割れた)。名は plan で決まっている
            d = f"section#{name}\n" + d
        return d, t.strip("\n") + "\n"

    @staticmethod
    def named_defs(design: str) -> list[tuple[str, str, str]]:
        """design の block の名のある定義 (種, 名, 行 + 字下げの子の text)。"""
        out: list[tuple[str, str, str]] = []
        lines = design.split("\n")
        k = 0
        while k < len(lines):
            m = _NAMED_DEF.match(lines[k])
            if m is None:
                k += 1
                continue
            j = k + 1
            while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
                if not lines[j].strip() and (j + 1 >= len(lines) or not lines[j + 1].startswith((" ", "\t"))):
                    break
                j += 1
            out.append((m.group(1), m.group(2), "\n".join(lines[k:j]).rstrip("\n") + "\n"))
            k = j
        return out

    def add_defs(self, c: str, text: str) -> bool:
        """定義の text を cut c の block の design (`section#c` の次) に足す (既にあれば足さない)。c の file が無ければ False。"""
        f = self.solo / f"cut_{c}.txt"
        if not f.exists() or not text.strip():
            return False
        body = f.read_text()
        if text.strip() in body:
            return True
        m = re.search(r"^section#[^\n]*\n", body, re.M)
        at = m.end() if m else 0
        f.write_text(body[:at] + text + body[at:])
        return True

    def remove_defs(self, c: str, texts: list[str]) -> None:
        f = self.solo / f"cut_{c}.txt"
        body = f.read_text()
        for text in texts:
            body = body.replace(text, "", 1)
        f.write_text(body)

    def defs_before(self, c: str) -> str:
        """c より前の live な cut の block の名のある定義 (担当・直し役の参考)。壊れた cut の定義は次の live な cut の block に移っている。"""
        parts: list[str] = []
        for x in self.order[: self.order.index(c)]:
            blk = self.cut_block(x)
            if blk and not self.broken.get(x):
                parts.extend(text for _kind, _name, text in self.named_defs(blk[0]))
        return "".join(parts)

    def write_defs_before(self, c: str) -> None:
        (self.solo / f"defs_before_{c}.txt").write_text(self.defs_before(c))

    def move_forward_defs(self, c: str) -> None:
        """cut c の block の定義のうち、前の cut (まだ ready でない) が既に使っている名の物は、その cut の block へ移す (定義は初めて
        使う cut の物 — 前の cut の check が NAME で落ちない)。"""
        blk = self.cut_block(c)
        if blk is None:
            return
        moved: list[str] = []
        for _kind, name, text in self.named_defs(blk[0]):
            pattern = re.compile(rf"(?<![\w#.]){re.escape(name)}(?![\w-])")
            for u in self.order[: self.order.index(c)]:
                if self.staged.get(u) or self.broken.get(u):
                    continue
                ublk = self.cut_block(u)
                if ublk and any(n == name for _k, n, _t in self.named_defs(ublk[0])):
                    # u は同じ名を自分で定義している (別の種でも — hook の `motion row` に引かれて parts の `def row` を hook へ移し、
                    # hook の担当がそれを消して parts が落ちた o11_16)。名が u に出るのはその定義の使用で、c の定義の使用ではない
                    continue
                if ublk and (pattern.search(ublk[0]) or pattern.search(ublk[1])) and self.add_defs(u, text):
                    moved.append(text)
                    self.log(cut=c, event="def_moved", name=name, to=u)
                    break
        if moved:
            self.remove_defs(c, moved)

    def adopt_defs_of(self, b: str) -> None:
        """壊れた cut b の定義を、b の後の最初の live な (まだ流していない) cut の block に移す — 後の cut がその名を使えるように。
        移す先が無ければ捨てる (後の cut も使えない)。"""
        blk = self.cut_block(b)
        if blk is None:
            return
        texts = [text for _kind, _name, text in self.named_defs(blk[0])]
        if not texts:
            return
        (self.solo / f"defs_{b}.txt").write_text("".join(texts))
        for x in self.order[self.order.index(b) + 1 :]:
            if self.broken.get(x) or x in self.submitted:
                continue
            if self.add_defs(x, "".join(texts)):
                self.log(cut=b, event="defs_adopted", by=x, n=len(texts))
                return

    def mark_broken(self, c: str, reason: str) -> None:
        self.broken[c] = reason
        self.adopt_defs_of(c)

    def first_live(self) -> str | None:
        """最初の live な cut (f) — 根の持ち主。壊れた cut は飛ばす。構成が来ていなければ None。"""
        return next((c for c in self.order if not self.broken.get(c)), None)

    # ---- doc ----
    def doc_src(self, pins: dict[str, object] | None = None) -> dict:
        """doc の src.json = studio/src.json (設定と著者の pin) + pins (run が解いた素材 — `--look` の静止画・書き戻し)。素材を解くのは
        run (warm と投入) で、check は doc の pin を読まない。"""
        base = self.studio / "src.json"
        d = json.loads(base.read_text()) if base.exists() else {"asset_pins": {}}
        d.setdefault("asset_pins", {}).update(pins or {})
        return d

    def live_cuts(self, cuts: list[str]) -> list[str]:
        """壊れた cut (直しで通らなかった物) は後の doc から外す — 1 cut 欠けても残りは描ける方を取る。"""
        return [c for c in cuts if not self.broken.get(c) or c == cuts[-1]]

    def cut_line_ranges(
        self, cuts: list[str], *, root_extra: str = ""
    ) -> dict[str, tuple[tuple[int, int], tuple[int, int]]]:
        """doc (根 + root_extra + cuts) の中で cut ごとの design / timeline の行の範囲 [a, b] (1 始まり)。"""
        rd, rt = self.root()
        d_at, t_at = (rd + root_extra).count("\n"), rt.count("\n")
        out: dict[str, tuple[tuple[int, int], tuple[int, int]]] = {}
        for c in cuts:
            blk = self.cut_block(c)
            if not blk:
                continue
            nd, nt = blk[0].count("\n"), blk[1].count("\n")
            out[c] = ((d_at + 1, d_at + nd), (t_at + 1, t_at + nt))
            d_at += nd
            t_at += nt
        return out

    def rename_collisions(self, cuts: list[str]) -> None:
        """先行 call と本体は同時に書くので、互いの cut の要素の名がぶつかる (03: `clash` と `climax` がどちらも `cl_p`)。
        根か前の cut が定義した名を後の cut が字下げ無しの行で定義していたら、後の cut の側の名をその block の中で
        (定義も参照も) `名_<cut>` に改名して solo/ に書き戻す。名は frame に写らない。どの doc で見つけても後の cut を直すので、
        cut の届く順に依らず同じ結果になる。"""
        with self.name_lock:
            self.normalize_root()
            rd, _ = self.root()
            seen = {m.group(2) for m in _TOP_DEF.finditer(rd)} | set(_RESERVED_NAMES)
            for c in cuts:
                f = self.solo / f"cut_{c}.txt"
                if self.root_renames and c not in self.root_renamed and f.exists():
                    # 根の予約名を改名した後に届いた cut は、その名への参照 (印・位置の式) を同じ名に揃える
                    self.root_renamed.add(c)
                    txt = f.read_text()
                    renamed_txt = self.rename(txt, self.root_renames)
                    if renamed_txt != txt:
                        f.write_text(renamed_txt)
                blk = self.cut_block(c)
                if not blk:
                    continue
                names = [m.group(2) for m in _TOP_DEF.finditer(blk[0]) if m.group(1) != "section"]
                clash = [n for n in dict.fromkeys(names) if n in seen and (_RENAMABLE.match(n) or n in _RESERVED_NAMES)]
                if clash:
                    txt = f.read_text()
                    tag = re.sub(r"[^a-z0-9]", "", c.lower())[:8] or "c"
                    renamed = {}
                    for n in clash:
                        new = f"{n}_{tag}"
                        k = 2
                        while new in seen or new in names:
                            new = f"{n}_{tag}{k}"
                            k += 1
                        renamed[n] = new
                    txt = self.rename(txt, renamed)
                    f.write_text(txt)
                    self.log(cut=c, event="rename", names=renamed)
                    blk = self.cut_block(c) or blk
                    names = [m.group(2) for m in _TOP_DEF.finditer(blk[0]) if m.group(1) != "section"]
                seen.update(names)

    def normalize_root(self) -> None:
        """根の字下げ無しの行が予約名 (`div#bg`) を定義していたら `名_root` に改名して solo/ に書き戻す (1 回)。根の DEFECT:NAME は
        cut の直し役では消えない。name_lock の中で呼ぶ。"""
        if self.root_checked or not (self.solo / "root_design.txt").exists():
            return
        self.root_checked = True
        rd = (self.solo / "root_design.txt").read_text()
        names = [m.group(2) for m in _TOP_DEF.finditer(rd) if m.group(1) != "section"]
        renames = {n: f"{n}_root" for n in dict.fromkeys(names) if n in _RESERVED_NAMES}
        if not renames:
            return
        for name in ("root_design.txt", "root_timeline.txt"):
            f = self.solo / name
            if f.exists():
                f.write_text(self.rename(f.read_text(), renames))
        self.root_renames = renames
        self.log(event="rename_root", names=renames)

    def rename(self, txt: str, renames: dict[str, str]) -> str:
        """cut の text の中の層の名を改名する (参照も文法どおりに・製品の文法 `drafts/rename/`)。"""
        return str(self.call("rename", {"text": txt, "renames": renames})["text"])

    @property
    def language(self) -> str:
        try:
            value = json.loads((self.studio / "src.json").read_text()).get("settings", {}).get("language")
        except (OSError, ValueError):
            return "ja"
        return str(value or "ja")

    @property
    def aspect(self) -> str:
        """依頼の縦横比 (params.txt の 2 つ目・`16:9` / `9:16`) — 根の canvas がこれと違えば check と投入検査が止める。"""
        return (self.project / "params.txt").read_text().split()[1]

    def plan_seconds(self) -> dict[str, float]:
        """plan の cut ごとの目標秒 (著者が長さの目安を cut へ配った値・尺の指摘の予算)。無ければ空。"""
        from stream_author import plan_names  # noqa: PLC0415 — scripts dir を sys.path に足している

        plan = self.solo / "plan.txt"
        return dict(plan_names(plan.read_text())) if plan.exists() else {}

    def note_cut_estimates(self, dd: Path) -> None:
        """check が書いた cut の時刻 (out/check_cuts.json・字数 × 話速 + 間・実尺 cache 込み) を cut ごとの見込み秒に写す。
        plan の秒は台詞を書く前の配分なので、進行線の全長と尺の指摘は check の値で数える。"""
        f = dd / "out/check_cuts.json"
        if not f.exists():
            return
        try:
            rows = json.loads(f.read_text()).get("cuts") or []
        except (OSError, ValueError):
            return
        for row in rows:
            if isinstance(row, dict) and isinstance(row.get("cut"), str):
                self.cut_estimate[row["cut"]] = (
                    max(float(row.get("end_ms", 0)) - float(row.get("start_ms", 0)), 0.0) / 1000
                )

    def estimated_seconds(self) -> dict[str, float]:
        """cut ごとの見込み秒 = check が測った値 (あれば) → 著者の plan の秒 → 10 s。"""
        plan = self.plan_seconds()
        return {c: self.cut_estimate.get(c, plan.get(c, 10.0)) for c in dict.fromkeys([*plan, *self.order])}

    def planned_total_ms(self) -> int | None:
        """見込み秒の合計 (ms)。`until: end` の進行線の全長に使う — stream では動画の全長が最後の cut まで決まらないので、
        どの prefix の doc でも同じ値で伸ばす (根は最初の cut の受理で凍るので、その時点の見込み)。"""
        total = sum(self.estimated_seconds().values())
        return int(total * 1000) if total > 0 else None

    @property
    def requested_seconds(self) -> float | None:
        """依頼の長さの目安 (params.txt の 3 つ目)。"""
        try:
            return float((self.project / "params.txt").read_text().split()[2])
        except (OSError, IndexError, ValueError):
            return None

    @functools.cached_property
    def verbatim(self) -> bool:
        """依頼の台本をそのまま読む動画か — 著者が plan に逐語の注記を書いた・依頼文が逐語の読み上げを求める言い回しを含む。逐語の動画には
        尺の指摘を掛けない (文の足し引きが依頼の台本の改変になる・10-06 の「著者に尺合わせをさせない」裁定の核)。plan が閉じてから読む。"""
        from stream_author import (  # noqa: PLC0415 — scripts dir を sys.path に足している
            VERBATIM_MARK,
            VERBATIM_REQUEST,
            is_verbatim,
        )

        plan = self.solo / "plan.txt"
        plan_text = plan.read_text() if plan.exists() else ""
        request = (self.project / "request.txt").read_text()
        if not is_verbatim(plan_text, request):
            return False
        self.log(
            event="verbatim",
            plan_mark=VERBATIM_MARK in plan_text,
            request_phrase=VERBATIM_REQUEST.search(request) is not None,
        )
        return True

    def cut_budget(self, c: str) -> float | None:
        """cut c の台詞の尺の予算 (秒) = plan の目標秒。締めの cut は弾性: 依頼の目安から前の live な cut の見込み (check の値か目標秒)
        を引いた残りを CLOSING_BUDGET_S の範囲で (前の cut の伸び縮みを締めで吸う)。plan に無い cut は None。"""
        plan = self.plan_seconds()
        if c not in plan:
            return None
        requested = self.requested_seconds
        if c != self.order[-1] or requested is None:
            return plan[c]
        before = sum(self.cut_estimate.get(x, plan.get(x, 10.0)) for x in self.order[:-1] if not self.broken.get(x))
        low, high = CLOSING_BUDGET_S
        return min(max(requested - before, low), high)

    def length_finding(self, c: str) -> str:
        """check の見積り (字数 × 話速 + 間) が cut の予算から LENGTH_TOLERANCE (か LENGTH_SLACK_S の大きい方) を超えて外れたら、
        直し役への指摘の 1 行 (文を丸ごと消す / 足す本数つき)。外れていなければ空。直し役を新しく呼ぶ理由にはしない — 見直し (全 cut
        1 回目の直し役) の call に添えるだけ (待ちと call を増やさない)。最初の cut は見ない: 再生開始の臨界路で、足した文が次の直しの
        指摘と声の作り直しを呼び最初の segment を 15〜30 s 遅らせた (10-24 の a2 d5)・ずれは締めの cut の弾性が吸う。"""
        from stream_author import LENGTH_RULE  # noqa: PLC0415 — scripts dir を sys.path に足している

        budget, estimate, blk = self.cut_budget(c), self.cut_estimate.get(c), self.cut_block(c)
        if self.verbatim or c == self.order[0] or budget is None or estimate is None or blk is None:
            return ""
        gap = estimate - budget
        if abs(gap) <= max(budget * LENGTH_TOLERANCE, LENGTH_SLACK_S):
            return ""
        lines = max(sum(1 for line in blk[1].splitlines() if line.lstrip().startswith("@")), 1)
        per = estimate / lines
        n = min(max(round(abs(gap) / per), 1), 2)
        verb = "消す" if gap > 0 else "足す"
        return (
            f"warn {LENGTH_RULE} (cut): 台詞の見積り {estimate:.0f} 秒 / この cut の目標 {budget:.0f} 秒 ({gap:+.0f} 秒・台詞の行 1 本 ≈ "
            f"{per:.0f} 秒) — 台詞の行を文ごと {n} 本{verb} (文単位・早口や間の詰めで合わせない)"
        )

    def length_gap(self) -> dict[str, float | None]:
        """依頼の目安の秒・著者の plan の和・check の見込みの和・実尺 (製品の stream_done の duration_s) — 記録。"""
        requested = self.requested_seconds
        actual: float | None = None
        with contextlib.suppress(OSError, ValueError):
            for line in (self.st / "run.jsonl").read_text().splitlines():
                e = json.loads(line)
                if e.get("event") == "stream_done" and isinstance(e.get("duration_s"), (int, float)):
                    actual = float(e["duration_s"])
        plan = self.plan_seconds()
        return {
            "requested_s": requested,
            "plan_s": round(sum(plan.values()), 1) if plan else None,
            "estimate_s": round(sum(self.estimated_seconds().values()), 1) if self.order else None,
            "actual_s": actual,
        }

    def root(self) -> tuple[str, str]:
        rd = (self.solo / "root_design.txt").read_text().rstrip("\n") + "\n"
        rt = (self.solo / "root_timeline.txt").read_text().rstrip("\n") + "\n"
        total = self.planned_total_ms()
        if total is not None:
            rd = re.sub(
                r"^(progress#[A-Za-z0-9_]+\([^\n]*?until:\s*end)(?![^\n]*total:)",
                rf"\1; total: {total}ms",
                rd,
                flags=re.M,
            )
        return rd, rt

    def doc_texts(self, cuts: list[str], *, root_extra: str = "") -> tuple[str, str]:
        """doc (根 + cuts の block) の design / timeline の text。root_extra = 根の design の後ろに足す行 (warm の doc が、まだ ready でない
        前の cut の定義を運ぶ)。"""
        rd, rt = self.root()
        des, tls = [rd + root_extra], [rt]
        for c in cuts:
            blk = self.cut_block(c)
            if blk:
                des.append(blk[0])
                tls.append(blk[1])
        return "".join(des), "".join(tls)

    def doc_dir(
        self, name: str, cuts: list[str], *, root_extra: str = "", pins: dict[str, object] | None = None
    ) -> Path:
        """doc (根 + cuts) を weave/<name>/ に組む。pins = doc の src.json に足す素材の pin (`--look` の静止画が warm の絵で撮る)。"""
        dd = self.weave / name
        (dd / "out").mkdir(parents=True, exist_ok=True)
        self.rename_collisions(cuts)
        design, timeline = self.doc_texts(cuts, root_extra=root_extra)
        (dd / "design.txt").write_text(design)
        (dd / "timeline.txt").write_text(timeline)
        marker = (
            dd / "OPEN_ENDED"
        )  # 後に cut が続く prefix → check (と warm の lowering) は最後の cut だけの規則を掛けない
        if not cuts or cuts[-1] != self.order[-1]:
            marker.touch()
        else:
            marker.unlink(missing_ok=True)
        # 同じ cut の doc を複数の thread が組み直す事があるので、読み手が書きかけを見ないよう置き換えで書く
        tmp = dd / f".src.json.{threading.get_ident()}"
        tmp.write_text(json.dumps(self.doc_src(pins), ensure_ascii=False, indent=1))
        os.replace(tmp, dd / "src.json")
        # 書体の実体 (TTF) は project で 1 つの cache (studio/out/fonts) を全部の doc が symlink で共有する (`--look` の静止画)
        shared = self.studio / "out/fonts"
        shared.mkdir(parents=True, exist_ok=True)
        fonts = dd / "out/fonts"
        if not fonts.is_symlink():
            if fonts.is_dir():  # 以前の run の実 dir — 中身を共有 cache へ寄せて置き換える
                for f in fonts.iterdir():
                    if f.is_file() and not (shared / f.name).exists():
                        shutil.copyfile(f, shared / f.name)
                shutil.rmtree(fonts)
            fonts.symlink_to(shared.resolve())
        return dd

    # ---- check と直し ----
    def check(self, dd: Path, *, ended: bool) -> tuple[str, list[Defect], list[dict]]:
        """ended = 動画の終わりまで書いた doc (False = この prefix の後に cut が続く — 最後の cut だけの規則を掛けない)。製品の check
        (`drafts/check/` — compile・composer と layout の乾いた実行・lint の全規則・cut の時刻。書体は本番と同じ・run の warm で解けた絵は
        実画像で判定) を doc の 2 file で 1 回。結果は doc の out/ に書く (defects.json = DEFECT の行・lint_check.json = 指摘・
        check_cuts.json = cut の時刻) — 欠陥の行を落とす `drop_defect_lines` と期限の見込み (`note_cut_estimates`) が読む。返り値の
        出力 = check の表 (担当に渡す時刻の行を含む)。"""
        body = self.call(
            "check",
            {
                "design": (dd / "design.txt").read_text(),
                "timeline": (dd / "timeline.txt").read_text(),
                "open_ended": not ended,
                "aspect_ratio": self.aspect,
                # 開始済みの run — warm で解けた絵 (測った主体と実画像) で読めない文字・主体に乗った文字も見る
                **({"video_id": self.video_id} if self.video_id else {}),
                # 編集可能モードの run — 違反は DEFECT (投入の門と同じ答え)
                **({"profile": "editable"} if self.editable else {}),
                # 持ち込み音声 — clip 台帳で `@clip` の話者と `[trim:]` を解く (開始済みの run は server が run の音声を使う)
                **({"speech_file_ids": self.speech_file_ids()} if self.speech_file_ids() else {}),
            },
        )
        records = [d for d in body.get("defects", []) if isinstance(d, dict)]
        defects = [Defect.read(d) for d in records]
        lint = [f for f in body.get("findings", []) if isinstance(f, dict)]
        out = dd / "out"
        out.mkdir(exist_ok=True)
        (out / "lint_check.json").write_text(json.dumps(lint, ensure_ascii=False))
        if records:
            (out / "defects.json").write_text(json.dumps(records, ensure_ascii=False))
        else:
            (out / "defects.json").unlink(missing_ok=True)
        (out / "check_cuts.json").write_text(json.dumps({"cuts": body.get("cuts") or []}, ensure_ascii=False))
        self.note_cut_estimates(dd)
        return str(body.get("report") or "\n".join(d.text for d in defects)), defects, lint

    @staticmethod
    def read_defects(dd: Path) -> list[Defect]:
        """doc の out/defects.json (無ければ空)。"""
        f = dd / "out/defects.json"
        if not f.exists():
            return []
        try:
            return [Defect.read(d) for d in json.loads(f.read_text()) if isinstance(d, dict)]
        except (OSError, ValueError):
            return []

    def attribute_lint(self, lint: list[dict[str, object]], c: str) -> None:
        """cut の無い lint の指摘 (`cut=-`: design 由来の shrunk / child_overflow など) を、層の名がこの cut の block に
        定義されていれば この cut の物にする — 直しの列の規則でも `cut=-` のままだと誰の物にもならず直らなかった (17 の text_fit・今の shrunk)。"""
        blk = self.cut_block(c)
        if not blk:
            return
        for f in lint:
            if f.get("cut") != "-":
                continue
            base = re.split(r"[.\[×( ]", str(f.get("layer", "")))[0].strip("'\")")
            if base and re.search(r"#" + re.escape(base) + r"(?:[\s(.\[]|$)", blk[0], re.M):
                f["cut"] = c

    def to_fix(self, f: dict[str, object]) -> bool:
        """fix を回す指摘か: 台帳の直しの列の規則の severe / warn (level では決めない — docs/draft_src_v2/quality.md)。"""
        return f.get("severity") in ("severe", "warn") and f.get("rule") in self.fixed

    def fix_finding(self, f: dict[str, object]) -> bool:
        """直し役に回す指摘か (`fix_scope`): defect = 隠れる文字だけ (一番避けたい崩れで、機械の直し move_after は字の札どうしに
        届かない)・severe = severe 全部 (担当後の severe は cut の 9%・大半は担当が作る — 隠れる文字 / 画面の外)・warn = 台帳の
        直しの列の severe / warn (`to_fix`)。"""
        if self.fix_scope == "warn":
            return self.to_fix(f)
        if self.fix_scope == "severe":
            return f.get("severity") == "severe"
        return f.get("rule") == "occluded" and f.get("severity") == "severe"

    def attribute_unlocated(
        self, c: str, cuts: list[str], unlocated: list[Defect], *, root_extra: str = ""
    ) -> tuple[list[Defect], list[Defect]]:
        """行の無い DEFECT の持ち主: c を除いた doc (根 + その doc の前の cut) でも出るなら c の物ではない (前の cut か根の物)。
        c が最初の live な cut なら、除いた doc は根だけ — 出れば根の物 (c の DEFECT として返し、持ち主を ROOT で覚える)。
        全 cut 同じ規則で、cut の index では分けない。
        確かめないと、前の cut の空の text 1 つが後の cut 全部の check に出て、どの cut の直しでも消えずに全部が壊れる (s8 の 16)。
        持ち主は sig で覚える (unlocated_owner) — 後の cut の check で同じ DEFECT が出たら、その cut を除いて lint を取れる (stage)。"""
        prev = [x for x in cuts if x != c and not self.broken.get(x) and self.cut_block(x)]
        base = self.doc_dir(f"{c}.base", prev, root_extra=root_extra)
        _out, base_defects, _lint = self.check(base, ended=False)
        there = {d.text for d in base_defects}
        mine = [d for d in unlocated if d.text not in there]
        foreign = [d for d in unlocated if d.text in there]
        for d in mine:
            self.unlocated_owner[d.sig] = c
        if not prev:  # 根だけの doc で出る = 根の物 → 根の持ち主 (最初の live な cut = c) の物として扱う
            for d in foreign:
                self.unlocated_owner[d.sig] = ROOT
            mine, foreign = mine + foreign, []
        return mine, foreign

    def check_cut(
        self, c: str, cuts: list[str], rnd: int | str, *, name: str | None = None, root_extra: str = ""
    ) -> tuple[Path, str, list[Defect], list[dict], set[str]]:
        """doc (根 + cuts・c を含む) を check し、cut c (か根) の DEFECT と c の lint を返す → (doc, 出力, DEFECT, lint, blockers)。
        blockers = check を止めた前の cut の DEFECT の持ち主 (行の無い DEFECT で持ち主が分からなければ "?")。blockers があればその
        doc の lint は c の物も含めて出ていない。name = doc の dir の名 (既定は c)。root_extra = 根の design の後ろに足す行 (除いた
        cut の定義 — check_without)。その行の DEFECT は根の物と数える。"""
        dd = self.doc_dir(name or c, cuts, root_extra=root_extra)
        out, all_defects, lint = self.check(dd, ended=cuts[-1] == self.order[-1])
        ranges = self.cut_line_ranges(cuts, root_extra=root_extra)
        rd, rt = self.root()
        root_n = ((rd + root_extra).count("\n"), rt.count("\n"))
        defects: list[Defect] = []
        unlocated: list[Defect] = []
        blockers: set[str] = set()
        for d in all_defects:  # file:行 で cut c (か根) の物だけ残す
            n, which = d.line, d.which
            if n <= 1:  # 行の無い DEFECT (RUNTIME の timeline.txt:1 など) は下で持ち主を確かめる
                unlocated.append(d)
                continue
            if n <= root_n[which]:
                # 根の行: 持ち主は最初の live な cut。他の cut はその ready を待つ (根の DEFECT は f の直しで消えるか機械が消す)
                if c == self.first_live():
                    defects.append(d)
                else:
                    blockers.add(ROOT)
                continue
            owner = next((k for k, r in ranges.items() if r[which][0] <= n <= r[which][1]), None)
            if owner in (None, c):
                defects.append(d)
            else:
                blockers.add(owner)
        if unlocated:
            mine_u, foreign = self.attribute_unlocated(c, cuts, unlocated, root_extra=root_extra)
            defects += mine_u
            if foreign:
                # 持ち主の cut が自分の物とした sig なら名で (stage がその cut を除いて lint を取る)・根かまだ分からなければ "?"
                owners = {self.unlocated_owner.get(d.sig, ROOT) for d in foreign}
                blockers |= {o if o not in (ROOT, c) else "?" for o in owners}
                self.log(cut=c, event="defect_elsewhere", round=rnd, n=len(foreign), first=foreign[0].text[:160])
        self.attribute_lint(lint, c)
        return dd, out, defects, lint, blockers

    def wait_owners(self, c: str, owners: set[str]) -> None:
        """持ち主待ち: DEFECT の持ち主の cut (根なら最初の live な cut) が ready (staged) になるまで。相手は持ち主だけ (前の全 cut ではない)。"""
        while True:
            targets = {self.first_live() or c if o in (ROOT, "?") else o for o in owners} - {c}
            if all(self.staged.get(x) for x in targets):
                return
            time.sleep(0.3)

    def check_without(
        self, c: str, cuts: list[str], skip: frozenset[str], rnd: int | str
    ) -> tuple[Path, str, list[Defect], list[dict], set[str]]:
        """skip の cut を除いた doc で c を check する。除いた cut の名のある定義は根の後ろに写す — c が使う名が
        除いた cut の block にあると、除いただけの doc では c の行に誤った DEFECT が出る (nt06 gold: hook の `motion title` を失って
        著者版が unclean になり、revert_author が効かずに落ちた)。"""
        extra = "".join(
            text
            for x in cuts
            if x in skip and (blk := self.cut_block(x)) is not None
            for _kind, _name, text in self.named_defs(blk[0])
        )
        return self.check_cut(c, [x for x in cuts if x not in skip], rnd, root_extra=extra)

    def check_settled(self, c: str, i: int, rnd: int | str) -> tuple[Path, str, list[Defect], list[dict], set[str]]:
        """doc (根 + live な cut 0..i) で c を check する。前の cut (か根) の DEFECT で check が止まると c の DEFECT も lint も見えない
        (dt_18: phone の `none` の色で後の 4 cut が lint なしのまま staged になった)。持ち主の分かる cut はその cut を除いた doc で取り
        (前の cut の直しと c の直しが並列に進む)、持ち主の分からない DEFECT (根・まだ check していない cut) か、除くと c に DEFECT が出る
        (除いた cut の sticky を指す) 時は、持ち主が ready になるまで待って掛け直す。掛け直しの check を止めた新しい持ち主もまた待つ —
        掛け直しの blockers を捨てると隠れた c の DEFECT を 0 と数えて staged にした (nt03 rain: 待った後は rules の DEFECT で止まって
        いた)。待った持ち主が ready なのにまだ止める時だけ打ち切る (見える範囲で進む・残りは投入検査が拾う)。"""
        waited: set[str] = set()
        while True:
            cuts = self.live_cuts(self.order[: i + 1])
            res = self.check_cut(c, cuts, rnd)
            defects, blockers = res[2], res[4]
            if defects or not blockers:
                return res
            skip = frozenset(blockers - {"?", ROOT})
            if skip and not (blockers & {"?", ROOT}):
                skipped = self.check_without(c, cuts, skip, rnd)
                if not skipped[2] and not skipped[4]:
                    self.log(cut=c, event="lint_skip", round=rnd, skip=sorted(skip))
                    return skipped
            if blockers <= waited:
                self.log(cut=c, event="lint_blocked", round=rnd, owners=sorted(blockers), stuck=True)
                return res
            self.log(cut=c, event="lint_blocked", round=rnd, owners=sorted(blockers))
            self.wait_owners(c, blockers)
            waited |= blockers

    def owns_root(self, c: str) -> bool:
        """cut c が根の持ち主か = 動画の最初の live な cut で、根がまだ流れていない (根は最初に受理される cut と一緒に流れて凍る・
        remote は根が閉じた時点で先に流れる)。"""
        return c == self.first_live() and not self.root_submitted

    def call_role(self, args: list[str], *, timeout: int, fatal: bool = True) -> subprocess.CompletedProcess[str]:
        """役割の異常終了・タイムアウトも Codex の投入停止へ伝える。fatal=False (直し役・見直し) は伝えない — 直しは cut を良くする
        だけの段で、失敗しても直す前の版で続けられる (止めると動画ごと落ちる)。"""
        try:
            result = subprocess.run(
                args, cwd=REPO or HERE.parent, env=self.env, capture_output=True, text=True, timeout=timeout
            )
        except Exception as exc:
            if fatal:
                self.fail_engine(f"{args[2]}: {exc}")
            raise
        if result.returncode != 0 and fatal:
            self.fail_engine(f"{args[2]}: exit {result.returncode} — {result.stderr[-400:]}")
        return result

    def fail_engine(self, reason: str) -> None:
        if os.environ.get("NOLANG_STUDIO_ENGINE") == "codex":
            temporary = self.st / f"engine.failed.{time.time_ns()}"
            temporary.write_text(reason + "\n")
            temporary.replace(self.st / "engine.failed")

    def run_fixer(self, c: str, ff: Path, *, review: bool = False, shots: list[Path] | None = None) -> tuple[bool, str]:
        """直し役 (claude -p) を 1 回。通れば cut の file を書き戻す → (通ったか, 出力の末尾)。通らない = 出力が使えない (読めない・
        cut を分けた) — 呼び直せば通り得る。返らない・process が落ちた時は FixerUnavailable。根の持ち主の cut なら根の 2 file も
        直せる (`--root`)。担当・直し役の参考に前の cut の定義を渡す。review = 見直し (effort は --review)・shots = 見直しに見せる静止画。"""
        self.write_defs_before(c)
        src = self.solo / f"cut_{c}.txt"
        before = src.read_text()
        for attempt in (0, 1):
            try:
                r = self.call_role(
                    [
                        PY,
                        str(AUTHOR),
                        "fix",
                        str(self.project),
                        c,
                        str(ff),
                        *(["--root"] if self.owns_root(c) else []),
                        "--effort",
                        (self.review_effort or self.fix_effort) if review else self.fix_effort,
                        *(["--review"] if review else []),
                        *(["--shots", ",".join(str(x) for x in shots)] if shots else []),
                    ],
                    timeout=FIX_TIMEOUT_S,
                    fatal=False,
                )
            except subprocess.TimeoutExpired:
                # 直し役が返らない (codex の turn が止まる等) — 待ち続けると後の cut の投入が止まり、server の待ちの上限 (180 秒) で
                # 動画ごと落ちる。直す前の版で続ける
                self.log(cut=c, event="fix_timeout", s=FIX_TIMEOUT_S, review=review)
                raise FixerUnavailable(f"timeout {FIX_TIMEOUT_S}s") from None
            if (
                os.environ.get("NOLANG_STUDIO_ENGINE") != "codex"
                and r.returncode != 0
                and "FileNotFoundError" in r.stderr
                and attempt == 0
            ):
                time.sleep(2)  # claude の shim が一瞬見つからない事がある → 1 回だけやり直す
                continue
            break
        if r.returncode == 0 and "---timeline---" in r.stdout and cut_heads(r.stdout) != cut_heads(before):
            # 直し役が cut を分けた・改名した — 片方だけ戻ると design と timeline の cut が食い違って組み立てで落ちるので受け取らない
            self.log(cut=c, event="fix_structure_changed", before=cut_heads(before), after=cut_heads(r.stdout))
            return False, "the fix changed the cut's headings (split or renamed the cut)"
        if r.returncode == 0 and "---timeline---" in r.stdout:
            # 担当の書き戻しと同じ門: 基準は書き戻す直前の file (直し役が走る間に後の cut の thread が c の block へ移した定義
            # — move_forward_defs — も含む)。直し役が消した定義・後の cut が使う定義の形を変えた物を戻す
            with self.name_lock:
                latest = src.read_text()
                src.write_text(r.stdout)
            self.restore_defs(c, latest if "---timeline---" in latest else before, who="fixer")
            return True, r.stdout
        if r.returncode != 0:
            raise FixerUnavailable((r.stdout + r.stderr)[-200:])
        return False, r.stdout[-200:]

    def stage(self, i: int, c: str) -> None:
        """cut c が出たら doc (根 + live な cut 0..i) を組んで check → 直し (2 回まで) → staged (ready)。段の thread が死んでも旗は
        立てる (立たないと後の cut が全部待ち続ける — 死んだ cut は guarded が壊れ扱いにする)。"""
        try:
            self._stage(i, c)
        finally:
            self.staged[c] = True
            self.log(cut=c, event="staged", broken=self.broken.get(c), **self.cut_length(c))

    def cut_length(self, c: str) -> dict[str, float | None]:
        """staged の時点の cut c の尺の記録: plan の目標秒・予算 (締めは弾性)・著者の宣言 (`# 台詞 ~N s`)・check の見積り。"""
        from stream_author import DECLARED_SECONDS  # noqa: PLC0415 — scripts dir を sys.path に足している

        author = self.solo / f"author_cut_{c}.txt"
        declared = DECLARED_SECONDS.search(author.read_text()) if author.exists() else None
        estimate = self.cut_estimate.get(c)
        budget = self.cut_budget(c)
        return {
            "plan_s": self.plan_seconds().get(c),
            "budget_s": None if budget is None else round(budget, 1),
            "declared_s": float(declared.group(1)) if declared else None,
            "estimate_s": None if estimate is None else round(estimate, 1),
        }

    def _stage(self, i: int, c: str) -> None:
        while self.cut_block(c) is None:
            if (
                self.st / "src.done"
            ).exists():  # 著者が書き終えたのに構成の cut が無い (名を変えた・書き落とした) — 待ち続けない
                self.broken[c] = "not written"
                return
            time.sleep(0.3)
        self.log(cut=c, event="cut_seen")
        self.move_forward_defs(c)
        if self.staff_effort:
            self.staff(i, c)
        # 絵と声は担当が書き終えた瞬間に作り始める (check と直しに並ぶ・DEFECT の行は落として残りを作り、直しの後に差分だけ作る)
        self.start_prewarm(c)
        fix_calls = 0  # 直し役を呼んだ回数 (著者版への差し戻しも 1 回と数える)・2 回まで
        autofixes = 0  # 機械の直しを当てた回数 (check し直す)・2 回まで
        before_fix: str | None = None  # 直し役を掛ける直前の cut の text (直し役が作った DEFECT の行を戻す元)
        settled = False  # 直し役の壊した行を戻した — DEFECT が消えれば残りの指摘で直し役をもう呼ばない
        before_clean = False  # before_fix の版の check が DEFECT 0 だったか (直しが DEFECT を作ったら版ごと戻せる)
        prev_keys: set[tuple[str, str]] | None = (
            None  # 直し役を掛ける直前の check の指摘 (規則と層) — 直しが新しく作った指摘の判定
        )
        # 見直し: 最初の reviews 回の直し役は指摘に出ない弱い所・崩れも探す (--look なら静止画も・round ごとに撮り直す)。
        # 見直しの call は直し役の 2 回の上限に数えない
        reviews = 0
        if self.review_effort is not None and not self.broken.get(c):
            reviews = REVIEW_ROUNDS_LOOK if self.look else REVIEW_ROUNDS
        prev_findings: str | None = None
        # 塊だけ戻した (`revert_new_findings`) 直前の版 — 塊の戻しで design と timeline の名がずれて DEFECT になったら、
        # 直す前の版 (DEFECT 0) へまるごと戻す (改名した要素の印だけ旧名に戻り 3 回空回りした: dv nt07 shift60)
        partial_base: str | None = None
        reverted_fixes: list[str] = []  # 戻した直し役の出力 (cut の text) — 同じ edit が返ったら当てずに戻す
        failed_edits = ""  # 戻した edit の本文 — 次の直し役に「効かなかった」と添える
        last: tuple[str, list[dict[str, object]]] | None = None  # 最後の check の (cut の text, その cut の指摘)
        for rnd in itertools.count():
            t = time.time()
            dd, out, defects, lint, _blockers = self.check_settled(c, i, rnd)
            cuts = self.live_cuts(self.order[: i + 1])
            mine = [f for f in lint if f.get("cut") == c]
            if autofixes < 2 and self.autofix(c, mine, rnd, sure_only=self.warn_fixer):
                autofixes += 1
                continue  # 直した text を check し直す (直し役の回数に数えない)
            last = ((self.solo / f"cut_{c}.txt").read_text(), mine)
            fixes = [f for f in mine if self.fix_finding(f)]
            self.log(
                cut=c,
                event="check",
                round=rnd,
                s=round(time.time() - t, 1),
                defect=len(defects),
                warn=sum(1 for f in mine if f.get("severity") == "warn"),
                severe=sum(1 for f in mine if f.get("severity") == "severe"),
                fix=len(fixes),
                rules=sorted({f["rule"] for f in fixes})[:8],
            )
            (dd / f"out/check_{rnd}.txt").write_text(out)
            if defects and partial_base is not None:
                (self.solo / f"cut_{c}.txt").write_text(partial_base)
                partial_base = None
                self.log(cut=c, event="fix_reverted", round=rnd, n=len(defects), defect=len(defects), whole=True)
                settled = True
                continue
            partial_base = None
            if not defects and not self.broken.get(c):
                # lint の直しが残っていても素材は作り始める (直し役は台詞も絵の説明文も変えない約束)
                self.start_prewarm(c)
            if defects and before_fix is not None:
                fixed_text = (self.solo / f"cut_{c}.txt").read_text()
                reverted = self.revert_fixer_damage(c, cuts, before_fix, defects)
                if not reverted and before_clean:
                    # 直す前の版は DEFECT 0 だった — 直し役が警告を直しに行って DEFECT を作った (別の行に同じ印を書き足す等で、
                    # 報告の行が直し役の変更の塊の外に出る)。落とすより直す前の版の方が良いので、直しをまるごと戻す
                    (self.solo / f"cut_{c}.txt").write_text(before_fix)
                    reverted = len(defects)
                before_fix = None
                if reverted:
                    reverted_fixes.append(fixed_text)
                    failed_edits = edit_lines((self.solo / f"cut_{c}.txt").read_text(), fixed_text)
                    self.log(cut=c, event="fix_reverted", round=rnd, n=reverted, defect=len(defects))
                    settled = True
                    continue
            if not defects and before_fix is not None and prev_keys is not None:
                # 直しが新しく作った指摘 (直す前の check に無かった規則と層の組・直しの列か severe) — その層を指す行が直し役の
                # 変更の塊にあれば、その塊だけ直す前に戻す (板の印を足して空の板を作る等。最後の直しが作った欠陥は誰も直さない)
                regressed = [
                    f
                    for f in mine
                    if f.get("severity") in ("severe", "warn")
                    and (self.to_fix(f) or f.get("severity") == "severe")
                    and (str(f.get("rule", "")), str(f.get("layer", ""))) not in prev_keys
                ]
                undone = self.revert_new_findings(c, before_fix, regressed) if regressed else 0
                partial_base = before_fix if undone and before_clean else None
                before_fix = None
                if undone:
                    self.log(
                        cut=c, event="fix_regressed", round=rnd, n=undone, rules=sorted({f["rule"] for f in regressed})
                    )
                    settled = True
                    continue
            if self.fix_effort is None:
                # 直し役なし: DEFECT は最後の手段 (著者の版・DEFECT の印を落とす) だけ・指摘は直さない
                if defects and not self.rescue_stage(i, c, rnd, defects):
                    self.mark_broken(c, "DEFECT (no fixer)")
                break
            need = bool(defects) or (bool(fixes) and not settled) or reviews > 0
            if not need:
                break
            if fix_calls >= 2:
                # 捨てるのは描けない cut (DEFECT・文法と実行) だけ — 2 回直しても残る severe (配置の重なり・はみ出し …) は受け入れて
                # 描く (判断 16・描画は best effort で続く: 字の床まで縮める・そのまま描く — layout/report.py)。DEFECT も捨てる前に
                # 最後の手段 (著者版・DEFECT の印を落とす) を掛ける — 落とすと cut が台詞ごと動画から消える
                if defects and not self.rescue_stage(i, c, rnd, defects):
                    self.mark_broken(c, "DEFECT after 2 fixes")
                break
            findings = "\n".join(d.text for d in defects[:40])
            rest = (
                [f for f in mine if f.get("severity") in ("severe", "warn") and f not in fixes]
                if self.fix_scope == "warn"
                else []
            )  # warn も直す直し役にはその cut の severe / warn を全部見せる (defect / severe の run は直す指摘だけ — warn を見せると直しに行く)
            for f in (fixes + rest)[:24]:
                findings += f"\n{f.get('severity')} {f.get('rule')} ({f.get('layer', '')}): {f.get('message', '')} — {f.get('hint', '')}"
            # 見直し (全 cut 1 回目) に添えるだけ — 尺だけでは呼ばない・2 回目以降の直し役 (指摘だけを直す) に文を足させると
            # 画面の変化の無い文が増えて静止が伸びた (10-24 の両順の比べ)
            if reviews > 0 and (length := self.length_finding(c)):
                findings += "\n" + length
                self.log(
                    cut=c,
                    event="length_lint",
                    round=rnd,
                    budget_s=round(self.cut_budget(c) or 0, 1),
                    estimate_s=round(self.cut_estimate[c], 1),
                    review=reviews > 0,
                )
            if failed_edits and defects:
                # 直し役は前の round と同じ edit を返しがち (nt06 gold: 戻した edit を 1 文字も違わずにもう 1 回)。効かなかった edit を見せる
                findings += (
                    "\n\n前の直しの edit は DEFECT を消さなかったので戻した (`+` = 前の直し役が書いた行・`-` = 今の行)。"
                    f"同じ edit は返さず、別の直し方にする:\n{failed_edits}"
                )
            if findings == prev_findings and not defects and not reviews:
                # 直しても指摘が 1 つも変わらない — もう 1 回頼んでも同じ答え (直し役が触れない層・直し方の無い指摘)。打ち切る。
                # DEFECT が残る時は打ち切らない: 2 回目 (か著者版への差し替え) で通る事があり、落とすと cut が台詞ごと消える
                # (cur7_03 climax: `~` の順の DEFECT を 1 回で打ち切って落とした)
                self.log(cut=c, event="fix_stalled", round=rnd, fix=len(fixes))
                break
            prev_findings = findings
            ff = dd / f"out/findings_{rnd}.txt"
            ff.write_text(findings)
            t = time.time()
            if fix_calls and defects and c in self.author_clean and self.revert_to_author(c):
                # 直しても DEFECT が残る — 担当が触る前の著者の版 (check で DEFECT 0) に差し替えて掛け直す (2 回目の直しの
                # 代わり・通らなければ最後の手段へ)。落ちた cut は台詞ごと消えるので、文字や効果音の少ない著者の版を取る
                fix_calls += 1
                self.log(cut=c, event="revert_author", round=rnd, defect=len(defects))
                continue
            review = reviews > 0
            reviews = max(reviews - 1, 0)
            shots = self.shots(c) if review and self.look else None  # 撮れなければ (空) 画像なしで見直す
            before_fix = (self.solo / f"cut_{c}.txt").read_text()
            before_clean = not defects
            prev_keys = {
                (str(f.get("rule", "")), str(f.get("layer", "")))
                for f in mine
                if f.get("severity") in ("severe", "warn")
            }
            try:
                ok, tail = self.run_fixer(c, ff, review=review, shots=shots)
            except FixerUnavailable as error:
                self.log(cut=c, event="fix_failed", round=rnd, s=round(time.time() - t, 1), tail=str(error))
                if defects and not self.rescue_stage(i, c, rnd, defects):
                    self.mark_broken(c, "fix call failed")
                break
            if not review:
                fix_calls += 1
            if ok:
                self.log(
                    cut=c,
                    event="fix",
                    round=rnd,
                    s=round(time.time() - t, 1),
                    chars=len(tail),
                    review=review,
                    look=bool(shots),
                )
                if (self.solo / f"cut_{c}.txt").read_text() in reverted_fixes:
                    # 戻した edit をそのまま返した — 当てても同じ DEFECT で戻すだけなので当てない (次の round は 2 回の上限で最後の手段へ)
                    (self.solo / f"cut_{c}.txt").write_text(before_fix)
                    before_fix = None
                    self.log(cut=c, event="fix_same_edits", round=rnd)
            else:
                # 出力が使えなかった (読めない・cut を分けた) — 直しの回数が残っていれば呼び直す (尽きれば次の round で最後の手段)
                self.log(cut=c, event="fix_unusable", round=rnd, s=round(time.time() - t, 1), tail=tail)
                before_fix = None
        if self.warn_fixer:
            self.final_autofix(c, i, last)
        self.drop_unshown(c, i, last)

    def final_autofix(self, c: str, i: int, last: tuple[str, list[dict[str, object]]] | None) -> None:
        """warn を直す直し役が回り終えた cut c に、消極的な機械の直しも当てる (LLM がもう見ない)。指摘は最後の check の物 (text が
        その時のままの時だけ)・当てた後の check に DEFECT が出たら戻す。"""
        if last is None or self.broken.get(c):
            return
        src = self.solo / f"cut_{c}.txt"
        checked, findings = last
        if src.read_text() != checked or not self.autofix(c, [dict(f) for f in findings], "final", sure_only=False):
            return
        if self.check_settled(c, i, "final")[2]:
            with self.name_lock:
                src.write_text(checked)
            self.log(cut=c, event="autofix_reverted", round="final")

    def drop_unshown(self, c: str, i: int, last: tuple[str, list[dict[str, object]]] | None) -> None:
        """直しの後まで残った `dropped` (compile が外して描いた記述・綴りは指摘の `drop`) を cut の src から消す — 描いている物と
        書いてある物を揃える (後の編集・参照で死んだ記述が効き出さない)。指摘は今の text の check の物だけ使い、消した後の check が
        DEFECT を出したら戻す。消した綴りは log に残す (文書の穴を数える材料)。"""
        if last is None or self.broken.get(c):
            return
        src = self.solo / f"cut_{c}.txt"
        checked, findings = last
        tokens = [str(f["drop"]) for f in findings if f.get("rule") == "dropped" and f.get("drop")]
        if not tokens or src.read_text() != checked:
            return
        text = checked
        removed: list[str] = []
        for token in dict.fromkeys(tokens):
            lines = text.split("\n")
            at = next((n for n, line in enumerate(lines) if token in line), None)
            if at is None:
                continue
            lines[at] = drop_token(lines[at], token)
            text = "\n".join(lines)
            removed.append(token)
        if not removed:
            return
        with self.name_lock:
            src.write_text(text)
        if self.check_settled(c, i, "drop")[2]:
            with self.name_lock:
                src.write_text(checked)
            self.log(cut=c, event="drop_reverted", tokens=removed)
            return
        self.log(cut=c, event="dropped_unshown", n=len(removed), tokens=removed)

    def shots(self, c: str) -> list[Path]:
        """見直し役に見せる cut c の静止画 (`studio.py shots`)。run の warm (担当の直後に頼む) が解いた絵を待ち、その pin を載せた根 + c
        の doc (前の cut の名のある定義は根の後ろ) を描く。前の cut を入れないのは、その cut の直し中の DEFECT で build できず、前の
        cut の声 (尺) がまだ無ければ TTS を待つから (前の cut の sticky な層は写らない)。c の DEFECT の行は落として描く。"""
        w = self.warms[c]
        if w.thread is not None:
            w.thread.join()
        t = time.time()
        pins = self.warm_pins()
        i = self.order.index(c)
        extra = "".join(
            text
            for x in self.order[:i]
            if not self.broken.get(x) and (blk := self.cut_block(x)) is not None
            for _kind, _name, text in self.named_defs(blk[0])
        )
        dd = self.doc_dir(f"{c}.shot", [c], root_extra=extra, pins=pins)
        out = ""
        for _attempt in range(3):
            (dd / "out/defects.json").unlink(missing_ok=True)  # 落とす行は今の attempt の DEFECT だけから
            try:
                out = self.studio_cmd("shots", str(dd), "--cut", c, timeout=120)
            except subprocess.TimeoutExpired:
                out = "TIMEOUT"
                break
            if "OK shots" in out or self.drop_defect_lines(dd, c) == 0:
                break
        (dd / "out/shots.txt").write_text(out)
        paths = [Path(line.split()[1]) for line in out.splitlines() if line.startswith("SHOT ")]
        self.log(cut=c, event="shots", s=round(time.time() - t, 1), n=len(paths), ok="OK shots" in out)
        return paths

    def warm_pins(self) -> dict[str, object]:
        """run の warm で解けた絵の pin — 頼んだ絵が解けるのを待つ (増えなくなって 3 s か 90 s まで・local だけ)。"""
        seen: dict[str, object] = {}
        stable_since = time.time()
        deadline = time.time() + 90
        while time.time() < deadline:
            raw = self.call("warm_pins").get("pins")
            now = raw if isinstance(raw, dict) else {}
            if len(now) != len(seen):
                seen, stable_since = now, time.time()
            elif seen and time.time() - stable_since > 3:
                break
            time.sleep(1)
        return seen

    def revert_fixer_damage(self, c: str, cuts: list[str], before: str, defects: list[Defect]) -> int:
        """直し役の後の check で出た DEFECT が、直し役が変えた行にあれば、その変更の塊だけ直し前 (before) に戻す — 直し役を 2 回目に
        呼ばない (2 回以上の直しの 3/6 は直し役が自分で作った DEFECT: 無い変種への印・div の size=・行の構造崩れ)。行の無い DEFECT
        (RUNTIME) は直し全体を戻す。戻した DEFECT の数 (0 = 直し役の変更の外にある → 従来どおり直し役へ)。"""
        blk = self.cut_block(c)
        before_blk = self.split_block(c, before)
        ranges = self.cut_line_ranges(cuts).get(c)
        if blk is None or before_blk is None or ranges is None:
            return 0
        after_text = blk[0] + "---timeline---\n" + blk[1]
        before_text = before_blk[0] + "---timeline---\n" + before_blk[1]
        if after_text == before_text:
            return 0
        nd = blk[0].count("\n")
        bad: set[int] = set()
        whole = False
        for d in defects:
            n, k = d.line, d.which
            if n <= 1:
                whole = True
                continue
            a, b = ranges[k]
            if a <= n <= b:
                bad.add((n - a) + (0 if k == 0 else nd + 1))
        new_text = before_text if whole else revert_changed_regions(before_text, after_text, bad)
        if new_text is None or new_text == after_text:
            return 0
        (self.solo / f"cut_{c}.txt").write_text(new_text)
        return len(defects) if whole else len(bad)

    def revert_to_author(self, c: str) -> bool:
        """cut c を著者の版 (担当が触る前・solo/author_cut_<c>.txt) に差し替える。著者の版に無い名のある定義で後の cut が使う物 (後の
        cut の thread が移した定義・壊れた cut から移った定義) は残す。著者の版が無いか、差し替えても今と同じなら何もしない → 差し替えたか。"""
        keep, src = self.solo / f"author_cut_{c}.txt", self.solo / f"cut_{c}.txt"
        if not keep.exists():
            return False
        with self.name_lock:
            now, author = src.read_text(), keep.read_text()
            src.write_text(author)
            had = {(k, n) for k, n, _t in self.named_defs(author.split("---timeline---", 1)[0])}
            for kind, name, text in self.named_defs(now.split("---timeline---", 1)[0]):
                if (kind, name) not in had and self.used_later(c, name):
                    self.add_defs(c, text)
            return src.read_text() != now

    def degrade_editable_motion(self, c: str, defects: list[str], *, drop_marks: bool = False) -> int:
        """editable_motion の機械 degrade (最後の網): 違反した層の `in:`/`out:` を `fade` に書き換え、custom の `main:` を落として
        層と台詞を残す — motion 違反だけで cut が落ちない受け入れ条件の実装。的は投入検査の render 文 (`#名 の slot`) から引き、
        cut の design の行 (def の行を含む) を書き換える。的の行が引けなければ cut の design 全行を blanket で寄せる。drop_marks = その層を
        的にした `[!#層 …]` / `[=#層 …]` の印も落とす (台詞と効果音は残す) — 動きが timeline の印から来た時 (engine が `!` の効果を
        層の motion に畳む) の網。戻り = 書き換えた宣言と落とした印の数 (0 = editable_motion が無い・直す物が無い)。"""
        rows = [m for d in defects if (m := _EDITABLE_MOTION_RE.search(d)) is not None]
        if not any("editable_motion" in d for d in defects):
            return 0
        src = self.solo / f"cut_{c}.txt"
        text = src.read_text()
        design, sep, rest = text.partition("---timeline---")
        lines = design.split("\n")
        changed = 0
        targets = [(m.group("name").split(".")[-1], _MOTION_SLOT_GROUP[m.group("slot")]) for m in rows]
        for idx, line in enumerate(lines):
            hits = {slot for leaf, slot in targets if re.search(rf"#{re.escape(leaf)}(?=[(.\s]|$)", line)}
            if hits:
                lines[idx], k = _degrade_motion_decls(line, hits)
                changed += k
        if changed == 0:  # 的の行が引けない (def の実体名と定義名の揺れ等) — blanket で object 形だけ寄せる
            for idx, line in enumerate(lines):
                lines[idx], k = _degrade_motion_decls(line, None)
                changed += k
        if drop_marks and targets:
            leaves = {re.escape(leaf) for leaf, _slot in targets}
            mark = re.compile(rf"\[[!=]#(?:{'|'.join(sorted(leaves))})(?=[\s\],.{{\[]|$)[^\]]*\]")
            rest, n = mark.subn("", rest)
            changed += n
        if changed:
            src.write_text("\n".join(lines) + sep + rest)
        return changed

    def last_resort(
        self, c: str, cuts: list[str], rnd: int | str, passes: Callable[[], bool], defects: list[str] | None = None
    ) -> bool:
        """直しきれない DEFECT で cut c を捨てる前の最後の手段 (stage と投入検査で同じ順)。(a) 著者の版に差し替えて passes() で通れば
        取る (`revert_author`)。(a2) 呼び手が渡す defects (stage の check か投入検査の ack の DEFECT) に editable_motion があれば機械 degrade (`degrade_editable_motion`) → passes() で通れば取る。(b) doc (根 +
        cuts・c が最後) の check で c の block の行を指す DEFECT を doc から落とし (warm の
        drop_defect_lines と同じ — 台詞は残して印だけ落とす) c の block を書き戻す → passes() で通れば取る (`defect_lines_dropped`)。
        どれも通らなければ元の text に戻して False (捨てるのは呼び手)。"""
        src = self.solo / f"cut_{c}.txt"
        current = src.read_text()
        if self.revert_to_author(c):
            if passes():
                self.log(cut=c, event="revert_author", round=rnd, last_resort=True)
                return True
            src.write_text(current)
        if defects:
            # 1 段目 = 違反した層の宣言を preset へ・2 段目 = それでも通らなければその層の `!` / `=` の印も落とす (動きが印から
            # 畳まれた形 — design に直す行が無い時の網)
            for drop_marks in (False, True):
                degraded = self.degrade_editable_motion(c, defects, drop_marks=drop_marks)
                if degraded and passes():
                    self.log(
                        cut=c,
                        event="editable_motion_degraded",
                        round=rnd,
                        n=degraded,
                        marks=drop_marks,
                        last_resort=True,
                    )
                    return True
                src.write_text(current)
        dropped = 0
        for _attempt in range(4):
            dd = self.doc_dir(f"{c}.drop", cuts)
            self.check(dd, ended=cuts[-1] == self.order[-1])
            n = self.drop_defect_lines(dd, c)
            block = self.block_in_doc(dd, c)
            if n == 0 or block is None:
                break
            dropped += n
            src.write_text(block)
            if passes():
                self.log(cut=c, event="defect_lines_dropped", round=rnd, n=dropped)
                return True
        src.write_text(current)
        return False

    def rescue_stage(self, i: int, c: str, rnd: int | str, defects: list[Defect]) -> bool:
        """stage の最後の手段 — 通ったか = doc (根 + live な cut 0..i) の check で c の DEFECT も止める持ち主も無い。"""

        def passes() -> bool:
            res = self.check_settled(c, i, rnd)
            return not res[2] and not res[4]

        return self.last_resort(c, self.live_cuts(self.order[: i + 1]), rnd, passes, [d.text for d in defects])

    def revert_new_findings(self, c: str, before: str, findings: list[dict[str, object]]) -> int:
        """直しが新しく作った指摘の層を指す行 (section の `#名(`・印の `#名`) のうち、直し役が変えた塊にある物を直す前 (before) に
        戻す。板の子の層 (`板._board`) は板の名でも引く。戻した指摘の数 (0 = 直し役の変更の外 → そのまま)。"""
        blk = self.cut_block(c)
        before_blk = self.split_block(c, before)
        if blk is None or before_blk is None:
            return 0
        after_text = blk[0] + "---timeline---\n" + blk[1]
        before_text = before_blk[0] + "---timeline---\n" + before_blk[1]
        if after_text == before_text:
            return 0
        bad, hit = rows_naming_layers(after_text, [str(f.get("layer", "")) for f in findings])
        new_text = revert_changed_regions(before_text, after_text, bad) if bad else None
        if new_text is None or new_text == after_text:
            return 0
        (self.solo / f"cut_{c}.txt").write_text(new_text)
        return hit

    def staff(self, i: int, c: str) -> None:
        """担当 (Opus) が著者の cut を仕上げる。前の cut は著者の版を渡すので cut ごとに並列に走る。
        著者の版は solo/author_cut_<名>.txt に残す (次の cut の参考・差分の検証)。担当は台詞も直してよい (声は担当の版から作る)。
        逐語の台本の動画だけ、担当が台詞の文字を変えていたら著者の版の文字に戻す (`restore_speech`・読点の追加と読みの指定は許す —
        後段では戻せない・`speech_restored`)。keep_assets の run は台詞を読点・行の割り方まで、絵を説明文まで著者の版に戻す
        (`restore_pictures`・`pictures_restored` — 素材は著者の版から先に作っている)。"""
        from stream_author import (  # noqa: PLC0415 — scripts dir を sys.path に足している
            restore_pictures,
            restore_speech,
        )

        src = self.solo / f"cut_{c}.txt"
        keep = self.solo / f"author_cut_{c}.txt"
        # 著者版の check は担当の前に回し、指摘を担当に渡す (check の 1.6 s を浮かせる並走は担当後の DEFECT を増やした)。直し方が
        # 一つに決まる指摘は check が機械で直してから (著者の版 = 直した版)
        ff = self.author_check(i, c)
        if not keep.exists():
            keep.write_text(src.read_text())
        if self.keep_assets:
            # 担当は絵と台詞を変えない — 著者の版のまま素材を頼み、担当と並列に作る
            self.start_prewarm(c)
        self.write_defs_before(c)
        before = src.read_text()  # 担当の前の block (著者の版 + 前方から移した定義) — 担当が消した定義を戻す基準
        t = time.time()
        r = self.call_role(
            [
                PY,
                str(AUTHOR),
                "staff",
                str(self.project),
                c,
                str(ff),
                "--effort",
                self.staff_effort or "medium",
                *(["--keep-assets"] if self.keep_assets else []),
            ],
            timeout=900,
        )
        if r.returncode == 0 and "---timeline---" in r.stdout:
            # 戻す基準は書き戻す直前の file — 担当の裏で前方から移された定義 (move_forward_defs) も含める (担当開始時の text だと
            # その定義が担当の出力に無いまま上書きされて消える)
            author = keep.read_text()
            text, restored = (
                restore_speech(author, r.stdout, exact=self.keep_assets)
                if self.verbatim or self.keep_assets
                else (r.stdout, [])
            )
            pictures: list[dict[str, str]] = []
            if self.keep_assets:
                text, pictures = restore_pictures(author, text)
            # 担当の版を分けて残す (cut_<名>.txt は直し役が上書きする最終の版)
            (self.solo / f"staff_cut_{c}.txt").write_text(text)
            with self.name_lock:
                latest = src.read_text()
                src.write_text(text)
            self.log(cut=c, event="staff", s=round(time.time() - t, 1), chars=len(r.stdout))
            if restored:
                self.log(cut=c, event="speech_restored", n=len(restored), lines=restored)
            if pictures:
                self.log(cut=c, event="pictures_restored", n=len(pictures), pictures=pictures)
            self.restore_defs(c, latest if "---timeline---" in latest else before, who="staff")
        else:
            self.log(cut=c, event="staff_failed", s=round(time.time() - t, 1), tail=(r.stdout + r.stderr)[-200:])

    def restore_defs(self, c: str, before: str, *, who: str) -> None:
        """担当か直し役 (who) が書き戻した cut c の block の名のある定義 (def・motion・run・svg・sound・image・cue) を、書き戻す前の text
        (before) と比べて直す。担当・stage の直し役・投入検査の直し役の 3 つの出口が全部この門を通る (直し役も定義の形を変える —
        直し役だけ素通りだと、投入検査の直し役 1 回が後の cut の安全網になっていた)。
        - 消した定義は戻す (`reason: missing`・前の cut も同じ種と名で定義していれば重複の直しなので戻さない)。後の cut はその名を使っていて (並列に書き直すので担当は知らない)、消えると後の cut だけが
          DEFECT:KEY を食って直し役を 1〜2 回払っていた (担当後の DEFECT 率 cut 0 6% vs 後の cut 12〜19%・code の 27/37 が KEY・o6_03 の
          `def kw`)。戻した定義が使われなければ無害 (未使用の def)。
        - 後の cut が使う定義の形 (`def_shape`) を変えていたら、元の定義 (字下げの子ごと) に戻す (`reason: shape`)。形 = 引数の並び
          (`def_signature`) と、後の cut が `実体.子` で参照する子の名 (`children_used_later`)。後の cut は著者の版の形で書かれている —
          now7_05 の normal の担当が `def node(i, t, c=$a)` を `node(p, t, n)` に書き換え、先に staged の reverse が投入検査の
          DEFECT:ARG で落ちて台詞ごと消えた。子の名 (`icon#i` → `img#p`) だけを変えても後の cut の `[!#rv_f[1].i …]` が DEFECT:KEY に
          なる。変えた側の版の `def` は `名_<cut>` に改名してこの block の使い方ごと残す (担当・直し役の絵は変えない)。def 以外の種は
          元に戻すだけ (この cut の使い方が新しい形なら check の DEFECT で直し役に回る)。
        同じ名・同じ形のまま見た目 (大きさ・余白・色) を変えた定義は、担当なら形の変更と同じに扱う (後の cut の担当は元の見た目で並列に
        置いている)。直し役は DEFECT を直すために定義の中身を変えるので触らない。戻した時は `defs_restored` に `who` を記録する。"""
        blk = self.cut_block(c)
        if blk is None or "---timeline---" not in before:
            return
        # 種ごとに見る — 名だけで見ると、雛形の `motion note` が残っているだけで担当が消した `def note` を「残っている」と誤り、後の cut の
        # `note#…` が投入検査の DEFECT:KEY で落ちた (o20_18 power・88 本で 3 件・全部 note)
        now = {(kind, name): text for kind, name, text in self.named_defs(blk[0])}
        # 前の cut が同じ種と名で定義していれば消したのは重複の直し (直し役が DEFECT:NAME を消した) — 戻さない
        earlier = {(kind, name) for kind, name, _t in self.named_defs(self.defs_before(c))}
        missing: list[tuple[str, str]] = []
        reshaped: list[tuple[str, str, str, str]] = []
        lost: dict[str, list[str]] = {}  # 名 → 後の cut が参照するのに消えた子の名
        for kind, name, text in self.named_defs(before.split("---timeline---", 1)[0]):
            cur = now.get((kind, name))
            if cur is None:
                if (kind, name) not in earlier:
                    missing.append((name, text))
                continue
            gone = sorted(self.children_used_later(c, name, def_children(text)) - def_children(cur))
            # 担当は見た目 (大きさ・余白・色) も変えない — 後の cut の担当は元の見た目で並列に置いている (nw1 の判子 52 → 112px で
            # 後の 2 cut がはみ出した・10-22)。直し役は DEFECT の直しで定義の中身を変えるので形だけを見る
            looks = who == "staff" and re.sub(r"\s+", " ", cur).strip() != re.sub(r"\s+", " ", text).strip()
            if (self.def_signature(cur) != self.def_signature(text) or gone or looks) and self.used_later(c, name):
                reshaped.append((kind, name, cur, text))
                if gone:
                    lost[name] = gone
        for _name, text in missing:
            self.add_defs(c, text)
        if missing:
            self.log(cut=c, event="defs_restored", who=who, reason="missing", names=[name for name, _ in missing])
        if not reshaped:
            return
        f = self.solo / f"cut_{c}.txt"
        design, sep, timeline = f.read_text().partition("---timeline---")
        kept: dict[str, str] = {}
        for kind, name, cur, text in reshaped:
            if kind != "def":
                design = design.replace(cur, text, 1)
                continue
            taken = {n for _k, n, _t in self.named_defs(design)}
            new = f"{name}_{re.sub(r'[^a-z0-9]', '', c.lower())[:8] or 'c'}"
            while new in taken:
                new += "x"
            # 変えた側の def の見出し・この block の要素の型 (`名#…`)・他の def の土台 (`= 名(`) を新しい名に。元の定義はその後ろに戻す
            uses = re.compile(rf"(?<![\w#.$-]){re.escape(name)}(?=[#(])")
            design = uses.sub(new, design).replace(uses.sub(new, cur), uses.sub(new, cur) + text, 1)
            kept[name] = new
        f.write_text(design + sep + timeline)
        self.log(
            cut=c,
            event="defs_restored",
            who=who,
            reason="shape",
            names=[name for _k, name, _c, _t in reshaped],
            was=[self.def_signature(text) for _k, _n, _c, text in reshaped],
            now=[self.def_signature(cur) for _k, _n, cur, _t in reshaped],
            lost_children=lost,
            kept_as=kept,
        )

    @staticmethod
    def def_signature(text: str) -> str:
        """名のある定義の引数の形 = 名の直後の `(…)` (引数の並びと既定値・括弧の入れ子を数える・空白は詰める)。引数の無い定義は空。"""
        head = text.split("\n", 1)[0]
        m = _NAMED_DEF.match(head)
        rest = head[m.end() :].lstrip() if m else ""
        depth = 0
        for k, ch in enumerate(rest if rest.startswith("(") else ""):
            depth += {"(": 1, ")": -1}.get(ch, 0)
            if depth == 0:
                return re.sub(r"\s+", "", rest[: k + 1])
        return ""

    def used_later(self, c: str, name: str) -> bool:
        """名 name を c より後の cut (著者の版か今の版) が使っているか。著者がまだ書き終えていなければ後の cut が分からない — 使うと見る。"""
        if not (self.st / "src.done").exists():
            return True
        pattern = re.compile(rf"(?<![\w#.]){re.escape(name)}(?![\w-])")
        for x in self.order[self.order.index(c) + 1 :]:
            for f in (self.solo / f"cut_{x}.txt", self.solo / f"author_cut_{x}.txt"):
                if f.exists() and pattern.search(f.read_text()):
                    return True
        return False

    def children_used_later(self, c: str, name: str, children: set[str]) -> set[str]:
        """定義 name の子の名 (children) のうち、c より後の cut (著者の版か今の版) が `実体.子` / `実体[k].子` で参照する物。実体 =
        その cut の block の `name#実体(` の行。著者がまだ書き終えていなければ後の cut が分からない — 全部を参照すると見る (`used_later`)。"""
        if not children:
            return set()
        if not (self.st / "src.done").exists():
            return set(children)
        instance = re.compile(rf"(?<![\w#.$-]){re.escape(name)}#([A-Za-z_][\w-]*)")
        used: set[str] = set()
        for x in self.order[self.order.index(c) + 1 :]:
            for f in (self.solo / f"cut_{x}.txt", self.solo / f"author_cut_{x}.txt"):
                if not f.exists():
                    continue
                text = f.read_text()
                for inst in set(instance.findall(text)):
                    refs = re.findall(rf"(?<![\w-]){re.escape(inst)}(?:\[[^\]]*\])?\.([A-Za-z_][\w-]*)", text)
                    used |= children & set(refs)
        return used

    # ---- warm ----
    # svg に焼く箱の行で、焼く絵を変えない宣言 (位置・動き・重なり) — これだけの直しは warm を掛け直さない
    _BOX_SKIP = frozenset(
        {"left", "top", "right", "bottom", "cx", "cy", "x", "y", "z-index", "in", "out", "main", "overlap"}
    )
    # 素材にならない行の tag (文字・絵は別に見る・def / cue は定義)
    _NOT_BOX = frozenset({"p", "h1", "h2", "h3", "h4", "span", "subtitle", "img", "def", "cue"})

    @classmethod
    def box_key(cls, line: str) -> tuple[object, ...] | None:
        """箱 (div / shape / veil / def の実体 / icon …) の行から、焼く絵を決める物 (型・大きさ・塗り・縁・影・中身) を取る。
        暗い palette の div は既定で glass・gradient / 影つきの箱は svg に焼かれ (`settle_paint_kinds`)、直しがその行を足す / 変えると
        stream が seal の時に resource-service で描く (3〜7 s・o27_03) — warm の鍵に入れて掛け直す。位置と動きは焼く絵を変えない。"""
        m = re.match(r"^\s*([A-Za-z_][\w-]*)(?:#\S*)?\(((?:[^()]|\([^()]*\))*)\)\s*(.*)$", line)
        if m is None or m.group(1) in cls._NOT_BOX:
            return None
        decls: list[str] = []
        depth, cur = 0, ""
        for ch in m.group(2):  # `;` で切る (in:{…} の中の `,` と `(…)` は切らない)
            if ch in "({[":
                depth += 1
            elif ch in ")}]":
                depth -= 1
            if ch == ";" and depth == 0:
                decls.append(cur)
                cur = ""
            else:
                cur += ch
        decls.append(cur)
        kept = frozenset(d.strip() for d in decls if d.strip() and d.split(":", 1)[0].strip() not in cls._BOX_SKIP)
        return (m.group(1), kept, m.group(3).strip())

    @classmethod
    def asset_key(cls, text: str) -> tuple[object, ...]:
        """cut の text のうち素材を決める物 (絵の説明文・台詞の文字 (印を除く)・効果音の説明・svg に焼く箱の見た目) — これが同じなら
        warm を掛け直さない (位置だけの直しは絵も声も変えない)。"""
        from stream_author import _without_marks  # noqa: PLC0415 — scripts dir を sys.path に足している

        # 集合で見る (並びと重複は素材を変えない — 直し役が img の行を section の行と一緒に書き直して 2 行になり、同じ絵なのに warm を
        # 掛け直した・o7_03 situation 17 s)
        lines = text.splitlines()
        pictures = frozenset(
            m.group(1).strip() for l in lines if (m := re.match(r"^\s*img#\S+\((?:[^()]|\([^()]*\))*\)\s*(.*)$", l))
        )
        speech = frozenset(_without_marks(l) for l in lines if l.lstrip().startswith("@"))
        boxes = frozenset(k for l in lines if (k := cls.box_key(l)) is not None)
        return (pictures, speech, frozenset(_SE.findall(text)), boxes)

    def start_prewarm(self, c: str) -> None:
        """cut c の素材 (絵・声) を run に先に作らせる (staged を待たずに・直しと並ぶ): 担当の直後と、check で DEFECT 0 を見た時点。
        頼みは返事を待たずに run が裏で解く (`warm` — 動画には入らない)。走っている頼み・通った頼みがあれば頼み直さない (直しで素材を
        決める物 = asset_key が変わっていれば頼み直す)。"""
        w = self.warms[c]
        f = self.solo / f"cut_{c}.txt"
        if (w.thread is not None and w.thread.is_alive()) or self.video_id is None:
            return
        if c in self.submitted or not f.exists() or (w.ok and w.key == self.asset_key(f.read_text())):
            return
        w.thread = threading.Thread(target=self.request_warm, args=(c,), daemon=True)
        w.thread.start()

    def request_warm(self, c: str) -> None:
        """run に cut c の素材を先に作らせる (`drafts/{id}/warm/`)。text = 根 (まだ流れていなければ) + 構成の順で c までの未投入の
        cut。投入と同じ検査で弾かれた頼み (前の cut が直しの途中) は記録だけして、次の契機に頼み直す。"""
        w = self.warms[c]
        w.key = self.asset_key((self.solo / f"cut_{c}.txt").read_text())
        parts: list[str] = []
        for x in self.order[: self.order.index(c) + 1]:
            if x in self.submitted or self.broken.get(x):
                continue
            blk = self.cut_block(x)
            if blk is None:
                continue
            parts.append(blk[0].rstrip("\n") + "\n" + blk[1].rstrip("\n") + "\n")
        text = "".join(parts)
        if not self.root_submitted:
            rd, rt = self.root()
            text = rd.rstrip("\n") + "\n" + "\n".join(l for l in rt.splitlines() if l.strip() != "#v2") + "\n" + text
        t = time.time()
        try:
            self.call("warm", {"text": text})
        except (Rejected, RuntimeError) as e:
            w.ok = False
            self.log(cut=c, event="warm", ok=False, s=round(time.time() - t, 1), error=str(e)[:300])
            return
        w.ok = True
        self.log(cut=c, event="warm", ok=True, s=round(time.time() - t, 1), cuts=len(parts))

    @staticmethod
    def drop_defect_lines(dd: Path, c: str) -> int:
        """warm の doc (dd) の out/defects.json のうち cut c の block の行を指す DEFECT を doc から外す → 直した行の数。design の行は
        その行と字下げの子を消す。timeline の台詞行は消さずに印 (`[…]`・効果音の `[♪…]` は残す) だけ落とす — 消した層を指す印の DEFECT で
        台詞 (TTS の元) まで消えて「台詞行が無い」に連鎖した (o6_03)。block の範囲は doc の text から引く (`section#c` / `*** c` から次の
        cut の頭まで)。"""
        defects = Run.read_defects(dd)
        if not defects:
            return 0
        total = 0
        for which in ("design", "timeline"):
            path = dd / f"{which}.txt"
            lines = path.read_text().split("\n")
            span = Run.block_span(lines, which, c)
            if span is None:
                continue
            start, end = span
            kill: set[int] = set()
            stripped: dict[int, str] = {}
            for d in defects:
                if d.level != "DEFECT" or d.file != f"{which}.txt":
                    continue
                n = d.line
                if not (start < n < end) or n in kill or n in stripped:  # block の頭 (section / *** の行) は落とさない
                    continue
                row = lines[n - 1]
                if which == "timeline" and row.lstrip().startswith("@"):
                    bare = _MARK_NOT_SE.sub("", row)
                    if bare != row:
                        stripped[n] = bare
                        continue
                kill.add(n)
                j = n + 1
                while j < end and lines[j - 1].startswith((" ", "\t")):
                    kill.add(j)
                    j += 1
            if kill or stripped:
                total += len(kill) + len(stripped)
                path.write_text(
                    "\n".join(stripped.get(k, line) for k, line in enumerate(lines, start=1) if k not in kill)
                )
        return total

    @staticmethod
    def block_span(lines: list[str], which: str, c: str) -> tuple[int, int] | None:
        """doc の design / timeline の行の中で cut c の block の [頭の行, 次の cut の頭の行) (1 始まり)。`section#c` / `*** c` から次の
        cut の頭まで。無ければ None。"""
        head, nxt = (
            (re.compile(rf"^section#{re.escape(c)}\b"), re.compile(r"^section#"))
            if which == "design"
            else (re.compile(rf"^\*\*\* {re.escape(c)}\s*$"), re.compile(r"^\*\*\* "))
        )
        start = next((k for k, line in enumerate(lines, start=1) if head.match(line)), None)
        if start is None:
            return None
        end = next((k for k, line in enumerate(lines[start:], start=start + 1) if nxt.match(line)), len(lines) + 1)
        return start, end

    @staticmethod
    def block_in_doc(dd: Path, c: str) -> str | None:
        """doc (dd) の中の cut c の block を cut の file の形 (design + `---timeline---` + timeline) で。"""
        parts: list[str] = []
        for which in ("design", "timeline"):
            lines = (dd / f"{which}.txt").read_text().split("\n")
            span = Run.block_span(lines, which, c)
            if span is None:
                return None
            parts.append("\n".join(lines[span[0] - 1 : span[1] - 1]).strip("\n") + "\n")
        return parts[0] + "---timeline---\n" + parts[1]

    def author_check(self, i: int, c: str) -> Path:
        """著者の版 (担当が触る前) を check し、DEFECT 0 なら author_clean に (revert_author の元)。指摘の file を返す (担当へ)。"""
        t = time.time()
        cuts = self.live_cuts(self.order[: i + 1])
        dd, out, defects, lint, blockers = self.check_cut(c, cuts, "author")
        clean = not defects and not blockers  # 止まった check では c の実行の DEFECT が見えない
        if blockers - {"?", ROOT}:
            # 前の cut (著者の版) の DEFECT で check が止まり lint が出ない — その cut を除いた doc で c の lint を取る (除いた cut の
            # 定義は根の後ろに写す — c が使う名を失った誤った DEFECT で unclean にしない)。判定は c の行に落ちる DEFECT で数える
            skip = frozenset(blockers - {"?", ROOT})
            dd, out, skipped, lint, rest = self.check_without(c, cuts, skip, "author")
            clean = not defects and not skipped and not rest
        if clean:
            self.author_clean.add(c)
        mine = [f for f in lint if f.get("cut") == c]
        fixed = self.autofix(c, mine, "author", sure_only=True)  # 担当がこの後に見る
        mine = [f for f in mine if f not in fixed]  # 機械で直した指摘は担当に渡さない
        # 担当には DEFECT と severe だけ (warn は渡さない — 思考の裾が減り担当 max 241 → 124 s・warn は後段の機械の直しが
        # 当たる物だけ直る。品質は揺れの縁: C 33-34 / C2 47-68・10-26 の 2 bench)
        staffed = [f for f in mine if f.get("severity") == "severe"]
        findings = "\n".join(d.text for d in defects[:20]) + "".join(
            f"\n{f.get('severity')} {f.get('rule')} ({f.get('layer', '')}): {f.get('message', '')} — {f.get('hint', '')}"
            for f in staffed[:30]
        )
        ff = dd / "out/findings_author.txt"
        ff.write_text(findings)
        (dd / "out/timing_author.txt").write_text(cut_timing(out, c))  # 担当が読む (stream_author の staff・指摘の隣)
        self.log(cut=c, event="check", round="author", s=round(time.time() - t, 1), defect=len(defects), warn=len(mine))
        if c in self.cut_estimate:
            self.log(
                cut=c,
                event="plan_estimate",
                plan_s=self.plan_seconds().get(c),
                estimate_s=round(self.cut_estimate[c], 1),
            )
        return ff

    @property
    def warn_fixer(self) -> bool:
        """warn も直す直し役がいる (`--fix low`)。いなければ担当の後の check からは LLM が warn を見ない。"""
        return self.fix_effort is not None and self.fix_scope == "warn"

    def autofix(self, c: str, findings: list[dict], rnd: int | str, *, sure_only: bool) -> list[dict]:
        """check の指摘のうち直し方が一つに決まる物 (`autofix`) を cut c の block に機械で当てる → 当てた指摘 (LLM に渡さない)。
        sure_only = 積極的な直しだけ (後に担当か warn を直す直し役が残る時 — 消極的な物は指摘のまま LLM へ)。"""
        from stream_author import apply_autofix  # noqa: PLC0415 — scripts dir を sys.path に足している

        src = self.solo / f"cut_{c}.txt"
        with self.name_lock:
            text, applied = apply_autofix(
                src.read_text(), [f for f in findings if f.get("autofix")], sure_only=sure_only
            )
            if applied:
                src.write_text(text)
        if applied:
            self.log(
                cut=c,
                event="autofix",
                round=rnd,
                sure_only=sure_only,
                n=len(applied),
                fixes=[str(f.get("autofix")) for f in applied],
            )
        return applied

    def guarded(self, fn, i: int, c: str) -> None:
        """段の thread が例外で死んだ cut は壊れ扱い (旗は段 (stage / warm) が finally で立てる)。"""
        try:
            fn(i, c)
        except Exception as exc:  # noqa: BLE001 — 1 cut の失敗で動画全体を止めない
            self.broken[c] = f"{fn.__name__} crashed: {exc!r}"[:200]
            self.log(cut=c, event="stage_crashed", stage=fn.__name__, error=repr(exc)[:300])

    # ---- run の開始と終わり ----
    def remote_get(self, path: str) -> dict[str, object]:
        req = urllib.request.Request(f"{self.remote}{path}", headers={"Authorization": f"Bearer {self.token}"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def remote_post(self, path: str, body: dict[str, object]) -> dict[str, object]:
        """remote の POST (止めた頼み = HTTP の 400 は応答の中身に `status: 400` を足して返す)。"""
        req = urllib.request.Request(
            f"{self.remote}{path}",
            data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code != 400:
                raise
            return {"status": 400, "error": e.read().decode("utf-8", "replace")[:600]}

    def speech_file_ids(self) -> list[str]:
        """持ち込み音声 (`--speech` — project/speech.json の sources) の id。無ければ空。"""
        path = self.project / "speech.json"
        if not path.is_file():
            return []
        return [str(source["file_id"]) for source in json.loads(path.read_text()).get("sources", [])]

    def fetch_speech(self, speech_ids: str) -> int:
        """持ち込み音声 (`--speech <id>[,<id>]`) の clip 台帳と著者に貼る節 (製品の著者と同じ文 — 正本は server) を受けて
        project/speech.json に書く (著者が読む)。`POST drafts/speeches/` が未転写の音声の転写を起こすので、ready になるまで待つ。
        remote だけ (手元の描画はまだ持ち込み音声の lane を持たない)。取れなければ止める (戻り 1)。"""
        if self.remote is None:
            self.log(event="speech_failed", error="--speech は --remote (NoLang API) だけ")
            return 1
        _kind, _aspect, seconds = (self.project / "params.txt").read_text().split()[:3]
        body: dict[str, object] = {"speech_file_ids": [x for x in speech_ids.split(",") if x], "language": "ja"}
        if seconds.isdigit():
            body["seconds"] = int(seconds)
        deadline = time.time() + SPEECH_WAIT_S
        transcribing = False
        while True:
            try:
                got = self.remote_post("/v1/unstable/drafts/speeches/", body)
            except (urllib.error.URLError, ValueError) as e:
                self.log(event="speech_failed", error=str(e)[:300])
                return 1
            if got.get("status") == "ready":
                (self.project / "speech.json").write_text(json.dumps(got, ensure_ascii=False))
                self.log(event="speech", sources=got.get("sources"), target_seconds=got.get("target_seconds"))
                return 0
            if got.get("status") != "transcribing" or time.time() > deadline:
                self.log(event="speech_failed", error=str(got)[:300])
                return 1
            if not transcribing:
                print("持ち込み音声を文字起こし中 …", flush=True)
                transcribing = True
            time.sleep(SPEECH_POLL_S)

    def fetch_reference(self, video_id: str) -> int:
        """参照の動画 (`--ref` / 依頼の `[video:id]`) の src と「ユーザーが選んだ形」の節を受けて project/reference.json に書く
        (著者が読む)。local は同じ flow 関数 (`studio.py api reference`)・remote は `GET drafts/templates/{id}/`。節の文は server が
        組む (正本 `reference_brief.py`) — 依頼の秒数と editable を渡す。取れなければ参照なしで続ける (戻り 1)。"""
        _kind, _aspect, seconds = (self.project / "params.txt").read_text().split()[:3]
        profile = "editable" if self.editable else None
        try:
            if self.remote is None:
                body: dict[str, object] = {"video_id": video_id, "profile": profile}
                if seconds.isdigit():
                    body["seconds"] = int(seconds)
                out = self.studio_cmd("api", "reference", timeout=600, stdin=json.dumps(body, ensure_ascii=False))
                last = next((l for l in reversed(out.strip().splitlines()) if l.startswith("{")), None)
                if last is None:
                    raise RuntimeError(out[-400:])
                got = json.loads(last)
            else:
                query = urllib.parse.urlencode(
                    {k: v for k, v in (("profile", profile), ("seconds", seconds if seconds.isdigit() else None)) if v}
                )
                got = self.remote_get(f"/v1/unstable/drafts/templates/{video_id}/" + (f"?{query}" if query else ""))
        except (RuntimeError, urllib.error.URLError, ValueError) as e:
            self.log(event="reference_failed", video_id=video_id, error=str(e)[:300])
            return 1
        if got.get("status") == 400 or not got.get("brief"):
            self.log(event="reference_failed", video_id=video_id, error=str(got.get("error") or got)[:300])
            return 1
        (self.project / "reference.json").write_text(json.dumps(got, ensure_ascii=False))
        self.log(event="reference", video_id=video_id, source=got.get("source"), title=got.get("title"))
        return 0

    def start(self) -> None:
        """run を開く (plan が閉じた時点)。remote は `drafts/` (視聴 URL はこの時点で出る — server の video page が追いかけ再生する)・
        local は `studio.py stream` (API の start と同じ行を作り、video の id を stream/video.json に書く)。"""
        t = time.time()
        if self.remote is None:
            self.start_stream()
            video = self.st / "video.json"
            while not video.exists() and self.stream_alive():
                time.sleep(0.2)
            if video.exists():
                self.video_id = str(json.loads(video.read_text())["video_id"])
            self.log(event="started", s=round(time.time() - t, 1), video_id=self.video_id)
            return
        kind, aspect, seconds = (self.project / "params.txt").read_text().split()[:3]
        title = (self.project / "request.txt").read_text().strip().splitlines()[0][:200]
        body: dict[str, object] = {"title": title, "aspect_ratio": aspect, "language": "ja"}
        if seconds.isdigit():  # `auto` (長さの指定なし) は送らない
            body["duration_s"] = int(seconds)
        if self.editable:
            body["editable"] = True
        reference = self.project / "reference.json"
        if reference.is_file():  # 参照から作る run — editable の線を参照の量まで緩める (server が参照を測る)
            body["reference_video_id"] = json.loads(reference.read_text())["template_video_id"]
        if speech_ids := self.speech_file_ids():  # 持ち込み音声 — 投入検査と worker が同じ clip 台帳で `@clip` を解く
            body["speech_file_ids"] = speech_ids
        req = urllib.request.Request(
            f"{self.remote}/v1/unstable/drafts/",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            r = json.loads(resp.read().decode("utf-8"))
        self.video_id = str(r["video_id"])
        self.watch_url = str(r["watch_url"])
        self.log(event="started", s=round(time.time() - t, 1), video_id=self.video_id, watch_url=self.watch_url)
        print(f"WATCH {self.watch_url}", flush=True)

    def abort(self, reason: str) -> None:
        """run を中断する (`drafts/{id}/` の DELETE — run を即解放する)。"""
        if self.video_id is None:
            return
        try:
            self.call("abort")
            self.log(event="aborted", reason=reason)
        except (Rejected, RuntimeError, urllib.error.URLError) as e:
            self.log(event="abort_failed", reason=reason, error=str(e)[:200])

    def remote_wait(self) -> int:
        """server の完成 (status completed) を待つ。途中、見る人が再生を始められる時点 (status の `playable` = 公開 manifest が S3 に
        載った) を 1 回だけ `playable` に記録して `PLAYABLE <url>` を出す (local の `playable` と同じ名 — stream_make の集計が読む)。
        poll の 1 回の失敗 (reload 中の 500 等) では止めない — 続けて失敗する時だけ諦める。"""
        playable_seen = False
        failures = 0
        while True:
            if self.engine_failed():
                return self.abort_engine()
            try:
                r = self.remote_get(f"/v1/videos/{self.video_id}/")
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
                failures += 1
                self.log(event="remote_poll_failed", n=failures, error=str(e)[:200])
                if failures >= 20:
                    return 1
                time.sleep(3)
                continue
            failures = 0
            if not playable_seen and r.get("playable"):
                playable_seen = True
                self.log(event="playable", video_id=self.video_id)
                print(f"PLAYABLE {self.watch_url}", flush=True)
            st = str(r.get("status"))
            if st in ("completed", "failed", "expired"):
                if st == "completed":
                    self.write_back()
                self.log(
                    event="final_ready" if st == "completed" else "final_failed",
                    since_launch=round(time.time() - self.t0, 1),
                    status=st,
                    broken=self.broken,
                )
                return 0 if st == "completed" else 1
            time.sleep(3)

    def local_wait(self) -> int:
        """この機械の run (`studio.py stream`) の完走を待つ。"""
        assert self.stream_proc is not None
        try:
            code = self.stream_proc.wait(timeout=1800)
        except subprocess.TimeoutExpired:
            self.stream_proc.kill()
            code = -9
        if code == 0 and (self.studio / "out/video.mp4").exists():
            self.write_back()
            (self.studio / "DONE").touch()
            self.log(event="final_ready", since_launch=round(time.time() - self.t0, 1), broken=self.broken)
            self.log(event="length_gap", **self.length_gap())
            return 0
        # 製品の run が完走しなかった (seal 後の worker の失敗など) — 製品の失敗はそのまま失敗にする (solo の render で描き直す
        # fallback は製品の bug を 2 件隠し、視聴者が見た HLS とも別物だった)
        self.log(event="final_failed", code=code, broken=self.broken)
        return 1

    def start_stream(self) -> None:
        """`studio.py stream <project>` を起こす (plan が閉じた時点 — Django と GPU の初期化を最初の cut の経路の外に置く)。
        常駐 server には委ねない (run の間ずっと生きる GPU の process)。"""
        env = {k: v for k, v in self.env.items() if k != "STUDIO_SERVER_SOCK"}
        # stream (organizer + 描画) は check / claude CLI と同じ機械で CPU を取り合う (4 core で load 3〜4.5)。止まりを決めるのは
        # stream の尾なので、こちらを優先する (root でなければ nice は上げられない — その時は素のまま)
        self.stream_proc = subprocess.Popen(
            [PY, str(STUDIO), "stream", str(self.project)],
            cwd=REPO or HERE.parent,
            env=env,
            stdout=(self.st / "stream.out").open("ab"),
            stderr=subprocess.STDOUT,
            preexec_fn=_prefer_cpu,
        )
        self.log(event="stream_launched", pid=self.stream_proc.pid)

    def stream_alive(self) -> bool:
        return not self.engine_failed() and (
            self.remote is not None or (self.stream_proc is not None and self.stream_proc.poll() is None)
        )

    # ---- 投入 ----
    def submit(self, c: str | None, text: str, *, end: bool) -> dict[str, object] | None:
        """cut の text を流す (`drafts/{id}/cuts/` — 投入検査を通れば run に流れる) → {"sealed": True} か {"rejected": 理由,
        "defects": [DEFECT の行]}。None = 流す先が死んだ。"""
        if os.environ.get("NOLANG_STUDIO_ENGINE") == "codex":
            # 著者が末尾まで成功したと確認してから end を送る。
            while end and not (self.st / "src.done").exists() and not self.engine_failed():
                time.sleep(0.1)
            if self.engine_failed():
                return None
        if not self.stream_alive():
            return None
        try:
            r = self.call("cut", {"text": text, "end": end})
        except Rejected as e:
            return {"rejected": str(e)[:400], "defects": e.defects}
        except RuntimeError as e:
            return {"rejected": str(e)[:400], "defects": []}
        return {"sealed": True, "lines": r.get("lines")}

    def feed_text(self, c: str) -> str | None:
        """cut c の投入の text (design の block + timeline の block)。根がまだ流れていなければ根を前に付ける (根の先行投入が弾かれた時)。"""
        blk = self.cut_block(c)
        if blk is None:
            return None
        text = blk[0].rstrip("\n") + "\n" + blk[1].rstrip("\n") + "\n"
        if not self.root_submitted:
            rd, rt = self.root()
            text = rd.rstrip("\n") + "\n" + "\n".join(l for l in rt.splitlines() if l.strip() != "#v2") + "\n" + text
        return text

    def submit_root(self) -> str:
        """根が閉じた時点で根だけを先に流す (run は cut を待たずに cast の素材の解決と cut の先行解決を始める)。根はここで凍る (cut 0
        の直し役は根を直さない)。投入検査で弾かれた根は最初の cut と一緒に流す。返り値 = 流した text ("" = 流さなかった)。"""
        while not ((self.solo / "root_design.txt").exists() and (self.solo / "root_timeline.txt").exists()):
            if (self.st / "src.done").exists():
                return ""
            time.sleep(0.3)
        time.sleep(0.2)  # 書きかけを読まない (著者は section が閉じてから置く)
        with self.name_lock:
            self.normalize_root()
            rd, rt = self.root()
        text = rd.rstrip("\n") + "\n" + "\n".join(l for l in rt.splitlines() if l.strip() != "#v2") + "\n"
        t = time.time()
        ack = self.submit(None, text, end=False)
        if ack is None or "rejected" in ack:
            self.log(event="root_submit_rejected", reason=str((ack or {}).get("rejected"))[:300])
            return ""
        self.root_submitted = True
        self.log(event="root_submitted", s=round(time.time() - t, 1))
        return text

    def feed(self) -> None:
        """staged の cut を構成の順に流す。根は閉じた時点で先に流す (以後凍結)。投入検査 (prefix との compile・出し済みの item が
        変わらない事・composer の乾いた実行・読めない素材) は投入そのもの — 弾かれたら、落とす前にその cut の直し役を 1 回だけ呼び
        (DEFECT の文と、流した前の cut の定義 `defs_before` を渡す)、直した text で流し直す (`fix` の `round: "intake"`)。この 1 回は stage
        の直し (2 回まで・`fix_calls`) とは別枠 — stage は staged で終わっていて、投入検査の DEFECT は stage の check に出なかった物 (前の
        cut の担当 / 直しが後から定義を変えた・流した prefix との食い違い) だから。それでも弾かれたら stage と同じ最後の手段
        (last_resort: 著者版 → DEFECT の印を落とす) を掛け、通らなければ落とす (`intake_rejected`)。最後の cut は end と一緒に。"""
        prefix = self.submit_root()  # 流した stream の text (根 + cut)
        for i, c in enumerate(self.order):
            while not self.staged.get(c):
                if not self.stream_alive():
                    self.log(event="stream_died", code=self.stream_proc.returncode if self.stream_proc else None)
                    return
                time.sleep(0.3)
            last = i == len(self.order) - 1
            text = None if self.broken.get(c) else self.feed_text(c)
            if text is None:
                self.log(cut=c, event="submit_skipped", broken=self.broken.get(c))
                continue
            t = time.time()
            ack = self.submit(c, text, end=last)
            if ack is None:
                self.log(cut=c, event="stream_died", code=self.stream_proc.returncode if self.stream_proc else None)
                return
            defects = [str(d) for d in ack.get("defects", [])] if "rejected" in ack else []
            if "rejected" in ack and defects and self.fix_effort is not None:
                ff = self.st / f"intake_{c}.txt"
                ff.write_text(
                    "投入検査 (流した前の cut + この cut) の DEFECT。前の cut はもう流れていて変えられない — 前の cut の定義の形"
                    " (参考の定義) に合わせてこの cut を直す:\n" + "\n".join(defects[:40])
                )
                try:
                    ok, tail = self.run_fixer(c, ff)
                except FixerUnavailable as error:
                    ok, tail = False, str(error)
                self.log(
                    cut=c,
                    event="fix" if ok else "fix_failed",
                    round="intake",
                    s=round(time.time() - t, 1),
                    defect=len(defects),
                    first=defects[0][:300],
                    **({} if ok else {"tail": tail}),
                )
                fixed = self.feed_text(c) if ok else None
                if fixed is not None:
                    text = fixed
                    ack = self.submit(c, text, end=last) or ack

            def accepted() -> bool:
                nonlocal ack, text
                text = self.feed_text(c) or text
                ack = self.submit(c, text, end=last) or ack
                return "rejected" not in ack

            if "rejected" in ack and defects:
                # 投入検査の defects (直し 1 回の後の最新) を直接渡す — check の defects.json に出ない規則 (editable は check で
                # warn) も救済路に乗る
                latest = [str(d) for d in ack.get("defects", [])] or defects
                self.last_resort(c, [x for x in self.order if x in self.submitted] + [c], "intake", accepted, latest)
            if "rejected" in ack:
                self.mark_broken(c, "rejected: " + str(ack["rejected"])[:160])
                self.log(cut=c, event="intake_rejected", s=round(time.time() - t, 1), reason=str(ack["rejected"])[:300])
                continue  # 根を運んでいたなら次の cut が運ぶ (root_submitted のまま False)
            self.root_submitted = True
            prefix += text
            self.submitted.add(c)
            self.log(cut=c, event="fed", s=round(time.time() - t, 1))
            if last:
                return
        if not self.root_submitted:
            # 1 cut も流せなかった — run を待たせない
            self.abort("no cut submitted")
            self.log(event="feed_aborted", reason="no cut submitted")
            return
        # 最後の cut が壊れて飛んだ時の閉じ (`#end` だけ)
        ack = self.submit(None, "", end=True)
        if ack is None or "rejected" in ack:
            self.log(event="end_rejected", ack=ack)
            self.abort("end rejected")

    def write_back(self) -> None:
        """流した最終の doc (根 + 流した cut・構成の順) を studio/ に書き戻す — studio/ に `new` の骨組みが残り、動画と doc が食い違って
        いた (nt01〜10 全部)。src.json は run が解いた素材の pin (local の run が stream/asset_pins.json に書く) を写した物。"""
        cuts = [c for c in self.order if c in self.submitted]
        design, timeline = self.doc_texts(cuts)
        pins_file = self.st / "asset_pins.json"
        src = self.doc_src(json.loads(pins_file.read_text()) if pins_file.exists() else None)
        (self.studio / "design.txt").write_text(design)
        (self.studio / "timeline.txt").write_text(timeline)
        (self.studio / "src.json").write_text(json.dumps(src, ensure_ascii=False, indent=1))
        self.log(event="written_back", cuts=cuts)

    def engine_failed(self) -> bool:
        return os.environ.get("NOLANG_STUDIO_ENGINE") == "codex" and (self.st / "engine.failed").exists()

    def abort_engine(self) -> int:
        self.log(event="engine_failed", reason=(self.st / "engine.failed").read_text()[:400])
        self.abort("Codex の生成に失敗")
        if self.stream_proc is not None:
            self.stream_proc.terminate()
        return 1

    def run(self) -> int:
        self.log(event="orchestrator_start")
        while not (self.solo / "order.txt").exists():
            if self.engine_failed():
                return self.abort_engine()
            # 根 call が死んだ (claude が無い等) → 待ち続けない。300 s の打ち切りは著者が生きている印 (思考か本文の最初の token) を
            # 出すまでだけ — 長い動画では著者の思考が 300 s を超え、生きている call を打ち切って動画ごと落とした (10-24 の 600 s 2 本)
            author_alive = (self.st / "author.jsonl").exists() and '"tag": "author"' in (
                self.st / "author.jsonl"
            ).read_text()
            if (time.time() - self.t0 > 300 and not author_alive) or (self.st / "src.done").exists():
                self.log(event="root_missing", waited_s=round(time.time() - self.t0, 1))
                return 1
            time.sleep(0.3)
        time.sleep(0.2)
        self.order = [l.strip() for l in (self.solo / "order.txt").read_text().splitlines() if l.strip()]
        self.log(event="plan_seen", cuts=self.order)
        if self.engine_failed():
            return self.abort_engine()
        self.fixed = frozenset(
            str(row["name"])
            for row in self.call("rules").get("rules", [])
            if isinstance(row, dict) and row.get("fixed")
        )
        self.start()
        if self.video_id is None:
            self.log(event="start_failed")
            return 1
        threads = [
            threading.Thread(target=self.guarded, args=(self.stage, i, c), daemon=True)
            for i, c in enumerate(self.order)
        ]
        threads.append(threading.Thread(target=self.feed, daemon=True))
        for t in threads:
            t.start()
        if os.environ.get("NOLANG_STUDIO_ENGINE") == "codex":
            while any(t.is_alive() for t in threads):
                if self.engine_failed():
                    return self.abort_engine()
                for t in threads:
                    t.join(timeout=0.1)
            if self.engine_failed():
                return self.abort_engine()
        else:
            for t in threads:
                t.join()
        return self.remote_wait() if self.remote is not None else self.local_wait()


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    project = Path(argv[0]).resolve()
    staff = argv[argv.index("--staff") + 1] if "--staff" in argv else None
    fix_arg = argv[argv.index("--fix") + 1] if "--fix" in argv else "severe"
    fix = {"none": None, "defect": "low", "severe": "low"}.get(fix_arg, fix_arg)
    review = argv[argv.index("--review") + 1] if "--review" in argv else "low"
    look = "--look" in argv
    remote = argv[argv.index("--remote") + 1] if "--remote" in argv else None
    token = argv[argv.index("--token") + 1] if "--token" in argv else os.environ.get("NOLANG_API_KEY")
    if token is None and remote is not None:
        token = claude_mcp_token(remote)
    if look and remote is not None:
        print("--look は local だけ (静止画はこの機械の GPU で描く)", file=sys.stderr)
        return 2
    run = Run(
        project,
        staff=staff,
        fix=fix,
        review=None if review == "none" else review,
        fix_scope=fix_arg if fix_arg in ("defect", "severe") else "warn",
        keep_assets="--staff-edits-assets" not in argv,
        look=look,
        remote=remote,
        token=token,
        editable="--editable" in argv,
    )
    if (
        "--fetch-ref" in argv
    ):  # 参照の動画の src を project/reference.json に (stream_make.sh が著者の起動前に 1 回呼ぶ)
        (project / "stream").mkdir(parents=True, exist_ok=True)
        return run.fetch_reference(argv[argv.index("--fetch-ref") + 1])
    if (
        "--fetch-speech" in argv
    ):  # 持ち込み音声の clip 台帳を project/speech.json に (stream_make.sh が著者の起動前に 1 回呼ぶ)
        (project / "stream").mkdir(parents=True, exist_ok=True)
        return run.fetch_speech(argv[argv.index("--fetch-speech") + 1])
    launch = project / "stream/author.jsonl"
    if launch.exists():
        for l in launch.read_text().splitlines():
            r = json.loads(l)
            if r.get("event") == "launch":
                run.t0 = float(r["t"])
    return run.run()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

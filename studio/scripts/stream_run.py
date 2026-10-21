"""stream の orchestrator — 著者 (stream_author.py・1 call) が落とす cut を出た順に check → 直し (低 effort の claude -p) → warm (絵・声) →
確定 → 投入。描画は製品の `DraftStreamRun` (`studio.py stream`・この機械の 1 process・studio_stream.py) が seal ごとに HLS を伸ばす
(cut 0 が seal された時点から再生できる)。cut の段は全 cut 同じで、orchestrator は cut の index で分岐しない。

cut ごとの段 (全部 thread・cut ごとに並列):
  受け (前の cut が使う定義はそちらへ移す) → 著者版 check → 担当 (Opus medium) → check + 直し (2 回まで・担当の直後と最初の DEFECT 0 の
  check で warm を起こす) → staged (ready) → 投入検査 (DEFECT は直し役を 1 回・別枠) → 投入 (構成の順・受理は watch_acks が記録する)。
根の規則: 名のある定義 (def・motion・run・svg・sound・cue) は初めて使う cut の block に書き、その cut だけが直す。根 (設定・cast・字幕と
BGM の開き・常設の層) の持ち主は最初の live な cut — その直し役だけが根を直し、根はその cut が受理された時に凍る。壊れた cut の定義は
次の live な cut の block へ移る。
cut を跨ぐ待ちは 投入の順・持ち主待ち (他の cut の行の DEFECT で check が止まった時だけ・相手は持ち主 1 つ)・根の先行解決・
機械全体の warm の枠 (期限順) だけ。

usage (repo root から): python stream_run.py <project> [--staff medium]
  --remote http://host:18000 [--token nlg-c-…] = 投入先を NoLang API (製品の draft stream・server が描く) にする。視聴 URL を `WATCH …`
    の 1 行で出す (token は --token か env NOLANG_API_KEY・無ければ Claude Code が `/mcp` の OAuth で得た token)。--template <video_id>
    = 素材台帳のテンプレ (`GET /v1/unstable/drafts/templates/` の 1 行・既定は server の空のテンプレ)。
  --staff = 担当 (Opus・判定役の 8 観点で cut を書き直す) を全 cut に、cut ごとに並列に (前の cut は著者の版を参考に渡す)。
  直し役に回す規則は台帳 (`studio_rules.fixed_rules`)。最後の cut 以外の doc は OPEN_ENDED (後に cut が続く prefix) で check する。
記録: project/stream/run.jsonl (event ごとの時刻・製品の segment の時刻も)・最終 project/studio/out/video.mp4。
"""

from __future__ import annotations

import contextlib
import fcntl
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
import urllib.request
from collections import defaultdict
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

from studio_rules import fixed_rules

HERE = Path(__file__).resolve().parent
# repo の中の skill なら自 repo (studio の check・名の改名・台帳)。plugin で入れた skill (repo 無し) は --remote だけが動き、
# check / 改名 / 台帳は NoLang API から受ける
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


_SE = re.compile(r'\[♪"([^"]+)"')  # 台詞の効果音の説明 (warm の鍵)
_MARK_NOT_SE = re.compile(
    r"\[(?!♪)[^\[\]]*\]"
)  # 台詞行の印 (効果音の `[♪…]` を除く) — 先行 warm が DEFECT の印を落とす
# cut の block に書ける名のある定義 (grammar の CUT_DEFINITION_ROOTS) — 持ち主はその block の cut。字下げの子の行も定義の一部
_NAMED_DEF = re.compile(r"^(def|svg|sound|motion|run|cue)\s+([A-Za-z_][\w-]*)\b")
ROOT = ""  # 行の無い DEFECT の持ち主が根 (Run.unlocated_owner の値)
_DEF_CHILD = re.compile(r"^[ \t]+[A-Za-z_][\w-]*#([A-Za-z_][\w-]*)", re.M)  # 定義の字下げの子の行 `  icon#i(…` → 子の名


def def_children(text: str) -> set[str]:
    """名のある定義 (見出しの行 + 字下げの子) の子の名 — 後の cut は実体の子を `実体.子` で参照する。"""
    return set(_DEF_CHILD.findall(text))


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
    """cut 1 つの warm の状態 (直しと並ぶ prewarm と staged 後の warm で 1 つ)。"""

    thread: threading.Thread | None = None  # 走っている / 走った prewarm
    key: tuple[object, ...] | None = (
        None  # prewarm が組んだ doc の素材の鍵 (asset_key)・同じなら staged 後の warm は要らない
    )
    ok: bool = False  # prewarm が行を落とさずに通った
    done: bool = False  # 段としての warm が終わった (feed が待つ旗)


# 機械全体で同時に走らせる warm の数 (run を跨ぐ・期限の近い cut から)。4 core の機械で 3 本並列の run が check の直後に 4 本ずつ warm を
# 起こすと 12 本が重なり、1 本 13 s の warm が 40〜64 s に伸びた (cur12・svg の描画と主体計測が CPU 待ち)
WARM_MACHINE_SLOTS = min(4, os.cpu_count() or 4)


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
        remote: str | None = None,
        token: str | None = None,
        template: str | None = None,
    ) -> None:
        self.project = project
        # remote = NoLang API (nolang-api consumer) の base URL。著者・担当・直しはこの機械の claude -p のまま、確定した cut の stream の
        # text を `unstable/drafts/{id}/cuts/` へ投入し、素材・描画・配信は server (製品の draft stream) に任せる。None = この機械の
        # `studio.py stream` (同じ製品の DraftStreamRun) に流す。どちらも根は最初に受理される cut と一緒に流れ、以後凍る
        self.remote = remote.rstrip("/") if remote else None
        self.token = token
        self.remote_template = template  # 素材台帳のテンプレ (drafts/templates/ の 1 行)。None = server の空のテンプレ
        self.remote_video_id: str | None = None
        self.remote_watch_url = ""  # 視聴 URL (`WATCH` / `PLAYABLE` の行に出す)
        self.root_submitted = False
        self.fixed = fixed_rules()  # 直し役に回す規則 = 台帳の直しの列
        self.staff_effort = staff  # 担当 (8 観点で cut を書き直す) の effort。None = 担当なし
        self.solo, self.st, self.studio = project / "solo", project / "stream", project / "studio"
        self.weave = project / "weave"
        self.weave.mkdir(parents=True, exist_ok=True)
        self.env = dict(
            os.environ,
            **({"PYTHONPATH": str(REPO), "STUDIO_SERVER_SOCK": str(REPO / "tmp/studio/.server/sock")} if REPO else {}),
            # run で 1 つの素材の置き場 — prefetch・warm・stream の render が同じ dir を使い、落とした絵と音を引き直さない
            STUDIO_PROCESS_ID=f"studio-{uuid5(NAMESPACE_URL, str(project.resolve())).hex[:12]}",
        )
        self.pin_lock = threading.Lock()
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
        # 根だけの先行解決 (root_prefetch) の合図: 話者・書体 (cut の warm が要る・1〜5 s) → 残り全部 (基準画像・BGM の聴取・
        # `[ref:` を使う cut の warm と最初の投入が待つ = root_done)
        self.root_fast_done = threading.Event()
        self.root_done = threading.Event()
        self.broken: dict[str, str] = {}
        self.feed_n = 0  # 流した feed の file の数 (= 次の番号)
        self.pending_acks: dict[int, str | None] = {}  # 流して受理 / 拒否が未だの feed 番号 → cut
        self.stream_proc: subprocess.Popen[bytes] | None = None
        self.t0 = time.time()
        self.order: list[str] = []

    # ---- 記録 ----
    def log(self, **kw: object) -> None:
        kw["t"] = time.time()
        kw["since"] = round(float(kw["t"]) - self.t0, 1)
        with (self.st / "run.jsonl").open("a") as f:
            f.write(json.dumps(kw, ensure_ascii=False) + "\n")
        print(json.dumps(kw, ensure_ascii=False), flush=True)

    def studio_cmd(self, *args: str, timeout: int = 1800) -> str:
        r = subprocess.run(
            [PY, str(STUDIO), *args],
            cwd=REPO or HERE.parent,
            env=self.env,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return r.stdout + r.stderr

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
    def merged_pins(self, cuts: list[str]) -> dict:
        with self.pin_lock:
            base = self.studio / "src.json"
            d = json.loads(base.read_text()) if base.exists() else {"asset_pins": {}}
            pins = d.setdefault("asset_pins", {})
            # 根だけの先行解決 (root_prefetch) の pin と、cut の check / warm の doc の pin — 全部の doc が写す (書く側は置き換えで
            # 書くので書きかけは読まない)
            paths = [self.weave / "_root/src.json"]
            for c in cuts:
                paths += [self.weave / c / "src.json", self.weave / f"{c}.img/src.json"]
            for path in paths:
                if path.exists():
                    for k, v in json.loads(path.read_text()).get("asset_pins", {}).items():
                        pins.setdefault(k, v)
            return d

    def live_cuts(self, cuts: list[str]) -> list[str]:
        """壊れた cut (直しで通らなかった物) は後の doc から外す — 1 cut 欠けても残りは描ける方を取る。"""
        return [c for c in cuts if not self.broken.get(c) or c == cuts[-1]]

    def cut_line_ranges(self, cuts: list[str]) -> dict[str, tuple[tuple[int, int], tuple[int, int]]]:
        """doc (根 + cuts) の中で cut ごとの design / timeline の行の範囲 [a, b] (1 始まり)。"""
        rd, rt = self.root()
        d_at, t_at = rd.count("\n"), rt.count("\n")
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
        """cut の text の中の層の名を改名する (参照も文法どおりに)。remote は server の文法 (`drafts/rename/`)・local は自 repo。"""
        if self.remote is not None:
            return str(self.remote_post("/v1/unstable/drafts/rename/", {"text": txt, "renames": renames})["text"])
        from domain.entities.video_draft import LayerPath  # noqa: PLC0415 — repo のある時だけ
        from domain_services.video_draft.grammar.rename import rename_name  # noqa: PLC0415

        for old, new in renames.items():
            txt = rename_name(txt, LayerPath.parse(old), LayerPath.parse(new))
        return txt

    @property
    def language(self) -> str:
        try:
            value = json.loads((self.studio / "src.json").read_text()).get("settings", {}).get("language")
        except (OSError, ValueError):
            return "ja"
        return str(value or "ja")

    def plan_seconds(self) -> dict[str, float]:
        """plan の cut ごとの見込み秒 (期限の材料)。無ければ空。"""
        from stream_author import plan_names  # noqa: PLC0415 — scripts dir を sys.path に足している

        plan = self.solo / "plan.txt"
        return dict(plan_names(plan.read_text())) if plan.exists() else {}

    def deadline(self, c: str) -> float:
        """cut c の期限 = run の起点 + plan で c より前の cut の見込み秒の和 (見る人がその cut に着く時刻の見込み)。plan が無ければ
        cut 1 つ 10 s と見る。"""
        secs = self.plan_seconds()
        before = self.order[: self.order.index(c)] if c in self.order else []
        return self.t0 + sum(secs.get(x, 10.0) for x in before)

    def planned_total_ms(self) -> int | None:
        """plan の見込み秒の合計 (ms)。`until: end` の進行線の全長に使う — stream では動画の全長が最後の cut まで決まらないので、
        どの prefix の doc でも同じ値で伸ばす (最終の尺とは plan の誤差の分だけ違う)。"""
        total = sum(self.plan_seconds().values())
        return int(total * 1000) if total > 0 else None

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

    def doc_dir(self, name: str, cuts: list[str], *, warm_cut: str | None = None, root_extra: str = "") -> Path:
        """doc (根 + cuts) を weave/<name>/ に組む。warm_cut = cut ごとの warm の doc: 素材を作るのは cuts の最後の cut だけ (前の
        cut の絵と声はその cut の warm が作る — `WARM_CUT`・studio_draft._warm_prefix)。"""
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
        if warm_cut is not None:
            (dd / "WARM_CUT").write_text(warm_cut)
        else:
            (dd / "WARM_CUT").unlink(missing_ok=True)
        # 同じ cut の doc を複数の thread が組み直す事があるので、読み手が書きかけを見ないよう置き換えで書く
        tmp = dd / f".src.json.{threading.get_ident()}"
        tmp.write_text(json.dumps(self.merged_pins(cuts), ensure_ascii=False, indent=1))
        os.replace(tmp, dd / "src.json")
        merged: dict = {}
        for o in [self.studio / "out", *(self.weave / f"{c}.img/out" for c in cuts), dd / "out"]:
            if (o / "tts_durations.json").exists():
                try:
                    merged.update(json.loads((o / "tts_durations.json").read_text()))
                except Exception:
                    pass
        (dd / "out/tts_durations.json").write_text(json.dumps(merged, ensure_ascii=False))
        # 書体の実体 (TTF) は project で 1 つの cache (studio/out/fonts) を全部の doc が symlink で共有する — check は out/fonts の
        # TTF で文字を測る (無い書体は既定 font で測り、送り幅の違う実書体で render が割れる)
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
        """ended = 動画の終わりまで書いた doc (False = この prefix の後に cut が続く — 最後の cut だけの規則を掛けない)。
        remote は server の compile の check (`drafts/check/`・DEFECT と compile の注意だけ — layout / render の段の lint は製品の
        stream が描く時に記録する)。local は studio の check (compile + layout + lint)。欠陥はどちらも `Defect.as_record()` の形
        (local は doc の out/defects.json — DEFECT の無い check はその file を消す)。"""
        if self.remote is not None:
            body = self.remote_post(
                "/v1/unstable/drafts/check/",
                {
                    "design": (dd / "design.txt").read_text(),
                    "timeline": (dd / "timeline.txt").read_text(),
                    "open_ended": not ended,
                },
            )
            defects = [Defect.read(d) for d in body.get("defects", []) if isinstance(d, dict)]
            lint = [f for f in body.get("findings", []) if isinstance(f, dict)]
            (dd / "out").mkdir(exist_ok=True)
            (dd / "out/lint_check.json").write_text(json.dumps(lint, ensure_ascii=False))
            return "\n".join(d.text for d in defects), defects, lint
        # 前の check の結果を読まない — DEFECT で止まった check は lint を書かない (前の round の lint が残ると、直し役に無い指摘を
        # 渡す)・途中で死んだ check は defects.json を書き換えない
        for name in ("lint_check.json", "defects.json"):
            (dd / "out" / name).unlink(missing_ok=True)
        out = self.studio_cmd(
            "check", str(dd), "--no-warm", "--no-def-probe"
        )  # ended は doc の OPEN_ENDED marker が運ぶ
        defects = [d for d in self.read_defects(dd) if d.level == "DEFECT"]
        lint = []
        p = dd / "out/lint_check.json"
        if p.exists():
            try:
                lint = json.loads(p.read_text())
            except Exception:
                lint = []
        return out, defects, lint

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

    def attribute_unlocated(
        self, c: str, cuts: list[str], unlocated: list[Defect]
    ) -> tuple[list[Defect], list[Defect]]:
        """行の無い DEFECT の持ち主: c を除いた doc (根 + その doc の前の cut) でも出るなら c の物ではない (前の cut か根の物)。
        c が最初の live な cut なら、除いた doc は根だけ — 出れば根の物 (c の DEFECT として返し、持ち主を ROOT で覚える)。
        全 cut 同じ規則で、cut の index では分けない。
        確かめないと、前の cut の空の text 1 つが後の cut 全部の check に出て、どの cut の直しでも消えずに全部が壊れる (s8 の 16)。
        持ち主は sig で覚える (unlocated_owner) — 後の cut の check で同じ DEFECT が出たら、その cut を除いて lint を取れる (stage)。"""
        prev = [x for x in cuts if x != c and not self.broken.get(x) and self.cut_block(x)]
        base = self.doc_dir(f"{c}.base", prev)
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
        self, c: str, cuts: list[str], rnd: int | str, *, name: str | None = None
    ) -> tuple[Path, str, list[Defect], list[dict], set[str]]:
        """doc (根 + cuts・c を含む) を check し、cut c (か根) の DEFECT と c の lint を返す → (doc, 出力, DEFECT, lint, blockers)。
        blockers = check を止めた前の cut の DEFECT の持ち主 (行の無い DEFECT で持ち主が分からなければ "?")。blockers があればその
        doc の lint は c の物も含めて出ていない。name = doc の dir の名 (既定は c)。"""
        dd = self.doc_dir(name or c, cuts)
        out, all_defects, lint = self.check(dd, ended=cuts[-1] == self.order[-1])
        ranges = self.cut_line_ranges(cuts)
        rd, rt = self.root()
        root_n = (rd.count("\n"), rt.count("\n"))
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
            mine_u, foreign = self.attribute_unlocated(c, cuts, unlocated)
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

    def owns_root(self, c: str) -> bool:
        """cut c が根の持ち主か = 動画の最初の live な cut で、根がまだ流れていない (根は最初に受理される cut と一緒に流れて凍る)。"""
        return c == self.first_live() and not self.root_submitted

    def run_fixer(self, c: str, ff: Path) -> tuple[bool, str]:
        """直し役 (claude -p・低 effort) を 1 回。通れば cut の file を書き戻す → (通ったか, 出力の末尾)。根の持ち主の cut なら根の 2 file も
        直せる (`--root`)。担当・直し役の参考に前の cut の定義を渡す。"""
        self.write_defs_before(c)
        src = self.solo / f"cut_{c}.txt"
        before = src.read_text()
        for attempt in (0, 1):
            r = subprocess.run(
                [PY, str(AUTHOR), "fix", str(self.project), c, str(ff), *(["--root"] if self.owns_root(c) else [])],
                cwd=REPO or HERE.parent,
                env=self.env,
                capture_output=True,
                text=True,
                timeout=600,
            )
            if r.returncode != 0 and "FileNotFoundError" in r.stderr and attempt == 0:
                time.sleep(2)  # claude の shim が一瞬見つからない事がある → 1 回だけやり直す
                continue
            break
        if r.returncode == 0 and "---timeline---" in r.stdout:
            # 担当の書き戻しと同じ門: 基準は書き戻す直前の file (直し役が走る間に後の cut の thread が c の block へ移した定義
            # — move_forward_defs — も含む)。直し役が消した定義・後の cut が使う定義の形を変えた物を戻す
            with self.name_lock:
                latest = src.read_text()
                src.write_text(r.stdout)
            self.restore_defs(c, latest if "---timeline---" in latest else before, who="fixer")
            return True, r.stdout
        return False, (r.stdout + r.stderr)[-200:]

    def stage(self, i: int, c: str) -> None:
        """cut c が出たら doc (根 + live な cut 0..i) を組んで check → 直し (2 回まで) → staged (ready)。段の thread が死んでも旗は
        立てる (立たないと後の cut が全部待ち続ける — 死んだ cut は guarded が壊れ扱いにする)。"""
        try:
            self._stage(i, c)
        finally:
            self.staged[c] = True
            self.log(cut=c, event="staged", broken=self.broken.get(c))

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
        before_fix: str | None = None  # 直し役を掛ける直前の cut の text (直し役が作った DEFECT の行を戻す元)
        settled = False  # 直し役の壊した行を戻した — DEFECT が消えれば残りの指摘で直し役をもう呼ばない
        prev_findings: str | None = None
        for rnd in itertools.count():
            t = time.time()
            cuts = self.live_cuts(self.order[: i + 1])
            dd, out, defects, lint, blockers = self.check_cut(c, cuts, rnd)
            if blockers and not defects:
                # 前の cut (か根) の DEFECT で check が止まると、この cut の lint は 1 件も出ない (dt_18: phone の `none` の色で後の
                # 4 cut が lint なしのまま staged になり、画面外・重なりが直し役に届かなかった)。持ち主の分かる cut はその cut を除いた
                # doc で c の lint を取る (前の cut の直しと c の直しが並列に進む)。持ち主の分からない DEFECT (根・まだ check して
                # いない cut) か、除くと c に DEFECT が出る (除いた cut の sticky を指す) 時だけ、持ち主が ready になるまで待って掛け直す
                skip = frozenset(blockers - {"?", ROOT})
                if skip and not (blockers & {"?", ROOT}):
                    skipped = self.check_cut(c, [x for x in cuts if x not in skip], rnd)
                    if not skipped[2] and not skipped[4]:
                        self.log(cut=c, event="lint_skip", round=rnd, skip=sorted(skip))
                        dd, out, defects, lint, blockers = skipped
                if blockers:
                    self.log(cut=c, event="lint_blocked", round=rnd, owners=sorted(blockers))
                    self.wait_owners(c, blockers)
                    dd, out, defects, lint, _ = self.check_cut(c, self.live_cuts(self.order[: i + 1]), rnd)
            mine = [f for f in lint if f.get("cut") == c]
            fixes = [f for f in mine if self.to_fix(f)]
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
            if not defects and not self.broken.get(c):
                # lint の直しが残っていても素材は作り始める (直し役は台詞も絵の説明文も変えない約束)
                self.start_prewarm(c)
            if defects and before_fix is not None:
                reverted = self.revert_fixer_damage(c, cuts, before_fix, defects)
                before_fix = None
                if reverted:
                    self.log(cut=c, event="fix_reverted", round=rnd, n=reverted, defect=len(defects))
                    settled = True
                    continue
            need = bool(defects) or (bool(fixes) and not settled)
            if not need:
                break
            if fix_calls >= 2:
                # 捨てるのは描けない cut (DEFECT・文法と実行) だけ — 2 回直しても残る severe (配置の重なり・はみ出し …) は受け入れて
                # 描く (判断 16・描画は best effort で続く: 字の床まで縮める・そのまま描く — layout/report.py)。落とすと cut が
                # 台詞ごと動画から消える
                if defects:
                    self.mark_broken(c, "DEFECT after 2 fixes")
                break
            findings = "\n".join(d.text for d in defects[:40])
            rest = [
                f for f in mine if f.get("severity") in ("severe", "warn") and f not in fixes
            ]  # 直し役にはその cut の severe / warn も全部見せる
            for f in (fixes + rest)[:24]:
                findings += f"\n{f.get('severity')} {f.get('rule')} ({f.get('layer', '')}): {f.get('message', '')} — {f.get('hint', '')}"
            if findings == prev_findings and not defects:
                # 直しても指摘が 1 つも変わらない — もう 1 回頼んでも同じ答え (直し役が触れない層・直し方の無い指摘)。打ち切る。
                # DEFECT が残る時は打ち切らない: 2 回目 (か著者版への差し替え) で通る事があり、落とすと cut が台詞ごと消える
                # (cur7_03 climax: `~` の順の DEFECT を 1 回で打ち切って落とした)
                self.log(cut=c, event="fix_stalled", round=rnd, fix=len(fixes))
                break
            prev_findings = findings
            ff = dd / f"out/findings_{rnd}.txt"
            ff.write_text(findings)
            t = time.time()
            if fix_calls and defects and c in self.author_clean:
                # 直しても DEFECT が残る — 担当が触る前の著者の版 (check で DEFECT 0) に差し替えて掛け直す (2 回目の直しの
                # 代わり・通らなければ今どおり落とす)。落ちた cut は台詞ごと消えるので、文字や効果音の少ない著者の版を取る
                author = (self.solo / f"author_cut_{c}.txt").read_text()
                if author != (self.solo / f"cut_{c}.txt").read_text():
                    (self.solo / f"cut_{c}.txt").write_text(author)
                    fix_calls += 1
                    self.log(cut=c, event="revert_author", round=rnd, defect=len(defects))
                    continue
            before_fix = (self.solo / f"cut_{c}.txt").read_text()
            ok, tail = self.run_fixer(c, ff)
            if ok:
                fix_calls += 1
                self.log(cut=c, event="fix", round=rnd, s=round(time.time() - t, 1), chars=len(tail))
            else:
                self.log(cut=c, event="fix_failed", round=rnd, s=round(time.time() - t, 1), tail=tail)
                if defects:
                    self.mark_broken(c, "fix call failed")
                break

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

    def staff(self, i: int, c: str) -> None:
        """担当 (Opus・8 観点) が著者の cut を見直して書き直す。前の cut は著者の版を渡すので cut ごとに並列に走る。
        著者の版は solo/author_cut_<名>.txt に残す (次の cut の参考・差分の検証)。担当が台詞の文字を変えていたら著者の版の文字に
        戻す (`restore_speech`・読点の追加と読みの指定は許す — 声は担当の版から作るので後段では戻せない・`speech_restored`)。"""
        from stream_author import restore_speech  # noqa: PLC0415 — scripts dir を sys.path に足している

        src = self.solo / f"cut_{c}.txt"
        keep = self.solo / f"author_cut_{c}.txt"
        if not keep.exists():
            keep.write_text(src.read_text())
        # 著者版の check は担当の前に回し、指摘を担当に渡す (check の 1.6 s を浮かせる並走は担当後の DEFECT を増やした)
        ff = self.author_check(i, c)
        self.write_defs_before(c)
        before = src.read_text()  # 担当の前の block (著者の版 + 前方から移した定義) — 担当が消した定義を戻す基準
        t = time.time()
        r = subprocess.run(
            [PY, str(AUTHOR), "staff", str(self.project), c, str(ff), "--effort", self.staff_effort or "medium"],
            cwd=REPO or HERE.parent,
            env=self.env,
            capture_output=True,
            text=True,
            timeout=900,
        )
        if r.returncode == 0 and "---timeline---" in r.stdout:
            # 戻す基準は書き戻す直前の file — 担当の裏で前方から移された定義 (move_forward_defs) も含める (担当開始時の text だと
            # その定義が担当の出力に無いまま上書きされて消える)
            text, restored = restore_speech(keep.read_text(), r.stdout)
            with self.name_lock:
                latest = src.read_text()
                src.write_text(text)
            self.log(cut=c, event="staff", s=round(time.time() - t, 1), chars=len(r.stdout))
            if restored:
                self.log(cut=c, event="speech_restored", n=len(restored), lines=restored)
            self.restore_defs(c, latest if "---timeline---" in latest else before, who="staff")
        else:
            self.log(cut=c, event="staff_failed", s=round(time.time() - t, 1), tail=(r.stdout + r.stderr)[-200:])

    def restore_defs(self, c: str, before: str, *, who: str) -> None:
        """担当か直し役 (who) が書き戻した cut c の block の名のある定義 (def・motion・run・svg・sound・cue) を、書き戻す前の text
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
        同じ名・同じ形のまま中身 (見た目) を変えた定義は触らない。戻した時は `defs_restored` に `who` を記録する。"""
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
            if (self.def_signature(cur) != self.def_signature(text) or gone) and self.used_later(c, name):
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
        """cut c の warm を staged を待たずに起こす (直しと並ぶ): 担当の直後と、check で DEFECT 0 を見た時点 (直後の warm が DEFECT で
        落ちていれば起こし直す)。走っている / 通った prewarm があれば起こし直さない。remote (素材は server が解く) は起こさない。"""
        w = self.warms[c]
        if self.remote is not None or (w.thread is not None and (w.thread.is_alive() or w.ok)):
            return
        w.thread = threading.Thread(target=self.image_prewarm, args=(c,), daemon=True)
        w.thread.start()

    @contextlib.contextmanager
    def machine_warm_slot(self, c: str) -> Iterator[None]:
        """機械全体の warm の枠 (flock の file・`tmp/studio/.warm_slots/<k>`)。空いた枠は期限 (見る人がその cut に着く時刻の見込み) の
        近い待ち手から取る — 待ち手は期限を名にした札を置き、自分より期限の近い札の数が空いた枠の数より少ない時だけ枠を取りに行く。"""
        d = (REPO or HERE.parent) / "tmp/studio/.warm_slots"
        (d / "queue").mkdir(parents=True, exist_ok=True)
        ticket = d / "queue" / f"{int(self.deadline(c) * 1000):016d}_{os.getpid()}_{c}"
        ticket.touch()
        handles = [(d / str(k)).open("a") for k in range(WARM_MACHINE_SLOTS)]
        held = None
        try:
            while held is None:
                free = []
                for h in handles:
                    try:
                        fcntl.flock(h, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    except OSError:
                        continue
                    free.append(h)
                if free:
                    ahead = sum(1 for p in sorted((d / "queue").iterdir()) if p.name < ticket.name and p.exists())
                    if ahead < len(free):
                        held = free[0]
                        free = free[1:]
                for h in free:  # 取らない枠は戻す (期限の近い待ち手に)
                    fcntl.flock(h, fcntl.LOCK_UN)
                if held is None:
                    time.sleep(0.3)
            ticket.unlink(missing_ok=True)
            yield
        finally:
            ticket.unlink(missing_ok=True)
            if held is not None:
                fcntl.flock(held, fcntl.LOCK_UN)
            for h in handles:
                h.close()

    def warm_doc(self, c: str) -> Path:
        """cut c の warm の doc = 根 + ready (staged) で live な前の cut + c (check と同じ組み合わせ — cut を跨ぐ状態 (開いた字幕・sticky)
        を含む) で、素材を作るのは c の分だけ (`WARM_CUT`)。まだ ready でない前の cut は入れない — その cut の直し中の DEFECT で c の
        warm の doc が build できず、c の絵と声を製品が作る事になる (o3_05: 3 cut)。前の cut の絵と声はその cut の warm が作り、pin は
        merged_pins が写す。"""
        i = self.order.index(c)
        earlier = [x for x in self.order[:i] if not self.broken.get(x) and self.cut_block(x)]
        ready = [x for x in earlier if self.staged.get(x)]
        # ready でない前の cut は block ごとは入れない (直し中の DEFECT で doc が build できない) が、その block の定義 (def・motion …) は
        # c が使うので根の後ろに写す (定義は根にも書ける)
        pending_defs = "".join(
            text
            for x in earlier
            if not self.staged.get(x)
            for _kind, _name, text in self.named_defs(self.cut_block(x)[0])
        )
        return self.doc_dir(f"{c}.img", [*ready, c], warm_cut=c, root_extra=pending_defs)

    def image_prewarm(self, c: str) -> None:
        """cut c の warm の doc で `warm` (絵の生成と TTS 込み・c の分だけ)。根の素材 (書体・話者・BGM・基準画像) は root_prefetch の
        pin を写すので作らない (root_done を待つ)。担当の直後に起こすので c の block に DEFECT が残っている事がある — その行 (と字下げの
        子) を doc から落として残りの絵と声を先に作る (2 回まで)。落とした時は `ok` を立てず、staged 後の warm が差分 (直した行の
        絵と声) だけ作る (済んだ物は台帳の hit)。素材の鍵は doc を組む時の text から取る (thread を起こした時の text だと、直し役の
        書き戻しが間に入って鍵と doc が食い違う)。"""
        w = self.warms[c]
        self.wait_root_for((self.solo / f"cut_{c}.txt").read_text())
        with self.machine_warm_slot(c):
            w.key = self.asset_key((self.solo / f"cut_{c}.txt").read_text())
            dd = self.warm_doc(c)
            t = time.time()
            dropped = 0
            out = ""
            for _attempt in range(4):
                try:
                    out = self.studio_cmd("warm", str(dd), timeout=150)
                except subprocess.TimeoutExpired:
                    out = "TIMEOUT"
                if "OK warm" in out:
                    break
                n = self.drop_defect_lines(dd, c)
                if (
                    n == 0
                ):  # c の行でない DEFECT (根・前の cut) か DEFECT 以外の失敗 — check が DEFECT 0 を見た時に起こし直す
                    break
                dropped += n
            (dd / "out/warm.txt").write_text(out)
            w.ok = "OK warm" in out and dropped == 0
            self.log(cut=c, event="image_prewarm", s=round(time.time() - t, 1), ok="OK warm" in out, dropped=dropped)

    @staticmethod
    def drop_defect_lines(dd: Path, c: str) -> int:
        """warm の doc (dd) の out/defects.json のうち cut c の block の行を指す DEFECT を doc から外す → 直した行の数。design の行は
        その行と字下げの子を消す。timeline の台詞行は消さずに印 (`[…]`・効果音の `[♪…]` は残す) だけ落とす — 消した層を指す印の DEFECT で
        台詞 (TTS の元) まで消えて「台詞行が無い」に連鎖した (o6_03)。block の範囲は doc の text から引く (`section#c` / `*** c` から次の
        cut の頭まで)。"""
        defects = Run.read_defects(dd)
        if not defects:
            return 0
        heads = {
            "design": re.compile(rf"^section#{re.escape(c)}\b"),
            "timeline": re.compile(rf"^\*\*\* {re.escape(c)}\s*$"),
        }
        nexts = {"design": re.compile(r"^section#"), "timeline": re.compile(r"^\*\*\* ")}
        total = 0
        for which in ("design", "timeline"):
            path = dd / f"{which}.txt"
            lines = path.read_text().split("\n")
            start = next((k for k, line in enumerate(lines, start=1) if heads[which].match(line)), None)
            if start is None:
                continue
            end = next(
                (k for k, line in enumerate(lines[start:], start=start + 1) if nexts[which].match(line)), len(lines) + 1
            )
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

    def author_check(self, i: int, c: str) -> Path:
        """著者の版 (担当が触る前) を check し、DEFECT 0 なら author_clean に (revert_author の元)。指摘の file を返す (担当へ)。"""
        t = time.time()
        cuts = self.live_cuts(self.order[: i + 1])
        dd, _out, defects, lint, blockers = self.check_cut(c, cuts, "author")
        clean = not defects and not blockers  # 止まった check では c の実行の DEFECT が見えない
        if blockers - {"?", ROOT}:
            # 前の cut (著者の版) の DEFECT で check が止まり lint が出ない — その cut を除いた doc で c の lint を取る
            skip = blockers - {"?", ROOT}
            dd, _out, skipped, lint, rest = self.check_cut(c, [x for x in cuts if x not in skip], "author")
            clean = not defects and not skipped and not rest
        if clean:
            self.author_clean.add(c)
        mine = [f for f in lint if f.get("cut") == c]
        findings = "\n".join(d.text for d in defects[:20]) + "".join(
            f"\n{f.get('severity')} {f.get('rule')} ({f.get('layer', '')}): {f.get('message', '')} — {f.get('hint', '')}"
            for f in mine[:30]
        )
        ff = dd / "out/findings_author.txt"
        ff.write_text(findings)
        self.log(cut=c, event="check", round="author", s=round(time.time() - t, 1), defect=len(defects), warn=len(mine))
        return ff

    def root_prefetch(self) -> None:
        """根が閉じた時点 (著者が cut 0 を書く前) で根だけの素材を先に解決する: 書体の TTF・基準画像 (`image 名 =`) の生成・話者と
        立ち絵・BGM の聴取 (`studio prefetch` → `root_asset_refs`)。基準画像を派生 (`[ref:@名]`) の前に作っておくので、cut の
        派生の絵は基準を待たない。pin は `weave/_root/src.json` に入り、merged_pins が全部の doc へ写す。"""
        try:
            while not ((self.solo / "root_design.txt").exists() and (self.solo / "root_timeline.txt").exists()):
                if (self.st / "src.done").exists():
                    return
                time.sleep(0.3)
            time.sleep(0.2)  # 書きかけを読まない (著者は section が閉じてから置く)
            dd = self.doc_dir("_root", [])
            # 2 段を 1 process で: 話者・書体 (1〜5 s・cut の warm が待つ) → 残り全部 (基準画像 10 s と BGM の聴取 7〜9 s を並べて・
            # `[ref:` を使う cut の warm と最初の投入が待つ)。1 段目の終わりは `out/prefetch_fast.done` で知る
            fast_done = dd / "out/prefetch_fast.done"
            fast_done.unlink(missing_ok=True)
            t = time.time()
            proc = subprocess.Popen(
                [PY, str(STUDIO), "prefetch", str(dd)],
                cwd=REPO or HERE.parent,
                env=self.env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            while proc.poll() is None:
                if not self.root_fast_done.is_set() and fast_done.exists():
                    self.root_fast_done.set()
                    self.log(event="root_prefetch", phase="fast", s=round(time.time() - t, 1), ok=True)
                if time.time() - t > 300:
                    proc.kill()
                    break
                time.sleep(0.2)
            out = (proc.stdout.read() if proc.stdout else "") or ""
            (dd / "out/prefetch.txt").write_text(out)
            lines = out.strip().splitlines()
            self.log(
                event="root_prefetch",
                phase="all",
                s=round(time.time() - t, 1),
                ok=bool(lines) and lines[-1].startswith("OK prefetch"),
                tail="" if lines and lines[-1].startswith("OK prefetch") else out[-160:],
            )
        finally:
            self.root_fast_done.set()
            self.root_done.set()

    def wait_root_for(self, text: str) -> None:
        """cut の warm の前に待つ根の先読み: 話者・書体は常に、残り (基準画像) は cut が `[ref:` で使う時だけ。"""
        self.root_fast_done.wait(timeout=90)
        if "[ref:" in text:
            self.root_done.wait(timeout=90)

    def warm(self, i: int, c: str) -> None:  # noqa: ARG002 — 段の thread は (i, c) で呼ばれる
        """cut c の素材 (絵・効果音・書体の pin と TTS) を warm の doc (`<c>.img`・根 + live な cut 0..c・作るのは c の分) で作る。prewarm
        (直しと並行) が同じ doc で作り始めていれば、素材を決める物 (絵の説明文・台詞・効果音) が変わっていない限りその結果を使う。"""
        while not self.staged.get(c):
            time.sleep(0.3)
        w = self.warms[c]
        try:
            if self.broken.get(c):  # 直しで通らなかった cut は流れない — 素材を作らない
                return
            t = time.time()
            key = self.asset_key((self.solo / f"cut_{c}.txt").read_text())
            if w.thread is not None:
                w.thread.join()
                if w.ok and w.key == key:
                    self.log(cut=c, event="warm", s=round(time.time() - t, 1), ok=True, reused="prewarm")
                    return
            with self.machine_warm_slot(c):
                dd = self.warm_doc(c)
                out = ""
                for attempt in (
                    0,
                    1,
                ):  # TTS の応答待ちで止まる事がある → 150 s で切って 1 回やり直す (済んだ scene は cache)
                    try:
                        out = self.studio_cmd("warm", str(dd), timeout=150)
                    except subprocess.TimeoutExpired:
                        out = "TIMEOUT"
                        self.log(cut=c, event="warm_timeout", attempt=attempt)
                        continue
                    break
                (dd / "out/warm.txt").write_text(out)
                # warm が落ちても壊れ扱いにしない — 製品の organizer が足りない素材を自分で作る
                self.log(cut=c, event="warm", s=round(time.time() - t, 1), ok="OK warm" in out)
        finally:
            w.done = True

    def guarded(self, fn, i: int, c: str) -> None:
        """段の thread が例外で死んだ cut は壊れ扱い (旗は段 (stage / warm) が finally で立てる)。"""
        try:
            fn(i, c)
        except Exception as exc:  # noqa: BLE001 — 1 cut の失敗で動画全体を止めない
            self.broken[c] = f"{fn.__name__} crashed: {exc!r}"[:200]
            self.log(cut=c, event="stage_crashed", stage=fn.__name__, error=repr(exc)[:300])

    # ---- remote (NoLang API) ----
    def remote_post(self, path: str, body: dict[str, object]) -> dict[str, object]:
        req = urllib.request.Request(
            f"{self.remote}{path}",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:600]
            raise RuntimeError(f"{path} -> {e.code}: {detail}") from e

    def remote_get(self, path: str) -> dict[str, object]:
        req = urllib.request.Request(f"{self.remote}{path}", headers={"Authorization": f"Bearer {self.token}"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def remote_start(self) -> None:
        """draft を開く — 視聴 URL はこの時点で出る (server の video page が追いかけ再生する)。"""
        kind, aspect, seconds = (self.project / "params.txt").read_text().split()[:3]
        title = (self.project / "request.txt").read_text().strip().splitlines()[0][:200]
        t = time.time()
        body: dict[str, object] = {"title": title, "aspect_ratio": aspect, "duration_s": int(seconds), "language": "ja"}
        if self.remote_template:
            body["template_video_id"] = self.remote_template
        r = self.remote_post("/v1/unstable/drafts/", body)
        self.remote_video_id = str(r["video_id"])
        self.remote_watch_url = str(r["watch_url"])
        self.log(
            event="remote_started",
            s=round(time.time() - t, 1),
            video_id=self.remote_video_id,
            watch_url=self.remote_watch_url,
        )
        print(f"WATCH {self.remote_watch_url}", flush=True)

    def remote_abort(self, reason: str) -> None:
        req = urllib.request.Request(
            f"{self.remote}/v1/unstable/drafts/{self.remote_video_id}/",
            headers={"Authorization": f"Bearer {self.token}"},
            method="DELETE",
        )
        try:
            with urllib.request.urlopen(req, timeout=60):
                pass
            self.log(event="remote_aborted", reason=reason)
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            self.log(event="remote_abort_failed", reason=reason, error=str(e)[:200])

    def remote_wait(self) -> int:
        """server の完成 (status completed) を待つ。途中、見る人が再生を始められる時点 (status の `playable` = 公開 manifest が S3 に
        載った) を 1 回だけ `playable` に記録して `PLAYABLE <url>` を出す (local の `playable` と同じ名 — stream_make の集計が読む)。
        poll の 1 回の失敗 (reload 中の 500 等) では止めない — 続けて失敗する時だけ諦める。"""
        playable_seen = False
        failures = 0
        while True:
            try:
                r = self.remote_get(f"/v1/videos/{self.remote_video_id}/")
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
                self.log(event="playable", video_id=self.remote_video_id)
                print(f"PLAYABLE {self.remote_watch_url}", flush=True)
            st = str(r.get("status"))
            if st in ("completed", "failed", "expired"):
                self.log(
                    event="final_ready" if st == "completed" else "final_failed",
                    since_launch=round(time.time() - self.t0, 1),
                    status=st,
                    broken=self.broken,
                )
                return 0 if st == "completed" else 1
            time.sleep(3)

    # ---- 製品の stream (この機械の DraftStreamRun) ----
    def start_stream(self) -> None:
        """`studio.py stream <project>` を起こす (plan が閉じた時点 — Django と GPU の初期化を最初の cut の経路の外に置く)。
        常駐 server には委ねない (run の間ずっと生きる GPU の process)。"""
        env = {k: v for k, v in self.env.items() if k != "STUDIO_SERVER_SOCK"}
        (self.st / "feed").mkdir(exist_ok=True)
        # stream (organizer + 描画) は check / warm / claude CLI と同じ機械で CPU を取り合う (4 core で load 3〜4.5)。止まりを決めるのは
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
        return self.remote is not None or (self.stream_proc is not None and self.stream_proc.poll() is None)

    def intake_check(self, prefix: str, text: str, *, ended: bool) -> list[str]:
        """投入検査 (製品の API と同じ関数・常駐 server で回す): 投入済みの prefix の後ろに text を足して良いか → DEFECT の行。remote は
        server が投入の時に同じ検査を掛ける (弾かれれば submit が rejected)。"""
        if self.remote is not None:
            return []
        d = self.st / "feed"
        d.mkdir(exist_ok=True)
        (d / "_prefix.txt").write_text(prefix)
        (d / "_text.txt").write_text(text)
        out = self.studio_cmd(
            "intake",
            str(d / "_prefix.txt"),
            str(d / "_text.txt"),
            *(["--end"] if ended else []),
            "--language",
            self.language,
        )
        return [l for l in out.splitlines() if l.startswith("DEFECT")]

    def submit(self, c: str | None, text: str, *, end: bool, pins: dict) -> dict[str, object] | None:
        """cut の text を流す。remote は server の応答 (受理 {"sealed": True} / 拒否 {"rejected": 理由}) をそのまま返す。local の stream は
        file を置いた時点で {"queued": feed 番号} を返し、受理 / 拒否は `watch_acks` が後から記録する (受理を待たずに次の cut を流す —
        seal は organizer が順に処理するので順は守られる。拒否は欠陥 2 件を直してから 0 本)。None = 流す先が死んだ。"""
        if self.remote is not None:
            try:
                r = self.remote_post(f"/v1/unstable/drafts/{self.remote_video_id}/cuts/", {"text": text, "end": end})
            except RuntimeError as e:
                return {"rejected": str(e)[:400]}
            return {"sealed": True, "lines": r.get("lines")}
        from studio_stream import feed_path, write_atomic  # noqa: PLC0415 — scripts dir を sys.path に足している

        if not self.stream_alive():
            return None
        n = self.feed_n
        self.feed_n += 1
        write_atomic(feed_path(self.st, n), {"cut": c, "text": text, "end": end, "pins": pins})
        self.pending_acks[n] = c
        self.log(cut=c, event="submitted", feed=n, end=end, pins=len(pins))
        return {"queued": n}

    def watch_acks(self) -> None:
        """流した feed の受理 / 拒否 (`NNN.ack.json`) を記録する。拒否された cut は壊れ扱い (その定義は次の live な cut へ)。"""
        from studio_stream import ack_path  # noqa: PLC0415

        while True:
            for n, c in list(self.pending_acks.items()):
                path = ack_path(self.st, n)
                if not path.exists():
                    continue
                try:
                    loaded = json.loads(path.read_text())
                except ValueError:
                    continue
                ack = loaded if isinstance(loaded, dict) else {}
                del self.pending_acks[n]
                if "rejected" in ack:
                    if c is not None:
                        self.mark_broken(c, "rejected: " + str(ack["rejected"])[:160])
                    self.log(cut=c, event="submit_rejected", feed=n, reason=str(ack["rejected"])[:300])
                else:
                    self.log(cut=c, event="sealed_ack", feed=n)
            if not self.stream_alive():
                if self.pending_acks:
                    self.log(event="ack_missing", feeds=sorted(self.pending_acks))
                return
            time.sleep(0.2)

    def feed_text(self, c: str) -> str | None:
        """cut c の投入の text (design の block + timeline の block)。根がまだ流れていなければ根を前に付ける (最初に受理される cut が運ぶ)。"""
        blk = self.cut_block(c)
        if blk is None:
            return None
        text = blk[0].rstrip("\n") + "\n" + blk[1].rstrip("\n") + "\n"
        if not self.root_submitted:
            rd, rt = self.root()
            text = rd.rstrip("\n") + "\n" + "\n".join(l for l in rt.splitlines() if l.strip() != "#v2") + "\n" + text
        return text

    def feed(self) -> None:
        """staged かつ warm 済みの cut を構成の順に流す。根は最初に受理される cut と一緒に (以後凍結)。各 cut は投入検査 (prefix との
        compile・出し済みの item が変わらない事・composer の乾いた実行) を通してから流す。投入検査の DEFECT は、落とす前にその cut の
        直し役を 1 回だけ呼び (DEFECT の文と、流した前の cut の定義 `defs_before` を渡す)、直した text で掛け直す (`fix` の
        `round: "intake"`)。この 1 回は stage の直し (2 回まで・`fix_calls`) とは別枠 — stage は staged で終わっていて、投入検査の DEFECT は
        stage の check に出なかった物 (前の cut の担当 / 直しが後から定義を変えた・流した prefix との食い違い) だから。それでも DEFECT なら
        落とす (`intake_rejected`)。local の stream は受理を待たずに次へ (seal は organizer が順に処理する・拒否は `watch_acks` が記録して
        壊れ扱い)。最後の cut は end と一緒に。"""
        prefix = ""  # 流した stream の text (根 + cut)
        for i, c in enumerate(self.order):
            while not (self.staged.get(c) and self.warms[c].done):
                if not self.stream_alive():
                    self.log(event="stream_died", code=self.stream_proc.returncode if self.stream_proc else None)
                    return
                time.sleep(0.3)
            last = i == len(self.order) - 1
            if not self.root_submitted:
                self.root_done.wait(timeout=180)  # 根の pin (BGM の聴取まで) を最初の投入に載せる
            text = None if self.broken.get(c) else self.feed_text(c)
            if text is None:
                self.log(cut=c, event="submit_skipped", broken=self.broken.get(c))
                continue
            t = time.time()
            defects = self.intake_check(prefix, text, ended=last)
            if defects:
                ff = self.st / "feed" / f"intake_{c}.txt"
                ff.write_text(
                    "投入検査 (流した前の cut + この cut) の DEFECT。前の cut はもう流れていて変えられない — 前の cut の定義の形"
                    " (参考の定義) に合わせてこの cut を直す:\n" + "\n".join(defects[:40])
                )
                ok, tail = self.run_fixer(c, ff)
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
                    defects = self.intake_check(prefix, text, ended=last)
            if defects:
                self.mark_broken(c, "intake: " + defects[0][:160])
                self.log(
                    cut=c, event="intake_rejected", s=round(time.time() - t, 1), n=len(defects), first=defects[0][:300]
                )
                continue
            ack = self.submit(c, text, end=last, pins=self.merged_pins([c]).get("asset_pins", {}))
            if ack is None:
                self.log(cut=c, event="stream_died", code=self.stream_proc.returncode if self.stream_proc else None)
                return
            if "rejected" in ack:  # remote だけ (local は受理を待たない — 拒否は watch_acks が後から記録する)
                self.mark_broken(c, "rejected: " + str(ack["rejected"])[:160])
                self.log(cut=c, event="submit_rejected", reason=str(ack["rejected"])[:300])
                continue  # 根を運んでいたなら次の cut が運ぶ (root_submitted のまま False)
            self.root_submitted = True
            prefix += text
            self.submitted.add(c)
            self.log(cut=c, event="fed", s=round(time.time() - t, 1))
            if last:
                return
        if not self.root_submitted:
            # 1 cut も流せなかった — stream を待たせない
            if self.remote is not None:
                self.remote_abort("no cut submitted")
            else:
                from studio_stream import feed_path, write_atomic  # noqa: PLC0415

                write_atomic(feed_path(self.st, self.feed_n), {"abort": True})
                self.feed_n += 1
            self.log(event="feed_aborted", reason="no cut submitted")
            return
        # 最後の cut が壊れて飛んだ時の閉じ (`#end` だけ)
        ack = self.submit(None, "", end=True, pins={})
        if ack is None or "rejected" in ack:
            self.log(event="end_rejected", ack=ack)
            if self.remote is not None:
                self.remote_abort("end rejected")

    def run(self) -> int:
        self.log(event="orchestrator_start")
        while not (self.solo / "order.txt").exists():
            if (
                time.time() - self.t0 > 300 or (self.st / "src.done").exists()
            ):  # 根 call が死んだ (claude が無い等) → 待ち続けない
                self.log(event="root_missing", waited_s=round(time.time() - self.t0, 1))
                return 1
            time.sleep(0.3)
        time.sleep(0.2)
        self.order = [l.strip() for l in (self.solo / "order.txt").read_text().splitlines() if l.strip()]
        self.log(event="plan_seen", cuts=self.order)
        if self.remote is not None:
            self.remote_start()
            for c in self.order:
                self.warms[c].done = True  # 素材は server が解く
            self.root_fast_done.set()  # 根の先読みも server が解く — 最初の投入が root_done を待たない
            self.root_done.set()
            stages = [self.stage]
        else:
            self.start_stream()
            stages = [self.stage, self.warm]
        threads = [threading.Thread(target=self.root_prefetch, daemon=True)] if self.remote is None else []
        for i, c in enumerate(self.order):
            for fn in stages:
                threads.append(threading.Thread(target=self.guarded, args=(fn, i, c), daemon=True))
        threads.append(threading.Thread(target=self.feed, daemon=True))
        if self.remote is None:
            threads.append(threading.Thread(target=self.watch_acks, daemon=True))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        if self.remote is not None:
            return self.remote_wait()
        assert self.stream_proc is not None
        try:
            code = self.stream_proc.wait(timeout=1800)
        except subprocess.TimeoutExpired:
            self.stream_proc.kill()
            code = -9
        if code == 0 and (self.studio / "out/video.mp4").exists():
            (self.studio / "DONE").touch()
            self.log(event="final_ready", since_launch=round(time.time() - self.t0, 1), broken=self.broken)
            return 0
        # 製品の stream が完走しなかった (seal 後の worker の失敗など) — 製品の失敗はそのまま失敗にする (solo の render で描き直す
        # fallback は製品の bug を 2 件隠し、視聴者が見た HLS とも別物だった)
        self.log(event="final_failed", code=code, broken=self.broken)
        return 1


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    project = Path(argv[0]).resolve()
    staff = argv[argv.index("--staff") + 1] if "--staff" in argv else None
    remote = argv[argv.index("--remote") + 1] if "--remote" in argv else None
    token = argv[argv.index("--token") + 1] if "--token" in argv else os.environ.get("NOLANG_API_KEY")
    if token is None and remote is not None:
        token = claude_mcp_token(remote)
    template = argv[argv.index("--template") + 1] if "--template" in argv else None
    run = Run(project, staff=staff, remote=remote, token=token, template=template)
    launch = project / "stream/author.jsonl"
    if launch.exists():
        for l in launch.read_text().splitlines():
            r = json.loads(l)
            if r.get("event") == "launch":
                run.t0 = float(r["t"])
    return run.run()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

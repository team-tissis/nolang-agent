"""cut の段の状態機械 — 著者が落とす cut を出た順に check → (担当) → 直し → 戻し → 最後の手段 → 機械の直し → staged → 投入する。

製品 (`application/video_draft/draft_author/orchestrator.DraftAuthorRun`) と配布 client (`agent_client/scripts/stream_stages.Run`) の
1 本の正本。両者は I/O だけを実装する subclass: check (`check_doc`)・直し役 (`call_fixer`)・投入 (`submit_text`)・warm (`warm_text`)・
改名 (`rename_text`)・記録 (`record`)・担当 (`staff` — client だけ)。製品は memory と同じ process の関数で、client は NoLang API の
HTTP と claude の子 process で運ぶ。意図して違う所はこの class の属性で明示する (`fix_scope`・`reviews`・`fixer_on`・`stills`・
`brief`・`staff`)。標準 library と `author_core` だけに依存する (配布 bundle では scripts の隣に同梱する)。

cut の段 (cut ごとに並列の task):
  受け (前の cut が使う定義はそちらへ移す) → (担当) → check + 直し (見直し + 指摘の直し 2 回まで・最初の DEFECT 0 で warm) → 機械の
  直し (直し役の後に 1 回) → staged → 投入 (構成の順・投入検査で弾かれた cut は直し役を 1 回・別枠)。直しきれない DEFECT は捨てる前に
  最後の手段 (著者の版 → editable の印と動きを機械で寄せる → DEFECT の印を落として台詞を残す) を掛ける。
根の規則: 名のある定義は初めて使う cut の block に書き、その cut だけが直す。根の持ち主は最初の live な cut — 根はその cut の check が
DEFECT 0 で通った時点で先に投入して凍る (弾かれたら最初の cut と一緒に流し、それまでその cut の直し役が根も直せる)。壊れた cut の
定義は次の live な cut へ移る。cut を跨ぐ待ちは投入の順と持ち主待ち (他の cut の行の DEFECT で check が止まった時だけ) だけ。
"""

from __future__ import annotations

import asyncio
import functools
import itertools
import re
import time
from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable, Mapping, Sequence
from dataclasses import dataclass, field, replace
from typing import TYPE_CHECKING

# 製品は libs の package として、配布 client は scripts の隣の top-level module として読む (どちらも author_core は同じ file)
if TYPE_CHECKING or __package__:
    from libs.ai.llm_prompts.draft_author import author_core
else:
    import author_core

# 持ち主が根の DEFECT (blockers / unlocated_owner の値・cut の名にならない綴り)
ROOT = "(root)"
# 指摘の直し役の上限 (著者の版への差し戻しも 1 回と数える)
FIX_CALLS = 2
# 1 cut の check の round の上限 (直し 2 回・見直し 1 回・戻しの往復で普通は 6 以内)
MAX_ROUNDS = 12
_SEP = author_core.TIMELINE_SEP


@dataclass(frozen=True)
class Defect:
    """check の欠陥 (製品の `grammar.lexicon.Defect.as_record()` の形)。`text` は描いた 1 行 (直し役に渡す文面)・場所と同一性は欄で
    見る。`author_core.LocatedDefect` を満たす。"""

    code: str
    file: str  # design.txt / timeline.txt
    line: int  # 0 / 1 = 行の無い欠陥 (RUNTIME など・持ち主は attribute_unlocated が確かめる)
    cause: str
    where: str | None
    level: str  # DEFECT (描けない) / severe / warn / info
    text: str
    # check した cut の block (`join_block` の形) の中の行 (0 始まり)。check_cut が check した doc と同じ組み立てから付ける —
    # doc の行番号は窓の doc の物なので、後から今の状態で範囲を作り直すと別の行を指す
    at: int | None = None

    @classmethod
    def read(cls, d: Mapping[str, object]) -> Defect:
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


@dataclass(frozen=True)
class Lint:
    """check の lint の指摘 (製品の `draft_check.lint.Finding.as_dict()` の形)。"""

    severity: str
    rule: str
    cut: str
    layer: str
    message: str
    hint: str = ""
    autofix: str = ""  # 直し方が一つに決まる指摘の機械の直し (`操作:引数`)

    @classmethod
    def read(cls, d: Mapping[str, object]) -> Lint:
        return cls(
            severity=str(d.get("severity", "")),
            rule=str(d.get("rule", "")),
            cut=str(d.get("cut", "-")),
            layer=str(d.get("layer", "")),
            message=str(d.get("message", "")),
            hint=str(d.get("hint", "")),
            autofix=str(d.get("autofix") or ""),
        )

    def render(self) -> str:
        return f"{self.severity} {self.rule} ({self.layer}): {self.message} — {self.hint}"


@dataclass
class Checked:
    """doc の check の結果。blockers = check を止めた前の cut の DEFECT の持ち主 (`check_cut`)・report = check の表 (client の担当が
    時刻の行を読む)。"""

    defects: list[Defect]
    findings: list[Lint]
    blockers: set[str] = field(default_factory=set[str])
    report: str = ""


@dataclass(frozen=True)
class FixReply:
    """直し役の 1 回の出力。block = 直した cut の block (None = 読めない出力)・root_* = 根の持ち主が直した根 (直していなければ None)。"""

    block: str | None
    tail: str
    root_design: str | None = None
    root_timeline: str | None = None


@dataclass
class Warm:
    """cut 1 つの先行解決の頼みの状態。key = 頼んだ text の素材の鍵 (同じなら頼み直さない)・ok = 投入と同じ検査を通った。"""

    task: asyncio.Task[None] | None = None
    key: author_core.AssetKey | None = None
    ok: bool = False


class FixerUnavailable(Exception):
    """直し役が返らない・API が全部落ちた — 呼び直しても同じなので、直す前の版で続ける (出力が使えないだけなら呼び直す)。"""


class Unreachable(RuntimeError):
    """受け口に届かない・返事を失った (client の HTTP)。段は cut を落とさず、その時の text を投入の門に任せる。"""


class FeedFailed(RuntimeError):
    """投入を終えられない (1 cut も流せなかった・`#end` が弾かれた)。"""


def usable_fix(before: str, block: str) -> bool:
    """直し役の出力を受けられるか — cut を分けない・改名しない (片方だけ戻ると design と timeline の cut が食い違う)。"""
    return _SEP in block and author_core.cut_heads(block) == author_core.cut_heads(before)


def _name_tag(c: str) -> str:
    return re.sub(r"[^a-z0-9]", "", c.lower())[:8] or "c"


def _uses(name: str) -> re.Pattern[str]:
    """名 name の使用 (定義の見出しの `#名` や `.名` の一部ではない)。"""
    return re.compile(rf"(?<![\w#.]){re.escape(name)}(?![\w-])")


class CutStages(ABC):
    """cut の段の状態。subclass は I/O の受け口を実装し、構成 (`order`・`plan`)・依頼 (`request`・`seconds`)・台帳 (`who`・`sure`)
    を置いてから `stages` を回す。根と cut の block は `receive_cut` / `put_root` で受ける。"""

    def __init__(self) -> None:
        # 依頼と構成
        self.request = ""
        self.seconds: float | None = None  # 依頼の長さの目安 (None = おまかせ)
        self.plan = ""
        self.order: list[str] = []
        # 誰が直すか = 製品の台帳の who (fixer = 直し役・machine = 機械の直し・author = 著者に見せるだけ)・sure = 担当の前に当てる機械の直し
        self.who: dict[str, str] = {}
        self.sure: frozenset[str] = frozenset()
        # 直し役に回す指摘の段: defect = 隠れる文字だけ・severe = who=fixer の severe・warn = who=fixer の severe / warn
        self.fix_scope = "severe"
        self.reviews = 0  # 見直し (指摘に出ない弱い所も探す直し役) の回数 — 直し役の 2 回の上限に数えない
        self.fixer_on = True  # 直し役なし (client の `--fix none`) は DEFECT を最後の手段だけで救う
        self.stills = (
            False  # 見直しが静止画を見る (client の `--review`) — 絵を変えた見直しの後は画像を見ない直しを挟む
        )
        self.brief = False  # 著者の版は台詞と絵コンテだけ (client の `--author-brief`) — 著者の版へ差し戻さない
        # 著者の出力
        self.root_design: str | None = None
        self.root_timeline: str | None = None
        self.blocks: dict[str, str] = {}  # cut → 今の block (直し役が書き換える)
        self.author_blocks: dict[str, str] = {}  # cut → 著者の版 (差し戻しの元)
        # 編集の lane の不変 cut (素通し): 親で検証・配信済みの block は凍結し、check も直し役も掛けない。doc の整合のためやむなく
        # 書き換える時は `demote_passthrough` で保証を外す (正しさの機構が優先)
        self.passthrough: set[str] = set()
        self.cut_seen: dict[str, asyncio.Event] = {}
        self.root_seen = asyncio.Event()
        self.author_done = asyncio.Event()
        # 最初の live な cut の check が DEFECT 0 で通った (根を先に流してよい)
        self.root_clear = asyncio.Event()
        # cut の段
        self.staged: dict[str, asyncio.Event] = {}
        self.broken: dict[str, str] = {}
        self.author_clean: set[str] = set()  # 著者の版が check で DEFECT 0 だった cut (差し戻せる)
        self.unlocated_owner: dict[tuple[str, str | None, str], str] = {}  # 行の無い DEFECT の sig → 持ち主の cut
        self.warms: dict[str, Warm] = {}
        self.cut_estimate: dict[str, float] = {}  # cut → check が測った見込み秒 (check の受け口が書く)
        # 改名
        self.root_renames: dict[str, str] = {}
        self.root_checked = False
        self.root_renamed: set[str] = set()
        # 投入
        self.root_submitted = False
        self.submitted: list[str] = []

    # ---- 受け口 (subclass) ----
    @abstractmethod
    def record(self, step: str, **fields: object) -> None:
        """段の記録 (製品は structlog・client は run.jsonl)。"""

    @abstractmethod
    async def check_doc(self, design: str, timeline: str, *, ended: bool, focus: str | None = None) -> Checked:
        """doc の check (compile・composer と layout の乾いた実行・lint・読めない素材・投入の順)。ended = 動画の終わりまで書いた doc・
        focus = lint を要る cut。測った cut の時刻は `cut_estimate` に写す。"""

    @abstractmethod
    async def call_fixer(
        self, c: str, block: str, findings: str, *, review: bool, own_root: bool, rnd: int | str
    ) -> FixReply:
        """直し役を 1 回呼ぶ (block = 今の cut の block・own_root = 根も直せる)。呼び直しても同じ失敗は `FixerUnavailable`。"""

    @abstractmethod
    async def submit_text(self, c: str | None, text: str, *, end: bool) -> list[str] | None:
        """text (根か cut — 根がまだ流れていなければ根も前に付く) を投入検査に掛けて run へ流す → 弾いた DEFECT の行 ([] = 流した)。
        None = 流す先が死んだ。"""

    @abstractmethod
    async def warm_text(self, text: str) -> str | None:
        """未投入の text (根 + c までの live な cut) の素材を run に先に作らせる → 弾かれた理由 (None = 頼んだ)。"""

    @abstractmethod
    def rename_text(self, text: str, renames: Mapping[str, str]) -> str:
        """text の中の層の名を改名する (参照も文法どおり)。同期 — 待つ間に block が変わらないよう event loop を止めて呼ぶ (改名は希)。"""

    async def staff(self, i: int, c: str) -> bool:
        """担当 (cut を仕上げる役) を回したか。製品は担当を置かない (10-25 裁定)。"""
        del i, c
        return False

    # ---- 受けと書き換え ----
    def receive_cut(self, name: str, body: str) -> None:
        """著者が書いた cut の block を受ける (著者の版として残す)。"""
        if name in self.blocks:
            self.record("cut_written_twice", cut=name)
            return
        self.blocks[name] = body
        self.author_blocks[name] = body
        self.cut_seen.setdefault(name, asyncio.Event()).set()
        if self.order and name not in self.order:
            self.record("cut_not_in_plan", cut=name)

    def put(self, c: str, text: str) -> None:
        """cut c の block を書き換える (client は file にも写す)。"""
        self.blocks[c] = text

    def put_root(self, design: str, timeline: str) -> None:
        self.root_design, self.root_timeline = design, timeline

    async def until_cut(self, c: str) -> bool:
        """cut c の block が届くまで待つ (著者が書き終えたのに無ければ False)。"""
        seen = self.cut_seen.setdefault(c, asyncio.Event())
        if not seen.is_set():
            await _first_of(seen, self.author_done)
        return c in self.blocks

    # ---- block と doc ----
    def cut_block(self, c: str) -> tuple[str, str] | None:
        text = self.blocks.get(c)
        return author_core.split_block(c, text) if text is not None else None

    def root(self) -> tuple[str, str]:
        """根の 2 block。`until: end` の進行線には見込みの全長を書き足す (stream では全長が最後の cut まで決まらない)。"""
        rd = (self.root_design or "#v2\n").rstrip("\n") + "\n"
        rt = (self.root_timeline or "#v2\n").rstrip("\n") + "\n"
        total = self.planned_total_ms()
        if total is not None:
            rd = re.sub(
                r"^(progress#[A-Za-z0-9_]+\([^\n]*?until:\s*end)(?![^\n]*total:)",
                rf"\1; total: {total}ms",
                rd,
                flags=re.M,
            )
        return rd, rt

    def first_live(self) -> str | None:
        return next((c for c in self.order if not self.broken.get(c)), None)

    def owns_root(self, c: str) -> bool:
        """cut c が根の持ち主か = 最初の live な cut で、根がまだ流れていない。"""
        return c == self.first_live() and not self.root_submitted

    def live_cuts(self, cuts: Sequence[str]) -> list[str]:
        """壊れた cut は後の doc から外す (最後の cut は残す — ended の判定に要る)。"""
        return [c for c in cuts if not self.broken.get(c) or c == cuts[-1]]

    def doc_texts(self, cuts: Sequence[str], *, root_extra: str = "") -> tuple[str, str]:
        """doc (根 + root_extra + cuts の block) の design / timeline。root_extra = 根の design の後ろに足す行 (除いた cut の定義)。"""
        rd, rt = self.root()
        design, timeline = [rd + root_extra], [rt]
        for c in cuts:
            blk = self.cut_block(c)
            if blk:
                design.append(blk[0])
                timeline.append(blk[1])
        return "".join(design), "".join(timeline)

    def doc(self, cuts: Sequence[str], *, root_extra: str = "") -> tuple[str, str]:
        """check する doc — 組む前に名の衝突を解く。"""
        self.rename_collisions(cuts)
        return self.doc_texts(cuts, root_extra=root_extra)

    def cut_line_ranges(
        self, cuts: Sequence[str], *, root_extra: str = ""
    ) -> dict[str, tuple[tuple[int, int], tuple[int, int]]]:
        """doc の中の cut ごとの design / timeline の行の範囲 [a, b] (1 始まり)。"""
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

    def root_text(self) -> str:
        """根の stream の text (design の block + `#v2` を除いた timeline の block)。"""
        rd, rt = self.root()
        return rd.rstrip("\n") + "\n" + "\n".join(line for line in rt.splitlines() if line.strip() != "#v2") + "\n"

    def feed_text(self, c: str) -> str | None:
        """cut c の投入の text。根がまだ流れていなければ根を前に付ける (根の先行投入が弾かれた時)。"""
        blk = self.cut_block(c)
        if blk is None:
            return None
        text = blk[0].rstrip("\n") + "\n" + blk[1].rstrip("\n") + "\n"
        return (text if self.root_submitted else self.root_text() + text).strip("\n")

    # ---- 名 ----
    def normalize_root(self) -> None:
        """根の字下げ無しの行が予約名 (`div#bg`) を定義していたら `名_root` に改名する (1 回)。根の DEFECT:NAME は cut の直し役では消えない。"""
        if self.root_checked or self.root_design is None or self.root_timeline is None:
            return
        self.root_checked = True
        names = [m.group(2) for m in author_core.TOP_DEF.finditer(self.root_design) if m.group(1) != "section"]
        renames = {n: f"{n}_root" for n in dict.fromkeys(names) if n in author_core.RESERVED_NAMES}
        if not renames:
            return
        self.put_root(self.rename_text(self.root_design, renames), self.rename_text(self.root_timeline, renames))
        self.root_renames = renames
        self.record("rename_root", names=renames)

    def rename_collisions(self, cuts: Sequence[str]) -> None:
        """根か前の cut が定義した名を後の cut が字下げ無しの行で定義していたら (著者は互いの cut の名を知らずに書く)、後の cut の側の名を
        その block の中で `名_<cut>` に改名する (cut の届く順に依らず同じ結果)。根の予約名を改名した後に届いた cut は参照を同じ名に揃える。"""
        self.normalize_root()
        rd, _ = self.root()
        seen = {m.group(2) for m in author_core.TOP_DEF.finditer(rd)} | set(author_core.RESERVED_NAMES)
        for c in cuts:
            if self.root_renames and c not in self.root_renamed and c in self.blocks:
                self.root_renamed.add(c)
                renamed_text = self.rename_text(self.blocks[c], self.root_renames)
                if renamed_text != self.blocks[c]:
                    self.demote_passthrough(c, "root_rename")
                    self.put(c, renamed_text)
            blk = self.cut_block(c)
            if not blk:
                continue
            names = [m.group(2) for m in author_core.TOP_DEF.finditer(blk[0]) if m.group(1) != "section"]
            clash = [
                n
                for n in dict.fromkeys(names)
                if n in seen and (author_core.RENAMABLE.match(n) or n in author_core.RESERVED_NAMES)
            ]
            if clash:
                tag = _name_tag(c)
                renamed: dict[str, str] = {}
                for n in clash:
                    new = f"{n}_{tag}"
                    k = 2
                    while new in seen or new in names:
                        new = f"{n}_{tag}{k}"
                        k += 1
                    renamed[n] = new
                self.demote_passthrough(c, "rename_collision")
                self.put(c, self.rename_text(self.blocks[c], renamed))
                self.record("rename", cut=c, names=renamed)
                blk = self.cut_block(c) or blk
                names = [m.group(2) for m in author_core.TOP_DEF.finditer(blk[0]) if m.group(1) != "section"]
            seen.update(names)

    # ---- 定義 ----
    def defs_before(self, c: str) -> str:
        """c より前の live な cut の block の名のある定義 (担当・直し役の参考)。"""
        parts: list[str] = []
        for x in self.order[: self.order.index(c)]:
            blk = self.cut_block(x)
            if blk and not self.broken.get(x):
                parts.extend(text for _kind, _name, text in author_core.named_defs(blk[0]))
        return "".join(parts)

    def move_forward_defs(self, c: str) -> None:
        """cut c の block の定義のうち、前の cut (まだ staged でない) が既に使っている名の物は、その cut の block へ移す (定義は初めて
        使う cut の物 — 前の cut の check が NAME で落ちない)。"""
        blk = self.cut_block(c)
        if blk is None:
            return
        moved: list[str] = []
        for _kind, name, text in author_core.named_defs(blk[0]):
            pattern = _uses(name)
            for u in self.order[: self.order.index(c)]:
                # 素通しの block へは移さない (凍結) — 届かない名は u の check / 投入検査が拾う
                if self.staged[u].is_set() or self.broken.get(u) or u in self.passthrough:
                    continue
                ublk = self.cut_block(u)
                if ublk is None or any(n == name for _k, n, _t in author_core.named_defs(ublk[0])):
                    # u は同じ名を自分で定義している (別の種でも — hook の `motion row` に引かれて parts の `def row` を hook へ移し、
                    # hook の担当がそれを消して parts が落ちた o11_16)。名が u に出るのはその定義の使用
                    continue
                if pattern.search(ublk[0]) or pattern.search(ublk[1]):
                    self.put(u, author_core.add_defs(self.blocks[u], text))
                    moved.append(text)
                    self.record("def_moved", cut=c, name=name, to=u)
                    break
        if moved:
            body = self.blocks[c]
            for text in moved:
                body = body.replace(text, "", 1)
            self.put(c, body)

    def adopt_defs_of(self, b: str) -> None:
        """壊れた cut b の定義を、b の後の最初の live な (まだ流していない) cut の block に移す — 後の cut がその名を使えるように。"""
        blk = self.cut_block(b)
        if blk is None:
            return
        texts = "".join(text for _kind, _name, text in author_core.named_defs(blk[0]))
        if not texts:
            return
        for x in self.order[self.order.index(b) + 1 :]:
            if self.broken.get(x) or x in self.submitted or x not in self.blocks:
                continue
            self.demote_passthrough(x, "defs_adopted")
            self.put(x, author_core.add_defs(self.blocks[x], texts))
            self.record("defs_adopted", cut=b, by=x)
            return

    def mark_broken(self, c: str, reason: str) -> None:
        self.broken[c] = reason
        self.adopt_defs_of(c)
        self.record("broken", cut=c, reason=reason)

    def demote_passthrough(self, c: str, reason: str) -> None:
        """素通しの block をやむなく書き換える前に凍結の保証を外して記録する。staged 済みでも check は掛け直さない
        (compile 級は投入検査が拾う) — ここに来るのは編集役が定義を動かした希な doc だけで、正しさの機構を優先する。"""
        if c in self.passthrough:
            self.passthrough.discard(c)
            self.record("passthrough_demoted", cut=c, reason=reason)

    def used_later(self, c: str, name: str) -> bool:
        """名 name を c より後の cut (著者の版か今の版) が使っているか。著者がまだ書き終えていなければ使うと見る。"""
        if not self.author_done.is_set():
            return True
        pattern = _uses(name)
        for x in self.order[self.order.index(c) + 1 :]:
            for text in (self.blocks.get(x), self.author_blocks.get(x)):
                if text is not None and pattern.search(text):
                    return True
        return False

    def children_used_later(self, c: str, name: str, children: set[str]) -> set[str]:
        """定義 name の子のうち、c より後の cut が `実体.子` / `実体[k].子` で参照する物。著者が書き終えていなければ全部を参照すると見る。"""
        if not children:
            return set()
        if not self.author_done.is_set():
            return set(children)
        instance = re.compile(rf"(?<![\w#.$-]){re.escape(name)}#([A-Za-z_][\w-]*)")
        used: set[str] = set()
        for x in self.order[self.order.index(c) + 1 :]:
            for text in (self.blocks.get(x), self.author_blocks.get(x)):
                if text is None:
                    continue
                for inst in set(instance.findall(text)):
                    refs = re.findall(rf"(?<![\w-]){re.escape(inst)}(?:\[[^\]]*\])?\.([A-Za-z_][\w-]*)", text)
                    used |= children & set(refs)
        return used

    def restore_defs(self, c: str, before: str, *, keep_looks: bool = False) -> None:
        """担当か直し役が書き戻した cut c の名のある定義を、書き戻す前の text と比べて直す。
        - 消した定義は戻す (後の cut はその名を使っている — 前の cut が同じ種と名で定義していれば重複の直しなので戻さない)。
        - 後の cut が使う定義の形 (引数の並び・後の cut が `実体.子` で参照する子の名) を変えていたら元の定義に戻す — 後の cut は著者の版の
          形で書かれている (now7_05: 担当が `def node(i, t, c=$a)` を `node(p, t, n)` に変え、後の cut が投入検査の DEFECT:ARG で落ちた)。
          def は変えた側の版を `名_<cut>` に改名してこの block の使い方ごと残す。def 以外の種は元に戻すだけ。
        keep_looks = 同じ形のまま見た目 (大きさ・余白・色) を変えた定義も形の変更と同じに扱う (担当 — 後の cut の担当は元の見た目で並列に
        置いている・nw1 の判子 52 → 112px)。直し役は DEFECT を直すために定義の中身を変えるので形だけを見る。"""
        blk = self.cut_block(c)
        if blk is None or _SEP not in before:
            return
        # 種ごとに見る — 名だけで見ると雛形の `motion note` が残っているだけで消した `def note` を「残っている」と誤った (o20_18)
        now = {(kind, name): text for kind, name, text in author_core.named_defs(blk[0])}
        earlier = {(kind, name) for kind, name, _t in author_core.named_defs(self.defs_before(c))}
        missing: list[tuple[str, str]] = []
        reshaped: list[tuple[str, str, str, str]] = []
        lost: dict[str, list[str]] = {}  # 名 → 後の cut が参照するのに消えた子の名
        for kind, name, text in author_core.named_defs(before.split(_SEP, 1)[0]):
            cur = now.get((kind, name))
            if cur is None:
                if (kind, name) not in earlier:
                    missing.append((name, text))
                continue
            gone = sorted(
                self.children_used_later(c, name, author_core.def_children(text)) - author_core.def_children(cur)
            )
            looks = keep_looks and re.sub(r"\s+", " ", cur).strip() != re.sub(r"\s+", " ", text).strip()
            if (author_core.def_signature(cur) != author_core.def_signature(text) or gone or looks) and self.used_later(
                c, name
            ):
                reshaped.append((kind, name, cur, text))
                if gone:
                    lost[name] = gone
        for _name, text in missing:
            self.put(c, author_core.add_defs(self.blocks[c], text))
        if missing:
            self.record("defs_restored", cut=c, reason="missing", names=[name for name, _ in missing])
        if not reshaped:
            return
        design, sep, timeline = self.blocks[c].partition(_SEP)
        kept: dict[str, str] = {}
        for kind, name, cur, text in reshaped:
            if kind != "def":
                design = design.replace(cur, text, 1)
                continue
            taken = {n for _k, n, _t in author_core.named_defs(design)}
            new = f"{name}_{_name_tag(c)}"
            while new in taken:
                new += "x"
            # 変えた側の def の見出し・この block の要素の型 (`名#…`)・他の def の土台 (`= 名(`) を新しい名に。元の定義はその後ろに戻す
            uses = re.compile(rf"(?<![\w#.$-]){re.escape(name)}(?=[#(])")
            design = uses.sub(new, design).replace(uses.sub(new, cur), uses.sub(new, cur) + text, 1)
            kept[name] = new
        self.put(c, design + sep + timeline)
        self.record(
            "defs_restored",
            cut=c,
            reason="shape",
            names=[name for _k, name, _c, _t in reshaped],
            was=[author_core.def_signature(text) for _k, _n, _c, text in reshaped],
            now=[author_core.def_signature(cur) for _k, _n, cur, _t in reshaped],
            lost_children=lost,
            kept_as=kept,
        )

    def revert_to_author(self, c: str) -> bool:
        """cut c を著者の版に差し替える。著者の版に無い名のある定義で後の cut が使う物 (後の cut が移した定義・壊れた cut から移った
        定義) は残す → 差し替えたか。brief の著者の版は絵の無い版なので差し替えない (11-02 dev 67aca628 cli_flow が真っ白)。"""
        author = self.author_blocks.get(c)
        if author is None or self.brief:
            return False
        now = self.blocks[c]
        text = author
        had = {(k, n) for k, n, _t in author_core.named_defs(author.split(_SEP, 1)[0])}
        for kind, name, def_text in author_core.named_defs(now.split(_SEP, 1)[0]):
            if (kind, name) not in had and self.used_later(c, name):
                text = author_core.add_defs(text, def_text)
        self.put(c, text)
        return text != now

    # ---- 尺 ----
    def plan_seconds(self) -> dict[str, float]:
        """plan の cut ごとの目標秒 (著者が長さの目安を cut へ配った値)。無ければ空。"""
        return dict(author_core.plan_names(self.plan)) if self.plan else {}

    def estimated_seconds(self) -> dict[str, float]:
        """cut ごとの見込み秒 = check が測った値 (あれば) → 著者の plan の秒 → 10 s。"""
        plan = self.plan_seconds()
        return {c: self.cut_estimate.get(c, plan.get(c, 10.0)) for c in dict.fromkeys([*plan, *self.order])}

    def planned_total_ms(self) -> int | None:
        total = sum(self.estimated_seconds().values())
        return int(total * 1000) if total > 0 else None

    @functools.cached_property
    def verbatim(self) -> bool:
        """依頼の台本をそのまま読む動画か — 尺の指摘を掛けない (文の足し引きが依頼の台本の改変になる)。plan が閉じてから読む。"""
        if not author_core.is_verbatim(self.plan, self.request):
            return False
        self.record(
            "verbatim",
            plan_mark=author_core.VERBATIM_MARK in self.plan,
            request_phrase=author_core.VERBATIM_REQUEST.search(self.request) is not None,
        )
        return True

    def cut_budget(self, c: str) -> float | None:
        """cut c の台詞の尺の予算 = plan の目標秒。締めの cut は弾性 (依頼の目安から前の live な cut の見込みを引いた残り)。"""
        plan = self.plan_seconds()
        if c not in plan:
            return None
        if c != self.order[-1] or self.seconds is None:
            return plan[c]
        before = sum(self.cut_estimate.get(x, plan.get(x, 10.0)) for x in self.order[:-1] if not self.broken.get(x))
        return author_core.closing_budget(self.seconds, before)

    def length_finding(self, c: str) -> str:
        """見直しに添える尺の指摘の 1 行 (`author_core.length_finding`)。逐語の動画と最初の cut は見ない (再生開始の臨界路・ずれは
        締めの cut の弾性が吸う)。"""
        budget, estimate, blk = self.cut_budget(c), self.cut_estimate.get(c), self.cut_block(c)
        if self.verbatim or c == self.order[0] or budget is None or estimate is None or blk is None:
            return ""
        return author_core.length_finding(estimate, budget, blk[1])

    def cut_length(self, c: str) -> dict[str, float | None]:
        """staged の時点の cut c の尺の記録: plan の目標秒・予算・著者の宣言 (`# 台詞 ~N s`)・check の見積り。"""
        author = self.author_blocks.get(c)
        declared = author_core.DECLARED_SECONDS.search(author) if author is not None else None
        estimate, budget = self.cut_estimate.get(c), self.cut_budget(c)
        return {
            "plan_s": self.plan_seconds().get(c),
            "budget_s": None if budget is None else round(budget, 1),
            "declared_s": float(declared.group(1)) if declared else None,
            "estimate_s": None if estimate is None else round(estimate, 1),
        }

    # ---- 指摘の振り分け ----
    def attribute_lint(self, findings: list[Lint], c: str) -> list[Lint]:
        """cut の無い lint の指摘 (`cut=-`: design 由来の shrunk / child_overflow など) を、層の名がこの cut の block に定義されて
        いれば この cut の物にする (`cut=-` のままだと誰の物にもならず直らなかった)。"""
        blk = self.cut_block(c)
        if not blk:
            return findings
        out: list[Lint] = []
        for f in findings:
            base = re.split(r"[.\[×( ]", f.layer)[0].strip("'\")")
            if f.cut == "-" and base and re.search(r"#" + re.escape(base) + r"(?:[\s(.\[]|$)", blk[0], re.M):
                f = replace(f, cut=c)
            out.append(f)
        return out

    def to_fix(self, f: Lint) -> bool:
        """直し役 (LLM) の規則か = 台帳の who=fixer。"""
        return self.who.get(f.rule, "author") == "fixer"

    def fix_finding(self, f: Lint) -> bool:
        """直し役に回す指摘か (`fix_scope` の段): defect = 隠れる文字だけ・severe = who=fixer の severe・warn = who=fixer の severe / warn。"""
        if not self.to_fix(f):
            return False
        if self.fix_scope == "warn":
            return f.severity in ("severe", "warn")
        if self.fix_scope == "severe":
            return f.severity == "severe"
        return f.rule == "occluded" and f.severity == "severe"

    def root_layer(self, c: str, f: Lint) -> bool:
        """指摘の層が根の物 (字幕・根に書いた要素) で、cut c がその持ち主でない = c の直し役には直せない (根は凍っている)。渡すと
        直し役が cut の block に根の行を書き直して DEFECT:ROOT_AFTER_CUT になり、丸ごと戻しを繰り返した (10-28: 字幕の offscreen)。"""
        if self.owns_root(c):
            return False
        base = f.layer.split(".")[0].split("[")[0]
        layers = {m.group(1) for m in re.finditer(r"^\s*[a-z_]+#([A-Za-z_]\w*)", self.root_design or "", re.M)}
        return base == "subtitle" or base in layers

    # ---- check ----
    async def attribute_unlocated(
        self, c: str, cuts: Sequence[str], unlocated: list[Defect], *, root_extra: str = ""
    ) -> tuple[list[Defect], list[Defect]]:
        """行の無い DEFECT の持ち主: c を除いた doc でも出るなら c の物ではない (前の cut か根の物)。c が最初の live な cut なら除いた
        doc は根だけ — 出れば根の物 (c の DEFECT として返し、持ち主を ROOT で覚える)。確かめないと前の cut の空の text 1 つが後の cut
        全部の check に出て、どの cut の直しでも消えずに全部が壊れた (s8 の 16)。"""
        prev = [x for x in cuts if x != c and not self.broken.get(x) and x in self.blocks]
        design, timeline = self.doc(prev, root_extra=root_extra)
        base = await self.check_doc(design, timeline, ended=False)
        there = {d.text for d in base.defects}
        mine = [d for d in unlocated if d.text not in there]
        foreign = [d for d in unlocated if d.text in there]
        for d in mine:
            self.unlocated_owner[d.sig] = c
        if not prev:
            for d in foreign:
                self.unlocated_owner[d.sig] = ROOT
            mine, foreign = mine + foreign, []
        return mine, foreign

    async def check_cut(self, c: str, cuts: Sequence[str], rnd: int | str, *, root_extra: str = "") -> Checked:
        """doc (根 + cuts・c を含む) を check し、cut c (か根) の DEFECT と lint を返す。blockers = check を止めた前の cut の DEFECT の
        持ち主 (行の無い DEFECT で持ち主が分からなければ "?") — blockers があればその doc の lint は c の物も含めて出ていない。
        root_extra の行の DEFECT は根の物と数える。"""
        # 行の範囲は check する doc と同じ時点で作る (check を待つ間に前の cut の書き戻しや根の put が行数を変える)
        design, timeline = self.doc(cuts, root_extra=root_extra)
        ranges = self.cut_line_ranges(cuts, root_extra=root_extra)
        rd, rt = self.root()
        root_n = ((rd + root_extra).count("\n"), rt.count("\n"))
        checked = await self.check_doc(design, timeline, ended=cuts[-1] == self.order[-1], focus=c)
        defects: list[Defect] = []
        unlocated: list[Defect] = []
        blockers: set[str] = set()
        for d in checked.defects:
            n, which = d.line, d.which
            if n <= 1:
                unlocated.append(d)
                continue
            if n <= root_n[which]:
                # 根の行: 持ち主は欠陥の場所 `*** 名` の cut (根の行を使って壊れた cut — 根の既定の切替は使った境界の cut が自分の
                # 切替で上書きできる)。doc に無い場所は根の持ち主 = 最初の live な cut。他の cut はその staged を待つ。場所を見ないと
                # 根を流した後の既定の切替の DEFECT が誰の物にもならず、後の cut が lint 無しで素通りした (11-03 R2 の dir: 'top')
                scope = d.where.removeprefix("*** ") if d.where and d.where.startswith("*** ") else None
                owner = scope if scope in ranges else ROOT
                if owner == c or (owner == ROOT and c == self.first_live()):
                    defects.append(d)
                else:
                    blockers.add(owner)
                continue
            owner = next((k for k, r in ranges.items() if r[which][0] <= n <= r[which][1]), None)
            if owner == c:
                (a, _b), (da, db) = ranges[c][which], ranges[c][0]
                defects.append(replace(d, at=(n - a) + (0 if which == 0 else db - da + 2)))
            elif owner is None:
                defects.append(d)
            else:
                blockers.add(owner)
        if unlocated:
            mine, foreign = await self.attribute_unlocated(c, cuts, unlocated, root_extra=root_extra)
            defects += mine
            if foreign:
                # 持ち主は doc の中の c より前の cut だけ — sig の map は run 全体の物で後ろの cut を返し得る。後ろを待つと 2 つの
                # cut が互いの staged を待って止まる (10-27 fit / r3)。前に居なければ "?" (= 最初の live な cut)
                earlier = set(cuts[: list(cuts).index(c)])
                owners = {self.unlocated_owner.get(d.sig, ROOT) for d in foreign}
                blockers |= {o if o in earlier else "?" for o in owners}
                self.record("defect_elsewhere", cut=c, round=rnd, n=len(foreign), first=foreign[0].text[:160])
        return Checked(
            defects=defects,
            findings=self.attribute_lint(checked.findings, c),
            blockers=blockers,
            report=checked.report,
        )

    async def wait_owners(self, c: str, owners: set[str]) -> None:
        """持ち主の cut (根なら最初の live な cut) が staged になるまで。"""
        while True:
            targets = {(self.first_live() or c) if o in (ROOT, "?") else o for o in owners} - {c}
            pending = [self.staged[x] for x in targets if x in self.staged and not self.staged[x].is_set()]
            if not pending:
                return
            await pending[0].wait()

    async def check_without(self, c: str, cuts: Sequence[str], skip: frozenset[str], rnd: int | str) -> Checked:
        """skip の cut を除いた doc で c を check する。除いた cut の名のある定義は根の後ろに写す — c が使う名が除いた cut の block に
        あると、除いただけの doc では c の行に誤った DEFECT が出る (nt06 gold)。"""
        extra = "".join(
            text
            for x in cuts
            if x in skip and (blk := self.cut_block(x)) is not None
            for _kind, _name, text in author_core.named_defs(blk[0])
        )
        return await self.check_cut(c, [x for x in cuts if x not in skip], rnd, root_extra=extra)

    _CROSSING_KINDS = frozenset({"bg", "avatar"})  # 既定で cut を跨ぐ族 (spans.py DEFAULT_SPANS)
    _DECL_RE = re.compile(r"(?m)^\s*([a-z_]+)#([A-Za-z_][\w-]*)([\w.\-]*)")
    _MARK_RE = re.compile(r"\[([<>!=])((?:#[A-Za-z_][\w.-]*(?:\[[^\]]*\])?(?:\.[\w-]+)*(?:\{[^}]*\})?,?)+)")
    _BGM_RE = re.compile(r"(?m)^bgm\s+([A-Za-z_][\w-]*)")

    def outside_window(self, c: str, cuts: Sequence[str]) -> frozenset[str]:
        """c の check に要らない cut (窓の外)。窓 = 最初の cut・直前の cut・c と、c の時点でまだ開いている cut を跨ぐ状態を持つ cut
        (字幕の lane を最後に開けた cut・閉じていない `.sticky` / 既定で跨ぐ族 / bgm を宣言した cut とそれに最後に印を打った cut)。
        開けた cut と閉じた cut は対で入れる。check の時間を cut 数に依らず一定にする (10-27・737 cut で DEFECT / severe の差 0)。"""
        i = list(cuts).index(c)
        opened: dict[str, int] = {}  # 跨ぐ層の名 → 宣言 (か開けた) cut
        touched: dict[str, int] = {}  # 名 → 最後に印を打った cut
        closed: list[tuple[int, int]] = []  # (開けた cut, 閉じた cut)
        for j in range(i):
            blk = self.cut_block(cuts[j])
            if blk is None:
                continue
            for m in self._DECL_RE.finditer(blk[0]):
                tag, name, flags = m.groups()
                if ".sticky" in flags or tag in self._CROSSING_KINDS:
                    opened[name] = j
            for m in self._BGM_RE.finditer(blk[1]):
                opened[m.group(1)] = j
            for m in self._MARK_RE.finditer(blk[1]):
                op = m.group(1)
                for name in re.findall(r"#([A-Za-z_][\w-]*)", m.group(2)):
                    if name == "subtitle":
                        if op != "<":
                            opened["subtitle"] = j
                        elif "subtitle" in opened:
                            closed.append((opened.pop("subtitle"), j))
                    elif name in opened:
                        if op == "<":
                            closed.append((opened.pop(name), j))
                            touched.pop(name, None)
                        else:
                            touched[name] = j
        keep = {0, max(0, i - 1), i} | set(opened.values()) | set(touched.values())
        while True:
            more = {b for a, b in closed if a in keep} | {a for a, b in closed if b in keep}
            if more <= keep:
                break
            keep |= more
        return frozenset(cuts[j] for j in range(i) if j not in keep)

    async def check_settled(self, c: str, i: int, rnd: int | str) -> Checked:
        """窓の doc (根 + 窓の外の cut の定義 + 窓の cut) で c を check する。前の cut (か根) の DEFECT で check が止まったら、持ち主の
        分かる cut はその cut も除いた doc で取り (前の cut の直しと c の直しが並列に進む)、分からない時か除くと c に DEFECT が出る時は
        持ち主が staged になるまで待って掛け直す。掛け直しの check を止めた新しい持ち主もまた待つ (nt03 rain)。待った持ち主が staged
        なのにまだ止める時だけ打ち切る (残りは投入検査が拾う)。"""
        waited: set[str] = set()
        while True:
            cuts = self.live_cuts(self.order[: i + 1])
            outside = self.outside_window(c, cuts)
            res = await (self.check_without(c, cuts, outside, rnd) if outside else self.check_cut(c, cuts, rnd))
            if res.defects or not res.blockers:
                return res
            skip = frozenset(res.blockers - {"?", ROOT})
            if skip and not (res.blockers & {"?", ROOT}):
                skipped = await self.check_without(c, cuts, skip | outside, rnd)
                if not skipped.defects and not skipped.blockers:
                    self.record("lint_skip", cut=c, round=rnd, skip=sorted(skip))
                    return skipped
            if res.blockers <= waited:
                self.record("lint_blocked", cut=c, round=rnd, owners=sorted(res.blockers), stuck=True)
                return res
            self.record("lint_blocked", cut=c, round=rnd, owners=sorted(res.blockers))
            await self.wait_owners(c, res.blockers)
            waited |= res.blockers

    # ---- 直し役と戻し ----
    async def run_fixer(self, c: str, findings: str, *, review: bool = False, rnd: int | str) -> tuple[bool, str]:
        """直し役を 1 回。通れば cut の block (と根の持ち主なら根) を書き戻す → (通ったか, 出力の末尾)。通らない = 出力が使えない
        (読めない・cut を分けた) — 呼び直せば通り得る。呼び直しても同じ失敗は `FixerUnavailable` をそのまま上げる。"""
        self.demote_passthrough(c, "fixer")
        before = self.blocks[c]
        own_root = self.owns_root(c)
        reply = await self.call_fixer(c, before, findings, review=review, own_root=own_root, rnd=rnd)
        if reply.block is None:
            return False, reply.tail
        if not usable_fix(before, reply.block):
            self.record(
                "fix_structure_changed",
                cut=c,
                before=author_core.cut_heads(before),
                after=author_core.cut_heads(reply.block),
            )
            return False, "the fix changed the cut's headings (split or renamed the cut)"
        if own_root and not self.root_submitted and (reply.root_design or reply.root_timeline):
            self.put_root(reply.root_design or self.root_design or "", reply.root_timeline or self.root_timeline or "")
        # 基準は書き戻す直前の block (直し役が走る間に後の cut が c の block へ移した定義も含む)
        latest = self.blocks[c]
        self.put(c, reply.block)
        self.restore_defs(c, latest if _SEP in latest else before)
        return True, reply.tail

    def _revert_regions(self, c: str, before: str, bad: set[int]) -> bool:
        """cut c の今の block のうち、bad (0 始まりの行番号) を含む直し役の変更の塊を before に戻す → 戻したか。"""
        blk, before_blk = self.cut_block(c), author_core.split_block(c, before)
        if blk is None or before_blk is None:
            return False
        after_text, before_text = author_core.join_block(*blk), author_core.join_block(*before_blk)
        new_text = author_core.revert_changed_regions(before_text, after_text, bad) if bad else before_text
        if new_text is None or new_text == after_text:
            return False
        self.put(c, author_core.prune_orphan_elements(before_text, after_text, new_text))
        return True

    def revert_fixer_damage(self, c: str, before: str, defects: Sequence[Defect]) -> int:
        """直し役の後の check の DEFECT が直し役の変えた行にあれば、その変更の塊だけ直し前に戻す (2 回以上の直しの 3/6 は直し役が自分で
        作った DEFECT だった)。行の無い DEFECT は直し全体を戻す。戻した DEFECT の数 (0 = 直し役の変更の外 → 直し役へ)。行は
        check_cut が付けた block の中の行 (`Defect.at`)。"""
        whole = any(d.line <= 1 for d in defects)
        bad = {d.at for d in defects if d.at is not None}
        if not (whole or bad) or not self._revert_regions(c, before, set() if whole else bad):
            return 0
        return len(defects) if whole else len(bad)

    def revert_new_findings(self, c: str, before: str, findings: Sequence[Lint]) -> int:
        """直しが新しく作った指摘の層を指す行 (section の `#名(`・印の `#名`) のうち、直し役が変えた塊にある物を直す前に戻す → 戻した
        指摘の数。"""
        blk = self.cut_block(c)
        if blk is None:
            return 0
        bad, hit = author_core.rows_naming_layers(author_core.join_block(*blk), [f.layer for f in findings])
        return hit if bad and self._revert_regions(c, before, bad) else 0

    async def last_resort(
        self,
        c: str,
        cuts: Sequence[str],
        rnd: int | str,
        passes: Callable[[], Awaitable[bool]],
    ) -> bool:
        """直しきれない DEFECT で cut c を捨てる前の最後の手段 (stage と投入検査で同じ順): 著者の版 → doc の check で c の行を指す
        DEFECT の行を落とす (台詞は残して印だけ・落とした中身は `defect_lines_dropped` の `lines`)。どれも通らなければ元の block に
        戻して False (捨てるのは呼び手)。"""
        self.demote_passthrough(c, "last_resort")
        current = self.blocks[c]
        if self.revert_to_author(c):
            if await passes():
                self.record("revert_author", cut=c, round=rnd, last_resort=True)
                return True
            self.put(c, current)
        dropped: list[dict[str, object]] = []
        for _attempt in range(4):
            design, timeline = self.doc(cuts)
            checked = await self.check_doc(design, timeline, ended=cuts[-1] == self.order[-1])
            design, timeline, now = author_core.drop_defect_lines(design, timeline, c, checked.defects)
            block = author_core.block_in_doc(design, timeline, c)
            if not now or block is None:
                break
            dropped += now
            self.put(c, block)
            if await passes():
                # 落とした中身 (台詞・印・素材) は記録に残す — client は stream_make.sh の最終出力が利用者向けに並べる
                self.record("defect_lines_dropped", cut=c, round=rnd, n=len(dropped), lines=dropped)
                return True
        self.put(c, current)
        return False

    async def rescue_stage(self, i: int, c: str, rnd: int | str) -> bool:
        """stage の最後の手段 — 通ったか = doc (根 + live な cut 0..i) の check で c の DEFECT も止める持ち主も無い。"""

        async def passes() -> bool:
            res = await self.check_settled(c, i, rnd)
            return not res.defects and not res.blockers

        return await self.last_resort(c, self.live_cuts(self.order[: i + 1]), rnd, passes)

    # ---- cut の段 ----
    async def stage(self, i: int, c: str) -> None:
        """段が例外で死んだ cut は壊れ扱い (受け口に届かず死んだ段は cut を落とさず、その時の text を投入の門に任せる)。staged の旗は
        必ず立てる (立たないと後の cut と投入が待ち続ける)。"""
        try:
            await self._stage(i, c)
        except asyncio.CancelledError:
            raise
        except Unreachable as error:
            self.record("stage_unreachable", cut=c, error=str(error)[:300])
        except Exception as error:  # 1 cut の失敗で動画全体を止めない
            self.broken[c] = f"stage crashed: {error!r}"[:200]
            self.record("stage_crashed", cut=c, error=repr(error)[:300])
        finally:
            self.staged[c].set()
            self.record("staged", cut=c, broken=self.broken.get(c), **self.cut_length(c))

    async def _stage(self, i: int, c: str) -> None:
        if not await self.until_cut(c):
            self.broken[c] = "not written"
            return
        self.record("cut_seen", cut=c)
        if c in self.passthrough:
            # 編集の lane の不変 cut — 親で検証・配信済みの block。check も直し役も掛けずに素材だけ温めて即 staged にする。根も
            # 不変なので、最初の live cut なら根の先行投入の待ちもここで解く
            self.author_clean.add(c)
            if c == self.first_live():
                self.root_clear.set()
            self.start_prewarm(c)
            self.record("cut_passthrough", cut=c)
            return
        self.move_forward_defs(c)
        staffed = await self.staff(i, c)
        self.start_prewarm(c)
        fix_calls = 0
        before_fix: str | None = None  # 直し役を掛ける直前の block (直し役が作った DEFECT の行を戻す元)
        settled = False  # 直し役の壊した行を戻した — DEFECT が消えれば残りの指摘で直し役をもう呼ばない
        before_clean = False  # before_fix の版の check が DEFECT 0 だったか (直しが DEFECT を作ったら版ごと戻せる)
        prev_keys: set[tuple[str, str]] | None = None  # 直し役の直前の check の指摘 (規則と層)
        reviews = self.reviews if self.fixer_on else 0
        prev_findings: str | None = None
        # 塊だけ戻した直前の版 — 塊の戻しで design と timeline の名がずれて DEFECT になったら版ごと戻す (dv nt07 shift60)
        partial_base: str | None = None
        reverted_fixes: list[str] = []  # 戻した直し役の出力 — 同じ edit が返ったら当てずに戻す
        failed_edits = ""  # 戻した edit の本文 — 次の直し役に「効かなかった」と添える
        last: tuple[str, list[Lint]] | None = None  # 最後の check の (cut の text, その cut の指摘)
        # 静止画を見た見直しが絵の説明文を変えた (作り直しが warm で裏に走る) — 次の見直しの前に、直す指摘があれば画像を見ない直しを挟む
        pictures_pending = False
        for rnd in itertools.count():
            if rnd >= MAX_ROUNDS:
                self.record("round_cap", cut=c)
                break
            started = time.monotonic()
            res = await self.check_settled(c, i, rnd)
            defects = res.defects
            mine = [f for f in res.findings if f.cut == c]
            last = (self.blocks[c], mine)
            fixes = [f for f in mine if self.fix_finding(f) and not self.root_layer(c, f)]
            if skipped := [f for f in mine if self.fix_finding(f) and self.root_layer(c, f)]:
                self.record("root_layer_skipped", cut=c, round=rnd, layers=sorted({f.layer for f in skipped}))
            self.record(
                "check",
                cut=c,
                round=rnd,
                s=round(time.monotonic() - started, 1),
                defect=len(defects),
                warn=sum(1 for f in mine if f.severity == "warn"),
                severe=sum(1 for f in mine if f.severity == "severe"),
                fix=len(fixes),
                rules=sorted({f.rule for f in fixes})[:8],
                first_defect=defects[0].text[:200] if defects else None,
            )
            clean = not defects and not res.blockers
            if rnd == 0 and clean and not staffed:
                self.author_clean.add(c)
            if clean and c == self.first_live():
                self.root_clear.set()
            if defects and partial_base is not None:
                self.put(c, partial_base)
                partial_base = None
                self.record("fix_reverted", cut=c, round=rnd, n=len(defects), whole=True)
                settled = True
                continue
            partial_base = None
            if not defects and not self.broken.get(c):
                self.start_prewarm(
                    c
                )  # lint の直しが残っていても素材は作り始める (直し役は台詞も絵の説明文も変えない約束)
            if defects and before_fix is not None:
                fixed_text = self.blocks[c]
                reverted = self.revert_fixer_damage(c, before_fix, defects)
                if not reverted and before_clean:
                    # 直す前の版は DEFECT 0 だった — 警告を直しに行って DEFECT を作った (報告の行が変更の塊の外)。直しをまるごと戻す
                    self.put(c, before_fix)
                    reverted = len(defects)
                before_fix = None
                if reverted:
                    reverted_fixes.append(fixed_text)
                    failed_edits = author_core.edit_lines(self.blocks[c], fixed_text)
                    self.record("fix_reverted", cut=c, round=rnd, n=reverted, defect=len(defects))
                    settled = True
                    continue
            if not defects and before_fix is not None and prev_keys is not None:
                # 直しが新しく作った指摘 (直す前の check に無かった規則と層の組・この lane が直す段か severe) — その層を指す行が直し役の
                # 変更の塊にあれば、その塊だけ直す前に戻す。lane が直さない warn (fix_scope=severe の who=fixer の warn) は退行に数えない —
                # 数えると severe を消した直しが戻されて severe が復活する。ただし直しが DEFECT を消した版は戻さない (DEFECT は severe
                # より重い — 戻すと DEFECT が復活して空回りした: 11-02 LOCAL A/B t1 onestop)。新しい指摘は次の round の直し役が見る
                regressed = [
                    f
                    for f in mine
                    if f.severity in ("severe", "warn")
                    and (self.fix_finding(f) or f.severity == "severe")
                    and (f.rule, f.layer) not in prev_keys
                ]
                if regressed and not before_clean:
                    self.record(
                        "fix_regression_kept",
                        cut=c,
                        round=rnd,
                        n=len(regressed),
                        rules=sorted({f.rule for f in regressed}),
                    )
                    regressed = []
                undone = self.revert_new_findings(c, before_fix, regressed) if regressed else 0
                partial_base = before_fix if undone else None
                before_fix = None
                if undone:
                    self.record("fix_regressed", cut=c, round=rnd, n=undone, rules=sorted({f.rule for f in regressed}))
                    settled = True
                    continue
            if not self.fixer_on:
                # 直し役なし: DEFECT は最後の手段だけ・指摘は直さない
                if defects and not await self.rescue_stage(i, c, rnd):
                    self.mark_broken(c, "DEFECT (no fixer)")
                break
            need = bool(defects) or (bool(fixes) and not settled) or reviews > 0
            if not need:
                break
            if fix_calls >= FIX_CALLS:
                # 捨てるのは描けない cut (DEFECT) だけ — 2 回直しても残る severe は受け入れて描く。DEFECT も捨てる前に最後の手段
                if defects and not await self.rescue_stage(i, c, rnd):
                    self.mark_broken(c, "DEFECT after 2 fixes")
                break
            findings = "\n".join(d.text for d in defects[:40])
            # 直し役には直す指摘だけ (他を見せると直しに行き、台帳が author に残した規則まで触る — 11-02 dev e466f4af の spoiler)。
            # 見直しだけは、その cut の severe / warn を全部見せる
            rest = [f for f in mine if f.severity in ("severe", "warn") and f not in fixes] if reviews > 0 else []
            for f in (fixes + rest)[:24]:
                findings += "\n" + f.render()
            # 尺の指摘は見直しに添えるだけ — 尺だけでは呼ばない (2 回目以降の直し役に文を足させると静止が伸びた・10-24)
            if reviews > 0 and (length := self.length_finding(c)):
                findings += "\n" + length
                self.record(
                    "length_lint", cut=c, round=rnd, budget_s=self.cut_budget(c), estimate_s=self.cut_estimate.get(c)
                )
            if failed_edits and defects:
                # 直し役は前の round と同じ edit を返しがち (nt06 gold) — 効かなかった edit を見せる
                findings += (
                    "\n\nThe previous fix's edits did not clear the DEFECT and were reverted (`+` = the line the previous"
                    f" fixer wrote, `-` = the current line). Do not return the same edits — fix it another way:\n{failed_edits}"
                )
            if findings == prev_findings and not defects and not reviews:
                # 直しても指摘が 1 つも変わらない — もう 1 回頼んでも同じ答え。DEFECT が残る時は打ち切らない (cur7_03 climax)
                self.record("fix_stalled", cut=c, round=rnd, fix=len(fixes))
                break
            prev_findings = findings
            started = time.monotonic()
            if fix_calls and defects and c in self.author_clean and self.revert_to_author(c):
                # 直しても DEFECT が残る — 著者の版 (check で DEFECT 0) に差し替えて掛け直す (2 回目の直しの代わり)
                fix_calls += 1
                self.record("revert_author", cut=c, round=rnd, defect=len(defects))
                continue
            interleave = pictures_pending and reviews > 0 and bool(defects or fixes)
            pictures_pending = False
            review = reviews > 0 and not interleave
            if review:
                reviews -= 1
            if interleave:
                self.record("look_interleave", cut=c, round=rnd, defect=len(defects), fix=len(fixes))
            before_fix = self.blocks[c]
            before_clean = not defects
            prev_keys = {(f.rule, f.layer) for f in mine if f.severity in ("severe", "warn")}
            try:
                ok, tail = await self.run_fixer(c, findings, review=review, rnd=rnd)
            except FixerUnavailable as error:
                self.record("fix_failed", cut=c, round=rnd, s=round(time.monotonic() - started, 1), tail=str(error))
                if defects and not await self.rescue_stage(i, c, rnd):
                    self.mark_broken(c, "fix call failed")
                break
            if not review:
                fix_calls += 1
            if ok:
                self.record("fix", cut=c, round=rnd, s=round(time.monotonic() - started, 1), review=review)
                if review and self.stills and author_core.touched_fixed(before_fix, self.blocks[c])[1]:
                    pictures_pending = True
                    self.record("look_pictures", cut=c, round=rnd)
                if self.blocks[c] in reverted_fixes:
                    # 戻した edit をそのまま返した — 当てても同じ DEFECT で戻すだけなので当てない
                    self.put(c, before_fix)
                    before_fix = None
                    self.record("fix_same_edits", cut=c, round=rnd)
            else:
                # 出力が使えなかった (読めない・cut を分けた) — 直しの回数が残っていれば呼び直す (尽きれば次の round で最後の手段)
                self.record("fix_unusable", cut=c, round=rnd, s=round(time.monotonic() - started, 1), tail=tail)
                before_fix = None
        await self.final_autofix(c, i, last)

    async def final_autofix(self, c: str, i: int, last: tuple[str, list[Lint]] | None) -> None:
        """直し役が回り終えた cut c に機械の直し (check の `autofix` — 直し方が一つに決まる指摘・`author_core.apply_autofix`) を 1 回
        当てる (LLM はもう見ない — 直し役の前に当てると、warn を見ない直し役の後で DEFECT を作った直しを戻せない)。台帳が author に残した
        規則は当てない。指摘は最後の check の物 (text がその時のままの時だけ)・当てた後の check に DEFECT が出たら戻す。"""
        if last is None or self.broken.get(c):
            return
        checked, findings = last
        if self.blocks[c] != checked:
            return
        fixable = [f for f in findings if f.autofix and self.who.get(f.rule, "author") != "author"]
        text, applied = author_core.apply_autofix(checked, [(f.rule, f.autofix) for f in fixable])
        if not applied:
            return
        self.put(c, text)
        self.record("autofix", cut=c, n=len(applied), fixes=[fixable[k].autofix for k in applied])
        if (await self.check_settled(c, i, "final")).defects:
            self.put(c, checked)
            self.record("autofix_reverted", cut=c)

    # ---- warm ----
    def start_prewarm(self, c: str) -> None:
        """cut c の素材 (絵・声) を run に先に作らせる (staged を待たずに・直しと並ぶ)。走っている頼み・同じ素材の鍵で通った頼みがあれば
        頼み直さない。"""
        w = self.warms.setdefault(c, Warm())
        if (w.task is not None and not w.task.done()) or c in self.submitted or c not in self.blocks:
            return
        if w.ok and w.key == author_core.asset_key(self.blocks[c]):
            return
        w.task = asyncio.create_task(self._request_warm(c), name=f"draft-warm-{c}")

    async def _request_warm(self, c: str) -> None:
        """text = 根 (まだ流れていなければ) + 構成の順で c までの未投入の live な cut。投入と同じ検査で弾かれた頼み (前の cut が直しの
        途中) は記録だけして、次の契機に頼み直す。"""
        w = self.warms[c]
        w.key = author_core.asset_key(self.blocks[c])
        parts: list[str] = []
        for x in self.order[: self.order.index(c) + 1]:
            if x in self.submitted or self.broken.get(x):
                continue
            blk = self.cut_block(x)
            if blk is not None:
                parts.append(blk[0].rstrip("\n") + "\n" + blk[1].rstrip("\n") + "\n")
        text = ("" if self.root_submitted else self.root_text()) + "".join(parts)
        started = time.monotonic()
        error = await self.warm_text(text)
        w.ok = error is None
        self.record(
            "warm",
            cut=c,
            ok=w.ok,
            s=round(time.monotonic() - started, 1),
            **({"cuts": len(parts)} if error is None else {"error": error[:300]}),
        )

    # ---- 投入 ----
    async def submit_root(self) -> None:
        """根を最初の cut より先に流す (run は cut を待たずに cast の素材の解決を始める)。根は流した時点で凍るので、最初の live な cut の
        check が根ごと DEFECT 0 で通るまで待つ — 根の欠陥 (無い書体の太さ …) は根と cut を合わせた doc でしか出ず、凍った後は誰も
        直せない (参照から作る run で全 cut が落ちた)。最初の cut が staged になるまで通らなければ、根はその cut と一緒に流す (その cut の
        直し役が根も直せる)。投入検査で弾かれた根も最初の cut と一緒に流す。"""
        while not self.root_clear.is_set():
            first = self.first_live()
            await _first_of(
                self.root_clear,
                *([] if self.author_done.is_set() else [self.author_done]),
                *([] if first is None else [self.staged[first]]),
            )
            if self.root_clear.is_set():
                break
            if first is None or self.staged[first].is_set():
                return
            if self.author_done.is_set() and not self.root_seen.is_set():
                return
        self.normalize_root()
        rejected = await self.submit_text(None, self.root_text().strip("\n"), end=False)
        if rejected is None or rejected:
            self.record("root_submit_rejected", first=(rejected or ["流す先が死んだ"])[0][:300])
            return
        self.root_submitted = True
        self.record("root_submitted")

    async def feed(self) -> None:
        """staged の cut を構成の順に流す。投入検査で弾かれたら、落とす前にその cut の直し役を 1 回だけ呼び (別枠 — 投入検査の DEFECT は
        stage の check に出なかった物: 前の cut が後から定義を変えた・流した prefix との食い違い)、それでも弾かれたら最後の手段を掛け、
        通らなければ落とす。最後の cut は end と一緒に。"""
        await self.submit_root()
        for i, c in enumerate(self.order):
            await self.staged[c].wait()
            last = i == len(self.order) - 1
            ready = None if self.broken.get(c) else self.feed_text(c)
            if ready is None:
                self.record("submit_skipped", cut=c, broken=self.broken.get(c))
                continue
            text: str = ready
            started = time.monotonic()
            rejected = await self.submit_text(c, text, end=last)
            if rejected is None:
                self.record("stream_died", cut=c)
                return
            if rejected and self.fixer_on:
                findings = (
                    "投入検査 (流した前の cut + この cut) の DEFECT。前の cut はもう流れていて変えられない — 前の cut の定義の形"
                    " (参考の定義) に合わせてこの cut を直す:\n" + "\n".join(rejected[:40])
                )
                try:
                    ok, tail = await self.run_fixer(c, findings, rnd="intake")
                except FixerUnavailable as error:
                    ok, tail = False, str(error)
                self.record(
                    "fix" if ok else "fix_failed",
                    cut=c,
                    round="intake",
                    s=round(time.monotonic() - started, 1),
                    defect=len(rejected),
                    first=rejected[0][:300],
                    **({} if ok else {"tail": tail}),
                )
                if ok and (fixed := self.feed_text(c)) is not None:
                    text = fixed
                    again = await self.submit_text(c, text, end=last)
                    if again is None:
                        self.record("stream_died", cut=c)
                        return
                    rejected = again
            if rejected:
                latest = rejected

                async def accepted() -> bool:
                    nonlocal text, latest
                    text = self.feed_text(c) or text
                    got = await self.submit_text(c, text, end=last)
                    latest = latest if got is None else got
                    return got == []

                submitted = [x for x in self.order if x in self.submitted]
                if not await self.last_resort(c, [*submitted, c], "intake", accepted):
                    self.mark_broken(c, "rejected: " + latest[0][:160])
                    self.record(
                        "intake_rejected", cut=c, s=round(time.monotonic() - started, 1), reason=latest[0][:300]
                    )
                    continue  # 根を運んでいたなら次の cut が運ぶ
            self.root_submitted = True
            self.submitted.append(c)
            self.record("fed", cut=c, s=round(time.monotonic() - started, 1))
            if last:
                return
        if not self.submitted:
            raise FeedFailed(f"投入できた cut が無い: {self.broken}")
        # 最後の cut が落ちた時の閉じ (`#end` だけ)
        if await self.submit_text(None, "", end=True) != []:
            raise FeedFailed("#end が弾かれた")
        self.record("closed_without_last_cut")

    async def stages(self) -> None:
        """構成の全 cut の段と投入を回す (構成を置いた後)。どこかで落ちたら走っている段と warm を止めて上げる。"""
        self.staged = {c: asyncio.Event() for c in self.order}
        tasks = [asyncio.create_task(self.stage(i, c), name=f"draft-cut-{c}") for i, c in enumerate(self.order)]
        try:
            await self.feed()
            await asyncio.gather(*tasks)
        except BaseException:
            for task in tasks:
                task.cancel()
            raise
        finally:
            for w in self.warms.values():
                if w.task is not None and not w.task.done():
                    w.task.cancel()


async def _first_of(*events: asyncio.Event) -> None:
    """events のどれかが立つまで待つ。"""
    waits = [asyncio.create_task(e.wait()) for e in events]
    try:
        await asyncio.wait(waits, return_when=asyncio.FIRST_COMPLETED)
    finally:
        for task in waits:
            task.cancel()

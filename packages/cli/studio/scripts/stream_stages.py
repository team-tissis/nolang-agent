"""stream の cut の段の client 側 — 著者 (stream_author.py・1 call) が solo/ に落とす cut を、製品と共有の状態機械
(`cut_stages.CutStages` — 正本は libs/ai/llm_prompts/draft_author/cut_stages.py) で check → 担当 → 直し → warm → 確定 → 投入する。

`Run` が持つのは client の I/O だけ: 著者の file の受け (`watch_author`)・check / 改名 / warm / 投入 / 中断 (受け口 `call` — 運ぶ先の
subclass が実装: remote = `stream_run.RemoteRun` (NoLang API の HTTP)・local = repo にだけある dev 入口 `stream_local.py` (手元の
flow 関数))・担当と直し役 (claude の子 process `stream_author.py staff|fix`)・レビューの静止画・記録 (stream/run.jsonl)。block は memory
が正本で、書き換えのたびに solo/cut_<名>.txt (根は root_*.txt) に写す (子 process と後の解析が読む)。cut の段は運ぶ先で分岐しない。
担当 (`--staff`) は client だけの役: 著者の版を check して直し方の決まる指摘 (台帳の sure) を機械で当て、担当に仕上げさせてから段に戻す。
"""

from __future__ import annotations

import asyncio
import contextlib
import json
import os
import shutil
import subprocess
import sys
import threading
import time
from abc import ABC, abstractmethod
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from stream_api import Defect, Rejected
from stream_author import REFERENCE_SYNC_FILE, author_core, cut_stages, restore_pictures, restore_speech

HERE = Path(__file__).resolve().parent
PY = sys.executable  # この script を動かしている python (repo は /opt/venv・plugin の client は使う側の python3)
AUTHOR = HERE / "stream_author.py"
# 直し役・レビューの 1 回の待ちの上限 — server は投入の行が 180 秒届かないと run を落とすので、その内側で諦めて直す前の版で続ける
FIX_TIMEOUT_S = 120


def cut_timing(check_out: str, cut: str) -> str:
    """check の出力から担当に渡す時刻の行を取る: 動画全体の `cut times` と、cut の `scene lengths` と `showing times` の行 (見出しを頭に付ける)。"""
    keep: list[str] = []
    header = ""
    for line in check_out.splitlines():
        if line.startswith("  cut times"):
            keep.append(line.strip())
        elif line.startswith("  ") and not line.startswith("    "):
            header = line.strip().split(" (", 1)[0].rstrip(":")
        elif line.startswith(f"    {cut}:") and header in ("scene lengths", "showing times"):
            keep.append(f"{header} — {line.strip()}")
    return "\n".join(keep)


@dataclass(frozen=True)
class RunOptions:
    """run の役の強さ (CLI の flag と同じ名 — `stream_run.main` が読む)。"""

    staff: str | None = None  # 担当の effort (`balanced` は cut ごとに決める)。None = 担当なし
    staff_warn: bool = False
    fix: str | None = "low"  # 直し役の effort (low 固定)。None = 直し役なし
    review: str | None = None
    fix_scope: str = "severe"
    stills: bool = True
    keep_assets: bool = True
    brief: bool = False
    editable: bool = False
    edit: bool = False


class Run(cut_stages.CutStages, ABC):
    def __init__(self, project: Path, options: RunOptions) -> None:
        super().__init__()
        self.project = project
        self.solo, self.st, self.studio = project / "solo", project / "stream", project / "studio"
        self.weave = project / "weave"
        self.weave.mkdir(parents=True, exist_ok=True)
        # 編集の run (`stream_make.sh --edit`): 著者は走らず、編集役 (stream_author.py edit) が置いた src を運ぶ。不変の cut は素通しで
        # 投入し (前の run で検証済み)、変わった cut だけ check → 直し、新しい cut だけ担当を通す
        self.edit = options.edit
        self.edit_new: frozenset[str] = frozenset()
        if options.edit:
            meta = json.loads((project / "edit/cuts.json").read_text())
            self.passthrough = {str(c) for c in meta.get("unchanged", [])}
            self.edit_new = frozenset(str(c) for c in meta.get("new", []))
        # 編集可能モード: start に editable を立て、check に profile=editable を渡す (投入の門は server が video の create_setting から
        # 読む)。著者・担当・直しの prompt の節は env NOLANG_STUDIO_PROFILE (stream_make.sh が立てる)
        self.editable = options.editable
        self.rules_payload: dict[str, object] | None = None  # 照合の時に受けた `drafts/rules/` (run の頭もこれを使う)
        self.video_id: str | None = None  # run の video (start で決まる)
        self.staff_effort = options.staff  # 担当 (cut を仕上げる) の effort。None = 担当なし
        self.staff_warn = options.staff_warn  # 担当に warn の指摘も渡す (`--staff-warn`・既定は DEFECT と severe だけ)
        self.fix_effort = (
            options.fix
        )  # 直し役の effort (low 固定)。None = 直し役なし (レビューもその機構を使うので無し)
        self.fixer_on = options.fix is not None
        self.fix_scope = options.fix_scope
        # レビュー (担当の後に 1 回・指摘に出ない弱い所・崩れも探して自分で直す call) の effort。None = なし。`--fix` の段とは独立
        self.review_effort = options.review if options.fix is not None else None
        self.reviews = author_core.REVIEW_ROUNDS if self.review_effort is not None else 0
        # レビューが cut の静止画 (絵の warm を待って描く) を見るか。False = doc と全指摘だけ (`--no-stills`)
        self.stills = options.stills and self.review_effort is not None
        # 著者 brief (`--author-brief`): 著者は台詞と絵コンテだけ書き、絵は担当が設計する — 担当は常に素材も変える (keep_assets と
        # 両立しない)。台詞だけは著者の版のまま固定し、声は著者の時点から担当と並列に作る
        self.brief = options.brief
        # 担当は絵と台詞を変えない — 絵と声は著者の版から担当と並列に作る (`staff` が担当の前に warm を頼む)
        self.keep_assets = options.keep_assets and not options.brief
        params = (project / "params.txt").read_text().split() if (project / "params.txt").exists() else []
        with contextlib.suppress(IndexError, ValueError):
            self.seconds = float(params[2])
        request = project / "request.txt"
        self.request = request.read_text() if request.exists() else ""
        self.env = dict(os.environ)  # 役 (著者・担当・直し役) の子 process の env (運ぶ先の subclass が足す)
        self.staff_trim: set[str] = set()  # 尺の指摘 (`cut_length`) を渡した担当の cut — 文を丸ごと消したのは戻さない
        self.shot_unwarmed: dict[str, list[str]] = {}  # cut → 静止画で warm が間に合わず仮の絵で描いた参照 (レビュー)
        self.t0 = time.time()
        # 止まらない開始の予測 (`staff_effort_for` の balanced) が読む進行の実測 — 値は全部 since 秒 (t0 からの経過)
        self.cut_seen_s: dict[str, float] = {}
        self.staff_begin_s: dict[str, float] = {}
        self.staff_end_s: dict[str, float] = {}
        self.staff_chosen: dict[str, str] = {}  # cut → 担当に渡した effort
        self.staged_s: dict[str, float] = {}
        self.fed_s: dict[str, float] = {}
        self._manifest_s: float | None = None  # 再生開始 (manifest 公開) の実測の cache

    # ---- 記録 ----
    def since(self) -> float:
        """起動からの経過秒 (run.jsonl の `since` と同じ時間軸)。"""
        return time.time() - self.t0

    def log(self, **kw: object) -> None:
        kw["t"] = time.time()
        kw["since"] = round(float(kw["t"]) - self.t0, 1)
        with (self.st / "run.jsonl").open("a") as f:
            f.write(json.dumps(kw, ensure_ascii=False) + "\n")
        print(json.dumps(kw, ensure_ascii=False), flush=True)

    _PACE = {"cut_seen": "cut_seen_s", "staged": "staged_s", "fed": "fed_s"}  # 担当の effort の予測が読む段の時刻

    def record(self, step: str, **fields: object) -> None:
        if step in self._PACE and isinstance(fields.get("cut"), str):
            getattr(self, self._PACE[step])[fields["cut"]] = self.since()
        self.log(event=step, **fields)

    # ---- 受け口 (運ぶ先の subclass) ----
    @abstractmethod
    def call(self, op: str, body: dict[str, object] | None = None, **path_args: str) -> dict[str, object]:
        """受け口 (nolang-api `drafts/` の flow 関数) を 1 回呼ぶ。止めた頼みは `stream_api.Rejected`・届かない時は
        `stream_api.Unreachable`・その他の失敗は RuntimeError (答えの読みは `stream_api.read_answer`)。"""

    @abstractmethod
    def sync_reference(self) -> None:
        """起動直後に著者と並走して、文書一式の版を照合して `write_sync` で書く (著者は claude を起こす直前に結果を読む)。"""

    @abstractmethod
    def start(self) -> None:
        """run を開く (plan が閉じた時点)。video の id を `video_id` に置く (開けなければ None のまま)。"""

    @abstractmethod
    def wait(self) -> int:
        """投入を終えた run の完成を待つ (完成なら `write_back` して 0)。"""

    @abstractmethod
    def fetch_reference(self, video_id: str) -> int:
        """参照の動画 (`--ref` / 依頼の `[video:id]`) の src と「ユーザーが選んだ形」の節を project/reference.json に書く (著者が
        読む)。節の文は server が組む (正本 `reference_brief.py`)。取れなければ参照なしで続ける (戻り 1)。"""

    @abstractmethod
    def fetch_speech(self, speech_ids: str) -> int:
        """持ち込み音声 (`--speech <id>[,<id>]`) の clip 台帳と著者に貼る節を project/speech.json に書く。取れなければ止める (戻り 1)。"""

    @abstractmethod
    def render_shots(self, c: str, dd: Path, t: float) -> list[Path]:
        """doc dd (根 + c) の cut c の静止画を描いて置き場の path を返す (描けなければ空)。仮の絵で描いた参照は `shot_unwarmed` に。"""

    def shot_pins(self, c: str) -> dict[str, object] | None:
        """静止画の doc に載せる warm の絵の pin (None = 受け口が warm の絵を待って使う)。"""
        return None

    def stream_alive(self) -> bool:
        return not self.engine_failed()

    def close(self) -> None:
        """中断で止まる時に、運ぶ先が持つ process を畳む。"""

    # ---- 著者の file (memory の block を file にも写す) ----
    def put(self, c: str, text: str) -> None:
        super().put(c, text)
        (self.solo / f"cut_{c}.txt").write_text(text)

    def put_root(self, design: str, timeline: str) -> None:
        super().put_root(design, timeline)
        (self.solo / "root_design.txt").write_text(design)
        (self.solo / "root_timeline.txt").write_text(timeline)

    async def watch_author(self) -> None:
        """著者 (別 process) が solo/ に置く根と cut を受ける (0.3 s ごと・file は置き換えで書かれる)。著者の終わりの印 src.done
        (`stream_author.mark_done`) で終わる — 途中で終わった著者 (`=== end ===` が無い・call の exit が 0 でない) は届かなかった
        cut を `author_incomplete` に記録する (段は書かれなかったで落として続ける)。著者の版は solo/author_cut_<名>.txt にも残す。"""
        while True:
            done = (self.st / "src.done").exists()  # 先に見る — done の前に置かれた file は下で必ず受ける
            rd, rt = self.solo / "root_design.txt", self.solo / "root_timeline.txt"
            if not self.root_seen.is_set() and rd.exists() and rt.exists():
                super().put_root(rd.read_text(), rt.read_text())
                self.root_seen.set()
            if self.root_seen.is_set():
                for c in self.order:
                    f = self.solo / f"cut_{c}.txt"
                    if c not in self.blocks and f.exists():
                        self.receive_cut(c, f.read_text())
                        keep = self.solo / f"author_cut_{c}.txt"
                        if not keep.exists():
                            keep.write_text(self.blocks[c])
            if done:
                ending = json.loads((self.st / "src.done").read_text())
                if not ending["ended"] or ending["exit"] != 0:
                    missing = [c for c in self.order if c not in self.blocks]
                    self.log(event="author_incomplete", ended=ending["ended"], exit=ending["exit"], missing=missing)
                self.author_done.set()
                return
            await asyncio.sleep(0.3)

    def write_defs_before(self, c: str) -> None:
        (self.solo / f"defs_before_{c}.txt").write_text(self.defs_before(c))

    # ---- doc (静止画) ----
    def doc_src(self, pins: dict[str, object] | None = None) -> dict:
        """doc の src.json = studio/src.json (設定と著者の pin) + pins (run が解いた素材 — レビューの静止画・書き戻し)。"""
        base = self.studio / "src.json"
        d = json.loads(base.read_text()) if base.exists() else {"asset_pins": {}}
        d.setdefault("asset_pins", {}).update(pins or {})
        return d

    def doc_dir(
        self, name: str, cuts: list[str], *, root_extra: str = "", pins: dict[str, object] | None = None
    ) -> Path:
        """doc (根 + cuts) を weave/<name>/ に組む (レビューの静止画)。pins = doc の src.json に足す素材の pin。"""
        dd = self.weave / name
        (dd / "out").mkdir(parents=True, exist_ok=True)
        design, timeline = self.doc(cuts, root_extra=root_extra)
        (dd / "design.txt").write_text(design)
        (dd / "timeline.txt").write_text(timeline)
        marker = dd / "OPEN_ENDED"  # 後に cut が続く prefix → check と描画は最後の cut だけの規則を掛けない
        if not cuts or cuts[-1] != self.order[-1]:
            marker.touch()
        else:
            marker.unlink(missing_ok=True)
        tmp = dd / f".src.json.{threading.get_ident()}"
        tmp.write_text(json.dumps(self.doc_src(pins), ensure_ascii=False, indent=1))
        os.replace(tmp, dd / "src.json")
        # 書体の実体 (TTF) は project で 1 つの cache (studio/out/fonts) を全部の doc が symlink で共有する
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

    async def shots(self, c: str) -> list[Path]:
        """レビュー役に見せる cut c の静止画。run の warm が解いた絵を待ち、根 + c の doc (前の cut の名のある定義は根の後ろ) を描く。
        前の cut を入れないのは、その cut の直し中の DEFECT で build できず、前の cut の声がまだ無ければ TTS を待つから。"""
        w = self.warms.get(c)
        if w is not None and w.task is not None:
            await asyncio.wait([w.task])
        t = time.time()
        pins = await asyncio.to_thread(self.shot_pins, c)
        i = self.order.index(c)
        extra = "".join(
            text
            for x in self.order[:i]
            if not self.broken.get(x) and (blk := self.cut_block(x)) is not None
            for _kind, _name, text in author_core.named_defs(blk[0])
        )
        dd = self.doc_dir(f"{c}.shot", [c], root_extra=extra, pins=pins)
        return await asyncio.to_thread(self.render_shots, c, dd, t)

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

    @staticmethod
    def drop_defect_lines(dd: Path, c: str) -> list[dict[str, object]]:
        """doc (dd) の out/defects.json のうち cut c の block の行を指す DEFECT を doc の file から外す → 落とした物の記録 (空 = 何も
        落とさない・`author_core.drop_defect_lines`)。"""
        defects = Run.read_defects(dd)
        if not defects:
            return []
        design, timeline, dropped = author_core.drop_defect_lines(
            (dd / "design.txt").read_text(), (dd / "timeline.txt").read_text(), c, defects
        )
        if dropped:
            (dd / "design.txt").write_text(design)
            (dd / "timeline.txt").write_text(timeline)
        return dropped

    # ---- check と改名 ----
    @property
    def aspect(self) -> str:
        """依頼の縦横比 (params.txt の 2 つ目・`16:9` / `9:16`) — 根の canvas がこれと違えば check と投入検査が止める。"""
        return (self.project / "params.txt").read_text().split()[1]

    def check_texts(
        self, design: str, timeline: str, *, ended: bool, focus: str | None = None
    ) -> tuple[str, list[Defect], list[dict[str, object]]]:
        """製品の check (`drafts/check/` — compile・composer と layout の乾いた実行・lint の全規則・cut の時刻。書体は本番と同じ・run の
        warm で解けた絵は実画像で判定) を 1 回 → (check の表, DEFECT, 指摘)。ended = 動画の終わりまで書いた doc・focus = 指摘を要る cut
        (server が lint をその cut に絞る)。測った cut の時刻を見込み秒に、focus の cut のまだ解けていない絵を `unwarmed` に写す。"""
        body = self.call(
            "check",
            {
                "design": design,
                "timeline": timeline,
                "open_ended": not ended,
                **({"lint_cut": focus} if focus else {}),
                "aspect_ratio": self.aspect,
                # 開始済みの run — warm で解けた絵 (測った主体と実画像) で読めない文字・主体に乗った文字も見る
                **({"video_id": self.video_id} if self.video_id else {}),
                # 編集可能モードの run — 違反は DEFECT (投入の門と同じ答え)
                **({"profile": "editable"} if self.editable else {}),
                # 持ち込み音声 — clip 台帳で `@clip` の話者と `[trim:]` を解く (開始済みの run は server が run の音声を使う)
                **({"speech_file_ids": self.speech_file_ids()} if self.speech_file_ids() else {}),
            },
        )
        defects = [Defect.read(d) for d in body.get("defects", []) if isinstance(d, dict)]
        for row in body.get("cuts") or []:
            if isinstance(row, dict) and isinstance(row.get("cut"), str):
                self.cut_estimate[row["cut"]] = (
                    max(float(row.get("end_ms", 0)) - float(row.get("start_ms", 0)), 0.0) / 1000
                )
        if focus:
            self.unwarmed[focus] = [str(name) for name in body.get("unwarmed") or []]
        lint = [f for f in body.get("findings", []) if isinstance(f, dict)]
        return str(body.get("report") or "\n".join(d.text for d in defects)), defects, lint

    def check(self, dd: Path, *, ended: bool, focus: str | None = None) -> tuple[str, list[Defect], list[dict]]:
        """doc の dir (静止画) を check して DEFECT を out/defects.json に書く (`drop_defect_lines` が読む)。"""
        out, defects, lint = self.check_texts(
            (dd / "design.txt").read_text(), (dd / "timeline.txt").read_text(), ended=ended, focus=focus
        )
        path = dd / "out/defects.json"
        if defects:
            path.write_text(json.dumps([d.__dict__ for d in defects], ensure_ascii=False))
        else:
            path.unlink(missing_ok=True)
        return out, defects, lint

    async def check_doc(
        self, design: str, timeline: str, *, ended: bool, focus: str | None = None
    ) -> cut_stages.Checked:
        report, defects, lint = await asyncio.to_thread(self.check_texts, design, timeline, ended=ended, focus=focus)
        return cut_stages.Checked(defects=defects, findings=[cut_stages.Lint.read(f) for f in lint], report=report)

    def rename_text(self, text: str, renames: Mapping[str, str]) -> str:
        """cut の text の中の層の名を改名する (参照も文法どおりに・製品の文法 `drafts/rename/`)。"""
        return str(self.call("rename", {"text": text, "renames": dict(renames)})["text"])

    # ---- 役の子 process ----
    def call_role(self, args: list[str], *, timeout: int) -> subprocess.CompletedProcess[str]:
        """役 (担当・直し役) の子 process。失敗は呼び手の段が前の版で続ける (止めると動画ごと落ちる — engine に依らない)。"""
        return subprocess.run(args, cwd=HERE.parent, env=self.env, capture_output=True, text=True, timeout=timeout)

    def _fix_process(self, c: str, ff: Path, *, own_root: bool, review: bool, shots: list[Path] | None) -> str:
        """直し役 (claude -p) を 1 回 → stdout (直した block)。根の持ち主の cut なら根の 2 file も直す (`--root`)。返らない・process が
        落ちた時は FixerUnavailable。"""
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
                        *(["--root"] if own_root else []),
                        "--effort",
                        (self.review_effort or self.fix_effort or "low") if review else (self.fix_effort or "low"),
                        *(["--review"] if review else []),
                        *(["--shots", ",".join(str(x) for x in shots)] if shots else []),
                    ],
                    timeout=FIX_TIMEOUT_S,
                )
            except subprocess.TimeoutExpired:
                # 直し役が返らない (codex の turn が止まる等) — 待ち続けると後の cut の投入が止まり、server の待ちの上限 (180 秒) で
                # 動画ごと落ちる。直す前の版で続ける
                self.log(cut=c, event="fix_timeout", s=FIX_TIMEOUT_S, review=review)
                raise cut_stages.FixerUnavailable(f"timeout {FIX_TIMEOUT_S}s") from None
            if (
                os.environ.get("NOLANG_STUDIO_ENGINE") != "codex"
                and r.returncode != 0
                and "FileNotFoundError" in r.stderr
                and attempt == 0
            ):
                time.sleep(2)  # claude の shim が一瞬見つからない事がある → 1 回だけやり直す
                continue
            break
        if r.returncode != 0:
            raise cut_stages.FixerUnavailable((r.stdout + r.stderr)[-200:])
        return r.stdout

    async def call_fixer(
        self, c: str, block: str, findings: str, *, review: bool, own_root: bool, rnd: int | str
    ) -> cut_stages.FixReply:
        """直し役の子 process に cut の file (`put` が今の block を写している)・指摘の file・前の cut の定義を渡す。レビューは静止画も
        見せる。根の持ち主が直した根は file から読んで返し (受けるかは段が決める)、file は今の根に戻す。"""
        del block
        dd = self.weave / c / "out"
        dd.mkdir(parents=True, exist_ok=True)
        ff = dd / f"findings_{rnd}.txt"
        shots = await self.shots(c) if review and self.stills else None  # 撮れなければ (空) 画像なしでレビュー
        if shots and self.shot_unwarmed.get(c):
            # warm が間に合わず意味検索で引いた仮の絵 — レビュー役に中身を判定させない (作り直しの連鎖を作らない)
            findings += "\n\nstill generating (placeholder pictures — do not judge their content): " + "・".join(
                self.shot_unwarmed[c]
            )
        ff.write_text(findings)
        self.write_defs_before(c)
        root = (self.root_design or "", self.root_timeline or "")
        out = await asyncio.to_thread(self._fix_process, c, ff, own_root=own_root, review=review, shots=shots)
        if shots:
            self.log(cut=c, event="look", round=rnd, n=len(shots))
        fixed_root = ((self.solo / "root_design.txt").read_text(), (self.solo / "root_timeline.txt").read_text())
        if fixed_root != root:  # file は memory の根に戻す (直した根を受けるかは段が決める)
            self.put_root(self.root_design or "", self.root_timeline or "")
        return cut_stages.FixReply(
            block=out if "---timeline---" in out else None,
            tail=out[-200:],
            root_design=fixed_root[0] if fixed_root[0] != root[0] else None,
            root_timeline=fixed_root[1] if fixed_root[1] != root[1] else None,
        )

    # ---- 担当 ----
    async def staff(self, i: int, c: str) -> bool:
        """担当 (Opus) が著者の cut を仕上げる。前の cut は著者の版を渡すので cut ごとに並列に走る。担当は台詞も直してよい (声は担当の
        版から作る)。逐語の台本の動画だけ、担当が台詞の文字を変えていたら著者の版の文字に戻す (`restore_speech`)。keep_assets の run は
        台詞を読点・行の割り方まで、絵を説明文まで著者の版に戻す (`restore_pictures` — 素材は著者の版から先に作っている)。"""
        if not self.staff_effort or (self.edit and c not in self.edit_new):
            return False
        # 著者版の check は担当の前に回し、指摘を担当に渡す。直し方が一つに決まる指摘は機械で直してから (著者の版 = 直した版)
        ff = await self.author_check(i, c)
        if self.keep_assets or self.brief:
            # 担当は絵と台詞を変えない — 著者の版のまま素材を頼み、担当と並列に作る (brief は台詞だけ固定)
            self.start_prewarm(c)
        self.write_defs_before(c)
        before = self.blocks[c]  # 担当の前の block (著者の版 + 前方から移した定義) — 担当が消した定義を戻す基準
        t = time.time()
        effort = self.staff_effort_for(i, c)
        self.staff_chosen[c] = effort
        self.staff_begin_s[c] = self.since()
        r = await asyncio.to_thread(
            self.call_role,
            [
                PY,
                str(AUTHOR),
                "staff",
                str(self.project),
                c,
                str(ff),
                "--effort",
                effort,
                *(["--keep-assets"] if self.keep_assets else []),
                *(["--author-brief"] if self.brief else []),
            ],
            timeout=900,
        )
        self.staff_end_s[c] = self.since()
        if r.returncode != 0 or "---timeline---" not in r.stdout:
            self.log(cut=c, event="staff_failed", s=round(time.time() - t, 1), tail=(r.stdout + r.stderr)[-200:])
            return True
        author = self.author_blocks[c]
        text, restored = (
            restore_speech(author, r.stdout, exact=self.keep_assets or self.brief, drop=c in self.staff_trim)
            if self.verbatim or self.keep_assets or self.brief
            else (r.stdout, [])
        )
        pictures: list[dict[str, str]] = []
        if self.keep_assets:
            text, pictures = restore_pictures(author, text, root=self.root_design or "")
        (self.solo / f"staff_cut_{c}.txt").write_text(
            text
        )  # 担当の版を分けて残す (cut_<名>.txt は直し役が上書きする最終の版)
        # 戻す基準は書き戻す直前の block — 担当の裏で前方から移された定義 (move_forward_defs) も含める
        latest = self.blocks[c]
        self.put(c, text)
        self.log(cut=c, event="staff", s=round(time.time() - t, 1), chars=len(r.stdout))
        if restored:
            self.log(cut=c, event="speech_restored", n=len(restored), lines=restored)
        if pictures:
            self.log(cut=c, event="pictures_restored", n=len(pictures), pictures=pictures)
        self.restore_defs(c, latest if "---timeline---" in latest else before, keep_looks=True)
        return True

    async def author_check(self, i: int, c: str) -> Path:
        """著者の版 (担当が触る前) を check し、DEFECT 0 なら author_clean に (差し戻しの元)。直し方の決まる指摘 (台帳の sure) を機械で
        当て、その版を著者の版として残す。指摘の file を返す (担当へ)。"""
        t = time.time()
        cuts = self.live_cuts(self.order[: i + 1])
        outside = self.outside_window(c, cuts)
        res = await (self.check_without(c, cuts, outside, "author") if outside else self.check_cut(c, cuts, "author"))
        clean = not res.defects and not res.blockers  # 止まった check では c の実行の DEFECT が見えない
        defects, lint, report = res.defects, res.findings, res.report
        last = res
        if skip := frozenset(res.blockers - {"?", cut_stages.ROOT}):
            # 前の cut (著者の版) の DEFECT で check が止まり lint も c の DEFECT も出ない — その cut も除いた doc で c の DEFECT と
            # lint を取る (取った DEFECT を担当に渡さず、同じ書き損じの cut ごとに直し役が 1 巡ずつ直していた — 11-05 FPN2 G2-4)
            last = await self.check_without(c, cuts, skip | outside, "author")
            clean = not res.defects and not last.defects and not last.blockers
            defects, lint, report = [*res.defects, *last.defects], last.findings, last.report
        # 根の行か持ち主の分からない DEFECT で止まった check は除いて取り直せない — c の行が起こしているかは分からないが、担当に見せる
        # (見せないと担当は直せず、根の def の書き損じを使う cut ごとに直し役が 1 巡ずつ直した — 11-05 FPN G2-4 の `pointer: below`)
        defects = [*defects, *last.unowned]
        if clean:
            self.author_clean.add(c)
        mine = [f for f in lint if f.cut == c]
        # 台帳が author に残した規則 (who=author) は機械でも当てない — 担当に見せるだけ
        fixable = [f for f in mine if f.autofix and self.who.get(f.rule, "author") != "author"]
        text, applied = author_core.apply_autofix(
            self.blocks[c], [(f.rule, f.autofix) for f in fixable], sure_only=True, sure_rules=self.sure
        )
        fixed = [fixable[k] for k in applied]
        if applied:
            self.put(c, text)
            self.log(cut=c, event="autofix", round="author", n=len(applied), fixes=[f.autofix for f in fixed])
            # 著者の版 = 機械で直した版 — 見込みにも足した無音の秒を足す (尺の指摘はこの版の見込みで決める・足さないと cut ごとに
            # 平均 0.25 s 短く読む — 11-05 1a)
            if c in self.cut_estimate:
                self.cut_estimate[c] += sum(
                    float(arg)
                    for op, _, arg in (f.autofix.partition(":") for f in fixed)
                    if op in ("silence_head", "silence_tail")
                )
        self.author_blocks[c] = self.blocks[c]
        (self.solo / f"author_cut_{c}.txt").write_text(self.blocks[c])
        # 担当には既定で DEFECT と severe だけ (warn は渡さない — 思考の裾が減り担当 max 241 → 124 s・10-26 の 2 bench)
        levels = ("severe", "warn") if self.staff_warn else ("severe",)
        staffed = [f for f in mine if f not in fixed and f.severity in levels]
        findings = "\n".join(d.text for d in defects[:20])
        if last.unowned:
            findings += (
                "\n(The check stopped at the DEFECT above, outside this block (the root or an earlier cut), so it shows no other"
                " findings for this cut. If this cut's lines trigger it, avoid it in this block.)"
            )
        findings += "".join("\n" + f.render() for f in staffed[:30])
        if c in self.cut_estimate:
            self.log(
                cut=c,
                event="plan_estimate",
                plan_s=self.plan_seconds().get(c),
                estimate_s=round(self.cut_estimate[c], 1),
            )
        # 著者版の見込みが予算と全体の許容を超えた cut は尺の指摘も渡す (担当は文を丸ごと消してよい — `staff` が戻さない)
        if length := self.staff_length_finding(c):
            self.staff_trim.add(c)
            findings += "\n" + length
        dd = self.weave / c / "out"
        dd.mkdir(parents=True, exist_ok=True)
        ff = dd / "findings_author.txt"
        ff.write_text(findings)
        (dd / "timing_author.txt").write_text(cut_timing(report, c))  # 担当が読む (stream_author の staff・指摘の隣)
        self.log(cut=c, event="check", round="author", s=round(time.time() - t, 1), defect=len(defects), warn=len(mine))
        return ff

    # 止まらない開始の予測の定数 (10-27〜28 の local 実測 30 run: 担当 low 7〜27 s (中央 15) / medium 21〜73 s (中央 37・
    # p80 44.5)・check+直し 中央 0.9 s・最初の fed → manifest 公開 約 2.5 s)。見積りは非対称に取る: 自分の完了 (作業側) は
    # 遅め (SLOW)・見る人の到達 (締切側) は早め (FAST × OFFSET_DISCOUNT) — どちらの外れも「medium を選んで止まる」でなく
    # 「low に落として質が少し下がる」側に倒れる。張りは 30 run の骨格のモンテカルロ (実測 6 停止/30 に較正) の frontier から
    # ユーザー裁定 (10-28) で「止まらない予測 94%・medium ~5 割」の点 = 作業側 medium の p80・締切側 p30。平均 9.4/10 だが
    # 10 本の周で 8/10 も 2 割ほど出る張り (単発の長尻 — 82 s を実測 — は締切ギリギリの判断の 2 割が踏む)。
    # ほぼ確実に 9 割を守るなら作業側 50.0 (p90・medium ~3 割・実走 9/10)、確実に止めないなら 55.0 (実走 10/10・medium ~4%)。
    # 11-05: 作業側 medium を 44.5 → 50.0 に (remote の実測 11 本の medium は 21〜89 s・p80 ≈ 58 s。warm が header より前に
    # 走って再生開始が 50 s 早まり、後半 cut の担当 medium 54〜64 s が間に合わず 14 s 止まった r7b)
    STAFF_SLOW_S: dict[str, float] = {"low": 20.0, "medium": 50.0}
    STAFF_FAST_S: dict[str, float] = {"low": 10.0, "medium": 31.0}
    # 著者 brief の run (plus) の担当は絵をゼロから設計し素材も頼むので所要が長い。11-05 の remote 実測 (plus 2 本・300 / 600 s・
    # 担当 low 4 本 32〜51 s・medium 25 本 58〜196 s・中央 147) の p80 (SLOW) と p30 (FAST)。10-28 の bench 由来の旧表 (medium
    # 64 s) は実測の 1/2〜1/3 で、締切を緩く読み medium を選び続けて止まった (miso: 担当 185 s・35 s の停止)
    STAFF_SLOW_S_BRIEF: dict[str, float] = {"low": 50.0, "medium": 175.0}
    STAFF_FAST_S_BRIEF: dict[str, float] = {"low": 40.0, "medium": 120.0}
    STAFF_MEASURED_MIN = 2  # この run で終わった担当が effort ごとにこれだけあれば、作業側の見込みに実測の中央値も使う
    STAGE_TAIL_S = 3.0  # 担当の後の check + 直しの見込み
    AUTHOR_CHECK_S = 5.0  # cut_seen から担当開始まで (著者版の check)
    RENDER_HEAD_S = 10.0  # fed からその cut の segment が再生に届くまで
    MANIFEST_LAG_S = 3.0  # 最初の fed から manifest 公開 (再生開始) まで
    NONSTOP_MARGIN_S = 2.0  # 見込みの揺れの余白
    OFFSET_DISCOUNT = 0.95  # 見込み秒の和の締切側の割引 (見込みより短い動画に早く着く)

    def _staff_s(self, effort: str, *, fast: bool) -> float:
        """担当 1 本の見込み秒。作業側 (slow) は表と、この run で終わった同じ effort の担当の実測の中央値の遅い方 — 題材や
        負荷で表より遅い run は実測が締切の読みを締める (速い run は表のまま = 張りは変えない)。締切側 (fast) は表のまま。"""
        if self.brief:
            table = self.STAFF_FAST_S_BRIEF if fast else self.STAFF_SLOW_S_BRIEF
        else:
            table = self.STAFF_FAST_S if fast else self.STAFF_SLOW_S
        est = table.get(effort, table["medium"])
        if fast:
            return est
        measured = sorted(
            self.staff_end_s[c] - self.staff_begin_s[c]
            for c in self.staff_end_s
            if self.staff_chosen.get(c) == effort and c in self.staff_begin_s
        )
        if len(measured) >= self.STAFF_MEASURED_MIN:
            return max(est, measured[len(measured) // 2])
        return est

    def _ready_est(self, c: str, now: float, *, fast: bool) -> float:
        """cut c が staged になる見込み (since 秒) — 実測があれば実測・走行中は担当の effort の見込みで先へ。"""
        if c in self.staged_s:
            return self.staged_s[c]
        if c in self.staff_end_s:
            return self.staff_end_s[c] + self.STAGE_TAIL_S
        effort_s = self._staff_s(self.staff_chosen.get(c, "medium"), fast=fast)
        if c in self.staff_begin_s:
            return max(self.staff_begin_s[c] + effort_s, now) + self.STAGE_TAIL_S
        return max(self.cut_seen_s.get(c, now) + self.AUTHOR_CHECK_S + effort_s, now) + self.STAGE_TAIL_S

    def _fed_est(self, i: int, candidate: str, now: float) -> float:
        """cut i (担当を candidate で回す場合) が投入 (fed) される見込み (遅め) — 投入は構成の順なので前の cut の遅い方を引き継ぐ。"""
        fed = 0.0
        for j, c in enumerate(self.order[: i + 1]):
            if self.broken.get(c):
                continue
            if c in self.fed_s:
                fed = max(fed, self.fed_s[c])
            elif j == i:
                fed = max(fed, now + self._staff_s(candidate, fast=False) + self.STAGE_TAIL_S)
            else:
                fed = max(fed, self._ready_est(c, now, fast=False))
        return fed

    def manifest_since(self) -> float | None:
        """再生開始 (manifest 公開) の実測 (since 秒)。local は studio_stream が run.jsonl に `manifest_published` を書く —
        remote の run では実測が無く、予測 (最初の fed + MANIFEST_LAG_S) に落ちる。"""
        if self._manifest_s is None:
            with contextlib.suppress(OSError, ValueError):
                for line in (self.st / "run.jsonl").read_text().splitlines():
                    e = json.loads(line)
                    if e.get("event") == "manifest_published":
                        self._manifest_s = float(e["since"])
                        break
        return self._manifest_s

    def _viewer_at(self, i: int, now: float) -> float:
        """見る人が cut i の頭に着く見込み (since 秒・早め) = 再生開始 (実測 → 最初の fed + lag → 早めの予測) +
        前の cut の見込み秒の和 × 割引。"""
        manifest = self.manifest_since()
        if manifest is None:
            first = next((c for c in self.order if not self.broken.get(c)), None)
            fed0 = self.fed_s.get(first) if first is not None else None
            if fed0 is None:
                fed0 = self._ready_est(first, now, fast=True) if first is not None else now
            manifest = fed0 + self.MANIFEST_LAG_S
        est = self.estimated_seconds()
        offset = sum(est.get(c, 10.0) for c in self.order[:i] if not self.broken.get(c))
        return manifest + offset * self.OFFSET_DISCOUNT

    def staff_effort_for(self, i: int, c: str) -> str:
        """cut i の担当の effort。`balanced` = cut 1・2 は low (再生開始の臨界路・2 題材群 16 本で止まらない開始 中央 117〜144 →
        84〜95 s・質は小さく落ちる・10-27)・cut 0 は medium (再生の頭まで余裕がある)・cut 3 以降は **medium の見込み完了が
        「見る人がその cut に着く時刻」に間に合う時だけ medium** — 間に合わない見込みなら low に落とす (止まらない 9 割の裁定・
        10-27。全 cut medium は止まらない 6/10 で、止まりは全部後半 cut の担当 medium の尻尾だった)。"""
        if self.staff_effort != "balanced":
            return self.staff_effort or "medium"
        if i in (1, 2):
            return "low"
        if i == 0:
            return "medium"
        now = self.since()
        fed = self._fed_est(i, "medium", now)
        viewer = self._viewer_at(i, now)
        effort = "medium" if fed + self.RENDER_HEAD_S + self.NONSTOP_MARGIN_S <= viewer else "low"
        self.log(cut=c, event="staff_pace", effort=effort, fed_est=round(fed, 1), viewer_est=round(viewer, 1))
        return effort

    # ---- 投入と warm ----
    def submit(self, c: str | None, text: str, *, end: bool) -> dict[str, object] | None:
        """cut の text を流す (`drafts/{id}/cuts/` — 投入検査を通れば run に流れる) → {"sealed": True} か {"rejected": 理由,
        "defects": [DEFECT の行]}。None = 流す先が死んだ。"""
        if not self.stream_alive():
            return None
        error: Exception | None = None
        for attempt in range(2):
            try:
                r = self.call("cut", {"text": text, "end": end})
                return {"sealed": True, "lines": r.get("lines")}
            except (Rejected, RuntimeError) as e:
                error = e
            # 返事を失った投入は、server が受理したかを受理済みの cut 名で確かめる — 受理済みなら流れた物として続け、届いて
            # いなければ 1 回だけ送り直す (server は検査した prefix の上にだけ原子に足すので二重には入らない。先の投入が後から
            # 入れば、送り直しは 409 か DUP_CUT で止まり、ここで受理済みと分かる)
            if c is None or not (attempt or isinstance(error, cut_stages.Unreachable)):
                break
            if c in self.server_submitted():
                self.log(cut=c, event="submit_recovered", error=str(error)[:200])
                return {"sealed": True, "lines": None}
            if attempt:
                break
            self.log(cut=c, event="submit_retry", error=str(error)[:200])
        return {"rejected": str(error)[:400], "defects": error.defects if isinstance(error, Rejected) else []}

    async def submit_text(self, c: str | None, text: str, *, end: bool) -> list[str] | None:
        ack = await asyncio.to_thread(self.submit, c, text + "\n" if text else "", end=end)
        if ack is None:
            return None
        if "rejected" not in ack:
            return []
        defects = ack.get("defects")
        return [str(d) for d in defects] if isinstance(defects, list) and defects else [str(ack["rejected"])]

    def server_submitted(self) -> list[str]:
        """server が受理済みの cut 名 (`GET drafts/{id}/` の submitted_cuts — 投入の真実)。読めなければ空。"""
        try:
            return [str(x) for x in self.call("status").get("submitted_cuts", [])]
        except RuntimeError:
            return []

    async def warm_text(self, text: str) -> str | None:
        """run に素材を先に作らせる (`drafts/{id}/warm/` — 返事を待たずに run が裏で解く・動画には入らない)。"""
        try:
            await asyncio.to_thread(self.call, "warm", {"text": text})
        except (Rejected, RuntimeError) as e:
            return str(e)
        return None

    # ---- run の開始と終わり ----
    def speech_file_ids(self) -> list[str]:
        """持ち込み音声 (`--speech` — project/speech.json の sources) の id。無ければ空。"""
        path = self.project / "speech.json"
        if not path.is_file():
            return []
        return [str(source["file_id"]) for source in json.loads(path.read_text()).get("sources", [])]

    def length_gap(self) -> dict[str, float | None]:
        """依頼の目安の秒・著者の plan の和・check の見込みの和・実尺 (製品の stream_done の duration_s) — 記録。"""
        actual: float | None = None
        with contextlib.suppress(OSError, ValueError):
            for line in (self.st / "run.jsonl").read_text().splitlines():
                e = json.loads(line)
                if e.get("event") == "stream_done" and isinstance(e.get("duration_s"), (int, float)):
                    actual = float(e["duration_s"])
        plan = self.plan_seconds()
        return {
            "requested_s": self.seconds,
            "plan_s": round(sum(plan.values()), 1) if plan else None,
            "estimate_s": round(sum(self.estimated_seconds().values()), 1) if self.order else None,
            "actual_s": actual,
        }

    # ---- 文書の版の照合 (app_main/docs/feature/video_generate/reference_sync.md) ----
    def write_sync(self, **state: object) -> None:
        """照合の状態 (stream/reference_sync.json) を atomic に書く — 著者・担当・直し役が claude を起こす前に読む。"""
        tmp = self.st / f"{REFERENCE_SYNC_FILE}.tmp"
        tmp.write_text(json.dumps(state, ensure_ascii=False))
        tmp.replace(self.st / REFERENCE_SYNC_FILE)
        self.log(event="reference_sync", **state)

    def sync_gate(self) -> str | None:
        """照合が版の契約の外 (gate) と決めた時の案内。"""
        path = self.st / REFERENCE_SYNC_FILE
        if not path.is_file():
            return None
        state = json.loads(path.read_text())
        return str(state.get("message")) if state.get("status") == "gate" else None

    def abort(self, reason: str) -> None:
        """run を中断する (`drafts/{id}/` の DELETE — run を即解放する)。"""
        if self.video_id is None:
            return
        try:
            self.call("abort")
            self.log(event="aborted", reason=reason)
        except (Rejected, RuntimeError, OSError) as e:
            self.log(event="abort_failed", reason=reason, error=str(e)[:200])

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
        """監督 (stream_pipeline.py) の中断の印 stream/engine.failed (engine に依らない「止める」信号)。"""
        return (self.st / "engine.failed").exists()

    def abort_engine(self) -> int:
        self.log(event="engine_failed", reason=(self.st / "engine.failed").read_text()[:400])
        self.abort("生成が中断された")
        self.close()
        return 1

    async def _stream(self) -> int:
        """著者の file の受けと cut の段・投入を回す。中断 (engine.failed) は即座に止める。0 = 投入を終えた。"""
        # 待ちの旗はこの loop で作り直す (python 3.9 の asyncio.Event は作った時の loop に縛られる — 配布 client は macOS 標準の 3.9)
        self.root_seen, self.author_done, self.root_clear = asyncio.Event(), asyncio.Event(), asyncio.Event()
        watcher = asyncio.create_task(self.watch_author())
        stages = asyncio.create_task(self.stages())
        try:
            while not stages.done():
                if self.engine_failed():
                    stages.cancel()
                    return self.abort_engine()
                await asyncio.wait([stages], timeout=0.1)
            if self.engine_failed():
                return self.abort_engine()
            try:
                stages.result()
            except cut_stages.FeedFailed as e:
                self.abort(str(e))
                self.log(event="feed_aborted", reason=str(e))
            return 0
        finally:
            watcher.cancel()
            await asyncio.gather(watcher, stages, return_exceptions=True)

    def run(self) -> int:
        self.log(event="orchestrator_start")
        sync = threading.Thread(target=self.sync_reference, daemon=True)
        sync.start()
        while not (self.solo / "order.txt").exists():
            if (gate := self.sync_gate()) is not None:  # 版の契約の外 — 著者も claude を起こす前に止まる
                print(f"開始できない: {gate}", flush=True)
                return 1
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
        plan = self.solo / "plan.txt"
        self.plan = plan.read_text() if plan.exists() else ""
        self.log(event="plan_seen", cuts=self.order)
        if self.engine_failed():
            return self.abort_engine()
        sync.join()
        if (gate := self.sync_gate()) is not None:
            print(f"開始できない: {gate}", flush=True)
            return 1
        rules = self.rules_payload if self.rules_payload is not None else self.call("rules")
        rows = [row for row in rules.get("rules", []) if isinstance(row, dict)]
        self.who = {str(row["name"]): str(row.get("who") or "author") for row in rows}
        self.sure = frozenset(str(row["name"]) for row in rows if row.get("sure"))
        self.start()
        if self.video_id is None:
            self.log(event="start_failed")
            return 1
        code = asyncio.run(self._stream())
        return code if code else self.wait()

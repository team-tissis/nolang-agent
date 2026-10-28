"""stream の著者 — Opus を Claude Code (`claude -p`・tool 無し) で呼び、本文の src を token の stream で受けて section が閉じた順に file に落とす。

著者は 1 call (`claude -p --output-format stream-json`・system prompt = skill の文書 + type の見本 2 本・既定 low):
  `=== plan ===` (cut 一覧) → `=== root_design ===` → `=== root_timeline ===` → `=== cut 名 ===` を構成の順に (design の block・`---timeline---`・
  timeline の block) → `=== end ===`。plan が閉じた時点で solo/order.txt を書く (orchestrator が cut を待ち始める)。
  low は書き始めるまで数秒で、書く速さ (約 180 字/s・1 cut 約 3.5 s) が再生より速いので、cut を分けて並行に書かせる理由が無い。質は cut ごとの
  担当 (medium) が運ぶ (docs/draft_src_v2/stream-evidence-261013.md s9 / s10)。1 人が全 cut を書くので、cut を跨ぐ名の衝突・型のばらつきも出ない。
直し (`--fix low` の時) は stream_run.py が cut ごとに頼む (`fix` subcommand: block + check の指摘 → 直した block)。
担当・直し役の system prompt (見本込み) は著者の call と並んで 1 回だけ温める (`warmup`・author.jsonl の `warmup` event)。

usage (repo root から):
  python stream_author.py run  <project>   [--effort low] [--samples a.md,b.md]
      --samples = system prompt に同梱する見本 (reference/samples/ の file 名・2 本以上)。省略時は reference/samples/ の hf の写し
                  `hf_<type>_*.md` 2 本 (依頼と同じ題材を外し、依頼と同じ向きの物を先に・pick_samples)。stream/samples.txt に記録し fix も同じ見本を使う
  python stream_author.py staff <project> <cut> <findings>  [--effort medium]   # 担当: cut を仕上げて block を stdout へ
  python stream_author.py fix  <project> <cut 名> <findings file> [--root] [--effort low] [--review] [--shots a.png,b.png]
      → stdout に直した block (--root = 根の 2 file も直す・--review = 見直し (指摘に出ない弱い所・崩れも探す)・
        --shots = 見直しに cut の静止画も見せる (stream_run の見直し))
project = tmp/studio/<name>/ (request.txt・params.txt = "type aspect seconds [editable]"・studio/ = `new` の雛形)。
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
from collections.abc import Callable
from pathlib import Path

import author_core  # 隣の file = libs/ai/llm_prompts/draft_author/author_core.py の byte 同一の写し (prompt と出力の読みの正本)
from author_core import (
    AUTO_SECONDS,
    AuthorOutputSplitter,
    AuthorSection,
    apply_line_edits,
    author_prompt,
    editable_note,
    emitted_block,
    fallback_root_timeline,
    fix_prompt,
    has_empty_edits,
    is_verbatim,
    parse_edits,
    plan_names,
    spoken,
    touched_fixed,
    without_marks,
)

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
# 見本の置き場 (選び方・近い type・1 本の大きさの上限は author_core.pick_samples)
SAMPLES_DIR = SKILL / "reference/samples"
# 担当・直しの system に見本を同梱する type。10-25 の著者固定 A/B (4 題材・Opus 盲検両順 + ユーザーの盲検視聴) で、
# 見本の効きが残るのは craft 的な type だけだった — cinematic は見本あり側が両順一致で勝ち・data は微・compare / concept は
# 見本なしが小勝ち (craft.md が見本の教えを肩代わり)。著者の user turn の見本は全 type で据え置き (外す検証はしていない)
STAFF_SAMPLE_TYPES = ("cinematic", "story")
# claude を起動する cwd: CLAUDE.md の無い場所 (repo の CLAUDE.md を読ませない)
CWD = Path("/tmp/nolang-stream-cwd")  # claude -p の cwd (repo の外 — project の CLAUDE.md / settings を読ませない)
MODEL = "claude-opus-5-5"
# 見直し役に見せる静止画の幅 (1920 のままだと 1 枚 2.7k token・960 で 0.7k — 字の重なりは 960 でも見える)
SHOT_WIDTH = 960


# claude の実体を起動時に解決する (PATH 上の shim が更新中だと一時的に見つからない)
def claude_bin() -> str:
    """`claude` の実体。shim は自動更新の瞬間に消える事があるので呼ぶたびに引く (見つからなければ名前のまま → 呼ぶ側がやり直す)。"""
    return shutil.which("claude") or "claude"


def log(st: Path, **kw: object) -> None:
    kw["t"] = time.time()
    with (st / "author.jsonl").open("a") as f:
        f.write(json.dumps(kw, ensure_ascii=False) + "\n")
    print(json.dumps(kw, ensure_ascii=False), file=sys.stderr, flush=True)  # stdout は fix の本文に使う


def _editable() -> bool:
    """編集可能モード (env NOLANG_STUDIO_PROFILE=editable・stream_make.sh --editable)。"""
    return os.environ.get("NOLANG_STUDIO_PROFILE") == "editable"


def same_topic(name: str, request: str) -> bool:
    """見本が依頼と同じ題材か (`author_core.same_topic`)。"""
    return author_core.same_topic(SAMPLES_DIR, name, request)


def pick_samples(typ: str, aspect: str, request: str) -> tuple[tuple[str, ...], list[str]]:
    """reference/samples/ から見本 2 本 → (見本, 外した見本)。選び方 (hf の写し / editable 準拠・同じ題材を外す・同じ向きを先に) は
    `author_core.pick_samples`。"""
    try:
        picked, skipped = author_core.pick_samples(
            SAMPLES_DIR, typ, request, portrait=aspect == "9:16", editable=_editable()
        )
    except ValueError as e:
        raise SystemExit(str(e)) from e
    return picked, skipped


def build_system_prompt(out: Path, samples: tuple[str, ...] | None) -> Path:
    """3 役の system prompt (`author_core.system_docs_text` — 役の冒頭 + skill の文書 + 見本) を file に書く。samples=None は見本なし
    (著者の静的な system prompt — 見本は user turn に置く)。担当と直し役の見本は STAFF_SAMPLE_TYPES だけ — hf2 (craft.md) 採用前は
    外すと大敗した (10-22) が、採用後の再検証 (10-25) では密度ほぼ同等・品質 2-2 で、効きが残るのは craft 的な type だけだった。"""
    out.write_text(author_core.system_docs_text(SKILL, tuple(samples or ())))
    return out


def samples_text(samples: tuple[str, ...]) -> str:
    """見本の本文 (著者の user turn に置く)。"""
    return author_core.samples_text(SAMPLES_DIR, samples)


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
    reference_note: str = "",
    verbatim: bool = False,
    keep_assets: bool = False,
) -> str:
    """担当の user turn — 著者の cut をプロの解説動画の密度と階層に仕上げる。見る観点・欠陥の型・字の大きさの規則は渡さず、機構の事実
    (依頼の遵守・根・定義を変えない・台詞は直してよいが逐語の台本は変えない・DEFECT の常連) だけ。担当は著者の構図を残して要素・印・効果音を足す (10-23 の実測で要素 4.9 → 9.7 個)。"""
    k, m = (order.index(name) + 1, len(order)) if order and name in order else (0, len(order or []))
    prev = (
        f"The previous cut `{prev_name}` (the author's version, for reference. Do not change it. That cut is being finished in parallel by its own staff, so the real screen will differ):\n"
        f"=== cut {prev_name} ===\n{prev_block}=== end ===\n"
        if prev_name and prev_block
        else ""
    )
    if keep_assets:
        speech_rule = "Do not change the speech (`@` lines) — neither the characters nor how the lines split (the voice is already being made from the author's version; adding marks is fine). "
        picture_rule = (
            "Pictures (`img#` descriptions and `subject:` / `room:`) stay as the author wrote them — do not change a description or add a picture with a new description (the pictures are"
            " already being made from the author's version; re-placing the same description, and changing position and size, are fine). Put text in the opening the picture's `room:` leaves."
        )
    else:
        speech_rule = (
            "Do not change a single character of the speech (`@` lines' characters) — this video reads the request's script verbatim (only added commas and the reading notation `{表記|読み}` are allowed). "
            if verbatim
            else "You may also fix the speech (`@` lines' characters) (the voice and subtitles are made from this version; the fixer after you cannot change them). Keep this cut's planned content and sentence count. "
        )
        picture_rule = (
            "This is the only stage that may rewrite a picture's description (the fixer after you cannot). The generated pictures cannot be looked at, so clear the spot where"
            " text goes with `subject:` / `room:`."
        )
    return f"""You are a professional motion designer and video editor, the staff in charge of cut `{name}` of this video. You received the block the author wrote.
Finish this cut to the density and hierarchy of an explainer video a professional studio could ship. Build it out to the motion and the sound. Rebuild it if needed.

What to keep (facts of the machine):
- The user's request below (how to show things, colors, text, what goes in and what stays out) binds you — however much you rebuild, do not drift from it.
- {speech_rule}Keep the speakers (`@name:`).
- Do not change the root (palette, font, cast) or earlier cuts' definitions (def, motion, run) (using them is fine). This block's definitions are used by later cuts under the same
  names — do not change a name, an argument shape or a look. If you need another shape or look, define it under a new name and use it in this block. Keep the element-name prefix (`{name}`).
- Do not settle a sentence's picture for "a title + a photo" — make a conclusion card or a state change the hero (no title-and-photo idle beat at a chapter's start).
- {picture_rule}
- Keys are only those in authoring's "Types" table (an unknown key is a DEFECT and the cut falls). `hug` is subtitles-only. Marks (`[>#name]` `[!#name …]`) go on this cut's layers and the root's elements (cards and subtitles that span cuts — keep a `[>#name]` whose word the author chose). Never mark an earlier cut's layer, and never create a copy of a root element.
- DEFECT regulars: a `"a;b"` list is per-instance values of ×N — the element (or the def call) needs `×N` at the end of its line / the same key appears once per element /
  a `name{{tok}}`'s tok is never empty / `to,{{…}}` has no GSAP position argument (`,2`) — timing is `+N` `-N` /
  `filter` looks are only the full-strength `sepia(1)` `grayscale(1)` `invert(1)`.
{editable_note(_editable())}{reference_note}
The user's request:
{request.strip() or "(none)"}
User settings: target length {"not specified" if target_s == AUTO_SECONDS else f"{target_s} seconds"} (the plan's targets sum to {planned_s:.0f} s; length is set by the speech)

This cut is number {k} of {m}.
The plan:
{plan}
Root (reference — do not change):
=== root_design ===
{root_d}
=== root_timeline ===
{root_t}
{"Definitions from earlier cuts (reference — do not change them; you may use them):" + chr(10) + defs_before if defs_before.strip() else ""}
{prev}
check's findings (on the author's version, for reference):
{findings or "(none)"}
The author's version's timing (check's estimate — seconds from the video's head; moving marks changes it):
{timing.strip() or "(none)"}

The block to finish:
=== cut {name} ===
{block}
=== end ===

Output only the finished block in the same format (no preamble, no explanations, no code fences; from `=== cut {name} ===` through `=== end ===`).
"""


def reference_of(project: Path) -> dict[str, object] | None:
    """参照の動画 (`stream_make.sh --ref` / 依頼の `[video:id]`) — project/reference.json (`GET drafts/templates/{id}/` の応答:
    src・題・「ユーザーが選んだ形」の節 `brief`)。無ければ None。"""
    path = project / "reference.json"
    if not path.exists():
        return None
    loaded = json.loads(path.read_text())
    return loaded if isinstance(loaded, dict) and loaded.get("brief") else None


def speech_of(project: Path) -> dict[str, object] | None:
    """持ち込み音声 (`stream_make.sh --speech`) — project/speech.json (`POST drafts/speeches/` の ready の応答: clip 台帳と `@clip` の
    書き方の節 `brief`・音声の id `sources`)。無ければ None。"""
    path = project / "speech.json"
    if not path.exists():
        return None
    loaded = json.loads(path.read_text())
    return loaded if isinstance(loaded, dict) and loaded.get("brief") else None


def reference_role_note(project: Path) -> str:
    """担当・直し役への参照の注記 (`author_core.reference_role_note` — src は渡さない。根は著者が参照から写した物)。"""
    ref = reference_of(project)
    return author_core.reference_role_note(None if ref is None else str(ref["title"]))


_SPEAKER = re.compile(r"^\s*@[^:\s\[]*:")  # 台詞の行の頭 `@n:` / `@:` (素材の復元の比較用。spoken は author_core)


def _split_marks(body: str) -> tuple[str, list[tuple[int, str]]]:
    """台詞の本文を (印を除いた文字, [(文字の中の位置, 印)]) に割る (`without_marks` と同じ入れ子の数え方)。"""
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


def restore_speech(author: str, staff: str, *, exact: bool = False) -> tuple[str, list[dict[str, str]]]:
    """逐語の台本の動画で、担当の block の台詞 (`@` の行) を著者の版の文字に戻す → (戻した block, 戻した行の記録)。比べるのは `spoken` (読点の追加と読みの
    指定は許す)。台詞の行の数が同じ区間は行ごとに著者の文字へ担当の印を載せ (`marks`)、行を足した / 消した区間は著者の行ごと
    戻す (`author_line`・印も著者の物)。台詞の行の割り方だけ変えた (文字の並びは同じ) なら戻さない。声は担当の版から作るので、ここで
    戻さないと後段では戻せない。exact = 読点・読みの指定・行の割り方も著者の版に揃える (担当が素材を変えない run — 声は著者の版から
    先に作っていて、文字が 1 つでも違うと合成し直しになる)。"""
    import difflib  # noqa: PLC0415

    def speech_rows(text: str) -> list[str]:  # timeline の台詞の行 (design の `@#名` は定義の見出し)
        return [l for l in text.split("---timeline---", 1)[-1].splitlines() if l.lstrip().startswith("@")]

    rows_a, rows_s = speech_rows(author), speech_rows(staff)
    norm = _bare_speech if exact else spoken
    norm_a, norm_s = [norm(l) for l in rows_a], [norm(l) for l in rows_s]
    if (norm_a == norm_s) if exact else ("".join(norm_a) == "".join(norm_s)):
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


def _bare_speech(line: str) -> str:
    """台詞の行の声の元の文字 (印と空白だけを除く — 読点と読みの指定は残す)。担当が素材を変えない run の台詞の比較。"""
    return re.sub(r"\s", "", without_marks(_SPEAKER.sub("", line, count=1)))


_PICTURE_LINE = re.compile(r"^(\s*)img#([^\s(]+)\((?:[^()]|\([^()]*\))*\)\s*(.*)$")


_ELEMENT_LINE = re.compile(r"^(\s*)[a-z][\w-]*#([\w-]+)")  # design の要素の行 (`  p#名(` — 字下げで親子)
_SILENCE_TAIL = re.compile(r"\[silence:\+([\d.]+)s\]\s*$")
_SILENCE_AT = re.compile(r"\[silence:\+([\d.]+)s\]")


def _split_top(text: str, sep: str) -> list[str]:
    """括弧・引用符の外の sep で割る (`out: fade {duration: .4}; main: spin {period: 9, dir: 'ccw'}` を宣言ごとに)。"""
    parts, depth, quote, start = [], 0, "", 0
    for at, ch in enumerate(text):
        if quote:
            quote = "" if ch == quote else quote
        elif ch in "'\"":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        elif ch == sep and depth == 0:
            parts.append(text[start:at])
            start = at + 1
    return [*parts, text[start:]]


def _add_silence(line: str, seconds: float, *, head: bool) -> str:
    """台詞の行の頭 (話者の後) か末尾の `[silence:+Ns]` に seconds を足す (無ければ書く)。"""
    if head:
        speaker = _SPEAKER.match(line)
        cut = speaker.end() if speaker else 0
        rest = line[cut:]
        lead = rest[: len(rest) - len(rest.lstrip())]
        if (old := _SILENCE_AT.match(rest[len(lead) :])) is not None:
            total = float(old.group(1)) + seconds
            return line[:cut] + lead + f"[silence:+{total:.2f}s]" + rest[len(lead) + old.end() :]
        return line[:cut] + lead + f"[silence:+{seconds:.2f}s]" + rest[len(lead) :]
    if (old := _SILENCE_TAIL.search(line)) is not None:
        return line[: old.start()] + f"[silence:+{float(old.group(1)) + seconds:.2f}s]"
    return line.rstrip() + f"[silence:+{seconds:.2f}s]"


def _element_spans(lines: list[str]) -> dict[str, tuple[int, int, str]]:
    """design の行 → 要素の path (字下げで親の名を `.` で繋ぐ) → (行の始め, 子を含む終わり, 親の path)。"""
    spans: dict[str, tuple[int, int, str]] = {}
    stack: list[tuple[int, str]] = []
    for at, line in enumerate(lines):
        hit = _ELEMENT_LINE.match(line)
        if hit is None:
            continue
        indent = len(hit.group(1))
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1] if stack else ""
        path = f"{parent}.{hit.group(2)}" if parent else hit.group(2)
        end = at + 1
        while end < len(lines) and lines[end].strip() and len(lines[end]) - len(lines[end].lstrip()) > indent:
            end += 1
        spans[path] = (at, end, parent)
        stack.append((indent, path))
    return spans


# 積極的に当てる機械の直し — 直し方が正解として一つに決まり、問題を隠さず、著者が書いた物を消さない (design の `\n`・根から継いだ
# 切替と書いた out の二重 (out を残して切替を cut に)・言い切ってから切り替える / 切替が済んでから話し始める 0.5 秒以下の間)。他
# (0.5 秒を超える間・切替を短く溶かす・文字を板の上に出す) は消極的: 問題は消えるが LLM ならもっと良い直し方 (構成・位置・切替の種)
# を選べる — 後に担当や warn を直す直し役が残る間は当てずに指摘のまま渡し、LLM がもう見ない段で当てる (10-26 bench: 0.5 秒以下の
# 間を積極的にした腕が 60-52・消極的まで担当の前に当てた腕は 40-74 で負け)。積極 / 消極は規則で決める (同じ `transition` の操作でも
# double_exit の `cut` は積極・ghost_dissolve の短い dissolve は消極)
AUTOFIX_SURE_RULES = frozenset({"literal_newline", "double_exit"})
AUTOFIX_SURE_SILENCE_S = 0.5


def apply_autofix(
    block: str, findings: list[dict[str, str]], *, sure_only: bool = False
) -> tuple[str, list[dict[str, str]]]:
    """check の指摘のうち直し方が一つに決まる物 (`autofix` — lint が計算した `操作:引数`) を cut の block (design
    `---timeline---` timeline) に当てる → (直した block, 当てた指摘)。当たらない指摘 (行が見つからない・形が違う) は飛ばす。
    - `silence_tail:秒` 最後の台詞の末尾の無音 (切替が台詞に掛かる) / `silence_head:秒` 最初の台詞の頭の無音 (入場が切替の窓に入る)
    - `transition:種,尺,overlap=…` cut の切替の行の種・尺・overlap を替える (他の引数 — 効果音・向き — は残す)・`transition:cut` は
      切替の行の無い cut に `transition cut` を足す (根から継いだ切替と書いた out の二重掛け — 書いた out を残す)
    - `move_after:文字:隠す側` 隠れた文字の行 (と子) を隠す側の行 (と子) の後へ (同じ親の兄弟の時だけ)
    - `br` design の文字の中の `\\n` を `[br]` に (`\"\"\"` の source の中は見ない — timeline の台詞は対象外)
    sure_only = 積極的な直し (`AUTOFIX_SURE_RULES` と短い無音) だけ当てる (後に LLM が残る時)。"""
    design, sep, timeline = block.partition("---timeline---")
    if not sep:
        return block, []
    dlines, tlines = design.split("\n"), timeline.split("\n")
    speech = [at for at, line in enumerate(tlines) if line.lstrip().startswith("@")]
    applied: list[dict[str, str]] = []
    for finding in findings:
        op, _, arg = str(finding.get("autofix") or "").partition(":")
        sure = finding.get("rule") in AUTOFIX_SURE_RULES or (
            op in ("silence_tail", "silence_head") and float(arg) <= AUTOFIX_SURE_SILENCE_S
        )
        if sure_only and not sure:
            continue
        before = (list(dlines), list(tlines))
        if op in ("silence_tail", "silence_head") and speech:
            at = speech[-1] if op == "silence_tail" else speech[0]
            tlines[at] = _add_silence(tlines[at], float(arg), head=op == "silence_head")
        elif op == "transition":
            spec = _split_top(arg, ",")
            lines = [at for at, line in enumerate(tlines) if line.lstrip().startswith("transition ")]
            if lines:
                old = _split_top(tlines[lines[-1]].strip().removeprefix("transition ").strip(), ",")
                extra = [part for part in old[1:] if "=" in part and not part.strip().startswith(("overlap=",))]
                tlines[lines[-1]] = "transition " + ",".join([*spec, *(part.strip() for part in extra)])
            else:
                last = max(at for at, line in enumerate(tlines) if line.strip())
                tlines.insert(last + 1, "transition " + arg)
        elif op == "br":
            fence = False
            for at, line in enumerate(dlines):
                if '"""' in line:
                    fence = fence if line.count('"""') % 2 == 0 else not fence
                    continue
                if not fence and "\\n" in line:
                    dlines[at] = line.replace("\\n", "[br]")
        elif op == "move_after":
            mine, _, theirs = arg.partition(":")
            spans = _element_spans(dlines)
            if (
                mine in spans
                and theirs in spans
                and spans[mine][2] == spans[theirs][2]
                and spans[mine][0] < spans[theirs][0]
            ):
                (start, end, _), (_, over_end, _) = spans[mine], spans[theirs]
                moved = dlines[start:end]
                dlines = dlines[:start] + dlines[end:over_end] + moved + dlines[over_end:]
        if (dlines, tlines) != before:
            applied.append(finding)
    return "\n".join(dlines) + sep + "\n".join(tlines), applied


def restore_pictures(author: str, staff: str) -> tuple[str, list[dict[str, str]]]:
    """担当が素材を変えない run で、担当の block の絵 (`img#`) を著者の版の説明文に戻す → (戻した block, 記録)。著者の版にある名の
    絵は説明文を著者の物に書き戻し (`mode: text`)、著者の版に無い説明文の新しい絵は行 (と字下げの子) ごと消して timeline の
    その名の印も落とす (`mode: dropped`)。同じ説明文の絵の置き直し (新しい名) はそのまま (同じ素材)。"""
    by_name: dict[str, str] = {}
    for line in author.split("---timeline---", 1)[0].splitlines():
        if m := _PICTURE_LINE.match(line):
            by_name[m.group(2)] = m.group(3).strip()
    known = set(by_name.values())
    design, sep, timeline = staff.partition("---timeline---")
    out: list[str] = []
    dropped: list[str] = []
    log: list[dict[str, str]] = []
    skip_indent: int | None = None
    for line in design.split("\n"):
        indent = len(line) - len(line.lstrip())
        if skip_indent is not None:
            if line.strip() and indent > skip_indent:
                continue
            skip_indent = None
        m = _PICTURE_LINE.match(line)
        if m is None:
            out.append(line)
            continue
        name, desc = m.group(2), m.group(3).strip()
        if name in by_name and desc != by_name[name]:
            out.append(line[: m.start(3)] + by_name[name])
            log.append({"mode": "text", "name": name, "staff": desc[:80]})
        elif name not in by_name and desc not in known:
            dropped.append(name)
            skip_indent = indent
            log.append({"mode": "dropped", "name": name, "staff": desc[:80]})
        else:
            out.append(line)
    if dropped and sep:
        names = "|".join(re.escape(n) for n in dropped)
        mark = re.compile(r"\[[^\[\]]*#(?:" + names + r")(?![\w.-])[^\[\]]*\]")
        timeline = "\n".join(mark.sub("", l) if l.lstrip().startswith("@") else l for l in timeline.split("\n"))
    return "\n".join(out) + sep + timeline, log


class Splitter:
    """stream の本文を section に割り (`author_core.AuthorOutputSplitter`)、閉じた順に solo/ へ書く。"""

    def __init__(self, proj: Path, st: Path, tag: str) -> None:
        self.proj, self.st, self.tag = proj, st, tag
        self.inner = AuthorOutputSplitter(self._write)
        self.out: dict[str, str] = {}
        self.order: list[str] = []

    def feed(self, text: str) -> None:
        self.inner.feed(text)

    def finish(self) -> None:
        self.inner.finish()

    def _write(self, sec: AuthorSection) -> None:
        kind, name, body = sec.kind, sec.name or "", sec.body
        if kind == "cut":
            if "root_design" in self.out and "root_timeline" not in self.out:
                rt = fallback_root_timeline(body)
                (self.proj / "root_timeline.txt").write_text(rt)
                self.out["root_timeline"] = rt
                log(self.st, event="root_timeline_missing", cut=name, root_timeline=rt, tag=self.tag)
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


def run(project: Path, *, effort: str, samples: tuple[str, ...] | None) -> int:
    proj, st, studio = project / "solo", project / "stream", project / "studio"
    proj.mkdir(exist_ok=True)
    st.mkdir(exist_ok=True)
    # params は "型 縦横 秒" + 任意の flag token (`editable` — stream_make.sh --editable が足す)
    typ, aspect, seconds = (project / "params.txt").read_text().split()[:3]
    request = (project / "request.txt").read_text()
    if samples is None:
        samples, skipped = pick_samples(typ, aspect, request)
        staff_samples = samples if typ in STAFF_SAMPLE_TYPES else ()
    else:  # 明示の見本はそのまま使う (同じ題材なら記録だけ)・明示なら担当・直しにも type を問わず入れる
        skipped = []
        staff_samples = samples
        if same := [n for n in samples if same_topic(n, request)]:
            log(st, event="samples_same_topic", samples=same)
    # 担当・直し役の system prompt (STAFF_SAMPLE_TYPES は見本込み — 同じ見本の run どうしで cache を共有する)。
    # 著者の call と並んで 1 回だけ温める
    shared_prompt = build_system_prompt(st / "system_prompt.md", staff_samples or None)
    warm = None
    if os.environ.get("NOLANG_STUDIO_ENGINE", "claude") == "claude":
        warm = threading.Thread(target=warmup, args=(st, shared_prompt), daemon=True)
        warm.start()
    # 著者の system prompt は見本を含めない静的な物 — 見本は題材ごとに変わるので system に置くと動画ごとに 85〜95k token が
    # cache miss になる (o20 / o21 の著者は cache read 0)。見本は user turn の末尾 (依頼の前) に同じ内容で置く (10-18)
    sp = build_system_prompt(st / "system_prompt_author.md", None)
    # 比べ用: 著者の user turn の見本を減らす — `none` = 置かない・`1` = 先頭の 1 本だけ (担当・直し役の見本は STAFF_SAMPLE_TYPES のまま)
    author_samples = {"none": (), "1": samples[:1]}.get(os.environ.get("NOLANG_STUDIO_AUTHOR_SAMPLES", ""), samples)
    # 比べ用: 著者の見本だけ別の type から選ぶ (製品は type を決めず concept の見本 = `concept`)
    if sample_type := os.environ.get("NOLANG_STUDIO_AUTHOR_SAMPLE_TYPE"):
        author_samples = pick_samples(sample_type, aspect, request)[0]
    (st / "samples.txt").write_text(",".join(samples) + "\n")  # 記録 (--samples で再投入 = 明示扱いで全役に入る)
    skeleton_d = (studio / "design.txt").read_text()
    canvas = next((line.split()[1] for line in skeleton_d.splitlines() if line.startswith("canvas ")), "")
    if not request.lstrip().startswith("---- ユーザーの依頼 ----"):
        request = "---- ユーザーの依頼 ----\n" + request.rstrip("\n") + "\n---- ここまで ----\n"
    log(
        st,
        event="launch",
        type=typ,
        aspect=aspect,
        seconds=seconds,
        effort=effort,
        samples=list(author_samples),
        samples_skipped=skipped,
    )
    ref = reference_of(project)
    if ref is not None:  # 依頼の `[video:<id>]` は参照の題に (製品の入口が題へ置換するのと同じ)
        request = re.sub(rf"\[video:{re.escape(str(ref['template_video_id']))}\]", f"「{ref['title']}」", request)
        log(st, event="reference", video_id=ref["template_video_id"], source=ref.get("source"), title=ref.get("title"))
    if extra := os.environ.get("NOLANG_STUDIO_AUTHOR_EXTRA"):  # 比べ用: 依頼の後ろに足す著者だけの注意 (file の path)
        request += "\n" + Path(extra).read_text()
    speech = speech_of(project)
    prompt = author_prompt(
        aspect,
        seconds,
        canvas,
        request,
        samples_text(author_samples),
        str(ref["brief"]) if ref is not None else "",
        f"\n{speech['brief']}\n" if speech is not None else "",
        editable=_editable(),
        referenced=ref is not None,
    )
    sp0 = Splitter(proj, st, "author")
    if author_model := os.environ.get(
        "NOLANG_STUDIO_AUTHOR_MODEL"
    ):  # 著者だけ別の model (担当・直し役は engine のまま)
        from stream_gemini import stream_gemini

        stream_gemini(st, prompt, sp0.feed, system_prompt=sp, effort=effort, tag="author", model=author_model, log=log)
    else:
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
    """著者 / 直し役 / 担当の出力から cut の block を切り出して stdout へ (`author_core.emitted_block` — 見出し無し・fence 付き・
    印無しで timeline が始まる形も受ける)。block が無ければ記録して 1。"""
    body = emitted_block(name, text)
    if body is None:
        log(st, event=event, cut=name, chars=len(text))
        return 1
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
    review = 見直し (指摘に出ない弱い所・崩れも探す)・shots = 見直しに見せる cut の静止画。"""
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
            reference_note=reference_role_note(project),
            editable=_editable(),
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
    if edits is None and not dropped and has_empty_edits(text):
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


def staff(project: Path, name: str, findings_file: Path, *, effort: str, keep_assets: bool = False) -> int:
    """担当: 著者の cut を仕上げる (前の cut は著者の版を参考に渡す = cut ごとに並列に走らせるため)。依頼文・cut の
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
    # 動画の長さの門 = plan の目標秒の和 (orchestrator の進行線の total と同じ値)
    planned_s = sum(sec for _, sec in plan_names(plan))
    _typ, _aspect, target_s = (project / "params.txt").read_text().split()[:3]
    request = (project / "request.txt").read_text()
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
            request=request,
            order=order,
            target_s=target_s,
            timing=timing_file.read_text() if timing_file.exists() else "",
            reference_note=reference_role_note(project),
            verbatim=is_verbatim(plan, request),
            keep_assets=keep_assets,
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
        return staff(project, argv[2], Path(argv[3]), effort=eff, keep_assets="--keep-assets" in argv)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

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
import unicodedata
from collections.abc import Callable
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
# 見本の置き場。既定の見本は hf の写し `hf_<type>_*.md` 2 本 (pick_samples)。自分の type の見本が足りない時に借りる近い type と、
# system prompt に同梱する見本 1 本の大きさの上限 (超える物は選ばない)
SAMPLES_DIR = SKILL / "reference/samples"
NEAR_TYPE = {"cinematic": "story", "compare": "concept", "data": "compare", "story": "cinematic", "concept": "compare"}
# 担当・直しの system に見本を同梱する type。10-25 の著者固定 A/B (4 題材・Opus 盲検両順 + ユーザーの盲検視聴) で、
# 見本の効きが残るのは craft 的な type だけだった — cinematic は見本あり側が両順一致で勝ち・data は微・compare / concept は
# 見本なしが小勝ち (craft.md が見本の教えを肩代わり)。著者の user turn の見本は全 type で据え置き (外す検証はしていない)
STAFF_SAMPLE_TYPES = ("cinematic", "story")
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
    """reference/samples/ から hf の写し (`hf_<type>_*.md`) 2 本 → (見本, 外した見本)。SAMPLE_MAX_BYTES 以下の自分の type の写しから
    (後ろに NEAR_TYPE の写しを足す)・依頼と同じ題材の物を外す・依頼と同じ向き (canvas の縦横) の物を先に。その中の順番は file 名順
    (大きさ順だと見本を 1 行直すたびに選ばれる物が替わる)。著者は見本を逐語で写す (s1 で 50〜68%・pv で台詞と印ごと) ので、同じ題材の
    見本は渡さない。NoLang の src の見本 (`<type>_NN.md`) は stream では渡さない — hf の写し 2 本の方が両順の比べで勝った (10-23)。"""
    portrait = aspect == "9:16"
    skipped: list[str] = []
    picked: list[str] = []
    if os.environ.get("NOLANG_STUDIO_PROFILE") == "editable":
        # 編集可能モードは editable 準拠の見本 (`editable_*.md`) を使う — hf の見本は keys / group / count を多用していて、
        # 著者が違反を写す (bench 10-25 の違反 19〜37/run の根)。type の合う物を先に、足りなければ他の editable で埋める
        names = sorted(
            p.name
            for p in SAMPLES_DIR.iterdir()
            if re.fullmatch(r"editable_.+\.md", p.name) and p.stat().st_size <= SAMPLE_MAX_BYTES
        )
        same = [n for n in names if same_topic(n, request)]
        skipped.extend(same)
        rest = [n for n in names if n not in same]
        by_type = [n for t in (typ, NEAR_TYPE[typ]) for n in rest if n.startswith(f"editable_{t}_")]
        ordered = by_type + [n for n in rest if n not in by_type]
        picked = sorted(ordered, key=lambda n: (ordered.index(n) >= len(by_type), sample_portrait(n) != portrait))[:2]
        if len(picked) == 2:
            return (picked[0], picked[1]), skipped
        skipped, picked = [], []  # editable の見本が足りない時だけ hf へ (無言で違反の見本に落ちるより良い)
    for t in (typ, NEAR_TYPE[typ]):
        names = sorted(
            p.name
            for p in SAMPLES_DIR.iterdir()
            if re.fullmatch(rf"hf_{t}_.+\.md", p.name) and p.stat().st_size <= SAMPLE_MAX_BYTES
        )
        same = [n for n in names if same_topic(n, request)]
        skipped.extend(same)
        picked += [n for n in names if n not in same]
    picked = sorted(picked, key=lambda n: sample_portrait(n) != portrait)[:2]
    if len(picked) < 2:
        raise SystemExit(f"reference/samples/ に {typ} ({NEAR_TYPE[typ]}) の hf の写しが 2 本無い: {picked}")
    return (picked[0], picked[1]), skipped


# 3 役の system prompt の冒頭 — プロの制作者への依頼の形 (hf の試行者に渡した依頼と同じ言い方)。作法の規則は渡さず、文法と機構の事実
# と制作の作法の抜粋 (reference/craft.md) を渡す。規則の束 (plan の規則・担当の 8 観点・確認表・style の組) より両順の比べで勝った (10-23)
SYSTEM_HEAD = (
    "You are a professional motion designer and video editor. You normally build videos with HTML + CSS + GSAP (write the"
    " scene's DOM, align the look with classes, and drive each element's entrance, state changes and exit on a GSAP"
    " timeline). This time you write that video as NoLang draft src, a compressed form of HTML / CSS / GSAP. Voices come"
    " from NoLang's speech synthesis, pictures from NoLang's image generation, and BGM, sound effects and fonts from"
    " NoLang's catalog — you order each with a short description. Build it out to the motion and the sound (BGM, entrance"
    " sound effects). The bar is the density and hierarchy of an explainer video a professional studio could ship.\n"
    "The work is split into three roles — the author who writes the whole video, the staff who finishes a cut, and the"
    " fixer who repairs what check flags. Which role you are, and what you may change, follow the user's instructions.\n"
    "This conversation has no tools (you cannot read or write files, and cannot run commands). The documents below are"
    " everything there is about writing draft src — do not try to read files. check and render are run by another"
    " process. You only write src in your reply.\n"
)
CRAFT_HEAD = (
    "The following is an excerpt from a production guide for making videos with HTML + GSAP. This conversation has no"
    " tools and no files, so skip anything about commands, files (SPEC.md and the like) or confirming with a person, and"
    " read it for the craft. For spelling, follow the draft src documents above.\n\n"
)
# SKILL.md のうち stream の役に渡す節 (文法)。工程・ループ・規則の一覧・stream の段取りは対話で skill を使う時の物なので渡さない
SKILL_GRAMMAR = ("## Differences", "## Spelling map", "## What cannot be written")


def _skill_grammar() -> str:
    """SKILL.md の冒頭 (圧縮の規則・素材の書き方) と文法の節だけ。frontmatter は落とす。"""
    parts = re.split(r"(?m)^(## .*)$", (SKILL / "SKILL.md").read_text())
    got = [parts[0].split("\n---\n", 1)[-1]]
    got += [parts[i] + parts[i + 1] for i in range(1, len(parts), 2) if parts[i].startswith(SKILL_GRAMMAR)]
    return "".join(got)


def build_system_prompt(out: Path, samples: tuple[str, ...] | None) -> Path:
    """役の冒頭 + SKILL の文法 + looks の罠 + sounds + authoring + capabilities + 制作の作法 + 見本 2 本 (道具の無い call は file を読めない
    ので全部同梱)。samples=None は見本なし (著者の静的な system prompt — 見本は user turn に置く)。担当と直し役の見本は
    STAFF_SAMPLE_TYPES だけ — hf2 (craft.md) 採用前は外すと大敗した (10-22) が、採用後の再検証 (10-25) では密度ほぼ同等・
    品質 2-2 で、効きが残るのは craft 的な type だけだった。"""
    looks = (SKILL / "reference/looks.md").read_text()
    parts = [
        SYSTEM_HEAD,
        "\n<!-- ===== how to write draft src ===== -->\n\n" + _skill_grammar(),
        "\n<!-- ===== reference/looks.md (traps) ===== -->\n\n## Beyond the grammar (traps)"
        + looks.split("## Beyond the grammar (traps)", 1)[1],
    ]
    # sounds.md のうち道具の節 (listen / engine の聴き比べ) は落とす — 3 役は command を打てない (SYSTEM_HEAD と矛盾する)
    sounds = re.sub(
        r"(?ms)^## (?:BGM: listen to candidates|Listening check).*?(?=^## |\Z)",
        "",
        (SKILL / "reference/sounds.md").read_text(),
    )
    parts.append("\n<!-- ===== reference/sounds.md ===== -->\n\n" + sounds)
    for rel in ("reference/authoring.md", "reference/capabilities.md"):
        parts.append(f"\n<!-- ===== {rel} ===== -->\n\n" + (SKILL / rel).read_text())
    parts.append(
        "\n<!-- ===== production craft ===== -->\n\n" + CRAFT_HEAD + (SKILL / "reference/craft.md").read_text()
    )
    parts.append(samples_text(samples or ()))
    out.write_text("".join(parts))
    return out


def samples_text(samples: tuple[str, ...]) -> str:
    """見本 2 本の本文 (著者の user turn に置く)。"""
    return "".join(
        f"\n<!-- ===== sample reference/samples/{name} ===== -->\n\n" + (SAMPLES_DIR / name).read_text()
        for name in samples
    )


def author_prompt(
    aspect: str, seconds: str, canvas: str, request: str, samples: str = "", reference: str = "", speech: str = ""
) -> str:
    """著者の user turn。構成の型・雛形・数字の規則は渡さない (台本と絵コンテは著者が依頼から決める)。雛形は 1 行目と canvas だけ —
    役の入った雛形 (cut の役・定義済みの段・theme dark) を渡すと部品を写し、暗い地に揃った (10-23)。"""
    if seconds == AUTO_SECONDS:
        allot = "No length was specified — decide a length that fits the content and give every cut a target"
        closing = ""
    else:
        allot = (
            f"Spread the target length of {seconds} seconds over the cuts in the plan (the targets sum to {seconds})"
        )
        closing = "The closing cut is elastic, 10–30 seconds (it absorbs the other cuts' stretch). "
    length_rule = f"""- Length is set by the amount of speech; there is no write-measure-revise loop. {allot},
  then turn target seconds into sentence counts: one speech sentence (one `@` line) ≈ 5 seconds (25–30 characters), so a cut's sentences = target seconds ÷ 5 (write `(target seconds · N sentences)` on the plan line).
  Write that many sentences in the cut — long videos tend to run short on sentences (eyeballed seconds read longer than they are). Tie at least one screen change (an element entering, a
  state change, a picture swap) to every sentence. {closing}Right after the last speech line of each cut's timeline (before the transition), note the sentence count and the
  estimated seconds: `# speech N sentences ~M s`.
- If the request hands over a script to read aloud (verbatim), use its sentences as the speech without changing a character, and derive the target seconds from the script's
  amount (do not add or cut sentences to meet the target length). In that case write `{VERBATIM_MARK}` as the first line of the plan."""
    return f"""You are the author of this video. You build the video in the user request below from scratch. Write the script (the narration)
yourself from the request (if the request carries a script or on-screen wording, use it as is). Build it out to the motion and the sound
(BGM, entrance sound effects). The bar is the density and hierarchy of an explainer video a professional studio could ship.

Write the plan and the root first, then the cuts in the plan's order, top to bottom, in one pass. Another process starts checking and
rendering each cut as soon as it is written, so never go back and revise while writing. Each cut is finished afterwards by its own staff.

The mechanics of draft src (facts of the machine):
- The screen is {aspect} — the root canvas is `canvas {canvas}` (do not copy a sample's canvas; decide positions and sizes for this screen).
- The root holds the video-wide settings (palette / font / fonts / photo_style / cut defaults / subtitle / bgm / cast / transition= / read / layers that span cuts).
- A named definition (def, motion, run, svg, sound, image, cue) is written in the design of the cut that first uses it (right after
  `section#name`) — later cuts can use the name (never define the same name twice, and never define it in a cut later than its first use).
- Do not write `out:` or `end`-based keys on a root (`.sticky`) layer (rendering stalls until the closing cut arrives).
- Prefix element names with the cut's name (in cut `hook`: `hook_t`, `hook_img`). Except the root's elements, never reuse a name across cuts.
- Image generation does not keep eras, shapes or counts straight; a description with two scenes becomes a stacked two-picture composite. To draw the same thing in two or more pictures, put
  `image name = "…"` in the root and derive each picture with `[ref:@name]`. Nobody gets to look at the generated pictures, so clear the spot where text goes with `subject:` / `room:`.
{length_rule}
{editable_note()}{editable_author_note(referenced=bool(reference))}Output shape (write nothing but this shape — no preamble, no explanations, no code fences, no headings; every `=== … ===` line starts at column 0):
=== plan ===
name: what this cut shows and how it moves (target seconds · N sentences)      ← one line per cut; names are lowercase ASCII; the cuts run in this order
=== root_design ===
everything in design.txt before `section#` (from `#v2`)
=== root_timeline ===
everything in timeline.txt before `***` (`#v2`, cast, transition=, read)
=== cut name ===
section#name(…)            ← this cut's design lines (indent 0; two-space indent is for children only). Definitions first used in this cut go right after this line
…
---timeline---
*** name                    ← this cut's timeline block (speech, marks, se, the transition on the last line)
…
# speech N sentences ~M s          ← right after the last speech line
transition …
=== cut next-name ===
…
=== end ===

Write the root and the cuts from scratch (the scaffold is only the first line and the screen):
--- design.txt ---
#v2
canvas {canvas}
--- timeline.txt ---
#v2
{samples}{reference}{speech}{request}
User settings: aspect {aspect} ({canvas}) · target length {"not specified" if seconds == AUTO_SECONDS else f"{seconds} seconds"}
"""


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
{editable_note()}{reference_note}
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


# 長さの指定なし (おまかせ) の params の秒 — 著者が長さを決め、尺の指摘は著者の目標秒だけを見る (締めの弾性なし)
AUTO_SECONDS = "auto"
# 依頼の台本をそのまま読む (逐語) と著者が判じた時に plan の最初の行に書く注記 — 尺の指摘を掛けない (文の足し引きが内容の改変になる)
VERBATIM_MARK = "# script: verbatim from the request"
# 依頼文が逐語の読み上げを求める強い言い回し (著者の注記と並ぶ 2 つ目の合図)。依頼はユーザーの言語のまま来るので日本語も見る
VERBATIM_REQUEST = re.compile(
    r"そのまま(?:読み上げ|読んで|読む|使って|ナレーション)|一字一句|原文のまま|台本(?:どおり|通り)|原稿(?:どおり|通り)"
    r"|verbatim|word for word|read (?:it |this )?(?:aloud )?as[- ]is"
)


def is_verbatim(plan: str, request: str) -> bool:
    """依頼の台本をそのまま読む動画か — 著者が plan に逐語の注記を書いた・依頼文が逐語の読み上げを求める言い回しを含む。"""
    return VERBATIM_MARK in plan or VERBATIM_REQUEST.search(request) is not None


# 台詞の尺の指摘 (orchestrator の stage が check の見積りと plan の目標秒から出す — `stream_run.Run.length_finding`)。直し役はこの
# 指摘がある時だけ台詞の行を文ごと消す / 足してよい
LENGTH_RULE = "cut_length"
# 著者が cut の timeline の最後の台詞の次に書く、文の数と台詞を読む秒の目安の注記 (`# speech N sentences ~M s`)。旧形 (台詞) も受ける
DECLARED_SECONDS = re.compile(r"^#\s*(?:speech|台詞)[^\n]*?[~〜約]\s*(\d+(?:\.\d+)?)\s*(?:s|秒)", re.M)


def editable_note() -> str:
    """編集可能モード (env NOLANG_STUDIO_PROFILE=editable・stream_make.sh --editable) の作法の節。著者・担当・直し役の
    prompt に同じ節を入れる — 投入の門 (intake) が同じ規則 (`editable_*`) を DEFECT にするので、書く前に守る方が速い。
    閾値の正本は server の台帳 (`GET drafts/rules/` の profiles.editable) — この文は既定値を写した作法。"""
    if os.environ.get("NOLANG_STUDIO_PROFILE") != "editable":
        return ""
    return """
Editable mode (the user will adjust this video themselves in the editor — write only inside the editable vocabulary. Breaking
it turns the submission into a DEFECT `editable_*`: the cut loses time in fix round-trips, or its motion is mechanically replaced with a fade):
- At most 25 elements per cut (×N counts as N). Fold information into one card (×N items, bullet rows) (add cuts only while planning — never split a cut during fixes).
- At most 2 word-bound state changes (`[!…]` `[=…]`) per cut — spend them on one hero emphasis and one still split (standing-figure expression and pose switches do not count).
- Do not use group / camera / svg / counting numbers (`[count:]`). Partial color / size `{tok}` runs, and `.sticky` layers
  that persist across cuts (a standing band, a logo card), are fine (a run cannot be the target of a word mark `[!…]`).
- Write motion only in these forms (positive examples — they are enough for a good screen):
  `in: fade`, `in: pop`, `in:{y:40, opacity:0, duration:.5}`, `in:{x:-40, opacity:0, duration:.4, ease:'power2.out'}`,
  `out: fade`, `out:{opacity:0, duration:.3}`; a picture's ambient is `main: kb {scale: [1, 1.06]}`; a card's or text's
  ambient is `main: float` (a gentle bob); a diagram's ambient is `main: pulse`.
  Forms that cannot be used (the gate rejects them and the cut is delayed): `keys(at=…)` keyframe rows, `path:`, ambient motions other than float / pulse (`main: sway`, per-glyph `wave`, …),
  filter tweens, and coefficient easings like `ease:'back.out(1.7)'` (word easings only).
- At most 3 fonts; one box-shadow, reused through a def (default to flat boards). Align text sizes to three tiers — heading / body / card — with defs.
- When the user picked a reference video, the quantity lines above relax to what the reference uses — copy the reference's
  root and persistent layers (frames, logo cards, mascots, the subtitle box) as they are (see "the shape the user chose" below).
"""


def editable_author_note(*, referenced: bool = False) -> str:
    """著者だけに足す editable の段取り (設計を軽くして plan を早く出す) — stream は plan が早いほど再生開始が早い。referenced =
    参照の動画がある run — 根と cut の型は参照から写すので、定型の根・画面の段は言わない (参照の型より定型が勝つため)。"""
    if os.environ.get("NOLANG_STUDIO_PROFILE") != "editable":
        return ""
    if referenced:
        return """
Editable-mode flow (with a reference — plan first):
- No long deliberation up front — put out the plan and the root first. Copy the reference's root (palette, font, defs, subtitle, persistent layers) as it is.
- Pick each cut's screen from the reference's cut shapes (cover, case, point, wrap-up, …) and fill it with the request's content. Keep the reference's order and scene shapes.
"""
    return """
Editable-mode flow (light design — plan first):
- No long deliberation up front — put out the plan and the root first, and decide cuts as you write. The root may be a minimal design system decided on the spot:
  2–3 palette colors, 1–2 fonts, text-tier defs (heading / body / card) and one card def. Do not build an ornate root (texture layers, multi-tier defs).
- Pick each cut's screen from the stock shapes: "heading + card (or diagram) + one emphasis", "full-bleed picture + a band card", "hero number + a footnote" —
  this tier is enough, and it stays in a shape the user can move in the editor.
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
    """担当・直し役への参照の注記 (src は渡さない — 根は著者が参照から写した物)。"""
    ref = reference_of(project)
    if ref is None:
        return ""
    return (
        f'\nThis video is built on the shape of the reference video the user chose, "{ref["title"]}" (its root palette / font /'
        " defs and its cut lineup) — keep the root design system and the shapes of the cut lineup. Do not bring speech or"
        " wording over from the reference.\n"
    )


def _numbered(text: str) -> str:
    return "\n".join(f"{k}| {line}" for k, line in enumerate(text.rstrip("\n").split("\n"), start=1))


# 見直しの静止画で絵の説明文を変えてよい時。作り直しは再生を待たせるので、文脈を取り違えさせる誤りだけ (些細な違いは放置)
PICTURE_FIX_NOTE = """Serious picture errors (judge from the images, and only then fix a picture): when a picture makes the speech or the explanation
misleading — it reads as a different thing than what is being explained (a sphere reads as an atom model; the map shows another country), a number or
shape the story hinges on is wrong (the number of holes, an arrow's direction, a graph's rise or fall), it contradicts the speech (person, era, place,
event), or an overlaid figure (ring, arrow, marker) does not sit on its target. Pick one fix: (a) rewrite that img's description (state the shapes and
counts plainly, and say that nothing outside the description is drawn) (b) for geometric / schematic subjects (spheres, rings, curved surfaces, graphs,
diagrams) drop the generated image and redraw it as a shape / svg figure (c) when the root `image` (a reused picture) is wrong, leave the root alone and
replace this cut's `content: @name` with an img described for this cut only.
Leave small differences alone (style, color cast, details, framing, not quite as imagined) — remaking a picture makes playback wait. When you fix a
picture, prefix that `=== look ===` line with `picture:`. Do not judge the content of pictures annotated "still generating (placeholder)".
"""


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
    reference_note: str = "",
) -> str:
    """own_root = この cut が根の持ち主 (動画の最初の live な cut・根が流れる前) — 根の 2 block も直せる (`@ root_design 行`)。他の cut
    の直し役は根と前の cut の定義を変えない (参考として見るだけ)。review = 見直し (厳しい監督として指摘に出ない弱い所・崩れも探す・
    指摘が無くても呼ぶ)。
    shots = 見直しに見せる静止画の名 (無ければ block を読んで描いた姿を想像させる)。"""
    if own_root:
        root_part = f"""Root (this cut's property — you may fix it, but never change the image / cast / read / photo_style / prompt_tail / art / canvas lines, or the names of named definitions):
=== root_design ===
{_numbered(root_d)}
=== root_timeline ===
{_numbered(root_t)}
"""
        where = "`@ line-number` is a line of the cut's block; root lines are `@ root_design line-number` / `@ root_timeline line-number`"
    else:
        root_part = f"""Root (reference — do not change it; avoid a finding on a root line by editing this cut's lines):
=== root_design ===
{root_d}
=== root_timeline ===
{root_t}
"""
        where = "`@ line-number` is a line of the cut's block only (the root and earlier cuts cannot be changed — if an earlier cut's definition does not fit, define your own under a new name in this block and use that)"
    defs = (
        f"Definitions from earlier cuts (reference — do not change them; you may use them):\n{defs_before}\n"
        if defs_before.strip()
        else ""
    )
    trim = ""
    if f" {LENGTH_RULE} " in findings:
        trim = (
            f"Only because the findings include {LENGTH_RULE} (the speech length missed the cut's target) you may delete whole speech lines (`@` lines)"
            " sentence by sentence, or add new one-sentence lines (never change the characters of the lines you keep; do not meet the target with fast"
            " talking, `[speed:]`, or packed `[silence:]`). Delete supporting sentences first (keep numbers and conclusions). For elements a deleted"
            " line's marks brought in, move the marks to a kept line's word or delete the element too. An added sentence must continue the surrounding"
            " speech, and its words must bring in at least one new element or state change (a card, a diagram, a picture swap) — do not leave the screen"
            ' still during an added sentence. Do not settle an added sentence\'s picture for "a title + a photo" — make a conclusion card or a state'
            " change the hero (no idle chapter-opening beat).\n"
        )
    look = ""
    if review or shots:
        if shots:
            names = "・".join(shots)
            intro = (
                f"The images are stills of this cut drawn by the production renderer ({names}; times run from the cut's head. Footage and standing"
                " figures are frozen, mouths closed, and the transition window is not shown). Apart from check's findings, look at each image as a"
                " strict motion director, and "
            )
        else:
            intro = "Apart from check's findings, read the block as a strict motion director, imagine the rendered result, and "
        kept = (
            'the speech characters stay unchanged; picture descriptions only for a "serious picture error" below'
            if shots
            else "only the speech characters and the picture descriptions stay unchanged"
        )
        look = f"""
{intro}hunt for what is weak or broken for a professional explainer video, and fix it.
You may rearrange the layout substantially (replace, add and delete lines; {kept}{" — the length finding's sentence deletions / additions work as above" if trim else ""}).
{PICTURE_FIX_NOTE if shots else ""}First write what you found in `=== look ===`, one line each (or "none"), then write the edits. If there is nothing to fix, put `=== end ===` right after `=== edits ===`.
"""
    head = (
        f"check flagged cut `{name}`'s block. "
        if findings.strip() or not look
        else f"Review cut `{name}`'s block and fix anything broken (check has no findings). "
    )
    pictures = (
        'the picture descriptions only for a "serious picture error" (an img line\'s content; its declaration may be fixed, and adding pictures is fine)'
        if shots
        else "the picture descriptions (an img line's content; its declaration may be fixed, and adding pictures is fine)"
    )
    return f"""{head}Return only the lines you fix (do not rewrite the whole block — writing time is playback wait). Do not change other cuts. No preamble{" (`=== look ===` is still written)" if look else ""}.
Things that stay unchanged (the voice and the pictures are already being made — changing them forces a redo and the playback waits): the speech characters (an `@` line's characters excluding the marks `[…]`; marks may move) and {pictures}.
Do not make it worse (the common shapes of fixes that should not have happened): keep the title, the heading and the first card showing from the cut's head (do not delay them with a mark — do not leave the cut's head background-only); do not split a subtitle mid-sentence; do not reduce a card's or diagram's wording, items or numbers; do not cover a person's face with a card or title; do not split the cut (never add or change `section#` and `***` headings).
{editable_note()}{reference_note}{trim}Format:
=== edits ===
@ line-number
the line's new content (it may span several lines; to delete the line, leave it empty and move to the next `@`)
@ line-number
…
=== end ===
{where}. To append after the block's last line, use `@ last-line-number+1`. Line numbers are the `N|` ones below (a finding's file:line counts design.txt / timeline.txt with the root first — a different numbering). `N|` is the number, not part of the line.
So the fix does not create a new defect: a variant used by a mark (`[!#name .tag]`) must have its `#name.tag(…)` line in the design; `size=` is for text and icons only (boxes take w= / h=);
keep one element per line (do not break an element's line in the middle; an indented child sits right under its parent).
{look}check's findings (with file:line and the fix):
{findings or "none"}

{root_part}{defs}
The block to fix:
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
    return re.sub(r"\s", "", _without_marks(_SPEAKER.sub("", line, count=1)))


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


SPEAKER = re.compile(r"^@([^\s:|.@]+)[.:]")


def fallback_root_timeline(cut_block: str) -> str:
    """著者が `=== root_timeline ===` を書き落とした時の根の timeline: 最初の cut の台詞の話者 (`@名:`) を既定のナレーターの声で
    宣言するだけ (声の解決は後段)。無いと根が組めず全 cut が落ちる (10-25 cinematic の実走)。"""
    names = list(dict.fromkeys(m.group(1) for line in cut_block.splitlines() if (m := SPEAKER.match(line.strip()))))
    return "#v2\n" + "".join(f'cast {name} = "ナレーター"\n' for name in names or ["n"])


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
        secs = re.findall(r"\((\d+(?:\.\d+)?)", l)  # 目標秒は行の最後の `(数` (見せ物の中の `(3 つ` を秒と読まない)
        out.append((name, float(secs[-1]) if secs else 10.0))
    return out


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

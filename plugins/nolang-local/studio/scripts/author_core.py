"""著者 3 役 (著者・担当・直し役) の prompt と出力の読みの共有実装 — 製品と skill の bench の 1 本の正本。

正本はこの 1 枚 (repo 内に写しは置かない)。`agent_client/scripts/` の script は repo 内ではこの file を importlib の file 読みで
import し (package init を通らない)、nolang-agent への sync が配布 bundle の scripts の隣に同梱する。bundle は repo の外で
単体で動くので、この file は標準 library だけに依存する。

文書 (spec.md・looks.md …) と見本 (samples/) は正本 1 式の dir (`libs/ai/llm_prompts/draft_author/reference/` — 配布 bundle
では scripts の隣の `reference/`) を引数に取って読み、連結する文書の集合と順は同 dir の `contract.json` の `compose` が決める
(文書の集合が変わっても古い client が新しい bundle を正しく組めるよう、組み立ては data 側に置く)。製品は
`skill_docs.REFERENCE_DIR`、skill の bench は `stream_author.py` が自分の場所から解決した dir を渡す。製品だけの物 (製品の
追記 `PRODUCT_RULES`・LLM message の組み立て) は libs の他の module、skill だけの物 (claude CLI の呼び出し・担当の prompt・
台詞や絵の復元) は `stream_author.py` に置く。
"""

from __future__ import annotations

import difflib
import functools
import hashlib
import json
import re
import unicodedata
from collections.abc import Callable, Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, TypeGuard

# ===== 文書の置き場 =====


def resolve_reference_dir(scripts_dir: Path) -> Path:
    """文書一式 (contract.json・spec.md・samples/ …) の dir — 配布 bundle では scripts の隣の `reference/`、repo 内では
    libs の正本 (`libs/ai/llm_prompts/draft_author/reference/`) を上へ辿って見つける。"""
    local = scripts_dir.parent / "reference"
    if (local / "contract.json").is_file():
        return local
    for parent in scripts_dir.parents:
        candidate = parent / "libs" / "ai" / "llm_prompts" / "draft_author" / "reference"
        if (candidate / "contract.json").is_file():
            return candidate
    raise FileNotFoundError(f"reference/ (contract.json) が {local} にも repo の libs にも無い")


# ===== 文書一式の版 (server の配信・client の照合・nolang-agent の sync が同じ範囲と指紋を使う) =====


def _is_json_object(value: object) -> TypeGuard[dict[str, object]]:
    return isinstance(value, dict)


def read_contract_json(reference_dir: Path) -> dict[str, object]:
    raw: object = json.loads((reference_dir / "contract.json").read_text(encoding="utf-8"))
    if not _is_json_object(raw):
        raise ValueError("contract.json: object でない")
    return raw


def reference_files(reference_dir: Path) -> tuple[str, ...]:
    """束に入る file の相対 path (昇順) — contract.json の `reference` の列 (`/` で終わる行は dir の中の全 file・`.` で始まる物と
    `__pycache__` は除く)。"""
    manifest = read_contract_json(reference_dir).get("reference")
    if not _is_json_array(manifest) or not all(isinstance(row, str) for row in manifest):
        raise ValueError("contract.json: reference が文字列の列でない")
    paths: set[str] = set()
    for row in (str(row) for row in manifest):
        target = reference_dir / row.rstrip("/")
        if row.endswith("/"):
            if not target.is_dir():
                raise FileNotFoundError(f"contract.json の reference の dir が無い: {row}")
            for path in target.rglob("*"):
                rel = path.relative_to(reference_dir)
                if path.is_file() and not any(part.startswith(".") or part == "__pycache__" for part in rel.parts):
                    paths.add(rel.as_posix())
        else:
            if not target.is_file():
                raise FileNotFoundError(f"contract.json の reference の file が無い: {row}")
            paths.add(row)
    return tuple(sorted(paths))


def reference_hash_of(reference_dir: Path) -> str:
    """文書一式の内容の指紋: sha256( Σ_{path の昇順} "{path}\\0{sha256(内容)}\\n" ) の hex。path は reference/ からの相対の POSIX
    表記で ASCII だけ。nolang-agent の sync (Node) も同じ算法 — 変える時は test vector
    (`libs/tests/ai/llm_core/test_draft_reference_bundle.py`) ごと揃える。"""
    digest = hashlib.sha256()
    for rel in reference_files(reference_dir):
        content = hashlib.sha256((reference_dir / rel).read_bytes()).hexdigest()
        digest.update(f"{rel}\0{content}\n".encode())
    return digest.hexdigest()


def doc_hashes_of(reference_dir: Path) -> dict[str, str]:
    """manifest の項目ごとの内容の指紋 (hex の先頭 12 文字) — 全体の指紋がずれた client が「どの文書が変わったか」を知り、
    変わった文書だけを server の現行で読み直すための物。file の行はその内容の sha256、dir の行 (`samples/`) は中の file で
    `reference_hash_of` と同じ算法。nolang-agent の sync (Node) も同じ算法 — 変える時は test vector ごと揃える。"""
    manifest = read_contract_json(reference_dir).get("reference")
    if not _is_json_array(manifest) or not all(isinstance(row, str) for row in manifest):
        raise ValueError("contract.json: reference が文字列の列でない")
    files = reference_files(reference_dir)
    out: dict[str, str] = {}
    for row in (str(row) for row in manifest):
        if row.endswith("/"):
            digest = hashlib.sha256()
            for rel in (rel for rel in files if rel.startswith(row)):
                content = hashlib.sha256((reference_dir / rel).read_bytes()).hexdigest()
                digest.update(f"{rel}\0{content}\n".encode())
            out[row] = digest.hexdigest()[:12]
        else:
            out[row] = hashlib.sha256((reference_dir / row).read_bytes()).hexdigest()[:12]
    return out


# ===== 見本の選び方 =====

# 自分の type の見本が足りない時に借りる近い type と、prompt に同梱する見本 1 本の大きさの上限 (超える物は選ばない)
NEAR_TYPE = {"cinematic": "story", "compare": "concept", "data": "compare", "story": "cinematic", "concept": "compare"}
SAMPLE_MAX_BYTES = 70_000
# 題の語: 漢字・片仮名の続き 2 字以上 (`カゴ落` `麻辣湯` のように混ざって良い)・英字で始まる英数 3 字以上。平仮名だけの語は数えない
# (「きている」「れない」のような活用の切れ端が題の語になる) — 1 字の漢字と助詞も数えない
TOPIC_WORD = re.compile(r"[一-鿿々゠-ヿー]{2,}|[A-Za-z][A-Za-z0-9]{2,}")


def sample_head(samples_dir: Path, name: str) -> str:
    """見本の 1 行目 `# type · 題 (注記) — canvas WxH`。"""
    return (samples_dir / name).read_text(encoding="utf-8").split("\n", 1)[0]


def sample_portrait(samples_dir: Path, name: str) -> bool:
    """見本が縦か (1 行目の `— canvas WxH` で幅 < 高さ)。"""
    m = re.search(r"— canvas (\d+)x(\d+)", sample_head(samples_dir, name))
    return bool(m) and int(m[1]) < int(m[2])


def sample_topic_words(samples_dir: Path, name: str) -> list[str]:
    """見本の 1 行目 `# type · 題 (注記) — canvas …` の題の語。hf の写しは英字の slug (`black-tire`) を除き、注記の `— ` の後の
    和文の題 (`タイヤが黒い理由`) を足す。NoLang の見本の注記 (`縦・台本そのまま・絵本調`) は題でないので読まない。"""
    head = sample_head(samples_dir, name).split(" · ", 1)[-1].split(" — canvas", 1)[0]
    m = re.fullmatch(r"(.*?)\s*\((.*)\)\s*", head)
    title, note = m.groups() if m else (head, "")
    parts = [
        p.split("・", 1)[0] for p in title.split(" — ") + note.split(" — ")[1:] if not re.fullmatch(r"[a-z0-9-]+", p)
    ]
    return sorted({w for p in parts for w in TOPIC_WORD.findall(unicodedata.normalize("NFKC", p))})


def same_topic(samples_dir: Path, name: str, request: str) -> bool:
    """見本が依頼と同じ題材か: 題の語の半分以上が依頼にあり、それが 2 語以上か 3 字以上の語を含む (「解説」「紹介」のような
    2 字の語 1 つだけの一致は曖昧なので同じ題材と見ない)。著者は見本を逐語で写すので、同じ題材の見本は渡さない。"""
    words = sample_topic_words(samples_dir, name)
    req = unicodedata.normalize("NFKC", request).lower()
    hit = [w for w in words if w.lower() in req]
    return 2 * len(hit) >= len(words) > 0 and (len(hit) >= 2 or any(len(w) >= 3 for w in hit))


def pick_samples(
    samples_dir: Path, typ: str, request: str, *, portrait: bool, editable: bool
) -> tuple[tuple[str, str], list[str]]:
    """見本 2 本 → ((見本 2 本), 同じ題材で外した物)。editable は editable 準拠の見本 (`editable_*.md`・type の合う物を先に・
    足りなければ hf の写しへ)、それ以外は hf の写し `hf_<type>_*.md` (足りなければ近い type)。依頼と同じ題材の物を外し、依頼と
    同じ向き (canvas の縦横) の物を先に。その中の順番は file 名順 (大きさ順だと見本を 1 行直すたびに選ばれる物が替わる)。"""

    def names_of(pattern: str) -> list[str]:
        return sorted(
            p.name
            for p in samples_dir.iterdir()
            if re.fullmatch(pattern, p.name) and p.stat().st_size <= SAMPLE_MAX_BYTES
        )

    skipped: list[str] = []
    if editable:
        # hf の見本は keys / group / count を多用していて、著者が違反を写す (bench 10-25 の違反 19〜37/run の根)
        names = names_of(r"editable_.+\.md")
        same = [n for n in names if same_topic(samples_dir, n, request)]
        skipped.extend(same)
        rest = [n for n in names if n not in same]
        by_type = [n for t in (typ, NEAR_TYPE[typ]) for n in rest if n.startswith(f"editable_{t}_")]
        ordered = by_type + [n for n in rest if n not in by_type]
        picked = sorted(
            ordered, key=lambda n: (ordered.index(n) >= len(by_type), sample_portrait(samples_dir, n) != portrait)
        )[:2]
        if len(picked) == 2:
            return (picked[0], picked[1]), skipped
        skipped = []  # editable の見本が足りない時だけ hf へ (無言で違反の見本に落ちるより良い)
    hf: list[str] = []
    for t in (typ, NEAR_TYPE[typ]):
        names = names_of(rf"hf_{t}_.+\.md")
        same = [n for n in names if same_topic(samples_dir, n, request)]
        skipped.extend(same)
        hf += [n for n in names if n not in same]
    hf = sorted(hf, key=lambda n: sample_portrait(samples_dir, n) != portrait)[:2]
    if len(hf) < 2:
        raise ValueError(f"reference/samples/ に {typ} ({NEAR_TYPE[typ]}) の見本が 2 本無い: {hf}")
    return (hf[0], hf[1]), skipped


def samples_text(samples_dir: Path, samples: tuple[str, ...]) -> str:
    """見本の本文 (著者の user turn の先頭 block — 著者と直し役が同じ物を置き、prompt cache を共有する)。"""
    return "".join(
        f"\n<!-- ===== sample reference/samples/{name} ===== -->\n\n" + (samples_dir / name).read_text(encoding="utf-8")
        for name in samples
    )


# ===== 3 役の system prompt (skill の文書) =====

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
# 3 役に渡す文書の集合と連結順は reference/contract.json の `compose` (`mode:file` の列)。mode は組み方: spec = 文法の正本を
# そのまま・traps = 罠の節から後ろ・sounds = 道具の節を落とす・raw = そのまま・craft = 制作の作法の前置き付き


def _is_json_array(value: object) -> TypeGuard[list[object]]:
    return isinstance(value, list)


@functools.cache
def compose_entries(reference_dir: Path) -> tuple[tuple[str, str], ...]:
    """contract.json の compose — (mode, file) の列。"""
    raw: dict[str, object] = json.loads((reference_dir / "contract.json").read_text(encoding="utf-8"))
    items = raw.get("compose")
    if not _is_json_array(items):
        raise ValueError("contract.json: compose が無い")
    entries: list[tuple[str, str]] = []
    for row in items:
        if not isinstance(row, str) or ":" not in row:
            raise ValueError(f"contract.json: compose の行が mode:file でない: {row!r}")
        mode, _, name = row.partition(":")
        entries.append((mode, name))
    return tuple(entries)


@functools.cache
def system_docs_text(reference_dir: Path, samples: tuple[str, ...] = ()) -> str:
    """文書の system prompt: 役の冒頭 + contract.json の compose 順の文書 (spec の文法 + looks の罠 + sounds + authoring +
    capabilities + 制作の作法) (+ 見本 — 道具の無い call は file を読めないので全部同梱)。samples=() は見本なし (著者の静的な
    system prompt — 見本は題材ごとに変わるので system に置くと cache miss になり、user turn に置く)。製品はこの後ろに追記
    (`product.PRODUCT_RULES`) を足す。"""
    parts = [SYSTEM_HEAD]
    for mode, name in compose_entries(reference_dir):
        text = (reference_dir / name).read_text(encoding="utf-8")
        if mode == "spec":
            parts.append("\n<!-- ===== how to write draft src ===== -->\n\n" + text)
        elif mode == "traps":
            parts.append(
                f"\n<!-- ===== reference/{name} (traps) ===== -->\n\n## Beyond the grammar (traps)"
                + text.split("## Beyond the grammar (traps)", 1)[1]
            )
        elif mode == "sounds":
            # 道具の節 (listen / engine の聴き比べ) は落とす — 3 役は command を打てない (SYSTEM_HEAD と矛盾する)
            text = re.sub(r"(?ms)^## (?:BGM: listen to candidates|Listening check).*?(?=^## |\Z)", "", text)
            parts.append(f"\n<!-- ===== reference/{name} ===== -->\n\n" + text)
        elif mode == "raw":
            parts.append(f"\n<!-- ===== reference/{name} ===== -->\n\n" + text)
        elif mode == "craft":
            parts.append("\n<!-- ===== production craft ===== -->\n\n" + CRAFT_HEAD + text)
        else:
            raise ValueError(f"contract.json: 知らない compose mode {mode!r} — この script が文書より古い")
    parts.append(samples_text(reference_dir / "samples", samples))
    return "".join(parts)


# ===== 著者の user turn =====

# 長さの指定なし (おまかせ) の秒 — 著者が長さを決め、尺の指摘は著者の目標秒だけを見る (締めの弾性なし)
AUTO_SECONDS = "auto"
# 依頼の台本をそのまま読む (逐語) と著者が判じた時に plan の最初の行に書く注記 — 尺の指摘を掛けない (文の足し引きが内容の改変になる)
VERBATIM_MARK = "# script: verbatim from the request"
# 依頼文が逐語の読み上げを求める強い言い回し (著者の注記と並ぶ 2 つ目の合図)。依頼はユーザーの言語のまま来るので日本語も見る
VERBATIM_REQUEST = re.compile(
    r"そのまま(?:読み上げ|読んで|読む|使って|ナレーション)|一字一句|原文のまま|台本(?:どおり|通り)|原稿(?:どおり|通り)"
    r"|verbatim|word for word|read (?:it |this )?(?:aloud )?as[- ]is"
)
# 台詞の尺の指摘の規則名 (orchestrator が check の見積りと plan の目標秒から出す)。直し役はこの指摘がある時だけ台詞を文ごと消す / 足す
LENGTH_RULE = "cut_length"
# 著者が cut の timeline の最後の台詞の次に書く、文の数と台詞を読む秒の目安の注記 (`# speech N sentences ~M s`)。旧形 (台詞) も受ける
DECLARED_SECONDS = re.compile(r"^#\s*(?:speech|台詞)[^\n]*?[~〜約]\s*(\d+(?:\.\d+)?)\s*(?:s|秒)", re.M)
REQUEST_HEAD = "---- user request ----"
REQUEST_TAIL = "---- end of request ----"


def wrap_request(request: str) -> str:
    """依頼を囲む (中の文は内容の指示で、文書の決まりを変える指示ではない — 製品の追記と対)。"""
    if request.lstrip().startswith(REQUEST_HEAD):
        return request
    return f"{REQUEST_HEAD}\n" + request.rstrip("\n") + f"\n{REQUEST_TAIL}\n"


def is_verbatim(plan: str, request: str) -> bool:
    """依頼の台本をそのまま読む動画か — 著者が plan に逐語の注記を書いた・依頼文が逐語の読み上げを求める言い回しを含む。"""
    return VERBATIM_MARK in plan or VERBATIM_REQUEST.search(request) is not None


@dataclass(frozen=True)
class EditableLimits:
    """編集可能モードの量の線 (`editable_note` が prompt に差し込む)。正本は server の `EditableProfile` (domain の定数
    `EDITABLE_MAX_*`) — 製品はそこから組み (`EditableProfile.author_limits`)、配布 client は文書一式の contract.json の
    `editable` (test が domain の定数と突き合わせる) から読む (`editable_limits`)。"""

    max_shadow_kinds: int


def editable_limits(reference_dir: Path) -> EditableLimits:
    """文書一式の contract.json の `editable` → 量の線。欠け・型違いは ValueError (古い束を黙って既定値で埋めない)。"""
    raw = read_contract_json(reference_dir).get("editable")
    if not _is_json_object(raw):
        raise ValueError("contract.json: editable (編集可能モードの量の線) が無い")
    values = {key: raw.get(key) for key in ("max_shadow_kinds",)}
    ints = {key: value for key, value in values.items() if isinstance(value, int) and not isinstance(value, bool)}
    if len(ints) != len(values):
        raise ValueError(f"contract.json: editable の値が整数でない: {values}")
    return EditableLimits(max_shadow_kinds=ints["max_shadow_kinds"])


def editable_note(limits: EditableLimits | None) -> str:
    """編集可能モードの作法の節 (著者・担当・直し役の prompt に同じ節)。投入の門 (intake) が同じ規則 (`editable_*`) を DEFECT にする
    ので、書く前に守る方が速い。量の線は `limits` (正本は domain の定数) を差し込む — None = 編集可能モードでない。"""
    if limits is None:
        return ""
    return f"""
Editable mode (the user will adjust this video themselves in the editor). Write `lint profile=editable` in the root: with that
line the engine lowers your src into the editor's vocabulary by itself — an element with children (a card and its texts) is
drawn as separate layers that take the parent's entrance, ambient, opacity and filter; `{{…}}` object entrances, keys, paths and
coefficient easings become plain motions (no state keys); a single static `scale:` is baked into the size. Small visual drift
from that rounding is accepted, so write as you normally would. Only these cannot be rounded and turn the submission into a
DEFECT `editable_*` (the cut loses time in fix round-trips, or the offending mark is mechanically stripped):
- Word-bound state changes are dropped: `[!…]` / `[=…]` marks (except a standing figure's expression / pose switch) and
  `stagger: …,dim` are not drawn in editable mode (they would be state keys), so do not rely on them. Show a change by bringing
  in another element with `[>…]` (a frame, a highlighted copy, the next card); emphasis is static (a `{{tok}}` run, a colored card).
- No group / camera / svg / counting numbers (`[count:]`); no `{{tok}}` run as a mark target; no filter (color) tweens in `in:` / `out:` / `main:`.
- On an element with children, no rotation / `transform: rotate` / `clip-path` / `overflow: hidden` (only a group could draw them over
  the children) — put them on a childless sibling. No static skew / 3D / translate transforms anywhere.
- Cut transitions: `transition fade {{duration: .6}}` / `dissolve {{duration: .3}}` / `wipe {{duration: .6, dir: 'left'}}` / `push` / `slide` / `zoom {{…}}` with `overlap` `zoom` `ease` and a trailing `se=`;
  `fade out,N` at the last cut and `fade in,N` at the first cut's head are fine — no `panel` curtain and no `bars`.
- At most {limits.max_shadow_kinds} box-shadow kind, reused through a def (default to flat boards). Align text sizes to three tiers — heading / body / card — with defs.
- When the user picked a reference video, the shadow line above relaxes to what the reference uses — copy the reference's
  root and persistent layers (frames, logo cards, mascots, the subtitle box) as they are (see "the shape the user chose" below).
"""


def editable_author_note(editable: bool, *, referenced: bool = False) -> str:
    """著者だけに足す editable の段取り (設計を軽くして plan を早く出す — plan が早いほど再生開始が早い)。referenced = 参照の動画が
    ある run — 根と cut の型は参照から写すので、定型の根・画面の段は言わない (参照の型より定型が勝つため)。"""
    if not editable:
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


# 著者 brief (`--author-brief`): 著者は台本 (台詞)・cut ごとの絵コンテ (`#` 1〜3 行)・transition と root だけを書き、
# 絵は cut ごとの担当がゼロから設計する (担当は常に素材も変える)。台詞は著者の版のまま固定 — 声は著者の時点から担当と並列に作る。
# 文言は 10-28 の bench (B′) で検証した版: 1 文 25〜30 字・意味つき palette token・cut を跨ぐ約束は root に書く。
# 決め技の段 (root の transition= を実例で凝る・1 本 1 種・ms はテンポとして変調) は 10-28 の sig3 bench で検証した版
# (Opus 両順 4-1・区間計 42-29。実例なしの sig2 は 2-2-1 で、hf の語彙 (angle・linear()・se の先行) が出なかった) —
# cut の transition 行は root からの逸脱だけ書く。例文は全部 check 緑を確認済み (bars は hex 直書き・se は引用の説明)
AUTHOR_BRIEF_NOTE = (
    "Production note for this run (it narrows the cut shape above): every cut is finished by its own staff, who designs all the"
    " visuals from scratch. For each cut, write only the brief:\n"
    "- the design block is just the `section#name(…)` line — no layers, no named definitions (def / motion / run / svg / sound / image / cue), no `img#`;\n"
    "- the timeline block opens with 1–3 `#` comment lines stating what the cut shows and how it moves (the hero, the support, the"
    " state changes, what picture if any), then the speech lines (`@speaker: …`), then the `# speech N sentences ~C characters ~M s` note, then"
    " the transition line only where this cut's handoff departs from the root default (only you see the whole lineup);\n"
    "- write no marks and no `se` in the cuts.\n"
    "The speech you write is final — the voice is made from your lines as they stand, so keep each sentence 25–30 characters (a"
    " long sentence bloats the length past the target).\n"
    "The plan and the root are still fully yours — write the root as usual (palette / font / fonts / photo_style / cut defaults /"
    " subtitle and bgm / cast / transition= / read / layers that span cuts).\n"
    "The staffs work in parallel and never see each other's cuts, so the root must carry every promise that spans cuts: give"
    " meaning-bearing colors named palette tokens (e.g. `old=` for the legacy side, one token per recurring subject), and when a"
    " cut's brief points at another cut's thing (the opening's …, the earlier …), state its color and shape in that brief.\n"
    "Give the film one signature transition: craft the root `transition=` to the film's mood instead of a plain dissolve, at"
    " the richness of these real moves —\n"
    "- `wipe {duration: .62, dir: 'left', angle: 16, bars: '#1E1B4B,520;#FF4F9A,600;#FFE14D,440'}` (an angled sweep in the"
    " film's own hex colors; a glow is `bars: 'linear(#7ADFD300,#7ADFD3F2@45%,#7ADFD300),180'`);\n"
    "- `slide {duration: .6, dir: 'right', offset: '8%', opacity: 0} se=\"ページをめくる音\" -4dB` or with `drift: 240, dim: .38` (a page turn);\n"
    "- `dissolve {duration: .32, overlap: .32, color: '#0A0F1A', zoom: 1.08}` (rising out of the dark) · `push {duration: .5, dir: 'top'}` · `none {duration: .3}` (hard"
    " documentary cuts).\n"
    "Keep the window 0.3–0.85 s and pick `dir` (`'left'` `'right'` `'top'` `'bottom'`) to fit this film (not every film sweeps left). Every transition sounds its"
    " own `切替音` matched to its motion; to give the film its own transition voice write a family name alone"
    ' (`se="切替音 ポロロン"` for a cheerful film, `キラキラ` elegant, `シュワーン` TV energy, `拍子木` Japanese — sounds.md) and'
    " each transition gets the version of its direction and length, or `se=` with another sound the film needs (a page turn)."
    " A quiet film (cinematic, story, anything the ambience carries) wants silent joins: write `se=none` on the root"
    " `transition=` and let the ambience and the picture carry the cut; sound at most the one turn that deserves it. A whoosh on"
    " every cut of a snowbound cabin is noise, not craft. One kind per film — but play that kind: vary its duration per cut like tempo (a 0.12 s melt on a quick beat, 0.8 on a"
    " slow reveal), drop to `transition cut` on a hard turn, and in a chaptered film punctuate the chapter heads with"
    " `transition panel {duration: .8, color: '$色', label: \"01 原因\", skew: -12}` (a curtain whose label is the chapter card — the chapter's first cut then opens on its content, not on the same heading again;"
    " never the root default or on the last cut).\n"
)


# 尺の換算の 1 文 (1 つの `@` 行・25〜30 字) の秒と、その下の字数の予算 (間込みの台詞の字 / 秒) — どちらも話速 100% での値
# (参照なしの len2 bench で 1 行 4.3 s・指定比 8/10 が ±20% 内)。cast の speed= を掛ける (10-29: speed=150% の参照で 100% のまま
# 数えて 7 本とも参照の実尺の 0.58〜0.71。文の数を直しても参照の短い文 (~14 字) を写すと 1 行 2.3 s で 0.72 — 字数で数える)
SENTENCE_SECONDS_AT_100 = 5.0
CHARS_PER_SECOND_AT_100 = 6


def author_prompt(
    aspect: str,
    seconds: str,
    canvas: str,
    request: str,
    samples: str = "",
    reference: str = "",
    speech: str = "",
    *,
    editable: EditableLimits | None,
    referenced: bool = False,
    brief: bool = False,
) -> str:
    """著者の user turn。構成の型・雛形・数字の規則は渡さない (台本と絵コンテは著者が依頼から決める)。雛形は 1 行目と canvas だけ —
    役の入った雛形 (cut の役・定義済みの段・theme dark) を渡すと部品を写し、暗い地に揃った (10-23)。
    seconds = 長さの目安の秒 (`AUTO_SECONDS` = 指定なし)・canvas = `WxH`・request = 囲んだ依頼・samples = 見本 (製品は prompt cache の
    ため別 block に置き、ここは空)・reference = 依頼の前に置く節 (参照の動画の「ユーザーが選んだ形」)・speech = 持ち込み音声の節・
    referenced = 参照の動画がある run (editable の段取りを参照を写す形にする)。"""
    if seconds == AUTO_SECONDS:
        allot = "No length was specified — decide a length that fits the content and give every cut a target"
        closing = ""
    else:
        allot = (
            f"Spread the target length of {seconds} seconds over the cuts in the plan (the targets sum to {seconds})"
        )
        closing = "The closing cut is elastic, 10–30 seconds (it absorbs the other cuts' stretch). "
    length_rule = f"""- Length is set by the amount of speech; there is no write-measure-revise loop. {allot},
  then turn target seconds into sentence counts: one speech sentence (one `@` line) ≈ {SENTENCE_SECONDS_AT_100:.0f} seconds (25–30 characters) at the cast's speed=100%, so a cut's sentences = target seconds ÷ {SENTENCE_SECONDS_AT_100:.0f} (write `(target seconds · N sentences · ~C characters)` on the plan line, C = target seconds × the characters per second below).
  The budget underneath is characters: ≈ {CHARS_PER_SECOND_AT_100} characters of speech per second at speed=100%, times the cast's `speed=` (speed=150% → {CHARS_PER_SECOND_AT_100 * 1.5:.0f} a second,
  so a 25–30 character sentence takes ≈ {SENTENCE_SECONDS_AT_100 / 1.5:.1f} s). Count a number by its reading (`96票` is きゅうじゅうろっぴょう = 11 characters, `8%` is はちぱーせんと = 7; other text counts as written). Count sentences with the speed of the cast you write, and write more of them when they run shorter than 25 characters.
  Write that many sentences in the cut — long videos tend to run short on sentences (eyeballed seconds read longer than they are). Tie at least one screen change (an element entering, a
  state change, a picture swap) to every sentence. {closing}Right after the last speech line of each cut's timeline (before the transition), note the sentence count and the
  estimated seconds: `# speech N sentences ~C characters ~M s`.
- Pauses the piece needs are not length fitting — plan and write them like speech: a voiceless cut (a chapter card or a title held with no
  narration, 1.5–3 s) is `(2 s · 0 sentences)` on the plan line and `@名: [silence:2s]` in the timeline; a held beat after a question, before a
  reveal or after a number that should sink in is `[silence:0.8s]` inside the cut (its seconds count toward the target). What is banned is bending
  speed or silences after writing to hit the length.
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
{editable_note(editable)}{editable_author_note(editable is not None, referenced=referenced)}Output shape (write nothing but this shape — no preamble, no explanations, no code fences, no headings; every `=== … ===` line starts at column 0):
=== plan ===
name: what this cut shows and how it moves (target seconds · N sentences · ~C characters — 0 for a voiceless cut)      ← one line per cut; names are lowercase ASCII; the cuts run in this order
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
# speech N sentences ~C characters ~M s          ← right after the last speech line
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
{samples}{reference}{speech}{request}{chr(10) + AUTHOR_BRIEF_NOTE if brief else ""}
User settings: aspect {aspect} ({canvas}) · target length {"not specified" if seconds == AUTO_SECONDS else f"{seconds} seconds"}
"""


def plan_names(plan_text: str) -> list[tuple[str, float]]:
    """plan の (cut の名, 目標秒) の列。目標秒は行の最後の `(数` (見せ物の中の `(3 つ` を秒と読まない)・無ければ 10 秒。"""
    out: list[tuple[str, float]] = []
    for line in plan_text.splitlines():
        if ":" not in line or line.startswith("#"):
            continue
        name = line.split(":", 1)[0].strip()
        secs = re.findall(r"\((\d+(?:\.\d+)?)", line)
        out.append((name, float(secs[-1]) if secs else 10.0))
    return out


# ===== 直し役の user turn と出力の読み =====


def reference_role_note(title: str | None) -> str:
    """担当・直し役への参照の注記 (src は渡さない — 根は著者が参照から写した物)。title = 参照の動画の題 (None = 参照なし)。"""
    if title is None:
        return ""
    return (
        f'\nThis video is built on the shape of the reference video the user chose, "{title}" (its root palette / font /'
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
    editable: EditableLimits | None,
) -> str:
    """own_root = この cut が根の持ち主 (動画の最初の live な cut・根が流れる前) — 根の 2 block も直せる (`@ root_design 行`)。他の cut
    の直し役は根と前の cut の定義を変えない (参考として見るだけ)。review = 見直し (厳しい監督として指摘に出ない弱い所・崩れも探す・
    指摘が無くても呼ぶ)。shots = 見直しに見せる静止画の名 (無ければ block を読んで描いた姿を想像させる)。"""
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
            " sentence by sentence (never a voiceless line `@名: [silence:2s]` or a held `[silence:2s]` beat — those pauses are the piece's rhythm, not"
            " length), or add new one-sentence lines (never change the characters of the lines you keep; do not meet the target with fast"
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
{editable_note(editable)}{reference_note}{trim}Format:
=== edits ===
@ line-number
the line's new content (it may span several lines; to delete the line, leave it empty and move to the next `@`)
@ line-number
…
=== end ===
{where}. To append after the block's last line, use `@ last-line-number+1`. Line numbers are the `N|` ones below (a finding's file:line counts design.txt / timeline.txt with the root first — a different numbering). `N|` is the number, not part of the line.
So the fix does not create a new defect: a variant used by a mark (`[!#name .tag]`) must have its `#name.tag(…)` line in the design;
keep one element per line (do not break an element's line in the middle; an indented child sits right under its parent).
{look}check's findings (with file:line and the fix):
{findings or "none"}

{root_part}{defs}
The block to fix:
=== cut {name} ===
{_numbered(block)}
=== end ===
"""


def without_marks(line: str) -> str:
    """台詞の行から印 `[…]` を外す (`[!#c[*] …]` のような入れ子の `]` も 1 つの印として)。"""
    out: list[str] = []
    depth = 0
    for ch in line:
        if ch == "[":
            depth += 1
        elif ch == "]" and depth:
            depth -= 1
        elif not depth:
            out.append(ch)
    return "".join(out).strip()


# 台詞の行の頭 (話者) — `@n:` / `@n.style .tag:` / `@:` / 折り目の `@|` / 持ち込み音声の `@clip id [.tag]` (コロンなし・後ろは原文)
SPEAKER = re.compile(r"^\s*@(?:\||clip\s+\S+(?:\s+\.[a-z][a-z0-9_]*(?!\S))?|[^:\s\[]*(?:\s+\.[a-z][a-z0-9_]*)?:)")
_READING = re.compile(r"\{([^{}|]*)\|[^{}]*\}")  # 読みの指定 `{表記|読み}`
PICTURE_LINE = re.compile(r"^\s*img#\S+\((?:[^()]|\([^()]*\))*\)\s*(.*)$")  # img の行 → 絵の説明文


def spoken(line: str) -> str:
    """台詞の行の声になる文字 — 話者・印 `[…]`・読点 `、。`・読みの指定 (`{表記|読み}` は表記に)・空白を除く。担当と直し役が台詞を
    変えたかの比較はこれで見る (読点の追加と読みの指定は変えた事にしない)。"""
    body = _READING.sub(r"\1", without_marks(SPEAKER.sub("", line, count=1)))
    return re.sub(r"[、。\s]", "", body)


def touched_fixed(before: str, after: str) -> tuple[int, int]:
    """直し役が変えない約束の物 — 台詞の文字 (`spoken`) と絵の説明文 — を変えた数 (記録用)。"""

    def speech(text: str) -> list[str]:
        return [
            spoken(line) for line in text.split("---timeline---", 1)[-1].splitlines() if line.lstrip().startswith("@")
        ]

    def pictures(text: str) -> list[str]:
        return [m.group(1).strip() for line in text.splitlines() if (m := PICTURE_LINE.match(line))]

    sb, sa = speech(before), speech(after)
    pb, pa = pictures(before), pictures(after)
    return sum(a != b for a, b in zip(sb, sa)) + abs(len(sb) - len(sa)), sum(p not in pb for p in pa)


def parse_edits(text: str, blocks: dict[str, str]) -> tuple[dict[str, dict[int, list[str]]] | None, list[str]]:
    """直し役の `=== edits ===` を block ごと (`@ 行番号` = cut・`@ root_design 行番号` …) の行番号 → 新しい中身に読む
    → (edits, 捨てた `@` の行)。`@ 行数+1` は block の末尾に足す edit。知らない block・範囲外の行番号の edit はその 1 つだけ捨てて
    残りを当てる。edits が無い・当てる edit が 1 つも無ければ None。"""
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


def has_empty_edits(text: str) -> bool:
    """直す所が無い (`=== edits ===` の直後に `=== end ===`)。"""
    return re.search(r"===\s*edits\s*===\s*\n\s*===\s*end\s*===", text) is not None


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


def emitted_block(name: str, text: str) -> str | None:
    """block 全体を返した直し役の出力から cut の block を切り出す (見出し無し・fence 付きも受ける)。block が無ければ None。"""
    m = re.search(r"===\s*cut\s+" + re.escape(name) + r"\s*===\s*\n(.*?)(?:\n===\s*end\s*===|\Z)", text, re.S)
    if m:
        body = m.group(1)
    else:
        # 見出し無しで `section#名` から書き始める著者もいる → `=== end ===` と code fence を剥がして全部を block とする
        body = re.sub(r"^\s*```.*$", "", text, flags=re.M)
        body = re.sub(r"===\s*end\s*===.*$", "", body, flags=re.S)
        ms = re.search(r"^section#", body, re.M)
        if ms is None:
            return None
        body = body[ms.start() :]
    body = body.strip("\n") + "\n"
    if "---timeline---" not in body:
        # 印無しで timeline が始まる形も受ける
        mt = re.search(r"^\*\*\* ", body, re.M)
        body = body[: mt.start()] + "---timeline---\n" + body[mt.start() :] if mt else body + "---timeline---\n"
    return body


# cut の名 (`section#名(宣言)` の名は `(` の前まで・`*** 名` の名と同じ文字)
_CUT_NAME = r"[A-Za-z0-9_\-]+"
_CUT_HEAD = re.compile(rf"^(?:section#{_CUT_NAME}|\*\*\*\s+\S+)")


def cut_heads(block: str) -> list[str]:
    """cut の block の見出し (design の `section#名` と timeline の `*** 名` の行) の並び。直し役は cut を分けない・改名しない —
    直す前と違う直しは受け取らない (片方だけ戻ると design と timeline の cut が食い違って組み立てで落ちる)。"""
    return [m.group(0).split("(")[0].strip() for line in block.splitlines() if (m := _CUT_HEAD.match(line))]


# ===== 著者の出力の section 割り =====

_MARK = re.compile(rf"^\s*===\s*(plan|root_design|root_timeline|end|cut\s+({_CUT_NAME}))\s*===\s*$")
_FENCE = re.compile(r"^\s*```")
_CUTHEAD = re.compile(rf"^section#({_CUT_NAME})")
_TLHEAD = re.compile(r"^\*\*\*\s+\S+")
TIMELINE_SEP = "---timeline---"


@dataclass(frozen=True)
class AuthorSection:
    """閉じた section 1 つ。kind = plan / root_design / root_timeline / cut・name = cut の名 (cut だけ)。cut の body は
    design の block + `---timeline---` + timeline の block。"""

    kind: str
    name: str | None
    body: str


class AuthorOutputSplitter:
    """著者の出力 (`author_prompt` の出力の形) の delta を行に組み、section が閉じるたびに on_section を呼ぶ。
    `=== plan ===` / `=== root_design ===` / `=== root_timeline ===` / `=== cut 名 ===` / `=== end ===` の行で割り、見出しを落とした
    cut (`section#名` で始まる block) と `---timeline---` を落とした cut (`*** 名` で timeline が始まる) も受ける。code fence は捨てる。"""

    def __init__(self, on_section: Callable[[AuthorSection], None]) -> None:
        self._on_section = on_section
        self._buf = ""
        self._sec: tuple[str, str | None] | None = None
        self._lines: list[str] = []
        self._sep = False
        self.ended = False  # `=== end ===` を読んだ

    def feed(self, text: str) -> None:
        self._buf += text
        while "\n" in self._buf:
            line, self._buf = self._buf.split("\n", 1)
            self._line(line)

    def finish(self) -> None:
        if self._buf:
            self._line(self._buf)
            self._buf = ""
        self._close()

    def _line(self, line: str) -> None:
        if _FENCE.match(line):
            return
        m = _MARK.match(line)
        if m:
            self._close()
            kind = m.group(1)
            if kind == "end":
                self._sec = None
                self.ended = True
                return
            self._sec = ("cut", m.group(2)) if m.group(2) else (kind, None)
            self._lines, self._sep = [], False
            return
        mc = _CUTHEAD.match(line)
        if mc and (self._sec is None or self._sec[0] != "cut" or self._sec[1] != mc.group(1) or self._sep):
            self._close()
            self._sec, self._lines, self._sep = ("cut", mc.group(1)), [line], False
            return
        if (
            self._sec
            and self._sec[0] == "cut"
            and not self._sep
            and (line.strip() == TIMELINE_SEP or _TLHEAD.match(line))
        ):
            self._sep = True
            self._lines.append(TIMELINE_SEP)
            if line.strip() == TIMELINE_SEP:
                return
        if self._sec:
            self._lines.append(line)

    def _close(self) -> None:
        if not self._sec:
            return
        kind, name = self._sec
        body = "\n".join(self._lines).strip("\n") + "\n"
        if kind == "cut" and TIMELINE_SEP not in body:
            body += TIMELINE_SEP + "\n"
        self._sec, self._lines = None, []
        self._on_section(AuthorSection(kind=kind, name=name, body=body))


_CAST_SPEAKER = re.compile(r"^@([^\s:|.@]+)[.:]")


def fallback_root_timeline(cut_block: str) -> str:
    """著者が `=== root_timeline ===` を書き落とした時の根の timeline: 最初の cut の台詞の話者 (`@名:`) を既定のナレーターの声で
    宣言するだけ (声の解決は後段)。無いと根が組めず全 cut が落ちる (10-25 cinematic の実走)。"""
    names = list(
        dict.fromkeys(m.group(1) for line in cut_block.splitlines() if (m := _CAST_SPEAKER.match(line.strip())))
    )
    return "#v2\n" + "".join(f'cast {name} = "ナレーター"\n' for name in names or ["n"])


# ===== 編集役 (nolang edit — 完成した動画の src を、依頼のぶんだけ書き換える) =====

EDITOR_BRIEF = """\
# The editor

You are the editor of a finished NoLang video. You receive the complete src of a video that already rendered and
shipped — its design.txt and timeline.txt — and a change request from its owner. Honor the request while rewriting as
little as possible: every line you do not touch stays exactly as the owner approved it.

## Output contract

Your whole reply is exactly these parts, in this order, and nothing else — no greetings, no explanations outside part 1:

1. A `VERDICT` section: split the request into its items and give one line per item:
   - `- <short restatement of the item>: patch` — you implement it below.
   - `- <item>: rebuild (<one-line why>)` — the item reshapes the whole video (a target length in seconds, a new
     aspect ratio, converting the overall style, redoing most of the cuts). Such an item is handed to the author
     instead; do not patch it.
   - `- <item>: asset (<one-line why>)` — the change lives inside a generated picture or clip (a face, a pose, what a
     drawing depicts). It is done by regenerating that asset. When the src can express it (an `image` description
     change, or pinning an uploaded file with `id=…`), still patch that line; otherwise emit no patch for it.
   - `- <item>: impossible (<one-line why>)` — the grammar has no way to express it at all. Emit no patch for it.
2. If any item is `patch`, the changed material, each piece in its own fence:
   - ```design-root — the full root of design.txt (everything above the first `section#`), re-emitted verbatim except
     your changes. Only when a root line changes.
   - ```timeline-root — the full head of timeline.txt (everything above the first `***`), same rule.
   - ```cut <name> — the full `section#<name>` block from design.txt, then a separator line containing only `***`,
     then the full `*** <name>` block from timeline.txt (including its `*** <name>` head line). Only for cuts you
     change; re-emit each such cut in full, verbatim except your changes.
   - ```new <name> after <existing-name> — same two-part body, for a cut you insert.
   - ```delete <name> — empty body, removes that cut.

## Rules

- A cut you do not emit stays byte-identical — never re-emit an unchanged cut, never reflow, re-space or "clean up"
  lines the request does not touch.
- The speech is the owner's: change wording only where the request says so. When the request changes a spoken number
  or term, change it everywhere it is spoken and shown, including totals and recaps in later cuts that depend on it.
- Your fences replace the originals wholesale, so each must be complete and self-consistent in the grammar of the
  documents above.
- A change to the root redraws every cut; that is fine — prefer one root change over repeating the same edit in many
  cuts.
- When the request asks for something visual you cannot verify from the src alone (an overlap, a cropped text), fix
  the plausible cause and keep the fix minimal.
"""


def edit_prompt(design: str, timeline: str, request: str) -> str:
    """編集役の user turn: 役の brief + 完成した src の全文 + 依頼。system prompt は 3 役と同じ文書一式 (cache を共有する)。"""
    return (
        EDITOR_BRIEF
        + "\n\nThe finished video's src:\n\n```design.txt\n"
        + design.rstrip("\n")
        + "\n```\n\n```timeline.txt\n"
        + timeline.rstrip("\n")
        + "\n```\n\nThe owner's change request:\n\n"
        + wrap_request(request)
    )


# ===== 編集役の出力の読み (fence の適用) — client の stream_author.py と製品の DraftAuthorRun の共有実装 =====

EDIT_FENCE = re.compile(r"```(design-root|timeline-root|cut \S+|new \S+ after \S+|delete \S+)[ \t]*\n(.*?)```", re.S)
_EDIT_VERDICT = re.compile(r"^[-*] (.+?): (patch|rebuild|asset|impossible)\b(.*)$", re.M)
_EDIT_SEP = re.compile(r"^\*\*\*\s*$", re.M)


@dataclass(frozen=True)
class EditVerdict:
    """VERDICT の 1 行 — item = 依頼の項目の言い直し・verdict = patch / rebuild / asset / impossible・why = 括弧の中。"""

    item: str
    verdict: str
    why: str


def edit_verdicts(reply: str) -> list[EditVerdict]:
    return [
        EditVerdict(item=item.strip(), verdict=verdict, why=why.strip(" ()"))
        for item, verdict, why in _EDIT_VERDICT.findall(reply)
    ]


@dataclass(frozen=True)
class AppliedEdit:
    """編集役の fence を src に当てた結果。根と block は末尾 1 つの改行の正規形・order = 構成の順 (delete 済み)。
    changed は根が変わった時、新規以外の全 cut (根は全 cut に効く — 不変の cut も check を通し直す)。"""

    design_root: str
    design_blocks: dict[str, str]
    timeline_root: str
    timeline_blocks: dict[str, str]
    order: tuple[str, ...]
    changed: tuple[str, ...]
    new: tuple[str, ...]
    deleted: tuple[str, ...]
    root_changed: bool

    @property
    def unchanged(self) -> tuple[str, ...]:
        return tuple(c for c in self.order if c not in self.changed and c not in self.new)

    @property
    def touched(self) -> bool:
        return bool(self.changed or self.new or self.deleted or self.root_changed)

    def cut_block(self, name: str) -> str:
        """cut 1 つの block (design + 区切り + timeline) — 著者の成果物と同じ形。"""
        design = self.design_blocks[name].rstrip("\n")
        return f"{design}\n{TIMELINE_SEP}\n" + self.timeline_blocks[name].rstrip("\n") + "\n"


def _split_src_doc(text: str, head: str) -> tuple[str, dict[str, str], list[str]]:
    """先頭部 (根) と、名 → block (head 行から次の head の前まで)・構成の順を返す。"""
    pat = re.compile(rf"^{head}({_CUT_NAME})", re.M)
    names = [m.group(1) for m in pat.finditer(text)]
    starts = [m.start() for m in pat.finditer(text)] + [len(text)]
    blocks = {names[i]: text[starts[i] : starts[i + 1]].strip("\n") + "\n" for i in range(len(names))}
    return (text[: starts[0]] if names else text), blocks, names


def apply_edit_reply(design: str, timeline: str, reply: str) -> AppliedEdit:
    """編集役の fence を src に当てる。形が壊れていれば ValueError (fence が無い出力は touched が偽の AppliedEdit)。"""
    d_root, d_blocks, order = _split_src_doc(design, r"section#")
    t_root, t_blocks, t_names = _split_src_doc(timeline, r"\*\*\* ")
    if set(order) != set(t_names):
        raise ValueError(f"src の design と timeline の cut が揃わない: {sorted(set(order) ^ set(t_names))}")
    changed: list[str] = []
    new: list[str] = []
    deleted: list[str] = []
    root_changed = False
    for kind, body in EDIT_FENCE.findall(reply):
        if kind == "design-root":
            new_root = body.strip("\n") + "\n"
            root_changed = root_changed or new_root != d_root.strip("\n") + "\n"
            d_root = new_root
            continue
        if kind == "timeline-root":
            new_root = body.strip("\n") + "\n"
            root_changed = root_changed or new_root != t_root.strip("\n") + "\n"
            t_root = new_root
            continue
        name = kind.split()[1]
        if kind.startswith("delete "):
            if name not in order:
                raise ValueError(f"delete {name}: 知らない cut")
            order.remove(name)
            deleted.append(name)
            continue
        m = _EDIT_SEP.search(body)
        if m is None:
            raise ValueError(f"{kind}: design と timeline を分ける *** の行が無い")
        d_part = body[: m.start()].strip("\n") + "\n"
        t_part = body[m.end() :].strip("\n") + "\n"
        if not re.search(rf"^section#{re.escape(name)}\b", d_part, re.M):
            raise ValueError(f"{kind}: design の頭が section#{name} でない")
        if not t_part.startswith(f"*** {name}"):
            raise ValueError(f"{kind}: timeline の頭が *** {name} でない")
        if kind.startswith("cut "):
            if name not in order:
                raise ValueError(f"cut {name}: 知らない cut (新しい cut は `new <名> after <名>`)")
            if d_part != d_blocks[name] or t_part != t_blocks[name]:
                changed.append(name)
            d_blocks[name], t_blocks[name] = d_part, t_part
        else:  # new <name> after <existing>
            after = kind.split()[3]
            if after not in order:
                raise ValueError(f"{kind}: {after} が構成に無い")
            if name in order:
                raise ValueError(f"{kind}: {name} は既にある")
            order.insert(order.index(after) + 1, name)
            d_blocks[name], t_blocks[name] = d_part, t_part
            new.append(name)
    if root_changed:  # 根は全 cut に効く — 不変の cut も check を通し直す (担当は掛けない)
        changed = [c for c in order if c not in new]
    return AppliedEdit(
        design_root=d_root,
        design_blocks=d_blocks,
        timeline_root=t_root,
        timeline_blocks=t_blocks,
        order=tuple(order),
        changed=tuple(changed),
        new=tuple(new),
        deleted=tuple(deleted),
        root_changed=root_changed,
    )


# ===== cut の block の text 操作 (製品の orchestrator と配布 client の stream_run の共有) =====
# 直し役の出力の事後処理・最後の手段・定義の移動・機械の直し。規則は bench の実測で決めた物 (各関数の注記) — 製品と client が同じ
# 実装を通る (片方だけ直すと lane で結果が食い違う)。block = cut の design の block + `---timeline---` + timeline の block。

# cut の block の字下げ無しの行で定義される要素の名 (`img#cl_p(inset: 0; …)`・`kick#cl_k(…)`)。字下げの子は親の名の下に付く
TOP_DEF = re.compile(r"^([A-Za-z][\w-]*)#([A-Za-z0-9_]+)", re.M)
# 自動で改名する名: `_` か数字を含む物 (`cl_p`・`h2`)。`hd` `bar` のような短い名は根の物を意図して書いた事もあるので直し役に任せる
RENAMABLE = re.compile(r"^[a-z]+(?:_[a-z0-9_]+|[0-9][a-z0-9_]*)$")
# grammar の予約 lane と予約語 (domain `RESERVED_LAYER_NAMES` と同じ集合 — domain は libs を import できないので値を持つ。一致は
# `libs/tests/ai/llm_core/test_draft_author_prompts.py` が縛る)。層の名に書くと DEFECT:NAME — 根の 1 行で全 cut が直し役に回ったので
# 機械で改名する
RESERVED_NAMES = frozenset({"bg", "se", "subtitle", "cut", "screen", "self", "prev"})
# cut の block に書ける名のある定義 (grammar の CUT_DEFINITION_ROOTS) — 持ち主はその block の cut。字下げの子の行も定義の一部
_NAMED_DEF = re.compile(r"^(def|svg|sound|image|motion|run|cue)\s+([A-Za-z_][\w-]*)\b")
_DEF_CHILD = re.compile(r"^[ \t]+[A-Za-z_][\w-]*#([A-Za-z_][\w-]*)", re.M)
# 台詞の効果音の説明 (warm の鍵) と、台詞行の印 (効果音の `[♪…]` を除く)
_SE = re.compile(r'\[♪"([^"]+)"')
_MARK_NOT_SE = re.compile(r"\[(?!♪)[^\[\]]*\]")
# svg に焼く箱の行で、焼く絵を変えない宣言 (位置・動き・重なり) と、素材にならない行の tag
_BOX_SKIP = frozenset(
    {"left", "top", "right", "bottom", "cx", "cy", "x", "y", "z-index", "in", "out", "main", "overlap"}
)
_NOT_BOX = frozenset({"p", "h1", "h2", "h3", "h4", "span", "subtitle", "img", "def", "cue"})
_ELEMENT_HEAD = re.compile(r"^[a-z][\w-]*#([\w-]+)\(")  # design の最上位の要素の行 (`p#名(` — 字下げなし)
_ELEMENT_LINE = re.compile(r"^(\s*)[a-z][\w-]*#([\w-]+)")  # design の要素の行 (`  p#名(` — 字下げで親子)


def unquoted_chars(text: str, start: int = 0) -> Iterator[tuple[int, str]]:
    """text[start:] のうち文字列の外の字を (位置, 字) で — 括弧の対応や区切りを数える scanner が文字列の中を見ないために。
    文字列の切り方は tokenize と同じ (`\"\"\"…\"\"\"` は生の本文・`\"…\"` は逃げ `\\x` を 2 字で 1 つ) に、HTML 形の `'…'`
    (GSAP の object の値 `ease: 'power2.out'`・逃げなし) を足した物。閉じない文字列は末尾まで。grammar (`grammar.lexicon`) も
    これを使う (配布 client と同じ 1 本)。"""
    position = start
    while position < len(text):
        char = text[position]
        if text.startswith('"""', position):
            end = text.find('"""', position + 3)
            position = len(text) if end < 0 else end + 3
            continue
        if char in "'\"":
            position += 1
            while position < len(text) and text[position] != char:
                position += 2 if char == '"' and text[position] == "\\" else 1
            position += 1
            continue
        yield position, char
        position += 1


def split_top_level(body: str, sep: str = ";") -> list[str]:
    """body を top-level の sep で割る (括弧 `(){}[]` と quote の中は割らない) — `(宣言)` の中身を宣言ごとに・切替の引数を `,` で。"""
    parts: list[str] = []
    depth = 0
    start = 0
    for k, ch in unquoted_chars(body):
        if ch in "({[":
            depth += 1
        elif ch in ")}]":
            depth -= 1
        elif ch == sep and depth == 0:
            parts.append(body[start:k])
            start = k + 1
    parts.append(body[start:])
    return parts


def split_block(name: str, text: str) -> tuple[str, str] | None:
    """cut の block の text を (design, timeline) に割る。頭の `section#名` を著者が落としていたら補う (落とすとその要素は doc の中で
    前の cut の物になる — s9 03: hook の写真が本体の cut で開いて `~` の継続が割れた)。`---timeline---` が無ければ None。"""
    if TIMELINE_SEP not in text:
        return None
    design, timeline = text.split(TIMELINE_SEP, 1)
    design = design.strip("\n") + "\n"
    if not re.search(r"^section#", design, re.M):
        design = f"section#{name}\n" + design
    return design, timeline.strip("\n") + "\n"


def join_block(design: str, timeline: str) -> str:
    return design + TIMELINE_SEP + "\n" + timeline


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


def def_children(text: str) -> set[str]:
    """名のある定義の字下げの子の名 — 後の cut は実体の子を `実体.子` で参照する。"""
    return set(_DEF_CHILD.findall(text))


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


def add_defs(block: str, text: str) -> str:
    """定義の text を block の design (`section#` の行の次) に足す (既にあればそのまま)。"""
    if not text.strip() or text.strip() in block:
        return block
    m = re.search(r"^section#[^\n]*\n", block, re.M)
    at = m.end() if m else 0
    return block[:at] + text + block[at:]


def rows_naming_layers(text: str, layers: Sequence[str]) -> tuple[set[int], int]:
    """text (cut の block) の中で層の名を指す行 (section の `#名(`・印の `#名`) の 0 始まりの行番号と、見つかった層の数。板の子の層
    (`板._board`) は板の名でも (板の出現の印は `[>#板]`)、×N の実体 (`row[2]`) と子 (`板.k`) は書いた名 (`#row(…) ×2`・字下げの
    `#k`) でも引く。"""
    lines = text.split("\n")
    rows: set[int] = set()
    hit = 0
    for layer in layers:
        owner = layer.split("._")[0]
        leaf = re.sub(r"\[\d+\]", "", owner.rsplit(".", 1)[-1])
        names = {name for name in (layer, owner, leaf) if name and name != "-"}
        if not names:
            continue
        pattern = re.compile(r"#(?:" + "|".join(re.escape(name) for name in names) + r")(?![\w.])")
        found = {k for k, line in enumerate(lines) if pattern.search(line)}
        if found:
            rows |= found
            hit += 1
    return rows, hit


def revert_changed_regions(before: str, after: str, bad: set[int]) -> str | None:
    """after (直し役の出力) のうち、bad (0 始まりの行番号) を含む変更の塊 (before との差分の塊) を before の行に戻した text。bad が
    変更の塊の外にしか無ければ None (直し役の変更が原因ではない)。"""
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


def prune_orphan_elements(before: str, after: str, text: str) -> str:
    """直し役が足した最上位の要素 (before に無く after にある) のうち、after の timeline では印で出していたのに、塊の戻し (text) で
    その印が消えた物の定義 (と残った印) を text から落とす。印を失った要素は cut の頭から末尾まで出っぱなしの層になり、他の文字に
    重なる (10-30 c15 super の learn: レビューが足した台詞の行ごと `[>#learn_q +300]` が戻り、`p#learn_q` だけ残って cut 全体に居座った)。"""

    def parts(s: str) -> tuple[list[str], str]:
        d, _sep, t = s.partition(TIMELINE_SEP)
        return d.split("\n"), t

    def names(lines: list[str]) -> set[str]:
        return {m.group(1) for line in lines if (m := _ELEMENT_HEAD.match(line))}

    def marked(timeline: str, name: str) -> bool:
        return re.search(r"#" + re.escape(name) + r"(?![\w-])", timeline) is not None

    b_design, _ = parts(before)
    a_design, a_timeline = parts(after)
    n_design, n_timeline = parts(text)
    orphans = {n for n in names(a_design) - names(b_design) if marked(a_timeline, n) and not marked(n_timeline, n)}
    if not orphans:
        return text
    out: list[str] = []
    skip = False
    for line in n_design:
        m = _ELEMENT_HEAD.match(line)
        if m is not None:
            skip = m.group(1) in orphans
        elif skip and line.strip() and not line.startswith((" ", "\t")):
            skip = False  # 字下げの子を抜けた
        if not skip:
            out.append(line)
    for n in orphans:  # 残った印 (`[<#名]` 等) — 名を抜き、空になった印を消す
        n_timeline = re.sub(r",?#" + re.escape(n) + r"(?![\w-])[^\],]*", "", n_timeline)
    n_timeline = re.sub(r"\[[>!<=~]\s*\]", "", n_timeline)
    return "\n".join(out) + TIMELINE_SEP + n_timeline


def edit_lines(now: str, fixed: str) -> str:
    """戻した直し役の edit の本文 (`+` = 直し役が書いた行・`-` = 今の行) — 次の直し役に「効かなかった」と見せる。"""
    diff = difflib.unified_diff(now.split("\n"), fixed.split("\n"), lineterm="", n=0)
    return "\n".join(line for line in diff if line[:1] in "+-" and not line.startswith(("---", "+++")))


def block_span(lines: Sequence[str], which: str, cut: str) -> tuple[int, int] | None:
    """doc の design / timeline の行の中で cut の block の [頭の行, 次の cut の頭の行) (1 始まり)。`section#cut` / `*** cut` から次の
    cut の頭まで。無ければ None。"""
    head, nxt = (
        (re.compile(rf"^section#{re.escape(cut)}\b"), re.compile(r"^section#"))
        if which == "design"
        else (re.compile(rf"^\*\*\* {re.escape(cut)}\s*$"), re.compile(r"^\*\*\* "))
    )
    start = next((k for k, line in enumerate(lines, start=1) if head.match(line)), None)
    if start is None:
        return None
    end = next((k for k, line in enumerate(lines[start:], start=start + 1) if nxt.match(line)), len(lines) + 1)
    return start, end


def block_in_doc(design: str, timeline: str, cut: str) -> str | None:
    """doc の中の cut の block を cut の block の形 (design + `---timeline---` + timeline) で。"""
    parts: list[str] = []
    for which, text in (("design", design), ("timeline", timeline)):
        lines = text.split("\n")
        span = block_span(lines, which, cut)
        if span is None:
            return None
        parts.append("\n".join(lines[span[0] - 1 : span[1] - 1]).strip("\n") + "\n")
    return join_block(parts[0], parts[1])


class LocatedDefect(Protocol):
    """check の欠陥の場所 (製品の `grammar.lexicon.Defect`・client の `stream_api.Defect` が満たす)。"""

    @property
    def level(self) -> str: ...

    @property
    def file(self) -> str: ...

    @property
    def line(self) -> int: ...


def drop_defect_lines(
    design: str, timeline: str, cut: str, defects: Sequence[LocatedDefect]
) -> tuple[str, str, list[dict[str, object]]]:
    """doc の DEFECT のうち cut の block の行を指す物を doc から外す → (design, timeline, 落とした物の記録 — 空 = 何も落とさない)。
    design の行はその行と字下げの子を消す (`kind: design`)。timeline の台詞行 (印を除くと `@` で始まる行 — 頭に印や無音のある行も)
    は消さずに印 (効果音の `[♪…]` は残す) だけ落とす (`kind: marks`) — 消した層を指す印の DEFECT で台詞 (TTS の元) まで消えて
    「台詞行が無い」に連鎖した (o6_03)。印の無い台詞行は行ごと消す (`kind: speech`・`@clip` なら `clip` = 持ち込み音声の発話の id)。
    他の timeline の行 (印だけの行・切替・bgm) は行ごと (`kind: timeline`)。記録は落とした中身そのもの — 利用者への出力に出す
    (黙って落とさない)。block の頭 (section / *** の行) は落とさない。"""
    texts = {"design": design, "timeline": timeline}
    dropped: list[dict[str, object]] = []
    for which in ("design", "timeline"):
        lines = texts[which].split("\n")
        span = block_span(lines, which, cut)
        if span is None:
            continue
        start, end = span
        kill: set[int] = set()
        stripped: dict[int, str] = {}
        for d in defects:
            if d.level != "DEFECT" or d.file != f"{which}.txt":
                continue
            n = d.line
            if not (start < n < end) or n in kill or n in stripped:
                continue
            row = lines[n - 1]
            record: dict[str, object] = {"cut": cut, "kind": which, "line": row.strip()}
            bare = _MARK_NOT_SE.sub("", row)
            if which == "timeline" and bare.lstrip().startswith("@"):
                if bare != row:
                    stripped[n] = bare
                    dropped.append({**record, "kind": "marks", "marks": _MARK_NOT_SE.findall(row)})
                    continue
                clip = re.match(r"\s*@clip\s+(\S+)", bare)
                record = {**record, "kind": "speech", **({"clip": clip.group(1)} if clip else {})}
            kill.add(n)
            j = n + 1
            while j < end and lines[j - 1].startswith((" ", "\t")):
                kill.add(j)
                j += 1
            dropped.append({**record, **({"children": j - n - 1} if j - n - 1 else {})})
        if kill or stripped:
            texts[which] = "\n".join(stripped.get(k, line) for k, line in enumerate(lines, start=1) if k not in kill)
    return texts["design"], texts["timeline"], dropped


BoxKey = tuple[str, frozenset[str], str]
AssetKey = tuple[frozenset[str], frozenset[str], frozenset[str], frozenset[BoxKey]]


def box_key(line: str) -> BoxKey | None:
    """箱 (div / shape / veil / def の実体 / icon …) の行から焼く絵を決める物 (型・大きさ・塗り・縁・影・中身)。暗い palette の div は
    既定で glass・gradient / 影つきの箱は svg に焼かれ、直しがその行を足す / 変えると seal の時に描き直す (3〜7 s・o27_03) — warm の
    鍵に入れて掛け直す。位置と動きは焼く絵を変えない。"""
    m = re.match(r"^\s*([A-Za-z_][\w-]*)(?:#\S*)?\(((?:[^()]|\([^()]*\))*)\)\s*(.*)$", line)
    if m is None or m.group(1) in _NOT_BOX:
        return None
    decls = split_top_level(m.group(2))
    kept = frozenset(d.strip() for d in decls if d.strip() and d.split(":", 1)[0].strip() not in _BOX_SKIP)
    return (m.group(1), kept, m.group(3).strip())


def asset_key(text: str) -> AssetKey:
    """cut の text のうち素材を決める物 (絵の説明文・台詞の文字 (印を除く)・効果音の説明・svg に焼く箱の見た目) — 同じなら warm を
    掛け直さない (位置だけの直しは絵も声も変えない)。並びと重複は素材を変えないので集合で見る (直し役が img の行を書き直して 2 行に
    なり、同じ絵なのに warm を掛け直した・o7_03 situation 17 s)。"""
    lines = text.splitlines()
    pictures = frozenset(m.group(1).strip() for line in lines if (m := PICTURE_LINE.match(line)))
    speech = frozenset(without_marks(line) for line in lines if line.lstrip().startswith("@"))
    boxes = frozenset(k for line in lines if (k := box_key(line)) is not None)
    return (pictures, speech, frozenset(_SE.findall(text)), boxes)


# ===== 直しの段の定数と尺の指摘 (製品と client の共有) =====

# 見直し (レビュー) の回数 — 静止画を見せて 1 回 (10-27 裁定: 静止画なしのレビューも 2 回目も置かない)。直し役の 2 回の上限には数えない
REVIEW_ROUNDS = 1
# 台詞の尺の指摘: check の見積りが cut の予算から ±20% (短い cut は ±2.5 s — 文 1 本より細かく寄せない) を超えたら直し役に文の刈り込み
# / 足しを頼む。締めの cut の予算は依頼の残りを 10〜30 s の範囲で (弾性)
LENGTH_TOLERANCE = 0.2
LENGTH_SLACK_S = 2.5
CLOSING_BUDGET_S = (10.0, 30.0)


def closing_budget(requested: float, before: float) -> float:
    """締めの cut の予算 (弾性): 依頼の目安から前の live な cut の見込みを引いた残りを CLOSING_BUDGET_S の範囲で。"""
    low, high = CLOSING_BUDGET_S
    return min(max(requested - before, low), high)


def length_finding(estimate: float, budget: float, timeline: str) -> str:
    """check の見積り (字数 × 話速 + 間) が cut の予算から LENGTH_TOLERANCE (か LENGTH_SLACK_S の大きい方) を超えて外れたら、直し役
    への指摘の 1 行 (文を丸ごと消す / 足す本数つき)。外れていない・声のある台詞行が無ければ空。逐語の動画と最初の cut に掛けないのは
    呼び手 (逐語は依頼の台本の改変になる・最初の cut は再生開始の臨界路で、ずれは締めの cut の弾性が吸う)。"""
    gap = estimate - budget
    if abs(gap) <= max(budget * LENGTH_TOLERANCE, LENGTH_SLACK_S):
        return ""
    # 声の無い行 (`@名: [silence:2s]`) は演出の間 — 数えず、声の無い cut (章の札・題の間) は文の足し引きで寄せない (足すと間が台詞に化ける)
    lines = sum(1 for line in timeline.splitlines() if line.lstrip().startswith("@") and spoken(line))
    if not lines:
        return ""
    per = estimate / lines
    n = min(max(round(abs(gap) / per), 1), 2)
    verb = "delete" if gap > 0 else "add"
    return (
        f"warn {LENGTH_RULE} (cut): estimated speech {estimate:.0f} s / this cut's target {budget:.0f} s ({gap:+.0f} s;"
        f" one speech line ≈ {per:.0f} s) — {verb} {n} whole speech line(s) (whole sentences; do not meet it with fast"
        " talking or packed pauses)"
    )


# ===== check の autofix (lint の `Finding.autofix` = `操作:引数` の解釈) =====

# 積極的に当てる機械の直し — 直し方が正解として一つに決まり、問題を隠さず、著者が書いた物を消さない (design の `\n`・根から継いだ
# 切替と書いた out の二重 (out を残して切替を cut に)・言い切ってから切り替える / 切替が済んでから話し始める 0.5 秒以下の間)。他
# (0.5 秒を超える間・切替を短く溶かす・文字を板の上に出す) は消極的: 問題は消えるが LLM ならもっと良い直し方 (構成・位置・切替の種)
# を選べる — 後に担当や warn を直す直し役が残る間は当てずに指摘のまま渡し、LLM がもう見ない段で当てる (10-26 bench: 0.5 秒以下の
# 間を積極的にした腕が 60-52・消極的まで担当の前に当てた腕は 40-74 で負け)。積極 / 消極は規則で決める (同じ `transition` の操作でも
# double_exit の `cut` は積極・ghost_dissolve の短い dissolve は消極)
AUTOFIX_SURE_SILENCE_S = 0.5
# 無音の token — grammar の `[silence:…]` (`timeline._SILENCE_RE`・単位つき) と同じ綴り (`+` = 既定への足し・ms / s)。標準
# library だけの file なので grammar を import せず、ずれは test (`test_draft_author_prompts`) が縛る
SILENCE_TOKEN = re.compile(r"\[silence:(?P<add>\+)?(?P<value>\d+(?:\.\d+)?|\.\d+)(?P<unit>ms|s)\]")
_SILENCE_TAIL = re.compile(SILENCE_TOKEN.pattern + r"\s*$")


def _silence_plus(old: re.Match[str] | None, seconds: float) -> str:
    """書いてある無音 old に seconds を足した token (無ければ `[silence:+Ns]`)。`+` の有無と単位は書いたまま — 行末の絶対値は
    端の無音の実効値・`+` は既定への足しなので、どちらも値に足せば意図の長さになる (後ろに `+` を足すと既定をもう一度数える)。"""
    if old is None:
        return f"[silence:+{seconds:.2f}s]"
    add, value = old.group("add") or "", float(old.group("value"))
    if old.group("unit") == "ms":
        return f"[silence:{add}{round(value + seconds * 1000)}ms]"
    return f"[silence:{add}{value + seconds:.2f}s]"


def _add_silence(line: str, seconds: float, *, head: bool) -> str:
    """台詞の行の頭 (話者の後 — `@clip id [.tag]` の後も) か末尾の `[silence:…]` に seconds を足す (無ければ書く)。書けない行は
    そのまま返す (当てない — 指摘が残る): 話者の読めない行・原文を書かない `@clip` の行 (`@clip id` だけ・印だけ — `[silence:]` だけの
    本文は原文の頭か尻か決まらず server が DEFECT にする)・頭に印のある `@clip` の行の頭 (印の位置で segment が割れ、無音だけの最初の
    segment を server の組み立てが同じ DEFECT にする — 印の後ろに置くと印は無音の前に出て、頭の無音の意味が無い)。"""
    speaker = SPEAKER.match(line)
    clip = re.match(r"\s*@clip\s", line) is not None
    if speaker is None or (clip and not spoken(line)):
        return line
    if head:
        cut = speaker.end()
        rest = line[cut:]
        lead = rest[: len(rest) - len(rest.lstrip())]
        body = rest[len(lead) :]
        old = SILENCE_TOKEN.match(body)
        after = body[old.end() :] if old else body
        if clip and after.startswith("[") and not after.startswith("[trim:"):
            return line
        return line[:cut] + lead + _silence_plus(old, seconds) + after
    old = _SILENCE_TAIL.search(line)
    return (line[: old.start()] if old else line.rstrip()) + _silence_plus(old, seconds)


def _element_spans(lines: Sequence[str]) -> dict[str, tuple[int, int, str]]:
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


def autofix_is_sure(rule: str, autofix: str, sure_rules: frozenset[str]) -> bool:
    """積極的な機械の直しか (台帳の `sure` の規則 ``sure_rules`` — 製品は `draft_check.rules.sure_rules`・stream は API `drafts/rules/`
    の行 — と 0.5 秒以下の無音)。"""
    op, _, arg = autofix.partition(":")
    return rule in sure_rules or (op in ("silence_tail", "silence_head") and float(arg) <= AUTOFIX_SURE_SILENCE_S)


# 切替の行 `種 {…} [se=…]` (object の文字列の中の `{` `}` は数えない)
_TRANSITION_LINE_RE = re.compile(
    r"""^(?P<kind>[a-z]+)(?:\s*(?P<obj>\{(?:[^{}'"]|'[^']*'|"[^"]*")*\}))?(?:\s+(?P<se>se=.*))?$"""
)
_AUTOFIX_TRANSITION_KEYS = frozenset({"duration", "overlap"})  # autofix が替える key (他は書いたまま)


def _object_items(obj: str | None) -> list[str]:
    """`{a: 1, b: 'x,y'}` → `["a: 1", "b: 'x,y'"]` (top-level の `,` で割る)。"""
    return [item.strip() for item in split_top_level(obj[1:-1], ",") if item.strip()] if obj else []


def _object_key(item: str) -> str:
    return item.partition(":")[0].strip()


def apply_autofix(
    block: str, fixes: Sequence[tuple[str, str]], *, sure_only: bool = False, sure_rules: frozenset[str] = frozenset()
) -> tuple[str, list[int]]:
    """check の指摘のうち直し方が一つに決まる物 (fixes = (規則, autofix) の列 — autofix は lint が計算した `操作:引数`) を cut の
    block に当てる → (直した block, 当てた fixes の index)。当たらない指摘 (行が見つからない・形が違う) は飛ばす。
    - `silence_tail:秒` 最後の台詞の末尾の無音 (切替が台詞に掛かる) / `silence_head:秒` 最初の台詞の頭の無音 (入場が切替の窓に入る)
    - `transition:種 {duration: 秒, overlap: 秒}` cut の切替の行の種・尺・overlap を替える (object の他の key — 向き・帯 — と
      `se=` は残す)・`transition:cut` は
      切替の行の無い cut に `transition cut` を足す (根から継いだ切替と書いた out の二重掛け — 書いた out を残す)
    - `move_after:文字:隠す側` 隠れた文字の行 (と子) を隠す側の行 (と子) の後へ (同じ親の兄弟の時だけ)
    - `br` design の文字の中の `\\n` を `[br]` に (`\"\"\"` の source の中は見ない — timeline の台詞は対象外)
    sure_only = 積極的な直し (`autofix_is_sure` — 台帳の sure の規則 ``sure_rules`` と短い無音) だけ当てる (後に LLM が残る時)。"""
    design, sep, timeline = block.partition(TIMELINE_SEP)
    if not sep:
        return block, []
    dlines, tlines = design.split("\n"), timeline.split("\n")
    speech = [at for at, line in enumerate(tlines) if line.lstrip().startswith("@")]
    applied: list[int] = []
    for index, (rule, autofix) in enumerate(fixes):
        if not autofix or (sure_only and not autofix_is_sure(rule, autofix, sure_rules)):
            continue
        op, _, arg = autofix.partition(":")
        before = (list(dlines), list(tlines))
        if op in ("silence_tail", "silence_head") and speech:
            at = speech[-1] if op == "silence_tail" else speech[0]
            tlines[at] = _add_silence(tlines[at], float(arg), head=op == "silence_head")
        elif op == "transition":
            lines = [at for at, line in enumerate(tlines) if line.lstrip().startswith("transition ")]
            if (
                lines
                and (old := _TRANSITION_LINE_RE.match(tlines[lines[-1]].strip().removeprefix("transition ").strip()))
                is not None
            ):
                new = _TRANSITION_LINE_RE.match(arg)
                items = _object_items(new.group("obj")) if new is not None else []
                kept = [
                    item
                    for item in _object_items(old.group("obj"))
                    if _object_key(item) not in _AUTOFIX_TRANSITION_KEYS
                ]
                kind = new.group("kind") if new is not None else arg
                body = f" {{{', '.join([*items, *kept])}}}" if items or kept else ""
                tlines[lines[-1]] = f"transition {kind}{body}" + (f" {old.group('se')}" if old.group("se") else "")
            elif not lines:
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
            applied.append(index)
    return "\n".join(dlines) + sep + "\n".join(tlines), applied

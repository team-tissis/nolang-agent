"""`studio new` の中身 — 構成の型の骨組み (reference/scaffolds/<型>_<縦横>/ の著述の HTML 形・手で書いた正本) を project に置き、
src.json を書く。stdlib だけ: plugin で入れた skill (repo 無し・--remote) も同じ骨組みから始める。骨組みを変えるときは
reference/scaffolds/ の file を直す (test_draft_studio が HTML 形で読める事と schema_version を見る)。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from stream_author import REFERENCE  # 隣の file — 文書一式の dir (bundle では scripts の隣・repo では libs の正本)

HERE = Path(__file__).resolve().parent
SCAFFOLDS = REFERENCE / "scaffolds"
SCHEMA_VERSION = 11  # domain.constants.draft_composer.DRAFT_COMPOSER_SCHEMA_VERSION (test が同じ値か見る)
KINDS = ("data", "concept", "compare", "story", "cinematic")


def scaffold_dir(kind: str, aspect: str) -> Path:
    return SCAFFOLDS / f"{kind}_{aspect.replace(':', 'x')}"


def new(path: Path, kind: str, aspect: str, seconds: int | None) -> list[str]:
    """骨組みを置く (既存 file は上書きしない)。aspect=9:16 は縦の design (timeline は同じ)。seconds = 目標の尺 (src.json の
    target_s)。書かなければ target_s を置かず、check は既定の尺に「雛形の既定」と添える。置いた file の名を返す。"""
    source = scaffold_dir(kind, aspect)
    if not source.is_dir():
        raise SystemExit(f"骨組みが無い: {kind} {aspect} (型は {' / '.join(KINDS)}・縦横は 16:9 / 9:16)")
    path.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    for name in ("timeline.txt", "design.txt"):
        target = path / name
        if target.exists():
            continue
        target.write_text((source / name).read_text(encoding="utf-8"), encoding="utf-8")
        written.append(name)
    src_json = path / "src.json"
    if not src_json.exists():
        settings: dict[str, object] = {"language": "ja", "resolution": 1080, "title": path.name}
        if seconds is not None:
            settings["target_s"] = float(seconds)
        meta = {
            "asset_pins": {},
            "schema_version": SCHEMA_VERSION,
            "settings": dict(sorted(settings.items())),
        }
        src_json.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        written.append("src.json")
    return written


if __name__ == "__main__":  # python studio_new.py <project/studio> <型> <縦横> [秒]
    target, kind, aspect = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
    seconds = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4].isdigit() else None  # `auto` = 指定なし
    names = new(target, kind, aspect, seconds)
    print(f"OK new ({kind} {aspect}): {target} に {', '.join(names) or '何も書かず (既にある)'}。# TODO を埋めて check")

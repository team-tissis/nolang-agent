"""stream の orchestrator と NoLang API (`unstable/drafts/`) の間の形 — 受け口の答えの読み方・欠陥の記録・HTTP の窓口・文書一式の取り直し。

cut の段 (`cut_stages.CutStages` — `stream_stages.Run`) はこの形だけを見て、運ぶ先 (remote = この HTTP の窓口・local = repo の dev script が手元の flow 関数を
呼ぶ) を知らない。標準 library だけで動く (配布 bundle の client は使う側の python3)。
"""

from __future__ import annotations

import http.client
import io
import json
import os
import shutil
import tarfile
import time
import urllib.error
import urllib.request
from collections.abc import Callable
from pathlib import Path

from stream_author import author_core, cut_stages

# 欠陥の形と届かない頼みは cut の段 (`cut_stages`) と共有 — 運ぶ先が上げ、段が読む
Defect = cut_stages.Defect
Unreachable = cut_stages.Unreachable

# 取り直した文書一式の置き場 (内容の指紋の名の dir — 中身は不変なので再検証も TTL も要らない)。新しい物から 2 版だけ残す
REFERENCE_CACHE_KEEP = 2


class Rejected(Exception):
    """受け口が止めた頼み (HTTP の 400 と同じ中身)。defects = 投入検査の DEFECT の行 (無ければ error の文)。"""

    def __init__(self, op: str, defects: list[str]) -> None:
        super().__init__(f"{op}: " + " / ".join(defects)[:600])
        self.defects = defects


def read_answer(op: str, loaded: dict[str, object]) -> dict[str, object]:
    """受け口の答え (remote の HTTP・local の flow 関数の JSON は同じ形) を読む: `status` 400 は `Rejected`・500 は RuntimeError。"""
    if loaded.get("status") == 500:
        raise RuntimeError(f"{op} -> 500: {loaded.get('error')}")
    if loaded.get("status") == 400:
        defects = loaded.get("defects")
        raise Rejected(op, [str(d) for d in defects] if isinstance(defects, list) else [str(loaded)[:600]])
    return loaded


def claude_mcp_token(remote: str) -> str | None:
    """Claude Code が remote MCP (`<remote>/mcp`) の OAuth で得た access token (`~/.claude/.credentials.json` の mcpOAuth)。
    CLI / MCP の窓口は OAuth の token だけを受ける (API key は 403) — `/mcp` で NoLang に接続した token をそのまま REST にも使う
    (同じ Bearer)。"""
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


def reference_cache_root() -> Path:
    return Path(os.environ.get("NOLANG_CONFIG_DIR") or Path.home() / ".config" / "nolang") / "reference"


class RemoteApi:
    """NoLang API の HTTP の窓口 — 認証と client の版の header (`X-NoLang-Client`)・止めた頼みと届かない頼みの見分け・送り直し。"""

    ROUTES = {  # op → (method, path) — {id} は run の video
        "cut": ("POST", "/v1/unstable/drafts/{id}/cuts/"),
        "warm": ("POST", "/v1/unstable/drafts/{id}/warm/"),
        "stills": ("POST", "/v1/unstable/drafts/{id}/stills/"),
        "stills_status": ("GET", "/v1/unstable/drafts/{id}/stills/{job}/"),
        "check": ("POST", "/v1/unstable/drafts/check/"),
        "rename": ("POST", "/v1/unstable/drafts/rename/"),
        "rules": ("GET", "/v1/unstable/drafts/rules/"),
        "abort": ("DELETE", "/v1/unstable/drafts/{id}/"),
        "status": ("GET", "/v1/unstable/drafts/{id}/"),
    }
    # 何度送っても同じ答えの頼み — 届かなければ間を置いて送り直す (dev の check は混むと ALB の 60 s を超えて 504・切断も出る。
    # 1 回で諦めると stage が死んで cut が動画から落ちた)。投入 (`cut`) は送り直さない — 照合は `Run.submit`
    RESENDABLE = frozenset({"check", "rename", "rules", "stills_status", "status"})

    def __init__(
        self, base: str, token: str | None, *, contract: int, reference_hash: str, log: Callable[..., None]
    ) -> None:
        self.base = base.rstrip("/")
        self.token = token
        self.client = f"contract={contract}; ref={reference_hash[:16]}"
        self.log = log

    def headers(self, *, content_type: str | None = "application/json") -> dict[str, str]:
        headers = {"Authorization": f"Bearer {self.token}", "X-NoLang-Client": self.client}
        if content_type is not None:
            headers["Content-Type"] = content_type
        return headers

    def call(
        self, op: str, body: dict[str, object] | None, *, video_id: str | None, **path_args: str
    ) -> dict[str, object]:
        """受け口を 1 回呼ぶ (`ROUTES`・path_args は path の `{名}`)。止めた頼み (HTTP の 400) は `Rejected`・届かない時は `Unreachable`
        (`RESENDABLE` は 3 回まで送ってから)・その他の失敗は RuntimeError。"""
        method, path = self.ROUTES[op]
        req = urllib.request.Request(
            f"{self.base}{path.format(id=video_id, **path_args)}",
            data=json.dumps(body or {}).encode("utf-8") if method == "POST" else None,
            headers=self.headers(),
            method=method,
        )
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    loaded = json.loads(resp.read().decode("utf-8") or "{}")
                break
            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", "replace")
                if e.code in (502, 503, 504):
                    error: RuntimeError = Unreachable(f"{op} -> {e.code}: {detail[:600]}")
                elif e.code >= 500 and op in self.RESENDABLE:
                    # server の 500 (check の例外) は 1 回だけ呼び直し、それでも駄目なら届かなかった扱い (Unreachable —
                    # `guarded` は cut を落とさず投入の門に任せる)。11-02 dev 67aca628: check の 500 で段が死んで intro が消えた
                    error = Unreachable(f"{op} -> {e.code}: {detail[:600]}")
                    if attempt >= 1:
                        raise error from e
                elif e.code != 400:
                    raise RuntimeError(f"{op} -> {e.code}: {detail[:600]}") from e
                else:
                    try:
                        loaded = {"status": 400, **json.loads(detail)}
                    except ValueError:
                        loaded = {"status": 400, "error": detail[:600]}
                    break
            except (urllib.error.URLError, http.client.HTTPException, ConnectionError, TimeoutError) as e:
                error = Unreachable(f"{op}: {e!r}")
            if op not in self.RESENDABLE or attempt == 2:
                raise error
            self.log(event="call_retry", op=op, attempt=attempt + 1, error=str(error)[:200])
            time.sleep(10 * (attempt + 1))
        return read_answer(op, loaded)

    def get(self, path: str) -> dict[str, object]:
        req = urllib.request.Request(f"{self.base}{path}", headers=self.headers(content_type=None))
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def post(self, path: str, body: dict[str, object]) -> dict[str, object]:
        """POST して答えを返す (止めた頼み = HTTP の 400 は応答の中身に `status: 400` を足して返す・他の HTTP の失敗は RuntimeError)。"""
        try:
            return self.open(path, body)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:600]
            if e.code != 400:
                # 断った理由 (本文の error_code・detail) を落とさない — 素の HTTPError では traceback に status しか残らない
                raise RuntimeError(f"{path} -> {e.code}: {detail}") from e
            return {"status": 400, "error": detail}

    def open(self, path: str, body: dict[str, object]) -> dict[str, object]:
        """素の POST (ここでは送り直さない・HTTP の失敗は urllib の例外のまま — run の開始は理由を見て待つか止まるかを決める)。"""
        req = urllib.request.Request(
            f"{self.base}{path}",
            data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
            headers=self.headers(),
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def fetch_reference_bundle(self, expected_hash: str, dest: Path) -> None:
        """`GET drafts/reference/` の束を dest (指紋の名の dir) に置く。tmp に展開して指紋を確かめてから rename するので、並行する
        run・途中の失敗で半端な dir は残らない。path は束の範囲の相対 path だけを受ける (絶対 path・`..`・file 以外は弾く)。"""
        req = urllib.request.Request(
            f"{self.base}/v1/unstable/drafts/reference/", headers=self.headers(content_type=None)
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.parent / f".{dest.name}.{os.getpid()}.tmp"
        shutil.rmtree(tmp, ignore_errors=True)
        try:
            with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
                for member in tar.getmembers():
                    name = Path(member.name)
                    if not member.isfile() or name.is_absolute() or ".." in name.parts:
                        raise ValueError(f"束に受けない path: {member.name}")
                    source = tar.extractfile(member)
                    if source is None:
                        raise ValueError(f"束の file を読めない: {member.name}")
                    (tmp / name).parent.mkdir(parents=True, exist_ok=True)
                    (tmp / name).write_bytes(source.read())
            got = author_core.reference_hash_of(tmp)
            if got != expected_hash:
                raise ValueError(f"束の指紋が違う: {got[:16]} ≠ {expected_hash[:16]}")
            try:
                tmp.rename(dest)
            except OSError:
                # 並行する run が先に置いた (同じ指紋 = 同じ中身) のでなければ失敗
                if not (dest / "contract.json").is_file():
                    raise
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        kept = sorted(
            (p for p in dest.parent.iterdir() if p.is_dir() and not p.name.startswith(".")),
            key=lambda p: p.stat().st_mtime,
        )
        for old in kept[:-REFERENCE_CACHE_KEEP]:
            if old != dest:
                shutil.rmtree(old, ignore_errors=True)

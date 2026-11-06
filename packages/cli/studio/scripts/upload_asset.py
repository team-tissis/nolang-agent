#!/usr/bin/env python3
"""手元の画像・動画を NoLang の自分の素材に upload し、draft src に書く `ref` (`id=<uuid>`) を出す (python3 の標準だけ — repo 無しでも動く)。

usage: python3 upload_asset.py <file>… --remote http://host:18000 [--token <OAuth の access token>] [--name 表示名]
  token は OAuth の access token — --token か env NOLANG_TOKEN・無ければ Claude Code が `/agent/mcp` で NoLang に接続した時の token (stream_run と同じ)。
  画像は 1 回の POST、動画 (mp4 / mov / webm …) は分割 upload → 確定 → 仕上げの job (尺・codec の検査と thumbnail) の完了まで待つ。
  1 file ごとに `REF <file> id=<uuid>` を 1 行。src には `image 名 = id=<uuid>` (動画は置く所に `play: loop`)。upload した素材は
  NoLang の自分の素材の一覧に入り、`nolang_assets_search` の scope=mine でも引ける。制限 (形式・大きさ) は web の upload と同じ。
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stream_api import claude_mcp_token  # 同じ dir の script (token の取り方を 1 か所に)

# 動画素材として送る拡張子 (web の動画の upload が受ける物 = `app_main/utils/magic_checks.py` の VIDEO_ALLOWED_EXTENSIONS —
# ほかは画像として送り、形式の検査は server)
_VIDEO_EXTENSIONS = frozenset({".mp4", ".webm", ".mov"})
_JOB_WAIT_S = 600


def _call(remote: str, token: str, method: str, path: str, body: bytes | None = None, ctype: str | None = None) -> dict:
    headers = {"Authorization": f"Bearer {token}"}
    if ctype:
        headers["Content-Type"] = ctype
    request = urllib.request.Request(f"{remote}{path}", data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            return json.loads(response.read() or b"{}")
    except urllib.error.HTTPError as error:
        raise SystemExit(f"{method} {path} → {error.code}: {error.read().decode(errors='replace')[:400]}") from error


def _upload_image(remote: str, token: str, path: Path, name: str | None) -> str:
    boundary = uuid.uuid4().hex
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    parts = [
        f'--{boundary}\r\nContent-Disposition: form-data; name="image_file"; filename="{path.name}"\r\n'
        f"Content-Type: {mime}\r\n\r\n".encode()
        + path.read_bytes()
        + b"\r\n"
    ]
    if name:
        names = json.dumps({"default": name}, ensure_ascii=False)
        parts.append(
            f'--{boundary}\r\nContent-Disposition: form-data; name="names_by_languages"\r\n\r\n{names}\r\n'.encode()
        )
    body = b"".join(parts) + f"--{boundary}--\r\n".encode()
    row = _call(remote, token, "POST", "/agent/v1/assets/images/", body, f"multipart/form-data; boundary={boundary}")
    return str(row["image_id"])


def _upload_footage(remote: str, token: str, path: Path, name: str | None) -> str:
    size = path.stat().st_size
    init = json.dumps({"filename": path.name, "total_size": size}).encode()
    started = _call(remote, token, "POST", "/agent/v1/assets/footages/uploads/", init, "application/json")
    chunk = int(started["chunk_size"])
    etags: list[dict[str, object]] = []
    with path.open("rb") as stream:
        for part in sorted(started["part_urls"], key=lambda p: p["part_number"]):
            stream.seek((part["part_number"] - 1) * chunk)
            request = urllib.request.Request(part["url"], data=stream.read(chunk), method="PUT")  # S3 の presigned URL
            with urllib.request.urlopen(request, timeout=600) as response:
                etags.append({"part_number": part["part_number"], "etag": response.headers["ETag"]})
    complete = {
        "upload_id": started["upload_id"],
        "object_key": started["object_key"],
        "filename": path.name,
        "parts": etags,
        **({"name": name} if name else {}),
    }
    upload_path = f"/agent/v1/assets/footages/uploads/{started['upload_id']}/"
    done = _call(remote, token, "PATCH", upload_path, json.dumps(complete).encode(), "application/json")
    deadline = time.monotonic() + _JOB_WAIT_S
    while time.monotonic() < deadline:  # 行は仕上げの job が作る (尺・codec の検査・S3 への配置・thumbnail)
        job = _call(remote, token, "GET", f"/agent/v1/jobs/{done['job_id']}/")
        if job["status"] == "succeeded":
            return str(done["footage_id"])
        if job["status"] in ("failed", "canceled"):
            raise SystemExit(
                f"{path.name}: 仕上げの job が {job['status']} ({job.get('error_code')} {job.get('error_params')})"
            )
        time.sleep(3)
    raise SystemExit(f"{path.name}: 仕上げの job が {_JOB_WAIT_S} s で終わらない (job {done['job_id']})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--remote", required=True, help="NoLang API (例 https://api.no-lang.com)")
    parser.add_argument("--token", default=None)
    parser.add_argument("--name", default=None, help="素材の表示名 (既定は file 名)")
    args = parser.parse_args()
    remote = args.remote.rstrip("/")
    token = args.token or os.environ.get("NOLANG_TOKEN") or claude_mcp_token(remote)
    if not token:
        raise SystemExit("token が無い (--token / NOLANG_TOKEN / Claude Code の `/agent/mcp` で NoLang に接続)")
    for path in args.files:
        if not path.is_file():
            raise SystemExit(f"{path}: file が無い")
        upload = _upload_footage if path.suffix.lower() in _VIDEO_EXTENSIONS else _upload_image
        print(f"REF {path} id={upload(remote, token, path, args.name)}", flush=True)


if __name__ == "__main__":
    main()

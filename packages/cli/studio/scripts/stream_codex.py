"""Codex app-server の本文差分を studio に渡す。対応確認: codex-cli 0.162.0。"""

from __future__ import annotations

import json
import os
import queue
import shutil
import subprocess
import tempfile
import threading
import time
from collections.abc import Callable
from pathlib import Path
from typing import TextIO


def object_value(value: object) -> dict[str, object]:
    if not isinstance(value, dict):
        raise RuntimeError("Codex の応答が object ではありません")
    return {str(k): v for k, v in value.items()}


def string_value(value: object) -> str:
    if not isinstance(value, str):
        raise RuntimeError("Codex の応答に必要な文字列がありません")
    return value


class CodexConnection:
    """1 call の stdio 接続。通知を request 待機中にも保持する。"""

    def __init__(self, process: subprocess.Popen[str], raw: TextIO, timeout: float) -> None:
        if process.stdin is None or process.stdout is None:
            raise RuntimeError("Codex の stdio がありません")
        self.process = process
        self.stdin = process.stdin
        self.raw = raw
        self.deadline = time.monotonic() + timeout
        self.lines: queue.Queue[str | None] = queue.Queue()
        self.pending: list[dict[str, object]] = []
        self.sequence = 0
        self.thread_id = ""
        self.turn_id = ""
        stdout = process.stdout

        def read_lines() -> None:
            try:
                for line in stdout:
                    self.lines.put(line)
            finally:
                self.lines.put(None)

        self.reader = threading.Thread(target=read_lines, daemon=True)
        self.reader.start()

    def send(self, message: dict[str, object]) -> None:
        self.stdin.write(json.dumps(message, ensure_ascii=False) + "\n")
        self.stdin.flush()

    def receive(self) -> dict[str, object]:
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Codex の応答が制限時間を超えました")
        try:
            line = self.lines.get(timeout=remaining)
        except queue.Empty as exc:
            raise TimeoutError("Codex の応答が制限時間を超えました") from exc
        if line is None:
            raise RuntimeError("Codex が完了通知の前に終了しました")
        self.raw.write(line)
        self.raw.flush()
        value: object = json.loads(line)
        message = object_value(value)
        # 著述にツールやユーザー操作は不要。想定外の request は実行せず失敗させる。
        if "method" in message and "id" in message:
            self.send({"id": message["id"], "error": {"code": -32601, "message": "studio はツールを実行しません"}})
            raise RuntimeError(f"Codex が著述以外の操作を要求しました: {message['method']}")
        return message

    def request(self, method: str, params: dict[str, object]) -> dict[str, object]:
        self.sequence += 1
        request_id = self.sequence
        self.send({"id": request_id, "method": method, "params": params})
        while True:
            message = self.receive()
            if message.get("id") != request_id:
                self.pending.append(message)
                continue
            if "error" in message:
                raise RuntimeError(f"Codex {method}: {message['error']}")
            return object_value(message.get("result"))

    def stream(self, on_text: Callable[[str], None]) -> None:
        # final_answer の本文だけを流す。思考・進捗文と他の turn は原稿に混ぜない。
        accepted: set[str] = set()
        texts: dict[str, str] = {}
        while True:
            message = self.pending.pop(0) if self.pending else self.receive()
            method = message.get("method")
            params = object_value(message.get("params", {}))
            if params.get("threadId") != self.thread_id:
                continue
            if method == "turn/completed":
                turn = object_value(params.get("turn"))
                if turn.get("id") != self.turn_id:
                    continue
                if turn.get("status") != "completed":
                    raise RuntimeError(f"Codex の生成に失敗しました: {turn.get('error') or turn.get('status')}")
                if not any(texts.values()):
                    raise RuntimeError("Codex が本文を返しませんでした")
                return
            if params.get("turnId") != self.turn_id:
                continue
            if method in ("item/started", "item/completed"):
                item = object_value(params.get("item"))
                if item.get("type") != "agentMessage" or item.get("phase") == "commentary":
                    continue
                item_id = string_value(item.get("id"))
                accepted.add(item_id)
                if method == "item/completed":
                    final = string_value(item.get("text"))
                    previous = texts.get(item_id, "")
                    if not final.startswith(previous):
                        raise RuntimeError("Codex の確定本文が受信済みの差分と一致しません")
                    if final[len(previous) :]:
                        on_text(final[len(previous) :])
                    texts[item_id] = final
            elif method == "item/agentMessage/delta":
                item_id = string_value(params.get("itemId"))
                if item_id in accepted:
                    delta = string_value(params.get("delta"))
                    texts[item_id] = texts.get(item_id, "") + delta
                    on_text(delta)

    def close(self) -> None:
        if self.process.poll() is None:
            try:
                if self.thread_id and self.turn_id:
                    self.send(
                        {
                            "id": "interrupt",
                            "method": "turn/interrupt",
                            "params": {
                                "threadId": self.thread_id,
                                "turnId": self.turn_id,
                            },
                        }
                    )
                self.stdin.close()
            except (OSError, ValueError):
                pass
            try:
                self.process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.process.terminate()
                try:
                    self.process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    self.process.kill()
                    self.process.wait()
        self.reader.join(timeout=1)
        try:
            self.stdin.close()
        except OSError:
            pass
        if self.process.stdout is not None:
            self.process.stdout.close()


def stream_codex(
    st: Path,
    prompt: str,
    on_text: Callable[[str], None],
    *,
    system_prompt: Path,
    effort: str,
    tag: str,
    images: list[Path] | None = None,
    timeout: float = 540,
) -> None:
    """個人の hook / plugin / MCP / 指示を読み込まず、認証だけを使う独立した著述 call。"""
    binary = shutil.which("codex")
    if binary is None:
        raise RuntimeError("codex がありません。Codex CLI をインストールしてください")
    auth = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "auth.json"
    if not auth.is_file():
        raise RuntimeError("Codex の auth.json がありません。codex login で file 保存の認証を用意してください")
    st.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    # プロジェクトの外の一時領域を使い、祖先の .codex 設定や指示も持ち込まない。
    # auth はコピーせず共有。設定・hooks・会話履歴は call ごとに隔離する。
    with tempfile.TemporaryDirectory(prefix="nolang-codex-") as temporary:
        home = Path(temporary).resolve()
        (home / "auth.json").symlink_to(auth.resolve())
        cwd = home / "cwd"
        cwd.mkdir()
        (home / "config.toml").write_text(
            'web_search = "disabled"\nproject_doc_max_bytes = 0\n'
            "[features]\nshell_tool = false\nplugins = false\napps = false\nhooks = false\n"
            "multi_agent = false\nmemories = false\nview_image = false\n"
            "image_generation = false\nbrowser_use = false\ncomputer_use = false\n"
        )
        env = {
            k: v
            for k, v in os.environ.items()
            if k
            in {
                "PATH",
                "HOME",
                "USER",
                "LANG",
                "LC_ALL",
                "TMPDIR",
                "SYSTEMROOT",
                "HTTPS_PROXY",
                "HTTP_PROXY",
                "NO_PROXY",
                "https_proxy",
                "http_proxy",
                "no_proxy",
                "SSL_CERT_FILE",
                "SSL_CERT_DIR",
            }
        }
        env["CODEX_HOME"] = str(home)
        with (st / f"codex_{tag}.jsonl").open("a") as raw, (st / f"codex_{tag}.err").open("a") as errors:
            process = subprocess.Popen(
                [binary, "app-server"],
                cwd=cwd,
                env=env,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=errors,
                text=True,
            )
            connection = CodexConnection(process, raw, timeout)
            try:
                connection.request(
                    "initialize",
                    {
                        "clientInfo": {"name": "nolang_studio", "version": "0.1.0"},
                        "capabilities": {"experimentalApi": True},
                    },
                )
                connection.send({"method": "initialized"})
                response = connection.request(
                    "thread/start",
                    {
                        "cwd": str(cwd),
                        "ephemeral": True,
                        "approvalPolicy": "never",
                        "sandbox": "read-only",
                        "baseInstructions": system_prompt.read_text(),
                        "developerInstructions": "与えられた原稿だけを出力してください。進捗の説明・ツール呼び出しは不要です。",
                        "environments": [],
                    },
                )
                connection.thread_id = string_value(object_value(response.get("thread")).get("id"))
                with (st / "author.jsonl").open("a") as log:
                    log.write(
                        json.dumps(
                            {
                                "event": "codex_launch",
                                "tag": tag,
                                "model": response.get("model"),
                                "effort": effort,
                                "t": time.time(),
                            }
                        )
                        + "\n"
                    )
                inputs: list[dict[str, object]] = [{"type": "text", "text": prompt}]
                inputs.extend({"type": "localImage", "path": str(path.resolve())} for path in images or [])
                turn = connection.request(
                    "turn/start",
                    {
                        "threadId": connection.thread_id,
                        "input": inputs,
                        "effort": effort,
                    },
                )
                connection.turn_id = string_value(object_value(turn.get("turn")).get("id"))
                connection.stream(on_text)
            finally:
                connection.close()
                with (st / "author.jsonl").open("a") as log:
                    log.write(
                        json.dumps(
                            {
                                "event": "codex_end",
                                "tag": tag,
                                "s": round(time.monotonic() - started, 2),
                                "t": time.time(),
                            }
                        )
                        + "\n"
                    )

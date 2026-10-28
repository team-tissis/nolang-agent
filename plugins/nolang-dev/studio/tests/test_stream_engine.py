"""実際の stdio と生成順序を使う、外部 LLM を呼ばない契約テスト。"""

from __future__ import annotations

import importlib
import io
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
codex = importlib.import_module("stream_codex")
author = importlib.import_module("stream_author")
runner = importlib.import_module("stream_run")


def event(method: str, **params: object) -> dict[str, object]:
    return {"method": method, "params": {"threadId": "t", "turnId": "u", **params}}


def message(kind: str, text: str = "", phase: str = "final_answer", item_id: str = "answer") -> dict[str, object]:
    return event(f"item/{kind}", item={"type": "agentMessage", "id": item_id, "phase": phase, "text": text})


DONE = event("turn/completed", turn={"id": "u", "status": "completed"})


class StreamContractTest(unittest.TestCase):
    def connect(self, events: list[dict[str, object]], *, timeout: float = 5, wait: bool = False):
        # Arrange: app-server の代わりに別プロセスから同じ JSONL 契約を流す。
        program = "import sys,time; sys.stdout.write(sys.argv[1]); sys.stdout.flush(); "
        program += "time.sleep(30)" if wait else "sys.stdin.read()"
        process = subprocess.Popen(
            [sys.executable, "-u", "-c", program, "".join(json.dumps(e) + "\n" for e in events)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
        )
        connection = codex.CodexConnection(process, io.StringIO(), timeout)
        connection.thread_id = "t"
        connection.turn_id = "u"
        self.addCleanup(connection.close)
        return connection

    def test_text_is_streamed_once_without_commentary_or_foreign_turn(self):
        # Arrange
        connection = self.connect(
            [
                message("started", phase="commentary", item_id="progress"),
                event("item/agentMessage/delta", itemId="progress", delta="進捗"),
                message("started"),
                event("item/agentMessage/delta", itemId="answer", delta="別の呼出し", turnId="other"),
                event("item/agentMessage/delta", itemId="answer", delta="=== cut "),
                event("item/agentMessage/delta", itemId="answer", delta="one ==="),
                message("completed", "=== cut one ==="),
                DONE,
            ]
        )
        output: list[str] = []
        # Act
        connection.stream(output.append)
        # Assert
        self.assertEqual(output, ["=== cut ", "one ==="])

    def test_final_message_without_deltas_is_delivered(self):
        connection = self.connect([message("completed", "原稿"), DONE])
        output: list[str] = []
        connection.stream(output.append)
        self.assertEqual(output, ["原稿"])

    def test_failed_turn_after_partial_text_is_not_success(self):
        connection = self.connect(
            [
                message("started"),
                event("item/agentMessage/delta", itemId="answer", delta="途中"),
                event("turn/completed", turn={"id": "u", "status": "failed", "error": "quota"}),
            ]
        )
        with self.assertRaisesRegex(RuntimeError, "quota"):
            connection.stream(lambda text: None)

    def test_final_message_must_preserve_already_streamed_prefix(self):
        connection = self.connect(
            [
                message("started"),
                event("item/agentMessage/delta", itemId="answer", delta="投入済み"),
                message("completed", "別の本文"),
                DONE,
            ]
        )
        with self.assertRaisesRegex(RuntimeError, "一致しません"):
            connection.stream(lambda text: None)

    def test_empty_success_is_rejected(self):
        connection = self.connect([DONE])
        with self.assertRaisesRegex(RuntimeError, "本文"):
            connection.stream(lambda text: None)

    def test_timeout_reaps_the_process(self):
        connection = self.connect([], timeout=0.05, wait=True)
        with self.assertRaises(TimeoutError):
            connection.stream(lambda text: None)
        connection.close()
        self.assertIsNotNone(connection.process.poll())

    def test_notifications_before_request_response_are_kept(self):
        connection = self.connect([message("completed", "原稿"), DONE, {"id": 1, "result": {"ok": True}}])
        response = connection.request("turn/start", {})
        output: list[str] = []
        connection.stream(output.append)
        self.assertEqual(response, {"ok": True})
        self.assertEqual(output, ["原稿"])

    def test_tool_request_is_rejected(self):
        connection = self.connect([{"id": 7, "method": "item/tool/call", "params": {}}])
        with self.assertRaisesRegex(RuntimeError, "著述以外"):
            connection.stream(lambda text: None)


class EngineRoutingTest(unittest.TestCase):
    def test_default_claude_keeps_existing_arguments(self):
        # Arrange
        def callback(text: str) -> None:
            pass

        arguments = dict(system_prompt=Path("system"), effort="low", tag="fix", cache_ttl="5m", images=[])
        with (
            patch.dict(os.environ, {}, clear=True),
            patch.object(author, "stream_claude", return_value={"ok": True}) as call,
        ):
            # Act
            result = author.stream_model(Path("stream"), "本文", callback, **arguments)
        # Assert
        call.assert_called_once_with(Path("stream"), "本文", callback, **arguments, before_input=None)
        self.assertEqual(result, {"ok": True})

    def test_codex_failure_is_visible_to_the_orchestrator(self):
        with tempfile.TemporaryDirectory() as directory:
            st = Path(directory)
            with (
                patch.dict(os.environ, {"NOLANG_STUDIO_ENGINE": "codex"}),
                patch.object(codex, "stream_codex", side_effect=RuntimeError("quota")),
                patch.object(author, "stream_claude") as claude,
            ):
                with self.assertRaisesRegex(RuntimeError, "quota"):
                    author.stream_model(
                        st, "本文", lambda text: None, system_prompt=st / "system", effort="low", tag="staff_one"
                    )
            self.assertIn("staff_one", (st / "engine.failed").read_text())
            claude.assert_not_called()

    def test_author_staff_and_fixer_use_codex_without_cache_warmup(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "stream").mkdir()
            (project / "studio").mkdir()
            (project / "params.txt").write_text("concept 16:9 15")
            (project / "request.txt").write_text("短い説明")
            (project / "studio/design.txt").write_text("#v2\ncanvas 1920x1080")
            (project / "studio/timeline.txt").write_text("#v2")
            roles: list[str] = []

            def generate(st, prompt, callback, *, system_prompt, effort, tag, images=None):
                self.assertTrue(system_prompt.exists())
                roles.append(tag)
                if tag == "author":
                    callback("=== plan ===\none: 説明 (15s)\n=== root_design ===\n#v2\ncanvas 1920x1080\n")
                    callback('=== root_timeline ===\n#v2\ncast n = "日本語の声"\n=== cut one ===\n')
                    callback(
                        "section#one\np#title こんにちは\n---timeline---\n*** one\n@n: こんにちは。\n=== end ===\n"
                    )
                elif tag.startswith("staff"):
                    callback(
                        "=== cut one ===\nsection#one\np#title こんにちは\n---timeline---\n*** one\n@n: こんにちは。\n=== end ===\n"
                    )
                else:
                    callback("=== edits ===\n=== end ===\n")

            def system(path, samples):
                path.write_text("文法と見本")
                return path

            with (
                patch.dict(os.environ, {"NOLANG_STUDIO_ENGINE": "codex"}),
                patch.object(codex, "stream_codex", side_effect=generate),
                patch.object(author, "build_system_prompt", side_effect=system),
                patch.object(author, "samples_text", return_value="見本"),
                patch.object(author, "warmup") as warmup,
            ):
                # Act: 実際の役割関数・Splitter・編集parserを通す。
                self.assertEqual(author.run(project, effort="low", samples=()), 0)
                findings = project / "stream/findings.txt"
                findings.write_text("確認")
                with patch("sys.stdout", new=io.StringIO()):
                    self.assertEqual(author.staff(project, "one", findings, effort="medium"), 0)
                    self.assertEqual(
                        author.fix(project, "one", findings, own_root=False, effort="low", review=False, shots=[]), 0
                    )
            # Assert
            self.assertEqual(roles, ["author", "staff_one", "fix_one"])
            warmup.assert_not_called()
            self.assertTrue((project / "stream/src.done").exists())


class ShellSelectionTest(unittest.TestCase):
    def test_inherited_engine_does_not_change_default_claude(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir()
            shutil.copy(SCRIPTS / "stream_make.sh", scripts)
            (scripts / "stream_pipeline.sh").write_text(
                '#!/bin/bash\nmkdir -p "$1/stream"\nprintf "%s" "$NOLANG_STUDIO_ENGINE" > "$1/engine"\n'
                ': > "$1/stream/run.jsonl"\n'
            )
            project = root / "project"
            (project / "studio").mkdir(parents=True)
            (project / "studio/design.txt").touch()
            result = subprocess.run(
                [
                    "bash",
                    str(scripts / "stream_make.sh"),
                    str(project),
                    "--type",
                    "concept",
                    "--request-text",
                    "説明",
                    "--remote",
                    "http://unused.invalid",
                ],
                env={**os.environ, "NOLANG_STUDIO_ENGINE": "codex", "PYTHON": sys.executable},
                capture_output=True,
                text=True,
                timeout=5,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((project / "engine").read_text(), "claude")


class SubmissionTest(unittest.TestCase):
    def test_killed_role_stops_codex_but_keeps_claude_failure_handling(self):
        for engine in ("claude", "codex"):
            with self.subTest(engine=engine), tempfile.TemporaryDirectory() as directory:
                run = runner.Run.__new__(runner.Run)
                run.st = Path(directory)
                run.env = os.environ.copy()
                with patch.dict(os.environ, {"NOLANG_STUDIO_ENGINE": engine}):
                    result = run.call_role([sys.executable, "-c", "import os; os._exit(7)"], timeout=5)
                self.assertEqual(result.returncode, 7)
                self.assertEqual((run.st / "engine.failed").exists(), engine == "codex")

    def test_cancel_during_render_wait_requests_remote_abort(self):
        with tempfile.TemporaryDirectory() as directory:
            run = runner.Run.__new__(runner.Run)
            run.st = Path(directory)
            run.video_id = "video"
            run.stream_proc = None
            (run.st / "engine.failed").write_text("中断")
            with (
                patch.dict(os.environ, {"NOLANG_STUDIO_ENGINE": "codex"}),
                patch.object(run, "abort") as abort,
                patch.object(run, "remote_get") as poll,
                patch.object(run, "log"),
            ):
                self.assertEqual(run.remote_wait(), 1)
                abort.assert_called_once()
                poll.assert_not_called()

    def test_end_waits_for_author_success_and_failure_prevents_submission(self):
        for failed in (False, True):
            with self.subTest(failed=failed), tempfile.TemporaryDirectory() as directory:
                run = runner.Run.__new__(runner.Run)
                run.st = Path(directory)
                run.remote = "http://unused.invalid"
                run.video_id = "video"
                result: list[object] = []
                with (
                    patch.dict(os.environ, {"NOLANG_STUDIO_ENGINE": "codex"}),
                    patch.object(run, "call", return_value={"lines": 3}) as post,
                ):
                    thread = threading.Thread(target=lambda: result.append(run.submit("one", "原稿", end=True)))
                    thread.start()
                    try:
                        time.sleep(0.15)
                        self.assertTrue(thread.is_alive())
                        post.assert_not_called()
                        (run.st / ("engine.failed" if failed else "src.done")).touch()
                    finally:
                        (run.st / "src.done").touch()
                        thread.join(timeout=3)
                    self.assertFalse(thread.is_alive())
                    self.assertEqual(post.call_count, 0 if failed else 1)
                    self.assertEqual(result, [None] if failed else [{"sealed": True, "lines": 3}])


class PipelineTest(unittest.TestCase):
    def test_abnormal_author_exit_aborts_runner_while_it_is_waiting(self):
        # Arrange: 著者が強制終了しても、orchestrator 終了まで検知を遅らせない。
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir()
            shutil.copy(SCRIPTS / "stream_codex_pipeline.py", scripts)
            (scripts / "stream_author.py").write_text("import os; os._exit(7)")
            (scripts / "stream_run.py").write_text(
                "import pathlib,sys,time\np=pathlib.Path(sys.argv[1])/'stream'\n"
                "while not (p/'engine.failed').exists(): time.sleep(.01)\n"
                "(p/'aborted').touch()\nsys.exit(1)\n"
            )
            project = root / "project"
            (project / "stream").mkdir(parents=True)
            # Act
            result = subprocess.run(
                [sys.executable, str(scripts / "stream_codex_pipeline.py"), str(project)],
                timeout=10,
            )
            # Assert
            self.assertEqual(result.returncode, 1)
            self.assertTrue((project / "stream/aborted").exists())
            self.assertIn("7", (project / "stream/engine.failed").read_text())

    def test_runner_failure_does_not_wait_for_the_author_to_finish(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copy(SCRIPTS / "stream_codex_pipeline.py", root)
            (root / "stream_author.py").write_text("import time; time.sleep(60)")
            (root / "stream_run.py").write_text("import sys; sys.exit(1)")
            project = root / "project"
            (project / "stream").mkdir(parents=True)
            started = time.monotonic()
            result = subprocess.run([sys.executable, str(root / "stream_codex_pipeline.py"), str(project)], timeout=10)
            self.assertEqual(result.returncode, 1)
            self.assertLess(time.monotonic() - started, 10)

    def test_cancel_aborts_runner_and_reaps_author(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copy(SCRIPTS / "stream_codex_pipeline.py", root)
            (root / "stream_author.py").write_text(
                "import pathlib,sys,signal,time\np=pathlib.Path(sys.argv[2])/'stream'\n"
                "def stop(*args): (p/'author_stopped').touch(); sys.exit(0)\n"
                "signal.signal(signal.SIGTERM, stop)\n(p/'author_ready').touch()\ntime.sleep(60)\n"
            )
            (root / "stream_run.py").write_text(
                "import pathlib,sys,time\np=pathlib.Path(sys.argv[1])/'stream'\n"
                "while not (p/'engine.failed').exists(): time.sleep(.01)\n"
                "(p/'aborted').touch()\nsys.exit(1)\n"
            )
            project = root / "project"
            stream = project / "stream"
            stream.mkdir(parents=True)
            process = subprocess.Popen([sys.executable, str(root / "stream_codex_pipeline.py"), str(project)])
            try:
                deadline = time.monotonic() + 5
                while not (stream / "author_ready").exists() and time.monotonic() < deadline:
                    time.sleep(0.01)
                self.assertTrue((stream / "author_ready").exists())
                process.send_signal(signal.SIGTERM)
                self.assertEqual(process.wait(timeout=10), 130)
                self.assertTrue((stream / "aborted").exists())
                self.assertTrue((stream / "author_stopped").exists())
            finally:
                if process.poll() is None:
                    process.terminate()
                    process.wait(timeout=10)


if __name__ == "__main__":
    unittest.main()

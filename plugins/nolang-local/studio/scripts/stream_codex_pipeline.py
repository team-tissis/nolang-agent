"""Codex の著者と投入側を監視し、異常終了と中断を取りこぼさない。"""

from __future__ import annotations

import os
import shlex
import signal
import subprocess
import sys
import time
from pathlib import Path


def stop_group(process: subprocess.Popen[bytes]) -> None:
    # 親が終了済みでも、担当・修正役や app-server が残っていれば回収する。
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        pass
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait()


def main(arguments: list[str]) -> int:
    project = Path(arguments[0]).resolve()
    scripts = Path(__file__).resolve().parent
    stream = project / "stream"
    failure = stream / "engine.failed"
    processes: list[subprocess.Popen[bytes]] = []

    def interrupted(_signum: int, _frame: object) -> None:
        raise KeyboardInterrupt

    signal.signal(signal.SIGTERM, interrupted)
    try:
        with (stream / "author.out").open("wb") as author_log, (stream / "run.out").open("wb") as run_log:
            author = subprocess.Popen(
                [
                    sys.executable,
                    os.environ.get("STREAM_AUTHOR") or str(scripts / "stream_author.py"),
                    "run",
                    str(project),
                    *arguments[1:],
                ],
                stdout=author_log,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
            processes.append(author)
            runner = subprocess.Popen(
                [
                    sys.executable,
                    os.environ.get("STREAM_RUN") or str(scripts / "stream_run.py"),
                    str(project),
                    *shlex.split(os.environ.get("STREAM_RUN_ARGS", "")),
                ],
                stdout=run_log,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
            processes.append(runner)
            while runner.poll() is None:
                code = author.poll()
                if code is not None and code != 0 and not failure.exists():
                    failure.write_text(f"Codex 著者が異常終了しました (exit {code})\n")
                time.sleep(0.1)
            if runner.returncode == 0 and not failure.exists():
                try:
                    return 0 if author.wait(timeout=10) == 0 else 1
                except subprocess.TimeoutExpired:
                    return 1
            return 1
    except KeyboardInterrupt:
        failure.write_text("Codex の生成が中断されました\n")
        # 投入側に abort の時間を与える。上限後はグループごと回収する。
        if len(processes) > 1:
            try:
                processes[1].wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
        return 130
    finally:
        for process in processes:
            stop_group(process)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

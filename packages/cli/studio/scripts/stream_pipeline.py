"""1 題材の stream 生成の監督: 著者 (stream_author.py run) と orchestrator (stream_run.py) を別の process group で同時に走らせる
(engine に依らない 1 本)。

usage: stream_pipeline.py <project> [--effort low] [--samples a.md,b.md] [--author-brief]
       (project = tmp/studio/<name>・params.txt と request.txt と studio/ が要る)。orchestrator の引数は env STREAM_RUN_ARGS
       (例: --staff medium)。script は env STREAM_RUN / STREAM_AUTHOR で差し替える (既定は隣の stream_run.py / stream_author.py —
       stream_make.sh が立てる)

- 著者の終わりは著者が書く stream/src.done (`stream_author.mark_done`)。著者の process が印を書かずに死んだら (kill・起動の失敗)
  監督が同じ形で書く — orchestrator は書けた所までで続ける (製品の DraftAuthorRun と同じ方針)
- 中断 (SIGINT / SIGTERM) は stream/engine.failed で orchestrator に伝え (server の abort)、両方の process group を回収する
"""

from __future__ import annotations

import json
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
    stream.mkdir(parents=True, exist_ok=True)
    done = stream / "src.done"
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
            # orchestrator は著者と同時に起こす — 起動直後の版の照合が著者の準備の影に入る (著者は call を起こす直前に結果を読む)
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
                if code is not None and not done.exists():
                    temporary = stream / "src.done.tmp"
                    temporary.write_text(json.dumps({"ended": False, "exit": code}) + "\n")
                    temporary.replace(done)
                time.sleep(0.1)
            author_code = author.poll()
            if (
                runner.returncode == 0 and author_code is None
            ):  # 印の後の著者の後始末 (予熱の記録) を少し待つ — 失敗した run は待たない
                try:
                    author_code = author.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    pass
            print(f"author exit {author_code} / run exit {runner.returncode}", flush=True)
            return runner.returncode
    except KeyboardInterrupt:
        (stream / "engine.failed").write_text("生成が中断されました\n")
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

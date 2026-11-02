#!/bin/bash
# 1 題材の stream 生成: 著者 (stream_author.py) と orchestrator (stream_run.py) を同時に走らせる。
# usage: stream_pipeline.sh <project> [--effort low] [--samples a.md,b.md]
#        (project = tmp/studio/<name>・params.txt と request.txt と studio/ が要る)。orchestrator の引数は env STREAM_RUN_ARGS (例: --staff medium)。
#        script は env STREAM_RUN / STREAM_AUTHOR で差し替える (既定は隣の stream_run.py / stream_author.py — stream_make.sh が立てる)
set -u
P=$1; shift
S=$(cd "$(dirname "$0")" && pwd)
PY=${PYTHON:-$([ -x /opt/venv/bin/python ] && echo /opt/venv/bin/python || echo python3)}
mkdir -p "$P/stream"
if [ "${NOLANG_STUDIO_ENGINE:-claude}" = codex ]; then
  exec "$PY" "$S/stream_codex_pipeline.py" "$P" "$@"
fi
$PY "${STREAM_AUTHOR:-$S/stream_author.py}" run "$P" "$@" > "$P/stream/author.out" 2>&1 &
A=$!
# orchestrator は著者と同時に起こす — 起動直後の版の照合が著者の準備の影に入る (著者は claude を起こす直前に結果を読む)
$PY "${STREAM_RUN:-$S/stream_run.py}" "$P" ${STREAM_RUN_ARGS:-} > "$P/stream/run.out" 2>&1
R=$?
wait $A
echo "author exit $? / run exit $R"

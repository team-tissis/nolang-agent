#!/bin/bash
# 1 題材の stream 生成: 著者 (stream_author.py) と orchestrator (stream_run.py) を同時に走らせる。
# usage: stream_pipeline.sh <project> [--effort low] [--samples a.md,b.md]
#        (project = tmp/studio/<name>・params.txt と request.txt と studio/ が要る)。orchestrator の引数は env STREAM_RUN_ARGS (例: --staff medium)
set -u
P=$1; shift
S=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$S/../.." && pwd)  # repo の root (agent_client/scripts の 2 つ上・plugin で入れた物なら pyproject は無い)
PY=${PYTHON:-$([ -x /opt/venv/bin/python ] && echo /opt/venv/bin/python || echo python3)}
if [ -f "$ROOT/pyproject.toml" ]; then cd "$ROOT"; RUN_ENV="PYTHONPATH=$ROOT STUDIO_SERVER_SOCK=$ROOT/tmp/studio/.server/sock"; else RUN_ENV=""; fi  # repo の外 (plugin) は --remote だけ
mkdir -p "$P/stream"
if [ "${NOLANG_STUDIO_ENGINE:-claude}" = codex ]; then
  exec env $RUN_ENV "$PY" "$S/stream_codex_pipeline.py" "$P" "$@"
fi
$PY "$S/stream_author.py" run "$P" "$@" > "$P/stream/author.out" 2>&1 &
A=$!
sleep 1
env $RUN_ENV $PY "$S/stream_run.py" "$P" ${STREAM_RUN_ARGS:-} > "$P/stream/run.out" 2>&1
R=$?
wait $A
echo "author exit $? / run exit $R"

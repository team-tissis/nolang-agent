#!/bin/bash
# 依頼文 1 つから stream (製品と同じ段取り: 著者 low 1 call → cut ごとの担当 medium → check / 直し → 素材 → 確定 → 投入 → 製品の DraftStreamRun が描く) で動画を作る。
# usage (repo root から):
#   bash .agents/skills/nolang-draft-studio/scripts/stream_make.sh tmp/studio/<name> --type concept|data|compare|story|cinematic \
#        (--request <file> | --request-text "…") [--aspect 16:9|9:16] [--seconds 60] [--effort low] [--staff medium|low] [--no-staff]
#        [--remote http://host:18000 --token nlg-c-…]   (描画を NoLang API に任せる = 製品の draft stream・視聴 URL が先に出る)
#        [--samples a.md,b.md | <file>]   (見本 2 本・file は 1 行目が `a.md,b.md` = 前の run の stream/samples.txt をそのまま渡せる。
#                                          省略時は reference/samples/ の <type>_NN 1 本 + hf_<type>_* 1 本 (同じ題材を除き同じ向きを先に) = stream_author.py の pick_samples)
# 出来上がり: <project>/studio/out/video.mp4 (再生開始の時点から製品の HLS (static/video_generate/<process>/) が伸びる)・stream/run.jsonl に時刻の記録。
# 前提は SKILL.md の「前提 (環境)」。著者と担当は `claude -p` なので claude CLI の login が要る。
set -eu
S=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$S/../../../.." && pwd)  # repo の root (plugin で入れた skill なら repo は無い → --remote だけ)
PY=${PYTHON:-$([ -x /opt/venv/bin/python ] && echo /opt/venv/bin/python || echo python3)}
[ $# -ge 1 ] || { sed -n 2,9p "$0"; exit 2; }
P=$($PY -c 'import os, sys; print(os.path.abspath(sys.argv[1]))' "$1"); shift  # project は絶対 path (repo の root へ cd しても同じ)
if [ -f "$ROOT/pyproject.toml" ]; then cd "$ROOT"; IN_REPO=1; else IN_REPO=""; fi
TYPE=""; ASPECT=16:9; SECONDS_=60; EFFORT=low; STAFF=medium; REQ_FILE=""; REQ_TEXT=""; SAMPLES=""; REMOTE=""; TOKEN=""; TEMPLATE=""
while [ $# -gt 0 ]; do
  case "$1" in
    --type) TYPE=$2; shift 2;;
    --aspect) ASPECT=$2; shift 2;;
    --seconds) SECONDS_=$2; shift 2;;
    --effort) EFFORT=$2; shift 2;;
    --staff) STAFF=$2; shift 2;;
    --no-staff) STAFF=""; shift;;
    --request) REQ_FILE=$2; shift 2;;
    --request-text) REQ_TEXT=$2; shift 2;;
    --samples) SAMPLES=$2; shift 2;;
    --remote) REMOTE=$2; shift 2;;
    --token) TOKEN=$2; shift 2;;
    --template) TEMPLATE=$2; shift 2;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done
[ -n "$TYPE" ] || { echo "--type が要る (concept|data|compare|story|cinematic)" >&2; exit 2; }
[ -n "$REQ_FILE" ] || [ -n "$REQ_TEXT" ] || { echo "--request <file> か --request-text が要る" >&2; exit 2; }
[ ! -e "$P/stream" ] || { echo "$P/stream が既にある (別の名にするか消す)" >&2; exit 2; }
if [ -n "$SAMPLES" ]; then
  if [ -f "$SAMPLES" ]; then SAMPLES=$(head -1 "$SAMPLES" | tr -d '[:space:]'); fi
  [ "$(echo "$SAMPLES" | tr ',' '\n' | grep -c .)" -ge 2 ] || { echo "--samples は 2 本以上 (a.md,b.md,…): $SAMPLES" >&2; exit 2; }
  for f in ${SAMPLES//,/ }; do [ -f "$S/../reference/samples/$f" ] || { echo "--samples: reference/samples/$f が無い" >&2; exit 2; }; done
fi
mkdir -p "$P"
echo "$TYPE $ASPECT $SECONDS_" > "$P/params.txt"
if [ -n "$REQ_FILE" ]; then cp "$REQ_FILE" "$P/request.txt"; else printf '%s\n' "$REQ_TEXT" > "$P/request.txt"; fi
[ -n "$IN_REPO" ] && export PYTHONPATH=$ROOT
[ -e "$P/studio/design.txt" ] || $PY "$S/studio_new.py" "$P/studio" "$TYPE" "$ASPECT" "$SECONDS_" | tail -1
if [ -n "$IN_REPO" ]; then $PY "$S/studio_server.py" start 2>&1 | head -1; fi   # 既に起動中なら何もしない (check / warm / 窓 / 束ねが Django の起動を毎回払わないため)
[ -n "$IN_REPO" ] || [ -n "$REMOTE" ] || { echo "repo の外では --remote <NoLang API> が要る (素材・描画は server)" >&2; exit 2; }
export STREAM_RUN_ARGS="${STAFF:+--staff $STAFF}${REMOTE:+ --remote $REMOTE}${TOKEN:+ --token $TOKEN}${TEMPLATE:+ --template $TEMPLATE}"
echo "stream: $P ($TYPE $ASPECT ${SECONDS_}s・著者 $EFFORT・担当 ${STAFF:-なし}・見本 ${SAMPLES:-type の既定})"
PYTHON=$PY bash "$S/stream_pipeline.sh" "$P" --effort "$EFFORT" ${SAMPLES:+--samples "$SAMPLES"}
$PY - "$P" <<'PYEOF'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1]); ev = [json.loads(l) for l in (p / "stream/run.jsonl").read_text().splitlines()]
by = lambda e: [x for x in ev if x.get("event") == e]
cuts = by("plan_seen")[0]["cuts"] if by("plan_seen") else []
asm = sorted(by("assemble"), key=lambda x: x["index"])
F = by("final_ready")[0]["since"] if by("final_ready") else None
# 落ちた cut = 最終版に入らなかった物 (窓の描き直しで通った cut は数えない)
dropped = sorted(set(by("final_ready")[0].get("broken", {}) if by("final_ready") else {}) | {x["cut"] for x in by("window_skipped")})
video = p / "studio/out/video.mp4"
if by("segment"):  # --organizer: 製品の HLS の segment (2 s) の時刻から
    segs = [x["since"] for x in sorted(by("segment"), key=lambda x: x["index"])]
    P = segs[0]; M = by("manifest_published")[0]["since"] if by("manifest_published") else None
    nostall = max(t - 2.0 * k for k, t in enumerate(segs))
    print(f"cut {len(cuts)}・最初の segment {round(P)} s・在庫 10 s の manifest {M and round(M)} s・止まらない開始 {round(nostall)} s・完成 {F and round(F)} s・落ちた cut {dropped or 'なし'}")
else:
    P = by("playable")[0]["since"] if by("playable") else None
    nostall = max((a["since"] - a["cut_start_s"] for a in asm), default=None)
    print(f"cut {len(cuts)}・再生開始 {P and round(P)} s・止まらない開始 {nostall and round(nostall)} s・完成 {F and round(F)} s・落ちた cut {dropped or 'なし'}")
if video.exists():
    print(f"video: {video} ({video.stat().st_size // 1024} KB)")
elif by("remote_started"):  # --remote: 描画と配信は server (手元に mp4 は無い)
    print(f"video: server — {by('remote_started')[0]['watch_url']} (status: GET /v1/videos/<id>/)")
else:
    print("video: なし (stream/run.out と weave/*/out/check_*.txt を見る)")
PYEOF

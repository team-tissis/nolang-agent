#!/bin/bash
# 依頼文 1 つから stream (製品と同じ段取り: 著者 low 1 call → cut ごとの担当 medium → check / 直し → 素材 → 確定 → 投入 → 製品の DraftStreamRun が描く) で動画を作る。
# usage (repo root から):
#   bash .agents/skills/nolang-draft-studio/scripts/stream_make.sh tmp/studio/<name> --type concept|data|compare|story|cinematic \
#        (--request <file> | --request-text "…") [--aspect 16:9|9:16] [--seconds 60|auto (指定なし)] [--effort low] [--staff medium|low] [--no-staff]
#        [--review low|medium|none] [--fix low] [--look]   (見直し = 1 回目の直し役が弱い所・崩れも探す・の effort / 2 回目以降の直し役の effort /
#                                                        見直しに cut の静止画も見せて 2 回 (local だけ・質を取りに行く mode))
#        [--editable]   (編集可能モード = 編集画面で調整できる文法サブセットに収める — 著者の作法 + check の profile + 投入の門の DEFECT)
#        [--ref <video_id>]   (参照の動画 = ユーザーが選んだテンプレか自分の動画。その src を著者に「ユーザーが選んだ形」として渡す・
#                              依頼文の `[video:<id>]` でも同じ。長さは --seconds が優先)
#        [--speech <speech_file_id>[,<id>]]   (持ち込み音声 = upload 済みの音声。server が文字起こしし、その clip を切って使う動画を作る・
#                                              --remote だけ)
#        [--remote http://host:18000 --token nlg-c-…]   (描画を NoLang API に任せる = 製品の draft stream・視聴 URL が先に出る)
#        [--samples a.md,b.md | <file>]   (見本 2 本・file は 1 行目が `a.md,b.md` = 前の run の stream/samples.txt をそのまま渡せる。
#                                          省略時は reference/samples/ の hf_<type>_* 2 本 (同じ題材を除き同じ向きを先に) = stream_author.py の pick_samples)
# 出来上がり: <project>/studio/out/video.mp4 (再生開始の時点から製品の HLS (static/video_generate/<process>/) が伸びる)・stream/run.jsonl に時刻の記録。
# 前提は SKILL.md の「前提 (環境)」。--engine claude (既定) / codex の CLI と login が要る。
set -eu
S=$(cd "$(dirname "$0")" && pwd)
ROOT=$(cd "$S/../../../.." && pwd)  # repo の root (plugin で入れた skill なら repo は無い → --remote だけ)
PY=${PYTHON:-$([ -x /opt/venv/bin/python ] && echo /opt/venv/bin/python || echo python3)}
[ $# -ge 1 ] || { sed -n 2,16p "$0"; exit 2; }
P=$($PY -c 'import os, sys; print(os.path.abspath(sys.argv[1]))' "$1"); shift  # project は絶対 path (repo の root へ cd しても同じ)
if [ -f "$ROOT/pyproject.toml" ]; then cd "$ROOT"; IN_REPO=1; else IN_REPO=""; fi
ENGINE=claude
TYPE=""; ASPECT=16:9; SECONDS_=60; EFFORT=low; STAFF=medium; REQ_FILE=""; REQ_TEXT=""; SAMPLES=""; REMOTE=""; TOKEN=""; FIX=low; REVIEW=low; LOOK=""; EDITABLE=""; REF=""; SPEECH=""
while [ $# -gt 0 ]; do
  case "$1" in
    --engine) ENGINE=$2; shift 2;;
    --editable) EDITABLE=1; shift;;
    --ref) REF=$2; shift 2;;
    --speech) SPEECH=$2; shift 2;;
    --type) TYPE=$2; shift 2;;
    --aspect) ASPECT=$2; shift 2;;
    --seconds) SECONDS_=$2; shift 2;;
    --effort) EFFORT=$2; shift 2;;
    --staff) STAFF=$2; shift 2;;
    --no-staff) STAFF=""; shift;;
    --fix) FIX=$2; shift 2;;
    --review) REVIEW=$2; shift 2;;
    --look) LOOK=1; shift;;
    --request) REQ_FILE=$2; shift 2;;
    --request-text) REQ_TEXT=$2; shift 2;;
    --samples) SAMPLES=$2; shift 2;;
    --remote) REMOTE=$2; shift 2;;
    --token) TOKEN=$2; shift 2;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done
case "$ENGINE" in claude|codex) ;; *) echo "--engine は claude / codex" >&2; exit 2;; esac
export NOLANG_STUDIO_ENGINE="$ENGINE"
if [ "$ENGINE" = codex ]; then
  command -v codex >/dev/null || { echo "codex がありません" >&2; exit 2; }
  [ -f "${CODEX_HOME:-$HOME/.codex}/auth.json" ] || { echo "Codex の auth.json がありません。codex login で file 保存の認証を用意してください" >&2; exit 3; }
  codex login status >/dev/null 2>&1 || { echo "codex login を先に実行してください" >&2; exit 3; }
fi
[ -n "$TYPE" ] || { echo "--type が要る (concept|data|compare|story|cinematic)" >&2; exit 2; }
[ -n "$REQ_FILE" ] || [ -n "$REQ_TEXT" ] || { echo "--request <file> か --request-text が要る" >&2; exit 2; }
[ ! -e "$P/stream" ] || { echo "$P/stream が既にある (別の名にするか消す)" >&2; exit 2; }
if [ -n "$SAMPLES" ]; then
  if [ -f "$SAMPLES" ]; then SAMPLES=$(head -1 "$SAMPLES" | tr -d '[:space:]'); fi
  [ "$(echo "$SAMPLES" | tr ',' '\n' | grep -c .)" -ge 2 ] || { echo "--samples は 2 本以上 (a.md,b.md,…): $SAMPLES" >&2; exit 2; }
  for f in ${SAMPLES//,/ }; do [ -f "$S/../reference/samples/$f" ] || { echo "--samples: reference/samples/$f が無い" >&2; exit 2; }; done
fi
mkdir -p "$P"
echo "$TYPE $ASPECT $SECONDS_${EDITABLE:+ editable}" > "$P/params.txt"
# 編集可能モード: 著者・担当・直しの prompt に editable の節が入り (stream_author.py が env を読む)、check と投入の門が
# profile=editable の規則を効かせる
[ -n "$EDITABLE" ] && export NOLANG_STUDIO_PROFILE=editable
if [ -n "$REQ_FILE" ]; then cp "$REQ_FILE" "$P/request.txt"; else printf '%s\n' "$REQ_TEXT" > "$P/request.txt"; fi
[ -n "$IN_REPO" ] && export PYTHONPATH=$ROOT
[ -e "$P/studio/design.txt" ] || $PY "$S/studio_new.py" "$P/studio" "$TYPE" "$ASPECT" "$SECONDS_" | tail -1
if [ -n "$IN_REPO" ]; then $PY "$S/studio_server.py" start 2>&1 | head -1; fi   # 既に起動中なら何もしない (check / warm / 窓 / 束ねが Django の起動を毎回払わないため)
[ -n "$IN_REPO" ] || [ -n "$REMOTE" ] || { echo "repo の外では --remote <NoLang API> が要る (素材・描画は server)" >&2; exit 2; }
export STREAM_RUN_ARGS="${STAFF:+--staff $STAFF} --review $REVIEW --fix $FIX${LOOK:+ --look}${EDITABLE:+ --editable}${REMOTE:+ --remote $REMOTE}${TOKEN:+ --token $TOKEN}"
# 参照の動画: --ref か依頼文の `[video:<id>]` (最初の 1 つ)。src と「ユーザーが選んだ形」の節を project/reference.json に (著者が読む)
[ -n "$REF" ] || REF=$(grep -oE '\[video:[0-9a-fA-F-]{36}\]' "$P/request.txt" | head -1 | sed -E 's/^\[video:(.*)\]$/\1/' || true)
if [ -n "$REF" ]; then
  # shellcheck disable=SC2086
  env ${IN_REPO:+PYTHONPATH=$ROOT} $PY "$S/stream_run.py" "$P" --fetch-ref "$REF" $STREAM_RUN_ARGS || echo "参照 $REF の src を取れない — 参照なしで書く (stream/run.jsonl の reference_failed)" >&2
fi
# 持ち込み音声: server の文字起こしの clip 台帳と `@clip` の書き方を project/speech.json に (著者が読む・転写を待つ)。取れなければ止める
if [ -n "$SPEECH" ]; then
  # shellcheck disable=SC2086
  env ${IN_REPO:+PYTHONPATH=$ROOT} $PY "$S/stream_run.py" "$P" --fetch-speech "$SPEECH" $STREAM_RUN_ARGS || { echo "持ち込み音声 $SPEECH の文字起こしを取れない (stream/run.jsonl の speech_failed)" >&2; exit 1; }
fi
echo "stream: $P ($TYPE $ASPECT ${SECONDS_}s・著者 $EFFORT・担当 ${STAFF:-なし}・見直し $REVIEW${LOOK:+ (静止画)}・直し $FIX${EDITABLE:+・編集可能モード}${REF:+・参照 $REF}${SPEECH:+・持ち込み音声 $SPEECH}・見本 ${SAMPLES:-type の既定})"
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

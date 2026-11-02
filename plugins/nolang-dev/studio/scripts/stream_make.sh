#!/bin/bash
# 依頼文 1 つから stream (製品と同じ段取り: 著者 low 1 call → cut ごとの担当 balanced → check / 直し → 素材 → 確定 → 投入 → 製品の DraftStreamRun が描く) で動画を作る。
# usage (配布の client — 描画は NoLang API (`--remote`)。repo の手元の run は repo の dev 入口 (studio_make.sh) が同じ引数で):
#   bash agent_client/scripts/stream_make.sh tmp/studio/<name> --type concept|data|compare|story|cinematic \
#        (--request <file> | --request-text "…") [--aspect 16:9|9:16] [--seconds 秒|auto (既定 auto = 台本の分量に合わせる)]
#        [--mode light|standard|plus|super]   (役の flag の組。light = 著者 low・担当なし・直し severe / standard = 既定 (著者 low・担当 balanced・直し severe) /
#                            plus = 著者 brief (low)・担当 balanced (素材も)・直し warn / super = 著者 high (brief なし)・担当 high (素材も)・レビュー medium・直し warn。
#                            後ろに書いた役の flag が組の値を上書きする)
#        役は 4 つ (著者・担当・レビュー・直し役)。flag は「役の名 → 強さ・none で外す」で、CLI `nolang make` と同じ名:
#        [--author low|medium|high|xhigh (著者の effort・既定 low)] [--author-brief]   (著者は台本 = 台詞・絵コンテ (`#` 1〜3 行)・transition と root だけを書き、
#                            絵は cut ごとの担当がゼロから設計する。台詞は著者の版のまま固定 (声は著者の時点から作り始める)。--staff-assets を含意・--staff none とは併用不可)
#        [--staff balanced (既定)|low|medium|high|xhigh|none] [--staff-warn (担当に warn の指摘も渡す・既定は DEFECT と severe だけ)]
#        [--staff-assets]   (担当が絵と台詞も変える・素材は担当の版から担当の後に作る。既定では担当は絵と台詞を変えず、絵と声は著者の版から担当と並列に作る)
#        [--review low|medium|none (既定 none)]   (レビュー = 担当の後に 1 回、cut の静止画 (warm の本物の絵を待って GPU で描く) と check の severe / warn 全部を見て、
#                            厳しい監督として指摘に出ない弱い所・崩れも探して直す call。--fix none とは併用不可。cut ごとに 25〜45 s 直列に乗る)
#        [--fix defect|severe|warn|none (既定 severe)]   (直し役 = check の指摘を直す call (effort low・2 回まで)。値は直す指摘の段: severe = DEFECT と severe
#                            (隠れる文字・画面の外 …) だけ・defect = DEFECT と隠れる文字だけ・warn = 台帳の severe / warn も・none = 直し役なし (DEFECT は機械の直しと最後の手段だけ))
#        [--editable]   (編集可能モード = 編集画面で調整できる文法サブセットに収める — 著者の作法 + check の profile + 投入の門の DEFECT)
#        [--ref <video_id>]   (参照の動画 = ユーザーが選んだテンプレか自分の動画。その src を著者に「ユーザーが選んだ形」として渡す・
#                              依頼文の `[video:<id>]` でも同じ。長さは --seconds が優先)
#        [--edit <video_id>]  (編集 = 完成した動画の stored src を種に、著者を飛ばして編集役 (Opus medium・1 call) が依頼のぶんだけ
#                              cut block を書き換える。不変の cut は担当も check も掛けず素通しで投入。依頼が作り直し級 (尺・縦横・
#                              全スタイル) なら著者経路 (--ref と同じ) へ自動で倒れる。--type は不要・縦横は親に合わせる)
#        [--speech <speech_file_id>[,<id>]]   (持ち込み音声 = upload 済みの音声。server が文字起こしし、その clip を切って使う動画を作る・
#                                              --remote だけ)
#        --remote http://host:18000 [--token <OAuth の access token>]   (描画を NoLang API に任せる = 製品の draft stream・視聴 URL が先に出る。
#                                          token の省略時は Claude Code の MCP の OAuth token)
#        [--samples a.md,b.md | <file>]   (見本 2 本・file は 1 行目が `a.md,b.md` = 前の run の stream/samples.txt をそのまま渡せる。
#                                          省略時は reference/samples/ の hf_<type>_* 2 本 (同じ題材を除き同じ向きを先に) = stream_author.py の pick_samples)
# 出来上がり: <project>/studio/out/video.mp4 (再生開始の時点から製品の HLS (static/video_generate/<process>/) が伸びる)・stream/run.jsonl に時刻の記録。
# 前提は SKILL.md の「前提 (環境)」。--engine claude (既定) / codex の CLI と login が要る。
set -eu
S=$(cd "$(dirname "$0")" && pwd)
PY=${PYTHON:-$([ -x /opt/venv/bin/python ] && echo /opt/venv/bin/python || echo python3)}
[ $# -ge 1 ] || { sed -n 2,29p "$0"; exit 2; }
P=$($PY -c 'import os, sys; print(os.path.abspath(sys.argv[1]))' "$1"); shift  # project は絶対 path (repo の root へ cd しても同じ)
ENGINE=claude
TYPE=""; ASPECT=16:9; SECONDS_=auto; EFFORT=low; STAFF=balanced; STAFF_WARN=""; REQ_FILE=""; REQ_TEXT=""; SAMPLES=""; REMOTE=""; TOKEN=""; FIX=severe; REVIEW=""; ASSETS=""; EDITABLE=""; REF=""; SPEECH=""; BRIEF=""; EDIT=""
# --mode = 役の flag の組 (先に読んで既定を置き換える・明示の役の flag が上書き)。表は CLI `nolang make` と同じ。
# 10-30 の bench (5 題材): solo (著者 medium だけ) は外した (著者 medium の思考で開始が 3〜4 倍遅く質は standard 以下)。レビューは plus に
# 足しても上積みが題材次第 (費用 +25%) なので plus には無く、super だけが持つ (super-B = 著者 high・担当 high + 素材・レビュー medium・直し warn
# が旧 super (brief medium) に Gemini 2 系で勝ち plus に全判定で勝った — ユーザー裁定で super の既定に)
MODE=""; _args=("$@"); for ((i=0; i<${#_args[@]}; i++)); do [ "${_args[$i]}" = --mode ] && MODE=${_args[$((i+1))]:-}; done
case "$MODE" in
  "") ;;
  light)    EFFORT=low;  BRIEF="";  STAFF="";       ASSETS="";  REVIEW="";       FIX=severe;;  # 速さ最優先: 著者だけ・DEFECT と severe だけ直す
  standard) EFFORT=low;  BRIEF="";  STAFF=balanced; ASSETS="";  REVIEW="";       FIX=severe;;  # 既定 (--mode を書かない時と同じ)
  plus)     EFFORT=low;  BRIEF=1;   STAFF=balanced; ASSETS=1;   REVIEW="";       FIX=warn;;    # 著者は台本だけ・担当が絵も設計・warn まで直す (長い説明系で standard に勝つ)
  super)    EFFORT=high; BRIEF="";  STAFF=high;     ASSETS=1;   REVIEW=medium;   FIX=warn;;    # 質を取りに行く: 著者 high・担当 high が素材も・レビュー (再生開始 6〜10 分・費用 plus の 2 倍)
  *) echo "--mode は light / standard / plus / super" >&2; exit 2;;
esac
while [ $# -gt 0 ]; do
  case "$1" in
    --mode) shift 2;;
    --engine) ENGINE=$2; shift 2;;
    --editable) EDITABLE=1; shift;;
    --ref) REF=$2; shift 2;;
    --edit) EDIT=$2; shift 2;;
    --speech) SPEECH=$2; shift 2;;
    --type) TYPE=$2; shift 2;;
    --aspect) ASPECT=$2; shift 2;;
    --seconds) SECONDS_=$2; shift 2;;
    --author) EFFORT=$2; shift 2;;
    --staff) STAFF=$2; [ "$STAFF" != none ] || STAFF=""; shift 2;;
    --staff-warn) STAFF_WARN=1; shift;;
    --fix) FIX=$2; shift 2;;
    --review) REVIEW=$2; [ "$REVIEW" != none ] || REVIEW=""; shift 2;;
    --staff-assets) ASSETS=1; shift;;
    --author-brief) BRIEF=1; shift;;
    --request) REQ_FILE=$2; shift 2;;
    --request-text) REQ_TEXT=$2; shift 2;;
    --samples) SAMPLES=$2; shift 2;;
    --remote) REMOTE=$2; shift 2;;
    --token) TOKEN=$2; shift 2;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done
case "$ENGINE" in claude|codex) ;; *) echo "--engine は claude / codex" >&2; exit 2;; esac
# 直し役の値は直す指摘の段 (effort は low 固定)。旧 `--fix low` (warn の直し + レビュー) は `--fix warn --review low`
case "$FIX" in
  defect|severe|warn|none) ;;
  low|medium|high|xhigh) echo "--fix は直す指摘の段 (defect|severe|warn|none)。warn まで直すなら --fix warn・レビューは --review" >&2; exit 2;;
  *) echo "--fix は defect / severe / warn / none" >&2; exit 2;;
esac
case "$REVIEW" in
  ""|low|medium) ;;
  *) echo "--review は low / medium / none" >&2; exit 2;;
esac
[ -z "$REVIEW" ] || [ "$FIX" != none ] || { echo "--review は直し役の機構で直す — --fix none とは併用できない" >&2; exit 2; }
export NOLANG_STUDIO_ENGINE="$ENGINE"
if [ "$ENGINE" = codex ]; then
  command -v codex >/dev/null || { echo "codex がありません" >&2; exit 2; }
  [ -f "${CODEX_HOME:-$HOME/.codex}/auth.json" ] || { echo "Codex の auth.json がありません。codex login で file 保存の認証を用意してください" >&2; exit 3; }
  codex login status >/dev/null 2>&1 || { echo "codex login を先に実行してください" >&2; exit 3; }
fi
[ -n "$TYPE" ] || { [ -n "$EDIT" ] && TYPE=concept; } || { echo "--type が要る (concept|data|compare|story|cinematic)" >&2; exit 2; }
if [ -n "$EDIT" ]; then
  [ -z "$SPEECH" ] || { echo "--edit と --speech は併用できない" >&2; exit 2; }
  [ -z "$BRIEF" ] || { echo "--edit と --author-brief は併用できない" >&2; exit 2; }
fi
# 著者 brief: 絵は担当が設計する前提 — 担当は必須・素材も担当が変える (固定)
if [ -n "$BRIEF" ]; then
  [ -n "$STAFF" ] || { echo "--author-brief は担当が各 cut を仕上げる前提 (--staff none と併用不可)" >&2; exit 2; }
  ASSETS=1
fi
[ -n "$REQ_FILE" ] || [ -n "$REQ_TEXT" ] || { echo "--request <file> か --request-text が要る" >&2; exit 2; }
[ ! -e "$P/stream" ] || { echo "$P/stream が既にある (別の名にするか消す)" >&2; exit 2; }
if [ -n "$SAMPLES" ]; then
  if [ -f "$SAMPLES" ]; then SAMPLES=$(head -1 "$SAMPLES" | tr -d '[:space:]'); fi
  [ "$(echo "$SAMPLES" | tr ',' '\n' | grep -c .)" -ge 2 ] || { echo "--samples は 2 本以上 (a.md,b.md,…): $SAMPLES" >&2; exit 2; }
  DOCS="$S/../reference"; [ -f "$DOCS/contract.json" ] || DOCS="$S/../../libs/ai/llm_prompts/draft_author/reference"
  for f in ${SAMPLES//,/ }; do [ -f "$DOCS/samples/$f" ] || { echo "--samples: reference/samples/$f が無い" >&2; exit 2; }; done
fi
mkdir -p "$P"
echo "$TYPE $ASPECT $SECONDS_${EDITABLE:+ editable}" > "$P/params.txt"
# 編集可能モード: 著者・担当・直しの prompt に editable の節が入り (stream_author.py が env を読む)、check と投入の門が
# profile=editable の規則を効かせる
[ -n "$EDITABLE" ] && export NOLANG_STUDIO_PROFILE=editable
if [ -n "$REQ_FILE" ]; then cp "$REQ_FILE" "$P/request.txt"; else printf '%s\n' "$REQ_TEXT" > "$P/request.txt"; fi
[ -e "$P/studio/design.txt" ] || $PY "$S/studio_new.py" "$P/studio" "$TYPE" "$ASPECT" "$SECONDS_" | tail -1
# 運ぶ先 (orchestrator) と著者の script — 既定は配布の物 (`--remote` = NoLang API)。repo の dev 入口 (studio_make.sh) が手元の run
# (STREAM_RUN) と比べ用の著者 (STREAM_AUTHOR) に差し替える
RUN=${STREAM_RUN:-$S/stream_run.py}; AUTHOR=${STREAM_AUTHOR:-$S/stream_author.py}; export STREAM_RUN=$RUN STREAM_AUTHOR=$AUTHOR
[ "$RUN" != "$S/stream_run.py" ] || [ -n "$REMOTE" ] || { echo "--remote <NoLang API> が要る (素材・描画は server)" >&2; exit 2; }
export STREAM_RUN_ARGS="${STAFF:+--staff $STAFF}${STAFF_WARN:+ --staff-warn} --fix $FIX${REVIEW:+ --review $REVIEW}${ASSETS:+ --staff-assets}${BRIEF:+ --author-brief}${EDITABLE:+ --editable}${REMOTE:+ --remote $REMOTE}${TOKEN:+ --token $TOKEN}"
# 参照の動画: --edit / --ref か依頼文の `[video:<id>]` (最初の 1 つ)。src と「ユーザーが選んだ形」の節を project/reference.json に (著者が読む)
[ -n "$REF" ] || REF=$EDIT
[ -n "$REF" ] || REF=$(grep -oE '\[video:[0-9a-fA-F-]{36}\]' "$P/request.txt" | head -1 | sed -E 's/^\[video:(.*)\]$/\1/' || true)
if [ -n "$REF" ]; then
  # shellcheck disable=SC2086
  $PY "$RUN" "$P" --fetch-ref "$REF" $STREAM_RUN_ARGS || {
    [ -z "$EDIT" ] || { echo "編集の対象 $EDIT の src を取れない (stream/run.jsonl の reference_failed)" >&2; exit 1; }
    echo "参照 $REF の src を取れない — 参照なしで書く (stream/run.jsonl の reference_failed)" >&2
  }
fi
# 持ち込み音声: server の文字起こしの clip 台帳と `@clip` の書き方を project/speech.json に (著者が読む・転写を待つ)。取れなければ止める
if [ -n "$SPEECH" ]; then
  # shellcheck disable=SC2086
  $PY "$RUN" "$P" --fetch-speech "$SPEECH" $STREAM_RUN_ARGS || { echo "持ち込み音声 $SPEECH の文字起こしを取れない (stream/run.jsonl の speech_failed)" >&2; exit 1; }
fi
# 編集 (--edit): 著者を飛ばし、編集役が stored src に依頼の patch を当てる。patch にならない依頼 (作り直し級・編集役の失敗) は
# 著者経路 (上で取った reference.json を参照に) へそのまま倒れる
RAN_EDIT=""
if [ -n "$EDIT" ]; then
  # 縦横は親の canvas から — start の aspect_ratio は親と一致していなければならない
  ASPECT=$($PY -c 'import json,re,sys,pathlib; ref=json.loads((pathlib.Path(sys.argv[1])/"reference.json").read_text()); m=re.search(r"^canvas (\d+)x(\d+)", str(ref["design"]), re.M); w,h=(int(m.group(1)),int(m.group(2))) if m else (1920,1080); print("9:16" if h>w else "16:9")' "$P")
  echo "$TYPE $ASPECT $SECONDS_${EDITABLE:+ editable}" > "$P/params.txt"
  echo "edit: $P (対象 $EDIT・$ASPECT・編集役 medium・直し $FIX)"
  EC=0
  # shellcheck disable=SC2086
  $PY "$AUTHOR" edit "$P" --effort medium > "$P/stream/editor.out" 2>&1 || EC=$?
  if [ $EC = 0 ]; then
    RAN_EDIT=1
    # shellcheck disable=SC2086
    $PY "$RUN" "$P" $STREAM_RUN_ARGS --edit > "$P/stream/run.out" 2>&1 || true
  elif [ $EC = 4 ]; then
    echo "edit: 変更なし — 項目の判定は $P/edit/verdict.json (patch の対象が無い)"
    exit 0
  else
    echo "edit: patch にならない (exit $EC — 判定は $P/edit/verdict.json) — 著者経路で作り直す (参照 $EDIT)"
  fi
fi
if [ -z "$RAN_EDIT" ]; then
  echo "stream: $P ($TYPE $ASPECT ${SECONDS_}$([ "$SECONDS_" = auto ] || echo s)・${MODE:+mode $MODE・}著者 $EFFORT${BRIEF:+ (brief = 台詞と絵コンテだけ)}・担当 ${STAFF:-なし}・直し $FIX${REVIEW:+・レビュー $REVIEW}${ASSETS:+・担当は素材も変える}${EDITABLE:+・編集可能モード}${REF:+・参照 $REF}${SPEECH:+・持ち込み音声 $SPEECH}・見本 ${SAMPLES:-type の既定})"
  PYTHON=$PY bash "$S/stream_pipeline.sh" "$P" --effort "$EFFORT" ${BRIEF:+--author-brief} ${SAMPLES:+--samples "$SAMPLES"}
fi
$PY - "$P" <<'PYEOF'
import json, pathlib, sys
p = pathlib.Path(sys.argv[1]); ev = [json.loads(l) for l in (p / "stream/run.jsonl").read_text().splitlines()]
by = lambda e: [x for x in ev if x.get("event") == e]
# 文書の版の照合 (stream_run の sync_reference) — gate は何も作らずに止まった run (exit 3)
sync = by("reference_sync")[-1] if by("reference_sync") else {}
if sync.get("status") == "gate":
    print(f"開始できない: {sync.get('message')}")
    sys.exit(3)
if sync.get("status") == "ready":
    print("注意: plugin の文書が server より古い — 今回は server の文書を取り直して書いた (`claude plugin update` で直る)")
elif sync.get("status") == "unknown":
    print(f"注意: 文書の版を照合できない ({sync.get('reason')}) — 焼き込みの文書で書いた")
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
    print(f"video: server — {by('remote_started')[0]['watch_url']} (status: GET /v1/unstable/videos/<id>/)")
else:
    print("video: なし (stream/run.out と stream/run.jsonl の check event を見る)")
PYEOF

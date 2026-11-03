"""stream の orchestrator — 著者 (stream_author.py・1 call) が落とす cut を出た順に check → 直し (低 effort の claude -p) → warm (絵・声) →
確定 → 投入。描画は製品の外部の著者の run (`authored_stream_run`) が seal ごとに HLS を伸ばす (cut 0 が seal された時点から再生
できる)。この script は NoLang の server (`--remote`) に運ぶ入口 (`RemoteRun`): 投入・先行解決 (warm)・check・改名・中断は nolang-api
`drafts/` の HTTP。cut の段は製品と共有の `cut_stages.CutStages` を `stream_stages.Run` が運ぶ (全 cut 同じで、cut の index でも運ぶ先でも分岐しない)。手元の機械で描く run は
repo にだけある dev 入口が `Run` を手元の flow 関数で実装して `main` に渡す (配布 bundle には無い)。

cut ごとの段 (asyncio の task・cut ごとに並列):
  受け (前の cut が使う定義はそちらへ移す) → 著者版 check → 担当 (Opus medium) → check + 直し (2 回まで・担当の直後と最初の DEFECT 0 の
  check で warm を頼む) → staged (ready) → 投入 (構成の順・投入検査で弾かれた cut は直し役を 1 回・別枠)。
  直しきれない DEFECT は捨てる前に最後の手段 (著者版に差し替え → DEFECT の印を落として台詞を残す・last_resort) を掛ける。
根の規則: 名のある定義 (def・motion・run・svg・sound・image・cue) は初めて使う cut の block に書き、その cut だけが直す。根 (設定・cast・字幕と
BGM の開き・常設の層) の持ち主は最初の live な cut — その直し役だけが根を直し、根はその cut が受理された時に凍る。壊れた cut の定義は
次の live な cut の block へ移る。
cut を跨ぐ待ちは 投入の順・持ち主待ち (他の cut の行の DEFECT で check が止まった時だけ・相手は持ち主 1 つ) だけ。素材 (絵・声) は
run が warm の頼みで先に作る (頼んだ cut の check と直しは待たない)。

usage: python stream_run.py <project> [--staff balanced|low|medium|high|xhigh|none] [--staff-warn] [--staff-assets]
  [--fix defect|severe|warn|none] [--review low|medium]   (役は 4 つ: 著者・担当・レビュー・直し役。flag の名は CLI `nolang make` と同じ)
  [--no-stills]   (bench 専用の knob — レビューに静止画を見せない)
  --remote http://host:18000 [--token <OAuth の access token>] = 投入先を NoLang API (製品の draft stream・server が描く) にする。視聴 URL を `WATCH …`
    の 1 行で出す (token は OAuth の access token — --token か env NOLANG_TOKEN (`eval "$(nolang auth env)"`)・無ければ Claude Code が
    `/mcp` の OAuth で得た token。CLI / MCP の窓口は API key を受けない (403))。
  --staff = 担当 (Opus・cut をプロの解説動画の密度と階層に仕上げる) を全 cut に、cut ごとに並列に (前の cut は著者の版を参考に渡す)。
    値は担当の effort (`none` = 担当なし)。`balanced` = cut 1・2 は low・cut 3 以降は medium の見込み完了が止まらない再生に間に合う時だけ medium
    (間に合わない見込みなら low に落とす。開始 中央 約 90 s・全 cut medium は約 130 s で止まらないは 6/10・質は小さく落ちる)。
  --staff-warn = 担当に warn の指摘も渡す (既定は DEFECT と severe だけ — 直し役の `--fix warn` と同じ向きの opt-in。担当の思考が伸びる)。
  --review = レビューの effort (`--mode super` が medium で持つ・既定 none): 担当の後に 1 回、厳しい監督として指摘に出ない弱い所・崩れも探して自分で直す call
    (指摘の無い cut も呼ぶ。check の severe / warn は常に全部見せる)。`--fix` の段とは独立 (直し役の 2 回の上限に数えない) — ただし直し役の
    機構で直すので `--fix none` とは併用不可。既定は cut の静止画も見る (REVIEW_ROUNDS = 1 回): 担当の後、warm が解いた本物の絵を待って cut を
    GPU で描く (server の GPU の worker `drafts/{id}/stills/`)。
    `--no-stills` = 静止画を撮らず doc と全指摘だけを見る (warm を待たず担当の check の直後に走る)。
    10-30 の mode bench: plus に足すと cut ごとに 25〜45 s 直列・費用 +25% で上積みは data / compare / story だけ → plus には無い。super (著者 high・
    担当 high + 素材・レビュー medium・直し warn) では旧 super (brief medium) に Gemini 2 系で勝ち plus に全判定で勝った → super の既定 (ユーザー裁定)。
  --fix = 直し役が直す指摘の段 (effort は low 固定)。既定 `severe` = DEFECT と severe の指摘 (隠れる文字・画面の外 …) だけ直し役を呼ぶ (warn は
    直さない — 担当後の severe は cut の 9% で、大半は担当が作る)。`defect` = DEFECT と隠れる文字 (severe の occluded) だけ。`warn` = 台帳の
    直しの列の warn も直す。`none` = 直し役も呼ばない (DEFECT は機械の直しと最後の手段 — 著者の版・DEFECT の印を落とす — だけ)。
  担当は既定で絵 (説明文) と台詞を変えない (変えていれば著者の版に戻す)。絵と声は著者の cut が届いた時点で warm に頼み、担当と並列に
    作る。--staff-assets = 担当が絵と台詞も変えてよい (素材は担当の版から・担当の後に作る)。
  既定 (担当 medium・素材は著者の版・DEFECT だけ直す) の根拠: 10-26 の 4 題材 bench で、担当 + 素材は著者の版 + 直しなしが、担当 + レビュー +
    直しに Opus 両順 3 勝 1 分・担当なしに 4 勝・最初の segment 中央 118 → 87 s (担当なし 70 s)・担当後の DEFECT 0/21 cut。DEFECT だけの
    直し役は、落ちる cut を減らす網 (DEFECT が無ければ呼ばれない)。
  直し役に回す規則は製品の台帳 (`drafts/rules/` の fixed)。最後の cut 以外の doc は open_ended (後に cut が続く prefix) で check する。
記録: project/stream/run.jsonl (event ごとの時刻・製品の segment の時刻も)・最終 project/studio/out/video.mp4 と、流した doc を
studio/ (design.txt・timeline.txt・src.json) に書き戻した物。solo/ の cut は著者の版 author_cut_<名>・担当の版 staff_cut_<名>・最終
cut_<名>。
"""

from __future__ import annotations

import functools
import http.client
import json
import os
import shutil
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from stream_api import (  # noqa: E402 — 隣の file (scripts dir を sys.path に足した後)
    Rejected,
    RemoteApi,
    Unreachable,
    claude_mcp_token,
    reference_cache_root,
)
from stream_author import author_core  # noqa: E402
from stream_stages import Run, RunOptions  # noqa: E402

# 持ち込み音声の転写を待つ上限 (`drafts/speeches/` が ready になるまで — 1 時間の音声で数分) と問い合わせの間隔
SPEECH_WAIT_S = 15 * 60
SPEECH_POLL_S = 5
# remote の静止画 (`drafts/{id}/stills/`) を待つ上限 — server は warm の絵を 90 s まで待ってから実現・描画する
REMOTE_SHOTS_TIMEOUT_S = 240
# 開始 (`POST drafts/`) が本人の同時生成の上限 (429 CONCURRENT_GENERATION_LIMIT) で断られた時に枠が空くのを待つ上限と送り直しの間隔
# — CLI `nolang make` の締切 420 s から plan (20〜40 s) を引いた内側に収める
START_WAIT_S = 300
START_POLL_S = 15


class RemoteRun(Run):
    """NoLang API (nolang-api consumer・製品の draft stream) に運ぶ run。著者・担当・直しはこの機械の claude -p のまま、確定した cut の
    stream の text を `unstable/drafts/{id}/cuts/` へ投入し、素材・描画・配信は server に任せる。根は閉じた時点で根だけを先に流し
    (`submit_root`)、以後凍る。"""

    def __init__(self, project: Path, options: RunOptions, *, remote: str, token: str | None) -> None:
        super().__init__(project, options)
        # 焼き込みの文書一式 (bundle では scripts の隣・repo では libs の正本) の版 — server の版との照合 (`sync_reference`)・
        # start の client_contract・全 request の X-NoLang-Client (server がずれた client の分布を測る)
        baked = author_core.resolve_reference_dir(HERE)
        contract = author_core.read_contract_json(baked).get("contract")
        if not isinstance(contract, int):
            raise ValueError(f"{baked}/contract.json: contract が整数でない")
        self.client_contract = contract
        self.baked_hash = author_core.reference_hash_of(baked)
        self.api = RemoteApi(remote, token, contract=self.client_contract, reference_hash=self.baked_hash, log=self.log)
        self.watch_url = ""  # 視聴 URL (`WATCH` / `PLAYABLE` の行に出す)

    def call(self, op: str, body: dict[str, object] | None = None, **path_args: str) -> dict[str, object]:
        return self.api.call(op, body, video_id=self.video_id, **path_args)

    def render_shots(self, c: str, dd: Path, t: float) -> list[Path]:
        """doc (根 + c) を server の GPU の worker に描かせ (`drafts/{id}/stills/` — warm の絵の pin は server が
        待つ)、出来た絵を dd/out/shots/ に落とす。c の DEFECT の行は check で引いて落としてから頼む。頼みの失敗・時間切れは
        空 (画像なしで見直す)。"""
        out = dd / "out/shots"
        shutil.rmtree(out, ignore_errors=True)
        out.mkdir(parents=True)
        try:
            for _attempt in range(3):
                _report, defects, _lint = self.check(dd, ended=not (dd / "OPEN_ENDED").exists(), focus=c)
                if not any(d.level == "DEFECT" for d in defects) or not self.drop_defect_lines(dd, c):
                    break
        except (Rejected, RuntimeError, OSError) as e:
            self.log(cut=c, event="shots", s=round(time.time() - t, 1), n=0, ok=False, error=str(e)[:300])
            return []
        body: dict[str, object] = {
            "design": (dd / "design.txt").read_text(),
            "timeline": (dd / "timeline.txt").read_text(),
            "cut": c,
            "open_ended": (dd / "OPEN_ENDED").exists(),
        }
        try:
            job = str(self.call("stills", body)["job_id"])
            deadline = time.time() + REMOTE_SHOTS_TIMEOUT_S
            state: dict[str, object] = {"status": "pending"}
            while state.get("status") == "pending" and time.time() < deadline:
                time.sleep(3)
                state = self.call("stills_status", job=job)
        except (Rejected, RuntimeError, OSError) as e:
            self.log(cut=c, event="shots", s=round(time.time() - t, 1), n=0, ok=False, error=str(e)[:300])
            return []
        raw = state.get("shots")
        paths: list[Path] = []
        for shot in raw if isinstance(raw, list) else []:
            path = out / str(shot["name"])
            try:
                with urllib.request.urlopen(str(shot["url"]), timeout=60) as resp:
                    path.write_bytes(resp.read())
            except OSError:
                continue
            paths.append(path)
        self.log(
            cut=c,
            event="shots",
            s=round(time.time() - t, 1),
            n=len(paths),
            ok=state.get("status") == "done",
            error=str(state.get("error") or "")[:300] or None,
            unwarmed=state.get("unwarmed") or None,
        )
        raw_unwarmed = state.get("unwarmed")
        self.shot_unwarmed[c] = [str(name) for name in raw_unwarmed] if isinstance(raw_unwarmed, list) else []
        return paths

    def fetch_speech(self, speech_ids: str) -> int:
        """持ち込み音声 (`--speech <id>[,<id>]`) の clip 台帳と著者に貼る節 (製品の著者と同じ文 — 正本は server) を受けて
        project/speech.json に書く (著者が読む)。`POST drafts/speeches/` が未転写の音声の転写を起こすので、ready になるまで待つ。
        取れなければ止める (戻り 1)。"""
        _kind, _aspect, seconds = (self.project / "params.txt").read_text().split()[:3]
        body: dict[str, object] = {"speech_file_ids": [x for x in speech_ids.split(",") if x], "language": "ja"}
        if seconds.isdigit():
            body["seconds"] = int(seconds)
        deadline = time.time() + SPEECH_WAIT_S
        transcribing = False
        while True:
            try:
                got = self.api.post("/v1/unstable/drafts/speeches/", body)
            except (urllib.error.URLError, ValueError) as e:
                self.log(event="speech_failed", error=str(e)[:300])
                return 1
            if got.get("status") == "ready":
                (self.project / "speech.json").write_text(json.dumps(got, ensure_ascii=False))
                self.log(event="speech", sources=got.get("sources"), target_seconds=got.get("target_seconds"))
                return 0
            if got.get("status") != "transcribing" or time.time() > deadline:
                self.log(event="speech_failed", error=str(got)[:300])
                return 1
            if not transcribing:
                print("持ち込み音声を文字起こし中 …", flush=True)
                transcribing = True
            time.sleep(SPEECH_POLL_S)

    def fetch_reference(self, video_id: str) -> int:
        """参照の動画 (`--ref` / 依頼の `[video:id]`) の src と「ユーザーが選んだ形」の節を受けて project/reference.json に書く
        (著者が読む・`GET drafts/templates/{id}/`)。節の文は server が
        組む (正本 `reference_brief.py`) — 依頼の秒数と editable を渡す。取れなければ参照なしで続ける (戻り 1)。"""
        _kind, _aspect, seconds = (self.project / "params.txt").read_text().split()[:3]
        profile = "editable" if self.editable else None
        query = urllib.parse.urlencode(
            {k: v for k, v in (("profile", profile), ("seconds", seconds if seconds.isdigit() else None)) if v}
        )
        try:
            got = self.api.get(f"/v1/unstable/drafts/templates/{video_id}/" + (f"?{query}" if query else ""))
        except (OSError, ValueError) as e:
            self.log(event="reference_failed", video_id=video_id, error=str(e)[:300])
            return 1
        if got.get("status") == 400 or not got.get("brief"):
            self.log(event="reference_failed", video_id=video_id, error=str(got.get("error") or got)[:300])
            return 1
        (self.project / "reference.json").write_text(json.dumps(got, ensure_ascii=False))
        self.log(event="reference", video_id=video_id, title=got.get("title"))
        return 0

    def sync_reference(self) -> None:
        """起動直後に著者と並走して、焼き込みの文書を server の版と照合する (著者は待たずに準備を進め、claude を起こす直前に結果を
        読む)。状態: match / fetching → ready (取り直した束の dir) / gate (版の契約
        の外 — 著者も orchestrator も始めない) / unknown (旧 server・失敗 — 焼き込みで続ける)。"""
        try:
            self.rules_payload = self.call("rules")
        except (Unreachable, RuntimeError, OSError, ValueError) as e:
            self.write_sync(status="unknown", reason=f"rules: {e}"[:300])
            return
        sync = self.rules_payload.get("sync")
        if not isinstance(sync, dict):
            self.write_sync(status="unknown", reason="server が版を返さない (古い server)")
            print("注意: 接続先の server が文書の版を返さない — 焼き込みの文書で書く", flush=True)
            return
        server_contract, min_supported, server_hash = (
            sync.get("contract"),
            sync.get("min_supported"),
            str(sync.get("reference_hash") or ""),
        )
        if isinstance(min_supported, int) and self.client_contract < min_supported:
            self.write_sync(
                status="gate",
                message=f"この NoLang plugin (contract {self.client_contract}) は server ({min_supported} 以上) より古い"
                " — `claude plugin update` で plugin を更新して",
            )
            return
        if isinstance(server_contract, int) and self.client_contract > server_contract:
            self.write_sync(
                status="gate",
                message=f"接続先の server (contract {server_contract}) がこの plugin (contract {self.client_contract})"
                " より古い — 接続先を確かめて",
            )
            return
        if server_hash == self.baked_hash:
            self.write_sync(status="match")
            return
        cached = reference_cache_root() / server_hash
        if (cached / "contract.json").is_file():
            self.write_sync(status="ready", reference_dir=str(cached), reference_hash=server_hash, cached=True)
            return
        self.write_sync(status="fetching", reference_hash=server_hash)
        t = time.time()
        try:
            self.api.fetch_reference_bundle(server_hash, cached)
        except (OSError, ValueError, tarfile.TarError) as e:
            self.write_sync(status="unknown", reason=f"取り直せない: {e}"[:300])
            print(
                "注意: server の文書を取り直せない — 焼き込みの文書で書く (`claude plugin update` で直る)", flush=True
            )
            return
        self.write_sync(
            status="ready", reference_dir=str(cached), reference_hash=server_hash, s=round(time.time() - t, 2)
        )
        print(
            "注意: plugin の文書が server より古い — 今回は server の文書を取り直して書く (`claude plugin update` で直る)",
            flush=True,
        )

    def start(self) -> None:
        """run を開く (plan が閉じた時点・`POST drafts/`)。視聴 URL はこの時点で出る (server の video page が追いかけ再生する)。"""
        t = time.time()
        kind, aspect, seconds = (self.project / "params.txt").read_text().split()[:3]
        title = (self.project / "request.txt").read_text().strip().splitlines()[0][:200]
        body: dict[str, object] = {"title": title, "aspect_ratio": aspect, "language": "ja"}
        if seconds.isdigit():  # `auto` (長さの指定なし) は送らない
            body["duration_s"] = int(seconds)
        if self.editable:
            body["editable"] = True
        reference = self.project / "reference.json"
        if reference.is_file():  # 参照から作る run — editable の線を参照の量まで緩める (server が参照を測る)
            body["reference_video_id"] = json.loads(reference.read_text())["template_video_id"]
        if speech_ids := self.speech_file_ids():  # 持ち込み音声 — 投入検査と worker が同じ clip 台帳で `@clip` を解く
            body["speech_file_ids"] = speech_ids
        # server の受ける範囲の外なら課金の前に弾かれる (gate の正本は server)
        body["client_contract"] = self.client_contract
        waits = 0
        while True:
            try:
                r = self.api.open("/v1/unstable/drafts/", body)
                break
            except urllib.error.HTTPError as e:
                # 本人の同時生成の上限 (429 CONCURRENT_GENERATION_LIMIT) は server が課金の前に判定する (api_draft_view: 同時上限 →
                # 課金の順) ので、断られても課金は無く送り直して安全 — 前の動画の完成で枠が空くので START_WAIT_S まで待って送り直す
                # (著者は書き続け、watch_author は src.done の後にも全 cut を拾う)。同じ 429 でもクレジット不足は待っても直らない
                # ので、判定は status でなく本文の error_code で。断った理由はこの行を CLI が run.out から error に載せる
                detail = e.read().decode("utf-8", "replace")[:600]
                try:
                    error_code = json.loads(detail).get("error_code")
                except (ValueError, AttributeError):
                    error_code = None
                waited = round(time.time() - t)
                if e.code == 429 and error_code == "CONCURRENT_GENERATION_LIMIT" and waited < START_WAIT_S:
                    waits += 1
                    self.log(event="start_waiting", n=waits, waited_s=waited)
                    print(f"WAITING 本人の同時生成の上限 — 前の動画の完成で枠が空くのを待つ {waited}s", flush=True)
                    time.sleep(START_POLL_S)
                    continue
                error = f"HTTP {e.code} {detail}"
                self.log(event="start_rejected", status=e.code, error=error, waited_s=waited)
                print(f"開始できない: {error}", flush=True)
                return
            except (urllib.error.URLError, http.client.HTTPException, ConnectionError, TimeoutError) as e:
                # 届かない・返事を失った: サーバーが受け付けたかは分からない (受け付けていれば視聴 URL の画面で続きが見える)
                self.log(event="start_unreachable", error=repr(e)[:400])
                print(f"開始できない (届かない・受け付けたかは不明): {e!r}"[:600], flush=True)
                return
        self.video_id = str(r["video_id"])
        self.watch_url = str(r["watch_url"])
        self.log(event="started", s=round(time.time() - t, 1), video_id=self.video_id, watch_url=self.watch_url)
        print(f"WATCH {self.watch_url}", flush=True)

    def wait(self) -> int:
        """server の完成 (status completed) を待つ。途中、見る人が再生を始められる時点 (status の `playable` = 公開 manifest が S3 に
        載った) を 1 回だけ `playable` に記録して `PLAYABLE <url>` を出す (stream_make の集計が読む)。
        poll の 1 回の失敗 (reload 中の 500 等) では止めない — 続けて失敗する時だけ諦める。"""
        playable_seen = False
        failures = 0
        while True:
            if self.engine_failed():
                return self.abort_engine()
            try:
                r = self.api.get(f"/v1/unstable/videos/{self.video_id}/")
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
                failures += 1
                self.log(event="remote_poll_failed", n=failures, error=str(e)[:200])
                if failures >= 20:
                    return 1
                time.sleep(3)
                continue
            failures = 0
            if not playable_seen and r.get("playable"):
                playable_seen = True
                self.log(event="playable", video_id=self.video_id)
                print(f"PLAYABLE {self.watch_url}", flush=True)
            st = str(r.get("status"))
            if st in ("completed", "failed", "expired"):
                if st == "completed":
                    self.write_back()
                self.log(
                    event="final_ready" if st == "completed" else "final_failed",
                    since_launch=round(time.time() - self.t0, 1),
                    status=st,
                    broken=self.broken,
                )
                return 0 if st == "completed" else 1
            time.sleep(3)


def main(argv: list[str], make_run: Callable[[Path, RunOptions], Run] | None = None) -> int:
    """make_run = 運ぶ先の run を作る物 (既定は `--remote` の `RemoteRun` — repo の dev 入口は手元の run を渡す)。"""
    if not argv:
        print(__doc__)
        return 2
    project = Path(argv[0]).resolve()
    staff = argv[argv.index("--staff") + 1] if "--staff" in argv else None
    staff = None if staff == "none" else staff
    fix_arg = argv[argv.index("--fix") + 1] if "--fix" in argv else "severe"
    if fix_arg not in ("defect", "severe", "warn", "none"):
        print(
            f"--fix は直す指摘の段 (defect|severe|warn|none): {fix_arg!r} — warn まで直すなら --fix warn・レビューは --review",
            file=sys.stderr,
        )
        return 2
    fix = None if fix_arg == "none" else "low"  # 直し役の effort は low 固定 (値は段)
    review = argv[argv.index("--review") + 1] if "--review" in argv else "none"
    if review != "none" and fix is None:
        print("--review は直し役の機構で直す — --fix none とは併用できない", file=sys.stderr)
        return 2
    if make_run is None:
        if "--remote" not in argv:
            print("--remote <NoLang API> が要る (素材・描画・配信は server)", file=sys.stderr)
            return 2
        remote = argv[argv.index("--remote") + 1]
        token = argv[argv.index("--token") + 1] if "--token" in argv else os.environ.get("NOLANG_TOKEN")
        make_run = functools.partial(RemoteRun, remote=remote, token=token or claude_mcp_token(remote))
    run = make_run(
        project,
        RunOptions(
            staff=staff,
            staff_warn="--staff-warn" in argv,
            fix=fix,
            review=None if review == "none" else review,
            fix_scope=fix_arg,
            stills="--no-stills" not in argv,
            keep_assets="--staff-assets" not in argv,
            brief="--author-brief" in argv,
            editable="--editable" in argv,
            edit="--edit" in argv,
        ),
    )
    if (
        "--fetch-ref" in argv
    ):  # 参照の動画の src を project/reference.json に (stream_make.sh が著者の起動前に 1 回呼ぶ)
        (project / "stream").mkdir(parents=True, exist_ok=True)
        return run.fetch_reference(argv[argv.index("--fetch-ref") + 1])
    if (
        "--fetch-speech" in argv
    ):  # 持ち込み音声の clip 台帳を project/speech.json に (stream_make.sh が著者の起動前に 1 回呼ぶ)
        (project / "stream").mkdir(parents=True, exist_ok=True)
        return run.fetch_speech(argv[argv.index("--fetch-speech") + 1])
    launch = project / "stream/author.jsonl"
    if launch.exists():
        for l in launch.read_text().splitlines():
            r = json.loads(l)
            if r.get("event") == "launch":
                run.t0 = float(r["t"])
    return run.run()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

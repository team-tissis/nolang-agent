# studio の実行エンジン

`stream_make.sh` の `--engine claude|codex` で著者・担当・修正役をまとめて選ぶ。
未指定時は Claude。既存のモデル・プロンプト・effort・予熱・TTLを維持する。
`NOLANG_STUDIO_ENGINE` は子プロセスに選択を伝える内部変数であり、外部からの設定入口にはしない。

Codex は `stream_codex.py` が `codex app-server` の stdio を扱い、本文差分を既存の Splitter に渡す。
対応確認は codex-cli 0.162.0。元の CODEX_HOME の auth.json を一時環境から共有し、設定・hooks・plugins・MCP・会話履歴は持ち込まない。
モデルは CLI の既定を使用し、実際のモデル・effort を author.jsonl、本文と usage 通知を codex_<役割>.jsonl に記録する。
API key 環境変数のみ・keyring のみの認証は現在対象外。画像つき見直しは localImage で渡す。

共通のプロンプト生成は両エンジンで行い、Claude 専用の cache 予熱は Codex では実行しない。
Codex の著者と投入側は stream_codex_pipeline.py が別プロセスグループで監視する。
役割の例外と著者の異常終了は stream/engine.failed で投入側に伝え、既存の abort に進む。
end は著者の src.done を確認してから送る。確定済み cut の再送や別エンジンへの切替は行わない。
終了時は役割の子プロセスと app-server を回収する。

外部 LLM を呼ばない契約テスト:

```bash
python3 -m unittest discover -s agent_client/tests
```

## 置き場と配布

この dir (`agent_client/scripts/`) は nolang-agent plugin へ写す配布 client。server のどの層からも import しない (importlinter
の `agent-client-is-shipped-code`)。prompt と出力の読みの正本 `author_core.py`・cut の段の状態機械の正本 `cut_stages.py` と文書一式 (`reference/` — 文法・見本・骨組み・
`contract.json`) は `libs/ai/llm_prompts/draft_author/` に 1 つだけ置き、repo 内ではそこを読む。配布 bundle は
`studio/{scripts,reference,tests}` の形で、sync (nolang-agent `scripts/sync-reference.mjs` の `STUDIO_FILES`) が `author_core.py`・
`cut_stages.py` を scripts の隣に (`stream_author._shipped` が隣か libs の正本を読む)、`reference/` を contract.json の
`reference` の列どおりに同梱する。dev 専用の script (studio.py・studio_server.py・stream_gemini.py …) は
`.agents/skills/nolang-draft-studio/scripts/` に残り、配布しない。配布 script は `.agents` を参照しない。

## orchestrator の分け方

| file | 責務 |
|---|---|
| `cut_stages.py` (libs に正本・同梱) | cut の段の状態機械 (`CutStages` — 受け・check・直し・戻し・最後の手段・autofix・投入の順)。製品の `DraftAuthorRun` と 1 本 |
| `stream_stages.py` | client の I/O (`Run(CutStages)` — 担当・file への書き通し・shots・`call` / `start` / `wait` / `render_shots` …の抽象) |
| `stream_api.py` | 受け口の答えの形 (`Defect`・`Rejected`・`Unreachable`・`read_answer`)・NoLang API の HTTP (`RemoteApi`)・文書一式の取り直し |
| `stream_run.py` | 配布の入口 (`main`)・server に運ぶ `RemoteRun` (`--remote` が要る) |

cut の text の操作は全部 `author_core`、段の進め方は全部 `cut_stages` (製品の `application/video_draft/draft_author/orchestrator.py` と同じ物)。repo の手元の run は
`.agents/skills/nolang-draft-studio/scripts/stream_local.py` (`LocalRun` を `stream_run.main` に渡す) で、入口 `studio_make.sh` が
env `STREAM_RUN` (orchestrator)・`STREAM_AUTHOR` (著者) で `stream_make.sh` / `stream_pipeline.sh` / `stream_codex_pipeline.py` に渡す。
Claude のプロンプトを保つ変更では、文法・見本などの無関係な同期を混ぜない。

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
python3 -m unittest discover -s .agents/skills/nolang-draft-studio/tests
```

nolang-agent への配布では scripts/sync-reference.mjs のコピー対象も更新する。
Claude のプロンプトを保つ変更では、文法・見本などの無関係な同期を混ぜない。

#!/usr/bin/env bash
# nolang-local につながるかを確かめる。localhost の 3 つの口が NoLang のスタックに届いているかを見る。
#   18000 = API (MCP)       401 が正常 (ログイン前)
#   8000  = ログイン (OAuth) 200 が正常
#   3000  = 視聴ページ       200 / 3xx が正常 (watch_url を開くのに使う)
set -u

# 転送や backend の再読み込みで最初の 1 回だけ応答しない事があるので、000 は 3 回まで試す
probe() {
  local code
  for _ in 1 2 3; do
    code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 "$1" 2>/dev/null || true)
    [ "$code" != 000 ] && break
    sleep 1
  done
  echo "$code"
}

ok=1
api=$(probe http://localhost:18000/agent/mcp)
auth=$(probe http://localhost:8000/.well-known/oauth-authorization-server)
web=$(probe http://localhost:3000/)

report() { # 名前 実際 期待の説明 正常か
  if [ "$4" = 1 ]; then echo "OK   $1 -> $2"; else echo "NG   $1 -> $2 ($3)"; ok=0; fi
}
report "localhost:18000/agent/mcp (API)" "$api" "401 が正常" "$([ "$api" = 401 ] && echo 1 || echo 0)"
report "localhost:8000 (ログイン)" "$auth" "200 が正常" "$([ "$auth" = 200 ] && echo 1 || echo 0)"
case "$web" in 2??|3??) w=1 ;; *) w=0 ;; esac
report "localhost:3000 (視聴ページ)" "$web" "200 か 3xx が正常" "$w"

if [ "$ok" = 1 ]; then
  echo
  echo "つながっています。Claude Code で nolang-local を認証すれば使えます。"
  exit 0
fi

cat <<'EOF'

つながっていない口があります。
- 000 = その port で誰も待っていない。NoLang のスタックへの転送 (SSH の LocalForward など) が張られているか確かめてください。
  転送は「Claude Code が動いている機械」の localhost に必要です。手元の PC の転送は、リモートの機械で動く Claude Code には効きません。
- 400 = Django の ALLOWED_HOSTS に弾かれている。localhost ではなく IP で届いている可能性があります。
- 18000 だけ 404 / 5xx = スタックは届いているが MCP が動いていない (backend の起動状態を管理者に確認)。
詳しくは README.md の「つなぐ先の準備」。
EOF
exit 1

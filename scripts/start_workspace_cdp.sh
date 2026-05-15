#!/usr/bin/env bash
set -euo pipefail

ROOT="/root/Hermes-Agent"
CHROME="/root/.cache/ms-playwright/chromium-1217/chrome-linux64/chrome"
PROFILE="$ROOT/workspace-agent-browser-profile"
HOST_CDP_PORT="${HOST_CDP_PORT:-19224}"
CONTAINER_PROXY_PORT="${CONTAINER_PROXY_PORT:-19225}"
DOCKER_GATEWAY="${DOCKER_GATEWAY:-172.16.1.1}"
CONTAINER="${HERMES_WORKSPACE_AGENT_CONTAINER:-hermes-workspace-tpas-hermes-agent-1}"
PROXY_SCRIPT="$ROOT/scripts/cdp_proxy.py"

mkdir -p "$PROFILE" "$ROOT/logs"

if ! curl -fsS --max-time 2 "http://127.0.0.1:${HOST_CDP_PORT}/json/version" >/dev/null 2>&1; then
  nohup "$CHROME" \
    --headless=new \
    --no-sandbox \
    --disable-dev-shm-usage \
    --disable-gpu \
    --remote-debugging-address=127.0.0.1 \
    --remote-debugging-port="$HOST_CDP_PORT" \
    --user-data-dir="$PROFILE" \
    about:blank >"$ROOT/logs/workspace-agent-chrome.log" 2>&1 &
  for _ in $(seq 1 40); do
    curl -fsS --max-time 2 "http://127.0.0.1:${HOST_CDP_PORT}/json/version" >/dev/null 2>&1 && break
    sleep 0.25
  done
fi

if ! curl -fsS --max-time 2 "http://${DOCKER_GATEWAY}:${CONTAINER_PROXY_PORT}/json/version" >/dev/null 2>&1; then
  if ! ss -ltn | grep -q ":${CONTAINER_PROXY_PORT} "; then
    nohup python3 "$PROXY_SCRIPT" \
      --listen-host 0.0.0.0 \
      --listen-port "$CONTAINER_PROXY_PORT" \
      --target-host 127.0.0.1 \
      --target-port "$HOST_CDP_PORT" >"$ROOT/logs/workspace-agent-cdp-proxy.log" 2>&1 &
  fi
  for _ in $(seq 1 40); do
    curl -fsS --max-time 2 "http://${DOCKER_GATEWAY}:${CONTAINER_PROXY_PORT}/json/version" >/dev/null 2>&1 && break
    sleep 0.25
  done
fi

WS_URL=$(python3 - <<PY
import json, urllib.request
port = ${HOST_CDP_PORT}
proxy_port = ${CONTAINER_PROXY_PORT}
gateway = "${DOCKER_GATEWAY}"
with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=5) as r:
    ws = json.load(r)["webSocketDebuggerUrl"]
print(ws.replace(f"ws://127.0.0.1:{port}", f"ws://{gateway}:{proxy_port}"))
PY
)

if docker ps --format '{{.Names}}' | grep -qx "$CONTAINER"; then
  docker exec -u hermes "$CONTAINER" /opt/hermes/.venv/bin/hermes config set browser.cdp_url "$WS_URL" >/dev/null
fi

echo "Workspace Browser CDP ready: $WS_URL"

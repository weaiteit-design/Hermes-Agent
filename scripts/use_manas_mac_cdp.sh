#!/usr/bin/env bash
set -euo pipefail

PORT="${MANAS_REVERSE_CDP_PORT:-9223}"
PROXY_PORT="${MANAS_DOCKER_CDP_PROXY_PORT:-9224}"
DOCKER_GATEWAY="${DOCKER_GATEWAY:-172.16.1.1}"
CONTAINER="${HERMES_WORKSPACE_AGENT_CONTAINER:-hermes-workspace-tpas-hermes-agent-1}"
ROOT="/root/Hermes-Agent"
PROXY_SCRIPT="$ROOT/scripts/cdp_proxy.py"
HOST_URL="http://127.0.0.1:${PORT}"

python3 - <<PY
import json, urllib.request, sys
url = "${HOST_URL}/json/version"
try:
    with urllib.request.urlopen(url, timeout=5) as r:
        data = json.load(r)
except Exception as e:
    print(f"CDP not reachable at {url}: {e}", file=sys.stderr)
    sys.exit(1)
print(data.get("Browser", ""))
print(data.get("User-Agent", ""))
if "Macintosh" not in data.get("User-Agent", ""):
    print("ERROR: CDP is reachable but is not a Macintosh Chrome.", file=sys.stderr)
    sys.exit(2)
if not data.get("webSocketDebuggerUrl"):
    print("ERROR: CDP did not return webSocketDebuggerUrl.", file=sys.stderr)
    sys.exit(3)
PY

mkdir -p "$ROOT/logs"
if ! curl -fsS --max-time 2 "http://${DOCKER_GATEWAY}:${PROXY_PORT}/json/version" >/dev/null 2>&1; then
  if ! ss -ltn | grep -q ":${PROXY_PORT} "; then
    nohup python3 "$PROXY_SCRIPT" \
      --listen-host "$DOCKER_GATEWAY" \
      --listen-port "$PROXY_PORT" \
      --target-host 127.0.0.1 \
      --target-port "$PORT" >"$ROOT/logs/manas-mac-cdp-proxy.log" 2>&1 &
  fi
  for _ in $(seq 1 40); do
    curl -fsS --max-time 2 "http://${DOCKER_GATEWAY}:${PROXY_PORT}/json/version" >/dev/null 2>&1 && break
    sleep 0.25
  done
fi

if ! curl -fsS --max-time 2 "http://${DOCKER_GATEWAY}:${PROXY_PORT}/json/version" >/dev/null 2>&1; then
  echo "ERROR: Docker-reachable Mac CDP proxy is not available at http://${DOCKER_GATEWAY}:${PROXY_PORT}" >&2
  exit 4
fi

start_container_loopback_proxy() {
  local c="$1"
  if ! docker ps --format '{{.Names}}' | grep -qx "$c"; then
    return 0
  fi
  docker cp "$PROXY_SCRIPT" "$c":/tmp/cdp_proxy.py >/dev/null
  if ! docker exec "$c" sh -lc "curl -fsS --max-time 2 http://127.0.0.1:${PORT}/json/version >/dev/null 2>&1"; then
    docker exec -d "$c" python3 /tmp/cdp_proxy.py \
      --listen-host 127.0.0.1 \
      --listen-port "$PORT" \
      --target-host "$DOCKER_GATEWAY" \
      --target-port "$PROXY_PORT" >/dev/null
    for _ in $(seq 1 40); do
      docker exec "$c" sh -lc "curl -fsS --max-time 2 http://127.0.0.1:${PORT}/json/version >/dev/null 2>&1" && break
      sleep 0.25
    done
  fi
  docker exec "$c" sh -lc "curl -fsS --max-time 5 http://127.0.0.1:${PORT}/json/version >/tmp/manas_cdp_check.json && python3 - <<'PY'
import json, sys
j=json.load(open('/tmp/manas_cdp_check.json'))
ua=j.get('User-Agent','')
print(j.get('Browser',''))
print(ua)
if 'Macintosh' not in ua:
    sys.exit(2)
PY"
}

start_container_loopback_proxy "$CONTAINER"
start_container_loopback_proxy "hermes-workspace-tpas-hermes-workspace-1"

if docker ps --format '{{.Names}}' | grep -qx "$CONTAINER"; then
  docker exec -u hermes "$CONTAINER" /opt/hermes/.venv/bin/hermes config set browser.cdp_url "$HOST_URL" >/dev/null
  echo "Set Workspace browser.cdp_url to $HOST_URL"
else
  echo "Workspace agent container not found: $CONTAINER" >&2
  exit 5
fi

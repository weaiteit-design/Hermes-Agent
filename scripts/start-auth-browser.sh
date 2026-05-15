#!/usr/bin/env bash
set -euo pipefail
mkdir -p /root/Hermes-Agent/browser-profile /root/Hermes-Agent/browser-downloads /root/Hermes-Agent/browser-screenshots /root/Hermes-Agent/logs

# Stop previous manual auth browser stack, but leave unrelated Hermes services alone.
pkill -f 'Xvfb :99' || true
pkill -f 'x11vnc.*5901' || true
pkill -f 'websockify.*6080' || true
pkill -f 'remote-debugging-port=9222' || true
sleep 1

CHROME="/root/.agent-browser/browsers/chrome-148.0.7778.167/chrome"
if [[ ! -x "$CHROME" ]]; then
  CHROME="$(find /root/.agent-browser/browsers -type f -name chrome | sort | tail -1)"
fi

Xvfb :99 -screen 0 1440x1000x24 > /root/Hermes-Agent/logs/xvfb.log 2>&1 &
sleep 1
export DISPLAY=:99
"$CHROME" \
  --no-sandbox \
  --disable-dev-shm-usage \
  --disable-gpu \
  --no-first-run \
  --no-default-browser-check \
  --user-data-dir=/root/Hermes-Agent/browser-profile \
  --remote-debugging-port=9222 \
  --window-size=1440,1000 \
  https://www.etsy.com/signin \
  https://www.linkedin.com/login \
  https://x.com/i/flow/login \
  > /root/Hermes-Agent/logs/manual-chrome.log 2>&1 &
sleep 2
x11vnc -display :99 -forever -shared -nopw -listen 127.0.0.1 -rfbport 5901 > /root/Hermes-Agent/logs/x11vnc.log 2>&1 &
websockify --web=/usr/share/novnc/ 127.0.0.1:6080 127.0.0.1:5901 > /root/Hermes-Agent/logs/novnc.log 2>&1 &

echo "Auth browser running: DISPLAY=:99, CDP=:9222, noVNC=:6080"

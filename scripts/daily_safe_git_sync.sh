#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-/root/Hermes-Agent}"
cd "$REPO"

# Never auto-stage raw credentials/browser sessions. This script stages only durable workspace outputs.
ALLOW_PATHS=(
  ".gitignore"
  "README.md"
  "docs"
  "reports"
  "social-content"
  "etsy-products"
  "scripts"
)

# Stage allowlisted paths if present. Ignore local CDP/tunnel scripts via .gitignore and explicit excludes.
for p in "${ALLOW_PATHS[@]}"; do
  [ -e "$p" ] || continue
  git add -A -- "$p"
done

# Explicitly unstage files that should never be preserved in GitHub.
git restore --staged -- \
  '.env' '*.env.*' '*.key' '*.pem' '*.token' 'secrets' \
  'browser-profile' 'workspace-agent-browser-profile' 'browser-downloads' 'browser-screenshots' \
  'scripts/*cdp*.sh' 'scripts/*cdp*.plist' 2>/dev/null || true

# Nothing to commit.
if git diff --cached --quiet; then
  echo "No safe workspace changes to sync."
  exit 0
fi

# Secret/sensitive scan on staged textual files. Keep broad, but allow the sync helper itself
# to contain the scanner pattern names.
SCAN_FILES=$(git diff --cached --name-only | grep -v '^scripts/daily_safe_git_sync\.sh$' || true)
if [ -n "$SCAN_FILES" ] && printf '%s\n' "$SCAN_FILES" | xargs -r grep -InE \
  '(^|[^A-Z0-9_])(API_KEY|SECRET|TOKEN|PASSWORD|PRIVATE_KEY|BEARER|client_secret|refresh_token|access_token|BEGIN [A-Z ]*PRIVATE KEY|ssh-rsa|ssh-ed25519|hermescdp@|StrictHostKeyChecking|ExitOnForwardFailure)' \
  2>/dev/null; then
  echo "Blocked: staged files may contain secrets or connection details. Review and commit manually."
  git restore --staged .
  exit 2
fi

# Show concise staged summary.
git diff --cached --stat

DATE_IST="$(TZ=Asia/Kolkata date +%Y-%m-%d)"
git commit -m "chore: daily Hermes workspace sync ${DATE_IST}"

git push origin "$(git branch --show-current)"

LOCAL_HEAD="$(git rev-parse --short HEAD)"
REMOTE_HEAD="$(git ls-remote origin "refs/heads/$(git branch --show-current)" | cut -f1 | cut -c1-7)"
echo "Synced. local=${LOCAL_HEAD} remote=${REMOTE_HEAD}"

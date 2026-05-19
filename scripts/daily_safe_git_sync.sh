#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-/root/Hermes-Agent}"
cd "$REPO"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "BLOCKED: $REPO is not a git repository"
  exit 2
fi

BRANCH="$(git branch --show-current)"
if [[ -z "$BRANCH" ]]; then
  echo "BLOCKED: detached HEAD; cannot safely sync"
  exit 2
fi

# Durable, safe folders only. Do not use git add . in this operator workspace.
ALLOWLIST=(
  reports
  project-intelligence
  social-content
  etsy-products
  scripts/daily_safe_git_sync.sh
  scripts/build_etsy_seller_command_center.py
  scripts/create_etsy_trust_launch_kit.py
)

# Stage only paths that exist.
for path in "${ALLOWLIST[@]}"; do
  [[ -e "$path" ]] && git add -- "$path"
done

# Explicitly unstage sensitive/runtime/local paths if they were picked up accidentally.
git reset -q -- \
  .env '*.env' '*.env.*' '*.key' '*.pem' '*.token' secrets \
  browser-profile workspace-agent-browser-profile browser-downloads browser-screenshots \
  logs data external-repos workspace \
  2>/dev/null || true

if git diff --cached --quiet; then
  echo "NO_CHANGES: no allowlisted durable changes to commit"
  exit 0
fi

# Secret/connection scan on staged content. Keep this list conservative and readable.
SCAN_FILES="$(git diff --cached --name-only --diff-filter=ACM)"
if [[ -n "$SCAN_FILES" ]]; then
  while IFS= read -r f; do
    [[ -f "$f" ]] || continue
    case "$f" in
      scripts/daily_safe_git_sync.sh) continue ;;
      *.png|*.jpg|*.jpeg|*.webp|*.gif|*.pdf|*.zip|*.xlsx|*.pptx|*.docx) continue ;;
    esac
    if grep -InE '(API[_-]?KEY|SECRET|TOKEN|PASSWORD|PRIVATE[ _-]?KEY|BEGIN [A-Z ]*PRIVATE KEY|AUTHORIZATION:|COOKIE=|SESSION=|ssh-ed25519|ssh-rsa)' "$f" >/tmp/daily-sync-secret-hit.txt 2>/dev/null; then
      echo "BLOCKED: staged file appears to contain secret/connection material: $f"
      sed -n '1,5p' /tmp/daily-sync-secret-hit.txt
      git reset -q
      exit 3
    fi
  done <<< "$SCAN_FILES"
fi

DATE="$(date -u +%F)"
git commit -m "chore: daily workspace sync $DATE" >/tmp/daily-sync-commit.txt
COMMIT="$(git rev-parse --short HEAD)"

# Push. Prefer existing git credentials. If unavailable, use GITHUB_TOKEN from environment or ~/.hermes/.env without printing it.
if git push origin "$BRANCH" >/tmp/daily-sync-push.txt 2>/tmp/daily-sync-push.err; then
  :
else
  TOKEN="${GITHUB_TOKEN:-}"
  if [[ -z "$TOKEN" && -f /root/.hermes/.env ]]; then
    TOKEN="$(python3 - <<'PY'
from pathlib import Path
for line in Path('/root/.hermes/.env').read_text(errors='ignore').splitlines():
    if line.startswith('GITHUB_TOKEN='):
        print(line.split('=',1)[1].strip().strip('"').strip("'"))
        break
PY
)"
  fi
  if [[ -z "$TOKEN" ]]; then
    echo "BLOCKED: committed locally as $COMMIT, but push failed and no GitHub token is available."
    sed -n '1,20p' /tmp/daily-sync-push.err
    exit 4
  fi
  REMOTE="$(git remote get-url origin)"
  if [[ "$REMOTE" =~ github.com[:/]([^/]+)/([^/.]+)(\.git)?$ ]]; then
    OWNER="${BASH_REMATCH[1]}"
    REPO="${BASH_REMATCH[2]}"
    AUTH_REMOTE="https://x-access-token:${TOKEN}@github.com/${OWNER}/${REPO}.git"
    git push "$AUTH_REMOTE" "$BRANCH" >/tmp/daily-sync-push.txt 2>/tmp/daily-sync-push.err || {
      echo "BLOCKED: committed locally as $COMMIT, but authenticated push failed."
      sed -n '1,20p' /tmp/daily-sync-push.err | sed -E 's#https://x-access-token:[^@]+@#https://x-access-token:[REDACTED]@#g'
      exit 5
    }
  else
    echo "BLOCKED: committed locally as $COMMIT, but remote is not a recognized GitHub URL."
    exit 6
  fi
fi

REMOTE_HEAD="$(git ls-remote origin "refs/heads/$BRANCH" 2>/dev/null | cut -f1 | cut -c1-7 || true)"
echo "SYNCED: commit $COMMIT pushed on $BRANCH; remote_head=${REMOTE_HEAD:-unknown}"

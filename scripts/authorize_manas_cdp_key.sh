#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 '<ssh-ed25519 public key line>'" >&2
  exit 2
fi
PUB="$1"
USER_NAME="hermescdp"
PORT="${MANAS_REVERSE_CDP_PORT:-9223}"

id "$USER_NAME" >/dev/null 2>&1 || useradd -m -s /usr/sbin/nologin "$USER_NAME"
install -d -m 700 -o "$USER_NAME" -g "$USER_NAME" "/home/$USER_NAME/.ssh"
touch "/home/$USER_NAME/.ssh/authorized_keys"
chown "$USER_NAME:$USER_NAME" "/home/$USER_NAME/.ssh/authorized_keys"
chmod 600 "/home/$USER_NAME/.ssh/authorized_keys"

LINE="restrict,port-forwarding,permitlisten=\"127.0.0.1:${PORT}\" ${PUB}"
# Replace existing key line for same public key body if present, otherwise append.
KEY_BODY=$(printf '%s\n' "$PUB" | awk '{print $2}')
TMP=$(mktemp)
awk -v key="$KEY_BODY" 'index($0,key)==0 {print}' "/home/$USER_NAME/.ssh/authorized_keys" > "$TMP"
printf '%s\n' "$LINE" >> "$TMP"
cat "$TMP" > "/home/$USER_NAME/.ssh/authorized_keys"
rm -f "$TMP"
chown "$USER_NAME:$USER_NAME" "/home/$USER_NAME/.ssh/authorized_keys"
chmod 600 "/home/$USER_NAME/.ssh/authorized_keys"

pkill -u "$USER_NAME" sshd 2>/dev/null || true
ss -ltnp | grep ":${PORT} " || true

echo "Authorized reverse CDP tunnel user '$USER_NAME' for 127.0.0.1:${PORT}."

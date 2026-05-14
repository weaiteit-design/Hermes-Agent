# Hermes Agent — Setup & Configuration

## VPS Details
- **Provider:** Hostinger
- **IP Address:**
- **OS:**
- **CPU / RAM / Storage:**
- **SSH User:**
- **Domain (if any):**

## LLM Provider
- **Provider:** OpenAI (Codex / GPT-5.5)
- **API Key:**

## Platform Integration
- **Channel:** Telegram
- **Bot Token:**
- **Bot Username:**

## Deployment Method
- [ ] Docker (recommended)
- [ ] Bare metal install

## Docker Config
```env
# ~/.hermes/.env — will be populated during setup
```

## Data Volume
```
# Persistent storage mount
-v ~/.hermes:/opt/data
```

## Post-Install Checklist
- [ ] VPS provisioned and SSH access confirmed
- [ ] Docker installed
- [ ] Hermes Agent container running
- [ ] LLM provider configured and tested
- [ ] Platform integrations connected
- [ ] Memory/skills persistence verified
- [ ] Firewall / security hardened
- [ ] Domain + SSL (optional)

## Admin Credentials
> Stored in `.env` (git-ignored) — never commit secrets to the repo.

## Notes
<!--
Dump anything here — credentials, links, ideas, config snippets.
I'll organize it on each pass.
-->

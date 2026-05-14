# Hermes Agent — Setup & Configuration

## VPS Details
- **Provider:** Hostinger
- **IP Address:** 187.127.167.128
- **OS:** Ubuntu 24.04 with Docker and Traefik
- **CPU / RAM / Storage:** 2 vCPU / 8 GB / 100 GB
- **SSH User:** root
- **Hostname:** HermesAgent.vps
- **Location:** India — Mumbai 2
- **Plan:** KVM 2 (expires 2027-05-14, auto-renew on)

## LLM Provider
- **Provider:** OpenAI (Codex / GPT-5.5)
- **API Key:**

## Platform Integration
- **Channel:** Telegram
- **Bot Token:** (in .env)
- **Telegram User ID:** 1295926144
- **Home Channel:** User DM

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

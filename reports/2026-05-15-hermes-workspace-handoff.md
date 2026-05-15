# Hermes Workspace Handoff — 2026-05-15

This note preserves the current Hermes/Telegram setup state before switching to Hermes Workspace.

## Safe working directory

Use this as the working folder:

```text
/root/Hermes-Agent
```

## GitHub preservation

Primary repo:

```text
https://github.com/weaiteit-design/Hermes-Agent.git
```

Known synced commit before this handoff:

```text
fa4fc89
```

That commit includes:

- WiseAI codespace review report: `reports/2026-05-15-wiseai-codespace-review.md`
- Etsy wedding mini milestones product package: `etsy-products/2026-05-15-wedding-mini-milestones-planner/`
- `.gitignore` update to keep local clones/browser profiles/secrets/logs/vendor files out of Git

## Browser / CDP state

Browser automation profile currently used by Hermes/agent-browser:

```text
/root/Hermes-Agent/browser-profile
```

Important:

- Do not delete or reset this folder.
- If browser/CDP login appears lost after switching workspaces, first confirm the new workspace is using this same profile path.
- Open browser tabs and live CDP target IDs are session-specific and may not survive switching, but the browser profile path is the durable piece.

## Auth/config state verified before handoff

Verified present/running before switching:

- Codex CLI auth: present at `~/.codex/auth.json`
- Hermes auth: present at `~/.hermes/auth.json`
- Hermes gateway: running as `hermes-gateway.service`
- Default profile gateway: running
- Specialist profiles exist: `builder`, `creative`, `orchestrator`, `researcher`, `reviewer`

## Scheduled jobs verified before handoff

Cron jobs existed and were enabled:

- `etsy-digital-products-growth-agent`
- `codex-project-context-agent`
- `linkedin-twitter-growth-execution-agent`
- `higgsfield-mcp-watch-agent`
- `Daily X App Ideas Report` — job ID `df970df22133`

## Recommended first verification command/task in Hermes Workspace

After switching to Hermes Workspace, ask:

```text
Verify my Hermes Workspace state:
1. Check /root/Hermes-Agent git status and latest commit.
2. Check Hermes gateway status.
3. Check cron jobs.
4. Check Codex CLI auth.
5. Check browser/CDP profile path /root/Hermes-Agent/browser-profile.
6. Confirm WiseAI report and Etsy product files exist.
```

## Key files to confirm

```text
/root/Hermes-Agent/reports/2026-05-15-wiseai-codespace-review.md
/root/Hermes-Agent/etsy-products/2026-05-15-wedding-mini-milestones-planner/
/root/Hermes-Agent/browser-profile
```

## Best next product task

Continue with:

```text
Fix WiseAI landing page for launch.
```

Rationale:

- Landing page is closer to production than the mobile app.
- Mobile app needs a larger Expo/web-to-native cleanup.
- Landing page fixes should be a faster launch win.

## Safety notes

- Do not commit `.env`, browser profiles, logs, external cloned repos, or local vendor caches.
- Treat any API keys found in WiseAI mobile/landing repos as exposed and rotate before production.
- If using browser automation with marketplace/social accounts, prefer the durable browser profile path above instead of repeatedly logging in.

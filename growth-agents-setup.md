# Growth Agents Setup

Owner: Manas
Updated: 2026-05-14

## Active daily agents

1. Etsy Digital Products Growth Agent
- Job ID: 059f495fc890
- Schedule: 03:30 UTC / 09:00 IST daily
- Output: Telegram summary + files under `/root/Hermes-Agent/etsy-growth/`
- Mode: research + product/listing asset prep. No live Etsy upload until account/browser access is approved.

2. Codex/Projects Context Agent
- Job ID: 4a4760ca3469
- Schedule: 04:00 UTC / 09:30 IST daily
- Output: Telegram summary + `/root/Hermes-Agent/project-intelligence/YYYY-MM-DD-project-map.md`
- Mode: scans available local/session context and suggests next actions. No code edits.

3. LinkedIn/Twitter Growth Draft Agent
- Job ID: 8758b7ce6f4a
- Schedule: 04:30 UTC / 10:00 IST daily
- Output: Telegram summary + `/root/Hermes-Agent/social-growth/YYYY-MM-DD-social-drafts.md`
- Mode: drafts only until social auth/posting approval is ready.

4. Higgsfield MCP Watch Agent
- Job ID: 3a5a7066ab72
- Schedule: 05:00 UTC / 10:30 IST daily
- Output: Telegram health/setup summary
- Mode: checks MCP config. Cannot connect until MCP endpoint/command and auth method are provided.

## What is still needed

### Etsy
- Chrome profile access or explicit approval to use browser session logged into `weaiteit@gmail.com`.
- Etsy shop URL/name.
- Whether Hermes may publish directly or should prepare draft listings for approval.
- Any brand constraints: colors, product categories to avoid, preferred price range.

### Higgsfield MCP
- MCP transport: HTTP URL or stdio command/args.
- Auth method and where token is stored. Do not paste token in chat if avoidable. Prefer adding it to `~/.hermes/.env` or provider config.
- Confirmation that it should bind/use Higgsfield account `manas@sociaaal.com`.

### Codex/projects
- Locations of active repositories or Codex workspaces if outside `/root/Hermes-Agent`.
- Whether Hermes can clone private GitHub repos using available auth.
- Which projects are highest priority.

### LinkedIn/Twitter
- X/Twitter API setup via `xurl` or a browser-based posting approval flow.
- LinkedIn automation method. Safer default: drafts only, user posts manually. Direct posting requires approved API/browser workflow.
- Confirmation of posting cadence and approval policy.

## Brand rules for social

- Voice: natural, humble, founder/operator, learning in public.
- Topics: AI learning, daily AI workflows, new tools, entrepreneurship, building with AI.
- Avoid em dashes.
- Do not lean on big achievements like KBC repeatedly.
- Prefer useful, specific posts over motivational fluff.

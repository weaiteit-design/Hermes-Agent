# Manas Agent Control Center

This is the Telegram-connected multi-agent setup for Manas.

## What is set up

- **Main commander:** Telegram Hermes default profile. This is the chat Manas uses.
- **Shared board:** `manas-os`
- **Dashboard:** Hermes Dashboard on `127.0.0.1:9119` with TUI enabled.
- **Kanban dispatcher:** runs inside the Hermes gateway every 60 seconds.
- **Worker profiles:**
  - `orchestrator` — breaks big requests into cards and coordinates dependencies.
  - `researcher` — market/product/research/web/docs intelligence.
  - `builder` — coding, scripts, repo work, implementation.
  - `reviewer` — checks quality, risks, correctness, and completion.
  - `creative` — ads, concepts, scripts, designs, creative strategy.

## How work should flow from Telegram

Manas talks to the main Telegram agent. The Telegram agent creates or coordinates work on the `manas-os` Kanban board. Worker profiles pick up tasks through the gateway dispatcher.

Example Telegram prompts:

```text
Create a multi-agent task for AiteitAI: researcher should study 10 AI ad agencies, creative should generate concepts, reviewer should produce a final recommendation.
```

```text
Put this on the agent board: builder should create a Wise AI launch checklist file, reviewer should check it, and send me the final summary.
```

## Telegram commands

```text
/kanban list
/kanban show <task_id>
/kanban tail <task_id>
/kanban stats
/kanban dispatch
/agents
```

## Local dashboard access

The dashboard is intentionally bound to localhost because it can expose private config/API-key management. Do **not** expose it publicly with `--insecure` unless you add proper access controls.

From your laptop, use SSH port forwarding:

```bash
ssh -L 9119:127.0.0.1:9119 root@<server-ip>
```

Then open:

```text
http://127.0.0.1:9119
```

## Control commands on the server

```bash
# Start dashboard
/root/Hermes-Agent/scripts/agent-control-center start

# Check status
/root/Hermes-Agent/scripts/agent-control-center status

# Stop dashboard
/root/Hermes-Agent/scripts/agent-control-center stop

# Show board
hermes kanban --board manas-os list

# Show profiles
hermes profile list
```

## Safety rule

Keep Telegram as the command center. Use worker profiles through Kanban for durable/project work. Use quick subagents for short parallel tasks. Do not expose the dashboard publicly unless you explicitly decide to secure it.

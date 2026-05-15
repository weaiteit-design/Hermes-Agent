# Project map: 2026-05-15

Sources inspected: `/root/Hermes-Agent`, core workspace files, Etsy growth outputs, cron config, recent session summaries, and Git status. No code was modified.

## Projects found

### 1. Wise AI
**What it is:** AI micro-lessons and updates platform.

**Current status:** Coding is inferred as mostly complete from `PROJECTS.md`. Current focus is launch readiness: App Store compliance, Play Store compliance, privacy/terms/data safety, store listing assets, release plan, final QA, and launch announcement content.

**Risks/blockers:**
- No local app repo found under `/root/Hermes-Agent`, so actual code, build status, and QA state cannot be verified here.
- Compliance tasks exist but appear not yet converted into a detailed checklist.
- Store listing assets and copy are still listed as launch-prep work.

**Opportunities:**
- Create a launch PM pack: compliance checklist, QA checklist, store copy checklist, release calendar, and daily standup prompts.
- Reuse Hermes daily research to generate AI update cards and micro-lesson ideas.

---

### 2. AiteitAI
**What it is:** AI-powered creative services startup for trailers, static ads, and AI-assisted creative production.

**Current status:** Defined at strategy level. Local notes point to service packaging, offer pages, pitch decks, client workflows, case study structure, and a UGC ad-studio style research workflow as next steps.

**Risks/blockers:**
- Official website/domain is still unconfirmed.
- Offers are not yet packaged into clear tiers, prices, deliverables, timelines, and proof assets.
- No client intake or production workflow templates found as completed artifacts.

**Opportunities:**
- Build a productized offer around “product URL to ad/trailer concepts, hooks, static ad directions, editor checklist.”
- Use the Hermes agent control center to split research, creative, and review work across profiles.

---

### 3. Sociaaal creative workflows
**What it is:** Manas’s generative AI creative director work across app concepts, creative materials, AI-assisted execution, editor coordination, and trend research.

**Current status:** Documented as an active responsibility area. Planned workflows include app concept ideation, TikTok/Instagram research, editor workflow templates, and a reusable AI workflow library.

**Risks/blockers:**
- No completed reusable workflow library found yet.
- Social/trend automation depends on live platform access or approved browser/API flows.
- Work may remain scattered unless templates and handoff formats are standardized.

**Opportunities:**
- Create one shared creative brief template, one editor handoff template, and one trend research digest format.
- Convert recurring creative tasks into Kanban cards for researcher, creative, and reviewer profiles.

---

### 4. Etsy digital products growth
**What it is:** Daily agent for researching Etsy digital-product niches and creating product/listing assets.

**Current status:** Active and producing real packages under `/root/Hermes-Agent/etsy-growth/`.

Recent outputs:
- `2026-05-15`: Printable Pen Pal Letter Writing Kit, with ZIP, A4/US Letter PDFs, prompt cards CSV, tracker CSV, Notion-style dashboard, listing images, Etsy listing draft, research notes, and recommended price.
- `2026-05-14`: AI Study Workflow Pack, with prompt library, revision planner, assignment template, checklist, PDF quick-start guide, CSV, and listing draft.

**Risks/blockers:**
- Etsy publishing is blocked by unauthenticated browser access and a DataDome CAPTCHA/device check.
- Etsy shop URL/name, brand constraints, price range preferences, and direct publish approval policy still need confirmation.
- Product quality may compound quickly, but listings cannot convert until publishing is solved.

**Opportunities:**
- Manually review and upload the strongest product first, then use actual Etsy metrics to steer the agent.
- Create a brand/product guideline file so every daily product uses consistent positioning, visual rules, and pricing.

---

### 5. LinkedIn/Twitter growth draft agent
**What it is:** Scheduled agent for drafting or publishing AI/workflow/founder content in Manas’s voice.

**Current status:** Configured to run daily at 04:30 UTC / 10:00 IST. It is draft-first unless authenticated X/LinkedIn access exists.

**Risks/blockers:**
- X/Twitter API tool `xurl` is not installed/authenticated based on local research notes.
- LinkedIn automation method is not confirmed. Safe default is manual posting from drafts.
- Direct posting needs approved browser/API flow to avoid risky automation.

**Opportunities:**
- Use Etsy product creation, Wise AI launch work, and Hermes workflow learnings as authentic daily content.
- Keep posts specific and useful, not generic motivational content.

---

### 6. Hermes workspace and multi-agent control center
**What it is:** Shared working hub and Telegram-connected multi-agent setup for Manas.

**Current status:** `/root/Hermes-Agent` is the durable workspace. It contains profile, project, task, automation, setup, research, and control center docs. The control center notes describe Telegram as the main commander, a shared `manas-os` board, a local dashboard on `127.0.0.1:9119`, and worker profiles: orchestrator, researcher, builder, reviewer, creative.

**Git/workspace state:** Local remote is configured to `https://github.com/weaiteit-design/Hermes-Agent.git`, but `git status` shows many untracked files, including workspace docs, Etsy outputs, browser profile/logs, vendor code, and Marathi translation outputs.

**Risks/blockers:**
- GitHub authentication and initial push are still listed as active tasks.
- Browser profile and logs are untracked and should not be blindly committed.
- Durable project files exist, but project task ownership and source of truth between repo vs Notion are still undecided.

**Opportunities:**
- Cleanly separate commit-worthy knowledge files from generated assets, logs, browser profiles, and vendor files.
- Use the Kanban dispatcher for durable, multi-step work instead of ad hoc chat-only execution.

---

### 7. Higgsfield MCP watch/setup
**What it is:** Scheduled checker for Higgsfield MCP configuration for creative workflows, intended for `manas@sociaaal.com`.

**Current status:** Configured to run daily at 05:00 UTC / 10:30 IST. Local setup notes say it cannot connect until MCP endpoint/command and auth method are provided.

**Risks/blockers:**
- Missing MCP transport: HTTP URL or stdio command/args.
- Missing auth method/token location.
- OAuth may need manual completion.

**Opportunities:**
- Once connected, route creative video/image workflows into Sociaaal and AiteitAI production systems.

---

### 8. Marathi document translation artifacts
**What it is:** Local translated education/training material artifacts, including a Marathi PDF and XLSX generated from cached English source files.

**Current status:** Outputs found:
- `/root/Hermes-Agent/4. EW_E&W_B1T1_RM_A2_Marathi.pdf`
- `/root/Hermes-Agent/8. EW_E&W_B1T1_Assmt_Marathi.xlsx`
- `/root/Hermes-Agent/translate_documents_marathi.py`

**Risks/blockers:**
- No matching session summary found, so project owner, target quality bar, and delivery status are unclear.
- Generated previews and caches are present locally, but no final project note explains whether review is complete.

**Opportunities:**
- Add a short project note with source, output files, review status, and remaining QA needs.

---

## Cross-project risks and blockers

1. **Authentication bottlenecks:** Etsy, X/Twitter, LinkedIn, GitHub, and Higgsfield all need either approved browser sessions, API/CLI auth, or manual user action before full automation can publish or sync.
2. **Source-of-truth ambiguity:** Tasks are in markdown today, but Notion vs repo vs both is still undecided.
3. **Workspace hygiene:** Many useful files are mixed with logs, browser data, generated assets, and vendor code. This increases risk of accidental commits or stale context.
4. **Priority ambiguity:** Wise AI, AiteitAI, Sociaaal, Etsy, social growth, and automation all have momentum. The top 1 to 2 outcomes for this week are not yet explicitly locked.

## 3 highest-leverage next actions

1. **Create a “launch and publishing access” checklist for Manas to complete once:** Etsy shop/auth, X/LinkedIn posting method, GitHub auth, Higgsfield MCP auth, and what Hermes is allowed to publish directly vs draft for approval.

2. **Package Wise AI launch readiness into one actionable folder:** App Store checklist, Play Store checklist, privacy/data safety checklist, QA checklist, store listing copy, and launch announcement plan. This is the clearest path to shipping a nearly complete product.

3. **Clean the Hermes workspace before pushing:** Add or update `.gitignore`, separate generated/browser/log/vendor artifacts from durable docs, then commit only the knowledge base, task/project files, scripts that should be retained, and selected product outputs.

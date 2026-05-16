# Project map: 2026-05-16

Sources inspected: `/root/Hermes-Agent`, project/task/control docs, recent reports, generated Etsy/social/cron outputs, recent session summaries, cron config, external repo status, and Git status. No code was modified.

## Projects found

### 1. Wise AI
**What it is:** AI micro-lessons and updates platform, currently split across a mobile app repo and a landing page repo.

**Current status:** Launch focus is now clearer. The landing page is the fastest ship path: TypeScript and production build passed in the prior review when dummy Supabase env vars were supplied, but lint and dependency/security work remain. The mobile app is not launch-ready because it is still in a partial web-to-Expo migration state.

**Local evidence:** `PROJECTS.md`, `TASKS.md`, and `reports/2026-05-15-wiseai-codespace-review.md`. External repo working trees for `Delta-` and `wiseai-landing` were clean when checked today.

**Risks/blockers:**
- Mobile app still has web/Vite leftovers and React web primitives mixed into Expo/React Native code.
- Landing page still needs lint fixes, dependency/security updates, safer Supabase env handling, security headers, SEO files, and waitlist hardening.
- A tracked `.env` and API-like values were previously found in the mobile repo. Treat those secrets as exposed before production.
- Store compliance and launch checklist work is still listed, but landing page launch should probably come first.

**Opportunities:**
- Ship the landing page/waitlist as a fast public milestone before tackling the deeper mobile refactor.
- Convert the WiseAI review into a small execution checklist with owner, status, and verification command per item.

---

### 2. AiteitAI
**What it is:** AI-powered creative services startup for trailers, static ads, and AI-assisted creative production.

**Current status:** Still strategy-level in local files. Tasks point to confirming the official website/domain, packaging services, creating offer pages/pitch decks, intake forms, production workflow, and case study structure.

**Risks/blockers:**
- Official website/domain is still unconfirmed in `TASKS.md`.
- Offers are not yet packaged into clear tiers, timelines, prices, deliverables, and proof assets.
- No completed intake/workflow templates found locally.

**Opportunities:**
- Build one productized offer around “product URL to ad/trailer concepts, hook bank, static ad directions, and editor handoff.”
- Reuse the Sociaaal creative workflow and Higgsfield MCP setup once available.

---

### 3. Sociaaal creative workflows
**What it is:** Manas’s generative AI creative director work across app concepts, creative materials, editor coordination, AI-assisted production, and trend research.

**Current status:** Active responsibility area, but local artifacts are still mostly planning docs. The control center defines worker profiles that could support research, creative generation, build tasks, and review.

**Risks/blockers:**
- Reusable app concept, creative brief, editor handoff, and trend research templates are still listed as tasks.
- TikTok/Instagram research automation depends on authenticated/safe platform access.
- Without a durable workflow library, learnings may stay scattered in chats and one-off outputs.

**Opportunities:**
- Create a single Sociaaal creative operating kit: app concept template, trend digest format, editor brief, and reviewer checklist.
- Use Manas’s `manas_builds` content loop to turn real workflow builds into audience growth.

---

### 4. Etsy digital products / HeirloomPlanners
**What it is:** Daily digital-product creation engine for the Etsy shop HeirloomPlanners.

**Current status:** Very active. A new upload-ready product was created today under `/root/Hermes-Agent/etsy-products/2026-05-16-mid-year-reset-planner/`:
- ZIP package: `Mid_Year_Reset_Planner_Bundle.zip`
- Customer files: printable PDF, PDF-ready HTML, Markdown workbook, CSV sheets, Notion instructions, reflection prompts, mockups
- Listing draft with SEO title, tags, price suggestion, description, FAQ
- Marketing and competitor notes

Prior products remain available from May 14 and May 15, including AI Study Workflow Pack, Pen Pal Letter Writing Kit, Digital Product Seller Launch Planner, and Wedding Mini Milestones Planner.

**Risks/blockers:**
- Etsy publishing remains the biggest bottleneck. Product packages exist locally, but manual upload/review is still needed unless a reliable authenticated Etsy flow is available.
- The 2026-05-16 product folder is currently untracked in Git, which is fine for now but should be intentionally preserved or ignored depending on repo policy.
- Quality/revenue feedback loop is missing until at least one listing is published and metrics are checked.

**Opportunities:**
- Manually upload the strongest 1 to 3 products first, starting with the most polished seasonal/timely bundle.
- Add one brand guideline file for HeirloomPlanners so daily products keep consistent pricing, style, licensing, and listing image rules.

---

### 5. LinkedIn / X growth content
**What it is:** Daily content engine for Manas around AI workflows, building in public, Wise AI, AiteitAI, creative AI, and digital products.

**Current status:** A content pack exists for 2026-05-15 under `/root/Hermes-Agent/social-content/2026-05-15/`. It includes LinkedIn post, X thread, alternate short posts, engagement replies, and source notes. The strongest angle was “the model is the engine, the workflow is the vehicle.” X auth appears to have been completed after drafting, but LinkedIn direct publishing is still not available locally.

**Risks/blockers:**
- LinkedIn still needs a reliable authenticated publishing route, so safe default is copy-paste.
- Direct X posting must stay low-risk and source-grounded.
- Content should be tied to real work to avoid generic AI commentary.

**Opportunities:**
- Use the daily Etsy product, WiseAI launch fixes, and Hermes agent learnings as authentic build-in-public material.
- Convert each daily project output into one LinkedIn post, one X thread, and three replies.

---

### 6. Daily X app ideas report
**What it is:** Scheduled daily research agent that searches X for fresh app idea signals using focused one-keyword-at-a-time queries.

**Current status:** Updated after the Mac CDP work: this job should now use authenticated browser/CDP access to X.com, not the X API or `xurl`. The cron job `df970df22133` has been updated to load only the `daily-x-app-ideas-research` skill, remove `xurl`, and run with browser/terminal/file/skills toolsets from `/root/Hermes-Agent`.

**Risks/blockers:**
- The Mac Chrome reverse tunnel must be running for `http://127.0.0.1:9223/json/version` to show a `Macintosh` user agent.
- If X shows logged-out/login-wall state in the Chrome-Hermes profile, the job must report the browser/CDP blocker instead of falling back to the API.
- Without fresh visible X sources, the report cannot meet its quality bar.

**Opportunities:**
- Use the logged-in Mac Chrome CDP session for focused X searches.
- Keep one-keyword-at-a-time searches and avoid broad OR queries.
- Do not depend on X API credits for this report anymore.

---

### 7. Hermes workspace and multi-agent control center
**What it is:** Durable project workspace and Telegram-connected multi-agent control center for Manas.

**Current status:** `/root/Hermes-Agent` is the working hub. Control docs define Telegram as command center, shared board `manas-os`, local dashboard at `127.0.0.1:9119`, Kanban dispatcher, and worker profiles: orchestrator, researcher, builder, reviewer, creative. Cron jobs are enabled for Etsy products, project context, LinkedIn/X growth, Higgsfield MCP watch, and Daily X App Ideas.

**Git/workspace state:** Today `git status --short` showed only the new Etsy product folder as untracked. External WiseAI repos checked today had clean working trees.

**Risks/blockers:**
- Generated outputs, browser profiles, logs, external repos, and durable knowledge files need continued separation before commits.
- Project/task source of truth between markdown, Kanban, and any external PM system is still not fully decided.
- Dashboard should remain localhost-only unless secured.

**Opportunities:**
- Keep committing only durable docs, selected scripts, and curated product outputs while excluding browser/log/vendor files.
- Use Kanban for multi-step project work instead of chat-only execution.

---

### 8. Higgsfield MCP watch/setup
**What it is:** Scheduled checker for Higgsfield MCP configuration for Sociaaal/AiteitAI creative workflows, intended for account `manas@sociaaal.com`.

**Current status:** Still appears configured as a watch job, not as a usable connected toolchain. Local setup notes from prior map said it needs endpoint/command and auth method before tools can be discovered.

**Risks/blockers:**
- Missing MCP transport: HTTP URL or stdio command/args.
- Missing auth method/token location.
- OAuth may need manual user completion.

**Opportunities:**
- Once connected, route creative video/image workflow support into AiteitAI and Sociaaal production systems.

---

### 9. B2T1 Navigating the Digital Workspace
**What it is:** ITI/NCVET learner content package for “Navigating the Digital Workspace,” aimed at Mechanic Diesel and Mechanic Motor Vehicle learners.

**Current status:** A substantial final/template-based package exists under `/root/Hermes-Agent/workspace/B2T1_Navigating_Digital_Workspace/`. Generated artifacts include template-filled PPTs, DOCX reading materials, formatted PDFs, QA preview images, and production scripts. The latest production note says video generation is paused and priority is nailing reading material and PPT formatting first.

**Risks/blockers:**
- Video output is explicitly paused.
- Needs final human QA against template fidelity, simple-language rules, and no brand/product names in learner content.
- Generated assets and scripts need a clear delivery note if this is client-facing work.

**Opportunities:**
- Add a short delivery checklist: final files, QA status, known limitations, and whether video is in or out of scope.
- Preserve the production rules as a reusable skill/template for future ITI/NCVET modules.

---

### 10. Marathi translation artifacts
**What it is:** Local translated education/training materials and scripts.

**Current status:** Previously found outputs include Marathi PDF/XLSX artifacts and a translation script. No fresh project note or session summary today clarified owner, review status, or delivery state.

**Risks/blockers:**
- Review status and delivery status remain unclear.
- Generated previews and caches exist locally without a concise project-level README.

**Opportunities:**
- Add a small project note listing source files, output files, QA status, and remaining language review needs.

## Cross-project risks and blockers

1. **Publishing/auth bottlenecks:** Etsy upload, LinkedIn publishing, X search credits/browser access, GitHub sync, and Higgsfield MCP setup are the recurring blockers.
2. **Launch sequencing risk:** WiseAI mobile app is a bigger refactor, while the landing page looks closer. Treating both as one “launch” could slow down the faster win.
3. **Feedback loop gap:** Etsy products and social content are being produced, but monetization/audience feedback is blocked until publishing and metrics are flowing.
4. **Source-of-truth drift:** Markdown docs, cron outputs, sessions, generated folders, external repos, and Kanban can diverge unless next actions are centralized.
5. **Workspace hygiene:** Current Git state is cleaner than yesterday, but new generated product folders still need intentional commit/ignore decisions.

## 3 highest-leverage next actions

1. **Ship the WiseAI landing page first:** Fix landing page lint/security/env/headers/SEO/waitlist issues, then deploy or prepare deploy instructions. This is the clearest near-term public launch win.

2. **Unblock publishing loops:** Manually upload one Etsy product, restore X search capability with credits or logged-in browser access, and define LinkedIn copy-paste vs direct-post workflow. This turns daily agent output into measurable external results.

3. **Create one operating checklist folder:** Add concise checklists for WiseAI launch, HeirloomPlanners publishing, social content publishing, AiteitAI offer packaging, and auth/setup blockers. Keep it as the single weekly control surface for Manas and the agents.

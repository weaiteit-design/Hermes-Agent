# Project map: 2026-05-18

Sources inspected: `/root/Hermes-Agent`, recent project maps, local project/task/control docs, recent cron outputs, recent reports, product folders, session history, and Git working-tree status for the workspace plus WiseAI external repos. No code was modified.

## Projects found

### 1. HeirloomPlanners / Etsy digital products

**What it is:** Manas's A-to-Z Etsy digital-product growth engine. It creates niche-tested digital downloads, listing copy, listing images, ZIPs, trust assets, and operator reports for the HeirloomPlanners shop.

**Current status:** Most active project. A new product was built today:

- Product: Etsy Seller Profit & Listing Command Center
- Path: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/`
- Includes: PDF, HTML workbook, Notion-copy workspace, prompt pack, 7 CSV trackers, listing copy, marketing copy, competitor notes, 3 listing images, banner SVG, trust copy, and verified customer ZIP.
- QA: ZIP integrity OK, 12 customer-facing files, PDF exists, 7 CSVs, 3 listing images, SVG fallback.
- Draft/live status: no Etsy draft and no live listing created because CDP/browser upload verification was unavailable.

The tracker now records three stronger ready packages: 2026-05-16 Wedding Mini-Milestones Kit, 2026-05-17 ADHD Student Deadline Rescue Kit, and 2026-05-18 Etsy Seller Profit & Listing Command Center. Earlier packages also exist but are lower priority or partially superseded. Last reliable shop baseline remains: 1 active listing, 0 known sales/reviews, shop trust setup 2/5 complete, missing banner, shop story, and seller photo unless Manas changed these manually.

**Risks/blockers:**

- Publishing is the bottleneck. Products are local-only until manually uploaded or CDP/file upload automation is reliable.
- Browser/CDP is down for Etsy and X workflows. The Mac Chrome tunnel on port 9223 is the recurring blocker.
- Shop trust is incomplete, which hurts conversion with 0 reviews.
- Catalog is testing across wedding, student, and small-business niches. This is fine for discovery, but Etsy sections and brand copy need to make it coherent.
- Generated files and reports are accumulating untracked in Git and need intentional preservation without committing browser profiles, logs, secrets, or caches.

**Opportunity:** Stop building more inventory briefly. Publish the three strongest packages, upload trust assets, add a seller/brand image, then measure views/favorites/orders by niche.

---

### 2. Wise AI

**What it is:** AI micro-lessons and updates platform, split across a mobile app repo and a landing page repo.

**Current status:** Landing page remains the fastest public launch path. The prior codespace review found TypeScript and production build passing when dummy Supabase env vars were supplied, but lint, dependency/security updates, safer env handling, headers, SEO files, and waitlist hardening remain. The mobile app repo is still not launch-ready because it is in a partial web-to-Expo migration state with Vite/web leftovers and React web patterns mixed into Expo/React Native.

Local repos checked today:

- Mobile app: `/root/Hermes-Agent/external-repos/Delta-`, branch `main`, clean working tree.
- Landing page: `/root/Hermes-Agent/external-repos/wiseai-landing`, branch `landing-page`, clean working tree.

Wurtle mascot assets and a patch exist locally, including Lottie animations and integration work. The prior critique remains: usable as placeholder assets, but brand clarity may not yet read strongly as a turtle.

**Risks/blockers:**

- Mobile app still needs a focused Expo refactor before store submission.
- A tracked `.env` and API-like values were previously found in the mobile repo. Treat as exposed before production and rotate relevant keys.
- Landing page still needs lint/security/hardening work before launch.
- Wurtle polish can distract from shipping the waitlist if handled too early.

**Opportunity:** Ship the landing page/waitlist first, then use real user interest to justify deeper mobile and mascot work.

---

### 3. AI business opportunity radar and app-idea research

**What it is:** Scheduled research for underexplored AI-executable opportunities and X app idea signals, evaluated against Manas's stack: Hermes, Codex, Claude, browser automation, creative tools, Wise AI, AiteitAI, Sociaaal, and Etsy.

**Current status:** Yesterday's radar picked a persistent memory/run-ledger for coding agents as the best opportunity. The suggested MVP: auto-summarize Hermes/Codex/Claude runs into repo-local decision memory and inject the top memories into future sessions. Today's X app ideas job was blocked because both CDP endpoints were down, and the workflow correctly did not fall back to X API or xurl.

**Risks/blockers:**

- X research quality depends on a working logged-in Mac Chrome/CDP tunnel.
- Research reports are producing good signals, but only one idea should be converted into an MVP at a time.
- The agent-memory/run-ledger idea directly improves this workspace, but it needs implementation scope discipline to avoid becoming a full memory platform.

**Opportunity:** Build the smallest run-ledger dogfood version inside `/root/Hermes-Agent`: append run summaries, decisions, failures, reusable commands, and next actions to a local memory file.

---

### 4. AiteitAI

**What it is:** AI-powered creative services startup for trailers, static ads, AI UGC, and AI-assisted creative production.

**Current status:** Still mostly strategy-level in local docs, but the opportunity radar repeatedly points to a strong near-term wedge: a 48-hour AI UGC/product-video sprint for small brands. This overlaps with Higgsfield-style workflows, approval pages, product research, hook generation, shot lists, captions, and client deliverables.

**Risks/blockers:**

- Official website/domain still needs confirmation.
- Offer packaging, pricing, intake flow, proof assets, and case-study format are not formalized.
- Higgsfield MCP/tooling is still not confirmed as locally usable.

**Opportunity:** Package one narrow offer: “3 AI UGC ad concepts in 48 hours,” with a simple intake form, sample storyboard, prompts, and approval workflow.

---

### 5. Sociaaal creative workflows

**What it is:** Manas's generative AI creative director work for app concepts, creative materials, editor coordination, trend research, and AI-assisted production workflows.

**Current status:** Active responsibility area in `PROJECTS.md` and `TASKS.md`. Local artifacts are still mainly planning docs and daily content/research outputs. The multi-agent control center defines researcher, builder, reviewer, and creative workers that could support this work.

**Risks/blockers:**

- Reusable creative briefs, editor handoff templates, trend-research workflows, and app concept templates are still open tasks.
- TikTok/Instagram/X research depends on stable authenticated browser access.
- Workflow knowledge can remain scattered unless converted into templates.

**Opportunity:** Turn AiteitAI's AI UGC sprint into Sociaaal's first reusable creative operating kit.

---

### 6. LinkedIn / X growth content

**What it is:** Content engine for Manas around AI workflows, building in public, Wise AI, AiteitAI, creative AI, digital products, and Hermes agents.

**Current status:** A new content pack exists under `/root/Hermes-Agent/social-content/2026-05-17/`, including LinkedIn post, X thread, short posts, engagement prompts, and source notes. The LinkedIn draft focuses on AI learning loops and can be tied back to Wise AI. There is also fresh content material from the Etsy product backlog, the agent-memory radar, and the CDP/browser reliability issue.

**Risks/blockers:**

- LinkedIn still appears safest as copy-paste/manual publishing.
- X posting/research depends on CDP and logged-in browser state.
- Content should stay attached to real work instead of generic AI commentary.

**Opportunity:** Use today's concrete work as posts: “I built a daily Etsy product factory but publishing is the bottleneck,” and “the next AI tool I need is a run ledger for agents.”

---

### 7. Hermes workspace and multi-agent control center

**What it is:** Durable local hub for Manas's projects, reports, automations, agents, product outputs, and Telegram-connected workflows.

**Current status:** `/root/Hermes-Agent` remains the main workspace. The control center defines Telegram as command center, shared board `manas-os`, dashboard on localhost, Kanban dispatcher, and worker profiles. Git status shows many valuable untracked generated outputs plus a modified HeirloomPlanners tracker.

Workspace Git status highlights today:

- Modified: `reports/heirloomplanners-growth-tracker.md`
- Untracked: 2026-05-17 and 2026-05-18 Etsy product folders, 2026-05-16 upload images, 2026-05-17 project map, recent reports, `scripts/build_etsy_seller_command_center.py`, and `social-content/2026-05-17/`
- WiseAI external repos are clean.

**Risks/blockers:**

- Valuable generated assets could remain only local unless intentionally committed or backed up.
- Browser profiles, logs, `.env`, caches, and external repo internals must stay out of commits.
- Dashboard should remain localhost-only unless secured.
- Cron outputs, Markdown reports, session memory, and Kanban can drift without one source-of-truth routine.

**Opportunity:** Create a preservation checklist: commit durable reports/products/scripts, ignore runtime/browser/cache files, and keep daily project maps as the cross-project index.

---

### 8. Higgsfield MCP watch/setup

**What it is:** Setup/watch item for connecting Higgsfield MCP or similar video tooling to Manas's creative workflows.

**Current status:** Still appears as a blocker/watch item, not a confirmed usable local toolchain. Its leverage is increasing because the AiteitAI AI UGC sprint idea depends on reliable creative-video execution.

**Risks/blockers:**

- Missing or unconfirmed transport, endpoint, command, and auth/token flow.
- Manual OAuth/account completion may be needed.
- Without a connected toolchain, AiteitAI remains a strategy/offering exercise more than a production workflow.

**Opportunity:** Confirm setup once, then template it into the AiteitAI/Sociaaal UGC sprint workflow.

---

### 9. B2T1 Navigating the Digital Workspace

**What it is:** ITI/NCVET learner content package for “Navigating the Digital Workspace,” aimed at Mechanic Diesel and Mechanic Motor Vehicle learners.

**Current status:** Substantial generated package remains under `/root/Hermes-Agent/workspace/B2T1_Navigating_Digital_Workspace/`, with source extracts, generated package ZIP, reading/PPT/DOCX/PDF assets, preview artifacts, and production scripts. No fresh changes were found today.

**Risks/blockers:**

- Video generation remains paused per earlier notes.
- Human QA is still needed for template fidelity, simple language, and no product/brand names in learner content.
- Delivery status is unclear.

**Opportunity:** Add a short delivery checklist and package index when this work becomes active again.

---

### 10. Marathi translation artifacts

**What it is:** Local Marathi translation outputs and scripts, including PDF/XLSX artifacts and preview folders.

**Current status:** Files exist in the workspace root and preview folders, but there was no fresh session or file today clarifying ownership, QA state, or delivery status.

**Risks/blockers:**

- QA and delivery state unclear.
- Project ownership and source/output mapping are unclear.
- Needs a small README or index if still active.

**Opportunity:** Create an inventory of source files, translated outputs, reviewer status, and delivery status when this project resumes.

## Cross-project risks and blockers

1. **Browser/CDP dependency is the recurring operational blocker:** Etsy publishing, X research, dashboard inspection, and authenticated social workflows all suffer when the Mac Chrome tunnel is down.
2. **Creation is outpacing publishing:** Etsy products, research ideas, and content drafts are being generated faster than they are shipped and measured.
3. **Source-of-truth drift:** Reports, cron outputs, Git status, Kanban, sessions, and product folders need daily/weekly reconciliation.
4. **Launch sequencing risk:** WiseAI landing page is the nearest software launch, but mobile, mascot, and store work can distract from the waitlist path.
5. **Workspace hygiene:** Preserve durable work while avoiding secrets/browser profiles/logs/cache files in Git.

## 3 highest-leverage next actions

1. **Fix the Mac Chrome CDP tunnel and use it to unblock Etsy/X.** Restart the Mac remote-debugging Chrome plus SSH tunnel so `127.0.0.1:9223` works again. This unlocks Etsy inspection/uploads, X research, and browser-based verification.

2. **Publish the HeirloomPlanners backlog before creating more products.** Manually or safely via verified browser automation, upload the Etsy Seller Command Center, Wedding Mini-Milestones Kit, and ADHD Student Deadline Rescue Kit. Also upload banner/story assets and add a seller/brand image.

3. **Ship one dogfood MVP from the opportunity radar: agent run ledger.** Create a minimal local memory/run-ledger for Hermes/Codex runs that records decisions, failures, reusable commands, and next actions. This improves Manas's own agent workflow and creates a strong `manas_builds` story.

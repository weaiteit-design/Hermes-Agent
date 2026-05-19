# Project map: 2026-05-19

Sources inspected: `/root/Hermes-Agent`, recent project maps, `PROJECTS.md`, `TASKS.md`, current Git status, recent reports, HeirloomPlanners tracker/operator brief, Etsy product folders, social-content outputs, Wise AI external repos, B2T1 production notes, and recent session history. No code was modified.

## Projects found

### 1. HeirloomPlanners / Etsy digital products

**What it is:** Manas's A-to-Z Etsy digital-product growth engine. It creates niche-tested digital downloads, listing copy, images, ZIPs, shop trust assets, and operator reports for the HeirloomPlanners shop.

**Current status:** Most active project. The work has shifted correctly from making more products to fixing shop trust and publishing bottlenecks. A new shop trust and launch kit was built today:

- Path: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/`
- ZIP: `heirloomplanners-shop-trust-launch-kit.zip`
- Includes: exact-size Etsy banner PNG/SVG, shop icon PNG/SVG, OpenAI banner concept, shop announcement/about/FAQ, sections and SEO architecture, upload SOP, marketing launch copy, and `ready_listing_upload_queue.csv`.
- QA: ZIP integrity OK, banner 3360x840, icon 500x500, policy checks passed for digital-download language, no income guarantees, no trademark/copyright visual assets, no review manipulation, and no false Etsy affiliation.

Ready local product backlog, in recommended upload order:

1. Etsy Seller Profit & Listing Command Center, $14.99, highest buyer-intent bundle.
2. Wedding Mini-Milestones Planner Kit, $14.99, wedding-season aligned.
3. ADHD Student Deadline Rescue Kit, $12.99, keep non-medical positioning.

Prior known shop baseline still stands unless Manas changed it manually: 1 active listing, 0 known sales/reviews, shop trust setup 2/5 complete, missing banner, story, and seller photo. No Etsy draft/live changes were claimed because browser/CDP automation timed out.

**Risks/blockers:**

- Publishing remains the core bottleneck. Assets are local and verified, but not verified in Etsy drafts/live listings.
- Etsy browser automation is unreliable. The dashboard/editor timed out during the latest run.
- Trust setup is incomplete, which is especially damaging with no reviews.
- Creation is still ahead of distribution and measurement.
- Generated product folders, reports, scripts, and social-content folders are untracked and need intentional preservation.

**Opportunity:** Spend one manual 30-minute block uploading trust assets and saving/publishing the first product draft. This is higher leverage than producing another SKU.

---

### 2. Wise AI

**What it is:** AI micro-lessons and updates platform. Local work is split between a mobile app repo and a landing page repo.

**Current status:** Landing page is still the fastest public launch path. Local repos inspected:

- Mobile app: `/root/Hermes-Agent/external-repos/Delta-`, branch `main`, clean working tree.
- Landing page: `/root/Hermes-Agent/external-repos/wiseai-landing`, branch `landing-page`, clean working tree.

The landing page is a Next.js app with Supabase dependency and basic scripts (`dev`, `build`, `start`, `lint`). The mobile repo is Expo-based but still carries Vite scripts and web-era dependencies, matching the previous assessment that it is in a partial web-to-Expo migration state.

**Risks/blockers:**

- Mobile app is not launch-ready until the Expo migration is cleaned up.
- Previously noted tracked `.env` or API-like values in the mobile repo should be treated as exposed before production.
- Landing page still needs launch hardening: env handling, waitlist reliability, SEO, headers, lint/security checks, and deployment readiness.
- Mascot/Wurtle polish can distract from the simpler waitlist launch.

**Opportunity:** Ship the landing page/waitlist first, then use signup signal to guide mobile, content, and mascot priorities.

---

### 3. AiteitAI

**What it is:** AI-powered creative services startup around trailers, static ads, AI UGC, and AI-assisted creative production.

**Current status:** Still mostly strategy-level in local docs, but the latest opportunity radar picked a strong near-term wedge: a brand-memory layer for AI video/UGC teams. This fits AiteitAI because it can be packaged as a service immediately while also becoming a reusable internal workflow.

**Risks/blockers:**

- Official website/domain still needs confirmation.
- Core services, packages, intake flow, proof assets, and case-study structure are not formalized.
- Higgsfield or equivalent AI video tooling is not confirmed as a reliable local production path.
- Without a narrow offer, AiteitAI can stay too broad.

**Opportunity:** Package a 48-hour offer: “AI UGC sprint with persistent brand memory.” Deliver brand-memory.md, approved/rejected examples, 10 prompts/storyboards, and an approval/revision log.

---

### 4. Sociaaal creative workflows

**What it is:** Manas's generative AI creative director work for app concepts, creative materials, editor coordination, trend research, and AI-assisted production workflows.

**Current status:** Active responsibility area in `PROJECTS.md` and `TASKS.md`. Local artifacts are mainly planning docs and daily content/research outputs. The AiteitAI brand-memory/UGC sprint can become Sociaaal's first concrete reusable operating kit.

**Risks/blockers:**

- Editor handoff templates, creative briefs, app concept templates, and trend research workflows remain open.
- TikTok/Instagram/X research depends on reliable authenticated browser access.
- Creative knowledge remains scattered unless converted into templates.

**Opportunity:** Turn one AiteitAI sprint into a repeatable Sociaaal workflow: intake, brand memory, hooks, storyboard, prompt pack, editor handoff, approval log.

---

### 5. AI business opportunity radar and app-idea research

**What it is:** Scheduled research for AI-executable business opportunities and app ideas, using Hermes, browser automation, Codex/Claude, X/Product Hunt/HN/YouTube/Indie Hackers/search, and Manas's current projects.

**Current status:** The 2026-05-18 radar selected “Brand-memory layer for AI video / UGC creative teams” as the best pick. Previous radar also highlighted an agent-memory/run-ledger for coding agents. Both are highly aligned with Manas's real workflows.

**Risks/blockers:**

- X research/posting is fragile: OAuth works for `manas_builds`, but API credits were depleted in the latest social-content run, and browser/CDP access is inconsistent.
- Research is producing more ideas than can be shipped.
- The best ideas should be dogfooded in the existing workspace before building a full SaaS.

**Opportunity:** Pick one dogfood MVP now: either BrandMemory for AI UGC under AiteitAI/Sociaaal, or a local Hermes run ledger. Do not start both as software products at once.

---

### 6. LinkedIn / X growth content

**What it is:** Content engine for Manas around AI workflows, building in public, Wise AI, AiteitAI, creative AI, digital products, and Hermes agents.

**Current status:** Fresh 2026-05-18 content pack exists under `/root/Hermes-Agent/social-content/2026-05-18/`. Best LinkedIn draft angle: AI as a first-draft operations partner that creates reviewable artifacts. X OAuth is configured for `manas_builds`, but API search/posting was blocked by depleted credits. LinkedIn remains manual copy-paste.

**Risks/blockers:**

- Prepared content is not automatically posted.
- X API credits and browser reliability are operational blockers.
- Content should stay tied to real work instead of generic AI commentary.

**Opportunity:** Publish the 2026-05-18 LinkedIn post manually, then follow with a concrete build-in-public post about the HeirloomPlanners trust kit or BrandMemory for AI UGC.

---

### 7. Hermes workspace and multi-agent control center

**What it is:** Durable local hub for Manas's projects, reports, automations, product outputs, browser workflows, Telegram-connected workflows, and daily project intelligence.

**Current status:** `/root/Hermes-Agent` remains the main workspace. Current Git status shows valuable generated work accumulating:

- Modified: `reports/heirloomplanners-a-to-z-operator-brief.md`, `reports/heirloomplanners-growth-tracker.md`.
- Untracked: 2026-05-17/18/19 Etsy assets, project maps, opportunity radars, HeirloomPlanners weekly review, seller command center/trust kit scripts, and social-content folders.
- External Wise AI repos are clean.

**Risks/blockers:**

- Durable assets may remain local-only unless committed or backed up.
- Browser profiles, caches, logs, `.env`, and external repo internals must not be accidentally committed.
- Daily reports, task docs, Git, sessions, and Kanban can drift without a preservation routine.

**Opportunity:** Add/update `.gitignore`, then commit only durable reports, product packages, scripts, and project maps. Keep runtime/browser/cache/secrets out.

---

### 8. Higgsfield MCP / AI video tooling watch

**What it is:** Setup/watch item for connecting Higgsfield MCP or comparable video-generation tooling to Manas's creative workflows.

**Current status:** Still not confirmed as a reliable local toolchain. Its importance increased because the best current AiteitAI opportunity depends on repeatable AI UGC/video production.

**Risks/blockers:**

- Missing confirmed transport, endpoint, command, auth, and account/OAuth flow.
- Without a working toolchain, AiteitAI can package strategy and prompts but not reliably produce final video outputs from this environment.

**Opportunity:** Confirm the video-tool path once, then template it into the BrandMemory/UGC sprint.

---

### 9. B2T1 Navigating the Digital Workspace

**What it is:** ITI/NCVET learner content package for “Navigating the Digital Workspace,” aimed at Mechanic Diesel and Mechanic Motor Vehicle learners.

**Current status:** Substantial local package remains under `/root/Hermes-Agent/workspace/B2T1_Navigating_Digital_Workspace/`, with English and Marathi scripts, summaries, assignments, reading materials, PPTX/DOCX/PDF-style outputs, and production notes. No fresh changes found today.

**Risks/blockers:**

- Shared template folder requires sign-in from this environment.
- ElevenLabs and Sarvam API keys are not present, so official audio generation is blocked.
- Remotion is not installed in the project.
- Delivery/QA state remains unclear.

**Opportunity:** When active again, add a package index and delivery checklist, then generate official audio and template-based videos after credentials/assets are available.

---

### 10. Marathi translation artifacts

**What it is:** Local Marathi translation outputs/scripts and preview artifacts in the workspace.

**Current status:** Files exist, but there was no fresh session or file today clarifying ownership, QA state, or delivery status.

**Risks/blockers:**

- QA state unclear.
- Source/output mapping unclear.
- Delivery status unclear.

**Opportunity:** Create a small inventory only when this becomes active again: source file, translated output, reviewer, QA status, and delivery status.

## Cross-project risks and blockers

1. **Browser/CDP reliability is still the recurring blocker:** Etsy publishing, X research/posting, and authenticated browser workflows all depend on it.
2. **Creation is outpacing shipping:** Etsy assets, research ideas, and content drafts are strong, but need publishing and measurement.
3. **Workspace preservation risk:** Useful generated files are untracked. Preserve durable outputs while excluding browser/cache/secrets.
4. **Launch sequencing risk:** Wise AI landing page, HeirloomPlanners publishing, and AiteitAI BrandMemory are all viable, but only one or two should be pushed at once.
5. **Measurement gap:** HeirloomPlanners needs live listings and stats before further niche decisions are meaningful.

## 3 highest-leverage next actions

1. **Upload HeirloomPlanners trust assets and first Etsy draft manually.** Use the 2026-05-19 trust kit, then upload the Etsy Seller Profit & Listing Command Center first. This unlocks conversion trust and starts the measurement loop.

2. **Fix the browser/CDP/X operating bottleneck.** Restore reliable Mac Chrome remote debugging/tunnel and resolve X API credits if automated X research/posting remains desired. This removes friction across Etsy, X, and authenticated workflows.

3. **Preserve durable workspace outputs safely.** Add/update ignore rules, then commit/back up project maps, reports, Etsy product folders, scripts, and social-content drafts while excluding browser profiles, caches, logs, `.env`, and external repo internals.

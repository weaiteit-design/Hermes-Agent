# Project map: 2026-05-17

Sources inspected: `/root/Hermes-Agent`, current project/task/control docs, previous project map, recent reports, recent session summaries, new Etsy product outputs, and Git working-tree status for the workspace plus WiseAI external repos. No code was modified.

## Projects found

### 1. Wise AI
**What it is:** AI micro-lessons and updates platform, split across a mobile app repo and a landing page repo.

**Current status:** Landing page remains the closest public launch path. The prior review found TypeScript and production build passing when dummy Supabase env vars were supplied, while lint, dependency/security, SEO, security headers, and waitlist hardening remain. Mobile app is still not launch-ready because it is in a partial web-to-Expo migration state. A recent session also reviewed the Wurtle mascot/Lottie pack and concluded the current mascot reads as a generic cute blob more than a clear turtle.

**Local evidence:** `PROJECTS.md`, `TASKS.md`, `reports/2026-05-15-wiseai-codespace-review.md`, recent Wurtle session summary, and clean Git status in `/root/Hermes-Agent/external-repos/Delta-` and `/root/Hermes-Agent/external-repos/wiseai-landing`.

**Risks/blockers:**
- Mobile app still has web/Vite leftovers and React web primitives mixed into Expo/React Native code.
- Mobile repo previously had a tracked `.env` and API-like values. Treat secrets as exposed before production.
- Landing page still needs lint fixes, dependency/security updates, safer Supabase env handling, security headers, SEO files, and waitlist protection.
- Wurtle animation assets may be usable as placeholders, but not launch-quality if brand clarity matters.

**Opportunity:** Ship the landing page/waitlist first as a fast public milestone, then handle deeper mobile refactor and mascot polish.

---

### 2. HeirloomPlanners / Etsy digital products
**What it is:** A daily digital-product growth engine for Manas’s Etsy shop, now positioned as an A-to-Z Etsy operator with niche testing, product creation, QA, listing copy, images, and publishing support.

**Current status:** Very active. A new product package was created today:
- Folder: `/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit/`
- Product: ADHD Student Deadline Rescue Kit
- Included: printable PDF workbook, HTML source, Notion copy template, student email templates, prompt pack, 6 CSV trackers, listing copy, marketing notes, competitor notes, 3 PNG listing images, SVG fallback, and verified customer ZIP.
- Suggested price: $12.99 launch, with $14.99 to $17.99 test after early traction.

The growth tracker now logs both the 2026-05-16 Wedding Mini-Milestones Planner Kit and the 2026-05-17 ADHD Student Deadline Rescue Kit as ready local packages. The known Etsy shop snapshot remains 1 active listing, 0 sales/reviews, and trust setup 2/5 complete. Browser/CDP was unreliable during today’s Etsy cron run, so no draft/listing was safely created.

**Local evidence:** `reports/heirloomplanners-growth-tracker.md`, `reports/heirloomplanners-a-to-z-operator-brief.md`, and the 2026-05-17 product folder.

**Risks/blockers:**
- Publishing is now the bottleneck. Local products exist, but Etsy draft/live listing creation still needs manual upload or a more reliable authenticated upload flow.
- Shop trust assets remain incomplete: banner, shop story, seller/brand photo.
- The workspace Git status shows `reports/heirloomplanners-growth-tracker.md` modified and the new ADHD product folder untracked. This should be preserved or intentionally ignored.
- No feedback loop yet until listings are live and views/favorites/orders are tracked.

**Opportunity:** Manually publish the two strongest ready products and complete trust assets before generating many more products.

---

### 3. App idea and AI business opportunity research
**What it is:** Scheduled research around X app ideas and AI-executable business opportunities, aimed at ideas Manas can actually execute with Codex, Claude, Hermes, browser workflows, and creative tooling.

**Current status:** Reports from 2026-05-16 identified several strong signals:
- TikTok Creator Search Insights to “trend-to-app brief” generator, selected as the best pick.
- AI UGC ad sprint service for small brands.
- Persistent memory/run ledger for coding agents.
- Screen-time accountability circles without real-money gambling.
- AI handwriting improvement coach for students.

X research recently worked through logged-in Mac Chrome/CDP in one session, but the previous project map also noted the active container endpoint can fall back to a logged-out browser state. This remains an operational dependency.

**Local evidence:** `reports/2026-05-16-x-app-ideas-research.md`, `reports/2026-05-16-ai-business-opportunity-radar.md`, and the 2026-05-16 daily sync.

**Risks/blockers:**
- Research quality depends on stable logged-in X/browser access.
- Ideas can pile up without one small MVP or service test selected.
- The opportunity radar is strong, but needs conversion into execution artifacts: landing page, scorer, offer page, or service package.

**Opportunity:** Build a simple “TikTok CSI Opportunity Scorer” using pasted keywords/screenshots and turn it into both a tool and `manas_builds` content.

---

### 4. AiteitAI
**What it is:** AI-powered creative services startup for trailers, static ads, AI UGC, and AI-assisted creative production.

**Current status:** Still strategy-level in local docs. The business opportunity radar strengthens the near-term wedge: a 48-hour AI UGC ad sprint for small brands using scripts, product shots, Higgsfield-style video workflow, captions, and posting calendar.

**Local evidence:** `PROJECTS.md`, `TASKS.md`, and `reports/2026-05-16-ai-business-opportunity-radar.md`.

**Risks/blockers:**
- Official website/domain still needs confirmation.
- Service packages, pricing, proof assets, intake flow, and production workflow are not yet formalized.
- Higgsfield MCP/tooling is still not confirmed as connected locally.

**Opportunity:** Package one narrow offer: “3 AI UGC ads in 48 hours” for one buyer niche, then use Sociaaal/Manas creative workflows as proof.

---

### 5. Sociaaal creative workflows
**What it is:** Manas’s generative AI creative director work for app concepts, creative materials, editor coordination, trend research, and AI-assisted production.

**Current status:** Active responsibility area, but local artifacts are still mostly planning docs. The control center defines worker profiles that could support research, creative generation, review, and build tasks. The daily sync notes the opportunity radar now evaluates ideas against Manas’s current execution stack.

**Local evidence:** `PROJECTS.md`, `TASKS.md`, `MANAS_AGENT_CONTROL_CENTER.md`, and the daily sync report.

**Risks/blockers:**
- Reusable creative brief, editor handoff, app concept, and trend research templates are still open tasks.
- TikTok/Instagram research workflows need stable authenticated/safe access.
- Workflow knowledge may remain scattered across chats and one-off outputs.

**Opportunity:** Turn the AiteitAI AI UGC ad sprint into the first reusable Sociaaal creative operating kit.

---

### 6. LinkedIn / X growth content
**What it is:** Daily content engine for Manas around AI workflows, building in public, Wise AI, AiteitAI, creative AI, digital products, and Hermes agents.

**Current status:** Existing packs under `social-content/2026-05-15/` and `social-content/2026-05-16/` provide LinkedIn/X drafts, short posts, engagement ideas, and source notes. New material now exists from Etsy products, WiseAI/Wurtle review, X app ideas, and AI opportunity radar.

**Local evidence:** `social-content/`, the daily sync, and reports generated on 2026-05-16.

**Risks/blockers:**
- LinkedIn still lacks a reliable direct publishing route, so copy-paste remains safest.
- X research/posting depends on stable logged-in browser/CDP state.
- Content should be tied to real work to avoid generic AI commentary.

**Opportunity:** Use today’s ADHD product build, TikTok CSI scorer idea, and Wurtle mascot critique as authentic build-in-public posts.

---

### 7. Hermes workspace and multi-agent control center
**What it is:** Durable local workspace and Telegram-connected multi-agent control setup for Manas.

**Current status:** `/root/Hermes-Agent` remains the main hub. Control docs define Telegram as command center, shared board `manas-os`, dashboard on localhost, Kanban dispatcher, and worker profiles: orchestrator, researcher, builder, reviewer, creative. Cron jobs exist for Etsy, project context, social/growth, Higgsfield watch, X app ideas, opportunity radar, and daily Git sync.

**Workspace state checked today:**
- `/root/Hermes-Agent`: modified growth tracker plus untracked 2026-05-17 Etsy product folder.
- WiseAI external repos: clean.
- Obvious local work directory under `/root`: `Hermes-Agent`. Other top-level directories were tool/config related.

**Risks/blockers:**
- Generated outputs, browser profiles, logs, external repos, and durable docs need continued separation before commits.
- Markdown docs, Kanban, cron outputs, and session memory can drift without one weekly control surface.
- Dashboard should remain localhost-only unless secured.

**Opportunity:** Keep a curated daily preservation flow: durable reports/product outputs in Git, secrets/browser/cache files excluded.

---

### 8. Higgsfield MCP watch/setup
**What it is:** Scheduled checker/setup path for Higgsfield MCP to support Sociaaal and AiteitAI creative workflows.

**Current status:** Still appears to be a watch/setup item, not a confirmed usable local toolchain. The AiteitAI opportunity is becoming more important, so this blocker has higher leverage now.

**Risks/blockers:**
- Missing or unconfirmed transport/endpoint/command.
- Missing or unconfirmed auth method/token location.
- OAuth/manual account completion may be needed.

**Opportunity:** Once connected, it can directly support the AI UGC ad sprint and creative production workflow.

---

### 9. B2T1 Navigating the Digital Workspace
**What it is:** ITI/NCVET learner content package for “Navigating the Digital Workspace,” aimed at Mechanic Diesel and Mechanic Motor Vehicle learners.

**Current status:** Substantial generated package exists under `/root/Hermes-Agent/workspace/B2T1_Navigating_Digital_Workspace/`, including reading materials, PPT/DOCX/PDF assets, QA preview images, and production notes. No fresh changes were found today.

**Risks/blockers:**
- Video generation is paused per earlier notes.
- Needs human QA for template fidelity, simple-language rules, and no product/brand names in learner content.
- Delivery status is unclear.

**Opportunity:** Add a short delivery checklist and preserve production rules as reusable instructions for future modules.

---

### 10. Marathi translation artifacts
**What it is:** Local translated education/training materials and scripts.

**Current status:** Previously found as local outputs/artifacts, but no fresh session or file today clarified ownership, review state, or delivery status.

**Risks/blockers:**
- QA and delivery state unclear.
- Needs a concise project-level README if it is still active.

**Opportunity:** Create a small index of source files, generated files, language-review status, and delivery status when this work becomes active again.

## Cross-project risks and blockers

1. **Publishing/auth bottlenecks:** Etsy uploads, X browser access, LinkedIn publishing, GitHub preservation, and Higgsfield setup are the recurring operational blockers.
2. **Launch sequencing risk:** WiseAI landing page is the fastest public win, while the mobile app is still a larger migration/refactor.
3. **Feedback loop gap:** Etsy products, social posts, and research reports are being produced faster than they are being published and measured.
4. **Source-of-truth drift:** Markdown, cron outputs, sessions, Git status, and Kanban need one control surface to prevent stale next actions.
5. **Workspace hygiene:** New generated Etsy product files and modified reports need intentional preservation without committing browser profiles/secrets/logs.

## 3 highest-leverage next actions

1. **Publish and trust-build HeirloomPlanners:** Manually upload the Wedding Mini-Milestones Kit and ADHD Student Deadline Rescue Kit as Etsy drafts/live listings, then complete banner, story, and seller/brand photo. This converts existing work into measurable marketplace output.

2. **Ship WiseAI landing page before mobile:** Fix landing page lint/security/env/headers/SEO/waitlist items and deploy or prepare deployment. Defer mobile Expo cleanup and Wurtle polish until the waitlist can collect users.

3. **Turn the best research signal into one asset:** Build the TikTok Creator Search Insights “opportunity scorer” as a tiny form or spreadsheet-driven workflow, then use it for a `manas_builds` post and as a lead magnet/service entry point for AiteitAI/Sociaaal-style execution.

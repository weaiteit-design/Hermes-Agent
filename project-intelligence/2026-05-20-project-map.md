# Project map: 2026-05-20

Sources inspected: `/root/Hermes-Agent`, `PROJECTS.md`, `TASKS.md`, previous project maps, current Git status, reports, social-content, Etsy product folders, workspace/Tata STRIVE artifacts, and local repos under `/root/Hermes-Agent/external-repos`. Read-only inspection only, except writing this report.

## Tooling availability

- Codex CLI: installed at `/root/.hermes/node/bin/codex`, version `codex-cli 0.130.0`.
- Claude Code CLI: installed at `/root/.hermes/node/bin/claude`, version `2.1.141 (Claude Code)`.

## Projects found

### 1. HeirloomPlanners / Etsy digital products

**Current status:** Most active shipping project. Today’s fresh work is a publishing-control packet, not another SKU, which is the right move. The local backlog now has three verified customer ZIP products plus a verified shop-trust kit:

- Trust kit: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/`
- Publishing control sheet: `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-publishing-control-sheet.md`
- First upload packet: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/`
- Other ready packets: wedding mini-milestones kit and ADHD student deadline rescue kit.

**What changed today:** The first product copy was made more policy-safe by moving from platform-specific language to “Online Seller Profit Tracker & Listing Planner…”. ZIP integrity and dimensions were re-verified: trust kit ZIP OK, seller/wedding/student ZIPs OK, banner 3360×840, icon 500×500, first listing images 1536×1024.

**Ready for Codex/Claude Code execution:** Partly. Codex/Claude can keep improving local SOPs, QA scripts, listing copy, image manifests, upload queues, and analytics templates. They should not pretend to publish to Etsy from this server.

**Blockers:** Etsy live/draft state is still not verifiable here. Chrome/CDP at `127.0.0.1:9223` refused connection in today’s publishing run. Prior known baseline remains 1 active listing, no known sales/reviews, trust setup 2/5 complete unless Manas changed it manually. Laptop/browser access is a real blocker for Etsy Shop Manager actions.

### 2. Wise AI

**Current status:** Two local repos exist and are clean:

- Mobile app: `/root/Hermes-Agent/external-repos/Delta-`, branch `main`, package `delta-ai`, scripts include Expo and Vite (`start`, `android`, `ios`, `web`, `dev:vite`, `build:vite`, `preview:vite`). Last local summary: Wurtle mascot animations integrated.
- Landing page: `/root/Hermes-Agent/external-repos/wiseai-landing`, branch `landing-page`, package `wiseai`, Next.js app with `dev`, `build`, `start`, `lint`.

**Ready for Codex/Claude Code execution:** Yes, especially the landing page. Best next coding target is still launch-hardening the landing page before touching mobile polish. The mobile app needs a focused Expo migration/refactor and secret hygiene before store work.

**Blockers:** App-store-level testing and real device/simulator QA are laptop-only until Manas connects laptop SSH/Tailscale/local Hermes. Prior review also warned that mobile repo secrets/API-like values should be treated as exposed before production.

### 3. AiteitAI

**Current status:** Still mostly strategy/docs in this workspace, but the strongest current wedge is concrete: “AI UGC brand-memory + consistency kit” as a productized service. The 2026-05-19 opportunity radar says this fits AiteitAI/Sociaaal directly and can be validated without building SaaS first.

**Ready for Codex/Claude Code execution:** Yes for service assets: intake form, `brand-memory.md`, UGC shot list, prompt pack, QA checklist, client approval log, and a small landing/offer page. Actual Higgsfield/video generation remains tool/account dependent.

**Blockers:** Official domain/website and core packages are still unconfirmed. AI video tooling path is not confirmed on this server.

### 4. Sociaaal creative workflows

**Current status:** Active responsibility area from `PROJECTS.md`/`TASKS.md`; still under-templated. The AiteitAI brand-memory service can double as Sociaaal’s reusable creative workflow: intake → brand memory → hooks → storyboards → prompts → editor handoff → approval log.

**Ready for Codex/Claude Code execution:** Yes for templates and workflow docs. Not ready for authenticated TikTok/Instagram research automation from this server without browser/account access.

**Blockers:** TikTok/Instagram/app work requiring logged-in browser sessions is laptop-only or credentialed-browser-only. No reliable authenticated social posting path is confirmed here.

### 5. AI business opportunity radar / app idea discovery

**Current status:** Fresh radar on 2026-05-19 found the strongest opportunity as AI UGC brand-memory/consistency, with other viable ideas around agent control towers, TikTok CSI workflows, vertical price trackers, Community Notes archives, and local lead packs.

**Ready for Codex/Claude Code execution:** Yes for small dogfood MVPs. Highest alignment is a local agent run ledger/control tower inside Hermes, or BrandMemory service artifacts for AiteitAI. Do not start multiple SaaS builds at once.

**Blockers:** X research/posting is degraded: OAuth has worked for `manas_builds`, but API search/posting hit `CreditsDepleted`. Browser/CDP reliability is inconsistent.

### 6. Social content / personal growth engine

**Current status:** Fresh 2026-05-19 content pack exists at `/root/Hermes-Agent/social-content/2026-05-19/`. Best LinkedIn post is about agent systems: trigger, context, workspace, output, review. X copy was preflighted but not posted because credits were depleted; LinkedIn remains manual.

**Ready for Codex/Claude Code execution:** Yes for repurposing content packs, scheduling files, and turning project work into post drafts. Not ready for automated posting without X credits and authenticated LinkedIn route.

**Blockers:** Manual publishing required. X API credits and LinkedIn auth/posting remain blockers.

### 7. Hermes workspace / control center

**Current status:** `/root/Hermes-Agent` is the main hub. Current Git status shows valuable uncommitted work: modified HeirloomPlanners docs and listing/upload queue files, plus untracked 2026-05-20 HeirloomPlanners control/verification reports. External Wise repos are clean.

**Ready for Codex/Claude Code execution:** Yes for read-only review, safe preservation planning, `.gitignore` recommendations, and a selective commit plan. Code changes were not made during this run.

**Blockers:** Generated assets and client-work binaries need intentional preservation rules. Avoid committing credentials, browser profiles, caches, logs, `.env`, and external repo internals.

### 8. Tata STRIVE / B2T1 Navigating the Digital Workspace

**Current status:** Substantial local package exists under `/root/Hermes-Agent/workspace`, including final EN/MR ZIPs, rebuilt reading materials, PPTX/DOCX/PDF/XLSX outputs, QA previews, and production scripts. Latest daily sync says the safe Git helper excludes `workspace/`, so these outputs will not be committed by default.

**Ready for Codex/Claude Code execution:** Yes only if Manas reactivates the project and wants indexing, QA checklist, or packaging scripts. It is not the highest-leverage app/product coding target today.

**Blockers:** Preservation decision is manual: whether any generated Tata STRIVE binaries or source artifacts should go to GitHub despite current ignore rules. External template/sign-in and audio API credentials remain blocked from this environment.

## Which projects are ready for Codex/Claude Code execution now

1. **Wise AI landing page:** strongest coding target; clean repo, clear hardening tasks, deployable web surface.
2. **AiteitAI BrandMemory kit:** ready for Claude/Codex to create service docs, templates, and a lightweight offer page.
3. **HeirloomPlanners local publishing ops:** ready for QA/reporting/upload-queue improvements, but Etsy publishing itself is blocked by browser/laptop access.
4. **Hermes run ledger/control tower:** ready as a dogfood MVP if Manas wants an agent-ops product, but should not distract from immediate Etsy/Wise/AiteitAI shipping.

## Blockers and laptop-only access

- **Etsy Shop Manager publishing and metrics:** blocked here; needs Manas’s laptop/browser or restored Chrome CDP tunnel. Do not claim Etsy drafts/live listings from server-only inspection.
- **Wise AI mobile QA/App Store execution:** laptop/device/simulator work is blocked until laptop SSH/Tailscale/local Hermes is connected.
- **LinkedIn posting and TikTok/Instagram research:** manual or laptop/authenticated-browser access needed.
- **X automation:** OAuth has worked, but API credits are depleted for search/posting.
- **AiteitAI video generation:** Higgsfield/equivalent tooling path is not confirmed on this server.

## 3 highest-leverage next actions

1. **Manas: use the 2026-05-20 HeirloomPlanners control sheet for a 30-minute manual Etsy session.** Upload banner/icon/about copy, then create or publish the Online Seller Profit & Listing Command Center first. This is the clearest revenue-loop unlock.
2. **Codex/Claude Code: harden the Wise AI landing page.** Fix lint/security/env/waitlist issues, add SEO/headers/robots/sitemap/structured data, and prepare deployment before mobile refactor.
3. **Claude/Codex: package AiteitAI’s BrandMemory service into a sellable kit.** Create intake form, brand-memory template, shot list, 5 prompt variants, QA checklist, and approval log; Manas only needs to confirm the domain/brand positioning and provide one sample product/client.

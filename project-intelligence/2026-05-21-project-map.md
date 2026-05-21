# Project map: 2026-05-21

Sources inspected: `/root/Hermes-Agent`, `PROJECTS.md`, `TASKS.md`, `project-intelligence`, `reports`, `social-content`, `etsy-products`, and local repos under `/root/Hermes-Agent/external-repos`. Read-only inspection only, except writing this report.

## Tooling availability

- Codex CLI: installed at `/root/.hermes/node/bin/codex`, version `codex-cli 0.130.0`.
- Claude Code CLI: installed at `/root/.hermes/node/bin/claude`, version `2.1.141 (Claude Code)`.

## Projects found

### 1. HeirloomPlanners / Etsy digital products

**Current status:** Still the most active shipping/revenue project. Today’s new report is `/root/Hermes-Agent/reports/2026-05-21-heirloomplanners-shipping-status.md`: the backlog was re-verified for manual Etsy shipping, but no Etsy live/draft changes are claimed.

Verified upload-ready backlog:

- Shop trust kit: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/`
- First product priority: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/`
- Second: `/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit/`
- Third: `/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit/`

Today’s verification says all relevant ZIPs are OK; banner is 3360×840; icon is 500×500; product images are Etsy-friendly; first three backlog products have titles under 140 characters and exactly 13 valid tags.

**Ready for Codex/Claude Code execution:** Partly. Codex/Claude can improve QA scripts, upload queues, listing manifests, copy checks, metrics templates, and preservation/commit plans. They should not pretend to publish or verify Etsy Shop Manager from this server.

**Blockers:** Etsy live/draft state remains blocked. Both `127.0.0.1:9223` and `127.0.0.1:9222` refused connection in today’s shipping report, so listings, messages, orders, reviews, dashboard prompts, and draft state cannot be inspected. Laptop/browser access is the real blocker for Etsy publishing.

### 2. Wise AI

**Current status:** Two clean local repos exist:

- Mobile app: `/root/Hermes-Agent/external-repos/Delta-`, package `delta-ai`, scripts include Expo and Vite (`start`, `android`, `ios`, `web`, `dev:vite`, `build:vite`, `preview:vite`). Prior review says Wurtle mascot work is integrated, but the app still needs a proper native Expo cleanup/refactor before store execution.
- Landing page: `/root/Hermes-Agent/external-repos/wiseai-landing`, package `wiseai`, Next.js app with homepage, waitlist form, privacy page, terms page, metadata/OG basics, and scripts `dev`, `build`, `start`, `lint`.

**Ready for Codex/Claude Code execution:** Yes, especially the landing page. Best coding target remains landing-page launch hardening: lint fixes, dependency/security update, env handling, waitlist hardening, headers, sitemap/robots/manifest/structured data, and copy alignment if the app is not actually live.

**Blockers:** Mobile device/simulator QA, App Store/Play Store packaging, and real app verification are laptop-only until laptop SSH/Tailscale/local Hermes is connected. Prior review also says tracked/API-like values in the mobile repo should be treated as exposed before production.

### 3. AiteitAI

**Current status:** Still primarily strategy/docs in this workspace. `PROJECTS.md` and `TASKS.md` define it as an AI creative services startup needing domain confirmation, service packages, pitch structure, intake form, and creative production workflow. The strongest practical wedge from recent maps remains an AI UGC brand-memory/consistency service kit.

**Ready for Codex/Claude Code execution:** Yes for non-authenticated deliverables: offer structure, intake form, brand-memory template, UGC shot list, prompt pack, QA checklist, client approval log, and a lightweight offer page.

**Blockers:** Official website/domain and core positioning are still unconfirmed. AI video generation tools/accounts are not confirmed on this server.

### 4. Sociaaal creative workflows

**Current status:** Active responsibility area, but still under-templated. The work overlaps with AiteitAI: reusable creative workflows, app concept research templates, TikTok/Instagram research notes, and editor handoff systems.

**Ready for Codex/Claude Code execution:** Yes for templates and local docs. Good targets: creative brief template, app concept ideation template, editor workflow library, and authenticated-research SOP.

**Blockers:** TikTok/Instagram/app research that requires logged-in sessions is laptop/authenticated-browser-only. No reliable social posting path is confirmed here.

### 5. Social content / personal growth engine

**Current status:** Latest content pack is `/root/Hermes-Agent/social-content/2026-05-20/`. The strongest angle was “AI as a control sheet for unfinished execution loops,” grounded in the HeirloomPlanners publishing bottleneck. LinkedIn and X assets are drafts only.

**Ready for Codex/Claude Code execution:** Yes for repurposing project work into daily LinkedIn/X drafts, content calendars, and source notes. Not ready for automated posting.

**Blockers:** LinkedIn posting remains manual/auth blocked. X OAuth previously worked, but API search/posting hit `CreditsDepleted`; do not rely on X automation.

### 6. Hermes workspace / control center

**Current status:** `/root/Hermes-Agent` is the central workspace. Current Git status shows modified HeirloomPlanners operator/growth docs and untracked 2026-05-21 HeirloomPlanners reports; external Wise repos are clean. This map itself is the only intentional write from this run.

**Ready for Codex/Claude Code execution:** Yes for read-only review, preservation planning, `.gitignore` recommendations, report indexing, and a selective commit plan.

**Blockers:** Generated assets, client-work binaries, browser profiles, caches, logs, `.env`, and external repo internals need deliberate preservation rules before broad commits.

### 7. Tata STRIVE / B2T1 Navigating the Digital Workspace

**Current status:** Substantial generated package remains under `/root/Hermes-Agent/workspace`, including EN/MR ZIPs, PDFs, DOCX/PPTX/XLSX outputs, previews, and scripts. No fresh project movement found today.

**Ready for Codex/Claude Code execution:** Yes only if Manas reactivates it for QA/indexing/packaging. Not the highest-leverage coding target today.

**Blockers:** Manual decision needed on whether generated binaries/source artifacts should be preserved in Git; external template/sign-in/audio API access remains outside this server.

## Which projects are ready for Codex/Claude Code execution now

1. **Wise AI landing page:** strongest code target; clean repo and clear launch-hardening checklist.
2. **AiteitAI BrandMemory/creative service kit:** strongest service/productization target; no laptop app access required for templates and offer assets.
3. **HeirloomPlanners local ops:** ready for QA/reporting/upload-queue improvements; Etsy publishing itself is blocked by laptop/browser access.
4. **Hermes workspace control center:** ready for indexing, report map, and selective commit plan, but avoid broad commits until preservation rules are clear.

## Blockers and laptop-only access

- **Etsy Shop Manager publishing/metrics:** blocked here; needs Manas’s laptop/browser or restored Chrome CDP tunnel.
- **Wise AI mobile QA/App Store/Play Store execution:** laptop/device/simulator work blocked until laptop SSH/Tailscale/local Hermes is connected.
- **LinkedIn/TikTok/Instagram authenticated work:** manual or laptop/authenticated-browser access needed.
- **X automation:** OAuth has worked before, but API credits are depleted for search/posting.
- **AiteitAI video generation:** tool/account path not confirmed on this server.

## 3 highest-leverage next actions

1. **Manas: do a 30-minute Etsy manual shipping session.** Upload HeirloomPlanners banner/icon/about assets, then create/publish the Online Seller Profit & Listing Command Center using `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-publishing-control-sheet.md` and today’s shipping status report.
2. **Codex/Claude Code: harden Wise AI landing page.** Fix lint/security/env/waitlist issues and add launch SEO/headers/robots/sitemap/manifest/structured data before mobile refactor.
3. **Claude/Codex: package AiteitAI BrandMemory service.** Create intake, brand memory, shot list, prompts, QA checklist, approval log, and offer page; Manas only needs to confirm the domain/positioning and one sample client/product.

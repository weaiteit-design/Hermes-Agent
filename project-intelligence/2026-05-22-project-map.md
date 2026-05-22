# Project map: 2026-05-22

Sources inspected: `/root/Hermes-Agent`, `PROJECTS.md`, `TASKS.md`, `project-intelligence`, `reports`, `social-content`, `etsy-products`, `/root/Hermes-Agent/workspace`, and local repos under `/root/Hermes-Agent/external-repos`. Read-only inspection only, except writing this report.

## Tooling availability

- Codex CLI: installed at `/root/.hermes/node/bin/codex`, version `codex-cli 0.130.0`.
- Claude Code CLI: installed at `/root/.hermes/node/bin/claude`, version `2.1.141 (Claude Code)`.

## Projects found

### 1. HeirloomPlanners / Etsy digital products

**Current status:** This remains the most urgent revenue/execution project. Today's fresh report is `/root/Hermes-Agent/reports/2026-05-22-heirloomplanners-shipping-status.md`. It re-verifies the same shipping bottleneck: do not create another SKU yet; get the verified backlog into Etsy drafts/live listings so market feedback can begin.

Verified upload-ready backlog:

- Shop trust kit: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/`
- First product priority: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/`
- Second product: `/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit/`
- Third product: `/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit/`

Today's verification says the first three product ZIPs pass integrity checks; banner is 3360×840; icon is 500×500; seller/listing images are Etsy-friendly sizes; first three product titles are under 140 characters; each has exactly 13 tags and no tag over Etsy's 20-character limit.

**Ready for Codex/Claude Code execution:** Partly. Codex/Claude can improve local QA automation, listing packet manifests, upload checklists, safe copy checks, metrics templates, and preservation plans. They should not claim Etsy publishing or dashboard verification from this server.

**Blockers:** Etsy live/draft state is still blocked. Port `127.0.0.1:9223` is listening but behaves like an `sshd` tunnel and CDP discovery times out; `127.0.0.1:9222` refuses connection. Current listing count, messages, orders, reviews, dashboard prompts, drafts, and live state cannot be inspected. This is a laptop/browser/CDP blocker.

### 2. Wise AI

**Current status:** Two local repos exist and are clean:

- Mobile/app repo: `/root/Hermes-Agent/external-repos/Delta-`, package `delta-ai`, branch `main`, scripts include Expo and Vite (`start`, `android`, `ios`, `web`, `dev:vite`, `build:vite`, `preview:vite`). Wurtle mascot assets and integration files are present. `MIGRATION.md` says the repo is partway through Expo migration: storage/Gemini/Supabase updates exist, but many views still use web HTML/Tailwind patterns and need React Native conversion before App Store submission.
- Landing page repo: `/root/Hermes-Agent/external-repos/wiseai-landing`, package `wiseai`, branch `landing-page`, Next.js app with homepage, waitlist API, privacy, terms, metadata, and scripts `dev`, `build`, `start`, `lint`. The waitlist route has email validation, duplicate handling, and an in-memory rate limiter, but production hardening can still improve abuse resistance and deployment confidence.

**Ready for Codex/Claude Code execution:** Yes. Best target remains Wise AI landing-page launch hardening because it is local, clean, and app-store-independent. Mobile refactor is also code-ready, but native QA is limited from this server.

**Blockers:** Mobile device/simulator QA, App Store/Play Store packaging, and real app verification are laptop-only until laptop SSH/Tailscale/local Hermes is connected. The mobile repo's migration notes explicitly flag remaining web-to-React-Native conversion work and store setup requirements.

### 3. AiteitAI

**Current status:** Still mostly strategy/docs in this workspace. `PROJECTS.md` defines it as an AI creative services startup around trailers, static ads, and AI-assisted creative production. `TASKS.md` still needs domain verification, service package definitions, sales pitch structure, intake form, and creative production workflow.

**Ready for Codex/Claude Code execution:** Yes for non-authenticated deliverables: service packages, offer copy, pitch deck outline, intake form, brand-memory template, creative brief, UGC/ad shot-list template, QA checklist, client approval log, and lightweight offer page.

**Blockers:** Official website/domain and core positioning are unconfirmed. AI video tooling/account access is not verified on this server.

### 4. Sociaaal creative workflows

**Current status:** Active responsibility area, but still needs reusable operating templates. `PROJECTS.md` frames Manas's role as AI creative director across app concepts, AI execution, editor coordination, and TikTok/Instagram research workflows.

**Ready for Codex/Claude Code execution:** Yes for local templates and workflow docs: app concept ideation template, creative brief template, editor workflow library, authenticated-research SOP, and a reusable trend-to-creative handoff packet.

**Blockers:** TikTok/Instagram/app research that requires logged-in browsing is laptop/authenticated-browser-only. No reliable social publishing path is confirmed here.

### 5. Social content / personal growth engine

**Current status:** Latest content pack is `/root/Hermes-Agent/social-content/2026-05-21/`. The useful current angle is execution handoff: AI workflows should identify the exact unfinished loop and the smallest manual action needed, not keep creating inventory. LinkedIn/X drafts exist, but no posting was attempted.

**Ready for Codex/Claude Code execution:** Yes for turning real project work into daily LinkedIn/X drafts, repurposing reports into posts, creating a content calendar, and building source-note discipline.

**Blockers:** LinkedIn posting remains manual/auth-blocked. Prior X tooling can identify the account, but search/posting has been blocked by depleted API credits; do not rely on X automation.

### 6. Hermes workspace / control center

**Current status:** `/root/Hermes-Agent` is the central workspace. Git status shows modified HeirloomPlanners operator/growth docs and untracked 2026-05-22 HeirloomPlanners reports. External Wise repos are clean. This project-map file is the only intentional write from this run.

**Ready for Codex/Claude Code execution:** Yes for read-only reviews, report indexing, a selective commit plan, agent-run ledger templates, `.gitignore` recommendations, and preservation policy. The 2026-05-21 opportunity radar suggests a lightweight local-first agent run ledger/control layer as a strong dogfood opportunity.

**Blockers:** Broad commits should wait for deliberate preservation rules around generated assets, binaries, browser profiles, caches, logs, `.env`, and external repo internals.

### 7. Tata STRIVE / B2T1 Navigating the Digital Workspace

**Current status:** Substantial generated package remains under `/root/Hermes-Agent/workspace`, including EN/MR ZIPs, PDFs, DOCX/PPTX/XLSX outputs, previews, and rebuild scripts. No fresh movement found today.

**Ready for Codex/Claude Code execution:** Yes only if reactivated for QA/indexing/packaging. It is not the highest-leverage coding target today.

**Blockers:** Manual decision needed on whether generated binaries/source artifacts should be preserved in Git; external template/sign-in/audio API access remains outside this server.

## Which projects are ready for Codex/Claude Code execution now

1. **Wise AI landing page:** strongest pure-code target; clean repo and launch-hardening checklist.
2. **Wise AI mobile Expo cleanup:** ready for a scoped refactor pass, but native QA/store submission remains laptop-only.
3. **AiteitAI BrandMemory/creative service kit:** strongest non-code/productization target with no app access required.
4. **HeirloomPlanners local ops:** ready for QA/reporting/upload-packet improvements; Etsy publishing itself remains laptop/browser-blocked.
5. **Hermes agent-run ledger/control layer:** ready as a dogfood Markdown/SQLite starter around Codex/Claude tasks.

## Blockers and laptop-only access

- **Etsy Shop Manager publishing/metrics:** blocked here; needs Manas's laptop/browser or a restored working Chrome CDP tunnel.
- **Wise AI mobile QA/App Store/Play Store execution:** laptop/device/simulator work blocked until laptop SSH/Tailscale/local Hermes is connected.
- **LinkedIn/TikTok/Instagram authenticated work:** manual or laptop/authenticated-browser access needed.
- **X automation:** prior tooling exists but API credits are depleted for search/posting.
- **AiteitAI video generation:** tool/account path not confirmed on this server.

## 3 highest-leverage next actions

1. **Manas: complete the HeirloomPlanners 30-minute Etsy manual upload.** Upload banner/icon/about assets, then create or publish the Online Seller Profit & Listing Command Center using `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-publishing-control-sheet.md` and today's shipping status report.
2. **Codex/Claude Code: harden Wise AI landing page.** Run a scoped launch pass: lint/build, waitlist API hardening, env/deployment docs, SEO/manifest/robots/sitemap/structured data, and final privacy/terms copy alignment.
3. **Codex/Claude Code: create an agent-run ledger starter for Hermes.** Turn one real task into a local template with goal, repo, agent, commands, files changed, diff summary, risk, approval, verification, and next action; this is also a build-in-public content asset.

# Project map: 2026-05-23

Sources inspected: `/root/Hermes-Agent`, `PROJECTS.md`, `TASKS.md`, `project-intelligence`, `reports`, `social-content`, `etsy-products`, and local repos under `/root/Hermes-Agent/external-repos`. Read-only inspection only, except writing this report.

## Tooling availability

- Codex CLI: installed at `/root/.hermes/node/bin/codex`, version `codex-cli 0.130.0`.
- Claude Code CLI: installed at `/root/.hermes/node/bin/claude`, version `2.1.141 (Claude Code)`.

## Workspace / repo state

- Main workspace repo: branch `main`, tracking `origin/main`; modified HeirloomPlanners operator/growth docs; new generated Tata STRIVE materials and today's HeirloomPlanners reports are untracked.
- Wise AI mobile repo: `/root/Hermes-Agent/external-repos/Delta-`, branch `main`, clean working tree, ahead of remote by 1 local commit.
- Wise AI landing repo: `/root/Hermes-Agent/external-repos/wiseai-landing`, branch `landing-page`, clean working tree.
- Browser/CDP check today: local ports `9222`, `9223`, and `9224` are closed, so laptop/browser-only app access remains blocked from this server.

## Projects found

### 1. HeirloomPlanners / Etsy digital products

**Current status:** Still the most immediate revenue project, but the bottleneck is not product creation. Today's report (`/root/Hermes-Agent/reports/2026-05-23-heirloomplanners-shipping-status.md`) re-verifies the backlog and says no Etsy live/draft changes are claimed.

Upload-ready local backlog:

- Shop trust kit: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/`
- First product priority: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/`
- Second product: `/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit/`
- Third product: `/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit/`

Verified today: trust ZIP plus the three product ZIPs pass integrity checks; banner is 3360×840; icon is 500×500; listing images are Etsy-friendly sizes; first three listing titles are under 140 characters; each has exactly 13 tags and no tag over Etsy's 20-character limit.

**Ready for Codex/Claude Code execution:** Partly. Good targets are local QA automation, upload packet manifests, copy/policy checks, listing checklist generation, and metrics templates. They should not claim Etsy publishing, listing count, messages, orders, reviews, or draft state from this server.

**Blockers:** Etsy Shop Manager state is unavailable here. Ports `9222`, `9223`, and `9224` are closed today. Publishing/metrics require Manas's laptop/authenticated browser or a restored working CDP/Tailscale/local Hermes path.

### 2. Wise AI mobile app (`Delta-`)

**Current status:** Local repo exists and is clean, but it is ahead of its remote by 1 local commit. Package name is `delta-ai`; scripts include Expo (`start`, `android`, `ios`, `web`) and Vite (`dev:vite`, `build:vite`, `preview:vite`). `MIGRATION.md` says the Expo migration has made key storage/Gemini/Supabase changes, but many views still use web HTML/Tailwind patterns and need React Native conversion before store submission.

**Ready for Codex/Claude Code execution:** Yes for scoped code work: web-to-React-Native conversion inventory, Expo migration cleanup, TypeScript/build checks, app-store compliance checklist, and release-plan docs.

**Blockers:** Real iOS/Android simulator/device QA, EAS/store credentials, App Store/Play Store packaging, and final app verification are laptop/account-access tasks until laptop SSH/Tailscale/local Hermes is connected.

### 3. Wise AI landing page

**Current status:** Local repo exists and is clean on `landing-page`. It is a Next.js app (`next 16.1.6`, React 19) with scripts for `dev`, `build`, `start`, and `lint`. Prior inspection found homepage, waitlist API, privacy, terms, metadata, and a built `.next` output present.

**Ready for Codex/Claude Code execution:** Yes. This is the strongest pure-code target because it is local, clean, and not blocked by mobile devices. Best scoped pass: lint/build, waitlist API hardening, deployment docs, SEO/manifest/robots/sitemap/structured data, privacy/terms alignment, and production env checklist.

**Blockers:** Deployment platform credentials/domain decisions are not verified here. Anything involving live DNS or production deployment needs Manas/account access.

### 4. AiteitAI

**Current status:** Mostly strategy/docs in this workspace. `PROJECTS.md` defines it as an AI creative services startup for trailers, static ads, and AI-assisted creative production. `TASKS.md` still needs website/domain verification, core service packages, sales pitch structure, intake form, and creative production workflow.

**Ready for Codex/Claude Code execution:** Yes for non-authenticated deliverables: service packages, offer copy, pitch deck outline, intake form, creative brief, client approval workflow, case-study structure, and lightweight landing/offer page draft.

**Blockers:** Official website/domain and final positioning are unconfirmed. AI video/account access is not verified on this server.

### 5. Sociaaal creative workflows

**Current status:** Active responsibility area in docs, but no dedicated app repo found locally. `PROJECTS.md` frames Manas's role around app concepts, AI execution, creative direction, editor coordination, and TikTok/Instagram research workflows.

**Ready for Codex/Claude Code execution:** Yes for local workflow assets: app concept ideation template, creative brief template, editor workflow library, authenticated-research SOP, trend-to-creative handoff packet, and QA checklist.

**Blockers:** TikTok/Instagram/app research that requires logged-in browsing remains laptop/authenticated-browser-only. No reliable social publishing path is confirmed here.

### 6. Social content / build-in-public engine

**Current status:** Latest content pack is `/root/Hermes-Agent/social-content/2026-05-22/`. The strongest current angle is practical agent honesty: separate verified facts, blocked facts, and the exact safe human action instead of pretending authenticated/browser state is known.

**Ready for Codex/Claude Code execution:** Yes for turning real project work into LinkedIn/X drafts, repurposing daily project maps, building a content calendar, and creating source-note discipline.

**Blockers:** LinkedIn posting is manual/auth-blocked. Prior X setup identified the account, but X search/posting has been blocked by depleted API credits; do not rely on X automation.

### 7. Hermes workspace / control center

**Current status:** `/root/Hermes-Agent` remains the central workspace. There is accumulating generated work: HeirloomPlanners reports/products, social content, Tata STRIVE deliverables, and daily project maps. Git needs an intentional preservation/ignore/commit policy before broad cleanup.

**Ready for Codex/Claude Code execution:** Yes for a read-only repo hygiene audit, generated-asset policy, `.gitignore` recommendations, report index, agent-run ledger template, and a safe commit plan.

**Blockers:** Do not blindly commit generated binaries, browser profiles, caches, logs, `.env`, or external repo internals. Manas should choose what is source-of-truth vs generated output.

### 8. Tata STRIVE / instructional deliverables

**Current status:** Fresh generated deliverables exist in `/root/Hermes-Agent/deliverables/`, including B4T1 reading-material DOCX/ZIP packages and supporting assets/scripts. This looks active as a content/package generation project rather than an app repo.

**Ready for Codex/Claude Code execution:** Yes if reactivated for QA/indexing/packaging: manifest generation, version notes, reproducibility docs, and source-vs-output preservation plan.

**Blockers:** Manual decision needed on what generated binaries belong in Git. External templates, sign-in, client feedback, and final acceptance are outside this server.

## Which projects are ready for Codex/Claude Code execution now

1. **Wise AI landing page:** best pure-code target; local, clean, and launch-hardening-ready.
2. **Wise AI mobile Expo cleanup:** code-ready, but native QA/store packaging remains laptop-only.
3. **Hermes workspace control layer:** high leverage for agent-run ledger, generated-file policy, and daily work indexing.
4. **AiteitAI service kit:** ready for structured non-code deliverables without account access.
5. **HeirloomPlanners local ops:** ready for QA/upload-packet improvements; Etsy publishing itself is blocked here.

## Blockers and laptop-only access

- **Etsy Shop Manager publishing/metrics:** blocked here; needs Manas's laptop/authenticated browser or restored CDP/Tailscale/local Hermes access.
- **Wise AI mobile QA/App Store/Play Store:** blocked for real device/simulator/store execution until laptop/account access is connected.
- **LinkedIn/TikTok/Instagram authenticated work:** manual or laptop/authenticated-browser-only.
- **X automation:** account identification previously worked, but search/posting is not reliable because API credits were depleted.
- **AiteitAI video tooling:** tool/account path is not confirmed on this server.
- **Workspace Git hygiene:** needs preservation rules before broad commits or cleanup.

## 3 highest-leverage next actions

1. **Manas: finish the HeirloomPlanners manual Etsy upload loop.** Upload banner/icon/about assets, then create or publish the Online Seller Profit & Listing Command Center using `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-publishing-control-sheet.md`. Save as draft if any upload/preview is uncertain.
2. **Codex/Claude Code: run a Wise AI landing-page launch-hardening pass.** Scope it to lint/build, waitlist API hardening, SEO/deployment docs, privacy/terms checks, and a production launch checklist.
3. **Codex/Claude Code: create a Hermes agent-run ledger + generated-asset policy.** This should define how daily agent work, commands, diffs, reports, binaries, and external repos are tracked without polluting Git or losing useful deliverables.

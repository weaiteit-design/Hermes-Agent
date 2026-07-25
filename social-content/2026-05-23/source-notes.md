# Source notes, 2026-05-23

## Research inputs used
- `/root/Hermes-Agent/project-intelligence/2026-05-23-project-map.md`
- `/root/Hermes-Agent/reports/2026-05-23-heirloomplanners-shipping-status.md`
- `/root/Hermes-Agent/reports/daily-sync/2026-05-22-telegram-workspace-summary.md`
- `/root/Hermes-Agent/reports/2026-05-22-ai-business-opportunity-radar.md`
- Previous content packs:
  - `/root/Hermes-Agent/social-content/2026-05-22/`
  - `/root/Hermes-Agent/social-content/2026-05-21/`
- Live tool checks in this run:
  - `date +%F` returned `2026-05-23`.
  - `xurl auth status` shows default app `manas-x` with OAuth2 user `manas_builds`.
  - `xurl whoami` succeeded for `@manas_builds`.
  - `xurl search "from:manas_builds" -n 3` returned `CreditsDepleted`.
  - `curl` checks to `127.0.0.1:9222`, `9223`, and `9224` failed to connect.
  - `session_search` for recent Manas/social/Etsy context returned no matching sessions, so local workspace files were the primary source.

## Verified facts used in drafts
- The 2026-05-23 project map says Codex CLI is installed at `/root/.hermes/node/bin/codex`, version `codex-cli 0.130.0`.
- The 2026-05-23 project map says Claude Code CLI is installed at `/root/.hermes/node/bin/claude`, version `2.1.141 (Claude Code)`.
- The 2026-05-23 project map says local ports `9222`, `9223`, and `9224` are closed, blocking laptop/browser-only app access from this server.
- Wise AI mobile repo `/root/Hermes-Agent/external-repos/Delta-` is local, clean, and ahead of remote by one commit. It is ready for scoped code work but not real device/store verification from this server.
- Wise AI landing repo `/root/Hermes-Agent/external-repos/wiseai-landing` is local and clean on branch `landing-page`; the project map identifies it as the strongest pure-code target for launch hardening.
- HeirloomPlanners has local upload-ready assets and product ZIPs, but Etsy live/draft/dashboard state is unknown because authenticated Etsy access was not available.
- AiteitAI is currently strategy/docs-heavy and ready for non-auth deliverables like service packages, pitch structure, creative brief, and landing/offer copy.
- Sociaaal workflows have no dedicated local app repo found, but are ready for workflow assets like creative brief templates, editor workflow library, trend-to-creative handoff packet, and QA checklist.
- The 2026-05-22 opportunity radar identifies a Claude/Codex cross-session memory and run-history starter kit as the best pick for Manas because it matches Hermes/Codex/Claude workflows and can be dogfooded immediately.

## Platform/tool status
- X account identification works for `@manas_builds`; public metrics from `whoami`: 3 followers, 17 following, 70 tweets, 8 likes, 4 media.
- X API search remains unusable due to `CreditsDepleted`; no X posting was attempted.
- LinkedIn remains copy-paste/manual only; no authenticated publishing route was verified.
- Mac Chrome CDP browser access was not usable from this run.

## Content decision
Yesterday’s strongest post already focused on “blocked browser = useful information” and HeirloomPlanners upload handoff.

Today’s post shifts up one level: the useful artifact is an execution-environment project map. It keeps the content grounded in actual workspace state while avoiding another repeated Etsy-only recap.

Core angle: agents should first classify work into locally executable, code-ready but device/account-blocked, authenticated-browser-only, and human-approval-needed. That makes delegation to Hermes/Codex/Claude more honest.

## Claims intentionally avoided
- No claim that any Etsy listing is live, drafted, viewed, or sold.
- No claim that Wise AI landing hardening has been completed today.
- No claim that Wise AI mobile is ready for App Store/Play Store submission.
- No claim of LinkedIn/X trends from authenticated browsing.
- No claim that X/LinkedIn posting was automated.
- No revenue, customers, launch, order, review, traffic, or follower-growth claims beyond `xurl whoami` public account metrics.

# Source notes, 2026-05-22

## Research inputs used

- `/root/Hermes-Agent/project-intelligence/2026-05-22-project-map.md`
- `/root/Hermes-Agent/reports/2026-05-22-heirloomplanners-shipping-status.md`
- `/root/Hermes-Agent/reports/2026-05-22-heirloomplanners-backlog-verification.json`
- Previous content pack: `/root/Hermes-Agent/social-content/2026-05-21/`
- Prior session context from recent social-content cron runs.
- Live tool checks in this run:
  - `date +%F` returned `2026-05-22`.
  - `curl http://127.0.0.1:9223/json/version` failed to connect from this run.
  - `xurl auth status` shows `manas-x` OAuth2 for `manas_builds`.
  - `xurl whoami` succeeded for `@manas_builds`.
  - `xurl search "from:manas_builds" -n 3` returned `CreditsDepleted`.

## Verified facts used in drafts

- The 2026-05-22 project map says HeirloomPlanners/Etsy remains the most urgent revenue/execution project.
- The latest shipping report says no Etsy live/draft changes are claimed.
- Etsy dashboard state could not be inspected today: live listing count, drafts, messages, orders, reviews, and dashboard prompts remain unknown.
- The shipping report states `127.0.0.1:9223` was listening earlier but behaved like an `sshd` tunnel and CDP discovery timed out; `127.0.0.1:9222` refused connection.
- In this social run, direct curl to `127.0.0.1:9223/json/version` failed to connect.
- Shop banner is verified at 3360×840.
- Shop icon is verified at 500×500.
- Three product ZIPs pass integrity checks:
  - Online Seller Profit & Listing Command Center: 12 customer-facing files, price $14.99.
  - Wedding Mini-Milestones Planner Kit: 9 customer-facing files, price $14.99.
  - ADHD Student Deadline Rescue Kit: 16 customer-facing files, price $12.99.
- First upload priority remains Online Seller Profit & Listing Command Center.
- Each of the first three listings has exactly 13 tags and no tag over Etsy’s 20-character tag limit.
- Listing title lengths are under Etsy’s 140-character limit: 129, 122, and 129 characters.
- Safe publish rule: publish only after Etsy visibly shows image thumbnails, the ZIP filename persists after saving, title/description/tags/price/category are complete, and preview matches the promised files; save as draft if uploads clear or preview is wrong.

## Platform/tool status

- X API remains unusable for research/posting because search returns `CreditsDepleted`.
- X account identification works for `@manas_builds`; public metrics from `whoami`: 3 followers, 17 following, 70 tweets, 8 likes, 4 media.
- No X posting was attempted.
- LinkedIn remains copy-paste/manual only; no authenticated publishing route was verified.
- Mac Chrome CDP browser access was not usable from this run.

## Content decision

Today’s strongest angle is not another Etsy verification recap. It is the operating principle exposed by the blocker:

A useful agent should not pretend authenticated/browser state is known. It should separate verified facts, blocked facts, and the exact safe human action.

This keeps the post grounded in actual Hermes + Etsy work while avoiding unsupported platform claims.

## Claims intentionally avoided

- No claim that any Etsy listing is live or drafted.
- No claim of Etsy sales, customers, revenue, orders, reviews, or traffic.
- No claim that LinkedIn/X trends were researched through logged-in browser sessions.
- No claim that X/LinkedIn posting was automated.
- No claim that Manas personally completed the manual Etsy upload today.

# Source notes and angle rationale, 2026-05-20

## Accessible sources checked

1. Local project map
   - File: `/root/Hermes-Agent/project-intelligence/2026-05-20-project-map.md`
   - Signal: HeirloomPlanners/Etsy is the most active shipping project today. The map says the right move is a publishing-control packet, not another SKU.
   - It also says social content automation is blocked for posting: X credits depleted and LinkedIn auth route unavailable.

2. HeirloomPlanners publishing control sheet
   - File: `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-publishing-control-sheet.md`
   - Key source facts:
     - Do not create another SKU today.
     - First manual action: upload shop trust assets, then first product packet.
     - First product priority: Online Seller Profit & Listing Command Center.
     - Safe publish rule: publish only after image thumbnails, ZIP filename, category, price, tags, description, and preview are verified.

3. Verification JSON
   - File: `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-verification.json`
   - Key source facts:
     - Trust kit ZIP OK.
     - Seller command center customer ZIP OK.
     - Wedding kit customer ZIP OK.
     - Student deadline rescue customer ZIP OK.
     - Banner dimensions verified at 3360×840.
     - Icon dimensions verified at 500×500.
     - First product listing images verified at 1536×1024.

4. Prior social-content pack
   - Folder: `/root/Hermes-Agent/social-content/2026-05-19/`
   - Yesterday’s angle: agent systems as trigger/context/workspace/output/review.
   - Today’s angle extends it into a concrete local example: agent output as a publishing control sheet.

5. X/Twitter API status
   - `xurl auth status` shows app `manas-x` has OAuth2 for `manas_builds`.
   - `xurl whoami` succeeded for @manas_builds.
   - Current public metrics from `whoami`: 3 followers, 16 following, 70 tweets, 8 likes, 4 media.
   - `xurl search "from:manas_builds" -n 3` returned `CreditsDepleted`, so X API search/posting should not be used.

6. Browser/CDP status
   - `curl http://127.0.0.1:9223/json/version` failed to connect.
   - Mac Chrome CDP is not available from this run, so no browser-based X/LinkedIn research or posting was attempted.

7. External public feeds reachable from server
   - Hugging Face blog RSS reachable. Recent items included OlmoEarth v1.1, Ettin Reranker, Cosmos Predict 2.5 fine-tuning, PaddleOCR 3.5, and Open Agent Leaderboard.
   - HN RSS reachable. Front page included evaluation reliability / GitHub security items.
   - OpenAI RSS and Product Hunt RSS returned 403 from this environment.
   - These were not used as the main post angle because the strongest Manas-specific source today is the local HeirloomPlanners control-sheet work.

## Why today’s angle

Today’s best social angle is specific and grounded: AI as a control sheet for unfinished execution loops.

It connects Manas’s actual work:
- Hermes agent workflows
- Etsy digital product experiments
- Wise AI / teaching AI as practical systems
- AiteitAI/Sociaaal workflow thinking

It avoids unsupported claims:
- no sales/revenue claim
- no Etsy live listing claim
- no customer/client claim
- no automated posting claim

## Publishing status

- LinkedIn: draft only. No reliable authenticated LinkedIn publishing route confirmed.
- X/Twitter: draft only. OAuth works, but API search returned CreditsDepleted; do not post automatically.

## Best post today

Use `linkedin-post.md` as the main post. It is grounded in today’s actual workspace progress and has a clear practical lesson.

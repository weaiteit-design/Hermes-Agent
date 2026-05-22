# HeirloomPlanners Shipping Status — 2026-05-22

Status: backlog re-verified for manual Etsy shipping; no Etsy live/draft changes claimed.

## Operator decision
Do **not** create another SKU today. There are already multiple verified packages ready, and the growth bottleneck remains shop trust setup + getting the backlog into Etsy drafts/live listings so measurement can begin.

## Browser / Etsy access
- `127.0.0.1:9223` is listening, but it is an `sshd` tunnel and CDP discovery hangs/timeouts on `/json/version`, `/json/list`, and WebSocket discovery.
- `127.0.0.1:9222` refused connection.
- Browser tool navigation to Etsy Shop Manager timed out because CDP discovery failed.
- Result: current live listing count, messages, orders, reviews, draft state, and dashboard prompts could not be inspected today.
- Safe action: no automated draft/publish attempt; keep the manual upload packet as the highest-leverage action.

## What I verified today
Detailed JSON: `/root/Hermes-Agent/reports/2026-05-22-heirloomplanners-backlog-verification.json`

### Shop trust assets
- Banner: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-banner-3360x840.png` — 3360×840
- Icon: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-icon-500x500.png` — 500×500

### Backlog listings
1. **Online Seller Profit & Listing Command Center**
   - ZIP integrity: OK
   - ZIP file count: 12 customer-facing files
   - Title length: 129/140
   - Tags: exactly 13, all within Etsy's 20-character tag limit
   - Images: 3 files at 1536×1024
   - Price: $14.99
   - Upload first: highest buyer-intent product and best fit for measuring practical template demand.

2. **Wedding Mini-Milestones Planner Kit**
   - ZIP integrity: OK
   - ZIP file count: 9 customer-facing files
   - Title length: 122/140
   - Tags: exactly 13, all within Etsy's 20-character tag limit
   - Upload-ready images: 3 JPG files at 1200×800
   - Price: $14.99

3. **ADHD Student Deadline Rescue Kit**
   - ZIP integrity: OK
   - ZIP file count: 16 customer-facing files
   - Title length: 129/140
   - Tags: exactly 13, all within Etsy's 20-character tag limit
   - Images: 3 files at 1536×1024
   - Price: $12.99
   - Policy note: keep the non-medical study-organization disclaimer already in the listing.

## Manual upload order
1. Add banner + icon + shop announcement/about/FAQ from the trust launch kit.
2. Upload **Online Seller Profit & Listing Command Center** as the first draft/live listing.
3. Upload **Wedding Mini-Milestones Planner Kit** second.
4. Upload **ADHD Student Deadline Rescue Kit** third.

## Highest-leverage under-30-minute action for Manas
Open Etsy Shop Manager and complete the exact first packet in `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-publishing-control-sheet.md`:

- Upload banner: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-banner-3360x840.png`
- Upload icon: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-icon-500x500.png`
- Then create/publish the first product listing using:
  - Listing copy: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/listing.md`
  - Images: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/listing_images/01-listing-image.png`, `02-listing-image.png`, `03-listing-image.png`
  - ZIP: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/etsy-seller-command-center-customer-files.zip`

Safe publish rule: only publish once Etsy visibly shows all image thumbnails, the digital ZIP filename persists after saving, title/description/tags/price/category are complete, and the preview matches the promised files. If any upload widget clears files, save as draft instead.

# HeirloomPlanners Shipping Status — 2026-05-21

Status: backlog verified for manual Etsy shipping; no Etsy live/draft changes claimed.

## Operator decision
Do **not** create another SKU today. The growth bottleneck is still trust setup + publishing the verified backlog so Etsy can start collecting traffic/favorite/order signals.

## Browser / Etsy access
- Mac Chrome/CDP check failed again: `127.0.0.1:9223` and `127.0.0.1:9222` both refused connection.
- Result: current live listing count, messages, orders, reviews, draft state, and dashboard prompts could not be inspected today.
- Safe action: leave publishing as a manual 30-minute packet; do not claim any listing is live or drafted.

## What I verified today
Detailed JSON: `/root/Hermes-Agent/reports/2026-05-21-heirloomplanners-backlog-verification.json`

### Shop trust assets
- Trust kit ZIP: OK
- Banner: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-banner-3360x840.png` — 3360×840
- Icon: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-icon-500x500.png` — 500×500

### Backlog listings
1. **Online Seller Profit & Listing Command Center**
   - ZIP integrity: OK
   - Title length: 129/140
   - Tags: exactly 13, all within 20-character Etsy tag limit
   - Images: 3 files at 1536×1024
   - Price: $14.99
   - Upload first: highest buyer-intent product

2. **Wedding Mini-Milestones Planner Kit**
   - ZIP integrity: OK
   - Title length: 122/140
   - Tags: exactly 13, all within 20-character Etsy tag limit
   - Upload-ready images: 3 JPG files at 1200×800
   - Price: $14.99

3. **ADHD Student Deadline Rescue Kit**
   - ZIP integrity: OK
   - Title length: 129/140
   - Tags: exactly 13, all within 20-character Etsy tag limit
   - Images: 3 files at 1536×1024
   - Price: $12.99
   - Policy note: keep the non-medical study-organization disclaimer already in the listing.

## Manual upload order
1. Add banner + icon + shop announcement/about/FAQ from the trust launch kit.
2. Upload **Online Seller Profit & Listing Command Center** as the first draft/live listing.
3. Upload Wedding Mini-Milestones second.
4. Upload ADHD Student Deadline Rescue third.

## Highest-leverage under-30-minute action for Manas
Open Etsy Shop Manager and complete the exact packet in `/root/Hermes-Agent/reports/2026-05-20-heirloomplanners-publishing-control-sheet.md`:

- Upload banner: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-banner-3360x840.png`
- Upload icon: `/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit/heirloomplanners-shop-icon-500x500.png`
- Then create/publish the first product listing using:
  - Listing copy: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/listing.md`
  - Images: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/listing_images/01-listing-image.png`, `02-listing-image.png`, `03-listing-image.png`
  - ZIP: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/etsy-seller-command-center-customer-files.zip`

Safe publish rule: only publish once Etsy visibly shows all image thumbnails, the digital ZIP filename persists after saving, title/description/tags/price/category are complete, and the preview matches the promised files. If any upload widget clears files, save as draft instead.

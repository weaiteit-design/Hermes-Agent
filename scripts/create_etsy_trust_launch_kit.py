from pathlib import Path
import csv, json, shutil, zipfile
from PIL import Image, ImageDraw, ImageFont

root = Path('/root/Hermes-Agent/etsy-products/2026-05-19-heirloomplanners-shop-trust-launch-kit')
assets = root / 'assets'
assets.mkdir(parents=True, exist_ok=True)

# Colors
cream = '#F7F1E6'
paper = '#FFF9EF'
sage = '#8FA58B'
dark_sage = '#465747'
gold = '#C9A85D'
ink = '#2E332D'
muted = '#6D6A5F'

banner_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="3360" height="840" viewBox="0 0 3360 840" role="img" aria-label="HeirloomPlanners Etsy shop banner">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{paper}"/><stop offset="1" stop-color="{cream}"/></linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#77694D" flood-opacity=".18"/></filter>
    <pattern id="dots" width="48" height="48" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="2" fill="#D9CBAE" opacity=".28"/></pattern>
  </defs>
  <rect width="3360" height="840" fill="url(#bg)"/>
  <rect width="3360" height="840" fill="url(#dots)"/>
  <rect x="170" y="118" width="3020" height="604" rx="46" fill="#FFFDF7" opacity=".82" filter="url(#shadow)"/>
  <rect x="220" y="168" width="470" height="504" rx="34" fill="{sage}" opacity=".92"/>
  <path d="M305 270h300M305 342h240M305 414h300M305 486h210M305 558h265" stroke="{paper}" stroke-width="26" stroke-linecap="round" opacity=".9"/>
  <circle cx="575" cy="248" r="52" fill="{gold}" opacity=".88"/>
  <rect x="2730" y="178" width="340" height="420" rx="28" fill="{cream}" stroke="{gold}" stroke-width="8"/>
  <path d="M2790 280h220M2790 350h150M2790 420h220M2790 490h180" stroke="{sage}" stroke-width="18" stroke-linecap="round" opacity=".7"/>
  <text x="1680" y="342" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="150" fill="{ink}" letter-spacing="2">HeirloomPlanners</text>
  <line x1="1055" y1="400" x2="2305" y2="400" stroke="{gold}" stroke-width="6" opacity=".9"/>
  <text x="1680" y="492" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="62" fill="{dark_sage}" letter-spacing="3">DIGITAL PLANNERS • TRACKERS • SMALL BUSINESS SYSTEMS</text>
  <text x="1680" y="590" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="42" fill="{muted}">Printable PDFs, spreadsheet-ready CSVs, copy/paste workspaces, and clear instructions</text>
</svg>'''
(root / 'heirloomplanners-shop-banner-3360x840.svg').write_text(banner_svg, encoding='utf-8')

icon_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="500" height="500" viewBox="0 0 500 500" role="img" aria-label="HeirloomPlanners shop icon">
  <rect width="500" height="500" rx="92" fill="{cream}"/>
  <rect x="74" y="72" width="352" height="356" rx="42" fill="{paper}" stroke="{gold}" stroke-width="10"/>
  <rect x="116" y="118" width="268" height="70" rx="18" fill="{sage}"/>
  <text x="250" y="276" text-anchor="middle" font-family="Georgia, 'Times New Roman', serif" font-size="126" fill="{ink}">HP</text>
  <path d="M146 332h208M146 374h160" stroke="{sage}" stroke-width="18" stroke-linecap="round" opacity=".75"/>
</svg>'''
(root / 'heirloomplanners-shop-icon-500x500.svg').write_text(icon_svg, encoding='utf-8')

# Deterministic PNG exports using PIL so dimensions are exactly Etsy-friendly.
def font(size, bold=False):
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf' if not bold else '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for c in candidates:
        try: return ImageFont.truetype(c, size)
        except Exception: pass
    return ImageFont.load_default()

img = Image.new('RGB', (3360, 840), '#F7F1E6')
d = ImageDraw.Draw(img)
d.rounded_rectangle((170,118,3190,722), radius=46, fill='#FFFDF7', outline='#E3D2AA', width=6)
d.rounded_rectangle((220,168,690,672), radius=34, fill='#8FA58B')
for y,w in [(270,300),(342,240),(414,300),(486,210),(558,265)]:
    d.line((305,y,305+w,y), fill='#FFF9EF', width=26)
d.ellipse((523,196,627,300), fill='#C9A85D')
d.rounded_rectangle((2730,178,3070,598), radius=28, fill='#F7F1E6', outline='#C9A85D', width=8)
for y,w in [(280,220),(350,150),(420,220),(490,180)]:
    d.line((2790,y,2790+w,y), fill='#8FA58B', width=18)
brand = 'HeirloomPlanners'
sub = 'DIGITAL PLANNERS • TRACKERS • SMALL BUSINESS SYSTEMS'
tag = 'Printable PDFs, spreadsheet-ready CSVs, copy/paste workspaces, and clear instructions'
for text, y, f, fill in [(brand,285,font(150, True),'#2E332D'),(sub,455,font(62),'#465747'),(tag,560,font(42),'#6D6A5F')]:
    bbox = d.textbbox((0,0), text, font=f)
    d.text(((3360-(bbox[2]-bbox[0]))/2,y), text, font=f, fill=fill)
d.line((1055,400,2305,400), fill='#C9A85D', width=6)
img.save(root / 'heirloomplanners-shop-banner-3360x840.png', quality=95)

icon = Image.new('RGB', (500,500), '#F7F1E6')
di = ImageDraw.Draw(icon)
di.rounded_rectangle((74,72,426,428), radius=42, fill='#FFF9EF', outline='#C9A85D', width=10)
di.rounded_rectangle((116,118,384,188), radius=18, fill='#8FA58B')
bbox=di.textbbox((0,0),'HP',font=font(126, True))
di.text(((500-(bbox[2]-bbox[0]))/2,210),'HP',font=font(126, True),fill='#2E332D')
di.line((146,332,354,332), fill='#8FA58B', width=18)
di.line((146,374,306,374), fill='#8FA58B', width=18)
icon.save(root / 'heirloomplanners-shop-icon-500x500.png', quality=95)

# Copy generated OpenAI visual as optional inspiration/mockup, preserving provenance.
gen = Path('/root/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260519_033514_ed9638b8.png')
if gen.exists():
    shutil.copy2(gen, root / 'openai-banner-concept-1536x1024.png')

(root / 'shop_about_announcement_faq.md').write_text('''# HeirloomPlanners Shop Trust Copy

## Positioning line
Practical digital planners, trackers, and small-business systems for calmer decisions and better follow-through.

## Shop announcement
Welcome to HeirloomPlanners — practical digital planners, printable workbooks, spreadsheet trackers, and small-business systems for calmer decisions and better follow-through. Every download is built for clarity, easy use, and everyday organization. New digital systems are added as we test what helps buyers most.

## About / story
HeirloomPlanners creates warm, practical digital organization tools for real life: events, study, work, business, money, and life admin. The shop aesthetic is calm and timeless — cream paper, sage, and soft gold — but the products are built to be useful first: printable PDFs, spreadsheet-ready CSVs, copy/paste workspaces, and clear instructions.

The goal is to help buyers move from scattered notes to simple systems they can actually use. Products are designed to be approachable for ordinary buyers: open the README, choose the PDF/HTML/spreadsheet/workspace format that fits, and start with one page or tracker.

Because products are digital downloads, no physical item is shipped. Please read each listing for included file types, compatibility notes, and license terms.

## FAQ copy
**Are these physical products?**  
No. HeirloomPlanners sells digital downloads only. No physical item will be shipped.

**What apps do I need?**  
Each listing states the included formats. Many products include PDFs, HTML files, CSV spreadsheets, and Markdown/Notion copy text that can be used with common free or built-in apps.

**Can I resell or share the files?**  
No. Unless a listing says otherwise, files are for personal/small-business internal use only and may not be resold, redistributed, sublicensed, or claimed as your own template product.

**What if I have trouble opening a file?**  
Send a message with the product name, file name, and device/app you are using. I will help troubleshoot.

## Policy/safety notes for seller
- Do not promise revenue, grades, rankings, medical outcomes, legal/tax/accounting results, or guaranteed life changes.
- Keep all customer-facing copy clear that products are digital downloads.
- Use descriptive product terms only; avoid copyrighted/trademarked brands, characters, celebrity names, or official-looking logos.
''', encoding='utf-8')

(root / 'shop_sections_and_seo_architecture.md').write_text('''# Shop Sections and SEO Architecture

## Recommended broad shop persona
HeirloomPlanners should remain broad but coherent: **calm, practical digital organization systems**. This allows niche testing without confusing buyers.

## Recommended Etsy sections
1. Small Business Systems
2. Student & Study Planners
3. Wedding & Event Kits
4. Printable Workbooks
5. Spreadsheet Trackers
6. Notion + AI Workflows
7. Life Admin Planners

## Naming system
Use outcome-first names, not generic template names:
- [Audience] + [Pain] + [System/Kit]
- [Outcome] + [Tracker/Planner/Command Center]
- [Event/Workflow] + [Checklist + Spreadsheet Bundle]

Examples:
- Etsy Seller Profit & Listing Command Center
- ADHD Student Deadline Rescue Kit
- Wedding Mini-Milestones Planner Kit

## Listing title architecture
Primary keyword + secondary keyword + audience/use case + format/bundle.
Keep under 140 characters and avoid keyword stuffing.

## Tag architecture
Use all 13 tags. Mix:
- buyer identity: student planner, seller planner, wedding planner
- pain/outcome: deadline tracker, profit tracker, guest list
- format: spreadsheet, printable, notion template, digital download
- broader discovery: small biz tools, study planner, event planner
''', encoding='utf-8')

rows = [
    ['priority','product','niche','price_usd','folder','customer_zip','listing_images','status','next_step'],
    ['1','Etsy Seller Profit & Listing Command Center','small-business seller operations','14.99','/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/','/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/etsy-seller-command-center-customer-files.zip','/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/listing_images/','ready local package; not verified as Etsy draft','Upload first; highest buyer intent and $14.99 bundle'],
    ['2','Wedding Mini-Milestones Planner Kit','wedding/event systems','14.99','/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit/','/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit/wedding-mini-milestones-kit-customer-files.zip','/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit/listing_images/*-upload.jpg','ready local package; not verified as Etsy draft','Upload second; aligns with Etsy wedding-season signal'],
    ['3','ADHD Student Deadline Rescue Kit','student productivity','12.99','/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit/','/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit/adhd-student-deadline-rescue-kit-customer-files.zip','/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit/listing_images/','ready local package; not verified as Etsy draft','Upload third; keep non-medical positioning'],
]
with (root / 'ready_listing_upload_queue.csv').open('w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(rows)

(root / 'manual_upload_sop.md').write_text('''# Manual Etsy Upload SOP — HeirloomPlanners

## First 30 minutes today
1. Upload `heirloomplanners-shop-banner-3360x840.png` as the shop banner.
2. Upload `heirloomplanners-shop-icon-500x500.png` as the shop icon if a seller photo/brand icon is acceptable; otherwise use a real seller/brand photo.
3. Paste the shop announcement and about/story from `shop_about_announcement_faq.md`.
4. Create/upload the first product draft: Etsy Seller Profit & Listing Command Center.

## Product upload order
Use `ready_listing_upload_queue.csv`.

## First product exact paths
- Listing copy: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/listing.md`
- Images: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/listing_images/01-listing-image.png`, `02-listing-image.png`, `03-listing-image.png`
- Digital ZIP: `/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center/etsy-seller-command-center-customer-files.zip`
- Suggested launch price: $14.99

## Save/publish rule
Publish only after Etsy visibly shows all image thumbnails, the digital ZIP filename persists after saving, listing category/price/tags/description are complete, and preview matches the files promised. If any upload widget clears files or cannot be verified, save as draft and retry manually.
''', encoding='utf-8')

(root / 'marketing_launch_copy.md').write_text('''# Launch Copy for Trust Refresh + First Listings

## Pinterest pin ideas
1. Calm digital planner shop for real-life organization — printable workbooks, spreadsheet trackers, and copy/paste systems.
2. New Etsy seller command center: profit tracker, listing planner, launch checklist, and AI prompts in one download.
3. From scattered notes to simple systems: HeirloomPlanners digital downloads for study, events, business, and life admin.

## Social posts
1. I’m building HeirloomPlanners around practical digital systems: PDFs you can print, CSVs you can import, and workflows you can actually use.
2. First shop focus: higher-value bundles, not generic one-page planners — seller tools, student systems, wedding/event kits, and life-admin trackers.
3. New shop assets are live-ready: warm heirloom paper tones, sage/cream/gold visual identity, and clear digital-download buyer instructions.

## Short launch message
HeirloomPlanners is becoming a calm digital systems shop: practical planners, trackers, printable workbooks, and small-business kits with clear instructions and no physical shipping.
''', encoding='utf-8')

qa = {
    'date': '2026-05-19',
    'asset_type': 'shop trust and launch kit',
    'banner_png_dimensions': Image.open(root / 'heirloomplanners-shop-banner-3360x840.png').size,
    'icon_png_dimensions': Image.open(root / 'heirloomplanners-shop-icon-500x500.png').size,
    'openai_concept_copied': (root / 'openai-banner-concept-1536x1024.png').exists(),
    'files_checked': [p.name for p in root.iterdir() if p.is_file()],
    'policy_checks': ['digital-download language included', 'no income guarantees', 'no copyrighted/trademarked visual assets', 'no review manipulation', 'no Etsy affiliation claims'],
    'publishing_status': 'assets created locally; Etsy dashboard/browser automation timed out, so no draft/live changes claimed'
}
(root / 'qa_summary.json').write_text(json.dumps(qa, indent=2), encoding='utf-8')

zip_path = root / 'heirloomplanners-shop-trust-launch-kit.zip'
include = [p for p in root.iterdir() if p.is_file() and p.name != zip_path.name]
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in include:
        z.write(p, p.name)
with zipfile.ZipFile(zip_path) as z:
    assert z.testzip() is None
    (root / 'zip_contents.txt').write_text('\n'.join(z.namelist()) + '\n', encoding='utf-8')
print(root)
print(zip_path)
print((root / 'zip_contents.txt').read_text())

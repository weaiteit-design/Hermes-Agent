from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import csv, shutil, textwrap, os, json
from datetime import date

root = Path('/root/Hermes-Agent/etsy-products/2026-05-18-etsy-seller-profit-listing-command-center')
customer = root / 'customer_files'
csvdir = customer / 'csv'
imgdir = root / 'listing_images'
for d in [customer, csvdir, imgdir]:
    d.mkdir(parents=True, exist_ok=True)

# Copy generated listing images if present
srcs = [
    '/root/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260518_033415_b1648f32.png',
    '/root/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260518_033519_e34be8d4.png',
    '/root/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260518_033639_2f593fa3.png',
]
for i, src in enumerate(srcs, 1):
    p = Path(src)
    if p.exists():
        shutil.copy2(p, imgdir / f'{i:02d}-listing-image.png')

readme = """# Etsy Seller Profit & Listing Command Center

Thank you for your purchase! This is a digital download bundle for small-shop owners and digital product sellers who want a calmer way to plan products, track listing performance, and understand basic profit.

## What is included

- `etsy_seller_command_center.pdf` — ready-to-print US Letter workbook.
- `etsy_seller_command_center.html` — editable/printable browser version of the workbook.
- `notion_copy_workspace.md` — copy/paste workspace for Notion or any notes app.
- `prompt_pack.md` — AI prompts for product research, listing copy, image planning, content, and customer support drafting.
- `csv/01_profit_calculator.csv` — simple pricing, fees, cost, and profit worksheet.
- `csv/02_listing_seo_tracker.csv` — title, tags, keyword angle, and status tracker.
- `csv/03_product_launch_pipeline.csv` — idea-to-launch workflow board.
- `csv/04_30_day_content_calendar.csv` — simple launch/promotion calendar.
- `csv/05_customer_message_templates.csv` — polite support response templates.
- `csv/06_review_safe_improvement_log.csv` — product quality and feedback improvement tracker.
- `csv/07_tax_prep_expense_log.csv` — simple expense categories for annual organization.

## How to use

1. Open the PDF and print the workbook pages you want, or use them digitally in a PDF reader.
2. Import any CSV into Google Sheets, Excel, Numbers, Airtable, or Notion.
3. Copy the Notion workspace markdown into a Notion page if you want a simple dashboard.
4. Use the prompts as drafting helpers. Always review outputs before publishing.

## Important notes

- This is a digital product. No physical item will be shipped.
- This bundle is an organization and planning aid, not legal, tax, accounting, or financial advice.
- The profit calculator uses simple placeholder fee fields so you can adapt it to your actual platform, currency, taxes, production costs, and payment processor.
- Personal/small-business use only. You may not resell, redistribute, sublicense, or claim these files as your own template product.
"""
(customer / 'README.md').write_text(readme, encoding='utf-8')

html = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Etsy Seller Profit & Listing Command Center</title>
<style>
@page { size: Letter; margin: 0.45in; }
:root{--sage:#7f927f;--cream:#fbf6ea;--paper:#fffdf7;--gold:#c7a85b;--ink:#2d2b27;--muted:#6d6a61;}
*{box-sizing:border-box} body{font-family:Arial,Helvetica,sans-serif;color:var(--ink);background:var(--cream);margin:0;}
.page{page-break-after:always;background:var(--paper);min-height:10in;padding:.35in;border:1px solid #eadfcb;position:relative;}
h1,h2{font-family:Georgia,'Times New Roman',serif;margin:0 0 .12in;} h1{font-size:34px;color:#3e5142} h2{font-size:24px;color:#3e5142;border-bottom:3px solid var(--gold);padding-bottom:8px;}
p{line-height:1.35;color:var(--muted)} .tag{display:inline-block;background:#edf1e9;color:#3e5142;padding:7px 10px;border-radius:999px;margin:4px;font-size:12px;font-weight:bold;}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.box{border:1px solid #d9ccb4;background:#fffaf0;border-radius:12px;padding:12px;min-height:95px}.full{grid-column:1/-1}.line{border-bottom:1px solid #d8d0c1;height:28px}.small{font-size:12px;color:#777}.table{width:100%;border-collapse:collapse;margin-top:8px}th{background:#dfe8dc;color:#34463a}td,th{border:1px solid #ddd0bc;padding:8px;text-align:left;font-size:12px}.accent{color:var(--gold);font-weight:bold}.cover{display:flex;align-items:center;justify-content:center;text-align:center;min-height:9in;background:linear-gradient(135deg,#fffdf7,#f2eadb)}.cover-card{border:2px solid var(--gold);padding:.5in;border-radius:24px;max-width:7in;background:rgba(255,255,255,.72)}
@media print{body{background:white}.page{border:none;min-height:auto}}
</style></head><body>
<section class="page cover"><div class="cover-card"><p class="tag">Printable + CSV + Notion Copy Workspace</p><h1>Etsy Seller Profit & Listing Command Center</h1><p>A calm operations kit for planning digital products, tracking listing quality, organizing launch tasks, and estimating simple profit before you publish.</p><p class="small">Digital planning aid only. No income guarantee. Not financial, tax, legal, or accounting advice.</p></div></section>
<section class="page"><h2>1. Product Idea Scorecard</h2><p>Score ideas before you spend hours building. Favor specific buyer pain, low support burden, clear keywords, and files you can QA well.</p><table class="table"><tr><th>Idea</th><th>Buyer pain</th><th>Keyword</th><th>Build ease</th><th>Support risk</th><th>Next action</th></tr><tr><td></td><td></td><td></td><td>/5</td><td>/5</td><td></td></tr><tr><td></td><td></td><td></td><td>/5</td><td>/5</td><td></td></tr><tr><td></td><td></td><td></td><td>/5</td><td>/5</td><td></td></tr></table></section>
<section class="page"><h2>2. Listing SEO Planner</h2><div class="grid"><div class="box"><b>Primary keyword</b><div class="line"></div><div class="line"></div></div><div class="box"><b>Buyer outcome</b><div class="line"></div><div class="line"></div></div><div class="box full"><b>Title draft under 140 characters</b><div class="line"></div><div class="line"></div></div><div class="box full"><b>13 tag ideas</b><p>1_____ 2_____ 3_____ 4_____ 5_____ 6_____ 7_____ 8_____ 9_____ 10_____ 11_____ 12_____ 13_____</p></div></div></section>
<section class="page"><h2>3. Simple Profit Snapshot</h2><p>Use your real fees, taxes, ad spend, and production costs. This page is for planning clarity, not accounting advice.</p><table class="table"><tr><th>Item</th><th>Amount</th><th>Notes</th></tr><tr><td>Listing price</td><td></td><td></td></tr><tr><td>Platform/payment fees</td><td></td><td></td></tr><tr><td>Tax/VAT reserve</td><td></td><td></td></tr><tr><td>Ad spend per sale</td><td></td><td></td></tr><tr><td>Net estimate</td><td></td><td></td></tr></table></section>
<section class="page"><h2>4. 30-Day Launch Calendar</h2><table class="table"><tr><th>Week</th><th>Focus</th><th>Content ideas</th><th>Improvement action</th></tr><tr><td>1</td><td>Publish + verify</td><td>Problem, preview, how-to</td><td>Check photos/files</td></tr><tr><td>2</td><td>SEO learning</td><td>Use cases, FAQ</td><td>Improve tags/title once</td></tr><tr><td>3</td><td>Trust</td><td>Behind the template, support</td><td>Add clearer image</td></tr><tr><td>4</td><td>Decision</td><td>Bundle/adjacent idea</td><td>Expand, revise, or pause</td></tr></table></section>
<section class="page"><h2>5. Review-Safe Improvement Log</h2><p>Track feedback and improve the product without asking for or manipulating reviews.</p><table class="table"><tr><th>Date</th><th>Signal</th><th>Issue/opportunity</th><th>Fix made</th><th>Version</th></tr><tr><td></td><td>View/favorite/message/order</td><td></td><td></td><td></td></tr><tr><td></td><td>View/favorite/message/order</td><td></td><td></td><td></td></tr><tr><td></td><td>View/favorite/message/order</td><td></td><td></td><td></td></tr></table></section>
<section class="page"><h2>6. Customer Support Templates</h2><div class="box"><b>Download help reply</b><p>Hi! Thanks for reaching out. This is a digital download, so you can access the files from your purchases/downloads page. If a file gives you trouble, please tell me which file/device you are using and I’ll help troubleshoot.</p></div><div class="box"><b>File update reply</b><p>Thank you for flagging this. I’m reviewing the file now and will update the download if a correction is needed.</p></div></section>
</body></html>'''
(customer / 'etsy_seller_command_center.html').write_text(html, encoding='utf-8')

notion = """# Etsy Seller Profit & Listing Command Center — Notion Copy Workspace

## Product Pipeline
| Idea | Buyer | Keyword | Status | Next Action |
|---|---|---|---|---|
| | | | Research / Build / QA / Listed / Improve / Pause | |

## Listing QA Checklist
- [ ] Title under 140 characters
- [ ] 13 concise tags
- [ ] Digital download clearly stated
- [ ] No trademarked/copyrighted terms
- [ ] Images legible on mobile
- [ ] Files open and ZIP is verified
- [ ] Instructions included

## Weekly Review
- Views:
- Favorites:
- Orders:
- Messages/questions:
- Conversion notes:
- Improve / expand / pause decision:
"""
(customer / 'notion_copy_workspace.md').write_text(notion, encoding='utf-8')

prompts = """# Prompt Pack for Digital Product Sellers

Use these as drafting helpers. Review everything before publishing.

## Product idea scoring
Act as a cautious Etsy digital-product researcher. Score these product ideas for buyer pain, specificity, build feasibility, support risk, and differentiation. Avoid trademarks and unrealistic income claims.

## Listing title drafting
Write 10 Etsy title options under 140 characters for a digital download. Include buyer outcome, product type, and file format. Avoid keyword stuffing.

## Listing description outline
Draft a warm Etsy description with: what is included, who it is for, how to use it, digital download note, compatibility limits, and FAQ.

## Image planning
Create 5 listing image concepts that show the product clearly without tiny text or income claims.

## Customer support
Draft a kind response to a buyer who cannot find their digital download. Do not ask for a review.

## Improvement review
Given views, favorites, orders, and messages, recommend whether to improve SEO/images once, create an adjacent product, bundle, or pause the niche.
"""
(customer / 'prompt_pack.md').write_text(prompts, encoding='utf-8')

csvs = {
'01_profit_calculator.csv': [
    ['Product','Listing Price','Discount %','Platform/Payment Fee Estimate','Ad Spend Per Sale','Production Cost','Tax Reserve','Estimated Net Profit','Notes'],
    ['Example Digital Planner','14.99','0','1.50','0.00','0.00','0.00','=B2-(B2*C2/100)-D2-E2-F2-G2','Replace example values with your own']
],
'02_listing_seo_tracker.csv': [['Listing','Primary Keyword','Secondary Keywords','Title Draft','Tag 1','Tag 2','Tag 3','Tag 4','Tag 5','Tag 6','Tag 7','Tag 8','Tag 9','Tag 10','Tag 11','Tag 12','Tag 13','Status','Notes']],
'03_product_launch_pipeline.csv': [['Idea','Buyer Persona','Pain Point','Files Needed','Build Status','QA Status','Listing Status','Price','Next Action','Decision']],
'04_30_day_content_calendar.csv': [['Day','Channel','Hook','Post Idea','Asset Needed','Status','Notes']] + [[str(i),'Pinterest / Instagram / X','','','','Planned',''] for i in range(1,31)],
'05_customer_message_templates.csv': [['Situation','Template','Personalization Notes'],['Download help','Hi! Thanks for reaching out. This is a digital download, so you can access the files from your purchases/downloads page. If a file gives you trouble, please tell me which file/device you are using and I will help troubleshoot.','Add order-specific file name if relevant'],['Correction/update','Thank you for flagging this. I am reviewing the file now and will update the download if a correction is needed.','Never promise unverified timing']],
'06_review_safe_improvement_log.csv': [['Date','Signal Type','What Buyer/Metric Suggested','Change Made','Version','Follow-up Needed']],
'07_tax_prep_expense_log.csv': [['Date','Vendor','Category','Amount','Currency','Receipt Link/Location','Business Purpose','Notes']]
}
for name, rows in csvs.items():
    with (csvdir / name).open('w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(rows)

listing = """# Etsy Listing Copy — Etsy Seller Profit & Listing Command Center

## SEO title (135/140 chars)
Etsy Seller Profit Tracker & Listing Planner, Small Business Spreadsheet, Digital Product Shop Command Center, Printable Bundle

## Suggested category
Paper & Party Supplies > Paper > Planners & Calendars OR Templates > Spreadsheets. Use the closest Etsy category available during listing.

## Suggested launch price
USD $14.99 launch price. Test $17.99 after first traction. INR equivalent: about ₹1,250 launch price before Etsy/local fee considerations.

## 13 Etsy tags
1. seller planner
2. profit tracker
3. listing planner
4. etsy spreadsheet
5. shop planner
6. product tracker
7. seo tracker
8. business planner
9. digital download
10. pricing tracker
11. launch planner
12. small biz tools
13. notion template

## Description
Plan, price, launch, and improve your digital product listings with one calm command center. This digital download bundle is designed for small-shop owners and digital sellers who want practical tools for organizing product ideas, listing SEO, launch tasks, simple profit estimates, content promotion, customer support notes, and product improvement decisions.

WHAT YOU RECEIVE
- Ready-to-print US Letter PDF workbook
- Editable/printable HTML workbook source
- 7 CSV trackers for spreadsheets, Notion, Airtable, Excel, Google Sheets, or Numbers
- Copy/paste Notion workspace markdown
- AI prompt pack for product research, listing drafting, image planning, content, and support replies
- Buyer instructions and personal-use license

FILES INCLUDED
PDF, HTML, Markdown, and CSV files inside one ZIP folder.

IMPORTANT
This is a digital download. No physical item will be shipped. This is an organization/planning tool only and is not legal, tax, accounting, financial, or business advice. It does not guarantee sales, revenue, ranking, or results.

HOW TO USE
Download the ZIP, open the README, print the PDF pages you need, and import the CSV files into your preferred spreadsheet app. You can also copy the Notion markdown into a Notion page.

## FAQ
Q: Is this a physical planner?  
A: No. This is a digital download only.

Q: Does it work with Google Sheets or Excel?  
A: The included CSV files can be imported into Google Sheets, Excel, Numbers, Airtable, Notion, and most spreadsheet tools.

Q: Is this tax or accounting advice?  
A: No. The profit and expense pages are simple organization aids. Please consult a qualified professional for tax/accounting decisions.

Q: Can I resell the files?  
A: No. The files are for personal/small-business use only and may not be resold, redistributed, sublicensed, or claimed as your own template product.
"""
(root / 'listing.md').write_text(listing, encoding='utf-8')

marketing = """# Marketing Assets

## Pinterest pins
1. A calm command center for digital product sellers: track listing ideas, SEO, profit estimates, and launch tasks in one printable + spreadsheet bundle.
2. Starting or organizing a small online shop? Use this seller planner to map products, tags, pricing, content, and product improvements without scattered notes.
3. Digital seller workflow kit: PDF workbook, spreadsheet trackers, Notion copy workspace, and prompt pack for a cleaner launch process.

## Social posts
1. Building digital products is easier when your ideas, pricing, listing SEO, and launch tasks live in one place. New: a practical seller command center bundle.
2. Before publishing another listing, score the idea, check the buyer pain, estimate profit, and plan how you’ll improve it after real signals.
3. A gentle reminder: tracking views, favorites, messages, and product fixes is more useful than guessing. This kit gives small sellers a simple system.

## Launch message
New in the shop: Etsy Seller Profit & Listing Command Center — a printable, spreadsheet, Notion-copy, and prompt bundle for digital sellers who want a calmer way to plan listings and track product decisions.
"""
(root / 'marketing.md').write_text(marketing, encoding='utf-8')

competitor = """# Competitor / Market Notes

## Source limitations
- Logged-in Etsy Shop Manager / Chrome CDP was unavailable during this cron run, so current shop metrics, orders, reviews, messages, and Etsy advisor prompts could not be verified today.
- Public Reddit JSON was blocked by network policy.
- Research used accessible DuckDuckGo snippets and YouTube search-page titles.

## Observed demand signals
- DuckDuckGo snippets show active marketplace demand for Etsy seller bookkeeping spreadsheets, profit trackers, shop planners, listing SEO trackers, and all-in-one business spreadsheets.
- YouTube search results repeatedly emphasize profitable/unsaturated Etsy digital products, product research, low-competition templates, launching products, and digital planner vs tracker demand.
- This product targets sellers with commercial intent and a recurring operational pain: tracking products, SEO, pricing, launch tasks, and improvement decisions.

## Positioning
Many seller spreadsheets are pure bookkeeping/accounting or pure Canva planners. This bundle differentiates as a low-friction command center: printable workbook + CSV trackers + Notion-copy workspace + prompt pack, with careful no-guarantee, no-tax-advice positioning.

## Niche test hypothesis
Small-business/digital-seller operations tools can become a higher-value product line ($14.99-$19.99) with adjacent products: niche research boards, listing-image planners, shop audit checklists, and launch content calendars.
"""
(root / 'competitor_notes.md').write_text(competitor, encoding='utf-8')

# Simple SVG fallback listing image
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1200" viewBox="0 0 1600 1200"><rect width="1600" height="1200" fill="#fbf6ea"/><rect x="120" y="110" width="1360" height="980" rx="36" fill="#fffdf7" stroke="#c7a85b" stroke-width="6"/><text x="800" y="235" text-anchor="middle" font-family="Georgia" font-size="70" fill="#3e5142">Profit &amp; Listing Command Center</text><text x="800" y="310" text-anchor="middle" font-family="Arial" font-size="34" fill="#6d6a61">Printable PDF • CSV Trackers • Notion Copy Workspace • Prompt Pack</text><rect x="210" y="420" width="520" height="360" rx="24" fill="#dfe8dc"/><rect x="260" y="470" width="420" height="42" fill="#fffdf7"/><rect x="260" y="545" width="420" height="42" fill="#fffdf7"/><rect x="260" y="620" width="420" height="42" fill="#fffdf7"/><rect x="850" y="405" width="520" height="420" rx="24" fill="#fffaf0" stroke="#d9ccb4"/><text x="1110" y="485" text-anchor="middle" font-family="Georgia" font-size="42" fill="#3e5142">Track What Matters</text><text x="1110" y="560" text-anchor="middle" font-family="Arial" font-size="30" fill="#6d6a61">Ideas • SEO • Pricing</text><text x="1110" y="620" text-anchor="middle" font-family="Arial" font-size="30" fill="#6d6a61">Launch Tasks • Improvements</text><text x="1110" y="680" text-anchor="middle" font-family="Arial" font-size="30" fill="#6d6a61">Customer Support Notes</text><rect x="320" y="900" width="960" height="90" rx="45" fill="#7f927f"/><text x="800" y="958" text-anchor="middle" font-family="Arial" font-size="38" font-weight="700" fill="#fffdf7">Digital download bundle for small-shop sellers</text></svg>'''
(root / 'cover_mockup_fallback.svg').write_text(svg, encoding='utf-8')

# Create PDF with reportlab fallback
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    pdf_path = customer / 'etsy_seller_command_center.pdf'
    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='HPTitle', parent=styles['Title'], fontName='Times-Bold', fontSize=25, textColor=colors.HexColor('#3e5142'), leading=31))
    styles.add(ParagraphStyle(name='HPH', parent=styles['Heading2'], fontSize=17, textColor=colors.HexColor('#3e5142'), spaceAfter=10))
    story = []
    story.append(Paragraph('Etsy Seller Profit & Listing Command Center', styles['HPTitle']))
    story.append(Paragraph('A printable workbook for planning digital products, listing SEO, simple profit estimates, launches, and product improvements.', styles['BodyText']))
    story.append(Spacer(1, .2*inch))
    for title, rows in [
        ('Product Idea Scorecard', [['Idea','Buyer pain','Keyword','Ease','Support risk','Next action'],['','','','/5','/5',''],['','','','/5','/5',''],['','','','/5','/5','']]),
        ('Listing SEO Planner', [['Primary keyword','Buyer outcome','Title draft','13 tag ideas'],['','','','']]),
        ('Simple Profit Snapshot', [['Item','Amount','Notes'],['Listing price','',''],['Fees','',''],['Ad spend per sale','',''],['Net estimate','','']]),
        ('30-Day Launch Calendar', [['Week','Focus','Content ideas','Improvement action'],['1','Publish + verify','Problem/preview/how-to','Check files/photos'],['2','SEO learning','Use cases/FAQ','Improve tags once'],['3','Trust','Behind template/support','Add clearer image'],['4','Decision','Bundle/adjacent idea','Expand/revise/pause']]),
        ('Review-Safe Improvement Log', [['Date','Signal','Issue/opportunity','Fix made','Version'],['','','','',''],['','','','','']])
    ]:
        story.append(PageBreak())
        story.append(Paragraph(title, styles['HPH']))
        tbl = Table(rows, repeatRows=1)
        tbl.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dfe8dc')),('TEXTCOLOR',(0,0),(-1,0),colors.HexColor('#34463a')),('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#cfc3ad')),('VALIGN',(0,0),(-1,-1),'TOP'),('FONT',(0,0),(-1,-1),'Helvetica'),('FONTSIZE',(0,0),(-1,-1),8),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, colors.HexColor('#fffaf0')])]))
        story.append(tbl)
    story.append(PageBreak())
    story.append(Paragraph('Customer Support Templates', styles['HPH']))
    story.append(Paragraph('Download help: Hi! Thanks for reaching out. This is a digital download, so you can access the files from your purchases/downloads page. If a file gives you trouble, please tell me which file/device you are using and I will help troubleshoot.', styles['BodyText']))
    story.append(Spacer(1,.15*inch))
    story.append(Paragraph('File update: Thank you for flagging this. I am reviewing the file now and will update the download if a correction is needed.', styles['BodyText']))
    doc.build(story)
except Exception as e:
    (root / 'PDF_GENERATION_ERROR.txt').write_text(str(e), encoding='utf-8')

# Buyer ZIP only customer-facing files
zip_path = root / 'etsy-seller-command-center-customer-files.zip'
files = [p for p in customer.rglob('*') if p.is_file()]
with ZipFile(zip_path, 'w', ZIP_DEFLATED) as z:
    for f in sorted(files):
        z.write(f, f.relative_to(customer))
with ZipFile(zip_path) as z:
    bad = z.testzip()
    if bad:
        raise RuntimeError(f'Bad zip member: {bad}')
    contents = z.namelist()
(root / 'zip_contents.txt').write_text('\n'.join(contents), encoding='utf-8')

# QA summary
qa = {
    'zip_path': str(zip_path),
    'zip_file_count': len(contents),
    'zip_integrity': 'OK',
    'pdf_exists': (customer/'etsy_seller_command_center.pdf').exists(),
    'pdf_size_bytes': (customer/'etsy_seller_command_center.pdf').stat().st_size if (customer/'etsy_seller_command_center.pdf').exists() else 0,
    'html_exists': (customer/'etsy_seller_command_center.html').exists(),
    'csv_count': len(list(csvdir.glob('*.csv'))),
    'listing_image_count': len(list(imgdir.glob('*.png'))),
    'fallback_svg_exists': (root/'cover_mockup_fallback.svg').exists(),
}
(root / 'qa_summary.json').write_text(json.dumps(qa, indent=2), encoding='utf-8')
print(json.dumps(qa, indent=2))
print('\nZIP CONTENTS:')
print('\n'.join(contents))

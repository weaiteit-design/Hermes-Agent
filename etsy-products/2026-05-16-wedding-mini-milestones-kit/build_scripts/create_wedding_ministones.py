from pathlib import Path
import csv, json, zipfile, textwrap, datetime

base = Path('/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit')
cf = base/'customer_files'
mock = base/'listing_images'
for p in [cf, mock]: p.mkdir(parents=True, exist_ok=True)

readme = """# Wedding Mini-Milestones Planner Kit

Thank you for purchasing this digital wedding mini-milestones kit from HeirloomPlanners.

## What is included
- `wedding-mini-milestones-workbook.html` — editable/printable source workbook.
- `wedding-mini-milestones-workbook.pdf` — ready-to-print US Letter PDF when included in your download.
- `mini-milestones-checklist.csv` — milestone-by-milestone task list for engagement party, bridal shower, bachelor/bachelorette weekend, rehearsal dinner, ceremony week, and day-after brunch.
- `mini-event-budget.csv` — budget tracker for small wedding-related events.
- `vendor-contact-tracker.csv` — quick vendor and helper contact tracker.
- `timeline-template.csv` — day-of timeline starter for showers, brunches, rehearsals, and weekend events.
- `notion-copy-instructions.md` — simple instructions for copying the CSV tables into Notion, Google Sheets, Excel, or Numbers.
- `ai-planning-prompts.md` — practical prompts to turn your notes into checklists, invitation text, timelines, and follow-up messages.

## How to use
1. Open the PDF and print the pages you need, or open the HTML file in a browser and print to PDF/paper.
2. Import the CSV files into Google Sheets, Excel, Numbers, or Notion.
3. Duplicate rows for each mini-event you are hosting.
4. Use the AI prompt pack with your preferred AI assistant to draft wording, timelines, and vendor questions.

## Digital download terms
This is a digital product. No physical item will be shipped.

## License
Personal use only for one household/couple/wedding planning team. You may print copies for your own wedding planning. You may not resell, redistribute, share publicly, or claim the files as your own.

## Support
If you have trouble opening a file, message the shop with your device/app and we will help with a friendly workaround.
"""
(cf/'README.md').write_text(readme, encoding='utf-8')

rows = [
 ['Milestone','Ideal timing','Task','Owner','Status','Notes'],
 ['Engagement party','8-12 months before','Choose host, guest count, and casual budget','','Not started',''],
 ['Engagement party','8-12 months before','Pick date, location, and simple theme','','Not started',''],
 ['Engagement party','6-8 months before','Send invitations and collect RSVPs','','Not started',''],
 ['Bridal/couple shower','3-5 months before','Confirm host, registry note, and guest list','','Not started',''],
 ['Bridal/couple shower','2-4 months before','Plan food, games, gifts table, and thank-you card station','','Not started',''],
 ['Bachelor/bachelorette','2-4 months before','Set realistic per-person budget and payment deadlines','','Not started',''],
 ['Bachelor/bachelorette','2-3 months before','Book stay/activities and collect emergency contacts','','Not started',''],
 ['Rehearsal dinner','1-3 months before','Confirm venue, menu, speeches, and seating style','','Not started',''],
 ['Ceremony week','Wedding week','Pack detail box, vendor balances, rings, licenses, and emergency kit','','Not started',''],
 ['Day-after brunch','1-2 months before','Decide host, drop-in time, casual menu, and cleanup owner','','Not started',''],
 ['All mini-events','Anytime','Record thank-you notes, final costs, and lessons learned','','Not started',''],
]
with (cf/'mini-milestones-checklist.csv').open('w', newline='', encoding='utf-8') as f: csv.writer(f).writerows(rows)

budget = [['Event','Category','Planned','Actual','Paid by','Due date','Notes'],
 ['Engagement party','Venue/host contribution','','','','',''],['Engagement party','Food + drinks','','','','',''],['Engagement party','Invitations + decor','','','','',''],
 ['Shower','Food + drinks','','','','',''],['Shower','Games/favors/decor','','','','',''],['Bach weekend','Lodging','','','','',''],['Bach weekend','Activities','','','','',''],['Rehearsal dinner','Restaurant/catering','','','','',''],['Day-after brunch','Food + coffee','','','','',''],['All','Tips/thank-you gifts','','','','','']]
with (cf/'mini-event-budget.csv').open('w', newline='', encoding='utf-8') as f: csv.writer(f).writerows(budget)

vendors = [['Event','Name/business','Role','Phone','Email','Confirmed?','Deposit/fee','Final due','Notes'],['Rehearsal dinner','','Restaurant/caterer','','','No','','',''],['Shower','','Host/helper','','','No','','',''],['Bach weekend','','Activity/lodging','','','No','','',''],['Day-after brunch','','Host/caterer','','','No','','','']]
with (cf/'vendor-contact-tracker.csv').open('w', newline='', encoding='utf-8') as f: csv.writer(f).writerows(vendors)

timeline = [['Time','Moment','Owner','Supplies needed','Notes'],['9:00 AM','Setup begins','','',''],['10:30 AM','Food/drinks ready','','',''],['11:00 AM','Guests arrive','','',''],['11:15 AM','Welcome/toast','','',''],['12:00 PM','Main activity or meal','','',''],['1:15 PM','Photos/gifts/speeches','','',''],['2:00 PM','Clean-up handoff','','','']]
with (cf/'timeline-template.csv').open('w', newline='', encoding='utf-8') as f: csv.writer(f).writerows(timeline)

notion = """# Notion / Spreadsheet Copy Instructions

## Google Sheets, Excel, or Numbers
1. Open a new spreadsheet.
2. Import each CSV file as a separate sheet/tab.
3. Rename tabs: Checklist, Budget, Vendors, Timeline.
4. Duplicate rows for every mini-event you are hosting.

## Notion
1. Create a new page.
2. Type `/table` and choose Table - Full page or Inline.
3. Import the CSV files, or copy/paste the rows from your spreadsheet.
4. Add Status, Owner, Date, and Notes views for a lightweight planning dashboard.

Tip: Keep one master page named “Wedding Mini-Milestones” and create linked filtered views for each event.
"""
(cf/'notion-copy-instructions.md').write_text(notion, encoding='utf-8')

prompts = """# AI Planning Prompts

Use these prompts with your preferred AI assistant. Replace bracketed details with your wedding details.

1. Mini-event checklist:
“Act as a calm wedding planning assistant. Create a realistic checklist for our [engagement party/bridal shower/rehearsal dinner/day-after brunch]. Date: [date]. Guest count: [number]. Budget: [amount]. Vibe: [casual/elegant/family-style]. Include owner, deadline, and notes columns.”

2. Budget sanity check:
“Review this event budget and suggest where to simplify without making guests feel under-cared-for: [paste budget rows]. Give low-cost alternatives and decision deadlines.”

3. Host message:
“Draft a warm, concise message to [parents/maid of honor/best man/friend] asking for help with [task]. Tone: grateful, clear, not demanding.”

4. Timeline builder:
“Turn these event details into a minute-by-minute timeline with setup, guest arrival, food, activities, speeches, photos, clean-up, and owner for each step: [paste details].”

5. Vendor questions:
“Create 12 practical questions to ask a [restaurant/caterer/florist/venue] for a small wedding-related event. Include questions about fees, timing, setup, cancellation, and accessibility.”

6. Thank-you notes:
“Write 5 short thank-you note options for someone who helped with [event/task]. Tone: heartfelt, specific, not overly formal.”
"""
(cf/'ai-planning-prompts.md').write_text(prompts, encoding='utf-8')

html = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Wedding Mini-Milestones Planner Kit</title>
<style>
@page { size: Letter; margin: 0; }
:root{--paper:#fbf5ea;--sage:#8fa58a;--deep:#314034;--gold:#c8a45d;--cream:#fffaf0;--ink:#273029;}
body{margin:0;background:#eee;color:var(--ink);font-family:Georgia,'Times New Roman',serif;}
.page{width:8.5in;min-height:11in;background:var(--paper);box-sizing:border-box;padding:.55in;page-break-after:always;position:relative;}
.page:before{content:"";position:absolute;inset:.25in;border:1.5px solid var(--gold);opacity:.65;pointer-events:none}.content{position:relative;z-index:1}h1,h2{font-family:Arial,Helvetica,sans-serif;color:var(--deep);letter-spacing:.02em}h1{font-size:34px;margin:0 0 14px}h2{font-size:22px;margin:0 0 10px}.kicker{font-family:Arial,sans-serif;text-transform:uppercase;letter-spacing:.18em;color:var(--sage);font-size:12px}.sub{font-size:18px;line-height:1.45;max-width:6.5in}.badge{display:inline-block;background:var(--sage);color:white;border-radius:999px;padding:7px 12px;margin:6px 6px 0 0;font-family:Arial,sans-serif;font-size:12px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.card{background:rgba(255,250,240,.82);border:1px solid rgba(200,164,93,.5);border-radius:14px;padding:14px}.line{height:22px;border-bottom:1px solid #cabf9d}.small{font-family:Arial,sans-serif;font-size:12px;line-height:1.4}table{width:100%;border-collapse:collapse;background:rgba(255,250,240,.75);font-family:Arial,sans-serif;font-size:11px}th{background:var(--sage);color:#fff;text-align:left}td,th{border:1px solid #d7c79d;padding:7px;vertical-align:top}.quote{font-size:23px;color:var(--deep);border-left:5px solid var(--gold);padding-left:16px;line-height:1.35}.footer{position:absolute;left:.55in;right:.55in;bottom:.35in;font-family:Arial,sans-serif;font-size:10px;color:#6d6a5e;display:flex;justify-content:space-between}
@media print{body{background:white}.page{box-shadow:none}}
</style></head><body>
<section class="page"><div class="content"><div class="kicker">HeirloomPlanners</div><h1>Wedding Mini-Milestones Planner Kit</h1><p class="sub">A calm, practical planning system for the meaningful events around the wedding: engagement party, shower, bachelor/bachelorette weekend, rehearsal dinner, ceremony week, and day-after brunch.</p><span class="badge">Printable workbook</span><span class="badge">Budget CSVs</span><span class="badge">Timeline templates</span><span class="badge">AI prompts</span><div style="height:.4in"></div><div class="quote">Plan the small moments with the same care as the big day — without turning every celebration into a second wedding.</div></div><div class="footer"><span>Digital download • No physical item shipped</span><span>Personal use license</span></div></section>
<section class="page"><div class="content"><div class="kicker">Start here</div><h2>Mini-Milestone Map</h2><div class="grid"><div class="card"><b>Engagement Party</b><p class="small">Host, guest count, casual budget, invitations, food plan, photo moment.</p></div><div class="card"><b>Shower</b><p class="small">Host handoff, registry note, games/favors, thank-you workflow.</p></div><div class="card"><b>Bach Weekend</b><p class="small">Transparent cost split, safety contacts, itinerary, payments.</p></div><div class="card"><b>Rehearsal Dinner</b><p class="small">Venue, menu, speeches, seating, final family logistics.</p></div><div class="card"><b>Ceremony Week</b><p class="small">Payments, rings, license, packing, emergency kit, contacts.</p></div><div class="card"><b>Day-After Brunch</b><p class="small">Simple hosting, leftover logistics, family goodbyes, cleanup.</p></div></div></div><div class="footer"><span>Wedding Mini-Milestones Planner Kit</span><span>2</span></div></section>
<section class="page"><div class="content"><div class="kicker">Worksheet</div><h2>Event Snapshot</h2><table><tr><th>Event</th><th>Date/time</th><th>Host/owner</th><th>Guest count</th><th>Budget cap</th></tr><tr><td>Engagement party</td><td></td><td></td><td></td><td></td></tr><tr><td>Shower</td><td></td><td></td><td></td><td></td></tr><tr><td>Bach weekend</td><td></td><td></td><td></td><td></td></tr><tr><td>Rehearsal dinner</td><td></td><td></td><td></td><td></td></tr><tr><td>Day-after brunch</td><td></td><td></td><td></td><td></td></tr></table><h2 style="margin-top:24px">Top decisions this week</h2><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="footer"><span>Wedding Mini-Milestones Planner Kit</span><span>3</span></div></section>
<section class="page"><div class="content"><div class="kicker">Budget</div><h2>Mini-Event Budget Planner</h2><table><tr><th>Event</th><th>Category</th><th>Planned</th><th>Actual</th><th>Paid by</th><th>Due</th></tr><tr><td></td><td>Venue/host contribution</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Food + drinks</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Invitations/printing</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Decor/florals</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Activities/games</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>Tips/thank-you gifts</td><td></td><td></td><td></td><td></td></tr></table><p class="small"><b>Rule of thumb:</b> Set the budget cap before choosing a venue or activity. A clear cap protects relationships and avoids surprise costs.</p></div><div class="footer"><span>Wedding Mini-Milestones Planner Kit</span><span>4</span></div></section>
<section class="page"><div class="content"><div class="kicker">Timeline</div><h2>Mini-Event Timeline</h2><table><tr><th>Time</th><th>Moment</th><th>Owner</th><th>Supplies</th><th>Notes</th></tr><tr><td></td><td>Setup begins</td><td></td><td></td><td></td></tr><tr><td></td><td>Food/drinks ready</td><td></td><td></td><td></td></tr><tr><td></td><td>Guests arrive</td><td></td><td></td><td></td></tr><tr><td></td><td>Welcome/toast</td><td></td><td></td><td></td></tr><tr><td></td><td>Main activity/meal</td><td></td><td></td><td></td></tr><tr><td></td><td>Photos/gifts/speeches</td><td></td><td></td><td></td></tr><tr><td></td><td>Cleanup handoff</td><td></td><td></td><td></td></tr></table><h2 style="margin-top:22px">Must-not-forget details</h2><div class="line"></div><div class="line"></div><div class="line"></div></div><div class="footer"><span>Wedding Mini-Milestones Planner Kit</span><span>5</span></div></section>
<section class="page"><div class="content"><div class="kicker">Communication</div><h2>Host + Helper Handoff</h2><div class="grid"><div class="card"><b>Who owns the event?</b><div class="line"></div><div class="line"></div></div><div class="card"><b>What is already decided?</b><div class="line"></div><div class="line"></div></div><div class="card"><b>What needs approval?</b><div class="line"></div><div class="line"></div></div><div class="card"><b>What should stay simple?</b><div class="line"></div><div class="line"></div></div></div><p class="small">Use this before handing plans to a parent, friend, wedding party member, or hired coordinator.</p></div><div class="footer"><span>Wedding Mini-Milestones Planner Kit</span><span>6</span></div></section>
<section class="page"><div class="content"><div class="kicker">Prompt pack preview</div><h2>AI-Assisted Planning Prompts</h2><p class="small">Use the included prompt file to turn your rough notes into helpful drafts. Always review for tone, accuracy, and real constraints.</p><div class="card"><b>Checklist prompt</b><p class="small">Create a realistic checklist for our [event]. Date: [date]. Guest count: [number]. Budget: [amount]. Vibe: [vibe]. Include owner, deadline, and notes.</p></div><div class="card"><b>Budget simplifier</b><p class="small">Review this event budget and suggest where to simplify without making guests feel under-cared-for: [paste rows].</p></div><div class="card"><b>Timeline builder</b><p class="small">Turn these details into a minute-by-minute timeline with setup, guest arrival, food, activities, speeches, photos, clean-up, and owner.</p></div></div><div class="footer"><span>Wedding Mini-Milestones Planner Kit</span><span>7</span></div></section>
</body></html>'''
(cf/'wedding-mini-milestones-workbook.html').write_text(html, encoding='utf-8')

listing = """# Etsy Listing Copy

## SEO Title (under 140 chars)
Wedding Mini Milestones Planner Kit, Rehearsal Dinner Bridal Shower Bach Weekend Budget Timeline, Printable + Spreadsheets

## Category
Weddings > Gifts and Mementos > Digital Prints OR Paper & Party Supplies > Paper > Planners & Notebooks > Digital Planners

## Price suggestion
- Launch price: USD $14.99
- INR equivalent shown by Etsy may vary, approx ₹1,250–₹1,350 depending on conversion.

## 13 Etsy Tags
1. wedding planner
2. wedding checklist
3. bridal shower plan
4. rehearsal dinner
5. bach weekend plan
6. wedding budget
7. guest list tracker
8. event timeline
9. printable planner
10. spreadsheet bundle
11. digital download
12. wedding organizer
13. bride planner

## Description
Plan the meaningful celebrations around your wedding day without starting from scratch each time.

This Wedding Mini-Milestones Planner Kit is made for engagement parties, bridal/couple showers, bachelor or bachelorette weekends, rehearsal dinners, ceremony week details, and day-after brunches. It combines a warm printable workbook with practical CSV spreadsheet templates and AI planning prompts so you can assign owners, set budgets, track vendors, and build calm timelines.

### What you receive
- Printable/PDF-ready Wedding Mini-Milestones Workbook
- Mini-milestones checklist CSV
- Mini-event budget tracker CSV
- Vendor/helper contact tracker CSV
- Timeline template CSV
- Notion / Google Sheets / Excel copy instructions
- AI planning prompt pack for checklists, timelines, vendor questions, host messages, and thank-you notes
- Buyer README and personal-use license

### Best for
- Couples planning multiple wedding-adjacent events
- MOHs, best men, parents, and hosts coordinating one celebration
- Brides/grooms who want budget clarity and fewer last-minute texts
- Small weddings, destination wedding weekends, and family-hosted events

### Digital download note
This is a digital product. No physical item will be shipped. After purchase, download the files from your Etsy account and open them on your computer or tablet.

### Software
The PDF/HTML can be opened in a browser or PDF reader. CSV files work with Google Sheets, Excel, Apple Numbers, and Notion import/copy workflows.

## FAQ
**Will I receive a physical planner?**  
No. This is a digital download only.

**Can I edit the files?**  
Yes. The CSV files are editable in spreadsheet tools. The HTML source can be opened in a browser and printed.

**Can I use this for a client?**  
Personal use only for one household/couple/wedding planning team. Please contact the shop for commercial/event-planner licensing.

**Do I need paid software?**  
No. You can use free tools such as Google Sheets and a browser.

**Can I share it with my wedding party?**  
You may share working copies with people directly helping plan your own wedding events, but the files may not be redistributed or resold.
"""
(base/'listing.md').write_text(listing, encoding='utf-8')

marketing = """# Marketing Copy

## Pinterest Pins
1. Title: Wedding Mini-Milestones Planner Kit  
   Description: Plan your engagement party, bridal shower, bach weekend, rehearsal dinner, and day-after brunch with one printable + spreadsheet wedding event planning bundle.

2. Title: Wedding Event Budget Tracker for Every Mini Celebration  
   Description: Keep showers, rehearsal dinners, brunches, and bach weekends calm with budget CSVs, timelines, vendor trackers, and printable worksheets.

3. Title: Not Just the Wedding Day — Plan the Moments Around It  
   Description: A warm heirloom-style planner kit for the smaller wedding milestones families still need to coordinate.

## Social Posts
1. Instagram/X: The wedding day has a planner — but what about the shower, bach weekend, rehearsal dinner, and brunch? Today’s kit helps couples coordinate every mini-milestone without endless group texts.

2. LinkedIn/X: New HeirloomPlanners launch: a Wedding Mini-Milestones Planner Kit combining printable worksheets, spreadsheet trackers, and AI prompts for practical event coordination.

3. Instagram: For the bride, groom, MOH, parent, or friend who suddenly owns “just one small event” — this kit turns mini-milestones into clear budgets, timelines, and task handoffs.

## Short launch message
New in HeirloomPlanners: the Wedding Mini-Milestones Planner Kit — a printable + spreadsheet bundle for engagement parties, showers, bach weekends, rehearsal dinners, ceremony week details, and day-after brunches. Digital download only.
"""
(base/'marketing.md').write_text(marketing, encoding='utf-8')

competitor = """# Competitor & Demand Notes — 2026-05-16

## Source limitations
- Etsy public search and the logged-in shop dashboard were accessible.
- YouTube search result snippets were accessible; comments were not deeply inspected in this run.
- Google-indexed Reddit/Pinterest search snippets were accessible; direct Reddit thread content may vary by login/region.

## Shop snapshot
- HeirloomPlanners public shop: 1 active listing, 0 sales, no reviews, new shop.
- Existing listing: Wedding Planner Dashboard | Budget, Guests, Tasks, Vendors (Digital Download), shown around ₹3,435.
- Dashboard trust tasks: Customize shop 2/5 complete. Missing banner, shop story, and seller photo.
- Etsy Shop Advisor prompt: “Say ‘I do’ to wedding shoppers,” plus a resource on wedding “ministones.”

## Etsy signals
- Etsy search for “wedding ministones planner digital download” returned ~914 results.
- Visible related filters included Guest List, Seating Chart, Dashboard, Checklist, Timeline, HTML App, iPad, PDF, and Canva.
- Competitor examples included interactive wedding dashboards and spreadsheets priced from roughly ₹444 sale price to ₹1,585+, with some high-review spreadsheet competitors showing 10k+ reviews.
- Saturation is high for generic “all-in-one wedding planner,” so this kit narrows into the under-served mini-events around the wedding.

## YouTube signals
- Search for 2026 Etsy digital product/planner templates surfaced recent “profitable/unsaturated digital products” videos with 30k–38k views within months.
- Creator language emphasizes profitable, unsaturated, beginner-friendly digital products; the actionable takeaway is to package outcome-specific templates instead of generic printable pages.

## Reddit/search signals
- Google-indexed r/weddingplanning results repeatedly mention guest list templates, ultimate wedding planning Google Sheets, wedding spreadsheet templates, and 30-page workbook-style planning sheets.
- Repeated pain point: couples want shareable spreadsheets/checklists because wedding coordination is fragmented across guests, budgets, timelines, and helpers.

## Pinterest/search signals
- Google results show large 2026 Pinterest boards for wedding planner printables, wedding planner digital products, and wedding planner templates.
- Visual trend fit: warm printable aesthetics and pin-friendly checklists should work well for Pinterest traffic.

## Why this can sell
Generic wedding dashboards compete head-on with huge shops. This product extends the current wedding niche while targeting a more specific buyer problem: the wedding-adjacent events that cause budget creep and family coordination stress. It supports a $14.99 launch price because it includes workbook pages, spreadsheet trackers, Notion instructions, and AI prompts rather than a single low-ticket printable.
"""
(base/'competitor_notes.md').write_text(competitor, encoding='utf-8')

# Clean SVG listing-image fallbacks
svg_template = '''<svg xmlns="http://www.w3.org/2000/svg" width="2000" height="1600" viewBox="0 0 2000 1600"><defs><linearGradient id="g" x1="0" x2="1"><stop stop-color="#fbf5ea"/><stop offset="1" stop-color="#eef3e8"/></linearGradient></defs><rect width="2000" height="1600" fill="url(#g)"/><rect x="110" y="100" width="1780" height="1400" rx="44" fill="#fffaf0" stroke="#c8a45d" stroke-width="6"/><circle cx="1660" cy="310" r="150" fill="#8fa58a" opacity=".22"/><circle cx="360" cy="1240" r="180" fill="#c8a45d" opacity=".16"/><text x="180" y="240" font-family="Arial, sans-serif" font-size="40" letter-spacing="8" fill="#8fa58a">HEIRLOOMPLANNERS</text><text x="180" y="390" font-family="Georgia, serif" font-size="92" fill="#314034">{title}</text><text x="180" y="500" font-family="Arial, sans-serif" font-size="42" fill="#4e5a4f">{subtitle}</text>{body}<text x="180" y="1410" font-family="Arial, sans-serif" font-size="34" fill="#6d6a5e">Digital download • Printable + spreadsheets • No physical item shipped</text></svg>'''
body1 = '<rect x="180" y="640" width="520" height="520" rx="28" fill="#fbf5ea" stroke="#c8a45d"/><rect x="760" y="640" width="520" height="520" rx="28" fill="#eef3e8" stroke="#8fa58a"/><rect x="1340" y="640" width="360" height="520" rx="28" fill="#fbf5ea" stroke="#c8a45d"/><text x="235" y="750" font-family="Arial" font-size="40" fill="#314034">Workbook</text><text x="815" y="750" font-family="Arial" font-size="40" fill="#314034">Budgets</text><text x="1390" y="750" font-family="Arial" font-size="40" fill="#314034">Prompts</text><text x="235" y="830" font-family="Arial" font-size="30" fill="#6d6a5e">Mini-events\nTimeline\nHandoffs</text>'
(mock/'01-cover.svg').write_text(svg_template.format(title='Wedding Mini-Milestones', subtitle='Planner Kit for the celebrations around the big day', body=body1), encoding='utf-8')
body2 = ''.join([f'<rect x="{180+(i%3)*560}" y="{610+(i//3)*210}" width="500" height="150" rx="22" fill="{("#eef3e8" if i%2 else "#fbf5ea")}" stroke="#c8a45d"/><text x="{220+(i%3)*560}" y="{700+(i//3)*210}" font-family="Arial" font-size="34" fill="#314034">{txt}</text>' for i,txt in enumerate(['Printable workbook','Checklist CSV','Budget tracker','Vendor contacts','Timeline CSV','AI prompt pack'])])
(mock/'02-bundle-overview.svg').write_text(svg_template.format(title='What is Included', subtitle='A multi-file system for practical wedding coordination', body=body2), encoding='utf-8')
body3 = '<text x="220" y="680" font-family="Arial" font-size="46" fill="#314034">1. Print the workbook pages you need</text><text x="220" y="820" font-family="Arial" font-size="46" fill="#314034">2. Import CSV trackers into Sheets or Notion</text><text x="220" y="960" font-family="Arial" font-size="46" fill="#314034">3. Use prompts for timelines, messages, and vendor questions</text><text x="220" y="1100" font-family="Arial" font-size="46" fill="#314034">4. Share working copies with your planning helpers</text>'
(mock/'03-how-it-works.svg').write_text(svg_template.format(title='How It Works', subtitle='Simple enough for family hosts, structured enough for busy couples', body=body3), encoding='utf-8')

# package selected customer files (PDF added later if generated)
def build_zip():
    zpath = base/'wedding-mini-milestones-kit-customer-files.zip'
    with zipfile.ZipFile(zpath, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(cf.iterdir()):
            if p.is_file(): z.write(p, arcname=p.name)
    with zipfile.ZipFile(zpath) as z:
        bad = z.testzip()
        contents = z.namelist()
    (base/'zip_contents.txt').write_text('\n'.join(contents)+('\nBAD: '+str(bad) if bad else '\nZIP integrity: OK\n'), encoding='utf-8')
    return zpath
build_zip()
print(base)

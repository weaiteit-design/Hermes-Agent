from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import csv, shutil, textwrap, json, os

root = Path('/root/Hermes-Agent/etsy-products/2026-05-17-adhd-student-deadline-rescue-kit')
(root/'csv').mkdir(parents=True, exist_ok=True)
(root/'images').mkdir(exist_ok=True)

README = '''# ADHD Student Deadline Rescue Kit

Thank you for your purchase! This is a digital download designed to help students turn messy syllabi, assignments, readings, and exam dates into one calm weekly action system.

## What is included

- `adhd-student-deadline-rescue-workbook.pdf` — ready-to-print US Letter workbook.
- `adhd-student-deadline-rescue-workbook.html` — editable/printable source file you can open in a browser.
- `notion-copy-template.md` — copy/paste template for Notion or any notes app.
- `student-email-templates.md` — polite templates for professor/TA messages, extensions, clarification, and group work.
- `prompt-pack.md` — optional AI prompts for turning syllabi into checklists, study plans, and weekly priorities.
- `csv/` — spreadsheet-ready trackers for Google Sheets, Excel, Numbers, Airtable, or Notion import.
- `images/` — reference images showing the kit layout.

## How to use

1. Open the PDF and print the pages you need, or open the HTML file in your browser and choose Print / Save as PDF.
2. Import the CSV files into Google Sheets, Excel, Numbers, Airtable, or Notion.
3. Copy the Notion template into your workspace if you prefer a digital dashboard.
4. Start with the Syllabus Capture page, then move dates into the Master Deadline Tracker and Weekly Rescue Plan.

## Compatibility

- PDF reader for the printable workbook.
- Any modern browser for the HTML workbook.
- CSV-compatible spreadsheet app for trackers.
- Notion is optional; no paid software is required.

## Important note

This product is an organization and study-planning tool. It is not medical, mental-health, legal, or academic advice and does not diagnose, treat, or guarantee outcomes. No physical item will be shipped.

## License

Personal use for one buyer/student. You may print or duplicate pages for your own use. Please do not resell, redistribute, share publicly, or upload these files as your own product.
'''
(root/'README.md').write_text(README, encoding='utf-8')

listing = '''# Etsy Listing Copy

## SEO title (137/140 chars)
ADHD Student Planner Bundle, Deadline Tracker, Assignment Tracker, Study Planner, Syllabus Organizer, Printable + Notion + Sheets

## Category
Paper & Party Supplies > Paper > Calendars & Planners OR Digital Prints > Calendars & Planners (choose the closest Etsy digital planner/template category available).

## Suggested price
- Launch price: $12.99 USD (about ₹1,085 INR before local pricing/taxes)
- After first reviews/traction: test $14.99–$17.99

## 13 Etsy tags
1. adhd student planner
2. deadline tracker
3. assignment tracker
4. study planner
5. syllabus organizer
6. student printable
7. college planner
8. notion student
9. google sheets
10. exam planner
11. homework tracker
12. digital planner
13. school template

## Description

A calm, practical deadline rescue system for students who need one place to collect syllabus dates, assignments, readings, exams, weekly priorities, and professor messages.

This digital bundle includes printable pages, spreadsheet CSV trackers, a copy/paste Notion-style template, student email templates, and optional AI prompts to help turn class information into a weekly action plan.

Designed with a warm heirloom paper aesthetic and a simple layout that focuses on clarity rather than clutter.

### What you receive
- Ready-to-print US Letter PDF workbook
- Editable/printable HTML workbook source
- CSV trackers for spreadsheet import
- Notion copy template in Markdown
- Student email templates
- Optional prompt pack for planning support
- Quick-start instructions and personal-use license

### Great for
- College, university, and high-school students
- Students managing multiple syllabi and deadlines
- Weekly study planning
- Assignment and exam countdowns
- Organizing readings, projects, and group work

### Digital download note
This is a digital download. No physical item will be shipped. Your files are delivered as a ZIP download after purchase.

### Compatibility
PDF reader, modern browser, and CSV-compatible spreadsheet app. Notion is optional. No paid app is required.

### Important disclaimer
This is an organization and study-planning product only. It is not medical, mental-health, legal, or academic advice and does not guarantee grades, performance, or outcomes.

## FAQ

**Is this a physical planner?**  
No. This is a digital download only. No physical item is shipped.

**Can I use it without Notion?**  
Yes. The PDF, HTML, and CSV files can be used without Notion.

**Can I edit the files?**  
You can copy/edit the Markdown template and spreadsheet CSVs after importing them into your preferred app. The PDF is designed for printing/writing.

**What size is the printable workbook?**  
US Letter, portrait orientation. It can usually be scaled by your printer settings for A4 if needed.

**Can I resell or share it?**  
No. This purchase is for personal use by one buyer/student.
'''
(root/'listing.md').write_text(listing, encoding='utf-8')

marketing = '''# Marketing Assets

## Pinterest pin ideas
1. Title: “The Deadline Rescue Kit for Students Who Hate Messy Syllabi”  
   Description: Printable + spreadsheet + Notion-friendly student planning bundle for assignments, exams, readings, and weekly study sprints.

2. Title: “Turn Every Class Syllabus Into One Calm Tracker”  
   Description: A warm, simple student planner system with deadline tracker, exam countdown, study sprint pages, and email templates.

3. Title: “ADHD-Friendly Student Planning Without the Clutter”  
   Description: Digital download planner kit for organizing school deadlines, class tasks, readings, and professor messages.

## Social posts
1. New in HeirloomPlanners: a student deadline rescue kit for turning syllabi into one calm weekly plan. Includes printables, CSV trackers, Notion copy template, and email templates.
2. If your semester deadlines live in five different places, this kit gives you one capture → sort → weekly plan workflow.
3. Built for students who need practical organization more than pretty-but-unused planner pages: deadlines, assignments, exams, study sprints, and support messages.

## Short launch message
Today’s new product test: an ADHD-friendly Student Deadline Rescue Kit — a practical digital bundle for students managing classes, assignments, readings, exams, and professor communication.
'''
(root/'marketing.md').write_text(marketing, encoding='utf-8')

competitor = '''# Competitor and Market Notes

## Source limitations
Etsy Shop Manager/browser CDP was unavailable in this autonomous run, so no live dashboard metrics, messages, orders, reviews, or Etsy advisor prompts could be verified today. Public search access was partially available via DuckDuckGo snippets and general marketplace/search reasoning.

## Signals observed
- DuckDuckGo snippets surfaced multiple Etsy results for ADHD student planners, ADHD academic planners, Goodnotes planners, digital student planners, and neurodivergent/executive-function student planners.
- Reddit/search snippets show recurring demand language around ADHD-friendly templates, GoodNotes templates, student tracking templates, and “life spreadsheet” organization systems.
- Current shop tracker shows HeirloomPlanners has only 1 active listing and incomplete trust assets, so catalog depth and trust remain primary bottlenecks.

## Why this can sell
- Buyer pain is urgent and recurring: syllabi, multiple classes, missed deadlines, exams, group work, readings, and professor communication.
- The product is outcome-specific (“deadline rescue”) rather than a generic student planner.
- It combines printable, spreadsheet, and Notion-copy formats without relying on paid software.
- It avoids medical claims: positioned as organization support, not treatment.

## Niche experiment record
- Niche: student/ADHD-friendly productivity systems.
- Buyer persona: college/high-school students who feel overwhelmed by multiple class deadlines and want a simple rescue workflow.
- Keywords: ADHD student planner, deadline tracker, assignment tracker, syllabus organizer, study planner, college planner, Notion student, Google Sheets.
- Product type: PDF + HTML + CSV + Markdown bundle.
- Price test: $12.99 launch; raise to $14.99–$17.99 if views/favorites/sales appear.
- Expected signal: Etsy views/favorites on student/ADHD/planner keywords within 7–14 days after listing, plus any buyer messages asking about formats.
- Next action if promising: create “Exam Week Rescue Kit,” “Syllabus-to-Semester Google Sheets Dashboard,” and “Student Email Template Pack.”
'''
(root/'competitor_notes.md').write_text(competitor, encoding='utf-8')

notion = '''# ADHD Student Deadline Rescue Kit — Notion Copy Template

## Semester Command Center

### Quick Capture Inbox
- [ ] New assignment / reading / admin task:
- Class:
- Due date:
- Estimated effort:
- Next tiny action:

### Master Deadline Tracker
| Due Date | Class | Task | Type | Effort | Status | Next Action | Notes |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | Example 101 | Chapter 2 notes | Reading | 45 min | Not started | Open textbook | |

### Weekly Rescue Plan
**Week of:**  
**Top 3 deadlines:**  
1. 
2. 
3. 

**Study sprints:**
| Day | Sprint | Task | Time Block | Done |
|---|---|---|---|---|
| Monday | 1 | | | [ ] |

### Exam Countdown
| Exam | Date | Topics | First Review | Practice Test | Final Review |
|---|---|---|---|---|---|

### Professor / TA Messages
Copy templates from `student-email-templates.md` and customize them for your class.
'''
(root/'notion-copy-template.md').write_text(notion, encoding='utf-8')

emails = '''# Student Email Templates

## Ask for clarification
Subject: Quick clarification on [assignment name]

Hi Professor/TA [Name],

I’m working on [assignment name] and wanted to clarify [specific question]. I checked [syllabus/rubric/notes], but I want to make sure I’m approaching it correctly.

Thank you,
[Your Name]

## Request an extension respectfully
Subject: Extension request for [assignment name]

Hi Professor [Name],

I’m writing to ask whether a short extension might be possible for [assignment name], currently due [date]. I have completed [specific progress] and can submit by [proposed date/time].

I understand if this is not possible and appreciate your consideration.

Thank you,
[Your Name]

## Group project check-in
Subject: Group project check-in for [project]

Hi everyone,

Can we confirm who is handling each part of the project before [date]? Here is what I have so far:
- My part:
- Still needed:
- Suggested next meeting/check-in:

Thanks!
[Your Name]
'''
(root/'student-email-templates.md').write_text(emails, encoding='utf-8')

prompts = '''# Optional AI Prompt Pack

Use these prompts only with information you are comfortable sharing. Remove private details first.

## Turn a syllabus into deadlines
I am a student. Extract all deadlines, exams, readings, projects, and recurring tasks from the syllabus text below. Return a table with date, class, task, type, estimated effort, and first next action. Do not invent dates. Syllabus text: [paste]

## Build a weekly rescue plan
Here is my deadline tracker for the next two weeks: [paste]. Create a realistic weekly plan with no more than 3 priority tasks per day, short study sprints, and buffer time.

## Break an assignment into tiny steps
Break this assignment into tiny next actions that each take 10–25 minutes. Include a suggested order and a “minimum viable submission” checklist. Assignment: [paste]

## Draft a professor email
Draft a polite, concise email to my professor/TA asking [clarification/extension/meeting]. Keep it respectful, specific, and not over-explained. Context: [paste]
'''
(root/'prompt-pack.md').write_text(prompts, encoding='utf-8')

# CSV files
csvs = {
 '01_syllabus_capture.csv': ['Class,Instructor,Contact,Office Hours,Key Links,Grading Notes,Recurring Tasks,Notes'],
 '02_master_deadline_tracker.csv': ['Due Date,Class,Task,Type,Estimated Effort,Priority,Status,Next Tiny Action,Notes'],
 '03_weekly_rescue_plan.csv': ['Week Of,Day,Top Priority,Study Sprint 1,Study Sprint 2,Admin Task,Done,Notes'],
 '04_exam_countdown.csv': ['Exam,Class,Date,Topics,First Review Date,Practice Questions Date,Final Review Date,Status,Notes'],
 '05_reading_lab_tracker.csv': ['Due Date,Class,Reading or Lab,Pages/Scope,Required Output,Estimated Time,Status,Notes'],
 '06_professor_message_log.csv': ['Date,Class,Person,Reason,Message Sent,Follow Up Date,Status,Notes'],
}
for name, rows in csvs.items():
    (root/'csv'/name).write_text('\n'.join(rows)+'\n', encoding='utf-8')

html = '''<!doctype html>
<html><head><meta charset="utf-8"><title>ADHD Student Deadline Rescue Workbook</title>
<style>
@page { size: Letter; margin: 0.55in; }
body { font-family: Georgia, 'Times New Roman', serif; color:#2f3328; background:#fbf7ed; }
.page { page-break-after: always; background:#fffdf7; border:1px solid #d8c79b; padding:24px; min-height:9.2in; box-sizing:border-box; }
h1 { color:#50624d; font-size:28px; margin:0 0 8px; }
h2 { color:#50624d; font-size:20px; border-bottom:2px solid #d8c79b; padding-bottom:5px; }
.small { color:#6e715f; font-size:12px; }
table { width:100%; border-collapse:collapse; margin:12px 0; font-size:12px; }
th { background:#e8ead8; color:#394333; }
th,td { border:1px solid #cfc4a3; padding:7px; vertical-align:top; height:22px; }
.box { border:1px solid #cfc4a3; min-height:52px; margin:8px 0; padding:8px; background:#fffaf0; }
.grid { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.badge { display:inline-block; background:#d8c79b; padding:5px 10px; border-radius:12px; font-size:12px; }
</style></head><body>
<div class="page"><h1>ADHD Student Deadline Rescue Kit</h1><p class="small">Printable workbook • US Letter • Personal use digital download</p><p>A calm workflow for collecting class information, sorting urgent deadlines, and turning school chaos into a weekly action plan.</p><div class="grid"><div class="box"><strong>Step 1:</strong> Capture every syllabus date.</div><div class="box"><strong>Step 2:</strong> Choose the next tiny action.</div><div class="box"><strong>Step 3:</strong> Plan short study sprints.</div><div class="box"><strong>Step 4:</strong> Review weekly and reset.</div></div><p class="small">Organization support only. Not medical, mental-health, or academic advice.</p></div>
<div class="page"><h2>Syllabus Capture</h2><table><tr><th>Class</th><th>Instructor</th><th>Contact</th><th>Office Hours</th></tr>''' + ''.join('<tr><td></td><td></td><td></td><td></td></tr>' for _ in range(8)) + '''</table><h2>Recurring Tasks</h2><div class="box"></div><div class="box"></div></div>
<div class="page"><h2>Master Deadline Tracker</h2><table><tr><th>Due Date</th><th>Class</th><th>Task</th><th>Type</th><th>Effort</th><th>Next Tiny Action</th><th>Status</th></tr>''' + ''.join('<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for _ in range(14)) + '''</table></div>
<div class="page"><h2>Weekly Rescue Plan</h2><p><span class="badge">Week of: __________</span></p><div class="grid"><div class="box"><strong>Top 3 deadlines</strong><br>1.<br>2.<br>3.</div><div class="box"><strong>Must-send messages</strong><br>□<br>□<br>□</div></div><table><tr><th>Day</th><th>Study Sprint 1</th><th>Study Sprint 2</th><th>Admin Task</th><th>Done</th></tr>''' + ''.join(f'<tr><td>{d}</td><td></td><td></td><td></td><td>□</td></tr>' for d in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']) + '''</table></div>
<div class="page"><h2>Assignment Breakdown</h2><div class="box"><strong>Assignment:</strong></div><table><tr><th>Tiny Step</th><th>Estimated Time</th><th>First Action</th><th>Done</th></tr>''' + ''.join('<tr><td></td><td></td><td></td><td>□</td></tr>' for _ in range(10)) + '''</table><h2>Minimum Viable Submission Checklist</h2><div class="box">□ Requirements checked<br>□ Sources/materials ready<br>□ Draft complete<br>□ Submitted before deadline</div></div>
<div class="page"><h2>Exam Countdown</h2><table><tr><th>Exam</th><th>Date</th><th>Topics</th><th>First Review</th><th>Practice</th><th>Final Review</th></tr>''' + ''.join('<tr><td></td><td></td><td></td><td></td><td></td><td></td></tr>' for _ in range(8)) + '''</table></div>
<div class="page"><h2>Professor / TA Message Planner</h2><table><tr><th>Class</th><th>Person</th><th>Reason</th><th>Draft Notes</th><th>Sent?</th><th>Follow Up</th></tr>''' + ''.join('<tr><td></td><td></td><td></td><td></td><td>□</td><td></td></tr>' for _ in range(8)) + '''</table></div>
</body></html>'''
(root/'adhd-student-deadline-rescue-workbook.html').write_text(html, encoding='utf-8')

# Simple SVG fallback listing images
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1200" viewBox="0 0 1600 1200"><rect width="1600" height="1200" fill="#fbf7ed"/><rect x="90" y="90" width="1420" height="1020" rx="34" fill="#fffdf7" stroke="#d8c79b" stroke-width="8"/><text x="150" y="210" font-family="Georgia" font-size="72" fill="#50624d">ADHD Student</text><text x="150" y="295" font-family="Georgia" font-size="72" fill="#50624d">Deadline Rescue Kit</text><text x="155" y="365" font-family="Arial" font-size="34" fill="#6e715f">Printable workbook • CSV trackers • Notion copy template</text><rect x="150" y="455" width="520" height="430" rx="18" fill="#f6eddc" stroke="#cfc4a3"/><text x="190" y="530" font-family="Arial" font-size="34" fill="#394333">Weekly Rescue Plan</text><line x1="190" y1="590" x2="620" y2="590" stroke="#cfc4a3" stroke-width="4"/><line x1="190" y1="655" x2="620" y2="655" stroke="#cfc4a3" stroke-width="4"/><line x1="190" y1="720" x2="620" y2="720" stroke="#cfc4a3" stroke-width="4"/><rect x="740" y="455" width="700" height="430" rx="18" fill="#e8ead8" stroke="#50624d" stroke-width="5"/><text x="790" y="530" font-family="Arial" font-size="34" fill="#394333">Deadline Tracker Dashboard</text><rect x="790" y="590" width="600" height="54" fill="#fffdf7"/><rect x="790" y="675" width="600" height="54" fill="#fffdf7"/><rect x="790" y="760" width="600" height="54" fill="#fffdf7"/><text x="150" y="980" font-family="Arial" font-size="36" fill="#50624d">Turn syllabus chaos into one calm weekly plan</text></svg>'''
(root/'images'/'listing-image-fallback-cover.svg').write_text(svg, encoding='utf-8')

# Copy generated images if present
image_sources = [
('/root/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260517_033318_61a3d63f.png','01-cover-openai.png'),
('/root/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260517_033416_1e4f3494.png','02-bundle-overview-openai.png'),
('/root/.hermes/cache/images/openai_codex_gpt-image-2-medium_20260517_033524_a31cf9df.png','03-how-it-works-openai.png'),
]
for src, dest in image_sources:
    p=Path(src)
    if p.exists(): shutil.copy2(p, root/'images'/dest)

# PDF via reportlab fallback
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    pdf_path = root/'adhd-student-deadline-rescue-workbook.pdf'
    doc=SimpleDocTemplate(str(pdf_path), pagesize=letter, rightMargin=0.55*inch,leftMargin=0.55*inch, topMargin=0.55*inch,bottomMargin=0.55*inch)
    styles=getSampleStyleSheet(); styles.add(ParagraphStyle(name='SageTitle', parent=styles['Title'], textColor=colors.HexColor('#50624d')))
    story=[Paragraph('ADHD Student Deadline Rescue Kit', styles['SageTitle']), Paragraph('Printable US Letter workbook for organizing syllabi, deadlines, assignments, exams, study sprints, and professor messages.', styles['BodyText']), Spacer(1,12)]
    sections=[('Syllabus Capture',['Class','Instructor','Contact','Office Hours']),('Master Deadline Tracker',['Due Date','Class','Task','Type','Effort','Next Tiny Action','Status']),('Weekly Rescue Plan',['Day','Study Sprint 1','Study Sprint 2','Admin Task','Done']),('Assignment Breakdown',['Tiny Step','Estimated Time','First Action','Done']),('Exam Countdown',['Exam','Date','Topics','First Review','Practice','Final Review']),('Professor / TA Message Planner',['Class','Person','Reason','Draft Notes','Sent?','Follow Up'])]
    for title, headers in sections:
        story.append(PageBreak()); story.append(Paragraph(title, styles['Heading1']))
        data=[headers]+[['' for _ in headers] for _ in range(10)]
        t=Table(data, repeatRows=1)
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e8ead8')),('TEXTCOLOR',(0,0),(-1,0),colors.HexColor('#394333')),('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#cfc4a3')),('VALIGN',(0,0),(-1,-1),'TOP'),('FONTSIZE',(0,0),(-1,-1),7),('ROWHEIGHT',(0,1),(-1,-1),24)]))
        story.append(t)
    doc.build(story)
except Exception as e:
    (root/'PDF_FALLBACK_ERROR.txt').write_text(str(e), encoding='utf-8')

# Create customer ZIP: buyer-facing only
zip_path = root/'adhd-student-deadline-rescue-kit-customer-files.zip'
include = ['README.md','adhd-student-deadline-rescue-workbook.html','notion-copy-template.md','student-email-templates.md','prompt-pack.md']
if (root/'adhd-student-deadline-rescue-workbook.pdf').exists(): include.insert(1,'adhd-student-deadline-rescue-workbook.pdf')
include += [str(p.relative_to(root)) for p in sorted((root/'csv').glob('*.csv'))]
include += [str(p.relative_to(root)) for p in sorted((root/'images').glob('*'))]
with ZipFile(zip_path,'w',ZIP_DEFLATED) as z:
    for rel in include:
        z.write(root/rel, arcname=rel)
with ZipFile(zip_path) as z:
    bad=z.testzip()
    if bad: raise RuntimeError(f'Bad zip member: {bad}')
    names=z.namelist()
(root/'zip_manifest.txt').write_text('\n'.join(names)+'\n', encoding='utf-8')
print('BUILT', root)
print('ZIP', zip_path)
print('\n'.join(names))

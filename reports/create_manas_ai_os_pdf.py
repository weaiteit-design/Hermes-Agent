from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    KeepTogether, HRFlowable
)
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfgen import canvas
from pathlib import Path

OUT = Path('/root/Hermes-Agent/reports/Manas_AI_OS_Report.pdf')

PAGE_W, PAGE_H = A4
MARGIN_X = 17 * mm
MARGIN_Y = 16 * mm

BG = colors.HexColor('#08090A')
PANEL = colors.HexColor('#0F1011')
TEXT = colors.HexColor('#F7F8F8')
MUTED = colors.HexColor('#A6ADBB')
SOFT = colors.HexColor('#707782')
ACCENT = colors.HexColor('#7C82FF')
BLUE = colors.HexColor('#2997FF')
GREEN = colors.HexColor('#42D392')
GOLD = colors.HexColor('#F6C46B')
ROSE = colors.HexColor('#FF8BA7')
PAPER = colors.HexColor('#F6F5F4')
INK = colors.HexColor('#1D1D1F')
LINE = colors.Color(1,1,1, alpha=.13)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name='CoverKicker', fontName='Helvetica-Bold', fontSize=9, leading=12,
    textColor=colors.HexColor('#D9DCFF'), uppercase=True, spaceAfter=10,
))
styles.add(ParagraphStyle(
    name='CoverTitle', fontName='Helvetica-Bold', fontSize=43, leading=42,
    textColor=TEXT, spaceAfter=16, alignment=TA_LEFT,
))
styles.add(ParagraphStyle(
    name='CoverSub', fontName='Helvetica', fontSize=13.5, leading=20,
    textColor=MUTED, spaceAfter=18,
))
styles.add(ParagraphStyle(
    name='Kicker', fontName='Helvetica-Bold', fontSize=8.5, leading=10,
    textColor=ACCENT, spaceBefore=2, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name='H1x', fontName='Helvetica-Bold', fontSize=27, leading=30,
    textColor=TEXT, spaceAfter=12,
))
styles.add(ParagraphStyle(
    name='H2x', fontName='Helvetica-Bold', fontSize=18, leading=21,
    textColor=TEXT, spaceBefore=4, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name='H3x', fontName='Helvetica-Bold', fontSize=13, leading=16,
    textColor=TEXT, spaceAfter=4,
))
styles.add(ParagraphStyle(
    name='Bodyx', fontName='Helvetica', fontSize=9.7, leading=14,
    textColor=MUTED, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name='BodyWhite', fontName='Helvetica', fontSize=10.2, leading=15,
    textColor=TEXT, spaceAfter=7,
))
styles.add(ParagraphStyle(
    name='Small', fontName='Helvetica', fontSize=8.3, leading=11,
    textColor=MUTED,
))
styles.add(ParagraphStyle(
    name='Mono', fontName='Courier', fontSize=8, leading=11,
    textColor=colors.HexColor('#D0D6E0'),
))
styles.add(ParagraphStyle(
    name='LightH', fontName='Helvetica-Bold', fontSize=18, leading=21,
    textColor=INK, spaceAfter=6,
))
styles.add(ParagraphStyle(
    name='LightBody', fontName='Helvetica', fontSize=9.5, leading=13.5,
    textColor=colors.HexColor('#615D59'), spaceAfter=5,
))


def P(txt, style='Bodyx'):
    return Paragraph(txt, styles[style])


def bullet(items, color=MUTED):
    out=[]
    for item in items:
        out.append(Paragraph(f'• {item}', ParagraphStyle('b'+str(abs(hash(item))), parent=styles['Bodyx'], leftIndent=8, firstLineIndent=-8, textColor=color, spaceAfter=3)))
    return out


def card(title, body, tag=None, bullets=None):
    data=[]
    inner=[]
    if tag:
        inner.append(Paragraph(tag.upper(), ParagraphStyle('tag', fontName='Helvetica-Bold', fontSize=7, leading=9, textColor=colors.HexColor('#D9DCFF'), spaceAfter=7)))
    inner.append(P(title, 'H3x'))
    inner.append(P(body, 'Bodyx'))
    if bullets:
        inner += bullet(bullets)
    data.append([inner])
    t=Table(data, colWidths='*')
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), colors.HexColor('#121417')),
        ('BOX',(0,0),(-1,-1), .6, colors.HexColor('#2B2D33')),
        ('TOPPADDING',(0,0),(-1,-1), 12),('BOTTOMPADDING',(0,0),(-1,-1), 12),
        ('LEFTPADDING',(0,0),(-1,-1), 12),('RIGHTPADDING',(0,0),(-1,-1), 12),
        ('VALIGN',(0,0),(-1,-1),'TOP'),
    ]))
    return t


def two_col(left, right, gap=8*mm):
    t=Table([[left, right]], colWidths=[(PAGE_W-2*MARGIN_X-gap)/2, (PAGE_W-2*MARGIN_X-gap)/2])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    return t


def three_col(items):
    w=(PAGE_W-2*MARGIN_X-8*mm)/3
    t=Table([items], colWidths=[w,w,w])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    return t


def section(kicker, title, body=None):
    els=[P(kicker.upper(), 'Kicker'), P(title, 'H1x')]
    if body: els.append(P(body, 'Bodyx'))
    return els

class ThemedDoc(SimpleDocTemplate):
    pass


def draw_bg(c: canvas.Canvas, doc):
    c.saveState()
    c.setFillColor(BG)
    c.rect(0,0,PAGE_W,PAGE_H, stroke=0, fill=1)
    # subtle orbs
    c.setFillColor(colors.Color(.49,.51,1, alpha=.13)); c.circle(40*mm, PAGE_H-32*mm, 54*mm, stroke=0, fill=1)
    c.setFillColor(colors.Color(.16,.59,1, alpha=.08)); c.circle(PAGE_W-28*mm, PAGE_H-12*mm, 42*mm, stroke=0, fill=1)
    c.setFillColor(colors.Color(.26,.83,.57, alpha=.05)); c.circle(PAGE_W/2, 12*mm, 70*mm, stroke=0, fill=1)
    # footer
    c.setStrokeColor(colors.HexColor('#24262B')); c.setLineWidth(.5)
    c.line(MARGIN_X, 11*mm, PAGE_W-MARGIN_X, 11*mm)
    c.setFillColor(SOFT); c.setFont('Helvetica', 7.5)
    c.drawString(MARGIN_X, 6.5*mm, 'Manas AI OS · Two-Device Automation Report')
    c.drawRightString(PAGE_W-MARGIN_X, 6.5*mm, str(doc.page))
    c.restoreState()


def draw_cover(c, doc):
    draw_bg(c, doc)
    c.saveState()
    # mark
    c.setFillColor(colors.HexColor('#7C82FF')); c.roundRect(MARGIN_X, PAGE_H-42*mm, 13*mm, 13*mm, 4*mm, stroke=0, fill=1)
    c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 11); c.drawCentredString(MARGIN_X+6.5*mm, PAGE_H-38.8*mm, 'M')
    c.setFillColor(TEXT); c.setFont('Helvetica-Bold', 13); c.drawString(MARGIN_X+17*mm, PAGE_H-38.8*mm, 'Manas AI OS')
    # visual device blocks
    x=PAGE_W-78*mm; y=PAGE_H-135*mm
    c.setFillColor(colors.Color(1,1,1, alpha=.06)); c.roundRect(x, y, 55*mm, 78*mm, 7*mm, stroke=0, fill=1)
    c.setStrokeColor(colors.Color(1,1,1, alpha=.13)); c.roundRect(x, y, 55*mm, 78*mm, 7*mm, stroke=1, fill=0)
    c.setFillColor(colors.Color(.49,.51,1, alpha=.13)); c.roundRect(x+7*mm, y+49*mm, 41*mm, 18*mm, 4*mm, stroke=0, fill=1)
    c.setFillColor(colors.Color(.26,.83,.57, alpha=.12)); c.roundRect(x+7*mm, y+23*mm, 41*mm, 18*mm, 4*mm, stroke=0, fill=1)
    c.setFillColor(MUTED); c.setFont('Helvetica', 7.5); c.drawString(x+7*mm,y+13*mm,'Always-on ops + builder cockpit')
    c.restoreState()

story=[]
# Cover
story += [Spacer(1, 58*mm), P('PERSONAL AI OPERATING SYSTEM REPORT', 'CoverKicker'), P('Turn two MacBooks into a one-person AI studio.', 'CoverTitle'), P('A structured plan for using your old M2 Air and future M5 Pro MacBook as an always-on AI life, work, app, content, and wealth automation system.', 'CoverSub')]
story.append(Spacer(1, 8*mm))
story.append(Table([[P('<b>New MacBook Pro M5 Pro</b><br/>Builder cockpit · apps · code · creative · Higgsfield · Magnific', 'BodyWhite'), P('<b>Old MacBook Air M2</b><br/>Always-on Hermes operator · cron agents · monitoring · reminders', 'BodyWhite')]], colWidths=[75*mm,75*mm], style=[('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#121417')),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#2B2D33')),('INNERGRID',(0,0),(-1,-1),.4,colors.HexColor('#2B2D33')),('PADDING',(0,0),(-1,-1),12),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(PageBreak())

# Executive summary
story += section('01 / Executive Summary', 'The strategy: split your machines by job.', 'The upgrade becomes powerful when the new MacBook handles deep creation and the old MacBook runs your always-on AI operations layer.')
story.append(two_col(
    card('M5 Pro MacBook', 'High-performance production machine for building, editing, coding, creative output and app launches.', 'CREATE', ['Claude Code, Codex, Xcode, VS Code/Cursor', 'Higgsfield motion, Magnific upscales, OpenAI creative', 'Clearmeds, WiseAI and new app experiments']),
    card('M2 Air', 'Low-friction always-on operations server that watches, summarizes, reminds and coordinates.', 'OPERATE', ['Hermes gateway and Telegram assistant', 'n8n, Uptime Kuma, cron jobs and browser automation', 'Daily briefs, stock watch, client and app trackers'])
))
story.append(Spacer(1, 8*mm))
story.append(card('Core principle', 'Your system should not create more noise. Every automation must produce a useful output: message, file, task, report, alert, draft, commit, dashboard update or decision prompt.', 'RULE'))
story.append(PageBreak())

# Stack
story += section('02 / Core Stack', 'Give every tool one clean role.', 'This prevents tool overload and turns your subscriptions into a coordinated operating system.')
story.append(three_col([
    card('Hermes', 'Command layer for memory, Telegram, cron jobs, reports, reminders, subagents and automation control.', 'OPS'),
    card('Claude', 'Deep reasoning and coding partner for architecture, strategy, debugging, reviews and high-quality writing.', 'THINK'),
    card('OpenAI', 'Creative and multimodal engine for ideation, image generation, copy, mockups and fast variations.', 'CREATE')
]))
story.append(Spacer(1, 6*mm))
story.append(three_col([
    card('GitHub', 'Permanent source of truth for apps, automations, prompts, docs, workflows and agent-readable context.', 'MEMORY'),
    card('Higgsfield', 'Cinematic motion layer for app demos, founder videos, ad concepts and social-first creative tests.', 'MOTION'),
    card('Magnific', 'Premium polish layer for upscaling visuals, thumbnails, ad assets and high-quality delivery material.', 'POLISH')
]))
story.append(PageBreak())

# AI departments
story += section('03 / AI Departments', 'Run agents like departments, not random chats.', 'Hermes coordinates the departments. Claude and Codex execute. GitHub stores the durable memory.')
deps=[
 ['Chief of Staff','Morning brief, nightly review, task prioritization, reminders and weekly review.'],
 ['App Studio Agent','Tracks Clearmeds, WiseAI, app ideas, validation tests and launch checklists.'],
 ['Growth Agent','Drafts X posts, launch copy, ad concepts, landing page ideas and content calendars.'],
 ['Investing Research Agent','Monitors AI, semiconductors, nuclear, political signals and major news catalysts.'],
 ['Client Ops Agent','Tracks leads, follow-ups, proposals, deliverables, invoices and AiteitAI offers.'],
 ['Knowledge Agent','Maintains notes, learnings, prompts, reusable procedures and personal memory.'],
]
rows=[]
for i,(a,b) in enumerate(deps,1):
    rows.append([Paragraph(f'{i:02d}', ParagraphStyle('n', fontName='Helvetica-Bold', fontSize=19, textColor=ACCENT)), P(f'<b>{a}</b><br/>{b}', 'Bodyx')])
t=Table(rows, colWidths=[16*mm, PAGE_W-2*MARGIN_X-16*mm], rowHeights=None)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#121417')),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#2B2D33')),('INNERGRID',(0,0),(-1,-1),.35,colors.HexColor('#252830')),('PADDING',(0,0),(-1,-1),9),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)
story.append(PageBreak())

# Automation suite
story += section('04 / Automation Suite', 'Build systems that improve money, focus and shipping.', 'Start with the systems below. They are ordered by leverage and practicality.')
autos=[
 ['Morning CEO Brief','Top 3 priorities, schedule, market watch, app/client alerts, one ask from you.','Hermes Cron','High'],
 ['Nightly Accountability','Work done, blockers, slipped tasks and tomorrow’s focus.','Hermes Cron','High'],
 ['AI App Studio Dashboard','App ideas, validation status, signals, next action and kill/continue decision.','GitHub + Notion/Sheets','High'],
 ['Stock Intelligence Agent','AI, semis, nuclear, Trump/media/deal signals and actionability.','Hermes + Web','Medium'],
 ['Content Engine','Personal manas_builds drafts from actual work and lessons.','Hermes + Claude/OpenAI','High'],
 ['Client Follow-up Agent','Follow-ups, proposals, delivery and payment reminders.','n8n + Sheets/Notion','High'],
 ['Uptime Monitor','Alerts if Clearmeds/WiseAI/AiteitAI sites or APIs go down.','Uptime Kuma','Medium'],
 ['GitHub Sync','Daily redacted workspace summary and durable docs backup.','Hermes + GitHub','Medium'],
]
t=Table([[Paragraph('<b>System</b>',styles['Small']),Paragraph('<b>What it does</b>',styles['Small']),Paragraph('<b>Tool</b>',styles['Small']),Paragraph('<b>Priority</b>',styles['Small'])]]+[[P(a,'Small'),P(b,'Small'),P(c,'Small'),P(d,'Small')] for a,b,c,d in autos], colWidths=[38*mm,72*mm,33*mm,22*mm])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1A1C22')),('BACKGROUND',(0,1),(-1,-1),colors.HexColor('#111317')),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#2B2D33')),('INNERGRID',(0,0),(-1,-1),.35,colors.HexColor('#252830')),('PADDING',(0,0),(-1,-1),7),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)
story.append(PageBreak())

# Roadmap
story += section('05 / 30-Day Roadmap', 'Build the operating system in layers.', 'Do not automate everything at once. Foundation first, then money workflows, then app studio, then creative and investing intelligence.')
for i,(title,body) in enumerate([
 ('Week 1: Foundation','Create the Manas AI OS repo, set up old M2 Air as always-on Hermes machine, enable daily briefs and nightly reviews.'),
 ('Week 2: Money & Workflows','Set up net worth tracker, AiteitAI lead tracker, client follow-ups, proposal templates and content draft system.'),
 ('Week 3: App Studio','Create dashboards and CLAUDE.md files for Clearmeds, WiseAI and new app experiments. Track validation, not just building.'),
 ('Week 4: Creative & Investing Layer','Add Higgsfield/Magnific creative pipeline, stock intelligence, weekly review and launch-readiness checklists.'),
],1):
    story.append(Table([[Paragraph(f'{i:02d}', ParagraphStyle('rn', fontName='Helvetica-Bold', fontSize=16, textColor=GOLD)), P(f'<b>{title}</b><br/>{body}', 'Bodyx')]], colWidths=[15*mm, PAGE_W-2*MARGIN_X-15*mm], style=[('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#121417')),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#2B2D33')),('PADDING',(0,0),(-1,-1),10),('VALIGN',(0,0),(-1,-1),'TOP')]))
    story.append(Spacer(1,4*mm))
story.append(PageBreak())

# Repo
story += section('06 / Source of Truth', 'Create one repo for your life OS.', 'This repo stores plans, dashboards, prompts, automation notes and reusable procedures.')
repo='''manas-ai-os/\n├── README.md\n├── LIFE_DASHBOARD.md\n├── NET_WORTH.md\n├── DAILY_REVIEW.md\n├── WEEKLY_REVIEW.md\n├── APP_STUDIO.md\n├── AITEITAI_PIPELINE.md\n├── STOCK_WATCHLIST.md\n├── CONTENT_IDEAS.md\n├── CLAUDE.md\n├── prompts/\n│   ├── morning-brief.md\n│   ├── nightly-review.md\n│   ├── x-post-drafter.md\n│   ├── stock-signal-review.md\n│   └── app-validation.md\n├── automations/\n│   ├── cron-jobs.md\n│   ├── n8n-flows.md\n│   └── scripts/\n└── dashboards/'''
story.append(Table([[P(repo.replace('\n','<br/>'), 'Mono')]], colWidths=[PAGE_W-2*MARGIN_X], style=[('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#111317')),('BOX',(0,0),(-1,-1),.6,colors.HexColor('#2B2D33')),('PADDING',(0,0),(-1,-1),12)]))
story.append(Spacer(1, 8*mm))
story.append(two_col(card('No auto-posting', 'Hermes drafts content and messages. You approve before anything public goes out.', 'SAFETY'), card('No auto-trading', 'Stock agents summarize signals and risk. You make final decisions before any trade.', 'SAFETY')))
story.append(Spacer(1, 5*mm))
story.append(two_col(card('GitHub is memory', 'If it matters, it belongs in a repo: plans, prompts, app docs, workflows and dashboards.', 'SYSTEM'), card('Weekly cleanup', 'Every Sunday, review subscriptions, dead app ideas, dashboards, net worth and next week’s focus.', 'SYSTEM')))
story.append(PageBreak())

# Closing
story += [Spacer(1, 48*mm), P('FINAL DIRECTION', 'CoverKicker'), P('Operate like a small AI-native studio.', 'CoverTitle'), P('Your old M2 Air becomes the always-on operator. Your new M5 Pro becomes the builder machine. Hermes is the command layer. Claude is the deep builder. OpenAI is the creative engine. Higgsfield and Magnific make the output look premium. GitHub stores the system.', 'CoverSub')]
story.append(card('Immediate next action', 'Start with the foundation: create the Manas AI OS repo and set up the first five Hermes scheduled jobs: morning brief, nightly review, weekly review, stock watch and app studio status.', 'NEXT'))

OUT.parent.mkdir(parents=True, exist_ok=True)
doc=ThemedDoc(str(OUT), pagesize=A4, rightMargin=MARGIN_X, leftMargin=MARGIN_X, topMargin=MARGIN_Y, bottomMargin=16*mm)
doc.build(story, onFirstPage=draw_cover, onLaterPages=draw_bg)
print(OUT)
print(OUT.stat().st_size)

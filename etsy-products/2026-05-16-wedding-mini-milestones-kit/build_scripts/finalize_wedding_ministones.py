from pathlib import Path
import zipfile, csv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

base=Path('/root/Hermes-Agent/etsy-products/2026-05-16-wedding-mini-milestones-kit')
cf=base/'customer_files'
pdf=cf/'wedding-mini-milestones-workbook.pdf'
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='SageTitle', parent=styles['Title'], fontSize=26, leading=31, textColor=colors.HexColor('#314034'), spaceAfter=16))
styles.add(ParagraphStyle(name='Kicker', parent=styles['Normal'], fontSize=9, leading=12, textColor=colors.HexColor('#8fa58a'), uppercase=True, spaceAfter=8))
styles.add(ParagraphStyle(name='BodyBig', parent=styles['BodyText'], fontSize=12, leading=17, spaceAfter=10))
styles.add(ParagraphStyle(name='H2Sage', parent=styles['Heading2'], fontSize=17, leading=21, textColor=colors.HexColor('#314034'), spaceBefore=12, spaceAfter=8))

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor('#fbf5ea'))
    canvas.rect(0,0,letter[0],letter[1],fill=1,stroke=0)
    canvas.setStrokeColor(colors.HexColor('#c8a45d'))
    canvas.setLineWidth(1)
    canvas.rect(.25*inch,.25*inch,letter[0]-.5*inch,letter[1]-.5*inch,fill=0,stroke=1)
    canvas.setFillColor(colors.HexColor('#6d6a5e'))
    canvas.setFont('Helvetica',8)
    canvas.drawString(.55*inch,.35*inch,'HeirloomPlanners • Wedding Mini-Milestones Planner Kit')
    canvas.drawRightString(letter[0]-.55*inch,.35*inch,str(doc.page))
    canvas.restoreState()

story=[]
story += [Paragraph('HEIRLOOMPLANNERS', styles['Kicker']), Paragraph('Wedding Mini-Milestones Planner Kit', styles['SageTitle']), Paragraph('A calm, practical planning system for the meaningful events around the wedding: engagement party, shower, bachelor/bachelorette weekend, rehearsal dinner, ceremony week, and day-after brunch.', styles['BodyBig']), Spacer(1,.15*inch)]
for item in ['Printable workbook','Budget CSVs','Timeline templates','AI prompts','No physical item shipped']:
    story.append(Paragraph('• '+item, styles['BodyBig']))
story.append(PageBreak())
story += [Paragraph('Mini-Milestone Map', styles['SageTitle'])]
for name,desc in [('Engagement Party','Host, guest count, casual budget, invitations, food plan, photo moment.'),('Shower','Host handoff, registry note, games/favors, thank-you workflow.'),('Bach Weekend','Transparent cost split, safety contacts, itinerary, payments.'),('Rehearsal Dinner','Venue, menu, speeches, seating, final family logistics.'),('Ceremony Week','Payments, rings, license, packing, emergency kit, contacts.'),('Day-After Brunch','Simple hosting, leftover logistics, family goodbyes, cleanup.')]:
    story += [Paragraph(name, styles['H2Sage']), Paragraph(desc, styles['BodyBig'])]
story.append(PageBreak())
story += [Paragraph('Event Snapshot', styles['SageTitle'])]
table_data=[['Event','Date/time','Host/owner','Guest count','Budget cap'],['Engagement party','','','',''],['Shower','','','',''],['Bach weekend','','','',''],['Rehearsal dinner','','','',''],['Day-after brunch','','','','']]
t=Table(table_data, colWidths=[1.55*inch,1.15*inch,1.35*inch,1*inch,1*inch], rowHeights=.42*inch)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#8fa58a')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#d7c79d')),('BACKGROUND',(0,1),(-1,-1),colors.HexColor('#fffaf0')),('FONT',(0,0),(-1,-1),'Helvetica'),('FONTSIZE',(0,0),(-1,-1),9)]))
story.append(t); story.append(Spacer(1,.3*inch)); story.append(Paragraph('Top decisions this week', styles['H2Sage']))
for _ in range(7): story.append(Paragraph('____________________________________________________________', styles['BodyBig']))
story.append(PageBreak())
story += [Paragraph('Budget + Timeline Worksheets', styles['SageTitle'])]
for heading, rows in [('Mini-Event Budget',[['Event','Category','Planned','Actual','Paid by','Due'],['','Venue/host','','','',''],['','Food + drinks','','','',''],['','Invites/decor','','','',''],['','Tips/gifts','','','','']]),('Timeline',[['Time','Moment','Owner','Supplies','Notes'],['','Setup begins','','',''],['','Guests arrive','','',''],['','Welcome/toast','','',''],['','Main activity/meal','','',''],['','Cleanup handoff','','','']])]:
    story.append(Paragraph(heading, styles['H2Sage']))
    tt=Table(rows, colWidths=[.9*inch,1.65*inch,1*inch,1.35*inch,1.35*inch], rowHeights=.38*inch)
    tt.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#8fa58a')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#d7c79d')),('BACKGROUND',(0,1),(-1,-1),colors.HexColor('#fffaf0')),('FONT',(0,0),(-1,-1),'Helvetica'),('FONTSIZE',(0,0),(-1,-1),8)]))
    story.append(tt); story.append(Spacer(1,.2*inch))
story.append(PageBreak())
story += [Paragraph('AI-Assisted Planning Prompts', styles['SageTitle']), Paragraph('Use the included prompt file to turn rough notes into draft checklists, vendor questions, messages, and timelines. Always review for accuracy and tone.', styles['BodyBig'])]
for p in ['Create a realistic checklist for our [event]. Date: [date]. Guest count: [number]. Budget: [amount]. Vibe: [vibe]. Include owner, deadline, and notes.', 'Review this event budget and suggest where to simplify without making guests feel under-cared-for: [paste rows].', 'Turn these event details into a minute-by-minute timeline with setup, guest arrival, food, activities, speeches, photos, clean-up, and owner.', 'Draft a warm message asking [person] for help with [task]. Tone: grateful, clear, not demanding.']:
    story.append(Paragraph('• '+p, styles['BodyBig']))

doc=SimpleDocTemplate(str(pdf), pagesize=letter, leftMargin=.65*inch, rightMargin=.65*inch, topMargin=.65*inch, bottomMargin=.65*inch)
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)

zpath=base/'wedding-mini-milestones-kit-customer-files.zip'
with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(cf.iterdir()):
        if p.is_file(): z.write(p, arcname=p.name)
with zipfile.ZipFile(zpath) as z:
    bad=z.testzip(); contents=z.namelist()
(base/'zip_contents.txt').write_text('\n'.join(contents)+('\nZIP integrity: OK\n' if bad is None else '\nBAD: '+str(bad)+'\n'), encoding='utf-8')
print('PDF', pdf, pdf.stat().st_size)
print('ZIP', zpath, zpath.stat().st_size)
print('\n'.join(contents))

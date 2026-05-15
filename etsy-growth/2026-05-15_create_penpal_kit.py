import os, csv, json, zipfile, textwrap, math
from datetime import date
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch, mm
from reportlab.pdfbase.pdfmetrics import stringWidth

BASE = '/root/Hermes-Agent/etsy-growth/2026-05-15'
ASSETS = os.path.join(BASE, 'assets')
PRODUCT = os.path.join(BASE, 'product_files')
os.makedirs(ASSETS, exist_ok=True)
os.makedirs(PRODUCT, exist_ok=True)

PALETTE = {
    'cream': '#FFF8EC', 'blush': '#F7CACA', 'rose': '#D9777D', 'ink': '#2F2A32',
    'sage': '#A8BFA3', 'sky': '#BFD7EA', 'mustard': '#E8B45B', 'lavender': '#C9B7D9'
}

def font(size=36, bold=False):
    paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf'
    ]
    for p in paths:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def wrap_draw(draw, text, xy, fnt, fill, max_width, line_gap=8):
    x,y=xy
    words=text.split()
    line=''
    for w in words:
        test=(line+' '+w).strip()
        if draw.textbbox((0,0), test, font=fnt)[2] <= max_width:
            line=test
        else:
            draw.text((x,y), line, font=fnt, fill=fill)
            y += fnt.size + line_gap
            line=w
    if line:
        draw.text((x,y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y

def draw_flower(draw, cx, cy, s, color, center='#E8B45B'):
    for ang in range(0,360,60):
        dx=math.cos(math.radians(ang))*s*.65; dy=math.sin(math.radians(ang))*s*.65
        draw.ellipse([cx+dx-s*.45, cy+dy-s*.45, cx+dx+s*.45, cy+dy+s*.45], fill=color)
    draw.ellipse([cx-s*.35, cy-s*.35, cx+s*.35, cy+s*.35], fill=center)

def make_listing_images():
    W,H=2000,1600
    specs=[
        ('listing_image_1.png','Printable Pen Pal Letter Writing Kit','Stationery, envelopes, tracker, prompts and Notion-style dashboard', ['12 writing papers','2 envelope templates','60 prompt cards','Snail mail tracker']),
        ('listing_image_2.png','What is included','Ready-to-print files for cozy snail mail lovers', ['A4 + US Letter PDFs','CSV trackers','Notion import markdown','Printing guide']),
        ('listing_image_3.png','Pen Pal Tracker','Keep addresses, birthdays, last reply dates and gift ideas organized', ['Contacts','Mail log','Birthday reminders','Response status']),
        ('listing_image_4.png','60 Letter Prompt Cards','Never stare at a blank page again', ['First letters','Deep questions','Seasonal notes','Long-distance friendship']),
        ('listing_image_5.png','Instant Digital Download','Print at home or use digitally in GoodNotes/Notion', ['No physical item','Beginner friendly','Neutral cozy style','Personal use'])
    ]
    for fname,title,subtitle,bullets in specs:
        im=Image.new('RGB',(W,H),PALETTE['cream']); d=ImageDraw.Draw(im)
        # background shapes
        d.rounded_rectangle([80,80,W-80,H-80], radius=60, fill='#FFFFFF', outline=PALETTE['rose'], width=6)
        d.rectangle([0,0,W,180], fill=PALETTE['blush'])
        for i,(cx,cy,c) in enumerate([(240,300,PALETTE['rose']),(1740,260,PALETTE['lavender']),(1800,1320,PALETTE['sage']),(220,1320,PALETTE['mustard'])]):
            draw_flower(d,cx,cy,70,c)
        d.text((150,130), 'SNAIL MAIL STUDIO', font=font(38,True), fill=PALETTE['ink'])
        d.text((150,310), title, font=font(96,True), fill=PALETTE['ink'])
        wrap_draw(d, subtitle, (155,445), font(48), PALETTE['rose'], 1500, 12)
        # mock paper stack
        x0,y0=1060,650
        d.rounded_rectangle([x0+90,y0+70,x0+620,y0+690], radius=30, fill='#F3E6FF', outline=PALETTE['lavender'], width=5)
        d.rounded_rectangle([x0+45,y0+35,x0+575,y0+655], radius=30, fill='#EAF4E7', outline=PALETTE['sage'], width=5)
        d.rounded_rectangle([x0,y0,x0+530,y0+620], radius=30, fill='#FFFDF8', outline=PALETTE['rose'], width=5)
        for yy in range(y0+125,y0+500,55): d.line([x0+70,yy,x0+460,yy], fill='#EBC9C9', width=3)
        d.text((x0+70,y0+55),'Dear friend,',font=font(34,True),fill=PALETTE['rose'])
        # bullets
        bx,by=180,670
        for b in bullets:
            d.ellipse([bx,by+8,bx+32,by+40], fill=PALETTE['sage'])
            d.text((bx+55,by), b, font=font(52,True), fill=PALETTE['ink'])
            by += 105
        d.rounded_rectangle([150,1380,780,1480], radius=45, fill=PALETTE['ink'])
        d.text((205,1402),'PRINTABLE PDF + CSV',font=font(42,True),fill='white')
        im.save(os.path.join(ASSETS,fname), quality=95)

stationery_themes = [
    ('Blush Florals', '#F7CACA', '#D9777D'), ('Sage Garden', '#DDEAD8', '#6E8B67'),
    ('Blue Air Mail', '#DDEEF8', '#4C7EA6'), ('Lavender Notes', '#EEE4F6', '#8C6AA8'),
    ('Warm Vintage', '#FFF0D1', '#B97B34'), ('Strawberry Cream', '#FFE1E1', '#C94C5A'),
    ('Minimal Lines', '#F7F5EF', '#55515C'), ('Sunny Daisy', '#FFF5C8', '#D5A122'),
    ('Moonlit Letter', '#E9EAF7', '#4A4F87'), ('Tea Time', '#EFE0CF', '#8A654A'),
    ('Bookish Brown', '#F3E8DA', '#755C48'), ('Weekend Postcard', '#E5F2EF', '#4E8A7A')]

prompts = [
'What made you smile this week?', 'Describe your perfect slow Sunday.', 'What book, song, or film feels like home right now?',
'Tell me about a tiny tradition you want to keep.', 'What is one local spot you wish I could visit with you?', 'What are three things currently on your desk?',
'Write a mini travel guide for your city.', 'What is a childhood snack you still love?', 'What did you learn the hard way recently?',
'What is your current creative obsession?', 'Send a recipe you can make without thinking.', 'What do you want the next season to feel like?',
'List five small joys from today.', 'What is one question you wish people asked more often?', 'Describe your favorite morning sound.',
'What are you trying to simplify?', 'What is the best compliment you received lately?', 'Share a memory attached to a scent.',
'What is a goal you are quietly working on?', 'If we swapped weekends, what should I do first?', 'What is in your bag right now?',
'Write a playlist in words, not links.', 'What is a belief you changed your mind about?', 'Describe a photo you did not take but remember.',
'What do you collect, even accidentally?', 'What is a tiny luxury you recommend?', 'What is your favorite handwritten note you ever received?',
'What is your comfort meal?', 'Tell me about a person who shaped your taste.', 'What is your current weather and mood?',
'What are you grateful for that feels ordinary?', 'What is a place you miss?', 'Write three predictions for your next month.',
'What would your ideal care package include?', 'What is a skill you want to learn slowly?', 'Describe your favorite corner of your home.',
'What is a quote you keep returning to?', 'What is a family saying or inside joke?', 'What have you been procrastinating and why?',
'What is something you noticed on a walk?', 'What is your favorite way to celebrate small wins?', 'What would you put in a time capsule today?',
'What is one thing you want to remember about this year?', 'Tell me about your favorite mug or cup.', 'What is a simple kindness someone did for you?',
'What does friendship mean to you this season?', 'What are your current top three colors?', 'Write a tiny poem about today.',
'What are you looking forward to?', 'What is the best advice you ignored?', 'What should I know before visiting your town?',
'What is something you do when you need courage?', 'What is your favorite old-fashioned habit?', 'What is a souvenir you kept?',
'What is a question for my next letter?', 'What has surprised you lately?', 'Describe a dream dinner party guest list.',
'What is a seasonal bucket list item?', 'What is a word you love?', 'What is one promise you want to make to yourself?']

def pdf_header(c, w, h, title, accent):
    c.setFillColor(colors.HexColor(PALETTE['cream'])); c.rect(0,0,w,h,stroke=0,fill=1)
    c.setFillColor(colors.HexColor(accent)); c.rect(0,h-42,w,42,stroke=0,fill=1)
    c.setFillColor(colors.HexColor(PALETTE['ink'])); c.setFont('Helvetica-Bold',16); c.drawString(36,h-28,title)

def create_kit_pdf(path, pagesize):
    c=canvas.Canvas(path, pagesize=pagesize); w,h=pagesize
    for name,bg,accent in stationery_themes:
        c.setFillColor(colors.HexColor(bg)); c.rect(0,0,w,h,stroke=0,fill=1)
        c.setStrokeColor(colors.HexColor(accent)); c.setLineWidth(1.2)
        c.roundRect(36,36,w-72,h-72,12,stroke=1,fill=0)
        c.setFillColor(colors.HexColor(accent)); c.setFont('Helvetica-Bold',18); c.drawString(54,h-64,'Dear friend,')
        y=h-110
        c.setStrokeColor(colors.HexColor('#D8B6B6'))
        while y>80:
            c.line(60,y,w-60,y); y-=28
        c.setFont('Helvetica',9); c.setFillColor(colors.HexColor(PALETTE['ink'])); c.drawRightString(w-54,50,name)
        c.showPage()
    # envelope templates
    for size_name in ['A2 envelope template', 'DL envelope template']:
        pdf_header(c,w,h,size_name,PALETTE['blush'])
        c.setStrokeColor(colors.HexColor(PALETTE['rose'])); c.setLineWidth(2)
        x,y=w*.18,h*.30; ew,eh=w*.64,h*.34
        c.roundRect(x,y,ew,eh,8,stroke=1,fill=0)
        c.line(x,y+eh,x+ew/2,y+eh+90); c.line(x+ew,y+eh,x+ew/2,y+eh+90)
        c.line(x,y,x+ew/2,y-70); c.line(x+ew,y,x+ew/2,y-70)
        c.line(x,y,x-70,y+eh/2); c.line(x,y+eh,x-70,y+eh/2)
        c.line(x+ew,y,x+ew+70,y+eh/2); c.line(x+ew,y+eh,x+ew+70,y+eh/2)
        c.setFont('Helvetica',12); c.setFillColor(colors.HexColor(PALETTE['ink']))
        c.drawString(54,120,'Cut outside the flaps, fold on the rectangle lines, glue side flaps, then tuck the top flap.')
        c.showPage()
    # tracker pages
    pdf_header(c,w,h,'Pen Pal Address & Birthday Tracker',PALETTE['sage'])
    cols=['Name','Address','Birthday','Interests','Last sent','Last received']
    widths=[.14,.27,.13,.18,.14,.14]
    x=36; y=h-90; row=34
    c.setFont('Helvetica-Bold',9)
    for col,pct in zip(cols,widths): c.drawString(x+4,y+12,col); x+=pct*(w-72)
    c.setFont('Helvetica',9)
    for r in range(14):
        x=36; c.rect(36,y-row*(r+1),w-72,row,stroke=1,fill=0)
        for pct in widths[:-1]: x+=pct*(w-72); c.line(x,y-row*r,x,y-row*(r+1))
    c.showPage()
    pdf_header(c,w,h,'Outgoing & Incoming Mail Log',PALETTE['sky'])
    cols=['Date','To/From','Type','Included','Reply needed','Notes']; widths=[.12,.18,.14,.22,.14,.20]
    x=36; y=h-90; row=32; c.setFont('Helvetica-Bold',9)
    for col,pct in zip(cols,widths): c.drawString(x+4,y+11,col); x+=pct*(w-72)
    c.setFont('Helvetica',9)
    for r in range(16):
        x=36; c.rect(36,y-row*(r+1),w-72,row,stroke=1,fill=0)
        for pct in widths[:-1]: x+=pct*(w-72); c.line(x,y-row*r,x,y-row*(r+1))
    c.showPage()
    # prompt cards
    for page in range(5):
        pdf_header(c,w,h,'Cut-Out Letter Prompt Cards',PALETTE['lavender'])
        c.setStrokeColor(colors.HexColor(PALETTE['rose']))
        cardw=(w-96)/2; cardh=(h-150)/3
        for i in range(6):
            idx=page*6+i
            if idx>=len(prompts): break
            cx=36+(i%2)*(cardw+24); cy=h-105-(i//2+1)*cardh-(i//2)*18
            c.setFillColor(colors.white); c.roundRect(cx,cy,cardw,cardh,10,stroke=1,fill=1)
            c.setFillColor(colors.HexColor(PALETTE['rose'])); c.setFont('Helvetica-Bold',11); c.drawString(cx+14,cy+cardh-24,f'Prompt {idx+1}')
            c.setFillColor(colors.HexColor(PALETTE['ink'])); c.setFont('Helvetica',11)
            text=c.beginText(cx+14,cy+cardh-48)
            for line in textwrap.wrap(prompts[idx], 34): text.textLine(line)
            c.drawText(text)
        c.showPage()
    c.save()

def create_printing_guide(path):
    c=canvas.Canvas(path, pagesize=letter); w,h=letter
    pdf_header(c,w,h,'Printing Guide and License',PALETTE['mustard'])
    c.setFillColor(colors.HexColor(PALETTE['ink']))
    c.setFont('Helvetica-Bold',18); c.drawString(54,h-95,'How to use your Pen Pal Letter Writing Kit')
    c.setFont('Helvetica',12)
    lines=[
        '1. Choose the A4 or US Letter PDF based on your paper size.',
        '2. Print stationery pages at 100% scale. Use borderless printing if your printer supports it.',
        '3. For envelope templates, print on cardstock or thicker paper, cut outside the flaps and fold on the guide lines.',
        '4. Import the CSV tracker into Google Sheets, Excel, Airtable or Notion.',
        '5. Use the Notion markdown file as a simple copy/paste dashboard structure.',
        '6. Personal use and gift use are included. Do not resell, redistribute or claim the files as your own.',
        'No physical item is shipped. Colors may vary slightly by screen and printer.'
    ]
    y=h-130
    for ln in lines:
        for part in textwrap.wrap(ln, 85): c.drawString(54,y,part); y-=20
        y-=8
    c.save()

def make_csvs():
    with open(os.path.join(PRODUCT,'Snail_Mail_Tracker.csv'),'w',newline='') as f:
        writer=csv.writer(f); writer.writerow(['Name','Mailing Address','Birthday','Interests','Favorite Colors','Last Sent','Last Received','Reply Needed','Gift Ideas','Notes'])
        for _ in range(20): writer.writerow(['','','','','','','','','',''])
    with open(os.path.join(PRODUCT,'Pen_Pal_Prompt_Cards.csv'),'w',newline='') as f:
        writer=csv.writer(f); writer.writerow(['Number','Prompt','Category'])
        for i,p in enumerate(prompts,1):
            cat=['Getting to know you','Cozy life','Deep questions','Seasonal','Creative'][i%5]
            writer.writerow([i,p,cat])

def write_text_files():
    notion='''# Pen Pal Snail Mail Dashboard\n\n## Pen Pals\n| Name | Address | Birthday | Interests | Favorite colors | Last sent | Last received | Reply needed | Gift ideas | Notes |\n|---|---|---|---|---|---|---|---|---|---|\n| Example Friend | 123 Main St | Jan 1 | books, tea | sage, blush | 2026-05-01 | 2026-05-10 | Yes | bookmark | Add personal notes here |\n\n## Mail Log\n| Date | To/From | Direction | Type | Included | Follow up |\n|---|---|---|---|---|---|\n| 2026-05-15 | Example Friend | Outgoing | Letter | prompt card, tea bag | Wait for reply |\n\n## Monthly Snail Mail Ritual\n- Pick 2 friends to write.\n- Choose 1 prompt card.\n- Add a tiny flat surprise if desired.\n- Log date sent.\n- Set a reminder to reply within 7 days after receiving mail.\n\n## Favorite Letter Prompts\n- What made you smile this week?\n- What do you want the next season to feel like?\n- What is one local spot you wish I could visit with you?\n'''
    open(os.path.join(PRODUCT,'Notion_Snail_Mail_Dashboard.md'),'w').write(notion)
    readme='''# Printable Pen Pal Letter Writing Kit\n\nA cozy digital snail mail bundle created for the 2026 resurgence of pen pal letters and digital detox hobbies.\n\n## Included\n- Pen_Pal_Letter_Writing_Kit_A4.pdf\n- Pen_Pal_Letter_Writing_Kit_US_Letter.pdf\n- Printing_Guide_and_License.pdf\n- Snail_Mail_Tracker.csv\n- Pen_Pal_Prompt_Cards.csv\n- Notion_Snail_Mail_Dashboard.md\n\n## Buyer note\nThis is an instant digital download. No physical product is shipped.\n'''
    open(os.path.join(BASE,'README.md'),'w').write(readme)

def write_listing():
    tags=['pen pal kit','letter writing','snail mail','printable stationery','penpal letters','letter paper','envelope template','mail tracker','notion tracker','prompt cards','digital download','stationery pdf','friendship gift']
    title='Pen Pal Letter Writing Kit, Printable Stationery, Snail Mail Tracker, Prompt Cards, Envelope Template, Notion Dashboard Digital Download'
    desc='''Bring back cozy handwritten letters with this printable Pen Pal Letter Writing Kit. Designed for snail mail lovers, long-distance friends, journaling fans and anyone craving a softer digital detox ritual.\n\nWHAT YOU GET\n• 12 printable stationery designs\n• A4 and US Letter PDF versions\n• 2 printable envelope templates\n• Address and birthday tracker\n• Outgoing/incoming mail log\n• 60 cut-out letter prompt cards\n• CSV tracker for Google Sheets, Excel, Airtable or Notion\n• Notion-style markdown dashboard\n• Printing guide and personal-use license\n\nWHY BUYERS LIKE IT\n• Helps you start a letter when you do not know what to write\n• Keeps pen pal addresses, birthdays and reply dates organized\n• Works as a thoughtful long-distance friendship gift\n• Instant download, print at home or use digitally in GoodNotes/Notion\n\nIMPORTANT\nThis is a digital product. No physical item will be shipped. Colors may vary slightly due to screen and printer settings. For personal use only. Do not resell or redistribute the files.\n'''
    listing=f'''# Etsy Listing Draft\n\nTitle:\n{title}\n\nPrice recommendation: $6.99\n\nCategory: Paper & Party Supplies > Paper > Stationery > Letter Writing Sets\nType: Digital download\n\nDescription:\n{desc}\n\nTags:\n{', '.join(tags)}\n\nMaterials:\nPDF, CSV, Markdown, printable stationery, digital download\n\nFiles to upload:\n- product_files/Pen_Pal_Letter_Writing_Kit_A4.pdf\n- product_files/Pen_Pal_Letter_Writing_Kit_US_Letter.pdf\n- product_files/Printing_Guide_and_License.pdf\n- product_files/Snail_Mail_Tracker.csv\n- product_files/Pen_Pal_Prompt_Cards.csv\n- product_files/Notion_Snail_Mail_Dashboard.md\n\nListing images:\n- assets/listing_image_1.png\n- assets/listing_image_2.png\n- assets/listing_image_3.png\n- assets/listing_image_4.png\n- assets/listing_image_5.png\n'''
    open(os.path.join(BASE,'etsy_listing.md'),'w').write(listing)
    return title,tags

def research_notes():
    content='''# Research Notes, 2026-05-15\n\nChosen niche: printable pen pal letter writing kit with snail mail tracker and prompt cards.\n\nWhy this niche:\n- Pinterest Predicts 2026 includes the “Pen Pals” trend, describing a move toward digital detox and old-fashioned snail mail. Extracted trend searches include “cute stamps”, “penpal letters”, “hand written letters”, “penpal ideas” and “snail mail gifts”. Source: https://business.pinterest.com/pinterest-predicts/\n- This maps cleanly to Etsy digital downloads because buyers can instantly print stationery, envelopes, prompt cards and trackers.\n- The product is differentiated from generic stationery by adding practical organization assets: CSV tracker and Notion-style dashboard.\n- Seasonal/evergreen gift angles: long-distance friendship, back-to-school, care packages, birthdays and slow-living hobbies.\n\nPositioning:\n- Primary buyer: women/teens/college students, journalers, long-distance friends, cozy hobby buyers.\n- Core keywords: pen pal kit, printable stationery, snail mail tracker, penpal letters, letter writing set, envelope template, prompt cards.\n- Pricing target: $5.99 to $7.99 for a multi-file instant download. Recommended launch price: $6.99.\n'''
    open(os.path.join(BASE,'research_notes.md'),'w').write(content)

make_listing_images()
create_kit_pdf(os.path.join(PRODUCT,'Pen_Pal_Letter_Writing_Kit_A4.pdf'), A4)
create_kit_pdf(os.path.join(PRODUCT,'Pen_Pal_Letter_Writing_Kit_US_Letter.pdf'), letter)
create_printing_guide(os.path.join(PRODUCT,'Printing_Guide_and_License.pdf'))
make_csvs(); write_text_files(); title,tags=write_listing(); research_notes()
manifest={
    'date': str(date.today()), 'product':'Printable Pen Pal Letter Writing Kit', 'price':'6.99',
    'title':title, 'tags':tags,
    'files':[os.path.join(dp,f) for dp,_,fs in os.walk(BASE) for f in fs]
}
open(os.path.join(BASE,'manifest.json'),'w').write(json.dumps(manifest,indent=2))
zip_path=os.path.join(BASE,'Pen_Pal_Letter_Writing_Kit.zip')
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for root,dirs,files in os.walk(PRODUCT):
        for f in files:
            p=os.path.join(root,f); z.write(p, os.path.relpath(p, PRODUCT))
print(json.dumps({'base':BASE,'zip':zip_path,'file_count':sum(len(fs) for _,_,fs in os.walk(BASE))}, indent=2))

#!/usr/bin/env python3
"""Manas OS Dashboard: simple chat, subscription usage, animated agent office."""
import http.server, socketserver, subprocess, json, urllib.parse, os, re, time, html, threading, mimetypes
from pathlib import Path

ROOT = Path('/root/Hermes-Agent')
ASSET_ROOT = ROOT / 'vendor' / 'pixel-agents' / 'webview-ui' / 'public'
TOKEN_FILE = ROOT / 'logs' / 'manas-dashboard-token.txt'
TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
if TOKEN_FILE.exists():
    TOKEN = TOKEN_FILE.read_text().strip()
else:
    import secrets
    TOKEN = secrets.token_urlsafe(18)
    TOKEN_FILE.write_text(TOKEN)

PORT = int(os.environ.get('MANAS_DASHBOARD_PORT', '9120'))
BOARD = os.environ.get('HERMES_KANBAN_BOARD', 'manas-os')
CHAT_LOCK = threading.Lock()

def run(cmd, timeout=20):
    try:
        p = subprocess.run(cmd, shell=True, text=True, capture_output=True, timeout=timeout, cwd=str(ROOT))
        return {'ok': p.returncode == 0, 'out': (p.stdout + p.stderr).strip(), 'code': p.returncode}
    except subprocess.TimeoutExpired as e:
        return {'ok': False, 'out': f'Timed out after {timeout}s', 'code': 124}
    except Exception as e:
        return {'ok': False, 'out': repr(e), 'code': 1}

def parse_insights(text):
    data = {'raw': text[-5000:]}
    patterns = {
        'sessions': r'Sessions:\s+([\d,]+)',
        'messages': r'Messages:\s+([\d,]+)',
        'tool_calls': r'Tool calls:\s+([\d,]+)',
        'input_tokens': r'Input tokens:\s+([\d,]+)',
        'output_tokens': r'Output tokens:\s+([\d,]+)',
        'total_tokens': r'Total tokens:\s+([\d,]+)',
        'active_time': r'Active time:\s+([^\n]+?)\s+Avg session:',
    }
    for k, pat in patterns.items():
        m = re.search(pat, text)
        if m: data[k] = m.group(1).strip()
    models=[]
    in_models=False
    for line in text.splitlines():
        if '🤖 Models Used' in line: in_models=True; continue
        if in_models and ('📱 Platforms' in line or '🔧 Top Tools' in line): break
        m=re.match(r'\s*([A-Za-z0-9._:/-]+)\s+(\d+)\s+([\d,]+)', line)
        if in_models and m:
            models.append({'model':m.group(1),'sessions':m.group(2),'tokens':m.group(3)})
    data['models']=models
    return data

def api_usage():
    insights = run('hermes insights --days 30', 45)['out']
    codex = run('test -f ~/.codex/auth.json && codex --version 2>/dev/null || true', 15)['out']
    codex_status = 'Connected' if 'codex' in codex.lower() else 'Not connected'
    return {
        'local_hermes_usage': parse_insights(insights),
        'subscriptions': [
            {'name':'OpenAI Codex / ChatGPT', 'status':codex_status, 'usage':'Official subscription quota must be checked in the provider UI. Hermes local token usage is shown above.', 'details':codex[-500:]},
            {'name':'Hermes local accounting', 'status':'Available', 'usage':'30-day sessions, messages, tool calls, and token counts from hermes insights.'}
        ]
    }


def api_health():
    cfg = run('python3 -c "import yaml,json,os; d=yaml.safe_load(open(os.path.expanduser(\'~/.hermes/config.yaml\'))) or {}; print(json.dumps(d.get(\'model\',{})))"', 10)['out']
    auth = run('hermes auth list 2>&1 | head -80', 20)['out']
    model = {}
    try:
        model = json.loads(cfg.splitlines()[-1])
    except Exception:
        model = {}
    status = 'ok'
    note = 'provider connected'
    low = auth.lower()
    provider = str(model.get('provider',''))
    if 'rate-limited' in low and provider in ('openai-codex','openai'):
        status = 'blocked'; note = 'OpenAI/Codex rate-limited'
    if provider == 'anthropic' and ('out of extra usage' in low or 'exhausted' in low):
        status = 'blocked'; note = 'Claude usage exhausted'
    return {'model': model, 'status': status, 'note': note}

def api_agents():
    assignees = run(f'hermes kanban --board {BOARD} assignees', 20)['out']
    stats = run(f'hermes kanban --board {BOARD} stats', 20)['out']
    tasks = run(f'hermes kanban --board {BOARD} list', 20)['out']
    agents=[]
    for name in ['orchestrator','researcher','builder','reviewer','creative']:
        status='idle'
        # Try to infer status from assignee lines if counts exist.
        for line in assignees.splitlines():
            if line.strip().startswith(name):
                if 'running' in line.lower(): status='working'
                elif 'ready' in line.lower() or 'todo' in line.lower(): status='queued'
                elif 'idle' in line.lower(): status='idle'
        agents.append({'name':name,'status':status})
    return {'board':BOARD,'agents':agents,'assignees_raw':assignees,'stats_raw':stats,'tasks_raw':tasks}

def api_chat(prompt):
    prompt = prompt.strip()[:4000]
    if not prompt:
        return {'reply':'Type a message first.'}
    # Safer: use the main Hermes CLI in non-interactive mode, bounded timeout.
    with CHAT_LOCK:
        quoted = subprocess.list2cmdline(['hermes','chat','-q',prompt,'--source','manas-dashboard'])
        res = run(quoted, 180)
    reply = res['out'] or '(No response)'
    low = reply.lower()
    if 'rate limit' in low or 'rate-limited' in low or 'usage limit' in low or 'out of extra usage' in low or '429' in low:
        reply = 'Provider quota/rate-limit issue. Telegram still works when a provider is available. Exact fix: refresh/add Claude usage or wait for OpenAI/Codex rate limit, then restart Hermes gateway.\n\n' + reply
    return {'reply': reply[-12000:], 'ok': res['ok']}

HTML = r'''<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hermes Agent - Manas OS</title>
<style>
:root{--bg:#041512;--panel:#09211d;--panel2:#0b2a25;--line:#29443e;--txt:#e8fff5;--muted:#91aaa2;--yellow:#f4d000;--orange:#d48658;--green:#4ee08b;--cyan:#6fffee;--blue:#58a6ff;--red:#ff657a}
*{box-sizing:border-box}html,body{height:100%}body{margin:0;background:#031511;color:var(--txt);font-family:"Courier New",ui-monospace,monospace;letter-spacing:.02em;background-image:radial-gradient(circle at 72% 16%,#0d77ff33,transparent 26%),radial-gradient(circle at 45% 42%,#00fff01f,transparent 24%),linear-gradient(90deg,#061b17,#08231f 52%,#061511)}body:before{content:"";position:fixed;inset:0;pointer-events:none;background:linear-gradient(#ffffff05 1px,transparent 1px);background-size:100% 4px;mix-blend-mode:screen;opacity:.36;z-index:20}body:after{content:"";position:fixed;inset:-30%;pointer-events:none;background:conic-gradient(from 0deg,transparent,#6fffee22,transparent,#58a6ff18,transparent);animation:hudspin 18s linear infinite;opacity:.22;z-index:0}@keyframes hudspin{to{transform:rotate(360deg)}}
.app{min-height:100%;display:grid;grid-template-columns:240px 1fr;position:relative;z-index:1}.side{border-right:1px solid #31524a;background:#061b17cc;min-height:100vh;position:sticky;top:0;padding:18px 16px}.logo{font-family:Georgia,serif;font-weight:900;line-height:.85;font-size:18px;margin-bottom:28px;color:#fff4cf}.nav a{display:flex;gap:12px;align-items:center;color:#b6c8c1;text-decoration:none;padding:11px 4px;text-transform:uppercase;font-size:12px;letter-spacing:.16em}.nav a.active,.nav a:hover{color:#fff}.nav a.active{background:#0b2a25;border-left:2px solid var(--yellow);padding-left:8px}.system{position:absolute;left:16px;right:16px;bottom:18px;border-top:1px solid #31524a;padding-top:12px;color:#7f9991;font-size:10px;line-height:1.8;text-transform:uppercase}.status{color:var(--green)}
.main{padding:0 22px 28px}.top{height:54px;border-bottom:1px solid #31524a;display:flex;align-items:center;justify-content:space-between}.top h1{font-size:22px;margin:0;color:#fff;letter-spacing:.08em}.model{border:1px solid #31524a;padding:8px 12px;color:#d5efe6}.health{border:1px solid #8a5d2b;color:#ffd6a3;padding:4px 8px;margin-left:8px;font-size:11px}.live{color:var(--green);border:1px solid #1d8c52;padding:4px 8px;margin-left:12px}.layout{display:grid;grid-template-columns:minmax(720px,1.35fr) minmax(340px,.65fr);gap:16px;margin-top:16px}@media(max-width:1050px){.app{grid-template-columns:1fr}.side{position:relative;min-height:auto}.system{position:static;margin-top:20px}.layout{grid-template-columns:1fr}}
.panel{background:linear-gradient(180deg,#09211de6,#071916e6);border:1px solid #31524a;box-shadow:0 18px 60px #0008, inset 0 0 30px #6fffee08;padding:16px;position:relative}.panel:before{content:"";position:absolute;left:0;top:0;width:42px;height:1px;background:var(--cyan);box-shadow:0 0 14px var(--cyan)}.panel h2{margin:0 0 12px;font-size:14px;color:#fff;text-transform:uppercase;letter-spacing:.16em}.subtle{color:var(--muted);font-size:12px}.hero{border-radius:7px;background:linear-gradient(135deg,#0b2b26,#071b24);padding:16px;border-color:#4b7b83}.hero-title{color:var(--yellow);font-size:13px;margin:0 0 12px}.ascii{font-size:10px;line-height:1;color:var(--yellow);white-space:pre;overflow:hidden}.split{display:grid;grid-template-columns:1fr;gap:14px;align-items:stretch}
/* Real pixel-agents repo assets */
.pa-office{height:372px;position:relative;overflow:hidden;border:1px solid var(--orange);background:#0c201d;image-rendering:pixelated;box-shadow:inset 0 0 0 1px #0b2a25}.office-stage{position:absolute;left:0;top:0;width:720px;height:372px;transform-origin:top left;z-index:2}.pa-office:before{content:"";position:absolute;inset:0 0 150px;background:linear-gradient(180deg,#0c302b,#102b27);border-bottom:3px solid #274940}.pa-office:after{content:"";position:absolute;left:-8%;right:-8%;bottom:-58px;height:66%;background-color:#1d2634;background-image:url('/pixel-assets/assets/floors/floor_7.png');background-size:64px 64px;transform:perspective(610px) rotateX(57deg);transform-origin:bottom;z-index:0;filter:saturate(.85) brightness(.82)}.wall{position:absolute;z-index:1;image-rendering:pixelated}.furn{position:absolute;z-index:4;image-rendering:pixelated;filter:drop-shadow(5px 7px 0 #0007)}.char{position:absolute;z-index:6;width:44px;height:auto;image-rendering:pixelated;filter:drop-shadow(5px 8px 0 #0008);animation:bob 1.4s steps(2,end) infinite}.agent-label{position:absolute;z-index:7;background:#061511;border:1px solid #31524a;color:#d7ece5;font-size:9px;text-transform:uppercase;padding:3px 5px;box-shadow:3px 3px 0 #0008}.badge{color:var(--green)}.work .badge,.working .badge{color:var(--cyan)}.queued .badge{color:var(--yellow)}.pc-on{animation:screenpulse .65s steps(2,end) infinite}.desk-row{position:absolute;z-index:3;height:1px}.books{width:64px}.plant{width:36px}.desk{width:82px}.pc{width:48px}.white{width:120px}.coffee{width:34px}.sofa{width:72px}@keyframes bob{50%{transform:translateY(-3px)}}@keyframes screenpulse{50%{filter:hue-rotate(60deg) brightness(1.3)}}
#a1c{left:78px;top:202px}#a2c{left:205px;top:142px}#a3c{left:325px;top:205px}#a4c{left:500px;top:145px}#a5c{left:585px;top:205px}#a1l{left:45px;top:248px}#a2l{left:174px;top:188px}#a3l{left:288px;top:251px}#a4l{left:463px;top:191px}#a5l{left:540px;top:251px}
.jarvis-strip{display:grid;grid-template-columns:180px 1fr 180px;gap:14px;align-items:center;margin:12px 0 16px;padding:14px;border:1px solid #2d6970;background:linear-gradient(90deg,#061511,#092b31,#061511);box-shadow:inset 0 0 30px #6fffee12}.arc{width:128px;height:128px;border-radius:50%;margin:auto;position:relative;background:radial-gradient(circle,#eaffff 0 8%,#6fffee 9% 12%,#07252b 13% 28%,transparent 29%),conic-gradient(from 0deg,#6fffee,#58a6ff,#f4d000,#6fffee);box-shadow:0 0 28px #6fffee88, inset 0 0 28px #000;animation:pulse 2.4s ease-in-out infinite}.arc:before{content:"";position:absolute;inset:14px;border:2px dashed #bdfcff;border-radius:50%;animation:hudspin 9s linear infinite}.arc:after{content:"JARVIS";position:absolute;inset:0;display:grid;place-items:center;font-size:11px;color:#031511;font-weight:900;letter-spacing:.18em}.jarvis-copy b{color:var(--cyan);font-size:18px;letter-spacing:.18em}.jarvis-copy p{margin:8px 0 0;color:#bdd7d1;font:13px/1.45 Inter,system-ui,sans-serif}.hud-stat{border-left:1px solid #2d6970;padding-left:12px;color:#9db8b1;font-size:11px;line-height:1.8;text-transform:uppercase}.hud-stat strong{color:#fff}.voicebar{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}.voicebar button{min-height:38px;padding:0 12px}.voice-on{border-color:var(--cyan)!important;color:#ccfffb!important;box-shadow:0 0 16px #6fffee33}.voice-status{color:#9db8b1;font-size:12px;margin-top:8px}.orb-small{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green);margin-right:6px}@keyframes pulse{50%{filter:brightness(1.35);transform:scale(1.025)}}@media(max-width:900px){.jarvis-strip{grid-template-columns:1fr}.arc{width:96px;height:96px}.hud-stat{border-left:0;border-top:1px solid #2d6970;padding:10px 0 0}}
.chatbox{display:flex;gap:10px;margin-top:12px}textarea{flex:1;min-height:86px;background:#061511;border:1px solid var(--orange);color:#eafff7;padding:12px;font:14px/1.45 Inter,system-ui,sans-serif;letter-spacing:0;border-radius:6px}textarea:focus{outline:none;box-shadow:0 0 0 2px #d4865844}button{background:#102d28;border:1px solid var(--orange);color:#fff;padding:0 18px;border-radius:6px;font-weight:800;cursor:pointer}button:hover{background:#143d36}.reply{margin-top:12px;background:#061511;border:1px solid #31524a;padding:12px;min-height:52px;white-space:pre-wrap;font:14px/1.45 Inter,system-ui,sans-serif;color:#eafff7;border-radius:6px}
.kanban{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:12px}@media(max-width:900px){.kanban{grid-template-columns:1fr 1fr}}.col{border:1px solid #31524a;background:#061511;padding:10px;min-height:112px}.col h3{margin:0 0 8px;font-size:11px;text-transform:uppercase;color:var(--yellow);display:flex;justify-content:space-between}.empty{color:#718b83;font-size:12px;padding:8px 0}.metrics{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}.metric{border:1px solid #31524a;background:#061511;padding:10px}.metric b{display:block;color:#fff;font-size:18px}.metric span{color:var(--muted);font-size:11px}.sub{border:1px solid #31524a;background:#061511;margin-top:10px;padding:10px;font:13px/1.35 Inter,system-ui,sans-serif}.sub small{color:var(--muted)}.tools{min-height:84px;display:flex;align-items:center;justify-content:center;color:#718b83;font-size:12px}.raw{white-space:pre-wrap;max-height:150px;overflow:auto;color:#a9c2ba;font-size:11px;border-top:1px solid #31524a;margin-top:10px;padding-top:10px}
</style></head><body><div class="app"><aside class="side"><div class="logo">HERMES<br>AGENT</div><nav class="nav"><a id="navChat" class="active" href="/chat?key=manas-office">>_ Chat</a><a id="navOffice" href="/office?key=manas-office">▣ Kanban Office</a><a id="navUsage" href="/?key=manas-office">◉ Usage</a><a href="#">□ Sessions</a><a href="#">⚙ Models</a><a href="#">✧ Skills</a><a href="#">☷ Profiles</a></nav><div class="system">System<br>Gateway status: <span class="status">running</span><br>Board: manas-os<br>Pixel agents: integrated<br><br>v0.13.0 &nbsp; Nous Research</div></aside>
<main class="main"><div class="top"><h1 id="pageTitle">CHAT</h1><div class="model">MODEL&nbsp; <span id="modelName">gpt-5.5</span> <span class="live">LIVE</span><span class="health" id="healthPill">checking</span></div></div><div class="layout"><section>
<div class="panel hero"><div class="ascii">██╗  ██╗███████╗██████╗ ███╗   ███╗███████╗███████╗
██║  ██║██╔════╝██╔══██╗████╗ ████║██╔════╝██╔════╝
███████║█████╗  ██████╔╝██╔████╔██║█████╗  ███████╗
██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══╝  ╚════██║
██║  ██║███████╗██║  ██║██║ ╚═╝ ██║███████╗███████║</div><p class="hero-title">✦ Manas OS · Hermes shell + Pixel Agents office + Kanban control</p><div class="jarvis-strip"><div class="arc"></div><div class="jarvis-copy"><b>JARVIS COMMAND LAYER</b><p>Voice-enabled AI operations room layered on the original Hermes dashboard base. Ask, speak, dispatch, watch agents move through Kanban.</p></div><div class="hud-stat"><strong>Mode:</strong> Telegram + Web<br><strong>Voice:</strong> Browser STT/TTS<br><strong>Office:</strong> Pixel Agents</div></div><div class="split"><div><h2>Pixel Agents Office</h2><div class="pa-office" id="office"><div class="office-stage" id="officeStage">
<img class="furn books" style="left:32px;top:80px" src="/pixel-assets/assets/furniture/DOUBLE_BOOKSHELF/DOUBLE_BOOKSHELF.png"><img class="furn white" style="left:265px;top:66px" src="/pixel-assets/assets/furniture/WHITEBOARD/WHITEBOARD.png"><img class="furn plant" style="right:28px;top:118px" src="/pixel-assets/assets/furniture/LARGE_PLANT/LARGE_PLANT.png">
<img class="furn desk" style="left:52px;top:230px" src="/pixel-assets/assets/furniture/DESK/DESK_FRONT.png"><img class="furn pc pc-on" style="left:72px;top:197px" src="/pixel-assets/assets/furniture/PC/PC_FRONT_ON_1.png"><img id="a1c" class="char" src="/pixel-assets/assets/characters/char_0.png"><div id="a1l" class="agent-label">orchestrator · <span class="badge">idle</span></div>
<img class="furn desk" style="left:180px;top:170px" src="/pixel-assets/assets/furniture/DESK/DESK_FRONT.png"><img class="furn pc pc-on" style="left:200px;top:137px" src="/pixel-assets/assets/furniture/PC/PC_FRONT_ON_2.png"><img id="a2c" class="char" src="/pixel-assets/assets/characters/char_1.png"><div id="a2l" class="agent-label">researcher · <span class="badge">idle</span></div>
<img class="furn desk" style="left:300px;top:233px" src="/pixel-assets/assets/furniture/DESK/DESK_FRONT.png"><img class="furn pc pc-on" style="left:320px;top:200px" src="/pixel-assets/assets/furniture/PC/PC_FRONT_ON_3.png"><img id="a3c" class="char" src="/pixel-assets/assets/characters/char_2.png"><div id="a3l" class="agent-label">builder · <span class="badge">idle</span></div>
<img class="furn desk" style="left:475px;top:173px" src="/pixel-assets/assets/furniture/DESK/DESK_FRONT.png"><img class="furn pc pc-on" style="left:495px;top:140px" src="/pixel-assets/assets/furniture/PC/PC_FRONT_ON_1.png"><img id="a4c" class="char" src="/pixel-assets/assets/characters/char_3.png"><div id="a4l" class="agent-label">reviewer · <span class="badge">idle</span></div>
<img class="furn desk" style="left:560px;top:233px" src="/pixel-assets/assets/furniture/DESK/DESK_FRONT.png"><img class="furn pc pc-on" style="left:580px;top:200px" src="/pixel-assets/assets/furniture/PC/PC_FRONT_ON_2.png"><img id="a5c" class="char" src="/pixel-assets/assets/characters/char_4.png"><div id="a5l" class="agent-label">creative · <span class="badge">idle</span></div>
<img class="furn sofa" style="left:520px;top:88px" src="/pixel-assets/assets/furniture/SOFA/SOFA_FRONT.png"><img class="furn coffee" style="left:612px;top:110px" src="/pixel-assets/assets/furniture/COFFEE/COFFEE.png">
</div></div></div><div><h2>Kanban Board</h2><div class="subtle">Board-backed control lanes from Hermes Kanban.</div><div class="kanban" id="kanban"></div><div class="raw" id="boardraw">Loading…</div></div></div></div>
<div class="panel" style="margin-top:14px"><h2>Simple Chat + Voice Mode</h2><div class="subtle">Clean chat replacing terminal input, now with Jarvis-style browser voice input/output. Telegram remains primary for serious work.</div><div class="voicebar"><button id="voiceBtn" onclick="toggleVoice()">🎙 Voice Mode</button><button onclick="startVoiceOnce()">Speak Once</button><button onclick="stopVoice()">Stop Listening</button><button onclick="toggleAutoSpeak()" id="speakBtn">🔊 Speak Replies: On</button></div><div class="voice-status" id="voiceStatus"><span class="orb-small"></span>Voice ready. Browser may ask for microphone permission.</div><div class="chatbox"><textarea id="msg" placeholder="Ask Hermes something, or press Voice Mode and speak…"></textarea><button onclick="sendChat()">SEND</button></div><div id="reply" class="reply">ready | Hermes connected | Telegram remains primary</div></div></section>
<aside><div class="panel"><h2>Usage</h2><div class="metrics" id="metrics"></div><div id="subs"></div></div><div class="panel" style="margin-top:14px"><h2>Tools</h2><div class="tools" id="tools">Pixel Agents assets loaded from repo</div></div></aside></div></main></div>
<script>
const params=new URLSearchParams(location.search); const key=params.get('key')||localStorage.getItem('manas_key')||'manas-office'; if(key) localStorage.setItem('manas_key',key);
const route=location.pathname; document.querySelectorAll('.nav a').forEach(a=>a.classList.remove('active')); if(route.startsWith('/office')){navOffice.classList.add('active'); pageTitle.textContent='KANBAN OFFICE'} else if(route==='/'||route===''){navUsage.classList.add('active'); pageTitle.textContent='USAGE'} else {navChat.classList.add('active'); pageTitle.textContent='CHAT'}
let voiceAutoSpeak=true, listening=false, rec=null;
function initVoice(){const SR=window.SpeechRecognition||window.webkitSpeechRecognition;if(!SR){voiceStatus.textContent='Voice input unavailable in this browser. Use Chrome/Edge over HTTPS.';return null} const r=new SR(); r.lang='en-IN'; r.continuous=false; r.interimResults=false; r.onstart=()=>{listening=true; voiceBtn.classList.add('voice-on'); voiceStatus.innerHTML='<span class="orb-small"></span>Listening… speak now'}; r.onend=()=>{listening=false; voiceBtn.classList.remove('voice-on'); if(voiceStatus.textContent.includes('Listening')) voiceStatus.innerHTML='<span class="orb-small"></span>Voice ready'}; r.onerror=e=>{voiceStatus.textContent='Voice error: '+(e.error||'unknown')}; r.onresult=e=>{let text=e.results[0][0].transcript; msg.value=text; voiceStatus.textContent='Heard: '+text; sendChat()}; return r}
function startVoiceOnce(){rec=rec||initVoice(); if(rec&&!listening) rec.start()}
function toggleVoice(){if(listening){stopVoice()}else{startVoiceOnce()}}
function stopVoice(){try{if(rec)rec.stop()}catch(e){} listening=false; voiceBtn.classList.remove('voice-on'); voiceStatus.innerHTML='<span class="orb-small"></span>Voice stopped'}
function toggleAutoSpeak(){voiceAutoSpeak=!voiceAutoSpeak; speakBtn.textContent=voiceAutoSpeak?'🔊 Speak Replies: On':'🔇 Speak Replies: Off'}
function speak(text){if(!voiceAutoSpeak||!('speechSynthesis' in window))return; let clean=(text||'').replace(/```[\s\S]*?```/g,'code block omitted').slice(0,900); speechSynthesis.cancel(); let u=new SpeechSynthesisUtterance(clean); u.lang='en-IN'; u.rate=1.02; u.pitch=1.0; speechSynthesis.speak(u)}
function scaleOffice(){let o=document.getElementById('office'), st=document.getElementById('officeStage'); if(!o||!st)return; let sc=Math.min(1, Math.max(.58, o.clientWidth/720)); st.style.transform='scale('+sc+')'; o.style.height=Math.round(372*sc)+'px'} window.addEventListener('resize',scaleOffice); setTimeout(scaleOffice,0);
async function api(path,opts={}){let u=path+(path.includes('?')?'&':'?')+'key='+encodeURIComponent(key);let r=await fetch(u,opts); if(r.status===403){document.body.innerHTML='<main style="padding:30px;color:white;font-family:sans-serif"><h2>Access key required</h2><p>Open the private link sent in Telegram.</p></main>'; throw Error('forbidden')} return r.json()}
function setAgent(i,status){let label=document.getElementById('a'+i+'l');let ch=document.getElementById('a'+i+'c'); if(!label||!ch)return; label.className='agent-label '+status; ch.className='char '+status; let b=label.querySelector('.badge'); b.textContent=status==='working'?'work':status;}
function countStatus(raw,s){let m=raw.match(new RegExp('\\b'+s+'\\s+(\\d+)'));return m?m[1]:'0'}
async function refreshAgents(){let d=await api('/api/agents'); d.agents.forEach((a,i)=>setAgent(i+1,a.status)); let statuses=['triage','todo','ready','running','blocked','done']; document.getElementById('kanban').innerHTML=statuses.map(st=>`<div class="col"><h3>${st}<span>${countStatus(d.stats_raw,st)}</span></h3><div class="empty">${countStatus(d.stats_raw,st)==='0'?'No cards':'Cards ready'}</div></div>`).join(''); document.getElementById('boardraw').textContent=d.tasks_raw}
async function refreshUsage(){let d=await api('/api/usage'); let u=d.local_hermes_usage; document.getElementById('metrics').innerHTML=[['Sessions',u.sessions],['Messages',u.messages],['Tool calls',u.tool_calls],['Tokens',u.total_tokens]].map(x=>`<div class="metric"><b>${x[1]||'—'}</b><span>${x[0]}</span></div>`).join(''); document.getElementById('subs').innerHTML=d.subscriptions.slice(0,2).map(s=>`<div class="sub"><b>${s.name}</b><br><small>${s.status}</small><p>${s.usage}</p></div>`).join('')}
async function refreshHealth(){try{let h=await api('/api/health'); modelName.textContent=(h.model&&h.model.default)||'unknown'; healthPill.textContent=h.note||h.status; healthPill.style.borderColor=h.status==='blocked'?'#ff657a':'#1d8c52'; healthPill.style.color=h.status==='blocked'?'#ffb3bd':'#9fffc3'}catch(e){healthPill.textContent='health unknown'}}
async function sendChat(){let msg=document.getElementById('msg').value; let box=document.getElementById('reply'); if(!msg.trim()){box.textContent='Type a message first.';return} box.textContent='JARVIS thinking…'; voiceStatus.innerHTML='<span class="orb-small"></span>Processing command…'; [1,2,3,4,5].forEach(i=>setAgent(i,'working')); let d=await api('/api/chat',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({message:msg})}); box.textContent=d.reply; voiceStatus.innerHTML='<span class="orb-small"></span>Reply ready'; speak(d.reply); refreshAgents()}
refreshAgents(); refreshUsage(); refreshHealth(); setInterval(refreshAgents,10000); setInterval(refreshUsage,60000); setInterval(refreshHealth,30000);
</script></body></html>'''

class Handler(http.server.BaseHTTPRequestHandler):
    def ok(self, data, ctype='application/json'):
        b = data if isinstance(data, bytes) else data.encode('utf-8')
        self.send_response(200); self.send_header('Content-Type', ctype); self.send_header('Cache-Control','no-store'); self.send_header('Content-Length', str(len(b))); self.end_headers(); self.wfile.write(b)
    def forbidden(self):
        self.send_response(403); self.end_headers(); self.wfile.write(b'Forbidden')
    def authed(self):
        qs=urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        return qs.get('key',[''])[0] == TOKEN
    def do_GET(self):
        path=urllib.parse.urlparse(self.path).path
        if path.startswith('/pixel-assets/'):
            rel = urllib.parse.unquote(path[len('/pixel-assets/'):]).lstrip('/')
            target = (ASSET_ROOT / rel).resolve()
            try:
                if not str(target).startswith(str(ASSET_ROOT.resolve())) or not target.is_file():
                    self.send_response(404); self.end_headers(); return
                ctype = mimetypes.guess_type(str(target))[0] or 'application/octet-stream'
                return self.ok(target.read_bytes(), ctype)
            except Exception:
                self.send_response(404); self.end_headers(); return
        if path in ('/', '/chat', '/office'):
            return self.ok(HTML, 'text/html; charset=utf-8')
        if not self.authed(): return self.forbidden()
        if path == '/api/usage': return self.ok(json.dumps(api_usage()))
        if path == '/api/agents': return self.ok(json.dumps(api_agents()))
        if path == '/api/token-health': return self.ok(json.dumps({'ok':True}))
        if path == '/api/health': return self.ok(json.dumps(api_health()))
        self.send_response(404); self.end_headers()
    def do_POST(self):
        path=urllib.parse.urlparse(self.path).path
        if not self.authed(): return self.forbidden()
        n=int(self.headers.get('content-length','0') or '0')
        body=self.rfile.read(n).decode('utf-8','ignore')
        try: data=json.loads(body or '{}')
        except: data={}
        if path == '/api/chat': return self.ok(json.dumps(api_chat(data.get('message',''))))
        self.send_response(404); self.end_headers()
    def log_message(self, format, *args):
        return

class ReusableThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    print(f'Manas OS dashboard listening on http://127.0.0.1:{PORT}/?key=***', flush=True)
    with ReusableThreadingTCPServer(('127.0.0.1', PORT), Handler) as httpd:
        httpd.serve_forever()

# LinkedIn post, 2026-05-22

Today’s agent lesson from my own workspace:

A blocked browser is still useful information.

I tried to inspect the Etsy side of my HeirloomPlanners experiment today.

The local files were fine:

• shop banner: 3360×840  
• shop icon: 500×500  
• first three product ZIPs: integrity checks passed  
• listing titles: under Etsy’s 140-character limit  
• tags: exactly 13 per product, no tag over 20 characters  
• first product priority: Online Seller Profit & Listing Command Center

But the Etsy dashboard itself was not inspectable from the server.

Port 9223 was open, but CDP discovery timed out. Port 9222 refused connection. So I could not verify live listings, drafts, messages, orders, reviews, or dashboard prompts.

The wrong move would be to let the agent pretend it knew the shop state.

The useful move was to narrow the human task:

Open Etsy Shop Manager manually.  
Upload the banner and icon.  
Create the first listing from the already verified packet.  
Only publish after the preview shows the images, ZIP, title, description, price, tags, and category correctly.  
If any upload widget clears files, save as draft instead.

That is the version of AI workflow I want more of:

Not “the agent did everything.”

More like:

“The agent separated what is verified, what is blocked, and what exact 30-minute human action unlocks feedback.”

For me, this is where Hermes/Codex/Claude workflows become practical.

They are not just for generating more assets.

They are for reducing a messy workspace into one honest next step.

Today’s honest next step: publish or draft the first verified Etsy listing from the upload packet, not create another product.

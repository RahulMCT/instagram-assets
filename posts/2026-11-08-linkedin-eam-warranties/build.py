import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:20px;line-height:1.28}.box h2{font-size:24px;margin-bottom:3px}.tbl{font-size:17px}.tbl th,.tbl td{padding:2px 6px}.iq ol{font-size:19px;line-height:1.22}.pill{font-size:16.5px}.grid{gap:12px}.handle{bottom:-12px}.box{padding:9px 12px}.tagline{font-size:19px;margin-bottom:9px}.code{font-family:Consolas,'DejaVu Sans Mono',monospace;background:#f1f5f9;border:1px dashed #94a3b8;border-radius:6px;padding:6px 8px;margin:4px 0;line-height:1.35;font-size:17px;white-space:pre-wrap;word-break:break-all}</style>
<div class="title">🛡️ HxGN EAM Warranties &amp; Claims <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">Stop paying for repairs the OEM already owes you. (Infor EAM Warranties brief)</div>
<div class="grid">
<div class="box c1"><h2>1. Warranty record</h2><ul><li>Warranty Type: <b>Equipment</b> (default) or <b>Part</b></li><li>Manufacturer, Supplier, Control Number</li><li>Agreement Start / End, On-site Repair, Loaner Provided</li><li>Renewal Alert Email</li></ul></div>
<div class="box c2"><h2>2. Start Date Basis</h2><ul><li>Equipment: <b>Commission Date</b> (default), Original / Latest Receipt, Original / Latest Install, Agreement Start</li><li>Part: Agreement Start or blank</li><li>Default Duration + Renewal Threshold (days)</li></ul></div>
<div class="box c3"><h2>3. Cost coefficients</h2><div class="code">Labor %, Hired Labor %, Services %
Stock Items %, Direct Purchases %
Tools %   → all default 100</div><ul><li>Max Labor / Stock Amount per claim</li></ul></div>
<div class="box c4"><h2>4. Fixed overrides</h2><table class="tbl"><tr><th>Enter</th><th>Clears + protects</th></tr><tr><td>Fixed Labor Rate</td><td>Labor, Hired Labor, Services %</td></tr><tr><td>Fixed Labor Amount</td><td>those 3 % + Fixed Labor Rate</td></tr><tr><td>Fixed Stock Amount</td><td>Stock Items %, Direct Purchases %</td></tr></table></div>
<div class="box c5"><h2>5. Equipment coverage</h2><ul><li><b>Calendar</b> (days, default) or <b>Usage</b> (UOM)</li><li>Usage UOM must be a logical meter on the equipment</li><li>Only Asset, Position, System. No Locations</li><li>Threshold flags upcoming expiry</li></ul></div>
<div class="box c6"><h2>6. Parts &amp; Components</h2><ul><li>Parts tab: <b>Warranty Days</b> after issue</li><li>Reimbursement: R Replacement / <b>C Cash</b> (default)</li><li>Components (ex-VMRS codes): System → Assembly → Component level, own cost coverage</li></ul></div>
<div class="box c7"><h2>7. Warranty claim math</h2><div class="code">WO internal labor   = $500
Warranty Labor %    = 80
WO Labor on claim   = $400
No warranty on claim → 100%</div><ul><li>Only <b>warrantable</b> activities / jobs count</li></ul></div>
<div class="box c8"><h2>8. Creating claims</h2><ul><li>Warranty Claim screen, or <b>Create Warranty Claim</b> popup on WO, Activity or Job tab</li><li>One non-cancelled claim per WO + Activity + Job</li><li>RMA Required → RMA Number mandatory</li><li>Parts: Part Warranty Claim + Import Parts</li></ul></div>
<div class="box c1"><h2>9. Claim status rules</h2><ul><li>New claim starts <b>Unfinished</b></li><li>Approved, Response Received, Completed, Cancelled → Activities tab protected</li><li>Settlement Details: Date Resolved, Total Settlement</li></ul></div>
<div class="box c2"><h2>10. Issue / Return Parts</h2><ul><li>Same part, same equipment + component location, inside warranty period → <b>Warranty</b> box ticked + warning</li><li>Logged in <b>r5warclaimparts</b></li><li>Print Warranty Return Label(s): qty 1, not on Returns</li></ul></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">Flow</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">Warranty</span><span class="arr">→</span><span class="pill">Coverage</span><span class="arr">→</span><span class="pill">Failure WO</span><span class="arr">→</span><span class="pill">Claim</span><span class="arr">→</span><span class="pill">Settlement</span></div></div>
<div class="box iq"><h2>Consultant tips</h2><ol><li>Flag warrantable activities before costs post</li><li>Keep Exclude PM Work Order on to cut PM noise</li><li>Set Renewal Alert Email on day one</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">Key points</h2><ul><li>% coefficients default 100</li><li>Fixed values override %</li><li>Usage UOM = logical meter</li></ul></div>
</div></div>'''
build("/workspace/instagram-assets/posts/2026-11-08-linkedin-eam-warranties",B,1350,"Rahul Kumar")

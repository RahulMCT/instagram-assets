import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:18.5px;line-height:1.25}.box h2{font-size:22.5px;margin-bottom:3px}.tbl{font-size:16px}.tbl th,.tbl td{padding:2px 6px}.iq ol{font-size:18px;line-height:1.24}.pill{font-size:15px}.grid{gap:10px}.handle{bottom:-12px}.box{padding:9px 12px}.tagline{font-size:19px;margin-bottom:9px}.code{font-family:Consolas,'DejaVu Sans Mono',monospace;background:#f1f5f9;border:1px dashed #94a3b8;border-radius:6px;padding:5px 7px;margin:4px 0;line-height:1.3;font-size:15px;white-space:pre-wrap;word-break:break-all}</style>
<div class="title">📉 HxGN EAM Equipment Depreciation <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">Value an asset over its useful life, event by event. (Infor EAM Equipment Depreciation brief, 11.5)</div>
<div class="grid">
<div class="box c1"><h2>1. Where it lives</h2><ul><li><b>Assets</b> screen → <b>Depreciation</b> tab</li><li>Fields: Type, From Date, Category, Method, Change Value / Life / Est. Lifetime Output</li><li>Relative Start + UOM for Equipment Configuration</li><li>Tab supports <b>UDFs</b></li></ul></div>
<div class="box c2"><h2>2. Depreciation Types</h2><ul><li>Entity <b>DETP</b>, default <b>*</b></li><li><b>GAAP</b>, <b>GASB</b>, <b>IFRS</b> + user-defined</li><li>Informational only: track operational vs accounting standards side by side</li></ul></div>
<div class="box c3"><h2>3. Straight Line</h2><div class="code">(Starting − Residual) / Useful Life
($5000 − $200) / 5 = $960 per year</div><ul><li>Simplest, most common</li></ul></div>
<div class="box c4"><h2>4. Sum of Years Digits</h2><div class="code">5 yrs → 5+4+3+2+1 = 15
Yr1 = $4800 × 5/15 ≈ $1600
Yr5 = $4800 × 1/15 ≈ $320</div><ul><li>Accelerated: more value lost early</li></ul></div>
<div class="box c5"><h2>5. Double Declining Balance</h2><div class="code">SL rate 20% → doubled 40%
Yr1 $4800 × 40% = $1920
Yr2 $2880 × 40% = $1152
Yr3 $691.20 &lt; $960 → switch to SL</div></div>
<div class="box c6"><h2>6. Units of Output</h2><div class="code">Rate = (Starting − Residual)
       / Est. Lifetime Output
Dep = Rate × Units produced</div><ul><li>Idle asset = <b>zero</b> depreciation</li><li>Best for assets with varying usage</li></ul></div>
<div class="box c7"><h2>7. Categories (DECT, 11)</h2><table class="tbl"><tr><th>Event</th><th>Needs</th></tr><tr><td>Commission (1st record default)</td><td>—</td></tr><tr><td>Increase / Decrease Value</td><td>Change Value</td></tr><tr><td>Increase / Decrease Life</td><td>Change Life</td></tr><tr><td>Inc / Dec Est. Lifetime Output</td><td>Units of Output only</td></tr><tr><td>Suspend → Reactivate</td><td>—</td></tr><tr><td>Change Depreciation Method</td><td>—</td></tr><tr><td>Early Disposal</td><td>no records after</td></tr></table></div>
<div class="box c8"><h2>8. Rules to remember</h2><ul><li>Change Value = <b>0</b> → Residual Value opens for edit</li><li>Recalc runs from <b>From Date</b>, replaces same/projected dates</li><li>Change Method: Units of Output excluded once records exist; blocked after Early Disposal</li></ul></div>
<div class="box c1"><h2>9. Setup steps</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">Add Depreciation Type</span><span class="arr">→</span><span class="pill">From Date = Commission Date</span><span class="arr">→</span><span class="pill">Method</span><span class="arr">→</span><span class="pill">Starting / Life / Residual</span></div><ul><li><b>View Depreciation Details</b>: To Date, Book Value, Period to Date</li></ul></div>
<div class="box c2"><h2>10. Equipment Configuration</h2><ul><li>Plan future events on templates</li><li><b>Relative Start</b> + <b>UOM</b> required</li><li>Commission 1/1/2015 + 5 Years → event in 2020</li></ul></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">Flow</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">Commission</span><span class="arr">→</span><span class="pill">Periodic calc</span><span class="arr">→</span><span class="pill">Life / Value events</span><span class="arr">→</span><span class="pill">Suspend / Reactivate</span><span class="arr">→</span><span class="pill">Early Disposal</span></div></div>
<div class="box iq"><h2>Consultant tips</h2><ol><li>Pick Units of Output on day one if usage drives value</li><li>Log PM upgrades as Increase Life / Value</li><li>Use one Type per accounting standard</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">Key points</h2><ul><li>4 methods, 11 categories</li><li>Events recalc from From Date</li><li>Early Disposal is final</li></ul></div>
</div></div>'''
build("/workspace/instagram-assets/posts/2026-11-07-linkedin-eam-equipment-depreciation",B,1350,"Rahul Kumar")

import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:18.5px;line-height:1.27}.box h2{font-size:24px;margin-bottom:4px}.code{font-size:14.5px;line-height:1.34}.tbl{font-size:16.5px}.tbl th,.tbl td{padding:3px 6px}.iq ol{font-size:17px;line-height:1.28}.pill{font-size:13.5px}.grid{gap:9px}.box li:before{font-size:16px}.handle{bottom:-12px}.box{padding:9px 11px}.tagline{font-size:18px;margin-bottom:7px}.note{font-size:15px}
.b{display:inline-block;padding:1px 6px;border-radius:4px;font-weight:700;font-size:15px;background:#e8f0fe;color:#1a3a5c}</style>
<div class="title">📊 HxGN EAM Overview 360 <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">Configurable widget dashboards for one asset or a whole org — List, KPI, charts, reports, custom URLs. (HxGN EAM 12.1 Overview 360 brief)</div>
<div class="grid">
<div class="box c1"><h2>1. What &amp; why</h2><ul><li>Two screens: <b>Equipment Overview 360</b> and <b>Organization Overview 360</b></li><li>Pick and configure widgets to user needs</li><li>Equipment screen: most widgets are <b>equipment-sensitive</b></li><li>Org screen: same idea, but <b>organization-sensitive</b></li></ul></div>
<div class="box c2"><h2>2. Widget types</h2><ul><li><b>List</b> — Dataspy results from EAM screens</li><li><b>KPI</b> — same KPIs as KPI Setup / Start Center</li><li><b>Pie / Line / Stacked Bar / Heat Map</b> — Queries or grids</li><li><b>Report</b> — Cognos HTML reports</li><li><b>Custom URL</b> — HTML custom tabs (incl. OpenCAD)</li></ul></div>
<div class="box c3"><h2>3. KPI widget</h2><ul><li>Shows a Key Performance Indicator defined on <b>KPI Setup</b></li><li>Same KPIs you can put on the EAM <b>Start Center</b></li><li>Config: pick one listed KPI — no further setup on the widget</li><li>Great for MTTR, open WO count, overdue PMs at a glance</li></ul></div>
<div class="box c4"><h2>4. Chart query rules</h2><table class="tbl"><tr><th>Widget</th><th>Columns</th></tr><tr><td>Pie</td><td>slice + numeric size</td></tr><tr><td>Line</td><td>x-axis + numeric y (aliases = labels)</td></tr><tr><td>Stacked Bar</td><td>x + up to 49 numeric series</td></tr><tr><td>Heat Map</td><td>row dim + numeric cells (aliases = cols)</td></tr></table><div class="note" style="margin-top:4px">Queries screen: tick <b>Normal</b> or it won&apos;t appear in the lookup.</div></div>
<div class="box c5"><h2>5. Sensitivity params</h2><div class="code">Queries (WHERE):
  :OBJECT / :OBJECTORG   equipment
  :ORG                   organization

User-defined Tab grids:
  :parameter.object
  :parameter.objorganization

Custom URL:
  equipmentno &amp; organization</div><div class="note">List View grids = system params only → no equipment sensitivity.</div></div>
<div class="box c6"><h2>6. Grids vs Queries</h2><ul><li>Grid Designer: Grid Type <b>List View</b> or <b>Tab</b></li><li>Tab grids: parent must be Assets / Positions / Systems / Locations (or clone)</li><li>Always pick a Dataspy; chart Dataspies must match column rules</li><li>Grids must be accessible (menu / parent tab)</li><li>Org Overview 360: List View grids only (no tab grids)</li></ul></div>
<div class="box c7"><h2>7. Edit Mode &amp; layout</h2><ul><li>Edit Mode: add / remove / drag widgets</li><li>Buttons: Exit Edit Mode · Edit Layout · Add Widget</li><li>Layout = 1 to 3 columns; reducing columns shifts rightmost widgets left</li><li>New widgets land in column 1; configure via Options → Edit</li><li>Personalize = title color · Refresh · Delete (Edit Mode)</li></ul></div>
<div class="box c8"><h2>8. Report &amp; Custom URL</h2><ul><li>Report must be <b>HTML</b>; define params even if unused: <b>SEL_OBJ</b>, <b>SEL_ORG</b>, <b>R5_OUTPUTFORMAT</b> (default HTML), Mandatory off</li><li>Org Overview: only SEL_ORG required</li><li>Custom URL height 300–600 px; Type = HTML custom tab</li><li>Native OpenCAD SVG / BIM URLs are equipment-sensitive</li></ul></div>
<div class="box c1" style="grid-column:1 / span 2"><h2>9. Overview templates</h2><ul><li>Admin builds a layout → <b>Save Template</b> (Code, Description, Public, Out of Service)</li><li>Grant via <b>User Groups → Overview Templates</b>; optional <b>Default</b> for the group</li><li>Users get a role-ready dashboard without configuring widgets themselves</li><li>Example: WORK-PLANNER for planners — Public usually off for role-specific packs</li><li>Colors: optional install param <b>360COLOR</b> (nivo schemes: category10, dark2, set1, paired, spectral)</li></ul></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">10a. Setup flow</h2><div class="flow"><span class="pill">KPI Setup / Queries / Grids</span><span class="arr">→</span><span class="pill">Edit Mode</span><span class="arr">→</span><span class="pill">Add widgets</span><span class="arr">→</span><span class="pill">Save Template</span><span class="arr">→</span><span class="pill">User Groups</span></div></div>
<div class="box iq"><h2>10b. Consultant tips</h2><ol><li>Design KPIs once; reuse on Start Center + 360</li><li>Mark Queries as Normal</li><li>Use :OBJECT filters for asset focus</li><li>Ship templates per role, not ad-hoc layouts</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">10c. Key points</h2><ul><li>Equip vs Org 360</li><li>KPI = Start Center</li><li>Templates scale</li></ul></div>
</div></div>'''
build("/workspace/social/posts/2026-10-15-linkedin-eam-overview-360",B,1620,"Rahul Kumar")

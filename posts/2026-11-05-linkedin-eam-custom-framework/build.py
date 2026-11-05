import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:19px;line-height:1.27}.box h2{font-size:23px;margin-bottom:4px}.tbl{font-size:16.5px}.tbl th,.tbl td{padding:2px 6px}.iq ol{font-size:18.5px;line-height:1.25}.pill{font-size:15.5px}.grid{gap:10px}.handle{bottom:-12px}.box{padding:9px 12px}.tagline{font-size:19px;margin-bottom:9px}.code{font-family:Consolas,'DejaVu Sans Mono',monospace;background:#f1f5f9;border:1px dashed #94a3b8;border-radius:6px;padding:5px 7px;margin:4px 0;line-height:1.3;font-size:15px;white-space:pre-wrap;word-break:break-all}</style>
<div class="title">🧩 HxGN EAM Custom Framework <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">Your own web app, opened inside EAM menus, tabs &amp; toolbar. (HxGN EAM Custom Framework brief, 12.1)</div>
<div class="grid">
<div class="box c1"><h2>1. What it gives you</h2><ul><li>Screens built in a <b>separate web app</b>, opened through EAM</li><li><b>Menus &amp; tabs</b> + <b>Toolbar</b> (Save/New/Delete work as usual)</li><li><b>System API</b> + <b>User-defined grids</b> (UDG)</li></ul></div>
<div class="box c2"><h2>2. ISA vs ESA</h2><table class="tbl"><tr><th></th><th>ISA</th><th>ESA</th></tr><tr><td>JVM</td><td>Same as EAM</td><td>Outside EAM's JVM</td></tr><tr><td>Tech</td><td>J2EE web 2.2+ war/ear</td><td>Any HTTP 1.1 web app (.Net, Java…)</td></tr><tr><td>System API</td><td>✔ Yes</td><td>✘ No</td></tr></table><ul><li>Need the API? Use ISA. Else ESA is fine</li></ul></div>
<div class="box c3"><h2>3. Stand-alone screen</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">Screens (BSFUNC)</span><span class="arr">→</span><span class="pill">6-letter mnemonic</span><span class="arr">→</span><span class="pill">URL Path</span><span class="arr">→</span><span class="pill">Add to menu</span></div><ul><li>Untick <b>Open URL in New Window</b>, or menus &amp; toolbar are lost</li></ul></div>
<div class="box c4"><h2>4. Custom tab on a screen</h2><ul><li>Screens → pick screen → <b>Custom Tabs</b> tab</li><li>Tab type <b>HTML</b> + fully qualified URL Path</li><li>Tab name format <b>UT&lt;seq&gt;</b> (UT1…)</li><li>Permissions are <b>all disabled</b> by default</li></ul></div>
<div class="box c5"><h2>5. Parameters EAM passes</h2><ul><li><b>eamid</b>, <b>internal_eamid</b>, <b>tenant</b></li><li>SYSTEM_ / USER_FUNCTION_NAME, CURRENT_TAB_NAME (tabs)</li><li>Header key field values (tabs)</li><li>Replaced in URL: <b>:user :password :org</b></li></ul></div>
<div class="box c6"><h2>6. Tab on a UDG</h2><ul><li>Grid Designer <b>(BSGRID)</b>, 6-letter name, <b>2nd letter U</b></li><li>Table in From Clause; select key fields + org</li><li>Mark keys as <b>Grid Key</b>; default Dataspy <b>Active</b></li></ul></div>
<div class="box c7"><h2>7. JavaScript Message API</h2><ul><li><b>window.postMessage</b> (EAM 11.0+), cross-origin safe</li></ul><div class="code">{ messageName: 'toolbarButtonState',
  buttons: ['saveRec','deleteRec'],
  state: 'enable' }</div><ul><li>Also: toolbarButtonClick, showMessage, directSelect, tabSelect, hyperlink, setDirtyFlag</li></ul></div>
<div class="box c8"><h2>8. System API (ISA, Java)</h2><ul><li>Package <b>com.dstm.mp.eamaccess</b></li></ul><div class="code">mEamFactory = EAMAccessManagerFactory.getInstance();
EAMAccessManager m =
  mEamFactory.getEAMAccessManager(pRequest);
getInstallParameter("DEPTSEC");
getOrgSecurity("ORG1","ACCCNT","UT1");</div><ul><li>Also: session check, DB connection</li></ul></div>
<div class="box c1"><h2>9. Golden rules</h2><ul><li><b>One</b> EAMAccessManager per request</li><li>Call <b>endRequest()</b> in a finally block</li><li>No HttpSession: use <b>EAMAccessSession</b> set/getAttribute, serializable objects (stateful + stateless)</li></ul></div>
<div class="box c2"><h2>10. Deploy (sample app)</h2><div class="code">jar cvf sampleApp.war .
rename → sampleApp.zip
→ &lt;EAM_HOME&gt;/overrides/customerwars
deploy.bat / ./deploy.sh → restart</div><ul><li>Set <b>EAM_DOMAIN</b> in customframework_common.js</li></ul></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">Flow</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">EAM menu/tab</span><span class="arr">→</span><span class="pill">URL + eamid</span><span class="arr">→</span><span class="pill">Your app</span><span class="arr">⇄</span><span class="pill">postMessage</span></div></div>
<div class="box iq"><h2>Consultant tips</h2><ol><li>Install the sample ISA first</li><li>ESA on another domain hits same-origin limits: use a proxy</li><li>Grant tab permissions</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">Key points</h2><ul><li>ISA = API access</li><li>BSFUNC / BSGRID</li><li>endRequest() always</li></ul></div>
</div></div>'''
build("/workspace/instagram-assets/posts/2026-11-05-linkedin-eam-custom-framework",B,1350,"Rahul Kumar")

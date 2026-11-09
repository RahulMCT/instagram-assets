import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:20px;line-height:1.28}.box h2{font-size:24px;margin-bottom:3px}.tbl{font-size:17px}.tbl th,.tbl td{padding:2px 6px}.iq ol{font-size:19px;line-height:1.22}.pill{font-size:16.5px}.grid{gap:12px}.handle{bottom:-12px}.box{padding:9px 12px}.tagline{font-size:19px;margin-bottom:9px}.code{font-family:Consolas,'DejaVu Sans Mono',monospace;background:#f1f5f9;border:1px dashed #94a3b8;border-radius:6px;padding:6px 8px;margin:4px 0;line-height:1.35;font-size:17px;white-space:pre-wrap;word-break:break-all}</style>
<div class="title">🔧 HxGN EAM Mechanic's Workbench <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">The technician's To Do list: start, stop and complete work, and labor books itself. (Infor EAM Mechanic's Workbench brief)</div>
<div class="grid">
<div class="box c1"><h2>1. What it is</h2><ul><li>Central screen for mechanics: assigned WO activities, task details, equipment</li><li>Start / Stop / Complete work from one place</li><li><b>Stop Job</b> creates the book labor record</li></ul></div>
<div class="box c2"><h2>2. What fills the list</h2><ul><li>Scheduled labor records of the employee</li><li><b>Daily Scheduling</b>: WO Daily Scheduling, Schedule Labor tab, WO Scheduling</li><li><b>Shift Scheduling</b>: only the Shift Scheduling tab</li></ul></div>
<div class="box c3"><h2>3. Shift auto-pick</h2><div class="code">a) earliest shift starting
   in next 8 hours
b) else latest shift ended
   in last 8 hours (ongoing ok)
c) else Shift stays blank</div><ul><li>Blank Shift → Daily records for yesterday, today, tomorrow</li></ul></div>
<div class="box c4"><h2>4. Header fields</h2><ul><li>Employee: from logged-on user (else enter it)</li><li>Shift Session / Start / Duration: from Shift</li><li><b>Type of Hours</b>: set it BEFORE Start Job, used on the booking</li><li>Password: optional, only checked if entered</li></ul></div>
<div class="box c5"><h2>5. Work Details grid</h2><table class="tbl"><tr><th>Field</th><th>Meaning</th></tr><tr><td>Started</td><td>Activity/job running; default Dataspy sorts it to top</td></tr><tr><td>Scheduled Trade</td><td>From scheduled labor</td></tr><tr><td>Planned Trade</td><td>From WO activity</td></tr><tr><td>Main Resource</td><td>Scheduled trade = planned trade</td></tr></table></div>
<div class="box c6"><h2>6. Due Percentage</h2><div class="code">PM every 100 days,
last done 90 days ago → 90%
12 days later          → 102%</div><ul><li>Calendar + meter PM: highest % shown</li></ul></div>
<div class="box c7"><h2>7. Start / Stop / Complete</h2><ul><li><b>Start Job</b>: checks pass → temp start record, Started ticked, Timer runs</li><li>Start another job → current one auto-stopped first</li><li><b>Stop Job</b>: no selection needed; failed check → no labor record, book manually</li><li><b>Complete Job</b>: Completed ticked, 100%, Hours Remaining 0</li></ul></div>
<div class="box c8"><h2>8. Timer &amp; links</h2><ul><li>Timer = now minus start time; keeps running if you leave the screen</li><li>Timer at zero = nothing started</li><li>Actions → View Comments / View Documents (Task Plan, Job Plan, PM, Pattern, activity)</li></ul></div>
<div class="box c1"><h2>9. Own User ID setup</h2><table class="tbl"><tr><th>Screen Designer</th><th>Setting</th></tr><tr><td>Employee</td><td>Protected</td></tr><tr><td>Password</td><td>Hidden</td></tr><tr><td>Clear Employee/Password</td><td>Hide Button</td></tr></table><ul><li>Log off after use</li></ul></div>
<div class="box c2"><h2>10. Shared kiosk setup</h2><table class="tbl"><tr><th>Field</th><th>No User ID</th><th>Has User ID</th></tr><tr><td>Employee</td><td>Required</td><td>Required</td></tr><tr><td>Password</td><td>Hidden</td><td>Required</td></tr><tr><td>Clear button</td><td>Show</td><td>Show</td></tr></table><ul><li>Click Clear Employee/Password when done</li></ul></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">Flow</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">Schedule labor</span><span class="arr">→</span><span class="pill">Workbench</span><span class="arr">→</span><span class="pill">Start Job</span><span class="arr">→</span><span class="pill">Stop Job</span><span class="arr">→</span><span class="pill">Booked labor</span></div></div>
<div class="box iq"><h2>Consultant tips</h2><ol><li>Link every Employee to a User ID</li><li>Pick the kiosk mode before go-live</li><li>Train Type of Hours before Start</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">Key points</h2><ul><li>Stop Job = labor booking</li><li>Started with password → stop needs it</li><li>8-hour shift window</li></ul></div>
</div></div>'''
build("/workspace/instagram-assets/posts/2026-11-09-linkedin-eam-mechanics-workbench",B,1350,"Rahul Kumar")

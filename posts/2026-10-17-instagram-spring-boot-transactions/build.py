import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:17px;line-height:1.24}.box li code,.box p code{font-size:14.5px;font-family:monospace;background:#efeae0;padding:0 3px;border-radius:3px}.box h2{font-size:21px;margin-bottom:3px}.code{font-size:13px;line-height:1.26}.tbl{font-size:15px}.tbl th,.tbl td{padding:2px 5px}.iq ol{font-size:16px;line-height:1.22}.pill{font-size:13.5px}.grid{gap:8px}.handle{bottom:-12px}.box{padding:8px 10px}.tagline{font-size:17.5px;margin-bottom:6px}.note{font-size:14.5px}</style>
<div class="title">🍃 Spring Boot Transactions <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">Transactional annotation = AOP proxy wraps your method: begin → commit on success → rollback on RuntimeException by default.</div>
<div class="grid">
<div class="box c1"><h2>1. What &amp; why</h2><ul><li>A <b>transaction</b> = all-or-nothing unit of DB work</li><li><b>ACID</b>: Atomic · Consistent · Isolated · Durable</li><li>Without it: half-updated rows, dirty money transfers</li><li>Spring Boot auto-enables tx when a DataSource exists</li></ul></div>
<div class="box c2"><h2>2. How it works (AOP)</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">Caller</span><span class="arr">→</span><span class="pill">Proxy</span><span class="arr">→</span><span class="pill">begin</span><span class="arr">→</span><span class="pill">your method</span><span class="arr">→</span><span class="pill">commit / rollback</span></div><ul style="margin-top:4px"><li>Annotation triggers a Spring AOP <b>proxy</b></li><li>Only works when called <b>through the proxy</b></li><li>EnableTransactionManagement is on by default in Boot</li></ul></div>
<div class="box c3"><h2>3. Propagation (the big table)</h2><table class="tbl"><tr><th>Value</th><th>Behavior</th></tr><tr><td><b>REQUIRED</b></td><td>join existing, else create (default)</td></tr><tr><td><b>REQUIRES_NEW</b></td><td>suspend + always new tx</td></tr><tr><td><b>SUPPORTS</b></td><td>join if exists, else non-tx</td></tr><tr><td><b>MANDATORY</b></td><td>must join; else error</td></tr><tr><td><b>NEVER</b></td><td>error if a tx exists</td></tr><tr><td><b>NOT_SUPPORTED</b></td><td>suspend existing; run non-tx</td></tr><tr><td><b>NESTED</b></td><td>savepoint inside current</td></tr></table></div>
<div class="box c4"><h2>4. Rollback rules</h2><ul><li>Default: rollback on <code>RuntimeException</code> / <code>Error</code></li><li><b>Checked</b> exceptions do <b>NOT</b> roll back by default</li><li><code>rollbackFor = Exception.class</code> → roll back checked too</li><li><code>noRollbackFor = ...</code> → keep commit for listed types</li><li><code>readOnly = true</code> → hint for optimization / flush skip</li></ul></div>
<div class="box c5"><h2>5. Example service</h2><div class="code">@Service
public class TransferService {
  @Transactional  // REQUIRED
  public void transfer(Long from, Long to,
                       BigDecimal amt) {
    debit(from, amt);
    credit(to, amt);
    // RuntimeException → full rollback
  }
  @Transactional(propagation =
      Propagation.REQUIRES_NEW)
  public void audit(String msg) {
    // commits even if outer rolls back
  }
}</div></div>
<div class="box c6"><h2>6. Self-invocation trap</h2><ul><li><code>this.transfer()</code> from same class → <b>no proxy</b> → no tx</li><li>Fix: call via another bean, or self-inject the proxy</li><li>private / final methods are not proxied (JDK/CGLIB limits)</li><li>Same for unchecked → checked: annotate carefully</li></ul></div>
<div class="box c7"><h2>7. Common mistakes</h2><ul><li>Catching RuntimeException inside method → Spring never sees it → no rollback</li><li>Expecting checked Exception to roll back without <code>rollbackFor</code></li><li>REQUIRES_NEW everywhere → too many commits, harder locks</li><li>Long tx holding DB connections / row locks</li><li>Calling @Transactional on a non-Spring bean</li></ul></div>
<div class="box c8"><h2>8. Isolation (quick)</h2><table class="tbl"><tr><th>Level</th><th>Allows</th></tr><tr><td>READ_UNCOMMITTED</td><td>dirty reads</td></tr><tr><td>READ_COMMITTED</td><td>no dirty (common default)</td></tr><tr><td>REPEATABLE_READ</td><td>stable rows in tx</td></tr><tr><td>SERIALIZABLE</td><td>full isolation, slowest</td></tr></table><div class="note">Set via isolation = Isolation.READ_COMMITTED</div></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">9a. Decision flow</h2><div class="flow" style="flex-wrap:wrap;row-gap:4px"><span class="pill">need atomic?</span><span class="arr">→</span><span class="pill">Transactional</span><span class="arr">→</span><span class="pill">audit must survive?</span><span class="arr">→</span><span class="pill">REQUIRES_NEW</span><span class="arr">→</span><span class="pill">checked fail?</span><span class="arr">→</span><span class="pill">rollbackFor</span></div></div>
<div class="box iq"><h2>9b. Interview Qs</h2><ol><li>Why does self-invocation skip the transaction?</li><li>REQUIRED vs REQUIRES_NEW?</li><li>Why checked exceptions don&apos;t roll back by default?</li><li>What does readOnly=true actually do?</li><li>How would you roll back on a checked Exception?</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">9c. Key points</h2><ul><li>Proxy = magic</li><li>Default = RuntimeException</li><li>Call via bean</li></ul></div>
</div></div>'''
build("/workspace/social/posts/2026-10-17-instagram-spring-boot-transactions",B,1350,"@the_codez.rahulrai")

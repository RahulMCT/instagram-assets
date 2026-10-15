import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:19px;line-height:1.28}.box li code,.box p code{font-size:15.5px;font-family:monospace;background:#efeae0;padding:0 3px;border-radius:3px}.box h2{font-size:23.5px;margin-bottom:4px}.code{font-size:15px;line-height:1.36}.tbl{font-size:17px}.tbl th,.tbl td{padding:4px 6px}.iq ol{font-size:18px;line-height:1.32}.pill{font-size:14.5px}.grid{gap:10px}.handle{bottom:-12px}.box{padding:10px 12px}.tagline{font-size:19px;margin-bottom:8px}.note{font-size:15.5px}</style>
<div class="title">🔒 JavaScript Closures <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">A function that remembers the variables from the scope where it was created — even after that scope is gone.</div>
<div class="grid">
<div class="box c1"><h2>1. What &amp; why</h2><ul><li>A <b>closure</b> = function + its lexical environment</li><li>Inner function can read/write outer locals after outer returns</li><li>Powers: private state, callbacks, factories, React hooks</li><li>Not a special keyword — every function can close over vars</li></ul></div>
<div class="box c2"><h2>2. Minimal example</h2><div class="code">function makeCounter() {
  let count = 0;          // private
  return function() {
    count += 1;
    return count;
  };
}
const c = makeCounter();
c(); // 1
c(); // 2</div><div class="note">count lives on even though makeCounter finished.</div></div>
<div class="box c3"><h2>3. Lexical scope</h2><ul><li>Scope is decided by <b>where</b> the function is written, not where it is called</li><li>Lookup walks outer → outer → global</li><li>Shadowing: inner <code>let x</code> hides outer <code>x</code></li><li>Closure captures the <b>binding</b> (live value), not a snapshot</li></ul></div>
<div class="box c4"><h2>4. Data privacy pattern</h2><div class="code">function bank(start) {
  let balance = start;
  return {
    deposit(n) { balance += n; },
    get() { return balance; }
  };
}
const a = bank(100);
a.deposit(50);
a.get(); // 150
// balance is not a.get.balance</div></div>
<div class="box c5"><h2>5. Classic loop trap</h2><div class="code">// BAD with var
for (var i = 0; i &lt; 3; i++) {
  setTimeout(() =&gt; console.log(i), 0);
}
// logs 3, 3, 3

// FIX: let (new binding each iter)
for (let i = 0; i &lt; 3; i++) {
  setTimeout(() =&gt; console.log(i), 0);
}
// 0, 1, 2</div></div>
<div class="box c6"><h2>6. Factory / partial apply</h2><div class="code">function multiply(a) {
  return (b) =&gt; a * b;
}
const double = multiply(2);
double(5); // 10

// same idea: debounce, once(),
// memoize, event handlers with config</div><ul><li>Currying = closures stacked</li></ul></div>
<div class="box c7"><h2>7. Common mistakes</h2><ul><li>Expecting a frozen copy — outer var can still change</li><li><code>var</code> in loops sharing one binding</li><li>Accidental retention: big objects closed over → memory leaks</li><li>Thinking arrow vs function changes closure (it doesn&apos;t; only <code>this</code>)</li><li>Returning object methods without binding and blaming closures</li></ul></div>
<div class="box c8"><h2>8. Closures vs this</h2><table class="tbl"><tr><th>Topic</th><th>Closures</th><th>this</th></tr><tr><td>Decided by</td><td>write site (lexical)</td><td>call site (mostly)</td></tr><tr><td>Arrow fn</td><td>same (closes over vars)</td><td>lexical this</td></tr><tr><td>Use for</td><td>private state / config</td><td>object methods</td></tr></table><div class="note" style="margin-top:4px">Don&apos;t mix them up in interviews.</div></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">9a. Mental model</h2><div class="flow"><span class="pill">outer runs</span><span class="arr">→</span><span class="pill">locals created</span><span class="arr">→</span><span class="pill">inner returned</span><span class="arr">→</span><span class="pill">outer done</span><span class="arr">→</span><span class="pill">inner still sees locals</span></div><div class="note" style="margin-top:6px">Engine keeps the environment alive while any closed-over function references it.</div></div>
<div class="box iq"><h2>9b. Interview Qs</h2><ol><li>What is a closure in one sentence?</li><li>Why does var in a loop print the last value?</li><li>How do closures enable privacy?</li><li>Snapshot or live binding?</li><li>When can closures cause leaks?</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">9c. Key points</h2><ul><li>Function + env</li><li>Live bindings</li><li>Prefer let in loops</li></ul></div>
</div></div>'''
build("/workspace/social/posts/2026-10-15-instagram-js-closures",B,1350,"@the_codez.rahulrai")

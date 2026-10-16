import sys; sys.path.insert(0,"/workspace/social/posts"); from build10 import build
B=r'''<style>.box p,.box li{font-size:17.5px;line-height:1.24}.box li code,.box p code{font-size:15px;font-family:monospace;background:#efeae0;padding:0 3px;border-radius:3px}.box h2{font-size:22px;margin-bottom:3px}.code{font-size:13.5px;line-height:1.28}.tbl{font-size:16px}.tbl th,.tbl td{padding:3px 6px}.iq ol{font-size:16.5px;line-height:1.24}.pill{font-size:14px}.grid{gap:8px}.handle{bottom:-12px}.box{padding:9px 11px}.tagline{font-size:18.5px;margin-bottom:7px}.note{font-size:15px}</style>
<div class="title">🪟 SQL Window Functions <span class="badge">CHEAT SHEET</span></div>
<div class="tagline">Calculate across related rows WITHOUT collapsing them — rankings, running totals, prev/next. (MySQL 8+, PostgreSQL, Oracle, SQL Server)</div>
<div class="grid">
<div class="box c1"><h2>1. What &amp; why</h2><ul><li>A function + <code>OVER()</code> = works on a <b>window</b> of rows</li><li>Every input row stays in the output</li><li>Use for: rank, top-N per group, running total, compare with previous row</li><li>Replaces messy self-joins &amp; subqueries</li></ul></div>
<div class="box c2"><h2>2. Syntax</h2><div class="code">func(...) OVER (
  PARTITION BY dept     -- groups
  ORDER BY salary DESC  -- order inside
  ROWS BETWEEN UNBOUNDED PRECEDING
       AND CURRENT ROW  -- frame
)</div><div class="note">All 3 parts are optional. Empty OVER() = whole result is one window.</div></div>
<div class="box c3"><h2>3. GROUP BY vs OVER</h2><table class="tbl"><tr><th></th><th>GROUP BY</th><th>OVER()</th></tr><tr><td>Rows out</td><td>1 per group</td><td>all rows kept</td></tr><tr><td>Detail cols</td><td>must be grouped</td><td>free to select</td></tr><tr><td>Example</td><td>dept avg only</td><td>each emp + dept avg</td></tr></table><div class="code" style="margin-top:5px">SELECT name, dept, salary,
  AVG(salary) OVER (PARTITION BY dept)
    AS dept_avg
FROM emp;</div></div>
<div class="box c4"><h2>4. ROW_NUMBER vs RANK vs DENSE_RANK</h2><table class="tbl"><tr><th>salary</th><th>ROW_NUMBER</th><th>RANK</th><th>DENSE_RANK</th></tr><tr><td>900</td><td>1</td><td>1</td><td>1</td></tr><tr><td>800</td><td>2</td><td>2</td><td>2</td></tr><tr><td>800</td><td>3</td><td>2</td><td>2</td></tr><tr><td>700</td><td>4</td><td><b>4</b></td><td><b>3</b></td></tr></table><ul><li>RANK leaves gaps after ties; DENSE_RANK doesn&apos;t</li><li>ROW_NUMBER is always unique</li></ul></div>
<div class="box c5"><h2>5. Top-N per group</h2><div class="code">-- 2nd highest salary in each dept
WITH r AS (
  SELECT name, dept, salary,
    DENSE_RANK() OVER (
      PARTITION BY dept
      ORDER BY salary DESC) AS rk
  FROM emp
)
SELECT name, dept, salary
FROM r
WHERE rk = 2;</div><div class="note">Filter in the outer query — not inside the same SELECT.</div></div>
<div class="box c6"><h2>6. Running total + LAG</h2><div class="code">SELECT order_date, amount,
  SUM(amount) OVER (ORDER BY order_date)
    AS running_total,
  LAG(amount) OVER (ORDER BY order_date)
    AS prev_amount,
  amount - LAG(amount)
    OVER (ORDER BY order_date) AS diff
FROM orders;</div><ul><li><code>LEAD()</code> = next row · first LAG = NULL</li></ul></div>
<div class="box c7"><h2>7. Common mistakes</h2><ul><li>Using a window fn in <code>WHERE</code> / <code>GROUP BY</code> → error; wrap in CTE</li><li>Forgetting <code>PARTITION BY</code> → ranks whole table</li><li>ROW_NUMBER with ties and no tiebreaker → random order</li><li>Default frame with ORDER BY is <b>RANGE</b> → same-date rows summed together</li><li><code>LAST_VALUE</code> returns current row unless frame goes to <code>UNBOUNDED FOLLOWING</code></li></ul></div>
<div class="box c8"><h2>8. Where it runs</h2><div class="flow" style="flex-wrap:wrap;row-gap:5px"><span class="pill">FROM / JOIN</span><span class="arr">→</span><span class="pill">WHERE</span><span class="arr">→</span><span class="pill">GROUP BY</span><span class="arr">→</span><span class="pill">HAVING</span><span class="arr">→</span><span class="pill">WINDOW fns</span><span class="arr">→</span><span class="pill">SELECT</span><span class="arr">→</span><span class="pill">ORDER BY</span><span class="arr">→</span><span class="pill">LIMIT</span></div><ul style="margin-top:5px"><li>That&apos;s why WHERE can&apos;t see them</li><li>But ORDER BY can use the alias</li></ul></div>
<div class="bottom">
<div class="box" style="border-color:#1a5f7a"><h2 style="color:#1a5f7a">9a. How a window is built</h2><div class="flow"><span class="pill">rows</span><span class="arr">→</span><span class="pill">PARTITION BY (split)</span><span class="arr">→</span><span class="pill">ORDER BY (sort)</span><span class="arr">→</span><span class="pill">frame</span><span class="arr">→</span><span class="pill">value per row</span></div><div class="note" style="margin-top:6px">Ranking fns ignore the frame; aggregates (SUM, AVG) and FIRST/LAST_VALUE use it.</div></div>
<div class="box iq"><h2>9b. Interview Qs</h2><ol><li>RANK vs DENSE_RANK vs ROW_NUMBER?</li><li>Find 2nd highest salary per dept.</li><li>Window fn vs GROUP BY?</li><li>Why not in WHERE?</li><li>Month-over-month change with LAG?</li></ol></div>
<div class="box" style="border-color:#2d8a5a"><h2 style="color:#2d8a5a">9c. Key points</h2><ul><li>Rows not collapsed</li><li>Filter via CTE</li><li>Mind the frame</li></ul></div>
</div></div>'''
build("/workspace/social/posts/2026-10-16-instagram-sql-window-functions",B,1350,"@the_codez.rahulrai")

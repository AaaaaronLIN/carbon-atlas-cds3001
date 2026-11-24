#!/usr/bin/env python3
"""Build the 'final front end' PDF report (HTML -> Chrome printToPDF).

Run:
    python3 make_report.py
    python3 shot.py --url file://.../out/pdf/report.html --pdf --out ../out/pdf/Carbon_Compass_Final_Frontend.pdf
"""
import base64
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "out", "screenshots")
OUT = os.path.join(ROOT, "out", "pdf")
os.makedirs(OUT, exist_ok=True)


def data_uri(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def img(name, cls="", style=""):
    return f'<img class="{cls}" style="{style}" src="{data_uri(os.path.join(SHOTS, name))}" alt="">'


# mobile: keep the first ~1150 CSS px so the page shows the phone layout
mobile = os.path.join(SHOTS, "mobile-2.0-full.png")
mob_crop = os.path.join(SHOTS, "mobile-2.0-top.png")
with Image.open(mobile) as im:
    w, h = im.size
    im.crop((0, 0, w, min(h, 2000))).save(mob_crop)

LOGO = """<svg width="46" height="46" viewBox="0 0 40 40" aria-hidden="true" style="display:block">
<circle cx="20" cy="20" r="18.2" fill="none" stroke="#16211C" stroke-opacity=".22" stroke-width="1.3"/>
<path d="M20 5.6l4.9 14.1L20 17.1l-4.9 2.6z" fill="#0E7C5A"/>
<path d="M20 34.4l-4.9-14.1 4.9 2.6 4.9-2.6z" fill="#16211C" opacity=".72"/>
<circle cx="20" cy="20" r="1.9" fill="#F6F3EC" stroke="#16211C" stroke-width="1.2"/></svg>"""

PAGES = []


def page(inner):
    PAGES.append(inner)


# --------------------------------------------------------------------- cover
page(f"""
<div class="brandbar"><span>CDS3001 · Databases &amp; Data Warehouses</span><span>Group Project · Part 3</span></div>
<div class="cover">
  <div class="logo-row">{LOGO}<span>Data Fanatics · Carbon Atlas</span></div>
  <p class="kicker">Final front end · submission PDF</p>
  <h1>Carbon<br>Compass</h1>
  <p class="cover-lede">A decision brief on global CO<sub>2</sub> emissions. Carbon Monitor data
  is stored in MySQL, exposed as JSON by our Flask API, and read by this single web page.</p>
  <p class="cover-tagline">See every tonne. Cut what matters.</p>
  <div class="statline">
    <div><b>655,200</b><span>rows in MySQL</span></div>
    <div><b>39</b><span>countries / regions</span></div>
    <div><b>6</b><span>sectors</span></div>
    <div><b>2019–2026</b><span>daily coverage</span></div>
  </div>
  <table class="meta">
    <tr><th>Product</th><td>Carbon Atlas — Global Carbon Brief</td></tr>
    <tr><th>Team</th><td>Data Fanatics · Lingnan University · CDS3001</td></tr>
    <tr><th>Data</th><td>Carbon Monitor daily CO₂ estimates · MtCO₂ per day · fair-use open data (Sci Data 7, 392 (2020), doi:10.1038/s41597-020-00708-7)</td></tr>
    <tr><th>Stack</th><td>MySQL 8 → Flask + PyMySQL → HTML + Apache ECharts (bundled locally)</td></tr>
    <tr><th>Run</th><td><code>python3 app.py</code> → <code>http://127.0.0.1:5001/</code></td></tr>
  </table>
  <div class="cover-peek">{img("stage-hero-2.0.png", "peek")}</div>
  <p class="cover-foot">Prepared 18 November 2026 · Screenshots of the running interface · Every number shown is computed by SQL at request time, not hard-coded.</p>
</div>
""")

# --------------------------------------------------------------------- 01 at a glance
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>01 · At a glance</span></div>
<h2>The brief at a glance</h2>
<p class="lede">One scrolling page answers five questions in order — <b>Where</b> do emissions come from,
<b>What</b> activity produces them, <b>When</b> did they move, <b>What</b> do the numbers say, and
<b>How</b> is the data governed. The scope controls re-query the API and redraw every panel.</p>
{img("hero-day-2.0.png", "shot")}
<div class="notes">
  <div><b>Live status, not a claim.</b> The pill reads <code>/api/health</code>: the row count and last date
  come from MySQL, and it turns red if the database is unreachable.</div>
  <div><b>Honest comparison.</b> The change figure compares the same months of 2019, so the partial 2026
  year can never look like a collapse.</div>
  <div><b>Meaning before charts.</b> The headline sentence states the number, the comparison and the
  largest sector before any chart is shown.</div>
</div>
<h3>The pipeline behind the page</h3>
<div class="pipe">
  <div><span>1</span><b>Carbon Monitor CSV</b><small>daily CO₂ by country and sector</small></div>
  <div><span>2</span><b>MySQL 8</b><small><code>carbon_lab.carbon_emission</code><br>655,200 rows</small></div>
  <div><span>3</span><b>Flask API</b><small>9 routes returning JSON<br>port 5001</small></div>
  <div><span>4</span><b>This page</b><small>HTML + Apache ECharts<br>assets bundled locally</small></div>
</div>
""")

# --------------------------------------------------------------------- 02 where
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>02 · Where</span></div>
<h2>Where emissions come from</h2>
<p class="lede">A world choropleth and a sortable ranking table share the same year. Clicking a country on
either one focuses the whole brief on it: the KPI strip, sector bars and weekly rhythm all re-query.</p>
{img("where-2.0.png", "shot")}
<div class="bullets">
  <div><b>Table, not just charts.</b> Rank, annual total, share of the world, like-for-like change since 2019
  and a seven-year sparkline — sortable, exportable, keyboard-focusable.</div>
  <div><b>One payload, two views.</b> Map and table both read <code>/api/country_year</code>, so the number in
  the table can never disagree with the map beside it.</div>
  <div><b>Aggregates are labelled.</b> WORLD, EU27 and ROW are aggregates, not countries, and are kept out of
  the country ranking.</div>
</div>
<h3>What the page receives (excerpt)</h3>
<pre class="code">GET /api/country_year
[ {{"country": "China",           "year": 2025, "total": 12089.14, "days": 365}},
  {{"country": "United States",   "year": 2025, "total":  5036.11, "days": 365}},
  ... ]

SELECT country, YEAR(date) AS year, ROUND(SUM(value), 2) AS total,
       COUNT(DISTINCT date) AS days
FROM carbon_emission GROUP BY country, year;</pre>
""")

# --------------------------------------------------------------------- 03 what
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>03 · What</span></div>
<h2>What activity produces the emissions</h2>
<p class="lede">Six sectors, measured every day. Power and industry hold roughly two thirds of the total;
the weekday view shows the rhythm that commuting and industrial work impose on the rest.</p>
{img("what-2.0.png", "shot")}
<div class="notes">
  <div><b>Sector bars.</b> Value and share are printed on every bar, and the two leading sectors are named
  in the takeaway underneath.</div>
  <div><b>Weekly rhythm.</b> Daily estimates are averaged by weekday, never by month, so the weekend dip is
  visible; bars start at zero to avoid exaggerating it.</div>
  <div><b>Follows the selection.</b> Change the country in the scope control and both panels re-query
  (<code>/api/sectors</code> and <code>/api/daily</code>).</div>
</div>
<h3>Why the rhythm matters for the argument</h3>
<p class="small">A country total is an average over very different days. Showing the weekly shape makes the
point that emissions are driven by activity cycles — and it is a pattern the reference dashboard does not
show. It also lets us explain the weekend dip without claiming a policy effect.</p>
<h3>What the page receives (excerpt)</h3>
<pre class="code">GET /api/sectors?country=WORLD&amp;year=2025
[ {{"sector": "Power",    "total": 13491.80}},
  {{"sector": "Industry", "total": 12664.11}}, ... ]

SELECT sector, ROUND(SUM(value), 2) AS total
FROM carbon_emission
WHERE country = 'WORLD' AND YEAR(date) = 2025
GROUP BY sector ORDER BY total DESC;</pre>
""")

# --------------------------------------------------------------------- 04 when
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>04 · When</span></div>
<h2>How emissions move through time</h2>
<p class="lede">Monthly totals from January 2019 to the latest complete month. The 2020 collapse and the
rebound are visible without smoothing. A second country can be overlaid, in absolute terms or indexed to
2019 = 100 so different sizes can be compared by shape.</p>
{img("when-2.0.png", "shot")}
<div class="notes">
  <div><b>Annotated, not decorated.</b> The COVID-19 window is marked as a region; the line itself is left
  untouched so the data is not smoothed away.</div>
  <div><b>Fair comparison.</b> <i>Index · 2019 = 100</i> puts China and India on one scale; each line is
  divided by its own 2019 average month.</div>
  <div><b>Zoom and export.</b> The slider narrows the window; the takeaway always names the lowest and
  highest month in the current view.</div>
</div>
<h3>How the index is computed</h3>
<pre class="code">// each line is divided by its own 2019 average month, then multiplied by 100
const base2019 = rows2019.reduce((sum, row) => sum + row.total, 0) / rows2019.length;
const indexed  = rows.map(row => 100 * row.total / base2019);</pre>
<p class="small">No smoothing, no moving average, no truncated axis: the raw monthly totals are what is drawn.
The annotation is a shaded region, not a changed line, so the reader can still see April 2020 for what it is.</p>
""")

# --------------------------------------------------------------------- 05 findings
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>05 · Findings</span></div>
<h2>What the numbers say</h2>
<p class="lede">Six readings are computed from the database on every request. They are the slide-ready
summary of the charts — and because they are generated, they cannot drift out of date.</p>
{img("findings-2.0.png", "shot")}
<h3>How each finding is produced</h3>
<table class="ev">
  <tr><td>2020 shock</td><td><code>GROUP BY month</code> over 2020 vs April 2019 — the lowest month in the dataset.</td></tr>
  <tr><td>Rebound</td><td>Annual world totals; 2021 vs 2020 and 2025 vs 2019.</td></tr>
  <tr><td>Two sectors</td><td>Latest complete year, sector totals with shares (<code>/api/insights</code>).</td></tr>
  <tr><td>One country</td><td>Country total ÷ world total for 2025.</td></tr>
  <tr><td>Biggest mover</td><td>Self-join of 2025 and 2024 country totals, emitters above 100 MtCO₂.</td></tr>
  <tr><td>2026 so far</td><td>January–August 2026 vs the same months of 2019 (never a full year).</td></tr>
</table>
<h3>What to say when this is on screen</h3>
<div class="bullets">
  <div><b>Lead with the human fact.</b> "April 2020 was the quietest month in the whole dataset — 14% below
  the same month a year earlier."</div>
  <div><b>Then the structure.</b> "By 2025 the world was 4% above 2019, and two sectors still account for
  69% of everything."</div>
  <div><b>Then the caveat.</b> "2026 is only eight months, so we compare it with the same eight months of
  2019 — never with a full year."</div>
</div>
""")

# --------------------------------------------------------------------- 06 method
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>06 · Method &amp; responsibility</span></div>
<h2>Method, provenance &amp; responsibility</h2>
<p class="lede">A dashboard is an argument about what counts. The page states where the data comes from,
what it cannot tell you, and how the system is governed — using the GELSI framework from Lecture 19.</p>
{img("method-2.0.png", "shot")}
""")

# --------------------------------------------------------------------- 07b stage + team
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>07 · Presentation mode &amp; team</span></div>
<h2>Built for the room — and for the record</h2>
<p class="lede">The same brief has two modes: a <b>Stage</b> theme for projection (deep ink, ivory and gold) and a
<b>Day</b> theme for print and review. The team that built the pipeline is on the page, with roles and student IDs.</p>
{img("story-2.0.png", "shot")}
<p class="cap"><b>Play the brief.</b> A guided tour of the same panels: 2019, the 2020 shock, the 2025 rebound,
a focus on China and the United States, then an indexed comparison — ending on the six findings.</p>
{img("team-2.0.png", "shot")}
<p class="cap"><b>Data Fanatics.</b> Five students, five roles: host and story, database and cost–benefit, API and GELSI,
front end and live demo, insights and campaign. The dashboard has a Team section with the same cards.</p>
""")

# --------------------------------------------------------------------- 07 integrity + customisation
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>08 · Integrity &amp; customisation</span></div>
<h2>Handling a partial year honestly</h2>
<p class="lede">The dataset ends on 31 August 2026. Summing a half-finished year and comparing it with a
full 2019 would manufacture a 31% "fall". The interface refuses to do that.</p>
{img("hero-2026-2.0.png", "shot small")}
<div class="notes">
  <div><b>Every label says so.</b> "Emissions · Jan–Aug 2026", "partial year", and a note under the table.</div>
  <div><b>The baseline changes with the period.</b> <code>/api/country_ytd</code> compares January–August 2026
  with January–August 2019 — one place in the code owns that rule.</div>
  <div><b>Same rule for rankings.</b> The "vs 2019" column follows the selected period.</div>
</div>
<h3>What we changed relative to the reference dashboard</h3>
<table class="cmp">
  <tr><th></th><th>Reference bonus dashboard</th><th>Carbon Atlas</th></tr>
  <tr><td>Look</td><td>dark neon, glass cards</td><td>Stage theme + light editorial brief, serif headlines</td></tr>
  <tr><td>Structure</td><td>a wall of widgets</td><td>five ordered questions</td></tr>
  <tr><td>Table</td><td>none</td><td>sortable ranking + sparklines + CSV</td></tr>
  <tr><td>Compare</td><td>one country at a time</td><td>overlay + index to 2019 = 100</td></tr>
  <tr><td>Interpretation</td><td>charts only</td><td>auto-generated findings</td></tr>
  <tr><td>Ethics</td><td>not addressed</td><td>GELSI panel + stated limits</td></tr>
  <tr><td>Assets</td><td>CDN</td><td>bundled locally, works offline</td></tr>
</table>
""")

# --------------------------------------------------------------------- 08 access
page(f"""
<div class="brandbar"><span>Carbon Atlas</span><span>09 · Access &amp; reproduce</span></div>
<h2>Accessible, and reproducible in five steps</h2>
<div class="two">
  <div>
    <h3>Accessibility</h3>
    <ul class="decisions">
      <li>Single-column layout at phone widths; no horizontal scrolling.</li>
      <li>Keyboard-operable controls and table rows; visible focus rings; a skip link.</li>
      <li>Contrast-checked ink/paper palette; never colour-only encoding.</li>
      <li><code>prefers-reduced-motion</code> turns animation off.</li>
      <li>Light theme prints and projects legibly.</li>
    </ul>
    <h3>Run it</h3>
    <ol class="decisions">
      <li>Start MySQL; run <code>Part_1_setup.sql</code> (creates the table and imports the CSV).</li>
      <li><code>python3 -m pip install -r requirements.txt</code></li>
      <li>Put your MySQL password in <code>app.py</code> (or set <code>DB_PASSWORD</code>).</li>
      <li><code>python3 app.py</code> → <code>http://127.0.0.1:5001/</code></li>
      <li>Open <code>/api/sectors</code> to see the JSON behind the charts.</li>
    </ol>
    <h3>API routes</h3>
    <p class="api">
      <code>/api/sectors</code> · <code>/api/monthly</code> · <code>/api/country_year</code> ·
      <code>/api/country_ytd</code> · <code>/api/daily</code> · <code>/api/compare</code> ·
      <code>/api/insights</code> · <code>/api/health</code> · <code>/api/meta</code>
    </p>
    <h3>What we would build next</h3>
    <ul class="decisions">
      <li>A per-capita view once a population column is joined in — deliberately not faked now.</li>
      <li>Saved views and a scheduled email digest for analysts.</li>
      <li>Server-side export and caching for larger datasets.</li>
    </ul>
  </div>
  <div class="phone-wrap">{img("mobile-2.0-top.png", "phone")}
    <p class="cap">Phone layout at 390 px: single column, controls stay reachable.</p>
  </div>
</div>
<h3>Demo checklist — what we show, in order</h3>
<table class="ev">
  <tr><td>1 · MySQL</td><td><code>SELECT COUNT(*)</code> and <code>MIN/MAX(date)</code> — the data is in the table, not in the CSV.</td></tr>
  <tr><td>2 · JSON</td><td>Open <code>/api/sectors</code> and <code>/api/monthly</code> in the browser.</td></tr>
  <tr><td>3 · Page</td><td>Open <code>127.0.0.1:5001</code> — served by the same Flask process, not <code>file://</code>.</td></tr>
  <tr><td>4 · Focus</td><td>Click a country on the map: four panels re-query.</td></tr>
  <tr><td>5 · Partial year</td><td>Switch to 2026: labels become "Jan–Aug", comparison stays like-for-like.</td></tr>
  <tr><td>6 · Compare</td><td>Overlay a second country and switch to <i>Index · 2019 = 100</i>.</td></tr>
</table>
<p class="endnote">Data Fanatics · CDS3001 Group Project · Part 1 MySQL · Part 2 Flask API ·
Part 3 ECharts. Data: Carbon Monitor, fair-use open data, cite Sci Data 7, 392 (2020), doi:10.1038/s41597-020-00708-7.</p>
""")

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
  background: #F6F3EC; color: #16211C;
  font-family: -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  font-size: 9.2pt; line-height: 1.5;
}
.page {
  width: 210mm; min-height: 297mm; padding: 13mm 15mm 12mm;
  page-break-after: always; position: relative; overflow: hidden; background: #F6F3EC;
}
.page:last-child { page-break-after: auto; }
.brandbar {
  display: flex; justify-content: space-between; align-items: baseline;
  border-bottom: 1px solid #DED9CC; padding-bottom: 4mm; margin-bottom: 7mm;
  font-family: "SF Mono", ui-monospace, Menlo, monospace; font-size: 6.6pt;
  letter-spacing: .16em; text-transform: uppercase; color: #5E6B63;
}
h1 { font-family: "Iowan Old Style", Palatino, Georgia, serif; font-weight: 400;
     font-size: 42pt; line-height: .95; letter-spacing: -.02em; margin: 0; }
h2 { font-family: "Iowan Old Style", Palatino, Georgia, serif; font-weight: 400;
     font-size: 21pt; line-height: 1.1; letter-spacing: -.01em; margin: 0 0 3mm; }
h3 { font-size: 9.4pt; font-weight: 700; margin: 5.5mm 0 2mm; }
p { margin: 0 0 2.5mm; }
.small { font-size: 8.8pt; color: #3B4A43; }
.lede { font-size: 9.6pt; color: #3B4A43; max-width: 165mm; margin-bottom: 5mm; }
.kicker { font-family: "SF Mono", ui-monospace, monospace; font-size: 7pt; letter-spacing: .2em;
          text-transform: uppercase; color: #0A5943; margin: 0 0 5mm; }
.cover { padding-top: 2mm; }
.logo-row { display: flex; align-items: center; gap: 3mm; margin-bottom: 8mm;
            font-family: "SF Mono", ui-monospace, monospace; font-size: 6.8pt;
            letter-spacing: .14em; text-transform: uppercase; color: #5E6B63; }
.cover-lede { font-size: 11pt; line-height: 1.45; color: #3B4A43; max-width: 148mm; margin: 5mm 0 4mm; }
.cover-tagline { font-family: "Iowan Old Style", Palatino, Georgia, serif; font-style: italic;
                 font-size: 16pt; color: #0E7C5A; margin: 0 0 7mm; }
.statline { display: flex; gap: 6mm; border-top: 1.2pt solid #16211C; border-bottom: 1px solid #DED9CC;
            padding: 3.5mm 0; margin-bottom: 6mm; }
.statline div { flex: 1; }
.statline b { display: block; font-family: "Iowan Old Style", Palatino, Georgia, serif;
              font-size: 18pt; font-weight: 400; letter-spacing: -.01em; }
.statline span { font-family: "SF Mono", ui-monospace, monospace; font-size: 6.2pt;
                 text-transform: uppercase; letter-spacing: .1em; color: #5E6B63; }
table.meta { width: 100%; border-collapse: collapse; font-size: 8.5pt; }
table.meta th { text-align: left; width: 24mm; font-family: "SF Mono", ui-monospace, monospace;
                font-size: 6.4pt; letter-spacing: .1em; text-transform: uppercase; color: #5E6B63;
                font-weight: 500; padding: 1.9mm 4mm 1.9mm 0; vertical-align: top;
                border-bottom: 1px solid #EAE5D9; }
table.meta td { padding: 1.9mm 0; border-bottom: 1px solid #EAE5D9; color: #3B4A43; }
.cover-peek { margin-top: 7mm; }
.cover-peek img { width: 100%; height: 62mm; object-fit: cover; object-position: top;
                  border: 1px solid #DED9CC; display: block; }
.cover-foot { position: absolute; left: 15mm; right: 15mm; bottom: 11mm;
              font-family: "SF Mono", ui-monospace, monospace; font-size: 6.2pt;
              letter-spacing: .06em; color: #5E6B63; border-top: 1px solid #DED9CC; padding-top: 2.5mm; }
.shot { display: block; width: 100%; border: 1px solid #DED9CC; background: #FFFDF8; }
.shot.small { width: 86%; margin: 0 auto; }
.cap { font-size: 8.2pt; color: #3B4A43; margin-top: 2.5mm; }
.two { display: flex; gap: 7mm; align-items: flex-start; }
.two > div:first-child { flex: 1; min-width: 0; }
.two > div:last-child { flex: 0 0 62mm; }
.notes { display: flex; gap: 5mm; margin-top: 4.5mm; }
.notes > div { flex: 1; font-size: 8.1pt; color: #3B4A43; border-top: 2pt solid #0E7C5A; padding-top: 2.4mm; }
.notes b { display: block; color: #16211C; font-size: 8.5pt; margin-bottom: 1mm; }
.bullets { margin-top: 4mm; }
.bullets > div { border-top: 1px solid #DED9CC; padding: 2.2mm 0; font-size: 8.6pt; color: #3B4A43; }
.bullets b { color: #16211C; }
ul.decisions, ol.decisions { margin: 0; padding-left: 4.5mm; font-size: 8.5pt; color: #3B4A43; }
ul.decisions li, ol.decisions li { margin-bottom: 1.5mm; }
code { font-family: "SF Mono", ui-monospace, Menlo, monospace; font-size: .92em;
       background: #F1EDE2; padding: .2mm 1mm; border-radius: 1px; }
pre.code { font-family: "SF Mono", ui-monospace, Menlo, monospace; font-size: 7.2pt; line-height: 1.65;
           background: #FFFDF8; border: 1px solid #DED9CC; padding: 3mm 4mm; margin: 2mm 0 0;
           white-space: pre-wrap; color: #3B4A43; }
.pipe { display: flex; gap: 2mm; margin-top: 1mm; }
.pipe > div { flex: 1; background: #FFFDF8; border: 1px solid #DED9CC; border-top: 2.5pt solid #0E7C5A;
              padding: 2.5mm 2.5mm 2.8mm; position: relative; min-width: 0; }
.pipe > div + div::before { content: "→"; position: absolute; left: -3.6mm; top: 50%;
                            transform: translateY(-50%); color: #0E7C5A; font-size: 10pt; }
.pipe span { font-family: "SF Mono", ui-monospace, monospace; font-size: 6.2pt; color: #0E7C5A;
             letter-spacing: .1em; display: block; margin-bottom: 1mm; }
.pipe b { display: block; font-size: 8.4pt; color: #16211C; margin-bottom: .8mm; }
.pipe small { font-size: 7pt; color: #5E6B63; line-height: 1.35; display: block; }
table.ev { width: 100%; border-collapse: collapse; font-size: 8.2pt; }
table.ev td { border-bottom: 1px solid #EAE5D9; padding: 1.9mm 0; vertical-align: top; color: #3B4A43; }
table.ev td:first-child { width: 24mm; font-family: "SF Mono", ui-monospace, monospace; font-size: 7pt;
                          color: #0A5943; font-weight: 600; letter-spacing: .02em; padding-right: 4mm; }
table.cmp { width: 100%; border-collapse: collapse; font-size: 8.1pt; margin-top: 2mm; }
table.cmp th { text-align: left; font-family: "SF Mono", ui-monospace, monospace; font-size: 6.3pt;
               letter-spacing: .09em; text-transform: uppercase; color: #5E6B63; font-weight: 500;
               border-bottom: 1px solid #DED9CC; padding: 1.8mm 3mm 1.8mm 0; }
table.cmp td { border-bottom: 1px solid #EAE5D9; padding: 1.6mm 3mm 1.6mm 0; color: #3B4A43; }
table.cmp td:first-child { font-family: "SF Mono", ui-monospace, monospace; font-size: 7.2pt;
                           color: #0A5943; font-weight: 600; width: 20mm; }
.phone-wrap { text-align: center; }
img.phone { width: 58mm; border: 1px solid #DED9CC; display: inline-block; }
.api { font-family: "SF Mono", ui-monospace, monospace; font-size: 7pt; line-height: 1.95; color: #3B4A43; }
.api code { background: none; padding: 0; color: #0A5943; }
.endnote { margin-top: 5mm; font-family: "SF Mono", ui-monospace, monospace; font-size: 6.4pt;
           line-height: 1.7; color: #5E6B63; border-top: 1px solid #DED9CC; padding-top: 2.5mm; }
"""

html = ("<!DOCTYPE html><html><head><meta charset='utf-8'><style>" + CSS +
        "</style></head><body>" +
        "".join('<div class="page">' + p + "</div>" for p in PAGES) + "</body></html>")

out_html = os.path.join(OUT, "report.html")
with open(out_html, "w") as f:
    f.write(html)
print("wrote", out_html, len(html), "bytes;", len(PAGES), "pages")

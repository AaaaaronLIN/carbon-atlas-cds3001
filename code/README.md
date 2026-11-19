# Carbon Atlas — Global CO₂ Brief

**CDS3001 Databases and Data Warehouses · Group Project (Parts 1–3)**
Data Fanatics · Carbon Monitor open data · MySQL → Flask API → one web page.

> **What it is.** A decision brief on global CO₂ emissions: where the emissions come from,
> what activity produces them, how they have moved since 2019, and what the numbers cannot tell you.
> Every figure is computed by SQL against the MySQL table and fetched live by the page.

---

## 1. Architecture

```
Carbon Monitor CSV                MySQL 8                      Flask (app.py)              Browser (index.html)
daily CO₂, 40 countries,    →   carbon_lab.carbon_emission  →   /api/*  → JSON         →   HTML + Apache ECharts
6 sectors, MtCO₂/day            ~655,200 rows, 2019–2026         port 5001                    map, table, charts
```

| Part | What the marker must see | Where it lives |
|---|---|---|
| **Part 1** | CSV imported into MySQL with `LOAD DATA`; row count / date range checked | `Part_1_setup.sql` |
| **Part 2** | A running API that turns SQL into JSON | `app.py` (+ `requirements.txt`, `API_reference.md`) |
| **Part 3** | A web page that fetches that API and draws charts/tables | `index.html` + `static/` |

---

## 2. Run it from scratch (5 steps)

1. **Start MySQL** (macOS: *System Settings → MySQL → Start*; Windows: *services.msc → MySQL80 → Start*).
2. **Import the data.** Download the Carbon Monitor CSV, open the MySQL client with local
   infile enabled, and run the Part 1 script:
   ```bash
   /usr/local/mysql/bin/mysql --local-infile=1 -u root -p
   ```
   ```sql
   source /full/path/to/Part_1_setup.sql
   ```
   (Edit the CSV path inside the script first. On Windows use `D:/...` with forward slashes.)
3. **Install the Python packages** (from this folder):
   ```bash
   python3 -m pip install -r requirements.txt
   ```
4. **Put your MySQL password in `app.py`** — one line, `DB_CONFIG["password"]`
   (or export `DB_PASSWORD=...` and leave the file alone).
5. **Start the server and open the page:**
   ```bash
   python3 app.py
   ```
   → <http://127.0.0.1:5001/>

   Keep the terminal open. `debug=True` restarts the server when you save `app.py`.

**Quick checks**

| Check | Expected |
|---|---|
| `http://127.0.0.1:5001/api/health` | `{"ok": true, "rows": 655200, ...}` |
| `http://127.0.0.1:5001/api/sectors` | JSON list of 6 sectors (the tutorial endpoint) |
| `http://127.0.0.1:5001/api/monthly` | JSON list of months (the tutorial endpoint) |
| Top-right status pill | `API live · 655,200 rows · to 2026-08-31` |

If the page shows an error banner, the banner tells you which of the three layers failed
(MySQL → API → page). The terminal shows Python errors; the browser console (F12) shows JavaScript errors.

---

## 3. Files

```
app/
├─ app.py                  Flask API (9 routes) + comments explaining every query
├─ index.html              the dashboard (one file: HTML + CSS + JS)
├─ static/
│  ├─ echarts.min.js       Apache ECharts 5.5.1, bundled locally (works offline)
│  └─ world.json           world map geometry, bundled locally
├─ Part_1_setup.sql        database, table, LOAD DATA import, verification, analytical queries
├─ requirements.txt        flask, pymysql, cryptography
├─ API_reference.md        every endpoint: parameters, sample JSON, the SQL behind it
└─ README.md               this file
```

Bundling ECharts and the map locally is deliberate: the demo cannot fail because a CDN is slow
or the lecture room has no Wi-Fi.

---

## 4. API in one table

| Route | Purpose | Query parameters |
|---|---|---|
| `/api/health` | status pill / proof the database is reachable | — |
| `/api/meta` | coverage, countries, sectors, years | — |
| `/api/sectors` | sector totals (**the tutorial endpoint**) | `country`, `year` |
| `/api/monthly` | monthly series (**the tutorial endpoint**) | `country` |
| `/api/country_year` | annual totals → map + sparklines | — |
| `/api/country_ytd` | totals + like-for-like change vs 2019 → KPIs + table | `year` |
| `/api/daily` | daily series → weekly rhythm | `country` |
| `/api/compare` | several countries in one query → overlay | `countries=A,B` |
| `/api/insights` | the numbers behind the six findings cards | — |

`API_reference.md` shows the sample response and the SQL for each one.

---

## 5. The interface — and why it is not the reference dashboard

The course supplies a bonus dashboard (`carbon_dashboard.zip`) as a **reference**. The brief says
plainly: *use the instructional code as a foundation, then make the final interface your own.*
We rebuilt the front end from scratch around a different question and a different visual language.

| | Reference bonus dashboard | Carbon Atlas |
|---|---|---|
| Visual language | dark, neon, glassmorphism | light editorial "analyst brief": paper, ink, emerald, serif headlines, hairline rules |
| Story | a wall of widgets | five questions in order: **Where → What → When → Findings → Method** |
| Table | none | sortable country ranking with share, like-for-like 2019 change and 7-year sparklines; CSV export |
| Comparison | one country at a time | overlay a second country, **absolute or indexed to 2019 = 100** |
| Annotation | none | COVID-19 window, rebound, partial-year warnings |
| Interpretation | charts only | auto-generated findings + one-sentence takeaway under every chart |
| Ethics | not addressed | Method & Responsibility panel with a full **GELSI** mapping and stated limits |
| Data integrity | totals can look like a crash in the partial year | partial years flagged and compared with the same months of 2019 |
| Robustness | ECharts + map from CDN | libraries bundled locally, `debug=False`-safe paths, JSON error handling |
| Accessibility | mouse-first dark UI | keyboard-operable table and controls, focus rings, contrast-checked palette, reduced-motion support, skip link |

Each of those is a deliberate design decision that can be explained in the viva — the code is
commented so every chart can be traced back to a route and a SQL query.

---

## 6. Data, limits and ethics (the one-slide version)

* **Source:** [Carbon Monitor](https://carbonmonitor.org/) — fair-use open data; cite **arXiv:2004.13614**.
* **Unit:** the raw column is **MtCO₂ per day**; every total on the page is a *sum of daily estimates* for the chosen period.
* **Living dataset:** values are revised after release, so a later download differs.
* **2026 is partial** (to 31 Aug): we compare it with the same months of 2019, never with a full year.
* **No per-capita ranking:** the dataset has no population column, so we do not divide by population.
* **No personal data:** countries and sectors only — no GDPR data-subject duties arise.
* **GELSI:** the page includes a Governance / Ethical / Legal / Social / Implications table that maps each
  letter to something the system actually does.

---

## 7. What we would say in the demo (30 seconds)

1. `SELECT COUNT(*)` in MySQL shows the rows are really in the database, not in the CSV.
2. `/api/sectors` in the browser shows JSON — the API is doing the SQL.
3. The page is served by the same Flask process on port 5001, so there is no `file://` or Live Server step.
4. Click a country on the map: the KPI strip, sector bars and weekly rhythm all re-query and redraw.
5. Change the year to 2026: the page switches to "Jan–Aug" and compares with the same months of 2019.
6. Compare China with India, then switch to **Index · 2019 = 100**: different sizes, comparable shapes.

---

## 8. Troubleshooting (mapped to the lecture's list)

| Symptom | Fix |
|---|---|
| `This site can't be reached` | `app.py` is not running — start it |
| `Not Found` on `/` | `index.html` is not next to `app.py` |
| `ModuleNotFoundError: flask` | `python3 -m pip install -r requirements.txt` |
| `Access denied for user 'root'` | wrong password in `DB_CONFIG` |
| `Unknown database 'carbon_lab'` | Part 1 import has not been run |
| Page loads but says "API offline" | MySQL down or the password in `app.py` is wrong |
| Charts blank, no error | open F12 → Console; usually the browser blocked a local fetch |
| Port 5001 busy | change `port=5001` in `app.py` and open `:5002` |

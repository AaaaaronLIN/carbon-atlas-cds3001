# Carbon Atlas — CDS3001 Group Project
**Company: Data Fanatics · Product: Carbon Atlas · Lingnan University · CDS3001**
Data: Carbon Monitor daily CO₂ estimates · MySQL 8 · Flask API · one web page · 9:23 presentation
Tagline: **See every tonne. Cut what matters.**

---

## What this submission contains

| Rubric item | Files in this ZIP |
|---|---|
| **Part 1 — data in MySQL (10%)** | `Part_1_Database/Part_1_setup.sql` — database, table, `LOAD DATA` import, verification queries and the analytical SQL behind the API. Evidence: `Part_1_Database/verification_output.txt` (real output: 655,200 rows, 2019-01-01 → 2026-08-31). |
| **Part 2 — API (10% of the presentation; 5% of the project)** | `Part_2_API/app.py` (Flask + PyMySQL, 9 JSON routes, parameterised SQL, JSON error handling), `requirements.txt`, `API_reference.md`. |
| **Part 3 — web page (10% of the presentation; 5% of the project)** | `Part_3_Frontend/index.html` + `static/` (Apache ECharts 5.5.1 and the world map are bundled locally, so the page works offline). |
| **Front-End Dashboard (10%)** | `Final_Frontend_PDF/Carbon_Atlas_Final_Frontend.pdf` — 10 A4 pages of screenshots of the running interface (Stage + Day themes, Story mode, Team, GELSI, partial-year integrity), with the design reasoning and reproduce steps. |
| **Full presentation kit** | `Presentation/` — 17-slide deck with **embedded 90 s demo video (S7)** and **embedded 30 s audio + 45 s video ad (S13)**; PDF copy of the deck; 9:23 run-of-show; 5 per-member scripts; Q&A cheat sheet; host cue card; A3 poster (PNG/PDF); audio-ad script + voice recording sheet; video storyboard; cost–benefit workbook. |
| **Media files (backup, also embedded in the deck)** | `Presentation/ads/audio/` — 30 s audio ad (MP3/WAV/M4A draft, voice to be replaced by LAI Patten). `Presentation/ads/video/` — 90 s demo recording and 45 s video ad (MP4, H.264/AAC). |

`carbon_api/` is the **runnable copy** of Parts 2 + 3 (app.py, index.html, static assets, requirements).
`Part_2_API/` and `Part_3_Frontend/` hold the same files split by part so each rubric section can be marked on its own.

---

## Presentation: how to run the media (Windows PowerPoint)

1. Open `Presentation/Carbon_Atlas_Deck.pptx` in **PowerPoint (Windows, 2016 or later / Microsoft 365)**.
2. Start the slideshow (F5).
3. **Slide 7** — click the large dark screenshot: the **90-second demo video** plays. Sound is not required for the demo; LAI/HUANG narrate over it.
4. **Slide 13** — click **PLAY 30 s AUDIO**, then **PLAY 45 s AD**. Turn the system volume up; the classroom has sound output.
5. If any embedded media does not play on the classroom machine, open the same file directly from the `Presentation/ads/audio` and `ads/video` folders in the USB copy — same files, same lengths.
6. Do not use browser / MySQL / Python on the classroom machine; the deck is self-contained.

---

## Run the live project (for marking / your own machine)

1. **Start MySQL** and import the data (edit the CSV path in the script first):
   ```bash
   mysql --local-infile=1 -u root -p
   source /full/path/to/Part_1_Database/Part_1_setup.sql
   ```
   Expected: `Query OK, 655200 rows affected … Warnings: 0`.
2. `cd carbon_api && python3 -m pip install -r requirements.txt`
3. Set your MySQL password: `export DB_PASSWORD='your-password'` (or put it in `app.py`).
4. `python3 app.py` → open **http://127.0.0.1:5001/**
   The same Flask process serves the page and the JSON API. `?theme=stage` is the default presentation theme; `?theme=light` is the print/review theme.

Quick checks: `/api/health` → `{"ok": true, "rows": 655200, …}`; `/api/sectors` and `/api/monthly` are the two tutorial endpoints; the status pill turns red if MySQL stops.

---

## The product in one paragraph

Carbon Monitor CSV → MySQL `carbon_lab.carbon_emission` → Flask JSON → **Carbon Atlas**.
655,200 rows · 39 country/region series · 6 sectors · 2019-01-01 → 2026-08-31 · unit **MtCO₂ per day**.
The page answers five questions in order — **Where → What → When → Findings → Method** — with a rotating globe hero, a sortable ranking table + sparklines + CSV export, sector and weekday views, a monthly trend with two-country comparison and **Index · 2019 = 100**, six rule-based findings, and a Method & Responsibility panel mapping the **GELSI** framework to real features.
2026 is partial: it is always compared with the same months of 2019, never with a full year. Every number is computed by SQL at request time; the page stores no data of its own.

**Customisation vs the supplied bonus dashboard:** the reference was a starting point, not the submission. Carbon Atlas re-designs the interface as an editorial analyst brief (default **Stage** theme for projection, **Day** theme for print), and adds the ranking table + CSV, the two-country index comparison, the guided **Play the brief** tour, rule-based findings, the GELSI panel, offline local assets, keyboard/contrast/reduced-motion support, and a data-integrity rule for partial years. The comparison is on page 8 of the final PDF and slide 12 of the deck.

---

## API summary

| Route | Purpose |
|---|---|
| `/api/sectors`, `/api/monthly` | the two required tutorial endpoints |
| `/api/country_year`, `/api/country_ytd` | map + ranking; totals with like-for-like 2019 comparison |
| `/api/daily`, `/api/compare` | weekly rhythm; multi-country monthly overlay |
| `/api/insights`, `/api/health`, `/api/meta` | findings facts, DB status, dimensions/coverage |

Full request/response examples and the SQL behind each route: `Part_2_API/API_reference.md`.

---

## Submission checklist (internal)

- [x] Part 1 code + import + real verification output
- [x] Part 2 code + endpoint reference
- [x] Part 3 code + local assets
- [x] Final front-end PDF (10 pages)
- [x] 17-slide deck with embedded demo video + audio/video ads; PDF copy
- [x] 9:23 run-of-show, 5 member scripts, Q&A cheat sheet, host cue card
- [x] A3 poster (PNG/PDF) + audio script + video storyboard + voice recording sheet
- [x] Cost–benefit workbook with labelled assumptions
- [ ] **LAI Patten records the 30 s + 45 s voice-over and sends the files** (before 24 Nov; instructions in `Presentation/ads/voice_recording_sheet_Patten.md`)
- [ ] Test the deck with media on a **Windows** classroom machine (or a Windows PC) before rehearsal
- [ ] Optional: replace the cartoon avatars with photo-based versions if the team supplies headshots
- [ ] Rehearse 9:23 twice as a group (no notes, every member speaks)
- [ ] Submit one ZIP on Moodle by **27 November 2026, 18:00 Hong Kong time**

---

## Credits

Data: [Carbon Monitor](https://carbonmonitor.org/) — fair-use open data, cite **Sci Data 7, 392 (2020), doi:10.1038/s41597-020-00708-7**; the dataset is living and values are revised.
Charts: Apache ECharts 5.5.1 (Apache-2.0) and its world map geometry, bundled locally under `static/`.
Built by Data Fanatics for CDS3001 Databases and Data Warehouses, Lingnan University.

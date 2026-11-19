# 06 · Q&A Cheat Sheet — 10 題 + 快速補問

> 用途：**只供排練與後台複習**。Lecture 17 明定**台上不可使用筆記**，所以答案要靠排練記住；Q&A 現場由 host 按主題分人回答（見 `00` 第 4 節）。
> 事實紀律：只用 verified facts；不確定的數字說 **"That number is not in our data; we can check after the session."** 不編。
> 答題結構（每題 ≤20 秒）：**一句結論 → 一個證據（slide / file / route）→ 一句限制或誠實界線**。
> **v2 場地**：Windows 教室、只有 PowerPoint、沒有瀏覽器／server；demo 是 S7 的 90 秒錄影。Q&A 遇到「為什麼不 live demo」一律誠實回答（見 Q6、快速補問）。

---

## Q1. Why not just use the supplied bonus dashboard (Moodle `carbon_dashboard.zip`) as-is?

**English answer（約 28 s）**
> "We started from it — it taught us the pattern: Flask, one page, ECharts. But the brief asks for a customised interface, and the bonus was a reference, not our submission. We rebuilt the page around five questions a client asks: a sortable ranking with sparklines and CSV export, an Index · 2019 = 100 compare mode, rule-based findings, a Method panel with the GELSI mapping — and it runs offline. The tutorial gave us the pattern; the brief is ours."

**中文註記**：語氣要尊重 reference（「kept what it got right」），不要貶低講義；重點是 **5 個具體改動**與「pattern 不是 product」。這也是 Lecture 17 錄音 22:14–24:26 的高分指引：原樣兩張圖不足以高分。
**證據 pointer**：S12 對照表 · **S7 錄影 0:00–1:30**（S8–S11 備援截圖）· `shots/atlas/deck1-stage-hero.png` 等 · `project/app/index.html` · 講義 p.12 Bonus / p.23 customised UI。

---

## Q2. How do you handle the partial 2026?

**English answer（約 28 s）**
> "2026 only runs to 31 August — 25,014 MtCO₂. Compared with the full 2019 total of 36,397, it would look like a 31% collapse. That is a display choice, not a data finding. So every 2026 comparison uses the same months of 2019 — like for like — and the chart flags the year as partial. One API route, `/api/country_ytd`, does that comparison, so every panel is consistent."

**中文註記**：這題幾乎必問。31% 假跌幅是最有力的例子；接著一定要說「同月比較 + 標記 partial + 單一路由保持一致」，這是 Ethical 的具體證據。
**證據 pointer**：S10/S11、dashboard trend 下方的 partial 註記、Method 面板 · `app.py` `/api/country_ytd` 與 `latest_complete_year()`。

---

## Q3. Is the data trustworthy?

**English answer（約 30 s）**
> "It is Carbon Monitor — open research data, cited as arXiv:2004.13614. But be precise about what it is: modelled daily estimates, not metered values. It is a living dataset, so values are revised; our numbers are a snapshot to 2026-08-31. And it is national totals — national averages hide sub-national variation. We print those limits in the Method panel rather than in a footnote."

**中文註記**：先給可信的部分（來源、citation），再主動說限制（modelled / living / national averages）。「主動說限制」正是 Safety & Responsibility 的得分點，不要防衛。
**證據 pointer**：S11 / S15、dashboard Method 面板（source、coverage、snapshot date、limits）· footer 的 citation · `project/app/index.html` footer。

---

## Q4. SQL injection / security — how is the API protected?

**English answer（約 26 s）**
> "Every query is parameterised — PyMySQL placeholders, values passed as parameters, never string-concatenated. The API is read-only: there are no INSERT or UPDATE routes. If MySQL fails, it returns JSON 503 instead of an HTML stack trace, so the page can explain the failure. And the demo runs on localhost, so it is not internet-exposed. No personal data is stored, so there is no personal-data attack surface."

**中文註記**：四層答案：參數化查詢 → 唯讀 → 錯誤處理（JSON 503）→ 本機／無個資。這是 Lecture 19 的 Legal/Governance 與 L17 Part 2 行為要求的交集。
**證據 pointer**：S5「SAFE BY DEFAULT」· `project/app/app.py` 的 `run_sql()`（`cur.execute(sql, params)`）與 `@app.route` 清單 · `/api/health` 503。

---

## Q5. Why no per-capita view?

**English answer（約 24 s）**
> "Because the dataset has no population column. We could have joined a population table from somewhere else, but then we would be comparing two different sources and calling it one number. For a client brief, a ranking that looks authoritative but mixes sources is worse than no ranking. So the Method panel states the limit, and we rank on totals only."

**中文註記**：這題是「誠實 > 好看」的測試。不要說「未來會做」；先說 why not，再說限制已印在畫面上。
**證據 pointer**：dashboard Method 面板「No per-capita view」· S15 Implications 列 · `carbon_emission` schema（country, date, sector, value — 無 population）。

---

## Q6. What happens if MySQL dies during the demo?

**English answer（約 26 s）**
> "What you watched is a recording of the build running from MySQL on our own machine. If MySQL had failed during that build, the API returns a JSON 503 and the page shows its status pill — it is designed to fail loudly, not to fake numbers. On this classroom machine we cannot run MySQL at all, so the recording is the honest way to show the build. If the recording itself fails, we switch to the backup screenshots and keep the same narrative."

**中文註記**：v2 這題要同時答「系統行為」與「場地限制」：JSON 503／status pill 是 Governance 的實際設計；不能 live demo 是因為教室只有 PowerPoint。**不要**說「我們即場跑」，也不要假裝系統不會掛。
**證據 pointer**：`project/app/app.py` 的 JSON 503 處理 · dashboard 狀態 pill／error banner · **S7 錄影** · S8–S11 備援截圖 · `scripts/07_interaction_plan.zh.md`。

---

## Q7. How were the ads produced?

**English answer（約 28 s）**
> "The three scripts and the poster are ours. The audio and the video are produced from those scripts and embedded on slide 13 — the voice is a team member's, recorded for this pitch. They are drafts, not an agency production, and they all carry the same line: '37,856 million tonnes a year. Now find the part you can move.'"

**中文註記**：**誠實**是這題的評分點：media drafts、team voice、不是專業製作、不是 AI 生成（也不要主動提 AI）。三媒體同一句是 rubric 的一致性證據。**前提**：pre-flight 已確認 S13 內嵌媒體可播；若未完成，不能說「embedded」，改說 *"The media are scripted drafts — we are showing the poster and the scripts, and we are not claiming a finished production."*
**證據 pointer**：S13（poster 圖＋內嵌 audio／video）· `ads/poster.html` + `poster.pdf` + `poster.png` · `ads/audio_ad_script.zh.md` · `ads/video_storyboard.zh.md` · 共用句也在海報主標。

---

## Q8. What would you build next?

**English answer（約 22 s）**
> "Three things, in order. Automatic refresh from Carbon Monitor, so the snapshot date stops moving. Sub-national data, because national totals hide where emissions actually are. And then a per-capita view — but only with a population source we can cite. None of those are built, and we are not claiming them."

**中文註記**：順序有理由（資料鮮度 → 空間解析度 → 人均）；最後一句「not built」一定要說，避免把未完成當完成（Conclusion 的評分要求）。
**證據 pointer**：S16「NEXT, HONESTLY」· Method 面板 limits · S11 method。

---

## Q9. What makes this "customised" versus the reference?

**English answer（約 28 s）**
> "Five concrete changes. The visual language is light and editorial, not the dark widget grid. The ranking table is sortable, with sparklines and CSV export. Compare mode has an Index · 2019 = 100 toggle. Findings are generated from fixed templates by the API, not hand-written. And the Method panel prints provenance, coverage and GELSI. The reference gave us the pattern; the brief is ours."

**中文註記**：與 Q1 互補：Q1 講「不只是原樣」，Q9 講「具體改了什麼」。五點都在 S12 表格上，逐點指。
**證據 pointer**：S12 對照表 · **S7 錄影（0:00–1:30）** · `shots/atlas/deck1-stage-hero.png`、`deck6-method.png` 等截圖。

---

## Q10. Why is the product worth paying for?

**English answer（約 30 s）**
> "We cannot claim revenue, clients or measured savings — this was never sold. What we can model is one analyst saving two hours a week: 92 hours a year at HK$250, so HK$23,000 a year, against a one-off HK$31,746. Break-even is 16.6 months, and the three-year net is about HK$37,254. The value is the hours plus the caveats being visible — a brief you can act on, with its limits printed."

**中文註記**：先否認不能宣稱的（營收／客戶／實測節省），再給可辯護的模型（工時×費率），最後回扣產品價值（可執行＋限制可見）。**不要說「很便宜」或「一定有回報」**。
**證據 pointer**：S14 · `cost_benefit.xlsx`（Summary / Costs & Benefits / Assumptions / Notes 四頁）· 「not claiming」虛線框。

---

## 快速補問（每題一句，≤10 s）

| 問題 | English one-liner | 證據 |
| --- | --- | --- |
| 為什麼用 ECharts 不用 Chart.js？ | "The brief needed a world map and event annotations; ECharts gives both, and we bundled it locally so the demo runs offline. Same fetch-first pattern as the tutorial." | S6、`static/echarts.min.js`、`static/world.json` |
| 655,200 怎麼來的？ | "Thirty-nine series × six sectors × 2,800 days; `SELECT COUNT(*)` returns 655,200 with zero warnings." | S4、`/api/health` |
| 為什麼是 39 個 series 而不是 40？ | "Thirty-nine is what the table holds — 655,200 closes at 39 × 6 × 2,800; smaller emitters sit inside Rest of World." | `/api/meta`、Method 面板 |
| 你們有幾條 API route？ | "Nine: health, meta, sectors, monthly, country_year, country_ytd, daily, compare, insights." | S5、`app.py` |
| 成本假設哪裡來？ | "All on the assumptions slide and in `cost_benefit.xlsx` — labour at HK$80 as opportunity cost, analyst at HK$250 loaded rate." | S14、xlsx Assumptions |
| 如果沒有網絡？ | "The build runs offline from local assets — ECharts and the world map are bundled. The demo is a recording, so it plays with the Wi-Fi off." | S6、`static/`、S7 |
| 為什麼 demo 是錄影？ | "This classroom machine only shows PowerPoint — no browser, no server. We recorded the build running from MySQL on our own machine, so the demo is real data, not a mock." | S7、`07`、`app.py` |
| Q&A 被問到 Cantonese？ | 用英文答；開場可說 "We are happy to answer in English; we can follow Cantonese." | — |
| 被問到不在資料的國家？ | "Carbon Monitor tracks 39 series; that country sits inside Rest of World — the brief says so instead of inventing a number." | Method 面板、`/api/meta` |

---

## Q&A 主持（host 用）

1. 有人舉手 → **"Yes — go ahead."**
2. 判斷路由 → **"Zichao, the data."** / **"Mantung, the API."** / **"Patten, the page."** / **"Haolin, the campaign."** / **"Mantung, the ethics."**
3. 冷場 → **"While you think — our question is for the next group."** 問 S17 的問題；再自問一題 partial-year，交 WENG。
4. 最後 10 秒 → **"One last question."** 答完 → **"Thank you — that's our minute."**
5. **必問句**：**"Which chart in your dashboard changed a decision — and how would you prove it?"**（Lecture 17 錄音要求，每組至少一題；不可漏）

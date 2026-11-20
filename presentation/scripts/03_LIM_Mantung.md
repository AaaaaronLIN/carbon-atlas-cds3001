# 03 · LIM Mantung (4592996) — Part 2 code + Safety & Responsibility (GELSI)

> **角色**：API (Part 2) & Safety/GELSI。**負責評分項**：#4 Part 2 code（10%）· #9 Safety & Responsibility（10%）。
> **投影片**：S5（One helper, nine JSON routes）· S15（GELSI: the risks we can actually see）。
> **說話時間**：42 + 53 = **95 秒**（目標 85–110）。**台上不可帶筆記**；本檔只作排練用。
> **Q&A 主答**：API／SQL injection／JSON 503／安全；GELSI／倫理／法律／社會責任；亦可答「客製化 vs reference」。
> **v3 場地**：demo 是 S7 的 live 90 秒（Mac 跑 Flask/MySQL；教室浏览器打开 tunnel/LAN URL），失败切回 S7 录屏。Part 2/GELSI 段不需要碰 server。Q&A 被问「MySQL 挂掉怎么办」时，先答系统行为（JSON 503/status pill），再交 LAI 补「live 失败切录屏」。

**朗讀圖例**：[PAUSE] = 停頓 1 秒 · [POINT …] = 指向畫面 · ⏱ = 相對秒數。

---

## A. Part 2 code — S5（42 s）

**上台起點**：時鐘 **2:13**（WENG 交棒後）· S5 在畫面上 · 站投影左側。

> ⏱ [0:00] **Part 2 is one helper and nine routes.**
>
> ⏱ [0:04] [POINT `run_sql`] **`run_sql` opens a connection, runs one parameterised query, returns the rows, and closes.**
>
> ⏱ [0:13] [POINT endpoint] **Every route is that same pattern. `/api/sectors` is the tutorial one: country and year come in, grouped totals go out.**
>
> ⏱ [0:23] [POINT JSON 區] **And this is the real response: world 2025 sector totals — Power 13,492, Industry 12,663, ground transport 6,884. The page does no arithmetic; MySQL does.**
>
> ⏱ [0:34] [POINT "SAFE BY DEFAULT" 兩行] **Two behaviours matter: inputs are parameterised, never concatenated; and if MySQL is down, the API returns JSON 503 — not an HTML error page.**
>
> ⏱ [0:41] **Patten, draw it.**

【中文註記 — 為什麼這樣講才有分】
- Part 2（10%）評分要求：**說清楚 SQL 如何經 API 變成 JSON，並展示回傳結果；不可略過資料庫連接與 API 行為**。這段四件事：helper（連接＋參數化查詢）、九條路由同一個 pattern、真實 JSON、錯誤行為（JSON 503）——正好是「DB 連接、SQL→JSON、API 行為」。
- **重要更正**：deck S5 的 JSON 範例數字是 **WORLD 2025** 總量（Power 13,492 / Industry 12,663 / Ground transport 6,884），不是 China（China 2025 全年只有 12,089，不可能是 13,492）。所以講稿說 **world**；deck 的 JSON 標籤也要改成 `country=WORLD`（見 `00` 第 6 節）。
- 不要念九條路由的名字；「nine routes, one pattern」比逐條念好記。若評審要看路由清單，指畫面下方的 /api 清單。
- JSON 503 這句是安全題的伏筆：Q&A 被問「MySQL 掛掉怎麼辦」時，就是這個行為讓頁面可以解釋錯誤、不會爆 HTML；v3 由 LAI 補一句「live 失敗切 S7 錄屏，再不行切 S8–S11 截圖」。

**忘詞備援**：只記兩句：**"One helper, nine routes."** 和 **"SQL does the arithmetic; the page only draws."**

---

## B. Safety & Responsibility — GELSI — S15（53 s）

**上台起點**：時鐘 **7:45**（WENG 交棒後）· S15 在畫面上 · 站投影左側，手指可逐列移動。

> ⏱ [0:00] **GELSI: governance, ethical, legal, social, implications. One line each — and every line has a feature behind it.**
>
> ⏱ [0:09] [POINT G 列] **Governance: one owned pipeline; source and coverage printed; `/api/health` exposes outages.**
>
> ⏱ [0:17] [POINT E 列] **Ethical: a partial 2026 would fake a 31% fall — we compare the same months, start axes at zero, and publish the limits.**
>
> ⏱ [0:27] [POINT L 列] **Legal: Carbon Monitor — fair-use open data, cited as arXiv:2004.13614. No personal data.**
>
> ⏱ [0:35] [POINT S 列] **Social: keyboard access, contrast, reduced motion, offline, and a light theme that prints.**
>
> ⏱ [0:42] [POINT I 列] **Implications: 69.1% sits in two sectors, so effort can go where emissions are — but we refuse per-capita claims; there is no population column.**
>
> ⏱ [0:50] [POINT coverage strip] **One limit we print: thirty-nine series; smaller emitters sit inside Rest of World.**
>
> ⏱ [0:52] **The Method panel is where these promises live in the product. Haolin, bring it home.**

【中文註記 — 為什麼這樣講才有分】
- Safety & Responsibility（10%）評分要求：**討論與本系統有關的風險、影響、應對方式，不能只有標題或泛泛口號**。這頁用 L19 的 GELSI 五柱，每一柱都接一個**真實存在的功能**：
  - G → `/api/health`＋畫面狀態 pill＋每張圖標明來源表；
  - E → 2026 同月比較（31% 假跌幅是最有力的具體例子）＋ zero-based axes＋不挑日期範圍；
  - L → Carbon Monitor fair-use＋cite arXiv:2004.13614＋無個人資料（GDPR data-subject 義務不適用）；
  - S → 鍵盤操作、對比、reduced motion、離線、可列印淺色主題；
  - I → 產業/國家集中度引導行動；拒絕 per-capita（資料沒有 population 欄位）。
- 「31% fall」是評審最可能記住的一句：raw 2026（25,014）vs full 2019（36,397）≈ −31%，我們用同月比較避免這個錯誤——這是把倫理講成「顯示決策」而不是口號。
- 至少一張安全／倫理投影片是 Lecture 17 明確要求；S15 就是。**五行不可跳**，即使時間緊也每行留一句。
- 若被問「這算安全嗎？」→ 提醒：我們談的是**系統安全＋倫理責任**，不是網絡攻防；網絡安全在 Q&A 另有答案（parameterised queries、JSON 503、localhost）。

**忘詞備援**：記五個字母的順序 G-E-L-S-I 與每列第一個字（one pipeline / like-for-like / fair-use / keyboard / concentration）。真的忘，就指著表格念字母開頭的字，再補「and each one maps to a feature on this page」。

---

## C. 交接與 Q&A

- 收句交 HUANG：**"Haolin, bring it home."**（已含在 53 s 內）
- **Q&A 主答題目**：
  1. 「SQL injection／安全？」→ *"Every query is parameterised — PyMySQL placeholders, values passed as parameters, never string-concatenated. The API is read-only: no INSERT or UPDATE routes. If MySQL fails, the API returns JSON 503 instead of an HTML stack trace, so the page can explain it. And it runs on localhost, not the public internet."*
  2. 「有處理個人資料嗎？」→ *"No personal data at all. Carbon Monitor is national and sector daily totals; there is no person in the dataset, so GDPR data-subject duties do not arise."*
  3. 「API 壞掉頁面會怎樣？」→ *"The page shows a status pill and an error banner with the reason; it does not silently show stale numbers. The live demo uses the same API; if the classroom network fails, the same build plays from the embedded recording, not a fake live run."*
  4. 「GELSI 為何用 Yale/WEF 的框架？」→ *"It is the framework from Lecture 19 — governance, ethical, legal, social, implications — and we used it as a checklist against our own features, not as decoration."*
  5. 「客製化 vs reference？」→ 見 `06_qa_cheatsheet.zh.md` Q1/Q9（可與 LAI 分工）。

## D. 個人排練檢查

- [ ] Part 2：helper → route → JSON → 503 四個順序不忘；JSON 說 **world**，不是 China。
- [ ] GELSI：G-E-L-S-I 五行每行 ≤10 秒，五個功能對應正確。
- [ ] 31% 假跌幅的例子能一句講完（25,014 vs 36,397）。
- [ ] 收句 "Haolin, bring it home." 不看稿。

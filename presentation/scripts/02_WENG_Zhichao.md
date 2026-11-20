# 02 · WENG Zhichao (4589896) — Part 1 code + Cost–Benefit

> **角色**：Database (Part 1) & cost–benefit。**負責評分項**：#3 Part 1 code（10%）· #8 Cost–Benefit Analysis（10%）。
> **投影片**：S4（655,200 rows land in MySQL）· S14（What it costs, what it returns）。
> **說話時間**：42 + 50 = **92 秒**（目標 85–110）。**台上不可帶筆記**；本檔只作排練用。
> **Q&A 主答**：資料從哪來／可不可信／2026 partial／成本效益／售價利潤。
> **v3 場地**：demo 是 S7 的 live 90 秒（Mac 跑 Flask/MySQL；教室浏览器打开 tunnel/LAN），失败切 S7 录屏；Part 1 段不需要碰 server/浏览器；成本模型的 hosting 假设（build 跑在 laptop、hosting 为零）不变。

**朗讀圖例**：[PAUSE] = 停頓 1 秒 · [POINT …] = 指向畫面 · ⏱ = 相對秒數。

---

## A. Part 1 code — S4（42 s）

**上台起點**：時鐘 **1:31**（host T1 交棒後）· S4 在畫面上 · 站在投影左側，先面向觀眾。

> ⏱ [0:00] **Part 1 is not "download a CSV". It is a schema, a controlled import, and a verification query.**
>
> ⏱ [0:07] [POINT CREATE TABLE 區] **One table: country, date, sector, value.**
>
> ⏱ [0:14] [POINT LOAD DATA] **One import. The file has a trailing comma, so we park the empty fifth column in `@dummy`.**
>
> ⏱ [0:22] [POINT `STR_TO_DATE`] **Dates arrive as DD/MM/YYYY, but MySQL needs a DATE. We convert during the import — not by hand.**
>
> ⏱ [0:31] [POINT 大字 **655,200**] **The result: six hundred fifty-five thousand, two hundred rows. Warnings: zero.**
>
> ⏱ [0:37] [POINT 驗證列] **And we verify it: January 2019 to August 2026, thirty-nine series, six sectors, one unit.**
>
> ⏱ [0:41] **The CSV is a file. This is a queryable table. Mantung, make it a URL.**

【中文註記 — 為什麼這樣講才有分】
- Part 1（10%）評分要求：**解釋 MySQL 匯入與檢查的關鍵程式及結果**，不是貼不能解釋的截圖。這段只講三個技術點（建表、`@dummy`、`STR_TO_DATE`）＋一個結果（655,200 / warnings 0）＋一個驗證（日期範圍、39 series、6 sectors、單位），正好覆蓋「import 與 check」兩個關鍵字。
- 「The CSV is a file. This is a queryable table.」這句是 Part 1 的存在理由，也幫評審記住資料已經真的進 MySQL、不只是 CSV。
- 不要逐行念 SQL；指著三塊程式各講一句就好。Workbench 截圖在 S4 右下，指一下即可（「and we check it in Workbench, not just the terminal.」可省，因為時間留給驗證列）。
- 655,200 是唯一要放慢的數字；warnings zero 要清楚。

**忘詞備援**：若忘 `STR_TO_DATE` 怎麼念，直接比著它說 **"DD/MM/YYYY in the file, DATE in MySQL — done in the import."** 然後跳去 655,200。

---

## B. Cost–Benefit — S14（50 s）

**上台起點**：時鐘 **6:55**（host T3 交棒後，廣告剛結束、音量已降）· S14 在畫面上 · 先停 0.5 秒再開口。

> ⏱ [0:00] **Now the business case.**
>
> ⏱ [0:03] [POINT 成本列] **One-off cost: HK$31,746. Development: 360 student-hours at HK$80 — 28,800. Poster: 60. Contingency: 2,886. Hosting: zero — the build runs on a laptop.**
>
> ⏱ [0:18] [POINT 效益列] **On the benefit side: one analyst saves two hours a week — 92 hours a year at HK$250. That is HK$23,000 a year.**
>
> ⏱ [0:30] [POINT 三個 KPI] **So: break-even 16.6 months — about seventeen. Three-year net: plus HK$37,254. Benefit–cost: 2.17 to one.**
>
> ⏱ [0:41] **A managed-cloud option adds HK$3,000 a year: break-even 24.4 months, net 28,254.**
>
> ⏱ [0:46] [POINT 虛線框 "WHAT WE ARE NOT CLAIMING"] **What we are not claiming: no revenue, no price, no clients, no measured savings. Every assumption is printed on the slide. Mantung, the responsibility side.**

【中文註記 — 為什麼這樣講才有分】
- Cost-Benefit（10%）評分要求：成本 vs 效益、假設要標明、數字一致、不冒充已實現收益。本段把 Lecture 17 錄音提到的「成本、售價、利潤」正面接住：**成本講清楚、效益用「一位分析師省下的時間」建模、售價／利潤明說不宣稱**（我們從未售出）。「not claiming」框是這頁的得分點，不是免責聲明。
- 所有數字都與 `cost_benefit.xlsx` 一致：31,746 = 28,800 + 60 + 2,886；23,000 = 92 h × 250；16.6 個月；3 年淨額 37,254；B/C 2.17；雲端變體 3,000/yr → 淨額 28,254、24.4 個月。若評審追問，說「All assumptions are on the slide and in the cost_benefit workbook」。
- 不要說「投資回報 217%」或任何 revenue 字眼；不要說「客戶會買」。我們賣的是 course project 的成本模型，誠實才有分。
- 語速：成本清單可以快（像會計），到 break-even 與 not-claiming 放慢。

**忘詞備援**：只記三個數字：**31,746 / 23,000 / 17 months**。其餘用「the rest is on the slide」帶過，不要停超過 2 秒。

---

## C. 交接與 Q&A

- 收句交 LIM：**"Mantung, the responsibility side."**（已含在 50 s 內）
- **Q&A 主答題目**：
  1. 「資料可信嗎？」→ *"Carbon Monitor — open research data, cited as arXiv:2004.13614. But be precise: modelled daily estimates, not metered values; a living dataset, so values are revised; our snapshot is 2026-08-31."*
  2. 「2026 部分年份怎麼處理？」→ *"2026 runs to 31 August only. Compared with full 2019 it would look like a 31% fall, so we compare the same months of 2019 and flag the year as partial. Every 2026 figure uses one route, `/api/country_ytd`, so the whole page is consistent."*
  3. 「成本假設哪來的？」→ *"360 hours = five students, eight hours, nine weeks; HK$80 is an opportunity cost, not cash; HK$250 is a loaded analyst rate. All in the Assumptions sheet."*
  4. 「售價／利潤？」→ *"There is no price and no profit — this was never sold. We model one analyst's time saving, and we say so on the slide."*
  5. 「655,200 怎麼算？」→ *"39 series × 6 sectors × 2,800 days, and `SELECT COUNT(*)` returns 655,200 with warnings zero."*
- 若被問到 `LOAD DATA` 的權限／路徑：*"It runs locally with `LOAD DATA LOCAL INFILE`; the path is printed on the slide."* 不要延伸。

## D. 個人排練檢查

- [ ] Part 1：三個技術點＋四個結果數字（655,200 / 0 / 2019-01-01 / 39+6）能不卡講完。
- [ ] Cost：31,746 / 23,000 / 16.6 / 37,254 / 2.17 五個數字順序不忘。
- [ ] 兩段的收句（Mantung）與（Mantung, the responsibility side）分清楚。
- [ ] 指螢幕時身體不擋投影；每個 [POINT] 都真指到再說話。

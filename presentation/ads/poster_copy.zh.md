# 海報版面說明 · Carbon Atlas（A3 直式）

檔案：`ads/poster.html`（可直接編輯）→ `ads/poster.pdf`（A3 直式，297 × 420 mm，可直接列印）→ `ads/poster.png`（2246 × 3174 px，預覽用）

---

## 1. 為什麼是這個尺寸與結構

- **A3 直式**：講者要求「先展示海報」。A3 在教室前排可讀，直式更像「一頁簡報」而不是廣告傳單。
- 版面由**一條中軸線**控制：所有元素左緣對齊 17 mm，右緣對齊 280 mm；上方報頭、下方 CTA 都用同一條 0.6 pt 細線收邊，這是整份 deck 的編輯風語言。
- 閱讀順序刻意設計成**由大到小、由承諾到證據**：
  1. 報頭（logo + 團隊 + 日期）→ 建立「這是誰的東西」
  2. 主標題 → 一句話講完整個產品
  3. 三格數據 → 用三個真數字支撐標題
  4. 產品預覽（schematic）→ 讓人看見「一個畫面」長什麼樣
  5. CTA → 要求一個具體動作
  6. 資料出處與限制 → 誠實收尾

## 2. 主標題與文案邏輯

> **37,856 million tonnes a year.**
> **Now find the part you can move.**

- 第一行是**資料故事**：2025 年全球 37,856 MtCO₂（= 378.56 億噸），來自 Carbon Monitor 同一份資料。
- 第二行是**承諾**：不談「拯救地球」，只談「找到你可以推動的那一部分」——與簡報的 mission（turn open data into decisions that cut emissions）一致。
- 主標題 42 pt Georgia，斜體行用 emerald，讓「可移動的部分」成為視覺重點。
- 副文只放三個名詞：655,200 rows、one screen、map / ranking / sector mix / trend / findings。不加形容詞。

## 3. 三個數據（全部可回溯）

| 數字 | 意義 | 來源 |
| --- | --- | --- |
| 37,856 MtCO₂ | 2025 年世界總排放 | 世界年度加總（2019 為 36,397） |
| +4.0% | 2019 → 2025 變化 | 37,856 ÷ 36,397 − 1 |
| 61% | 前五大排放國佔比 | 23,082 ÷ 37,856（China 12,089、US 5,036、India 3,309、Russia 1,670、Japan 978） |

三個數字都標了「2025」或「2019 → 2025」，避免和 2026 部分年份混淆。

## 4. 產品預覽：刻意標成 schematic

- 中間的大區塊是**用 CSS/SVG 重畫的儀表板示意**，不是截圖；上方有一行小字 `PRODUCT PREVIEW · SCHEMATIC OF THE DASHBOARD · OFFLINE, LOCAL ASSETS`，避免把 mock 當成已完成產品（講義明確禁止把未完成功能說成已完成）。
- 內容都跟真實資料一致：產業佔比 35.6 / 33.5 / 18.2 / 9.0 / 2.7 / 1.1；排名表 China 12,089 起；年度折線 2019–2025 與 2026 虛線（部分年份）。
- 右下「COVERAGE 40 SERIES」是**一格一個系列**的矩陣圖，深色五格 = 2025 前五大排放國；圖例寫明，避免被誤讀成地圖或熱度圖。
- 「DESIGN NOTE — The chart is not the brief; the sentence under it is.」是刻意的編輯風註記，也是對講者「不要只放兩張圖」的回應。
- 底部 METHOD 列（SOURCE / UNIT / CAVEAT）與 dashboard 的 Method & responsibility 面板同一個概念：把限制印在畫面上。

## 5. 品牌與可及性

| 元素 | 規格 | 理由 |
| --- | --- | --- |
| 紙色 | `#F7F5F0` | 與 deck 同一 paper 色；列印時比純白溫和，投影也不刺眼 |
| 墨色 | `#14201B` | 正文與標題；與紙色對比 > 12:1 |
| 主色 | `#0E7C5A` emerald | 標題斜體、KPI、按鈕 |
| 輔色 | `#C2521F` vermilion | 只用在 kicker 短線、注意事項（約 3% 面積） |
| 第三色 | `#A97E12` ochre | 第三個數字，讓三格數據有層次 |
| 標題字 | Georgia（系統 serif） | 編輯風、列印穩定 |
| 正文 | Helvetica Neue / Arial | 小字清楚 |
| 對比 | 小字全部 ≥ 4.5:1 | 投影與列印都可讀 |

- 沒有外部字體、圖片或 CDN：整個 HTML 自帶 CSS + inline SVG，離線可開。
- logo 用 inline SVG 重畫（羅盤 + 北向葉片），與 `assets/logo.png` 同一幾何。

## 6. 列印與輸出

- `@page { size: A3 portrait; margin: 0 }`，`.sheet` 固定 297 × 420 mm，`print-color-adjust: exact` 已在 CSS 內。
- 已產出 `poster.pdf`（單頁、A3 直式），可直接送印；`poster.png` 為 2× 預覽（2246 × 3174）。
- 若要重出：`build/render_poster.sh`（或見 `integration_notes.md` 的 Chrome 指令）。
- **送印前檢查**：四邊 15 mm 內無重要文字（目前最外元素距邊 12 mm 是頁碼與 CTA 底色，安全）；主標題不可斷行；CTA 按鈕不可被裁切。

## 7. 已知取捨

- 預覽區的空白是刻意的（模擬 dashboard 的呼吸空間），不是排版錯誤；若覺得太鬆，把 `.preview{flex:1}` 改成固定高度即可。
- 海報上的 2026 部分年份已標「1 Jan – 31 Aug」，但沒有畫進年度折線的實線，只以虛線接出，避免看起來像暴跌。
- 沒有放 QR code：目前沒有可公開的網址（demo 只在本機 127.0.0.1:5001），放 QR code 反而是假承諾。

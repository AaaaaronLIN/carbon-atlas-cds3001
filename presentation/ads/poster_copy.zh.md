# 海報版面說明 · Carbon Atlas（A3 直式 · Stage 版）

檔案：
- `ads/poster.html` — 可直接編輯的版面
- `ads/poster.pdf` — A3 直式 297 × 420 mm（向量，可直接列印）
- `ads/poster.png` — 2246 × 3174 px（螢幕預覽 / 放進 deck）
- 素材：`poster_globe.png`（Stage 地球截圖去背）、`poster_ui_where.png` / `poster_ui_when.png`（Stage 真實介面）

---

## 1. 為什麼改成 Stage 深色版

- 網站**預設就是 Stage 深色主題**（投影用）；舊海報是米白紙張版，和預設介面不一致。
- 新海報直接使用 Stage 的色票與字體：
  - 背景 `#0A1310`、面板 `#0F1D17`
  - 象牙白 `#F2EFE5`、薄荷綠 `#43D6A4`、金色 `#E3B341`
  - 標題 serif 用網站同一套 Iowan Old Style / Palatino / Georgia
- 這樣評審看到「海報 → 打開 deck/網站」時，是**同一個產品、同一個視覺系統**。

## 2. 版面結構（由上到下）

1. **報頭**：logo + CARBON ATLAS + BY DATA FANATICS；右上 A3 / Stage edition / Lingnan CDS3001。
2. **主視覺**：97 pt 的 `37,856` + `million tonnes a year.` + campaign line `Now find the part you can move.` + 一行產品說明。
3. **右側地球**：直接來自 Stage 首頁（去背 + 軌道線），加 `2025 · FULL YEAR` 膠囊。
4. **四格數據**：世界 37,856 · 前五國 61.0% · Power 35.6% · 655,200 筆 / 2,800 天。
5. **The brief answers four questions**：WHERE / WHAT / WHEN / WHAT IT CANNOT SAY，四格對應網站四個區塊。
6. **Under the hood**：CSV → MySQL → Flask → ECharts → One brief，對應 Part 1 / 2 / 3。
7. **The screen you actually get**：兩張真實 Stage 介面截圖（Where / When），證明不是 mock-up。
8. **Footer**：tagline `See every tonne. Cut what matters.` + CTA + 資料出處與工具。

## 3. 文案與數字（全部可回溯）

| 數字 | 意義 | 來源 |
|---|---|---|
| 37,856 MtCO₂ | 2025 世界總排放 | SUM by year（2019 = 36,397） |
| +4.0% | 2019 → 2025 | 37,856 ÷ 36,397 − 1 |
| 61.0% | 前五國佔比 | 23,082 ÷ 37,856 |
| 35.6% | Power 部門佔比 | GROUP BY sector, 2025 |
| 655,200 | 總列數 | MySQL COUNT(*) |
| 2,800 | 天數 | 2019-01-01 → 2026-08-31（39 × 6 × 2,800 = 655,200） |

> 海報上的 `MTCO₂ / DAY` 是資料單位；`37,856 MtCO₂` 是年度加總，兩者不矛盾（網站 Method 面板有寫）。

## 4. 列印 / 展示

- 直接印 `ads/poster.pdf`，A3 直式、無白邊；深色底建議用彩雷/相紙，避免太薄透光。
- 教室展示順序：**先指海報 → 再播 30 s audio → 45 s video**（S13 已經按這個順序排）。
- 若列印偏暗：把 PDF 交給印刷店時說「深色底、請保色彩對比」，不要讓印表機自動省墨。

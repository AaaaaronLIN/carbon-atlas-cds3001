# 45 秒影片廣告 · 分鏡腳本（Storyboard）

專案：Carbon Atlas（Data Fanatics · Team Data Fanatics · Lingnan University CDS3001）
長度：**45.0 秒整**
形式：**儀表板螢幕錄影為主**（不需演員、不需外景），片頭／片尾卡片由簡報素材合成。
語言：英文 VO（配音）＋畫面英文字卡；中文為拍攝與剪輯註記。
輸出：1920 × 1080 · 30 fps · H.264 MP4（檔名 `video_ad_45s.mp4`）

---

## 1. 一句話訊息（與海報、音訊一致）

> **37,856 million tonnes a year. Now find the part you can move.**

三種媒體同一句，不另創標語。

---

## 2. 分鏡表

| # | 時間碼 | 長度 | 畫面（Visual） | 畫面英文字（On-screen text） | 英文 VO | 中文拍攝／剪輯註記 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0:00–0:05 | 5.0 s | 全紙色底，數字由 0 跳到 **37,856**，下方一行小字。緩慢上浮 4 px。 | `37,856 MtCO₂ · 2025 · WORLD TOTAL` | "Nearly thirty-eight billion tonnes a year." | 用 deck 的 paper/emerald 色；數字用 Georgia 40 pt 以上。不要放煙、地球、工廠素材（clip-art 感）。 |
| 2 | 0:05–0:09 | 4.0 s | 品牌卡：logo 由小放大到 1.2 倍再回位，右側 wordmark。 | `CARBON ATLAS` / `See every tonne. Cut what matters.` | "Carbon Atlas." | 0.6 秒 logo 動態即可，不要轉場特效。 |
| 3 | 0:09–0:16 | 7.0 s | **螢幕錄影開始**：dashboard 首頁，游標由左上移到 KPI 條，再滑到世界地圖。 | `One brief · nine routes · 655,200 rows` | "One brief: the whole world on one map, from six hundred fifty-five thousand rows." | 錄影前把瀏覽器書籤列、分頁、桌面通知隱藏；網址列只露 `127.0.0.1:5001`。 |
| 4 | 0:16–0:23 | 7.0 s | 點選地圖上的 **China** → 面板同步更新 → 右側排名表排序 → 表格 sparkline 放大（游標停留 1 秒）。 | `CLICK A COUNTRY · EVERY PANEL FOLLOWS` | "Pick a country. Its eight-year line, its share, its rank." | 游標移動放慢（可用錄影後 0.8× 變速）；不要出現真實個資或桌面檔名。 |
| 5 | 0:23–0:30 | 7.0 s | 產業長條圖（Power 35.6% → Industry 33.5% → …）+ 星期節奏圖。 | `POWER + INDUSTRY = 69.1%` / `AVIATION < 4%` | "Power and industry are sixty-nine percent. Aviation is under four." | 只錄這兩個圖，不要一路滾動（45 秒裝不下）。 |
| 6 | 0:30–0:37 | 7.0 s | 月度趨勢圖，游標停在 2020-04 的標註；切到 compare 疊圖（兩條線）。 | `APR 2020: −5%` / `2019 → 2025: +4%` | "The 2020 dip was a shock. The plateau since 2019 is the problem." | 這是全片最重要的「判斷」，字卡一定要留 2 秒可讀。 |
| 7 | 0:37–0:41 | 4.0 s | 捲到 Findings 卡 + Method & responsibility 面板（GELSI 對照）。 | `RULE-BASED FINDINGS · CAVEATS ON SCREEN` | "Every finding traces to one query — and the caveats are on the screen." | 只錄 2 張 finding 卡；Method 面板要拍到「snapshot date」。 |
| 8 | 0:41–0:45 | 4.0 s | 片尾卡：logo + 品牌句 + CTA + 資料出處小字。 | `ASK FOR A 15-MINUTE WALKTHROUGH` / `Carbon Monitor · Sci Data 7, 392 (2020), doi:10.1038/s41597-020-00708-7 · data to 2026-08-31` | "Carbon Atlas. See every tonne. Cut what matters." | 與海報右下角 CTA 同一句話；出處字級可小，但不可省略。 |

---

## 3. 拍攝清單（Screen recording checklist）

1. **只錄我們自己的 dashboard**（`http://127.0.0.1:5001`），不錄任何第三方網站、廣告或個人帳號。
2. 瀏覽器：隱藏書籤列與擴充功能，視窗 1600 × 900 以上；縮放 100%（必要時 90%）。
3. 資料：使用本機 MySQL 的同一份快照（2026-09-01）；不要為了畫面好看手動改數字。
4. 錄影工具：macOS 內建 `⌘⇧5`（或 QuickTime）→ 30 fps，先錄 90–120 秒素材再剪。
5. 游標：錄影時開啟「游標高亮」；移動速度慢，每個互動停留 ≥ 1 秒。
6. 音訊：VO 另錄（48 kHz / 24-bit），音樂用可商用或自製 loop；**不從影片原聲收音**。
7. 字幕：建議燒錄英文字幕（教室投影不保證音響），並另交一份 `.srt`。

## 4. 剪輯與節奏

- 全片 45 秒，**每 5–7 秒一個畫面變化**，避免長時間定格。
- 轉場只用「硬切」或 0.2 秒淡入；不要用縮放、翻頁、粒子特效（與編輯風衝突）。
- 字卡：Georgia 粗體 + Calibri 小字，紙色底、墨色字，與 deck 同一套；字卡停留 ≥ 2 秒或 VO 念完該句。
- 音樂：與音訊廣告同一條 bed（保持一致），VO 時 duck 6 dB，片尾 0:43 起淡出。

## 5. 事實核對

| 畫面／台詞 | 數字 | 檢查方式 |
| --- | --- | --- |
| 37,856 MtCO₂（2025 世界） | 37,856 | `/api/insights` 的 annual 陣列 |
| 655,200 rows | 655,200 | `/api/health` 的 `rows` |
| Power 35.6% / Industry 33.5% | 69.1% 合計 | `/api/sectors?year=2025` |
| 2020 較 2019 −5.0% | 34,583 vs 36,397 | 年度加總 |
| 2019 → 2025 +4.0% | 36,397 → 37,856 | 年度加總 |
| data to 2026-08-31 | — | Method 面板 |

> 若錄影當天 API 回傳的數字與上表不同（Carbon Monitor 是 living dataset），**以畫面顯示的數字為準**，並重錄字卡；不要讓字卡與畫面不一致。

## 6. 與另外兩個媒體的關係

| 媒體 | 長度 | 角色 | 一致性檢查 |
| --- | --- | --- | --- |
| 海報 | A3 靜態 | 讓人停下來、帶走一個數字 | 主標 37,856、+4.0%、61% 與影片一致 |
| 音訊 | 30 s | 用聽的記住一句話 | 品牌句與 CTA 與影片片尾相同 |
| 影片 | 45 s | 用看的相信 dashboard 是真的 | 只錄真實操作，不造假互動 |

播放順序（簡報 S13）：**海報 → 音訊 30 秒 → 影片 45 秒**，共 80 秒（含 3 秒海報開場與 2 秒收句）。

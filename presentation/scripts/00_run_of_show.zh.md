# CARBON ATLAS · 最終簡報 Run of Show（9:23 + 1 分鐘 Q&A）· v2（真實場地版）

> **公司 / 團隊**：Data Fanatics · Lingnan University · CDS3001
> **產品**：Carbon Atlas（舊名 Carbon Compass 一律不再使用）
> **Tagline**：See every tonne. Cut what matters.（品牌面不加引號）
> **Campaign line**："37,856 million tonnes a year. Now find the part you can move."（三媒體同一句，可加引號）
> **場合**：Lecture 17 最後一堂 · 2026-11-27（五）· 每組 9–10 分鐘簡報 + 1 分鐘 Q&A
> **語言**：全英文 · **不可使用筆記** · 每位成員都要發言 · 手機靜音
> **角色設定**：我們是 account team，台下是「香港上市公司的 sustainability team」，評審是 panel。Host 用 account lead 的語氣主持整場。

**場地與媒體（v2 確認）**

| 項目 | 事實 | 對簡報的影響 |
| --- | --- | --- |
| 教室電腦 | **Windows** | 所有操作只能靠 PowerPoint：上一頁、播放內嵌媒體、雷射筆 |
| 可顯示的程式 | **只有 PowerPoint**（依經驗） | **沒有瀏覽器、沒有本機伺服器、不保證 MySQL / Python** |
| 檔案傳輸 | 可用 USB 複製 | 上台前把**最終 PPTX（含所有內嵌媒體）＋ PDF 備份**放入 USB |
| 音效 | **有聲音輸出** | S13 的 30 s 音訊與 45 s 影片**直接播**；音量 pre-flight 設 70% |
| Demo 方式 | **S7 內嵌 90 秒預錄影片**（在我們機器上真實跑 MySQL build 的 Stage 主題螢幕錄影） | 6a + 6b 邊播邊旁白；**不再有任何 live 點擊** |
| 備援畫面 | S8–S11 截圖、`out/screenshots/atlas/*.png`、deck PDF | 影片／媒體不播時立即切換 |

**成員（顯示格式固定）**

| 顯示名 | 角色 | 負責評分項 | 分段秒數 | 實際口述（估） |
| --- | --- | --- | --- | --- |
| **LIN Xiaotong (4589755)** | Host / Company & story | #1、#2、全部轉場、3 個互動、Q&A 主持 | 103 | **109 s**（含 Beat 3 poll 6 s） |
| **WENG Zhichao (4589896)** | Database (Part 1) & cost–benefit | #3、#8 | 92 | **92 s** |
| **LIM Mantung (4592996)** | API (Part 2) & Safety/GELSI | #4、#9 | 95 | **95 s** |
| **LAI Patten (4001777)** | Front end (Part 3) & demo A 旁白 | #5、#6a | 100（42 + 58） | **94 s**（42 + 52） |
| **HUANG Haolin (4455930)** | Demo B 旁白、ad campaign、conclusion | #6b、#7、#10 | 98 | **98 s**（53 + 5 + 40） |

- **總長 563 s = 9:23**（含 90 s demo 錄影的旁白 + 75 s 廣告媒體）。Q&A 1 分鐘另計。
- 每人實際口述 92–109 s，全部在 85–110（host 上限 115）之內。
- 6a 的 58 s 由 **host poll（6 s）＋ LAI 旁白（52 s）** 共用；LAI 的分段仍計 58 s／100 s。

**評分順序與秒數骨架（Lecture 17 p.23 順序，不可調換）**

| # | 評分項 | 權重 | 秒 | 講者 | 呈現方式 |
| --- | --- | --- | --- | --- | --- |
| 1 | Company intro + logo + 成員介紹 + 卡通頭像（含開場 poll） | 5% | 50 | LIN Xiaotong | S1→S2 |
| 2 | User Requirements（含「猜 2025 vs 2019」互動） | 5% | 38 | LIN Xiaotong | S3 |
| 3 | Part 1 code | 10% | 42 | WENG Zhichao | S4 |
| 4 | Part 2 code | 10% | 42 | LIM Mantung | S5 |
| 5 | Part 3 code | 10% | 42 | LAI Patten | S6 |
| 6a | Dashboard demo A：S7 錄影前段（globe → map → ranking）＋ Beat 3 poll | 10%（與 6b 合計） | 58 | LAI Patten | S7 內嵌 90 s 影片（0:00–0:44） |
| 6b | Dashboard demo B：錄影後段（sector/weekday → trend/compare/Index → findings → Method/GELSI）＋ S12 客製化 | ↑ | 53 | HUANG Haolin | S7 影片（0:48–1:30）→ S12 |
| 7 | Ad campaign（海報 → S13 內嵌音訊 30 s → 內嵌影片 45 s） | 10% | 80 | HUANG Haolin | S13 |
| 8 | Cost–Benefit | 10% | 50 | WENG Zhichao | S14 |
| 9 | Safety & Responsibility（GELSI） | 10% | 53 | LIM Mantung | S15 |
| 10 | Conclusion | 10% | 40 | HUANG Haolin（host 收尾並交 Q&A） | S16 |
| — | Host transitions（4 段，已嵌入時間軸） | — | 15 | LIN Xiaotong | S3/S16 等 |
| 11 | Presentation Skills | 10% | 全場 | 全員 | — |

> 骨架規定：每段可在 ±3 s 內微調，總和 ≤570 s。本版只做 +2/+1/+1/+1 的微調，總計 **563 s**（與 v1 相同）。

---

## 1. 精確時間軸（含累計時鐘、畫面、播放動作、交接句）

> **投影片編號固定 S1–S17**（deck 已重整品牌，頁序不變）。Demo 不再切瀏覽器：**6a 在 S7 按「PLAY」播內嵌影片，6b 讓同一段影片播完**。
> 「交接句」是該段最後一句英文；下一段的人接著開口。

| # | 評分項 | 秒 | 累計時鐘 | 講者 | 投影片 | 台上畫面 | 播放／操作 | 交接句（English，照念） | 互動 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Company intro + logo + team + avatars | 50 | **0:00 – 0:50** | LIN | S1 → S2 | S1：logo、Carbon Atlas 字標、tagline、problem / mission / brief 三欄；S2：五張成員卡＋卡通頭像＋姓名/ID | [ADVANCE] → 指 logo → 指三欄 → 指成員卡 | *"Every member speaks — English, no notes."*（S2 收句） | **Beat 1 開場舉手 poll（10 s）** |
| 2 | User Requirements | 38 | **0:50 – 1:28** | LIN | S3 | 四個 persona＋五行「問題 → 資料 → route → 圖表」表 | 指 persona → 指表 → 指 requirements chain 收句 | *"Every row ends in a route and a view."*（接 T1） | **Beat 2 猜 2025 vs 2019（10 s）** |
| T1 | → Part 1 | 3 | **1:28 – 1:31** | LIN | S3 → S4 | 交棒畫面 | [ADVANCE] | *"The data starts in MySQL — Zichao."* | — |
| 3 | Part 1 code | 42 | **1:31 – 2:13** | WENG | S4 | CREATE TABLE + LOAD DATA（@dummy、STR_TO_DATE）＋大字 655,200＋驗證列＋Workbench 截圖 | 指 SQL 三段 → 指 655,200 → 指驗證列 | *"Mantung, make it a URL."* | — |
| 4 | Part 2 code | 42 | **2:13 – 2:55** | LIM | S5 | run_sql helper、/api/sectors、JSON 範例、SAFE BY DEFAULT、JSON 截圖 | 指 helper → 指 endpoint → 指 JSON → 指安全兩行 | *"Patten, draw it."* | — |
| 5 | Part 3 code | 42 | **2:55 – 3:37** | LAI | S6 | fetch/map/setOption 程式、browser→Flask→MySQL 流程、本機 assets | 指 fetch → 指 rows.map → 指 markPoint → 指流程圖 | *"That is the code. Here is the recording."* | — |
| 6a | Dashboard demo A（前半段錄影） | 58 | **3:37 – 4:35** | LAI（＋LIN poll 6 s） | **S7（90 s 內嵌影片 0:00–0:44）** | 影片：Stage 主題 hero／globe → map → ranking table | LIN：**"Hands up — India or Russia: who emitted more in 2025?"** → **"India — 3,309. Russia — 1,670."**；LAI：3:43 接麥克風 → 誠實開場句 → **3:51 [PLAY video]** → 指畫面旁白 | *"That is the where."*（接 T2；影片繼續播） | **Beat 3 舉手 poll（6 s）** |
| T2 | → demo B | 4 | **4:35 – 4:39** | LIN | S7（影片繼續） | 影片播到約 0:44–0:48，不停 | 不出手 | *"Patten has the where. Haolin, the what and the when."* | — |
| 6b | Dashboard demo B（後半段錄影） | 53 | **4:39 – 5:32** | HUANG | **S7 影片 0:48–1:30 → S12** | 影片：sector bars → weekday → trend/compare/Index → findings → Method/GELSI（約 5:21 播完）→ S12 客製化對照 | [POINT] 影片；影片結束（約 5:21）[ADVANCE to S12]；指 S12 表格 | *"The product is done. Now the campaign."*（接 S13） | — |
| 7 | Ad campaign | 80 | **5:32 – 6:52** | HUANG | S13 | 海報圖＋AUDIO 0:30 卡＋VIDEO 0:45 卡＋共用句子 | [POINT 海報] → **[PLAY audio，內嵌]** 30 s → **[PLAY video，內嵌]** 45 s → 指共用句 | *"One message, three media."*（接 T3） | 媒體播放（30 + 45 s） |
| T3 | → cost–benefit | 3 | **6:52 – 6:55** | LIN | S13 → S14 | 交棒畫面 | [ADVANCE] | *"Weng, the business case."* | — |
| 8 | Cost–Benefit | 50 | **6:55 – 7:45** | WENG | S14 | 成本/效益表＋三個 KPI（≈17 個月、2.17:1、+HK$37,254）＋「not claiming」虛線框＋假設句 | 指表 → 指 KPI → 指虛線框 | *"Mantung, the responsibility side."* | — |
| 9 | Safety & Responsibility（GELSI） | 53 | **7:45 – 8:38** | LIM | S15 | GELSI 五列（G/E/L/S/I：risk → what we do）＋coverage 39 series 限制條 | 逐列指五個字母 → 指 coverage strip | *"Haolin, bring it home."* | — |
| 10 | Conclusion | 40 | **8:38 – 9:18** | HUANG | S16 | 三點回顧＋四個數字 chip＋金句＋honest next | 指三點 → 指 chips → 放慢念金句 | *"Thank you."*（接 T4） | — |
| T4 | Host 收尾 + 交 Q&A | 5 | **9:18 – 9:23** | LIN | S16 → S17 | S17：Thank you / Questions — and one for you.＋我們給下一組的問題＋出處 | [ADVANCE] 到 S17 | *"Thank you. Questions — and we have one for the next group."* | — |
| — | **Q&A** | 60 | **9:23 – 10:23** | LIN 主持、全員答 | S17（留在畫面） | S17 頁不切走 | — | 見第 4 節 | 必要時問下一組問題 |

**總計：50 + 38 + 3 + 42 + 42 + 42 + 58 + 4 + 53 + 80 + 3 + 50 + 53 + 40 + 5 = 563 s = 9:23。**

**S7 影片時鐘（單獨記，避免旁白對不上畫面）**

| 影片時間 | 實際時鐘 | 畫面 | 誰旁白 |
| --- | --- | --- | --- |
| 0:00 | **3:51**（6a 的第 14 秒按 PLAY） | Stage 主題 hero／globe 旋轉 | LAI |
| 0:12 | 4:03 | 世界地圖 + country focus | LAI |
| 0:28 | 4:19 | ranking table、sparkline、vs 2019 欄 | LAI |
| 0:44 | **4:35** | 影片播到 ranking 尾段 → 進 T2 | LAI 收句；LIN T2 |
| 0:48 | **4:39** | 影片：sector／weekday 開始 | HUANG |
| 1:00 | 4:51 | sector（Power／Industry） | HUANG |
| 1:08 | 4:59 | trend、compare、Index | HUANG |
| 1:20 | 5:11 | findings、Method／GELSI | HUANG |
| 1:30 | **5:21** | 影片結束，切 S12（S12 到 5:32） | HUANG |

> **對不上時的補救**：旁白以「畫面現在顯示什麼」為準，不以秒數為準；影片比預期慢 2–3 s 就直接跳到下一個畫面關鍵詞講（見 `07` 的「旁白落後」處理）。

---

## 2. 秒數核算

### 2.1 每人說話秒數

| 成員 | 分段分配 | 實際口述（含 video voiceover／poll） | 判定（85–110；host ≤115） |
| --- | --- | --- | --- |
| LIN Xiaotong | 50 + 38 + 15 = **103 s** | **109 s**（Beat 3 poll 6 s） | ✅ host 上限內 |
| WENG Zhichao | 42 + 50 = **92 s** | **92 s** | ✅ |
| LIM Mantung | 42 + 53 = **95 s** | **95 s** | ✅ |
| LAI Patten | 42 + 58 = **100 s** | **94 s**（42 + 開場 5 + 旁白 47） | ✅ |
| HUANG Haolin | 53 + 5 + 40 = **98 s** | **98 s** | ✅ |
| **合計** | **488 s**（分段） | **488 s** | — |
| 廣告媒體 | 30 s 音訊 + 45 s 影片 | **75 s** | — |
| **全場** | 488 + 75 | **563 s = 9:23** | ✅ |

- 90 s demo 錄影是 **6a + 6b 的背景畫面**，旁白疊在影片上，不另外加時間；它不是「第 4 段媒體」。
- Beat 3 poll 的 5 s 由 host 在 6a 內帶，所以 LAI 的實際口述比 6a 分段少 5 s；兩人都仍在 85–110 內。

### 2.2 Buffer 計算

| 對照 | 秒數 | Buffer |
| --- | --- | --- |
| 目標帶上限 9:28 | 568 s | **5 s**（計劃 563 s） |
| 排練內部上限 9:30（講義建議流程，非硬規則） | 570 s | **7 s** |
| 規則硬上限 10:00 | 600 s | **37 s** |
| 目標帶下限 9:18 | 558 s | 計劃比下限多 5 s，屬安全中位 |

- 媒體時間固定：**90 s demo 錄影**（6a+6b 內）＋**75 s 廣告**（S13 內）。
- 若影片播放比預期慢：旁白照「畫面」走，不要加速；時間由 6b 後面約 14 s 的 S12 段吸收。

---

## 3. 臨場調節：落後 / 超前怎麼辦

**原則**：每段秒數是上限；落後時只刪不影響 rubric 證據的句子；**不能因為影片播放就跳過口述內容**（S7 是唯一 demo 證據）。

### 3.1 落後時（先刪這兩句）

| # | 位置 | 講者 | 刪掉的英文句 | 省下 | 為什麼可以刪 |
| --- | --- | --- | --- | --- | --- |
| **D1** | 6b 影片完結後（S12 前） | HUANG | *"Not a re-skin: ranking table, Index compare, findings, Method — ours."* | **約 6 s** | S12 的對照表仍在畫面；S15/S16 會再回扣「not a re-skin」。 |
| **D2** | 6a 錄影 ranking 段 | LAI | *"The view changes the URL, so a colleague can open exactly what you cited. One click exports the current view."* | **約 7 s** | 影片本身有 ranking 畫面；rubric 不要求逐個互動。 |

- 仍落後 >15 s：刪 **D3**（WENG，成本段）*"A managed-cloud option adds HK$3,000 a year: break-even 24.4 months, net 28,254."*（約 5 s）。
- **絕對不可刪**：三個互動、S15 五列、廣告 75 s、結論金句、S7 影片本身。

### 3.2 超前時（只加這兩段）

| # | 位置 | 講者 | 加的口述／動作 | 增加 | 素材來源（已核實） |
| --- | --- | --- | --- | --- | --- |
| **E1** | 6a 錄影 ranking 段 | LAI | [POINT 影片] *"India is 8.7% — third — and Russia 4.4% — fourth. Five countries are 61%."* | **約 7 s** | India 3,309（8.7%）、Russia 1,670（4.4%）、top five 61.0% |
| **E2** | 6b 錄影 trend 段 | HUANG | [POINT 影片] *"April 2020 was the lowest month in our snapshot: 2,477 MtCO₂ — 14.3% below April 2019."* | **約 6 s** | 已核實 2020-04 數字 |

- 超前 >13 s：不要加新內容；把「前五大國家 = 61.0%」這類已講過的數字留給 Q&A；或讓影片多播 2 秒再開口。
- **不要**為了填時間重播影片或重講已播過的畫面。

### 3.3 超時紅線（給 HUANG 的計時器）

- **5:21** 影片還沒播完 → 立刻切 S12（影片可在 PowerPoint 按暫停），照 D1 講，接廣告。
- **8:38** 還沒進 S16 → 直接結論，跳過 E1/E2。
- **9:18** 還沒講完結論最後一句 → 直接說金句 + 交 host，剪掉「next, honestly」。
- **9:30** 一定停；Q&A 由 host 接手。

---

## 4. Q&A 1 分鐘交接計劃

**時間**：9:23–10:23（S17 畫面不切走）。Host 主持，全員在場。

### 4.1 Host 開場與結束（英文照念）

- 開場（T4 已說）：*"Thank you. Questions — and we have one for the next group."*
- 中段節奏：*"One at a time, please — we have about a minute."*
- 收尾：*"Thank you — that's our minute."*

### 4.2 題目路由（誰答什麼，每人只答 20 s 內）

| 題目類型 | 主答 | 補一句 | 證據 pointer |
| --- | --- | --- | --- |
| 為什麼 demo 是錄影？／為什麼不即場跑？ | **LAI** | LIN（場地限制） | S7 影片、S8–S11 備援截圖、`07` fallback |
| 資料從哪來 / 可不可信 / 2026 partial | **WENG** | LIM（API 一致性） | S11 Method、`/api/health`、`/api/country_ytd` |
| 成本 / 效益 / 售價 / 利潤 | **WENG** | — | S14、`cost_benefit.xlsx` Assumptions |
| API / SQL injection / JSON 503 / 安全 | **LIM** | WENG（DB 權限） | S5、`app.py` `run_sql()`、`/api/health` |
| Dashboard / UX / 客製化 / 無障礙 | **LAI** | HUANG（findings） | S12、S7 影片、Method 面板 |
| GELSI / 倫理 / 法律 / 社會責任 | **LIM** | LIN（補充治理） | S15、L19 GELSI 框架、Method 面板 |
| 廣告 / 品牌 / 故事 / 結論 | **HUANG** | LIN（pitch 框架） | S13、`ads/` 三份腳本 |
| 「這和 bonus dashboard 有何不同？」 | **LIM 或 LAI**（誰近誰答） | HUANG | S12、`shots/atlas/deck1-stage-hero.png` 等截圖 |
| 「你們下一步做什麼？」 | **HUANG** | — | S16 next 句 |
| 不確定的數字 | **LIN** | — | *"That number is not in our data; we can check after the session."*（不可臨場編） |

### 4.3 必問下一組的問題（Lecture 17 錄音要求：每組至少向其他組問一題）

- **英文**：*"Which chart in your dashboard changed a decision — and how would you prove it?"*
- 位置：S17 頁面中央。問的時機：評審問完 1–2 題後、或 Q&A 過 45 s 仍無人舉手、或結束前 10 s 補問。
- **注意**：這是評分項，不可以漏；問完不需等對方在台上回答，點到即可。

### 4.4 時間控制

- HUANG 用手勢計時：**30 s**（握拳一次）、**50 s**（手掌向下壓）、**60 s**（收）。
- Host 在 50 s 說：*"One last question."*；60 s 說收尾句。
- 若 Q&A 冷場：host 先問下一組問題 → 再自問自答一題（用 Q&A cheat sheet Q2 的 partial-year 答案），確保 1 分鐘不空白。

---

## 5. 上台前 30 分鐘 Pre-flight（Windows 教室）

| 項目 | 負責人 | 檢查內容 | 失敗備案 |
| --- | --- | --- | --- |
| USB / 檔案 | WENG | USB 內有：**最終 `Carbon_Atlas_Deck.pptx`（含 S7 影片、S13 音訊＋影片）**、`Carbon_Atlas_Deck.pdf`、`out/screenshots/atlas/*.png` 備援圖 | 用 PDF 簡報；截圖用備援圖 |
| 教室電腦 | HUANG | 提前到場把 PPTX 複製到桌面；確認 PowerPoint 開得起來、16:9、影片／音訊**內嵌可播** | 用 PDF；影片失敗見 `07` |
| 音量 | HUANG | 播 5 秒 S13 音訊測音量，設 70%；確認喇叭有聲 | 提高系統音量；再不行口述三媒體句 |
| S7 影片 | LAI | 開到 S7，試播 3 秒再按暫停到第一幀；確認 90 s 版本、Stage 主題、字幕清楚 | 用 S8–S11 截圖（`07` 的錄影失敗 fallback） |
| S13 媒體 | HUANG | 試播 audio 3 秒、video 3 秒；確認聲音與畫面 | 口述三媒體內容（`07`） |
| 簡報模式 | HUANG | Slide Show 全螢幕、Presenter View 關閉（評審只看投影）；游標隱藏 | 用 F5 |
| 海報 | HUANG | A3 已印、面朝觀眾、放在講台側 | 用 PDF 版 A3 |
| MySQL / API | — | **不需要**：場地不跑瀏覽器、不跑 server；不要嘗試在教室電腦啟動 | 不處理 |
| 手機 | 全員 | 靜音（Lecture 17 p.20 明說電話響會扣分） | — |
| 筆記 | 全員 | 台上不帶紙本；cue card 只留在後台／排練 | — |

---

## 6. 已同步狀態（Lead 更新，2026-11-18 17:10）

| # | 之前的不一致 | 現在 |
| --- | --- | --- |
| 1 | S7 未嵌入 demo 影片 | ✅ 已嵌入 `Carbon_Atlas_Deck.pptx` S7（90.00 s，H.264 MP4，海報幀 = Stage hero 截圖，點擊播放） |
| 2 | S13 未嵌入音訊/影片 | ✅ 已嵌入 30 s 音訊（MP3）與 45 s 影片（MP4），海報按鈕「PLAY 30 s AUDIO / PLAY 45 s AD」；獨立檔在 `ads/audio`、`ads/video` |
| 3 | Campaign line 用字不一致 | ✅ 全統一為 **"37,856 million tonnes a year. Now find the part you can move."**（deck S13、海報、音訊、影片） |
| 4 | 影片分鏡仍是舊品牌 | ✅ `ads/video_storyboard.zh.md` 已改 Carbon Atlas / 新 tagline |
| 5 | `BRAND.tagline` 常數仍是舊句 | ✅ 已改 **See every tonne. Cut what matters.**（影片錄製後才改，畫面已用新句） |
| 6 | Deck 備忘稿仍是 1.0 版分工 | ⚠️ 未改（不影響演出：台上不可用筆記）；**以本資料夾 00–08 為唯一講稿** |
| 7 | S2 仍寫 LIVE DEMO | ✅ 已改 `FRONT END & DEMO` |
| 8 | 90 s demo 未錄 | ✅ 已錄好：`ads/video/carbon_atlas_demo_90s.mp4`（90.00 s，1280×720，16:9，Stage 主題） |

> **仍待團隊完成**：Patten 真人聲重錄（30 s + 45 s）、Windows PowerPoint 實機試播媒體、Workbench 截圖、全組 9:23 排練、Moodle 提交。

## 7. 檔案索引（本資料夾）

| 檔案 | 用途 |
| --- | --- |
| `00_run_of_show.zh.md` | 本文件：時間軸、秒數核算、Fallback 調節、Q&A 交接、場地 pre-flight |
| `01_host_LIN_Xiaotong.md` | Host 全稿：開場、需求、3 個互動、4 段轉場、Q&A 主持、收尾 |
| `02_WENG_Zhichao.md` | Part 1 code + Cost–Benefit |
| `03_LIM_Mantung.md` | Part 2 code + Safety & Responsibility（GELSI） |
| `04_LAI_Patten.md` | Part 3 code + demo A（S7 90 s 錄影前段旁白） |
| `05_HUANG_Haolin.md` | Demo B（錄影後段旁白）+ Ad campaign（S13 內嵌媒體）+ Conclusion |
| `06_qa_cheatsheet.zh.md` | 10 題 Q&A（英文答案＋中文註記＋證據 pointer） |
| `07_interaction_plan.zh.md` | 3 個互動 beat＋PPT 媒體失敗 fallback |
| `08_host_cue_card.md` | Host 一頁 A4 cue card（後台／排練用，不上台） |

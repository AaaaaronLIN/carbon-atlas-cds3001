# 04 · LAI Patten (4001777) — Part 3 code + Dashboard demo A（v2：S7 錄影版）

> **角色**：Front end (Part 3) & demo A 旁白。**負責評分項**：#5 Part 3 code（10%）· #6a Front-End Dashboard demo A（10%，與 HUANG 的 6b 合計）。
> **投影片**：S6（Fetch, transform, draw）→ **S7 內嵌 90 秒 demo 錄影**（S8–S11 為 fallback 截圖）。
> **說話時間**：42 + 58 = **100 秒分段**（實際口述約 **94 s**；6a 內含 host poll 6 s）。**台上不可帶筆記**；本檔只作排練用。
> **場地**：Windows 教室電腦，**只有 PowerPoint**；不開瀏覽器、不跑 server、不碰 MySQL。
> **操作責任**：6a 由你把 S7 的內嵌影片按 PLAY、盯住播放；影片不會切頁。簡報切頁由 HUANG 控制。
> **Q&A 主答**：dashboard／UX／客製化／無障礙／「demo 為何是錄影」。

**朗讀圖例**：[PAUSE] · [POINT 畫面] · [PLAY] = 按 S7 影片播放 · ⏱ = 相對秒數。

---

## A. Part 3 code — S6（42 s）

**上台起點**：時鐘 **2:55**（LIM 交棒後）· S6 在畫面上。

> ⏱ [0:00] **Part 3 is three moves: ask, reshape, draw.**
>
> ⏱ [0:05] [POINT `fetch`] **Ask the API: fetch the route.**
>
> ⏱ [0:09] [POINT `rows.map`] **Reshape the rows — no numbers are hard-coded in the page. If a query changes, every chart follows.**
>
> ⏱ [0:18] [POINT `setOption`] **Then draw: hand a config to ECharts.**
>
> ⏱ [0:22] [POINT `markPoint`] **April 2020 is an annotation here — not a second data source.**
>
> ⏱ [0:27] [POINT 流程圖] **Browser → Flask → MySQL. One chain — so when something breaks, we know which layer to inspect.**
>
> ⏱ [0:35] [POINT 底部 assets 行] **Both assets are bundled locally: ECharts and the world map. The build runs with the Wi-Fi off.**
>
> ⏱ [0:40] **That is the code. Here is the recording.**

【中文註記 — 為什麼這樣講才有分】
- Part 3（10%）評分要求：**解釋網頁怎樣呼叫 API、轉換資料及繪圖；不能由前端畫面代替程式說明**。這段三個動作（fetch / map / setOption）逐字對應 rubric 的「呼叫、轉換、繪圖」，再加 annotate 與資料流，正好補上「不能只有 demo」。
- 「no numbers are hard-coded」是加分句；「Wi-Fi off」說明本機 assets，也幫 v2 的「錄影也能在任何 laptop 播」鋪路。
- 不要逐行念程式；每個 [POINT] 指到就往下。

**忘詞備援**：記三個動詞 **ask / reshape / draw**；每忘一句就回到下一個動詞。

---

## B. Dashboard demo A — S7 錄影（58 s 分段）｜globe → map → ranking（影片 0:00–0:44）

**上台起點**：時鐘 **3:37** · 已 [ADVANCE] 到 S7 · **影片停在第 0 幀**。
**Beat 3 由 host 帶（0:00–0:06）**：host 說 **"Hands up — India or Russia: who emitted more in 2025?"** → **"India — 3,309. Russia — 1,670."** 你趁這 6 秒 [ADVANCE] 到 S7、把游標移到影片播放鍵；**不要說話**。

> ⏱ [0:06]（3:43 接麥克風，誠實開場）**This is a recording of the build running from MySQL on our machine — on this machine we show the recording.**
>
> ⏱ [0:14]（**3:51**）**[PLAY — S7 內嵌 90 s 影片，0:00 開始]**（不要停、不要點其他東西）
>
> ⏱ [0:16]（影片：globe）[POINT 畫面] **The globe is the front door — drag to spin, click a country. Thirty-nine monitored series, one planet.**
>
> ⏱ [0:25]（影片：map）**The map answers where. China is 31.9% of the 2025 world total; the top five are 61%.**
>
> ⏱ [0:34]（影片：ranking table）**The table answers who: sortable, with sparklines, and a like-for-like column against 2019 — so a partial year cannot look like progress.**
>
> ⏱ [0:45]（影片：URL／CSV 段）**The view changes the URL, so a colleague can open exactly what you cited. One click exports the current view.** ←（**D2 可刪句**，落後時整句略過）
>
> ⏱ [0:56] **That is the where.**（影片繼續播；交給 host T2）

**旁白原則**：眼睛看畫面，嘴巴說畫面現在顯示的東西。若影片比預期慢 2–3 秒，直接跳到下一個畫面關鍵詞；**不要重播、不要道歉、不要說「等一下」**。

**影片不播／中途卡住 — 逐字 fallback（Lead 指定的一句話 + 截圖）**
> [按 PLAY 一次仍然沒反應，或卡住超過 2 秒] **"The recording will not play on this machine — the same view is on this slide."** [ADVANCE 到 S8]
> 然後用 **S8 截圖**把 globe/map/ranking 三段講完（約 40 s，照上面同樣內容，把 [POINT 畫面] 改指 S8 的地圖與表格），收句 **"That is the where."**
> **不要**在台上重開 PowerPoint、不要找檔案、不要開任何其他程式；**不要**試著連 MySQL（場地沒有 server）。

**其他播放小狀況**：
- 影片有聲但很小：**不要**調 PowerPoint 音量條；HUANG 已在 pre-flight 設 70%。繼續講大聲一點。
- 影片畫面被切到／比例不對：直接繼續講；評審看到的是「有 dashboard 的畫面」，不必修正。
- 播放到一半 PowerPoint 跳回桌面：說 **"One second — the recording is still on this slide."** 按 Alt+Tab 回 PowerPoint，按一次 PLAY；不要重播整段。

【中文註記 — 為什麼這樣講才有分】
- Front-End Dashboard（10%）要求**客製化 UI 的視覺化與互動**。錄影裡的四個證據：① Stage 主題的 globe hero；② map→全頁聚焦；③ 可排序 ranking＋sparkline＋vs 2019 欄；④ 可分享 URL＋CSV 匯出。旁白逐點點名，評審不必自己找。
- **「This is a recording of the build running from MySQL… recorded, not mocked.」** 是 v2 最重要的一句：誠實說「教室電腦只能播 PowerPoint」，同時強調資料是真的（真的 MySQL build 錄下來的），不是假畫面。Lecture 17 明確禁止把未完成功能說成已完成；這句把兩邊都守住。
- 五大國 61% 是「客戶洞察」，不是圖表說明：先給結論，再指畫面。
- 你的台詞約 95 字，其餘時間留給影片畫面與停頓；**慢一點**比念完更重要。

---

## C. 交接（給 host T2）

- 收句：**"That is the where."** 影片繼續播（約影片 0:44），你退半步；host T2 說 **"Patten has the where. Haolin, the what and the when."**
- 6b 期間你**不要**碰簡報：影片由 HUANG 接手讓它播完，S12 也由 HUANG 切。你只負責盯 S7 有沒有異常（卡住就低聲提醒 HUANG）。

## D. Q&A 主答題目

1. 「為什麼 demo 是錄影？為什麼不即場跑？」→ *"This classroom machine only shows PowerPoint — no browser, no server. We recorded the build running from MySQL on our own machine so the demo is still real data, not a mock. The recording is our fallback plan, not a workaround for something that does not exist."*
2. 「這和 Moodle bonus dashboard 有何不同？」→ *"We kept the pattern but rebuilt the interface: a sortable ranking table with sparklines and CSV export, an Index · 2019 = 100 compare mode, rule-based findings, a Method panel, offline local assets, and keyboard access. The reference was a starting point, not our submission."*（可與 LIM 分工，一人一句）
3. 「為什麼用 ECharts 不用 Chart.js？」→ *"The brief needed a world map and event annotations. ECharts provides both, and we bundled it locally so the build runs offline. The tutorial's Chart.js exercise taught the fetch-first pattern; we kept the pattern and changed the library to fit the brief."*
4. 「無障礙怎麼做？」→ *"Keyboard-accessible controls, a visible focus state, high-contrast palette, no colour-only encoding, `prefers-reduced-motion` support, and a light theme that prints."*
5. 「Stage 主題／Story mode 是什麼？」→ *"Stage is a presentation theme for projection — same data, higher contrast. Story mode, ▶ Play the brief, is a guided auto-tour of the same panels for a first-time user; in a client meeting we drive manually so we can answer questions."*

## E. 個人排練檢查

- [ ] Part 3：ask / reshape / draw 三段各一句，42 秒內收；收句改為 **"Here is the recording."**
- [ ] S7 試播 10 次以上，每次都能在影片第 0 幀按 PLAY；知道影片總長 90 秒、影片結束時會停在最後一幀。
- [ ] 旁白與影片畫面同步：globe（0:12）、map（0:20）、ranking（0:30）、URL/CSV（0:42）四段能在正確畫面開口。
- [ ] 練一次「影片不播」fallback：一句英文 + 切 S8 + 照念 40 秒；不要重開 PowerPoint。
- [ ] 全程不碰 terminal、不開瀏覽器、不開任何檔案總管。

# 04 · LAI Patten (4001777) — Part 3 code + Dashboard demo A（v3：S7 现场 live，fallback 錄屏）

> **角色**：Front end (Part 3) & demo A 旁白。**負責評分項**：#5 Part 3 code（10%）· #6a Front-End Dashboard demo A（10%，與 HUANG 的 6b 合計）。
> **投影片**：S6（Fetch, transform, draw）→ **S7 现场 live 90 秒**（教室浏览器；S7 内嵌錄屏 + S8–S11 截图为 fallback）。
> **說話時間**：42 + 58 = **100 秒分段**（實際口述約 **94 s**；6a 內含 host poll 6 s）。**台上不可帶筆記**；本檔只作排練用。
> **場地**：Windows 教室電腦 + 浏览器；Mac 跑 Flask/MySQL；Live 操作见 `LIVE_DEMO_OPERATOR_CARD.md`。
> **操作責任**：6a 由你 Alt+Tab 到浏览器、按 live cue 点击；失败 5 秒内 Alt+Tab 回 PPT 播 S7 錄屏。簡報切頁由 HUANG 控制。
> **Q&A 主答**：dashboard／UX／客製化／無障礙／「live 还是錄屏、网络失败怎么办」。

**朗讀圖例**：[PAUSE] · [POINT 畫面] · [Alt+Tab] = 切浏览器/PPT · [PLAY] = 只用于 fallback 的 S7 錄屏 · ⏱ = 相對秒數。

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
> ⏱ [0:40] **That is the code. Let me open the live build.**

【中文註記 — 為什麼這樣講才有分】
- Part 3（10%）評分要求：**解釋網頁怎樣呼叫 API、轉換資料及繪圖；不能由前端畫面代替程式說明**。這段三個動作（fetch / map / setOption）逐字對應 rubric 的「呼叫、轉換、繪圖」，再加 annotate 與資料流，正好補上「不能只有 demo」。
- 「no numbers are hard-coded」是加分句；「Wi-Fi off」說明本機 assets，也幫 v2 的「錄影也能在任何 laptop 播」鋪路。
- 不要逐行念程式；每個 [POINT] 指到就往下。

**忘詞備援**：記三個動詞 **ask / reshape / draw**；每忘一句就回到下一個動詞。

---

## B. Dashboard demo A — S7 **live**（58 s 分段）｜globe → map → ranking（页面 0:00–0:44）

**上台起点**：时钟 **3:37** · S7 在画面上 · 浏览器已打开、F11、URL 已预热（LAI 在 3:37 前完成）。
**3:37–3:43 你自己说产品 bridge**：**"Remember the number: 37,856 million tonnes a year. Let me show you where it comes from."** 说完把鼠标放在浏览器标签页上；3:43 接麦。

> ⏱ [0:06]（**3:43**，接麦克风，诚实开场）**This is the live build — MySQL → Flask → this page. Every number below is a SQL query, not a screenshot.**
>
> ⏱ [0:11]（**3:48**）**[Alt+Tab — 切到浏览器，F11 全屏]**（不要点 S7 视频；视频是 fallback）
>
> ⏱ [0:13]（页面：globe）[拖一下地球] **The globe is the front door — drag to spin, click a country. Thirty-nine monitored series, one planet.**
>
> ⏱ [0:22]（页面：Where；点 **China**）**The map answers where. China is 31.9% of the 2025 world total; the top five are 61%.**
>
> ⏱ [0:32]（页面：ranking；点 **VS 2019** 排序）**The table answers who: sortable, with sparklines, and a like-for-like column against 2019 — so a partial year cannot look like progress.**
>
> ⏱ [0:42]（页面：URL／CSV 小字）**The view changes the URL, so a colleague can open exactly what you cited. One click exports the current view.** ←（**D2 可删句**，落后时整句略过）
>
> ⏱ [0:56]（页面仍停在 ranking）**That is the where.**（live 继续；交给 host T2）

**旁白原则**：眼睛看浏览器，嘴巴说当前画面。live 没有固定帧率；如果 LAI 点慢了 2–3 秒，直接跳到下一个画面关键词；**不要重播、不要道歉、不要催 LAI**。

**live 打不开／断网 — 5 秒 fallback（Lead 指定的话）**
> [页面 5 秒没出来，或 URL 报错] **"I'll show the recorded build."** [Alt+Tab 回 PPT → 点 S7 海报，播 90 秒录屏]
> **S7 錄屏本身沒有聲音**：你繼續現場講，不要等聲音、不要臨時找配音。
> 然后按原录屏版旁白讲完 6a：globe → map → ranking；收句 **"That is the where."**
> **不要**在台上重启 MySQL／tunnel／浏览器；**不要**找文件；**不要**让 HUANG 接手鼠标。5 秒内没恢复就走 fallback。

**其他小状况**：
- 页面图表还没画完：先讲 hero/地球，等 1 秒再滚 Where。
- 浏览器 URL 栏露出来：按 Ctrl+L 后 Esc（或 F11 再按一次），不要现场解释。
- 投影分辨率小：Ctrl+- 到 90/80%，继续讲；不要在台上调系统设置。

【中文註記 — 為什麼這樣講才有分】
- live 的最大加分是 **"every number is a SQL query"**：现场运行、真实 API，不是截图。
- 四个必须点到的证据：① live globe；② map→China；③ ranking 可排序 + sparkline + vs 2019；④ URL/CSV。
- 同时保留诚实边界：如果 live 失败，立刻说 "I'll show the recorded build"；录屏是同一版本，不假装 live。
- 五大国 61% 是客户洞察，先给结论再指画面。
- 你的台词约 95 字，其余时间留画面与停顿；**慢一点**比念完重要。

---

## C. 交接（給 host T2）

- 收句：**"That is the where."** live 继续，你退半步；host T2 說 **"Patten has the where. Haolin, the what and the when."**
- 6b 期間你**繼續控浏览器**（滾動/選國家）；HUANG 只講，不碰電腦。S12 由 HUANG 切；你負責 live 頁面別卡住。

## D. Q&A 主答題目

1. 「為什麼 demo 是 live／如果网络坏了怎么办？」→ *"This is the live build: the browser reads our Flask API, which queries the MySQL table built in Part 1. The classroom network is the only variable — if it fails, the same build is embedded as a 90-second recording on the same slide, and we switch in five seconds. The data is real either way; the recording is a fallback, not a mock."*
2. 「這和 Moodle bonus dashboard 有何不同？」→ *"We kept the pattern but rebuilt the interface: a sortable ranking table with sparklines and CSV export, an Index · 2019 = 100 compare mode, rule-based findings, a Method panel, offline local assets, and keyboard access. The reference was a starting point, not our submission."*（可與 LIM 分工，一人一句）
3. 「為什麼用 ECharts 不用 Chart.js？」→ *"The brief needed a world map and event annotations. ECharts provides both, and we bundled it locally so the build runs offline. The tutorial's Chart.js exercise taught the fetch-first pattern; we kept the pattern and changed the library to fit the brief."*
4. 「無障礙怎麼做？」→ *"Keyboard-accessible controls, a visible focus state, high-contrast palette, no colour-only encoding, `prefers-reduced-motion` support, and a light theme that prints."*
5. 「Stage 主題／Story mode 是什麼？」→ *"Stage is a presentation theme for projection — same data, higher contrast. Story mode, ▶ Play the brief, is a guided auto-tour of the same panels for a first-time user; in a client meeting we drive manually so we can answer questions."*

## E. 個人排練檢查

- [ ] Part 3：ask / reshape / draw 三段各一句，42 秒內收；收句改為 **"Let me open the live build."**
- [ ] live 全流程練 10 次以上：S7 → Alt+Tab → F11 → 90 秒 click cue → Alt+Tab 回 PPT；知道 URL 已预热。
- [ ] 旁白與 live 画面同步：globe、Where/China、ranking、URL/CSV 四段能在正确画面开口。
- [ ] 練一次「live 打不開」fallback：说 "I'll show the recorded build." + Alt+Tab + 点 S7 錄屏；≤5 秒。
- [ ] 提前 30 分鐘測 URL/F11；全場不碰 terminal、不在台上 debug。

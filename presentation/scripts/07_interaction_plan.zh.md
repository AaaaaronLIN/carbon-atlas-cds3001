# 07 · Interaction Plan（3 個互動 beat）＋ Live / Media Failure Fallback（v3）

> 這份文件給三種人看：**host**（誰說話／何時救場）、**操作者**（誰按什麼）、**計時者**（容許秒數）。
> **v3 場地事實**：Windows 教室電腦 + 浏览器；Mac 跑 Flask/MySQL；S7 优先 live（tunnel/LAN），失败 5 秒切 S7 录屏；有声音输出；USB 备份。
> 原則：互動是節奏，不是風險。任何互動**最多 10 秒**；觀眾不接球，host 用準備好的數據自答，**不冷場、不重複問**。

---

## Beat 1 · 開場舉手 poll（Section 1，#Company intro）

| 項目 | 內容 |
| --- | --- |
| 位置 | 時鐘 **0:06–0:16**（Section 1 內） |
| 秒數預算 | **10 s**（含兩次停頓）；硬上限 12 s |
| 操作者 | **無**（host 一人完成；LAI / HUANG 在側邊站定） |
| 目的 | 讓觀眾在 15 秒內從「聽眾」變成「參與者」；也把「有數字、沒有 sector」的落差變成 pitch 的缺口。 |

**Host 逐字**
> **"Quick show of hands: who has read a carbon number this week?"** [PAUSE 2]
> **"Keep it up if you could name the sector."** [PAUSE 2]
> **"Almost none. That is the gap we sell against."**

**預期反應**：第一個問題 3–6 隻手；第二個問題 0–2 隻手。若有人喊答案，host 點頭說 **"Good — write it down."** 再繼續。

**觀眾沉默的 fallback（host 自答 + 數據）**
> **"No hands — fine. The number is public anyway: 37,856 million tonnes in 2025. What is missing is where it comes from."** [PAUSE]（不要再問第二次；直接接 "Our product is Carbon Atlas."）

**超時處理**：若已超過 12 s，刪掉第二問，直接說 **"Almost none. That is the gap."** 接產品名。

---

## Beat 2 · 猜 2025 vs 2019（Section 2，#User Requirements）

| 項目 | 內容 |
| --- | --- |
| 位置 | 時鐘 **0:50–1:00**（Section 2 開頭） |
| 秒數預算 | **10 s**；硬上限 12 s |
| 操作者 | **無**（host 一人完成；WENG 在 S4 就位） |
| 目的 | 用「猜」把 2019→2025 的 +4.0% 種進評審腦裡，也自然接到需求表的「How has it moved?」。 |

**Host 逐字**
> **"Quick guess — 2025 versus 2019: has the world's CO₂ gone up or down? And by how much?"** [PAUSE 2]
> **"Up — 4.0%."** [PAUSE] **"36,397 to 37,856. Eight years, and no real decline."**

**預期反應**："down"（最常見，因為新聞常說減排）、"flat"、"10%"、"5%"。若有人喊「down」：不要停留，直接 **"Up — 4.0%."** 給正確方向。

**觀眾沉默的 fallback（host 自答 + 數據）**
> **"I'll answer it: up 4.0% — 36,397 to 37,856. Eight years, no real decline."** [PAUSE]（直接接 "Four users — analyst, researcher, journalist, student — and five questions."）

**超時處理**：若已超過 12 s，只說答案 **"Up 4.0% — 36,397 to 37,856."** 立刻接 requirements。

---

## Beat 3 · 舉手：印度 vs 俄羅斯（Demo A 前的 PowerPoint-safe poll）

| 項目 | 內容 |
| --- | --- |
| 位置 | 時鐘 **3:37–3:43**（6a 的頭 6 秒） |
| 秒數預算 | **6 s**；硬上限 8 s |
| 操作者 | **LAI**：在这 6 秒 [ADVANCE] 到 S7、把浏览器标签页准备好（**不说话**）；**host**：问与答；**HUANG**：不动，准备 4:39 接手旁白 |
| 目的 | 让评委参与；同时给 LAI 一个自然的“准备浏览器”窗口。 |

**Host 逐字**
> **"Hands up — India or Russia: who emitted more in 2025?"** [PAUSE 2]
> **"India — 3,309. Russia — 1,670."** [PAUSE]

**預期反應**：可能喊 "Russia"（直覺認為俄羅斯更大）、"India"、或沉默。處理方式：
- 有人喊 "Russia" → **"Good guess — India, 3,309. Russia, 1,670. Nearly double."**（3,309 / 1,670 約 2 倍）
- 有人喊 "India" → **"Correct — 3,309 versus 1,670."**
- 完全沉默 → host 直接自答上面兩句，**不要重問**。

**Fallback 重點**：這題只用已核實數字（India 3,309、Russia 1,670，2025 世界排名第 3 與第 4），不延伸、不報其他國家百分比。

**超時處理**：6 秒一到，host 收（"India — 3,309" 那句講完就停）；LAI 在 3:43 必須接麥克風說誠實開場句，**不能靠 poll 拖延**。

**為什麼這樣設計**：v3 是 live，但 6 秒內不可能让观众上台点击；举手 poll 仍是零风险互动，答案（India 8.7%、Russia 4.4%）会在 S7 live ranking 段再次出现。

---

## 互動時間總帳

| Beat | 位置 | 預算 | 硬上限 | 超時處理 |
| --- | --- | --- | --- | --- |
| 1 開場舉手 poll | 0:06–0:16 | 10 s | 12 s | 刪第二問 |
| 2 猜 2025 vs 2019 | 0:50–1:00 | 10 s | 12 s | 只說答案，接 requirements |
| 3 印度 vs 俄羅斯 | 3:37–3:43 | 6 s | 8 s | 講完「India — 3,309」就收 |
| **合計** | — | **26 s** | **32 s** | — |

> 三個 beat 都已含在 563 s 骨架內（Beat 1 在 50 s、Beat 2 在 38 s、Beat 3 在 6a 的 58 s；6a 內 poll 6 s、LAI 52 s）。**若任何 beat 超出硬上限，從該段後面的內容扣**（見 `00` 第 3 節 D1/D2），不延長全場。

---

## Live / Media Failure Fallback（v3 核心備援）

> 主方案是 **live**（Mac Flask+MySQL → 教室浏览器 tunnel/LAN）；fallback 是 **S7 的 90 秒錄屏 + S8–S11 截圖**。所有 fallback 都是：**一句誠實英文 + 5 秒內切回 PPT + 繼續講**。不要找檔案、不要開 terminal、不要在台上修 network。

### ① S7 live 打不开／断网（LAI）

**判断**：Alt+Tab 后 5 秒页面仍空白/转圈，或 URL 报错。
**LAI 逐字**
> **"I'll show the recorded build."** [Alt+Tab 回 PPT → 点 S7 海报，播 90 秒錄屏]
> **S7 錄屏没有声音**：LAI/HUANG 继续现场讲，不要等音频。
**做法**：
1. 5 秒内没出来就切；不要在台上刷新 URL/重启 tunnel。
2. 用录屏按原 6a/6b 旁白讲完 90 秒；5:21 正常切 S12。
3. 若录屏也不播：切 S8–S11 截图讲（见 ②）；全程仍守 563 s。

### ② live 中途卡住／浏览器跳走（LAI 或 HUANG）

- 页面卡住 >2 s：LAI 立刻 **Alt+Tab 回 PPT → 点 S7 录屏**；HUANG 继续同一段旁白，不要等。
- 浏览器跳到别的标签/桌面：Alt+Tab 回 PPT，先播录屏；**不要**在台上找标签页。
- live 页面有图但 API 报错（status pill 红）：切 S7 录屏；不要假装数据正常。

### ③ S13 內嵌音訊／影片不播（HUANG）

（保留原 v2 文案，不变）
**判断**：按 PLAY 后 2 秒无声/无画面。
**一句版**：
> **"The media are embedded on this slide — in one line: the poster, the audio and the video all say 37,856 million tonnes a year; now find the part you can move."**
**长版（约 30–35 秒）**：见 `05_HUANG_Haolin.md` B 段 fallback；然后指 S13 三张卡补到 80 s。

### ④ 整份簡報開不起來／PowerPoint 當機（全員）

- WENG 用 USB 的 **`Carbon_Atlas_Deck.pdf`** 开 PDF 版；流程/秒数不变，S7/S13 媒体改口述。
- 若 PDF 也开不了：host 收在 9:18–9:30，把时间留给 Q&A 的技术深度。
- **不要**在台上重开电脑超过 20 秒。

### ⑤ 其他現場故障 → 對應句

| 故障 | 講者 | 逐字 |
| --- | --- | --- |
| 投影比例／畫面被切 | HUANG | **"One second — the projector is cropping the page; the content is fine."**（5 秒內解決） |
| 麥克風沒聲 | Host | 提高音量、用腹式發聲；不要說「can you hear me」超過一次 |
| 有人電話響 | Host | 不點名、不評論，繼續；排練時全部靜音 |
| 超時（>9:30） | Host | **"Let me stop there — the numbers are on the slide, and we will take your questions."** 直接接 Q&A |
| 浏览器分辨率不匹配 | LAI | Ctrl+- 到 80/90%；不在台上改系统设置 |

---

## 操作者分工表（v2 · pre-flight 前確認）

| 角色 | 人 | 手上控制 | 不可以做 |
| --- | --- | --- | --- |
| S7 live | **LAI** | Alt+Tab 到浏览器、F11、按 operator card 点击；失败 5 秒切回 PPT 播录屏 | 不在台上重启 MySQL/tunnel/找文件 |
| 简报 + S13 媒体 + 计时 | **HUANG** | PowerPoint 切页、S13 内嵌音频/视频 PLAY、音量、计时器 | 不在媒体播放中说话；不重开简报 |
| USB / 檔案 | **WENG** | 开场前确认 USB 有最终 PPTX+PDF+独立 mp4/mp3+截图 | 不在台上找文件、不碰 Mac |
| 主持 / 互动 / Q&A | **LIN** | 全场节奏、三个 poll、Q&A 路由 | 不抢答技术题（交主答） |

> **v3 原则**：live 是加分项，fallback 是底线；教室网络/浏览器任何一步失败，5 秒内切 S7 录屏，不在台上 debug。Mac 由 LAI 在台下控制。

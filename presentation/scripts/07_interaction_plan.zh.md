# 07 · Interaction Plan（1 個互動 beat）＋ Live / Media Failure Fallback（v3）

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
| 目的 | 用「天氣 vs 碳排放」把產品價值講清楚：讓碳排放像天氣一樣容易查。 |

**Host 逐字**
> **"Quick show of hands — who checked the weather this week?"** [PAUSE 2]
> **"Who checked carbon emissions this week?"** [PAUSE 2]
> **"That is the gap. We check what we feel. We don't check what we could change."**

**預期反應**：第一個問題 3–6 隻手；第二個問題 0–2 隻手。若有人喊答案，host 點頭說 **"Good — write it down."** 再繼續。

**觀眾沉默的 fallback（host 自答 + 數據）**
> **"That is the gap. We check what we feel. We don't check what we could change."** [PAUSE]（不要再問第二次；直接接 "Our product is Carbon Atlas."）

**超時處理**：若已超過 12 s，只說 **"That is the gap."** 接產品名。

---

## 3:37 · 產品 bridge（不是互動）

| 項目 | 內容 |
| --- | --- |
| 位置 | 時鐘 **3:37–3:43**（6a 的頭 6 秒） |
| 秒數預算 | **6 s**；硬上限 8 s |
| 操作者 | **LIN** 說一句；**LAI** 趁這 6 秒把瀏覽器準備好（不說話） |
| 為什麼 | 不加第三個互動；用一句產品數字把畫面交給 demo，同時給 LAI 準備時間。 |

**Host 逐字**
> **"Remember the number: 37,856 million tonnes a year. Patten — show us where it comes from."**

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

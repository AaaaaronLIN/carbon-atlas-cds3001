# 30 秒音訊廣告 · 腳本與製作說明

專案：Carbon Atlas（Data Fanatics · Team Data Fanatics · Lingnan University CDS3001）
長度：**30.0 秒整**（含尾音樂，不可超過 30.5 秒）
語言：英語 VO（配音）＋中文製作註記
播放場合：簡報 S13 廣告段（海報之後、影片之前），全長播放一次。

---

## 1. 一句話訊息

> **See every tonne. Cut what matters. — 將近 380 億噸的 CO₂ 每年都在那裡；Carbon Atlas 把它變成一個兩分鐘就能讀完、而且說得出限制的簡報。**

所有文案只支撐這一件事，不出現「拯救地球」「AI 預測」等未實作或誇大的說法。

---

## 2. 逐句腳本（含時間碼）

| # | 時間碼 | 長度 | 英文 VO（照念） | 中文註記（語氣／音效） |
| --- | --- | --- | --- | --- |
| 1 | 0:00–0:05 | 5.0 s | "Nearly thirty-eight billion tonnes of CO₂. **Every year.**" | 開場用「氣聲＋停頓」，不要喊。念完 "CO₂" 後停 0.6 秒，讓數字落地。SFX：鍵盤一聲輕敲（資料感），音樂同時淡入。 |
| 2 | 0:05–0:12 | 7.0 s | "The data is already public: every country, every sector, every day. Six hundred fifty-five thousand rows." | 語速稍快、像陳述事實。"already public" 加重；"Six hundred fifty-five thousand rows" 放慢，這是全段唯一的具體數量。 |
| 3 | 0:12–0:20 | 8.0 s | "Carbon Atlas turns those rows into one honest brief — where emissions come from, what moved, and what the data cannot tell you." | 這句是差異化：講到 "honest" 時降速；"cannot tell you" 要清楚，不能含糊。音樂在此稍微拉高 1 dB 再回落。 |
| 4 | 0:20–0:25 | 5.0 s | "Two minutes. One screen. No spreadsheet." | 三個短句，每句之間 0.3 秒停頓，像打點。SFX：三下輕微 tick（與三個短句對齊）。 |
| 5 | 0:25–0:30 | 5.0 s | "Carbon Atlas. See every tonne. Cut what matters. Ask us for a walkthrough." | 品牌句放慢、平穩；最後一句是 CTA，語氣上揚一點點，不要懇求。尾音樂在 0:29.0 開始收，0:30.0 歸零。 |

**字數**：英文共 73 字，約 146 wpm（廣告正常範圍 140–160）。
**如果錄出來超過 30 秒**：先刪第 2 句的 "every sector"（省 0.7 秒），再刪第 4 句的 "No spreadsheet."（省 0.9 秒）。不要加速整段。

---

## 3. 聲音設計（Sound design）

| 時間 | 元素 | 規格／說明 |
| --- | --- | --- |
| 0:00 | 鍵盤敲擊 SFX | 一聲、乾、近距離；-22 LUFS，不要有殘響 |
| 0:00–0:30 | 音樂底 | 極簡鋼琴／pulse，60–70 BPM，無明顯旋律記憶點（避免版權相似的罐頭音樂）；整體 -20 LUFS |
| VO 出現時 | Ducking | 音樂自動降 6 dB，VO 結束後 0.4 秒回復 |
| 0:20 | 三個 tick | 與 "Two minutes / One screen / No spreadsheet" 對齊，-26 LUFS |
| 0:26 | 品牌 sting | 一個乾淨的低音＋紙張翻頁聲，帶出 CTA |
| 0:30 | 結束 | 音樂歸零，不留尾巴（避免播放器截斷） |

**混音目標**：整體 -16 LUFS integrated，true peak ≤ -1 dBTP。
**格式**：WAV 48 kHz / 24-bit 交付；另存 MP3 320 kbps 給現場播放（檔名 `audio_ad_30s.wav` / `.mp3`）。

---

## 4. 配音指示（VO direction）

- 聲線：中性、低沉、像記者在念一段已核實的數字；不要「廣告腔」。
- 語速：前 20 秒 150 wpm，最後 10 秒降到 135 wpm。
- 重音：第 1 句 **every year**；第 2 句 **already public**；第 3 句 **honest**、**cannot tell you**；第 5 句 **Carbon Atlas**。
- 不需要背景人聲、不需要「專家」假引言（我們沒有受訪者）。

---

## 5. 事實核對（錄音前必看）

| 台詞 | 對應事實 | 出處 |
| --- | --- | --- |
| "Nearly thirty-eight billion tonnes" | 2025 年世界 37,856 MtCO₂ = 378.56 億噸 = 37.9 billion tonnes（四捨五入為 nearly 38 billion） | 世界年度加總 |
| "Six hundred fifty-five thousand rows" | 655,200 筆 | `SELECT COUNT(*)`（見 integration_notes 的數字核對提醒） |
| "where emissions come from, what moved" | 產業／國家／月度趨勢三個面板 | dashboard |
| "what the data cannot tell you" | Method & responsibility 面板（部分年份、覆蓋率） | dashboard |

> 注意：英文是 **billion tonnes**（十億噸），不是 "million"。37,856 **million** tonnes = 37.856 **billion** tonnes。中文說明用「378.56 億噸」就不會混亂。

---

## 6. 使用位置與備註

- 簡報 S13：先展示海報（3 秒），播本音訊 30 秒，再播 45 秒影片。**不要用影片的聲音代替本音訊**——講者已說明影片有聲音不等於交了 audio ad。
- 檔案放在投影片同一資料夾，播放前先試音量（教室音響常偏小，建議系統音量 70%）。
- 若現場無法播放，講者需口述第 5 句品牌句，並說明「audio ad 已隨檔案提交」。

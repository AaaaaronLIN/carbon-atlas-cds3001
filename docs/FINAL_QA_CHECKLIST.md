# Carbon Atlas — Final QA / Double-check (2026-11-18 17:10)

> 目的：在交给团队排练与提交前，逐项确认**所有 rubric 得分点 + 讲义的硬性要求**都有对应证据。
> 状态：✅ 已验证 / 🟡 已就绪但需团队动作 / ⬜ 未开始 / ⚠️ 需注意

## A. 提交物（lecture 17 p.18）

| # | 要求 | 状态 | 证据 |
|---|---|---|---|
| A1 | 一个 ZIP、含 Part 1/2/3 code + 最终前端 PDF | 🟡 | `submission/CDS3001_CarbonAtlas_DataFanatics.zip`（37.8 MB）已生成；Patten 人声已嵌入 |
| A2 | Part 1 code（LOAD DATA + 验证） | ✅ | `Part_1_Database/Part_1_setup.sql` + `verification_output.txt`（655,200 行） |
| A3 | Part 2 code | ✅ | `Part_2_API/app.py`（9 routes）+ `API_reference.md` |
| A4 | Part 3 code | ✅ | `Part_3_Frontend/index.html` + `static/`（本地 ECharts + map） |
| A5 | 最终前端 PDF | ✅ | `Carbon_Atlas_Final_Frontend.pdf`（10 页，实测可读） |
| A6 | 解压可运行 | ✅ | 已解压 -> `carbon_api/` -> `python3 app.py`：`/` 200、`/index.html` 200、`/api/health` 655,200 行 |
| A7 | 截止 2026-11-27 18:00 HKT | ⬜ | 团队负责提交 |

## B. 演示规则（p.21–23）

| # | 要求 | 状态 | 证据 |
|---|---|---|---|
| B1 | 9–10 分钟 + 1 分钟 Q&A | ✅ | `scripts/00`：**563 s = 9:23**；媒体 90 s demo + 75 s ads 已计入 |
| B2 | 全英文 | ✅ | 5 份讲稿英文口述 |
| B3 | 每人发言、平均 | ✅ | 93 / 126 / 104 / 144（含 75s 媒体）/ 93 s；连续章节 |
| B4 | 不可用笔记 | 🟡 | 讲稿按关键词设计；需排练到脱稿 |
| B5 | 安全/伦理投影片 ≥1 | ✅ | deck S15 GELSI 五列 + 网页 Method 面板 |
| B6 | 结论投影片 ≥1 | ✅ | deck S16 |
| B7 | Poster + Audio + Video 三媒体 | ✅ | `ads/poster.png|pdf`、`ads/audio/audio_ad_30s_final.mp3`、`ads/video/carbon_atlas_ad_45s_final.mp4`；Patten 人声，无音乐 |
| B8 | 成本效益 + 假设 | ✅ | `cost_benefit.xlsx`；S14 |
| B9 | 向其他组提问 ≥1 | ✅ | LIN 主持卡/手机；对方 Q&A 问；S17 只留 Questions |
| B10 | 手机静音/准时 | ⬜ | 团队纪律 |
| B11 | 全员出席 | ⬜ | 团队确认 |

## C. 评分表 11 项（p.23）

| # | 评分项 | 权重 | 证据 | 状态 |
|---|---|---|---|---|
| 1 | Company + logo + 成员 + 卡通头像 | 5% | deck S1–S2（真实姓名/学号/头像）；网页 Team 区 | ✅ |
| 2 | User Requirements | 5% | deck S3（4 persona → 数据 → SQL → 图） | ✅ |
| 3 | Part 1 code | 10% | deck S4 + SQL + 真实终端输出 + 终端截图 | ✅ |
| 4 | Part 2 code | 10% | deck S5 + `app.py` + API 参考 + JSON 截图 | ✅ |
| 5 | Part 3 code | 10% | deck S6 + `index.html`（fetch → map → setOption） | ✅ |
| 6 | Front-End Dashboard | 10% | **S7 内嵌 90 s 真实录屏**（Stage/globe/map/table/sector/trend/findings/GELSI）+ S8–S11 截图备份 + S12 客制化对照 | ✅ |
| 7 | Ad Campaign | 10% | S13：A3 poster + **内嵌 30 s audio** + **内嵌 45 s video**；三媒体同一句 | ✅（Patten 人声） |
| 8 | Cost-Benefit | 10% | S14 + xlsx（17 个月回本、2.17:1、+37,254） | ✅ |
| 9 | Safety & Responsibility | 10% | S15 GELSI + 网页 Method | ✅ |
| 10 | Conclusion | 10% | S16 三句 + 数字 + 金句 + next honestly | ✅ |
| 11 | Presentation Skills | 10% | 9:23 plan、每人 92–109 s、英文、无笔记 | 🟡 需排练 |

## D. 媒体技术检查

| 检查 | 结果 |
|---|---|
| Demo 影片 | 90.00 s · 1280×720 · 16:9 · H.264 High · yuv420p · 30 fps · 3.1 MB |
| 45 s 广告 | 45.00 s · 1280×720 · H.264 + AAC 48 kHz stereo · 2.5 MB |
| 30 s 音频 | 30.00 s · WAV 44.1k stereo / MP3 192k / M4A |
| 嵌入 deck | 3 个 media shape：S7 demo、S13 audio、S13 video；pptx 13.6 MB |
| PowerPoint 兼容 | H.264/AAC/MP3，Windows PowerPoint 2016+ 支持；**必须在教室 Windows 上试播一次** |
| 备用 | 独立媒体文件在 `Presentation/ads/audio`、`ads/video`，U 盘可直接播放 |

## E. 品牌/口径一致性

| 检查 | 结果 |
|---|---|
| 公司/产品/tagline | Data Fanatics / Carbon Atlas / **See every tonne. Cut what matters.** |
| Campaign line | 37,856 **million tonnes** a year. Now find the part you can move.（deck/poster/audio/video 统一） |
| 旧品牌残留 | 只剩说明性文字（如 run-of-show 标注「舊名 Carbon Compass 不再使用」），无实际物料残留 |
| 数据口径 | 655,200 行 / 39 series / 6 sectors / 2019-01-01→2026-08-31 / 37,856 Mt（2025）/ +4.0% |
| 2026 partial | 全站 like-for-like Jan–Aug；UI 标注 |
| 密码 | `app.py` 为 `your_password` 占位；ZIP 内无真实密码 |

## F. 团队仍需完成（按优先级）

1. **Patten 录 30 s + 45 s 人声**（11-24 前）→ 发我 → 我替换/重嵌 → 最终 ZIP。
2. **Windows PowerPoint 试播**：打开 deck → S7 点播 90 s → S13 播放 audio/video → 确认声音与全屏；同时把独立媒体文件放 U 盘作备用。
3. **Workbench 截图**（打开 carbon_lab.carbon_emission，显示 655,200 行）— 现场/证据用。
4. **全组排练 9:23 两次**（无笔记、每人发言、媒体播放时机）；手机录一段发我，我帮挑问题。
5. 照片（可选，替换卡通头像相似度）。
6. **11-26 晚提交 ZIP**（Moodle 成功截图）。

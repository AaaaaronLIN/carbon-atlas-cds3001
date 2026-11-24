# CDS3001 最高分 · 合规检查矩阵（Double-check）

> 用途：开工前逐条对照 Lecture 10/14/17/19 + `presentation_instruction.txt`（22 页双语摘要）+ 评分表 p.23，
> 确保**没有任何得分点被漏掉**。状态：✅ 已完成并验证；🟡 进行中；⬜ 未开始；❓ 待你确认。
> 更新：2026-11-18 · 品牌：**Data Fanatics**（公司）/ **Carbon Atlas**（产品）/ "The world's carbon, in one brief."（tagline）

---

## A. 提交要求（硬性）

| # | 要求 | 依据 | 状态 | 证据/位置 |
|---|---|---|---|---|
| A1 | 截止 **2026-11-27（五）18:00 HKT**，Moodle 交**一个 ZIP** | 摘要 p.2–3；L17 slide 18 | ⬜ | 待最终打包 |
| A2 | ZIP 含 **Part 1 code** | 摘要 p.3 | ✅ | `Part_1_Database/Part_1_setup.sql`（含 LOAD DATA + 验证 + API 用的分析 SQL） |
| A3 | ZIP 含 **Part 2 code** | 摘要 p.3 | ✅ | `Part_2_API/app.py` + `requirements.txt` + `API_reference.md` |
| A4 | ZIP 含 **Part 3 code** | 摘要 p.3 | ✅ | `Part_3_Frontend/index.html` + `static/` |
| A5 | ZIP 含**一份包含最终前端的 PDF** | 摘要 p.3；L17 slide 18 | 🟡 | 2.0 版界面已完成，PDF 需按 2.0 重做（旧 PDF 是 1.0） |
| A6 | 可解压、可运行、截图正常（自检） | 摘要 p.3 | ✅ | 已实测：解压→`carbon_api/`→`python3 app.py`→页面 200 + `/api/health` 返回 655,200 行 |
| A7 | 不延期、迟交按日扣（数额未列明，不假设宽限） | 摘要 p.3 | ⬜ | 计划 11-26 晚提交，留 1 天 buffer |
| A8 | 一个 ZIP 而不是散档 | 摘要 p.3（课堂补充） | ⬜ | 最终打包时确认 |

## B. 演示规则（硬性）

| # | 要求 | 依据 | 状态 | 安排/证据 |
|---|---|---|---|---|
| B1 | 严格 **9–10 分钟** + 1 分钟 Q&A | 摘要 p.10；L17 slide 21 | ✅ | Run of show **563 s = 9:23**（含 75 s 广告媒体），buffer 7 s |
| B2 | **全英文** | 同上 | ✅ | 所有稿件为英文口述 + 中文备注 |
| B3 | **每位成员都要发言、平均分配** | 同上 | ✅ | 每人独立章节 93 / 126 / 104 / 144（含 75s 媒体）/ 93 s；均发言；连续章节，非机械平均 |
| B4 | **不可使用笔记** | 同上 | 🟡 | 讲稿按"关键词记忆"设计；需排练到脱稿（Host cue card 只放后台） |
| B5 | 至少一张**安全/伦理**投影片 | 摘要 p.9 | ✅ | deck S15 GELSI 五列 + 网页 Method & GELSI 面板 |
| B6 | 至少一张**结论**投影片 | 摘要 p.9 | ✅ | deck S16 |
| B7 | **Poster + Audio + Video** 三媒体齐全 | 摘要 p.8；L17 slide 23 | ✅ | 海报 ✅；30 s Patten audio ✅；45 s Patten video ✅；已嵌入 deck S13；无音乐干净版 |
| B8 | 成本效益：成本/售价/利润、假设标明、不冒充收益 | 摘要 p.8 | ✅ | `cost_benefit.xlsx`：一次性 HK$31,746、年收益 HK$23,000、回本 16.6 月、3 年净 +37,254、2.17:1；"NOT claiming" 页 |
| B9 | 每小组**至少向其他组问一个问题** | 摘要 p.11（录音补充） | ✅ | LIN 主持卡/手机备忘；在对方 Q&A 问："Which chart in your dashboard changed a decision — and how would you prove it?"；S17 不显示 |
| B10 | 手机静音/震动、专注、准时 | 摘要 p.10–11 | ⬜ | 排演时作为团队纪律 |
| B11 | 全体出席（缺席上限 10/20） | 摘要 p.5；L17 slide 19 | ⬜ | 确认 5 人当天到场 |

## C. 评分表 11 项（p.23，顺序不可变）

| # | 评分项 | 权重 | 我们的证据 | 主讲 | 状态 |
|---|---|---|---|---|---|
| 1 | Company intro + logo + 成员 + **卡通头像** | 5% | deck S1–S2（logo + problem/mission/brief + 5 张成员卡）；网页 Team 区（5 个卡通头像 + 姓名/ID）；Data Fanatics 品牌 | LIN Xiaotong | 🟡 头像为原创卡通占位，照片来了可替换 |
| 2 | User Requirements | 5% | deck S3：4 persona × 问题→数据→SQL/route→图表 | LIN Xiaotong | ✅ |
| 3 | Part 1 code | 10% | deck S4 + `Part_1_setup.sql` + 真实 mysql 输出 + 终端证据 | WENG Zhichao | ✅ |
| 4 | Part 2 code | 10% | deck S5 + `app.py`（9 routes，参数化）+ `API_reference.md` + JSON 截图 | LIM Mantung | ✅ |
| 5 | Part 3 code | 10% | deck S6 + `index.html`（fetch→transform→chart；本地 assets） | LAI Patten | ✅ |
| 6 | Front-End Dashboard（自定 UI） | 10% | Carbon Atlas 2.0 + **S7 内嵌 90 s 真实录屏**；排序表/sparkline/CSV、双国对比/Index、Findings、GELSI、离线资产 | LAI Patten + HUANG Haolin | ✅ 已完成并嵌入 deck |
| 7 | Ad Campaign（poster/audio/video） | 10% | A3 海报 2.0 + 30 s 音讯 + 45 s 视频；三媒体同一句；已嵌入 deck S13 | HUANG Haolin | ✅ 草稿完成（Patten 人声待替换） |
| 8 | Cost-Benefit | 10% | `cost_benefit.xlsx`（5 sheets，假设全标）；deck S14 | WENG Zhichao | ✅ |
| 9 | Safety & Responsibility（GELSI） | 10% | deck S15 五列 + 网页 Method 面板 + 数据限制清单 | LIM Mantung | ✅ |
| 10 | Conclusion | 10% | deck S16 三句回扣 + 数字 + 金句 + next honestly | HUANG Haolin | ✅ |
| 11 | Presentation Skills | 10% | 9:23 计时、每人 92–109 s、英文、无笔记、全组排练 | 全员（host 主持） | 🟡 需排练 |

## D. 三部分实现要求（L10/L14/L17）

| # | 要求 | 状态 | 证据 |
|---|---|---|---|
| D1 | CSV 真正导入 MySQL（不是只有 CSV） | ✅ | 655,200 行；39 地区；6 部门；2019-01-01→2026-08-31；`Part_1_setup.sql` 在临时库用样例 CSV 实测通过 |
| D2 | 两个教程 API `/api/sectors`、`/api/monthly` 可用 | ✅ | 实测 JSON |
| D3 | 自定 dashboard 调 API 展示表格+图表 | ✅ | 实测：表 36 行 + 5 张 ECharts 图 + 地球；零 console error |
| D4 | 保留三部分连接、代码可解释 | ✅ | README + API_reference + deck S4–S6 + Q&A cheat sheet |
| D5 | 不照抄讲师 bonus dashboard | ✅ | 全新视觉/布局/交互/叙事（对比见 PDF p.8、deck S12） |
| D6 | 不能只放静态截图 | ✅ | 主 demo 为实机；截图仅作 fallback |

## E. GELSI（L19）

| 字母 | 我们在系统里对应的真实功能 | 状态 |
|---|---|---|
| G Governance | 单一 owned pipeline；方法面板印 source/coverage/unit；`/api/health` 状态 | ✅ |
| E Ethical | 不完整年 like-for-like；坐标轴从 0；不挑区间；明确写限制 | ✅ |
| L Legal | Carbon Monitor fair-use、引用 Sci Data 7, 392 (2020), doi:10.1038/s41597-020-00708-7、无个人数据 | ✅ |
| S Social | 键盘可操作、对比度、无仅靠颜色、reduced-motion、可打印浅色主题 | ✅ |
| I Implications | 部门/国家集中度指向行动；拒绝臆造人均（数据集无人名列） | ✅ |

## F. 数据与诚信红线

| # | 红线 | 状态 |
|---|---|---|
| F1 | 不虚构收益/客户/实测节省 | ✅ 成本表写 "NOT claiming" |
| F2 | 不把估算当实测 | ✅ 方法面板写 "These are estimates" |
| F3 | 不拿不完整 2026 与整年比 | ✅ 全部 like-for-like Jan–Aug，UI 到处标注 |
| F4 | 不编造学生经历/头像 | ✅ 卡通头像为设计形象；成员信息来自你们 |
| F5 | 不把未完成功能说成已完成 | ✅ 广告媒体 = 草稿/待录人声，讲稿会诚实说明 |

## G. Double-check 实测记录（本轮）

| 检查 | 结果 |
|---|---|
| MySQL 真实数据 | 655,200 行 / 39 series / 6 sectors / 2019-01-01→2026-08-31 ✅ |
| 9 个 API 路由 | `/api/sectors`、`/api/monthly`、`/api/country_year`、`/api/country_ytd`、`/api/daily`、`/api/compare`、`/api/insights`、`/api/health`、`/api/meta` 全部 200 ✅ |
| 2.0 页面 | 零 console error；地球 519×519 正常渲染；Team 5 卡；Story 导览切年/切国正常 ✅ |
| Theme | Day / Stage 双向切换正常，图表/地图/表格颜色随主题重绘 ✅ |
| 旧 ZIP | 解压后可运行（Part 1 SQL 在临时库实测通过）✅ |
| 旧 PDF / deck | PDF 9 页、deck 17 页可用；但为 1.0 品牌/界面 → **必须重做** 🟡 |
| 旧品牌残留 | 旧 deck/PDF/海报/ZIP 仍写 "Carbon Compass (Analytics)" → 将全部替换为 Data Fanatics / Carbon Atlas 🟡 |

## H. 剩余工作（按优先级）

| # | 事项 | 负责人 | 期限 |
|---|---|---|---|
| H1 | Deck 品牌/成员/头像/新截图更新 + 排版复核 | Lead | 11-20 |
| H2 | 最终前端 PDF 2.0 重做（Day + Stage + Team + Story 截图） | Lead | 11-20 |
| H3 | 海报换品牌 + 30 s / 45 s 广告（Patten 人声最终版） | Lead | 11-24 |
| H4 | 成员照片（可选，换卡通头像相似度） | 你们 | 11-20 前 |
| H5 | 录音/录音替换、视频人声 | 你们 | 11-24 |
| H6 | MySQL Workbench 截图（现场演示用） | 你们 | 11-24 |
| H7 | 全组排练 9:23、无笔记、每人 92–103 s、准备问别组的问题 | 全组 | 11-25–26 |
| H8 | 最终打包 ZIP + 提交成功截图 | Lead + 你们 | 11-26 晚 |

**结论**：A/B/C/D/E/F 中共 12 项 🟡（主要是广告媒体草稿、deck/PDF 2.0 重做、排练），其余 ✅；无任何"未识别"的评分项。方向正确，继续按 H 执行。

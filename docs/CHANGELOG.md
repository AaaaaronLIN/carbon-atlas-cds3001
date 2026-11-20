# Changelog

## 2026-11-20 · v5.1（当前）
- **互动减为 1 个**：0:06 天气 vs 碳排放（host）；删除 0:50 的 2019 vs 2025 提问，LIN 不再背这段
- **S1 副标题**：`A decision brief on global CO₂ — as easy to check as the weather.`（tagline / campaign line / 三媒体不动）
- LIN 只负责：破冰 + 产品引入 + 用户需求 + 4 个交接 + Q&A 主持
- 9 页 run sheet / 每人 packs / 讲稿 00·01·07·08 同步；Deck PDF / ZIP 重出

## 2026-11-20 · v5.0
- **流程简化**：8 个步骤按顺序走；互动从 3 个减到 **2 个，全部由 LIN 带**；3:37 改为 6 秒产品 bridge（不是互动）
- **英文稿重写**：短句、口语化；每页顶部明确写“这一段主要讲什么（中文）”；英文正文不再混中文/cue
- **新主文件**：`Carbon_Atlas_Run_Sheet_and_Scripts.pdf`（9 页）
  - p1 8 步流程 + 2 互动 + 规则；p2 LIN 稿；p3 LIN 互动/交接/Q&A；p4 WENG；p5 LIM；p6 LAI；p7–8 HUANG；p9 Q&A/检查/评分
- **每人 packs**：`Team_Script_Packs.zip`
- 旧版 10 页 handout / 纯英文稿 / Team_Member_Packs 已退役
- Q&A：向其他组提问移到对方 Q&A；deck S17 / 讲稿 / ZIP 同步

## 2026-11-20 · v4.4
- **Q&A 提问时机修正**：S17 的“向其他组提问”不在我们自己的 1 分钟 Q&A 问；改到下一组/其他组 Q&A 举手问（课程硬性要求，否则扣分）
- S17 标题改 “OUR QUESTION FOR ANOTHER GROUP”；host T4 改 “Thank you. We're happy to take questions.”
- **新增纯英文逐字稿** `English_Verbatim_Scripts.pdf`（7 页）：正文只有英文，顶部保留中文任务；每页一人
- **新增每人整合包** `Team_Member_Packs.zip`：英文稿 + 中文指导 + Q&A
- 讲稿 00/01/06/08 同步更新；Deck PDF/ZIP 已重出

## 2026-11-20 · v4.3
- S10 KPI 数字回到左对齐（headline KPI 风格；表格/排名仍右对齐，按位比较）
- 全 deck 17 页重渲染检查：黄色 takeaway 行 8 处位置一致、单行不溢出、不与 footer 重叠；无 shape 超出页面边界
- Deck PDF / contact sheet / ZIP 已重出

## 2026-11-20 · v4.2
- 明确 **S7 fallback 录屏没有声音**：不在视频里加 AI 旁白；live 失败时 LAI/HUANG 继续现场讲
- S8–S11 截图 fallback 同样无声音，由讲者继续讲
- S13 的 45 s 视频广告 + 30 s 音频广告有声音；最终由 Patten 真人声替换 TTS
- 讲稿 / live playbook / operator card 已补上“录屏无声，继续讲”提示

## 2026-11-20 · v4.1
- 引用改成 **source paper arXiv:2004.13614**（deck 封面/S17、海报、最终 PDF、网站）
- 海报底部 source line 之前被版面裁掉：已收紧 hero/stats/answers/pipeline/footer 间距，source 现在完整可见
- 全部 deck/PDF/海报/ZIP 重新同步

## 2026-11-20 · v4.0
- 引用写法统一：`arXiv:2004.13614` → **`source paper arXiv:2004.13614`**（deck 封面 / S17 / 海报 / 最终 PDF / 網站 Method/footer）
- 说明：arXiv ID `2004.13614` = 2020 年 4 月提交的 Carbon Monitor 论文编号，不是 2004 年或数据年份
- 论文标题：COVID-19 causes record decline in global CO2 emissions（Liu et al., 2020）
- 所有 deck/PDF/海报/ZIP 已同步

## 2026-11-20 · v3.9
- 删除所有 slide kicker 里的 rubric 权重 `(10%)`（S4/S5/S6/S7/S13/S14/S15）——评分标准不应出现在观众页面
- S12 表头 `REFERENCE (MOODLE BONUS)` → `REFERENCE DASHBOARD`，正文改 "supplied dashboard"
- S10 三个 KPI 数字改为右对齐（与标签列分开），解决数字长度不同造成的视觉错位
- audit_deck.py 新增 rubric 权重 / Moodle 字样扫描；当前 PASS
- Deck PDF / contact sheet / ZIP 已重出

## 2026-11-20 · v3.8
- **audience-copy cleanup**：删除 slides 上所有 `SAY` / `Screenshot:` / `fallback` / `no notes` / storyboard 等内部用语（S4–S11、S14、S15）
- 清空全部 speaker notes（旧 1.0 Member A–E 笔记 + 临时 team notes），避免 presenter view 出现内部文字
- 最终 PDF 封面 "Screenshots..." → "Captured from..."; PDF 10 页扫描无内部用语
- 新增 `tools/audit_deck.py`：自动扫描 forbidden terms / notes / media count；当前 PASS
- S13 音频只留 transcript；S14 数字列右对齐、说明句首大写；S2 删除 delivery rules

## 2026-11-20 · v3.7
- S2 删除 "no notes / even speaking time" 等内部规则，改成 "Built end to end: database → API → interface → story."
- S13 删除 audio 分镜三行（0:00/0:12/0:25），改为音频 transcript + "Voice-over + music" 说明，避免评委误读
- S14 数字列右对齐、KPI 说明改句首大写；全 deck 数据说明统一句首大写
- 视频全屏：在 PowerPoint 里通过 Playback → Play Full Screen 设置（步骤进 playbook；非版面属性，Mac 上无法直接写）
- Deck PDF / contact sheet / ZIP 已重出

## 2026-11-20 · v3.6
- **最终决定：S7 优先现场 live**（Mac Flask+MySQL → 教室浏览器 tunnel/LAN），S7 内嵌 90 秒录屏为 5 秒 fallback
- 9 份讲稿全部改为 live cue：`00` run-of-show / `01` host / `02` WENG / `03` LIM / `04` LAI / `05` HUANG / `06` Q&A / `07` fallback / `08` cue card
- S7 caption 已同步；live 失败流程写入 `07` 和 `LIVE_DEMO_PLAYBOOK.zh.md`

## 2026-11-20 · v3.5
- 用 5 位成员的真实头像作 likeness 参考，重画 **原创卡通头像**（仍符合 rubric 的 "Cartoon profile picture"）：
  LIN 黑发侧分/深色西装、WENG 乱发+圆眼镜+花衬衫、LIM 短发+西装领带、HUANG 卷发+方框眼镜、Patten 刘海+方框眼镜+绿色 hoodie
- 网站 Team 区、Deck S2、PDF Team 页全部同步；LAI 角色更新为 **FRONT END & LIVE DEMO**
- 原始真人照片只保存在本地 `presentation/team_photos/`，**不进 public repo**（隐私）

## 2026-11-20 · v3.4
- 新增现场 live 网站演示套件：`presentation/LIVE_DEMO_PLAYBOOK.zh.md`、`LIVE_DEMO_OPERATOR_CARD.md`、`tools/start_live_demo.sh`、`start_tunnel.sh`、`live_demo_check.py`
- `app.py` 支持 `HOST=0.0.0.0` / `PORT` / `FLASK_DEBUG`，方便教室局域网访问；本地默认仍是 127.0.0.1
- S7 caption 改为 live + embedded fallback 两种模式
- 实测：Mac LAN `10.9.64.72:5001` 与 Cloudflare quick tunnel 均返回 200

## 2026-11-20 · v3.3
- 修复最终前端 PDF 封面：`Carbon Compass` → **Carbon Atlas**，旧 compass 图标 → 新 orbit mark；PDF 10 页全部检查无旧品牌残留
- 封面把第三栏明确标成 **THE SOLUTION**，正好对应 rubric 的 problem / mission / solution

## 2026-11-20 · v3.2
- Deck 重新设计为 **Stage 深色 premium 版**：深墨绿 + 象牙白 + 薄荷绿/金，全 17 页统一；S8–S11 截图换成真实 Stage 界面；S13 海报/媒体保持深色一致
- 新增 `deliverable/README.md`：说明 GitHub 不能预览 `.pptx`，先看 deck PDF；更新 README 的看 PPT 指引

## 2026-11-20 · v3.1
- 重新设计 A3 海报：与网站默认 **Stage 深色主题**一致（深墨绿 + 象牙白 + 薄荷绿），加入真实 Stage 介面截图、数据管线、四问结构；修正 2,800 天数字
- 海报/deck/ZIP 同步更新

## 2026-11-19 · v3.0
- 新增：90 秒真实 MySQL build 录屏（Stage 主题）、45 秒视频广告、30 秒音频广告、媒体嵌入 deck S7/S13
- 新增：最终前端 PDF 10 页（Stage + Day + Team + Story + GELSI + partial-year + 复现）
- 新增：9:23 PPT-only 讲稿包（run-of-show / 5 人逐字稿 / Q&A / cue card / interaction）
- 修复：Stage 下 inline code 白底白字；锚点标题被 header 挡住；HUD "LIVE · 2025" 歧义；选择国家地球自动聚焦；S13 campaign line 单位统一
- 打包：最终 ZIP（56 files, 41 MB）

## 2026-11-18 · v2.0
- 品牌：Carbon Compass → **Carbon Atlas**，公司 **Data Fanatics**；新 tagline
- 网页：旋转地球 hero、Stage/Day 主题、Play the brief 导览、Team 区、5 个真实成员卡通头像、运动渐变（地球颜色/KPI/图表/表格/主题）
- Deck：真实成员、新截图、新海报、GELSI/成本/广告页更新；PDF 2.0

## 2026-11-18 · v1.0
- 初版 Carbon Compass：浅色 analytics brief、排序表/sparkline/CSV、双国对比 + Index、Findings、Method & GELSI、离线 assets
- 完成 Part 1/2/3 代码与首个 ZIP

# Changelog

## 2026-11-20 · v3.9（当前）
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

# Changelog

## 2026-11-20 · v3.4（当前）
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

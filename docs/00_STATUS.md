# 项目状态 · 2026-11-19

## 当前阶段：可实现部分全部完成，等 5 个团队动作

| 模块 | 状态 | 位置 |
|---|---|---|
| Part 1 MySQL（655,200 行 / 39 series / 6 sectors） | ✅ 完成并实测 | `code/Part_1_setup.sql` + `docs/Part1_verification_output.txt` |
| Part 2 Flask API（9 条 JSON 路由） | ✅ 完成并实测 | `code/app.py` + `code/API_reference.md` |
| Part 3 网页（Carbon Atlas 2.0） | ✅ 完成，Stage 默认 | `code/index.html` + `code/static/` |
| 最终前端 PDF（必交） | ✅ 10 页 | `deliverable/Carbon_Atlas_Final_Frontend.pdf` |
| 17 页 PPT（含内嵌媒体） | ✅ 13.6 MB，S7 demo、S13 audio+video | `deliverable/Carbon_Atlas_Deck.pptx` |
| 90 秒 demo 录屏 | ✅ 真实 MySQL build、Stage 主题 | `deliverable/carbon_atlas_demo_90s.mp4` |
| 45 秒视频广告 | ✅（TTS 草稿人声） | `deliverable/carbon_atlas_ad_45s.mp4` |
| 30 秒音频广告 | ✅（TTS 草稿人声） | `deliverable/audio_ad_30s_draft.mp3` |
| A3 海报 | ✅ | `deliverable/poster.png` / `.pdf` |
| 9:23 讲稿包 | ✅ 9 份 | `presentation/scripts/` |
| 成本效益 / GELSI | ✅ | `presentation/cost_benefit.xlsx` + deck S14/S15 |
| 最终 Moodle ZIP | 🟡 等 Patten 人声后做最终重打包 | 由 Lead 生成 |

## 本轮（2026-11-18 ~ 19）已修复的细节
- 深色主题下 inline code 白底白字 → 改成深绿底象牙字；
- 锚点跳转标题被 sticky header 挡住 → `scroll-margin-top: 78px`；
- 地球 HUD "LIVE · 2025" 歧义 → 改为 `2025 · FULL YEAR` / `2026 · Jan–Aug`，API live 只在右上状态条；
- 选择国家时地球自动平滑旋转到该国并高亮；
- S13 campaign line 统一为 `million tonnes`；
- 广告分镜/脚本旧品牌清理。

## 关键数据（口播/物料统一）
- 655,200 行；39 series；6 sectors；2019-01-01 → 2026-08-31；MtCO₂/day
- 世界年度：2019 36,397 · 2020 34,583 (−5.0%) · 2021 36,401 · 2022 36,908 · 2023 37,386 · 2024 37,648 · 2025 **37,856** (+4.0%)；2026 Jan–Aug **25,014** (+3.9% vs 2019 同期)
- 2025 部门：Power 35.6% · Industry 33.5% · Ground Transport 18.2% · Residential 9.0% · Int'l Aviation 2.7% · Domestic Aviation 1.1%
- 2025 国家：China 12,089 (31.9%) · US 5,036 (13.3%) · India 3,309 (8.7%) · Russia 1,670 (4.4%) · Japan 978 (2.6%)；前五 = 61.0%
- 2025 最大涨幅/跌幅（>100 Mt）：Netherlands +5.3% · France −6.0%

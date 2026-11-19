# CDS3001 小组项目：交付要求与提交指南

**Part 1 / Part 2 / Part 3 + Final Presentation · 截止 2026-11-27（周五）18:00 香港时间**

> 课程：CDS3001 Databases and Data Warehouses（岭南大学）
> 适用：Data Fanatics 小组 / 项目品牌 Carbon Compass Analytics
> 依据：L10（Part 1）、L14（Part 2）、L17（Part 3 与 Final Presentation）、L19（Data Ethics / GELSI）讲义，以及 Lecture 17 双语摘要（`presentation_instruction.txt`，22 页）
> 引用约定：`摘要 p.x/22` = 上述双语摘要的 PDF 页码；`Lxx slide n` = 对应讲义幻灯片页
> 整理日期：2026-11-18。讲义未写明的事项一律标 **[待确认]**，我们的做法标 **[建议]**，不把建议写成规定

**本文结构**

- a. 项目是什么（数据流与三部分考核重点）
- b. 评分与算分（20 分、11 项 100%、公式与两个例子）
- c. 必须提交什么（ZIP 结构、最终前端 PDF、命名、截止）
- d. 现状盘点（已有什么、哪里有问题、数据事实复核）
- e. 还需要做什么（P0 / P1 / P2 表格与分工）
- f. 演示怎么排（9 分 30 秒、谁讲哪段、无笔记、扣分点）
- g. 数据与伦理（GELSI 一页纸、引用、红线）
- h. 提交前 checklist
- 附录 A 待确认清单 / 附录 B 出处索引

---

## 0. 一页速览

- **截止**：2026-11-27（周五）18:00 香港本地时间；在 Moodle 只交 **一个 ZIP**；不延期，迟交按日扣分（**每日扣多少，讲义与录音都未列明**）——摘要 p.2–3/22；L17 slide 18。
- **ZIP 里四样**：Part 1 code、Part 2 code、Part 3 code、**一份包含最终前端的 PDF**（摘要 p.3/22；L17 slide 18）。PDF 的页数与章节结构讲义**没有规定**（摘要 p.3/22 明确说明），所以「截图 + 简短说明」是**[建议]**而不是硬性格式。
- **20 分怎么来**：Part 1 10 + Part 2 5 + Part 3 5 = 20；最终项目分 =（三部分得分之和）×（演示分 ÷ 100），满分 20（摘要 p.4–5/22；L17 slide 24–25）。
- **演示**：11 项 rubric 共 100%，严格 9–10 分钟 + 1 分钟 Q&A；全英文、每位成员都要发言、**不可用笔记**（摘要 p.6–11/22；L17 slide 21–23）。
- **当前 5 个最大缺口**（详见 §d.3）：Part 1 导入证据链断、最终前端 PDF 不存在、旧前端是讲师 Bonus dashboard 的换皮版（新版 Carbon Compass 已生成，待验收）、演示材料（广告 / 成本效益 / GELSI / 结论）为零、数据库截图证据与密码卫生缺失。

---

## a. 项目是什么

### a.1 一句话

把 Carbon Monitor 的全球日度 CO₂ 排放 CSV 导入 MySQL，用一个小型 Flask 服务把 SQL 查询结果以 JSON API 提供出来，再用一个**自定的前端 dashboard** 把数据变成非技术用户能读懂的图表；最后用 9–10 分钟全英文、无笔记的演示把「数据 → 查询 → 图表 → 用户价值」讲成一个完整方案（摘要 p.1–2/22；L10 slide 3；L17 slide 3–4）。

### a.2 数据流（四步，演示就按这条线讲）

| 步骤 | 做什么 | 产物 | 可展示的证据 | 依据 |
|---|---|---|---|---|
| 1 数据源 | 从 carbonmonitor.org 下载 CSV | 约 34.5 MB、65 万行级 CSV | 下载页/文件、行数与日期范围 | L10 slide 6–8 |
| 2 MySQL | 建 `carbon_lab` 库与 `carbon_emission` 表，`LOAD DATA` 导入 | 数据库表 | `LOAD DATA` 成功输出、`COUNT(*)`、Workbench 截图 | L10 slide 9–17 |
| 3 API | Flask + pymysql 执行 SQL，`jsonify` 返回 JSON | 可访问的 URL | 浏览器打开 `/api/sectors` 等看到 JSON | L14 slide 4、13–18；L17 slide 7 |
| 4 前端 | HTML 调 API，用图表库画图并做交互 | 可操作的 dashboard | 现场演示 + 截图 + PDF | L17 slide 4–10；摘要 p.14–17/22 |

### a.3 三部分各考什么

| 部分 | 分值 | 要做什么 | 讲台上要能证明什么（拿分点） | 依据 |
|---|---|---|---|---|
| Part 1 | 10 | 下载 CSV；建库建表；`LOAD DATA` 导入；在 MySQL Workbench 检查 | **数据确实在 MySQL 里**，不是躺着的 CSV；能解释每一条导入/检查 SQL | 摘要 p.1–2/22；L10 slide 4、17 |
| Part 2 | 5 | 小型服务器连接 MySQL、执行 SQL、以 JSON 返回；浏览器测试 | 一个**能返回数据的 URL**；能讲清数据库连接、查询、`jsonify` 三步 | 摘要 p.2/22；L14 slide 4、20 |
| Part 3 | 5 | 建 HTML 页面、调用 Part 2 API、用表格/图表展示 | 页面真的在调 API、数据真的来自数据库；能解释取数、转换、绘图 | 摘要 p.2/22；L17 slide 8–11 |

**关键要求**：保留三部分的连接与**可解释的代码**，不能只准备最后一页的外观；不要只放静态截图而不说明数据来自哪个 API / 数据库（摘要 p.2/22）。这也是为什么 §d.3 把「前端可解释性」列为高风险。

### a.4 一个容易被忽略的措辞差异

L14 / L17 的第 2 页写「Part 3: Show the data on a web page **& presentation** (5%)」，而 L17 slide 24–25 的算分公式把 presentation 单独按 100 分计、再相乘。**以公式为准**：presentation 不是 5 分，而是一个 0–100 的乘数（摘要 p.5/22 专门提醒不要算错）。此处如需绝对确认，可向讲师提问 **[待确认]**。

---

## b. 评分与算分

### b.1 实现分（20 分）

| 组成 | 满分 | 说明 |
|---|---|---|
| Part 1 — Import data into MySQL | 10 | 项目里权重最大、也最容易拿满的一项 |
| Part 2 — Write a simple API | 5 | 两个基础端点即可满足最低要求，多做才有区分度 |
| Part 3 — Show data on a web page | 5 | 页面 + 图表 + 自定界面 |
| **合计** | **20** | 这是**整科成绩中的 20 个百分点**，不是演示评分的权重 |

### b.2 最终公式与讲义的两个例子

**最终项目分（满分 20）=（Part 1 得分 + Part 2 得分 + Part 3 得分）×（演示分 ÷ 100）**

| 讲义例子 | 计算 | 正确解读 | 依据 |
|---|---|---|---|
| Part 1 = 8/10；Part 2 = 5/5；Part 3 = 3/5；演示 = 80/100 | (8 + 5 + 3) × 0.8 = **12.8/20** | 得分率 64%，对整科贡献 12.8 个百分点 | L17 slide 24；摘要 p.4–5/22 |
| Part 1 = 10/10；Part 2 = 5/5；Part 3 = 5/5；演示 = 90/100 | (10 + 5 + 5) × 0.9 = **18/20** | 得分率 90%，对整科贡献 18 个百分点 | L17 slide 25；摘要 p.5/22 |

**不要这样算**：不要把演示的 100 分直接加到 20 分上；也不要再额外加一个「演示占整科 10%」——rubric 里的 Presentation Skills 10% 是演示分内部的一项（摘要 p.5/22 明确提醒）。

### b.3 演示评分表（11 项，共 100%）

顺序即演示顺序，必须按顺序覆盖（摘要 p.6–9/22；L17 slide 22–23）。

| # | 评分项（英文原名） | 权重 | 必须呈现 | 拿分要点 / 本项目落点 |
|---|---|---|---|---|
| 1 | Company Intro & logo + member Intro & Cartoon profile picture | 5% | 公司介绍与 logo、成员介绍与卡通头像；问题、使命、方案 | 开场 30 秒讲清「帮谁解决什么问题」；logo、头像一个都不能漏；不要虚构经历 |
| 2 | User Requirements | 5% | 解决方案需要哪些资料 | 把用户需求连到数据字段、查询和 dashboard；不要只报技术名 |
| 3 | Part 1 | 10% | Part 1 Code | 解释导入与检查的关键 SQL 和结果，而不是无法解释的截图 |
| 4 | Part 2 | 10% | Part 2 Code | 讲清 SQL 怎样经 API 变成 JSON，并当场展示返回结果 |
| 5 | Part 3 | 10% | Part 3 Code | 解释网页怎样调用 API、转换数据、创建图表；画面不能替代代码说明 |
| 6 | Front-End Dashboard | 10% | 自定的用户界面 | 展示对用户有意义的可视化与交互；只保留讲义里的基础两图不足以争高分（摘要 p.16/22、录音 22:14–24:26） |
| 7 | Ad Campaign | 10% | Poster、Audio、Video 广告 | 三者齐备、信息一致；**不要漏音频广告**；先放海报再放视频（摘要 p.9/22） |
| 8 | Cost-Benefit Analysis | 10% | 方案的成本与效益 | 成本、售价、利润都要谈；估算必须标假设、前后数字一致；不冒充已实现收益 |
| 9 | Safety & Responsibility | 10% | 系统的安全与伦理考虑 | 讲与本系统相关的具体风险、影响与应对；不要只有一个标题或口号 |
| 10 | Conclusion | 10% | 总结与有力收结 | 回扣需求、已展示成果与方案价值；不要把未完成说成已完成 |
| 11 | Presentation Skills | 10% | 表达、时间、团队合作 | 英语、全员发言、无笔记、整组排练；避免一人包办或超时 |

**合计 100%；其中三个 code 部分 + dashboard 合计 40%**（摘要 p.9/22）。公司介绍与用户需求合计 10%，权重不高但最容易拿满，不要因为「赶技术」而跳过。

### b.4 算分敏感度（自己算一遍就明白该先做什么）

| 实现分（P1+P2+P3） | 演示 70 | 演示 80 | 演示 90 | 演示 100 |
|---|---|---|---|---|
| 14/20 | 9.8 | 11.2 | 12.6 | 14.0 |
| 16/20 | 11.2 | 12.8 | 14.4 | 16.0 |
| 18/20 | 12.6 | 14.4 | 16.2 | 18.0 |
| 20/20 | 14.0 | 16.0 | 18.0 | 20.0 |

**结论**：在实现分已接近满分的区间，**每 1 个演示分 = 最终 0.2 分**；rubric 里每个 10% 的评分项，在实现满分时最多值 **2 个最终分**。所以「实现分拿满」只是及格线，演示的 11 项一项都不能空着上。

### b.5 缺席上限（硬规则）

出席与参与 Final Presentation 是强制的。缺席的学生，其小组项目最多拿 **10/20**（= 项目满分的一半），而且这是上限、不是保底分（L17 slide 19；摘要 p.5/22）。**每位成员都必须到场并参与。**

---

## c. 必须提交什么

### c.1 硬性要求

| 要求 | 内容 | 依据 |
|---|---|---|
| 截止时间 | 2026-11-27（周五）18:00 香港本地时间 | 摘要 p.3/22；L10 slide 4；L17 slide 18 |
| 提交形式 | Moodle 上**只收一个 ZIP**；把相关文件整合，不要散着传 | 摘要 p.3/22；L17 slide 18 |
| ZIP 内容 | Part 1 code、Part 2 code、Part 3 code、一份包含**最终前端**的 PDF | 摘要 p.3/22；L17 slide 18 |
| 延期 | 不延期；迟交按日扣分（**每日扣多少未列明**，录音补充） | 摘要 p.3/22、p.20/22 |
| 验交 | 自己解压 ZIP、确认文件可读、PDF 正常、Moodle 显示提交成功（[建议]） | 摘要 p.3/22、p.21/22 |

**日期提醒**：演示在 11 月 27 日的最后一堂课进行，**各组的出场时段要另行确认**；18:00 是**提交**截止，不是上台时间（摘要 p.10/22 课堂补充）。**[建议]** 最晚在 11 月 26 日晚上前完成上传——不要等上台之后再交。

### c.2 ZIP 结构（[建议]，与项目组约定一致）

```
CDS3001_DataFanatics_CarbonCompass_2026-11-27.zip
|-- Part_1_SQL/
|   |-- Part_1_setup.sql          # 建库、建表、LOAD DATA 一条龙（路径写成占位符）
|   |-- Part_1_verify.sql         # 4 条验证查询：行数/日期范围/地区数/前 10 行
|   `-- screenshots/              # LOAD DATA 成功、COUNT/MIN/MAX、Workbench 表、DESCRIBE
|-- Part_2_API/
|   |-- app.py                    # 不含真实密码
|   |-- requirements.txt          # flask / pymysql / cryptography（固定版本）
|   `-- API_reference.md          # 每个端点：URL、参数、返回示例、对应 SQL
|-- Part_3_Frontend/
|   |-- index.html
|   |-- static/                   # echarts.min.js、world.json（离线可用）
|   |-- README.md                 # 3 步跑起来：建库→装依赖→python3 app.py
|   `-- screenshots/              # dashboard 各屏截图
|-- PDF/
|   `-- Carbon_Compass_Final_Frontend.pdf
`-- Presentation/
    |-- Carbon_Compass_deck.pdf   # 如使用幻灯片
    |-- poster.png / poster.pdf
    |-- audio_ad.mp3
    |-- video_ad.mp4
    `-- cost_benefit.xlsx / .pdf
```

说明：讲义只要求「三部分 code + 最终前端 PDF」，上面细分目录是**[建议]**的整理方式；只要四类东西都在、可读、可对照，就是合规的。截图的文件命名建议带日期与版本，如 `2026-11-26_load_data_warnings0.png`，避免「week1_shot.png」这种无法追溯的名字。

### c.3 「最终前端 PDF」到底放什么

讲义只说 PDF 要包含最终前端，**没有规定页数或章节结构**（摘要 p.3/22 明确指出 L17 slide 18 没有这些规定）。**[建议]** 做一份 6–10 页、可离线打开、每屏可读的说明型 PDF：

| 页 | 内容 | 目的 |
|---|---|---|
| 1 | 封面：Carbon Compass Analytics + logo、组名、成员（与 Moodle 注册一致）、日期、课程 | 让评分人一眼知道是谁的项目 |
| 2 | 数据流图 + 一段话：CSV → MySQL → API → ECharts；标明数据版本与单位 | 证明三部分是连在一起的，不是三份作业 |
| 3–7 | 每个界面 1 页：整屏截图 + 2–4 句说明（这个界面回答什么问题、数据来自哪个 API、怎么读图） | 覆盖 Front-End Dashboard 10% 的证据 |
| 8 | API 清单与示例 JSON 截图（3–4 个端点） | 支撑 Part 2 的可信度 |
| 9 | 方法与限制：估算数据、覆盖缺口、完整年 vs 部分年、离线资源 | 给 Safety & Responsibility 加分 |
| 10 | 数据来源与引用（Carbon Monitor + 文献）、版本记录 | 给 Ethical / Legal 加分 |

视频型内容（广告）不要塞进这份 PDF——广告单独交在 Presentation 目录；PDF 只放「前端 + 必要说明」。

### c.4 命名与提交操作

- ZIP：`CDS3001_DataFanatics_CarbonCompass_2026-11-27.zip`（[建议]）。
- PDF：`Carbon_Compass_Final_Frontend.pdf`（与项目组约定一致；文件名不要带中文与空格）。
- 提交前 30 分钟：本地解压 ZIP → 打开 PDF → 打开 `index.html` 确认没有 `file:///` 依赖 → 截图 Moodle 提交成功页 → 保留 ZIP 一份在本地与云盘。
- ZIP 内若有 `.DS_Store`、`__pycache__`、`.venv`，先删掉再压缩；不要压缩 `.venv`。

---

## d. 现状盘点

> 盘点时间：2026-11-18 15:24（项目组负责人与前端正在并行更新 `project/app/`，以下为当时的快照）。旧版文件在旧工作目录 `carbon_api 2/`（本机 `~/Downloads/carbon_api 2/`）；新版 Carbon Compass 正在 `project/app/` 落地。**最终以交付目录的版本为准**。

### d.1 旧版已有资产（carbon_api 2）

| 资产 | 现状 | 问题 | 影响与处置 |
|---|---|---|---|
| Part 1 SQL 文件（34 行） | 建库、建表 + 2 条 SELECT（China）；文件名 `Part_1_setup.sql` | **缺 `SET GLOBAL local_infile=1`、缺 `LOAD DATA`、缺验证查询**；表结构 `VARCHAR(100)/FLOAT` 且可空，与讲义 `VARCHAR(50)/DOUBLE NOT NULL` 不一致；注释为中文 | Part 1 的核心证据（数据确实导入 MySQL）断链，**这是 10 分里最大的风险**；处置见 §e P0-1 |
| app.py（旧，81 行） | Flask + pymysql；5 个旧端点：sectors、monthly、country_year、country_sector、daily，另有 `/` | **明文密码 `password="******（已移除）"`**；SQL 用字符串拼接（`country` 未参数化）；无错误处理 | 可作「Part 2 教学版」讲解基线；**交付前必须清除真实密码**（§e P0-3） |
| `index.html`（旧，509 行，Carbon Pulse） | 深色 ECharts 仪表盘：世界地图点选、Top 10 + ▶ Play、sector donut、月度趋势缩放、每天一格日历 | 功能集合与讲师 Moodle **Bonus dashboard 高度重合**，属于「换皮」；ECharts、world.json、Google Fonts 全部走 CDN；代码不是本组所写 | 同时压低 **Part 3 code 10%**（讲不清自己没写的代码）与 **Front-End 10%**（讲义明确「原样不够」）；另有被质疑「未自定/照搬」的风险。处置：归档为「迭代前版本」，最终版用 Carbon Compass，并准备「改了什么」清单 |
| 两份旧 PDF | 基础两图版、旧 dashboard（仅过程截图） | **不是** L17 slide 18 要求的最终前端 PDF | 可作「迭代对比」素材（P2），不能当最终 PDF 交 |
| 本地数据 | `carbon_lab.carbon_emission` 已导入 | 见 §d.4 数据事实 | 可作为最终数据源；重导只需几秒（§e P0-1） |
| 缺 | — | 无最终 PDF、无演示 deck、无海报/音频/视频、无 GELSI 页、无结论页、无数据库截图、无 `README.md` / `requirements.txt` / `API_reference.md` | 对应 rubric 的 6 个评分项（合计 50%）目前没有证据 |

> 旧 PDF 文件名：`CDS_3001_group_project_chart.pdf`、`Carbon Pulse – Global CO2 Dashboard.pdf`（均在 `carbon_api 2/`）。

### d.2 新版 Carbon Compass 进度快照（project/app）

| 文件 | 状态 | 说明 |
|---|---|---|
| `app/app.py`（15:17 快照，517 行） | 已重写 | 9 个 `/api/*` 端点：`sectors`、`monthly`、`health`、`meta`、`country_year`、`country_sector`、`daily`、`compare`、`insights`；参数化查询、JSON 化错误处理；用「最近完整年份 + 年初至今同期」避免把 2026 部分年份加总成「暴跌」——**这一点很适合在演示里讲，是数据伦理的加分材料** |
| `app/static/echarts.min.js` + `world.json` | 已本地化 | 解决旧版 CDN 依赖，断网也能演示；这是对旧版的实质性改进，要写进「改动清单」 |
| `app/index.html` | 已生成（15:23，约 72 KB） | Carbon Compass 新界面，调用本地 `static/` 资源；**待验收、截图、写改动清单** |
| `README.md`、`requirements.txt`、`Part_1_setup.sql` | 待落地 | 计划路径为 `project/app/`；`project/out/pdf`、`out/presentation`、`out/screenshots` 目前为空（截图与 PDF 均未生成） |
| 密码处理 | 部分完成 | 新版改为环境变量读取，**但 fallback 默认值仍是真实密码**（15:24 复核：`app.py` 第 41 行），交付前必须改成占位符（`your_password`） |

### d.3 关键风险（★ = 最紧急）

**★ R1 — Part 1 证据链断**：`.sql` 没有 `LOAD DATA`、没有 `local_infile`、没有验证语句，表结构与讲义不一致，也没有任何截图证明 65 万行真的进了 MySQL。Part 1 权重 10 分，是三点里最大的一块，目前证据最弱。

**★ R2 — 缺「最终前端 PDF」**：这是 L17 slide 18 明列的四个必交件之一。没有它属于交付清单不完整；讲义未写具体扣分额，但**不能假设不会扣**。

**★ R3 — 前端原创性与可解释性**：旧 `index.html`（Carbon Pulse）是 Bonus dashboard 换皮。严格说，Bonus 代码是讲师给的、允许参考，问题不在「用了参考」，而在于**没有自己的改动、且代码不是自己写的**，答辩时无法解释 fetch → JSON 解析 → 数据整形 → ECharts option 这条链。新的 Carbon Compass（15:23 已生成）已重写结构，但仍必须：①完成「改了什么」清单（≥5 条），②确保每位讲者能不看代码讲清 3 个交互，③没有再次照搬讲师 Bonus 的版式与交互。否则仍会同时压低 Part 3 code（10%）与 Front-End（10%）。

**★ R4 — 演示材料为零**：公司介绍/头像、用户需求、广告三件套、成本效益、安全伦理、结论，合计 **50% 演示权重**没有任何素材。缺这些不是「少几分」，而是演示分可能直接腰斩——按 §b.4，实现满分 + 演示 50 分 = 最终 10/20。

**★ R5 — 安全与责任自相矛盾**：交付代码里带真实 root 密码；API 也没有鉴权与限流（本地演示环境可接受，但必须在安全页说明）。同时 rubric 要求讲「系统的安全与伦理」——如果不处理，Safety & Responsibility 10% 会被扣，而且 ZIP 等于把密码发给讲师/助教。改法很简单：环境变量 + 占位符 + README 说明（§e P0-3）。

**R6 — 数据口径不统一**：讲义写 647,946 行 / 39 地区 / 截至 2026-07-31（那是 2026-09-30 下载版，L10 slide 6 明说「Yours may be a bit bigger」）；我们本地是 655,200 行 / **39** 地区 / 截至 2026-08-31。小组笔记里曾出现「40 个国家/地区」，经 SQL 复核**应为 39**。截图、图表、口播必须统一成自己库里的数字，不要照抄讲义数字。

**R7 — 9 天多人并行、无版本管理**：容易出现「谁覆盖了谁的 index.html」「截图用的是旧版」。**[建议]** 设一个 release 目录 + 每日 21:00 freeze，所有截图从同一版本出；PDF/演示引用同一数据版本。

### d.4 数据事实（已用 SQL 复核，2026-11-18）

| 项目 | 数值 / 内容 |
|---|---|
| 总行数 | 655,200 |
| 地区数 | **39**（含 WORLD、EU27、ROW） |
| 部门数 | 6：Domestic Aviation、Ground Transport、Industry、International Aviation、Power、Residential |
| 日期范围 | 2019-01-01 → 2026-08-31（2,800 天，无缺日） |
| WORLD 行数 | 16,800（= 6 部门 × 2,800 天） |
| 单位 | MtCO₂ per day（**日排放率，不是年度总量**） |
| 来源文件 | `carbonmonitor-global_datas_2026-10-23.csv`（34.5 MB，655,201 行含表头） |
| 数据表 | `carbon_lab.carbon_emission`，InnoDB，utf8mb4；实际结构为 `VARCHAR(100)/FLOAT` 可空 |
| 校验方式 | `COUNT(*)`、`COUNT(DISTINCT country)`、`COUNT(DISTINCT date)`、`MIN/MAX(date)` |

对照讲义：L10 slide 6 的 647,946 行是 2026-09-30 下载版的数字；两者相差约 7,254 行、晚一个月，属正常版本差异。**对外统一说法**：「我们使用 2026-10-23 下载版，共 655,200 行，覆盖 2019-01-01 至 2026-08-31。」

---

## e. 还需要做什么

> 负责人一栏是**角色**，不是人名（不虚构成员信息）；组长在 11-18 当天把角色落到具体成员。工时按 1 人估算，熟练度不同 ±50%。优先级：P0 = 不做会直接丢分/漏交；P1 = 不做演示会缺块；P2 = 锦上添花。

| 优先级 | 事项 | 为什么（对应评分） | 验收标准 | 建议负责人 | 预估工时 |
|---|---|---|---|---|---|
| P0-1 | 补齐 Part 1 SQL 与导入证据 | Part 1 10 分；「数据确实在 MySQL」 | 空库开始能一次跑通；`LOAD DATA` 显示 `Warnings: 0`；4 张截图（导入成功、COUNT/MIN/MAX、DESCRIBE、Workbench）；`.sql` 里路径用占位符 | 数据/DB 角色 | 2 h |
| P0-2 | Part 2 API 讲解材料与截图 | Part 2 10%（演示权重） | 9 个端点返回 200/JSON；`API_reference.md` 表格（URL、参数、返回、对应 SQL）；3 张浏览器截图；任何成员 2 分钟内讲清 `run_sql → jsonify` | API/后端角色 | 2 h |
| P0-3 | 清除真实密码 + 配置说明 | 安全责任 10% + 交付卫生 | 全 ZIP `grep` 无真实密码；`README` 写明 `export DB_PASSWORD=...`、`pip install -r requirements.txt`、`python3 app.py` | API/安全角色 | 0.5 h |
| P0-4 | Part 3 前端定稿（Carbon Compass）+ 改动清单 | Part 3 code 10% + Front-End 10% | `index.html` 离线可跑；≥5 处可指认的改动（结构/交互/叙事/视觉/离线化）；1280 与 1920 宽都正常 | 前端/设计角色（前端主做、另一人交叉验收） | 验收 2 h |
| P0-5 | 最终前端 PDF | 必交件（L17 slide 18） | 6–10 页、每屏可读、含数据来源与日期、含 API 说明、离线打开 | 内容 + 前端 | 3 h |
| P0-6 | 全流程计时彩排 ×2（含媒体与现场演示） | Presentation Skills 10% | 两次都在 9:00–10:00 内完成；每人发言；不看笔记；Q&A 能接住 | 全员 | 4 h |
| P0-7 | 每组向别组提 ≥1 个问题 | 现场规则（录音：不问会扣分，数额未列明） | 准备 3 个备选问题；Q&A 时至少提出 1 个 | 组长 | 0.5 h |
| P1-8 | 海报 + 音频广告 + 视频广告 | Ad Campaign 10% | 三件齐备、同一 slogan/数字/CTA；音频是独立文件；视频有字幕更好；能现场播放 | 视觉/演示角色 | 6–8 h |
| P1-9 | 成本效益页（含假设表） | Cost-Benefit 10% | 一页 3 栏（成本/收益/假设），所有数字标「assumption」；与广告、结论数字一致 | 内容角色 | 2 h |
| P1-10 | Safety & Responsibility / GELSI 页 | Safety 10% | 至少 1 页，G/E/L/S 各 2 条本项目具体风险 + 应对；75 秒能讲完 | 内容角色 | 2 h |
| P1-11 | 结论页 | Conclusion 10% | 回扣 3 类用户、3 个已展示证据、1 个限制、1 个下一步 | 内容角色 | 1 h |
| P1-12 | Deck 组装（11 项顺序 + logo/头像/成员/公司介绍） | 全覆盖、顺序分 | 页面顺序 = rubric 顺序；总页数 ≤ 18；每页 ≤ 25 词；字号投影可读 | 视觉 + 组长 | 4 h |
| P2-13 | `README.md` / `API_reference.md` 英文润色；`requirements.txt` 固定版本 | Part 2 可信度 | 非本组同学按 README 3 步跑起来；`pip install` 一次成功 | API 角色 | 1 h |
| P2-14 | 60–90 秒 dashboard 操作录屏（fallback） | 现场演示可靠性 | 断网/MySQL 故障时仍能讲 | 前端角色 | 1 h |
| P2-15 | 旧 Carbon Pulse 归档 + before/after 对比页 | 证明「自定」不是换皮 | 一页对比截图 + 3 条改动说明 | 组长 | 1 h |
| P2-16 | ER 图 / prototype（可选） | L17 slide 22 的 Key Takeaways 提到，但 slide 23 评分表没有对应条目 **[待确认]** | 先问讲师是否计入、算哪一项；不占用 P0 时间 | 待确认 | — |

### e.1 P0-1 的 SQL 参考骨架（来自 L10 slide 17，路径换成自己的）

```sql
-- 1) 允许本地导入（服务器端；MySQL 重启后需重跑）
SET GLOBAL local_infile = 1;
SHOW VARIABLES LIKE 'local_infile';   -- Value 必须是 ON

-- 2) 建库建表（讲义结构：NOT NULL + DOUBLE）
CREATE DATABASE IF NOT EXISTS carbon_lab;
USE carbon_lab;
CREATE TABLE carbon_emission (
  id      INT AUTO_INCREMENT PRIMARY KEY,
  country VARCHAR(50) NOT NULL,
  date    DATE        NOT NULL,
  sector  VARCHAR(50) NOT NULL,
  value   DOUBLE      NOT NULL
);

-- 3) 导入（CSV 4 列，行尾多一个逗号 → @dummy；日期 DD/MM/YYYY → STR_TO_DATE）
LOAD DATA LOCAL INFILE '/你的路径/carbonmonitor-global_datas_2026-10-23.csv'
INTO TABLE carbon_emission
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(country, @date, sector, value, @dummy)
SET date = STR_TO_DATE(@date, '%d/%m/%Y');

-- 4) 验证（4 条，全部截图）
SELECT COUNT(*) FROM carbon_emission;                          -- 655,200
SELECT MIN(date), MAX(date) FROM carbon_emission;              -- 2019-01-01 / 2026-08-31
SELECT COUNT(DISTINCT country), COUNT(DISTINCT sector) FROM carbon_emission;  -- 39 / 6
SELECT * FROM carbon_emission LIMIT 10;
```

**注意**：本地现有表是 `VARCHAR(100)/FLOAT` 可空结构。若要严格按讲义重导，先 `DROP TABLE`（或 `TRUNCATE` 后再导入），重新 `LOAD DATA`，然后**重拍所有截图**（新库的 AUTO_INCREMENT 会变）。这只是几分钟的操作，但截图与 PDF 必须用重导后的版本，否则「SQL 写一套、库里是另一套」会被追问。

---

## f. 演示怎么排

### f.1 硬规则（先记住这几条）

| 规则 | 要求 | 依据 |
|---|---|---|
| 时长 | 严格 **9–10 分钟** + 1 分钟 Q&A；超时没有「每秒扣多少」的明文，但计入 Presentation Skills 10% | L17 slide 21；摘要 p.10/22、p.20/22 |
| 语言 | 英语 | L17 slide 21；摘要 p.10/22 |
| 发言 | **每一位成员都必须发言**，小组形式；录音另要求平均分配 | L17 slide 21；摘要 p.10/22 |
| 笔记 | **不可使用笔记**；讲义没有禁止使用幻灯片，但不要把讲稿放投影页照着念 | L17 slide 21；摘要 p.11/22 |
| 出席 | 强制；缺席上限 10/20 | L17 slide 19；摘要 p.5/22 |
| 手机 | 静音或震动；录音说电话响会扣分，**数额未列明** | L17 slide 20；摘要 p.11/22 |
| 提问 | 每组至少向其他组问 1 个问题（录音补充，未问会扣分，数额未列明）；举手或等停顿再发言 | L17 slide 20；摘要 p.11/22 |
| 流程 | 先展示海报、再播视频；至少一张安全/伦理页、至少一张结论页 | 摘要 p.9/22 课堂补充 |

### f.2 9 分 30 秒时间分配（[建议]，不是讲师逐项规定）

以下来自摘要 p.12–13/22 的「可参考 9 分 30 秒流程」；Q&A 的 1 分钟另计，广告各段时长讲义未规定。

| 时间 | 内容 | 累计 |
|---|---|---|
| 00:00–00:30 | 公司、logo、成员、卡通头像 | 0:30 |
| 00:30–01:00 | 用户需求 | 1:00 |
| 01:00–01:55 | Part 1 code | 1:55 |
| 01:55–02:50 | Part 2 code | 2:50 |
| 02:50–03:45 | Part 3 code | 3:45 |
| 03:45–05:15 | 自定 dashboard 演示 | 5:15 |
| 05:15–06:15 | 海报、音频、视频广告 | 6:15 |
| 06:15–07:20 | 成本效益 | 7:20 |
| 07:20–08:35 | 安全与责任 | 8:35 |
| 08:35–09:30 | 总结与收结 | 9:30 |

9:30 结束留了 30 秒缓冲；目标是把每次彩排压进 **9:00–9:40**，不要贴着 10:00 结束。

### f.3 谁讲哪段（5 人默认）

| 成员 | 时段 | 内容 | 合计 |
|---|---|---|---|
| 成员 A（组长） | 00:00–01:00 + 08:35–09:30 | 公司/成员/需求 + 结论 | 1:55 |
| 成员 B | 01:00–01:55 + 07:20–08:35 | Part 1 + 安全与责任 | 2:10 |
| 成员 C | 01:55–02:50 + 06:15–07:20 | Part 2 + 成本效益 | 2:00 |
| 成员 D | 02:50–03:45 + 05:15–06:15 | Part 3 code + 广告 | 1:55 |
| 成员 E | 03:45–05:15 | dashboard 演示 | 1:30 |

- 每人 1:30–2:10，基本平均（录音要求「平均分配」）。
- **4 人**：把成员 E 的 dashboard 并入 D，广告给 B；**3 人**：Part 1/2/3 合并讲解，广告与成本效益拆给不同人。原则：每人 ≥ 1:30，且**尽量讲自己做的部分**（无笔记也讲得出来）。
- 卡通头像与成员介绍由每人自己 1 句话，不要由组长代讲。

### f.4 每段只记一句话（无笔记的讲稿骨架）

| 段落 | 只记这一句 | 手上的证据 |
|---|---|---|
| 开场 | 「我们帮关注气候的人读懂每天 65 万行碳排放数据。」 | logo + 5 个头像 |
| 需求 | 「三类用户，其实只要三个问题的答案：哪里、哪个部门、在变好还是变坏。」 | 需求→字段→界面 一页图 |
| Part 1 | 「数据是真的进了 MySQL：655,200 行、2,800 天、39 个地区。」 | `Warnings: 0` 截图 |
| Part 2 | 「同一个 SQL，换成 JSON，浏览器就能读。」 | 浏览器 `/api/sectors` |
| Part 3 | 「页面只做三件事：fetch、reshape、draw。」 | 代码 10 行 |
| Dashboard | 「切年份、点国家、看趋势——这就是用户的使用路径。」 | 现场操作 3 个动作 |
| 广告 | 「同样的信息，三种媒介：海报、音频、视频。」 | 先海报、再视频 |
| 成本效益 | 「成本是假设，收益是情景，我们不把估算说成已经发生。」 | 假设表 |
| 安全责任 | 「最大的风险不是系统崩，而是把估算当成实测。」 | GELSI 一页 |
| 结论 | 「数据、查询、图表、用户——四步都通了；下一步是 uncertainty。」 | 回到开场那句话 |

### f.5 无笔记技巧

1. 只背「每段第一句 + 1 个数字」；其余靠屏幕上的图讲，图就是提示卡。
2. 讲自己写的那段代码/那张图——自己做的部分，忘词也能指着屏幕说下去。
3. 背熟 5 个转场句：「That is Part 1. Now the API.」「So what does the user see?」等；转场不卡，整场就顺。
4. 彩排时把讲稿收起来，只留每页 3 个关键词；**不把关键词卡带上台**（可以放在讲台边，但不拿在手里）。
5. 用鼠标/激光笔指图，不要对着屏幕念；每页停留 ≥ 15 秒，别急着翻。
6. 兜底：忘词就回到「数据 → 查询 → 图表 → 用户」四步链，讲当前这张图回答哪一步的问题。

### f.6 常见扣分点与预防

| 扣分点 | 依据 | 预防 |
|---|---|---|
| 超时或明显不足 9 分钟 | L17 slide 21；摘要 p.10/22（无每秒罚则） | 两次计时彩排；9:30 目标；留 30 秒缓冲 |
| 使用笔记/讲稿 | L17 slide 21 明文 | 关键词卡不上台；两次无稿彩排 |
| 一人包办 | L17 slide 21 + 录音要求平均 | 5 段分工，每人 ≥1:30；转场说名字 |
| 电话响 | L17 slide 20（录音：会扣分，数额未列明） | 上台前全部静音/飞行模式，组长逐个检查 |
| 不向别组提问 | 录音 07:46–07:57（会扣分，数额未列明） | 准备 3 个问题；Q&A 第一个举手 |
| 缺席 | L17 slide 19（上限 10/20） | 全员到场；提前确认时间 |
| 只放静态截图、不解释来源 | 摘要 p.2/22「Avoid」 | 每张截图配一句「这是哪个 API / 哪张表」 |
| 把未完成说成完成 | 摘要 p.2/22、p.9/22 | 明说「planned / not in this version」 |
| 漏音频广告 | 摘要 p.8–9/22 | 三件套检查表；音频独立文件 |
| 数字/单位/国家不一致 | 摘要 p.22/22 checklist | 统一 655,200 / 39 地区 / MtCO₂ per day / 至 2026-08-31 |
| 演示打不开（`file:///`、5500 端口、断网） | L17 slide 14、17；摘要 p.14/22 | 只用 `http://127.0.0.1:5001/`；静态资源本地化；录屏 fallback |
| 漏交最终前端 PDF | L17 slide 18 | ZIP 四件套清单逐项勾 |
| 迟交 | 摘要 p.3/22 | 11-26 晚前上传，不留到最后一刻 |

### f.7 现场演示脚本（3:45–5:15 只用三个动作）

**上台前 10 分钟**：启动 MySQL → `SELECT COUNT(*)` 确认 655,200 → 启动 `python3 app.py` → 打开 `/api/health` 确认 `ok: true` → 打开 `http://127.0.0.1:5001/` → 把页面从上到下滚一遍让图表完成首次渲染 → 关掉通知/其他窗口 → 浏览器缩放到投影可读（110–125%）→ 确认 fallback 录屏在桌面。

**演示顺序**（讲义建议的排查顺序也是这个）：MySQL（一句话 + 一张表）→ API JSON（一个端点）→ 页面（整屏）→ 图表（交互）。**不要现场改代码、不要现场装包、不要开第二个终端。**

**Fallback**：MySQL 挂了 → 用 60–90 秒录屏 + 截图讲，不硬撑；端口占用 → 改 5002 并提前记住；投影偏色 → Carbon Compass 是亮色主题，比旧版深色更稳。

### f.8 Q&A（1 分钟）与向别组提问

**最可能被问的 5 个问题**（答案要点）：

1. **数据有多少？** 655,200 行、39 个地区、6 个部门、2,800 天、2019-01-01 至 2026-08-31、单位 MtCO₂/day。
2. **估算数据可信吗？** Carbon Monitor 是近实时估算、方法公开；我们明确它是估算，标注覆盖范围与日期，不用于问责单个国家。
3. **SQL 怎么变成 JSON？** `pymysql` 连接 → `DictCursor` → `cursor.execute` → `fetchall` → `jsonify`；所有参数用占位符。
4. **图表怎么画的？** `fetch` 拿 JSON → 在 JS 里 reshape → ECharts `setOption`；图表库本地化，断网可跑。
5. **成本效益数字哪来的？** 全部是假设：开发工时、托管/维护、零图表许可成本；标在假设表里，给区间不给单点。

**给别组准备的 3 个问题**（任选其一，举手问）：

1. 「你们的 dashboard 怎么处理最新一年数据不完整？会直接加总吗？」
2. 「地图上哪些国家没有数据？你们怎么让用户不把‘没数据’读成‘零排放’？」
3. 「你们的成本效益里，哪一个假设最敏感？如果它错了会怎样？」

### f.9 彩排计划（按 11-27 倒排）

| 时间 | 做什么 | 验收 |
|---|---|---|
| 11-20（T-7） | 分段走场：每人 2 次，只讲自己那段 | 每段 ≤ 分配时间 +10 秒 |
| 11-24（T-3） | 全流程 1 次，录像回看 | 找出 3 个卡点并改 |
| 11-26（T-1） | 全流程 2 次（真演示 + 真媒体 + 真切换） | 两次 9:00–10:00；无笔记 |
| 11-27 当天 | 提前 30 分钟到场，设备测试 5 分钟 | 手机静音、PPT/视频/音频都能放 |

---

## g. 数据与伦理

这一节直接支撑 **Safety & Responsibility 10%**；同时是 Part 1/2/3 讲解里「我们知道自己数据的边界」的加分点。GELSI 是耶鲁数字伦理中心（Yale Digital Ethics Center，见 L19 slide 20 的链接）与世界经济论坛 C4IR 推广的框架（L19 slide 22），L19 展开的是 Governance、Ethical、Legal、Social 四项（slides 23–26）。

### g.1 数据来源、许可与引用

- 数据源：**Carbon Monitor**（https://carbonmonitor.org/），公开可下载的全球日度 CO₂ 估算数据；讲义把它作为 open dataset 使用（L10 slide 6）。
- 引用：使用与展示时注明 **Carbon Monitor**，并引用其方法论文献 **arXiv:2004.13614**（近实时全球 CO₂ 排放监测）。**[建议]** 在 PDF 末页与 dashboard footer 各放一次。
- 不声称数据所有权：我们只是使用者与可视化者；不要写「our data」，写「data from Carbon Monitor」。
- **[待确认]** Carbon Monitor 的具体许可条款（如 CC BY 4.0）与官方引用格式，以官网 FAQ / 下载页为准；拿不准就写「open data, cited」。

### g.2 「living dataset」与口径

Carbon Monitor 是持续更新的数据集，**同一下载日的文件，过几天再下数字会变**。我们的处理：

- 全项目锁定一个版本：`carbonmonitor-global_datas_2026-10-23.csv`（655,200 行，至 2026-08-31）。
- 所有截图、PDF、演示标注「data downloaded 2026-10-23; coverage 2019-01-01 – 2026-08-31」。
- 口播统一说 655,200，不引用讲义的 647,946（那是 2026-09-30 版的数字）。
- 数据更新后，`/api/health` 的 `last_day` 和 `insights` 的数字会跟着变——演示前必须重跑一次并重新截图。

### g.3 「估算」不是「实测」

- Carbon Monitor 的数字是**基于活动数据的近实时估算**，不是电厂/烟囱的实测值；PPT 与 PDF 里凡出现数字，建议第一次出现时加一句「estimated」。
- 单位是 **MtCO₂ per day**（日排放率），不是年总量；图里必须标单位，不要把 12 个月的日值相加后说成「年度排放」。
- 2026 年只有 8 个月：**不要把不完整年份直接和完整年份比**。新 `app.py` 已用「最近完整年份」和「年初至今同期（YTD）」处理（`latest_complete_year()`、`insights` 的 `ytd` 字段），这是很好的演示素材——它正是一个「技术上正确、伦理上也负责」的设计选择。
- 冬季上升与 2020-04 的下跌可以讲（L17 slide 10 的解读示例：COVID lockdown、供暖与电力），但要说明「这是估算数据呈现的模式，不等于因果证明」。

### g.4 GELSI 一页纸（映射到本项目）

| GELSI | 本项目的具体问题 | 我们的应对 | 演讲一句话 |
|---|---|---|---|
| **G**overnance | 谁对 dashboard 上的结论负责？数据版本与口径谁维护？ | `/api/health` 暴露行数与日期范围；README 记录数据版本与下载日；单一 release 目录、截图与 PDF 同版本 | 「我们的数字有版本、有日期、可追溯。」 |
| **E**thical | 估算值被当成实测；国家排名造成污名；覆盖偏差 | 标注「estimated」；地图对无数据国家灰显并写「no data ≠ zero」；Top 10 只展示变化与份额，不做「谁最差」的排名羞辱 | 「我们让用户看到‘不知道’，而不是假装知道。」 |
| **L**egal | 数据许可与引用；EU27/ROW 等聚合口径与国家并列的歧义；无个人数据 | 引用 Carbon Monitor 与文献；界面注明数据来源；声明「本项目不含个人数据」；聚合区（EU27/ROW）在界面中标注 | 「数据是别人的，标注是我们的责任。」 |
| **S**ocial | 用户可能据此问责国家/企业；数字素养差异；可访问性；数据基础设施成本 | 界面写「for awareness, not accountability」；键盘可操作、对比度足够、不靠颜色单独编码；资源本地化减少现场网络依赖 | 「这是帮人理解趋势的工具，不是法庭证据。」 |
| **I**mplications（L19 未单列页） | 未来若接入更多数据源/更细粒度，隐私与再识别风险上升 | 结论页写「next: uncertainty intervals + methodology page」；不做个人级数据 | 「下一步是把不确定性也画出来。」 |

L19 的 GELSI 框架只展开了 G/E/L/S 四项（slides 23–26）；**Implications** 是缩写的一部分但讲义没有单独一页，所以放在结论/未来工作里讲即可，不要为它单开一页挤占时间。

### g.5 不虚构红线（演示与材料通用）

- 不编用户数、合作方、试点、收益、实验结论；没有就说「we have not tested with real users」。
- 成本效益的所有数字必须标注**假设**（assumption），给区间比给单点更稳；同一数字在广告、成本页、结论页保持一致。
- 不把「计划做」说成「已经做」；未完成的功能明说「planned」。
- 不把估算数据说成实测；不把日值说成年值；不把 2026 部分年份和完整年份直接比。

### g.6 伦理内容放在哪

- Dashboard footer：`Data: Carbon Monitor (estimated) · coverage 2019-01-01 to 2026-08-31 · for awareness, not accountability`
- 最终前端 PDF：最后一页「Data source & limitations」。
- 演示 deck：Safety & Responsibility 一页 + 结论页一句「limitations」。
- 代码：`app.py` 顶部注释写数据来源与单位（新版已写 `UNIT`、`SOURCE`，继续保持）。

---

## h. 提交前 checklist

> 用法：打印或复制到群里，做完一项勾一项；每项后面写负责人与日期。

### A. 提交包（ZIP）

- ☐ ZIP 内有 Part 1 code（`Part_1_setup.sql` + 验证 SQL + 截图）
- ☐ ZIP 内有 Part 2 code（`app.py` + `requirements.txt` + `API_reference.md`）
- ☐ ZIP 内有 Part 3 code（`index.html` + `static/` + `README.md` + 截图）
- ☐ ZIP 内有最终前端 PDF（`Carbon_Compass_Final_Frontend.pdf`）
- ☐ ZIP 内有演示材料（deck、海报、音频、视频、成本效益）
- ☐ ZIP 内**没有**真实密码、`.DS_Store`、`__pycache__`、`.venv`
- ☐ 本地解压过一次，所有文件能打开；PDF 能离线打开
- ☐ 文件命名带组名/品牌/日期，无中文、无空格
- ☐ Moodle 已提交并截图显示成功（不是只放在电脑里）

### B. Part 1 / 2 / 3 证据

- ☐ Part 1：`LOAD DATA` 成功截图（`Warnings: 0`）
- ☐ Part 1：`COUNT(*)` / `MIN,MAX(date)` / `DISTINCT country,sector` 截图
- ☐ Part 1：`DESCRIBE carbon_emission` 截图（与 SQL 文件一致）
- ☐ Part 1：MySQL Workbench 表视图截图
- ☐ Part 2：`/api/sectors`、`/api/monthly` 浏览器 JSON 截图
- ☐ Part 2：`/api/health` 返回 `ok: true` 截图
- ☐ Part 2：`API_reference.md` 覆盖 9 个端点
- ☐ Part 3：`index.html` 截图（1280 与 1920 宽各一组）
- ☐ Part 3：能当场解释 `fetch → reshape → setOption`
- ☐ 页面从 `http://127.0.0.1:5001/` 打开（不是 `file:///`，不是 5500）

### C. 演示内容（11 项全覆盖）

- ☐ 公司介绍 + logo（Carbon Compass Analytics）
- ☐ 成员介绍 + 卡通头像（每人一张，与 Moodle 注册一致）
- ☐ 问题、使命、方案（30 秒内讲完）
- ☐ User Requirements（需求 → 字段 → 查询 → 界面）
- ☐ Part 1 code 讲解（不是截图流水账）
- ☐ Part 2 code 讲解（连接、SQL、`jsonify`）
- ☐ Part 3 code 讲解（fetch、转换、画图）
- ☐ 自定 dashboard 现场演示（≥3 个交互）
- ☐ 海报 + 音频广告 + 视频广告（三件齐）
- ☐ 成本效益（成本/售价/利润 + 假设表，数字一致）
- ☐ 安全与责任（≥1 页，G/E/L/S 具体风险与应对）
- ☐ 结论（回扣需求、成果、价值、限制、下一步）
- ☐ 全程英语、每人发言、无笔记
- ☐ 9–10 分钟内完成（彩排 2 次达标）
- ☐ 准备好 3 个问别组的问题

### D. 现场与排练

- ☐ 全员到场（缺席上限 10/20）；手机全部静音/震动
- ☐ 提前 30 分钟到场，测试投影、音频、视频、网络
- ☐ MySQL + `app.py` + 浏览器页面全部提前启动
- ☐ 60–90 秒 fallback 录屏在桌面
- ☐ 至少 2 次完整计时彩排，含媒体与转场
- ☐ 讲稿关键词卡**不拿上台**

### E. 数据与伦理

- ☐ 所有数字统一：655,200 行 / 39 地区 / 6 部门 / 2019-01-01–2026-08-31 / MtCO₂ per day
- ☐ 所有截图与 PDF 来自同一数据版本（2026-10-23 下载）
- ☐ 引用 Carbon Monitor + arXiv:2004.13614
- ☐ 明确「估算，不是实测」「for awareness, not accountability」
- ☐ 成本效益所有数字标 assumption，未完成功能标 planned

---

## 附录 A：待确认清单

以下事项讲义与录音都**没有写明**，或需要向讲师确认；不要自行假设、更不要编造数字。

1. **小组注册**：组名「Data Fanatics」、成员与学号是否已按 L10 slide 2 的要求回复帖子；演示材料上的组名必须与 Moodle 注册一致。**[待确认]**
2. **出场时段**：演示在 11 月 27 日最后一堂课，各组具体时段「另行确认」（摘要 p.10/22）。**[待确认]**
3. **广告时长与播放方式**：海报/音频/视频是分开播还是合并播、各自多长，讲义未规定（摘要 p.9/22、p.20/22）。**[待确认]**
4. **PDF 页数与结构**：L17 slide 18 没有规定，截图+说明即可（摘要 p.3/22）。**[待确认]**
5. **扣分数额**：迟交（按日）、电话响、不问别组、超时——录音提到会扣分，但**数额全部未列明**（摘要 p.19–20/22）。不要在演示中引用具体数字。**[待确认]**
6. **ER 图 / prototype**：L17 slide 22 的 Key Takeaways 提到 ER Diagram、Prototype、Functions，但 slide 23 评分表没有这些条目；若要做，先问讲师对应哪一项（摘要 p.20/22 也建议确认）。**[待确认]**
7. **Part 3 的 5% 是否包含 presentation**：slide 2 的措辞与 slide 24–25 的公式不一致；以公式为准，但可向讲师确认。**[待确认]**
8. **现场设备**：是否用自己的笔记本、投影比例（16:9 / 4:3）、是否有 HDMI/USB-C 转接、音频能否从电脑外放。**[待确认]**
9. **Carbon Monitor 许可条款**：具体 license 与官方引用格式，以官网为准。**[待确认]**
10. **数据库账号**：演示用 root 还是新建只读用户；若讲师要求 root，就在安全页说明「仅本地演示环境」。**[待确认]**

---

## 附录 B：出处索引（写作/答辩时查证用）

| 主题 | 出处 |
|---|---|
| 项目三部分与数据流 | L10 slide 3；L14 slide 3；L17 slide 3–4；摘要 p.1–2/22 |
| 实现分 10/5/5，合计 20 | L10 slide 4；L14 slide 2；L17 slide 2；摘要 p.4/22 |
| 截止 2026-11-27 18:00 HKT | L10 slide 4；L17 slide 18；摘要 p.3/22 |
| ZIP 四件套 | L17 slide 18；摘要 p.3/22 |
| 最终公式与两个例子 | L17 slide 24–25；摘要 p.4–5/22 |
| 11 项 rubric 与权重 | L17 slide 22–23；摘要 p.6–9/22 |
| 缺席上限 10/20 | L17 slide 19；摘要 p.5/22 |
| 9–10 分钟 + 1 分钟 Q&A、英语、每人、无笔记 | L17 slide 21；摘要 p.10–11/22 |
| 手机、提问、准时 | L17 slide 20；摘要 p.11/22 |
| 先海报后视频、安全页、结论页 | 摘要 p.9/22（课堂补充 09:36–10:45） |
| 9 分 30 秒流程 | 摘要 p.12–13/22 |
| Phase 3 任务与常见错误 | 摘要 p.13–19/22；L17 slide 4–17 |
| 「原样两图不够」「要自定」 | 摘要 p.16/22（录音 22:14–24:26）；L17 slide 12 |
| 数据规模/单位/39 地区（讲义版） | L10 slide 6 |
| CSV 列与 `LOAD DATA`/`STR_TO_DATE` | L10 slides 8、13、17 |
| 本地库统计（655,200 / 39 / 2,800 天） | SQL 复核，2026-11-18（见 §d.4） |
| GELSI 定义与 G/E/L/S | L19 slides 22–26 |
| 数据伦理概念（隐私、偏差、透明、问责） | L19 slides 11–18 |
| Moodle Bonus dashboard 内容 | L17 slide 12；旧 `index.html` 与 `carbon_pulse.txt` |

---

*本文依据 2026-11-18 可获取的讲义、双语摘要与本地文件整理；讲义未列明的事项已标 **[待确认]**，建议性做法已标 **[建议]**。如 Moodle 或讲师后续通知与本文冲突，以官方通知为准。*

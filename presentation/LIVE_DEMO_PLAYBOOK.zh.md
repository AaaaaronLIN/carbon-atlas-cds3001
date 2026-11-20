# Carbon Atlas · 现场 Live Website 演示手册（TA / 全组版）

> 目标：在 9:23 的演示里，用**教室 Windows 电脑的浏览器**打开真实网站（Flask → MySQL → 页面），而不是只看 PPT 里的录屏；同时保留 **90 秒视频**作为一键 fallback。
> 本文所有命令都在自己的 Mac 上执行；Windows 教室电脑只需要 **打开一个 URL**。

---

## 0. 先看结论：三种方案，推荐组合

| 方案 | 教室需要 | 优点 | 风险 | 用途 |
|---|---|---|---|---|
| **A. Cloudflare Tunnel（推荐主方案）** | 教室 Windows 能上网 | 一条 HTTPS URL；Windows 不用装任何东西；Mac 跑真 MySQL/Flask | 依赖 Mac 不睡眠、公网窗口期；学校网络可能挡 | **首选 live 90 秒** |
| **B. Mac 热点 + 局域网 LAN** | Mac 和 Windows 在同一 Wi-Fi/热点 | 不需要互联网；完全本地 | 需要 macOS Internet Sharing 或旅行路由器；校园 Wi-Fi 可能隔离客户端 | A 失败时备选 |
| **C. 90 秒录屏 fallback** | 无 | 100% 可控、已经在 S7 内嵌 | 不算“live” | 任何失败 5 秒内切回 |

**最终建议**：A 作为 primary（今天已实测 tunnel 返回 200）；B 作为备用；C 永远留在 PPT 里。
**不推荐**：把 MySQL/Python 装到教室 Windows 上来跑——不可控、时间成本高。

---

## 1. 角色分工（live 时）

| 角色 | 谁 | 任务 |
|---|---|---|
| Operator（点网页） | **LAI Patten** | 拿无线鼠标/触控板，按 cue card 点；出问题 5 秒内 Alt+Tab 回 PPT |
| 旁白 A（0:00–0:44） | **LAI Patten** | 讲 hero → map → ranking；手点网页 |
| 旁白 B（0:48–1:30） | **HUANG Haolin** | 讲 sector → trend → findings → method |
| 计时 / 切换 | **LIN Xiaotong** | 看表报“3:48 切 live”“5:21 回 PPT”；不碰电脑 |
| 备用 | WENG / LIM | 递 U 盘、盯网络灯；不操作 |

> 实际操作只让 **一个人** 碰电脑（LAI），避免两只手抢鼠标。

---

## 2. 方案 A：Cloudflare Tunnel（推荐，今天已实测）

### 2.1 在 Mac 上启动数据库 + Flask

```bash
cd "/Users/aronlin/dev/deepseek-harness/default-workspace/CDS3001_CarbonAtlas_GroupProject/01_WebApp_Code"

# 1) 确认 MySQL 在跑（有输出 "mysqld is alive" 即可）
mysqladmin -u root -p ping

# 2) 启动 Flask（HOST=0.0.0.0 才能被浏览器/隧道访问）
export DB_PASSWORD='你的MySQL密码'
HOST=0.0.0.0 PORT=5001 python3 app.py
```

另开一个终端验证：

```bash
curl -s http://127.0.0.1:5001/api/health
# 应该看到 "rows": 655200, "last_day": "2026-08-31"

curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:5001/
# 200
```

### 2.2 启动 cloudflared（免费临时公网 URL）

```bash
cd /tmp

# Apple Silicon（M1/M2/M3…）
curl -L -o cloudflared.tgz \
  https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-arm64.tgz
# Intel Mac 把 arm64 换成 amd64

tar -xzf cloudflared.tgz
chmod +x cloudflared

./cloudflared tunnel --url http://127.0.0.1:5001 --no-autoupdate
```

终端会打印类似：

```
https://warrior-engine-ventures-bedding.trycloudflare.com
```

**把这个 URL 复制到 Windows 浏览器打开**。这个 URL 每次重启 tunnel 都会变，**当天以新打印的为准**。

### 2.3 验证（重要）

- 用**手机 4G/5G**（不要连教室 Wi-Fi）打开这个 URL → 能看到 Stage 首页 + 右上角 `API live · 655,200 rows`；
- 再用教室 Windows 打开一次；
- 若两者都 200，live 方案可用。

### 2.4 Mac 防睡眠 / 防掉线

```bash
# 演示期间保持 Mac 唤醒（Ctrl+C 结束）
caffeinate -dimsu
```

- 接电源，关掉“低电量自动睡眠”；
- 关通知（Focus / Do Not Disturb）；
- 不要再点 sleep / 合盖；
- 保持 tunnel 终端和 Flask 终端窗口开着（最小化可以，不要关）。

### 2.5 安全说明（TA 可能会问）

- 隧道只暴露**只读**页面；没有写接口、没有登录、没有密码下发；
- `app.py` 的 DB 密码只在本机环境变量里，不会出现在页面/仓库；
- 演示结束 `Ctrl+C` 关掉 cloudflared 和 Flask 即可；
- 如果担心公开，临时 tunnel 只在那几分钟有效，URL 随机。

---

## 3. 方案 B：Mac 热点 + 局域网（无互联网也能 live）

适用：学校网络挡 443/tunnel，但允许自带热点。

### 3.1 macOS Internet Sharing（推荐）

1. Mac 先有互联网：接 **Ethernet** 或 **iPhone USB**（不要用同一个 Wi-Fi 做共享源）；
2. **System Settings → General → Sharing → Internet Sharing** 点 (i)；
3. **Share connection from**：Ethernet / iPhone USB；
   **To computers using**：Wi-Fi；
4. **Wi-Fi Options**：Network name `CarbonAtlas-Demo`，设置密码，Done；
5. 打开 **Internet Sharing** 开关；
6. Windows：连 `CarbonAtlas-Demo`；
7. Mac 查热点 IP（通常是 `192.168.2.1`）：

```bash
ipconfig getifaddr bridge100   # 有的系统是 bridge100
# 或
ifconfig | grep -A2 "bridge"
```

8. Windows 浏览器打开：

```
http://192.168.2.1:5001/
```

### 3.2 备选：iPhone 个人热点
- Mac 和 Windows 都连 iPhone 热点；
- Mac 上 `ipconfig getifaddr en0` 查 IP；
- 部分运营商/热点会**隔离客户端**（Windows ping 不到 Mac），先试 `ping <Mac-IP>`；不行就回到 Internet Sharing 或 tunnel。

### 3.3 防火墙

macOS 如果开了防火墙：
- **System Settings → Network → Firewall → Options**，允许 `Python` 接收传入连接；
- 或在演示前临时关闭防火墙（演示后打开）。

---

## 4. 教室 Windows 浏览器怎么准备（30 秒）

1. 提前打开 **Edge 或 Chrome**；
2. 地址栏输入 tunnel URL / `http://192.168.2.1:5001/`；
3. **F11** 全屏；**Ctrl+Shift+B** 隐藏书签栏；缩放 90%（Ctrl+- 一次）；
4. 关闭其他标签页，只留网站；
5. 关闭系统通知 / 微信 / 弹窗；
6. 先滚到 Team / Method 再回顶部，确认图片、图表都加载（预热缓存）；
7. 保持这个标签页，**不要关**；演示时 Alt+Tab 直接回来。

> 分辨率建议 1920×1080 或 1280×720；如果教室投影是 1024×768，浏览器缩到 80%，先试一次。

---

## 5. 90 秒 live 演示脚本（与讲稿 6a/6b 对齐）

> 时钟：**3:48 切浏览器**（比原来 3:51 提前 3 秒，吸收切换时间）；**5:21 回 PPT**。
> 总时长仍是 90 秒；切换 + 操作约 3 秒，已用提前量吸收。

| 页面时间 | 时钟 | 操作（LAI） | 画面 / 旁白 |
|---|---|---|---|
| 0:00 | 3:48 | Alt+Tab 到浏览器；鼠标放地球 | hero：globe 旋转、KPI；LAI：“This is the live build — MySQL → Flask → this page.” |
| 0:08 | 3:56 | 拖一下地球（或停住） | 展示可交互；说“every number below is a SQL query” |
| 0:14 | 4:02 | 点 **Play the brief**（若不想等故事，8 秒后点 Skip） | 故事模式 2019→2020→2025 |
| 0:24 | 4:12 | 点 **Skip**（如还在故事） | 回 hero |
| 0:26 | 4:14 | 滚到 **Where**；国家选 **China** | 地图 + ranking；LAI 讲 China 31.9%、top five 61% |
| 0:36 | 4:24 | 点 ranking 表头 **VS 2019** 排序 | 展示可排序/可比较 |
| 0:44 | 4:32 | 交棒 HUANG；滚到 **What** | 部门图；HUANG 接 |
| 0:48 | 4:36 | 选 **India** | sector/weekday 变化 |
| 0:56 | 4:44 | 滚到 **When**；Compare 选 **United States** | 双国对比 |
| 1:02 | 4:50 | 点 **Index · 2019 = 100** | 指数模式 |
| 1:10 | 4:58 | 滚到 **Findings** | 六张 findings |
| 1:18 | 5:06 | 滚到 **Method / GELSI** | 责任面板 |
| 1:24 | 5:12 | 点 **☀ Day / Stage** 切一次主题（可选，若时间够） | 展示双主题 |
| 1:28 | 5:16 | 回顶部 | 收尾 |
| 1:30 | **5:21** | **Alt+Tab 回 PPT**（S8/S12） | HUANG 收句 “The product is done. Now the campaign.” |

> 若某一步点错：**不要回头解释**，直接继续下一个动作；旁白按“画面现在是什么”讲，不要按秒数硬对。

---

## 6. 讲稿要改的 3 句话（live 版）

原稿是按“播录屏”写的；如果确定 live，把这三句换掉：

| 位置 | 原句 | live 版 |
|---|---|---|
| LAI 6a 开头 | “That is the code. Here is the recording.” | “That is the code. **Let me open the live build.**” |
| LAI 6a | “This is a recording of the build running from MySQL on our machine.” | “**This is the live build — MySQL → Flask → this page.**” |
| HUANG 6b 开头 | “The recording continues…” | “**Still live — now the what and the when.**” |

其余 6a/6b 的旁白内容不变（顺序、数字、交接句都保持）。

---

## 7. 失败处理（< 5 秒，不在台上 debug）

| 症状 | 处理 |
|---|---|
| Alt+Tab 后页面空白/转圈 | 数到 5；没出来就 **Alt+Tab 回 PPT → 点 S7 海报播 90 秒录屏**；说一句 “I'll show the recorded build.” |
| 右上角 `API offline` | 直接切回视频（说明网络问题，不在台上重启 MySQL） |
| Tunnel URL 打不开 | 切回视频；如还有时间，改用 LAN URL（提前准备好） |
| 教室电脑没有浏览器/被锁 | 用 PPT 视频 + U 盘独立 mp4 |
| 投影 1024×768 太挤 | 浏览器 Ctrl+- 到 80%；或全程用视频 |
| Mac 睡眠/合盖 | 视频；下次彩排开 `caffeinate` |

**原则：live 是加分项，不是风险项；5 秒内切回视频，评委不会扣“没 live”，但会扣“台上修电脑”。**

---

## 8. 排练与验收（至少 2 次）

1. **T-2 天**：Mac 本地 + tunnel 在手机 4G 打开成功；截一张手机成功图发群；
2. **T-1 天**：教室/类似 Windows 上打开 tunnel URL，F11，跑一遍 90 秒 click cue；用手机计时，必须 **90±3 秒**；
3. **全组 dress**：从 S7 前一句开始，LAI 切浏览器，HUANG 接，5:21 回 PPT，继续 S8；全程 9:23 ±5 秒；
4. **失败演练**：故意断网/关 tunnel，从 live 切回视频，计时 ≤5 秒；
5. 把 click cue 打印一张给 LAI（`LIVE_DEMO_OPERATOR_CARD.md`）。

---

## 9. 当天 Pre-flight Checklist（打印）

### Mac
- [ ] 充电器 + 转接头
- [ ] MySQL 在跑：`mysqladmin -u root -p ping`
- [ ] Flask 在跑：`/api/health` 返回 655,200
- [ ] `HOST=0.0.0.0` 启动
- [ ] cloudflared tunnel 已开，URL 已复制
- [ ] 手机 4G 打开 URL 成功
- [ ] `caffeinate -dimsu` 已开
- [ ] 通知关闭、Mac 不睡眠
- [ ] 90 秒视频在 S7 可播（fallback）

### Windows 教室电脑
- [ ] 能上网 / 或连上 Mac 热点
- [ ] 浏览器打开 tunnel/LAN URL
- [ ] F11 全屏、Ctrl+Shift+B 隐藏书签、缩放 90%
- [ ] 页面右上角 `API live · 655,200 rows`
- [ ] 图表/地球/Team 都加载过（预热）
- [ ] 只留一个网站标签页
- [ ] 音量（如果 Q&A 要看视频）正常

### 备用
- [ ] U 盘：`Carbon_Atlas_Deck.pptx`、`Carbon_Atlas_Deck.pdf`、`carbon_atlas_demo_90s.mp4`、`Carbon_Atlas_Final_Frontend.pdf`
- [ ] 手机热点（作第二网络）
- [ ] 打印的 Operator Card

---

## 10. 对 TA / 评委可以这样解释（英文口述）

> “This is not a static screenshot. The page is served by our Flask API, which queries the MySQL table built in Part 1 — 655,200 rows. The tunnel/LAN is only how we reach the classroom browser. If the classroom network blocks it, the same build is embedded as a 90-second recording on slide 7, so the demo is never lost.”
>
> 中文：**“这不是静态截图；页面由 Part 1 建好的 MySQL 表经 Flask API 实时查询。Tunnel/局域网只是把教室浏览器接到我们电脑的方式；网络被挡时，同一版本的 90 秒录屏已经内嵌在 S7。”**

---

## 11. 今天已做的实测

- `HOST=0.0.0.0` 启动后：`http://10.9.64.72:5001/` 返回 **200**；
- cloudflared quick tunnel：公网 URL 的 `/` 与 `/api/health` 均返回 **200**；
- 这些 URL 是临时的，演示当天重新生成即可。

---

## 12. 如果你要“完全离线”的 live（进阶，需提前说）

可以另做一个 **static snapshot 版**（把同一份数据冻结成 JSON，双击 `index.html` 即可打开，不需要 MySQL/网络）。这需要额外开发/测试；当前最稳的 fallback 仍是 **S7 录屏 + U 盘**。

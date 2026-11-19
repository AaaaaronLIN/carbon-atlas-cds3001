# GitHub 仓库信息与日常操作

> **本 repo 已经发布为 public**：<https://github.com/AaaaaronLIN/carbon-atlas-cds3001>
> 默认分支 `main`，最新 commit 见仓库页；组员凭链接即可浏览/下载，不需要邀请。

## 1. 组员怎么拿
```bash
git clone https://github.com/AaaaaronLIN/carbon-atlas-cds3001.git
cd carbon-atlas-cds3001
```
或者直接在网页上点 **Code → Download ZIP**；也可以打开 `README.md` 在线阅读。

## 2. 本地仓库路径变了（GitHub Desktop 报 "Can't find" 的原因）
Lead 把本地文件夹改名成更清晰的结构，旧路径不存在了：

- 旧：`.../default-workspace/project/repo/carbon-atlas-cds3001`
- 新：`.../default-workspace/CDS3001_CarbonAtlas_GroupProject/03_GitHub_Repo/carbon-atlas-cds3001`

**修复 GitHub Desktop**：
1. 在报错页点 **Locate…**；
2. 选择上面的新路径（Finder 里 ⌘+Shift+G 可直接粘贴路径）；
3. 仓库会恢复，remote 仍然是 `https://github.com/AaaaaronLIN/carbon-atlas-cds3001.git`。
> 不要点 "Clone Again"，除非你想在别处重新 clone 一份。

## 3. 日常提交 / 推送（组员有写权限时）
```bash
cd CDS3001_CarbonAtlas_GroupProject/03_GitHub_Repo/carbon-atlas-cds3001
git add -A
git commit -m "describe the change"
git push
```
如果是 private repo，需要先被邀请为 collaborator（Settings → Collaborators）。

## 4. 公开 vs 私有
- **public（当前）**：组员/老师有链接即可看；注意 repo 里含成员姓名和学号（rubric 需要），如果不想公开请改回 private 并邀请组员。
- **private**：GitHub → Settings → Collaborators → 邀请组员的 GitHub 用户名；或 Settings → General → 改 visibility。
- repo 里 **没有真实 MySQL 密码**（`code/app.py` 用 `DB_PASSWORD` 环境变量/占位符），也 **没有原始 CSV**。

## 5. 建议的仓库设置（可选，但更专业）
- Description：`CDS3001 group project — Carbon Atlas (Data Fanatics)`
- Topics：`data-visualization`, `mysql`, `flask`, `echarts`, `carbon-emissions`, `cds3001`
- 把 repo 链接设为 group chat 置顶。

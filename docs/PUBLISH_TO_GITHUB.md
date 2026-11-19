# 把本 repo 发布到 GitHub（让组员都能看到）

> 本 repo 已在本机初始化好 git（main 分支、已提交）。只差"推到远端"这一步。
> 我（Lead）没有你的 GitHub 账号授权，所以远端创建/推送需要你操作一次。

## 方式 A：GitHub Desktop（最简单，推荐）
1. 打开 **GitHub Desktop** → File → **Add Local Repository…** → 选择本文件夹 `carbon-atlas-cds3001`；
2. 点右上 **Publish repository**；
3. 取消勾选 "Keep this code private"（组员凭链接即可看）或保持 private（需要邀请组员）；
4. Publish → 把仓库链接发群。
   - Private 又想组员看：GitHub → repo → Settings → Collaborators → 邀请组员的 GitHub 用户名。

## 方式 B：先在 GitHub 网站建空 repo，再命令行推送
1. github.com → New repository → 名字 `carbon-atlas-cds3001` → **不要**勾 README/.gitignore → Create；
2. 在本文件夹执行：
```bash
cd carbon-atlas-cds3001
git branch -M main
git remote add origin https://github.com/<你的用户名>/carbon-atlas-cds3001.git
git push -u origin main
```
3. macOS 第一次可能弹 GitHub 登录/Keychain 授权，按提示登录即可。

## 方式 C：不建远端，直接发压缩包
- 直接发 `carbon-atlas-cds3001.zip`（不含 .git）到微信群/网盘；组员解压后看 `README.md`。
- 但这样没有版本历史/在线预览。

## 公开 vs 私有
- **公开**：组员只要链接就能看（推荐，最快）。
- **私有**：需要邀请组员 GitHub 用户名；课程内容不含密码，公开一般也安全。
- 仓库里 **没有** 真实 MySQL 密码（`code/app.py` 用 `DB_PASSWORD` 环境变量/占位符）；没有原始 CSV（太大，按 Part 1 说明自行下载）。

## 想让 Lead 帮你推？
把「GitHub 空仓库地址 + 允许本机 git 推送」告诉 Lead（例如你先在终端里 `git push` 一次完成登录），Lead 就能代推后续 commits。

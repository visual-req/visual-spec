# 多 AI 平台安装指南

推荐使用 skills.sh 的官方安装器（skills CLI）进行安装：同一套命令可面向不同 AI 平台（Trae / Claude Code / Cursor / GitHub Copilot 等）把 Skill 安装到对应的 skills 目录。

## 方式一：skills.sh（推荐）

安装器会自动检测本机支持的 agent，并提示选择安装位置与范围（项目级或全局）。

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill
```

指定安装到某个 AI 平台（示例）：

```bash
# Trae（项目级）
npx skills add visual-req/visual-spec --skill visual-spec-skill -a trae

# Claude Code（项目级）
npx skills add visual-req/visual-spec --skill visual-spec-skill -a claude-code

# Cursor（项目级）
npx skills add visual-req/visual-spec --skill visual-spec-skill -a cursor

# GitHub Copilot（项目级）
npx skills add visual-req/visual-spec --skill visual-spec-skill -a github-copilot
```

全局安装（对当前用户所有项目生效）：

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill -g
```

查看该仓库包含的 skills：

```bash
npx skills add visual-req/visual-spec --list
```

## 方式二：npm + vspec（适合 Trae/自定义目录）

全局安装：

```bash
npm install -g visual-spec@latest
```

默认安装到当前目录的 `.trae/skills/visual-spec-skill`：

```bash
vspec --force
```

安装到自定义 skills 目录（传入 skills 目录，脚本会自动追加 `visual-spec-skill/`）：

```bash
vspec --target-skills-dir /path/to/skills --force
```

或指定完整目标目录（包含 `visual-spec-skill`）：

```bash
vspec --target-skill-dir /path/to/skills/visual-spec-skill --force
```

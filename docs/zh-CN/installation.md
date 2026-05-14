## 安装到支持 Skill 的 AI 编辑器

[English](../en-US/installation.md) | [中文](../zh-CN/installation.md) | [日本語](../ja-JP/installation.md)

推荐使用 skills.sh 的官方安装器（skills CLI）安装到支持 Skill 的 AI 编辑器（Trae / Qwen / Kiro 等）。安装器会自动识别可用的 agent，并把 `visual-spec` 安装到对应的 `skills/` 目录。

### 前置条件

- Node.js >= 14

### 安装/更新（推荐：skills.sh）

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

### 备选：`vspec` CLI（手动指定目标目录）

如果你希望绕过 skills.sh 安装器，直接安装到某个指定目录，可以使用内置 CLI：

```bash
npx visual-spec --help
npx visual-spec install --target /path/to/your/project --force
```

默认安装路径为：`<project>/.trae/skills/visual-spec`。

### 下一步

- 快速开始：`getting-started.md`
- 多 AI 平台安装指南：`ai-platform-installation.md`

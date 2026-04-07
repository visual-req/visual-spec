## 安装到支持 Skill 的 AI 编辑器

本包使用脚本把内置的 Skill 目录复制到你的 AI 编辑器配置目录（Trae / Qwen / Kiro 等）。不同编辑器的配置路径可能不同，但安装逻辑一致：把 `visual-spec-skill` 安装到目标目录的 `skills/` 下。

### 前置条件

- Node.js >= 14

### 安装/更新（npm）

```bash
npm install -g visual-spec@latest
```

### 安装/更新（pnpm）

```bash
pnpm add -g visual-spec@latest
```

### 安装/更新（yarn）

Yarn Classic：

```bash
yarn global add visual-spec@latest
```

Yarn Berry（v2+）：

```bash
yarn dlx -p visual-spec@latest vspec
```

### 下一步

- 快速开始：`getting-started.md`

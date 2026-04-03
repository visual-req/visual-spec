## 安装到支持 Skill 的 AI 编辑器

本包通过脚本把内置的 Skill 目录复制到你的 AI 编辑器配置目录下（Trae/Qwen/Kiro 等）。不同编辑器的“配置目录”位置可能不同，但安装逻辑一致：把 `starter-skill` 安装到对应的 `skills/` 目录下。

### 前置条件

- Node.js >= 14

### 安装/更新（npm）

```bash
npm install -g visual-spec
```

### 安装/更新（pnpm）

```bash
pnpm add -g visual-spec
```

### 安装/更新（yarn）

Yarn Classic：

```bash
yarn global add visual-spec
```

Yarn Berry（v2+）：

```bash
yarn dlx -p visual-spec vreq-skill
```

### 下一步

- 快速上手指南：`docs/getting-started.md`

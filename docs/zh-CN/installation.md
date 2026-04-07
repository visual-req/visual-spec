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

### 指定安装目录（`--target-skills-dir`）

默认情况下，安装脚本会把 Skill 安装到当前目录的 `.trae/skills/visual-spec-skill`。如果你需要安装到自定义的 `skills/` 目录（例如统一放在某个编辑器配置目录），可以在安装后执行：

```bash
vspec --target-skills-dir /path/to/skills --force
```

说明：
- `--target-skills-dir` 传入的是“skills 目录”，脚本会自动追加子目录 `visual-spec-skill/`
- 你也可以使用 `--target-skill-dir` 传入完整目标目录（包含 `visual-spec-skill`）：

```bash
vspec --target-skill-dir /path/to/skills/visual-spec-skill --force
```

### 下一步

- 快速开始：`getting-started.md`

## Troubleshooting（常见问题与排障）

### 编辑器里看不到 [`/vspec:*`](../../README.md#commands) 命令

- 确认 skill 已安装到编辑器读取的 skills 目录。
- 以 Trae 为例，默认通常在项目目录下：`.trae/skills/visual-spec/`。
- 重新安装（覆盖更新）：

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

或使用内置 CLI（显式指定目标目录）：

```bash
npx visual-spec install --target /path/to/your/project --force
```

### 已安装但仍不可用

- 检查 Node.js 版本：Node.js >= 14
- 确认编辑器已开启 Skill 能力，并且正在读取正确的 skills 目录
- 用 dry-run 检查最终会安装到哪里（不写入文件）：

```bash
npx visual-spec --dry-run --target /path/to/your/project
```

### 安装到错误目录了

- 删除错误安装的目录，然后在正确项目目录重新安装：
  - 删除：`<project>/.trae/skills/visual-spec/`
  - 安装：`npx visual-spec install --target <project> --force`

### 产物输出到哪里？

- 产物默认输出到 `/specs/`（models、prototypes、details、qc report、plan）。
- `docs/` 用于存放业务输入材料与修订指令（refine）。

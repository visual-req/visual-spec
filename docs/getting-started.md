## Getting Started

本项目提供一组以 `/vspec:*` 命令驱动的 Skill，用于把原始需求逐步产出为规格、模型、原型、细节、验收用例、测试与集成实现。

### 1. 安装

先安装 npm 包，再把 Skill 写入到你的 AI 编辑器配置目录：

- 安装与验证：`docs/installation.md`

最常用方式（npm）：

```bash
npm install -g visual-spec
vspec --force --target "$HOME"
```

### 2. 推荐工作流

- 需求初版：`/vspec:new`
  - 执行过程中会生成待确认问题清单（`/specs/background/questions.md`）
  - 需要把业务答案补充到该文件后再继续后续流程
- 合并问答并修订生效需求：`/vspec:refine-q`
- 快速验证（模型 + 原型）：`/vspec:verify`
- 细节拆解：`/vspec:detail`
- 验收用例：`/vspec:accept`
- 集成实现：`/vspec:impl`
- 自动化测试：`/vspec:test`
- 变更响应：`/vspec:change`
- 升级改造（从旧系统材料继承）：`/vspec:upgrade`

### 3. 关键目录

- `/docs/`：材料归档（legacy/current/change/refine/templates/texts/assets）
- `/specs/`：产物输出（background/details/models/prototypes/acceptance 等）
- `/scheme.yaml`：技术栈与包管理器选择（原型与实现必须严格按此执行）

目录结构约定：

- `docs/structure.md`

下一步：

- 先阅读 `docs/structure.md`，确认材料目录与产物输出目录位置

### 4. 常见场景

#### 需求修订（refine）

- 把修订材料放到 `/docs/refine/`
- 要求：必须已有 `/specs/details/` 内容，否则 refine 不执行
- 运行：`/vspec:refine`
- 结果：追加更新 `/specs/background/original.md`，并同步更新受影响的 `/specs/details/` 与 `/specs/prototypes/`

#### 需求变更（change）

- 把变更材料放到 `/docs/change/`（可选 `file_list.md`）
- 运行：`/vspec:change`
- 结果：做影响分析并更新产物（优先更新 `/specs/details/<module_slug>/`），并更新变更日志

#### 升级改造（upgrade）

- 在 `/docs/current/file_list.md` 列出输入材料（旧系统在 `/docs/legacy/`，新增在 `/docs/current/`）
- 运行：`/vspec:upgrade`
- 结果：生成/更新 `/specs/`，并同步技术规格到 `/scheme.yaml`

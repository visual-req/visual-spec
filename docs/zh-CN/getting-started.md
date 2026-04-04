## 快速开始

本包提供一套由 `/vspec:*` 命令驱动的 Skill 工作流，用于把原始需求转成可评审的交付产物：规格、数据模型、可运行原型、详细设计、验收用例、测试与集成实现输入。

### 1. 安装

先全局安装 npm 包，再把 Skill 安装到 AI 编辑器的配置目录：

- 安装与校验：`installation.md`

安装/更新（npm）：

```bash
npm install -g visual-spec
```

安装/更新（pnpm）：

```bash
pnpm add -g visual-spec
```

安装/更新（yarn）：

Yarn Classic：

```bash
yarn global add visual-spec
```

Yarn Berry（v2+）：

```bash
yarn dlx -p visual-spec vspec
```

### 2. 推荐流程

- 初始规格：`/vspec:new`
  - 执行过程中会生成开放问题清单（`/specs/background/questions.md`）
  - 在继续流程前，把业务答案填写到该文件
- 合并 Q&A 到需求口径：`/vspec:refine-q`
- 详细规格：`/vspec:detail`
- 快速验证（模型 + 原型）：`/vspec:verify`（要求 `/specs/details/` 非空）
- 验收用例：`/vspec:accept`
- 集成实现：`/vspec:impl`
- 自动化测试：`/vspec:test`
- 变更处理：`/vspec:change`
- 升级/重构（继承遗留材料）：`/vspec:upgrade`

### 3. 关键目录

- `/docs/`：输入归档（legacy/current/change/refine/templates/texts/assets）
- `/specs/`：生成产物（background/details/models/prototypes/acceptance 等）
- `/scheme.yaml`：技术栈与包管理器选择（原型与实现必须遵循）

目录结构参考：

- `structure.md`

下一步：

- 阅读 `structure.md`，确认输入放在哪里、输出会生成到哪里

### 4. 常见场景

#### 补充/澄清（`refine`）

- 把补充材料放到 `/docs/refine/`
- 前置条件：`/specs/details/` 必须存在且非空，否则 `refine` 不执行
- 运行：`/vspec:refine`
- 结果：向 `/specs/background/original.md` 追加更新，并同步更新受影响的 `/specs/details/` 与 `/specs/prototypes/`

#### 变更（`change`）

- 把变更材料放到 `/docs/change/`（可选 `file_list.md`）
- 运行：`/vspec:change`
- 结果：做影响分析并更新产物（优先 `/specs/details/<module_slug>/`），同时更新变更日志

#### 升级/重构（`upgrade`）

- 在 `/docs/current/file_list.md` 中列出输入材料（遗留系统在 `/docs/legacy/`，新增输入在 `/docs/current/`）
- 运行：`/vspec:upgrade`
- 结果：生成/更新 `/specs/`，并把技术选型同步到 `/scheme.yaml`

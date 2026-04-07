## 快速开始

本包提供一套由 `/vspec:*` 命令驱动的 Skill 工作流，用于把原始需求转成可评审的交付产物：规格、数据模型、可运行原型、详细设计、验收用例、测试与集成实现输入。

### 1. 安装

把 Skill 安装到 AI 编辑器的配置目录：

- 安装与校验：`installation.md`

安装/更新（skills.sh）：

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill
```

### 2. 推荐流程

- 初始规格：`/vspec:new`
  - 执行中会先生成需求口径文件（`/specs/background/original.md`），并在该步骤提出若干澄清问题
  - 你需要先在对话中回答这些问题，然后输入“继续”才能完成 `/vspec:new` 全流程（这些澄清回答不写入 `questions.md`）
  - 执行过程中还会生成开放问题清单（`/specs/background/questions.md`），用于后续合并
- 合并 Q&A 到最新口径：`/vspec:refine-q`（把 `/specs/background/questions.md` 中已回答条目合并回 `original.md`，形成可追溯的口径演进）
- 质量检查：`/vspec:qc`（对已生成的 `/specs/` 产物做不符合项检查，输出 `/specs/qc_report.md`，用于在进入补充/实现前先补齐质量问题）
- 详细规格：`/vspec:detail`（遍历所有 functions，生成 RBAC、数据权限、交互、校验、状态机等细节产物）
- 快速验证（模型 + 原型）：`/vspec:verify`（基于 functions + details + models 生成可运行原型；要求 `/specs/details/` 非空）
- 验收用例：`/vspec:accept`（把关键场景转成可执行的验收点/检查表）
- 集成实现：`/vspec:impl`（生成后端/前端的实现输入与工程骨架约束，包含模型/Service/Repository/异常等）
- 自动化测试：`/vspec:append-test`（生成可落地的测试计划与自动化用例骨架）
- 升级/重构（继承遗留材料）：`/vspec:upgrade`（把 legacy/current 材料归一成新的 specs 与选型）

### 3. 关键目录

- `/docs/`：输入归档（legacy/current/refine/templates/texts/assets）
- `/specs/`：生成产物（background/details/models/prototypes/acceptance 等）
- `/scheme.yaml`：技术栈与包管理器选择（原型与实现必须遵循）

目录结构参考：

- `structure.md`

下一步：

- 阅读 `structure.md`，确认输入放在哪里、输出会生成到哪里

### 4. 常见场景

#### 补充/澄清（`refine`）

- 把补充材料写到 `/docs/refine/refine.md`（优先使用该文件作为入口；如有多文件再配合目录内其他文件）
- 前置条件：`/specs/details/` 必须存在且非空，否则 `refine` 不执行
- 运行：`/vspec:refine`
- 结果：向 `/specs/background/original.md` 追加更新，并同步更新受影响的 `/specs/details/` 与 `/specs/prototypes/`

#### 升级/重构（`upgrade`）

- 在 `/docs/current/file_list.md` 中列出输入材料（遗留系统在 `/docs/legacy/`，新增输入在 `/docs/current/`）
- 运行：`/vspec:upgrade`
- 结果：生成/更新 `/specs/`，并把技术选型同步到 `/scheme.yaml`

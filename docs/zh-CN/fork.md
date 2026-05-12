## Fork 后如何定制

本仓库的默认行为适用于通用需求分析与交付场景。若你 fork 本仓库用于某个行业/领域或团队内部落地，建议按以下方式进行定制，以便让 `/vspec:*` 输出更贴合你的组织规范。

### 1) 增加领域/行业质量规范（推荐）

在你的项目根目录新增：

- `domain_quality_standard.md`

用途：
- 用于补充行业/领域特有的质量检查点（例如：医疗/金融/教育/政务等的合规、审计、留存、数据口径约束）
- 执行 `/vspec:qc` 时会同时扫描：
  - 内置标准：`skills/visual-spec/prompts/vspec_qc/quality_standard.md`
  - 领域标准：`domain_quality_standard.md`
  - 项目标准：`quality_standard.md`（如存在，优先级最高）

建议内容结构：
- 以“检查点 + 判定口径 + 常见错误 + 修复建议”的形式写规则
- 对需要落地到具体产物的规则，明确对应文件路径（例如 `/specs/background/original.md`、`/specs/models/*.md`、`/specs/details/**`）

### 2) 定制标准估算基准（推荐）

估算基准位于：

- `skills/visual-spec/prompts/vspec_plan/estimate.md`

该文件内置了两张“供参考的标准表”（作为团队估算口径基线，fork 后可改）：
- “标准估值表（Story Points 标尺）”
- “标准工作项估值参考表”（CRUD、导入导出、审批/状态机、RBAC、数据权限、对接、定时任务等）

建议做法：
- 按你的团队效率、代码生成比例、测试强度、上线流程，把 SP 与典型人天区间调整为更符合现实的数据
- 对你们的高频领域能力补充工作项类型（例如：工单、报表、支付、内容管理、配置发布等）

### 3) 复用与维护“错题本”

内置质量规范来自：

- `skills/visual-spec/prompts/vspec_qc/需求分析错题本.xlsx`（原始错题本）
- `skills/visual-spec/prompts/vspec_qc/quality_standard.md`（从错题本转写后的可扫描规范）

建议：
- 你可以继续维护自己的错题本，并将可复用的检查点沉淀到 `domain_quality_standard.md`

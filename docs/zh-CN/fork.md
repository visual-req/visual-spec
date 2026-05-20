## Fork 后如何定制

[English](../en-US/fork.md) | [中文](../zh-CN/fork.md) | [日本語](../ja-JP/fork.md)

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

估算标准值以 JSON 形式存放：

- `skills/visual-spec/prompts/vspec_plan/estimation_standards.json`

阅读器（单文件 HTML，支持中/英/日切换）：

- `skills/visual-spec/prompts/vspec_plan/estimation_standards_reader.html`

`/vspec:plan` 的估算阶段会读取该 JSON，作为统一的 Story Points 口径（仅允许 `0/0.5/1/2/3/5/8/13`）。

如何扩展/修订 JSON（fork 后）：
- 保持 `allowedStoryPoints` 不变；如需改变点数集合，必须同步调整估算策略与团队流程，否则会造成“点数漂移”
- 在 `scalePoints` 中调整每个 SP 的语义（范围/描述），用于统一对齐“点数代表什么”
- 在 `workItemBenchmarks` 中新增你们的高频工作项类型（建议用稳定的 `key`），并补齐 `en/zh-CN/ja` 三语文案，避免跨语言阅读时内容错配
- 建议同步更新 `version` 与 `updatedAt`，便于审计与回溯

### 3) 复用与维护“错题本”

内置质量规范来自：

- `skills/visual-spec/prompts/vspec_qc/需求分析错题本.xlsx`（原始错题本）
- `skills/visual-spec/prompts/vspec_qc/quality_standard.md`（从错题本转写后的可扫描规范）

建议：
- 你可以继续维护自己的错题本，并将可复用的检查点沉淀到 `domain_quality_standard.md`

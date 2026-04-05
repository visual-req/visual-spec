---
name: "visual-spec-skill"
description: "将原始需求分析为可评审的视觉规格，并生成相关产物。当用户运行 /vspec:new 进行分析或运行 /vspec:verify 生成模型与原型时调用。"
---

# Visual Spec Skill（中文）

基于用户输入分析视觉规格，把简短的业务请求转化为结构化的需求输出。

## 何时使用

在以下情况调用本 Skill：
- 业务侧给出的需求描述非常简略。
- 用户运行 `/vspec:new` 开始新的需求分析流程。

## 本 Skill 定义的内容

- 使用“场景驱动拆解”的方式补齐细节。
- 设计数据模型。
- 基于补齐后的细节生成 UI 原型。
- 以可视化/结构化形式生成业务逻辑细节。

## Commands

### `/vspec:new`

用于创建一轮新的需求分析会话。

流程：
0. 确保 `/docs/` 存在，并确保子目录存在：
   - `/docs/legacy/`
   - `/docs/current/`
   - `/docs/change/`
   - `/docs/refine/`
0.5 尽早创建可编辑的项目约束文件，便于用户提前调整（若已存在则不得覆盖）：
   - 若缺失则创建 `/scheme.yaml`（包含原型选栈 + catalog）
   - 若缺失则创建 `/prototype_ui_convention.md`（与 `/scheme.yaml` 同级）
1. 提示用户输入原始需求。
2. 当用户按下回车，将输入视为原始需求来源。
3. 加载提示词文件 `prompts/vspec_new/background.md`。
4. 使用该提示词分析需求并扩展业务背景。
5. 将原始需求与背景分析写入 `/specs/background/original.md`。
6. 提示用户回答 `待确认问题` 章节中的问题。
7. 用户回复后，加载 `prompts/vspec_new/stakeholders.md` 分析干系人。
8. 将干系人结果写入 `/specs/background/stakeholder.md`（markdown 表格）。
9. 加载 `prompts/vspec_new/roles.md` 分析系统用户角色（直接用户）及其工作任务。
10. 将角色结果写入 `/specs/background/roles.md`。
11. 加载 `prompts/vspec_new/terms.md` 抽取关键术语与定义。
12. 将术语结果写入 `/specs/background/terms.md`（markdown 表格）。
13. 加载 `prompts/vspec_new/flows.md` 分析业务流程并生成 PlantUML 泳道图。
14. 将图写入 `/specs/flows/*.puml`。
15. 加载 `prompts/vspec_new/scenarios.md` 按节点组合枚举业务场景。
16. 将场景结果写入 `/specs/background/scenarios.md`（markdown 表格）。
17. 加载 `prompts/vspec_new/details_pre_post.md` 创建按节点拆分的详情目录，并为每个节点生成 `pre_post.md`。
18. 加载 `prompts/vspec_new/details_constraints.md` 为每个节点生成 `constraints.md`。
19. 加载 `prompts/vspec_new/details_variations.md` 为每个节点生成 `variations.md`。
20. 加载 `prompts/vspec_new/details_boundaries.md` 为每个节点生成 `boundaries.md`。
21. 加载 `prompts/vspec_new/details_symmetry.md` 为每个节点生成 `symmetry.md`。
22. 确保按节点拆分的输出都写到 `/specs/background/scenario_details/`。
23. 加载 `prompts/vspec_new/dependencies.md` 分析外部依赖系统。
24. 将依赖结果写入 `/specs/background/dependencies.md`。
25. 加载 `prompts/vspec_new/functions.md` 生成按模块与外部依赖系统分组的功能/特性清单。
26. 将功能清单写入 `/specs/functions/`。
27. 加载 `prompts/vspec_new/questions.md` 生成问题清单与所需业务材料清单。
28. 将问题清单写入 `/specs/background/questions.md`（markdown 列表）。
29. 加载 `prompts/harness/post_new_verify.md` 验证 functions 与 scenario_details 是否完备（登录/配置/主数据维护/审批等）。若输出了问题列表，则提示问题并立即结束。
30. 返回结构化分析结果，并进入下一步需求设计流程。

### `/vspec:refine`

用于基于 `/docs/refine/` 下的补充/澄清材料，或基于命令参数提供的一个/多个输入文件或目录，对需求进行补充与更新。

流程：
0. 确保 `/specs/details/` 存在且非空；若缺失则停止并提示用户先运行 `/vspec:detail`。
1. 读取 refine 输入：
   - 若命令参数提供了路径，将其视为 refine 输入源（文件/目录）。
   - 否则读取 `/docs/refine/`（若存在优先读 `/docs/refine/file_list.md`；否则按文件名顺序读取）。
2. 若 `prompts/vspec_refine/refine.md` 不存在：立即结束，不执行任何写入。
3. 加载 `prompts/vspec_refine/refine.md` 应用补充信息、更新需求口径并同步更新受影响的产物。
4. 将 refine 结果追加到 `/specs/background/original.md`，并更新受影响的 `/specs/details/` 与 `/specs/prototypes/`。

### `/vspec:refine-q`

用于基于“已回答的问题”补充与更新需求。

流程：
1. 若 `/specs/background/questions.md` 不存在：立即结束，不执行任何写入。
2. 若 `/specs/background/questions.md` 中不存在待回答的问题：立即结束，不执行任何写入。
3. 读取 `/specs/background/questions.md` 并选择已回答项。
4. 加载 `prompts/vspec_refine/refine_q.md` 将答案合并进最新口径。
5. 将结果追加到 `/specs/background/original.md`。
6. 更新 `/specs/background/questions.md`，标记本次运行中已视为回答的条目：
   - 用 `<mark>...</mark>` 包裹 `回答` 与 `状态`，以高亮已回答项。

### `/vspec:detail`

用于基于功能清单展开需求细节。

流程：
1. 读取 `/specs/functions/*` 中的功能清单。
   - 必须遍历 `/specs/functions/` 目录下所有文件的每一行功能（不仅是 core.md），避免遗漏任何模块/外部系统相关功能点。
2. 尽可能读取可用的上下文产物：`/specs/background/*`、`/specs/flows/*.puml`、`/specs/background/scenario_details/`、`/specs/background/roles.md`，以及已有的 `/specs/models/*.md`（若存在）。
3. 对每个功能（页面或非页面任务），先判断哪些详情产物真正涉及，再只生成涉及的部分；对不涉及的部分不得生成空文档。
   - 覆盖性要求（必须）：对遍历到的每个功能点，必须至少产出 `rbac.md` 与 `data_permission.md`（按规则写入对应路径）；若因信息不足无法产出，必须输出可见错误并停止，而不是静默跳过。
   - 始终生成基础文档：
     - `rbac.md`：RBAC 权限下沉到页面区域与控件级。
     - `data_permission.md`：数据权限规则与范围。
   - 仅页面类功能生成：
     - `page_load.md`：页面加载逻辑。
      - `interaction.md`：页面交互逻辑。
     - `validation_matrix.md`：矩阵形式的校验逻辑（仅提交类页面/动作；若页面无 submit/save/approve/reject/cancel/change 等动作则跳过）。
     - `post_submit_check.md`：提交后检查（若页面存在提交）。
     - `post_submit_processing.md`：提交后处理（若页面存在提交）。
     - `post_submit_navigation.md`：提交后返回与跳转（若页面存在提交）。
   - 条件生成（仅当该功能的逻辑/场景/模型/依赖涉及时才生成）：
     - `logging_matrix.md`：操作/审计日志（仅在业务需要保留变更历史、合规审计或不可抵赖时生成，否则跳过）。
     - `decision_matrix.md`：决策矩阵（用于状态机下各状态/角色的操作可用性）。
     - `notification_matrix.md`：通知（存在通知需求时生成）。
     - `mq.md`：MQ topic/event/消息 schema/可靠性细节（存在异步事件、队列或跨系统事件时生成）。
     - `file_import.md`：导入（存在导入入口/需求时生成）。
     - `file_export.md`：导出（存在导出入口/需求时生成）。
     - `formula.md`：计算公式与指标语义（存在计算/指标时生成）。
     - `expression_tree.md`：表达式树（HTML）（存在多层嵌套分支逻辑时生成）。
     - `code_rules.md`：编号/编码生成规则（存在编码生成时生成）。
     - `judgemental_matrix.md`：判定矩阵（2+ 因素共同决定结果的多因子分支时生成）。
   - 模块级（每模块最多生成一次，且仅当涉及时生成）：
     - `timeline.md`：时间轴（HTML）用于整体流程影响分析（存在跨较长时间跨度影响决策的逻辑，如生效/失效、截止期、宽限期、跨天规则等时生成）。
      - `state_machine.md`：状态列表 + 迁移 + PlantUML 状态图（模块整体，不按功能拆分）。
     - `nfp.md`：模块非功能需求总结（模块整体，不按功能拆分）。
     - `cron_job.md`：模块定时任务总结（模块整体，不按功能拆分）。
4. 仅写入生成的（涉及的）详情文档：
   - 单功能：`/specs/details/<module_slug>/<logic_type>/<function_slug>.(md|html)`
   - 模块级：`/specs/details/<module_slug>/<logic_type>/<module_slug>.(md|html)`

### `/vspec:verify`

用于生成模型与可运行原型，用于快速验证与评审。

流程：
0. 确保 `/specs/details/` 存在且非空；若缺失则立即停止并提示前置条件：“请先执行 /vspec:detail 生成 /specs/details/，再执行 /vspec:verify”。
1. 若 `/specs/background/questions.md` 存在且仍有未回答的问题，先要求用户回答再继续（允许逐条跳过，但必须保证不存在“未处理”的问题）。
2. 加载 `prompts/vspec_verify/model.md` 生成数据模型。
3. 将模型文件写入 `/specs/models/*.md`。
4. 基于 functions/details/models/roles 生成可运行的页面原型；原型技术栈由 `/scheme.yaml` 选择（若缺失则按默认值自动创建）。
   - 加载 `prompts/vspec_verify/prototype.md` 执行原型生成规则（必须遵循 `scheme.yaml` 技术栈；禁止只生成 html-only）。
5. 将原型工程写入 `/specs/prototypes/`。
6. 加载 `prompts/vspec_verify/validation.md` 生成场景验证网页。
7. 将验证页面写入 `/specs/prototypes/`，并提供 `scenario.html` 作为访问入口。
8. 加载 `prompts/harness/post_verify_verify.md` 检查原型是否覆盖关键约束（移动端/审批/CRUD/布局/登录/RBAC 等）。若输出了问题列表，则提示问题并立即结束。

### `/vspec:qc`

用于对 `/specs/` 下生成的需求产物进行质量检查。

流程：
1. 读取内置标准 `prompts/vspec_qc/quality_standard.md`。
2. 若项目 `qc/` 下存在“需求质量错误簿”，则据此生成/更新项目根目录的 `quality_standard.md`。
3. 若项目根目录存在 `quality_standard.md`，则将其作为补充/覆盖标准合并。
4. 加载 `prompts/vspec_qc/qc.md` 生成不符合项清单。
5. 将报告写入 `/specs/qc_report.md`。

### `/vspec:accept`

用于生成验收测试用例。

流程：
1. 读取 `/specs/functions/*`、`/specs/background/scenarios.md`、`/specs/background/scenario_details/`、`/specs/background/roles.md`、`/specs/models/*.md`。
2. 加载 `prompts/vspec_accept/accept.md` 生成验收用例，覆盖主流程、异常、边界、权限与数据范围。
3. 将结果写入 `/specs/acceptance/`（按功能建子目录），并生成 `/specs/acceptance/index.md` 索引。

### `/vspec:test`

用于基于验收用例与规格生成自动化测试代码。

流程：
1. 读取 `/specs/acceptance/`、`/specs/functions/*`、`/specs/details/`，并识别仓库中已有的测试框架。
2. 加载 `prompts/vspec_test/test.md`，按既有框架与约定生成自动化测试。
3. 将测试代码写入项目测试目录（若不存在标准目录则写入 `/tests/`），并确保能通过已有脚本运行。

### `/vspec:impl`

用于基于 specs 生成前后端集成实现代码。

流程：
1. 读取 `/specs/functions/*`、`/specs/details/`、`/specs/models/*.md`、`/specs/background/dependencies.md`，并识别当前前后端技术栈与代码约定。
2. 加载 `prompts/vspec_impl/implement.md` 并按后端优先实现：先在 `/specs/backend/` 生成可运行后端工程（health check + 核心 API/service），再在后端 API 可用后生成前端集成对接。
3. 仅允许在 `/specs/` 下写代码，并尽量保持差异最小且可审查；后端必须在 `/specs/backend/`，原型前端在 `/specs/prototypes/`。

### `/vspec:upgrade`

用于基于 `/docs/` 下材料（`/docs/legacy` 遗留系统、`/docs/current` 新输入）进行升级/改造分析，并按 `/vspec:new` 相同结构重新生成 `/specs/` 产物。

流程：
1. 确保 `/docs/current/file_list.md` 入口文件存在；若缺失则按模板生成。
2. 读取 `/docs/current/file_list.md`，再按顺序读取 `/docs/` 下列出的输入（通常 `/docs/legacy/*`、`/docs/current/*`，可选 `/docs/templates/*`、`/docs/texts/*`、`/docs/assets/*`）并抽取结构化信息（功能、依赖、UI 风格、角色/权限、技术规格）。
3. 若 `/specs/background/original.md` 已存在，则将其视为当前需求口径并作为 diff 基线（继承/新增/变更/废弃）。
4. 加载 `prompts/vspec_upgrade/upgrade.md`，按 `/vspec:new` 产物约定生成/更新 `/specs/`。
5. 将抽取到的技术规格同步到 `/scheme.yaml`，供 `/vspec:verify` 与 `/vspec:impl` 使用。

### `/vspec:change`

用于响应需求变更并更新受影响产物。

流程：
1. 读取 `/docs/change/` 下的变更输入（若存在优先用 `/docs/change/file_list.md` 作为入口；若仅存在 `/docs/changes/` 则兼容读取）。
2. 若目标仓库为 git 仓库，在写入任何更新前先创建变更前快照提交，保证 diff 可审查。
3. 读取已存在的 `/specs/` 产物（包括 `/specs/details/`、`/specs/models/`、`/specs/prototypes/`）。
4. 加载 `prompts/vspec_change/change.md` 做影响分析并更新受影响文档，优先更新 `/specs/details/<module_slug>/` 下的模块详情文档。
5. 写入更新后的产物，并将变更日志写入 `/specs/change_log.md`。

### `/vspec:plan`

用于把需求拆解为故事地图并进行估算与排期。

流程：
1. 读取 `/specs/functions/*`、`/specs/background/roles.md`、`/specs/background/scenarios.md`、`/specs/details/`、`/specs/background/dependencies.md`。
2. 加载 `prompts/vspec_plan/estimate.md`，按功能清单生成估算。
3. 将估算写入 `/specs/plan/plan_estimate.md`。
4. 加载 `prompts/vspec_plan/schedule.md` 生成排期与交付地图。
5. 将排期 HTML 写入 `/specs/plan/plan_schedule.html`。

## Prompt Files

- `prompts/vspec_new/background.md`：`/vspec:new` 接收原始需求后立即使用的提示词。
- `prompts/vspec_new/stakeholders.md`：用户回答 `待确认问题` 后生成 `/specs/background/stakeholder.md` 的提示词。
- `prompts/vspec_new/roles.md`：生成 `/specs/background/roles.md` 的提示词。
- `prompts/vspec_new/terms.md`：生成 `/specs/background/terms.md` 的提示词。
- `prompts/vspec_new/flows.md`：生成 `/specs/flows/*.puml` 的提示词。
- `prompts/vspec_new/scenarios.md`：生成 `/specs/background/scenarios.md` 的提示词。
- `prompts/vspec_new/details_pre_post.md`：生成按节点拆分的 `pre_post.md` 的提示词。
- `prompts/vspec_new/details_constraints.md`：生成按节点拆分的 `constraints.md` 的提示词。
- `prompts/vspec_new/details_variations.md`：生成按节点拆分的 `variations.md` 的提示词。
- `prompts/vspec_new/details_boundaries.md`：生成按节点拆分的 `boundaries.md` 的提示词。
- `prompts/vspec_new/details_symmetry.md`：生成按节点拆分的 `symmetry.md` 的提示词。
- `prompts/vspec_new/dependencies.md`：生成 `/specs/background/dependencies.md` 的提示词。
- `prompts/vspec_new/functions.md`：生成 `/specs/functions/` 的提示词。
- `prompts/vspec_new/questions.md`：生成 `/specs/background/questions.md` 的提示词。
- `prompts/vspec_refine/refine.md`：`/vspec:refine` 使用的提示词。
- `prompts/vspec_refine/refine_q.md`：`/vspec:refine-q` 使用的提示词。
- `prompts/vspec_verify/model.md`：生成 `/specs/models/*.md` 的提示词。
- `prompts/vspec_verify/prototype.md`：生成按选栈的可运行原型工程（`/specs/prototypes/`）的提示词（必须遵循 `scheme.yaml`）。
- `prompts/vspec_verify/validation.md`：生成 `scenario.html` 场景评审页的提示词。
- `prompts/vspec_detail/rbac.md`：生成 RBAC 详情的提示词。
- `prompts/vspec_detail/data_permission.md`：生成数据权限详情的提示词。
- `prompts/vspec_detail/page_load.md`：生成页面加载逻辑的提示词。
- `prompts/vspec_detail/interaction.md`：生成页面交互逻辑的提示词。
- `prompts/vspec_detail/timeline.md`：生成时间轴 HTML 的提示词。
- `prompts/vspec_detail/formula.md`：生成公式说明的提示词。
- `prompts/vspec_detail/expression_tree.md`：生成表达式树 HTML 的提示词。
- `prompts/vspec_detail/code_rules.md`：生成编号/编码规则的提示词。
- `prompts/vspec_detail/judgemental_matrix.md`：生成判定矩阵的提示词。
- `prompts/vspec_detail/validation_matrix.md`：生成校验矩阵的提示词。
- `prompts/vspec_detail/post_submit_check.md`：生成提交后检查的提示词。
- `prompts/vspec_detail/post_submit_processing.md`：生成提交后处理的提示词。
- `prompts/vspec_detail/post_submit_navigation.md`：生成提交后跳转规则的提示词。
- `prompts/vspec_detail/mq.md`：生成 MQ 设计的提示词。
- `prompts/vspec_detail/logging_matrix.md`：生成日志矩阵的提示词。
- `prompts/vspec_detail/notification_matrix.md`：生成通知矩阵的提示词。
- `prompts/vspec_detail/nfp.md`：生成非功能需求的提示词。
- `prompts/vspec_detail/file_import.md`：生成导入设计的提示词。
- `prompts/vspec_detail/file_export.md`：生成导出设计的提示词。
- `prompts/vspec_detail/cron_job.md`：生成定时任务设计的提示词。
- `prompts/vspec_accept/accept.md`：生成验收用例的提示词。
- `prompts/vspec_test/test.md`：生成自动化测试的提示词。
- `prompts/vspec_impl/implement.md`：生成前后端集成实现的提示词。
- `prompts/vspec_upgrade/upgrade.md`：生成升级/改造规格的提示词。
- `prompts/vspec_change/change.md`：处理变更的提示词。
- `prompts/vspec_plan/estimate.md`：生成估算的提示词。

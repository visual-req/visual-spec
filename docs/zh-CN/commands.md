## 命令总览

| 命令 | 作用 | 主要输入 | 主要输出 |
| --- | --- | --- | --- |
| `/vspec:new` | 从原始需求生成第一版规格产物 | 原始需求文本 + 交互式问答 | `/specs/`（original、stakeholders、roles、terms、flows、scenarios、scenario_details、dependencies、functions、questions）+ 初始化 `/docs/*` 输入归档目录 |
| `/vspec:refine` | 应用补充/澄清材料，并同步更新详情与原型 | `/docs/refine/*`（或命令参数）+ `/specs/background/original.md` + 前置条件 `/specs/details/` | 追加更新到 `/specs/background/original.md`（变更清单 + 最新口径）+ 更新受影响的 `/specs/details/` 与 `/specs/prototypes/` |
| `/vspec:refine-q` | 将已回答的问题合并回需求并形成新口径 | `/specs/background/original.md` + `/specs/background/questions.md` | 追加到 `/specs/background/original.md`（采纳项 + 变更清单 + 最新口径） |
| `/vspec:verify` | 快速验证：生成模型与可运行原型用于评审 | 现有 `/specs/` 产物 | `/specs/models/*.md`、`/specs/prototypes/`（按 `scheme.yaml` 选栈生成可运行原型 + `scenario.html` 评审页） |
| `/vspec:detail` | 展开到“可实现”的单功能详细规格 | `/specs/functions/*` + details/models/roles | `/specs/details/<function_slug>/*`（RBAC、交互、校验、日志、通知、MQ、导入导出、定时任务等） |
| `/vspec:accept` | 生成验收用例 | functions/scenarios/details/roles/models | `/specs/acceptance/<function_slug>/acceptance_cases.md`、`/specs/acceptance/index.md` |
| `/vspec:test` | 生成自动化测试代码 | 验收用例 + 仓库测试技术栈 | 写入既有测试目录或 `/tests/` |
| `/vspec:impl` | 生成后端 + 前端联调实现代码 | specs/details/models/dependencies | 写入集成实现代码（API 合同、后端、前端对接） |
| `/vspec:upgrade` | 基于遗留材料做升级/重构分析并生成新规格 | `/docs/current/file_list.md` + `/docs/legacy/*`（可选 templates/texts/assets）+ 既有 `/specs/background/original.md`（可选） | 生成/更新 `/specs/`（沿用 `/vspec:new` 结构）+ 同步技术选型到 `/scheme.yaml` |
| `/vspec:change` | 处理变更：影响分析并更新产物 | `/docs/change/*`（可选 file_list.md）+ 既有 `/specs/` | 更新受影响文件（优先 `/specs/details/<module_slug>/`）+ `/specs/change_log.md`（更新前需要 git 快照提交） |
| `/vspec:qc` | 对 `/specs/` 产物做质量检查 | 内置标准 + 可选 `quality_standard.md` + `/specs/` | `/specs/qc_report.md` |
| `/vspec:plan` | 估算与排期 | functions/roles/flows/dependencies/details | `/specs/plan/plan_estimate.md`、`/specs/plan/plan_schedule.html` |

## `/vspec:new`

- 适用场景：刚拿到需求且信息不完整，需要快速形成“可评审的共同语言”
- 关键输出：干系人、角色、术语、流程、场景、功能清单、开放问题
- 目录初始化：创建 `/docs/` 及其子目录（legacy/current/change/refine/templates/texts/assets）用于输入归档与后续命令使用

## `/vspec:refine`

- 适用场景：实现中出现新信息/澄清，需要更新需求口径并同步更新详情与原型，且保留可追溯性
- 输入：
  - 默认：`/docs/refine/`（优先 `/docs/refine/file_list.md`，否则按文件名顺序读取）
  - 可选：命令参数指定文件/目录（优先级更高）
- 前置条件：`/specs/details/` 必须存在且非空；否则不执行（避免上游变化但下游未同步）
- 关键输出：
  - 追加“变更清单 + 最新口径 + 影响分析与产物同步”到 `original.md` 末尾
  - 更新受影响的 `/specs/details/`（优先修改已有文件）与 `/specs/prototypes/`（尽量保持差异最小、可审查）

## `/vspec:refine-q`

- 适用场景：业务已在 `/specs/background/questions.md` 填写答案，需要合并回需求并形成新口径
- 关键输出：采纳的 Q&A 项 + 变更清单 + 最新口径

## `/vspec:verify`

- 适用场景：尽快验证数据结构与页面形态，降低沟通误差
- 关键输出：模型文件（实体拆分/关系/状态机等）、可运行原型、场景评审页
- UI 规范：生成或复用 `/prototype_ui_convention.md`（与 `/scheme.yaml` 同级），并以其作为唯一口径约束原型 UI 风格与交互
- Note：执行 `/vspec:verify` 之前务必先审核 `/specs/functions/*` 的功能清单，确保覆盖完整；否则原型与模型将仅基于现有 functions 生成，可能出现功能缺失。

## `/vspec:detail`

- 适用场景：在设计/实现前，需要把每个功能点展开到“可实现”的规格粒度
- 关键输出：RBAC 到控件级、数据权限、加载/交互/校验矩阵、提交后处理、日志/通知矩阵、MQ、导入导出、定时任务等

## `/vspec:accept`

- 适用场景：用“可执行用例”对齐交付与验收
- 关键输出：每功能点验收用例表，覆盖主流程、异常、边界、RBAC、数据权限

## `/vspec:test`

- 适用场景：将验收用例转化为可运行的自动化测试（E2E/API/单测）
- 关键输出：优先复用仓库现有测试框架与脚本，避免引入新依赖

## `/vspec:impl`

- 适用场景：把规格产物转成可运行的后端 + 前端联调实现
- 关键输出：API 合同、后端实现、前端页面与 API 对接、RBAC/状态机约束落地

## `/vspec:change`

- 适用场景：收到明确变更请求，需要可追溯的影响评估与更新
- 输入：从 `/docs/change/` 读取（可选 `/docs/change/file_list.md` 作为有序输入清单；兼容旧路径 `/docs/changes/`）
- 更新策略：优先更新受影响模块目录 `/specs/details/<module_slug>/`，并同步 models/functions/prototypes/acceptance 等
- 更新前快照：若目标仓库是 git 仓库，更新前先做一次快照提交，保证差异可审查
- 关键输出：结构化变更清单、影响分析表、变更日志以及对应产物更新

## `/vspec:upgrade`

- 适用场景：基于遗留系统材料做“升级/重构/迁移”分析，继承必要部分并生成新规格
- 入口清单：`/docs/current/file_list.md`（缺失时生成模板）用于列出输入文件、用途、提取要点、是否必须
- 输入范围：通常来自 `/docs/legacy/*` 与 `/docs/current/*`，也可组合 `/docs/templates/*`、`/docs/texts/*`、`/docs/assets/*`
- 关键输出：按 `/vspec:new` 的产物结构生成/更新 `/specs/`，并在功能清单中标注 继承/新增/调整/废弃
- 技术选型同步：从“系统技术规格”等输入中提取选型并写入 `/scheme.yaml`，供 `/vspec:verify` 与 `/vspec:impl` 使用

## `/vspec:plan`

- 适用场景：对齐交付节奏，通过故事地图拆解并产出排期
- 关键输出：故事拆解与估算（人日）、迭代计划、排期页面（HTML）

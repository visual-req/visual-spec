## 命令总览

| 命令 | 目的 | 主要输入 | 主要输出 |
| --- | --- | --- | --- |
| `/vspec:new` | 从原始需求生成基础规格产物 | 原始需求文本 + 交互问答 | `/specs/`（original、stakeholder、roles、terms、flows、scenarios、scenario_details、dependencies、functions、questions）+ 初始化 `/docs/*` 归档目录 |
| `/vspec:refine` | 基于修订材料修订需求，并同步更新细节与原型 | `/docs/refine/*`（或命令参数）+ `/specs/background/original.md`（基线）+ `/specs/details/`（前置条件） | 追加写入 `/specs/background/original.md`（变更清单 + Canonical）+ 更新受影响 `/specs/details/` 与 `/specs/prototypes/` |
| `/vspec:refine-q` | 基于 questions 的已回答内容修订需求 | `/specs/background/original.md` + `/specs/background/questions.md` | 追加写入 `/specs/background/original.md`（采纳条目 + 变更清单 + Canonical） |
| `/vspec:verify` | 生成模型与原型，用于快速验证 | `/specs/` 产物 | `/specs/models/*.md`、`/specs/prototypes/`（Vue + Ant Design Vue 原型、场景确认页 `scenario.html`） |
| `/vspec:detail` | 按功能点细化需求细节 | `/specs/functions/*` + 细节/模型/角色 | `/specs/details/<function_slug>/*`（权限/交互/校验/日志/通知/MQ/导入导出/定时任务等） |
| `/vspec:accept` | 生成验收测试用例 | 功能/场景/细节/角色/模型 | `/specs/acceptance/<function_slug>/acceptance_cases.md`、`/specs/acceptance/index.md` |
| `/vspec:test` | 生成自动化测试代码 | 验收用例 + 仓库既有测试框架 | 写入既有测试目录或 `/tests/` |
| `/vspec:impl` | 生成前后端集成代码 | 规格/细节/模型/依赖 | 写入仓库源码（API、后端实现、前端页面与集成） |
| `/vspec:upgrade` | 基于旧系统材料做升级改造分析并生成新规格 | `/docs/current/file_list.md` + `/docs/legacy/*`（可选 templates/texts/assets）+ 既有 `/specs/background/original.md`（如存在） | 按 `/vspec:new` 结构生成/更新 `/specs/` + 同步技术规格到 `/scheme.yaml` |
| `/vspec:change` | 基于变更材料做影响分析并更新产物 | `/docs/change/*`（可选 file_list.md）+ 现有产物 `/specs/` | 更新相关文件（优先 `/specs/details/<module_slug>/`）+ `/specs/change_log.md`（更新前需 git 快照提交） |
| `/vspec:qc` | 对 `/specs/` 产物做质量检查并输出不合格清单 | 内嵌标准 + 项目 `quality_standard.md`（可选） + `/specs/` | `/specs/qc_report.md` |
| `/vspec:plan` | 估算与排期 | 功能/角色/流程/依赖/细节 | `/specs/plan_estimate.md`、`/specs/plan_schedule.html` |

## `/vspec:new`

- 使用场景：需求刚拿到、信息不完整，需要快速形成统一语言与初版规格
- 输出重点：干系人/角色/术语/流程/场景/功能清单/待确认问题
- 目录初始化：会在项目根目录初始化 `/docs/` 及其子目录（legacy/current/change/refine/templates/texts/assets），用于材料归档与后续命令读取

## `/vspec:refine`

- 使用场景：需求在开发/细化过程中出现补充与修订，需要在保留可追溯的前提下，更新“当前生效需求”并同步更新细节与原型
- 输入来源：
  - 默认读取：`/docs/refine/`（优先 `/docs/refine/file_list.md`；否则按文件名顺序）
  - 可选：命令参数指定文件/目录（优先级更高）
- 前置条件：必须已存在且非空的 `/specs/details/`，否则 refine 不执行（避免只有上游需求变了、下游细节不跟导致产物失配）
- 输出重点：
  - 在 `original.md` 末尾追加“变更清单 + 当前生效需求（Canonical）+ 影响分析与产物更新”
  - 更新受影响的 `/specs/details/`（优先更新既有文件）与 `/specs/prototypes/`（最小可评审 diff）

## `/vspec:refine-q`

- 使用场景：业务已回答 `/specs/background/questions.md`，希望将已回答内容合并回需求并形成新的生效版本
- 输出重点：采纳的问答条目 + 变更清单 + 当前生效需求（Canonical）

## `/vspec:verify`

- 使用场景：希望尽快验证数据结构与页面形态，降低理解偏差
- 输出重点：数据模型文件（实体拆分）、可运行原型、场景确认页

## `/vspec:detail`

- 使用场景：进入方案设计/开发前，需要把“每个功能点”拆到可实现的细节级别
- 输出重点：RBAC 到控件级、数据权限、加载/交互/校验矩阵、提交后处理、日志/通知矩阵、MQ、导入/导出、定时任务

## `/vspec:accept`

- 使用场景：准备验收与交付对齐，形成可执行的用例集合
- 输出重点：按功能点组织的验收用例表，覆盖主流程/异常/边界/权限/数据权限

## `/vspec:test`

- 使用场景：需要把验收用例落地为可运行的自动化测试（E2E/API/单测）
- 输出重点：复用仓库既有测试框架与脚本，不引入新依赖

## `/vspec:impl`

- 使用场景：需要把规格产物转为真实可运行的前后端联调代码
- 输出重点：接口契约、后端实现、前端页面与 API 集成、权限与状态机落地

## `/vspec:change`

- 使用场景：需求发生明确变更，需要可追溯地更新产物并评估影响
- 输入来源：读取 `/docs/change/` 下材料（可选 `/docs/change/file_list.md` 作为入口按顺序读取；兼容旧路径 `/docs/changes/`）
- 更新策略：优先更新受影响模块的明细规格目录 `/specs/details/<module_slug>/`，并按需联动 models/functions/prototypes/acceptance
- 更新前快照：若目标仓库是 git 仓库，写入任何更新前必须先提交一次快照，便于查看本次变更 diff
- 输出重点：结构化变更清单、影响分析表、变更日志与对应产物更新

## `/vspec:upgrade`

- 使用场景：基于遗留系统材料做“升级改造/重构迁移”分析，从旧内容继承并生成新的规格产物
- 入口清单：`/docs/current/file_list.md`（不存在则先生成模板），用于列出输入文件及用途、提取要点、是否必须
- 输入范围：通常来自 `/docs/legacy/*` 与 `/docs/current/*`，可选结合 `/docs/templates/*`、`/docs/texts/*`、`/docs/assets/*`
- 输出重点：复用 `/vspec:new` 的产物结构生成/更新 `/specs/`，并在功能清单中标注“继承/新增/调整/废弃”
- 技术规格同步：从“系统技术规格”输入中抽取选型并写入 `/scheme.yaml`，用于后续 `/vspec:verify` 与 `/vspec:impl`

## `/vspec:plan`

- 使用场景：需要对齐交付节奏，按用户故事地图拆解并排期
- 输出重点：故事拆分与估算（人天）、迭代计划、HTML 用户故事地图

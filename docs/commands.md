## 命令总览

| 命令 | 目的 | 主要输入 | 主要输出 |
| --- | --- | --- | --- |
| `/vspec:new` | 从原始需求生成基础规格产物 | 原始需求文本 + 交互问答 | `/specs/`（original、stakeholder、roles、terms、flows、scenarios、scenario_details、dependencies、functions、questions） |
| `/vspec:refine` | 基于 refine.md 修订需求，形成新的生效版本 | `/specs/background/original.md` + `refine.md` | 追加写入 `/specs/background/original.md`（变更清单 + Canonical） |
| `/vspec:refine-q` | 基于 questions 的已回答内容修订需求 | `/specs/background/original.md` + `/specs/background/questions.md` | 追加写入 `/specs/background/original.md`（采纳条目 + 变更清单 + Canonical） |
| `/vspec:verify` | 生成模型与原型，用于快速验证 | `/specs/` 产物 | `/specs/models/*.md`、`/specs/prototypes/`（Vue + Ant Design Vue 原型、场景确认页 `scenario.html`） |
| `/vspec:proto-apply` | 仅生成/更新“申请”原型 | `/specs/functions/*` + roles + models | `/specs/prototypes/`（申请模块页面与工作台差异） |
| `/vspec:proto-approve` | 仅生成/更新“审批”原型 | `/specs/functions/*` + roles + models | `/specs/prototypes/`（审批模块页面与工作台差异） |
| `/vspec:proto-execute` | 仅生成/更新“执行”原型（含移动端） | `/specs/functions/*` + roles + models | `/specs/prototypes/`（执行模块页面与 `/m/*`） |
| `/vspec:proto-crud` | 仅生成/更新 CRUD 管理页原型 | `/specs/functions/*` + roles + models | `/specs/prototypes/`（配置/主数据类 CRUD 页面） |
| `/vspec:detail` | 按功能点细化需求细节 | `/specs/functions/*` + 细节/模型/角色 | `/specs/details/<function_slug>/*`（权限/交互/校验/日志/通知/MQ/导入导出/定时任务等） |
| `/vspec:accept` | 生成验收测试用例 | 功能/场景/细节/角色/模型 | `/specs/acceptance/<function_slug>/acceptance_cases.md`、`/specs/acceptance/index.md` |
| `/vspec:test` | 生成自动化测试代码 | 验收用例 + 仓库既有测试框架 | 写入既有测试目录或 `/tests/` |
| `/vspec:impl` | 生成前后端集成代码 | 规格/细节/模型/依赖 | 写入仓库源码（API、后端实现、前端页面与集成） |
| `/vspec:change` | 响应需求变更并更新产物 | 变更描述 + 现有产物 | 更新相关文件 + `/specs/change_log.md` |
| `/vspec:qc` | 对 `/specs/` 产物做质量检查并输出不合格清单 | 内嵌标准 + 项目 `quality_standard.md`（可选） + `/specs/` | `/specs/qc_report.md` |
| `/vspec:plan` | 估算与排期 | 功能/角色/流程/依赖/细节 | `/specs/plan_estimate.md`、`/specs/plan_schedule.html` |

## `/vspec:new`

- 使用场景：需求刚拿到、信息不完整，需要快速形成统一语言与初版规格
- 输出重点：干系人/角色/术语/流程/场景/功能清单/待确认问题

## `/vspec:refine`

- 使用场景：已有 `/specs/background/original.md`，希望用一份 `refine.md` 指令对需求做版本化修订
- 输出重点：在 `original.md` 末尾追加“变更清单 + 当前生效需求（Canonical）”

## `/vspec:refine-q`

- 使用场景：业务已回答 `/specs/background/questions.md`，希望将已回答内容合并回需求并形成新的生效版本
- 输出重点：采纳的问答条目 + 变更清单 + 当前生效需求（Canonical）

## `/vspec:verify`

- 使用场景：希望尽快验证数据结构与页面形态，降低理解偏差
- 输出重点：数据模型文件（实体拆分）、可运行原型、场景确认页

## 原型拆分命令（/vspec:proto-*)

- 使用场景：原型太大/太乱，希望按“申请/审批/执行/CRUD”分段生成，保证端分配与角色差异更可控
- 输出重点：在同一套 `/specs/prototypes/` 工程上做增量更新，仅聚焦对应模块的页面与路由

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

- 使用场景：需求发生变更，需要可追溯地更新产物并评估影响
- 输出重点：结构化变更清单、影响分析表、变更日志与对应产物更新

## `/vspec:plan`

- 使用场景：需要对齐交付节奏，按用户故事地图拆解并排期
- 输出重点：故事拆分与估算（人天）、迭代计划、HTML 用户故事地图

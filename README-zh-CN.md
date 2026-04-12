# 中文说明

本仓库提供一个“需求分析与交付助手”Skill。它提供一套由 `/vspec:*` 命令驱动的工作流，将原始需求转化为可评审的交付产物：规格、数据模型、可运行原型、详细设计、验收用例、测试与集成实现输入。

版本：0.1.9（2026-04-12）

## 概览

- 需求分析：生成背景、干系人、角色、术语、流程、场景、详情、依赖、功能清单与开放问题
- 方案验证：生成数据模型、可运行原型与场景评审页
- 详细设计：按功能生成 RBAC/数据权限/交互/校验/日志/通知/MQ/导入导出/定时任务 等规格
- 验收与测试：生成验收用例与自动化测试代码
- 集成实现：生成后端 + 前端集成实现代码（对齐仓库实际技术栈与约定）
- 规划：基于功能清单进行估算与排期（HTML 输出）

## 命令

- `/vspec:new`：生成基础规格产物（写入 `/specs/`）
- `/vspec:refine`：从 `/docs/refine/`（或命令参数）读取补充材料，更新 `/specs/details/` 与 `/specs/prototypes/`（需要已有 details）
- `/vspec:refine-q`：将 `questions.md` 中已回答项合并回需求，并更新 `/specs/background/original.md` 的最新口径
- `/vspec:detail`：生成单功能详细规格（写入 `/specs/details/`）
- `/vspec:verify`：生成数据模型与按 `/scheme.yaml` 选栈的可运行原型（写入 `/specs/models/`、`/specs/prototypes/`；要求 `/specs/details/` 非空）
- `/vspec:accept`：生成验收用例（写入 `/specs/acceptance/`）
- `/vspec:append-test`：生成自动化测试代码（写入仓库既有测试目录或 `/tests/`）
- `/vspec:impl`：生成后端 + 前端联调实现代码（写入 `/specs/`）
- `/vspec:upgrade`：基于 `/docs/` 下的遗留与新增输入做升级/重构分析，生成/更新 `/specs/`，并把技术选型同步到 `/scheme.yaml`
- `/vspec:qc`：对产物做质量检查并输出报告（写入 `/specs/qc_report.md`）
- `/vspec:plan`：生成估算与排期（写入 `/specs/plan/plan_estimate.md`、`/specs/plan/plan_schedule.html`）

## 目录结构

- `skills/visual-spec/SKILL.md`：Skill 定义与命令工作流
- `skills/visual-spec/prompts/`：各命令使用的提示词文件

## 版本与授权

- `prompts/harness/*`（运行后校验命令）为付费版（Pro）功能。
- Pro 版提供更广泛的质量检测能力（例如原型选栈/目录结构校验、点击无反应检测、移动端交互规范校验、价格格式校验、后端 MVC 与测试覆盖率校验等），需要付费开通。

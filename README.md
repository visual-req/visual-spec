本工程是一个需求分析与交付辅助 Skill，提供一组以 `/vspec:*` 命令驱动的流程，用于把原始需求逐步产出为规格、模型、原型、细节、验收用例、测试与集成实现所需的输入。

## 功能概览

- 需求分析：从原始描述生成背景、干系人、角色、术语、流程、场景、细节、依赖、功能清单与待确认问题
- 方案验证：生成数据模型、页面原型与场景确认页
- 细节梳理：按功能点输出权限/数据权限/交互/校验/日志/通知/MQ/导入导出/定时任务等规格
- 验收与测试：生成验收测试用例与自动化测试代码
- 集成开发：生成前后端集成代码（按仓库现有技术栈与约定）
- 变更响应：分析需求变更影响并更新产物，生成变更日志
- 排期规划：按功能清单输出估算与排期（HTML）

## 命令

- `/vspec:new`：生成基础规格产物（输出到 `/specs/`）
- `/vspec:refine`：读取 `/docs/refine/` 的修订材料（或命令参数），修订需求并同步更新 `/specs/details/` 与 `/specs/prototypes/`（需已有 details 才执行）
- `/vspec:refine-q`：基于 `questions.md` 的已回答内容修订需求内容，并更新 `/specs/background/original.md` 中的“当前生效需求”
- `/vspec:verify`：生成数据模型与 Vue + Ant Design Vue 原型（输出到 `/specs/models/`、`/specs/prototypes/`）
- `/vspec:detail`：按功能点生成细节规格（输出到 `/specs/details/`）
- `/vspec:accept`：生成验收测试用例（输出到 `/specs/acceptance/`）
- `/vspec:test`：生成自动化测试代码（写入仓库既有测试目录或 `/tests/`）
- `/vspec:impl`：生成前后端集成代码（只允许写入 `/specs/prototypes/` 原型工程内）
- `/vspec:upgrade`：从 `/docs/`（legacy/current/templates/texts/assets）读取旧系统与新增材料，升级改造并生成/更新 `/specs/`，同步技术规格到 `/scheme.yaml`
- `/vspec:change`：读取 `/docs/change/` 的变更材料，做影响分析并更新产物，输出 `/specs/change_log.md`（更新前需 git 快照提交）
- `/vspec:qc`：对 `/specs/` 产物进行质量检查并输出不合格清单（输出到 `/specs/qc_report.md`）
- `/vspec:plan`：估算与排期（输出到 `/specs/plan_estimate.md`、`/specs/plan_schedule.html`）

## 目录结构

- `skills/visual-spec-skill/SKILL.md`：Skill 定义与命令流程
- `skills/visual-spec-skill/prompts/`：各命令对应的提示词文件

# visual-spec（中文）

[English](README.md) | [中文](README-zh-CN.md) | [日本語](README-ja-JP.md)

本仓库提供一个“需求分析与交付助手”Skill：用一套 `/vspec:*` 命令驱动的工作流，把原始需求转换为可评审、可落地的交付产物（规格、数据模型、可运行原型、详细设计、验收用例、测试与集成实现输入）。

该 Skill 的开发初衷是把“需求澄清 → 方案设计 → 交付验证”流程标准化、可视化、可复用，减少沟通损耗与返工成本。整体能力范围以独立知识产权的“可视化需求分析”方法为基础进行设计：强调以流程/场景/角色/数据模型为主线，把需求拆解为可验证的结构化产物，并确保下游原型/细节/实现输入可持续迭代同步。

版本：0.1.13（2026-04-12）

## Quick Installation

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

Docs:
- [Installation](docs/en-US/installation.md)
- [Multi-agent installation](docs/en-US/ai-platform-installation.md)
 - Fork 定制指南：[docs/zh-CN/fork.md](docs/zh-CN/fork.md)

## 文档导览

| 文档 | 说明 | 链接 |
| --- | --- | --- |
| 快速开始 | 从安装到跑通一次完整工作流 | [docs/zh-CN/getting-started.md](docs/zh-CN/getting-started.md) |
| 命令说明 | `/vspec:*` 命令与输入输出 | [docs/zh-CN/commands.md](docs/zh-CN/commands.md) |
| 目录结构 | `/docs/`、`/specs/` 目录与产物结构 | [docs/zh-CN/structure.md](docs/zh-CN/structure.md) |
| 工作流图 | 可视化流程与关键产物 | [docs/zh-CN/workflows.md](docs/zh-CN/workflows.md) |
| 安装 | 安装与配置（英文） | [docs/en-US/installation.md](docs/en-US/installation.md) |
| Fork 定制 | Fork 后的定制指南 | [docs/zh-CN/fork.md](docs/zh-CN/fork.md) |

## 功能概览

- 需求分析：生成背景、干系人、角色、术语、流程、场景、详情、依赖、功能清单与开放问题
- 方案验证：生成数据模型、可运行原型与场景评审页
- 详细设计：按功能生成 RBAC/数据权限/交互/校验/日志/通知/MQ/导入导出/定时任务 等规格
- 验收与测试：生成验收用例与自动化测试代码
- 集成实现：生成后端 + 前端集成实现代码（对齐仓库实际技术栈与约定）
- 规划：基于功能清单进行估算与排期（HTML 输出）

## 命令一览

| 命令 | 用途 | 主要输入 | 主要输出 |
| --- | --- | --- | --- |
| `/vspec:new` | 生成基础规格产物 | 原始需求文本 +（可选）`/docs/current/*` | `/specs/`（background/functions/flows 等） |
| `/vspec:refine` | 按变更内容持续修订需求并同步下游产物 | `/docs/refine/refine.md` 或窗口粘贴变更或命令参数 | 更新 `/specs/background/original.md` + 同步更新 `/specs/details/`、`/specs/prototypes/`、已存在的 `/specs/backend/` |
| `/vspec:refine-q` | 合并已回答问题并更新最新口径 | `/specs/background/questions.md`（已回答项） | 更新 `/specs/background/original.md` 与 `questions.md` 标记 |
| `/vspec:detail` | 生成单功能详细规格 | `/specs/functions/*` + 背景/流程/场景/模型等 | `/specs/details/` |
| `/vspec:verify` | 生成数据模型与可运行原型 | `/scheme.yaml` + `/specs/details/` | `/specs/models/`、`/specs/prototypes/` |
| `/vspec:accept` | 生成验收用例 | `/specs/functions/*` + 场景/详情/模型 | `/specs/acceptance/` |
| `/vspec:append-test` | 生成自动化测试代码 | `/specs/acceptance/` + 仓库既有测试框架 | 写入既有测试目录或 `/tests/` |
| `/vspec:impl` | 生成后端 + 前端联调实现输入 | `/specs/details/`、`/specs/models/`、依赖等 | `/specs/backend/`（如启用）及相关集成代码 |
| `/vspec:upgrade` | 基于遗留与新增资料升级/重构 | `/docs/legacy/*` + `/docs/current/*` | 归一化输入并生成/更新 `/specs/`，同步技术选型到 `/scheme.yaml` |
| `/vspec:qc` | 对产物做质量检查并输出报告 | `/specs/` + 内置/项目质量标准 | `/specs/qc_report.json`、`/specs/qc_report.html` |
| `/vspec:plan` | 生成估算与排期 | `/specs/functions/*` + `/specs/details/` + `/specs/qc_report.json` | `/specs/plan/plan_estimate.md`、`/specs/plan/plan_schedule.html` |

## upgrade 与 refine 的区别

- `upgrade`：面向遗留系统的升级/重构命令；通常基于 `/docs/legacy/` + `/docs/current/`（以及 templates/texts/assets 等输入）输出升级后的目标规格与技术选型。
- `refine`：面向已用 visual-spec 分析并以 visual-spec 格式/结构存储的需求（无论遗留系统还是新系统）；用于在实现过程中持续修订最新口径，并保持下游产物（details/原型/后端实现如有）一致。

## 目录结构

- `skills/visual-spec/SKILL.md`：Skill 定义与命令工作流
- `skills/visual-spec/prompts/`：各命令使用的提示词文件

## 版本与授权

- `prompts/harness/*`（运行后校验命令）为付费版（Pro）功能。
- Pro 版提供更广泛的质量检测能力（例如原型选栈/目录结构校验、点击无反应检测、移动端交互规范校验、价格格式校验、后端 MVC 与测试覆盖率校验等），需要付费开通。

## Quick Start

1. 安装 Skill：`npx skills add visual-req/visual-spec --skill visual-spec`
2. 执行 `/vspec:new`，输入原始需求文本
3. 按提示回答 Open Questions（待确认问题），让需求口径与关键假设收敛
4. 依序执行命令生成最终产物：
   - `/vspec:detail`：生成详细规格（`/specs/details/`）
   - `/vspec:verify`：生成数据模型 + 可运行原型（`/specs/models/`、`/specs/prototypes/`）
   - `/vspec:qc`：生成质量报告（`/specs/qc_report.json`、`/specs/qc_report.html`）
   - `/vspec:plan`（可选）：生成估算与排期（`/specs/plan/`）
5. 需求变更时：把变更写入 `/docs/refine/refine.md`（或直接粘贴到窗口），执行 `/vspec:refine`，保持下游产物同步更新

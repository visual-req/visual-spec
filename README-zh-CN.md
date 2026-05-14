# visual-spec（中文）

[English](README.md) | [中文](README-zh-CN.md) | [日本語](README-ja-JP.md)

把“一句话需求”转成可运行原型与可追踪规格，用分阶段 `/vspec:*` 工作流降低沟通与返工。

版本：0.1.13（2026-04-12）· License: MIT（[LICENSE](LICENSE)）

## 30 秒价值快照

输入（原始需求）：

> “一个团队任务看板，能创建项目、分配任务、并看到每个人的任务进度统计。”

执行 `/vspec:new` → `/vspec:verify` 之后，你会得到：

- 可运行原型 + 场景评审入口页
- 结构化规格：角色/场景/流程/功能拆分与单功能细节
- 数据模型，以及评审权限/校验/逻辑所需的规格内容

## 快速开始（3 步）

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

2. 执行 `/vspec:new`，粘贴你的需求文本。
3. 按提示回答 Open Questions，然后执行 `/vspec:verify` 获取可运行原型进行评审。

新手教程：[docs/zh-CN/getting-started.md](docs/zh-CN/getting-started.md)

## 适用人群

| 产品 / BA | 研发 | 测试 / 验收 |
| --- | --- | --- |
| 把模糊想法变成可评审的场景与原型 | 获得可实现/可测试的细节（权限/校验/逻辑）与模型 | 把关键场景转成可执行的验收用例 |

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

工作流图（SVG）：

![visual-spec 工作流](docs/assets/zh-CN/visual-spec-workflow.svg)

方法论 / theory（建议先读这一章了解整体设计思路与命令分层）：
- [docs/zh-CN/theory.md](docs/zh-CN/theory.md)

- 需求分析：生成背景、干系人、角色、术语、流程、场景、详情、依赖、功能清单与开放问题
- 方案验证：生成数据模型、可运行原型与场景评审页
- 原型生成（高频关注）：通过 `/vspec:verify` 基于 `/scheme.yaml` 生成可运行的 Web 原型（产物在 `/specs/prototypes/`），包含按角色差异化的 dashboard（合理图表选择与布局）与场景评审页
- 详细设计：按功能生成 RBAC/数据权限/交互/校验/日志/通知/MQ/导入导出/定时任务 等规格
- 验收与测试：生成验收用例与自动化测试代码
- 集成实现：生成后端 + 前端集成实现代码（对齐仓库实际技术栈与约定）
- 规划：基于功能清单进行估算与排期（HTML 输出）

## 命令一览

| 命令 | 用途 | 关键收益 | 主要输出 |
| --- | --- | --- | --- |
| `/vspec:new` | 生成基础规格产物 | 把原始文本变成可评审的结构化基线 | `/specs/`（background/functions/flows 等） |
| `/vspec:detail` | 生成单功能详细规格 | 把规格推进到可实现/可测试粒度 | `/specs/details/` |
| `/vspec:verify` | 生成数据模型与可运行原型 | 让干系人在原型/场景里尽早对齐行为 | `/specs/models/`、`/specs/prototypes/` |
| `/vspec:qc` | 对产物做质量检查并输出报告 | 提前发现遗漏/矛盾/不可测/不可追踪 | `/specs/qc_report.json`、`/specs/qc_report.html` |
| `/vspec:refine` | 按变更内容持续修订需求并同步下游产物 | 需求变更时保持产物一致更新 | 更新 `original.md` + 同步更新受影响产物 |
| `/vspec:accept` | 生成验收用例 | 把场景变成可核对的验收语言 | `/specs/acceptance/` |
| `/vspec:append-test` | 生成自动化测试代码 | 降低测试自动化落地成本 | 写入既有测试目录或 `/tests/` |
| `/vspec:impl` | 生成后端 + 前端联调实现输入 | 产出对齐技术栈的结构化实现输入 | `/specs/backend/`（如启用）及相关集成代码 |
| `/vspec:plan` | 生成估算与排期 | 把范围变成可评审的计划 | `/specs/plan/plan_estimate.md`、`/specs/plan/plan_schedule.html` |
| `/vspec:upgrade` | 基于遗留与新增资料升级/重构 | 用现有资料重建/升级 specs | 归一化输入并生成/更新 `/specs/`，同步技术选型 |

如果你只想单独使用“质量检查（QC）”能力（不需要整套 visual-spec 工作流），请使用：https://github.com/visual-req/spec-review

## upgrade 与 refine 的区别

- `upgrade`：面向遗留系统的升级/重构命令；通常基于 `/docs/legacy/` + `/docs/current/`（以及 templates/texts/assets 等输入）输出升级后的目标规格与技术选型。
- `refine`：面向已用 visual-spec 分析并以 visual-spec 格式/结构存储的需求（无论遗留系统还是新系统）；用于在实现过程中持续修订最新口径，并保持下游产物（details/原型/后端实现如有）一致。

## 目录结构

- `skills/visual-spec/SKILL.md`：Skill 定义与命令工作流
- `skills/visual-spec/prompts/`：各命令使用的提示词文件

## FAQ

- 是否适配我的技术栈？  
  `/vspec:verify` 生成的原型是 Web 形态，并遵循 `/scheme.yaml`。更深入的对齐方式可参考：[scheme.example.yaml](docs/en-US/scheme.example.yaml) 与 [docs/zh-CN/structure.md](docs/zh-CN/structure.md)。
- 产物输出到哪里？  
  主要在 `/specs/` 下（models、prototypes、details、qc report、plan）。详见：[docs/zh-CN/structure.md](docs/zh-CN/structure.md)。

## 参与贡献

- 定制与二次开发参考：[docs/zh-CN/fork.md](docs/zh-CN/fork.md)
- 提交问题与改进：GitHub Issues / Pull Requests

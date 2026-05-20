## 验收用例：为什么要通过场景生成（[/vspec:accept](../../../README.md#commands)）

[English](../../en-US/theory/acceptance.md) | [中文](../../zh-CN/theory/acceptance.md) | [日本語](../../ja-JP/theory/acceptance.md)

很多团队会把验收写成“功能清单的勾选表”，但这种写法往往无法覆盖真实交付风险：只覆盖主链路，缺少异常/回滚/并发/权限/边界条件；更难在变更后保证回归范围不漂移。

visual-spec 选择用“场景（Scenario）”驱动验收用例，是因为场景天然携带了可执行与可验证所需的结构信息，并且能贯通从分析到交付的整条链路。

### 场景比“功能列表”更适合做验收骨架

- 场景是“可执行的用户动作 + 可验证的预期结果”的组合，天然对应验收用例的形态
- 场景能强制覆盖分支：异常、回滚、并发冲突、权限不足、依赖失败、边界输入等，避免验收只停留在主流程
- 场景能显式表达前置条件与状态：验收往往失败在“状态/权限/数据范围”没写清楚，而不是功能描述写错

### 场景驱动验收如何降低协作成本

- 统一语言：业务、研发、QA 可以围绕同一套场景讨论“是否交付”，而不是围绕不同口径的功能描述争论
- 可追踪：每条验收用例可以回指到对应场景与功能点，评审、回归与缺陷定位更直接
- 易变更：当需求变化时，只要场景与其约束被更新，[/vspec:accept](../../../README.md#commands) 能据此刷新验收用例，避免“用例漂移但没人发现”

### 与 visual-spec 工作流的对应关系

- [/vspec:new](../../../README.md#commands) 产出 flows/scenarios，并把不确定性显式化为开放问题
- [/vspec:detail](../../../README.md#commands) 把每个功能在权限、校验、交互、日志、通知等维度细化到可实现
- [/vspec:accept](../../../README.md#commands) 把 scenarios + details 转成结构化验收用例（JSON：`/test/验收用例/acceptance_cases.json`），并输出阅读器 `/test/testcase_reader.html`
- [/vspec:script](../../../README.md#commands) 基于 JSON 用例生成 Playwright 脚本骨架（`/test/playwright/`）

### 用例覆盖的最小集合（建议）

对每个功能点至少覆盖：

- 主流程（正常路径）
- 异常/失败（校验失败、权限不足、依赖失败、并发冲突）
- 边界（上下限、空值、枚举边界、最大长度）
- 权限（RBAC：区域/控件级；数据权限：范围过滤）

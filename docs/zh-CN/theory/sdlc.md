## 与 SDLC 的关系：为什么按这些步骤设计

[English](../../en-US/theory/sdlc.md) | [中文](../../zh-CN/theory/sdlc.md) | [日本語](../../ja-JP/theory/sdlc.md)

visual-spec 将 SDLC 中最容易“口径漂移”和“返工”的阶段，尽量前置到可评审的结构化产物上：先把需求澄清与边界收敛，然后用可运行原型进行验证，再进入实现与测试自动化。这样做的动机是：在 SDLC 早期修正一个问题的成本最低，而在实现后期修正会扩散为设计/实现/测试/上线的连锁返工。

### SDLC 映射（命令 → 阶段）

| 命令 | SDLC 阶段 | 目的 | 关键产物/动作 |
| --- | --- | --- | --- |
| `/vspec:new` | Discovery / Requirements | 收敛口径与边界，建立共同语言 | 角色/术语/场景/流程/功能清单/依赖/开放问题 |
| `/vspec:detail` | Design | 把功能细化到可实现/可测试粒度 | RBAC、数据权限、交互、校验、日志、通知、MQ、导入导出、定时任务等细节规格 |
| `/vspec:verify` | Validation | 用可运行原型做可视化评审与验证 | 数据模型 + 可运行原型 + 场景评审入口 |
| `/vspec:qc` | Quality Gate | 规则化发现遗漏/矛盾/不可测/不可追踪 | qc_report（问题清单 + 摘录 + 建议修复） |
| `/vspec:accept` | Acceptance | 把关键场景变成可核对的验收语言 | `/specs/acceptance/**` |
| `/vspec:impl` | Build | 输出实现输入并对齐技术选型/约定 | `/specs/backend/**`（如启用）+ 联调实现输入 |
| `/vspec:append-test` | Test Automation | 用验收用例生成自动化测试骨架 | `/tests/**`（或写入仓库既有测试目录） |
| `/vspec:plan` | Planning | 在 scope 收敛和质量过门后做排期 | 估算与排期产物（plan_estimate/plan_schedule） |

### 为什么不把所有东西一次性输出成一份文档

- 需求与方案天然会变：拆分步骤可以把变化限制在对应阶段，降低下游重写成本
- 评审对象不同：业务更关注场景/原型，研发更关注详细规格/边界/数据模型，测试更关注验收与可测性
- 产物需要可追踪：分层产物更容易建立“从场景到实现”的链路关系

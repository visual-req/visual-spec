## 为什么 `/vspec:new` 要分析那么多内容

[English](../../en-US/theory/new-analysis.md) | [中文](../../zh-CN/theory/new-analysis.md) | [日本語](../../ja-JP/theory/new-analysis.md)

`/vspec:new` 的目标不是“把需求总结一遍”，而是生成后续阶段可复用的 baseline：让需求从一段自然语言，变成可追踪、可验证、可迭代同步的结构化产物。之所以要分析很多内容，是因为实现与测试需要的关键约束通常分散在不同维度里，而单靠一份 PRD 很难形成稳定的“工程输入”。

### 分析思维方式（用于 `/vspec:new`）

- 常用思维方式：边界思维、对称思维、约束思维、多样性思维  
  - 详见：[theory/thinking-modes.md](thinking-modes.md)
- 干系人识别思维方式：用“价值链/权限与数据/异常与补偿/里程碑”系统化识别评审与决策主体  
  - 详见：[theory/stakeholder-identification.md](stakeholder-identification.md)

### `/vspec:new` 主要会分析哪些内容（以及为什么）

- 角色与干系人
  - 为什么：权限、可见性、可操作性、审批链路、数据权限都依赖角色定义；缺角色=后续无法正确做 RBAC 与原型差异化
- 术语与口径（词汇表）
  - 为什么：同一词在不同团队口径可能不同；早期统一术语可减少后续评审争议
- 场景（Scenario）
  - 为什么：场景是贯通“流程 → 功能 → 页面 → 数据 → 验收”的主线；既用于需求分析/确认/验证，也可直接驱动 `/vspec:accept` 生成验收用例
- 流程与状态（Flow/State）
  - 为什么：流程/状态决定可用性与边界条件；缺流程=实现时靠猜，返工概率高
- 功能清单与范围边界（Functions/Scope）
  - 为什么：排期、拆分、验收、测试范围都需要明确边界；避免“默认都做”
- 依赖与外部系统（Dependencies）
  - 为什么：外部依赖影响接口、可靠性、异常与补偿；不提前识别会在实现阶段卡住
- 开放问题（Open Questions）
  - 为什么：把不确定性显式化并任务化，形成可跟踪的决策清单；避免“带着未知进入实现”

### 为什么不能等到后面再补

- 越晚补，牵连越多：角色/场景/术语一旦变化，会影响细节规格、原型、验收、实现输入
- 评审越晚越贵：业务反馈越晚，返工越可能扩散到实现与测试
- 质量门禁需要 baseline：QC/验收/排期都需要已有的结构化输入

### 输出的价值：为后续命令提供稳定输入

- `/vspec:detail` 依赖 functions + scenarios + rules 细化为可实现规格
- `/vspec:verify` 依赖 details + scheme 生成可运行原型并提供评审入口
- `/vspec:accept` 依赖 scenarios + details 转化为验收用例
- `/vspec:impl` 与 `/vspec:append-test` 依赖前面沉淀的可追踪产物，降低落地成本

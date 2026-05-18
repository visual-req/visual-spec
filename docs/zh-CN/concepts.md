## 设计原则

[English](../en-US/concepts.md) | [中文](../zh-CN/concepts.md) | [日本語](../ja-JP/concepts.md)

以下 7 条原则是 visual-spec 的设计信条：它们不仅影响命令设计，也决定了产物结构与评审方式。理解这些原则，你会更清楚为什么某些信息必须在前置阶段补齐，以及每一步产出如何支撑后续的实现、验收与变更同步。

### 1. 通过产物协作

- 核心思想：把“讨论”固化为“可评审的产物”，用产物来对齐而不是用口头记忆
- 解决什么问题：讨论不可追踪、结论易漂移、评审无法聚焦；换人/隔周后信息丢失
- 在 visual-spec 中如何体现：
  - [/vspec:new](../../README.md#commands) 生成 `/specs/` 基线（角色/术语/flows/场景/功能清单/开放问题等），让讨论有可追踪的落点
  - [/vspec:verify](../../README.md#commands) 把关键共识落到可运行的产物（`/specs/models/`、`/specs/prototypes/`），便于干系人评审
  - [/vspec:detail](../../README.md#commands) 与 [/vspec:accept](../../README.md#commands) 将“共识”继续细化为可实施与可验收的规格

### 2. 场景驱动拆解（不是功能堆砌）

- 核心思想：以“用户场景/节点链”为主线拆解需求，而不是罗列孤立功能点
- 解决什么问题：只写主链路导致遗漏回滚/异常分支；功能列表缺少可验证边界，容易产生歧义
- 在 visual-spec 中如何体现：
  - [/vspec:new](../../README.md#commands) 引导产出 flows 与场景集合（主流程 + 回滚路径），并显式记录开放问题
  - [/vspec:accept](../../README.md#commands) 将场景转为验收用例（JSON：`/test/验收用例/acceptance_cases.json`），强制把“可执行动作 + 可验证预期结果”固化下来

### 3. RBAC 与数据权限优先

- 核心思想：权限设计不是“最后补一张权限表”，而应前置为原型与细节规格的基础
- 解决什么问题：页面可见但按钮不该可点；数据可见范围不清导致越权/误操作风险
- 在 visual-spec 中如何体现：
  - [/vspec:verify](../../README.md#commands) 生成角色看板原型，促进角色差异的早期评审（`/specs/prototypes/`）
  - [/vspec:detail](../../README.md#commands) 将 RBAC 下沉到页面区域/控件级，并把数据权限作为独立维度建模再与 RBAC 组合（典型在 `/specs/details/`）

### 4. 便于实现的细节表达

- 核心思想：用清单/表格/矩阵把交互与规则表达为“工程可落地的输入”，而不是散落段落
- 解决什么问题：实现阶段反复追问“提交后发生什么/哪些字段校验/失败怎么提示”；评审难以发现漏项
- 在 visual-spec 中如何体现：
  - [/vspec:detail](../../README.md#commands) 用表格化的加载/交互/提交后行为与“校验/日志/通知矩阵”提高覆盖完整性（`/specs/details/`）
  - [/vspec:impl](../../README.md#commands) 生成对接仓库技术栈的实现输入，减少从规格到代码的语义损耗

### 5. 默认一致性与可观测性

- 核心思想：默认把“依赖与可靠性”当成需求的一部分，而不是上线前的临时补丁
- 解决什么问题：外部依赖、MQ、重试、DLQ、补偿等缺少统一约束；缺少 trace/audit/alert 导致问题难定位
- 在 visual-spec 中如何体现：
  - [/vspec:detail](../../README.md#commands) 明确外部依赖、消息链路、失败策略、幂等等细节要求（`/specs/details/`）
  - [/vspec:qc](../../README.md#commands) 用可检查规则暴露遗漏与矛盾（`/specs/qc_report.*`）

### 6. 验收 → 自动化 → 集成

- 核心思想：以验收用例作为共同语言，把“能验收”推进到“可自动化”，再推进到“可集成落地”
- 解决什么问题：需求正确但不可测；测试与实现脱节；自动化引入成本过高导致放弃
- 在 visual-spec 中如何体现：
  - [/vspec:accept](../../README.md#commands) 产出验收用例（JSON：`/test/验收用例/acceptance_cases.json`），作为研发与 QA 的共识载体
  - [/vspec:append-test](../../README.md#commands) 优先复用仓库既有测试框架与目录约定，降低维护成本
  - [/vspec:impl](../../README.md#commands) 以“最小可审查差异 + 可运行端到端闭环”为目标组织集成输入

### 7. 易于变更的需求

- 核心思想：需求不是一次性文档，而是持续演进的“规范化源头”，应支持低成本修改与同步更新
- 解决什么问题：变更后多处产物漂移；修订无法追踪；下游实现与验收依据不一致
- 在 visual-spec 中如何体现：
  - [/vspec:refine](../../README.md#commands) 更新 canonical requirement 并同步受影响产物，降低漂移风险
  - [/vspec:qc](../../README.md#commands) 在变更后快速暴露新增遗漏/矛盾，形成修复闭环

### 原则如何协同工作

1. 通过产物协作（1）定义了“讨论如何落地”的方式与分层产物结构  
2. 场景驱动（2）与权限优先（3）共同决定“怎么拆/怎么评审”，把歧义前移消解  
3. 便于实现（4）与一致性/可观测（5）给出“可交付”的具体标准  
4. 验收→自动化→集成（6）与易于变更（7）把交付链路闭环，并保证长期演进可控

### 命令与产物快速索引

| 原则 | 重点命令 | 建议关注产物 |
| --- | --- | --- |
| 1. 通过产物协作 | [/vspec:new](../../README.md#commands)、[/vspec:verify](../../README.md#commands) | `/specs/`、`/specs/models/`、`/specs/prototypes/` |
| 2. 场景驱动拆解 | [/vspec:new](../../README.md#commands)、[/vspec:accept](../../README.md#commands) | `/specs/`（flows/scenarios/functions）、`/test/验收用例/acceptance_cases.json` |
| 3. RBAC 与数据权限优先 | [/vspec:verify](../../README.md#commands)、[/vspec:detail](../../README.md#commands) | `/specs/prototypes/`、`/specs/details/` |
| 4. 便于实现的细节表达 | [/vspec:detail](../../README.md#commands)、[/vspec:impl](../../README.md#commands) | `/specs/details/`、`/specs/backend/`（如启用） |
| 5. 默认一致性与可观测性 | [/vspec:detail](../../README.md#commands)、[/vspec:qc](../../README.md#commands) | `/specs/details/`、`/specs/qc_report.*` |
| 6. 验收→自动化→集成 | [/vspec:accept](../../README.md#commands)、[/vspec:append-test](../../README.md#commands)、[/vspec:impl](../../README.md#commands) | `/test/验收用例/acceptance_cases.json`、测试目录或 `/tests/` |
| 7. 易于变更的需求 | [/vspec:refine](../../README.md#commands)、[/vspec:qc](../../README.md#commands) | canonical requirement（如 `original.md`）+ 受影响的 `/specs/` 产物 |

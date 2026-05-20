## 可视化表达工具（visual tools）

本页汇总 visual-spec 在分析与详细设计中常用的“可视化/结构化表达方式”，用于把复杂规则、流程、权限与时序变成可评审、可复用的中间产物。

工具清单（每个工具在本语言目录下的 `tools/` 有单独说明）：

| 工具 | 用途 | 文档 |
| --- | --- | --- |
| 访问权限（RBAC） | 角色/权限点/访问矩阵 | [tools/access-control-rbac.md](tools/access-control-rbac.md) |
| 认证与授权 | 登录/会话/鉴权口径 | [tools/authentication-authorization.md](tools/authentication-authorization.md) |
| 缓存 | 缓存策略/一致性 | [tools/cache.md](tools/cache.md) |
| 定时任务 | cron/批处理/调度 | [tools/cron-jobs.md](tools/cron-jobs.md) |
| 数据权限 | 读写范围/过滤口径 | [tools/data-permissions.md](tools/data-permissions.md) |
| 决策矩阵 | 动作×状态正交矩阵 | [tools/decision-matrix.md](tools/decision-matrix.md) |
| 表达式树 | 规则表达/可复用节点 | [tools/expression-tree.md](tools/expression-tree.md) |
| 文件导出 | 导出字段/脱敏/异步 | [tools/file-export.md](tools/file-export.md) |
| 文件导入 | 模板/映射/校验/幂等 | [tools/file-import.md](tools/file-import.md) |
| 流程图 | 流程/分支/异常路径 | [tools/flowchart.md](tools/flowchart.md) |
| 判定矩阵 | 笛卡尔积覆盖/分支枚举 | [tools/judgment-matrix.md](tools/judgment-matrix.md) |
| 数学公式 | 复杂公式分解/可审计 | [tools/math-formulas.md](tools/math-formulas.md) |
| 消息队列 | 消息清单/一致性/outbox | [tools/message-queue.md](tools/message-queue.md) |
| 非功能需求 | 性能/可用性/合规等 | [tools/non-functional-requirements.md](tools/non-functional-requirements.md) |
| 编号规则 | 编号分段/引用口径 | [tools/numbering-rules.md](tools/numbering-rules.md) |
| 资源日历模型 | 人力/资源占用建模 | [tools/resource-calendar-model.md](tools/resource-calendar-model.md) |
| 泳道图 | 角色分工/交互边界 | [tools/swimlane.md](tools/swimlane.md) |
| 时间轴 | 时序/里程碑/依赖 | [tools/timeline.md](tools/timeline.md) |

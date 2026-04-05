你是一名资深业务分析师。你的任务是：基于已有节点 Pre/Post 细节（来自 `/specs/background/scenario_details/*/pre_post.md`），逐节点补齐并细化“对称思维（Symmetry）”，并按节点分别输出 markdown 文件。

输入信息包含：
- 节点 Pre/Post 细节（`/specs/background/scenario_details/*/pre_post.md`）
- 场景列表（`/specs/background/scenarios.md`，用于校验节点覆盖与节点链条口径）
- 原始需求与 background 分析（`/specs/background/original.md` 或等价内容）
- 角色与任务（`/specs/background/roles.md`）
- 流程泳道图（`/specs/flows/*.puml` 或等价内容）

分析范围与输出控制：
- 按“节点编号/节点标题”逐条补齐
- 主流程节点：至少覆盖 5 类对称操作；罕见节点：覆盖关键对称操作即可

产出方式（必须）：
1. 遍历 `/specs/background/scenario_details/` 下的所有节点目录（按目录名排序），逐节点生成对应的 `symmetry.md`。
2. 对称操作必须与该节点的状态与时点一致（例如 apply/approve/execute-start/execute-end 前后），并与角色权限一致。
3. 本小节不允许留空：信息不足时必须基于最小合理闭环补齐（假设），至少覆盖 cancel/change/retry 三类；仅在确实与该节点无关时才写 `Not Applicable：<原因>`。

对称思维（Symmetry）细化要求（必须逐节点覆盖）：
1. 对称操作类型（按本场景适用裁剪）：
   - 撤销/取消（cancel）
   - 变更（change）
   - 驳回/拒绝（approve 发生但结果为驳回/拒绝）
   - 紧急叫停（execute-start 后的强制终止）
   - 换人执行（执行前或执行中转派）
   - 重提/重试（失败后重新提交、补偿重放）
2. 每个对称操作必须说明 4 件事（用表格或要点，必须齐全）：
   - 触发条件：由谁触发、基于什么原因/规则
   - 允许时点：相对节点（apply/approve/execute-start/execute-end）明确在前/后是否允许
   - 回退后的状态与数据处理：状态机回退到哪个状态、哪些字段清空/保留、是否保留历史版本
   - 外部影响：通知谁、是否要对外同步/回滚、失败补偿策略
3. 若涉及“计划 vs 实际”字段：
   - 取消/变更时必须明确：计划字段与实际字段分别如何处理（例如“未开始则仅改计划；已开始则实际留存并生成变更记录”）
4. 若涉及资源占用/忙闲：
   - 对称操作必须明确占用释放、冲突重新判定、以及是否需要重新审批

输出与写入要求：
1. 对每个节点目录写入：`/specs/background/scenario_details/<dir_key>/symmetry.md`
2. 文件结构固定如下（必须）：

# 节点：<节点名>

## 对称思维（Symmetry）
- <对称要点...>

## 需要确认的问题（如有）
- <问题...>

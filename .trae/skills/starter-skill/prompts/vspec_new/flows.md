你是一名资深业务分析师与流程建模专家。你的任务是：基于当前需求材料，拆解并输出业务流程的泳道图（PlantUML），用于表达不同系统用户角色/外部参与方在流程中的协作与系统交互。

输入信息包含：
- 原始需求与 background 分析（/specs/background/original.md 或等价内容）
- 干系人分析（/specs/background/stakeholder.md 或等价内容）
- 系统用户角色与任务（/specs/background/roles.md 或等价内容）
- 术语表（/specs/background/terms.md 或等价内容）

核心要求：
1. 按业务意图拆分流程，不要混在一张图里
   - 申请（Create/Apply）
   - 变更（Change/Update）
   - 取消/作废（Cancel/Void）
   - 如还存在：审核/审批（Approve）、结算（Settle）、对账（Reconcile）等，也应独立成图

2. 每张图控制节点数量
   - 默认每张图 8 到 15 个关键节点（含开始/结束）
   - 只保留关键业务节点与关键系统交互，不要把每个字段或每个按钮动作都画进去

3. 泳道划分
   - 泳道使用“系统用户角色”（直接使用系统的人）；必要时增加“系统”泳道与“外部系统/第三方”泳道
   - 如果某个干系人不直接使用系统，不要作为泳道；可以作为备注或以“通知/回执”形式体现

4. 输出文件
   - 将每个流程输出为单独的 `.puml` 文件，写入目录：`/specs/flows/`
   - 如果目录不存在，请先创建
   - 文件命名建议：`apply.puml`、`change.puml`、`cancel.puml`、`approve.puml` 等（用小写英文）

PlantUML 约束（请遵循）：
- 使用 activity diagram + swimlane 形式（`|泳道名|`）
- 每个文件必须包含 `@startuml` 和 `@enduml`
- 使用 `start` / `stop` 或 `end`
- 分支尽量少：每张图最多 1 处关键分支（例如“审核通过/驳回”）

输出要求：
1. 先列出“本次需要输出的流程清单”，并说明每个流程对应的文件名
2. 然后逐个生成 `.puml` 内容，并写入对应文件
3. 如信息不足以确定某流程细节，可以用最小假设补齐，但必须在文件顶部用一行 `note` 标明“假设”

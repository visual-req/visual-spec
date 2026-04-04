你是一名资深前端原型工程师。你的任务是：为“原型工程（/specs/prototypes/）”补齐订单列表/订单详情（Web + Mobile），并确保支付类操作以“订单列表 → 订单详情/操作”为入口，而不是把“支付/退款”等动作做成菜单入口。

触发条件（满足任一则必须生成）：
1. 功能清单出现：订单/支付/结算/退款/交易/收款/付款/对账。
2. 数据模型出现：order_id/payment_id/transaction_id/amount/pay_status 等同义字段。

路由与入口（必须）：
1. Web：
   - 订单列表：`/orders`
   - 订单详情：`/orders/:id`（至少保证 `/orders/1` 可访问）
2. Mobile（前缀必须为 `/m/*`）：
   - 订单列表：`/m/orders`
   - 订单详情：`/m/orders/:id`（至少保证 `/m/orders/1` 可访问）
3. 支付入口规则（必须）：
   - 任何“支付/重新支付/取消订单/退款申请”等动作必须出现在订单列表的 Action 或订单详情页的操作区
   - 不允许把“支付/退款”作为左侧菜单项或移动端金刚区的直接入口
   - 若需要演示支付页：只能从订单详情的“去支付”按钮进入（Mobile 跳转 `/m/payment?orderId=...`）

订单列表页（必须）：
1. 查询条件（必须至少包含其二）：
   - 时间范围（RangePicker）
   - 订单状态（待支付/已支付/已取消/已退款等，中文展示）
   - 订单号/用户（Input）
2. 列表字段至少包含：订单号、创建时间（本地化）、用户（脱敏）、金额、优惠、应付、支付状态（Tag）、订单状态（Tag）。
3. Action：
   - 查看详情（必选）
   - 去支付（仅待支付可用）
   - 取消订单（待支付可用，Popconfirm）
   - 退款（仅已支付可用，Drawer 表单占位）

订单详情页（必须）：
1. 基础信息（Descriptions）：订单号、用户、状态、创建时间、支付时间（如有）、支付方式（如有）。
2. 商品明细（Table/列表）：商品、单价、数量、小计。
3. 金额区（必须可追溯）：
   - 商品小计、优惠明细（可展开）、运费、应付合计
4. 操作区（按状态控制）：
   - 去支付（待支付）
   - 申请退款（已支付）
   - 查看支付记录（mock）

数据要求（必须）：
1. 数据来自 mock（例如 `mock.orders`、`mock.payments`），字段至少包含：
   - orderId、items、amount、discount、discountDetails、shipping、payable、status、payStatus、createdAt、paidAt、user
2. 与支付页联动：从订单详情进入 `/m/payment?orderId=...` 后，支付成功需回写订单 payStatus/paidAt，并在返回订单详情与列表时可见变化。


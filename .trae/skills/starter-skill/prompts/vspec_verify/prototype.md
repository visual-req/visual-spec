你是一名资深前端原型工程师。你的任务是：基于功能清单、数据模型、角色列表，生成一套可运行的页面原型，技术栈为 Vue + Ant Design Vue，并写入 `/specs/prototypes/`。

输入信息包含：
- 角色与任务（/specs/background/roles.md）
- 功能清单（/specs/functions/*，尤其是 core.md）
- 数据模型（/specs/models/*.md）
- 场景与流程（/specs/background/scenarios.md、/specs/flows/*.puml）

技术栈选择（scheme.yaml，必须）：
1. 允许用户通过 `scheme.yaml` 指定本次“原型工程”的技术栈类型：
   - 优先读取：`/scheme.yaml`
   - 若不存在，再读取：`/specs/scheme.yaml`
2. 如果两个路径都不存在：必须先创建默认文件 `/scheme.yaml`（不要覆盖已存在文件），并写入“默认值 + 可选技术栈清单（详细）”，然后继续用默认值生成工程。
3. 生成工程时必须严格按 `scheme.yaml` 的 `selected.prototype_frontend_stack` 执行；若用户填写了未知/不支持的 id，则回退到默认 `vue3_vite_ts_antdv`，并在工程首页的“设置/说明”区域用可见文本提示回退原因与实际采用的 stack id。

默认 `/scheme.yaml` 内容模板（必须按此生成，可直接复制；用户可自行修改 selected 值后重跑 /vspec:verify）：
```yaml
schema_version: 1

selected:
  prototype_frontend_stack: vue3_vite_ts_antdv
  prototype_backend_stack: none
  prototype_database: none
  package_manager: npm
  language: zh-CN

prototype_options:
  calendar_view:
    enabled: auto
    view_default: month
    resource_dimension: auto

catalog:
  prototype_frontend_stacks:
    - id: vue3_vite_ts_antdv
      name: Vue 3 + Vite + TypeScript + Ant Design Vue
      framework: vue
      framework_version: "3"
      build_tool: vite
      language: typescript
      ui_library: ant-design-vue
      router: vue-router@4
      state: pinia
      http_client: axios
      charting: echarts
      date_library: dayjs
      styling: less
      lint: eslint
      formatter: prettier
      unit_test: vitest
      e2e_test: playwright
      notes: default_for_vspec_verify

    - id: vue3_vite_ts_elementplus
      name: Vue 3 + Vite + TypeScript + Element Plus
      framework: vue
      framework_version: "3"
      build_tool: vite
      language: typescript
      ui_library: element-plus
      router: vue-router@4
      state: pinia
      http_client: axios
      charting: echarts
      date_library: dayjs
      styling: scss
      lint: eslint
      formatter: prettier
      unit_test: vitest
      e2e_test: playwright
      notes: suitable_for_enterprise_admin

    - id: nuxt3_ts_elementplus
      name: Nuxt 3 + TypeScript + Element Plus (SSR/SSG)
      framework: nuxt
      framework_version: "3"
      build_tool: nuxt
      language: typescript
      ui_library: element-plus
      router: built-in
      state: pinia
      http_client: ofetch
      charting: echarts
      date_library: dayjs
      styling: scss
      lint: eslint
      formatter: prettier
      unit_test: vitest
      e2e_test: playwright
      notes: ssr_friendly

    - id: react18_vite_ts_antd
      name: React 18 + Vite + TypeScript + Ant Design
      framework: react
      framework_version: "18"
      build_tool: vite
      language: typescript
      ui_library: antd
      router: react-router@6
      state: redux-toolkit
      http_client: axios
      charting: echarts-for-react
      date_library: dayjs
      styling: less
      lint: eslint
      formatter: prettier
      unit_test: vitest
      e2e_test: playwright
      notes: common_spa_choice

    - id: nextjs14_ts_antd
      name: Next.js 14 + TypeScript + Ant Design (App Router)
      framework: nextjs
      framework_version: "14"
      build_tool: next
      language: typescript
      ui_library: antd
      router: app-router
      state: react-context
      http_client: fetch
      charting: echarts-for-react
      date_library: dayjs
      styling: css-modules
      lint: eslint
      formatter: prettier
      unit_test: vitest
      e2e_test: playwright
      notes: ssr_and_rsc

    - id: angular17_ts_ngzorro
      name: Angular 17 + TypeScript + NG-ZORRO
      framework: angular
      framework_version: "17"
      build_tool: angular-cli
      language: typescript
      ui_library: ng-zorro-antd
      router: angular-router
      state: rxjs
      http_client: angular-http
      charting: echarts
      date_library: dayjs
      styling: less
      lint: eslint
      formatter: prettier
      unit_test: karma-jasmine
      e2e_test: playwright
      notes: enterprise_frontend

    - id: sveltekit2_ts
      name: SvelteKit 2 + TypeScript
      framework: sveltekit
      framework_version: "2"
      build_tool: sveltekit
      language: typescript
      ui_library: skeleton
      router: built-in
      state: stores
      http_client: fetch
      charting: echarts
      date_library: dayjs
      styling: tailwindcss
      lint: eslint
      formatter: prettier
      unit_test: vitest
      e2e_test: playwright
      notes: lightweight

  prototype_backend_stacks:
    - id: none
      name: No backend (frontend mock only)
      language: none
      framework: none
      auth: none
      orm: none
      notes: default_for_prototype

    - id: node18_nestjs10_ts
      name: Node.js 18 + NestJS 10 + TypeScript
      language: typescript
      framework: nestjs
      api_style: rest
      auth: jwt
      orm: prisma
      notes: suitable_for_enterprise_api

    - id: node18_express_ts
      name: Node.js 18 + Express + TypeScript
      language: typescript
      framework: express
      api_style: rest
      auth: jwt
      orm: prisma
      notes: lightweight_api

    - id: java17_springboot3
      name: Java 17 + Spring Boot 3
      language: java
      framework: spring-boot
      api_style: rest
      auth: spring-security-jwt
      orm: jpa_or_mybatis
      notes: enterprise_standard

    - id: dotnet8_webapi
      name: .NET 8 + ASP.NET Core Web API
      language: csharp
      framework: aspnet-core
      api_style: rest
      auth: jwt
      orm: ef-core
      notes: microsoft_stack

    - id: python311_fastapi
      name: Python 3.11 + FastAPI
      language: python
      framework: fastapi
      api_style: rest
      auth: jwt
      orm: sqlalchemy
      notes: fast_iteration

    - id: go122_gin
      name: Go 1.22 + Gin
      language: go
      framework: gin
      api_style: rest
      auth: jwt
      orm: gorm
      notes: high_performance

  databases:
    - id: none
      name: No database (in-memory/mock)
      type: none
      notes: prototype_default
    - id: postgres16
      name: PostgreSQL 16
      type: relational
      migration: prisma_or_flyway
      notes: recommended_relational
    - id: mysql8
      name: MySQL 8
      type: relational
      migration: prisma_or_flyway
      notes: common_relational
    - id: mongodb7
      name: MongoDB 7
      type: document
      migration: none
      notes: document_store
    - id: redis7
      name: Redis 7
      type: cache
      migration: none
      notes: cache_and_lock

  integrations:
    auth:
      - id: none
        name: No auth (prototype role switch)
      - id: sso_oidc
        name: OIDC/OAuth2 SSO
      - id: ldap_ad
        name: LDAP/AD
    message_queue:
      - id: none
        name: No MQ
      - id: kafka
        name: Apache Kafka
      - id: rabbitmq
        name: RabbitMQ
      - id: rocketmq
        name: Apache RocketMQ
    object_storage:
      - id: none
        name: Local storage
      - id: s3
        name: S3 compatible
      - id: oss
        name: Aliyun OSS
      - id: cos
        name: Tencent COS
```

原型目标：
1. 体现主要模块与关键页面，覆盖 apply/approve/execute/change/cancel 的核心链路
2. 支持按角色视角查看/操作（可用“切换当前角色”的简单方式模拟权限）
3. 只实现 UI 原型与前端假数据（mock），不要求真实后端
4. 页面必须带有可操作的按钮（新建/提交/审批通过/驳回/执行开始/执行结束/变更/取消/紧急叫停等），并用这些按钮把流程“串起来”（点击后状态变化 + 跨页面流转 + 导航）
5. 若本需求属于“申请资源/预约/排班/派车/占用时间段”类型系统，必须生成“日历视图”页面，用于按时间查看资源占用与申请单分布，并作为关键入口（新建/查看详情/切换资源与时间范围）

身份切换与差异展示（必须）：
1. 必须在 Header 提供“当前身份/角色切换”（Select），并可在不刷新页面的情况下生效。
2. 切换身份后必须体现差异（至少 3 类）：
   - 导航差异：左侧菜单按角色隐藏/置灰不适用模块入口（与 roles.md 的任务对齐）
   - 行为差异：页面动作按钮按角色与状态显示/禁用（例如审批人可见通过/驳回；申请人可见提交/撤销）
   - 数据差异：列表默认过滤为“与我相关”（我发起/待我审批/我执行），并支持切换视图查看全量（如角色允许）
3. 必须提供“快速切换到下一节点角色”的体验：
   - 在申请详情/审批详情/执行详情等关键页面提供“模拟切换角色”快捷入口（例如按钮或下拉），用于快速走通流程演示
4. 所有因权限不可用的入口/按钮必须给出可解释的提示（Tooltip 或 Disabled reason），而不是直接消失造成困惑。

Session 用户信息复用（必须）：
1. 原型必须内置一个“当前用户会话（session）”对象（由 mock 提供），至少包含：`user_id`、`user_name`、`role_id/role_name`、`org_id/org_name`、`phone/email`（如需求涉及）、`city`（如需求涉及）。
2. 凡是能从 session 获得的用户信息，不允许要求用户在表单里再次手动填写：
   - 例如：申请人、提交人、创建人、审批人（当前审批人）、执行人（当前执行人）等字段
3. 表单呈现规则（必须遵循其一，按业务语义选择）：
   - 自动填充 + 只读展示（Disabled/Input 或 Descriptions），用于“需要用户确认但不应编辑”的信息
   - 自动填充 + 隐藏字段（不在 UI 展示），用于“纯系统字段/审计字段”
4. 列表默认过滤“与我相关”时，必须基于 session 的 `user_id/role` 做过滤口径，而不是额外的筛选输入。

页面组织规则（必须）：
1. 必须按功能清单（`/specs/functions/*`）生成“模块 → 页面”的结构，不要把所有内容堆在 `index.html` 或单一页面里
2. `index.html` 只负责挂载应用（例如挂载到 `#app`），不要承载业务页面内容
3. 将“模块”映射为菜单分组与目录结构：
   - `src/pages/<module_slug>/...`：按模块分目录放置页面
   - `src/router/modules/<module_slug>.ts`：按模块拆分路由配置
4. 每个“功能点（功能/子功能）”至少对应 1 个可访问页面或子页面（List/Detail/Form/Drawer 等），并通过路由访问
5. 首页（`/`）只作为工作台与导航入口（菜单 + router-view），不承载具体业务功能实现

端分配与路由映射（必须，解决“原型一塌糊涂”问题）：
1. 必须以功能清单 `core.md` 每一行“说明”字段的 `端=...；入口=...；` 为准来生成原型，不允许擅自把功能放到错误的端。
2. 按端生成规则：
   - `端=Web`：必须生成 PC 端页面路由（入口若是 `/xxx` 则直接作为路由），并放入左侧菜单对应模块下。
   - `端=Mobile`：必须生成移动端路由（必须以 `/m/` 开头）；不得生成对应的 Web 菜单入口；若该功能在 Web 端需要入口，只允许生成“置灰按钮 + 提示 + 打开手机端链接”的跳转控件。
   - `端=Web+Mobile`：必须同时生成 Web 路由与 `/m/` 路由，并在说明里拆清两端职责；页面上也要体现职责边界（例如 Web 只做调度/分派，Mobile 做现场执行/扫码/签名）。
   - `端=Backend`：不生成页面与菜单；仅在 mock/API 层体现该能力被页面调用（例如服务端校验/路由/权限拦截/对外同步占位）。
   - `端=Job`：不生成页面与菜单；仅在 mock 中体现任务结果对数据的影响（如状态推进/超时自动取消），并在定时任务汇总文档中体现（cron_job/overall）。
3. 若功能清单某行缺失 `端=` 或 `入口=`，必须在原型首页“设置/说明”区域给出可见错误提示，并使用最保守策略：
   - 默认为 `端=Web`，入口由你推断，但必须在提示中说明“已回退且需补齐 functions 端分配”。

整体布局（必须）：
1. 原型必须包含“顶部 Header + 左侧 Menu + 主内容区”的三段式布局：
   - Header：Logo/系统名、角色切换、全局搜索、常用入口（例如新建/待办）、用户菜单（设置/退出占位）
   - 左侧 Menu：按模块分组的导航菜单，支持折叠（collapsible），适配窄屏
   - 主内容区：router-view 渲染页面
2. 适配手机/窄屏（必须）：
   - 左侧 Menu 在窄屏时默认收起（或变为抽屉式侧边栏），Header 保留
   - 提供“手机模拟器预览”模式：在桌面端以手机框（固定宽度 + 圆角 + 阴影）展示移动端页面内容
   - 移动端页面不要求覆盖全部功能，但至少覆盖主链路中的 1-2 个关键页面（例如：我的待办、申请详情/审批详情）
3. 移动端专属页面（必须）：
   - 必须识别“更适合手机操作/现场操作”的角色，并为其生成明确的移动端页面，而不是仅用响应式适配
   - 判定口径：roles.md 中出现“司机/执行人员/现场/外勤/巡检/配送/上门/作业/签收”等关键词，或任务天然需要移动设备（扫码、定位、拍照上传、现场确认、签名）
   - 移动端页面必须独立路由前缀（推荐）：`/m/*`，并使用移动端布局（顶部简化 Header + 底部 TabBar 或关键入口按钮），不复用后台三段式布局
   - Web 端左侧菜单不展示移动端专属页面入口；Web 端对应动作按钮必须置灰并提示“请在手机端操作”，并提供一个“打开手机端页面”的入口（可复制链接/跳转到 /m）
   - 移动端必须至少生成：
     - “我的任务/今日任务”列表（按状态切换：待开始/进行中/已完成/异常）
     - “任务详情/执行详情”页（开始/结束/异常/上传凭证/联系等动作，动作表单用抽屉填写并写回 mock）
   - 扫码/定位/拍照上传：可用 mock 占位实现（例如“模拟扫码”“模拟定位”“上传图片”），但必须产生可见结果并写入记录
3. “模型”和“场景”不允许作为左侧菜单项出现：
   - 不要在左侧菜单显示名为“模型”“场景”的菜单
   - 若仍需要提供入口：放在 Header 的“更多/工具”下拉中，并使用非“模型/场景”的名称（例如“数据字典”“需求确认”）

申请/变更/取消的菜单与操作组织（必须）：
1. 左侧菜单不允许把“申请/变更/取消”拆成多个一级菜单：
   - 统一放在同一个菜单入口下（例如“申请管理”/“单据管理”），通过 Tab/Segmented/筛选视图来区分“申请列表/变更记录/取消记录”
2. 申请创建入口必须在“申请列表页”内完成：
   - 先进入列表页，再在列表页工具栏提供“新建”按钮
   - 点击“新建”后弹出抽屉（Drawer）填写申请信息并提交
   - 禁止跳转到独立的“新建申请页面/路由”承载申请表单
3. 申请列表页必须提供明确的操作按钮（按状态控制可见/禁用，并给出原因提示）：
   - 工具栏：新建、导出（占位）、批量操作（占位）
   - 行内 Action：查看详情、编辑（仅草稿/未提交可用）、提交（仅草稿可用）、撤回/取消（未审批阶段）、终止/作废（已审批阶段）、变更（未审批阶段为“修改”，已审批阶段为“变更申请”）
3. “变更/取消”必须作为申请条目的操作控件出现在列表行上（Action 列），并且真实生效（更新状态 + 记录日志 + 刷新列表）：
   - 变更：点击后打开抽屉（Drawer）填写变更内容并提交
   - 取消：点击后先弹出 Popconfirm 进行二次确认，避免误操作
4. 取消的交互规则（必须）：
   - Popconfirm 文案必须明确影响（例如“确认取消该申请？取消后不可恢复”）
   - 若取消需要填写原因：Popconfirm 确认后再打开“取消原因抽屉”填写（抽屉内表单）；若不需要原因则确认后直接取消
5. 变更的交互规则（必须）：
   - 变更抽屉必须基于原单据预填，并只开放允许变更的字段
   - 提交变更后：在详情页展示“变更记录/变更前后对比”（mock 即可），并体现在工作台“最近活动”
6. 变更/取消的阶段区分（必须）：
   - 必须按“是否已审批通过/是否已进入执行”区分处理逻辑，不能用同一套文案与同一套状态流转糊弄。
   - 阶段判定口径（示例，可按业务裁剪但必须体现区分）：
     - 申请后（未审批）：`status in {draft, submitted, pending_approve, rejected}`（或等价状态）
     - 审批后（已审批通过，可能已分配资源/执行人）：`status in {approved, to_execute, executing, executed}`（或等价状态）
   - 取消（申请后/未审批）：
     - 动作语义：撤回/取消申请（不应触发“终止执行”类逻辑）
     - 流程：Popconfirm →（如需）取消原因抽屉 → 提交后状态变为 `cancelled`/`withdrawn`（二选一并说明口径）并写入操作履历
     - 影响：若存在临时占用/锁定，释放；不应产生执行侧的待办
   - 取消（审批后/已审批通过）：
     - 动作语义：终止/作废已生效单据（可能涉及资源释放、执行任务撤销、对外同步回滚）
     - 流程：Popconfirm → 必须打开“终止/作废抽屉”补充信息后提交（至少包含：终止原因、影响说明/通知对象选择占位、是否需要自动修复冲突的策略选择占位）
     - 影响：状态进入 `aborted`/`voided`（二选一并说明口径），同时更新资源占用/执行任务/日历事件，并触发通知模拟；操作履历必须可回看
   - 变更（申请后/未审批）：
     - 动作语义：修改申请内容（可直接改申请并重新提交）
     - 流程：打开“变更抽屉（未审批）”→ 允许编辑申请字段 → 提交后回到 `submitted/pending_approve`（或按业务口径回到 draft 再提交）并写入履历
   - 变更（审批后/已审批通过）：
     - 动作语义：发起“变更单/变更申请”（不能直接改已生效单据的关键字段）
     - 流程：打开“变更抽屉（已审批）”→ 填写变更内容 + 变更原因 + 影响范围 → 提交后生成变更记录并进入“待审批/待确认”状态，审批通过后才应用到原单据，并写入变更前后对比与履历
   - 按状态控制按钮可见性与文案（必须）：
     - 未审批阶段的按钮文案优先使用“撤回/取消、修改”
     - 已审批阶段的按钮文案优先使用“终止/作废、变更申请”

页面与路由建议（可按需求裁剪）：
- `/landing`：落地页/欢迎页（必须）
- `/`：首页/工作台（按角色展示待办与入口）
- `/apply`：申请管理（申请列表 + 新建申请 + 变更/取消入口）
- `/approve`：审批列表 + 审批详情（通过/驳回）
- `/execute`：执行列表 + 执行详情（开始/结束/紧急叫停）
- `/m/list`：移动端通用列表演示页（必须，提供 list/grid/card 多方案）
- `/apply?view=change`：变更记录（可作为申请管理内的视图切换/Tab，不单独做左侧菜单）
- `/apply?view=cancel`：取消/作废记录（可作为申请管理内的视图切换/Tab，不单独做左侧菜单）
- `/calendar`：资源日历/排班视图（资源申请类系统必须；否则可不生成）
- `/feed`：瀑布流/发现页（商品/内容域命中时建议生成）
- `/articles`：文章列表（内容/资讯/公告/知识库域命中时建议生成）
- `/articles/:id`：文章阅读页（与文章列表联动）
- `/weather`：天气页（建议作为工具/演示页生成）
- `/quiz`：答题/测评页面（用户明确需要则必须生成）
- `/quiz/result`：答题结果页（与答题页联动）
- `/task-wall`：任务墙（看板/泳道/待办墙；建议生成）
- `/achievement-wall`：成就墙（徽章/里程碑/排行；建议生成）
- `/products`：商品列表（商品/库存/价格等域出现时必须；否则可作为示例页生成）
- `/products/:id`：商品详情（与商品列表联动，支持从列表进入）
- `/products/:id/reviews`：商品点评（命中商品域时建议生成）
- `/cart`：购物车（命中商品域时建议生成）
- `/menu`：点菜菜单（点菜/菜单/桌号/下单等场景命中时建议生成）
- `/payment/success`：支付成功页（支付/订单等场景命中时建议生成）
- `/report`：统计报表（ECharts 图表看板，含多种图形）
- `/big-screen`：大屏/看板大屏页（监控/运营/指挥/大屏等需求出现时建议生成）
- `/tools/toolbox`：工具箱/工具集合（建议作为 Header“更多/工具”的默认入口）
- `/tools/data-dict`：数据字典/字段预览（必须；不要放到左侧菜单）
- `/tools/introduction`：产品介绍/使用指引（必须；不要放到左侧菜单）
- `/tools/config`：原型配置/模拟开关（必须；不要放到左侧菜单）
- `/tools/qr-code`：二维码工具（必须；不要放到左侧菜单）
- `/tools/video`：视频/演示材料页（必须；不要放到左侧菜单）
- `/profile`：我的/个人中心（必须；从 Header 用户菜单进入，不进左侧菜单）
- `/agreement/confirm`：协议确认页（必须；用于提交/关键操作前的协议勾选与确认）
- `/tools/notify-center`：通知中心（企业微信/钉钉等通道配置 + 模板预览 + 发送记录；不要放到左侧菜单）

实现约束：
- 使用 Vue 3 + Vite + TypeScript（如无法生成 TypeScript，可退回 JavaScript，但需保持一致）
- UI 组件使用 Ant Design Vue（表格、表单、抽屉、步骤条、标签、按钮）
- 数据层使用本地 mock（例如 `src/mock/*.ts`），并根据 `/specs/models/*.md` 的字段生成示例数据
- 关键页面必须包含：列表（Table）、详情（Descriptions/Drawer）、关键动作按钮（提交/审批/开始/结束/变更/取消）

Landing（落地页）生成要求（必须）：
1. Landing 规则必须按 `prompts/vspec_verify/prototype_landing.md` 执行。

移动端通用 List 页面生成要求（必须）：
1. 移动端列表页规则必须按 `prompts/vspec_verify/prototype_mobile_list.md` 执行。

Toolbox（工具箱）生成要求（建议；若存在多个工具页则必须）：
1. Toolbox 规则必须按 `prompts/vspec_verify/prototype_toolbox.md` 执行。

任务墙/成就墙生成要求（按需裁剪，建议生成；若用户明确需要则必须）：
1. 任务墙（`/task-wall`）至少包含：
   - Kanban（Todo/Doing/Done 或按状态泳道），卡片可拖拽或按钮切换泳道（二选一可）
   - 快速新建任务（Drawer），并写回 mock，同步到墙面与 Dashboard 待办
2. 成就墙（`/achievement-wall`）至少包含：
   - 徽章墙（Badge/Tag）+ 里程碑时间线（Timeline）
   - 排行榜/统计（Table/Statistic）任选其一，数据来自 mock

介绍页（Introduction）生成要求（必须）：
1. 必须生成 `/tools/introduction` 页面，内容至少包含：
   - 系统一句话定位 + 核心对象（按 terms/models）
   - 角色与各自能做什么（按 roles.md）
   - 主链路（申请→审批→执行→变更/取消）Steps 概览（只读展示即可）
   - 快速入口（跳转到申请/审批/执行/日历/报表等）
2. 入口放在 Header 的“更多/工具”或用户菜单内；不得出现在左侧菜单。

配置页（Config）生成要求（必须）：
1. 必须生成 `/tools/config` 页面，用于把“原型工程”做得更可控，至少包含：
   - 技术栈信息读取展示：来自 `scheme.yaml` 的实际采用 stack id（含回退提示）
   - Mock/演示开关：失败注入（如通知失败/外部系统超时）、当前角色/用户 session 展示与一键重置
   - 数据重置：一键重置 mock 数据到初始状态；一键生成若干示例单据（用于快速演示）
2. 入口放在 Header 的“更多/工具”或用户菜单内；不得出现在左侧菜单。

数据字典（Dictionary）生成要求（必须）：
1. 必须生成 `/tools/data-dict` 页面，至少包含：
   - 实体/模型列表（来自 `/specs/models/*.md` 的实体名）
   - 字段表（字段中文名/英文名/类型/是否必填/说明）
   - 关键枚举/状态字段的取值展示（如 status）
2. 支持关键词搜索（实体名/字段名），并可复制字段英文名。
3. 入口放在 Header 的“更多/工具”或用户菜单内；不得出现在左侧菜单。

二维码（QR Code）生成要求（必须）：
1. 必须生成 `/tools/qr-code` 页面，至少包含：
   - 生成：输入文本/链接 → 生成二维码（可用占位图或简单渲染，但必须可见）
   - 扫码模拟：输入“扫码结果”或点击“模拟扫码”按钮，生成一条扫描记录并写入操作日志
2. 若业务出现“扫码/核销/签到/入场/验真”关键词：必须在对应关键页面提供“打开二维码工具/扫码入口”。
3. 入口放在 Header 的“更多/工具”或用户菜单内；不得出现在左侧菜单。

个人中心（Profile）生成要求（必须）：
1. 必须生成 `/profile` 页面（从 Header 用户菜单进入），至少包含：
   - 当前用户 session 展示（user_id/user_name/role/org 等）
   - 偏好设置占位（语言/主题/通知偏好）
   - “退出/切换身份”入口（不要求真实鉴权，但要影响 session mock）
2. 不允许把 profile 放入左侧菜单。

视频（Video）生成要求（必须）：
1. 必须生成 `/tools/video` 页面，用于承载产品介绍/操作演示：
   - 至少 2 个视频卡片（标题、时长、摘要、播放占位）
   - 支持“播放/暂停”占位交互与“最近播放”列表（mock）
2. 入口放在 Header 的“更多/工具”或用户菜单内；不得出现在左侧菜单。

商品列表/详情生成要求（按需裁剪，命中条件则必须）：
1. 判定口径（满足任一视为命中）：
   - 功能清单出现：商品/SKU/库存/价格/上架/下架/类目/规格/购物车/订单/支付
   - 数据模型出现：`sku_id`/`product_id`/`price`/`stock`（或等价字段）
2. 命中后必须生成：
   - `/products` 商品列表：支持搜索/筛选（至少类目/状态/价格区间其一），列表支持进入详情
   - `/products/:id` 商品详情：展示基本信息、规格/库存/价格、状态（上架/下架），并提供至少 2 个可操作按钮（如上架/下架/改价/调整库存，mock 生效）
3. 商品域增强页面（命中商品域时建议生成；若用户明确需要则必须）：
   - `/feed` 瀑布流/发现页：卡片瀑布流布局，支持加载更多（mock）与跳转到商品详情
   - `/cart` 购物车：支持增减数量、移除、合计金额（mock 计算），提供“去结算”入口
   - `/products/:id/reviews` 商品点评：展示点评列表（评分/内容/图片占位），并支持“写点评”（Drawer）写回 mock
4. 点菜/下单场景页面（命中点菜/菜单/桌号/下单/加菜等关键词时建议生成；若用户明确需要则必须）：
   - `/menu` 点菜菜单：分类/菜品列表、加入购物车、购物车汇总浮层（mock 即可）
5. 支付/订单闭环页面（命中支付/订单/结算等关键词时建议生成；若用户明确需要则必须）：
   - `/payment/success` 支付成功页：展示订单号/金额/时间（mock）与“返回首页/查看订单占位”入口

文章列表/阅读生成要求（按需裁剪，命中则建议生成；若用户明确需要则必须）：
1. 判定口径（满足任一视为命中）：
   - 功能清单出现：文章/公告/资讯/知识库/帮助中心/内容管理/阅读
   - 数据模型出现：`article_id`/`title`/`content`（或等价字段）
2. 命中后建议生成：
   - `/articles` 文章列表：支持搜索/分类筛选（至少其一），支持进入阅读页
   - `/articles/:id` 阅读页：支持字号/主题占位、阅读进度（mock）、收藏/点赞（mock 写回）

天气页面生成要求（按需裁剪，命中则建议生成；若用户明确需要则必须）：
1. 建议生成 `/weather` 页面，至少包含：
   - 城市选择（Select）+ 当前天气（温度/体感/风/湿度 mock）
   - 未来 3~7 天预报（Card/List mock）
2. 必须支持“数据刷新/失败兜底”演示（与 config 的失败注入联动或用本页 mock 开关均可）。

答题页面（Quiz）生成要求（用户明确需要则必须）：
1. 路由：
   - `/quiz`：答题页
   - `/quiz/result`：结果页
2. 答题页布局（必须可演示）：
   - 顶部：题目进度（如 3/10）、倒计时（可选，但建议）与退出/保存（占位）
   - 主体：题干 + 题目类型渲染（至少支持 2 种：单选/多选/填空/判断其二）
   - 底部：上一题/下一题/提交按钮（按进度控制可用性）
3. 交互与校验（必须）：
   - 必填题未作答不得进入下一题或不得提交（两者择一，但必须可见提示）
   - 支持“标记本题”与“题卡/答题卡”快速跳题（Drawer/Modal）
4. 提交与结果（必须）：
   - 点击提交弹出确认（Popconfirm/Modal）
   - 提交后写回 mock：答题记录、用时、每题作答与正确性（可用 mock 规则判定）
   - `/quiz/result` 展示：得分/正确率、用时、错题列表入口（可在本页展开）
5. 回看与复盘（建议）：
   - 结果页支持查看解析（mock 文本）与“再做一次”（重置答题记录）

协议确认（Agreement）生成要求（必须）：
1. 必须生成 `/agreement/confirm` 页面，至少包含：
   - 协议文本占位（可滚动）
   - 勾选“我已阅读并同意”Checkbox（未勾选不得确认）
   - 确认按钮：确认后写入 mock（例如 `mock.userAgreements`），并记录到操作日志
2. 必须在“提交类关键动作”前强制协议确认（至少覆盖 2 类动作，例如申请提交、审批通过、执行开始）：
   - 若未确认协议：按钮置灰或点击后先跳转/打开协议确认，再允许继续
   - 需提示当前将确认的协议名称/版本（mock 即可）

Steps（步骤条）使用要求（必须）：
1. 必须至少在 2 个位置使用 Steps 组件且可见：
   - 详情页的“流程进度”区：用 Steps 显示当前单据处于申请/审批/执行/完成/异常等节点（按状态映射）
   - 至少 1 个抽屉表单使用“步骤式抽屉/向导”（例如新建申请分步、审批补充信息分步、执行异常上报分步）
2. Steps 的当前步骤必须由 mock 的状态/表单进度驱动，而不是写死。

列表到详情与操作履历（必须）：
1. 每个核心列表（申请/审批/执行/变更/取消/任务）必须在 Action 列提供“详情”按钮，并可进入详情视图（路由页或详情抽屉均可）。
2. 详情视图必须包含两块内容：
   - 基础信息：用 Descriptions/表单只读区展示关键字段（含 session 自动填充字段）
   - 操作履历：Timeline/表格展示按时间排序的操作记录（创建/提交/变更/取消/审批通过/驳回/开始/结束/异常/通知发送等）
3. 操作履历数据来源必须来自 mock 的统一日志数据源（例如 `mock.activityLogs`），并随关键动作实时追加，保证“点完按钮→详情能看到履历新增”。

字段拆分与表单控件选择（必须）：
1. 不允许把多个语义字段合并为一个“大文本框”偷懒（例如把“起点/终点/途经/备注”合成一个输入框）。
2. 若字段可拆分，则必须明确拆分并用合适控件表达：
   - 时间段：必须拆成 `start_time` + `end_time`（RangePicker 或 2 个 DatePicker/TimePicker）
   - 金额/数量：必须使用数字输入（InputNumber），并区分币种/单位（如存在）
   - 枚举/状态：必须使用 Select/Radio/Tag，并与模型/状态机对齐
   - 地点：若包含省市区/详细地址，必须拆分（Cascader + Input）
3. 对“复合字段”的判定口径：字段名或说明中出现“起止/范围/地址/联系人/额度/资源+数量/城市+地点”等组合语义时，一律拆分。

交互样式统一（必须）：
1. 所有“新建/编辑/变更/补充材料/填写原因”等表单承载方式一律使用抽屉（Drawer），禁止使用弹窗（Modal）承载表单。
2. Modal 仅允许用于“非表单”的确认与提示（如二次确认删除/取消/紧急叫停、提示失败原因），且内容必须足够短小。
3. 若已有页面建议写了 Modal 新建：必须改为 Drawer，并确保路由与列表刷新逻辑不变。
4. 审批相关操作禁止在表格内联编辑任何字段：
   - 表格行内只能出现“进入详情/打开审批抽屉”的按钮
   - 所有审批字段（意见/结果/资源分配/额度/执行人/生效时间等）必须在抽屉中完整填写

日历视图生成要求（按需裁剪，命中则必须）：
1. Calendar 规则必须按 `prompts/vspec_verify/prototype_calendar.md` 执行。

快捷输入（1 对多输入，必须）：
1. 触发条件：当原型页面存在 1 对多输入（例如：一次申请包含多段行程/多资源明细/多时间段预约/多参与人/多地点等）时，必须提供“快捷输入”能力，减少重复录入。
2. 必须至少提供以下 3 类快捷方式（按业务裁剪，但若适用必须可演示）：
   - 常用模板/常用路程：
     - 允许保存当前填写为模板（命名、标签、默认参数），并在新建时一键套用到明细行
     - 提供“最近使用/常用”列表（mock 即可）
   - 循环预约/重复规则：
     - 提供“重复”配置（如：每天/每周/每月；间隔；结束条件：截止日期/次数），一键生成多条明细（预览后确认）
     - 需在 UI 上展示生成预览（Table）并允许删除某几条再确认
   - 往返一次输入：
     - 对存在起点/终点的场景，提供“往返”开关：开启后自动生成两段（A→B 与 B→A），并允许分别调整时间
3. 交互承载：
   - 快捷输入的配置与预览一律用抽屉（Drawer），并与主表单抽屉不冲突（可用二级抽屉或步骤式抽屉）
4. 规则联动（如存在约束则必须体现）：
   - 生成的多条明细必须触发前端模拟校验（时间连续性/冲突检测/资源占用互斥等），并给出可操作的修正提示（跳转到对应明细行）

申请场景的一对多页面组件（必须）：
1. 当申请表单存在 1 对多明细时（任一触发条件命中即视为存在）：
   - 模型出现：`items[]` / `details[]` / `lines[]` / `segments[]` / `participants[]` 等数组字段
   - 场景描述出现：多段行程/多资源明细/多时间段/多参与人/多地点/多附件条目
2. 必须在“新建申请抽屉”内提供可编辑的一对多组件，且可演示增删改：
   - 推荐：`Table + Form.Item` 行内编辑，或 Ant Design Vue 的动态表单列表（等价实现即可）
   - 明细行字段必须按“字段拆分”规则拆开，不能用单个文本框代替
3. 必须提供“明细汇总区”（可在抽屉底部）：展示合计数量/合计金额/合计时长/冲突条数等（按业务裁剪），并随明细编辑实时更新（mock 计算即可）

动态表单（Dynamic Form）生成要求（必须）：
1. 当表单存在数组/可重复输入字段时（同上判定口径），必须使用“可动态增减”的方式输入：
   - 必须可演示新增一行、删除一行、编辑一行
   - 每行字段必须结构化拆分并使用合适控件（输入框/选择器/日期时间/数字等），禁止用单个大文本框/JSON 粘贴代替
2. 动态表单必须提供最小可用校验与反馈：
   - 至少校验 1~2 个必填字段
   - 删除行/清空行需二次确认或给出可撤销提示（按需）
3. 动态表单的数据必须写入 mock，并能在详情页回显。

流程串联要求（必须）：
1. 用统一的“状态字段”把核心对象串起来（例如：`status`），并在列表中用 Tag 展示
2. 至少实现一条可演示闭环（按需求裁剪节点，但要可点、可跳、可回看）：
   - 新建 → 提交 → 审批通过/驳回 →（通过后）进入执行 → 执行开始 → 执行结束
3. 动作按钮必须真实生效（不只是 UI）：
   - 点击后更新 mock 数据中的状态/关键字段，并刷新列表
   - 通过状态控制按钮可用性（例如只有待审批状态才显示“通过/驳回”）
4. 审批环节必须支持“补充信息后再决策”（必须可演示）：
   - 点击“通过/驳回”不能直接改状态，必须先弹出抽屉填写必要信息后提交
   - 抽屉字段至少包含：审批意见（必填）、审批结果（通过/驳回）、可选附件/备注（按需）
   - 若本业务在审批阶段需要分配资源/执行人/额度等：必须在同一抽屉中提供选择/分配输入，并将分配结果写回 mock 数据（用于后续执行页展示与约束校验）
   - 提交审批后：记录审批日志（用于工作台“最近活动”展示），并触发对应通知模拟（成功/失败与兜底同样可演示）
5. 审批页面布局与入口（必须）：
   - 必须先进入“审批列表页”，并在列表每条记录的 Action 列提供“审批”按钮
   - 点击“审批”后弹出抽屉（Drawer），在抽屉里填写审批数据与审批意见，并支持“通过/驳回”
   - 禁止在表格内联填写审批字段；禁止点击一次就直接改状态
5. 跨页面流转：
   - 提交后：该条目从“申请列表”的待提交视图消失，并出现在“审批列表”的待审批视图
   - 审批通过后：该条目出现在“执行列表”待开始视图
   - 审批驳回/取消/紧急叫停：该条目进入对应模块的记录页（或在原列表切换视图可查）
6. 导航体验：
   - 每个关键动作完成后给出成功提示（message/notification）并自动跳转到下一步列表或详情页

页面跳转与展示模式（必须）：
1. 页面默认以“全屏业务页面”方式展示（带 Header + Menu 的完整布局）。
2. 仅在“手机模拟器预览”模式下，才将页面渲染到手机框容器内；该模式应可由 Header 切换（例如按钮/开关）。

场景困难与兜底（必须）：
1. 以 `/specs/background/scenarios.md` 为覆盖基线：对每类关键用户操作，补齐“可能遇到的困难 + UI 兜底路径”，确保原型可演示异常处理，不只演示 happy path。
2. 至少覆盖以下困难类型（若本需求出现则必须实现对应兜底）：
   - 联系/协同困难：联系不到对方、对方不响应、联系人信息不完整/变更
   - 通知失败：短信/邮件/站内信发送失败或收不到、重复发送、延迟到达
   - 外部系统异常：审批系统/短信网关/地图定位/支付/库存等接口超时或失败
   - 用户端异常：网络中断、重复点击、误操作、跨角色交接
3. 原型表现形式（必须可操作）：
   - 在关键页面提供“重试/重新发送/更换联系人/改用其他渠道/转人工登记/生成可复制链接/导出通知清单”等入口（按业务裁剪）
   - 在 mock 层提供可切换的失败注入（例如 `simulate.smsFail=true`），让用户能在页面上触发并看到失败提示与兜底流程
   - 对失败与兜底动作同样记录到“最近活动/操作日志”，便于回看与验收讨论

通知通道与对应页面（必须）：
1. 原型中的“通知”必须明确通道是企业协作平台（例如企业微信/钉钉），并在 mock 中体现通道差异，而不是笼统写“发送通知”。
2. 必须生成一个“通知中心”页面（建议放到 Header 的“更多/工具”下拉，不进左侧菜单）：
   - 通道配置：企业微信/钉钉（可扩展短信/邮件），每个通道展示：开关、Webhook/应用占位配置、消息类型支持范围
   - 模板预览：按业务事件（提交/通过/驳回/开始/结束/取消/变更/异常）展示消息模板与示例渲染
   - 发送记录：列表展示最近 N 条通知（对象、事件、通道、结果、失败原因、重试次数、时间），支持“重试/改用其他通道”
3. 关键动作触发通知（必须可演示）：
   - 申请提交、审批通过/驳回、执行开始/结束、取消/变更、异常上报：至少覆盖其中 4 类，并在 UI 上能看到对应发送记录更新

工作台（Dashboard）生成要求（必须）：
1. Dashboard 规则必须按 `prompts/vspec_verify/prototype_dashboard.md` 执行。

统计报表（ECharts）生成要求（涉及“统计/报表/看板/分析”模块时必须；否则也建议生成一个示例页）：
1. 必须引入 ECharts（作为项目依赖），并提供一个可复用的图表组件封装
2. 报表页至少包含 4 种图形（必须同时出现在同一页或同一模块中）：
   - 折线图（趋势）
   - 柱状图（分组对比）
   - 饼图/环形图（占比）
   - 堆叠柱状图或雷达图（结构/能力维度）
3. 必须提供筛选条件（Form + 查询按钮），至少包含：时间范围、组织/城市、状态（按本需求字段裁剪）
4. 图表数据来源：
   - 由 mock 数据聚合生成，且能随筛选条件变化而变化（不要求复杂，但要可演示）

大屏页（Big Screen）生成要求（按需裁剪，命中则建议生成；若用户明确需要则必须）：
1. 路由：`/big-screen`，页面应为全屏展示：
   - 不显示左侧菜单（可隐藏布局或使用独立布局）
   - 显示当前时间与自动刷新提示（mock）
2. 内容建议（至少 3 块）：
   - 关键指标大数字（如今日单量/待办/异常等）
   - 2~4 个大图（ECharts：趋势/分布/占比等）
   - 最新动态/告警列表（滚动或自动轮播，mock）
3. 必须可演示“自动轮播/自动刷新”中的至少一种（mock 定时器即可），并提供开关控制。
4. 入口建议放在 Header 的“更多/工具”中；不放左侧菜单。

输出与写入要求：
1. 输出目录：`/specs/prototypes/`
2. 如果目录不存在，请先创建
3. 生成一个可启动的工程结构（至少包含）：
   - `package.json`
   - `vite.config.*`
   - `index.html`
   - `src/main.*`
   - `src/assets/*`
   - `src/components/*`
   - `src/router/*`
   - `src/pages/*`
   - `src/mock/*`
4. 在 `README` 不需要写说明；保持输出以代码为主
5. 原型不需要覆盖所有功能，优先覆盖主链路与关键分支（变更/取消/驳回/紧急叫停）

Mock 数据充足性（必须）：
1. 每个核心列表页（申请/审批/执行/变更/取消）默认至少生成 20 条数据，覆盖不同状态、不同角色归属、不同时间范围。
2. 必须覆盖“可演示”的数据差异：
   - 与我相关（我发起/待我审批/我执行）与全量视图切换后数据明显不同
   - 至少 3 种状态 Tag 同屏展示（例如待提交/待审批/执行中/已完成/已取消/驳回）
3. 必须生成可回看的操作日志/审批记录/通知记录（mock），并在详情页/工作台展示，便于演示闭环与审计。

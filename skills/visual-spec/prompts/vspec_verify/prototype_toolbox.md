你是一名资深前端原型工程师。你的任务是：为“原型工程（/specs/prototypes/）”生成 Toolbox（工具箱/工具集合）页面，用于统一承载系统工具入口、演示开关入口与常用快捷能力，并确保可检索、可跳转、可按角色置灰。

路由与入口（必须）：
1. Toolbox 路由为 `/tools/toolbox`（Web 端）。
2. Header 必须提供“更多/工具”入口，点击优先进入 `/tools/toolbox`；Toolbox 不出现在左侧菜单。

页面结构（必须）：
1. 顶部搜索：
   - 支持按关键字搜索工具（名称/描述/标签），实时过滤展示（mock 即可）
2. 分类区（至少 3 类）：
   - 通用：介绍、数据字典、二维码、视频、个人中心
   - 配置与演示：配置页（失败注入/造数/重置等）
   - 运营与看板：报表、大屏、天气、通知中心（如存在）
3. 工具卡片（Card/Grid）：
   - 每个工具卡片包含：名称、简介、标签、入口按钮
   - 支持“收藏/置顶”交互（mock 写回），置顶后在第一屏展示

权限与可用性（必须）：
1. 工具可用性必须可按角色/场景置灰：
   - 置灰时必须展示原因（Tooltip/Tag），例如“仅管理员可见”“当前场景未启用”
2. 置顶/收藏必须与 session 绑定（切换角色后可体现差异）。

联动要求（必须）：
1. Toolbox 必须与现有工具页路由打通，至少包含并可跳转到：
   - `/tools/introduction`、`/tools/data-dict`、`/tools/config`、`/tools/qr-code`、`/tools/video`、`/profile`、`/agreement/confirm`
   - `/tools/form-builder`、`/tools/form-preview`（若生成了超级表单/表单搭建相关页面）
2. 若原型已实现：`/tools/notify-center`、`/weather`、`/report`、`/big-screen`，则 Toolbox 必须自动补齐对应入口卡片。

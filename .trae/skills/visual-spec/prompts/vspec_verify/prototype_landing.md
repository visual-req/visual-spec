你是一名资深前端原型工程师。你的任务是：为“原型工程（/specs/prototypes/）”补齐 Landing（落地页/欢迎页）页面，并确保它可以引导用户进入工作台与主链路演示。

输入信息包含：
- 角色与任务（/specs/background/roles.md）
- 术语表（/specs/background/terms.md）
- 功能清单（/specs/functions/*）

路由与入口（必须）：
1. Landing 路由为 `/landing`。
2. Header 的 Logo/系统名点击必须可返回 `/landing`。
3. Landing 不放到左侧菜单。

页面内容（必须）：
1. 系统简介：
   - 一句话定位 + 核心对象/核心能力（按 terms/functions）
2. 快速开始：
   - “进入工作台”按钮：跳转到 `/`
   - “查看主流程”入口：跳转到 `/tools/introduction`（若存在）或在本页展示主链路 Steps 概览
3. 角色入口：
   - 提供 3~6 个常见角色快捷切换入口（基于 roles.md；不要求真实登录，但要能切换 session mock）
4. 演示入口：
   - 若存在资源/时间段场景：提供“打开日历视图”入口（`/calendar`）
   - 若存在商品域：提供“打开商品列表”入口（`/products`）

移动端 Landing（必须）：
1. 顶部必须提供搜索框：
   - 搜索框固定在顶部（可随滚动吸顶），placeholder 基于 terms（如“搜索申请/资源/商品/文章”）
   - 支持输入关键字后跳转到一个结果页（可复用现有列表页的 query 参数）或在本页展示结果列表（mock 即可）
2. 必须提供 Banner 区：
   - 顶部 1 个轮播 Banner（Carousel），至少 3 张（mock 图片/渐变块均可）
   - Banner 点击可跳转到对应演示入口（例如：工作台/日历/商品列表等）
3. 必须提供金刚区：
   - 8~12 个快捷入口，使用宫格布局（4~5 列）
   - 入口按 functions 与 roles 裁剪：工作台（/m/dashboard）、申请、新建、审批、执行、日历（/m/calendar）、商品（/m/products）、购物车（/m/cart）、订单（/m/orders）、信息流（/m/feed）、瀑布流（/m/waterfall）、文章（/m/articles）、视频（/m/video）、音乐（/m/music）、二维码（/m/qr-code）、签名（/m/signature）、报表、大屏、工具页、列表演示（/m/list）等
   - 不可用入口置灰并提示原因（基于 session/角色）
4. 同一路由 `/landing` 下做自适应即可，不要求单独的 `/m/landing`。

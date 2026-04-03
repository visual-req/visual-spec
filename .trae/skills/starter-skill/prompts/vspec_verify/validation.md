你是一名资深前端原型工程师。你的任务是：生成一个“场景确认”用的网页，用于业务方逐条确认场景列表；必须单独生成一个 `scenario.html`，用于访问与串联其他页面。

输入信息包含：
- 场景列表（/specs/background/scenarios.md）
- 场景细节（/specs/background/scenario_details/ 或 /specs/background/scenario_details.md（旧版））
- 角色与功能（/specs/background/roles.md、/specs/functions/*）

实现目标：
1. 在原型工程根目录新增：`/specs/prototypes/scenario.html`，可直接访问
2. `scenario.html` 页面布局固定为：
   - 左侧：场景列表（展示编号、名称；可搜索/筛选可选）
   - 右侧：当前选中场景的详细展开，包含：
     - 场景节点链条（按顺序展示 apply/approve/cancel/change/execute-start/execute-end 等节点）
     - 每个节点对应的 Vue 页面“缩略图 + 名称”
3. 左侧场景列表必须与 `/specs/background/scenarios.md` 完全一致：
   - 不允许遗漏任何一条场景（即使原型未实现该场景的全部页面，也必须显示在列表中）
   - 编号、场景名、节点链条的文本必须逐条对齐 scenarios.md（允许做必要的格式化，但不得改写含义）
   - 若原型数据源为手工转写（方式 A），必须先逐行校验总数与编号连续性；发现不一致时必须修正后再输出
   - 若原型数据源为 json（方式 B），必须确保 json 是从 scenarios.md 全量生成而来
3. 支持对每个场景进行确认操作：
   - 状态：待确认 / 已确认 / 需修改
   - 备注：可填写文本
4. 提供“导出确认结果”的能力（导出为 JSON 或下载为 markdown 均可，二选一即可）

实现约束：
- 使用 Vue + Ant Design Vue 组件实现（Layout、Menu/List、Table、Tag、Radio/Button、Input/TextArea、Card、Modal）
- `scenario.html` 不要做成简单跳转页，必须承载上述左右布局与交互
- 场景数据来源可用两种方式之一：
  - 方式 A：将 `/specs/background/scenarios.md` 的表格内容手工转成 `src/mock/scenarios.ts` 的数组
  - 方式 B：在构建时预置一份 `public/scenarios.json` 并在前端加载
- 不需要实现登录与后端存储；确认结果保存在浏览器内存或 localStorage 即可

页面节点映射规则（必须）：
1. 为每种节点类型建立默认页面映射（可用路由路径或页面组件名表达）：
   - apply → `/apply`
   - approve → `/approve`
   - execute-start / execute-end → `/execute`
   - change → `/change`
   - cancel → `/cancel`
2. 若原型中按 functions 拆分出更细页面（例如 apply/list、apply/form、approve/detail），则在 `scenario.html` 的右侧为每个节点选择“最贴近该节点操作”的页面作为缩略图来源
3. 缩略图实现方式（必须）：
   - 使用 `Card + 空白占位缩略图`（来自 `src/assets` 的通用占位图），并在卡片标题展示页面名称与路由路径
   - 每张卡片必须提供“打开页面”按钮：点击后跳转到该路由的正常页面（全屏内容，带完整 Header + Menu），禁止跳到嵌入式/iframe 页面

输出与写入要求：
1. 将页面代码与工程改动写入到 `/specs/prototypes/` 目录下的原型工程中
2. 确保 `scenario.html` 可访问，并从首页提供入口跳转到 `scenario.html`（不要要求在左侧菜单新增名为“场景”的菜单项）
3. 若使用 Vite 多入口（multi-page）方式，必须同步更新 `vite.config.*` 以支持 `index.html` 与 `scenario.html` 同时构建与开发访问

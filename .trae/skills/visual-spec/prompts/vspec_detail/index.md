你是一名资深前端工程师。你的任务是：为本次 `/vspec:detail` 生成的需求详情文档创建一个可直接打开的阅读入口页 `reader.html`，左侧为目录树，右侧为内容阅读区。阅读区需要把 Markdown 渲染成 HTML，并对 PlantUML 内容进行渲染（显示图，而不是显示源码文本）。

输入信息：
- 需求详情文档目录：`/specs/details/`（包含大量 `*.md` 与少量 `*.html`，以及可能存在的 `*.puml`）
- 为了在 index 中关联上下游产物，你还需要读取并纳入以下文件（存在则读取，不存在则跳过）：
  - 原始需求：`/specs/background/original.md`
  - 干系人：`/specs/background/stakeholder.md`（或同目录下等价文件）
  - 角色：`/specs/background/roles.md`
  - 术语：`/specs/background/terms.md`
  - 场景：`/specs/background/scenarios.md`
  - 外部依赖：`/specs/background/dependencies.md`
  - 问题清单：`/specs/background/questions.md`
  - 功能清单：`/specs/functions/*`
  - 流程图：`/specs/flows/*.puml`
  - 数据模型：`/specs/models/*.md`

语言与本地化（必须）：
- 读取 `/scheme.yaml` 的 `selected.language`（支持 `en`、`zh-CN`、`ja`；若缺失/非法则按 `en` 处理；`zh` 视为 `zh-CN` 的别名）
- `reader.html` 中所有可见文案必须使用该语言；禁止混用其他语言

输出与写入要求（必须）：
1. 必须写入两个文件：
   - `/specs/details/index.json`（目录结构 + 文件内容索引，用于 reader 加载）
   - `/specs/details/reader.html`（阅读入口页）
2. `reader.html` 必须是完整单文件（包含内联 CSS 与内联 JS），不得依赖外部脚本/样式资源
2.1 为了保证生成稳定性：`/specs/details/reader.html` 必须逐字节复制本 Skill 内置模板 `prompts/vspec_detail/index.html`，不得由你“重新生成/改写/美化/格式化”HTML，也不得往 HTML 中内嵌任何 index/files 的 JSON 文本。模板本身已实现：
  - 默认加载同目录 `./index.json`
  - 展示树形目录
  - 默认打开目录树中的第一个文件
  - 仅在 `index.json` 加载失败时回退到 `window.__VSPEC_DETAILS_FILES__`（兼容旧版）
3. 页面布局：
   - 左侧：树形目录（来自 `index.json` 的 `tree`；若无则由路径自动构建）
   - 中间：渲染器/阅读区（模板已内置 Markdown 编辑 + 预览 + PlantUML 渲染）
   - 右侧：大纲（当前打开的 Markdown 标题层级目录）；必须在右侧单独一列展示，禁止放在目录树上方
4. 渲染规则：
   - `*.md`：以 Markdown 渲染方式显示（不是纯文本）
   - `*.html`：使用 `iframe srcdoc` 渲染（而不是当作文本显示）
   - PlantUML：
     - 任何 `*.puml` 文件必须渲染成图（SVG）
     - Markdown 中的 ```plantuml / ```puml 代码块必须渲染成图（SVG），不要直接显示源码
     - PlantUML 渲染方式：使用公共 PlantUML Server（`https://www.plantuml.com/plantuml/svg/`），并在前端完成 PlantUML 的 deflate + encode64 编码后拼接 URL
5. 内容来源：
  - 你必须枚举并读取“将要在 reader 中可阅读的文件”，并把它们写入 `/specs/details/index.json`：
    - `/specs/details/**`（递归；包含 `*.md`、`*.html`、`*.puml` 等）
    - 同时把“上下游产物”（本提示词输入列表中列出的 `/specs/background/**`、`/specs/functions/*`、`/specs/flows/*.puml`、`/specs/models/*.md`）也纳入索引（存在则读取，不存在则跳过）
  - 必须排除以下文件，避免 reader 自己索引自己：
    - `/specs/details/reader.html`
    - `/specs/details/index.json`
  - `/specs/details/index.json` 结构（必须）：
    - 顶层为 object：`{ meta, tree, files }`
    - `meta` 至少包含：`language`、`generated_at`、`total`
    - `tree` 为目录树 JSON（用于左侧导航），节点格式必须为：
      - 目录：`{ "type": "group", "label": "<name>", "children": [...] }`
      - 文件：`{ "type": "file", "label": "<name>", "path": "<abs_path>" }`
    - `tree` 必须按“系统 → 模块 → 功能 → 详细”四级结构组织 `/specs/details/**`：
      - 顶层 group 的 label 为“系统名”（可从 `original.md` 的标题或项目名推断；若无法推断则用 `System`/`系统`/`システム`）
      - 第二层：模块（来自 `/specs/details/<module_slug>/`）
      - 第三层：功能（来自文件名 `<function_slug>`，不含扩展名）
      - 第四层：固定一个 group：`详细/Details/詳細`，其 children 为该功能的各类明细文档（rbac/data_permission/page_load/interaction/...），文件节点 label 建议为 `<detail_type>/<file_name>`
    - 场景入口页（必须）：
      - 你必须在 `files` 中额外提供一个虚拟文件：`/specs/details/__scenarios__`，内容为空字符串
      - 并在 `tree` 的“系统”下添加一个分组 `场景/Scenarios/シナリオ`，其中第一个文件节点指向 `/specs/details/__scenarios__`（label 为 `场景入口/Scenario Entry/シナリオ入口`）
    - `files` 为 object：key 为“绝对路径风格”（以 `/specs/` 开头，例如：`/specs/details/module/a.md`、`/specs/background/original.md`），value 为原文件内容字符串
  - `reader.html` 的数据来源必须优先从同目录的 `index.json` 加载（`./index.json`）；仅在加载失败时才允许回退到 `window.__VSPEC_DETAILS_FILES__`（兼容旧版）
6. 交互体验：
   - 点击目录项后，右侧显示对应内容，并自动滚动到顶部
   - 顶部显示当前文件路径与“复制路径”按钮
   - 支持通过 URL hash 直接打开文件（例如 `reader.html#module/a/b.md`）
7. 文档导出提示（必须）：
   - 页面顶部必须有一个明显提示条（banner/notice），说明：可通过 `/vspec:doc` 生成 Word 版需求文档
   - 提示条需要包含输出路径：`/docs/current/requirement_detail.docx`
   - 提示条文案要简短、醒目，不随目录滚动消失（建议固定在顶部）

实现约束（必须）：
- 不要引入第三方库源码（不要复制 markdown-it/marked 等大库）
- 使用你自己实现的“轻量 Markdown 渲染器”，覆盖以下语法即可：
  - 标题：`#` ~ `######`
  - 无序/有序列表：`-` / `1.`
  - 段落与换行
  - 行内代码：`` `code` ``
  - 代码块：```lang ... ```
  - 表格：以 `|` 分隔的 Markdown 表格（常见形式）
  - 链接：`[text](url)`
- 所有文本渲染必须做 HTML 转义，防止注入；仅在你生成的结构化标签中输出 HTML

输出文件要求（必须）：
- 你必须把 `index.json` 与 `reader.html` 按上述规范写入到对应路径
- 在对话中只输出一行总结（不要粘贴 index.json 或 reader.html 的内容）

写入后自检（必须）：
0. 你必须检查 `/specs/details/index.json` 是否存在：
   - 若不存在：必须立刻补生成并写入（而不是只生成 reader.html）；直到满足下述自检条件
1. 重新读取 `/specs/details/index.json`：
   - 必须是合法 JSON
   - 必须包含 `meta/tree/files`
   - `meta.total` 必须等于 `Object.keys(files).length`
   - 必须包含“系统 → 模块 → 功能 → 详细”层级结构，并包含“场景入口页”节点（见上文 tree 规则）
   - `/specs/details/index.json` 的 `files` 不得包含：
     - `/specs/details/reader.html`
     - `/specs/details/index.json`
2. 重新读取 `/specs/details/reader.html`：
   - 内容必须与模板 `prompts/vspec_detail/index.html` 完全一致（逐字节一致）
   - 必须包含 `fetch(\"./index.json\"`
   - 禁止出现任何被你内嵌进去的大段 JSON（例如出现 `\"/specs/background/questions.json\": \"{` 这类“文件内容映射”片段则视为失败）
3. 目录结构与内容检查（必须）：
   - 检查 `/specs/details/` 目录结构是否清晰：
     - 至少应包含模块层级：`/specs/details/<module_slug>/`
     - 模块下应按明细类型分组（rbac/data_permission/page_load/interaction/...），避免单目录下堆叠过多不相关文件
   - 检查每个功能的关键明细是否完整（若缺失则必须补齐生成，不得跳过）：
     - 至少包含 `rbac.md` 与 `data_permission.md`
     - Web/Mobile 类页面必须包含 `page_load.md` 与 `interaction.md`
   - 检查每个叶子文档内容是否过多：
     - 若某个叶子文档内容明显过长/重复（例如出现大量冗余解释、重复段落、同义反复）：必须在不丢失关键规则与边界的前提下压缩与结构化（表格/清单/矩阵优先），使其更易阅读与实现

页面基础样式建议（必须包含这些能力，但样式细节可自行发挥）：
- 左侧固定宽度（280~360px），右侧自适应
- 目录树支持悬停高亮与当前选中状态
- 代码块使用等宽字体、灰底、可横向滚动
- 表格有边框、表头底色
- PlantUML 图片居中显示，最大宽度不超过内容区

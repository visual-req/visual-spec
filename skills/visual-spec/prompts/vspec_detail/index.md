你是一名资深前端工程师。你的任务是：为本次 `/vspec:detail` 生成的需求详情文档创建一个可直接打开的阅读入口页 `index.html`，左侧为目录树，右侧为内容阅读区。阅读区需要把 Markdown 渲染成 HTML，并对 PlantUML 内容进行渲染（显示图，而不是显示源码文本）。

输入信息：
- 需求详情文档目录：`/specs/details/`（包含大量 `*.md` 与少量 `*.html`，以及可能存在的 `*.puml`）

输出与写入要求（必须）：
1. 只写入一个文件：`/specs/details/index.html`
2. HTML 必须是完整单文件（包含内联 CSS 与内联 JS），不得依赖外部脚本/样式资源
3. 页面布局：
   - 左侧：目录树（按 `/specs/details/` 的目录结构分组；支持展开/收起；支持搜索过滤）
   - 右侧：阅读窗口（支持标题、列表、表格、代码块等基础 Markdown 渲染）
4. 渲染规则：
   - `*.md`：以 Markdown 渲染方式显示（不是纯文本）
   - `*.html`：使用 `iframe srcdoc` 渲染（而不是当作文本显示）
   - PlantUML：
     - 任何 `*.puml` 文件必须渲染成图（SVG）
     - Markdown 中的 ```plantuml / ```puml 代码块必须渲染成图（SVG），不要直接显示源码
     - PlantUML 渲染方式：使用公共 PlantUML Server（`https://www.plantuml.com/plantuml/svg/`），并在前端完成 PlantUML 的 deflate + encode64 编码后拼接 URL
5. 内容来源：
   - 由于浏览器无法直接读取本地文件系统，必须在 `index.html` 内嵌本次生成的 `/specs/details/**` 文件内容
   - 你必须枚举 `/specs/details/` 下的所有文件（递归），将其内容以 JSON 的形式内嵌进页面（键为相对路径，例如 `module/a/b.md`；值为原文件内容字符串）
6. 交互体验：
   - 点击目录项后，右侧显示对应内容，并自动滚动到顶部
   - 顶部显示当前文件路径与“复制路径”按钮
   - 支持通过 URL hash 直接打开文件（例如 `index.html#module/a/b.md`）

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
- 你必须直接把完整 HTML 写入 `/specs/details/index.html`
- 在对话中只输出一行总结（不要粘贴完整 HTML）

页面基础样式建议（必须包含这些能力，但样式细节可自行发挥）：
- 左侧固定宽度（280~360px），右侧自适应
- 目录树支持悬停高亮与当前选中状态
- 代码块使用等宽字体、灰底、可横向滚动
- 表格有边框、表头底色
- PlantUML 图片居中显示，最大宽度不超过内容区

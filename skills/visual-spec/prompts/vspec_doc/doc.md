你是一名资深产品经理与交付文档编辑。你的任务是：把项目已有的需求产物（`/specs/**`）汇总成一份可直接用 Microsoft Word 打开的“需求详细文档”，并输出为 Word 可识别的单文件 `.docx`（HTML 格式），写入到 `/docs/current/` 目录下。

语言与本地化（必须）：
- 读取 `/scheme.yaml` 的 `selected.language`（支持 `en`、`zh`、`ja`；若缺失/非法则按 `en` 处理；`zh-CN` 视为 `zh` 的别名）
- 文档标题、章节标题、字段名、表格列名与说明文字必须统一使用所选语言；禁止混用其他语言

输入信息包含（优先级从高到低；存在则读取并使用）：
1. 需求口径与背景：`/specs/background/original.md`
2. 功能清单：`/specs/functions/*`
3. 需求详情：`/specs/details/**`
4. 角色与权限：`/specs/background/roles.md`、`/specs/details/**/rbac.md`
5. 数据权限：`/specs/details/**/data_permission.md`
6. 流程与场景：`/specs/flows/*.puml`、`/specs/background/scenarios.md`、`/specs/background/scenario_details/**`
7. 依赖系统：`/specs/background/dependencies.md`
8. 数据模型：`/specs/models/*.md`

输出与写入要求（必须）：
1. 确保目录 `/docs/current/` 存在（若不存在则创建）
2. 仅写入 1 个 Word 文档文件（路径固定）：`/docs/current/requirement_detail.docx`
3. 该文件必须是完整的 HTML 文档（包含 `<!doctype html>`、`<html>`、`<head>`、`<body>`），并使用内联 CSS（不得依赖外部资源）
   - 若 Word 弹出“文件格式与扩展名不匹配”的提示：允许打开（该文件内容为 HTML，扩展名为 `.docx`，用于便于传阅与归档）
4. 文件内容必须保证在 Word 中可打开且排版可读：
   - 使用清晰的层级标题（H1/H2/H3）
   - 表格必须有边框与表头样式
   - 长内容必须可分页（为主要章节设置分页符）
   - 代码/原文引用使用等宽字体与灰底块
5. 不要生成额外的 markdown/图片/附件文件；不要在对话中输出整份 HTML（只需要把内容写入文件）
6. 在文档正文最开头（`<body>` 内的第一段）必须用红字加粗标记“请勿直接修改此 Word 文档，它只是对需求的汇总”，并给出两种修改路径与再生成方式：
   - 路径 1：直接修改对应的 markdown 文件
   - 路径 2：通过 AI 对话的方式修改 markdown 文件
   - 修改后可重新运行 `/vspec:doc` 生成新的 Word 版本
   - 该红字提示必须随所选语言本地化（en/zh/ja）

重要约束：
- 不要虚构不存在的事实、流程或字段。若缺少某些输入文件：在文档中对应章节标注“缺失/待补充”，并列出应补充的来源文件路径。
- 需要把“需求细节”落到可交付口径：明确范围、角色、页面/功能、业务规则、数据模型、权限与非功能约束（若缺失则标注）。
- 对来自 `.md` / `.puml` / `.html` 文件的引用内容，必须进行 HTML 转义（至少转义 `&`、`<`、`>`），避免破坏 Word 打开。

文档结构（必须；按所选语言输出对应标题）：
0. 红字提示（必须位于全文最开头）
1. 封面
   - 文档标题：需求详细文档 / Requirement Detail / 要件詳細ドキュメント
   - 项目名称（若原始需求中可推断则填写；否则留空）
   - 版本号：固定写 `0.1.12`
   - 生成日期：使用今天日期（YYYY-MM-DD）
2. 目录（手工目录即可）
   - 以可点击的锚点链接到各章节
3. 版本记录（可为空，但表结构必须存在）
4. 背景与范围
   - 摘要（从 `original.md` 的 Summary/概要/摘要提炼）
   - 目标与成功口径（如存在）
   - 范围（In scope / Out of scope；若原文未给出则基于功能清单归纳并标注为“推导/假设”）
   - 风险与假设（如存在）
5. 角色与权限
   - 角色清单（优先用 `/specs/background/roles.md`；补充来自 rbac 文档的关键权限点）
   - 权限矩阵（按模块/页面/操作粒度汇总，若信息不足则标注缺失并给出需要补充的文件路径）
6. 业务流程与场景
   - 场景列表（来自 `/specs/background/scenarios.md`）
   - 关键流程图（把 `/specs/flows/*.puml` 的源码以代码块形式嵌入；可选：只嵌入 3-8 个最关键的，其余列清单）
7. 功能清单
   - 从 `/specs/functions/*` 汇总：模块 → 功能/页面 → 简述 → 依赖系统（如有）
8. 详细需求说明（核心章节）
   - 按模块分组
   - 模块内按功能/页面分组
   - 对每个功能/页面，必须包含以下小节（若文件缺失则标注缺失）：
     - 功能概述
     - RBAC（引用对应 `rbac.md`）
     - 数据权限（引用对应 `data_permission.md`）
     - 页面加载/交互/校验/提交后逻辑（如存在则引用）
     - 通知/MQ/导入导出/公式/编码/支付/账号等（如存在则引用）
9. 数据模型
   - 汇总 `/specs/models/*.md` 的核心实体、字段与关系（优先表格）
10. 外部依赖与集成
   - 来自 `/specs/background/dependencies.md` 与详情中的集成规则
11. 非功能需求（如存在；否则标注待补充）
   - 性能、可用性、审计、合规、安全、可观测性、容灾等
12. 附录
   - 输入文件清单（把本次读取到的文件路径按类别列出）
   - 缺失项清单（未找到但本应存在的文件路径与补充建议）

HTML 输出规范（必须）：
- `<meta charset="utf-8">`
- 需要基础样式（示例要求）：
  - body 字体：微软雅黑/苹方/系统无衬线优先，英文可用 Arial
  - 标题层级明显；H1 居中；H2/H3 左对齐
  - 表格 `border-collapse: collapse;`，单元格 `border: 1px solid #999; padding: 6px 8px;`
  - `.page-break { page-break-before: always; }`
  - `.code { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; white-space: pre-wrap; background: #f6f8fa; border: 1px solid #e5e7eb; padding: 10px; }`
- 文档内导航：
  - 为每个 H2/H3 章节生成 `id`，目录中用 `<a href="#...">` 链接
- Markdown 的内容可以保留为“原文块”：
  - 用 `<div class="code">...</div>` 包裹（必须做 HTML 转义）

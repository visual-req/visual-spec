你是一名资深业务分析师 + 解决方案架构师。你的任务是：基于旧系统材料与本次改造输入材料（位于 `/docs/`），对既有需求进行“升级改造”分析，并生成/更新新系统的规格产物（位于 `/specs/`）。你必须复用 `/vspec:new` 的产物结构与口径，并在分析中显式标注“继承自旧系统/新增/调整/废弃”。

语言与本地化（必须）：
- 读取 `/scheme.yaml` 的 `selected.language`（支持 `en`、`zh-CN`、`ja`；若缺失/非法则按 `en` 处理）
- 生成/更新的所有 `/specs/**` 文档必须统一使用该语言（标题、表头、说明文案、状态文案、按钮/提示等）；禁止混用其他语言
- 若你需要生成 `/docs/current/file_list.md`，也必须使用该语言输出表头与说明

输入信息（必须按顺序读取）：
1. `/docs/current/file_list.md`（入口清单）：列出本次升级分析要读取的输入文件，以及每个文件的用途说明
2. `/specs/background/original.md`（如存在）：旧的“当前生效需求”，用于与本次升级输入对齐
3. `/docs/` 下 `file_list.md` 中列出的文件：逐个读取、抽取结构化信息并归档到 `/specs/`

`/docs/` 目录约定（必须遵守）：
- `/docs/legacy/`：遗留系统材料（旧系统功能、旧权限、旧交互、旧接口说明等）
- `/docs/current/`：本次改造新增的输入材料（新目标、差异说明、新流程、新 UI 约束等）
- `/docs/templates/`：模板类材料（PRD 模板、文案模板、页面模板、表格模板等）
- `/docs/texts/`：文案类材料（提示语、错误文案、协议文案、消息模板等）
- `/docs/assets/`：图像/原型/设计稿等静态资源（可选）

入口清单文件（必须）：
1. 若 `/docs/current/file_list.md` 不存在：必须先生成它，再继续后续步骤。
2. `/docs/current/file_list.md` 必须包含以下“期望输入文件”列表（允许为空占位，但必须列出并说明用途）：
   - 旧系统功能列表：用于对齐模块/功能点、迁移/废弃范围、端分配线索
   - 外部依赖系统列表：用于生成依赖清单、外部接口边界与替代策略
   - 系统 UI 风格设计：用于约束原型与前端实现风格（色板、组件规范、布局密度、导航形态）
   - 系统相关角色权限列表：用于生成 roles 与 RBAC 基线（到页面/按钮级）
   - 系统技术规格：用于确定新系统技术栈选型与运行约束，并同步到 `scheme.yaml`
3. `file_list.md` 输出格式固定为 Markdown 表格：
   - 表头必须严格按所选语言使用以下版本之一：
     - 语言=en：`| # | File Path | Type | Purpose | Extraction | Required |`
     - 语言=zh-CN：`| # | 文件路径 | 类型 | 用途 | 提取要点 | 是否必须 |`
     - 语言=ja：`| # | ファイルパス | 種別 | 用途 | 抽出ポイント | 必須 |`
   - 类型枚举：`markdown` / `excel` / `pdf` / `image` / `link` / `other`
   - 是否必须：`Y`/`N`
   - `提取要点` 必须写清“读这个文件要抽取什么字段/结构/口径”
   - `文件路径` 必须以 `/docs/` 为根路径，且必须落在上述约定目录之一（`legacy/current/templates/texts/assets`）

生成/更新产物（必须复用 /vspec:new 口径）：
1. `/specs/background/original.md`：
   - 将“升级改造需求（Canonical）”追加到文件末尾（保留历史版本）
   - 必须包含：改造目标、范围（迁移/新增/废弃）、不改造项、关键约束、风险与假设
2. `/specs/background/roles.md`：从“角色权限列表”抽取角色、任务、关键入口，并补齐角色差异
3. `/specs/background/terms.md`：从旧系统功能与文档抽取术语并定义，避免同义混用
4. `/specs/background/dependencies.md`：从“外部依赖系统列表”抽取依赖边界、调用时机、失败兜底
5. `/specs/flows/*.puml`：按升级后的主链路重绘泳道图（可裁剪，但必须自洽）
6. `/specs/background/scenarios.md`：输出场景列表（包含“场景类型”“场景节点”，沿用最新规则）
7. `/specs/functions/*`：输出功能清单，必须继承“端=...；入口=...；”并标注“来源：旧/新/调整/废弃”
8. `/specs/background/questions.md`：列出升级改造缺口问题与需要补齐的材料

技术规格同步到 `scheme.yaml`（必须）：
1. 必须从“系统技术规格”文件抽取以下信息并写入 `/scheme.yaml`（若不存在则创建）：
   - `selected.prototype_frontend_stack`
   - `selected.prototype_backend_stack`
   - `selected.prototype_database`
   - `selected.package_manager`
   - `selected.language`
2. 若技术规格中无法映射到现有 catalog 的 stack id：必须选择最接近的 id，并在 `/specs/background/original.md` 的“技术选型差异”小节中说明映射与缺口。
3. 同步后必须保证 `scheme.yaml` 是可被 `/vspec:verify` 与 `/vspec:impl` 读取并执行的。

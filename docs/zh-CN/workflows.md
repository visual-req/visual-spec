## 工作流

### 1. 需求分析（`/vspec:new`）

- 输入原始需求
- 回答开放问题（关键假设、范围、规则、依赖）
- 在 `/specs/` 下得到第一版产物：角色、术语、流程、场景、功能清单、依赖、问题清单
- 提问回答（HTML 方式，推荐）：
  - `/vspec:new` 会生成交互式问答页：`/specs/background/question_and_answer.html`
  - 打开该 HTML 后，分别选择：
    - `/specs/background/original.md`
    - `/specs/background/questions.md`
  - 在页面里用表单回答问题并保存回写（浏览器支持写入时可直接覆盖写回；否则下载后手动替换）

### 2. 补充问题（`/vspec:more-q`）

- 适用场景：问题清单还不够，或需求发生变更，需要补充更多“待确认问题”
- 输入：`/specs/background/questions.md`（不存在则先 `/vspec:new`）
- 输出：追加写入 `/specs/background/questions.md`（新增问题 + 回答指引）
- 提问回答（HTML 方式，推荐）：
  - `/vspec:more-q` 会更新/生成交互式问答页：`/specs/background/question_and_answer.html`
  - 打开该 HTML，用表单继续回答新增问题，保存回写后再执行 `/vspec:refine-q`

### 3. 合并问答（`/vspec:refine-q`）

- 适用场景：业务已在 `/specs/background/questions.md` 填写答案，需要合并回需求并形成新口径
- 输入：`/specs/background/questions.md`（已回答项）+ `original.md`
- 输出：追加更新到 `/specs/background/original.md`（采纳项 + 变更清单 + 最新口径）

### 4. 应用补充材料（`/vspec:refine`）

- 适用场景：实现中出现新信息/澄清，需要更新需求口径并同步更新详情与原型，且保留可追溯性
- 输入：
  - 默认：`/docs/refine/*`（优先 `file_list.md`）
  - 可选：命令参数指定文件/目录
- 前置条件：`/specs/details/` 必须存在且非空
- 输出：追加更新到 `original.md` + 更新受影响的 `/specs/details/` 与 `/specs/prototypes/`

### 5. 详细规格（`/vspec:detail`）

- 以 `/specs/functions/*` 为输入，在 `/specs/details/<function_slug>/` 下生成单功能规格
- 目标：把“需求”转成可实现的设计输入：
  - RBAC 到控件级 + 数据权限
  - 加载/交互/校验矩阵
  - 提交后检查/处理/跳转
  - 日志/通知矩阵、MQ、导入导出、定时任务
- 额外输出：`/specs/details/index.html`（左侧目录树 + 右侧 Markdown 渲染阅读；PlantUML 渲染为图）

### 6. Word 汇总文档（`/vspec:doc`）

- 适用场景：把当前已有的规格产物汇总成可交付的 Word 文档，用于评审/流转/归档
- 输入：现有 `/specs/**` 产物（original/functions/details/models/flows 等，存在则读取）
- 输出：`/docs/current/requirement_detail.docx`（Word 可打开的 `.docx`，HTML 单文件）
- 提示：该 Word 只是汇总，不建议直接修改；修改应回到对应的 markdown 文件，修改后重新 `/vspec:doc` 生成新版本

### 7. 方案验证（`/vspec:verify`）

- 前置条件：`/specs/details/` 存在且非空
- 基于 `/specs/`（functions + details + roles）生成：
  - `/specs/models/*.md`：实体与字段、关系、状态机、索引、外部字段来源
  - `/specs/prototypes/`：按 `scheme.yaml` 选栈生成可运行原型，以及 `scenario.html` 场景评审页
- 目标：尽早暴露理解偏差，尽快收敛到可评审方案

可选：分段生成原型

- 原型很大或希望按流程更细粒度控制时，可按阶段增量生成：
  - `/vspec:proto-apply`：申请流页面 + 工作台差异
  - `/vspec:proto-approve`：审批流页面 + 工作台差异
  - `/vspec:proto-execute`：执行流页面（包含移动端 `/m/*`）
  - `/vspec:proto-crud`：配置/主数据 CRUD 管理页

### 8. 验收用例（`/vspec:accept`）

- 在 `/specs/acceptance/` 下生成验收用例
- 目标：定义验收口径与覆盖范围（主流程、异常、边界、RBAC、数据权限）

### 9. 自动化测试（`/vspec:append-test`）

- 读取验收用例与仓库现有测试技术栈
- 生成最小可运行的一组 E2E/API/单测
- Note：该步骤只生成/补齐测试代码以提升覆盖率，不负责执行测试命令（例如 mvn test）。

### 10. 集成实现（`/vspec:impl`）

- 读取 specs、details、models、dependencies
- 按仓库约定生成后端 + 前端联调代码（API 合同 → 后端实现 → 前端对接）

### 11. 质量检查（`/vspec:qc`）

- 对 `/specs/` 下产物做质量检查
- 输出：`/specs/qc_report.md`

### 12. 估算与排期（`/vspec:plan`）

- 把功能与场景拆成用户故事，估算工作量，并生成迭代排期
- 输出：
  - `/specs/plan/plan_estimate.md`
  - `/specs/plan/plan_schedule.html`

### 13. 升级/改造（`/vspec:upgrade`）

- 适用场景：基于遗留系统材料做“升级/重构/迁移”分析，继承必要部分并生成新规格
- 入口清单：`/docs/current/file_list.md`（缺失时生成模板）
- 输出：生成/更新 `/specs/`（沿用 `/vspec:new` 结构）+ 同步技术选型到 `/scheme.yaml`

### 14. MRD 分析包（`/vspec:mrd`）

- 输出市场/竞品/用户/产品设计分析包
- 输出目录：`/docs/market/`（market/competitors/users/product_design）

## 独立使用质量规范（不依赖 `/vspec:qc`）

内置质检标准文件位于（任选其一，取你当前环境中存在的路径）：
- Skill 根目录下：`/prompts/vspec_qc/quality_standard.md`
- 本仓库源码路径：`skills/visual-spec/prompts/vspec_qc/quality_standard.md`

你可以把它作为“通用需求质检标准”，独立用于检查其他方式写出来的需求文档（不要求必须由 `/vspec:*` 生成）。

以 DeepSeek 聊天窗口为例（其他大模型/聊天产品同理）：
1. 上传 2 份文件：
   - `quality_standard.md`（质检标准）
   - 你的需求文档（例如 PRD/需求说明/功能规格）
2. 在聊天窗口输入以下指令：

   请按照质量标准对需求文档进行质量检查，并生成质量检查结果的表格。

建议输出表格列（可选）：
- 检查项编号
- 检查项标题
- 是否通过（是/否/部分）
- 发现的问题摘要
- 涉及的文档位置（章节/段落）
- 修复建议

## 安装（skills.sh）

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

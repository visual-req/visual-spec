## 工作流

### 1. 需求分析（`/vspec:new`）

- 输入原始需求
- 回答开放问题（关键假设、范围、规则、依赖）
- 在 `/specs/` 下得到第一版产物：角色、术语、流程、场景、功能清单、依赖、问题清单

### 2. 详细规格（`/vspec:detail`）

- 以 `/specs/functions/*` 为输入，在 `/specs/details/<function_slug>/` 下生成单功能规格
- 目标：把“需求”转成可实现的设计输入：
  - RBAC 到控件级 + 数据权限
  - 加载/交互/校验矩阵
  - 提交后检查/处理/跳转
  - 日志/通知矩阵、MQ、导入导出、定时任务

### 3. 方案验证（`/vspec:verify`）

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

### 4. 验收用例（`/vspec:accept`）

- 在 `/specs/acceptance/` 下生成验收用例
- 目标：定义验收口径与覆盖范围（主流程、异常、边界、RBAC、数据权限）

### 5. 自动化测试（`/vspec:append-test`）

- 读取验收用例与仓库现有测试技术栈
- 生成最小可运行的一组 E2E/API/单测
- Note：该步骤只生成/补齐测试代码以提升覆盖率，不负责执行测试命令（例如 mvn test）。

### 6. 集成实现（`/vspec:impl`）

- 读取 specs、details、models、dependencies
- 按仓库约定生成后端 + 前端联调代码（API 合同 → 后端实现 → 前端对接）

### 7. 估算与排期（`/vspec:plan`）

- 把功能与场景拆成用户故事，估算工作量，并生成迭代排期
- 输出：
  - `/specs/plan/plan_estimate.md`
  - `/specs/plan/plan_schedule.html`

## 安装（npm）

- 推荐在目标项目根目录安装：`npm install <git-url>`
- 安装后 Skill 会被复制到：`<your-project>/.trae/skills/visual-spec-skill/`
- 需要时可手动安装：`npx vspec --force`

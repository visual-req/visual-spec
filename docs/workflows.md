## 工作流程

### 0. 准备

- 在你的项目根目录（包含 `.trae/`）安装该 skill
- 确保 `.trae/skills/starter-skill/` 已出现在项目内（安装方式见下方“安装”）

### 1. 需求分析（/vspec:new）

- 输入原始需求
- 回答待确认问题（关键假设、范围、规则、依赖）
- 得到 `/specs/` 下基础规格产物：角色/术语/流程/场景/功能清单/依赖/问题清单

### 2. 方案验证（/vspec:verify）

- 基于 `/specs/` 产物生成：
  - `/specs/models/*.md`：实体与字段、关系、状态机、索引、外部字段来源
  - `/specs/prototypes/`：Vue + Ant Design Vue 原型与 `scenario.html` 场景确认页
- 目标：尽早暴露理解偏差，收敛到可评审方案

补充：原型分段生成（可选）

- 当原型规模较大或希望更可控地按链路落地时，可改用拆分命令增量生成：
  - `/vspec:proto-apply`：聚焦申请链路页面与工作台差异
  - `/vspec:proto-approve`：聚焦审批链路页面与工作台差异
  - `/vspec:proto-execute`：聚焦执行链路页面（含移动端 `/m/*`）
  - `/vspec:proto-crud`：聚焦配置/主数据类 CRUD 管理页

### 3. 细节梳理（/vspec:detail）

- 以 `/specs/functions/*` 为输入，逐功能点输出 `/specs/details/<function_slug>/`
- 目标：把“需求”变成可实现的设计输入：
  - 权限（RBAC 到控件级）与数据权限
  - 加载/交互/校验矩阵
  - 提交后检查/处理/跳转
  - 日志矩阵/通知矩阵/MQ 规格/导入导出/定时任务

### 4. 验收用例（/vspec:accept）

- 生成验收用例到 `/specs/acceptance/`
- 目标：明确验收口径与覆盖范围（主流程/异常/边界/权限/数据权限）

### 5. 自动化测试（/vspec:test）

- 读取验收用例与仓库现有测试框架
- 生成最小可运行的 E2E/API/单元测试集合

### 6. 集成开发（/vspec:impl）

- 读取规格、细节、模型与依赖
- 按仓库现有技术栈与约定生成前后端集成代码（接口契约 → 后端实现 → 前端集成）

### 7. 排期规划（/vspec:plan）

- 从功能与场景拆成用户故事，估算人天并按迭代排期
- 输出：
  - `/specs/plan.md`
  - `/specs/story_map.html`（用户故事地图）

### 8. 变更响应（/vspec:change）

- 输入变更描述
- 输出影响分析与变更日志，并同步更新受影响产物与用例

## 安装（npm）

- 推荐在你的项目根目录执行：`npm install <git-url>`
- 安装完成后会将 skill 复制到：`<你的项目>/.trae/skills/starter-skill/`
- 如需手动执行安装：`npx vspec --force`

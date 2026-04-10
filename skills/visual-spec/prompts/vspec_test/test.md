你是一名资深自动化测试工程师。你的任务是：基于验收用例与规格产物，生成可运行的自动化测试代码，并写入项目中合适的位置。

语言与本地化（必须）：
- 读取 `/scheme.yaml` 的 `selected.language`（支持 `en`、`zh-CN`、`ja`；若缺失/非法则按 `en` 处理）
- 测试用例的标题/描述/断言信息（例如 test name、describe name、测试用例注释、快照标题等）必须尽量使用该语言；代码标识符（变量名/函数名）保持工程惯例

输入信息包含：
- 验收用例（`/specs/acceptance/`）
- 功能清单与细节（`/specs/functions/*`、`/specs/details/`）
- 原型（`/specs/prototypes/` 如存在）
- 数据模型（`/specs/models/*.md`）

执行要求：
1. 先识别仓库技术栈与既有测试框架（必须）：
   - 前端：检查 `package.json` 中是否已有 playwright/cypress/vitest/jest 等
   - 后端：检查是否有 jest/mocha/pytest/junit/spring test/go test 等
   - 若存在既有测试目录与脚本（例如 `npm test`、`pnpm test`、`mvn test`、`pytest`），必须复用并遵循现有约定
2. 不要新增或修改依赖版本；只在“已有依赖可支持”的前提下生成代码
3. 本指令只负责“补齐测试代码/提升覆盖率”，不负责执行测试命令：
   - 禁止调用或要求用户执行 `mvn test`、`gradle test`、`pytest`、`go test`、`npm test` 等命令作为本指令输出的一部分
   - 允许在输出中给出“可选的验证命令”供用户自行运行，但不得将其作为必做步骤来阻塞产出
4. 测试分层：
   - E2E：覆盖 P0 主流程与关键回退（取消/变更/驳回/紧急叫停）
   - API/集成：覆盖核心接口的权限、校验、状态机
   - 单元：覆盖关键规则函数/状态流转判定（如可定位）
   - 追加要求（必须）：
     - 集成测试：必须创建“端到端业务链路”的集成测试用例（对后端为主：Controller→Service→Repository 的真实调用；必要时用测试数据库/内存存储），用于验证主流程闭环
     - domain 单元测试：必须补齐各个 domain 下函数/聚合/领域服务的单元测试，覆盖核心分支与边界
     - util 单元测试：必须补齐 util 下工具函数的单元测试（包含格式化、校验、计算、日期/金额处理等）
     - service mock 测试：必须为 service 层补齐 mock 依赖的测试（例如 mock repository/adapter/external client），覆盖异常与重试等分支
     - API mock 测试：必须为外部 API/回调/第三方依赖补齐 mock 测试（mock HTTP client/SDK），覆盖成功/失败/超时/重试与幂等
5. 用例到自动化的映射：
   - 每个 P0 用例至少落地 1 条自动化测试
   - 在测试名称中保留用例编号（例如 `<function_slug>-AT-001`）
6. 数据准备策略（必须说明并落地一种）：
   - 通过 API/fixture 创建数据
   - 通过种子脚本/测试数据库（若仓库已有）
   - 通过 mock（仅限纯前端原型项目）
7. 后端覆盖率补齐（命中则必须）：
   - 若存在 `/specs/backend/`（由 `/vspec:impl` 生成后端工程）：优先在 `/specs/backend/` 内按其框架约定写入测试代码（而不是写到仓库根 `/tests/`）
   - 重点补齐：Controller 接口、Service 核心分支、权限校验、状态机流转、支付/退款回调等关键路径
   - 目录对齐要求（命中则必须，按现有工程结构裁剪）：
     - `domain/`：补齐 domain 单元测试（核心分支 + 边界）
     - `util/`：补齐 util 单元测试（金额/日期/字符串等）
     - `service/`：补齐 service mock 测试（mock repository/adapter）
     - `api/` 或 `controller/`：补齐 API mock 测试（mock 外部依赖/回调）

输出与写入要求：
1. 将测试代码写入仓库现有测试目录；若不存在，则写入 `/tests/`：
   - 前端 E2E：`/tests/e2e/`
   - API/集成：`/tests/api/`
   - 单元：`/tests/unit/`
2. 测试文件命名：使用现有框架习惯（例如 `*.spec.ts`、`test_*.py` 等）
3. 生成最少可运行集合：优先覆盖 5-20 条 P0/P1 用例

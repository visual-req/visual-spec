# 复杂输入材料（Word/Excel 等）的归档与使用

当你的需求不是“一段文字”，而是多份原始材料（Word/Excel/PDF/流程图/截图/样例数据/协议等）时，建议把这些材料统一归档到 `/docs/`，并通过约定目录与清单文件让 Skill 能够稳定引用与复用。

## 1. `/docs/current/`：本次需求/迭代的原始材料

把“本次要分析的输入材料”放到 `/docs/current/`，并尽量保持结构清晰、可追溯、可复用。

推荐做法：
- 用子目录按来源/主题组织（可选）：`/docs/current/prd/`、`/docs/current/rules/`、`/docs/current/ui/`、`/docs/current/data/`、`/docs/current/api/`
- 文件名建议包含：来源、主题、版本或日期，例如：
  - `prd_v3_2026-04-12.docx`
  - `field_mapping_v1.xlsx`
  - `process_overview_v2.pdf`
  - `ui_screenshots_2026-04-12/`（多张截图可用目录）
- 如果你有“材料入口清单”，放在：`/docs/current/file_list.md`
  - `/vspec:upgrade` 会读取/生成该文件，并按清单顺序读取输入
  - 即使 `/vspec:upgrade` 会扫描 `/docs/legacy/`，你仍然应该在 `file_list.md` 中把“你认为最重要/最权威”的材料排在前面

常见材料放置建议：
- Word/Doc/PRD：放 `prd/` 或根目录，强调“口径优先级”
- Excel（字段口径、枚举、映射表、权限矩阵、接口清单）：放 `rules/` 或 `data/`
- PDF（历史说明/流程/合规材料）：放 `prd/` 或 `rules/`
- 截图/原型/设计稿：放 `ui/` 或 `assets/`
- 样例数据（CSV/JSON）：放 `data/`

## 2. `/docs/legacy/`：升级/重构场景的遗留系统材料

当你做的是“升级/重构/迁移”，遗留系统材料应该放在 `/docs/legacy/`（包含子目录）。例如：
- 旧系统功能说明、页面截图、交互说明
- 旧 RBAC/权限模型、数据权限口径
- 旧接口文档、事件/MQ 定义、对账规则
- 旧表结构/字段定义、枚举表、状态机

`/vspec:upgrade` 的用法要点：
- 会递归扫描 `/docs/legacy/` 及其子目录，把其中的文档当作原始输入资料
- 若发现 `/docs/current/file_list.md` 未覆盖的 legacy 文件，会先把它们追加进 `file_list.md`，再读取并参与抽取
- 你仍然可以通过 `/docs/current/file_list.md` 来“控制阅读顺序”和“强调哪些文件更权威”，避免被大量 legacy 资料淹没

## 3. `/docs/dependencies/`：外部依赖系统文档库

当你的需求依赖外部系统（例如 SSO/CRM/ERP/支付/消息/地图/库存等），建议把这些依赖系统的“稳定资料”沉淀到 `/docs/dependencies/`，作为长期复用的知识库。

推荐放入：
- 对方系统的接口说明、字段字典、错误码、鉴权方式
- 回调/事件/MQ 消息定义、签名校验、幂等规则
- 业务对账规则、结算口径、对接注意事项
- 版本更新记录与差异说明（如有）

与 `/docs/current/` 的区别：
- `/docs/current/`：本次迭代的输入（更可能频繁变动）
- `/docs/dependencies/`：依赖系统的“相对稳定资料”（用于多次迭代复用）

## 4. 推荐操作顺序（有多份材料时）

1. 把材料放入 `/docs/current/`（需要升级/重构则同时整理 `/docs/legacy/`）
2. 如材料较多：先整理 `/docs/current/file_list.md`（按“权威性/优先级”排序）
3. 运行 `/vspec:new`（生成 `/specs/background/original.md` 与问题清单）
4. 需要继承 legacy/当前材料并生成新 specs：运行 `/vspec:upgrade`
5. 需要汇总成 Word：运行 `/vspec:doc` 输出到 `/docs/current/requirement_detail.doc`

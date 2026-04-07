# 目录结构

本文描述目标项目中使用的目录结构：
- Skill 生成的 `/specs/` 产物树（需求/设计交付物）

## 目标项目布局

Skill 会按命令阶段逐步在 `/specs/` 下生成产物，并维护少量项目级配置与输入归档目录。典型目录结构如下：

```text
<your-project>/
├─ docs/                                  # 输入归档（/vspec:new 会创建）
│  ├─ legacy/                             # 遗留系统材料（功能、权限、交互、API 等）
│  ├─ current/                            # 本次迭代新增/补充材料（目标、差异、流程、UI 约束等）
│  │  └─ file_list.md                     # upgrade 入口清单（/vspec:upgrade 读取/生成）
│  ├─ change/                             # 变更输入归档（可选）
│  │  └─ file_list.md                     # 可选：有序输入清单
│  ├─ refine/                             # 补充/澄清输入（/vspec:refine 读取）
│  │  └─ file_list.md                     # 可选：有序输入清单
│  ├─ templates/                          # 模板（PRD/文案/UI/表格模板，可选）
│  ├─ texts/                              # 文案（提示语、错误信息、协议、消息模板，可选）
│  └─ assets/                             # 静态资源（设计稿、截图、原型图、图片等，可选）
├─ scheme.yaml                            # 原型选栈（/vspec:verify 使用；缺失时会生成默认值）
└─ specs/
   ├─ background/                         # 背景分析与共享材料
   │  ├─ original.md                      # 原始需求（或等价输入）
   │  ├─ stakeholders.md                  # 干系人
   │  ├─ roles.md                         # 角色与职责
   │  ├─ terms.md                         # 术语表
   │  ├─ scenarios.md                     # 场景清单
   │  ├─ scenario_details/                # 场景节点细化：pre_post.md/constraints.md/variations.md/boundaries.md/symmetry.md
   │  ├─ dependencies.md                  # 外部依赖
   │  └─ questions.md                     # 开放问题（verify 前必须解决或显式跳过）
   ├─ flows/                              # 流程图（PlantUML）
   │  └─ *.puml
   ├─ functions/                          # 功能清单（按模块拆分）
   │  └─ *.md
   ├─ details/                            # 单功能详细设计（/vspec:detail 输出）
   │  └─ <module_slug>/
   │     ├─ rbac/                         # RBAC
   │     ├─ data_permission/              # 数据权限
   │     ├─ page_load/
   │     ├─ interaction/
   │     ├─ validation_matrix/
   │     ├─ logging_matrix/
   │     ├─ notification_matrix/
   │     ├─ mq/
   │     ├─ nfp/                          # 非功能：性能/安全/兼容性/韧性/稳定性
   │     ├─ file_import/
   │     ├─ file_export/
   │     └─ cron_job/
   ├─ models/                             # 数据模型（/vspec:verify 输出）
   │  ├─ *.md
   │  └─ README.md
   ├─ prototypes/                         # 可运行原型 + 评审页（/vspec:verify 输出）
   │  └─ ...
   ├─ acceptance/                         # 验收用例（/vspec:accept 输出）
   │  ├─ index.md
   │  └─ ...
   ├─ qc_report.md                        # 质量报告（/vspec:qc 输出）
   ├─ plan/                               # 规划输出（/vspec:plan 输出）
   │  ├─ plan_estimate.md                 # 估算
   │  └─ plan_schedule.html               # 排期页面
   └─ change_log.md                       # 变更日志（可选）
```

说明：
- `docs/`：归档业务输入与交付对齐材料。建议使用 `legacy/current/change/refine/templates/texts/assets` 等子目录，并在文件名中包含来源/版本信息。
- `scheme.yaml`：选择 `/vspec:verify` 与 `/vspec:impl` 使用的技术栈与选项。读取顺序为项目根目录的 `scheme.yaml` 优先，其次 `/specs/scheme.yaml`。若都不存在则生成默认 `scheme.yaml`。

下一步：

- 阅读 `commands.md`，了解各 `/vspec:*` 命令的输入、输出与使用场景

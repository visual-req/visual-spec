# 目录结构说明

本文说明两类目录结构：
- 项目内 `/specs/` 产物目录结构：skill 在目标项目中生成的需求与设计产物


## 目标项目目录结构

skill 会在目标项目根目录生成 `/specs/` 产物（按命令阶段逐步补齐），并维护少量项目级配置与材料归档目录。典型结构如下：

```text
<your-project>/
├─ .trae/
│  └─ skills/
│     └─ starter-skill/                   # 安装后的 skill 目录（项目级或全局拷贝）
├─ docs/                                  # 需求材料归档目录（/vspec:new 自动创建）
│  └─ README.md                           # 目录用途说明（业务材料/模板/协议/文案/截图/样例数据等）
├─ scheme.yaml                            # 原型工程技术栈选择（/vspec:verify 使用；不存在会自动创建默认值）
└─ specs/
   ├─ background/                         # 背景分析与通用资料
   │  ├─ original.md                      # 原始需求（或等价输入）
   │  ├─ stakeholders.md                  # 干系人
   │  ├─ roles.md                         # 角色与任务
   │  ├─ terms.md                         # 术语表
   │  ├─ scenarios.md                     # 场景清单
   │  ├─ scenario_details/                # 场景细节（按节点拆分：每节点 pre_post.md/constraints.md/variations.md/boundaries.md/symmetry.md）
   │  ├─ dependencies.md                  # 外部依赖
   │  └─ questions.md                     # 待确认问题清单（进入 verify 前需清零未回答/允许跳过）
   ├─ flows/                              # 流程图（PlantUML）
   │  └─ *.puml
   ├─ functions/                           # 功能清单（按模块拆分）
   │  └─ *.md
   ├─ details/                             # 逐功能点的细节设计（/vspec:detail 输出）
   │  └─ <module_slug>/
   │     ├─ rbac/                          # 权限细化
   │     ├─ data_permission/               # 数据权限
   │     ├─ page_load/
   │     ├─ interaction/
   │     ├─ validation_matrix/
   │     ├─ logging_matrix/
   │     ├─ notification_matrix/
   │     ├─ mq/
   │     ├─ nfp/                           # 非功能性需求（性能/压测/安全/兼容/容错/稳定）
   │     ├─ file_import/
   │     ├─ file_export/
   │     └─ cron_job/
   ├─ models/                              # 数据模型（/vspec:verify 输出）
   │  ├─ *.md
   │  └─ README.md
   ├─ prototypes/                          # 原型工程与验证页（/vspec:verify 输出）
   │  └─ ...
   ├─ acceptance/                          # 验收用例（/vspec:accept 输出）
   │  ├─ index.md
   │  └─ ...
   ├─ qc_report.md                         # 质量检查报告（/vspec:qc 输出）
   ├─ plan_estimate.md                     # 估算（/vspec:plan 输出）
   ├─ plan_schedule.html                   # 排期页面（/vspec:plan 输出）
   └─ change_log.md                        # 变更日志（/vspec:change 输出）
```

补充说明：
- `docs/`：用于存放与本需求相关的业务材料与交付对齐资料，例如原始文档、流程说明、字段口径、模板/协议/文案、截图、样例数据等；建议按主题或日期建子目录并在文件名中体现来源与版本。
- `scheme.yaml`：用于指定 `/vspec:verify` 生成“可运行原型工程”时采用的技术栈与选项；优先读取项目根目录 `scheme.yaml`，若不存在才读取 `/specs/scheme.yaml`，两者都不存在则会创建默认的 `scheme.yaml`。

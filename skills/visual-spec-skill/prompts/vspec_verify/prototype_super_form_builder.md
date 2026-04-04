你是一名资深前端原型工程师。你的任务是：为“原型工程（/specs/prototypes/）”补齐“超级表单配置（表单搭建器）”页面，用于演示“字段拖拽/配置 → 预览 → 生成表单 Schema → 用 Schema 渲染填写页”的闭环。

路由（必须）：
1. Web：
   - 表单配置：`/tools/form-builder`（必须稳定可访问）
   - 表单预览：`/tools/form-preview`（必须稳定可访问）
2. Mobile（可选；用户明确需要移动端填写时才生成）：
   - 表单填写：`/m/form/:id`（至少保证 `/m/form/1` 可访问）

表单配置页（必须）：
1. 页面布局（必须，三栏）：
   - 左侧：字段库（Field Palette）
   - 中间：表单画布（Canvas，展示当前表单结构）
   - 右侧：属性面板（Properties，配置选中字段）
2. 字段库（至少 10 类控件）：
   - 文本输入、数字、金额、单选、多选、下拉选择、日期、日期范围、开关、上传（占位）、地址（占位）
3. 画布能力（必须可演示）：
   - 支持新增字段（点击添加即可，不要求真实拖拽，但若可做拖拽更好）
   - 支持调整顺序（上移/下移按钮）
   - 支持分组（Section/Divider），至少支持“基础信息/明细/补充信息”三段结构
   - 支持必填标识与校验提示展示
4. 属性面板（必须）：
   - 字段 label（中文）、fieldKey（英文唯一标识）、是否必填、占位文案
   - 控件类型相关属性（例如 Select 的 options；金额的小数位；日期格式）
   - 校验规则（最小可用即可：必填/长度范围/数值范围）
5. Schema 输出（必须）：
   - 提供“导出 Schema（JSON）”按钮，弹窗展示 JSON（可复制）
   - Schema 至少包含：id、version、title、sections、fields（fieldKey/type/label/required/rules/options/...）
6. 操作区（必须）：
   - 保存（写回 mock，生成/更新 formDefinition）
   - 预览（跳转 `/tools/form-preview` 并带 formId）
   - 新建表单/复制表单（可选）

表单预览页（必须）：
1. 以只读/可填两种模式展示（Tabs/开关均可）。
2. 必须使用“同一份 Schema”渲染出表单 UI（最小可用即可）。
3. 提交动作（mock）：
   - 校验通过：成功提示 + 生成一条提交记录
   - 校验失败：定位到第一个错误字段并提示
4. 提供“返回配置”入口回到 `/tools/form-builder`。

数据要求（必须）：
1. 数据来自 mock（例如 `mock.forms`），至少包含：
   - `formDefinitions`：表单定义列表（id、title、version、schemaJson、updatedAt）
   - `currentEditingFormId`
   - `submissions`：提交记录（formId、submissionId、data、time）
2. 所有字段 label、状态文案必须中文化；时间本地化。

入口要求（必须）：
1. Web：必须能从 Toolbox 进入（例如“更多/工具 → 工具箱 → 表单搭建器”）。

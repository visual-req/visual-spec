## 背景

原型生成过程中，页面数量与类型会持续增长（Web + Mobile），如果没有统一的 UI 规范，很容易出现：

- 同类页面布局不一致（表格/表单/详情）
- 状态色与状态文案口径不一致
- Mobile 与 Web 视觉语言割裂
- 交互方式随意（新建页、页内表单、抽屉/弹窗使用不统一）

因此引入统一且可编辑的 UI 规范文件：`/prototype_ui_convention.md`。

## 变更点

- 新增约束文件：`/prototype_ui_convention.md`（与 `/scheme.yaml` 同级）
- `/vspec:verify` 生成/更新原型时：
  - 若 `/prototype_ui_convention.md` 不存在：先生成默认模板（不覆盖已存在文件）
  - 原型 UI 生成必须严格遵守 `/prototype_ui_convention.md`
  - 若存在更严格的现有规范（例如 `/docs/current/ui_spec.md` 或 `/docs/current/ui_style.md`）：需把更严格的规则合并进 `/prototype_ui_convention.md`，并以合并后的结果作为最终口径

## 如何修改 UI 规范

- 直接编辑目标项目根目录的 `/prototype_ui_convention.md`
- 建议只改“口径”，不要写具体实现细节：
  - 色彩与状态映射
  - 表格/表单/详情的通用结构
  - Drawer/Modal 的使用规则
  - 字体与间距（Web/Mobile）
  - 文案与反馈（成功/失败/权限/空态/错误态）
- 修改完成后重跑 `/vspec:verify`，使生成/更新的页面整体对齐新规范

## 不建议的修改

- 不建议把规范写成某个页面的特例规则（会破坏整体一致性）
- 不建议引入新的 UI 组件库（除非项目技术栈明确要求）
- 不建议在规范中硬编码大量页面级颜色/尺寸（优先抽象为少量全局变量与结构规则）

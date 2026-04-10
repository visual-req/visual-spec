## 需求质量检查（独立使用）

本节说明如何不依赖 `/vspec:qc`，单独利用内置的质量标准文件，对“Word/Markdown/文档库”等任意格式的需求文档进行质量扫描，并生成质量问题表格。

### 准备

- 质量标准文件路径（任选其一，取当前环境存在者）：
  - Skill 根目录：`/prompts/vspec_qc/quality_standard.md`
  - 源码路径：`skills/visual-spec-skill/prompts/vspec_qc/quality_standard.md`
- 你的需求文档（PRD、功能说明、规格等），支持 Word/PDF/Markdown 等

### 使用方式（以 DeepSeek 聊天式 AI 为例）

1. 在聊天窗口上传两份文件：
   - `quality_standard.md`（质量标准）
   - 你的需求文档（Word/PDF/Markdown 等）
2. 在输入框键入：

   请按照质量标准对需求文档进行质量检查，并生成质量检查结果的表格。

3. 若需要结构化表格，可补充表头要求，例如：
   - 编号
   - 问题分类/标题
   - 是否通过（是/否/部分）
   - 问题摘要
   - 涉及位置（章节/段落/页码）
   - 修复建议

### 建议

- 对于“上下限、时间口径、公式精度、权限与数据权限、外部依赖失败策略”等容易遗漏的部分，可在提问中强调“请重点覆盖边界/异常/幂等/回滚/审计/对账”等关键维度
- 如果发现高频问题，可将其沉淀到你项目根目录的 `domain_quality_standard.md`，作为领域补充标准，供 `/vspec:qc` 合并使用


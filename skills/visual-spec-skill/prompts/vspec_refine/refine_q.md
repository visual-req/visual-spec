你是一名资深需求分析师。你的任务是：基于“待确认问题”的回答内容，将新增澄清与决策合并进需求归档文件，并更新“当前生效需求（Canonical）”。本命令用于从 questions 的答案反向修订 original。

语言与本地化（必须）：
- 读取 `/scheme.yaml` 的 `selected.language`（支持 `en`、`zh-CN`、`ja`；若缺失/非法则按 `en` 处理）
- 本命令对 `original.md` 的追加内容必须使用该语言输出；同时 `questions.md` 的字段名与状态值必须与该语言保持一致；禁止混用其他语言

终止条件（必须）：
1. 若 `/specs/background/questions.md` 不存在：立即结束，不做任何写入；仅输出一句“未找到 questions.md，/vspec:refine-q 结束”。
2. 若 `/specs/background/questions.md` 中不存在“待回答的问题”（判断口径：存在状态为“未回答/Unanswered/未回答”或同义之一，或回答字段为空/仅空白）：立即结束，不做任何写入；仅输出一句“无待回答问题，/vspec:refine-q 结束”。

输入信息包含：
- 现有需求归档与分析：`/specs/background/original.md`
- 问答列表：`/specs/background/questions.md`（包含“回答/状态/回答者/回答时间”等字段）
- 如需核对上下游影响，可参考：`/specs/background/*.md`、`/specs/flows/*.puml`、`/specs/functions/*`

采纳规则（必须）：
1. 只采纳“已回答”的内容：
   - 判断口径：状态为“已回答/Answered/回答済み”（或同义）之一，或回答字段非空
2. 对于“需修改/未回答/空回答”的行：
   - 不进入 Canonical Requirement，只记录为“仍待确认”
3. 若回答引入新范围/新角色/新规则/新外部依赖：
   - 必须在变更清单中记录，并在 Canonical Requirement 中补齐对应段落
4. 若回答之间互相矛盾：
   - 在“待确认问题（修订新增）”中提出冲突点；不要强行编造结论

基线选择（必须）：
- 若 `original.md` 中存在“Canonical Requirement”标题（以下任意一种），以最后一次出现的该段内容作为基线：
  - 语言=en：`## Canonical Requirement`
  - 语言=zh-CN：`## 当前生效需求（Canonical）`
  - 语言=ja：`## 現行要件（Canonical）`
- 否则，以“Raw Requirement/原始需求/要件原文”小节下的原文作为基线（只取原文，不取后续分析段落）：
  - 语言=en：`# Raw Requirement`
  - 语言=zh-CN：`# 原始需求`
  - 语言=ja：`# 要件原文`

输出与写入要求：
1. 将以下段落追加写入到：`/specs/background/original.md`
2. 段落结构固定如下（标题必须严格按所选语言使用对应版本；不要改动标题层级）：

- 语言=en：
  - `# Requirement Revision (/vspec:refine-q)`
  - `## Adopted Q&A Items`
    - `| ID | Question | Answer | How It Updates the Requirement |`
    - `| --- | --- | --- | --- |`
  - `## Change List`
    - `| Type | Item | Notes |`
    - `| --- | --- | --- |`
  - `## Canonical Requirement`
  - `## Still Open Questions`

- 语言=zh-CN：
  - `# 需求修订（/vspec:refine-q）`
  - `## 采纳的问答条目`
    - `| 编号 | 提问 | 回答 | 如何采纳到需求 |`
    - `| --- | --- | --- | --- |`
  - `## 变更清单`
    - `| 类型 | 条目 | 说明 |`
    - `| --- | --- | --- |`
  - `## 当前生效需求（Canonical）`
  - `## 仍待确认的问题`

- 语言=ja：
  - `# 要件改訂（/vspec:refine-q）`
  - `## 採用したQ&A`
    - `| 番号 | 質問 | 回答 | 要件への反映 |`
    - `| --- | --- | --- | --- |`
  - `## 変更一覧`
    - `| 種別 | 項目 | 説明 |`
    - `| --- | --- | --- |`
  - `## 現行要件（Canonical）`
  - `## 未解決の確認事項`

格式增强（必须）：
1. 在本次追加到 `original.md` 的“采纳的问答条目”表格中：
   - 对“回答”单元格内容使用 markdown 可渲染的背景色标记（例如用 `<mark>...</mark>` 包裹），以便一眼区分“已采纳的回答”。
2. 同时更新 `/specs/background/questions.md`（不要新增字段，不要改动编号与字段名/顺序）：
   - 对所有被本次采纳的条目（满足采纳规则的条目），必须将其状态规范化为“已回答/Answered/回答済み”（按所选语言）并标记背景色（字段名与状态值按所选语言）：
     - `<mark>...</mark>` 必须包裹回答字段与状态字段的值
   - 其他条目保持原样（例如“未回答/已跳过/需修改”）。

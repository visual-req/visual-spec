## How to customize after forking

[English](../en-US/fork.md) | [中文](../zh-CN/fork.md) | [日本語](../ja-JP/fork.md)

The default behavior of this repo targets general-purpose requirements analysis and delivery. If you fork this repo for a specific industry/domain or for internal team rollout, consider the following customizations so `/vspec:*` outputs better match your organization’s standards.

### 1) Add domain/industry quality standards (Recommended)

Create the following file in your project root:

- `domain_quality_standard.md`

What it’s for:
- Add domain/industry-specific check points (e.g. compliance, auditability, retention, accounting semantics)
- When running `/vspec:qc`, standards are merged from:
  - Built-in standard: `skills/visual-spec/prompts/vspec_qc/quality_standard.md`
  - Domain standard: `domain_quality_standard.md`
  - Project standard: `quality_standard.md` (if present, highest priority)

Suggested rule format:
- “Checkpoint + Decision criteria + Common mistakes + Fix suggestions”
- For rules that must land on specific artifacts, specify target paths (e.g. `/specs/background/original.md`, `/specs/models/*.md`, `/specs/details/**`)

### 2) Customize estimation baselines (Recommended)

Estimation standards are stored as JSON:

- `skills/visual-spec/prompts/vspec_plan/estimation_standards.json`

Reader (single-file HTML, with EN/中文/日本語 switching):

- `skills/visual-spec/prompts/vspec_plan/estimation_standards_reader.html`

During `/vspec:plan` estimation, the model must use this JSON as the shared Story Points baseline (only `0/0.5/1/2/3/5/8/13` are allowed).

How to extend/revise the JSON after forking:
- Keep `allowedStoryPoints` stable; changing the set requires aligning your estimation process to avoid point drift
- Tune `scalePoints` to clarify what each SP means for your team
- Add your high-frequency work item categories under `workItemBenchmarks` using stable `key`s, and fill `en/zh-CN/ja` texts to keep multilingual docs consistent
- Update `version` and `updatedAt` for auditability

### 3) Reuse and maintain a “mistake book”

The built-in quality rules are derived from:

- `skills/visual-spec/prompts/vspec_qc/需求分析错题本.xlsx` (source)
- `skills/visual-spec/prompts/vspec_qc/quality_standard.md` (converted and scan-ready)

Recommendation:
- Keep your own mistake book, and promote reusable check points into `domain_quality_standard.md`

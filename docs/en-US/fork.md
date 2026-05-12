## How to customize after forking

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

The estimation baseline lives at:

- `skills/visual-spec/prompts/vspec_plan/estimate.md`

This file includes two reference tables that can be tuned after forking:
- Story Points scale
- Work-item estimation reference (CRUD, import/export, approval/state machine, RBAC, data permission, integrations, cron jobs, etc.)

Recommended approach:
- Adjust SP baselines to match your team’s efficiency, code-generation ratio, test rigor, and release process
- Add your own common work item categories (e.g. ticketing, reporting, payments, CMS, config deployment)

### 3) Reuse and maintain a “mistake book”

The built-in quality rules are derived from:

- `skills/visual-spec/prompts/vspec_qc/需求分析错题本.xlsx` (source)
- `skills/visual-spec/prompts/vspec_qc/quality_standard.md` (converted and scan-ready)

Recommendation:
- Keep your own mistake book, and promote reusable check points into `domain_quality_standard.md`

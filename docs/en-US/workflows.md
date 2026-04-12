## Workflow

### 1. Requirements Analysis (`/vspec:new`)

- Provide the raw requirement input
- Answer open questions (key assumptions, scope, rules, dependencies)
- Get baseline artifacts under `/specs/`: roles, terms, flows, scenarios, function list, dependencies, questions
- Answer questions (HTML, recommended):
  - `/vspec:new` generates an interactive Q&A page: `/specs/background/question_and_answer.html`
  - Open the HTML, then pick:
    - `/specs/background/original.md`
    - `/specs/background/questions.md`
  - Answer questions in the form UI and save back (if the browser supports File System Access API, it can overwrite; otherwise download and replace manually)

### 2. More Questions (`/vspec:more-q`)

- Use when the question list is not enough or the requirement changed and you need more clarifications
- Input: `/specs/background/questions.md` (if missing, run `/vspec:new` first)
- Output: append new items to `/specs/background/questions.md` (new questions + how-to-answer)
- Answer questions (HTML, recommended):
  - `/vspec:more-q` updates/generates the same Q&A page: `/specs/background/question_and_answer.html`
  - Open the HTML, answer the newly appended questions, save back, then run `/vspec:refine-q`

### 3. Merge Answers (`/vspec:refine-q`)

- Use when the business has filled answers in `/specs/background/questions.md` and you want to merge them back into the canonical requirement
- Input: answered items in `/specs/background/questions.md` + `original.md`
- Output: append updates to `/specs/background/original.md` (adopted items + change log + latest wording)

### 4. Apply Refinements (`/vspec:refine`)

- Use when new information arrives during implementation and you need to update the canonical requirement and sync downstream artifacts
- Inputs:
  - Default: `/docs/refine/*` (prefer `file_list.md`)
  - Optional: files/directories passed as command arguments
- Prerequisite: `/specs/details/` must exist and be non-empty
- Outputs: append updates to `original.md` and update impacted `/specs/details/` and `/specs/prototypes/`

### 5. Detailed Specs (`/vspec:detail`)

- Using `/specs/functions/*` as input, generate per-function specs under `/specs/details/<function_slug>/`
- Goal: turn “requirements” into implementable design inputs:
  - RBAC down to control level, and data permissions
  - load/interaction/validation matrices
  - post-submit checks/processing/navigation
  - logging/notification matrices, MQ specs, import/export, cron jobs
- Extra output: `/specs/details/index.html` (left directory tree + right markdown-rendered reader; PlantUML rendered as diagrams)

### 6. Word Summary Doc (`/vspec:doc`)

- Use when you need a deliverable Word doc for review/circulation/archiving based on current artifacts
- Input: existing `/specs/**` artifacts (original/functions/details/models/flows, when available)
- Output: `/docs/current/requirement_detail.docx` (Word-openable `.docx`, single-file HTML)
- Note: this Word file is a read-only summary; make changes in the corresponding markdown files and rerun `/vspec:doc` to regenerate

### 7. Solution Verification (`/vspec:verify`)

- Prerequisite: `/specs/details/` exists and is non-empty
- Based on `/specs/` (functions + details + roles), generate:
  - `/specs/models/*.md`: entities and fields, relationships, state machines, indexes, external field sources
  - `/specs/prototypes/`: stack-selected runnable prototype (per `scheme.yaml`) and the `scenario.html` scenario review page
- Goal: expose misunderstandings early and converge to a reviewable solution

Optional: segmented prototype generation

- For large prototypes or tighter control by flow, you can generate incrementally:
  - `/vspec:proto-apply`: application flow pages + dashboard differences
  - `/vspec:proto-approve`: approval flow pages + dashboard differences
  - `/vspec:proto-execute`: execution flow pages (including mobile `/m/*`)
  - `/vspec:proto-crud`: config/master-data CRUD admin pages

### 8. Acceptance Cases (`/vspec:accept`)

- Generate acceptance cases into `/specs/acceptance/`
- Goal: define acceptance criteria and coverage (happy path, exceptions, boundaries, RBAC, data permissions)

### 9. Automated Tests (`/vspec:append-test`)

- Read acceptance cases and the repo’s existing test stack
- Generate a minimal runnable set of E2E/API/unit tests
- Note: this step only generates/adds test code to improve coverage; it does not run test commands (e.g. mvn test).

### 10. Integrated Implementation (`/vspec:impl`)

- Read specs, details, models, and dependencies
- Generate integrated backend + frontend code following repo conventions (API contract → backend implementation → frontend integration)

### 11. Quality Check (`/vspec:qc`)

- Run a quality check on artifacts under `/specs/`
- Output: `/specs/qc_report.md`

### 12. Planning (`/vspec:plan`)

- Split functions and scenarios into user stories, estimate effort, and build iteration schedules
- Outputs:
  - `/specs/plan/plan_estimate.md`
  - `/specs/plan/plan_schedule.html`

### 13. Upgrade / Retrofit (`/vspec:upgrade`)

- Use when you need to retrofit/upgrade based on materials under `/docs/` (legacy/current)
- Entry list: `/docs/current/file_list.md` (generated if missing)
- Output: generate/update `/specs/` following the `/vspec:new` structure and sync tech selections to `/scheme.yaml`

### 14. MRD Pack (`/vspec:mrd`)

- Generate market/competitor/user/product-design pack
- Output directory: `/docs/market/` (market/competitors/users/product_design)

## Installation (skills.sh)

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

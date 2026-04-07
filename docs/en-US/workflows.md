## Workflow

### 1. Requirements Analysis (`/vspec:new`)

- Provide the raw requirement input
- Answer open questions (key assumptions, scope, rules, dependencies)
- Get baseline artifacts under `/specs/`: roles, terms, flows, scenarios, function list, dependencies, questions

### 2. Detailed Specs (`/vspec:detail`)

- Using `/specs/functions/*` as input, generate per-function specs under `/specs/details/<function_slug>/`
- Goal: turn “requirements” into implementable design inputs:
  - RBAC down to control level, and data permissions
  - load/interaction/validation matrices
  - post-submit checks/processing/navigation
  - logging/notification matrices, MQ specs, import/export, cron jobs

### 3. Solution Verification (`/vspec:verify`)

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

### 4. Acceptance Cases (`/vspec:accept`)

- Generate acceptance cases into `/specs/acceptance/`
- Goal: define acceptance criteria and coverage (happy path, exceptions, boundaries, RBAC, data permissions)

### 5. Automated Tests (`/vspec:append-test`)

- Read acceptance cases and the repo’s existing test stack
- Generate a minimal runnable set of E2E/API/unit tests
- Note: this step only generates/adds test code to improve coverage; it does not run test commands (e.g. mvn test).

### 6. Integrated Implementation (`/vspec:impl`)

- Read specs, details, models, and dependencies
- Generate integrated backend + frontend code following repo conventions (API contract → backend implementation → frontend integration)

### 7. Planning (`/vspec:plan`)

- Split functions and scenarios into user stories, estimate effort, and build iteration schedules
- Outputs:
  - `/specs/plan/plan_estimate.md`
  - `/specs/plan/plan_schedule.html`

## Installation (skills.sh)

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill
```

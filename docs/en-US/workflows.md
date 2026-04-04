## Workflow

### 0. Setup

- Install this Skill at your project root (the target project contains `.trae/`)
- Ensure `.trae/skills/visual-spec-skill/` exists in the target project (see “Installation” below)

### 1. Requirements Analysis (`/vspec:new`)

- Provide the raw requirement input
- Answer open questions (key assumptions, scope, rules, dependencies)
- Get baseline artifacts under `/specs/`: roles, terms, flows, scenarios, function list, dependencies, questions

### 2. Solution Verification (`/vspec:verify`)

- Based on `/specs/`, generate:
  - `/specs/models/*.md`: entities and fields, relationships, state machines, indexes, external field sources
  - `/specs/prototypes/`: stack-selected runnable prototype (per `scheme.yaml`) and the `scenario.html` scenario review page
- Goal: expose misunderstandings early and converge to a reviewable solution

Optional: segmented prototype generation

- For large prototypes or tighter control by flow, you can generate incrementally:
  - `/vspec:proto-apply`: application flow pages + dashboard differences
  - `/vspec:proto-approve`: approval flow pages + dashboard differences
  - `/vspec:proto-execute`: execution flow pages (including mobile `/m/*`)
  - `/vspec:proto-crud`: config/master-data CRUD admin pages

### 3. Detailed Specs (`/vspec:detail`)

- Using `/specs/functions/*` as input, generate per-function specs under `/specs/details/<function_slug>/`
- Goal: turn “requirements” into implementable design inputs:
  - RBAC down to control level, and data permissions
  - load/interaction/validation matrices
  - post-submit checks/processing/navigation
  - logging/notification matrices, MQ specs, import/export, cron jobs

### 4. Acceptance Cases (`/vspec:accept`)

- Generate acceptance cases into `/specs/acceptance/`
- Goal: define acceptance criteria and coverage (happy path, exceptions, boundaries, RBAC, data permissions)

### 5. Automated Tests (`/vspec:test`)

- Read acceptance cases and the repo’s existing test stack
- Generate a minimal runnable set of E2E/API/unit tests

### 6. Integrated Implementation (`/vspec:impl`)

- Read specs, details, models, and dependencies
- Generate integrated backend + frontend code following repo conventions (API contract → backend implementation → frontend integration)

### 7. Planning (`/vspec:plan`)

- Split functions and scenarios into user stories, estimate effort, and build iteration schedules
- Outputs:
  - `/specs/plan/plan_estimate.md`
  - `/specs/plan/plan_schedule.html`

### 8. Change Handling (`/vspec:change`)

- Provide change inputs
- Output impact analysis and change log, and update impacted artifacts and cases

## Installation (npm)

- Recommended at your project root: `npm install <git-url>`
- After installation, the Skill is copied to: `<your-project>/.trae/skills/visual-spec-skill/`
- Manual installation (if needed): `npx vspec --force`

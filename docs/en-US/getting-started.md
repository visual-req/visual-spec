## Getting Started

This package provides a `/vspec:*` command-driven Skill that turns raw requirements into reviewable artifacts: specs, data models, runnable prototypes, detailed design, acceptance cases, tests, and integrated implementation inputs.

### 1. Installation

Install the Skill into your AI editor configuration directory:

- Installation and verification: `installation.md`

Install / update (skills.sh):

```bash
npx skills add visual-req/visual-spec --skill visual-spec-skill
```

### 2. Recommended Workflow

- Initial spec: `/vspec:new`
  - Midway it generates the canonical requirement file (`/specs/background/original.md`) and asks clarification questions
  - Answer those questions in chat first, then type “continue” to finish `/vspec:new` (do not write these clarification answers into `questions.md`)
  - It also generates an open question list (`/specs/background/questions.md`) for later merging
- Merge Q&A into the canonical requirement: `/vspec:refine-q` (merge answered items from `/specs/background/questions.md` back into `original.md`)
- Quality check: `/vspec:qc` (run a non-conformance check on generated `/specs/` artifacts and write `/specs/qc_report.md` before refinements/implementation)
- Detailed specs: `/vspec:detail` (iterate all functions and generate RBAC, data permission, interaction, validation, state machine, etc.)
- Quick validation (models + prototype): `/vspec:verify` (build runnable prototypes from functions + details + models; requires non-empty `/specs/details/`)
- Acceptance cases: `/vspec:accept` (turn key scenarios into reviewable acceptance checklists)
- Integrated implementation: `/vspec:impl` (implementation inputs and structure constraints: models/services/repositories/exceptions, etc.)
- Automated tests: `/vspec:append-test` (test plan and automation skeletons)
- Upgrade/redesign (inherit from legacy materials): `/vspec:upgrade` (normalize legacy/current materials into new specs and selections)

### 3. Key Directories

- `/docs/`: input archive (legacy/current/refine/templates/texts/assets)
- `/specs/`: generated artifacts (background/details/models/prototypes/acceptance, etc.)
- `/scheme.yaml`: stack and package manager selection (prototype and implementation must follow it)

Directory structure reference:

- `structure.md`

Next:

- Read `structure.md` to confirm where inputs are stored and where outputs are generated

### 4. Common Scenarios

#### Refinements (`refine`)

- Put refinement materials into `/docs/refine/refine.md` (use it as the primary entry; add other files under the folder only when needed)
- Prerequisite: `/specs/details/` must exist and be non-empty, otherwise `refine` does not run
- Run: `/vspec:refine`
- Result: appends updates to `/specs/background/original.md` and syncs impacted `/specs/details/` and `/specs/prototypes/`

#### Upgrade/Redesign (`upgrade`)

- List input materials in `/docs/current/file_list.md` (legacy system under `/docs/legacy/`, new inputs under `/docs/current/`)
- Run: `/vspec:upgrade`
- Result: generates/updates `/specs/` and syncs technical selections into `/scheme.yaml`

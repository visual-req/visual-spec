## Getting Started

This package provides a `/vspec:*` command-driven Skill that turns raw requirements into reviewable artifacts: specs, data models, runnable prototypes, detailed design, acceptance cases, tests, and integrated implementation inputs.

### 1. Installation

Install the npm package, then install the Skill into your AI editor configuration directory:

- Installation and verification: `installation.md`

Install / update (npm):

```bash
npm install -g visual-spec
```

Install / update (pnpm):

```bash
pnpm add -g visual-spec
```

Install / update (yarn):

Yarn Classic:

```bash
yarn global add visual-spec
```

Yarn Berry (v2+):

```bash
yarn dlx -p visual-spec vspec
```

### 2. Recommended Workflow

- Initial spec: `/vspec:new`
  - During execution it generates an open question list (`/specs/background/questions.md`)
  - Fill in business answers in that file before continuing the workflow
- Merge Q&A into the canonical requirement: `/vspec:refine-q`
- Quick validation (models + prototype): `/vspec:verify`
- Detailed specs: `/vspec:detail`
- Acceptance cases: `/vspec:accept`
- Integrated implementation: `/vspec:impl`
- Automated tests: `/vspec:test`
- Change handling: `/vspec:change`
- Upgrade/redesign (inherit from legacy materials): `/vspec:upgrade`

### 3. Key Directories

- `/docs/`: input archive (legacy/current/change/refine/templates/texts/assets)
- `/specs/`: generated artifacts (background/details/models/prototypes/acceptance, etc.)
- `/scheme.yaml`: stack and package manager selection (prototype and implementation must follow it)

Directory structure reference:

- `structure.md`
 - `structure.md`

Next:

- Read `structure.md` to confirm where inputs are stored and where outputs are generated

### 4. Common Scenarios

#### Refinements (`refine`)

- Put refinement materials into `/docs/refine/`
- Prerequisite: `/specs/details/` must exist and be non-empty, otherwise `refine` does not run
- Run: `/vspec:refine`
- Result: appends updates to `/specs/background/original.md` and syncs impacted `/specs/details/` and `/specs/prototypes/`

#### Changes (`change`)

- Put change materials into `/docs/change/` (optional `file_list.md`)
- Run: `/vspec:change`
- Result: performs impact analysis, updates artifacts (prefers `/specs/details/<module_slug>/`), and updates the change log

#### Upgrade/Redesign (`upgrade`)

- List input materials in `/docs/current/file_list.md` (legacy system under `/docs/legacy/`, new inputs under `/docs/current/`)
- Run: `/vspec:upgrade`
- Result: generates/updates `/specs/` and syncs technical selections into `/scheme.yaml`

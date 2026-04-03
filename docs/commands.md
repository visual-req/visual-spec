## Command Overview

| Command | Purpose | Primary Inputs | Primary Outputs |
| --- | --- | --- | --- |
| `/vspec:new` | Generate baseline spec artifacts from raw requirements | Raw requirement text + interactive Q&A | `/specs/` (original, stakeholders, roles, terms, flows, scenarios, scenario_details, dependencies, functions, questions) + initializes `/docs/*` archive directories |
| `/vspec:refine` | Apply refinement materials and sync impacted details and prototypes | `/docs/refine/*` (or command args) + baseline `/specs/background/original.md` + prerequisite `/specs/details/` | Appends to `/specs/background/original.md` (change list + canonical) + updates impacted `/specs/details/` and `/specs/prototypes/` |
| `/vspec:refine-q` | Merge answered questions back into the requirement | `/specs/background/original.md` + `/specs/background/questions.md` | Appends to `/specs/background/original.md` (adopted items + change list + canonical) |
| `/vspec:verify` | Generate models and prototype for fast validation | Existing `/specs/` artifacts | `/specs/models/*.md`, `/specs/prototypes/` (runnable prototype + `scenario.html` review page) |
| `/vspec:detail` | Expand per-function detailed specs | `/specs/functions/*` + details/models/roles | `/specs/details/<function_slug>/*` (RBAC, interaction, validation, logging, notifications, MQ, import/export, cron, etc.) |
| `/vspec:accept` | Generate acceptance test cases | functions/scenarios/details/roles/models | `/specs/acceptance/<function_slug>/acceptance_cases.md`, `/specs/acceptance/index.md` |
| `/vspec:test` | Generate automated test code | acceptance cases + repo test stack | Writes into existing test directories or `/tests/` |
| `/vspec:impl` | Generate integrated backend + frontend implementation | specs/details/models/dependencies | Writes integrated implementation code (API contract, backend, frontend integration) |
| `/vspec:upgrade` | Analyze and generate new specs based on legacy materials | `/docs/current/file_list.md` + `/docs/legacy/*` (optional templates/texts/assets) + existing `/specs/background/original.md` (if any) | Generate/update `/specs/` in `/vspec:new` structure + sync technical selections to `/scheme.yaml` |
| `/vspec:change` | Apply change inputs, do impact analysis, and update artifacts | `/docs/change/*` (optional file_list.md) + existing `/specs/` | Update impacted files (prefers `/specs/details/<module_slug>/`) + `/specs/change_log.md` (requires git snapshot commit before updating) |
| `/vspec:qc` | Run quality checks on `/specs/` artifacts | built-in standard + optional project `quality_standard.md` + `/specs/` | `/specs/qc_report.md` |
| `/vspec:plan` | Estimation and scheduling | functions/roles/flows/dependencies/details | `/specs/plan_estimate.md`, `/specs/plan_schedule.html` |

## `/vspec:new`

- When to use: you just received the requirement and information is incomplete; you need a shared language and a first-cut spec quickly
- Key outputs: stakeholders, roles, terms, flows, scenarios, function list, open questions
- Directory initialization: creates `/docs/` and its subdirectories (legacy/current/change/refine/templates/texts/assets) for input archiving and future command inputs

## `/vspec:refine`

- When to use: new information/refinements appear during implementation; you need to update the canonical requirement while keeping traceability, and sync details and prototype
- Inputs:
  - Default: `/docs/refine/` (prefers `/docs/refine/file_list.md`, otherwise reads files by name order)
  - Optional: command args can override with explicit files/directories (higher priority)
- Prerequisite: `/specs/details/` must exist and be non-empty; otherwise `refine` does not run (to avoid upstream changes without downstream sync)
- Key outputs:
  - Append “change list + canonical requirement + impact analysis and artifact updates” to the end of `original.md`
  - Update impacted `/specs/details/` (prefer updating existing files) and `/specs/prototypes/` (minimal reviewable diff)

## `/vspec:refine-q`

- When to use: business has answered `/specs/background/questions.md`, and you want to merge those answers into the requirement and produce a new canonical version
- Key outputs: adopted Q&A items + change list + canonical requirement

## `/vspec:verify`

- When to use: you want to validate the data structure and page shape quickly and reduce misunderstanding risk
- Key outputs: model files (entity splitting), runnable prototype, scenario review page

## `/vspec:detail`

- When to use: before design/implementation, you need each function to be specified at an implementable level
- Key outputs: RBAC to control level, data permissions, load/interaction/validation matrices, post-submit processing, logging/notification matrices, MQ, import/export, cron jobs

## `/vspec:accept`

- When to use: align delivery and acceptance with an executable set of cases
- Key outputs: per-function acceptance case tables covering happy path, exceptions, boundaries, RBAC, and data permissions

## `/vspec:test`

- When to use: turn acceptance cases into runnable automated tests (E2E/API/unit)
- Key outputs: reuse the repo’s existing test frameworks and scripts; avoid introducing new dependencies

## `/vspec:impl`

- When to use: convert spec artifacts into runnable integrated backend + frontend code
- Key outputs: API contract, backend implementation, frontend pages and API integration, RBAC/state machine enforcement

## `/vspec:change`

- When to use: explicit change requests arrive and you need traceable updates and impact assessment
- Inputs: read from `/docs/change/` (optional `/docs/change/file_list.md` as an ordered entry list; compatible with legacy path `/docs/changes/`)
- Update strategy: prioritize the impacted module directory `/specs/details/<module_slug>/` and sync models/functions/prototypes/acceptance as needed
- Pre-update snapshot: if the target repo is a git repo, create a snapshot commit before writing any updates so diffs are reviewable
- Key outputs: structured change list, impact analysis table, change log, and corresponding artifact updates

## `/vspec:upgrade`

- When to use: do an “upgrade/redesign/migration” analysis based on legacy system materials, inherit what is needed, and generate new spec artifacts
- Entry list: `/docs/current/file_list.md` (generates a template if missing) to list input files, usage, extracted key points, and whether required
- Input scope: usually from `/docs/legacy/*` and `/docs/current/*`, optionally combined with `/docs/templates/*`, `/docs/texts/*`, `/docs/assets/*`
- Key outputs: generate/update `/specs/` using the `/vspec:new` artifact structure, and label inherited/new/adjusted/deprecated items in the function list
- Stack sync: extract technical selections from “system technical spec” inputs and write them into `/scheme.yaml` for `/vspec:verify` and `/vspec:impl`

## `/vspec:plan`

- When to use: align delivery cadence, decompose via story mapping, and build a schedule
- Key outputs: story decomposition and estimation (person-days), iteration plan, and an HTML story map

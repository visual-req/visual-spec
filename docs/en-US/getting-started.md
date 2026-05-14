## Getting Started

[English](../en-US/getting-started.md) | [中文](../zh-CN/getting-started.md) | [日本語](../ja-JP/getting-started.md)

This package provides a [/vspec:*](../../README.md#commands) command-driven Skill that turns raw requirements into reviewable artifacts: specs, data models, runnable prototypes, detailed design, acceptance cases, tests, and integrated implementation inputs.

### 1. Installation

Install the Skill into your AI editor configuration directory:

- Installation and verification: `installation.md`

Install / update (skills.sh):

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

### 2. Recommended Workflow

- Initial spec: [/vspec:new](../../README.md#commands)
  - Optional language:
    - Single language: [/vspec:new](../../README.md#commands) `lang=zh` (or `lang=en`, `lang=ja`) sets `/scheme.yaml` `selected.language` and generates docs in that language
    - Multi-language (prototype switch): [/vspec:new](../../README.md#commands) `lang=zh,en` sets docs default to `zh` and sets `/scheme.yaml` `selected.languages` for prototype UI language switching
  - Midway it generates the canonical requirement file (`/specs/background/original.md`) and asks clarification questions
  - Answer those questions in chat first, then type “continue” to finish [/vspec:new](../../README.md#commands) (do not write these clarification answers into `questions.md`)
  - It also generates an open question list (`/specs/background/questions.md`) for later merging
- Merge Q&A into the canonical requirement: [/vspec:refine-q](../../README.md#commands) (merge answered items from `/specs/background/questions.md` back into `original.md`)
- Quality check: [/vspec:qc](../../README.md#commands) (run a non-conformance check on generated `/specs/` artifacts and write `/specs/qc_report.md` before refinements/implementation)
- Detailed specs: [/vspec:detail](../../README.md#commands) (iterate all functions and generate RBAC, data permission, interaction, validation, state machine, etc.)
- Quick validation (models + prototype): [/vspec:verify](../../README.md#commands) (build runnable prototypes from functions + details + models; requires non-empty `/specs/details/`)
- Acceptance cases: [/vspec:accept](../../README.md#commands) (turn key scenarios into reviewable acceptance checklists)
- Integrated implementation: [/vspec:impl](../../README.md#commands) (implementation inputs and structure constraints: models/services/repositories/exceptions, etc.)
- Automated tests: [/vspec:append-test](../../README.md#commands) (test plan and automation skeletons)
- Upgrade/redesign (inherit from legacy materials): [/vspec:upgrade](../../README.md#commands) (normalize legacy/current materials into new specs and selections)

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
- Run: [/vspec:refine](../../README.md#commands)
- Result: appends updates to `/specs/background/original.md` and syncs impacted `/specs/details/` and `/specs/prototypes/`

#### Upgrade/Redesign (`upgrade`)

- List input materials in `/docs/current/file_list.md` (legacy system under `/docs/legacy/`, new inputs under `/docs/current/`)
- Run: [/vspec:upgrade](../../README.md#commands)
- Result: generates/updates `/specs/` and syncs technical selections into `/scheme.yaml`

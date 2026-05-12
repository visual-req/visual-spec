# visual-spec

This repo provides a requirements analysis and delivery assistant Skill. It offers a `/vspec:*` command-driven workflow that turns raw requirements into reviewable, shippable artifacts: specs, data models, runnable prototypes, detailed design, acceptance cases, tests, and integrated implementation inputs.

It is designed around an independently-owned IP methodology: “visualized requirements analysis”. The goal is to standardize and make the end-to-end workflow (clarification → design → validation) more visual, traceable, and reusable, so teams can reduce communication overhead and avoid rework.

Version: 0.1.13 (2026-04-12)

## Installation

Install the Skill into your AI editor configuration directory (Trae / Claude Code / Cursor / GitHub Copilot, etc.):

```bash
npx skills add visual-req/visual-spec --skill visual-spec
```

Docs:
- Installation: `docs/en-US/installation.md`
- Multi-agent installation: `docs/en-US/ai-platform-installation.md`

## Overview

- Requirements analysis: generate background, stakeholders, roles, terms, flows, scenarios, details, dependencies, function list, and open questions
- Solution verification: generate data models, runnable prototypes, and a scenario review page
- Detailed design: produce RBAC/data-permission/interaction/validation/logging/notification/MQ/import-export/cron specs per function
- Acceptance & testing: generate acceptance cases and automated test code
- Integrated implementation: generate backend + frontend integrated code (aligned with the repo’s actual stack and conventions)
- Planning: estimate and schedule based on the function list (HTML output)

## Commands

| Command | Purpose | Main inputs | Main outputs |
| --- | --- | --- | --- |
| `/vspec:new` | Generate baseline spec artifacts | raw requirement text + optional `/docs/current/*` | `/specs/` (background/functions/flows, etc.) |
| `/vspec:refine` | Refine an existing visual-spec requirement and sync downstream artifacts | `/docs/refine/refine.md` or prompt-window pasted changes or command args | updates `/specs/background/original.md` + sync updates `/specs/details/`, `/specs/prototypes/`, existing `/specs/backend/` |
| `/vspec:refine-q` | Merge answered questions back into the canonical spec | `/specs/background/questions.md` (answered items) | updates `/specs/background/original.md` and marks answers in `questions.md` |
| `/vspec:detail` | Generate per-function detailed specs | `/specs/functions/*` + supporting artifacts | `/specs/details/` |
| `/vspec:verify` | Generate data models and a stack-selected runnable prototype | `/scheme.yaml` + non-empty `/specs/details/` | `/specs/models/`, `/specs/prototypes/` |
| `/vspec:accept` | Generate acceptance test cases | functions + scenarios + details + models | `/specs/acceptance/` |
| `/vspec:append-test` | Generate automated test code | acceptance cases + existing test framework | existing test directories or `/tests/` |
| `/vspec:impl` | Generate integrated backend + frontend implementation inputs | details + models + dependencies | `/specs/backend/` (if enabled) and related integration code |
| `/vspec:upgrade` | Upgrade/redesign based on legacy + new inputs | `/docs/legacy/*` + `/docs/current/*` | regenerated `/specs/` + synced technical selections to `/scheme.yaml` |
| `/vspec:qc` | Run quality checks on generated artifacts | `/specs/` + built-in/project standards | `/specs/qc_report.json`, `/specs/qc_report.html` |
| `/vspec:plan` | Generate estimation and schedule | functions + details + `/specs/qc_report.json` | `/specs/plan/plan_estimate.md`, `/specs/plan/plan_schedule.html` |

## Documentation

| Doc | Description | Link |
| --- | --- | --- |
| Getting started | Run a full workflow end-to-end | [docs/en-US/getting-started.md](docs/en-US/getting-started.md) |
| Commands | `/vspec:*` reference | [docs/en-US/commands.md](docs/en-US/commands.md) |
| Structure | Directory structure and artifacts | [docs/en-US/structure.md](docs/en-US/structure.md) |
| Workflows | Visual workflow overview | [docs/en-US/workflows.md](docs/en-US/workflows.md) |
| Installation | Installation & setup | [docs/en-US/installation.md](docs/en-US/installation.md) |

## Upgrade vs Refine

- `upgrade`: for legacy-system upgrade/rebuild scenarios; it uses `/docs/legacy/` + `/docs/current/` (and related template/text/assets inputs) to produce an upgraded target spec and technical selections.
- `refine`: for improving/adjusting an already visual-spec-structured requirement (legacy or new); it updates the canonical requirement and keeps downstream artifacts in sync.

## Directory Structure

- `skills/visual-spec/SKILL.md`: Skill definition and command workflow
- `skills/visual-spec/prompts/`: prompt files used by each command

## Licensing / Plans

- `prompts/harness/*` (post-run validation commands) is a paid feature and is only available in the Pro edition.
- Pro edition adds broader quality checks across commands (e.g. prototype stack verification, click-no-op detection, mobile UX checks, price formatting checks, and backend MVC/test coverage checks) and requires a paid plan to enable.

## Quick Start

1. Install: `npx skills add visual-req/visual-spec --skill visual-spec`
2. Run `/vspec:new` and paste your raw requirement
3. Answer the Open Questions so the spec converges on decisions and assumptions
4. Run commands in order to get end-to-end deliverables:
   - `/vspec:detail` → detailed specs under `/specs/details/`
   - `/vspec:verify` → models + runnable prototype under `/specs/models/` and `/specs/prototypes/`
   - `/vspec:qc` → quality report `/specs/qc_report.json` and `/specs/qc_report.html`
   - `/vspec:plan` (optional) → estimation + schedule under `/specs/plan/`
5. When requirements change, put updates in `/docs/refine/refine.md` (or paste into the prompt window) and run `/vspec:refine` to keep downstream artifacts in sync

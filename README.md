This repo provides a requirements analysis and delivery assistant Skill. It offers a `/vspec:*` command-driven workflow that turns raw requirements into reviewable artifacts: specs, data models, runnable prototypes, detailed design, acceptance cases, tests, and integrated implementation inputs.

Version: 0.1.11 (2026-04-12)

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

- `/vspec:new`: Generate baseline spec artifacts (writes to `/specs/`)
- `/vspec:refine`: Apply refinements from `/docs/refine/` (or command arguments) and update `/specs/details/` and `/specs/prototypes/` (requires existing details)
- `/vspec:refine-q`: Merge answered items from `questions.md` back into the spec and update the canonical requirement in `/specs/background/original.md`
- `/vspec:detail`: Generate per-function detailed specs (writes to `/specs/details/`)
- `/vspec:verify`: Generate data models and a stack-selected runnable prototype (per `/scheme.yaml`) (writes to `/specs/models/`, `/specs/prototypes/`; requires non-empty `/specs/details/`)
- `/vspec:accept`: Generate acceptance test cases (writes to `/specs/acceptance/`)
- `/vspec:append-test`: Generate automated test code (writes into the repo’s existing test directories or `/tests/`)
- `/vspec:impl`: Generate integrated backend + frontend implementation code (writes under `/specs/`)
- `/vspec:upgrade`: Upgrade/redesign based on legacy + new inputs under `/docs/` (legacy/current/templates/texts/assets), generate/update `/specs/`, and sync technical selections to `/scheme.yaml`
- `/vspec:qc`: Run artifact quality checks and write a report (writes to `/specs/qc_report.md`)
- `/vspec:plan`: Generate estimation and schedule (writes to `/specs/plan/plan_estimate.md`, `/specs/plan/plan_schedule.html`)

## Directory Structure

- `skills/visual-spec/SKILL.md`: Skill definition and command workflow
- `skills/visual-spec/prompts/`: prompt files used by each command

## Licensing / Plans

- `prompts/harness/*` (post-run validation commands) is a paid feature and is only available in the Pro edition.
- Pro edition adds broader quality checks across commands (e.g. prototype stack verification, click-no-op detection, mobile UX checks, price formatting checks, and backend MVC/test coverage checks) and requires a paid plan to enable.

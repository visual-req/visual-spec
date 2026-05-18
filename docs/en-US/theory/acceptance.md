## Acceptance cases: why they should be scenario-driven ([/vspec:accept](../../../README.md#commands))

[English](../../en-US/theory/acceptance.md) | [中文](../../zh-CN/theory/acceptance.md) | [日本語](../../ja-JP/theory/acceptance.md)

Many teams write acceptance as a “feature checklist”. This usually misses real delivery risks: it covers only the happy path, skips exceptions/rollbacks/concurrency/permissions/boundaries, and becomes unreliable after requirement changes.

visual-spec derives acceptance cases from scenarios because scenarios naturally carry the structure needed to make behavior executable and verifiable, and they connect analysis to delivery through one traceable backbone.

### Why scenarios work better than feature lists

- A scenario is “executable user actions + verifiable expected outcomes”, which matches the shape of an acceptance case
- Scenarios force branch coverage: exceptions, rollbacks, concurrency conflicts, permission denials, dependency failures, boundary inputs
- Scenarios make preconditions and state explicit, where most acceptance gaps actually happen (state/permission/data scope), not in the feature label

### How scenario-driven acceptance reduces collaboration cost

- Shared language: business, dev, and QA can align on the same scenario set when discussing “done”
- Traceability: each acceptance case can point back to its scenario and feature, making review, regression, and defect triage faster
- Change-friendliness: when scenarios/constraints change, rerunning [/vspec:accept](../../../README.md#commands) refreshes cases and prevents silent drift

### How it maps to the visual-spec workflow

- [/vspec:new](../../../README.md#commands) outputs flows/scenarios and captures uncertainty as open questions
- [/vspec:detail](../../../README.md#commands) specifies implementable details (permissions, validation, interaction, logging, notifications, etc.)
- [/vspec:accept](../../../README.md#commands) converts scenarios + details into structured acceptance cases (JSON: `/test/验收用例/acceptance_cases.json`) and outputs `/test/testcase_reader.html`
- [/vspec:script](../../../README.md#commands) generates Playwright automation skeletons from JSON cases (`/test/playwright/`)
- [/vspec:append-test](../../../README.md#commands) turns acceptance cases into automated tests, closing the loop from acceptance to automation

### Minimal coverage set (recommended)

For each feature, cover at least:

- Happy path
- Exceptions/failures (validation errors, permission denials, dependency failures, concurrency conflicts)
- Boundaries (min/max, null/empty, enum edges, max length)
- Permissions (RBAC to control level; data scope filtering)

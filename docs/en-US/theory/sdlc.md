## SDLC alignment: why the workflow is staged

[English](../../en-US/theory/sdlc.md) | [中文](../../zh-CN/theory/sdlc.md) | [日本語](../../ja-JP/theory/sdlc.md)

visual-spec intentionally turns the most costly “late discoveries” in SDLC into early, reviewable artifacts. Fixing a misunderstanding is cheapest during requirements/design, but becomes expensive once it has propagated into implementation, tests, and release operations.

### Command → SDLC mapping

- `/vspec:new`: Discovery / Requirements
  - Establish a shared language: roles, terms, scenarios, flows, function list, dependencies, and open questions
- `/vspec:detail`: Design
  - Convert “features” into implementation-ready specs: RBAC, data permissions, interaction, validation, logging, notifications, MQ, import/export, cron, etc.
- `/vspec:verify`: Validation
  - Generate data models and a runnable prototype so stakeholders can review behavior visually
- `/vspec:qc`: Quality gate
  - Run rule-based checks for omissions, contradictions, non-testable specs, and missing traceability
- `/vspec:accept`: Acceptance definition
  - Turn key scenarios into reviewable acceptance cases
- `/vspec:impl`: Build inputs
  - Produce structured implementation inputs aligned with the selected stack and repo conventions (if enabled)
- `/vspec:append-test`: Test automation
  - Generate test plans/skeletons from acceptance cases to reduce adoption cost
- `/vspec:plan`: Planning
  - Estimate and schedule after scope is stabilized and quality has passed the gate

### Why not output a single “big PRD”

- Requirements change: staging limits blast radius and reduces rewrite cost
- Different reviewers need different views: scenarios/prototype vs specs/models vs acceptance/tests
- Traceability matters: layered artifacts make “scenario → spec → prototype → acceptance → test” linkable

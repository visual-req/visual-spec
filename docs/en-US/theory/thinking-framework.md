## Analysis thinking: modularize requirements analysis

[English](../../en-US/theory/thinking-framework.md) | [中文](../../zh-CN/theory/thinking-framework.md) | [日本語](../../ja-JP/theory/thinking-framework.md)

Requirements analysis is not a single template; it’s a set of reusable thinking modules. visual-spec makes these modules explicit and applies them across stages so the workflow converges decisions early and keeps downstream artifacts consistent.

### Module 1: Goals and boundaries

- Clarify “what problem to solve, for whom, and to what extent”
- Output verifiable success criteria and explicit non-goals

### Module 2: Roles and RBAC

- Establish “role → visibility scope → actionable behaviors”
- Push permissions down to sections/controls and data scope (not only menus)

### Module 3: Scenarios and flows

- Describe “trigger → happy path → branches/exceptions → rollback/compensation → done”
- Use flows/state to cover completeness and recoverability

### Module 4: Data definitions

- Align field semantics, calculations, status meanings, time/money rules, rounding/precision
- Provide reusable definitions for models and APIs

### Module 5: Rules and constraints

- Make implicit rules explicit: validation, idempotency, tolerance, reconciliation, audit, compliance
- Turn constraints into checkable items for QC and acceptance

### Module 6: Testability and traceability

- Ensure every function maps to inputs/outputs/expected outcomes/exceptions/logs/audits
- Use acceptance cases and test skeletons to carry review conclusions into automation

### Module 7: Review and iteration

- Use runnable prototypes + scenario review to shorten feedback loops
- Use refine to sync downstream artifacts (details/prototype/impl inputs) when requirements change

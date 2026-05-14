## Design Principles

[English](../en-US/concepts.md) | [中文](../zh-CN/concepts.md) | [日本語](../ja-JP/concepts.md)

These 7 principles are the design creed behind visual-spec. They influence command behavior, artifact structure, and review ergonomics. If you understand them, the workflow becomes predictable: you’ll know why some information must be clarified early and how each output supports downstream implementation, acceptance, and change sync.

### 1. Collaborate Through Artifacts

- Core idea: turn “discussion” into “reviewable artifacts” so alignment is based on shared evidence, not memory
- What it fixes: decisions drift; reviews become vague; context is lost across time and people
- How it shows up in visual-spec:
  - [/vspec:new](../../README.md#commands) creates the baseline under `/specs/` (roles/terms/flows/scenarios/function list/open questions, etc.)
  - [/vspec:verify](../../README.md#commands) makes key agreements runnable and reviewable (`/specs/models/`, `/specs/prototypes/`)
  - [/vspec:detail](../../README.md#commands) and [/vspec:accept](../../README.md#commands) carry that agreement into implementable and testable specs

### 2. Scenario-Driven Decomposition (Not Feature Piling)

- Core idea: decompose requirements by user scenarios / node chains, not by isolated feature checklists
- What it fixes: happy-path-only specs; missing rollback/exception branches; untestable “feature lists”
- How it shows up in visual-spec:
  - [/vspec:new](../../README.md#commands) outputs flows + scenario sets (happy path + rollback paths) and explicit open questions
  - [/vspec:accept](../../README.md#commands) converts scenarios into acceptance cases (`/specs/acceptance/`), enforcing “executable actions + verifiable outcomes”

### 3. RBAC and Data Permissions First

- Core idea: treat permission design as a first-class requirement, not an afterthought
- What it fixes: “page is visible but actions shouldn’t be clickable”; unclear data scope leading to overexposure and mistakes
- How it shows up in visual-spec:
  - [/vspec:verify](../../README.md#commands) generates role-based dashboard prototypes to review role differences early (`/specs/prototypes/`)
  - [/vspec:detail](../../README.md#commands) specifies RBAC down to page sections/controls and models data permissions independently before composing them (`/specs/details/`)

### 4. Implementation-Friendly Detail

- Core idea: express behavior as checklists/tables/matrices so it becomes direct engineering input
- What it fixes: endless “what happens after submit?” clarifications; reviews missing edge-case gaps
- How it shows up in visual-spec:
  - [/vspec:detail](../../README.md#commands) uses table-friendly patterns for load/interaction/post-submit behavior and matrices for validation/logging/notifications (`/specs/details/`)
  - [/vspec:impl](../../README.md#commands) structures implementation inputs aligned to the repo’s stack and conventions

### 5. Consistency and Observability by Default

- Core idea: reliability and observability are part of the requirement, not a late-stage patch
- What it fixes: inconsistent retry/DLQ/compensation behaviors; missing trace/audit/alert signals that block debugging
- How it shows up in visual-spec:
  - [/vspec:detail](../../README.md#commands) makes external deps, MQ, failure strategies, idempotency, and compensations explicit (`/specs/details/`)
  - [/vspec:qc](../../README.md#commands) surfaces omissions and contradictions via checkable rules (`/specs/qc_report.*`)

### 6. Acceptance → Automation → Integration

- Core idea: make acceptance the shared language, then push toward automation and integration
- What it fixes: requirements that are “right” but not testable; high adoption cost for test automation
- How it shows up in visual-spec:
  - [/vspec:accept](../../README.md#commands) produces acceptance cases (`/specs/acceptance/`)
  - [/vspec:append-test](../../README.md#commands) reuses existing test frameworks and directory conventions whenever possible
  - [/vspec:impl](../../README.md#commands) organizes inputs around minimal reviewable diffs and a runnable end-to-end loop

### 7. Requirements That Are Easy to Change

- Core idea: requirements evolve; keep one canonical source and synchronize derived artifacts
- What it fixes: prototypes/tests/specs drifting after changes; unclear change attribution; inconsistent delivery basis
- How it shows up in visual-spec:
  - [/vspec:refine](../../README.md#commands) updates the canonical requirement and syncs impacted downstream artifacts
  - [/vspec:qc](../../README.md#commands) quickly exposes new omissions/contradictions after changes

### How the principles work together

1. Artifact collaboration (1) defines the layered structure for alignment  
2. Scenario-driven decomposition (2) + permissions-first (3) remove ambiguity early and make reviews concrete  
3. Implementation-friendly detail (4) + consistency/observability (5) define what “deliverable specs” mean  
4. Acceptance→automation→integration (6) + change-friendly requirements (7) close the loop for delivery and long-term evolution

### Quick index: principle → command → artifact

| Principle | Focus commands | Key artifacts |
| --- | --- | --- |
| 1. Collaborate through artifacts | [/vspec:new](../../README.md#commands), [/vspec:verify](../../README.md#commands) | `/specs/`, `/specs/models/`, `/specs/prototypes/` |
| 2. Scenario-driven decomposition | [/vspec:new](../../README.md#commands), [/vspec:accept](../../README.md#commands) | `/specs/` (flows/scenarios/functions), `/specs/acceptance/` |
| 3. RBAC and data permissions first | [/vspec:verify](../../README.md#commands), [/vspec:detail](../../README.md#commands) | `/specs/prototypes/`, `/specs/details/` |
| 4. Implementation-friendly detail | [/vspec:detail](../../README.md#commands), [/vspec:impl](../../README.md#commands) | `/specs/details/`, `/specs/backend/` (if enabled) |
| 5. Consistency & observability by default | [/vspec:detail](../../README.md#commands), [/vspec:qc](../../README.md#commands) | `/specs/details/`, `/specs/qc_report.*` |
| 6. Acceptance→automation→integration | [/vspec:accept](../../README.md#commands), [/vspec:append-test](../../README.md#commands), [/vspec:impl](../../README.md#commands) | `/specs/acceptance/`, test directories or `/tests/` |
| 7. Requirements that are easy to change | [/vspec:refine](../../README.md#commands), [/vspec:qc](../../README.md#commands) | canonical requirement (e.g. `original.md`) + impacted `/specs/` artifacts |

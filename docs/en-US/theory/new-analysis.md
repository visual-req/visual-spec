## Why `/vspec:new` analyzes so many dimensions

[English](../../en-US/theory/new-analysis.md) | [中文](../../zh-CN/theory/new-analysis.md) | [日本語](../../ja-JP/theory/new-analysis.md)

`/vspec:new` is not trying to “summarize a requirement”. Its goal is to produce reusable baselines that downstream stages can rely on. The reason it analyzes many dimensions is that implementation and testing constraints live across multiple axes, and a single narrative PRD rarely becomes stable engineering input by itself.

### Thinking modes used by `/vspec:new`

- Common thinking modes: boundary thinking, symmetry thinking, constraint thinking, diversity thinking  
  - See: [theory/thinking-modes.md](thinking-modes.md)
- Stakeholder identification thinking: systematically identify decision makers and reviewers via value chain / permissions & data / failure & compensation / milestones  
  - See: [theory/stakeholder-identification.md](stakeholder-identification.md)

### What `/vspec:new` typically extracts (and why)

- Roles and stakeholders
  - Why: RBAC, visibility, approvals, and data permissions depend on clear roles
- Terms and definitions (glossary)
  - Why: inconsistent semantics cause review conflicts and implementation ambiguity
- Scenarios
  - Why: the backbone for “flow → functions → pages → data → acceptance”; used for analysis/confirmation/validation and also drives acceptance case generation via `/vspec:accept`
- Flows and states
  - Why: boundaries and edge cases are usually state/flow problems
- Function list and scope boundaries
  - Why: estimation, acceptance scope, and test scope require explicit boundaries
- Dependencies (external systems)
  - Why: integrations impact APIs, reliability, retries/compensation, and failure handling
- Open questions
  - Why: make uncertainty explicit and track decisions before implementation

### Why not postpone this to later stages

- Later changes have higher blast radius: roles/scenarios/definitions affect details, prototype, acceptance, and implementation inputs
- Review later is more expensive: late feedback triggers chain rework
- Quality gates need baselines: QC/acceptance/planning need structured inputs

### How downstream commands reuse it

- `/vspec:detail`: expands functions and scenarios into implementation-ready detail specs
- `/vspec:verify`: builds runnable prototypes from details and selected stack
- `/vspec:accept`: converts scenarios into acceptance cases
- `/vspec:impl` and `/vspec:append-test`: reduce adoption cost by reusing traceable artifacts

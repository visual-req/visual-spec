## Quality Check: why these rules are “sufficient”

The rules used by `/vspec:qc` come from `quality_standard.md`. They are not an industry-specific template. They are an executable checklist that turns “what a high-quality requirement must answer” into verifiable items.

### 0) Quality dimensions and how to operationalize them (9)

Quality checking is not “subjective scoring”. It breaks quality into checkable dimensions, and for each dimension defines: defect taxonomy → questions → how to locate → how to fix → how to accept.

- Completeness: whether all required objects and branches are covered
  - Typical defect taxonomy: missing roles, missing scenarios, missing states, missing exceptions/compensations, missing constraints, missing artifacts (fields/logs/audit/reports)
  - How to check: build a coverage checklist first (role × action × data scope × scenario branch × state changes), then verify the spec explicitly defines each item
  - How to fix: add missing items and bind them to scenarios and acceptance cases (avoid “just prose” that cannot be verified)
- Correctness: consistency with facts/rules and internal logical soundness
  - Defects: contradictory rules, unreachable/no-exit state machines, conflicts with contract/production policies
  - How to check: counterexample reasoning, cross-check against source-of-truth rules/data, boundary derivations
  - How to fix: name the decision owner and authoritative reference, then rewrite rules with examples
- Precision: measurable, implementable semantics
  - Defects: unclear time semantics (TZ/business day), missing bounds, missing rounding/precision rules, unclear defaults
  - How to check: for each core field/metric require definition + unit + precision + range + default + examples
  - How to fix: codify into field/rule tables and cover boundary values in acceptance
- Flexibility: ability to respond to change (scope/rules/policies)
  - Defects: unclear change boundaries, hard-coded rules inside flows, missing versioning semantics, no safe rollout/rollback path
  - How to check: explicitly define “what can change vs. what must not”, change impact surface (state/data/permissions/dependencies), and validation + rollback strategy
  - How to fix: extract variable parts into rule tables/config/policies, add migration/compat plan, and cover change scenarios in acceptance and drills
- Reusability: reusable models rather than one-off delivery text
  - Defects: rules scattered everywhere, inconsistent terminology, missing reusable models (RBAC/data permissions/resource calendar/events)
  - How to check: extract reusable “models and lists” (glossary, rule tables, permission points, event schema) and reference them from scenarios
  - How to fix: move common parts into shared definitions; scenarios describe only deltas
- Readability: readers can understand and find answers fast
  - Defects: poor structure, missing diagrams/tables, key definitions buried in paragraphs
  - How to check: conclusion-first structure, tables for key objects, clear entry diagram + output list per module
  - How to fix: restructure, add summaries/tables, and make navigation obvious
- Consistency: same concepts/fields/flows are consistent across the document
  - Defects: same name different meaning, same meaning different names, mismatch between diagram/text/api/cases
  - How to check: maintain a glossary/field table as single source of truth; align diagrams, tables, APIs, and tests
  - How to fix: unify naming/definitions and record changes at the glossary/field/state level
- Implementability: feasible with reasonable engineering cost
  - Defects: missing dependency boundaries, missing failure strategies, missing idempotency/concurrency semantics, missing ops/observability requirements
  - How to check: for critical paths build dependency list + failure matrix + state machine + data flow; require degrade/rollback/compensation
  - How to fix: add boundary/strategies and adjust scope or split milestones to keep a deliverable closed loop
- Testability: verifiable by acceptance/automation, not “looks fine”
  - Defects: no observable outputs, scenarios not enumerable, acceptance criteria subjective
  - How to check: every core rule maps to at least one executable acceptance case; every exception path has observable evidence
  - How to fix: turn rules into Given/When/Then cases with assertions and required test data + permission/data-scope preconditions

Note: you usually cannot “prove completeness” directly. Instead, classify completeness into the defect categories above (roles/scenarios/states/exceptions/constraints/artifacts) and verify via a coverage checklist. This turns completeness into an actionable QA plan.

### 1) Industry-agnostic: it checks structure and verifiability

The checklist does not rely on domain jargon. It checks whether requirements are implementable and testable, for example:

- Goal & scope: clear goals/non-goals and decision boundaries
- Roles & permissions: who can do what and who can see what (access control and data permissions)
- States & constraints: state transitions, preconditions, limits, exceptions and compensations are closed-loop
- Consistency: time semantics, upper/lower bounds, formula precision, field definitions are consistent and traceable
- Acceptance & testability: scenarios can be enumerated and acceptance cases cover key branches and constraints
- Risks & dependencies: failure strategies, retries, idempotency, rollback, auditability and alerting are explicit

These dimensions are universal for software delivery, regardless of industry.

### 2) Why it is “sufficient”: it targets common failure modes

The point is not to enumerate every business detail. The point is to surface the high-frequency gaps that cause rework, incidents, and acceptance disputes, such as:

- Only the happy path is described; no cancel/reject/withdraw/compensation, making operations impossible
- Permissions are one-liners without permission points and data scope, leading to authorization bugs and churn
- Missing time/precision/bounds semantics, leading to inconsistent implementation and acceptance arguments
- Missing external dependency failure handling, leading to unrecoverable states and poor accountability

### 3) Battle-tested: distilled from repeated delivery feedback

This checklist is iterated through requirement reviews, implementation alignment, acceptance disputes, and postmortems. Each rule maps to a real defect class, rewritten into an item that can be checked, located, and fixed with actionable guidance.

### 4) Methodology first, prompts second

The key step is: methodology first, prompts second. Use abstraction and thinking modes to fix the dimensions (boundaries, symmetry, constraints, diversity), then use prompts to produce structured outputs. Ad-hoc prompts without methodological support rarely achieve stable completeness and reuse across teams.

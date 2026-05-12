## Abstraction: one flows diagram for all approval workflows

The purpose of `visual-spec-flows.svg` is not to model a single product. It is a reusable abstraction that can normalize most approval / routing workflows into the same backbone, making review, estimation, and implementation alignment much easier.

![visual-spec flows](../../assets/en-US/visual-spec-flows.svg)

This is one abstraction example for approval/routing workflows. In real systems there are many other abstractions (e.g., resource scheduling, billing & settlement, risk/eligibility, inventory & fulfillment, reconciliation & money flow, event-driven collaboration). They are not enumerated here.

The key step is: abstract first, then design prompts. Abstraction fixes the dimensions and boundaries you must cover; prompts turn those dimensions into stable, repeatable output. Without methodological support, “ad-hoc prompts” rarely produce the same level of completeness, implementability, and verifiability.

### Why this abstraction matters

Approval-type workflows share the same skeleton (request → approval → execution → post), while differences mainly come from:

- How the approval chain is configured (levels, countersign, conditional routing)
- What constraints gate execution (validation, limits, compliance, concurrency, idempotency)
- What exception controls exist (cancel/reject changes, emergency stop, emergency change, conflict resolution)

By standardizing the skeleton, analysis focuses on “what is special here” instead of redrawing a new flow every time.

### Prompt-driven analysis design

To make model outputs stable, treat this diagram as a checklist in prompts:

- Produce a mapping table: for each step, list roles, inputs, outputs, and state transitions
- Produce a constraints list: validations, constraints, failure strategies, idempotency keys, concurrency limits
- Produce control paths: cancel/reject/withdraw/rollback/compensation conditions and permissions
- Produce verification artifacts: acceptance cases that cover each branch and key constraint

### Shared properties (via thinking-modes)

After abstraction, most approval/routing workflows share the same structure: a stable main path + enumerable control paths + a checklist of execution constraints. Use [thinking-modes.md](file:///Users/stephenwang/Documents/trae_projects/my_skills/docs/en-US/theory/thinking-modes.md) to make the “differences” explicit:

- Boundary thinking: scope/roles/permissions/time/data boundaries
- Symmetry thinking: reverse flows and compensations (revoke/rollback/idempotency)
- Constraint thinking: validations, state machine rules, audit/compliance, concurrency limits
- Diversity thinking: multi-role, multi-scenario, multi-channel coverage

In complex businesses, “approval” and “execution” are often multi-step subflows; the key is to keep them aligned to the same control/constraint/artifact dimensions.

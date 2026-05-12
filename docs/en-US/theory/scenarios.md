---
title: Scenarios (Branching Cases)
---

This page explains how the analysis method in [abstraction.md](file:///Users/stephenwang/Documents/trae_projects/my_skills/docs/en-US/theory/abstraction.md) helps you systematically derive a “scenario set”, and how those scenarios capture boundaries and constraints that power downstream detailed specs, prototyping, and acceptance tests.

This “main path + scenario branches + role swimlanes” way of communication is also business-friendly: stakeholders tend to understand systems in terms of “what scenarios happen / who does what / what exceptions exist”, rather than starting from APIs, tables, or implementation details.

![Enterprise fleet scenarios (example)](../../assets/en-US/visual-spec-scenarios.svg)

## From Abstraction to Scenarios

Abstraction (flows) answers “what dimensions must be covered”. Scenarios answer “what those dimensions look like in this business”.

- After mapping the workflow into flows, you get a stable backbone (main steps), control paths (cancel/reject/withdraw/rollback), and constraint gates (validations/constraints/failure strategies).
- For each step, split by role and enumerate “who can do what / cannot do what / when”. This naturally yields a list of scenarios (change/cancel/revoke, emergency stop/change, conflict handling, etc.).
- Putting scenarios into swimlanes makes accountability explicit: who triggers, who processes, who confirms, and who owns compensations/rollbacks.

## What Each Scenario Should Capture

A scenario is not just a label. It should carry information that is implementable and verifiable:

- Trigger conditions: who triggers it, under which states, and whether concurrency is allowed.
- Preconditions and constraints: validations, resource availability, feasibility constraints (e.g., location, travel time, working-hour rules).
- State transitions: what state changes, what fields are written, and whether bookings are created/updated/removed (e.g., calendar bookings).
- Failures and compensations: how failures are surfaced, retry policy, rollback/compensation, and idempotency strategy.
- Permission boundaries: which roles/permissions can perform this scenario (who can revoke, who can emergency-stop, who can emergency-change).

## How It Helps Downstream Work

- Detailed analysis: scenarios become the checklist for the “differences”, driving state machines, fields, permissions, rules, and exception handling into PRD-level detail.
- Prototyping: scenarios determine the required branching UI states (normal, unavailable, conflict, revoked, changing, rolled back), avoiding happy-path-only prototypes.
- Acceptance tests: scenarios become the test skeleton, covering the main path plus all control paths and critical constraints with explicit preconditions and expected outcomes.

## Using Scenarios to Define Delivery Scope

Scenarios are not only for completeness but also for making trade-offs. When resources are limited, you can tier scenarios by likelihood and business value to define what is in scope for a release and what is not:

- Likelihood: prioritize high-frequency main flows and common exceptions (e.g., revoke/change). Rare edge cases can be deferred, but risk and fallback must be explicit.
- Business value: prioritize scenarios that directly impact revenue/cost/compliance/experience. Low-value but high-effort scenarios can be delayed or simplified.
- Combined decision: use “likelihood × value × risk (compliance/loss/reputation)” to rank priority, and write P0/P1/P2 boundaries into both scope and acceptance criteria.

This makes reviews clearer: what will be covered now, what will not, and what needs a placeholder (API extension point, degradation, or manual handling) to stay safe.

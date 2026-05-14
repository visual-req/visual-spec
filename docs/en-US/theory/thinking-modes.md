## Thinking modes used by `/vspec:new`: boundary / symmetry / constraints / diversity

[English](../../en-US/theory/thinking-modes.md) | [中文](../../zh-CN/theory/thinking-modes.md) | [日本語](../../ja-JP/theory/thinking-modes.md)

This document describes several thinking modes that `/vspec:new` uses to turn natural-language requirements into reviewable, implementation-ready artifacts. These are not templates; they are tools to reveal missing information, contradictions, and decision points.

### 1) Boundary thinking

- Clarify scope and non-scope, applicability, and edge conditions
- Identify boundaries: role boundaries, data boundaries, time boundaries, org boundaries, permission boundaries

### 2) Symmetry thinking

- Derive rollback/compensation from the happy path
- Mirror “create” with “edit/cancel/rollback/reverse/refund”
- Mirror “success” with “failure/retry/idempotency/duplicate submission”

### 3) Constraint thinking

- Make implicit constraints explicit: validation rules, authorization rules, state machine constraints, data semantics
- Make system constraints explicit: reliability, auditability, compliance, traceability, alerting

### 4) Diversity thinking

- Cover variations across roles, scenarios, channels, devices, org structures, and operating modes
- Focus on role differences (especially for dashboards and prototypes)

### 5) Closed-loop thinking

Business requirements often focus only on the “core moment” and miss the two ends:

- Pre-processing: what must be true before the core action (prerequisites, data preparation, authorization, validation, initialization)
- Post-processing: what must happen after the action (state sync, notifications, logs, reconciliation/compensation, and a clear end condition)

Closed-loop thinking expands a point requirement into an end-to-end deliverable loop, ensuring pre- and post-processing are analyzed so gaps don’t surface late during implementation or acceptance.

Typical prompts:

- “What prerequisites must hold before this action? What happens if they don’t?”
- “After success/failure, what post-actions must the system perform?”
- “How do we know the process is truly finished (async notifications, retries, compensation, reconciliation)?”

### 6) Action–course mapping (example output)

In course-based products, requirements often describe “the course” but omit the concrete actions that make the course usable. A simple action–course mapping helps reveal missing entry points, permissions, validations, and state transitions.

Example (partial):

| Course object | User action | Expected state change | Key spec focus |
| --- | --- | --- | --- |
| Course | browse/search | none | filters, sorting, visibility rules |
| Course | enroll/purchase | enrolled | payment, idempotency, access control |
| Lesson | play/pause/seek | progress updated | tracking, rate limiting, anti-abuse |
| Lesson | complete | completed | completion criteria, retries, offline sync |
| Course | certificate | certificate issued | eligibility rules, audit, notification |

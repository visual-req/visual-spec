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

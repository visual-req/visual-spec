## Design Principles

### 1. Collaborate Through Artifacts

- Turn “discussion” into “reviewable artifacts” to reduce alignment cost
- Artifacts progress by layers: raw requirement → specs (`/specs`) → models (`/specs/models`) → prototype (`/specs/prototypes`) → details (`/specs/details`) → acceptance/tests/code

### 2. Scenario-Driven Decomposition (Not Feature Piling)

- Use node chains (apply/approve/cancel/change/execute-start/execute-end, etc.) to cover the happy path and rollback paths
- Drive details from scenarios: every function point should map to “executable user actions + verifiable expected outcomes”

### 3. RBAC and Data Permissions First

- RBAC down to page sections and controls to avoid “page is visible but buttons shouldn’t be clickable”
- Model data permissions independently (row/column/scope/status/org) and compose them with RBAC (authorize first, then filter)

### 4. Implementation-Friendly Detail

- Express page load, interactions, and post-submit behavior as checklists/tables for engineering implementation and review
- Use “matrices” for validation/logging/notifications to ensure complete coverage and traceability

### 5. Consistency and Observability by Default

- Provide explicit specs for external dependencies, MQ, retries, DLQ, compensations, etc.
- Require traceability (trace_id/request_id), auditability (activity logs), and alertability (failures/backlogs) by default

### 6. Acceptance → Automation → Integration

- Use acceptance cases as a shared language for dev and QA
- Prefer reusing existing test frameworks and directory conventions to reduce maintenance
- Generated code focuses on minimal reviewable diffs and a runnable end-to-end loop

### 7. Requirements That Are Easy to Change

- Generated requirement docs should be editable, readable, easy to spot issues, easy to fix, and quick to adapt to changes.

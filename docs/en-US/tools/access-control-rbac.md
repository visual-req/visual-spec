## Access Control (RBAC)

Turns “who can do what” into an implementable, testable, auditable permission model, so permissions don’t degrade into vague one-liners and inconsistent implementations.

When to use:
- Multi-role systems (ops/reviewer/finance/compliance/admin/external collaborators)
- Permissions must reach page areas/buttons, APIs, and operation/action level

Core concepts:
- Role: a bundle of permissions (e.g., dispatcher, driver, finance, admin)
- Permission key: the smallest grantable action (e.g., `order:approve`, `dispatch:revoke`)
- Resource: what the permission applies to (page, API, feature, menu, data entity)
- Action: the operation on the resource (read/create/update/delete/approve/export)

RBAC table format (recommended to be written directly into each feature’s `rbac.md`):

Role table:
| Role | Responsibility / Boundary | Typical Operations | Notes |
|---|---|---|---|
| Admin | ... | ... | ... |

Permission key table (single source of truth for both frontend and backend):
| Permission Key | Name | Resource Type | Resource Path | Action | Description | Related API | UI Control Point |
|---|---|---|---|---|---|---|---|
| order:approve | Approve Order | Page/Button | /orders/{id}#approve | approve | ... | POST /api/orders/{id}/approve | Order detail - Approve button |

Role-permission matrix (Allow / Deny / Conditional):
| Permission Key | Admin | Reviewer | Operator | Conditions (e.g., data scope / status) |
|---|---|---|---|---|
| order:approve | Allow | Allow | Deny | Only when status=Pending; org-scoped data only |

Execution notes:
- Use permission keys end-to-end: UI gating and backend authorization must share the same permission keys; never rely on “frontend hide-only” or “backend error-only”.
- Bind permissions to scenarios/cases: mark the triggering role in scenarios; acceptance cases must cover allow/deny copy and the default landing page when unauthorized.
- Default deny: anything not explicitly allowed in the matrix is denied, with consistent error codes and messages.
- Conditional must be executable: express conditions as implementable fields (data scope, org/tenant, status, ownership, time window), not free text.

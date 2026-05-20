## Authentication & Authorization

Used to separate "who you are (Authentication)" and "what you can do (Authorization)", translating them into implementable, auditable, and testable rules and API contracts.

Applicable Scenarios:
- Any system requiring login, role permissions (RBAC), data permissions, and audit accountability
- Systems requiring multi-client access (Web/App/Third-party) or exposing open APIs

Suggested Structure:
- Authentication (AuthN): account system, login methods, session (cookie/token), expiration and refresh, logout
- Authorization (AuthZ): RBAC permission points, data permission scopes, conditional permissions (state/fields/time window)
- Credentials and Security: key rotation, token binding to device/client, replay attack prevention
- Audit: trace of logins/critical operations (who/when/where/what/result)

Implementation Suggestions:
- Frontend button control and backend authorization must be consistent: use "permission point + data scope" as the unified standard.
- Categorize authorization failures: not logged in (401), unauthorized (403), data scope miss (404/403, depending on strategy), and cover these in acceptance test cases.
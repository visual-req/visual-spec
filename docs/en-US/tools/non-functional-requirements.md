## Non-functional Requirements (NFRs)

Used early in requirement breakdown to make "quality attributes the system must possess" explicit and verifiable, avoiding breaking down only business features and patching them during implementation/stress testing/launch.

Applicable Scenarios:
- "Scope and alignment" of any business requirement before entering detail/verify/impl
- Systems with explicit constraints on performance, stability, security, compliance, observability, and operability

Types (tailor as needed; each category must be written to be "verifiable"):

### Performance

Focuses on "is it fast, can it handle the load", and whether it remains controllable under peaks and anomalies.
- Common Concerns: Response time (P50/P95/P99), throughput (QPS/TPS), concurrency, peaks, queue backlogs, batch processing windows, rate limiting and queuing strategies.
- Capacity Guidelines: Define capacity by "critical scenarios" rather than single APIs; e.g., end-to-end latency and success rate of "Order + Payment Callback + Inventory Deduction".
- Verification: Stress testing plan (dataset/concurrency model/peak curve/scaling strategy) + Post-launch dashboards (SLOs and alert thresholds).

### Reliability / Availability

Focuses on "can it consistently provide service", and whether it can recover and mitigate losses during faults.
- Common Concerns: SLA/SLO, degradation, circuit breaking, timeouts, retries, idempotency, rate limiting, isolation, disaster recovery, backup and restore, data consistency strategies.
- Fault Boundaries: Clarify which faults allow "partial unavailability" (e.g., exports/reports) and which must keep the "core flow available".
- Verification: Chaos engineering (injecting timeouts/dependency unavailability/rate limiting/active-standby switching) + RTO/RPO acceptance.

### Security

Focuses on "can it be bypassed, tampered with, leaked", and whether risks are auditable and traceable.
- Common Concerns: Authentication, authorization (RBAC/data permissions), session and token management, encryption (transit/storage), sensitive info handling, auditing, vulnerability risks (OWASP), supply chain security.
- Data Protection: Clarify which fields are sensitive (desensitized display/export limits/watermarks/access audits/least privilege).
- Verification: Permission cases (allow/deny/prompts), security testing (scanning/penetration/baseline checks), audit log sampling.

### Compliance

Focuses on "are mandatory rules implemented in system behavior", including retention, data lifecycles, privacy, and cross-border transfers.
- Common Concerns: Traceability and non-repudiation, data retention periods, access control, export limits, privacy terms, cross-border transmission, log retention, audit forensics.
- Lifecycle: Clarify the "collection → usage → sharing → archiving → deletion" strategy for data, defining trigger conditions and responsible parties.
- Verification: Audit checklist + forensics drill (can events be reconstructed by time/operator/object).

### Observability

Focuses on "can issues be quickly located", and whether key metrics are continuously monitored.
- Common Concerns: Logs (structured/correlation IDs), metrics (RED/USE), distributed tracing, alerts, key event tracking, business funnels, and anomaly rates.
- Minimum Observability Set: Every critical flow must have a `trace_id`, and critical actions must have operation logs and audit fields.
- Verification: Dashboard and alert drills (simulating increased error rates/latency/queue backlogs) to locate root causes within a time limit.

### Operability

Focuses on "are launches and changes controllable", and whether ops actions are repeatable, rollback-able, and auditable.
- Common Concerns: Configuration management, canary releases, rollback strategies, change windows, data migrations, feature flags, runbooks, on-call and emergency plans.
- Change Control: Clarify which changes require canary releases, which require downtime windows, rollback trigger conditions, and rollback steps.
- Verification: A simulated release (canary → expand → rollback) to verify the operability of data migration and rollbacks.

### Accessibility (a11y)

Focuses on "is it usable by disabled/elderly/temporarily restricted users", complying with laws or organizational standards (e.g., WCAG).
- Common Concerns: Keyboard accessibility (Tab order/visible focus), semantic structure (ARIA), contrast, scalable fonts, screen reader support, form error prompts, toggleable animations.
- Interaction Requirements: All core operations must be completable without mouse/touch precision; error prompts must be readable by screen readers.
- Verification: Automated scanning (a11y lint) + manual walkthroughs (keyboard/screen reader/high contrast) + key page acceptance checklists.

### Locale & Cultural Conventions

Focuses on "are habits of users in different regions respected", avoiding misuse or complaints due to incompatible formats, expressions, or processes.
- Common Concerns: Language and terminology, time/time zones/calendars, number and currency formats, decimal/thousands separators, address formats, name order, phone number rules, holidays and workdays, color/icon meanings, compliance copy differences.
- Interaction Requirements: Time and amounts must specify time zones/currencies; default formats vary by region but allow user switching; don't hardcode cultural assumptions in rules.
- Verification: Regional test cases (formatting/sorting/searching/validation/exports) + key copy reviews (localization and compliance).

### Compatibility

Focuses on "can it run in target environments", including browsers, devices, OS versions, API versions, and external dependencies.
- Common Concerns: Browser/device matrix, resolutions and input methods (mouse/touch), API version compatibility, external dependency compatibility and replacement strategies, degradation strategies.
- Version Strategy: Clarify minimum supported versions and deprecation strategies; breaking changes require migration windows and compatibility layers.
- Verification: Compatibility matrix testing (mainstream + minimum support) + regression baselines + dependency replacement drills (mock/degradation).

### Portability

Focuses on "how high is the migration cost", including deployment environment migration, cloud vendor migration, DB/middleware replacement, and regional expansion.
- Common Concerns: Environment-agnostic configurations (12-factor), infrastructure abstractions, replaceable dependencies (DB/Cache/MQ/Object Storage), data migration and rollback, cross-region deployment.
- Architectural Constraints: Avoid hardcoding vendor features in the business layer; dependencies must have minimum feature sets and adapter layers.
- Verification: Complete an end-to-end deployment and regression in a second environment (or local containerized environment); perform replacement verification on core dependencies (e.g., switching DB/MQ).
## Cache

Used to express "what data can be cached, where it is cached, when it invalidates, and how to maintain consistency and origin fallback", avoiding caches being added ad-hoc during implementation which leads to dirty reads, penetration, and avalanches.

Applicable Scenarios:
- Hotspot reads (lists/details/configs/dictionaries)
- Computationally expensive or slow external dependencies (aggregated reports, permission/scope resolution, third-party queries)

Suggested Structure:
- Cache Object: cache key, value, dimension (tenant/user/role/resource)
- Location: browser/local process/Redis/CDN
- TTL and Invalidation: expiration strategy, active invalidation, double-write/delayed double-delete
- Consistency: allowed stale window, origin fallback strategy, idempotency and concurrency control (single flight/lock)
- Risks: penetration/breakdown/avalanche and fallbacks (degradation, rate limiting, warmup)

Implementation Suggestions:
- Clearly state "hit rate target" and "invalidation trigger conditions" for each cache, and verify invalidation correctness when key scenarios change.
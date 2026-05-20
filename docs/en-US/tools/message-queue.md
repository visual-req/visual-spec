## Message Queue (MQ)

Used to express the logic of "how asynchronous events/tasks flow": what the event is, who produces/consumes it, ordering and idempotency, failure retries, and dead letters, avoiding just saying "send to MQ" without being verifiable.

Applicable Scenarios:
- Asynchronous decoupling (async processing after submission, notifications, reconciliation)
- Event-driven (state changes trigger downstream actions)
- Peak shaving and valley filling (writing to queue during peaks, background consuming slowly)

Suggested Structure:
- Event Definition: topic, event name, schema, versioning strategy
- Producer: in which scenario it's generated, trigger conditions, transactional consistency (outbox/transactional messages)
- Consumer: processing logic, idempotency keys, retry strategy, ordering requirements
- Failure Handling: DLQ, alerts, manual compensation, replayability
- Observability: delivery/consumption latency, backlog volume, failure rate, traceId penetration

Implementation Suggestions:
- Every event must define an "idempotency key + deduplication window", and acceptance test cases must cover duplicate delivery and out-of-order scenarios.
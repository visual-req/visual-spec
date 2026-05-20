## Cron Jobs

Used to express "background processing triggered periodically", including scheduling frequency, idempotency, concurrency control, and failure compensation.

Applicable Scenarios:
- End-of-day reconciliation, batch settlement, billing
- Data synchronization, cleanup, archiving
- SLA monitoring, alert scanning

Suggested Information to Include:
- Trigger: cron expression/scheduling platform, time zone, execution window
- Input: scan range, sharding strategy, cursor/watermark
- Output: write data, notification/alert, traceable logs
- Idempotency: how to avoid duplicate deductions/shipments/notifications upon repeated execution
- Failure: retry, rollback, manual intervention, and compensation plans

Implementation Suggestions:
- Clarify concurrency limits and locks (by tenant/task/batch)
- Clarify observability (execution time, success rate, failure reason distribution)
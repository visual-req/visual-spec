## Swimlane Diagram

Used to express "cross-role/cross-system collaboration processes", emphasizing responsibility boundaries: who does it, where it is done, and where the handover points are.

Applicable Scenarios:
- Multi-role participation (customer/ops/finance/compliance/third-party)
- Multi-system collaboration (main system + external channels + reconciliation system)

Suggested Structure:
- Swimlane Dimension: Role / System / Department / Service (choose one as primary)
- Handover Points: Events/messages/API calls/file deliveries
- Key Outputs: Inputs/outputs for each swimlane stage

Implementation Suggestions:
- Clarify the protocol for each handover point (API, MQ, File, Manual Operation)
- Clarify failure attribution and compensation responsibilities (which party retries/rollbacks/intervenes manually)
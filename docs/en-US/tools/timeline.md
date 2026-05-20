## Timeline

Used to express "the sequence, dependencies, and parallel relationships of events over time", as well as the inputs/outputs and responsibility boundaries of different stages.

Applicable Scenarios:
- Business lifecycle (Application → Approval → Execution → Reconciliation/Settlement → Archiving)
- State evolution and key milestones (Start/Pause/Rollback/Terminate)
- Version release rhythm, canary, rollback windows, data migration windows

Suggested Information to Include:
- Time Points/Periods: trigger conditions, prerequisites, output results
- Participating Roles: who triggers/who approves/who executes/who monitors
- Risk Points: failure fallbacks, compensation paths, timeout strategies

Suggested Output Formats:
- Linear Timeline (single main thread)
- Branching Timeline (parallel/fork/merge)
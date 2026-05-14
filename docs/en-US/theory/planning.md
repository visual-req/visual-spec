## Planning: scope breakdown, estimation, and scheduling (`/vspec:plan`)

[English](../../en-US/theory/planning.md) | [中文](../../zh-CN/theory/planning.md) | [日本語](../../ja-JP/theory/planning.md)

`/vspec:plan` is not meant to “guess a timeline”. It turns stabilized requirements into a traceable delivery plan by breaking down work, estimating with story points, and loading the work into iterations in a review-friendly story map.

### Preconditions and outputs

- Preconditions (typically hard gates): `/vspec:detail` has produced implementation-ready specs, and `/vspec:qc` has run as a quality gate
- Outputs:
  - `/specs/plan/plan_estimate.md`: story point estimates aligned with the function list
  - `/specs/plan/plan_story_map.json`: the story map data (structured and reusable)
  - `/specs/plan/plan_schedule.html`: the story map HTML template (loads and renders the JSON)

### Scope breakdown: from scenarios to deliverable slices

Breakdown is only useful when it preserves deliverability, verifiability, and traceability.

- Use scenarios as the backbone: connect “flow → feature → UI/API → data/rules → acceptance” to avoid slicing by menus/pages only
- Use vertical slices as the unit of delivery: prioritize a P0 end-to-end happy path that can be demonstrated and validated early
- Split by dependency and risk: when external dependencies are unclear, schedule internal-only slices first (models/UI/flows/mocks), and move real integrations to later sprints with explicit blockers
- Enforce size constraints: if an item is too large to track/review, keep splitting until each item is small enough (for example, keep each item within SP<=13)

### Estimation: story points as the loading unit

visual-spec uses Story Points (SP) to express relative cost and uncertainty for iteration planning.

- Keep a shared scale: estimate similar work consistently across the plan
- Make uncertainty explicit: add risk tags for unknowns (dependencies, definitions, resource constraints)
- Avoid oversized items: large cards hide risk and make progress tracking misleading; split while keeping traceability

### Scheduling: turning an estimate table into an iteration plan

A schedule is a decision artifact: goals, capacity, dependencies, and risks must be visible in one place.

- Organize by sprint goals: each sprint should state what it delivers and what can be validated
- Load by capacity: use velocity (or derived capacity) and apply a buffer ratio to reserve time for unknowns, acceptance, and release
- Sequence by constraints: close the core path first; respect serial dependencies and parallelism limits
- Plan the acceptance loop: testing/acceptance/release windows belong in the plan, not as “extra work later”

### Why the story map is HTML

The primary job of the story map is cross-stakeholder review, where HTML is a better entrypoint than plain text tables.

- Two-dimensional visibility: “sprint × module” makes scope and coverage obvious at a glance
- Low review friction: open in a browser and review together (PM/Dev/QA/Business)
- Faster iteration: each card can show estimate and blockers without switching between documents

### Why JSON + an HTML template (load and render)

`/vspec:plan` separates planning data from presentation so updates are cheaper and diffs are cleaner.

- Reusable data: JSON is easy to consume for exports, dashboards, and comparisons
- Evolving UI: the HTML template can improve interaction (filter/search/highlight risk) without changing the data model
- Controlled changes: most plan updates land in JSON, while the rendering stays stable

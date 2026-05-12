## Why scenarios are output as HTML and linked to the prototype

[English](../../en-US/theory/prototype-review.md) | [中文](../../zh-CN/theory/prototype-review.md) | [日本語](../../ja-JP/theory/prototype-review.md)

Review inefficiency usually comes from:

- People review different things (PRD vs prototype vs verbal notes), so conclusions are not reusable
- Feedback is hard to anchor to a concrete scenario/page/action, so it’s not traceable
- Validating behavior is expensive: issues surface only after implementation starts

visual-spec addresses this by providing an HTML review entry for scenarios and linking it to a runnable prototype.

### Why HTML (not only Markdown)

- Better review navigation: clickable entry, jump-to, cross-links, and fast location of scenarios/pages
- More accessible for non-technical stakeholders: open in a browser with consistent rendering
- Easier to “task-ify” reviews: lists can be reviewed item by item with less cognitive load

### Why “scenario list ↔ prototype linking”

- Scenarios are the smallest effective review unit: users validate “how the flow works”, not only pages
- Scenarios connect roles and permissions: role-based visibility/actions can be validated directly
- Scenarios expose data semantics early: field meanings, statuses, money/time rules, edge cases
- Review results transfer downstream: validated scenarios can be converted to acceptance cases and tests

### Why this improves stakeholder review

- Feedback becomes anchorable and traceable (scenario/page/action)
- Reduces “imagination cost”: validate assumptions via a runnable prototype
- Shortens feedback loops: refine updates can sync prototype/specs downstream

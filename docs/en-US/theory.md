## Theory

[English](../en-US/theory.md) | [中文](../zh-CN/theory.md) | [日本語](../ja-JP/theory.md)

This section explains the core design philosophy of the visual-spec Skill: how it maps to SDLC, why the workflow is split into these command stages, why scenarios are output as an HTML review entry that links to the runnable prototype, and why `/vspec:new` analyzes “so much” up front.

### Visual workflow

![visual-spec workflow](../assets/visual-spec-workflow-en.svg)

### Index

- SDLC mapping: why the command stages exist and how they align with SDLC  
  - See: [theory/sdlc.md](theory/sdlc.md)
- Planning: how to break down scope, estimate, and schedule, and why the story map is HTML (`/vspec:plan`)  
  - See: [theory/plan.md](theory/plan.md)
- Review ergonomics: why scenario lists are HTML and how they link to prototypes to make reviews faster  
  - See: [theory/prototype-review.md](theory/prototype-review.md)
- Verification & Validation: the review loop (review → refine → re-validate)  
  - See: [theory/verification_and_validation.md](theory/verification_and_validation.md)
- Why `/vspec:new` analyzes many dimensions and how each output is reused downstream  
  - See: [theory/new-analysis.md](theory/new-analysis.md)
- Analysis thinking: break “requirements analysis” into reusable modules  
  - See: [theory/thinking-framework.md](theory/thinking-framework.md)

### One-line summary

visual-spec is designed to turn requirements into an end-to-end, traceable, reviewable delivery chain: scenarios as the backbone, connected to roles, rules, data models, and a runnable prototype, so teams can align before implementation and keep downstream artifacts in sync when requirements change.

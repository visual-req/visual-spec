---
name: "visual-spec-skill"
description: "Analyzes raw requirements into visual specs and generates artifacts. Invoke when user runs /vspec:new for analysis or /vspec:verify for models and prototypes."
---

# Visual Spec Skill

Analyzes visual specifications based on user input and turns brief business requests into structured requirement output.


## When to Use

Invoke this skill when:
- Business side provided a very simple described requirements.
- User runs `/vspec:new` to start a new requirement analysis flow.

## What This Skill Defines

- Fill in details based on scenario-based-facilitation method.
- Design the data models.
- Generate UI mockups based on the details filled in.
- Generate business logic details in visual formats.

## Commands

### `/vspec:new`

Use this command to create a new requirement analysis session.

Flow:
1. Ask the user to input the original requirement.
2. When the user presses Enter, treat the input as the raw requirement source.
3. Load the prompt file at `prompts/vspec_new/background.md`.
4. Use that prompt to analyze the requirement and expand the business context.
5. Write the raw requirement and background analysis output to `/specs/background/original.md`.
6. Ask the user to answer the questions from the `待确认问题` section.
7. After the user replies, load `prompts/vspec_new/stakeholders.md` to analyze stakeholders.
8. Write the stakeholder result to `/specs/background/stakeholder.md` (markdown table).
9. Load `prompts/vspec_new/roles.md` to analyze system user roles (direct users) and their work tasks.
10. Write the roles result to `/specs/background/roles.md`.
11. Load `prompts/vspec_new/terms.md` to extract key terms and definitions.
12. Write the terms result to `/specs/background/terms.md` (markdown table).
13. Load `prompts/vspec_new/flows.md` to analyze business workflows and generate PlantUML swimlane diagrams.
14. Write the diagrams to `/specs/flows/*.puml`.
15. Load `prompts/vspec_new/scenarios.md` to enumerate business scenarios by node combinations.
16. Write the scenarios result to `/specs/background/scenarios.md` (markdown table).
17. Load `prompts/vspec_new/details_pre_post.md` to create per-node detail folders and generate `pre_post.md` for each node.
18. Load `prompts/vspec_new/details_constraints.md` to generate `constraints.md` for each node.
19. Load `prompts/vspec_new/details_variations.md` to generate `variations.md` for each node.
20. Load `prompts/vspec_new/details_boundaries.md` to generate `boundaries.md` for each node.
21. Load `prompts/vspec_new/details_symmetry.md` to generate `symmetry.md` for each node.
22. Ensure the per-node outputs are written under `/specs/background/scenario_details/`.
23. Load `prompts/vspec_new/dependencies.md` to analyze external dependency systems.
24. Write the dependencies result to `/specs/background/dependencies.md`.
25. Load `prompts/vspec_new/functions.md` to generate feature/function lists grouped by modules and external dependency systems.
26. Write the function lists to `/specs/functions/`.
27. Load `prompts/vspec_new/questions.md` to generate question lists and required business materials.
28. Write the questions result to `/specs/background/questions.md` (markdown table).
29. Return the structured analysis result and continue to the next requirement-design step.

### `/vspec:refine`

Use this command to refine and update the requirement based on a `refine.md` file, or based on one or more input files/directories provided as command arguments.

Flow:
1. If command arguments are provided, treat them as refine input sources (files/directories); otherwise ensure the refine instruction file exists at `/specs/background/refine.md` (or `/refine.md`).
2. Load `prompts/vspec_refine/refine.md` to apply the refinement and update the canonical requirement.
3. Append the refinement result to `/specs/background/original.md`.

### `/vspec:refine-q`

Use this command to refine and update the requirement based on answered questions.

Flow:
1. Read `/specs/background/questions.md` and pick answered rows.
2. Load `prompts/vspec_refine/refine_q.md` to merge answers into the canonical requirement.
3. Append the refinement result to `/specs/background/original.md`.

### `/vspec:verify`

Use this command to verify and prototype based on the analysis artifacts.

Flow:
0. If `/specs/background/questions.md` exists and contains unanswered questions, ask the user to answer them before continuing (allow skip per question, but ensure none remains unanswered).
1. Load `prompts/vspec_verify/model.md` to generate data models.
2. Write model files to `/specs/models/*.md`.
3. Generate a runnable page prototype based on functions, models, and roles; the prototype tech stack can be selected via `/scheme.yaml` (auto-created with defaults if missing).
4. Write the prototype to `/specs/prototypes/`.
5. Load `prompts/vspec_verify/validation.md` to generate a scenario validation web page.
6. Write the validation page to `/specs/prototypes/` and provide a `scenario.html` entry for access.

### `/vspec:proto-apply`

Use this command to generate/update the prototype focusing on “申请（Apply）” flow and pages.

Flow:
0. If `/specs/background/questions.md` exists and contains unanswered questions, ask the user to answer them before continuing (allow skip per question, but ensure none remains unanswered).
1. Ensure `/specs/models/` exists; if missing, load `prompts/vspec_verify/model.md` to generate models first.
2. Load `prompts/vspec_verify/prototype_apply.md` to generate/update the prototype.
3. Write changes to `/specs/prototypes/`.

### `/vspec:proto-approve`

Use this command to generate/update the prototype focusing on “审批（Approve）” flow and pages.

Flow:
0. If `/specs/background/questions.md` exists and contains unanswered questions, ask the user to answer them before continuing (allow skip per question, but ensure none remains unanswered).
1. Ensure `/specs/models/` exists; if missing, load `prompts/vspec_verify/model.md` to generate models first.
2. Load `prompts/vspec_verify/prototype_approve.md` to generate/update the prototype.
3. Write changes to `/specs/prototypes/`.

### `/vspec:proto-execute`

Use this command to generate/update the prototype focusing on “执行（Execute）” flow and pages (including mobile `/m/*` when applicable).

Flow:
0. If `/specs/background/questions.md` exists and contains unanswered questions, ask the user to answer them before continuing (allow skip per question, but ensure none remains unanswered).
1. Ensure `/specs/models/` exists; if missing, load `prompts/vspec_verify/model.md` to generate models first.
2. Load `prompts/vspec_verify/prototype_execute.md` to generate/update the prototype.
3. Write changes to `/specs/prototypes/`.

### `/vspec:proto-crud`

Use this command to generate/update the prototype focusing on generic CRUD admin pages (list/detail/create/edit) for configuration/master-data modules.

Flow:
0. If `/specs/background/questions.md` exists and contains unanswered questions, ask the user to answer them before continuing (allow skip per question, but ensure none remains unanswered).
1. Ensure `/specs/models/` exists; if missing, load `prompts/vspec_verify/model.md` to generate models first.
2. Load `prompts/vspec_verify/prototype_crud.md` to generate/update the prototype.
3. Write changes to `/specs/prototypes/`.

### `/vspec:detail`

Use this command to expand requirement details based on the function list.

Flow:
1. Read the feature/function list from `/specs/functions/*`.
2. For each function (page or non-page job), first determine which detail artifacts are actually involved, then only generate those artifacts; do not generate documents for non-involved parts.
   - Always generate the baseline docs:
     - `rbac.md`: RBAC permissions down to page areas and controls.
     - `data_permission.md`: data permission rules and scope.
   - Page-only:
     - `page_load.md`: page loading logic.
      - `interaction.md`: page interaction logic.
     - `validation_matrix.md`: validation logic in matrix format (only for submit-type pages/actions; if the page has no submit/save/approve/reject/cancel/change actions, skip).
     - `post_submit_check.md`: checks after submit (if the page has submit).
     - `post_submit_processing.md`: processing logic after submit (if the page has submit).
     - `post_submit_navigation.md`: post-submit return and navigation (if the page has submit).
   - Conditional (generate only if involved by the current function’s logic/scenarios/models/dependencies):
     - `logging_matrix.md`: operation/audit logging (only when the business requires change history retention, compliance audit, or non-repudiation; otherwise skip).
     - `decision_matrix.md`: decision matrix (决策矩阵) for operation availability under each status (if there is a status machine and operations vary by status/role).
     - `notification_matrix.md`: notifications (if there is any notification requirement).
     - `mq.md`: MQ topics/events/message schema/reliability details (if there is async events, queues, or cross-system eventing).
     - `file_import.md`: file import details (if there is any import entry/requirement).
     - `file_export.md`: file export details (if there is any export entry/requirement).
     - `formula.md`: calculation formulas and metric semantics (if there are any calculations/metrics).
     - `expression_tree.md`: expression tree (HTML) (if there is multi-level nested branching logic).
     - `code_rules.md`: numbering/code generation rules (if any codes/serial numbers are generated/assigned).
     - `judgemental_matrix.md`: judgemental matrix (判定矩阵) for multi-factor logic branching (if 2+ factors jointly decide outcomes).
   - Module-level (generate at most once per module, and only if involved):
     - `timeline.md`: time-axis visualization (HTML) for overall flow impact analysis (only when there is long time-span logic that affects flow decisions, e.g. effective/expiry, deadlines, grace periods, cross-day rules).
      - `state_machine.md`: status list + transitions + PlantUML state diagram (overall; not per function).
     - `nfp.md`: non-functional requirements summary for the module (overall; not per function).
     - `cron_job.md`: scheduled jobs summary for the module (overall; not per function).
3. Write only the generated (involved) detail documents:
   - Per-function: `/specs/details/<module_slug>/<logic_type>/<function_slug>.(md|html)`
   - Module-level: `/specs/details/<module_slug>/<logic_type>/overall.(md|html)`

### `/vspec:qc`

Use this command to run a quality check on the generated requirement artifacts under `/specs/`.

Flow:
1. Read built-in standard at `prompts/vspec_qc/quality_standard.md`.
2. If a requirement quality error book exists under project `qc/`, generate/update project root `quality_standard.md` based on it.
3. If project root `quality_standard.md` exists, merge it as supplementary/overriding standard.
4. Load `prompts/vspec_qc/qc.md` and generate a non-conformance checklist.
5. Write the report to `/specs/qc_report.md`.

### `/vspec:accept`

Use this command to generate acceptance test cases.

Flow:
1. Read `/specs/functions/*`, `/specs/background/scenarios.md`, `/specs/background/scenario_details/`, `/specs/background/roles.md`, `/specs/models/*.md`.
2. Load `prompts/vspec_accept/accept.md` to generate acceptance test cases covering core flows, exceptions, boundary, permissions, and data scope.
3. Write results to `/specs/acceptance/` (one subfolder per function) and generate an index at `/specs/acceptance/index.md`.

### `/vspec:test`

Use this command to generate automation test code based on acceptance cases and specs.

Flow:
1. Read `/specs/acceptance/`, `/specs/functions/*`, `/specs/details/`, and detect the existing test frameworks in the repository.
2. Load `prompts/vspec_test/test.md` to generate automation tests using the existing frameworks and conventions.
3. Write test code to the project test directories (or `/tests/` if no standard exists) and ensure it can run with existing scripts.

### `/vspec:impl`

Use this command to generate integrated frontend/backend code based on the specs.

Flow:
1. Read `/specs/functions/*`, `/specs/details/`, `/specs/models/*.md`, `/specs/background/dependencies.md`, and detect the current frontend/backend stacks and code conventions.
2. Load `prompts/vspec_impl/implement.md` to generate API contracts, backend endpoints/services, and frontend integration (API calls, pages, state) following repo patterns.
3. Write changes directly into the repository source code with minimal diffs and keep it reviewable.

### `/vspec:change`

Use this command to respond to requirement changes and update impacted artifacts.

Flow:
1. Ask the user to provide the change description and scope.
2. Read existing artifacts under `/specs/` (including `/specs/models/` and `/specs/prototypes/`) if present.
3. Load `prompts/vspec_change/change.md` to analyze impact, update affected documents, and generate a change log.
4. Write updated artifacts and a change log to `/specs/change_log.md`.

### `/vspec:plan`

Use this command to break down requirements, estimate efforts, and schedule via a user story map.

Flow:
1. Read `/specs/functions/*`, `/specs/background/roles.md`, `/specs/background/scenarios.md`, `/specs/details/`, `/specs/background/dependencies.md`.
2. Load `prompts/vspec_plan/estimate.md` to generate estimates aligned to the function list.
3. Write estimates to `/specs/plan_estimate.md`.
4. Load `prompts/vspec_plan/schedule.md` to generate the schedule and delivery map.
5. Write schedule HTML to `/specs/plan_schedule.html`.

## Prompt Files

- `prompts/vspec_new/background.md`: the prompt used right after `/vspec:new` receives the raw requirement.
- `prompts/vspec_new/stakeholders.md`: the prompt used after the user answers `待确认问题` to generate `/specs/background/stakeholder.md`.
- `prompts/vspec_new/roles.md`: the prompt used after stakeholder analysis to generate `/specs/background/roles.md`.
- `prompts/vspec_new/terms.md`: the prompt used after roles analysis to generate `/specs/background/terms.md`.
- `prompts/vspec_new/flows.md`: the prompt used after terms analysis to generate `/specs/flows/*.puml`.
- `prompts/vspec_new/scenarios.md`: the prompt used after flows analysis to generate `/specs/background/scenarios.md`.
- `prompts/vspec_new/details_pre_post.md`: the prompt used after scenarios analysis to generate per-node `pre_post.md` under `/specs/background/scenario_details/`.
- `prompts/vspec_new/details_constraints.md`: the prompt used after Pre/Post to generate per-node `constraints.md` under `/specs/background/scenario_details/`.
- `prompts/vspec_new/details_variations.md`: the prompt used after Constraints to generate per-node `variations.md` under `/specs/background/scenario_details/`.
- `prompts/vspec_new/details_boundaries.md`: the prompt used after Variations to generate per-node `boundaries.md` under `/specs/background/scenario_details/`.
- `prompts/vspec_new/details_symmetry.md`: the prompt used after Boundaries to generate per-node `symmetry.md` under `/specs/background/scenario_details/`.
- `prompts/vspec_new/dependencies.md`: the prompt used after details analysis to generate `/specs/background/dependencies.md`.
- `prompts/vspec_new/functions.md`: the prompt used after dependencies analysis to generate `/specs/functions/`.
- `prompts/vspec_new/questions.md`: the prompt used after functions analysis to generate `/specs/background/questions.md`.
- `prompts/vspec_refine/refine.md`: the prompt used by `/vspec:refine` to refine the requirement based on `refine.md`.
- `prompts/vspec_refine/refine_q.md`: the prompt used by `/vspec:refine-q` to refine the requirement based on answered questions.
- `prompts/vspec_verify/model.md`: the prompt used by `/vspec:verify` to generate `/specs/models/*.md`.
- `prompts/vspec_verify/prototype.md`: the prompt used by `/vspec:verify` to generate the Vue + Ant Design prototype under `/specs/prototypes/`.
- `prompts/vspec_verify/validation.md`: the prompt used by `/vspec:verify` to generate the validation web page with a `scenario.html` entry.
- `prompts/vspec_detail/rbac.md`: the prompt used by `/vspec:detail` to generate RBAC detail docs.
- `prompts/vspec_detail/data_permission.md`: the prompt used by `/vspec:detail` to generate data permission detail docs.
- `prompts/vspec_detail/page_load.md`: the prompt used by `/vspec:detail` to generate page loading logic docs.
- `prompts/vspec_detail/interaction.md`: the prompt used by `/vspec:detail` to generate page interaction logic docs.
- `prompts/vspec_detail/timeline.md`: the prompt used by `/vspec:detail` to generate time-axis HTML docs.
- `prompts/vspec_detail/formula.md`: the prompt used by `/vspec:detail` to generate formula docs.
- `prompts/vspec_detail/expression_tree.md`: the prompt used by `/vspec:detail` to generate expression tree docs.
- `prompts/vspec_detail/code_rules.md`: the prompt used by `/vspec:detail` to generate numbering/code rules docs.
- `prompts/vspec_detail/judgemental_matrix.md`: the prompt used by `/vspec:detail` to generate decision matrix docs.
- `prompts/vspec_detail/validation_matrix.md`: the prompt used by `/vspec:detail` to generate validation matrix docs.
- `prompts/vspec_detail/post_submit_check.md`: the prompt used by `/vspec:detail` to generate post-submit checks docs.
- `prompts/vspec_detail/post_submit_processing.md`: the prompt used by `/vspec:detail` to generate post-submit processing docs.
- `prompts/vspec_detail/post_submit_navigation.md`: the prompt used by `/vspec:detail` to generate post-submit navigation docs.
- `prompts/vspec_detail/mq.md`: the prompt used by `/vspec:detail` to generate MQ message design docs.
- `prompts/vspec_detail/logging_matrix.md`: the prompt used by `/vspec:detail` to generate logging matrix docs.
- `prompts/vspec_detail/notification_matrix.md`: the prompt used by `/vspec:detail` to generate notification matrix docs.
- `prompts/vspec_detail/nfp.md`: the prompt used by `/vspec:detail` to generate non-functional requirements docs.
- `prompts/vspec_detail/file_import.md`: the prompt used by `/vspec:detail` to generate file import docs.
- `prompts/vspec_detail/file_export.md`: the prompt used by `/vspec:detail` to generate file export docs.
- `prompts/vspec_detail/cron_job.md`: the prompt used by `/vspec:detail` to generate scheduled job docs.
- `prompts/vspec_accept/accept.md`: the prompt used by `/vspec:accept` to generate acceptance test cases.
- `prompts/vspec_test/test.md`: the prompt used by `/vspec:test` to generate automation test code.
- `prompts/vspec_impl/implement.md`: the prompt used by `/vspec:impl` to generate integrated frontend/backend code.
- `prompts/vspec_change/change.md`: the prompt used by `/vspec:change` to handle requirement changes.
- `prompts/vspec_plan/estimate.md`: the prompt used by `/vspec:plan` to generate `/specs/plan_estimate.md`.
- `prompts/vspec_plan/schedule.md`: the prompt used by `/vspec:plan` to generate `/specs/plan_schedule.html`.
- `prompts/vspec_qc/qc.md`: the prompt used by `/vspec:qc` to generate `/specs/qc_report.md`.
- `prompts/vspec_qc/quality_standard.md`: built-in quality standard used by `/vspec:qc`.

## Suggested Workflow

1. Install this skill.
2. Run `/vspec:new`.
3. Ask the user to input the original requirement and wait for Enter.
4. Load `prompts/vspec_new/background.md` and start requirement analysis.
5. Ask the user to answer `待确认问题`.
6. Load `prompts/vspec_new/stakeholders.md` and generate `/specs/background/stakeholder.md`.
7. Load `prompts/vspec_new/roles.md` and generate `/specs/background/roles.md`.
8. Load `prompts/vspec_new/terms.md` and generate `/specs/background/terms.md`.
9. Load `prompts/vspec_new/flows.md` and generate `/specs/flows/*.puml`.
10. Load `prompts/vspec_new/scenarios.md` and generate `/specs/background/scenarios.md`.
11. Load `prompts/vspec_new/details_pre_post.md` and generate per-node `pre_post.md` under `/specs/background/scenario_details/`.
12. Load `prompts/vspec_new/details_constraints.md` and generate per-node `constraints.md` under `/specs/background/scenario_details/`.
13. Load `prompts/vspec_new/details_variations.md` and generate per-node `variations.md` under `/specs/background/scenario_details/`.
14. Load `prompts/vspec_new/details_boundaries.md` and generate per-node `boundaries.md` under `/specs/background/scenario_details/`.
15. Load `prompts/vspec_new/details_symmetry.md` and generate per-node `symmetry.md` under `/specs/background/scenario_details/`.
16. Load `prompts/vspec_new/dependencies.md` and generate `/specs/background/dependencies.md`.
17. Load `prompts/vspec_new/functions.md` and generate `/specs/functions/`.
18. Load `prompts/vspec_new/questions.md` and generate `/specs/background/questions.md`.
19. Follow the generated analysis steps to continue the project.

## Output Goal

- Clarify business objective and core user scenario.
- Identify key roles, page modules, and interaction flow.
- Extract entities and main data fields.
- Produce a visual-spec-oriented requirement draft for the next step.

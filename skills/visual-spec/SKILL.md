---
name: "visual-spec"
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

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- If the command argument or input explicitly provides `lang=<en|zh|ja>`, use that value for this run and update `selected.language` to it (update only that field). `zh-CN` should be treated as an alias of `zh`.
- When `selected.language=en`, all headings in `/specs/background/original.md` must be English; normalize any non-English headings to:
  `# Raw Requirement`, `# Summary`, `# Business Context`, `# Core Features`, `# Pages & Interactions`, `# Data Model`, `# Business Logic`, `# Risks & Assumptions`, `# Open Questions`.

Flow:
0. Ensure `/docs/` exists, and ensure subfolders exist:
   - `/docs/legacy/`
   - `/docs/current/`
   - `/docs/refine/`
   - `/docs/dependencies/`
   - Do NOT create `/docs/change/` (it is deprecated).
0.2 If the user passes `lang=<en|zh|ja>` in the command arguments, set `/scheme.yaml` `selected.language` to that value (update only that field, keep other fields and formatting unchanged). `zh-CN` should be treated as an alias of `zh`.
0.5 Create editable project constraints so the user can tweak them early (do not overwrite if they already exist):
   - Create `/scheme.yaml` with defaults (prototype stack selection + catalog) if missing
   - Create `/prototype_ui_convention.md` (same directory as `/scheme.yaml`) if missing
1. Ask the user to input the original requirement.
2. When the user presses Enter, treat the input as the raw requirement source.
3. Load the prompt file at `prompts/vspec_new/background.md`.
4. Use that prompt to analyze the requirement and expand the business context.
5. Write the raw requirement and background analysis output to `/specs/background/original.md`.
5.5 Create `/specs/background/question_and_answer.html` by copying `prompts/vspec_new/question_and_answer.html` (single-file HTML with inline CSS/JS) so the user can answer questions and write back to markdown.
6. Ask the user to answer the questions from the Open Questions section (use the section title in the selected language). The user should answer via `/specs/background/question_and_answer.html` (select `/specs/background/original.md` in the page and save back), then reply with a continuation signal (e.g. `继续` / `continue`). Then STOP. Do not load any subsequent prompts or generate any further artifacts before that.
7. After the user replies (answers or confirmed), load `prompts/vspec_new/stakeholders.md` to analyze stakeholders.
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
28. Write the questions result to `/specs/background/questions.md` (markdown list).
29. Load `prompts/harness/post_new_verify.md` to validate whether functions and scenario_details are complete (login/config/master-data/approval). If it outputs any issues, show the issue list and stop.
30. Return the structured analysis result and continue to the next requirement-design step.

### `/vspec:refine`

Use this command to refine and update the requirement based on refine materials stored under `/docs/refine/`, or based on one or more input files/directories provided as command arguments.

Flow:
0. Ensure `/specs/details/` exists and is non-empty; if missing, stop and ask the user to run `/vspec:detail` first.
1. Read refine inputs:
   - If command arguments are provided, treat them as refine input sources (files/directories).
   - Otherwise, read `/docs/refine/` (prefer `/docs/refine/file_list.md` as the entry if present; else read files in name order).
2. If `prompts/vspec_refine/refine.md` is missing, stop immediately and do nothing.
3. Load `prompts/vspec_refine/refine.md` to apply the refinement, update the canonical requirement, and update impacted artifacts.
4. Append the refinement result to `/specs/background/original.md`, and update impacted `/specs/details/` and `/specs/prototypes/` accordingly.

### `/vspec:refine-q`

Use this command to refine and update the requirement based on answered questions.

Flow:
1. If `/specs/background/questions.md` is missing, stop immediately and do nothing.
2. If `/specs/background/questions.md` contains no pending/unanswered questions, stop immediately and do nothing.
3. Read `/specs/background/questions.md` and pick answered items.
4. Load `prompts/vspec_refine/refine_q.md` to merge answers into the canonical requirement.
5. Append the refinement result to `/specs/background/original.md`.
6. Update `/specs/background/questions.md` to mark items that are treated as answered in this run:
   - Wrap the answer and status values with `<mark>...</mark>` (use the field names in the selected language) so answered items are visually highlighted.

### `/vspec:more-q`

Use this command to generate more clarification questions and append them to `/specs/background/questions.md`.

Flow:
1. If `/specs/background/questions.md` is missing, stop and ask the user to run `/vspec:new` first.
2. Load `prompts/vspec_more_q/more_q.md` to generate additional questions (avoid duplicates and continue numbering).
3. Append the new items to `/specs/background/questions.md` (do not rewrite existing items).
4. Provide a clear instruction for the user to answer the questions and then run `/vspec:refine-q`.

### `/vspec:detail`

Use this command to expand requirement details based on the function list.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- All generated spec documents under `/specs/` must use the selected language consistently (headings, tables, field descriptions, statuses, button names, messages).

Flow:
1. Read the feature/function list from `/specs/functions/*`.
   - You must iterate every function row across all files under `/specs/functions/` (not just core.md), so no module or external-system function is missed.
2. Read supporting artifacts when available: `/specs/background/*`, `/specs/flows/*.puml`, `/specs/background/scenario_details/`, `/specs/background/roles.md`, and existing `/specs/models/*.md` (if any).
3. For each function (page or non-page job), first determine which detail artifacts are actually involved, then only generate those artifacts; do not generate documents for non-involved parts.
   - Coverage requirement: for every function row you iterate, you must generate at least `rbac.md` and `data_permission.md`. If you cannot, output an explicit error and stop (do not silently skip).
   - Step type requirement: you must determine the step type from the function row (e.g. terminal type / page vs backend vs job), and generate the corresponding logic artifacts; do not skip logic:
     - For `Web` / `Mobile` / `Web+Mobile` steps: always generate `page_load.md` and `interaction.md`.
     - For `Backend` steps: always generate `service_logic.md` (service logic: inputs/outputs, rules, states, APIs/events, errors, idempotency).
     - For `Job` steps: always generate `job_logic.md` (job logic: trigger/schedule, data scope, retries/compensation, observability, failure handling).
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
    - `payment.md`: payment and refund details (if there is any payment/refund/settlement/reconciliation logic).
    - `auth.md`: account/login details (if there is any non-SSO login/account/password flow).
    - `judgemental_matrix.md`: judgemental matrix (判定矩阵) for multi-factor logic branching (if 2+ factors jointly decide outcomes).
   - Module-level (generate at most once per module, and only if involved):
     - `timeline.md`: time-axis visualization (HTML) for overall flow impact analysis (only when there is long time-span logic that affects flow decisions, e.g. effective/expiry, deadlines, grace periods, cross-day rules).
      - `state_machine.md`: status list + transitions + PlantUML state diagram (overall; not per function).
     - `nfp.md`: non-functional requirements summary for the module (overall; not per function).
     - `cron_job.md`: scheduled jobs summary for the module (overall; not per function).
4. Write only the generated (involved) detail documents:
   - Per-function: `/specs/details/<module_slug>/<logic_type>/<function_slug>.(md|html)`
   - Module-level: `/specs/details/<module_slug>/<logic_type>/<module_slug>.(md|html)`
5. Load `prompts/vspec_detail/index.md` to generate a single-page viewer `/specs/details/index.html`:
   - Left: directory tree based on `/specs/details/`
   - Right: markdown-rendered reading pane
   - Render PlantUML diagrams (do not show raw PlantUML text)

### `/vspec:doc`

Use this command to generate a Word document (Word-openable single-file `.doc` in HTML format) that aggregates the requirement detail artifacts into a deliverable doc, and write it under `/docs/current/`.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- The generated Word document must use the selected language consistently (titles, headings, field labels, table headers).

Flow:
1. Ensure `/docs/current/` exists.
2. Read the existing artifacts when available:
   - Canonical requirement: `/specs/background/original.md`
   - Function list: `/specs/functions/*`
   - Detail specs: `/specs/details/**`
   - Roles & permissions: `/specs/background/roles.md`, `/specs/details/**/rbac.md`
   - Data permission: `/specs/details/**/data_permission.md`
   - Scenarios & flows: `/specs/background/scenarios.md`, `/specs/background/scenario_details/**`, `/specs/flows/*.puml`
   - Dependencies: `/specs/background/dependencies.md`
   - Models: `/specs/models/*.md`
3. Load `prompts/vspec_doc/doc.md` and generate the doc as a Word-openable single HTML file.
4. Write the output file to: `/docs/current/requirement_detail.doc`.

### `/vspec:verify`

Use this command to generate models and a runnable prototype for validation.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- Generate `/specs/models/` docs and all prototype UI copy in the selected language consistently.

Flow:
0. Ensure `/specs/details/` exists and is non-empty; if missing, stop and output the prerequisite message: “Run /vspec:detail to generate /specs/details/ before /vspec:verify”.
1. If `/specs/background/questions.md` exists and contains unanswered questions, ask the user to answer them before continuing (allow skip per question, but ensure none remains unanswered).
2. Load `prompts/vspec_verify/model.md` to generate data models.
3. Write model files to `/specs/models/*.md`.
4. Generate a runnable page prototype based on functions, details, models, and roles; the prototype tech stack can be selected via `/scheme.yaml` (auto-created with defaults if missing).
   - Load `prompts/vspec_verify/prototype.md` for the prototype generation rules (must follow `scheme.yaml` stack; do not output html-only).
5. Write the prototype to `/specs/prototypes/`.
6. Load `prompts/harness/post_verify_stack_verify.md` to validate whether the prototype frontend stack matches `/scheme.yaml`. If it outputs any issues, show the issue list and stop.
7. Load `prompts/vspec_verify/validation.md` to generate a scenario validation web page.
8. Write the validation page to `/specs/prototypes/` and provide a `scenario.html` entry for access.
9. Load `prompts/vspec_verify/entries.md` to generate an entry page and write it to `/specs/prototypes/entries.html` (do not link it from any menu/header).
10. Load `prompts/harness/post_verify_mobile_selection_check.md` to ensure mobile data selection uses a picker page (list-based), not dropdown Select. If it outputs any issues, show the issue list and stop.
11. Load `prompts/harness/post_verify_price_format_check.md` to validate money/price formatting (right aligned, 2 decimals, thousand separators). If it outputs any issues, show the issue list and stop.
12. Load `prompts/harness/post_verify_click_check.md` to detect clickable UI elements that do nothing. If it outputs any issues, show the issue list and stop.
13. Load `prompts/harness/post_verify_verify.md` to validate the prototype completeness. If it outputs any issues, show the issue list and stop.

### `/vspec:qc`

Use this command to run a quality check on the generated requirement artifacts under `/specs/`.

Note: The Pro edition supports broader quality checks (e.g. more post-run prototype/implementation verifications) and requires a paid plan.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- The QC report `/specs/qc_report.md` must use the selected language consistently.

Flow:
1. Read built-in standard at `prompts/vspec_qc/quality_standard.md`.
2. If a requirement quality error book exists under project `qc/`, generate/update project root `quality_standard.md` based on it.
3. If project root `quality_standard.md` exists, merge it as supplementary/overriding standard.
4. Load `prompts/vspec_qc/qc.md` and generate a non-conformance checklist.
5. Write the report to `/specs/qc_report.md`.

### `/vspec:accept`

Use this command to generate acceptance test cases.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- All acceptance documents under `/specs/acceptance/` must use the selected language consistently.

Flow:
1. Read `/specs/functions/*`, `/specs/background/scenarios.md`, `/specs/background/scenario_details/`, `/specs/background/roles.md`, `/specs/models/*.md`.
2. Load `prompts/vspec_accept/accept.md` to generate acceptance test cases covering core flows, exceptions, boundary, permissions, and data scope.
3. Write results to `/specs/acceptance/` (one subfolder per function) and generate an index at `/specs/acceptance/index.md`.

### `/vspec:append-test`

Use this command to generate automation test code based on acceptance cases and specs.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- Test case titles/descriptions should follow the selected language as much as possible.

Flow:
1. Read `/specs/acceptance/`, `/specs/functions/*`, `/specs/details/`, and detect the existing test frameworks in the repository.
2. Load `prompts/vspec_test/test.md` to generate automation tests using the existing frameworks and conventions.
3. Write test code to the project test directories (or `/tests/` if no standard exists) and ensure it can run with existing scripts.
4. Load `prompts/harness/post_append_test_coverage_check.md` to verify whether test coverage is sufficiently complete; if it outputs any issues, continue.
5. If issues exist, rerun `/vspec:append-test` once focusing only on the missing items from the issue list, then rerun the coverage check.
6. If issues still exist after the second coverage check, show the issue list and stop.
7. This command generates/adds tests to improve coverage; it does not execute test commands.

### `/vspec:impl`

Use this command to generate integrated frontend/backend code based on the specs.

Flow:
1. Read `/specs/functions/*`, `/specs/details/`, `/specs/models/*.md`, `/specs/background/dependencies.md`, and detect the current frontend/backend stacks and code conventions.
2. Load `prompts/vspec_impl/implement.md` and implement backend-first: generate a runnable backend project under `/specs/backend/` (health check + core APIs/services), then generate frontend integration after backend APIs are available.
3. Write code only under `/specs/` with minimal diffs and keep it reviewable; backend must be under `/specs/backend/` and prototype frontend under `/specs/prototypes/`.
4. Load `prompts/harness/post_impl_verify.md` to validate backend MVC structure and test coverage. If it outputs any issues, show the issue list and stop.

### `/vspec:upgrade`

Use this command to upgrade/retrofit requirements based on materials stored under `/docs/` (`/docs/legacy` for legacy system, `/docs/current` for new inputs), and regenerate the `/specs/` artifacts in the same structure as `/vspec:new`.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- All regenerated `/specs/**` artifacts must use the selected language consistently.

Flow:
1. Ensure the input entry file exists at `/docs/current/file_list.md`; if missing, generate it with the expected input list template.
2. Read `/docs/current/file_list.md`, then read the listed sources under `/docs/` (typically `/docs/legacy/*`, `/docs/current/*`, optionally `/docs/templates/*`, `/docs/texts/*`, `/docs/assets/*`) in order and extract structured information (functions, dependencies, UI style, roles/permissions, technical spec). Additionally, you must recursively scan `/docs/legacy/` and all its subdirectories and treat those documents as raw input materials (even if they are not explicitly listed yet); when you find legacy files not in `file_list.md`, append them into `/docs/current/file_list.md` and then read them.
3. If `/specs/background/original.md` exists, treat it as the current canonical requirement and use it as baseline for diff (inherit/new/change/deprecate).
4. Load `prompts/vspec_upgrade/upgrade.md` and generate/update artifacts under `/specs/`, reusing `/vspec:new` output conventions.
5. Sync extracted technical spec into `/scheme.yaml` so it can be used by `/vspec:verify` and `/vspec:impl`.

### `/vspec:plan`

Use this command to break down requirements, estimate efforts, and schedule via a user story map.

Language:
- Read `/scheme.yaml` `selected.language` (supports `en`, `zh`, `ja`; default to `en` if missing/invalid).
- Both `/specs/plan/plan_estimate.md` and `/specs/plan/plan_schedule.html` must use the selected language consistently.

Flow:
1. Read `/specs/functions/*`, `/specs/background/roles.md`, `/specs/background/scenarios.md`, `/specs/details/`, `/specs/background/dependencies.md`.
2. Load `prompts/vspec_plan/estimate.md` to generate estimates aligned to the function list.
3. Write estimates to `/specs/plan/plan_estimate.md`.
4. Load `prompts/vspec_plan/schedule.md` to generate the schedule and delivery map.
5. Write schedule HTML to `/specs/plan/plan_schedule.html`.

### `/vspec:mrd`

Use this command to generate a market research and product positioning pack (MRD): market landscape, competitor analysis, user positioning, and product design notes.

Flow:
1. Ensure `/docs/market/` exists.
2. Read baseline artifacts when available: `/specs/background/original.md`, `/specs/background/roles.md`, `/specs/background/terms.md`, `/specs/background/scenarios.md`, `/specs/flows/*.puml`, `/specs/background/dependencies.md`, and `/specs/functions/*` (if any).
3. Load `prompts/vspec_mrd/mrd.md`.
4. Write outputs to:
   - `/docs/market/market.md`
   - `/docs/market/competitors.md`
   - `/docs/market/users.md`
   - `/docs/market/product_design.md`

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
- `prompts/vspec_more_q/more_q.md`: the prompt used by `/vspec:more-q` to append more questions to `/specs/background/questions.md`.
- `prompts/vspec_mrd/mrd.md`: the prompt used by `/vspec:mrd` to generate market/user/competitor/product docs under `/docs/market/`.
- `prompts/vspec_refine/refine.md`: the prompt used by `/vspec:refine` to refine the requirement based on `refine.md`.
- `prompts/vspec_refine/refine_q.md`: the prompt used by `/vspec:refine-q` to refine the requirement based on answered questions.
- `prompts/vspec_doc/doc.md`: the prompt used by `/vspec:doc` to generate a Word-openable `.doc` (HTML) requirement detail document under `/docs/current/`.
- `prompts/vspec_verify/model.md`: the prompt used by `/vspec:verify` to generate `/specs/models/*.md`.
- `prompts/vspec_verify/prototype.md`: the prompt used by `/vspec:verify` to generate the stack-selected runnable prototype under `/specs/prototypes/` (must follow `scheme.yaml`).
- `prompts/vspec_verify/validation.md`: the prompt used by `/vspec:verify` to generate the validation web page with a `scenario.html` entry.
- `prompts/vspec_detail/rbac.md`: the prompt used by `/vspec:detail` to generate RBAC detail docs.
- `prompts/vspec_detail/data_permission.md`: the prompt used by `/vspec:detail` to generate data permission detail docs.
- `prompts/vspec_detail/page_load.md`: the prompt used by `/vspec:detail` to generate page loading logic docs.
- `prompts/vspec_detail/interaction.md`: the prompt used by `/vspec:detail` to generate page interaction logic docs.
- `prompts/vspec_detail/index.md`: the prompt used by `/vspec:detail` to generate `/specs/details/index.html` as a markdown/PlantUML-rendered viewer.
- `prompts/vspec_detail/index.html`: the fixed HTML template used by `/vspec:detail` to stabilize `/specs/details/index.html` generation (directory tree + markdown renderer).
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
- `prompts/vspec_detail/service_logic.md`: the prompt used by `/vspec:detail` to generate backend service logic docs for `Backend` steps.
- `prompts/vspec_detail/job_logic.md`: the prompt used by `/vspec:detail` to generate job logic docs for `Job` steps.
- `prompts/vspec_detail/logging_matrix.md`: the prompt used by `/vspec:detail` to generate logging matrix docs.
- `prompts/vspec_detail/notification_matrix.md`: the prompt used by `/vspec:detail` to generate notification matrix docs.
- `prompts/vspec_detail/nfp.md`: the prompt used by `/vspec:detail` to generate non-functional requirements docs.
- `prompts/vspec_detail/file_import.md`: the prompt used by `/vspec:detail` to generate file import docs.
- `prompts/vspec_detail/file_export.md`: the prompt used by `/vspec:detail` to generate file export docs.
- `prompts/vspec_detail/cron_job.md`: the prompt used by `/vspec:detail` to generate scheduled job docs.
- `prompts/vspec_accept/accept.md`: the prompt used by `/vspec:accept` to generate acceptance test cases.
- `prompts/vspec_test/test.md`: the prompt used by `/vspec:append-test` to generate automation test code.
- `prompts/vspec_impl/implement.md`: the prompt used by `/vspec:impl` to generate integrated frontend/backend code.
- `prompts/vspec_upgrade/upgrade.md`: the prompt used by `/vspec:upgrade` to generate upgraded specs from `/docs/` inputs.
- `prompts/vspec_plan/estimate.md`: the prompt used by `/vspec:plan` to generate `/specs/plan/plan_estimate.md`.
- `prompts/vspec_plan/schedule.md`: the prompt used by `/vspec:plan` to generate `/specs/plan/plan_schedule.html`.
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

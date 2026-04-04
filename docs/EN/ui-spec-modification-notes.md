## Background

As the prototype grows (Web + Mobile), the number and types of pages will keep increasing. Without a unified UI convention, it is very easy to get:

- Inconsistent layouts across similar pages (tables/forms/details)
- Inconsistent status colors and status wording
- Fragmented visual language between Mobile and Web
- Inconsistent interaction patterns (create flows, in-page forms, drawer/modal usage)

To prevent this, the prototype generation is constrained by an editable UI convention file: `/prototype_ui_convention.md`.

## What Changed

- Add a project-level constraint file: `/prototype_ui_convention.md` (same directory as `/scheme.yaml`)
- When `/vspec:verify` generates/updates prototypes:
  - If `/prototype_ui_convention.md` does not exist: generate a default template first (do not overwrite existing files)
  - Prototype UI generation must follow `/prototype_ui_convention.md`
  - If stricter existing rules exist (for example `/docs/current/ui_spec.md` or `/docs/current/ui_style.md`), merge the stricter rules into `/prototype_ui_convention.md` and treat the merged file as the final source of truth

## How to Modify the UI Convention

- Edit `/prototype_ui_convention.md` at the target project root
- Prefer updating conventions rather than writing implementation details:
  - Color/status mappings
  - Common structure for tables/forms/details
  - Drawer/Modal usage rules
  - Typography and spacing (Web/Mobile)
  - Copy and feedback patterns (success/failure/permission/empty/error states)
- Re-run `/vspec:verify` after changes so newly generated/updated pages align with the updated convention

## Not Recommended

- Do not make the convention a set of page-specific exceptions (it breaks overall consistency)
- Do not introduce a new UI component library unless the project’s selected stack requires it
- Do not hardcode lots of page-level colors/sizes in the convention; prefer a small set of global tokens and structural rules

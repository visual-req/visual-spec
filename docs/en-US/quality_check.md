## Requirement Quality Check (Standalone Use)

[English](../en-US/quality_check.md) | [中文](../zh-CN/quality_check.md) | [日本語](../ja-JP/quality_check.md)

This page explains how to run a requirements quality scan without relying on [/vspec:qc](../../README.md#commands). You can use the built-in quality standard file to scan any requirement document format (Word/Markdown/document repositories) and produce a issues table.

If you only want the standalone quality check capability (without the full visual-spec workflow), you can also use: https://github.com/visual-req/spec-review

For the design rationale, quality dimensions, and the fix loop behind QC, see: [theory/quality_check.md](theory/quality_check.md)

### Prepare

- Quality standard file (use whichever path exists in your environment):
  - Skill root: `/prompts/vspec_qc/quality_standard.md`
  - Repo source: `skills/visual-spec/prompts/vspec_qc/quality_standard.md`
- Your requirement document (PRD/spec/etc.), in Word/PDF/Markdown, etc.

### How to use (DeepSeek chat as an example)

1. Upload two files:
   - `quality_standard.md` (the standard)
   - your requirement document (Word/PDF/Markdown, etc.)
2. Ask:

   Please check the requirement document against the quality standard and generate a table of findings.

3. If you want a structured table, specify columns such as:
   - ID
   - category/title
   - pass/fail/partial
   - issue summary
   - location (section/paragraph/page)
   - fix suggestion

### Tips

- For commonly missed areas (limits, time semantics, formula precision, permissions/data permissions, dependency failure strategies), explicitly ask to focus on boundaries/exceptions/idempotency/rollback/audit/reconciliation.
- If you see recurring domain issues, extract them into `domain_quality_standard.md` at your project root, as a domain extension standard that [/vspec:qc](../../README.md#commands) can merge and apply.

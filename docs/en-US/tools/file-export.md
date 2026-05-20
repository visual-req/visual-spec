## File Export

Used to define the data flow of "system outputting as a file": export scope, permissions, format, performance, and auditing.

Applicable Scenarios:
- Report export, reconciliation export, bulk data delivery to third parties
- Data retention and archiving, audit evidence collection

Suggested Information to Include:
- Export Scope: filter conditions, field set, sorting rules
- Permissions and Desensitization: which roles can export, handling of sensitive fields
- File Format: CSV/XLSX/JSON, encoding, date/amount formats
- Performance: pagination/async tasks, download link validity, concurrency limits
- Audit: exporter, export time, conditions, file checksum

Implementation Suggestions:
- Unify export task state machine and error receipts
- Clarify strategies for large data volumes (sharding, compression, volume splitting, resumable downloads)
## File Import

Used to define the data flow of "external files as input": format, validation, parsing, database persistence, receipts, and error handling.

Applicable Scenarios:
- Bulk creation/update (customers, products, quotas, whitelists)
- Bank statement import, historical data migration

Suggested Information to Include:
- File Format: CSV/XLSX/JSON, encoding, delimiters, headers
- Field Mapping: column name → target field, required/optional, default values
- Validation Rules: types, ranges, uniqueness, cross-row/cross-table validations
- Processing Strategy: all-or-nothing / partial success, error row feedback
- Idempotency and Deduplication: import batch number, duplicate row handling

File and Security Requirements (Anti-duplication / Anti-overwrite / Anti-virus / Naming Rules):
- Anti-overwrite: uploaded files must be written to an "append-only" object storage path, prohibiting direct overwriting with original filenames; business data persistence must be "create new import batch record → insert by batch", prohibiting direct overwriting of historical batch files.
- Anti-duplication (File level): calculate file hash (e.g., SHA-256), use `(tenant_id, uploader_id, file_hash)` as idempotency key; return "existing import batch number" on hit, do not persist repeatedly.
- Anti-duplication (Content level): must define "business idempotency key" (e.g., `external_id` / `code` / `(org_id, code)`); duplicate rows in the same file must be identifiable with error row feedback; cross-batch duplicates must follow strategies: skip / overwrite / error (must be explicit).
- Anti-virus: enter quarantine after upload, parse and persist only after virus scan/type sniffing completes; scan failure/timeout must be rejected and audited.
- File Type Whitelist: only explicitly listed extensions and MIME types (e.g., `.csv/.xlsx/.json`), perform file header sniffing, prohibit "disguised extensions".
- Size and Row Limits: specify max size (MB), max rows, max columns; excess must be rejected and prompted.
- Encoding and Formatting: for CSV specify encoding (UTF-8 preferred), delimiters, quote escapes, newline rules; for XLSX specify sheet name (or first sheet) and header row position.
- File Naming Rules (Recommended): `<system>_<object>_<yyyymmdd>_<batch>.<ext>`; only for display and retrieval, not for idempotency; backend final storage name should include batch number (to avoid conflicts).

File Content and Data Mapping (must be explicit to column/field level):

Mapping Table (Example):
| Source Column (Header) | Example Value | Target Field (DB/API) | Type | Required | Default | Conversion Rule | Validation Rule | Notes |
|---|---|---|---|---|---|---|---|---|
| customer_code | C001 | customer.code | string | Y | - | trim+upper | Unique; length<=32 | Business idempotency key |
| customer_name | Alice | customer.name | string | Y | - | trim | length<=128 | - |
| phone | 13800000000 | customer.phone | string | N | - | normalize_e164 | Valid format | - |
| level | VIP | customer.level | enum | N | Normal | map: VIP->VIP | Enum validation | - |

Parsing and Persistence Guidelines (Recommended to clarify):
- Header Positioning: allow header aliases? allow missing columns? fixed column order?
- Data Types: determination of empty values/empty strings/NULL; dates and time zones; decimal precision and rounding rules.
- Error Feedback: error rows must contain "row number + original value + error code + error message + target field", and provide download (CSV/JSON).
- Partial Success Strategy: clarify "successful rows persist + failed rows feedback" vs "batch rollback"; if partial success is supported, idempotency keys must guarantee no duplicate persistence upon re-upload.
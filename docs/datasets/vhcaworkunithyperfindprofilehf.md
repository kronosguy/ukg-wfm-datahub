# vHcaWorkUnitHyperfindProfileHF

**Group:** Detail Dataset → Healthcare Productivity

A set of rows with the work unit hyperfinds associated with each work unit hyperfind profile.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaWorkUnitHyperfindProfileHF |
| Unique Identifier | workUnitHyperfindProfileId |
| Source Pipeline | hcaWorkUnitHyperfindProfile (DR) |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workUnitHyperfindProfileId | INT64 | The ID of the work unit hyperfind profile |  |  |
| workUnitHyperfindId | INT64 | Work unit hyperfind ID |  |  |
| workUnitHyperfindName | STRING | Work unit hyperfind name |  |  |
| workUnitHyperfindIsActive | BOOLEAN | Is work unit hyperfind active |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

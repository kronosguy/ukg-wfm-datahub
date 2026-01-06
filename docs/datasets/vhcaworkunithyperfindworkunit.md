# vHcaWorkUnitHyperfindWorkUnit

**Group:** Detail Dataset → Healthcare Productivity

A set of rows with the work units associated with each work unit hyperfind.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaWorkUnitHyperfindWorkUnit |
| Unique Identifier | workUnitHyperfindId |
| Source Pipeline | hcaWorkUnitHyperfind (DR) |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workUnitHyperfindId | INT64 | The ID of the work unit hyperfind |  |  |
| workUnitId | INT64 | The ID of the work unit |  |  |
| workUnitName | STRING | Work Unit Name |  |  |
| workUnitIsActive | BOOLEAN | Is work unit active |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

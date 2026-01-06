# vHcaWorkUnitLocation

**Group:** Detail Dataset → Healthcare Productivity

One row for each location (orgId) assigned to a work unit.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vHcaWorkUnitLocation |
| Unique Identifier | workUnitId |
| Source Pipeline | hcaWorkUnits (CDC) |

## Columns

**Column count:** 3

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workUnitId | INT64 | The ID of the work unit |  |  |
| orgId | INT64 | The ID of the location from the businessStructure view. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

# vCostCenter

**Group:** Detail Dataset → Timekeeping Setup

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vCostCenter |
| Unique Identifier | costCenterId |
| Source Pipeline | getCostCenter (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| costCenterId | INT64 | The ID of a cost center. |  |  |
| costCenterName | STRING | The name of a cost center. |  |  |
| costCenterDesc | STRING | The description of a cost center. |  |  |
| inactive | BOOLEAN | A Boolean indicator of whether or not a cost center is inactive. |  |  |
| version | INT64 | The current version of the entity. This is used to ensure that an entity is not updated with stale data. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

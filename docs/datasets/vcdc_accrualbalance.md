# vCdc_accrualBalance

**Group:** Detail Dataset → Change Data Capture Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vCdc_accrualBalance |
| Unique Identifier |  |
| Source Pipeline | accrualBalance (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | personId for which the change occured |  |  |
| srcPartitionDate | DATE | The date for which a record transaction was made |  |  |
| runtype | STRING | Indicates whether the change was due to Incremental or Historical Reload. |  |  |
| updateDtm | DATETIME | The date and time an update to a record was loaded in Data Hub Views. |  |  |

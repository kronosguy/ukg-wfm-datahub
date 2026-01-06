# vAccrualCodes

**Group:** Detail Dataset → Accrual Detail Views

Contains a list of accrual code types

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAccrualCodes |
| Unique Identifier | accrualCodeId |
| Source Pipeline | getAccrualCodes (DR) |

## Columns

**Column count:** 8

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| accrualCodeId | INT64 | The ID of an accrual code. |  |  |
| accrualCode | STRING | The name of an accrual code. |  |  |
| shortName | STRING | The short name of an accrual code. |  |  |
| typeId | INT64 | The ID of an accrual code type. |  |  |
| typeName | STRING | The name of an accrual code type. |  |  |
| hoursPerDayInSeconds | INT64 | The hours per day (in seconds) associated with an accrual code. |  |  |
| allowEditSwt | BOOLEAN | A Boolean indicator of whether or not an accrual code is ediview. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

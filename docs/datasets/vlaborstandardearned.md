# vLaborStandardEarned

**Group:** Detail Dataset → Forecasting Detail Views

Labor Standards Earned Data

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborStandardEarned |
| Unique Identifier | partitionDate,orgId,laborStandardId |
| Source Pipeline | laborStandardEarned (CDC) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| laborStandardId | INT64 | The ID of an effective labor standard version. |  |  |
| laborStandardName | STRING | The name of an effective labor standard version. |  |  |
| taskGroupId | INT64 | The ID of a labor task group. |  |  |
| taskGroupName | STRING | The name of a labor task group. |  |  |
| taskId | INT64 | The ID of a labor task. |  |  |
| taskName | STRING | The name of a labor task |  |  |
| totalLaborMinutes | FLOAT | Total labor minutes |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |  |  |

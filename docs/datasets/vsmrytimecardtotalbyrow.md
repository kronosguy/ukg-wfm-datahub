# vSmryTimecardTotalByRow

**Group:** Detail Dataset → Data Detail Validation

Timecard Total hours and amounts by date, personId and pay code (IA vs Data Hub Summary)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vSmryTimecardTotalByRow |
| Unique Identifier | All fields |
| Source Pipeline | valTimecardTotal (DR) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| valPersonid | INT64 | valScheduledTotal personId |  |  |
| smryPersonid | INT64 | vScheduleTotal personId |  |  |
| valPaycodeid | INT64 | valScheduledTotal pay code Id |  |  |
| smryPaycodeid | INT64 | vScheduleTotal pay code Id |  |  |
| valOrgjobId | INT64 | valScheduledTotal orgId |  |  |
| smryOrgjobId | INT64 | vScheduleTotal orgId |  |  |
| valHours | FLOAT | Totalized Hours valScheduledTotal |  |  |
| smryHours | FLOAT | Totalized Hours vScheduleTotal |  |  |
| valWages | FLOAT | Totalized Wages valScheduledTotal |  |  |
| smryWages | FLOAT | Totalized Wages vScheduleTotal |  |  |

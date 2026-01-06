# vDtlTimecardTotalByRow

**Group:** Detail Dataset → Data Detail Validation

Timecard total detail data from IA validation data and Data Hub by person, pay code and date with amounts and variances

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDtlTimecardTotalByRow |
| Unique Identifier | All fields |
| Source Pipeline | valTimecardTotal (DR) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| valPersonid | INT64 | valScheduledTotal personId |  |  |
| dtlPersonid | INT64 | vScheduleTotal personId |  |  |
| valPaycodeid | INT64 | valScheduledTotal pay code Id |  |  |
| dtlPaycodeid | INT64 | vScheduleTotal pay code Id |  |  |
| valOrgjobId | INT64 | valScheduledTotal orgId |  |  |
| dtlOrgjobId | INT64 | vScheduleTotal orgId |  |  |
| valHours | FLOAT | Totalized Hours valScheduledTotal |  |  |
| dtlHours | FLOAT | Totalized Hours vScheduleTotal |  |  |
| valWages | FLOAT | Totalized Wages valScheduledTotal |  |  |
| dtlWages | FLOAT | Totalized Wages vScheduleTotal |  |  |

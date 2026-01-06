# vTimecardWorkShiftScheduledShift

**Group:** Detail Dataset → Timecard Detail Views

- Association between the timecard and scheduler entries.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardWorkShiftScheduledShift |
| Unique Identifier | workedShiftId,shiftId |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workedShiftId | INT64 | Worked Shift ID |  |  |
| partitionDate | DATE | Represents Date Part of startDateTime for the transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| shiftId | INT64 | Shift ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

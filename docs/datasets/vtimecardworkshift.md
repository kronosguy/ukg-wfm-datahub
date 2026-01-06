# vTimecardWorkShift

**Group:** Detail Dataset → Timecard Detail Views

- Worked Shifts data. Includes rounded start and end times.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardWorkShift |
| Unique Identifier | workedShiftId,partitionDate,personId,shiftTotalHours |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 28

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| workedShiftId | INT64 | Worked shift ID |  |  |
| partitionDate | DATE | Represents Date Part of startDateTime for the transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| startDateTime | DATETIME | The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| roundedStartDateTime | DATETIME | An optional field containing the start date and time based on configured rounding rules. |  |  |
| unscheduledStartDateTime | DATETIME | A string parameter that represents the start date and time for an unscheduled shift. |  |  |
| startTimezone | INT64 | Start timezone where the worked shift was entered. Normally, this is the default or home timezone for the employee, but the worked shift can include a different timezone as necessary. |  |  |
| startTimezoneId | INT64 | Start time zone ID |  |  |
| roundedStartTimezone | STRING | An optional field containing the start timezone based on configured rounding rules. |  |  |
| roundedStartTimezoneId | INT64 | Rounded start time zone ID |  |  |
| endDateTime | DATETIME | An optional field containing the end date and time based on configured rounding rules. |  |  |
| roundedEndDateTime | DATETIME | The rounded punch date and time. |  |  |
| unscheduledEndDateTime | DATETIME | A string parameter that represents the end date and time for an unscheduled shift. |  |  |
| endTimezone | INT64 | The end timezone where the worked shift was entered. Normally, this is the default or home timezone for the employee, but the worked shift can include a different timezone as necessary. |  |  |
| endTimezoneId | INT64 | End time zone ID |  |  |
| roundedEndTimezone | STRING | An optional field containing the end timezone based on configured rounding rules. |  |  |
| roundedEndTimezoneId | INT64 | Rounded end time zone ID |  |  |
| fromScheduleSwt | BOOLEAN | A Boolean indicator of whether or not shift is from schedule |  |  |
| inProgressSwt | BOOLEAN | A Boolean indicator of whether or not a returned worked shift is currently in progress. in-punch without a corresponding out-punch when the shift is part of a schedule. |  |  |
| projectedSwt | BOOLEAN | A Boolean indicator of whether or not a shift is projected |  |  |
| dataSource | STRING | A reference to the data source, if one exists. Normally, this indicates that the context object came from a different source, such as a clock, device, or an external data source such as an import or interface. |  |  |
| dataSourceId | INT64 | Data source ID |  |  |
| unscheduledWorkRule | STRING | A string parameter that represents the work rule for an unscheduled shift. |  |  |
| unscheduledWorkRuleId | INT64 | Unscheduled work rule ID |  |  |
| transactionDateTime | DATETIME | The date and time stamp for when this worked shift transaction was entered through the API. |  |  |
| shiftTotalHours | FLOAT | Total number of hours for a worked shift. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| assignmentId | INT64 |  |  |  |

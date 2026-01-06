# vScheduleDayList

**Group:** Detail Dataset → Schedule Detail Views

- Lists the person/dates where there is a scheduled shift,paycode or holiday. (TRUE/FALSE) The set of schedule day lists associated with the manager's view of employee schedules.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleDayList |
| Unique Identifier | partitionDate,personId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| hasShiftSwt | BOOLEAN | The Boolean flag that indicates day lock has a shift attached |  |  |
| hasPayCodeEditSwt | BOOLEAN | The Boolean flag that indicates day lock has pay code edit |  |  |
| hasHolidaySwt | BOOLEAN | Boolean indicator where the schedule day is a holiday |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

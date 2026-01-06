# vTimecardException

**Group:** Detail Dataset → Timecard Detail Views

- All outstanding exceptions as seen on the timecard.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardException |
| Unique Identifier | exceptionId |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 35

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| exceptionId | INT64 | The exception category ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| reviewedSwt | BOOLEAN | A Boolean indicator of whether or not the exception was reviewed |  |  |
| startTimeZoneId | INT64 | The start timezone ID where the exception was entered. |  |  |
| startExceptionSwt | BOOLEAN | A Boolean indicator of whether or not this is an in punch exception |  |  |
| startDateTime | DATETIME | The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss) |  |  |
| endTimeZoneId | INT64 | The end timezone ID where the exception was entered. |  |  |
| endExceptionSwt | BOOLEAN | A Boolean indicator of whether or not this is an out punch exception |  |  |
| endDateTime | DATETIME | The end date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |  |  |
| transferSwt | BOOLEAN | A Boolean indicator of whether or not the exception involves a transfer |  |  |
| workRule | STRING | Work Rule Name |  |  |
| workRuleId | INT64 | Work Rule ID |  |  |
| eventDate | DATE | The date to which the event applies. |  |  |
| violationInHours | FLOAT64 | The total number of hours violated which caused an exception. |  |  |
| overLimitInHours | FLOAT64 | The amount (in hours) that exceeds the limit defined by the exception associated with the pay code edit. |  |  |
| exceptionCategory | STRING | The exception category name |  |  |
| exceptionTypeName | STRING | The exception type name |  |  |
| exceptionTypeDesc | STRING | The exception type descirption |  |  |
| exceptionType | STRING | The exception type name |  |  |
| exceptionTypeId | INT64 | The exception type ID |  |  |
| punchId | INT64 | Timecard Punch ID |  |  |
| payCodeEditId | INT64 | Pay code edit ID |  |  |
| hourWorkedId | INT64 | Hours Worked ID |  |  |
| holidayCreditId | INT64 | Holiday credit ID |  |  |
| workedShiftId | INT64 | Worked shift ID |  |  |
| workedShiftSpanId | INT64 | Worked shift span ID |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| isExcusedAbsenceSwt | BOOLEAN | A Boolean indicator of whether or not the exception involves an excused absence. |  |  |
| isUnExcusedAbsenceSwt | BOOLEAN | A Boolean indicator of whether or not the exception involves an unexcused absence. |  |  |
| schedulePayCodeId | INT64 | Unique identifier of a pay code. Joins to pay code dimension |  |  |
| schedulePunchDtm | DATETIME | Scheduled punch date time |  |  |
| shiftId | INT64 | Shift ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| assignmentId | INT64 |  |  |  |

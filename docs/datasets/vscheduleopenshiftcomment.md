# vScheduleOpenShiftComment

**Group:** Detail Dataset → Schedule Detail Views

- Comments attached to Open Shifts (Child of scheduleOpenShift)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleOpenShiftComment |
| Unique Identifier | uniqueId,noteId (nullable), noteTimeStamp (nullable) |
| Source Pipeline | scheduleOpenShift (CDC) |

## Columns

**Column count:** 14

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| openShiftId | INT64 | Schedule open shift ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | **  Note this value will always be null because openShift is not tied to person ** |  |  |
| commentNoteId | INT64 | Schedule open shift comment note ID |  |  |
| commentId | INT64 | Schedule open shift comment ID |  |  |
| comment | STRING | Schedule open shift comment |  |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not the shift is active |  |  |
| noteId | INT64 | Note ID |  |  |
| noteText | STRING | Note text | PII | BLANK |
| dataSourceDisplayName | STRING | Data source name |  |  |
| noteTimestamp | DATETIME | The date time stamp the note was entered |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| orgIds | INT64 (NESTED) | Nested list of orgIds |  |  |
| uniqueId | STRING | Unique Identifier |  |  |

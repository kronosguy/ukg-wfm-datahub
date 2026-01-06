# vTimecardExceptionComment

**Group:** Detail Dataset → Timecard Detail Views

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTimecardExceptionComment |
| Unique Identifier | exceptionId,commentId,commentNoteId,timestamp (nullable) |
| Source Pipeline | timecard (CDC) |

## Columns

**Column count:** 19

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| exceptionId | INT64 | Exception ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| commentNoteId | INT64 | The ID for the note. |  |  |
| timestamp | DATETIME | The data/time the comment was created or updated |  |  |
| notesText | STRING | The text entered in the note | PII | BLANK |
| dataSourceId | INT64 | The ID of the person who entered the note. |  |  |
| dataSourceDisplayName | STRING | The name of the person who entered the note. |  |  |
| comment | STRING | The name of the comment and attached notes. |  |  |
| commentId | INT64 | The ID for the comment and attached notes. |  |  |
| commentCategory | STRING | Comment category name |  |  |
| commentCategoryId | INT64 | Comment category ID |  |  |
| punchId | INT64 | Timecard Punch ID |  |  |
| payCodeEditId | INT64 | Pay code edit ID |  |  |
| hourWorkedId | INT64 | Hours worked ID |  |  |
| holidayCreditId | INT64 | Holiday credit ID |  |  |
| workedShiftId | INT64 | Worked Shift ID |  |  |
| workedShiftSpanId | INT64 | Worked Shift Span ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

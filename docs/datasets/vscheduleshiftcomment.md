# vScheduleShiftComment

**Group:** Detail Dataset → Schedule Detail Views

- Comments attached to Scheduled Shifts (Child of scheduleShift)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleShiftComment |
| Unique Identifier | shiftId, commentsNoteId, commentId, noteId (nullable), noteText (nullable) |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| shiftId | INT64 | Shift ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| commentsNoteId | INT64 | The ID for the comment and attached notes. |  |  |
| commentId | INT64 | The ID for the comment |  |  |
| comment | STRING | The name of the comment and attached notes. |  |  |
| activeSwt | BOOLEAN | Whether the comment is active or not. |  |  |
| noteId | INT64 | The ID for the note |  |  |
| notesText | STRING | The text of the note. | PII | BLANK |
| dataSourceDisplayName | STRING | The name of the person who entered the note. |  |  |
| notesTimestamp | DATETIME | The date and time when the note was created or modified; in ISO_LOCAL_DATE format (YYYY-MM-DD). |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

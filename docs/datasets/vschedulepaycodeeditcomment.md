# vSchedulePayCodeEditComment

**Group:** Detail Dataset → Schedule Detail Views

- Comments attached to Scheduled Paycode Edits (Child of schedulePayCodeEdit)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vSchedulePayCodeEditComment |
| Unique Identifier | payCodeEditsId,partitionDate,personId,commentId,commentNoteId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 10

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeEditsId | INT64 | Pay code edit ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| commentNoteId | INT64 | Schedule open shift comment note ID |  |  |
| timestamp | DATETIME | The timstamp when the comment was entered |  |  |
| notesText | STRING | The text in the note | PII | BLANK |
| dataSourceDisplayName | STRING | The name of the person who entered the comment |  |  |
| comment | STRING | Paycode edit comment |  |  |
| commentId | INT64 | Schedule open shift comment ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

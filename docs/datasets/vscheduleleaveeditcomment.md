# vScheduleLeaveEditComment

**Group:** Detail Dataset → Schedule Detail Views

- Comments attached to Leave Case Edits (Child of scheduleLeaveEdits)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleLeaveEditComment |
| Unique Identifier | leaveEditId,partitionDate,personId,commentId,commentNoteId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 12

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| leaveEditId | INT64 | Schedule leave edit ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| commentNoteId | INT64 | Schedule leave edit comment note ID |  |  |
| commentId | INT64 | Schedule leave edit comment ID |  |  |
| comment | STRING | Schedule leave edit comment |  |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not the comment is active |  |  |
| noteId | INT64 | Note ID |  |  |
| noteText | STRING | Note text | PII | BLANK |
| dataSourceDisplayName | STRING | Data source name |  |  |
| noteTimestamp | DATETIME | The date time stamp the note was entered |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

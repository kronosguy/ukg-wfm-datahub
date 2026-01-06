# vScheduleAuditShiftAuditsComments

**Group:** Detail Dataset → Audit Detail Views

A list of comments for the historical audits of shifts.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditShiftAuditsComments |
| Unique Identifier | shiftId, partitionDate, revisionId, commentId, commentsNoteId, notesTimestamp (nullable) |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 19

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| shiftId | INT64 | Shift ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| auditLocalTimestamp | TIMESTAMP | The date and time that the revision was made in the user's home time zone |  |  |
| auditTimestamp | TIMESTAMP | Timestamp for the schedule change |  |  |
| auditType | STRING | The type of this revision. |  |  |
| auditUser | STRING | The full name of the user who made the revision. | PII |  |
| revisionId | INT64 | The id of the this revision/audit record. |  |  |
| startDateTime | TIMESTAMP | Shift Start Date Time |  |  |
| endDateTime | TIMESTAMP | Shift End Date Time |  |  |
| commentsNoteId | INT64 | The notes attached to this audit |  |  |
| commentId | INT64 | The comment ID |  |  |
| comment | STRING | The comment attached to this audit |  |  |
| activeSwt | BOOLEAN | Boolean flag indicating that the relation to the shift's source is active. |  |  |
| noteId | INT64 | Note ID |  |  |
| notesText | STRING | The note attached to this audit | PII |  |
| dataSourceDisplayName | STRING | Data source of the scheudle audit |  |  |
| notesTimestamp | TIMESTAMP | The date time stamp of the note |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

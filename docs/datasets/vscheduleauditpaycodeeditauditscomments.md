# vScheduleAuditPayCodeEditAuditsComments

**Group:** Detail Dataset → Audit Detail Views

This view provides schedule audit comments related to scheduled pay code edits.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditPayCodeEditAuditsComments |
| Unique Identifier | payCodeEditsId,partitionDate,revisionId,commentId,commentNoteId, timestamp (nullable) |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 19

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeEditsId | INT64 | The ID for the relationship between the pay code edit and schedule. |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| auditLocalTimestamp | TIMESTAMP | The date and time that the revision was made in the user's home time zone. |  |  |
| auditTimestamp | TIMESTAMP | Timestamp for the schedule change |  |  |
| auditType | STRING | The type of this revision. |  |  |
| auditUser | STRING | The full name of the user who made the revision. | PII |  |
| revisionId | INT64 | The id of the this revision/audit record. |  |  |
| startDate | DATE | The inclusive start date of the comment |  |  |
| endDate | DATE | The inclusive end date of the comment |  |  |
| startTime | TIME | The inclusive start time of the commentt |  |  |
| endTime | TIME | The inclusive end time of the commentt |  |  |
| commentNoteId | INT64 | Schedule Audit Comment Note ID |  |  |
| timestamp | TIMESTAMP | The date and time that the comment was made in Greenwich Mean Time (GMT). |  |  |
| notesText | STRING | Comment notes | PII |  |
| dataSourceDisplayName | STRING | Data source of the scheudle audit |  |  |
| comment | STRING | Schedule Audit comment |  |  |
| commentId | INT64 | Schedule Audit Comment ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

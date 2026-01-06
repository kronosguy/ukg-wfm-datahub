# vScheduleAuditPayCodeEditAuditsRelations

**Group:** Detail Dataset → Audit Detail Views

This view provides alist of objects related to scheduled pay code edits

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditPayCodeEditAuditsRelations |
| Unique Identifier | payCodeEditsId,partitionDate,revisionId,relationType,fromId,targetRefId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 21

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| payCodeEditsId | INT64 | The ID for the relationship between the pay code edit and schedule. |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| auditLocalTimestamp | TIMESTAMP | The date and time that the revision was made in the user's home time zone |  |  |
| auditTimestamp | TIMESTAMP | Timestamp for the schedule change |  |  |
| auditType | STRING | The type of this revision. |  |  |
| auditUser | STRING | The full name of the user who made the revision. | PII |  |
| revisionId | INT64 | The id of the this revision/audit record. |  |  |
| type | STRING | The name from the type |  |  |
| startDate | DATE | Shift start date |  |  |
| endDate | DATE | The shift end date |  |  |
| startTime | TIME | Shift start time |  |  |
| endTime | TIME | The shift end time |  |  |
| targetVersion | INT64 | The VERSION from the target |  |  |
| targetRef | STRING | The name of the target |  |  |
| targetRefId | INT64 | The ID from the target |  |  |
| relationType | STRING | Entity relation type |  |  |
| fromQualifier | STRING | The name from the source | PII |  |
| fromId | INT64 | The ID from the source |  |  |
| activeSwt | BOOLEAN | Boolean flag indicating that the relation to the shift's source is active. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

# vScheduleAuditPayCodeEditAuditsPayCodeEditRelations

**Group:** Detail Dataset → Audit Detail Views

This view provides alist of objects related to scheduled pay code edits

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditPayCodeEditAuditsPayCodeEditRelations |
| Unique Identifier | payCodeEditsId,partitionDate,revisionId,relationType,fromId,targetRefId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 22

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
| id | INT64 | Pay coed edits relation ID |  |  |
| startDate | DATE | The shift start date |  |  |
| endDate | DATE | The shift end date |  |  |
| startTime | TIME | The shift start time |  |  |
| endTime | TIME | The shift end time |  |  |
| active | BOOLEAN | Boolean flag indicating that the relation to the shift's source is active. |  |  |
| relationType | STRING | Entity relation type. |  |  |
| targetVersion | INT64 | The VERSION from the target |  |  |
| type | STRING | The name from the type |  |  |
| fromId | INT64 | The ID from the source |  |  |
| fromQualifier | STRING | The name from the source |  |  |
| targetRefId | INT64 | The ID from the target |  |  |
| targetRefQualifier | STRING | The name from the target |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

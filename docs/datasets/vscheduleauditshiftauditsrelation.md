# vScheduleAuditShiftAuditsRelation

**Group:** Detail Dataset → Audit Detail Views

This view provides alist of objects related to the shifts

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditShiftAuditsRelation |
| Unique Identifier | shiftId,partitionDate,revisionId,relationType,fromId,targetId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 19

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| shiftId | INT64 | The shift ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| auditLocalTimestamp | TIMESTAMP | The date and time that the revision was made in the user's home time zone |  |  |
| auditTimestamp | TIMESTAMP | Timestamp for the schedule change |  |  |
| auditType | STRING | The type of this revision. |  |  |
| auditUser | STRING | The full name of the user who made the revision. | PII |  |
| revisionId | INT64 | The id of the this revision/audit record. |  |  |
| startDateTime | TIMESTAMP | The shift start date time |  |  |
| endDateTime | TIMESTAMP | Shift end date time |  |  |
| type | STRING | The name from the type |  |  |
| targetVersion | INT64 | The VERSION from the target |  |  |
| targetId | INT64 | The name from the target |  |  |
| targetQualifier | STRING | The name from the target | PII |  |
| relationType | STRING | Entity relation type. |  |  |
| fromId | INT64 | The from ID |  |  |
| fromQualifier | STRING | The  relationship name between the pay code edit and schedule | PII |  |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not this audit relation is active |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

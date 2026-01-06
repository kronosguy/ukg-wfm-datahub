# vScheduleAuditShiftAuditsSegmentSkillCertProfile

**Group:** Detail Dataset → Audit Detail Views

The list of segments of this availability by Skill Cert Profile

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditShiftAuditsSegmentSkillCertProfile |
| Unique Identifier | shiftId,shiftSegmentID,partitionDate,revisionId,skillCertProfileId) |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 14

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
| startDateTime | TIMESTAMP | Shift start date time |  |  |
| endDateTime | TIMESTAMP | Shift end date time |  |  |
| shiftSegmentId | INT64 | The shift segment ID |  |  |
| skillCertProfile | STRING | Skills and cert profile |  |  |
| skillCertProfileId | INT64 | Skills and cert profile ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

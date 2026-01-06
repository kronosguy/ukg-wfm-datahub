# vScheduleAuditShiftAuditsSegmentTag

**Group:** Detail Dataset → Audit Detail Views

A list of historical audits by shift segment tag

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditShiftAuditsSegmentTag |
| Unique Identifier | shiftId, shiftSegmentID, segmentTagId, segmentTagDefinitionId, partitionDate, revisionId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 16

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
| endDateTime | TIMESTAMP | Shift end date time |  |  |
| shiftSegmentId | INT64 | Shift Segment ID |  |  |
| segmentTagId | INT64 | Segment tag ID |  |  |
| segmentTagColor | STRING | The color of schedule tag segment. |  |  |
| segmentTagDefinition | STRING | The definition of the segment tag |  |  |
| segmentTagDefinitionId | INT64 | Segment tag definition ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

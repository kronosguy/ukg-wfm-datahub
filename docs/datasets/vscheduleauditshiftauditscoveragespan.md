# vScheduleAuditShiftAuditsCoverageSpan

**Group:** Detail Dataset → Audit Detail Views

A list of historical audits of shift by coverage span

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleAuditShiftAuditsCoverageSpan |
| Unique Identifier | shiftId,partitionDate,revisionId,uniqueId |
| Source Pipeline | scheduleAudit (CDC) |

## Columns

**Column count:** 20

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
| startDateTime | TIMESTAMP | Shift start date time |  |  |
| endDateTime | TIMESTAMP | Shift end date time |  |  |
| contributingHours | FLOAT | Total hours in shift coverage span |  |  |
| spanDate | DATE | Coverage span date |  |  |
| uniqueId | STRING | Unique identifier |  |  |
| workloadSpanEndTime | TIME | Unique identifier |  |  |
| name | STRING | Name of the coveage span |  |  |
| workloadSpanStartTime | TIME | The start time of a workload span. |  |  |
| workloadSpanId | INT64 | The ID of a workload span. Can be either a Shift ID or a Zone ID. |  |  |
| workloadSpanSetId | INT64 | The ID of the shift set or zone set containing the shift or zone represented by this workload span. |  |  |
| workloadSpanType | STRING | An enumeration to determine if workload span represents a shift, zone, or interval. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

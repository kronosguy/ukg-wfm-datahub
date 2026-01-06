# vScheduleLeaveEditOverrideSegment

**Group:** Detail Dataset → Schedule Detail Views

- Leave Case Segments (Child of scheduleLeaveEdits)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleLeaveEditOverrideSegment |
| Unique Identifier | leaveEditId,overrideSegmentLeaveTypeId,partitionDate,personId |
| Source Pipeline | schedule (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| leaveEditId | INT64 | Schedule leave edit ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| overrideSegmentLeaveTypeId | INT64 | Override segmant leave type ID |  |  |
| leaveType | STRING | Schedule leave type |  |  |
| overrideSegmentDurationInTime | INT64 | The duration in seconds of this override segment |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

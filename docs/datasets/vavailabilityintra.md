# vAvailabilityIntra

**Group:** Summary Dataset → Summary Staging Views (not for reporting)

- Employee Availability by segment (time range and type) and date converted to 15 min increments for usage in intraday Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAvailabilityIntra |
| Unique Identifier | availabilityId,personId,partitionDate,time_24H |
| Source Pipeline | summaryIntra (DR), availability (CDC) |

## Columns

**Column count:** 15

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| availabilityID | INT64 | Availabilirty ID |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| partitiondate | DATE | Represents date of availability - use to join to date dimension |  |  |
| time_24H | TIME | 24H Time |  |  |
| availabilitySegmentId | INT64 | Avaiablility Segment ID |  |  |
| availabilityType | STRING | Availablity Type Name |  |  |
| availabilityTypeId | INT64 | Availablity Type ID |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| days | FLOAT64 | Number of days in Availability |  |  |
| minutes | INT64 | Total Minutes |  |  |
| hours | FLOAT64 | Total Hours |  |  |
| headCountWholeSpan | INT64 | Whole Span Head Count (if employee is available the entire segment the value will be 1 otherwise 0) |  |  |
| headCountRounded | INT64 | Rounded Head Count (if employee is available 8 minutes or more the value will be 1 otherwise 0) |  |  |
| headCountAny | INT64 | Total Headcount  (if employee is available any part of the segment the value will be 1 otherwise 0) |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

# vScheduleOpenShiftSegmentIntra

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- This view contains open shifts converted to 15 min increments for usage in the intraday Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleOpenShiftSegmentIntra |
| Unique Identifier | partitionDate,orgId,openShiftId,openShiftSegmentId,time_24H |
| Source Pipeline | summaryIntra (DR), scheduleOpenshift (DR) |

## Columns

**Column count:** 27

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| openShiftId | INT64 | Open Shift ID |  |  |
| partitionDate | DATE | Represents date of Open Shift Segment - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| openShiftSegmentId | INT64 | Open Shift Segment ID |  |  |
| time_24H | TIME | 24H Time |  |  |
| minutes | INT64 | Total Minutes |  |  |
| hours | FLOAT | Total Hours |  |  |
| days | FLOAT | Total number of Days |  |  |
| headCountWholeSpan | INT64 | Whole Span Head Count |  |  |
| headCountRounded | INT64 | Rounded Head Count |  |  |
| headCountAnyWorked | INT64 | Total Headcount |  |  |
| openshiftSegmentType | STRING | Open Shift Segment Type |  |  |
| openshiftSegmentTypeId | INT64 | Open Shift Segment Type ID |  |  |
| segmentType | STRING | Open Shift Segment Type |  |  |
| segmentTypeId | INT64 | Open Shift Segment Type ID |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction |  |  |
| orgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| primaryCostCenter | STRING | Primary Cost Center |  |  |
| primaryCostCenterId | INT64 | Primary Cost Center ID |  |  |
| costCenter | STRING | Cost Center Name |  |  |
| costCenterId | INT64 | Cost Center ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

# vScheduleShiftSegmentIntra

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- Scheduled Shift Segments (Child of scheduleShift) - 15min Grain

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vScheduleShiftSegmentIntra |
| Unique Identifier | shiftId,partitionDate,personId,shiftSegmentId,time_24H |
| Source Pipeline | summaryIntra (DR), schedule (CDC) |

## Columns

**Column count:** 27

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| shiftId | INT64 | Shift ID |  |  |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| shiftSegmentId | INT64 | Shift Segment ID |  |  |
| time_24H | TIME | 24H Time |  |  |
| minutes | INT64 | Total Minutes |  |  |
| hours | FLOAT64 | Total Hours |  |  |
| days | FLOAT64 | Total number of Days |  |  |
| headCountWholeSpan | INT64 | Whole Span Head Count (if employee is scheduled the entire segment the value will be 1 otherwise 0) |  |  |
| headCountRounded | INT64 | Rounded Head Count (if employee is scheduled 8 minutes or more the value will be 1 otherwise 0) |  |  |
| headCountAnyWorked | INT64 | Total Headcount  (if employee is scheduled any part of the segment the value will be 1 otherwise 0) |  |  |
| shiftSegmentType | STRING | Shift Segment Type |  |  |
| shiftSegmentTypeId | INT64 | Shift Segment Type ID |  |  |
| segmentType | STRING | Segment Type |  |  |
| segmentTypeId | INT64 | Segment Type ID |  |  |
| laborEntryName1 | STRING | Labor Category 1 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName2 | STRING | Labor Category 2 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName3 | STRING | Labor Category 3 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName4 | STRING | Labor Category 4 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName5 | STRING | Labor Category 5 entry name associated with transaction (applies to labor category transfer) |  |  |
| laborEntryName6 | STRING | Labor Category 6 entry name associated with transaction (applies to labor category transfer) |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| primaryCostCenter | STRING | Primary cost center for employee associated with transaction |  |  |
| primaryCostCenterId | INT64 | Primary cost center ID - joins to cost center dimension |  |  |
| costCenter | STRING | Cost Center name |  |  |
| costCenterId | INT64 | Unique Identifier for a CostCenter joins to costCenter dimension |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

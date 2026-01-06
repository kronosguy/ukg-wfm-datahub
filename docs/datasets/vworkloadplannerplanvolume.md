# vWorkloadPlannerPlanVolume

**Group:** Detail Dataset → Workload Planner

Planned Volume and Planned Weighted Volume per Workload Span

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vWorkloadPlannerPlanVolume |
| Unique Identifier | All fields |
| Source Pipeline | workloadPlannerVolume (DR) |

## Columns

**Column count:** 15

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| partitionDate | DATE | Workload Plan Date |  |  |
| volumeDetailId | INT64 | Unique ID  workload planner planned volume |  |  |
| standardShiftSetId | INT64 | Shift Set ID |  |  |
| scheduleZoneSetId | INT64 | Schedule Zone ID |  |  |
| workloadSpanStandardShiftId | INT64 | Workload Spand Shift Id |  |  |
| workloadSpanScheduleZoneId | INT64 | Wokload Span Schedule Zone Id |  |  |
| workloadSpanType | STRING | An enumeration to determine if workload span represents a shift, zone, or interval. "STANDARD_SHIFT", "SCHEDULE_ZONE", "INTERVAL" |  |  |
| workloadSpanName | STRING | The name of the shift or zone represented by this workload span. |  |  |
| workloadSpanStartTime | TIME | The start time of a workload span. |  |  |
| workloadSpanEndTime | TIME | The end time of a workload span. |  |  |
| volume | FLOAT | Volume amount assigned to workload span |  |  |
| weightedVolume | FLOAT | Weighted volume amount assigned to workload span |  |  |
| versionCount | INT64 | The latest version number |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

# vWorkloadPlannerPlanWorkload

**Group:** Detail Dataset → Workload Planner

Planned Workload per Workload Span Note: Below are the joins needed to link workloadPlannerPlanVolume with workloadPlannerPlanWorkload
workloadPlannerPlanVolume.workloadSpanType = workloadPlannerPlanWorkload.workloadSpanType 
AND 
workloadPlannerPlanVolume.workloadSpanSetId IN (workloadPlannerPlanWorkload.standardShiftSetId, workloadPlannerPlanWorkload.scheduleZoneSetId)
AND
workloadPlannerPlanVolume.workloadSpanId IN (workloadPlannerPlanWorkload.workloadSpanStandardShiftId, workloadPlannerPlanWorkload.workloadSpanScheduleZoneId)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vWorkloadPlannerPlanWorkload |
| Unique Identifier | partitionDate, uniqueID |
| Source Pipeline | workloadPlannerWorkload (DR) |

## Columns

**Column count:** 11

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| partitionDate | DATE | Workload Plan Date |  |  |
| workloadSpanSetId | INT64 | The ID of the shift set or zone set containing the shift or zone represented by this workload span. |  |  |
| workloadSpanId | INT64 | The ID of a workload span. Can be either a Shift ID or a Zone ID. |  |  |
| workloadSpanType | STRING | An enumeration to determine if workload span represents a shift, zone, or interval. "STANDARD_SHIFT", "SCHEDULE_ZONE", "INTERVAL" |  |  |
| workloadSpanName | STRING | The name of the shift or zone represented by this workload span. |  |  |
| workloadSpanStartTime | TIME | The start time of a workload span. |  |  |
| workloadSpanEndTime | TIME | The end time of a workload span. |  |  |
| workloadCount | FLOAT | Workload Count |  |  |
| uniqueID | STRING | Unique identifier |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

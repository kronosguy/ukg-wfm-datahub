# vWorkloadPlannerActualWorkload

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** workloadPlannerVolume (DR)

## What it is

Actual Workload per Workload Span Note: Below are the joins needed to link workloadPlannerActualVolume with workloadPlannerActualWorkload
workloadPlannerActualVolume.workloadSpanType = workloadPlannerActualWorkload.workloadSpanType 
AND 
workloadPlannerActualWorkload.workloadSpanSetId IN (workloadPlannerActualVolume.standardShiftSetId, workloadPlannerActualVolume.scheduleZoneSetId)
AND
workloadPlannerActualWorkload.workloadSpanId IN (workloadPlannerActualVolume.workloadSpanStandardShiftId, workloadPlannerActualVolume.workloadSpanScheduleZoneId)

## Fields

| Field                          | Description                                                                                                                                                       |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vWorkloadPlannerActualWorkload | Actual Workload per Workload Span Note: Below are the joins needed to link workloadPlannerActualVolume with workloadPlannerActualWorkload                         |
|                                | workloadPlannerActualVolume.workloadSpanType = workloadPlannerActualWorkload.workloadSpanType                                                                     |
|                                | AND                                                                                                                                                               |
|                                | workloadPlannerActualWorkload.workloadSpanSetId IN (workloadPlannerActualVolume.standardShiftSetId, workloadPlannerActualVolume.scheduleZoneSetId)                |
|                                | AND                                                                                                                                                               |
|                                | workloadPlannerActualWorkload.workloadSpanId IN (workloadPlannerActualVolume.workloadSpanStandardShiftId, workloadPlannerActualVolume.workloadSpanScheduleZoneId) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

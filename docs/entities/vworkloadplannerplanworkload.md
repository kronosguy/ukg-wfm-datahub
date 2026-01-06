# vWorkloadPlannerPlanWorkload

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** workloadPlannerWorkload (DR)

## What it is

Planned Workload per Workload Span Note: Below are the joins needed to link workloadPlannerPlanVolume with workloadPlannerPlanWorkload
workloadPlannerPlanVolume.workloadSpanType = workloadPlannerPlanWorkload.workloadSpanType 
AND 
workloadPlannerPlanVolume.workloadSpanSetId IN (workloadPlannerPlanWorkload.standardShiftSetId, workloadPlannerPlanWorkload.scheduleZoneSetId)
AND
workloadPlannerPlanVolume.workloadSpanId IN (workloadPlannerPlanWorkload.workloadSpanStandardShiftId, workloadPlannerPlanWorkload.workloadSpanScheduleZoneId)

## Fields

| Field                        | Description                                                                                                                                                   |
|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vWorkloadPlannerPlanWorkload | Planned Workload per Workload Span Note: Below are the joins needed to link workloadPlannerPlanVolume with workloadPlannerPlanWorkload                        |
|                              | workloadPlannerPlanVolume.workloadSpanType = workloadPlannerPlanWorkload.workloadSpanType                                                                     |
|                              | AND                                                                                                                                                           |
|                              | workloadPlannerPlanVolume.workloadSpanSetId IN (workloadPlannerPlanWorkload.standardShiftSetId, workloadPlannerPlanWorkload.scheduleZoneSetId)                |
|                              | AND                                                                                                                                                           |
|                              | workloadPlannerPlanVolume.workloadSpanId IN (workloadPlannerPlanWorkload.workloadSpanStandardShiftId, workloadPlannerPlanWorkload.workloadSpanScheduleZoneId) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# vWorkloadPlannerBudgetWorkload

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** workloadPlannerWorkload (DR)

## What it is

Budget Workload per Workload Span n Note: Below are the joins needed to link workloadPlannerBudgetVolume with workloadPlannerBudgetWorkload workloadPlannerBudgetVolume.workloadSpanType = workloadPlannerBudgetWorkload.workloadSpanType 
AND 
workloadPlannerBudgetVolume.workloadSpanSetId IN (workloadPlannerBudgetWorkload.standardShiftSetId, workloadPlannerBudgetWorkload.scheduleZoneSetId)
AND
workloadPlannerBudgetVolume.workloadSpanId IN (workloadPlannerBudgetWorkload.workloadSpanStandardShiftId, workloadPlannerBudgetWorkload.workloadSpanScheduleZoneId)

## Fields

| Field                          | Description                                                                                                                                                                                                                                |
|:-------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vWorkloadPlannerBudgetWorkload | Budget Workload per Workload Span n Note: Below are the joins needed to link workloadPlannerBudgetVolume with workloadPlannerBudgetWorkload workloadPlannerBudgetVolume.workloadSpanType = workloadPlannerBudgetWorkload.workloadSpanType  |
|                                | AND                                                                                                                                                                                                                                        |
|                                | workloadPlannerBudgetVolume.workloadSpanSetId IN (workloadPlannerBudgetWorkload.standardShiftSetId, workloadPlannerBudgetWorkload.scheduleZoneSetId)                                                                                       |
|                                | AND                                                                                                                                                                                                                                        |
|                                | workloadPlannerBudgetVolume.workloadSpanId IN (workloadPlannerBudgetWorkload.workloadSpanStandardShiftId, workloadPlannerBudgetWorkload.workloadSpanScheduleZoneId)                                                                        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

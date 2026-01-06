# scheduleStartTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

for scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. for unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. end time in hh:mm am|pm format.

## Fields

| Field             | Type   | Description                                                                                                                                                                                                                                                    |
|:------------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scheduleStartTime | INT64  | for scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. for unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. end time in hh:mm am|pm format. |
| scheduleStartTime | INT64  | or scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. for unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. end time in hh:mm am|pm format.  |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# scheduleEndTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The end time of a schedule closes the range of time that allows in-punches to link to an assigned schedule. For scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. For unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. The end time is in hh:mm am|pm format.

## Fields

| Field           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                       |
|:----------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| scheduleEndTime | INT64  | The end time of a schedule closes the range of time that allows in-punches to link to an assigned schedule. For scheduled employees to qualify for the assigned shift, their scheduled start times must be before the end time. For unscheduled employees to qualify for the assigned shift, their in-punches must be before the end time. The end time is in hh:mm am|pm format. |
| scheduleEndTime | INT64  | The end time of a schedule closes the range of time that allows in-punches to link to an assigned schedule.                                                                                                                                                                                                                                                                       |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

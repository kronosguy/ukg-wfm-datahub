# M_SchdPost_Last_PostDeadline_Hrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Count of hours difference between the posting deadline and the date time of the last posting for the the jobs/departments/sites for the schedule week. This number will be negative is the schedule is posted early and positive if the schedule is posted late.

## Fields

| Field                            | Type   | Description                                                                                                                                                                                                                                                      |
|:---------------------------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M_SchdPost_Last_PostDeadline_Hrs | INT64  | Count of hours difference between the posting deadline and the date time of the last posting for the the jobs/departments/sites for the schedule week. This number will be negative is the schedule is posted early and positive if the schedule is posted late. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

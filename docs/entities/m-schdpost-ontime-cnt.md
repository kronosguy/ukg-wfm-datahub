# M_SchdPost_OnTime_Cnt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Count of jobs/departments/sites where the earliest posting date was prior to the posting deadline posting deadline for the schedule week. For each row, the value is 1 if posting was on time or 0 if the posting was late.

## Fields

| Field                 | Type   | Description                                                                                                                                                                                                                 |
|:----------------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M_SchdPost_OnTime_Cnt | INT64  | Count of jobs/departments/sites where the earliest posting date was prior to the posting deadline posting deadline for the schedule week. For each row, the value is 1 if posting was on time or 0 if the posting was late. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

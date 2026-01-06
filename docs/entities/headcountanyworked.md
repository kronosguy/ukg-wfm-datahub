# headCountAnyWorked

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Total Headcount

## Fields

| Field              | Type   | Description                                                                                         |
|:-------------------|:-------|:----------------------------------------------------------------------------------------------------|
| headCountAnyWorked | INT64  | Total Headcount                                                                                     |
| headCountAnyWorked | INT64  | Total Headcount  (if employee is scheduled any part of the segment the value will be 1 otherwise 0) |
| headCountAnyWorked | INT64  | Total Headcount  (if employee works any part of the segment the value will be 1 otherwise 0)        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

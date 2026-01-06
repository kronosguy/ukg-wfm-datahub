# postEarlyHrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

If the job is posted prior to the postDeadlineDtm the value is postDeadLineDtm - firstPostDtm

## Fields

| Field        | Type   | Description                                                                                   |
|:-------------|:-------|:----------------------------------------------------------------------------------------------|
| postEarlyHrs | FLOAT  | If the job is posted prior to the postDeadlineDtm the value is postDeadLineDtm - firstPostDtm |
| postEarlyHrs | INT64  | If the job is posted prior to the postDeadlineDtm the value is postDeadLineDtm - firstPostDtm |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

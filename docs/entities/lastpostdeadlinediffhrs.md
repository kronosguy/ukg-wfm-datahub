# lastPostDeadlineDiffHrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The difference between the postDeadLineDtm and lastPostDtm this number will be negative if it's early and positive if its late

## Fields

| Field                   | Type   | Description                                                                                                                    |
|:------------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------|
| lastPostDeadlineDiffHrs | FLOAT  | The difference between the postDeadLineDtm and lastPostDtm this number will be negative if it's early and positive if its late |
| lastPostDeadlineDiffHrs | INT64  | The difference between the postDeadLineDtm and lastPostDtm this number will be negative if it's early and positive if its late |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

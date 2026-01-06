# postRequiredCnt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

If the the Current Date Time the pipeline is running is greater than the postDeadlineDtm the value is 1 otherwise it's 0

## Fields

| Field           | Type    | Description                                                                                                              |
|:----------------|:--------|:-------------------------------------------------------------------------------------------------------------------------|
| postRequiredCnt | INTEGER | If the the Current Date Time the pipeline is running is greater than the postDeadlineDtm the value is 1 otherwise it's 0 |
| postRequiredCnt | INT64   | If the the Current Date Time the pipeline is running is greater than the postDeadlineDtm the value is 1 otherwise it's 0 |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# leaveCaseStatus

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The status of a leave case for which the leave edit is created.

## Fields

| Field           | Type   | Description                                                     |
|:----------------|:-------|:----------------------------------------------------------------|
| leaveCaseStatus | INT64  | The status of a leave case for which the leave edit is created. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

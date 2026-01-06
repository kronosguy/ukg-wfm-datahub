# coverageCount

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The actual coverage count for the workload span

## Fields

| Field         | Type   | Description                                       |
|:--------------|:-------|:--------------------------------------------------|
| coverageCount | FLOAT  | The actual coverage count for the workload span   |
| coverageCount | FLOAT  | The palnned coverage count for the workload span  |
| coverageCount | FLOAT  | The budgeted coverage count for the workload span |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

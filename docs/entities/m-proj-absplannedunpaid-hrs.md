# M_Proj_AbsPlannedUnpaid_Hrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Projected Absence PlannedUnpaid Hours

## Fields

| Field                       | Type    | Description                                                     |
|:----------------------------|:--------|:----------------------------------------------------------------|
| M_Proj_AbsPlannedUnpaid_Hrs | FLOAT64 | Projected Absence PlannedUnpaid Hours                           |
| M_Proj_AbsPlannedUnpaid_Hrs | FLOAT64 | Pay Category in Absence, Is Paid=No, Absence Category = Planned |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

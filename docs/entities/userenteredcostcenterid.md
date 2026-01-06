# userEnteredCostCenterId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

User entered cost center ID

## Fields

| Field                   | Type   | Description                                                          |
|:------------------------|:-------|:---------------------------------------------------------------------|
| userEnteredCostCenterId | INT64  | User entered cost center ID                                          |
| userEnteredCostCenterId | INT64  | The user-entered Cost Center ID (applies to labor category transfer) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

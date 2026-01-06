# costCenterId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Unique Identifier for a CostCenter joins to costCenter dimension

## Fields

| Field        | Type   | Description                                                                                            |
|:-------------|:-------|:-------------------------------------------------------------------------------------------------------|
| costCenterId | INT64  | Unique Identifier for a CostCenter joins to costCenter dimension                                       |
| costCenterId | INT64  | costCenterId for which the change occured                                                              |
| costCenterId | INT64  | The cost center associated with a node.                                                                |
| costCenterId | INT64  | Unique Identifier for a cost center                                                                    |
| costCenterId | INT64  | Cost Center ID                                                                                         |
| costCenterId | INT64  | Value is null API is not returning correct value,  This will be addressed in a future release          |
| costCenterId | INT64  | Unique Identifier for a CostCenter joins to costCenter dimension  (applies to labor category transfer) |
| costCenterId | INT64  | The ID of a cost center.                                                                               |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# applicationFactor

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The number of items for application factor, a positive value the maximum of which is 9999999999.99999.

## Fields

| Field             | Type   | Description                                                                                            |
|:------------------|:-------|:-------------------------------------------------------------------------------------------------------|
| applicationFactor | FLOAT  | The number of items for application factor, a positive value the maximum of which is 9999999999.99999. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

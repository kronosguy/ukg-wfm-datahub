# vFixedRules

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** fixedRules (DR)

## What it is

- Fixed rules identify constant pay policies that are assigned to employees, such as pay periods, day divides, and the Hours belong to option

## Fields

| Field       | Description                                                                                                                                   |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| vFixedRules | - Fixed rules identify constant pay policies that are assigned to employees, such as pay periods, day divides, and the Hours belong to option |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

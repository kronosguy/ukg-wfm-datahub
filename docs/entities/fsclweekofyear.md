# fsclWeekOfYear

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Fiscal week of year number - generally should be 1-53

## Fields

| Field          | Type   | Description                                           |
|:---------------|:-------|:------------------------------------------------------|
| fsclWeekOfYear | INT64  | Fiscal week of year number - generally should be 1-53 |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

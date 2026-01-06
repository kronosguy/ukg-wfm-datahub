# payPeriodType

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Pay period configuration type Days, Hours, etc.

## Fields

| Field         | Type   | Description                                            |
|:--------------|:-------|:-------------------------------------------------------|
| payPeriodType | STRING | Pay period configuration type Days, Hours, etc.        |
| payPeriodType | STRING | The type of a pay period associated with a fixed rule. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

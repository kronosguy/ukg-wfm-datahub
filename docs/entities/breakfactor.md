# breakFactor

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The value of a break factor expressed as a percent, from 0 to 100.

## Fields

| Field       | Type   | Description                                                        |
|:------------|:-------|:-------------------------------------------------------------------|
| breakFactor | FLOAT  | The value of a break factor expressed as a percent, from 0 to 100. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

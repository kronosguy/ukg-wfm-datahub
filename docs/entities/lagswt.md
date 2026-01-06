# lagSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not to start labor distribution after the labor period. When false, labor distribution starts before the labor period. If no value is passed, labor distribution is the same as the selected labor period.

## Fields

| Field   | Type    | Description                                                                                                                                                                                                                                  |
|:--------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lagSwt  | BOOLEAN | A Boolean indicator of whether or not to start labor distribution after the labor period. When false, labor distribution starts before the labor period. If no value is passed, labor distribution is the same as the selected labor period. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

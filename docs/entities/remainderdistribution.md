# remainderDistribution

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The type indicating how to evenly distribute the remaining labor. ROUNDING: use the standard labor distribution algorithm. LEFT: spread the remaining labor to the left. RIGHT: spread the remaining labor to the right.

## Fields

| Field                 | Type   | Description                                                                                                                                                                                                              |
|:----------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| remainderDistribution | STRING | The type indicating how to evenly distribute the remaining labor. ROUNDING: use the standard labor distribution algorithm. LEFT: spread the remaining labor to the left. RIGHT: spread the remaining labor to the right. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

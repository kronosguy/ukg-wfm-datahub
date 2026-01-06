# M_Lbrfcst_Adjusted_Hrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Labor Forecast Adjusted Hours

## Fields

| Field                  | Type    | Description                   |
|:-----------------------|:--------|:------------------------------|
| M_Lbrfcst_Adjusted_Hrs | FLOAT64 | Labor Forecast Adjusted Hours |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

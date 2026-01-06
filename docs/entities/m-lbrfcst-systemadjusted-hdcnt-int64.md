# M_Lbrfcst_SystemAdjusted_HdCnt (INT64)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

laborForecastTypeName='SYSTEM_ADJUSTED'

## Fields

| Field                                  | Type   | Description                             |
|:---------------------------------------|:-------|:----------------------------------------|
| M_Lbrfcst_SystemAdjusted_HdCnt (INT64) | INT64  | laborForecastTypeName='SYSTEM_ADJUSTED' |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

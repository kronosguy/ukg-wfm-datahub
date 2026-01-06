# M_TrafPatVolFcstAdj_Drvr14_Amt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Volume Forecast Adjusted Driver Driver 14 Amount * Traffic Pattern Forecast Adjusted Driver 14 Percentage

## Fields

| Field                          | Type    | Description                                                                                               |
|:-------------------------------|:--------|:----------------------------------------------------------------------------------------------------------|
| M_TrafPatVolFcstAdj_Drvr14_Amt | FLOAT64 | Volume Forecast Adjusted Driver Driver 14 Amount * Traffic Pattern Forecast Adjusted Driver 14 Percentage |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

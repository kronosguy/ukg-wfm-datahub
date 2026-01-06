# lbrfcstHrs_Earned

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Labor Forecast Hours Earned

## Fields

| Field             | Type    | Description                                                                                                             |
|:------------------|:--------|:------------------------------------------------------------------------------------------------------------------------|
| lbrfcstHrs_Earned | FLOAT64 | Labor Forecast Hours Earned                                                                                             |
| lbrfcstHrs_Earned | FLOAT64 | Earned Hours are currently not available for 15 minute interval but this column is a placeholder for future development |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# M_Lbrfcst_Earned_Hrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Labor Forecast Earned Hours Note: The earned forecast hours engine generates earned hours values based on actual volume data for a provided site or department category and a given forecast week.

## Fields

| Field                | Type    | Description                                                                                                                                                                                        |
|:---------------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M_Lbrfcst_Earned_Hrs | FLOAT64 | Labor Forecast Earned Hours Note: The earned forecast hours engine generates earned hours values based on actual volume data for a provided site or department category and a given forecast week. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# M_Act_All_Amt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Actual All Amount

## Fields

| Field         | Type    | Description                                                  |
|:--------------|:--------|:-------------------------------------------------------------|
| M_Act_All_Amt | FLOAT64 | Actual All Amount                                            |
| M_Act_All_Amt | FLOAT64 | All wages - includes wages for mapped and unmapped pay codes |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

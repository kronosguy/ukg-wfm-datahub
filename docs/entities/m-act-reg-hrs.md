# M_Act_Reg_Hrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Reg Hours

## Fields

| Field         | Type    | Description                                                                                 |
|:--------------|:--------|:--------------------------------------------------------------------------------------------|
| M_Act_Reg_Hrs | FLOAT64 | Reg Hours                                                                                   |
| M_Act_Reg_Hrs | FLOAT64 | if isOTNetDownSwt then actualHours will be deducted from Hours where Pay Category = Regular |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

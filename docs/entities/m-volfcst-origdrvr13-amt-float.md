# M_Volfcst_OrigDrvr13_Amt (float)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

volume forecast amount where volumeType ='GENERATED' and volumeDriverId = 4096

## Fields

| Field                            | Type    | Description                                                                    |
|:---------------------------------|:--------|:-------------------------------------------------------------------------------|
| M_Volfcst_OrigDrvr13_Amt (float) | FLOAT64 | volume forecast amount where volumeType ='GENERATED' and volumeDriverId = 4096 |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

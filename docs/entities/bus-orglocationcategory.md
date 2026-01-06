# Bus_orgLocationCategory

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Category, Department, or Site,   used for Forecasting (Retail)

## Fields

| Field                   | Type   | Description                                                    |
|:------------------------|:-------|:---------------------------------------------------------------|
| Bus_orgLocationCategory | STRING | Category, Department, or Site,   used for Forecasting (Retail) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

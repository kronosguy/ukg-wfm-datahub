# Volume Actuals Metrics (M_VolAct)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Actual volume metrics contain historical amounts
Supported by Business Structure, Date attributes.
Mapping of budget drivers to columns is determined by the volume driver ID

## Fields

| Field                             | Description                                                                |
|:----------------------------------|:---------------------------------------------------------------------------|
| Volume Actuals Metrics (M_VolAct) | Actual volume metrics contain historical amounts                           |
|                                   | Supported by Business Structure, Date attributes.                          |
|                                   | Mapping of budget drivers to columns is determined by the volume driver ID |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# vDtlScheduledTotalByRow

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** valScheduledTotal (DR)

## What it is

Schedule total detail data from IA validation data and Data Hub by person, pay code and date with amounts and variances

## Fields

| Field                   | Description                                                                                                             |
|:------------------------|:------------------------------------------------------------------------------------------------------------------------|
| vDtlScheduledTotalByRow | Schedule total detail data from IA validation data and Data Hub by person, pay code and date with amounts and variances |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

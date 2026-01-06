# inProgressSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not a returned worked shift is currently in progress. in-punch without a corresponding out-punch when the shift is part of a schedule.

## Fields

| Field         | Type    | Description                                                                                                                                                              |
|:--------------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inProgressSwt | BOOLEAN | A Boolean indicator of whether or not a returned worked shift is currently in progress. in-punch without a corresponding out-punch when the shift is part of a schedule. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

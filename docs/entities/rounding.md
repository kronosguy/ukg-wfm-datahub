# rounding

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The value of a round up headcount threshold. The possible values are: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9].

## Fields

| Field    | Type   | Description                                                                                                             |
|:---------|:-------|:------------------------------------------------------------------------------------------------------------------------|
| rounding | FLOAT  | The value of a round up headcount threshold. The possible values are: [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

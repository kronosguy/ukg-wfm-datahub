# durationInHours

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Hours amount for totalized transaction

## Fields

| Field           | Type    | Description                                              |
|:----------------|:--------|:---------------------------------------------------------|
| durationInHours | FLOAT   | Hours amount for totalized transaction                   |
| durationInHours | FLOAT64 | The duration (in hours) of the pay code edit             |
| durationInHours | FLOAT64 | The duration (in hours) after the historical correction. |
| durationInHours | FLOAT64 | The duration (in hours) for the Holiday Credit           |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

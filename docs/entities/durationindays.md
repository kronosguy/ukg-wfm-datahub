# durationInDays

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The duration in days of a pay code edit.

## Fields

| Field          | Type    | Description                                             |
|:---------------|:--------|:--------------------------------------------------------|
| durationInDays | FLOAT   | The duration in days of a pay code edit.                |
| durationInDays | FLOAT64 | The duration (in days) of the pay code edit.            |
| durationInDays | FLOAT   | Days amount for totalized transaction                   |
| durationInDays | FLOAT64 | The duration (in days) after the historical correction. |
| durationInDays | FLOAT64 | The duration (in days) for the Holiday Credit           |
| durationInDays | FLOAT64 | The duration (in days) of the pay code edit             |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

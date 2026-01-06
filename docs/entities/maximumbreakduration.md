# maximumBreakDuration

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The number of minutes that defines a break in labor from 0 to 120. The number must be a multiple of 15.

## Fields

| Field                | Type   | Description                                                                                             |
|:---------------------|:-------|:--------------------------------------------------------------------------------------------------------|
| maximumBreakDuration | INT64  | The number of minutes that defines a break in labor from 0 to 120. The number must be a multiple of 15. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

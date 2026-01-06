# workunitId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

workIUnitId for which the change occured

## Fields

| Field      | Type   | Description                              |
|:-----------|:-------|:-----------------------------------------|
| workunitId | INT64  | workIUnitId for which the change occured |
| workunitId | INT64  | The ID of the work unit                  |
| workunitId | INT64  |                                          |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

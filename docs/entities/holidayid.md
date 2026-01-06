# holidayId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Holiday ID

## Fields

| Field     | Type   | Description                       |
|:----------|:-------|:----------------------------------|
| holidayId | INT64  | Holiday ID                        |
| holidayId | INT64  | The ID of the associated holiday. |
| holidayId | INT64  | The id of the associated holiday. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

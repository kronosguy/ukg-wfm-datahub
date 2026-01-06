# id

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Pay coed edits relation ID

## Fields

| Field   | Type   | Description                               |
|:--------|:-------|:------------------------------------------|
| id      | INT64  | Pay coed edits relation ID                |
| id      | INT64  | Unique identifer Device Id                |
| id      | INT64  | Unique Identifier for a generic job       |
| id      | INT64  | Unique Identifier for a generic location. |
| id      | INT64  | LocationType ID                           |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

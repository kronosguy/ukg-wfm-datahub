# hasCommentsSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator that shows whether or not a Comment is associated with a punch.

## Fields

| Field          | Type    | Description                                                                         |
|:---------------|:--------|:------------------------------------------------------------------------------------|
| hasCommentsSwt | BOOLEAN | A Boolean indicator that shows whether or not a Comment is associated with a punch. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

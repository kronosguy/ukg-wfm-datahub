# commentsAvailableSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not a coment is added for this edit.

## Fields

| Field                | Type    | Description                                                                        |
|:---------------------|:--------|:-----------------------------------------------------------------------------------|
| commentsAvailableSwt | BOOLEAN | A Boolean indicator of whether or not a coment is added for this edit.             |
| commentsAvailableSwt | BOOLEAN | A Boolean indicator of whether or not Comments are associated with a pay code edit |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

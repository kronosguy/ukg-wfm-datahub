# vTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

_No description found in this sheet._

## Fields

| Field   | Type                                                 |
|:--------|:-----------------------------------------------------|
| vTime   | A time view used in materializations of 15 min views |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

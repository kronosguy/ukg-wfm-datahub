# Availability Intraday Metrics (M_Avl)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Availability is at 15 minutes grain level. All dimensions supported

## Fields

| Field                                 | Description                                                         |
|:--------------------------------------|:--------------------------------------------------------------------|
| Availability Intraday Metrics (M_Avl) | Availability is at 15 minutes grain level. All dimensions supported |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

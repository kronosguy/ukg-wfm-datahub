# vVolumeBudget

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** volumeBudget (DR)

## What it is

Customer's budgeted volumes.
- volume budget - daily by category

## Fields

| Field         | Description                         |
|:--------------|:------------------------------------|
| vVolumeBudget | Customer's budgeted volumes.        |
|               | - volume budget - daily by category |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

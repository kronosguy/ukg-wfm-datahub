# vLaborBudget

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** laborBudget (DR)

## What it is

Customer's budgeted amounts for labor costs and hours. Separate rows for budgeted hours and budgeted costs.

- labor budget -  (COST and HOURS) daily by Job(org)

## Fields

| Field        | Description                                                                                                 |
|:-------------|:------------------------------------------------------------------------------------------------------------|
| vLaborBudget | Customer's budgeted amounts for labor costs and hours. Separate rows for budgeted hours and budgeted costs. |
|              |                                                                                                             |
|              | - labor budget -  (COST and HOURS) daily by Job(org)                                                        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

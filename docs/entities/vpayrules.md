# vPayRules

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** payRules (DR)

## What it is

- The pay rule allows you to define and manage rules that control how time and attendance information is processed for each employee.

## Fields

| Field     | Description                                                                                                                           |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------|
| vPayRules | - The pay rule allows you to define and manage rules that control how time and attendance information is processed for each employee. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

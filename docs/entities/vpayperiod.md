# vPayPeriod

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** getPayPeriod (DR)

## What it is

This view/view only contains information for the current pay period - dimPayPeriod in the summary dataset is a better source for reporting by pay period.

- payperiod  (like current, next, last etc)  spans for each payruleid

## Fields

| Field      | Description                                                                                                                                               |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| vPayPeriod | This view/view only contains information for the current pay period - dimPayPeriod in the summary dataset is a better source for reporting by pay period. |
|            |                                                                                                                                                           |
|            | - payperiod  (like current, next, last etc)  spans for each payruleid                                                                                     |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

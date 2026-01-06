# originalMoneyAmount

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The original money amount of the accrual transaction.

## Fields

| Field               | Type    | Description                                                                            |
|:--------------------|:--------|:---------------------------------------------------------------------------------------|
| originalMoneyAmount | FLOAT64 | The original money amount of the accrual transaction.                                  |
| originalMoneyAmount | FLOAT   | Money amount for totalized transaction. Original Amount before Correction              |
| originalMoneyAmount | FLOAT64 | The amount (as a decimal value representing money) prior to the historical correction. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

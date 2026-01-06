# moneyAmount

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The money amount of the accrual transaction.

## Fields

| Field       | Type    | Description                                                                      |
|:------------|:--------|:---------------------------------------------------------------------------------|
| moneyAmount | FLOAT64 | The money amount of the accrual transaction.                                     |
| moneyAmount | FLOAT   | The amount (as a decimal value representing money) of the pay code edit.         |
| moneyAmount | FLOAT64 | The amount (as a decimal value representing money) of the pay code edit.         |
| moneyAmount | FLOAT   | Money amount for totalized transaction                                           |
| moneyAmount | FLOAT64 | The amount (as a decimal value representing money) of the historical correction. |
| moneyAmount | FLOAT64 | Holiday credit money amount                                                      |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

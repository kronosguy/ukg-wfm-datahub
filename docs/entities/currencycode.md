# currencyCode

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Currency code for the amounts . Currency code for the current, probation, planned, pending, taking, earned or available amounts.

## Fields

| Field        | Type   | Description                                                                                                                      |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------|
| currencyCode | STRING | Currency code for the amounts . Currency code for the current, probation, planned, pending, taking, earned or available amounts. |
| currencyCode | STRING | Currency code for amounts i.e. USD, GBP                                                                                          |
| currencyCode | STRING | The three digit ISO currency code.                                                                                               |
| currencyCode | STRING | Currency Code                                                                                                                    |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

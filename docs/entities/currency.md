# currency

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

If amount is cost type then currency code. (e.g. USD)

## Fields

| Field    | Type    | Description                                                               |
|:---------|:--------|:--------------------------------------------------------------------------|
| currency | STRING  | If amount is cost type then currency code. (e.g. USD)                     |
| currency | BOOLEAN | Indicates if amount is a currency amount                                  |
| currency | STRING  | Currency name                                                             |
| currency | BOOLEAN | A Boolean indicator of whether or not a Volume Driver is currency-related |
| currency | STRING  | Currency code if volume driver is currency amount, null if not            |
| currency | STRING  | Curency Type                                                              |
| currency | STRING  | Currency                                                                  |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

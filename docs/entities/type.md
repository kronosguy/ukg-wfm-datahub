# type

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The type of accrual transaction. i.e. "TAKEN", "GRANT", "ACCRUAL_RESET"

## Fields

| Field   | Type   | Description                                                             |
|:--------|:-------|:------------------------------------------------------------------------|
| type    | STRING | The type of accrual transaction. i.e. "TAKEN", "GRANT", "ACCRUAL_RESET" |
| type    | STRING | The name from the type                                                  |
| type    | STRING | The data type of the pipeline setting                                   |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

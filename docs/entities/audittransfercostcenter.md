# auditTransferCostCenter

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Transfer Cost Center Name (at the time of transaction)

## Fields

| Field                   | Type   | Description                                            |
|:------------------------|:-------|:-------------------------------------------------------|
| auditTransferCostCenter | STRING | Transfer Cost Center Name (at the time of transaction) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

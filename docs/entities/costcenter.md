# costCenter

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Cost Center name

## Fields

| Field      | Type   | Description                                            |
|:-----------|:-------|:-------------------------------------------------------|
| costCenter | STRING | Cost Center name                                       |
| costCenter | STRING | Cost Center Name (applies to cost cent transfer)       |
| costCenter | STRING | Cost Center name (applies to cost cent transfer)       |
| costCenter | STRING | Cost center name at the time of the transaction        |
| costCenter | STRING | Cost Center Name  (applies to labor category transfer) |
| costCenter | STRING | Cost Center associated with the transaction            |
| costCenter | STRING | Cost Center Name                                       |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

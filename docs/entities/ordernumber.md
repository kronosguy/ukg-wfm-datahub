# orderNumber

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

order number

## Fields

| Field       | Type   | Description                                                                                  |
|:------------|:-------|:---------------------------------------------------------------------------------------------|
| orderNumber | INT64  | order number                                                                                 |
| orderNumber | INT64  | An order number associated with processing work orders that can be configured in a pay rule. |
| orderNumber | INT64  | Order number                                                                                 |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# orderNum

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

An order number associated with processing work orders that can be configured in a pay rule.

## Fields

| Field    | Type   | Description                                                                                  |
|:---------|:-------|:---------------------------------------------------------------------------------------------|
| orderNum | INT64  | An order number associated with processing work orders that can be configured in a pay rule. |
| orderNum | INT64  | The order number of the assignment rules that are assigned to a particular pay rule.         |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

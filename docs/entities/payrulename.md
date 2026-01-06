# payRuleName

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Pay Rule Name

## Fields

| Field       | Type   | Description                                                                                                |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------|
| payRuleName | STRING | Pay Rule Name                                                                                              |
| payRuleName | STRING | Assigned pay rule name                                                                                     |
| payRuleName | STRING | Pay rule name                                                                                              |
| payRuleName | STRING | The name of a pay rule. The name can be up to 32 characters long, is case insensitive, and must be unique. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

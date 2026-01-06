# managerApprovalRestrictionRuleId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A reference to the manager approval restriction rule.

## Fields

| Field                            | Type   | Description                                           |
|:---------------------------------|:-------|:------------------------------------------------------|
| managerApprovalRestrictionRuleId | INT64  | A reference to the manager approval restriction rule. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# payRuleId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

payRuleId for which the change occured

## Fields

| Field     | Type   | Description                                                               |
|:----------|:-------|:--------------------------------------------------------------------------|
| payRuleId | INT64  | payRuleId for which the change occured                                    |
| payRuleId | INT64  | The ID of a pay rule join with vPayRules                                  |
| payRuleId | INT64  | Unique identifier of the pay rule that the pay period is associated with. |
| payRuleId | INT64  | Pay rule ID                                                               |
| payRuleId | INT64  | The ID of a pay rule.                                                     |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

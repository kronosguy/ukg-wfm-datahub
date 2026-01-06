# workRuleId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Work rule ID

## Fields

| Field      | Type   | Description                                                                                                      |
|:-----------|:-------|:-----------------------------------------------------------------------------------------------------------------|
| workRuleId | INT64  | Work rule ID                                                                                                     |
| workRuleId | INT64  | Work Rule ID                                                                                                     |
| workRuleId | INT64  | Unique identifier of a transfer work rule. Joins to workRule dimension                                           |
| workRuleId | INT64  | The work rule ID                                                                                                 |
| workRuleId | INT64  | The name of the associated work rule that identifies the work rule that interprets and calculates employee time. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

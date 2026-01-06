# workRuleTransferSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not the work rule transfers option is enabled for this effective pay rule. When this option is enabled, any work rule transfer that was entered is allowed to continue until a new transaction (employee punch, timecard edit, or group edit) is entered.

## Fields

| Field               | Type    | Description                                                                                                                                                                                                                                                                                 |
|:--------------------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| workRuleTransferSwt | BOOLEAN | A Boolean indicator of whether or not the work rule transfers option is enabled for this effective pay rule. When this option is enabled, any work rule transfer that was entered is allowed to continue until a new transaction (employee punch, timecard edit, or group edit) is entered. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

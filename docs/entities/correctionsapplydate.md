# correctionsApplyDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The apply date for corrections. Valid values are: 1:'today', 2:'first day of the current pay period', 3:'last day of the current pay period', 4:'first day of the previous pay period', 5:'last day of the previous pay period'.

## Fields

| Field                | Type   | Description                                                                                                                                                                                                                      |
|:---------------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| correctionsApplyDate | INT64  | The apply date for corrections. Valid values are: 1:'today', 2:'first day of the current pay period', 3:'last day of the current pay period', 4:'first day of the previous pay period', 5:'last day of the previous pay period'. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

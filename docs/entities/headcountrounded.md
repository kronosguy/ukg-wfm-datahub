# headCountRounded

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Rounded Head Count (if employee is available 8 minutes or more the value will be 1 otherwise 0)

## Fields

| Field            | Type   | Description                                                                                     |
|:-----------------|:-------|:------------------------------------------------------------------------------------------------|
| headCountRounded | INT64  | Rounded Head Count (if employee is available 8 minutes or more the value will be 1 otherwise 0) |
| headCountRounded | INT64  | Rounded Head Count                                                                              |
| headCountRounded | INT64  | Rounded Head Count (if employee is scheduled 8 minutes or more the value will be 1 otherwise 0) |
| headCountRounded | INT64  | Rounded Head Count (if employee works 8 minutes or more the value will be 1 otherwise 0)        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

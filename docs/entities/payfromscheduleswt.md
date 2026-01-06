# payFromScheduleSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator that functions in conjunction with applyonly. When payfromschedule is equal to true and applyonly is equal to false, the behavior corresponds to when apply scheduled edits is equal to always and apply scheduled shifts is equal to never.

## Fields

| Field              | Type    | Description                                                                                                                                                                                                                                                      |
|:-------------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| payFromScheduleSwt | BOOLEAN | A Boolean indicator that functions in conjunction with applyonly. When payfromschedule is equal to true and applyonly is equal to false, the behavior corresponds to when apply scheduled edits is equal to always and apply scheduled shifts is equal to never. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

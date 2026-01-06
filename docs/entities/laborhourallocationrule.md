# laborHourAllocationRule

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A type indicating how to allocate labor hours. The default value is ACTUAL_DAY. ACTUAL_DAY: Labor hours are split as they fall across the day divide. START_DAY: All hours for the job are applied to the day on which the labor hours begin. END_DAY: All hours for the job are applied to the day on which the labor hours end.

## Fields

| Field                   | Type   | Description                                                                                                                                                                                                                                                                                                                       |
|:------------------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| laborHourAllocationRule | STRING | A type indicating how to allocate labor hours. The default value is ACTUAL_DAY. ACTUAL_DAY: Labor hours are split as they fall across the day divide. START_DAY: All hours for the job are applied to the day on which the labor hours begin. END_DAY: All hours for the job are applied to the day on which the labor hours end. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

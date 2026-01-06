# vScheduleHoliday

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** schedule (CDC)

## What it is

- lists the person/dates where exists a scheduled holiday. NOTE: the holidays are tied to the employee's pay rule and the holidays associated with that pay rule

## Fields

| Field            | Description                                                                                                                                                      |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vScheduleHoliday | - lists the person/dates where exists a scheduled holiday. NOTE: the holidays are tied to the employee's pay rule and the holidays associated with that pay rule |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

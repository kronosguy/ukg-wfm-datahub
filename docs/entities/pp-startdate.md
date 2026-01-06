# PP_startDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Pay Period start date

## Fields

| Field        | Type   | Description                                                     |
|:-------------|:-------|:----------------------------------------------------------------|
| PP_startDate | DATE   | Pay Period start date                                           |
| PP_startDate | DATE   | Pay period start date                                           |
| PP_startDate |        | Pay Period Start Date - first date in the associated pay period |
| PP_startDate |        | Pay Period Start Date                                           |
| PP_startDate | DATE   | Pay Period Start Date                                           |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

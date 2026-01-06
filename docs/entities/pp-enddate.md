# PP_endDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Pay Period end date

## Fields

| Field      | Type   | Description                                                  |
|:-----------|:-------|:-------------------------------------------------------------|
| PP_endDate | DATE   | Pay Period end date                                          |
| PP_endDate | DATE   | Pay period end date                                          |
| PP_endDate |        | Pay Period End Date - last date in the associated pay period |
| PP_endDate |        | Pay Period End Date                                          |
| PP_endDate | DATE   | Payperiod End Date                                           |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

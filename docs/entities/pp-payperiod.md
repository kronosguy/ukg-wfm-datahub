# PP_payPeriod

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Pay Period name

## Fields

| Field        | Type   | Description                                                                                                                      |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------|
| PP_payPeriod | STRING | Pay Period name                                                                                                                  |
| PP_payPeriod | STRING | Pay period name - describes relative to current pay period                                                                       |
| PP_payPeriod | STRING | Symbolic Time Period                                                                                                             |
| PP_payPeriod |        | Pay Period Name - Current Pay Period, 15 Pay Periods in the past and 5 Pay Periods in the future will be available for reporting |
| PP_payPeriod |        | Pay Period                                                                                                                       |
| PP_payPeriod | STRING | Pay Period                                                                                                                       |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

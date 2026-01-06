# PP_payPeriodOffset

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Number of pay period back or forward from current pay period

## Fields

| Field              | Type   | Description                                                                                                                                                                                                                                                                                                                                                                      |
|:-------------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PP_payPeriodOffset | INT64  | Number of pay period back or forward from current pay period                                                                                                                                                                                                                                                                                                                     |
| PP_payPeriodOffset | INT64  | Indicates number of pay periods in the past or future.                                                                                                                                                                                                                                                                                                                           |
| PP_payPeriodOffset | INT64  | Number of pay periods in the future or past                                                                                                                                                                                                                                                                                                                                      |
| PP_payPeriodOffset |        | Pay Period Offset - indicates sequentially timing of the pay period relative to current pay period.  The value will be zero for current pay period and negative INT64 for Pay Periods in Past (I.e. -1 for Previous Pay Period, -2 for Two Pay Periods back and so on and Positive INT64 for future Pay Periods (i.e. 1 for Next Pay Period and 2 for Two pay periods in future) |
| PP_payPeriodOffset |        | Pay Period Offset                                                                                                                                                                                                                                                                                                                                                                |
| PP_payPeriodOffset | INT64  | Pay Period Offset                                                                                                                                                                                                                                                                                                                                                                |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# endDateTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Shift End Date Time

## Fields

| Field       | Type      | Description                                                                                                                                                                                                                                      |
|:------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| endDateTime | TIMESTAMP | Shift End Date Time                                                                                                                                                                                                                              |
| endDateTime | TIMESTAMP | Shift end date time                                                                                                                                                                                                                              |
| endDateTime | TIMESTAMP | The end date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss).                                                                                                                                                 |
| endDateTime | DATETIME  | Schedule end date time                                                                                                                                                                                                                           |
| endDateTime | DATETIME  | The shift end date time                                                                                                                                                                                                                          |
| endDateTime | DATETIME  | Shift end date time                                                                                                                                                                                                                              |
| endDateTime | DATETIME  | Shift End DAte Time                                                                                                                                                                                                                              |
| endDateTime | DATETIME  | Schedule End Date Time                                                                                                                                                                                                                           |
| endDateTime | DATETIME  | The inclusive end date and time segment from the totalizer note: this time is rounded if employee workRule has an associated Rounding rule for punches                                                                                           |
| endDateTime | DATETIME  | The end date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss).                                                                                                                                                   |
| endDateTime | DATETIME  | An optional field containing the end date and time based on configured rounding rules.                                                                                                                                                           |
| endDateTime | DATETIME  | The inclusive end date and time segment from the totalizer (This value will align with vTimecardWorkShiftSpan.roundedEndDateTime, and its time zone will match that of the shift's start time to ensure consistency in time-based calculations.) |
| endDateTime | DATETIME  | Work Shift End Date Time                                                                                                                                                                                                                         |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

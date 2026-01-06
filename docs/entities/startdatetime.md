# startDateTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Shift Start Date Time

## Fields

| Field         | Type      | Description                                                                                                                                                                                                                                                |
|:--------------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| startDateTime | TIMESTAMP | Shift Start Date Time                                                                                                                                                                                                                                      |
| startDateTime | TIMESTAMP | Shift start date time                                                                                                                                                                                                                                      |
| startDateTime | TIMESTAMP | The shift start date time                                                                                                                                                                                                                                  |
| startDateTime | TIMESTAMP | The start date and time of an ESS request in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss).                                                                                                                                                         |
| startDateTime | DATETIME  | Schedule start date time                                                                                                                                                                                                                                   |
| startDateTime | DATETIME  | The shift start date time                                                                                                                                                                                                                                  |
| startDateTime | DATETIME  | Shift start date time                                                                                                                                                                                                                                      |
| startDateTime | DATETIME  | Shift Start Date Time                                                                                                                                                                                                                                      |
| startDateTime | DATETIME  | The inclusive start date and time segment from the totalizer note: this time is rounded if employee workRule has an associated Rounding rule for punches                                                                                                   |
| startDateTime | DATETIME  | The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss).                                                                                                                                                           |
| startDateTime | DATETIME  | The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss)                                                                                                                                                            |
| startDateTime | DATETIME  | The earliest start date associated with a timecard in ISO_LOCAL_DATE format (YYYY-MM-DD).                                                                                                                                                                  |
| startDateTime | DATETIME  | The date and time of the start of the activity in ISO_LOCAL_DATE_TIME format (yyyy-MM-dd HH:mm:ss.SSS).                                                                                                                                                    |
| startDateTime | DATETIME  | Work Span Start Date Time.  The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss).                                                                                                                               |
| startDateTime | DATETIME  | The inclusive start date and time segment from the totalizer (Note: This value will align with vTimecardWorkShiftSpan.roundedStartDateTime, and its time zone will match that of the shift's start time to ensure consistency in time-based calculations.) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

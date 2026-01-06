# endTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The shift end time

## Fields

| Field   | Type   | Description                                                                                           |
|:--------|:-------|:------------------------------------------------------------------------------------------------------|
| endTime | TIME   | The shift end time                                                                                    |
| endTime | TIME   | The inclusive end time of the commentt                                                                |
| endTime | TIME   | The inclusive end time of the coverage span                                                           |
| endTime | TIME   | End date time of 15 minute span that the volume amount was recorded                                   |
| endTime | TIME   | End date/time for span labor forecast                                                                 |
| endTime | TIME   | The end time of a labor forecast limit item, from 00:00 to 23:45. The value must be a multiple of 15. |
| endTime | TIME   | The end time of a period element, from 00:00 to 23:45. The value must be a multiple of 15.            |
| endTime | TIME   | Interval End Time                                                                                     |
| endTime | TIME   | End time                                                                                              |
| endTime | TIME   | Availability end time                                                                                 |
| endTime | TIME   | Schdeule end time                                                                                     |
| endTime | TIME   | Shift End Time                                                                                        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

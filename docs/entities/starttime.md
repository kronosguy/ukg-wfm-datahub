# startTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The inclusive start time of the pay code edit

## Fields

| Field     | Type   | Description                                                                                             |
|:----------|:-------|:--------------------------------------------------------------------------------------------------------|
| startTime | TIME   | The inclusive start time of the pay code edit                                                           |
| startTime | TIME   | The inclusive start time of the commentt                                                                |
| startTime | TIME   | The inclusive end time of the coverage span                                                             |
| startTime | TIME   | The shift start time                                                                                    |
| startTime | TIME   | Shift start time                                                                                        |
| startTime | TIME   | Approval period start time of the time-off period; in ISO_LOCAL_TIME format (HH:mm:ss.SSS).             |
| startTime | TIME   | Start time of the time-off period; in ISO_LOCAL_TIME format (HH:mm:ss.SSS).                             |
| startTime | TIME   | Start date time of 15 minute span that the volume amount was recorded                                   |
| startTime | TIME   | Start date/time for span labor forecast                                                                 |
| startTime | TIME   | The start time of a labor forecast limit item, from 00:00 to 23:45. The value must be a multiple of 15. |
| startTime | TIME   | The start time of a period element, from 00:00 to 23:45. The value must be a multiple of 15.            |
| startTime | TIME   | Interval Start Time                                                                                     |
| startTime | TIME   | Start time                                                                                              |
| startTime | TIME   | Availability start time                                                                                 |
| startTime | TIME   | Shift Start Time                                                                                        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# startDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

start date of a date range associated with an HR position code

## Fields

| Field     | Type   | Description                                                                               |
|:----------|:-------|:------------------------------------------------------------------------------------------|
| startDate | DATE   | start date of a date range associated with an HR position code                            |
| startDate | DATE   | The shift start date                                                                      |
| startDate | DATE   | The inclusive start date of the comment                                                   |
| startDate | DATE   | The inclusive start date of the coverage span                                             |
| startDate | DATE   | Shift start date                                                                          |
| startDate | DATE   | Approval period start date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD). |
| startDate | DATE   | The start date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD).             |
| startDate | DATE   | Start Date of the pay period                                                              |
| startDate | DATE   | The effective start date                                                                  |
| startDate | DATE   | Hours of Operation Start Date                                                             |
| startDate | DATE   | Shift Start Date                                                                          |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

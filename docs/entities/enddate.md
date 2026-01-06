# endDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The end date of the accrual transaction.

## Fields

| Field   | Type   | Description                                                                                 |
|:--------|:-------|:--------------------------------------------------------------------------------------------|
| endDate | DATE   | The end date of the accrual transaction.                                                    |
| endDate | DATE   | end date of a date range associated with an HR position code                                |
| endDate | DATE   | The shift end date                                                                          |
| endDate | DATE   | The inclusive end date of the comment                                                       |
| endDate | DATE   | The inclusive end date of the  coverage span                                                |
| endDate | DATE   | Approval period the end date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD). |
| endDate | DATE   | The end date of the time-off period; in ISO_LOCAL_DATE format (YYYY-MM-DD).                 |
| endDate | DATE   | End date of the pay period                                                                  |
| endDate | DATE   | The effective end date                                                                      |
| endDate | DATE   | Hours of Operation End Date                                                                 |
| endDate | DATE   | Schedule end date                                                                           |
| endDate | DATE   | Shift End Date                                                                              |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

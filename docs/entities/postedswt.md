# postedSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The pay code edit posted status.

## Fields

| Field     | Type    | Description                                                                                    |
|:----------|:--------|:-----------------------------------------------------------------------------------------------|
| postedSwt | BOOLEAN | The pay code edit posted status.                                                               |
| postedSwt | BOOLEAN | A Boolean indicator of whether or not the employee has been notified of the posted shift.      |
| postedSwt | BOOLEAN | The Boolean flag  that the system generated this day lock.                                     |
| postedSwt | BOOLEAN | The Boolean indicating that the holiday is posted                                              |
| postedSwt | BOOLEAN | A Boolean indicator of whether or not the employee has been notified of the posted leave edit. |
| postedSwt | BOOLEAN | A Boolean indicator of whether or not a shift is posted.                                       |
| postedSwt | BOOLEAN | A Boolean indicator of whether or not a pay code edit is posted.                               |
| postedSwt | BOOLEAN | If job is posted the value is True and False if the job in unposted                            |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

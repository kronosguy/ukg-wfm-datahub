# workWeekApplyDateTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The date and time for which the totals are applied in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). This property is returned when the forWorkWeek request payload Boolean is 'true'

## Fields

| Field                 | Type     | Description                                                                                                                                                                                  |
|:----------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| workWeekApplyDateTime | DATETIME | The date and time for which the totals are applied in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). This property is returned when the forWorkWeek request payload Boolean is 'true' |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

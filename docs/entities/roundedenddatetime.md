# roundedEndDateTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The rounded punch date and time.

## Fields

| Field              | Type     | Description                                                                                                                                                                                                                                                                                                                                                       |
|:-------------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| roundedEndDateTime | DATETIME | The rounded punch date and time.                                                                                                                                                                                                                                                                                                                                  |
| roundedEndDateTime | DATETIME | Work Span Rounded End Date Time.  The start date and time of a date range in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). (Note: If an employee clocks in from one time zone and clocks out from another, the time zone associated with this value will align with the clock-in time zone. This ensures accurate calculation of the total hours worked.) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

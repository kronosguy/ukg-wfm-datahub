# vSchedulePostJobsByWeek

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

- This view included all jobs by scneduled week whether it was posted or never posted.  Since the API only returns posted jobs we insert never posted jobs and these records will have a postpersonId = -999

## Fields

| Field                   | Description                                                                                                                                                                                                  |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vSchedulePostJobsByWeek | - This view included all jobs by scneduled week whether it was posted or never posted.  Since the API only returns posted jobs we insert never posted jobs and these records will have a postpersonId = -999 |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

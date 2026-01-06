# vFiscalCalendar

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** This is loaded via uploading a file to Data Hub Director. The fiscal calendar is loaded into DHD and then pushed to the fiscalCalendar view.

## What it is

- Imported Fiscal Calendar (1), must be imported thru the standard process and will only represent the dates imported(caution on joins outside of the date range)

## Fields

| Field           | Description                                                                                                                                                       |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vFiscalCalendar | - Imported Fiscal Calendar (1), must be imported thru the standard process and will only represent the dates imported(caution on joins outside of the date range) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

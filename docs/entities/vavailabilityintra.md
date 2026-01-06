# vAvailabilityIntra

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** summaryIntra (DR), availability (CDC)

## What it is

- Employee Availability by segment (time range and type) and date converted to 15 min increments for usage in intraday Views

## Fields

| Field              | Description                                                                                                                  |
|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| vAvailabilityIntra | - Employee Availability by segment (time range and type) and date converted to 15 min increments for usage in intraday Views |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

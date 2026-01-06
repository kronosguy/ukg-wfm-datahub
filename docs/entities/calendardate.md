# calendarDate

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The effective date of the currency exchange rate.  There is one row per day betwene the effective and expiration date of the currency exchnange

## Fields

| Field        | Type   | Description                                                                                                                                     |
|:-------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| calendarDate | DATE   | The effective date of the currency exchange rate.  There is one row per day betwene the effective and expiration date of the currency exchnange |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

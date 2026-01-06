# closeTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The close  time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS).

## Fields

| Field     | Type   | Description                                                                                          |
|:----------|:-------|:-----------------------------------------------------------------------------------------------------|
| closeTime | TIME   | The close  time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS).  |
| closeTime | TIME   | The opening time associated with an hours of operation item in ISO_LOCAL_TIME format (HH:mm:ss.SSS). |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

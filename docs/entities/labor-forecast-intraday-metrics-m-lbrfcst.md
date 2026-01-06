# Labor Forecast Intraday Metrics (M_Lbrfcst)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Labor Forecast metrics are headcounts at 15 min grain. all dimensions except BusPri_ and Person_ supported

## Fields

| Field                                       | Description                                                                                                |
|:--------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| Labor Forecast Intraday Metrics (M_Lbrfcst) | Labor Forecast metrics are headcounts at 15 min grain. all dimensions except BusPri_ and Person_ supported |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

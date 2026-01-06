# Healthcare Productivity

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Healthcare Productivity is a Dimensions offering for healthcare providers to report on staffing levels relative to volume. These metrics are configured in Dimensions and loaded into Data Hub by the Healthcare Analytics wrapper/pipelines.

## Fields

| Field                   | Description                                                                                                                                                                                                                                   |
|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Healthcare Productivity | Healthcare Productivity is a Dimensions offering for healthcare providers to report on staffing levels relative to volume. These metrics are configured in Dimensions and loaded into Data Hub by the Healthcare Analytics wrapper/pipelines. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

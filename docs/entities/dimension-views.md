# Dimension Views

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

These Views contain the attributes specific to particular reporting domains and can be used with the metrics in the summary Views.  They may also be used to for dimensional metadata in BI tools.

## Fields

| Field           | Description                                                                                                                                                                                        |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dimension Views | These Views contain the attributes specific to particular reporting domains and can be used with the metrics in the summary Views.  They may also be used to for dimensional metadata in BI tools. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

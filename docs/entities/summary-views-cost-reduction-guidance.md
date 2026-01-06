# Summary Views - Cost Reduction Guidance

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Where you can,  use a BI reporting tool's internal "symbolic time period"(STP) logic against the date_partitionDate column rather than any of the STP related objects in ANY of these Views. and Views.  This will reduce GBQ scan cost for those customers who are not pre-paying for slot time monthly.

## Fields

| Field                                   | Description                                                                                                                                                                                                                                                                                               |
|:----------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Summary Views - Cost Reduction Guidance | Where you can,  use a BI reporting tool's internal "symbolic time period"(STP) logic against the date_partitionDate column rather than any of the STP related objects in ANY of these Views. and Views.  This will reduce GBQ scan cost for those customers who are not pre-paying for slot time monthly. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

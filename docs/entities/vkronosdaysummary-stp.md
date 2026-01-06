# vKronosDaySummary_STP

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** view on view vKronosDailySummary

## What it is

Same as vKronosDailySummary but includes the "STPName" field.  All data in this view is replicated to all STP's, so you would filter each metric or graph in your visualization tool on the STPName field.  

There is an "All Dates" STP which, when filtered, provides all data so that you can utilize this view exactly as you would the above, in the same report.

## Fields

| Field                 | Description                                                                                                                                                                                                  |
|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vKronosDaySummary_STP | Same as vKronosDailySummary but includes the "STPName" field.  All data in this view is replicated to all STP's, so you would filter each metric or graph in your visualization tool on the STPName field.   |
|                       |                                                                                                                                                                                                              |
|                       | There is an "All Dates" STP which, when filtered, provides all data so that you can utilize this view exactly as you would the above, in the same report.                                                    |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

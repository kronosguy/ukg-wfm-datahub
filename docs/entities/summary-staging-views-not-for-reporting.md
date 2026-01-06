# Summary Staging Views (not for reporting)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The Summary Views may contain diferent types of transactional data. These "unpivot or intraDay Views/Views contain detail data that has been logically transformed in the process of loading data into summary Views. These Views are not intended for analytical reporting as that is the purpose of the summary Views.

## Fields

| Field                                     | Description                                                                                                                                                                                                                                                                                                              |
|:------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Summary Staging Views (not for reporting) | The Summary Views may contain diferent types of transactional data. These "unpivot or intraDay Views/Views contain detail data that has been logically transformed in the process of loading data into summary Views. These Views are not intended for analytical reporting as that is the purpose of the summary Views. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

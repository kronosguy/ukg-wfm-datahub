# Data Detail Validation

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Views that support Data Hub data validation against Information Access dataview data.  These Views are populated when the validation pipelines are run manually.  Note: Data from these Views is not intended for reporting analysis or extraction.

## Fields

| Field                  | Description                                                                                                                                                                                                                                         |
|:-----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Detail Validation | Views that support Data Hub data validation against Information Access dataview data.  These Views are populated when the validation pipelines are run manually.  Note: Data from these Views is not intended for reporting analysis or extraction. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

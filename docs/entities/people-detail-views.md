# People Detail Views

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Detail Views for people data.  The people view is the person's current Dimensions data pulled from the numerous effective dated supporting Views.

## Fields

| Field               | Description                                                                                                                                       |
|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| People Detail Views | Detail Views for people data.  The people view is the person's current Dimensions data pulled from the numerous effective dated supporting Views. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

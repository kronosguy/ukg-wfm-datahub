# Hours of Operation Attributes (HROP)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Hours of Operation by Org and Date at the 15 minute grain

## Fields

| Field                                | Description                                               |
|:-------------------------------------|:----------------------------------------------------------|
| Hours of Operation Attributes (HROP) | Hours of Operation by Org and Date at the 15 minute grain |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

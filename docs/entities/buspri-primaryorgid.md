# BusPri_primaryOrgId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Primary Org Id

## Fields

| Field               | Type   | Description                                                                                           |
|:--------------------|:-------|:------------------------------------------------------------------------------------------------------|
| BusPri_primaryOrgId | INT64  | Primary Org Id                                                                                        |
| BusPri_primaryOrgId | INT64  | Org ID for the Business Structure Location based on Location type mappings in Data Hub configuration. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

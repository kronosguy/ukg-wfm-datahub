# Bus_orgId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Primary Key (  Mimics behavior from ORG_IDS_ID in WFAN) DOES NOT contain all previous versions of the org path which are currently active.  - Should be used for all joins to detail fact Views.

## Fields

| Field     | Type   | Description                                                                                                                                                                                      |
|:----------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bus_orgId | INT64  | Primary Key (  Mimics behavior from ORG_IDS_ID in WFAN) DOES NOT contain all previous versions of the org path which are currently active.  - Should be used for all joins to detail fact Views. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

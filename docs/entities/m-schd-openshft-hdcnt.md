# M_Schd_OpenShft_HdCnt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Scheduled Open shift head count (if scheduled hours less than 8 minutes in 15 minutes span  then 0 else 1) where segmentType = 'REGULAR_SEGMENT'

## Fields

| Field                 | Type   | Description                                                                                                                                      |
|:----------------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| M_Schd_OpenShft_HdCnt | INT64  | Scheduled Open shift head count (if scheduled hours less than 8 minutes in 15 minutes span  then 0 else 1) where segmentType = 'REGULAR_SEGMENT' |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# M_ReqstTimeOff_Completed_Cnt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Total number of completed  request which only include request that were Approved or Refused by reviewer

## Fields

| Field                        | Type   | Description                                                                                             |
|:-----------------------------|:-------|:--------------------------------------------------------------------------------------------------------|
| M_ReqstTimeOff_Completed_Cnt | INT64  | Total number of completed  request which only include request that were Approved or Refused by reviewer |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

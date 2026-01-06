# vEssSelfScheduleStatusChange

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** essSelfSchedule (DR)

## What it is

- Self Schedule Request Status Change - Tracks changes in status of request i.e.Draft > Submitted, Submitted > Approved/Rejected

## Fields

| Field                        | Description                                                                                                                      |
|:-----------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| vEssSelfScheduleStatusChange | - Self Schedule Request Status Change - Tracks changes in status of request i.e.Draft > Submitted, Submitted > Approved/Rejected |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

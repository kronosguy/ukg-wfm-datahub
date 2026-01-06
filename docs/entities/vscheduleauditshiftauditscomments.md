# vScheduleAuditShiftAuditsComments

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** scheduleAudit (CDC)

## What it is

A list of comments for the historical audits of shifts.

## Fields

| Field                             | Description                                             |
|:----------------------------------|:--------------------------------------------------------|
| vScheduleAuditShiftAuditsComments | A list of comments for the historical audits of shifts. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

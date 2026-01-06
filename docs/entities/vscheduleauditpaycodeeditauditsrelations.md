# vScheduleAuditPayCodeEditAuditsRelations

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** scheduleAudit (CDC)

## What it is

This view provides alist of objects related to scheduled pay code edits

## Fields

| Field                                    | Description                                                             |
|:-----------------------------------------|:------------------------------------------------------------------------|
| vScheduleAuditPayCodeEditAuditsRelations | This view provides alist of objects related to scheduled pay code edits |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

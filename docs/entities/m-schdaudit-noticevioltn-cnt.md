# M_SchdAudit_NoticeVioltn_Cnt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Schedule Shift Audit Notice Period Violations: Count of schedule changes where the change was recorded after specified number of hours before the scheduled shift start dtm. ("Global" pipeline setting)
shiftid_revisioniId of the audit will be populated in this column. User will have to use Count(Distinct) logic in BI tool to get this count.

## Fields

| Field                        | Type   | Description                                                                                                                                                                                              |
|:-----------------------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M_SchdAudit_NoticeVioltn_Cnt | STRING | Schedule Shift Audit Notice Period Violations: Count of schedule changes where the change was recorded after specified number of hours before the scheduled shift start dtm. ("Global" pipeline setting) |
|                              |        | shiftid_revisioniId of the audit will be populated in this column. User will have to use Count(Distinct) logic in BI tool to get this count.                                                             |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

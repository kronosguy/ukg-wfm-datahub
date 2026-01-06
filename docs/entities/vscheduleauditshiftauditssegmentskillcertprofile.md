# vScheduleAuditShiftAuditsSegmentSkillCertProfile

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** scheduleAudit (CDC)

## What it is

The list of segments of this availability by Skill Cert Profile

## Fields

| Field                                            | Description                                                     |
|:-------------------------------------------------|:----------------------------------------------------------------|
| vScheduleAuditShiftAuditsSegmentSkillCertProfile | The list of segments of this availability by Skill Cert Profile |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

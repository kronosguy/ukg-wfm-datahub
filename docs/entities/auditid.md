# auditId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Audit ID (this value can be joined to the ids in the Timecard views i.e.vTimecardPunch.punchId = vTimecardAudit.auditId, vTimecardPayCodeEdit.payCodeEditId =  vTimecardAudit.auditId, vTimecardException.exceptionId = vTimecardAudit.auditId

## Fields

| Field   | Type   | Description                                                                                                                                                                                                                                    |
|:--------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| auditId | INT64  | Audit ID (this value can be joined to the ids in the Timecard views i.e.vTimecardPunch.punchId = vTimecardAudit.auditId, vTimecardPayCodeEdit.payCodeEditId =  vTimecardAudit.auditId, vTimecardException.exceptionId = vTimecardAudit.auditId |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# M_SchdAudit_ShiftChange_Cnt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Number of shifts modified (Count of shift audit revisions where audit type = "Update" and deleted_swt = False)
shiftid_revisioniId of the audit will be populated in this column. User will have to use Count(Distinct) logic in BI tool to get this count.

## Fields

| Field                       | Type   | Description                                                                                                                                  |
|:----------------------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| M_SchdAudit_ShiftChange_Cnt | STRING | Number of shifts modified (Count of shift audit revisions where audit type = "Update" and deleted_swt = False)                               |
|                             |        | shiftid_revisioniId of the audit will be populated in this column. User will have to use Count(Distinct) logic in BI tool to get this count. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

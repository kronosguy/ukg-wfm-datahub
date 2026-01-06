# M_EmpCnt_ActPaid_Cnt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

If M_Act_Paid_Hrs > 0 THEN personId ELSE NULL. User will have to use Count(Distinct) logic in BI tool to get the employee count

## Fields

| Field                | Type   | Description                                                                                                                     |
|:---------------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------|
| M_EmpCnt_ActPaid_Cnt | INT64  | If M_Act_Paid_Hrs > 0 THEN personId ELSE NULL. User will have to use Count(Distinct) logic in BI tool to get the employee count |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

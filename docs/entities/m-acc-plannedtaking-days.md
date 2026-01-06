# M_Acc_PlannedTaking_Days

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Days scheduled to be taken or used after the current partition date. For example, vacation days that are  scheduled to be taken after current partion date, 8/22. These are considered to be planned but not yet taken.

## Fields

| Field                    | Type   | Description                                                                                                                                                                                                             |
|:-------------------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| M_Acc_PlannedTaking_Days | FLOAT  | Days scheduled to be taken or used after the current partition date. For example, vacation days that are  scheduled to be taken after current partion date, 8/22. These are considered to be planned but not yet taken. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

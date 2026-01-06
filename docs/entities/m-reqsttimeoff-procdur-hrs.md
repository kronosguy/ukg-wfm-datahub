# M_ReqstTimeOff_ProcDur_Hrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Request Process Hours (difference  between creation and completed) only includes completed request (Approved, Refused)

## Fields

| Field                      | Type   | Description                                                                                                            |
|:---------------------------|:-------|:-----------------------------------------------------------------------------------------------------------------------|
| M_ReqstTimeOff_ProcDur_Hrs | FLOAT  | Request Process Hours (difference  between creation and completed) only includes completed request (Approved, Refused) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

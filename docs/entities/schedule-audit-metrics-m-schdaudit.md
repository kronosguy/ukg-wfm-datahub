# Schedule Audit Metrics (M_SchdAudit)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Schedule Audits capture changes to scheduled shifts. (Not scheduled pay code edits)
Supported by Business Structure, Date, Person, Primary Business Structure Attributes

## Fields

| Field                                | Description                                                                          |
|:-------------------------------------|:-------------------------------------------------------------------------------------|
| Schedule Audit Metrics (M_SchdAudit) | Schedule Audits capture changes to scheduled shifts. (Not scheduled pay code edits)  |
|                                      | Supported by Business Structure, Date, Person, Primary Business Structure Attributes |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

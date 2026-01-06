# vHcaWorkUnitHyperfindProfileHF

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** hcaWorkUnitHyperfindProfile (DR)

## What it is

A set of rows with the work unit hyperfinds associated with each work unit hyperfind profile.

## Fields

| Field                          | Description                                                                                   |
|:-------------------------------|:----------------------------------------------------------------------------------------------|
| vHcaWorkUnitHyperfindProfileHF | A set of rows with the work unit hyperfinds associated with each work unit hyperfind profile. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

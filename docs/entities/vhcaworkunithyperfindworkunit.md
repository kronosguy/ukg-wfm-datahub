# vHcaWorkUnitHyperfindWorkUnit

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** hcaWorkUnitHyperfind (DR)

## What it is

A set of rows with the work units associated with each work unit hyperfind.

## Fields

| Field                         | Description                                                                 |
|:------------------------------|:----------------------------------------------------------------------------|
| vHcaWorkUnitHyperfindWorkUnit | A set of rows with the work units associated with each work unit hyperfind. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

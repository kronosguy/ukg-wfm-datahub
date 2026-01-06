# vWorkloadPlannerActualCoverage

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** workloadPlannerCoverage (DR)

## What it is

Actual Assigned and Unassigned Coverage per Workload Span

## Fields

| Field                          | Description                                               |
|:-------------------------------|:----------------------------------------------------------|
| vWorkloadPlannerActualCoverage | Actual Assigned and Unassigned Coverage per Workload Span |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

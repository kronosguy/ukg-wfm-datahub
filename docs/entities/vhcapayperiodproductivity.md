# vHcaPayperiodProductivity

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** hcaPayperiodProductivityPaid (CDC), hcaPayperiodProductivityProd (CDC)

## What it is

Pay Period Productivity Paid provides pay period work unit productivity, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts.(This is a combination of views vHcaPayperiodProductivityPaid and vHcaPayperiodProductivityProd)

## Fields

| Field                     | Description                                                                                                                                                                                                                                                                           |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vHcaPayperiodProductivity | Pay Period Productivity Paid provides pay period work unit productivity, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts.(This is a combination of views vHcaPayperiodProductivityPaid and vHcaPayperiodProductivityProd) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

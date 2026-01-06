# vHcaPayperiodProductivityProd

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** hcaPayperiodProductivityProd (CDC)

## What it is

Pay Period Productivity Productive provides pay period work unit productivity, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Fields

| Field                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vHcaPayperiodProductivityProd | Pay Period Productivity Productive provides pay period work unit productivity, regular and supplemental labor details, and fixed and variable targets compared to actual hours and amounts. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# vHcaVolumeDetail

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** hcaVolumeDetail (CDC)

## What it is

Volume Detail provides work unit totals at the procedure code level for raw and weighted volume quantities that are based on the posting and service dates. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period.

## Fields

| Field            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vHcaVolumeDetail | Volume Detail provides work unit totals at the procedure code level for raw and weighted volume quantities that are based on the posting and service dates. Historical Reload Constraint: The historical reload capability of this pipeline is limited by the pay periods defined in vHcaWorkUnitPayPeriod. Specifically, data can be reloaded for a range spanning 26 pay periods in the past up to 5 pay periods in the future relative to the current pay period. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

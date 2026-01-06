# vProjectedTotalExcludeCorrection

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** timecardMetrics (CDC)

## What it is

- Same as projectedTotal, but excludes the "Historical Corrections", represents what the totals in the past were originally.

## Fields

| Field                            | Description                                                                                                                  |
|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| vProjectedTotalExcludeCorrection | - Same as projectedTotal, but excludes the "Historical Corrections", represents what the totals in the past were originally. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

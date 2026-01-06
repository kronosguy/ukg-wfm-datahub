# Scheduled to Worked Hours Metrics (M_WaS)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Hours are based on timecard worked shift and scheduled shift coverage (not totalized hours) and therefore may differ from totalized hours due to rounding.
Supported by all attributes except Pay Code

## Fields

| Field                                     | Description                                                                                                                                                |
|:------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scheduled to Worked Hours Metrics (M_WaS) | Hours are based on timecard worked shift and scheduled shift coverage (not totalized hours) and therefore may differ from totalized hours due to rounding. |
|                                           | Supported by all attributes except Pay Code                                                                                                                |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

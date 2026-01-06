# vSmryTimecardTotalByRow

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** valTimecardTotal (DR)

## What it is

Timecard Total hours and amounts by date, personId and pay code (IA vs Data Hub Summary)

## Fields

| Field                   | Description                                                                              |
|:------------------------|:-----------------------------------------------------------------------------------------|
| vSmryTimecardTotalByRow | Timecard Total hours and amounts by date, personId and pay code (IA vs Data Hub Summary) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

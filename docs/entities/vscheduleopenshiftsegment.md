# vScheduleOpenShiftSegment

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** scheduleOpenShift (CDC)

## What it is

- Open Shift Segments (Child of scheduleOpenShift) Represents scheduled open shift segments within a shift. Excludes break segments

## Fields

| Field                     | Description                                                                                                                         |
|:--------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| vScheduleOpenShiftSegment | - Open Shift Segments (Child of scheduleOpenShift) Represents scheduled open shift segments within a shift. Excludes break segments |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

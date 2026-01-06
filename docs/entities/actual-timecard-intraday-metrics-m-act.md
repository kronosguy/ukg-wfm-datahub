# Actual Timecard Intraday Metrics (M_Act)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Actual worked coverage. All dimensions supported
Note: Known issue with actual hours from pay-to-schedule not generating actual headcounts

## Fields

| Field                                    | Description                                                                               |
|:-----------------------------------------|:------------------------------------------------------------------------------------------|
| Actual Timecard Intraday Metrics (M_Act) | Actual worked coverage. All dimensions supported                                          |
|                                          | Note: Known issue with actual hours from pay-to-schedule not generating actual headcounts |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

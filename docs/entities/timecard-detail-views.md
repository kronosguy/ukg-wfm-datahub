# Timecard Detail Views

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Detail Views for timecard data (not totals).  Includes details related to punches, pay code edits, worked shifts, and exceptions.

## Fields

| Field                 | Description                                                                                                                       |
|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| Timecard Detail Views | Detail Views for timecard data (not totals).  Includes details related to punches, pay code edits, worked shifts, and exceptions. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

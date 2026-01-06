# shiftId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The shift id (shiftId and revisionId are concatenated for the Shift Audit Counts)

## Fields

| Field   | Type   | Description                                                                       |
|:--------|:-------|:----------------------------------------------------------------------------------|
| shiftId | INT64  | The shift id (shiftId and revisionId are concatenated for the Shift Audit Counts) |
| shiftId | INT64  | Shift ID                                                                          |
| shiftId | INT64  | The shift ID                                                                      |
| shiftId | INT64  | The shift id (shiftId is used for the Shift Audit Counts)                         |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

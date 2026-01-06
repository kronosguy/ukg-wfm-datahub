# revisionId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The id of the this revision/audit record.

## Fields

| Field      | Type   | Description                                                                                                    |
|:-----------|:-------|:---------------------------------------------------------------------------------------------------------------|
| revisionId | INT64  | The id of the this revision/audit record.                                                                      |
| revisionId | INT64  | The id of the this revision/audit record. (shiftId and revisionId are concatenated for the Shift Audit Counts) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

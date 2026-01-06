# payCodeEditsId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The ID for the relationship between the pay code edit and schedule.

## Fields

| Field          | Type   | Description                                                         |
|:---------------|:-------|:--------------------------------------------------------------------|
| payCodeEditsId | INT64  | The ID for the relationship between the pay code edit and schedule. |
| payCodeEditsId | INT64  | The pay code edit ID                                                |
| payCodeEditsId | INT64  | Pay code edit ID                                                    |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

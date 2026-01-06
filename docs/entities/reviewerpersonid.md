# reviewerPersonId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The employee ID of a reviewer, which is an ID that uniquely identifies an employee. This is not a person number.

## Fields

| Field            | Type   | Description                                                                                                      |
|:-----------------|:-------|:-----------------------------------------------------------------------------------------------------------------|
| reviewerPersonId | INT64  | The employee ID of a reviewer, which is an ID that uniquely identifies an employee. This is not a person number. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

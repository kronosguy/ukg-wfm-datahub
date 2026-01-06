# auditType

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The type of this revision.

## Fields

| Field     | Type   | Description                                                          |
|:----------|:-------|:---------------------------------------------------------------------|
| auditType | STRING | The type of this revision.                                           |
| auditType | STRING | The type of Audit Insert or Update                                   |
| auditType | STRING | The type of timecard entity that was edited i.e. Punch, paycode edit |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

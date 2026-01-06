# comment

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Schedule Audit comment

## Fields

| Field   | Type   | Description                                 |
|:--------|:-------|:--------------------------------------------|
| comment | STRING | Schedule Audit comment                      |
| comment | STRING | The comment attached to this audit          |
| comment | STRING | Schedule leave edit comment                 |
| comment | STRING | Schedule open shift comment                 |
| comment | STRING | Paycode edit comment                        |
| comment | STRING | The name of the comment and attached notes. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

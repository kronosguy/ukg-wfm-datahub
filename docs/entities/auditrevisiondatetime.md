# auditRevisionDatetime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The date and time the audit was made (i.e. if this was a punch it would be the punch date time or sign-off/approval the date time it was made)

## Fields

| Field                 | Type     | Description                                                                                                                                    |
|:----------------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| auditRevisionDatetime | DATETIME | The date and time the audit was made (i.e. if this was a punch it would be the punch date time or sign-off/approval the date time it was made) |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

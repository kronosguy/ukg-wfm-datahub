# Person_PrimaryLaborEntryName1

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Primary Labor Entry Name 1

## Fields

| Field                         | Type   | Description                |
|:------------------------------|:-------|:---------------------------|
| Person_PrimaryLaborEntryName1 | STRING | Primary Labor Entry Name 1 |
| Person_PrimaryLaborEntryName1 | STRING | Primary Labor Category     |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

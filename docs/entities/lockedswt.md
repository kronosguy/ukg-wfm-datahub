# lockedSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not a pay code edit is locked.

## Fields

| Field     | Type    | Description                                                      |
|:----------|:--------|:-----------------------------------------------------------------|
| lockedSwt | BOOLEAN | A Boolean indicator of whether or not a pay code edit is locked. |
| lockedSwt | BOOLEAN | A Boolean indicator of whether or not the shift is locked.       |
| lockedSwt | BOOLEAN | The Boolean flag  that the holiday is locked                     |
| lockedSwt | BOOLEAN | The leave edit locked status.                                    |
| lockedSwt | BOOLEAN | A Boolean indicator of whether or not a shift is locked.         |
| lockedSwt | BOOLEAN | A Boolean indicator of whether or not a pay code edit is locked  |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# stp_Last8Weeks (boolean)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Boolean indicator where or not this is Last 8 Weeks

## Fields

| Field                    | Description                                         |
|:-------------------------|:----------------------------------------------------|
| stp_Last8Weeks (boolean) | Boolean indicator where or not this is Last 8 Weeks |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

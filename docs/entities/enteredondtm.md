# enteredOnDtm

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The date and time stamp for when this punch transaction was entered through the API.

## Fields

| Field        | Type     | Description                                                                          |
|:-------------|:---------|:-------------------------------------------------------------------------------------|
| enteredOnDtm | DATETIME | The date and time stamp for when this punch transaction was entered through the API. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

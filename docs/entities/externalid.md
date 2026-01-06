# externalId

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The external ID of an org map node. If no value is passed during an update, the previous value remains in effect and is taken from the revision with the most recent effective date.

## Fields

| Field      | Type   | Description                                                                                                                                                                          |
|:-----------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| externalId | STRING | The external ID of an org map node. If no value is passed during an update, the previous value remains in effect and is taken from the revision with the most recent effective date. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# activeSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Boolean flag indicating that the relation to the shift's source is active.

## Fields

| Field     | Type    | Description                                                                |
|:----------|:--------|:---------------------------------------------------------------------------|
| activeSwt | BOOLEAN | Boolean flag indicating that the relation to the shift's source is active. |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not this audit relation is active        |
| activeSwt | BOOLEAN | Whether the comment is active or not.                                      |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor forecast limit is active.    |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor standard is active.          |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor task is active.              |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a labor task group is active.        |
| activeSwt | BOOL    | A Boolean indicator of whether or not Hours of Operation object is active. |
| activeSwt | BOOL    | A Boolean indicator of whether or not the override is active               |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not a generic location is active.        |
| activeSwt | BOOLEAN | License active switch                                                      |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not the comment is active                |
| activeSwt | BOOLEAN | A Boolean indicator of whether or not the shift is active                  |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

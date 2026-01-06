# lastRevision

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Is this the last revision of this org node. - True/False

## Fields

| Field        | Type    | Description                                                                     |
|:-------------|:--------|:--------------------------------------------------------------------------------|
| lastRevision | BOOLEAN | Is this the last revision of this org node. - True/False                        |
| lastRevision | BOOLEAN | A Boolean indicator of whether or not this is the generic job's first revision. |
| lastRevision | BOOLEAN | A Boolean indicator of whether or not this is a node type's last revision.      |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# vEssShiftCover

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** essShiftCover (DR)

## What it is

- This operation returns one or more shift cover requests matching specified search criteria corresponding to a set of cover request IDs, managers, or current state

## Fields

| Field          | Description                                                                                                                                                          |
|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vEssShiftCover | - This operation returns one or more shift cover requests matching specified search criteria corresponding to a set of cover request IDs, managers, or current state |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

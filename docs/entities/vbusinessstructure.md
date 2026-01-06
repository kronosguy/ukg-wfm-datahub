# vBusinessStructure

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** getBusinessStructure (DR)

## What it is

- One Row for every unique path in the business structure, only contains completely end dated(does not have a current version), currently effective, or future(where there is no current version)

NOTE: If new Location Types are added,  the orgBreak% columns need to be mapped in the Admin Panel.

## Fields

| Field              | Description                                                                                                                                                                                       |
|:-------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vBusinessStructure | - One Row for every unique path in the business structure, only contains completely end dated(does not have a current version), currently effective, or future(where there is no current version) |
|                    |                                                                                                                                                                                                   |
|                    | NOTE: If new Location Types are added,  the orgBreak% columns need to be mapped in the Admin Panel.                                                                                               |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

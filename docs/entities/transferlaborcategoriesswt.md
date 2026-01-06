# transferLaborCategoriesSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not there is a labor category transfer  for this shift segment.

## Fields

| Field                      | Type    | Description                                                                                       |
|:---------------------------|:--------|:--------------------------------------------------------------------------------------------------|
| transferLaborCategoriesSwt | BOOLEAN | A Boolean indicator of whether or not there is a labor category transfer  for this shift segment. |
| transferLaborCategoriesSwt | BOOLEAN | A Boolean indicator of whether or not the labor category is a transfer.                           |
| transferLaborCategoriesSwt | BOOLEAN | A Boolean indicator of whether or not there is a labor categry transfer                           |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

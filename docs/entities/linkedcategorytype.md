# linkedCategoryType

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals.

## Fields

| Field              | Type   | Description                                                                                                                                                          |
|:-------------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals  |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

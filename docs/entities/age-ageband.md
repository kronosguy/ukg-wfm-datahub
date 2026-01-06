# Age_ageBand

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Age band

## Fields

| Field       | Type   | Description                                                                                                                                                                                                                                                     |
|:------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Age_ageBand | STRING | Age band                                                                                                                                                                                                                                                        |
| Age_ageBand |        | Employee Age Band Attribute - Name of the age-based grouping based on employee age on the date transactions were recorded. Possible values are: 13 and Under, 14 and 15, 16 and 17, 18 to 20, 21 to 35, 36 to 45, 46 to 55, 56 to 65, 66 and Older, Unknown Age |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

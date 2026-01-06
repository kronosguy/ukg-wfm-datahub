# distributionType

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The type of labor standard distribution if distributed by traffic pattern. Valid values include POA and HOO. POA corresponds to 'compressed' and HOO to 'truncate'. This setting allows you to compress or truncate traffic pattern distribution.

## Fields

| Field            | Type   | Description                                                                                                                                                                                                                                       |
|:-----------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| distributionType | STRING | The type of labor standard distribution if distributed by traffic pattern. Valid values include POA and HOO. POA corresponds to 'compressed' and HOO to 'truncate'. This setting allows you to compress or truncate traffic pattern distribution. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# currentBalVestedHrs

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Vested Balance Hours as of the partitionDate. In this example if the partiotionDate is 8/22,  Vested hours as of 8/22.

## Fields

| Field               | Type   | Description                                                                                                            |
|:--------------------|:-------|:-----------------------------------------------------------------------------------------------------------------------|
| currentBalVestedHrs | FLOAT  | Vested Balance Hours as of the partitionDate. In this example if the partiotionDate is 8/22,  Vested hours as of 8/22. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

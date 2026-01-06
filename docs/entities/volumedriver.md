# volumeDriver

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The ID of the Volume Driver.

## Fields

| Field        | Type   | Description                                                                                              |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------|
| volumeDriver | STRING | The ID of the Volume Driver.                                                                             |
| volumeDriver | STRING | Volume driver amount is assigned to (Sales, traffic, units, etc)                                         |
| volumeDriver | STRING | Volume Driver Name                                                                                       |
| volumeDriver | STRING | The Name of  the Volume Driver. (derived from volumeDrivers.volumeDriver for slowly changing dimensions) |
| volumeDriver | STRING | The volume driver the amount is associated with. Examples: sales, units, traffic                         |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

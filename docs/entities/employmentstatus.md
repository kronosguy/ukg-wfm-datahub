# employmentStatus

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Represents the start date of a defined period during where different positions can have different status

## Fields

| Field            | Type   | Description                                                                                              |
|:-----------------|:-------|:---------------------------------------------------------------------------------------------------------|
| employmentStatus | STRING | Represents the start date of a defined period during where different positions can have different status |
| employmentStatus | STRING | Employment status of employee: Active, Inactive, Terminated                                              |
| employmentStatus | STRING | Employment status - active, inactive, terminated                                                         |
| employmentStatus | STRING | Employment status                                                                                        |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

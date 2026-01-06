# dataSource

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A reference to the data source, if one exists. Normally, this indicates that the context object came from a different source, such as a clock, device, or an external data source such as an import or interface.

## Fields

| Field      | Type   | Description                                                                                                                                                                                                                                                                |
|:-----------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dataSource | STRING | A reference to the data source, if one exists. Normally, this indicates that the context object came from a different source, such as a clock, device, or an external data source such as an import or interface.                                                          |
| dataSource | STRING | A reference to the data source, if one exists, related to a historical correction.                                                                                                                                                                                         |
| dataSource | STRING | A reference to the data source, if one exists. Normally, this indicates that the punch came from a different source, such as a clock, device, or an external data source such as an import or interface. Note: This can be name of the employee/manager who made the punch |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

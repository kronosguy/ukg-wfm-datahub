# applicationType

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The type indicating the way labor is distributed throughout the day. ABSOLUTE: labor period times are specific. HOO: labor periods are defined by the hours of operation for the department or site. HOO_CLOSE: start labor after the store closes. HOO_OPEN: start labor after the store opens.

## Fields

| Field           | Type   | Description                                                                                                                                                                                                                                                                                      |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| applicationType | STRING | The type indicating the way labor is distributed throughout the day. ABSOLUTE: labor period times are specific. HOO: labor periods are defined by the hours of operation for the department or site. HOO_CLOSE: start labor after the store closes. HOO_OPEN: start labor after the store opens. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

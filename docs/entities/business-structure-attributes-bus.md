# Business Structure Attributes (Bus)

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Refer to data definitions for the Business Structure view in the Detail dataset

## Fields

| Field                               | Description                                                                     |
|:------------------------------------|:--------------------------------------------------------------------------------|
| Business Structure Attributes (Bus) | Refer to data definitions for the Business Structure view in the Detail dataset |
| Business Structure Attributes (Bus) |                                                                                 |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

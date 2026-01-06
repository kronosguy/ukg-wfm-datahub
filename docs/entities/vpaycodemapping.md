# vPayCodeMapping

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** Sourced from Config Portal (DR)

## What it is

- Imported Mapping of paycodes to pay categories.  Used in summary level Views.  Must be imported using the standard process and requires it is kept up to date when new paycodes are added.

## Fields

| Field           | Description                                                                                                                                                                                  |
|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vPayCodeMapping | - Imported Mapping of paycodes to pay categories.  Used in summary level Views.  Must be imported using the standard process and requires it is kept up to date when new paycodes are added. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

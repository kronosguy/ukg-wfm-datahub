# vEssOpenShift

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** essOpenShift (DR)

## What it is

- This resource allows a manager to retrieve open shift requests. Employees can request to select their own schedule from the times that are available when the request period is open.

## Fields

| Field         | Description                                                                                                                                                                             |
|:--------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vEssOpenShift | - This resource allows a manager to retrieve open shift requests. Employees can request to select their own schedule from the times that are available when the request period is open. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

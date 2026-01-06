# vEssAvailability

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** essAvailability (DR)

## What it is

- This resource allows you to retrieve availability requests, which allow managers to handle requests made by employees to temporarily override the times when they are available to work. Note: This does not include Availability Pattern Requests

## Fields

| Field            | Description                                                                                                                                                                                                                                          |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vEssAvailability | - This resource allows you to retrieve availability requests, which allow managers to handle requests made by employees to temporarily override the times when they are available to work. Note: This does not include Availability Pattern Requests |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

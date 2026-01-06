# vTrafficPatternForecast

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** trafficPatternForecast (DR)

## What it is

Traffic patterns are the basis for allocating day level volume forecast amount to 15 minute intra day allocations.

## Fields

| Field                   | Description                                                                                                        |
|:------------------------|:-------------------------------------------------------------------------------------------------------------------|
| vTrafficPatternForecast | Traffic patterns are the basis for allocating day level volume forecast amount to 15 minute intra day allocations. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# vGenericLocations

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

- Generic Locations can be a physical location (Operating Room or Mail Room) or a logistical unit that is not a physical location (Support, Administration, a Home Care Unit). Note: for Simplified Business Structure Customers Only

## Fields

| Field             | Description                                                                                                                                                                                                                           |
|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vGenericLocations | - Generic Locations can be a physical location (Operating Room or Mail Room) or a logistical unit that is not a physical location (Support, Administration, a Home Care Unit). Note: for Simplified Business Structure Customers Only |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

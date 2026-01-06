# vActualVolumeIntra

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** actualVolume (DR)

## What it is

Use this view instead of the view since this will display at the lowest business structure node
Actual Volume by Site (eventually will be at the Category Level) (Retail Forecasting) 15 Min Grain Note: Includes only currently active orgs

## Fields

| Field              | Description                                                                                                                                  |
|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| vActualVolumeIntra | Use this view instead of the view since this will display at the lowest business structure node                                              |
|                    | Actual Volume by Site (eventually will be at the Category Level) (Retail Forecasting) 15 Min Grain Note: Includes only currently active orgs |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

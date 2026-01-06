# transferCostCenterSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not there is a transfer cost center for this shift segment.

## Fields

| Field                 | Type    | Description                                                                                   |
|:----------------------|:--------|:----------------------------------------------------------------------------------------------|
| transferCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not there is a transfer cost center for this shift segment. |
| transferCostCenterSwt | BOOLEAN | A Boolean indicator of whether or not the cost center is a transfer.                          |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

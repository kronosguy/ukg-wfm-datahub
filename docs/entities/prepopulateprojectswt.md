# prepopulateProjectSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A Boolean indicator of whether or not project prepopulation is enabled for this effective pay rule. When this option is enabled, a project view timecard is prepopulated with the transfer accounts that were used in the previous pay period.

## Fields

| Field                 | Type    | Description                                                                                                                                                                                                                                    |
|:----------------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| prepopulateProjectSwt | BOOLEAN | A Boolean indicator of whether or not project prepopulation is enabled for this effective pay rule. When this option is enabled, a project view timecard is prepopulated with the transfer accounts that were used in the previous pay period. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

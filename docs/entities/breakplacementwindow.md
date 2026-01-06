# breakPlacementWindow

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A window (in minutes) on each side of the day divide. Any gap in labor with a start day and end day that falls within this window and meets the maximum break duration is ignored. For example, if you define the window to be 60 minutes, then the window extends from one hour before the day divide to one hour after the day divide. The numerical value of this window represents minutes and can be 0 to 360. The value must be a multiple of 15 and greater than or equal to the maximum break duration.

## Fields

| Field                | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:---------------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| breakPlacementWindow | INT64  | A window (in minutes) on each side of the day divide. Any gap in labor with a start day and end day that falls within this window and meets the maximum break duration is ignored. For example, if you define the window to be 60 minutes, then the window extends from one hour before the day divide to one hour after the day divide. The numerical value of this window represents minutes and can be 0 to 360. The value must be a multiple of 15 and greater than or equal to the maximum break duration. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

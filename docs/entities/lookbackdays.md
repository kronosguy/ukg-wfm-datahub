# lookBackDays

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The number of days to look back. For the VARIABLE_CUSTOM type, valid values are 0, 1, 2, 3, 4, 5, 6, and 7. For the VARIABLE_VOLUME type, valid values are 0, 1, 2, and 3.

## Fields

| Field        | Type   | Description                                                                                                                                                                |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| lookBackDays | INT64  | The number of days to look back. For the VARIABLE_CUSTOM type, valid values are 0, 1, 2, 3, 4, 5, 6, and 7. For the VARIABLE_VOLUME type, valid values are 0, 1, 2, and 3. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

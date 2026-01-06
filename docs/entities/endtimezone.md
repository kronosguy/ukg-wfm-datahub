# endTimezone

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The end timezone where the worked shift was entered. Normally, this is the default or home timezone for the employee, but the worked shift can include a different timezone as necessary.

## Fields

| Field       | Type   | Description                                                                                                                                                                               |
|:------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| endTimezone | INT64  | The end timezone where the worked shift was entered. Normally, this is the default or home timezone for the employee, but the worked shift can include a different timezone as necessary. |
| endTimezone | STRING | The end timezone where the worked span was entered. Normally, this is the default or home timezone for the employee, but the worked span can include a different timezone as necessary.   |
| endTimezone | STRING | End timezone where the worked span was entered. Normally, this is the default or home timezone for the employee, but the worked span can include a different timezone as necessary.       |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

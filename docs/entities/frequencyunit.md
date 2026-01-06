# frequencyUnit

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The frequency interval.
The Frequency Interval i.e. PER_PERIOD PER_HOUR PER_DAY PER_WEEK

## Fields

| Field         | Type   | Description                                                                        |
|:--------------|:-------|:-----------------------------------------------------------------------------------|
| frequencyUnit | STRING | The frequency interval.                                                            |
|               |        | The Frequency Interval i.e. PER_PERIOD PER_HOUR PER_DAY PER_WEEK                   |
| frequencyUnit | STRING | The unit of time representing frequency i.e. .PER_PERIOD PER_HOUR PER_DAY PER_WEEK |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

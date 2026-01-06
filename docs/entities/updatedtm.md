# updateDtm

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The UTC date/time stamp of when the row was inserted or updated in BigQuery

## Fields

| Field     | Type     | Description                                                                        |
|:----------|:---------|:-----------------------------------------------------------------------------------|
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery        |
| updateDtm | DATETIME |                                                                                    |
| updateDtm | DATETIME | The date and time an update to a record was loaded in Data Hub Views.              |
| updateDtm |          |                                                                                    |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery          |
| updateDtm | DATETIME | Represents apply date of transaction - use to join to date dimension               |
| updateDtm | DATETIME | pipeline update date time                                                          |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted or updated in Data Hub - BigQuery |
| updateDtm | DATETIME | Date time row was updated.                                                         |
| updateDtm | STRING   | The UTC date/time stamp of when the row was inserted or updated in BigQuery        |
| updateDtm | DATE     | pipeline update date time                                                          |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

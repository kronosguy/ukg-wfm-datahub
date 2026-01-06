# description

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Description of the custom date

## Fields

| Field       | Type   | Description                                                                                                        |
|:------------|:-------|:-------------------------------------------------------------------------------------------------------------------|
| description | STRING | Description of the custom date                                                                                     |
| description | STRING | The description of the device.                                                                                     |
| description | STRING | Describes the hours of operation                                                                                   |
| description | STRING | Hours of operation override description                                                                            |
| description | STRING | Hours of operation description                                                                                     |
| description | STRING | Description of the Org Node as entered in WFD (single value)                                                       |
| description | STRING | The description of a generic job.Despite location behavior if null passed on update then empty string will be set. |
| description | STRING | Location Type Description                                                                                          |
| description | STRING | Pay code description                                                                                               |
| description | STRING | Custom date description                                                                                            |
| description | STRING | Description of the punch                                                                                           |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

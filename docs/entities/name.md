# name

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

name of the particular employment term

## Fields

| Field   | Type   | Description                                           |
|:--------|:-------|:------------------------------------------------------|
| name    | STRING | name of the particular employment term                |
| name    | STRING | Name of the HR position code                          |
| name    | STRING | name of the particular schedule group                 |
| name    | STRING | Name of the coveage span                              |
| name    | STRING | Name of custom driver                                 |
| name    | STRING | Name of hours operation object                        |
| name    | STRING | Hours of operation override name                      |
| name    | STRING | Name of the Org Node as entered in WFD (single value) |
| name    | STRING | The short name of a generic job.                      |
| name    | STRING | The short name of a generic location.                 |
| name    | STRING | Location Type Name                                    |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

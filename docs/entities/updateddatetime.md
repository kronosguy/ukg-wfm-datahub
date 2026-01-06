# updatedDateTime

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

The last updated time of a generic job.

## Fields

| Field           | Type     | Description                                                                                                         |
|:----------------|:---------|:--------------------------------------------------------------------------------------------------------------------|
| updatedDateTime | DATETIME | The last updated time of a generic job.                                                                             |
| updatedDateTime | DATETIME | The date and time of the most recent update to a node type in ISO_LOCAL_DATE_TIME format (yyyy-mm-ddThh:mm:ss.sss). |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

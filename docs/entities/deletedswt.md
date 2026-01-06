# deletedSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

Shift deleted switch

## Fields

| Field      | Type    | Description                                                                                                            |
|:-----------|:--------|:-----------------------------------------------------------------------------------------------------------------------|
| deletedSwt | BOOLEAN | Shift deleted switch                                                                                                   |
| deletedSwt | BOOLEAN | A Boolean indicator of whether or not the shift is deleted.                                                            |
| deletedSwt | BOOLEAN | Indicates deleted.                                                                                                     |
| deletedSwt | BOOLEAN | Boolean indicator of whether or not the availability is deleted.                                                       |
| deletedSwt | BOOLEAN | The Boolean flag indicating the day lock deleted status (read-only).                                                   |
| deletedSwt | BOOLEAN | this value is always null/blank deleted open shifts no longer appear once deleted                                      |
| deletedSwt | BOOLEAN | A Boolean indicator of whether or not the pay code edit is deleted                                                     |
| deletedSwt | BOOLEAN | A Boolean indicator of whether or not the shift is deleted. ** Do Not Use this value is not available or inaccurate ** |
| deletedSwt | BOOLEAN | True if the job was posted and subsequently unposted                                                                   |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

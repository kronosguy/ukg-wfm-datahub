# postedNotifiedSwt

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

A boolean indicator of whether or not the  employee has received notification pay code edit

## Fields

| Field             | Type    | Description                                                                                 |
|:------------------|:--------|:--------------------------------------------------------------------------------------------|
| postedNotifiedSwt | BOOLEAN | A boolean indicator of whether or not the  employee has received notification pay code edit |
| postedNotifiedSwt | BOOLEAN | A Boolean indicator of whether or not the employee has been notified of the posted shift.   |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

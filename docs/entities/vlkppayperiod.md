# vLkpPayPeriod

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** getPayPeriod (DR)

## What it is

INTERNAL USE ONLY use dimPayPeriod in Summary Dataset
Contains payperiod data generated from transactional data with 5 pay periods in the future and 15 pay periods in the past.
This data is available in both lkpPayPeriod in the detail dataset and  dimPayPeriod in the summary dataset.

## Fields

| Field         | Description                                                                                                                |
|:--------------|:---------------------------------------------------------------------------------------------------------------------------|
| vLkpPayPeriod | INTERNAL USE ONLY use dimPayPeriod in Summary Dataset                                                                      |
|               | Contains payperiod data generated from transactional data with 5 pay periods in the future and 15 pay periods in the past. |
|               | This data is available in both lkpPayPeriod in the detail dataset and  dimPayPeriod in the summary dataset.                |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

# vAccrualBalanceRptgPerdCurr

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

**Pipeline:** accrualBalance (DR)

## What it is

This view provides the balances for each accrual code at the beginning of the reporting span , end of the reporting span  and prior to beginning of the reporting span.  There will be one record per accrualCode for the selected duration.If there is more than 1 reporting span in the duration, the reporting span which includes the current date is selected.

## Fields

| Field                       | Description                                                                                                                                                                                                                                                                                                                                                         |
|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vAccrualBalanceRptgPerdCurr | This view provides the balances for each accrual code at the beginning of the reporting span , end of the reporting span  and prior to beginning of the reporting span.  There will be one record per accrualCode for the selected duration.If there is more than 1 reporting span in the duration, the reporting span which includes the current date is selected. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

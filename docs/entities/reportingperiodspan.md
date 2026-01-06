# reportingPeriodSpan

> Auto-generated from a Data Dictionary workbook. Output is public-safe by default.

## What it is

This is what is displayed as the "Reporting Period" in WFD. Usually begining to end of the year which contains the date for which we have extracted the data. In this example where we ran the API for 8/16/22-8/22/22 , it is 1/1/22-12/31/22 Note : Reporting span is an attribute of an accrual code and so could different for different accrual codes.

## Fields

| Field               | Type   | Description                                                                                                                                                                                                                                                                                                                                                 |
|:--------------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| reportingPeriodSpan | STRING | This is what is displayed as the "Reporting Period" in WFD. Usually begining to end of the year which contains the date for which we have extracted the data. In this example where we ran the API for 8/16/22-8/22/22 , it is 1/1/22-12/31/22 Note : Reporting span is an attribute of an accrual code and so could different for different accrual codes. |

## How to use it

- Confirm the **grain** (what one row represents) before joining.
- Join using **IDs/keys**, not labels.
- Apply **partition/date filters** early (BigQuery cost control).
- Validate with a small reference sample before publishing dashboards.

## Gotchas

- If this entity participates in many-to-many joins, document the safe join path here.
- If attributes are “current only,” document how to handle historical reporting here.

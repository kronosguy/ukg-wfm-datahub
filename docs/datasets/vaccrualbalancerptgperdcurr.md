# vAccrualBalanceRptgPerdCurr

**Group:** Detail Dataset → Accrual Detail Views

This view provides the balances for each accrual code at the beginning of the reporting span , end of the reporting span  and prior to beginning of the reporting span.  There will be one record per accrualCode for the selected duration.If there is more than 1 reporting span in the duration, the reporting span which includes the current date is selected.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAccrualBalanceRptgPerdCurr |
| Unique Identifier | personId,accrualCodeId,reportingPeriodSpan |
| Source Pipeline | accrualBalance (DR) |

## Columns

**Column count:** 28

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Person Identifier |  |  |
| accrualCodeId | INT64 | Accrual Code Identifier |  |  |
| currencyCode | STRING | Currency code for amounts i.e. USD, GBP |  |  |
| reportingPeriodSpan | STRING | This is what is displayed as the "Reporting Period" in WFD. Usually begining to end of the year which contains the date for which we have extracted the data. In this example where we ran the API for 8/16/22-8/22/22 , it is 1/1/22-12/31/22 Note : Reporting span is an attribute of an accrual code and so could different for different accrual codes. |  |  |
| reportingSpanStart | DATE | Start of the reporting span |  |  |
| reportingSpanEnd | DATE | End of the reporting span |  |  |
| openingBalDate | DATE | Start Date of the reporting Span |  |  |
| openingBalVestedDays | FLOAT | Vested days as of the opening balance date |  |  |
| openingBalVestedHrs | FLOAT | Vested Hours as of the opening balance date |  |  |
| openingBalVestedAmt | FLOAT | Vested money amount as of the opening balance date |  |  |
| openingBalProbationDays | FLOAT | Probation days as of the opening balance date |  |  |
| openingBalProbationHrs | FLOAT | Probation hours as of the opening balance date |  |  |
| openingBalProbationAmt | FLOAT | Probation money amount as of the opening balance date |  |  |
| endingBalDate | DATE | End Date of the reporting Span |  |  |
| endingBalVestedDays | FLOAT | Vested days as of ending Balance Date |  |  |
| endingBalVestedHrs | FLOAT | Vested Hours as of ending Balance Date |  |  |
| endingBalVestedAmt | FLOAT | Vested money amount as of ending Balance Date |  |  |
| endingBalProbationDays | FLOAT | Probation days as of as of ending Balance Date |  |  |
| endingBalProbationHrs | FLOAT | Probation hours as of as of ending Balance Date |  |  |
| endingBalProbationAmt | FLOAT | Probation money amount as of ending Balance Date |  |  |
| priorEndingBalDate | DATE | The day before the reporting Span Start Date |  |  |
| priorEndingBalVestedDays | FLOAT | Vested days as of prior ending balance date |  |  |
| priorEndingBalVestedHrs | FLOAT | Vested Hours as of prior ending balance date |  |  |
| priorEndingBalVestedAmt | FLOAT | Vested money amount as of prior ending balance date |  |  |
| priorEndingBalProbationDays | FLOAT | Probation days as of prior ending balance date |  |  |
| priorEndingBalProbationHrs | FLOAT | Probation hours as of prior ending balance date |  |  |
| priorEndingBalProbationAmt | FLOAT | Probation money amount as of prior ending balance date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

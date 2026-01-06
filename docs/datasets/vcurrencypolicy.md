# vCurrencyPolicy

**Group:** Detail Dataset → Employee Self Service Detail Views

This view contains one or more currency policies as configured in Dimensions

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vCurrencyPolicy |
| Unique Identifier | calendarDate,currencyId |
| Source Pipeline | getCurrencyPolicy (DR) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| calendarDate | DATE | The effective date of the currency exchange rate.  There is one row per day betwene the effective and expiration date of the currency exchnange |  |  |
| currencyId | INT64 | The ID of a currency. |  |  |
| currencyCode | STRING | The three digit ISO currency code. |  |  |
| exchangeRate | FLOAT | The initial or default exchange rate of a currency policy. |  |  |
| baseCurrencySwt | BOOLEAN | A Boolean indicator of whether or not a currency is the base currency. |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |

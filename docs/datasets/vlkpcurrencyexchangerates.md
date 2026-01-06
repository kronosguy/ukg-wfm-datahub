# vLkpCurrencyExchangeRates

**Group:** Detail Dataset → Multicurrency Views

Stores the source (from) to destination (to) exchange rates for calculations in materilization process

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLkpCurrencyExchangeRates |
| Unique Identifier | partitionDate,fromCurrencyId,toCurrencyId |
| Source Pipeline | getCurrencyPolicy (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | The effective date of the currency exchange rate.  There is one row per day betwene the effective and expiration date of the currency exchnange |  |  |
| fromCurrencyId | INT64 | Source ID of a currency |  |  |
| fromCurrencyCode | STRING | Source three digit ISO currency code. |  |  |
| toCurrencyId | INT64 | Destitnation ID of a currency |  |  |
| toCurrencyCode | STRING | Destination three digit ISO currency code. |  |  |
| rate | FLOAT | The exchange rate calclulator used to multiply to the source to get destinantion value |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |

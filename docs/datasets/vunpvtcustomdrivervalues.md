# vUnpvtCustomDriverValues

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- Unpivioted version for the first 25 custom drivers.  Uses the Custom Driver Mapping the the Vision Admin Website.  This is based on  vCustomDriverValues

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtCustomDriverValues |
| Unique Identifier | partitionDate,orgId |
| Source Pipeline |  |

## Columns

**Column count:** 31

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| currency | STRING | Curency Type |  |  |
| currencyId | INT64 | Currency ID |  |  |
| amtCstmDrvr_1 | FLOAT64 | Custom Driver 1 |  |  |
| amtCstmDrvr_2 | FLOAT64 | Custom Driver 2 |  |  |
| amtCstmDrvr_3 | FLOAT64 | Custom Driver 3 |  |  |
| amtCstmDrvr_4 | FLOAT64 | Custom Driver 4 |  |  |
| amtCstmDrvr_5 | FLOAT64 | Custom Driver 5 |  |  |
| amtCstmDrvr_6 | FLOAT64 | Custom Driver 6 |  |  |
| amtCstmDrvr_7 | FLOAT64 | Custom Driver 7 |  |  |
| amtCstmDrvr_8 | FLOAT64 | Custom Driver 8 |  |  |
| amtCstmDrvr_9 | FLOAT64 | Custom Driver 9 |  |  |
| amtCstmDrvr_10 | FLOAT64 | Custom Driver 10 |  |  |
| amtCstmDrvr_11 | FLOAT64 | Custom Driver 11 |  |  |
| amtCstmDrvr_12 | FLOAT64 | Custom Driver 12 |  |  |
| amtCstmDrvr_13 | FLOAT64 | Custom Driver 13 |  |  |
| amtCstmDrvr_14 | FLOAT64 | Custom Driver 14 |  |  |
| amtCstmDrvr_15 | FLOAT64 | Custom Driver 15 |  |  |
| amtCstmDrvr_16 | FLOAT64 | Custom Driver 16 |  |  |
| amtCstmDrvr_17 | FLOAT64 | Custom Driver 17 |  |  |
| amtCstmDrvr_18 | FLOAT64 | Custom Driver 18 |  |  |
| amtCstmDrvr_19 | FLOAT64 | Custom Driver 19 |  |  |
| amtCstmDrvr_20 | FLOAT64 | Custom Driver 20 |  |  |
| amtCstmDrvr_21 | FLOAT64 | Custom Driver 21 |  |  |
| amtCstmDrvr_22 | FLOAT64 | Custom Driver 22 |  |  |
| amtCstmDrvr_23 | FLOAT64 | Custom Driver 23 |  |  |
| amtCstmDrvr_24 | FLOAT64 | Custom Driver 24 |  |  |
| amtCstmDrvr_25 | FLOAT64 | Custom Driver 25 |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |

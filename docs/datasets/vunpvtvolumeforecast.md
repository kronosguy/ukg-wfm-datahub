# vUnpvtVolumeForecast

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtVolumeForecast |
| Unique Identifier | partitionDate,orgId,currencyId |
| Source Pipeline |  |

## Columns

**Column count:** 58

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| currency | STRING | Currency |  |  |
| currencyId | INT64 | Currency ID |  |  |
| volFcstAdjDrvr_1 | FLOAT64 | Volume Forecast Adjustment Driver 1 |  |  |
| volFcstAdjDrvr_2 | FLOAT64 | Volume Forecast Adjustment Driver 2 |  |  |
| volFcstAdjDrvr_3 | FLOAT64 | Volume Forecast Adjustment Driver 3 |  |  |
| volFcstAdjDrvr_4 | FLOAT64 | Volume Forecast Adjustment Driver 4 |  |  |
| volFcstAdjDrvr_5 | FLOAT64 | Volume Forecast Adjustment Driver 5 |  |  |
| volFcstAdjDrvr_6 | FLOAT64 | Volume Forecast Adjustment Driver 6 |  |  |
| volFcstAdjDrvr_7 | FLOAT64 | Volume Forecast Adjustment Driver 7 |  |  |
| volFcstAdjDrvr_8 | FLOAT64 | Volume Forecast Adjustment Driver 8 |  |  |
| volFcstAdjDrvr_9 | FLOAT64 | Volume Forecast Adjustment Driver 9 |  |  |
| volFcstAdjDrvr_10 | FLOAT64 | Volume Forecast Adjustment Driver 10 |  |  |
| volFcstAdjDrvr_11 | FLOAT64 | Volume Forecast Adjustment Driver 11 |  |  |
| volFcstAdjDrvr_12 | FLOAT64 | Volume Forecast Adjustment Driver 12 |  |  |
| volFcstAdjDrvr_13 | FLOAT64 | Volume Forecast Adjustment Driver 13 |  |  |
| volFcstAdjDrvr_14 | FLOAT64 | Volume Forecast Adjustment Driver 14 |  |  |
| volFcstAdjDrvr_15 | FLOAT64 | Volume Forecast Adjustment Driver 15 |  |  |
| volFcstAdjDrvr_16 | FLOAT64 | Volume Forecast Adjustment Driver 16 |  |  |
| volFcstAdjDrvr_17 | FLOAT64 | Volume Forecast Adjustment Driver 17 |  |  |
| volFcstAdjDrvr_18 | FLOAT64 | Volume Forecast Adjustment Driver 18 |  |  |
| volFcstAdjDrvr_19 | FLOAT64 | Volume Forecast Adjustment Driver 19 |  |  |
| volFcstAdjDrvr_20 | FLOAT64 | Volume Forecast Adjustment Driver 20 |  |  |
| volFcstAdjDrvr_21 | FLOAT64 | Volume Forecast Adjustment Driver 21 |  |  |
| volFcstAdjDrvr_22 | FLOAT64 | Volume Forecast Adjustment Driver 22 |  |  |
| volFcstAdjDrvr_23 | FLOAT64 | Volume Forecast Adjustment Driver 23 |  |  |
| volFcstAdjDrvr_24 | FLOAT64 | Volume Forecast Adjustment Driver 24 |  |  |
| volFcstAdjDrvr_25 | FLOAT64 | Volume Forecast Adjustment Driver 25 |  |  |
| volFcstOrigDrvr_1 | FLOAT64 | Volume Forecast Original Driver 1 |  |  |
| volFcstOrigDrvr_2 | FLOAT64 | Volume Forecast Original Driver 2 |  |  |
| volFcstOrigDrvr_3 | FLOAT64 | Volume Forecast Original Driver 3 |  |  |
| volFcstOrigDrvr_4 | FLOAT64 | Volume Forecast Original Driver 4 |  |  |
| volFcstOrigDrvr_5 | FLOAT64 | Volume Forecast Original Driver 5 |  |  |
| volFcstOrigDrvr_6 | FLOAT64 | Volume Forecast Original Driver 6 |  |  |
| volFcstOrigDrvr_7 | FLOAT64 | Volume Forecast Original Driver 7 |  |  |
| volFcstOrigDrvr_8 | FLOAT64 | Volume Forecast Original Driver 8 |  |  |
| volFcstOrigDrvr_9 | FLOAT64 | Volume Forecast Original Driver 9 |  |  |
| volFcstOrigDrvr_10 | FLOAT64 | Volume Forecast Original Driver 10 |  |  |
| volFcstOrigDrvr_11 | FLOAT64 | Volume Forecast Original Driver 11 |  |  |
| volFcstOrigDrvr_12 | FLOAT64 | Volume Forecast Original Driver 12 |  |  |
| volFcstOrigDrvr_13 | FLOAT64 | Volume Forecast Original Driver 13 |  |  |
| volFcstOrigDrvr_14 | FLOAT64 | Volume Forecast Original Driver 14 |  |  |
| volFcstOrigDrvr_15 | FLOAT64 | Volume Forecast Original Driver 15 |  |  |
| volFcstOrigDrvr_16 | FLOAT64 | Volume Forecast Original Driver 16 |  |  |
| volFcstOrigDrvr_17 | FLOAT64 | Volume Forecast Original Driver 17 |  |  |
| volFcstOrigDrvr_18 | FLOAT64 | Volume Forecast Original Driver 18 |  |  |
| volFcstOrigDrvr_19 | FLOAT64 | Volume Forecast Original Driver 19 |  |  |
| volFcstOrigDrvr_20 | FLOAT64 | Volume Forecast Original Driver 20 |  |  |
| volFcstOrigDrvr_21 | FLOAT64 | Volume Forecast Original Driver 21 |  |  |
| volFcstOrigDrvr_22 | FLOAT64 | Volume Forecast Original Driver 22 |  |  |
| volFcstOrigDrvr_23 | FLOAT64 | Volume Forecast Original Driver 23 |  |  |
| volFcstOrigDrvr_24 | FLOAT64 | Volume Forecast Original Driver 24 |  |  |
| volFcstOrigDrvr_25 | FLOAT64 | Volume Forecast Original Driver 25 |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |

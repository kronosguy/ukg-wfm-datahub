# vUnpvtActualVolumeIntra

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtActualVolumeIntra |
| Unique Identifier | partitionDate,orgId,time_24h |
| Source Pipeline | summaryIntra (DR) |

## Columns

**Column count:** 32

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| time_24H | TIME | 24H Time |  |  |
| volActDrvr_1 | FLOAT64 | Volume Actual Driver 1 |  |  |
| volActDrvr_2 | FLOAT64 | Volume Actual Driver 2 |  |  |
| volActDrvr_3 | FLOAT64 | Volume Actual Driver 3 |  |  |
| volActDrvr_4 | FLOAT64 | Volume Actual Driver 4 |  |  |
| volActDrvr_5 | FLOAT64 | Volume Actual Driver 5 |  |  |
| volActDrvr_6 | FLOAT64 | Volume Actual Driver 6 |  |  |
| volActDrvr_7 | FLOAT64 | Volume Actual Driver 7 |  |  |
| volActDrvr_8 | FLOAT64 | Volume Actual Driver 8 |  |  |
| volActDrvr_9 | FLOAT64 | Volume Actual Driver 9 |  |  |
| volActDrvr_10 | FLOAT64 | Volume Actual Driver 10 |  |  |
| volActDrvr_11 | FLOAT64 | Volume Actual Driver 11 |  |  |
| volActDrvr_12 | FLOAT64 | Volume Actual Driver 12 |  |  |
| volActDrvr_13 | FLOAT64 | Volume Actual Driver 13 |  |  |
| volActDrvr_14 | FLOAT64 | Volume Actual Driver 14 |  |  |
| volActDrvr_15 | FLOAT64 | Volume Actual Driver 15 |  |  |
| volActDrvr_16 | FLOAT64 | Volume Actual Driver 16 |  |  |
| volActDrvr_17 | FLOAT64 | Volume Actual Driver 17 |  |  |
| volActDrvr_18 | FLOAT64 | Volume Actual Driver 18 |  |  |
| volActDrvr_19 | FLOAT64 | Volume Actual Driver 19 |  |  |
| volActDrvr_20 | FLOAT64 | Volume Actual Driver 20 |  |  |
| volActDrvr_21 | FLOAT64 | Volume Actual Driver 21 |  |  |
| volActDrvr_22 | FLOAT64 | Volume Actual Driver 22 |  |  |
| volActDrvr_23 | FLOAT64 | Volume Actual Driver 23 |  |  |
| volActDrvr_24 | FLOAT64 | Volume Actual Driver 24 |  |  |
| volActDrvr_25 | FLOAT64 | Volume Actual Driver 25 |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |

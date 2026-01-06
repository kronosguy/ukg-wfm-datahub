# vUnpvtVolumeBudget

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtVolumeBudget |
| Unique Identifier | partitionDate,orgId,currencyId |
| Source Pipeline |  |

## Columns

**Column count:** 33

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| currency | STRING | Curency Type |  |  |
| currencyId | INT64 | Currency ID |  |  |
| volBdgtDrvr_1 | FLOAT | Volume Budget Driver 1 |  |  |
| volBdgtDrvr_2 | FLOAT | Volume Budget Driver 2 |  |  |
| volBdgtDrvr_3 | FLOAT | Volume Budget Driver 3 |  |  |
| volBdgtDrvr_4 | FLOAT | Volume Budget Driver 4 |  |  |
| volBdgtDrvr_5 | FLOAT | Volume Budget Driver 5 |  |  |
| volBdgtDrvr_6 | FLOAT | Volume Budget Driver 6 |  |  |
| volBdgtDrvr_7 | FLOAT | Volume Budget Driver 7 |  |  |
| volBdgtDrvr_8 | FLOAT | Volume Budget Driver 8 |  |  |
| volBdgtDrvr_9 | FLOAT | Volume Budget Driver 9 |  |  |
| volBdgtDrvr_10 | FLOAT | Volume Budget Driver 10 |  |  |
| volBdgtDrvr_11 | FLOAT | Volume Budget Driver 11 |  |  |
| volBdgtDrvr_12 | FLOAT | Volume Budget Driver 12 |  |  |
| volBdgtDrvr_13 | FLOAT | Volume Budget Driver 13 |  |  |
| volBdgtDrvr_14 | FLOAT | Volume Budget Driver 14 |  |  |
| volBdgtDrvr_15 | FLOAT | Volume Budget Driver 15 |  |  |
| volBdgtDrvr_16 | FLOAT | Volume Budget Driver 16 |  |  |
| volBdgtDrvr_17 | FLOAT | Volume Budget Driver 17 |  |  |
| volBdgtDrvr_18 | FLOAT | Volume Budget Driver 18 |  |  |
| volBdgtDrvr_19 | FLOAT | Volume Budget Driver 19 |  |  |
| volBdgtDrvr_20 | FLOAT | Volume Budget Driver 20 |  |  |
| volBdgtDrvr_21 | FLOAT | Volume Budget Driver 21 |  |  |
| volBdgtDrvr_22 | FLOAT | Volume Budget Driver 22 |  |  |
| volBdgtDrvr_23 | FLOAT | Volume Budget Driver 23 |  |  |
| volBdgtDrvr_24 | FLOAT | Volume Budget Driver 24 |  |  |
| volBdgtDrvr_25 | FLOAT | Volume Budget Driver 25 |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |

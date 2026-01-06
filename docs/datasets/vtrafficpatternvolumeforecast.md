# vTrafficPatternVolumeForecast

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- Introduced DH 8.0 Release

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTrafficPatternVolumeForecast |
| Unique Identifier | partitionDate,orgId,time_24h,currencyCode |
| Source Pipeline | trafficPatternForecast (DR) |

## Columns

**Column count:** 57

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| currencyCode | STRING | Currency Code |  |  |
| time_24h | STRING | 24H Time |  |  |
| trafPatVolFcstAdj_Drvr1 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr2 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr3 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr4 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr5 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr6 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr7 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr8 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr9 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr10 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr11 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr12 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr13 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr14 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr15 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr16 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr17 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr18 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr19 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr20 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr21 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr22 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr23 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr24 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstAdj_Drvr25 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstAdjDrvr_? else vUnpvtVolumeForecast.volFcstAdjDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr1 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr2 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr3 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr4 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr5 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr6 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr7 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr8 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr9 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr10 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr11 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr12 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr13 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr14 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr15 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr16 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr17 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr18 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr19 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr20 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr21 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr22 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr23 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr24 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| trafPatVolFcstGen_Drvr25 | FLOAT | if vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? <> null then vUnpvtTrafficPatternForecast.trafPatFcstDrvr_? * vUnpvtVolumeForecast.volFcstGenDrvr_? else vUnpvtVolumeForecast.volFcstGenDrvr_?/96 |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |
| currencyExchangeRates | STRING | a string value that contains the available currency and exchange rate needed for calculations |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |

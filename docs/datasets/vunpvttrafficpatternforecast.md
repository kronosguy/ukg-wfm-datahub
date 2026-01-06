# vUnpvtTrafficPatternForecast

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

- Introduced in DH Release 8.0

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtTrafficPatternForecast |
| Unique Identifier | partitionDate,orgId, volumeDriverId |
| Source Pipeline | summaryIntra (DR), trafficPatternForecast (DR) |

## Columns

**Column count:** 30

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| time_24H | STRING | time in 15 min segment |  |  |
| trafPatFcstDrvr_1 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_2 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_3 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_4 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_5 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_6 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_7 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_8 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_9 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_10 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_11 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_12 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_13 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_14 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_15 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_16 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_17 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_18 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_19 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_20 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_21 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_22 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_23 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_24 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| trafPatFcstDrvr_25 | FLOAT | Interval percentage for volume associated volume driver id |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |

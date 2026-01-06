# vTrafficPatternForecast

**Group:** Detail Dataset → Forecasting Detail Views

Traffic patterns are the basis for allocating day level volume forecast amount to 15 minute intra day allocations.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vTrafficPatternForecast |
| Unique Identifier | partitionDate,orgId,volumeDriverId,startTime,endTime |
| Source Pipeline | trafficPatternForecast (DR) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | The date associated with a traffic pattern per day object |  |  |
| orgId | INT64 | Business structure org id |  |  |
| volumeDriverId | INT64 | Volume Driver Assignment ID |  |  |
| startTime | TIME | Interval Start Time |  |  |
| endTime | TIME | Interval End Time |  |  |
| intervalPct | FLOAT | Forecast percentage |  |  |
| updateDtm | DATETIME | Date time row was updated. |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |

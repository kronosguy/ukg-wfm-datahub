# vVolumeForecast

**Group:** Detail Dataset → Forecasting Detail Views

Volume Forecast (Adjusted and Generated) - Daily by Category

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vVolumeForecast |
| Unique Identifier | partitionDate,orgId,volumeDriverId,volumeTypeId |
| Source Pipeline | volumeForecast (CDC) |

## Columns

**Column count:** 13

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| volumeType | STRING | Options: GENERATED (forecasted), ADJUSTED or CHANGE. |  |  |
| volumeTypeId | INT64 | Volume type ID |  |  |
| currency | STRING | Currency code if volume driver is currency amount, null if not |  |  |
| currencyId | INT64 | Currency ID |  |  |
| eventRatio | FLOAT64 | Event Ratio |  |  |
| dailyAmount | FLOAT64 | Volume driver amount |  |  |
| volumeDriver | STRING | The volume driver the amount is associated with. Examples: sales, units, traffic |  |  |
| volumeDriverId | INT64 | Volume driver ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
| linkedCategoryType | STRING | a string value Primary or Secondary identifying how the org was defined in Dimensions.  This field can used to filter on the org you wish to include in your totals. |  |  |
| includeSummarySwt | BOOLEAN | determines which nodes will appear vKronosDaySummary .  It’s based on linked_category_configuration |  |  |

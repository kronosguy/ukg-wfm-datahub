# vLaborForecast

**Group:** Detail Dataset → Forecasting Detail Views

Forecasted Labor (Retail), for each JOB in the Business Structure.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborForecast |
| Unique Identifier | partitionDate,orgId,laborForecastTypeName |
| Source Pipeline | laborForecast (DR) |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| laborForecastTypeName | STRING | Forecast type (i.e. ADJUSTED, GENERATED, RAW) |  |  |
| dailyHrs | FLOAT64 | Forecast hours |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

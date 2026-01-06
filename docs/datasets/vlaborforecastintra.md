# vLaborForecastIntra

**Group:** Detail Dataset → Forecasting Detail Views

Forecasted Labor (Retail), for each JOB in the Business Structure. - 15Min Grain

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vLaborForecastIntra |
| Unique Identifier | partitionDate,orgId,laborForecastTypeName,startTime,endTime |
| Source Pipeline | laborForecast (DR) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| laborForecastTypeName | STRING | Forecast type (i.e. ADJUSTED, GENERATED, RAW) Note: laborForecastTypeName='EARNED' ** Do Not Use this value is not available or inaccurate ** |  |  |
| startTime | TIME | Start date/time for span labor forecast |  |  |
| endTime | TIME | End date/time for span labor forecast |  |  |
| incrementHdCnt | FLOAT64 | Head count of forecast workers for span |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

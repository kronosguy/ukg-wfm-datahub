# vValLaborForecast

**Group:** Detail Dataset → Data Detail Validation

Validation Labor Forecast Data sourced from IA

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vValLaborForecast |
| Unique Identifier | partitionDate,orgId |
| Source Pipeline | valLaborForecast (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| laborForecastHrs | FLOAT | Labor forecast Daily Hours |  |  |
| updateDtm | DATETIME | The date/time stamp of when the row was inserted into Data Hub – BigQuery |  |  |

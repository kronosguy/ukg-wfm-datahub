# vDtlLaborForecastByRow

**Group:** Detail Dataset → Data Detail Validation

Labor forecast amounts by org and date

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDtlLaborForecastByRow |
| Unique Identifier | partitionDate,orgId,smryOrgId |
| Source Pipeline | valLaborForecast (DR) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| PartitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| valOrgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension from valLaborForecast |  |  |
| smryOrgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension from vLaborForecast |  |  |
| valLaborForecastHrs | FLOAT | Total Hours from valLaborForecast |  |  |
| dtlPartitionDate | DATE | Represents apply date of transaction - use to join to date dimension from vLaborForecast |  |  |
| dtlLaborForecastHrs | FLOAT | Total Hours from vLaborForecast |  |  |

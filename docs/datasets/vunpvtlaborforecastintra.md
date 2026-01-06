# vUnpvtLaborForecastIntra

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtLaborForecastIntra |
| Unique Identifier | partitionDate,orgId,time_24h |
| Source Pipeline | summaryIntra (DR), laborForecast (CDC) |

## Columns

**Column count:** 16

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| time_24H | TIME | 24H Time |  |  |
| lbrfcstHC_Adjusted | FLOAT64 | Labor Forecast Headcount Adjusted |  |  |
| lbrfcstHrs_Adjusted | FLOAT64 | Labor Forecast Hours Adjusted |  |  |
| lbrfcstHC_SystemAdjusted | FLOAT64 | Labor Forecast Hours System Adjusted |  |  |
| lbrfcstHrs_SystemAdjusted | FLOAT64 | Labor Forecast Hours System Adjusted |  |  |
| lbrfcstHC_Raw | FLOAT64 | Labor Forecast Headcount Raw |  |  |
| lbrfcstHrs_Raw | FLOAT64 | Labor Forecast Hours Raw |  |  |
| lbrfcstHC_Generated | FLOAT64 | Labor Forecast Headcount Generated |  |  |
| lbrfcstHrs_Generated | FLOAT64 | Labor Forecast Hours Generated |  |  |
| lbrfcstHC_Unallocated | FLOAT64 | Labor Forecast Headcount  Unallocated |  |  |
| lbrfcstHrs_Unallocated | FLOAT64 | Labor Forecast Hours Unallocated |  |  |
| lbrfcstHC_Earned | FLOAT64 | Earned Hours are currently not available for 15 minute interval but this column is a placeholder for future development |  |  |
| lbrfcstHrs_Earned | FLOAT64 | Earned Hours are currently not available for 15 minute interval but this column is a placeholder for future development |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

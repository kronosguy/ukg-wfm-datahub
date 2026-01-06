# vUnpvtLaborForecast

**Group:** Summary Dataset → metricsIntra (vKronosIntraSummary)

-

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vUnpvtLaborForecast |
| Unique Identifier | partitionDate,orgId |
| Source Pipeline |  |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| orgId | INT64 | Unique ID of Business Structure location - joins to Business Structure Dimension |  |  |
| lbrfcstHrs_Adjusted | FLOAT64 | Labor Forecast Hours Adjusted |  |  |
| lbrfcstHrs_SystemAdjusted | FLOAT64 | Labor Forecast Hours System Adjusted |  |  |
| lbrfcstHrs_Raw | FLOAT64 | Labor Forecast Hours Raw |  |  |
| lbrfcstHrs_Generated | FLOAT64 | Labor Forecast Hours Generated |  |  |
| lbrfcstHrs_Unallocated | FLOAT64 | Labor Forecast Hours Unallocated |  |  |
| lbrfcstHrs_Earned | FLOAT64 | Labor Forecast Hours Earned |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

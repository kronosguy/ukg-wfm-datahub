# vDtlLaborForecastByMonth

**Group:** Detail Dataset → Data Detail Validation

Labor Forecast row counts by month (IA vs Data Hub Detail)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDtlLaborForecastByMonth |
| Unique Identifier | yearMonth |
| Source Pipeline | valLaborForecast (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| yearMonth | STRING | Labor Forecast Year and Month Loaded |  |  |
| dtlDiffRowCount | INT64 | Number of rows difference from vLaborForecast |  |  |
| allRowCount | INT64 | Total row count (allRowCount) |  |  |
| perCentDiff | FLOAT | Percent difference from vScheduledTotal |  |  |

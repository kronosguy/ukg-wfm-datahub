# vDtlScheduledTotalByMonth

**Group:** Detail Dataset → Data Detail Validation

Scheduled Total row counts by month (IA vs Data Hub Detail)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDtlScheduledTotalByMonth |
| Unique Identifier | yearMonth |
| Source Pipeline | valScheduledTotal (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| yearMonth | STRING | Scheduled Total Year and Month Loaded |  |  |
| DtlDiffRowCount | INT64 | Number of rows difference from vScheduleTotal |  |  |
| allRowCount | INT64 | Total row count (allRowCount) |  |  |
| perCentDiff | FLOAT | Percent difference from vTimecardTotal |  |  |

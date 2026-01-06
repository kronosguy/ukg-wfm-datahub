# vSmryTimecardTotalByMonth

**Group:** Detail Dataset → Data Detail Validation

Timecard Total hours and amounts by month (IA vs Data Hub Summary)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vSmryTimecardTotalByMonth |
| Unique Identifier | yearMonth |
| Source Pipeline | valScheduledTotal (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| yearMonth | STRING | Timecard Total Year and Month Loaded |  |  |
| SmryDiffRowCount | INT64 | Number of rows difference from vTimecardTotal |  |  |
| allRowCount | INT64 | Total row count (allRowCount) |  |  |
| perCentDiff | FLOAT | Percent difference from vTimecardTotal |  |  |

# vDtlTimecardTotalByMonth

**Group:** Detail Dataset → Data Detail Validation

Timecard total row counts by month  (IA vs Data Hub Detail)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vDtlTimecardTotalByMonth |
| Unique Identifier | yearMonth |
| Source Pipeline | valTimecardTotal (DR) |

## Columns

**Column count:** 4

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| yearMonth | STRING | Timecard Total Year and Month Loaded |  |  |
| DtlDiffRowCount | INT64 | Number of rows difference from vTimecardTotal |  |  |
| allRowCount | INT64 | Total row count (allRowCount) |  |  |
| perCentDiff | FLOAT | Percent difference from vTimecardTotal |  |  |

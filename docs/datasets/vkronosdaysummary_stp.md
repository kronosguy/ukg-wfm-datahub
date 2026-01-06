# vKronosDaySummary_STP

**Group:** Summary Dataset → Volume Forecast Metrics (M_Volfcst)

Same as vKronosDailySummary but includes the "STPName" field.  All data in this view is replicated to all STP's, so you would filter each metric or graph in your visualization tool on the STPName field.  

There is an "All Dates" STP which, when filtered, provides all data so that you can utilize this view exactly as you would the above, in the same report.

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vKronosDaySummary_STP |
| Unique Identifier |  |
| Source Pipeline | view on view vKronosDailySummary |
| Scrubbing | None, Originates from source Views naturally |

## Columns

**Column count:** 1

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| STPName | STRING | Symbolic Time Period Name |  |  |

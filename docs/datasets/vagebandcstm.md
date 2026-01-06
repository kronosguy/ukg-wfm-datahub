# vAgeBandCstm

**Group:** Detail Dataset → Org Structure Detail Views

This view would need to be loaded by the customer - not populated by default

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAgeBandCstm |
| Unique Identifier | age |
| Source Pipeline | This data is populated as silver data. Loaded via BQ Cloud Function |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| age | INT64 | Age - employee age |  |  |
| ageBandCstm1 | STRING | Custom age band 1 |  |  |
| ageBandCstm2 | STRING | Custom age band 2 |  |  |
| sortOrderCstm1 | INT64 | Custom sort order 1 |  |  |
| sortOrderCstm2 | INT64 | Custom sort order 1 |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

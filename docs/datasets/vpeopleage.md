# vPeopleAge

**Group:** Detail Dataset → People Detail Views

- Person ages and age bands calculated for days in partition date

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleAge |
| Unique Identifier | personId,partitionDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| Age_age | INT64 | Employee age | PII |  |
| Age_ageBand | STRING | Age band | PII |  |
| Age_ageBandCstm1 | STRING | Custom age band 1 | PII |  |
| Age_ageBandCstm2 | STRING | Custom age band 2 | PII |  |
| Age_sortOrderCstm1 | INT64 | Custom sort order for custom age band 1 |  |  |
| Age_sortOrderCstm2 | INT64 | Custom sort order of custom age band 2 |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

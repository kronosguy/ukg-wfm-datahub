# vPeopleCustomDate

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - Custom Dates (Used in Accruals)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleCustomDate |
| Unique Identifier | personId,customDateTypeId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| overrideDate | STRING | Override date |  |  |
| dateName | STRING | Name of custom date | PII |  |
| description | STRING | Custom date description | PII |  |
| defaultDate | STRING | Default date | PII |  |
| customDateTypeId | INT64 | Custom date type ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

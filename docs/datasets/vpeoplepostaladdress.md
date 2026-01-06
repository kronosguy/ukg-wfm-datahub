# vPeoplePostalAddress

**Group:** Detail Dataset → People Detail Views

- Non-Effective Dated - Addresses

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeoplePostalAddress |
| Unique Identifier | personId,contactTypeId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 9

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| zipCode | STRING | Zip code | PII | Needed for GEO Analysis |
| state | STRING | State | PII | BLANK |
| contactTypeId | INT64 | contact type ID |  |  |
| contactType | STRING | Contact type | PII | BLANK |
| street | STRING | Street | PII | BLANK |
| country | STRING | Country | PII | BLANK |
| city | STRING | City | PII | BLANK |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  | BLANK |

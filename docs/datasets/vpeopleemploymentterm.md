# vPeopleEmploymentTerm

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Employment Term Profile Assignments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleEmploymentTerm |
| Unique Identifier | personId,employmentTermId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| employmentTermId | INT64 | Employment term ID |  |  |
| expirationDate | DATE | Expiration Date |  |  |
| employmentTerm | STRING | Employment term |  |  |
| effectiveDate | DATE | Effective date |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

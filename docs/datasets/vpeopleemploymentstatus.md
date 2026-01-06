# vPeopleEmploymentStatus

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Employment Status (Active, Inactive, Terminated)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleEmploymentStatus |
| Unique Identifier | personId,employmentStatusTypeId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| employmentStatusTypeId | INT64 | Employment status type ID |  |  |
| expirationDate | DATE | Expiration Date |  |  |
| employmentStatus | STRING | Employment status - active, inactive, terminated |  |  |
| effectiveDate | DATE | Effective date of status |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

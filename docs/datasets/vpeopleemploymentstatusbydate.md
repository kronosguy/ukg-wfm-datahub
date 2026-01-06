# vPeopleEmploymentStatusByDate

**Group:** Detail Dataset → People Detail Views

- Employment Status by Date (Active, Inactive, Terminated)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleEmploymentStatusByDate |
| Unique Identifier | personId,partitionDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 5

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| partitionDate | DATE | Represents apply date of transaction - use to join to date dimension |  |  |
| personId | INT64 | Used to join to people dimension |  |  |
| employmentStatus | STRING | Employment status |  |  |
| primaryOrgId | INT64 | Unique identifier of Primary Business Structure location of the employee associated with the transaction - Joins to Business Structure dimensions |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

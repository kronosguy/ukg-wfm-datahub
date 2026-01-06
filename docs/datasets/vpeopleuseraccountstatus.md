# vPeopleUserAccountStatus

**Group:** Detail Dataset → People Detail Views

- Effective Dated - User Account Status (Active, Inactive, Terminated) (For logging into WFD)

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleUserAccountStatus |
| Unique Identifier | personId,accountStatusTypeId,effectiveDate,expirationDate |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 6

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| effectiveDate | DATE | User account status effective date |  |  |
| expirationDate | DATE | User account status expiration date |  |  |
| accountStatusTypeId | INT64 | Account status type ID |  |  |
| accountStatus | STRING | Account status |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

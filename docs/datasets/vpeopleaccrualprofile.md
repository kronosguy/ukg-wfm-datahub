# vPeopleAccrualProfile

**Group:** Detail Dataset → People Detail Views

- Effective Dated - Accrual Profile Assignments

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vPeopleAccrualProfile |
| Unique Identifier | personId,accrualProfileId,accrualProfileAssignmentId |
| Source Pipeline | people (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | Used to join to people dimension |  |  |
| expirationDate | DATE | Expiration date |  |  |
| effectiveDate | DATE | Effective Date |  |  |
| accrualProfileName | STRING | Accrual profile name |  |  |
| accrualProfileAssignmentId | INT64 | Accrual profile assignement ID |  |  |
| accrualProfileId | INT64 | Accrual profile ID |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |

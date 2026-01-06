# vAssignmentAccrualProfiles

**Group:** Detail Dataset → Assignment Detail Views

## Metadata

| Field | Value |
| --- | --- |
| Dataset / View / Table | vAssignmentAccrualProfiles |
| Unique Identifier |  |
| Source Pipeline | peoplePositions (CDC) |

## Columns

**Column count:** 7

| Column | Data Type | Description | PII/Confidential | Scrubbing |
| --- | --- | --- | --- | --- |
| personId | INT64 | id of the employee to which that particular position is assigned |  |  |
| assignmentId | INT64 | id of a particular assignment |  |  |
| accrualProfileId | INT64 | id of the accrual profile assigned in a particular position |  |  |
| accrualProfileName | STRING | name of that particular accrual profile |  |  |
| effectiveDate | DATE | date when a specific accrual profile becomes effective. |  |  |
| expirationDate | DATE | date when a specific accrual profile expires. |  |  |
| updateDtm | DATETIME | The UTC date/time stamp of when the row was inserted or updated in BigQuery |  |  |
